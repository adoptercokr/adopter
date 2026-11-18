import re, json
with open('temp.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
if state_match:
    state = json.loads(state_match.group(1))
    for k in state.keys():
        if 'Accommodation' in k or 'Biz' in k or 'Place' in k:
            print(k)
            for subk in state[k]:
                print('  -', subk)
