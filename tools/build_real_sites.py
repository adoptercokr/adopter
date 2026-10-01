import os
import shutil
import json
import urllib.request
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, 'Customer')

with open('tools/real_ig_photos.json', 'r', encoding='utf-8') as f:
    props = json.load(f)

# unique properties
unique_props = []
seen_names = set()
for p in props:
    if p['name'] not in seen_names:
        unique_props.append(p)
        seen_names.add(p['name'])
        
print(f"Building {len(unique_props)} unique properties")

route_map_adds = []

for idx, prop in enumerate(unique_props[:10]):
    theme_num = (idx % 10) + 1
    theme = f"tpl-{theme_num:02d}"
    if theme == 'tpl-01':
        theme = 'tpl-01-heestay'
    elif theme == 'tpl-02':
        theme = 'tpl-02-moheomdam'
    elif theme == 'tpl-03':
        theme = 'tpl-03-dark-luxury'
    elif theme == 'tpl-04':
        theme = 'tpl-04-boutique-minimal'
    elif theme == 'tpl-05':
        theme = 'tpl-05-wabi-sabi'
    elif theme == 'tpl-06':
        theme = 'tpl-06-modern-glass'
    elif theme == 'tpl-07':
        theme = 'tpl-07-hanok-heritage'
    elif theme == 'tpl-08':
        theme = 'tpl-08-coastal-breeze'
    elif theme == 'tpl-09':
        theme = 'tpl-09-industrial-chic'
    elif theme == 'tpl-10':
        theme = 'tpl-10-velaa-luxury'

    subdomain = f"real-{idx+1}"
    folder_name = f"261001-real-{idx+1}"
    folder_path = os.path.join(CUSTOMER_DIR, folder_name)
    tmpl_path = os.path.join(CUSTOMER_DIR, theme)
    
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    shutil.copytree(tmpl_path, folder_path)
    
    cfg_path = os.path.join(folder_path, 'stay_config.js')
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            
        cfg = re.sub(r'brandName:\s*".*?"', f'brandName: "{prop["name"]}"', cfg)
        
        for i in range(1, 11):
            if i <= len(prop['images']):
                img_url = prop['images'][i-1]
                cfg = cfg.replace(f'./img/photo_{i}.jpg', img_url)
                cfg = cfg.replace(f'./img/photo_{i}.png', img_url)
            
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(cfg)
            
    # Also update index.html if it's heestay or moheomdam (hardcoded images)
    if theme in ['tpl-01-heestay', 'tpl-02-moheomdam']:
        html_path = os.path.join(folder_path, 'index.html')
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        html = html.replace('제주 희스테이', prop['name'])
        html = html.replace('HEESTAY', prop['name'])
        html = html.replace('모험담', prop['name'])
        html = html.replace('MOHEOMDAM', prop['name'])
        
        for i in range(1, 11):
            if i <= len(prop['images']):
                img_url = prop['images'][i-1]
                html = html.replace(f'./img/photo_{i}.jpg', img_url)
                
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    route_map_adds.append(f'  "{subdomain}": "{folder_name}",')
    print(f"Built {prop['name']} with {theme} into {folder_name}")

rm_path = os.path.join(ADOPTER_DIR, 'functions', '_route_map.js')
with open(rm_path, 'r', encoding='utf-8') as f:
    rm = f.read()
insert_pos = rm.find('const routeMap = {') + len('const routeMap = {\n')
rm = rm[:insert_pos] + '\n'.join(route_map_adds) + '\n' + rm[insert_pos:]
with open(rm_path, 'w', encoding='utf-8') as f:
    f.write(rm)
