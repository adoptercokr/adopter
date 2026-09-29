import json
import os
import re

with open('tools/moheomdam_apollo.json', 'r', encoding='utf-8') as f:
    state = json.load(f)

extracted_rooms = []

def search_rooms(obj):
    if isinstance(obj, dict):
        if 'resocName' in obj:
            extracted_rooms.append(obj)
        for v in obj.values():
            search_rooms(v)
    elif isinstance(obj, list):
        for item in obj:
            search_rooms(item)

search_rooms(state)

print(f"Extracted {len(extracted_rooms)} room objects.")
output_data = []
for r in extracted_rooms:
    name = r.get('resocName')
    desc = r.get('resocDesc')
    base_g = r.get('cond2Val')
    max_g = r.get('cond3Val')
    sub_images = r.get('subImage', [])
    images = [img for img in sub_images if isinstance(img, str)]
    
    # Also check if there are other image fields
    print(f"\n[객실명: {name}]")
    print(f"  기준인원: {base_g}인 / 최대인원: {max_g}인")
    print(f"  설명: {desc}")
    print(f"  사진 수: {len(images)}")
    for i, img in enumerate(images[:5]):
        print(f"    - img {i+1}: {img}")
    
    output_data.append({
        "name": name,
        "desc": desc,
        "baseGuests": base_g,
        "maxGuests": max_g,
        "images": images,
        "raw": r
    })

with open('tools/extracted_moheomdam_rooms.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("\nSaved to tools/extracted_moheomdam_rooms.json")
