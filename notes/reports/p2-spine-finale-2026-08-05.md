# P2-SPINE-FINALE — upisana kralježnica završnice

**Paket:** `P2-SPINE-FINALE`

**Datum:** 5. kolovoza 2026.

**Ishod:** ratificirana kralježnica poglavlja 18 upisana je u kanonski registar,
čime su ratificirane sve devetnaest kralježnica knjige; deterministična je
provjera proširena na točne obveze završnice, uključujući izmijenjenu granicu
nove metode i uvjet redoslijeda ratifikacije koji imenuje svih sedamnaest
numeriranih poglavlja; odobreno povećanje od jednoga definicijskog bloka, obveza
usklađivanja retka `.chapter-meta` i obveza o putovima preneseni su naprijed
umjesto da budu provedeni. Nijedna rečenica proze i nijedan `#def-` blok nisu
promijenjeni.

## Ulazi i prijenosi

Cjeloviti ledger prijenosa pročitan je prije zahtjeva za pisanjem. **Točno jedna
isporuka cilja `P2-SPINE-FINALE`.**

`H-G-A2B-FINALE-001` isporuka je na vratu `before_start`. Priznata je i
**potrošena prije zahtjeva za pisanjem**, s izričitom dispozicijom i dokazima.
Njezina je dispozicija da ratificirana kralježnica iz gatea `G-A2b-FINALE` bude
točna i jedina granica ovoga paketa. Njezina druga isporuka, prema
`P6-CONTINUITY`, na vratu je `before_close` i **ostaje `pending`**, kako i mora:
taj paket revidira gotovu knjigu prema istoj granici.

Pročitani su u cijelosti ugovor paketa `shared_registry`, stavke
`R04-SPINE-FINALE`, `R04-C18-definitions` i `R04-C18-whole-prerequisites`,
trajni zapis odluke `notes/reports/g-a2b-finale-spine-decision-2026-08-05.md`,
izvještaj `notes/reports/p2-spine-v-2026-08-05.md` kao obrazac postupanja, te
obje obvezujuće autorove izmjene od 5. kolovoza 2026.

Četiri prijenosa dodiruju okolinu završnice i sva četiri ostaju `pending` i
nepotrošena ovdje: `H-P1C-INTEGRITY-002` cilja `P2-TERMS` i zamrzava skup od 46
živih definicija, pojmovni ledger i generirani graf; `H-G-A2D-005` cilja
`WE-C18` i nosi datiranu politiku privatnosti koju ova kralježnica upisuje kao
obvezu; `H-P2-SPINE-V-001` cilja `P2-TERMS` i `WD-C17`; `H-P2-SPINE-V-002` cilja
`P5-ROUTES`.

## Što je upisano

| Jedinica | Aspekti | Pojmovi | Preduvjeti | Isključenja |
|---|---|---|---|---|
| `18-vase-prvo-istrazivanje` | 12 | 12 | 17 | 12 |

Zapis nosi i svoj gate `G-A2b-FINALE`, nadnevak ratifikacije i putanju trajnoga
zapisa odluke. Brojevi aspekata, pojmova, preduvjeta i isključenja točno
odgovaraju prihvaćenom nacrtu; ništa nije dodano ni izostavljeno.

**Ratificirano je devetnaest od devetnaest kralježnica.** Nijedna više nije
neratificirana, i to je posljednji od sedam kralježničnih gateova koji je
proveden u registar.

## Preduvjeti završnice i strojna provjera kumulativnosti

Poglavlje 18 traži poglavlja 1 do 17, svih sedamnaest, i svako od njih nosi točno
određenu obvezu iz tablice trajnoga zapisa odluke. Isti je popis upisan i kao
uvjet redoslijeda ratifikacije u `scripts/check-chapter-spines.py`, pa je
kumulativnost završnice **strojno provjerena, a ne tvrđena**: poglavlje 18 nije
moglo biti ratificirano prije nijednoga ranijeg poglavlja.

Nijedan preduvjet ne pokazuje na kasniju jedinicu, jer kasnije jedinice nema.

