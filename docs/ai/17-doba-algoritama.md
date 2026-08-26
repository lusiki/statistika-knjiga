# Statistika u doba algoritama

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| nije mjereno | Istraživač pravednosti | ParlaSent 1.0 i simulacija | obvezno kategorički podatci; dohvat mjerenja, zavaravajućih brojki, uzorkovanja, testiranja, veličine učinka i regresije |

**Vinjeta.**
„Da li je pošteno da se ukida prethodna stopa i da se povećava u odnosu na
prethodnu?” Prvi je to hrvatski redak nastavne datoteke ParlaSent 1.0. Jedan
ga je koder označio neutralnim uz negativan ton, drugi negativnim, a postupak
usklađenja zabilježio je oznaku `Negative` (Mochtak, 2023).

Zamislimo urednički sustav koji rečenice označene kao negativne šalje u red za
ljudski pregled prije mogućega javnog sažetka. Sustav ne briše tekst, ne
kažnjava govornika i ne objavljuje oznaku automatski. Ipak, odluka određuje
koje će rečenice dobiti dodatnu pozornost. Pogrešan ulazak može neopravdano
usmjeriti pozornost, a pogrešno izostavljanje može sakriti važan dio govora.

Veza između negativnoga tona i potrebe za pregledom osporiva je urednička
politika, a ne posljedica podataka. Treba je zasebno obrazložiti i usporediti s
neutralnom alternativom, primjerice slučajnom provjerom ili kriterijem javne
relevantnosti koji ne ovisi o sentimentu.

Treba li ova rečenica ući u red? Odgovor ne počinje izborom modela. Počinje
pitanjima što je jedinica, tko je mogao biti opažen, kako je oznaka nastala i
tko je može osporiti.

## Odluka, korpus i jedinica

Klasifikator može ponuditi predviđenu vjerojatnost da rečenica pripada
određenoj kategoriji. Institucija tek zatim određuje koja će vrijednost
pokrenuti ljudski pregled. Model proizvodi broj, prag ga pretvara u odluku, a
postupak odlučuje što se događa nakon te odluke.

Predviđanje i objašnjenje nisu dva naziva za isti cilj [Breiman, 2001;
Shmueli, 2010]. Model za predviđanje prosuđujemo prema ponašanju na podacima koje
nije rabio za učenje. Od objasnidbenoga modela tražimo odgovor na pitanje kako
su varijable povezane s ishodom i može li se ta povezanost braniti teorijom i
nacrtom. Uspješno predviđanje tona ne pokazuje što je govornik namjeravao niti
što je ton uzrokovalo.

U ovom je primjeru [tekstna jedinica]{.pojam
def="Jedan unaprijed određen komad teksta koji se zasebno označava i analizira."
en="text unit" ch="17"} jedna rečenica. Redak nije cijeli govor, osoba ni
parlamentarna sjednica. [Granica korpusa]{.pojam
def="Pravilo koje određuje koji tekstovi mogu ući u analizu, a koji ostaju izvan nje."
en="corpus boundary" ch="17"} obuhvaća samo retke koje je izvorna datoteka
ParlaSent označila s `country = HR`. Paket ne sadržava govornika, stranku,
datum, položaj vlasti ili oporbe ni vezu na cijeli govor.

Ta odsutnost nije prazno polje koje smijemo nadopuniti nagađanjem. Uzvodni je
odabir također selektivan. Izvorni su autori isključili rečenice moderatora i
zadržali samo rečenice duljine između prvoga i trećega kvartila
(Mochtak, 2024). Rečenice u
dijelu namijenjenom učenju zatim su stratificirano uzorkovane prema tome
sadrže li pozitivne, negativne ili nijednu riječ iz sentimentnih leksikona,
dok je ispitni dio odabran slučajno, bez oslanjanja na sentimentne leksikone,
ali pod istim ograničenjem duljine i moderatorskim filtrom
(Mochtak, 2023; Mochtak, 2024). Zato udio negativnih oznaka nije procjena udjela negativnoga
tona u Hrvatskome saboru. Nije dopušten ni prijelaz s rečenice na namjeru ili
osobinu govornika. Dobra analiza najprije imenuje što nije moglo ući u podatke,
a tek zatim opisuje ono što jest.

