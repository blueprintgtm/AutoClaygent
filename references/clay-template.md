# Clay Template

Copy this template into your Clay workspace:

**https://app.clay.com/shared-workbook/share_0t8b7fh5xNR57ptm4R2**

---

## What's Included

This template is pre-configured with:

1. **Webhook Receiver Column** - Receives prompt data from Claude
2. **Claygent Column** - Runs the AI agent with your prompt
3. **JSON Parser Formula** - Extracts structured data from Claygent response
4. **HTTP Callback Action** - Sends results back to Claude for evaluation

---

## Setup Instructions

1. Click the link above to open the template
2. Click "Copy to my workspace" in Clay
3. Find the Webhook column and copy its unique URL (looks like `https://app.clay.com/api/v1/webhooks/...`)
4. Give that URL to Claude - everything else is automatic!

---

## Template Structure

| Column | Type | Purpose |
|--------|------|---------|
| row_id | Text | Unique identifier for tracking |
| domain | Text | Company domain to research |
| prompt | Text | The Claygent prompt to run |
| Claygent | AI Agent | Runs the prompt, returns JSON |
| Parsed Output | Formula | Extracts JSON from response |
| HTTP Callback | Action | POSTs results back to Claude |

---

## Troubleshooting

**Results not appearing:**
- Claude handles the webhook server and tunnel automatically
- Make sure the Claygent column ran successfully (not errored)
- Check that the HTTP Callback column shows "Success"

**Claygent errors:**
- Check that your API key is configured in Clay settings
- Verify the prompt is valid (no syntax errors)
- Try running a single row first to debug
