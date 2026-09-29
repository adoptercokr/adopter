import urllib.request
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pid = '1716272359'
url = f'https://m.place.naver.com/accommodation/{pid}/home'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

print('title:', re.findall(r'<title>(.*?)</title>', html))
print('og:title:', re.findall(r'<meta property="og:title" content="(.*?)"', html))
print('og:description:', re.findall(r'<meta property="og:description" content="(.*?)"', html))

# window.__APOLLO_STATE__
m = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});', html)
if m:
    data = json.loads(m.group(1))
    print('Apollo keys count:', len(data))
    for k, v in data.items():
        if isinstance(v, dict) and v.get('name') and not k.startswith('ROOT_'):
            print(f'Apollo place match -> id: {k}, name: {v.get("name")}, address: {v.get("roadAddress", v.get("address"))}, phone: {v.get("phone", v.get("virtualPhone"))}')
            if 'homepages' in v:
                print('   homepages in Apollo:', v.get('homepages'))
