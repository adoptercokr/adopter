import re

with open('moheomdam.html', 'r', encoding='utf-8') as f: html = f.read()
cal_section = re.search(r'<section id="calendar-section".*?</section>', html, re.DOTALL)
if cal_section:
    with open('tools/cal_extracted.html', 'w', encoding='utf-8') as f:
        f.write(cal_section.group(0))
    print('Section saved:', len(cal_section.group(0)))
    
script_section = re.search(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{.*?(// 2\. 달력 렌더링.*?)// 옵저버.*?</script>', html, re.DOTALL)
if script_section:
    with open('tools/script_extracted.js', 'w', encoding='utf-8') as f:
        f.write(script_section.group(1))
    print('Script saved:', len(script_section.group(1)))
else:
    # let's just grab the whole script block
    scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    if scripts:
        with open('tools/script_extracted.js', 'w', encoding='utf-8') as f:
            f.write(scripts[-1])
        print('Script saved (last block):', len(scripts[-1]))

