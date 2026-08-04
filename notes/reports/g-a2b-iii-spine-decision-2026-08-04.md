# G-A2b-III — ratificirana kralježnica Dijela III

**Gate:** `G-A2b-III`

**Datum odluke:** 4. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2b-III-spine-approved-2026-08-04-Luka-Sikic`, vezano uz nacrt
kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu Dijela III: nosive aspekte,
nosive pojmove, preduvjete i isključenja za poglavlja 7, 8 i 9, ugovor na razini
dijela te dispoziciju definicijskoga opterećenja Dijela III. Ne odobrava prozu,
ne dodaje i ne uklanja nijedan `#def-` blok i ne ratificira nijednu kasniju
kralježnicu.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-III-SPINE`, upravljana stavka `R04-SPINE-III`, prihvaćene arhitekture
`G-A2a` i `G-A2d`, identitetski brifovi `P2-IDENTITY`, ratificirane kralježnice
predgovora te Dijelova I i II, zabilježena autorova namjera, pravilo `H10` u
`STYLE.md`, pojasevi `bands` u `conventions.json` te sve stavke registra koje
ciljaju poglavlja 7, 8 i 9, uključujući prihvaćene ispravke paketa `P1A-C07`,
`P1A-C08` i `P1A-C09`.

Cjeloviti ledger prijenosa pročitan je prije odluke. Nijedan prijenos ne cilja
`G-A2b-III`, pa nema dolazne isporuke koju bi ovaj gate priznao ili potrošio.

`H-P0-REGISTER-008` cilja `WC-C08`, `WC-C09` i `WD-C17` i ostaje `pending`.
Kralježnice poglavlja 8 i 9 njegov dug **izriču kao vlastitu obvezu tih paketa**,
ali ga ovaj gate ne naplaćuje i ne troši. Isto vrijedi za
`H-P1C-INTEGRITY-002`, koji ostaje obveza paketa `P2-TERMS` i zamrzava skup od 46
živih definicija.

## Ugovor na razini Dijela III

Dio III nosi tri koraka i ništa više: **što slučajnost proizvodi**, zatim **dokle
uzorak seže**, zatim **što procjena kaže zajedno sa svojom nesigurnošću**.
Redoslijed vjerojatnost, uzorkovanje, procjena zadržava se nepromijenjen.

Cijeli je dio organiziran oko jednoga pitanja: **što generalizacija može, a što
ne može dohvatiti**. Svako od triju poglavlja odgovara na jedan njegov dio.
Poglavlje 7 pokazuje da slučajnost ima pravilnosti koje se mogu opisati.
Poglavlje 8 pokazuje da uzorak doseže populaciju samo pod uvjetima koje netko
mora osigurati. Poglavlje 9 pokazuje da procjena bez svoje nesigurnosti još nije
tvrdnja.

**Poglavlje 8 pedagoška je okosnica knjige** i ovaj gate to čuva izričito. Ono je
mjesto na kojemu čitatelj prelazi s opisivanja podataka koje ima na tvrdnju o
populaciji koju nije vidio. Zbog toga poglavlje 8 nosi najveći dio pojmovnoga
opterećenja dijela i jedino ono formalno uvodi populaciju, uzorak i pogrešku
uzorkovanja, odgođene iz poglavlja 1.

Ovdje se naplaćuju dugovi posađeni u poglavlju 3. Rano čitanje ankete i margina
pogreške koje poglavlje 3 izriče kao najavljeni dug razrješuju se u poglavljima 8
i 9. Prema prijenosu `H-P0-REGISTER-008` ta je naplata obveza paketa `WC-C08` i
`WC-C09` nad stvarnom prozom; kralježnica dug imenuje i smješta, ali ga ne
zatvara.

Dio naglašava tri faze životnoga ciklusa iz prihvaćene arhitekture: prikupljanje,
modeliranje i vrednovanje. Razvija nit proračuna nesigurnosti, nit selekcije i
odsutnosti te nit komunikacije tvrdnje, a dohvaća jedinicu analize i nazivnik iz
ranijih dijelova. Na granici dijela nosi punu mapu tvrdnji sa šest dimenzija i
šest revizijskih pitanja, odgovorivu samoprovjeru i zadatak dohvata unatrag.

Ratificirano razlikovanje ostaje na snazi u cijelome dijelu: **vjerojatnosno
uzorkovanje za generalizaciju na populaciju nije isto što i razdvajanje na skup
za učenje, provjeru i ispitivanje**, i jedno ne zamjenjuje drugo.

Simulacija ostaje ispred formalizma. Seeded simulacije nose demonstracije, a
empirijski podaci ulaze kao omeđeni prijenos. Ljestvica AI kompetencija u Dijelu
III traži razlikovanje proizvedene sigurnosti od uzoračke nesigurnosti i
osporavanje neutemeljenoga dosega na populaciju, uz čitljivu potvrdu provjere.
Nijedan ocijenjeni zadatak ne traži pisanje koda.

## Nacrtana kralježnica po poglavljima

### Poglavlje 7 — Vjerojatnost

**Nosivi aspekti**

1. Vjerojatnost kao ono što ponavljanje proizvodi na dugi rok, doživljeno
   simulacijom prije nego što je imenovano.
2. Vjerojatnost kao kalibrirana nesigurnost uz dugoročnu učestalost, bez
   istiskivanja simulacije.
3. Tri pravila i jedna pretpostavka: komplement, zbrajanje, množenje i neovisnost
   kao pretpostavka koja ih nosi.
4. Uvjetna vjerojatnost i razlika između vjerojatnosti A uz B i vjerojatnosti B
   uz A, uz temeljnu stopu dohvaćenu iz poglavlja 3.
5. Ponovljeni pokušaji s dva ishoda: binomna raspodjela kao model brojanja.
6. Zvonasta krivulja i njezino područje kao način čitanja koliko je vrijednost
   neobična; standardizirana vrijednost iz poglavlja 4 postaje položaj na poznatoj
   krivulji.
7. Uvjeti pod kojima uvodna tvrdnja o središnjem graničnom teoremu vrijedi:
   stabilna zajednička raspodjela, neovisna opažanja i konačna varijanca, uz
   widget omeđen kao demonstracija.
8. Kada podaci ne pristaju krivulji, i zašto je to obavijest, a ne neuspjeh.
9. Nizovi koje slučajnost sama proizvodi: nizovi pogodaka, odabir nakon niza i
   ljudska sklonost čitanju uzorka u šumu.
10. Sredina poglavlja nosi stanku za dohvat, a poglavlje smanjuje količinu
    istodobne novosti.

**Nosivi pojmovi**: vjerojatnost, neovisnost, uvjetna vjerojatnost, binomna
raspodjela, normalna raspodjela, zakon velikih brojeva, kalibrirana nesigurnost,
slučajni niz.

**Preduvjeti**: poglavlja 3 i 4.

**Isključenja**: nikakva distribucija uzorkovanja statistike ni standardna
pogreška, koje pripadaju poglavlju 8; nikakav interval ni test, koji pripadaju
poglavljima 9 i 10; nikakav mjerno-teorijski ni kombinatorni aparat izvan onoga
što traži jedno pravilo na razini pismenosti; nikakva puna Bayesovska inferencija,
jer je kalibrirana nesigurnost stupanj uvjerenja, a ne tečaj; demonstracija
središnjega graničnog teorema ne smije se iznijeti kao opće jamstvo za proizvoljne
podatke, ovisnost ili beskonačnu varijancu; nijedan ocijenjeni zadatak pisanja
koda; nijedan izmišljen ili neizvorni empirijski primjer.

### Poglavlje 8 — Uzorkovanje

**Nosivi aspekti**

1. Okosnica knjige: prijelaz s opisivanja podataka koje imamo na tvrdnju o
   populaciji koju nismo vidjeli.
2. Populacija, uzorak i pogreška uzorkovanja imenovani su ovdje, nakon što ih je
   simulacija proizvela; iz poglavlja 1 su izričito odgođeni upravo dovde.
3. Ponovljeno uzorkovanje i distribucija uzorkovanja kao predmet koji čitatelj
   gleda kako nastaje.
4. Standardna pogreška kao raspršenost te distribucije, uz imenovane
   pretpostavke jednostavnoga slučajnog uzorka.
5. Nacrt izvan jednostavnoga slučajnog uzorka na razini pismenosti: nejednake
   vjerojatnosti odabira, težine, klasteri, učinak nacrta, efektivna veličina
   uzorka i korekcija za konačnu populaciju, uz jednu provjerenu usporedbu
   ponderirane i neponderirane procjene.
6. Pokrivenost, neodgovor i način regrutacije: vjerojatnosni uzorak nasuprot
   samoodabiru, i zašto veličina uzorka ne popravlja selekciju.
7. Heuristika ankete od otprilike tisuću ljudi omeđena procjenjivanom veličinom,
   nacrtom, selekcijom, odazivom, veličinom podskupine i traženom preciznošću.
8. Kartica za čitanje ankete dovršava se ovdje; dug ranoga čitanja ankete iz
   poglavlja 3 naplaćuje paket `WC-C08` prema prijenosu `H-P0-REGISTER-008`.
9. Generalizacija na populaciju odvojena je od razdvajanja na skup za učenje,
   provjeru i ispitivanje; jedno ne zamjenjuje drugo.
10. Tekst kao problem uzorkovanja: koji govori, platforme, datumi, jezici i
    govornici uopće mogu ući u korpus.

**Nosivi pojmovi**: populacija, uzorak, pogreška uzorkovanja, distribucija
uzorkovanja, standardna pogreška, jednostavan slučajni uzorak, težina
uzorkovanja, učinak nacrta, efektivna veličina uzorka, pokrivenost, neodgovor,
prigodni uzorak.

**Preduvjeti**: poglavlja 2, 3, 4 i 7.

**Isključenja**: nikakav tečaj varijance u složenim anketnim nacrtima; težine,
klasteri i učinak nacrta objašnjavaju se samo na razini pismenosti; nikakav
interval ni test, koji pripadaju poglavljima 9 i 10; nikakva tvrdnja da veći
uzorak popravlja pokrivenost, neodgovor ili selekciju; nikakvo poistovjećivanje
vjerojatnosnoga uzorka s razdvajanjem na skup za učenje, provjeru i ispitivanje;
nijedan ocijenjeni zadatak pisanja koda, uz vidljivi kod koji se čita kao potvrda;
nijedan izmišljen ili neizvorni empirijski primjer, pa usporedba ponderirane i
neponderirane procjene mora biti provjerena; nikakva metoda obrade prirodnoga
jezika, jer je pitanje o korpusu pitanje o uzorkovanju; odabir podatkovnoga paketa
ostaje gateu `G-A3-ESS` i ostalim podatkovnim gateovima.

### Poglavlje 9 — Procjena

**Nosivi aspekti**

1. Od točke prema rasponu: procjena bez svoje nesigurnosti još nije tvrdnja.
2. Interval pouzdanosti i ono što razina pouzdanosti stvarno obećava, pokazano
   ponovljenim uzorkovanjem prije nego što je izrečeno.
3. Preciznost nasuprot pouzdanosti: uži interval i viša razina suprotstavljeni su
   zahtjevi, a veličina uzorka je cijena.
4. Bootstrap kao vlastiti izum: ponovno uzorkovanje daje raspon ondje gdje formule
   nema, uz imenovane pretpostavke o reprezentativnosti, neovisnosti i ispravnoj
   jedinici ponovnog uzorkovanja te uz granice na malim uzorcima, kod diskretnih
   vrijednosti i u repovima.
5. Opisni raspon po normalnom pravilu nije interval predviđanja za pojedinačno
   opažanje niti interval za sredinu.
6. Jedna percentilna bootstrap demonstracija jest konstrukcija raspona, a ne dokaz
   pokrivenosti.
7. Procjena, interval, jedinica i populacija kao jezik kojim ostatak knjige
   izvještava; poštena rečenica ovdje se razvija.
8. Uzoračka nesigurnost u kodiranom udjelu ne upija nesigurnost kodiranja i
   mjerenja.
9. Kratka čitljiva potvrda računa primjerena procjeni.
10. Dug margine pogreške iz poglavlja 3 razrješuje se ovdje i u poglavlju 8;
    naplata je obveza paketa `WC-C09` prema prijenosu `H-P0-REGISTER-008`.
11. Granica Dijela III: puna mapa tvrdnji sa šest dimenzija i šest revizijskih
    pitanja, odgovoriva samoprovjera i zadatak dohvata unatrag.

**Nosivi pojmovi**: procjena, interval pouzdanosti, razina pouzdanosti, margina
pogreške, preciznost, bootstrap, percentilni raspon, jedinica ponovnog
uzorkovanja, nesigurnost kodiranja.

**Preduvjeti**: poglavlja 3, 4, 7 i 8.

**Isključenja**: nikakav test hipoteze ni p-vrijednost, koji pripadaju poglavlju
10; nikakav model ni interval izveden iz modela, koji pripadaju poglavlju 16;
sredina uvećana i umanjena za 1,96 standardnih devijacija ne smije se iznijeti kao
opći interval predviđanja; pokusni eksperiment pokrivenosti z-intervala ne smije
se upotrijebiti kao provjera percentilnoga bootstrap intervala za medijan;
nijedan ocijenjeni zadatak pisanja koda, uz potvrdu računa koja se čita; nijedan
izmišljen ili neizvorni empirijski primjer; nikakva puna Bayesovska inferencija ni
poučavanje vjerodostojnih intervala, jer Bayesovski okvir ostaje omeđeni okvir u
poglavlju 10.

## Hijerarhija definicija za Dio III

Ovaj gate ne mijenja definicijsko opterećenje Dijela III. Poglavlje 7 zadržava
svojih pet blokova, poglavlje 8 svoja tri, a poglavlje 9 svoj jedan. Sva su tri
poglavlja unutar ratificiranoga pojasa od jedne do pet definicija, i nijedna
stavka registra ne traži izmjenu.

| Poglavlje | `#def-` blok | Proza pri prvoj upotrebi | Odgođeno |
|---|---|---|---|
| 7 | vjerojatnost, neovisnost, uvjetna vjerojatnost, binomna raspodjela, normalna raspodjela | zakon velikih brojeva, kalibrirana nesigurnost, slučajni niz | distribucija uzorkovanja i standardna pogreška (poglavlje 8) |
| 8 | pogreška uzorkovanja, distribucija uzorkovanja, standardna pogreška | populacija, uzorak, jednostavan slučajni uzorak, težina uzorkovanja, učinak nacrta, efektivna veličina uzorka, pokrivenost, neodgovor, prigodni uzorak | razdvajanje na skup za učenje, provjeru i ispitivanje (poglavlje 17) |
| 9 | interval pouzdanosti | procjena, razina pouzdanosti, margina pogreške, preciznost, bootstrap, percentilni raspon, jedinica ponovnog uzorkovanja, nesigurnost kodiranja | test i p-vrijednost (poglavlje 10), model (poglavlje 16) |

