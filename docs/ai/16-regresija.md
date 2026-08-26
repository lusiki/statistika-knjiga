# Regresija — opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 32 min | Regresijski pravac | simulirana populacija | pogl. 2, 5, 6, 9 i 13–15 |

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
poglavlja o zaključivanju (Šikić, 2026). Povjerenje u medije mjereno je na
ljestvici od jedan do deset, a zanima nas kako se ono mijenja s dobi. Poglavlje
o povezanosti dalo bi na to pitanje jedan broj o jačini veze. Linearni model
umjesto toga daje modelom predviđeni linearni sažetak povjerenja za svaku dob.

Procjenjivana veličina, odnosno količina koju analiza cilja, jest broj koji
najbolje linearno sažima tih pedeset tisuća zabilježenih odgovora. Budući da su
obuhvaćene sve jedinice ove fiksne nastavne populacije, nema pogreške uzorkovanja
ni intervala koji bi je trebao izraziti. Brojevi iz generatora opisuju latentno
pravilo prije zaokruživanja i rezanja ljestvice. Oni nisu procjenjivana veličina
ove analize.

**Podsjetnik.** Nagib

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata izračunatim na svih pedeset tisuća pojedinačnih odgovora.*

Pravac na slici nije nacrtan kroz sredinu oblaka po oku. Bira ga pravilo koje
za svaku moguću kombinaciju odsječka i nagiba gleda koliko svako pojedino
opažanje promašuje, i uzima onu kombinaciju kojoj ti promašaji zajedno najmanje
teže.

**Rezidual** je razlika između opažene vrijednosti ishoda kod pojedine jedinice
i vrijednosti koju za nju predviđa model, dakle onaj dio ishoda koji model nije
objasnio.

Rezidual $i$-te jedinice označavamo $e_i$, njezinu opaženu vrijednost $y_i$, a
vrijednost koju model predviđa $\hat{y}_i$; kapica označava procjenu.

$$e_i = y_i - \hat{y}_i$$

Zbroj samih reziduala nije upotrebljiv kao mjera promašaja, jer se pozitivna i
negativna odstupanja poništavaju, pa bi loš pravac mogao izgledati savršeno.
Kvadriranje uklanja predznak i istodobno velika odstupanja košta više nego mala,
što je razlog zbog kojeg jedno jako promašeno opažanje pomiče pravac osjetnije
od deset blago promašenih.

**Metoda najmanjih kvadrata** bira koeficijente modela tako da zbroj kvadriranih
reziduala bude najmanji mogući za zadane podatke.

U ovoj je analizi procjenjivana veličina konačnopopulacijski koeficijent
najmanjih kvadrata. Model koji taj postupak daje ima oblik koji su poglavlja o
dvjema i o više skupina već koristila. Opaženi ishod $y_i$ rastavljamo na
modelom predviđenu vrijednost koju čine odsječak $\beta_0$ i nagib $\beta_1$
pomnožen s prediktorom $x_i$, te na odstupanje pojedine jedinice
$\varepsilon_i$.

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

Taj se oblik s jednim brojčanim prediktorom naziva **jednostavna linearna
regresija**.

Odsječak $\beta_0$ ostaje modelom sažeta vrijednost ishoda kada prediktor ima
vrijednost nula. U ovoj analizi $\beta_0$ i $\beta_1$ označavaju koeficijente
najmanjih kvadrata za cijelu fiksnu populaciju, dok je rezidual $e_i$ opaženo
odstupanje pojedine jedinice. Da je pred nama uzorak, kapice bi označavale
procjene tih ciljnih koeficijenata i uz njih bi trebalo prikazati uzoračnu
nesigurnost. Razlika prema poglavlju o dvjema grupama jedino je u tome što $x_i$
sada nije oznaka skupine nego izmjeren broj.

