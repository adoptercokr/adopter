const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/1185001387/home",
  phone: "0507-1384-4214",
  name: "모노가든",
  subtitle: "Premium Stay",
  description: "머묾, 그 자체가 온전한 쉼이 되는 공간",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241025_21%2F1729831876950DbBRw_JPEG%2FScreenshot_2024-10-25_at_11.48.47.JPG" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241025_234%2F17298318777188bcMw_JPEG%2FScreenshot_2024-10-25_at_11.49.10.JPG" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241025_53%2F1729831877645V7lLN_JPEG%2FScreenshot_2024-10-25_at_11.49.25.JPG" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241025_275%2F1729831877438wyVM3_JPEG%2FScreenshot_2024-10-25_at_11.49.32.JPG" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMjMw%2FMDAxNzkwMjIzNjg1MDg5.L17He3OUPJiTT7QTusulGzUIGR5u6VVD6iYVX1cMUXUg.p2mSqo4Z1fAf4dYx13KAVMOgcRhqOaqZLX8g2gX5fNkg.GIF%2F3251293220.gif%2F282x500" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMTA2%2FMDAxNzkwMjIzNjI4NTgx.LNrY0VuXBNNgzLfTbLHJwtGGMXAYWYWduJGVak1O9Ycg.RH49D3aHGe7Y8_5OImo6r2HRX1akfFIEFxuQowEc1_kg.JPEG%2FIMG%25EF%25BC%25BF2006.jpg%2F900x1200" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMjc2%2FMDAxNzkwMjIzNjI4MDMw.mO9nDalwqbhmXQ-dQnkg2LAdXyUrXnheAhBny13Fn1Ag.5dTbWn8DEQABW73VZ7KBArsJio2_aRzeJjoYUmMPswcg.JPEG%2FIMG%25EF%25BC%25BF1996.jpg%2F900x676" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMTk3%2FMDAxNzkwMjIzNjI4Nzc0.tbF9isMs4IKuQ79kBWjhO7yakL_P67k0DONao5q1L_Qg.w1-eehnb3BHDXhv-EX50w-czpmaW-aYK6o7QCbvgUA0g.JPEG%2FIMG%25EF%25BC%25BF2007.jpg%2F900x676" },

  ],
  facilities: [
    { name: "스파", icon: "wifi" },
    { name: "모던", icon: "wifi" },
    { name: "개별샤워실", icon: "wifi" },
    { name: "개별화장실", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
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
