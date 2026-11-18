const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36',locale:'es-MX',viewport:{width:1280,height:2000}});
 for (const h of process.argv.slice(2)){
  try{ await p.goto('https://www.instagram.com/'+h+'/',{waitUntil:'domcontentloaded',timeout:45000}); await p.waitForTimeout(18000);
   const posts=await p.evaluate(()=>[...document.querySelectorAll('a[href*="/p/"],a[href*="/reel/"]')].map(a=>({href:a.getAttribute('href'),alt:(a.querySelector('img')||{}).alt||null, carousel: !!a.querySelector('svg[aria-label*="Carrusel"],svg[aria-label*="Carousel"],svg[aria-label*="Clip"],svg[aria-label*="secuencia"]'), labels:[...a.querySelectorAll('svg[aria-label]')].map(s=>s.getAttribute('aria-label'))})));
   console.log(JSON.stringify({h,n:posts.length,posts}));
  }catch(e){console.log(JSON.stringify({h,err:String(e).slice(0,200)}))}
 }
 await b.close();})();
