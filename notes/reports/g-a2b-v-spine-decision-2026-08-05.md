# G-A2b-V — ratificirana kralježnica Dijela V

**Gate:** `G-A2b-V`

**Datum odluke:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2b-V-spine-approved-2026-08-05-Luka-Sikic`, vezano uz nacrt
kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu Dijela V: nosive aspekte,
nosive pojmove, preduvjete i isključenja za poglavlja 13, 14, 15, 16 i 17,
ugovor na razini dijela te hijerarhiju definicija kojom se rješava stavka
`R04-C17-definitions`. Uz to utvrđuje točne preduvjete poglavlja 17, čime se
rješava stavka `R04-C17-prerequisites` i podmiruje proturječje zabilježeno u
prijenosu `H-P0-REGISTER-004`.

Gate ne odobrava prozu, ne dodaje i ne uklanja nijedan `#def-` blok, ne upisuje
ništa u `chapter-spine.json` i ne ratificira nijednu kasniju kralježnicu.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-V-SPINE`, upravljane stavke `R04-SPINE-V`, `R04-C17-definitions` i
`R04-C17-prerequisites`, ratificirani identitetski brif `c17` u
`conventions.json#identity_briefs` zajedno sa zajedničkim ugovorom triju
identitetskih stupova, popis odgoda iz paketa `P2-IDENTITY` koji imenuje
`P2-SPINE-V`, prihvaćene arhitekture `G-A2a` i `G-A2d` (registar tvrdnji,
životni ciklus s ulogom `part_v`, sedam niti, ljestvica AI kompetencija i
granica H10), ratificirane kralježnice predgovora te Dijelova I, II, III i IV,
zabilježena autorova namjera, pojasevi `bands` u `conventions.json`, prihvaćene
odluke D02, D03, D07, D08 i D13, te sve stavke registra koje ciljaju poglavlja
13 do 17, uključujući prihvaćene ispravke paketa `P1A-C13`, `P1A-C14`,
`P1A-C15` i `P1A-C16`.

Pročitane su i dvije obvezujuće autorove izmjene od 5. kolovoza 2026.:
`notes/reports/g-a2c-reviewer-amendment-2026-08-05.md` i
`notes/reports/g-a3-data-rights-determination-2026-08-05.md`.

Cjeloviti ledger prijenosa pročitan je prije prve sadržajne izmjene. **Nijedan
prijenos ne cilja `G-A2b-V`**, pa nema dolazne isporuke koju bi ovaj gate
priznao ili potrošio. `H-P0-REGISTER-004` cilja pakete `P2-SPINE-V` i
`P5-ROUTES` i ostaje `pending`: ovaj gate donosi odluku koju ta dva paketa
provode, ali sam prijenos ne troši. `H-P1C-INTEGRITY-002` cilja `P2-TERMS`,
ostaje `pending` i zamrzava skup od 46 živih definicija, pa ovaj gate odlučuje
samo kartu definicija. `H-P0-REGISTER-007` i `H-P0-REGISTER-008` ciljaju
`WD-C17` i ovdje se ne troše.

## Ugovor na razini Dijela V

Dio V nosi jedan luk i ništa više: **od jedne tablice do jednoga modela, pa do
jednoga postavljenog sustava**. Poglavlje 13 pokazuje kako se broji i što
nazivnik čini uvjetnim, poglavlja 14 i 15 čitaju jednu i više usporedbi,
poglavlje 16 otkriva da je sve to bio jedan model, a poglavlje 17 taj model
stavlja u odluku o stvarnim ljudima. Redoslijed poglavlja ostaje nepromijenjen,
prema odluci D03.

**Poglavlje 16 je vrhunac knjige i sinteza se u njemu isplaćuje.** Poglavlja 14
i 15 smiju pripremiti jezik općega modela, ali ga ne smiju potrošiti: otkriće da
su razlika među dvjema skupinama, usporedba više skupina i regresija jedan te
isti model pripada poglavlju 16 i nigdje se prije njega ne izvodi. To je zapisano
i kao ugovor dijela i kao obvezujuće isključenje u poglavljima 14 i 15.

**Poglavlje 13 preduvjet je poglavlja 17.** Uvjetni nazivnici i kontingencijska
tablica koje čitatelj usvaja u poglavlju 13 upravo su ono što u poglavlju 17
postaje tablica zabune; pravednost i klasifikacija ne mogu se čitati bez njih.
Time se rješava proturječje iz `H-P0-REGISTER-004`, gdje je ogledni kratki put
kritičke pismenosti preskakao poglavlje 13, dok je isti pregled tražio poglavlje
13 prije poglavlja 17. Posljedica je obvezujuća za `P2-SPINE-V`, koji te
preduvjete upisuje, i za `P5-ROUTES`, koji oglašeni kratki put mora izmijeniti.

Dio naglašava četiri faze životnoga ciklusa iz prihvaćene arhitekture:
modeliranje, vrednovanje, komunikaciju i nadzor. Nit nazivnika razvija se u
poglavlju 13 i žanje u poglavlju 17; nit jedinice analize i nit selekcije i
odsutnosti žanju se u poglavlju 17; nit proračuna nesigurnosti žanje se u
poglavljima 16 i 17; nit posljedica pogreške žanje se u poglavlju 17; nit
komunikacije tvrdnje razvija se u poglavlju 16, a žanje tek u završnici. Nit
reproducibilnosti i podrijetla ovdje se dohvaća, a ne razvija iznova.

