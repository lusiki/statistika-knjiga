# P5-VERIFY — vrata procjene, dodataka i putova

**Datum:** 26. kolovoza 2026.

**Paket:** `P5-VERIFY`

**Ugovor:** `review_gate`

Ovaj je paket samo provjerio i izvijestio. Nije popravljao prihvaćene pakete,
nije uređivao poglavlja, dodatke, zapise rješenja, generirane prikaze ni
provjerivače i nije zatvorio nijednu stavku ili roditelja registra. Otkriveni
su kvarovi dobili vlasnika i odredišni paket.

## Jedno deklarirano izvorno stanje

Cijelo se izvješće odnosi na jedno stanje:

`p5-verify-state:sha256-0a592fbf1a78f7281b9e528abd9688ed11483c705c77f1e6621490726c362990`.

Sažetak je izračunan nad ovim manifestom:

- izvorni commit
  `5b2de98ee2986a9616a52b13f4d51b9069f5f375`;
- Gitovo stablo
  `7731381e0e24a75e52a4128bc0b4a89509adc3c6`;
- deklarirani vanjski ulaz `data/_kandidat/p3-text/ParlaSent_BCS.jsonl`,
  SHA-256 `c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98`;
- deklarirani vanjski ulaz `data/_kandidat/p3-text/ParlaSent_BCS_test.jsonl`,
  SHA-256 `412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0`;
- deklarirani vanjski ulaz `data/_kandidat/p3-text/README.txt`, SHA-256
  `848a892cede62d37f469532eba6d2f5e6f00d29234f0257a67737f8a8646c285`.

Tri vanjska ulaza potrebna su samo za ponavljanje tekstne transformacije u
provjeri P5-A. Nisu predstavljena kao predani dio commita. Testovi Gitova
izvora izvedeni su u čistom checkoutu toga commita s isključenom pretvorbom
završetaka redaka; test P5-A dobio je samo tri navedena ulaza. Time se ne
spajaju različita sadržajna stanja. Ujedno je otkriveno da pojedini provjerivači
nepotrebno vežu ugrađene sažetke uz prikaz završetaka redaka u radnom stablu;
taj je kvar zasebno odgođen s vlasnikom.

## Audit dolaznih handoffa

Početna tvrdnja da knjiga handoffa ima nula dostava za P5-VERIFY nije vrijedila
u kanonskom stanju. Knjiga ima dvije dostave: `H-P5-ROUTES-001` i
P5-VERIFY-dostavu iz `H-P5-ROUTES-002`. Obje su priznate prije sadržajne
provjere i potrošene prije zatvaranja.

Audit svih paketa Faze 5 našao je šest handoffa s izvorom u toj fazi. Četiri su
prijenosa bila usmjerena samo na P5-ROUTES:

- `H-P5-CLOSURE-00-001` prenio je ugovor jednoga spremišta zapisa;
- `H-P5-B-001` prenio je granicu 19 podržanih i 7 ograđenih jamovi vrijednosti;
- `H-P5-D-001` prenio je kvar razlikovanja Quarto i bibliografskih referenci;
- `H-P5-G-001` prenio je osnovu 19/7/38/17/17/4 prije rute rješenja.

To je stvarna posredna ruta, ali nije preostala praznina dostave: P5-ROUTES ih
je potrošio s dispozicijama, ugradio rezultate u vlastiti artefakt i dokazne
zapise te predao završnu osnovu 19/7/39/1/17/17/4 u
`H-P5-ROUTES-001`. Rizik uvoda slike dobio je vlastitu izravnu dostavu u
`H-P5-ROUTES-002`. Gate je ipak ponovno pročitao sva četiri izvorna handoffa,
a nije njihov sadržaj pretpostavio iz statusa P5-ROUTES.

## Provjera P5-ROUTES prije matrice

Trinaest, a ne dvanaest, primjenjivih dostava za P5-ROUTES imaju stanje
`consumed`, vlastitu dispoziciju i barem jedan dokaz. Posebni testovi potvrđuju:

- `R04-ARCH-macro-order`, `R04-ROUTES-two-track-map` i putovnu polovicu
  `R04-C18-whole-prerequisites` zasebno su prihvaćeni;
