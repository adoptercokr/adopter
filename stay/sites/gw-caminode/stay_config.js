const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/1956080428/home",
  phone: "0507-1484-0534",
  name: "까미노데플로레스타",
  subtitle: "홍천강을 품은 하이엔드 부티크 풀빌라",
  description: "숲으로 가는 길이라는 의미를 담은 부티크 풀빌라입니다. 홍천강의 수려한 자연을 바라보며 프라이빗 온수풀과 이국적인 휴식을 만끽할 수 있습니다.",
  address: "강원특별자치도 홍천군 북방면 도사곡길 201",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200503_5%2F15884807481746YKao_JPEG%2F4.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250327_93%2F1743075825731Sk1pF_JPEG%2F_PAC3381.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjEwMjRfMjE1%2FMDAxNzkyODQ3MTA0NzA0.mefnFTZmmaiP2-5-U5c5RIRe9DyUT0wiLpoKKSccgHsg.bo_ZrqCT2vLpTmVqAQCXUZj_gO2KSCm05bo3WtYt2wUg.JPEG%2FPublishThumb_20261024_220048_829.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200503_264%2F1588480748173wfAIw_JPEG%2F8.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200503_32%2F1588480748181PIlXh_JPEG%2F4.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjhfMjQz%2FMDAxNzkzMTQzOTQwMTIy.ev1HkeK1nKUtwxCiiVCX1eqBui97xJQz2CapqLTQaBgg.6IH2olUn_C3FBjDomosNoMRfSvmyttIT95SIiPNszgQg.JPEG%2Fvideo_thumbnail.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjhfNyAg%2FMDAxNzkzMTY0Nzc0NTE3.olI07AXENRzZ1jiIDmWNJfILwQ1QxQ6DlZf61UfcdLUg.R_wKtxqLz7dl-MkklMcAgKweUEG18twj4BTb2F7a2Ngg.JPEG%2F42621.jpg.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMjRfMTcy%2FMDAxNzkyODMyNDgxMjc5.QiaPuAlEWVAo_IvtSZnvwd_6YMSY3in7AhJ2bJnCJJkg.WNacqpcn6frpbTI15P0sOUGE3wdesxMx_2I4lhP__8og.JPEG%2F596bfecf-f30f-4dd6-879b-08c98343545e.jpeg%2F1536x852" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMjRfMTEy%2FMDAxNzkyODMyMzU5NzQ4.guHkMMNJvcFCAisSD8ZrFpNnm-y0Vg-XyfwoiD1fEh8g.UYYoZjgEv1GNU7SJZEUkSL671OX-BxTYvdZbk5A29HYg.PNG%2F%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2026-10-24_175855.png%2F396x505" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMjRfMTMz%2FMDAxNzkyODMyNzMzNDUx.PWw0FIfOuTbD11GXoCEcGtsIpP6rO-lXEs7bw6bBOskg.vp7LmXME9fZEBVsvMk26i9imkL_M4fHzoFd3Ek4OQqsg.JPEG%2F09661cfb-96b1-4fba-998c-1617e4c7a963.jpeg%2F1536x866" }
  ],
  facilities: [
    { name: "프라이빗온수풀", icon: "wifi" },
    { name: "홍천강전망", icon: "wifi" },
    { name: "개별테라스", icon: "wifi" },
    { name: "독립스파", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "디자인가구", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "450,000",
    weekend: "540,000",
    peak: "607,500"
  }
};
