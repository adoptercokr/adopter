import urllib.request
import urllib.parse
import json

query = "제주 애월 펜션"
encoded_query = urllib.parse.quote(query)
url = f"https://map.naver.com/p/api/search/allSearch?query={encoded_query}&type=all&searchCoord=126.32%3B33.46"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://map.naver.com/'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("Keys:", list(res.keys()))
    if 'result' in res and res['result']:
        print("Result keys:", list(res['result'].keys()))
    else:
        print("Response structure:", json.dumps(res, ensure_ascii=False)[:500])
