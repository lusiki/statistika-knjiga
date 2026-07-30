# DIO III: OD UZORKA DO POPULACIJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Vjerojatnost koliko treba

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Simulator novčića i A/B kampanje | simulacija | pogl. 4 |

**Vinjeta.**
Simmons i suradnici pokazali su kako velik broj razumno zvučećih analitičkih
odluka može povećati vjerojatnost lažno pozitivnog rezultata (Simmons, 2011).
Svaka pojedina odluka mogla je izgledati bezazleno. Problem je postao vidljiv
tek kada se promatrao cijeli niz mogućih putova kroz podatke.

Istraživač zato ne pita samo je li opaženi rezultat moguć pod jednom
pretpostavkom. Mora pitati koliko je prilika postupak dao slučajnosti da
proizvede nešto što izgleda uvjerljivo.

Kako računati s neizvjesnošću bez pretvaranja vjerojatnosti u obećanje o jednom
događaju?

## Neizvjesnost kao raspodjela

**Vjerojatnost** povezuje događaj sa skupom mogućih ishoda. U dugom nizu
ponavljanja može se čitati kao relativna učestalost. U situaciji koja se neće
ponoviti može izražavati stupanj uvjerenja pod jasno navedenim informacijama.
Ta dva čitanja ne moraju biti suparnici, ali zahtijevaju da kažemo na što se
broj odnosi.

Pravilo komplementa prevodi vjerojatnost događaja u vjerojatnost da se događaj
ne dogodi. Zbrajanje pripada međusobno isključivim ishodima, dok množenje
povezuje zajedničko pojavljivanje neovisnih događaja. Najčešća pogreška nije
računska, nego sadržajna pretpostavka da su događaji neovisni samo zato što je
to zgodno za račun.

Binomna situacija ima ponovljene pokušaje, dva ishoda i jednaku vjerojatnost
uspjeha u svakom pokušaju. Glasanje, klik i odgovor na pitanje mogu se tako
modelirati samo kada jedinice i pokušaji dovoljno dobro odgovaraju tim
uvjetima. Model nije opis cijelog svijeta, nego kontrolirana slika dijela
procesa.

## Obrasci mnogih ponavljanja

Pojedinačni ishodi mogu biti neuredni, dok raspodjela velikog broja ishoda
pokazuje stabilan oblik. Normalna krivulja opisuje mnoge takve obrasce oko
središta. Pravilo približnih područja oko sredine korisno je za orijentaciju,
ali se ne primjenjuje na svaku asimetričnu ili višemodalnu raspodjelu.

QQ prikaz uspoređuje poredane podatke s poredanim vrijednostima očekivanima pod
odabranom raspodjelom. Točke blizu pravca podupiru približan oblik, dok
sustavna zakrivljenost pokazuje odstupanje. Prikaz ne izdaje presudu o tome je
li analiza dopuštena. On pokazuje gdje pretpostavka pristaje, a gdje se lomi.

## Interakcija — Simulator novčića i A/B kampanje

Simulator povezuje jednostavno bacanje novčića s A/B kampanjom.
Čitatelj mijenja stvarnu stopu uspjeha i broj pokušaja te promatra kako se
kratki nizovi kolebaju, dok se raspodjela mnogih ponavljanja stabilizira.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu stvarnu vjerojatnost.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na A/B kampanju i postavite stvarnu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

**Statistika u divljini.**
**Mnogo prilika za slučajnost.** Analitička fleksibilnost omogućuje da se među
mnogim ishodima, podskupinama i trenucima zaustavljanja izdvoji rezultat koji
izgleda rijetko, iako je cijeli postupak takav nalaz učinio mnogo vjerojatnijim
(Simmons, 2011).

Čitanje jednog rezultata zato mora uključiti broj pokušaja i odluke donesene
nakon gledanja podataka. Vjerojatnost pripada postupku koji je rezultat
proizveo, a ne samo njegovoj posljednjoj tablici.

