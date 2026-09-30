import os, re

for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    p = os.path.join('Customer', d, 'stay_config.js')
    if not os.path.exists(p): continue
    
    with open(p, 'r', encoding='utf-8') as f:
        js = f.read()
    
    def clean_name(m):
        raw = m.group(1)
        # e.g., "260930-peaceofmind-평정심" -> "평정심"
        # "260930-staypanpo-판포포구" -> "판포포구"
        # "260930-cloudhouse-클라우드하우스" -> "클라우드하우스"
        # If it has a korean part, take that. Otherwise, strip 260930-
        parts = raw.split('-')
        if len(parts) >= 3:
            name = parts[-1]
        else:
            name = parts[-1]
        return f'name: "{name}"'
        
    new_js = re.sub(r'name:\s*"([^"]*260930-[^"]*)"', clean_name, js)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_js)
