# WC-C12 — sinteza šest kritičara

Panel je radio u tri zaključana read-only prolaza. Prvi prolaz nad SHA-256
`8c1a2b34fceb2c4d9402c3377c1aa1345f2b7b30a158e41e0476c8102bfd2937`
pronašao je tri major nalaza. Autor je 13. kolovoza 2026. odobrio samo te tri
obvezne dorade i ostavio sve minore za `C12`:

1. pet empirijskih ili postupovnih rečenica dobilo je vlastiti citat prema H7;
2. simulacija i tiskani prikaz premješteni su prije formule, uz odvojene upute
   koje odgovaraju digitalnim kontrolama i tiskanim krivuljama;
3. vidljivi receipt sveden je na početniku čitljiv trag i neposredno protumačen.

Prvi završni kandidat SHA-256 `29723f17…` zatvorio je ta tri nalaza, ali je
strukturna leća pronašla da pojednostavljeni receipt više ne prikazuje
ratificirano grananje između primarne sirove i alternativne standardizirane
analize. Taj kontraks razriješen je unutar treće odobrene dorade, bez promjene
zaključaka, izvora ili ocijenjenih zadataka.

Svih šest kritičara zatim je ponovno, neovisno i u cijelosti pročitalo isti
završni izvor:

- putanja: `chapters/12-kriza-i-obnova.qmd`
- SHA-256: `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`
- git blob: `bc9bb538625e6996f116ae1fd5b1acba56dc0852`

Pokriveni su statističke metode, skepticizam, pedagogija, dokazna osnova,
hrvatski rukopisni stil i struktura.

## Završni ishod

| Težina | Broj |
|---|---:|
| Fatalno | 0 |
| Major | 0 |
| Minor zapisi po lećama | 10 |

Panel prolazi za closeout `WC-C12` i izlaganje autoru u `C12`. Sinteza ne
bilježi prihvaćanje poglavlja niti tvrdi da ga je autor pročitao.

## Razrješenje obveznih nalaza

1. Svih pet označenih empirijskih ili postupovnih rečenica sada ima
   `[@wagenmakers2016]` u istoj rečenici. Dokazni i stilski kritičar potvrđuju
   nula nedostajućih tvrdnji i potpuni H7 prolaz.
2. Digitalna simulacija i tiskani prikaz prethode oznaci `m` i pragu `0,05/m`.
   Digitalne upute odgovaraju kontrolama, a tiskane krivuljama za 1, 12 i 48
   putova te pragovima 0,05 i 0,05 / 12.
3. Sedmeroredni receipt otvara kanonski CSV, provjerava 17 laboratorija i 1.894
   sudionika, označuje primarnu sirovu i alternativnu standardiziranu granu te
   prikazuje njihove provjerene procjene i intervale. Proza jasno kaže da
   isječak ne računa metaanalizu ponovno.

## Završni minori za C12

Deset zapisa po lećama grupira se u pet cjelina:

- kalibracija p-vrijednosti, modelom uvjetovana REML sinteza i načelno
  prihvaćanje registriranoga izvještaja;
- neimenovani sadržajni prag iza „malih” razlika i prejaka formulacija o
  vidljivosti koju reforma daje;
- ranija glosa replikacije te podsjetnik na jedinice sirove razlike i Cohenova
  `d`;
- nominalnost YAML podnaslova, izraz „ručna dispozicija” i ponovljeni završetak
  razrađenoga primjera.

Dokazna i strukturna leća nemaju završni minor. Minori nisu uređivani jer je
autor odobrio samo tri major popravka. Svi ostaju vidljivi za autorsku
dispoziciju u `C12`.

## Suglasnost panela

Svih šest leća potvrđuje da završni izvor nema fatalni ni major nalaz.
Metodološka, skeptička i dokazna leća prihvaćaju omeđenje RRR-a, forest plota,
osjetljivosti i simulacije. Pedagoška i stilska leća potvrđuju da je receipt
čitljiv početniku, ispod dvanaest redaka i bez zadatka proizvodnje koda.
Strukturna leća potvrđuje dva ratificirana definicijska bloka, jedan stvarni
RRR artefakt, vjerni widget/tiskani par, četiri razine zadataka i vidljivu
primarnu nasuprot alternativnoj grani.

Završna preporuka je zatvoriti `WC-C12` na stvarnim provjerama i predati točan
commit autoru kroz gate `C12`.
