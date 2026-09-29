import urllib.request
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect a few places for photos: 모험담(1716272359), 평정심(1214240071), 하이제인(38448679)
pids = ["1716272359", "1214240071", "38448679"]
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}

for pid in pids:
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        
    m = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});', html)
    if m:
        data = json.loads(m.group(1))
        # Find images
        found_imgs = []
        for k, v in data.items():
            if isinstance(v, dict):
                for img_k in ['origin', 'url', 'imageUrl']:
                    val = str(v.get(img_k, ''))
                    if 'ldb-phinf.pstatic.net' in val or 'naver.net' in val:
                        found_imgs.append(val)
        found_imgs = list(dict.fromkeys(found_imgs))
        print(f"Place {pid} found images in home: {len(found_imgs)}")
        for img in found_imgs[:3]:
            print("  ", img)
