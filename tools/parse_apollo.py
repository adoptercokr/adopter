import re
import json
import urllib.request
import urllib.parse

url = 'https://m.place.naver.com/accommodation/1226740854/home'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')

idx = html.find('window.__APOLLO_STATE__')
if idx != -1:
    start_brace = html.find('{', idx)
    # Find matching closing brace
    depth = 0
    end_brace = -1
    in_string = False
    escape = False
    
    for i in range(start_brace, len(html)):
        c = html[i]
        if in_string:
            if escape:
                escape = False
            elif c == '\\':
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    end_brace = i
                    break
    
    if end_brace != -1:
        json_str = html[start_brace:end_brace+1]
        print(f"Extracted JSON! Length: {len(json_str)}")
        state = json.loads(json_str)
        
        # Analyze Accommodation Root
        for k, v in state.items():
            if isinstance(v, dict):
                name = v.get('name')
                road = v.get('roadAddress')
                phone = v.get('virtualPhone') or v.get('phone')
                if name and road:
                    print("Found Place Entity:", k)
                    print(f"Name: {name}")
                    print(f"Address: {road}")
                    print(f"Phone: {phone}")
                    print(f"Category: {v.get('category')}")
                    print(f"Description: {v.get('desc')}")
                    
        # Extract Photos
        photo_urls = []
        for k, v in state.items():
            if isinstance(v, dict) and 'url' in v and 'ldb-phinf.pstatic.net' in str(v.get('url')):
                photo_urls.append(v.get('url'))
                
        print(f"Found {len(photo_urls)} photos in Apollo state!")
        if photo_urls:
            print("Sample photo:", photo_urls[0])
            
        with open("tools/extracted_state.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        print("Saved extracted_state.json")
    else:
        print("Could not balance braces for __APOLLO_STATE__")
