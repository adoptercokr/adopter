import os
import json
import re
import shutil
import urllib.request
import time
from google import genai

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADOPTER_DIR = os.path.dirname(CURRENT_DIR)
TEMPLATE_DIR = os.path.join(ADOPTER_DIR, "templates", "01-stay")
CUSTOMER_DIR = os.path.join(ADOPTER_DIR, "Customer")

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def fetch_apollo_state(pid):
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            state_match = re.search(r'__APOLLO_STATE__\s*=\s*(\{.*?\});\s*<\/script>', html, re.DOTALL)
            if state_match:
                return json.loads(state_match.group(1))
    except Exception as e:
        print(f"Error fetching {pid}: {e}")
    return None

def fetch_photos(pid):
    photo_urls = []
    for tab in ["home", "photo"]:
        url = f"https://m.place.naver.com/accommodation/{pid}/{tab}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                src_matches = re.findall(r'src=(https%3A%2F%2F[^\s"\'&]+)', html)
                for sm in src_matches:
                    unquoted = urllib.parse.unquote(sm)
                    if any(domain in unquoted for domain in ['ldb-phinf', 'naverbooking-phinf', 'pup-review-phinf', 'blogfiles']):
                        if not any(ex in unquoted.lower() for ex in ['profile', 'icon', 'favicon', 'banner', 'logo']):
                            if unquoted not in photo_urls:
                                photo_urls.append(unquoted)
        except: pass
        if len(photo_urls) >= 12: break
    return photo_urls[:10]

def build_stay(item):
    slug = item.get('folder', '').split('-')[-1]
    pid_match = re.search(r'/accommodation/(\d+)', item.get('naverLink', ''))
    if not pid_match or not slug: return False
    pid = pid_match.group(1)
    
    clean_name = item.get('name', slug).replace('제주', '').replace(' ', '')
    print(f"\n=> Building {slug} (PID: {pid})...")
    
    raw_data = fetch_apollo_state(pid)
    if not raw_data:
        print("Failed to fetch raw data")
        return False
        
    dest_dir = os.path.join(CUSTOMER_DIR, f"260930-{slug}")
    img_dir = os.path.join(dest_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    
    photos = fetch_photos(pid)
    for i, p_url in enumerate(photos, 1):
        target_file = os.path.join(img_dir, f"photo_{i}.jpg")
        try:
            req = urllib.request.Request(p_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                with open(target_file, "wb") as f_out:
                    f_out.write(resp.read())
        except: pass

    # Clean the raw data to save tokens
    clean_raw = str(raw_data)[:12000]
    
    prompt = f'''
You are an AI generating a `stay_config.js` for a high-end, luxury stay website.
I will give you a JSON string containing the Naver Place raw data for this stay.
Extract the brand name, description, exact facilities, exact rooms/spaces (and their features), notices, and pricing.
Return ONLY valid JavaScript code defining `const STAY_CONFIG = {{...}};`. Do not use markdown backticks.

Use this exact schema (fill in extracted values, replace my examples):
const STAY_CONFIG = {{
  name: "{clean_name}",
  subtitle: "Jeju Private Poolvilla",
  description: "Extracted description or tagline from raw data",
  benefits: [
    {{ id: "b1", icon: "<svg viewBox=\\"0 0 24 24\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" class=\\"w-6 h-6\\"><path stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" d=\\"M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3\\"></path></svg>", title: "Title", description: "Desc", detail: "Detail" }}
  ],
  spaces: [
    {{ id: "s1", title: "Space 1", subtitle: "Desc", mainImage: "./img/photo_1.jpg", images: ["./img/photo_1.jpg"], totalPhotos: 1 }}
  ],
  facilities: [
    {{ name: "Facility 1", icon: "svg-icon-name" }}
  ],
  rules: [
    "Check-in 15:00", "No smoking"
  ],
  rates: {{
    weekday: "Extracted weekday price",
    weekend: "Extracted weekend price",
    peak: "Extracted peak price"
  }}
}};

Raw Data Snippet:
{clean_raw}
'''

    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        
        js_code = response.text
        if '```' in js_code:
            js_code = js_code.split('```javascript')[-1].split('```')[0].strip()
        
        with open(os.path.join(dest_dir, "stay_config.js"), "w", encoding="utf-8") as f:
            f.write(js_code)
            
        # Copy template files
        files_to_copy = ["index.html", ".gitignore", "robots.txt", "sitemap.xml"]
        for f in files_to_copy:
            src = os.path.join(TEMPLATE_DIR, f)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(dest_dir, f))
        print(f"Successfully built {slug}!")
        return True
    except Exception as e:
        print("Gemini error:", e)
        return False
    return False

def main():
    with open(os.path.join(ADOPTER_DIR, 'tools', 'west_10_collected.json'), 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    
    # We will just do the first item to test
    for item in data1[:1]:
        build_stay(item)
    
    print("Test run complete.")

if __name__ == "__main__":
    main()
