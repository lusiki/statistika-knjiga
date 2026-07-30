# Povezanost

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 20 min | Pogodi korelaciju | simulirana anketa, Anscombeov kvartet | pogl. 4, 5 |

**Vinjeta.**
Anscombeova četiri skupa imaju gotovo jednaku Pearsonovu korelaciju, iako
njihovi grafovi prikazuju različite odnose (Anscombe, 1973). Analitičar koji je
dobio samo koeficijent mogao je uredno izvijestiti o smjeru i jačini linearne
veze, a ipak propustiti zakrivljenost ili jedno opažanje koje određuje cijeli
rezultat.

Korelacija je bila točno izračunata. Nije pogriješila u računu, nego je sažela
samo jedan aspekt odnosa. Poteškoća je nastala kada je taj sažetak pročitan kao
potpuna slika.

Što koeficijent povezanosti čuva, a koje odnose ostavlja izvan kadra?

## Zajedničko kretanje

Dvije su varijable povezane kada se njihov raspored mijenja zajedno. Pozitivna
veza znači da se veće vrijednosti jedne češće pojavljuju uz veće vrijednosti
druge. Negativna veza spaja veće vrijednosti jedne s manjima druge. Slaba
linearna veza ne znači da odnosa nema, jer zakrivljeni obrazac može imati
koeficijent blizu nule.

Do mjere se dolazi pitanjem koje se može postaviti za svakog pojedinog
ispitanika. Je li iznad prosjeka u obje varijable, ispod prosjeka u obje, ili
iznad u jednoj i ispod u drugoj. U simuliranoj anketi `anketa_mreze`, koja ima
`r s6_n` ispitanika i nije mjerenje nego nastavni skup proizveden kodom, na istu
stranu prosjeka u dobi i u dnevnim minutama odstupa
`r paste0(hr_broj(100 * s6_udio_slaganje, 0), " %")` ispitanika. Kada varijable
ne bi bile povezane, taj bi udio bio blizu polovine, jer bi predznaci dvaju
odstupanja bili neovisni. Udio znatno ispod polovine znak je da odstupanja
redovito idu na suprotne strane, dakle da je veza negativna. Sam udio ipak ne
kaže koliko je veza jaka, jer ne razlikuje jedva prijeđeni prosjek od krajnje
vrijednosti.

Odgovor na to daje umnožak. Za svakog se ispitanika pomnože njegova odstupanja
od dviju sredina, čime se veliko slaganje nagrađuje jače od malog, a neslaganje
ulazi s negativnim predznakom. Prosjek tih umnožaka po cijelom uzorku mjera je
zajedničkog kretanja.

**Kovarijanca** je prosjek umnožaka odstupanja dviju varijabli od njihovih
sredina, uz djelitelj umanjen za jedan, pa je pozitivna kada opažanja
odstupaju na istu stranu i negativna kada odstupaju na suprotne.

Zapisano simbolima, gdje $x_i$ i $y_i$ označavaju vrijednosti izmjerene kod
istog opažanja, $\bar{x}$ i $\bar{y}$ njihove sredine, a $n$ broj opažanja,
kovarijanca glasi

$$\operatorname{Cov}(x, y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}).$$

Djelitelj $n-1$ isti je onaj iz poglavlja o sažimanju podataka, a formula je
poopćenje varijance, jer varijanca nastaje kada se ista varijabla stavi na oba
mjesta.

Jedna osobina kovarijancu čini neupotrebljivom za izvještavanje. Ona nosi
jedinice obiju varijabli pomnožene jedna s drugom. Kovarijanca dobi i dnevnih
minuta u anketi iznosi `r hr_broj(s6_kov, 1)`, a kovarijanca dobi i istog
vremena izraženog u satima `r hr_broj(s6_kov_sati, 1)`. Odnos se nije
promijenio, promijenila se jedinica, a broj se promijenio šezdeset puta.
Vrijednost kovarijance zato ne govori ništa dok se ne zna u čemu je mjereno,
i nijedan se par varijabli po njoj ne može usporediti s drugim parom.

## Zajedničko kretanje bez jedinica