ParlaSent 1.0 donosi stvarne označene parlamentarne rečenice, a nastavna
prilagodba pod licencom CC BY-SA 4.0 zadržava samo retke s izvornom oznakom
zemlje `HR` (Mochtak, 2023). Paket ima 2.698 redaka, a svi su dokumenti
držani unutar jednoga izvedenog skupa.

Provjerni račun čita već pripremljenu datoteku i broji retke. Njegov je izlaz
tablica s brojnostima triju skupova; računsko zaleđe ostaje skriveno jer ovdje
čitatelju treba trag rezultata, a ne sintaksa uređivanja kategorija.

*Slika. Oznake i brojnosti u nastavnom paketu ParlaSent. Izrada autora prema @mochtak2023.*

Brojnosti opisuju paket, ne parlament. Skup za učenje ima 1.090 redaka, skup
za provjeru 272, a skup za ispitivanje 1.336. Svih 1.336 ispitnih redaka
zadržano je. U ovoj je prilagodbi iz izvornoga dijela za učenje uklonjeno 25
redaka iz 20 dokumenata koji su prelazili ispitnu granicu. Nijedan redak nije
uklonjen prema oznaci. Transformacijski trag s ulaznim i izlaznim kontrolnim
sumama te tim dvjema brojnostima nalazi se u podatkovnoj putovnici
`data/parlament_tekst/PUTOVNICA.md`.

## Nastanak oznake

[Okvir kodiranja]{.pojam
def="Skup pravila po kojima se tekst pretvara u kategorije koje analiza rabi."
en="coding frame" ch="17"} govori što riječi `Negative`, `Neutral` i `Positive`
trebaju značiti. Oznaka nije prirodno svojstvo retka koje čeka da ga otkrijemo.
Ona je rezultat uputa, osobe koja kodira i postupka rješavanja neslaganja.

Putovi nastanka oznake u paketu namjerno ostaju različiti. U dijelu izvorno
namijenjenom učenju dostupne su dvije pojedinačne oznake i usklađenje. U
izvornom ispitnom dijelu dostupna je jedna oznaka uvježbanoga kodera; drugi
koder i usklađenje nisu dostupni iz izvora. Učenje i ispitivanje zato nemaju
jednak postupak mjerenja, premda oba završavaju stupcem `recorded_label`.

**Zabilježeni referentni ishod** jest ishod ili oznaka zapisana određenim
postupkom mjerenja, prema kojoj se vrednuje klasifikator, ali koja može
sadržavati pogrešku.

Neslaganje kodera nije samo smetnja koju usklađenje briše. Ono otkriva mjesta
na kojima je konstrukt nejasan ili pravilo teško primjenjivo. Ako promijenimo
upute, kodere ili postupak usklađenja, možemo promijeniti zabilježeni
referentni ishod. Tada se mijenja i tablica prema kojoj ocjenjujemo model, čak
i ako su njegova predviđanja ostala ista.

## Tri skupa, dva pitanja

Puni naziv postupka glasi [razdvajanje na skup za učenje, provjeru i
ispitivanje]{.pojam
def="Odvajanje podataka za prilagodbu modela, izbor postupka i jednu završnu procjenu."
en="train-validation-test split" ch="17"}. Skup za učenje služi prilagodbi
modela, skup za provjeru izboru pravila i praga, a skup za ispitivanje čuva se
za jednu završnu procjenu nakon tih izbora. U ovom je paketu usporediva završna
procjena blokirana jer ispitni dio ima drukčiji
postupak odabira i drugi referentni postupak.

