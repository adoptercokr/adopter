import re

file_path = 'Customer/260930-moheomdam-모험담/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 객실 메인 및 썸네일 이미지 업데이트 (Section 4)
html = html.replace('src="./img/photo_1.jpg" alt="첫번째 모험"', 'src="./img/room1_1.jpg" alt="첫번째 모험"')
html = html.replace('src="./img/photo_3.jpg" alt="두번째 모험"', 'src="./img/room2_1.jpg" alt="두번째 모험"')
html = html.replace('src="./img/photo_7.jpg" alt="세번째 모험"', 'src="./img/room3_1.jpg" alt="세번째 모험"')

# 객실 1 썸네일 3장 교체
html = re.sub(
    r'(<img src="\./img/photo_4\.jpg" class="h-16 w-full object-cover rounded-sm" alt="다이닝">.*?<img src="\./img/photo_6\.jpg" class="h-16 w-full object-cover rounded-sm" alt="정원">)',
    '<img src="./img/room1_2.jpg" class="h-16 w-full object-cover rounded-sm" alt="침실"><img src="./img/room1_3.jpg" class="h-16 w-full object-cover rounded-sm" alt="다이닝"><img src="./img/room1_4.jpg" class="h-16 w-full object-cover rounded-sm" alt="욕실">',
    html,
    flags=re.DOTALL
)

# 객실 2 썸네일 3장 교체
html = re.sub(
    r'(<img src="\./img/photo_2\.jpg" class="h-16 w-full object-cover rounded-sm" alt="테라스">.*?<img src="\./img/photo_4\.jpg" class="h-16 w-full object-cover rounded-sm" alt="다이닝">)',
    '<img src="./img/room2_2.jpg" class="h-16 w-full object-cover rounded-sm" alt="벽난로"><img src="./img/room2_3.jpg" class="h-16 w-full object-cover rounded-sm" alt="거실"><img src="./img/room2_4.jpg" class="h-16 w-full object-cover rounded-sm" alt="테라스">',
    html,
    flags=re.DOTALL
)

# 객실 3 썸네일 3장 교체
html = re.sub(
    r'(<img src="\./img/photo_8\.jpg" class="h-16 w-full object-cover rounded-sm" alt="자쿠지">.*?<img src="\./img/photo_9\.jpg" class="h-16 w-full object-cover rounded-sm" alt="자연뷰">)',
    '<img src="./img/room3_2.jpg" class="h-16 w-full object-cover rounded-sm" alt="수영장"><img src="./img/room3_3.jpg" class="h-16 w-full object-cover rounded-sm" alt="자쿠지"><img src="./img/room3_4.jpg" class="h-16 w-full object-cover rounded-sm" alt="불멍">',
    html,
    flags=re.DOTALL
)

# 2. DEFAULT_ROOMS 데이터 업데이트
old_script_start = html.find('const DEFAULT_ROOMS = {')
holidays_idx = html.find('// 2. 대한민국 공식 공휴일 프리셋')

