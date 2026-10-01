import urllib.request
import urllib.parse
import json
import re

query = urllib.parse.quote('까미노데플로레스타')
url = f'https://www.yeogi.com/api/v1/search/domestic/accommodations?keyword={query}&personal=2'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    print(data)
except Exception as e:
    print(e)
