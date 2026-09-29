import sys
import os
import re
import json
import urllib.request
import urllib.parse

def extract_place_id(url):
    m = re.search(r'/accommodation/(\d+)', url)
    if m:
        return m.group(1)
    m = re.search(r'/place/(\d+)', url)
    if m:
        return m.group(1)
    return None

def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=12) as resp:
        return resp.read().decode('utf-8')

def parse_apollo_state(html):
    idx = html.find('window.__APOLLO_STATE__')
    if idx == -1:
        return {}
    start_brace = html.find('{', idx)
    depth = 0
    end_brace = -1
    in_string = False
    escape = False
    
    for i in range(start_brace, len(html)):
        c = html[i]
        if in_string:
            if escape:
                escape = False
            elif c == '\\':
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    end_brace = i
                    break
    if end_brace != -1:
        return json.loads(html[start_brace:end_brace+1])
    return {}

def crawl_stay(place_url, target_folder_name=None):
    place_id = extract_place_id(place_url)
    if not place_id:
        print(f"Error: Invalid place URL {place_url}")
        return None

    print(f"=== [1/4] 네이버 플레이스 데이터 크롤링 시작 (ID: {place_id}) ===")
    home_url = f"https://m.place.naver.com/accommodation/{place_id}/home"
    photo_url = f"https://m.place.naver.com/accommodation/{place_id}/photo?filterType=%EC%97%85%EC%B2%B4"
    
    home_html = fetch_html(home_url)
    home_state = parse_apollo_state(home_html)
    
    # 1. 기본 정보 추출
    stay_info = {
        "placeId": place_id,
        "name": "감성 숙소",
        "address": "제주특별자치도",
        "phone": "",
        "category": "펜션",
        "description": "",
        "images": [],
        "instagram": "",
        "blog": ""
    }
    
    for k, v in home_state.items():
        if isinstance(v, dict):
            if v.get('roadAddress') and v.get('name'):
                stay_info["name"] = v.get('name')
                stay_info["address"] = v.get('roadAddress')
                stay_info["phone"] = v.get('virtualPhone') or v.get('phone') or ""
                stay_info["category"] = v.get('category') or "단독 풀빌라"
            if 'desc' in v and v.get('desc'):
                stay_info["description"] = v.get('desc')
                
    # SNS 링크 추출
    for k, v in home_state.items():
        if isinstance(v, dict) and 'url' in v:
            u = str(v.get('url'))
            if 'instagram.com' in u:
                stay_info["instagram"] = u
            elif 'blog.naver.com' in u:
                stay_info["blog"] = u

    # 2. 사진 추출
    try:
        photo_html = fetch_html(photo_url)
        photo_state = parse_apollo_state(photo_html)
    except Exception as e:
        photo_state = {}

    merged_state = {**home_state, **photo_state}
    photo_urls = []
    
    for k, v in merged_state.items():
        if isinstance(v, dict):
            # Photo Viewer Items
            orig = v.get('originalUrl') or v.get('url')
            if orig and ('pstatic.net' in orig or 'ldb-phinf' in orig) and orig not in photo_urls:
                if not any(x in orig for x in ['icon_', 'emoji', 'profile']):
                    photo_urls.append(orig)

    stay_info["images"] = photo_urls[:20] # 최대 20장
    print(f"-> 추출된 숙소명: {stay_info['name']}")
    print(f"-> 주소: {stay_info['address']}")
    print(f"-> 연락처: {stay_info['phone']}")
    print(f"-> 고화질 사진 개수: {len(stay_info['images'])}장")

    # 3. 폴더 생성 및 템플릿 복제
    if not target_folder_name:
        # '독채', '네이버페이' 등 불필요 키워드 정돈
        clean_name = re.sub(r'네이버페이|독채|펜션|감성숙소|제주도|제주', '', stay_info['name']).strip()
        target_folder_name = clean_name if clean_name else f"stay_{place_id}"

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    studio_dir = os.path.dirname(base_dir)
    target_dir = os.path.join(studio_dir, target_folder_name)
    template_dir = os.path.join(base_dir, "templates", "01-stay")

    print(f"=== [2/4] 프로젝트 폴더 생성 및 템플릿 복제: {target_dir} ===")
    os.makedirs(os.path.join(target_dir, "img"), exist_ok=True)

    # 템플릿 파일 복사
    for fn in ["index.html", "favicon.svg", "robots.txt", "sitemap.xml", ".gitignore"]:
        src = os.path.join(template_dir, fn)
        dst = os.path.join(target_dir, fn)
        if os.path.exists(src):
            with open(src, "rb") as sf, open(dst, "wb") as df:
                df.write(sf.read())

    # 4. 사진 다운로드
    print(f"=== [3/4] 고화질 사진 로컬 다운로드 ===")
    local_photo_entries = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for i, p_url in enumerate(stay_info["images"]):
        fname = f"photo_{i+1}.jpg"
        fpath = os.path.join(target_dir, "img", fname)
        try:
            req = urllib.request.Request(p_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r, open(fpath, "wb") as f:
                f.write(r.read())
            
            cat = "exterior" if i < 3 else ("living" if i < 7 else ("bedroom" if i < 11 else "pool-jacuzzi"))
            local_photo_entries.append({
                "src": f"./img/{fname}",
                "cat": cat,
                "title": f"{stay_info['name']} 공간 {i+1}"
            })
            print(f"   [V] {fname} 다운로드 완료")
        except Exception as e:
            print(f"   [X] 사진 다운로드 실패 ({fname}): {e}")

    # 5. stay_config.js 생성
    print(f"=== [4/4] stay_config.js 자동 바인딩 ===")
    
    # 법적 금지어 치환 검수 (독채 -> 단독주택)
    safe_name = stay_info['name'].replace("독채", "단독")
    safe_desc = (stay_info['description'] or f"{safe_name}에서 전하는 온전하고 프라이빗한 쉼").replace("독채", "단독주택")
    subdomain = re.sub(r'[^a-zA-Z0-9]', '', target_folder_name.lower())
    if not subdomain:
        subdomain = f"stay{place_id}"

    config_content = f"""/**
 * {safe_name} 자동 생성 설정 데이터
 * Auto-generated by Adopter Naver Crawler
 */

const STAY_CONFIG = {{
  brandName: "{safe_name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "머묾, 그 자체가 온전한 쉼이 되는 곳",
  description: "{safe_desc}",
  
  owner: "호스트",
  businessNo: "",
  address: "{stay_info['address']}",
  phone: "{stay_info['phone']}",
  email: "contact@adopter.co.kr",
  domain: "{subdomain}.adopter.co.kr",
  
  kakaoChatUrl: "http://pf.kakao.com/_HCTxiX/chat",
  naverMapUrl: "{place_url}",
  
  youtubeIntroId: "f09Xfn1fHm8",
  youtubeTourId: "JG92-0fSScQ",
  
  pricing: {{
    weekday: 250000,
    weekend: 280000,
    peakSurcharge: 20000,
    baseGuests: 4,
    maxGuests: 8,
    extraGuestFee: 10000,
    minNights: 2,
    discounts: {{
      days7: 10,
      days14: 15,
      days28: 20
    }},
    depositLessThan7: 200000,
    depositMoreThan7: 300000,
    depositMoreThan28: 500000
  }},

  freeBenefits: [
    {{ title: "프라이빗 정원 & 테라스", subtitle: "Garden", desc: "단독 정원 및 야외 휴식 공간 완비" }},
    {{ title: "바베큐 시설 제공", subtitle: "BBQ", desc: "사계절 전용 다이닝 그릴 완비" }},
    {{ title: "안락한 쉼과 온수", subtitle: "Relax", desc: "편안한 침구 및 쾌적한 전용 시설" }}
  ],

  photos: {json.dumps(local_photo_entries, ensure_ascii=False, indent=4)},
  adminPassword: "1316"
}};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = STAY_CONFIG;
}}
"""
    config_path = os.path.join(target_dir, "stay_config.js")
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)
    print(f"-> {config_path} 생성 완료!")
    
    result = {
        "name": safe_name,
        "folder": target_folder_name,
        "subdomain": f"{subdomain}.adopter.co.kr",
        "phone": stay_info['phone'],
        "address": stay_info['address'],
        "photoCount": len(local_photo_entries),
        "targetDir": target_dir
    }
    return result

if __name__ == "__main__":
    test_url = sys.argv[1] if len(sys.argv) > 1 else "https://m.place.naver.com/accommodation/1226740854/home"
    target_name = sys.argv[2] if len(sys.argv) > 2 else "당근민박"
    res = crawl_stay(test_url, target_name)
    print("\n=== 최종 결과 ===")
    print(json.dumps(res, ensure_ascii=False, indent=2))
