"""
Claygent Builder - Local Webhook Server

Receives results from Clay's HTTP Action and stores them for evaluation.
Used by the claygent-build skill to test and improve Claygent prompts.

Usage:
    python webhook_server.py              # Starts on port 8765
    python webhook_server.py --port 9000  # Custom port

Endpoints:
    POST /webhook          - Receive Clay results
    GET  /batch/status     - Check current batch status
    POST /batch/start      - Start a new batch (optional)
    POST /batch/complete   - Mark batch as complete
    GET  /results/latest   - Get the latest batch results
"""

import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuration
RESULTS_DIR = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Current batch state
current_batch = {
    "id": None,
    "started_at": None,
    "results": [],
    "expected_count": None,
}


def get_batch_file(batch_id: str) -> Path:
    """Get the file path for a batch."""
    return RESULTS_DIR / f"batch_{batch_id}.json"


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Receive a single result from Clay's HTTP Action.

    FIXED STRUCTURE - Claude → Clay Webhook (5 fields only):
    {
        "row_id": "...",                 # Unique identifier for this row
        "prompt": "...",                 # COMPLETE prompt with all data embedded
        "prompt_version": "...",         # Version ID like "signup-v1.2"
        "change_log": "...",             # What changed from last version
        "callback_url": "...",           # URL where Clay sends results back
        "reference_json_text": "..."     # JSON schema as TEXT (not parsed)
    }

    CRITICAL RULES:
    - NO separate data fields (domain, company_name, city, state)
    - ALL input data must be embedded in the prompt field
    - reference_json_text is TEXT prefixed with "PASTE THIS INTO CLAY JSON OUTPUT:"

    Clay → Claude Callback (from HTTP Action):
    {
        "row_id": "...",                 # Matches original row_id
        "prompt_version": "...",         # Which version was used
        "claygent_output": {...}         # Full Claygent response with steps
    }
    """
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": f"Invalid JSON: {e}"}), 400

    # Add metadata
    data["received_at"] = datetime.now().isoformat()

    # Auto-start batch if needed
    if current_batch["id"] is None:
        batch_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        current_batch["id"] = batch_id
        current_batch["started_at"] = datetime.now().isoformat()
        current_batch["results"] = []
        print(f"\n[Batch Started] ID: {batch_id}")

    # Add to current batch
    current_batch["results"].append(data)
    count = len(current_batch["results"])

    # Log receipt
    input_preview = data.get("input", {})
    if isinstance(input_preview, dict):
        preview = input_preview.get("domain", input_preview.get("company", str(input_preview)[:50]))
    else:
        preview = str(input_preview)[:50]
    print(f"  [{count}] Received: {preview}")

    # Auto-save every 5 results
    if count % 5 == 0:
        _save_current_batch()

    return jsonify({
        "status": "received",
        "batch_id": current_batch["id"],
        "result_count": count,
    })


@app.route("/batch/start", methods=["POST"])
def batch_start():
    """
    Start a new batch explicitly.

    Optional payload:
    {
        "expected_count": 20,  # How many results expected
        "name": "tech-stack-test"  # Optional name
    }
    """
    global current_batch

    # Save previous batch if exists
    if current_batch["id"] and current_batch["results"]:
        _save_current_batch()

    # Start new batch
    data = request.get_json(force=True) if request.data else {}
    batch_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    if data.get("name"):
        batch_id = f"{batch_id}_{data['name']}"

    current_batch = {
        "id": batch_id,
        "started_at": datetime.now().isoformat(),
        "results": [],
        "expected_count": data.get("expected_count"),
    }

    print(f"\n[Batch Started] ID: {batch_id}")
    if data.get("expected_count"):
        print(f"  Expected: {data['expected_count']} results")

    return jsonify({
        "status": "started",
        "batch_id": batch_id,
    })


@app.route("/batch/status", methods=["GET"])
def batch_status():
    """Get status of the current batch."""
    if current_batch["id"] is None:
        return jsonify({
            "status": "no_batch",
            "message": "No batch in progress. Send data to /webhook to start.",
        })

    count = len(current_batch["results"])
    expected = current_batch["expected_count"]

    return jsonify({
        "status": "in_progress",
        "batch_id": current_batch["id"],
        "started_at": current_batch["started_at"],
        "result_count": count,
        "expected_count": expected,
        "progress": f"{count}/{expected}" if expected else f"{count} received",
    })


@app.route("/batch/complete", methods=["POST"])
def batch_complete():
    """Mark current batch as complete and save it."""
    if current_batch["id"] is None:
        return jsonify({"error": "No batch in progress"}), 400

    filepath = _save_current_batch()
    batch_id = current_batch["id"]
    result_count = len(current_batch["results"])

    # Reset for next batch
    current_batch["id"] = None
    current_batch["started_at"] = None
    current_batch["results"] = []
    current_batch["expected_count"] = None

    print(f"\n[Batch Complete] {batch_id} - {result_count} results saved")

    return jsonify({
        "status": "completed",
        "batch_id": batch_id,
        "result_count": result_count,
        "file": str(filepath),
    })


@app.route("/results/latest", methods=["GET"])
def results_latest():
    """Get the latest batch results."""
    # Check current batch first
    if current_batch["id"] and current_batch["results"]:
        return jsonify({
            "batch_id": current_batch["id"],
            "status": "in_progress",
            "started_at": current_batch["started_at"],
            "results": current_batch["results"],
        })

    # Otherwise, find most recent file
    batch_files = sorted(RESULTS_DIR.glob("batch_*.json"), reverse=True)
    if not batch_files:
        return jsonify({"error": "No batch results found"}), 404

    with open(batch_files[0]) as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/results/<batch_id>", methods=["GET"])
def results_by_id(batch_id):
    """Get results for a specific batch."""
    filepath = get_batch_file(batch_id)
    if not filepath.exists():
        return jsonify({"error": f"Batch {batch_id} not found"}), 404

    with open(filepath) as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
    })


def _save_current_batch() -> Path:
    """Save the current batch to disk."""
    if not current_batch["id"]:
        return None

    filepath = get_batch_file(current_batch["id"])
    data = {
        "batch_id": current_batch["id"],
        "started_at": current_batch["started_at"],
        "completed_at": datetime.now().isoformat(),
        "result_count": len(current_batch["results"]),
        "results": current_batch["results"],
    }

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    return filepath


def main():
    parser = argparse.ArgumentParser(description="Claygent Builder Webhook Server")
    parser.add_argument("--port", type=int, default=8765, help="Port to listen on")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   ⚠️  DEPRECATION NOTICE ⚠️                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  This local webhook server is DEPRECATED.                    ║
║                                                              ║
║  AutoClaygent now uses Supabase Edge Functions instead.     ║
║  This provides reliable callbacks without tunnel drops.      ║
║                                                              ║
║  See CLAUDE.md Mode 2 for Supabase setup instructions.       ║
║                                                              ║
║  This server is only for offline/airgapped environments.     ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║           Claygent Builder - Webhook Server (Legacy)         ║
╠══════════════════════════════════════════════════════════════╣
║  Listening on: http://{args.host}:{args.port}                      ║
║                                                              ║
║  Endpoints:                                                  ║
║    POST /webhook        - Receive Clay results               ║
║    GET  /batch/status   - Check batch progress               ║
║    POST /batch/complete - Finalize batch                     ║
║    GET  /results/latest - Get latest results                 ║
╚══════════════════════════════════════════════════════════════╝
""")

    app.run(host=args.host, port=args.port, debug=True)


if __name__ == "__main__":
    main()
