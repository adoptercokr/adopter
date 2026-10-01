import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.stayfolio.com/findstay?city=gangwon-do', timeout=30000)
        await page.wait_for_timeout(5000)
        
        # print all a tags that have href containing '/journal/' or '/findstay/'
        links = await page.eval_on_selector_all('a', 'elements => elements.map(e => e.href)')
        for link in links:
            if 'journal' in link or 'stays' in link or 'findstay/' in link or 'journal/' not in link and 'com/stays/' in link:
                print(link)
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
