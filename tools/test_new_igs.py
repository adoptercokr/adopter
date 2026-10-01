import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright
import json

new_properties = [
    {"id": "new1", "name": "포레스트 풀빌라", "ig": "https://www.instagram.com/forest_poolvilla"},
    {"id": "new2", "name": "오션트리 리조트", "ig": "https://www.instagram.com/oceantree_resort"},
    {"id": "new3", "name": "스테이 숲", "ig": "https://www.instagram.com/stay_soop"},
    {"id": "new4", "name": "블루엘", "ig": "https://www.instagram.com/blueel_poolvilla"},
    {"id": "new5", "name": "더브리즈", "ig": "https://www.instagram.com/thebreeze_jeju"},
    {"id": "new6", "name": "히든비치", "ig": "https://www.instagram.com/hiddenbeach_resort"}
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for prop in new_properties:
            try:
                print(f"Scraping {prop['ig']}...")
                await page.goto(prop['ig'], timeout=15000)
                await page.wait_for_timeout(3000)
                imgs = await page.eval_on_selector_all('img', 'elements => elements.map(e => e.src)')
                valid = [img for img in imgs if 'scontent' in img][:10]
                print(f"{prop['name']}: got {len(valid)} images")
            except Exception as e:
                print(f"Failed {prop['name']}: {e}")
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
