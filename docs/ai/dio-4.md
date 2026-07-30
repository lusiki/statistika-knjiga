# DIO IV: ZAKLJUČIVANJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Logika testiranja

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Simulator p-vrijednosti | simulirana populacija | pogl. 7–9 |

**Vinjeta.**
Američko statističko udruženje moralo je 2016. javno razjasniti p-vrijednost jer
je jedan računski izlaz prečesto služio kao automatska odluka o postojanju
učinka (Wasserstein, 2016). Udruženje se u svojoj povijesti dotad nije oglasilo o
pojedinačnom statističkom postupku, pa je sama izjava bila priznanje da problem
nije u računu nego u tome što se s njim radi.

Izvještaji su prag pretvarali u granicu između rezultata koji „postoje" i onih
koji „ne postoje". Postupak takvu podjelu ne može nositi, jer ne uspoređuje dvije
tvrdnje o svijetu nego jednu tvrdnju s onim što bi slučajnost proizvela.

Što mala p-vrijednost govori o podacima, a što ne može reći o hipotezi?

## Sudnica i njezina asimetrija

Testiranje počinje pretpostavkom u koju nitko ne vjeruje. Postupak najprije
opiše svijet u kojem učinka koji tražimo nema, izračuna što bi taj svijet
proizveo, i tek onda pogleda podatke. Ako podaci u takvom svijetu izgledaju
neobično, pretpostavka postaje neodrživa.

**Nulta hipoteza** je precizan model postupka koji je proizveo podatke, sastavljen
tako da u njemu nema razlike ni veze koju istražujemo.

Alternativna hipoteza opisuje odstupanje koje bi nas zanimalo i namjerno je
neodređena, jer obuhvaća sve razlike osim nulte. Te dvije tvrdnje nisu
ravnopravne suparnice. Samo nulta hipoteza dovoljno je precizna da se iz nje
može izračunati što će se dogoditi, i zbog toga cijeli postupak stoji na njoj.

Analogija sa suđenjem tu asimetriju objašnjava bolje od bilo koje formule. Sud
polazi od pretpostavke nevinosti, a tužiteljstvo iznosi dokaze protiv nje.
Presuda kojom optužba nije dokazana nije utvrđenje nevinosti nego izjava da
dokazi nisu bili dovoljni. Statistički postupak radi isto, pa neodbacivanje
nulte hipoteze nikada ne znači da je ona istinita.

Analogija ima i granicu koju vrijedi navesti odmah. Sud presuđuje o jednom
događaju, a test opisuje ponašanje postupka kroz mnogo ponavljanja. Sve što
slijedi vrijedi za postupak, a ne za pojedini rezultat, i upravo se to u
izvještajima gubi.

Zbog toga se dio odluka mora donijeti prije podataka. Nulti model treba biti
zapisan tako da se iz njega može računati, mjera odstupanja odabrana, a prag uz
koji će se rezultat čitati postavljen dok se još ne zna kako će podaci ispasti.
Ništa od toga nije tehnička priprema. Postupak čije se komponente biraju nakon
pogleda na podatke više nema stopu pogreške koju obećava, jer je obećanje dano
za postupak koji se ponavlja jednak, a ne za onaj koji se dotjeruje. Koliko se
tim putem može doći dokazuje poglavlje o krizi i obnovi.

