# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 21 min | Hvatač intervala | simulirana populacija | pogl. 8 |

**Vinjeta.**
Cumming je zagovarao izvještavanje procjena i intervala kao središte
statističkog zaključivanja, umjesto oslanjanja na samu odluku o značajnosti
(Cumming, 2014). Pomak mijenja pitanje koje postavljamo podacima. Umjesto
binarnog prolaza pitamo koliki je učinak i koliko je procjena precizna.

Poglavlje o uzorkovanju pokazalo je zašto takvo pitanje uopće ima smisla. Naša
procjena samo je jedan ishod iz raspodjele mogućih ishoda, a širina te
raspodjele poznata je u simulaciji jer smo uzorkovanje ponovili tri tisuće puta.

Istraživač koji objavljuje rezultat nema tri tisuće uzoraka. Ima jedan, i iz
njega mora reći koliko je siguran.

Kako iz jednoga opaženog uzorka pošteno govoriti o vrijednosti koja ostaje
nepoznata?

## Od točke prema rasponu

Uzorak od `r hr_broj(s9$n, 0)` osoba iz naše populacije daje prosječno
povjerenje u medije od `r hr_broj(s9$sredina, 2)`. Ta jedna vrijednost naziva se
**točkasta procjena** (*point estimate*) i najbolji je sažeti pogodak koji
trenutačno imamo. Njezina je slabost u tome što ne nosi nikakav trag vlastite
nesigurnosti. Ista brojka mogla je nastati iz uzorka od dvadeset ljudi i iz
uzorka od dvadeset tisuća, a te dvije situacije ne zaslužuju jednako povjerenje.

Sve što nedostaje već je izračunato u prethodnom poglavlju. Standardna pogreška
mjeri koliko bi procjena tipično varirala kroz ponovljena uzorkovanja, a za naš
uzorak iznosi `r hr_broj(s9$se, 3)`. Uz nju procjena prestaje biti gola brojka i
postaje brojka s poznatom skalom vlastitog kolebanja.

Prije nego što rasponu damo ime, vratimo se poznatoj populaciji. Deset tisuća
puta izvukli smo po dvjesto osoba. Oko svake dobivene sredine povukli smo
raspon od 1,96 njezinih standardnih pogrešaka na svaku stranu i provjerili
siječe li fiksnu populacijsku vrijednost. Cilj je obuhvaćen u
`r paste0(hr_broj(s9$pokrivenost, 1), " %")` raspona, a promašen u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja.
Pojedini raspon može promašiti, ali postupak kroz ponavljanja pokazuje stabilan
udio pogodaka.

Središnji granični teorem kazuje i kakav oblik to kolebanje ima. Raspodjela
uzoračkih sredina približno je normalna, a za normalnu raspodjelu znamo koliki
udio vrijednosti pada unutar zadanog broja standardnih devijacija od središta,
što je pravilo koje je poglavlje o vjerojatnosti već postavilo. Približno 95 %
vrijednosti leži unutar 1,96 standardnih devijacija.

Odatle slijedi konstrukcija koja se čini gotovo previše jednostavnom da bi
radila. Ako je naša sredina u 95 % slučajeva unutar 1,96 standardnih pogrešaka
od populacijske vrijednosti, tada je i populacijska vrijednost u 95 % slučajeva
unutar te iste udaljenosti od naše sredine. Razmak oko procjene dug 1,96
standardnih pogrešaka na svaku stranu zato će hvatati cilj u 95 % ponavljanja.

Slovo $z^{*}$ označava koliko standardnih pogrešaka širimo na svaku stranu.
Bira ga željena razina, pa je za 95 % jednako 1,96.

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

Za naš uzorak taj račun daje raspon od `r hr_broj(s9$donja, 2)` do
`r hr_broj(s9$gornja, 2)`, a prava populacijska vrijednost iznosi
`r hr_broj(s9$mu, 2)` i nalazi se unutra.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Vrijedi obratiti pozornost na to gdje u toj definiciji stoji obećanje. Ono ne
stoji uz raspon nego uz postupak, i upravo se ta razlika u praksi najčešće gubi.

