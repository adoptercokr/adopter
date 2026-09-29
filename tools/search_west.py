import urllib.request
import urllib.parse
import json

query = "제주 애월 독채펜션"
encoded_query = urllib.parse.quote(query)
# Jeju west coords: 126.32;33.46
url = f"https://map.naver.com/p/api/search/allSearch?query={encoded_query}&type=all&searchCoord=126.32%3B33.46"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://map.naver.com/'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    place = res.get('result', {}).get('place', {})
    items = place.get('list', [])
    print(f"Total found: {place.get('totalCount')} | Fetched: {len(items)}")
    
    results = []
    for it in items:
        pid = it.get('id')
        name = it.get('name')
        tel = it.get('tel')
        addr = it.get('roadAddress') or it.get('address')
        homepage = it.get('homePage') or ""
        
        # Calculate website necessity (홈페이지 필요도)
        # If no custom website (or only naver/insta), need is high (80~90%)
        need = "90%" if not homepage else ("70%" if ("instagram.com" in homepage or "blog.naver" in homepage) else "30%")
        
        results.append({
            "pid": pid,
            "name": name,
            "link": f"https://m.place.naver.com/accommodation/{pid}/home",
            "tel": tel,
            "addr": addr,
            "homepage": homepage,
            "need": need
        })
        print(f"[{need}] {name} ({pid}) - {addr} | Tel: {tel} | Web: {homepage}")

    with open("tools/west_jeju_candidates.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
