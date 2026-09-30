with open('index.html', 'r', encoding='utf-8') as f: html = f.read()
import re
# Find the plan array in index.html
# monthly: 2000 -> monthly: 5000
# yearly: 1600 -> yearly: 4000

html = re.sub(r'(title:\s*[\'"]이벤트형[\'"],.*?monthly:\s*)2000', r'\g<1>5000', html, flags=re.DOTALL)
html = re.sub(r'(title:\s*[\'"]이벤트형[\'"],.*?yearly:\s*)1600', r'\g<1>4000', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
print("Updated pricing!")
