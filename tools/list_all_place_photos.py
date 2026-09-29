import json
import re

with open("tools/moheomdam_apollo.json", "r", encoding="utf-8") as f:
    text = f.read()

# Match all pstatic URLs
urls = re.findall(r'https://[a-zA-Z0-9_\-\./]+(?:ldb-phinf|naverbooking-phinf|blogpfthumb-phinf)\.pstatic\.net/[a-zA-Z0-9_\-\./]+(?:\.jpg|\.png|\.jpeg)', text)
urls = list(dict.fromkeys(urls))
print(f"Total unique photos: {len(urls)}")
for i, u in enumerate(urls):
    print(f"[{i+1}] {u}")

with open("tools/all_apollo_photos.json", "w", encoding="utf-8") as f:
    json.dump(urls, f, indent=2)
