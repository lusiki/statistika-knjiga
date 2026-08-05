# P2-VERIFY — provjera dosljednosti arhitekture faze 2

**Paket:** `P2-VERIFY`

**Datum:** 5. kolovoza 2026.

**Ugovor:** `review_gate`

**Deklarirano izvorno stanje:** `commit:fd4564c3d2890c80f5f865f6b386f34b29f8feea`,
grana `revision/comprehensive-review`. Cijeli je izvještaj vezan uz to jedno
stanje i nijedna tvrdnja u njemu nije uzeta iz ranijega.

## Dolazne isporuke

**Nijedna isporuka ne cilja `P2-VERIFY`.** Cijeli je ledger prosljeđivanja
pročitan prije prve izmjene i to se ovdje bilježi izričito: nije bilo dolazne
obveze koju bi trebalo potvrditi ili potrošiti, pa nijedna nije ni potrošena.
Ovaj paket ne troši ništa što cilja drugi paket.

## Ishod gatea, izrečen bez ublažavanja

Gate **prolazi vlastite izlazne testove** i **ne može potvrditi jednu klauzulu
izlaznoga uvjeta faze 2 iz ratificiranoga plana**. To dvoje nije isto i ovdje se
namjerno ne miješa.

Klauzula koja nije ispunjena glasi „R04 is closed". Ona je u fazi 2
**strukturno neispunjiva**, po vlastitom ustroju registra, a ne zbog propuštenoga
posla. To je zabilježeno kao neusklađenost, nije zaobiđeno agregacijom i nije
riješeno prekrajanjem uvjeta.

## `R04` — točan popis otvorene djece

`R04` ima 21 obveznu djecu. Sedamnaest ih je `accepted`. **Četvero je otvoreno**
i nijedno od njih ovaj paket ne može zatvoriti.

| Dijete | Status | Vlasnik zatvaranja | Faza | Zašto je otvoreno |
|---|---|---|---|---|
| `R04-ARCH-macro-order` | `ratified` | `P5-ROUTES` | 5 | Redoslijed u `_quarto.yml` jest nepromijenjen i provjeren, ali test traži i da su „oba puta točna". Ta dva puta ne postoje: predgovor ih ne objavljuje. `P2-DOCS` ju je zato namjerno ostavio otvorenom. |
| `R04-C11-fixed-order` | `ratified` | `WC-C11` | 4, val C | Traži vraćanje kanonskoga redoslijeda sedam dijelova u poglavlju 11, dakle izmjenu proze poglavlja. |
| `R04-ROUTES-two-track-map` | `ratified` | `P5-ROUTES` | 5 | Objava dvaju putova čitanja, uz preduvjete koji uključuju poglavlje 13 prije 17 i cijelu knjigu prije 18. |
| `R04-C18-whole-prerequisites` | `ratified` | `WE-C18` i `P5-ROUTES` | 4 i 5 | Registarska je polovica živa i strojno provjerena, ali `.chapter-meta` redak poglavlja 18 još imenuje uži popis, a nijedan put nije objavljen. |

Dvoje ih traži izmjenu proze poglavlja, dvoje objavu putova. Ni jedno ni drugo
nije posao faze 2, u kojoj se po ratificiranom planu uređuju registri i
upravljajući dokumenti, a nikada proza poglavlja.

**Ispunjen dio uvjeta i odgođeni dio, izrečeni odvojeno.** Od pet klauzula
izlaznoga uvjeta faze 2:

| Klauzula | Ishod |
|---|---|
| „R04 is closed" | **nije ispunjena**, strukturno odgođena u faze 4 i 5 |
| Arhitektonski gateovi za `R10`, `R15`, `R24` i `R36` su ratificirani, a same stavke ostaju otvorene | **ispunjena**, i to je izričita namjera uvjeta |
| Svih 19 kralježnica je ratificirano | **ispunjena** |
| Promjene definicija i preduvjeta imaju odobrenu kartu | **ispunjena** |
| Nema neriješenog sukoba između pregleda i živih upravljačkih dokumenata | **ispunjena** |

Četiri od pet klauzula stoje. Peta ne stoji i ne može stajati u ovoj fazi.

## Je li gate time neprolazan?

Nije, i razlog treba izreći precizno.

Izlazni testovi **ovoga paketa** su tri i svi su ispunjeni: svaki imenovani
preduvjet ima svoj traženi dokaz, nijedna prepreka nije skrivena agregacijom, i
izvještaj je vezan uz jedno deklarirano izvorno stanje. Klauzula „R04 is closed"
pripada **narativnom opisu izlaznoga uvjeta u planu**, a ne ugovoru
`review_gate` ni izlaznim testovima ovoga paketa.

