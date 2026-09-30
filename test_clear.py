import urllib.request
import json

app_url = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return urllib.request.Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})
opener = urllib.request.build_opener(RedirectHandler)

payload = json.dumps({"action": "clear"}).encode('utf-8')
req = urllib.request.Request(app_url, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})

try:
    with opener.open(req, timeout=10) as resp:
        print('Post Status:', resp.status)
        print('Response body:', resp.read().decode('utf-8'))
except Exception as e:
    print('Post error:', e)
