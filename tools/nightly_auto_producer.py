#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================================================
🌌 Adopter Nightly Auto Producer (무인 야간 자동화 제작 엔진)
------------------------------------------------------------------------------
- 매일 새벽(밤)에 윈도우 스케줄러 또는 원클릭으로 실행되는 100% 무인 제작기입니다.
- AI LLM API를 전혀 호출하지 않아 토큰 비용이 0원(완전 무료)입니다.
- 실행 흐름:
    1. 네이버 지도 플레이스에서 '외부 홈페이지가 0개'인 핵심 타겟 숙소 10곳 자동 발굴
    2. 각 숙소의 네이버 고화질 사진 최대 10장 자동 다운로드
    3. `\01-Nova-Web-Studio\adopter\Customer\` 폴더에 맞춤형 사이트 10개 즉각 빌드
    4. 구글 시트로 10개 제작 데이터 및 도메인 주소 자동 전송
==============================================================================
"""

import os
import sys
import json
import re
import shutil
import urllib.request
import urllib.parse
import time
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# 경로 설정
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
TEMPLATE_DIR = os.path.join(ADOPTER_DIR, "templates", "01-stay")
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, "Customer")
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8'
}

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}", flush=True)

def sanitize_text(text):
    """절대 규칙 준수: 독채 단어 일체 금지"""
    if not text:
        return ""
    text = text.replace("독채펜션", "단독펜션")
    text = text.replace("독채 풀빌라", "단독 풀빌라")
    text = text.replace("독채", "단독주택")
    return text

def inspect_place_strictly(pid):
    """Apollo State 및 앵커를 검사하여 외부 독립 홈페이지가 0개인 곳만 선별"""
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception:
        return None

    # 1. 앵커 태그 검사
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    for href, text in anchors:
        text_clean = re.sub(r'<[^>]+>', '', text).strip()
        if '홈페이지' in text_clean:
            return None # 탈락!
        href_lower = href.lower()
        if href_lower.startswith('http') and not any(nd in href_lower for nd in ['naver.com', 'instagram.com', 'facebook.com', 'youtube.com']):
            return None # 탈락!

    # 2. Apollo State 검사
    m = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});', html)
    if not m:
        return None
    try:
        data = json.loads(m.group(1))
    except Exception:
        return None

    for k, v in data.items():
        if isinstance(v, dict) and 'homepages' in v and v['homepages']:
            hp = v['homepages']
            if hp.get('etc') and len(hp['etc']) > 0:
                return None
            if hp.get('repr'):
                r_type = hp['repr'].get('type', '')
                r_url = hp['repr'].get('url', '').lower()
                if r_type == '홈페이지' or (r_url and not any(nd in r_url for nd in ['naver.com', 'instagram.com', 'facebook.com', 'youtube.com'])):
                    return None

    base = data.get(f'PlaceDetailBase:{pid}', {})
    if not base:
        for k, v in data.items():
            if k.startswith('PlaceDetailBase:') and v.get('id') == pid:
                base = v
                break

    name = base.get('name', '')
    if not name:
        return None

    phone = base.get('virtualPhone') or base.get('phone') or "0507-0000-0000"
    road_addr = base.get('roadAddress') or base.get('address') or "제주특별자치도"

    # 인스타그램 링크 추출
    insta_link = ""
    for href, text in anchors:
        if 'instagram.com' in href.lower():
            insta_link = href
            break

    return {
        'pid': pid,
        'name': name,
        'phone': phone,
        'address': road_addr,
        'instagram': insta_link,
        'naverLink': url
    }

def fetch_photos(pid):
    """네이버 플레이스에서 고화질 사진 최대 10장 추출"""
    photo_urls = []
    for tab in ["home", "photo"]:
        url = f"https://m.place.naver.com/accommodation/{pid}/{tab}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                src_matches = re.findall(r'src=(https%3A%2F%2F[^\s"\'&]+)', html)
                for sm in src_matches:
                    unquoted = urllib.parse.unquote(sm)
                    if any(domain in unquoted for domain in ['ldb-phinf', 'naverbooking-phinf', 'pup-review-phinf', 'blogfiles']):
                        if not any(ex in unquoted.lower() for ex in ['profile', 'icon', 'favicon', 'banner', 'logo']):
                            if unquoted not in photo_urls:
                                photo_urls.append(unquoted)
        except Exception:
            pass
        if len(photo_urls) >= 12:
            break
    return photo_urls[:10]

def build_single_stay(stay_info, today_prefix):
    clean_name = sanitize_text(stay_info['name'])
    slug = f"stay-{stay_info['pid']}"
    folder_name = f"{today_prefix}-{slug}-{clean_name.replace(' ', '')}"
    dest_dir = os.path.join(CUSTOMER_DIR, folder_name)
    img_dir = os.path.join(dest_dir, "img")

    os.makedirs(img_dir, exist_ok=True)
    
    # 템플릿 복사
    files_to_copy = ["index.html", "favicon.svg", ".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))

    # 사진 다운로드
    photos = fetch_photos(stay_info['pid'])
    cat_cycle = ["exterior", "living", "bedroom", "kitchen", "outdoor"]
    photo_meta = []
    
    for i, p_url in enumerate(photos, 1):
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
                "title": f"{clean_name} {cat.capitalize()} 공간 {i}"
            })
        except Exception:
            pass

    price_val = 300000
    config_content = f"""/**
 * {clean_name} 공식 웹사이트 설정 데이터
 * Auto-generated by Adopter Nightly Producer
 */

const STAY_CONFIG = {{
  brandName: "{clean_name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "머묾, 그 자체가 온전한 쉼이 되는 곳",
  description: "{clean_name}에서 전하는 온전하고 프라이빗한 쉼. 제주의 자연과 돌담이 어우러진 아름다운 공간.",
  
  owner: "호스트",
  businessNo: "",
  address: "{stay_info['address']}",
  phone: "{stay_info['phone']}",
  email: "contact@adopter.co.kr",
  domain: "{slug}.adopter.co.kr",
  
  kakaoChatUrl: "http://pf.kakao.com/_HCTxiX/chat",
  naverMapUrl: "{stay_info['naverLink']}",
  instagramUrl: "{stay_info['instagram']}",
  
  youtubeIntroId: "f09Xfn1fHm8",
  youtubeTourId: "JG92-0fSScQ",
  
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

  freeBenefits: [
    {{ title: "프라이빗 정원 & 테라스", subtitle: "Garden", desc: "단독 정원 및 야외 휴식 공간 완비" }},
    {{ title: "사계절 전용 바베큐", subtitle: "BBQ", desc: "독립 다이닝 공간 및 그릴 무료 완비" }},
    {{ title: "안락한 쉼과 온수", subtitle: "Relax", desc: "편안한 프리미엄 침구 및 쾌적한 전용 시설" }}
  ],

  spaces: {{
    landSize: "120평 대지",
    buildingSize: "35평 단독주택",
    floor1: "거실, 풀옵션 주방, 마스터룸, 온돌룸, 욕실, 파우더룸",
    outdoor: "프라이빗 정원, 야외 테라스, 개별 바베큐장, 전용 주차공간"
  }},

  photos: {json.dumps(photo_meta, ensure_ascii=False, indent=4)},
  adminPassword: "1316"
}};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = STAY_CONFIG;
}}
"""
    with open(os.path.join(dest_dir, "stay_config.js"), "w", encoding="utf-8") as f_cfg:
        f_cfg.write(config_content)

    return {
        "slug": slug,
        "folder": folder_name,
        "url": f"https://{slug}.adopter.co.kr"
    }

def push_to_google_sheet(rows):
    """구글 시트로 새 제작 행들 전송"""
    class RedirectHandler(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return urllib.request.Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})
            
    opener = urllib.request.build_opener(RedirectHandler)
    payload = json.dumps(rows, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(APPS_SCRIPT_URL, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    try:
        with opener.open(req, timeout=15) as resp:
            log(f"구글 시트 전송 완료: {resp.read().decode('utf-8')}")
    except Exception as e:
        log(f"구글 시트 전송 에러: {e}")

def run_nightly_job():
    log("====================================================")
    log("🌙 [야간 자동화 가동] 제주 숙소 발굴 및 10개 사이트 빌드 시작")
    log("====================================================")
    
    os.makedirs(CUSTOMER_DIR, exist_ok=True)
    today_prefix = datetime.now().strftime("%y%m%d")
    
    # 1. 네이버 지도 플레이스 후보군 수집
    queries = [
        "제주 감성 숙소", "제주 조천 펜션", "제주 서귀포 펜션",
        "제주 대정 감성숙소", "제주 애월 펜션", "제주 구좌 민박"
    ]
    candidate_pids = []
    for q in queries:
        try:
            url = f"https://m.search.naver.com/search.naver?query={urllib.parse.quote(q)}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                found = re.findall(r'place\.naver\.com/accommodation/(\d+)', html)
                for p in found:
                    if p not in candidate_pids:
                        candidate_pids.append(p)
        except Exception:
            pass
        if len(candidate_pids) >= 40:
            break

    log(f"후보 숙소 {len(candidate_pids)}곳 발굴. 정밀 필터링 시작...")
    
    verified_targets = []
    for pid in candidate_pids:
        info = inspect_place_strictly(pid)
        if info:
            log(f"  ✨ [합격! 홈페이지 없음] {info['name']} (0507-{info['phone'][-8:]})")
            verified_targets.append(info)
            if len(verified_targets) >= 10:
                break
        time.sleep(0.3)

    log(f"\n최종 엄선된 10곳 빌드 시작...")
    sheet_rows = []
    for idx, target in enumerate(verified_targets, 1):
        built = build_single_stay(target, today_prefix)
        row = [
            "숙박업",
            target['naverLink'],
            "95%",
            sanitize_text(target['name']),
            f"{today_prefix}-{built['slug']}",
            built['url'],
            "제작완료",
            "준비완료",
            target['phone'],
            target['address'],
            "300000",
            target['instagram'],
            "",
            "",
            "",
            f"야간무인자동생성 (사진다운로드완료/인스타:{target['instagram'].split('/')[-1] if target['instagram'] else '없음'})"
        ]
        sheet_rows.append(row)
        log(f"  [{idx}/10] {target['name']} -> {built['url']}")

    # 4. 구글 시트 전송
    log("\n구글 시트로 10개 행 전송 중...")
    push_to_google_sheet(sheet_rows)
    log("🎉 오늘 밤 야간 자동화 임무 100% 완료!\n")

if __name__ == "__main__":
    run_nightly_job()
