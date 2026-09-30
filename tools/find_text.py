with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if '제작' in line or '질문' in line or '이벤트형' in line or '유지비' in line:
        print(f"{i}: {line.strip()}")
