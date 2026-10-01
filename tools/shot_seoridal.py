import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://adopter.co.kr/Customer/261001-gangwon-seoridal/')
        await page.wait_for_timeout(3000)
        await page.screenshot(path='tools/seoridal_debug.png')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
