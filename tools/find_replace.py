with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Find something like: 월 유지비 0원 or 월유지비 무료
match = re.search(r'월\s*유지비\s*[0-9]+원|월\s*유지비\s*무료', html)
if match:
    print("MATCH:", match.group(0))
    html = html.replace(match.group(0), '월 유지비 5천원')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Replaced!")
else:
    # Just look for '무료' near '유지비'
    match2 = re.search(r'.{0,10}유지비.{0,10}', html)
    if match2:
        print("NEAR:", match2.group(0))
