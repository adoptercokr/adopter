with open('index.html', 'r', encoding='utf-8') as f:
    for line in f:
        if 'portfolio.html' in line or 'faq.html' in line or '이벤트형' in line or '5천원' in line or '유지비' in line:
            print(line.strip())
