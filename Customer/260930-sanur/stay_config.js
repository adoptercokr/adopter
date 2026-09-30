const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/2036409548/home",
  phone: "0507-1360-4845",
  name: "사누르제주",
  subtitle: "Premium Stay",
  description: "여행 중에 정말 기대했던 숙소인데 기대 이상으로 너무 좋았고 완전 힐링했습니다!! 개인 풀빌라 숙소 가고 싶어서 선택했는데 수영장도 물놀이 하기 너무 좋았고 옆에 바로 자쿠지...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251106_67%2F1762398954018zcDeb_JPEG%2FDSC_6318.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251106_82%2F1762398953716SgGes_JPEG%2FDSC_6329.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251106_249%2F1762398953835h4sLV_JPEG%2FDSC_6255.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251121_20%2F1763717054704y7BKw_JPEG%2F20251101_134739.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDlfMTYg%2FMDAxNzgzNjAwMTg1NzAz.Yu99xt0ZCbS2pbmU5N_0fNYoYcX5YU-N6DTVEGPNkNYg.L-yq1MkO_irLbF3kCWVMn3_C62OgHJ-uWWIWVwmMJbkg.JPEG%2Foutput%25EF%25BC%25BF392678371.jpg%2F900x1200" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogpfthumb-phinf.pstatic.net%2FMjAyMzExMTBfMTc1%2FMDAxNjk5NTk0NzU4NjY0.QSDdCnQudJ0dZ8G_T8daLhRQ1rsFLsb4O6sZDNRSERAg.Cezv-Eb97zLuiZp_xyVjWmvVn0gB5OQHuIOlGk-A1I0g.JPEG.dana5689%2F%25EA%25BF%2580%25EB%25B2%258C%25EB%25A3%25A8%25ED%2594%25BC.jpg%2F%25EA%25BF%2580%25EB%25B2%258C%25EB%25A3%25A8%25ED%2594%25BC.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDdfMTU2%2FMDAxNzgzNDE5ODgyNDY3.c7EbyF-t2KETrnWkN-Aa0b8KlonlG7UmPztNUfom-K4g.IMUHHXealtnFHC-iO0pZj2K_lQeEtzlXsdhCoYTU9Skg.JPEG%2FIMG%25EF%25BC%25BF8334.jpg%2F900x1200" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDdfMjg2%2FMDAxNzgzNDE5ODkwNzc4.ZxZ9MR3Rsi7HnrIh03mFujGQrHTdqOo_xtu5KDWU7v4g.BTcURN9HiJf3BEQa0ioIdrbSOxvxStH7Y7ZQfRi2uswg.JPEG%2FIMG%25EF%25BC%25BF8346.jpg%2F900x1200" },

  ],
  facilities: [
    { name: "개별샤워실", icon: "wifi" },
    { name: "자쿠지", icon: "wifi" },
    { name: "개별화장실", icon: "wifi" },
    { name: "수영장", icon: "wifi" },
    { name: "풀빌라", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "2인실", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "반려동물 동반 불가"
  ],
  rates: {
    weekday: "0",
    weekend: "0",
    peak: "0"
  }
};
