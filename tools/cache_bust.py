import os, re
for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    p = os.path.join('Customer', d, 'index.html')
    if not os.path.exists(p): continue
    with open(p, 'r', encoding='utf-8') as f: html = f.read()
    
    # Check if already has v=
    if '?v=' not in html:
        html = html.replace('src="./stay_config.js"', 'src="./stay_config.js?v=2"')
    else:
        # increment version
        html = re.sub(r'src="\./stay_config\.js\?v=(\d+)"', lambda m: f'src="./stay_config.js?v={int(m.group(1))+1}"', html)
        
    with open(p, 'w', encoding='utf-8') as f: f.write(html)
