import re

file_path = "Customer/260930-moheomdam-모험담/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Swap #calendar-section and #gallery
cal_start = content.find('<!-- 5. 🌟 대화형 실시간 예약 달력')
cal_end = content.find('<!-- 6. Space Gallery')
gal_start = cal_end
gal_end = content.find('<!-- 7. Location & Contact Section -->')

if cal_start != -1 and cal_end != -1 and gal_end != -1:
    cal_block = content[cal_start:cal_end].strip()
    gal_block = content[gal_start:gal_end].strip()

    # Rename section headers numbers in comments
    gal_block = gal_block.replace('<!-- 6. Space Gallery', '<!-- 5. Space Gallery')
    cal_block = cal_block.replace('<!-- 5. 🌟 대화형 실시간 예약 달력', '<!-- 6. 🌟 대화형 실시간 예약 달력')

    # Swapped
    new_middle = f"{gal_block}\n\n  {cal_block}\n\n  "
    content = content[:cal_start] + new_middle + content[gal_end:]
    print("Successfully swapped #gallery and #calendar-section!")
else:
    print("Warning: Section markers not found for swap!")

# 2. Update Room Modal HTML with Naver Place style
old_modal_start = content.find('<!-- 10. 객실 상세 모달')
old_modal_end = content.find('<!-- 11. 관리자 비밀번호 입력 모달 -->')

