import re, os
with open('templates/01-stay/index.html', 'r', encoding='utf-8') as f: html = f.read()
with open('tools/cal_extracted.html', 'r', encoding='utf-8') as f: cal_html = f.read()

# Replace Reservation section with cal_html
html = re.sub(r'<section id="reservation".*?</section>', cal_html, html, flags=re.DOTALL)

with open('templates/01-stay/index.html', 'w', encoding='utf-8') as f: f.write(html)