Konačnopopulacijski nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`. Deset godina
dobi u ovoj populaciji povezano je s razlikom od
`r hr_broj(10 * s16$nagib_jedan, 2)` boda povjerenja. Odsječak od
`r hr_broj(s16$presjek_jedan, 2)` boda odnosio bi se na osobu od nula godina,
koje u podacima nema, pa je računski potreban i sadržajno prazan. Kad se
prediktor prije procjene umanji za svoju sredinu, odsječak postane modelom
predviđeni ishod kod osobe prosječne dobi, a nagib se ne promijeni. Isti model
tada ima jedan broj manje bez značenja.

Pravac je pritom linearno sažeta tvrdnja o prosjecima, a ne o pojedincima. Točke
na slici su prosjeci nekoliko stotina ljudi po godini dobi i u ovom skupu leže
blizu pravca, dok pojedinačni odgovori odstupaju od njega za nekoliko bodova u
oba smjera. Rečenica da model za osobe od pedeset godina predviđa viši prosjek
nego za osobe od trideset opisuje linearni sažetak i ne dopušta zaključak o
konkretnoj osobi bilo koje dobi.

## Nagib koji nosi tuđu priču

Konačnopopulacijski nagib za zabilježeno povjerenje iznosi
`r hr_broj(s16$nagib_jedan, 4)` boda po godini. To je ciljna veličina ove
analize, izračunata bez pogreške uzorkovanja. Generator je prije zaokruživanja i
rezanja ishoda koristio latentni nagib od `r hr_broj(s16$latentno_dob, 3)`.
Razlika među tim brojevima nije pogreška procjene, jer oni opisuju različite
veličine. Latentni broj služi samo za pregled mehanizma kojim je nastao
zabilježeni ishod.

Razlog je u drugoj varijabli koja se mijenja zajedno s dobi. Generator najprije
stvara dob, zatim prema njoj raspoređuje izvor vijesti, pa prosječna dob ide od
`r hr_broj(s16$dob_mreze, 1)` godine među onima koji se informiraju preko
društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među slušateljima radija.
Kako povjerenje ovisi i o izvoru, a stariji ljudi biraju izvore uz koje ide više
povjerenja, nagib uz dob pokupi i tu razliku i pripiše je godinama.

Tvrdnja se može provjeriti bez ijednog novog pojma. U ovom poznatom generatoru
isti latentni dobni nagib vrijedi po svim izvorima, pa očekujemo manje nagibe
unutar skupina ljudi koji se informiraju iz istoga izvora, gdje se izvor više
ne mijenja zajedno s dobi.

*Slika. Nagib uz dob izračunat zasebno među korisnicima svakog izvora vijesti, uz zbirni konačnopopulacijski nagib i latentno pravilo prije mjerenja. Izrada autora.*

Nijedna od pet skupina nema nagib blizu zbirnoga. Skupni nagibi kreću se između
`r hr_broj(s16$nagib_unutar_min, 4)` i `r hr_broj(s16$nagib_unutar_max, 4)`, dok
je zbirni nagib veći od svakoga od njih. Njihova blizina latentnom pravilu
korisna je provjera generatora, ali ih ne pretvara u procjene toga pravila.
Ista pojava kojoj je poglavlje o povezanosti dalo ime pri usporedbi
koeficijenata unutar i između skupina ovdje se pojavljuje u modelu i pokazuje
da razlika ne dolazi iz pogreške procjene nego iz toga što se pita.

To nije konfundiranje u strogom uzročnom smislu. Izvor u poznatom generatoru
nastaje nakon dobi i prije povjerenja, pa je nalik posredniku na putu od dobi
prema ishodu. Zbirni koeficijent opisuje ukupni dobni obrazac u populaciji, a
koeficijent uz jednak izvor opisuje drugi, uvjetni obrazac koji taj put zatvara.
Nijedan ne govori koliko bi se povjerenje promijenilo kod iste osobe koja stari.

Ta razlika nema veze s količinom podataka. Model obuhvaća svih pedeset tisuća
ljudi, pa je ciljna konačnopopulacijska vrijednost poznata i nema uzoračne
nesigurnosti. Kad bi se iz te populacije izvukao uzorak, trebalo bi procijeniti
isti cilj i prikazati nesigurnost koja odgovara nacrtu uzorkovanja. Ni tada
interval ne bi mjerio udaljenost od latentnog pravila prije mjerenja.

## Prilagodba i ono što je čini mogućom

Ako opažena povezanost miješa dvije priče, model može zadati usporedbu pri
jednakoj vrijednosti druge varijable. Umjesto rezanja uzorka na skupine iste
dobi i istog izvora, sve koeficijente procjenjuje odjednom.

**Višestruka regresija** procjenjuje modelnu povezanost svakog prediktora s
ishodom pri zadanim jednakim vrijednostima svih ostalih prediktora u modelu.
Koeficijent je uvjetna usporedba koju zadaje model; kao usporedba podataka
obranjiv je samo ondje gdje postoji dovoljno potpore i preklapanja, pa ne mora
označavati stvarno uparene jedinice.

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

Izraz „uz kontrolu" zato opisuje račun, a ne postupak. U pokusu randomizacija
čini dodjelu neovisnom o početnim obilježjima i uravnotežuje skupine u
očekivanju, premda u konkretnom uzorku ostaje moguća slučajna neravnoteža, a
provedba i osipanje mogu narušiti početnu usporedbu. Kontrola u modelu znači da
je zadana uvjetna usporedba pri jednakim vrijednostima uključenih varijabli.

Iz toga slijedi oblik rečenice koji svaki koeficijent zaslužuje. U području
podataka s dovoljnom potporom model za ljude deset godina starije, uz jednak
izvor vijesti, predviđa prosjek povjerenja viši za
`r hr_broj(10 * s16$nagib_dva, 2)` boda. Rečenica navodi jedinicu prediktora,
jedinicu ishoda i uvjet pod kojim usporedba vrijedi, i bez ijednog od ta tri
dijela koeficijent se ne može provjeriti. Ista se disciplina traži i od
kategorijskih koeficijenata, gdje uvjet uključuje referentnu skupinu.

Riječ „prilagodba” ipak ne govori treba li varijabla ući u model. To ovisi o
njezinu mjestu u pretpostavljenom slijedu događaja. Sljedeći dijagram uspoređuje
tri mjesta koja u ispisu mogu izgledati jednako, a traže različite odluke.

*Slika. Tri uloge treće varijable u uzročnom dijagramu. Prilagodba za zajednički uzrok može zatvoriti neuzročni put, prilagodba za posrednika mijenja cilj s ukupne na izravnu vezu, a prilagodba za kolider može otvoriti novu pristranost. Izrada autora.*

Zajednički uzrok prethodi i pretpostavljenoj izloženosti i ishodu, pa ga je
razumno razmotriti radi poštenije usporedbe. Posrednik nastaje nakon izloženosti;
njegovim uključivanjem više se ne procjenjuje ista ukupna veza nego veza koja
ne prolazi tim putem. Kolider je posljedica obiju varijabli. Uvjetovanje na
njega može povezati inače nepovezane uzroke i stvoriti pristranost. Zato u model
ne ulazi „sve što imamo”. Prvo se određuju vremenski redoslijed, mjerna kvaliteta
i uloga svake varijable, a tek zatim specifikacija modela.

Odsječak u takvom modelu ostaje formalno potreban i sadržajno još slabiji nego
prije, jer sada opisuje osobu od nula godina koja se informira putem portala.
Model se time ne kvari. Kvari se samo pokušaj da se svaki broj iz ispisa
protumači kao da nešto opisuje.

Postoji i slučaj u kojem prilagodba ne uspijeva iako su sve varijable izmjerene.
Kad dva prediktora nose gotovo istu informaciju, podaci ne sadrže usporedbe u
kojima se jedan mijenja, a drugi ne, pa se njihovi pojedinačni doprinosi ne mogu
razdvojiti i koeficijenti postaju osjetljivi na male promjene uzorka. Zbroj tih
prediktora model i dalje koristi jednako dobro, a pitanje o svakome od njih
zasebno u tim podacima nema odgovor.

## Interakcija i regresijski pravac

Višestruki model ne mora pretpostaviti da jedna povezanost vrijedi jednako za
sve. Interakcija dopušta da se nagib jednog prediktora promijeni s vrijednošću
drugoga. U unaprijed planiranoj usporedbi modifikator, kodiranje, kontrast i
postupak zaključivanja zapisani su prije pregleda rezultata, a očekivani smjer
dodaje se kada je hipoteza usmjerena. Naknadno uočena podskupina može biti
korisna za novo pitanje, ali ostaje istraživačka i traži neovisnu provjeru.

Simulirani prikaz namjerno daje skupini A nagib
`r hr_broj(s16$heterogenost_a, 1)`, a skupini B
`r hr_broj(s16$heterogenost_b, 1)`. Zbirni model ih sažima nagibom
`r hr_broj(s16$heterogenost_zbirno, 1)`, koji ne opisuje nijednu skupinu.
Sljedeće predviđene linije zato čuvaju heterogenost koju bi jedan prosječni
koeficijent sakrio.

*Slika. Predviđene vrijednosti u simuliranom primjeru s različitim skupnim nagibima. Deblja zbirna linija opisuje prosjek koji ne vrijedi ni za jednu skupinu. Izrada autora.*

Interakcija se tumači zajednički, preko skupnih nagiba ili predviđenih
vrijednosti, a ne kao izolirani redak ispisa. Prikaz također sprečava čestu
pogrešku u kojoj se značajnost unutar jedne skupine i neznačajnost unutar druge
proglašavaju dokazom njihove razlike. Pitanje o heterogenosti pripada izravnom
testu interakcije i njegovoj nesigurnosti (Nieuwenhuis, 2011). Ovaj
deterministički prikaz demonstrira oblik, ne snagu dokaza; u stvarnim podacima
uz skupne se nagibe izvještava i interval za interakciju.

Sljedeći prikaz razdvaja dvije stvari koje su u prethodna tri odjeljka
ispisane kao gotov rezultat. U digitalnom izdanju čitatelj pomiče pravac i
uključuje treću varijablu, dok tiskani blizanac uspoređuje unaprijed zadani
kandidat s minimumom i prilagođenim pravcem. Podaci su manji i posebno
konstruirani za ovaj prikaz, kako bi se pojedini reziduali mogli vidjeti.

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

Prije nastavka zastanemo bez vraćanja tekstu. Koju veličinu analiza procjenjuje?
Što rezidual mjeri? O čemu ovisi uzročni doseg koeficijenta? Koji kriterij bira
pravac najmanjih kvadrata?

## Isti model iza ranijih poglavlja

Razlika dviju sredina može se zapisati kao koeficijent binarnog prediktora, a
usporedba više skupina kao niz koeficijenata prema referentnoj skupini. Brojčani
prediktor zatvara popis slučajeva. Vrijedi provjeriti da to nije samo tvrdnja o
zapisu.

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
pretvara ta dva postupka računanja nesigurnosti u isti test. Udio objašnjene
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

Ako ista osoba daje više redaka ili su osobe ugniježđene u razrede, ustanove ili
gradove, prvo treba ponovno odrediti jedinicu i procjenjivanu veličinu. Osobe s
više redaka inače dobivaju veću težinu, a obična nesigurnost nema opravdanje
neovisnih jedinica. Tu treba stati, imenovati vezu među redcima i odabrati
postupak koji je čuva. Ovo poglavlje takav problem prepoznaje i usmjerava dalje,
ali ne procjenjuje modele za ovisne podatke.

## Pristajanje i njegove granice

Koliko dobro model opisuje podatke mjeri se udjelom varijabilnosti ishoda koji
je model uspio objasniti. Ta mjera nosi ime koje obećava više nego što daje, pa
je vrijedi definirati oprezno.

**Koeficijent determinacije** je udio ukupne varijabilnosti ishoda u promatranom
skupu podataka koji je model objasnio, izračunat kao jedan minus omjer zbroja
kvadrata reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

Označavamo ga $R^2$; $e_i$ je rezidual, $y_i$ opaženi ishod, a $\bar{y}$
zajednička sredina ishoda.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Model samo s dobi objašnjava `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti
povjerenja, a model s dobi i izvorom `r hr_broj(100 * s16$r2_dva, 1)` %. Obje su
brojke male, ali sama niska vrijednost ne razlikuje raznolikost ljudi od mjerne
pogreške ili neprimjerenog oblika modela. Model s izvorom istodobno opisuje
prilagođeni odnos u ovoj konačnoj populaciji i leži blizu latentnoga pravila
generatora. Te dvije veličine ipak nisu iste.

