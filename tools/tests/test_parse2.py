import re
with open('temp.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'<meta[^>]*description[^>]*content="([^"]+)"', html, re.I)
if m: print('DESC1:', m.group(1))

m2 = re.search(r'property="og:description"[^>]*content="([^"]+)"', html, re.I)
if m2: print('DESC2:', m2.group(1))

text_blocks = re.findall(r'"text":"([^"]+)"', html)
long_texts = [t for t in text_blocks if len(t) > 20 and any('\uAC00' <= c <= '\uD7A3' for c in t)]
for t in set(long_texts):
    print('TEXT:', t[:100])
