import re

with open(r'templates\01-stay\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find calendar and admin related scripts
print('Calendar in HTML:', 'id="calendar"' in html)
print('Admin functions in HTML:')
for m in re.finditer(r'function\s+([a-zA-Z0-9_]+)\s*\([^)]*\)\s*\{', html):
    name = m.group(1)
    if any(k in name.lower() for k in ['cal', 'calc', 'admin', 'date', 'price', 'book', 'toggle']):
        print('  -', name)

# Search for admin modal or password check
admin_blocks = re.findall(r'<div[^>]+id="admin[^>]*>.*?</div>', html, re.DOTALL)
print('Admin blocks found:', len(admin_blocks))
