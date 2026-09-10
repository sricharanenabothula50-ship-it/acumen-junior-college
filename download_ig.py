import asyncio
import json
import re
from pathlib import Path
from playwright.async_api import async_playwright

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

async def get_images_from_embed(page, shortcode):
    url = f"https://www.instagram.com/p/{shortcode}/embed/"
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)
        
        # Get all image sources
        images = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('img');
                return Array.from(imgs).map(img => ({
                    src: img.src,
                    width: img.naturalWidth,
                    height: img.naturalHeight
                })).filter(i => i.src && (i.src.includes('scontent') || i.src.includes('fbcdn')));
            }
        """)
        
        # Also get any background images or data-src attributes
        bg_images = await page.evaluate("""
            () => {
                const allEls = document.querySelectorAll('*');
                const urls = [];
                for (const el of allEls) {
                    const style = window.getComputedStyle(el);
                    const bg = style.backgroundImage;
                    if (bg && bg !== 'none' && bg.includes('url')) {
                        const match = bg.match(/url\\("?([^"]+)"?\\)/);
                        if (match) urls.push(match[1]);
                    }
                }
                return urls.filter(u => u.includes('scontent') || u.includes('fbcdn'));
            }
        """)
        
        all_urls = []
        for img in images:
            if img['width'] > 100:  # Skip tiny profile pics
                all_urls.append(img['src'])
        for u in bg_images:
            if u not in all_urls:
                all_urls.append(u)
        
        return all_urls
    except Exception as e:
        print(f"  Error: {e}")
        return []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        photos = []
        
        for sc in SHORTCODES:
            print(f"\n--- {sc} ---")
            images = await get_images_from_embed(page, sc)
            print(f"  Found {len(images)} images")
            
            for i, img_url in enumerate(images):
                img_url_clean = img_url.replace("&amp;", "&")
                # Get highest resolution
                if "p720x720" in img_url_clean or "s1080x1080" in img_url_clean:
                    suffix = "_hd"
                elif "p640x640" in img_url_clean:
                    suffix = "_sd"
                else:
                    suffix = f"_{i}"
                
                fname = f"ig_{sc}{suffix}"
                try:
                    resp = await page.request.get(img_url_clean)
                    if resp.ok:
                        ct = resp.headers.get("content-type", "")
                        ext = ".jpg"
                        if "png" in ct: ext = ".png"
                        elif "webp" in ct: ext = ".webp"
                        
                        filepath = GALLERY_DIR / f"{fname}{ext}"
                        body = await resp.body()
                        if len(body) > 5000:
                            filepath.write_bytes(body)
                            print(f"  [OK] {filepath.name} ({len(body):,} bytes)")
                            photos.append({
                                "file": filepath.name,
                                "alt": "Acumen Junior College Instagram post",
                                "caption": "Instagram post",
                            })
                        else:
                            print(f"  [SKIP] Too small ({len(body)} bytes)")
                except Exception as e:
                    print(f"  [ERROR] {e}")
        
        await browser.close()
    
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

asyncio.run(main())
