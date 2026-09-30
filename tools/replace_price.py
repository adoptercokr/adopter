with open('index.html', 'r', encoding='utf-8') as f: html = f.read()

# Replace any occurrence of '월유지비 무료' or '월유지비 0원' with '5천원'
html = html.replace('월유지비 0원', '월유지비 5천원')
html = html.replace('월 유지비 0원', '월 유지비 5천원')
html = html.replace('유지비 무료', '유지비 5천원')
html = html.replace('유지비 무상', '유지비 5천원')
html = html.replace('이벤트형 (무료)', '이벤트형 (5천원)')

with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
print("Replaced!")