new_rooms_code = """const DEFAULT_ROOMS = {
      1: {
        name: "첫번째모험",
        badge: "독채 1동 · 커플&소규모",
        baseGuests: 2,
        maxGuests: 4,
        weekdayPrice: 350000,
        weekendPrice: 400000,
        peakSurcharge: 50000,
        extraGuestFee: 20000,
        priceRange: "350,000 ~ 400,000원",
        metaRooms: "침실 1개 · 침대 1개 · 욕실 1개",
        metaTime: "입실 16:00 · 퇴실 11:00",
        desc: "돌담으로 아늑하게 둘러싸인 프라이빗 잔디 정원과 감성 우드 다이닝 키친이 돋보이는 독채 공간입니다.",
        guide: "외부의 자연을 넘나들 수 있는 개방감 있는 공간으로 반려견 동반이 가능한 객실입니다. 아늑한 돌담 정원과 사계절 푸른 제주의 자연 속에서 온전한 쉼을 경험해보세요.",
        config: [
          { title: "유형", value: "독채" },
          { title: "침실 1", value: "킹 1" },
          { title: "욕실", value: "욕실 1" }
        ],
        amenities: [
          { icon: "🏊", name: "풀빌라" },
          { icon: "📺", name: "OTT" },
          { icon: "🧴", name: "욕실용품" },
          { icon: "📶", name: "와이파이" },
          { icon: "🍳", name: "취사가능" },
          { icon: "🎬", name: "VOD" },
          { icon: "🌿", name: "테라스" }
        ],
        images: [
          "./img/room1_1.jpg", "./img/room1_2.jpg", "./img/room1_3.jpg", "./img/room1_4.jpg", "./img/room1_5.jpg",
          "./img/room1_6.jpg", "./img/room1_7.jpg", "./img/room1_8.jpg", "./img/room1_9.jpg", "./img/room1_10.jpg"
        ]
      },
      2: {
        name: "두번째모험",
        badge: "독채 2동 · 시그니처 벽난로",
        baseGuests: 4,
        maxGuests: 6,
        weekdayPrice: 380000,
        weekendPrice: 420000,
        peakSurcharge: 50000,
        extraGuestFee: 20000,
        priceRange: "380,000 ~ 420,000원",
        metaRooms: "침실 2개 · 침대 2개 · 욕실 2개",
        metaTime: "입실 16:00 · 퇴실 11:00",
        desc: "모험담의 가장 큰 시그니처인 원형 벽난로가 있는 넓은 패밀리 리빙룸입니다. 가족 또는 소중한 친구들과 둘러앉아 따뜻한 불멍을 즐길 수 있습니다.",
        guide: "모험담의 가장 큰 시그니처인 원형 벽난로가 있는 넓은 패밀리 리빙룸입니다. 가족 또는 소중한 친구들과 둘러앉아 따뜻한 불멍과 함께 제주의 밤을 만끽해보세요.",
        config: [
          { title: "유형", value: "독채" },
          { title: "침실 2", value: "퀸 2" },
          { title: "욕실", value: "욕실 2" }
        ],
        amenities: [
          { icon: "🔥", name: "원형벽난로" },
          { icon: "📺", name: "OTT" },
          { icon: "🧴", name: "욕실용품" },
          { icon: "📶", name: "와이파이" },
          { icon: "🍳", name: "취사가능" },
          { icon: "☕", name: "커피머신" },
          { icon: "🌿", name: "테라스" }
        ],
        images: [
          "./img/room2_1.jpg", "./img/room2_2.jpg", "./img/room2_3.jpg", "./img/room2_4.jpg", "./img/room2_5.jpg",
          "./img/room2_6.jpg", "./img/room2_7.jpg", "./img/room2_8.jpg", "./img/room2_9.jpg", "./img/room2_10.jpg"
        ]
      },
      3: {
        name: "세번째모험",
        badge: "독채 3동 · 프리미엄 풀빌라",
        baseGuests: 4,
        maxGuests: 8,
        weekdayPrice: 400000,
        weekendPrice: 450000,
        peakSurcharge: 50000,
        extraGuestFee: 20000,
        priceRange: "400,000 ~ 450,000원",
        metaRooms: "침실 2개 · 침대 2개 · 욕실 2개",
        metaTime: "입실 16:00 · 퇴실 11:00",
        desc: "모험담에서 가장 프라이빗하고 넓은 최고급 독채 풀빌라입니다. 단독 프라이빗 수영장과 돌담 노천 온수 자쿠지, 야외 모닥불 화로대까지 완비되어 있습니다.",
        guide: "모험담에서 가장 프라이빗하고 고급스러운 단독 풀빌라 독채입니다. 단독 온수 수영장과 돌담 노천 온수 자쿠지, 야외 전용 모닥불 화로대까지 완비되어 사계절 힐링을 선사합니다.",
        config: [
          { title: "유형", value: "독채 풀빌라" },
          { title: "침실 2", value: "퀸 2" },
          { title: "욕실", value: "욕실 2" }
        ],
        amenities: [
          { icon: "🏊", name: "풀빌라" },
          { icon: "♨️", name: "노천자쿠지" },
          { icon: "🔥", name: "야외불멍" },
          { icon: "📺", name: "OTT" },
          { icon: "🧴", name: "욕실용품" },
          { icon: "📶", name: "와이파이" },
          { icon: "🍖", name: "바베큐" }
        ],
        images: [
          "./img/room3_1.jpg", "./img/room3_2.jpg", "./img/room3_3.jpg", "./img/room3_4.jpg", "./img/room3_5.jpg",
          "./img/room3_6.jpg", "./img/room3_7.jpg", "./img/room3_8.jpg", "./img/room3_9.jpg", "./img/room3_10.jpg"
        ]
      }
    };

    // 로컬 저장된 요금 설정 불러오기
    function loadRoomsConfig() {
      try {
        const saved = localStorage.getItem('moheomdam_custom_rooms');
        if (saved) {
          const parsed = JSON.parse(saved);
          return {
            1: Object.assign({}, DEFAULT_ROOMS[1], parsed[1] || {}),
            2: Object.assign({}, DEFAULT_ROOMS[2], parsed[2] || {}),
            3: Object.assign({}, DEFAULT_ROOMS[3], parsed[3] || {})
          };
        }
      } catch (e) {}
      return JSON.parse(JSON.stringify(DEFAULT_ROOMS));
    }

    let ROOMS = loadRoomsConfig();"""