Rješenje je već napisano u poglavlju o sažimanju podataka. Standardizirana
vrijednost pretvara opažanje u broj standardnih devijacija od sredine i time
odbacuje jedinicu. Ako se prije množenja obje varijable standardiziraju,
umnožak više ne ovisi o tome mjeri li se vrijeme u minutama ili satima.

**Pearsonova korelacija** je prosjek umnožaka standardiziranih vrijednosti
dviju varijabli, pa mjeri smjer i jačinu njihove linearne veze na ljestvici od
$-1$ do $+1$, neovisno o mjernim jedinicama.

Uzoračku korelaciju označavamo slovom $r$, a odgovarajuću vrijednost cijele
populacije grčkim slovom $\rho$, po istom pravilu po kojem su u poglavlju o
sažimanju podataka uzorak nosio latinicu, a populacija grčka slova. Definicija
se zapisuje kao

$$r = \frac{1}{n-1} \sum_{i=1}^{n} z_{x_i} \, z_{y_i} = \frac{\operatorname{Cov}(x, y)}{s_x \, s_y},$$

gdje su $z_{x_i}$ i $z_{y_i}$ standardizirane vrijednosti dviju varijabli kod
istog opažanja, a $s_x$ i $s_y$ njihove standardne devijacije. Dva zapisa daju
isti broj, jer dijeljenje kovarijance standardnim devijacijama i
standardiziranje prije množenja isti su postupak izveden različitim redom.

Da to nije samo tvrdnja, provjerava se izravno. Prosjek umnožaka
standardiziranih vrijednosti dobi i dnevnih minuta u anketi iznosi
`r hr_broj(s6_r_iz_z, 3)`, a ugrađeni izračun korelacije daje
`r hr_broj(s6_r, 3)`. Ista korelacija izračunata na satima umjesto minuta
iznosi `r hr_broj(s6_r_sati, 3)`, dakle nepromijenjeno, dok se kovarijanca u
istoj zamjeni pomaknula šezdeset puta. Standardizacija je učinila upravo ono
zbog čega je uvedena.

Krajnje vrijednosti ljestvice imaju geometrijsko značenje. Vrijednost $+1$ znači
da sve točke leže na jednom uzlaznom pravcu, $-1$ da leže na silaznom, a nula da
linearne veze nema. Sve između mjeri koliko se oblak približio pravcu, i to je
cijeli sadržaj koeficijenta. Ono što on ne mjeri jest nagib tog pravca, pa
korelacija od `r hr_broj(s6_r, 2)` ne govori za koliko se minuta mijenja
vrijeme korištenja po godini dobi. Taj broj daje tek regresija, i to je razlika
koju poglavlje o regresiji razrađuje.

## Koliko znači jedan koeficijent

Nakon izračuna redovito slijedi pitanje je li dobiveni broj velik. Cohen je za
društvene znanosti ponudio orijentacijske vrijednosti, po kojima se korelacija
oko 0,10 opisuje kao mala, oko 0,30 kao srednja, a oko 0,50 kao velika
(Cohen, 1988). Te se vrijednosti citiraju toliko često da su stekle status
ljestvice za očitavanje, što nisu.

Uvjet stoji već kod izvora. Vrijednosti su ponuđene za polja u kojima ne postoji
bolja osnova za prosudbu i izričito ustupaju mjesto poznavanju područja
(Cohen, 1988). U predviđanju pojedinačnog ponašanja korelacija od 0,30 ozbiljan
je nalaz, a u provjeri pouzdanosti mjernog instrumenta 0,50 je razlog za
odbacivanje instrumenta. Isti broj u dvama kontekstima nosi suprotne prosudbe,
pa se veličina ne očitava iz tablice nego iz literature koja mjeri isto što i
mi.

