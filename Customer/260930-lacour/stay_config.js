const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/37550280/home",
  phone: "064-747-5553",
  name: "흰수염고래리조트",
  subtitle: "Premium Stay",
  description: "제주시 애월읍 구엄리에 위치한 키즈펜션&가족펜션&카페입니다. 제주공항에서 20분 거리에 위치하며, 애니멀스토리하우스 외 다양한 객실과 야외수영장, 베이커리카페가 있는 리조트입니다.",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260913_54%2F1789297522207dh31B_JPEG%2F01_%25BC%25F6%25BF%25B5%25C0%25E5_%25B4%25EB%25C7%25A5.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260913_141%2F1789297522042vuQg2_JPEG%2F02_%25BD%25BA%25C5%25C4%25B4%25D9%25B5%25E5%25B4%25F5%25BA%25ED_%25B4%25EB%25C7%25A5.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260913_237%2F1789297522079D2WtU_JPEG%2F03_%25C5%25B0%25C1%25EE%25BD%25BA%25C0%25A7%25C6%25AE_%25B4%25EB%25C7%25A5.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260913_235%2F17892975220261nOla_JPEG%2F04_%25C6%25D0%25B9%25D0%25B8%25AE%25BD%25BA%25C0%25A7%25C6%25AE_%25B4%25EB%25C7%25A5.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MzFfMjc5%2FMDAxNzg4MTM3Nzc3OTU0.gsO3UwU_7tVwWJfFEJW2Q7hHF7Ek6F8MUYMtn2lTzcog.drd0aA8IwgC7xXo57yUhdMBZRAhQQh3ml4is1CT0pSQg.JPEG%2FKakaoTalk_20260831_094309665_02.jpg%2F5712x4284" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MzFfMjc5%2FMDAxNzg4MTM4ODM2NjQ2.rGwH4S0whhKzwvun2IOPF0KMBrW0dsa0J6-YvKOiH1kg.OBXuQh-lg8kiHIGTMnURdhfBTX7A61DcYfJMPQHKk0Mg.GIF%2F3243459683.gif%2F282x500" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MzFfMTQ4%2FMDAxNzg4MTM3Nzk2NzYx.5yj_Rss1b_4JbEBil4ERAnDjZm6gVM6LPhHUifnMgB0g._SmQQyLOQxaTaaYoknpDskaH1jDZ-3kwEXWQ4jbNas8g.JPEG%2FKakaoTalk_20260831_094309665_19.jpg%2F4284x5712" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MzFfMTky%2FMDAxNzg4MTM3Nzk4NzY5.nPkkdXg_LX6gu12o1QjfUuZniz1Z7-LLJNfuffj8YMEg.ExxLTH3nOSk3rUFwapE3TSvsfqmGl2trrsupUh8Rr-Yg.JPEG%2FKakaoTalk_20260831_094309665_21.jpg%2F4284x5712" },

  ],
  facilities: [
    { name: "disabledFriendlyParking", icon: "wifi" }
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
