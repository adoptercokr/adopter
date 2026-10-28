import asyncio
import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

STAYS = [
    {"key": "gw-namubat", "name": "홍천 나무밭", "query": "홍천 나무밭"},
    {"key": "gw-caminode", "name": "까미노데플로레스타", "query": "홍천 까미노데플로레스타"},
    {"key": "gw-narobuteo", "name": "강릉 나로부터 풀빌라", "query": "강릉 나로부터 풀빌라"},
    {"key": "gw-secretgarden", "name": "강릉 비밀의정원 풀빌라", "query": "강릉 비밀의정원 풀빌라"},
    {"key": "gw-privateyangyang", "name": "프라이빗양양 독채 풀빌라", "query": "프라이빗양양 독채 풀빌라"},
    {"key": "gw-lahenne", "name": "고성 라헨느풀빌라", "query": "고성 라헨느풀빌라"},
    {"key": "gw-uirim", "name": "춘천 의림여관", "query": "춘천 의림여관"},
    {"key": "gw-bebridge", "name": "영월 비브릿지 풀빌라", "query": "영월 비브릿지 풀빌라"},
    {"key": "gw-urpoolvilla", "name": "원주 유알 풀빌라", "query": "원주 유알 풀빌라"},
    {"key": "gw-migallu", "name": "삼척 미갈루 풀빌라", "query": "삼척 미갈루 풀빌라"}
]

async def collect_gangwon_stays():
    results = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            viewport={'width': 390, 'height': 844}
        )
        page = await ctx.new_page()

        for item in STAYS:
            print(f"\n==========================================")
            print(f"[*] 검색 중: {item['name']} ({item['query']})")
            search_url = f"https://m.map.naver.com/search2/search.naver?query={item['query']}"
            
            place_id = None
            try:
                await page.goto(search_url, timeout=25000, wait_until='domcontentloaded')
                await page.wait_for_timeout(3500)
                content = await page.content()
                
                # regex to extract place id
                ids = re.findall(r'siteview/([0-9]+)', content) or re.findall(r'place/([0-9]+)', content) or re.findall(r'accommodation/([0-9]+)', content)
                if ids:
                    place_id = ids[0]
                    print(f"  [+] 플레이스 ID 발견: {place_id}")
                else:
                    print(f"  [-] 플레이스 ID 미발견")
            except Exception as e:
                print(f"  [!] 검색 에러: {e}")

            photos = []
            if place_id:
                photo_url = f"https://m.place.naver.com/accommodation/{place_id}/photo"
                print(f"  [*] 사진 페이지 접속: {photo_url}")
                try:
                    await page.goto(photo_url, timeout=25000, wait_until='domcontentloaded')
                    await page.wait_for_timeout(4000)
                    
                    imgs = await page.evaluate("""
                        () => {
                            const imgs = document.querySelectorAll('img');
                            return Array.from(imgs)
                                .map(i => i.src)
                                .filter(s => s && s.startsWith('http') && !s.includes('icon') && !s.includes('profile'))
                                .filter(s => s.includes('pstatic') || s.includes('naverbooking') || s.includes('ldb-phinf'));
                        }
                    """)
                    photos = list(dict.fromkeys(imgs))[:15] # Deduplicate while keeping order
                    print(f"  [+] 고화질 실사진 {len(photos)}장 수집 완료!")
                except Exception as e:
                    print(f"  [!] 사진 수집 에러: {e}")

            naver_link = f"https://m.place.naver.com/accommodation/{place_id}/home" if place_id else ""
            
            results.append({
                "key": item["key"],
                "name": item["name"],
                "query": item["query"],
                "place_id": place_id,
                "naver_link": naver_link,
                "photos": photos
            })

        await browser.close()

    os.makedirs('tools', exist_ok=True)
    with open('tools/gangwon_10_collected.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n==========================================")
    print(f"[SUCCESS] 강원도 10곳 수집 결과 저장 완료: tools/gangwon_10_collected.json")

if __name__ == '__main__':
    asyncio.run(collect_gangwon_stays())
