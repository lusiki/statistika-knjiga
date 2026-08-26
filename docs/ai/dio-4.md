# DIO IV: ZAKLJUČIVANJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Logika testiranja

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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

Prije nego što se pokrene test, izvještaj treba pokazati koliko je opažena
razlika velika i koliko je neizvjesna. Treba postaviti i drugo pitanje. Što bi u
stvarnoj odluci bilo skuplje, proglasiti razliku koje nema ili propustiti onu
koja postoji? Račun bez veličine i posljedica lako postane obred oko jednoga
praga.

Tek tada počinje testiranje, pretpostavkom u koju nitko ne mora vjerovati.
Postupak najprije opisuje svijet u kojem učinka koji tražimo nema, izračuna što
bi taj svijet proizvodio i tek onda gleda podatke. Ako podaci u takvom svijetu
izgledaju neobično, početna pretpostavka postaje teško održiva.

Analogija sa suđenjem tu asimetriju objašnjava bolje od bilo koje formule. Sud
polazi od pretpostavke nevinosti, a tužiteljstvo iznosi dokaze protiv nje.
Presuda kojom optužba nije dokazana nije utvrđenje nevinosti nego izjava da
dokazi nisu bili dovoljni. Statistički postupak radi isto. Neuspjeh da se
početna pretpostavka odbaci ne znači da je ona utvrđena kao istinita.

Analogija ima i granicu koju vrijedi navesti odmah. Sud presuđuje o jednom
događaju, a test opisuje ponašanje postupka kroz mnogo ponavljanja. Sve što
slijedi vrijedi za postupak, a ne za pojedini rezultat, i upravo se to u
izvještajima gubi.

Zbog toga se dio odluka mora donijeti prije podataka. Početni model treba biti
zapisan tako da se iz njega može računati, mjera odstupanja odabrana, a prag uz
koji će se rezultat čitati postavljen dok se još ne zna kako će podaci ispasti.
Ništa od toga nije tehnička priprema. Postupak čije se komponente biraju nakon
pogleda na podatke više nema stopu pogreške koju obećava, jer je obećanje dano
za postupak koji se svaki put provodi jednako, a ne za onaj koji se dotjeruje.
Koliko se tim putem može doći dokazuje poglavlje o krizi i obnovi.

