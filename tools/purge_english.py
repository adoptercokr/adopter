import os
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)

# Configurations for all 10
configs = [
    {"id": "interview", "name": "스테이 인터뷰 강릉", "desc": "강릉의 맑은 바다와 소나무 숲이 어우러진 완벽한 프라이빗 독채 스테이. 오직 한 팀만을 위한 고요한 공간입니다."},
    {"id": "uretreat", "name": "홍천 유리트리트", "desc": "홍천강이 내려다보이는 럭셔리 풀빌라. 노출 콘크리트의 웅장함과 자연이 조화를 이루는 완벽한 휴식처입니다."},
    {"id": "stjohns", "name": "세인트존스 독채", "desc": "최고급 호텔의 서비스를 프라이빗하게 누릴 수 있는 강릉 최고의 럭셔리 독채 스테이."},
    {"id": "heritage", "name": "홍천 헤리티지", "desc": "세월의 깊이가 느껴지는 홍천의 프라이빗 한옥 풀빌라. 전통과 현대의 완벽한 조화."},
    {"id": "ramada", "name": "속초 라마다 프라이빗", "desc": "속초 바다의 파도 소리와 함께하는 미니멀리즘 럭셔리 스테이."},
    {"id": "surfyy", "name": "양양 서피 스테이", "desc": "양양의 자유로운 분위기와 모던한 인테리어가 돋보이는 프라이빗 공간."},
    {"id": "oceanview", "name": "동해 오션뷰 하우스", "desc": "끝없이 펼쳐진 동해 바다를 품은 가장 한국적이고 우아한 프라이빗 숙소."},
    {"id": "delpino", "name": "고성 델피노 풀빌라", "desc": "설악산과 동해바다를 동시에 조망하는 완벽한 럭셔리 미니멀리즘 공간."},
    {"id": "flora", "name": "평창 플로라 스테이", "desc": "평창의 고요한 자연 속에 숨겨진 트렌디한 인더스트리얼 감성 스테이."},
    {"id": "solsuite", "name": "삼척 쏠비치 스위트", "desc": "그리스 산토리니의 이국적인 감성을 프라이빗하게 누리는 하이엔드 리조트."}
]

for c in configs:
    folder = os.path.join(ADOPTER_DIR, c['id'])
    html_path = os.path.join(folder, 'index.html')
    
    if not os.path.exists(html_path):
        continue
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. MOHEOMDAM CLEANUP (For tpl-01 to tpl-04)
    html = re.sub(r'3개의 독립 객실', '완벽히 독립된 프라이빗 객실', html)
    html = re.sub(r'3개동', '단독 풀빌라', html)
    html = re.sub(r'제주의 숲과 돌담에 둘러싸여', '청정 자연에 둘러싸여', html)
    html = re.sub(r'제주 구좌 감성', '하이엔드 감성', html)
    html = re.sub(r'제주 구좌읍.*?독채 풀빌라', c['desc'], html)
    html = re.sub(r'제주.*?쉼에 집중하는', '오롯이 쉼에 집중하는', html)
    html = re.sub(r'완벽하게 분리된 3개의 독립 객실과', '완벽하게 프라이빗한 독채 객실과', html)
    
    # 2. ENGLISH TEMPLATE CLEANUP (For tpl-05 to tpl-10)
    # Wabi Sabi (tpl-05)
    html = re.sub(r'Wabi[- ]?Sabi', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'A tranquil escape blending minimalist wabi-sabi aesthetics.*?(?=")', c['desc'], html, flags=re.IGNORECASE)
    html = re.sub(r'Philosophy', '브랜드 철학', html, flags=re.IGNORECASE)
    html = re.sub(r'Sanctuaries', '객실 안내', html, flags=re.IGNORECASE)
    html = re.sub(r'Embracing the <br>\s*beauty of nature', '자연과 하나되는<br>완벽한 휴식', html, flags=re.IGNORECASE)
    html = re.sub(r'Rooted in the Japanese philosophy.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'Discover our sanctuaries', '객실 둘러보기', html, flags=re.IGNORECASE)
    html = re.sub(r'Finding beauty in imperfection.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'Jeju, South Korea', '강원특별자치도', html, flags=re.IGNORECASE)
    
    # Modern Glass (tpl-06)
    html = re.sub(r'Modern Glass', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'The Architecture of Light', '빛이 머무는 공간', html, flags=re.IGNORECASE)
    html = re.sub(r'Floor-to-ceiling glass.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Hanok Heritage (tpl-07)
    html = re.sub(r'Hanok Heritage', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'Timeless Korean Elegance', '전통의 우아함', html, flags=re.IGNORECASE)
    html = re.sub(r'Experience the profound serenity.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Coastal Breeze (tpl-08)
    html = re.sub(r'Coastal Breeze', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'Where the Ocean Meets Minimal Luxury', '바다와 맞닿은 공간', html, flags=re.IGNORECASE)
    html = re.sub(r'Let the sound of waves.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)

    # Industrial Chic (tpl-09)
    html = re.sub(r'Industrial Chic', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'Raw Textures, Refined Comfort', '거친 질감 속의 평온함', html, flags=re.IGNORECASE)
    html = re.sub(r'Concrete and steel.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Velaa Luxury (tpl-10)
    html = re.sub(r'Velaa Luxury', c['name'], html, flags=re.IGNORECASE)
    html = re.sub(r'The Pinnacle of Island Luxury', '하이엔드 럭셔리의 정점', html, flags=re.IGNORECASE)
    html = re.sub(r'Unparalleled service.*?</p>', f'{c["desc"]}</p>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Common English words across templates
    html = re.sub(r'All rights reserved.', 'All rights reserved.', html)
    html = re.sub(r'Privacy Policy', '개인정보처리방침', html)
    html = re.sub(r'Terms of Service', '이용약관', html)
    html = re.sub(r'>\s*Book Now\s*<', '>네이버 예약<', html, flags=re.IGNORECASE)
    html = re.sub(r'>\s*Contact\s*<', '>문의하기<', html, flags=re.IGNORECASE)
    
    # Specific English replacements for sections
    html = re.sub(r'Rooms & Spaces', '객실 안내', html, flags=re.IGNORECASE)
    html = re.sub(r'Amenities', '어메니티', html, flags=re.IGNORECASE)
    html = re.sub(r'Experience', '특별한 경험', html, flags=re.IGNORECASE)
    html = re.sub(r'Gallery', '갤러리', html, flags=re.IGNORECASE)
    html = re.sub(r'Explore Spaces', '객실 둘러보기', html, flags=re.IGNORECASE)
    html = re.sub(r'Reserve Your Stay', '실시간 예약', html, flags=re.IGNORECASE)
    html = re.sub(r'Starting from \/night', '1박 500,000원 부터', html, flags=re.IGNORECASE)

    # Room names (English to Korean fallback)
    html = re.sub(r'The Master Suite', f'{c["name"]} 스위트', html, flags=re.IGNORECASE)
    html = re.sub(r'The Ocean Villa', f'{c["name"]} 풀빌라', html, flags=re.IGNORECASE)
    html = re.sub(r'The Penthouse', f'{c["name"]} 펜트하우스', html, flags=re.IGNORECASE)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Purged Moheomdam and English from {c['id']}")

