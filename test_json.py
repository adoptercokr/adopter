import os, re, json
with open("test3.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

m = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\})\s*<\/script>', text, re.DOTALL)
if m:
    try:
        data = json.loads(m.group(1))
        print("JSON parse success!")
    except Exception as e:
        print("JSON Error:", e)
