with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    content = f.read()

addition = """  "namubat": "gw-namubat",
  "caminode": "gw-caminode",
  "narobuteo": "gw-narobuteo",
  "secretgarden": "gw-secretgarden",
  "privateyangyang": "gw-privateyangyang",
  "lahenne": "gw-lahenne",
  "uirim": "gw-uirim",
  "bebridge": "gw-bebridge",
  "urpoolvilla": "gw-urpoolvilla",
  "migallu": "gw-migallu",
"""

if 'namubat' not in content:
    content = content.replace('export const routeMap = {', 'export const routeMap = {\n' + addition)
    with open('functions/_route_map.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated route map successfully!')
else:
    print('Already present')
