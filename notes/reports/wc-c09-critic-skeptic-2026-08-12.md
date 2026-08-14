# WC-C09 — završni skeptički izvještaj

**Izvor:** `chapters/09-procjena.qmd`

**SHA-256 prije i poslije pregleda:**
`42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`

Kritičar je radio neovisno i samo za čitanje. Nijedna datoteka nije uređena
niti je stvoren artefakt.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Pretpostavke | 5/5 |
| Granice tvrdnje | 5/5 |
| Protutumačenja | 5/5 |
| Odgovornost čitatelja | 5/5 |

## Snage

- Tekst uporno odvaja uski interval od valjanosti uzorka, mjerenja i kodiranja
  te izričito povlači populacijsku tvrdnju ako reprezentativnost nije obranjiva.
- Šest pitanja revizije i šest dimenzija tvrdnje priječe da čitatelj svede
  provjeru na jednu granicu intervala ili jednu oznaku pouzdanosti.
- Obični opisni raspon nije predstavljen kao predikcijski interval, a
  bootstrap konstrukcija ostaje odvojena od provjere pokrivenosti postupka.
- Tvrdnje o nepreklapanju intervala omeđene su nacrtom, zavisnošću i izravnim
  intervalom razlike.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

1. Rečenica da je uzak interval oko procjene iz pristranoga uzorka „sigurnost
   u pogrešnu vrijednost” kategoričnija je od ostatka poglavlja: pristran
   postupak ne mora u svakoj realizaciji promašiti. U budućem stilskom prolazu
   mogla bi se ublažiti u „može dati veliku preciznost oko sustavno pomaknute
   vrijednosti”.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **1**
- Korisno poboljšanje: **0**

**Verdikt:** skeptički prolaz za završni panel. Minor ostaje vidljiv bez
promjene zaključanoga izvora; odluka o C09 ostaje autoru/editoru.
