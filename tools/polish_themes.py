import os

def append_css(theme, css_add):
    path = f'Customer/tpl-{theme}/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('</style>', f"{css_add}\\n</style>")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Polished {theme}")

css_omai = '''
    /* Iteration 2: Polish */
    h1 { font-size: 3.5rem !important; line-height: 1.2 !important; }
    #gallery .grid > div { box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
'''
append_css('05-wabi-sabi', css_omai)

css_editorial = '''
    /* Iteration 2: Polish */
    h2 { font-size: 5rem !important; margin-bottom: 2rem !important; }
    #rooms .grid > div > div:first-child { filter: grayscale(100%); transition: filter 0.3s; }
    #rooms .grid > div:hover > div:first-child { filter: grayscale(0%); }
'''
append_css('06-modern-glass', css_editorial)

css_masseria = '''
    /* Iteration 2: Polish */
    .hero-slider { box-shadow: inset 0 0 0 1px #3A352F !important; }
    #about p { text-align: justify !important; text-align-last: center !important; }
'''
append_css('07-hanok-heritage', css_masseria)

css_mrc = '''
    /* Iteration 2: Polish */
    #rooms .grid > div:hover { background: #fff !important; transform: translateY(-10px); transition: 0.3s; box-shadow: 0 20px 40px rgba(0,0,0,0.05) !important; }
    h2 { letter-spacing: 0.5em !important; }
'''
append_css('08-coastal-breeze', css_mrc)

css_the8 = '''
    /* Iteration 2: Polish */
    #gallery .grid > div:hover { filter: invert(1); }
    h2 { font-size: 2rem !important; }
'''
append_css('09-industrial-chic', css_the8)

css_velaa = '''
    /* Iteration 2: Polish */
    h1 { text-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    #rooms .grid > div > div:first-child { filter: brightness(0.8); }
'''
append_css('10-velaa-luxury', css_velaa)

print("Iteration 2 polish applied!")
