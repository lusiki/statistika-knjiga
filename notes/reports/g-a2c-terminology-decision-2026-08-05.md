# G-A2c — kanonsko nazivlje i put recenzije

**Gate:** `G-A2c`

**Datum odluke:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2c-terminology-and-reviewer-route-approved-2026-08-05-Luka-Sikic`,
vezano uz nacrt kanonskoga registra u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odlučuje dvije stvari i ništa više.

Prvo, **put recenzije nazivlja**: tko odgovara za kanonsku kartu pojmova i koju
tvrdnju o toj odgovornosti prvo izdanje smije iznijeti.

Drugo, **kanonske hrvatske oblike** za nosive pojmove knjige: koji je oblik
kanonski, koje se inačice bilježe kao prihvaćene ali neupotrijebljene, koja su
odstupanja od uobičajene hrvatske prakse namjerna i zašto, te gdje se živa proza
s tim oblicima još ne slaže.

Gate ne mijenja nijednu prozu, ne dodaje i ne uklanja nijedan `#def-` blok, ne
upisuje ništa u `concept-ledger.json`, `conventions.json`, `pojmovnik.qmd` ni
`dodaci/e-rjecnik.qmd`, ne regenerira `data/concept-graph.json` i ne pokreće
`P2-TERMS`. Provedbu nosi `P2-TERMS`, a prozu poglavljni paketi.

Gate također **ne ratificira nijednu kralježnicu i nijednu ne mijenja**. Svih je
devetnaest kralježnica već ratificirano na sedam `G-A2b` gateova. Njihovi su
ključni pojmovi time već fiksirani i ovaj ih gate potvrđuje kao kanonske, a ne
otvara ponovno.

## Ulazi pročitani prije odluke

- ratificirani plan, poglavlje 5, faza 2, točka 7 — popis nazivlja koje se mora
  kanonizirati: predviđanje, skupovi za učenje/provjeru/ispitivanje,
  preprilagodba, reziduali, izgledi, težine, tekstne jedinice i algoritamske
  oznake, uz zahtjev da se zabilježe prihvaćene inačice i namjerna odstupanja;
- register: `R04-TERMS-concept-regeneration`, `R36-BOOK-new-cluster`,
  `R36-BOOK-alternatives` i `R36-BOOK-domestic-review`, sva četiri u cijelosti;
- vanjski upit `OA-G-A2C-TERMS-EDITOR` u cijelosti;
- **cijeli ledger prosljeđivanja**. Nijedna isporuka ne cilja `G-A2c`. To se
  ovdje bilježi izričito: nije bilo dolazne obveze koju bi trebalo potvrditi ni
  potrošiti. Šest isporuka koje ciljaju `P2-TERMS` — `H-P1C-INTEGRITY-002`,
  `H-P2-SPINE-I-001`, `H-P2-SPINE-II-001`, `H-P2-SPINE-IV-001`,
  `H-P2-SPINE-V-001` i `H-P2-SPINE-FINALE-001` — pročitane su jer imenuju upravo
  ono što ovaj gate mora fiksirati, ali nijedna nije potrošena ovdje;
- ratificirani registar kralježnica `chapter-spine.json`, svih 19 jedinica;
- živi izvor: 46 `#def-` blokova u `chapters/`, `concept-ledger.json` sa 46
  pojmova i 40 zapisa notacije, `scripts/integrity-debt.json`,
  `dodaci/e-rjecnik.qmd` i `STYLE.md` H9 i S2;
- obje autorove izmjene od 5. kolovoza 2026.:
  `notes/reports/g-a2c-reviewer-amendment-2026-08-05.md` i
  `notes/reports/g-a3-data-rights-determination-2026-08-05.md`.

## Put recenzije nazivlja

Autorova izmjena od 5. kolovoza 2026. ovdje je obvezujuća i ovaj je gate mjesto
na kojem se ona zaključuje.

