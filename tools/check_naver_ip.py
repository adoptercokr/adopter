import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            resp = await page.goto('https://m.place.naver.com/accommodation/1853358036/home', timeout=15000)
            print("Status:", resp.status)
            title = await page.title()
            print("Title:", title)
            if '제한' in title:
                print("STILL BLOCKED BY NAVER")
        except Exception as e:
            print("Error:", e)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
