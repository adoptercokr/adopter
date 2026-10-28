import os
import json
import shutil
import re

# Load collected data
with open('tools/gangwon_10_collected.json', 'r', encoding='utf-8') as f:
    collected_list = json.load(f)

# Metadata mapping for the 10 real Gangwon stays
META = {
    "gw-namubat": {
        "slug": "namubat",
        "name": "홍천 나무밭",
        "sub": "숲속의 고요한 독채 노천탕 스테이",
        "desc": "강원도 홍천의 맑은 숲속에 둘러싸인 프라이빗 독채 숙소입니다. 사계절 야외 노천탕과 따스한 불멍, 온전한 쉼을 위한 완벽한 독립 공간을 제공합니다.",
        "addr": "강원특별자치도 홍천군 영귀미면 궁터길 14",
        "phone": "0507-1335-9876",
        "price": 380000,
        "variant": 1,
        "facilities": ["야외노천탕", "단독바베큐", "불멍존", "독채전용정원", "와이파이", "호텔식침구"]
    },
    "gw-caminode": {
        "slug": "caminode",
        "name": "까미노데플로레스타",
        "sub": "홍천강을 품은 하이엔드 부티크 풀빌라",
        "desc": "숲으로 가는 길이라는 의미를 담은 부티크 풀빌라입니다. 홍천강의 수려한 자연을 바라보며 프라이빗 온수풀과 이국적인 휴식을 만끽할 수 있습니다.",
        "addr": "강원특별자치도 홍천군 북방면 도사곡길 201",
        "phone": "0507-1484-0534",
        "price": 450000,
        "variant": 2,
        "facilities": ["프라이빗온수풀", "홍천강전망", "개별테라스", "독립스파", "와이파이", "디자인가구"]
    },
    "gw-narobuteo": {
        "slug": "narobuteo",
        "name": "강릉 나로부터 풀빌라",
        "sub": "발리의 이국적인 감성을 담은 독채 온수풀빌라",
        "desc": "강릉 사천의 평온한 풍경 속 이국적인 감성을 자아내는 프라이빗 풀빌라입니다. 야외 온수풀과 대형 빔프로젝터로 특별한 낭만을 선물합니다.",
        "addr": "강원특별자치도 강릉시 사천면 방동길 302",
        "phone": "0507-1433-3558",
        "price": 420000,
        "variant": 3,
        "facilities": ["사계절온수풀", "야외빔프로젝터", "발리풍인테리어", "개별바베큐", "와이파이", "어메니티"]
    },
    "gw-secretgarden": {
        "slug": "secretgarden",
        "name": "강릉 비밀의정원 풀빌라",
        "sub": "사천해변 인근 프라이빗 가든 럭셔리 스테이",
        "desc": "사계절 따뜻한 개별 온수풀과 초록빛 정원이 어우러진 강릉의 감성 독채 풀빌라입니다. 사랑하는 사람들과 오붓하고 소중한 시간을 보낼 수 있습니다.",
        "addr": "강원특별자치도 강릉시 사천면 해안로 1064",
        "phone": "0507-1329-8733",
        "price": 390000,
        "variant": 4,
        "facilities": ["실내개별온수풀", "사천해변인접", "가든정원", "단독바베큐", "와이파이", "스마트TV"]
    },
    "gw-privateyangyang": {
        "slug": "privateyangyang",
        "name": "프라이빗양양 독채 풀빌라",
        "sub": "오산해수욕장 프라이빗 힐링 독채 스테이",
        "desc": "양양의 푸른 바다와 자연을 오롯이 누릴 수 있는 단독 독채 풀빌라입니다. 넓은 수영장과 정갈한 인테리어로 온전한 프라이버시를 보장합니다.",
        "addr": "강원특별자치도 양양군 손양면 선사유적로 260",
        "phone": "0507-1384-5993",
        "price": 480000,
        "variant": 1,
        "facilities": ["단독전용수영장", "오산해변도보", "프라이빗마당", "개별바베큐", "와이파이", "주차완비"]
    },
    "gw-lahenne": {
        "slug": "lahenne",
        "name": "고성 라헨느풀빌라",
        "sub": "동해안 파노라마 오션뷰와 제트스파",
        "desc": "가진해변 바다 바로 앞에 위치하여 객실 어디서나 푸른 동해바다와 일출을 감상할 수 있는 감성 풀빌라입니다. 제트스파와 개별 풀이 준비되어 있습니다.",
        "addr": "강원특별자치도 고성군 죽왕면 가진해변길 217",
        "phone": "0507-1436-1683",
        "price": 350000,
        "variant": 2,
        "facilities": ["파노라마오션뷰", "제트스파", "사계절온수풀", "일출명소", "와이파이", "카페테리아"]
    },
    "gw-uirim": {
        "slug": "uirim",
        "name": "춘천 의림여관",
        "sub": "자연의 소리에 귀 기울이는 사색의 숲속 독채",
        "desc": "춘천 신동면 깊은 숲속, 단 두 채의 객실로만 운영되는 프라이빗 힐링 스테이입니다. 원목의 따스함과 큰 창 너머의 푸르름 속에서 진정한 쉼을 마주합니다.",
        "addr": "강원특별자치도 춘천시 신동면 풍류길 46",
        "phone": "0507-1324-5197",
        "price": 320000,
        "variant": 3,
        "facilities": ["사색의원목인테리어", "숲속뷰파노라마", "프라이빗다실", "오디오청음존", "와이파이", "친환경어메니티"]
    },
    "gw-bebridge": {
        "slug": "bebridge",
        "name": "영월 비브릿지 풀빌라",
        "sub": "영월 계곡의 절경을 담은 럭셔리 리조트 스테이",
        "desc": "청정 영월의 계곡과 기암괴석을 마주하는 하이엔드 독채 풀빌라입니다. 넓은 테라스와 개별 온수 수영장에서 계곡의 물소리와 함께 힐링하세요.",
        "addr": "강원특별자치도 영월군 김삿갓면 영월동로 1121",
        "phone": "0507-1392-6555",
        "price": 460000,
        "variant": 4,
        "facilities": ["계곡전망온수풀", "대형프라이빗테라스", "개별바베큐", "호텔식서비스", "와이파이", "카페"]
    },
    "gw-urpoolvilla": {
        "slug": "urpoolvilla",
        "name": "원주 유알 풀빌라",
        "sub": "건축 미학과 자연이 공존하는 프리미엄 풀빌라",
        "desc": "노출 콘크리트의 유려한 조형미와 모던한 디자인이 돋보이는 원주의 하이엔드 스테이입니다. 넓은 개별 풀과 프라이빗 라운지에서 특별한 여유를 즐기세요.",
        "addr": "강원특별자치도 원주시 지정면 지정로 912",
        "phone": "0507-1390-2972",
        "price": 500000,
        "variant": 1,
        "facilities": ["건축디자인스테이", "독립프라이빗풀", "라운지테라스", "고급음향시스템", "와이파이", "개별주차"]
    },
    "gw-migallu": {
        "slug": "migallu",
        "name": "삼척 미갈루 풀빌라",
        "sub": "동해 바다의 푸른 숨결을 마주하는 독채 풀빌라",
        "desc": "삼척의 청정한 바다를 한눈에 담는 오션뷰 프라이빗 풀빌라입니다. 사계절 개별 온수풀과 스파, 그리고 모던한 휴양 인테리어를 자랑합니다.",
        "addr": "강원특별자치도 삼척시 근덕면 삼척로 2132",
        "phone": "070-4376-6476",
        "price": 410000,
        "variant": 2,
        "facilities": ["오션뷰온수풀", "프라이빗스파", "동해바다전망", "개별바베큐", "와이파이", "호텔식어메니티"]
    }
}

