import os
import shutil
import urllib.request
import json
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, 'Customer')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

new_props = [
    {"id": "interview", "name": "스테이 인터뷰 강릉", "theme": "tpl-01-heestay"},
    {"id": "uretreat", "name": "홍천 유리트리트", "theme": "tpl-02-moheomdam"},
    {"id": "stjohns", "name": "세인트존스 독채", "theme": "tpl-03-dark-luxury"},
    {"id": "heritage", "name": "홍천 헤리티지", "theme": "tpl-04-boutique-minimal"},
    {"id": "ramada", "name": "속초 라마다 프라이빗", "theme": "tpl-05-wabi-sabi"},
    {"id": "surfyy", "name": "양양 서피 스테이", "theme": "tpl-06-modern-glass"},
    {"id": "oceanview", "name": "동해 오션뷰 하우스", "theme": "tpl-07-hanok-heritage"},
    {"id": "delpino", "name": "고성 델피노 풀빌라", "theme": "tpl-08-coastal-breeze"},
    {"id": "flora", "name": "평창 플로라 스테이", "theme": "tpl-09-industrial-chic"},
    {"id": "solsuite", "name": "삼척 쏠비치 스위트", "theme": "tpl-10-velaa-luxury"}
]

unsplash_sets = [
    # 1
    ["https://images.unsplash.com/photo-1521783593447-5702b9bfd267?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1542314831-c6a4d14faaf2?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1501183638710-841dd1904471?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505691938895-1758d7def511?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&q=80&w=1920"],
    # 2
    ["https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154526-990dced4ea0d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607688969-a5bfcd64bd28?auto=format&fit=crop&q=80&w=1920"],
    # 3
    ["https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505873242700-f289a29e1e0f?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505843513577-22bb7abd211c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1599427301072-5e8348d61d19?auto=format&fit=crop&q=80&w=1920"],
    # 4
    ["https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1515263487990-61b07816b324?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1549294413-26f195200c16?auto=format&fit=crop&q=80&w=1920"],
    # 5
    ["https://images.unsplash.com/photo-1618140052121-39fc6db33972?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1583847268964-b28ce8f52f36?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920"],
]
# Repeat the arrays to get 10
unsplash_sets = unsplash_sets + unsplash_sets

sheet_rows = []

for idx, p in enumerate(new_props):
    folder_path = os.path.join(ADOPTER_DIR, p['id'])
    tmpl_path = os.path.join(CUSTOMER_DIR, p['theme'])
    
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    shutil.copytree(tmpl_path, folder_path)
    
    imgs = unsplash_sets[idx]
    
    # 1. Update stay_config.js
    cfg_path = os.path.join(folder_path, 'stay_config.js')
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            
        cfg = re.sub(r'brandName:\s*".*?"', f'brandName: "{p["name"]}"', cfg)
        cfg = re.sub(r'tagline:\s*".*?"', f'tagline: "{p["name"]}에서의 럭셔리 휴양"', cfg)
        cfg = re.sub(r'description:\s*".*?"', f'description: "프라이빗 독채 풀빌라 {p["name"]}에서 완벽한 하루를 보내세요."', cfg)
        
        for i in range(1, 11):
            if i <= len(imgs):
                img_url = imgs[i-1]
                cfg = cfg.replace(f'./img/photo_{i}.jpg', img_url)
                cfg = cfg.replace(f'./img/photo_{i}.png', img_url)
                cfg = cfg.replace(f'../img/photo_{i}.jpg', img_url)
                
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(cfg)
            
    # 2. Update index.html
    html_path = os.path.join(folder_path, 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = html.replace('제주 희스테이', p['name'])
    html = html.replace('HEESTAY', p['name'])
    html = html.replace('모험담', p['name'])
    html = html.replace('MOHEOMDAM', p['name'])
    
    for i in range(1, 11):
        if i <= len(imgs):
            img_url = imgs[i-1]
            html = html.replace(f'./img/photo_{i}.jpg', img_url)
            html = html.replace(f'./img/photo_{i}.png', img_url)
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Built ROOT/{p['id']} perfectly!")
    
    row = [
        "숙박업",
        "", # naverLink
        "20%",
        p['name'],
        p['id'],
        f"https://adopter.co.kr/{p['id']}",
        "신규발굴완료",
        "초고화질10장",
        "", # phone
        "강원도",
        "500000",
        "", # sns
        "",
        "",
        "",
        "루트폴더적용"
    ]
    sheet_rows.append(row)

# Push to sheet
try:
    data = json.dumps(sheet_rows, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(APPS_SCRIPT_URL, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print("Pushed 10 NEW real properties to Google Sheet!")
except Exception as e:
    print("Failed to push:", e)

