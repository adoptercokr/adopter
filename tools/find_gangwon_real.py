import asyncio
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

SEARCH_QUERIES = [
    'https://m.place.naver.com/search?query=%EA%B0%95%EC%9B%90%EB%8F%84+%ED%92%80%EB%B9%8C%EB%9D%BC+%EB%8F%85%EC%B1%84&type=accommodation',
    'https://m.place.naver.com/search?query=%EA%B0%95%EB%A6%89+%ED%92%80%EB%B9%8C%EB%9D%BC&type=accommodation',
    'https://m.place.naver.com/search?query=%EC%96%91%EC%96%91+%EB%8F%85%EC%B1%84+%ED%92%80%EB%B9%8C%EB%9D%BC&type=accommodation',
]

async def search_naver(page, url):
    try:
        print(f"Loading: {url[:80]}")
        await page.goto(url, timeout=30000, wait_until='domcontentloaded')
        await page.wait_for_timeout(4000)
        
        # Extract place IDs and names from search results
        places = await page.evaluate("""
            () => {
                const items = document.querySelectorAll('a[href*="/accommodation/"]');
                const results = [];
                const seen = new Set();
                for (const item of items) {
                    const href = item.href || '';
                    const match = href.match(/\\/accommodation\\/(\\d+)/);
                    if (match && !seen.has(match[1])) {
                        seen.add(match[1]);
                        // Find name
                        const nameEl = item.querySelector('.TYaxT, .place_name, h2, h3, strong');
                        const name = nameEl ? nameEl.innerText.trim() : '';
                        results.push({
                            id: match[1],
                            name: name,
                            naverLink: 'https://m.place.naver.com/accommodation/' + match[1] + '/home'
                        });
                    }
                }
                return results.slice(0, 10);
            }
        """)
        print(f"  Found {len(places)} places")
        return places
    except Exception as e:
        print(f"  Error: {e}")
        return []

async def get_photos(page, place_id):
    try:
        url = f"https://m.place.naver.com/accommodation/{place_id}/photo"
        await page.goto(url, timeout=25000, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)
        
        imgs = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('img');
                return Array.from(imgs)
                    .map(i => i.src)
                    .filter(s => s && s.includes('pstatic') && s.length > 80);
            }
        """)
        return imgs[:10]
    except Exception as e:
        print(f"  Photo error: {e}")
        return []

async def main():
    all_found = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            viewport={'width': 390, 'height': 844}
        )
        page = await ctx.new_page()
        
        seen_ids = set()
        
        for query_url in SEARCH_QUERIES:
            places = await search_naver(page, query_url)
            for p_info in places:
                if p_info['id'] not in seen_ids and p_info['name']:
                    seen_ids.add(p_info['id'])
                    all_found.append(p_info)
                    print(f"  + {p_info['name']} ({p_info['id']})")
                    if len(all_found) >= 10:
                        break
            if len(all_found) >= 10:
                break
        
        print(f"\nTotal found: {len(all_found)} places")
        print("Now scraping photos...")
        
        results = []
        for place in all_found[:10]:
            print(f"\nGetting photos for: {place['name']}")
            photos = await get_photos(page, place['id'])
            place['photos'] = photos
            place['photoCount'] = len(photos)
            results.append(place)
            print(f"  Got {len(photos)} photos")
        
        await browser.close()
    
    with open('tools/gangwon_real.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n=== RESULTS ===")
    for r in results:
        print(f"{r['name']} | {r['id']} | {r['photoCount']}photos")
    print("\nSaved to gangwon_real.json")

asyncio.run(main())
