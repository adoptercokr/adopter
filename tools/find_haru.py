import os
for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    p = os.path.join('Customer', d, 'stay_config.js')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            if '하루를' in f.read():
                print("Found in", d)
