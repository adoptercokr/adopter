import os

def append_css(theme, css_add):
    path = f'Customer/tpl-{theme}/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('</style>', f"{css_add}\\n</style>")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Final Iteration {theme}")

css_omai = '''
    /* Iteration 3: Final structural fix */
    html { scroll-behavior: smooth; }
    #header { position: absolute !important; }
'''
append_css('05-wabi-sabi', css_omai)

css_editorial = '''
    /* Iteration 3 */
    html { scroll-behavior: smooth; }
    #header { position: sticky !important; }
'''
append_css('06-modern-glass', css_editorial)

css_masseria = '''
    /* Iteration 3 */
    html { scroll-behavior: smooth; }
'''
append_css('07-hanok-heritage', css_masseria)

css_mrc = '''
    /* Iteration 3 */
    html { scroll-behavior: smooth; }
'''
append_css('08-coastal-breeze', css_mrc)

css_the8 = '''
    /* Iteration 3 */
    html { scroll-behavior: smooth; }
'''
append_css('09-industrial-chic', css_the8)

css_velaa = '''
    /* Iteration 3 */
    html { scroll-behavior: smooth; }
'''
append_css('10-velaa-luxury', css_velaa)

print("Iteration 3 final fixes applied!")
