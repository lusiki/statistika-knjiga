# STYLE.md — Osnove statistike za društvene znanosti

Vizualni sustav knjige. Vrijedi jednako za digitalno izdanje (Quarto book) i za
tiskani blok (B5, crno-bijelo). Referentni prikaz: `Statistika — Stil knjige.dc.html`.
Implementacija: `_statistika.scss`.

---

## 1. Načela

1. **Zrak je građa.** Odjeljke razdvaja bjelina i vlas linija (1 px, `#E4DFD2`),
   nikad okvir, sjena ni zaobljena kartica. Vertikalni ritam: 96–104 px između
   glavnih odjeljaka na zaslonu, 7,5 rem prije otvaranja poglavlja.
2. **Oker znači dodir.** Jedina boja naglaska rezervirana je za interakciju i
   navođenje: poveznice, klizači, kartice koda, oznake widgeta, brojevi bilježaka.
   Nikad kao ukras i nikad kao boja podataka.
3. **Crno-bijelo prvo.** Značenje nose debljina linije, položaj i tekstualna
   oznaka. Svaki element mora ostati razumljiv kad se boja oduzme — blok se
   tiska jednobojno.
4. **Brojke su monospace.** Sve brojke u tablicama, izlazima i legendama su
   JetBrains Mono, `tabular-nums lining-nums`.
5. **Mjera prije širine.** Stupac teksta nikad ne prelazi 66 znakova, bez obzira
   na širinu prozora. Sve ostalo raste oko njega.

## 2. Boja

| Uloga | Hex | Napomena |
|---|---|---|
| papir | `#FBFAF6` | nikad čisti bijeli |
| uvučena traka | `#F3EFE6` | sažetci, kod, ispune |
| ploha widgeta | `#FFFFFF` | jedino što „pluta” iznad papira |
| tinta | `#16150F` | naslovi, tamne trake |
| tekst | `#33322A` | tijelo |
| prigušeno | `#6E6C61` | sekundarno |
| slabo | `#9B9789` | potpisi, izvori |
| vlas linija | `#E4DFD2` / `#EFEBE0` | strukturna / meka |
| **oker grafika** | `#C08A16` | crte, ispune, točke |
| **oker tekst** | `#8A6212` | poveznice i oznake (AA na papiru) |
| oker ispuna | `#FAF2DE` | definicije |

**Paleta podataka**, poredana po svjetlini tako da preživi pretvorbu u sivo:
`#16150F` → `#40566B` → `#8A6212` → `#9B9789` → `#C9C2B0`.
Ako serija treba više od pet razina, mijenja se oblik točke ili uzorak ispune,
ne ton.

## 3. Tipografija

| Obitelj | Uloga | Postavke |
|---|---|---|
| **Newsreader** | naslovi, displej, kurzivni citati | rez 300 na velikim veličinama, nikad bold, tracking −0,022em, line-height 1,02–1,2 |
| **Literata** | tijelo teksta | 17 px / 1,62; u tisku 10,5 pt / 14,5 pt |
| **Public Sans** | sučelje, potpisi, margina, izvori | 13–15 px |
| **JetBrains Mono** | kod, brojke, oznake, „eyebrow” | 11–13 px, letter-spacing 0,14–0,16em za oznake |

**Ligature u kodu su isključene** (`font-variant-ligatures: none`). JetBrains
Mono bi inače R-ov `<-` prikazao kao `←`, a `<=` `>=` `!=` `%>%` kao znakove
kojih nema na tipkovnici. Čitatelj bez programerskog iskustva mora moći
prepisati svaki znak koji vidi. Pravilo vrijedi za `pre`, `code` i sve izlaze.

Sve četiri obitelji imaju punu Latin Extended-A podršku (č ć đ š ž).
Ljestvica: H1 68–76 · H2 34 · H3 22–26 · tekst 17 · margina 13 · oznaka 11.

## 4. Repertoar elemenata

Svaki tip okvira razlikuje se **crtom i oznakom**, ne bojom pozadine.

