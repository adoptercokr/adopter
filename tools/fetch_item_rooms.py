import urllib.request
import re
import json

found_items = []

for item_id in range(6123380, 6123410):
    url = f"https://m.booking.naver.com/booking/3/bizes/1199277/items/{item_id}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
            "Accept-Language": "ko-KR,ko;q=0.9"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r"<title>(.*?)</title>", html)
            title = m.group(1) if m else "No title"
            
            # Check for item name
            name_m = re.search(r'"name":"([^"]+모험[^"]*)"', html)
            item_name = name_m.group(1) if name_m else title
            
            # Images
            imgs = list(dict.fromkeys(re.findall(r'https://naverbooking-phinf\.pstatic\.net/[a-zA-Z0-9_/]+(?:\.jpg|\.png|\.jpeg)', html)))
            
            print(f"ID {item_id}: {item_name} | {len(imgs)} imgs")
            found_items.append({
                "id": item_id,
                "name": item_name,
                "title": title,
                "images": imgs,
                "html_len": len(html)
            })
            with open(f"tools/item_{item_id}.html", "w", encoding="utf-8") as f:
                f.write(html)
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"ID {item_id}: HTTP {e.code}")
    except Exception as e:
        pass

with open("tools/found_items.json", "w", encoding="utf-8") as f:
    json.dump(found_items, f, ensure_ascii=False, indent=2)

print(f"Found {len(found_items)} items total.")
