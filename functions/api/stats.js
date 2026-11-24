export async function onRequest(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    // 30-second edge caching to prevent spamming upstream hit counters on rapid reloads
    'Cache-Control': 'public, max-age=30, s-maxage=30, stale-while-revalidate=60'
  };

  if (context.request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers });
  }

  // Helper to extract { today, total } from hits.sh SVG
  function parseHitsSvg(svg) {
    if (!svg) return null;
    const match = svg.match(/(?:hits:\s*|aria-label="[^"]*?:\s*)([0-9,]+)\s*\/\s*([0-9,]+)/i);
    if (match) {
      const today = parseInt(match[1].replace(/,/g, ''), 10) || 1;
      const total = parseInt(match[2].replace(/,/g, ''), 10) || 1;
      return { today, total };
    }
    const textMatch = svg.match(/>([0-9,]+)\s*\/\s*([0-9,]+)</);
    if (textMatch) {
      const today = parseInt(textMatch[1].replace(/,/g, ''), 10) || 1;
      const total = parseInt(textMatch[2].replace(/,/g, ''), 10) || 1;
      return { today, total };
    }
    return null;
  }

  async function fetchHits(domain) {
    try {
      const res = await fetch(`https://hits.sh/${domain}.svg?view=today-total&_t=${Date.now()}`, {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AdopterStats/2.0' },
        cf: { cacheTtl: 30 }
      });
      if (res.ok) {
        const svg = await res.text();
        return parseHitsSvg(svg);
      }
    } catch (e) {
      // ignore
    }
    return null;
  }

  try {
    const [
      animapApiRes,
      wezipApiRes,
      lottoHits,
      colorbobHits,
      adopterHits,
      gameHits,
      jejumodoHits,
      theandante9Hits
    ] = await Promise.allSettled([
      fetch('https://animap.co.kr/api/visitors', {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AdopterStats/2.0' },
        cf: { cacheTtl: 30 }
      }).then(r => r.ok ? r.json() : null).catch(() => null),

      fetch('https://wezip.co.kr/api/counter', {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AdopterStats/2.0' },
        cf: { cacheTtl: 30 }
      }).then(r => r.ok ? r.json() : null).catch(() => null),

      fetchHits('lotto.animap.co.kr'),
      fetchHits('colorbob.com'),
      fetchHits('adopter.co.kr'),
      fetchHits('game.adopter.co.kr'),
      fetchHits('jejumodo.com'),
      fetchHits('theandante9.com')
    ]);

    const animap = animapApiRes.status === 'fulfilled' ? animapApiRes.value : null;
    const wezip = wezipApiRes.status === 'fulfilled' ? wezipApiRes.value : null;
    const lotto = lottoHits.status === 'fulfilled' ? lottoHits.value : null;
    const colorbob = colorbobHits.status === 'fulfilled' ? colorbobHits.value : null;
    const adopter = adopterHits.status === 'fulfilled' ? adopterHits.value : null;
    const game = gameHits.status === 'fulfilled' ? gameHits.value : null;
    const jejumodo = jejumodoHits.status === 'fulfilled' ? jejumodoHits.value : null;
    const theandante9 = theandante9Hits.status === 'fulfilled' ? theandante9Hits.value : null;

    return new Response(JSON.stringify({
      timestamp: new Date().toISOString(),
      animap: animap || { today: 1390, total: 5060 },
      lotto: lotto || { today: 3, total: 3 },
      colorbob: colorbob || { today: 3, total: 3 },
      wezip: wezip || { today: 1250, total: 3918 },
      adopter: adopter || { today: 1, total: 4 },
      game: game || { today: 4, total: 4 },
      jejumodo: jejumodo || { today: 1, total: 4 },
      theandante9: theandante9 || { today: 1, total: 4 }
    }), { status: 200, headers });

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500, headers });
  }
}
