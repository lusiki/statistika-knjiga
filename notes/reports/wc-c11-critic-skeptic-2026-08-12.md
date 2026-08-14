# WC-C11 — skeptički kritičar

Prvi pregled izveden je read-only nad zaključanim izvorom
`chapters/11-velicina-ucinka-i-snaga.qmd`:

- SHA-256: `4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
- git blob: `e4577e72897a6c450aba04f11270ca97bf19c26b`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Pokrivenost osporavanja | 4/5 |
| Poštenje prema drugim pogledima | 5/5 |
| Normativna iskrenost | 4/5 |

## Snage

- Rezultat o pretjerivanju dobro je omeđen na zadanu simuliranu populaciju,
  uzorak, postupak i prag.
- Niska snaga nije pretvorena u presudu o istinitosti; tekst traži interval,
  način selekcije, prethodne dokaze i neovisnu replikaciju.
- Granice permutacijske krivulje, idealiziranoga widgeta i z-primjera jasno su
  razdvojene.
- Praktična važnost prikazana je kao prosudba, a Cohenove orijentacijske
  vrijednosti i cilj od 80 % kao pomoćne konvencije.

## Nalazi

Sva su tri nalaza minor:

1. U retcima 196–205 spoj „punom populacijom”, „istina” i urednička odluka
   može ponovno otvoriti uzročno čitanje. Treba lokalno reći da je riječ o
   opisnoj razlici u simuliranoj populaciji te da puni obuhvat ne uklanja
   samoodabir, ne stvara uzročni učinak i ne jamči generalizaciju.
2. U retcima 239–245 „zajednički jezik” standardizacije može sugerirati
   sadržajnu usporedivost koju broj ne osigurava. Treba dodati da
   standardizacija ne izjednačuje konstrukte, populacije ni kvalitetu mjerenja.
3. U retcima 405–418 i 815–824 formulacija da najmanji važan učinak „postavlja
   istraživač” preusko dodjeljuje normativnu ovlast. Prag treba prikazati kao
   obrazloženi prijedlog uz relevantne donositelje odluka ili pogođene skupine,
   a zaključak o 200–250 jedinica vezati uz prag, raspršenost i uporabljiva
   opažanja.

## Presuda

Prolaz bez fatalnih ili major nalaza, uz tri manje ograde koje bi dovršile
uzročnu, mjernu i normativnu granicu argumenta.

## Završna ponovna provjera

Kritičar je read-only ponovno pregledao cijeli završni izvor SHA-256
`d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`, git
blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f`. Ocjene ostaju 4/5, 5/5 i
4/5. Dva metodološka popravka nisu unijela novi skeptički problem. Nema
fatalnih ni major nalaza; sva tri ranija minora ostaju primjenjiva za autorsku
dispoziciju u `C11`.
