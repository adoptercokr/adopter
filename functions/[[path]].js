export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const hostname = url.hostname.toLowerCase();

  // 1. 서브도메인 확인 (예: moheomdam.adopter.co.kr)
  // 메인 도메인이 아니거나 서브도메인이 존재하는 경우
  if (hostname.endsWith('.adopter.co.kr') && hostname !== 'adopter.co.kr' && hostname !== 'www.adopter.co.kr') {
    const subdomain = hostname.replace('.adopter.co.kr', '');

    // 만약 정적 리소스(/img/..., .jpg, .css, .js) 요청인 경우
    if (url.pathname.startsWith('/img/')) {
      const assetUrl = new URL(`/${subdomain}${url.pathname}`, request.url);
      return env.ASSETS.fetch(new Request(assetUrl, request));
    }

    // 메인 루트 요청 (/) 또는 일반 경로인 경우 해당 숙소의 index.html 반환
    if (url.pathname === '/' || url.pathname === '/index.html') {
      const stayUrl = new URL(`/${subdomain}/index.html`, request.url);
      return env.ASSETS.fetch(new Request(stayUrl, request));
    }

    // 기타 경로
    const fallbackUrl = new URL(`/${subdomain}${url.pathname}`, request.url);
    const resp = await env.ASSETS.fetch(new Request(fallbackUrl, request));
    if (resp.status !== 404) {
      return resp;
    }
  }

  // 2. 기본 요청은 원래 에셋 그대로 전달
  return env.ASSETS.fetch(request);
}
