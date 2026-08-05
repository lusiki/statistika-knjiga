# G-A2b-FINALE — ratificirana kralježnica završnice

**Gate:** `G-A2b-FINALE`

**Datum odluke:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano, uz izmjenu preporučene
zadane odluke o novoj metodi.

**Izvorno stanje odluke:**
`conversation:G-A2b-FINALE-spine-approved-2026-08-05-Luka-Sikic`, vezano uz
nacrt kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu završnice: nosive aspekte,
nosive pojmove, preduvjete i isključenja poglavlja 18, ugovor završnice te
hijerarhiju definicija kojom se rješava stavka `R04-C18-definitions`. Uz to
utvrđuje da je poglavlje 18 kumulativno na razini cijele knjige, čime se rješava
stavka `R04-C18-whole-prerequisites`, i izriče **izmijenjenu granicu nove
metode** u završnici.

Gate ne odobrava prozu, ne dodaje i ne uklanja nijedan `#def-` blok, ne upisuje
ništa u `chapter-spine.json` i ne ratificira nijednu kralježnicu sam.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

Ovo je **jedini** od sedam kralježničnih gateova na kojemu zabilježena namjera
mijenja preporučenu zadanu odluku iz registra. Razlika je zapisana u odjeljku
„Izmjena zabrane nove metode" i u dispoziciji `accepted_as_amended`.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-FINALE-SPINE`, upravljane stavke `R04-SPINE-FINALE`,
`R04-C18-definitions` i `R04-C18-whole-prerequisites`, sve stavke registra koje
ciljaju poglavlje 18 (`R08-SPINE-18`, `R09-C18-interval-conclusion`,
`R10-C18-whole-book-harvest`, `R11-C18-table-audit`,
`R11-SCOPE-no-multiple-imputation`, `R13-C18-corpus-package`, `R15-CLOSURE-18`,
`R17-C18-two-pass`, `R19-C18-substantive-sensitivity`, `R24-C18-privacy-sources`,
`R24-C18-algorithm-harvest`, `R24-C18-explanatory-scope`, `R24-C18-dated-policy`,
`R24-C18-workflow`, `R27-C17-18-transition`, `R32-C18-transfer-path`,
`R35-REACHBACK-18`), prihvaćene arhitekture `G-A2a` i `G-A2d` (registar tvrdnji,
životni ciklus s ulogom `finale`, sedam niti s njihovim mjestima žetve,
ljestvica AI kompetencija s razinom `finale`, ugovor vidljivosti rješenja i
granica H10), ratificirane kralježnice predgovora te Dijelova I, II, III, IV i V,
prihvaćene odluke D03, D05, D06, D13, D15 i D16, prihvaćeni ispravak paketa
`P1A-C18`, pojasevi `bands` u `conventions.json`, cjeloviti izvor
`chapters/18-vase-prvo-istrazivanje.qmd` i zabilježena autorova namjera.

Pročitane su i dvije obvezujuće autorove izmjene od 5. kolovoza 2026.:
`notes/reports/g-a2c-reviewer-amendment-2026-08-05.md` i
`notes/reports/g-a3-data-rights-determination-2026-08-05.md`.

Cjeloviti ledger prijenosa pročitan je prije prve sadržajne izmjene. **Nijedan
prijenos ne cilja `G-A2b-FINALE`**, pa nema dolazne isporuke koju bi ovaj gate
priznao ili potrošio. `H-G-A2D-005` cilja `WE-C18` na vratu `before_start`,
ostaje `pending` i nosi datiranu politiku privatnosti koju ova kralježnica
upisuje kao obvezu, ali je ne troši. `H-P1C-INTEGRITY-002` cilja `P2-TERMS`,
ostaje `pending` i zamrzava skup od 46 živih definicija, pa ovaj gate odlučuje
samo kartu definicija. `H-P2-SPINE-V-001` cilja `P2-TERMS` i `WD-C17`, a
`H-P2-SPINE-V-002` cilja `P5-ROUTES`; nijedan se ovdje ne troši.

## Ugovor završnice

Završnica nosi jedan luk i ništa više: **od cijele knjige do jednoga paketa
dokaza koji netko drugi može provjeriti bez razgovora s autorom.** Poglavlje 18
ne uvodi gradivo nego ga sastavlja, i to je jedino mjesto na kojemu čitatelj
sam prolazi cijeli životni ciklus, od pitanja do nadzora.

**Poglavlje 18 kumulativno je na razini cijele knjige.** Njegov preduvjet nije
nekoliko poglavlja nego svih sedamnaest. To je zapisano i kao popis preduvjeta i
kao prvo isključenje, pa nijedan metapodatak, nijedna proza, nijedan zadatak i
nijedan oglašeni put ne smije završnicu prikazati kao samostalnu jedinicu.