ParlaSentov nastavni paket dijeli cijele dokumente, ne pojedine rečenice.
Dokument koji se pojavio u izvornoj ispitnoj datoteci uklonjen je iz izvornoga
dijela za učenje, a preostali su dokumenti deterministički raspoređeni u
učenje i provjeru. Tako rečenice istoga dokumenta ne cure preko granice i ne
stvaraju privid provjere na novom tekstu.

[Preprilagodba]{.pojam
def="Učenje posebnosti viđenih podataka koje poboljšava pristajanje njima, ali pogoršava predviđanje novih jedinica."
en="overfitting" ch="17"} objašnjava zašto je odvajanje potrebno. Ono ipak ne
rješava pitanje uzorkovanja o dosegu populacije. U pravilno projektiranom
razdvajanju procjenjujemo ponašanje na izdvojenim jedinicama iz istoga
podatkovnog postupka, dok nacrt uzorkovanja određuje na koju populaciju smijemo
generalizirati. ParlaSentov se ispitni dio razlikuje i odabirom i putem oznake,
pa ovdje ne daje usporedivu završnu validaciju. Dobar ispitni rezultat ni u
idealnom slučaju ne pretvara odabrani korpus u reprezentativan uzorak.

## Od vjerojatnosti do pravednosti

Ako je prag za slanje u pregled 0,60, rečenica s predviđenom vjerojatnošću
0,59 ne ulazi u red, a ona s 0,61 ulazi. Razlika od dvije stotinke postaje
razlika u postupanju. Prag zato nije samo tehničko podešenje. Njegov izbor
govori koji je teret pogreške institucija spremna prihvatiti.

**Klasifikacijski prag** jest unaprijed određena vrijednost koja predviđenu
vjerojatnost pretvara u kategoričku odluku; njegovim se pomicanjem mijenja
odnos vrsta pogrešaka.

[Tablica zabune]{.pojam
def="Kontingencijska tablica koja križa klasifikacijsku odluku i zabilježeni referentni ishod."
en="confusion matrix" ch="17"} isti je tablični objekt koji smo u poglavlju o
kategoričkim podatcima čitali kao kontingencijsku tablicu. Ovdje redovi mogu
označivati zabilježeni referentni ishod, a stupci odluku o pregledu. Stopa lažno pozitivnih odluka ima
u nazivniku sve zabilježene nenegativne rečenice, dok stopa lažno negativnih
odluka polazi od svih zabilježenih negativnih rečenica. Pozitivna prediktivna
vrijednost zatim pita koliki udio među svim rečenicama poslanima u pregled ima
zabilježeni negativni ishod. Ukupna točnost ponderira uspjeh u dvjema uvjetnim
skupinama njihovim temeljnim stopama, pa može sakriti teret pojedine vrste
pogreške.

Temeljna stopa, uvedena u poglavlju o tome kako brojke zavode, ovdje određuje
koliko je zabilježeno negativnih ishoda prije odluke modela. Čak i kada dvije
skupine imaju jednake uvjetne stope lažno pozitivnih i lažno negativnih
odluka, različite temeljne stope mogu dati različitu pozitivnu prediktivnu
vrijednost. Poglavlja o testiranju i veličini učinka podsjećaju nas da isti
broj pogrešaka nije jednako važan kada su posljedice odluka različite. Zato se
više poželjnih mjerila pravednosti ne može uvijek izjednačiti istodobno
(Chouldechova, 2017; Barocas, 2023).

[Pogreške po podskupinama]{.pojam
def="Odvojeni prikaz vrsta pogreške unutar unaprijed smislenih skupina."
en="subgroup errors" ch="17"} imaju smisla samo ako paket doista sadržava
obranjivu skupnu varijablu. Nastavni paket ParlaSent takve podatke nema. Ne
smijemo iz imena, teksta ili nedostupnoga govornog konteksta izvesti skupine
koje datoteka nije isporučila. Widget zato rabi izmišljene skupine A i B, a
empirijski primjer ne glumi podskupinsku analizu.
Nemogućnost izračuna podskupinskih stopa nije dokaz da su pogreške pravedno
raspoređene; to je ograničenje onoga što paket može provjeriti.