Registar, koji je po `AGENTS.md` mjerodavan zapis rada i statusa, sam propisuje
da `R04-ROUTES-two-track-map` pripada paketu `P5-ROUTES` u fazi 5 i da
`R04-C11-fixed-order` pripada paketu `WC-C11` u fazi 4. Plan i registar time
proturječe jedan drugome oko toga kada `R04` može biti zatvoren. To je
neusklađenost dvaju ratificiranih dokumenata, a ne propust nekoga paketa.

Ovaj paket nema ovlast izmijeniti ratificirani plan i nije ga izmijenio.
Zabilježio je neusklađenost, imenovao pakete koji je jedini mogu razriješiti i
proslijedio je. Ako autor želi da tekst plana odgovara registru, to je autorska
izmjena i traži vlastitu odluku; nijedan je paket ne smije uzeti sam.

## Neovisna provjera 22 preduvjetna paketa

Faza 2 ima 23 paketa. Dvadeset i dva su `accepted`; dvadeset treći je ovaj.
Svaki je od 22 provjeren **pojedinačno**, prema vlastitom ugovoru, a ne skupno.

Za svaki je paket ponovno izvedeno trinaest uvjeta: da mu je status terminalan,
da mu se `source_state` i `change_reference` poklapaju, da priznanice točno
pokrivaju deklarirane `required_evidence`, `outputs` i `exit_tests`, da je svaki
izlazni test označen kao `passed`, da paket nosi sav dokaz i sve testove koje
njegov ugovor traži te barem jedan test iznad ugovora, da ima zapis pregleda s
deklaracijom `all_future_effects_recorded`, da mu popis odlaznih isporuka točno
odgovara isporukama kojima je on izvor, i da mu nijedna dolazna isporuka nije
ostala u neterminalnom stanju.

**Rezultat: svih 22 zadovoljava svih trinaest uvjeta.** Nijedan paket nema
neterminalnu dolaznu isporuku i nijedan zapis pregleda ne izostavlja isporuku
kojoj je taj paket izvor.

| Paket | Ugovor | Dolazne | Odlazne |
|---|---|---|---|
| `G-A2a` | `decision_gate` | 0 | 1 |
| `P2-CLAIMS` | `shared_architecture` | 1 | 0 |
| `G-A2d` | `decision_gate` | 0 | 5 |
| `P2-ASSESS` | `shared_architecture` | 3 | 0 |
| `P2-IDENTITY` | `shared_architecture` | 0 | 0 |
| `G-A2b-PREFACE` | `decision_gate` | 0 | 1 |
| `P2-SPINE-PREFACE` | `shared_registry` | 1 | 0 |
| `G-A2b-I` | `decision_gate` | 0 | 1 |
| `P2-SPINE-I` | `shared_registry` | 1 | 1 |
| `G-A2b-II` | `decision_gate` | 0 | 1 |
| `P2-SPINE-II` | `shared_registry` | 1 | 1 |
| `G-A2b-III` | `decision_gate` | 0 | 1 |
| `P2-SPINE-III` | `shared_registry` | 1 | 0 |
| `G-A2b-IV` | `decision_gate` | 0 | 1 |
| `P2-SPINE-IV` | `shared_registry` | 1 | 1 |
| `G-A2b-V` | `decision_gate` | 0 | 1 |
| `P2-SPINE-V` | `shared_registry` | 2 | 2 |
| `G-A2b-FINALE` | `decision_gate` | 0 | 1 |
| `P2-SPINE-FINALE` | `shared_registry` | 1 | 2 |
| `G-A2c` | `decision_gate` | 0 | 2 |
| `P2-TERMS` | `shared_registry` | 7 | 4 |
| `P2-DOCS` | `governing_documents` | 2 | 3 |

### Dva nalaza o dokazima koje treba iznijeti, a nisu prepreke

**Prvi.** Sedam najranijih paketa faze 2 ne navodi nijednu namjernu grešku u
svojoj dovršnoj evidenciji: `G-A2a`, `P2-CLAIMS`, `G-A2d`, `P2-ASSESS`,
`P2-IDENTITY`, `G-A2b-PREFACE` i `G-A2b-I`. To nije kršenje njihovih ugovora —
nijedan ugovor faze 2 ne traži namjernu grešku; traži je samo
`release_engineering`. Nalaz je o pokrivenosti, ne o valjanosti. Uz to,
`P2-ASSESS` i `P2-IDENTITY` **jesu** zabilježili po dvije namjerne greške, samo
pod oznakom `check:` umjesto `fixture:`, pa je stvarni broj paketa bez ijednoga
takvog zapisa pet, a ne sedam. Od `G-A2b-II` nadalje svaki gate bilježi obje
namjerne greške radnoga tijeka.

Provjeritelj koji `P2-CLAIMS` navodi kao dokaz,
`scripts/check-book-architecture.py`, **uopće nema mehanizam namjerne greške**.
To je stvarna praznina u pokrivenosti i prosljeđuje se.

