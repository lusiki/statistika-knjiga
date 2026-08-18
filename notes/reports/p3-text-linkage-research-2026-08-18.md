# P3-TEXT — istraživanje izvornoga izdanja za povezivanje

**Datum:** 18. kolovoza 2026.

**Status:** dovršeno istraživanje; `P3-TEXT` ostaje `in_progress` i blokiran.

**Ovlast:** `A-P3-TEXT-LINKAGE-RESEARCH-2026-08-18`.

## Zaključak

Ne postoji službeno izdanje ParlaMint-HR koje se može dokazati kao izvor
hrvatskoga dijela ParlaSenta 1.0 i koje zadovoljava prihvaćeni uvjet jedne
jedinstvene veze za svih 1.336 hrvatskih ispitnih redaka.

ParlaMint 3.0 jedino je službeno izdanje objavljeno prije ParlaSenta 1.0 koje
obuhvaća cijeli potreban hrvatski vremenski raspon. Njegova službena
`ParlaMint-HR.tgz` arhiva prolazi objavljeni MD5, ali daje potpuno isti
fail-closed rezultat kao ParlaMint 5.0: 1.297 jedinstvenih veza, 24 retka bez
veze i 15 višestrukih veza. Nijedan redak nije odbačen, pogođen neizrazitim
povezivanjem ili dodijeljen prvom pronađenom govoru.

Izvorni članak ParlaSenta uklanja preostalu dvojbu o provenijenciji. Za
Hrvatsku izrijekom navodi CROCorp i njegov DOI, dok ParlaMint 3.0 navodi za
češki, slovenski i britanski korpus. CROCorp je zaseban korpus; nije
ParlaMint-HR izdanje. Njegov službeni Zenodo zapis označava izdanje 1.1.1,
razdoblje 2003.–2020. i licencu CC BY 4.0. Taj izvor nije odabran, dohvaćen ni
prihvaćen za nastavni paket.

## Službeni zapisi i vremenska eliminacija

| Izdanje | Službeni zapis | Datum izdanja | Hrvatska arhiva | Dispozicija |
|---|---|---:|---|---|
| ParlaMint 1.0 | CLARIN.SI `11356/1345` | 2020-10-15 | `ParlaMint-HR.zip`, MD5 `01ef392a95587ba35b6f109e61f68be1` | Arhiva obuhvaća samo 2016-11-15 – 2020-05-17; 873 od 1.336 hrvatskih ispitnih redaka starija su od 2016. |
| ParlaMint 2.1 | CLARIN.SI `11356/1432` | 2021-06-18 | `ParlaMint-HR.tgz`, MD5 `cf2ce85cb3d61df368d8bbfe2635988a` | Isti raspon 2016-11-15 – 2020-05-17; ne može sadržavati 873 ranija retka. |
| ParlaMint 3.0 | CLARIN.SI `11356/1486` | 2023-07-04 | `ParlaMint-HR.tgz`, MD5 `4191e37352aaf96166af03b3214ac671` | Vremenski moguć, ali empirijski pada s potpisom 1.297/24/15. |
| ParlaMint 4.0 | CLARIN.SI `11356/1859` | 2023-10-24 | `ParlaMint-HR.tgz`, MD5 `723497dac7ab24ca5863450a45d20819` | Objavljen nakon ParlaSenta 1.0 od 2023-09-18; ne može biti njegovo izvorno izdanje. |
| ParlaMint 4.1 | CLARIN.SI `11356/1912` | 2024-06-03 | `ParlaMint-HR.tgz`, MD5 `f8d8308fd03d9fda5bf9647fbff8f85e` | Objavljen nakon ParlaSenta 1.0. |
| ParlaMint 5.0 | CLARIN.SI `11356/2004` | 2025-07-08 | `ParlaMint-HR.tgz`, MD5 `b852098ae5c2561aef1de43f44e09a77` | Već prihvaćeni kandidat; pada s istim potpisom 1.297/24/15. |

