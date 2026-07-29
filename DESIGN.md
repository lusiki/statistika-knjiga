# DESIGN.md — vizualni sustav knjige

Knjiga ima identitet. Zove se **prozračni uredništveni** (*airy editorial*):
topao papir, jedan oker akcent, knjižni serif i crno-bijeli tiskani blok.
Izvorni paket iz kojeg je preslikan stoji u [knjiga-stil/](knjiga-stil/) i
služi kao referenca; radna implementacija živi u datotekama opisanima ispod.

Ovaj dokument je specifikacija. Uredništvena pravila (proza, ton, citiranje)
su u [STYLE.md](STYLE.md) i s ovim se ne preklapaju.

---

## 1. Pet načela

Ovo nisu preporuke. Svako od njih odlučuje kako izgleda konkretan element, i
svako se može provjeriti gledanjem.

1. **Zrak je građa.** Odjeljke razdvaja bjelina i vlas linija (1 px, `rule`),
   nikad okvir, sjena ni zaobljena kartica. Vertikalni ritam je 4,5 rem između
   glavnih odjeljaka na zaslonu, 6 redaka prije otvaranja poglavlja.
2. **Oker znači dodir.** Jedina boja naglaska rezervirana je za interakciju i
   navođenje — poveznice, klizači, kartice koda, oznake widgeta, brojevi
   bilježaka. Nikad kao ukras i **nikad kao boja podataka**.
3. **Crno-bijelo prvo.** Značenje nose debljina linije, položaj i tekstualna
   oznaka. Svaki element mora ostati razumljiv kad se boja oduzme — blok se
   tiska jednobojno.
4. **Brojke su monospace.** Sve brojke u tablicama, izlazima i legendama su
   JetBrains Mono, `tabular-nums lining-nums`.
5. **Mjera prije širine.** Stupac teksta nikad ne prelazi 66 znakova, bez
   obzira na širinu prozora. Sve ostalo raste oko njega.

---

## 2. Pravilo četiri datoteke

Dizajn živi na točno četiri mjesta. Nigdje drugdje u repozitoriju nema
sirovog hexa ni imena pisma.

| Datoteka | Sloj | Što nosi |
|----------|------|----------|
| `design-tokens.yml` | **izvor istine** | paleta (imena → hex), tipografija, mjere |
| `styles/_tokens.scss` | web | iste vrijednosti kao SCSS varijable i `var(--tok-*)` svojstva |
| `tex/theme.tex` | tisak | iste vrijednosti kao `\definecolor`, plus pisma i naslovi |
| `R/theme_book.R` | grafovi | **čita `design-tokens.yml`** — ne održava se ručno |

Četiri datoteke smiju nositi vrijednosti izvan tog kruga, i svaka ima razlog:

| Datoteka | Zašto |
|----------|-------|
| `styles/_dark.scss` | invertirani tokeni za tamni način — ista imena, druge vrijednosti |
| `styles/head.html` | `theme-color` čita preglednik, ne stranica, pa ne može kroz CSS varijablu |
| `styles/statistika.theme` | Pandoc traži hex u samoj temi bojanja sintakse |
| `styles/statistika-tisak.theme` | ista tema u sivim tonovima za tiskani blok |

Sinkronizacija se ne pamti napamet nego provjerava:

```bash
Rscript scripts/check-tokens.R
```

Skripta uspoređuje `design-tokens.yml` s oba preslikana sloja po oznakama
`# token:<ime>` u komentarima, ispisuje svaku razliku s brojem retka i usput
prijavi svaki sirovi hex koji se ušuljao u neku komponentu. Vrti se i u CI-ju
kao neblokirajući korak.

---

## 3. Boja

Imena tokena opisuju **ulogu**, ne boju, pa preživljavaju svaku promjenu
palete.

| Token | Hex | Uloga |
|-------|-----|-------|
| `paper` | `#FBFAF6` | stranica — topla, nikad čisto bijela |
| `paper-soft` | `#F3EFE6` | uvučene trake: sažetak, kod, ispune |
| `surface` | `#FFFFFF` | ploha widgeta — jedino što „pluta" iznad papira |
| `ink` | `#16150F` | naslovi, tamne trake |
| `ink-soft` | `#33322A` | tijelo teksta |
| `ink-mute` | `#6E6C61` | sekundarno |
| `ink-faint` | `#9B9789` | potpisi, izvori |
| `rule` | `#E4DFD2` | strukturna vlas linija |
| `rule-soft` | `#EFEBE0` | meka vlas linija |
| **`accent`** | `#C08A16` | oker grafika: crte, ispune, točke, klizači |
| **`accent-deep`** | `#8A6212` | oker tekst i poveznice (AA na papiru, 5,1:1) |
| `accent-dark` | `#5C4109` | prijelaz mišem |
| `accent-wash` | `#FAF2DE` | ispuna definicija |
| `alert` | `#8A2A12` | pogreška u ispisu koda — jedina druga boja u sustavu |

