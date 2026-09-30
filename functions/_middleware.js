import { routeMap } from './route_map.js';

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const hostname = url.hostname.toLowerCase();

  // Check for custom subdomains like moheomdam.adopter.co.kr
  const parts = hostname.split('.');
  if (parts.length >= 3 && !['www', 'adopter', 'api'].includes(parts[0])) {
    const sub = parts[0];
    const mappedFolder = routeMap[sub] || sub;

    let targetPath = url.pathname;
    if (targetPath === '/' || targetPath === '') {
      targetPath = `/${mappedFolder}/index.html`;
    } else if (!targetPath.startsWith(`/${mappedFolder}/`)) {
      targetPath = `/${mappedFolder}${targetPath}`;
    }

    const rewriteUrl = new URL(targetPath, request.url);
    const newRequest = new Request(rewriteUrl.toString(), request);
    return env.ASSETS.fetch(newRequest);
  }

  return context.next();
}
