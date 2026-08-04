# P1-VERIFY — provjera zatvorenosti prve faze

**Paket:** `P1-VERIFY`

**Datum provjere:** 4. kolovoza 2026.

**Ishod:** prihvaćen nakon evidence-only revalidacije `P1A-C02` i
`P1A-METHODS`; svih dvanaest preduvjeta prolazi.

## Granica i stanje izvora

Provjera je vezana uz urezani izvor:

- grana `revision/comprehensive-review`;
- commit `89229759ed61ce3a3bced127496b731dfdd7cf73`;
- stablo `59bbab72e2a10ea8bbd9fc5d9e95cd724a423568`.

Svih dvanaest dokazanih implementacijskih commita predaka su toga commita.
Matrica uspoređuje njihove ugovore, strukturirane primitke, trajne izvještaje i
deklarirana stanja s navedenim stablom. Nije prihvaćen sažetak paketa bez
provjere njegova izvora.

Prvi prolaz na commitu `b7898ef…` otkrio je jedan izvorni nesklad. Autor Luka
Sikic potom je 4. kolovoza 2026. izričito odobrio evidence-only ponovno
otvaranje `P1A-C02` i `P1A-METHODS`, bez izmjene proze. Završna matrica u ovom
izvještaju uključuje taj novi exact-source primitak.

Radno stablo prije ove provjere sadržavalo je jednu tuđu, neumetnutu izmjenu
`.github/workflows/publish.yml`: prelazak `actions/checkout` s v4 na v5 i
dodavanje instalacije `librsvg2-dev`. Ta izmjena nije dio provjeravanoga
commita, ne mijenja nijedan blokirajući korak i ostavljena je netaknuta. Svi
zaključci o stanju izvora odnose se na urezani commit; rezultati naredbi iz
radnoga stabla upotrijebljeni su samo ondje gdje ta jedina razlika ne ulazi u
provjeravani put.

Paket nije mijenjao rukopis, implementaciju, inventare, lockove, generirane
artefakte, release metapodatke ni vanjsko stanje. Nije pokrenut render,
objava, upload ili deployment.

## Fail-closed matrica {#fail-closed-matrix}