Neovisni recenzent nazivlja povučen je iz prvoga izdanja. Nitko izvana neće
prolaziti kartu nazivlja. `OA-P6-TERMS-REVIEWER-RECRUIT` i `OA-P6-TERMS-SIGNOFF`
su `withdrawn_with_reason`, a `R36-BOOK-domestic-review` je
`rejected_with_reason`.

Odluka ovoga gatea glasi: **recenzija nazivlja jest i ostaje autorova vlastita
urednička odgovornost.** Luka Sikić jedini je imenovani nositelj nazivlja knjige.
Kanonska karta nije ukinuta niti oslabljena; mijenja se samo tko za nju odgovara.

Iz toga slijedi granica koju ovaj gate izriče i prosljeđuje: **prvo izdanje ne
smije nigdje tvrditi da je nazivlje prošlo neovisnu recenziju** — ni u knjizi, ni
u predgovoru, ni u kolofonu, ni u metapodacima izdanja, ni u opisu na mrežnim
stranicama. Ta granica veže `P2-TERMS`, `P2-DOCS`, `P6-METHODS`, `P6-VERIFY`,
`P8-META` i svaki paket koji piše opis izdanja.

Ovaj gate sam ne iznosi nikakvu tvrdnju o neovisnoj recenziji.

## Načela kanonskoga nazivlja

Pet načela vrijedi za cijeli registar.

1. **Jedan pojam, jedno kanonsko hrvatsko ime kroz cijelu knjigu.** To je već
   pravilo `STYLE.md` S2 i H9; ovaj gate ga primjenjuje na nosive pojmove.
2. **Engleski se zadržava, ali samo na dva mjesta**: u bloku `{.pojmovi}` na
   kraju poglavlja i u Dodatku E. U prozi engleski original stoji najviše jednom,
   pri prvom spomenu, i samo kada literatura doista živi pod engleskim imenom.
3. **Prihvaćena inačica nije sinonim u prozi.** Inačica se bilježi u registru kao
   uputnica da čitatelj prepozna oblik iz druge literature. Proza je ne
   upotrebljava.
4. **Namjerno odstupanje mora imati zapisan razlog.** Ako knjiga bira oblik koji
   nije najčešći, razlog se bilježi uz pojam, a ne prepušta čitatelju.
5. **Preimenovanje pojma ne preimenuje njegov identifikator.** `#def-` ID je
   stabilno sidro: nosi ga `data/concept-graph.json` kao ID čvora i
   `pojmovnik.qmd` kao poveznicu `#def-${n.id}`. Promjena kanonskoga naziva mijenja
   podebljani pojam i zapis u registru, nikada ID.

## Kanonski registar: što je već fiksirano ratifikacijom

Devetnaest ratificiranih kralježnica nosi ukupno **168 mjesta ključnih pojmova**,
odnosno **166 različitih pojmova**. Dva se pojma pojavljuju u dvije jedinice i to
je namjerno: `procjena` u predgovoru i u poglavlju 9, te `standardizirana
razlika` u poglavljima 11 i 14. Riječ je o istom pojmu koji dvije jedinice nose,
a ne o dvama značenjima, pa nije riječ o sudaru.

Tih je 166 oblika ratificirano na `G-A2b-PREFACE`, `G-A2b-I`, `G-A2b-II`,
`G-A2b-III`, `G-A2b-IV`, `G-A2b-V` i `G-A2b-FINALE`. **Ovaj ih gate potvrđuje
kao kanonske i nijedan ne mijenja.** Gate koji odlučuje o nazivlju nema ovlast
oslabiti ratificiranu kralježnicu.

Iz toga slijedi i rješenje za pojmove koje su kralježnice imenovale kao nosive, a
nisu ih kanonizirale: ondje gdje kralježnica već nosi jedan oblik, taj je oblik
kanonski. Gate ne izmišlja treći oblik.

## Pojmovi koje ovaj gate fiksira

