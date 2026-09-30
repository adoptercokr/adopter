import os, re
def fix(p):
    if not os.path.exists(p): return
    with open(p, 'r', encoding='utf-8') as f: js = f.read()
    js = js.replace('icon: "<svg', "icon: '<svg")
    js = js.replace('</svg>", title:', "</svg>', title:")
    with open(p, 'w', encoding='utf-8') as f: f.write(js)
    print("Fixed", p)
fix('Customer/260930-aewolrowa/stay_config.js')
fix('Customer/260930-staypanpo/stay_config.js')