**Pitajte model.**
Asistent može simulirati postupak i usporediti analitički račun sa
učestalostima u ponavljanjima. Treba mu jasno opisati skup mogućih ishoda,
neovisnost i sve putove kojima je analiza mogla doći do rezultata. Modeli često
računaju pod prešutnom pretpostavkom neovisnosti.

> Simuliraj ovaj slučaj mnogo puta i prikaži raspodjelu ishoda. Prije računanja
> navedi koje pretpostavke koristiš o neovisnosti i jednakoj vjerojatnosti
> pokušaja.

**Nađite grešku.**
U nizu je više puta zaredom zabilježen isti ishod. Budući da se ravnoteža mora
vratiti, sljedeći pokušaj sada ima veću vjerojatnost suprotnog ishoda.
Pojedinačni pokušaji provedeni su pod jednakim uvjetima.

Greška je kockarska zabluda. Ako su pokušaji neovisni i uvjeti jednaki,
prethodni niz ne mijenja vjerojatnost sljedećeg ishoda.

## Razrađeni primjer

Simuliramo mnogo kampanja s jednakom stvarnom stopom odgovora. Svaka kampanja
daje nešto drukčiji udio, iako se temeljni proces ne mijenja. Histogram
prikazuje koliko je raspršena ta slučajna varijacija.

Raspodjela simuliranih stopa uspjeha. Izrada autora.

Jedna kampanja može završiti daleko od središta bez promjene stvarne stope.
Zaključak se zato ne temelji na tome izgleda li jedan rezultat neobično, nego
na usporedbi s raspodjelom koju bi cijeli postupak mogao proizvesti.

## Sažetak

Vjerojatnost opisuje neizvjesnost unutar jasno određenog skupa mogućnosti.
Pravila računanja vrijede samo uz sadržajne pretpostavke o događajima i
neovisnosti. Simulacija pokazuje kako stabilna raspodjela nastaje iz neurednih
pojedinačnih ishoda. Poglavlje o uzorkovanju tu će logiku primijeniti na
statistike koje se mijenjaju od uzorka do uzorka.

## Pojmovi

vjerojatnost (*probability*), događaj (*event*), neovisnost (*independence*),
binomna raspodjela (*binomial distribution*), normalna raspodjela (*normal
distribution*), QQ prikaz (*Q–Q plot*)

## Zadaci

### Konceptualni

Objasnite zašto niz jednakih ishoda ne mijenja vjerojatnost sljedećeg pokušaja
ako su pokušaji neovisni. Predajte jedan odlomak.

### Računski

Promijenite veličinu pokušaja u objektu `sim_kampanje` i predajte dva histograma
s kratkom usporedbom raspršenosti.

### Kritički

Objasnite kako više analitičkih putova mijenja čitanje rijetkog rezultata
(Simmons, 2011). Predajte dijagram mogućih odluka.

### Revizija modela

Ocijenite analizu modela iz okvira. Imenujte pretpostavku koju navodi, jednu
pogrešku i ispravnu vjerojatnostnu interpretaciju.

---

# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | CLT stroj | simulacija | pogl. 4, 7 |

**Vinjeta.**
Efron je bootstrap predstavio kao način procjene nesigurnosti kada imamo jedan
uzorak, a teorijski račun nije jednostavan (Efron, 1979). Postupak se ponaša kao
da uzorak predstavlja malu dostupnu populaciju i iz njega mnogo puta izvlači
nova opažanja s vraćanjem.

Ta ideja ima smisla tek kada razumijemo što se događa prije bootstrapiranja.
Svaki stvarni uzorak samo je jedan mogući ishod postupka odabira. Drugi uzorak
iz iste populacije dao bi drugu sredinu, udio ili korelaciju.

Kako iz jednog uzorka učimo o cijeloj raspodjeli rezultata koje nismo vidjeli?

## Od populacije do uzorka

**Populacija** je skup jedinica o kojima želimo zaključivati. **Uzorak** je dio
jedinica koje smo stvarno promatrali. Razlika nije samo u veličini. Uzorak
nastaje postupkom odabira, a taj postupak određuje koje populacijske jedinice
imaju priliku postati podatak.

