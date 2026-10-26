// End-to-end learning tools audit. Run after HTML rendering:
// node scripts/audit-learning-tools.cjs [path-to-docs]
const {chromium}=require('playwright');
const fs=require('node:fs');const path=require('node:path');const http=require('node:http');const assert=require('node:assert/strict');
const root=path.resolve(process.argv[2]||'docs');
const registry=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/widgets.json'),'utf8'));
const server=http.createServer((req,res)=>{let file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return;}fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'})[path.extname(file)]||'application/octet-stream');res.end(data);});});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const base=`http://127.0.0.1:${server.address().port}/`;
 const browser=await chromium.launch();
 try {
  const context=await browser.newContext({viewport:{width:1280,height:1000},permissions:['clipboard-read','clipboard-write']});const p=await context.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
  for(const w of registry.widgets){
   await p.goto(base+w.poglavlje.replace('.qmd','.html'));await p.locator('.experiment-live').waitFor();await p.locator('[id^="fig-w"] svg').first().waitFor();await p.waitForTimeout(750);
   assert.equal(await p.locator('.experiment-lesson').count(),1,w.id+' task');
   const before=await p.locator('[data-learning-form]').evaluate(f=>f.value);
   const changed=await p.locator('[data-learning-form]').evaluate(f=>{const v={...f.value};const key=Object.keys(v).find(k=>typeof v[k]==='number');if(key){const i=Object.keys(v).indexOf(key);const form=f.querySelectorAll('form')[i];const input=form.querySelector('input[type=range]');if(input)v[key]=Number(input.value)+Number(input.step)<=Number(input.max)?Number(input.value)+Number(input.step):Number(input.value)-Number(input.step);}else {const key=Object.keys(v)[0];const form=f.querySelector('form');const select=form.querySelector('select');v[key]=select.options[(select.selectedIndex+1)%select.length].textContent;}f.value=v;f.dispatchEvent(new Event('input',{bubbles:true}));return f.value;});
   await p.waitForFunction(expected=>{const e=document.querySelector('[data-experiment-state]');return e&&e.dataset.experimentState===JSON.stringify(expected);},changed);
   await p.waitForTimeout(350);
   assert(!/NaN|undefined/.test(await p.locator('.experiment-live').innerText()),w.id+' interpretation');
   await p.getByRole('button',{name:'Usporedi s ovim rezultatom',exact:true}).click();assert(await p.locator('.experiment-comparison').isVisible());
   if(['w08','w09','w11'].includes(w.id))assert.equal(await p.locator('.experiment-comparison svg').count(),2,w.id+' paired plots');
   await p.locator('.experiment-lesson textarea').fill('PRIVATE-PREDICTION');
   await p.getByRole('button',{name:'Kopiraj poveznicu na ovaj prikaz'}).click();const url=await p.evaluate(()=>navigator.clipboard.readText());assert(!url.includes('PRIVATE-PREDICTION'));
   const fresh=await browser.newContext({viewport:{width:1280,height:1000}});const q=await fresh.newPage();q.on('pageerror',e=>errors.push(e.message));await q.goto(url);await q.locator('.experiment-live').waitFor();await q.waitForTimeout(900);
   assert.deepEqual(await q.locator('[data-learning-form]').evaluate(f=>f.value),changed,w.id+' restored parameters');
   assert.equal(await q.locator('.experiment-lesson textarea').inputValue(),'');
   // Fixed random streams must yield the same rendered geometry at the same width.
   const geometry=page=>page.locator('[id^="fig-w"] svg').first().evaluate(s=>[...s.querySelectorAll('path,line,circle,rect')].map(e=>['d','x','y','x1','x2','y1','y2','cx','cy','r','width','height'].map(k=>e.getAttribute(k))));
   assert.deepEqual(await geometry(q),await geometry(p),w.id+' reproduced chart');await fresh.close();
   await p.setViewportSize({width:390,height:900});await p.waitForTimeout(300);assert(await p.locator('.widget-frame').evaluate(e=>e.scrollWidth<=e.clientWidth+2),w.id+' mobile overflow');await p.setViewportSize({width:1280,height:1000});
   console.log(w.id+' PASS');
  }
  await p.goto(base+'index.html');await p.locator('h1.hero-title').waitFor();
  assert.equal(await p.locator('#landing-sample-size').count(),0);
  for (const [name, file] of [['Luka Šikić — osobni profil','cv-luka.html'],['Petra Palić — osobni profil','cv-petra.html']]) {
   await p.getByRole('link',{name,exact:true}).click();assert(p.url().endsWith(file));await p.locator('.author-profile h1.name').waitFor();await p.goto(base+'index.html');
  }
  await p.goto(base+'pojmovnik.html?pojam=interval-pouzdanosti');
  await p.locator('.atlas-definition h2').waitFor();
  assert.equal(await p.locator('.atlas-definition h2').innerText(),'Interval pouzdanosti');
  assert((await p.locator('.atlas-chapter').getAttribute('href')).endsWith('#def-interval-pouzdanosti'));
  const graph=JSON.parse(fs.readFileSync(path.join(root,'data/concept-graph.json'),'utf8'));
  assert.equal(await p.locator('.atlas-node').count(),graph.nodes.length);
  assert.deepEqual(errors,[]);console.log('LEARNING_TOOLS_OK widgets=17 landing=pass authors=pass atlas=pass sharing=pass reproducibility=pass mobile=pass');
 } finally {await browser.close();await new Promise(r=>server.close(r));}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
