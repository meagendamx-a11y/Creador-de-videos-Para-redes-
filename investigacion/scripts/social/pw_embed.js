const { chromium } = require('playwright');
(async()=>{
 const out=process.argv[2]; const ids=process.argv.slice(3);
 const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});
 const p=await b.newPage({viewport:{width:400,height:720},userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'});
 for(const id of ids){
  try{
   await p.goto('https://www.tiktok.com/embed/v2/'+id,{waitUntil:'domcontentloaded',timeout:45000});
   await p.waitForTimeout(6000);
   const info=await p.evaluate(()=>{const v=document.querySelector('video');return v?{src:!!v.currentSrc,dur:v.duration,t:v.currentTime,paused:v.paused}:null});
   console.log(id,JSON.stringify(info));
   await p.screenshot({path:`${out}/${id}_a.png`});
  }catch(e){console.log(id,'ERR',String(e).slice(0,150))}
 }
 await b.close();})();
