# Pisma za tiskani PDF

Ove statičke instance dio su izvora knjige. `tex/theme.tex` ih učitava po nazivu
datoteke iz ovoga direktorija, pa PDF ima ista pisma na svakom stroju i ne može
neopaženo pasti na Latin Modern.

| Obitelj | Uloga | Izvor |
|---|---|---|
| Literata | proza | <https://github.com/google/fonts/tree/main/ofl/literata> |
| Newsreader | naslovi | <https://github.com/google/fonts/tree/main/ofl/newsreader> |
| Public Sans | potpisi i pomoćni tekst | <https://github.com/google/fonts/tree/main/ofl/publicsans> |
| JetBrains Mono | kod i brojevi | <https://github.com/google/fonts/tree/main/ofl/jetbrainsmono> |

Sve su obitelji dostupne pod licencijom SIL Open Font License 1.1. Tekst licence
za svaku obitelj stoji uz instance (`OFL-*.txt`). Izvorni varijabilni fontovi
pretvoreni su pomoću `fontTools.varLib.instancer`: Literata na `opsz=11`,
Newsreader na `opsz=36`, a rezovi prema nazivima datoteka na `wght=300`, `400`
ili `700`. Public Sans i JetBrains Mono imaju samo os `wght`.

Prije pakiranja PDF-a provjerite da su sva četiri registra ugrađena u PDF.
