# P6-CONTINUITY — završni audit kontinuiteta knjige

**Datum:** 26. kolovoza 2026.

**Paket:** `P6-CONTINUITY`

**Ugovor:** `whole_book_review`

Paket provjerava strukturu, nazivlje, preduvjete, niti i prijelaze na konačnom
materijalnom stanju. Ne mijenja prozu poglavlja i ne preuzima rad paketa
`P6-EVIDENCE`, `P6-FIGURES`, `P6-DATA`, `P6-STYLE`, `P6-PANELS`, `P6-ARC` ili
`P7-CLEAN-BUILD`. Jedine materijalne promjene izvan kontrolnih datoteka jesu
omeđena pomirenja zajedničkoga registra pojmova i triju generiranih ruta koje
su ovom paketu predane poimence.

## Jedno deklarirano izvorno stanje

Cijeli audit i oba neovisna čitanja odnose se na:

`p6-continuity-state:sha256-e65f9fc6b56fc6ea085ff7aed37d3419979ecd01d7163f4fc5fd062d3f8e93da`.

Stanje polazi od commita
`b12291f4cac1ee0b48ebaf72607428a69149a0c0`. Sažetak je izračunan iz
normaliziranih UTF-8 sadržaja, uz CRLF i CR svedene na LF, kao SHA-256
sortiranih zapisa `putanja NUL SHA-256 LF`. Time dokaz nije ovisan o lokalnoj
pretvorbi završetaka redaka. Pet skupina ulaza jesu:

| Skupina | Datoteke | SHA-256 skupine |
|---|---:|---|
| sva poglavlja | 19 | `6bd6a30e76a5741e099d38b7253764e495516f54a4ca729c9589ce4ae7862911` |
| svi dodaci A–G | 7 | `e56154791c9c3cad8394641f8ba6c2da1574f9505a7b9dcbf1ebcd06940069d9` |
| kanonski zapisi rješenja | 95 | `0b7dbda3d26b96ad04301bd391d891cb7687a143315f66ec25af4d3527f857b7` |
| konvencije, kralježnice, konceptni ledger i dvije sheme | 5 | `5f456e28b68c1e86ae5e1b44984c675f0854694fa21e7416c4131620116bb602` |
| rute, javni prikazi, inventar, widgeti i Quarto/STYLE ugovori | 12 | `5a89fc87309cde3e3e35555abcf81f49c98b779175946011df0b9f1a9556de34` |

Kontrolne datoteke i ovo izvješće nisu ulaz u vlastiti dokaz. Nema vanjskoga
ulaza specifičnog za ovaj paket.

## Audit dolaznih handoffa

Kanonski ledger ima četiri, a ne tri, obvezne dostave `before_start`:

| Handoff | Zasebna obveza | Dispozicija |
|---|---|---|
| `H-G-A2D-004` | cijela H10 ljestvica osumnjičenoga koda | potrošen; svih 19 jedinica ima artefakt ili poimence obrazloženu iznimku |
| `H-P5-VERIFY-002` | zastarjeli hash konvencija u P5-E | potrošen; zaseban `check-appendix-e.py` prolazi |
| `H-P5-VERIFY-003` | neovisno zastarjeli konceptni graf | potrošen; zaseban `check-concepts.py` prolazi s 52 čvora i 662 brida |
| `H-P5-VERIFY-005` | zastarjeli inventarni trag P5-G | potrošen; zaseban `check-appendix-g.py` prolazi za četiri teme i četiri prve uporabe |

Tri dostave `before_close` također ostaju zasebne:

| Handoff | Zasebna obveza | Dispozicija |
|---|---|---|
| `H-G-A2B-FINALE-001` | završni audit izmijenjene granice nove metode | potrošen; Poglavlje 18 izričito prenosi raniji postupak „bez nove metode” i ne stvara prednju ovisnost |
| `H-P2-TERMS-001` | zatvaranje samo `R36-BOOK-new-cluster` nakon audita cijele knjige | potrošen; nula živih divergencija i zaseban test proze, slika, zadataka, definicija i obaju javnih rječnika |
| `H-WB-C06-002` | uvjetna definicija ograničenja raspona | potrošen; ledger je pomiren s prihvaćenim `#def-ogranicenje-raspona`, a graf i terminološke projekcije regenerirani |

