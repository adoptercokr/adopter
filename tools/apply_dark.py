import os
import shutil
import re

targets = ['peaceofmind', 'cloudhouse', 'dalsoop', 'hijane', 'dumomansion', 'late-summer', 'seolchon', 'wolla', 'stay-2045570969']

customer_dir = 'Customer'
# 1. Rename folders to match target exact names if they have suffixes
for t in targets:
    exact_name = f"260930-{t}"
    exact_path = os.path.join(customer_dir, exact_name)
    
    # if exact doesn't exist, find the one with suffix
    if not os.path.exists(exact_path):
        for d in os.listdir(customer_dir):
            if d.startswith(exact_name + '-'):
                os.rename(os.path.join(customer_dir, d), exact_path)
                print(f"Renamed {d} to {exact_name}")
                break

# 2. Inject Dark Theme CSS
dark_css = '''
<style id="dark-theme">
    /* Dark Luxury Theme Overrides */
    body { background-color: #0a0a0a !important; color: #f0f0f0 !important; }
    .bg-white { background-color: #141414 !important; border-color: #333 !important; }
    .text-brand-dark { color: #f0f0f0 !important; }
    .text-brand-wood { color: #D4AF37 !important; } /* Gold */
    .bg-brand-cream { background-color: #1a1a1a !important; }
    .bg-brand-wood { background-color: #D4AF37 !important; color: #000 !important; }
    header.bg-white { background-color: rgba(10,10,10,0.9) !important; border-bottom: 1px solid #333 !important; }
    .border-brand-border { border-color: #333 !important; }
    .cal-day { color: #f0f0f0; }
    .cal-day.range { background-color: #2a2a2a !important; color: #fff !important; }
    .cal-day:hover:not(.disabled):not(.booked) { background-color: #D4AF37 !important; color: #000 !important; }
    .cal-day.selected { background-color: #D4AF37 !important; color: #000 !important; }
    .calendar-container { background-color: #141414 !important; border-color: #333 !important; }
    input, select, textarea { background-color: #222 !important; color: #fff !important; border-color: #444 !important; }
    .text-stone-800 { color: #e0e0e0 !important; }
    .text-stone-600 { color: #aaa !important; }
    .bg-stone-50 { background-color: #111 !important; }
    .lux-heading { font-family: 'Playfair Display', serif; color: #D4AF37 !important; }
</style>
'''

for t in targets:
    exact_name = f"260930-{t}"
    html_path = os.path.join(customer_dir, exact_name, 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Remove old dark-theme if exists
        html = re.sub(r'<style id="dark-theme">.*?</style>', '', html, flags=re.DOTALL)
        
        # Insert before </head>
        html = html.replace('</head>', dark_css + '\n</head>')
        
        # Change title
        html = re.sub(r'<title>.*?</title>', f'<title>{t.upper()} - Premium Private Stay</title>', html)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Applied Dark Theme to {exact_name}")

