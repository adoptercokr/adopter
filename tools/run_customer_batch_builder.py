import os
import sys
import json
import re
import shutil
import urllib.request
import urllib.parse
import time

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adopter
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates", "01-stay")
CUSTOMER_DIR = os.path.join(BASE_DIR, "Customer")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8'
}

def sanitize_text(text):
    """절대 규칙 준수: 독채 단어 금지"""
    if not text:
        return ""
    text = text.replace("독채펜션", "단독펜션")
    text = text.replace("독채 풀빌라", "단독 풀빌라")
    text = text.replace("독채", "단독주택")
    return text

def fetch_photos(pid):
    """네이버 플레이스에서 고화질 사진 최대 10장 URL 추출"""
    photo_urls = []
    
    # 1. home 페이지와 photo 페이지 모두 탐색
    for tab in ["home", "photo"]:
        url = f"https://m.place.naver.com/accommodation/{pid}/{tab}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                
                # src= 파라미터에서 원본 이미지 추출
                src_matches = re.findall(r'src=(https%3A%2F%2F[^\s"\'&]+)', html)
                for sm in src_matches:
                    unquoted = urllib.parse.unquote(sm)
                    if any(domain in unquoted for domain in ['ldb-phinf', 'naverbooking-phinf', 'pup-review-phinf', 'blogfiles']):
                        # 프로필 이미지, 아이콘 등 제외
                        if not any(ex in unquoted.lower() for ex in ['profile', 'icon', 'favicon', 'banner', 'logo']):
                            if unquoted not in photo_urls:
                                photo_urls.append(unquoted)
                                
                # 직링 추출
                direct_matches = re.findall(r'(https://ldb-phinf\.pstatic\.net/[^\s"\'<>]+)', html)
                for dm in direct_matches:
                    clean = dm.split('"')[0].split("'")[0]
                    if not any(ex in clean.lower() for ex in ['profile', 'icon', 'favicon', 'banner', 'logo']):
                        if clean not in photo_urls:
                            photo_urls.append(clean)
        except Exception as e:
            print(f"    사진 탐색 에러 ({tab}): {e}")
        time.sleep(0.3)
        if len(photo_urls) >= 12:
            break

    return photo_urls[:10]

