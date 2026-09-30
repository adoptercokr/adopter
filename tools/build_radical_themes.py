import os
import re

def update_css(theme, css_add):
    path = f'Customer/tpl-{theme}/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Cache bust stay_config.js
    html = re.sub(r'<script src="stay_config.js\??.*?"></script>', '<script src="stay_config.js?v=100"></script>', html)
    
    # Remove existing injected theme block if any
    html = re.sub(r'<style id=".*?">.*?</style>', '', html, flags=re.DOTALL)
    
    # Inject new CSS
    style_block = f'\\n<style id="{theme}-theme">\\n{css_add}\\n</style>\\n'
    html = html.replace('</head>', style_block + '</head>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {theme}")

css_omai = '''
    body { background: #f4eee0 !important; color: #4a4238 !important; font-family: 'Noto Serif KR', serif !important; }
    #mainHeader { top: 1.5rem !important; width: calc(100% - 3rem) !important; margin: 0 auto; border-radius: 50px !important; background: rgba(244,238,224,0.9) !important; color: #4a4238 !important; border: none !important; box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important; }
    #mainHeader a { color: #4a4238 !important; }
    #mainHeader svg { stroke: #4a4238 !important; }
    .hero-slider { height: 85vh !important; border-radius: 40px !important; margin: 1.5rem !important; width: calc(100% - 3rem) !important; box-shadow: 0 20px 40px rgba(0,0,0,0.1) !important; }
    #about { display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 800px; margin: 0 auto; padding: 8rem 2rem !important; }
    #rooms .grid { display: flex !important; flex-direction: column !important; gap: 5rem !important; }
    #rooms .grid > div { display: flex !important; flex-direction: row !important; align-items: center !important; gap: 4rem !important; background: transparent !important; box-shadow: none !important; }
    #rooms .grid > div:nth-child(even) { flex-direction: row-reverse !important; }
    #rooms .grid > div > div:first-child { width: 50% !important; height: 500px !important; border-radius: 40px !important; overflow: hidden !important; }
    #rooms .grid > div > div:last-child { width: 50% !important; padding: 0 !important; }
    #gallery .grid { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 2rem; padding-bottom: 2rem; }
    #gallery .grid > div { flex: 0 0 80%; scroll-snap-align: center; border-radius: 40px !important; overflow: hidden !important; }
    #gallery .grid > div img { position: static !important; height: 600px !important; }
'''
update_css('05-wabi-sabi', css_omai)

css_editorial = '''
    body { background: #ffffff !important; color: #000000 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important; }
    #mainHeader { background: #fff !important; border-bottom: 3px solid #000 !important; color: #000 !important; padding: 2rem !important; }
    #mainHeader a { color: #000 !important; font-weight: 900 !important; text-transform: uppercase; font-size: 1.2rem !important; }
    #mainHeader svg { stroke: #000 !important; }
    h1, h2, h3, h4 { font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: -0.05em !important; }
    .hero-slider { height: 100vh !important; filter: grayscale(100%) contrast(1.2) !important; border-radius: 0 !important; }
    #about { border-bottom: 3px solid #000 !important; padding: 10rem 2rem !important; }
    #about p { font-size: 2.5rem !important; font-weight: 700 !important; line-height: 1.1 !important; max-width: 100% !important; text-transform: uppercase; }
    #rooms .grid { display: flex !important; flex-direction: column !important; gap: 0 !important; border-top: 3px solid #000 !important; }
    #rooms .grid > div { border-bottom: 3px solid #000 !important; display: flex !important; flex-direction: row !important; border-radius: 0 !important; box-shadow: none !important; }
    #rooms .grid > div > div:first-child { width: 40% !important; height: 400px !important; border-radius: 0 !important; }
    #rooms .grid > div > div:last-child { width: 60% !important; padding: 4rem !important; display: flex; flex-direction: column; justify-content: center; }
'''
update_css('06-modern-glass', css_editorial)

css_masseria = '''
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400&display=swap');
    body { background: #E8E4D9 !important; color: #3A352F !important; font-family: 'Cormorant Garamond', serif !important; }
    h1, h2, h3, h4 { font-style: italic !important; font-weight: 400 !important; letter-spacing: 0.05em !important; }
    #mainHeader { background: rgba(232,228,217,0.9) !important; border-bottom: 1px solid #D1CBBF !important; color: #3A352F !important; }
    #mainHeader a { color: #3A352F !important; }
    #mainHeader svg { stroke: #3A352F !important; }
    .hero-slider { border: 24px solid #F2EFE8 !important; box-shadow: 0 0 0 1px #D1CBBF !important; height: 90vh !important; border-radius: 0 !important; width: 100% !important; margin: 0 !important; }
    #gallery .grid { display: block !important; column-count: 3 !important; column-gap: 2rem !important; }
    #gallery .grid > div { break-inside: avoid !important; margin-bottom: 2rem !important; border-radius: 0 !important; overflow: hidden !important; height: auto !important; position: relative !important; }
    #gallery .grid > div img { height: auto !important; position: static !important; }
    #rooms .grid > div { background: #F2EFE8 !important; border: 1px solid #D1CBBF !important; border-radius: 0 !important; }
'''
update_css('07-hanok-heritage', css_masseria)

css_mrc = '''
    body { background: #FAFAFA !important; color: #222 !important; font-family: 'Inter', sans-serif !important; font-weight: 300 !important; }
    #mainHeader { background: transparent !important; border-bottom: 1px solid rgba(0,0,0,0.1) !important; color: #222 !important; }
    #mainHeader a { color: #222 !important; font-weight: 300 !important; letter-spacing: 0.1em; text-transform: uppercase; }
    #mainHeader svg { stroke: #222 !important; }
    section { padding: 10rem 4rem !important; border-bottom: 1px solid #EEE !important; }
    h2 { font-size: 2.5rem !important; font-weight: 200 !important; text-transform: uppercase !important; letter-spacing: 0.3em !important; text-align: center !important; margin-bottom: 5rem !important; }
    #rooms .grid { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 3rem !important; }
    #rooms .grid > div { background: transparent !important; box-shadow: none !important; border: 1px solid #EEE !important; border-radius: 0 !important; }
    #rooms .grid > div > div:first-child { border-radius: 0 !important; height: 450px !important; }
    .hero-slider { height: 100vh !important; border-radius: 0 !important; }
'''
update_css('08-coastal-breeze', css_mrc)

css_the8 = '''
    body { background: #FFFFFF !important; color: #000000 !important; font-family: 'Space Mono', monospace !important; border-left: 1px solid #000 !important; border-right: 1px solid #000 !important; max-width: 1440px !important; margin: 0 auto !important; }
    #mainHeader { background: #FFF !important; color: #000 !important; border-bottom: 1px solid #000 !important; position: sticky !important; }
    #mainHeader a { color: #000 !important; }
    #mainHeader svg { stroke: #000 !important; }
    section { padding: 5rem 2rem !important; border-bottom: 1px solid #000 !important; }
    h2 { font-weight: bold !important; text-transform: uppercase !important; border-bottom: 1px solid #000 !important; padding-bottom: 1rem !important; margin-bottom: 3rem !important; }
    .hero-slider { height: 75vh !important; border: 1px solid #000 !important; border-radius: 0 !important; margin-top: 2rem !important; }
    #rooms .grid { display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 0 !important; border-top: 1px solid #000 !important; border-left: 1px solid #000 !important; }
    #rooms .grid > div { border-right: 1px solid #000 !important; border-bottom: 1px solid #000 !important; border-radius: 0 !important; box-shadow: none !important; background: transparent !important; }
    #rooms .grid > div > div:first-child { border-radius: 0 !important; border-bottom: 1px solid #000 !important; height: 350px !important; }
    #gallery .grid { display: grid !important; grid-template-columns: repeat(4, 1fr) !important; gap: 0 !important; border-top: 1px solid #000 !important; border-left: 1px solid #000 !important; }
    #gallery .grid > div { border-right: 1px solid #000 !important; border-bottom: 1px solid #000 !important; border-radius: 0 !important; height: 250px !important; }
'''
update_css('09-industrial-chic', css_the8)

css_velaa = '''
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');
    body { background: #071526 !important; color: #C5A880 !important; font-family: 'Playfair Display', serif !important; }
    #mainHeader { background: rgba(7, 21, 38, 0.95) !important; border-bottom: 1px solid rgba(197, 168, 128, 0.3) !important; color: #C5A880 !important; }
    #mainHeader a { color: #C5A880 !important; font-weight: 400 !important; letter-spacing: 0.1em; }
    #mainHeader svg { stroke: #C5A880 !important; }
    h1, h2, h3, h4 { color: #E8D5B5 !important; text-align: center !important; font-weight: 400 !important; letter-spacing: 0.05em !important; }
    .hero-slider { height: 100vh !important; border-radius: 0 !important; }
    .hero-slider::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, #071526, transparent 50%); z-index: 2; pointer-events: none; }
    #about { padding: 8rem 2rem !important; }
    #rooms .grid { display: grid !important; grid-template-columns: 1fr !important; max-width: 900px !important; margin: 0 auto !important; gap: 5rem !important; }
    #rooms .grid > div { background: #0B1D33 !important; border: 1px solid rgba(197, 168, 128, 0.3) !important; border-radius: 0 !important; display: flex !important; flex-direction: column !important; align-items: center !important; text-align: center !important; padding-bottom: 3rem !important; }
    #rooms .grid > div > div:first-child { border-radius: 0 !important; height: 600px !important; width: 100% !important; margin-bottom: 2rem !important; }
    #rooms .grid > div > div:last-child { width: 80% !important; }
'''
update_css('10-velaa-luxury', css_velaa)

print("Radical themes successfully applied!")
