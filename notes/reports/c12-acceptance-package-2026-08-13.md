# C12 — paket za autorovo prihvaćanje dvanaestoga poglavlja

**Gate:** `C12`

**Stanje gatea:** autor prihvatio; uska dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum autorove odluke:** 13. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor dvanaestoga poglavlja nalazi se u commitu
`23282e67cf876a3d654d1465f399ce48c31baacd`. Taj commit sadrži cijeli
`WC-C12` vertikalni rez, svih šest završnih izvještaja, sintezu i closeout
dokaze. Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`;
- git blob poglavlja: `bc9bb538625e6996f116ae1fd5b1acba56dc0852`;
- izvještaj vertikalnoga reza:
  `notes/reports/wc-c12-2026-08-13.md`;
- sinteza panela:
  `notes/reports/wc-c12-six-critic-synthesis-2026-08-13.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pregledalo je upravo navedeni završni
SHA-256:

1. metode — `notes/reports/wc-c12-critic-methods-2026-08-13.md`;
2. skepticizam — `notes/reports/wc-c12-critic-skeptic-2026-08-13.md`;
3. pedagogija — `notes/reports/wc-c12-critic-pedagogy-2026-08-13.md`;
4. dokazi i citati — `notes/reports/wc-c12-critic-evidence-2026-08-13.md`;
5. hrvatski stil — `notes/reports/wc-c12-critic-style-2026-08-13.md`;
6. struktura — `notes/reports/wc-c12-critic-structure-2026-08-13.md`.

Završni panel bilježi nula fatalnih, nula major i deset neblokirajućih minor
zapisa po lećama. Dokazna i strukturna leća nemaju završni minor. Zajednički
hash nije mijenjan nakon panela.

## Tri razrijeđena obvezna nalaza

Autor je 13. kolovoza 2026. prethodno odobrio samo tri major popravka prvoga
prolaza. Sva tri provedena su i ponovno neovisno provjerena:

1. pet empirijskih ili postupovnih rečenica sada ima vlastiti
   `[@wagenmakers2016]` citat u istoj rečenici;
2. digitalna simulacija i tiskani prikaz prethode formuli, a njihove zasebne
   upute odgovaraju stvarno dostupnim kontrolama odnosno krivuljama;
3. sedmeroredni vidljivi receipt čitljiv je početniku, provjerava 17
   laboratorija i 1.894 sudionika te jasno mapira primarnu sirovu i
   alternativnu standardiziranu granu bez ponovnoga računanja metaanalize.

Strukturni kritičar otkrio je da je prvi kandidat trećega popravka izgubio
mapiranje dviju grana. Završna inačica vratila je upravo to mapiranje unutar
već odobrenoga popravka i zatvorila posljednji major nalaz.

## Deset minor zapisa i autorska dispozicija

Točan odgovor autora prihvaća završni WC-C12 commit i sintezu panela. Sljedećih
deset zapisa zato je autoru izloženo, poznato i neblokirajuće za ovo izdanje;
nisu uređivani nakon zaključavanja izvora.

### Metode — 3

1. Kalibraciju p-vrijednosti moglo bi se vezati uz unaprijed određen cjelovit
   postupak pod njegovim pretpostavkama, a ne samo uz jednu analizu.
2. REML objedinjavanje moglo bi se izrijekom nazvati ponderiranim i modelom
   uvjetovanim, uz užu interpretaciju intervala modelskoga prosjeka.
3. Opis registriranoga izvještaja mogao bi dodati načelno prihvaćanje prije
   poznatoga ishoda kao glavni mehanizam protiv selekcije prema rezultatu.

### Skepticizam — 2

4. Izrazi „male razlike” i „male vrijednosti” ne navode zaseban sadržajni prag
   praktične važnosti, iako su omeđeni izvornom procjenom i ljestvicom.
5. Formulacija da reforma „daje” vidljiv i osporiv postupak mogla bi biti uža,
   jer provedba reforme ne jamči potpunu vidljivost ni osporivost.

### Pedagogija — 2

6. Replikacija se u vinjeti pojavljuje prije najjednostavnije početničke glose
   razlike prema reproducibilnosti.
7. Usporedba sirove razlike i Cohenova `d` mogla bi ranije podsjetiti da su
   jedinice bodovi odnosno standardne devijacije i da standardizacija mijenja
   relativne težine laboratorija.

### Hrvatski stil — 3

8. YAML podnaslov „Kako se znanstveni zaključci mogu popraviti” nije jasno
   nominalan niti potpuno pitanje s upitnikom.
9. Izraz „ručna dispozicija” ostaje administrativan i angliziran.
10. Završetak razrađenoga primjera djelomice ponavlja već izrečene granice.

Broj deset označuje zapise po lećama, ne nužno deset potpuno neovisnih
defekata. Nijedan završni kritičar nije ocijenio ijedan zapis fatalnim ili
velikim.

## Materijalna osnova prihvaćanja

Jedan provjereni višelaboratorijski RRR nosi cijeli put od izvorne tvrdnje,
analitičke fleksibilnosti i selekcije do kumulativnoga čitanja procjena,
reformi i njihovih granica. Vlastiti forest plot ne kopira izdavačev graf niti
uključuje sudioničke bajtove. Primarna sirova i alternativna standardizirana
grana ostaju vidljivo odvojene, a lokalni CSV ostaje urednički dokazni zapis.

Konceptni ledger i terminološki zapis slažu se s 49 živih definicija;
regenerirani graf ima 49 čvorova i 543 brida, bez duga. Widget i tiskani
blizanac prolaze paritet. Ciljani HTML, odobreni PDF wrapper i DOCX wrapper
imaju zabilježene prolaze. Sva četiri razreda zadataka mogu se riješiti bez
pisanja ili mijenjanja R koda.

## Provedena uska dispozicija

C12 nakon provjere točnoga odgovora provodi samo sljedeće:

- pomiče `12-kriza-i-obnova` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomiče iz `ratified` u `accepted` samo `R07-C12-full-argument`,
  `R08-SPINE-12`, `R11-C12-pipeline-flexibility`, `R19-C12-forest-plot`,
  `R19-C12-replication-cumulative`, `R23-C12-no-R-production`,
  `R23-C12-visible-receipt`, `R23-C12-code-ladder`,
  `R24-C12-primary-sources` i `R35-REACHBACK-12`;
- evidentira deset minor zapisa kao autoru izložene, poznate i neblokirajuće
  za ovo izdanje, bez promjene zaključanoga izvora;
- ostavlja poglavlje 6 u fazi `draft` i `H-WB-PART-001` netaknutim;
- ostavlja `WC-PARTS` neclaimanim i zaustavlja se prije njegova obveznog
  blast-radius pitanja autoru.

Nijedna druga stavka ni poglavlje ne mijenja status.

## Granice odluke

C12 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge,
tag, arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao
poglavlje. `WC-PARTS` se smije otvoriti tek nakon dovršenoga C12 closeouta,
workflow provjere i zasebnoga lokalnog commita; prije prve prozne izmjene mora
zaustaviti rad i autoru izložiti točan blast-radius popis.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
C12 accepted for 23282e67cf876a3d654d1465f399ce48c31baacd on 2026-08-13.
```

Odgovor navodi točan završni WC-C12 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.
