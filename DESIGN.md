# DESIGN.md — kako se zadaje i mijenja vizualni identitet knjige

Ovaj repozitorij je namjerno isporučen **bez vizualnog identiteta**. Sva
mehanika dizajna postoji i radi, ali su vrijednosti neutralni placeholder
(bijeli papir, sistemska pisma, jedna plava). Knjiga se renderira od prvog
dana, a identitet se doda kasnije bez diranja ijednog poglavlja.

Postoje tri načina da se to ne napravi ovako, i svaki je gori. Kopirati
dizajn prethodne knjige znači da ga poslije treba čupati iz dvije tisuće
redaka CSS-a. Isporučiti repozitorij bez stilskih datoteka znači da ništa
ne radi dok se dizajn ne odabere. Držati boje raspršene po komponentama
znači da svaka promjena postaje pretraga po cijelom stablu. Postavka ispod
izbjegava sva tri.

---

## Pravilo četiri datoteke

Dizajn živi na točno četiri mjesta. Nigdje drugdje u repozitoriju nema
sirovog hexa ni imena pisma.

| Datoteka | Sloj | Što nosi |
|----------|------|----------|
| `design-tokens.yml` | **izvor istine** | paleta (imena → hex), tipografija, veličine |
| `styles/_tokens.scss` | web | iste vrijednosti kao SCSS varijable i `var(--tok-*)` svojstva |
| `tex/theme.tex` | tisak | iste vrijednosti kao `\definecolor`, plus pisma i naslovi |
| `R/theme_book.R` | grafovi | **čita `design-tokens.yml`** — ne održava se ručno |

`styles/_dark.scss` je peta iznimka i jedini drugi legitiman nositelj boja:
invertirani tokeni za tamni način. Ista imena, druge vrijednosti.

Sinkronizacija se ne pamti napamet nego provjerava:

```bash
Rscript scripts/check-tokens.R
```

Skripta uspoređuje `design-tokens.yml` s oba preslikana sloja po oznakama
`# token:<ime>` u komentarima, ispisuje svaku razliku s brojem retka i
usput prijavi svaki sirovi hex koji se ušuljao u neku komponentu. Vrti se
i u CI-ju kao neblokirajući korak.

---

## Tokeni i njihove uloge

Imena tokena opisuju **ulogu**, ne boju, pa preživljavaju svaku promjenu
palete. Komponenta koja traži „akcent" dobiva ga i kad akcent iz plave
postane bakrena.

| Token | Uloga | Gdje se vidi |
|-------|-------|--------------|
| `paper` | pozadina stranice | tijelo, navbar, sidebar |
| `paper-soft` | elevirana ploha | kutije, blokovi koda, upravljačke ploče grafova |
| `ink` | tijelo teksta i naslovi | proza |
| `ink-soft` | sekundarni tekst | uvodi, opisi u kutijama |
| `ink-mute` | tercijarni tekst | natpisi, opisi slika, živa pagina |
| `ink-faint` | vlasne crte | separatori, mreža u grafovima |
| `accent` | **primarna radnja** | poveznice, gumbi, klizači, kutija „Pitajte model" |
| `accent-deep` | hover i tisak | naslovi odjeljaka u PDF-u |
| `accent-wash` | vrlo blaga podloga akcenta | istaknuta kutija, oznaka varijable u tekstu |
| `emphasis` | naglasak i upozorenje | kutije „Statistika u divljini" i „Nađite grešku" |
| `archival` | treći akcent | kutija „Vinjeta", crte iznad naslova dijelova |

Tipografija ima tri registra, ne više: `serif` (proza i naslovi), `sans`
(sučelje, natpisi, oznake kutija, tablice) i `mono` (kod, brojke, oznake
varijabli).

---

## Kako zadati novi dizajn

Tri načina, po rastućoj preciznosti. Svaki završava istim korakom:
uređivanjem `design-tokens.yml` pa `Rscript scripts/check-tokens.R`.

### 1. Gotov dizajnerski paket

