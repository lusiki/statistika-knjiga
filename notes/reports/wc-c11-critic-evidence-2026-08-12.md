# WC-C11 — dokazni kritičar

Prvi pregled izveden je read-only nad zaključanim izvorom
`chapters/11-velicina-ucinka-i-snaga.qmd`:

- SHA-256: `4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
- git blob: `e4577e72897a6c450aba04f11270ca97bf19c26b`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Integritet citata | 5/5 |
| Potpora tvrdnjama | 5/5 |

## Snage

- Svih pet živih citatnih pojava koristi postojeće i jedinstvene ključeve:
  `cohen1994`, `cohen1988` i `button2013`. Metapodaci i sadržaj odgovaraju
  tvrdnjama kojima su pridruženi.
- Podrijetlo `populacija_medija` sljedivo je do
  `simuliraj_populaciju(N = 50000, sjeme = 8001)`. Analitička i agregatna
  snimka odgovaraju katalogom propisanim MD5 vrijednostima.
- Upravljani agregat reproducira portalski redak
  `15101 / 72101 / 4,774584464604993`, redak tiska
  `4855 / 26791 / 5,518228630278064`, razliku `0,743644165673071` i tiskane
  snage 42,5 %, 72,4 %, 94,6 % i 99,9 %.
- Reproducirane su nosive simulacijske veličine: krivulja snage
  22,6667–99,6667 %, `d = 0,3888976`, faktor pretjerivanja `2,0142789`,
  pogrešan predznak `0,1474926 %`, veliki-uzorak faktor `1,0267078` te plan
  46,2 %, 63,5 %, 75,05 % i 83,25 %.

## Nalazi

Nema fatalnih, major ni minor nalaza. Nema nedostajućih ili neprovjerenih
izvora.

## Presuda

Potpun dokazni i citatni prolaz na točno zadanom hashu.

## Završna ponovna provjera

Kritičar je read-only ponovno pregledao završni izvor SHA-256
`d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`, git
blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f`. Ocjene ostaju 5/5 i 5/5.
Neovisno je reproducirao:

- `39.324.683 / 73.315.355 = 53,6377175 %` stroge nadmoći;
- `10.219.593 / 73.315.355 = 13,9392260 %` izjednačenja;
- `60,6073305 %` prilagođene nadmoći;
- `0,5 / 1,9 = 0,2631579` za ciljni `d`;
- `power.t.test(...)$n = 227,6400263`, pa 228 osoba po skupini.

Vrijednosti su točno prikazane kao 53,6 %, 13,9 %, 60,6 %, 0,26 i 228 te
jasno označene kao rezultati simulirane populacije odnosno uvjetnoga planskog
računa. Nema nedostajućih izvora ni fatalnih, major ili minor dokaznih nalaza.
