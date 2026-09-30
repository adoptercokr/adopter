import re, os
with open('templates/01-stay/index.html', 'r', encoding='utf-8') as f: html = f.read()

# Remove the simple calendar JS completely
html = re.sub(r'// Rates & Calendar Logic.*?// Observers', '// Observers', html, flags=re.DOTALL)

with open('templates/01-stay/index.html', 'w', encoding='utf-8') as f: f.write(html)

for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    tp = os.path.join('Customer', d, 'index.html')
    if os.path.exists(tp):
        with open(tp, 'w', encoding='utf-8') as f: f.write(html)
