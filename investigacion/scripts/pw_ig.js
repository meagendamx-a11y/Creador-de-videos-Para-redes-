const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36',locale:'es-MX'});
 for (const h of process.argv.slice(2)){
  try{ await p.goto('https://www.instagram.com/'+h+'/',{waitUntil:'domcontentloaded',timeout:45000}); await p.waitForTimeout(18000);
   const d=await p.evaluate(()=>({t:document.title,og:(document.querySelector('meta[property="og:description"]')||{}).content||null,body:document.body.innerText.slice(0,300)}));
   console.log(JSON.stringify({h,...d}));
  }catch(e){console.log(JSON.stringify({h,err:String(e).slice(0,200)}))}
 }
 await b.close();})();