[Algoritamska pravednost]{.pojam
def="Ocjena raspodjele koristi, pogrešaka i mogućnosti osporavanja u cijelom sustavu odluke."
en="algorithmic fairness" ch="17"} nije jedna stopa. Traži da zajedno čitamo
nazivnike, posljedice, obavijest, obrazloženje, prigovor i žalbu.

## Interakcija — Istraživač pravednosti

Istraživač pravednosti mijenja klasifikacijski prag za dvije skupine s
različitim temeljnim stopama, ali jednakom kvalitetom rezultata uvjetno na
zabilježeni referentni ishod. Skupine i brojke generira poznati simulacijski
mehanizam; one ne opisuju ParlaSent ni stvarne ljude. Prikaz pokazuje kako
zajednički prag može izjednačiti neke stope pogreške, a ipak proizvesti
različitu prediktivnu vrijednost i točnost.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

Widget drži uvjetne stope pogreške jednakima u objema skupinama jer za obje
rabi iste simulirane raspodjele rezultata. Kad su i temeljne stope jednake,
poklapaju se sva četiri mjerila. Kad se temeljne stope razdvoje, pozitivna
prediktivna vrijednost i točnost više se ne poklapaju. Time se vraćamo
posljedici različitih temeljnih stopa objašnjenoj u poglavlju o zavaravajućim
brojkama, a ne dokazujemo da je jedna skupina povlaštena u nekom stvarnom
sustavu.

## Osporiva oznaka i postupak

Vratimo se početnoj rečenici. Postupkom usklađenja rečenica je označena
negativnom, ali prvi je koder odabrao neutralnu kategoriju s negativnim tonom. Razumno je
pitati je li kodna uputa dovoljno jasna i bi li drugi postupak dao drukčiji
ishod. Takav prigovor ne briše podatak, nego zahtijeva otvaranje traga odluke i
može dovesti do ispravka zabilježenoga referentnog ishoda.

Postupovna pravednost u našem primjeru ima prepoznatljiv redoslijed. Interna
kontrola kvalitete traži da osoba zadužena za pregled zna zašto je rečenica
ušla u red, vidi izvornu rečenicu i pravilo, zabilježi obrazloženje te može
osporiti oznaku. Odvojeno od toga, odluka važna za govornika ili uredničku sliku
javnoga govora traži obavijest pogođenoj strani, pravo na žalbu i osobu koja o
njoj odlučuje. Nastavni paket nema identitet govornika i sam ne može uspostaviti
taj institucionalni postupak. Ljudski pregled nije čarobni popravak; i on treba
upute, odgovornost i nadzor.

Promjena oznake mijenja nazivnike i brojnike tablice zabune. Rečenica koja je
bila lažno pozitivna može postati točno pozitivna samo zato što je promijenjen
referentni zapis. Zato se uz rezultate čuva inačica okvira kodiranja, datum
ispravka i razlog promjene. Mjerilo bez puta nastanka oznake nema stabilno
značenje.

Sustav u primjeni nije samo model. Čine ga podatci, pravilo praga, sučelje,
red za ljudski pregled, način bilježenja prigovora i odluka što se iz pregleda
vraća u buduće podatke. Ako se za daljnje učenje biraju samo pregledane
rečenice, sustav češće dobiva nove oznake upravo za tekst koji je već smatrao
zanimljivim. Pogreške u neopaženom tekstu tada teže ulaze u podatke za ispravak
modela.

