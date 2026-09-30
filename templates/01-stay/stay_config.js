const STAY_CONFIG = {
  name: "희스테이 (HEESTAY)",
  subtitle: "Jeju Private Poolvilla",
  description: "머묾, 그 자체가 온전한 쉼이 되는 곳",
  benefits: [
    {
      id: "pool",
      icon: `<svg class="w-6 h-6 stroke-current" fill="none" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"/></svg>`,
      title: "야외 온수 수영장 무료",
      description: "돌담 아래 프라이빗 풀장. 타 숙소의 비싼 수영장 이용료 없이 온수 이용 가능합니다.",
      detail: "공과금 실비: 수도·온수가스비는 마진 없이 계량기 실비로만 보증금에서 투명하게 정산됩니다."
    },
    {
      id: "jacuzzi",
      icon: `<svg class="w-6 h-6 stroke-current" fill="none" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"/></svg>`,
      title: "야외 노천 자쿠지 무료",
      description: "성산의 밤하늘 별을 보며 즐기는 사계절 야외 온수 스파. 시설 이용료 없이 자유롭게 힐링하세요.",
      detail: "공과금 실비: 온수 공급에 사용된 실제 수도·가스 실비만 보증금에서 차감됩니다."
    },
    {
      id: "bbq",
      icon: `<svg class="w-6 h-6 stroke-current" fill="none" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v4M8 4l2 3M16 4l-2 3M5 11h14a7 7 0 01-14 0zM7 16l-2 5M17 16l2 5M12 16v5"/></svg>`,
      title: "사계절 바베큐 썬룸 무료",
      description: "비바람 걱정 없는 독립 썬룸과 웨버 바베큐 그릴 장비 대여비가 전액 무료로 제공됩니다.",
      detail: "안내: 일회용 석쇠망·숯은 개별 준비해 주시고, 이용 후 그릴 세척·정리 부탁드립니다."
    }
  ],
  spaces: [
    {
      id: "space1",
      title: "야외 풀장 & 노천 자쿠지",
      subtitle: "온수 가능",
      mainImage: "./img/수영장1.jpg",
      images: ["./img/수영장2.jpg", "./img/자쿠지1.jpg", "./img/수영장테라스1.jpg"],
      totalPhotos: 8
    },
    {
      id: "space2",
      title: "사계절 바베큐 썬룸",
      subtitle: "웨버 그릴",
      mainImage: "./img/썬룸1.jpg",
      images: ["./img/썬룸1.jpg", "./img/썬룸2.jpg"],
      totalPhotos: 2
    },
    {
      id: "space3",
      title: "1층 패밀리 거실",
      subtitle: "마당 통창뷰",
      mainImage: "./img/거실2.jpg",
      images: ["./img/거실3.jpg", "./img/창1.jpg", "./img/스피커.jpg"],
      totalPhotos: 5
    },
    {
      id: "space4",
      title: "풀옵션 주방 & 원목 식탁",
      subtitle: "6인용",
      mainImage: "./img/주방1.jpg",
      images: ["./img/주방2.jpg", "./img/주방6.jpg", "./img/식탁2.jpg"],
      totalPhotos: 6
    },
    {
      id: "space5",
      title: "침실 3개 (총 4베드)",
      subtitle: "1·2층 분리",
      mainImage: "./img/방1.jpg",
      images: ["./img/방1화장대.jpg", "./img/방2.jpg", "./img/방3.jpg"],
      totalPhotos: 4
    },
    {
      id: "space6",
      title: "2층 야외 전망 테라스",
      subtitle: "성산 힐링뷰",
      mainImage: "./img/2층테라스1.jpg",
      images: ["./img/2층테라스2.jpg", "./img/2층테라스3.jpg", "./img/2층테라스4.jpg"],
      totalPhotos: 4
    }
  ],
  facilities: [
    { name: "야외 수영장", icon: "수영장아이콘" },
    { name: "노천 자쿠지", icon: "자쿠지아이콘" },
    { name: "바베큐 썬룸", icon: "바베큐아이콘" },
    { name: "무료 와이파이", icon: "와이파이아이콘" },
    { name: "세탁기/건조기", icon: "세탁기아이콘" },
    { name: "풀옵션 주방", icon: "주방아이콘" }
  ],
  rules: [
    "실내 절대 금연",
    "반려동물 동반 불가",
    "밤 10시 이후 고성방가 자제",
    "이용 후 주방기구 및 그릴 세척"
  ],
  rates: {
    weekday: "190,000",
    weekend: "210,000",
    peak: "250,000"
  }
};
