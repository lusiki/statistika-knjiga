# Pisma za tiskani PDF

Ove statičke instance dio su izvora knjige. `tex/theme.tex` i `tex/korica.tex`
učitavaju ih po nazivu datoteke iz ovoga direktorija, a `R/theme_book.R` ih
registrira za grafove. PDF zato ima ista pisma na svakom stroju i ne može
neopaženo pasti na Latin Modern.

Sustav Zvono koristi tri obitelji:

| Obitelj | Uloga | Datoteke | Izvor |
|---|---|---|---|
| Literata | proza | `Literata-*.ttf` | <https://github.com/google/fonts/tree/main/ofl/literata> |
| Jost | displej, naslovi, oznake, potpisi, korica | `Jost-Regular.ttf`, `Jost-Medium.ttf`, `Jost-Italic.ttf` | <https://github.com/google/fonts/tree/main/ofl/jost> |
| JetBrains Mono | kod i brojevi | `JetBrainsMono-*.ttf` | <https://github.com/google/fonts/tree/main/ofl/jetbrainsmono> |

Sve su obitelji dostupne pod licencijom SIL Open Font License 1.1. Tekst licence
za svaku obitelj stoji uz instance (`OFL-*.txt`). Izvorni varijabilni fontovi
pretvoreni su pomoću `fontTools.varLib.instancer`. Literata je instancirana na
`opsz=11`, a rezovi prema nazivima datoteka na `wght=400` ili `700`. Jost je
instanciran iz `Jost[wght].ttf` na `wght=400` (Regular) i `wght=500` (Medium) te
iz `Jost-Italic[wght].ttf` na `wght=400` (Italic); sve tri instance sadrže
č ć đ š ž i hrvatske navodnike. JetBrains Mono ima samo os `wght`.

Newsreader i Public Sans pripadali su prethodnom identitetu („prozračni
uredništveni”). Tiskarski sloj i R tema više ih ne učitavaju; datoteke su
zadržane samo radi usporedbe sa starijim izdanjima i mogu se ukloniti.

Prije pakiranja PDF-a provjerite da su sva tri registra ugrađena u PDF.
