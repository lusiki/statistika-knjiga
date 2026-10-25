# DESIGN.md — vizualni sustav knjige

Knjiga *Statistika 101: Intuitivni uvod u analizu podataka* ima identitet koji
se zove **Zvono**. Polazi od korice 02 Zvono: bauhausovska geometrija, mala slova
u displejnom registru i četiri oblika koji ponavljaju jedan statistički motiv,
kupolu normalne raspodjele nad osnovicom, s tankom osi kroz sredinu.

Isti sustav objavljen je kao Claude Design System **Sustav Zvono**
(<https://claude.ai/artifact/CWRe5LJpZksUtzXJfc65Sp>): tokeni, priručnik marke i
osamnaest sastavnica s pregledima. Ovaj dokument je njegova provedbena
specifikacija u repozitoriju. Kad se razilaze, mjerodavan je `design-tokens.yml`,
a Design System i ovaj dokument usklađuju se s njim.

Uredništvena pravila (proza, ton, citiranje) su u [STYLE.md](STYLE.md) i s ovim
se ne preklapaju. Raniji identitet „prozračni uredništveni” ostaje sačuvan u
[knjiga-stil/](knjiga-stil/) i na grani `main` kao referenca.

---

## 1. Pet načela

Ovo nisu preporuke. Svako od njih odlučuje kako izgleda konkretan element i
svako se može provjeriti gledanjem.

1. **Oblik nosi značenje.** Četiri oblika imaju stalne uloge: **kupola** je znak
   knjige, **disk** nosi broj, **os** povezuje i označava sredinu, **osnovica**
   zatvara. Ne uvodi se peti oblik ni ukrasna ilustracija.
2. **Boja je posao.** Oker (`accent`) znači dodir i navođenje. Modra
   (`concept`) gradi pojam. Crvena (`error`) označava grešku. Nijedna nije ukras
   u čitateljskoj zoni i **nijedna nije boja podataka**.
3. **Crno-bijelo prvo.** Svaki element ostaje razumljiv kad se boja oduzme.
   Tiskani blok je jednobojan, pa razliku nose debljina crte, oblik oznake i
   riječ.
4. **Brojke su monospace.** Sve brojke u tablicama, osima, legendama i
   oznakama widgeta su JetBrains Mono, `tabular-nums lining-nums`. Iznimka je
   broj u disku, koji je dio oblika i stoji u Jostu.
5. **Mjera prije širine.** Stupac teksta nikad ne prelazi 66 znakova, bez
   obzira na širinu prozora. Sve ostalo raste oko njega.

### Dvije zone

- **Naslovna zona**: korica, uvodna traka naslovne stranice, stranica dijela i
  naslovni slajd. Paleta nastupa kao velika polja punog tona i ne mijenja se s
  temom: `brand-mustard` podloga, ugniježđene kupole `brand-navy`,
  `brand-cream` i `brand-red`, naslov, disk i osnovica u `brand-ink`. Ovo je
  jedino mjesto gdje crvena ne znači grešku.
- **Čitateljska zona**: poglavlje, widget, tablica, graf i tiskani blok. Boja
  ima posao ili je nema.

Kad nije jasno kojoj zoni ploha pripada, pripada čitateljskoj.

---

## 2. Pravilo četiri datoteke

Dizajn živi na točno četiri mjesta. Nigdje drugdje u repozitoriju nema sirovog
hexa ni imena pisma.

| Datoteka | Sloj | Što nosi |
|----------|------|----------|
| `design-tokens.yml` | **izvor istine** | paleta (imena → hex), tipografija, mjere |
| `styles/_tokens.scss` | web | iste vrijednosti kao SCSS varijable; `styles/_base.scss` ih izlaže kao `var(--tok-*)` |
| `tex/theme.tex` | tisak | iste vrijednosti kao `\definecolor`, plus pisma i naslovi |
| `R/theme_book.R` | grafovi | **čita `design-tokens.yml`** — ne održava se ručno |

Četiri datoteke smiju nositi vrijednosti izvan tog kruga, i svaka ima razlog:

| Datoteka | Zašto |
|----------|-------|
| `styles/_dark.scss` | tamni tokeni — ista imena, druge vrijednosti; `brand-*` se namjerno ne nadjačavaju |
| `styles/head.html` | `theme-color` i favicon čita preglednik, ne stranica |
| `styles/statistika.theme` | Pandoc traži hex u samoj temi bojanja sintakse |
| `styles/statistika-tisak.theme` | ista tema u sivim tonovima za tiskani blok |

Korica u tisku (`tex/korica.tex`) ponavlja `brand-*` vrijednosti jer se prevodi
kao zasebni dokument; mijenja se zajedno s njima.

Sinkronizacija se ne pamti napamet nego provjerava:

```text
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R
```

---

## 3. Boja

Imena tokena opisuju **ulogu**, ne boju. Omjeri kontrasta izmjereni su prema
WCAG 2 na podlozi u zagradi.

| Token | Svijetla | Tamna | Uloga |
|-------|----------|-------|-------|
| `paper` | `#F2E8D5` | `#191814` | stranica; u tisku je papir bijel |
| `paper-soft` | `#E6D9BC` | `#24221C` | uvučene plohe: sažetak, kod, ploča widgeta |
| `surface` | `#FAF5EA` | `#2C2A23` | oblačić pojma, polja za unos |
| `ink` | `#1B1A17` | `#F2E8D5` | naslovi, crte, disk (14,3 : 1) |
| `ink-soft` | `#2F2D28` | `#E2D8C4` | tijelo teksta (11,3 : 1) |
| `ink-mute` | `#4F4A3F` | `#B5AB96` | sekundarno (7,3 : 1) |
| `ink-faint` | `#625B4B` | `#A39985` | potpisi, izvori (5,5 : 1; 4,8 : 1 na `paper-soft`) |
| `rule` | `#CDBF9C` | `#3D392F` | vlas linija |
| `rule-soft` | `#DDD0B2` | `#2F2C25` | meka vlas linija |
| **`accent`** | `#E8B343` | `#E8B343` | oker: ispuna gumba, palac klizača, aktivna stavka |
| `on-accent` | `#1B1A17` | `#191814` | tekst i rub na okeru (9,1 : 1) |
| `accent-deep` | `#7A5A0F` | `#E8B343` | tekst poveznice (5,2 : 1) |
| `accent-dark` | `#4F3A08` | `#F4CF7A` | prijelaz mišem |
| `accent-wash` | `#F6E6BE` | `#3A2F14` | odabir, kod u retku, bljesak promjene |
| **`concept`** | `#1E3F7A` | `#9DB4E0` | modra: os definicije, kupola vinjete, pojam (8,4 : 1) |
| **`error`** | `#D1472F` | `#E86A52` | crvena: znak i crta okvira Nađite grešku (3,7 : 1, samo znak) |
| `alert` | `#9E2F1C` | `#F08A72` | tekst pogreške, pogreška u izlazu koda (6,0 : 1) |

Oker na papiru ima samo 1,6 : 1. Zato ga uvijek prati tinta, rub ili debljina:
aktivna kartica je u `ink` i ima crtu od 3 px, gumb ima rub, palac klizača ima
obrub u `on-accent`. **Krem tekst na okeru nije dopušten.** Fokus tipkovnice je
puna crta od 2 px u `ink`, nikad oker.

**Paleta podataka** poredana je po svjetlini, pa preživi pretvorbu u sivo:

`data-1 #1B1A17` (L* 9) → `data-2 #1E3F7A` (L* 27) → `data-3 #7F6234` (L* 44) →
`data-4 #998F7B` (L* 60) → `data-5 #D2C4A2` (L* 79)

Treba li serija više od pet razina, mijenja se **oblik točke ili uzorak
ispune**, nikad ton. `data-3` je zemljani oker, a ne `accent`, pa ulazi u
obično kodiranje kategorija (`boje_knjige` u R-u). Pravi oker ulazi u graf samo
kroz `skala_naglasak()` i tada znači „pogledajte ovo”. Crvena nikad ne ulazi u
graf.

**Naslovna zona**: `brand-mustard #E8B343`, `brand-navy #1E3F7A`,
`brand-cream #F2E8D5`, `brand-red #D1472F`, `brand-ink #1B1A17`, iste u obje
teme.

---

## 4. Tipografija

Tri obitelji, sve s punom Latin Extended-A podrškom (č ć đ š ž). Web ih učitava
iz `styles/head.html`; PDF i R grafovi učitavaju statičke instance iz
`fonts/print/`.

| Obitelj | Uloga | Postavke |
|---------|-------|----------|
| **Jost** | displej, naslovi, sučelje, potpisi, margina | rez 400 za displej, 500 za naslove, oznake i gumbe; bez reza 700 |
| **Literata** | tijelo teksta, podnaslovi u kurzivu, engleski parovi | 17 px / 1,62; u tisku 10,5 pt / 14,5 pt |
| **JetBrains Mono** | kod, brojke, oznake widgeta | 11–13 px; ligature isključene |

**Mala slova pripadaju samo displejnom registru**: korica, naslovna stranica,
naslov poglavlja (1–18) i dijela. U izvoru naslov ostaje u rečeničnom pismu,
a mala slova postiže stil. Naslovi odjeljaka, oznake i gumbi ostaju u
rečeničnom pismu; oznaka okvira piše se verzalom kroz stil. Dodaci ne idu u mala
slova jer bi „R praktikum” postao „r praktikum”.

Ljestvica na zaslonu: naslov poglavlja `clamp(2,5 – 4 rem)` · h2 1,75 rem s
crtom od 3 px iznad · h3 1,25 rem · tekst 1,0625 rem · potpis 0,8125 rem ·
oznaka 0,75 rem · mono oznaka 0,6875 rem.

**Ligature u kodu su isključene** (`font-variant-ligatures: none`, u LaTeX-u
`Ligatures = ResetAll`). JetBrains Mono bi inače R-ov `<-` prikazao kao `←`, a
`<=` `>=` `!=` `%>%` kao znakove kojih nema na tipkovnici. Čitatelj bez
programerskog iskustva mora moći prepisati svaki znak koji vidi.

### Pisma za PDF

`tex/theme.tex` učitava `Jost-Regular`, `Jost-Medium` i `Jost-Italic` te
Literatu i JetBrains Mono iz `fonts/print/`. Nepostojanje datoteke zaustavlja
gradnju umjesto da neopaženo promijeni izgled. Podrijetlo i licence su u
`fonts/print/README.md`.

---

## 5. Repertoar elemenata

Svaki tip kutije razlikuje se **oblikom, crtom i oznakom**. Boja pojačava, ali
ne nosi razliku. Oznaku kategorije ispisuje CSS; u `.qmd`-u se ne upisuje.

| Element | Klasa | Na zaslonu | U tisku |
|---------|-------|------------|---------|
| **Otvaranje poglavlja** | naslovni blok | disk s brojem (88 px), os do naslova, oznaka dijela, naslov malim slovima, podnaslov u kurzivu, crta od 3 px | disk, os 0,8 pt, naslov malim slovima, crta 1,2 pt |
| **Uvodni slučaj** | `.callout-vinjeta` | modra kupola 28 × 14 px, modra gornja crta 2 px, vlas donja, bez oznake; pitanje vinjete u Jostu 500 | crna kupola, crta 0,8 pt |
| **Definicija** | `::: {#def-…}` | modra lijeva os 4 px, bez ispune, pojam u Jostu 500 modrom; oznaka „Definicija N” samo za čitače zaslona | crna os 1,6 pt, bez oznake |
| **Statistika u divljini** | `.callout-divljina` | puna ploha `ink` u stupcu teksta, krem disk u oznaci, naslov slučaja u Jostu 500 | crna gornja traka 2,4 pt, bez plohe |
| **Pitajte model** | `.callout-model` | točkasti okvir, upit u monou | isto |
| **Nađite grešku** | `.callout-greska` | crvena zdjelica 22 × 11 px, crvena gornja crta 2 px; tekst oznake u `ink` | crna zdjelica, crta 0,8 pt |
| **Razrađeni primjer** | `##` odjeljak · `.primjer` | obični odjeljak; `.primjer` daje korake s diskom | isto, crno |
| **Sažetak** | `## … {.sazetak}` | ploha `paper-soft`, crta od 3 px u `ink` | crta 1,2 pt, bez plohe |
| **Pojmovi** | `## … {.pojmovi}` | HR lijevo u Literati, EN desno u kurzivu | isto |
| **Zadaci** | `### … {.zadaci-razina}` | disk s rednim brojem razine, mono brojevi zadataka `01`, `02` | isto |
| **Widget** | `.widget-frame` | ploča `paper-soft`, osnovica 6 px, disk s brojem widgeta, kontrole ispod vlas linije | statična figura, bez kontrola |
| **Tablica** | — | glava u Jostu 500 s crtom 2 px, retci vlas linijom, brojke mono desno | isto |
| **Gumb** | `.btn-knjiga` | pravi kut, rub 2 px, najmanje 44 px; `.primarni` puna tinta | — |

Razrađeni primjer je po [STYLE.md](STYLE.md) obični `##` odjeljak, ne kutija.
Klasa `.primjer` postoji za slučaj kad se analiza doista raspada na numerirane
korake; tada `###` podnaslovi postaju koraci s diskom.

### Pojam s definicijom na dodir

```markdown
…počiva cijelo [statističko zaključivanje]{.pojam
  def="Izvođenje tvrdnji o populaciji na temelju uzorka."
  en="statistical inference" ch="8"}.
```

U tekstu modra točkasta podcrta od 2 px. Oblačić je `surface` s modrom gornjom
crtom; gradi ga `styles/book-include.html` iz atributa. U PDF-u filter pretvara
pojam u kurziv, a engleski termin u bilješku uz vanjski rub. Ovo **ne**
zamjenjuje `#def-` div: samo `#def-` divovi ulaze u pojmovnik i graf pojmova
(`R/build-concept-graph.R`).

### Početak bez metapodatkovne trake

Poglavlja nemaju traku s vremenom čitanja, podacima, widgetom i preduvjetima.
Podaci se uvode običnim odlomkom prije prve uporabe. Uvodni slučaj nema
ispisanu oznaku „Vinjeta”.

### Widget

```markdown
::: {.widget-frame data-naslov="Stroj za CLT" data-oznaka="Widget 08.1 · interaktivno"}
```{ojs}
…
```
:::
```

Zaglavlje s diskom („08.1”), naslovom i oznakom gradi `styles/book-include.html`
iz atributa. Bez JS-a pseudo-elementi ispisuju naslov i oznaku.

---

## 6. Mreža

- **Zaslon.** Stupac teksta 680 px, margina 260 px, sidebar 280 px, razmak
  2,2 rem. Mjeru od 66 znakova drži `--tok-measure`, ne širina stupca — stupac
  je okvir, mjera je pravilo. Ispod 1 000 px margina pada u tijek teksta iza
  odlomka na koji se odnosi.
- **Tisak.** B5, 176 × 250 mm. Unutarnji rub 22 mm, vanjski 33 mm, gore
  21 mm, dolje 23 mm; bilješke uz rub 25 mm.
- **Crte.** vlas 1 px (0,4 pt) · os 2 px (0,8 pt) · naslov 3 px (1,2 pt) ·
  definicija 4 px (1,6 pt) · osnovica 6 px (2,4 pt).
- **Kutovi.** Sve plohe imaju pravi kut. Krug i kupola su oblici, ne
  zaobljenja. Nema sjena ni gradijenata osim onih kojima se crtaju oblici.

---

## 7. Otvaranje poglavlja i naslovna zona

**Poglavlje.** Na webu skripta u `html-filters/systemic-layout.lua` numeriranim
poglavljima dodaje disk s dvoznamenkastim brojem i os, a iznad naslova oznaku
„Poglavlje 8 · Dio III · Od uzorka do populacije” iz putokaza. Naslov je u
Jostu 400 malim slovima, podnaslov (YAML `subtitle:`) u kurzivu Literate, a blok
zatvara crta od 3 px. U tisku isto, crno-bijelo.

**Naslovna stranica weba.** Uvodna traka je oker polje s kompozicijom Zvono
desno: disk „101”, tri ugniježđene kupole, os i osnovica. Kompoziciju crta CSS iz
`brand-*` tokena na praznom divu `.hero-zvono`, pa nema slike koju bi trebalo
održavati.

**Korica.** `tex/korica.tex` crta koricu u formatu B5 iz `brand-*` vrijednosti
i prevodi se u `images/korica.pdf`; `images/cover.png` je njezin rasterski
prikaz za dijeljenje. Tiskani PDF počinje koricom, a unutrašnjost ostaje
crno-bijela.

---

## 8. Kako se dizajn mijenja

1. Uredite `design-tokens.yml` — paletu i obitelji pisama.
2. Uskladite `styles/_tokens.scss` i `tex/theme.tex` (iste vrijednosti,
   iste `token:` oznake).
3. Ako se mijenjaju pisma, uskladite `styles/head.html`, blok pisama u
   `tex/theme.tex`, statičke instance u `fonts/print/` i učitavanje u
   `R/theme_book.R`.
4. Pregledajte `styles/_dark.scss` — tamni tokeni se ne izvode automatski.
5. Ako se mijenja paleta, uskladite obje `.theme` datoteke bojanja sintakse i
   `tex/korica.tex`.
6. Provjera tokena mora proći bez razlike.
7. Uskladite Claude Design System **Sustav Zvono** (`tokens.json`), da drugi
   materijali ostanu na istom sustavu.
8. Pregled: naslovnica, jedno poglavlje s widgetom, pojmovnik, tamni način,
   korica i nekoliko stranica PDF-a.

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
- [ ] Oker se pojavljuje samo ondje gdje se nešto može dodirnuti, crvena samo
      uz grešku, modra samo uz pojam.

---

## 10. Što je namjerno izostavljeno

- **Slika za dijeljenje poveznice** (Open Graph) još nije uključena u
  `_quarto.yml`, iako `images/cover.png` postoji.
- **Word rukopis** (`scripts/render-book-docx.ps1`) nasljeđuje boje i pisma iz
  zadanog predloška; nema vlastiti Zvono predložak.
