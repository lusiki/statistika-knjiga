# G-A2b-I — ratificirana kralježnica Dijela I

**Gate:** `G-A2b-I`

**Datum odluke:** 4. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2b-I-spine-approved-2026-08-04-Luka-Sikic`, vezano uz nacrt
kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu Dijela I: nosive aspekte,
nosive pojmove, preduvjete i isključenja za poglavlja 1, 2 i 3, ugovor na razini
dijela i hijerarhiju definicija za poglavlja 1 i 3. Ne odobrava prozu, ne dodaje
i ne uklanja nijedan `#def-` blok i ne ratificira nijednu kasniju kralježnicu.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-I-SPINE`, upravljane stavke `R04-SPINE-I`, `R04-C01-definitions` i
`R04-C03-definitions`, prihvaćene arhitekture `G-A2a`, `G-A2d` i identitetski
brifovi `P2-IDENTITY` u `conventions.json`, ratificirana kralježnica predgovora,
zabilježena autorova namjera, pravilo `H10` u `STYLE.md` te sve stavke registra
koje ciljaju poglavlja 1, 2 i 3.

Cjeloviti ledger prijenosa pročitan je prije odluke. Nijedan prijenos ne cilja
`G-A2b-I`, pa nema dolazne isporuke koju bi ovaj gate priznao ili potrošio.
`H-P0-REGISTER-008` cilja `WC-C08`, `WC-C09` i `WD-C17` i ostaje `pending`;
kralježnica poglavlja 3 njegov dug izriče, ali ga ne naplaćuje.

## Ugovor na razini Dijela I

Dio I nosi tri koraka i ništa više: **broj nije zaključak**, zatim **kako broj
nastaje**, zatim **kako točan broj ipak zavodi**. Poglavlje 1 postavlja pitanje i
imenuje četiri djelatnosti, poglavlje 2 pokazuje kako opažanje postaje podatak, a
poglavlje 3 kao prvi identitetski stup pokazuje što se događa kad se taj put ne
provjeri.

Dio naglašava tri faze životnoga ciklusa iz prihvaćene arhitekture: pitanje,
prikupljanje i provjeru. Sadi pet niti: jedinicu analize, selekciju i odsutnost,
nazivnik, proračun nesigurnosti i posljedice pogreške. Na granici dijela nosi
punu mapu tvrdnji sa šest dimenzija i šest revizijskih pitanja, prema
prihvaćenoj arhitekturi `G-A2a`, te odgovoriv samoprovjeru.

Cijeli Dio I nema vidljivoga koda. Skriveni pogonski blokovi ostaju dopušteni,
profil `kolegij` ih smije otkriti, i nijedan ocijenjeni zadatak ne traži pisanje
koda. Ljestvica AI kompetencija u Dijelu I traži provjeru podrijetla i
izmišljenih brojeva, ali još ne traži pisanu potvrdu provjere.

Rampa ostaje blaga. Formalna definicijska opterećenja ne rastu radi sebe samih.

## Nacrtana kralježnica po poglavljima

### Poglavlje 1 — Zašto statistika

**Nosivi aspekti**

1. Broj sam po sebi nije zaključak: između podatka i suda stoji pitanje,
   usporedba i neizvjesnost.
2. Jedinica analize kao prvo pitanje svake tablice: što predstavlja jedan redak.
3. Nazivnik kao uvjet svakoga postotka, stope i usporedbe.
4. Simpsonov paradoks kao razlog za sumnju u zbirnu sliku, s prvim susretom
   skrivene strukture.
5. Životni ciklus podataka od pitanja do nadzora, imenovan i smješten kao okvir
   knjige.
6. Četiri djelatnosti razlikovane isključivo po pitanju kojim upravljaju:
   statistika, podatkovna znanost, strojno učenje i sustav umjetne inteligencije.
7. Podrijetlo podatka kao prvo pitanje čitatelja, prije svake računice.

**Nosivi pojmovi**: jedinica analize, nazivnik, Simpsonov paradoks, životni
ciklus podataka, statistika, podatkovna znanost, strojno učenje, sustav umjetne
inteligencije.

