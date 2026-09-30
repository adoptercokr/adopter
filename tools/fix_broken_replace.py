import os
def fix_all():
    customer_dir = 'Customer'
    for d in os.listdir(customer_dir):
        if not d.startswith('260930-'): continue
        p = os.path.join(customer_dir, d, 'stay_config.js')
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                js = f.read()
            
            # fix the broken facilities replacement
            import re
            js = re.sub(r'\{\s*variant:\s*\d+,\s*naverLink:\s*"[^"]+",\s*name:\s*', '{ name: ', js)
            
            with open(p, 'w', encoding='utf-8') as f:
                f.write(js)
            print(f"Fixed {d}")
fix_all()
