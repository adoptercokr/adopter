import urllib.request
import urllib.parse
import re

url = 'https://m.place.naver.com/accommodation/2036409548/home'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        match = re.search(r'(https://ldb-phinf\.pstatic\.net/[^"\'\s>]+)', html)
        if match:
            valid_img = match.group(1)
            print("Found valid img:", valid_img)
            
            # Test proxy
            proxy_url = f'https://adopter.co.kr/api/img?url={urllib.parse.quote(valid_img)}'
            req2 = urllib.request.Request(proxy_url, headers={'User-Agent': 'Mozilla/5.0'})
            resp2 = urllib.request.urlopen(req2)
            print("Proxy success! Bytes:", len(resp2.read()))
        else:
            print("No image found.")
except Exception as e:
    print("Failed:", e)
