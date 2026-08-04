# P1C-BROWSER: zaključana prijenosna preglednička provjera

**Paket:** `P1C-BROWSER`

**Stavka:** `R18-BROWSER-runtime`

**Datum provjere:** 4. kolovoza 2026.

**Dokazani implementacijski izvor:**
`8b04c6cec15972d85416f4d9b2cd5f49a8776d3e`

**Stanje paketa:**
`browser-smoke:sha256-c76a872c9bbf374c3ed9e28b8f952636bbad2448bdfbb0a265494bc941c03ba7`

## Granica paketa

Paket uvodi samo blokirajuću pregledničku provjeru najvažnije interakcijske
putanje u već renderiranom HTML-u. Ne uvodi paritet widgeta, nove zlatne
vrijednosti, inventare, katalog podataka, izvoze, politiku vrednovanja,
izmjene poglavlja ni opću pregledničku ili asistivno-tehnološku pokrivenost.
Postojeća potpuna snimkovna provjera ostaje zaseban ručni dijagnostički način.

`H-P1C-LOCK-001` potrošen je prije zahtjeva za paketom. Njegova je odluka
provedena bez izmjene `package.json`, `package-lock.json`, `.node-version`,
`renv.lock` ili `scripts/restore-dependencies.py` u odnosu na prihvaćeni
commit `945e7cc`.

## Provedeni ugovor

- `scripts/audit-rendered-html.js` izravno razrješava Playwright iz
  repozitorijeva `node_modules/playwright`; `NODE_PATH` se ne čita niti je
  potreban.
- Preglednik se pokreće s `chromium.launch({ headless: true })`, bez
  `executablePath` i bez lokalne putanje do Chromea. Prije pokretanja audit
  usklađuje manifest, lockfile, instaliranu inačicu Playwrighta, Node pin,
  Chromiumovu reviziju i stvarnu izvršnu datoteku.
- Neovisno poziva naredba
  `node scripts/audit-rendered-html.js --smoke --root docs`. Ona podiže vlastiti
  HTTP poslužitelj samo na `127.0.0.1` i ne treba prethodno pokrenut servis.
- Provjera na Poglavlju 7 tipkovnicom otvara sklopivu upravljačku ploču,
  mijenja klizač, provjerava neispraznu pristojnu živu regiju, tipkovnicom
  vraća početnu vrijednost i tipkovnicom prebacuje tamni način. Zatim na
  širinama 1280 i 390 piksela provjerava vidljiv widget i izostanak vodoravnog
  prelijevanja.
- Potpuni ručni način istoga audita sada također rabi zaključani lokalni
  Playwright i instalirani Chromium, ali nije proširen niti uključen kao
  blokirajuća opća provjera.
- `scripts/check-browser-smoke-fixtures.py` poziva istu javnu smoke naredbu s
  namjerno nepostojećom rutom i prolazi samo ako audit završi nenultim statusom
  zbog HTTP-a 404.
- Objavni workflow nakon `npm ci` instalira Chromium iz zaključanog
  Playwrightova paketa. Pozitivna i negativna preglednička provjera izvode se
  nakon HTML rendera i statičke provjere, a prije konfiguriranja i predaje
  Pages artefakta. Koraci su blokirajući i nemaju `continue-on-error` ni
  pričuvni preglednik.

## Čista zaključana provjera

Odvojena radna kopija izrađena je izravno iz commita `8b04c6c`. R biblioteka i
cache, npm cache, `node_modules` i `PLAYWRIGHT_BROWSERS_PATH` bili su novi i
prazni. Javna naredba `python scripts/restore-dependencies.py` obnovila je R
4.6.0, npm 11.12.1, Playwright 1.62.1 i Chromium reviziju 1234. Dokazna kopija
nije rabila razvojni `node_modules`, postojeći preglednik, `_freeze` ni topli
cache.

Namjerno je postavljen i nepostojeći `NODE_PATH`; pozitivna je provjera ipak
razriješila Playwright iz dokazne kopije i završila zapisima:

```text
BROWSER_RUNTIME_OK node=24.15.0 playwright=1.62.1 chromium_revision=1234
BROWSER_SMOKE_OK route=/chapters/07-vjerojatnost.html widths=1280,390 themes=light,dark keyboard=pass reset=pass live_region=pass publish=false
P1C_BROWSER_CLEAN_PROOF_OK commit=8b04c6c publish=false worktree_clean=true
```

`git status --short` ostao je prazan nakon obnove i obje provjere.

## Namjerni neuspjeh

Ista čista zaključana kopija pokrenula je pregledničku fixturu:

```text
BROWSER_AUDIT_FAILED mode=smoke fixture=missing-route: browser path returned HTTP 404
EXPECTED_FAILURE fixture=missing-route exit=1
BROWSER_SMOKE_NEGATIVE_FIXTURES_OK fixtures=1 publish=false
```

Time je potvrđeno da nepostojeća ili pogrešna preglednička putanja blokira
proces i da nema prelaska na drugi URL, preglednik ili lokalno stanje.

## Dodatne provjere

- `node --check scripts/audit-rendered-html.js` prošao je.
- Pythonova sintaktička provjera fixture-harnessa prošla je.
- `python scripts/check-rendered-html.py docs` provjerio je svih 36 kanonskih
  stranica prije smoke audita.
- Pretraga implementacijskih datoteka vratila je nula pojava `NODE_PATH`,
  razvojne Chrome putanje i ručnog `executablePath` argumenta.
- Git usporedba s `945e7cc` potvrdila je da su svih pet prihvaćenih lock i
  restore ulaza nepromijenjeni.
- `scripts/check-review-workflow.R` prošao je s praznim aktivnim paketom i
  `P1C-PARITY` kao sljedećim dopuštenim paketom. Fixture
  `generic_packet_evidence` i fixture `invalid_outside_ask_link` zasebno su
  završile statusom 1 iz očekivanih razloga.
- Nije pokrenut upload, Pages konfiguracija, deployment ni druga objava.

## Budući učinak

Paket nije otkrio novi budući učinak. Potpuna semantička pristupačnost,
šira tipkovnička i responsive matrica te dokaz artefakta već imaju zasebne
pakete `P7-A11Y` i `P7-HTML`; paritet i inventari ostaju u
`P1C-PARITY` i `P1C-INVENTORY`. Zato se ne stvara novi izlazni handoff.
