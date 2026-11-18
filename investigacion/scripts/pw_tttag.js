const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36',locale:'es-MX'});
 const url=process.argv[2];
 await p.goto(url,{waitUntil:'domcontentloaded',timeout:60000}); await p.waitForTimeout(20000);
 const links=await p.evaluate(()=>[...document.querySelectorAll('a[href*="/video/"]')].map(a=>a.href));
 console.log(JSON.stringify({title:await p.title(),n:links.length,links:[...new Set(links)].slice(0,60),txt:(await p.evaluate(()=>document.body.innerText)).slice(0,500)}));
 await p.screenshot({path:'/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/social/tag_shot.png'});
 await b.close();})();
