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
