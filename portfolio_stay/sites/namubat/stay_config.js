const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/1159898766/home",
  phone: "0507-1335-9876",
  name: "홍천 나무밭",
  subtitle: "숲속의 고요한 독채 노천탕 스테이",
  description: "강원도 홍천의 맑은 숲속에 둘러싸인 프라이빗 독채 숙소입니다. 사계절 야외 노천탕과 따스한 불멍, 온전한 쉼을 위한 완벽한 독립 공간을 제공합니다.",
  address: "강원특별자치도 홍천군 영귀미면 궁터길 14",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20240204_39%2F1707057974755IMof0_JPEG%2F%25C6%25E6%25BC%25C7-1947.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210918_275%2F1631971357684EjXIG_JPEG%2Fop4zP0gK3BKbgXOS4uOdZoJo.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA5MjhfNjQg%2FMDAxNzkwNTcwNTk5MDcx.myCoOw_mwZOE1kr60H51XFzwWzH5wFfNy9uf-Hucte8g.xTWV3QgRsxhGzzOsQcIJQ4oZXbRL2DpuwAJr7XNskbcg.JPEG%2FPublishThumb_20260928_134313_446.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210918_218%2F1631971397537TlzKj_JPEG%2Frgfqatba0vWWOJE0HnXC-rTb.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20240204_251%2F17070579762809Y0nK_JPEG%2F%25C6%25E6%25BC%25C7-1800.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTZfMzAw%2FMDAxNzgxNjEwNTkwMjk2.S1x0u_qJzbj1fTPcGcbnkwSF9s0vcdvjd3EkOTK9qq8g.UqgCxWv5Y1d1bqKBrPVVINNAibFzpe_JViJV5XnESP8g.JPEG%2F900_20260508_160039.jpg%2F900x900" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTZfMjIg%2FMDAxNzgxNjA5NjcxNDIz.f2t6tLyA-X44jyBKiZD1qTV747IIkzzbt5_fLl5vx_Yg.gJkZ4GCuiNpyjWTNm4IuMwXp_UrrKxOeEzHS2M_vMGMg.JPEG%2F900_20260508_154913.jpg%2F864x486" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTZfMTk5%2FMDAxNzgxNjA5NjY3MDY3.Gi6Py8yoFOQ8OwzrW2Szilc_fghx7kwMUrFY4r52UTYg.VA7kUsmvtVcCzKEx5BKgY7XN00h4PaGPveWvvPtLTUgg.JPEG%2F900_20260508_164906.jpg%2F900x507" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTZfOSAg%2FMDAxNzgxNjA5NjczNTY2.OpX_n67IxQDypaV6GxHVJcMaZ-NoprCQqWwOuBXWSfcg.0tmrpAgxoZO86DGKppYEtpvzMIgn6UfooE17QCqxcncg.JPEG%2F900_20260508_165937.jpg%2F900x1350" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTZfMjE5%2FMDAxNzgxNjEwNTU5NTk5.DN6Q51Mxxi7v6GhAjK2hSsbbSgkHCXQBY-cMxDaOi0Ag.86E0AOfvrH0zFHVTWdrexQFk0MWMPVeQL7AXKHmyFawg.JPEG%2F900_20260509_001422_(1).jpg%2F900x507" }
  ],
  facilities: [
    { name: "야외노천탕", icon: "wifi" },
    { name: "단독바베큐", icon: "wifi" },
    { name: "불멍존", icon: "wifi" },
    { name: "독채전용정원", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "호텔식침구", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "380,000",
    weekend: "456,000",
    peak: "513,000"
  }
};
