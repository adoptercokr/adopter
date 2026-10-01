import os
import re

path = 'Customer/tpl-01-heestay/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('모험담', '제주 희스테이')
html = html.replace('MOHEOMDAM', 'HEESTAY')
html = html.replace('moheomdam', 'heestay')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
