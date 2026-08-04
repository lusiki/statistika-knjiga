# P1-VERIFY — provjera zatvorenosti prve faze

**Paket:** `P1-VERIFY`

**Datum provjere:** 4. kolovoza 2026.

**Ishod:** otvoren; `P1A-METHODS` nije vezan uz trenutačni Git blob
Poglavlja 2.

## Granica i stanje izvora

Provjera je vezana uz urezani izvor:

- grana `revision/comprehensive-review`;
- commit `b7898ef03b41609e25dfc4fbc4a91c6f71532e41`;
- stablo `05ab7d9a4c20cdb3559709e25650569e72620e49`.

Svih dvanaest dokazanih implementacijskih commita predaka su toga commita.
Matrica uspoređuje njihove ugovore, strukturirane primitke, trajne izvještaje i
deklarirana stanja s navedenim stablom. Nije prihvaćen sažetak paketa bez
provjere njegova izvora.

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

## Fail-closed matrica

| Preduvjet | Ugovor i izvor | Pozitivni dokaz prema provjeravanom stanju | Obvezna negativna proba | Nerazriješeni blokator i granica ovlasti | Nalaz |
|---|---|---|---|---|---|
| `P1A-METHODS` | `methods_verification`; source commit `7832b07`, tree `7168b933…`; izvještaj `p1a-methods-verification-2026-08-03.md` | Izvorni panel ima svih 12 izvještaja i agregatnu matricu, ali je dokaz za `P1A-C02` vezan uz blob `ccae632a…`, a trenutačni blob je `908780ee…`. | Izvorne kontrolne probe `generic_packet_evidence` i `invalid_outside_ask_link` pale su kako je propisano; one dokazuju kontrolu primitka, ne aktualnost metodološkoga čitanja. | Commit `9995f3b…` nakon zatvaranja uklanja metodološki sadržaj o trećoj varijabli. Nema neovisnoga metodološkog čitanja bloba `908780ee…`, nove agregatne matrice ni zabilježene invalidacije. `P1-VERIFY` nema ovlast proizvesti taj dokaz ili uređivati poglavlje. | **BLOKIRA** |
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

## Točan popis blokatora

### Nerazriješen blokator

1. `P1A-METHODS`, preko `P1A-C02`: izvještaj
   `p1a-c02-methods-review-2026-08-03.md` i agregatni gate dokazuju blob
   `ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00`. Commit
   `9995f3b7bf93afd95b4cb7fd4b6be713e78cbff3` potom je promijenio
   `chapters/02-mjerenje-i-dizajn.qmd`; u provjeravanom stanju blob je
   `908780ee6fdb2916afb1b1226bb3c9f567a81ce2`. Nedostaju neovisno
   metodološko čitanje toga bloba, novi strukturirani primitak `P1A-C02` i
   agregatna matrica `P1A-METHODS` vezana uz isti izvor.

### Razriješeni blokatori u ovom gateu

Nijedan. Gate nema ovlast popravljati preduvjete, a prividno popravljanje
kontrolnom ili stilskom provjerom sakrilo bi nedostajući metodološki dokaz.
Preostalih jedanaest preduvjeta nema nerazriješen blokator unutar svojega
ratificiranog opsega prve faze.

### Vidljive, ali neblokirajuće kasnije granice

- `_quarto.yml` checksum razlika ostaje otvorena isključivo pod
  `H-P1C-EXPORT-002` za `P7-FREEZE` i `P8-META`; nije proglašena zelenom.
- Izostanak `docs/errata.html` jest očekivano stanje urezanoga razvojnog builda
  nakon paketa koji nije smio renderirati. Ne služi kao pozitivan dokaz i nije
  popravljen.
- Svih sedam vanjskih release ovlasti ostaje lažno; ova provjera ne odobrava
  push, merge, tag, arhiviranje, deployment ni objavu.

## Budući učinak i odluka gatea

Jedini novi budući učinak jest blokada samoga `P1-VERIFY`: prije nastavka treba
u zasebno omeđenom korekcijskom ili revalidacijskom radu pribaviti aktualan
neovisan metodološki primitak za `P1A-C02` i ponovno vezati `P1A-METHODS` uz
isti izvor. To nije poslano kasnijem paketu jer nijedan kasniji paket ne smije
početi dok je gate otvoren. `next_permitted_packet` zato je `null`, a `G-A2a`
ostaje netaknut i blokiran svojom postojećom ovisnošću.

Nije potreban bounded outside ask: poznata je dokazna praznina i postojeća
uloga recenzenta. Potrebno je novo, zasebno odobrenje opsega za revalidaciju,
ne vanjska poruka ili javna radnja.

`P1-VERIFY` ostaje `in_progress`; `completion_evidence` ostaje prazan i
`change_reference` ostaje `null`.

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
active packet: P1-VERIFY
next permitted packet: none while a packet is active
```

Obje obvezne in-memory negativne probe završile su kodom 1 iz točnoga razloga:

```text
EXPECTED_FAILURE fixture=generic_packet_evidence exit=1
Terminal packet completion_evidence must be a structured mapping: G-A0

EXPECTED_FAILURE fixture=invalid_outside_ask_link exit=1
Outside ask OA-G-A1A-C10-SPEC links unknown items: R99-NOT-A-REGISTER-ITEM
```

Time su dokazani i otvoreno stanje gatea i fail-closed kontrolni ugovor. Nije
pokrenut `G-A2a` ni ijedan kasniji paket.
