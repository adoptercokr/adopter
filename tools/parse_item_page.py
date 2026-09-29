import re
import json

with open("tools/item_6123393.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find JSON in script tags
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Total scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    if "window.__APOLLO_STATE__" in s:
        print(f"Script {i} has APOLLO_STATE! Length: {len(s)}")
        idx = s.find("=")
        data = json.loads(s[idx+1:].strip())
        with open("tools/item_apollo.json", "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        print("Saved tools/item_apollo.json")
        for k, v in data.items():
            if isinstance(v, dict):
                typename = v.get("__typename")
                name = v.get("name") or v.get("resocName") or v.get("itemName")
                if name or "Item" in str(typename) or "Biz" in str(typename):
                    print(f"  {k} -> {typename} | name: {name}")