Sljedeći su pojmovi imenovani u ledgeru prosljeđivanja kao nosivi, a njihov je
kanonski hrvatski oblik izričito ostavljen ovome gateu.

| Pojam | Kanonski hrvatski oblik | Engleski | Izvor obveze |
|---|---|---|---|
| razdvajanje skupova | `razdvajanje na skup za učenje, provjeru i ispitivanje` | *training/validation/test split* | `H-P2-SPINE-V-001` |
| sastavnice razdvajanja | `skup za učenje`, `skup za provjeru`, `skup za ispitivanje` | *training set*, *validation set*, *test set* | `H-P2-SPINE-V-001` |
| procjenjivana veličina | `procjenjivana veličina` | *estimand* | `H-P2-SPINE-V-001` |
| curenje | `curenje informacija` | *leakage* | `H-P2-SPINE-V-001` |
| zabilježeni referentni ishod | `zabilježeni referentni ishod` | *recorded reference outcome* | `H-P2-SPINE-V-001` |
| klasifikacijski prag | `klasifikacijski prag` | *classification threshold* | `H-P2-SPINE-V-001` |
| paket dokaza | `paket dokaza` | *evidence package* | `H-P2-SPINE-FINALE-001` |
| putovnica skupa podataka | `putovnica skupa podataka` | *dataset passport* | `H-P2-SPINE-FINALE-001` |
| objava uporabe asistenta | `objava uporabe asistenta` | *AI-use disclosure* | `H-P2-SPINE-FINALE-001` |
| analitička fleksibilnost | `analitička fleksibilnost` | *analytic flexibility* | `H-P2-SPINE-IV-001` |
| reproducibilnost | `reproducibilnost` | *reproducibility* | `H-P2-SPINE-IV-001` |
| jedinica analize | `jedinica analize` | *unit of analysis* | `H-P2-SPINE-I-001` |
| Simpsonov paradoks | `Simpsonov paradoks` | *Simpson's paradox* | `H-P2-SPINE-I-001` |
| temeljna stopa | `temeljna stopa` | *base rate* | `H-P2-SPINE-I-001` |
| varijanca uz standardnu devijaciju | `varijanca` i `standardna devijacija`, oba kanonska, oba imenovana u jednoj definicijskoj rečenici | *variance*, *standard deviation* | `H-P2-SPINE-II-001` |

Sedam od tih petnaest redaka samo potvrđuje oblik koji ratificirana kralježnica
već nosi. To nije prazan hod: dok gate ne izrekne da je taj oblik kanonski,
`P2-TERMS` ne smije upisati pojam u kanonski registar, a `R04-C17-definitions`
ostaje otvoren. Upravo je zato `P2-SPINE-V` tu stavku namjerno ostavio otvorenom.

### Novi pojmovni sklop iz `R36-BOOK-new-cluster`

Stavka imenuje sklop: četiri djelatnosti, razdvajanje skupova, izgledi, uzročni
pojmovi, osjetljivost, kalibracija i pomak. Kanonski oblici:

| Sklop | Kanonski oblici | Engleski |
|---|---|---|
| četiri djelatnosti | `statistika`, `podatkovna znanost`, `strojno učenje`, `sustav umjetne inteligencije` | *statistics*, *data science*, *machine learning*, *AI system* |
| razdvajanje skupova | kako je gore | — |
| izgledi | `izgledi`, `omjer izgleda`, `predviđena vjerojatnost` | *odds*, *odds ratio*, *predicted probability* |
| uzročni pojmovi | `konfundirajuća varijabla`, `medijator`, `kolider`, `prilagođena povezanost` | *confounder*, *mediator*, *collider*, *adjusted association* |
| osjetljivost | `osjetljivost`, `provjera osjetljivosti` | *sensitivity (of a conclusion)*, *sensitivity check* |
| kalibracija | `kalibrirana nesigurnost`, `kalibracija stope pogreške prve vrste` | *calibrated uncertainty*, *type-I error calibration* |
| pomak | `pomak distribucije` | *distribution shift* |

