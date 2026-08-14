# C10 — paket za autorovo prihvaćanje desetoga poglavlja

**Gate:** `C10`

**Stanje gatea:** autor prihvatio; dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 12. kolovoza 2026.

**Datum autorove odluke:** 12. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor desetoga poglavlja nalazi se u commitu
`88b41d02fcea8222673f28a40938fe7db2aaffd6`. Taj commit sadrži cijeli WC-C10
vertikalni rez, svih šest završnih izvještaja, sintezu i closeout dokaze.
Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236`;
- Git blob poglavlja: `e0275e8ba85f360d238bbace6a216dcdef5283bc`;
- izvještaj vertikalnoga reza:
  `notes/reports/wc-c10-2026-08-12.md`;
- sinteza panela:
  `notes/reports/wc-c10-six-critic-synthesis-2026-08-12.md`.

## Šest završnih izvještaja

Svih šest neovisnih kritičara samo za čitanje pregledalo je upravo navedeni
SHA-256:

1. metode — `notes/reports/wc-c10-critic-methods-2026-08-12.md`;
2. skepticizam — `notes/reports/wc-c10-critic-skeptic-2026-08-12.md`;
3. pedagogija — `notes/reports/wc-c10-critic-pedagogy-2026-08-12.md`;
4. dokazi i citati — `notes/reports/wc-c10-critic-evidence-2026-08-12.md`;
5. hrvatski stil — `notes/reports/wc-c10-critic-style-2026-08-12.md`;
6. struktura — `notes/reports/wc-c10-critic-structure-2026-08-12.md`.

Završni panel bilježi nula fatalnih, nula velikih, četiri neblokirajuća manja i
nula korisnih nalaza. Pedagoški izvještaj bilježi da završni popis osam pojmova
ne slijedi posve redoslijed njihovih prvih pojava. Stilski izvještaj bilježi
izraz „kao kurikularnom izboru”, niz „Prva… Druga… Treća…” u AI okviru i
brojčane uputnice na poglavlja 7 i 8 umjesto tematskih naziva. Izvor nije
mijenjan nakon panela jer bi se time poništio zajednički dokazni hash.

## Materijalna osnova preporuke

Preporuka je **prihvatiti** zaključano stanje. Dio IV sada počinje veličinom
procjene, neizvjesnošću i konkretnim posljedicama pogrešne odluke, a simulirani
svijet pune nule dolazi prije formalnoga imenovanja nulte hipoteze. Prihvaćeni
D01 ostaje cijeli: permutacija oznaka cilja nulu pune raspodjele odnosno
nepovezanosti pod razmjenjivošću, statistika je obostrana nestudentizirana
razlika sredina, a slučajne permutacije rabe `(b + 1) / (B + 1)` s
izjednačenjima. Egzaktna enumeracija, poznata puna nula, opažačka uzročna
granica, analitički w10 i omeđena Bayesova usporedba ostaju jasno odvojeni.

Poglavlje je glavni nastavni dom epizode Američkoga statističkog udruženja i
razdvaja što je struka rekla, zašto je intervenirala i kako se čitanje
p-vrijednosti promijenilo. Kratak okvir razlikuje procijenjenu stopu pogreške
od pogrešive referentne oznake bez otvaranja novoga empirijskog primjera.
Povratni zadatak dohvaća vjerojatnost i uzorkovanje, ima HTML i tiskani odnosno
DOCX put te kanonsko zatvaranje unutar četiriju razina zadataka.

Živi w10 i produkcijski parity adapter rabe isti necachirajući
Marsaglia-polarni generator. Paritet prolazi za svih 17 parova, a tri negativna
fixturea padaju zatvoreno; w10-specifični fixture odstupa na sva četiri zlatna
izlaza, bez proširenja tolerancije. Konceptni graf svježe je obnovljen na 47
čvorova i 514 bridova. HTML, odobrenim wrapperom izrađen PDF i wrapperom izrađen
DOCX završili su kodom 0 na zaključanom izvoru.

## Provedena uska dispozicija

C10 je nakon provjere točnoga odgovora proveo samo sljedeće:

- pomaknuti `10-logika-testiranja` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomaknuti iz `ratified` u `accepted` samo
  `R13-C10-label-fallibility`, `R31-C10-ASA-home` i `R35-REACHBACK-10`, uz
  WC-C10 dokaz, ovaj paket, konačni commit i stvarni autorov odgovor;
- ostaviti prihvaćene korekcije `R01-C10-null-exchangeability`,
  `R01-C10-monte-carlo-correction` i `R01-C10-bayesian-balance`
  nepromijenjene;
- ostaviti poglavlje 6 u fazi `draft` i `H-WB-PART-001` netaknutim.

Nijedna druga stavka ni poglavlje nisu promijenili status.

## Granice koje odluka ne mijenja

C10 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge,
tag, arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao
poglavlje. C10 ne zatvara nijednu kasniju isporuku w10 umjesto njezina
vlastitoga ciljnog paketa i ne otvara WC-C11.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
status: accepted
author_reply: C10 accepted for 88b41d02fcea8222673f28a40938fe7db2aaffd6 on 2026-08-12.
reply_evidence: conversation:user-message-recorded-2026-08-12
```

Odgovor navodi točan završni WC-C10 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.

`WC-C11` se smije otvoriti tek nakon dovršenoga C10 closeouta, workflow
provjere i zasebnoga lokalnog commita.