if old_script_start != -1 and holidays_idx != -1:
    html = html[:old_script_start] + new_rooms_code + "\n\n    " + html[holidays_idx:]
    print("Updated DEFAULT_ROOMS successfully!")
else:
    print("Warning: Could not find DEFAULT_ROOMS markers!")

# 3. openRoomModal 함수 및 슬라이더 스크립트 업데이트
old_fn_start = html.find('function openRoomModal(roomId) {')
init_idx = html.find('// 초기화')

new_modal_js = """let currentModalRoomId = 1;
    let currentModalPhotoIdx = 0;

    function openRoomModal(roomId) {
      const data = ROOMS[roomId];
      if (!data) return;
      currentModalRoomId = roomId;
      currentModalPhotoIdx = 0;

      // 뱃지 및 제목/가격
      document.getElementById('roomBadge').innerText = data.badge;
      document.getElementById('roomTitle').innerText = data.name;
      document.getElementById('roomPrice').innerText = data.priceRange || `${data.weekdayPrice.toLocaleString()} ~ ${data.weekendPrice.toLocaleString()}원`;

      // 핵심 속성 3줄
      document.getElementById('roomMetaGuestsText').innerText = `독채, 기준 ${data.baseGuests}인 (최대 ${data.maxGuests}인) · 유료 ${data.baseGuests}인 초과시 추가요금`;
      document.getElementById('roomMetaRoomsText').innerText = data.metaRooms || '침실 1개 · 침대 1개 · 욕실 1개';
      document.getElementById('roomMetaTimeText').innerText = data.metaTime || '입실 16:00 · 퇴실 11:00';

      // 편의시설 그리드
      const amenGrid = document.getElementById('roomAmenitiesGrid');
      amenGrid.innerHTML = '';
      (data.amenities || []).forEach(a => {
        const item = document.createElement('div');
        item.className = 'flex flex-col items-center justify-center p-2.5 rounded-2xl bg-stone-50 border border-stone-100 hover:bg-stone-100 transition shadow-sm';
        item.innerHTML = `<span class="text-2xl mb-1">${a.icon}</span><span class="text-[11px] font-medium text-stone-700">${a.name}</span>`;
        amenGrid.appendChild(item);
      });

      // 구성 카드 3개
      const confGrid = document.getElementById('roomConfigCards');
      confGrid.innerHTML = '';
      (data.config || []).forEach(c => {
        const card = document.createElement('div');
        card.className = 'p-3.5 rounded-2xl bg-[#F8F7F4] border border-stone-200 text-center flex flex-col justify-center';
        card.innerHTML = `<div class="text-[11px] text-stone-500 font-medium mb-1">${c.title}</div><div class="text-xs sm:text-sm font-bold text-stone-900">${c.value}</div>`;
        confGrid.appendChild(card);
      });

      // 안내 텍스트
      document.getElementById('roomGuideText').innerText = data.guide || data.desc;

      // 사진 총 개수
      document.getElementById('roomPhotoTotal').innerText = data.images.length;

      // 썸네일 스트립 생성 (10장)
      const thumbBox = document.getElementById('roomThumbnails');
      thumbBox.innerHTML = '';
      data.images.forEach((imgSrc, idx) => {
        const thumb = document.createElement('img');
        thumb.src = imgSrc;
        thumb.className = `h-14 sm:h-16 w-20 sm:w-24 flex-shrink-0 object-cover rounded-xl cursor-pointer border-2 transition ${idx === 0 ? 'border-[#03C75A] opacity-100 scale-105' : 'border-transparent opacity-60 hover:opacity-100'}`;
        thumb.onclick = () => selectModalPhoto(idx);
        thumbBox.appendChild(thumb);
      });

      updateModalPhoto();

      document.getElementById('roomModal').classList.remove('hidden');
      document.getElementById('roomModal').classList.add('flex');
    }

    function selectModalPhoto(idx) {
      const data = ROOMS[currentModalRoomId];
      if (!data || !data.images) return;
      if (idx < 0) idx = 0;
      if (idx >= data.images.length) idx = data.images.length - 1;
      currentModalPhotoIdx = idx;
      updateModalPhoto();
    }

    function changeRoomModalPhoto(delta) {
      const data = ROOMS[currentModalRoomId];
      if (!data || !data.images) return;
      let nextIdx = currentModalPhotoIdx + delta;
      if (nextIdx < 0) nextIdx = data.images.length - 1;
      if (nextIdx >= data.images.length) nextIdx = 0;
      currentModalPhotoIdx = nextIdx;
      updateModalPhoto();
    }

    function updateModalPhoto() {
      const data = ROOMS[currentModalRoomId];
      if (!data || !data.images) return;
      const curImg = data.images[currentModalPhotoIdx];
      document.getElementById('roomMainImg').src = curImg;
      document.getElementById('roomPhotoIndex').innerText = currentModalPhotoIdx + 1;

      // 썸네일 active 스타일 반영
      const thumbBox = document.getElementById('roomThumbnails');
      Array.from(thumbBox.children).forEach((t, i) => {
        if (i === currentModalPhotoIdx) {
          t.className = 'h-14 sm:h-16 w-20 sm:w-24 flex-shrink-0 object-cover rounded-xl cursor-pointer border-2 transition border-[#03C75A] opacity-100 scale-105 shadow-sm';
          t.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        } else {
          t.className = 'h-14 sm:h-16 w-20 sm:w-24 flex-shrink-0 object-cover rounded-xl cursor-pointer border-2 transition border-transparent opacity-60 hover:opacity-100';
        }
      });
    }

    function closeRoomModal() {
      document.getElementById('roomModal').classList.remove('flex');
      document.getElementById('roomModal').classList.add('hidden');
    }

    """

if old_fn_start != -1 and init_idx != -1:
    html = html[:old_fn_start] + new_modal_js + html[init_idx:]
    print("Updated room modal JS functions successfully!")
else:
    print("Warning: Could not find openRoomModal markers!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished applying updates to Customer/260930-moheomdam-모험담/index.html!")
