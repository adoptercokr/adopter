const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/1771698587/home",
  phone: "0507-1433-3558",
  name: "강릉 나로부터 풀빌라",
  subtitle: "발리의 이국적인 감성을 담은 독채 온수풀빌라",
  description: "강릉 사천의 평온한 풍경 속 이국적인 감성을 자아내는 프라이빗 풀빌라입니다. 야외 온수풀과 대형 빔프로젝터로 특별한 낭만을 선물합니다.",
  address: "강원특별자치도 강릉시 사천면 방동길 302",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230428_243%2F1682657402972hx6v4_JPEG%2F001.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230428_94%2F1682657403071Qwc3Q_JPEG%2F002.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20260826_77%2Fbw3v0_1787747864653dvNGu_JPEG%2Fthumbnail-9200AF4A-93AC-4492-9906-F8FDD8279FC0.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230428_267%2F16826574029592RX5D_JPEG%2F003.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230428_18%2F1682657384010bTWYt_JPEG%2F001.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fvideo-phinf.pstatic.net%2F20250225_100%2F17404743088613IQzW_JPEG%2FFgT2UYdrV1_03.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MDVfMTY1%2FMDAxNzg1OTMyMzI1MTI2.BvIh5anISHttZZMjitZf7pvJktpmlmujJHFgbcMG-LMg.YK8HDS53Jing0C2DK5GLexvI_udXSSnoKzcgFd_Pt3og.JPEG%2F20260803_194950.jpg.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MDVfNzkg%2FMDAxNzg1OTMyMzI1MTU4.e8YiHDtOFVx4moJHWKlYl-uoumTp8JMWMgdgi5tNFPQg._V7qUaI9refGBUu70agalZHNBOjFt29WMOyvyYcbDC8g.JPEG%2F20260803_194923.jpg.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MzBfMjYg%2FMDAxNzg1NDA2NTg1MTMy.tvRA17qYK4LjoihAfFNMr1Tn0l_Fzqs00ZNimNn5ABMg.fYfbP3-JVw5ktclUjN6MvKNfR8hvXMsXx67dvuiWukkg.JPEG%2F900_20260725_154951.jpg%2F900x675" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA3MzBfMjEw%2FMDAxNzg1Mzk1ODg5ODQ4.2F2sF2gVns49lTSV_oGNBxntUpPITSN4Rw2LdOMffYsg.IWnsM038TKBtNvEdrKjZbPaTWmiuBSuG-gP9r4CtD9sg.JPEG%2F900_20260725_152724.jpg%2F900x1200" }
  ],
  facilities: [
    { name: "사계절온수풀", icon: "wifi" },
    { name: "야외빔프로젝터", icon: "wifi" },
    { name: "발리풍인테리어", icon: "wifi" },
    { name: "개별바베큐", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "어메니티", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "420,000",
    weekend: "504,000",
    peak: "567,000"
  }
};
