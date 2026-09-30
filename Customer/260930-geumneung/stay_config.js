const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/2000699781/home",
  phone: "0507-1423-0976",
  name: "금능여관",
  subtitle: "Premium Stay",
  description: "머묾, 그 자체가 온전한 쉼이 되는 공간",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20250627_212%2F1750987575650ypEE6_JPEG%2FKakaoTalk_20250603_230753005_02_%25281%2529.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250627_217%2F1750986425615okVTJ_JPEG%2FKakaoTalk_20250605_111705786_03.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA4MjdfMjcg%2FMDAxNzg3ODEyMjUzNDA3.M97snUrPqSzcaj7IC8bj5QkAYkHH8N5dH8GMZZEaJiog.CFyutOuFmxBIQc90HZDEkq4na5YdkCWse8GRQUUeQQAg.JPEG%2Fthumbnail-2AD4BCE3-6141-4BE7-B7A6-8DABC422B0B2.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA2MDNfMTE3%2FMDAxNzgwNDcyNTM0MzYz.O2SBfq3qqm_R_JO0mL9L5ZNONPXGseNFI6DEZmTH6Hog.C00UfyMauQnhcJmxASm2YGyPyxskQLaA5LkA6TwLxKYg.JPEG%2Fimage.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250627_204%2F17509864009705XjwB_JPEG%2FKakaoTalk_20250603_230753005_04.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250627_205%2F1750986385119dA2Wv_JPEG%2FKakaoTalk_20250603_230753005_01_%25281%2529.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA5MjBfNDkg%2FMDAxNzg5ODcwODk4OTM5.PA9IwiBJ5eXUMlgRUMp478fdGLkmLXBfyxNuMP5Tp2Yg.QxPXEL2Yrf_W4yZb7O7i-986iTGPYa6hfvrKx0_ger4g.JPEG%2FC782DB9D-346E-4908-A399-15A23CA10CAF.jpeg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MThfMTQw%2FMDAxNzg5NzMyNjMwODcw.UP2lSiEkJFQcOnhUJmToVqr0Fbz_bngNhy039gvcEOcg.Tx4Ex9983dApg5ZByAJbnjbS8887LTy1Ax5MRpRGCvQg.JPEG%2F900_20260828_164944.jpg%2F900x1200" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fblogpfthumb-phinf.pstatic.net%2FMjAyNDA3MTdfMjEz%2FMDAxNzIxMTc5NzMyMjcy.rAOd4ASWEZ8ebygbyfbcCY6uXbBr9WrnqD3IPwtDh0Yg.ZkEcLeqTr5s0yZd0j4eWLiekLo0POk5mtpS5OpQGYCog.JPEG%2F%25EA%25B8%25B0%25EC%25A1%25B4%25EC%258D%25B8%25EB%2584%25A4%25EC%259D%25BC.jpg%2F%25EA%25B8%25B0%25EC%25A1%25B4%25EC%258D%25B8%25EB%2584%25A4%25EC%259D%25BC.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MThfMTAz%2FMDAxNzg5NzMyNjM1NTg3.7_u5e5QzLmCqzBkL8UMJLmp3lUA7V6ewaODdF0aT6j8g.VDw8hT5isEOj9ZZ4vzvPUPjH0zyYbgxFQB3O_vjfpMwg.JPEG%2F900_20260828_175101.jpg%2F900x1200" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MThfOTEg%2FMDAxNzg5NzMyNjMzNzQ1.ZqrnOU5XOgWP3VOhNiIouDViVH9qFRfrv-03ZZEu5Asg.TKhgopd0ORaquN9BDubSATZUd57Tnjw2l9Le90rQGowg.JPEG%2F900_20260829_101630.jpg%2F900x1200" },
    { id: "s12", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MThfMjg4%2FMDAxNzg5NzMyNjMyMzI2.3VNwSRtYcXDRCOkjCnFexFMNIUCIlXfLp-LWqi_JJrMg.rL15Xwvsg2Uh149LvKlGnoWsaaVBHjoQwIL3cEJ3Lisg.JPEG%2F900_20260828_165528.jpg%2F900x1200" },

  ],
  facilities: [
    { name: "와이파이", icon: "wifi" }
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