Jedna preinaka koeficijenta ipak pomaže prosudbi, jer ga stavlja na ljestvicu
koja se lakše tumači. Kvadrirana korelacija kaže koliki je udio varijance jedne
varijable zajednički s drugom, pa korelacija od `r hr_broj(s6_r, 2)` znači da
dvije varijable dijele `r paste0(hr_broj(100 * s6_r^2, 0), " %")` varijance,
dok preostalih `r paste0(hr_broj(100 * (1 - s6_r^2), 0), " %")` ostaje
neobjašnjeno. Kvadriranje je pritom nemilosrdno prema srednjim vrijednostima,
jer korelacija od 0,30, koju bi mnogi opisali kao osrednju, dijeli devet posto
varijance. Poglavlje o regresiji istu veličinu koristi kao mjeru prilagodbe
modela.

Druga polovina odgovora nema veze s veličinom. Koeficijent izračunat na uzorku
procjena je, pa nosi vlastitu nesigurnost, koja opada s brojem opažanja.
Korelacija od 0,40 na trideset ispitanika i ista korelacija na tri tisuće
ispitanika dva su vrlo različita nalaza, iako je broj jednak. Dio knjige o
uzorkovanju i procjeni tu nesigurnost izračunava, a do tada vrijedi da se
korelacija bez broja opažanja uz sebe ne može prosuditi.

Kada se varijabli nakupi, korelacije svih parova slažu se u matricu, koja je
simetrična i na dijagonali nosi jedinice, jer je svaka varijabla savršeno
povezana sama sa sobom.

*Slika. Korelacije triju brojčanih varijabli simulirane ankete. Izrada autora.*

Matrica je ekonomična i opasna u istoj mjeri. Tri varijable daju tri para,
deset varijabli daje četrdeset pet, a pregled u kojem se traži najveći broj
prestaje biti provjera hipoteze i postaje njezino izmišljanje. Poglavlje o krizi
i obnovi pokazuje što se s takvim pretraživanjem dogodi kada mu se doda
testiranje. Ovdje je dovoljno pravilo da matrica služi za pregled, a da svaki
par koji ulazi u zaključak dobije vlastiti raspršeni dijagram.

## Rangovi umjesto vrijednosti

Pearsonova korelacija mjeri koliko se oblak približio pravcu, pa je zakrivljena
veza za nju djelomično nevidljiva. Odnos u kojem jedna varijabla stalno raste s
drugom, ali sve sporije, postoji i uredan je, a mjeren pravcem izgleda slabije
nego što jest.

Za takve slučajeve podaci se prije računanja zamjenjuju rangovima. Najmanja
vrijednost dobiva prvi rang, sljedeća drugi, i tako redom, nakon čega se na
rangove primijeni isti Pearsonov izračun. Rangiranje čuva poredak i odbacuje
razmake, pa rezultat mjeri je li kretanje dosljedno u jednom smjeru bez zahtjeva
da bude pravocrtno. Tako dobivena **Spearmanova korelacija**, koja se označava
sa $r_s$, mjeri monotonu vezu.

*Slika. Dob i dnevno vrijeme korištenja u simuliranoj anketi. Veza je dosljedno silazna, ali nije pravocrtna, pa je mjera koja traži pravac strože kažnjava.*

Oblak pada strmo u mlađim godinama i izravnava se poslije, što je oblik koji
pravac ne može pratiti. Pearsonova korelacija dobi i dnevnih minuta iznosi
`r hr_broj(s6_r, 2)`, a Spearmanova `r hr_broj(s6_rs, 2)`. Razlika u istom
smjeru redovit je znak da je veza monotona, ali zakrivljena. Potvrda dolazi
odmah, jer korelacija dobi s logaritmom minuta, koja zakrivljenost uklanja,
iznosi `r hr_broj(s6_r_log, 2)` i približila se Spearmanovoj vrijednosti.

Iz toga slijedi jednostavna dijagnostika. Kada se dva koeficijenta slažu, veza
je približno pravocrtna i Pearsonov je izbor u redu. Kada se razilaze,
zakrivljenost je vjerojatna i graf će je pokazati. Spearmanova mjera uz to slabije
reagira na pojedinačno krajnje opažanje, jer krajnja vrijednost dobiva samo
sljedeći rang umjesto vlastite udaljenosti, pa se koristi i kada podaci sadrže
malo opažanja koja izrazito odudaraju.

