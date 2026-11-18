import os
customer_dir = r"C:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter\Customer"
for d in os.listdir(customer_dir):
    p = os.path.join(customer_dir, d, "stay_config.js")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        # The garbled text was caused by PowerShell string. Let's replace the common garbled strings with correct Korean!
        content = content.replace('ӹ,  ü   Ǵ ', '머묾, 그 자체가 온전한 쉼이 되는 공간')
        content = content.replace('?라?빗 공간', '프라이빗 공간')
        content = content.replace('?직 ???만을 ?한 ?벽???라?빗 ?테?', '오직 한 팀만을 위한 완벽한 프라이빗 스테이')
        content = content.replace('조용?고 ?늑???식', '조용하고 아늑한 휴식')
        content = content.replace('?리미엄 ?메?티', '프리미엄 어메니티')
        content = content.replace('최고??텔 ?????메?티 ?공', '최고급 호텔 수준의 어메니티 제공')
        content = content.replace('친환??품 ?용', '친환경 제품 사용')
        content = content.replace('?식 공간', '휴식 공간')
        content = content.replace('무선 ?터?', '무선 인터넷')
        content = content.replace('주차?', '주차장')
        content = content.replace('체크??15:00 / 체크?웃 11:00', '체크인 15:00 / 체크아웃 11:00')
        content = content.replace('?내 ?? 금연', '실내 절대 금연')
        content = content.replace('반려?물 ?반 불?', '반려동물 동반 불가')
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