To je povratna sprega između predviđanja i podataka. Sličan obrazac vrijedi za
sustave preporuke. Rangiranje sadržaja mijenja ono što ljudi vide, a njihovo
ponašanje nakon toga postaje novi podatak za rangiranje. Mjera poput vremena
zadržavanja pritom nije isto što i zadovoljstvo, informiranost ili javna
vrijednost. Ona je operacionalizirani cilj sustava (Barocas, 2023).

[Pomak distribucije]{.pojam
def="Promjena odnosa u novim podatcima zbog koje stara procjena uspješnosti više ne opisuje sadašnji rad sustava."
en="distribution shift" ch="17"} može nastati promjenom jezika, tema, izbora
tekstova ili načina označavanja. Nadzor zato ne pita samo je li ukupna točnost
pala. Operativni pregled prati količinu pregledanoga i nepregledanoga teksta,
sporne oznake, vrijeme do ispravka i promjene granice korpusa. Zaseban slučajni
ili unaprijed stratificirani uzorak nepregledanih rečenica mora dobiti neovisan
i usporediv postupak označavanja. Bez takve provjere ne možemo procijeniti
stopu lažno negativnih odluka nakon ugradnje. Dobra uspješnost na izdvojenim
podatcima nije trajna dozvola za uporabu niti potvrda da oznaka valjano mjeri
ton.

## Jezični modeli kao sustavi predikcije

Asistent kojim smo se služili kroz knjigu pripada istoj obitelji prediktivnih
sustava. Pojam [jezični model kao sustav predikcije]{.pojam
def="Sustav koji iz prethodnoga teksta procjenjuje vjerojatne nastavke i iz njih proizvodi novi tekst."
en="language model as a prediction system" ch="17"} određuje što u toj vezi
provjeravamo. Autoregresivni GPT-3 iz 2020. opisan je kao model koji proizvodi
nastavke uvjetovane prethodnim tekstom (Brown, 2020). Njegov tečan izlaz zato
nije sam po sebi potvrda izvora, ispravnosti brojke ili valjanosti zaključka.
Kao u poglavlju o regresiji, predviđena vjerojatnost ne govori zašto je
pojedinačan tekst dobio određeni odgovor niti sama podupire uzročnu tvrdnju.

Statističko čitanje takva izlaza vraća nas na isti lanac. Pitamo iz kojih su
podataka mogli nastati obrasci, što je jedinica izlaza, koja se odluka na njemu
temelji i kako se pogreška otkriva. Asistent može predložiti klasifikacijsku
tablicu ili izračun, ali ne smije izmisliti stupac s predviđanjima, zamijeniti
nedostupni kontekst pretpostavkom ili proglasiti zabilježenu oznaku
nepogrešivom.

Isti se matematički sukob mjerila pojavljuje i izvan analize parlamentarnoga
govora.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Analiza instrumenata za procjenu rizika
pokazala je sukob između kalibracije i jednakosti određenih stopa pogreške kada
se temeljne stope razlikuju (Chouldechova, 2017).

To je ograničen dokaz o matematičkom odnosu mjerila, ne predložak za prenošenje
kaznenopravnih skupina u naš parlamentarni primjer. Tvrdnja da je model
„pravedan” nije potpuna bez imenovanja zabilježenoga referentnog ishoda,
mjerila, skupina, praga i posljedica. Agregatna točnost može ostati jednaka dok
se vrste pogrešaka vrlo nejednako raspoređuju.

**Pitajte model.**
Asistent može provjeriti pripremljenu tablicu, ali najprije mora dobiti opis
jedinice, granice korpusa, puta oznake i triju skupova. Zatim provjerava
curenje informacija, prag, uvjetne nazivnike, pogreške po dostupnim
podskupinama, promjene distribucije i valjanost kodiranja. Ne dajemo mu osobne
identifikatore niti dopuštamo da nedostupno polje dopuni iz teksta.

