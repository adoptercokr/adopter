import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        ig_accounts = [
            'https://www.instagram.com/poolvilla_k/', # 풀빌라 케이
            'https://www.instagram.com/onda_poolvilla/', # 온다 풀빌라
            'https://www.instagram.com/secretgarden_poolvilla/', # 비밀의정원
            'https://www.instagram.com/bigpinetree_official/', # 빅파인트리
            'https://www.instagram.com/camino_de_floresta/', # 까미노데플로레스타
            'https://www.instagram.com/poolvilla_su/', # 독채풀빌라 수
            'https://www.instagram.com/nj_poolvilla/', # 엔제이 풀빌라
            'https://www.instagram.com/dalnosi_stay/', # 달노시
            'https://www.instagram.com/chungchun_yeonga/', # 청춘연가
            'https://www.instagram.com/stay_handam/' # 한담
        ]
        
        results = []
        for ig in ig_accounts:
            try:
                print(f"Scraping {ig}...")
                await page.goto(ig, timeout=15000)
                await page.wait_for_timeout(3000)
                imgs = await page.eval_on_selector_all('img', 'elements => elements.map(e => e.src)')
                valid = [img for img in imgs if 'scontent' in img][:10]
                if len(valid) >= 5:
                    results.append({
                        'ig': ig,
                        'name': ig.split('/')[-2],
                        'images': valid
                    })
                    print(f"Got {len(valid)} images for {ig}")
            except Exception as e:
                print(f"Failed {ig}: {e}")
                
        import json
        with open('tools/real_ig_photos.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
