import json

with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Extract the JSON object
import re
match = re.search(r'export const routeMap = (\{.*?\});', js)
route_map = json.loads(match.group(1))

# Add themes
route_map['theme1'] = 'tpl-01-heestay'
route_map['theme2'] = 'tpl-02-moheomdam'
route_map['theme3'] = 'tpl-03-dark-luxury'
route_map['theme4'] = 'tpl-04-boutique-minimal'
route_map['theme5'] = 'tpl-05-wabi-sabi'
route_map['theme6'] = 'tpl-06-modern-glass'
route_map['theme7'] = 'tpl-07-hanok-heritage'
route_map['theme8'] = 'tpl-08-coastal-breeze'
route_map['theme9'] = 'tpl-09-industrial-chic'
route_map['theme10'] = 'tpl-10-velaa-luxury'

new_js = f"export const routeMap = {json.dumps(route_map)};\n"
with open('functions/_route_map.js', 'w', encoding='utf-8') as f:
    f.write(new_js)
print("Added themes to routeMap")