Nije dirnuta nijedna dostava za `P6-DATA`, `P6-EVIDENCE`, `P6-FIGURES` ili
`P7-CLEAN-BUILD`. Status P5-VERIFY nije upotrijebljen kao dokaz popravka.

## Tri P5-VERIFY invalida

Tri su kvara provedena kao tri odvojena testa:

1. `B-P5V-E-CONVENTIONS`: `build-terminology-views.py` osvježio je
   `config/appendix-e-terminology-route.json`; `check-appendix-e.py` prolazi za
   52 pojma, 662 brida, 12 uputnica, 3 namjerna odstupanja i 4 pravila značenja.
2. `B-P5V-E-GRAPH`: `R/build-concept-graph.R` ponovno je izgradio
   `data/concept-graph.json`; `check-concepts.py` zasebno potvrđuje
   `graph_fresh=true`, 52 čvora i 662 brida.
3. `B-P5V-G`: `build-appendix-g-route.py` osvježio je samo konfiguracijsku
   rutu; `check-appendix-g.py` zasebno potvrđuje točno 4 D10 teme, 4 prve
   uporabe, 39 stranica i 7 dodataka.

Jedan prolaz nije upotrijebljen kao dokaz za drugi. P5-E i P5-G nisu
reklasificirani, a P5-F nije regeneriran: njegov zaseban zastarjeli dokaz ostaje
kod vlasnika `P6-EVIDENCE`.

## Sačuvane arhitekturne invarijante

| Invarijanta | Konačni dokaz | Rezultat |
|---|---|---|
| `19/7/39/1/17/17/4` | `check-book-inventory.py`; `check-book-architecture.py`; živi `pathway-routes.json#architecture.after_solution_route` | prolaz |
| dvije čitateljske rute | semantički audit `kriticko-citateljski` i `analiticki` nad živim kralježnicama | prolaz |
| 19 ratificiranih kralježnica | `check-chapter-spines.py`, 19/19; 17 preduvjeta za Poglavlje 18 | prolaz |
| 95 zapisa iz jednoga izvora | `check-assessment-architecture.py`, 5 × 19 zapisa i 95 živih sidara | prolaz |
| bez javnoga curenja | isti test: 1.166 zaštićenih nizova, 0 curenja u javni izvoz ili navigaciju | prolaz |
| puni zajednički kostur | checkout-local `structure_scan.R`, svih 19 jedinica, 4/4 razine zadataka, bez placeholdera | prolaz |

`_quarto.yml` i redoslijed poglavlja nisu promijenjeni. Semantički audit obaju
putova prolazi svih 18 numeriranih jedinica i svaki živi preduvjet. Puni
`check-pathways.py` i dalje pada samo na već predanom LF/CRLF hashu generirane
rute rješenja; to je postojeći `H-P5-VERIFY-007` za `P7-CLEAN-BUILD`, a ne
semantički kvar rute i ovdje nije popravljen ni potrošen.

## Matrica devet zasebnih stavki

Svaka stavka ima vlastiti test i vlastiti dokaz. Nijedan roditelj nije zatvoren
zbrajanjem prolaza djece.

