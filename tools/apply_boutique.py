import os, re

boutique_css = '''
<style id="boutique-theme">
    /* Boutique Minimal Theme Overrides */
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');
    
    body { background-color: #FDFBF7 !important; color: #4A4541 !important; }
    
    /* Boxed Hero with elegant shadow */
    .hero-slider {
        height: 75vh !important;
        width: 94% !important;
        max-width: 1400px;
        margin: 2rem auto !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15) !important;
    }
    .hero-slider .swiper-wrapper { height: 75vh !important; }
    
    /* Header integration */
    #header {
        position: relative !important;
        background: transparent !important;
        color: #4A4541 !important;
    }
    #header .text-white { color: #4A4541 !important; }
    
    /* Typography Overrides */
    .lux-heading { font-family: 'Nanum Myeongjo', serif !important; color: #4A4541 !important; font-weight: 700; letter-spacing: -0.02em; }
    
    /* About section left-aligned */
    #about .text-center { text-align: left !important; }
    #about .items-center { align-items: flex-start !important; }
    
    /* Sections background overrides */
    .bg-white, .bg-stone-50 { background-color: transparent !important; }
    
    /* Brand Accent */
    .text-brand-accent { color: #A67C52 !important; }
    .bg-brand-accent { background-color: #A67C52 !important; }
    .text-brand-wood { color: #A67C52 !important; }
    
    /* Calendar UI adjustments */
    .calendar-container { background: #fff !important; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
    .cal-day:hover:not(.disabled):not(.booked) { background-color: #A67C52 !important; color: #fff !important; }
    .cal-day.selected { background-color: #A67C52 !important; color: #fff !important; font-weight: 700; }
</style>
'''

targets = ['peaceofmind', 'cloudhouse', 'dalsoop', 'hijane', 'dumomansion', 'late-summer', 'seolchon', 'wolla', 'stay-2045570969']
for t in targets:
    p = os.path.join('Customer', f'260930-{t}', 'index.html')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f: html = f.read()
        html = re.sub(r'<style id="boutique-theme">.*?</style>', '', html, flags=re.DOTALL)
        html = html.replace('</head>', boutique_css + '\n</head>')
        
        # Make header items not white on initial load
        html = html.replace('bg-transparent text-white border-transparent', 'bg-transparent text-brand-dark border-transparent')
        
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
        print("Applied boutique theme to", p)
