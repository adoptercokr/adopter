import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'ko-KR,ko;q=0.9'
}

req = urllib.request.Request("https://m.place.naver.com/accommodation/1716272359/photo?filterType=%EC%97%85%EC%B2%B4", headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

# Extract all photo URLs
imgs = re.findall(r'https://[a-zA-Z0-9_\-\./]+ldb-phinf\.pstatic\.net/[a-zA-Z0-9_\-\./]+(?:\.jpg|\.png|\.jpeg)', html)
booking_imgs = re.findall(r'https://[a-zA-Z0-9_\-\./]+naverbooking-phinf\.pstatic\.net/[a-zA-Z0-9_\-\./]+(?:\.jpg|\.png|\.jpeg)', html)

all_imgs = list(dict.fromkeys(imgs + booking_imgs))
print(f"Total photos found from 업체 탭: {len(all_imgs)}")
for i, img in enumerate(all_imgs[:25]):
    print(f"  [{i+1}] {img}")

with open("tools/moheomdam_official_photos.json", "w", encoding="utf-8") as f:
    json.dump(all_imgs, f, indent=2)