def build_stay_site(stay_info):
    name = sanitize_text(stay_info['name'])
    code = stay_info['code']
    slug = code.split("-")[1]
    folder_name = f"{code}-{name.replace(' ', '')}"
    dest_dir = os.path.join(CUSTOMER_DIR, folder_name)
    img_dir = os.path.join(dest_dir, "img")
    
    os.makedirs(img_dir, exist_ok=True)
    print(f"\n==========================================")
    print(f"🚀 [{stay_info['name']}] 사이트 빌드 시작 -> {folder_name}")
    print(f"==========================================")
    
    # 1. 템플릿 파일 복사
    files_to_copy = ["index.html", "favicon.svg", ".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))
            
    # 2. 사진 다운로드
    photo_urls = fetch_photos(stay_info['pid'])
    print(f"  📷 추출된 고화질 사진: {len(photo_urls)}장")
    
    photo_meta = []
    cat_cycle = ["exterior", "living", "bedroom", "kitchen", "outdoor"]
    
    for i, p_url in enumerate(photo_urls, 1):
        target_file = os.path.join(img_dir, f"photo_{i}.jpg")
        try:
            req = urllib.request.Request(p_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                with open(target_file, "wb") as f_out:
                    f_out.write(resp.read())
            cat = cat_cycle[(i - 1) % len(cat_cycle)]
            photo_meta.append({
                "src": f"./img/photo_{i}.jpg",
                "cat": cat,
                "title": f"{name} {cat.capitalize()} 공간 {i}"
            })
            print(f"    다운로드 완료 [{i}/10]: photo_{i}.jpg")
        except Exception as e:
            print(f"    사진 다운로드 실패 ({i}): {e}")
            
    # 만약 사진이 부족할 경우 당근민박/기본 고화질 사진 보충
    if len(photo_meta) < 5:
        print("  ⚠️ 사진 보충 중...")
        sample_img_dir = os.path.join(BASE_DIR, "..", "당근민박", "img")
        if os.path.exists(sample_img_dir):
            for i in range(len(photo_meta) + 1, 11):
                sample_file = os.path.join(sample_img_dir, f"photo_{i}.jpg")
                if os.path.exists(sample_file):
                    shutil.copy2(sample_file, os.path.join(img_dir, f"photo_{i}.jpg"))
                    cat = cat_cycle[(i - 1) % len(cat_cycle)]
                    photo_meta.append({
                        "src": f"./img/photo_{i}.jpg",
                        "cat": cat,
                        "title": f"{name} {cat.capitalize()} 공간 {i}"
                    })
                    
    # 3. stay_config.js 생성
    price_val = int(stay_info.get('price', 300000))
    config_content = f"""/**
 * {name} 공식 웹사이트 설정 데이터
 * Auto-generated by Adopter Nightly Producer
 */

const STAY_CONFIG = {{
  // 1. 브랜드 및 숙소 기본 정보
  brandName: "{name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "머묾, 그 자체가 온전한 쉼이 되는 곳",
  description: "{name}에서 전하는 온전하고 프라이빗한 쉼. 제주의 자연과 돌담이 어우러진 아름다운 공간.",
  
  // 2. 호스트 및 연락처 정보
  owner: "호스트",
  businessNo: "",
  address: "{stay_info.get('address', '제주특별자치도')}",
  phone: "{stay_info.get('phone', '0507-0000-0000')}",
  email: "contact@adopter.co.kr",
  domain: "{slug}.adopter.co.kr",
  
  // 3. 외부 연동 링크
  kakaoChatUrl: "http://pf.kakao.com/_HCTxiX/chat",
  naverMapUrl: "{stay_info.get('naverLink', '')}",
  instagramUrl: "{stay_info.get('instagram', '')}",
  
  // 4. 고화질 영상 배경
  youtubeIntroId: "f09Xfn1fHm8",
  youtubeTourId: "JG92-0fSScQ",
  
  // 5. 숙박 요금 및 연박 할인 정책
  pricing: {{
    weekday: {price_val},
    weekend: {price_val + 30000},
    peakSurcharge: 30000,
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

  // 6. 3대 무료 혜택
  freeBenefits: [
    {{ title: "프라이빗 정원 & 테라스", subtitle: "Garden", desc: "단독 정원 및 야외 휴식 공간 완비" }},
    {{ title: "사계절 전용 바베큐", subtitle: "BBQ", desc: "독립 다이닝 공간 및 그릴 무료 완비" }},
    {{ title: "안락한 쉼과 온수", subtitle: "Relax", desc: "편안한 프리미엄 침구 및 쾌적한 전용 시설" }}
  ],

  // 7. 공간 구성 안내
  spaces: {{
    landSize: "120평 대지",
    buildingSize: "35평 단독주택",
    floor1: "거실, 풀옵션 주방, 마스터룸, 온돌룸, 욕실, 파우더룸",
    outdoor: "프라이빗 정원, 야외 테라스, 개별 바베큐장, 전용 주차공간"
  }},

  // 8. 포토 갤러리 메타데이터
  photos: {json.dumps(photo_meta, ensure_ascii=False, indent=4)},

  // 9. 관리자 비밀번호
  adminPassword: "1316"
}};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = STAY_CONFIG;
}}
"""
    with open(os.path.join(dest_dir, "stay_config.js"), "w", encoding="utf-8") as f_cfg:
        f_cfg.write(config_content)
        
    print(f"  ✨ {name} 빌드 완료! ({dest_dir})")
    return True

def main():
    os.makedirs(CUSTOMER_DIR, exist_ok=True)
    
    # payload에서 10곳 정보 로드
    payload_file = os.path.join(BASE_DIR, "tools", "new_10_rows_payload.json")
    with open(payload_file, "r", encoding="utf-8") as f:
        rows = json.load(f)
        
    print(f"총 {len(rows)}개 타겟 숙소 빌드 파이프라인 가동...")
    
    built_count = 0
    for r in rows:
        # r[1]: naverLink, r[3]: name, r[4]: code, r[8]: phone, r[9]: addr, r[10]: price, r[11]: instagram
        pid_m = re.search(r'accommodation/(\d+)', r[1])
        pid = pid_m.group(1) if pid_m else "0"
        
        stay_info = {
            "pid": pid,
            "name": r[3],
            "code": r[4],
            "naverLink": r[1],
            "phone": r[8],
            "address": r[9],
            "price": r[10],
            "instagram": r[11]
        }
        
        success = build_stay_site(stay_info)
        if success:
            built_count += 1
            
    print(f"\n🎉 10개 전 고객사 맞춤형 사이트 빌드 완료! (성공: {built_count}/10)")

if __name__ == "__main__":
    main()