**Preduvjeti**: nijedan; poglavlje 1 slijedi predgovor, ali ne pretpostavlja
nijedno poglavlje.

**Isključenja**: nijedan vidljivi blok koda; nikakva formalna definicija
populacije, uzorka i uzorkovanja, koje pripadaju poglavlju 8; nikakva
vjerojatnosna notacija; nikakav test ni interval; nijedan ocijenjeni zadatak
pisanja koda; nijedan izmišljen ili neizvorni empirijski primjer; svaka
pojavnost Berkeleyjeva slučaja postavlja novo pitanje.

### Poglavlje 2 — Mjerenje i istraživački dizajn

**Nosivi aspekti**

1. Od pojma do podatka: operacionalizacija kao odluka, a ne kao tehnikalija.
2. Prihvatljivost i isključenja: tko je i što je uopće moglo ući u podatke.
3. Pouzdanost i valjanost kao dva različita pitanja o istom mjerenju.
4. Razine mjerenja kao praktičan opis s poviješću i granicama, a ne kao potpuno
   pravilo o dopuštenim postupcima.
5. Zajednički uzrok, medijator i kolider kao tri različita odnosa; kontroliranje
   svega nije rješenje.
6. Randomizacija kao ravnoteža u očekivanju, uz pridržavanje, prelijevanje,
   osipanje i različito mjerenje.
7. Opažačke studije i doseg zaključka, s prvom karticom za čitanje ankete.
8. Kodiranje jezika kao mjerenje, s isključenjima i dvosmislenošću.
9. Prvi proračun nesigurnosti: mjerna i dizajnerska nesigurnost prije ijednoga
   računa o uzorkovanju.

**Nosivi pojmovi**: operacionalizacija, pouzdanost, valjanost, konfundirajuća
varijabla, medijator, kolider, randomizacija, prihvatljivost, razina mjerenja,
kodiranje kao mjerenje.

**Preduvjeti**: poglavlje 1.

**Isključenja**: nijedan vidljivi blok koda; nikakav formalni uzročni račun ni
identifikacijska strategija, koji pripadaju poglavlju 16; nikakva psihometrija
ni faktorska analiza, koje su izvan opsega knjige; nikakva potpuna teorija
uzorkovanja, koja pripada poglavlju 8; nijedan ocijenjeni zadatak pisanja koda;
Stevensove razine ne smiju se iznijeti kao potpuno pravilo o dopuštenim
postupcima; nijedan izmišljen ili neizvorni empirijski primjer.

### Poglavlje 3 — Kako brojke zavode

Kralježnica poglavlja 3 podređena je njegovu ratificiranom identitetskom brifu
`c03` i ne ponavlja ga. Brif određuje argument; kralježnica određuje što
poglavlje mora nositi kao pojam i granicu.

**Nosivi aspekti**

1. Jedna javna tvrdnja s provjerljivim izvorom nosi cijelo poglavlje.
2. Os i nazivnik: isti podatak, drugi prikaz i druga baza.
3. Temeljna stopa kao uvjet svakoga suda o rijetkom ishodu.
4. Rano čitanje ankete kao izričito označen dug prema poglavljima 8 i 9.
5. Biranje trešanja kao izbor razdoblja, podskupine ili usporedbe.
6. Provjera podrijetla broja koji je proizveo asistent: izvor, podaci,
   transformacija, nazivnik i citat.
7. Sintetički medij i pitanje podrijetla.
8. Četiri različite oznake dokaza: simulacija, sintetički zapis, hipotetski izlaz
   modela i izmišljeni dokaz.
9. Protokol skeptičnoga čitanja kao ishod argumenta.
10. Granica Dijela I: puna mapa tvrdnji sa šest dimenzija i šest revizijskih
    pitanja te odgovoriva samoprovjera.

**Nosivi pojmovi**: temeljna stopa, postotak i postotni bod, margina pogreške kao
najavljeni dug, podrijetlo tvrdnje, sintetički zapis, protokol skeptičnoga
čitanja.

