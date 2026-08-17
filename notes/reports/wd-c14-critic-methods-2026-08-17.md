# WD-C14 — završni metodološki pregled

Neovisni read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/14-dvije-grupe.qmd`:

- SHA-256: `84b6c8fac8ce4eecf5474a0535ba02030dbf332a37789bcd7347c4ae9a66cfa2`;
- git blob: `6ef3a218dfc61d5ad73f83e236a70e3917909d86`;
- podudaranje zadanog i opaženog bloba: da.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 5/5 |
| Pretpostavke | 5/5 |
| Interpretacija | 5/5 |
| Preciznost | 5/5 |

## Snage

- D02 je ostao točan: procjenjuje se razlika populacijskih sredina televizija
  minus društvene mreže, nulta hipoteza jest dvostrana `Delta = 0`, Welchov je
  postupak zadan, a koeficijent binarnoga OLS prediktora ima istu sirovu
  procjenu, ali općenito ne i istu neizvjesnost.
- Neovisni, upareni i jednouzorački dizajn pravilno su razdvojeni. Ovisnost
  aktivira izričito pravilo zaustavljanja, dok upareni primjer čuva kovarijancu
  unutar para i odbija uzročno tumačenje bez randomizacije ili kontrolne
  skupine.
- Standardizirana razlika odgovara definiciji iz 11. poglavlja s objedinjenom
  standardnom devijacijom i točnim smjerom. Nazivnik za upareni dizajn izrijekom
  je razlikovan, a Wilcoxonov test predznaka rangova nije prikazan kao
  zaključivanje o srednjoj razlici.
- Formule widgeta točne su za navedeni normalni model, jednake rubne standardne
  devijacije i korelaciju parova 0,65. Tekst sada izrijekom imenuje izostavljenu
  kovarijancu unutar para, a odlomak o Shapiro–Wilkovu testu točno opisuje
  ovisnost o veličini uzorka.

## Nalazi

Nema fatalnih, velikih ni manjih metodoloških nalaza.

## Presuda

Poglavlje prolazi završni metodološki pregled. D02, pretpostavke, smjerovi
kontrasta i razlike među dizajnima očuvani su na zaključanom izvoru.
