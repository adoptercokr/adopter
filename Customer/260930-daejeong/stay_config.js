const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/1124644686/home",
  phone: "0507-1392-6012",
  name: "대정프라방",
  subtitle: "Premium Stay",
  description: "#대정프라방 #제주도단체펜션 #서귀포단체펜션 #제주가족펜션 #제주가족여행 #제주단체여행 #산방산 제주도 독채 단체 펜션 대정프라방 가는 길에 보이는 산방산과 푸른 하늘🩵💙",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221125_51%2F1669385345208WmQ7o_JPEG%2FKakaoTalk_20221125_230745209_18.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221125_205%2F1669385494053nJ0ve_JPEG%2FKakaoTalk_20221125_231000311.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogpfthumb-phinf.pstatic.net%2FMjAyNDA2MTBfMjU5%2FMDAxNzE4MDIyMDAyNjc0.eNFO9ag9-GiF2JmD4WpBK-4WSuhomVt0BDzNpKjv2nAg.cv84OutOnwCUh-skCmf-SxkeBvdVT4xaBXxYOiO-Vw0g.JPEG%2FKakaoTalk_20221120_134334929_04.jpg%2FKakaoTalk_20221120_134334929_04.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221125_18%2F1669385494635POAiD_JPEG%2FKakaoTalk_20221125_231000311_01.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221125_88%2F1669385494093GMsTO_JPEG%2FKakaoTalk_20221125_231000311_02.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MTJfMzUg%2FMDAxNzg2NTIwNTE2Njkz.HiNTiWTVR3SmIoe-wEV2JLjDq3qMpyHJiFJvikD2Hvkg.tk7ljsHLamOKv62KNBarU33rAU_3QgHx4MTqFG4hBCYg.JPEG%2FIMG%25EF%25BC%25BF3990.jpg%2F900x1200" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MTJfMTQ2%2FMDAxNzg2NTIwNDQ4Nzky.KCQXgPDK-g45C5cjZcx91BKQKaZH5GvRti8H0IUvnmwg.diAZ_pXrjCqQ15ARnPOBu0n4z78PoamDe9Cqw6joqm4g.JPEG%2FIMG%25EF%25BC%25BF3928.jpg%2F900x676" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MTJfMjY1%2FMDAxNzg2NTIwNDcyNDIz.EA_uV1U1ZUnHnuLqoGrCPRH64qLU_VBhjxGUdk-8iNog.wBzrLQaVZrqdn6aNXpWwsGKpivNvhGnLfXM9yYuQZaYg.JPEG%2FIMG%25EF%25BC%25BF3937.jpg%2F900x676" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MTJfMTIw%2FMDAxNzg2NTIwNDc0NzY0.BbLH7suv0gwBvx71pyIDXS0SQIH4CxdkF_KSMU15BXMg.rP0G0A9ZGsgQkKVwAMEckSVjEySPWoPTpfaZlEOJM5wg.JPEG%2FIMG%25EF%25BC%25BF3938.jpg%2F900x676" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MTJfMjIz%2FMDAxNzg2NTIwNTA2MzE3.ODOfBKhAcPHcc170VEfeL0tX0izY6d1Ki488c-EipVYg.Wehn3ik2HW1FgxiqrJL1Y0Jzy42kq03k0E-uHDzHWzQg.JPEG%2FIMG%25EF%25BC%25BF3946.jpg%2F900x676" },
    { id: "s12", mainImage: "https://g-place.pstatic.net/assets/shared/images/img_review_clip_light.png" },
    { id: "s13", mainImage: "https://g-place.pstatic.net/assets/shared/images/icon_blur_keyword_dessert_good.png" },
    { id: "s14", mainImage: "https://g-place.pstatic.net/assets/shared/images/icon_blur_keyword_price_cheap.png" },
    { id: "s15", mainImage: "https://g-place.pstatic.net/assets/shared/images/icon_blur_keyword_talk_good.png" },

  ],
  facilities: [
    { name: "바비큐장", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "노래방", icon: "wifi" },
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
