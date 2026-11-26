export async function onRequest(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Cache-Control': 'no-store'
  };

  if (context.request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers });
  }

  // Pure honest real status - Never fabricate fake numbers
  const stats = {
    timestamp: new Date().toISOString(),
    animap: { note: "실시간 Supabase DB 카운터 연동", hasApi: true, apiUrl: "https://animap.co.kr/api/visitors" },
    wezip: { note: "실시간 DB 카운터 연동", hasApi: true, apiUrl: "https://wezip.co.kr/api/counter" },
    lotto: { note: "오픈 전 개발 진행 중 (BETA)", hasApi: false },
    care: { note: "오픈 전 데이터 검증 중 (BETA)", hasApi: false },
    colorbob: { note: "Google GA4 속성 측정 중 (자체 카운터 미연동)", hasApi: false },
    adopter: { note: "Google GA4 속성 측정 중 (자체 카운터 미연동)", hasApi: false },
    game: { note: "Google GA4 속성 측정 중 (자체 카운터 미연동)", hasApi: false },
    jejumodo: { note: "Cafe24 쇼핑몰 관리자 확인", hasApi: false },
    theandante9: { note: "Cafe24 쇼핑몰 관리자 확인", hasApi: false }
  };

  return new Response(JSON.stringify(stats), { status: 200, headers });
}
