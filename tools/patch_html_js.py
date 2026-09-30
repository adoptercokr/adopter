import os
with open('templates/01-stay/index.html', 'r', encoding='utf-8') as f: html = f.read()
with open('tools/script_extracted_dynamic.js', 'r', encoding='utf-8') as f: js = f.read()

# Insert before </body>
html = html.replace('</body>', '<script>\n' + js + '\n</script>\n</body>')

with open('templates/01-stay/index.html', 'w', encoding='utf-8') as f: f.write(html)

for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    tp = os.path.join('Customer', d, 'index.html')
    if os.path.exists(tp):
        with open(tp, 'w', encoding='utf-8') as f: f.write(html)
