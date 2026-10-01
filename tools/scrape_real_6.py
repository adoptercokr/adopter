import asyncio
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

targets = [
    {"folder": "260930-sanur", "ig": "https://www.instagram.com/sanur.jeju/"},
    {"folder": "260930-negeut", "ig": "https://www.instagram.com/stay__negeut/"},
    {"folder": "260930-aewolrowa", "ig": "https://www.instagram.com/7another_day/"},
    {"folder": "260930-gyeotgyeop", "ig": "https://www.instagram.com/gyeotgyeop/"},
    {"folder": "260930-handam", "ig": "https://www.instagram.com/stay_handam/"},
    {"folder": "260930-plumeria", "ig": "https://www.instagram.com/plumeria_pension/"},
]

async def scrape_ig(page, url):
    try:
        await page.goto(url, timeout=20000, wait_until='networkidle')
        await page.wait_for_timeout(4000)
        # Get all img src from scontent CDN
        imgs = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('img');
                return Array.from(imgs)
                    .map(i => i.src)
                    .filter(s => s.includes('scontent') || s.includes('cdninstagram'));
            }
        """)
        # Deduplicate + filter out tiny avatar/icon images
        seen = set()
        big_imgs = []
        for img in imgs:
            if img not in seen and ('1080' in img or '640' in img or 'e35' in img or 'e15' in img or len(img) > 100):
                seen.add(img)
                big_imgs.append(img)
        return big_imgs[:10]
    except Exception as e:
        print(f"Error: {e}")
        return []

async def main():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        )
        page = await ctx.new_page()
        
        for t in targets:
            print(f"Scraping {t['folder']}...")
            imgs = await scrape_ig(page, t['ig'])
            results[t['folder']] = imgs
            print(f"  Got {len(imgs)} images")
            if imgs:
                print(f"  First: {imgs[0][:80]}")
        
        await browser.close()
    
    with open('tools/real_ig_photos2.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Saved to real_ig_photos2.json")

asyncio.run(main())
