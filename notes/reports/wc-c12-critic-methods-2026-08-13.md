# WC-C12 — metodološki kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/12-kriza-i-obnova.qmd`:

- SHA-256: `8c1a2b34fceb2c4d9402c3377c1aa1345f2b7b30a158e41e0476c8102bfd2937`
- git blob: `e8533e54020f8649cab857d137349d887b8f5d81`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 5/5 |
| Pretpostavke | 4/5 |
| Interpretacija | 5/5 |
| Preciznost | 4/5 |

## Snage

- P-hakiranje je odvojeno od podatkovno uvjetovanih račvajućih putova, a
  stopa pogreške vezana je uz cijeli selekcijski postupak.
- Laboratoriji nisu pretvoreni u glasove. Točke, intervali i objedinjena
  procjena čitaju se kumulativno, bez poistovjećivanja praga s postojanjem ili
  odsutnošću učinka.
- Sirova razlika i Cohenov `d` tretirani su kao različite procjenjivane
  veličine s različitim ponderima, a osjetljivost se tumači sadržajno.
- Interakcija izričito navodi neovisnost putova, kalibraciju pod nultim
  modelom, omeđenu obitelj i granice Bonferronijeva praga.

## Nalazi

Sva su tri nalaza minor:

1. U retcima 65–67 kalibracija p-vrijednosti preusko je vezana uz jednu
   unaprijed određenu analizu. Preciznije je vezati je uz unaprijed određen
   postupak pod njegovim pretpostavkama, uključujući uzorkovanje, zaustavljanje
   i selekciju.
2. U retcima 131–136 REML sažetak može zvučati kao običan prosjek opaženih
   laboratorijskih učinaka. Treba ga imenovati ponderiranim, modelom uvjetovanim
   objedinjavanjem i interval omeđiti na nesigurnost modelskoga prosjeka.
3. U retcima 245–248 opis registriranoga izvještaja izostavlja načelno
   prihvaćanje prije poznatoga ishoda, glavni mehanizam smanjivanja selekcije
   prema rezultatu.

## Presuda

Metodološki prolaz bez fatalnih ili major nalaza, uz tri manje precizacije za
autorsku dispoziciju.

## Završna ponovna provjera

Nakon autorova odobrenja triju obveznih popravaka i razrješenja receipt
kontraksa kritičar je ponovno read-only pregledao cijeli završni izvor:

- SHA-256: `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`
- git blob: `bc9bb538625e6996f116ae1fd5b1acba56dc0852`

Završne ocjene su točnost 5/5, pretpostavke 4/5, interpretacija 5/5 i
preciznost 4/5. Simulacija prethodi formuli, a sedmeroredni receipt provjerava
17 laboratorija i 1.894 sudionika, označuje primarnu sirovu i alternativnu
standardiziranu granu te prikazuje njihove provjerene procjene i intervale bez
glumljenja novoga izračuna metaanalize.

Nema fatalnih ni major nalaza. Ostaju tri minora o kalibraciji p-vrijednosti,
modelom uvjetovanom REML sažetku i načelnom prihvaćanju u registriranom
izvještaju. Sva tri ostaju za `C12`.