Margina pogreške svjesno ostaje u prozi. Poglavlje 8 je već imenuje i objašnjava
na prvoj upotrebi, a formalni bi blok udvostručio interval pouzdanosti iz
poglavlja 9 bez ijednoga kasnijeg poglavlja koje bi o njemu ovisilo. Dug iz
poglavlja 3 time je naplaćen sadržajno, a kanonski hrvatski oblik ostaje gateu
`G-A2c`.

Prvi je susret uvijek prije formalizacije. Nijedan `#def-` blok ne stoji prije
nego što je pojam doživljen u prozi, prikazu ili widgetu.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Zadržati vjerojatnost, zatim uzorkovanje, zatim procjenu | Ugovor dijela; preduvjeti poglavlja 8 i 9 |
| Očuvati poglavlje 8 kao pedagošku okosnicu knjige | Ugovor dijela; prvi i drugi aspekt poglavlja 8; najveće pojmovno opterećenje dijela |
| Organizirati dio oko onoga što generalizacija može i ne može dohvatiti | Ugovor dijela; aspekti 8.6, 8.7, 8.9 i 9.1 |
| Ovdje se naplaćuju dugovi ankete i margine pogreške iz poglavlja 3 | Aspekt 8.8 i aspekt 9.10, oboje izrijekom vezani uz `H-P0-REGISTER-008` |
| `H-P0-REGISTER-008` cilja `WC-C08`, `WC-C09` i `WD-C17`; dug izreći, prijenos ne trošiti | Prijenos ostaje `pending`; kralježnica ga imenuje kao obvezu tih paketa |

