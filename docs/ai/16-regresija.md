# Regresija, opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 32 min | Regresijski pravac | simulirana populacija | pogl. 6, 14 i 15 |

**Vinjeta.**
Breiman je 2001. napisao da se statističko modeliranje razdvojilo na dvije
kulture koje jedna drugu jedva primjećuju (Breiman, 2001). Jedna pretpostavlja da
podatke stvara model koji treba pogoditi i protumačiti, a druga postupak
ocjenjuje po tome koliko dobro pogađa ishode koje još nije vidjela.

Prigovor nije bio matematički. Breiman je tvrdio da prva kultura svoje modele
ocjenjuje mjerama pristajanja koje ne provjeravaju ono što obećavaju, pa
istraživač lako ostane uvjeren da je opisao mehanizam, a zapravo je opisao samo
uzorak koji ima pred sobom.

Ista jednadžba pritom služi za sve. Opisati prosječan odnos, predvidjeti ishod
za novu osobu i tvrditi da bi promjena jedne varijable promijenila drugu tri su
različita zadatka. Kako znati na koji od njih model zapravo odgovara?

## Pravac kao tvrdnja o prosjeku

Vraćamo se simuliranoj populaciji od pedeset tisuća odraslih koju su koristila
poglavlja o zaključivanju. Povjerenje u medije mjereno je na ljestvici od jedan
do deset, a zanima nas kako se ono mijenja s dobi. Poglavlje o povezanosti dalo
bi na to pitanje jedan broj o jačini veze. Model daje nešto drugo, jer imenuje
očekivano povjerenje za svaku pojedinu dob.

Cilj analize u glavnom primjeru jest konačnopopulacijski koeficijent
najmanjih kvadrata za tih pedeset tisuća zabilježenih odgovora. To je broj koji
najbolje opisuje ovu fiksnu nastavnu populaciju. Budući da su obuhvaćene sve
njezine jedinice, nema pogreške uzorkovanja ni intervala koji bi je trebao
izraziti. Brojevi iz generatora opisuju latentno pravilo prije zaokruživanja i
rezanja ljestvice. Oni nisu ciljna veličina ove analize.

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata izračunatim na svih pedeset tisuća pojedinačnih odgovora.*

Pravac na slici nije nacrtan kroz sredinu oblaka po oku. Bira ga pravilo koje
za svaku moguću kombinaciju odsječka i nagiba gleda koliko svako pojedino
opažanje promašuje, i uzima onu kombinaciju kojoj ti promašaji zajedno najmanje
teže.

**Rezidual** je razlika između opažene vrijednosti ishoda kod pojedine jedinice
i vrijednosti koju za nju predviđa model, dakle onaj dio ishoda koji model nije
objasnio.

$$e_i = y_i - \hat{y}_i$$

Oznaka $y_i$ stoji za opaženu vrijednost kod $i$-te jedinice, a $\hat{y}_i$ za
vrijednost koju model za nju predviđa, pri čemu kapica i ovdje označava
procjenu.

Zbroj samih reziduala nije upotrebljiv kao mjera promašaja, jer se pozitivna i
negativna odstupanja poništavaju, pa bi loš pravac mogao izgledati savršeno.
Kvadriranje uklanja predznak i istodobno velika odstupanja košta više nego mala,
što je razlog zbog kojeg jedno jako promašeno opažanje pomiče pravac osjetnije
od deset blago promašenih.

**Metoda najmanjih kvadrata** bira koeficijente modela tako da zbroj kvadriranih
reziduala bude najmanji mogući za zadane podatke.

Model koji taj postupak daje ima oblik koji su poglavlja o dvjema i o više
skupina već koristila. Očekivano povjerenje raste od polazne vrijednosti za
onoliko koliko nalaže nagib pomnožen s dobi, a ostatak pripada onome što model
o pojedinoj osobi ne zna.

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

Oznaka $\beta_0$ ostaje modelom sažeta vrijednost ishoda kada prediktor ima
vrijednost nula, $\beta_1$ je promjena te vrijednosti po jednoj jedinici
prediktora, a $\varepsilon_i$ je odstupanje pojedine jedinice od sažetka. U ovoj
analizi $\beta_0$ i $\beta_1$ označavaju koeficijente najmanjih kvadrata za cijelu
fiksnu populaciju, dok je rezidual $e_i$ opaženo odstupanje pojedine jedinice.
Da je pred nama uzorak, kapice bi označavale procjene tih ciljnih koeficijenata
i uz njih bi trebalo prikazati uzoračnu nesigurnost. Razlika prema poglavlju o
dvjema grupama jedino je u tome što $x_i$ sada nije oznaka skupine nego izmjeren
broj.

