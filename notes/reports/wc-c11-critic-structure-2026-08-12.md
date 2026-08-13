# WC-C11 — strukturni kritičar

Prvi pregled izveden je read-only nad zaključanim izvorom
`chapters/11-velicina-ucinka-i-snaga.qmd`:

- SHA-256: `4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
- git blob: `e4577e72897a6c450aba04f11270ca97bf19c26b`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Vjernost otvaranja | 5/5 |
| Izbor definicija | 5/5 |
| Uvodi u slike | 4/5 |
| Pokrivenost zadacima | 5/5 |

## Snage

- Cohenova stvarna kritika uvodi problem prosudbe, a vinjeta završava
  neodgovorenim pitanjem koje povezuje važan učinak s potrebnom količinom
  podataka.
- Pet pojmovnih odjeljaka napreduje od izvornih jedinica preko standardizacije,
  značajnosti i snage do selekcijskog pretjerivanja i planiranja unatrag.
  Kanonski sedmodijelni poredak potpuno je vraćen.
- Tri `#def-` bloka odgovaraju ratificiranoj hijerarhiji i živom registru
  pojmova.
- Divljina, model, realistična pogreška naknadne snage, razrađeni primjer i
  četiri razine zadataka tvore povezanu cjelinu.

## Nalaz

Jedan minor nalaz: zajednički uvod u interakciju i upute „Što isprobati” u
retcima 438–450 obećavaju mijenjanje učinka, uzorka i praga te `d = 0,10`, ali
tiskani blizanac u retcima 613–706 fiksira prag na 0,05 i prikazuje samo
`d = 0,2`, `0,4` i `0,6`. Treba dodati tiskani preset za drugi prag i
`d = 0,10` ili u tiskanoj grani dati upute koje odgovaraju postojećim
krivuljama i tablicama.

## Presuda

Strukturni prolaz bez fatalnih ili major zapreka, uz jednu manju korekciju
vjernosti tiskane interakcije.

## Završna ponovna provjera

Kritičar je read-only ponovno pregledao cijeli završni izvor SHA-256
`d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`, git
blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f`. Ocjene ostaju 5/5, 5/5,
4/5 i 5/5. Kanonski sedmodijelni poredak, tri definicije, četiri razine zadataka
i dohvat 9. poglavlja ostaju očuvani. Nema fatalnih ni major nalaza; raniji
minor o nepotpunoj vjernosti vođenih poteza u tiskanoj interakciji ostaje za
`C11`.
