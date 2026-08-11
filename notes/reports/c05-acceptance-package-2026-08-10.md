# C05 — paket za autorovo prihvaćanje petoga poglavlja

**Gate:** `C05`

**Stanje gatea:** autor prihvatio; dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Šikić, autor/editor.

**Datum pripreme:** 10. kolovoza 2026.

**Datum autorove odluke:** 10. kolovoza 2026.

**Datum zapisa odluke:** 10. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor petoga poglavlja nalazi se u commitu
`de85c7018b934bf5c6310fd4f1125f0ae65473a0`. Taj commit mijenja
`chapters/05-vizualizacija.qmd`; nakon njega poglavlje nije mijenjano.

- SHA-256 radne datoteke u tom commitu:
  `db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`;
- Git blob poglavlja:
  `6c478a6efc6c80b44c2475849024db782d139076`;
- izvješće vertikalnoga reza:
  `notes/reports/wb-c05-2026-08-10.md`;
- memorandum o gustoći slika:
  `notes/reports/wb-c05-figure-density-2026-08-10.md`.

## Šest završnih izvješća

Svih šest perspektiva neovisno je i samo za čitanje pregledalo upravo navedeni
konačni SHA-256:

1. metode — `notes/reports/wb-c05-critic-methods-2026-08-10.md`;
2. skepticizam — `notes/reports/wb-c05-critic-skeptic-2026-08-10.md`;
3. pedagogija — `notes/reports/wb-c05-critic-pedagogy-2026-08-10.md`;
4. dokazi i citati — `notes/reports/wb-c05-critic-evidence-2026-08-10.md`;
5. stil — `notes/reports/wb-c05-critic-style-2026-08-10.md`;
6. struktura — `notes/reports/wb-c05-critic-structure-2026-08-10.md`.

Sinteza je
`notes/reports/wb-c05-six-critic-synthesis-2026-08-10.md`. Metode,
pedagogija, dokazi i citati, stil te struktura daju 5/5; skepticizam daje 4/5.
Nema fatalnoga ni velikoga nalaza.

## Otvoreni manji nalazi

Dva neblokirajuća skeptička nalaza ostaju u konačnom tekstu i nisu prešućena
ni popravljena tijekom pripreme C05:

1. tablica kaže da histogram ili krivulja gustoće čuva oblik cijele
   raspodjele, bez napomene da izbor razreda ili stupanj izglađivanja može
   promijeniti prividni oblik;
2. tvrdnja da boja prestaje raditi iznad tri ili četiri skupine zvuči kao
   univerzalan prag, premda ishod ovisi o zadatku, preklapanju, paleti,
   izravnim oznakama i drugim kanalima.

Dokazni kritičar bilježi još jedan manji nalaz izvan petoga poglavlja:
`data/README.md` zastario je u odnosu na kanonski katalog, a javni prikaz
Dodatka C još nije generiran. To je postojeća dokumentacijska obveza paketa
`P5-C`, već zapisana u `H-WB-C04-001` i `H-P3-CATALOG-002`; C05 je ne smije
potrošiti ni duplicirati.

## Sintetizirana dispozicija za odluku

Preporuka je **prihvatiti** konačno stanje uz vidljivo zadržavanje navedenih
manjih nalaza. Poglavlje vodi od Anscombeove vinjete preko gramatike grafike,
perceptivne preciznosti, izbora prikaza, ljestvice, malih višestrukih polja i
pristupačnosti do razrađenoga povratka Anscombeu i prijelaza prema povezanosti.

Namjerno odabrani mikrokorpus šest naslova transparentno daje 36 pojavnica, 28
oblika, 22 jednokratna i šest ponovljenih oblika. DigiKatov prikaz razdvaja
3.604 domene i 551.712 objava od mjesečnoga platformskog nazivnika, pokazuje
djelomični siječanj, prazninu od veljače do svibnja i lipanjski lom metode te
ne tvrdi trend, rast ni usporedbu prije i poslije loma.

Obvezni računski put koristi `anketa_mreze` s urednom licencom. `anscombe`
ostaje opcionalni lokalni R put bez kopiranja ili promocije. Widget ima četiri
dinamična opisa i oznake, živi status te tiskanu tablicu za sva četiri stanja.
Šest logičkih slika ima šest zasebnih argumentacijskih uloga; neposredni uvod
uz `fig-anscombe` prolazi blokirajući detektor, a popis registriranoga figurnog
duga sada je prazan.

HTML, PDF i omotačem izrađen DOCX prošli su na konačnom materijalnom stanju.
Citatne, podatkovne, pojmovne, stilske, rukopisne, figurne, widget i workflow
provjere također prolaze.

## Provedena dispozicija registra i knjige poglavlja

C05 je proveo sljedeću usku dispoziciju vezanu uz navedeni commit:

- `05-vizualizacija` u
  `bookwright_plugin/bookwright/shared/chapter-ledger.json` prelazi iz `draft`
  u `coauthor_review`, uz bilješku da prihvaćanje ne tvrdi da je autor pročitao
  poglavlje i da to nije faza `final`;
- sljedeće četiri stavke prelaze iz `ratified` u `accepted` uz dokaz WB-C05,
  C05 paketa, završnoga commita i stvarnoga autorova odgovora:

  - `R13-C05-frequency-visual`;
  - `R28-C05-introduction`;
  - `R28-C05-density`;
  - `R31-C05-Anscombe`.

Ni jedna druga stavka nije promijenila status. Sve četiri navedene stavke sada
su `accepted`, `05-vizualizacija` sada je `coauthor_review`, a C05 je zatvoren
kao `accepted`. To ne tvrdi da je autor pročitao poglavlje i ne proglašava ga
konačnim. Stalna delegacija od 5. kolovoza i amandman niti od 10. kolovoza nisu
upotrijebljeni umjesto odgovora koji je ovaj gate izričito zahtijevao.

## Granica slijeda

`H-C04-THREAD-SEQUENCE-001` priznat je pri claimu C05 i potrošen tek nakon
stvarne autorove odluke pri zatvaranju gatea. `WB-C06` je sljedeći dopušteni
paket i nije pokrenut u C05. Push, merge, tag, arhiviranje, deployment i objava
nisu dio ove odluke.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
status: accepted
author_reply: C05 accepted for de85c7018b934bf5c6310fd4f1125f0ae65473a0 on 2026-08-10.
reply_evidence: conversation:user-message-recorded-2026-08-10
```

Odgovor navodi točan završni izvorni commit i datum odluke. Ne tvrdi se da je
autor pročitao poglavlje.