Konačnopopulacijski nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`. Deset godina
dobi u ovoj populaciji povezano je s razlikom od
`r hr_broj(10 * s16$nagib_jedan, 2)` boda povjerenja. Odsječak od
`r hr_broj(s16$presjek_jedan, 2)` boda odnosio bi se na osobu od nula godina,
koje u podacima nema, pa je računski potreban i sadržajno prazan. Kad se
prediktor prije procjene umanji za svoju sredinu, odsječak postane očekivani
ishod kod osobe prosječne dobi, a nagib se ne promijeni. Isti model tada ima
jedan broj manje bez značenja.

Pravac je pritom tvrdnja o prosjecima, a ne o pojedincima. Točke na slici su
prosjeci nekoliko stotina ljudi po godini dobi i leže blizu pravca, dok
pojedinačni odgovori odstupaju od njega za nekoliko bodova u oba smjera.
Rečenica da osobe od pedeset godina imaju u prosjeku više povjerenja od osoba
od trideset opisuje te prosjeke točno i ne dopušta nikakav zaključak o
konkretnoj osobi bilo koje dobi.

## Nagib koji nosi tuđu priču

Konačnopopulacijski nagib za zabilježeno povjerenje iznosi
`r hr_broj(s16$nagib_jedan, 4)` boda po godini. To je ciljna veličina ove
analize, izračunata bez pogreške uzorkovanja. Generator je prije zaokruživanja i
rezanja ishoda koristio latentni nagib od `r hr_broj(s16$latentno_dob, 3)`.
Razlika među tim brojevima nije pogreška procjene, jer oni opisuju različite
veličine. Latentni broj služi samo za pregled mehanizma kojim je nastao
zabilježeni ishod.

Razlog je u drugoj varijabli koja se mijenja zajedno s dobi. Izvor vijesti nije
jednako raspoređen po dobi, pa prosječna dob ide od
`r hr_broj(s16$dob_mreze, 1)` godine među onima koji se informiraju preko
društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među slušateljima radija.
Kako povjerenje ovisi i o izvoru, a stariji ljudi biraju izvore uz koje ide više
povjerenja, nagib uz dob pokupi i tu razliku i pripiše je godinama.

Tvrdnja se može provjeriti bez ijednog novog pojma. Ako nagib doista nosi tuđu
priču, onda bi unutar skupine ljudi koji se informiraju iz istoga izvora morao
biti manji, jer se ondje izvor više ne mijenja zajedno s dobi.

*Slika. Nagib uz dob izračunat zasebno među korisnicima svakog izvora vijesti, uz zbirni konačnopopulacijski nagib i latentno pravilo prije mjerenja. Izrada autora.*

Nijedna od pet skupina nema nagib blizu zbirnoga. Svi se kreću između
`r hr_broj(s16$nagib_unutar_min, 4)` i `r hr_broj(s16$nagib_unutar_max, 4)`, dok
je zbirni nagib veći od svakoga od njih. Njihova blizina latentnom pravilu
korisna je provjera generatora, ali ih ne pretvara u procjene toga pravila.
Ista pojava kojoj je poglavlje o povezanosti dalo ime pri usporedbi
koeficijenata unutar i između skupina ovdje se pojavljuje u modelu i pokazuje
da razlika ne dolazi iz pogreške procjene nego iz toga što se pita.

To je konfundiranje iz poglavlja o mjerenju, sada u obliku broja umjesto
dijagrama. Koeficijent uz dob odgovara na pitanje koliko se povjerenje razlikuje
među ljudima različite dobi, a ne koliko bi se promijenilo kod jedne osobe koja
stari. Prvo je pitanje o usporedbi skupina i model na njega odgovara točno.
Drugo je pitanje o promjeni i na njega nije ni odgovarao.

Vrijedi zadržati da razlika nema veze s količinom podataka. Model obuhvaća svih
pedeset tisuća ljudi, pa je ciljna konačnopopulacijska vrijednost poznata i nema
uzoračne nesigurnosti. Kad bi se iz te populacije izvukao uzorak, trebalo bi
procijeniti isti cilj i prikazati nesigurnost koja odgovara nacrtu uzorkovanja.
Ni tada interval ne bi mjerio udaljenost od latentnog pravila prije mjerenja.

## Prilagodba i ono što je čini mogućom

Ako opažena povezanost miješa dvije priče, izlaz je usporediti ljude koji se u
drugoj od njih ne razlikuju. Umjesto da se uzorak reže na skupine iste dobi i
istog izvora, model to radi računski, procjenjujući sve koeficijente odjednom.

**Višestruka regresija** procjenjuje povezanost svakog prediktora s ishodom pri
jednakim vrijednostima svih ostalih prediktora u modelu, pa je svaki koeficijent
usporedba jedinica koje se razlikuju po tom prediktoru, a po ostalima ne.

Model s dobi i izvorom vijesti daje uz dob nagib od
`r hr_broj(s16$nagib_dva, 4)`. To je konačnopopulacijski odgovor na prilagođeno
pitanje, a ne procjena latentnog pravila. Broj je blizak latentnom pravilu od
`r hr_broj(s16$latentno_dob, 3)`, što je zasebna provjera poznatog generatora,
ali ta blizina ne određuje je li koeficijent ispravan.

*Slika. Konačnopopulacijski koeficijenti izvora vijesti uz jednaku dob, uz latentna pravila prije mjerenja. Portal je referentna skupina. Izrada autora.*

Stupci namjerno ne nose ista imena. Latentna pravila pripadaju ishodu prije
bilježenja, a koeficijenti pripadaju zabilježenoj ljestvici od jedan do deset.
U ovom su skupu potonji brojevi blago manji jer su vrijednosti zaokružene i
odrezane na krajevima ljestvice. Latentni broj zato nije vrijednost koju model
zabilježenog ishoda mora dosegnuti.

Blizina dvaju stupaca nije potvrda postupka. Vidimo je jer poznajemo generator i
jer su obje varijable koje su sudjelovale u nastanku povjerenja izmjerene. Da
izvor vijesti nije zabilježen, koeficijent uz dob ostao bi na
`r hr_broj(s16$nagib_jedan, 4)` i ništa u ispisu ne bi upozorilo da taj broj
odgovara drugom, neprilagođenom pitanju.

Izraz „uz kontrolu" zato opisuje račun, a ne postupak. Kontrola u pokusu znači
da je istraživač sam dodijelio uvjete, pa se skupine ne razlikuju ni po čemu
drugome, uključujući ono što nikome nije palo na pamet izmjeriti. Kontrola u
modelu znači da su uspoređene jedinice s jednakim vrijednostima onih varijabli
koje su ušle u model.

Iz toga slijedi oblik rečenice koji svaki koeficijent zaslužuje. Uz jednak izvor
vijesti, ljudi stariji za deset godina imaju u prosjeku
`r hr_broj(10 * s16$nagib_dva, 2)` boda više povjerenja. Rečenica navodi jedinicu
prediktora, jedinicu ishoda i uvjet pod kojim usporedba vrijedi, i bez ijednog
od ta tri dijela koeficijent se ne može provjeriti. Ista se disciplina traži i
od kategorijskih koeficijenata, gdje uvjet uključuje i referentnu skupinu prema
kojoj se svaki od njih mjeri.

Odsječak u takvom modelu ostaje formalno potreban i sadržajno još slabiji nego
prije, jer sada opisuje osobu od nula godina koja se informira putem portala.
Model se time ne kvari. Kvari se samo pokušaj da se svaki broj iz ispisa
protumači kao da nešto opisuje.

Postoji i slučaj u kojem prilagodba ne uspijeva iako su sve varijable izmjerene.
Kad dva prediktora nose gotovo istu informaciju, podaci ne sadrže usporedbe u
kojima se jedan mijenja a drugi ne, pa se njihovi pojedinačni doprinosi ne mogu
razdvojiti i koeficijenti postaju osjetljivi na male promjene uzorka. Zbroj tih
prediktora model i dalje koristi jednako dobro, a pitanje o svakome od njih
zasebno u tim podacima nema odgovor.

## Interakcija — Regresijski pravac

Sljedeći prikaz razdvaja dvije stvari koje su u prethodna tri odjeljka
ispisane kao gotov rezultat. Čitatelj sam pomiče pravac i vidi kako zbroj
kvadrata reagira na svaki pomak, a zatim uključuje treću varijablu i uspoređuje
zbirni nagib s onim koji vrijedi pri njezinoj jednakoj vrijednosti. Podaci su
manji i posebno konstruirani za ovaj prikaz, kako bi se pojedini reziduali
mogli vidjeti.

*Slika. Regresijski pravac — pomični pravac, reziduali i usporedba zbirnog s prilagođenim nagibom.*

**Što isprobati.**

1. Mijenjajte odsječak i nagib dok se zbroj kvadrata ne približi prikazanom
   minimumu.
2. Povećajte samo nagib za jednu jedinicu i pratite koji se reziduali najviše
   produljuju.
3. Uključite model s prethodnim interesom i usporedite njegov nagib sa zbirnim
   pravcem.

Zbroj kvadrata oko svojeg minimuma reagira sporo, pa se pravac može osjetno
pomaknuti prije nego što se brojka vidljivo pokvari. Kad podaci dolaze iz
uzorka, ta je geometrija jedan dio računanja intervala za odabranu ciljnu
veličinu. Widget sam ne daje zaključak o uzoračnoj nesigurnosti.

## Isti model iza ranijih poglavlja

Poglavlje o dvjema grupama zapisalo je usporedbu dviju sredina kao model s
binarnim prediktorom, a poglavlje o više skupina proširilo ga je na četiri
koeficijenta. Ovdje je isti model dobio prediktor koji je broj, čime je popis
slučajeva zatvoren. Vrijedi provjeriti da to nije bila samo tvrdnja o zapisu.

Uzorak od sto dvadeset ljudi iz poglavlja o dvjema grupama daje razliku sredina
od `r hr_broj(s16$razlika_dvije, 2)` boda. Koeficijent uz izvor u modelu iznosi
`r hr_broj(s16$koef_dvije, 2)`. To je točna jednakost dvaju načina zapisivanja
iste točkaste procjene.

Omjer koeficijenta i obične homoskedastične standardne pogreške iznosi
`r hr_broj(s16$t_dvije, 2)`. Jednak je združenom Studentovu t-testu, koji u kodu
izričito postavlja `var.equal = TRUE`, pa oba računa pretpostavljaju jednu
zajedničku rezidualnu varijancu i imaju
`r hr_broj(s16$df_student_dvije, 0)` stupnjeva slobode. Welchov zadani postupak
iz poglavlja o dvjema grupama dopušta različite varijance. Na istim podacima
daje t od `r hr_broj(s16$t_welch_dvije, 2)` i
`r hr_broj(s16$df_welch_dvije, 3)` stupnja slobode. Točkasta procjena ostaje
ista, ali inferencija nije isti račun.

Uzorak od tristo ljudi iz poglavlja o više skupina daje ukupni test s
F-vrijednošću `r hr_broj(s16$f_pet, 2)` uz `r s16$df1_pet` i `r s16$df2_pet`
stupnja slobode. To je klasična homoskedastična analiza s jednom rezidualnom
varijancom, ista kao prikazani `aov` u poglavlju o više skupina. Welchov račun
na istim podacima daje F od `r hr_broj(s16$f_welch_pet, 2)` uz
`r hr_broj(s16$df1_welch_pet, 0)` i
`r hr_broj(s16$df2_welch_pet, 1)` stupnjeva slobode. Zajednički model sredina ne
pretvara te dvije procedure nesigurnosti u isti test. Udio objašnjene
varijabilnosti u klasičnom modelu iznosi
`r hr_broj(100 * s16$r2_pet, 1)` %, a to je ista brojka koju je poglavlje o više
skupina nazvalo eta-kvadratom.

Iz toga slijedi praktična posljedica za čitanje tuđih radova. Rad koji
izvještava o t-testu, rad koji izvještava o analizi varijance i rad koji
izvještava o regresiji mogu polaziti od zajedničkog modela sredina, pa se čitaju
istim pitanjima o jedinici analize, o tome što je uspoređeno i uz što je
usporedba provedena. Zatim se zasebno provjerava kako je izračunata nesigurnost
i je li pretpostavljena zajednička ili skupinama svojstvena varijanca.

Ista posljedica vrijedi i za odabir postupka. Tablica koja vodi od vrste
podataka i pitanja do metode, kakva stoji u dodatku o odabiru testa, pomaže dok
se uči, a njezini redovi često polaze od različitih oblika zajedničkog modela.
Pitanja koja ostaju jesu što je ishod, što su prediktori, jesu li jedinice
neovisne i kako treba prikazati nesigurnost. Sam oblik modela ne odlučuje između
Welchove i obične homoskedastične inferencije.

Okvir se pritom širi dalje nego što ova knjiga ide. Ishod koji nije broj nego
kategorija, mjerenja ponovljena na istim ljudima i podaci grupirani po
razredima ili gradovima traže preinake koje pripadaju literaturi izvan opsega
ovog udžbenika. Zajedničko im je da se i dalje piše model, imenuje ishod i
imenuju prediktori, pa čitatelj koji je razumio ovo poglavlje takav rad može
čitati i kad njegovu procjenu ne bi znao ponoviti.

## Pristajanje i njegove granice

Koliko dobro model opisuje podatke mjeri se udjelom varijabilnosti ishoda koji
je model uspio objasniti. Ta mjera nosi ime koje obećava više nego što daje, pa
je vrijedi definirati oprezno.

**Koeficijent determinacije** je udio ukupne varijabilnosti ishoda u promatranom
skupu podataka koji je model objasnio, izračunat kao jedan minus omjer zbroja
kvadrata reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Model samo s dobi objašnjava `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti
povjerenja, a model s dobi i izvorom `r hr_broj(100 * s16$r2_dva, 1)` %. Obje su
brojke male, a model s izvorom istodobno opisuje prilagođeni odnos u ovoj
konačnoj populaciji i leži blizu latentnoga pravila generatora. Te dvije veličine
ipak nisu iste. Ljudi se međusobno razlikuju iz mnoštva razloga koje nijedno
istraživanje ne bilježi, pa niska vrijednost ovdje ne znači loš model nego da su
ljudi raznoliki.

