
export function createNetwork(d3, data) {
 const host=document.createElement("div");
 host.innerHTML="<div id=\"concept-studio\">\n <header><h2 class=\"network-title\">Ideje su povezane.</h2><p>Odaberite pojam i istražite njegove veze. Povucite čvorove, približite mrežu ili zabilježite vlastitu misao.</p></header>\n <div class=\"toolbar\">\n  <div class=\"search\"><label for=\"concept-search\">Pronađite pojam</label><input id=\"concept-search\" list=\"concept-options\" placeholder=\"npr. standardna pogreška\" autocomplete=\"off\"><datalist id=\"concept-options\"></datalist></div>\n  <div class=\"mode\" aria-label=\"Opseg mreže\"><button data-mode=\"focus\" aria-pressed=\"true\">Bliske veze</button><button data-mode=\"all\" aria-pressed=\"false\">Cijela mreža</button></div>\n  <button class=\"pen-toggle\" aria-pressed=\"false\">Crtaj bilješke</button><button class=\"clear\" disabled>Obriši bilješke</button>\n </div>\n <p class=\"empty\" hidden role=\"status\"></p>\n <div class=\"workspace\">\n  <section class=\"map\" aria-label=\"Interaktivna mreža pojmova\">\n   <div class=\"canvas-head\"><span class=\"counts\"></span><div class=\"zoom\"><button class=\"minus\" aria-label=\"Smanji mrežu\">−</button><button class=\"plus\" aria-label=\"Povećaj mrežu\">+</button><button class=\"reset\">Posloži</button></div></div>\n   <svg aria-label=\"Mreža pojmova; pojmovi su dostupni i putem pretraživanja i popisa veza\"></svg>\n   <p class=\"map-help\">Povucite čvor · kotačić za zum · prazna ploha za pomicanje</p>\n  </section>\n  <div class=\"network-inspector\" aria-live=\"polite\"><span class=\"eyebrow\"></span><h2></h2><p class=\"network-definition\"></p><a target=\"_blank\" rel=\"noopener\">Pročitaj u poglavlju →</a><h3>Najčešće zajedno</h3><div class=\"related\"></div></div>\n </div>\n <div class=\"legend\"><span><i class=\"sample\"></i>Supojavljivanje · deblje = češće</span><span><i class=\"sample def\"></i>Veza u definiciji</span><span><i class=\"sample note\"></i>Vaše bilješke · samo u ovom prikazu</span></div>\n </div>";
 const root=host.firstElementChild; root.remove();
 const nodeById=new Map(data.nodes.map(n=>[n.id,n]));
 // Authored reading sequences, deliberately separate from co-occurrence edges.
 const journeys = [
  {name:'Od uzorka do intervala',steps:[
   ['pogreska-uzorkovanja','Različiti uzorci daju različite procjene. Pogreška uzorkovanja opisuje odstupanje procjene od populacijske vrijednosti.'],
   ['distribucija-uzorkovanja','Ponavljanjem uzorkovanja dobivamo raspodjelu mogućih vrijednosti statistike. Ona opisuje variranje procjene kroz uzorke.'],
   ['standardna-pogreska','Raspršenost distribucije uzorkovanja mjerimo standardnom pogreškom. Njome povezujemo veličinu uzorka i preciznost procjene.'],
   ['interval-pouzdanosti','Standardna pogreška sudjeluje u konstrukciji intervala. Razina pouzdanosti opisuje pokrivenost postupka kroz ponovljene uzorke.']]},
  {name:'Od povezanosti do modela',steps:[
   ['kovarijanca','Počinjemo zajedničkim variranjem dviju varijabli. Veličina kovarijance ovisi i o njihovim mjernim jedinicama.'],
   ['korelacija','Standardizacija kovarijance vodi Pearsonovoj korelaciji. Ona opisuje smjer i jačinu linearne povezanosti.'],
   ['konfundirajuca-varijabla','Za tumačenje odnosa razmatramo treće varijable. Zbirna povezanost sama po sebi ne utvrđuje uzrok.'],
   ['visestruka-regresija','Višestruka regresija opisuje odnos uz uključene druge prediktore. Tumačenje koeficijenta ovisi o modelu i istraživačkom dizajnu.']]},
  {name:'Od hipoteze do snage',steps:[
   ['nulta-hipoteza','Nulta hipoteza određuje referentni model za usporedbu s podacima.'],
   ['testna-statistika','Testna statistika sažima odstupanje podataka relevantno za tu usporedbu.'],
   ['p-vrijednost','Referentna raspodjela omogućuje izračun p-vrijednosti. Ona se računa uz pretpostavljenu nultu hipotezu.'],
   ['pogreska-prve-vrste','Odbacivanje istinite nulte hipoteze jest pogreška prve vrste. Prag odluke povezan je s kontrolom te pogreške.'],
   ['statisticka-snaga','Snaga opisuje vjerojatnost odbacivanja nulte hipoteze pri određenom stvarnom učinku. Ovisi o učinku, uzorku i postupku.']]}
 ];
 const journeyBox=document.createElement('div');journeyBox.className='concept-journey';
 const journeyLabel=document.createElement('label');journeyLabel.textContent='Vođeni put kroz pojmove';
 const journeySelect=document.createElement('select');journeySelect.setAttribute('aria-label','Odaberite vođeni put');
 journeySelect.add(new Option('Odaberite put',''));
 journeys.forEach((j,i)=>journeySelect.add(new Option(j.name,String(i))));journeyLabel.append(journeySelect);
 const journeySteps=document.createElement('div');journeySteps.className='concept-journey-steps';
 const journeyNote=document.createElement('p');journeyNote.textContent='Redoslijed učenja je autorski prijedlog. Crte na mreži i dalje prikazuju veze iz knjige.';
 const journeyExplanation=document.createElement('p');journeyExplanation.setAttribute('aria-live','polite');
 journeyBox.append(journeyLabel,journeyNote,journeySteps,journeyExplanation);root.querySelector('.toolbar').before(journeyBox);
 journeySelect.onchange=()=>{
  journeySteps.replaceChildren();journeyExplanation.textContent='';if(journeySelect.value==='')return;
  const j=journeys[+journeySelect.value];
  j.steps.forEach(([id,explanation],i)=>{const b=document.createElement('button');b.type='button';b.textContent=(i+1)+'. '+(nodeById.get(id)?.term||'Pojam izvan odabranog filtra');b.disabled=!nodeById.has(id);b.onclick=()=>{state.mode='focus';select(id);journeySteps.querySelectorAll('button').forEach(x=>x.removeAttribute('aria-current'));b.setAttribute('aria-current','step');journeyExplanation.textContent=explanation;};journeySteps.append(b);});
  journeySteps.querySelector('button:not(:disabled)')?.click();
 };

 const state={selected:data.nodes.some(n=>n.id==='standardna-pogreska')?'standardna-pogreska':data.nodes[0].id,mode:'focus',pen:false};
 const svg=d3.select(root.querySelector('svg')), map=root.querySelector('.map');
 const scene=svg.append('g'), edgesG=scene.append('g'), notesG=scene.append('g'), nodesG=scene.append('g');
 let width=700,height=520,nodes=[],edges=[],notePath=null,strokes=[],positions=new Map(),moved=false;
 const colors={ink:'var(--ink)',navy:'var(--navy)',note:'var(--note)'};
 const search=root.querySelector('input'), options=root.querySelector('datalist');
 data.nodes.slice().sort((a,b)=>a.term.localeCompare(b.term,'hr')).forEach(n=>{const o=document.createElement('option');o.value=n.term;options.appendChild(o);});
 function neighbours(id){return data.edges.filter(e=>e.source===id||e.target===id).map(e=>({id:e.source===id?e.target:e.source,edge:e})).sort((a,b)=>b.edge.cooc-a.edge.cooc||b.edge.weight-a.edge.weight);}
 function save() {}
 function inspector(){const n=nodeById.get(state.selected);root.querySelector('.network-inspector .eyebrow').textContent=n.chapterTitle;root.querySelector('.network-inspector h2').textContent=n.term;root.querySelector('.network-definition').textContent=n.firstSentence; if(window.MathJax?.typesetPromise) window.MathJax.typesetPromise([root.querySelector('.network-definition')]).catch(()=>{});root.querySelector('.network-inspector a').href=n.chapter.replace('.qmd','.html')+'#def-'+n.id;const list=root.querySelector('.related');list.replaceChildren();neighbours(n.id).slice(0,6).forEach(({id,edge})=>{const b=document.createElement('button'),label=document.createElement('span'),count=document.createElement('small');label.textContent=nodeById.get(id).term;count.textContent=edge.cooc+' ×';b.append(label,count);b.onclick=()=>select(id);list.appendChild(b);});}
 function select(id){state.selected=id;search.value=nodeById.get(id).term;draw();save();}
 const zoom=d3.zoom().scaleExtent([.85,3]).filter(e=>!state.pen && (!e.button || e.type==='wheel')).on('zoom',e=>scene.attr('transform',e.transform));
 svg.call(zoom).on('dblclick.zoom',null);
 function tick(){edgesG.selectAll('line').attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);nodesG.selectAll('.node').attr('transform',d=>`translate(${d.x},${d.y})`);}
 function draw(){
  width=Math.max(280,map.clientWidth);height=width<500?440:520;svg.attr('viewBox',`0 0 ${width} ${height}`).style('height',height+'px');
  const near=neighbours(state.selected).slice(0,width<500?4:8),set=new Set([state.selected,...near.map(n=>n.id)]);
  nodes=data.nodes.filter(n=>state.mode==='all'||set.has(n.id)).map((n,i)=>{const p=positions.get(n.id);return {...n,x:p?.[0]??width/2+Math.cos(i*2.399)*130,y:p?.[1]??height/2+Math.sin(i*2.399)*130};});
  const ids=new Set(nodes.map(n=>n.id));
  edges=data.edges.filter(e=>ids.has(e.source)&&ids.has(e.target)&&(state.mode==='focus'?(e.source===state.selected||e.target===state.selected):(e.cooc>=4||e.type==='def'))).map(e=>({...e}));
  const selected=nodes.find(n=>n.id===state.selected);if(!positions.has(selected.id)){selected.fx=width/2;selected.fy=height/2;}
  const sim=d3.forceSimulation(nodes).force('link',d3.forceLink(edges).id(n=>n.id).distance(state.mode==='focus'?165:85).strength(.25)).force('charge',d3.forceManyBody().strength(state.mode==='focus'?-500:-110)).force('x',d3.forceX(width/2).strength(.09)).force('y',d3.forceY(height/2).strength(.13)).force('collision',d3.forceCollide(state.mode==='focus'?64:20)).stop();
  for(let i=0;i<180;i++)sim.tick();if(state.mode==='all'){const sx=d3.scaleLinear().domain(d3.extent(nodes,n=>n.x)).range([85,width-85]),sy=d3.scaleLinear().domain(d3.extent(nodes,n=>n.y)).range([35,height-75]);nodes.forEach(n=>{n.x=sx(n.x);n.y=sy(n.y);});}nodes.forEach(n=>{n.x=Math.max(85,Math.min(width-85,n.x));n.y=Math.max(35,Math.min(height-70,n.y));});
  edgesG.selectAll('line').data(edges).join('line').attr('stroke',e=>e.type==='def'?colors.navy:colors.ink).attr('stroke-opacity',e=>state.mode==='focus'?.38:.2).attr('stroke-width',e=>Math.min(3.5,.6+e.cooc*.17)).attr('stroke-dasharray',e=>e.type==='def'?'5 5':null);
  const group=nodesG.selectAll('.node').data(nodes,n=>n.id).join(enter=>{const g=enter.append('g').attr('class','node');g.append('circle');g.append('text').attr('class','chapter');const fo=g.append('foreignObject').attr('x',-82).attr('y',-20).attr('width',164).attr('height',84);fo.append('xhtml:button').attr('type','button').append('xhtml:span');return g;});
  group.select('foreignObject').attr('x',width<500?-70:-82).attr('width',width<500?140:164);
  const labelled=new Set(),boxes=[];[selected,...near.map(v=>nodes.find(n=>n.id===v.id)).filter(Boolean)].forEach(n=>{const box={x:n.x-82,y:n.y+14,w:164,h:43};if(!boxes.some(b=>Math.abs((b.x+b.w/2)-(box.x+box.w/2))<(b.w+box.w)/2+4 && Math.abs((b.y+b.h/2)-(box.y+box.h/2))<(b.h+box.h)/2+4)){boxes.push(box);labelled.add(n.id);}});
  group.attr('class',n=>'node'+(n.id===state.selected?' selected':'')+(labelled.has(n.id)?' labelled':''));
  group.on('mouseenter',function(){d3.select(this).classed('labelled',true).raise();}).on('mouseleave',function(e,n){d3.select(this).classed('labelled',labelled.has(n.id));});
  group.select('circle').attr('r',n=>n.id===state.selected?21:state.mode==='focus'?14:7+Math.min(4,n.mentions*.2));
  group.select('.chapter').text(n=>state.mode==='focus'||n.id===state.selected?(n.chapter.match(/\/(\d+)/)||[])[1]:'');
  group.select('button').attr('aria-label',n=>n.term+'. Povucite za pomicanje ili pritisnite Enter za istraživanje veza.').on('click',(e,n)=>{if(!e.defaultPrevented)select(n.id);}).on('keydown',(e,n)=>{const moves={ArrowLeft:[-10,0],ArrowRight:[10,0],ArrowUp:[0,-10],ArrowDown:[0,10]};if(moves[e.key]){e.preventDefault();n.x+=moves[e.key][0];n.y+=moves[e.key][1];positions.set(n.id,[n.x,n.y]);tick();save();}}).select('span').text(n=>n.term);
  group.on('click',(e,n)=>{if(e.target.tagName==='circle'&&!e.defaultPrevented)select(n.id);});
  group.call(d3.drag().filter(()=>!state.pen).on('start',()=>{moved=false;}).on('drag',(e,n)=>{moved=true;n.x=e.x;n.y=e.y;positions.set(n.id,[n.x,n.y]);tick();}).on('end',()=>{if(moved)save();}));
  tick();inspector();root.querySelector('.counts').textContent=state.mode==='focus'?`${nodes.length} od ${data.nodes.length} pojmova · ${near.length} najbližih veza`:`${nodes.length} pojma · ${edges.length} jačih i definicijskih veza`;
  root.querySelectorAll('[data-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===state.mode)));
 }
 function renderNotes(){notesG.selectAll('path').data(strokes).join('path').attr('d',p=>d3.line()(p)).attr('fill','none').attr('stroke',colors.note).attr('stroke-width',2.5).attr('stroke-linecap','round').attr('pointer-events','none');root.querySelector('.clear').disabled=!strokes.length;}
 svg.on('pointerdown.notes',e=>{if(!state.pen)return;e.preventDefault();svg.node().setPointerCapture(e.pointerId);notePath=[];strokes.push(notePath);notePath.push(d3.zoomTransform(svg.node()).invert(d3.pointer(e)));renderNotes();}).on('pointermove.notes',e=>{if(!notePath)return;notePath.push(d3.zoomTransform(svg.node()).invert(d3.pointer(e)));renderNotes();}).on('pointerup.notes pointercancel.notes',()=>{if(notePath){notePath=null;save();}});
 root.querySelector('.pen-toggle').onclick=e=>{state.pen=!state.pen;e.currentTarget.setAttribute('aria-pressed',String(state.pen));map.classList.toggle('pen',state.pen);root.querySelector('.map-help').textContent=state.pen?'Crtajte po mreži. Vaše bilješke ne mijenjaju veze iz knjige.':'Povucite čvor · kotačić za zum · prazna ploha za pomicanje';};
 root.querySelector('.clear').onclick=()=>{strokes=[];renderNotes();save();};
 root.querySelectorAll('[data-mode]').forEach(b=>b.onclick=()=>{state.mode=b.dataset.mode;svg.call(zoom.transform,d3.zoomIdentity);draw();save();});
 root.querySelector('.plus').onclick=()=>svg.call(zoom.scaleBy,1.25);root.querySelector('.minus').onclick=()=>svg.call(zoom.scaleBy,.8);
 root.querySelector('.reset').onclick=()=>{positions.clear();svg.call(zoom.transform,d3.zoomIdentity);draw();save();};
 function find(){const q=search.value.toLocaleLowerCase('hr').trim();const n=data.nodes.find(n=>n.term.toLocaleLowerCase('hr')===q)||data.nodes.find(n=>n.term.toLocaleLowerCase('hr').includes(q));const msg=root.querySelector('.empty');if(n&&q){msg.hidden=true;select(n.id);}else{msg.textContent='Nema pojma za taj upit. Pokušajte s drugim nazivom.';msg.hidden=false;}}
 search.addEventListener('change',find);search.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();find();}});
 function restore(snapshot){const s=snapshot?.modelContent||snapshot,p=snapshot?.privateContent;if(s&&nodeById.has(s.selectedConcept)){state.selected=s.selectedConcept;state.mode=s.view==='all'?'all':'focus';}if(p?.positions)positions=new Map(p.positions.filter(v=>Array.isArray(v)&&nodeById.has(v[0])));if(p?.notes)strokes=p.notes;search.value=nodeById.get(state.selected).term;draw();renderNotes();}
 restore(null);
 let lastWidth=map.clientWidth;const observer=new ResizeObserver(()=>{if(Math.abs(lastWidth-map.clientWidth)>2){lastWidth=map.clientWidth;positions.clear();draw();}});observer.observe(map);
 root.dispose=()=>observer.disconnect();
 return root;
}

