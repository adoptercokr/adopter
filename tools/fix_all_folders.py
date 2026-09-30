import os, json

customer_dir = 'Customer'
# Read route map to know exact folder names
with open('functions/_route_map.js', 'r', encoding='utf-8') as f:
    js = f.read()
import re
match = re.search(r'export const routeMap = (\{.*?\});', js)
if not match: exit()

route_map = json.loads(match.group(1).replace("'", '"'))

# We want the folders to EXACTLY match the values in routeMap
# (e.g. "260930-handam")

for sub, exact_name in route_map.items():
    exact_path = os.path.join(customer_dir, exact_name)
    if not os.path.exists(exact_path):
        # find the folder with suffix
        for d in os.listdir(customer_dir):
            if d.startswith(exact_name + '-'):
                os.rename(os.path.join(customer_dir, d), exact_path)
                print(f"Renamed {d} to {exact_name}")
                break
