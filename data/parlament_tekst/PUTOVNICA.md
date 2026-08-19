# Putovnica podataka — ParlaSent HR rečenice

## Što predstavlja jedan redak?

Jedan redak predstavlja jednu hrvatsku parlamentarnu rečenicu koju nosi
službena datoteka ParlaSent BCS 1.0 za učenje ili ispitivanje. Redak nije cijeli
govor, govornik, zastupnik ni reprezentativan uzorak Hrvatskoga sabora.

## Izvor, inačica i licenca

- izvor: **The multilingual sentiment dataset of parliamentary debates
  ParlaSent 1.0**, CLARIN.SI `11356/1868`;
- inačica i datum izdanja: 1.0, 18. rujna 2023.;
- izvorne datoteke: `ParlaSent_BCS.jsonl`,
  `ParlaSent_BCS_test.jsonl` i `README.txt`;
- licenca izvedene datoteke: CC BY-SA 4.0;
- atribucija, izvorni i izvedeni checksumovi te označene promjene:
  `data/parlament-oznake.LICENCA.md`.

Promovirana nastavna datoteka jest `data/parlament_oznake.csv`. Ima 2.698
redaka, MD5 `55b1c4263009ab783911f094907312d9` i SHA-256
`0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`.

## Kako je nastao hrvatski rez?

Obje izvorne BCS datoteke imaju po 2.600 redaka i doslovno polje `country` s
vrijednostima `BiH`, `HR` i `SRB`. Odabir koristi samo `country = HR`; zemlja
se ne izvodi iz imena, stranke ili teksta.

- datoteka za učenje sadrži 1.387 hrvatskih redaka u 1.198 dokumenata;
- izvorna ispitna datoteka sadrži 1.336 hrvatskih redaka u 1.321 dokumentu i
  svi su zadržani;
- 20 dokumenata pojavljuje se u obje izvorne datoteke, pa je iz datoteke za
  učenje uklonjeno svih njihovih 25 redaka;
- nakon uklanjanja ostaje 1.362 retka u 1.178 dokumenata za novo razdvajanje.

Nijedan redak nije odabran ili uklonjen prema sentimentnoj oznaci.

## Razdvajanje bez dokumentnoga curenja

Izvorna ispitna datoteka ostaje netaknut `ispitivanje`. Za svaki preostali
dokument iz datoteke za učenje računa se:

```text
SHA256("statistika-p3-text-parlasent-only-v1|" + document_id)
```

Prvih 16 heksadekadskih znakova tumači se kao 64-bitni cijeli broj. Dokument
ulazi u `provjera` ako je broj manji od `floor(0,20 × 2^64)`; inače ulazi u
`ucenje`. Svi redci istoga dokumenta zato uvijek ostaju zajedno. Konstanta nije
naknadno ugađana prema rezultatu.

| Izvedeni skup | Redaka | Dokumenata | Negative | Neutral | Positive |
|---|---:|---:|---:|---:|---:|
| `ucenje` | 1.090 | 944 | 530 | 343 | 217 |
| `provjera` | 272 | 234 | 122 | 90 | 60 |
| `ispitivanje` | 1.336 | 1.321 | 560 | 546 | 230 |

## Kako je nastala zabilježena oznaka?

Put oznake nije jednak u dvjema izvornim datotekama.

- Redci iz datoteke za učenje nose `annotator1`, `annotator2`,
  `reconciliation` i trostupanjski `label`. U nastavnoj tablici njihov je
  `label_path = dva_kodera_i_uskladjenje`.
- Redci iz ispitne datoteke imaju jednoga uvježbanog kodera i trostupanjski
  `label`. Drugi koder, usklađenje i izvorni split nisu dostupni; nisu
  izmišljeni. U tablici su označeni kao `nije_dostupno_iz_izvora`, a
  `label_path = jedan_uvjezbani_koder`.

`recorded_label` može biti `Negative`, `Neutral` ili `Positive`. To je
zabilježeni referentni ishod, ne istina o rečenici ili namjeri govornika.

## Što je izostavljeno?

Paket ne uključuje vezu na ParlaMint-HR, cijeli govor, ime govornika, stranku,
spol, godinu rođenja, ulogu vlasti/opozicije ni izvedene mjere govora. CROCorp
nije odabran ni dohvaćen. Izostavljanje tih polja sprječava da rečenični
klasifikacijski zadatak prešutno postane tvrdnja o govornicima ili korpusu
govora.

## Dopuštene i nedopuštene tvrdnje

Paket dopušta:

- opis odabranih označenih rečenica i dvaju putova nastanka oznake;
- provjeru dokumentnoga razdvajanja na skup za učenje, provjeru i ispitivanje;
- vrednovanje klasifikatora prema zabilježenom referentnom ishodu;
- raspravu o pragu, tablici zabune i uvjetnim nazivnicima pogrešaka.

Paket ne dopušta:

- procjenu prevalencije sentimenta u Hrvatskome saboru;
- tvrdnju o namjeri, stavu ili osobini govornika;
- uzročnu tvrdnju;
- generalizaciju na neoznačene rečenice ili druge parlamente;
- tvrdnju da zabilježena oznaka predstavlja istinu.

## Tko snosi teret pogreške?

Okvir oznaka odredili su autori izvornoga skupa. Pogrešna oznaka ili odluka o
slanju rečenice u ljudski pregled može neopravdano povećati ili smanjiti pažnju
usmjerenu na javni govor. Zato poglavlje mora prikazati odvojene nazivnike
pogrešaka, mogućnost osporavanja oznake, ljudski pregled i praćenje nakon
uvođenja. Ovaj podatkovni paket sam ne uspostavlja postupak žalbe.

## Reprodukcija

```text
python scripts/build-text-package.py
python scripts/check-text-package.py
```

Prva naredba bez `--write` dokazuje da se promovirani CSV reproducira bajt po
bajt. Druga neovisno provjerava izvorne MD5/SHA-256 vrijednosti, sheme, hrvatski
rez, uklanjanje dokumenta, split, put oznake, brojnosti i izvedene checksumove.