Vrijednost ima i mehaničko svojstvo koje je čini neupotrebljivom za usporedbu
modela. Nikada ne pada kad se doda prediktor, pa i onaj koji s ishodom nema
nikakve veze podigne ju za nešto. U uzorku od dvjesto osoba dodavanje pet
potpuno slučajnih brojeva podiže udio objašnjene varijabilnosti s
`r hr_broj(100 * s16$r2_bez, 1)` % na `r hr_broj(100 * s16$r2_sa, 1)` %, dok
prilagođeni koeficijent determinacije, koji kažnjava svaki dodani prediktor,
pada s `r hr_broj(100 * s16$prilagodeni_bez, 1)` % na
`r hr_broj(100 * s16$prilagodeni_sa, 1)` %. Prvi broj tvrdi da je model bolji,
drugi da je gori, i drugi je u pravu.

Postoji i druga strana iste mehanike, po kojoj vrijednost pada iako se odnos ne
mijenja. Ograničimo li populaciju na ljude između trideset i pedeset godina,
nagib uz dob ostaje `r hr_broj(s16$nagib_usko, 4)`, praktički kao prije, a udio
objašnjene varijabilnosti pada s `r hr_broj(100 * s16$r2_jedan, 1)` % na
`r hr_broj(100 * s16$r2_usko, 1)` % na `r hr_broj(s16$n_usko, 0)` ljudi.
Ograničenje raspona iz poglavlja o povezanosti radi i ovdje, jer je udio
objašnjenoga svojstvo skupa podataka koji je ušao u analizu, a ne odnosa među
varijablama.