`omjer izgleda` i `predviđena vjerojatnost` jedini su oblici u ovoj tablici koje
nijedna kralježnica ne imenuje. Ulaze jer ratificirani plan za poglavlje 16
predviđa omeđen most prema binarnim ishodima, omjerima izgleda i predviđenim
vjerojatnostima, pa bi bez fiksiranoga oblika taj most uveo nazivlje mimo
registra. Fiksira se oblik, ne i odluka hoće li se pojaviti; to ostaje
`WD-C16`.

## Sudari značenja koje gate razrješava

Četiri riječi u knjizi nose više od jednoga značenja. Registar bi ih tiho spojio,
pa gate izriče pravilo za svaku.

**`osjetljivost`.** Rezervira se za otpornost zaključka na obranjivu drukčiju
odluku u analizi — poglavlje 12 je uvodi, poglavlja 16 i 18 je razvijaju i žanju.
Stopa točno prepoznatih pozitivnih slučajeva iz tablice zabune **nikada se ne
zove osjetljivošću**; imenuje se svojim nazivnikom. Razlog je dvostruk: knjiga bi
inače jednom riječju zvala dvije nepovezane veličine, a `c17` brif izričito
zabranjuje svođenje pravednosti na jedno mjerilo, čemu bi kratko ime za jednu
stopu upravo pogodovalo.

**`kalibracija`.** Ne postoji kao samostalan kanonski pojam. Uvijek se piše sa
svojim predmetom: `kalibrirana nesigurnost` u poglavlju 7 i `kalibracija stope
pogreške prve vrste` u poglavlju 13. Živa proza poglavlja 13 već tako postupa —
`kalibraciju postupka`, `kalibraciji pogreške prve vrste`, `kalibracija pod
nulom` — pa pravilo potvrđuje postojeću praksu umjesto da je mijenja.

**`predviđanje` i `predikcija`.** Kanonska je hrvatska imenica `predviđanje`, i za
čin i za njegov rezultat. `predikcija` ostaje dopuštena **samo unutar
ratificirane sintagme `sustav predikcije`**, gdje imenuje vrstu sustava, a ne
pojedinačan ishod. Time ostaje netaknut ratificirani pojam poglavlja 17 `jezični
model kao sustav predikcije`, a poglavlje 16 zadržava `predviđanje izvan uzorka`.
`predikcijski model` nije kanonski oblik; kanonski je `model za predviđanje`.

**`referentna oznaka` i `zabilježeni referentni ishod`.** Poglavlje 10 sadi
`referentnu oznaku` kao pogrešivu oznaku prema kojoj se mjeri stopa pogreške.
Poglavlje 17 žanje `zabilježeni referentni ishod` kao objekt prema kojem se
klasifikator vrednuje. To su dva koraka istoga luka, a ne dva imena za isto, pa
oba ostaju. **Nijedan se od njih nigdje ne piše kao `istina` ni kao *ground
truth*.** To je izravna obveza stavke `R24-C17-recorded-reference`.

## Namjerna odstupanja

Tri oblika odstupaju od uobičajenoga i razlog se bilježi ovdje.

**`tablica zabune`, a ne matrica.** Engleski se par zadržava kao *confusion
matrix*, kako živi blok `{.pojmovi}` poglavlja 17 već piše. Hrvatski je naziv
tablica jer je isti objekt u poglavlju 13 ratificiran kao kontingencijska tablica
s uvjetnim nazivnicima. Dva bi imena za jedan objekt stvorila dva izvora istine i
oslabila upravo onaj preduvjet koji `G-A2b-V` ratificira, a to je razlog kojim je
`H-P2-SPINE-V-001` već odbio zaseban definicijski blok za tablicu zabune.

**`kolider`.** Zadržava se prijenos engleskoga naziva jer ga tako nosi
ratificirana kralježnica poglavlja 2, uz `medijator` i `konfundirajuću
varijablu`, i jer knjiga tu trojku uvodi kao jedan rječnik dijagrama.

