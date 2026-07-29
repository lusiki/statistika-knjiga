# knjiga-stil

Vizualni sustav za **Osnove statistike za društvene znanosti** — digitalno
izdanje (Quarto book) i tiskani blok (B5, crno-bijelo) iz jednog izvora.

Kopirajte cijelu mapu `knjiga-stil/` u korijen repozitorija knjige. Ništa u njoj
ne treba mijenjati da bi radila; sve što se mijenja po poglavlju živi izvan nje.

---

## Instalacija u tri koraka

**1. Kopirajte mapu.**

```
vasa-knjiga/
├── knjiga-stil/          ← ova mapa, nepromijenjena
├── poglavlja/
├── dodaci/
├── slike/
├── index.qmd
└── _quarto.yml
```

**2. Preuzmite `_quarto.yml`.** Otvorite `knjiga-stil/_quarto.yml` i kopirajte
njegov sadržaj u `_quarto.yml` u korijenu. Popis poglavlja prilagodite svojemu;
sve ostalo ostavite.

**3. Provjerite.**

```bash
quarto preview
```

Ako se prikaže topla bijela stranica s okernim naglascima, sustav radi.

---

## Što je u mapi

| Datoteka | Uloga |
|---|---|
| `_quarto.yml` | Cjelovita konfiguracija: HTML + PDF, hrvatski nizovi, mreža, `code-fold` |
| `scss/_statistika.scss` | Tema. Boje, tipografija, svi `.st-*` elementi, pravila za tisak |
| `css/statistika-extras.css` | Ono što SCSS ne može: oblačići pojmova, margina, OJS widgeti |
| `filters/statistika.lua` | Pretvara `::: {.definicija}` i ostale blokove u HTML **i** u LaTeX |
| `html/head.html` | Fontovi (Google Fonts) |
| `html/foot.html` | Traka napretka, pamćenje stanja widgeta, pojmovi na dodir |
| `statistika.theme` | Bojanje sintakse za R, Python i OJS — tiho, čitljivo u sivom |
| `tisak/preamble.tex` | B5 blok: `scrbook`, fontovi, svi okviri kao LaTeX okruženja |
| `R/theme_statistika.R` | `theme_statistika()` + palete + `spremi_figuru()` |
| `python/statistika_style.py` | Isto za matplotlib, znak za znak jednako |
| `predlosci/poglavlje.qmd` | Kostur poglavlja sa svim elementima — kopirajte i pišite preko |
| `STYLE.md` | Pisana specifikacija i kontrolni popis prije predaje poglavlja |

---

## Elementi u tekstu

Sve se piše kao obični Quarto blok. Filter ga pretvori i za web i za tisak.

```markdown
::: {.vinjeta}
U studenome 2024. agencija je objavila da 34 % građana vjeruje Crkvi.
:::

::: {.definicija term="Distribucija uzorkovanja" en="sampling distribution"}
Distribucija neke statistike preko svih mogućih uzoraka zadane veličine.
:::

::: {.divljina claim="Podrška je porasla za 3 boda." source="portal, 2025."}
Margina pogreške odnosi se na jednu procjenu, ne na razliku dviju.
:::

::: {.pitajte prompt="Objasni razliku između SD i SE na mojim podacima."}
Asistent dobro objašnjava SE. Loše procjenjuje reprezentativnost uzorka.
:::

::: {.pogreska}
Interval pouzdanosti od 95 % ne znači da je vjerojatnost 95 %…
:::

::: {.widget id="08.1" title="Stroj za CLT" fig="8.4" static="slike/08-clt.svg"}
```{ojs}
…
```
:::

::: {.sazetak}
- Jedan uzorak daje jednu procjenu.
:::

::: {.primjer}
### Pitanje
### Podaci
### Model
:::

::: {.zadaci}
### Pojmovno
### Računski
### Kritički
### Revizija modela
:::

::: {.pojmovi}
| distribucija uzorkovanja | sampling distribution |
:::
```

Pojam u rečenici:

```markdown
…počiva cijelo [statističko zaključivanje]{.pojam
  def="Izvođenje tvrdnji o populaciji na temelju uzorka."
  en="statistical inference" ch="8"}.
```

Samo za zaslon ili samo za tisak: `::: {.samo-zaslon}` i `::: {.samo-tisak}`.

---

## Figure

**R**

```r
source("knjiga-stil/R/theme_statistika.R")
ucitaj_fontove()
postavi_temu()

p <- ggplot(ess, aes(dob, povjerenje)) +
  geom_point() +
  labs(title = "Povjerenje pada s dobi", caption = "Izvor: ESS HR 2023")

spremi_figuru(p, "08-clt")   # → slike/08-clt.svg + .pdf
```

**Python**

```python
from knjiga_stil.python.statistika_style import postavi_stil, PALETA, izvor
postavi_stil()
```

Svaki widget mora imati statičnog blizanca s istim sjemenom (`2026`) na putanji
navedenoj u atributu `static=`. U tisku filter ubaci njega, a OJS ćeliju izbaci.

---

## Fontovi

Newsreader · Literata · Public Sans · JetBrains Mono — sve s Google Fontsa,
sve s punom hrvatskom dijakritikom (č ć đ š ž).

Za web ništa ne treba: `html/head.html` ih učitava. Za PDF ih instalirajte
lokalno (`~/.fonts` ili Font Book), jer `lualatex` čita sistemske fontove.

**Ligature u kodu su isključene.** JetBrains Mono bi inače R-ov `<-` prikazao
kao `←`. Čitatelj bez programerskog iskustva mora moći prepisati svaki znak.

---

## Dva profila

Iz istog izvora:

```bash
quarto render                    # cijela knjiga, HTML + PDF
quarto render --to html          # samo digitalno izdanje
quarto render --to pdf           # samo tiskani blok, B5
```

Za kolegij dodajte `_quarto-kolegij.yml` s `code-fold: false` i seminarskim
materijalima; poglavlja ostaju iste datoteke.

---

## Prije predaje poglavlja

Kontrolni popis je u `STYLE.md`, odjeljak 9. Ukratko: mjera 66 znakova, svaki
widget ima blizanca, svaka figura čitljiva u sivom, brojke u prozi jednake
brojkama u kodu, nigdje zvjezdica značajnosti, oker samo ondje gdje se nešto
može dodirnuti.