Ostali aspekti nisu novi zahtjevi. Svaki provodi već ratificiranu stavku registra
ili prihvaćenu arhitekturu.

| Aspekt | Već ratificirani izvor |
|---|---|
| 7.2 vjerojatnost kao stupanj uvjerenja | `R10-C07-degree-belief` |
| 7.7 uvjeti središnjega graničnog teorema | prihvaćeni `R09-C07-clt-conditions` |
| 7.10 stanka za dohvat i smanjena novost | `R29-C07-retrieval-load` |
| 8.4 granica jednostavnoga slučajnog uzorka | prihvaćeni `R12-C08-srs-boundary` |
| 8.5 složeni nacrt i ponderirana usporedba | prihvaćeni `R12-C08-complex-design`, `R12-C08-survey-realism`, `R12-C08-weighted-table` |
| 8.7 heuristika od tisuću ljudi | prihvaćeni `R12-C08-thousand-claim` |
| 8.9 generalizacija nasuprot razdvajanju skupova | `G-A2a` `lifecycle_registry.exclusions` |
| 8.10 korpus kao pitanje uzorkovanja | `R13-C08-corpus-selection` |
| 9.4 granice bootstrapa | prihvaćeni `R09-C09-bootstrap-failures` |
| 9.5 normalno pravilo nije interval predviđanja | prihvaćeni `R09-C09-normal-not-prediction` |
| 9.6 bootstrap medijana kao konstrukcija | prihvaćeni `R09-C09-bootstrap-validation` |
| 9.7 jezik procjene i intervala | `claim_registry.honest_sentence_standard`, mjesto razvoja |
| 9.8 nesigurnost kodiranja | `R13-C09-coded-uncertainty` |
| 9.9 čitljiva potvrda računa | `R23-C09-code-reading` |
| 9.11 granica dijela | `G-A2a` `claim_registry.placement_rule`, `R35-SELF-CHECK-III` |
| omeđena simulacija i empirijski prijenos | `R08-SPINE-07-11` |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki.

