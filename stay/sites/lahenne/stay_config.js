const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/36651683/home",
  phone: "0507-1436-1683",
  name: "고성 라헨느풀빌라",
  subtitle: "동해안 파노라마 오션뷰와 제트스파",
  description: "가진해변 바다 바로 앞에 위치하여 객실 어디서나 푸른 동해바다와 일출을 감상할 수 있는 감성 풀빌라입니다. 제트스파와 개별 풀이 준비되어 있습니다.",
  address: "강원특별자치도 고성군 죽왕면 가진해변길 217",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190325_79%2F1553508219797l0Yfg_JPEG%2F1.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190325_142%2F1553508219794LnmVk_JPEG%2F%25BF%25DC%25B0%25FC2.jpeg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA3MjlfMTcz%2FMDAxNzg1MzMzMDcwMTEz.AHpzJy0w2kdYPoSn7D3ln2h_WUhFz59ypL5ey9iBKPsg.tp2KqZ6kmgh21JG5E3YLxmvUZwrcNguY84EQTbhuzK4g.JPEG%2Fthumbnail-461B33C1-BE4F-4439-9EF2-BB32464218D0.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190325_218%2F1553508219796VwWPb_JPEG%2F%25C0%25FC%25B0%25E62.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190325_195%2F1553508219789PiPmf_JPEG%2F07.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fvideo-phinf.pstatic.net%2F20240229_257%2F1709184849989Wq9nP_JPEG%2F28ee6511-d6c4-11ee-ba10-a0369ffdb264_03.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMTlfNzgg%2FMDAxNzkyMzk3MzQ4NjYz.l_zLpclj9nvvav9kirRbOOenNrim5TNhnvE5jczUCJ8g.2tSCZ5wMO6L58xk-wTVJIxG4sQypgWIBzCaLN7bpYq8g.JPEG%2F15.jpg%2F700x525" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMTlfMTQx%2FMDAxNzkyMzk3MzQ3NjMz.UP2s-AbLLkpUsKMWxbLlYPeT-zz0JPeE6tBljzjfG34g.nGdsbHBQ3HxTPayf_hdgUUlSJ2n6n7WuICI6uGfD-k4g.JPEG%2F2.jpg%2F700x525" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMTlfOTMg%2FMDAxNzkyMzk3MzI4Mjcw.RX4mt6wU1sMSuSJUGguQm7W0D1ScGtDYqc3dXZdWpuQg.IqCUvyTwH0QRYXmWZvzmuynGXoXoiRAmWlUTbQrWcEQg.JPEG%2F2.jpg%2F700x525" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMTlfMTUy%2FMDAxNzkyMzk3MzQ5Mzgz.wVh5ufmtDmWb-_HGOdAoSFacmLLMP-JrWSKycO9nCQkg.Eu4mF1lAPbmJF7bdWtqTskM5_b7IED9ziiYnAgz1r30g.JPEG%2F23.jpg%2F700x525" }
  ],
  facilities: [
    { name: "파노라마오션뷰", icon: "wifi" },
    { name: "제트스파", icon: "wifi" },
    { name: "사계절온수풀", icon: "wifi" },
    { name: "일출명소", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "카페테리아", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "350,000",
    weekend: "420,000",
    peak: "472,500"
  }
};
