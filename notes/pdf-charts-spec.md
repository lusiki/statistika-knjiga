# Specifikacija grafova u tisku

Kako statički blizanci interaktivnih grafova izgledaju u PDF-u.

## Pozadina

Uređaj crta na **prozirnoj** pozadini (`bg: "transparent"` u
`_quarto-pdf.yml`), a boju papira postavlja `\pagecolor` u `tex/theme.tex`.
Tako boja stranice postoji na jednom mjestu po formatu i graf nikad ne iscrta
bijeli pravokutnik na obojanoj stranici.

`theme_knjiga()` zato ne boji `plot.background` ni `panel.background`.

## Uređaj

`dev: cairo_pdf`. Zadani Windows PDF uređaj ispušta Unicode znakove koji se
pojavljuju u oznakama grafova (Δ, →, ₙ, ≥, ½) uz poruku o „mbcsToSbcs
conversion failure". Cairo ih ispisuje ispravno.

## Boja ili sivo

Web je uvijek u boji. Tisak je otvorena odluka (DESIGN.md, polje 12):

- **u boji** — koristi `boje_knjige` i `scale_*_knjiga()`, ništa se ne mijenja;
- **jednobojno** — koristi niz `sivo` i `scale_*_sivo()`, i provjeri da se
  serije razlikuju i oblikom (linija, točka, šrafura), ne samo tonom.

Odluku treba donijeti prije nego nastane peti graf, jer je poslije prepravljanje
skupo.

## Što blizanac mora nositi

Ne mora biti isti graf. Mora nositi **istu tvrdnju** pri jednoj razumnoj
postavci parametara. Gdje interaktivni graf pokazuje kretanje, blizanac često
pokazuje tri stanja jedno uz drugo.

Naslov blizanca završava s `-print` u `label`-u da se ne sudari s OJS grafom.
