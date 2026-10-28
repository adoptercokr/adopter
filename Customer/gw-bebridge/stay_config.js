const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/1824311893/home",
  phone: "0507-1392-6555",
  name: "영월 비브릿지 풀빌라",
  subtitle: "영월 계곡의 절경을 담은 럭셔리 리조트 스테이",
  description: "청정 영월의 계곡과 기암괴석을 마주하는 하이엔드 독채 풀빌라입니다. 넓은 테라스와 개별 온수 수영장에서 계곡의 물소리와 함께 힐링하세요.",
  address: "강원특별자치도 영월군 김삿갓면 영월동로 1121",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 독립된 프라이빗 스테이", detail: "완벽한 프라이버시 보장" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 힐링", description: "사계절 온수 및 최고급 어메니티 완비", detail: "안락하고 쾌적한 휴식" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fnaverbooking-phinf.pstatic.net%2F20250512_235%2F174701445798468d1d_JPEG%2FKakaoTalk_20250511_095114881_03.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20181230_134%2F15461666330882OOHN_JPEG%2FnFen_AVPNrnP9_thytWybO62.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjEwMjBfNDMg%2FMDAxNzkyNTA4MTczNDU5.8QQLC7wuj-qDQiTWF5wTq7BG1HWdGFlMRu4-Oq4vUSwg.ohCHX-m4RRDungWgmoc0I7NAoR9vovA-H50IGUdfHVIg.JPEG%2Fthumbnail-23830FF4-D3C6-40AA-B17F-A3FF228B68C8.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251202_79%2F1764672289422EtLWv_JPEG%2F7%25B5%25BF2%25C2%25F7_%25284%2529.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251205_34%2F1764933195369nh7iV_JPEG%2F6%25B5%25BF2%25C2%25F7_%252813%2529.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA3MjFfMjk4%2FMDAxNzg0NTkxMDc3OTIw.TCrK1gFseS7PrO2GAdE4XiOkYwjJW90M8kBIXdxCG78g.c95jiA2gSjtKSqEVPScnGIu9xCKLpw7IyfaueSZw6tgg.JPEG%2FD377F7EB-35B9-4648-9EA2-BC85134BAF9A.jpeg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjRfOTIg%2FMDAxNzkyODIyOTEzNzUz.ks-pacDcDNBpwGsHH2vwd6MHbrLKZkERmxojRRz38pUg.JecTGHSCyH0sesFNwA8EVNXlHCpn3HmCJAUFrheexmwg.JPEG%2F20261024_152045.jpg.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMjRfODQg%2FMDAxNzkyODIyOTEzNjY5.zcRkeM_8F5I5yMEB7vmZPUgUCtwrdl1wF3Tmks8yMjwg.QNR59FXcxC3G9fUQbSXhHDlf3h5dhmPMOZMlQjWRfBog.JPEG%2F20261024_152038.jpg.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjEwMTlfNDEg%2FMDAxNzkyNDE1MTI5MjQ5.P1YhkdneUllqy7jvXYWBXAP-oXbPg1yWyFctVMG4wuIg.B9aRTwdZuTOURVg6wvKMYrIE8AVPmAH0qmgZM5tYzDIg.JPEG%2F20261018_112251.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjEwMTRfMjk5%2FMDAxNzkxOTM3MTE0MjMx.izOAttoH56YOqJK3W8Fic0XnwFaoL8uLT_1FvBfDhEgg.LxnW6TG8r5ClbEPI9KulU5Wx8f-hnhfHGiYZky0F_Jgg.JPEG%2FKakaoTalk_20261014_091506974.jpg%2F3024x4032" }
  ],
  facilities: [
    { name: "계곡전망온수풀", icon: "wifi" },
    { name: "대형프라이빗테라스", icon: "wifi" },
    { name: "개별바베큐", icon: "wifi" },
    { name: "호텔식서비스", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "카페", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "지정된 구역 외 취사 및 화기 사용 제한"
  ],
  rates: {
    weekday: "460,000",
    weekend: "552,000",
    peak: "621,000"
  }
};
