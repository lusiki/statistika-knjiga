# G-A2b-IV — ratificirana kralježnica Dijela IV

**Gate:** `G-A2b-IV`

**Datum odluke:** 4. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2b-IV-spine-approved-2026-08-04-Luka-Sikic`, vezano uz nacrt
kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu Dijela IV: nosive aspekte,
nosive pojmove, preduvjete i isključenja za poglavlja 10, 11 i 12, ugovor na
razini dijela te hijerarhiju definicija kojom se rješava stavka
`R04-C12-definitions`. Ne odobrava prozu, ne dodaje i ne uklanja nijedan `#def-`
blok i ne ratificira nijednu kasniju kralježnicu.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-IV-SPINE`, upravljane stavke `R04-SPINE-IV` i `R04-C12-definitions`,
ratificirani identitetski brif `c12` u `conventions.json#identity_briefs`,
prihvaćene arhitekture `G-A2a` i `G-A2d`, ratificirane kralježnice predgovora te
Dijelova I, II i III, zabilježena autorova namjera, pravilo `H10` u `STYLE.md`,
pojasevi `bands` u `conventions.json` te sve stavke registra koje ciljaju
poglavlja 10, 11 i 12, uključujući prihvaćene ispravke paketa `P1A-C10` i
`P1A-C11` te prihvaćenu odluku D01.

Cjeloviti ledger prijenosa pročitan je prije odluke. Nijedan prijenos ne cilja
`G-A2b-IV`, pa nema dolazne isporuke koju bi ovaj gate priznao ili potrošio.
`H-P1C-INTEGRITY-002` cilja `P2-TERMS`, ostaje `pending` i zamrzava skup od 46
živih definicija, pa ovaj gate odlučuje samo kartu definicija.

## Ugovor na razini Dijela IV

Dio IV nosi tri koraka i ništa više: **što test može, a što ne može odgovoriti**,
zatim **koliko je velik učinak i koliko stoji pogreška**, zatim **što
istraživački sustav radi s dokazom**. Redoslijed poglavlja 10, 11 i 12 ostaje
nepromijenjen, prema odluci D03.

Ono što vodi nije mehanika. **Vode veličina učinka i posljedice pogreške**, i one
upravljaju čitanjem svakoga testa u dijelu. Poredak u kojemu mehanika testiranja
dolazi prva **izričito je odbijen**: poglavlje 10 gradi svijet bez učinka
simulacijom prije nego što imenuje nultu hipotezu, uvodi asimetriju odluke prije
praga, i o pragu govori kao o konvenciji, a ne kao o mjeri. Knjiga ostaje
estimacijska: procjena i interval iz poglavlja 9 nose zaključak, a test odgovara
na jedno usko pitanje unutar toga okvira.

Testiranje značajnosti poučava se **s poviješću i sa zlouporabama**, a ne kao
postupak. Epizoda Američkoga statističkog udruženja glavni je instruktivni slučaj
poglavlja 10, i ondje je zato što je povijest dio sadržaja, a ne ukras.

Poglavlje 12 ostaje **jedan dokazima vođen argument o istraživačkom sustavu**, a
ne popis reformi. Njegova je kralježnica podređena ratificiranom identitetskom
brifu `c12` i ne ponavlja ga: brif određuje argument, njegove obvezne sastavnice i
dokazni artefakt, a kralježnica određuje što poglavlje mora nositi kao pojam,
preduvjet i granicu.

Dio naglašava pet faza životnoga ciklusa iz prihvaćene arhitekture: provjeru,
pripremu, modeliranje, vrednovanje i komunikaciju. Razvija nit proračuna
nesigurnosti i nit posljedica pogreške, razvija selekciju i odsutnost kroz
selekciju objavljivanja te reproducibilnost i podrijetlo kroz cijeli put podataka.
Na granici dijela nosi punu mapu tvrdnji sa šest dimenzija i šest revizijskih
pitanja, odgovorivu samoprovjeru, zadatak dohvata unatrag i ugovor o reformiranoj
praksi kojim poglavlje 13 počinje raditi.

Ljestvica AI kompetencija u Dijelu IV traži reviziju nulte hipoteze,
višestrukosti, analitičke fleksibilnosti, dokazne asimetrije, reproducibilnosti i
jedne obranjive alternative, uz čitljivu potvrdu provjere. Vidljivi je kod potvrda
koja se čita, a nijedan ocijenjeni zadatak nigdje u dijelu ne traži pisanje koda.

