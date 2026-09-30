with open('index.html', 'r', encoding='utf-8') as f: lines = f.readlines()

for i, line in enumerate(lines):
    if '이벤트형' in line or '유지비' in line:
        if '0원' in line or '무료' in line:
            lines[i] = line.replace('0원', '5천원').replace('무료', '5천원')
            print(f"Replaced in line {i}:", lines[i].strip())

with open('index.html', 'w', encoding='utf-8') as f: f.writelines(lines)
