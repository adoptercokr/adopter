import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
with open('temp.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

desc_match = re.search(r'property="og:description"\s*content="([^"]+)"', html)
print('OG DESC:', desc_match.group(1) if desc_match else 'None')

state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*window\.__', html, re.DOTALL)
if state_match:
    state = json.loads(state_match.group(1))
    
    facs = set()
    for k in state.keys():
        if k.startswith('InformationFacilities:'):
            parts = k.split(':')
            if len(parts) > 1: facs.add(parts[1].split()[0])
    print('Facilities:', list(facs))
    
    candidates = []
    def find_text(obj):
        if isinstance(obj, dict):
            for v in obj.values(): find_text(v)
        elif isinstance(obj, list):
            for v in obj: find_text(v)
        elif isinstance(obj, str):
            if len(obj) > 30 and ('독채' in obj or '풀빌라' in obj or '펜션' in obj or '제주' in obj):
                candidates.append(obj)
    find_text(state)
    if candidates:
        print('Best Desc:', sorted(candidates, key=len, reverse=True)[0][:200].replace('\n', ' '))
