import re
import os

path = 'Customer/tpl-01-heestay/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

count = 1
def replacer(match):
    global count
    res = f"'./img/photo_{(count % 10) + 1}.jpg'"
    count += 1
    return res
def replacer_html(match):
    global count
    res = f'"./img/photo_{(count % 10) + 1}.jpg"'
    count += 1
    return res

html = re.sub(r"'\./img/.*?\.jpg'", replacer, html)
html = re.sub(r'"\./img/.*\.jpg"', replacer_html, html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
