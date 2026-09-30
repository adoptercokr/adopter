import os

def update_css(theme, css_add):
    path = f'Customer/tpl-{theme}/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # insert css_add before </style> in the injected theme
    import re
    html = re.sub(r'(</style>\s*</head>)', f"{css_add}\\n\\1", html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {theme}")

css_wabi = '''
    /* Wabi Sabi Radical Changes */
    .hero-slider { height: 60vh !important; border-radius: 50% 50% 0 0 !important; width: 80% !important; margin: 0 auto !important; }
    #about { display: flex; flex-direction: column; align-items: center; text-align: center; }
    #gallery-grid { display: block !important; column-count: 2; column-gap: 1rem; }
    #gallery-grid > div { break-inside: avoid; margin-bottom: 1rem; }
'''
update_css('05-wabi-sabi', css_wabi)

css_glass = '''
    /* Glass Radical Changes */
    #header { top: auto !important; bottom: 0 !important; border-top: 1px solid rgba(255,255,255,0.2) !important; border-bottom: none !important; }
    .hero-slider { height: 100vh !important; }
    section { padding: 10rem 2rem !important; }
    .container { max-width: 1600px !important; }
'''
update_css('06-modern-glass', css_glass)

css_hanok = '''
    /* Hanok Radical Changes */
    #about p { writing-mode: vertical-rl; text-orientation: upright; height: 300px; margin: 0 auto; line-height: 2.5; }
    .hero-slider { border: double 12px #4A3525 !important; }
    #header { background: #F5F0E6 !important; }
'''
update_css('07-hanok-heritage', css_hanok)

css_coastal = '''
    /* Coastal Radical Changes */
    section { margin: 2rem !important; border-radius: 40px !important; background: white; padding: 4rem !important; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    body { background: #E0F2F1 !important; }
    .hero-slider { border-radius: 40px !important; margin: 2rem !important; width: calc(100% - 4rem) !important; }
'''
update_css('08-coastal-breeze', css_coastal)

css_industrial = '''
    /* Industrial Radical Changes */
    #header { background: #000 !important; color: #0f0 !important; font-family: monospace !important; }
    #header a { color: #0f0 !important; }
    #header svg { stroke: #0f0 !important; }
    .hero-slider { filter: invert(1); }
    section { border: 4px solid #000; margin: 1rem; }
'''
update_css('09-industrial-chic', css_industrial)

css_velaa = '''
    /* Velaa Radical Changes */
    body { border: 20px solid #D4AF37; min-height: 100vh; }
    .hero-slider { height: 50vh !important; margin-top: 2rem !important; }
    h1 { font-size: 4rem !important; }
    #gallery-grid { grid-template-columns: repeat(1, 1fr) !important; }
'''
update_css('10-velaa-luxury', css_velaa)

