import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print("Visiting Instagram...")
        await page.goto('https://www.instagram.com/sanur.jeju/', timeout=15000)
        await page.wait_for_timeout(3000)
        imgs = await page.eval_on_selector_all('img', 'elements => elements.map(e => e.src)')
        valid = [img for img in imgs if 'scontent' in img]
        print(f"Found {len(valid)} Instagram images!")
        for i, img in enumerate(valid[:3]):
            print(f"Img {i}: {img}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
