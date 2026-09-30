import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on('console', lambda msg: print(f"CONSOLE: {msg.type}: {msg.text}"))
        page.on('pageerror', lambda err: print(f"PAGE ERROR: {err}"))
        
        path = 'file://' + os.path.abspath('Customer/260930-aewolrowa/index.html').replace('\\', '/')
        await page.goto(path)
        await page.wait_for_timeout(2000)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
