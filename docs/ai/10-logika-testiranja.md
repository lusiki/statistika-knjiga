# Logika testiranja

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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

Nulti model za ovo pitanje tvrdi da je cijela raspodjela povjerenja jednaka
među čitateljima tiska i portala. Kad bi to vrijedilo, oznake izvora bile bi
zamjenjive u odnosu na ishod i mogle bi se rasporediti drukčije bez promjene
zajedničke raspodjele. Promiješamo ih stoga nasumično, izračunamo razliku
sredina i postupak ponovimo mnogo puta. Dobiveni raspon razlika pokazuje što
takav nulti model dopušta.

Ta zamjenjivost nije dana samim podatkom da su sredine jednake. Skupine s
jednakim sredinama, ali različitim rasponima ili oblicima raspodjele ne
zadovoljavaju ovaj nulti model. Postupak uz to pretpostavlja da su osobe
zasebne, međusobno neovisne jedinice opažanja. Budući da izvor vijesti nije
nasumično dodijeljen, zamjenjivost je ovdje pretpostavka modela, a ne posljedica
istraživačkog dizajna, i test ne može poduprijeti uzročnu tvrdnju.

**Testna statistika** je jedan broj izračunat iz podataka koji sažima odstupanje
od nultog modela u obliku usporedivom s odstupanjima koja taj model proizvodi.

Ovdje je testna statistika sirova razlika sredina. Obostrani postupak uspoređuje
apsolutnu opaženu razliku s apsolutnim razlikama nakon premještanja, pa jednako
broji odstupanja u oba smjera. Takva statistika u sirovoj permutaciji ispituje
upravo opisani nulti model cijele raspodjele, a ne samo jednakost sredina.
Sljedeći graf prikazuje što nulti model s njome radi kroz četiri tisuće
premještanja, a uz njega stoji razlika koju je dao stvarni raspored oznaka.

*Slika. Razlike sredina kroz četiri tisuće nasumičnih premještanja oznaka skupine, uz okomitu crtu na razlici opaženoj u uzorku.*

Nulta raspodjela ima sredinu u nuli i standardnu devijaciju od
`r hr_broj(s10$sd_nulte, 2)` boda. Devedeset pet posto premještanja daje razliku
koja po apsolutnoj vrijednosti nije veća od `r hr_broj(s10$granica, 2)` boda,
pa nulti model cijeli taj raspon proizvodi bez ikakve pomoći. Opažena razlika od
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

Kad bismo pobrojili sva moguća premještanja, p-vrijednost bi bila njihov točan
udio, uključujući opaženi raspored. Ovdje nasumično izvlačimo konačan broj
premještanja. Označimo li njihov broj s $B$, a broj apsolutnih razlika barem
toliko velikih kao opažena s $b$, procijenjena p-vrijednost iznosi
$(b + 1)/(B + 1)$. Dodani
opaženi raspored sprečava da konačna simulacija vrati nulu i daje valjanu
procjenu pri nasumičnom uzorkovanju premještanja.

## Interakcija — Simulator p-vrijednosti

Sljedeći prikaz radi ono što jedan uzorak ne može. Postupak ponavlja mnogo puta,
odvojeno u svijetu u kojem učinka nema i u svijetu u kojem ga ima, i prikazuje
kako se p-vrijednosti raspoređuju u jednom i u drugom. Radi preglednosti koristi
normalne ishode s poznatom varijabilnošću i obostrani test. P-vrijednosti računa
iz poznate normalne raspodjele, pa korekcija za konačan broj nasumičnih
premještanja ne pripada ni interaktivnom prikazu ni njegovoj statičnoj inačici.

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

**Pogreška prve vrste** je odbacivanje nulte hipoteze koja je istinita. Pod
pretpostavkama modela postupak ograničava dugoročni udio takvih odbacivanja
odabranim pragom.

