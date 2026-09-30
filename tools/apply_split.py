import os, re

split_css = '''
<style id="split-theme">
    /* Elegant Split-Screen Editorial Theme */
    body { background-color: #FAFAFA !important; color: #333 !important; }
    
    @media (min-width: 1024px) {
        body { display: flex; flex-direction: row-reverse; }
        
        /* Right side: Fixed Hero/Branding (Since row-reverse, it appears on the Left) */
        /* Actually let's just make it normal flex */
        body { flex-direction: row; align-items: flex-start; }
        
        #header { display: none !important; } /* Hide standard header */
        
        .hero-slider {
            position: sticky !important;
            top: 0;
            width: 45vw !important;
            height: 100vh !important;
            flex-shrink: 0;
            border-right: 1px solid #EAE6E1;
        }
        
        .content-wrapper {
            width: 55vw !important;
            padding: 4rem 4rem !important;
            background: #fff;
        }
        
        /* Adjust inner sections for the new width */
        .max-w-7xl { max-w-full !important; px-0 !important; }
        section { padding: 4rem 0 !important; }
    }
    
    .lux-heading { font-family: 'Noto Serif KR', serif !important; letter-spacing: -0.02em; }
    .text-brand-accent { color: #8A7353 !important; }
    .bg-brand-accent { background-color: #8A7353 !important; }
</style>
'''

targets = ['peaceofmind', 'cloudhouse', 'dalsoop', 'hijane', 'dumomansion', 'late-summer', 'seolchon', 'wolla', 'stay-2045570969']
for t in targets:
    p = os.path.join('Customer', f'260930-{t}', 'index.html')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f: html = f.read()
        
        # Wrap sections after hero in a div
        if '<div class="content-wrapper">' not in html:
            html = html.replace('</section>\n\n    <!-- About Section -->', '</section>\n\n<div class="content-wrapper">\n    <!-- About Section -->')
            html = html.replace('</body>', '</div>\n</body>')
        
        html = re.sub(r'<style id="split-theme">.*?</style>', '', html, flags=re.DOTALL)
        html = html.replace('</head>', split_css + '\n</head>')
        
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
        print("Applied split theme to", p)
