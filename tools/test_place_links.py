import urllib.request
import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

place_id = '1631444549' # 보아비양
url = f'https://m.place.naver.com/accommodation/{place_id}/home'

req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        
    print(f'HTML Length: {len(html)}')
    
    # 1. 앵커 태그 분석
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    print(f'Total anchors: {len(anchors)}')
    for href, text in anchors:
        text_clean = re.sub(r'<[^>]+>', '', text).strip()
        if '홈페이지' in text_clean or 'http' in href or 'instagram' in href:
            print(f'  [Anchor] text: {text_clean} | href: {href}')

    # 2. window.__APOLLO_STATE__
    state_match = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});</script>', html)
    if state_match:
        print('Found APOLLO_STATE!')
        state = json.loads(state_match.group(1))
        for k, v in state.items():
            if isinstance(v, dict):
                # check for url or homepage
                for key in ['homepage', 'homepages', 'homepageList', 'url', 'bookingUrl']:
                    if key in v and v[key]:
                        print(f'State key: {k} -> {key}: {v[key]}')
    else:
        print('APOLLO_STATE not matched directly. Checking other JSON...')
        json_scripts = re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html)
        print(f'Found {len(json_scripts)} application/json scripts')
        for i, js in enumerate(json_scripts):
            if 'voirvien' in js or 'http' in js:
                print(f'Script {i} contains keywords!')
except Exception as e:
    print('Error:', e)
