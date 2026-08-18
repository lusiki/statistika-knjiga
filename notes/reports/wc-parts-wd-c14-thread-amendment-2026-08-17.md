# Autorski amandman — WC-PARTS do WD-C14

**Odluka:** `A-THREAD-WC-PARTS-WD-C14-2026-08-17`

**Autor i urednik:** Luka Sikic

**Datum odluke:** 17. kolovoza 2026.

**Ulazno stanje:** C12 closeout commit
`1d7c2689bbf70bc0c5faefb3fa4bb926556fd723`.

## Odluka

Za ovu nit pravilo zaustavljanja nakon jednoga paketa zamjenjuje se strogim
slijedom `WC-PARTS`, `P3-VERIFY-D`, `WD-C13`, `C13`, `WD-C14`. Svaki paket
ostaje zasebna transakcija s vlastitim claimom, jednom aktivnom write-lockom,
dokazima, dispozicijama handoffa, provjerama pri claimu i closeoutu te
ograničenim lokalnim commitom. Nijedan lock, dokaz ni nedovršena dispozicija ne
prenosi se preko granice paketa.

Ovo je nova, zasebna odluka. Svi raniji thread-amandmani završili su na
vlastitim granicama; ovaj ih zapis ne mijenja retroaktivno i iz njih ne izvodi
novu ovlast.

## WC-PARTS — unaprijed prihvaćena opcija B i obvezno zaustavljanje

Paket obuhvaća točno poglavlja 7–12, koja su na ulazu sva u fazi
`coauthor_review`. Autor unaprijed prihvaća opciju B: mostovi i samoprovjere
smiju se provesti, a svaka prihvaćena jedinica kojoj se promijene bajtovi izvora
pošteno se vraća u `draft`, jer raniji panel i autorska odluka više ne opisuju
njezino materijalno stanje. Nijedna zastarjela prihvaćenost ne smije ostati nad
promijenjenim izvorom.

Prije prve izmjene proze treba navesti svaku jedinicu koja bi se promijenila i
točan zahvat u njoj te potvrditi da svaki zahvat ostaje unutar ratificiranoga
ugovora dijela i kralježnica `G-A2b-III` i `G-A2b-IV`. Ako se obvezni materijal
može nositi bez izmjene prihvaćenoga tijela poglavlja, to se mora izrijekom
utvrditi i preferirati.

Nakon te raščlambe treba predložiti, ali ne i stvoriti bez nove izričite
autorove suglasnosti, jedna skupna vrata ponovnoga prihvaćanja neposredno iza
`WC-PARTS`. Prijedlog mora dati točan ID, sekvencu, ugovor, tražene dokaze,
izlazne testove, obuhvaćene jedinice i jedan imenovani handoff kojim se njihovi
odgođeni paneli premještaju iz `P6-PANELS`. Nit se na tom prijedlogu zaustavlja.
Nijedan zapis ne smije tvrditi da je autor pročitao poglavlje.

## Granice preostalih paketa

`P3-VERIFY-D` provjerava svaki preduvjet neovisno protiv jednoga deklariranog
izvornog stanja, bez dokazivanja zbrajanjem. Ponavlja determinističke provjere i
namjerne negativne fixturee, izrijekom navodi koje su jedinice nakon
`WC-PARTS` u `draft`, a koje u `coauthor_review`, i ne skriva zastarjelu
prihvaćenost ni drugi blocker iza sažetka.

`WD-C13` provodi vertikalni presjek poglavlja 13 prema kralježnici `G-A2b-V`.
Prije claima troši `H-P3-ESS-001`. ESS ostaje portalom posredovan, neobvezan i
nepromoviran: poglavlje ne smije tvrditi da je lokalno pakiran, da izdanja imaju
datotečnu parnost ili da postoji dopuštenje nositelja prava. Obvezni offline
studentski zadatak mora izrijekom imenovati svoju licencno čistu lokalnu
alternativu. Terminologija ostaje usklađena s poglavljem 17, uključujući
kanonski naziv prilagođenoga standardiziranog reziduala i odluku da su tablica
kontingencije i tablica zabune isti objekt pod jednim nazivom. Svih šest
neovisnih kritičara mora biti dovršeno i sintetizirano; sinteza preporučuje, ali
ne bilježi prihvaćanje.

`C13` se ne može zatvoriti bez točnoga datiranog odgovora autora vezanog uz
završni izvorni commit poglavlja. Stalna delegacija od 5. kolovoza nije zamjena.
Traženi oblik odgovora glasi `C13 accepted for <commit> on <date>.` Nit se
zaustavlja dok taj odgovor ne stigne.

`WD-C14` provodi vertikalni presjek poglavlja 14 prema kralježnici `G-A2b-V` i
u cijelosti primjenjuje ratificiranu ispravku D02 prihvaćenu na gateu A1b, bez
ponovnoga tumačenja. `H-P3-ESS-001` troši prije claima, a `H-WB-C06-001` prije
closeouta. Za ESS vrijede iste portalne, licencne i offline granice kao u
poglavlju 13. Paket provodi puni panel od šest kritičara.

## Stalne podatkovne i izdavačke granice

Gdje se pojavljuju DigiKat ili Eurostat, nema tvrdnje o rastu ili trendu preko
2024., nema usporedbe preko prekida metode iz lipnja 2024. bez izričite napomene,
izvorni nazivnik ostaje 551.712, nema usporedbe interakcije ili dosega između
mjerene i nemjerene platforme, a jaz iz 2024. ostaje vidljiv i neizglađen.

Nijedno poglavlje ne smije tvrditi da su vremena čitanja mjerena ili iskušana
na čitateljima, da su knjigu potvrdili novi čitatelji ili da je terminologija
prvoga izdanja neovisno pregledana.

Poglavlje 6 ostaje namjerno u `draft` pod `H-WB-PART-001`. Ovaj amandman ne
odobrava njegovo uređivanje, napredovanje ni panel prije `P6-PANELS`.

## Uvjeti zaustavljanja i granica ovlasti

Rad se zaustavlja prije sljedećega paketa ako stvarni dokaz ne zadovolji izlazni
test, ako panel vrati fatalan ili neriješen veliki nalaz, ako bi nastavak tražio
izmišljanje broja, izvora, studije ili citata, na prijedlogu skupnih vrata nakon
`WC-PARTS` i na vratima `C13`. Pošteno djelomično izvršenje ispravan je ishod.

Amandman ne spaja pakete, ne dopušta drugi write-lock, ne ukida nijedan
preduvjet, handoff, panel, determinističku provjeru ili autorski odgovor i ne
odobrava push, merge, tag, arhiviranje, deployment ni objavu.
