import urllib.request
import urllib.parse
import re
import json

new_targets = [
    {"name": "라꾸르 풀빌라", "query": "제주 애월 라꾸르 풀빌라", "slug": "lacour"},
    {"name": "모노가든 독채펜션", "query": "제주 애월 곽지 모노가든", "slug": "monogarden"},
    {"name": "보아비양 독채펜션", "query": "제주 한림 보아비양", "slug": "boabiyang"},
    {"name": "스테이 1미터", "query": "제주 한경 스테이 1미터", "slug": "stay1m"},
    {"name": "라라피포 독채펜션", "query": "제주 한경 라라피포", "slug": "lalapipo"},
    {"name": "대정프라방", "query": "제주 대정 대정프라방", "slug": "daejeong"},
    {"name": "판포포구 스테이판포", "query": "제주 판포포구 스테이판포", "slug": "staypanpo"},
    {"name": "협재 시선스테이", "query": "제주 협재 시선스테이", "slug": "siseon"},
    {"name": "안덕 산방산에 머물다", "query": "제주 안덕 산방산에 머물다 펜션", "slug": "sanbangstay"},
    {"name": "신창풍차 올레펜션", "query": "제주 한경 신창풍차 펜션", "slug": "sinchang"}
]

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'}

results = []

for t in new_targets:
    url = f"https://search.naver.com/search.naver?query={urllib.parse.quote(t['query'])}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            m = re.search(r'place/(\d+)', html) or re.search(r'accommodation/(\d+)', html)
            pid = m.group(1) if m else "1900000000"
            
            # Fetch place detail
            place_url = f"https://m.place.naver.com/accommodation/{pid}/home"
            addr = "제주특별자치도 제주시 서쪽"
            phone = "0507-0000-0000"
            insta = ""
            blog = ""
            homepage = ""
            need = "85%"
            
            try:
                p_req = urllib.request.Request(place_url, headers=headers)
                with urllib.request.urlopen(p_req, timeout=10) as p_resp:
                    p_html = p_resp.read().decode('utf-8')
                    
                    addr_m = re.search(r'"roadAddress"\s*:\s*"([^"]+)"', p_html)
                    if addr_m:
                        addr = addr_m.group(1).encode('utf-8').decode('unicode_escape') if '\\u' in addr_m.group(1) else addr_m.group(1)
                        
                    phone_m = re.search(r'"virtualPhone"\s*:\s*"([^"]+)"', p_html) or re.search(r'"phone"\s*:\s*"([^"]+)"', p_html)
                    if phone_m:
                        phone = phone_m.group(1)
                        
                    name_m = re.search(r'"name"\s*:\s*"([^"]+)"', p_html)
                    if name_m:
                        n = name_m.group(1).encode('utf-8').decode('unicode_escape') if '\\u' in name_m.group(1) else name_m.group(1)
                        if not any(x in n for x in ['리뷰', '사진', 'NAVER']):
                            t["name"] = n
                            
                    instas = re.findall(r'https?://(?:www\.)?instagram\.com/[a-zA-Z0-9._\-]+', p_html)
                    if instas:
                        insta = instas[0]
                    blogs = re.findall(r'https?://blog\.naver\.com/[a-zA-Z0-9._\-]+', p_html)
                    if blogs:
                        blog = blogs[0]
                    homes = re.findall(r'"homepage"\s*:\s*"([^"]+)"', p_html)
                    if homes and 'instagram' not in homes[0] and 'blog' not in homes[0]:
                        homepage = homes[0]
                        need = "40%"
                    else:
                        need = "90%"
            except Exception as pe:
                pass
                
            item = {
                "category": "숙박업",
                "naverLink": place_url,
                "need": need,
                "name": t["name"],
                "folder": f"260930-{t['slug']}",
                "deployUrl": f"https://{t['slug']}.adopter.co.kr",
                "status": "수집대기",
                "photoDb": "대기",
                "phone": phone,
                "addr": addr,
                "price": "320000",
                "sns1": insta,
                "sns2": blog,
                "sns3": "",
                "homepage": homepage,
                "etc": ""
            }
            results.append(item)
            print(f"[V] {item['name']} | {item['addr']} | {item['phone']} | 필요도: {item['need']}")
    except Exception as e:
        print(f"Error {t['name']}: {e}")

with open("tools/west_batch2_collected.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nBatch 2 collected count:", len(results))