Statistika ostaje estimacijska i u dijelu o modelima. Procjena, interval i
sadržajna veličina vode svako poglavlje; naziv postupka dolazi poslije razlike,
a ne prije nje. Nijedno poglavlje ne postaje katalog testova.

Ljestvica AI kompetencija u Dijelu V žanje provjeru i alternative: asistent se
propituje o referentnim skupinama, pretpostavkama, izostavljenim varijablama,
uzročnom jeziku, dijagnostici, curenju informacija, oznakama, uspješnosti na
izdvojenim podacima, pogreškama po podskupinama i pomaku, i suočava se s jednom
obranjivom alternativom. Vidljivi je kod potvrda koja se čita i dijagnosticira —
u poglavlju 15 kao sumnjiv artefakt, u poglavlju 17 kao kratka potvrda uz
skrivenu instalaciju — a nijedan ocijenjeni zadatak nigdje u dijelu ne traži
pisanje koda.

Empirijski okvir dijela ostaje onakav kakav je već ratificiran: jedan pripeti
anketni skup na razini osobe ponovno se koristi kroz obitelji modela, dok
poglavlje 17 zadržava simulaciju za poznatu istinu, a upravljani tekstni paket
za empirijsku analizu. Ovaj gate ne bira nijedan paket.

## Nacrtana kralježnica po poglavljima

### Poglavlje 13 — Kategorički podaci

**Nosivi aspekti**

1. Dio V otvara se nastavkom ugovora o reformiranoj praksi iz poglavlja 12:
   poglavlje čita obitelj modela, a ne prikuplja postupke.
2. Brojanje prije testiranja: kontingencijska je tablica konstruiran objekt —
   tko je u njoj, tko u nju nije mogao ući i što ćelija zapravo broji.
3. Uvjetni nazivnik: postotak po retku i postotak po stupcu odgovaraju na
   različita pitanja, a svaki postotak imenuje svoj nazivnik.
4. Očekivane frekvencije pod nezavisnošću kao izrečeni model svijeta bez
   povezanosti.
5. Hi-kvadrat statistika kao zbroj odstupanja s vlastitim referentnim
   rasporedom; ona je dokaz o tablici, a ne mjera jačine povezanosti.
6. Prilagođeni standardizirani rezidual imenuje gdje tablica odstupa od
   nezavisnosti i nije z-vrijednost ćelije.
7. Kalibracija pod nultom hipotezom i snaga pod alternativom dva su odvojena
   pitanja.
8. Referentna raspodjela istraživačka je odluka: test prilagodbe uspoređuje
   opaženu raspodjelu s odabranom referencom, a izbor reference je sadržajan.
9. Kad je aproksimacija tanka: male očekivane frekvencije, egzaktne alternative
   i cijena velike tablice.
10. Kodirani tekst ulazi u tablicu kao mjerna odluka s imenovanim vlasnikom
    kategorije i imenovanim nazivnikom.
11. Temelj za poglavlje 17: uvjetni nazivnici i kontingencijska tablica
    pročitani ovdje ondje postaju tablica zabune, pa je poglavlje 13 preduvjet
    poglavlja 17.

**Nosivi pojmovi**: kontingencijska tablica, uvjetni nazivnik, očekivana
frekvencija, hi-kvadrat statistika, prilagođeni standardizirani rezidual, test
prilagodbe, referentna raspodjela, Cramérovo V.

**Preduvjeti**: poglavlja 2, 3, 4, 10, 11 i 12.

**Isključenja**

1. Nikakav katalog testova za kategoričke podatke; poglavlje do kraja čita jednu
   tablicu.
2. Hi-kvadrat statistika nije mjera jačine povezanosti i ne smije se čitati kao
   veličina učinka.
3. Kalibracija pod nultom hipotezom ne smije se brkati sa snagom pod
   alternativom, a prilagođeni standardizirani rezidual nije z-vrijednost ćelije.
4. Nikakvo prilagođavanje modela za kategorički ishod; logistički se model u
   knjizi čita u poglavlju 16, a ne procjenjuje.
5. Nikakva uzročna tvrdnja iz kontingencijske tablice.
6. Nijedan ocijenjeni zadatak pisanja koda.
7. Nijedan izmišljen ili neizvorni empirijski primjer; odabir podatkovnoga
   paketa ostaje gateovima `G-A3-DIP` i `G-A3-ESS`.

### Poglavlje 14 — Dvije grupe

**Nosivi aspekti**

1. Tko nosi dva rezultata: jedinica neovisnosti odlučuje koja je usporedba
   uopće moguća, a redak nije automatski neovisna jedinica.
2. Razlika prije oznake: procjena i njezin interval izriču se u jedinicama
   pitanja prije nego što se spomene ijedan naziv testa.
3. Ista razlika, dva dizajna: neovisne skupine i upareni podaci odgovaraju na
   različita pitanja iz istih brojeva.
4. Welchova inferencija ostaje zadana: koeficijent uz binarni prediktor jednak
   je razlici aritmetičkih sredina, ali obična homoskedastična OLS nesigurnost
   nije općenito Welchova nesigurnost.
5. Referentna skupina je izbor koji mijenja što koeficijent kaže, a ne što
   podaci kažu.
6. Jedan model iza triju testova — pripremljen, a ne potrošen: poglavlje
   pokazuje vrata prema poglavlju 16 i kroz njih ne prolazi.