## Kako se gradi svijet bez učinka

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s10$n` osoba koje se primarno informiraju preko
portala ili preko tiska, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije.

Prvo dolazi ono što odgovara na postavljeno pitanje. Razlika između sredina
iznosi `r hr_broj(s10$razlika, 2)` boda u korist tiska, uz interval pouzdanosti
od `r hr_broj(s10$donja, 2)` do `r hr_broj(s10$gornja, 2)`. Test dolazi tek
poslije, jer odgovara na uže pitanje, na to je li s podacima uskladiva i nula.

Sada privremeno sagradimo svijet u kojem je cijela raspodjela povjerenja jednaka
među čitateljima tiska i portala. U takvu bi svijetu oznake izvora bile
zamjenjive u odnosu na ishod i mogle bi se rasporediti drukčije bez promjene
zajedničke raspodjele. Promiješamo ih nasumično, izračunamo razliku sredina i
postupak ponovimo mnogo puta. Dobiveni raspon razlika pokazuje što svijet bez
veze između oznake i ishoda dopušta.

Tek sada taj izgrađeni svijet treba imenovati.

**Nulta hipoteza** je precizan model postupka koji je proizveo podatke, sastavljen
tako da u njemu nema razlike ni veze koju istražujemo.

Alternativna hipoteza opisuje odstupanje koje bi nas zanimalo i namjerno je
neodređena, jer obuhvaća sve razlike osim nulte. Te dvije tvrdnje nisu
ravnopravne suparnice. Samo je nulta hipoteza ovdje dovoljno precizna da se iz
nje može izračunati što će se dogoditi, i zbog toga testni račun stoji na njoj.

Postupak nasumičnog premještanja oznaka koji smo upravo izgradili zove se
**permutacijski test**.

Zamjenjivost nultoga modela nije dana samim podatkom da su sredine jednake.
Skupine s jednakim sredinama, ali različitim rasponima ili oblicima raspodjele
ne zadovoljavaju ovaj nulti model. Postupak uz to pretpostavlja da su osobe
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
oblik koji vrijedi zapamtiti doslovno. Zadržimo li opažene ishode i veličine
skupina, nulti model daje apsolutnu razliku ovoliku ili veću u otprilike
`r hr_broj(s10$p * 100, 1)` % simuliranih rasporeda oznaka. Sve što p-vrijednost
kaže stoji u toj rečenici, i svaka tvrdnja koja iz nje izlazi mora biti
opravdana posebno.

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
Kontrola standardiziranu razliku izražava u jedinicama standardne devijacije i
ovdje služi samo usporedivom pomicanju učinka. Njezino puno tumačenje pripada
sljedećem poglavlju.

*Slika. Raspodjele p-vrijednosti pod nultim modelom i pod odabranim stvarnim učinkom.*

**Što isprobati.**

1. Postavite stvarnu razliku na nulu i opišite oblik gornje raspodjele.
2. Podignite stvarnu razliku na 0,35 uz nepromijenjen uzorak.
3. Povećajte uzorak bez promjene razlike i usporedite udio rezultata ispod praga.
4. Spustite prag s 0,05 na 0,01 i pogledajte obje raspodjele.

Prvi korak otkriva svojstvo koje nije intuitivno. Kad učinka nema,
p-vrijednosti su ravnomjerno raspoređene po cijelom rasponu od nule do jedinice,
pa je vrijednost od 0,03 pod nultim modelom jednako vjerojatna kao vrijednost od
0,53. Prag ne odvaja obično od neobičnog nego odsijeca unaprijed određen udio te
ravnomjerne raspodjele, i taj udio je sve što prag jamči.

## Dvije vrste pogreške

Odluka može zakazati u oba smjera, a nijedan se rizik ne može ukloniti. Kad se
odbaci nulta hipoteza koja je istinita, radi se o pogrešci prve vrste.
**Pogreška druge vrste** nastaje kad se ne odbaci nulta hipoteza koja je lažna.

**Pogreška prve vrste** je odbacivanje nulte hipoteze koja je istinita. Pod
pretpostavkama modela postupak ograničava dugoročni udio takvih odbacivanja
odabranim pragom.

Zamislimo da istraživački tim mora odlučiti hoće li u izvještaju poduprijeti
tvrdnju da se skupine razlikuju. Pogreška prve vrste ostavila bi čitateljima i
opisanim skupinama neutemeljenu usporedbu. Pogreška druge vrste prešutjela bi
razliku koja u populaciji postoji i mogla bi zaustaviti njezino daljnje
istraživanje. Tim bira prag, ali posljedice ne snosi samo tim, pa izvještaj mora
reći kojoj je pogrešci dao veću težinu i zašto.

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

Sljedeća slika postavlja raspodjelu pod nultim modelom i raspodjelu procijenjene
razlike kad učinak postoji na istu os. Taj je geometrijski prikaz potreban da se
vidi kako iste granične crte povezuju rizike dviju pogrešaka.

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

### Referentna oznaka nije isto što i istina

Simulacija ima povlasticu koju stvarno istraživanje obično nema. Odgovor je
poznat jer smo sami zadali postupak koji stvara podatke. Izvan simulacije
procijenjena stopa pogreške često se računa usporedbom odluke s
**referentnom oznakom**, primjerice ručno dodijeljenom kategorijom. Ta oznaka
nije automatski nepogrešiva. Može ovisiti o mjerenju, uputi osobi koja označava
ili pravilu prema kojem je sporni slučaj razvrstan.

Neslaganje s referentnim oznakama zato može sadržavati i pogreške postupka koji
se ispituje i pogreške same reference. Pošten izvještaj kaže prema kojoj je
referenci stopa procijenjena, kako su oznake nastale i jesu li neslaganja
ponovno pregledana. To kratko ograničenje postat će važno u poglavlju o
algoritmima, gdje velik broj precizno izračunanih pogrešaka ne može neprovjerenu
referencu pretvoriti u istinu.

## Prag je konvencija, a ne mjera

**Prag značajnosti** od 0,05 pojavljuje se u ovom poglavlju kao zadana
vrijednost, a postupak ga ničim ne zahtijeva. Widget dopušta da se pomakne na
0,01 ili na 0,10 i ništa se u računu ne buni, jer prag samo određuje koliki
udio nultog modela pristajemo odsjeći. Odabir je stvar dogovora struke i
posljedica koje pogreška nosi, pa u području u kojem je lažni nalaz skup ima
smisla biti stroži nego u području u kojem je propušten nalaz skuplji.

Iz toga slijedi da razlika između rezultata tik ispod praga i onoga tik iznad
nije razlika u dokazu. Vrijednosti 0,048 i 0,052 gotovo su isti broj, a
izvještaj koji jednu naziva nalazom, a drugu odsutnošću nalaza uvodi razliku
koje u podacima nema. Upravo to je razlog zbog kojeg izjava Američkog
statističkog udruženja traži da znanstveni zaključak ne ovisi samo o tome
prelazi li p-vrijednost određeni prag (Wasserstein, 2016).

U šest je načela izjava vezala p-vrijednost uz neusklađenost podataka s točno
određenim modelom. Odvojila ju je od vjerojatnosti hipoteze, tvrdnje da je nalaz
„nastao slučajno” te veličine ili važnosti učinka. Valjano zaključivanje
povezala je s potpunim izvještavanjem, transparentnošću i drugim znanstvenim
dokazima, a ne s jednim izdvojenim brojem (Wasserstein, 2016).

Razlog za takvu izjavu nije bila nova računska pogreška. Problem je bio običaj
da se prag pretvori u prekidač. Ispod njega rezultat dobiva oznaku
„statistički značajan”, iznad njega gotovo nestaje iz zaključka. Time se gube i
veličina procjene, i njezina neizvjesnost, i cijena pogrešne odluke. Upravo je
tim trima pitanjima ovaj dio knjige započeo.

Izjava nije ukinula p-vrijednost niti je jedan postupak zamijenila drugim.
Promijenila je pravilo njezina čitanja. P-vrijednost može biti dio argumenta,
ali ne smije sama donositi znanstveni zaključak. Za izvještaj u ovom poglavlju
to znači da procjena i interval stoje prvi, pretpostavke su izgovorene, sama
p-vrijednost nije pretvorena u binarnu etiketu, a posljedice obiju pogrešaka
ostaju vidljive.

Drugi se razlog može izravno izmjeriti. Ponovili smo pitanje o izvoru vijesti
na osamsto uzoraka iz iste populacije, u kojoj
razlika stvarno postoji i uvijek je jednaka. U polovici uzoraka p-vrijednost je
bila ispod `r hr_broj(s10$ples_sredina, 3)`, u četvrtini iznad
`r hr_broj(s10$ples_cetvrtina, 3)`, a u desetini iznad
`r hr_broj(s10$ples_gornji, 3)`. Ista populacija, isti postupak i ista veličina
uzorka daju p-vrijednosti raspoređene preko dva reda veličine, pa je u
`r hr_broj(s10$udio_iznad_deset, 1)` % uzoraka rezultat prešao i granicu od 0,10.

P-vrijednost je dakle i sama statistika koja se mijenja od uzorka do uzorka. U
ovoj se simulaciji, pri istoj populaciji, postupku i veličini uzorka, protegnula
preko dva reda veličine. Navođenje triju decimala ne uklanja tu uzorkovnu
promjenjivost. Procjena i njezin interval stoje prvi zato što odgovaraju na
glavno pitanje o veličini razlike i njezinoj neizvjesnosti, a ne zato što su
imuni na promjenu uzorka.

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
nije vjerojatnost da je nalaz „slučajan”. Račun je uvjetovan određenim nultim
modelom i ne pripisuje opaženom rezultatu jedan uzrok. P-vrijednost nije ni
mjera veličine učinka, jer ovisi o uzorku jednako koliko i o razlici, pa dovoljno
velik uzorak proizvodi male vrijednosti i za razlike koje nikoga ne zanimaju.

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

Knjiga ostaje na frekvencijskom putu kao kurikularnom izboru koji povezuje
postupke u sljedećim poglavljima. Bayesovski račun ovdje ostaje pogled kroz
prozor, a procjena veličine učinka i njezina neizvjesnost i dalje vode izvještaj
u oba jezika. Na razliku između tih dvaju pitanja vratit ćemo se uz regresiju, u
kratkom pogledu prema Bayesu.

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
Asistent može provesti test i ispisati p-vrijednost, a pritom preskočiti ono što
računu prethodi ako to upit ne zahtijeva. Prije poziva treba mu reći koja je
jedinica opažanja i što nulti model tvrdi, jer iz tablice ne može zaključiti
smiju li se oznake premještati slobodno. Provjeravamo tri stvari u odgovoru.
Prva je redoslijed, jer procjena i interval moraju stajati ispred testa. Druga
je rečenica kojom tumači p-vrijednost, koja može pogrešno postati vjerojatnost
hipoteze. Treća je zaključak iz velike p-vrijednosti, koji se ne smije pretvoriti
u tvrdnju da razlike nema.

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
`r hr_broj(s10$p * 100, 1)` % simuliranih rasporeda opaženih oznaka. Podaci su
promatrački i ljudi svoj izvor biraju sami, pa razlika opisuje dvije skupine, a
ne učinak čitanja tiska.

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

nulta hipoteza (*null hypothesis*), testna statistika (*test statistic*),
p-vrijednost (*p-value*), pogreška prve vrste (*Type I error*), pogreška druge
vrste (*Type II error*), prag značajnosti (*significance threshold*),
permutacijski test (*permutation test*), referentna oznaka (*reference label*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto p-vrijednost nije vjerojatnost nulte hipoteze,
tako da napišete dvije rečenice koje se razlikuju samo po tome što je uvjet, a
što zaključak. Imenujte podatak koji bi bio potreban da se od prve dođe do
druge.

### Računski

Nulta raspodjela iz ovog poglavlja ima sredinu nula i standardnu devijaciju
`r hr_broj(s10$sd_nulte, 2)` boda. Primijenite pravilo područja iz poglavlja 7
i procijenite granice koje su dvije standardne devijacije udaljene od nule.
Prije računa imenujte testnu statistiku i postupak kojim je nulta raspodjela
izgrađena, pa procjenu usporedite s graničnom vrijednošću
`r hr_broj(s10$granica, 2)`. Zatim
pretpostavite da je isti uzorak prikupljen dobrovoljnom poveznicom na jednom
portalu. Pozivajući se na razliku između slučajnosti uzorkovanja i selekcije iz
poglavlja 8, odredite koju tvrdnju o populaciji ni mala p-vrijednost ne bi
mogla opravdati. Na kraju u HTML widgetu postavite stvarnu razliku na nulu i
zabilježite približan udio uzoraka ispod praga. U tiskanom ili dokumentnom
izdanju očitajte odgovarajući udio iz prvoga retka tablice stopa odbacivanja.

### Kritički

Prosudite zašto je jednom strukovnom udruženju trebalo objaviti izjavu o
pojedinačnom statističkom postupku, a skupini statističara popis od dvadeset pet
pogrešnih tumačenja (Wasserstein, 2016; Greenland, 2016). Predajte kratku
uredničku bilješku i navedite jedno pravilo izvještavanja koje bi uklonilo
najviše pogrešaka odjednom. Dodajte tko u glavnom primjeru snosi posljedice
svake vrste pogreške i zašto procijenjena stopa pogreške prema referentnim
oznakama ne dokazuje da su te oznake nepogrešive.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte korake koji su provedeni
ispravno, redak koda iz kojeg izlazi izvještajna brojka, rečenicu koja iz nje ne
slijedi i njezinu ispravljenu inačicu.

---

# Veličina učinka i snaga

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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
čitatelja tiska i jednog čitatelja portala, prvi ima strogo više povjerenja u
`r hr_broj(s11$nadmoc_stroga, 1)` % parova, dok je
`r hr_broj(s11$izjednaceno, 1)` % parova izjednačeno. Ako se izjednačenja
nasumično razriješe, prilagođena vjerojatnost nadmoći iznosi
`r hr_broj(s11$nadmoc, 1)` %. Kad razlike u raspodjelama ne bi bilo, ta bi mjera
iznosila pedeset posto. Rečenica tog oblika prolazi kroz uredničku raspravu bolje
od bilo koje standardizirane mjere, jer nitko ne mora znati što je standardna
devijacija da bi razumio ishod.

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

Vjerojatnost da postupak pronađe učinak koji postoji nije svojstvo dobivenoga
rezultata. Pripada cijelom planu, koji povezuje postupak, veličinu učinka,
uzorak, raspršenost i prag prije nego što su podaci prikupljeni.

**Statistička snaga** je vjerojatnost da postupak odbaci nultu hipotezu kad je
ona lažna, dakle udio ponavljanja u kojima bi učinak zadane veličine bio
otkriven.

Prethodno je poglavlje na ovoj populaciji izmjerilo da postupak stvarnu razliku
pronalazi u otprilike četiri od pet uzoraka od tristo osoba. Ta brojka upravo je
snaga, i sada je vrijedi izmjeriti na više veličina uzorka.

Mjerenje zadržava permutacijski postupak iz prethodnog poglavlja i njegove
granice. Nulti model tvrdi da je cijela raspodjela povjerenja jednaka u objema
skupinama, tako da su oznake izvora zamjenjive u odnosu na ishod. Obostrana
testna statistika jest apsolutna sirova razlika sredina. Osobe se tretiraju kao
zasebne jedinice bez zajedničke ovisnosti, dok simulacija bez ponavljanja izvlači
uzorke iz jedne konačne simulirane populacije u kojoj razlika po izvoru postoji.
Svaka točka krivulje obuhvaća tristo zamišljenih studija. U svakoj se
p-vrijednost procjenjuje iz dvjesto nasumičnih premještanja uz korekciju
$(b + 1)/(B + 1)$. Pritom $B$ predstavlja broj premještanja, a $b$ broj rezultata
barem toliko ekstremnih kao opaženi. Krivulja zato procjenjuje snagu samo za taj
mehanizam podataka i taj postupak, a ne opće svojstvo uzorka određene veličine.

*Slika. Udio uzoraka u kojima permutacijski postupak prelazi prag od 0,05 pri stvarnoj razlici od 0,74 boda. Tristo simuliranih studija po retku. Izrada autora.*

Rast nije ravnomjeran i to je najvažnije u tablici. Podizanje uzorka sa
šezdeset na tristo osoba snagu diže s `r hr_broj(s11$snaga_60, 1)` % na
`r hr_broj(s11$snaga_300, 1)` %, a svako daljnje ulaganje kupuje sve manje, jer
je udio ograničen odozgo. Pri šezdeset osoba ovaj bi postupak stvarnu razliku
propustio u približno tri od četiri zamišljene studije.

Četiri stvari određuju gdje se na toj krivulji nalazimo. Veći stvarni učinak
lakše se otkriva, veći uzorak daje precizniju procjenu, manja raspršenost ishoda
čisti signal, a blaži prag propušta više rezultata. Plan izravno određuje uzorak
i prag, dok dizajn i kvaliteta mjerenja mogu utjecati na raspršenost. Stvarni
učinak nije upravljačka postavka, nego veličina za koju se snaga mora zasebno
procijeniti.

Uobičajeno polazište od 80 % nije univerzalno pravilo (Cohen, 1988). Ako
propuštena razlika nosi ozbiljnu posljedicu, osamdeset posto može biti premalo,
a ako je istraživanje prvo u nizu i služi kao provjera izvedivosti, može biti
više nego što je potrebno.

## Podsnažene studije pretjeruju

Uobičajena pouka o slaboj snazi glasi da se stvarni učinci propuštaju. To je
točno, ali nije cijela posljedica. Slaba snaga mijenja i skup procjena koje
prežive prag, a na poznatoj populaciji taj se selekcijski učinak može izmjeriti.

Ponovili smo isto pitanje na tri tisuće studija sa šezdeset osoba. Prosjek svih
procjena iznosi `r hr_broj(s11$prosjek_svih, 2)` boda i praktički se poklapa sa
stvarnom razlikom od `r hr_broj(s11$razlika, 2)`, pa postupak prije primjene
praga nije pristran u ovoj simulaciji.

*Slika. Procijenjena razlika u tri tisuće studija sa šezdeset osoba, sve zajedno i samo one koje su prešle prag. Okomita crta označuje stvarnu razliku u populaciji.*

Donji panel prikazuje odabrani podskup koji je u ovoj simulaciji prešao prag.
Prosječna procjena u tom podskupu iznosi
`r hr_broj(s11$prosjek_znacajnih, 2)` boda, odnosno
`r hr_broj(s11$faktor, 1)` puta više od istine. Razlog je mehanički i ne ovisi o
namjeri istraživača. Uz slabu snagu prag uglavnom prelaze uzorci u kojima je
slučajnost razliku uvećala, jer manja procjena s ovako malim uzorkom najčešće ne
može prijeći prag. Najmanja značajna procjena u ovoj simulaciji iznosi
`r hr_broj(s11$najmanja_znacajna, 2)` boda.

Drugi je smjer rjeđi, ali nije nemoguć. Među procjenama koje su u ovoj
simulaciji prešle prag `r hr_broj(s11$krivi_predznak, 2)` % ima suprotan
predznak od stvarne razlike. Takav nalaz ne sadržava računsku pogrešku, ali bi
izolirano vodio pogrešnom sadržajnom zaključku.

Kad istu simulaciju ponovimo s pet stotina osoba, odabrane procjene istinu
premašuju za faktor `r hr_broj(s11$faktor_veliki, 2)`. U tom scenariju
iskrivljenja gotovo nema. Brojčani faktori vrijede samo za ovdje zadanu
populaciju, veličine uzoraka, postupak i prag. Ne opisuju svako istraživačko
područje ni svaki nalaz iz maloga uzorka.

Za čitanje objavljenoga rada zato nije dovoljna presuda da mu je uzorak malen.
Velik učinak uz p-vrijednost tik ispod praga sam po sebi ne dokazuje
precjenjivanje, ali traži provjeru širine intervala, načina odabira nalaza i
usklađenosti s prethodnim dokazima. Povjerenje u veličinu procjene raste ako je
sličan rezultat dobiven u neovisnoj replikaciji. Niska snaga tako usmjerava
pozornost na nesigurnost i selekciju, a ne daje automatsku odluku o tome je li
tvrdnja istinita.

## Planiranje unatrag

Uzorak nije samo stvar raspoloživosti. Odluka o njegovoj veličini počinje
razlikom koja bi bila dovoljno važna da promijeni postupanje.

**Najmanji važan učinak** je najmanja razlika koja bi promijenila zaključak,
odluku ili postupanje, određena sadržajno i prije prikupljanja podataka.

Postavlja ga istraživač, a ne račun, i obrazlaže se troškom postupanja,
ozbiljnošću ishoda i onim što je u istom području već izmjereno. Tek kad je
zapisan, pitanje o veličini uzorka ima odgovor, jer se snaga uvijek računa za
neku određenu veličinu učinka.

Redoslijed je time obrnut od uobičajenog. Ne pita se koliko se ispitanika može
prikupiti pa se nada da će biti dovoljno, nego se kreće od razlike koja bi nešto
značila, dodaje se željena snaga i iz toga izlazi broj jedinica. Ako je taj broj
neizvediv, to je nalaz sam po sebi i treba ga znati prije istraživanja, a ne
poslije.

Postoji i drugi način planiranja, bliži načelu po kojem je ova knjiga napisana.
Umjesto da se pita koliko je jedinica potrebno da bi se prešao prag, pita se
koliko ih je potrebno da bi procjena bila dovoljno precizna. Uz raspršenost iz
ove populacije interval razlike širok je `r hr_broj(s11$sirina_100, 2)` boda pri
stotinu ljudi po skupini, `r hr_broj(s11$sirina_300, 2)` pri tristo i
`r hr_broj(s11$sirina_800, 2)` pri osamsto. Istraživač koji zna da mu je za
odluku potrebna procjena unutar pola boda odatle čita odgovor izravno, bez
pretpostavke o tome koliki je stvarni učinak.

Ta je razlika u pristupu važnija nego što izgleda. Planiranje prema snazi
zahtijeva da se zada veličina učinka koji se traži, a upravo je ta veličina ono
što se ne zna i zbog čega se istraživanje provodi. Uz unaprijed zadanu razinu
pouzdanosti i pretpostavku o raspršenosti, planiranje prema preciznosti ne traži
pretpostavku o veličini učinka, jer širina intervala ovisi o raspršenosti i
broju jedinica. Studija planirana na taj način ne obećava da će nešto naći, nego
da će, što god nađe, biti dovoljno precizno da se o tome može odlučivati.

## Interakcija — Istraživač snage

Sljedeći prikaz odvaja tri odluke koje se u praksi donose zajedno. Čitatelj
mijenja stvarnu veličinu učinka, broj jedinica i prag, svaki put samo jedno, i
prati kako se pomiče udio uzoraka u kojima bi postupak nešto našao.

Prikaz koristi idealizirani model u kojem nulta hipoteza postavlja
standardiziranu razliku na nulu. Testna statistika je apsolutna z-vrijednost, a
postupak je obostran. Model pretpostavlja dvije neovisne skupine jednake
veličine, neovisne normalne ishode i zajedničku poznatu standardnu devijaciju.
Za svaku točku izravno simulira z-vrijednosti iz pripadne normalne raspodjele,
pa broj ponavljanja određuje samo Monte Carlo nesigurnost prikazane snage.

*Slika. Simulirana snaga kroz veličine uzorka u idealiziranom postupku s poznatom varijabilnošću.*

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Spustite prag odluke i provjerite koliko je jedinica potrebno za istu snagu.
4. Postavite standardiziranu razliku na 0,10 i pokušajte dosegnuti 80 %.

Posljednji korak ne uspijeva unutar ponuđenog raspona. Pri standardiziranoj
razlici 0,10 ni tristo jedinica po skupini ne doseže 80 %, pa bi za taj cilj
trebao još veći uzorak. Odluka o tome koji je učinak vrijedan traženja zato mora
doći prije odluke o uzorku.

**Statistika u divljini.**
**Neuspjeh snage.** Button i suradnici pregledali su literaturu iz neuroznanosti
i zaključili da niska prosječna snaga može pridonijeti precijenjenim objavljenim
učincima i slabijoj ponovljivosti rezultata (Button, 2013). Naslov rada naglašava
neuspjeh snage, ali njegov argument nije samo poziv na veće uzorke. Povezuje
vjerojatnost otkrivanja s nesigurnošću procjene i selekcijom nalaza koji prijeđu
prag.

Brojčani rezultat iz naše simulacije ne smije se preslikati na tu literaturu.
Ovdje dvostruko pretjerivanje vrijedi za jednu simuliranu populaciju, uzorak od
šezdeset osoba, jedan permutacijski postupak i jedan prag. Niska snaga zato nije
automatska presuda o istinitosti pojedinoga rada. Ona je razlog da uz interval i
veličinu uzorka provjerimo selekciju nalaza, prethodne dokaze i neovisne
replikacije prije sadržajnoga zaključka.

**Pitajte model.**
Asistent može brzo izračunati standardiziranu razliku i provesti analizu snage,
ali ulazne odluke ne može preuzeti iz samoga računa. Prije poziva treba mu zadati
dizajn, očekivanu raspršenost ishoda i najmanji učinak koji bi nešto značio.
Provjera zatim obuhvaća nazivnik koji odgovara dizajnu, sadržajno opravdanje
veličine učinka i izvor svake unaprijed zadane vrijednosti. Posebno treba odbiti
račun u kojem je ciljna veličina učinka procijenjena iz istih podataka čiju se
snagu zatim navodno provjerava.

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

## Razrađeni primjer

Pretpostavimo da bi uredništvo reagiralo na razliku od pola boda i da očekuje
raspršenost sličnu onoj u ovoj populaciji. Analiza ispod za nekoliko veličina
uzorka broji u kolikom udjelu simuliranih studija bi takva razlika bila
otkrivena.

Nulta hipoteza u ovom računu tvrdi da je razlika sredina nula, a testna
statistika dijeli opaženu razliku poznatom standardnom pogreškom. Simulacija
pretpostavlja dvije neovisne skupine, neovisne normalne ishode, jednaku i poznatu
standardnu devijaciju od 1,9 boda te obostrani z-postupak s pragom 0,05. Za svaku
veličinu uzorka proizvodi dvije tisuće novih parova skupina. Izračunana snaga
vrijedi samo pod tim pretpostavkama i za unaprijed zadanu razliku od pola boda.

Funkcija `replicate` ponavlja cijelu zamišljenu studiju dvije tisuće puta, a
`sapply` isti račun provodi za svaku ponuđenu veličinu uzorka. Granica 1,96
dolazi iz standardne normalne raspodjele i pripada upravo opisanom obostranom
z-postupku, a ne permutacijskom postupku iz prvog prikaza snage.

*Slika. Udio simuliranih studija u kojima bi razlika od pola boda bila otkrivena, pri četirima veličinama uzorka po skupini. Izrada autora.*

Za razliku od pola boda treba između dvjesto i dvjesto pedeset ljudi po skupini
da bi se dosegla uobičajena granica od osamdeset posto. Ako uredništvo može
prikupiti stotinu, plan je i dalje moguć, ali izvještaj mora unaprijed reći da
će studija razliku te veličine propustiti u više od polovice slučajeva.

Račun ne odlučuje ništa od onoga što je važno. Pola boda kao granicu postavio je
netko tko zna što se s tom razlikom radi, raspršenost je procijenjena iz ranijih
mjerenja, a odustajanje ispitanika i kvaliteta mjerenja nisu ni ušli u simulaciju.
Račun daje obranjiv oblik rečenice o uzorku, u kojem broj jedinica stoji uz
učinak koji se njime može uočiti.

## Sažetak

Veličina učinka vraća pitanju koliko je razlika velika, a standardizirana mjera
čini je usporedivom preko različitih ljestvica. Statistička značajnost i
praktična važnost odgovaraju na različita pitanja, pa golem uzorak može odvojiti
od nule i razliku koja ne mijenja odluku. Snaga povezuje učinak, uzorak,
raspršenost i prag, dok planiranje prema preciznosti polazi od potrebne širine
intervala. U simuliranom scenariju maloga uzorka procjene koje su prešle prag u
prosjeku su dvostruko veće od poznate razlike, ali taj broj ne vrijedi izvan
zadanoga mehanizma. Sljedeće poglavlje pokazuje što se događa kada sustav
nagrađuje objavljeni nalaz, a skriva cijeli put koji je do njega doveo.

## Pojmovi

veličina učinka (*effect size*), standardizirana razlika (*Cohen's d*),
praktična važnost (*practical significance*), statistička snaga (*statistical
power*), precjenjivanje učinka u malim uzorcima (*effect-size exaggeration in
small samples*), najmanji važan učinak (*smallest effect size of interest*),
planiranje veličine uzorka (*sample size planning*), širina intervala (*interval
width*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto u simulaciji ovoga poglavlja podskup procjena
koje su prešle prag u prosjeku premašuje poznatu razliku, iako prosjek svih
procjena ostaje blizu istini. Imenujte korak u kojem nastaje iskrivljenje i
objasnite zašto se dobiveni faktor ne smije prenijeti na svako područje.

### Računski

Iz upravljanoga agregata `data/populacija-medija-agregat.csv` uzmite retke za
portal i tisak. U tiskanom ili dokumentnom izdanju iste su vrijednosti u tablici
uz statični prikaz. Za svaki redak podijelite zbroj povjerenja brojem osoba,
usporedite rezultat s pohranjenim prosjekom i izračunajte razliku prosjeka.
Zatim za standardiziranu razliku 0,4 zabilježite snagu pri 40, 80, 160 i 300
jedinica po skupini. U HTML-u upotrijebite widget, a u tiskanom izdanju tablicu
sa zadanom postavkom.

Vratite se objašnjenju standardne pogreške i širine intervala u poglavlju o
procjeni. Objasnite zašto veći uzorak istodobno sužava interval i povećava snagu,
ali ne mijenja unaprijed zadanu veličinu učinka. Predajte dva računa prosjeka,
njihovu razliku, četiri vrijednosti snage i jedan odlomak koji povezuje preciznost
sa snagom. Ocjenjuje se račun i tumačenje, ne pisanje koda.

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
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/12-kriza-i-obnova.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 6 min | Pješčanik p-hakiranja | replikacijski izvještaj, 17 laboratorija | pogl. 4, 5, 9–11 |

**Vinjeta.**
Ljudi su u poznatom pokusu držali olovku zubima ili usnama dok su ocjenjivali
stripove. Razlika između skupina protumačena je kao dokaz da položaj mišića
lica može utjecati na doživljaj zabave (Wagenmakers, 2016). Izvorna je studija izvijestila razliku
od 0,82 boda na ljestvici od 0 do 9, a gotovo tri desetljeća poslije 17
laboratorija provelo je izravne replikacije prema zajedničkom protokolu, s
planom i analitičkim kodom pripremljenima prije uvida u podatke
(Wagenmakers, 2016).

U replikacijama je bilo uključeno 1.894 sudionika (Wagenmakers, 2016).
Objedinjena sirova razlika iznosila je 0,03 boda, uz 95-postotni interval od
−0,11 do 0,16 (Wagenmakers, 2016). Taj rezultat ne govori da izrazi lica nikada
i nigdje ne mogu utjecati na osjećaje. Govori nešto uže i provjerljivije o tome
što se dogodilo kada je određeni postupak ponovljen u više laboratorija.

Laboratorijske rezultate možemo opisati i povezati s eksperimentalnim uvjetom,
ograničeno ih uopćiti na provedene postupke te odlučiti koliko težine dati
izvornoj procjeni. Iz njih ne možemo predvidjeti novi rezultat ni uzročno
objasniti razliku između izvornoga i replikacijskog nalaza.

Zašto je put do toga zaključka važniji od pobjede jednoga broja nad drugim?
Kako jedan privlačan nalaz prolazi kroz istraživački sustav, gdje ga taj sustav
može iskriviti i što reforma stvarno mijenja u postupku?

## Od jedne tvrdnje do provjerljivoga pitanja

Između izvorne procjene i replikacijskoga rezultata ne stoji samo nova skupina
ljudi. Stoji cijeli put odluka. Netko određuje tko može sudjelovati, kako se
izvodi zadatak, koja se ocjena pretvara u ishod, što se događa s nepotpunim
odgovorima i koja će razlika biti glavna. Kada završni članak pokaže samo
posljednju tablicu, čitatelj teško razlikuje odluke donesene prije podataka od
odluka potaknutih onim što su podaci pokazali.

P-hakiranje
namjerno koristi taj prostor. Istraživač može iskušavati ishode, podskupine,
pravila isključivanja ili trenutke zaustavljanja te prikazati put koji je dao
poželjan nalaz. Simmons i suradnici pokazali su simulacijom i pokusima da takva
neobjavljena fleksibilnost može povećati udio lažno pozitivnih zaključaka iako
svaka pojedinačna odluka izgleda uobičajeno (Simmons, 2011). Problem nije mala
p-vrijednost sama po sebi. Uobičajena p-vrijednost kalibrirana je za jednu
unaprijed određenu analizu. Nakon pretraživanja prikazana vrijednost ne opisuje
stopu pogreške cijeloga postupka kojim je odabrana.

Vrt račvajućih putova
ne zahtijeva svjesno pretraživanje. Istraživač može iskreno provesti samo jednu
analizu, ali bi na svakoj raskrsnici izabrao drukčije da su podaci izgledali
drukčije. Konačna odluka zato nije neovisna o podacima, premda su sve
neodabrane grane ostale neizračunane (Gelman, 2013). Ta razlika čuva poštenu
kritiku. P-hakiranje opisuje ponašanje, a račvajući putovi strukturu postupka.

Publikacijska pristranost
dodaje još jednu razinu. Čak i kada je svaka studija korektno provedena,
literatura nije nepristran uzorak svih pokušaja ako vidljivost ovisi o rezultatu.
Open Science Collaboration pokazao je zašto sustav treba proučavati skupno, a
ne svaku razliku svesti na moralnu procjenu pojedinoga autora (Collaboration}, 2015).
Odsutan nalaz nije isto što i nalaz o odsutnosti, ali odsutni pokušaji ipak
mijenjaju sliku koju stvara objavljena literatura.

## Analitička fleksibilnost prije modela

Poglavlja o sažimanju i vizualizaciji već su pokazala da sredina, medijan,
raspon osi i način grupiranja nisu neutralni ukrasi. Ovdje iste odluke čitamo
kao dijelove istraživačkoga sustava. Fleksibilnost počinje pri prikupljanju,
nastavlja se pravilima uključivanja i spajanja, ulazi u rekodiranje i obradu
nedostajućih vrijednosti te tek onda stiže do modela. Dvije analize mogu imati
istu završnu formulu, a ipak predstavljati različite skupove ljudi i različite
ciljne tvrdnje.

**Analitička fleksibilnost** je prostor više obranjivih odluka duž cijeloga puta
podataka, od prikupljanja, uključivanja i spajanja do rekodiranja, postupanja s
nedostajućim vrijednostima i izbora analize.

U registriranom replikacijskom izvještaju (RRR) zajednički je protokol taj
prostor suzio i učinio vidljivijim. Unaprijed
su navedeni kriteriji uključivanja, način izračuna ocjene i glavna sirova
razlika između skupina, a plan i kod nastali su prije uvida u stvarne podatke
(Wagenmakers, 2016). Lokalne prilagodbe nisu time nestale. Postale su dio zapisa
koji se može usporediti s planom. Bit reforme nije uklanjanje svake odluke,
nego promjena vremena njezina donošenja i mogućnost da je netko poslije
provjeri.

**Reproducibilnost** je mogućnost da druga osoba iz istih podataka, materijala i
opisanoga postupka ponovno dobije iste rezultate i utvrdi gdje su nastali.

Reproducibilnost nije isto što i replikacija. Reproduciranje ponovno izvodi
račun nad istim dokaznim materijalom. Replikacija
prikuplja nove podatke. Reproducibilan račun može vjerno ponoviti loše mjerenje
ili nevaljan zaključak, a dobra replikacija može dati drukčiji rezultat zbog
uzorkovne varijacije ili konteksta. Zato trag postupka podupire kritiku, ali ne
zamjenjuje valjanost.

## Replikacija kao kumulativno mjerenje

Sedamnaest laboratorija nije sedamnaest glasova za ili protiv tvrdnje
(Wagenmakers, 2016). Svaki laboratorij daje procjenu na istoj izvornoj ljestvici
i interval koji pokazuje koliko je ta procjena neodređena. Devet točkastih
procjena bilo je pozitivno, ali nijedan od 17 intervala nije bio u cijelosti
iznad nule (Wagenmakers, 2016). Samo dva intervala obuhvatila su izvornu razliku
od 0,82 boda (Wagenmakers, 2016). Brojanje devet „uspješnih” i osam
„neuspješnih” replikacija izbrisalo bi upravo informacije koje intervali nose.

Objedinjena procjena opisuje prosječnu razliku u ovome skupu izravnih
replikacija prema zajedničkom protokolu. Vrijednost 0,03, uz interval od −0,11
do 0,16, dopušta samo male razlike u oba smjera, ali ne određuje pouzdano njihov
predznak (Wagenmakers, 2016). Interval isključuje razlike blizu izvornih 0,82
boda za ovaj postupak, ali ne može isključiti svaki mali učinak niti svaku drugu
operacionalizaciju facijalne povratne sprege (Wagenmakers, 2016).

Kumulativno čitanje zato ide od ciljne tvrdnje prema dizajnu, zatim prema
pojedinačnim procjenama, intervalima i sintezi. Razlike među laboratorijima
nisu automatski dokaz „stvarne heterogenosti”. Mogu odražavati uzorkovnu
varijaciju, lokalni kontekst, mjerenje ili postupak. Ovaj slučaj ne omogućuje
uzročnu procjenu razloga tih razlika. Omogućuje opis, usporedbu i oprezno
uopćavanje na skup postupaka koje su laboratoriji doista proveli.

## Cijeli zapis u forest plotu

Forest plot
treba čitati vodoravno. Točka označuje procijenjenu razliku u jednome
laboratoriju, a crta njezin 95-postotni interval. Okomita puna crta označuje
nulu, odnosno jednaku prosječnu ocjenu u dvjema skupinama. Isprekidana crta na
0,82 pokazuje izvornu procjenu samo kao referencu (Wagenmakers, 2016). Ona nije
osamnaesti laboratorij i ne ulazi u objedinjavanje.

U izvornom zapisu `smile` označuje držanje olovke zubima, a `pout` držanje
olovke usnama (Wagenmakers, 2016). Pozitivna razlika `smile − pout` zato znači
višu prosječnu ocjenu stripova u skupini koja je olovku držala zubima.

*Slika. Procjene sirove razlike smile − pout i 95-postotni intervali u 17 laboratorija. Objedinjena procjena RRR-a iznosi 0,03 [−0,11; 0,16], a isprekidana crta označuje izvornu procjenu 0,82, koja ne ulazi u sintezu. Izrada autora iz lokalne rekonstrukcije službenoga arhiva prema @wagenmakers2016.*

Prikaz nema jednu priču skrivenu u boji. Položaj, duljina intervala, puna i
isprekidana crta te drukčiji znak za sintezu nose značenje i u crno-bijelom
tisku. Točke su raspršene oko nule, a svi intervali presijecaju nulu
(Wagenmakers, 2016).
Objedinjeni interval mnogo je uži jer spaja informacije iz više laboratorija,
ali predstavlja samo laboratorije i postupak uključene u taj RRR.

Osjetljivost
ovdje uspoređuje sirovu razliku s alternativnom standardiziranom procjenjivanom
veličinom, Cohenovim *d*. Standardizirana objedinjena procjena iznosila je 0,01,
uz interval od −0,08 do 0,10, dok je sirova procjena iznosila 0,03, uz interval
od −0,11 do 0,16 (Wagenmakers, 2016). Uspoređuje se isti skup laboratorija, ali
ne posve ista ciljana veličina ni isti relativni doprinos svakoga laboratorija.
Promjena ipak ne mijenja sadržajni zaključak. Obje procjene ostaju blizu nule,
a oba intervala obuhvaćaju male vrijednosti u oba smjera. To nije nova prilika
za lov na prag, nego provjera ovisi li zaključak o jednoj obranjivoj odluci o
mjerilu.

## Reforma redoslijeda i vidljivosti

Predregistracija
odvaja ono što je planirano od onoga što je naučeno iz podataka. Ne zabranjuje
istraživanje neočekivanih obrazaca. Traži da se naknadna grana tako i nazove,
umjesto da se poslije prikaže kao jedini plan. RRR je išao dalje. Plan, kod i
ogledni prikazi pripremljeni su prije stvarnih podataka, pa se kasniji rezultat
može usporediti s unaprijed vidljivim postupkom (Wagenmakers, 2016).

Registrirani izvještaj
mijenja i redoslijed uredničke selekcije. Metoda se može vrednovati prije nego
što urednik vidi je li rezultat nov, velik ili blizu određenoga praga
(Wagenmakers, 2016). Otvoreni materijali zatim daju čitatelju plan, kod i trag do
tablice. U ovome su slučaju službeni članak, projekt, registrirani plan, kod i
podaci povezani, što je omogućilo neovisnu provjeru laboratorijskih procjena
(Wagenmakers, 2016).

Otvorenost ipak nije naredba da se objavi svaki bajt. Sudionički podaci mogu
nositi privatnosna i licencijska ograničenja. Za ovu je knjigu zato iz službenog
arhiva izveden samo neidentificirajući zapis na razini laboratorija. Izvorni
retci sudionika, službeni kod, plan i izdavačev graf nisu preuzeti u knjigu.
Transparentnost uključuje i jasnu izjavu o onome što nije redistribuirano te o
provjeri koja ostaje moguća iz službenoga izvora.

Svaku statističku tvrdnju sada možemo smjestiti u šest dimenzija. Ona može
opisivati, povezivati, uopćavati, predviđati, tvrditi uzrok ili podupirati
odluku. Ovaj RRR podupire opis laboratorijskih rezultata, njihovu
povezanost s uvjetom u provedenom eksperimentu, ograničeno uopćavanje na
provedene postupke i odluku o tome koliko težine dati izvornoj procjeni. Ne daje
predikcijski alat ni uzročnu tvrdnju o tome zašto se izvorna i replikacijska
procjena razlikuju.

Prije prihvaćanja tvrdnje postavljamo šest pitanja. Što je opažanje i koja je
jedinica? Tko ili što nije moglo ući? Koja se ciljna veličina procjenjuje i
koja je vrsta tvrdnje? Koju neizvjesnost interval prikazuje, a koju izostavlja?
Koja je jedna razumna alternativna odluka i mijenja li zaključak? Tko snosi
posljedice pogreške? Reforma ne daje unaprijed točne odgovore. Daje postupak u
kojemu su odgovori vidljivi, usporedivi i osporivi.

## Interakcija — Pješčanik p-hakiranja

Pješčanik omogućuje biranje ishoda, podskupina i trenutka zaustavljanja na
podacima bez stvarnog učinka. Čitatelj promatra kako rast broja odluka povećava
priliku za privlačan rezultat i kako korekcija za cijeli postupak mijenja sliku.
Radi preglednosti svaki je analitički put u simulaciji neovisan. Stvarni putovi
često dijele podatke, ali idealizacija izdvaja cijenu njihova broja. Simulacija
dodatno pretpostavlja valjano kalibrirane p-vrijednosti pod nultim modelom i
unaprijed omeđenu obitelj analiza. Korekcija ovdje ilustrira cijenu poznate
obitelji, ali sama ne rješava neobjavljene ili podatkovno uvjetovane odluke.
Ovisnost među putovima mijenja točan oblik prikazane krivulje.

*Slika. Udio simuliranih istraživanja s barem jednim rezultatom ispod odabranog praga nakon pretraživanja više neovisnih analitičkih putova.*

Ako ukupan broj unaprijed omeđenih putova označimo s $m$, korigirani prag
$0{,}05/m$ raspodjeljuje ukupno dopušteni rizik na sve putove. Svaki
pojedinačni put zato mora prijeći stroži prag. To je zaštita za ovu omeđenu
idealizaciju, a ne opći popravak analitičke fleksibilnosti.

**Što isprobati.**

1. Provedite jednu unaprijed određenu analizu.
2. Dodajte ishode, a podskupine i trenutke provjere ostavite jednakima.
3. Dodajte podskupinske inačice i trenutke provjere bez promjene broja ishoda.
4. Usporedite nominalni prag 0,05 s pragom korigiranim za sve putove.

Najmanja p-vrijednost nije sažetak jedne unaprijed određene analize kada je
nastala pretraživanjem. Zaključak tada mora opisati cijeli skup mogućnosti ili
koristiti postupak koji njihov broj uzima u obzir.

**Statistika u divljini.**
**Sedamnaest procjena nije referendum.** Forest plot RRR-a lako je svesti na
rečenicu da je devet laboratorija našlo pozitivan učinak, a osam negativan
(Wagenmakers, 2016).
Takvo brojanje zanemaruje da nijedan laboratorijski interval nije u cijelosti
iznad nule i da samo dva obuhvaćaju izvornu procjenu 0,82
(Wagenmakers, 2016). Smjer točke ne mjeri snagu dokaza.

Ni objedinjena procjena nije presuda cijeloj teoriji facijalne povratne sprege.
Ona sažima sirovu razliku u ovih 17 izravnih replikacija prema zajedničkom
protokolu (Wagenmakers, 2016). Forest plot zato treba čitati od pitanja i dizajna
prema redcima, pa tek onda prema sintezi. Granice selekcije, mjerenja i konteksta
ne nestaju kada interval postane uzak. Kao opis povezanosti u provedenom pokusu,
prikaz dopušta samo ograničen prijenos na usporedive postupke i odluku o težini
izvorne procjene. Ne predviđa nov rezultat i ne otkriva uzrok razlika među
laboratorijima.

**Pitajte model.**
Asistent može ubrzati usporedbu registriranoga plana, analitičkoga koda,
izvedenog zapisa i rukopisa. Taj je posao koristan samo ako svaku označenu
razliku veže uz točno mjesto u dostupnom materijalu. Uvjerljiv sažetak bez
takvoga traga novi je tekst, a ne provjera.

U osjetljivim podacima najprije pripremamo dopušten, minimalan prikaz. Modelu ne
dajemo sudioničke retke samo zato što ih može pročitati. Čuvamo upit, verziju
alata, njegov izlaz i ručnu dispoziciju svake označene razlike. Publikacija,
podaci i izvršiv postupak ostaju izvori. Model ostaje instrument.

Provjera smije označiti opis, povezanost, uopćavanje ili prijedlog odluke samo
ako za njih pronađe trag u materijalu. Nedostajući dokaz ne smije pretvoriti u
predviđanje ni uzročno objašnjenje.

> Usporedi priloženi registrirani plan, kod, izvedeni zapis i rukopis. Za svako
> neslaganje navedi dokument i mjesto, označi je li potvrđeno ili samo moguće te
> reci koja se tvrdnja mijenja. Ne nadopunjuj dokumente informacijama kojih u
> njima nema.

**Nađite grešku.**
RRR je unaprijed naveo glavni ishod, pravila uključivanja i primarnu analizu
(Wagenmakers, 2016).
Objedinjena sirova razlika iznosi 0,03 boda, uz 95-postotni interval od −0,11 do
0,16 (Wagenmakers, 2016). Budući da je analiza predregistrirana, njezin je
zaključak nužno valjan.

## Razrađeni primjer

Zajednički replikacijski postupak daje sirovu razliku, a jedna standardizirana
grana provjerava mijenja li se sadržajni zaključak. Najprije treba utvrditi
podrijetlo. Službeni arhiv sadrži sudioničke podatke iz 17 laboratorija, ali
knjiga ih ne redistribuira (Wagenmakers, 2016). Iz njega je neovisnom provjerom
izveden minimalan zapis s grupnim sažetcima, procjenama i intervalima. Svih 17
redaka zbraja se na 1.894 uključena sudionika i usklađuje s objavljenim
laboratorijskim sažetcima, osim jednoga lokaliziranog zaokruživanja standardne
devijacije koje se ne rabi u tvrdnjama knjige (Wagenmakers, 2016).

Potpuna tablica dopušta provjeru prikaza i bez pisanja koda. Redci su
laboratoriji, `n` je broj uključenih sudionika, a interval pripada sirovoj
razlici prosječne ocjene između držanja olovke zubima (`smile`) i usnama
(`pout`).

*Slika. Sirove laboratorijske procjene iz RRR-a. Izrada autora iz lokalne rekonstrukcije službenoga arhiva prema @wagenmakers2016.*

Vidljivi isječak nije računanje metaanalize. Prvi redak otvara lokalni zapis, a
drugi zaustavlja postupak ako se očekivanih 17 laboratorija ili 1.894 sudionika
ne podudara (Wagenmakers, 2016). Sljedeća četiri retka bilježe oznake primarne i
alternativne grane, njihove procjene te granice intervala. Posljednji ih redak
slaže u malu tablicu. Funkcija `c` povezuje vrijednosti redom, a `data.frame`
prikazuje ih u imenovanim stupcima. Čitatelj provjerava putanju, brojnost, oznake
grana i vrijednosti koje je reproducirao neovisni verifikator. Isječak ih ne
računa ponovno.

Provjerena sirova procjena iznosi 0,03 uz interval od −0,11 do 0,16, dok
standardizirana procjena iznosi 0,01 uz interval od −0,08 do 0,10
(Wagenmakers, 2016). Tablica dodatno pokazuje 9 pozitivnih točaka, 0 intervala u
cijelosti iznad nule i 2 intervala koja obuhvaćaju 0,82 (Wagenmakers, 2016). Ta
brojanja nisu tri nova testa. Obje grane dolaze iz istih 17 laboratorija, ali
standardizacija mijenja ciljanu veličinu i relativni doprinos laboratorija. Obje
ipak podupiru isti ograničen zaključak.

Zaključak može biti pošteno kratak. Prema zajedničkom postupku iz ovog RRR-a,
prosječna razlika bila je blizu nule i mnogo manja od izvornih 0,82 boda
(Wagenmakers, 2016).
Intervali sirove i standardizirane sinteze dopuštaju male razlike u oba smjera,
ali ne podupiru prijenos izvorne veličine na ove laboratorije
(Wagenmakers, 2016). Analiza ne govori zašto su se rezultati razlikovali, ne
pokriva svaku operacionalizaciju facijalne povratne sprege i ne dokazuje da je
predregistracija uzrokovala rezultat.

Poštena rečenica opisuje opaženu povezanost i prenosi je samo na usporedive
postupke, a odluku o težini izvorne procjene veže uz obje grane. Ne služi
predviđanju ni uzročnom objašnjenju razlike.

## Granica Dijela IV — Od testa do reformirane tvrdnje

Dio IV završava promjenom pitanja. P-vrijednost više nije presuda, a jedna
procjena nije samostalna tvrdnja. Čitatelj sada može povezati nulti model,
veličinu učinka, interval, posljedice pogreške, analitičku fleksibilnost i
tragove reproducibilnosti u jednu ograničenu prosudbu. I dalje ne može iz
rezultata izvesti uzrok razlike među studijama, predvidjeti nalaz u novom
okruženju ili prenijeti zaključak na ljude i postupke koje dizajn nije
obuhvatio. Dio V toj prosudbi dodaje modele za kategoričke ishode, usporedbe
grupa i zajedničko razmatranje više varijabli.

Šest revizijskih pitanja primjenjujemo na višelaboratorijski RRR i njegove dvije
provjerene analitičke grane (Wagenmakers, 2016). Ona vežu brojčani rezultat uz
jedinicu, doseg i odluke koje su ga proizvele.

| Pitanje revizije | Primjena na provjereni zapis |
|---|---|
| Što predstavlja jedan redak ili jedno opažanje? | zapis za jedan laboratorij sa sažetkom razlike između eksperimentalnih uvjeta i njezine nesigurnosti |
| Tko ili što nije moglo ući u ove podatke? | ljudi izvan uključenih uzoraka, drugi laboratoriji i drukčije operacionalizacije facijalne povratne sprege |
| Koja je ciljana količina i vrsta tvrdnje? | prosječna razlika ocjena između uvjeta u zajedničkom postupku, opisana sirovom i standardiziranom sintezom |
| Koji su izvori nesigurnosti obuhvaćeni, a koji ostaju izvan izračuna? | intervali prate preciznost laboratorijskih procjena i sinteze, ali ne uključuju svaku mjernu, selekcijsku ni protokolarnu mogućnost |
| Koja bi razumna alternativna odluka mogla bitno promijeniti odgovor? | standardizirana umjesto sirove sinteze mijenja ciljanu veličinu i relativne doprinose, pa obje grane treba čitati zajedno |
| Na koga može utjecati pogrešan zaključak ili odluka? | pretjerana tvrdnja može zavesti istraživače, urednike i čitatelje pri procjeni težine izvornoga nalaza |

: Šest revizijskih pitanja primijenjenih na provjereni RRR. Izrada autora prema wagenmakers2016.

Odgovori ograničavaju ono što se može prenijeti iz jedne tablice ili slike.
Karta tvrdnji zato razdvaja šest dosega iste analize.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje laboratorijske procjene, intervale i dvije objedinjene analitičke grane |
| povezanost | povezuje prosječnu ocjenu s eksperimentalnim uvjetom u provedenom postupku |
| generalizacija | oprezno prenosi zaključak na usporedive provedene postupke, ne na svaku populaciju ili operacionalizaciju |
| predviđanje | nije poduprto jer analiza ne gradi ni provjerava pravilo za novi laboratorij ili novoga sudionika |
| uzročnost | ne podupire uzročno objašnjenje razlike između izvorne i replikacijskih procjena |
| odluka | podupire opreznije odmjeravanje težine izvorne procjene uz obje grane i njihove intervale |

: Šest dimenzija tvrdnje na granici Dijela IV. Izrada autora prema wagenmakers2016.

Samoprovjera na granici dijela povezuje četiri kumulativna pitanja. Zašto
p-vrijednost ne daje vjerojatnost nulte hipoteze i zašto nalaz blizu nule nije
dokaz njezine istinitosti? Zašto veličinu učinka i interval treba čitati prije
planirane snage, a opaženi učinak ne treba vraćati u kružni račun post hoc
snage? Kako višestrukost i analitička fleksibilnost mijenjaju tumačenje
najmanje p-vrijednosti i koje odluke zato moraju biti vidljive? Koji trag
reproducibilnosti omogućuje provjeru zaključka i koja bi rečenica prešla
potkrijepljeni doseg generalizacije ili uzročnosti?

Reformirana praksa za svaku kasniju analizu traži ciljnu tvrdnju, primarnu
analizu, jednu obranjivu alternativu, podrijetlo podataka i granicu zaključka.
Sljedeći je korak primijeniti taj ugovor na brojeve ljudi u kategoričkim
tablicama. Prije testne statistike mora biti jasno tko je prebrojen, tko nije
mogao ući i koji nazivnik nosi tvrdnju.

## Sažetak

Dokazna vrijednost nalaza ovisi o cijelome putu od pitanja do tvrdnje.
Analitička fleksibilnost obuhvaća odluke pri prikupljanju, pripremi i analizi,
a p-hakiranje i račvajući putovi opisuju različite načine na koje taj prostor
može ostati nevidljiv. Replikacija prikuplja nove podatke, dok reproducibilnost
provjerava može li se isti rezultat ponovno dobiti iz istoga materijala i
postupka. Višelaboratorijski RRR čita se kumulativno kroz procjene, intervale i
sintezu, pri čemu sirova i standardizirana analiza daju isti ograničen zaključak
o razlici blizu nule u provedenom postupku. Predregistracija,
registrirani izvještaji i otvoreni materijali mijenjaju redoslijed i vidljivost
odluka, ali ne jamče valjano mjerenje ni valjanu inferenciju. Ugovor za sljedeća
poglavlja traži ciljnu tvrdnju, primarnu analizu, jednu obranjivu alternativu,
podrijetlo podataka i granicu zaključka.

## Pojmovi

p-hakiranje (*p-hacking*), vrt račvajućih putova (*garden of forking paths*),
publikacijska pristranost (*publication bias*), analitička fleksibilnost
(*analytical flexibility*), reproducibilnost (*reproducibility*), replikacija
(*replication*), forest plot (*forest plot*), osjetljivost (*sensitivity
analysis*), predregistracija (*preregistration*), registrirani izvještaj
(*registered report*)

## Zadaci

### Konceptualni

Istraživač je nakon pregleda podataka iskušao pet pravila isključivanja i
objavio jedino ono koje je dalo poželjan rezultat. Druga je istraživačica prije
analize odlučila „upotrijebit ću medijan ako je raspodjela jako asimetrična, a
sredinu inače” i zatim provela samo odabranu granu. Objasnite koji primjer
prikazuje p-hakiranje, a koji vrt račvajućih putova. Za svaki navedite koji bi
trag postupka čitatelju omogućio provjeru i pokažite gdje se u primjeru nalazi
analitička fleksibilnost (Simmons, 2011; Gelman, 2013). Na kraju jednom rečenicom
razlikujte reproducibilnost takve provjere od replikacije koja bi prikupila nove
podatke.

### Računski

Koristite samo tiskanu tablicu laboratorijskih procjena, bez pisanja koda.
Prebrojite koliko je od
17 točkastih procjena veće od nule i izračunajte taj udio u postocima
(Wagenmakers, 2016). Zatim prebrojite koliko je 95-postotnih intervala u cijelosti
iznad nule i koliko ih obuhvaća izvornu procjenu 0,82 (Wagenmakers, 2016).
Napišite dvije rečenice koje objašnjavaju zašto prvi udio nije stopa „uspjelih
replikacija”.

### Kritički

Vratite se definiciji intervala iz 9. poglavlja i logici nultoga modela iz 10.
poglavlja. Netko uz forest plot ovog poglavlja piše „niti jedan laboratorij
nije dobio značajan rezultat, pa je dokazano da učinak ne postoji”
(Wagenmakers, 2016). Revidirajte tu tvrdnju u tri rečenice. Uključite objedinjenu
procjenu s intervalom, objasnite što nula u prikazu znači, usporedite primarnu i
standardiziranu analizu osjetljivosti te navedite jednu populacijsku ili
kontekstualnu granicu koju forest plot ne uklanja. Dodajte jednu rečenicu o tome
kako bi publikacijska pristranost promijenila tumačenje sinteze kada nevidljive
studije ovise o rezultatu.

### Revizija modela

Revidirajte analizu iz okvira o pogrešci. Predajte zapis s četiri polja. U
prvome prepišite provjerene brojke, u drugome označite jedinu pogrešnu tvrdnju,
u trećemu napišite ispravljeni zaključak, a u četvrtome navedite koji biste
dokument ili redak postupka provjerili prije prihvaćanja analize i objasnite
koju dodatnu vidljivost daje registrirani izvještaj. Ne traži se novi kod.
