import urllib.request
import urllib.parse

img_url = 'https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230531_252%2F1685514605159wG7f3_JPEG%2FIMG_2961.jpeg'
proxy_url = f'https://adopter.co.kr/api/img?url={urllib.parse.quote(img_url)}'
req = urllib.request.Request(proxy_url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})
try:
    resp = urllib.request.urlopen(req, timeout=15)
    print("Image fetch success! Bytes:", len(resp.read()))
except Exception as e:
    print(e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8'))
