import urllib.request
import urllib.parse
import re
import json

targets = [
    "사누르제주",
    "하일리제주",
    "스테이느긋",
    "애월로와 키즈풀빌라",
    "한림 곁겹 풀빌라",
    "후아힌협재풀빌라",
    "애월 담소원 펜션",
    "한림 금능여관",
    "한경 차귀스테이",
    "애월 한담 스테이"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

resolved = []

for t in targets:
    url = f"https://search.naver.com/search.naver?query={urllib.parse.quote('제주 ' + t)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            m = re.search(r'place/(\d+)', html)
            if not m:
                m = re.search(r'accommodation/(\d+)', html)
            
            if m:
                pid = m.group(1)
                resolved.append({"name": t, "pid": pid})
                print(f"[FOUND] {t} -> Place ID: {pid}")
            else:
                print(f"[NOT FOUND] {t}")
    except Exception as e:
        print(f"Error {t}: {e}")

print("\nResolved count:", len(resolved))
with open("tools/resolved_10.json", "w", encoding="utf-8") as f:
    json.dump(resolved, f, ensure_ascii=False, indent=2)
