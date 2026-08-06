# C01 — paket za autorovo prihvaćanje prvoga poglavlja

**Gate:** `C01`

**Stanje gatea:** autor prihvatio; dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Šikić, autor/editor.

**Datum pripreme:** 6. kolovoza 2026.

**Datum autorove odluke:** 6. kolovoza 2026.

**Datum zapisa odluke:** 6. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor prvoga poglavlja nalazi se u commitu
`3b1706d42ea1bc56f0a909d895b04641872e85fd`. Taj commit mijenja
`chapters/01-zasto-statistika.qmd`; nakon njega poglavlje nije mijenjano.

- SHA-256 radne datoteke u tom commitu:
  `e16f109d399c820d65080b9da38f984aa3d68b195d73d5a30d54140ee2f7d946`;
- Git blob poglavlja:
  `99313b22f7174e0b6cef284d9c4972f852ea7914`;
- izvješće vertikalnoga reza:
  `notes/reports/wa-c01-2026-08-06.md`.

## Šest završnih izvješća

Svih šest perspektiva neovisno je i samo za čitanje pregledalo upravo navedeni
konačni SHA-256:

1. metode — `notes/reports/wa-c01-critic-methods-2026-08-06.md`;
2. skepticizam — `notes/reports/wa-c01-critic-skeptic-2026-08-06.md`;
3. pedagogija — `notes/reports/wa-c01-critic-pedagogy-2026-08-06.md`;
4. dokazi i citati — `notes/reports/wa-c01-critic-evidence-2026-08-06.md`;
5. stil — `notes/reports/wa-c01-critic-style-2026-08-06.md`;
6. struktura — `notes/reports/wa-c01-critic-structure-2026-08-06.md`.

Sinteza je
`notes/reports/wa-c01-six-critic-synthesis-2026-08-06.md`. Svih šest
perspektiva daje 5/5; nema preostaloga fatalnog, velikog ni manjeg nalaza.

## Sintetizirana dispozicija za odluku

Preporučena je dispozicija **prihvatiti** konačno stanje. Poglavlje provodi
ratificiranu kralježnicu, dodaje točno dvije odobrene definicije, uči životni
ciklus, četiri statističke djelatnosti, šest vrsta tvrdnji i šest auditnih
pitanja, te Berkeleyjski slučaj koristi bez lokalnih nepoduprtih brojki.
Obvezni brojčani rad koristi licencno čist `populacija_medija`, a HTML, PDF i
DOCX renderi te sve primjenjive pozitivne i negativne provjere prolaze.

Prihvat zatvara samo `R24-C01-modern-AI-history` i `R31-C01-Berkeley` te dopušta
da samo `01-zasto-statistika` prijeđe iz `draft` u `coauthor_review`. Ne znači
da je autor pročitao poglavlje, ne proglašava ga konačnim i ne pokreće
`WA-C02`.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
status: accepted
author_reply: C01 accepted for 3b1706d42ea1bc56f0a909d895b04641872e85fd on 2026-08-06.
reply_evidence: conversation:user-message-recorded-2026-08-06
```

Odgovor navodi točan završni izvorni commit i datum odluke. Ne tvrdi se da je
autor pročitao poglavlje.

## Provedena dispozicija knjige poglavlja

- `bookwright_plugin/bookwright/shared/chapter-ledger.json` za
  `01-zasto-statistika` promijenjen je iz `draft` u `coauthor_review`, uz
  bilješku vezanu uz završni commit i `C01`;
- prihvaćene su samo stavke `R24-C01-modern-AI-history` i
  `R31-C01-Berkeley`, s dokazima iz WA-C01 i C01;
- `C01` citira ovaj paket, završni commit, svih šest izvješća, sintezu, stvarni
  odgovor autora i dispoziciju knjige poglavlja;
- `OA-C01-ACCEPTANCE` je razriješen izravnim odgovorom u niti. Vanjska poruka
  nije poslana;
- kontrolni registar, ledger prosljeđivanja i nadzorna ploča usklađeni su prije
  završnih pozitivnih i negativnih workflow provjera.

`01-zasto-statistika` je sada `coauthor_review`. To nije faza `final`; kasniji
zatvarački, kontinuitetni i release gateovi ostaju obvezni. `WA-C02` nije
pokrenut u ovome paketu.
