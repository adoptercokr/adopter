import os, re

kakao_css = '''
    .fab-kakao { position: fixed; bottom: 100px; right: 30px; width: 60px; height: 60px; background-color: #FEE500; color: #000; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,0,0,0.2); z-index: 9999; transition: transform 0.3s ease; }
    .fab-kakao:hover { transform: scale(1.1); }
'''

kakao_html = '''
    <!-- Floating Kakao Button -->
    <a href="javascript:void(0)" onclick="alert('카카오톡 채널 링크를 설정해주세요.')" class="fab-kakao">
      <svg viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8"><path d="M12 3c-5.523 0-10 3.582-10 8 0 2.827 1.76 5.313 4.417 6.78-.182.646-.658 2.34-.755 2.73-.122.493.18.48.375.352.155-.1 1.956-1.282 2.756-1.808C9.832 19.346 10.9 19.5 12 19.5c5.523 0 10-3.582 10-8s-4.477-8-10-8z"/></svg>
    </a>
'''

def patch_file(p):
    if not os.path.exists(p): return
    with open(p, 'r', encoding='utf-8') as f: html = f.read()

    # 1. Nav update
    nav_old = '''<nav class="hidden md:flex space-x-10 text-sm tracking-widest uppercase">
          <a href="#about" class="hover:text-brand-accent transition-colors">About</a>
          <a href="#gallery" class="hover:text-brand-accent transition-colors">Gallery</a>
          <a href="#reservation" class="hover:text-brand-accent transition-colors">Reservation</a>
        </nav>'''
    
    nav_new = '''<nav class="hidden md:flex space-x-10 text-sm tracking-widest uppercase">
          <a href="#about" class="hover:text-brand-accent transition-colors">About</a>
          <a href="#gallery" class="hover:text-brand-accent transition-colors">Gallery</a>
          <a href="#calendar-section" class="hover:text-brand-accent transition-colors">Calendar</a>
          <a href="javascript:void(0)" onclick="window.open(typeof STAY_CONFIG !== 'undefined' ? STAY_CONFIG.naverLink || '#' : '#', '_blank')" class="hover:text-brand-accent transition-colors">Reservation</a>
        </nav>'''
        
    html = html.replace(nav_old, nav_new)
    
    # 2. Kakao CSS
    if '.fab-kakao' not in html:
        html = html.replace('.fab-call:hover { transform: scale(1.1); }', '.fab-call:hover { transform: scale(1.1); }\n' + kakao_css)
        
    # 3. Kakao HTML
    if 'fab-kakao' not in html.split('</style>')[1]:
        html = html.replace('<!-- Floating Call Button -->', kakao_html + '\n    <!-- Floating Call Button -->')
        
    with open(p, 'w', encoding='utf-8') as f: f.write(html)
    print("Patched", p)

patch_file('templates/01-stay/index.html')
for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    patch_file(os.path.join('Customer', d, 'index.html'))