> Provjeri ovu pripremljenu klasifikacijsku tablicu. Odvoji ono što podatci
> pokazuju od onoga što ne mogu pokazati. Provjeri jedinicu, granicu korpusa,
> put oznake, razdvajanje dokumenata, prag i svaki uvjetni nazivnik. Navedi
> koje postupke prigovora, ispravka i nadzora ta odluka zahtijeva.

**Nađite grešku.**
Ako model na izdvojenom skupu za ispitivanje postigne visoku točnost prema
zabilježenim oznakama, time je dokazano da ispravno mjeri ton.

## Razrađeni primjer

Račun ispituje samo 272 retka skupa za provjeru, u kojem su dostupne dvije
pojedinačne oznake i usklađena zabilježena oznaka. Za nastavnu provjeru gradimo
jednostavan rezultat s mogućim vrijednostima 0, 0,5 i 1. U ovoj se nastavnoj
redukciji oznake `Negative` i `M_Negative` računaju kao negativan glas, a
`Positive`, `M_Positive`, `N_Neutral` i `P_Neutral` kao nenegativan glas. To je
odluka koju treba provjeriti na osjetljivost. Rezultat nije predviđena
vjerojatnost modela, jezični model ni neovisna provjera. Usklađena oznaka nastala je iz
istih koderskih ulaza, pa račun namjerno pokazuje ovisnost mjerila o postupku
proizvodnje oznake.

U razrađenom računu prag pravila odluke postavljamo na 0,5. To nije
klasifikacijski prag nad predviđenom vjerojatnošću, nego strukturno slično
pravilo nad dvama koderskim glasovima koje služi samo provjeri puta oznake.
Rečenica ulazi u red ako je barem jedan koder dao negativan glas. `mutate()`
primjenjuje tu odluku na svaki redak, a `count()`
ispisuje četiri ćelije kontingencijske tablice poznate iz poglavlja o
kategoričkim podatcima.

Prag 0,5 uspoređujemo sa strožim pragom 1, kod kojega oba kodera moraju
odabrati negativnu kategoriju. Brojevi u tablici izravno se reproduciraju iz
pripremljenoga paketa.

*Slika. Dvije odluke o ljudskom pregledu prema istom zabilježenom referentnom ishodu u skupu za provjeru. Izrada autora prema @mochtak2023.*

Uz niži prag svih je 122 rečenica sa zabilježenim negativnim ishodom poslano u
pregled, ali je u red ušlo i 16 od 150 rečenica sa zabilježenim nenegativnim
ishodom. Uz stroži prag nisu ušle 22 od 122 rečenice sa zabilježenim negativnim
ishodom, dok je među 150 rečenica sa zabilježenim nenegativnim ishodom samo
jedna ušla. Niži prag zato ima stopu lažno
pozitivnih odluka 10,7 % i stopu lažno negativnih odluka 0,0 %. Stroži prag
ima odgovarajuće stope 0,7 % i 18,0 %.

Ne možemo iz same tablice proglasiti jedno pravilo najboljim. Uredništvo mora
odrediti posljedicu nepotrebnoga pregleda, posljedicu izostavljanja, raspoloživ
kapacitet i put prigovora. Prije toga mora obrazložiti zašto negativan polaritet
uopće određuje red te usporediti takvu politiku sa slučajnom provjerom ili
kriterijem relevantnosti koji ne ovisi o sentimentu. Provjera osjetljivosti
zaključka na prag pokazuje da odluka o redu nije sadržana u podatcima.

Ispitni dio postavlja važno ograničenje. Ondje nije dostupan drugi koder ni
usklađenje, pa se pravilo dvaju glasova ne može primijeniti ni vrednovati na
isti način. Pošten izvještaj zato ne izmišlja završnu uspješnost. Za budući bi
klasifikator trebalo unaprijed zaključati model, prag i usporediv referentni
postupak, sačuvati njegova predviđanja te tek jednom otvoriti skup za
ispitivanje. Ovaj paket podupire provjeru podataka i odluke, ali ne tvrdnju o
izvedbi nepostojećega modela izvan korpusa.