| Stavka | Vlastiti izvorni dokaz | Vlastiti test i dispozicija |
|---|---|---|
| `R10-LIFECYCLE-distribution` | biljka `chapters/01-zasto-statistika.qmd:235-252`; razvoj po dijelovima; žetva `chapters/18-vase-prvo-istrazivanje.qmd:796-801` | devet zasebnih redaka niže ima biljku, razvoj i žetvu; **prihvaćeno** |
| `R12-SAMPLING-vs-test` | `chapters/08-uzorkovanje.qmd:1014-1061`; `chapters/16-regresija.qmd:1183-1234`; `chapters/17-doba-algoritama.qmd:209-234,767-782` | svaki tekst imenuje vlastito jamstvo i niječe drugo; **prihvaćeno** |
| `R12-POLL-recurrence` | `chapters/02-mjerenje-i-dizajn.qmd:414-446`; `03:160-193`; `08:1014-1028`; `13:246-250`; `16:1294-1313` | funkcije se spiralno razvijaju, ali `02:429` i `03:167` oba zvuče kao prvo uvođenje, dok `08:1014` podrijetlo pripisuje samo Poglavlju 3; **ostaje ratificirano**, zaseban `F-P6C-V02` za `P6-STYLE` i završni `P6-ARC` pregled |
| `R14-BOOK-causal-thread` | `chapters/02-mjerenje-i-dizajn.qmd:314-345`; `06:712-726,1122-1138`; `08:1033-1061`; `16:515-604,1157-1257`; `17:115-119,576-604` | redoslijed odvaja povezanost, doseg, prilagodbu, identifikaciju, predviđanje i povratnu spregu; **prihvaćeno** |
| `R17-REPORT-thread` | `chapters/04-sazimanje-podataka.qmd:1145-1163`; `09:761-762,934-941`; `11:259-286,819-825`; `16:1433-1453`; `18:484-533,728-755` | svih pet mjesta jača proizvodnju ili audit; Poglavlje 18 izričito primjenjuje isti standard na vlastiti i asistentov izvještaj; **prihvaćeno** |
| `R23-BOOK-suspect-code-ladder` | 19 callout sidara i 19 sidara `revizija-modela`, plus `assessment_architecture.h10_boundary` | 8 stvarnih artefakata čitanja koda + 11 poimence obrazloženih stupanjski prikladnih iznimki; svih 95 zapisa kaže `code_production_assessed=false`; **prihvaćeno** |
| `R24-BOOK-AppendixF-references` | 19 različitih `callout-model` blokova; `chapters/18-vase-prvo-istrazivanje.qmd:324,673-706`; `dodaci/f-ai-protokol.qmd:121-160` | kompetencija raste, 19/19 blokova sadržajno je različito i potpuni protokol nije umnožen, ali izričita poveznica prema Dodatku F postoji tek u Poglavlju 18; **ostaje ratificirano**, zaseban `F-P6C-A01` |
| `R27-BOOK-part-bridges` | `chapters/03-kako-brojke-zavode.qmd:630-707`; `06:1095-1158`; `09:892-931`; `12:654-721`; `17:734-788` | svih pet mostova nosi potrebne tri funkcije, ali prvi je tipografski podređen razrađenom primjeru na `03:630`; **ostaje ratificirano**, zaseban `F-P6C-V01` |
| `R36-BOOK-new-cluster` | živi `terminology_registry`, 52 definicije, 19 poglavlja, figure/zadatci i oba rječnička prikaza | `check-terminology.py`: 166 oblika kralježnice, 12 uputnica, 3 odstupanja, 4 pravila, 52 definicije, 0 divergencija; `check-appendix-e.py` prolazi; **prihvaćeno** |

Roditelji `R10`, `R12`, `R14`, `R17`, `R23`, `R24`, `R27` i `R36` ostaju u
svojim zatečenim stanjima. Prolaz ove stavke nije dokaz za drugi potomak niti
za roditelja.

## Devet faza životnoga ciklusa

| Faza | Biljka | Razvoj | Žetva |
|---|---|---|---|
| pitanje | `01:237-244` | `02:451-483`, dosezi dizajna i vrste pitanja | `18:174-212`, pitanje i šest dimenzija prije podataka |
| pribavljanje | `01:245` | `08:891-1005`, okvir, uključivanje, pokrivenost i odaziv | `18:292-297`, zaseban zapis pribavljanja ili prikupljanja |
| provjera | `01:246` | `04:273-370`, jedinica, ključ, broj redaka i nedostajanje | `18:299-341`, zaključavanje i provjera analitičke tablice |
| priprema | `01:247` | `04:311-370`, spajanje, filtri i trag transformacija | `18:299-312`, poimence zabilježene promjene prije modela |
| istraživanje | `01:248` | `05:251-688`, gramatika prikaza, ljestvica i male višestruke plohe | `18:352-428`, opis i graf prije modela |
| modeliranje | `01:249` | `16:289-658`, procjenjivana veličina, prilagodba i interakcija | `18:431-505`, primarni model vezan uz pitanje |
| vrednovanje | `01:250` | `09:584-744` i `17:209-234`, preciznost/pokrivenost i odvojena prediktivna provjera | `18:492-505,611-629`, osjetljivost i izričite granice vrednovanja |
| komunikacija | `01:251` | `04:1145-1163`, `09:934-941`, `16:1433-1453`, poštena rečenica kroz procjenu, interval i uvjet | `18:507-566,728-755`, vlastiti izvještaj i audit asistentova nacrta |
| praćenje/nadzor | `01:239-252` | `17:546-589,785-801`, povratna sprega, prigovor i nadzor nakon ugradnje | `18:796-810`, nadzor kao dio paketa i izričita nepostavljenost sustava |