## Nacrtana kralježnica po poglavljima

### Poglavlje 10 — Logika testiranja

**Nosivi aspekti**

1. Asimetrija sudnice: test može ne odbaciti, a to nije dokaz odsutnosti.
2. Svijet bez učinka izgrađen simulacijom prije nego što je nulta hipoteza
   imenovana.
3. Nulta hipoteza izrečena kao hipoteza pune raspodjele uz razmjenjivost i
   neovisne opažačke jedinice, uz korekciju za konačan broj premještanja.
4. Dvije vrste pogreške i njihove različite stvarne cijene; nit posljedica
   pogreške ovdje se razvija.
5. Prag je konvencija, a ne mjera; što p-vrijednost nije.
6. Epizoda Američkoga statističkog udruženja kao povijesni slučaj poglavlja: što
   je struka rekla, zašto je to rekla i što je time promijenila.
7. Drugo pitanje i drugi račun, da se postupak nikada ne pročita kao obred nad
   jednim oblikom podataka.
8. Procijenjena stopa pogreške nije nepogrešiva referentna istina; referentne
   oznake same mogu biti krive, čime se priprema poglavlje 17.
9. Omeđena Bayesovska usporedba koja knjigu drži estimacijskom, bez tečaja
   Bayesovske inferencije.

**Nosivi pojmovi**: nulta hipoteza, testna statistika, p-vrijednost, pogreška
prve vrste, pogreška druge vrste, prag značajnosti, permutacijski test,
referentna oznaka.

**Preduvjeti**: poglavlja 7, 8 i 9.

**Isključenja**: nikakav katalog testova ni tablica pragova; mehanika nikada ne
vodi; nikakva tvrdnja da neodbacivanje utvrđuje nultu hipotezu; nikakva uzročna
tvrdnja iz opažačkoga permutacijskog testa; nikakva puna Bayesovska inferencija;
veličina učinka i snaga pripadaju poglavlju 11, a argument o reformi poglavlju 12;
nijedan ocijenjeni zadatak pisanja koda; nijedan izmišljen ili neizvorni
empirijski primjer.

### Poglavlje 11 — Veličina učinka i snaga

**Nosivi aspekti**

1. Veličina vodi: razlika koja nešto znači izriče se u jedinicama pitanja prije
   nego što se spomene ijedan prag.
2. Značajno i važno dvije su različite prosudbe.
3. Standardizirana razlika i najmanji važan učinak kao dva načina da se kaže
   koliko je velik učinak.
4. Snaga kao svojstvo plana, a ne rezultata; planiranje unatrag od najmanjega
   važnog učinka.
5. Podsnažene studije pretjeruju u onome što preživi prag, uz rezultat omeđen na
   simulaciju koja ga proizvodi.
6. Niska snaga traži kalibriranu pozornost na nesigurnost, selekciju, prethodne
   dokaze i replikaciju, a ne paušalno nepovjerenje.
7. Imenovane pretpostavke demonstracije snage: neovisna normalna opažanja,
   zajednička poznata standardna devijacija i dvostrani z-postupak.
8. Jezik izvještavanja razvija se dalje: procjena, interval, veličina i ono što
   bi promijenilo zaključak.

**Nosivi pojmovi**: veličina učinka, standardizirana razlika, najmanji važan
učinak, statistička snaga, planiranje veličine uzorka, precjenjivanje učinka u
malim uzorcima, širina intervala.

**Preduvjeti**: poglavlja 9 i 10.

**Isključenja**: nikakav novi testni postupak; poglavlje tumači veličinu i planira
studije; rezultat o pretjerivanju ne smije se poopćiti izvan simulacije koja ga je
proizvela; niska snaga ne smije postati paušalna presuda o literaturi; nikakvo
odstupanje od kanonskoga sedmodijelnog poretka poglavlja, pa razrađeni primjer ne
smije prethoditi odjeljcima o statistici u divljini i o asistentu; metaanaliza i
sinteza dokaza pripadaju poglavlju 12; nijedan ocijenjeni zadatak pisanja koda;
nijedan izmišljen ili neizvorni empirijski primjer.

### Poglavlje 12 — Kriza i obnova

