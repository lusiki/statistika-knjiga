// Presentation-only diagrams: no observations or simulation results are encoded.
// The real, seeded computations remain in the chapter widgets.
const cards = {
  w01: ["Kako sastav skupina može preokrenuti zaključak?", "groups"],
  w02: ["Što se dogodi s povezanošću kada razdvojimo skupine?", "scatter"],
  w03: ["Koliko je precizna procjena iz ankete?", "intervals"],
  w04: ["Kako oblik podataka mijenja njihove sažetke?", "distribution"],
  w05: ["Kako isti podaci mogu ispričati različite priče?", "bars"],
  w06: ["Koliko su dvije varijable povezane?", "scatter"],
  w07: ["Kako se slučajni ishodi mijenjaju kroz ponavljanja?", "sequence"],
  w08: ["Zašto veći uzorci daju stabilnije procjene?", "distribution"],
  w09: ["Koliko intervala obuhvaća stvarnu vrijednost?", "intervals"],
  w10: ["Koliko je rezultat neobičan pod nultom hipotezom?", "distribution"],
  w11: ["Kada istraživanje može otkriti učinak?", "curves"],
  w12: ["Što se događa kada isprobavamo sve više analiza?", "sequence"],
  w13: ["Koliko se opaženo razlikuje od očekivanoga?", "bars"],
  w14: ["Koliko razlika dviju grupa ovisi o uzorku?", "groups"],
  w15: ["Koliko varijabilnosti dolazi od razlika među grupama?", "groups"],
  w16: ["Kako pravac sažima povezanost dviju varijabli?", "regression"],
  w17: ["Kako prag odluke mijenja pogreške među skupinama?", "bars"]
};

export function question(id) { return cards[id][0]; }

export function topic(id) {
  const n = Number(id.slice(1));
  return n <= 3 ? "Statističko mišljenje" : n <= 6 ? "Opisivanje podataka" :
    n <= 9 ? "Od uzorka do populacije" : n <= 12 ? "Zaključivanje" : "Modeli";
}

export function preview(id) {
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", "0 0 240 128");
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  function mark(tag, attrs, className = "gallery-primary") {
    const node = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, String(v)));
    node.setAttribute("class", className);
    svg.appendChild(node);
  }
  const kind = cards[id][1];
  if (kind === "distribution") {
    [5, 12, 28, 49, 73, 87, 73, 49, 28, 12, 5].forEach((h, i) =>
      mark("rect", {x: 27 + i * 17, y: 107 - h, width: 13, height: h}));
    mark("line", {x1: 118, x2: 118, y1: 12, y2: 111}, "gallery-axis");
  } else if (kind === "scatter" || kind === "regression") {
    [[28,91],[40,67],[57,83],[72,51],[87,66],[101,43],[117,63],
      [133,35],[149,49],[166,25],[183,38],[207,17]].forEach(([cx,cy]) =>
      mark("circle", {cx, cy, r: 5}));
    if (kind === "regression") mark("line", {x1: 24, y1: 91, x2: 216, y2: 20}, "gallery-axis");
  } else if (kind === "intervals") {
    [[62,151],[89,173],[49,136],[131,208],[76,160]].forEach(([a,b],i) => {
      const y = 24 + i * 18;
      mark("line", {x1:a,x2:b,y1:y,y2:y}, "gallery-interval");
      mark("circle", {cx:(a+b)/2,cy:y,r:4});
    });
    mark("line", {x1:120,x2:120,y1:12,y2:108,"stroke-dasharray":"4 4"}, "gallery-axis");
  } else if (kind === "groups") {
    [0,1].forEach(g => [0,1,2,3,4,5].forEach(i => {
      const x=48+g*110+(i%3)*14, y=77-Math.floor(i/3)*19-g*24;
      mark(g ? "rect" : "circle", g ? {x:x-5,y:y-5,width:10,height:10} : {cx:x,cy:y,r:5},
        g ? "gallery-secondary" : "gallery-primary");
    }));
  } else if (kind === "bars") {
    [58,82,44,65].forEach((h,i)=>{
      mark("rect",{x:30+i*48,y:107-h,width:15,height:h});
      mark("rect",{x:48+i*48,y:107-h*.7,width:15,height:h*.7},"gallery-secondary");
    });
  } else if (kind === "curves") {
    [88,153].forEach((mid,i)=>{
      let d="";
      for(let x=20;x<=220;x+=2) d+=(x===20?"M":"L")+x+","+(106-76*Math.exp(-(((x-mid)/32)**2)));
      mark("path",{d},i?"gallery-curve-secondary":"gallery-curve");
    });
  } else {
    for(let i=0;i<24;i++) mark("circle",{cx:35+(i%8)*24,cy:32+Math.floor(i/8)*28,r:7},
      i%5===0?"gallery-secondary":"gallery-primary");
  }
  mark("line",{x1:18,x2:224,y1:110,y2:110},"gallery-axis");
  return svg;
}
