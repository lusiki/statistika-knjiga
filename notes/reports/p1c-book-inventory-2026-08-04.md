# P1C-INVENTORY: kanonski inventar knjige i putova

Datum: 4. kolovoza 2026.

Paket: `P1C-INVENTORY`

Stavka: `R05-CONFIG-inventories`

Implementacijski commit: `8731a9d62c72264b435b829924e3259b730311b1`

Stanje implementacije:
`inventory:sha256-1cc773c5b0a9546c2c111b994d6c9eda3797139419cb91e4396fa1d92c49e499`

Kanonski sadržaj inventara:
`b2f20bd4c7877cac30cc36117fef5c5f0872ed874e67d674cfd0911333c48e0f`

## Granica paketa

Paket uvodi samo konfiguracijski vođen inventar stranica, strukture knjige,
dodataka, navigacije, javnih putova i trenutačno praznoga inventara putova
rješenja. Nije dodana ni uklonjena nijedna sankcionirana stranica. Sačuvano je
svih šest i samo šest ratificiranih dodataka A–F, u istom redoslijedu. Nisu
mijenjani tekst poglavlja ili dodataka, katalog podataka, procjena, AI izvoz,
paritet widgeta, pregledničko ponašanje izvan potrošnje inventara, renderirani
artefakti, release-candidate stanje ni objava. D10, D06 i D34 odluke nisu
razriješene unaprijed; `solution_routes` zato dokazano ostaje prazan.

Nije pokrenut Quarto render, PDF/DOCX build, upload, deploy ni publish.

## Trag postojećih kopija

Prije uređivanja pročitani su `_quarto.yml`, sva tri profila, oba omotača
knjige, objavni workflow te svi skriptni potrošači inventara. Trag je zatvoren
ovako:

| Vlasnik ili potrošač | Dispozicija |
|---|---|
| `_quarto.yml` | Struktura knjige, literatura, dodaci, navbar, podnožje i PDF alat postali su označene projekcije iz jednoga izvora. |
| `_quarto-kolegij.yml`, `_quarto-pdf.yml`, `_quarto-docx.yml` | Profili i dalje nasljeđuju kanonsku strukturu; blokirajuća provjera zabranjuje konkurentske popise poglavlja, dodataka i navigacije. |
| `R/build-ai-exports.R`, `R/build-concept-graph.R` | I dalje čitaju kanonski redoslijed iz `_quarto.yml`; označena projekcija sada se obnavlja iz sankcioniranoga izvora prije njihove potrošnje. |
| `scripts/check-rendered-html.py` | Očekivane HTML stranice, poglavlja s widgetom i dodaci dolaze iz kanonskoga inventara. |
| `scripts/audit-rendered-html.js` | Javni putovi, korijenski alias, vrste stranica, widgeti, dodaci i smoke-stranica dolaze iz istoga inventara. |
| `styles/book-include.html` | Popisi samostalnih stranica, grupa navbara, unutarnjih odredišta i putova poglavlja označena su generirana projekcija. |
| `scripts/embed-404-assets.py` | Posebna prijenosna stranica više nije zadana imenom datoteke, nego oznakom `portable_assets` u inventaru. |
| `scripts/render-book-pdf.ps1`, `scripts/render-book-docx.ps1` | Oba omotača prije rada pozivaju samostalnu blokirajuću provjeru; DOCX očekivane dodatke čita iz izvora. |
| `scripts/check-pdf-release-path.ps1` | Izolirana proba omotača kopira kanonski inventar i njegove potrošače umjesto vlastitoga popisa A–F. |
| `.github/workflows/publish.yml` | Pozitivna provjera i negativne fixture provjere blokiraju prije rendera i Pages koraka, bez `continue-on-error`. |
| `scripts/check-release-governance.R` | Zadržana je njegova zasebna semantička obveza za predobjavni errata-put; generirana Quarto projekcija i dalje sadrži taj već sankcionirani put. Poznati checksum dug ostaje u `H-P1C-EXPORT-002`. |