Nijedna faza ne živi samo u registru. Paket nije dodao empirijsku tvrdnju,
broj ni citat.

## H10 i ljestvica osumnjičenoga koda

Svaki redak ima točno mjesto posađene pogreške i završne revizije. „Iznimka”
znači da je statistička dijagnoza namjerno čitljiva bez koda u stupnju u kojem
bi kod bio zabranjen ili bi preusmjerio ocjenu sa prosudbe na sintaksu.

| Jedinica | `callout-greska` / revizija | Dispozicija |
|---|---|---|
| 00 | `00:150` / `00:216` | iznimka: provjerljiv trag nije zamjena za provjeru; predgovor nema vidljiv kod |
| 01 | `01:737` / `01:855` | iznimka: audit brojnik–nazivnik i granica tvrdnje; H10 Dijela I |
| 02 | `02:843` / `02:1090` | iznimka: dizajn, mjerenje i uzročni skok; H10 Dijela I |
| 03 | `03:512` / `03:755` | iznimka: službeni broj i operativna definicija; H10 Dijela I |
| 04 | `04:1064` / `04:1235` | iznimka: izlaz otkriva nepotpun ključ spajanja; procjenjuje se dijagnoza transformacije |
| 05 | `05:1008` / `05:1172` | kod: čitanje parametra širine i nenajavljena površina |
| 06 | `06:1037` / `06:1249` | kod: filtar podskupine i nedopuštena generalizacija |
| 07 | `07:839` / `07:952` | kod: čitanje simulacijskoga mehanizma i neopravdana neovisnost |
| 08 | `08:1093` / `08:1241` | iznimka: standardna pogreška nije raspršenost pojedinaca |
| 09 | `09:795` / `09:1026` | kod: bootstrap trag i pogrešno tumačenje fiksnog intervala |
| 10 | `10:842` / `10:972` | kod: permutacijski račun i posteriorno tumačenje p-vrijednosti |
| 11 | `11:750` / `11:882` | kod: opaženi učinak kružno vraćen u post hoc snagu |
| 12 | `12:564` / `12:784` | iznimka: predregistracija nije jamstvo valjanosti; razvoj audita odluka |
| 13 | `13:795` / `13:911` | iznimka: mala p-vrijednost nije velika povezanost; čitanje tablice/reziduala |
| 14 | `14:857` / `14:966` | iznimka: podskupna neznačajnost nije odsutnost povezanosti |
| 15 | `15:698` / `15:812` | kod: neispravljeni parni testovi i obiteljska stopa pogreške |
| 16 | `16:1372` / `16:1520` | kod: trening-pristajanje predstavljeno kao provjera novih jedinica |
| 17 | `17:641` / `17:839` | iznimka: ispitna točnost prema pogrešivoj oznaci nije valjanost konstrukta |
| 18 | `18:744` / `18:876` | iznimka: interval koji obuhvaća nulu nije dokaz odsutnosti povezanosti; završni audit izvještaja |

Rezultat je 8 artefakata s čitanjem koda i 11 evidentiranih iznimki, bez
nepraćene praznine. Sva su 19 bloka `callout-model` različita; puni protokol
nije prepisan u poglavlja.

## Prijelazi, preduvjeti i finale

Pet završetaka dijelova imaju zasebne mostove. Posebno:

- Dio I završava izvedivim protokolom i predaje ključ, transformaciju i sažetak
  Poglavlju 4 (`03:693-707`).
- Dio II dopušta opis i povezanost u presjeku, niječe individualni, uzročni i
  budući doseg te predaje uzorkovanje i neizvjesnost (`06:1122-1138`).
- Dio III dopušta omeđenu procjenu, niječe nedopuštena čitanja i izričito
  razlikuje populacijsko uzorkovanje od prediktivne podjele (`09:914-931`).
- Dio IV dopušta reformiranu prosudbu, niječe uzrok/predviđanje/prijenos izvan
  dizajna i predaje modele Dijelu V (`12:654-663,717-721`).
- Dio V dopušta audit sustava i odluke, niječe nedokazane doseege te predaje
  prag, teret pogreške, nadzor i prigovor finalu (`17:734-788`).

