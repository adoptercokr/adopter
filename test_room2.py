import re
with open('temp_room.html', 'r', encoding='utf-8', errors='ignore') as f: html = f.read()

# Let's search for some typical korean room names like "A동", "B동"
print('A동 in html?', 'A동' in html)
print('B동 in html?', 'B동' in html)

# Let's check for "price" in the raw html
prices = re.findall(r'price', html)
print('price count:', len(prices))
