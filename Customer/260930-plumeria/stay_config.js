const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/38729145/home",
  phone: "0507-1411-8705",
  name: "플루메리아 펜션",
  subtitle: "Premium Stay",
  description: "[자차_렌터카 이용 시] 네이버 지도에 플루메리아 펜션 or 애월해안로 476 검색  [대중 교통이용] 1. 택시 : 제주공항에서 20분소요. 약 15,000원. 2. 버스 ...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20230805_82%2F1691233056126C5vO3_JPEG%2F230725%25BE%25D6%25BF%25F9-%25C7%25C3%25B7%25E7%25B8%25DE%25B8%25AE%25BE%25C6%25281920px%2529DSC03094.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250315_218%2F1741997796007DAdUl_JPEG%2F20220504_103325.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20230805_199%2F1691233056433jz8ul_JPEG%2F230725%25BE%25D6%25BF%25F9-%25C7%25C3%25B7%25E7%25B8%25DE%25B8%25AE%25BE%25C6%25281920px%2529DSC03087.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250315_73%2F1741997812286T1SFj_JPEG%2F20230725_182326.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fvideo-phinf.pstatic.net%2F20241003_125%2F1727914714622YCDeO_JPEG%2FoTuvXe0HdP_03.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MjZfNzIg%2FMDAxNzg3Njk2Mzg5ODA0.cD8QKSCRU_cl5Q3Q6emkvHg-rfHh-RznVLFYBRniCf0g.6VGv7SH1XdLl0shfbaShnmIlsujXWt_BuTma1227HR8g.JPEG%2FF9ABE8B3-6D78-44ED-AF4E-CB8D79962154.jpeg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MjZfMjg2%2FMDAxNzg3Njk2Mzg5OTY1.jYAxGJRcvg-9TKh0F_pKPQazQx5ylsFnKAlgvtiAHGog.fnyWOwZWtqSVJgZ_DeZX19MaJSQqCbseZ_9u8CrjVWUg.JPEG%2FDBAB764B-DBB1-4875-A1AE-F5EC8E719F05.jpeg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MjZfMTcz%2FMDAxNzg3Njk2Mzg4NjY0.cILK0Vy8ksPkkxxNHxxCZxYyOUj6Cqvv6tbkNtMylZEg.DTy3QLCOqbjm7x31ALrMbz-O1Wi4WUuTAPMkS52LGbog.JPEG%2F0EAC22E8-121D-48C6-B10C-A95AEA8D2D6C.jpeg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MjZfNjEg%2FMDAxNzg3Njk2Mzg4Nzk1.ZHayfkod3lJkBoCkeUfn9P2uTc-zhSKsS0R_b1DYR54g.fWss0-prOxD_t6_qrJ-7ir4nm4ruAyF6LpaghQtJbfkg.JPEG%2FF138EE27-5751-42A4-9DBA-7C2F219B43F8.jpeg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA1MjZfMTEw%2FMDAxNzc5NzgzNDQxNTI0.9a8Rs4JsOT4TXKzOfGLmIg2KRvVnAWabQhSM0nw2cBkg.kidS_OM2Kg3M0WUKwo1ahuy0hkQuhWE86Ur6KhzYuQEg.JPEG%2F20260425_121206.jpg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Fcontact%2F20211007_247%2F1633607039333iFGam_JPEG%2Fimage.jpg" },

  ],
  facilities: [
    { name: "스파", icon: "wifi" },
    { name: "모던", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "2인실", icon: "wifi" },
    { name: "잔디", icon: "wifi" },
    { name: "장기숙박", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "반려동물 동반 불가"
  ],
  rates: {
    weekday: "69,000",
    weekend: "69,203",
    peak: "69,203"
  }
};