Polovica ukupne širine toga raspona jest **margina pogreške**. Poglavlje o tome
kako brojke zavode ostavilo ju je kao dug kada je uz anketni postotak prikazalo
znak ±, a sada je vidljivo što taj znak sažima. U ovom postupku margina iznosi
$z^{*} \cdot SE$ i pokriva promjenjivost koju bi ponovljeno uzorkovanje
proizvelo pod pretpostavkama postupka. Ne pokriva pristran okvir, neodgovor,
formulaciju pitanja ni pogrešku mjerenja. Zato manja margina znači uži raspon
uzoračke neizvjesnosti, a ne općenito bolju anketu.

## Obećanje razine pouzdanosti

Simulirani postupak radi približno onako kako obećava, i vrijedi zadržati riječ
približno. Broj pogodaka u konačnom nizu nije unaprijed propisan. Zamjena
nepoznate populacijske raspršenosti onom izmjerenom u uzorku
unosi vlastitu nesigurnost, koja je pri dvjesto osoba mala, a pri dvadeset osoba
ne bi bila. Ispravak koji to nadoknađuje širi interval za mali uzorak i knjiga
ga uvodi u poglavlju o usporedbi dviju grupa, gdje ga postupak prvi put stvarno
treba.

Ono što se u brojci od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne vidi jest
sudbina pojedinačnog intervala. Svaki od tih deset tisuća raspona ili sadrži
pravu vrijednost ili je ne sadrži, i nakon što je izračunat, u njemu nema
ničega slučajnog. Slučajan je bio uzorak koji ga je proizveo. Populacijska
sredina fiksan je broj i ne kreće se, pa rečenica o vjerojatnosti da se ona
nalazi unutar zadanih granica opisuje nešto što nema promjenjivosti koju bi ta
vjerojatnost mjerila.

Analogija koja to drži na okupu jest bacanje obruča na fiksni kolac. Obruč je
interval, kolac je parametar, a razina pouzdanosti opisuje koliko često obruč
pada oko kolca kroz mnogo bacanja. Nakon jednoga bacanja obruč je pao ili nije,
a mi ga gledamo zatvorenih očiju. Postotak opisuje ruku koja baca, ne ovaj
pojedini obruč.

Zbog te razlike korisno je znati što čitatelj objavljenog intervala smije reći.
Vrijednosti unutar granica uskladive su s podacima, a one izvan njih slabo su
uskladive pod pretpostavkama postupka. Širina također pokazuje ispunjava li
raspon unaprijed zadani cilj preciznosti, primjerice marginu manju od deset
minuta. Interval za jedan parametar ipak ne govori može li se razlučiti razlika
ili promjena, jer za to treba procijeniti samu razliku i njezinu nesigurnost.
Ne pripisujemo mu ni vjerojatnost da parametar leži unutra niti očekivanje da
će se ponovljeno istraživanje smjestiti unutar istih granica, jer bi ono imalo
vlastiti uzorak i vlastiti interval.

## Interakcija — Hvatač intervala

Prebrojavanje iz prethodnog odjeljka dalo je jednu brojku i sakrilo postupak koji
je do nje doveo. Widget taj postupak vraća na vidjelo, jer prikazuje same
intervale, jedan ispod drugoga, oko iste nepomične ciljne crte. Veličina uzorka i
razina pouzdanosti mijenjaju se odvojeno, pa se vidi da prva mijenja širinu
intervala, a druga mijenja i širinu i učestalost promašaja.

*Slika. Intervali iz ponovljenih simuliranih uzoraka oko fiksne populacijske sredine. Istaknuti intervali promašuju okomitu ciljnu crtu.*

**Što isprobati.**

1. Zadržite pedeset intervala i prebrojite one koji ne sijeku okomitu ciljnu crtu.
2. Povećajte broj intervala na sto bez promjene veličine uzorka ili razine pouzdanosti.
3. Usporedite širinu intervala pri uzorcima veličine dvadeset i sto.
4. Promijenite razinu pouzdanosti s devedeset na devedeset i devet posto te opišite odnos širine i obuhvata.

### Tiskane postavke za vježbu

Čitatelj tiskanoga izdanja iste dvije usporedbe može provesti bez widgeta.
Sljedeće tri postavke nastale su iz normalne populacije sa sredinom nula i
standardnom devijacijom jedan. Svaka sadrži pedeset intervala iz fiksnoga
simulacijskog niza. Postavke A i B razlikuju se samo po razini pouzdanosti, a A
i C samo po veličini uzorka.

*Slika. Tri fiksne postavke za usporedbu širine i promašaja intervala u tiskanom izdanju. Izrada autora.*

