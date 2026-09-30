import urllib.request
import sys

def get_title(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            start = html.find('<title>')
            end = html.find('</title>')
            if start != -1 and end != -1:
                return html[start+7:end]
            return "No title tag"
    except Exception as e:
        return f"Error: {e}"

print("Root URL:", get_title('https://aewolrowa.adopter.co.kr/'))
print("Sub URL:", get_title('https://aewolrowa.adopter.co.kr/aewolrowa/'))
