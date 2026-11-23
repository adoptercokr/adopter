const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/1202686132/home",
  phone: "070-4376-6476",
  name: "삼척 미갈루 풀빌라",
  subtitle: "동해 바다의 푸른 숨결을 마주하는 독채 풀빌라",
  description: "삼척의 청정한 바다를 한눈에 담는 오션뷰 프라이빗 풀빌라입니다. 사계절 개별 온수풀과 스파, 그리고 모던한 휴양 인테리어를 자랑합니다.",
  address: "강원특별자치도 삼척시 근덕면 삼척로 2132",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240220_234%2F1708395249329tNyEw_JPEG%2F21.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240220_61%2F1708395573123e0xTE_JPEG%2F6.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA2MTNfMTk5%2FMDAxNzgxMjc5ODAzNzM0.D_zwBCmoWi9K-igrWYUqVKiWP4w_QwpJmkFKPcX1v2Eg.H8CA9Okvp7dkt1wLx2MGrRBfskMiK8IYfVKNb5NMOmAg.JPEG%2Fthumbnail-1C407843-F4C7-4418-A46E-3695341BB5E3.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240220_148%2F1708395573393pBEeI_JPEG%2F7.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240220_14%2F1708395573082pqVUR_JPEG%2F4.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA1MThfNzgg%2FMDAxNzc5MDc1NTM1NzY1.VVyNIu7xQkvoNbprZwadpcilP26UgaMhiIKzmtAaRvcg.LQEpLHv-HqTcLPtyKL0gUNj0UdROoiQ7Ift5_URfbKwg.JPEG%2F34A8217B-AE41-428B-B54A-AD462095AF0F.jpeg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfMTU4%2FMDAxNzkzMDc1NTkzNTAz.GdgFhejbXNJGvRPHamRsWm_A-m082CajP3a_OvxGOwUg.f5Drvdh7aLhYY9wJV46O5wzPXQNz52NzH8FSp2khw4Qg.JPEG%2F20261025_160123.jpg.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfMTA4%2FMDAxNzkzMDc1NTkzNDky.IMmjttjPNAUIkma0WDXUE52n-9ztdxqGiOgvFBvmIlIg.jUP9A7jU7QYEXAja8l5sDPFORRbkEA_k9AT6XHbAhm8g.JPEG%2F20261025_160014.jpg.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjBfNTcg%2FMDAxNzkyNTA1MTI5OTA5.xK42szsm_4-Dg3Did5EDydKMGTqcUmpLphjTd-XEDE4g.cmRrcaPA9XorSCGqcDtwYiW26kssv3J7ZCeebuwe_Z0g.JPEG%2F1792504753310.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjBfMjEg%2FMDAxNzkyNTA1MTI5OTQ2.2vKovaEpmzxlSX1xUpA_CWL46vN8vpO-JpnQJxNZ2kIg.TIP8JxJwW-E_Ty-HbdLcS3VVZ-J9Qe2kdC26cOG9Kmcg.JPEG%2F1792504753526.jpg" }
  ],
  facilities: [
    { name: "오션뷰온수풀", icon: "wifi" },
    { name: "프라이빗스파", icon: "wifi" },
    { name: "동해바다전망", icon: "wifi" },
    { name: "개별바베큐", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "호텔식어메니티", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "410,000",
    weekend: "492,000",
    peak: "553,500"
  }
};