Zbog toga usporedba te mjere među radovima gotovo nikada ništa ne znači.
Istraživanje na cijeloj populaciji i istraživanje na uskoj dobnoj skupini mogu
naći potpuno isti odnos i izvijestiti o vrijednostima koje se razlikuju šest
puta. Broj koji se uspoređuje jest procijenjeni koeficijent sa svojim
intervalom, jer je jedini izražen u jedinicama koje su u oba rada iste.

Pristajanje pritom ništa ne govori o tome gdje model griješi, a to se vidi tek
kad se reziduali pogledaju nasuprot vrijednostima koje model predviđa. Vrijeme
provedeno uz medije u ovoj populaciji raste s dobi za
`r hr_broj(s16$nagib_minute, 2)` minute po godini, i taj je pravac sasvim
razuman, ali njegovi reziduali nisu jednako raspršeni po cijelom rasponu.

*Slika. Reziduali modela za dnevno vrijeme uz medije nasuprot vrijednostima koje model predviđa, na slučajnom podskupu od dvije tisuće osoba.*

Raspršenost reziduala raste sa `r hr_broj(s16$rasprsenost_dolje, 0)` minuta u
šestini s najnižim predviđanjima na `r hr_broj(s16$rasprsenost_gore, 0)` u
šestini s najvišima. Model je time u jednom dijelu raspona precizniji nego u
drugome, pa jedna zajednička mjera nesigurnosti za sve vrijedi u prosjeku i ni
za koga posebno. Prikaz reziduala kaže gdje model ne pristaje, a ne što s tim
učiniti, i ta razlika između nalaza i odluke ostaje na istraživaču.