Isti sintetički podaci dostupni su kao pojedinačni zapisi i kao sažetak po
primarnom izvoru vijesti. Sljedeća tablica prikazuje sažetak bez novoga
računanja i bez zaokruživanja pohranjenih vrijednosti. Ona priprema kasniju
provjeru istih rezultata iz pojedinačnih zapisa. Budući da je populacija
sintetička, tablica provjerava postupak i ne iznosi empirijsku tvrdnju o
stvarnim stanovnicima.

*Slika. Brojnici, nazivnici i agregatne vrijednosti za portal u sintetičkoj populaciji. Izrada autora prema javnom agregatnom prikazu sintetičkih podataka.*

## Preciznost nasuprot pouzdanosti

Dva pomaka koja widget dopušta imaju vrlo različite učinke i lako ih je pobrkati
jer oba mijenjaju širinu. Veći uzorak sužava interval time što smanjuje
standardnu pogrešku, pa uz jednako obećanje o obuhvatu dobivamo precizniji
odgovor. Prosječna širina intervala pri uzorku od pedeset osoba iznosi
`r hr_broj(s9$sirine[["50"]], 2)` boda, pri dvjesto
`r hr_broj(s9$sirine[["200"]], 2)`, a pri osamsto
`r hr_broj(s9$sirine[["800"]], 2)`.

Viša razina pouzdanosti također širi interval, ali ništa ne dobiva na
preciznosti. Na istom našem uzorku raspon od 90 % širok je
`r hr_broj(s9$razine[["90"]], 2)` boda, onaj od 95 %
`r hr_broj(s9$razine[["95"]], 2)`, a onaj od 99 %
`r hr_broj(s9$razine[["99"]], 2)`. Podaci se nisu promijenili, promijenio se
zahtjev. Interval koji obuhvaća cilj u 100 % slučajeva postoji i proteže se od
minus do plus beskonačno, čime savršena pouzdanost postaje savršeno beskorisna.

**Preciznost** je zato svojstvo koje se plaća podacima, a **pouzdanost** je
svojstvo koje se bira i plaća širinom. U ovoj knjizi 95 % služi kao uobičajena
nastavna postavka, a ne kao prirodna granica. Uz svaki interval zato navodimo
razinu na kojoj je izračunat.

Širok interval ne znači loše obavljen posao. Češće znači mali uzorak ili
podatke koji su stvarno raspršeni, i tada je široki raspon iskren opis stanja, a
ne priznanje nesposobnosti. Suprotan je slučaj mnogo opasniji. Uzak interval
oko procjene iz pristranog uzorka izgleda kao preciznost, a jest sigurnost u
pogrešnu vrijednost, jer interval mjeri samo ono što bi se mijenjalo kroz
ponavljanja istoga postupka.

Iz širine slijedi i način na koji se intervali čitaju kada ih je više na istoj
slici, što je najčešći oblik u kojem ih društveni znanstvenik susreće. Grafovi
koji uz svaku skupinu crtaju raspon umjesto samog stupca odmah pokazuju koje su
procjene oslonjene na malo ljudi, a koje na mnogo, i time govore više od
tablice prosjeka. Iskušenje je da se iz njih očita i zaključak o razlici.

Nepreklapanje usporedivih intervala može biti snažan dokaz da jednakost nije
dobro uskladiva s podacima pod pretpostavkama postupka. Iz preklapanja ipak ne
slijedi da razlike nema, a ni jedan ni drugi obrazac ne daje vjerojatnost da je
razlika „stvarna”. Ovisnost procjena i istraživački nacrt dodatno određuju kako
se takva slika čita. Pošten odgovor zato traži interval za samu razliku, a ne
dva intervala jedan pokraj drugoga. Taj postupak knjiga uvodi u poglavlju o
usporedbi dviju grupa.

Postoji i druga zamjena koja se često javlja u istom odlomku. Interval
pouzdanosti govori gdje je prosjek, a ne gdje su ljudi. Za naš uzorak od
dvjesto osoba raspon oko sredine dug je
`r hr_broj(s9$gornja - s9$donja, 2)` boda. Ako su pojedinačne ocjene približno
normalno raspoređene, sredina plus ili minus 1,96 uzoračkih standardnih
devijacija daje opisni raspon po normalnom pravilu širok približno
`r hr_broj(2 * s9$normalni_poluraspon, 1)` boda, u kojem bi pod tim modelom
ležalo oko 95 % ocjena. Za izrazito asimetrične, ograničene ili diskretne
raspodjele takav opisni obuhvat ne slijedi. Taj prikaz nije interval predviđanja
za novu osobu, jer ne uključuje nesigurnost procjene središta i raspršenosti
niti određuje iz koje bi populacije buduća osoba došla. Interval za sredinu
odnosi se na parametar i sužava se s većim uzorkom, dok opisni raspon prikazuje
raspršenost pojedinačnih ocjena.

