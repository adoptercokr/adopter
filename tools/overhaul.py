import os
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)

# Configurations for all 10
configs = [
    {"id": "interview", "name": "스테이 인터뷰 강릉", "rooms": 1, "theme": "tpl-01"},
    {"id": "uretreat", "name": "홍천 유리트리트", "rooms": 2, "theme": "tpl-02"},
    {"id": "stjohns", "name": "세인트존스 독채", "rooms": 1, "theme": "tpl-03"},
    {"id": "heritage", "name": "홍천 헤리티지", "rooms": 2, "theme": "tpl-04"},
    {"id": "ramada", "name": "속초 라마다 프라이빗", "rooms": 1, "theme": "tpl-05"},
    {"id": "surfyy", "name": "양양 서피 스테이", "rooms": 1, "theme": "tpl-06"},
    {"id": "oceanview", "name": "동해 오션뷰 하우스", "rooms": 2, "theme": "tpl-07"},
    {"id": "delpino", "name": "고성 델피노 풀빌라", "rooms": 1, "theme": "tpl-08"},
    {"id": "flora", "name": "평창 플로라 스테이", "rooms": 1, "theme": "tpl-09"},
    {"id": "solsuite", "name": "삼척 쏠비치 스위트", "rooms": 2, "theme": "tpl-10"}
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
unsplash_sets = unsplash_sets + unsplash_sets

for idx, c in enumerate(configs):
    folder = os.path.join(ADOPTER_DIR, c['id'])
    html_path = os.path.join(folder, 'index.html')
    imgs = unsplash_sets[idx]
    
    if not os.path.exists(html_path):
        continue
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. FIX THE TEXT/TITLES IN ALL HTML
    # Catch any generic template names
    html = re.sub(r'<title>.*?</title>', f'<title>{c["name"]} | 럭셔리 프라이빗 스테이</title>', html)
    html = html.replace('Wabi-Sabi Stay', c['name'])
    html = html.replace('Modern Glass', c['name'])
    html = html.replace('Hanok Heritage', c['name'])
    html = html.replace('Coastal Breeze', c['name'])
    html = html.replace('Industrial Chic', c['name'])
    html = html.replace('Velaa Luxury', c['name'])
    html = html.replace('Luxury Stay', c['name'])
    
    # 2. FIX THE 3 ROOMS FOR tpl-01, tpl-02
    if c['theme'] in ['tpl-01', 'tpl-02']:
        if c['rooms'] == 1:
            # Physically remove room 2 and room 3 containers from the main grid
            html = re.sub(r'<!-- Room 2:.*?<!-- Room 3', '<!-- Room 3', html, flags=re.DOTALL)
            html = re.sub(r'<!-- Room 3:.*?(?=</section>)', '', html, flags=re.DOTALL)
            
            # Hide them in the CSS just in case
            hide_css = "<style>\n#roomTab2, #roomTab3, #priceTab2, #priceTab3 { display: none !important; }\n"
            hide_css += ".grid-cols-1.md\\:grid-cols-3 { grid-template-columns: repeat(1, minmax(0, 1fr)) !important; }\n"
            hide_css += "</style>\n</head>"
            html = html.replace("</head>", hide_css)
        elif c['rooms'] == 2:
            html = re.sub(r'<!-- Room 3:.*?(?=</section>)', '', html, flags=re.DOTALL)
            hide_css = "<style>\n#roomTab3, #priceTab3 { display: none !important; }\n"
            hide_css += ".grid-cols-1.md\\:grid-cols-3 { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }\n"
            hide_css += "</style>\n</head>"
            html = html.replace("</head>", hide_css)

    # 3. FIX THE PHOTOS (Subagents used hardcoded unsplash URLs)
    # Find all Unsplash URLs in the HTML
    unsplash_urls = re.findall(r'https://images\.unsplash\.com/[^"\']+', html)
    # Deduplicate while preserving order
    seen = set()
    unique_unsplash = [x for x in unsplash_urls if not (x in seen or seen.add(x))]
    
    for i, old_url in enumerate(unique_unsplash):
        if i < len(imgs):
            html = html.replace(old_url, imgs[i])
            
    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Completely overhauled {c['id']}")