Kada bismo nasumično uzorkovanje ponovili mnogo puta, svaki bi uzorak dao
drugačiju statistiku. Raspodjela tih mogućih statistika naziva se
**distribucija uzorkovanja**. Ona ne opisuje raspršenost pojedinaca, nego
raspršenost procjene kroz ponovljene uzorke.

Standardna pogreška sažima tu raspršenost. S rastom uzorka procjene se obično
zbijaju jer svako pojedinačno opažanje nosi manji dio ukupnog rezultata. Dobit
nije linearna. Udvostručavanje uzorka ne prepolovljuje automatski standardnu
pogrešku, pa vrlo veliki uzorci mogu biti skupi za sve manji dobitak preciznosti.

## Oblik koji se pojavljuje

Središnji granični teorem najprije se može vidjeti. Iz asimetrične populacije
uzimamo mnogo uzoraka, računamo njihove sredine i slažemo ih u novi histogram.
Kako uzorci rastu, histogram sredina postaje pravilniji i zbijeniji iako
izvorna populacija nije normalna.

Taj obrazac omogućuje približne račune za mnoge procjene, ali ne popravlja
pristran odabir. Tisuće odgovora iz zatvorenog okvira ne postaju
reprezentativne samo zato što im je standardna pogreška mala. Slučajna
promjenjivost i sustavna pristranost različiti su problemi.

## Interakcija — CLT stroj

CLT stroj gradi distribuciju uzorkovanja pred čitateljem. Izvorna populacija,
veličina uzorka i broj ponavljanja mogu se mijenjati odvojeno, pa je vidljivo
što utječe na oblik, a što na raspršenost uzoračkih sredina.

*Slika. Izvorna populacija i raspodjela sredina mnogih uzoraka na zajedničkoj osi. Okomita crta označuje populacijsku sredinu simulacije.*

**Što isprobati.**

1. Odaberite simetričnu populaciju i uzorak veličine dva pa usporedite širine dvaju histograma.
2. Promijenite populaciju u desno asimetričnu bez povećanja uzorka.
3. Povećajte uzorak na četrdeset i odvojeno opišite promjenu oblika i širine raspodjele sredina.
4. Odaberite dvovršnu populaciju i pronađite veličinu uzorka pri kojoj se dvije populacijske skupine više ne vide u sredinama.

**Statistika u divljini.**
**Jedan uzorak kao privremena populacija.** Bootstrap iznova uzorkuje opažanja
iz dostupnog uzorka kako bi približio promjenjivost procjene (Efron, 1979).
Postupak ne stvara nove vrste jedinica i ne nadoknađuje dio populacije koji
nikada nije mogao ući u uzorak.

Tvrdnja da je rezultat „bootstrapiran" zato govori o procjeni slučajne
nesigurnosti. Ne dokazuje reprezentativnost niti valjanost mjerenja.

**Pitajte model.**
Asistent može napisati simulaciju distribucije uzorkovanja, ali treba mu
odvojeno zadati populaciju, postupak odabira, veličinu uzorka i statistiku.
Provjeravamo uzorkuje li s vraćanjem samo kada je to namjera i brka li
raspršenost pojedinaca sa standardnom pogreškom procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno opiši standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

Greška je zamjena dviju razina varijabilnosti. Veći uzorak sužava raspodjelu
procjene, ali ne mora smanjiti razlike među pojedincima u svakom uzorku.

## Razrađeni primjer

Stvaramo desno asimetričnu simuliranu populaciju i iz nje ponavljano uzimamo
uzorke dviju veličina. Za svaki uzorak računamo sredinu. Usporedba dviju
distribucija pokazuje da veći uzorci daju zbijenije procjene.

Distribucije sredina pri dvjema veličinama uzorka. Izrada autora.

Izvorna populacija ostaje asimetrična u oba slučaja. Mijenja se ponašanje
sredine kroz ponavljanja. Ta razlika između raspodjele opažanja i raspodjele
statistike nosi cijelo kasnije zaključivanje.

