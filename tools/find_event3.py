with open('index.html', 'r', encoding='utf-8') as f:
    for line in f:
        if '이벤트형' in line:
            print("EVENT:", line.strip())
