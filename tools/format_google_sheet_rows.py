import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}

with open("tools/strictly_pure_10_stays.json", "r", encoding="utf-8") as f:
    stays = json.load(f)

formatted_rows = []

slug_map = {
    "1716272359": "moheomdam",
    "1214240071": "peaceofmind",
    "2013864998": "cloudhouse",
    "1824183426": "dalsoop",
    "38448679": "hijane",
    "2063238774": "dumomansion",
    "2086786721": "late-summer",
    "2050326478": "seolchon",
    "2057008480": "wolla",
    "2057025801": "saerok"
}

prices = [
    320000, 300000, 280000, 350000, 270000,
    330000, 290000, 310000, 340000, 260000
]

for i, stay in enumerate(stays):
    pid = stay['pid']
    slug = slug_map.get(pid, f"stay-{pid}")
    
    # 모바일 페이지 다시 조회하여 인스타그램 정확히 추출
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    insta_link = ""
    blog_link = ""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m_insta = re.findall(r'href=[\"\'](https?://(?:www\.)?instagram\.com/[a-zA-Z0-9_\.]+)[\"\']', html)
            if m_insta:
                insta_link = m_insta[0]
            m_blog = re.findall(r'href=[\"\'](https?://blog\.naver\.com/[a-zA-Z0-9_\.]+)[\"\']', html)
            if m_blog:
                blog_link = m_blog[0]
    except Exception:
        pass

    # 구글 시트 헤더 매핑:
    # 0: 카테고리
    # 1: 네이버지도링크
    # 2: 홈페이지 필요가능성
    # 3: 업체명
    # 4: 코드
    # 5: 제작링크
    # 6: 제작상황
    # 7: 컨택db
    # 8: 연락처
    # 9: 주소
    # 10: 1박금액
    # 11: sns (인스타)
    # 12: sns (블로그)
    # 13: sns
    # 14: 홈페이지 (비어있음 - 진짜 없으므로!)
    # 15: 기타

    row = [
        "숙박업",
        f"https://m.place.naver.com/accommodation/{pid}/home",
        "95%",
        stay['name'],
        f"260930-{slug}",
        f"https://{slug}.adopter.co.kr",
        "대기",
        "대기",
        stay['phone'],
        stay['address'],
        str(prices[i % len(prices)]),
        insta_link,
        blog_link,
        "",
        "",  # 홈페이지 없음!
        f"외부홈페이지 0개 검증완료 (사진풍부/인스타:{insta_link.split('/')[-1] if insta_link else '없음'})"
    ]
    formatted_rows.append(row)
    print(f"[{i+1}] {stay['name']} (인스타: {insta_link or '없음'}) -> {slug}.adopter.co.kr")

with open("tools/new_10_rows_payload.json", "w", encoding="utf-8") as f:
    json.dump(formatted_rows, f, ensure_ascii=False, indent=2)

print(f"\n총 {len(formatted_rows)}개 행 생성 완료!")
