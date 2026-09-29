import json
import re

with open("tools/moheomdam_apollo.json", "r", encoding="utf-8") as f:
    text = f.read()

# Look for all 7-digit item IDs near 6123393
item_ids = set(re.findall(r'612\d{4}', text))
print("Nearby item IDs in moheomdam_apollo:", item_ids)

# Look for '모험' in the file
for m in re.finditer(r'([^\"]*모험[^\"]*)', text):
    val = m.group(1)
    if len(val) < 80:
        print("  Text with 모험:", val)