**`izgledi`, a ne šanse.** Hrvatski oblik bira se zato što knjiga uz njega gradi
`omjer izgleda`, a par *odds/odds ratio* mora ostati prepoznatljiv u obama
smjerovima.

## Razilaženja žive proze i kanonskoga oblika

Ovo je popis mjesta na kojima živi izvor još ne nosi kanonski oblik. Gate ih
imenuje točno i dodjeljuje ih paketu koji smije mijenjati prozu. **Gate ne mijenja
nijedno od njih.**

| Mjesto | Živi oblik | Kanonski oblik | Nositelj |
|---|---|---|---|
| `chapters/17-doba-algoritama.qmd:50-51` | skup za treniranje, skup za testiranje | `skup za učenje`, `skup za provjeru`, `skup za ispitivanje` | `WD-C17` |
| `chapters/17-doba-algoritama.qmd:463` | skup za treniranje (*training set*), skup za testiranje (*test set*) | isto | `WD-C17` |
| `chapters/17-doba-algoritama.qmd:48, 56, 57, 104` | Predikcija, Predikcijski model | `predviđanje`, `model za predviđanje` | `WD-C17` |
| `chapters/16-regresija.qmd:1082, 1088` | predikciju | `predviđanje` | `WD-C16` |
| `chapters/00-predgovor.qmd:34, 84` | predikcije, Predikcija | `predviđanje` | `WA-C00` |
| `chapters/16-regresija.qmd:956` | curenje cilja | `curenje informacija` | `WD-C16` |
| `chapters/16-regresija.qmd:129, 1008, 1239` | curenje, curenje podataka iz budućnosti, curenje iz budućnosti | `curenje informacija`, uz vremensku granicu opisanu u rečenici | `WD-C16` |
| `chapters/08-uzorkovanje.qmd:875, 1075` | težina uzorka | `težina uzorkovanja` | `WC-C08` |
| `chapters/08-uzorkovanje.qmd:876, 877, 1058` | Neponderirana, ponderiranje, ponderirane | `procjena bez težina`, `procjena s težinama` | `WC-C08` |
| `bookwright_plugin/bookwright/shared/concept-ledger.json` | `standardizirani rezidual` uz zastarjelu definiciju s korijenom očekivane frekvencije | `prilagođeni standardizirani rezidual`, uz definiciju koja uzima rubne udjele | `P2-TERMS` |

Zadnji redak nije stilsko razilaženje nego zaostatak ispravka. Poglavlje 13 već
nosi ispravljeni blok, a registar još nosi Pearsonov oblik koji je taj ispravak
uklonio. To je jedini od dva zapisa koje deterministički provjeritelj broji kao
`ledger_debt=2` i `P2-TERMS` ga mora pomiriti.

**`curenje podataka` u `chapters/02-mjerenje-i-dizajn.qmd:380` nije na ovom
popisu i namjerno ostaje.** Ondje riječ opisuje stvarni ispad podataka kao
događaj u svijetu, koji kvazieksperiment koristi kao razliku koju nije proizveo
nacrt istraživanja. To nije statističko curenje informacija i pravilo ga ne
dodiruje.

## Stabilni identifikatori koji se ne mijenjaju

Tri `#def-` ID-a ne slijede svoj pojam i to je odluka, ne propust.

| ID | Podebljani pojam | Zašto ID ostaje |
|---|---|---|
| `#def-standardizirani-rezidual` | Prilagođeni standardizirani rezidual | ID je sidro čvora u `concept-graph.json` i poveznice u `pojmovnik.qmd` |
| `#def-korelacija` | Pearsonova korelacija | isto |
| `#def-mala-polja` | Mala višestruka polja | isto |

`P2-TERMS` upisuje kanonski pojam, a ID ostavlja nedirnut.

