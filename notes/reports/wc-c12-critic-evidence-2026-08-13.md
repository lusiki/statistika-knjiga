# WC-C12 — dokazni kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/12-kriza-i-obnova.qmd`:

- SHA-256: `8c1a2b34fceb2c4d9402c3377c1aa1345f2b7b30a158e41e0476c8102bfd2937`
- git blob: `e8533e54020f8649cab857d137349d887b8f5d81`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Integritet citata | 5/5 |
| Potpora tvrdnjama | 5/5 |

## Snage

- Sva četiri živa ključa poglavlja — `wagenmakers2016`, `simmons2011`,
  `gelman2013` i `osc2015` — postoje u `references.bib`; cjelovita provjera
  prolazi s 45 živih ključeva i 45 zapisa.
- RRR izvor podupire 17 laboratorija, 1.894 sudionika, izvornih 0,82, sirovu
  sintezu 0,03 [−0,11; 0,16] i sva tri laboratorijska brojanja.
- Standardizirana grana pravilno je odvojena od tiskanoga članka. Lokalni
  artefakt i verifikator reproduciraju `d = 0,014151
  [−0,076191; 0,104493]`.
- Urednički CSV ima očekivani SHA-256 `23ca66fd…`; poglavlje generira vlastiti
  prikaz, ne prenosi izdavačev graf ni sudioničke bajtove i ne tvrdi da je
  Talaricova vrijednost 1,60 reproducirana.

## Nalaz

Jedan administrativni minor ne odnosi se na rukopis: u ulaznom nalogu kritičaru
naveden je nepostojeći put
`data/editorial/rrr-wagenmakers-2016-study-level.csv`. Kanonski dokazni artefakt
jest `notes/reports/p3-evidence12-rrr-lab-effects.csv`, ima očekivani hash i
prolazi provjeru. Budući handoff treba navesti stvarni put, bez stvaranja
duplikata.

Nema nedostajućih ili neprovjerenih tvrdnji u evidencijskoj leći. H7
rečenicama bez vlastitoga citata zasebno upravlja stilski nalaz.

## Presuda

Potpun evidencijski prolaz bez fatalnih ili major nalaza.

## Završna ponovna provjera

Kritičar je read-only pregledao cijeli završni izvor SHA-256
`47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`, git
blob `bc9bb538625e6996f116ae1fd5b1acba56dc0852`. Završne ocjene su 5/5 i 5/5.

Receipt točno prenosi sirovu procjenu `0.026766 [-0.107693, 0.161225]` i
standardizirani `d = 0.014151 [-0.076191, 0.104493]`, a proza izričito kaže da
ih je reproducirao neovisni verifikator i da ih isječak ne računa ponovno.
Svih pet odobrenih H7 popravaka ima citat u istoj rečenici. Četiri živa ključa
postoje, lokalni artefakt ima očekivano podrijetlo, izvornih 0,82 ostaje samo
referenca, a zabranjeni sudionički i izdavački artefakti te Talaricova SD
tvrdnja nisu uključeni.

Nema nedostajućih ili neprovjerenih tvrdnji ni fatalnih, major ili minor
dokaznih nalaza. Raniji administrativni nesklad bio je u nalogu kritičaru, ne u
rukopisu ili kanonskom handoffu, pa nije završni panel nalaz.
