#!/usr/bin/env python3
"""
Technology Finder - Bulk HTML Fetcher

Automatically finds CSV files in the current directory, extracts website/domain columns,
and downloads HTML from all websites for technology detection analysis.

Usage:
    python html_fetcher.py [--concurrency 100] [--timeout 10] [--test 50]
    python html_fetcher.py --input domains.csv --output ./my_cache

The tool will:
1. Find all CSV files in the current directory (or use --input)
2. Extract domains/websites from columns like: website, domain, url, site, homepage
3. Download and cache HTML (gzip compressed) to ./html_cache/ (or --output)
4. Track progress and show statistics
"""

import asyncio
import aiohttp
import aiofiles
import gzip
import json
import time
import sys
import argparse
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

# Default paths (can be overridden via CLI)
DEFAULT_CACHE_DIR = Path("./html_cache")

# Default settings
DEFAULT_CONCURRENCY = 100
DEFAULT_TIMEOUT = 10  # seconds

# User agent to avoid blocks
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Column names to look for (case-insensitive)
DOMAIN_COLUMNS = ['website', 'domain', 'url', 'site', 'homepage', 'web', 'company_website', 'company_url']


def find_csv_files(search_dir: Path) -> list[Path]:
    """Find all CSV files in the given directory."""
    return list(search_dir.glob("*.csv"))


def extract_domain(url: str) -> str | None:
    """Extract clean domain from URL or domain string."""
    if not url or not isinstance(url, str):
        return None

    url = url.strip().lower()

    # Skip empty or invalid
    if not url or url in ['nan', 'none', 'null', '']:
        return None

    # Add scheme if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path.split('/')[0]

        # Remove www prefix
        if domain.startswith('www.'):
            domain = domain[4:]

        # Remove port
        domain = domain.split(':')[0]

        # Validate domain format
        if '.' not in domain or len(domain) < 4:
            return None

        # Skip common invalid patterns
        invalid_patterns = ['facebook.com', 'instagram.com', 'twitter.com', 'linkedin.com',
                          'youtube.com', 'google.com', 'yelp.com', 'yellowpages.com']
        if domain in invalid_patterns:
            return None

        return domain
    except Exception:
        return None


def load_domains_from_csvs(search_dir: Path, input_file: Path = None) -> list[str]:
    """Load unique domains from CSV files."""
    import pandas as pd

    if input_file:
        csv_files = [input_file] if input_file.exists() else []
    else:
        csv_files = find_csv_files(search_dir)

    if not csv_files:
        print("No CSV files found!")
        if input_file:
            print(f"Specified file not found: {input_file}")
        else:
            print(f"Looking in: {search_dir}")
        sys.exit(1)

    print(f"\nFound {len(csv_files)} CSV file(s):")
    for f in csv_files:
        print(f"  - {f.name}")

    all_domains = set()

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file, low_memory=False, dtype=str)

            # Find matching columns (case-insensitive)
            matching_cols = []
            for col in df.columns:
                if col.lower().strip() in DOMAIN_COLUMNS:
                    matching_cols.append(col)

            if matching_cols:
                print(f"\n  {csv_file.name}: Found columns {matching_cols}")
                for col in matching_cols:
                    domains = df[col].dropna().apply(extract_domain)
                    valid_domains = [d for d in domains if d]
                    all_domains.update(valid_domains)
                    print(f"    - {col}: {len(valid_domains):,} valid domains")
            else:
                print(f"\n  {csv_file.name}: No domain columns found")
                print(f"    Available columns: {list(df.columns)[:10]}...")

        except Exception as e:
            print(f"\n  {csv_file.name}: Error reading - {e}")

    return list(all_domains)


def get_cached_domains(cache_dir: Path) -> set[str]:
    """Get set of domains already cached."""
    if not cache_dir.exists():
        return set()
    cached = set()
    for f in cache_dir.glob("*.html.gz"):
        # Convert filename back to domain
        domain = f.stem.replace('.html', '').replace('_', '.')
        cached.add(domain)
    return cached


def domain_to_filename(domain: str) -> str:
    """Convert domain to safe filename."""
    return domain.replace('.', '_').replace('/', '_') + '.html.gz'


def load_progress(cache_dir: Path) -> dict:
    """Load progress tracking data."""
    progress_file = cache_dir / "progress.json"
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            return json.load(f)
    return {
        'started_at': datetime.now().isoformat(),
        'completed': 0,
        'failed': 0,
        'errors': {}
    }


