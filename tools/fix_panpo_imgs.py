with open('Customer/260930-staypanpo/stay_config.js', 'r', encoding='utf-8') as f: js = f.read()
import re
js = re.sub(r'https://ldb-phinf[^"\']+', lambda m: f'./img/photo_{min(5, int(m.group(0)[-5]) if m.group(0)[-5].isdigit() else 1)}.jpg', js)

with open('Customer/260930-staypanpo/stay_config.js', 'w', encoding='utf-8') as f: f.write(js)