Poglavlje 18 zadržava svih 17 ranijih poglavlja kao preduvjete. Njegova glavna
studija ostaje objasnidbena (`18:484-505`), a empirijski prijenos izričito
ponavlja isti redoslijed „bez nove metode” (`18:575-582`). Jedini novi
definicijski objekt jest `paket dokaza`; to je spremnik ranije naučenih
postupaka, a ne nova statistička tehnika. Nijedna tehnika s popisa izvan opsega
nije uvedena, nijedna nije ostala bez lokalnoga objašnjenja i nijedna ne traži
znanje koje ranija ratificirana kralježnica nije trebala dati.

## Terminološko pomirenje

`R36-BOOK-new-cluster` nije zatvoren iz stanja samoga registra. Zasebni audit
proze, slika, zadataka, definicija i obaju rječnička prikaza koristi živi
`terminology_registry`, sva 52 definicijska sidra i nulti
`live_divergences`. `check-terminology.py` prolazi s 166 oblika kralježnice,
12 uputnica, 3 namjerna odstupanja, 4 pravila značenja i 52 definicije.

`H-WB-C06-002` zatvoren je vlastitim semantičkim testom. Kanonska definicija
ograničenja raspona sada kaže da pojava **može** oslabiti izmjerenu povezanost,
ali da smjer ovisi o obliku odnosa i pravilu odabira. Time odgovara
`chapters/06-povezanost.qmd:485-505`, bez mijenjanja prihvaćenoga
definicijskog bloka ili korisnoga približno linearnog primjera. Tek su zatim
regenerirani graf i terminološke projekcije.

## Svježi neovisni čitatelji

Završni glasovni kritičar i kritičar cjeline čitali su neovisno isti deklarirani
izvorni state. Njihovi se nalazi ne spajaju s determinističkim provjerama.

Kritičar cjeline ocijenio je kumulativnu gradnju `5/5`, redoslijed i
preduvjete `5/5`, a izostanak suvišnoga ponavljanja `4/5`: nula fatalnih,
nula velikih i jedan manji nalaz. Osam vlastitih stavki ocijenio je prolaznima;
za `R36-BOOK-new-cluster` izričito nije glumio terminološku ekspertizu, a za
`R24-BOOK-AppendixF-references` našao je da progresija kompetencije postoji bez
umnožavanja protokola, ali da prije Poglavlja 18 nema izričite poveznice prema
Dodatku F. Taj nalaz ostaje zasebno otvoren kao `F-P6C-A01`.

Glasovni kritičar ocijenio je konzistentnost glasa `4/5`, a ujednačenost
registra `3/5`: nula fatalnih, četiri velika i četiri manja nalaza. Kritičar je
potvrdio prepoznatljiv glas iskusnoga predavača, ujednačene definicije i
namjerno opravdano prvo lice množine u finalu. Veliki nalazi ostaju odvojeni:
`F-P6C-V01` za hijerarhiju prve granice dijela, `F-P6C-V02` za dvostruko
podrijetlo anketne kartice, `F-P6C-V03` za formulaične početke svih AI-okvira i
`F-P6C-V04` za implementacijski registar u čitateljskom Dodatku F. Manji
`F-P6C-V05`–`V08` također su evidentirani pojedinačno.

Panel se ne preglasava agregacijom. Arc-ocjena da je funkcionalna rekurencija
anketne kartice dobra ne briše glasovni nalaz o njezinu nejasnom podrijetlu;
prolaz sadržaja pet mostova ne briše hijerarhiju prvoga. Ovaj paket po
checkout-local continuity ugovoru ne smije mijenjati prozu. Zato su svi veliki
nalazi i jedan manji kvar točne stavke odgođeni s vlasnikom prema `P6-STYLE`, a
`P6-ARC` mora ih ponovno provjeriti na stanju nakon promjena. Oni moraju biti
razriješeni prije nizvodnoga release proofa; prihvaćanje ovoga paketa prihvaća
izvršen audit i izvješće, ne prihvaća te kvarove kao popravljene.

## Nalazi i dispozicije

### Razriješeno u ovom paketu

