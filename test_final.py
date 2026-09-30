import re, json
html = open('test3.html', 'r', encoding='utf-8', errors='ignore').read()
m = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
if m:
    try:
        data = json.loads(m.group(1))
        print("Success! Keys:", list(data.keys())[:5])
    except Exception as e:
        print("Error:", e)
