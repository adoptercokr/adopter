import urllib.request
import json
import re

try:
    req = urllib.request.Request('https://www.stayfolio.com/findstay?city=gangwon-do', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
    if match:
        data = json.loads(match.group(1))
        build_id = data['buildId']
        api_url = f"https://www.stayfolio.com/_next/data/{build_id}/ko/findstay.json?city=gangwon-do"
        req2 = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        api_data = json.loads(urllib.request.urlopen(req2).read().decode('utf-8'))
        stays = api_data['pageProps']['dehydratedState']['queries'][0]['state']['data']['pages'][0]['data']['stays']
        
        print(f"Found {len(stays)} stays!")
        for s in stays[:2]:
            print(s['title'], s['city'])
            print(s['images'][:2])
    else:
        print("No NEXT_DATA")
except Exception as e:
    print(e)