| ID | Nalaz | Vlasnik | Dispozicija i dokaz |
|---|---|---|---|
| `F-P6C-001` | kanonski ledger ima četvrti `before_start` H10 handoff koji početni sažetak nije naveo | P6-CONTINUITY | razriješeno prije audita; `H-G-A2D-004` potrošen odvojeno |
| `F-P6C-002` | zastarjeli P5-E hash konvencija | P6-CONTINUITY | razriješeno; `APPENDIX_E_CHECK_OK` |
| `F-P6C-003` | zasebno zastarjeli konceptni graf 664/662 | P6-CONTINUITY | razriješeno; svježi graf 52/662 i `CONCEPT_INTEGRITY_OK` |
| `F-P6C-004` | zastarjeli P5-G trag inventara | P6-CONTINUITY | razriješeno; `APPENDIX_G_CHECK_OK`, 4 teme/4 rute/39 stranica |
| `F-P6C-005` | bezuvjetna ledger-definicija ograničenja raspona | P6-CONTINUITY | razriješeno uvjetnom definicijom, zatim graf/terminologija/P5-E zasebno provjereni |
| `F-P6C-006` | H10 strand nije imao završni popis artefakata i iznimki | P6-CONTINUITY | razriješeno matricom 19/19: 8 code-reading + 11 evidentiranih iznimki |

### Odgođeni nalazi svježih čitatelja s vlasnikom

| ID | Ozbiljnost | Točno mjesto i nalaz | Vlasnik i dispozicija |
|---|---|---|---|
| `F-P6C-V01` | veliki | `chapters/03-kako-brojke-zavode.qmd:558,600,630`: prva granica dijela ostaje `###` unutar razrađenoga primjera, za razliku od ostale četiri top-level granice | `P6-STYLE` popravlja hijerarhiju ako urednička provjera potvrdi; `P6-ARC` mora ponovno provjeriti; `R27-BOOK-part-bridges` ostaje ratificiran |
| `F-P6C-V02` | veliki | `chapters/02-mjerenje-i-dizajn.qmd:429-448`, `03:167-194`, `08:1014-1028`: dvije susjedne početne kartice i upućivanje samo na Poglavlje 3 zamagljuju jedno podrijetlo | `P6-STYLE` usklađuje podrijetlo bez gubitka spiralnog povratka; `P6-ARC` ponovno provjerava; `R12-POLL-recurrence` ostaje ratificiran |
| `F-P6C-V03` | veliki | početci svih 19 AI-okvira (`00:140`, `01:725`, `02:822`, `03:500`, `04:1051`, `05:992`, `06:1013`, `07:816`, `08:1080`, `09:782`, `10:827`, `11:737`, `12:544`, `13:781`, `14:845`, `15:685`, `16:1352`, `17:629`, `18:729`): svih 19 počinje subjektom „Asistent“, a 16/19 formulom „Asistent može“ | `P6-STYLE` mijenja retoričku strukturu, ne samo glagol; `P6-ARC` ponovno provjerava; H10 matrica i sadržajna različitost ostaju zaseban prolaz |
| `F-P6C-V04` | veliki | `dodaci/f-ai-protokol.qmd:130-150`: 95 kanonskih zadataka, `#ex-` sidra, otisak prompta, konfiguracijska putanja i čuvar zvuče kao implementacijsko izvješće | `P6-STYLE` zadržava čitateljski učinak, a implementacijski dokaz premješta u kontrolni izvještaj; `P6-ARC` ponovno provjerava |
| `F-P6C-V05` | manji | `chapters/02-mjerenje-i-dizajn.qmd:105-153,465-497` i `13-kategoricki-podaci.qmd:189-211,688-711`: zbijene konstrukcije „nije/ne… nego“ prelaze iz autorske značajke u maniru | `P6-STYLE`, zasebna ljudska dispozicija |
| `F-P6C-V06` | manji | `05:409`, `07:371`, `10:332`, `11:452`, `13:321`, `14:300`, `15:226`, `16:664`: osam puta „Sljedeći prikaz“; `10:871`, `14:869`, `15:720`: tri srodna otvaranja razrađenog primjera | `P6-STYLE`, zasebna ljudska dispozicija |
| `F-P6C-V07` | manji | granice dijelova `03:630-690`, `06:1095-1178`, `09:892-959`, `12:654-720`, `17:734-788`: prva četiri mosta ponavljaju isti površinski slijed | `P6-STYLE` varira mostove bez uklanjanja ratificiranih šest dimenzija i pitanja |
| `F-P6C-V08` | manji | `chapters/04-sazimanje-podataka.qmd:273-461`: pet ugniježđenih cjelina i 974 riječi pomiču registar prema operativnom priručniku | `P6-STYLE`, zasebna ljudska dispozicija; podudara se s lint kandidatima R06–R09, ali ih ne briše |
| `F-P6C-A01` | manji | `chapters/04-sazimanje-podataka.qmd:1058`, `09-procjena.qmd:790`, `17-doba-algoritama.qmd:628`, `18-vase-prvo-istrazivanje.qmd:324,675`, `dodaci/f-ai-protokol.qmd:50`: kompetencija napreduje, ali Dodatak F imenom se pojavljuje tek u Poglavlju 18 | `P6-STYLE` dodaje rijetke usidrene poveznice pri novim razinama kompetencije; `P6-ARC` ponovno provjerava; `R24-BOOK-AppendixF-references` ostaje ratificiran |

