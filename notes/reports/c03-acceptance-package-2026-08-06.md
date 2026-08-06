# C03 — paket za autorovo prihvaćanje trećega poglavlja

**Gate:** `C03`

**Stanje gatea:** pripremljen; čeka autorovu odluku.

**Imenovani vlasnik odluke:** Luka Šikić, autor/editor.

**Datum pripreme:** 6. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor trećega poglavlja nalazi se u commitu
`72f774a3b302e6beca14730ac82727be92f29be1`. Taj commit mijenja
`chapters/03-kako-brojke-zavode.qmd`; nakon njega poglavlje nije mijenjano.

- SHA-256 radne datoteke u tom commitu:
  `11e949a5f4bfa3f762a6b3ad4f2f3e6a36333cdd2fbfae08103d2fcd8263bad5`;
- Git blob poglavlja:
  `5ecef6c96379af17e03c30e6facc5a191a670618`;
- izvješće vertikalnoga reza:
  `notes/reports/wa-c03-2026-08-06.md`.

## Šest završnih izvješća

Svih šest perspektiva neovisno je i samo za čitanje pregledalo upravo navedeni
konačni SHA-256:

1. metode — `notes/reports/wa-c03-critic-methods-2026-08-06.md`;
2. skepticizam — `notes/reports/wa-c03-critic-skeptic-2026-08-06.md`;
3. pedagogija — `notes/reports/wa-c03-critic-pedagogy-2026-08-06.md`;
4. dokazi i citati — `notes/reports/wa-c03-critic-evidence-2026-08-06.md`;
5. stil — `notes/reports/wa-c03-critic-style-2026-08-06.md`;
6. struktura — `notes/reports/wa-c03-critic-structure-2026-08-06.md`.

Sinteza je
`notes/reports/wa-c03-six-critic-synthesis-2026-08-06.md`. Svih šest
perspektiva daje 5/5; nema preostaloga fatalnog, velikog ni manjeg nalaza.

## Sintetizirana dispozicija za odluku

Preporuka je **prihvatiti** konačno stanje. Jedan portalno posredovan DIP-ov
slučaj nosi cijeli argument. Pet službenih veličina ostaje razdvojeno,
aritmetika je ponovljiva, a doseg ne prelazi opis službenoga zapisa i omeđenu
uredničku odluku. Poglavlje ne izvodi potporu listama, individualne uzroke,
ekološke zaključke, lokalni DIP-ov skup, pravo redistribucije ni budući portalni
paritet.

Dodana je točno jedna definicija, `temeljna stopa`. Concept ledger,
terminološki živi broj i graf usklađeni su na 49 definicija, uz nula duga i
svjež graf. Widget kod i `data/widgets.json` nisu promijenjeni; kanonska uputa,
digitalni prikaz i statični blizanac prolaze ugovor i paritet.

Upravljani generirani skup daje izvanmrežni zadatak s jedinicom generirane
osobe. DZS-ov dolazak nije pretvoren u osobu, administrativni i anketni brojevi
nisu zbrojeni, a zaokruženi ostatak ±1 nije proglašen pogreškom. Nema tvrdnje o
dopuštenju nositelja prava.

HTML, PDF i DOCX renderi, neovisni računi, DIP portal, inventar, tokeni,
integritet rukopisa, figure, citati, pojmovi, terminologija, kralježnice,
katalog, podaci, widgeti, paritet i workflow prolaze. Obje negativne workflow
probe padaju s očekivanim izlazom 1.

## Predložena dispozicija registra i knjige poglavlja

Ako autor prihvati ovaj paket vezan uz navedeni commit, C03 treba provesti
sljedeću usku dispoziciju:

- `03-kako-brojke-zavode` u
  `bookwright_plugin/bookwright/shared/chapter-ledger.json` prelazi iz `draft`
  u `coauthor_review`, uz bilješku da prihvaćanje ne tvrdi da je autor pročitao
  poglavlje i da to nije faza `final`;
- sljedećih devet stavki prelazi iz `ratified` u `accepted` uz dokaz WA-C03,
  C03 paketa, završnoga commita i stvarnoga autorova odgovora:

  - `R07-C03-full-argument`;
  - `R10-C03-base-rate`;
  - `R12-C03-poll-literacy`;
  - `R12-C03-margin-debt`;
  - `R23-C03-no-R-production`;
  - `R24-C03-synthetic-media`;
  - `R24-C03-AI-provenance`;
  - `R30-C03-slide-enumeration`;
  - `R31-C03-public-case`.

Ni jedna od tih promjena još nije provedena. Poglavlje ostaje `draft`, svih
devet stavki ostaje `ratified`, a C03 ostaje otvoren dok autor ne odgovori.

## Točan odgovor autora

Za prihvaćanje odgovorite doslovno:

```text
C03 accepted for 72f774a3b302e6beca14730ac82727be92f29be1 on 2026-08-06.
```

Ili navedite točne blokirajuće revizije vezane uz isti commit. Odgovor ne mora
tvrditi da ste pročitali poglavlje; on prihvaća sintetiziranu dispoziciju.

Push, merge, tag, arhiviranje, deployment i objava nisu dio ove odluke.
