import requests
import re

r = requests.get(
    'https://www.instagram.com/p/C3SXMXCvRFh/embed/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
    timeout=15
)

# Save full content for analysis
with open('debug_full.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)

# Find ALL URLs in the page
all_urls = re.findall(r'https?://[^\s"\'<>]+', r.text)
print(f"Total URLs found: {len(all_urls)}")

# Filter for instagram/image related
for u in all_urls:
    u_clean = u.replace('\\/', '/').replace('&amp;', '&')
    if 'scontent' in u_clean or 'fbcdn' in u_clean:
        print(f"  {u_clean[:200]}")