## Kako se gradi svijet bez učinka

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s10$n` osoba koje se primarno informiraju preko
portala ili preko tiska, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije.

Prvo dolazi ono što odgovara na postavljeno pitanje. Razlika između sredina
iznosi `r hr_broj(s10$razlika, 2)` boda u korist tiska, uz interval pouzdanosti
od `r hr_broj(s10$donja, 2)` do `r hr_broj(s10$gornja, 2)`. Test dolazi tek
poslije, jer odgovara na uže pitanje, na to je li s podacima uskladiva i nula.

Nulti model za ovo pitanje ne treba izvoditi računom. Ako izvor vijesti nema
nikakve veze s povjerenjem, onda su oznake skupina samo naljepnice koje su
jednako mogle biti razdijeljene bilo kako. Promiješamo ih dakle nasumično,
izračunamo razliku sredina, i to ponovimo mnogo puta. Dobiveni raspon razlika
točno je ono što nulti model dopušta.

**Testna statistika** je jedan broj izračunat iz podataka koji sažima odstupanje
od nultog modela u obliku usporedivom s odstupanjima koja taj model proizvodi.

Ovdje je ta statistika sama razlika sredina, jer je upravo ona ono o čemu se
odlučuje. Sljedeći graf prikazuje što nulti model s njome radi kroz četiri
tisuće premještanja, a uz njega stoji razlika koju je dao stvarni raspored
oznaka.

*Slika. Razlike sredina kroz četiri tisuće nasumičnih premještanja oznaka skupine, uz okomitu crtu na razlici opaženoj u uzorku.*

Nulta raspodjela ima sredinu u nuli i standardnu devijaciju od
`r hr_broj(s10$sd_nulte, 2)` boda. Devedeset pet posto premještanja daje razliku
manju od `r hr_broj(s10$granica, 2)` boda po apsolutnoj vrijednosti, dakle sve
unutar tog raspona nulti model proizvodi bez ikakve pomoći. Opažena razlika od
`r hr_broj(s10$razlika, 2)` boda leži izvan njega.

Preostaje prebrojati koliko je premještanja dalo odstupanje barem toliko veliko
kao opaženo. Taj udio ima ime.

**P-vrijednost** je udio rezultata koje nulti model proizvodi, a koji su s njime
u najmanju ruku jednako neusklađeni kao opaženi rezultat.

U našem uzorku iznosi `r hr_broj(s10$p, 3)`. Rečenica koja iz toga slijedi ima
oblik koji vrijedi zapamtiti doslovno. Kad izvor vijesti ne bi imao nikakve veze
s povjerenjem, razliku ovoliku ili veću vidjeli bismo u otprilike
`r hr_broj(s10$p * 100, 1)` % uzoraka. Sve što p-vrijednost kaže stoji u toj
rečenici, i svaka tvrdnja koja iz nje izlazi mora biti opravdana posebno.

## Interakcija — Simulator p-vrijednosti

Sljedeći prikaz radi ono što jedan uzorak ne može. Postupak ponavlja mnogo puta,
odvojeno u svijetu u kojem učinka nema i u svijetu u kojem ga ima, i prikazuje
kako se p-vrijednosti raspoređuju u jednom i u drugom. Radi preglednosti koristi
normalne ishode s poznatom varijabilnošću i obostrani test.

*Slika. Raspodjele p-vrijednosti pod nultim modelom i pod odabranim stvarnim učinkom.*

**Što isprobati.**

1. Postavite stvarnu razliku na nulu i opišite oblik gornje raspodjele.
2. Podignite stvarnu razliku na 0,35 uz nepromijenjen uzorak.
3. Povećajte uzorak bez promjene razlike i usporedite udio rezultata ispod praga.
4. Spustite prag s 0,05 na 0,01 i pogledajte obje raspodjele.

Prvi korak otkriva svojstvo koje iznenađuje gotovo svakoga. Kad učinka nema,
p-vrijednosti su ravnomjerno raspoređene po cijelom rasponu od nule do jedinice,
pa je vrijednost od 0,03 pod nultim modelom jednako vjerojatna kao vrijednost od
0,53. Prag ne odvaja obično od neobičnog nego odsijeca unaprijed određen udio te
ravnomjerne raspodjele, i taj udio je sve što prag jamči.

## Dvije vrste pogreške

Postupak može pogriješiti na dva načina i nijedan se ne može ukloniti. Kad se
odbaci nulta hipoteza koja je istinita, radi se o pogrešci prve vrste. Kad se ne
odbaci nulta hipoteza koja je lažna, radi se o pogrešci druge vrste.

**Pogreška prve vrste** je odbacivanje nulte hipoteze koja je istinita, a udio
takvih odbacivanja u dugom nizu ponavljanja postupka jednak je odabranom pragu.

Ta se tvrdnja obično iznosi kao definicija, a u ovoj se knjizi može izmjeriti,
jer je populacija poznata. Postavimo pitanje na koje unaprijed znamo odgovor.
Razlikuju li se žene i muškarci po povjerenju u medije? U populaciji ta razlika
iznosi `r hr_broj(s10$istina_spol, 3)` boda, dakle nule nema samo zato što je
populacija konačna. Nulta hipoteza je za to pitanje praktički istinita.

Provedemo li isti permutacijski postupak na osamsto novih uzoraka od
`r s10$n` osoba, prag od 0,05 prijeđe ih `r hr_broj(s10$stopa_spol, 1)` %. Prag
je dakle održao obećanje, i to je jedino obećanje koje daje.

*Slika. Udio uzoraka u kojima permutacijski postupak prelazi prag od 0,05, za dva pitanja s poznatim odgovorom. Osamsto uzoraka po pitanju, u svakome tristo premještanja. Izrada autora.*

Drugi redak tablice nosi drugu vrstu pogreške. Razlika po izvoru vijesti u
populaciji doista postoji i iznosi `r hr_broj(s10$istina_izvor, 2)` boda, a
postupak je pronalazi u `r hr_broj(s10$stopa_izvor, 1)` % uzoraka. U preostalih
`r hr_broj(s10$promasaj, 1)` % istraživač bi zaključio da nema dovoljno dokaza,
i pritom bi se pridržavao svih pravila.

*Slika. Raspodjela procijenjene razlike kad učinka nema i kad postoji, uz isprekidane crte na graničnim vrijednostima postupka.*

Slika pokazuje zašto se dvije pogreške ne mogu istovremeno smanjivati. Granične
crte određene su gornjom raspodjelom, a odsijecaju i donju. Pomaknemo li ih
prema van kako bismo rjeđe pogriješili na prvi način, veći dio donje raspodjele
ostaje između njih i postupak češće promašuje stvarnu razliku. Jedini način da
oba udjela padnu jest razmaknuti dvije raspodjele, a to se postiže većim uzorkom
ili preciznijim mjerenjem, dakle odlukama iz dizajna, a ne izborom praga.

Koliki je uzorak za to potreban i kako se planira unaprijed, tema je sljedećeg
poglavlja. Ovdje je dovoljno vidjeti da udio promašaja nije svojstvo testa nego
posljedica dizajna, i da se o njemu odlučuje prije prikupljanja podataka.

## Prag je konvencija, a ne mjera

Prag od 0,05 pojavljuje se u ovom poglavlju kao zadana vrijednost, a postupak ga
ničim ne zahtijeva. Widget dopušta da se pomakne na 0,01 ili na 0,10 i ništa se
u računu ne buni, jer prag samo određuje koliki udio nultog modela pristajemo
odsjeći. Odabir je stvar dogovora struke i posljedica koje pogreška nosi, pa u
području u kojem je lažni nalaz skup ima smisla biti stroži nego u području u
kojem je propušten nalaz skuplji.

Iz toga slijedi da razlika između rezultata tik ispod praga i onoga tik iznad
nije razlika u dokazu. Vrijednosti 0,048 i 0,052 gotovo su isti broj, a
izvještaj koji jednu naziva nalazom, a drugu odsutnošću nalaza uvodi razliku
koje u podacima nema. Upravo to je razlog zbog kojeg izjava Američkog
statističkog udruženja traži da znanstveni zaključak ne ovisi samo o tome
prelazi li p-vrijednost određeni prag (Wasserstein, 2016).

Postoji i drugi razlog, koji se rijetko spominje, a lako se izmjeri. Ponovili
smo pitanje o izvoru vijesti na osamsto uzoraka iz iste populacije, u kojoj
razlika stvarno postoji i uvijek je jednaka. U polovici uzoraka p-vrijednost je
bila ispod `r hr_broj(s10$ples_sredina, 3)`, u četvrtini iznad
`r hr_broj(s10$ples_cetvrtina, 3)`, a u desetini iznad
`r hr_broj(s10$ples_gornji, 3)`. Ista populacija, isti postupak i ista veličina
uzorka daju p-vrijednosti raspoređene preko dva reda veličine, pa je u
`r hr_broj(s10$udio_iznad_deset, 1)` % uzoraka rezultat prešao i granicu od 0,10.

P-vrijednost je dakle i sama statistika koja se mijenja od uzorka do uzorka, i
to snažnije od gotovo svake druge veličine u knjizi. Izvještaj koji je navodi na
tri decimale sugerira preciznost koju ona nema, a ponovljeno istraživanje s
istim dizajnom lako proizvede vrijednost desetostruko drugačiju. Procjena i
njezin interval pod ponavljanjem se ponašaju mnogo mirnije, i to je jedan od
razloga zbog kojih u izvještaju stoje prvi.

## Što p-vrijednost nije

Vratimo se pitanju o spolu, gdje odgovor unaprijed znamo. U našem uzorku razlika
iznosi `r hr_broj(s10$razlika_spol, 2)` boda uz interval od
`r hr_broj(s10$donja_spol, 2)` do `r hr_broj(s10$gornja_spol, 2)`, a p-vrijednost
je `r hr_broj(s10$p_spol, 2)`. Postupak je ovdje postupio ispravno, jer razlike
doista nema.

Izvještaj koji bi iz toga zaključio da razlike nema rekao bi ipak previše.
Interval dopušta razlike do gotovo pola boda u oba smjera, a to je raspon unutar
kojeg bi se uredničke odluke razlikovale. Da je razlika u populaciji iznosila
trećinu boda, ovaj bi uzorak jednako izgledao. Velika p-vrijednost znači da
podaci nisu neusklađeni s nultim modelom, a ne da su s njime posebno usklađeni.

Najčešća pogreška ide u suprotnom smjeru i tiče se malih p-vrijednosti. Za naše
pitanje o izvoru vjerojatnost od `r hr_broj(s10$p, 3)` odnosi se na podatke pod
pretpostavljenim modelom, a ne na model pod opaženim podacima. To su dvije
različite uvjetne vjerojatnosti, upravo one koje je poglavlje o vjerojatnosti
razdvojilo, i njihova zamjena mijenja tvrdnju iz temelja.

Iz iste zamjene slijede još dvije rečenice koje treba prepoznati. P-vrijednost
nije vjerojatnost da je nalaz nastao slučajno, jer se već računa pod
pretpostavkom da jest. I nije mjera veličine učinka, jer ovisi o uzorku jednako
koliko i o razlici, pa dovoljno velik uzorak proizvodi male vrijednosti i za
razlike koje nikoga ne zanimaju.

## Drugo pitanje i drugi račun

Pitanje koje istraživači zapravo imaju obično glasi koliko je vjerojatno da
učinak postoji. Postupak iz ovog poglavlja na njega ne odgovara i nije za njega
ni napravljen. Odgovor na to pitanje traži nešto što test nigdje ne traži, a to
je izjava o tome što se držalo vjerojatnim prije podataka.

Bayesovski pristup upravo tu izjavu zahtijeva. Istraživač unaprijed navodi koliko
su mu koje vrijednosti učinka vjerojatne, podaci tu raspodjelu mijenjaju, i
rezultat je nova raspodjela vjerojatnosti nad mogućim učincima. Iz nje se može
očitati vjerojatnost da je učinak veći od nule ili veći od neke granice koja je
sadržajno važna, dakle upravo ono što se od p-vrijednosti pogrešno očekuje.

Cijena je vidljiva i nije skrivena. Početnu raspodjelu netko mora postaviti i
obrazložiti, a različiti izbori daju različite zaključke iz istih podataka. Za
pristup koji se često predstavlja kao izlaz iz proizvoljnosti to je neugodna
osobina, no ona je barem eksplicitna. U testiranju su pretpostavke jednako
prisutne, samo se ne moraju izgovoriti.

Knjiga ostaje na frekvencijskom putu jer je to jezik kojim je napisana golema
većina istraživanja koja čitatelj mora znati pročitati. Bayesovski račun ovdje
ostaje pogled kroz prozor, s napomenom da odgovara na drugo pitanje i da mu za
to treba dodatan ulaz. Poglavlje o regresiji na tu razliku se vraća u
zaključnom pogledu unaprijed.

**Statistika u divljini.**
**Popis od dvadeset pet.** Sedmorica statističara objavila su u recenziranom
časopisu popis od dvadeset pet pogrešnih tumačenja p-vrijednosti, intervala
pouzdanosti i snage, uz obrazloženje svakoga (Greenland, 2016). Autori u istom
radu tvrde da pogrešna tumačenja tih pojmova ostaju raširena unatoč desetljećima
upozorenja i da ne postoji tumačenje koje bi istovremeno bilo jednostavno,
intuitivno, ispravno i otporno na pogrešku.

Iz postojanja takvog popisa slijedi zaključak koji nije o nemaru. Pogreške se
ponavljaju jer postupak odgovara na jedno pitanje, a čitatelju treba drugo, pa
prijevod između njih mora obaviti netko drugi i najčešće ga nitko ne obavi. Isti
rad upozorava i na to da mala p-vrijednost može nastati i kad je nulti model
točan, ako je analiza birana prema rezultatima koje daje, čime pomiče krivnju s
pojedinačnog čitanja na cijeli postupak istraživanja. Popis dakle ne služi da
bi se provjerila tuđa rečenica, nego da bi se prepoznalo koje pitanje analiza
uopće može zatvoriti.

**Pitajte model.**
Asistent pouzdano provede test i ispiše p-vrijednost, a rijetko sam postavi ono
što mu prethodi. Prije poziva treba mu reći koja je jedinica opažanja i što nulti
model tvrdi, jer iz tablice ne može zaključiti smiju li se oznake premještati
slobodno. Provjeravamo tri stvari u odgovoru. Prva je redoslijed, jer procjena i
interval moraju stajati ispred testa. Druga je rečenica kojom tumači
p-vrijednost, koju vrlo često napiše kao vjerojatnost hipoteze. Treća je
zaključak iz velike p-vrijednosti, koji redovito pretvara u tvrdnju da razlike
nema.

> Imenuj nulti model i jedinicu premještanja, izgradi nultu raspodjelu
> simulacijom i usporedi je s opaženom statistikom. Izvijesti procjenu s
> intervalom prije p-vrijednosti i napiši što bi rezultat značio da je stvarna
> razlika upola manja.

**Nađite grešku.**
Na pitanje razlikuju li se čitatelji tiska i portala po povjerenju u medije
asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Oznake skupina premještene su četiri tisuće puta,
a razlika ovoliku ili veću daje `r hr_broj(s10$p * 100, 1)` % premještanja.
Budući da je taj udio ispod praga, zaključuje da vjerojatnost da između dviju
skupina nema razlike iznosi `r hr_broj(s10$p * 100, 1)` %.

Greška je posljednja rečenica, u kojoj udio premještanja postaje vjerojatnost
hipoteze. Kod i sve prije te rečenice su ispravni. Izračunati udio odnosi se na
rezultate koje nulti model proizvodi, dakle uvjetovan je time da razlike nema, a
tvrdnja ga okreće u vjerojatnost samog modela nakon podataka. Popravak je
napisati što je izračunato, dakle da bi razliku ovoliku ili veću nulti model
proizveo u `r hr_broj(s10$p * 100, 1)` % uzoraka, i uz to navesti procjenu
razlike s intervalom.

## Razrađeni primjer

Cijeli se postupak može ispisati u nekoliko redaka, i vrijedi ga jednom vidjeti
u cjelini. Analiza najprije računa opaženu razliku, zatim gradi nultu raspodjelu
premještanjem oznaka, i na kraju prebrojava koliko je premještanja dalo barem
toliko veliko odstupanje.

Funkcija `sample` bez dodatnih argumenata vraća isti niz oznaka u nasumičnom
poretku, a `replicate` ponavlja izraz zadani broj puta i skuplja rezultate. Cijeli
nulti model stane u te dvije funkcije, bez ijedne pretpostavke o obliku
raspodjele.

Izvještaj koji iz ovoga slijedi ima tri rečenice i njihov je redoslijed obvezan.
Čitatelji tiska imaju u prosjeku `r hr_broj(s10$razlika, 2)` boda više povjerenja
od čitatelja portala, uz interval od `r hr_broj(s10$donja, 2)` do
`r hr_broj(s10$gornja, 2)`. Razliku ovoliku ili veću nulti model proizvodi u
`r hr_broj(s10$p * 100, 1)` % uzoraka. Podaci su promatrački i ljudi svoj izvor
biraju sami, pa razlika opisuje dvije skupine, a ne učinak čitanja tiska.

Posljednja rečenica nije opreznost nego točnost. Test je odgovorio na pitanje o
usklađenosti podataka s jednim modelom i ništa više od toga nije ni mogao. Ono
što razlika znači, koliko je velika i vrijedi li na nju reagirati, ostaje
otvoreno i vodi u sljedeće poglavlje.

## Sažetak

Testiranje uspoređuje opaženi rezultat s onim što proizvodi precizno opisan
svijet bez učinka, a nulta raspodjela za tu usporedbu gradi se premještanjem
oznaka umjesto formulom. P-vrijednost je udio takvih rezultata barem toliko
neusklađenih s nultim modelom kao opaženi, i ne kaže ni kolika je vjerojatnost
hipoteze ni koliko je učinak važan. Dvije vrste pogreške povezane su tako da
pomicanje praga jednu smanjuje, a drugu povećava, pa se obje snižavaju samo
boljim dizajnom. Na poznatoj populaciji obje su stope izmjerene, i postupak je
uz istinitu nultu hipotezu održao prag od pet posto, ali je stvarnu razliku od
`r hr_broj(s10$istina_izvor, 2)` boda propustio u svakom petom uzorku. Sljedeće
poglavlje stavlja veličinu učinka i snagu ispred rituala značajnosti.

## Pojmovi

nulta hipoteza (*null hypothesis*), alternativna hipoteza (*alternative
hypothesis*), permutacijski test (*permutation test*), testna statistika (*test
statistic*), p-vrijednost (*p-value*), pogreška prve vrste (*Type I error*),
pogreška druge vrste (*Type II error*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto p-vrijednost nije vjerojatnost nulte hipoteze,
tako da napišete dvije rečenice koje se razlikuju samo po tome što je uvjet, a
što zaključak. Imenujte podatak koji bi bio potreban da se od prve dođe do
druge.

### Računski

Nulta raspodjela iz ovog poglavlja ima sredinu nula i standardnu devijaciju
`r hr_broj(s10$sd_nulte, 2)` boda. Koristeći pravilo područja iz poglavlja o
vjerojatnosti, procijenite koje bi razlike prelazile granicu od dviju
standardnih devijacija, i usporedite svoju procjenu s graničnom vrijednošću
`r hr_broj(s10$granica, 2)` koju poglavlje navodi. Zatim u widgetu poglavlja
postavite stvarnu razliku na nulu i opišite koliko uzoraka prelazi prag.

### Kritički

Prosudite zašto je jednom strukovnom udruženju trebalo objaviti izjavu o
pojedinačnom statističkom postupku, a skupini statističara popis od dvadeset pet
pogrešnih tumačenja (Wasserstein, 2016; Greenland, 2016). Predajte kratku
uredničku bilješku i navedite jedno pravilo izvještavanja koje bi uklonilo
najviše pogrešaka odjednom.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte korake koji su provedeni
ispravno, redak koda iz kojeg izlazi izvještajna brojka, rečenicu koja iz nje ne
slijedi i njezinu ispravljenu inačicu.

---

# Veličina učinka i snaga

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Istraživač snage | simulirana populacija | pogl. 9, 10 |

**Vinjeta.**
Cohen je 1994. objavio kritiku prakse u kojoj je statistička značajnost
zamijenila razmišljanje o veličini i važnosti učinka, pod naslovom koji je
podsjećao da neke tvrdnje ne trebaju test (Cohen, 1994). Nije prigovarao računu.
Prigovarao je tome što je jedan broj preuzeo posao prosudbe.

Prigovor je imao vrlo konkretan oblik. Recenzent koji pročita da je razlika
značajna ne doznaje je li riječ o pomaku koji bi promijenio nečiju odluku ili o
razlici koju je otkrio samo dovoljno velik uzorak. Autor mu tu informaciju nije
uskratio namjerno, nego zato što obrazac izvještavanja nije tražio da je napiše.

Koliko podataka trebamo da bismo pouzdano uočili učinak koji je vrijedan
uočavanja?

## Razlika koja nešto znači

Poglavlje nastavlja usporedbu iz prethodnog. Isti simulirani stanovnici, isto
pitanje o povjerenju u medije među čitateljima tiska i portala, ali sada s
punom populacijom umjesto uzorka, jer nas zanima što je istina, a ne kako je
pogađamo.

Razlika iznosi `r hr_broj(s11$razlika, 2)` boda na ljestvici od jedan do deset.
Ta brojka je najvažniji rezultat cijele usporedbe i mora stajati u izvornim
jedinicama, jer se samo tako o njoj može odlučivati. Uredništvo koje razmišlja o
preraspodjeli sadržaja treba znati govori li se o tri četvrtine boda ili o tri
boda.

Sama razlika ipak ne kaže koliko je velika u odnosu na to kako su ljudi
raspoređeni. Bod razlike znači jedno kad su svi odgovori zbijeni oko sredine, a
nešto posve drugo kad se protežu preko cijele ljestvice. Standardizirana mjera
tu usporedbu ugrađuje u sam broj.

**Standardizirana razlika** je razlika dviju sredina podijeljena združenom
standardnom devijacijom skupina, pa se izražava u standardnim devijacijama
umjesto u izvornim jedinicama.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Oznaka $s_{\text{zdr}}$ stoji za združenu standardnu devijaciju, dakle za
zajedničku mjeru raspršenosti unutar obiju skupina.

Povjerenje se u ovoj populaciji raspršuje sa združenom standardnom devijacijom
od `r hr_broj(s11$zdruzena, 2)` boda, pa razlika od `r hr_broj(s11$razlika, 2)`
boda daje standardiziranu razliku od `r hr_broj(s11$d, 2)`. Dvije skupine dakle
dijeli nešto više od trećine standardne devijacije, što znači da se njihove
raspodjele u najvećem dijelu preklapaju i da po jednom ispitaniku ne bi bilo
moguće pogoditi odakle se informira.

Standardna devijacija kao mjerna jedinica ipak ostaje apstraktna, pa isti učinak
vrijedi izraziti i na način koji se može zamisliti. Izvučemo li nasumce jednog
čitatelja tiska i jednog čitatelja portala, prvi ima više povjerenja u
`r hr_broj(s11$nadmoc, 1)` % slučajeva. Kad razlike ne bi bilo, taj bi udio
iznosio pedeset posto, pa je učinak veličine kakvu ovdje gledamo pomak od desetak
postotnih bodova u tako postavljenom pitanju. Rečenica tog oblika prolazi kroz
uredničku raspravu bolje od bilo koje standardizirane mjere, jer nitko ne mora
znati što je standardna devijacija da bi razumio ishod.

Orijentacijske vrijednosti za takve mjere postoje i najčešće se navode prema
Cohenu, koji ih je ponudio kao pomoć u odsutnosti boljeg oslonca, a ne kao
ljestvicu za očitavanje (Cohen, 1988). Što je učinak ove veličine sadržajno,
odlučuje usporedba s drugim učincima u istom području i cijena postupanja, a ne
tablica pragova. Standardizacija služi tome da se ta usporedba uopće može
napraviti, jer razlike izmjerene u minutama, bodovima i postocima inače nemaju
zajednički jezik.

## Kad je značajno, a nije važno

Test odgovara na pitanje je li s podacima uskladiva i nula. To pitanje s
veličinom učinka ima manje veze nego što se pretpostavlja, i najlakše se to vidi
kad je uzorak vrlo velik.

Zamislimo portal koji uspoređuje dvije naslovnice. Prva ima stvarnu stopu klika
od 2,00 %, druga od 2,05 %, a svaka je prikazana pola milijuna puta. Podaci
ispod su konstruirani za ovu svrhu i nisu nalaz ni o kojoj stvarnoj kampanji.

U simuliranom pokusu prva je naslovnica postigla `r hr_broj(s11$ab_a, 3)` %, a
druga `r hr_broj(s11$ab_b, 3)` %. Razlika iznosi
`r hr_broj(s11$ab_razlika, 3)` postotnog boda uz interval od
`r hr_broj(s11$ab_donja, 3)` do `r hr_broj(s11$ab_gornja, 3)`, a p-vrijednost
je `r formatC(s11$ab_p, format = "f", digits = 5, decimal.mark = ",")`. Po
svakom kriteriju iz prethodnog poglavlja rezultat je jasan, jer nulti model
ovakvu razliku gotovo nikada ne proizvodi.

Prevedeno natrag u odluku, dobitak je jedan dodatni klik na otprilike tisuću
prikaza. Isplati li se zbog toga mijenjati naslovnicu, ovisi o trošku promjene i
o tome što jedan klik vrijedi, a ni jedno ni drugo nije u podacima. Statistička
značajnost ovdje govori samo to da je uzorak bio dovoljno velik da razliku ove
veličine odvoji od nule.

Ista logika radi i u suprotnom smjeru. Razlika koja bi promijenila uredničku
odluku može ostati neznačajna ako je uzorak malen, i tada izostanak značajnosti
ne govori o svijetu nego o količini prikupljenih podataka. Zbog toga se
značajnost i važnost izvještavaju odvojeno, i zbog toga procjena s intervalom
uvijek stoji ispred testa.

## Snaga kao svojstvo plana

Vjerojatnost da postupak pronađe učinak koji postoji nije svojstvo testa nego
kombinacije nekoliko odluka, od kojih se većina donosi prije podataka.

**Statistička snaga** je vjerojatnost da postupak odbaci nultu hipotezu kad je
ona lažna, dakle udio ponavljanja u kojima bi učinak zadane veličine bio
otkriven.

Prethodno je poglavlje na ovoj populaciji izmjerilo da postupak stvarnu razliku
pronalazi u otprilike četiri od pet uzoraka od tristo osoba. Ta brojka upravo je
snaga, i sada je vrijedi izmjeriti na više veličina uzorka.

*Slika. Udio uzoraka u kojima permutacijski postupak prelazi prag od 0,05 pri stvarnoj razlici od 0,74 boda. Tristo simuliranih studija po retku. Izrada autora.*

Rast nije ravnomjeran i to je najvažnije u tablici. Podizanje uzorka sa
šezdeset na tristo osoba snagu diže s `r hr_broj(s11$snaga_60, 1)` % na
`r hr_broj(s11$snaga_300, 1)` %, a svako daljnje ulaganje kupuje sve manje, jer
je udio ograničen odozgo. Studija sa šezdeset osoba nije upola lošija od studije
s tristo, nego je gotovo beskorisna za ovo pitanje.

Četiri stvari određuju gdje se na toj krivulji nalazimo. Veći stvarni učinak
lakše se otkriva, veći uzorak daje precizniju procjenu, manja raspršenost ishoda
čisti signal, a blaži prag propušta više rezultata. Prve dvije obično su jedine
koje istraživač može mijenjati, i samo je druga u njegovim rukama nakon što je
pitanje postavljeno.

Konvencija traži barem 80 %, i kao svaka konvencija služi kao polazište, a ne
kao dokaz. Ako propuštena razlika nosi ozbiljnu posljedicu, osamdeset posto je
premalo, a ako je istraživanje prvo u nizu i služi kao provjera izvedivosti,
može biti previše.

## Interakcija — Istraživač snage

Sljedeći prikaz odvaja tri odluke koje se u praksi donose zajedno. Čitatelj
mijenja stvarnu veličinu učinka, broj jedinica i prag, svaki put samo jedno, i
prati kako se pomiče udio uzoraka u kojima bi postupak nešto našao.

*Slika. Simulirana snaga kroz veličine uzorka u idealiziranom postupku s poznatom varijabilnošću.*

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Spustite prag odluke i provjerite koliko je jedinica potrebno za istu snagu.
4. Postavite standardiziranu razliku na 0,10 i pokušajte dosegnuti 80 %.

Posljednji korak ne uspijeva unutar ponuđenog raspona, i to je poanta. Za male
učinke potreban uzorak raste brže nego što većina istraživanja može podnijeti,
pa odluka o tome koji je učinak vrijedan traženja mora doći prije odluke o
uzorku.

## Podsnažene studije pretjeruju

Uobičajena pouka o slaboj snazi glasi da se stvarni učinci propuštaju. To je
točno, a nije najgori dio. Studija sa slabom snagom kvari i one nalaze koje
proizvede, i to se na poznatoj populaciji može izmjeriti.

Ponovili smo isto pitanje na tri tisuće studija sa šezdeset osoba. Prosjek svih
procjena iznosi `r hr_broj(s11$prosjek_svih, 2)` boda i praktički se poklapa sa
stvarnom razlikom od `r hr_broj(s11$razlika, 2)`, dakle postupak sam po sebi
nije pristran.

*Slika. Procijenjena razlika u tri tisuće studija sa šezdeset osoba, sve zajedno i samo one koje su prešle prag. Okomita crta označuje stvarnu razliku u populaciji.*

Donji panel prikazuje ono što bi se objavilo. Među studijama koje su prešle prag
prosječna procjena iznosi `r hr_broj(s11$prosjek_znacajnih, 2)` boda, dakle
`r hr_broj(s11$faktor, 1)` puta više od istine. Razlog je mehanički i nema veze
s poštenjem istraživača. Uz slabu snagu prag prelaze samo uzorci u kojima je
slučajnost razliku slučajno uvećala, jer manja procjena s ovako malim uzorkom
prag ne može prijeći. Najmanja značajna procjena u ovoj simulaciji iznosi
`r hr_broj(s11$najmanja_znacajna, 2)` boda.

Drugi smjer rjeđi je, ali nije nemoguć. Među značajnim nalazima
`r hr_broj(s11$krivi_predznak, 2)` % ima suprotan predznak od stvarne razlike,
dakle tvrdi da čitatelji portala imaju više povjerenja. Takav bi rad prošao
recenziju jednako lako kao svaki drugi, jer je iznutra besprijekoran.

Ista simulacija s pet stotina osoba daje procjene koje istinu premašuju za
faktor `r hr_broj(s11$faktor_veliki, 2)`, dakle iskrivljenja praktički nema.
Pretjerivanje nije svojstvo područja ni teme, nego posljedica toga što se prag
primjenjuje na procjene koje su preraspršene za veličinu učinka koji se traži.

Za čitatelja objavljenih radova iz toga slijedi konkretan postupak. Kad rad na
malom uzorku izvještava o velikom učinku uz p-vrijednost tik ispod praga,
najvjerojatnije objašnjenje nije da je učinak zaista tolik nego da je uzorak
propustio samo one procjene koje su slučajno ispale velike. Interval to obično
odaje, jer se u takvim radovima proteže od jedva zamjetne do nevjerojatno velike
vrijednosti. Zato se prvo gleda koliko je jedinica bilo i koliko je interval
širok, a tek onda što piše u zaključku.

## Planiranje unatrag

Iz svega prethodnog slijedi da uzorak nije stvar raspoloživosti nego odluke, i
da ta odluka počinje na kraju.

**Najmanji važan učinak** je najmanja razlika koja bi promijenila zaključak,
odluku ili postupanje, određena sadržajno i prije prikupljanja podataka.

Postavlja ga istraživač, a ne račun, i obrazlaže se troškom postupanja,
ozbiljnošću ishoda i onim što je u istom području već izmjereno. Tek kad je
zapisan, pitanje o veličini uzorka ima odgovor, jer se snaga uvijek računa za
neku određenu veličinu učinka.

Redoslijed je time obrnut od uobičajenog. Ne pita se koliko se ispitanika može
prikupiti pa se nada da će biti dovoljno, nego se kreće od razlike koja bi nešto
značila, dodaje se željena snaga, i iz toga izlazi broj jedinica. Ako je taj broj
neizvediv, to je nalaz sam po sebi i treba ga znati prije istraživanja, a ne
poslije.

Postoji i drugi način planiranja, bliži načelu po kojem je ova knjiga napisana.
Umjesto da se pita koliko je jedinica potrebno da bi se prešao prag, pita se
koliko ih je potrebno da bi procjena bila dovoljno precizna. Uz raspršenost iz
ove populacije interval razlike širok je `r hr_broj(s11$sirina_100, 2)` boda pri
stotinu ljudi po skupini, `r hr_broj(s11$sirina_300, 2)` pri tristo i
`r hr_broj(s11$sirina_800, 2)` pri osamsto. Istraživač koji zna da mu je za
odluku potrebna procjena unutar pola boda odatle čita odgovor izravno, bez
ijedne pretpostavke o tome koliki je stvarni učinak.

Ta je razlika u pristupu važnija nego što izgleda. Planiranje prema snazi
zahtijeva da se pogodi veličina učinka koji se traži, a upravo je ta veličina
ono što se ne zna i zbog čega se istraživanje provodi. Planiranje prema
preciznosti tu pretpostavku ne treba, jer širina intervala ovisi samo o
raspršenosti i broju jedinica. Studija planirana na taj način ne obećava da će
nešto naći, nego da će, što god nađe, biti dovoljno precizno da se o tome može
odlučivati.

## Razrađeni primjer

Pretpostavimo da bi uredništvo reagiralo na razliku od pola boda i da očekuje
raspršenost sličnu onoj u ovoj populaciji. Analiza ispod za nekoliko veličina
uzorka broji u kolikom udjelu simuliranih studija bi takva razlika bila
otkrivena.

Funkcija `replicate` ponavlja cijelu zamišljenu studiju dvije tisuće puta, a
`sapply` isti račun provodi za svaku ponuđenu veličinu uzorka. Granica 1,96
dolazi iz pravila područja koje uvodi poglavlje o vjerojatnosti, pa se ovdje
ništa novo ne pretpostavlja.

*Slika. Udio simuliranih studija u kojima bi razlika od pola boda bila otkrivena, pri četirima veličinama uzorka po skupini. Izrada autora.*

Za razliku od pola boda treba između dvjesto i dvjesto pedeset ljudi po skupini
da bi se dosegla uobičajena granica od osamdeset posto. Ako uredništvo može
prikupiti stotinu, plan je i dalje moguć, ali izvještaj mora unaprijed reći da
će studija razliku te veličine propustiti u više od polovice slučajeva.

Račun ne odlučuje ništa od onoga što je važno. Pola boda kao granicu postavio je
netko tko zna što se s tom razlikom radi, raspršenost je procijenjena iz ranijih
mjerenja, a odustajanje ispitanika i kvaliteta mjerenja nisu ni ušli u simulaciju.
Ono što račun daje jest jedini pošten oblik rečenice o uzorku, u kojem broj
jedinica stoji uz učinak koji se njime može uočiti.

**Statistika u divljini.**
**Neuspjeh snage.** Skupina istraživača objavila je pregled u kojem tvrdi da je
prosječna statistička snaga studija u neuroznanosti vrlo niska, i da posljedice
toga uključuju precijenjene veličine učinka i slabu ponovljivost rezultata
(Button, 2013). Rad je naslovljen kao neuspjeh snage i čitan je najčešće kao
poziv na veće uzorke.

Ono što se u tom čitanju gubi jest drugi dio tvrdnje. Niska snaga ne smanjuje
samo izglede da se pravi učinak pronađe, nego smanjuje i vjerojatnost da
statistički značajan nalaz odgovara stvarnom učinku. To je ista mehanika koju
simulacija u prethodnom odjeljku mjeri, gdje su procjene koje su prešle prag u
prosjeku dvostruko veće od istine. Iz toga slijedi da podsnaženo područje ne
proizvodi samo manje nalaza nego i lošije, pa preporuka nije čitati takve radove
opreznije, nego ne vjerovati veličini učinka koju objavljuju.

**Pitajte model.**
Asistent pouzdano izračuna standardiziranu razliku i provede analizu snage, a
sam ne zna ono što u nju ulazi. Prije poziva mu treba dizajn, očekivana
raspršenost ishoda i najmanji učinak koji bi nešto značio, jer bez posljednjega
snaga nema referencu. Provjeravamo tri stvari. Prva je koristi li nazivnik koji
odgovara dizajnu, budući da se kod uparenih mjerenja dijeli standardnom
devijacijom razlika. Druga je uzima li konvencionalne pragove kao sadržajnu
činjenicu i naziva li učinak malim prije nego što je pitao o čemu se radi. Treća
je računa li snagu iz učinka koji je već opažen, što je najčešća i najskuplja
pogreška u ovom području.

> Reci mi koji ulaz nedostaje prije nego što izračunaš snagu. Zatim izračunaj
> potreban uzorak za nekoliko veličina učinka i pokaži koliko se odgovor mijenja
> ako je stvarni učinak upola manji od pretpostavljenog.

**Nađite grešku.**
Nakon male studije s tridesetero ljudi po skupini asistent je uz nalaz priložio
i ovu provjeru.

Uz ispis je dodao obrazloženje. Opažena razlika daje standardiziranu razliku
oko 0,78, a snaga izračunata za tu vrijednost i trideset ljudi po skupini iznosi
0,84. Budući da je snaga iznad uobičajene granice, zaključuje da je studija
bila dovoljno velika i da se procijenjenoj razlici može vjerovati.

Greška je računanje snage iz učinka koji je već opažen. Poziv je sintaktički
ispravan, ali je `delta` popunjena procjenom iz istih podataka, pa rezultat ne
donosi nikakvu novu informaciju i uvijek ispada visok kad je nalaz značajan.
Simulacija u ovom poglavlju pokazuje i zašto je zaključak obrnut od istine, jer
prag pri maloj studiji prelaze upravo pretjerane procjene. Snaga se računa iz
najmanjeg važnog učinka, postavljenog prije podataka, i tada bi za razliku ove
veličine tražila znatno više od trideset ljudi po skupini.

## Sažetak

Veličina učinka vraća pitanju koliko je razlika velika, a standardizirana mjera
čini je usporedivom preko različitih ljestvica. Statistička značajnost i
praktična važnost odgovaraju na različita pitanja, pa golem uzorak proizvodi
značajnost za razlike koje nikoga ne zanimaju, dok premali uzorak propušta one
koje bi promijenile odluku. Snaga povezuje učinak, uzorak, raspršenost i prag, a
mjerenje na poznatoj populaciji pokazuje koliko brzo pada kad uzorak popusti.
Studije sa slabom snagom pritom ne griješe samo propuštanjem, jer među njihovim
objavljenim nalazima procjene su u prosjeku dvostruko veće od istine, a poneka
ima i pogrešan predznak. Sljedeće poglavlje pokazuje što se događa kada sustav
nagrađuje objavljeni nalaz, a skriva cijeli put koji je do njega doveo.

## Pojmovi

veličina učinka (*effect size*), standardizirana razlika (*Cohen's d*),
praktična važnost (*practical significance*), statistička snaga (*statistical
power*), najmanji važan učinak (*smallest effect size of interest*), planiranje
uzorka (*sample size planning*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto među objavljenim nalazima podsnaženih studija
procjene učinka sustavno premašuju istinu, iako nijedan pojedinačni istraživač
nije napravio ništa nedopušteno. Imenujte korak u kojem nastaje iskrivljenje.

### Računski

Dvije skupine imaju sredine 5,4 i 4,6 uz združenu standardnu devijaciju 1,9.
Izračunajte razliku i standardiziranu razliku, a zatim ponovite račun uz
združenu standardnu devijaciju 3,8. Objasnite koja se od dviju brojki promijenila
i zašto. Zatim u widgetu poglavlja pronađite koliko je jedinica po skupini
potrebno da se manja od dviju standardiziranih razlika otkrije u četiri od pet
pokušaja.

### Kritički

Prosudite tvrdnju da niska prosječna snaga nekog područja znači samo da
istraživanja propuštaju stvarne učinke (Button, 2013). Predajte kratku uredničku
bilješku i navedite podatak koji bi vam trebao da procijenite koliko je
objavljena veličina učinka precijenjena.

### Revizija modela

Ocijenite provjeru iz okvira o pogrešci. Imenujte što je u pozivu ispravno,
argument u kojem stoji kružnost, redak koda u kojem ona ulazi u račun, i
napišite čime bi taj argument trebalo zamijeniti.

---

# Kriza i obnova

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/12-kriza-i-obnova.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 6 min | Pješčanik p-hakiranja | simulacija | pogl. 10, 11 |

**Vinjeta.**
Velika suradnja istraživača pokušala je ponoviti niz objavljenih psiholoških
studija prema zajedničkom protokolu. Replikacijski rezultati u cjelini bili su
slabiji od slike koju je ostavljala izvorna literatura (Collaboration}, 2015). Rasprava
koja je slijedila nije se mogla svesti na podjelu između dobrih i loših
istraživača.

Objavljivanje je dugo nagrađivalo nov, jasan i statistički značajan rezultat.
Istraživači su istodobno donosili mnogo odluka o uzorku, ishodima, podskupinama
i modelima. Čak i bez svjesne prevare, fleksibilan put kroz podatke mogao je
završiti pričom koja izgleda unaprijed planirana (Simmons, 2011; Gelman, 2013).

Kako znanstveni sustav može učiniti vlastite rezultate provjerljivijima bez
pretvaranja skepticizma u cinizam?

## Putovi koji ostaju nevidljivi

P-hakiranje obuhvaća prilagođavanje analize sve dok se ne pojavi poželjan
rezultat. Može uključivati promjenu ishoda, pravila isključivanja, trenutka
zaustavljanja ili skupa kontrolnih varijabli. Svaka odluka može imati razumno
obrazloženje, ali njihova kombinacija mijenja vjerojatnost konačnog nalaza
(Simmons, 2011).

Vrt račvajućih putova širi problem. Istraživač ne mora isprobati deset analiza
i sakriti devet. Podaci mogu usmjeriti jednu odabranu analizu kroz niz odluka
koje bi bile drukčije da su podaci izgledali drukčije (Gelman, 2013). Konačni
tekst pokazuje samo put kojim se prošlo, ne sve putove koji su bili mogući.

Publikacijska pristranost zatim djeluje na razini literature. Rezultati koji
izgledaju jasni i novi lakše postaju vidljivi, dok neodređeni i neuspjeli
pokušaji ostaju u ladicama. Metaanaliza tada može precizno sažeti odabrani dio
istraživačkog zapisa i dati varljiv osjećaj stabilnosti.

## Reforma kao promjena postupka

Predregistracija vremenski odvaja plan od ishoda. Ona ne jamči dobar plan ni
istinito mjerenje, ali čitatelju pokazuje koje su odluke donesene prije gledanja
podataka. Registrirani izvještaj ide dalje jer se pitanje i metoda vrednuju
prije nego što je rezultat poznat.

Otvoreni podaci, materijali i kod omogućuju provjeru i ponavljanje. Otvorenost
ne uklanja etičke i privatnosne granice. Podaci o ljudima ne postaju sigurni
samim objavljivanjem, pa transparentnost mora uključiti razloge zbog kojih neki
materijali ne mogu biti javni.

Replikacija nije glasanje o tome je li izvorni autor bio u pravu. Rezultati se
mogu razlikovati zbog uzoračke varijacije, konteksta, mjerenja ili stvarne
heterogenosti učinka. Obnova zato traži kumulativno čitanje procjena i uvjeta,
a ne zamjenu jednog spektakularnog nalaza drugim.

## Asistent u dvostrukoj ulozi

Generativni modeli mogu ubrzati izradu koda, provjeru tablica i usporedbu
izvještaja s analizom. Isti kapacitet može proizvoditi uvjerljive izvore koji ne
postoje, sintetičke rukopise i velik broj varijanti iste tvrdnje. Brzina
pojačava i provjeru i proizvodnju šuma.

Disciplina rada s asistentom zato mora ostaviti trag. Čuvamo ulazne podatke,
upit, kod, verziju alata i ručnu provjeru. Model ne dobiva osjetljive
ispitanikove podatke, a njegov tekst ne postaje izvor. Izvor ostaje publikacija,
skup podataka ili reproducibilan postupak koji se može otvoriti bez modela.

## Interakcija — Pješčanik p-hakiranja

Pješčanik omogućuje biranje ishoda, podskupina i trenutka zaustavljanja na
podacima bez stvarnog učinka. Čitatelj promatra kako rast broja odluka povećava
priliku za privlačan rezultat i kako korekcija za cijeli postupak mijenja sliku.
Radi preglednosti svaki je analitički put u simulaciji neovisan. Stvarni putovi
često dijele podatke, ali idealizacija izdvaja cijenu njihova broja.

*Slika. Udio simuliranih istraživanja s barem jednim rezultatom ispod odabranog praga nakon pretraživanja više neovisnih analitičkih putova.*

**Što isprobati.**

1. Provedite jednu unaprijed određenu analizu.
2. Dodajte ishode, a podskupine i trenutke provjere ostavite jednakima.
3. Dodajte podskupinske inačice i trenutke provjere bez promjene broja ishoda.
4. Usporedite nominalni prag 0,05 s pragom korigiranim za sve putove.

Najmanja p-vrijednost nije sažetak jedne unaprijed određene analize kada je
nastala pretraživanjem. Zaključak tada mora opisati cijeli skup mogućnosti ili
koristiti postupak koji njihov broj uzima u obzir.

**Statistika u divljini.**
**Replikacija kao zajedničko mjerenje.** Open Science Collaboration koristio je
zajednički postupak za procjenu reproducibilnosti niza psiholoških nalaza
(Collaboration}, 2015). Rezultat nije jednostavna stopa istine jer se izvorne i replikacijske
studije razlikuju u preciznosti, kontekstu i mogućim učincima.

Vrijednost projekta leži i u tome što je privatni problem pojedinačnih sumnji
pretvorio u podatke o sustavu. Čitatelj može procjenjivati obrasce bez
pretpostavke da svaki neuspjeh ima isti uzrok.

**Pitajte model.**
Asistent može usporediti registrirani plan, kod i rukopis te označiti
neslaganja. Ne smije izmišljati nedostajuće datoteke ni procjenjivati
reproducibilnost samo prema tonu teksta. Svaki nalaz mora imati put do retka
koda, tablice ili dokumenta.

> Usporedi istraživački plan, analitički kod i izvještaj. Navedi svako
> odstupanje s točnim mjestom u dokumentima i odvoji potvrđene razlike od
> informacija koje nedostaju.

**Nađite grešku.**
Studija je predregistrirala ishod, pravilo isključivanja i model prije
prikupljanja podataka. Kod i anonimizirani materijali dostupni su za provjeru.
Zbog predregistracije rezultat mora biti istinit.

Greška je pretvaranje predregistracije u jamstvo istine. Ona povećava
vidljivost analitičkih odluka, ali ne uklanja pogrešku mjerenja, uzoračku
varijaciju, slabu teoriju ni neprikladan model.

## Razrađeni primjer

Simuliramo podatke bez stvarne grupne razlike, ali s više mogućih ishoda.
Analitičar koji prijavi samo najmanju p-vrijednost prikazuje rezultat jedne
odabrane analize, dok je stvarni postupak uključivao mnogo prilika
(Simmons, 2011).

*Slika. Najmanja p-vrijednost među simuliranim ishodima bez učinka. Izrada autora prema @simmons2011.*

Tablica je jedna realizacija simulacije i ne mora svaki put sadržavati
privlačan rezultat. Upravo je to poanta. Kada se cijeli postupak ponavlja,
neki će nizovi ponuditi malu p-vrijednost bez učinka. Predregistracija,
izvještavanje svih ishoda i korekcija za višestrukost čine tu priliku vidljivom.

Reforma ne traži da prestanemo istraživati neočekivane obrasce. Traži da
razlikujemo potvrđujuću analizu od naknadnog istraživanja i da novu hipotezu
predstavimo kao početak sljedeće provjere.

## Sažetak

Kriza reproducibilnosti nastaje iz spoja uzoračke varijacije, analitičke
fleksibilnosti i poticaja koji nagrađuju jasan pozitivan nalaz. Predregistracija,
registrirani izvještaji i otvoreni materijali povećavaju vidljivost postupka, ali
ne jamče istinu. Replikacija procjenjuje stabilnost nalaza kroz nove podatke i
uvjete. Asistent može pomoći u provjeri samo kada njegov rad ostaje
reproducibilan, provjerljiv i odvojen od izvora.

## Pojmovi

p-hakiranje (*p-hacking*), vrt račvajućih putova (*garden of forking paths*),
publikacijska pristranost (*publication bias*), predregistracija
(*preregistration*), registrirani izvještaj (*registered report*), replikacija
(*replication*), otvorena znanost (*open science*)

## Zadaci

### Konceptualni

Razlikujte p-hakiranje od vrta račvajućih putova. Predajte dva kratka scenarija
koja pokazuju razliku (Simmons, 2011; Gelman, 2013).

### Računski

Ponovite simulaciju `sim_putovi` mnogo puta i predajte raspodjelu najmanjih
p-vrijednosti.

### Kritički

Prosudite što veliki replikacijski projekt može reći o literaturi, a što ne
može o svakoj pojedinačnoj studiji (Collaboration}, 2015). Predajte dva odlomka.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dvije dobre prakse, jednu
pretjeranu tvrdnju i ograničenje koje ostaje nakon predregistracije.
