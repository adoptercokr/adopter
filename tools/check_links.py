import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.stayfolio.com/findstay?city=gangwon-do', timeout=30000)
        await page.wait_for_timeout(5000)
        links = await page.eval_on_selector_all('a', 'elements => elements.map(e => e.href)')
        print(f"Total a tags: {len(links)}")
        for l in list(dict.fromkeys(links))[:20]:
            print(l)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
