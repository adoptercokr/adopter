import os
import shutil
import re

base_tpl = 'Customer/260930-moheomdam'
templates_dir = 'templates'

os.makedirs(templates_dir, exist_ok=True)

# 1. Heestay (01-stay)
shutil.copytree('templates/01-stay', 'templates/01-heestay', dirs_exist_ok=True)

# 2. Moheomdam
shutil.copytree(base_tpl, 'templates/02-moheomdam', dirs_exist_ok=True)

# Read base html (without any custom injected themes)
with open(os.path.join(base_tpl, 'index.html'), 'r', encoding='utf-8') as f:
    base_html = f.read()
# Ensure no injected theme exists in base
base_html = re.sub(r'<style id=".*?">.*?</style>', '', base_html, flags=re.DOTALL)

def create_variant(name, css, folder_name):
    folder_path = os.path.join(templates_dir, folder_name)
    shutil.copytree(base_tpl, folder_path, dirs_exist_ok=True)
    
    style_block = f'\n<style id="{name}-theme">\n{css}\n</style>\n'
    new_html = base_html.replace('</head>', style_block + '</head>')
    
    with open(os.path.join(folder_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created {folder_name}")

# 03 Dark Luxury
css_dark = '''
    body { background-color: #111111 !important; color: #E8E8E8 !important; }
    h1, h2, h3, h4 { color: #FFFFFF !important; font-family: 'Cinzel', serif !important; }
    .hero-slider { opacity: 0.8; }
    #header { background: rgba(0,0,0,0.9) !important; border-bottom: 1px solid #333; }
    .swiper-button-next, .swiper-button-prev { color: #fff !important; }
    button, a.btn { background: #333 !important; color: #fff !important; border: 1px solid #555 !important; }
'''
create_variant('dark-luxury', css_dark, '03-dark-luxury')

# 04 Boutique Minimal
css_boutique = '''
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');
    body { background-color: #FDFBF7 !important; color: #4A4541 !important; }
    .hero-slider {
        height: 75vh !important; width: 94% !important; max-width: 1400px;
        margin: 2rem auto !important; border-radius: 12px !important; box-shadow: 0 30px 60px rgba(0,0,0,0.15) !important;
    }
    .hero-slider .swiper-wrapper { height: 75vh !important; }
    #header { position: relative !important; background: transparent !important; border-bottom: none !important; }
    #header nav a, #header .brand-name { color: #4A4541 !important; }
    #header svg { stroke: #4A4541 !important; }
    #header .bg-white\\\\/10 { background: rgba(74,69,65,0.1) !important; border-color: rgba(74,69,65,0.2) !important; color: #4A4541 !important; }
    h1, h2, h3, h4, .font-serif { font-family: 'Nanum Myeongjo', serif !important; letter-spacing: 0.05em; color: #2C2926 !important; }
'''
create_variant('boutique', css_boutique, '04-boutique-minimal')

# 05 Wabi Sabi
css_wabi = '''
    body { background-color: #EFEBE4 !important; color: #5C5248 !important; font-family: 'Noto Serif KR', serif !important; }
    .hero-slider { filter: sepia(0.2) contrast(0.9); }
    h1, h2 { font-weight: 300 !important; letter-spacing: 0.1em; color: #3A3229 !important; }
    img { border-radius: 4px !important; }
'''
create_variant('wabisabi', css_wabi, '05-wabi-sabi')

# 06 Modern Glass
css_glass = '''
    body { background-color: #FAFAFA !important; color: #111 !important; font-family: 'Pretendard', sans-serif !important; }
    #header { background: rgba(255,255,255,0.1) !important; backdrop-filter: blur(15px) !important; border-bottom: 1px solid rgba(255,255,255,0.2) !important; }
    h1, h2, h3 { font-weight: 700 !important; letter-spacing: -0.02em; }
    .hero-slider::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, transparent, rgba(250,250,250,1)); z-index: 2; pointer-events: none; }
'''
create_variant('glass', css_glass, '06-modern-glass')

# 07 Hanok Heritage
css_hanok = '''
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang&display=swap');
    body { background-color: #F5F0E6 !important; color: #3D2B1F !important; font-family: 'Gowun Batang', serif !important; }
    h1, h2, h3 { color: #2C1E16 !important; }
    .hero-slider { border: 8px solid #4A3525 !important; margin: 1rem !important; width: calc(100% - 2rem) !important; }
'''
create_variant('hanok', css_hanok, '07-hanok-heritage')

# 08 Coastal Breeze
css_coastal = '''
    body { background-color: #F2F7F9 !important; color: #2B4C5E !important; }
    h1, h2 { color: #1A3645 !important; }
    img { border-radius: 20px !important; }
    .hero-slider { border-bottom-left-radius: 50px !important; border-bottom-right-radius: 50px !important; }
'''
create_variant('coastal', css_coastal, '08-coastal-breeze')

# 09 Industrial Chic
css_industrial = '''
    body { background-color: #D3D3D3 !important; color: #1C1C1C !important; font-family: 'Helvetica Neue', Helvetica, sans-serif !important; }
    h1, h2, h3 { text-transform: uppercase !important; font-weight: 900 !important; letter-spacing: -1px; }
    img { filter: grayscale(20%) contrast(1.1); }
'''
create_variant('industrial', css_industrial, '09-industrial-chic')

# 10 Velaa Luxury
css_velaa = '''
    body { background-color: #0B1C2E !important; color: #D4AF37 !important; font-family: 'Cormorant Garamond', serif !important; }
    h1, h2, h3 { color: #F3E5AB !important; text-align: center; }
    p { text-align: center; }
    .hero-slider { border: 2px solid #D4AF37 !important; padding: 5px; }
'''
create_variant('velaa', css_velaa, '10-velaa-luxury')

print("All 10 templates created successfully.")