- roditelj `R04` ostaje `ratified`, kao i roditelji `R23` i `R24`; zatvoreni
  su samo roditelji `R15` i `R21` nakon svih vlastitih potrebnih potomaka;
- oba čitateljska puta prolaze Poglavlja 1–18 u kanonskom redoslijedu, s
  Poglavljem 13 prije 17 i cijelom ranijom knjigom prije 18;
- dio `book.chapters` u `_quarto.yml` nije preuređen; dodane su samo provjere
  prije izgradnje i javna poveznica na odvojenu rutu rješenja;
- `config/book-inventory.json#solution_routes` sadrži točno jednu stranicu,
  a `rjesenja.qmd` je čista projekcija svih 95 zapisa iz
  `assessment/solution-records`; u poglavljima nema drugoga izvora odgovora.

Kanonski SHA-256 artefakta `config/pathway-routes.json` jest
`7e9b227de93fc3ed16f6e7d7576be0ef5c211b8cda755a5b7c69b275a5f758db`.

## Matrica 27 imenovanih preduvjeta

Svaki je redak provjeren protiv vlastitih zahtjeva paketa. Status `accepted`
nigdje nije korišten kao zamjena za izvještaj, artefakt, sidro, brojčani test,
vidljivost ili tiskovni ulaz.

| Preduvjet | Vlastiti dokaz i ponovljeni test | Presuda na deklariranom stanju |
|---|---|---|
| `P5-CLOSURE-00` | 5 zapisa, 5 sidara, vlastiti brojčani trag jedinice 00 i provjera javne/zaštićene vidljivosti; sadašnji jedinični sažetak `55c5d9c4…` | prolazi |
| `P5-CLOSURE-01` | 5 zapisa i sidara; brojčani i tiskovni trag jedinice 01; `468d2505…` | prolazi |
| `P5-CLOSURE-02` | 5 zapisa i sidara; obrnuto kodiranje i tiskovni trag; `b6c2e6b2…` | prolazi |
| `P5-CLOSURE-03` | 5 zapisa i sidara; DIP/medijski brojnici i jedna posađena pogreška; `9e4676e4…` | prolazi |
| `P5-CLOSURE-04` | 5 zapisa i sidara; join, agregat i tiskovne tablice; `ce1c7878…` | prolazi |
| `P5-CLOSURE-05` | 5 zapisa i sidara; nejednake širine i statički tiskovni prikaz; `5249d06d…` | prolazi |
| `P5-CLOSURE-06` | 5 zapisa i sidara; korelacijski, rasponski i tiskovni trag; `7bfef840…` | prolazi |
| `P5-CLOSURE-07` | 5 zapisa i sidara; komplement i dijagnostička tablica; `cdedc04f…` | prolazi |
| `P5-CLOSURE-08` | 5 zapisa i sidara; ponderirana/neponderirana usporedba i tiskovna tablica; `385fcdf5…` | prolazi |
| `P5-CLOSURE-09` | 5 zapisa i sidara; širine intervala, promašaji i tiskovni preseti; `bfe8a07e…` | prolazi |
| `P5-CLOSURE-10` | 5 zapisa i sidara; permutacija, kalibracija i Monte Carlo trag; `83381cdf…` | prolazi |
| `P5-CLOSURE-11` | 5 zapisa i sidara; učinak, snaga i tiskovne vrijednosti; `8559bfea…` | prolazi |
| `P5-CLOSURE-12` | 5 zapisa i sidara; replikacija, sinteza, višestrukost i tisak; `ec511c67…` | prolazi |
| `P5-CLOSURE-13` | 5 zapisa i sidara; tablica, hi-kvadrat i Cramérov V; `ad23f162…` | prolazi |
| `P5-CLOSURE-14` | 5 zapisa i sidara; Welch/OLS, upareni put, osjetljivost i tisak; `51aeb351…` | prolazi |
| `P5-CLOSURE-15` | 5 zapisa i sidara; ANOVA, Tukey, robusnost, višestrukost i tisak; `d3cf1161…` | prolazi |
| `P5-CLOSURE-16` | 5 zapisa i sidara; zasebni regresijski brojčani test, artefakt rezultata i tisak; `a4e4602e…` | prolazi |
| `P5-CLOSURE-17` | 5 zapisa i sidara; tekstni paket, klasifikacija, pravednost i tisak; `ef90f9be…` | prolazi |
| `P5-CLOSURE-18` | 5 zapisa i sidara; capstone, paket dokaza, tekstni prijenos i tisak; `71703578…` | prolazi |
| `P5-A` | `check-appendix-a.py` ponovno je izveo 26 provjera za Poglavlja 6–16 i tekstnu transformaciju iz tri deklarirana vanjska ulaza | prolazi uz izričitu granicu da tri sirova ulaza nisu u commitu |
| `P5-B` | `check-appendix-b.py` potvrđuje 26/26 pariteta, 19 podržanih i 7 ograđenih vrijednosti, sidra i tiskovni ulaz | prolazi; čista jamovi instalacija ostaje nepotvrđena i javno sužena |
| `P5-C` | `check-appendix-c.py` i čisti graditelj zaustavljaju se jer `config/appendix-c-data-route.json` nema kontrolni zbroj sadašnjega `data/katalog.yml` | **blokator**; vlasnik `P6-DATA` |
| `P5-D` | `check-appendix-d.py` potvrđuje 9 podržanih, 9 stop-ruta, 20/20 slučajeva, 17 sidara i tiskovni PNG | prolazi |
| `P5-E` | terminološki registar prolazi samostalno, ali `check-appendix-e.py` zaustavlja zastarjeli hash `conventions.json`; `check-concepts.py` dodatno nalazi zastarjeli graf 664 naspram 662 ponovno izgrađene veze | **blokator**; vlasnik `P6-CONTINUITY` |
| `P5-F` | sadržajna granica 3 trake, 8 koraka i 95 sigurnih ruta ostaje zabilježena, ali `check-appendix-f.py` zaustavlja zastarjeli izvorni hash nakon kasnije promjene konvencija | **blokator**; vlasnik `P6-EVIDENCE` |
| `P5-G` | četiri teme i četiri prve uporabe ostaju u izvoru, ali `check-appendix-g.py` nalazi zastarjeli artefakt nakon dodavanja D06 rute rješenja u inventar | **blokator**; vlasnik `P6-CONTINUITY` |
| `P5-ROUTES` | čisti checkout potvrđuje 2 rute, svih 19 kralježnica, 95 javnih provjera, 95 zaštićenih rubrika, 0 drugih izvora, 5 klasa putova i osnovu 19/7/39/1/17/17/4 | prolazi |