Uz `#def-korelacija` ide i jedna razina više: `korelacija` je kanonski opći
pojam i ključni pojam kralježnice poglavlja 6, a `Pearsonova korelacija` kanonsko
ime konkretne mjere definirane u bloku. Oba su kanonska jer isto poglavlje
ratificira i `Spearmanov koeficijent ranga`, pa se dvije mjere moraju razlikovati.
Ondje gdje se misli na mjeru, knjiga piše `Pearsonova korelacija`.

## Karta definicija: 46 prema 52

Šest ratificiranih karata definicija zajedno vodi zamrznuti skup od 46 živih
`#def-` blokova na 52.

| Gate | Promjena | Zbroj |
|---|---|---|
| polazno stanje | 46 živih blokova | 46 |
| `G-A2b-I` | +3: `jedinica analize`, `Simpsonov paradoks` u poglavlju 1, `temeljna stopa` u poglavlju 3 | 49 |
| `G-A2b-II` | −2: `varijanca` se spaja u blok standardne devijacije, `asimetrija` se spušta u prozu | 47 |
| `G-A2b-III` | +0 | 47 |
| `G-A2b-IV` | +2: `analitička fleksibilnost`, `reproducibilnost` u poglavlju 12 | 49 |
| `G-A2b-V` | +2: `zabilježeni referentni ishod`, `klasifikacijski prag` u poglavlju 17 | 51 |
| `G-A2b-FINALE` | +1: `paket dokaza` u poglavlju 18 | 52 |

Gate potvrđuje taj zbroj i ne mijenja nijednu od šest karata. Živi je broj i
dalje 46: nijedan blok nije napisan i ovaj gate nijedan ne piše.

Neovisna provjera protiv živoga izvora slaže se s kartama. Tri od 46 podebljanih
pojmova nisu ključni pojmovi vlastite ratificirane kralježnice, i to su točno
`varijanca` i `asimetrija` u poglavlju 4, koje karta `G-A2b-II` uklanja kao
zasebne blokove, te `Pearsonova korelacija` u poglavlju 6, koja je razina niže od
ključnoga pojma `korelacija`. Nijedno drugo razilaženje ne postoji.

## Što ovaj gate ne odlučuje

- Ne piše nijedan `#def-` blok i ne mijenja živi broj od 46.
- Ne zatvara `R04-C17-definitions`. Ta je stavka `P2-TERMS`-ova, koji je smije
  zatvoriti tek kad su kanonski oblici fiksirani, uz izričit zapis da je
  recenziju obavio autor sam.
- Ne dodiruje `R04-C18-whole-prerequisites`, koji pripada `WE-C18` i `P5-ROUTES`.
- Ne objavljuje i ne mijenja nijedan put kroz knjigu.
- Ne bira i ne promiče nijedan skup podataka i ne tvrdi nikakvo dopuštenje
  nositelja prava.
- Ne mijenja `STYLE.md`, `DESIGN.md`, `AGENTS.md` ni `notes/struktura-knjige.md`.
  Usklađivanje upravljačkih dokumenata je `P2-DOCS`.

## Razmotrene alternative

Osam je alternativa razmotreno i odbijeno.

1. **Zadržati neovisnu recenziju nazivlja u prvom izdanju.** Odbijeno: autor ju
   je povukao 5. kolovoza 2026. i nijedan recenzent nije imenovan. Zadržavanje bi
   značilo tvrdnju koja nije istinita.
2. **Povući recenzenta i tiho zadržati opis „recenzirano nazivlje" u opisu
   izdanja.** Odbijeno kao netočna tvrdnja. Zato granica zabrane ide izričito na
   knjigu, predgovor, kolofon, metapodatke i mrežni opis.
3. **Ponovno otvoriti ključne pojmove ratificiranih kralježnica i složiti registar
   od nule.** Odbijeno: gate o nazivlju nema ovlast oslabiti ratificiranu
   kralježnicu, a sedam bi `G-A2b` odluka time postalo privremeno.
