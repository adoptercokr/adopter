import urllib.request
import re
import json

with open("tools/west_10_collected.json", "r", encoding="utf-8") as f:
    items = json.load(f)

headers = {'User-Agent': 'Mozilla/5.0'}

print("=== 1차 10곳 실제 홈페이지 보유 여부 정밀 진단 ===")
for it in items:
    m = re.search(r'/accommodation/(\d+)', it['naverLink'])
    if not m:
        continue
    pid = m.group(1)
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        
        # Look for custom homepages
        links = re.findall(r'https?://[a-zA-Z0-9.\-_/]+', html)
        external_web = []
        for l in links:
            if any(domain in l for domain in ['imweb.me', '.co.kr', '.com', '.kr', 'modoo.at']):
                if not any(x in l for x in ['naver.com', 'pstatic.net', 'google', 'instagram.com', 'facebook.com', 'schema.org', 'w3.org']):
                    if l not in external_web:
                        external_web.append(l)
                        
        print(f"[{it['name']}]")
        if external_web:
            print(f"   -> ⚠️ 이미 자체 웹사이트 보유: {external_web[:2]} (필요도: 10~20% 낮음)")
        else:
            print(f"   -> ✅ 자체 웹사이트 없음! (인스타/네이버만 사용 중 - 필요도: 90% 극상 타겟)")
    except Exception as e:
        print(f"[{it['name']}] 에러: {e}")
