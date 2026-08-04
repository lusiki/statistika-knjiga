# P2-SPINE-PREFACE — upisana kralježnica predgovora

**Paket:** `P2-SPINE-PREFACE`

**Datum:** 4. kolovoza 2026.

**Ishod:** ratificirana kralježnica predgovora upisana je u kanonski registar,
shema registra proširena je tako da preduvjeti i isključenja postanu provjerljivi,
a svi potrošači koji su tvrdili da nijedna kralježnica nije ratificirana
usklađeni su. Nijedna rečenica proze nije promijenjena.

## Ulazi i potrošeni prijenos

`H-G-A2B-PREFACE-001` priznat je i potrošen prije prve sadržajne izmjene. Njegova
je dispozicija da ratificirana kralježnica iz gatea `G-A2b-PREFACE` bude točna i
jedina granica ovoga paketa. Pročitani su u cijelosti ugovor paketa
`shared_registry`, stavka `R04-SPINE-PREFACE` i trajni zapis odluke
`notes/reports/g-a2b-preface-spine-decision-2026-08-04.md`.

`H-P0-STATE-001` cilja `WA-C00` i ostaje `pending`. Ovaj ga paket ne troši; njegova
je obveza sada zapisana kao isključenje 2 u kralježnici, pa je `WA-C00` može
provesti nad stvarnom prozom i tek tada potrošiti.

## Što je upisano

Jedinica `00-predgovor` u
`bookwright_plugin/bookwright/shared/chapter-spine.json` sada nosi devet nosivih
aspekata, pet nosivih pojmova, prazan popis preduvjeta i dvanaest isključenja,
zajedno s oznakom gatea, nadnevkom ratifikacije i putanjom trajnoga zapisa odluke.
Zapis je vjeran prihvaćenom nacrtu; ništa nije dodano ni izostavljeno.

Prazan popis preduvjeta nije propust nego odluka. Predgovor je ulazna točka knjige
i ne smije pretpostaviti nijedno poglavlje, dodatak ni widget.

Preostalih osamnaest jedinica ostaje neratificirano i prazno. Kralježnice
poglavlja 1 do 3 dolaze na gateu `G-A2b-I`, a ostale na svojim gateovima.

## Proširenje sheme

`chapter-spine.schema.json` do sada je dopuštao samo `id`, `key_aspects`,
`key_terms` i `ratified`, pa preduvjeti i isključenja koje traži stavka
`R04-SPINE-PREFACE` nisu imali gdje stajati. Shema sada dopušta i `ratified_at`,
`decision`, `decision_record`, `prerequisites` i `exclusions`. Nijedno postojeće
polje nije uklonjeno ni promijenjeno, pa svi raniji zapisi ostaju valjani.

Shema ta polja ne čini bezuvjetno obveznima jer lokalni validator ne podržava
uvjetne sheme. Obveznost za ratificirani zapis provodi
`scripts/check-chapter-spines.py`.

## Usklađivanje potrošača

Tri su provjere dosad tvrdile da je ratificirano nula od devetnaest kralježnica.
Ta je tvrdnja bila točan snimak stanja pri zatvaranju njihovih paketa, ali nije
bila invarijanta: `P2-SPINE-PREFACE` je paket koji tu brojku po dizajnu mijenja.

Sve tri sada provjeravaju stvarnu invarijantu, a to je da njihov vlastiti registar
nema ovlast ratificirati kralježnicu i da svaka ratificirana kralježnica nosi svoj
`G-A2b` gate. Brojka se ispisuje, ali se više ne tvrdi kao nula.

| Provjera | Prije | Sada |
|---|---|---|
| `check-book-architecture.py` | „P2-CLAIMS mora ostaviti svih 19 kralježnica neratificiranima" | `chapter_spine_ratification_authorised` je `false` i svaka ratificirana kralježnica imenuje svoj `G-A2b` gate |
| `check-assessment-architecture.py` | „P2-ASSESS mora ostaviti svih 19 kralježnica neratificiranima" | ista invarijanta, uz granicu autoriteta arhitekture provjere znanja |
| `check-identity-briefs.py` | „P2-IDENTITY mora ostaviti svih 19 kralježnica neratificiranima" | ista invarijanta, uz dodatnu provjeru da ratificirana kralježnica stupa dolazi sa svoga dijela, a ne iz brifova |

Prihvaćena stanja `architecture:sha256-30e10508…`, `assessment:sha256-c1206f08…`
i `identity:sha256-f09124e5…` ostaju nepromijenjena; promijenjena je samo tvrdnja
koju provjere iznose o broju ratificiranih kralježnica.

## Nova provjera i njezini negativni fiksatori

`scripts/check-chapter-spines.py` validira registar prema shemi, traži svih
devetnaest jedinica u kanonskom redoslijedu i za svaku ratificiranu kralježnicu
zahtijeva neprazne aspekte, točan `G-A2b` gate te jedinice, trajni zapis odluke,
nadnevak, izričite preduvjete koji smiju upućivati samo na ranije jedinice, i
neprazna isključenja. Za predgovor i Dio I dodatno zahtijeva izričito isključenje
vidljivoga koda, a za predgovor i granicu Dodatka B te zabranu `#def-` blokova.
Neratificirana kralježnica mora ostati prazna i bez odluke. Provjera također
potvrđuje da nijedna faza poglavlja nije napredovala iznad `draft` i da nije
nastala nijedna ruta rješenja.

Oba obvezna negativna fiksatora vraćaju izlaz 1. Fiksator
`ratified_without_decision` uklanja oznaku gatea s ratificirane kralježnice, a
`part_i_visible_code_admitted` uklanja isključenje vidljivoga koda iz jedinice
Dijela I.

## Kanonsko stanje i provjere

Deterministično stanje registra jest
`spine:sha256-53ee28d57cfb7fb1b533e77977abae152717a0afc1b3a7ec24ad35b03145149c`.

Prošli su `scripts/check-chapter-spines.py`, `scripts/check-book-architecture.py`,
`scripts/check-assessment-architecture.py`, `scripts/check-identity-briefs.py` i
blokirajuća struktura `scripts/check-manuscript-integrity.py --lane structure` s
devetnaest poglavlja. Oba negativna fiksatora arhitekture provjere znanja i oba
fiksatora identitetskih brifova i dalje padaju s izlazom 1.

Nijedna proza poglavlja ili dodatka, faza jedinice, terminologija, podatkovni
paket, ruta, render, generirani artefakt ni vanjska ovlast nisu promijenjeni.
Osamnaest kralježnica ostaje neratificirano i svih devetnaest jedinica ostaje u
fazi `draft`.
