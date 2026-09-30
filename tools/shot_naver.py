import asyncio
from playwright.async_api import async_playwright
import urllib.request
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto('https://m.place.naver.com/accommodation/51922/home')
        await page.wait_for_timeout(5000)
        
        # Take a screenshot to see what's wrong
        await page.screenshot(path='tools/naver.png')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