Povratak početnoj rečenici sada daje drukčiji odgovor. Znamo zašto je njezina
oznaka sporna i što bi slanje u pregled učinilo, ali nemamo osnovu tvrditi što
je govornik namjeravao. Razumna odluka zahtijeva pregled izvornoga teksta,
vidljivo obrazloženje, mogućnost ispravka i praćenje učinka praga.

## Granica Dijela V — Od modela do sustava u primjeni

Na prijelazu iz modela u sustav u primjeni provjeravamo jedinicu i granice
podataka, vrstu tvrdnje, izvore nesigurnosti, razumne alternative i osobe koje
odluka može pogoditi. Primjena na ljudski pregled pokazuje dokle ovaj dokaz
seže.

| Pitanje revizije | Primjena na odluku o ljudskom pregledu |
|---|---|
| Što predstavlja jedan redak ili jedno opažanje? | jednu odabranu parlamentarnu rečenicu s putom nastanka zabilježene oznake, ne govor, govornika ili sjednicu |
| Tko ili što nije moglo ući u ove podatke? | rečenice moderatora i rečenice izvan srednjega raspona duljine isključene su uzvodno; paket nema govornika, cijeli govor ni obranjivu skupnu varijablu |
| Koja je ciljana količina i vrsta tvrdnje? | tablica uspoređuje dva pravila slanja u pregled prema zabilježenom negativnom ishodu; riječ je o opisu i provjeri odluke, ne izvedbi postojećega klasifikatora |
| Koji su izvori nesigurnosti obuhvaćeni, a koji ostaju izvan izračuna? | prikazana je osjetljivost odluke na prag pravila, ali ne i uzoračka reprezentativnost, valjanost sentimenta, pogreška kodiranja ili budući pomak distribucije |
| Koja bi razumna alternativna odluka mogla bitno promijeniti odgovor? | stroži prag mijenja teret pogrešaka, a slučajna provjera ili kriterij relevantnosti mijenjaju i sam cilj uredničkoga reda |
| Na koga može utjecati pogrešan zaključak ili odluka? | pregledavatelji mogu trošiti pozornost na pogrešne retke, važan tekst može biti izostavljen, a govornik ili javnost mogu dobiti iskrivljenu uredničku sliku |

: Šest revizijskih pitanja za odluku o ljudskom pregledu. Izrada autora prema Mochtak, 2023 i mochtakparlasent2024.

Isti dokaz zatim raspoređujemo u šest dimenzija tvrdnje. One nisu ljestvica na
kojoj svaka analiza mora dosegnuti vrh, nego karta različitih zahtjeva za
dokazom.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje brojnosti, put oznake i posljedice dvaju pravila unutar pripremljenoga paketa |
| povezanost | pokazuje povezanost dvaju koderskih glasova s usklađenom oznakom, uz izričitu ovisnost jer su isti glasovi sudjelovali u njezinu nastanku |
| generalizacija | ne podupire prijenos na sav parlamentarni govor, govornike ili tekstove izvan odabranih rečenica |
| predviđanje | ne ocjenjuje postojeći model; buduća bi procjena tražila zaključan model, prag, usporediv referentni postupak i jedan izdvojeni ispitni skup |
| uzročnost | ne pokazuje što uzrokuje ton, uredničku važnost ili bilo koju posljedicu za govornika |
| odluka | podupire provjeru tereta dvaju pragova, ali ne dokazuje da je negativan sentiment legitiman cilj usmjeravanja pozornosti |

: Šest dimenzija tvrdnje na granici Dijela V. Izrada autora prema mochtak2023.

Zašto razdvajanje na skup za učenje, provjeru i ispitivanje ne stvara
populacijsku reprezentativnost? Kako uzvodni
odabir i put oznake ograničavaju tablicu zabune? Zašto jednake uvjetne stope
pogreške ne jamče jednaku pozitivnu prediktivnu vrijednost? Što nakon ugradnje
moramo opažati izvan redovnoga reda za pregled da bismo uopće mogli procijeniti
lažno negativne odluke?

