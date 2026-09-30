import re, os
with open('templates/01-stay/index.html', 'r', encoding='utf-8') as f: html = f.read()
with open('tools/cal_extracted.html', 'r', encoding='utf-8') as f: cal_html = f.read()
with open('tools/script_extracted.js', 'r', encoding='utf-8') as f: cal_js = f.read()

# Replace the Reservation section
html = re.sub(r'<section id="reservation".*?</section>', cal_html, html, flags=re.DOTALL)

# Insert the calendar JS logic at the end of the script block
# But wait, cal_js has EVERYTHING from moheomdam's script!
# We just need to replace the entire <script> block in index.html with moheomdam's, but keeping Swiper and GLightbox logic!
# Actually, the user essentially wants the EXACT SAME behavior as Heestay/Moheomdam.