4. **Zadržati dvodijelno razdvajanje `skup za treniranje` i `skup za testiranje`
   jer ga proza već nosi.** Odbijeno: ratificirana kralježnica poglavlja 17 nosi
   trodijelno razdvajanje kao nosivi pojam, pa bi ovaj izbor mijenjao kralježnicu
   prema prozi umjesto obrnuto.
5. **Proglasiti `predikciju` kanonskom imenicom jer je kraća.** Odbijeno:
   `predviđanje` je oblik koji nose obje ratificirane kralježnice koje pojam
   trebaju, a sintagma `sustav predikcije` ostaje netaknuta kao ime vrste sustava.
6. **Dopustiti `osjetljivost` i za stopu iz tablice zabune.** Odbijeno: dvije
   nepovezane veličine pod jednim imenom, uz izravan sukob sa zabranom svođenja
   pravednosti na jedno mjerilo iz brifa `c17`.
7. **Uskladiti `#def-` ID-e s preimenovanim pojmovima.** Odbijeno: ID je sidro
   čvora u generiranom grafu i poveznice u pojmovniku, pa bi preimenovanje
   prekinulo obje veze bez ijedne dobiti.
8. **Odgoditi kanonske oblike do `P2-TERMS` i pustiti da ih provedbeni paket
   odabere usput.** Odbijeno: tada bi registar odlučivao o nazivlju, a
   `R04-C17-definitions` ne bi imao osnovu za zatvaranje jer njegov test traži
   pregledanu kartu, a ne usput odabrane oblike.

## Obvezujuće autorove izmjene od 5. kolovoza 2026.

Obje su pročitane prije odluke i obje vrijede.

**Nazivlje.** Prvo izdanje ne iznosi nikakvu tvrdnju o neovisnoj recenziji
nazivlja. Ovaj gate takvu tvrdnju ne iznosi i izričito je zabranjuje paketima
koje imenuje.

**Prava na podatke.** Knjiga ne smije tvrditi da je pribavila dopuštenje
nositelja prava jer ono nije traženo. Ovaj gate ne bira nijedan izvor podataka i
ne iznosi nikakvu tvrdnju o pravima. `H-P1B-DATA-LIC-003` nije nadomješten i
ostaje obveza `G-A3` gateova.

## Granica autoriteta

Ova odluka ovlašćuje `P2-TERMS` da provede kanonski registar, pomiri žive
definicije i kanonski ledger, regenerira `data/concept-graph.json` i povuče dug
pojmovnoga gatea. Ne ovlašćuje ništa drugo.

Ne odobrava izmjenu proze ni u jednom poglavlju ili dodatku, ne ratificira i ne
mijenja nijednu kralježnicu, ne otvara nijedan `G-A3` ili `G-A4` gate, ne mijenja
ugovor ocjenjivanja, ne odobrava render, generirani artefakt, push, merge, tag,
arhiviranje, deployment ni objavu.

Ako se pri provedbi pokaže da neki kanonski oblik razbija ratificiranu
kralježnicu, `P2-TERMS` staje i vraća pitanje ovome gateu umjesto da oblik
prilagodi sam.

## Blokirane ovisnosti koje se ovime otključavaju

| Stavka | Paket | Stanje nakon ovoga gatea |
|---|---|---|
| `R04-TERMS-concept-regeneration` | `P2-TERMS` | odblokirana |
| `R36-BOOK-new-cluster` | `P2-TERMS` | odblokirana |
| `R04-C17-definitions` | `P2-TERMS` | odblokirana za zatvaranje |
| `R36-BOOK-alternatives` | `P5-E` | oblici fiksirani; provedba ostaje u fazi 5 |
| `R36-BOOK-domestic-review` | `P2-TERMS` | već `rejected_with_reason` i `accepted`; ovaj gate ga ne dira |

`OA-G-A2C-TERMS-EDITOR` prelazi u `done`, bez ijedne poslane vanjske poruke.