## Razmotrene alternative

1. **Staviti uzorkovanje ispred vjerojatnosti.** Odbijeno: proturječi
   zabilježenoj namjeri i odluci D03, a distribucija uzorkovanja bez pojma
   slučajnosti nema na čemu počivati.
2. **Spojiti procjenu u poglavlje o uzorkovanju.** Odbijeno: poglavlje 8 je
   okosnica upravo zato što staje na dosegu, a interval je zaseban korak koji
   traži vlastiti prostor.
3. **Definirati marginu pogreške kao `#def-` blok u poglavlju 8 ili 9.**
   Odbijeno: nijedno kasnije poglavlje ne ovisi o formalnome bloku, poglavlje 8 je
   već imenuje u prozi, a blok bi udvostručio interval pouzdanosti. `P2-SPINE-V` i
   `G-A2c` smiju to zatražiti ako kasnije poglavlje pokaže stvarnu potrebu.
4. **Naplatiti dug iz poglavlja 3 već u ovoj kralježnici.** Odbijeno: dug se
   naplaćuje nad prozom, a `H-P0-REGISTER-008` izričito cilja `WC-C08`, `WC-C09`
   i `WD-C17`.
5. **Uvesti složeni anketni račun varijance u poglavlje 8.** Odbijeno: proturječi
   prihvaćenoj granici iz `P1A-C08` i uvelo bi tečaj koji plan izričito isključuje.
