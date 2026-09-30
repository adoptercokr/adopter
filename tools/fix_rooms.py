import re, os

def fix_calendar():
    for d in os.listdir('Customer'):
        if not d.startswith('260930-'): continue
        p = os.path.join('Customer', d, 'index.html')
        if not os.path.exists(p): continue
        
        with open(p, 'r', encoding='utf-8') as f: html = f.read()
        
        # 1. Hide roomTab2 and roomTab3
        html = html.replace('id="roomTab2"', 'id="roomTab2" style="display:none;"')
        html = html.replace('id="roomTab3"', 'id="roomTab3" style="display:none;"')
        
        # 2. Fix the loop in selectRoomType to only use [1]
        html = html.replace('[1, 2, 3].forEach(id => {', '[1].forEach(id => {')
        
        # 3. Fix loadRoomsConfig if it tries to load 1,2,3
        # I will also just make sure ROOMS has 2 and 3 as fallbacks just in case
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
        # Replace the DEFAULT_ROOMS definition in html
        html = re.sub(r'const DEFAULT_ROOMS = \{.*?\n    \};', fallback_rooms.strip(), html, flags=re.DOTALL)
        
        # 4. Remove grid-cols-3 and make it grid-cols-1 for the room tabs
        html = html.replace('class="grid grid-cols-3 gap-2"', 'class="grid grid-cols-1 gap-2"')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed {d}")

fix_calendar()
