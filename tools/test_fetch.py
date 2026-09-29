import urllib.request
import re
import json

url = 'https://m.place.naver.com/accommodation/1226740854/home'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        print(f"HTML Fetched successfully! Length: {len(html)}")
        
        # Look for window.__APOLLO_STATE__
        match = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});</script>', html)
        if match:
            raw_json = match.group(1)
            print(f"Found __APOLLO_STATE__! Length: {len(raw_json)}")
            data = json.loads(raw_json)
            with open("tools/apollo_dump.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Saved to tools/apollo_dump.json")
        else:
            # Look for NEXT_DATA
            match2 = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.+?)</script>', html)
            if match2:
                print(f"Found __NEXT_DATA__! Length: {len(match2.group(1))}")
                data2 = json.loads(match2.group(1))
                with open("tools/next_dump.json", "w", encoding="utf-8") as f:
                    json.dump(data2, f, ensure_ascii=False, indent=2)
                print("Saved to tools/next_dump.json")
            else:
                print("Could not find state in HTML. Checking script tags...")
                scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
                print(f"Total script tags: {len(scripts)}")
except Exception as e:
    print(f"Error: {e}")
