import { routeMap } from './_route_map.js';

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const hostname = url.hostname.toLowerCase();

  const parts = hostname.split('.');
  if (parts.length >= 3 && !['www', 'adopter', 'api'].includes(parts[0])) {
    const sub = parts[0];
    const mappedFolder = routeMap[sub] || sub;

    let targetPath = url.pathname;
    if (targetPath === '/' || targetPath === '') {
      targetPath = '/Customer/' + mappedFolder + '/index.html';
    } else if (!targetPath.startsWith('/Customer/' + mappedFolder + '/')) {
      // Allow assets like /img/photo_1.jpg to map to /Customer/260930-aewolrowa/img/photo_1.jpg
      targetPath = '/Customer/' + mappedFolder + targetPath;
    }

    const rewriteUrl = new URL(targetPath, request.url);
    const newRequest = new Request(rewriteUrl.toString(), request);
    return env.ASSETS.fetch(newRequest);
  }

  return context.next();
}