*Slika. Interval pouzdanosti za sredinu i opisni raspon po normalnom pravilu za pojedinačne ocjene na istom uzorku i istoj osi.*

## Bootstrap kao vlastiti izum

Sve dosad počiva na jednoj formuli za standardnu pogrešku, a upotrebljiv
zatvoren račun nije jednako dostupan za svaku mjeru. Za sredinu je jednostavan,
za udio također, dok za medijan, razliku percentila ili omjer može biti
nepraktičan ili tražiti dodatne pretpostavke. Odgovor za slučaj kada takav račun
nemamo može se smisliti bez ijedne nove ideje, uz uvjet da se prethodno
poglavlje shvatilo ozbiljno.

Standardna pogreška bila je definirana kroz ponovljene uzorke iz populacije.
Kad bismo populaciji imali pristup, izvukli bismo tisuću uzoraka, izračunali
tisuću medijana i pogledali koliko se razilaze. Populaciji pristupa nemamo,
imamo samo uzorak. Njegova empirijska raspodjela može privremeno glumiti
populaciju samo ako opažene jedinice razumno predstavljaju ciljnu populaciju.
U jednostavnom bootstrapu redaka pretpostavljamo i da su jedinice neovisne i
međusobno zamjenjive na razini na kojoj su bile uzorkovane. Uparena,
grupirana ili ponovljena opažanja zato se ne rastavljaju na proizvoljne retke,
nego se ponovno uzorkuju cijeli parovi, skupine ili osobe. Pod tim uvjetima
uzorci jednake veličine iz opaženih podataka oponašaju promjene sastava koje
bismo vidjeli pri novom uzorkovanju iz populacije.

Izvlačenje mora biti s vraćanjem, i to nije tehnički detalj. Izvlačenjem bez
vraćanja iz uzorka od šezdeset osoba dobili bismo šezdeset istih osoba u drugom
poretku, pa bi svaki takav uzorak dao identičan medijan i raspodjela ne bi
imala nikakvu širinu. Vraćanjem opažanja u posudu dopuštamo da neka uđu
dvaput, a neka nijednom, i upravo ta promjena sastava oponaša promjenu sastava
koja nastaje pri izvlačenju iz populacije. Postupak nosi ime **bootstrap** i
uveden je kao način procjene nesigurnosti kada teorijski račun nije pri ruci
(Efron, 1979).

Uzmimo uzorak od `r hr_broj(s9$mali_n, 0)` osoba i pitajmo se koliko iznosi
medijan dnevnih minuta praćenja medija. U uzorku on iznosi
`r hr_broj(s9$medijan_uzorak, 1)` minuta. Četiri tisuće bootstrap uzoraka daju
središnji percentilni raspon od `r hr_broj(s9$boot_donja, 1)` do
`r hr_broj(s9$boot_gornja, 1)` minuta. Poznata populacijska vrijednost od
`r hr_broj(s9$medijan_pop, 1)` minuta u ovom se jednom slučaju nalazi unutar
granica. Slika zato pokazuje konstrukciju raspona iz jednoga uzorka, a ne
njegovu dugoročnu pokrivenost.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću.*

Histogram ima vidljiv stubast oblik jer medijan maloga, zaokruženog uzorka može
poprimiti samo ograničen skup vrijednosti. Ta diskretnost nije računalna
pogreška, ali granice percentilnog raspona čini grubima. Veći broj bootstrap
ponavljanja smanjuje slučajno kolebanje izračunanih percentila, no ne dodaje
nove vrijednosti u siromašan početni uzorak i ne uklanja grube granice ni
nestabilnost koje je mali uzorak već zadao.

