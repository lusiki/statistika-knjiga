# Statistika u doba algoritama

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

ParlaSent je skup rečenica iz parlamentarnih rasprava kojima su ljudi označili
ton. Koristimo njegov hrvatski dio kako bismo pratili što
model uči iz takvih oznaka i kako provjeravamo njegove pogreške
(Mochtak, 2023). Jedan redak sadrži jednu rečenicu i njezinu oznaku, a ne
cijeli govor ili mišljenje zastupnika.

„Da li je pošteno da se ukida prethodna stopa i da se povećava u odnosu na
prethodnu?” Tako glasi prvi hrvatski redak nastavne datoteke ParlaSent 1.0.
Jedan ga je koder označio neutralnim uz negativan ton, a drugi negativnim.
Nakon usklađenja zabilježena je oznaka `Negative` (Mochtak, 2023).

Zamislimo da urednički sustav šalje negativno označene rečenice na ljudski
pregled prije mogućeg javnog sažetka. Oznaka se ne objavljuje automatski, ali
određuje koji tekst dobiva dodatnu pozornost. Pogrešno uključivanje može
neopravdano istaknuti rečenicu, a pogrešno izostavljanje sakriti važan dio
govora.

Prije primjene trebamo opravdati zašto negativan ton uopće daje prednost pri
pregledu. To je urednička odluka. Možemo je usporediti sa slučajnim pregledom
ili izborom prema javnoj relevantnosti neovisno o tonu.

Treba li početnu rečenicu poslati na pregled? Najprije trebamo znati što je
jedinica analize, kako je odabrana i označena te tko može osporiti oznaku.

Kod regresije smo razlikovali opis postojećih podataka od predviđanja novih
ishoda. Sada nas zanima što se događa kada predviđanje pokrene postupak prema
nekoj osobi ili tekstu. U zamišljenom uredničkom sustavu iz vinjete
procijenjeni ton odlučuje koja će rečenica dobiti dodatni pregled. Za procjenu
takva sustava trebamo pratiti i nastanak oznake i posljedice pogrešne odluke.

Hrvatski dio ParlaSenta sadrži stvarne parlamentarne rečenice s ljudskim
oznakama tona (Mochtak, 2023). Jedan redak predstavlja rečenicu, a ne
zastupnika ili cijeli govor. Pratit ćemo tekst, dostupne oznake kodera i
podjelu podataka. U nastavnom primjeru iz tih ćemo oznaka izvesti jednostavan
rezultat za usporedbu pravila slanja na pregled. Time provjeravamo kako izbor
praga mijenja odluku. Uspješnost uvježbanoga klasifikatora ovdje ne mjerimo.

U tom se zadatku sastaju ranija pitanja o mjerenju, uzorkovanju i pogreškama.
Ljudska oznaka nije nepogrešiva mjera tona, a odabrani korpus nije automatski
slika svih parlamentarnih rasprava. Razmotrit ćemo zašto podatke razdvajamo za
učenje, provjeru i ispitivanje te kako prilagođavanje poznatim primjerima može
prikriti slabo predviđanje novih. Za svaku procjenu trebamo znati na kojim je
podacima nastala i što je već moglo utjecati na odluke o modelu.

Promjenom praga usporedit ćemo pogrešna uključivanja i propuštanja. U zasebnoj
simulaciji s dvjema skupinama istražit ćemo zašto se mjerila pravednosti mogu
razilaziti kada se razlikuju učestalosti ishoda. ParlaSentu pritom nećemo
pripisivati skupinska obilježja koja u paketu ne postoje. Provjeru ćemo
proširiti na mogućnost osporavanja oznake, odgovornost za postupak i uporabu
jezičnih modela. Umjesto samog postotka točnosti moći ćemo tražiti opis toga
što sustav predviđa, prema kojoj oznaci mjeri uspjeh i tko snosi posljedice.
Te odluke počinju izborom korpusa i jedinice koju sustav razvrstava.

## Odluka, korpus i jedinica

Klasifikator može procijeniti vjerojatnost pripadnosti kategoriji. Institucija
zatim bira prag koji pokreće pregled i određuje daljnje postupanje. Procjena,
odluka i njezine posljedice zasebni su dijelovi sustava.

Predviđanje procjenjujemo na novim podacima, a objašnjenje prema sadržajnom
pitanju, teoriji i nacrtu (Breiman, 2001; Shmueli, 2010). Dobro predviđen ton ne
otkriva namjeru govornika ni uzrok njegova izražavanja.