Nijedna od dviju mjera ne vidi vezu koja nije monotona. Kada je zadovoljstvo
niže i pri vrlo malom i pri vrlo velikom opterećenju, oba koeficijenta mogu
ispasti blizu nule, jer se uzlazni i silazni dio međusobno ponište. To nije
znak da odnosa nema nego znak da nijedan jedan broj taj odnos ne može nositi.

## Kada koeficijent zavarava

Prvi način na koji koeficijent zavara nije pogreška računanja nego izbor onoga
tko je birao uzorak. Korelacija mjeri koliko varijacije jedne varijable prati
varijaciju druge, pa uklanjanje varijacije uklanja i mjeru.

**Ograničenje raspona** (*range restriction*) je smanjenje izmjerene
povezanosti do kojeg dolazi kada uzorak pokriva samo dio raspona jedne
varijable, pa unutar njega ostaje premalo varijacije da bi se odnos vidio.

Anketa to pokazuje na sebi. U cijelom uzorku korelacija dobi i dnevnih minuta
iznosi `r hr_broj(s6_r, 2)`. Ograničimo li se na najmlađu dobnu skupinu, u kojoj
je `r s6_n_uzak` ispitanika unutar raspona od sedam godina, ista korelacija
iznosi `r hr_broj(s6_r_uzak, 2)`, dakle slabo i k tome u suprotnom smjeru.
Vrijedi znati odakle taj drugi broj dolazi. Generator koji je skup proizveo
razlikuje dobne skupine, a unutar skupine svim ispitanicima dodjeljuje istu
raspodjelu, pa je prava vrijednost unutar te skupine nula. Dobivenih
`r hr_broj(s6_r_uzak, 2)` cijelim je iznosom ono što promjenjivost uzorka
proizvede na `r s6_n_uzak` opažanja.

Veza između dobi i vremena korištenja time nije opovrgnuta. Nestao je raspon
dobi unutar kojeg se mogla očitati, i to je razlog zbog kojeg se studija
provedena na studentima jedne generacije ne može uzeti kao dokaz da dob nije
važna. Isto vrijedi za svaku selekciju koja prethodi mjerenju, dakle za uzorke
sastavljene od primljenih kandidata, zaposlenih radnika ili preživjelih
poduzeća. Poglavlje o mjerenju i dizajnu isti postupak opisuje kao pitanje o
tome tko je ušao u skup.

Isti izračun pokazao je i drugi način na koji koeficijent zavara, jer je broj
različit od nule ovdje nastao iz uzorka u kojem veze nema. Što je opažanja
manje, to je takav ishod vjerojatniji, pa koeficijent bez broja opažanja uz sebe
ne nosi dovoljno da bi se prosudio. Treći je način osjetljivost na pojedinačno
opažanje, jer jedna vrijednost daleko od ostalih pomiče oba prosjeka i obje
standardne devijacije, a s njima i sam koeficijent. Sva tri načina nose isti
simptom, dakle broj koji izgleda uvjerljivo, i sva tri otkriva isti postupak,
dakle pogled na raspršeni dijagram prije nego što se broj negdje zapiše.

## Kada se predznak preokrene

Najteži slučaj nije oslabljen nego preokrenut koeficijent. On nastaje kada
uzorak sadrži podskupine koje se razlikuju po razini obiju varijabli, a
promatraju se zbirno.

Zamislimo tri odjela jedne organizacije, koji se razlikuju po tome koliko su
njihovi zaposlenici iskusni i koliko su zadovoljni poslom. Podaci koji slijede
konstruirani su za ovu svrhu i nisu mjerenje. Unutar svakog odjela zadovoljstvo
blago opada s godinama staža, dok su odjeli s iskusnijim zaposlenicima ujedno
oni s višim zadovoljstvom.

*Slika. Konstruirani podaci u kojima zbirna veza raste, a veza unutar svakog odjela pada. Isti su podaci prikazani jednom bez oznake odjela i jednom s njom.*