Prema odluci D13 glavna studija ostaje **objasnidbena i simulirana**. Zato
poglavlje na kraju smije reći je li oprezan zaključak bio ispravan, ali mora
reći i da to znanje dolazi izvana, a ne iz analize. Uz nju stoji **jedan omeđen
empirijski prijenos** koji isti redoslijed pitanja, dizajna i granice tvrdnje
provodi nad stvarnim podacima i predaje cjelovit paket dokaza. Ta dvopotezna
građa je ratificirana stavkama `R08-SPINE-18` i `R17-C18-two-pass` i ovaj je
gate ne mijenja.

Završnica žanje sve četiri faze koje su ranije bile podijeljene po dijelovima i
sve devet faza životnoga ciklusa iz prihvaćene arhitekture. Od sedam niti ovdje
se žanju sve: jedinica analize, selekcija i odsutnost, nazivnik, proračun
nesigurnosti i posljedice pogreške dolaze iz poglavlja 17 i ranije, nit
reproducibilnosti i podrijetla ima ovdje svoju jedinu žetvu, a **sedma nit,
komunikacija tvrdnje, ovdje se žanje i nigdje drugdje**: čitatelj mora sam
napisati pošten izvještaj, a zatim istim mjerilom revidirati asistentov
izvještaj o istoj analizi.

Ljestvica AI kompetencija dolazi na svoju posljednju razinu. Svih pet dimenzija
— specifikacija zadatka, provjera, alternative, podrijetlo i odgovornost —
ovdje se žanje odjednom, u jednom protokolu koji se zapisuje po koracima:
specificiraj, delegiraj, reproduciraj, ospori, dokumentiraj, objavi. Asistent
nastupa u sve tri uloge, a odgovornost ostaje na osobi koja predaje rad.

Statistika ostaje estimacijska i u završnici. Procjena, interval i sadržajna
veličina vode zaključak; prag značajnosti ne odlučuje ni glavni nalaz ni
usporedbu s alternativom. Poglavlje nema widget i cijelo mu je tijelo jedno
prošireno vođeno istraživanje, kako je već ratificirano u `widget_policy`.

## Nacrtana kralježnica poglavlja 18

### Poglavlje 18 — Vaše prvo istraživanje

**Nosivi aspekti**

1. Završnica ne uvodi gradivo nego ga sastavlja: poglavlje je kumulativno na
   razini cijele knjige, traži svih sedamnaest ranijih poglavlja i nijedno od
   njih ne ponavlja kao mini-predavanje.
2. Pitanje i vrsta tvrdnje dolaze prije podataka: opis, povezanost,
   generalizacija, predviđanje, uzročnost i odluka razlikuju se prije nego što
   se ishod vidi, a dizajn postavlja granicu koju nijedna kasnija analiza ne
   može pomaknuti.
3. Analitička tablica vidljivo se konstruira: jedinica, prihvatljivost,
   spajanja, prekodiranja, transformacije, isključenja i nedostajuće vrijednosti
   nose zapisan razlog donesen prije nego što se vidjelo kako mijenjaju
   rezultat.
4. Opis i prikaz prethode modelu: nalaz o obliku raspodjele i o skupinama
   zapisuje se prije nego što je izračunata ijedna povezanost, pa graf pokazuje
   odakle povezanost dolazi prije nego što ju je model izmjerio.
5. Jedna procjena, njezin interval i njezina promjena pod prilagodbom;
   zaključak se piše iz onoga što interval podnosi, bez jezika o nestaloj
   povezanosti i bez zaključka o odsutnosti učinka iz prijelaza preko praga.
6. Sadržajna provjera osjetljivosti koja smije pomaknuti granicu zaključka:
   primarna analiza i jedna obranjiva alternativa uspoređuju se po procjeni,
   intervalu, sadržajnom zaključku i dosegnutoj populaciji.
7. Poznata istina i njezina granica: glavna je studija simulirana i tako
   označena prije prve brojke, pa se na kraju zna je li oprezan zaključak bio
   ispravan, ali se izriče i da to znanje dolazi izvana, a u stvarnom radu tu
   ulogu preuzimaju dizajn, teorija i ranija mjerenja.
8. Jedan omeđen empirijski prijenos s cjelovitim paketom dokaza: putovnica
   skupa podataka, izvor i verzija, dnevnik transformacija, analiza, provjera
   osjetljivosti, granica tvrdnje, zapis o uporabi asistenta i objava.
9. Sedma nit ovdje se žanje: čitatelj piše vlastiti pošten izvještaj po
   ratificiranom standardu — procjena, interval, jedinice, dosegnuta populacija
   i određeno ograničenje koje bi promijenilo zaključak — a zatim istim
   mjerilom revidira asistentov izvještaj o istoj analizi.
