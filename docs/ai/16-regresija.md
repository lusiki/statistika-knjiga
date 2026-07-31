# Regresija, opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

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

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata procijenjenim na svih pedeset tisuća pojedinačnih odgovora.*

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

Oznaka $\beta_0$ ostaje očekivani ishod kada prediktor ima vrijednost nula,
$\beta_1$ je promjena očekivanog ishoda po jednoj jedinici prediktora, a
$\varepsilon_i$ je odstupanje pojedine jedinice od tog očekivanja. Ta se oznaka
odnosi na model, a rezidual $e_i$ na ono što od nje vidimo nakon što su
koeficijenti procijenjeni, pa je jedno pretpostavka o svijetu, a drugo mjerljiva
posljedica procjene. Razlika prema poglavlju o dvjema grupama je jedino u tome
što $x_i$ sada nije oznaka skupine nego izmjeren broj.

Procijenjeni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`, što znači da je deset
godina dobi u ovoj populaciji povezano s razlikom od
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

Populacija je simulirana, pa se zna po kojem je pravilu nastala. Povjerenje u
njoj raste s dobi za točno `r hr_broj(s16$istina_dob, 3)` boda po godini, a
procijenjeni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`. Procjena je za
trećinu veća od vrijednosti koju procjenjuje, i to nije pogreška uzorkovanja jer
je model procijenjen na cijeloj populaciji.

Razlog je u drugoj varijabli koja se mijenja zajedno s dobi. Izvor vijesti nije
jednako raspoređen po dobi, pa prosječna dob ide od
`r hr_broj(s16$dob_mreze, 1)` godine među onima koji se informiraju preko
društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među slušateljima radija.
Kako povjerenje ovisi i o izvoru, a stariji ljudi biraju izvore uz koje ide više
povjerenja, nagib uz dob pokupi i tu razliku i pripiše je godinama.

Tvrdnja se može provjeriti bez ijednog novog pojma. Ako nagib doista nosi tuđu
priču, onda bi unutar skupine ljudi koji se informiraju iz istoga izvora morao
biti manji, jer se ondje izvor više ne mijenja zajedno s dobi.

*Slika. Nagib uz dob procijenjen zasebno među korisnicima svakog izvora vijesti, uz zbirni nagib i vrijednost ugrađenu u generator populacije. Izrada autora.*

Nijedna od pet skupina nema nagib blizu zbirnoga. Svi se kreću između
`r hr_broj(s16$nagib_unutar_min, 4)` i `r hr_broj(s16$nagib_unutar_max, 4)`, oko
vrijednosti koja je u populaciju ugrađena, dok je zbirni nagib veći od svakoga
od njih. Ista pojava kojoj je poglavlje o povezanosti dalo ime pri usporedbi
koeficijenata unutar i između skupina ovdje se pojavljuje u modelu, i pokazuje
da razlika ne dolazi iz podataka nego iz toga što se pita.

To je konfundiranje iz poglavlja o mjerenju, sada u obliku broja umjesto
dijagrama. Koeficijent uz dob odgovara na pitanje koliko se povjerenje razlikuje
među ljudima različite dobi, a ne koliko bi se promijenilo kod jedne osobe koja
stari. Prvo je pitanje o usporedbi skupina i model na njega odgovara točno.
Drugo je pitanje o promjeni i na njega nije ni odgovarao.

Vrijedi zadržati da razlika nema veze s količinom podataka. Model je procijenjen
na svih pedeset tisuća ljudi, pa nikakvo povećanje uzorka zbirni nagib ne bi
pomaknulo prema vrijednosti koju je generator ugradio. Veći uzorak sužava
interval oko krive vrijednosti, i to je razlog zbog kojeg se preciznost i
točnost u izvještaju nikada ne miješaju.

## Prilagodba i ono što je čini mogućom

Ako opažena povezanost miješa dvije priče, izlaz je usporediti ljude koji se u
drugoj od njih ne razlikuju. Umjesto da se uzorak reže na skupine iste dobi i
istog izvora, model to radi računski, procjenjujući sve koeficijente odjednom.

**Višestruka regresija** procjenjuje povezanost svakog prediktora s ishodom pri
jednakim vrijednostima svih ostalih prediktora u modelu, pa je svaki koeficijent
usporedba jedinica koje se razlikuju po tom prediktoru, a po ostalima ne.

Model s dobi i izvorom vijesti daje uz dob nagib od
`r hr_broj(s16$nagib_dva, 4)`, praktički onu vrijednost koja je u populaciju i
ugrađena. Uspoređujući ljude koji se informiraju iz istog izvora, model je
oporavio pravilo po kojem su podaci nastali.

*Slika. Procijenjeni učinci izvora vijesti uz jednaku dob, uz vrijednosti ugrađene u generator populacije. Portal je referentna skupina. Izrada autora.*

