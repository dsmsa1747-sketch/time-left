const CACHE="timeleft-v13";
const ASSETS=["./","index.html","privacy.html","terms.html","manifest.webmanifest","icon-192.png","icon-512.png","apple-touch-icon.png","og.png","v/surgery.webm","v/smoke.webm","v/tray.webm","v/dawn.webm","v/lungs.webm","v/field.webm"];
self.addEventListener("install",e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()));
});
self.addEventListener("activate",e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));
});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET") return;
  e.respondWith(
    caches.match(e.request).then(hit=>hit || fetch(e.request).then(res=>{
      if(res && res.status===200 && res.type==="basic"){
        const copy=res.clone();
        caches.open(CACHE).then(c=>c.put(e.request,copy));
      }
      return res;
    }).catch(()=>caches.match("/index.html")))
  );
});