## Sažetak

Uzorak je jedan ishod postupka odabira, a distribucija uzorkovanja opisuje kako
bi se procjena mijenjala kroz ponavljanja. Standardna pogreška pripada procjeni,
ne pojedincima. Veći uzorci obično povećavaju preciznost, ali ne uklanjaju
sustavnu pristranost. Poglavlje o procjeni upotrijebit će tu raspodjelu kako bi
izgradilo interval oko vrijednosti koju ne možemo izravno vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), distribucija uzorkovanja
(*sampling distribution*), standardna pogreška (*standard error*), središnji
granični teorem (*central limit theorem*), reprezentativnost
(*representativeness*)

## Zadaci

### Konceptualni

Razlikujte raspodjelu opažanja od distribucije uzoračkih sredina. Predajte
skicu i dva popratna objašnjenja.

### Računski

Promijenite veličine uzorka u simulaciji `sim_sredine` i predajte graf koji
pokazuje promjenu širine distribucije.

### Kritički

Objasnite što bootstrap može, a što ne može nadoknaditi kada je početni uzorak
pristran (Efron, 1979). Predajte jedan odlomak.

### Revizija modela

Ocijenite analizu modela iz okvira. Izdvojite točan zaključak o preciznosti,
jednu zamjenu razina varijabilnosti i njezin popravak.

---

# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | Hvatač intervala | simulacija | pogl. 8 |

**Vinjeta.**
Cumming je zagovarao izvještavanje procjena i intervala kao središte
statističkog zaključivanja, umjesto oslanjanja na samu odluku o značajnosti
(Cumming, 2014). Pomak mijenja pitanje koje postavljamo podacima. Umjesto
binarnog prolaza pitamo koliki je učinak i koliko je procjena precizna.

Interval ipak nije ukras oko točkaste procjene. Njegovo značenje dolazi iz
postupka koji bi kroz ponovljene uzorke stvarao intervale, među kojima neki
obuhvaćaju populacijsku vrijednost, a neki je promašuju.

Kako iz jednog opaženog intervala pošteno govoriti o vrijednosti koja ostaje
nepoznata?

## Od točke prema rasponu

**Točkasta procjena** daje jednu vrijednost iz uzorka. Ona je najbolji sažeti
pogodak koji trenutačno imamo, ali drugi bi uzorak dao drugi rezultat. Interval
pouzdanosti toj procjeni dodaje raspon usklađen s njezinom uzoračkom
promjenjivošću.

Širi interval nije znak lošeg istraživača. On može pošteno pokazivati mali
uzorak ili vrlo promjenjive podatke. Uži interval označava veću preciznost pod
pretpostavkama postupka. Ne govori da su mjera, uzorak i model nepristrani.

Razina pouzdanosti pripada dugoročnom postupku. Kada bismo uzorkovanje i izradu
intervala ponavljali, unaprijed određeni udio intervala obuhvatio bi fiksnu
populacijsku vrijednost. Nakon što je jedan interval izračunat, njegova je
granica opažena, a populacijska vrijednost ostaje nepoznata.

## Bootstrap iz uzorka

Bootstrap ponovljeno izvlači opažanja s vraćanjem iz dostupnog uzorka, računa
željenu statistiku i slaže dobivene vrijednosti u raspodjelu (Efron, 1979).
Postupak tako približava pitanje što bi se dogodilo s procjenom kada bismo mogli
ponoviti prikupljanje sličnih podataka.

Njegova snaga je prilagodljivost. Može se primijeniti na medijan, razliku,
korelaciju i druge statistike za koje jednostavna formula nije pri ruci.
Njegova granica ostaje početni uzorak. Ako on ne predstavlja populaciju ili je
premalen da zabilježi važan dio raspodjele, resampling ponavlja tu prazninu.

## Interakcija — Hvatač intervala