Procjene su blago manje od ugrađenih vrijednosti, i to nije slučajnost.
Povjerenje je u populaciji zaokruženo na cijeli broj i odrezano na krajevima
ljestvice, pa mjerenje gubi dio razlika koje generator proizvodi. Isti se učinak
javlja u svakom istraživanju s ljestvicom od nekoliko stupnjeva, gdje grubo
mjerilo procjene sustavno vuče prema nuli.

Slaganje u tablici izgleda kao potvrda da postupak radi, i jest, ali samo pod
uvjetom koji se u stvarnom istraživanju nikada ne može provjeriti. Model je
pogodio jer su obje varijable koje su sudjelovale u nastanku povjerenja i
izmjerene. Da izvor vijesti nije zabilježen, koeficijent uz dob ostao bi na
`r hr_broj(s16$nagib_jedan, 4)` i ništa u ispisu ne bi upozorilo da je pogrešan.

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
pomaknuti prije nego što se brojka vidljivo pokvari. To je ista činjenica koju
poglavlje o procjeni izražava intervalom, jer sve te bliske vrijednosti nagiba
podaci podnose gotovo jednako dobro.

## Isti model iza ranijih poglavlja

Poglavlje o dvjema grupama zapisalo je usporedbu dviju sredina kao model s
binarnim prediktorom, a poglavlje o više skupina proširilo ga je na četiri
koeficijenta. Ovdje je isti model dobio prediktor koji je broj, čime je popis
slučajeva zatvoren. Vrijedi provjeriti da to nije bila samo tvrdnja o zapisu.

Uzorak od sto dvadeset ljudi iz poglavlja o dvjema grupama daje razliku sredina
od `r hr_broj(s16$razlika_dvije, 2)` boda. Koeficijent uz izvor u modelu iznosi
`r hr_broj(s16$koef_dvije, 2)`, a omjer tog koeficijenta i njegove standardne
pogreške iznosi `r hr_broj(s16$t_dvije, 2)`, jednako kao vrijednost koju daje
t-test na istim podacima. Riječ je o jednom računu s dva imena.

Uzorak od tristo ljudi iz poglavlja o više skupina daje ukupni test s
F-vrijednošću `r hr_broj(s16$f_pet, 2)` uz `r s16$df1_pet` i `r s16$df2_pet`
stupnja slobode, što je vrijednost koju je to poglavlje ispisalo. Udio
objašnjene varijabilnosti u tom modelu iznosi
`r hr_broj(100 * s16$r2_pet, 1)` %, a to je ista brojka koju je poglavlje o više
skupina nazvalo eta-kvadratom.

Iz toga slijedi praktična posljedica za čitanje tuđih radova. Rad koji
izvještava o t-testu, rad koji izvještava o analizi varijance i rad koji
izvještava o regresiji ne koriste tri različita aparata, pa se mogu čitati istim
pitanjima o jedinici analize, o tome što je uspoređeno i uz što je usporedba
provedena.

