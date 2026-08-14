# WC-C12 — skeptički kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/12-kriza-i-obnova.qmd`:

- SHA-256: `8c1a2b34fceb2c4d9402c3377c1aa1345f2b7b30a158e41e0476c8102bfd2937`
- git blob: `e8533e54020f8649cab857d137349d887b8f5d81`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Pokrivenost osporavanja | 5/5 |
| Poštenje prema drugim pogledima | 5/5 |
| Normativna iskrenost | 4/5 |

## Snage

- Doseg RRR-a dosljedno je ograničen: nema univerzalne tvrdnje o nepostojanju
  učinka, uzročnoga objašnjenja razlika ni prijenosa izvan usporedivih
  postupaka.
- P-hakiranje je odvojeno od račvajućih putova, a publikacijska selekcija
  prikazana je kao sustavni problem bez moraliziranja o pojedincima.
- Slabosti reformi nisu prešućene: reproducibilnost može ponoviti loše
  mjerenje, predregistracija ne jamči valjanost, a otvorenost ne ukida
  privatnost ni licencijska ograničenja.
- Izvornih 0,82 odvojeno je od sinteze; izdavačev prikaz i sudionički izvori
  nisu uključeni, a uzroci laboratorijskih razlika ostaju neidentificirani.

## Nalazi

Oba su nalaza minor:

1. Izrazi „samo male razlike” i „male vrijednosti” u retcima 131–136,
   225–234, 633–639 i 658–662 uvode prešutni sadržajni prag. Treba ih vezati uz
   izvornu procjenu i ljestvicu te navesti da prag praktične važnosti nije
   zadan.
2. Apsolutno „ne možemo predvidjeti” ili „ne predviđa nov rezultat” u retcima
   40–43, 260–266, 516–523 i 641–643 može sugerirati da sinteza uopće ne može
   informirati očekivanje. Uža je tvrdnja da ova analiza nije izvela pouzdanu
   predikciju za novu ciljnu populaciju i kontekst.

## Presuda

Prolaz bez fatalnih ili major nalaza, uz dvije manje formulacijske granice za
autorsku dispoziciju.

## Završna ponovna provjera

Kritičar je read-only pregledao cijeli završni izvor SHA-256
`47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`, git
blob `bc9bb538625e6996f116ae1fd5b1acba56dc0852`. Završne ocjene su 5/5, 5/5 i
4/5. Receipt pošteno odvaja prikaz provjerenih vrijednosti od računanja, a
interakcija zadržava granice neovisnosti putova, kalibracije i omeđene obitelji.

Nema fatalnih ni major nalaza. Završna dva minora odnose se na neimenovani
sadržajni prag iza izraza „male razlike” i na prejaku formulaciju da reforma
„daje” potpuno vidljiv i osporiv postupak. Oba ostaju za `C12`.