**Paleta podataka** je poredana po svjetlini, ne po tonu, tako da preživi
pretvorbu u sivo:

`data-1 #16150F` → `data-2 #40566B` → `data-3 #8A6212` → `data-4 #9B9789` →
`data-5 #C9C2B0`

Treba li serija više od pet razina, mijenja se **oblik točke ili uzorak
ispune**, nikad ton. Oker u grafu smije se pojaviti samo kroz
`skala_naglasak()`, i tada znači „gledajte ovo", ne „ovo je kategorija A".

Tamni način invertira iste uloge (`styles/_dark.scss`): papir postaje topla
tama `#14130E`, oker se posvjetljuje u `#D9A62E`, paleta podataka obrće smjer.

---

## 4. Tipografija

Četiri registra, sva četiri s punom Latin Extended-A podrškom (č ć đ š ž).
Web ih učitava iz `styles/head.html`; PDF ih traži u sustavu.

| Obitelj | Uloga | Postavke |
|---------|-------|----------|
| **Newsreader** | naslovi, otvaranje poglavlja, kurzivni navodi | rez 300 na velikim veličinama, **nikad bold**, tracking −0,022em, line-height 1,02–1,14 |
| **Literata** | tijelo teksta | 17 px / 1,62; u tisku 10,5 pt / 14,5 pt |
| **Public Sans** | sučelje, potpisi, margina, izvori, glave tablica | 13 px |
| **JetBrains Mono** | kod, brojke, oznake, „eyebrow" | 11–13 px, letter-spacing 0,14–0,16em za oznake |

Ljestvica: H1 clamp(2,4 – 3,6 rem) · H2 2,125 rem · H3 1,4 rem · tekst
1,0625 rem · margina 0,8125 rem · oznaka 0,6875 rem.

**Ligature u kodu su isključene** (`font-variant-ligatures: none`, u LaTeX-u
`Ligatures = ResetAll`). JetBrains Mono bi inače R-ov `<-` prikazao kao `←`,
a `<=` `>=` `!=` `%>%` kao znakove kojih nema na tipkovnici. Čitatelj bez
programerskog iskustva mora moći prepisati svaki znak koji vidi. Pravilo
vrijedi za `pre`, `code`, sve izlaze i sve slajdove.

### Pisma za PDF

`tex/theme.tex` traži pisma u sustavu preko `\IfFontExistsTF`. Ako ih nema,
blok se **tiho gradi na Latin Modernu** — PDF nikad ne pada zbog pisma, samo
izgubi identitet. Instalacija je opisana u `fonts/print/README.md`; za pun
tiskani izgled trebaju Newsreader i Literata (Public Sans i JetBrains Mono su
neobavezni i učitavaju se ako postoje).

---

## 5. Repertoar elemenata

Svaki tip kutije razlikuje se **crtom i oznakom**, ne bojom pozadine. Oznaku
kategorije ispisuje CSS; u `.qmd`-u se ne upisuje.

| Element | Klasa | Oblik na zaslonu | U tisku |
|---------|-------|------------------|---------|
| **Vinjeta** | `.callout-vinjeta` | 2 px gornja crta + vlas donja, displejni kurziv 22 px | isto |
| **Definicija** | `::: {#def-…}` | 2 px lijeva oker crta + ispuna `accent-wash` | crna crta + 4 % siva |
| **Statistika u divljini** | `.callout-divljina` | puna tamna traka `ink`, navod u bijelom kurzivu | bijela ploha s 1,6 pt crnim okvirom |
| **Pitajte model** | `.callout-model` | 1 px točkasti okvir; upit u monou na `paper-soft` | isto |
| **Nađite grešku** | `.callout-greska` | 3 px gornja crta, bez ispune, oznaka podcrtana okerom | podcrta crna |
| **Razrađeni primjer** | `##` odjeljak · `.primjer` | u pravilu obični `##` odjeljak; klasa `.primjer` daje viseće mono brojeve koraka i vlas liniju po koraku | isto |
| **Sažetak** | `## … {.sazetak}` | uvučena traka `paper-soft`, strelice `→` | isto |
| **Pojmovi** | `## … {.pojmovi}` | HR lijevo u serifu, EN desno u sansu kurzivom | isto |
| **Zadaci** | `### … {.zadaci-razina}` | vlas linija po razini, mono brojevi `01`, `02` | isto |
| **Widget** | `.widget-frame` | bijela ploha, vlas okvir, kontrole odvojene linijom na dnu | statična figura, bez kontrola |

Razrađeni primjer je po [STYLE.md](STYLE.md) obični `##` odjeljak, ne kutija.
Klasa `.primjer` postoji za slučaj kad se analiza doista raspada na numerirane
korake; tada `###` podnaslovi postaju koraci `01`, `02`, `03`.