Matrica zato daje 23 prolaza i 4 jasno odgođena blokatora. Nijedan od četiri
ne mijenja se u ovom gateu i nijedan nije sakriven statusom roditelja ili
paketa.

## Četiri izričite cjeloknjižne potvrde

1. Svih 19 jedinica ima točno pet schema-valjanih zapisa i pet podudarnih
   živih sidara. Ukupno je 95 zapisa, 95 sidara i 19 zasebnih jediničnih
   brojčanih/tiskovnih potvrda.
2. Provjereno je 1.166 dovoljno dugih zaštićenih nizova rubrika, alternativa i
   bilježaka nastavniku. Javni prikaz, javna navigacija i release AI izvoz imaju
   nula curenja; kolegijski prikaz sadrži svih 95 zaštićenih rubrika.
3. Oba oglašena čitateljska puta provjerena su prema živim preduvjetima svih
   19 ratificiranih kralježnica. Kanonski redoslijed 1–18 ostaje nepromijenjen.
4. Neisporučena obećanja nisu izbrisana. Jamovi put javno obećava samo 19
   podržanih mjerila, sedam vrijednosti ostavlja ograđenima, a čistu instalaciju
   vlasniku. Neovisna terminološka recenzija, puni objavljivi PDF svakoga
   dodatka i ponavljanje AI izlaza uživo nisu prikazani kao dovršeni.

## Puni blokirajući niz provjera

Na deklariranom izvoru prošli su inventar i njegove tri negativne probe,
generator rješenja, arhitektura procjene, putovi, tokeni, integritet rukopisa,
citati, podaci, sedam integritetnih negativnih proba, 17 widgetskih ugovora,
17 pariteta, sedam paritetnih negativnih proba, put PDF-omotača, release AI
izvoz, njegove tri negativne probe i naknadna validacija.

Dvije su opće provjere pale i ostaju blokatori:

