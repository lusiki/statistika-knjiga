# Route A — odluka o redoslijedu `G-A3-ESS`, `P3-ESS` i `WC-C08`

**Status:** autor je odobrio Route A; kontrolni amandman je proveden.

**Vlasnik odluke:** Luka Sikic, autor/editor.

**Datum odluke i zapisa:** 11. kolovoza 2026.

**Polazno čisto stanje:** commit
`36376c7a815d43a113aeeff4917ae11695931206`, nakon prihvaćenoga C07.

## Točan odgovor autora

```text
Route A approved for H-WC-C07-WC-C08-PREREQUISITE-001 on 2026-08-11: move G-A3-ESS and P3-ESS immediately after C07 and before WC-C08, preserve the relative order of all other packets, replace G-A3-ESS prerequisite WC-PARTS with C07 while retaining P0-OUTSIDE and P3-CATALOG, add P3-ESS to WC-C08 prerequisites, retain all four WC-C08 item requirements, and preserve the separate OA-G-A3-ESS-SELECTION and OA-G-A3-ESS-RIGHTS decisions.
```

Odluka je u registru zapisana kao
`A-WC-C08-P3-ESS-ROUTE-A-2026-08-11`. Ona mijenja samo kontrolni redoslijed,
ovisnosti, dispoziciju pripadajućega upita i postojeće handoffe. Ne prihvaća
nijedan ESS paket i ne mijenja rukopis.

## Provedena promjena redoslijeda

`G-A3-ESS` i `P3-ESS` premješteni su neposredno iza C07. Svi ostali paketi
zadržavaju međusobni relativni redoslijed.

| Paket | Prijašnji slijed | Novi slijed |
|---|---:|---:|
| `G-A3-ESS` | 112 | 98 |
| `P3-ESS` | 113 | 99 |
| `WC-C08` | 98 | 100 |
| `C08` | 99 | 101 |
| `WC-C09` | 100 | 102 |
| `C09` | 101 | 103 |
| `WC-C10` | 102 | 104 |
| `C10` | 103 | 105 |
| `WC-C11` | 104 | 106 |
| `C11` | 105 | 107 |
| `G-A4-12` | 106 | 108 |
| `P3-EVIDENCE12` | 107 | 109 |
| `P3-VERIFY-C` | 108 | 110 |
| `WC-C12` | 109 | 111 |
| `C12` | 110 | 112 |
| `WC-PARTS` | 111 | 113 |

`P3-VERIFY-D` ostaje na slijedu 114, a svi paketi izvan raspona 98–113 ostaju
na svojim prijašnjim slijedovima.

## Provedene promjene ovisnosti

- `G-A3-ESS` sada zahtijeva `C07`, `P0-OUTSIDE` i `P3-CATALOG`; uklonjen je
  kasni preduvjet `WC-PARTS`.
- `P3-ESS` i dalje zahtijeva `G-A3-ESS`.
- `WC-C08` sada zahtijeva `C07`, `P1A-C08` i `P3-ESS`.
- `R12-C08-survey-realism`, `R12-C08-weighted-table`,
  `R13-C08-corpus-selection` i `R35-REACHBACK-08` i dalje pojedinačno
  zahtijevaju `P3-ESS`. Njihov sadržaj, status i dokazni ugovor nisu promijenjeni.

Time kontrolni graf sada mehanički onemogućuje claimanje `WC-C08` prije nego
što `P3-ESS` bude prihvaćen; odluka ne glumi da je taj budući paket već izveden.

## Sačuvane ESS odluke i granice ovlasti

`OA-G-A3-ESS-SELECTION` ostaje zasebna autorska odluka o točnoj ediciji,
varijablama, populaciji, težinama, receptu i ulozi u poglavljima.
Njezina je spremnost sada `ready_for_author_decision` jer je `P3-CATALOG`
prihvaćen; njezin status ostaje `drafted_unsent` i nikakva selekcijska
dispozicija nije izvedena iz Route A.
`OA-G-A3-ESS-RIGHTS` ostaje zasebna odluka vlasnika prava o redistribuciji.
D08 i dalje dopušta portal-mediated put bez lokalnoga bundlanja; tehnički pristup
ne dokazuje pravo redistribucije.

