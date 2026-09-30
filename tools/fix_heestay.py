import os
p = 'templates/01-stay/stay_config.js'
with open(p, 'r', encoding='utf-8') as f: js = f.read()
if 'variant:' not in js:
    js = js.replace('const STAY_CONFIG = {', 'const STAY_CONFIG = {\n  variant: 1,\n  naverLink: "https://m.place.naver.com/accommodation/1647416345/home",')
with open(p, 'w', encoding='utf-8') as f: f.write(js)
