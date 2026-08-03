# Osnove statistike za društvene znanosti

Quarto knjiga — udžbenik statistike za studente društvenih znanosti koji moraju
razumjeti istraživanje, a ne postati analitičari.

### 📖 &nbsp;Radna mrežna inačica → **<https://lusiki.github.io/statistika-knjiga/>**

[![Render and deploy](https://github.com/lusiki/statistika-knjiga/actions/workflows/publish.yml/badge.svg)](https://github.com/lusiki/statistika-knjiga/actions/workflows/publish.yml)

Workflow je podešen da pri svakom pushu na `main` ponovno izgradi radnu
stranicu; poveznica na razvojni PDF je
[`/pdf/Statistika.pdf`](https://lusiki.github.io/statistika-knjiga/pdf/Statistika.pdf).

**Stanje: sadržajni nacrt u sveobuhvatnoj reviziji.** Predgovor i svih 18
numeriranih poglavlja imaju tekst i zajedničke strukturne sastavnice, ali svih
19 jedinica još ima status `draft`. Mrežna inačica, PDF i DOCX razvojni su
artefakti, a ne objavljeno izdanje. Opseg i plan knjige opisani su u
[notes/struktura-knjige.md](notes/struktura-knjige.md).

## Licenca

Izvorni autorski tekst, programski kod i pridružena dokumentacija u ovom
repozitoriju dostupni su pod MIT licencom iz datoteke [LICENSE](LICENSE).
Skupovi podataka i drugi materijali trećih strana zadržavaju zasebno označene
uvjete; tehnički pristup ne znači dopuštenje za preraspodjelu.
Generirani nastavni skupovi `anketa_mreze` i `populacija_medija` te njihove
buduće datotečne snimke dostupni su pod [CC BY 4.0](data/LICENCA-generirani-podaci.md).
Ta licenca podataka ne mijenja MIT licencu koda koji ih stvara.

## Lokalni pregled

Repozitorij još nema `renv.lock`, pa ponovljiva čista instalacija R ovisnosti
nije zaključana. `scripts/init-renv.R` pripremni je instalacijski skript, a ne
potpun ugovor o obnovi okruženja. Ako su Quarto i potrebne R ovisnosti već
dostupni, pregled se pokreće ovako:

```bash
quarto preview
```

## Naredbe

| Naredba | Što radi |
|---------|----------|
| `quarto preview` | lokalni pregled knjige |
| `quarto render` | razvojni HTML build u `docs/` |
| `quarto render --profile kolegij` | nastavni profil u `docs-kolegij/`, sa svim kodom otvorenim |
| `powershell -File scripts/render-book-pdf.ps1` | razvojni PDF u `pdf/Statistika.pdf` i njegova kopija u `docs/pdf/` |
| `powershell -File scripts/render-book-docx.ps1` | razvojni rukopis u `word/Statistika.docx` |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R` | jesu li slojevi dizajna usklađeni |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-ai-exports.R` | tekstualni izvoz knjige za AI asistente |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-concept-graph.R` | mreža pojmova za pojmovnik |

PDF i DOCX **ne** pokreću se golim `quarto render --profile …`. PDF omotač
provjerava kanonski popis literature i dodataka A–F, pokreće PDF profil te
kopira rezultat u `docs/pdf/`. DOCX omotač tijekom rendera privremeno isključuje
pre-render hook i zamjenjuje vrata statičkih slika; `finally` blok vraća
konfiguraciju i izvore i ako render ne uspije.

## Gdje što stoji

| Želim… | Idem u… |
|--------|---------|
| uređivati nacrt poglavlja | `chapters/` — pravila su u `STYLE.md` |
| promijeniti izgled | `DESIGN.md`, pa `design-tokens.yml` |
| dodati interaktivni graf | `widgets/README.md` i `data/widgets.json` |
| provjeriti pravila za podatke | `data/README.md`, `R/fetch-podaci.R` i `dodaci/c-katalog-podataka.qmd` |
| provjeriti kanonski redoslijed | `_quarto.yml` i `notes/struktura-knjige.md` |
| napraviti prezentaciju | `predavanja/README.md` |
| razumjeti cjelinu | `AGENTS.md` |

## Dizajn

Identitet knjige zove se **prozračni uredništveni**: topao papir, jedan oker
akcent koji uvijek znači „ovo se može dodirnuti", knjižni serif i crno-bijeli
tiskani blok u formatu B5.

Pet načela — zrak je građa · oker znači dodir · crno-bijelo prvo · brojke su
monospace · mjera prije širine. Puna specifikacija, repertoar elemenata i
postupak zamjene su u [DESIGN.md](DESIGN.md); izvorni paket iz kojeg je
preslikan stoji u `knjiga-stil/`.

Dizajn živi u točno četiri datoteke, a `design-tokens.yml` je izvor istine.
Sinkronizaciju slojeva provjerava
`python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R`.

## Pisanje

- [AGENTS.md](AGENTS.md) — zajednički operativni priručnik za Codex i Claude Code
- [CLAUDE.md](CLAUDE.md) — Claude Code ulaz koji učitava `AGENTS.md`
- [STYLE.md](STYLE.md) — uređivački stil, tvrda pravila H1–H10, meka S1–S9
- [ENRICHMENT.md](ENRICHMENT.md) — kako se poglavlje produbljuje
- [notes/struktura-knjige.md](notes/struktura-knjige.md) — plan knjige

Sva proza je na hrvatskom (hr-HR).

## Uređivački alati

`bookwright_plugin/` je mali uređivački tim za Codex i Claude Code koji živi uz repozitorij: voditelj
koji prati stanje poglavlja, provjera stila s R linterom, produbljivanje,
provjera uvoda uz slike, panel kritičara po poglavlju i provjera dosljednosti
kroz cijelu knjigu. Nije build ovisnost. Upute su u
`bookwright_plugin/README.md`.

Codex instalacija iz korijena repozitorija:

```powershell
codex plugin marketplace add .
codex plugin add bookwright@statistika-local
```

Nakon instalacije ili nadogradnje otvorite novu dretvu kako bi Codex učitao
vještine. Claude Code koristi lokalni marketplace u `bookwright_plugin/`;
točne naredbe za oba domaćina i razvojni postupak nadogradnje nalaze se u
`bookwright_plugin/README.md`.

## Razvojna objava

Radna mrežna inačica podešena je za
<https://lusiki.github.io/statistika-knjiga/>. Ta adresa i razvojni artefakti
nisu dokaz objavljenog izdanja.

Push na `main` pokreće [`.github/workflows/publish.yml`](.github/workflows/publish.yml),
koji renderira knjigu, pokuša PDF i objavi `docs/` na GitHub Pages. PDF korak
trenutačno je neblokirajući, pa pri njegovu neuspjehu može ostati prethodno
urezani PDF. Izvor za Pages je **GitHub Actions**, ne grana; `docs/` u
repozitoriju jest urezani razvojni build, ali nije sam po sebi dokaz onoga što
se poslužuje.

Ručno pokretanje bez pusha ide preko kartice Actions („Run workflow") ili:

```bash
gh workflow run publish.yml
gh run watch
```

Adresa je upisana na tri mjesta i mijenja se zajedno: `site-url` i `repo-url` u
`_quarto.yml`, `link` u `design-tokens.yml`, `SITE_URL` u `R/build-ai-exports.R`.

## Podrijetlo

Pogon je prenesen iz knjige *Javne politike u Hrvatskoj* i prilagođen ovoj
temi. Preneseni su build, izvozi za AI, mreža pojmova, PDF i DOCX lanac, CI i
uređivački alati; sadašnji prozračni uredništveni identitet zasebno je preslikan
i dokumentiran u `DESIGN.md`.