Ta se tvrdnja može izmjeriti u uvjetima u kojima znamo da vrijedi cijeli nulti
model. Iz poznate populacije svaki put izvučemo `r s10$n` ishoda, a zatim im
nasumično dodijelimo jednako mnogo oznaka A i B. Oznaka nastaje neovisno o
ishodu, pa je puna raspodjela povjerenja pod nultom hipotezom ista u objema
skupinama po konstrukciji, a ne samo približno jednaka po sredini.

Provedemo li permutacijski postupak na osamsto tako nastalih uzoraka, prag od
0,05 prijeđe ih `r hr_broj(s10$stopa_nulta, 1)` %. Konačan broj premještanja i
slučajnost među osamsto ponavljanja znače da izmjereni udio ne mora biti točno
pet posto. Bitno je da se provjerava postupak pod nultim modelom koji doista
zadovoljava njegovu pretpostavku zamjenjivosti.

*Slika. Udio uzoraka u kojima permutacijski postupak prelazi prag od 0,05, za dva pitanja s poznatim odgovorom. Osamsto uzoraka po pitanju, u svakome tristo premještanja. Izrada autora.*

Drugi redak tablice nosi drugu vrstu pogreške. Razlika po izvoru vijesti u
populaciji doista postoji i iznosi `r hr_broj(s10$istina_izvor, 2)` boda, a
postupak je pronalazi u `r hr_broj(s10$stopa_izvor, 1)` % uzoraka. U preostalih
`r hr_broj(s10$promasaj, 1)` % istraživač bi zaključio da nema dovoljno dokaza,
i pritom bi se pridržavao svih pravila.

*Slika. Geometrija dviju pogrešaka — uvjetna nulta raspodjela iz glavnog uzorka i raspodjela procijenjene razlike kroz uzorke kad učinak postoji. Isprekidane crte prikazuju granične vrijednosti glavnog uzorka, pa plohe ne prikazuju stope iz tablice.*

Slika pokazuje zašto se pomicanjem istih graničnih crta jedna pogreška ne može
smanjiti bez povećanja druge. Crte su određene gornjom raspodjelom, a odsijecaju
i donju. Pomaknemo li ih
prema van kako bismo rjeđe pogriješili na prvi način, veći dio donje raspodjele
ostaje između njih i postupak češće promašuje stvarnu razliku. Veći uzorak ili
preciznije mjerenje pri istom pragu smanjuju pogrešku druge vrste, dok pogreška
prve vrste ostaje ograničena odabranim pragom. Više informacija može omogućiti
i stroži prag uz zadržanu ili veću snagu, ali samo nakon nove odluke o odnosu
dviju pogrešaka.

Plohe na slici objašnjavaju geometriju tog odnosa, a ne predstavljaju izmjerene
stope iz tablice, jer gornja raspodjela uvjetuje na glavni uzorak, dok donja
dolazi iz ponovljenih uzoraka. Stvarna snaga ovisi zajedno o veličini učinka,
varijabilnosti, veličini i dizajnu uzorka, testnoj statistici i pragu odluke.
Kako se te sastavnice planiraju unaprijed, tema je sljedećeg poglavlja.

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

Vratimo se kalibracijskom uzorku s nasumično dodijeljenim oznakama. Razlika
iznosi `r hr_broj(s10$razlika_nulta, 2)` boda uz interval od
`r hr_broj(s10$donja_nulta, 2)` do `r hr_broj(s10$gornja_nulta, 2)`, a
p-vrijednost je `r hr_broj(s10$p_nulta, 2)`. Oznaka je nastala neovisno o
ishodu, pa ovdje znamo da nulti model vrijedi.

Izvještaj koji bi iz toga zaključio da razlike nema rekao bi ipak previše.
Interval i dalje dopušta razlike u oba smjera koje bi mogle biti sadržajno
važne u drugom istraživačkom pitanju. Velika p-vrijednost znači da podaci nisu
neusklađeni s nultim modelom, a ne da su s njime posebno usklađeni.

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

