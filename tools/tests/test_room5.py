import re
with open('temp_room.html', 'r', encoding='utf-8', errors='ignore') as f: html = f.read()

# context around A동
m = re.search(r'.{0,50}A동.{0,50}', html)
if m: print(m.group(0))
