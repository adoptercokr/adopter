import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
url = "https://api.github.com/repos/adoptercokr/adopter/actions/runs"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        runs = data.get('workflow_runs', [])
        print(f"Total runs: {len(runs)}")
        for r in runs[:5]:
            print(f"Name: {r.get('name')} | Status: {r.get('status')} | Conclusion: {r.get('conclusion')} | Created: {r.get('created_at')}")
except Exception as e:
    print("Error:", e)
