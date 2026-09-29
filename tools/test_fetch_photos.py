import urllib.request
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pid = "1716272359" # 모험담
url = f"https://m.place.naver.com/accommodation/{pid}/photo"
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
    
    # 1. ldb-phinf.pstatic.net
    phinf_urls = re.findall(r'https://ldb-phinf\.pstatic\.net/[a-zA-Z0-9_\-/]+\.(?:jpg|jpeg|png)', html)
    print(f"Direct phinf regex matches: {len(phinf_urls)}")
    
    # 2. window.__APOLLO_STATE__
    m = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});', html)
    if m:
        data = json.loads(m.group(1))
        photos = []
        for k, v in data.items():
            if isinstance(v, dict):
                for img_key in ['origin', 'url']:
                    if img_key in v and str(v[img_key]).startswith('http'):
                        photos.append(v[img_key])
        photos = list(dict.fromkeys(photos))
        print(f"Apollo state photo matches: {len(photos)}")
        for p in photos[:5]:
            print("  Photo:", p)
except Exception as e:
    print("Error:", e)