Ista posljedica vrijedi i za odabir postupka. Tablica koja vodi od vrste
podataka i pitanja do metode, kakva stoji u dodatku o odabiru testa, pomaže dok
se uči, a njezini redovi nisu odvojeni postupci nego različiti oblici jednog
istog modela. Pitanje koje ostaje jest što je ishod, što su prediktori i jesu li
jedinice neovisne, a ime testa iz tih odgovora slijedi.

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
uzorku koji je model objasnio, izračunat kao jedan minus omjer zbroja kvadrata
reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Model samo s dobi objašnjava `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti
povjerenja, a model s dobi i izvorom `r hr_broj(100 * s16$r2_dva, 1)` %. Obje su
brojke male, a model s izvorom je istodobno onaj koji je oporavio pravilo po
kojem su podaci nastali. Ljudi se međusobno razlikuju iz mnoštva razloga koje
nijedno istraživanje ne bilježi, pa niska vrijednost ovdje ne znači loš model
nego da su ljudi raznoliki.

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
objašnjenoga svojstvo uzorka koji je ušao u analizu, a ne odnosa među
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

Razilaženje počinje već kod izbora varijabli. Spremnost na plaćanje vijesti u
ovoj populaciji nastaje pod utjecajem povjerenja, dakle nakon ishoda koji se
modelira. Kao prediktor povjerenja ipak radi, jer podiže udio objašnjene
varijabilnosti s `r hr_broj(100 * s16$r2_dva, 1)` % na
`r hr_broj(100 * s16$r2_posljedica, 1)` % i smanjuje preostalu raspršenost. Za
predviđanje je to dobitak, a za objašnjenje besmislica, budući da nitko ne može
znati koliko će netko platiti prije nego što ta osoba to i odluči.

Razlika se dalje ne vidi dok se model ocjenjuje na podacima na kojima je
procijenjen. Vidi se čim se podaci razdvoje na skup na kojem model uči i skup
koji je odvojen prije nego što je model postavljen.

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
se na podacima koji u procjeni nisu sudjelovali, jer se pristajanje uvijek može
podići dodavanjem varijabli. Poglavlje o algoritmima na toj razlici gradi cijeli
argument, budući da postupci koji odlučuju o kreditima, sadržaju i rangiranju
svoju vrijednost mjere isključivo uspješnošću na jedinicama koje još nisu
viđene.

## Granica prema uzroku

Poglavlje o mjerenju uvelo je konfundirajuću varijablu kao razlog zbog kojeg
opažena veza ne dokazuje uzrok, i obećalo da će se pitanje vratiti kad za njega
bude postojao račun. Račun sada postoji i vrijedi biti precizan o tome što je
njime dobiveno.

Uz izvor vijesti u modelu, koeficijent uz dob poklopio se s pravilom po kojem je
populacija nastala. Uspjeh nije proizašao iz postupka nego iz toga što je
generator poznat, pa se znalo koje dvije varijable treba uključiti. Stvarno
istraživanje tu informaciju nema, i nijedan ispis modela ne razlikuje slučaj u
kojem su svi važni čimbenici izmjereni od slučaja u kojem nisu.

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
referentne kategorije i cilj analize, jer isti podaci uz isti kod daju različit
model ovisno o tome je li pitanje opisno, prediktivno ili uzročno. Provjeravamo
tri stvari. Prva je tumači li koeficijent u izvornim jedinicama i uz uvjet
ostalih varijabli, umjesto da ga opiše kao učinak. Druga je predlaže li skup
kontrola prema tome koje su varijable dostupne, umjesto prema tome koje bi
pitanje tražilo. Treća je ocjenjuje li predikciju na podacima koji su
sudjelovali u procjeni, što je najčešća pogreška u ovom zadatku.

> Prilagodi model i protumači koeficijent glavne varijable u izvornim
> jedinicama, s intervalom. Za svaku kontrolu napiši zašto je u modelu i može li
> biti posljedica glavne varijable. Predikciju ocijeni na odvojenom skupu.

**Nađite grešku.**
Na traženje da procijeni koliko dobro model predviđa povjerenje kod novih
korisnika asistent je priložio ovaj račun.

Uz ispis je napisao obrazloženje. Model objašnjava osjetno veći udio
varijabilnosti nego prethodni, a prosječna pogreška iznosi manje od dva boda
na ljestvici od jedan do deset. Iz toga zaključuje da model dovoljno pouzdano
predviđa povjerenje kod korisnika koje nije vidio i preporučuje ga za primjenu
na novim podacima.

Greška je ocjena predviđanja na podacima na kojima je model procijenjen. Račun
je ispravan i obje su brojke točne, ali obje opisuju pristajanje na skupu za
učenje, koje je uvijek bolje od uspješnosti na novim jedinicama i to postaje
prividno bolje sa svakom dodanom varijablom. Tablica u ovom poglavlju mjeri
koliko je razlika velika, jer je model s dodanim slučajnim brojevima na svojem
uzorku griješio manje, a na odvojenom skupu više nego postupak koji svakome
pripiše prosjek. Odgovor bi tražio skup podataka odvojen prije procjene, i tek
tada izračunatu pogrešku.

## Razrađeni primjer

Ponavljamo cijeli argument na jednom mjestu i u obliku u kojem bi se pojavio u
izvještaju. Pitanje je kako se povjerenje u medije mijenja s dobi, a analiza
daje dva odgovora ovisno o tome uspoređuju li se svi ljudi ili samo oni koji se
informiraju iz istog izvora.

Funkcija `confint` uz procjenu vraća i granice intervala pouzdanosti iz
poglavlja o procjeni, pa svaki nagib dolazi s rasponom vrijednosti koje su s
podacima uskladive. Funkcija `rbind` slaže dva takva raspona jedan ispod
drugoga.

*Slika. Nagib uz dob u dvama modelima, s intervalom pouzdanosti, uz vrijednost ugrađenu u generator populacije. Izrada autora.*

Intervali dvaju modela se ne preklapaju, pa razlika među njima nije stvar
nepreciznosti. Zbirni nagib je za trećinu veći od vrijednosti koju procjenjuje,
dok prilagođeni tu vrijednost dohvaća na gornjem rubu svojeg intervala, uz malo
zaostajanje koje dolazi od zaokruživanja ljestvice. Izvještaj koji bi naveo samo prvi broj ne bi
sadržavao nijednu netočnu rečenicu o podacima, i svejedno bi ostavio dojam da
dob s povjerenjem ima jaču vezu nego što je ima.

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
jednakim vrijednostima ostalih varijabli, i na poznatoj populaciji to je
dovoljno da se pravilo po kojem su podaci nastali oporavi, ali samo zato što se
znalo što treba izmjeriti. Udio objašnjene varijabilnosti raste i kad se doda
čista buka, pa pristajanje nije ocjena, dok reziduali pokazuju gdje model ne
odgovara podacima. Objašnjenje i predviđanje odatle se razdvajaju, jer se drugo
provjerava isključivo na jedinicama koje model nije vidio. Sljedeće poglavlje
uzima taj kriterij ozbiljno i pita što se događa kad postupci koji ga
zadovoljavaju počnu odlučivati o ljudima.

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
brojke izgledaju uvjerljivo, i napišite zaključak koji bi isti ispis podnio.