def save_progress(progress: dict, cache_dir: Path):
    """Save progress tracking data."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    progress_file = cache_dir / "progress.json"
    with open(progress_file, 'w') as f:
        json.dump(progress, f, indent=2)


async def fetch_domain(
    session: aiohttp.ClientSession,
    domain: str,
    cache_dir: Path,
    timeout: int,
    semaphore: asyncio.Semaphore
) -> dict:
    """
    Fetch HTML from a domain and cache to disk.
    Tries HTTPS first, then HTTP if that fails.
    """
    result = {
        'domain': domain,
        'status': 'pending',
        'url': None,
        'size': 0,
        'error': None,
        'timestamp': datetime.now().isoformat()
    }

    cache_path = cache_dir / domain_to_filename(domain)

    # Skip if already cached
    if cache_path.exists():
        result['status'] = 'cached'
        return result

    async with semaphore:
        html_content = None

        # Try HTTPS first, then HTTP
        for scheme in ['https', 'http']:
            url = f"{scheme}://{domain}"

            try:
                async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=timeout),
                    allow_redirects=True,
                    ssl=False  # Skip SSL verification for speed
                ) as resp:
                    if resp.status == 200:
                        html_content = await resp.text()
                        result['url'] = str(resp.url)
                        break  # Success, don't try HTTP

            except asyncio.TimeoutError:
                result['error'] = f'timeout ({scheme})'
            except aiohttp.ClientError as e:
                result['error'] = f'{type(e).__name__}: {str(e)[:100]}'
            except Exception as e:
                result['error'] = f'{type(e).__name__}: {str(e)[:100]}'

        # Save HTML if we got content
        if html_content:
            try:
                compressed = gzip.compress(html_content.encode('utf-8', errors='ignore'))
                async with aiofiles.open(cache_path, 'wb') as f:
                    await f.write(compressed)
                result['size'] = len(html_content)
                result['status'] = 'success'
            except Exception as e:
                result['status'] = 'error'
                result['error'] = f'Save error: {str(e)[:100]}'
        elif result['error']:
            result['status'] = 'error'
        else:
            result['status'] = 'error'
            result['error'] = 'No content retrieved'

    return result


async def run_fetcher(
    cache_dir: Path,
    search_dir: Path,
    input_file: Path = None,
    concurrency: int = DEFAULT_CONCURRENCY,
    timeout: int = DEFAULT_TIMEOUT,
    test_limit: int = 0
) -> dict:
    """Main fetcher coroutine. Returns summary stats."""
    print(f"\n{'='*60}")
    print("Technology Finder - Bulk HTML Fetcher")
    if test_limit > 0:
        print(f"*** TEST MODE: Only fetching {test_limit} domains ***")
    print(f"{'='*60}")

    # Setup
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Load domains from CSVs
    print("\nScanning for CSV files and extracting domains...")
    all_domains = load_domains_from_csvs(search_dir, input_file)
    print(f"\nTotal unique domains found: {len(all_domains):,}")

    if not all_domains:
        print("\nNo domains found! Make sure your CSV has a column named:")
        print(f"  {', '.join(DOMAIN_COLUMNS)}")
        return {'success': 0, 'errors': 0, 'total': 0}

    # Check what's already cached
    cached = get_cached_domains(cache_dir)
    domains_to_fetch = [d for d in all_domains if d not in cached]
    print(f"Already cached: {len(cached):,}")
    print(f"Remaining to fetch: {len(domains_to_fetch):,}")

    # Apply test limit if specified
    if test_limit > 0:
        domains_to_fetch = domains_to_fetch[:test_limit]
        print(f"Test mode: limited to {len(domains_to_fetch)} domains")

    if not domains_to_fetch:
        print("\nAll domains already cached!")
        print(f"Cache location: {cache_dir}")
        return {'success': len(cached), 'errors': 0, 'total': len(all_domains)}

    # Load progress
    progress = load_progress(cache_dir)

    # Setup session with connection pooling
    connector = aiohttp.TCPConnector(
        limit=concurrency,
        limit_per_host=5,
        ttl_dns_cache=300,
        enable_cleanup_closed=True
    )

    headers = {'User-Agent': USER_AGENT}

    print(f"\nStarting fetch with {concurrency} concurrent connections...")
    print(f"Timeout per request: {timeout}s")
    print("\nProgress:")

    semaphore = asyncio.Semaphore(concurrency)
    start_time = time.time()
    success_count = 0
    error_count = 0
    all_results = []
    batch_size = 500

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        for i in range(0, len(domains_to_fetch), batch_size):
            batch = domains_to_fetch[i:i + batch_size]

            tasks = [
                fetch_domain(session, domain, cache_dir, timeout, semaphore)
                for domain in batch
            ]

            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Process results
            for result in results:
                if isinstance(result, Exception):
                    error_count += 1
                    continue

                all_results.append(result)

                if result['status'] == 'success':
                    success_count += 1
                elif result['status'] == 'error':
                    error_count += 1
                    err_type = result.get('error', 'unknown')[:50]
                    progress['errors'][err_type] = progress['errors'].get(err_type, 0) + 1

            # Progress update
            completed = i + len(batch)
            elapsed = time.time() - start_time
            rate = completed / elapsed if elapsed > 0 else 0
            remaining = len(domains_to_fetch) - completed
            eta = remaining / rate if rate > 0 else 0

            print(f"\r  {completed:,}/{len(domains_to_fetch):,} ({completed/len(domains_to_fetch)*100:.1f}%) | "
                  f"Success: {success_count:,} | Errors: {error_count:,} | "
                  f"Rate: {rate:.1f}/s | ETA: {eta/60:.1f}m", end='', flush=True)

            # Save progress periodically
            progress['completed'] = success_count
            progress['failed'] = error_count
            progress['last_update'] = datetime.now().isoformat()
            save_progress(progress, cache_dir)

    # Save detailed results
    results_file = cache_dir / "fetch_results.json"
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)

    # Save failed domains for Apify fallback
    failed_domains = [r['domain'] for r in all_results if r['status'] == 'error']
    if failed_domains:
        failed_file = cache_dir / "failed_domains.txt"
        with open(failed_file, 'w') as f:
            f.write('\n'.join(failed_domains))
        print(f"\nFailed domains saved to: {failed_file}")
        print(f"Use apify_fetcher.py to retry these with cloud proxy")

    # Final stats
    elapsed = time.time() - start_time
    print(f"\n\n{'='*60}")
    print("COMPLETED")
    print(f"{'='*60}")
    print(f"Total time: {elapsed/60:.1f} minutes")
    print(f"Domains fetched: {success_count:,}")
    print(f"Errors: {error_count:,}")
    if success_count + error_count > 0:
        print(f"Success rate: {success_count/(success_count+error_count)*100:.1f}%")
        print(f"Average rate: {(success_count+error_count)/elapsed:.1f} domains/second")
    print(f"\nCache location: {cache_dir}")
    print(f"Results saved to: {results_file}")

    # Show top error types
    if progress['errors']:
        print("\nTop error types:")
        sorted_errors = sorted(progress['errors'].items(), key=lambda x: x[1], reverse=True)[:10]
        for err, count in sorted_errors:
            print(f"  {count:>5}: {err}")

    save_progress(progress, cache_dir)

    return {
        'success': success_count,
        'errors': error_count,
        'total': len(all_domains),
        'failed_domains': failed_domains
    }


def main():
    parser = argparse.ArgumentParser(
        description='Technology Finder - Bulk HTML Fetcher',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python html_fetcher.py                          # Auto-find CSVs in current dir
  python html_fetcher.py --input domains.csv     # Use specific CSV file
  python html_fetcher.py --output ./my_cache     # Custom output directory
  python html_fetcher.py --test 50               # Test with 50 domains first
  python html_fetcher.py -c 200 -t 5             # Fast mode: 200 concurrent, 5s timeout
        """
    )
    parser.add_argument('--input', '-i', type=str, default=None,
                        help='Input CSV file (default: auto-find all CSVs)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output cache directory (default: ./html_cache)')
    parser.add_argument('--concurrency', '-c', type=int, default=DEFAULT_CONCURRENCY,
                        help=f'Number of concurrent connections (default: {DEFAULT_CONCURRENCY})')
    parser.add_argument('--timeout', '-t', type=int, default=DEFAULT_TIMEOUT,
                        help=f'Timeout per request in seconds (default: {DEFAULT_TIMEOUT})')
    parser.add_argument('--test', type=int, default=0,
                        help='Test mode: only fetch N domains (e.g., --test 50)')
    parser.add_argument('--clear-cache', action='store_true',
                        help='Clear existing cache before starting')
    args = parser.parse_args()

    # Determine paths
    cache_dir = Path(args.output) if args.output else DEFAULT_CACHE_DIR
    search_dir = Path.cwd()
    input_file = Path(args.input) if args.input else None

    if args.clear_cache:
        import shutil
        if cache_dir.exists():
            shutil.rmtree(cache_dir)
            print(f"Cleared cache: {cache_dir}")

    asyncio.run(run_fetcher(
        cache_dir=cache_dir,
        search_dir=search_dir,
        input_file=input_file,
        concurrency=args.concurrency,
        timeout=args.timeout,
        test_limit=args.test
    ))


if __name__ == '__main__':
    main()
