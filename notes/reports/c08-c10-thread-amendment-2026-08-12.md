# Autorski amandman za nit C08–C10

**Odluka:** `A-THREAD-C08-C10-2026-08-12`

**Datum:** 12. kolovoza 2026.

**Autor i urednik:** Luka Sikic

## Odluka

Za ovu nit uobičajeno pravilo zaustavljanja nakon jednoga paketa zamjenjuje se
strogo slijednim lancem:

```text
C08 -> WC-C09 -> C09 -> WC-C10 -> C10
```

Svaki paket ostaje zasebna jedinica rada. Najviše jedan paket smije imati
aktivnu pisanu bravu; svaki se paket zasebno claim-a, dokazuje, zatvara,
provjerava kroz `scripts/check-review-workflow.R` i commit-a prije claimanja
sljedećega paketa. Dokaz, brava ili nedovršena dispozicija ne prenose se preko
granice paketa.

Ova je odluka novi i zaseban zapis. Ne zamjenjuje
`A-THREAD-C07-C09-2026-08-11`, koji po vlastitim uvjetima završava nakon
closeouta `WC-C09` i prije prihvaćanja `C09`. Posebno ne zamjenjuje
`H-WC-C07-THREAD-SEQUENCE-001`: njegova dostava `before_close` za `C08` i
dostava `before_start` za `WC-C09` ostaju obvezne i moraju se potrošiti s
točnom dispozicijom na svojim vratima.

## Obvezni autorski odgovori

`C08`, `C09` i `C10` ne smiju se zatvoriti bez zasebnoga, točnog i datiranog
odgovora autora vezanog uz završni izvorni commit odgovarajućega poglavlja:

```text
Cxx accepted for <commit> on <date>.
```

Stalna delegacija od 5. kolovoza 2026. ne može zamijeniti te odgovore. Nijedan
paket ne smije zabilježiti da je autor pročitao poglavlje.

## Paketne granice

- `C08` odlučuje samo o zaključanom stanju poglavlja 8 i njegovu završnom
  panelu. ESS ostaje portalno posredovan, fakultativan i nepromoviran; lokalno
  paketiranje ostaje zabranjeno bez pisanoga dopuštenja vlasnika prava.
- `WC-C09` provodi ratificiranu kralježnicu `G-A2b-III`. Prije prvoga
  sadržajnog uređivanja priznaje sve primjenjive dolazne handoffove, a prije
  closeouta mora potrošiti `H-P0-REGISTER-008`, `H-P3-EXISTING-002` i
  `H-WB-C06-001`. Stavka `R32-CATALOG-paired-views` mora dobiti čitateljski
  zadatak koji reproducira objavljeni agregat. Završni izvor dobiva šest
  neovisnih kritičara.
- `C09` odlučuje samo o završnom stanju poglavlja 9 i njegovu panelu.
- `WC-C10` provodi ratificiranu korekciju `D01` prihvaćenu na `G-A1a` i
  kralježnicu `G-A2b-IV`. Veličina učinka i posljedice pogreške vode čitanje
  testa; povijest i zloupotrebe testiranja ostaju sastavni dio poglavlja.
  `H-WB-C06-001` mora biti potrošen prije closeouta, a završni izvor dobiva šest
  neovisnih kritičara.
- `C10` odlučuje samo o završnom stanju poglavlja 10 i njegovu panelu.

## Uvjeti zaustavljanja i granica ovlasti

Nit se zaustavlja prije sljedećega paketa ako stvarni dokaz ne zadovolji izlazni
test, ako ostane fatalan ili neriješen veliki nalaz panela ili ako bi zatvaranje
zahtijevalo izmišljanje broja, izvora, studije ili citata. Takvo je djelomično
izvršenje ispravan ishod.

Odluka ne spaja pakete, ne dopušta drugu pisanu bravu, ne ukida preduvjet,
handoff, stavku, panel, determinističku provjeru ni autorski odgovor. Ne
autorizira push, merge, tag, arhiviranje, deployment ili objavu.
