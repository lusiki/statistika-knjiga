# UPUTE-IZVORNIK.md — upute iz izvornog paketa dizajna

> **Ovo NISU radne upute repozitorija.** Datoteka se izvorno zvala `CLAUDE.md`
> i preimenovana je da se ne učitava kao projektne upute: pretpostavlja drugačiji
> raspored mapa (`poglavlja/`, `slike/`) i drugačija imena klasa nego što knjiga
> stvarno koristi. Radne upute su u `CLAUDE.md` u korijenu, specifikacija
> vizualnog sustava u `DESIGN.md`, uredništvena pravila u `STYLE.md`.
>
> Sadržaj ispod ostavljen je nepromijenjen kao zapis o izvorniku.

Upute za svakog asistenta koji piše ili uređuje poglavlja ove knjige.
Vizualni sustav je zatvoren i nije predmet pregovora: `knjiga-stil/STYLE.md`
je specifikacija, `knjiga-stil/README.md` je priručnik za uporabu.

## Knjiga

Udžbenik statistike za studente društvenih znanosti bez matematičke i
programerske pozadine. Čitatelj koji mora **razumjeti** istraživanje, ne
čitatelj koji mora postati analitičar. Jezik: hrvatski. Ton: prijateljski,
podučavateljski, prvo lice množine u zajedničkim koracima.

Pet načela: simulacija prije formula · procjena umjesto rituala · pismenost kao
sadržaj · računanje u pregledniku · umjetna inteligencija kao alat i kao predmet.

## Kostur poglavlja — nepromjenjiv

1. Vinjeta · 2. Izgradnja pojma · 3. Interakcija · 4. Statistika u divljini
5. Pitajte model · 6. Razrađeni primjer · 7. Sažetak, pojmovi i četiri razine
zadataka (pojmovno, računski, kritički, revizija modela).

Predložak: `knjiga-stil/predlosci/poglavlje.qmd`. Kopirajte ga, ne izmišljajte
strukturu.

## Pravila pisanja

- **Bez zvjezdica značajnosti.** Svaka procjena ima interval pouzdanosti.
- **Simulacija prije formule.** Ideja se prvo doživi kroz preuzorkovanje, pa
  imenuje. Formula dolazi zadnja i uvijek u `<details>` izvodu.
- **Fiksno sjeme 2026.** Brojka u prozi mora biti jednaka brojci koju daje kod.
- **Hrvatski i engleski pojam u paru** u odjeljku Pojmovi; hrvatska
  terminologija razlikuje se među fakultetima, a literatura je engleska.
- **Decimalni zarez**, razmak kao razdjelnik tisućica (`1 810`, `0,417`).
- Analogije nose objašnjenje. Duge rečenice u prozi, ne popisi natuknica.
- Svaki primjer ima izvor. Izmišljeni podatak označen je kao izmišljen.

## Pravila oblikovanja

- Elemente pišite kao Quarto blokove (`::: {.definicija}` …), nikad kao sirovi
  HTML. Filter `knjiga-stil/filters/statistika.lua` generira i web i tisak.
- **Nikad ne pišite inline stilove ni nove CSS klase u poglavljima.** Ako
  element ne postoji, tražite dopunu sustava — ne improvizirajte.
- Oker (`#C08A16`) znači: ovo se može dodirnuti. Nikad kao ukras, nikad kao
  boja podataka.
- Figure isključivo kroz `theme_statistika()` (R) ili `postavi_stil()` (Python).
- Svaki widget ima statičnog blizanca (`static="slike/NN-naziv.svg"`) s istim
  sjemenom i brojem slike.
- Stupac teksta ostaje na 66 znakova. Margina (`.column-margin`) nikad ne nosi
  informaciju nužnu za razumijevanje glavnog teksta.

## Izvan opsega

Vremenski nizovi, faktorska analiza i psihometrija, višerazinski modeli,
matematika strojnog učenja, potpuna bayesovska inferencija. Bayes je uokvireni
okvir u pogl. 10 i odlomak izgleda u pogl. 16 — ne poglavlje.

## Prije predaje

Prođite kontrolni popis iz `STYLE.md`, odjeljak 9.
