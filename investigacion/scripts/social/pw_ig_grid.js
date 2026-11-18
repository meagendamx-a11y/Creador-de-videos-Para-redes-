const { chromium } = require('playwright');
(async()=>{
 const out=process.argv[2];
 const b=await chromium.launch(); const p=await b.newPage({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36',locale:'es-MX',viewport:{width:1000,height:1800}});
 for (const h of process.argv.slice(3)){
  try{ await p.goto('https://www.instagram.com/'+h+'/',{waitUntil:'domcontentloaded',timeout:45000}); await p.waitForTimeout(18000);
   const posts=await p.evaluate(()=>[...document.querySelectorAll('a[href*="/p/"],a[href*="/reel/"]')].map(a=>({href:a.getAttribute('href'),alt:(a.querySelector('img')||{}).alt||null,labels:[...a.querySelectorAll('svg[aria-label]')].map(s=>s.getAttribute('aria-label'))})));
   console.log(JSON.stringify({h,n:posts.length,posts}));
   const first=await p.$('a[href*="/p/"],a[href*="/reel/"]');
   if(first){ await first.scrollIntoViewIfNeeded(); await p.waitForTimeout(2500); }
   await p.screenshot({path:`${out}/grid_${h}.png`});
  }catch(e){console.log(JSON.stringify({h,err:String(e).slice(0,200)}))}
 }
 await b.close();})();