Zbirna korelacija staža i zadovoljstva iznosi `r hr_broj(s6_r_zbirno, 2)`, dakle
jasno pozitivna. Unutar odjela ona iznosi
`r hr_broj(s6_r_odjeli$r[[1]], 2)`, `r hr_broj(s6_r_odjeli$r[[2]], 2)` i
`r hr_broj(s6_r_odjeli$r[[3]], 2)`, dakle negativna u sva tri. Nijedan broj nije
pogrešno izračunat i nijedan ne proturječi drugome, jer odgovaraju na različita
pitanja. Zbirni koeficijent mjeri i razliku među odjelima i odnos unutar njih
odjednom, a razlika među odjelima ovdje je toliko veća da određuje predznak.

Ista je pojava koju je Simpson opisao na tablicama frekvencija (Simpson, 1951), a
poglavlje o statističkom mišljenju pokazalo je na stvarnom slučaju prijamnog
postupka u Berkeleyju, gdje se zbirna razlika u stopama prijma raspala čim su
odjeli razdvojeni (Bickel, 1975). Vizualni oblik iste pojave nose mala višestruka
polja iz poglavlja o vizualizaciji. Zajedničko im je da razlika među skupinama i
odnos unutar skupina nisu ista veličina, i da ih zbirni broj spaja u jedan.

Društvene znanosti taj problem susreću u obliku koji nema ni jednu podskupinu
nego samo pogrešnu jedinicu analize. Korelacije se često računaju na zemljama,
županijama ili školama, dakle na prosjecima, jer su podaci u tom obliku
dostupni. Prosjeci su glatkiji od pojedinaca, pa su korelacije među njima
redovito znatno jače, a njihov smjer ne mora vrijediti unutar tih jedinica.
Zaključak o pojedincu izveden iz veze među skupinama naziva se **ekološkom
pogreškom** (*ecological fallacy*), i ne otklanja se boljim izračunom nego samo
podacima o pojedincima. Tvrdnja izračunata na razini zemalja legitiman je nalaz
o zemljama, i ništa više od toga.

Odatle slijedi ono što se o uzroku smije reći. Varijabla koja je povezana i s
pretpostavljenim uzrokom i s ishodom prisvaja dio veze koja se pripisuje uzroku,
i to je konfundirajuća varijabla iz poglavlja o mjerenju i dizajnu. Odjel je
ovdje takva varijabla, jer određuje i staž i zadovoljstvo. Kada je poznata i
izmjerena, razdvajanje je popravlja. Kada nije izmjerena, ona i dalje djeluje, a
koeficijent o njoj ne javlja ništa.

Zbog toga povezanost sama ne određuje uzrok. Veza između dviju varijabli
podnosi četiri objašnjenja, jer prva može djelovati na drugu, druga na prvu,
obje može oblikovati treća, ili je obrazac nastao pukom promjenjivošću uzorka.
Koeficijent je jednak u sva četiri slučaja i ne razlikuje ih. Razlikuje ih
dizajn istraživanja, o kojem je poglavlje o mjerenju i dizajnu već govorilo, pa
je smjer tvrdnje koju o povezanosti smijemo iznijeti određen prije nego što je
izračunata.

## Interakcija — Pogodi korelaciju

Igra prikazuje četiri raspršena oblaka bez koeficijenta i traži procjenu
smjera i jačine. Rezultat se mijenja sa svakom procjenom, pa se vidljivi oblik
može izravno usporediti s veličinom Pearsonove korelacije.

*Slika. Četiri deterministički simulirana oblaka bez prikazanih koeficijenata. Zajedničke osi omogućuju usporedbu smjera i zbijenosti.*

**Što isprobati.**

1. Procijenite samo znak svake povezanosti i provjerite jesu li klizači na pravoj strani nule.
2. Usporedite oblake A i D te procijenite koji je odnos bliže savršenoj povezanosti.
3. Fino namjestite procjene za slabije oblake B i C bez mijenjanja prvih dviju.
4. Pokušajte ostvariti četiri pogotka, zatim opišite koji je oblak bilo najteže procijeniti.

