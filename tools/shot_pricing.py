import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://adopter.co.kr/')
        await page.wait_for_timeout(3000)
        
        # Take a screenshot of the pricing section
        await page.evaluate("document.getElementById('pricing').scrollIntoView()")
        await page.wait_for_timeout(1000)
        await page.screenshot(path='tools/pricing.png')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
