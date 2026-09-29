import urllib.request
import urllib.parse
import re
import json
import csv

place_targets = [
    {"name": "사누르제주", "pid": "2036409548", "slug": "sanur"},
    {"name": "하일리제주", "pid": "1831033368", "slug": "haily"},
    {"name": "스테이느긋", "pid": "1266911405", "slug": "negeut"},
    {"name": "애월로와 키즈풀빌라", "pid": "160795798", "slug": "aewolrowa"},
    {"name": "한림 곁겹 풀빌라", "pid": "1076531080", "slug": "gyeotgyeop"},
    {"name": "후아힌협재풀빌라", "pid": "1293795324", "slug": "huahin"},
    {"name": "한림 금능여관", "pid": "2000699781", "slug": "geumneung"},
    {"name": "애월 한담스테이", "pid": "1299722517", "slug": "handam"},
    {"name": "애월 플루메리아 펜션", "pid": "38729145", "slug": "plumeria"},
    {"name": "한림 몽돌하우스", "pid": "2576795", "slug": "mongdol"}
]

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8'
}

sheet_rows = []

for idx, p in enumerate(place_targets, 1):
    pid = p["pid"]
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    
    info = {
        "category": "숙박업",
        "naverLink": url,
        "need": "85%",
        "name": p["name"],
        "folder": f"260930-{p['slug']}",
        "deployUrl": f"https://{p['slug']}.adopter.co.kr",
        "status": "수집대기",
        "photoDb": "대기",
        "phone": "",
        "addr": "",
        "price": "300000",
        "sns1": "",
        "sns2": "",
        "sns3": "",
        "homepage": "",
        "etc": ""
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            
            # Extract Address
            addr_m = re.search(r'"roadAddress"\s*:\s*"([^"]+)"', html)
            if addr_m:
                info["addr"] = addr_m.group(1).encode('utf-8').decode('unicode_escape') if '\\u' in addr_m.group(1) else addr_m.group(1)
            
            # Extract Phone
            phone_m = re.search(r'"virtualPhone"\s*:\s*"([^"]+)"', html) or re.search(r'"phone"\s*:\s*"([^"]+)"', html)
            if phone_m:
                info["phone"] = phone_m.group(1)
                
            # Extract exact Name
            name_m = re.search(r'"name"\s*:\s*"([^"]+)"', html)
            if name_m:
                raw_name = name_m.group(1).encode('utf-8').decode('unicode_escape') if '\\u' in name_m.group(1) else name_m.group(1)
                if not any(x in raw_name for x in ['리뷰', '사진', 'NAVER', '지도']):
                    info["name"] = raw_name
                    
            # Extract SNS
            instas = re.findall(r'https?://(?:www\.)?instagram\.com/[a-zA-Z0-9._\-]+', html)
            if instas:
                info["sns1"] = instas[0]
                
            blogs = re.findall(r'https?://blog\.naver\.com/[a-zA-Z0-9._\-]+', html)
            if blogs:
                info["sns2"] = blogs[0]
                
            # Check custom homepage
            homes = re.findall(r'"homepage"\s*:\s*"([^"]+)"', html)
            if homes:
                h = homes[0]
                if 'instagram' not in h and 'blog' not in h:
                    info["homepage"] = h
                    info["need"] = "40%"
                else:
                    info["need"] = "85%"
            else:
                info["need"] = "90%" # 홈페이지 완전 없음 (최고 타겟)
                
    except Exception as e:
        print(f"Error fetching {p['name']}: {e}")

    print(f"[{idx}/10] {info['name']} | {info['addr']} | {info['phone']} | 필요도: {info['need']}")
    sheet_rows.append(info)

# Save to JSON
with open("tools/west_10_collected.json", "w", encoding="utf-8") as f:
    json.dump(sheet_rows, f, ensure_ascii=False, indent=2)

# Save to TSV (for easy copy-paste directly into Google Sheet)
tsv_path = "tools/west_10_for_googlesheet.tsv"
with open(tsv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    # Headers matching the sheet
    writer.writerow([
        "카테고리", "네이버지도링크", "홈페이지 필요도", "업체명", "폴더명", "배포주소", 
        "진행상황", "사진및db", "연락처", "주소", "평균금액", "sns", "sns", "sns", "홈페이지", "기타"
    ])
    for r in sheet_rows:
        writer.writerow([
            r["category"], r["naverLink"], r["need"], r["name"], r["folder"], r["deployUrl"],
            r["status"], r["photoDb"], r["phone"], r["addr"], r["price"], r["sns1"], r["sns2"], r["sns3"],
            r["homepage"], r["etc"]
        ])

print(f"\nGenerated TSV at {tsv_path}")
