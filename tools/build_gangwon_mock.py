import os
import re
import shutil
import json
import urllib.request

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, 'Customer')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

properties = [
    {'name': '스테이 서리달', 'subdomain': 'seoridal', 'address': '강원도 양양군 현북면', 'phone': '010-1111-2222', 'price': '450000', 'theme': 'tpl-05-wabi-sabi'},
    {'name': '강릉 호수정담', 'subdomain': 'hosu', 'address': '강원도 강릉시 저동', 'phone': '010-2222-3333', 'price': '500000', 'theme': 'tpl-06-modern-glass'},
    {'name': '속초 이움', 'subdomain': 'ium', 'address': '강원도 속초시 대포동', 'phone': '010-3333-4444', 'price': '400000', 'theme': 'tpl-07-hanok-heritage'},
    {'name': '평창 고요재', 'subdomain': 'goyo', 'address': '강원도 평창군 봉평면', 'phone': '010-4444-5555', 'price': '600000', 'theme': 'tpl-08-coastal-breeze'},
    {'name': '고성 르메르', 'subdomain': 'lemer', 'address': '강원도 고성군 토성면', 'phone': '010-5555-6666', 'price': '550000', 'theme': 'tpl-09-industrial-chic'},
    {'name': '양양 브리드', 'subdomain': 'breathe', 'address': '강원도 양양군 강현면', 'phone': '010-6666-7777', 'price': '700000', 'theme': 'tpl-10-velaa-luxury'},
    {'name': '홍천 소노펠리체', 'subdomain': 'sono', 'address': '강원도 홍천군 서면', 'phone': '010-7777-8888', 'price': '350000', 'theme': 'tpl-05-wabi-sabi'},
    {'name': '동해 묵호별장', 'subdomain': 'mukho', 'address': '강원도 동해시 묵호동', 'phone': '010-8888-9999', 'price': '450000', 'theme': 'tpl-06-modern-glass'},
    {'name': '삼척 쏠비치 프라이빗', 'subdomain': 'solbeach', 'address': '강원도 삼척시 갈천동', 'phone': '010-9999-0000', 'price': '800000', 'theme': 'tpl-07-hanok-heritage'},
    {'name': '정선 파크로쉬', 'subdomain': 'parkroche', 'address': '강원도 정선군 북평면', 'phone': '010-0000-1111', 'price': '650000', 'theme': 'tpl-08-coastal-breeze'}
]

# Random Unsplash architecture / interior images for luxury look
unsplash_images = [
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600585154526-990dced4ea0d?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&q=80&w=1200',
    'https://images.unsplash.com/photo-1600607688969-a5bfcd64bd28?auto=format&fit=crop&q=80&w=1200'
]

sheet_data = []
route_map_adds = []

for prop in properties:
    folder_name = f"261001-gangwon-{prop['subdomain']}"
    folder_path = os.path.join(CUSTOMER_DIR, folder_name)
    tmpl_path = os.path.join(CUSTOMER_DIR, prop['theme'])
    
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    shutil.copytree(tmpl_path, folder_path)
    
    # Rewrite config
    cfg_path = os.path.join(folder_path, 'stay_config.js')
    with open(cfg_path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        
    cfg = re.sub(r'brandName:\s*".*?"', f'brandName: "{prop["name"]}"', cfg)
    cfg = re.sub(r'address:\s*".*?"', f'address: "{prop["address"]}"', cfg)
    cfg = re.sub(r'phone:\s*".*?"', f'phone: "{prop["phone"]}"', cfg)
    
    # Replace up to 10 images
    for idx in range(1, 11):
        proxy_url = unsplash_images[(idx-1) % len(unsplash_images)]
        cfg = cfg.replace(f'./img/photo_{idx}.jpg', proxy_url)
        cfg = cfg.replace(f'./img/photo_{idx}.png', proxy_url)
        
    with open(cfg_path, 'w', encoding='utf-8') as f:
        f.write(cfg)
        
    site_url = f"https://{prop['subdomain']}.adopter.co.kr"
    route_map_adds.append(f'  "{prop["subdomain"]}": "Customer/{folder_name}",')
    
    sheet_data.append({
        "name": prop['name'],
        "subdomain": prop['subdomain'],
        "theme": prop['theme'],
        "siteUrl": site_url,
        "naverUrl": "Unsplash Mock",
        "price": prop['price'],
        "phone": prop['phone'],
        "address": prop['address'],
        "memo": "강원도 신규 (Unsplash)"
    })
    print(f"Built {prop['name']}")
    
# Route map
rm_path = os.path.join(ADOPTER_DIR, 'functions', '_route_map.js')
with open(rm_path, 'r', encoding='utf-8') as f:
    rm = f.read()

insert_pos = rm.find('const routeMap = {') + len('const routeMap = {\n')
rm = rm[:insert_pos] + '\n'.join(route_map_adds) + '\n' + rm[insert_pos:]
with open(rm_path, 'w', encoding='utf-8') as f:
    f.write(rm)

# Push to sheet
req = urllib.request.Request(
    APPS_SCRIPT_URL,
    data=json.dumps(sheet_data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
try:
    urllib.request.urlopen(req)
    print("Pushed to Google Sheet!")
except Exception as e:
    print(f"Sheet push failed: {e}")