Bootstrap ne pretpostavlja imenovani oblik populacijske raspodjele, ali nije
bez pretpostavki. Shema se mora prilagoditi statistici i dizajnu. Kod
korelacije ponovno uzorkujemo cijele parove vrijednosti, kod razlike između
neovisnih skupina svaku skupinu zasebno, a kod ovisnih podataka cijele neovisne
jedinice. Postupak također ne može obnoviti rijetke ili krajnje vrijednosti koje
početni uzorak nije zabilježio. Procjene repova, poput vrlo visokog percentila,
zato su osobito osjetljive na mali uzorak i raspodjele s teškim repovima, dok
je medijan manje ovisan o repovima, ali pri mnogo vezanih vrijednosti i dalje
daje grube granice. Ako uzorak ne predstavlja ciljnu populaciju, bootstrap
precizno ponavlja isti problem umjesto da ga ukloni.

### Kodirani udio i dvije nesigurnosti

Kada je podatak nastao kodiranjem teksta, procijenjeni udio nosi najmanje dva
odvojena izvora nesigurnosti. **Uzoračka nesigurnost** dolazi od toga koji su
tekstovi ušli u korpus ili uzorak. **Nesigurnost kodiranja** dolazi od pravila
po kojem je tekst svrstan, rubnih slučajeva i odluka kodera ili klasifikatora.
Mjerenje može dodati još jedan izvor ako kodirana kategorija samo približno
predstavlja pojam koji istraživanje želi zahvatiti.

Bootstrap redaka s već dodijeljenim oznakama mijenja sastav opaženih tekstova i
zato može prikazati uzoračku komponentu pod pretpostavkom da je jedinica
ponovnog uzorkovanja ispravna. Ne mijenja pravilo kodiranja i ne provjerava
jesu li oznake valjane. Kada bi se rubni tekstovi razvrstali drugim obranjivim
pravilom, procijenjeni udio mogao bi se pomaknuti iako bi bootstrap interval za
svaku od dviju inačica bio uzak. Pošten izvještaj zato uz procjenu i interval
navodi jedinicu teksta, ciljnu populaciju tekstova, postupak odabira i pravilo
kodiranja te izrijekom kaže koju je nesigurnost račun obuhvatio, a koju nije.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživači su studentima i aktivnim
znanstvenicima predočili interval iz zamišljenoga istraživanja i uz njega šest
tvrdnji o njegovu značenju, među kojima nijedna nije bila točna (Hoekstra, 2014).
Velik dio ispitanika u svim skupinama, uključujući iskusne istraživače,
prihvatio je barem neke od njih (Hoekstra, 2014).

Tvrdnje nisu bile besmislene. Upravo ih uvjerljivost čini poučnima. Sve su govorile o
vjerojatnosti da se prava vrijednost nalazi unutar granica, ili o tome koliko
je vjerojatno da bi se ponovljeno istraživanje unutar njih smjestilo. Postupak
koji smo izgradili takva obećanja ne daje, jer se njegov postotak odnosi na
udio intervala koje bi ponovljeno uzorkovanje proizvelo. Nalaz ne pokazuje da
su intervali loš alat nego da je rečenica kojom ih opisujemo teža od računa
koji ih proizvodi.

**Pitajte model.**
Asistent može bootstrapirati mnoge statistike, ali ispravan kod ne jamči
ispravan plan ponovnog uzorkovanja. Provjeravamo predstavlja li početni uzorak
ciljnu populaciju i koja je stvarno neovisna jedinica. Zatim gledamo uzorkuje li
s vraćanjem na punoj veličini uzorka i čuva li parove, skupine ili ponovljena
opažanja. Broj ponavljanja također mora biti dovoljan da računalno kolebanje
granica bude malo. Ključna pogreška koju ovdje provjeravamo nije u kodu nego u
zaključnoj rečenici, gdje se već izračunatom intervalu pripiše vjerojatnost.

> Izračunaj točkastu procjenu i bootstrap interval. Uzorkuj s vraćanjem na
> punoj veličini uzorka, sačuvaj strukturu podataka i interpretiraj razinu
> pouzdanosti kao svojstvo ponovljenog postupka.

**Nađite grešku.**
Za vektor `minute` s jednom vrijednošću po neovisno uzorkovanoj osobi asistent
je vratio kratak račun za bootstrap medijana.

Objasnio je da `replicate` ponavlja postupak, `sample` na punoj veličini uzorka
i s vraćanjem mijenja njegov sastav, `median` u svakom ponavljanju računa istu
mjeru, a `quantile` uzima središnjih 95 % dobivenih vrijednosti. Zatim je
zaključio da postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

## Razrađeni primjer