Šest namjernih grešaka koje postoje ponovno je pokrenuto u ovom izvornom stanju i
svih šest vraća izlaz 1: `protected_export_field` i `assessed_code_production` za
ugovor ocjenjivanja, `fairness_widget_dropped` i `nlp_implementation_admitted` za
identitetske brifove, `ratified_without_decision` i
`part_i_visible_code_admitted` za kralježnice.

**Drugi.** `P2-CLAIMS`, `P2-ASSESS` i `P2-IDENTITY` u svojoj dovršnoj evidenciji
nose oznaku `check:chapter-spines-ratified-0-of-19`. Ta je tvrdnja bila istinita
u trenutku njihova zatvaranja i danas nije: ratificirano je 19 od 19. Dokaz je po
ugovoru vezan uz deklarirano izvorno stanje, pa to nije greška u zapisu nego
povijesni zapis. Bitno je da **živi provjeritelji tu tvrdnju više ne postavljaju**:
`scripts/check-book-architecture.py`, `scripts/check-assessment-architecture.py` i
`scripts/check-identity-briefs.py` u ovom stanju javljaju „chapter spines
ratified: 19 of 19, each at its own G-A2b gate". Snimka je zamijenjena
invarijantom, kako je `P2-SPINE-PREFACE` i zabilježio.

## Živo stanje provjereno u ovom izvornom stanju

| Provjera | Rezultat |
|---|---|
| `scripts/check-review-workflow.R` | prolazi; 36 roditelja, 371 dijete, nula nemapiranih, 188 paketa, 18 manifesta, 64 isporuke |
| `scripts/check-chapter-spines.py` | 19 ratificiranih od 19; 19 jedinica u `draft` |
| `scripts/check-book-architecture.py` | prolazi; 4 djelatnosti, 8 nacrta, 7 niti; 19 od 19 kralježnica |
| `scripts/check-assessment-architecture.py` | prolazi; produkcija koda zabranjena u svakoj stepenici; 0 zapisa rješenja i 0 provedenih putova |
| `scripts/check-identity-briefs.py` | prolazi; 19 jedinica u `draft` |
| `scripts/check-terminology.py` | `TERMINOLOGY_OK`; 166 oblika kralježnice, 13 oblika gatea, 12 povučenih, 8 razilaženja, tvrdnja o neovisnoj recenziji `false` |
| `scripts/check-concepts.py` | `CONCEPT_INTEGRITY_OK definitions=46 ledger_debt=0 graph_fresh=true` |
| `scripts/check-manuscript-integrity.py` | `MANUSCRIPT_INTEGRITY_OK lane=all`, 19 poglavlja |
| `scripts/check-book-inventory.py` | `BOOK_INVENTORY_OK pages=37 chapters=19 appendices=6 solutions=0` |
| `scripts/check-citations.py` | `CITATION_INTEGRITY_OK files=37 live_keys=35 records=35` |
| `scripts/check-widgets.py` | 17 widgeta, svaki s grafom, blizancem i registrom |
| `scripts/check-figure-introductions.py` | `FIGURE_INTRO_OK registered_debt=1 unexpected=0 stale_debt=0` |
| `scripts/check-tokens.R` | svi slojevi dizajna usklađeni |

Preostali zapis duga je jedan i imenovan: uvod za `fig-anscombe` u poglavlju 5,
u vlasništvu paketa `WB-C05`. Pojmovni je dug povučen u `P2-TERMS`.

## Granica ovlasti, provjerena a ne pretpostavljena

`push`, `merge`, `tag`, `archive` i `deploy` u registru su i dalje `false`;
dopušteni su samo omeđeni provjereni lokalni commitovi. Nijedan paket faze 2 nije
tvrdio ni jednu od tih ovlasti, nijedna vanjska poruka nije poslana, a broj
poslanih vanjskih poruka i dalje je nula uz 82 kanonska upita.

Obje autorove izmjene od 5. kolovoza 2026. vrijede i u ovom su stanju provjerene.
Tvrdnja o neovisnoj recenziji nazivlja nigdje ne postoji i registar je zabranjuje,
uz namjernu grešku koja tu zabranu dokazuje. Nijedan paket faze 2 nije odabrao ni
promaknuo skup podataka niti tvrdio dopuštenje nositelja prava, a
`H-P1B-DATA-LIC-003` nije nadomješten.

## Što ovaj gate nije napravio

Nije zatvorio nijednu stavku registra osim vlastitoga paketa. Nije zatvorio
`R04` ni ijedno njegovo otvoreno dijete. Nije izmijenio ratificirani plan ni
njegov izlazni uvjet. Nije dirnuo prozu, registre, kralježnice, definicije,
generirane artefakte ni faze poglavlja. Nije pokrenuo render.