7. Što razlika sama ne kaže: doseg populacije, mjerenje i alternativna odluka.
8. Znakovi ovisnosti i pravilo zaustavljanja: ponovljena mjerenja, gnijezdo i
   povezana opažanja prepoznaju se i upućuju dalje.
9. Pretpostavke i njihove granice na razini pismenosti, uz reviziju asistentove
   analize po referentnoj skupini i pretpostavkama.

**Nosivi pojmovi**: jedinica neovisnosti, neovisne skupine, upareni podaci,
razlika aritmetičkih sredina, Welchov t-test, referentna skupina,
standardizirana razlika, ovisnost opažanja.

**Preduvjeti**: poglavlja 2, 4, 9, 10 i 11.

**Isključenja**

1. Nikakvo izjednačavanje Welchove nesigurnosti s običnom homoskedastičnom OLS
   nesigurnošću; procjena je ista, nesigurnost nije.
2. Nikakav katalog testova za dvije skupine; poglavlje vodi razlika, a ne naziv
   postupka.
3. Nikakvo trošenje sinteze poglavlja 16; opći se model priprema, ali se ovdje
   ne otkriva.
4. Nikakvi modeli za ovisne podatke; oni se prepoznaju i upućuju dalje pravilom
   zaustavljanja.
5. Nikakva uzročna tvrdnja iz razlike među skupinama.
6. Nijedan ocijenjeni zadatak pisanja koda.
7. Nijedan izmišljen ili neizvorni empirijski primjer; odabir anketnoga paketa
   ostaje gateu `G-A3-ESS`.

### Poglavlje 15 — Više grupa

**Nosivi aspekti**

1. Cijena mnogih usporedbi: stopa obiteljske pogreške svojstvo je postupka, a ne
   podataka.
2. Varijanca između i unutar skupina kao jedna dekompozicija istoga ukupnog
   raspršenja.
3. F-statistika kao omjer dviju varijanci s vlastitim referentnim rasporedom.
4. Ukupni test kaže da se nešto razlikuje, a ne što se razlikuje; planirana
   usporedba i post-hoc postupak odgovaraju na različita pitanja.
5. Eta-kvadrat kao objašnjeni udio, s granicama; veličina i ovdje dolazi prije
   oznake.
6. Isti model s više koeficijenata — opet pripremljen, a ne potrošen.
7. Neformalni omjer varijanci gruba je dijagnostika, a nikada dokaz da
   pretpostavka vrijedi.
8. Omeđen sumnjiv artefakt koda vezan uz pojam poglavlja: vidljivi se kod čita i
   dijagnosticira, a ne piše.
9. Znakovi ovisnosti i pravilo zaustavljanja za ponovljena, gnijezdna i povezana
   opažanja.

**Nosivi pojmovi**: analiza varijance, stopa obiteljske pogreške, F-statistika,
planirana usporedba, post-hoc postupak, eta-kvadrat, varijanca između skupina,
varijanca unutar skupina.

**Preduvjeti**: poglavlja 9, 10, 11 i 14.

**Isključenja**

1. Nikakav katalog post-hoc postupaka; poglavlje vodi cijena višestrukosti, a ne
   popis testova.
2. Neformalni omjer varijanci nije dokaz da pretpostavka vrijedi.
3. Ukupni test ne imenuje koja se skupina razlikuje.
4. Nikakvo trošenje sinteze poglavlja 16.
5. Nikakvi modeli za ovisne podatke; poglavlje ih prepoznaje i upućuje dalje.
6. Nijedan ocijenjeni zadatak pisanja koda; sumnjiv se kod čita i dijagnosticira.
7. Nijedan izmišljen ili neizvorni empirijski primjer.

### Poglavlje 16 — Regresija

**Nosivi aspekti**

1. Vrhunac je sinteza, a ne novi postupak: poglavlje otkriva da su ranije
   usporedbe cijelo vrijeme bile jedan model.
2. Jedna procjenjivana veličina, odabrana i održana: konačnopopulacijski
   koeficijenti najmanjih kvadrata za zabilježeni ishod, razlučeni od latentnih
   parametara generatora.
3. Pravac kao tvrdnja o prosjeku; vode opažena procjena i njezina nesigurnost, a
   ne istina generatora.
4. Prilagodba i ono što je čini mogućom: zajednički uzročni dijagram iz
   poglavlja 2 ovdje se žanje, a prilagodba za sve varijable može stvoriti
   pristranost preko medijatora, kolidera, mjerenja i vremena.
5. Interakcije i heterogenost čitaju se kroz predviđene pravce i vrijednosti, uz
   razliku između planirane i istraživačke analize podskupina.
6. Objašnjenje i predviđanje različite su zadaće: imenuje se koja informacija
   postoji u trenutku predviđanja, a poslijeishodni prediktori isključuju se kao
   curenje informacija.
7. Pristajanje i njegove granice, uz namjernu stanku dohvata na sredini
   poglavlja prije kasnije sinteze.
8. Omeđen most čitanja za binarni ishod: vjerojatnost, izgledi, omjeri izgleda i
   rizika, referentne skupine, intervali i predviđene vjerojatnosti — čitaju se,
   a ne procjenjuju.
9. Jedna objavljena tablica rezultata i jedan kraći odlomak rezultata, oboje
   pribilježeno kao vježba čitanja, bez ponovnog procjenjivanja.