Naručitelja istraživanja zanima koliko vremena dnevno stanovnici grada provode
uz medije. Procjena mu je uporabiva samo ako njezina margina nije veća od deset
minuta, a na raspolaganju je uzorak od šezdeset ljudi.

Prvi izbor nije statistički nego opisni. Dnevne minute imaju rep prema velikim
vrijednostima, a poglavlje o sažimanju podataka pokazalo je da prosjek takav
rep povlači za sobom, dok medijan ostaje kod tipičnog ispitanika. Za pitanje o
tome koliko vremena uz medije provodi uobičajena osoba medijan je pošteniji
odgovor. Cijena tog izbora vidi se tek sada, jer za sredinu imamo jednostavan
račun standardne pogreške, dok bi račun za medijan tražio dodatne pretpostavke.
Upravo zato ovaj primjer i postoji.

Cijeli bootstrap stane u istu petlju koju je poglavlje o uzorkovanju već
pokazalo, uz jednu izmjenu. Umjesto iz populacije, izvlačimo iz uzorka, i to s
vraćanjem.

Poziv `sample` uz argument `replace` izvlači s vraćanjem i jedini je novi
element u odnosu na prethodno poglavlje, dok `quantile` odsijeca zadani udio
raspodjele s obje strane. Blok proizvodi upravo one tri brojke koje je odjeljak
o bootstrapu već naveo, jer je riječ o istoj analizi ispisanoj u cijelosti.

Odgovor najprije imenuje populaciju i jedinicu, a tek zatim broj. Za ciljnu
populaciju odraslih stanovnika simuliranoga grada, gdje je jedinica jedna
osoba, medijan dnevnog praćenja medija procjenjujemo na
`r hr_broj(s9$medijan_uzorak, 1)` minuta. Percentilni bootstrap raspon od 95 %
proteže se od `r hr_broj(s9$boot_donja, 1)` do
`r hr_broj(s9$boot_gornja, 1)` minuta i opisuje uzoračku promjenjivost medijana
pod navedenim uvjetima. Raspon je širok gotovo
`r hr_broj(s9$boot_gornja - s9$boot_donja, 0)` minuta, pa njegova margina
iznosi približno
`r hr_broj((s9$boot_gornja - s9$boot_donja) / 2, 0)` minuta. Time unaprijed
zadani cilj od najviše deset minuta nije ispunjen. Poštena je odluka izvijestiti
o stvarnoj širini ili prikupiti dovoljno informacija za precizniju procjenu, a
ne iz ovoga raspona zaključivati o promjeni. Kada odabrane osobe ne bi
predstavljale ciljnu populaciju, populacijska bi se tvrdnja povukla i ostao bi
samo opis uzorka, jer bootstrap tu pogrešku ne uključuje.

Budući da populaciju poznajemo, možemo napraviti i ono što stvarno istraživanje
ne može. Prava vrijednost iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i nalazi
se unutar granica. Taj jedan pogodak ne potvrđuje niti opovrgava percentilni
bootstrap. Deset tisuća ponavljanja iz ranijeg odjeljka provjerava drugi
postupak, normalni interval za sredinu. Pokrivenost raspona za medijan trebalo bi
provjeriti ponavljanjem cijeloga lanca, od novog uzorka od šezdeset osoba do
novoga bootstrap raspona u svakom ponavljanju, pa zatim prebrojiti koliko takvih
raspona obuhvaća populacijski medijan. Takva provjera ovdje nije provedena, pa
primjer pokazuje konstrukciju i ograničenja raspona, a ne dokazuje njegovu
nominalnu pokrivenost.

Redoslijed kojim su tri brojke ispisane isti je onaj kojim se rezultat i
izvještava. Najprije dolazi procjena, jer je ona odgovor na postavljeno pitanje.
Zatim dolazi raspon, jer bez njega procjena tvrdi više nego što zna. Tek na
kraju dolazi ograda, koja ovdje kaže da su podaci simulirani, da je mjera
medijan, a ne prosjek, i da šezdeset ljudi nije mnogo. Ista tri koraka vrijede
za nalaz čija je populacija stvarna, s tom razlikom da se ondje srednji korak
mora izvesti bez izravne provjere prema poznatom parametru u istom istraživanju,
i upravo zato mora biti izveden pažljivo.

## Granica Dijela III — Od procjene do tvrdnje

