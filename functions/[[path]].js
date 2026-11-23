export async function onRequest(context) {
  try {
    const { request, env } = context;
    const url = new URL(request.url);

    // 1. 구버전 루트 sample1.html ~ sample8.html -> /samples/ 301 영구 리디렉션 (404 완벽 방지)
    const sampleMatch = url.pathname.match(/^\/sample([1-8])\.html$/);
    if (sampleMatch) {
      return Response.redirect(`${url.origin}/samples/sample${sampleMatch[1]}.html`, 301);
    }

    // 2. 구버전 templates.html 및 Customer 경로 -> portfolio.html 301 리디렉션
    if (url.pathname === '/templates.html' || url.pathname.startsWith('/Customer/')) {
      return Response.redirect(`${url.origin}/portfolio.html`, 301);
    }

    // 4. 숙소 서브도메인 접근 시 메인 도메인으로 301 리디렉션 (5xx 크래시 원천 방지)
    const hostname = url.hostname.toLowerCase();
    if (hostname.endsWith('.adopter.co.kr') && hostname !== 'adopter.co.kr' && hostname !== 'www.adopter.co.kr') {
      return Response.redirect(`https://adopter.co.kr${url.pathname}`, 301);
    }

    // 5. 기본 정적 에셋 서빙
    const response = await env.ASSETS.fetch(request);
    
    // 6. 없는 경로일 경우 친절한 404.html 서빙
    if (response.status === 404 && !url.pathname.startsWith('/api/')) {
      try {
        const notFoundUrl = new URL('/404.html', request.url);
        const notFoundResponse = await env.ASSETS.fetch(new Request(notFoundUrl, request));
        if (notFoundResponse.status === 200) {
          return new Response(notFoundResponse.body, {
            status: 404,
            headers: notFoundResponse.headers
          });
        }
      } catch (e) {
        // fallback
      }
    }

    return response;
  } catch (err) {
    // 5xx 서버 오류 원천 방지: 에러 발생 시 안전하게 메인 페이지 서빙
    try {
      return await context.env.ASSETS.fetch(new Request('https://adopter.co.kr/', context.request));
    } catch (fallbackErr) {
      return new Response('Adopter Web Studio', { status: 200, headers: { 'Content-Type': 'text/plain' } });
    }
  }
}