Upit u „Pitajte model" piše se kao obični blok citat i CSS ga pretvara u mono
traku, pa `.qmd` ne nosi ni jedan sirovi `<div>`:

```markdown
::: {.callout-model}
Asistent dobro objašnjava standardnu pogrešku. Loše procjenjuje je li uzorak
reprezentativan — to ne može znati iz podataka koje mu date.

> Objasni razliku između SD i SE na mojim podacima. Navedi pretpostavke.
:::
```

### Pojam s definicijom na dodir

```markdown
…počiva cijelo [statističko zaključivanje]{.pojam
  def="Izvođenje tvrdnji o populaciji na temelju uzorka."
  en="statistical inference" ch="8"}.
```

Oblačić gradi `styles/book-include.html` iz atributa; u PDF-u filter pretvara
pojam u kurziv, a engleski termin u bilješku uz vanjski rub. Ovo **ne**
zamjenjuje `#def-` div: samo `#def-` divovi ulaze u pojmovnik i graf pojmova
(`R/build-concept-graph.R`).

### Traka metapodataka poglavlja

```markdown
::: {.chapter-meta}
| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 28 min | Stroj za CLT | ESS HR 2023 | pogl. 4, 7 |
:::
```

Tablica se pri učitavanju pretvara u jedan mono redak ispod naslova poglavlja.

### Widget

```markdown
::: {.widget-frame data-naslov="Stroj za CLT" data-oznaka="Widget 08.1 · interaktivno"}
```{ojs}
…
```
:::
```

---

## 6. Mreža

- **Zaslon.** Stupac teksta 680 px, margina 260 px, sidebar 280 px, razmak
  2,2 rem. Mjeru od 66 znakova drži `--tok-measure`, ne širina stupca — stupac
  je okvir, mjera je pravilo. Ispod 1 000 px margina pada u tijek teksta iza
  odlomka na koji se odnosi.
- **Tisak.** B5, 176 × 250 mm. Unutarnji rub 22 mm, vanjski 38 mm, gore
  22 mm, dolje 25 mm; bilješke uz rub 28 mm. Vanjski je rub širok namjerno:
  prima izvore, engleske termine i sitne figure.

---

## 7. Otvaranje poglavlja

Puna stranica, bez slike. Redom: oznaka `POGLAVLJE 08` u okernom monou,
naslov u Newsreaderu u rezu 300 na najviše 16 znakova širine, uvodna rečenica
(YAML `subtitle:`) u Literati na 54 znaka, pa vlas linija i traka
metapodataka — vrijeme čitanja, widget, podaci, preduvjeti.

U tisku isto, bez okera: oznaka je u tinti, crta je vlas siva.

---

## 8. Kako se dizajn mijenja

1. Uredite `design-tokens.yml` — paletu i četiri obitelji pisama.
2. Uskladite `styles/_tokens.scss` i `tex/theme.tex` (iste vrijednosti,
   iste `token:` oznake).
3. Ako se mijenjaju pisma, uskladite `styles/head.html` (poveznica na
   Google Fonts) i blok `\setmainfont` u `tex/theme.tex`.
4. Pregledajte `styles/_dark.scss` — tamni tokeni se ne izvode automatski.
5. Ako se mijenja paleta, uskladite i obje `.theme` datoteke bojanja sintakse.
6. `Rscript scripts/check-tokens.R` mora proći bez razlike.
7. `quarto preview` i pregled: naslovnica, jedno poglavlje s widgetom,
   pojmovnik, tamni način.

Nijedan `.qmd` se u tom postupku ne dira. To je i mjerilo je li postavka
ispravna: ako promjena dizajna traži uređivanje poglavlja, negdje je procurio
sirovi hex.

---

## 9. Provjera prije predaje poglavlja

- [ ] Nijedan odlomak nije širi od 66 znakova.
- [ ] Svaki widget ima statičnog blizanca i broj slike.
- [ ] Svaka figura čitljiva u sivim tonovima; nijedna legenda ne ovisi o boji.
- [ ] Brojke u prozi = brojke u kodu (isto sjeme, 2026).
- [ ] Pojmovi u sažetku postoje u Dodatku E, HR i EN.
- [ ] Nema zvjezdica značajnosti; svaka procjena ima interval.
- [ ] Oker se pojavljuje samo ondje gdje se nešto može dodirnuti.

---

## 10. Što je namjerno izostavljeno

- **Naslovnica** (`cover.png`) i **favicon**. Redci su u `_quarto.yml`
  zakomentirani; otključavaju se kad datoteke postoje.
- **Slika za dijeljenje poveznice** (Open Graph). Ista priča.
- **Statičke instance pisama** u `fonts/print/`. PDF radi bez njih, na Latin
  Modernu; s njima dobiva pun tiskani izgled.
