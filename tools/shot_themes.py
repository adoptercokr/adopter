import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for i, theme in enumerate([
            '05-wabi-sabi', '06-modern-glass', '07-hanok-heritage',
            '08-coastal-breeze', '09-industrial-chic', '10-velaa-luxury'
        ]):
            page = await browser.new_page()
            url = f'file:///{os.path.abspath(f"Customer/tpl-{theme}/index.html")}'.replace('\\\\', '/')
            await page.goto(url)
            await page.wait_for_timeout(2000)
            await page.screenshot(path=f'tools/shot_theme_{i+5}.png', full_page=True)
            print(f'Captured theme {theme}')
            await page.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