Predgovor je namjerno izostavljen, uz zabilježen razlog: on je čitateljski
ugovor, a ne gradivo o kojemu kasnija jedinica ovisi, i nijedna druga
ratificirana kralježnica u knjizi ne imenuje ga kao preduvjet.

Prvo isključenje nosi obje strane obveze: poglavlje se ne smije čitati bez
cijele knjige, i nijedan metapodatak, nijedna proza, nijedan zadatak i nijedan
oglašeni put ne smije završnicu prikazati kao samostalnu jedinicu.

## Izmijenjena granica nove metode, sada strojno provjerljiva

Gate `G-A2b-FINALE` jedini je od sedam kralježničnih gateova koji je izmijenio
preporučenu zadanu odluku registra. Zadana odluka zabranjuje svaku novu metodu u
capstoneu; autor ju je izmijenio tako da poglavlje 18 *smije* uvesti tehniku koju
obrađeni slučaj doista traži, pod tri točna ograničenja. Ta su ograničenja
upisana kao isključenja 2 i 3 kralježnice, a ovaj ih je paket učinio strojno
provjerljivima **prije nego što je ijedna rečenica završnice napisana**.

Obvezne oznake isključenja za jedinicu 18 sada su:

| Oznaka | Što provodi |
|---|---|
| `bez cijele knjige` | kumulativnost na razini cijele knjige |
| `popisa izvan opsega iz predgovora` | ograničenje 1 izmijenjene granice |
| `u cijelosti objašnjena ondje gdje se pojavljuje` | ograničenja 2 i 3 izmijenjene granice |
| `ocijenjeni zadatak pisanja koda` | granica H10 |

Uklanjanje bilo koje od dviju srednjih oznaka vraća izlaz 1. To je provjereno
izravno, u prolaznom pokusu koji je registar vratio u bajt-identično stanje:

- uklanjanje oznake `popisa izvan opsega iz predgovora` → izlaz 1, poruka
  *Ratified spine 18-vase-prvo-istrazivanje does not state its required
  exclusion about 'popisa izvan opsega iz predgovora'.*;
- uklanjanje oznake `u cijelosti objašnjena ondje gdje se pojavljuje` → izlaz 1,
  s istom vrstom poruke.

`P2-SPINE-FINALE` i `P6-CONTINUITY` dva su imenovana provoditelja te granice.
Ovaj je paket prvi i završio je svoj dio; drugi ostaje otvoren i mora gotovu
knjigu provjeriti prema istoj granici.

### Jedna zabilježena razlika prema nacrtu

Nacrtano isključenje 3 u trajnom zapisu odluke glasi „u cijelosti **je**
objašnjena ondje gdje se pojavljuje", dok tablica oznaka u istom zapisu traži
doslovni podniz „u cijelosti objašnjena ondje gdje se pojavljuje". Ta se dva
mjesta u nacrtu ne podudaraju doslovno.

Upisano je isključenje koje nosi traženu oznaku doslovno: „Tehnika koju obrađeni
slučaj doista traži dopuštena je samo pod dva uvjeta: **mora biti** u cijelosti
objašnjena ondje gdje se pojavljuje i samodostatna, i ne smije tražiti nijedan
pojam, postupak ni sposobnost koje nijedna ranija ratificirana kralježnica nije
bila zadužena isporučiti."

Promijenjen je samo red riječi, i to najmanji mogući. Oba su uvjeta
nepromijenjena, značenje je nepromijenjeno, a razlika se ovdje **bilježi, a ne
prešućuje**, jer je izvor obveze isti dokument koji nosi obje formulacije.

## Definicijsko opterećenje i zamrznuti pojmovni gate

Gate `G-A2b-FINALE` riješio je stavku `R04-C18-definitions`. Poglavlje 18 nema
nijedan blok i time pada ispod ratificiranoga pojasa, pa raste na točno jedan:
**paket dokaza**, jedini objekt koji završnica stvara, a ne dohvaća, čiji je
sadržaj već ratificiran ulogom `finale` u registru životnoga ciklusa i koji pet
ratificiranih stavki registra traži imenom.