## Objašnjenje i predviđanje

Dva zadatka koje ista jednadžba obavlja razlikuju se po tome što od modela
traže. Objašnjenje traži koeficijent koji odgovara nekom stvarnom odnosu, a
predviđanje traži malu pogrešku na jedinicama koje model nije vidio. Shmueli je
pokazala da se ta dva cilja razilaze već u izboru varijabli i mjera, pa model
koji je bolji za jedno može biti lošiji za drugo (Shmueli, 2010).

Prediktivni primjeri u ovom odjeljku imaju istu vremensku granicu. Povjerenje
treba predvidjeti za novu osobu neposredno prije nego što ona odgovori na pitanje
o povjerenju. Dob i izvor vijesti tada su dostupni. Umjetni slučajni stupci u
primjeru prekomjernog pristajanja također su zapisani prije te granice i postoje
u istom obliku za skup učenja i odvojeni skup, premda ne nose korisnu
informaciju. Sve što nastaje nakon odgovora o povjerenju isključeno je.

Razilaženje počinje već kod izbora varijabli. Spremnost na plaćanje vijesti u
ovoj populaciji nastaje pod utjecajem povjerenja, dakle nakon ishoda koji se
modelira. Kao prediktor povjerenja ipak radi, jer podiže udio objašnjene
varijabilnosti s `r hr_broj(100 * s16$r2_dva, 1)` % na
`r hr_broj(100 * s16$r2_posljedica, 1)` % i smanjuje preostalu raspršenost. Za
odabranu vremensku granicu to nije prediktivni dobitak nego curenje cilja.
Spremnost na plaćanje još ne postoji kad predviđanje treba nastati, pa takav
model ne bi mogao proizvesti valjano predviđanje za novu osobu.

