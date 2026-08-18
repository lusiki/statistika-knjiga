# P3-TEXT — odluka o omeđenom istraživanju povezivanja

**Datum odluke:** 18. kolovoza 2026.

**Vlasnik odluke:** Luka Sikic, autor/editor.

**Paket:** aktivni `P3-TEXT`.

## Točan odgovor autora

```text
P3-TEXT-LINKAGE-RESEARCH approved for ParlaMint-HR SHA256 bb78b3611e313f9eb3139a036e22ab2f6c543648915af9c5e390460f7d725b8c and ParlaSent BCS test SHA256 412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0 on 2026-08-18.
```

Odgovor je primljen u razgovoru 18. kolovoza 2026. i točno odgovara zahtjevu
`OA-P3-TEXT-LINKAGE-RESEARCH`.

## Odobreni opseg

Smiju se pregledati i, samo u git-ignoriranu kandidatsku zonu, dohvatiti
službena, verzionirana i licencirana izdanja ParlaMint-HR radi utvrđivanja
točnoga izdanja iz kojega je izveden ParlaSent 1.0. Svaki kandidat mora imati
službeni zapis o verziji i licenci te provjerljiv checksum. Provjera uspijeva
samo ako svih 1.336 redaka ParlaSent BCS testa s izvornim poljem `country = HR`
dobije točno jednu vezu s govorom, bez neizrazitoga povezivanja, nagađanja ili
izbacivanja retka.

Odluka je vezana uz već opažena stanja:

- ParlaMint-HR 5.0 SHA-256
  `bb78b3611e313f9eb3139a036e22ab2f6c543648915af9c5e390460f7d725b8c`;
- ParlaSent BCS test 1.0 SHA-256
  `412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0`.

## Granica ovlasti i stop-pravila

Ova odluka ne odabire drugo izdanje ParlaMint-HR, ne prihvaća njegova prava za
nastavni paket, ne mijenja `G-A3-TEXT`, ne stvara nastavne CSV datoteke,
putovnicu ili licenčnu obavijest, ne mijenja katalog i ne dopušta promociju.
`P3-TEXT` ostaje `in_progress`; `P3-VERIFY`, `WD-C17` i `C17` ostaju blokirani.

Ako jedno točno službeno izdanje zadovolji uvjet 1.336 od 1.336 jedinstvenih
veza, rad staje radi zasebne autorske odluke o odabiru izvora i pravima prije
uporabe toga izdanja. Ako nijedno izdanje ne zadovolji uvjet, zapisuje se novi
blokator i rad staje radi zasebne odluke o ParlaSent-only redizajnu ili
uklanjanju empirijskoga paketa.

Ne tvrdi se dopuštenje nositelja prava, autorsko čitanje, čitateljsko
testiranje, izmjereno vrijeme čitanja ni neovisna terminološka recenzija. Odluka
ne dopušta push, merge, tag, arhiviranje, deployment ni objavu.
