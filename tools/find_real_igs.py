import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Searching Instagram for Gangwon pool villas...")
        await page.goto('https://duckduckgo.com/?q=site%3Ainstagram.com+%22%EA%B0%95%EC%9B%90%EB%8F%84+%ED%92%80%EB%B9%8C%EB%9D%BC%22', timeout=30000)
        await page.wait_for_timeout(3000)
        links = await page.eval_on_selector_all('a[href*="instagram.com/"]', 'elements => elements.map(e => e.href)')
        
        valid_igs = []
        for l in links:
            if '/p/' not in l and '/explore/' not in l and '/tags/' not in l:
                clean = l.split('?')[0].strip('/')
                if clean not in valid_igs and clean != 'https://www.instagram.com':
                    valid_igs.append(clean)
        
        print("Found accounts:")
        for ig in valid_igs[:10]:
            print(ig)
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
