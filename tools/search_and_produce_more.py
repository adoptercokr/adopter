#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================================================
?뵇 Adopter Dynamic Search & Continuous Producer (?ъ빞 臾댁씤 異붽? 諛쒓뎬 諛??쒖옉)
------------------------------------------------------------------------------
- 議곗쿇, 援ъ쥖, ?깆궛, ?쒖꽑, ?⑥썝, ?쒓??? ?덈뜒 ???쒖＜ ?꾩뿭??媛먯꽦 ?숈냼瑜?異붽? 諛쒓뎬
- Apollo State 諛??듭빱瑜?寃?ы븯???몃? ?낅┰ ?덊럹?댁?媛 0媛쒖씤 怨노쭔 ?꾩꽑
- ?ъ쭊 理쒕? 10???ㅼ슫濡쒕뱶 諛?留욎땄???ъ씠??鍮뚮뱶 (臾댁콈??SVG ?꾩씠肄? ?붿씠??寃ъ쟻湲?
- 援ш? ?쒗듃濡??좉퇋 ?쒖옉 ???ㅼ떆媛??꾩넚
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
    text = text.replace("?낆콈?쒖뀡", "?⑤룆?쒖뀡")
    text = text.replace("?낆콈 ?鍮뚮씪", "?⑤룆 ?鍮뚮씪")
    text = text.replace("?낆콈", "?⑤룆二쇳깮")
    return text.strip()

def inspect_place_strictly(pid):
    """?몃? ?덊럹?댁?媛 0媛쒖씤 怨노쭔 ?좊퀎"""
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception:
        return None

    # ?덊럹?댁? 議댁옱 ?щ? 寃??
    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>', html, re.DOTALL)
    if not state_match:
        return None

    try:
        state = json.loads(state_match.group(1))
    except Exception:
        return None

    # ?덊럹?댁? 留곹겕 泥댄겕
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)<\/a>', html, re.IGNORECASE)
    for href, text in anchors:
        if any(h in href.lower() for h in ['instagram.com', 'naver.com', 'daum.net', 'kakao.com', 'tel:']):
            continue
        if href.startswith('http') and not any(p in href for p in ['map.naver', 'm.place.naver', 'booking.naver']):
            return None # ?낅┰ ?덊럹?댁? 蹂댁쑀 -> ?쒖쇅

    detail_keys = [k for k in state.keys() if k.startswith('PlaceDetailBase:')]
    if not detail_keys:
        return None

    base = state[detail_keys[0]]
    name = base.get('name', '')
    if not name:
        return None

    # ?덊럹?댁? URL ?꾨뱶 泥댄겕
    for k in ['homepage', 'url', 'site']:
        val = base.get(k)
        if val and isinstance(val, str) and val.startswith('http') and not any(p in val for p in ['instagram.com', 'naver.com']):
            return None

    phone = base.get('virtualPhone') or base.get('phone') or "0507-0000-0000"
    road_addr = base.get('roadAddress') or base.get('address') or "?쒖＜?밸퀎?먯튂??

    # ?몄뒪?洹몃옩
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
    root_slug_dir = os.path.join(ADOPTER_DIR, f"{today_prefix}-{slug}")

    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(root_slug_dir, exist_ok=True)
    img_dir = os.path.join(dest_dir, "img")
    root_img_dir = os.path.join(root_slug_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(root_img_dir, exist_ok=True)

# 1. ?쒗뵆由?蹂듭궗 諛?HTML ?대? ?띿뒪???대?吏 寃쎈줈 移섑솚
    files_to_copy = [".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))
            shutil.copy2(src, os.path.join(root_slug_dir, f))

    # index.html 移섑솚
    index_src = os.path.join(TEMPLATE_DIR, "index.html")
    if os.path.exists(index_src):
        with open(index_src, "r", encoding="utf-8") as f:
            html_content = f.read()

        # ?띿뒪??移섑솚
        html_content = html_content.replace("?ъ뒪?뚯씠", clean_name)
        html_content = html_content.replace("HEESTAY", slug.upper())
        html_content = html_content.replace("jejuheestay.co.kr", f"{slug}.adopter.co.kr")
        
        # ?대?吏 寃쎈줈 移섑솚 (photo_1.jpg ~ photo_10.jpg 諛섎났)
        import urllib.parse
        img_paths = re.findall(r'(\./img/[^"\'\s]+\.jpg|/img/[^"\'\s]+\.jpg|img/[^"\'\s]+\.jpg)', html_content)
        unique_imgs = list(set(img_paths))
        for idx, old_img in enumerate(unique_imgs):
            new_img = old_img.replace(old_img.split('/')[-1], f"photo_{(idx % 10) + 1}.jpg")
            html_content = html_content.replace(old_img, new_img)
            # URL ?몄퐫?⑸맂 寃쎈줈??移섑솚
            encoded_old = urllib.parse.quote(old_img)
            if "%" in encoded_old:
                encoded_new = urllib.parse.quote(new_img)
                html_content = html_content.replace(encoded_old, encoded_new)
                
        with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(os.path.join(root_slug_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

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
                "title": f"{clean_name} {cat.capitalize()} 怨듦컙 {i}"
            })
        except Exception:
            pass

    price_val = 320000
    config_content = f"""/**
 * {clean_name} 怨듭떇 ?뱀궗?댄듃 ?ㅼ젙 ?곗씠??
 * Auto-generated by Adopter Continuous Search Engine
 */

const STAY_CONFIG = {{
  brandName: "{clean_name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "癒몃Ь, 洹??먯껜媛 ?⑥쟾???쇱씠 ?섎뒗 怨?,
  description: "{clean_name}?먯꽌 ?꾪븯???⑥쟾?섍퀬 ?꾨씪?대퉿???? ?쒖＜???먯뿰怨??뚮떞???댁슦?ъ쭊 ?꾨쫫?ㅼ슫 怨듦컙.",
  
  owner: "?몄뒪??,
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
    {{ title: "?꾨씪?대퉿 ?뺤썝 & ?뚮씪??, subtitle: "Garden", desc: "?⑤룆 ?뺤썝 諛??쇱쇅 ?댁떇 怨듦컙 ?꾨퉬" }},
    {{ title: "?ш퀎???꾩슜 諛붾쿋??, subtitle: "BBQ", desc: "?낅┰ ?ㅼ씠??怨듦컙 諛?洹몃┫ 臾대즺 ?꾨퉬" }},
    {{ title: "?덈씫???쇨낵 ?⑥닔", subtitle: "Relax", desc: "?몄븞???꾨━誘몄뾼 移④뎄 諛?苡뚯쟻???꾩슜 ?쒖꽕" }}
  ],

  spaces: {{
    landSize: "120???吏",
    buildingSize: "35???⑤룆二쇳깮",
    floor1: "嫄곗떎, ??듭뀡 二쇰갑, 留덉뒪?곕８, ?⑤룎猷? ?뺤떎, ?뚯슦?붾８",
    outdoor: "?꾨씪?대퉿 ?뺤썝, ?쇱쇅 ?뚮씪?? 媛쒕퀎 諛붾쿋?먯옣, ?꾩슜 二쇱감怨듦컙"
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


    # Update route_map.js
    route_map_path = os.path.join(ADOPTER_DIR, 'functions', '_route_map.js')
    if os.path.exists(route_map_path):
        with open(route_map_path, 'r', encoding='utf-8') as f:
            rm_text = f.read()
        import ast
        try:
            dict_str = rm_text.split('=', 1)[1].strip().rstrip(';')
            route_map = ast.literal_eval(dict_str)
        except:
            route_map = {}
    else:
        route_map = {}
        
    route_map[slug] = f"{today_prefix}-{slug}"
    with open(route_map_path, 'w', encoding='utf-8') as f:
        f.write(f"export const routeMap = {repr(route_map)};\n")

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
            log(f"援ш? ?쒗듃 ?꾩넚 寃곌낵: {resp.read().decode('utf-8')}")
    except Exception as e:
        log(f"援ш? ?쒗듃 ?꾩넚 ?먮윭: {e}")

def run_continuous_producer():
    log("================================================================")
    log("?뵊 [Adopter 吏??諛쒓뎬 & ?쒖옉 ?붿쭊 媛?? ?쒖＜ 誘몃낫???숈냼 異붽? ?먯깋")
    log("================================================================")

    # 湲곗〈 ?앹꽦??PID 紐⑸줉 濡쒕뱶 (以묐났 ?앹꽦 諛⑹?)
    existing_folders = os.listdir(CUSTOMER_DIR)
    known_pids = set()
    for f in existing_folders:
        match = re.search(r'stay-(\d+)', f)
        if match:
            known_pids.add(match.group(1))

    search_queries = [
        "?쒖＜ 議곗쿇 媛먯꽦?숈냼", "?쒖＜ 議곗쿇 ?鍮뚮씪", "?쒖＜ 援ъ쥖 媛먯꽦?숈냼",
        "?쒖＜ ?됰?由??쒖뀡", "?쒖＜ ?명솕 ?鍮뚮씪", "?쒖＜ ?깆궛 ?낆콈?쒖뀡",
        "?쒖＜ ?쒖꽑 媛먯꽦?숈냼", "?쒖＜ ?⑥썝 ?쒖뀡", "?쒖＜ ?꾨? 媛먯꽦?숈냼",
        "?쒖＜ ?덈뜒 媛먯꽦?숈냼", "?쒖＜ ????鍮뚮씪", "?쒖＜ ?쒓꼍硫??쒖뀡"
    ]

    discovered_candidates = []
    for q in search_queries:
        log(f"寃??荑쇰━ ?ㅽ뻾 以? '{q}'...")
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

    log(f"珥?{len(discovered_candidates)}媛??좉퇋 ?꾨낫 諛쒓뎬. ?덊럹?댁? 遺???щ? ?뺣? ?ъ궗 ?쒖옉...")

    qualified_targets = []
    for pid in discovered_candidates:
        info = inspect_place_strictly(pid)
        if info:
            log(f"  ??[?⑷꺽! ?몃? ?덊럹?댁? ?놁쓬] {info['name']} (PID: {pid})")
            qualified_targets.append(info)
            if len(qualified_targets) >= 10:
                break
        time.sleep(0.3)

    log(f"\n理쒖쥌 ?꾩꽑??{len(qualified_targets)}媛??좉퇋 ?숈냼 ?먮룞 鍮뚮뱶 ?쒖옉...")
    today_prefix = datetime.now().strftime("%y%m%d")
    sheet_rows = []

    for idx, target in enumerate(qualified_targets, 1):
        slug = f"stay-{target['pid']}"
        built = build_stay_website(target, slug)
        log(f"  [{idx}/{len(qualified_targets)}] {target['name']} -> {built['url']} (?ъ쭊 {built['photosCount']}??")

        row = [
            "?숇컯??,
            target['naverLink'],
            "95%",
            sanitize_text(target['name']),
            f"{today_prefix}-{slug}",
            built['url'],
            "?쒖옉?꾨즺",
            "以鍮꾩셿猷?,
            target['phone'],
            target['address'],
            "320000",
            target['instagram'],
            "",
            "",
            "",
            f"?먮룞諛쒓뎬?쒖옉?꾨즺 (?ъ쭊:{built['photosCount']}??SVG?⑥깋???붿씠?멸껄?곴린)"
        ]
        sheet_rows.append(row)

    if sheet_rows:
        log("\n援ш? ?쒗듃濡??좉퇋 諛쒓뎬 ?쒖옉 ?곗씠???꾩넚 以?..")
        push_to_google_sheet(sheet_rows)
        log("?럦 ?좉퇋 諛쒓뎬 10媛?援ш? ?쒗듃 ?꾩넚 ?꾨즺!")
    else:
        log("?좉퇋 異붽? 諛쒓뎬 ?꾨즺!")

if __name__ == "__main__":
    run_continuous_producer()
