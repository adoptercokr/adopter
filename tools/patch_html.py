import os
p = 'templates/01-stay/index.html'
with open(p, 'r', encoding='utf-8') as f: html = f.read()

# Fix price display when 0
html = html.replace("if(pWd > 0) document.getElementById('price-weekday').innerText = pWd.toLocaleString() + '원';",
"if(pWd > 0) document.getElementById('price-weekday').innerText = pWd.toLocaleString() + '원'; else document.getElementById('price-weekday').innerText = '실시간 확인';")
html = html.replace("if(pWe > 0) document.getElementById('price-weekend').innerText = pWe.toLocaleString() + '원';",
"if(pWe > 0) document.getElementById('price-weekend').innerText = pWe.toLocaleString() + '원'; else document.getElementById('price-weekend').innerText = '실시간 확인';")
html = html.replace("if(pPk > 0) document.getElementById('price-peak').innerText = pPk.toLocaleString() + '원';",
"if(pPk > 0) document.getElementById('price-peak').innerText = pPk.toLocaleString() + '원'; else document.getElementById('price-peak').innerText = '실시간 확인';")

# Fix calendar calculation when price is 0
html = html.replace("if (pWd === 0) return; // If prices aren't fetched properly",
"if (pWd === 0) { document.getElementById('calc-title').innerText = '예상 결제 금액'; document.getElementById('calc-desc').innerText = '선택하신 날짜의 요금은 네이버 예약에서 실시간으로 확인 가능합니다.'; document.getElementById('price-block').classList.add('hidden'); document.getElementById('calc-result').classList.remove('hidden'); document.getElementById('calc-total').innerText = '실시간 요금 확인'; return; }")

with open(p, 'w', encoding='utf-8') as f: f.write(html)

for d in os.listdir('Customer'):
    if not d.startswith('260930-'): continue
    tp = os.path.join('Customer', d, 'index.html')
    if os.path.exists(tp):
        with open(tp, 'w', encoding='utf-8') as f: f.write(html)
