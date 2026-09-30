const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/160795798/home",
  phone: "0507-1497-1007",
  name: "하루를품다",
  subtitle: "Premium Stay",
  description: "1. 제주공항 출발 시: 평화로(1135번 도로)를 타고 서귀포 방향으로 약 35분 직진 후 동광교차로에서 안덕 중문 방면 우측 진입, 동광본동로 표지판을 따라 오시면 됩니다...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240528_287%2F1716872857915NMkYg_JPEG%2F%25C8%25AD%25B8%25E9_%25C4%25B8%25C3%25B3_2024-05-28_140723.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190105_180%2F1546674554051qQcUf_JPEG%2F2.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20240516_137%2F742o7_1715832509577DqS9J_JPEG%2F64769CA7-8350-4C3A-9CC0-561AC6DEDAF6.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNTA4MTJfNDcg%2FMDAxNzU0OTMwMDE2ODEz.bZV4WNtGRgUMHOgwPnCgjI1rPmZtPsWmsQr-2YZPfNgg.KLdYN0DJkMTsNH4dqx0NFvSdB5X_Uw82O76DtaJr-Qkg.JPEG%2Fimage.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_104%2F1785344942074jqoFq_JPEG%2Fa-1.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_152%2F1785344958303Vxj76_JPEG%2Fa-8.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA2MDVfNzMg%2FMDAxNzgwNjI1ODUyOTUz.IWe7CyaNvn20eEhWvqxsM3Rb6GLoK3Us46wD8pV8wqog.176TgI49nwlK8bAedNOmbH63JVGZLCZO7mHieoaEvbog.JPEG%2FKakaoTalk_20260605_111644715.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA2MDVfMjQ2%2FMDAxNzgwNjI1ODUzMDE1.6M3MiqZQpxs9nfLN8-oZ_RmOZiFxH23cDKAbm-I4xTQg.qqGQ3DPb1iZfbyE02jXFEOFn1Osl52KWVkE8bZgn3N0g.JPEG%2FKakaoTalk_20260605_111644715_03.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA2MDVfMjA3%2FMDAxNzgwNjI1ODUyODc5.B1Wn60y1wgRjWDiYylgAKypsBAa5mXgp5b6kkLJ_LwYg.nSLSGJD30BTQV2dSyetW2lO5KY0WQDOoJXQcOXOA_N8g.JPEG%2FKakaoTalk_20260605_111644715_01.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA2MDVfOTMg%2FMDAxNzgwNjI1ODUyOTc2.uMrU8Xw5d3nhtFf4i_L24lsRh6OyP7Qyg9SZXOlcOfgg.OlXAv5hZzVBPHF5yUZDGQ4D8eL14L2vfK7nxUXJeisAg.JPEG%2FKakaoTalk_20260605_111644715_02.jpg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA2MDVfMjQx%2FMDAxNzgwNjI1ODU1OTU1.NoB2G4Vak554sYUH7NuJCWw3EHDABFMTj9Z_OQqy0qIg.j5GlTGWTlWwHa1NKGoDLbMaQaj5e1e6TM8QtJ5VKqX0g.JPEG%2FKakaoTalk_20260605_111644715_06.jpg" },

  ],
  facilities: [
    { name: "파티", icon: "wifi" },
    { name: "모던", icon: "wifi" },
    { name: "장기숙박", icon: "wifi" },
    { name: "개별바비큐", icon: "wifi" },
    { name: "수영장", icon: "wifi" },
    { name: "바비큐장", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "풀빌라", icon: "wifi" }
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
