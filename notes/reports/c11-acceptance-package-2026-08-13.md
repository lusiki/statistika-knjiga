# C11 — paket za autorovo prihvaćanje jedanaestoga poglavlja

**Gate:** `C11`

**Stanje gatea:** autor prihvatio; dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 13. kolovoza 2026.

**Datum autorove odluke:** 13. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor jedanaestoga poglavlja nalazi se u commitu
`00c40c9ebc0627ec8dda9f25d1ee70465f4861c9`. Taj commit sadrži cijeli WC-C11
vertikalni rez, svih šest završnih izvještaja, sintezu i closeout dokaze.
Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`;
- Git blob poglavlja: `87db0124679ae2085f87c4e7cc4145f9e3191b8f`;
- izvještaj vertikalnoga reza:
  `notes/reports/wc-c11-2026-08-12.md`;
- sinteza panela:
  `notes/reports/wc-c11-six-critic-synthesis-2026-08-12.md`.

## Šest završnih izvještaja

Svih šest neovisnih kritičara samo za čitanje pregledalo je upravo navedeni
SHA-256:

1. metode — `notes/reports/wc-c11-critic-methods-2026-08-12.md`;
2. skepticizam — `notes/reports/wc-c11-critic-skeptic-2026-08-12.md`;
3. pedagogija — `notes/reports/wc-c11-critic-pedagogy-2026-08-12.md`;
4. dokazi i citati — `notes/reports/wc-c11-critic-evidence-2026-08-12.md`;
5. hrvatski stil — `notes/reports/wc-c11-critic-style-2026-08-12.md`;
6. struktura — `notes/reports/wc-c11-critic-structure-2026-08-12.md`.

Završni panel bilježi nula fatalnih, nula velikih i trinaest neblokirajućih
minor zapisa po lećama. Dokazni kritičar nema nijedan nalaz. Zajednički hash
nije mijenjan nakon panela.

## Razriješena dva obvezna nalaza

Autor je 13. kolovoza 2026. odobrio upravo dva obvezna popravka prvoga prolaza.
Oba su provedena i ponovno neovisno provjerena:

1. diskretna raspodjela sada odvojeno prikazuje 53,6 % stroge nadmoći, 13,9 %
   izjednačenja i 60,6 % mjere s polovicom izjednačenja;
2. primjer planiranja više ne računa kružnu opaženu snagu, nego polazi od
   unaprijed zadanoga cilja 0,5 uz SD 1,9, pa dobiva `d = 0,2632` i 228 osoba
   po skupini za 80 % snage.

Metodološki završni pregled potvrđuje da su prethodni fatalni i major nalaz
potpuno razrijeđeni. Novi dokazni pregled reproducira sve cijele omjere i
planski račun.

## Trinaest minor zapisa za dispoziciju u C11

Sukladno autorovoj uputi, nijedan od sljedećih nalaza nije popravljen unutar
WC-C11. Oni ostaju vidljivi i neblokirajući u ovom gateu.

### Metode — 1

1. Izraz „procjena unutar pola boda” ne razlikuje poluširinu od ukupne širine
   intervala i lokalno ne ponavlja uvjete jednakih neovisnih skupina te poznate
   zajedničke standardne devijacije.

### Skepticizam — 3

2. Lokalni spoj „puna populacija”, „istina” i urednička odluka mogao bi jasnije
   reći da je riječ o opisnoj razlici u simuliranoj populaciji: puni obuhvat ne
   uklanja samoodabir, ne stvara uzročni učinak i ne jamči generalizaciju.
3. „Zajednički jezik” standardizacije mogao bi izričito upozoriti da broj ne
   izjednačuje konstrukte, populacije ni kvalitetu mjerenja.
4. Najmanji važan učinak pripisan je preusko samom istraživaču; prag bi se mogao
   prikazati kao obrazloženi prijedlog koji uključuje relevantne donositelje
   odluka ili pogođene skupine, uz vezu planiranoga uzorka s pragom,
   raspršenošću i uporabljivim opažanjima.

### Pedagogija — 3

5. Simboli `d` i `s_zdr` mogli bi biti objašnjeni prije prve formule.
6. Permutacijska krivulja rabi ukupan `n`, a widget i z-primjer broj jedinica
   po skupini; ta dva značenja i pripadne snage mogla bi biti izravnije
   razdvojena.
7. HTML zadatak zadaje 1.500 ponavljanja, dok tiskana tablica i rješenje rabe
   2.000; ruta bi mogla zadati jedinstven broj i toleranciju ili zasebne
   očekivane rezultate.

### Hrvatski stil — 5

8. Nekoliko prijelaza otkriva montažnu skelu formulacijama poput „Poglavlje
   nastavlja…” i „Analiza ispod…”.
9. Naslovi „Kad je značajno, a nije važno” i „Podsnažene studije pretjeruju”
   nisu nominalni, a prvi odlomak odjeljka o snazi djelomice ponavlja naslov.
10. Ograda simulacijskoga faktora i upozorenje da mala snaga nije presuda
    ponavljaju se u tijelu i okviru divljine.
11. Početak sažetka „Veličina učinka vraća pitanju…” nije idiomatski dovršena
    hrvatska rečenica.
12. „Rečenica tog oblika” ima labav antecedent, a red riječi u uvjetnoj
    rečenici o najmanjoj važnoj razlici ostaje težak.

### Struktura — 1

13. Zajedničke upute za interakciju obećavaju promjenu praga i `d = 0,10`, ali
    tiskani blizanac fiksira prag na 0,05 i prikazuje samo `d = 0,2`, `0,4` i
    `0,6`; tiskani preset ili upute mogli bi potpunije odgovarati toj ruti.

Broj 13 označuje zapise po lećama, ne trinaest međusobno neovisnih defekata;
neki se stilski, pedagoški i skeptički zapisi dodiruju. Nijedan kritičar nije
ocijenio ijedan od njih fatalnim ili velikim.

## Materijalna osnova preporuke

Preporuka je **prihvatiti** zaključano stanje s navedenih trinaest minora kao
poznatim, neblokirajućim nalazima. Poglavlje vodi od učinka u izvornim
jedinicama preko standardizacije, praktične važnosti i snage do selekcijskoga
pretjerivanja i planiranja unatrag. Niska snaga nije pretvorena u presudu o
istinitosti, a pretjerivanje je omeđeno na konkretan simulacijski sustav.

Kanonski sedmodijelni poredak je vraćen. Tiskani zadatak ima ocjenjiv put, živi
w11 i parity adapter rabe isti necachirajući generator, a stvarni zlatni izlazi
i namjerno pogrešan cached-pair fixture prolaze odnosno padaju zatvoreno bez
širenja tolerancije. Podaci, citati, pojmovi, figure, HTML, odobreni PDF wrapper
i DOCX wrapper imaju zapisane prolaze na zaključanom izvoru.

## Provedena uska dispozicija

C11 je nakon provjere točnoga odgovora proveo samo sljedeće:

- pomaknuti `11-velicina-ucinka-i-snaga` iz `draft` u `coauthor_review`, uz
  izričitu bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da
  to nije faza `final`;
- pomaknuti iz `ratified` u `accepted` samo `R17-C11-exaggeration`,
  `R17-C11-low-power`, `R32-C11-static` i `R35-REACHBACK-11`;
- ostaviti već prihvaćeni `R04-C11-fixed-order` te prihvaćene bazne stavke
  `R01-C11-inherited-permutation` i `R09-C11-power-assumptions` nepromijenjene;
- evidentirati trinaest minor zapisa kao autoru izložene, poznate i
  neblokirajuće za ovo izdanje, bez naknadne promjene zaključanoga izvora;
- ostaviti poglavlje 6 u fazi `draft` i `H-WB-PART-001` netaknutim.

Nijedna druga stavka ni poglavlje nisu promijenili status. R04 je ostao
otvoren jer njegova tri preostala djeteta pripadaju paketima `WE-C18` i
`P5-ROUTES`.

## Granice odluke

C11 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge,
tag, arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao
poglavlje. Gate ne otvara `G-A4-12` prije vlastitoga closeouta, workflow
provjere i zasebnoga lokalnog commita.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
C11 accepted for 00c40c9ebc0627ec8dda9f25d1ee70465f4861c9 on 2026-08-13.
```

Odgovor navodi točan završni WC-C11 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.

`G-A4-12` se smije otvoriti tek nakon dovršenoga C11 closeouta, workflow
provjere i zasebnoga lokalnog commita.
