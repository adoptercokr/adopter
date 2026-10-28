import asyncio
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

# Naver 검색 URL 직접 접근
SEARCH_URL = 'https://search.naver.com/search.naver?query=%EA%B0%95%EC%9B%90%EB%8F%84+%ED%92%80%EB%B9%8C%EB%9D%BC+%EB%8F%85%EC%B1%84&nso=&where=nexearch&sm=tab_opt&ie=utf8'

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1280, 'height': 900}
        )
        page = await ctx.new_page()
        
        print("Loading Naver search...")
        await page.goto(SEARCH_URL, timeout=30000, wait_until='domcontentloaded')
        await page.wait_for_timeout(5000)
        
        # Get all hrefs from the page
        hrefs = await page.evaluate("""
            () => {
                const links = document.querySelectorAll('a');
                return Array.from(links).map(a => a.href).filter(h => h.includes('place.naver.com') || h.includes('accommodation'));
            }
        """)
        print(f"Found {len(hrefs)} naver place links:")
        for h in hrefs[:20]:
            print(f"  {h}")
        
        # Also get the full page text
        title = await page.title()
        print(f"\nPage title: {title}")
        
        # Look for accommodation IDs
        ids_found = await page.evaluate("""
            () => {
                const text = document.body.innerHTML;
                const matches = text.match(/accommodation\\/([0-9]+)/g) || [];
                return [...new Set(matches)].slice(0, 20);
            }
        """)
        print(f"\nAccommodation IDs found: {ids_found}")
        
        await browser.close()

asyncio.run(main())
