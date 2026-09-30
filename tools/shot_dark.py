import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Serve it locally since it's not deployed yet
        # Actually I can just wait for deploy
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
