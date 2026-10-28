import urllib.request
import json
import os

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

with open('tools/gangwon_10_deployed.json', 'r', encoding='utf-8') as f:
    deployed = json.load(f)

sheet_rows = []
for p in deployed:
    row = [
        "숙박업",
        p['naver_link'],
        "90%",
        p['name'],
        p['slug'],
        p['deploy_url'],
        "영업포트폴리오완료",
        f"네이버실사진{p['photos_count']}장",
        p['phone'],
        p['addr'],
        str(p['price']),
        "",
        "",
        "",
        "",
        "강원도실제발굴_네이버실사진_독채풀빌라"
    ]
    sheet_rows.append(row)

try:
    data = json.dumps(sheet_rows, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(APPS_SCRIPT_URL, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        result = resp.read().decode('utf-8')
        print("[SUCCESS] 구글 시트에 강원도 실제 10곳 전송 완료:", result)
except Exception as e:
    print("[ERROR] 구글 시트 전송 실패:", e)
