import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

import os

account_id = os.environ.get('CLOUDFLARE_ACCOUNT_ID', '4edd9e53c7f24979c30d48c7133b4170')
token = os.environ.get('CLOUDFLARE_API_TOKEN', '')
project_name = 'adopter'

url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}/domains'

# Get existing domains
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
try:
    with urllib.request.urlopen(req) as resp:
        existing = [d.get('name') for d in json.loads(resp.read().decode('utf-8')).get('result', [])]
except Exception as e:
    existing = []

print(f'Already registered in Cloudflare Pages ({len(existing)}):', existing)

subdomains = [
    'sanur', 'haily', 'negeut', 'aewolrowa', 'gyeotgyeop', 'huahin',
    'geumneung', 'handam', 'plumeria', 'mongdol', 'lacour', 'monogarden',
    'boabiyang', 'stay1m', 'lalapipo', 'daejeong', 'staypanpo', 'sanbangstay',
    'sinchang', 'cloudhouse', 'dalsoop', 'dumomansion', 'hijane',
    'late-summer', 'peaceofmind', 'seolchon', 'stay-2045570969', 'wolla'
]

for sub in subdomains:
    full_domain = f'{sub}.adopter.co.kr'
    if full_domain in existing:
        print(f'-> {full_domain} already registered. Skipping.')
        continue

    payload = json.dumps({'name': full_domain}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get('success'):
                print(f'✅ Successfully registered: {full_domain}')
            else:
                print(f'❌ Failed {full_domain}: {data.get("errors")}')
    except Exception as e:
        print(f'Error registering {full_domain}: {e}')
    time.sleep(0.3)

print('All subdomains registered to Cloudflare Pages!')
