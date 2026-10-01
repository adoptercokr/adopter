const STAY_CONFIG = {
  variant: 3,
  naverLink: "https://m.place.naver.com/accommodation/1266911405/home",
  phone: "0507-1482-8211",
  name: "스테이느긋",
  subtitle: "Premium Stay",
  description: "찾아오시는 길  네비게이션에서 '스테이느긋'을 검색하시면 편하게 찾아오실 수 있습니다.  주소 제주특별자치도 제주시 애월읍 오당빌레길 30 (하가리 804-5)  제주공항에서...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_96%2F1785366621277GcNEm_JPEG%2F3%25BF%25F922%25C0%25CF_%25C0%25FC%25BC%25DB-64.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_280%2F1785367072514BNPjh_JPEG%2F3%25BF%25F9_%25C3%25D4%25BF%25B5-99.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA5MzBfMTg5%2FMDAxNzkwNzY4ODQ3Nzcx.XLYnsV5aoXYNauRQFCgS2e1lJr5j0lcIILh6xQvk9wEg.3sz7HIqC0mHBb37OLqtHC3h5Dh4wTjejwHzd21Q-g3gg.JPEG%2Fthumbnail-7A32E3EC-4928-479F-8E9A-1E39B0CDBB3E.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNTA4MTFfMTkz%2FMDAxNzU0OTA5MDM5NDYw.WHFkLy0kKs28HJ887kecwYjoon4n1KkJz_ilx3ufcSQg.VDLxrPLVHXvuDsPVcOhBv6geCXQL1CgkRmPRyIkNQsQg.JPEG%2F7.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_58%2F1785367136015Ip2QX_JPEG%2FKakaoTalk_20260729_213735156.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260730_251%2F1785414541138VTxUS_JPEG%2FIMG_1744.jpg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MjVfMzcg%2FMDAxNzg3NjU0MjM1NDE0.AvUI3FNFcfeUJdRPk4H7L4f6wSkolNHNTumr3ar4qx4g.aRX7l-suN3hbzGZHaDDGA5alX2zhpJvVtLbEz3p5514g.JPEG%2F17366644-022B-4225-93FC-0BE67C7ACB57.jpeg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjdfNDQg%2FMDAxNzkwNDkyODM4MTAx.A-1QhcbF7kXK7m6vEb17eS-Wjd9g943H8YfpOXGaNBwg.2kNiBfaczHodTyqzv7Y6s4jCnQCC9lTvh_kVtlY5e4wg.JPEG%2F900_20260915_161640.jpg%2F900x1200" },

  ],
  facilities: [
    { name: "바비큐장", icon: "wifi" },
    { name: "수영장", icon: "wifi" },
    { name: "풀빌라", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "잔디", icon: "wifi" },
    { name: "독채", icon: "wifi" },
    { name: "개별바비큐", icon: "wifi" }
  ],
  rules: [
    "체크인 15:00 / 체크아웃 11:00",
    "실내 절대 금연",
    "반려동물 동반 불가"
  ],
  rates: {
    weekday: "250,000",
    weekend: "250,000",
    peak: "250,000"
  }
};