Završno poglavlje preuzima prag, teret pogreške, nadzor i put prigovora kao
dijelove vlastitoga istraživačkog protokola. Asistentu se može odgovorno
delegirati račun i provjera dosljednosti, ali izbor cilja, procjena dokaza i
odgovornost za objavljenu odluku ostaju na istraživaču.

## Sažetak

Algoritamska odluka počinje granicom korpusa i postupkom mjerenja, a ne
modelom. Razdvajanje na skup za učenje, provjeru i ispitivanje štiti procjenu
predviđanja, ali ne stvara populacijsku reprezentativnost ni valjan konstrukt.
Klasifikacijski prag raspoređuje vrste pogrešaka, a temeljne stope mogu dovesti
mjerila pravednosti u sukob. Nakon ugradnje podatci, sučelje, ljudski pregled,
prigovor, povratna sprega i nadzor čine jedan sustav. Jezični model proizvodi
vjerojatan nastavak; provjera izvora i odgovornost za odluku ostaju ljudske.
U završnom poglavlju isti se zahtjev pretvara u cjelovit protokol u kojem prag,
teret pogreške, nadzor, prigovor i odgovorno delegiranje moraju ostati vidljivi
od pitanja do objave.

## Pojmovi

tekstna jedinica (*text unit*), granica korpusa (*corpus boundary*), okvir
kodiranja (*coding frame*), zabilježeni referentni ishod (*recorded reference
outcome*), razdvajanje na skup za učenje, provjeru i ispitivanje
(*train-validation-test split*), preprilagodba (*overfitting*), klasifikacijski
prag (*classification threshold*), tablica zabune (*confusion matrix*),
pogreške po podskupinama (*subgroup errors*), algoritamska pravednost
(*algorithmic fairness*), pomak distribucije (*distribution shift*), jezični
model kao sustav predikcije (*language model as a prediction system*)

## Zadaci

### Konceptualni

Objasnite kako razdvajanje na skup za učenje, provjeru i ispitivanje otkriva
preprilagodbu te zašto dokument koji prijeđe među skupovima stvara curenje
informacija. Zatim povežite tablicu zabune s kontingencijskom tablicom iz
poglavlja o kategoričkim podatcima i objasnite zašto predviđena vjerojatnost iz
poglavlja o regresiji još nije odluka. Imenujte oba uvjetna nazivnika pogreške.

### Računski

U pripremljenoj tablici odluka nalazi se 90 točno pozitivnih, 30 lažno
pozitivnih, 10 lažno negativnih i 170 točno negativnih slučajeva. Izračunajte
stopu lažno pozitivnih odluka, stopu lažno negativnih odluka, pozitivnu
prediktivnu vrijednost i točnost. Uz svaki rezultat napišite njegov nazivnik i
jednu moguću posljedicu za red ljudskoga pregleda.

### Kritički

Osporite zabilježenu oznaku početne rečenice. Napišite koje biste dijelove
okvira kodiranja, izvornih oznaka i usklađenja trebali vidjeti prije odluke.
Zatim objasnite zašto promjena oznake može promijeniti mjerila pravednosti bez
ijedne promjene modela.

### Revizija modela

Ocijenite tvrdnju iz okvira o pogrešci. Navedite jednu prihvatljivu tvrdnju,
jedan pogrešan prijelaz i dokaz koji pokazuje razliku. Zatim u najviše šest
rečenica revidirajte tvrdnju tako da obuhvati jedinicu, granicu korpusa, put
oznake, curenje, prag, dostupne podskupine, pomak distribucije te postupak
obavijesti, prigovora i žalbe. Objasnite zašto tečan odgovor jezičnoga modela
ne dokazuje nijednu nedostupnu sastavnicu.
