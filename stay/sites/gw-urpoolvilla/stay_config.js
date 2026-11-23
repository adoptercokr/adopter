const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/1979423304/home",
  phone: "0507-1390-2972",
  name: "원주 유알 풀빌라",
  subtitle: "건축 미학과 자연이 공존하는 프리미엄 풀빌라",
  description: "노출 콘크리트의 유려한 조형미와 모던한 디자인이 돋보이는 원주의 하이엔드 스테이입니다. 넓은 개별 풀과 프라이빗 라운지에서 특별한 여유를 즐기세요.",
  address: "강원특별자치도 원주시 지정면 지정로 912",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260317_40%2F1773737720966eMb45_JPEG%2FKakaoTalk_20260311_115534152.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260317_183%2F17737378048958X29H_JPEG%2FKakaoTalk_20260311_115804623_04.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20260607_254%2FXtfuU_1780820333779OXlIs_JPEG%2FPublishThumb_20260607_171608_644.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260317_295%2F1773737804991Wn9HD_JPEG%2FKakaoTalk_20260311_115804623_05.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260317_176%2F1773737764533FnIUS_JPEG%2FKakaoTalk_20260311_115617984_06.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTlfNTEg%2FMDAxNzgxODU4NDY3MDkx.EqqigIbp8gYJZUCgAw9-a-miuK53fCI3EtzXSnPunwAg.EXaKUYJ5hRoZqJGbkmpeXMqdbKz7hsz2d_o0C6xx0oEg.JPEG%2FIMG%25EF%25BC%25BF1160.JPG%2F900x600" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTlfMjM4%2FMDAxNzgxODU4NDg3ODMy.NzrOkKAkEIdcOOaH2_s9ZgpFi2MXjBhmGlzxv1v244Qg.tgOnkKWWrszgzvtnV-Rx3-ud63mVJbG7DHCncDLybk0g.JPEG%2FIMG%25EF%25BC%25BF1130.JPG%2F900x1350" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MDNfMTQw%2FMDAxNzg4NDQ0Mzk0NTQ4.PYglj914fg-ggnmPOAFJEjJJwm3Z2ZPxEJpbV2aw0GQg.r_NDJX4L8PIlS0EolCmk3YAbR8dsI8pJx-SrMFbALmkg.JPEG%2Foutput%25EF%25BC%25BF234085345.jpg%2F869x1199" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTlfMTg1%2FMDAxNzgxODU4NDkxNjg2.8cr8n3vr7Vt9QYTaV5i3Xn4a8tg0mUmpOC6L4AXn_0sg.VJW4wmynAI7TxJ1Za06jhma_cbmtnobPQh-bYmg_frAg.JPEG%2FIMG%25EF%25BC%25BF1141.JPG%2F900x1350" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA2MTlfNjEg%2FMDAxNzgxODU4NDA1OTEx.HXzhPSXYZ2Q2FBkXlzEfycXrIBhvXGQlMcOBXcqsbwsg.j2N7XZuw841wyQPzJQrRjxJW0xm7ahSebvCU9Nibgjsg.JPEG%2FIMG%25EF%25BC%25BF3499.jpg%2F900x1200" }
  ],
  facilities: [
    { name: "건축디자인스테이", icon: "wifi" },
    { name: "독립프라이빗풀", icon: "wifi" },
    { name: "라운지테라스", icon: "wifi" },
    { name: "고급음향시스템", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "개별주차", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "500,000",
    weekend: "600,000",
    peak: "675,000"
  }
};
