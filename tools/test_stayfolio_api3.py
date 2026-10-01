import urllib.request
import json
import re

req = urllib.request.Request('https://www.stayfolio.com/findstay?city=gangwon-do', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
data = json.loads(match.group(1))
with open('tools/stayfolio_dump.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Dumped to stayfolio_dump.json")
