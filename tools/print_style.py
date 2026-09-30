with open('Customer/260930-moheomdam/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if match:
    print(match.group(1))
