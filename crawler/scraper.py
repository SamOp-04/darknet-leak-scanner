# crawler/scraper.py (updated)
from bs4 import BeautifulSoup
import re
from crawler.tor_connector import get_session, renew_tor_identity

import re

# Obfuscated + standard email regex
EMAIL_REGEX = re.compile(
    r'''(
        [\w.+-]+
        \s*(?:@|\[at\]|\(at\)|-a-t-|\sat\s)\s*
        [\w.-]+
        \s*(?:\.|\[dot\]|\(dot\)|-dot-|\sdot\s)\s*
        [a-zA-Z]{2,}
    )''',
    re.VERBOSE | re.IGNORECASE
)
def scrape_page(url, attempt=0):
    if attempt > 2:
        return None
        
    session = get_session()
    try:
        response = session.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()  # Case-insensitive matching
        emails = re.findall(EMAIL_REGEX, text)
        return {'url': url, 'emails': list(set(emails)), 'raw': text}  # Deduplicate
    except Exception as e:
        print(f"Retrying {url}...")
        renew_tor_identity()
        return scrape_page(url, attempt+1)