Ručne poveznice u rukopisu nisu proglašene inventarima niti su prepisivane:
one su sadržajne unakrsne poveznice i njihova bi izmjena prešla granicu ovoga
paketa.

## Jedini sankcionirani izvor i blokirajući ugovor

`config/book-inventory.json` sadrži 37 stranica: naslovnicu, predgovor,
18 brojčanih poglavlja, Literaturu, dodatke A–F te deset samostalnih ili
posebnih stranica. Uz njih bilježi osam stavki navbara, devet putova podnožja,
korijenski javni alias, PDF odredište i nula putova rješenja. Svaki `.qmd` u
korijenu, `chapters/` i `dodaci/` mora pripadati točno jednoj ulozi.

Naredba

```text
python scripts/check-book-inventory.py
```

provjerava shemu, jedinstvenost izvora i izlaza, potpunu jednakost s datotekama
na disku, redoslijed poglavlja 1–18, kontinuirani niz dodataka od A, jednakost
footer-render inventara, javne aliase, potrošače, profile i označene projekcije.
Ne mijenja datoteke. Svaki nesklad završava kodom 1.

Samo svjesna naredba

```text
python scripts/check-book-inventory.py --write
```

obnavlja označene blokove u `_quarto.yml` i `styles/book-include.html`. Dodavanje
ili uklanjanje sankcioniranoga puta zato počinje u jednoj JSON datoteci, nakon
čega se svaka izvedena kopija obnavlja istom naredbom, a nepospremljeni ili
ručno izmijenjeni prikaz blokira. `_quarto.yml` poziva pozitivnu provjeru kao
prvi pre-render korak, pa se isti ugovor primjenjuje na zadani HTML i na svaki
profil. PDF i DOCX omotači ostaju samostalno pozivi; workflow izravno poziva i
pozitivnu i negativnu naredbu.

## Pozitivna i namjerno neuspješna proba

`python scripts/check-book-inventory-fixtures.py` stvara samo privremene kopije.
Pozitivna proba dodala je `fixture-route` u kanonski izvor, njegovu izvornu
datoteku i footer-ulogu, zatim je jednom naredbom obnovila obje projekcije.
Ponovna provjera prihvatila je 38 stranica i desetu footer-stavku:

```text
BOOK_INVENTORY_SYNC_FIXTURE_OK added=fixture-route publish=false
```

Tri neovisne regresije završile su kodom 1:

| Fixture | Namjerni kvar | Blokirajući nalaz |
|---|---|---|
| `missing-route` | `app-f` uklonjen je iz uloge dodatka, ali ne iz sankcioniranih stranica. | Stranica nije dodijeljena točno jednoj ulozi. |
| `extra-route` | U izvor je dodan put bez obnove označenih projekcija. | Generirana projekcija odstupa od izvora. |
| `reordered-route` | Dodaci A i B zamijenili su mjesta. | Niz dodataka više nije kontinuiran i poredan od A. |

Završni primitak bio je:

```text
BOOK_INVENTORY_NEGATIVE_FIXTURES_OK fixtures=3 publish=false
```

Naslijeđena proba PDF omotača također je ostala zelena: pozitivna zamjena
artefakta prolazi, a preflight, neuspjeh build-naredbe i zastarjeli ili
nedostajući artefakt završavaju očekivanim blokiranjem.

## Dokaz iz čiste zaključane okoline

Iz commita `8731a9d62c72264b435b829924e3259b730311b1` stvorena je odvojena
detached radna kopija. `R_LIBS_USER`, R cache, izvorna i binarna spremišta,
npm cache i Playwrightovi preglednici bili su usmjereni u nove prazne
direktorije, uz `RENV_CONFIG_CACHE_ENABLED=FALSE`. Javna naredba
`python scripts/restore-dependencies.py` obnovila je samo zaključane ovisnosti
i završila ovim primicima:

```text
R_RESTORE_OK version=4.6.0 direct_packages=19 detected_packages=22
BROWSER_RESTORE_OK version=1.62.1
DEPENDENCY_RESTORE_OK r_lock=renv.lock playwright=1.62.1 node=24.15.0 npm=11.12.1
```

U istoj čistoj radnoj kopiji prošli su pozitivna provjera, pozitivna sinkronizacija
novoga puta, tri namjerno neuspješne regresije, PDF fixture i sintaktička
provjera pregledničkoga potrošača. Kanonski primitak bio je:

```text
BOOK_INVENTORY_OK pages=37 chapters=19 appendices=6 solutions=0 navbar=8 footer=9 sha256=b2f20bd4c7877cac30cc36117fef5c5f0872ed874e67d674cfd0911333c48e0f
P1C_INVENTORY_CLEAN_PROOF_OK commit=8731a9d62c72264b435b829924e3259b730311b1 worktree_clean=true pages=37 appendices=6 solutions=0 fixtures=3 publish=false
```

`git status --short` bio je prazan prije i poslije svih provjera. Nije pokrenut
render niti bilo kakva javna radnja.

## Stanje implementacijskih datoteka

Stanje `inventory:sha256-1cc773c5...` jest SHA-256 poredanoga manifesta
`putanja<TAB>Git blob` za 13 implementacijskih datoteka na navedenom commitu:

| Putanja | Git blob |
|---|---|
| `.github/workflows/publish.yml` | `1665d3204b3ff5b03be5013516fad864dd940a09` |
| `_quarto.yml` | `5e7e6cb9033ebc3ad5aa94223e86255c95aa6aae` |
| `config/book-inventory.json` | `5f44db7c8dfd92884cb854e28777e22c720606a9` |
| `scripts/book_inventory.py` | `baa994f0771b1041ef67c9cbf954942336c590f2` |
| `scripts/check-book-inventory.py` | `5ecf47f909dd132a9ed44f559fe18b2e124e52b0` |
| `scripts/check-book-inventory-fixtures.py` | `15859f3ce51d1e43d9616f8a552e80b1fd5e06a7` |
| `scripts/check-rendered-html.py` | `2729286cf2e453ddde703fbb2ad9b5a9f2a578e3` |
| `scripts/audit-rendered-html.js` | `62fef2d315a3bbc2764b0a7a9155095b98c8a961` |
| `scripts/embed-404-assets.py` | `282d83559ee0d4fa3f4874d6dcaf9f58340bebeb` |
| `scripts/render-book-pdf.ps1` | `8b1034723428531004503b4cd4fa0f5a63fe6588` |
| `scripts/render-book-docx.ps1` | `fb9bce1e3a830d0d77cfdd7f640b252f71468558` |
| `scripts/check-pdf-release-path.ps1` | `eca4eb39d01a11a3ac2a3cf8431302bcce2538c1` |
| `styles/book-include.html` | `a736e5a11db96941aef40ec4f7624c99affc5360` |

## Budući učinci

Nije otkriven nov budući učinak. Već postojeći `H-P1C-EXPORT-002` točno
predaje predobjavni `_quarto.yml` checksum dug paketima `P7-FREEZE` i
`P8-META`; ponovna provjera `scripts/check-release-governance.R` i dalje
završava samo tim poznatim neskladom. Ovaj paket ga ne duplicira i ne rješava
prije kandidatskoga izvora.

Ratificirani `P5-G` već izravno ovisi o `P1C-INVENTORY`: eventualni D10 Dodatak
G mora se poslije odluke dodati kroz novi kanonski izvor i proći iste pozitivne
i negativne provjere. `P2-ASSESS` i `P5-ROUTES` već imaju
`H-P1C-EXPORT-001` za buduću arhitekturu zaštićenih rješenja. Stoga novi
handoff ne bi dodao informaciju ni promijenio postojeću ovisnost.