**Preduvjeti**: poglavlja 1 i 2.

**Isključenja**: nijedan vidljivi blok koda; nikakvo izvođenje margine pogreške
prije poglavlja 8 i 9; epizoda Američkoga statističkog udruženja nije slučaj
poglavlja; nikakav redni popis umjesto naracije; nikakva uzročna tvrdnja iz
revidirane javne tvrdnje; nijedan ocijenjeni zadatak pisanja koda; nijedan
izmišljen ili neizvorni empirijski primjer; odabir slučaja, izvora i podatkovnoga
paketa ostaje gateovima `G-A4-03`, `G-A3-DZS` i `G-A3-DIP`.

## Hijerarhija definicija za Dio I

Ovaj gate odlučuje koji pojam dobiva `#def-` blok, koji se imenuje i objašnjava u
prozi pri prvoj upotrebi, a koji se izričito odgađa kasnijem poglavlju. Gate ne
mijenja nijednu datoteku poglavlja. Same blokove pišu paketi `WA-C01`, `WA-C02`
i `WA-C03`, a kanonske hrvatske oblike i regeneraciju grafa pojmova preuzima
`P2-TERMS` na gateu `G-A2c`.

| Poglavlje | `#def-` blok | Proza pri prvoj upotrebi | Odgođeno |
|---|---|---|---|
| 1 | jedinica analize, Simpsonov paradoks | nazivnik, životni ciklus podataka, četiri djelatnosti | populacija, uzorak i uzorkovanje (poglavlje 8) |
| 2 | operacionalizacija, pouzdanost, valjanost, konfundirajuća varijabla | medijator, kolider, randomizacija, prihvatljivost, razina mjerenja, kodiranje kao mjerenje | uzročna identifikacija (poglavlje 16), složeni dizajni uzorkovanja (poglavlje 8) |
| 3 | temeljna stopa | postotak i postotni bod, podrijetlo tvrdnje, sintetički zapis, protokol skeptičnoga čitanja | margina pogreške i interval (poglavlja 8 i 9) |

Poglavlje 2 zadržava svoja četiri postojeća bloka nepromijenjena. Dio I dobiva
tri nova bloka: `jedinica analize` i `Simpsonov paradoks` u poglavlju 1 te
`temeljna stopa` u poglavlju 3.

Četiri djelatnosti ne dobivaju četiri bloka. Njihova kanonska razlika već stoji u
`intellectual_architecture.data_science_registry.activities`, s upravljačkim
pitanjem svake, i poglavlje 1 je izriče, a ne redefinira.

Medijator i kolider ostaju u prozi uz mehanizam `.pojam`. Poglavlje 16 ih
dohvaća, a `P2-SPINE-V` smije zatražiti formalni blok ako pokaže da ga poglavlje
16 stvarno treba.

Prvi je susret uvijek prije formalizacije. Nijedan `#def-` blok ne stoji prije
nego što je pojam doživljen u prozi, prikazu ili widgetu.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Ratificirati samo definicije o kojima kasniji dijelovi stvarno ovise | Hijerarhija definicija; tri nova bloka, svaki s imenovanim kasnijim ovisnikom |
| Držati granicu D05 da Dio I nema vidljivoga koda | Ugovor dijela i prvo isključenje svakoga od triju poglavlja |
| Blaga rampa; formalno opterećenje ne raste radi sebe | Četiri djelatnosti bez blokova, medijator i kolider u prozi, populacija i uzorak odgođeni poglavlju 8 |
| Tvrdnja, ciklus, mjerenje i pismenost kao četiri područja | Poglavlje 1 nosi tvrdnju i ciklus, poglavlje 2 mjerenje, poglavlje 3 pismenost |

Ostali aspekti nisu novi zahtjevi. Svaki provodi već ratificiranu stavku registra
ili prihvaćenu arhitekturu.

