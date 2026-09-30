import os
import re
import json

path = r'c:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter\tools\autonomous_all_stays_producer.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace root_slug_dir = os.path.join(ADOPTER_DIR, slug)
# with root_slug_dir = os.path.join(ADOPTER_DIR, f"{today_prefix}-{slug}")
content = content.replace(
    'root_slug_dir = os.path.join(ADOPTER_DIR, slug)',
    'root_slug_dir = os.path.join(ADOPTER_DIR, f"{today_prefix}-{slug}")'
)

# And append updating route_map.js inside push_to_google_sheet or end of build_stay_website
# We can do it at the end of build_stay_website.
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

# Find return { at the end of build_stay_website
content = content.replace(
    '    return {\n        "slug": slug,',
    inject_code + '\n    return {\n        "slug": slug,'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched producer for route_map")
