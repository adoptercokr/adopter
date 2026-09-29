import urllib.request
import urllib.parse
import json

queries = ["제주 애월 펜션", "제주 한림 펜션", "제주 서쪽 풀빌라"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://map.naver.com/'
}

all_places = []
seen_ids = set()

for q in queries:
    encoded_query = urllib.parse.quote(q)
    url = f"https://map.naver.com/p/api/search/allSearch?query={encoded_query}&type=all&searchCoord=126.32%3B33.46"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            place_data = data.get('result', {}).get('place')
            if place_data and 'list' in place_data:
                for it in place_data['list']:
                    pid = it.get('id')
                    if pid not in seen_ids:
                        seen_ids.add(pid)
                        name = it.get('name')
                        tel = it.get('tel') or ""
                        addr = it.get('roadAddress') or it.get('address') or ""
                        home = it.get('homePage') or ""
                        
                        # Website necessity
                        if not home:
                            need = "90%" # 홈페이지 완전 없음 (최우선 타겟)
                        elif "instagram.com" in home or "blog.naver" in home:
                            need = "80%" # 인스타나 블로그만 있음 (강력 타겟)
                        else:
                            need = "40%" # 기존 홈페이지 있음
                            
                        all_places.append({
                            "category": "숙박업",
                            "link": f"https://m.place.naver.com/accommodation/{pid}/home",
                            "need": need,
                            "name": name,
                            "folder": f"260930-{re.sub(r'[^가-힣a-zA-Z0-9]', '', name)[:10]}",
                            "deployUrl": "",
                            "status": "수집대기",
                            "photoDb": "대기",
                            "tel": tel,
                            "addr": addr,
                            "price": "250000",
                            "sns1": home if ("blog.naver" in home or "instagram" in home) else "",
                            "sns2": "",
                            "sns3": "",
                            "homepage": home if ("blog" not in home and "instagram" not in home) else "",
                            "etc": ""
                        })
    except Exception as e:
        print(f"Query {q} error: {e}")

print(f"Total collected west Jeju stays: {len(all_places)}")
with open("tools/west_jeju_collected.json", "w", encoding="utf-8") as f:
    json.dump(all_places, f, ensure_ascii=False, indent=2)

for p in all_places[:10]:
    print(f"[{p['need']}] {p['name']} | {p['addr']} | {p['tel']} | {p['link']}")
