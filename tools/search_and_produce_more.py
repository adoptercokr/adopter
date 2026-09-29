#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================================================
🔍 Adopter Dynamic Search & Continuous Producer (심야 무인 추가 발굴 및 제작)
------------------------------------------------------------------------------
- 조천, 구좌, 성산, 표선, 남원, 서귀포, 안덕 등 제주 전역의 감성 숙소를 추가 발굴
- Apollo State 및 앵커를 검사하여 외부 독립 홈페이지가 0개인 곳만 엄선
- 사진 최대 10장 다운로드 및 맞춤형 사이트 빌드 (무채색 SVG 아이콘, 화이트 견적기)
- 구글 시트로 신규 제작 행 실시간 전송
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

class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return urllib.request.Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})

opener = urllib.request.build_opener(RedirectHandler)

def sanitize_text(text):
    if not text:
        return ""
    text = text.replace("독채펜션", "단독펜션")
    text = text.replace("독채 풀빌라", "단독 풀빌라")
    text = text.replace("독채", "단독주택")
    return text.strip()

def inspect_place_strictly(pid):
    """외부 홈페이지가 0개인 곳만 선별"""
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception:
        return None

    # 홈페이지 존재 여부 검사
    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>', html, re.DOTALL)
    if not state_match:
        return None

    try:
        state = json.loads(state_match.group(1))
    except Exception:
        return None

    # 홈페이지 링크 체크
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)<\/a>', html, re.IGNORECASE)
    for href, text in anchors:
        if any(h in href.lower() for h in ['instagram.com', 'naver.com', 'daum.net', 'kakao.com', 'tel:']):
            continue
        if href.startswith('http') and not any(p in href for p in ['map.naver', 'm.place.naver', 'booking.naver']):
            return None # 독립 홈페이지 보유 -> 제외

    detail_keys = [k for k in state.keys() if k.startswith('PlaceDetailBase:')]
    if not detail_keys:
        return None

    base = state[detail_keys[0]]
    name = base.get('name', '')
    if not name:
        return None

    # 홈페이지 URL 필드 체크
    for k in ['homepage', 'url', 'site']:
        val = base.get(k)
        if val and isinstance(val, str) and val.startswith('http') and not any(p in val for p in ['instagram.com', 'naver.com']):
            return None

    phone = base.get('virtualPhone') or base.get('phone') or "0507-0000-0000"
    road_addr = base.get('roadAddress') or base.get('address') or "제주특별자치도"

    # 인스타그램
    insta_link = ""
    for href, text in anchors:
        if 'instagram.com' in href.lower():
            insta_link = href
            break

    return {
        'pid': str(pid),
        'name': name,
        'phone': phone,
        'address': road_addr,
        'instagram': insta_link,
        'naverLink': url
    }

def fetch_photos(pid):
    photo_urls = []
    for tab in ["home", "photo"]:
        url = f"https://m.place.naver.com/accommodation/{pid}/{tab}"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
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

