import urllib.request
import json
import urllib.parse
import sys
sys.stdout.reconfigure(encoding='utf-8')

app_url = 'https://script.google.com/macros/s/AKfycby_Gy2SSKIZk0KDz2Jh9vMLL7JV2gtfGyaYMge6Spj9ldhIXJRtAl186V7WPNO7mQILNQ/exec'

class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return urllib.request.Request(newurl, headers={'User-Agent': 'Mozilla/5.0'})
opener = urllib.request.build_opener(RedirectHandler)

# 1. Fetch current data
print("Fetching current data...")
req = urllib.request.Request(app_url)
try:
    with opener.open(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"Loaded {len(data)} rows.")
except Exception as e:
    print(f"Failed to fetch data: {e}")
    sys.exit(1)

# 2. Deduplicate
unique_rows = []
seen_slugs = set()
for row in data:
    slug = row.get('subdomain', '').strip()
    if not slug:
        slug = row.get('name', '').strip()
    if slug and slug not in seen_slugs:
        seen_slugs.add(slug)
        unique_rows.append(row)

print(f"Found {len(unique_rows)} unique rows out of {len(data)}.")

# 3. Post to overwrite? The App Script probably appends.
# We will just post an action 'clear_and_replace' if supported, else we can't do it via API without knowing the App Script.
# Let's see if we can do something. I'll just print out the deduplicated list for now.
