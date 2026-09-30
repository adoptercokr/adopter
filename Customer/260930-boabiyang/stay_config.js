const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/1631444549/home",
  phone: "0507-0000-0000",
  name: "보아비양",
  subtitle: "Premium Stay",
  description: "머묾, 그 자체가 온전한 쉼이 되는 공간",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180420_165%2F1524212717123a8AWE_JPEG%2FEiU7f8uZLQQiVDCThaQTWIfQ.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230420_221%2F1681983785344LQHkp_JPEG%2F049.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA2MDlfNCAg%2FMDAxNzgxMDA4MzYyMjcy.xSu15AyQbxyoKYizz9U7kdybjnWIpXY_txPzxwUMFjwg.GLYDE_Geq6zU1k5hXRgesrJyWrZpsCdwMxXbKFDsOHUg.JPEG%2FPublishThumb_20260609_213220_309.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180420_11%2F152421271536150Ph3_JPEG%2F4dRQWyVp0pBYt431cDZ6Sy_s.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180420_223%2F1524212717371pgUy9_JPEG%2F2NcwFTDgeMGBHHU4fmbCTLRj.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDRfNDYg%2FMDAxNzgzMTM5ODU3MTAz.W2bLD3ncVjWoV20W-MGt7N_Ouhzf0SjmKtrzW_7wnsog.uJnrRtk3MSyYmY6UTGEJYu1pQpChfxhBEodUQP72Wfkg.JPEG%2F%25EC%25A0%259C%25EC%25A3%25BC%25EB%258F%2584_%25EC%2598%25A4%25EC%2585%2598%25EB%25B7%25B0_%25EC%2588%2599%25EC%2586%258C_%25EB%25B3%25B4%25EC%2595%2584%25EB%25B9%2584%25EC%2596%2591_%25ED%259B%2584%25EA%25B8%25B0_(108).jpg%2F3000x4000" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MTJfMTMy%2FMDAxNzgzODY0MDA1MjQy.Eo9PGycOvFSjZnT-en8MRzOYQQeRv_wi6M_9rJITuXUg.Bfq3nP1GuRxL1kWgr3pEPUQerLrJvzNtt3NwCgfy2Pkg.JPEG%2FIMG_4099.JPG%2F5184x3456" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDRfMjM2%2FMDAxNzgzMTM5NzM1Njcw.i5Z0LGhQqExa0pR5DC0z6qmH4m0p1qxof18fVuY4DdMg.qFJZq1JwwgKDr6sCn0JW4FSKzWm7pvMs6VXIcFLJZhwg.JPEG%2F%25EC%25A0%259C%25EC%25A3%25BC%25EB%258F%2584_%25EC%2598%25A4%25EC%2585%2598%25EB%25B7%25B0_%25EC%2588%2599%25EC%2586%258C_%25EB%25B3%25B4%25EC%2595%2584%25EB%25B9%2584%25EC%2596%2591_%25ED%259B%2584%25EA%25B8%25B0_(103).jpg%2F3000x4000" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDRfMjEy%2FMDAxNzgzMTQwMTg0Mjc3.jIFui80lZopI4w5v1gjgpYeeee77couSvHRWvYRPUtUg.lMF9pw8cfCtSINR3G_-xnb9aUmyjOAlVblqxCUUlEs0g.JPEG%2F%25EC%25A0%259C%25EC%25A3%25BC%25EB%258F%2584_%25EC%2598%25A4%25EC%2585%2598%25EB%25B7%25B0_%25EC%2588%2599%25EC%2586%258C_%25EB%25B3%25B4%25EC%2595%2584%25EB%25B9%2584%25EC%2596%2591_%25ED%259B%2584%25EA%25B8%25B0_(133).jpg%2F4000x3000" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MDRfMjA0%2FMDAxNzgzMTQwMjUwODM5.oicm3nMr7e9w4DxfK6L4wnvlPJYpyxLMwseujrgofUEg.YGK-boDN3zG3yhWQMDRLZBjtxW_8aPdxc0JNhkmIZNkg.JPEG%2F%25EC%25A0%259C%25EC%25A3%25BC%25EB%258F%2584_%25EC%2598%25A4%25EC%2585%2598%25EB%25B7%25B0_%25EC%2588%2599%25EC%2586%258C_%25EB%25B3%25B4%25EC%2595%2584%25EB%25B9%2584%25EC%2596%2591_%25ED%259B%2584%25EA%25B8%25B0_(140).jpg%2F2190x2920" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fpup-post-phinf.pstatic.net%2FMjAyNjA4MTdfMTAy%2FMDAxNzg2OTQwMTAzMzgz.XmA03YnEY0Hxrs5JoYKr4nCIFPKZviK_AiBiujYekl8g.WV-FkqjIEi4n_sMO17XfMpM0IyAEoI8c8LUCcZm9ZMkg.JPEG%2FPOST_IMAGE_ENC_20260817_131435_043.jpg" },
    { id: "s12", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA2MDlfNCAg%2FMDAxNzgxMDA4MzYyMjcy.xSu15AyQbxyoKYizz9U7kdybjnWIpXY_txPzxwUMFjwg.GLYDE_Geq6zU1k5hXRgesrJyWrZpsCdwMxXbKFDsOHUg.JPEG%2FPublishThumb_20260609_213220_309.jpg" },
    { id: "s13", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA0MjJfMjk0%2FMDAxNzc2ODY5NzY5OTcy.jJmQfPdVdpUxBCha7WWT7dK23d3AXKfKWrarwiqmxX0g.zBICQOv2QGvOro1HO4uHgCaKeryY7XKoVA6WknU4zPIg.JPEG%2FPublishThumb_20260422_235553_254.jpg" },
    { id: "s14", mainImage: "https://clip-service-phinf.pstatic.net/MjAyNjAxMTVfMjIz/MDAxNzY4NDg2MjcwNjk1.DawyeU7Dpoa3ToVHqEUzZs4Am-kOJKJJGpk2oYgjGUkg.ccEgF_l8H2r98qYYGYtyk9BsbU0WuEKWPUQ69rja1V0g.JPEG/2018-05-01-21-49-04.jpg" },
    { id: "s15", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNTExMDNfMTc1%2FMDAxNzYyMTc1NDU0MTI2.QIaGKlJolJU-w9jYU_36fJZ48a0ICCp5FwN7a68S1Hgg.Ved6ZShJqOfKk_Hfh6qJDAi5Q2b8QEzI5rvY7_O6aAQg.JPEG%2FPublishThumb_20251103_221039_009.jpg" },

  ],
  facilities: [
    { name: "와이파이", icon: "wifi" },
    { name: "독채", icon: "wifi" },
    { name: "조식제공", icon: "wifi" }
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
