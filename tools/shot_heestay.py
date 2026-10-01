import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://adopter.co.kr/Customer/tpl-01-heestay/')
        await page.wait_for_timeout(3000)
        await page.screenshot(path='tools/heestay_debug_2.png')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