### Deterministički kandidati za kasniji urednički paket

`structure_lint.R` je prijavio 16 kandidata. Alat ih izričito ne popravlja
automatski. P6-CONTINUITY nema ovlast mijenjati prozu; svaki kandidat zato
ostaje zaseban u `H-P6-CONTINUITY-001` za ljudski `P6-STYLE` pregled. Svježi
glasovni nalaz promaknuo je R04/R05 u veliki `F-P6C-V01`, a R06–R09 podupiru
manji `F-P6C-V08`; izvorni kandidati ipak ostaju zasebno evidentirani:

| ID | Točno mjesto | Kandidat | Dispozicija |
|---|---|---|---|
| `F-P6C-R01` | `00-predgovor`, „Granice i putovi čitanja” | 2 ugniježđena pododjeljka | odgođeno `P6-STYLE` |
| `F-P6C-R02` | `01-zasto-statistika`, poglavlje | omjer veličina 3,8× | odgođeno `P6-STYLE` |
| `F-P6C-R03` | `01-zasto-statistika`, „Životni ciklus podataka” | 1 ugniježđen pododjeljak | odgođeno `P6-STYLE` |
| `F-P6C-R04` | `03-kako-brojke-zavode`, „Razrađeni primjer” | 2 ugniježđena pododjeljka | odgođeno `P6-STYLE` |
| `F-P6C-R05` | isto mjesto | 20 odlomaka / 769 riječi | odgođeno `P6-STYLE` |
| `F-P6C-R06` | `04-sazimanje-podataka`, poglavlje | evenness 0,62 | odgođeno `P6-STYLE` |
| `F-P6C-R07` | isto poglavlje | omjer veličina 4,4× | odgođeno `P6-STYLE` |
| `F-P6C-R08` | `04`, „Od izvora do sažetka” | 5 ugniježđenih pododjeljaka | odgođeno `P6-STYLE` |
| `F-P6C-R09` | isto mjesto | 16 odlomaka / 974 riječi | odgođeno `P6-STYLE` |
| `F-P6C-R10` | `09-procjena`, poglavlje | omjer veličina 3,1× | odgođeno `P6-STYLE` |
| `F-P6C-R11` | `09`, granica Dijela III | coda 228 prema medijanu 452 riječi | odgođeno `P6-STYLE` |
| `F-P6C-R12` | `09`, „Interakcija — Hvatač intervala” | 1 ugniježđen pododjeljak | odgođeno `P6-STYLE` |
| `F-P6C-R13` | `09`, „Bootstrap kao vlastiti izum” | 1 ugniježđen pododjeljak | odgođeno `P6-STYLE` |
| `F-P6C-R14` | `10-logika-testiranja`, poglavlje | granični omjer veličina 3,0× | odgođeno `P6-STYLE` |
| `F-P6C-R15` | `10`, „Kako se gradi svijet bez učinka” | 12 odlomaka / 540 riječi | odgođeno `P6-STYLE` |
| `F-P6C-R16` | `10`, „Dvije vrste pogreške” | 1 ugniježđen pododjeljak | odgođeno `P6-STYLE` |

### Već odgođeno drugom vlasniku, bez promjene stanja

| Nalaz | Vlasnik | Ovdje učinjeno |
|---|---|---|
| zastarjeli P5-F hash konvencija | `P6-EVIDENCE`, `H-P5-VERIFY-004` | samo potvrđeno da `check-appendix-f.py` i dalje pada na točno tom hashu; bez popravka i bez potrošnje |
| `rjesenja.qmd` nije deklarirani consumer paketa `populacija_medija` | `P6-DATA`, `H-P6-CONTINUITY-008` | novi zasebni kvar punoga laddera; nije spojen sa zastarjelim P5-C artefaktom ni LF/CRLF kvarom |
| čista ponovljivost vanjskih P5-A ulaza | `P7-CLEAN-BUILD`, `H-P5-VERIFY-006` | nije dirnuto |
| LF/CRLF ovisnost generiranih hashova, uključujući `rjesenja.qmd` | `P7-CLEAN-BUILD`, `H-P5-VERIFY-007` | semantika ruta provjerena odvojeno; infrastrukturni kvar nije popravljen ni potrošen |
| uvod slike `fig-pravac` | `P6-FIGURES`, `H-P5-ROUTES-002` | nije dirnuto |

