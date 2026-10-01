import json
with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for d in data:
    print(d['name'], d.get('sns1'))
