const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/1676997352/home",
  phone: "0507-1324-5197",
  name: "춘천 의림여관",
  subtitle: "자연의 소리에 귀 기울이는 사색의 숲속 독채",
  description: "춘천 신동면 깊은 숲속, 단 두 채의 객실로만 운영되는 프라이빗 힐링 스테이입니다. 원목의 따스함과 큰 창 너머의 푸르름 속에서 진정한 쉼을 마주합니다.",
  address: "강원특별자치도 춘천시 신동면 풍류길 46",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20261001_214%2F1790810400106Q8dfK_JPEG%2F1000016968.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20261001_56%2F1790810396540Kd5FV_JPEG%2F1000017005.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20250329_300%2FbwGFr_1743257081445wmOlu_JPEG%2FDDA7D5C2-1C40-4879-91FF-59B5AF983D04.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20261001_23%2F17908109158053Aowk_JPEG%2F1000016236.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20261001_135%2F1790819584485K9ABx_JPEG%2F1000026126.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfNjIg%2FMDAxNzkzMDcxOTk4MzEx.VAznvtv64_GOrs3ar8flEiVVfguwhyVYgy14uWl8GPUg.7hT4IP07nN1D9n8uu-t3giXwCPhLM7CbR_TbYo_fL-Yg.JPEG%2FAFA458C2-1932-45CA-8631-2EC3C27BA530.jpeg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfMTMg%2FMDAxNzkzMDcyMDAxODE2.UtK8j9hbcuzS7s_qLPVNKTe8-nA1c3tsxQW9JDX_ffEg.mMtJUMN7Y3D2RQ4Ymf1qkMxpQa4PkGzJXL-R2UeAjkog.JPEG%2F2FE67AB2-DDA6-4D1A-A972-28DDA0803C5F.jpeg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfMjA3%2FMDAxNzkzMDcyMDAyNjg0.IdQZRnXeVKflR0C9ghvyKHrloUkJTH1vvROd7RqVu9wg.H2iuL1FVRf12haLP7FrqtNlOvwLxXBT2wK6kquRM7Q8g.JPEG%2FDD5D047D-B208-411C-BF32-D6E11C5EE562.jpeg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfNDIg%2FMDAxNzkzMDcyMDEyMTYy.DeCONdQ7yO4__ccGvK2IWcuVmEgPuPvbYcC2-pn53lsg.ZMpuOD4MzkL8qNxIDIQApYu_BrwnUDQSFz8dFvrQH64g.JPEG%2F8CE190CA-4DC1-4BAB-A09C-D459B57737FF.jpeg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjdfMjM5%2FMDAxNzkzMDcyMDEyMzA2.axKUAAwcPGQCHSrR5q5pPELK2sscn1OggV0S_arzYnwg.V4oKhLUKyGwY_pcOJgWcu_cUBRh1AoFOrhpE0Xebw_Mg.JPEG%2FB65DDBC4-CBE0-4C81-99F2-6AF97B9F47E4.jpeg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f320_320&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20261001_214%2F1790810400106Q8dfK_JPEG%2F1000016968.jpg" },
    { id: "s12", mainImage: "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f320_320&src=https%3A%2F%2Fpup-post-phinf.pstatic.net%2FMjAyNjAxMDZfMTI5%2FMDAxNzY3NjkzMTIwOTMz.DbHLIlCNiCCOTIdPjHkfmLuZgOcECHuUs-WsRnokrrYg.EZOvZtfjoqkYpEiZv5trh4hgUphKsHjUPLe4f08TRIog.JPEG%2F069FDB25-1D24-4C51-A9B3-61B04DA424A4.jpg" }
  ],
  facilities: [
    { name: "사색의원목인테리어", icon: "wifi" },
    { name: "숲속뷰파노라마", icon: "wifi" },
    { name: "프라이빗다실", icon: "wifi" },
    { name: "오디오청음존", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "친환경어메니티", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "320,000",
    weekend: "384,000",
    peak: "432,000"
  }
};
