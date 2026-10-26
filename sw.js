/* Silverwing public-only service worker. No private data or authenticated caching. */
const VERSION = "silverwing-public-v8";
const CORE = ["./","./index.html","./manifest.webmanifest","./assets/icon-192.png","./assets/icon-512.png","./assets/silverwing-harpy-mark.svg","./assets/harpy-eagle-cinema.png","./assets/andes-cinema.png","./assets/amazon-cinema.png","./assets/patagonia-cinema.png","./assets/editorial-glass-cinema.png"];
self.addEventListener("install",event=>{event.waitUntil(caches.open(VERSION).then(cache=>cache.addAll(CORE)));self.skipWaiting()});
self.addEventListener("activate",event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith("silverwing-public-")&&k!==VERSION).map(k=>caches.delete(k)))));self.clients.claim()});
self.addEventListener("fetch",event=>{const req=event.request;if(req.method!=="GET"||new URL(req.url).origin!==self.location.origin)return;
if(new URL(req.url).pathname.endsWith("/catalog.json")||new URL(req.url).pathname.endsWith("/i18n.js")){event.respondWith(fetch(req,{cache:"no-store"}));return}
if(req.mode==="navigate"){event.respondWith(fetch(req).then(res=>{if(res.ok){const copy=res.clone();caches.open(VERSION).then(c=>c.put("./index.html",copy))}return res}).catch(()=>caches.match("./index.html")));return}
event.respondWith(caches.match(req).then(cached=>cached||fetch(req).then(res=>{if(res.ok){const copy=res.clone();caches.open(VERSION).then(c=>c.put(req,copy))}return res})))
});