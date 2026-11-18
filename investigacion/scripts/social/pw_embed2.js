const { chromium } = require('playwright');
(async()=>{
 const out=process.argv[2]; const ids=process.argv.slice(3);
 const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required','--mute-audio']});
 const p=await b.newPage({viewport:{width:400,height:720},userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'});
 for(const id of ids){
  try{
   await p.goto('https://www.tiktok.com/embed/v2/'+id,{waitUntil:'domcontentloaded',timeout:45000});
   await p.waitForTimeout(5000);
   await p.screenshot({path:`${out}/${id}_0.png`});
   await p.mouse.click(200,290);
   const marks=[1.5,3.5,8];
   for(const m of marks){
     const ok=await p.waitForFunction((m)=>{const v=document.querySelector('video');return v&&v.currentTime>=m},m,{timeout:15000}).then(()=>true).catch(()=>false);
     const info=await p.evaluate(()=>{const v=document.querySelector('video');return v?{t:v.currentTime,d:v.duration,err:v.error&&v.error.code,rs:v.readyState}:null});
     console.log(id,m,ok,JSON.stringify(info));
     await p.screenshot({path:`${out}/${id}_${m}.png`});
   }
  }catch(e){console.log(id,'ERR',String(e).slice(0,150))}
 }
 await b.close();})();
