const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/1730925405/home",
  phone: "0504-0904-2309",
  name: "스테이1미터",
  subtitle: "Premium Stay",
  description: "제주의 서쪽, 용수리 마을에 위치한 스테이1미터(STAY1METER)는 초록 들판 사이로 바다와 차귀도 섬을 마주한 집입니다. 멀리서 보면 주변의 억새와 밀밭 사이에 낮게 떠...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190710_197%2F1562744215347gb2GX_JPEG%2F65kumeXq_RZiLuUQlhSGW3sL.jpeg.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190710_209%2F1562744238216qIEnn_JPEG%2FMKaIRZBc3wRusvvIpd1HgkTE.jpeg.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190710_185%2F1562744302163nT6Be_JPEG%2FjrQY8MI26MUOgDyjNou1lgzk.jpeg.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_96%2F1581587791393w3LLd_JPEG%2FKakaoTalk_20190221_193845254_10.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_205%2F1581587791387U02yI_JPEG%2FKakaoTalk_20190221_193845254_11.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_8%2F1581587791404F5LBV_JPEG%2FKakaoTalk_20190221_193845254_21.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_91%2F1581587791386YDJY9_JPEG%2FKakaoTalk_20190221_193845254_12.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_151%2F1581587791404oTofO_JPEG%2FKakaoTalk_20190221_193845254_13.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_234%2F1581587791369heKro_JPEG%2FKakaoTalk_20190221_193845254_15.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200213_75%2F15815877913965sC9k_JPEG%2FKakaoTalk_20190221_193845254_16.jpg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f48_48&src=http%3A%2F%2Fblogpfthumb.phinf.naver.net%2F20131016_182%2Fstomp100_1381933740794pSHfs_JPEG%2Fimage1.jpg" },
    { id: "s12", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f180_180&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA2MTVfMjUw%2FMDAxNzQ5OTY0NTAzMDkz.Gk4QOIXSuCs8marlEzWLv5Au2KmEIBq_OygaDX_SD10g.Vtnej36B-copIjy73uLhDe5yAU53XAUU8GhRPH2uXxwg.JPEG%2F20250531_183733.jpg%233000x1689" },
    { id: "s13", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f180_180&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTAxMjBfMTgy%2FMDAxNTQ3OTUyOTY5NDU3.0L3mb1hcRU-1it_LXIfD2gosd2YZM8tdoLhoD6nSIDkg.IQVIJhkgBXT5i_RltJrHpMCWUmUuCn-ZoeFZVn-8wDsg.JPEG.archiry%2F031.jpg%23886x590" },
    { id: "s14", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f48_48&src=http%3A%2F%2Fblogpfthumb.phinf.naver.net%2F20140930_234%2Fsilpisi77_1412073884079AqJKG_JPEG%2FIMG_0361.JPG" },
    { id: "s15", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f180_180&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAyMjNfMjY4%2FMDAxNzA4NjU1NzM5MjAx.nOh-6zrzYxy16DiWE2JHMawZWiFQS09Az_gPI7_QNhYg.q0pgR5z3SlXJfF-12dgxM2ljZT2q4xeOhcCHqYf_ZiYg.JPEG%2F20231023_173826.jpg%231688x2251" },

  ],
  facilities: [
    { name: "무선 인터넷", icon: "wifi" },
    { name: "주차장", icon: "wifi" },
    { name: "독채", icon: "wifi" }
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
