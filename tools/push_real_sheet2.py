import urllib.request
import json
import urllib.parse
import os

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

properties = [
    {"id": "camino", "name": "까미노데플로레스타", "sns": "https://www.instagram.com/camino_de_floresta"},
    {"id": "dalnosi", "name": "달노시 스테이", "sns": "https://www.instagram.com/dalnosi_stay"},
    {"id": "chungchun", "name": "청춘연가", "sns": "https://www.instagram.com/chungchun_yeonga"},
    {"id": "handam", "name": "스테이 한담", "sns": "https://www.instagram.com/stay_handam"},
    {"id": "sanur", "name": "사누르제주", "sns": "https://www.instagram.com/sanur.jeju"},
    {"id": "negeut", "name": "스테이느긋", "sns": "https://www.instagram.com/stay__negeut"},
    {"id": "haru", "name": "하루를품다", "sns": "https://www.instagram.com/7another_day"},
    {"id": "gyeot", "name": "곁겹", "sns": "https://www.instagram.com/gyeotgyeop"},
    {"id": "plumeria", "name": "플루메리아 펜션", "sns": "http://www.instagram.com/plumeria_pension"},
    {"id": "solbeach", "name": "삼척 쏠비치", "sns": "https://www.instagram.com/solbeach_samcheok"} 
]

sheet_rows = []
for p in properties:
    row = [
        "숙박업",
        "", # naverLink
        "20%",
        p['name'],
        p['id'],
        f"https://adopter.co.kr/{p['id']}",
        "영업포트폴리오완료",
        "초고화질10장",
        "", # phone
        "강원도/제주도",
        "500000",
        p['sns'],
        "",
        "",
        "",
        "루트폴더적용완료"
    ]
    sheet_rows.append(row)

try:
    data = json.dumps(sheet_rows, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(APPS_SCRIPT_URL, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print("Pushed 10 real properties to Google Sheet:", resp.read().decode('utf-8'))
except Exception as e:
    print("Failed to push:", e)
