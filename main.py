# main.py (updated)
from crawler.scraper import scrape_page
from core.indexer import init_db, store_leaks
from core.alert import check_alert_terms
import time

init_db()

with open("crawler/targets.txt") as f:
    urls = [line.split('#')[0].strip() for line in f if line.strip() and not line.startswith('#')]

for i, url in enumerate(urls):
    print(f"[{i+1}/{len(urls)}] Scraping: {url}")
    if data := scrape_page(url):
        if data['emails']:
            store_leaks(data)
    time.sleep(10)  # Be polite

check_alert_terms(["samad04", "charusat", "example.com"])