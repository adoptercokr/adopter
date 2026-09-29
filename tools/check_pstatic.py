with open("tools/moheomdam_apollo.json", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'https?://[^\s",\']*(?:pstatic|naver)[^\s",\']*', text)
print(f"Total matching URLs: {len(matches)}")
unique = list(dict.fromkeys(matches))
print(f"Unique matching URLs: {len(unique)}")
for i, u in enumerate(unique[:30]):
    print(f"[{i+1}] {u}")
