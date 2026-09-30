import re, json
with open('temp.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
state = json.loads(state_match.group(1))

def find_keys(d, target, path=""):
    if isinstance(d, dict):
        for k, v in d.items():
            if target.lower() in k.lower(): print(f'{path}.{k}')
            if isinstance(v, str) and len(v) > 50 and '머묾' not in v and '수영장' in v:
                print('DESC_CANDIDATE:', v[:100])
            find_keys(v, target, path + "." + k)
    elif isinstance(d, list):
        for i, item in enumerate(d):
            find_keys(item, target, path + f"[{i}]")

find_keys(state, 'amenit')
find_keys(state, 'facilit')
find_keys(state, 'desc')

# Let's find rooms
rooms = []
for k, v in state.items():
    if k.startswith('BizItem:') or k.startswith('AccommodationRoom:'):
        if 'name' in v: print('ROOM:', v['name'])
    if 'description' in k:
        print('DESC_KEY:', k, str(v)[:100])