Razlika se dalje ne vidi dok se model ocjenjuje na podacima na kojima je
procijenjen. Vidi se čim se podaci razdvoje na skup na kojem model uči i skup
koji je odvojen prije nego što je model postavljen. Oba modela u tablici koriste
samo prediktore dostupne do iste vremenske granice.

*Slika. Prosječna pogreška predviđanja dvaju modela na podacima na kojima su procijenjeni i na odvojenom skupu, u bodovima povjerenja. Izrada autora.*

Bogatiji model objašnjava `r hr_broj(100 * s16$r2_bogat, 1)` % varijabilnosti u
`r s16$n_ucenje` osoba na kojima je procijenjen, prema
`r hr_broj(100 * s16$r2_skroman, 1)` % kod skromnijeg, i na tim podacima griješi
manje. Na `r s16$n_provjera` osoba koje nije vidio griješi više od skromnijeg
modela i više nego postupak koji svakome pripiše prosjek skupa za učenje. Model
je naučio raspored slučajnih brojeva u svojem uzorku i taj raspored u novim
podacima ne postoji.

Skromniji model pritom nije samo bolji od bogatijeg nego je blizu najboljega što
je na ovim podacima uopće moguće. Povjerenje se u populaciji raspršuje sa
standardnom devijacijom `r hr_broj(s16$sd_ishoda, 2)` boda, a nakon što model
uzme u obzir dob i izvor ostaje raspršenost od `r hr_broj(s16$sd_ostatka, 2)`.
Ta je preostala raspršenost u populaciju ugrađena kao slučajni dio ishoda i
nijedan je model ne može ukloniti, pa je pogreška predviđanja odozdo ograničena
bez obzira na to koliko se varijabli doda.

Za istraživanje iz toga slijedi jedno pravilo. Tvrdnja o predviđanju provjerava
se na podacima koji u procjeni nisu sudjelovali i smije koristiti samo
informacije dostupne u trenutku primjene. Prvi uvjet sprječava da model ocjenjuje
sam sebe, a drugi curenje podataka iz budućnosti. Poglavlje o algoritmima na toj
razlici gradi cijeli argument, budući da postupci koji odlučuju o kreditima,
sadržaju i rangiranju svoju vrijednost mjere uspješnošću na jedinicama koje još
nisu viđene.

## Granica prema uzroku

Poglavlje o mjerenju uvelo je konfundirajuću varijablu kao razlog zbog kojeg
opažena veza ne dokazuje uzrok, i obećalo da će se pitanje vratiti kad za njega
bude postojao račun. Račun sada postoji i vrijedi biti precizan o tome što je
njime dobiveno.

Uz izvor vijesti u modelu, konačnopopulacijski koeficijent uz dob približio se
latentnom pravilu po kojem je ishod nastao prije mjerenja. To slaganje nije
ciljna veličina analize ni dokaz postupka. Vidimo ga zato što je generator
poznat, pa se znalo koje dvije varijable treba uključiti. Stvarno istraživanje
tu informaciju nema, i nijedan ispis modela ne razlikuje slučaj u kojem su svi
važni čimbenici izmjereni od slučaja u kojem nisu.

Prilagođena povezanost zato nije uzročni učinak nego usporedba pod uvjetom
uključenih varijabli. Da bi postala uzročna tvrdnja, potrebno je znati da je
uzrok prethodio ishodu, da su svi čimbenici koji djeluju na oboje izmjereni i
da nijedna uključena varijabla nije posljedica pretpostavljenog uzroka.
Posljednji uvjet je najmanje poznat, jer prilagodba za posljedicu uzroka može
uvesti pristranost ondje gdje je prije nije bilo.

Ta tri uvjeta nisu statistička nego sadržajna, pa se o njima raspravlja prije
podataka. Za pitanje o dobi i povjerenju prvi je uvjet trivijalno zadovoljen,
drugi ovisi o tome je li išta osim izvora vijesti povezano i s dobi i s
povjerenjem, a treći traži provjeru da izvor vijesti nije nešto što ljudi biraju
zbog razine povjerenja koju već imaju. Ovdje je i taj posljednji odgovor poznat,
jer generator izvor određuje prije povjerenja. U stvarnom istraživanju o tom bi
se redoslijedu raspravljalo, a ne računalo.

