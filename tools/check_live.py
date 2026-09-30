import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on('console', lambda msg: print(f"CONSOLE: {msg.type}: {msg.text}"))
        page.on('pageerror', lambda err: print(f"PAGE ERROR: {err.stack}"))
        
        await page.goto('https://aewolrowa.adopter.co.kr/')
        await page.wait_for_timeout(3000)
        
        # Check if spaces-container has images
        html = await page.evaluate("document.getElementById('spaces-container') ? document.getElementById('spaces-container').innerHTML : 'NO_CONTAINER'")
        print("SPACES CONTAINER HTML:\n", html[:500])
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
