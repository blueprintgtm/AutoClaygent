# Technology Finder

Detect technology stacks across thousands of websites automatically.

## What It Does

Technology Finder is a bulk HTML fetching and fingerprint detection system that:

1. **Downloads HTML** from thousands of websites using async concurrent connections
2. **Handles failures gracefully** with Apify cloud fallback for blocked sites
3. **Scans for technologies** using regex fingerprint patterns
4. **Outputs structured results** as CSV for easy analysis

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your CSV file with a 'website' or 'domain' column
cp your_domains.csv .

# 3. Run the full workflow
python scripts/orchestrator.py --input your_domains.csv
```

Results will be in `./results/fingerprint_detections.csv`

## Performance

- **Local fetcher:** ~100 domains/second (100 concurrent connections)
- **Apify fallback:** ~50 domains/second (cloud, bypasses bot detection)
- **Fingerprint scan:** ~1,000 files/second (8 parallel workers)

Example: 10,000 domains in ~15 minutes

## Scripts

### `html_fetcher.py` - Local Bulk Fetcher

Downloads HTML from all domains in your CSV. Fast and free.

```bash
python scripts/html_fetcher.py --input domains.csv
python scripts/html_fetcher.py --input domains.csv --test 50        # Test mode
python scripts/html_fetcher.py --input domains.csv -c 200 -t 5      # Faster
```

Features:
- HTTPS-first with HTTP fallback
- Gzip compression (90%+ storage savings)
- Resume-capable (skips cached domains)
- Exports failed domains for Apify fallback

### `apify_fetcher.py` - Cloud Fallback

Uses Apify's Cheerio Scraper for domains that block local requests.

```bash
# Set your API key
export APIFY_API_KEY=your_key_here

# Or use config file
cp config/apify_config.example.json config/apify_config.json

# Run
python scripts/apify_fetcher.py
python scripts/apify_fetcher.py --test 10                           # Test first
python scripts/apify_fetcher.py --resume RUN_ID                     # Resume
```

Cost: ~$0.25-0.50 per 1,000 URLs with datacenter proxy

### `fingerprint_scanner.py` - Technology Detection

Scans cached HTML for technology patterns.

```bash
python scripts/fingerprint_scanner.py
python scripts/fingerprint_scanner.py --workers 16                  # More cores
python scripts/fingerprint_scanner.py --fingerprints ./my_patterns/ # Custom
```

Detects 80+ platforms:
- CMS: WordPress, Shopify, Wix, Squarespace, Webflow...
- Analytics: Google Analytics, Hotjar, Mixpanel, Segment...
- Marketing: HubSpot, Marketo, Mailchimp, Klaviyo...
- Chat: Intercom, Drift, Zendesk, Freshchat...
- E-commerce: Stripe, PayPal, WooCommerce...
- And more...

### `orchestrator.py` - Full Workflow

Runs all three scripts in sequence.

```bash
python scripts/orchestrator.py --input domains.csv
python scripts/orchestrator.py --input domains.csv --use-apify      # Include cloud
python scripts/orchestrator.py --skip-fetch                          # Scan only
```

## Custom Fingerprints

Create your own detection patterns in `fingerprints/patterns/`:

```python
# fingerprints/patterns/my_industry.py
import re

FINGERPRINTS = {
    'competitor_a': re.compile(r'competitor-a\.com|competitora-widget', re.I),
    'competitor_b': re.compile(r'competitor-b\.js|data-competitorb', re.I),
    'industry_tool': re.compile(r'industrytool\.io', re.I),
}
```

Then run with your custom patterns:

```bash
python scripts/fingerprint_scanner.py --fingerprints ./fingerprints/patterns/
```

## Output Files

After running, you'll find:

```
results/
  fingerprint_detections.csv    # Per-domain results
  fingerprint_summary.json      # Aggregate statistics
  workflow_summary.json         # Run metadata

html_cache/
  *.html.gz                     # Compressed HTML files
  progress.json                 # Resume tracking
  failed_domains.txt            # For Apify retry
```

## CSV Format

The `fingerprint_detections.csv` includes:

| Column | Description |
|--------|-------------|
| domain | Website domain |
| primary_cms | Most likely CMS platform |
| primary_marketing | Most likely marketing platform |
| detected | Pipe-separated list of all detected technologies |
| detection_count | Total number of technologies found |
| categories | JSON of technologies by category |
| html_size | Size of cached HTML |

## Apify Setup

1. Create account at [apify.com](https://apify.com)
2. Get API key from Settings > API Keys
3. Set environment variable or config file:

```bash
# Option 1: Environment variable
export APIFY_API_KEY=apify_api_xxxxx

# Option 2: Config file
cp config/apify_config.example.json config/apify_config.json
# Edit and add your key
```

Recommended plan: $49/mo (Personal) or $99/mo (Team) for datacenter proxy access.

## Real-World Results

**ChiroHD Case Study:**
- Input: 15,000 chiropractic practice websites
- Local success rate: 82%
- With Apify fallback: 97%
- Technologies detected: 2,500+ platform instances
- Primary use: Competitor detection and market analysis

## Requirements

- Python 3.10+
- pandas, aiohttp, aiofiles, requests
- Optional: Apify account for cloud fallback

## Tips

1. **Start small**: Use `--test 100` to verify your CSV format
2. **Check failures**: Review `html_cache/failed_domains.txt` before using Apify
3. **Custom patterns**: Industry-specific patterns improve detection accuracy
4. **Incremental**: Run fetcher multiple times - it skips cached domains
5. **Parallel workers**: Increase `--workers` on machines with more CPU cores