new_modal_html = """<!-- 10. 객실 상세 모달 (네이버 플레이스 100% 동일 스타일) -->
  <div id="roomModal" class="fixed inset-0 z-50 bg-black/85 hidden items-center justify-center p-2 sm:p-4 backdrop-blur-md overflow-y-auto">
    <div class="bg-white rounded-3xl max-w-xl w-full overflow-hidden shadow-2xl relative my-auto text-left max-h-[92vh] flex flex-col">
      <!-- 닫기 버튼 -->
      <button onclick="closeRoomModal()" class="absolute top-4 right-4 z-30 w-9 h-9 rounded-full bg-black/60 hover:bg-black/80 text-white flex items-center justify-center text-xl font-light transition shadow-lg">
        &times;
      </button>

      <!-- 스크롤 가능 컨테이너 -->
      <div class="overflow-y-auto flex-1 pb-4">
        <!-- 1. 사진 슬라이더 (10장) + 1/10 뱃지 + 좌우 넘김 버튼 -->
        <div class="relative aspect-[16/10] bg-stone-900 overflow-hidden select-none group">
          <img id="roomMainImg" src="" alt="객실 사진" class="w-full h-full object-cover transition duration-300">
          
          <!-- 좌우 넘김 화살표 -->
          <button onclick="changeRoomModalPhoto(-1)" class="absolute left-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full bg-black/50 hover:bg-black/80 text-white flex items-center justify-center text-lg transition shadow-md">‹</button>
          <button onclick="changeRoomModalPhoto(1)" class="absolute right-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full bg-black/50 hover:bg-black/80 text-white flex items-center justify-center text-lg transition shadow-md">›</button>

          <!-- 1 / 10 뱃지 -->
          <div class="absolute bottom-3 right-3 px-3 py-1 rounded-full bg-black/70 backdrop-blur-md text-[11px] text-white font-mono font-medium tracking-wider shadow">
            <span id="roomPhotoIndex">1</span> / <span id="roomPhotoTotal">10</span>
          </div>

          <!-- 좌측 상단 독채 뱃지 -->
          <div class="absolute top-4 left-4 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white font-serif-kr text-xs font-medium" id="roomBadge">
            독채
          </div>
        </div>

        <!-- 썸네일 스트립 (10장) -->
        <div class="flex gap-1.5 p-2 bg-stone-100 overflow-x-auto scrollbar-thin" id="roomThumbnails"></div>

        <!-- 2. 본문 내용 (네이버 캡쳐 완벽 구현) -->
        <div class="p-6 sm:p-7 space-y-6 text-stone-900">
          <!-- 객실명 & 가격 & Npay+ -->
          <div>
            <div class="flex items-center gap-2 mb-1">
              <h3 class="font-serif-kr text-2xl font-bold text-stone-900" id="roomTitle">첫번째모험</h3>
              <span class="text-stone-400 text-xs">▼</span>
            </div>
            <div class="flex items-center gap-2 mb-3">
              <span class="font-serif-kr text-2xl font-bold text-stone-900" id="roomPrice">350,000 ~ 400,000원</span>
              <span class="px-2 py-0.5 rounded bg-[#03C75A]/15 text-[#03C75A] font-bold text-[11px] flex items-center gap-0.5">
                <span class="font-black text-xs">N</span>pay+
              </span>
            </div>

            <!-- 핵심 속성 3줄 (네이버 스타일) -->
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
            </div>
          </div>

          <!-- 네이버 탭 바 -->
          <div class="grid grid-cols-3 text-center text-xs font-bold font-serif-kr border-b border-stone-200">
            <button class="py-2.5 text-stone-400 hover:text-stone-700">예약하기</button>
            <button class="py-2.5 text-stone-900 border-b-2 border-stone-900">정보</button>
            <button class="py-2.5 text-stone-400 hover:text-stone-700">리뷰 <span class="text-brand-wood font-mono">5</span></button>
          </div>

          <!-- 편의시설 아이콘 그리드 (네이버 캡쳐와 동일) -->
          <div>
            <h4 class="font-bold text-sm text-stone-900 mb-3">편의시설</h4>
            <div class="grid grid-cols-4 sm:grid-cols-7 gap-2.5 text-center" id="roomAmenitiesGrid">
              <!-- JS 동적 렌더링 -->
            </div>
          </div>

          <!-- 소개 / 구성 카드 3개 -->
          <div>
            <h4 class="font-bold text-sm text-stone-900 mb-1">소개</h4>
            <span class="text-xs font-bold text-stone-700 block mb-3">구성</span>
            <div class="grid grid-cols-3 gap-3" id="roomConfigCards">
              <!-- 카드 3개 (유형 / 침실 / 욕실) -->
            </div>
          </div>

          <!-- 안내 텍스트 -->
          <div class="pt-4 border-t border-stone-100">
            <h4 class="font-bold text-sm text-stone-900 mb-2">안내</h4>
            <p class="text-xs sm:text-sm text-stone-700 leading-relaxed font-serif-kr" id="roomGuideText">
              외부의 자연을 넘나들 수 있는 개방감 있는 공간으로 반려견 동반이 가능한 객실입니다.
            </p>
          </div>
        </div>
      </div>

      <!-- 하단 고정 예약 바 -->
      <div class="p-4 border-t border-stone-200 bg-white flex gap-3">
        <a href="https://m.place.naver.com/accommodation/1716272359/booking" target="_blank" class="flex-1 py-3.5 rounded-2xl bg-[#03C75A] hover:bg-[#02b350] text-white font-bold text-sm text-center transition flex items-center justify-center gap-2 shadow-md hover:shadow-lg active:scale-[0.99]">
          <span class="font-black text-base">N</span>
          <span>네이버 예약하기</span>
        </a>
        <button onclick="closeRoomModal()" class="px-6 py-3.5 rounded-2xl bg-stone-100 hover:bg-stone-200 text-stone-700 text-xs font-semibold transition">닫기</button>
      </div>
    </div>
  </div>\n\n  """

if old_modal_start != -1 and old_modal_end != -1:
    content = content[:old_modal_start] + new_modal_html + content[old_modal_end:]
    print("Successfully updated Room Modal HTML!")
else:
    print("Warning: Room modal markers not found!")

# 3. Update room cards in Section 4 to show "사진 10장 보기 +" and use room1_1.jpg thumbnails
content = re.sub(r'사진 \d+장 보기 \+', '사진 10장 보기 +', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully!")
