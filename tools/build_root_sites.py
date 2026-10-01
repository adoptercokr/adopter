import os
import shutil
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, 'Customer')

properties = [
    {
        "id": "camino", "name": "까미노데플로레스타", "theme": "tpl-01-heestay",
        "tagline": "홍천의 숲 속에서 만나는 완벽한 프라이빗 휴식",
        "desc": "자연과 동화되는 완전한 독채 풀빌라. 홍천강의 고요함 속에서 당신만의 럭셔리한 휴식을 경험하세요.",
        "imgs": ["https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154526-990dced4ea0d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "dalnosi", "name": "달노시 스테이", "theme": "tpl-02-moheomdam",
        "tagline": "달빛 아래 머무는 고즈넉한 시간",
        "desc": "일상의 소음을 벗어나 달빛이 내려앉는 마당에서 온전한 쉼을 누릴 수 있는 감성 스테이입니다.",
        "imgs": ["https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505843513577-22bb7abd211c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1501183638710-841dd1904471?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505691938895-1758d7def511?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "chungchun", "name": "청춘연가", "theme": "tpl-03-dark-luxury",
        "tagline": "젊음의 낭만이 머무는 모던 프라이빗 풀빌라",
        "desc": "블랙 앤 화이트의 세련된 인테리어와 압도적인 프라이빗 인피니티 풀을 자랑하는 하이엔드 펜션.",
        "imgs": ["https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505873242700-f289a29e1e0f?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "handam", "name": "스테이 한담", "theme": "tpl-04-boutique-minimal",
        "tagline": "바다를 품은 미니멀리즘 부티크 스테이",
        "desc": "여백의 미를 살린 건축물 안에서 푸른 바다의 윤슬을 감상하며 진정한 힐링을 경험하세요.",
        "imgs": ["https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1515263487990-61b07816b324?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "sanur", "name": "사누르제주", "theme": "tpl-05-wabi-sabi",
        "tagline": "발리의 감성을 제주에 온전히 담다",
        "desc": "이국적인 라탄 인테리어와 따뜻한 조명, 프라이빗 야외 수영장이 있는 감성 펜션입니다.",
        "imgs": ["https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1549294413-26f195200c16?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1618140052121-39fc6db33972?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "negeut", "name": "스테이 느긋", "theme": "tpl-06-modern-glass",
        "tagline": "시간이 멈춘 듯한 나른한 오후의 휴식",
        "desc": "통유리로 스며드는 따스한 햇살을 맞으며 커피 한 잔의 여유를 즐길 수 있는 모던 하우스.",
        "imgs": ["https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154526-990dced4ea0d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607688969-a5bfcd64bd28?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "haru", "name": "하루를품다", "theme": "tpl-07-hanok-heritage",
        "tagline": "전통과 현대가 조화롭게 어우러진 한옥 풀빌라",
        "desc": "서까래의 우아함과 최신식 스파의 편리함을 동시에 누리는 가장 한국적이고 럭셔리한 하루.",
        "imgs": ["https://images.unsplash.com/photo-1542314831-c6a4d14faaf2?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1501183638710-841dd1904471?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1505843513577-22bb7abd211c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "gyeot", "name": "곁겹", "theme": "tpl-08-coastal-breeze",
        "tagline": "바람이 머무는 아름다운 제주 해변의 숙소",
        "desc": "새하얀 톤의 극도의 미니멀리즘 인테리어. 파도 소리를 들으며 지친 마음을 위로받으세요.",
        "imgs": ["https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1515263487990-61b07816b324?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "plumeria", "name": "플루메리아 펜션", "theme": "tpl-09-industrial-chic",
        "tagline": "열대의 감성을 살린 트렌디한 인더스트리얼 스테이",
        "desc": "거친 질감의 콘크리트와 세련된 철제 가구가 빚어내는 독특한 분위기 속에서 자유를 느끼세요.",
        "imgs": ["https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1599427301072-5e8348d61d19?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1583847268964-b28ce8f52f36?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&q=80&w=1920"]
    },
    {
        "id": "solbeach", "name": "삼척 쏠비치 프라이빗", "theme": "tpl-10-velaa-luxury",
        "tagline": "최고급 어메니티와 압도적인 오션뷰 리조트",
        "desc": "그리스 산토리니를 연상케 하는 푸른 돔과 프라이빗 럭셔리 인피니티 풀에서 진정한 하이엔드 휴양을 경험하세요.",
        "imgs": ["https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1549294413-26f195200c16?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1618140052121-39fc6db33972?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=1920", "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&q=80&w=1920"]
    }
]

for p in properties:
    # We will build them directly at the ROOT of adopter, e.g., adopter/camino
    folder_path = os.path.join(ADOPTER_DIR, p['id'])
    tmpl_path = os.path.join(CUSTOMER_DIR, p['theme'])
    
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    shutil.copytree(tmpl_path, folder_path)
    
    # 1. Update stay_config.js
    cfg_path = os.path.join(folder_path, 'stay_config.js')
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            
        cfg = re.sub(r'brandName:\s*".*?"', f'brandName: "{p["name"]}"', cfg)
        cfg = re.sub(r'tagline:\s*".*?"', f'tagline: "{p["tagline"]}"', cfg)
        cfg = re.sub(r'description:\s*".*?"', f'description: "{p["desc"]}"', cfg)
        
        for i in range(1, 11):
            if i <= len(p['imgs']):
                img_url = p['imgs'][i-1]
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
    
    # Replace metadata text
    html = re.sub(r'<title>.*?</title>', f'<title>{p["name"]} | {p["tagline"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{p["desc"]}">', html)
    
    # Replace large header text if it exists (for Heestay/Moheomdam styles)
    html = re.sub(r'제주의 숲과 돌담에 둘러싸여.*?온전히 머무는 곳,', f'{p["tagline"]},', html, flags=re.DOTALL)
    
    for i in range(1, 11):
        if i <= len(p['imgs']):
            img_url = p['imgs'][i-1]
            html = html.replace(f'./img/photo_{i}.jpg', img_url)
            html = html.replace(f'./img/photo_{i}.png', img_url)
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Built ROOT/{p['id']} perfectly!")