| Element | Oblik | U tisku |
|---|---|---|
| **Vinjeta** | 2 px gornja crta + vlas donja; kurzivni Newsreader 23 px | isto |
| **Definicija / ključni pojam** | 2 px lijeva oker crta + ispuna `#FAF2DE` | crna crta + 4 % siva |
| **Statistika u divljini** | puna tamna traka `#16150F`, bijeli kurzivni navod | bijela ploha s 2 px crnim okvirom |
| **Pitajte model** | 1 px točkasti okvir; prompt u mono na `#F3EFE6` | isto |
| **Česta pogreška** | 3 px gornja crta, bez ispune, oznaka podcrtana okerom | podcrta crna |
| **Razrađeni primjer** | viseći mono brojevi koraka, vlas linija po koraku | isto |
| **Sažetak** | uvučena traka `#F3EFE6`, strelice `→` | isto |
| **Widget** | bijela ploha, vlas okvir, kontrole odvojene linijom na dnu | statična figura, bez kontrola |

## 5. Interakcija

- **Widget** je jedini „plutajući” element. Zaglavlje: naslov + oznaka
  `WIDGET 08.1 · INTERAKTIVNO`. Prikaz na bijelom, kontrole na papirnatoj
  podlozi ispod, podnožje s brojem slike i napomenom za tisak.
- **Kod** je zatvoren (`code-fold: true`). R i Python u karticama, nikad jedan
  ispod drugoga. Aktivna kartica: 2 px oker donji rub.
- **Izvodi** su `<details>`; sažetak počinje s `+` / `–`, mono, oker.
- **Pojmovi** u tekstu nose točkastu oker podcrtu i otkrivaju tamni oblačić s
  definicijom, poveznicom na poglavlje i engleskim terminom.
- **Podaci**: svaki skup ima redak s licencom, brojem ispitanika i preuzimanjem
  CSV-a i kodne knjige.
- Svaka simulacija ima fiksno sjeme (`2026`) da se brojka u prozi i brojka u
  kodu podudaraju.

## 6. Slike i tablice

- Potpis: mono oznaka `SLIKA 8.5` u okeru, zatim rečenica u Public Sansu,
  zatim izvor u mono sivom. Maksimalno 60 znakova širine.
- Tablice: bez okomitih linija, bez zebre. Glava u Public Sansu verzalom,
  crna crta ispod glave i ispod zadnjeg retka. Brojke desno poravnate, mono.
- **Bez zvjezdica značajnosti.** Umjesto njih interval pouzdanosti.

## 7. Mreža

- Zaslon: stupac teksta `minmax(0, 680px)` + margina 220 px, razmak 48 px.
  Ispod 1 000 px margina pada u tijek teksta iza odlomka na koji se odnosi.
- Puna širina stranice: 1 280 px, unutarnji razmak 56 px.
- Tisak B5 (176 × 250 mm): satnica 108 mm, margina 38 mm, vanjski rub 18 mm.

## 8. Otvaranje poglavlja

Puna stranica, bez slike. Redom: `POGLAVLJE 08` (oker mono) i `DIO III · …`
(sivi mono) u istom retku, naslov u Newsreaderu 68 px / rez 300 na najviše 14
znakova širine, uvodna rečenica u Literati 21 px na 52 znaka, pa vlas linija i
red metapodataka: vrijeme čitanja, widget, podaci, preduvjeti.

## 9. Provjera prije predaje poglavlja

- [ ] Nijedan odlomak nije širi od 66 znakova.
- [ ] Svaki widget ima statičnog blizanca i broj slike.
- [ ] Svaka figura čitljiva u sivim tonovima; nijedna legenda ne ovisi o boji.
- [ ] Brojke u prozi = brojke u kodu (isto sjeme).
- [ ] Pojmovi u sažetku postoje u Dodatku E, HR i EN.
- [ ] Nema zvjezdica značajnosti; svaka procjena ima interval.
- [ ] Oker se pojavljuje samo ondje gdje se nešto može dodirnuti.
