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

  try {
    const [animapRes, wezipRes] = await Promise.allSettled([
      fetch('https://animap.co.kr/api/visitors', {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
        cache: 'no-store'
      }),
      fetch('https://wezip.co.kr/api/counter', {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
        cache: 'no-store'
      })
    ]);

    let animap = null;
    if (animapRes.status === 'fulfilled' && animapRes.value.ok) {
      animap = await animapRes.value.json().catch(() => null);
    }

    let wezip = null;
    if (wezipRes.status === 'fulfilled' && wezipRes.value.ok) {
      wezip = await wezipRes.value.json().catch(() => null);
    }

    return new Response(JSON.stringify({
      timestamp: new Date().toISOString(),
      animap,
      wezip
    }), { status: 200, headers });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500, headers });
  }
}