Route A ne odobrava dohvat podataka, ne bira ESS varijable, ne daje dopuštenje
za bundlanje i ne mijenja poglavlje 8. Ne autorizira render, push, merge, tag,
arhiviranje, deployment ni objavu.

## Dispozicija upita i handoffa

- `OA-WC-C08-P3-ESS-DEPENDENCY` je `done` na temelju točnoga odgovora autora;
  nijedna vanjska poruka nije poslana.
- Četiri privremene blocker-veze prema tom upitu uklonjene su. Njihovi stvarni
  preduvjeti `P3-ESS` ostaju u stavkama, a sada su provedeni i na razini paketa.
- `H-WC-C07-WC-C08-PREREQUISITE-001` je potrošen tek nakon provedbe točnoga
  redoslijeda i ovisnosti; ništa nije waived.
- `H-WC-C07-THREAD-SEQUENCE-001` proširen je na `G-A3-ESS` i `P3-ESS`.
  Njihove su dostave još pending i moraju se zasebno potrošiti na njihovim
  `before_start` gateovima.
- Nije nastao novi handoff: dvije postojeće evidencije u cijelosti nose učinak
  ove naknadne autorske odluke.

## Stanje nakon odluke

Nema aktivnoga write paketa. `C07` ostaje posljednji dovršeni paket, a
`G-A3-ESS` je sljedeći dopušteni pokazivač jer su `C07`, `P0-OUTSIDE` i
`P3-CATALOG` prihvaćeni. `G-A3-ESS` nije claiman u ovom kontrolnom amandmanu.

U budućoj bounded claim izmjeni za `G-A3-ESS` treba potrošiti njegove dvije
pending `before_start` dostave, `H-P1B-DATA-LIC-003` i
`H-WC-C07-THREAD-SEQUENCE-001`, te priznati `H-P3-CATALOG-001` na gateu
`before_close` prije uspostave aktivnoga write-locka i ponovnoga pokretanja
validatora. Katalogsku dostavu zatim treba potrošiti prije closeouta.

## Provjere closeouta

- `scripts/check-review-workflow.R` prolazi s 188 paketa, 371 atomskom stavkom,
  93 handoffa, bez aktivnoga paketa i s `G-A3-ESS` kao sljedećim pokazivačem.
- Tri obvezna negativna fixturea padaju zatvoreno s izlaznim kodom 1 za točno
  ubrizganu pogrešku: `generic_packet_evidence`, `invalid_outside_ask_link` i
  `descoped_without_amendment`.
- Neovisna usporedba s polaznim commitom dokazuje 188 jedinstvenih sequence
  vrijednosti, točnih šesnaest promjena u rasponu 98–113 i očuvan relativni
  redoslijed svih paketa osim dvaju namjerno premještenih.
- Ista usporedba nalazi točno dvije promjene `requires`: samo `G-A3-ESS` i
  `WC-C08`. Svi ostali packet-preduvjeti ostaju jednaki; `P3-VERIFY-D` ostaje
  sequence 114 i i dalje zahtijeva `WC-PARTS` i `P3-ESS`.
- Ručni audit potvrđuje točne `requires` liste za `G-A3-ESS`, `P3-ESS` i
  `WC-C08`; sva četiri WC-C08 item-preduvjeta ostaju `P3-ESS`, a samo su njihove
  razriješene privremene blocker-veze uklonjene.
- Inventar 84 upita sada sadrži 40 `done`, 38 `drafted_unsent` i 6
  `withdrawn_with_reason`; vanjskih poruka i dalje je 0.
- `git diff --check` prolazi. Promjena je ograničena na četiri kanonska
  kontrolna dokumenta i ovaj zapis odluke; nema promjene u `chapters/`, `data/`,
  `references.bib` ni u zajedničkim Bookwright registrima.

R provjera i dalje ispisuje prethodno postojeće upozorenje da `renv` nije
sinkroniziran, ali završava uspješno; Route A ne mijenja dependency lock.
