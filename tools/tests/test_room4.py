import re, json
with open('temp_room.html', 'r', encoding='utf-8', errors='ignore') as f: html = f.read()
m = re.search(r'__PLACE_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
if m:
    state = json.loads(m.group(1))
    print(list(state.keys()))
    if 'rooms' in state: print('Rooms:', state['rooms'])
