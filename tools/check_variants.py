import os, json
customer_dir = 'Customer'
variants = {}
for d in os.listdir(customer_dir):
    if not d.startswith('260930-'): continue
    p = os.path.join(customer_dir, d, 'stay_config.js')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            for line in f:
                if 'variant:' in line:
                    v = line.split(':')[1].strip().strip(',')
                    if v not in variants:
                        variants[v] = d
                    break
print("Found variants:")
for v, d in variants.items():
    print(f"Variant {v}: {d.replace('260930-', '')}.adopter.co.kr")
