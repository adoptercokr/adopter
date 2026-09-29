import urllib.request
import urllib.parse
import json
import re

query = "제주 애월 풀빌라 펜션"
encoded_query = urllib.parse.quote(query)
url = f"https://map.naver.com/p/api/search/allSearch?query={encoded_query}&type=all&searchCoord=126.32%3B33.46"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://map.naver.com/'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        places = res.get('result', {}).get('place', {}).get('list', [])
        print(f"Found {len(places)} places for query '{query}'!")
        for p in places[:10]:
            name = p.get('name')
            pid = p.get('id')
            addr = p.get('roadAddress') or p.get('address')
            tel = p.get('tel')
            homepage = p.get('homePage')
            print(f"- [{pid}] {name} | {tel} | {addr} | Homepage: {homepage}")
except Exception as e:
    print(f"Error: {e}")