Šest revizijskih pitanja povezuje vjerojatnost, uzorkovanje i procjenu. Ona
sprječavaju da uzak raspon postane dopuštenje za širu tvrdnju od one koju
podaci i postupak mogu nositi. Na razrađenom primjeru odgovori izgledaju ovako.

| Pitanje revizije | Primjena na bootstrap medijana |
|---|---|
| Što predstavlja jedan redak ili jedno opažanje? | jednu generiranu odraslu osobu s jednim zapisom dnevnih minuta |
| Tko ili što nije moglo ući u ove podatke? | uzorak je slučajno izvučen iz poznate sintetičke populacije, pa ne predstavlja stvarni grad ni osobe izvan te populacije |
| Koja je ciljana količina i vrsta tvrdnje? | populacijski medijan dnevnih minuta, opisan procjenom i rasponom uzoračke nesigurnosti |
| Koji su izvori nesigurnosti obuhvaćeni, a koji ostaju izvan izračuna? | bootstrap mijenja sastav uzorka pod zadanom jedinicom, ali ne provjerava pokrivenost ovoga postupka, mjerenje minuta ni doseg na stvarne stanovnike |
| Koja bi razumna alternativna odluka mogla bitno promijeniti odgovor? | prosjek bi odgovarao na drugo pitanje i jače bi pratio desni rep, a veći uzorak mogao bi dati uži raspon za isti medijan |
| Na koga može utjecati pogrešan zaključak ili odluka? | u ovoj sintetičkoj vježbi nitko stvaran, a u analognoj odluci naručitelj i stanovnici mogli bi dobiti neopravdano preciznu tvrdnju |

: Šest revizijskih pitanja primijenjenih na procjenu iz simulirane populacije. Izrada autora.

Odgovori određuju rečenicu koja se smije prenijeti. Oni ne pretvaraju
sintetičku populaciju u empirijski dokaz, a izostavljenu mjernu nesigurnost ili
nesigurnost kodiranja ne skrivaju unutar uzoračkoga raspona. Karta tvrdnji zato
razdvaja šest mogućih dosega iste analize.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje medijan i raspodjelu minuta u opaženom sintetičkom uzorku |
| povezanost | nije poduprta jer primjer ne uspoređuje dvije varijable |
| generalizacija | usmjerena je na poznatu sintetičku populaciju pod postupkom slučajnoga odabira, bez prava prijenosa na stvarni grad |
| predviđanje | nije poduprto jer nije izgrađeno ni provjereno pravilo za nova opažanja |
| uzročnost | nije poduprta jer nema intervencije ni usporedbe mogućih ishoda |
| odluka | poduprta je odluka da raspon ne ispunjava unaprijed zadanu marginu od najviše deset minuta, ali ne tvrdnja o promjeni ni odluka o medijskoj politici |

: Šest dimenzija tvrdnje na granici Dijela III. Izrada autora.

Samoprovjera na granici dijela obuhvaća četiri povezana pitanja. Zašto pedeset
intervala u widgetu ne mora sadržavati točno pet posto promašaja? Zašto
bootstrap redaka s gotovim oznakama ne uključuje nesigurnost kodiranja? Koje
elemente mora sadržavati poštena rečenica o procjeni i što mora doći prije
brojke? Zašto
podjela već sastavljenih podataka na skupove za učenje i provjeru ne zamjenjuje
vjerojatnosni uzorak za populacijsku generalizaciju?

Kratki račun provjere čini delegirani bootstrap čitljivim i bez pisanja koda.
Svako polje povezuje zahtjev, izlaz i odgovornost s dokazom koji je vidljiv u
ovom poglavlju.

| Polje računa | Bootstrap medijana |
|---|---|
| Što je traženo | procijeniti populacijski medijan dnevnih minuta i njegovu uzoračku nesigurnost iz uzorka neovisnih osoba |
| Što je vraćeno | točkasta procjena te donja i gornja granica središnjega percentilnog raspona |
| Što je provjereno | puna veličina ponovnog uzorka, izvlačenje s vraćanjem, ista statistika u svakom ponavljanju i redoslijed izvještavanja |
| Kako je provjereno | čitanjem poziva `sample`, `median`, `replicate` i `quantile` te usporedbom ispisa s brojkama u prozi |
| Uloga AI-ja | instrument i pogrešiv analitičar |
| Što je ostalo neprovjereno | dugoročna pokrivenost percentilnoga postupka za medijan, reprezentativnost u stvarnom istraživanju i valjanost mjerenja minuta |
| Odgovorna osoba | osoba koja odabire procjenjivanu količinu, provjerava račun i potpisuje zaključak |