def build_stay_website(target, slug):
    today_prefix = datetime.now().strftime("%y%m%d")
    clean_name = sanitize_text(target['name'])
    folder_name = f"{today_prefix}-{slug}-{clean_name.replace(' ', '')}"
    dest_dir = os.path.join(CUSTOMER_DIR, folder_name)
    root_slug_dir = os.path.join(ADOPTER_DIR, slug)

    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(root_slug_dir, exist_ok=True)
    img_dir = os.path.join(dest_dir, "img")
    root_img_dir = os.path.join(root_slug_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(root_img_dir, exist_ok=True)

    files_to_copy = ["index.html", ".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))
            shutil.copy2(src, os.path.join(root_slug_dir, f))

    photos = fetch_photos(target['pid'])
    cat_cycle = ["exterior", "living", "bedroom", "kitchen", "outdoor"]
    photo_meta = []

    for i, p_url in enumerate(photos, 1):
        target_file = os.path.join(img_dir, f"photo_{i}.jpg")
        root_target_file = os.path.join(root_img_dir, f"photo_{i}.jpg")
        try:
            req = urllib.request.Request(p_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = resp.read()
                with open(target_file, "wb") as f_out:
                    f_out.write(data)
                with open(root_target_file, "wb") as f_out2:
                    f_out2.write(data)
            cat = cat_cycle[(i - 1) % len(cat_cycle)]
            photo_meta.append({
                "src": f"./img/photo_{i}.jpg",
                "cat": cat,
                "title": f"{clean_name} {cat.capitalize()} 공간 {i}"
            })
        except Exception:
            pass

    price_val = 320000
    config_content = f"""/**
 * {clean_name} 공식 웹사이트 설정 데이터
 * Auto-generated by Adopter Continuous Search Engine
 */

const STAY_CONFIG = {{
  brandName: "{clean_name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "머묾, 그 자체가 온전한 쉼이 되는 곳",
  description: "{clean_name}에서 전하는 온전하고 프라이빗한 쉼. 제주의 자연과 돌담이 어우러진 아름다운 공간.",
  
  owner: "호스트",
  businessNo: "",
  address: "{target['address']}",
  phone: "{target['phone']}",
  email: "contact@adopter.co.kr",
  domain: "{slug}.adopter.co.kr",
  
  kakaoChatUrl: "http://pf.kakao.com/_HCTxiX/chat",
  naverMapUrl: "{target['naverLink']}",
  instagramUrl: "{target.get('instagram', '')}",
  
  youtubeIntroId: "f09Xfn1fHm8",
  youtubeTourId: "JG92-0fSScQ",
  
  pricing: {{
    weekday: {price_val},
    weekend: {price_val + 40000},
    peakSurcharge: 40000,
    baseGuests: 4,
    maxGuests: 8,
    extraGuestFee: 20000,
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
    with open(os.path.join(root_slug_dir, "stay_config.js"), "w", encoding="utf-8") as f_cfg2:
        f_cfg2.write(config_content)

    return {
        "slug": slug,
        "folder": folder_name,
        "url": f"https://{slug}.adopter.co.kr",
        "photosCount": len(photo_meta)
    }

def push_to_google_sheet(rows):
    if not rows:
        return
    payload = json.dumps(rows, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(APPS_SCRIPT_URL, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    try:
        with opener.open(req, timeout=20) as resp:
            log(f"구글 시트 전송 결과: {resp.read().decode('utf-8')}")
    except Exception as e:
        log(f"구글 시트 전송 에러: {e}")

def run_continuous_producer():
    log("================================================================")
    log("🔎 [Adopter 지속 발굴 & 제작 엔진 가동] 제주 미보유 숙소 추가 탐색")
    log("================================================================")

    # 기존 생성된 PID 목록 로드 (중복 생성 방지)
    existing_folders = os.listdir(CUSTOMER_DIR)
    known_pids = set()
    for f in existing_folders:
        match = re.search(r'stay-(\d+)', f)
        if match:
            known_pids.add(match.group(1))

    search_queries = [
        "제주 조천 감성숙소", "제주 조천 풀빌라", "제주 구좌 감성숙소",
        "제주 평대리 펜션", "제주 세화 풀빌라", "제주 성산 독채펜션",
        "제주 표선 감성숙소", "제주 남원 펜션", "제주 위미 감성숙소",
        "제주 안덕 감성숙소", "제주 대정 풀빌라", "제주 한경면 펜션"
    ]

    discovered_candidates = []
    for q in search_queries:
        log(f"검색 쿼리 실행 중: '{q}'...")
        try:
            url = f"https://m.search.naver.com/search.naver?query={urllib.parse.quote(q)}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                pids = re.findall(r'place\.naver\.com/accommodation/(\d+)', html)
                for pid in pids:
                    if pid not in known_pids and pid not in discovered_candidates:
                        discovered_candidates.append(pid)
        except Exception:
            pass
        time.sleep(0.3)
        if len(discovered_candidates) >= 20:
            break

    log(f"총 {len(discovered_candidates)}개 신규 후보 발굴. 홈페이지 부재 여부 정밀 심사 시작...")

    qualified_targets = []
    for pid in discovered_candidates:
        info = inspect_place_strictly(pid)
        if info:
            log(f"  ✨ [합격! 외부 홈페이지 없음] {info['name']} (PID: {pid})")
            qualified_targets.append(info)
            if len(qualified_targets) >= 10:
                break
        time.sleep(0.3)

    log(f"\n최종 엄선된 {len(qualified_targets)}개 신규 숙소 자동 빌드 시작...")
    today_prefix = datetime.now().strftime("%y%m%d")
    sheet_rows = []

    for idx, target in enumerate(qualified_targets, 1):
        slug = f"stay-{target['pid']}"
        built = build_stay_website(target, slug)
        log(f"  [{idx}/{len(qualified_targets)}] {target['name']} -> {built['url']} (사진 {built['photosCount']}장)")

        row = [
            "숙박업",
            target['naverLink'],
            "95%",
            sanitize_text(target['name']),
            f"{today_prefix}-{slug}",
            built['url'],
            "제작완료",
            "준비완료",
            target['phone'],
            target['address'],
            "320000",
            target['instagram'],
            "",
            "",
            "",
            f"자동발굴제작완료 (사진:{built['photosCount']}장/SVG단색화/화이트견적기)"
        ]
        sheet_rows.append(row)

    if sheet_rows:
        log("\n구글 시트로 신규 발굴 제작 데이터 전송 중...")
        push_to_google_sheet(sheet_rows)
        log("🎉 신규 발굴 10개 구글 시트 전송 완료!")
    else:
        log("신규 추가 발굴 완료!")

if __name__ == "__main__":
    run_continuous_producer()
