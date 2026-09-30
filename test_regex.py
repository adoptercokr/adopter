import os
import re

url = "https://m.place.naver.com/accommodation/2036409548/home"
cmd = f"curl.exe -s -A \"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15\" -o test3.html \"{url}\""
os.system(cmd)

with open("test3.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Try multiple regex patterns to see what matches
patterns = [
    r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>',
    r'__APOLLO_STATE__\s*=\s*(\{.*?\})\s*<\/script>',
    r'__APOLLO_STATE__=(.*?)</script>',
    r'window\.__APOLLO_STATE__\s*=\s*(\{.*?\})'
]

for p in patterns:
    m = re.search(p, text, re.DOTALL)
    if m:
        print(f"MATCHED: {p}")
        print("Length:", len(m.group(1)))
        break
else:
    print("ALL PATTERNS FAILED")