10. Cjelovit protokol rada s asistentom, zapisan po koracima: specificiraj,
    delegiraj, reproduciraj, ospori, dokumentiraj i objavi, uz čitljivu potvrdu
    provjere koja imenuje što je provjereno, kako, i što je ostalo neprovjereno.
11. Privatnost ispitanika kao datirana oprezna politika kolegija, objavljena u
    cijelosti u Dodatku F i ovdje primijenjena; politika, pravni opis i
    empirijski dokaz o ponovnoj identifikaciji ostaju tri razdvojene stvari.
12. Zatvaranje knjige: četiri obećanja, šest dimenzija tvrdnje sa šest
    revizijskih pitanja, sedam niti, devet faza životnoga ciklusa i razlika
    između statistike, znanosti o podacima, strojnoga učenja i postavljenoga
    sustava, uz izričito obrazloženje zašto objasnidbena glavna studija ne
    koristi svaki predikcijski alat poglavlja 17, te jedan zadatak dohvata
    unatrag najmanje dva poglavlja.

**Nosivi pojmovi**: paket dokaza, putovnica skupa podataka, trag odluka, dnevnik
transformacija, potvrđujuća analiza, istraživačka analiza, provjera
osjetljivosti, granica tvrdnje, reproducibilan tijek rada, pošten izvještaj,
objava uporabe asistenta, minimizacija podataka.

**Preduvjeti**: poglavlja 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
i 17.

**Isključenja**

1. Poglavlje se ne smije čitati bez cijele knjige, i nijedan metapodatak,
   nijedna proza, nijedan zadatak i nijedan oglašeni put ne smije završnicu
   prikazati kao samostalnu jedinicu.
2. Nijedna metoda s popisa izvan opsega iz predgovora ne smije ući u završnicu:
   vremenske serije, faktorska analiza i psihometrija, višerazinski modeli,
   matematika strojnoga učenja i puna Bayesovska inferencija ostaju izvan knjige
   i ondje gdje bi obrađeni slučaj s njima bio zanimljiviji.
3. Tehnika koju obrađeni slučaj doista traži dopuštena je samo pod dva uvjeta:
   u cijelosti je objašnjena ondje gdje se pojavljuje i samodostatna je, i ne
   traži nijedan pojam, postupak ni sposobnost koje nijedna ranija ratificirana
   kralježnica nije bila zadužena isporučiti.
4. Empirijski prijenos ne uvodi nijednu metodu; on ponavlja isti redoslijed
   pitanja, dizajna i granice tvrdnje nad stvarnim podacima.
5. Glavna studija ostaje objasnidbena i ne postaje predikcijska; ona ne koristi
   svaki alat poglavlja 17, a razlog se izriče kao odluka o opsegu tvrdnje, a ne
   prešućuje.
6. Nikakav središnji widget; cijelo je tijelo poglavlja jedno prošireno vođeno
   istraživanje.
7. Nijedan ocijenjeni zadatak pisanja koda; kod se čita, pokreće i provjerava, a
   ne piše kao ocijenjeni ishod.
8. Nikakva ocjenska ljestvica ni rubrika u samom poglavlju; glavni tekst ostaje
   bez odgovora, a rubrika, ključ i alternative pripadaju kanonskomu zapisu
   rješenja i njegovim zaštićenim projekcijama.
9. Nijedna nedatirana ni univerzalna pravna tvrdnja o privatnosti; politika
   kolegija navodi se kao datirana politika, a ne kao propis i ne kao pravni
   zaključak.
10. Nikakva višestruka imputacija ni napredno postupanje s nedostajućim
    vrijednostima; poglavlje izvještava koliko odgovora nedostaje i po kojem je
    pravilu postupljeno.
11. Nikakav novi obrazac koda: pet ranije uvedenih obrazaca završnica sastavlja,
    a tehnika dopuštena trećim isključenjem mora stati u postojeći obrazac
    poziva i ispisa.
12. Nijedan izmišljen ili neizvorni empirijski primjer; odabir podatkovnoga
    paketa za empirijski prijenos ostaje njegovim gateovima podataka i paketu
    `WE-C18`.

## Preduvjeti završnice: cijela knjiga

Ovaj gate rješava stavku `R04-C18-whole-prerequisites`. Poglavlje 18 traži svih
sedamnaest ranijih poglavlja, i svako nosi točno određenu obvezu:

| Preduvjet | Što završnica iz njega uzima |
|---|---|
| 1 — Zašto statistika | životni ciklus, jedinica analize i nazivnik |
| 2 — Mjerenje i dizajn | operacionalizacija, dizajn kao granica zaključka, osjetljive varijable |
| 3 — Kako brojke zavode | revizija tuđe tvrdnje i temeljna stopa |
| 4 — Sažimanje podataka | analitička tablica, nedostajuće vrijednosti i sjeme poštene rečenice |
| 5 — Vizualizacija | graf kao tvrdnja i zabrana skraćene osi bez napomene |
| 6 — Povezanost | povezanost i njezine granice, dijagram raspršenja kao primarni prikaz |
| 7 — Vjerojatnost | što slučaj proizvodi |
| 8 — Uzorkovanje | doseg generalizacije, pokrivenost i neodazivanje |
| 9 — Procjena | procjena, interval i jezik nesigurnosti |
| 10 — Logika testiranja | što test može i što ne može odgovoriti |
| 11 — Veličina učinka i snaga | planiranje preciznosti i sadržajna veličina |
| 12 — Kriza i obnova | potvrđujuća i istraživačka odluka, analitička fleksibilnost, reproducibilnost |
| 13 — Kategorički podaci | uvjetni nazivnik i kontingencijska tablica |
| 14 — Dvije grupe | usporedba dviju skupina i jedinica neovisnosti |
| 15 — Više grupa | cijena višestrukosti |
| 16 — Regresija | model, prilagođena povezanost i pošteno uvjetno izvještavanje |
| 17 — Doba algoritama | prag, nejednak teret pogreške, nadzor i prigovor |

Nijedan preduvjet ne pokazuje na kasniju jedinicu, jer kasnije jedinice nema.

Predgovor je namjerno **izostavljen** iz popisa preduvjeta. On je čitateljski
ugovor, a ne gradivo o kojemu kasnija jedinica ovisi, i nijedna ratificirana
kralježnica u knjizi ne imenuje ga kao preduvjet. Kumulativnost završnice tvrdi
se o sedamnaest poglavlja, i tako je strojno provjerljiva.

Posljedica je obvezujuća i za metapodatke. Postojeći redak `.chapter-meta` u
poglavlju 18 danas navodi „pogl. 2, 6 i 16", što je uže od ratificiranoga
preduvjeta i time proturječi prvomu isključenju. Ovaj gate tu prozu **ne
mijenja**; ispravak je obveza paketa `WE-C18`, a `P5-ROUTES` ne smije objaviti
nijedan put koji čitatelja uvodi u poglavlje 18 bez cijele knjige.

## Izmjena zabrane nove metode

Preporučena zadana odluka zabilježena u vanjskom upitu `OA-G-A2B-FINALE-SPINE`
glasi: učiniti poglavlje 18 kumulativnim na razini cijele knjige, **ne uvesti
nijednu novu metodu**, i empirijski prijenos iskoristiti za cjelovitu reviziju.

**Autor je taj dio izmijenio.** Poglavlje 18 *smije* uvesti tehniku koju
obrađeni slučaj doista traži, pod tri točna ograničenja:

1. nikada metodu s popisa izvan opsega iz predgovora — vremenske serije,
   faktorska analiza i psihometrija, višerazinski modeli, matematika strojnoga
   učenja i puna Bayesovska inferencija;
2. u cijelosti objašnjena ondje gdje se pojavljuje, samodostatno;
3. bez ovisnosti prema naprijed — ne smije tražiti ništa što nijedna ranija
   kralježnica nije bila zadužena isporučiti.

Autorov zabilježeni razlog za ograničenja jest da bi **neomeđena nova metoda u
završnici ponovno otvorila obećanje opsega koje predgovor daje**. Sama izmjena
postoji zato da završnica ostane stvarno istraživanje: capstone koji bi morao
odbiti tehniku koju njegov vlastiti slučaj traži ili bi slučaj izobličio ili bi
čitatelja naučio da analizom upravlja popis metoda, a ne pitanje. Prvo načelo
knjige traži suprotno.

Dispozicija je zato zabilježena kao **`accepted_as_amended`**, a ne
`accepted_as_recommended`. To je jedina razlika između zabilježene namjere i
preporučene zadane odluke na svih sedam kralježničnih gateova.

Ograničenja su upisana kao **isključenja 2 i 3** kralježnice, pa nisu ostavljena
kao proza. Provode ih dva paketa, oba izrijekom imenovana zabilježenom
namjerom:

- **`P2-SPINE-FINALE`** upisuje oba isključenja u `chapter-spine.json` i
  proširuje `scripts/check-chapter-spines.py` njihovim točnim oznakama, pa
  granica postaje strojno provjerljiva prije nego što je ijedna rečenica
  poglavlja napisana;
- **`P6-CONTINUITY`** provjerava gotovu knjigu prema toj granici i mora naći
  svaku tehniku koja je u završnicu ušla bez cjelovitoga objašnjenja na mjestu
  pojavljivanja ili s ovisnošću koju nijedna ranija kralježnica ne isporučuje.

