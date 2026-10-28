const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/1418295993/home",
  phone: "0507-1384-5993",
  name: "프라이빗양양 독채 풀빌라",
  subtitle: "오산해수욕장 프라이빗 힐링 독채 스테이",
  description: "양양의 푸른 바다와 자연을 오롯이 누릴 수 있는 단독 독채 풀빌라입니다. 넓은 수영장과 정갈한 인테리어로 온전한 프라이버시를 보장합니다.",
  address: "강원특별자치도 양양군 손양면 선사유적로 260",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210612_120%2F1623458065446d1Lbo_JPEG%2FPYY_82.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210612_299%2F1623458065335rSLVg_JPEG%2FPYY_86.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210612_266%2F1623458065400usSSV_JPEG%2FPYY_80.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210612_147%2F1623458065362KhRUv_JPEG%2FPYY_84.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfMTU2%2FMDAxNzc2OTAwNjQxNTc3.tMN4WHklbMD98ddPiQWVa12XCs49SgrkRVB3g-OUOZMg.OsJo2I7yPexyM_8R1lgphPBzu3-ybxKuvM7lepH99AUg.JPEG%2F03_final.jpg%2F1917x1077" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfMjc3%2FMDAxNzc2OTAwNjQxNTgw.WjL9qC12ZJwasq1sd0bP5a-QOqZn0WK3bo0JLFjKu4gg.nmD_TKI6KdG6tmtk6NG_9maeRm_zcuTr6rBicVI4_OAg.JPEG%2F02_final.jpg%2F1917x1080" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfMTM4%2FMDAxNzc2OTAwNjQxNjQy.hggCdsa1znoVmHOK1gKruV9GuZDdusmv-pRS5oolurIg.BaK1HIeALgwAFKA6uR3DXxBw4uvRcFIrYoMgJd3d-Xwg.JPEG%2F01_final.jpg%2F1920x1078" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfOTkg%2FMDAxNzc2OTAwNjQ5MTgy.ui6MSYUsUKSPRELvgTt3pWkTLaWLmNSxxmnfu3AWqoEg.6Gh9pe4wAxI6Tw_5oJY5zPbKlxk3BHsCaREJi-DyG5sg.JPEG%2F04_final.jpg%2F1918x1078" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfMTYw%2FMDAxNzc2OTAwNjU5Mzgz.iXixE-Jh_1CojadGh1q5_h0VuIt-uJp0ncBXNh6ahO0g.tSZNOnDCfom-Qx9uYp0jwhvl3B_gtJ2_5t8ZWXvJHW8g.JPEG%2F02_final.jpg%2F1918x1077" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA0MjNfMjM4%2FMDAxNzc2OTAwNjU5Mzg3.eMvbkwnnaxRVHeyQRukVxWqr5gAnmUBJ3UITNDc6s1Ug.MveZVIE1wZyRLfEeBaH1zu5-gykwn2yNAaVc-AiAKF8g.JPEG%2F01_final.jpg%2F1918x1077" }
  ],
  facilities: [
    { name: "단독전용수영장", icon: "wifi" },
    { name: "오산해변도보", icon: "wifi" },
    { name: "프라이빗마당", icon: "wifi" },
    { name: "개별바베큐", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "주차완비", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "480,000",
    weekend: "576,000",
    peak: "648,000"
  }
};
