import os
import json

def fix_again():
    with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f: d1 = json.load(f)
    with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f: d2 = json.load(f)
    items = d1 + d2
    
    for item in items:
        folder = "260930-" + (item.get('folder', '').split('-')[-1] or item.get('subdomain'))
        p = os.path.join('Customer', folder, 'stay_config.js')
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                js = f.read()
            
            # If variant isn't at the top, add it
            if 'variant:' not in js:
                import random
                v = random.randint(1, 4)
                nl = item.get('naverLink', '')
                js = js.replace('const STAY_CONFIG = {', f'const STAY_CONFIG = {{\n  variant: {v},\n  naverLink: "{nl}",')
            
            with open(p, 'w', encoding='utf-8') as f:
                f.write(js)
            print(f"Fixed {folder}")
fix_again()