Vrijednost ima i mehaničko svojstvo koje je čini nedostatnom za izbor modela.
Na istim redcima i istom ishodu nikada ne pada kad se doda prediktor, pa i onaj
koji s ishodom nema nikakve veze podigne ju za nešto. U uzorku od dvjesto osoba
dodavanje pet potpuno slučajnih brojeva podiže udio objašnjene varijabilnosti s
`r hr_broj(100 * s16$r2_bez, 1)` % na `r hr_broj(100 * s16$r2_sa, 1)` %, dok
prilagođeni koeficijent determinacije, koji kažnjava svaki dodani prediktor,
pada s `r hr_broj(100 * s16$prilagodeni_bez, 1)` % na
`r hr_broj(100 * s16$prilagodeni_sa, 1)` %. Prilagođena inačica ublažava
automatski rast, ali ostaje heuristika. Ni ona sama ne presuđuje o predviđanju,
uzroku ili sadržajnoj valjanosti.

Postoji i druga strana iste mehanike, po kojoj vrijednost pada iako se odnos ne
mijenja. Ograničimo li populaciju na ljude između trideset i pedeset godina,
nagib uz dob ostaje `r hr_broj(s16$nagib_usko, 4)`, praktički kao prije, a udio
objašnjene varijabilnosti pada s `r hr_broj(100 * s16$r2_jedan, 1)` % na
`r hr_broj(100 * s16$r2_usko, 1)` % u skupu od
`r hr_broj(s16$n_usko, 0)` ljudi.
Ograničenje raspona iz poglavlja o povezanosti radi i ovdje. Koeficijent
determinacije nije stabilno svojstvo odnosa neovisno o populaciji i rasponu
podataka.

