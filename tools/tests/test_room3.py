import re
with open('temp_room.html', 'r', encoding='utf-8', errors='ignore') as f: html = f.read()
# find all window.__... objects
vars = re.findall(r'window\.__([A-Z_]+)__', html)
print('Variables:', set(vars))