Odatle slijedi i skromnost u jeziku. Model daje razliku između usporedivih
skupina, i tu rečenicu treba napisati doslovno tako. Rečenica o tome što bi se
dogodilo da se nešto promijeni pripada dizajnu koji tu promjenu doista provodi
ili opravdava, a to je pitanje poglavlja o mjerenju i dizajnu, ne poglavlja o
modelima.

Postoji koristan test koji ne traži nikakav račun. Prije nego što se koeficijent
opiše kao učinak, napiše se rečenica o tome što bi se moralo dogoditi da tvrdnja
bude pogrešna, i provjeri se može li ijedan podatak iz istraživanja tu rečenicu
opovrgnuti. Ako odgovor ovisi isključivo o pretpostavci koju podaci ne dodiruju,
tvrdnja je pretpostavka napisana kao nalaz.

**Statistika u divljini.**
**Druga tablica.** Westreich i Greenland opisali su uobičajen postupak u kojem
autor u jednoj tablici prikaže sve koeficijente višestrukog modela, s
koeficijentom glavne varijable i koeficijentima kontrola jedan ispod drugoga
(Westreich, 2013). Tvrde da takva tablica potiče čitatelja da svaki redak
protumači kao učinak varijable iz tog retka, iako uvjeti pod kojima to vrijedi
ne mogu biti ispunjeni za sve retke istodobno.

Razlog je u tome što je model postavljen s obzirom na jednu varijablu. Skup
kontrola izabran je tako da usporedba po njoj bude poštena, a za neku od tih
kontrola isti skup u pravilu nije prikladan, jer među preostalim varijablama
može biti i posljedica te kontrole. Tablica pritom izgleda jednako uredno u oba
slučaja. Rad koji uz nju napiše da su svi navedeni čimbenici povezani s ishodom
ostaje točan, a rad koji svaki redak pretvori u učinak izrekao je nekoliko
tvrdnji za koje njegov dizajn jamči samo jednu.

**Pitajte model.**
Asistent pouzdano prilagodi model, izradi dijagnostičke prikaze i prevede
koeficijente u prozu. Prije poziva treba mu zadati ulogu svake varijable,
referentne kategorije, ciljnu veličinu i cilj analize, jer isti podaci uz isti kod
daju različit model ovisno o tome je li pitanje opisno, prediktivno ili uzročno.
Za prediktivni cilj treba mu zadati i trenutak primjene. Provjeravamo četiri
stvari.
Prva je tumači li koeficijent u izvornim jedinicama i uz uvjet ostalih
varijabli, umjesto da ga opiše kao učinak. Druga je predlaže li skup kontrola
prema pitanju, umjesto prema tome koje su varijable pri ruci. Treća je koristi
li u predviđanju samo informacije dostupne do trenutka primjene. Četvrta je
ocjenjuje li predikciju na podacima koji su sudjelovali u procjeni.

> Prilagodi model i protumači koeficijent glavne varijable u izvornim
> jedinicama, s mjerom nesigurnosti koja odgovara ciljnoj veličini i nacrtu. Za
> svaku kontrolu napiši zašto je u modelu i može li biti posljedica glavne
> varijable.
> Imenuj trenutak predviđanja, isključi poslijeishodne podatke i predikciju
> ocijeni na odvojenom skupu.

**Nađite grešku.**
Na traženje da procijeni koliko dobro model predviđa povjerenje kod novih
korisnika asistent je priložio ovaj račun. U zamišljenoj primjeni sve navedene
varijable zabilježene su prije odgovora o povjerenju, pa je vremenska granica
zadovoljena.

Uz ispis je napisao obrazloženje. Model objašnjava osjetno veći udio
varijabilnosti nego prethodni, a prosječna pogreška iznosi manje od dva boda
na ljestvici od jedan do deset. Iz toga zaključuje da model dovoljno pouzdano
predviđa povjerenje kod korisnika koje nije vidio i preporučuje ga za primjenu
na novim podacima.

## Razrađeni primjer

Ponavljamo cijeli argument na jednom mjestu i u obliku u kojem bi se pojavio u
izvještaju. Pitanje je kako se povjerenje u medije mijenja s dobi, a analiza
daje dva odgovora ovisno o tome uspoređuju li se svi ljudi ili samo oni koji se
informiraju iz istog izvora. Ciljne su veličine u oba slučaja koeficijenti
najmanjih kvadrata za zabilježene odgovore svih pedeset tisuća ljudi.

Funkcija `lm` ovdje izračunava opisne koeficijente iz cijele konačne populacije.
Nijedna jedinica nije uzorkovana, pa uz te brojeve nema uzoračne nesigurnosti.
Funkcija `confint` zato se ne poziva. Njezin uobičajeni interval odnosio bi se na
drugi, modelni ili nadpopulacijski cilj koji ovo poglavlje nije odabralo.

*Slika. Konačnopopulacijski nagib uz dob u dvama modelima za zabilježeni ishod. Izrada autora.*

