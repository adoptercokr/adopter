
    // 1. 객실 기본 메타데이터
    
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

    let ROOMS = loadRoomsConfig();

    // 2. 대한민국 공식 공휴일 프리셋 (2025~2028년)
    const HOLIDAYS_PRESETS = {
      "2025-01-01": "신정",
      "2025-01-27": "설날(대체)",
      "2025-01-28": "설날",
      "2025-01-29": "설날",
      "2025-01-30": "설날",
      "2025-03-01": "삼일절",
      "2025-03-03": "대체공휴일",
      "2025-05-05": "어린이날/부처님오신날",
      "2025-05-06": "대체공휴일",
      "2025-06-06": "현충일",
      "2025-08-15": "광복절",
      "2025-10-03": "개천절",
      "2025-10-05": "추석",
      "2025-10-06": "추석",
      "2025-10-07": "추석",
      "2025-10-08": "대체공휴일",
      "2025-10-09": "한글날",
      "2025-12-25": "성탄절",

      "2026-01-01": "신정",
      "2026-02-16": "설날",
      "2026-02-17": "설날",
      "2026-02-18": "설날",
      "2026-03-01": "삼일절",
      "2026-03-02": "대체공휴일",
      "2026-05-05": "어린이날",
      "2026-05-24": "부처님오신날",
      "2026-05-25": "대체공휴일",
      "2026-06-06": "현충일",
      "2026-08-15": "광복절",
      "2026-08-17": "대체공휴일",
      "2026-09-24": "추석",
      "2026-09-25": "추석",
      "2026-09-26": "추석",
      "2026-10-03": "개천절",
      "2026-10-05": "대체공휴일",
      "2026-10-09": "한글날",
      "2026-12-25": "성탄절",

      "2027-01-01": "신정",
      "2027-02-06": "설날",
      "2027-02-07": "설날",
      "2027-02-08": "설날",
      "2027-02-09": "대체공휴일",
      "2027-03-01": "삼일절",
      "2027-05-05": "어린이날",
      "2027-05-13": "부처님오신날",
      "2027-06-06": "현충일",
      "2027-06-07": "대체공휴일",
      "2027-08-15": "광복절",
      "2027-08-16": "대체공휴일",
      "2027-09-14": "추석",
      "2027-09-15": "추석",
      "2027-09-16": "추석",
      "2027-10-03": "개천절",
      "2027-10-04": "대체공휴일",
      "2027-10-09": "한글날",
      "2027-10-11": "대체공휴일",
      "2027-12-25": "성탄절",

      "2028-01-01": "신정",
      "2028-01-26": "설날",
      "2028-01-27": "설날",
      "2028-01-28": "설날",
      "2028-03-01": "삼일절",
      "2028-05-02": "부처님오신날",
      "2028-05-05": "어린이날",
      "2028-06-06": "현충일",
      "2028-08-15": "광복절",
      "2028-10-02": "추석",
      "2028-10-03": "개천절/추석",
      "2028-10-04": "추석",
      "2028-10-05": "대체공휴일",
      "2028-10-09": "한글날",
      "2028-12-25": "성탄절"
    };

    function loadHolidays() {
      try {
        const saved = localStorage.getItem('moheomdam_holidays');
        return saved ? JSON.parse(saved) : Object.assign({}, HOLIDAYS_PRESETS);
      } catch (e) {
        return Object.assign({}, HOLIDAYS_PRESETS);
      }
    }

    let holidays = loadHolidays();

    // 상태 관리
    let currentRoomId = 1;
    let activePriceRoomId = 1;
    let selectedStartDate = null;
    let selectedEndDate = null;
    let guestCount = 2;
    let isAdmin = false;
    let calYear = new Date().getFullYear();
    let calMonth = new Date().getMonth(); // 0-indexed

    // 로컬 스토리지 기반 마감일 관리 (객실별 분리)
    function getBookedDates(roomId) {
      try {
        const stored = localStorage.getItem(`moheomdam_booked_room_${roomId}`);
        return stored ? JSON.parse(stored) : [];
      } catch (e) {
        return [];
      }
    }

    function saveBookedDates(roomId, dates) {
      localStorage.setItem(`moheomdam_booked_room_${roomId}`, JSON.stringify(dates));
    }

    // 1. 객실 선택 변경
    function selectRoomType(roomId) {
      currentRoomId = roomId;
      [1, 2, 3].forEach(id => {
        const btn = document.getElementById(`roomTab${id}`);
        const r = ROOMS[id];
        if (id === roomId) {
          btn.className = "py-2.5 px-2 rounded-xl text-xs font-serif-kr font-bold transition border-2 border-brand-accent bg-brand-cream text-stone-900";
        } else {
          btn.className = "py-2.5 px-2 rounded-xl text-xs font-serif-kr font-bold transition border-2 border-stone-200 bg-white text-stone-600 hover:border-stone-400";
        }
        btn.innerHTML = `${r.name}<br><span class="text-[10px] font-normal text-stone-500">${(r.weekdayPrice/10000)}만원/${r.baseGuests}인</span>`;
      });

      const room = ROOMS[roomId];
      document.getElementById('calcRoomName').innerText = room.name;
      document.getElementById('calcBaseGuests').innerText = `기준 ${room.baseGuests}인 / 최대 ${room.maxGuests}인`;
      guestCount = room.baseGuests;
      document.getElementById('calcGuests').innerText = guestCount;
      
      const notice = document.getElementById('calcNoticeRate');
      if (notice) {
        const peakText = (room.peakSurcharge && room.peakSurcharge > 0) ? ` · 성수기 할증 +${(room.peakSurcharge/10000)}만` : '';
        notice.innerText = `* 평일(월~목) ${room.weekdayPrice.toLocaleString()}원 / 주말·공휴일 ${room.weekendPrice.toLocaleString()}원${peakText}`;
      }

      renderCalendar();
      updateCalculation();
    }

    // 2. 달력 렌더링
    function renderCalendar() {
      const grid = document.getElementById('calGrid');
      grid.innerHTML = '';

      const monthNames = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"];
      document.getElementById('calCurrentMonth').innerText = `${calYear}년 ${monthNames[calMonth]}`;

      const firstDay = new Date(calYear, calMonth, 1).getDay();
      const lastDate = new Date(calYear, calMonth + 1, 0).getDate();
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const bookedDates = getBookedDates(currentRoomId);
      if (isAdmin) {
        const countEl = document.getElementById('adminBookedCount');
        if (countEl) countEl.innerText = bookedDates.length;
      }

      // 빈 날짜 채우기
      for (let i = 0; i < firstDay; i++) {
        const empty = document.createElement('div');
        empty.className = "h-11";
        grid.appendChild(empty);
      }

      for (let d = 1; d <= lastDate; d++) {
        const thisDate = new Date(calYear, calMonth, d);
        const dateStr = `${calYear}-${String(calMonth + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
        const isPast = thisDate < today;
        const isBooked = bookedDates.includes(dateStr);
        const isHoliday = !!holidays[dateStr];
        const dayOfWeek = thisDate.getDay();

        const dayEl = document.createElement('div');
        dayEl.className = "cal-day h-11 flex flex-col items-center justify-center rounded-xl text-xs relative cursor-pointer";
        
        // 날짜 텍스트
        let dayHtml = `<span>${d}</span>`;
        if (isHoliday) {
          dayHtml = `<span class="text-rose-600 font-bold">${d}</span><span class="text-[9px] text-rose-500 scale-90 leading-none truncate max-w-[40px]">${holidays[dateStr]}</span>`;
          dayEl.title = `공휴일: ${holidays[dateStr]}`;
        } else if (dayOfWeek === 0) {
          dayHtml = `<span class="text-rose-500 font-bold">${d}</span>`;
        } else if (dayOfWeek === 6) {
          dayHtml = `<span class="text-sky-600 font-bold">${d}</span>`;
        }
        dayEl.innerHTML = dayHtml;

        if (isPast) {
          dayEl.classList.add('disabled');
        } else if (isBooked) {
          dayEl.classList.add('booked');
          dayEl.title = isHoliday ? `[예약마감] 공휴일: ${holidays[dateStr]}` : "예약 마감";
          if (isAdmin) {
            dayEl.onclick = () => toggleAdminDate(dateStr);
          }
        } else {
          // 날짜 범위 표시
          if (selectedStartDate && dateStr === selectedStartDate) {
            dayEl.classList.add('selected');
          } else if (selectedEndDate && dateStr === selectedEndDate) {
            dayEl.classList.add('selected');
          } else if (selectedStartDate && selectedEndDate && dateStr > selectedStartDate && dateStr < selectedEndDate) {
            dayEl.classList.add('range');
          }

          dayEl.onclick = () => {
            if (isAdmin) {
              toggleAdminDate(dateStr);
            } else {
              onSelectDate(dateStr);
            }
          };
        }

        grid.appendChild(dayEl);
      }
    }

    // 3. 날짜 클릭 선택 (체크인/체크아웃)
    function onSelectDate(dateStr) {
      if (!selectedStartDate || (selectedStartDate && selectedEndDate)) {
        selectedStartDate = dateStr;
        selectedEndDate = null;
      } else if (selectedStartDate && !selectedEndDate) {
        if (dateStr <= selectedStartDate) {
          selectedStartDate = dateStr;
          selectedEndDate = null;
        } else {
          // 중간에 마감된 날이 있는지 확인
          const booked = getBookedDates(currentRoomId);
          let hasBlocked = false;
          let cur = new Date(selectedStartDate);
          const end = new Date(dateStr);
          while (cur < end) {
            const checkStr = cur.toISOString().split('T')[0];
            if (booked.includes(checkStr)) {
              hasBlocked = true;
              break;
            }
            cur.setDate(cur.getDate() + 1);
          }
          if (hasBlocked) {
            alert('선택하신 기간 사이에 이미 마감된 날짜가 포함되어 있습니다.');
            selectedStartDate = dateStr;
            selectedEndDate = null;
          } else {
            selectedEndDate = dateStr;
          }
        }
      }
      renderCalendar();
      updateCalculation();
    }

    function resetDates() {
      selectedStartDate = null;
      selectedEndDate = null;
      renderCalendar();
      updateCalculation();
    }

    // 4. 인원 변경
    function changeGuest(delta) {
      const room = ROOMS[currentRoomId];
      const next = guestCount + delta;
      if (next >= 1 && next <= room.maxGuests) {
        guestCount = next;
        document.getElementById('calcGuests').innerText = guestCount;
        updateCalculation();
      }
    }

    // 5. 견적 계산 (금·토·일 + 공휴일 + 성수기 할증 자동 합산)
    function updateCalculation() {
      const room = ROOMS[currentRoomId];
      if (!selectedStartDate) {
        document.getElementById('calcDates').innerText = "달력에서 날짜를 선택하세요";
        document.getElementById('calcNights').innerText = "0박 0일";
        document.getElementById('calcBasePrice').innerText = "0원";
        document.getElementById('calcExtraPrice').innerText = "0원";
        document.getElementById('calcTotalPrice').innerText = "0원";
        return;
      }

      if (!selectedEndDate) {
        document.getElementById('calcDates').innerText = `${selectedStartDate} (체크아웃 날짜 선택)`;
        document.getElementById('calcNights').innerText = "체크아웃 날짜 클릭";
        document.getElementById('calcBasePrice').innerText = "0원";
        document.getElementById('calcExtraPrice').innerText = "0원";
        document.getElementById('calcTotalPrice').innerText = "0원";
        return;
      }

      const start = new Date(selectedStartDate);
      const end = new Date(selectedEndDate);
      const diffTime = Math.abs(end - start);
      const nights = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

      document.getElementById('calcDates').innerText = `${selectedStartDate} ~ ${selectedEndDate}`;
      document.getElementById('calcNights').innerText = `${nights}박 ${nights + 1}일`;

      // 박수별 기본 요금 계산 (금, 토, 일 주말 및 공휴일 + 7·8월 성수기 할증)
      let baseTotal = 0;
      let cur = new Date(start);
      for (let i = 0; i < nights; i++) {
        const curStr = cur.toISOString().split('T')[0];
        const dayOfWeek = cur.getDay(); // 0(일)~6(토)
        const isHoliday = !!holidays[curStr];
        const isPeakMonth = (cur.getMonth() === 6 || cur.getMonth() === 7); // 7월, 8월

        let nightFee = 0;
        if (dayOfWeek === 0 || dayOfWeek === 5 || dayOfWeek === 6 || isHoliday) {
          nightFee = room.weekendPrice;
        } else {
          nightFee = room.weekdayPrice;
        }

        // 성수기 할증료 적용 (7·8월 또는 공휴일)
        if ((isPeakMonth || isHoliday) && room.peakSurcharge) {
          nightFee += room.peakSurcharge;
        }

        baseTotal += nightFee;
        cur.setDate(cur.getDate() + 1);
      }

      // 추가 인원 요금
      let extraTotal = 0;
      const extraFeePerPerson = room.extraGuestFee || 20000;
      if (guestCount > room.baseGuests) {
        const extraPersons = guestCount - room.baseGuests;
        extraTotal = extraPersons * extraFeePerPerson * nights;
      }

      const total = baseTotal + extraTotal;

      document.getElementById('calcBasePrice').innerText = `${baseTotal.toLocaleString()}원`;
      document.getElementById('calcExtraPrice').innerText = `${extraTotal.toLocaleString()}원`;
      document.getElementById('calcTotalPrice').innerText = `${total.toLocaleString()}원`;
    }

    // 6. 월 이동
    function prevMonth() {
      calMonth--;
      if (calMonth < 0) {
        calMonth = 11;
        calYear--;
      }
      renderCalendar();
    }
    function nextMonth() {
      calMonth++;
      if (calMonth > 11) {
        calMonth = 0;
        calYear++;
      }
      renderCalendar();
    }

    // 7. 관리자 기능 (비밀번호: 1316)
    function promptAdminLogin() {
      if (isAdmin) {
        logoutAdmin();
      } else {
        document.getElementById('adminLoginModal').classList.remove('hidden');
        document.getElementById('adminLoginModal').classList.add('flex');
        document.getElementById('adminPwdInput').value = '';
        document.getElementById('adminPwdInput').focus();
      }
    }
    function closeAdminLoginModal() {
      document.getElementById('adminLoginModal').classList.remove('flex');
      document.getElementById('adminLoginModal').classList.add('hidden');
    }
    function checkAdminPassword() {
      const pwd = document.getElementById('adminPwdInput').value;
      if (pwd === "1316") {
        isAdmin = true;
        closeAdminLoginModal();
        document.getElementById('adminBar').classList.remove('hidden');
        document.getElementById('adminBtnText').innerText = "관리자 로그아웃";
        renderCalendar();
      } else {
        alert("비밀번호가 올바르지 않습니다.");
      }
    }
    function logoutAdmin() {
      isAdmin = false;
      document.getElementById('adminBar').classList.add('hidden');
      document.getElementById('adminBtnText').innerText = "호스트 관리자 모드";
      renderCalendar();
    }
    function toggleAdminDate(dateStr) {
      let booked = getBookedDates(currentRoomId);
      if (booked.includes(dateStr)) {
        booked = booked.filter(d => d !== dateStr);
      } else {
        booked.push(dateStr);
      }
      saveBookedDates(currentRoomId, booked);
      renderCalendar();
    }

    // 8. 관리자 요금 및 성수기 설정 모달 제어
    function openPriceSettingModal() {
      switchPriceModalRoom(currentRoomId);
      document.getElementById('priceSettingModal').classList.remove('hidden');
      document.getElementById('priceSettingModal').classList.add('flex');
    }
    function closePriceSettingModal() {
      document.getElementById('priceSettingModal').classList.remove('flex');
      document.getElementById('priceSettingModal').classList.add('hidden');
    }
    function switchPriceModalRoom(roomId) {
      activePriceRoomId = roomId;
      [1, 2, 3].forEach(id => {
        const tab = document.getElementById(`priceTab${id}`);
        if (id === roomId) {
          tab.className = "py-2.5 rounded-xl text-xs font-bold transition bg-amber-500 text-stone-900 shadow";
        } else {
          tab.className = "py-2.5 rounded-xl text-xs font-bold transition bg-stone-800 text-stone-300 hover:bg-stone-700";
        }
      });
      const room = ROOMS[roomId];
      document.getElementById('cfgWeekday').value = room.weekdayPrice;
      document.getElementById('cfgWeekend').value = room.weekendPrice;
      document.getElementById('cfgPeak').value = room.peakSurcharge || 0;
      document.getElementById('cfgBaseGuests').value = room.baseGuests;
      document.getElementById('cfgMaxGuests').value = room.maxGuests;
      document.getElementById('cfgExtraGuestFee').value = room.extraGuestFee || 20000;
    }
    function savePriceConfig() {
      const room = ROOMS[activePriceRoomId];
      room.weekdayPrice = parseInt(document.getElementById('cfgWeekday').value) || room.weekdayPrice;
      room.weekendPrice = parseInt(document.getElementById('cfgWeekend').value) || room.weekendPrice;
      room.peakSurcharge = parseInt(document.getElementById('cfgPeak').value) || 0;
      room.baseGuests = parseInt(document.getElementById('cfgBaseGuests').value) || room.baseGuests;
      room.maxGuests = parseInt(document.getElementById('cfgMaxGuests').value) || room.maxGuests;
      room.extraGuestFee = parseInt(document.getElementById('cfgExtraGuestFee').value) || 20000;

      localStorage.setItem('moheomdam_custom_rooms', JSON.stringify(ROOMS));
      selectRoomType(currentRoomId);
      closePriceSettingModal();
      alert(`[${room.name}] 요금 및 성수기 설정이 성공적으로 저장되었습니다!`);
    }
    function resetDefaultConfig() {
      if (confirm('모든 객실의 요금 설정을 초기 기본값으로 복원하시겠습니까?')) {
        localStorage.removeItem('moheomdam_custom_rooms');
        ROOMS = JSON.parse(JSON.stringify(DEFAULT_ROOMS));
        switchPriceModalRoom(activePriceRoomId);
        selectRoomType(currentRoomId);
        alert('기본값으로 복원되었습니다.');
      }
    }

    // 9. 관리자 공휴일 및 성수기 관리
    function openHolidaySettingModal() {
      renderHolidayList();
      document.getElementById('holidaySettingModal').classList.remove('hidden');
      document.getElementById('holidaySettingModal').classList.add('flex');
    }
    function closeHolidaySettingModal() {
      document.getElementById('holidaySettingModal').classList.remove('flex');
      document.getElementById('holidaySettingModal').classList.add('hidden');
    }
    function renderHolidayList() {
      const box = document.getElementById('holidayListContainer');
      box.innerHTML = '';
      const keys = Object.keys(holidays).sort();
      document.getElementById('holidayCountText').innerText = keys.length;

      keys.forEach(dateStr => {
        const row = document.createElement('div');
        row.className = "flex justify-between items-center bg-stone-800/80 px-3 py-2 rounded-xl border border-stone-700/60";
        row.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="font-mono text-amber-300 font-bold">${dateStr}</span>
            <span class="text-stone-300">${holidays[dateStr]}</span>
          </div>
          <button onclick="deleteHoliday('${dateStr}')" class="text-stone-500 hover:text-red-400 transition text-xs">삭제</button>
        `;
        box.appendChild(row);
      });
    }
    function syncHolidaysByYear(year) {
      let count = 0;
      Object.keys(HOLIDAYS_PRESETS).forEach(dateStr => {
        if (dateStr.startsWith(String(year))) {
          holidays[dateStr] = HOLIDAYS_PRESETS[dateStr];
          count++;
        }
      });
      localStorage.setItem('moheomdam_holidays', JSON.stringify(holidays));
      renderHolidayList();
      renderCalendar();
      updateCalculation();
      alert(`${year}년 공식 공휴일 ${count}개가 달력에 업데이트되었습니다!`);
    }
    function syncAllHolidaysPreset() {
      if (confirm('2025~2028년 전체 네이버 공식 공휴일을 동기화하시겠습니까?')) {
        holidays = Object.assign({}, HOLIDAYS_PRESETS);
        localStorage.setItem('moheomdam_holidays', JSON.stringify(holidays));
        renderHolidayList();
        renderCalendar();
        updateCalculation();
        alert('전체 연도 공휴일이 완벽히 동기화되었습니다!');
      }
    }
    function addNewHoliday() {
      const date = document.getElementById('newHolidayDate').value;
      const name = document.getElementById('newHolidayName').value.trim();
      if (!date || !name) {
        alert('날짜와 공휴일 명칭을 모두 입력해 주세요.');
        return;
      }
      holidays[date] = name;
      localStorage.setItem('moheomdam_holidays', JSON.stringify(holidays));
      document.getElementById('newHolidayDate').value = '';
      document.getElementById('newHolidayName').value = '';
      renderHolidayList();
      renderCalendar();
      updateCalculation();
      alert(`[${date} ${name}] 공휴일이 추가되었습니다.`);
    }
    function deleteHoliday(dateStr) {
      delete holidays[dateStr];
      localStorage.setItem('moheomdam_holidays', JSON.stringify(holidays));
      renderHolidayList();
      renderCalendar();
      updateCalculation();
    }
    function clearAllHolidays() {
      if (confirm('등록된 모든 공휴일을 삭제하시겠습니까?')) {
        holidays = {};
        localStorage.setItem('moheomdam_holidays', JSON.stringify(holidays));
        renderHolidayList();
        renderCalendar();
        updateCalculation();
      }
    }

    // 10. 마감일정 복사 & 불러오기
    function copyBookedDates() {
      const booked = getBookedDates(currentRoomId);
      if (booked.length === 0) {
        alert(`현재 [${ROOMS[currentRoomId].name}]에 등록된 마감 일정이 없습니다.`);
        return;
      }
      navigator.clipboard.writeText(booked.join(', ')).then(() => {
        alert(`[${ROOMS[currentRoomId].name}] 마감 일정 총 ${booked.length}개가 클립보드에 복사되었습니다!`);
      }).catch(() => {
        prompt('마감 일정 목록을 복사하세요:', booked.join(', '));
      });
    }
    function promptImportBookedDates() {
      const input = prompt(`[${ROOMS[currentRoomId].name}]에 추가할 마감 날짜들을 붙여넣어 주세요:\n(형식: 2026-10-05, 2026-10-06 등)`);
      if (!input) return;
      const matches = input.match(/\d{4}-\d{2}-\d{2}/g);
      if (!matches || matches.length === 0) {
        alert('유효한 날짜(YYYY-MM-DD) 형식을 찾을 수 없습니다.');
        return;
      }
      let booked = getBookedDates(currentRoomId);
      let added = 0;
      matches.forEach(d => {
        if (!booked.includes(d)) {
          booked.push(d);
          added++;
        }
      });
      saveBookedDates(currentRoomId, booked);
      renderCalendar();
      alert(`총 ${added}개의 마감 날짜가 달력에 추가 반영되었습니다!`);
    }

    // 11. 단순 사진 모달 & 객실 상세 모달
    function openModal(src) {
      document.getElementById('modalImg').src = src;
      document.getElementById('imgModal').classList.remove('hidden');
      document.getElementById('imgModal').classList.add('flex');
    }
    function closeModal() {
      document.getElementById('imgModal').classList.remove('flex');
      document.getElementById('imgModal').classList.add('hidden');
    }

    let currentModalRoomId = 1;
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

      // 편의시설 그리드 (단색/흑백 미니멀 라인 SVG 아이콘 적용 - 조잡한 컬러 이모지 배제)
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

    // 초기화
    window.addEventListener('DOMContentLoaded', () => {
      selectRoomType(1);
    });
  