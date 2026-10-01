import urllib.request
import json
import re

req = urllib.request.Request('https://www.stayfolio.com/findstay?city=jeju-do', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        
        # Look for the buildId in __NEXT_DATA__
        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
        if match:
            data = json.loads(match.group(1))
            build_id = data.get('buildId')
            print("Build ID:", build_id)
            
            # Now fetch the data JSON
            # _next/data/{buildId}/ko/findstay.json?city=jeju-do
            api_url = f"https://www.stayfolio.com/_next/data/{build_id}/ko/findstay.json?city=jeju-do"
            print("Fetching:", api_url)
            
            req2 = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req2) as resp2:
                api_data = json.loads(resp2.read().decode('utf-8'))
                print("API data keys:", api_data.keys())
                
                # Check for dehydratedState
                queries = api_data['pageProps']['dehydratedState']['queries']
                for q in queries:
                    if 'queryKey' in q and 'stays' in str(q['queryKey']):
                        stays = q['state']['data']['edges']
                        print(f"Found {len(stays)} stays!")
                        for edge in stays[:3]:
                            print(edge['node']['title'])
except Exception as e:
    print("Failed:", e)
