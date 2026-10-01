import json
with open('tools/verified_strictly_no_homepage.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for d in data[:5]:
    print(d['name'], d['instagram'])
