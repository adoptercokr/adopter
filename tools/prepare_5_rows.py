import json
import os

files = ['tools/west_10_collected.json', 'tools/west_batch2_collected.json']
data = []
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            data.extend(json.load(file))

targets = ['staypanpo', 'aewolrowa', 'mongdol', 'sanbangstay', 'siseon']

result = []
for item in data:
    if any(t in item.get('folder', '') for t in targets):
        row = [
            item.get('category', '숙박업'),
            item.get('naverLink', ''),
            '95%',
            item.get('title', item.get('name', '')),
            item.get('folder', ''),
            item.get('deployUrl', ''),
            '완료',
            '완료',
            item.get('phone', ''),
            item.get('addr', ''),
            item.get('price', ''),
            item.get('sns1', ''),
            item.get('sns2', ''),
            item.get('sns3', ''),
            item.get('homepage', ''),
            '🚨네이버 IP 차단으로 실제 사진 수집 불가. 임시 사진(모험담) 적용 완료. 추후 호스트에게 실제 사진 파일 받아 교체 필요'
        ]
        result.append(row)

with open('tools/5_fallback_rows.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Found {len(result)} items")
