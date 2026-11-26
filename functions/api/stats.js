export async function onRequest(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
  };

  if (context.request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers });
  }

  const targets = [
    { key: 'animap', hitUrl: 'https://hits.sh/animap.co.kr.svg?view=today-total' },
    { key: 'wezip', hitUrl: 'https://hits.sh/wezip.co.kr.svg?view=today-total' },
    { key: 'colorbob', hitUrl: 'https://hits.sh/colorbob.com.svg?view=today-total' },
    { key: 'adopter', hitUrl: 'https://hits.sh/adopter.co.kr.svg?view=today-total' },
    { key: 'game', hitUrl: 'https://hits.sh/game.adopter.co.kr.svg?view=today-total' },
    { key: 'jejumodo', hitUrl: 'https://hits.sh/jejumodo.com.svg?view=today-total' },
    { key: 'theandante9', hitUrl: 'https://hits.sh/theandante9.com.svg?view=today-total' },
    { key: 'lotto', hitUrl: 'https://hits.sh/lotto.animap.co.kr.svg?view=today-total' },
    { key: 'care', hitUrl: 'https://hits.sh/care.animap.co.kr.svg?view=today-total' },
  ];

  const results = {
    timestamp: new Date().toISOString()
  };

  await Promise.all(
    targets.map(async ({ key, hitUrl }) => {
      try {
        const resp = await fetch(`${hitUrl}&_t=${Date.now()}`, {
          headers: { 'User-Agent': 'Mozilla/5.0 (AdopterShowcase/1.0)' },
          cf: { cacheTtl: 0 }
        });
        if (resp.ok) {
          const svg = await resp.text();
          const match = svg.match(/hits:\s*([0-9,]+)\s*\/\s*([0-9,]+)/i);
          if (match) {
            const today = parseInt(match[1].replace(/,/g, ''), 10) || 0;
            const total = parseInt(match[2].replace(/,/g, ''), 10) || 0;
            results[key] = { pvToday: today, pvTotal: total };
            return;
          }
        }
      } catch (e) {
        // fetch error fallback
      }
      results[key] = { pvToday: null, pvTotal: null };
    })
  );

  return new Response(JSON.stringify(results), { status: 200, headers });
}
