import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
pid = '1716272359'
url = f'https://m.place.naver.com/accommodation/{pid}/home'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')

matches = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png)', html)
print('Found image urls:', len(matches))
for m in list(set(matches))[:10]:
    print(' ', m)

# Also check for pstatic or naver image domains without extension
pstatic = re.findall(r'https?://(?:ldb-phinf|search\.pstatic|naverbooking-phinf)[^\s"\'<>]+', html)
print('Found pstatic matches:', len(pstatic))
for p in list(set(pstatic))[:10]:
    print('  pstatic:', p)
