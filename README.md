# Osnove statistike za društvene znanosti

Quarto knjiga — udžbenik statistike za studente društvenih znanosti koji moraju
razumjeti istraživanje, a ne postati analitičari.

### 📖 &nbsp;Knjiga uživo → **<https://lusiki.github.io/statistika-knjiga/>**

[![Render and deploy](https://github.com/lusiki/statistika-knjiga/actions/workflows/publish.yml/badge.svg)](https://github.com/lusiki/statistika-knjiga/actions/workflows/publish.yml)

Stranica se ponovno gradi sama pri svakom pushu na `main`; PDF radne verzije
stoji na [`/pdf/Statistika.pdf`](https://lusiki.github.io/statistika-knjiga/pdf/Statistika.pdf).

**Stanje: kostur.** Cijeli pogon radi (build, izvozi, PDF, CI, uređivački
alati) i knjiga ima vizualni identitet. Nijedno poglavlje još nema sadržaj —
ono što je na stranici je struktura, ne tekst. Plan knjige je
[notes/struktura-knjige.md](notes/struktura-knjige.md).

## Prvo pokretanje

```bash
# 1. R okruženje (jednom)
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/init-renv.R

# 2. pregled u pregledniku
quarto preview
```

Ako Quarto javi da nedostaje R paket, pokrenite korak 1. Sve što knjiga koristi
je u `scripts/init-renv.R`.

## Naredbe

| Naredba | Što radi |
|---------|----------|
| `quarto preview` | živi pregled |
| `quarto render` | cijela knjiga u `docs/` |
| `quarto render --profile kolegij` | nastavno izdanje u `docs-kolegij/`, kod otvoren, rješenja vidljiva |
| `powershell -File scripts/render-book-pdf.ps1` | `pdf/Statistika.pdf` |
| `powershell -File scripts/render-book-docx.ps1` | `word/Statistika.docx`, rukopis za lekturu |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R` | jesu li slojevi dizajna usklađeni |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-ai-exports.R` | tekstualni izvoz knjige za AI asistente |
| `python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-concept-graph.R` | mreža pojmova za pojmovnik |

PDF i DOCX **ne** pokreću se golim `quarto render --profile …`. Quarto spaja
popise dodataka aditivno, pa profil ne može skratiti popis; PowerShell skripte
privremeno prepišu `_quarto.yml` i uvijek ga vrate.

## Gdje što stoji

| Želim… | Idem u… |
|--------|---------|
| pisati poglavlje | `chapters/` — kostur je već tu, pravila su u `STYLE.md` |
| promijeniti izgled | `DESIGN.md`, pa `design-tokens.yml` |
| dodati interaktivni graf | `widgets/README.md` i `data/widgets.json` |
| dodati podatke | `R/fetch-podaci.R` i `dodaci/c-katalog-podataka.qmd` |
| promijeniti redoslijed poglavlja | `_quarto.yml` |
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
- [STYLE.md](STYLE.md) — uređivački stil, tvrda pravila H1–H9, meka S1–S9
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

## Objava

Knjiga je na <https://lusiki.github.io/statistika-knjiga/>.

Push na `main` pokreće [`.github/workflows/publish.yml`](.github/workflows/publish.yml),
koji renderira knjigu, pokuša PDF (neblokirajuće, stari ostaje ako padne) i
objavi `docs/` na GitHub Pages. Izvor za Pages je **GitHub Actions**, ne grana —
`docs/` u repozitoriju je samo urezani zadnji build, ne ono što se poslužuje.

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
uređivački alati; izgled nije prenesen, namjerno.