Naša [tekstna jedinica]{.pojam def="Jedan unaprijed određen komad teksta koji
se zasebno označava i analizira." en="text unit" ch="17"} jest rečenica. Ona
ne predstavlja cijeli govor, osobu ili sjednicu. [Granica korpusa]{.pojam
def="Pravilo koje određuje koji tekstovi mogu ući u analizu, a koji ostaju
izvan nje." en="corpus boundary" ch="17"} ovdje obuhvaća retke ParlaSenta s
oznakom `country = HR`. Paket ne daje govornika, stranku, datum, položaj vlasti ili
oporbe ni poveznicu na cijeli govor.

Nedostajući kontekst ne smijemo nadomjestiti nagađanjem. Izvorni autori
izostavili su moderatorske rečenice i zadržali duljine između prvog i trećeg
kvartila (Mochtak, 2024). Dio za učenje stratificirano su odabrali
prema prisutnosti pozitivnih, negativnih ili nijedne leksikonske riječi.
Ispitni dio odabrali su slučajno, uz iste filtre duljine i moderatora
(Mochtak, 2023; Mochtak, 2024). Zbog takvog odabira udio negativnih
oznaka ne procjenjuje udio negativnog tona u Hrvatskom saboru. Iz rečenice
također ne zaključujemo o osobini ili namjeri govornika.

Nastavna prilagodba ParlaSenta 1.0 sadrži stvarne parlamentarne rečenice s
oznakom zemlje `HR`, pod licencom CC BY-SA 4.0 (Mochtak, 2023). Ima 2.698
redaka. Sve rečenice istog dokumenta zadržane su u jednom izvedenom skupu.

Sljedeća tablica prikazuje broj redaka u svakom skupu. Račun čita pripremljenu
datoteku, pa brojnosti možemo reproducirati.

*Slika. Oznake i brojnosti u nastavnom paketu ParlaSent. Izrada autora prema @mochtak2023.*

Za učenje je izdvojeno 1.090 redaka, za provjeru 272, a za ispitivanje 1.336.
Zadržani su svi izvorni ispitni redci. Iz izvornog dijela za učenje uklonjeno
je 25 redaka iz 20 dokumenata koji su se pojavljivali i u ispitnom dijelu.
Uklanjanje nije ovisilo o oznaci. Koraci i kontrolne sume zapisani su u
podatkovnoj putovnici `data/parlament_tekst/PUTOVNICA.md`. Te brojnosti opisuju nastavni paket.

## Nastanak oznake

Izdvojili smo rečenice koje možemo analizirati, ali njihova oznaka tona još
nije sama po sebi razumljiva. [Okvir kodiranja]{.pojam def="Skup pravila po kojima se tekst pretvara u
kategorije koje analiza rabi." en="coding frame" ch="17"} određuje značenje
oznaka `Negative`, `Neutral` i `Positive`. Dodijeljena oznaka ovisi o uputama,
prosudbi kodera i načinu rješavanja neslaganja.

Izvorni dio za učenje sadrži dvije pojedinačne oznake i usklađenu oznaku. U
ispitnom dijelu dostupna je samo oznaka jednog uvježbanog kodera. Iako oba
dijela imaju stupac `recorded_label`, oznake nisu nastale jednakim postupkom.

**Zabilježeni referentni ishod** jest ishod ili oznaka zapisana određenim
postupkom mjerenja, prema kojoj se vrednuje klasifikator, ali koja može
sadržavati pogrešku.

Neslaganje kodera može upozoriti na nejasan pojam ili teško primjenjivo
pravilo. Drukčije upute ili usklađivanje mogu promijeniti referentnu oznaku.
Time se mijenja i ocjena klasifikatora, čak i ako njegova predviđanja ostanu
ista.

## Tri skupa, dva pitanja

Jedno je pitanje kojim ćemo modelom i pragom razvrstavati rečenice.
Drugo je koliko taj zaključani postupak uspješno radi na novim rečenicama.

U regresiji smo odvojili podatke na kojima ćemo provjeriti predviđanje novih
osoba. Ako sada na izdvojenim podacima biramo model ili prag, i oni utječu na
konačni postupak. Za njegovu završnu provjeru zato trebamo sačuvati još jedan
skup. [Razdvajanje na skup za učenje, provjeru i ispitivanje]{.pojam def="Odvajanje
podataka za prilagodbu modela, izbor postupka i jednu završnu procjenu."
en="train-validation-test split" ch="17"} odvaja tri zadatka. Model
prilagođavamo na učenju, pravilo i prag biramo na provjeri, a završnu
uspješnost jednom procjenjujemo na sačuvanom ispitnom skupu. Ovdje ispitni dio
ima drukčiji odabir i način označavanja, pa ga ne možemo koristiti za izravno
usporedivu završnu provjeru.

Paket razdvaja cijele dokumente. Dokumente iz izvorne ispitne datoteke
uklonili smo iz dijela za učenje, a preostale prema ponovljivom pravilu
podijelili na učenje i provjeru. Tako rečenice istog dokumenta ne prelaze
granice skupova i ne stvaraju privid provjere na neovisnom tekstu.
Takvo preklapanje dokumenata bilo bi još jedan oblik curenja informacija.

[Preprilagodba]{.pojam def="Učenje posebnosti viđenih podataka koje poboljšava
pristajanje njima, ali pogoršava predviđanje novih jedinica." en="overfitting"
ch="17"} nastaje kada model nauči posebnosti viđenih podataka pa njima
bolje pristaje, ali lošije predviđa nove jedinice. Zato ga provjeravamo
na odvojenim jedinicama. Ta provjera
ipak ne stvara reprezentativan uzorak. Populacijski doseg ovisi o odabiru
podataka. Čak ni dobar rezultat na pravilno izdvojenom skupu ne opravdava
prijenos na sve tekstove. Ovdje različit odabir i označavanje ispitnog dijela
dodatno ograničavaju usporedbu.

## Od vjerojatnosti do pravednosti

Uz prag 0,60 rečenica s procjenom 0,59 ne ulazi u pregled, a ona s 0,61 ulazi.
Mala razlika u broju tako mijenja postupanje. Izbor praga treba povezati s
posljedicama obiju vrsta pogreške.

**Klasifikacijski prag** jest unaprijed određena vrijednost koja predviđenu
vjerojatnost pretvara u kategoričku odluku; njegovim se pomicanjem mijenja
odnos vrsta pogrešaka.

Svaka rečenica sada završava među poslanima na pregled ili među
izostavljenima. Tu odluku možemo usporediti s njezinom zabilježenom oznakom,
kao što smo u poglavlju o kategoričkim podacima križali dob i izvor vijesti.
Pozitivna odluka ovdje znači slanje na pregled, a tražena je oznaka negativnog
tona. [Tablica zabune]{.pojam def="Kontingencijska tablica koja križa
klasifikacijsku odluku i zabilježeni referentni ishod." en="confusion matrix"
ch="17"} jest kontingencijska tablica odluka i referentnih oznaka. Stopa lažno
pozitivnih odluka računa se među zabilježenim nenegativnim rečenicama. Stopa
lažno negativnih računa se među zabilježenim negativnima. Pozitivna
prediktivna vrijednost pita koliko je zabilježenih negativnih među svima
poslanima na pregled. Ukupna točnost spaja uspjeh u obje skupine prema
njihovim brojnostima, pa može sakriti neravnomjerno raspoređene pogreške.

Nazivnik određuje značenje svake stope. Osjetljivost, odnosno odziv
(*recall*), računa se kao $TP/(TP+FN)$, a specifičnost kao
$TN/(TN+FP)$. Pozitivna prediktivna vrijednost, u klasifikaciji zvana i
preciznost (*precision*), računa se kao $TP/(TP+FP)$. Točnost
(*accuracy*) jest $(TP+TN)/n$. Kratice TP i TN znače točno pozitivne i
točno negativne odluke, a FP i FN lažno pozitivne i lažno negativne.
Klasifikacijska preciznost zato nije isto što i uski interval procjene.

Brojeve ćemo u razrađenom primjeru dobiti prebrojavanjem ljudskih glasova,
a ne provjerom gotovoga algoritma. Za prag od barem jednoga negativnog
glasa tablica daje $TP=122$, $FP=16$, $FN=0$ i $TN=134$.
Osjetljivost je $122/122$, specifičnost $134/150$, pozitivna prediktivna
vrijednost $122/138$, a točnost $256/272$. Ti različiti nazivnici
objašnjavaju zašto jedan postotak ne može opisati cijelu odluku.
Lažna uzbuna podsjeća na pogrešku prve vrste iz testiranja, ali ovdje
brojimo odluke prema referentnoj oznaci pojedinih rečenica, a ne
odbacivanja statističke hipoteze kroz ponovljene uzorke.

Temeljna stopa ovdje je udio zabilježenih negativnih ishoda prije odluke
modela. Ako se razlikuje među skupinama, jednake stope lažno pozitivnih i
lažno negativnih odluka mogu dati različite pozitivne prediktivne vrijednosti.
Zato se neka poželjna mjerila pravednosti ne mogu uvijek istodobno izjednačiti
(Chouldechova, 2017; Barocas, 2023). Uz broj pogrešaka trebamo razmotriti i
njihove posljedice.

Za [pogreške po podskupinama]{.pojam def="Odvojeni prikaz vrsta pogreške
unutar unaprijed smislenih skupina." en="subgroup errors" ch="17"} trebamo
pouzdanu skupnu varijablu. Nastavni paket takve podatke nema. Ne izvodimo ih
nagađanjem iz teksta ili imena. Zato za prikaz koristimo izmišljene skupine A
i B, a empirijski primjer ostaje bez podskupinske analize. To ograničenje ne
dokazuje da su pogreške pravedno raspoređene.

[Algoritamska pravednost]{.pojam def="Ocjena raspodjele koristi, pogrešaka i
mogućnosti osporavanja u cijelom sustavu odluke." en="algorithmic fairness"
ch="17"} zahtijeva više od jedne stope. Uz nazivnike i posljedice pogrešaka
razmatramo obavijest, obrazloženje te mogućnost prigovora i žalbe.

## Interakcija — Istraživač pravednosti

Za ovaj pokus zadajemo referentne ishode 0 i 1, ne ton stvarnih rečenica.
Za ishod 0 generiramo 6.000 rezultata iz normalne raspodjele sa sredinom
0,30 i standardnom devijacijom 0,18, a za ishod 1 drugih 6.000 sa sredinom
0,70 i istom standardnom devijacijom. Vrijednosti ispod nule zamjenjujemo
nulom, a iznad jedan jedinicom. Tako dobiveni brojevi služe razvrstavanju,
bez pretpostavke da su kalibrirane vjerojatnosti. Kalibracija iz poglavlja
o vjerojatnosti tražila bi slaganje najavljenih izgleda s učestalošću ishoda
među usporedivim prognozama. Ovdje to nismo provjerili.

Pri pragu 0,60 rezultat 0,65 vodi pozitivnoj odluci. Ako je referentni ishod
0, taj zapis ulazi u brojnik lažno pozitivnih. Taj broj dijelimo sa svih
6.000 zapisa ishoda 0. Analogno među 6.000 zapisa ishoda 1 brojimo rezultate
ispod praga za stopu lažno negativnih. Sve vrijednosti zadržavamo, uključujući
one ograničene na nulu i jedan.

Skupine A i B zatim slažemo ponderiranjem istih dviju uvjetnih raspodjela,
u prikazanoj postavci s udjelima ishoda 1 od 20 % i 45 %. Ne izvlačimo nove
osobe za svaku skupinu. Primjerice, u A udio točno pozitivnih među svima
iznosi $0,20(1-\text{stopa lažno negativnih})$, a udio lažno pozitivnih
$0,80 \times \text{stopa lažno pozitivnih}$. Njihov zbroj nazivnik je
pozitivne prediktivne vrijednosti. U B mijenjaju se težine u 0,45 i 0,55.
Uvjetne stope zato su u prikazu točno jednake po konstrukciji. Novi niz
simuliranih rezultata malo bi promijenio njihove vrijednosti.

Na slici uspoređujemo dvije simulirane skupine s različitim temeljnim stopama.
Za isti referentni ishod raspodjele rezultata jednake su u obje skupine.
Zajednički prag zato može dati jednake uvjetne stope pogreške, ali različitu
točnost i prediktivnu vrijednost. Prikaz ne opisuje ParlaSent ni stvarne
skupine ljudi.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

Kada su jednake i temeljne stope, sva četiri mjerila poklapaju se. Kada
temeljne stope promijenimo, razlikuju se pozitivna prediktivna vrijednost i
točnost, iako uvjetne stope pogreške ostaju jednake. Prikaz objašnjava
matematički odnos koji smo susreli u poglavlju o zavaravajućim brojkama. Sam
ne dokazuje nejednako postupanje u stvarnom sustavu.

## Osporiva oznaka i postupak

U simulaciji smo točno znali koji je referentni ishod. Vratimo se sada početnoj
rečenici, čija je oznaka nastala ljudskom prosudbom. Nakon usklađenja nosi
negativnu oznaku, dok je prvi koder odabrao neutralnu kategoriju s negativnim
tonom. Trebamo pregledati upute i obrazloženje te procijeniti bi li drugo
opravdano pravilo dalo drukčiji rezultat. Takva provjera može dovesti do
ispravka reference prema kojoj ocjenjujemo odluke.

Osoba koja pregledava rečenicu treba vidjeti izvorni tekst, pravilo i razlog
slanja na pregled. Treba moći zabilježiti obrazloženje i osporiti oznaku. Ako
odluka utječe na govornika ili javni prikaz njegova govora, potreban je i
postupak obavijesti i žalbe. Paket bez identiteta govornika to sam ne
omogućuje. Ljudski pregled također treba jasne upute, odgovornost i nadzor.

Promjena referentne oznake mijenja ćelije tablice zabune. Prethodno lažno
pozitivna odluka može postati točno pozitivna bez promjene predviđanja. Zato
čuvamo inačicu kodnih pravila, datum i razlog ispravka. Samo tako možemo
uspoređivati mjerila kroz vrijeme.

U primjeni pratimo i podatke, prag, sučelje, pregled, prigovore i daljnje
učenje. Ako nove oznake dobivaju samo pregledane rečenice, sustav uči uglavnom
iz teksta koji je već odabrao. Pogreške među izostavljenim rečenicama teže će
biti otkrivene.

Tako nastaje povratna sprega između odluka i budućih podataka. Slično je kod
preporuka. Rangiranje određuje što korisnici vide, a njihovo ponašanje postaje
podatak za novo rangiranje. Vrijeme zadržavanja pritom ne mjeri automatski
zadovoljstvo, informiranost ni javnu vrijednost (Barocas, 2023).

[Pomak distribucije]{.pojam def="Promjena odnosa u novim podatcima zbog koje
stara procjena uspješnosti više ne opisuje sadašnji rad sustava."
en="distribution shift" ch="17"} može nastati zbog novih tema, jezika, odabira
tekstova ili načina označavanja. Nakon primjene pratimo pregledane i
nepregledane tekstove, sporne oznake, vrijeme ispravka i promjene korpusa. Za
procjenu lažno negativnih odluka trebamo zasebno i usporedivo označiti
slučajni ili unaprijed stratificirani uzorak nepregledanih rečenica. Ranija
uspješnost ne jamči trajno dobar rad ni valjano mjerenje tona.

## Jezični modeli kao sustavi predikcije

I asistent kojim se služimo proizvodi predviđanja. [Jezični model kao sustav
predikcije]{.pojam def="Sustav koji iz prethodnoga teksta procjenjuje
vjerojatne nastavke i iz njih proizvodi novi tekst." en="language model as a
prediction system" ch="17"} možemo razumjeti na primjeru autoregresivnog GPT-3
iz 2020., koji generira nastavke uvjetovane prethodnim tekstom (Brown, 2020).
Tečan odgovor zato ne potvrđuje izvor, brojku ni zaključak. Predviđanje teksta
samo po sebi ne daje ni uzročno objašnjenje odgovora.

U odgovoru asistenta provjeravamo podatke, jedinicu, planiranu odluku i
način otkrivanja pogreške. Asistent može predložiti račun ili tablicu. Ne smije
nadomjestiti nedostajuća predviđanja izmišljenim stupcem, nagađati kontekst
ili tretirati referentnu oznaku kao nepogrešivu.

Odnos temeljnih stopa i mjerila susrećemo i u drugim primjenama klasifikacije.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Procjena da je osoba
visokorizična može utjecati na odluku koja se na nju odnosi.
Chouldechova je u istraživanju instrumenata za procjenu
ponavljanja kaznenog djela razmotrila kako različita mjerila
pravednosti mogu dati različite ocjene istog sustava
(Chouldechova, 2017). Spor se ne može riješiti samo podatkom
da je model ukupno dovoljno točan.

Jedan zahtjev polazi od značenja ocjene. Među ljudima s
jednakom ocjenom rizika zabilježeni bi ishod trebao biti
podjednako čest u različitim skupinama. Drugi zahtjev
polazi od pogrešno označenih ljudi. Među onima kod kojih
ishod nije zabilježen želimo usporediti koliko ih je ipak
označeno visokorizičnima. Ti zahtjevi koriste različite
nazivnike, pa jednakost prema jednome ne jamči jednakost
prema drugome.

Za cijelu skupinu označenu visokorizičnom možemo tražiti
jednak udio zabilježenih pozitivnih ishoda. Chouldechova
je pokazala zašto taj zahtjev pri različitim temeljnim
stopama u pravilu dolazi u sukob s jednakošću obiju stopa
pogreške (Chouldechova, 2017). Takav sukob ne javlja se
kod savršenog predviđanja, ali njega ne možemo
pretpostaviti u stvarnoj primjeni.
Taj matematički nalaz ne određuje koju bi pogrešku društvo
trebalo smatrati prihvatljivom niti opravdava njezine
posljedice za osobu.

Zato bi prije uporabe takve procjene trebalo razjasniti
što referentni ishod bilježi, kome pogrešna oznaka šteti
i kako se odluka može osporiti. Promjena praga može
promijeniti raspored pogrešaka, ali ne može sama dati
odgovor na ta pitanja. Ni dobro slaganje s postojećim
zapisima ne potvrđuje da oni potpuno opisuju pojavu
koju želimo procjenjivati.

U našem parlamentarnom primjeru posljedice i jedinice
drukčije su. Pogrešno uključena rečenica dobiva dodatni
pregled, a pogrešno izostavljena ostaje izvan njega.
Kaznenopravne skupine i njihove temeljne stope ne
prenosimo u taj korpus. Prenosimo način postavljanja
pitanja. Tvrdnja da je sustav pravedan treba imenovati
ishod, skupine, prag i pogrešku čije posljedice
procjenjujemo. Bez toga jednaka ocjena modela može
prikrivati različita iskustva ljudi na koje se odnosi.

Plan vrednovanja treba odrediti što će se provjeravati i koju će odluku
dobiveni rezultat poduprijeti. Sljedeći prijedlog povezuje te dvije zadaće.

**Nađite grešku.**
Tim priprema plan vrednovanja klasifikatora parlamentarnih rečenica.
U nastavnom paketu ParlaSent rečenice su razdvojene po dokumentima.
Izvorni dio za učenje ima dvije pojedinačne i usklađenu oznaku, dok
ispitni dio ima oznaku jednog uvježbanog kodera
(Mochtak, 2023; Mochtak, 2024). To su dva različita puta nastanka
oznake koje smo već upoznali.

Predloženi plan predviđa zaključavanje modela i praga prije otvaranja
ispitnog skupa. Točnost bi se računala kao udio predviđanja koja se
podudaraju sa zabilježenim oznakama. Tim još nije proveo tu provjeru ni
neovisno ponovno kodiranje ispitnih rečenica. Asistent je predložio
rečenicu za plan.

> Izdvojeni skup omogućit će provjeru slaganja predviđanja sa
> zabilježenim oznakama, uz ograničenja odabira i različitog kodiranja.
> Ako model na njemu postigne visoku točnost, time ćemo dokazati da
> ispravno mjeri ton rečenica.

Uredite plan tako da jasno kaže što će se tom provjerom doznati.
Navedite jednu dodatnu provjeru mjerenja i objasnite što bi ona mogla
otkriti čak i kada bi podudarnost modela s postojećim oznakama bila
visoka. Ne pripisujte klasifikatoru rezultat koji još nije izmjeren.

## Razrađeni primjer

Neslaganje kodera iz početne rečenice sada pretvaramo u pitanje o pravilu
pregleda. Je li dovoljan jedan negativan glas ili ćemo zahtijevati oba?
Usporedbu provodimo samo na 272 retka skupa za provjeru, s dvije pojedinačne i
usklađenom oznakom. Iz glasova kodera računamo rezultat 0, 0,5 ili 1. Oznake
`Negative` i `M_Negative` računamo kao negativne, a `Positive`,
`M_Positive`, `N_Neutral` i `P_Neutral` kao nenegativne. Ta nastavna
podjela zahtijeva provjeru osjetljivosti. Rezultat nije vjerojatnost
klasifikatora ni neovisno predviđanje. Usklađena referenca nastala je iz istih
ulaza, pa primjer pokazuje kako način označavanja oblikuje mjerila.

To objašnjava i nulu u ćeliji lažno negativnih pri blažem pravilu. Svaka
referentno negativna rečenica u ovom paketu ima barem jedan negativan glas.
Nula stoga proizlazi iz odnosa glasova i njihove usklađene oznake, a nije
dokaz savršenog prepoznavanja novih rečenica. Pri strožem pravilu postoji
jedna rečenica s dva negativna glasa i nenegativnom usklađenom oznakom,
`train-2089`. To je stvarno neslaganje zapisa, koje čuvamo vidljivim.

Od svih 2.698 zapisa sada zadržavamo samo 272 s oznakom `provjera`, bez
daljnjeg izostavljanja. Za mali prikaz namjerno biramo prvi redak sa svakom
od triju mogućih vrijednosti glasovanja. Broj retka odnosi se na cijelu
nastavnu datoteku, pa se zapis može ponovno pronaći.

*Slika. Tri odabrana koderska zapisa prije tablice zabune. Izrada autora prema @mochtak2023.*

Dva negativna glasa daju $(1+1)/2 = 1$, a jedan $(1+0)/2 = 0,5$.
U svakom retku odluku uspoređujemo s referencom. Slanje uz negativnu
referencu dodaje jedan točno pozitivnima, a slanje uz nenegativnu jedan
lažno pozitivnima. Neslanje analogno puni preostale dvije ćelije. Tako
prebrojavamo svih 272 zapisa, bez procjene klasifikatora.

Prvo pravilo postavlja prag na 0,5, pa rečenica ulazi na pregled ako je barem
jedan koder dao negativan glas. Taj prag primjenjujemo na glasove, za razliku
od ranijeg praga modelom predviđene vjerojatnosti. Poziv `mutate()` donosi
odluku za svaki redak, a `count()` zatim prebroji njezine kombinacije s
referentnom oznakom u četiri ćelije tablice.

Brojanja pri prvom pragu možemo pročitati kao običnu kontingencijsku
tablicu. Njezini se redci odnose na referentnu oznaku, a stupci na odluku.

| Referentna oznaka | Poslano na pregled | Nije poslano | Ukupno |
|---|---:|---:|---:|
| negativna | 122 | 0 | 122 |
| nenegativna | 16 | 134 | 150 |
| ukupno | 138 | 134 | 272 |

: Brojanja za prag 0,5 na istom skupu za provjeru. Izrada autora prema mochtak2023.

Stopa lažno pozitivnih je $16/150$, a pozitivna prediktivna vrijednost
$122/138$. Ista ćelija zato može sudjelovati u različitim pitanjima, uz
drukčiji nazivnik.

Da bismo vidjeli što traženje suglasnosti obaju kodera mijenja, na iste
rečenice primjenjujemo i prag 1. Sljedeća tablica uspoređuje ga s pragom 0,5,
uz isti zabilježeni referentni ishod. Sve su vrijednosti izračunate iz
pripremljenog paketa.

*Slika. Dvije odluke o ljudskom pregledu prema istom zabilježenom referentnom ishodu u skupu za provjeru. Izrada autora prema @mochtak2023.*

U tablici prve četiri brojnosti koriste upravo definirane kratice, a
sljedeća tri retka pokazuju nazivnike stopa. Posljednji redak daje ukupnu
točnost, udio ispravnih odluka među svim rečenicama. Jedna lažno pozitivna odluka
pri strožem pragu znači $1/150$, odnosno 0,7 %. Još jedna takva odluka
udvostručila bi taj postotak. Taj mali broj ne opravdava preciznu tvrdnju
o stopi u budućim tekstovima.

Pri nižem pragu na pregled ulaze sve 122 rečenice sa zabilježenim negativnim
ishodom i 16 od 150 nenegativnih. Stopa lažno pozitivnih odluka iznosi 10,7 %,
a lažno negativnih 0,0 %. Pri strožem pragu izostaju 22 od 122 negativne
rečenice, a ulazi jedna od 150 nenegativnih. Stope tada iznose 0,7 % i 18,0 %.

Za izbor pravila trebamo znati kapacitet pregleda, posljedice nepotrebnog
uključivanja i izostavljanja te mogućnost prigovora. Prije toga uredništvo
mora opravdati izbor negativnog tona kao kriterija. Treba ga usporediti sa
slučajnim pregledom ili kriterijem relevantnosti. Tablica pokazuje posljedice
praga, ali ne donosi tu odluku umjesto uredništva.

U ispitnom dijelu nemamo drugog kodera ni usklađenje, pa pravilo dvaju glasova
ne možemo jednako primijeniti i ocijeniti. Završnu uspješnost zato ne
izvještavamo. Za budući klasifikator trebali bismo unaprijed zaključati model,
prag i usporediv referentni postupak, spremiti predviđanja i jednom provesti
završnu provjeru. Ovdje provjeravamo podatke i pravilo odluke, bez tvrdnje o
izvedbi modela koji nije izgrađen.

Sada znamo zašto je oznaka početne rečenice sporna i što bi značilo
uključivanje u pregled. Još ne znamo namjeru govornika. Odluku treba vezati uz
izvorni tekst, obrazloženje, mogućnost ispravka i praćenje posljedica praga.

## Od modela do odluke

U tablici provjeravamo jedinicu i obuhvat podataka, vrstu tvrdnje,
nesigurnost, alternative i osobe na koje odluka može utjecati. Tako određujemo
doseg ovog primjera.

| Revizijsko pitanje | Primjena na odluku o ljudskom pregledu |
|---|---|
| Koja je jedinica? | jedna odabrana parlamentarna rečenica s putom nastanka zabilježene oznake, ne govor, govornik ili sjednica |
| Tko ili što nedostaje? | rečenice moderatora i rečenice izvan srednjega raspona duljine isključene su uzvodno; paket nema govornika, cijeli govor ni obranjivu skupnu varijablu |
| Koji je cilj tvrdnje? | tablica uspoređuje dva pravila slanja u pregled prema zabilježenom negativnom ishodu; riječ je o opisu i provjeri odluke, ne izvedbi postojećega klasifikatora |
| Gdje je neizvjesnost? | osjetljivost na prag; ne provjeravamo reprezentativnost, valjanost oznake, pogrešku kodiranja ni budući pomak distribucije |
| Koje drugo objašnjenje ostaje? | stroži prag mijenja pogreške; slučajni pregled ili kriterij relevantnosti mijenjaju i cilj odabira |
| Tko snosi posljedice? | pregledavatelji troše vrijeme, važan tekst može izostati, a govornik i javnost mogu dobiti iskrivljen prikaz |

: Šest revizijskih pitanja za odluku o ljudskom pregledu. Izrada autora prema Mochtak, 2023 i mochtakparlasent2024.

Sljedeća tablica razlikuje šest vrsta tvrdnji. Svaka traži odgovarajuće dokaze, pa
analiza ne mora niti može odgovoriti na sve.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje brojnosti, put oznake i posljedice dvaju pravila unutar pripremljenoga paketa |
| povezanost | pokazuje povezanost dvaju koderskih glasova s usklađenom oznakom, uz izričitu ovisnost jer su isti glasovi sudjelovali u njezinu nastanku |
| generalizacija | ne podupire prijenos na sav parlamentarni govor, govornike ili tekstove izvan odabranih rečenica |
| predviđanje | ne ocjenjuje postojeći model; buduća bi procjena tražila zaključan model, prag, usporediv referentni postupak i jedan izdvojeni ispitni skup |
| uzročnost | ne pokazuje što uzrokuje ton, uredničku važnost ili bilo koju posljedicu za govornika |
| odluka | podupire provjeru tereta dvaju pragova, ali ne dokazuje da je negativan sentiment legitiman cilj usmjeravanja pozornosti |

: Šest dimenzija tvrdnje na završetku dijela o modelima. Izrada autora prema mochtak2023.

Zašto razdvajanje na skup za učenje, provjeru i ispitivanje ne stvara
populacijsku reprezentativnost? Kako izbor rečenica i način njihova označavanja ograničavaju ono što možemo
zaključiti iz tablice zabune? Zašto jednake uvjetne stope
pogreške ne jamče jednaku pozitivnu prediktivnu vrijednost? Nakon primjene
sustava, koje rečenice moramo dodatno pregledati da bismo mogli procijeniti
koliko je negativnih slučajeva sustav propustio?

U završnom poglavlju sastavit ćemo vlastiti istraživački protokol. U njega
uključujemo pragove odluke, posljedice pogreške, nadzor i prigovor. Asistentu
možemo povjeriti račun i provjeru dosljednosti, dok cilj, prosudba dokaza i
odgovornost za zaključak ostaju naši.

Zaštitu osoba povezujemo s pravilima iz poglavlja o mjerenju i dizajnu.
Javna dostupnost zapisa sama ne uklanja mogućnost identifikacije ni štetu
od njegova povezivanja s drugim podacima. Prije dijeljenja provjeravamo
svrhu, nužnost pojedinih obilježja i prikladnost alata za osjetljivost
podataka. Pravila određenoga kolegija dodatni su uvjet u toj nastavi,
a nisu univerzalna zamjena za odgovornost prema sudionicima.

## Sažetak

Ocjenu algoritma počinjemo pitanjem što model može naučiti iz odabranih
podataka i što možemo provjeriti prema referentnim oznakama. Odvajanje skupova pomaže provjeri
predviđanja, ali samo ne stvara reprezentativnost ni valjano mjerenje. Kada
rezultat pretvorimo u odluku, prag mijenja raspodjelu pogrešaka, a različite
temeljne stope mogu dovesti mjerila pravednosti u sukob. Nakon primjene ostajemo odgovorni za pregled, ispravke, prigovor i nadzor,
uključujući provjeru izostavljenih slučajeva. Izvore i zaključke provjeravamo i u odgovoru jezičnog modela, koliko god bio
tečan.

## Pojmovi

osjetljivost klasifikatora (*sensitivity*), specifičnost (*specificity*),
preciznost odnosno pozitivna prediktivna vrijednost (*precision; positive predictive value*),
ukupna točnost (*accuracy*),

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
jedan pogrešan prijelaz i dokaz koji pokazuje razliku. Zatim u sažetom odgovoru revidirajte tvrdnju tako da obuhvati jedinicu, granicu korpusa, put
oznake, curenje, prag, dostupne podskupine, pomak distribucije te postupak
obavijesti, prigovora i žalbe. Objasnite zašto tečan odgovor jezičnoga modela
ne dokazuje nijednu nedostupnu sastavnicu.