Razlika među nagibima nije stvar uzoračne nepreciznosti. Oba su poznata točno za
ovu populaciju, ali odgovaraju na različita pitanja. Zbirni nagib miješa dob s
izborom izvora, a prilagođeni uspoređuje ljude koji se informiraju iz istog
izvora. Izvještaj koji bi naveo samo prvi broj ne bi sadržavao nijednu netočnu
rečenicu o podacima i svejedno bi zamaglio razliku između tih pitanja.

Zaključak se zato piše u dva dijela. Ljudi različite dobi razlikuju se u
povjerenju za `r hr_broj(10 * s16$nagib_jedan, 2)` boda po desetljeću, a među
ljudima koji se informiraju iz istog izvora ta razlika iznosi
`r hr_broj(10 * s16$nagib_dva, 2)` boda. Prva rečenica opisuje populaciju kakva
jest, druga izdvaja dob od izbora izvora, i tek zajedno kažu ono što je model
doista našao.

Izvještaj uz to mora reći što je izostavljeno. Model sadrži dvije varijable, a
povjerenje u medije ovisi i o obrazovanju, iskustvu s pojedinim redakcijama i
političkim sklonostima, koje ovdje nisu ni izmjerene. Nijedna od njih ne bi
promijenila to da je opisana usporedba točna, i svaka od njih mogla bi
promijeniti veličinu razlike koja ostaje kad se izjednače.

Ostaje i pitanje na koje ova analiza uopće nije odgovarala. Nijedna od dviju
rečenica ne kaže da bi se povjerenje neke osobe promijenilo time što ona
ostari, ni da bi se promijenilo time što promijeni izvor vijesti. Analiza
opisuje kako izgleda populacija u jednom trenutku, a promjena kod iste osobe
kroz vrijeme zahtijeva podatke koji istu osobu prate, kojih ovdje nema.

## Sažetak

Linearni model povezuje ishod s prediktorima kroz očekivane vrijednosti i
reziduale, a metoda najmanjih kvadrata bira koeficijente po jasnom kriteriju
koji se u widgetu može vidjeti kako radi. Više prediktora daje povezanosti pri
jednakim vrijednostima ostalih varijabli. Koeficijenti za cijelu konačnu
populaciju opisuju zabilježeni ishod bez uzoračne nesigurnosti i nisu latentni
parametri generatora. Udio objašnjene varijabilnosti raste i kad se doda čista
buka, pa pristajanje nije ocjena, dok reziduali pokazuju gdje model ne odgovara
podacima. Objašnjenje i predviđanje odatle se razdvajaju, jer se drugo provjerava
na jedinicama koje model nije vidio i samo s informacijama dostupnima u trenutku
primjene. Sljedeće poglavlje uzima taj kriterij ozbiljno i pita što se događa kad
postupci koji ga zadovoljavaju počnu odlučivati o ljudima.

## Pojmovi

linearna regresija (*linear regression*), rezidual (*residual*), metoda
najmanjih kvadrata (*least squares*), koeficijent determinacije (*R-squared*),
višestruka regresija (*multiple regression*), prilagođena povezanost
(*adjusted association*), predviđanje izvan uzorka (*out-of-sample
prediction*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto se nagib uz dob mijenja kada u model uđe izvor
vijesti, a nijedan podatak o dobi pritom nije promijenjen. Imenujte pitanje na
koje odgovara svaki od dvaju nagiba.

### Računski

Poglavlje navodi da je zbirni nagib `r hr_broj(s16$nagib_jedan, 4)` boda po
godini. Izračunajte očekivanu razliku u povjerenju između osobe od 25 i osobe od
55 godina prema tom modelu, a zatim isti račun ponovite s prilagođenim nagibom
`r hr_broj(s16$nagib_dva, 4)`. Predajte obje brojke i jednu rečenicu o tome koja
od njih odgovara na pitanje o dvjema stvarnim osobama iz ove populacije.

### Kritički

Pronađite objavljeni rad ili novinski članak koji uz koeficijent iz višestrukog
modela navodi da je nešto „utjecalo" na ishod. Prosudite ga prema pitanju koje
tablica koeficijenata potiče, a dizajn ne pokriva (Westreich, 2013). Predajte
kratku bilješku s popisom varijabli za koje bi taj koeficijent bio ispravno
protumačen i onih za koje ne bi.

### Revizija modela

Ocijenite račun i zaključak iz okvira o pogrešci. Imenujte što je u kodu
ispravno, redak u kojem se pogreška događa, razlog zbog kojeg obje priložene
brojke izgledaju uvjerljivo i napišite zaključak koji bi isti ispis podnio.
Objasnite i zašto pogreška nije curenje iz budućnosti u zadanoj vremenskoj
granici, nego pogrešna provjera na skupu za učenje.
