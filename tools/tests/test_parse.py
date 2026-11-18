import re, json
with open('temp.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

meta_desc = re.search(r'<meta property="og:description" content="(.*?)"', html)
if meta_desc:
    print('OG DESC:', meta_desc.group(1))

# Also let's extract raw text blocks
text_blocks = re.findall(r'"text":"([^"]+)"', html)
# filter for long Korean text
long_texts = [t for t in text_blocks if len(t) > 20 and any('\uAC00' <= c <= '\uD7A3' for c in t)]
for t in long_texts[:5]:
    print('TEXT:', t)
