import json

with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace "late-summer": "260930-late-summer" with "late-summer": "260930-late"
js = js.replace('"late-summer": "260930-late-summer"', '"late-summer": "260930-late"')

with open('functions/_route_map.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated route map for late-summer")
