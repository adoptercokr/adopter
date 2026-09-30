const STAY_CONFIG = {
  variant: 4,
  naverLink: "https://m.place.naver.com/accommodation/1188489877/home",
  phone: "0507-1344-6481",
  name: "모티브하우스",
  subtitle: "Premium Stay",
  description: "저희 모티브하우스의 자랑은  층고가 높고 넓은 개방적인  공간이며 조용한 시골동네에서 오롯이 쉼을 즐길 수 있는 주인장이 손수 집짓고 가구제작,인테리어한 독채펜션입니다. 풍차...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240323_191%2F1711191767853RLhM2_JPEG%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5_%25282%2529.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240323_110%2F1711192015677VIB20_JPEG%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5_%252812%2529.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fphinf.pstatic.net%2Ftvcast%2F20260924_133%2FN7lX6_17902336458538P97j_JPEG%2FPublishThumb_20260924_160621_988.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=f84_sharpen&src=https%3A%2F%2Fclip-service-phinf.pstatic.net%2FMjAyNTA4MjJfOSAg%2FMDAxNzU1ODI2NTI2MDAx.WkBmRIaXyg-SCNbno8ZV6v9sJeGHMl8VapqUuV_-u2og.MrDvdjOpsvL-1neKOJjUSt19KfQdhaS2cIea0YgIHEYg.JPEG%2Fimage.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240121_106%2F1705835994554TqmwH_JPEG%2F1000004273.jpg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240323_202%2F1711191665389pQ0fh_JPEG%2FKakaoTalk_20240203_090729090_10.jpg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTExMjVfOTgg%2FMDAxNzYzOTk3MDM2OTkw.ln3GHlaK1LDGcLbohTL7VliHevRM4ImdJKLaQqcLIkkg.u5Ci3tf3vwh0k3_sTvUqWvEKVUz5EkHKuamTttjLKKMg.JPEG%2F3EF9E275-4A6F-452A-BDB7-A345F82705B3.jpeg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfOCAg%2FMDAxNzkwMjMyODQ5ODI0.rpYKr1OoG8YCIOjnvO8rZbCzyCepj6gL-5oI4PDJEVYg.ndWi_IUaCOsAzeV6xNqcuU-8TATx0vXFMNxLrZjQ4mog.JPEG%2F20260920_170032.jpg%2F1689x3000" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfODMg%2FMDAxNzkwMjMzMDI5Njg1.-dwDRw9ZmYle3nAcuT1fGTUTQwLrz11VOPfqbjYZ4tYg.OwQ6IICwNO13wtlt_G9r_Skmxrasy9gTc-ztcnYq6VAg.JPEG%2F20260920_170235.jpg%2F1689x3000" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMjQw%2FMDAxNzkwMjMzNDI2ODA2.lj39cYOC2LrQ7QIcDuEGnJXA0Iir-eS7W35M8A8TGjYg.8F8W3YYbOelF14ComcT5rV6PYK1KdUoPerDNK7NWsm4g.JPEG%2F20260920_170049.jpg%2F2250x3000" },
    { id: "s11", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fblogfiles.pstatic.net%2FMjAyNjA5MjRfMTU2%2FMDAxNzkwMjMzNzI1MjAy.prtSXd7RZq_f3BGk6t3SEa_qNThH69PudGanR2IyL2Ig.eECN6yxLl4McpfZP19EIzX-oUGF95GZqdyC-XbIP5psg.JPEG%2F20260920_170943.jpg%2F2250x3000" },

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