10. Jedna izričita usporedba dizajna nad zajedničkim svakodnevnim pojmom, koja
    pokazuje da dvije mjere s istom oznakom nisu isti konstrukt, ista jedinica ni
    ista populacija.
11. Pošteno uvjetno izvještavanje razvija se ovdje: procjena, interval, jedinice,
    dosegnuta populacija i ono određeno što bi promijenilo zaključak.
12. Granica prema uzroku i kratak izgled prema Bayesu koji knjigu drži
    estimacijskom, bez tečaja Bayesovske inferencije.

**Nosivi pojmovi**: linearna regresija, procjenjivana veličina, rezidual, metoda
najmanjih kvadrata, višestruka regresija, prilagođena povezanost, koeficijent
determinacije, interakcija, curenje informacija, predviđanje izvan uzorka,
izgledi.

**Preduvjeti**: poglavlja 2, 5, 6, 9, 13, 14 i 15.

**Isključenja**

1. Nikakvo prilagođavanje logističkoga modela ni njegov izvod; binarni ishod,
   izgledi i omjeri izgleda čitaju se, a ne procjenjuju.
2. Nikakvo ponovno procjenjivanje objavljene tablice; artefakt je isključivo
   vježba čitanja.
3. Nikakva zamjena procjenjivane veličine usred poglavlja; latentni parametri
   generatora nisu cilj analize.
4. Nikakva uzročna identifikacija ni tečaj uzročne inferencije; prilagodba nije
   identifikacija.
5. Nikakva puna Bayesovska inferencija; izgled prema Bayesu ostaje kratak.
6. Nikakvi modeli za ovisne podatke; poglavlje ih prepoznaje i upućuje dalje.
7. Nikakva matematika strojnoga učenja; poglavlje 17 ne anticipira se kao tečaj.
8. Nijedan ocijenjeni zadatak pisanja koda.
9. Nijedan izmišljen ili neizvorni empirijski primjer; odabir objavljene tablice
   i uvjeti njezine reprodukcije ostaju gateu `G-A4-16`.

### Poglavlje 17 — Doba algoritama

Kralježnica poglavlja 17 podređena je njegovu ratificiranom identitetskom brifu
`c17` i ne ponavlja ga. Brif određuje argument, njegovih devet koraka, obvezne
sastavnice i modul mjerenja teksta; kralježnica određuje što poglavlje mora
nositi kao pojam, preduvjet i granicu.

**Nosivi aspekti**

1. Poglavlje je jedna posljedična odluka utemeljena na klasifikaciji teksta;
   argument i njegove sastavnice određuje brif `c17`, a kralježnica pojam,
   preduvjet i granicu.
2. Poglavlje 13 je preduvjet: uvjetni nazivnici i kontingencijska tablica
   pročitani ondje ovdje postaju tablica zabune, pa se pravednost i klasifikacija
   ne uvode prije njih.
3. Zabilježeni referentni ishod, a ne istina: referentne oznake nastaju
   postupkom i mogu biti krive, a izraz je dosljedan u prozi, prikazu, natpisu i
   alternativnom tekstu.
4. Selektivno opažanje i proizvodnja oznaka razvijaju se prije evaluacije
   modela, a ne poslije nje.
5. Klasifikacijski prag i nejednak teret pogreške: uvjetni nazivnik i cijena
   svake vrste pogreške čitaju se zajedno s temeljnom stopom posađenom u
   poglavlju 3.
6. Uspješnost na izdvojenim podacima nije valjanost konstrukta.
7. Populacijska generalizacija i razdvajanje na skup za učenje, provjeru i
   ispitivanje dvije su različite stvari; poglavlje 8 se ovdje dohvaća, a ne
   ponavlja.
8. Jezični modeli kao sustavi predikcije čiji izlaz traži provjeru.
9. Postavljeni sustav kroz podatke, sučelje, odluke, povratnu spregu i nadzor;
   obavijest, objašnjenje, prigovor i žalba dio su ocjene sustava, a ne dodatak.
10. Ljestvica AI kompetencija ovdje traži reviziju podjele na skupove, oznaka,
    curenja informacija, praga, pogrešaka po podskupinama, pomaka distribucije i
    valjanosti kodiranja.
11. Granica Dijela V: puna mapa tvrdnji sa šest dimenzija i šest revizijskih
    pitanja, odgovoriva samoprovjera, zadatak dohvata unatrag te predaja praga,
    tereta pogreške, nadzora i prigovora poglavlju 18.

**Nosivi pojmovi**: tekstna jedinica, granica korpusa, okvir kodiranja,
zabilježeni referentni ishod, klasifikacijski prag, tablica zabune, pogreške po
podskupinama, algoritamska pravednost, razdvajanje na skup za učenje, provjeru i
ispitivanje, preprilagodba, pomak distribucije, jezični model kao sustav
predikcije.

**Preduvjeti**: poglavlja 2, 3, 8, 10, 11, 13 i 16.

**Isključenja**

1. Poglavlje se ne smije čitati bez poglavlja 13, i nijedan oglašeni put kroz
   knjigu ne smije čitatelja uputiti u poglavlje 17 bez poglavlja 13.
2. Kralježnica je podređena ratificiranom identitetskom brifu `c17` i ne
   ponavlja njegov argument.
3. Nikakva provedba obrade prirodnoga jezika, tokenizatora ni predobrade; ulaz
   su isporučeni tekst i pripremljene tablice.
