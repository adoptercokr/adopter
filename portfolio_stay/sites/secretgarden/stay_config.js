const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/1138391385/home",
  phone: "0507-1329-8733",
  name: "강릉 비밀의정원 풀빌라",
  subtitle: "사천해변 인근 프라이빗 가든 럭셔리 스테이",
  description: "사계절 따뜻한 개별 온수풀과 초록빛 정원이 어우러진 강릉의 감성 독채 풀빌라입니다. 사랑하는 사람들과 오붓하고 소중한 시간을 보낼 수 있습니다.",
  address: "강원특별자치도 강릉시 사천면 해안로 1064",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260413_146%2F1776060261505xaPuD_JPEG%2FKakaoTalk_20260409_122231207.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221228_65%2F1672203231866BEAnY_JPEG%2F1.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20260525_167%2Fj5glh_1779711579757pn8l2_JPEG%2Fthumbnail-06A3D821-272F-45F0-8047-1FC095EDE357.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221228_25%2F1672203231872rPe7c_JPEG%2F3.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221228_198%2F1672203231885sVTpw_JPEG%2F5.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjVfMjI5%2FMDAxNzkyOTE3NzU2MTQ2.m_GNu9U3MMFSl5IiQJ-rb2GoFqFGvNpQQfuHFBNaeYwg.Hsxf0ZlAelDBOv9AjHutcQb6uRJ1S_H87R1pe5c5bM0g.JPEG%2F20261025_172555.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjVfMTU2%2FMDAxNzkyOTE3NzU2NDc3.7amaWGGCFrhPr8gIo2o00UpIejGPE_F4cMpBY10Ua-cg.aNfNT2v5WofKfIjF5WpmkK0yEiGaOVFIxjaDXOSROLQg.JPEG%2F20261025_141326.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjVfMTkw%2FMDAxNzkyOTE3NzUwNDgx.u9pRce4TLsEJQmVxsuaG45P0u5BG3W5ciDzxRFdh0FMg.z3lqpVHzHGFbew4R3SfxWI_bbJOIxUa85phubka9G-0g.JPEG%2F1792917648334.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjVfMTcz%2FMDAxNzkyOTE3NzQ0NzY2.InsHk0W4-GHzgT9b89cZBuoi78AgwX_qwpwdExUglgcg.Bsl8odChK-Iyv8M6eRC2REBPhNGOFv17iczpNzNkBe0g.JPEG%2F20261025_141325.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjVfMjM0%2FMDAxNzkyOTE3NzQ0NjU3.hi7SD86XF3uk0vjBJ_L8oK-gV41u9n_iPq0Vbq7w7Kog.lwovI8_UaBlVuotLXfM5gJ731oYc4hCRVi0khXquqrQg.JPEG%2F20261025_141316.jpg" }
  ],
  facilities: [
    { name: "실내개별온수풀", icon: "wifi" },
    { name: "사천해변인접", icon: "wifi" },
    { name: "가든정원", icon: "wifi" },
    { name: "단독바베큐", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "스마트TV", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "390,000",
    weekend: "468,000",
    peak: "526,500"
  }
};
