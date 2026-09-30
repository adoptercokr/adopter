import json
with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for item in data:
    if '산방' in item.get('title', item.get('name', '')):
        print(item)
