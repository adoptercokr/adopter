import urllib.request
import re
import json

req = urllib.request.Request('https://www.stayfolio.com/findstay?city=jeju-do', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
        if match:
            data = json.loads(match.group(1))
            queries = data['props']['pageProps']['dehydratedState']['queries']
            for q in queries:
                if 'queryKey' in q:
                    print("QueryKey:", q['queryKey'])
                    if 'stays' in str(q['queryKey']):
                        stays = q['state']['data']['edges']
                        print(f"Found {len(stays)} stays!")
                        for edge in stays[:5]:
                            node = edge['node']
                            print(node.get('title'), node.get('defaultImage'))
        else:
            print("No NEXT_DATA found.")
except Exception as e:
    print("Failed:", e)
