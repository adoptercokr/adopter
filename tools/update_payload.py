import json

with open('tools/new_10_rows_payload.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

for row in rows:
    if row[3] == '새록':
        row[4] = '260930-stay'
        row[5] = 'https://saerok.adopter.co.kr'
        print("Updated saerok in payload")

with open('tools/new_10_rows_payload.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