## Završni testovi

Pozitivne provjere konačnoga stanja:

- `BOOK_ARCHITECTURE_OK`;
- `BOOK_INVENTORY_OK pages=39 chapters=19 appendices=7 solutions=1`;
- `CHAPTER_SPINES_OK`, 19/19 ratificirano;
- `ASSESSMENT_ARCHITECTURE_OK`, 95 zapisa, 95 sidara, nula javnih curenja;
- `TERMINOLOGY_OK`, 0 divergencija;
- `CONCEPT_INTEGRITY_OK`, 52 čvora, 662 brida, svjež graf;
- `APPENDIX_E_CHECK_OK`;
- `APPENDIX_G_CHECK_OK`;
- checkout-local `structure_scan.R`, 19/19 strukturno potpune jedinice;
- semantički audit putova, 2 rute, 18 numeriranih kralježnica, 0 povreda
  preduvjeta;
- dva svježa, neovisna čitatelja na deklariranom stanju.

Puni blokirajući ladder izveden je na istom stanju. Prolaze inventar i tri
inventarne negativne probe, arhitektura procjene, tokeni, integritet rukopisa,
citati, koncepti, integritet podataka, sedam integritetnih negativnih proba,
svih 17 widgetskih ugovora, 17 pariteta, sedam paritetnih negativnih proba,
arhitektura knjige, svih 19 kralježnica, terminologija, Dodatci A, B, D, E i G,
četiri probe PDF-omotača, release AI izvoz, njegove tri negativne probe i
naknadna validacija. Pet zasebnih kvarova ostaje vidljivo u šest naredbi:

| Naredba | Rezultat | Zaseban vlasnik |
|---|---|---|
| `build-solution-routes.py --check`; `check-pathways.py` | izlaz 1: `rjesenja.qmd` nije čista bajtna projekcija u CRLF checkoutu | `P7-CLEAN-BUILD`, postojeći `H-P5-VERIFY-007` |
| `check-figure-introductions.py` | izlaz 1: `chapters/16-regresija.qmd#fig-pravac` | `P6-FIGURES`, postojeći `H-P5-ROUTES-002` |
| `check-katalog.py` | izlaz 1: `populacija_medija` nema deklariran `rjesenja.qmd` consumer | `P6-DATA`, novi `H-P6-CONTINUITY-008` |
| `check-appendix-c.py` | izlaz 1: zastarjeli kataloški zbroj | `P6-DATA`, postojeći `H-P5-VERIFY-001` |
| `check-appendix-f.py` | izlaz 1: zastarjeli hash konvencija | `P6-EVIDENCE`, postojeći `H-P5-VERIFY-004` |

Jedan prolaz ni kvar nije upotrijebljen kao zamjena za drugi. Posebno, novi
katalogski consumer nije pripisan zastarjelom artefaktu Dodatka C, a dva pada
rute jesu dvije naredbe za isti već predani LF/CRLF kvar.

Završni `check-review-workflow.R` prolazi nakon istodobnoga closeouta registra,
handoff-ledgera i dashboarda. Tri njegove negativne fixture provjere
`generic_packet_evidence`, `invalid_outside_ask_link` i
`descoped_without_amendment` vraćaju izlaz 1 i imenuju točno ubrizgani kvar.

## Granica closeouta

Paket prihvaća šest vlastitih stavki na šest zasebnih testova. Stavke
`R12-POLL-recurrence`, `R24-BOOK-AppendixF-references` i
`R27-BOOK-part-bridges` ostaju ratificirane zbog triju odvojenih nalaza i ne
zatvaraju se zbrajanjem drugih prolaza. Ne mijenja se status nijednoga roditelja
agregacijom. Sam P6-CONTINUITY može biti prihvaćen samo kao dovršen audit i
izvješće s odgođenim nalazima i vlasnicima; to nije dokaz da su kvarovi
popravljeni. `P6-EVIDENCE` ostaje sljedeći dopušteni paket i nije claimed.
Nisu provedeni push, merge, tag, archive, deploy niti publish.