4. Nikakva matematika strojnoga učenja i nijedan zadatak treniranja modela.
5. Nikakav izraz "istina" za zabilježeni referentni ishod.
6. Pravednost se ne svodi na jednu mjeru.
7. Nikakav drugi središnji widget i nikakvo uklanjanje postojećega widgeta
   pravednosti; widget ne smije sam nositi objašnjenje.
8. Nijedna nedatirana ili neizvorna tehnička tvrdnja.
9. Nijedan ocijenjeni zadatak pisanja koda; vidljivi je kod kratka potvrda koja
   se čita.
10. Odabir pitanja, pravila uzorkovanja, tekstnoga paketa i obrisa ostaje
    gateovima `G-A4-17` i `G-A3-TEXT`.

## Preduvjeti poglavlja 17 i posljedica za putove

Ovaj gate rješava stavku `R04-C17-prerequisites`. Poglavlje 17 traži sedam
ranijih jedinica, i svaka nosi točno određenu obvezu:

| Preduvjet | Što poglavlje 17 iz njega uzima |
|---|---|
| 2 — Mjerenje i dizajn | kodiranje jezika kao mjerenje, s isključenjima i dvosmislenošću |
| 3 — Kako brojke zavode | temeljna stopa kao operativna pismenost prije klasifikacije |
| 8 — Uzorkovanje | selekcija i granica korpusa; razlika populacijske generalizacije od razdvajanja na skupove |
| 10 — Logika testiranja | vrste pogreške i pogrešiva referentna oznaka |
| 11 — Veličina učinka i snaga | posljedice pogreške i sadržajna veličina prije praga |
| 13 — Kategorički podaci | uvjetni nazivnici i kontingencijska tablica koja postaje tablica zabune |
| 16 — Regresija | model, predviđanje i trenutak predviđanja |

Nijedan preduvjet ne pokazuje na kasniju jedinicu.

Time je podmireno proturječje iz `H-P0-REGISTER-004`. Ogledni kratki put
kritičke pismenosti iz izvornoga pregleda preskakao je poglavlje 13, dok je isti
pregled tražio poglavlje 13 prije poglavlja 17. Odluka je jednoznačna: **prednost
ima preduvjet, a put se mijenja.** `P5-ROUTES` mora izmijeniti oglašeni kratki
put i ne smije objaviti nijedan put koji čitatelja uvodi u poglavlje 17 bez
poglavlja 13. Sam prijenos `H-P0-REGISTER-004` ostaje `pending` i troše ga
`P2-SPINE-V` i `P5-ROUTES`, svaki na svojoj strani.

Ovaj gate ne mijenja i ne zamjenjuje brif `c17`. Njegovo isključenje da
metapodaci o preduvjetima poglavlja 17 ostaju neriješeni do `P2-SPINE-V` i dalje
je točno: ovdje se preduvjeti **odlučuju**, a `P2-SPINE-V` ih **upisuje**.

## Hijerarhija definicija za Dio V

Ovaj gate rješava stavku `R04-C17-definitions`. Odluka slijedi isto pravilo kao
Dijelovi I i IV: blok dobiva samo pojam o kojemu kasnije poglavlje stvarno ovisi.
Kasnije od poglavlja 17 postoji samo završnica, pa je ona jedini mogući ovisnik.

| Poglavlje | `#def-` blok | Proza pri prvoj upotrebi | Odgođeno |
|---|---|---|---|
| 13 | kontingencijska tablica, očekivana frekvencija, hi-kvadrat statistika, prilagođeni standardizirani rezidual, Cramérovo V | uvjetni nazivnik, test prilagodbe, referentna raspodjela | model za kategorički ishod (poglavlje 16, kao čitanje) |
| 14 | jedinica neovisnosti, referentna skupina | razlika aritmetičkih sredina, upareni podaci, Welchov t-test, ovisnost opažanja | opći model (poglavlje 16) |
| 15 | stopa obiteljske pogreške, F-statistika, eta-kvadrat | planirana usporedba, post-hoc postupak, varijanca između i unutar skupina | opći model (poglavlje 16) |
| 16 | rezidual, metoda najmanjih kvadrata, višestruka regresija, koeficijent determinacije | procjenjivana veličina, prilagođena povezanost, interakcija, curenje informacija, izgledi, predviđanje izvan uzorka | klasifikacija i prag (poglavlje 17) |
| 17 | zabilježeni referentni ishod, klasifikacijski prag | tekstna jedinica, granica korpusa, okvir kodiranja, tablica zabune, algoritamska pravednost, preprilagodba, razdvajanje na skupove, pomak distribucije | — |

Poglavlja 13, 14, 15 i 16 zadržavaju svojih pet, dva, tri i četiri postojeća
bloka nepromijenjena. Sva su unutar ratificiranoga pojasa
`bands.definitions_per_chapter`, koji traži od jednoga do pet, i nijedna stavka
registra ne traži izmjenu njihova broja.

Poglavlje 17 trenutno nema nijedan blok i time pada ispod pojasa. Dobiva točno
dva, svaki s imenovanim kasnijim ovisnikom:

- **zabilježeni referentni ishod** — stavka `R24-C17-recorded-reference` traži
  jedan dosljedan izraz kroz prozu, prikaz, natpis i alternativni tekst, a
  kanonski je blok upravo mehanizam koji taj oblik učvršćuje. Poglavlje 18 o
  njemu ovisi jer njegov paket dokaza traži putovnicu korpusa s oznakama i
  granicama tvrdnje. Prvi susret uredno prethodi formalizaciji: poglavlje 10 već
  nosi pogrešivu referentnu oznaku u prozi.
