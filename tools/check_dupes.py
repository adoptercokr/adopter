import json
with open('tools/west_10_collected.json', 'r', encoding='utf-8') as f:
    d1 = json.load(f)
with open('tools/west_batch2_collected.json', 'r', encoding='utf-8') as f:
    d2 = json.load(f)
names1 = [d['name'] for d in d1]
names2 = [d['name'] for d in d2]
print("batch 1:", names1)
print("batch 2:", names2)