Kralježnica poglavlja 12 podređena je njegovu ratificiranom identitetskom brifu
`c12` i ne ponavlja ga. Brif određuje argument, njegovih šest obveznih sastavnica
i dokazni artefakt; kralježnica određuje što poglavlje mora nositi kao pojam,
preduvjet i granicu.

**Nosivi aspekti**

1. Jedan provjeren istraživački artefakt nosi cijeli životni ciklus; poglavlje je
   jedan argument, a ne popis reformi.
2. Analitička fleksibilnost kao svojstvo cijeloga puta podataka — prikupljanja,
   isključenja, spajanja, rekodiranja i pravila o nedostajućim vrijednostima —
   dohvaćena iz Dijela II, a ne uvedena kao nova tema.
3. Selekcija objavljivanja: što se objavljuje, a što ostaje neobjavljeno; nit
   selekcije i odsutnosti ovdje se razvija.
4. Replikacija kao kumulativni dokaz, s kontekstom, dizajnom i mjernom
   nesigurnošću.
5. Jedna usporedba osjetljivosti: primarna analiza i jedna obranjiva alternativa,
   uspoređene po procjenama, intervalima, sadržajnim zaključcima i predstavljenim
   populacijama.
6. Jedan forest plot koji se čita, a ne računa: procjene i intervali studija,
   objedinjena procjena, vidljiva heterogenost i granice koje nameću selekcija i
   kontekst.
7. Reproducibilnost i podrijetlo kao žetva: dokazna se vrijednost nalaza čita kroz
   put kojim je nastao, a ne kroz jedan broj.
8. Reforma i njezine granice: predregistracija, otvoreni materijali i registrirani
   izvještaji mijenjaju postupak, a reproducibilnost ne čini nevaljanu inferenciju
   valjanom.
9. Asistent u dvostrukoj ulozi: proizvođač uvjerljivoga teksta i sredstvo provjere
   reproducibilnosti; vidljive potvrde koda otkrivaju analitičko grananje bez
   ijednoga zadatka pisanja koda.
10. Granica Dijela IV: puna mapa tvrdnji sa šest dimenzija i šest revizijskih
    pitanja, odgovoriva samoprovjera, zadatak dohvata unatrag i ugovor o
    reformiranoj praksi kojim poglavlje 13 počinje raditi.

**Nosivi pojmovi**: analitička fleksibilnost, reproducibilnost, p-hakiranje, vrt
račvajućih putova, publikacijska pristranost, predregistracija, registrirani
izvještaj, replikacija, forest plot, osjetljivost.

**Preduvjeti**: poglavlja 4, 5, 9, 10 i 11.

**Isključenja**: nikakav popis reformi umjesto jednoga argumenta; kralježnica je
podređena brifu `c12` i ne ponavlja njegov argument; nikakav novi statistički
postupak, jer se objedinjena procjena i forest plot čitaju, a ne računaju; nikakav
tečaj sinteze dokaza ni metaanalitičke metode; nijedan izmišljen rezultat studije,
veličina učinka ni ulaz u forest plot; nijedna nedatirana ili neizvorna tvrdnja o
otvorenoj znanosti; nikakva tvrdnja da reproducibilnost popravlja nevaljanu
inferenciju; nijedan ocijenjeni zadatak pisanja koda; odabir dokaznoga artefakta i
obris ostaju gateovima `G-A4-12` i `P3-EVIDENCE12`.

## Hijerarhija definicija za Dio IV

Ovaj gate rješava stavku `R04-C12-definitions`. Poglavlje 12 trenutno nema nijedan
`#def-` blok, čime pada ispod ratificiranoga pojasa
`bands.definitions_per_chapter`, koji traži najmanje jedan. Odluka slijedi isto
pravilo kao Dio I: blok dobiva samo pojam o kojemu kasnije poglavlje stvarno
ovisi.

| Poglavlje | `#def-` blok | Proza pri prvoj upotrebi | Odgođeno |
|---|---|---|---|
| 10 | nulta hipoteza, testna statistika, p-vrijednost, pogreška prve vrste | pogreška druge vrste, prag značajnosti, permutacijski test, referentna oznaka | veličina učinka i snaga (poglavlje 11) |
| 11 | standardizirana razlika, statistička snaga, najmanji važan učinak | veličina učinka, planiranje veličine uzorka, širina intervala | metaanaliza i sinteza dokaza (poglavlje 12) |
| 12 | analitička fleksibilnost, reproducibilnost | p-hakiranje, vrt račvajućih putova, publikacijska pristranost, predregistracija, registrirani izvještaj, replikacija, forest plot, osjetljivost | — |

