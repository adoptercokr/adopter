import json, os, re

def fix_images():
    for d in os.listdir('Customer'):
        if not d.startswith('260930-'): continue
        p = os.path.join('Customer', d, 'stay_config.js')
        if not os.path.exists(p): continue
        
        with open(p, 'r', encoding='utf-8') as f:
            js = f.read()
            
        # extract all images
        lines = js.split('\n')
        new_lines = []
        for line in lines:
            if 'mainImage' in line:
                if 'pup-review' in line or 'tvcast' in line or 'clip-service' in line:
                    continue # skip weird photos
                if 'f84_sharpen' in line: # small thumbnails
                    line = line.replace('f84_sharpen', 'w800_800')
                if 'w560_sharpen' in line:
                    line = line.replace('w560_sharpen', 'w800_800')
            new_lines.append(line)
            
        with open(p, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"Fixed {d}")
        
fix_images()
