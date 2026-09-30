import re, os
with open('tools/script_extracted.js', 'r', encoding='utf-8') as f: js = f.read()

# Replace DEFAULT_ROOMS with dynamic one from STAY_CONFIG
dynamic_rooms = '''
    const cRates = (typeof STAY_CONFIG !== 'undefined' && STAY_CONFIG.rates) ? STAY_CONFIG.rates : {weekday: '0', weekend: '0', peak: '0'};
    const pWd = parseInt(String(cRates.weekday).replace(/,/g,'')) || 0;
    const pWe = parseInt(String(cRates.weekend).replace(/,/g,'')) || 0;
    const pPk = parseInt(String(cRates.peak).replace(/,/g,'')) || 0;
    const nm = (typeof STAY_CONFIG !== 'undefined' && STAY_CONFIG.name) ? STAY_CONFIG.name : '객실';
    
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
      }
    };
'''

js = re.sub(r'const DEFAULT_ROOMS = \{.*?\n    \};', dynamic_rooms, js, flags=re.DOTALL)

with open('tools/script_extracted_dynamic.js', 'w', encoding='utf-8') as f: f.write(js)