Istraživače često zanima koliko je nakon podataka vjerojatna određena veličina
učinka. Postupak iz ovog poglavlja na to pitanje ne odgovara i nije za njega ni
napravljen. Njegovo je legitimno pitanje kako bi se unaprijed određen postupak
ponašao kroz ponavljanja kad vrijedi precizan nulti model. Takav model može biti
sadržajno važan kad upravo odsutnost razlike ili određena referentna vrijednost
ima značenje za odluku.

Bayesovski pristup raspodjelu uvjerenja prije podataka povezuje s modelom koji
opisuje koliko su podaci vjerojatni pri različitim vrijednostima učinka. Rezultat
je nova raspodjela vjerojatnosti nad mogućim učincima. Iz nje se može očitati
vjerojatnost da je učinak veći od nule ili od sadržajno važne granice, što je
drukčije pitanje od dugoročnog ponašanja testa.

Oba pristupa ovise o pretpostavkama koje treba izgovoriti. Bayesovski zaključak
može se promijeniti s početnom raspodjelom i s modelom podataka, pa osjetljivost
na oba izbora pripada izvještaju. Frekvencijski zaključak ovisi o modelu
uzorkovanja ili dodjele, testnoj statistici i unaprijed zadanom postupku. Razlika
među pristupima nije u tome ima li pretpostavki, nego koja pitanja postavljaju i
kako provjeravaju posljedice svojih izbora.

Knjiga ostaje na frekvencijskom putu jer je to jezik kojim je napisana golema
većina istraživanja koja čitatelj mora znati pročitati. Bayesovski račun ovdje
ostaje pogled kroz prozor, a procjena veličine učinka i njezina neizvjesnost i
dalje vode izvještaj u oba jezika. Poglavlje o regresiji na tu razliku vraća se
u zaključnom pogledu unaprijed.

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

Uz ispis je dodao obrazloženje. Osobe su zasebne jedinice opažanja, a nulti
model pretpostavlja jednaku punu raspodjelu povjerenja u objema skupinama, zbog
čega se oznake smatraju zamjenjivima. Oznake su promatračke, pa rezultat ne
podupire uzročnu tvrdnju. Premještene su četiri tisuće puta, a korigirana
p-vrijednost iznosi `r hr_broj(s10$p, 3)`. Budući da je ispod praga, zaključuje
da vjerojatnost da između dviju skupina nema razlike iznosi
`r hr_broj(s10$p * 100, 1)` %.

## Razrađeni primjer

Cijeli se postupak može ispisati u nekoliko redaka, i vrijedi ga jednom vidjeti
u cjelini. Analiza najprije računa opaženu razliku, zatim gradi nultu raspodjelu
premještanjem oznaka, i na kraju prebrojava koliko je premještanja dalo barem
toliko veliko odstupanje.

Funkcija `sample` bez dodatnih argumenata vraća isti niz oznaka u nasumičnom
poretku, a `replicate` ponavlja izraz zadani broj puta i skuplja rezultate. Cijeli
nulti model stane u te dvije funkcije i ne zadaje parametarski oblik raspodjele.
Njegova valjanost ipak počiva na neovisnim jedinicama i zamjenjivosti oznaka pod
nultim modelom pune raspodjele. Brojanje u oba repa čini postupak obostranim, a
dodavanje jedinice u brojnik i nazivnik ispravlja procjenu za konačan nasumični
skup premještanja.

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
pomicanje praga jednu smanjuje, a drugu povećava, dok više informacija pri istom
pragu smanjuje pogrešku druge vrste. Kalibracijska simulacija s nasumično
dodijeljenim oznakama provjerila je prag pod istinitim nultim modelom pune
raspodjele, dok je postupak stvarnu razliku od
`r hr_broj(s10$istina_izvor, 2)` boda propustio u
`r hr_broj(s10$promasaj, 1)` % uzoraka. Sljedeće poglavlje stavlja veličinu
učinka i snagu ispred rituala značajnosti.

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
