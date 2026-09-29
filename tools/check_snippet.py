import re
import json

with open("tools/test_fetch.py", "r", encoding="utf-8") as f:
    pass

import urllib.request
url = 'https://m.place.naver.com/accommodation/1226740854/home'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')

# Search for "1226740854" in html
matches = [m.start() for m in re.finditer(r'1226740854', html)]
print(f"Occurrences of 1226740854: {len(matches)}")
for idx in matches[:5]:
    snippet = html[max(0, idx-50):min(len(html), idx+200)]
    print("--- SNIPPET ---")
    print(snippet)

# Search for window.__ or __NEXT or similar
found_vars = re.findall(r'window\.([a-zA-Z0-9_]+)\s*=', html)
print("Found window vars:", found_vars)