- **klasifikacijski prag** — stavka `R27-C17-18-transition` i uloga sadnje u
  brifu `c17` izrijekom predaju prag i nejednak teret pogreške poglavlju 18, koje
  ih provodi na vlastitom paketu dokaza.

Ostali pojmovi poglavlja 17 ostaju u prozi uz mehanizam `.pojam`. Tri su
odbijena bloka vrijedna izričitoga obrazloženja. **Tablica zabune** ne dobiva
blok jer je ona kontingencijska tablica s uvjetnim nazivnicima, već definirana u
poglavlju 13; drugi bi zapis stvorio dva izvora istine o istome objektu i
oslabio upravo onaj preduvjet koji ovaj gate ratificira. **Algoritamska
pravednost** ne dobiva blok jer bi jedna definicijska rečenica gurnula poglavlje
prema svođenju pravednosti na jednu mjeru, što brif `c17` i nit posljedica
pogreške izričito zabranjuju. **Preprilagodba i razdvajanje na skupove** ne
dobivaju blok jer nijedno kasnije poglavlje ne ovisi o njihovoj formalnoj
definiciji: glavna studija završnice je objasnidbena prema odluci D13 i izričito
ne koristi svaki predikcijski alat poglavlja 17.

Poglavlje 17 time prelazi s nula na dva bloka i ulazi u pojas. Dio V ide s
četrnaest na šesnaest blokova. Neto učinak na zamrznuti skup od 46 živih
definicija, zajedno s već odobrenim kartama ranijih gateova, iznosi 51:
46 + 3 (`G-A2b-I`) − 2 (`G-A2b-II`) + 0 (`G-A2b-III`) + 2 (`G-A2b-IV`) + 2 (ovaj
gate).

Ovaj gate nijedan blok ne piše. Kartu provodi `WD-C17` nad stvarnom prozom i
`P2-TERMS` nad ledgerom i grafom pojmova, nakon što `G-A2c` utvrdi kanonske
hrvatske oblike. Do tada `H-P1C-INTEGRITY-002` drži skup od 46 definicija
zamrznutim.

Kanonski hrvatski oblici svih pojmova iz ove kralježnice ostaju odluka gatea
`G-A2c`. To osobito vrijedi za pojmove koje knjiga danas piše u više inačica —
skup za treniranje i skup za testiranje naspram razdvajanja na skup za učenje,
provjeru i ispitivanje — te za pojmove `procjenjivana veličina` i `curenje
informacija`, koje kralježnica imenuje kao nosive, ali ne kanonizira.

## Točne oznake za deterministički provjeritelj

Paket `P2-SPINE-V` upisuje ovu kralježnicu i proširuje
`scripts/check-chapter-spines.py` točno ovim obvezama. Oznake su doslovni
podnizovi teksta isključenja.

| Jedinica | Obvezne oznake isključenja |
|---|---|
| 13 | `katalog testova za kategoričke podatke`, `mjera jačine povezanosti`, `Kalibracija pod nultom hipotezom`, `ocijenjeni zadatak pisanja koda` |
| 14 | `homoskedastičnom OLS nesigurnošću`, `katalog testova za dvije skupine`, `trošenje sinteze poglavlja 16`, `ocijenjeni zadatak pisanja koda` |
| 15 | `katalog post-hoc postupaka`, `Neformalni omjer varijanci`, `trošenje sinteze poglavlja 16`, `ocijenjeni zadatak pisanja koda` |
| 16 | `prilagođavanje logističkoga modela`, `ponovno procjenjivanje objavljene tablice`, `zamjena procjenjivane veličine`, `ocijenjeni zadatak pisanja koda` |
| 17 | `bez poglavlja 13`, `podređena ratificiranom identitetskom brifu c17`, `tokenizatora ni predobrade`, `ocijenjeni zadatak pisanja koda` |

| Jedinica | Obvezni nosivi pojmovi |
|---|---|
| 13 | kontingencijska tablica, uvjetni nazivnik, očekivana frekvencija, prilagođeni standardizirani rezidual |
| 14 | jedinica neovisnosti, razlika aritmetičkih sredina, Welchov t-test, referentna skupina |
| 15 | stopa obiteljske pogreške, F-statistika, planirana usporedba, eta-kvadrat |
| 16 | linearna regresija, procjenjivana veličina, prilagođena povezanost, curenje informacija, interakcija |
| 17 | tekstna jedinica, zabilježeni referentni ishod, klasifikacijski prag, tablica zabune, algoritamska pravednost |

