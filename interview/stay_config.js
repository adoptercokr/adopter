/**
 * 제주 희스테이 (JEJU HEESTAY) 샘플 데이터 설정 파일
 * 숙박업 웹사이트 마스터 템플릿 (templates/01-stay) 데이터 예시
 */

const STAY_CONFIG = {
  // 1. 브랜드 및 숙소 기본 정보
  brandName: "스테이 인터뷰 강릉",
  brandSubtitle: "Jeju Private Poolvilla",
  tagline: "스테이 인터뷰 강릉에서의 럭셔리 휴양",
  description: "프라이빗 독채 풀빌라 스테이 인터뷰 강릉에서 완벽한 하루를 보내세요.",
  
  // 2. 호스트 및 사업자 정보
  owner: "지희철",
  businessNo: "526-40-00959",
  address: "제주특별자치도 서귀포시 성산읍 온평서로 28-7",
  phone: "070-7954-1417",
  email: "jejuheestay@gmail.com",
  domain: "jejuheestay.co.kr",
  
  // 3. 외부 연동 링크
  kakaoChatUrl: "http://pf.kakao.com/_HCTxiX/chat",
  naverMapUrl: "https://map.naver.com/v5/search/%EC%A0%9C%EC%A3%BC%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84%20%EC%84%9C%EA%B7%80%ED%8F%AC%EC%8B%9C%20%EC%84%B1%EC%82%B0%EC%9D%8D%20%EC%98%A8%ED%8F%89%EC%84%9C%EB%A1%9C%2028-7",
  naverReservationUrl: "", // 네이버 예약 링크가 있을 경우 기입
  
  // 4. 유튜브 고화질 스트리밍 연동 (쇼츠 ID)
  youtubeIntroId: "f09Xfn1fHm8", // 메인 100vh 비디오 배경 쇼츠
  youtubeTourId: "JG92-0fSScQ",  // 공간 전체 둘러보기 모달 영상 쇼츠
  
  // 5. 숙박 요금 및 연박 할인 정책
  pricing: {
    weekday: 190000,              // 평일 1박 기본 요금
    weekend: 210000,              // 주말 및 공휴일(공휴일 전날 포함) 1박 요금
    peakSurcharge: 20000,         // 성수기(7, 8월, 명절 연휴) 1박 추가금
    baseGuests: 4,                // 기본 기준 인원
    maxGuests: 9,                 // 최대 수용 인원
    extraGuestFee: 10000,         // 4인 초과 시 1인 1박당 추가금
    minNights: 3,                 // 최소 숙박일 (기본 3박 이상)
    discounts: {
      days7: 10,                  // 7박 이상 10% 특별 할인
      days14: 15,                 // 14박 이상 15% 보름 살기 할인
      days28: 20                  // 28박 이상 20% 한달 살기 할인
    },
    depositLessThan7: 200000,     // 7박 미만 보증금
    depositMoreThan7: 300000,     // 7박 이상 보증금
    depositMoreThan28: 500000     // 28박 이상 보증금
  },

  // 6. 3대 무료 혜택 (시설 추가금 제로)
  freeBenefits: [
    {
      title: "단독 야외 수영장",
      subtitle: "Pool 0원",
      desc: "온수 추가비 0원 / 프라이빗 단독 이용"
    },
    {
      title: "프라이빗 노천 자쿠지",
      subtitle: "Jacuzzi 0원",
      desc: "사계절 온수 무료 / 돌담 힐링 스파"
    },
    {
      title: "사계절 독립 바베큐장",
      subtitle: "BBQ 0원",
      desc: "그릴 및 썬룸 대여 0원 / 쾌적한 환기 완비"
    }
  ],

  // 7. 공간 구성 안내
  spaces: {
    landSize: "130평 대지",
    buildingSize: "40평 2층 단독주택",
    floor1: "거실, 풀옵션 주방, 세탁실, 방2개(각 퀸베드), 욕실1개, 6인 식탁",
    floor2: "마스터룸(퀸+슈퍼싱글), 파우더룸, 욕실1개, 야외 전망 테라스",
    outdoor: "단독 야외 수영장, 온수 자쿠지, 독립 썬룸 바베큐장, 프라이빗 잔디마당"
  },

  // 8. 관리자 비밀번호
  adminPassword: "1316"
};

// 브라우저 및 Node 환경 호환
if (typeof module !== 'undefined' && module.exports) {
  module.exports = STAY_CONFIG;
}
