# WC-C11 — pedagoški kritičar

Prvi pregled izveden je read-only nad zaključanim izvorom
`chapters/11-velicina-ucinka-i-snaga.qmd`:

- SHA-256: `4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
- git blob: `e4577e72897a6c450aba04f11270ca97bf19c26b`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Jasnoća | 4/5 |
| Postupno uvođenje | 4/5 |
| Preduvjeti | 5/5 |
| Kvaliteta zadataka | 4/5 |

## Snage

- Slijed vodi početnika od razlike u izvornim jedinicama preko standardizacije,
  praktične i statističke značajnosti, snage i selekcijskog pretjerivanja do
  planiranja unatrag.
- Snaga se izravno nadovezuje na propuštene učinke iz 10. poglavlja, a tekst
  zaključke više puta ograničava na simuliranu populaciju i postupak.
- Widget je sastavni dio argumenta, a tiskana ruta donosi krivulje, točne
  agregate i vrijednosti potrebne za ocijenjeni zadatak.
- Sve četiri razine zadataka zahtijevaju primjenu ili prosudbu; računski zadatak
  ostvaruje stvaran dohvat 9. poglavlja.

## Nalazi

Sva su tri nalaza minor:

1. U retcima 207–220 simbol `d` prvi se put pojavljuje u formuli, a
   `s_zdr` objašnjava se tek poslije. Oba simbola treba objasniti prije formule.
2. Permutacijska krivulja rabi ukupan uzorak, dok widget i razrađeni z-primjer
   rabe broj jedinica po skupini. Treba izričito upozoriti da vrijednosti `n`
   i pripadne snage nisu izravno usporedive.
3. HTML zadatak u retcima 856–880 ne zadaje broj ponavljanja: zadano je 1.500,
   dok tiskana tablica i rješenje rabe 2.000. Treba zadati 2.000 ponavljanja i
   navesti toleranciju ili rezultate specifične za rutu.

## Presuda

Prolaz bez fatalnih ili major nalaza, uz tri manja pojašnjenja. Poglavlje je
dobro sekvencirano, simulacijski vođeno, dovršivo u tisku i bogato zadacima.

## Završna ponovna provjera

Kritičar je read-only ponovno pregledao cijeli završni izvor SHA-256
`d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`, git
blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f`. Ocjene ostaju jasnoća 4/5,
postupno uvođenje 4/5, preduvjeti 5/5 i zadaci 4/5. Dva metodološka popravka
poboljšavaju učivost jer transparentno obrađuju izjednačenja i zamjenjuju
kružnu opaženu snagu konkretnim ciljnim učinkom. Nema fatalnih ni major nalaza;
sva tri ranija minora ostaju za `C11`.
