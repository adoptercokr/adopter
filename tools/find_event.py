with open('index.html', 'r', encoding='utf-8') as f: html = f.read()

# "이벤트형" -> "5천원"
# Wait, let's find the exact text in index.html:
# "이벤트형 (월 유지비 0원)" or something?
import re
# Print context around 이벤트형
match = re.search(r'.{0,20}이벤트형.{0,20}', html)
if match: print("FOUND1:", match.group(0))

match2 = re.search(r'.{0,30}유지비.{0,30}', html)
if match2: print("FOUND2:", match2.group(0))