Zbog toga usporedba te mjere među različitim populacijama ili rasponima često
ne odgovara na korisno pitanje. Istraživanje na cijeloj populaciji i istraživanje
na uskoj dobnoj skupini mogu naći sličan nagib i izvijestiti o vrijednostima koje
se razlikuju šest puta. Ni koeficijenti nisu automatski usporedivi. Traže isti
ishod i ljestvicu, usporedivu populaciju, kodiranje i skup prilagodbi, a uz
uzorak i interval koji odgovara nacrtu.

Isti svakodnevni naziv također može sakriti različit nacrt. U lokalnoj
simuliranoj populaciji „medijska aktivnost” znači dnevne minute zabilježene za
osobu u konačnom skupu odraslih (Šikić, 2026). DigiKat bilježi objave vidljive
platformi koje zadovoljavaju pravila korpusa, s jedinicom objave ili agregata i
populacijom obuhvaćenog medijskog sadržaja (Šikić, 2026). Nevidljivo privatno
ponašanje u prvom i sadržaj izvan praćenog korpusa u drugom slučaju ostaju izvan
analize. Zato se regresija osobne uporabe ne može protumačiti kao regresija
platformskih objava niti se skupni trag smije pripisati pojedincu. Zajednički
naziv ne stvara isti konstrukt, jedinicu, populaciju ni granicu vidljivosti.

Pristajanje pritom ništa ne govori o tome gdje model griješi, a to se vidi tek
kad se reziduali pogledaju nasuprot vrijednostima koje model predviđa. Vrijeme
provedeno uz medije u ovoj populaciji raste s dobi za
`r hr_broj(s16$nagib_minute, 2)` minute po godini, i taj je pravac sasvim
razuman, ali njegovi reziduali nisu jednako raspršeni po cijelom rasponu.