| Preduvjet | Ugovor i izvor | Pozitivni dokaz prema provjeravanom stanju | Obvezna negativna proba | Nerazriješeni blokator i granica ovlasti | Nalaz |
|---|---|---|---|---|---|
| `P1A-METHODS` | `methods_verification`; završno stanje commit `8922975…`, tree `59bbab72…`; izvještaji `p1a-methods-verification-2026-08-03.md` i `p1a-methods-revalidation-2026-08-04.md` | Svih 12 redaka ima strukturirane primitke. Novi read-only `critic_methods` pročitao je cijeli Chapter 2 blob `908780ee…`, dao 5/5 za korektnost, pretpostavke, tumačenje i preciznost te nula nalaza. Ostalih 11 chapter blobova nije se promijenilo. | Izvorne i završne kontrolne probe `generic_packet_evidence` i `invalid_outside_ask_link` padaju kako je propisano. Byte-identičnih osam R/OJS blokova čuva izvorni numerički primitak. | Prethodni source mismatch razriješen je exact-source izvještajima `p1a-c02-methods-revalidation-2026-08-04.md` i `p1a-methods-revalidation-2026-08-04.md`. Nema izmjene proze ni nerazriješenog blokatora. | **PROLAZI** |
| `P1B-NAVARRO` | `evidence_licence`; `state:sha256-fc7f6536…`; izvještaj `p1b-navarro-provenance-and-licence-audit-2026-08-03.md` | Trenutačni citatni pregled prolazi s 35 živih i 35 bibliografskih ključeva; kasniji diffovi ne vraćaju javnu uporabu Navarra, a licencni izvor i vlasnička odluka ostaju nepromijenjeni. | Ugovor ne propisuje paketnu negativnu fixturu; obje kontrolne fixture provjere bile su obvezne i prošle su pri zatvaranju. | Nema blokatora. Vlasnička odluka ostaje nulta javna uporaba; nova uporaba zahtijevala bi novu odluku i licencnu provjeru. | **PROLAZI** |
| `P1B-DATA-LIC` | `evidence_licence`; `state:sha256-2e0f065b…`; izvještaj `p1b-data-licence-access-inventory-2026-08-03.md` | Sedmoputni manifest reproduciran je na prihvaćenom stanju; trenutačna provjera javlja `DATA_INTEGRITY_OK`, 50.300 redaka, katalog `pre-P3`, nula snimki i `CC-BY-4.0`. | Nije propisana paketna negativna fixture proba; trenutna namjerno duplicirana podatkovna oznaka pada, a cijeli integrity harness javlja sedam očekivanih padova. | Nema blokatora za sadašnje generirane skupove. Svih 13 predloženih paketa ostaje samo uvjetna kasnija prava/pristup granica. | **PROLAZI** |
| `P1B-BIB` | `evidence_licence`; `state:sha256-8e9a96cf…`; izvještaj `p1b-bibliography-metadata-audit-2026-08-03.md` | Četveroputni manifest reproduciran je na prihvaćenom stanju. Trenutačni pregled javlja `CITATION_INTEGRITY_OK files=37 live_keys=35 records=35 blanket_nocite=0`. | Ugovor ne propisuje paketnu fixturu; namjerno nepoznat ključ pada u integrity harnessu. | Nema blokatora. Svaki budući empirijski navod i dalje zahtijeva provjeren zapis, bez izmišljanja ključa ili nalaza. | **PROLAZI** |
| `P1B-META` | `public_metadata`; `state:sha256-11be9838…`; izvještaj `p1b-public-metadata-audit-2026-08-03.md` | Jednoputni manifest reproduciran je na prihvaćenom stanju. Cijeli trenutačni `README.md` i kasniji diff pregledani su; kasnije izmjene samo usklađuju zaključanu obnovu i prihvaćeni PDF put, bez tvrdnje o objavljenom izdanju. | Ugovor ne propisuje paketnu fixturu; obje kontrolne fixture provjere bile su obvezne pri zatvaranju. | Nema blokatora. Handoffovi prema `P2-DOCS` i `P5-ROUTES` i dalje nose točno imenovane kasnije dokumentacijske i putne obveze. | **PROLAZI** |
| `P1B-GOV` | `release_governance`; `governance:sha256-dcfcc7d7…`; izvještaj `p1b-release-governance-2026-08-04.md` | Predobjavna shema, vlasnici i hrvatske površine ostaju na mjestu; sve vanjske ovlasti ostaju `false`. Izvorni pozitivni dokaz pri stanju mehanizma prolazi. | Ugovor ne propisuje zasebnu fixturu. Trenutačni `check-release-governance.R` namjerno završava kodom 1 zbog jedne `_quarto.yml` SHA-256 razlike, čime mehanizam i dalje dokazuje fail-closed ponašanje. | Razlika nije skrivena ni riješena: `H-P1C-EXPORT-002` je već obvezno dostavlja `P7-FREEZE` i `P8-META`. To nije završni release-candidate ugovor ovoga paketa. Push, merge, tag, arhiva, deployment i objava nisu odobreni. | **PROLAZI U GRANICI 1. FAZE** |
| `P1C-PDF` | `release_engineering`; commit `f2c4f824…`; izvještaj `p1c-pdf-release-path-2026-08-04.md` | Čisti dokaz s toga izvora daje novi PDF SHA-256 `cb57918e…`. Kasnija inventarna dopuna omotača zasebno je vezana uz commit `8731a9d…`; trenutačna izolirana proba ponovno prolazi. | Trenutačno prolaze sva tri očekivana pada: preflight, build-command i stale/missing artifact; harness javlja četiri slučaja ukupno. | Nema blokatora. Novi puni PDF nije građen u ovom gateu jer su render i generirani artefakti izvan ovlasti. | **PROLAZI** |
| `P1C-INTEGRITY` | `release_engineering`; commit `919b0b1…`, `sha256-8699a3b2…`; izvještaj `p1c-integrity-gates-2026-08-04.md` | Trenutačno prolaze tokeni, stil i struktura 25 izvora, figure s jednim točno registriranim dugom, citati, pojmovi s dva točno registrirana duga i podaci. | Trenutačni harness namjerno kvari svih sedam putova; svaki završava kodom 1 i završni primitak glasi `INTEGRITY_NEGATIVE_FIXTURES_OK lanes=7`. | Nema blokatora. `fig-anscombe` i dva pojmovna otiska ostaju točno usmjeren kasniji dug; promjena otiska pada. | **PROLAZI** |
| `P1C-EXPORT` | `release_engineering`; commit `ac7c34f…`, `sha256-3453f828…`; izvještaj `p1c-export-release-path-2026-08-04.md` | Trenutačna `--release --validate-only` provjera prolazi za 19 poglavlja i 20 zaštićenih regija. | Trenutačno prolaze tri očekivana pada: build error, metadata drift i protected-content leak; `publish=false`. | Nema blokatora za javni izvoz. Buduće rute rješenja ostaju pod `H-P1C-EXPORT-001`; checksum dug ostaje pod `H-P1C-EXPORT-002`. | **PROLAZI** |
| `P1C-BROWSER` | `release_engineering`; commit `8b04c6c…`, `browser-smoke:sha256-c76a872c…`; izvještaj `p1c-browser-smoke-audit-2026-08-04.md` | Inventarni paket kasnije je promijenio potrošač rute, pa je ugovor ponovno provjeren na sadašnjem izvoru. Smoke prolazi na Poglavlju 7 za širine 1280/390, svijetlu/tamnu temu, tipkovnicu, reset i živu regiju. | Trenutačna nepostojeća ruta daje HTTP 404 i harness javlja `BROWSER_SMOKE_NEGATIVE_FIXTURES_OK fixtures=1`. | Nema blokatora bounded smoke ugovora. `docs/errata.html` nije generiran jer `P1C-INVENTORY` izričito nije renderirao; statička post-render provjera bez svojega preduvjeta zato nije dokaz neuspjeha preglednika i nije popravljana u ovom gateu. | **PROLAZI** |
| `P1C-PARITY` | `release_engineering`; commit `79824e0…`, `parity:sha256-f22f3df4…`; izvještaj `p1c-widget-parity-2026-08-04.md` | Trenutačno prolazi svih 17 parova: šest egzaktnih i jedanaest distribucijskih. | Trenutačna regresija očekivane vrijednosti namjerno pada; harness javlja `WIDGET_PARITY_NEGATIVE_FIXTURES_OK fixtures=1`. | Nema blokatora. Granice `w10` i različitih `w08` populacija ostaju one koje je dokazao prihvaćeni metodološki ugovor. | **PROLAZI** |
| `P1C-INVENTORY` | `release_engineering`; commit `8731a9d…`, `inventory:sha256-1cc773c5…`; izvještaj `p1c-book-inventory-2026-08-04.md` | Trenutačni manifest i dalje je identičan prihvaćenom: 37 stranica, 19 jedinica poglavlja, dodaci A–F, nula ruta rješenja. Logička provjera daje vlastiti, zaseban digest `b2f20bd4…`. | Trenutačno prolaze tri očekivana pada: missing, extra/unsynced i reordered; pozitivna privremena sinkronizacija prolazi s 38 stranica. | Nema blokatora. D10 i rute rješenja ostaju kasniji ugovori; paket nije stvarao ni renderirao novu stranicu. | **PROLAZI** |

