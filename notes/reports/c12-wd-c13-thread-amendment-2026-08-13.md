# Autorski amandman — WC-C12 do WD-C13

**Odluka:** `A-THREAD-C12-WD-C13-2026-08-13`

**Autor i urednik:** Luka Sikic

**Datum odluke:** 13. kolovoza 2026.

**Ulazno stanje:** P3-VERIFY-C closeout commit
`f86d2d8d042a187291b39a95d9d73de4c375f679`.

## Odluka

Za ovu nit pravilo zaustavljanja nakon jednoga paketa zamjenjuje se strogim
slijedom `WC-C12`, `C12`, `WC-PARTS`, `P3-VERIFY-D`, `WD-C13`. Svaki paket
ostaje zasebna transakcija s vlastitim claimom, jednom aktivnom write-lockom,
dokazima, dispozicijama handoffa, provjerama pri claimu i closeoutu te
ograničenim lokalnim commitom. Nijedan lock, dokaz ni nedovršena dispozicija ne
prenosi se preko granice paketa.

Ovo je nova odluka. Razlikuje se od ranijih thread-amandmana, čiji su se lanci
završili na vlastitim granicama, i ne mijenja ih retroaktivno.

## Obvezna zaustavljanja

`C12` se ne može zatvoriti bez točnoga datiranog odgovora autora vezanog uz
završni izvorni commit poglavlja. Stalna delegacija od 5. kolovoza nije zamjena
za taj odgovor i nijedan zapis ne smije tvrditi da je autor pročitao poglavlje.
Traženi oblik odgovora glasi `C12 accepted for <commit> on <date>.`

`WC-PARTS` mora se zaustaviti prije prve izmjene proze. Autor najprije dobiva
točan popis jedinica koje bi paket mijenjao, njihov trenutačni stage i opis
svake izmjene. Zatim bira hoće li prihvatiti pošteno vraćanje svih materijalno
izmijenjenih prihvaćenih jedinica u `draft` i njihove svježe panele ili će paket
ograničiti na aditivne mostove i samoprovjere koje ne mijenjaju prihvaćena
tijela poglavlja.

## Granice pojedinih paketa

`WC-C12` provodi samo ratificirani brif `G-A4-12`, kralježnicu `G-A2b-IV` i
dokazni paket `P3-EVIDENCE12`. Smije upotrijebiti samo provjerene izvore i
brojke, mora provesti puni panel od šest neovisnih kritičara i ne smije
zatvoriti fatalan ili neriješen veliki nalaz.

`P3-VERIFY-D` provjerava svaki preduvjet zasebno protiv jednoga deklariranog
izvornog stanja, ponavlja determinističke provjere i negativne fixturee te
izrijekom navodi koje su jedinice nakon `WC-PARTS` u `draft`, a koje u
`coauthor_review`.

`WD-C13` zadržava ESS Round 11 edition 3.0 kao portalom posredovanu, neobveznu
i nepromoviranu rutu. Ne smije tvrditi da je ESS lokalno pakiran, da izdanja
imaju datotečnu parnost ni da postoji dopuštenje nositelja prava. Obvezni
offline studentski zadatak mora imenovati svoju licencno čistu lokalnu
alternativu. Terminologija ostaje usklađena s činjenicom da je 13. poglavlje
ratificirani preduvjet 17. poglavlja.

Poglavlje 6 ostaje namjerno u `draft` pod `H-WB-PART-001`. Ovaj amandman ne
odobrava njegovo uređivanje, napredovanje ni panel prije `P6-PANELS`.

## Uvjeti zaustavljanja i granica ovlasti

Rad se zaustavlja prije sljedećega paketa ako stvarni dokaz ne zadovolji izlazni
test, ako panel vrati fatalan ili neriješen veliki nalaz, ako bi nastavak tražio
izmišljanje broja, izvora, studije ili citata ili na izričitim vratima `C12` i
`WC-PARTS`. Djelomično izvršenje koje se ondje pošteno zaustavi ispravan je
ishod.

Amandman ne spaja pakete, ne dopušta drugi write-lock, ne ukida nijedan
preduvjet, handoff, panel, determinističku provjeru ili autorski odgovor i ne
odobrava push, merge, tag, arhiviranje, deployment ni objavu.
