import os, re
targets = ['peaceofmind', 'cloudhouse', 'dalsoop', 'hijane', 'dumomansion', 'late-summer', 'seolchon', 'wolla', 'stay-2045570969']
for t in targets:
    p = os.path.join('Customer', f'260930-{t}', 'index.html')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f: html = f.read()
        html = re.sub(r'<style id="split-theme">.*?</style>', '', html, flags=re.DOTALL)
        html = html.replace('<div class="content-wrapper">\n    <!-- About Section -->', '    <!-- About Section -->')
        html = html.replace('</div>\n</body>', '</body>')
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
        print("Reverted split theme in", p)
