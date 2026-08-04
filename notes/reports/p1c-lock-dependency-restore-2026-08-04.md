# P1C-LOCK: zaključavanje R i pregledničkih ovisnosti

**Paket:** `P1C-LOCK`

**Stavka:** `R05-LOCK-renv`

**Datum provjere:** 4. kolovoza 2026.
**Dokazani izvor:** `945e7ccd1ba32985c0429cc166b5233d93b58cdb`

## Granica paketa

Paket uvodi samo mehanizam zaključavanja i obnove R i pregledničkih
ovisnosti. Ne mijenja preglednički test, PDF put, provjere integriteta,
izvoze, paritet widgeta ni inventare. Stoga su
`scripts/audit-rendered-html.js`, PDF omotači i njihove kasnije izlazne
provjere ostali izvan promjene.

`H-P1B-META-001` prihvaćen je prije prve implementacijske izmjene. Privremeno
upozorenje u README-u uklonjeno je tek nakon uspješne hladne obnove opisane u
nastavku.

## Zaključani ugovor

- R je zaključan na 4.6.0, a `renv` na 1.2.4. `renv.lock` sadržava 64 zapisa;
  `scripts/init-renv.R` izričito provjerava 19 izravnih paketa i sve ovisnosti
  otkrivene u izvorima. U studentskim primjerima koji se ne izvršavaju
  `tidyverse` je namjerno označen kao izuzeti metapaket; izvršne sastavnice
  zaključane su pojedinačno.
- Node je zaključan na 24.15.0, npm na 11.12.1, a Playwright i
  `playwright-core` na 1.62.1 s integritetima registra u
  `package-lock.json`. Playwrightova instalacija iz tog zapisa dohvaća
  Chromium reviziju 1234 (Chrome for Testing 151.0.7922.34).
- `python scripts/restore-dependencies.py` jedina je javna naredba za obnovu.
  Provjerava lockfileove i inačice alata, pokreće R obnovu bez pričuvnog puta,
  izvodi `npm ci`, instalira zaključani Chromium i provjerava stvarnu inačicu
  paketa i postojanje izvršne datoteke preglednika.
- CI sada uvijek koristi R 4.6.0 i `setup-renv` iz `renv.lock`; uklonjene su
  detekcija lockfilea i ad hoc grana `setup-r-dependencies`. Node se uzima iz
  `.node-version`, a preglednički paket isključivo iz `package-lock.json`.
  Postojeći neblokirajući PDF i token koraci namjerno ostaju za svoje zasebne
  pakete.

Zajednički SHA-256 kanonskih Git blobova ugovora jest
`aaf12f9d337efd342cf13a6db37d30b437cf351e19b6c68a78ae528fbabf49e8`.
Najvažniji SHA-256 zapisi u hladnoj Windows radnoj kopiji bili su:

| Datoteka | SHA-256 |
|---|---|
| `renv.lock` | `0ab8728a4d51ffc1e5de68e754bd93ab48a01fa8854562edee89dfc5c04cdf48` |
| `package-lock.json` | `542ba5dcc6ea50d98926004c39174efa065cc4e9e6294ad7bb8a2e9a815b8d57` |
| `renv/activate.R` | `a36f28f84219b6b9a89c4e5eb365a0f44d2f01f4fb9cfedb0940d1cc7d09103a` |
| `renv/settings.json` | `f2ffa05d630950bd286591fd2337c57c8a40a17c450f97243817cc9ec8cb7950` |

## Pozitivna hladna obnova

Odvojena radna kopija stvorena je izravno iz commita `945e7cc`. Prije
pokretanja javne naredbe usmjereni su:

- R biblioteka, cache, izvorne i binarne pohrane u nove prazne direktorije;
- `RENV_CONFIG_CACHE_ENABLED=FALSE` i novi `R_LIBS_USER`;
- npm cache u novi prazni direktorij;
- `PLAYWRIGHT_BROWSERS_PATH` u novi prazni direktorij.

Naredba `python scripts/restore-dependencies.py` dohvatila je i instalirala 63
zaključana R paketa bez cachea, provjerila 19 izravnih i 22 iz izvora
otkrivena paketa, izvela čisti `npm ci`, preuzela Chromium reviziju 1234 u
novi direktorij te završila zapisima:

```text
R_RESTORE_OK version=4.6.0 direct_packages=19 detected_packages=22
BROWSER_RESTORE_OK version=1.62.1
DEPENDENCY_RESTORE_OK r_lock=renv.lock playwright=1.62.1 node=24.15.0 npm=11.12.1
```

`git status --short` nakon obnove nije vratio nijedan zapis. Time je potvrđeno
da obnova ne treba `_freeze`, postojeću projektnu biblioteku, node_modules,
topli cache, nepraćenu datoteku ni razvojnu instalaciju paketa.

## Namjerno neuspješna provjera

Isti commit pokrenut je s memorijskom fixturom koja mehanizmu zadaje
nepostojeći preglednički lockfile, bez promjene kanonskih datoteka:

```text
python scripts/restore-dependencies.py --fixture missing-browser-lock
dependency restore: missing committed browser lockfile: fixtures\missing-package-lock.json
EXPECTED_FAILURE fixture=missing-browser-lock exit=2
```

Neuspjeh se događa prije mrežnog ili instalacijskog rada i ne postoji
nezaključana pričuvna grana.

## Budući učinak

`P1C-BROWSER` mora rabiti ovaj manifest, lockfile i instalirani Playwrightov
preglednik umjesto sadašnjeg `NODE_PATH` i tvrdo zadane lokalne putanje do
Chromea. `P7-FREEZE` mora preuzeti ove kanonske lockfileove i njihove hashove
u evidenciju kandidata za izdanje. Ti su učinci zapisani u
`H-P1C-LOCK-001`; nijedan od tih kasnijih paketa nije započet.