Poglavlja 10 i 11 zadržavaju svoja postojeća četiri i tri bloka nepromijenjena;
oba su unutar pojasa i nijedna stavka registra ne traži izmjenu.

Poglavlje 12 dobiva točno dva nova bloka, svaki s imenovanim kasnijim ovisnikom.
**Analitička fleksibilnost** nosi ono što poglavlje 16 traži kao redovnu obvezu
osjetljivosti i što poglavlje 18 dokumentira u dnevniku transformacija.
**Reproducibilnost** je pojam koji poglavlje 18 žanje kao cjelovit trag od izvora
do tvrdnje; nit ga sadi u poglavljima 4 i 5, razvija ovdje i žanje u završnici, pa
je prvi susret uredno prije formalizacije.

Ostali pojmovi poglavlja 12 ostaju u prozi uz mehanizam `.pojam`. Predregistracija,
registrirani izvještaj, publikacijska pristranost, p-hakiranje, vrt račvajućih
putova, replikacija, forest plot i osjetljivost pripadaju argumentu poglavlja, ali
nijedno kasnije poglavlje ne ovisi o njihovoj formalnoj definiciji. Davanje bloka
svakome od njih pretvorilo bi poglavlje u katalog reformi, što je upravo ono što
zabilježena namjera odbija, i probilo bi pojas.

Poglavlje 12 time prelazi s nula na dva bloka i ulazi u pojas. Neto učinak na
zamrznuti skup jest povećanje s 46 na 48 živih definicija, uz smanjenje od dva
bloka koje je već odobrio gate `G-A2b-II` za poglavlje 4.

Ovaj gate nijedan blok ne piše. Kartu provodi `WC-C12` nad stvarnom prozom i
`P2-TERMS` nad ledgerom i grafom pojmova, nakon što `G-A2c` utvrdi kanonske
hrvatske oblike.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Vode veličina učinka i posljedice pogreške | Ugovor dijela; aspekti 10.1, 10.4, 11.1 i 11.2 |
| Testiranje značajnosti poučava se s poviješću i zlouporabama, a ne kao postupak | Ugovor dijela; aspekti 10.2, 10.5 i 10.6; prvo isključenje poglavlja 10 |
| Poglavlje 12 ostaje jedan dokazima vođen argument o istraživačkom sustavu, a ne popis reformi | Aspekt 12.1 i prvo isključenje poglavlja 12 |
| Poredak s mehanikom testiranja na prvome mjestu izričito je odbijen | Ugovor dijela i prvo isključenje poglavlja 10 |
| Kralježnica poglavlja 12 podređena je ratificiranom brifu `c12` i ne ponavlja ga | Uvodna napomena poglavlja 12 i drugo isključenje |
| Riješiti `R04-C12-definitions` kroz tu identitetsku kralježnicu | Hijerarhija definicija; dva bloka, svaki s imenovanim kasnijim ovisnikom |

Ostali aspekti nisu novi zahtjevi. Svaki provodi već ratificiranu stavku registra,
prihvaćenu odluku ili ratificirani brif.

| Aspekt | Već ratificirani izvor |
|---|---|
| 10.3 nulta hipoteza i korekcija | prihvaćena odluka D01, prihvaćeni `R01-C10-null-exchangeability` i `R01-C10-monte-carlo-correction` |
| 10.6 epizoda ASA-e | `R31-C10-ASA-home` |
| 10.8 pogrešiva referentna oznaka | `R13-C10-label-fallibility` |
| 10.9 omeđena Bayesovska usporedba | prihvaćeni `R01-C10-bayesian-balance` |
| 11.5 pretjerivanje u podsnaženim studijama | `R17-C11-exaggeration` |
| 11.6 kalibrirana pozornost umjesto nepovjerenja | `R17-C11-low-power` |
| 11.7 pretpostavke demonstracije snage | prihvaćeni `R09-C11-power-assumptions` |
| isključenje o sedmodijelnom poretku | `R04-C11-fixed-order` |
| 12.1 do 12.9 | ratificirani identitetski brif `c12` u `identity_briefs` |
| 12.2 fleksibilnost cijeloga puta podataka | `R11-C12-pipeline-flexibility` |
| 12.4 replikacija kao kumulativni dokaz | `R19-C12-replication-cumulative` |
| 12.6 forest plot | `R19-C12-forest-plot` |
| 12.9 vidljive potvrde koda bez zadatka pisanja | `R23-C12-code-ladder`, `R23-C12-visible-receipt`, `R23-C12-no-R-production` |
| isključenje o nedatiranim tvrdnjama | `R24-C12-primary-sources` |
| 12.10 ugovor o reformiranoj praksi | `R27-C12-13-transition`, `R35-SELF-CHECK-IV` |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki.

