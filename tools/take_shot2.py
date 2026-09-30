import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto('https://aewolrowa.adopter.co.kr/')
        await page.wait_for_timeout(3000)
        
        # Scroll down to gallery
        await page.evaluate("document.getElementById('gallery').scrollIntoView()")
        await page.wait_for_timeout(1000)
        
        await page.screenshot(path='tools/aewolrowa_gallery.png')
        print("Screenshot saved to tools/aewolrowa_gallery.png")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
