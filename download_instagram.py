import requests
import re
import json
from pathlib import Path

GALLERY_DIR = Path("assets/gallery")
GALLERY_DIR.mkdir(parents=True, exist_ok=True)

SHORTCODES = [
    "C3SXMXCvRFh",
    "C4fWHgvSnBB",
    "C3PTtmdP7cQ",
    "DOsunCFkh5b",
    "DOssJMOEg1U",
    "CjrW3JoL7hP",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.instagram.com/",
}

def get_best_image(shortcode):
    url = f"https://www.instagram.com/p/{shortcode}/embed/"
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return None
    
    # Find all CDN image URLs
    all_urls = re.findall(r'https?://[^\s"\'<>]+', r.text)
    
    # Filter for actual post images (not profile pics, not static resources)
    post_images = []
    for u in all_urls:
        u_clean = u.replace('\\/', '/').replace('&amp;', '&')
        # Skip profile pictures (t51.2885-19 is profile pic)
        if 't51.2885-19' in u_clean:
            continue
        # Skip static CDN resources
        if 'static.cdninstagram.com' in u_clean:
            continue
        # Must be a fbcdn image
        if 'fbcdn.net' not in u_clean:
            continue
        # Must be an image format
        if not re.search(r'\.(jpg|jpeg|png|webp|heic)', u_clean):
            continue
        # Get the highest resolution version
        # Look for p720x720 or s1080x1080
        if 'p720x720' in u_clean or 's1080x1080' in u_clean:
            post_images.insert(0, u_clean)  # Prefer higher res
        elif 'p640x640' in u_clean or 's640x640' in u_clean:
            post_images.append(u_clean)
        elif 'p480x480' in u_clean:
            post_images.append(u_clean)
    
    # Deduplicate by base URL
    seen = set()
    unique = []
    for img in post_images:
        base = img.split('?')[0]
        if base not in seen:
            seen.add(base)
            unique.append(img)
    
    return unique[0] if unique else None

def download_image(url, filename):
    try:
        r = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        if r.status_code == 200:
            ct = r.headers.get('content-type', '')
            ext = '.jpg'
            if 'png' in ct:
                ext = '.png'
            elif 'webp' in ct:
                ext = '.webp'
            elif 'heic' in ct or 'heif' in ct:
                ext = '.jpg'  # Convert heic to jpg extension
            
            filepath = GALLERY_DIR / f"{filename}{ext}"
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
            
            size = filepath.stat().st_size
            if size > 5000:
                print(f"  [OK] {filepath.name} ({size:,} bytes)")
                return filepath.name
            else:
                filepath.unlink()
                print(f"  [SKIP] Too small ({size} bytes)")
                return None
        else:
            print(f"  [WARN] Status {r.status_code}")
            return None
    except Exception as e:
        print(f"  [ERROR] {e}")
        return None

def main():
    photos = []
    
    for sc in SHORTCODES:
        print(f"\n--- {sc} ---")
        img_url = get_best_image(sc)
        if img_url:
            print(f"  Best image URL found")
            result = download_image(img_url, f"ig_{sc}")
            if result:
                photos.append({
                    "file": result,
                    "alt": "Acumen Junior College Instagram post",
                    "caption": "Instagram post",
                })
        else:
            print(f"  No image found")
    
    # Update photos.json
    json_path = GALLERY_DIR / "photos.json"
    existing = []
    if json_path.exists():
        try:
            existing = json.loads(json_path.read_text())
        except:
            pass
    
    existing_files = {p["file"] for p in existing}
    added = 0
    for p in photos:
        if p["file"] not in existing_files:
            existing.append(p)
            existing_files.add(p["file"])
            added += 1
    
    json_path.write_text(json.dumps(existing, indent=2))
    print(f"\n=== Done. {added} new photos added. Total: {len(existing)} ===")

if __name__ == "__main__":
    main()