6. **Uvesti Bayesovske vjerodostojne intervale u poglavlje 9.** Odbijeno: puna
   Bayesovska inferencija izvan je opsega knjige, a njezin omeđeni okvir pripada
   poglavlju 10.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu Dijela III. Ne odobrava prozu poglavlja
7, 8 ni 9 i ne mijenja nijednu datoteku poglavlja. Ne dodaje, ne briše i ne spaja
nijedan `#def-` blok i ne regenerira graf pojmova; to ostaje paketima `WC-C07`,
`WC-C08`, `WC-C09` i `P2-TERMS`. Ne troši `H-P0-REGISTER-008` ni
`H-P1C-INTEGRITY-002`, koji ostaju obveze paketa `WC-C08`, `WC-C09`, `WD-C17` i
`P2-TERMS`. Ne utvrđuje kanonsku terminologiju, koja ostaje gateu `G-A2c`. Ne
ratificira nijednu kasniju kralježnicu. Ne bira slučaj, izvor ni podatkovni paket,
osobito ne rutu za ESS. Ne mijenja fazu nijedne jedinice, koja ostaje `draft`. Ne
odobrava render, generirani artefakt, push, merge, tag, arhiviranje, deployment ni
objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavka `R04-SPINE-III`;
- paket `P2-SPINE-III`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json`.

Ovisnosti koje ostaju blokirane: `WC-C07`, `WC-C08` i `WC-C09` čekaju
`P3-VERIFY-C`, podatkovni gate `G-A3-ESS` te svoje gateove prihvaćanja `C07`,
`C08` i `C09`; `P2-TERMS` čeka `G-A2c`; `WC-PARTS` čeka svoja poglavlja.