**Statistika u divljini.**
**Dinosaur s urednim sažetkom.** Anscombeove je skupove trebalo sastaviti ručno,
pa je dugo ostajalo otvoreno koliko je takvih slučajeva uopće moguće. Matejka i
Fitzmaurice odgovorili su postupkom koji polazi od zadanog skupa i sitnim
pomacima točaka mijenja njegov oblik, a pritom sredine, standardne devijacije i
korelaciju drži nepromijenjenima do druge decimale (Matejka, 2017). Iz istog
sažetka tako su izveli niz oblika, među njima zvijezde, križeve i obris
dinosaura.

Dohvat nalaza vrijedi izmjeriti. Rad ne pokazuje da je korelacija nestabilna
niti da je pogrešno izračunata, jer je u svim tim skupovima ista i točna. Ono
što pokazuje jest da sažetak od nekoliko brojeva ne određuje skup podataka, pa
put od podataka do sažetka ide samo u jednom smjeru. Iz toga slijedi obveza koja
je skromnija od pouke koja se uz rad obično navodi, dakle da se uz koeficijent
prikaže i oblik iz kojeg je nastao, a ne da se koeficijent napusti.

**Pitajte model.**
Asistent može izračunati Pearsonovu i Spearmanovu korelaciju i opisati graf.
Treba mu zatražiti provjeru linearnosti, krajnjih vrijednosti, podskupina i
ograničenja raspona. Nakon odgovora valja provjeriti jesu li redovi u dvjema
varijablama ispravno upareni i je li iz povezanosti izveden nedopušten uzrok.

Tri promašaja ponavljaju se dovoljno često da ih vrijedi tražiti unaprijed.
Asistent rado veličinu koeficijenta očitava s Cohenove ljestvice bez uvjeta koji
uz nju ide (Cohen, 1988). Rado navodi korelaciju bez broja opažanja, pa se
nesigurnost procjene ne može prosuditi. I rado prelazi s opisa veze na jezik
učinka, u kojem jedna varijabla „dovodi do" druge, iako je izračunao samo
zajedničko kretanje.

> Usporedi Pearsonovu i Spearmanovu korelaciju, opiši oblik raspršenog
> dijagrama i provjeri utjecaj krajnjih opažanja. Zaključak ograniči na
> povezanost koju dizajn podupire.

**Nađite grešku.**
Na pitanje o odnosu dobi i vremena korištenja asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Korelacija u toj skupini iznosi
`r hr_broj(s6_r_uzak, 2)` uz `r s6_n_uzak` ispitanika, dakle slaba je i
pozitivna. Budući da je skupina dobno homogena i bez krajnjih vrijednosti,
procjena je čista od miješanja naraštaja, pa zaključuje da dob i vrijeme
korištenja praktički nisu povezani.

Greška je posljednja rečenica, u kojoj nalaz iz jedne dobne skupine postaje
tvrdnja o dobi uopće. Redak `filter` zadržava ispitanike unutar sedam godina
dobi i time uklanja upravo onu varijaciju dobi koja je nosila odnos, pa
homogenost skupine nije prednost procjene nego njezino ograničenje. Na cijelom
uzorku ista korelacija iznosi `r hr_broj(s6_r, 2)`. Popravak je izračunati je na
cijelom rasponu, a nalaz iz podskupine izvijestiti kao nalaz o toj podskupini.

## Razrađeni primjer

Zadatak je ispravno izvijestiti o povezanosti dviju varijabli iz simulirane
ankete, dakle dobi i dnevnog vremena korištenja društvenih mreža. Postupak ima
tri koraka i svaki od njih odgovara jednoj provjeri iz ovog poglavlja. Najprije
se pogleda oblik, zatim se izračunaju obje mjere, i tek se onda piše rečenica.

Poziv `summarise` i njegov niz glagola dolaze iz poglavlja o sažimanju podataka,
a funkcija `cor` jedina je novost i računa korelaciju dvaju stupaca, po zadanom
Pearsonovu. Argument `method` mijenja mjeru u Spearmanovu. Ovo poglavlje ne
uvodi nijedan novi obrazac čitanja koda, što je i njegova svrha, jer se ista
tri elementa pojavljuju od poglavlja o sažimanju nadalje.

