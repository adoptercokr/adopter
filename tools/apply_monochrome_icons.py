import re

file_path = "Customer/260930-moheomdam-모험담/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace emoji in Meta 3 lines in Room Modal
old_meta = """            <!-- 핵심 속성 3줄 (네이버 스타일) -->
            <div class="space-y-1 text-xs text-stone-600 font-serif-kr">
              <div class="flex items-center gap-2">
                <span class="text-stone-400">👤</span> <span id="roomMetaGuestsText">독채, 기준 2인 (최대 5인)</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-stone-400">🛏️</span> <span id="roomMetaRoomsText">침실1, 침대1, 욕실1</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-stone-400">🕒</span> <span id="roomMetaTimeText">입실오후 3:00, 퇴실오전 11:00</span>
              </div>
            </div>"""

new_meta = """            <!-- 핵심 속성 3줄 (네이버 스타일 - 단색 라인 SVG 아이콘) -->
            <div class="space-y-1.5 text-xs text-stone-600 font-serif-kr">
              <div class="flex items-center gap-2">
                <span class="text-stone-400 flex-shrink-0">
                  <svg class="w-4 h-4 text-stone-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                </span>
                <span id="roomMetaGuestsText">독채, 기준 2인 (최대 4인)</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-stone-400 flex-shrink-0">
                  <svg class="w-4 h-4 text-stone-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><path d="M6 8v9"/></svg>
                </span>
                <span id="roomMetaRoomsText">침실 1개 · 침대 1개 · 욕실 1개</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-stone-400 flex-shrink-0">
                  <svg class="w-4 h-4 text-stone-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </span>
                <span id="roomMetaTimeText">입실 16:00 · 퇴실 11:00</span>
              </div>
            </div>"""

if old_meta in content:
    content = content.replace(old_meta, new_meta)
    print("Replaced meta 3 lines with clean SVGs!")
else:
    # Try regex fallback if spacing differs
    pattern = r'<!-- 핵심 속성 3줄.*?<span id="roomMetaTimeText">[^<]+</span>\s*</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_meta + content[match.end():]
        print("Replaced meta 3 lines with regex!")
    else:
        print("Warning: Meta 3 lines block not found!")

# 2. Update AMENITY SVG ICONS in JavaScript
old_amen_loop = """      // 편의시설 그리드
      const amenGrid = document.getElementById('roomAmenitiesGrid');
      amenGrid.innerHTML = '';
      (data.amenities || []).forEach(a => {
        const item = document.createElement('div');
        item.className = 'flex flex-col items-center justify-center p-2.5 rounded-2xl bg-stone-50 border border-stone-100 hover:bg-stone-100 transition shadow-sm';
        item.innerHTML = `<span class="text-2xl mb-1">${a.icon}</span><span class="text-[11px] font-medium text-stone-700">${a.name}</span>`;
        amenGrid.appendChild(item);
      });"""

new_amen_loop = """      // 편의시설 그리드 (단색/흑백 미니멀 라인 SVG 아이콘 적용 - 조잡한 컬러 이모지 배제)
      const AMENITY_ICONS = {
        '풀빌라': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2-1 4-1 6 0s4 1 6 0 4-1 6 0"/><path d="M2 17c2-1 4-1 6 0s4 1 6 0 4-1 6 0"/><path d="M15 5a2 2 0 1 0 4 0 2 2 0 0 0-4 0z"/><path d="m8 10 4-5 3 2"/></svg>`,
        '프라이빗풀': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2-1 4-1 6 0s4 1 6 0 4-1 6 0"/><path d="M2 17c2-1 4-1 6 0s4 1 6 0 4-1 6 0"/><path d="M15 5a2 2 0 1 0 4 0 2 2 0 0 0-4 0z"/><path d="m8 10 4-5 3 2"/></svg>`,
        'OTT': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg>`,
        '욕실용품': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6h6m-3-3v3"/><rect x="6" y="6" width="12" height="15" rx="3"/><path d="M10 12h4"/></svg>`,
        '와이파이': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>`,
        '취사가능': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2v20M6 2v20M6 7h12M6 12h12"/></svg>`,
        'VOD': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="8" x2="22" y2="8"/><line x1="2" y1="16" x2="22" y2="16"/><line x1="7" y1="4" x2="7" y2="8"/><line x1="17" y1="4" x2="17" y2="8"/></svg>`,
        '테라스': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>`,
        '원형벽난로': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>`,
        '커피머신': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>`,
        '노천자쿠지': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v7a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-7"/><path d="M2 12h20"/><path d="M7 4a2 2 0 0 1 0 4 2 2 0 0 0 0 4"/><path d="M12 4a2 2 0 0 1 0 4 2 2 0 0 0 0 4"/><path d="M17 4a2 2 0 0 1 0 4 2 2 0 0 0 0 4"/></svg>`,
        '야외불멍': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>`,
        '바베큐': `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10a9 9 0 0 0 18 0H3z"/><line x1="12" y1="10" x2="12" y2="21"/><line x1="7" y1="14" x2="4" y2="21"/><line x1="17" y1="14" x2="20" y2="21"/></svg>`
      };
      const DEFAULT_ICON = `<svg class="w-5 h-5 text-stone-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`;

      const amenGrid = document.getElementById('roomAmenitiesGrid');
      amenGrid.innerHTML = '';
      (data.amenities || []).forEach(a => {
        const item = document.createElement('div');
        item.className = 'flex flex-col items-center justify-center p-3 rounded-2xl bg-stone-50/80 border border-stone-200/60 hover:bg-stone-100 hover:border-stone-300 transition shadow-[0_1px_2px_rgba(0,0,0,0.04)]';
        const svgIcon = AMENITY_ICONS[a.name] || a.svg || DEFAULT_ICON;
        item.innerHTML = `<div class="mb-1.5 flex items-center justify-center">${svgIcon}</div><span class="text-[11px] font-medium text-stone-800 tracking-tight">${a.name}</span>`;
        amenGrid.appendChild(item);
      });"""

if old_amen_loop in content:
    content = content.replace(old_amen_loop, new_amen_loop)
    print("Replaced amenities rendering loop with monochrome SVGs!")
else:
    print("Warning: old_amen_loop not found directly!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated Customer/260930-moheomdam-모험담/index.html with monochrome SVGs!")
