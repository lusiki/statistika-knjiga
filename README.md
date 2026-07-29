# Osnove statistike za društvene znanosti

Quarto knjiga — udžbenik statistike za studente društvenih znanosti koji moraju
razumjeti istraživanje, a ne postati analitičari.

**Stanje: kostur.** Cijeli pogon radi (build, izvozi, PDF, CI, uređivački
alati). Nijedno poglavlje još nema sadržaj. Plan knjige je
[notes/struktura-knjige.md](notes/struktura-knjige.md).

## Prvo pokretanje

```bash
# 1. R okruženje (jednom)
Rscript scripts/init-renv.R

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
| `Rscript scripts/check-tokens.R` | jesu li slojevi dizajna usklađeni |
| `Rscript R/build-ai-exports.R` | tekstualni izvoz knjige za AI asistente |
| `Rscript R/build-concept-graph.R` | mreža pojmova za pojmovnik |

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
| razumjeti cjelinu | `CLAUDE.md` |

## Dizajn

Knjiga **još nema vizualni identitet**. Paleta i tipografija su namjerno
neutralni placeholder, pa se sve renderira i radi, ali ništa ne izgleda gotovo.

Dizajn živi u točno četiri datoteke, a `design-tokens.yml` je izvor istine. Postupak
zamjene i obrazac za brief su u [DESIGN.md](DESIGN.md).

## Pisanje

- [CLAUDE.md](CLAUDE.md) — operativni priručnik, kostur poglavlja, konvencije
- [STYLE.md](STYLE.md) — uređivački stil, tvrda pravila H1–H9, meka S1–S9
- [ENRICHMENT.md](ENRICHMENT.md) — kako se poglavlje produbljuje
- [notes/struktura-knjige.md](notes/struktura-knjige.md) — plan knjige

Sva proza je na hrvatskom (hr-HR).

## Uređivački alati

`bookwright_plugin/` je mali uređivački tim koji živi uz repozitorij: voditelj
koji prati stanje poglavlja, provjera stila s R linterom, produbljivanje,
provjera uvoda uz slike, panel kritičara po poglavlju i provjera dosljednosti
kroz cijelu knjigu. Nije build ovisnost. Upute su u
`bookwright_plugin/README.md`.

## Objava

Push na `main` pokreće `.github/workflows/publish.yml`, koji renderira knjigu,
pokuša PDF (neblokirajuće) i objavi `docs/` na GitHub Pages.

Prije prve objave zamijenite radne vrijednosti na četiri mjesta: `site-url` u
`_quarto.yml`, `link` u `design-tokens.yml`, `SITE_URL` u `R/build-ai-exports.R` i
konstantu `UPUTA` u `styles/book-include.html`.

## Podrijetlo

Pogon je prenesen iz knjige *Javne politike u Hrvatskoj* i prilagođen ovoj
temi. Preneseni su build, izvozi za AI, mreža pojmova, PDF i DOCX lanac, CI i
uređivački alati; izgled nije prenesen, namjerno.
