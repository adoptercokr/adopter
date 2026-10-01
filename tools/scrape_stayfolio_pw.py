import asyncio
from playwright.async_api import async_playwright
import json
import time

async def main():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Visiting Stayfolio Jeju...")
        await page.goto('https://www.stayfolio.com/findstay?city=jeju-do', timeout=30000)
        
        # Wait for the stay cards to load
        await page.wait_for_selector('.findstay-list-item', timeout=20000)
        await page.wait_for_timeout(3000)
        
        # Get all links to stays
        links = await page.eval_on_selector_all('.findstay-list-item a', 'elements => elements.map(e => e.href)')
        
        print(f"Found {len(links)} links. Processing first 10...")
        
        for link in links[:10]:
            try:
                print(f"Visiting {link}...")
                p2 = await browser.new_page()
                await p2.goto(link, timeout=30000)
                await p2.wait_for_timeout(3000)
                
                # Name
                name = await p2.evaluate("() => document.querySelector('h1')?.innerText || ''")
                
                # Address
                address = await p2.evaluate("() => { const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText.includes('제주')); return el ? el.innerText : ''; }")
                
                # Images (Swiper or img tags)
                images = await p2.evaluate("() => Array.from(document.querySelectorAll('img')).map(img => img.src).filter(src => src.includes('http'))")
                
                # Clean images (remove duplicates, pick high res)
                images = list(dict.fromkeys(images))
                images = [img for img in images if 'stayfolio.com' in img and 'logo' not in img.lower()][:10]
                
                if name and len(images) >= 5:
                    results.append({
                        'name': name.strip(),
                        'address': address.strip() if address else '제주특별자치도',
                        'phone': '010-1234-5678', # Mock phone
                        'images': images,
                        'url': link
                    })
                    print(f"Success: {name}")
                await p2.close()
            except Exception as e:
                print(f"Error on {link}: {e}")
                
        await browser.close()
        
        with open('tools/stayfolio_10.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
            
        print(f"Saved {len(results)} properties to tools/stayfolio_10.json")

if __name__ == '__main__':
    asyncio.run(main())
