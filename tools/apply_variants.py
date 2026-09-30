import os, json, re, shutil, random

def fix_all():
    with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f: d1 = json.load(f)
    with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f: d2 = json.load(f)
    items = d1 + d2
    
    for item in items:
        folder = "260930-" + (item.get('folder', '').split('-')[-1] or item.get('subdomain'))
        p = os.path.join('Customer', folder, 'stay_config.js')
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                js = f.read()
            
            # 1. Random layout variant
            variant = random.randint(1, 4)
            
            # 2. Add naver link and variant
            nl = item.get('naverLink', '')
            if 'naverLink:' not in js:
                js = js.replace('name: "', f'variant: {variant},\n  naverLink: "{nl}",\n  name: "')
                
            # 3. Fix fake prices
            js = js.replace('weekday: "200,000"', 'weekday: "0"')
            js = js.replace('weekend: "250,000"', 'weekend: "0"')
            js = js.replace('peak: "250,000"', 'peak: "0"')
            
            with open(p, 'w', encoding='utf-8') as f:
                f.write(js)
                
            # Copy new index.html
            shutil.copy2('templates/01-stay/index.html', os.path.join('Customer', folder, 'index.html'))
            print(f"Updated {folder} with variant {variant}")

fix_all()