Hvatač intervala prikazuje niz ponovljenih uzoraka i njihove intervale oko iste
populacijske vrijednosti. Većina je hvata, a neki je promašuju. Tek niz
intervala čini značenje razine pouzdanosti vidljivim. Simulacija koristi
normalnu populaciju poznate standardne devijacije kako bi odvojila logiku
obuhvata od procjene same standardne devijacije.

*Slika. Intervali iz ponovljenih simuliranih uzoraka oko fiksne populacijske sredine. Istaknuti intervali promašuju okomitu ciljnu crtu.*

**Što isprobati.**

1. Zadržite pedeset intervala i prebrojite one koji ne sijeku okomitu ciljnu crtu.
2. Povećajte broj intervala na sto bez promjene veličine uzorka ili razine pouzdanosti.
3. Usporedite širinu intervala pri uzorcima veličine dvadeset i sto.
4. Promijenite razinu pouzdanosti s devedeset na devedeset i devet posto te opišite odnos širine i obuhvata.

**Statistika u divljini.**
**Procjena prije odluke.** Pristup „novih statistika" stavlja veličinu učinka,
interval i metaanalitičko povezivanje nalaza ispred binarne odluke o
značajnosti (Cumming, 2014).

Interval ne jamči da je istina blizu sredine ni da je istraživanje valjano.
Njegova vrijednost je u tome što čitatelju pokazuje koje su veličine još
usklađene s postupkom i koliko prostora ostaje za znanstvenu nesigurnost.

**Pitajte model.**
Asistent može bootstrapirati gotovo svaku statistiku, ali treba provjeriti
uzorkuje li s vraćanjem, čuva li strukturu uparenih ili grupiranih podataka i
ponavlja li dovoljno puta. Modeli često daju pogrešno probabilističko značenje
već izračunatom intervalu.

> Izračunaj točkastu procjenu i bootstrap interval. Sačuvaj strukturu podataka,
> opiši postupak resamplinga i interpretiraj razinu pouzdanosti kao svojstvo
> ponovljenog postupka.

**Nađite grešku.**
Bootstrap raspodjela je približno simetrična i interval je uredno izračunat iz
njezinih krajeva. Postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

Greška je pripisivanje vjerojatnosti fiksnom parametru nakon izračuna
frekventističkog intervala. Razina pouzdanosti opisuje dugoročni udio intervala
koji obuhvaćaju parametar.

## Razrađeni primjer

Simulirani uzorak sadrži ocjene povjerenja. Zanimaju nas medijan i njegova
nesigurnost jer raspodjela nije savršeno simetrična. Bootstrap uzorci ponovno
izvlače opažene ocjene s vraćanjem i za svaki izračunavaju medijan.

*Slika. Bootstrap procjena medijana simuliranih ocjena. Izrada autora.*

Tablica je rezultat simuliranog nastavnog primjera, a ne nalaz o stvarnom
povjerenju. Ona pokazuje redoslijed izvještavanja. Najprije dolazi procjena,
zatim raspon nesigurnosti i naposljetku ograničenje uzorka i mjere.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval prikazuje
preciznost postupka i mora se tumačiti kroz ponovljeno uzorkovanje. Bootstrap
približava tu promjenjivost resamplingom dostupnog uzorka, bez čarobnog
popravljanja njegove pristranosti. Sljedeće poglavlje uvodi testiranje kao još
jedan način usporedbe opaženog rezultata s raspodjelom mogućih rezultata.

## Pojmovi

točkasta procjena (*point estimate*), interval pouzdanosti (*confidence
interval*), preciznost (*precision*), bootstrap (*bootstrap*), resampling
(*resampling*), parametar (*parameter*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. Predajte jedan odlomak.

### Računski

Upotrijebite `sim_povjerenje`. Bootstrapirajte aritmetičku sredinu i medijan te
predajte usporednu tablicu intervala.

### Kritički

Prosudite zašto izvještaj usmjeren na procjenu i interval daje više informacija
od same odluke o značajnosti (Cumming, 2014). Predajte tri rečenice.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira. Imenujte točan postupak, jednu
pogrešnu rečenicu i frekventistički ispravnu zamjenu.
