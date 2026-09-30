import re, os
p = 'templates/01-stay/index.html'
with open(p, 'r', encoding='utf-8') as f: html = f.read()

html = html.replace('id="roomTab2"', 'id="roomTab2" style="display:none;"')
html = html.replace('id="roomTab3"', 'id="roomTab3" style="display:none;"')
html = html.replace('[1, 2, 3].forEach(id => {', '[1].forEach(id => {')
html = html.replace('class="grid grid-cols-3 gap-2"', 'class="grid grid-cols-1 gap-2"')

fallback_rooms = '''
    const DEFAULT_ROOMS = {
      1: {
        name: nm,
        badge: "독채",
        baseGuests: 2,
        maxGuests: 4,
        weekdayPrice: pWd,
        weekendPrice: pWe,
        peakSurcharge: pPk > pWe ? (pPk - pWe) : 0,
        extraGuestFee: 20000,
        priceRange: pWd.toLocaleString() + "원 ~ " + pWe.toLocaleString() + "원",
        metaRooms: "공간",
        metaTime: "입실 15:00 · 퇴실 11:00",
        desc: "", guide: "", config: [], amenities: []
      },
      2: { name: "Room 2", baseGuests: 2, weekdayPrice: 0 },
      3: { name: "Room 3", baseGuests: 2, weekdayPrice: 0 }
    };
'''
html = re.sub(r'const DEFAULT_ROOMS = \{.*?\n    \};', fallback_rooms.strip(), html, flags=re.DOTALL)

with open(p, 'w', encoding='utf-8') as f: f.write(html)