*Slika. Reziduali modela za dnevno vrijeme uz medije nasuprot vrijednostima koje model predviđa, na slučajnom podskupu od dvije tisuće osoba.*

Raspršenost reziduala raste s `r hr_broj(s16$rasprsenost_dolje, 0)` na
`r hr_broj(s16$rasprsenost_gore, 0)` minuta, od šestine s najnižim do šestine s
najvišim predviđanjima. Agregatna rezidualna raspršenost zato ne opisuje uvjetnu
predikcijsku pogrešku u svakom dijelu raspona. Kad bi podaci bili uzorak,
inferencija bi morala dopustiti promjenjivu varijancu. Prikaz reziduala kaže gdje
model ne pristaje, a ne što s tim učiniti, i ta razlika između nalaza i odluke
ostaje na istraživaču.

Bayesovski pristup može istu strukturu modela dopuniti prethodnim raspodjelama i
vratiti raspodjelu nesigurnosti za koeficijente ili predviđene vrijednosti.
Time se mijenja način izražavanja nesigurnosti, ali se ne popravljaju pogrešna
mjera, ovisne jedinice, curenje informacija ni neopravdana uzročna pretpostavka.
Ovdje taj pogled ostaje kratka najava, a ne drugi sustav zaključivanja.

## Objašnjenje i predviđanje

Dva zadatka koja ista jednadžba obavlja razlikuju se po tome što od modela
traže. Objašnjenje traži sadržajno određenu i protumačivu povezanost, dok
predviđanje traži malu pogrešku na jedinicama koje model nije vidio. Uzročno
objašnjenje dodatno traži prikladan dizajn i identifikacijske pretpostavke.
Shmueli je pokazala da se ta dva cilja razilaze već u izboru varijabli i mjera,
pa model koji je bolji za jedno može biti lošiji za drugo (Shmueli, 2010).

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
odabranu vremensku granicu to nije prediktivni dobitak nego curenje informacija.
Spremnost na plaćanje još ne postoji kad predviđanje treba nastati, pa takav
model ne bi mogao proizvesti valjano predviđanje za novu osobu.

Razlika se dalje ne vidi dok se model ocjenjuje na podacima na kojima je
procijenjen. Predviđanje izvan uzorka provjerava se na skupu odvojenom prije
postavljanja modela. Takva je provjera ovdje interna i vrijedi za isti
simulirani mehanizam; sama ne dokazuje prijenos u drugo vrijeme, sustav ili
populaciju. Oba modela u tablici koriste samo prediktore dostupne do iste
vremenske granice.

*Slika. Prosječna pogreška predviđanja dvaju modela na podacima na kojima su procijenjeni i na odvojenom skupu, u bodovima povjerenja. Izrada autora.*

Na skupu za učenje od `r s16$n_ucenje` osoba bogatiji model objašnjava
`r hr_broj(100 * s16$r2_bogat, 1)` % varijabilnosti, prema
`r hr_broj(100 * s16$r2_skroman, 1)` % kod skromnijeg. Na tim podacima griješi
manje, ali na `r s16$n_provjera` osoba koje nije vidio griješi više od
skromnijeg modela i više nego postupak koji svakome pripiše prosjek skupa za
učenje. Model je naučio raspored slučajnih brojeva u svojem uzorku i taj raspored
u novim podacima ne postoji.

Skromniji model pritom je bolji od bogatijega na ovom odvojenom skupu.
Povjerenje se u populaciji raspršuje sa standardnom devijacijom
`r hr_broj(s16$sd_ishoda, 2)` boda, a nakon što model uzme u obzir dob i izvor
ostaje rezidualna raspršenost od `r hr_broj(s16$sd_ostatka, 2)`. Dio te
raspršenosti dolazi od slučajne sastavnice generatora, a dio može pripadati
nepotpunom obliku modela. Zato sama rezidualna standardna devijacija nije
dokazana donja granica pogreške nekog boljeg prediktivnog postupka.

Tvrdnja o predviđanju stoga se provjerava na podacima koji u procjeni nisu
sudjelovali i smije koristiti samo
informacije dostupne u trenutku primjene. Prvi uvjet sprječava da model ocjenjuje
sam sebe, a drugi curenje informacija iz budućnosti. Poglavlje o algoritmima na toj
razlici gradi cijeli argument, budući da postupci koji odlučuju o kreditima,
sadržaju i rangiranju svoju vrijednost mjere uspješnošću na jedinicama koje još
nisu viđene.

## Granica prema uzroku

Konfundirajuća varijabla prethodi i pretpostavljenom uzroku i ishodu. Regresija
može izračunati uvjetnu usporedbu uz takvu varijablu, ali njezinu ulogu ne može
otkriti iz ispisa. Za to su potrebni sadržajno znanje, vremenski redoslijed i
dizajn istraživanja.

U poznatom generatoru izvor vijesti ne igra tu ulogu. Nastaje nakon dobi i prije
povjerenja, pa prilagodba za izvor zatvara mogući posrednički put i mijenja
procjenjivanu veličinu sa zbirnog na uvjetni dobni obrazac. Prilagođeni se
koeficijent približava latentnom izravnom pravilu zato što poznajemo način
nastanka podataka. To slaganje nije dokaz da bi isti postupak u stvarnom
istraživanju otkrio učinak.

