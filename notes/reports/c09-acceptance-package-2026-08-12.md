# C09 — paket za autorovo prihvaćanje devetoga poglavlja

**Gate:** `C09`

**Stanje gatea:** autor prihvatio; dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 12. kolovoza 2026.

**Datum autorove odluke:** 12. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor devetoga poglavlja nalazi se u commitu
`6c50a9fb5389401d2bb05585d6b12feaa6010e81`. Taj commit sadrži cijeli WC-C09
vertikalni rez, svih šest završnih izvještaja, sintezu i closeout dokaze.
Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`;
- Git blob poglavlja: `197ffe4340022d7465e797095645fb7a523863b2`;
- izvještaj vertikalnoga reza:
  `notes/reports/wc-c09-2026-08-12.md`;
- sinteza panela:
  `notes/reports/wc-c09-six-critic-synthesis-2026-08-12.md`.

## Šest završnih izvještaja

Svih šest neovisnih kritičara samo za čitanje pregledalo je upravo navedeni
SHA-256:

1. metode — `notes/reports/wc-c09-critic-methods-2026-08-12.md`;
2. skepticizam — `notes/reports/wc-c09-critic-skeptic-2026-08-12.md`;
3. pedagogija — `notes/reports/wc-c09-critic-pedagogy-2026-08-12.md`;
4. dokazi i citati — `notes/reports/wc-c09-critic-evidence-2026-08-12.md`;
5. hrvatski stil — `notes/reports/wc-c09-critic-style-2026-08-12.md`;
6. struktura — `notes/reports/wc-c09-critic-structure-2026-08-12.md`.

Završni panel bilježi nula fatalnih, nula velikih, pet neblokirajućih minor i
nula useful nalaza. Jedan skeptički zapis traži buduće ublažavanje
kategorične rečenice o uskom intervalu iz pristranoga uzorka. Tri stilska
zapisa odnose se na osmorečenični sažetak, jedno podebljavanje i izraz „binarni
prolaz”. Strukturni zapis ocjenjuje da je vinjeta više metodološki scenarij
nego imenovan konkretan slučaj. Izvor nije mijenjan nakon panela jer bi se
time poništio zajednički dokazni hash.

## Materijalna osnova preporuke

Preporuka je **prihvatiti** zaključano stanje. Pokrivenost se doživljava i
brojčano provjerava prije formalizacije, `z*` se objašnjava prije formule, a
interaktivni i tiskani A/B te A/C parovi mijenjaju jednu stvar uz isti
pseudoslučajni niz. Margina pogreške omeđena je na uzorkovnu nesigurnost;
pristranost, pokrivenost, neodgovor, mjerenje i kodiranje ostaju zasebni.

Razrađeni primjer ima unaprijed zadan cilj preciznosti, ne izvodi tvrdnju o
promjeni iz samih intervala i povlači populacijsku tvrdnju kada
reprezentativnost nije obranjiva. Bootstrap konstrukcija nije prikazana kao
potvrda vlastite pokrivenosti, a obični opisni raspon nije nazvan
predikcijskim intervalom.

Završetak Part III donosi šest audit pitanja, šest dimenzija tvrdnje,
odgovorivu samoprovjeru i sedmopoljnu potvrdu provjere. Kratka potvrda čitanja
koda ne traži proizvodnju sintakse. Povratni zadatak točno dohvaća Chapter 3
„Istraživač margine pogreške” i njegova dva stanja.

Tiskana tablica čita upravljani agregat, a R-or-jamovi zadatak iz analitičkoga
prikaza reproducira portalski redak 15 101 od 50 000, udio 0,30202, zbroj
povjerenja 72 101 i prosjek 4,774584464604993. Exact reconciliation prolazi;
`R32-CATALOG-paired-views` već je prihvaćen u WC-C09 prema autorskom amandmanu
i nije dio ovoga četverostavčanog C09 statusnog prijelaza.

Živi w09 i parity adapter rabe isti necachirajući Marsaglia-polar generator.
Obični parity prolazi za svih 17 parova, a negativni fixture za asimetrično
cachiranje pada bez proširenja tolerancije. HTML, odobrenim wrapperom izrađen
PDF i wrapperom izrađen DOCX završili su kodom 0 na zaključanom izvoru.

## Provedena uska dispozicija

C09 je nakon provjere točnoga odgovora proveo samo sljedeće:

- pomaknuti `09-procjena` iz `draft` u `coauthor_review`, uz izričitu bilješku
  da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije faza
  `final`;
- pomaknuti iz `ratified` u `accepted` samo
  `R13-C09-coded-uncertainty`, `R23-C09-code-reading`, `R32-C09-static` i
  `R35-REACHBACK-09`, uz WC-C09 dokaz, ovaj paket, konačni commit i stvarni
  autorov odgovor;
- ostaviti prihvaćene korekcije `R09-C09-normal-not-prediction`,
  `R09-C09-bootstrap-validation` i `R09-C09-bootstrap-failures`
  nepromijenjene;
- ostaviti već prihvaćen `R32-CATALOG-paired-views` nepromijenjen;
- ostaviti poglavlje 6 u fazi `draft` i `H-WB-PART-001` netaknutim.

Nijedna druga stavka ni poglavlje nisu promijenili status.

## Granice koje odluka ne mijenja

ESS ostaje fakultativan, portalno posredovan i nepromoviran. U repozitoriju se
ne dodaju ESS mikropodaci ni empirijski rezultat; `OA-G-A3-ESS-RIGHTS` ostaje
otvoren i bundling ostaje zabranjen. DigiKat i Eurostat granice ostaju
nepromijenjene.

C09 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge,
tag, arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao
poglavlje.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
status: accepted
author_reply: C09 accepted for 6c50a9fb5389401d2bb05585d6b12feaa6010e81 on 2026-08-12.
reply_evidence: conversation:user-message-recorded-2026-08-12
```

Odgovor navodi točan završni WC-C09 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.

`WC-C10` smije se otvoriti tek nakon dovršenoga C09 closeouta, workflow
provjere i zasebnoga lokalnog commita.
