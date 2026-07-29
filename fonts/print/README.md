# fonts/print/

Statičke instance pisama za PDF (xelatex ne voli varijabilne fontove).

Prazno je dok tipografija nije odabrana. Do tada `tex/theme.tex` ne poziva
`\setmainfont`, pa se PDF gradi s Latin Modernom na svakom stroju bez ijednog
preuzimanja.

Kad pisma budu odabrana:

1. Stavite statičke `.ttf` instance ovamo (Regular, Italic, SemiBold/Bold,
   BoldItalic za serif; Regular, Italic, Bold za sans; Regular, Bold za mono).
2. Otključajte blok `\setmainfont` / `\setsansfont` / `\setmonofont` u
   `tex/theme.tex` i upišite imena datoteka.
3. Uskladite `design-tokens.yml` i `styles/_tokens.scss`, pa pokrenite
   `Rscript scripts/check-tokens.R`.

`.gitignore` prati **samo** ovaj poddirektorij (`fonts/*` je ignoriran,
`!fonts/print/` je iznimka), jer su ove datoteke ulaz u build, a ne
regenerabilan otpad.
