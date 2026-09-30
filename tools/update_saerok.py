import json

with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace "saerok": "260930-stay-2045570969" with "saerok": "260930-stay"
js = js.replace('"saerok": "260930-stay-2045570969"', '"saerok": "260930-stay"')

with open('functions/_route_map.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated route map")
