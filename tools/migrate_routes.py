import os
import glob
import shutil

adopter_dir = r'c:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter'
customer_dir = os.path.join(adopter_dir, 'Customer')

# 1. Identify all folders in Customer to know the mapping
routes = {}
for name in os.listdir(customer_dir):
    if name.startswith('260930-'):
        parts = name.split('-')
        if len(parts) >= 3:
            slug = parts[1]
            # new root folder name
            new_folder = f"260930-{slug}"
            routes[slug] = new_folder
            
            # If old root folder exists, rename it
            old_path = os.path.join(adopter_dir, slug)
            new_path = os.path.join(adopter_dir, new_folder)
            if os.path.isdir(old_path):
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f"Renamed {slug} to {new_folder}")
                else:
                    # If it already exists, just remove the old one or merge
                    shutil.rmtree(old_path)
                    print(f"Deleted old {slug}, {new_folder} already exists")

# Write route_map.js
route_map_code = "export const routeMap = " + str(routes) + ";\n"
with open(os.path.join(adopter_dir, 'functions', 'route_map.js'), 'w', encoding='utf-8') as f:
    f.write(route_map_code)

print("Generated route_map.js")
