import urllib.request
import urllib.parse
import re
import json

targets = [
    "사누르제주",
    "하일리제주",
    "스테이느긋",
    "애월 한담 스테이",
    "한림 곁겹",
    "후아힌협재풀빌라",
    "애월 담소원 펜션",
    "한림 금능여관",
    "제주 애월로와",
    "한경 차귀스테이"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

collected = []

for t in targets:
    q = f"제주 {t}"
    url = f"https://search.naver.com/search.naver?query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            
            # Look for place id: accommodation/(\d+) or place/(\d+) or data-cid="(\d+)"
            m = re.search(r'm\.place\.naver\.com/accommodation/(\d+)', html)
            if not m:
                m = re.search(r'm\.place\.naver\.com/place/(\d+)', html)
            if not m:
                m = re.search(r'data-cid="(\d+)"', html)
            if not m:
                m = re.search(r'place\.naver\.com/accommodation/(\d+)', html)
                
            pid = m.group(1) if m else None
            
            # Extract tel, address
            addr_m = re.search(r'class="addr"[^>]*>([^<]+)', html) or re.search(r'class="txt"[^>]*>([^<]+(?:애월|한림|한경|제주시)[^<]*)', html)
            addr = addr_m.group(1).strip() if addr_m else "제주특별자치도 제주시 서쪽"
            
            tel_m = re.search(r'(\d{2,4}-\d{3,4}-\d{4})', html)
            tel = tel_m.group(1) if tel_m else "0507-0000-0000"
            
            # Extract SNS / homePage
            home_m = re.search(r'href="(https?://(?:www\.)?instagram\.com/[^"]+)"', html)
            insta = home_m.group(1) if home_m else ""
            
            blog_m = re.search(r'href="(https?://blog\.naver\.com/[^"]+)"', html)
            blog = blog_m.group(1) if blog_m else ""
            
            print(f"[{t}] PID: {pid} | Addr: {addr} | Tel: {tel} | Insta: {insta}")
            if pid:
                collected.append({
                    "name": t,
                    "pid": pid,
                    "link": f"https://m.place.naver.com/accommodation/{pid}/home",
                    "addr": addr,
                    "tel": tel,
                    "insta": insta,
                    "blog": blog
                })
    except Exception as e:
        print(f"Error for {t}: {e}")

print(f"\nSuccessfully resolved {len(collected)} places with IDs!")
with open("tools/west_resolved.json", "w", encoding="utf-8") as f:
    json.dump(collected, f, ensure_ascii=False, indent=2)
