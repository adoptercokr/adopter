with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
import json

match = re.search(r'export const routeMap = (\{.*?\});', js)
if match:
    route_map = json.loads(match.group(1).replace("'", '"'))
    route_map['peaceofmind'] = '260930-peaceofmind'
    route_map['cloudhouse'] = '260930-cloudhouse'
    route_map['dalsoop'] = '260930-dalsoop'
    route_map['hijane'] = '260930-hijane'
    route_map['dumomansion'] = '260930-dumomansion'
    route_map['late-summer'] = '260930-late-summer'
    route_map['seolchon'] = '260930-seolchon'
    route_map['wolla'] = '260930-wolla'
    route_map['saerok'] = '260930-stay-2045570969' # the last one
    
    new_js = "export const routeMap = " + json.dumps(route_map) + ";"
    with open('functions/_route_map.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Updated _route_map.js")
