import os
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)

configs = [
    {"id": "interview", "rooms": ["프라이빗 풀빌라"]},
    {"id": "uretreat", "rooms": ["유리트리트 A동", "유리트리트 B동"]},
    {"id": "stjohns", "rooms": ["이그제큐티브 스위트"]},
    {"id": "heritage", "rooms": ["헤리티지 본채", "헤리티지 사랑채"]},
    {"id": "ramada", "rooms": ["펜트하우스"]},
    {"id": "surfyy", "rooms": ["서피 카바나"]},
    {"id": "oceanview", "rooms": ["오션뷰 디럭스", "오션뷰 스위트"]},
    {"id": "delpino", "rooms": ["로얄 스위트"]},
    {"id": "flora", "rooms": ["플로라 독채"]},
    {"id": "solsuite", "rooms": ["쏠비치 산토리니", "쏠비치 아쿠아"]}
]

for c in configs:
    folder = os.path.join(ADOPTER_DIR, c['id'])
    
    # 1. Update index.html
    html_path = os.path.join(folder, 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Rename rooms
        if len(c['rooms']) >= 1:
            html = html.replace("첫번째모험담", c['rooms'][0])
            html = html.replace("첫번째모험", c['rooms'][0])
        if len(c['rooms']) >= 2:
            html = html.replace("두번째모험담", c['rooms'][1])
            html = html.replace("두번째모험", c['rooms'][1])
            
        # Hide unused rooms
        hide_css = "<style>\n"
        if len(c['rooms']) == 1:
            hide_css += "#roomTab2, #roomTab3, #priceTab2, #priceTab3 { display: none !important; }\n"
        elif len(c['rooms']) == 2:
            hide_css += "#roomTab3, #priceTab3 { display: none !important; }\n"
        hide_css += "</style>\n</head>"
        
        html = html.replace("</head>", hide_css)
        
        # General Moheomdam replace
        html = re.sub(r'모험담(?!\.adopter)', c['rooms'][0].split()[0], html) # Replace generic 모험담 with first word of room
        html = html.replace('MOHEOMDAM', c['rooms'][0].split()[0].upper())
        html = html.replace('moheomdam.adopter.co.kr', f"{c['id']}.adopter.co.kr")
        html = html.replace('instagram.com/moheomdam', f"instagram.com/{c['id']}")
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
    # 2. Update stay_config.js
    cfg_path = os.path.join(folder, 'stay_config.js')
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            
        if len(c['rooms']) >= 1:
            cfg = cfg.replace("첫번째모험담", c['rooms'][0])
            cfg = cfg.replace("첫번째모험", c['rooms'][0])
        if len(c['rooms']) >= 2:
            cfg = cfg.replace("두번째모험담", c['rooms'][1])
            cfg = cfg.replace("두번째모험", c['rooms'][1])
            
        cfg = re.sub(r'모험담(?!\.adopter)', c['rooms'][0].split()[0], cfg)
        cfg = cfg.replace('MOHEOMDAM', c['rooms'][0].split()[0].upper())
        cfg = cfg.replace('moheomdam.adopter.co.kr', f"{c['id']}.adopter.co.kr")
        cfg = cfg.replace('instagram.com/moheomdam', f"instagram.com/{c['id']}")
        
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(cfg)
            
    print(f"Fixed {c['id']}")

