import os
import subprocess

url = "https://m.place.naver.com/accommodation/2036409548/home"
# -o temp.html will let curl write directly to file
cmd = f"curl.exe -s -A \"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15\" -o temp2.html \"{url}\""
os.system(cmd)

with open("temp2.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>', text, re.DOTALL)
if state_match:
    print("Found! Length:", len(state_match.group(1)))
    print("Sample:", state_match.group(1)[:100])
else:
    print("Regex failed.")
