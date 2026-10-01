import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))
        await page.goto('https://adopter.co.kr/Customer/tpl-01-heestay/')
        await page.wait_for_timeout(3000)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
