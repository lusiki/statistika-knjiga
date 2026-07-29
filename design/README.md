# design/

Ulazni materijal za vizualni identitet. Ništa odavde ne ide u build; ovo je
mjesto na koje se spušta ono što dizajn definira, prije nego se preslika u
`design-tokens.yml`.

Što ovdje smije stajati:

- izvoz iz dizajnerskog alata (CSS s varijablama, tokens.json, Figma izvoz)
- stilski priručnik u PDF-u
- snimke zaslona referenci
- `brief.md`, ispunjen obrazac s dna [DESIGN.md](../DESIGN.md)

Postupak i pravilo četiri datoteke opisani su u [DESIGN.md](../DESIGN.md).
Kratko: ovdje se **opisuje** dizajn, u `design-tokens.yml` se **zadaje**, a
`Rscript scripts/check-tokens.R` provjerava da su ostali slojevi usklađeni.