| Aspekt | Već ratificirani izvor |
|---|---|
| 1.5 životni ciklus, 1.6 četiri djelatnosti | D04, `G-A2a` lifecycle i `data_science_registry` |
| 1.2, 1.3, 2.2, 2.9, 3.3 niti Dijela I | `G-A2a` thread registry, mjesta sadnje |
| 2.5 zajednički uzrok, medijator, kolider | `R14-C02-confounder` |
| 2.6 randomizacija kao ravnoteža u očekivanju | `R09-C02-randomisation` |
| 2.4 povijesno omeđene Stevensove razine | `R09-C02-stevens` |
| 2.2 prihvatljivost i isključenja | `R11-C02-units-eligibility` |
| 2.8 kodiranje jezika kao mjerenje | `R13-C02-coding-measurement` |
| 3.1 do 3.9 | ratificirani identitetski brif `c03` u `identity_briefs` |
| 3.4 dug margine pogreške | `R12-C03-margin-debt`, `H-P0-REGISTER-008` |
| 3.10 granica dijela | `G-A2a` `claim_registry.placement_rule` |
| 1.7 podrijetlo, 3.6 provjera AI broja | `R24-C03-AI-provenance`, ljestvica AI kompetencija, stupanj `part_i` |
| isključenje o Berkeleyju | `R31-C01-Berkeley` |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki.

## Razmotrene alternative

1. **Dati svakoj od četiriju djelatnosti vlastiti `#def-` blok.** Odbijeno:
   kanonska razlika već stoji u prihvaćenoj arhitekturi, a četiri apstraktna bloka
   u prvom poglavlju rušila bi blagu rampu.
2. **Formalno definirati populaciju i uzorak već u poglavlju 1.** Odbijeno:
   poglavlje 8 je pedagoška okosnica knjige i ondje ti pojmovi dobivaju
   simulaciju prije imena.
3. **Dodati medijatoru i kolideru vlastite blokove u poglavlju 2.** Odbijeno na
   ovom gateu: proza uz mehanizam `.pojam` nosi ih na razini pismenosti, a
   `P2-SPINE-V` ih smije zatražiti ako poglavlje 16 to pokaže.
4. **Ne dodati nijedan novi blok u Dio I.** Odbijeno: pregled je našao da
   poglavlje 1 nema stabilnu hijerarhiju definicija, a poglavlje 17 stvarno ovisi
   o temeljnoj stopi posađenoj u poglavlju 3.
5. **Definirati marginu pogreške u poglavlju 3.** Odbijeno: proturječi
   `R12-C03-margin-debt` i prijenosu `H-P0-REGISTER-008`.
6. **Dopustiti vidljivi kod u poglavlju 3 kao dokaz provjere.** Odbijeno:
   proturječi odluci D05 i pravilu H10, a zahtjev je već zabilježen kao odbijen u
   `R23-C03-visible-receipt-conflict`.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu Dijela I i njezinu hijerarhiju
definicija. Ne odobrava prozu poglavlja 1, 2 ni 3 i ne mijenja nijednu datoteku
poglavlja. Ne dodaje ni ne uklanja nijedan `#def-` blok i ne regenerira graf
pojmova; to ostaje paketima `WA-C01`, `WA-C02`, `WA-C03` i `P2-TERMS`. Ne
utvrđuje kanonsku terminologiju, koja ostaje gateu `G-A2c`. Ne ratificira
nijednu kasniju kralježnicu. Ne bira slučaj, izvor ni podatkovni paket poglavlja
3. Ne mijenja fazu nijedne jedinice, koja ostaje `draft`. Ne odobrava push,
merge, tag, arhiviranje, deployment ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavke `R04-SPINE-I`, `R04-C01-definitions` i `R04-C03-definitions`;
- paket `P2-SPINE-I`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json`.

Ovisnosti koje ostaju blokirane: `WA-C01`, `WA-C02` i `WA-C03` čekaju
`P3-VERIFY-A`, `P3-PILOT` i svoje gateove, `P2-TERMS` čeka `G-A2c`, a
`WA-PART` čeka svoja tri poglavlja.
