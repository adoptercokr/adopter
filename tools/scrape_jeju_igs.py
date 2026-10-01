import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright
import json

async def main():
    with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f:
        jeju_props = json.load(f)
        
    ig_accounts = []
    for p in jeju_props:
        if p.get('sns1') and 'instagram.com' in p['sns1']:
            ig_accounts.append((p['name'], p['sns1']))
            
    with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f:
        jeju_props2 = json.load(f)
    for p in jeju_props2:
        if p.get('sns1') and 'instagram.com' in p['sns1']:
            ig_accounts.append((p['name'], p['sns1']))
            
    # Also add the 4 we got
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        results = []
        # load existing
        try:
            with open('tools/real_ig_photos.json', 'r', encoding='utf-8') as f:
                results = json.load(f)
        except:
            pass
            
        got_names = [r['name'] for r in results]
        
        for name, ig in ig_accounts:
            if name in got_names or ig in got_names:
                continue
            if len(results) >= 10:
                break
            try:
                print(f"Scraping {ig}...")
                await page.goto(ig, timeout=15000)
                await page.wait_for_timeout(3500)
                imgs = await page.eval_on_selector_all('img', 'elements => elements.map(e => e.src)')
                valid = [img for img in imgs if 'scontent' in img][:10]
                if len(valid) >= 5:
                    results.append({
                        'ig': ig,
                        'name': name,
                        'images': valid
                    })
                    print(f"Got {len(valid)} images for {name}")
                else:
                    print(f"Only {len(valid)} images for {name}")
            except Exception as e:
                print(f"Failed {name}: {e}")
                
        with open('tools/real_ig_photos.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
            
        print(f"Total properties: {len(results)}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
