import os
import re
import json
import glob

# Read the template
template_path = r'c:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter\templates\01-stay\index.html'
with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all images ending in .jpg
img_paths = re.findall(r'(\./img/[^"\']+\.jpg|/img/[^"\']+\.jpg|img/[^"\']+\.jpg)', html)
unique_imgs = list(set(img_paths))
print(f"Found {len(unique_imgs)} unique image paths in template.")
