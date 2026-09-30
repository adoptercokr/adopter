const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/1831033368/home",
  phone: "0507-1364-5625",
  name: "하일리제주",
  subtitle: "Premium Stay",
  description: "독채,수영장 감성숙소 하일리제주 가격은 50만원 부터 제주특별자치도 제주시 애월읍 수산8길 6 https://www.instagram.com/highly_jeju/ 더 많은 ...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220109_194%2F1641725616875EUutn_JPEG%2F500891CB-634C-4D11-B6EC-BD8191850C77.jpeg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220109_160%2F1641725612551dNsAi_JPEG%2F0409C004-3E33-4FF2-9B68-4C8A11969969.jpeg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220109_268%2F1641725610918N9UCC_JPEG%2F930C1163-F907-4A01-BEDF-91D0B5376C5C.jpeg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220109_56%2F1641725354335eJSV9_JPEG%2F234DECE1-214A-48CA-A3F4-DEAC3E83DFBD.jpeg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfMTk4%2FMDAxNzg3ODEyODE3NjI4.uVDHOevJLFKsyC5MEUO7AekhfKesKYQ5FmDXfG_Effcg.UMrhkKnDYWckMNZnBUVxdgNlh-z8JDsJcZ3qz9s5jEog.JPEG%2FIMG%25EF%25BC%25BF0654.jpg%2F900x1200" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfNjUg%2FMDAxNzg3ODEyNzQ1NTY4.3GGBH13Ng8jCBbYADqXiEMcd3UELEZvRuKFtdxHFMiwg.bx2sR3g7rUuKD3qt4IquraaGw0CPVceo4rxBakkttq4g.JPEG%2FIMG%25EF%25BC%25BF0641.jpg%2F900x1200" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfMjU4%2FMDAxNzg3ODEyOTcwNTYw.wcuyONzRvSiaUyao2QTNdvXxfPjNUCoGsjfrP5iYARgg.Itmvb2rsdJshj9_ippefkDMmuwNPVnpScoIVblMv_u4g.JPEG%2FIMG%25EF%25BC%25BF0648.jpg%2F900x1200" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfMTU0%2FMDAxNzg3ODEyNjgxMTQx.Tw-qqNxYDZwv3LNA4kKRgUR2ROlOY9UL6xrpLRX1IlEg.Z-QrK2OzTkLNMXdUbb2qNR7KAPQvbtnSI-ZTMjp8d2sg.JPEG%2FIMG%25EF%25BC%25BF0644.jpg%2F900x1200" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfNDAg%2FMDAxNzg3ODEzMDgzMTk3.FsJIPmYynNx6eN1wDMDcD-d8klLrYJBXjFxKPUmP9P8g.ly9OeeSx9iUM3o1Gcf3UzFOxsM8ORFMSjM0ywk1_5t8g.JPEG%2FIMG%25EF%25BC%25BF0647.jpg%2F900x1200" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w800_800&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA4MjdfMTk5%2FMDAxNzg3ODEyOTI0MDQx.2Ls6EDe6-9Yvvb_bPiT1F0zWzSRM-4_41l2gNXZsMkgg.GTCn2aM_MrRoDCzRADUa6us7xHZnqxALUng_qqLopdEg.JPEG%2FIMG%25EF%25BC%25BF0653.jpg%2F900x1200" },

  ],
  facilities: [
    { name: "스파", icon: "wifi" },
    { name: "단체", icon: "wifi" },
    { name: "복층", icon: "wifi" },
    { name: "풀빌라", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "독채", icon: "wifi" },
    { name: "개별바비큐", icon: "wifi" }
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