Prilagođena povezanost zato nije sama po sebi uzročni učinak. Vremenski red,
izostanak neizmjerenih zajedničkih uzroka i izbjegavanje prilagodbe za posljedice
pretpostavljenog uzroka jesu važni, ali nisu dovoljni uvjeti. Uzročna
identifikacija traži i valjano mjerenje, dovoljno preklapanja usporedivih
jedinica, dobro definiranu intervenciju, zaštitu od selekcijske pristranosti i
primjeren oblik modela. Ovo poglavlje te uvjete imenuje, ali njima ne uspostavlja
uzročnu identifikaciju.

Dob dodatno nema jednostavno intervencijsko tumačenje. U stvarnom istraživanju
o vremenskom redu, ulozi izvora i opravdanosti svake usporedbe raspravljalo bi
se prije računanja, a nijedan modelni ispis ne bi potvrdio da su pretpostavke
zadovoljene.

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
**Od omjera do dopuštene rečenice.** Kad je ishod binaran, vjerojatnost je udio
usporedivih jedinica s ishodom 1. Označimo li tu vjerojatnost s $p$, izgledi su
omjer $p$ i njegove nadopune, $p/(1-p)$. Omjer izgleda uspoređuje izglede dviju
skupina; omjer rizika uspoređuje njihove vjerojatnosti. Omjer izgleda zato ne
znači promjenu u postotnim bodovima i ne smije se preimenovati u omjer rizika.
Ako 20 od 100 ljudi ima ishod, vjerojatnost je 0,20, a izgledi su 20 prema 80,
odnosno 0,25.

Kategorijski prediktor čita se prema referentnoj skupini, čiji je omjer izgleda
jedan. Vrijednost iznad jedan znači veće izglede od referentnih, a vrijednost
ispod jedan manje. Interval od 95 % koji obuhvaća vrijednost jedan spojiv je i s
jednakim izgledima. Predviđena vjerojatnost zahtijeva cijelu
specifikaciju, odsječak i vrijednosti ostalih prediktora, pa se ne može obnoviti
iz izdvojenog omjera izgleda kad ti dijelovi nisu objavljeni. Ovdje učimo samo
čitati ishod, referentnu skupinu, omjer i interval; procjenjivanje logističkog
modela, njegova jednadžba i dijagnostika ostaju izvan opsega knjige.

Kleppang i suradnici analizirali su
samoprijavljene presječne podatke istraživanja Ungdata iz 2018. za 12.353
norveških adolescenata u dobi od 15 do 16 godina, uz ukupni odaziv od 85 %
(Kleppang, 2021). Presječni nacrt ne određuje vremenski smjer i ne podupire
uzročnu tvrdnju.

| Prediktor i kategorija | Model 1, društvene mreže AOR (95 % interval) | Model 2, igranje AOR (95 % interval) | Model 3, oba prediktora AOR (95 % interval) |
|---|---:|---:|---:|
| Društvene mreže, do 3 sata | 1 (ref.) | nije u modelu | 1 (ref.) |
| Društvene mreže, više od 3 sata | 1,60 (1,43–1,80) | nije u modelu | 1,51 (1,34–1,70) |
| Igranje, do 3 sata | nije u modelu | 1 (ref.) | 1 (ref.) |
| Igranje, više od 3 sata | nije u modelu | 1,57 (1,36–1,80) | 1,38 (1,19–1,59) |

: Prilagođeni omjeri izgleda za simptome depresije prema uporabi društvenih mreža i igranju. Sadržajno skraćena, preoblikovana i na hrvatski prevedena prilagodba Tablice 3 iz rada Kleppang i suradnika (Kleppang, 2021).

Ishod je kodiran kao simptomi depresije na ili iznad 80. percentila nasuprot
vrijednosti ispod 80. percentila. AOR označava omjer izgleda prilagođen za rod ili
spol, imanje prijatelja, pušenje, visoko obrazovanje roditelja i obiteljsko
materijalno stanje. Stupac Model 1 sadrži društvene mreže, Model 2 igranje, a
Model 3 oba prediktora uz isti navedeni skup prilagodbi (Kleppang, 2021).