Paket `WE-C18`, koji prozu piše, vezan je ratificiranom kralježnicom, a ne
zasebnom isporukom. Udvostručena bi isporuka stvorila drugi izvor iste obveze,
što je isti razlog iz kojega `G-A2b-V` nije udvostručio obveze svojih dvaju
durabilnih zapisa.

### Odnos prema ratificiranoj stavci `R17-C18-two-pass`

Izmjena i ratificirani registar ne proturječe si, ali ih treba čitati zajedno, i
to se ovdje izriče umjesto da se prešuti.

Test prihvaćanja stavke `R17-C18-two-pass` traži da **empirijski prijenos ne
uvodi nijednu metodu**. Izmjena dopušta tehniku koju traži *obrađeni slučaj*, a
obrađeni je slučaj poglavlja 18 njegova glavna vođena studija: cijelo tijelo
poglavlja jedan je prošireni obrađeni primjer, kako je ratificirano u kosturu
poglavlja. Dopuštenje zato slijeće u glavnu studiju, dok prijenos ostaje bez
nove metode, i tako je zapisano kao isključenje 4.

Uz to vrijedi odluka D13: glavna studija ostaje objasnidbena. Dopuštena tehnika
mora biti s time uskladiva i ne smije glavnu studiju pretvoriti u predikcijsku,
što nosi isključenje 5.

Ako autor želi da dopuštenje dosegne i empirijski prijenos, to traži izmjenu
testa prihvaćanja stavke `R17-C18-two-pass`. **Ovaj gate tu izmjenu namjerno ne
provodi** i tu stavku ne dira.

## Hijerarhija definicija za završnicu

Ovaj gate rješava stavku `R04-C18-definitions`. Poglavlje 18 danas nema nijedan
`#def-` blok i time pada ispod ratificiranoga pojasa
`bands.definitions_per_chapter`, koji traži od jednoga do pet.

Odluka slijedi isto pravilo kao Dijelovi I, II, IV i V: blok dobiva samo pojam o
kojemu kasnija jedinica stvarno ovisi, a pojam koji završnica samo dohvaća
ostaje u prozi uz mehanizam `.pojam`. Za posljednju jedinicu u knjizi pravilo
traži jedan dodatak, i to se ovdje zapisuje, a ne pretpostavlja: **kasnijega
poglavlja nema**, pa se test primjenjuje na jedine nizvodne potrošače koji
postoje — pojmovnik i graf pojmova koji se generiraju iz `#def-` blokova,
protokol Dodatka F, zatvaranje ocjenjivanja jedinice 18 u paketu
`P5-CLOSURE-18` i objavljene studentske putove u paketu `P5-ROUTES`.

Točno jedan pojam prolazi taj test.

| Poglavlje | `#def-` blok | Proza pri prvoj upotrebi | Odgođeno |
|---|---|---|---|
| 18 | paket dokaza | putovnica skupa podataka, trag odluka, dnevnik transformacija, potvrđujuća analiza, istraživačka analiza, provjera osjetljivosti, granica tvrdnje, reproducibilan tijek rada, pošten izvještaj, objava uporabe asistenta, minimizacija podataka | — |

**Paket dokaza** dobiva blok jer je to jedini objekt koji završnica *stvara*, a
ne dohvaća. Njegov je sadržaj već ratificiran ulogom `finale` u registru
životnoga ciklusa — putovnica skupa podataka, zapis izvora i verzije, dnevnik
transformacija, analiza, provjera osjetljivosti, granica tvrdnje, zapis o
uporabi asistenta i objava — i pet ratificiranih stavki registra traži ga
imenom: `R08-SPINE-18`, `R11-C18-table-audit`, `R13-C18-corpus-package`,
`R24-C18-workflow` i `R32-C18-transfer-path`. Bez kanonskoga zapisa svaka od tih
stavki nosi vlastitu inačicu istoga popisa, a `P5-CLOSURE-18` i `P5-ROUTES`
nemaju jedan oblik prema kojemu bi provjeravali predani rad.

Jedanaest ostalih pojmova ostaje u prozi, i za svaki postoji razlog:

- **trag odluka** i **reproducibilan tijek rada** ne dobivaju blok jer je
  `reproducibilnost` već odobren blok poglavlja 12; završnica ga žanje, a drugi
  bi zapis stvorio dva izvora istine o istoj obvezi;
- **potvrđujuća analiza** i **istraživačka analiza** ne dobivaju blok jer je
  njihova razlika argument poglavlja 12 i već je nosi odobren blok `analitička
  fleksibilnost`;