Raspršeni dijagram iz odjeljka o rangovima pokazao je da veza pada strmo u
mlađim godinama i izravnava se poslije. Uz taj oblik dva koeficijenta imaju
smisla zajedno, jer Pearsonova vrijednost od `r hr_broj(s6_r, 2)` mjeri koliko
je oblak blizu pravca, a Spearmanova od `r hr_broj(s6_rs, 2)` koliko je kretanje
dosljedno silazno. Razlika među njima nije neslaganje nego opis zakrivljenosti.

Iz toga slijedi rečenica koju je dopušteno napisati. U ovom simuliranom uzorku
od `r s6_n` ispitanika dob i dnevno vrijeme korištenja povezani su negativno i
dosljedno, uz Spearmanovu korelaciju od `r hr_broj(s6_rs, 2)`, dok je veza
zakrivljena, pa je Pearsonova vrijednost od `r hr_broj(s6_r, 2)` niža. Rečenica
navodi mjeru, njezinu veličinu, broj opažanja i oblik odnosa, a ne navodi uzrok,
jer podaci dolaze iz jednokratnog mjerenja bez ikakve intervencije.

## Sažetak

Kovarijanca mjeri zajedničko odstupanje od sredina, a korelacija je ista mjera
očišćena od jedinica, pa se kreće između minus jedan i plus jedan i mjeri koliko
je oblak blizu pravca. Spearmanova inačica radi s rangovima, pa mjeri
dosljednost smjera bez zahtjeva da veza bude pravocrtna, a njihovo je
razilaženje najjeftinija dijagnostika zakrivljenosti u knjizi. Jedan broj ne
može nositi ni oblik odnosa, ni širinu raspona iz kojeg je izračunat, ni
podskupine koje ga mogu preokrenuti, i sve troje otkriva prikaz iz prethodnog
poglavlja. Iz povezanosti se ne izvodi uzrok, jer četiri različita objašnjenja
proizvode isti koeficijent, a razlikuje ih dizajn a ne izračun. Sve dosad
izračunato odnosilo se na uzorak pred nama, pa sljedeći dio knjige uvodi
vjerojatnost i pita koliko se od takvog obrasca može očekivati i kad veze nema.

## Pojmovi

kovarijanca (*covariance*), Pearsonova korelacija (*Pearson correlation*),
Spearmanova korelacija (*Spearman correlation*), monotona veza (*monotonic
relationship*), linearnost (*linearity*), matrica korelacija (*correlation
matrix*), ograničenje raspona (*range restriction*), utjecajno opažanje
(*influential observation*), konfundirajuća varijabla (*confounder*), ekološka
pogreška (*ecological fallacy*)

## Zadaci

### Konceptualni

Nacrtajte dva različita odnosa koja mogu imati sličnu Pearsonovu korelaciju, i
uz svaki napišite što bi izvještaj koji navodi samo koeficijent propustio.
Predajte skicu i objašnjenje.

### Računski

Upotrijebite tablicu korelacija koju poglavlje ispisuje za tri varijable
simulirane ankete. Za svaki od triju parova zapišite smjer veze i procijenite,
prema onome što ste vidjeli na raspršenom dijagramu dobi i minuta, bi li se
Spearmanova vrijednost razlikovala od Pearsonove i u kojem smjeru. Zatim
upotrijebite interakciju poglavlja i za svaki od četiriju oblaka zabilježite
koliko je vaša procjena promašila. Predajte tablicu sa sedam redaka i jednom
rečenicom obrazloženja u svakom. Postupak za ponavljanje izračuna nad cijelim
skupom nalazi se u praktikumu.

### Kritički

Pronađite objavljenu tvrdnju u kojoj se iz povezanosti dviju društvenih pojava
izvodi preporuka za djelovanje. Odredite koje od četiriju objašnjenja veze tekst
pretpostavlja, koju bi treću varijablu trebalo isključiti i kakav bi dizajn to
mogao učiniti. Predajte odlomak s presudom i s uvjetom pod kojim bi preporuka
bila opravdana.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte što je u pozivu ispravno
izvedeno, redak koda koji proizvodi pogrešan zaključak, mehanizam zbog kojeg
koeficijent pada, i napišite ispravljenu rečenicu izvještaja.