: Čitljiv račun provjere za procjenu iz Dijela III. Izrada autora.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval pouzdanosti
uzima standardnu pogrešku i oblik koji je dao središnji granični teorem te oko
procjene gradi raspon čije obećanje pripada postupku, a ne pojedinačnom rasponu
koji imamo pred sobom. Preciznost se kupuje podacima, a pouzdanost se bira i
plaća širinom, pa uz svaki raspon mora stajati razina na kojoj je izračunat.
Bootstrap istu ideju oslobađa formule tako što uzorku dopušta da privremeno
glumi populaciju kada uzorak i jedinica ponovnog uzorkovanja odgovaraju ciljnom
načinu uzorkovanja. Time otvara mjere za koje jednostavan račun ne postoji, ali
ne popravlja premalen ili nereprezentativan uzorak niti pogrešno odabranu
jedinicu ponovnog uzorkovanja. Kodirani udio nosi i nesigurnost kodiranja i
nesigurnost mjerenja, koje bootstrap već zadanih oznaka ne obuhvaća. Poštena
rečenica zato imenuje populaciju i jedinicu, navodi procjenu, mjernu jedinicu i
raspon te završava konkretnim ograničenjem koje bi moglo promijeniti zaključak.
Sljedeće poglavlje uzima isti aparat i mijenja mu pitanje, jer umjesto raspona
usklađenog s podacima traži koliko su podaci neobični pod jednom određenom
pretpostavkom.

## Pojmovi

procjena (*estimate*), interval pouzdanosti (*confidence interval*), razina
pouzdanosti (*confidence level*), margina pogreške (*margin of error*),
preciznost (*precision*), bootstrap (*bootstrap*), percentilni raspon
(*percentile interval*), jedinica ponovnog uzorkovanja (*resampling unit*),
nesigurnost kodiranja (*coding uncertainty*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica te zašto bootstrap gotovih oznaka teksta ne
obuhvaća nesigurnost pravila kodiranja. Predajte jedan odlomak.

### Računski

Iz tiskane tablice s trima postavkama izračunajte širinu svakog intervala kao
$2z^*/\sqrt{n}$ i usporedite rezultat s objavljenom širinom i brojem promašaja.
Objasnite što se mijenja između postavki A i B, a što između A i C. Zatim u
alatu iz Dodatka A ili B otvorite analitičku datoteku
`data/populacija-medija.csv`, zabilježite ukupan broj redaka pa izdvojite retke
za koje je `izvor_vijesti_sifra` jednak 1. Reproducirajte broj izdvojenih
redaka, ukupan nazivnik, zbroj `povjerenje_medijima`, udio portala i prosječno
povjerenje među korisnicima portala. Usporedite svih pet rezultata s
agregatnom tablicom u ovom poglavlju i s datotekom
`data/populacija-medija-agregat.csv`.
Predajte račun za tri postavke, pet reproduciranih vrijednosti i jednu rečenicu
o slaganju analitičkog i agregatnog prikaza. Ocjenjuje se rezultat i provjera,
ne pisanje koda.

### Kritički

Vratite se prikazu **Istraživač margine pogreške** u poglavlju o tome kako
brojke zavode. Usporedite stanje s uzorkom od 1000 osoba bez pristranosti i
stanje s jednakim uzorkom te pristranošću od šest postotnih bodova. Oba
pokazuju procjenu od 52 %. Primijenite ondje uvedeni protokol čitanja ankete i
sadašnje znanje o intervalima. Objasnite zašto ista uska margina pogreške ne
može obuhvatiti pristranost odabira, navedite koji je izvor nesigurnosti unutar,
a koji izvan intervala te napišite ispravljenu tvrdnju za pristrano stanje.
Predajte usporedbu dvaju stanja i ispravljenu tvrdnju.

### Revizija modela

Pročitajte modelov račun iz okvira o pogrešci. Za svaki od poziva `replicate`,
`sample`, `median` i `quantile` jednom rečenicom povežite redak koda s pojmom
koji provodi. Zatim izdvojite jedinu pogrešnu rečenicu i napišite
frekventistički ispravnu zamjenu koja zadržava razinu od 95 % i ne uvodi nove
tvrdnje o podacima. Kod ne treba prepisivati ni mijenjati.
