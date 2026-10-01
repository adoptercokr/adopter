import os
import sys
import json
import re
import shutil
import urllib.request
import urllib.parse
import random
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, 'Customer')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def search_pids(keyword):
    url = f'https://m.search.naver.com/search.naver?query={urllib.parse.quote(keyword)}'
    req = urllib.request.Request(url, headers=HEADERS)
    pids = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            found = re.findall(r'place\.naver\.com/accommodation/(\d+)', html)
            for pid in found:
                if pid not in pids:
                    pids.append(pid)
    except Exception as e:
        print(f"Search failed for {keyword}: {e}")
    return pids

def fetch_details(pid):
    url = f'https://m.place.naver.com/accommodation/{pid}/home'
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            match = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.*?\});\s*</script>', html)
            if not match:
                return None
            state = json.loads(match.group(1))
            
            # Find base entity
            root = state.get('ROOT_QUERY', {})
            base_key = None
            for k in root.keys():
                if k.startswith('accommodationBase'):
                    base_key = root[k].get('__ref')
                    break
            
            if not base_key:
                return None
                
            base_data = state.get(base_key, {})
            name = base_data.get('name', '')
            if not name: return None
            
            # Filter logic: skip if it has independent homepage
            urls = base_data.get('urls', [])
            has_homepage = any('homepage' in u.get('type', '') for u in urls if isinstance(u, dict))
            if has_homepage:
                return None
                
            address = base_data.get('address', '')
            phone = base_data.get('phone', '')
            price = 300000
            
            # Images
            images = []
            for k, v in state.items():
                if k.startswith('Image:') and v.get('url'):
                    if v['url'] not in images:
                        images.append(v['url'])
                if len(images) >= 15:
                    break
            
            if len(images) < 10:
                return None
                
            return {
                'pid': pid,
                'name': name,
                'address': address,
                'phone': phone,
                'images': images[:10],
                'naverUrl': url
            }
    except Exception as e:
        pass
    return None

def push_to_sheet(data_list):
    try:
        req = urllib.request.Request(
            APPS_SCRIPT_URL,
            data=json.dumps(data_list).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as resp:
            print("Pushed to Google Sheet!")
    except Exception as e:
        print(f"Sheet push failed: {e}")

def get_proxy_url(naver_url):
    return f"https://adopter.co.kr/api/img?url={urllib.parse.quote(naver_url)}"

def main():
    queries = ['제주 서귀포 독채 풀빌라', '제주 감성 숙소', '제주 조천 풀빌라', '제주 애월 독채펜션']
    collected = []
    
    # Existing PIDs to avoid duplicates
    existing = set()
    if os.path.exists('west_10_collected.json'):
        with open('west_10_collected.json', 'r', encoding='utf-8') as f:
            for item in json.load(f):
                existing.add(item.get('pid'))
    
    print("Searching Naver Place...")
    for q in queries:
        if len(collected) >= 10: break
        pids = search_pids(q)
        for pid in pids:
            if pid in existing: continue
            if len(collected) >= 10: break
            
            print(f"Fetching {pid}...")
            details = fetch_details(pid)
            if details:
                collected.append(details)
                existing.add(pid)
                print(f"Found: {details['name']} ({len(collected)}/10)")
                
    if not collected:
        print("No new places found.")
        return

    # Build sites
    templates = ['tpl-05-wabi-sabi', 'tpl-06-modern-glass', 'tpl-07-hanok-heritage', 
                 'tpl-08-coastal-breeze', 'tpl-09-industrial-chic', 'tpl-10-velaa-luxury']
    
    sheet_data = []
    route_map_adds = []
    
    today = datetime.now().strftime('%y%m%d')
    
    for i, place in enumerate(collected):
        # Clean name
        safe_name = re.sub(r'[^a-zA-Z0-9가-힣]', '', place['name'])
        slug = f"{today}-{safe_name}"
        folder_path = os.path.join(CUSTOMER_DIR, slug)
        
        # Pick template
        tmpl = templates[i % len(templates)]
        tmpl_path = os.path.join(CUSTOMER_DIR, tmpl)
        
        shutil.copytree(tmpl_path, folder_path)
        
        # Rewrite stay_config.js
        cfg_path = os.path.join(folder_path, 'stay_config.js')
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            
        # Update name, address, phone
        cfg = re.sub(r'brandName:\s*".*?"', f'brandName: "{place["name"]}"', cfg)
        cfg = re.sub(r'address:\s*".*?"', f'address: "{place["address"]}"', cfg)
        cfg = re.sub(r'phone:\s*".*?"', f'phone: "{place["phone"]}"', cfg)
        
        # The templates use photo_1.jpg to photo_10.jpg
        # We need to replace them with the proxy URLs
        for idx in range(1, 11):
            proxy_url = get_proxy_url(place['images'][idx-1])
            cfg = cfg.replace(f'./img/photo_{idx}.jpg', proxy_url)
            
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(cfg)
            
        site_url = f"https://{safe_name}.adopter.co.kr"
        route_map_adds.append(f'  "{safe_name}": "Customer/{slug}",')
        
        sheet_data.append({
            "name": place['name'],
            "subdomain": safe_name,
            "theme": tmpl,
            "siteUrl": site_url,
            "naverUrl": place['naverUrl'],
            "price": "300000",
            "phone": place['phone'],
            "address": place['address'],
            "memo": "Auto-built with Proxy Images"
        })
        print(f"Built {place['name']} using {tmpl}")
        
    # Update route map
    rm_path = os.path.join(ADOPTER_DIR, 'functions', '_route_map.js')
    with open(rm_path, 'r', encoding='utf-8') as f:
        rm = f.read()
    
    insert_pos = rm.find('const routeMap = {') + len('const routeMap = {\n')
    rm = rm[:insert_pos] + '\n'.join(route_map_adds) + '\n' + rm[insert_pos:]
    with open(rm_path, 'w', encoding='utf-8') as f:
        f.write(rm)
        
    # Push to sheet
    push_to_sheet(sheet_data)
    print("Done building 10 new properties.")

if __name__ == '__main__':
    main()
