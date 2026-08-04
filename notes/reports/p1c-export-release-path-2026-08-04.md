# P1C-EXPORT: blokirajući javni AI izvoz

**Paket:** `P1C-EXPORT`

**Stavka:** `R05-EXPORT-failclosed`

**Datum provjere:** 4. kolovoza 2026.

**Dokazani implementacijski izvor:**
`ac7c34fb6723b1e232674cec3b9ce4bddf7e2f00`

**Kanonski sažetak implementacije i generiranih izvoznih artefakata:**
`3453f828e47b5d3895295b7dd092de730cbe7e0eda7c0fc8cdc1ddd7fde9b4de`

## Granica paketa

Nijedan obvezni dolazni handoff nije ciljao `P1C-EXPORT`. Paket mijenja samo
samostalnu naredbu AI izvoza, njezin release ugovor, objavni workflow,
izolirane fixture provjere i iz te naredbe svježe generirane javne artefakte.
Nisu mijenjani rukopis, dodaci, zaštićena rješenja, nastavna politika,
inventari, katalog podataka, paritet widgeta ni preglednički audit. Nije
pokrenut upload, Pages deployment, objava ni druga vanjska radnja.

## Implementirani release put

- `R/build-ai-exports.R --release` ostaje samostalno pozivljiv i za svaku
  pogrešku vraća nenulti status. Lokalni Quarto pre-render bez release oznake
  ostaje best-effort kako se time ne bi neizravno proširio ovaj paket.
- Objavni workflow prije HTML rendera poziva blokirajuću izgradnju i fixture
  dokaz, a nakon rendera poziva `--release --validate-only`. Nema
  `continue-on-error`, stale pričuvnog puta ni pretvaranja pogreške u
  upozorenje.
- Release izvoz zahtijeva svako poglavlje 00–18 deklarirano u `_quarto.yml`,
  točan skup očekivanih javnih Markdown artefakata, manifest i obje
  `llms*.txt` datoteke. Neočekivani stari `.md` artefakt u `docs/ai/` također
  blokira release.
- Svaki `content-visible` blok s atributom `when-profile` isključuje se iz
  javnoga izvoza. Audit pregledava 19 poglavlja i sve dodatke te uspoređuje
  normalizirani sadržaj svih 20 trenutačnih zaštićenih regija s javnim
  izlazima.
- Naslov i predobjavno stanje dolaze iz `release/governance.yml`. Autori,
  opis i mrežna adresa dolaze iz njegova deklariranog
  `book.authorship_source`, trenutačno `_quarto.yml`. Izvoz sada svugdje
  navodi Luku Šikića i Petru Palić te prekida rad ako se kanonski radni
  naslov i naslov autorskoga izvora raziđu.

Svježa release izgradnja zapisala je 19 poglavlja, šest paketa dijelova,
57.302 riječi i manifest sa stanjem `pre_release`. Naknadna validacija
potvrdila je 20 zaštićenih regija i isti kanonski metapodatkovni lanac:

```text
AI_EXPORT_RELEASE_OK chapters=19 protected_regions=20 governance=pre_release
AI_EXPORT_RELEASE_VALIDATION_OK chapters=19 protected_regions=20 governance=pre_release
```

## Zaključana čista provjera

Iz commita `ac7c34f` stvorena je detached radna kopija. R biblioteka i cache,
R izvorna i binarna pohrana, npm cache i Playwrightovi preglednici usmjereni
su u nove prazne direktorije. Javna naredba
`python scripts/restore-dependencies.py` obnovila je i provjerila R 4.6.0,
19 izravnih i 22 iz izvora otkrivena paketa, Node 24.15.0, npm 11.12.1,
Playwright 1.62.1 i Chromium reviziju 1234:

```text
R_RESTORE_OK version=4.6.0 direct_packages=19 detected_packages=22
BROWSER_RESTORE_OK version=1.62.1
DEPENDENCY_RESTORE_OK r_lock=renv.lock playwright=1.62.1 node=24.15.0 npm=11.12.1
```

Release izlaz zapisan je izvan radne kopije. Pozitivna izgradnja, naknadna
validacija i sve tri negativne fixture provjere prošle su na točnom commitu;
radna kopija ostala je bez praćenih izmjena:

```text
P1C_EXPORT_CLEAN_PROOF_OK commit=ac7c34fb6723b1e232674cec3b9ce4bddf7e2f00 worktree_clean=true chapters=19 protected_regions=20 fixtures=3 publish=false
```

`renv::status()` pritom je informativno označio pet zaključanih, instaliranih
ali trenutačno neupotrijebljenih tranzitivnih paketa. Javna obnova svejedno je
uspješno provjerila zaključane inačice i nije uporabila toplu projektnu
biblioteku, cache, nepratenu datoteku ni razvojnu instalaciju.

## Namjerno neuspješne provjere

`python scripts/check-ai-export-fixtures.py` radi samo u privremenim kopijama
i ne objavljuje. Svaki namjerni kvar završio je kodom 1:

| Fixture | Namjerni kvar | Dokazani ishod |
|---|---|---|
| `build-error` | uklonjeno deklarirano poglavlje 18 | nedostajuće poglavlje blokira izvoz |
| `metadata-drift` | naslov u autorskom izvoru razilazi se s governance naslovom | metapodatkovni nesklad blokira izvoz |
| `protected-content-leak` | tijelo zaštićenoga rješenja dodano u `llms-full.txt` | audit nalazi curenje i blokira validaciju |

```text
EXPECTED_FAILURE fixture=build-error exit=1
EXPECTED_FAILURE fixture=metadata-drift exit=1
EXPECTED_FAILURE fixture=protected-content-leak exit=1
AI_EXPORT_NEGATIVE_FIXTURES_OK fixtures=3 publish=false
```

## Budući učinci i rizik

- `H-P1C-EXPORT-001` predaje `P2-ASSESS` i `P5-ROUTES` obvezu da budući D06
  i svaki drugi nastavni ili rješenjski put ostane izvan ulaza javnoga AI
  izvoza ili unutar profilnoga `content-visible` bloka te da ponovno prođe
  pozitivnu i leak fixture provjeru.
- `H-P1C-EXPORT-002` bilježi ranije postojeći checksum-rizik za `P8-META`:
  `release/provenance.yml` za `_quarto.yml` navodi SHA-256 `080dc1c5…`, dok
  čisti praćeni blob ima SHA-256 `a43fabaf…`. Zbog toga
  `scripts/check-release-governance.R` u čistoj kopiji trenutačno vraća 1.
  Ovaj paket ne mijenja governance manifest; njegov vlastiti release izvoz
  provjerava vrijednosti iz kanonskog izvora i prolazi. Rizik se mora
  ukloniti pri zamrzavanju konačnih metapodataka, bez konkurentskog izvora.

Nije pronađen drugi budući učinak. `P1C-BROWSER`, `P1C-PARITY`,
`P1C-INVENTORY` i svi kasniji paketi ostali su nepokrenuti.