## Razmotrene alternative

1. **Otvoriti Dio IV mehanikom testa i tek onda uvesti veličinu učinka.**
   Odbijeno: proturječi zabilježenoj namjeri i ratificiranom estimacijskom
   usmjerenju knjige.
2. **Premjestiti poglavlje 11 ispred poglavlja 10 da veličina doslovno vodi.**
   Odbijeno: proturječi odluci D03 o očuvanju makro-poretka; namjera traži da
   veličina i posljedice pogreške vode kao okvir čitanja, ne da se poglavlja
   preslože.
3. **Pretvoriti poglavlje 12 u pregled reformi s odjeljkom po reformi.**
   Odbijeno: proturječi zabilježenoj namjeri i ratificiranom brifu `c12`, koji
   izričito isključuje popis reformi umjesto jednoga argumenta.
4. **Ponoviti argument brifa `c12` unutar kralježnice poglavlja 12.** Odbijeno:
   kralježnica je podređena brifu; dva zapisa istoga argumenta stvorila bi dva
   izvora istine.
5. **Dati blok svakom reformskom pojmu poglavlja 12.** Odbijeno: probija
   ratificirani pojas i pretvara argument u katalog.
6. **Ne dodati poglavlju 12 nijedan blok.** Odbijeno: ostavlja poglavlje ispod
   ratificiranoga pojasa i ostavlja poglavlje 18 bez kanonskoga pojma za put koji
   mora dokumentirati.
7. **Definirati p-hakiranje kao formalni blok umjesto analitičke fleksibilnosti.**
   Odbijeno: p-hakiranje je jedna pojavnost šire fleksibilnosti, a poglavlja 16 i
   18 ovise o širem pojmu.
8. **Preseliti epizodu Američkoga statističkog udruženja iz poglavlja 10.**
   Odbijeno: proturječi `R31-C10-ASA-home` i ratificiranoj kralježnici poglavlja
   3, koja je izričito isključuje.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu Dijela IV i njezinu hijerarhiju
definicija. Ne odobrava prozu poglavlja 10, 11 ni 12 i ne mijenja nijednu datoteku
poglavlja. Ne dodaje, ne briše i ne spaja nijedan `#def-` blok i ne regenerira
graf pojmova; to ostaje paketima `WC-C10`, `WC-C11`, `WC-C12` i `P2-TERMS`. Ne
troši `H-P1C-INTEGRITY-002`, koji ostaje obveza paketa `P2-TERMS`. Ne mijenja i ne
zamjenjuje ratificirani identitetski brif `c12`. Ne utvrđuje kanonsku
terminologiju, koja ostaje gateu `G-A2c`. Ne ratificira nijednu kasniju
kralježnicu i ne pokreće `P2-SPINE-IV`. Ne bira dokazni artefakt, izvor, slučaj ni
podatkovni paket poglavlja 12, što ostaje gateovima `G-A4-12` i `P3-EVIDENCE12`.
Ne mijenja fazu nijedne jedinice, koja ostaje `draft`. Ne odobrava render,
generirani artefakt, push, merge, tag, arhiviranje, deployment ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavke `R04-SPINE-IV` i `R04-C12-definitions`;
- paket `P2-SPINE-IV`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json`.

Ovisnosti koje ostaju blokirane: `WC-C10`, `WC-C11` i `WC-C12` čekaju
`P3-VERIFY-C`, `WC-C12` uz to čeka `G-A4-12` i `P3-EVIDENCE12`, a sva tri čekaju
svoje gateove prihvaćanja `C10`, `C11` i `C12`; `P2-TERMS` čeka `G-A2c`;
`WC-PARTS` čeka svoja poglavlja.