Službeni GitHub tag `v2.0` jest verzionirano stanje shema, skripti i uzoraka,
ali nije pronađen zaseban puni CLARIN.SI hrvatski korpus 2.0. To ne mijenja
zaključak: javne pune hrvatske arhive 1.0 i 2.1 imaju isti raspon koji izostavlja
873 potrebna retka, a članak izvor hrvatskih rečenica veže uz CROCorp.

## Provjerene lokalne kandidatske kopije

Sve su kopije u git-ignoriranoj mapi `data/_kandidat/p3-text/research/`.

| Datoteka | Bajtova | Objavljeni i potvrđeni MD5 | Lokalni SHA-256 |
|---|---:|---|---|
| `ParlaMint-HR-1.0.zip` | 96.722.649 | `01ef392a95587ba35b6f109e61f68be1` | `a49a9e72efe6781190d926ccf3b9de4802e409bbcfb92797dadd6e003dca6a1e` |
| `ParlaMint-HR-2.1.tgz` | 96.140.762 | `cf2ce85cb3d61df368d8bbfe2635988a` | `b24411e9a5f94a65a33fe25e64a7f9be1e03ac408741ee4dc98c5320fc44914d` |
| `ParlaMint-HR-3.0.tgz` | 405.033.822 | `4191e37352aaf96166af03b3214ac671` | `773c8d6e10415fdea3003b154c310f923652df54aef66c82e7f5650488bf350b` |
| ParlaSent članak, arXiv v1 source | 28.660 | bez objavljenoga checksum pina | `6bbea7609405613d4953412b1cd2c427f10d13a097d0afa2e61571d67da20bcd` |

ParlaMint 3.0 audit pokrenut je proširenim, ali unatrag kompatibilnim
`scripts/check-text-package.py`. Isti normalizacijski i povezivački ugovor kao
za 5.0 daje:

```text
TEXT_LINK_AUDIT train_rows=1387 train_linked=1340 train_no_link=18 train_ambiguous=29 test_rows=1336 test_linked=1297 test_no_link=24 test_ambiguous=15 source_document_overlap=20 resolved_speech_overlap=40
```

Zadani 5.0 poziv i dalje reproducira isti pinani blocker. Istraživački CLI
zahtijeva zajedno put do službene arhive, objavljeni MD5 i raspakiranu
plain-text mapu; nepotpun trojac ili pogrešan MD5 pada prije povezivanja.

## Službena provenijencija

- ParlaSent 1.0: <https://www.clarin.si/repository/xmlui/handle/11356/1868>
- izvorni članak ParlaSenta v1: <https://arxiv.org/abs/2309.09783v1>
- CROCorp zapis koji članak navodi za Hrvatsku:
  <https://doi.org/10.5281/zenodo.6521372>
- ParlaMint 1.0: <https://www.clarin.si/repository/xmlui/handle/11356/1345>
- ParlaMint 2.1: <https://www.clarin.si/repository/xmlui/handle/11356/1432>
- ParlaMint 3.0: <https://www.clarin.si/repository/xmlui/handle/11356/1486>
- ParlaMint 4.0: <https://www.clarin.si/repository/xmlui/handle/11356/1859>
- ParlaMint 4.1: <https://www.clarin.si/repository/xmlui/handle/11356/1912>
- ParlaMint 5.0: <https://www.clarin.si/repository/xmlui/handle/11356/2004>
- službeni ParlaMint tagovi: <https://github.com/clarin-eric/ParlaMint/tags>

## Dispozicija

Istraživački gate staje bez odabira izvora. Nema nastavnog CSV-a, putovnice,
licenčne obavijesti, kataloške promjene, promocije, empirijskoga rezultata ili
izmjene poglavlja. `P3-TEXT` ostaje aktivan i neprihvaćen, a `P3-VERIFY`,
`WD-C17` i `C17` ostaju blokirani.

Sljedeća dopuštena radnja jest zasebna autorska odluka: ili redizajnirati paket
kao ParlaSent-only bez govorne veze i bez triju izvorno prihvaćenih slojeva, ili
ukloniti empirijski tekstni paket iz prvoga izdanja. CROCorp se ne smije dodati
kao treća opcija bez novoga, zasebnog odabira izvora i prava.
