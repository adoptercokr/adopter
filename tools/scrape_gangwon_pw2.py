import asyncio
from playwright.async_api import async_playwright
import json

async def main():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Visiting Stayfolio Gangwon...")
        await page.goto('https://www.stayfolio.com/findstay?city=gangwon-do', timeout=30000)
        await page.wait_for_timeout(5000)
        
        links = await page.eval_on_selector_all('a', 'elements => elements.map(e => e.href)')
        valid_links = []
        for l in links:
            if 'stays/' in l and 'journal' not in l:
                if l not in valid_links:
                    valid_links.append(l)
                    
        print(f"Found {len(valid_links)} stays. Processing 10...")
        
        for link in valid_links[:10]:
            try:
                print(f"Visiting {link}...")
                p2 = await browser.new_page()
                await p2.goto(link, timeout=30000)
                await p2.wait_for_timeout(3000)
                
                name = await p2.evaluate("() => document.querySelector('h1')?.innerText || ''")
                address = await p2.evaluate("() => { const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText.includes('강원')); return el ? el.innerText : ''; }")
                
                images = await p2.evaluate("() => Array.from(document.querySelectorAll('img')).map(img => img.src).filter(src => src.includes('http'))")
                images = list(dict.fromkeys(images))
                images = [img for img in images if 'stayfolio.com' in img and 'logo' not in img.lower()][:10]
                
                if name and len(images) >= 5:
                    results.append({
                        'name': name.strip(),
                        'address': address.strip() if address else '강원도',
                        'phone': '010-0000-0000',
                        'images': images,
                        'url': link
                    })
                    print(f"Success: {name}")
                await p2.close()
            except Exception as e:
                print(f"Error on {link}: {e}")
                
        await browser.close()
        
        with open('tools/stayfolio_gangwon_10.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
            
        print(f"Saved {len(results)} properties to tools/stayfolio_gangwon_10.json")

if __name__ == '__main__':
    asyncio.run(main())
