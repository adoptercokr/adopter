import os, json, re, urllib.request, uuid

def fetch_html_curl(url):
    temp_file = f"temp_{uuid.uuid4().hex}.html"
    try:
        cmd = f'curl.exe -s -A "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15" -o {temp_file} "{url}"'
        os.system(cmd)
        with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
        if os.path.exists(temp_file): os.remove(temp_file)
        return html
    except: return ""

def get_unique_data(pid):
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    html = fetch_html_curl(url)
    state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
    
    facs = []
    desc = "머묾, 그 자체가 온전한 쉼이 되는 공간"
    prices = []
    
    if state_match:
        state = json.loads(state_match.group(1))
        # Facilities
        fac_set = set()
        for k in state.keys():
            if k.startswith('InformationFacilities:'):
                parts = k.split(':')
                if len(parts) > 1: fac_set.add(parts[1].split()[0])
        if fac_set: facs = list(fac_set)
        
        # Prices
        raw_str = json.dumps(state, ensure_ascii=False)
        found_prices = re.findall(r'"price":(\d+)', raw_str)
        valid_prices = sorted([int(p) for p in set(found_prices) if int(p) > 50000])
        if valid_prices: prices = valid_prices
        
        # Description
        candidates = []
        def find_text(obj):
            if isinstance(obj, dict):
                for v in obj.values(): find_text(v)
            elif isinstance(obj, list):
                for v in obj: find_text(v)
            elif isinstance(obj, str):
                if len(obj) > 30 and len(obj) < 300 and ('독채' in obj or '풀빌라' in obj or '펜션' in obj or '제주' in obj or '스테이' in obj):
                    if '리뷰' not in obj and 'blog' not in obj.lower() and '불펌' not in obj:
                        candidates.append(obj)
        find_text(state)
        if candidates:
            # Sort by length, prefer shorter concise ones over long blog dumps
            desc = sorted(candidates, key=len)[-1].replace('\n', ' ').replace('"', "'")
            # Limit to 100 chars
            if len(desc) > 100: desc = desc[:97] + "..."
            
    return facs, desc, prices

def update_folder(folder, pid, name):
    facs, desc, prices = get_unique_data(pid)
    
    weekday = f"{prices[0]:,}" if len(prices) > 0 else "200,000"
    weekend = f"{prices[-1]:,}" if len(prices) > 0 else "250,000"
    
    if not facs: facs = ["무선 인터넷", "주차장", "독채"]
    
    # Generate facilities JS array
    facs_js = ",\n    ".join([f'{{ name: "{f}", icon: "wifi" }}' for f in facs[:6]])
    
    # We will format the JS code with unicode escapes to be safe
    # But since we use python file I/O with utf-8, it's fine.
    
    bt = chr(96)
    js_code = f'''const STAY_CONFIG = {{
  name: "{name}",
  subtitle: "Premium Stay",
  description: "{desc}",
  benefits: [
    {{ id: "b1", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>{bt}, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" }},
    {{ id: "b2", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>{bt}, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }}
  ],
  spaces: [
    {{ id: "s1", title: "메인 공간", subtitle: "Main Space", mainImage: "./img/photo_1.jpg", images: ["./img/photo_1.jpg", "./img/photo_2.jpg"], totalPhotos: 2 }},
    {{ id: "s2", title: "휴식 공간", subtitle: "Rest Area", mainImage: "./img/photo_3.jpg", images: ["./img/photo_3.jpg", "./img/photo_4.jpg", "./img/photo_5.jpg"], totalPhotos: 3 }}
  ],
  facilities: [
    {facs_js}
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
    p = os.path.join('Customer', folder, 'stay_config.js')
    if os.path.exists(p):
        with open(p, 'w', encoding='utf-8') as f:
            f.write(js_code)
        print(f"Updated {folder}: {weekday} / {len(facs)} facs / {desc[:20]}")

with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f:
    d1 = json.load(f)
with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f:
    d2 = json.load(f)
    
for item in d1 + d2:
    folder = "260930-" + (item.get('folder', '').split('-')[-1] or item.get('subdomain'))
    pid_match = re.search(r'/accommodation/(\d+)', item.get('naverLink', ''))
    if pid_match:
        update_folder(folder, pid_match.group(1), item.get('name'))
