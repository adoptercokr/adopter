import asyncio
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

with open('tools/gangwon_10_collected.json', 'r', encoding='utf-8') as f:
    stays = json.load(f)

async def enrich_details():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            viewport={'width': 390, 'height': 844}
        )
        page = await ctx.new_page()

        for s in stays:
            pid = s.get('place_id')
            if not pid:
                continue
            
            home_url = f"https://m.place.naver.com/accommodation/{pid}/home"
            print(f"Fetching details for {s['name']} ({home_url})...")
            try:
                await page.goto(home_url, timeout=25000, wait_until='domcontentloaded')
                await page.wait_for_timeout(3500)
                
                details = await page.evaluate("""
                    () => {
                        const addrEl = document.querySelector('.LDgIH, .IH9tW, .Dry01');
                        const addr = addrEl ? addrEl.innerText.trim() : '';
                        
                        const phoneEl = document.querySelector('.xlx7Q, .dry01 a');
                        const phone = phoneEl ? phoneEl.innerText.trim() : '';
                        
                        const descEl = document.querySelector('.zPfVt, .T8RFa');
                        const desc = descEl ? descEl.innerText.trim() : '';
                        
                        return { addr, phone, desc };
                    }
                """)
                s['addr'] = details.get('addr', '')
                s['phone'] = details.get('phone', '')
                s['desc'] = details.get('desc', '')
                print(f"  Addr: {s['addr']}, Phone: {s['phone']}")
            except Exception as e:
                print(f"  Error: {e}")

        await browser.close()

    with open('tools/gangwon_10_enriched.json', 'w', encoding='utf-8') as f:
        json.dump(stays, f, ensure_ascii=False, indent=2)
    print("Saved enriched data to tools/gangwon_10_enriched.json")

if __name__ == '__main__':
    asyncio.run(enrich_details())