Uvjeti redoslijeda ratifikacije jednaki su popisima preduvjeta: 13 nakon 2, 3,
4, 10, 11 i 12; 14 nakon 2, 4, 9, 10 i 11; 15 nakon 9, 10, 11 i 14; 16 nakon 2,
5, 6, 9, 13, 14 i 15; 17 nakon 2, 3, 8, 10, 11, 13 i 16.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Očuvati poglavlje 16 kao isplatu sinteze | Ugovor dijela; aspekt 16.1; isključenja 14.3 i 15.4 |
| Poglavlje 13 jest preduvjet poglavlja 17 | Aspekti 13.11 i 17.2; popis preduvjeta poglavlja 17; isključenje 17.1 |
| Uvjetni nazivnici i tablice zabune moraju prethoditi pravednosti i klasifikaciji | Aspekti 13.3, 13.11 i 17.5; tablica preduvjeta |
| Time se rješava proturječje iz `H-P0-REGISTER-004` | Odjeljak o preduvjetima i posljedici za putove |
| Posljedica je obvezujuća za `P2-SPINE-V` i `P5-ROUTES` | Isključenje 17.1; blokirane ovisnosti; prijenos `H-G-A2B-V-001` |
| Kralježnica poglavlja 17 podređena je brifu `c17` i ne ponavlja ga | Uvodna napomena poglavlja 17 i isključenje 17.2 |
| Riješiti `R04-C17-definitions` kroz tu identitetsku kralježnicu | Hijerarhija definicija; dva bloka, svaki s imenovanim kasnijim ovisnikom |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki. Ostali aspekti nisu
novi zahtjevi. Svaki provodi već ratificiranu stavku registra, prihvaćenu
odluku, prihvaćenu arhitekturu ili ratificirani brif.

| Aspekt | Već ratificirani izvor |
|---|---|
| 13.1 | `R27-C13-partV-contract` |
| 13.3 i 13.10 | nit nazivnika i `R13-C13-contingency` |
| 13.6 | prihvaćeni `R09-C13-residual-name` |
| 13.7 | prihvaćeni `R09-C13-calibration-power` |
| 14.4 | prihvaćena odluka D02 i `R02-C14-welch-ols` |
| 14.8 i 15.9 | `R22-C14-C16-dependence` |
| 15.7 | `R09-C15-variance-ratio` |
| 15.8 | `R23-C15-suspect-code` |
| 16.2 i 16.3 | prihvaćeni `R09-C16-estimand` i `R09-C16-uncertainty` |
| 16.4 | `R14-C16-adjustment-contract` |
| 16.5 | `R14-C16-interaction` |
| 16.6 | prihvaćeni `R09-C16-leakage-time` |
| 16.7 | `R29-C16-retrieval` |
| 16.8 | `R14-C16-binary-reading` i `R14-SCOPE-reading-not-fitting` |
| 16.9 | `R16-C16-table`, `R16-C16-paragraph`, `R16-C16-no-refit` |
| 16.10 | `R08-C16-cross-design` |
| 16.11 | prihvaćeni `R17-REPORT-honest-standard` i nit komunikacije |
| 17.1 do 17.9 | ratificirani identitetski brif `c17` |
| 17.3 i 17.4 | `R24-C17-recorded-reference`, `R24-C17-label-process`, `R24-C17-selective-observation` |
| 17.5 | `R10-C03-base-rate` i nit posljedica pogreške |
| 17.6 | `R13-C17-performance-validity` |
| 17.7 | `R12-SAMPLING-vs-test` i isključenja životnoga ciklusa |
| 17.8 i 17.9 | `R24-C17-LLM-prediction`, `R24-C17-system-feedback`, `R24-C17-procedural-fairness` |
| 17.10 | `R24-LADDER-C17` |
| 17.11 | `R35-SELF-CHECK-V` i `R27-C17-18-transition` |
| isključenja o čitanju umjesto proizvodnje | `R23-SCOPE-reading-not-production`, `R23-C17-no-R-production`, `R23-C17-no-tokenizer`, `R23-C17-visible-receipt` |
| isključenje o nedatiranim tehničkim tvrdnjama | `R24-C17-primary-sources` |
| isključenje o widgetu pravednosti | odluka D07, `R13-C17-placement`, `R07-C17-widget-prose-balance` |

## Razmotrene alternative

1. **Otvoriti Dio V regresijom pa se vratiti na jednostavnije usporedbe.**
   Odbijeno: proturječi odluci D03 o očuvanju makro-poretka i potrošilo bi
   isplatu poglavlja 16 na prvoj stranici dijela.
2. **Otkriti opći model već u poglavlju 14 ili 15.** Odbijeno: proturječi
   zabilježenoj namjeri da poglavlje 16 ostane isplata sinteze i ratificiranom
   pravilu da poglavlja 14 i 15 pripremaju jezik općega modela, ali ga ne troše.
3. **Ostaviti poglavlje 13 izvan preduvjeta poglavlja 17 i zadržati oglašeni
   kratki put nepromijenjenim.** Odbijeno: proturječi zabilježenoj namjeri i
   ostavlja `H-P0-REGISTER-004` neriješenim; čitatelj bi u tablicu zabune ušao
   bez uvjetnoga nazivnika.
4. **Izmijeniti preduvjet umjesto puta, tako da poglavlje 17 samo ukratko ponovi
   uvjetne nazivnike.** Odbijeno: pretvara poglavlje 13 u neobvezno, uvodi
   ponovljeno mini-predavanje koje pravilo niti izričito zabranjuje i probija
   opseg identitetskoga stupa.
5. **Dati poglavlju 17 blok za tablicu zabune.** Odbijeno: tablica zabune jest
   kontingencijska tablica s uvjetnim nazivnicima, već definirana u poglavlju 13;
   drugi zapis stvorio bi dva izvora istine.
6. **Dati poglavlju 17 blok za algoritamsku pravednost.** Odbijeno: definicijska
   rečenica gura prema svođenju pravednosti na jednu mjeru, što brif `c17`
   izričito zabranjuje.
7. **Ne dodati poglavlju 17 nijedan blok.** Odbijeno: ostavlja poglavlje ispod
   ratificiranoga pojasa i ostavlja završnicu bez kanonskoga pojma za oznaku i
   prag koje mora provesti na vlastitom paketu dokaza.