- `scripts/check-figure-introductions.py` nalazi
  `chapters/16-regresija.qmd#fig-pravac`, gdje je odobreni `podsjetnik` između
  uvodne proze i slike. To je postojeći `H-P5-ROUTES-002`; vlasnik je
  `P6-FIGURES`.
- `scripts/check-concepts.py` nalazi svjež graf s 52 čvora i 662 veze naspram
  predanoga grafa s 52 čvora i 664 veze. Vlasnik je `P6-CONTINUITY`; gate ne
  regenerira datoteku.

Tri obvezne negativne probe tijeka rada izvedene su zasebno. Sve su vratile
izlaz 1 i imenovale točan ubrizgani kvar:

- `generic_packet_evidence`;
- `invalid_outside_ask_link`;
- `descoped_without_amendment`.

Četiri negativne probe arhitekture procjene također su zasebno odbile
`protected_export_field`, `assessed_code_production`,
`invalid_solution_record` i `protected_record_leak`. Negativne probe Dodataka
E–G nisu prihvaćene kao novi dokaz pojedinačnih ubrizganih kvarova jer njihove
pozitivne osnove već padaju na zastarjelim artefaktima; taj problem nije
maskiran povijesnim rezultatima.

## Razriješeno i odgođeno s vlasnikom

Razriješeno u smislu gate-provjere, bez nove izmjene izvora:

- kanonska knjiga handoffa nema nula nego dvije dostave za P5-VERIFY;
- četiri ranija prijenosa samo prema P5-ROUTES imaju dokazanu dispoziciju i
  završni rezultat u artefaktu P5-ROUTES;
- P5-ROUTES je potrošio svih 13 dostava, a ne 12;
- roditelji `R04`, `R23` i `R24` nisu zatvoreni agregiranjem;
- javni i zaštićeni prikaz potječu iz jednoga spremišta 95 zapisa;
- javno obećanje jamovi puta već je suženo i ne pripisuje čistu instalaciju.

Odgođeno s vlasnikom:

| ID | Kvar ili granica | Vlasnik |
|---|---|---|
| `B-P5V-C` | zastarjeli kataloški hash u artefaktu P5-C | `P6-DATA` |
| `B-P5V-E-CONVENTIONS` | zastarjeli hash `conventions.json` u artefaktu P5-E | `P6-CONTINUITY` |
| `B-P5V-E-GRAPH` | predani konceptni graf ima 664 veze, a svježi 662 | `P6-CONTINUITY` |
| `B-P5V-F` | zastarjeli izvorni hash P5-F nakon kasnije promjene konvencija | `P6-EVIDENCE` |
| `B-P5V-G` | zastarjeli P5-G artefakt nakon dodavanja rute rješenja | `P6-CONTINUITY` |
| `B-P5V-FIG16` | `podsjetnik` prekida neposredni uvod za `fig-pravac` | `P6-FIGURES` |
| `B-P5V-A-RAW` | čista provjera P5-A traži tri dokumentirana, ali nepredana sirova ulaza | `P7-CLEAN-BUILD` |
| `B-P5V-EOL` | ugrađeni bajtni sažeci ovise o pretvorbi LF/CRLF; generator rješenja pada u CRLF checkoutu i prolazi nad kanonskim Gitovim blobovima | `P7-CLEAN-BUILD` |
| `B-P5V-JAMOVI` | čista instalacija jamovi 2.7.30.0 / jmv 2.7.7 nije izvedena | Luka Šikić; postojeća javna granica ostaje na 19/7 |

## Dispozicija gatea

P5-VERIFY je dovršio vlastiti posao provjere i izvještavanja: svih 27
preduvjeta dobilo je vlastiti redak, jedno izvorno stanje, stvarni rezultat i
vlasnika svakoga odstupanja. Pet pojedinačnih kvarova u četiri nevaljana
paketna dokaza i četiri dodatne granice ne proglašavaju se popravljenima. Gate
ne mijenja njihove pakete ni
stavke i ne tvrdi da je Faza 5 bez blokatora; njihovi su učinci predani točnim
kasnijim vlasnicima.

Nije preuzet nijedan paket Faze 6. Nije izveden push, merge, tag, arhiviranje,
postavljanje ni objava.
