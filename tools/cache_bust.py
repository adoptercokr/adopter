import os, re

# We will increment the ?v= version in ALL Customer/*/index.html files
for d in os.listdir('Customer'):
    p = os.path.join('Customer', d, 'index.html')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f: html = f.read()
        
        # Replace stay_config.js or stay_config.js?v=... with stay_config.js?v=4
        html = re.sub(r'stay_config\.js(\?v=\d+)?', 'stay_config.js?v=4', html)
        
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
