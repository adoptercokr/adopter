import re, json
with open('temp_room.html', 'r', encoding='utf-8', errors='ignore') as f: html = f.read()
state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
if state_match:
    state = json.loads(state_match.group(1))
    raw = json.dumps(state, ensure_ascii=False)
    
    # prices
    prices = re.findall(r'"price":(\d+)', raw)
    print('Prices:', sorted(list(set(int(p) for p in prices))))
    
    # names
    names = re.findall(r'"name":"([^"]+)"', raw)
    print('Names:', list(set(names))[:20])
