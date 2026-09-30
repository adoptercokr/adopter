import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

app_url = 'https://script.google.com/macros/s/AKfycbwesXD_ySLB1sE-hyY11UaXohKuyct4YIHF6mLLUrqSSfForgdtKm2lvJkm8MhiiHVSKQ/exec'

class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return urllib.request.Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})

opener = urllib.request.build_opener(RedirectHandler)

with open('tools/5_fallback_rows.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

payload = json.dumps(rows, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request(app_url, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})

try:
    with opener.open(req, timeout=15) as resp:
        print('Post Status:', resp.status)
        print('Response body:', resp.read().decode('utf-8'))
        print('✅ 구글 시트 전송 성공!')
except Exception as e:
    print('Post error:', e)
