# C04 — paket za autorovo prihvaćanje četvrtoga poglavlja

**Gate:** `C04`

**Stanje gatea:** pripremljen; čeka autorovu odluku.

**Imenovani vlasnik odluke:** Luka Šikić, autor/editor.

**Datum pripreme:** 10. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor četvrtoga poglavlja nalazi se u commitu
`2a6ac10596a578e593e652204e06c30b6b3f1ed8`. Taj commit mijenja
`chapters/04-sazimanje-podataka.qmd`; nakon njega poglavlje nije mijenjano.

- SHA-256 radne datoteke u tom commitu:
  `7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`;
- Git blob poglavlja:
  `02a9c2dd88d7ffdc6e598c75ac77e9ae7801a081`;
- izvješće vertikalnoga reza:
  `notes/reports/wb-c04-2026-08-10.md`.

## Šest završnih izvješća

Svih šest perspektiva neovisno je i samo za čitanje pregledalo upravo navedeni
konačni SHA-256:

1. metode — `notes/reports/wb-c04-critic-methods-2026-08-10.md`;
2. skepticizam — `notes/reports/wb-c04-critic-skeptic-2026-08-10.md`;
3. pedagogija — `notes/reports/wb-c04-critic-pedagogy-2026-08-10.md`;
4. dokazi i citati — `notes/reports/wb-c04-critic-evidence-2026-08-10.md`;
5. stil — `notes/reports/wb-c04-critic-style-2026-08-10.md`;
6. struktura — `notes/reports/wb-c04-critic-structure-2026-08-10.md`.

Sinteza je
`notes/reports/wb-c04-six-critic-synthesis-2026-08-10.md`. Svih šest
perspektiva daje 5/5; nema preostaloga fatalnog, velikog ni manjeg nalaza.

## Sintetizirana dispozicija za odluku

Preporuka je **prihvatiti** konačno stanje. Poglavlje vodi čitatelja od izvora
i jedinice analize do provjerene analitičke tablice, sažetka i poštene granice
tvrdnje. Ispravan spoj čuva 438 redaka i 710.307 objava, a namjerno pogrešan
spoj daje 3.571 redak i 5.959.081 objavu. Oba su puta zaključana asercijama i
nose točno jednu pogrešku u modelskoj reviziji.

DigiKatov slučaj ne tvrdi trend kroz 2024., ne prelazi lipanjski lom metode, ne
uspoređuje dostupne i strukturno nedostupne metrike te svaki udio iz datoteke
domena veže uz nazivnik 551.712. Sažetak domena, prikaz u HTML-u i tiskani put
slažu se na sredini 153,0832, medijanu 4 i prvih deset domena s 148.748 objava.

Poglavlje ima točno četiri odobrena definicijska bloka. Concept ledger,
terminološki živi broj i graf usklađeni su na 47 definicija, uz nula duga i
svjež graf. Widget i statični blizanac koriste ista tri provjerena stanja, a
upravljani agregat omogućuje dovršiv tiskani računski zadatak.

HTML, PDF i DOCX renderi te citatne, podatkovne, pojmovne, terminološke,
stilske, rukopisne i figurne provjere prošli su na konačnom materijalnom
stanju.

## Otvorene obveze izvan C04

Nema neriješenoga nalaza protiv četvrtoga poglavlja. Handoff
`H-WB-C04-001` bilježi samo buduću dokumentacijsku obvezu: paket `P5-C` mora
uskladiti zastarjelu tvrdnju o promociji u `data/README.md` s kanonskim
katalogom. Ta obveza ne mijenja ishod C04 i C04 je ne smije potrošiti.

Registrirani dug uvoda uz `fig-anscombe` pripada paketu `WB-C05`; ostaje otvoren
i nije nalaz protiv četvrtoga poglavlja.

## Predložena dispozicija registra i knjige poglavlja

Ako autor prihvati ovaj paket vezan uz navedeni commit, C04 treba provesti
sljedeću usku dispoziciju:

- `04-sazimanje-podataka` u
  `bookwright_plugin/bookwright/shared/chapter-ledger.json` prelazi iz `draft`
  u `coauthor_review`, uz bilješku da prihvaćanje ne tvrdi da je autor pročitao
  poglavlje i da to nije faza `final`;
- sljedećih šest stavki prelazi iz `ratified` u `accepted` uz dokaz WB-C04,
  C04 paketa, završnoga commita i stvarnoga autorova odgovora:

  - `R08-C04-engagement-source`;
  - `R11-C04-raw-to-table`;
  - `R11-C04-wrong-join-AI`;
  - `R11-C04-missingness`;
  - `R13-C04-denominators`;
  - `R32-C04-static`.

Ni jedna od tih promjena još nije provedena. Poglavlje ostaje `draft`, svih
šest stavki ostaje `ratified`, a C04 ostaje otvoren dok autor ne odgovori.
Stalna delegacija od 5. kolovoza ne zamjenjuje odgovor koji ovaj gate izričito
zahtijeva.

## Točan odgovor autora

Za prihvaćanje odgovorite doslovno:

```text
C04 accepted for 2a6ac10596a578e593e652204e06c30b6b3f1ed8 on 2026-08-10.
```

Ili navedite točne blokirajuće revizije vezane uz isti commit. Odgovor ne mora
tvrditi da ste pročitali poglavlje; on prihvaća sintetiziranu dispoziciju.

Push, merge, tag, arhiviranje, deployment i objava nisu dio ove odluke.
