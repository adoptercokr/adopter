import asyncio
from playwright.async_api import async_playwright
import urllib.request
import os

async def main():
    os.makedirs('Customer/260930-sanbangstay/img', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto('https://m.place.naver.com/accommodation/51922/home')
        await page.wait_for_timeout(5000)
        
        # Extract images from DOM
        images = await page.evaluate('''() => {
            const imgs = Array.from(document.querySelectorAll('img'));
            return imgs.map(img => img.src).filter(src => src.includes('ldb-phinf.pstatic.net'));
        }''')
        
        valid_imgs = list(dict.fromkeys(images))
        
        for i, url in enumerate(valid_imgs[:10]):
            url = url.replace('type=f180_180', 'type=f800_800')
            url = url.replace('type=f140_140', 'type=f800_800')
            req = urllib.request.Request(url, headers={'Referer': 'https://m.place.naver.com/'})
            try:
                with urllib.request.urlopen(req) as response:
                    with open(f'Customer/260930-sanbangstay/img/photo_{i+1}.jpg', 'wb') as f:
                        f.write(response.read())
                    print(f"Downloaded photo_{i+1}")
            except Exception as e:
                print(e)
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
