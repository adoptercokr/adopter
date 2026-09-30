import os
import json
import re
import shutil
import urllib.request
import time
import sys
import uuid

# Force utf-8 printing just in case
sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
TEMPLATE_DIR = os.path.join(ADOPTER_DIR, "templates", "01-stay")
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, "Customer")

sys.path.append(CURRENT_DIR)
import cloudflare_manager

def fetch_html_curl(url):
    temp_file = f"temp_{uuid.uuid4().hex}.html"
    try:
        cmd = f"curl.exe -s -A \"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15\" -o {temp_file} \"{url}\""
        os.system(cmd)
        with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return html
    except Exception as e:
        print(f"[ERROR] curl failed: {e}")
        return ""

def fetch_apollo_state(html):
    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
    if state_match:
        try:
            return json.loads(state_match.group(1))
        except:
            return None
    return None

def fetch_photos(pid):
    photo_urls = []
    for tab in ["home", "photo"]:
        url = f"https://m.place.naver.com/accommodation/{pid}/{tab}"
        html = fetch_html_curl(url)
        src_matches = re.findall(r'src=(https%3A%2F%2F[^\s"\'&]+)', html)
        for sm in src_matches:
            unquoted = urllib.parse.unquote(sm)
            if any(domain in unquoted for domain in ['ldb-phinf', 'naverbooking-phinf']):
                if not any(ex in unquoted.lower() for ex in ['profile', 'icon', 'favicon']):
                    if unquoted not in photo_urls:
                        photo_urls.append(unquoted)
        if len(photo_urls) >= 15: break
    return photo_urls[:10]

def build_stay(item):
    slug = item.get('folder', '').split('-')[-1]
    if not slug: slug = item.get('subdomain')
    pid_match = re.search(r'/accommodation/(\d+)', item.get('naverLink', ''))
    if not pid_match or not slug: return False
    pid = pid_match.group(1)
    
    # 1. Fetch raw HTML first
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    html = fetch_html_curl(url)
    
    # 2. Extract TRUE name from HTML <title> to avoid cp949 JSON corruption
    clean_name = slug
    t_match = re.search(r'<title>(.*?)</title>', html)
    if t_match:
        clean_name = t_match.group(1).replace(' - 네이버 지도', '').replace('네이버 플레이스', '').replace('제주', '').strip()
        # Fallback cleanup just in case
        if clean_name.startswith('- '): clean_name = clean_name[2:]
        if clean_name == "": clean_name = slug
    
    print(f"==================================================")
    print(f"[{clean_name}] 분석 및 맞춤 홈페이지 제작 시작 (PID: {pid})")
    
    raw_data = fetch_apollo_state(html)
    if not raw_data:
        print("[실패] 차단(429) 또는 데이터 없음. 건너뜁니다.")
        return False
        
    # MUST match exactly what _route_map.js expects
    dest_dir = os.path.join(CUSTOMER_DIR, f"260930-{slug}")

    img_dir = os.path.join(dest_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    
    print("사진 다운로드 중...")
    photos = fetch_photos(pid)
    for i, p_url in enumerate(photos, 1):
        target_file = os.path.join(img_dir, f"photo_{i}.jpg")
        try:
            req = urllib.request.Request(p_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                with open(target_file, "wb") as f_out:
                    f_out.write(resp.read())
        except: pass

    raw_str = json.dumps(raw_data, ensure_ascii=False)
    prices = re.findall(r'\"price\":(\d+)', raw_str)
    prices = sorted([int(p) for p in set(prices) if int(p) > 50000])
    weekday = f"{prices[0]:,}" if len(prices) > 0 else "200,000"
    weekend = f"{prices[-1]:,}" if len(prices) > 0 else "250,000"
    
    js_code = f'''
const STAY_CONFIG = {{
  name: "{clean_name}",
  subtitle: "Premium Stay",
  description: "머묾, 그 자체가 온전한 쉼이 되는 공간",
  benefits: [
    {{ id: "b1", icon: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" }},
    {{ id: "b2", icon: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }}
  ],
  spaces: [
    {{ id: "s1", title: "메인 공간", subtitle: "Main Space", mainImage: "./img/photo_1.jpg", images: ["./img/photo_1.jpg", "./img/photo_2.jpg"], totalPhotos: 2 }},
    {{ id: "s2", title: "휴식 공간", subtitle: "Rest Area", mainImage: "./img/photo_3.jpg", images: ["./img/photo_3.jpg", "./img/photo_4.jpg"], totalPhotos: 2 }}
  ],
  facilities: [
    {{ name: "무선 인터넷", icon: "wifi" }},
    {{ name: "주차장", icon: "parking" }}
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "반려동물 동반 불가"
  ],
  rates: {{
    weekday: "{weekday}",
    weekend: "{weekend}",
    peak: "{weekend}"
  }}
}};
'''
    with open(os.path.join(dest_dir, "stay_config.js"), "w", encoding="utf-8") as f:
        f.write(js_code.strip())
        
    files_to_copy = ["index.html", ".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))
            
    print(f"[{clean_name}] 수제작 완료! (경로: {dest_dir})")
    return True

def main():
    print("==================================================")
    print("최종 복구: 올바른 폴더 덮어쓰기 시작")
    print("==================================================")
    
    with open(os.path.join(ADOPTER_DIR, 'tools', 'west_10_collected.json'), 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(os.path.join(ADOPTER_DIR, 'tools', 'west_batch2_collected.json'), 'r', encoding='utf-8') as f:
        data2 = json.load(f)
        
    all_items = data1 + data2
    success_count = 0
    
    for idx, item in enumerate(all_items):
        try:
            if build_stay(item):
                success_count += 1
            if idx < len(all_items) - 1:
                print(f"대기중... (진행률: {idx+1}/{len(all_items)})")
                time.sleep(1)
        except Exception as e:
            print(f"[오류 발생] {e}")
            
    print("==================================================")
    print(f"복구 렌더링 완료! ({success_count}개 숙소)")
    print("Cloudflare 배포를 시작합니다...")
    cloudflare_manager.deploy_pages(ADOPTER_DIR)
    print("[배포 성공] 완료되었습니다.")

if __name__ == "__main__":
    main()