Izvor su Annette Løvheim Kleppang, Anne Mari Steigen, Li Ma, Hanne Søberg
Finbråten i Curt Hagquist, „Electronic media use and symptoms of depression
among adolescents in Norway”, *PLOS ONE* 16(7), e0254197, 2021,
članak (https://doi.org/10.1371/journal.pone.0254197) i
izvorna Tablica 3 (https://doi.org/10.1371/journal.pone.0254197.t003)
(Kleppang, 2021). Izvor je pod licencom
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Ovdje su odabrani
redci i tri modelna stupca preoblikovani, skraćeni i prevedeni na hrvatski;
brojčane vrijednosti i granice intervala nisu promijenjene. Prilagodba ne
podrazumijeva odobrenje autora ni PLOS-a.

U prilagođenom i skraćenom prijevodu prvog odlomka rezultata tablica prikazuje
omjere izgleda za simptome depresije prema uporabi društvenih mreža u prvom
stupcu, igranju u drugom te objema varijablama u trećem, nakon prilagodbe za
navedene čimbenike. U modelu prilagođenom za rod ili spol, imanje prijatelja,
pušenje, visoko obrazovanje roditelja i obiteljsko materijalno stanje,
adolescenti koji društvene mreže rabe više od tri sata na dan imali su 1,60
puta onolike izglede da budu na ili iznad 80. percentila simptoma kao oni koji
ih rabe do tri sata (AOR 1,60; 95 % interval 1,43–1,80) (Kleppang, 2021).

Prva rečenica prijevoda oslanja se na naslove triju stupaca i bilješku o
prilagodbama. Druga se oslanja na ćeliju 1,60 s intervalom od 1,43 do 1,80 u
Modelu 1 i na referentni redak iznad nje. Ni ta ćelija ni cijela tablica ne daju
apsolutne vjerojatnosti, omjere rizika ili predviđene vjerojatnosti. Ne daju ni
presjek modela potreban za njihov izračun (Kleppang, 2021).

Izvadak namjerno ne prikazuje modelno specifične nazivnike, odsječak, mjere
pristajanja, dijagnostiku, p-vrijednosti ni zvjezdice. Intervali nose
nesigurnost, ali bez tih elemenata nije moguće provjeriti gubitak redaka,
usporediti pristajanje modela ili obnoviti apsolutni rizik. Koeficijenti
prilagodbenih varijabli također ne bi automatski bili njihovi učinci, jer je
njihova uzročna uloga drugačija za svako pitanje (Westreich, 2013). Samoprijava,
neizmjereni čimbenici i presječni nacrt dodatno ograničavaju zaključak
(Kleppang, 2021).

**Pitajte model.**
Asistent može prilagoditi model, izraditi dijagnostičke prikaze i prevesti
koeficijente u prozu. Prije poziva treba mu zadati ulogu svake varijable,
referentne kategorije, procjenjivanu veličinu i cilj analize, jer različite
specifikacije odgovaraju opisnom, prediktivnom ili uzročnom pitanju. Za
prediktivni cilj treba zadati i trenutak primjene.

U odgovoru se provjerava tumači li koeficijent u izvornim jedinicama i uz uvjet
ostalih varijabli, umjesto kao učinak, te bira li prilagodbe prema pitanju, a ne
prema tome što je pri ruci. Predviđanje smije koristiti samo informacije
dostupne do trenutka primjene i mora se ocijeniti na podacima koji nisu
sudjelovali u procjeni.

> Prilagodi model i protumači koeficijent glavne varijable u izvornim
> jedinicama, s mjerom nesigurnosti koja odgovara ciljnoj veličini i nacrtu. Za
> svaku kontrolu napiši zašto je u modelu i može li biti posljedica glavne
> varijable.
> Imenuj trenutak predviđanja, isključi poslijeishodne podatke i predviđanje
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

Pitanje je kako se povjerenje u medije mijenja s dobi, a analiza daje dva
odgovora ovisno o tome opisuje li se zbirni obrazac ili obrazac pri jednakom
izvoru. Ciljne su veličine u oba slučaja koeficijenti najmanjih kvadrata za
zabilježene odgovore svih pedeset tisuća ljudi.

Funkcija `lm` ovdje izračunava opisne koeficijente iz cijele konačne populacije.
Nijedna jedinica nije uzorkovana, pa uz te brojeve nema uzoračne nesigurnosti.
Funkcija `confint` zato se ne poziva. Njezin uobičajeni interval odnosio bi se na
drugi, modelni ili nadpopulacijski cilj koji ovo poglavlje nije odabralo.

*Slika. Konačnopopulacijski nagib uz dob u dvama modelima za zabilježeni ishod. Izrada autora.*

Razlika među nagibima nije stvar uzoračne nepreciznosti. Oba su poznata točno za
ovu populaciju, ali odgovaraju na različita pitanja. Zbirni nagib obuhvaća dobni
obrazac koji prolazi i kroz izbor izvora, a prilagođeni je modelna usporedba pri
jednakom izvoru i zatvara taj put. Izvještaj koji bi naveo samo prvi broj ne bi
sadržavao netočnu brojku i svejedno bi zamaglio razliku između pitanja.

Zaključak se zato piše u dva dijela. Zbirni model za deset godina veću dob
predviđa prosjek povjerenja viši za
`r hr_broj(10 * s16$nagib_jedan, 2)` boda. Pri jednakom izvoru model predviđa
razliku od `r hr_broj(10 * s16$nagib_dva, 2)` boda. Prva rečenica opisuje ukupni
linearni obrazac, druga uvjetni obrazac, i tek zajedno kažu što je model našao.

Uvjetni oblik izvještaja čuva granicu zaključka. Ako je cilj opisati ovu
simuliranu konačnu populaciju, navode se oba koeficijenta bez uzoračnog
intervala. Za širu populaciju iz uzorka isti bi koeficijenti trebali interval
koji odgovara nacrtu. Predviđanje nove osobe traži pogrešku na odvojenim
podacima i trenutak dostupnosti prediktora. Nijedan od tih oblika sam po sebi ne
podupire uzročnu rečenicu.

Izvještaj uz to mora reći što je izostavljeno. Model sadrži dvije varijable, dok
bi obrazovanje, iskustvo s pojedinim redakcijama ili političke sklonosti bili
mogući, ovdje neizmjereni čimbenici koje bi stvarno istraživanje moralo
razmotriti. Njihovo uključivanje moglo bi promijeniti ciljnu uvjetnu usporedbu i
njezinu veličinu.

Ostaje i pitanje na koje ova analiza uopće nije odgovarala. Nijedna od dviju
rečenica ne kaže da bi se povjerenje neke osobe promijenilo time što ona
ostari, ni da bi se promijenilo time što promijeni izvor vijesti. Analiza
opisuje kako izgleda populacija u jednom trenutku, a promjena kod iste osobe
kroz vrijeme zahtijeva podatke koji istu osobu prate, kojih ovdje nema.

## Sažetak

Linearni model povezuje ishod s prediktorima kroz modelom predviđene vrijednosti i
reziduale, a metoda najmanjih kvadrata bira koeficijente po jasnom kriteriju
koji se u widgetu može vidjeti kako radi. Više prediktora daje povezanosti pri
jednakim vrijednostima ostalih varijabli, dok interakcija dopušta različite
nagibe i traži zajedničko tumačenje predviđenih vrijednosti. Koeficijenti za
cijelu konačnu populaciju opisuju zabilježeni ishod bez uzoračne nesigurnosti i
nisu latentni parametri generatora; udio objašnjene varijabilnosti raste i kad
se doda čista buka, pa pristajanje samo ne ocjenjuje generalizaciju, dok
reziduali pokazuju gdje model ne odgovara podacima. Objašnjenje i predviđanje
odatle se razdvajaju, jer se drugo provjerava na jedinicama koje model nije
vidio i samo s informacijama dostupnima u trenutku primjene. Kod binarnog
ishoda omjer izgleda nije omjer rizika ni razlika vjerojatnosti, a referentna
skupina i interval sastavni su dijelovi čitanja; prilagođena povezanost nije
sama po sebi učinak, pa izvještaj mora imenovati procjenu, jedinice, populaciju,
nesigurnost i uzročni doseg koji dizajn podupire. Sljedeće poglavlje uzima
kriterij predviđanja ozbiljno i pita što se događa kad postupci koji ga
zadovoljavaju počnu odlučivati o ljudima.

## Pojmovi

linearna regresija (*linear regression*), procjenjivana veličina (*estimand*),
rezidual (*residual*), metoda najmanjih kvadrata (*least squares*), višestruka
regresija (*multiple regression*), prilagođena povezanost (*adjusted
association*), koeficijent determinacije (*R-squared*), interakcija
(*interaction*), curenje informacija (*information leakage*), predviđanje izvan
uzorka (*out-of-sample prediction*), izgledi (*odds*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto se nagib uz dob mijenja kada u model uđe izvor
vijesti, a nijedan podatak o dobi pritom nije promijenjen. Imenujte pitanje na
koje odgovara svaki od dvaju nagiba. Na prikazu interakcije zatim odredite koji
nagib opisuje skupinu A, koji skupinu B i zašto zbirni nagib ne opisuje nijednu.

### Računski

Zbirni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)` boda po godini. Izračunajte
modelom predviđenu razliku prosjeka između dobi od 25 i 55 godina, a zatim isti
račun ponovite s prilagođenim nagibom
`r hr_broj(s16$nagib_dva, 4)` uz jednak izvor vijesti. Predajte obje brojke i
objasnite zašto nijedna ne određuje ostvarenu razliku dviju konkretnih osoba.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi operacionalizacije i vremenskog
reda te poglavlju o tome kako brojke zavode radi razlike između točne brojke i
preširoke tvrdnje. Na prilagođenoj Tablici 3 iz okvira odredite što je mjereno,
koja je referentna skupina, koju količinu podupire ćelija 1,60 i koja bi dodatna
količina trebala za tvrdnju o apsolutnoj vjerojatnosti. Zatim preuredite naslov
„Više od tri sata na društvenim mrežama povećava depresiju za 60 %” u jednu
rečenicu koju presječni nacrt i prikazani omjer izgleda doista podupiru.

### Revizija modela

Ocijenite račun i zaključak iz okvira o pogrešci. Imenujte što je u kodu
ispravno, redak u kojem se pogreška događa, razlog zbog kojeg obje priložene
brojke izgledaju uvjerljivo i napišite zaključak koji bi isti ispis podnio.
Objasnite i zašto pogreška nije curenje informacija iz budućnosti u zadanoj
vremenskoj granici, nego pogrešna provjera na skupu za učenje.
