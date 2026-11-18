import os
import re

path = r'c:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter\tools\search_and_produce_more.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = r'''# 1. 템플릿 복사 및 HTML 내부 텍스트/이미지 경로 치환
    files_to_copy = [".gitignore", "robots.txt", "sitemap.xml"]
    for f in files_to_copy:
        src = os.path.join(TEMPLATE_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_dir, f))
            shutil.copy2(src, os.path.join(root_slug_dir, f))

    # index.html 치환
    index_src = os.path.join(TEMPLATE_DIR, "index.html")
    if os.path.exists(index_src):
        with open(index_src, "r", encoding="utf-8") as f:
            html_content = f.read()

        # 텍스트 치환
        html_content = html_content.replace("희스테이", clean_name)
        html_content = html_content.replace("HEESTAY", slug.upper())
        html_content = html_content.replace("jejuheestay.co.kr", f"{slug}.adopter.co.kr")
        
        # 이미지 경로 치환 (photo_1.jpg ~ photo_10.jpg 반복)
        import urllib.parse
        img_paths = re.findall(r'(\./img/[^"\'\s]+\.jpg|/img/[^"\'\s]+\.jpg|img/[^"\'\s]+\.jpg)', html_content)
        unique_imgs = list(set(img_paths))
        for idx, old_img in enumerate(unique_imgs):
            new_img = old_img.replace(old_img.split('/')[-1], f"photo_{(idx % 10) + 1}.jpg")
            html_content = html_content.replace(old_img, new_img)
            # URL 인코딩된 경로도 치환
            encoded_old = urllib.parse.quote(old_img)
            if "%" in encoded_old:
                encoded_new = urllib.parse.quote(new_img)
                html_content = html_content.replace(encoded_old, encoded_new)
                
        with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(os.path.join(root_slug_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
'''

# Find the block to replace
start_idx = content.find('files_to_copy = [')
end_idx = content.find('photos = fetch_photos', start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx - 4] + replacement + '\n    ' + content[end_idx:]
    
    # Also patch root_slug_dir logic
    new_content = new_content.replace(
        'root_slug_dir = os.path.join(ADOPTER_DIR, slug)',
        'root_slug_dir = os.path.join(ADOPTER_DIR, f"{today_prefix}-{slug}")'
    )
    
    # And inject route_map logic at the end of build_stay_website
    inject_code = """
    # Update route_map.js
    route_map_path = os.path.join(ADOPTER_DIR, 'functions', 'route_map.js')
    if os.path.exists(route_map_path):
        with open(route_map_path, 'r', encoding='utf-8') as f:
            rm_text = f.read()
        import ast
        try:
            dict_str = rm_text.split('=', 1)[1].strip().rstrip(';')
            route_map = ast.literal_eval(dict_str)
        except:
            route_map = {}
    else:
        route_map = {}
        
    route_map[slug] = f"{today_prefix}-{slug}"
    with open(route_map_path, 'w', encoding='utf-8') as f:
        f.write(f"export const routeMap = {repr(route_map)};\\n")
"""
    new_content = new_content.replace(
        '    return {\n        "slug": slug,',
        inject_code + '\n    return {\n        "slug": slug,'
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patch applied to search script.")
else:
    print("Could not find blocks")