Ovaj paket odobrenu kartu **nije proveo**. Dodavanje `#def-` bloka uređuje prozu
poglavlja, a `H-P1C-INTEGRITY-002` zamrzava točan skup od 46 živih definicija,
pojmovni ledger i generirani graf kriptografskim otiscima dok `P2-TERMS` ne
zatvori taj dug. Poglavlje 18 i dalje nosi nula živih blokova, a ukupan broj
ostaje 46.

Novi prijenos `H-P2-SPINE-FINALE-001` nosi odobrenu kartu paketima `P2-TERMS` i
`WE-C18` na njihovu vratu `before_close`, točno kako je to učinio
`H-P2-SPINE-V-001` za poglavlje 17. Prijenos nosi i **svih jedanaest izričito
odbijenih blokova** s njihovim zabilježenim razlozima, pa ih `WE-C18` ne može
tiho ponovno otvoriti.

## Tri stavke registra, dvije zatvorene i jedna namjerno otvorena

`R04-SPINE-FINALE` i `R04-C18-definitions` zatvorene su ovdje.
`R04-C18-whole-prerequisites` **nije** i ostaje na statusu `ratified`. Svaka je
odluka donesena prema vlastitom testu prihvaćanja te stavke.

**`R04-SPINE-FINALE`** traži da su sve kralježnice iz opsega ratificirane, da
proza nije uređivana i da faza poglavlja nije pomaknuta. Sve troje vrijedi:
jedinica 18 je ratificirana, nijedna datoteka poglavlja nije dirnuta, i svih
devetnaest jedinica ostaje u fazi `draft`.

**`R04-C18-definitions`** traži da završnica ne uvodi slučajnu novu metodu ni
nezabilježen pojam. Obje su polovice riješene onim što ovaj paket doista može
proizvesti: granica nove metode strojno je provjerljiva prije ijedne rečenice
završnice, a dvanaest nosivih pojmova zabilježeno je u registru, od kojih pet
provjeritelj traži poimence, dok svaki od jedanaest odbijenih blokova nosi
zabilježen razlog. Provjera gotove knjige prema toj granici ostaje paketu
`P6-CONTINUITY` i ovdje se **ne tvrdi da je provedena**.

**`R04-C18-whole-prerequisites`** traži da metapodaci, proza, putovi i zadaci ne
prikazuju capstone kao samostalnu jedinicu. Polovica registra je gotova i strojno
provjerena. Druga polovica nije: postojeći redak `.chapter-meta` u
`chapters/18-vase-prvo-istrazivanje.qmd:110` i dalje glasi „pogl. 2, 6 i 16", što
je uže od ratificiranoga popisa i proturječi prvomu isključenju, a nijedan put
nije objavljen ni izmijenjen. Metapodatak je u vlastitom deklariranom opsegu te
stavke, `chapters/18-vase-prvo-istrazivanje.qmd`, a ovaj paket prozu poglavlja ne
smije mijenjati. Zatvoriti stavku ovdje značilo bi ustvrditi stanje koje se nije
dogodilo. Prijenos `H-P2-SPINE-FINALE-002` nosi obvezu metapodatka paketu
`WE-C18` i obvezu puta paketu `P5-ROUTES`.

Ta odluka **ne mijenja** trenutak u kojem roditeljska stavka `R04` može biti
zatvorena: `R04-ROUTES-two-track-map` već je obvezno dijete čiji je paket
`P5-ROUTES` u Fazi 5, pa je zatvaranje `R04` ionako izvan Faze 2.

## Proširena provjera i pokrivenost fiksatora

`scripts/check-chapter-spines.py` sada uz opće obveze ratificiranoga zapisa traži
i točne obveze završnice: četiri oznake isključenja, pet obveznih nosivih pojmova
— `paket dokaza`, `putovnica skupa podataka`, `trag odluka`, `granica tvrdnje` i
`provjera osjetljivosti` — te uvjet redoslijeda ratifikacije sa svih sedamnaest
numeriranih poglavlja.

Oba obvezna negativna fiksatora zadržala su svoje oznake i vratila izlaz 1.
Nijedan nije dodan, uklonjen ni preimenovan. Njihova stvarna pokrivenost jedinice
18 izriče se ovdje točno:

- `ratified_without_decision` uklanja gate svakoj ratificiranoj jedinici, pa za
  jedinicu 18 pada vezanje na gate `G-A2b-FINALE`;
- `part_i_visible_code_admitted` uklanja prvu obveznu oznaku i prvi obvezni
  nosivi pojam svakoj ratificiranoj jedinici, pa za jedinicu 18 padaju i provjera
  isključenja (`bez cijele knjige`) i provjera pojmova (`paket dokaza`);
- **provjera redoslijeda ratifikacije pada i za jedinicu 18.** Isti fiksator
  razratificira poglavlja 5 i 7, a oba su u popisu preduvjeta poglavlja 18, jer
  taj popis obuhvaća cijelu knjigu.

Za jedinicu 18 stoga **nijedna vrsta provjere ne ostaje neisprobana** — sve tri
padaju kako moraju. To je potpunija pokrivenost po jedinici nego što su je
dobila poglavlja 13, 14, 15 i 17, čija redoslijedna pravila taj fiksator ne
dodiruje, i posljedica je upravo toga što završnica traži cijelu knjigu.

## Kanonsko stanje i provjere

Deterministično stanje registra jest
`spine:sha256-27e5c37481e84cefed4dde818b6d5ed13727faae56e917747916bf3ff2e93efb`.

Prošli su `scripts/check-chapter-spines.py` s devetnaest ratificiranih i nula
neratificiranih jedinica, `scripts/check-book-architecture.py`,
`scripts/check-assessment-architecture.py`, `scripts/check-identity-briefs.py` i
blokirajuća struktura `scripts/check-manuscript-integrity.py --lane structure` s
devetnaest poglavlja. Sva tri arhitekturna potrošača broje ratificirane
kralježnice i **slažu se na devetnaest od devetnaest**; nijedan ne tvrdi zatečeni
broj i nijedna snimka stanja nije vraćena. Prihvaćena stanja
`architecture:sha256-30e10508…`, `assessment:sha256-c1206f08…` i
`identity:sha256-f09124e5…` ostaju nepromijenjena, a `conventions.json` nije
dirnut.

Struktura rukopisa i dalje bilježi 46 živih `#def-` blokova, a poglavlje 18 nula.

## Obvezujuće autorove izmjene od 5. kolovoza 2026.

Obje su izmjene pročitane prije prve sadržajne izmjene i obje ovdje vrijede.

Ovaj paket **ne tvrdi i ne pretpostavlja nikakvu neovisnu recenziju** — nazivlja
ni bilo čega drugoga — ni u registru, ni u provjeritelju, ni u ovom izvještaju.
Kanonski hrvatski oblici svih pojmova završnice, osobito `paket dokaza`,
`putovnica skupa podataka` i `objava uporabe asistenta`, ostaju odluka gatea
`G-A2c` i isključiva su odgovornost autora i urednika.

Ovaj paket **ne tvrdi nikakvo dopuštenje vlasnika prava** ni za jedan izvor i ne
bira nijedan podatkovni paket. Odabir paketa za empirijski prijenos upisan je kao
obveza njegovih gateova podataka i paketa `WE-C18`, i to kao dvanaesto
isključenje kralježnice. Oba su ograničenja namjerno ostavljena izvan zasebnih
isključenja o recenziji i pravima, jer njihovi durabilni zapisi već imenuju točne
pakete koje vežu.

## Što nije promijenjeno

Nijedna proza poglavlja ili dodatka, uključujući redak `.chapter-meta` u
poglavlju 18; nijedan `#def-` blok, brid grafa pojmova, faza jedinice,
terminologija, identitetski brif, podatkovni paket, ruta, render, generirani
artefakt ni vanjska ovlast. Test prihvaćanja stavke `R17-C18-two-pass` nije
izmijenjen i ta stavka nije dirnuta. Svih devetnaest jedinica ostaje u fazi
`draft`, broj živih definicija ostaje 46, `G-A2c` nije otvoren i nijedan kasniji
paket nije pokrenut.
