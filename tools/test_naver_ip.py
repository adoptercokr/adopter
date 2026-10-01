import urllib.request
req = urllib.request.Request('https://m.place.naver.com/accommodation/2036409548/home', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        if '과도한' in html:
            print("STILL BLOCKED BY NAVER")
        else:
            print("SUCCESS! Length:", len(html))
except Exception as e:
    print("Error:", e)
