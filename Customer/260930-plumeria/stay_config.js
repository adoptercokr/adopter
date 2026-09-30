const STAY_CONFIG = {
  variant: 2,
  naverLink: "https://m.place.naver.com/accommodation/38729145/home", name: "플루메리아 펜션",
  subtitle: "Premium Stay",
  description: "[자차_렌터카 이용 시] 네이버 지도에 플루메리아 펜션 or 애월해안로 476 검색  [대중 교통이용] 1. 택시 : 제주공항에서 20분소요. 약 15,000원. 2. 버스 ...",
  benefits: [
    { id: "b1", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>`, title: "프라이빗 공간", description: "오직 한 팀만을 위한 완벽한 프라이빗 스테이", detail: "조용하고 아늑한 휴식" },
    { id: "b2", icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>`, title: "프리미엄 어메니티", description: "최고급 호텔 수준의 어메니티 제공", detail: "친환경 제품 사용" }
  ],
  spaces: [
    { id: "s1", title: "메인 공간", subtitle: "Main Space", mainImage: "./img/photo_1.jpg", images: ["./img/photo_1.jpg", "./img/photo_2.jpg"], totalPhotos: 2 },
    { id: "s2", title: "휴식 공간", subtitle: "Rest Area", mainImage: "./img/photo_3.jpg", images: ["./img/photo_3.jpg", "./img/photo_4.jpg", "./img/photo_5.jpg"], totalPhotos: 3 }
  ],
  facilities: [
    { name: "침대방", icon: "wifi" },
    { name: "가족실", icon: "wifi" },
    { name: "모던", icon: "wifi" },
    { name: "와이파이", icon: "wifi" },
    { name: "스파", icon: "wifi" },
    { name: "잔디", icon: "wifi" }
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
