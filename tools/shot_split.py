import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        # Serve it locally using a file URL
        abs_path = os.path.abspath('Customer/260930-peaceofmind/index.html')
        await page.goto('file://' + abs_path)
        await page.wait_for_timeout(3000)
        
        await page.screenshot(path='tools/split.png')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
