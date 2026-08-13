# WC-C12 — pedagoški kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/12-kriza-i-obnova.qmd`:

- SHA-256: `8c1a2b34fceb2c4d9402c3377c1aa1345f2b7b30a158e41e0476c8102bfd2937`
- git blob: `e8533e54020f8649cab857d137349d887b8f5d81`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Jasnoća | 4/5 |
| Postupno uvođenje | 3/5 |
| Preduvjeti | 4/5 |
| Kvaliteta zadataka | 5/5 |

## Snage

- Jedan stvarni RRR nosi put od početne tvrdnje preko analitičkih odluka do
  kumulativnoga dokaza i granica reforme.
- Ključne razlike izgrađene su na jasnim kontrastima: p-hakiranje prema
  račvajućim putovima te reproducibilnost prema replikaciji.
- Forest plot najprije objašnjava točku, interval i referentne crte, a zatim se
  čita bez glasovanja o „uspješnim” laboratorijima.
- Sve četiri razine zadataka traže primjenu i prosudbu te ne zahtijevaju
  proizvodnju koda.

## Nalazi

### Major — slijed interakcije i tiskani put

U retcima 275–507 formula `0,05/m` dolazi prije simulacijskoga iskustva, a
tiskani blizanac ne dopušta prva tri postupka iz zajedničkoga bloka „Što
isprobati”. Digitalni i tiskani čitatelj zato ne prolaze isti put od opažanja
prema formalizaciji.

Preporučeni popravak: premjestiti oznaku `m` i korigirani prag iza widgeta te
razdvojiti digitalne korake od tiskane upute koja vodi kroz prikazane krivulje
za 1, 12 i 48 putova.

### Major — vidljivi računski receipt

U retcima 600–630 slijed `read.csv`, `stopifnot`, `nrow`, `$`, `data.frame` i
`c` nije samostalno čitljiv početniku bez programiranja. Proza objašnjava samo
jednu naredbu i stupce, pa nosivi trag podrijetla djeluje kao neprozirna potvrda
autoriteta.

Preporučeni popravak: svesti vidljivi receipt na najkraći provjerljivi trag i
uz njega mapirati svaki redak na pitanje koje provjerava; računsku
infrastrukturu zadržati skrivenom.

### Minor

1. U retcima 225–234 treba kratko podsjetiti da je sirova razlika u bodovima,
   a `d` u standardnim devijacijama, te zašto standardizacija može promijeniti
   težine laboratorija.
2. Replikacija se u vinjeti rabi prije jednostavne razlike prema
   reproducibilnosti; kratka glosa pri prvom spomenu olakšala bi čitanje.

## Presuda

Poglavlje još ne prolazi pedagoški panel: dva major nalaza traže autorski
odobrenu doradu interakcije i vidljivoga receipta.

## Završna ponovna provjera

Nakon autorova odobrenja kritičar je read-only pregledao cijeli završni izvor
SHA-256 `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`, git
blob `bc9bb538625e6996f116ae1fd5b1acba56dc0852`. Završne ocjene su jasnoća 4/5,
postupno uvođenje 4/5, preduvjeti 5/5 i zadaci 5/5.

Oba major nalaza su zatvorena. Digitalna simulacija i tiskani prikaz prethode
formuli, a njihove upute odgovaraju dostupnim kontrolama odnosno krivuljama za
1, 12 i 48 putova. Sedmeroredni receipt ostaje čitljiv bez programerskoga
iskustva: proza mapira učitavanje, provjeru brojnosti, četiri imenovana vektora
i tablicu te jasno kaže da se vrijednosti ovdje ne računaju ponovno.

Ostaju samo dva namjerno neizmijenjena minora, kratka glosa replikacije pri
prvom spomenu i podsjetnik na jedinice sirove razlike nasuprot Cohenovu `d`.
Završna presuda je pedagoški prolaz bez fatalnih ili major nalaza.
