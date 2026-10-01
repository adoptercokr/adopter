import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print("Visiting Instagram...")
        await page.goto('https://www.instagram.com/sanur.jeju/', timeout=15000)
        await page.wait_for_timeout(3000)
        title = await page.title()
        print("Title:", title)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
