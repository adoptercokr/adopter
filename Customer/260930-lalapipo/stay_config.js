const STAY_CONFIG = {
  variant: 1,
  naverLink: "https://m.place.naver.com/accommodation/1061012161/home",
  phone: "0507-0000-0000",
  name: "라라피포 제주",
  subtitle: "Premium Stay",
  description: "[입퇴실안내] - 입실: 15시 00분 - 퇴실: 11시 00분 - 입실 마감시간: 22시 00분 - 저녁 10시 이후 입실 시 반드시 펜션으로 사전 연락 부탁드립니다.   ...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220902_149%2F1662096909315yg8P4_JPEG%2F11_%25282%2529.jpg" },
    { id: "s2", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220902_110%2F16620969073329hg7s_JPEG%2F1.jpg" },
    { id: "s3", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220902_147%2F1662096907528DS7If_JPEG%2F0.jpg" },
    { id: "s4", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220902_40%2F1662096907522iW6MI_JPEG%2F2.jpg" },
    { id: "s5", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTExMTlfMzgg%2FMDAxNzYzNTM4MTc0Njk1.zdEhA1qHXXVgXpqvv4U3RPL3eFuiPWGrTtHK-EDtovEg.itdUhdGsTLUQd7lU2V46m0tZV0Of-mZzWD-DLZEpOXkg.JPEG%2FDB6C9A64-9DFA-4F8D-90B4-5544993286A0.jpeg" },
    { id: "s6", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTA4MTFfMjk0%2FMDAxNzU0ODQzNjMzNzM2.HKjKAvJtFozFp1AwXhiiXs049g4yRtvtjdJyZ5ISvfAg.-IUw-JQvqvPHRcQvUbLSc3Y5-X2WAmtex5SGKEDlRC8g.JPEG%2FA1E26132-F263-42E7-BBAA-0188A5B7622B.jpeg" },
    { id: "s7", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTA4MTFfMjA3%2FMDAxNzU0ODQzNjMzOTQ5.uqhvrIbFyswHkN8DqNXihDxwOV0f83FUdKWinlHyFZkg.fXvF4LefvjzgGpzqPgOsico0MeNj9EWmxZEf38IBe0sg.JPEG%2FB05F631D-794E-4C66-A308-2729B487E34A.jpeg" },
    { id: "s8", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTA3MDNfMjcz%2FMDAxNzUxNTQ5NjEwMjY4.J2rhsDPQXWDP76N5xaOzEZsMUtCPHdAoZcz5HjPk1Acg.gVjIrtcFxKPVkuCZe0lzoSCbuenpeMmIx76GrtxDHm4g.JPEG%2FD9B2DB9C-CB38-44F2-AE01-7FE2BCFF567D.jpeg" },
    { id: "s9", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTAzMDZfMTQx%2FMDAxNzQxMjM3MDMyNjQ5.3MdshDqzPR7Nnx4oTLvEwo1K79utCfzwZ7PT_NeBcAAg.cw8DSJcUe0cpbNmfPq2sikz8XFchWAAkDSWHGGtExkAg.JPEG%2F9CAD6541-027F-4979-8FE9-A596DEBB90F5.jpeg" },
    { id: "s10", mainImage: "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTAzMDZfMjcx%2FMDAxNzQxMjM3MDMyMzQz.s3qvNYerDGhvq9Er19WeFNQEhFJFqFGeSL5dNouDGbog.MdgG-eItT2ZeZGeKP-4MQA53cRM021_cmqEWBqmbo3wg.JPEG%2F33D267E4-0433-456E-9609-A03B50B9EA16.jpeg" },

  ],
  facilities: [
    { name: "반려동물", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "침대방", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "온돌방", icon: "wifi" },
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
    weekday: "0",
    weekend: "0",
    peak: "0"
  }
};
