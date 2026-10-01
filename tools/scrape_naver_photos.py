import asyncio
import json
import os
import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

# Real accommodations with Naver Place IDs
targets = [
    {"folder": "260930-sanur",     "name": "사누르제주",   "naver": "https://m.place.naver.com/accommodation/2036409548/photo"},
    {"folder": "260930-negeut",    "name": "스테이느긋",   "naver": "https://m.place.naver.com/accommodation/1266911405/photo"},
    {"folder": "260930-aewolrowa", "name": "하루를품다",   "naver": "https://m.place.naver.com/accommodation/160795798/photo"},
    {"folder": "260930-gyeotgyeop","name": "곁겹",        "naver": "https://m.place.naver.com/accommodation/1076531080/photo"},
    {"folder": "260930-handam",    "name": "스테이한담",   "naver": "https://m.place.naver.com/accommodation/1299722517/photo"},
    {"folder": "260930-plumeria",  "name": "플루메리아",   "naver": "https://m.place.naver.com/accommodation/38729145/photo"},
]

async def get_naver_photos(page, url, name):
    try:
        print(f"  Loading {url}")
        await page.goto(url, timeout=30000, wait_until='domcontentloaded')
        await page.wait_for_timeout(4000)
        
        # Extract all image URLs from the page
        imgs = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('img');
                return Array.from(imgs)
                    .map(i => i.src)
                    .filter(s => s && s.startsWith('http') && !s.includes('data:') && s.length > 50)
                    .filter(s => !s.includes('loading') && !s.includes('placeholder'));
            }
        """)
        
        # Filter for large content images
        real = [i for i in imgs if any(x in i for x in ['pstatic', 'naver', 'kakao']) and len(i) > 80]
        print(f"  Got {len(real)} naver images for {name}")
        if real:
            print(f"  First: {real[0][:100]}")
        return real[:10]
    except Exception as e:
        print(f"  Error for {name}: {e}")
        return []

async def main():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Visible to pass bot checks
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            viewport={'width': 390, 'height': 844}
        )
        page = await ctx.new_page()
        
        for t in targets:
            print(f"\nScraping {t['name']} ({t['folder']})...")
            imgs = await get_naver_photos(page, t['naver'], t['name'])
            results[t['folder']] = imgs
        
        await browser.close()
    
    with open('tools/naver_photos.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved to naver_photos.json")

asyncio.run(main())
