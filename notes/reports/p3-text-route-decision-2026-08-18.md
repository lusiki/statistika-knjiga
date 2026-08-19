# P3-TEXT — odluka o ParlaSent-only ruti

**Datum odluke:** 18. kolovoza 2026.

**Vlasnik odluke:** Luka Sikic, autor/editor.

**Paket:** aktivni `P3-TEXT`.

## Točan odgovor autora

```text
P3-TEXT-ROUTE accepted as recommended: ParlaSent-only for ParlaSent BCS SHA256 c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98 and ParlaSent BCS test SHA256 412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0 on 2026-08-18.
```

Odgovor je primljen u razgovoru i točno odgovara zahtjevu
`OA-P3-TEXT-ROUTE`.

## Prihvaćena ruta

`P3-TEXT` se redizajnira kao ParlaSent-only paket vezan uz dvije nepromijenjene
službene datoteke iz zapisa ParlaSent 1.0, CLARIN.SI `11356/1868`:

- `ParlaSent_BCS.jsonl`, SHA-256
  `c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98`;
- `ParlaSent_BCS_test.jsonl`, SHA-256
  `412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0`.

Zadržavaju se svi retci s doslovnim izvornim poljem `country = HR` iz
ispitne datoteke. Iz hrvatskih redaka datoteke za učenje najprije se uklanjaju
cijeli izvorni dokumenti čiji se `document_id` pojavljuje u ispitnoj datoteci.
Preostali se dokumenti deterministički razdvajaju na skup za učenje i skup za
provjeru jednom javno zapisanom SHA-256 funkcijom i konstantom. Ne
uravnotežuju se oznake i nijedan se redak ne uklanja prema rezultatu.

Izlaz je samo jedna rečenična nastavna tablica, `data/parlament_oznake.csv`,
pod CC BY-SA 4.0. Ona čuva izvorne ključeve, izvornu ulogu datoteke,
izvedeni skup, trostupanjsku zabilježenu oznaku, dostupne pojedinačne oznake i
točan put njihova nastanka. Za ispitne retke ne izmišljaju se drugi koder,
usklađenje ni izvorni split.

`WD-C17` ostaje jedini analitički potrošač. Paket podupire samo omeđenu
nastavnu odluku o slanju rečenice u ljudski pregled te provjeru selekcije,
puta oznake, razdvajanja, praga i uvjetnih nazivnika pogrešaka. Ne podupire
tvrdnju o prevalenciji sentimenta, govornom kontekstu, namjeri govornika,
uzročnosti ili generalizaciji izvan odabranih označenih rečenica.

## Uklonjeni dijelovi ranije prihvaćene kompozicije

Ova odluka uklanja svaku vezu na ParlaMint-HR, polja govornoga konteksta,
ParlaMint-only izlaze `parlament_govori.csv` i `parlament_mjere.csv`, obećanje
triju povezanih razina i test jedinstvene veze na govor. `parlamint_hr` ostaje
registriran, nepromoviran i bez datoteka; više nije potrošač ni sastavnica
prvoga izdanja tekstnoga paketa. CROCorp nije treća prešutna ruta: nije
odabran, dohvaćen ni prihvaćen.

## Prava i granica ovlasti

Izvedena rečenična tablica zadržava ParlaSentovu licencu CC BY-SA 4.0 i
ShareAlike obvezu. Obavijest mora navesti autore, puni naslov i inačicu,
izdavatelja, trajni zapis, licencu i promjene: hrvatski rez, uklanjanje
dokumenata koji prelaze granicu ispitivanja, dokumentno razdvajanje,
preimenovanje polja i evidentiranje puta oznake. MIT licenca koda knjige ne
obuhvaća podatke treće strane. Ne tvrdi se posebno dopuštenje nositelja prava;
nijedno nije traženo.

Ova odluka sama ne prihvaća izvedene bajtove, brojnosti, split, checksum,
putovnicu, licenčnu obavijest, katalog, promociju, empirijski rezultat ni
izmjenu 17. poglavlja. `P3-TEXT` mora zasebno izgraditi i dokazati paket,
potrošiti `H-P3-DZS-003`, proći pozitivne provjere i namjerne negativne
fixturee te tek tada zatvoriti paket. `P3-VERIFY`, `WD-C17` i `C17` ostaju
blokirani do toga closeouta.

Ne tvrdi se autorovo čitanje, testiranje novim čitateljima, izmjereno vrijeme
čitanja ni neovisna terminološka recenzija. Odluka ne dopušta push, merge, tag,
arhiviranje, deployment ni objavu.