## Točan popis blokatora {#exact-blocker-list}

### Nerazriješeni blokatori

Nema ih. Svih dvanaest preduvjeta prolazi unutar svojega ratificiranog opsega
prve faze.

### Razriješeni blokatori u ovom gateu

1. `P1A-METHODS`, preko `P1A-C02`: prvi prolaz ispravno je zaustavio gate jer
   je stari izvještaj dokazivao blob `ccae632a…`, a živi blob bio je
   `908780ee…`. Autor je odobrio zasebnu evidence-only revalidaciju. Neovisni
   `critic_methods` zatim je na blobu `908780ee…` dao četiri ocjene 5/5 i nula
   nalaza, a nova agregatna matrica potvrdila je da se drugih jedanaest blobova
   nije promijenilo. Novi strukturirani primitci sada su vezani uz isti izvor.

### Vidljive, ali neblokirajuće kasnije granice

- `_quarto.yml` checksum razlika ostaje otvorena isključivo pod
  `H-P1C-EXPORT-002` za `P7-FREEZE` i `P8-META`; nije proglašena zelenom.
- Izostanak `docs/errata.html` jest očekivano stanje urezanoga razvojnog builda
  nakon paketa koji nije smio renderirati. Ne služi kao pozitivan dokaz i nije
  popravljen.
- Svih sedam vanjskih release ovlasti ostaje lažno; ova provjera ne odobrava
  push, merge, tag, arhiviranje, deployment ni objavu.

## Budući učinak i odluka gatea

Evidence-only revalidacija ne stvara novi downstream učinak. Postojeće
ovisnosti već vode prihvaćeni `P1-VERIFY` u `G-A2a`, pa bi novi handoff
duplicirao mjerodavnu ovisnost. Poznati kasniji dugovi ostaju na svojim
postojećim isporukama i nisu riješeni unaprijed.

`P1-VERIFY` je `accepted`; strukturirani `completion_evidence` i
`change_reference` vezani su uz commit `8922975…` i tree `59bbab72…`.
`next_permitted_packet` postaje `G-A2a`, ali taj paket nije pokrenut.

## Izvršene provjere

Uz izvorne čiste primitke navedene u matrici, na trenutačnim provjeravanim
putovima izvršene su pozitivne i namjerno neuspješne paketne naredbe za
inventar, PDF put, sedam integrity putova, AI izvoz, browser smoke, paritet i
njihove fixture harnessove. Svi su dali očekivani ishod naveden u matrici.
`check-release-governance.R` dao je točno jednu već registriranu `_quarto.yml`
SHA-256 razliku. `check-rendered-html.py docs` dao je samo nedostajući
`docs/errata.html`, ali bez prethodnoga rendera koji ovaj gate ne smije
pokrenuti, pa taj rezultat nije korišten kao dokaz pregledničkog neuspjeha.

Nakon usklađenja registra, handoff ledgera i nadzorne ploče izvršeno je:

```text
Comprehensive-review workflow: OK
active packet: none
next permitted packet: G-A2a
```

Obje obvezne in-memory negativne probe završile su kodom 1 iz točnoga razloga:

```text
EXPECTED_FAILURE fixture=generic_packet_evidence exit=1
Terminal packet completion_evidence must be a structured mapping: G-A0

EXPECTED_FAILURE fixture=invalid_outside_ask_link exit=1
Outside ask OA-G-A1A-C10-SPEC links unknown items: R99-NOT-A-REGISTER-ITEM
```

Time su dokazani zatvaranje gatea i fail-closed kontrolni ugovor. `G-A2a` je
samo sljedeći dopušteni paket; nije pokrenut ni on ni ijedan kasniji paket.
