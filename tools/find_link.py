import urllib.request
import urllib.parse
import re

q = '제주 사누르제주'
url = f'https://search.naver.com/search.naver?query={urllib.parse.quote(q)}'
headers = {'User-Agent': 'Mozilla/5.0'}
with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as resp:
    html = resp.read().decode('utf-8')
    links = re.findall(r'https?://[a-zA-Z0-9./_\-?=&;%]+', html)
    for l in links:
        if 'place.naver.com' in l or 'naver.me' in l or 'map.naver.com' in l:
            print("Matched link:", l)
