const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/1293795324/home",
  phone: "0507-1393-4399",
  name: "후아힌협재 풀빌라",
  subtitle: "Premium Stay",
  description: "제주애월 풀빌라, 후아힌협재 추천 해외 감성 숙소 미온수풀 제주도여행",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20260416_110%2F1776314254644oHz0l_JPEG%2Fimage.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20260416_248%2F1776314257662IorCK_JPEG%2Fimage.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20260416_240%2F1776314256271hBbyS_JPEG%2Fimage.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20260416_150%2F1776314259097dAg0H_JPEG%2Fimage.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fvideo-phinf.pstatic.net%2F20250728_153%2F1753656841835ui0pU_JPEG%2FbqxifewG1D_03.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fphinf.pstatic.net%2Fcontact%2F20210104_257%2F1609735567302wcMdA_JPEG%2Fimage.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjJfMjYg%2FMDAxNzkwMDgzMDA4OTY0.hfks19ThesIMqqx6Z76kETWwluPxexwaY0-w2J2xbmgg.Yfhtbzildx1ZzsTABMhF1lIkvYnJ4DiQ9I7yVTH5twUg.JPEG%2FIMG%25EF%25BC%25BF7421.jpg%2F900x1200" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogpfthumb-phinf.pstatic.net%2FMjAyNjAzMThfMTcg%2FMDAxNzczNzg4ODYyNzkx.knW7cmqyi29T1LpJQodV3H88PBy50hWznW9RjfM7oikg.Rb-8QY7p9YxMmK-iIOb9WZcH92bnsxmPg56ldnQTQpkg.JPEG%2Fbc721c688b683c4c30bbd31d04731a59.jpg%2Fbc721c688b683c4c30bbd31d04731a59.jpg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjJfMTI2%2FMDAxNzkwMDgzMDE1ODU4.eCdMQOXEa9QShqCjonTPT62XqWcVFKiWIKgthR3QMYgg.nczPPG7ssEdCiowNodMFEvMnzlfmViHBegvTxGld-KEg.JPEG%2FIMG%25EF%25BC%25BF7434.jpg%2F900x1200" },
    { id: "s12", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjJfMTA2%2FMDAxNzkwMDgzMDI1NzM5.k1_UL-f17brYCfycvRmTcF11UcmTPXW7dvNvKJH69eQg.op0MX2XSTFtAg2ZiiVSTLcE4lL4ukqqJEjz8k1l-zGQg.JPEG%2FIMG%25EF%25BC%25BF7487.jpg%2F900x1200" },
    { id: "s13", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjJfMTE2%2FMDAxNzkwMDgzMDQ4NDk5.lCJeipekbenoUmpjwOkoINEpA4BI2z0SxnXjQo63M5gg.5ELZWEjfeFTg3araVrdUSo9H8EhQn9A8bvlahavq9Q4g.JPEG%2FIMG%25EF%25BC%25BF7414.jpg%2F900x1200" },
    { id: "s14", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20240911_145%2F1726055561101gyvbB_JPEG%2F%25BC%25F6%25BF%25B5%25C0%25E57.jpg" },
    { id: "s15", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20240911_116%2F1726055554995TM2Fr_JPEG%2F%25B0%25C5%25BD%25C72.jpg" },

  ],
  facilities: [
    { name: "모던", icon: "wifi" },
    { name: "개별샤워실", icon: "wifi" },
    { name: "자쿠지", icon: "wifi" },
    { name: "개별화장실", icon: "wifi" },
    { name: "수영장", icon: "wifi" },
    { name: "바비큐장", icon: "wifi" },
    { name: "풀빌라", icon: "wifi" },
    { name: "침대방", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "반려동물 동반 불가"
  ],
  rates: {
    weekday: "400,000",
    weekend: "400,000",
    peak: "400,000"
  }
};