- **putovnica skupa podataka** i **dnevnik transformacija** ne dobivaju blok jer
  su sastavnice paketa dokaza i definirane su unutar njegove definicijske
  rečenice; zaseban bi ih zapis odvojio od cjeline koju čine;
- **provjera osjetljivosti** i **granica tvrdnje** ne dobivaju blok jer su
  ratificirani standardi prihvaćene arhitekture — `sensitivity_standard` i
  registar tvrdnji sa šest dimenzija — pa bi blok udvostručio već ratificiran
  mehanizam;
- **pošten izvještaj** ne dobiva blok jer je standard `honest_sentence_standard`
  ratificiran u `conventions.json` sa svojih šest zahtjeva i tri zabrane, a
  poglavlje ga provodi, ne definira;
- **minimizacija podataka** i **objava uporabe asistenta** ne dobivaju blok jer
  su pravila datirane politike kolegija iz odluke D15, čiji je nositelj Dodatak
  F. Definicijski bi ih blok predstavio kao bezvremene pojmove, što stavka
  `R24-C18-dated-policy` izričito zabranjuje.

Poglavlje 18 time prelazi s nula na jedan blok i ulazi u pojas. Neto učinak na
zamrznuti skup od 46 živih definicija, zajedno sa svim ranije odobrenim kartama,
iznosi 52: 46 + 3 (`G-A2b-I`) − 2 (`G-A2b-II`) + 0 (`G-A2b-III`) + 2
(`G-A2b-IV`) + 2 (`G-A2b-V`) + 1 (ovaj gate).

Ovaj gate blok **ne piše**. Kartu provodi `WE-C18` nad stvarnom prozom i
`P2-TERMS` nad ledgerom i grafom pojmova, nakon što `G-A2c` utvrdi kanonski
hrvatski oblik. Do tada `H-P1C-INTEGRITY-002` drži skup od 46 definicija
zamrznutim, poglavlje 18 nosi nula blokova, a ukupan broj ostaje 46.

Kanonski hrvatski oblici svih pojmova ove kralježnice ostaju odluka gatea
`G-A2c`. To osobito vrijedi za `paket dokaza`, `putovnica skupa podataka` i
`objava uporabe asistenta`, koje kralježnica imenuje kao nosive, ali ne
kanonizira.

## Točne oznake za deterministički provjeritelj

Paket `P2-SPINE-FINALE` upisuje ovu kralježnicu i proširuje
`scripts/check-chapter-spines.py` točno ovim obvezama. Oznake su doslovni
podnizovi teksta isključenja.

| Jedinica | Obvezne oznake isključenja |
|---|---|
| 18 | `bez cijele knjige`, `popisa izvan opsega iz predgovora`, `u cijelosti objašnjena ondje gdje se pojavljuje`, `ocijenjeni zadatak pisanja koda` |

| Jedinica | Obvezni nosivi pojmovi |
|---|---|
| 18 | paket dokaza, putovnica skupa podataka, trag odluka, granica tvrdnje, provjera osjetljivosti |

Uvjet redoslijeda ratifikacije jednak je popisu preduvjeta: 18 nakon 1, 2, 3, 4,
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 i 17. Time poglavlje 18 ne može biti
ratificirano prije nijednoga ranijeg poglavlja, a knjiga dobiva svoj posljednji
strojno provjerljiv dokaz da je završnica doista kumulativna.

Druga i treća oznaka zajedno čine strojnu provedbu izmijenjene granice nove
metode. Njihovo je uklanjanje upravo ono što `P2-SPINE-FINALE` mora učiniti
nemogućim, a `P6-CONTINUITY` mora prepoznati u gotovom tekstu.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Poglavlje 18 kumulativno je na razini cijele knjige | Aspekt 1; popis od sedamnaest preduvjeta; isključenje 1; uvjet redoslijeda ratifikacije |
| Žanje svaku nit kroz jedan empirijski zadatak prijenosa koji student revidira od početka do kraja | Aspekti 8 i 12; pojam `paket dokaza`; isključenje 4 |
| Uključujući reviziju asistentova izvještaja o istoj analizi | Aspekt 9 |
| Sedma nit komunikacije slijeće ovdje | Aspekt 9; ugovor završnice |
| Izmjena: dopuštena tehnika koju obrađeni slučaj doista traži | Isključenje 3; odjeljak „Izmjena zabrane nove metode" |
| Ograničenje 1 — nikada metoda s popisa izvan opsega | Isključenje 2 |
| Ograničenje 2 — u cijelosti objašnjena, samodostatna | Isključenje 3, prvi uvjet |
| Ograničenje 3 — bez ovisnosti prema naprijed | Isključenje 3, drugi uvjet |
| `P2-SPINE-FINALE` i `P6-CONTINUITY` provode ograničenja | Odjeljak o izmjeni; oznake za provjeritelja; prijenos `H-G-A2B-FINALE-001` |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki. Ostali aspekti nisu
novi zahtjevi. Svaki provodi već ratificiranu stavku registra, prihvaćenu odluku
ili prihvaćenu arhitekturu.

