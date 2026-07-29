# images/

Statički vizualni materijali: infografike, sheme, portreti, favicon,
naslovnica.

Konvencije koje engine očekuje:

- Infografike se crtaju kao **SVG**, a `scripts/svg-to-png.R` proizvodi PNG
  blizanca. Filter `pdf-filters/swap-svg-png.lua` pri PDF renderu prepisuje
  `.svg` u `.png`, pa se u poglavlju uvijek referencira SVG.
- Datoteke koje se moraju naći na webu, a nisu referencirane iz .qmd-a
  (favicon, slika za dijeljenje), navode se u `resources:` u `_quarto.yml`.
- Naslovnica (`cover.png`) i favicon još ne postoje; redci u `_quarto.yml` su
  zakomentirani dok se ne odabere vizualni identitet (DESIGN.md).
