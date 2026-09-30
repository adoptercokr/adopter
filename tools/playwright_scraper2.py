import asyncio, json, os, re, shutil, random
from playwright.async_api import async_playwright

def extract_valid_id(url):
    m = re.search(r'/accommodation/(\d+)', url)
    return m.group(1) if m else None

async def scrape_place(page, item):
    pid = extract_valid_id(item.get('naverLink', ''))
    if not pid: return None
    
    facs = []
    prices = []
    desc = "머묾, 그 자체가 온전한 쉼이 되는 공간"
    images = []
    
    # 1. Fetch Home Tab (for photos, facilities, desc)
    home_url = f"https://m.place.naver.com/accommodation/{pid}/home"
    try:
        await page.goto(home_url, timeout=10000)
        html = await page.content()
        state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
        if state_match:
            state = json.loads(state_match.group(1))
            
            # Fetch Facilities
            fac_set = set()
            for k in state.keys():
                if k.startswith('InformationFacilities:'):
                    parts = k.split(':')
                    if len(parts) > 1: fac_set.add(parts[1].split()[0])
            if fac_set: facs = list(fac_set)
            
            # Fetch Images
            raw_str = json.dumps(state, ensure_ascii=False)
            found_urls = re.findall(r'(https://[a-zA-Z0-9\-\.]+(?:ldb-phinf|naverbooking-phinf)[^\s"\']+\.jpg\?type=[a-zA-Z0-9_]+)', raw_str)
            import urllib.parse
            for u in found_urls:
                u_dec = urllib.parse.unquote(u).replace('type=f100_100', 'type=w800_800').replace('type=f180_180', 'type=w800_800')
                if u_dec not in images: images.append(u_dec)
            
            # Fallback desc
            candidates = []
            def find_text(obj):
                if isinstance(obj, dict):
                    for v in obj.values(): find_text(v)
                elif isinstance(obj, list):
                    for v in obj: find_text(v)
                elif isinstance(obj, str):
                    if len(obj) > 30 and len(obj) < 300 and ('독채' in obj or '풀빌라' in obj or '펜션' in obj or '스테이' in obj):
                        if '리뷰' not in obj and 'blog' not in obj.lower() and '불펌' not in obj:
                            candidates.append(obj)
            find_text(state)
            if candidates:
                desc = sorted(candidates, key=len)[-1].replace('\n', ' ').replace('"', "'")
                if len(desc) > 100: desc = desc[:97] + "..."
    except Exception as e:
        print(f"Error fetching home for {pid}: {e}")

    # 2. Fetch Room Tab (for prices)
    room_url = f"https://m.place.naver.com/accommodation/{pid}/room"
    try:
        await page.goto(room_url, timeout=10000)
        # Give it a second to load the API response for rooms
        await page.wait_for_timeout(2000)
        
        price_elements = await page.evaluate('''() => {
            const texts = Array.from(document.querySelectorAll('*')).map(el => el.innerText || '');
            const prices = [];
            texts.join(' ').replace(/[1-9]\\d{0,2}(?:,\\d{3})+(?=\\s*원)/g, match => {
                prices.push(match);
            });
            return prices;
        }''')
        
        if price_elements:
            parsed = [int(p.replace(',', '')) for p in set(price_elements)]
            parsed = sorted([p for p in parsed if p > 50000])
            if parsed: prices = parsed
    except Exception as e:
        print(f"Error fetching room for {pid}: {e}")

    # If still no images, use DOM images
    if len(images) < 5:
        try:
            dom_imgs = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll('img'))
                    .map(img => img.src)
                    .filter(src => src.includes('pstatic.net') && !src.includes('profile'))
            }''')
            for d_img in dom_imgs:
                if d_img not in images: images.append(d_img)
        except: pass

    return { 'facs': facs, 'prices': prices, 'desc': desc, 'images': images }

async def main():
    with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f: d1 = json.load(f)
    with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f: d2 = json.load(f)
    items = d1 + d2
    
    for i in items:
        if 'staypanpo' in i.get('folder', ''):
            i['naverLink'] = "https://m.place.naver.com/accommodation/1638843236/home"
            
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")
        page = await context.new_page()
        
        for item in items:
            folder = "260930-" + (item.get('folder', '').split('-')[-1] or item.get('subdomain'))
            print(f"Scraping {folder}...")
            data = await scrape_place(page, item)
            
            if not data: continue
            
            facs = data['facs'] if data['facs'] else ["무선 인터넷", "주차장", "독채"]
            desc = data['desc']
            prices = data['prices']
            
            weekday = f"{prices[0]:,}" if len(prices) > 0 else "0"
            weekend = f"{prices[-1]:,}" if len(prices) > 0 else "0"
            
            imgs = data['images']
            if not imgs: imgs = [f"./img/photo_{i}.jpg" for i in range(1, 6)]
            
            # Generate exactly what index.html needs
            spaces_js = ""
            for i, img in enumerate(imgs[:15]): # Use up to 15 images
                spaces_js += f'    {{ id: "s{i+1}", mainImage: "{img}" }},\n'
                
            facs_js = ",\n    ".join([f'{{ name: "{f}", icon: "wifi" }}' for f in facs[:8]])
            
            bt = chr(96)
            nl = item.get('naverLink', '')
            ph = item.get('phone', '')
            nm = item.get('name', 'Stay')
            v = random.randint(1, 4)
            
            js = f'''const STAY_CONFIG = {{
  variant: {v},
  naverLink: "{nl}",
  phone: "{ph}",
  name: "{nm}",
  subtitle: "Premium Stay",
  description: "{desc}",
  benefits: [
    {{ id: "b1", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>{bt}, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" }},
    {{ id: "b2", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>{bt}, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }}
  ],
  spaces: [
{spaces_js}
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
                    f.write(js)
                shutil.copy2('templates/01-stay/index.html', os.path.join('Customer', folder, 'index.html'))
                print(f"Updated {folder} - {len(imgs)} imgs, Price: {weekday}")
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