| Aspekt | Već ratificirani izvor |
|---|---|
| 1 | `R04-C18-whole-prerequisites`, `R10-C18-whole-book-harvest` |
| 2 | registar tvrdnji sa šest dimenzija i šest revizijskih pitanja |
| 3 | `R11-C18-table-audit` |
| 4 | nit reproducibilnosti i podrijetla; uloga `finale` u životnom ciklusu |
| 5 | prihvaćeni `R09-C18-interval-conclusion` |
| 6 | `R19-C18-substantive-sensitivity` i `sensitivity_standard` |
| 7 | `R08-SPINE-18`, odluka D13 |
| 8 | `R17-C18-two-pass`, `R13-C18-corpus-package`, `R32-C18-transfer-path` |
| 9 | sedma nit; prihvaćeni `R17-REPORT-honest-standard` |
| 10 | `R24-C18-workflow`; razina `finale` ljestvice AI kompetencija |
| 11 | `R24-C18-dated-policy`, `R24-C18-privacy-sources`, odluka D15 |
| 12 | `R10-C18-whole-book-harvest`, `R24-C18-explanatory-scope`, `R24-C18-algorithm-harvest`, `R35-REACHBACK-18`, `R27-C17-18-transition` |
| isključenje 7 | `R23-SCOPE-reading-not-production` i granica H10 |
| isključenje 8 | ugovor vidljivosti rješenja iz odluke D06 |
| isključenje 10 | `R11-SCOPE-no-multiple-imputation` |

## Razmotrene alternative

1. **Zadržati preporučenu zabranu i ne dopustiti nijednu novu tehniku.**
   Odbijeno: proturječi zabilježenoj autorovoj namjeri, koja upravo tu zadanu
   odluku mijenja. Zadržana je kao granica u trima ograničenjima, a ne kao
   zabrana.
2. **Dopustiti novu tehniku bez ograničenja, jer je završnica ionako
   posljednje poglavlje.** Odbijeno: autorov zabilježeni razlog jest da bi
   neomeđena metoda ponovno otvorila obećanje opsega iz predgovora.
3. **Upisati ograničenja kao prozu ugovora, a ne kao isključenja.** Odbijeno:
   proza nije strojno provjerljiva, a `P6-CONTINUITY` bi granicu morao izvoditi
   iz izvještaja umjesto iz registra.
4. **Proširiti dopuštenje i na empirijski prijenos.** Odbijeno: test
   prihvaćanja ratificirane stavke `R17-C18-two-pass` traži prijenos bez nove
   metode, a ovaj gate tu stavku ne mijenja.
5. **Navesti preduvjet kao „cijela knjiga" bez popisa poglavlja.** Odbijeno:
   nepopisan preduvjet nije strojno provjerljiv i ne može nositi uvjet
   redoslijeda ratifikacije.
6. **Uključiti predgovor u popis preduvjeta.** Odbijeno: predgovor je
   čitateljski ugovor, a ne gradivo; nijedna druga kralježnica ne imenuje ga kao
   preduvjet, pa bi ga završnica uvela kao presedan bez potrebe.
7. **Ne dodati poglavlju 18 nijedan blok, uz zabilježenu iznimku od pojasa.**
   Odbijeno: ostavlja jedino numerirano poglavlje izvan ratificiranoga pojasa i
   traži zasebnu izmjenu `conventions.json` koju nijedan gate nije odobrio, dok
   paket dokaza ostaje bez kanonskoga oblika koji četiri kasnija paketa
   provjeravaju.
8. **Dati blok tragu odluka ili reproducibilnom tijeku rada.** Odbijeno:
   `reproducibilnost` je već odobren blok poglavlja 12, pa bi drugi zapis stvorio
   dva izvora istine o istoj obvezi.
9. **Dati blok minimizaciji podataka ili objavi uporabe asistenta.** Odbijeno:
   oba su pravila datirane politike iz odluke D15 čiji je nositelj Dodatak F, a
   `R24-C18-dated-policy` zabranjuje da se datirana politika prikaže kao
   bezvremeni pojam.
10. **Dati blok poštenom izvještaju.** Odbijeno: standard je već ratificiran u
    `conventions.json` sa šest zahtjeva i tri zabrane, pa bi blok udvostručio
    mehanizam koji poglavlje treba provesti, a ne definirati.
