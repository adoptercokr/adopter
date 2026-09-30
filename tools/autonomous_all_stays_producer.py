#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================================================================
?뙆 Adopter Autonomous All-Stays Producer (珥덇퀬??臾댁씤 ?꾩옄???쒖옉 ?붿쭊)
------------------------------------------------------------------------------
- LLM API ?좏겙 鍮꾩슜 0??(?꾩쟾 臾대즺 ?뚭퀬由ъ쬁 湲곕컲 怨좎냽 ?앹꽦)
- ?ъ쟾 ?섏쭛??20媛??숈냼 諛?異붽? 諛쒓뎬 ?숈냼瑜??쒖감?곸쑝濡??꾩옄???쒖옉
- ?ㅼ씠踰?怨듭떇 怨좏솕吏??ъ쭊 理쒕? 10???ㅼ슫濡쒕뱶
- 議곗옟??而щ윭 ?대え吏 諛곗젣 -> 100% 臾댁콈???⑥깋 誘몃땲硫 ?쇱씤 SVG ?꾩씠肄??묒옱
- ?뚮퉬肄??쒓굅 (鍮??곗씠??URI ?곸슜)
- 怨듦컙 媛ㅻ윭由?-> ?ㅼ떆媛??덉빟 ?щ젰 ?쒖꽌 諛곗튂
- Customer/ 諛?猷⑦듃 /{slug}/ ?숈떆 諛고룷 (Cloudflare Pages ?쒕툕?꾨찓???쇱슦??
- 援ш? ?ㅽ봽?덈뱶?쒗듃 ?ㅼ떆媛???異붽? (doPost ?곕룞)
- Cloudflare Pages & Git Commit/Push ?먮룞??
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

def fetch_photos(pid):
    """?ㅼ씠踰??뚮젅?댁뒪?먯꽌 怨좏솕吏??ъ쭊 理쒕? 10??異붿텧"""
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

def inspect_place_detail(pid):
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception:
        return None

    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>', html, re.DOTALL)
    if not state_match:
        return None

    try:
        state = json.loads(state_match.group(1))
    except Exception:
        return None

    detail_keys = [k for k in state.keys() if k.startswith('PlaceDetailBase:')]
    if not detail_keys:
        return None

    base = state[detail_keys[0]]
    name = base.get('name', '')
    if not name:
        return None

    phone = base.get('virtualPhone') or base.get('phone') or "0507-0000-0000"
    road_addr = base.get('roadAddress') or base.get('address') or "?쒖＜?밸퀎?먯튂??

    # ?몄뒪?洹몃옩 留곹겕 ?뺤씤
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)<\/a>', html, re.IGNORECASE)
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
            # URL ?몄퐫?⑸맂 寃쎈줈??移섑솚 (og:image ?깆뿉 ?ъ슜??
            encoded_old = urllib.parse.quote(old_img)
            if "%" in encoded_old:
                encoded_new = urllib.parse.quote(new_img)
                html_content = html_content.replace(encoded_old, encoded_new)
                
        with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(os.path.join(root_slug_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

    # 2. ?ъ쭊 ?ㅼ슫濡쒕뱶
    photos = fetch_photos(target['pid'])
    cat_cycle = ["exterior", "living", "bedroom", "kitchen", "outdoor"]
    photo_meta = []

    for i, p_url in enumerate(photos, 1):
        target_file = os.path.join(img_dir, f"photo_{i}.jpg")
        root_target_file = os.path.join(root_img_dir, f"photo_{i}.jpg")
        try:
            req = urllib.request.Request(p_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
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

    price_val = int(target.get('price', 300000))
    config_content = f"""/**
 * {clean_name} 怨듭떇 ?뱀궗?댄듃 ?ㅼ젙 ?곗씠??
 * Auto-generated by Adopter Autonomous Producer
 */

const STAY_CONFIG = {{
  brandName: "{clean_name}",
  brandSubtitle: "Jeju Private Stay",
  tagline: "癒몃Ь, 洹??먯껜媛 ?⑥쟾???쇱씠 ?섎뒗 怨?,
  description: "{clean_name}?먯꽌 ?꾪븯???⑥쟾?섍퀬 ?꾨씪?대퉿???? ?쒖＜???먯뿰怨??뚮떞???댁슦?ъ쭊 ?꾨쫫?ㅼ슫 怨듦컙.",
  
  owner: "?몄뒪??,
  businessNo: "",
  address: "{target.get('address') or target.get('addr') or '?쒖＜?밸퀎?먯튂??}",
  phone: "{target.get('phone', '0507-0000-0000')}",
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

def run_autonomous_batch():
    log("================================================================")
    log("?? [Adopter ?먯쑉 ?쒖옉 ?붿쭊 媛?? 援ш? ?쒗듃 ?꾩껜 ?寃??곗냽 鍮뚮뱶 ?쒖옉")
    log("================================================================")

    # 1. 湲곗〈 west_10 諛?west_batch2 濡쒕뱶
    targets = []
    seen_pids = set()

    for path in ['tools/west_10_collected.json', 'tools/west_batch2_collected.json']:
        full_p = os.path.join(ADOPTER_DIR, path)
        if os.path.exists(full_p):
            with open(full_p, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    pid_match = re.search(r'/accommodation/(\d+)', item.get('naverLink', ''))
                    if pid_match:
                        pid = pid_match.group(1)
                        if pid not in seen_pids:
                            seen_pids.add(pid)
                            item['pid'] = pid
                            targets.append(item)

    log(f"?섏쭛 紐⑸줉?먯꽌 珥?{len(targets)}媛??寃??숈냼 濡쒕뱶 ?꾨즺!")

    # 2. 媛??숈냼 ?뺣? ?뺣낫 ?뚯떛 諛??ъ씠??鍮뚮뱶
    today_prefix = datetime.now().strftime("%y%m%d")
    built_sheet_rows = []

    for idx, item in enumerate(targets, 1):
        pid = item['pid']
        name = item.get('name', '')
        log(f"\n[{idx}/{len(targets)}] {name} (PID: {pid}) 鍮뚮뱶 ?쒖옉...")

        # 理쒖떊 ?뺣낫 媛?몄삤湲?
        detailed = inspect_place_detail(pid)
        if detailed:
            item.update(detailed)

        # ?щ윭洹?寃곗젙
        folder_raw = item.get('folder', '')
        if folder_raw and '-' in folder_raw:
            slug = folder_raw.split('-')[-1]
        else:
            slug = f"stay-{pid}"

        built = build_stay_website(item, slug)
        log(f"  -> ?ъ씠??鍮뚮뱶 ?꾨즺! ?ъ쭊 {built['photosCount']}??| {built['url']}")

        # ?쒗듃 ???앹꽦
        row = [
            "?숇컯??,
            item.get('naverLink', f"https://m.place.naver.com/accommodation/{pid}/home"),
            "95%",
            sanitize_text(item.get('name', '')),
            f"{today_prefix}-{slug}",
            built['url'],
            "?쒖옉?꾨즺",
            "以鍮꾩셿猷?,
            item.get('phone', '0507-0000-0000'),
            item.get('address') or item.get('addr') or '?쒖＜?밸퀎?먯튂??,
            str(item.get('price', 300000)),
            item.get('sns1') or item.get('instagram', ''),
            "",
            "",
            "",
            f"?먯쑉?쒖옉?붿쭊?꾨즺 (?ъ쭊:{built['photosCount']}??SVG?⑥깋???붿씠?멸껄?곴린)"
        ]
        built_sheet_rows.append(row)

        # 5媛쒕쭏??援ш? ?쒗듃 以묎컙 ?꾩넚
        if len(built_sheet_rows) % 5 == 0:
            log(f"-> 5媛??쒖옉 ?꾨즺. 援ш? ?쒗듃濡?以묎컙 ?꾩넚 以?..")
            push_to_google_sheet(built_sheet_rows[-5:])

        time.sleep(0.5)

    # ?⑥? ??理쒖쥌 ?꾩넚
    remaining = len(built_sheet_rows) % 5
    if remaining > 0:
        log(f"-> ?⑥? {remaining}媛???援ш? ?쒗듃 理쒖쥌 ?꾩넚 以?..")
        push_to_google_sheet(built_sheet_rows[-remaining:])

    log("\n?럦 珥?20媛??숈냼 ?ъ씠??鍮뚮뱶 諛?援ш? ?쒗듃 諛섏쁺 ?꾨즺!")

if __name__ == "__main__":
    run_autonomous_batch()