8. **Dodati poglavlju 16 blok za procjenjivanu veličinu.** Odbijeno: prihvaćeni
   registar tvrdnji već knjigom nosi revizijsko pitanje o ciljnoj veličini i
   vrsti tvrdnje, pa bi blok udvostručio već ratificiran mehanizam; pojam ostaje
   nosiv i ostaje u prozi.
9. **Ponoviti argument brifa `c17` unutar kralježnice poglavlja 17.** Odbijeno:
   kralježnica je podređena brifu; dva zapisa istoga argumenta stvorila bi dva
   izvora istine.
10. **Uvesti logističku regresiju kao postupak u poglavlju 16 ili 17.**
    Odbijeno: proturječi `R14-SCOPE-reading-not-fitting` i
    `R23-SCOPE-reading-not-production` i probija granicu opsega knjige.

## Obvezujuće autorove izmjene od 5. kolovoza 2026.

Obje izmjene pročitane su prije odluke i obje ovdje vrijede.

Neovisni recenzent nazivlja povučen je iz prvoga izdanja. Ova kralježnica **ne
tvrdi i ne pretpostavlja nikakvu neovisnu recenziju** — nazivlja ni bilo čega
drugoga. Kanonski hrvatski oblici pojmova iz Dijela V ostaju odluka gatea
`G-A2c` i isključiva su odgovornost autora i urednika.

Za odabrane izvatke DZS-a i DIP-a nije traženo niti dobiveno dopuštenje vlasnika
prava. Ova kralježnica **ne tvrdi nikakvo dopuštenje** ni za jedan izvor i ne
bira nijedan podatkovni paket: poglavlja 13, 14, 15 i 16 upućuju izbor gateovima
`G-A3-DIP`, `G-A3-ESS` i `G-A4-16`, a poglavlje 17 gateovima `G-A3-TEXT` i
`G-A4-17`.

Ta se dva ograničenja namjerno **ne** upisuju kao isključenja pojedinačnih
kralježnica. Njihovi durabilni zapisi već imenuju točne pakete koje vežu —
`P2-TERMS`, `P2-DOCS`, `P6-METHODS`, `P6-VERIFY` i `P8-META` za recenzenta, te
`G-A3-DZS`, `P3-DZS`, `G-A3-DIP`, `P3-DIP`, `P3-CATALOG` i `P8-META` za prava —
pa bi njihovo udvostručavanje u registru kralježnica stvorilo drugi izvor istine
o obvezi koju taj registar ne posjeduje. Ovaj gate stoga bilježi usklađenost, a
ne novu obvezu.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu Dijela V, njezinu hijerarhiju
definicija i točne preduvjete poglavlja 17. Ne odobrava prozu nijednoga
poglavlja i ne mijenja nijednu datoteku poglavlja niti dodatka. Ne upisuje ništa
u `bookwright_plugin/bookwright/shared/chapter-spine.json`; to je posao paketa
`P2-SPINE-V`. Ne dodaje, ne briše i ne spaja nijedan `#def-` blok i ne
regenerira graf pojmova; to ostaje paketima `WD-C13` do `WD-C17` i `P2-TERMS`.
Ne troši `H-P1C-INTEGRITY-002`, koji ostaje obveza paketa `P2-TERMS`, ni
`H-P0-REGISTER-004`, koji ostaje obveza paketa `P2-SPINE-V` i `P5-ROUTES`, ni
`H-P0-REGISTER-007` i `H-P0-REGISTER-008`, koji ostaju obveze paketa `WD-C17`.
Ne mijenja i ne zamjenjuje ratificirani identitetski brif `c17` ni zajednički
ugovor identitetskih stupova. Ne utvrđuje kanonsku terminologiju, koja ostaje
gateu `G-A2c`. Ne definira i ne objavljuje nijedan put čitanja; `P5-ROUTES`
zadržava tu ovlast i s njom obvezu izmjene kratkoga puta. Ne ratificira nijednu
kasniju kralježnicu, ne otvara `G-A2b-FINALE` i ne pokreće `P2-SPINE-V`. Ne bira
nijedan podatkovni paket, izvor, slučaj, objavljenu tablicu ni tekstni korpus i
ne tvrdi nikakvo dopuštenje vlasnika prava. Ne mijenja fazu nijedne jedinice,
koja ostaje `draft`. Ne odobrava render, generirani artefakt, push, merge, tag,
arhiviranje, deployment ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavke `R04-SPINE-V`, `R04-C17-definitions` i `R04-C17-prerequisites`;
- paket `P2-SPINE-V`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json` i proširuje
  `scripts/check-chapter-spines.py`.

Ovisnosti koje ostaju blokirane: `WD-C13`, `WD-C14`, `WD-C15`, `WD-C16` i
`WD-C17` čekaju svoje podatkovne i brif-gateove te svoje gateove prihvaćanja
`C13` do `C17`; `WD-C16` uz to čeka `G-A4-16`, a `WD-C17` čeka `G-A4-17`,
`G-A3-TEXT` i `P3-TEXT`; `WD-PART` čeka svoja poglavlja; `P2-TERMS` čeka
`G-A2c`; `P5-ROUTES` čeka svoju fazu i ondje troši `H-P0-REGISTER-004`;
`G-A2b-FINALE` i `P2-SPINE-FINALE` ostaju zasebni i neotvoreni.
