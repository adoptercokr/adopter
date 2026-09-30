const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/1299722517/home",
  phone: "0507-1315-4934",
  name: "스테이한담",
  subtitle: "Premium Stay",
  description: "<<찾아오는길 안내>>  자차 이용 시  내비게이션에 제주시 애월읍 납읍리 1683-1 또는 스테이한담(한담스테이X) 입력  대중교통 이용 시  1. 제주국제공항 도착 후 제...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250606_176%2F1749174778249ujujV_JPEG%2F963A3415_copy.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250606_249%2F17491747793349XNQ9_JPEG%2F963A5011_copy.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20260806_178%2FM21RH_1785995635760oaPdy_JPEG%2Fthumbnail-4C7D2592-B2B7-464E-83B9-95BA3510A343.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNjA4MjBfMTMw%2FMDAxNzg3MjAzNzM1MDA3.AzPkMKjO2UNlB_h3-jiUJ_PSkS9PJuO4aIvE8bt-G5Ig.cBty1OVgU8aapUTCYffElPqs6riepTuPIoeaMESewVkg.JPEG%2Fimage.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250606_10%2F17491747789918KoAS_JPEG%2F963A2865_copy.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250606_233%2F1749174777896Ef7Y6_JPEG%2F963A3021_copy.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fvideo-phinf.pstatic.net%2F20240803_271%2F1722694739362z6ub6_JPEG%2FBfEzsDeQtn_03.jpg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA5MThfNjcg%2FMDAxNzg5NzM0MTM2MjI4.7gCxvNjxEj2YdAENvXWkYNwSBUfz6cHOHvenRq_rj-4g.t7pTsQjRvTZT53OqamdX4-MbldkYxR7XmrRgkcQuOFgg.JPEG%2F46DB04BD-0C40-4B25-81CC-FBB1F4BB3499.jpeg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA5MTdfMjMg%2FMDAxNzg5NjA5MzM3MDgw.Jw49gR-X-rHupGoqgc21vYiQRpkI6f42fSjg0Yr-nwAg.L3VknN2SY61T6X9s3zTk1aZ5MDv9D5wkpKPbtpcZ5wog.JPEG%2F20260912_200402.jpg.jpg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MTJfMjM2%2FMDAxNzg2NDk4ODY3NTg2.jp1Hp2CGR9X1ckREYqaakGgNsnyJ_LBcOqk6Qex5-vIg.QgPeoKlA8r8MFlqDlWzE1RZrPyN0FrwOI_yBjW2xu4Eg.JPEG%2F20260809_193545.jpg.jpg" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNjA4MTJfMjgw%2FMDAxNzg2NDk4ODY3NjQy.HjPbd8JjuwjIeDxCL7N41vVZLnH9jCN12M6dhyOCetUg.V1-_T2Rqqg2owcIgOxYAavimdCHy3dbXdbtZ4ioN7vUg.JPEG%2F20260809_193617.jpg.jpg" },

  ],
  facilities: [
    { name: "모던", icon: "wifi" },
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
