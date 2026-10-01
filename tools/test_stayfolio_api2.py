import urllib.request
import json
import re

req = urllib.request.Request('https://www.stayfolio.com/findstay?city=gangwon-do', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
data = json.loads(match.group(1))
build_id = data['buildId']
api_url = f"https://www.stayfolio.com/_next/data/{build_id}/ko/findstay.json?city=gangwon-do"
req2 = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
api_data = json.loads(urllib.request.urlopen(req2).read().decode('utf-8'))
queries = api_data['pageProps']['dehydratedState']['queries']
for i, q in enumerate(queries):
    query_key = q.get('queryKey', [])
    if 'findStays' in str(query_key):
        print(f"Query {i}: {query_key}")
        state_data = q['state']['data']
        print(list(state_data.keys()))
        if 'pages' in state_data:
            print("Found pages")
        else:
            print("No pages. Dump:", str(state_data)[:200])