Najbrži put. Spustite paket u `design/` (CSS s varijablama, izvoz iz Figme,
stilski priručnik u PDF-u, čak i snimku zaslona referentne stranice) i
recite koja datoteka vrijedi. Mapiranje na jedanaest tokena gore je
mehanički posao. Ovaj je repozitorij nastao iz knjige čiji je identitet
došao upravo tako, kao paket s paletom i tipografijom koji je preslikan u
`design-tokens.yml`.

### 2. Ispunjen brief

Kad paketa nema, ispunite obrazac na dnu ove datoteke. Deset polja,
nijedno ne traži poznavanje CSS-a. Iz ispunjenog briefa slijedi paleta,
tipografija i tretman naslova bez daljnjih pitanja.

### 3. Referenca

Najmanje precizno, ali korisno kao polazište. Navedite dvije ili tri knjige,
udžbenika ili mrežna mjesta čiji vam se izgled sviđa i recite što točno na
njima. Iz toga se izvodi prijedlog palete i tipografije koji onda potvrđujete
ili odbijate.

---

## Postupak zamjene, korak po korak

1. Uredite `design-tokens.yml` — paletu i tri obitelji pisama.
2. Uskladite `styles/_tokens.scss` i `tex/theme.tex` (iste vrijednosti,
   iste `token:` oznake).
3. Ako pisma nisu sistemska:
   - u `_quarto.yml` otključajte `include-in-header` blok i upišite Google
     Fonts poveznicu (ili lokalno pismo);
   - stavite statičke instance u `fonts/print/` i otključajte `\setmainfont`
     blok u `tex/theme.tex`.
4. Pregledajte `styles/_dark.scss` — tamni tokeni se ne izvode automatski.
5. `Rscript scripts/check-tokens.R` mora proći bez razlike.
6. `quarto preview` i pregled: naslovnica, jedno poglavlje s widgetom,
   pojmovnik, tamni način.

Nijedan `.qmd` se u tom postupku ne dira. To je i mjerilo je li postavka
ispravna: ako promjena dizajna traži uređivanje poglavlja, negdje je
procurio sirovi hex.

---

## Što je namjerno izostavljeno

- **Naslovnica** (`cover.png`) i **favicon**. Redci su u `_quarto.yml`
  zakomentirani; otključavaju se kad datoteke postoje.
- **Slika za dijeljenje poveznice** (Open Graph). Ista priča.
- **Pisma.** Nema `fonts/print/*.ttf`, pa PDF gradi na Latin Modernu i radi
  na svakom stroju bez ijednog preuzimanja.

---

## Brief — obrazac

Kopirajte u `design/brief.md` i ispunite. Prazna polja su u redu; iz njih
slijedi prijedlog umjesto odluke.

```
1.  UGOĐAJ. Tri pridjeva. Što knjiga treba odavati na prvi pogled?
2.  REFERENCE. Dvije do tri knjige ili stranice, i što točno na njima.
3.  PAPIR. Bijelo, toplo krem, hladno sivo ili nešto drugo?
4.  TEKST. Klasična crna, topla tamna ili hladna tamna?
5.  AKCENT. Jedna boja koja nosi poveznice i gumbe. Ako imate hex, upišite ga.
6.  NAGLASAK. Boja za upozorenje i za kutiju „Statistika u divljini".
7.  TREĆI TON. Boja za vinjete i crte iznad dijelova knjige.
8.  PISMA. Serif za prozu, sans za sučelje, mono za kod i brojke.
    Ako nemate izbor, recite samo registar (npr. „suvremeno, ne akademski").
9.  NASLOVI POGLAVLJA. Mirno i tipografski, ili s natpisom i crtom, ili s
    brojem poglavlja kao velikim znakom?
10. TAMNI NAČIN. Treba li ga uopće biti, i je li ravnopravan svijetlom?
11. TISAK. Jedna boja ili dvije, i je li papir u PDF-u obojan ili bijel?
12. GRAFOVI. Boja i u tisku ili sivi tonovi? (Web ostaje u boji.)
```