11. **Pretvoriti glavnu studiju u predikcijsku kako bi završnica potrošila
    alate poglavlja 17.** Odbijeno: proturječi odluci D13 i stavki
    `R24-C18-explanatory-scope`, koja traži da se izostavljanje izrekne kao
    odluka o opsegu tvrdnje.
12. **Uvesti widget u završnicu radi simetrije s poglavljima 1 do 17.**
    Odbijeno: `widget_policy` izrijekom izuzima predgovor i poglavlje 18, a
    cijelo je tijelo poglavlja jedno prošireno vođeno istraživanje.

## Obvezujuće autorove izmjene od 5. kolovoza 2026.

Obje izmjene pročitane su prije odluke i obje ovdje vrijede.

Neovisni recenzent nazivlja povučen je iz prvoga izdanja. Ova kralježnica **ne
tvrdi i ne pretpostavlja nikakvu neovisnu recenziju** — nazivlja ni bilo čega
drugoga. Kanonski hrvatski oblici pojmova završnice ostaju odluka gatea `G-A2c`
i isključiva su odgovornost autora i urednika.

Za odabrane izvatke DZS-a i DIP-a nije traženo niti dobiveno dopuštenje vlasnika
prava. Ova kralježnica **ne tvrdi nikakvo dopuštenje** ni za jedan izvor i ne
bira nijedan podatkovni paket: odabir paketa za empirijski prijenos upisan je
kao obveza njegovih gateova podataka i paketa `WE-C18`.

Ta se dva ograničenja namjerno **ne** upisuju kao isključenja kralježnice.
Njihovi durabilni zapisi već imenuju točne pakete koje vežu, pa bi njihovo
udvostručavanje u registru kralježnica stvorilo drugi izvor istine o obvezi koju
taj registar ne posjeduje. Ovaj gate stoga bilježi usklađenost, a ne novu
obvezu.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu završnice, njezinu hijerarhiju
definicija, njezine preduvjete i izmijenjenu granicu nove metode. Ne odobrava
prozu poglavlja 18 i ne mijenja nijednu datoteku poglavlja niti dodatka; osobito
ne mijenja postojeći redak `.chapter-meta`, koji ostaje obveza paketa `WE-C18`.
Ne upisuje ništa u `bookwright_plugin/bookwright/shared/chapter-spine.json`; to
je posao paketa `P2-SPINE-FINALE`. Ne dodaje i ne briše nijedan `#def-` blok i
ne regenerira graf pojmova; to ostaje paketima `WE-C18` i `P2-TERMS`. Ne troši
`H-P1C-INTEGRITY-002`, koji ostaje obveza paketa `P2-TERMS`, ni `H-G-A2D-005`,
koji ostaje obveza paketa `P5-F`, `P6-EVIDENCE` i `WE-C18`, ni
`H-P2-SPINE-V-001` i `H-P2-SPINE-V-002`. Ne mijenja i ne zamjenjuje nijedan
identitetski brif ni ratificiranu kralježnicu ranijega dijela. Ne mijenja test
prihvaćanja stavke `R17-C18-two-pass`. Ne utvrđuje kanonsku terminologiju, koja
ostaje gateu `G-A2c`. Ne definira i ne objavljuje nijedan put čitanja;
`P5-ROUTES` zadržava tu ovlast zajedno s obvezom da nijedan put ne uvodi
čitatelja u poglavlje 18 bez cijele knjige. Ne zatvara ocjenjivanje jedinice 18,
što ostaje paketu `P5-CLOSURE-18`. Ne ratificira nijednu kralježnicu, ne otvara
`G-A2c` i ne pokreće `P2-SPINE-FINALE`. Ne bira nijedan podatkovni paket, izvor
ni slučaj i ne tvrdi nikakvo dopuštenje vlasnika prava. Ne tvrdi nikakvu
neovisnu recenziju. Ne mijenja fazu nijedne jedinice, koja ostaje `draft`. Ne
odobrava render, generirani artefakt, push, merge, tag, arhiviranje, deployment
ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavke `R04-SPINE-FINALE`, `R04-C18-definitions` i
  `R04-C18-whole-prerequisites`;
- paket `P2-SPINE-FINALE`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json` i proširuje
  `scripts/check-chapter-spines.py`.

Ovisnosti koje ostaju blokirane: `WE-C18` čeka `WD-PART`, `P2-SPINE-FINALE`,
svoje gateove podataka i gate prihvaćanja `C18`; `P5-CLOSURE-18` čeka
`P5-CLOSURE-17` i `P2-ASSESS`; `P2-TERMS` čeka `G-A2c`; `P5-ROUTES` i
`P6-CONTINUITY` čekaju svoje faze. Time je svih sedam kralježničnih gateova
odlučeno, a `G-A2c` i `P2-SPINE-FINALE` ostaju zasebni i neotvoreni.
