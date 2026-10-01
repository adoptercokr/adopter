import urllib.request
import urllib.parse
img_url = 'https://ldb-phinf.pstatic.net/20230531_252/1685514605159wG7f3_JPEG/IMG_2961.jpeg'
proxy_url = f'https://adopter.co.kr/api/img?url={urllib.parse.quote(img_url)}'
print("Fetching:", proxy_url)
req = urllib.request.Request(proxy_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    print("Success! Bytes:", len(resp.read()))
except Exception as e:
    print(e)
