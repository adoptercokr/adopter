import json
import urllib.request
import re

url = "https://m.place.naver.com/accommodation/1684347780/home" # aewolrowa
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
    if state_match:
        state = json.loads(state_match.group(1))
        raw = json.dumps(state)
        # Find ANY image URLs
        urls = set(re.findall(r'https://[^"\s]+?\.jpg[^\s"\']*', raw))
        print("FOUND URLS:")
        for u in urls:
            print(u)
except Exception as e:
    print(e)