# Template source
MASTER_HTML = 'Customer/260930-sanur/index.html'
with open(MASTER_HTML, 'r', encoding='utf-8') as f:
    master_html_content = f.read()

# Generate stay_config.js and index.html for each stay
deployed_stays = []

for item in collected_list:
    key = item['key']
    meta = META.get(key)
    if not meta:
        continue

    slug = meta['slug']
    name = meta['name']
    naver_link = item['naver_link']
    
    # Filter high quality real photos
    photos = [p for p in item.get('photos', []) if not any(b in p for b in ['profile', 'icon', 'blogpfthumb', 'f84_sharpen'])][:12]
    
    # Format spaces array
    spaces_json = []
    for idx, p in enumerate(photos):
        spaces_json.append(f'    {{ id: "s{idx+1}", mainImage: "{p}" }}')
    spaces_str = ",\n".join(spaces_json)

    # Format facilities array
    facilities_json = []
    for fac in meta['facilities']:
        facilities_json.append(f'    {{ name: "{fac}", icon: "wifi" }}')
    fac_str = ",\n".join(facilities_json)

    # Generate clean, non-emoji, modern stay_config.js
    stay_config_content = f"""const STAY_CONFIG = {{
  variant: {meta['variant']},
  naverLink: "{naver_link}",
  phone: "{meta['phone']}",
  name: "{name}",
  subtitle: "{meta['sub']}",
  description: "{meta['desc']}",
  address: "{meta['addr']}",
  benefits: [
    {{ id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" }},
    {{ id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }}
  ],
  spaces: [
{spaces_str}
  ],
  facilities: [
{fac_str}
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {{
    weekday: "{meta['price']:,}",
    weekend: "{int(meta['price']*1.2):,}",
    peak: "{int(meta['price']*1.35):,}"
  }}
}};
"""

    # Targets: Customer folder AND root folder for direct access
    targets = [
        f"Customer/gw-{slug}",
        slug
    ]

    for target_dir in targets:
        os.makedirs(target_dir, exist_ok=True)
        # Write stay_config.js
        with open(os.path.join(target_dir, 'stay_config.js'), 'w', encoding='utf-8') as f:
            f.write(stay_config_content)
        # Write index.html
        with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(master_html_content)

    deployed_stays.append({
        "key": key,
        "slug": slug,
        "name": name,
        "addr": meta['addr'],
        "phone": meta['phone'],
        "price": meta['price'],
        "naver_link": naver_link,
        "deploy_url": f"https://adopter.co.kr/{slug}/",
        "photos_count": len(photos)
    })
    print(f"[+] 생성 완료: {name} -> /{slug}/ (실사진 {len(photos)}장)")

with open('tools/gangwon_10_deployed.json', 'w', encoding='utf-8') as f:
    json.dump(deployed_stays, f, ensure_ascii=False, indent=2)

print("\n[SUCCESS] 강원도 10곳 실제 숙소 사이트 생성 완료!")
