import requests
import re

r = requests.get(
    'https://www.instagram.com/p/C3SXMXCvRFh/embed/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
    timeout=15
)
print(f"Status: {r.status_code}, Length: {len(r.text)}")

# Search for image URLs
patterns = [
    r'(https?://[^"\'\s]*scontent[^"\'\s]*)',
    r'(https?://[^"\'\s]*cdninstagram[^"\'\s]*)',
    r'"display_url"\s*:\s*"([^"]+)"',
    r'src="(https?://[^"]*\.(?:jpg|png|webp)[^"]*)"',
]
for p in patterns:
    matches = re.findall(p, r.text)
    if matches:
        print(f"\nPattern found: {len(matches)} matches")
        for m in matches[:5]:
            print(f"  {m[:150]}")
