# DIO V: MODELI

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Kategorički podaci

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Berkeleyjski podaci mogu se zapisati kao tablica frekvencija. Redovi označuju
ishod prijave, stupci spol, a svaka ćelija broj prijava (Bickel, 1975). Zbirna
tablica pokazuje razliku, ali ne govori koje su ćelije najviše odstupile od
onoga što bismo očekivali kada bi dvije varijable bile nepovezane.

Hi-kvadrat postupak upravo tu počinje. Ne pita jesu li svi postoci jednaki,
nego uspoređuje opažene brojeve s brojevima koje proizvode rubni zbrojevi pod
modelom nezavisnosti.

Kako iz tablice brojanja prepoznati gdje se nalazi veza i koliko je ona snažna?

## Opaženo prema očekivanom

Kategorički podaci počinju frekvencijama i udjelima. Frekvencija govori koliko
je jedinica u ćeliji, a udio je stavlja u odnos prema jasnom nazivniku.
Kontingencijska tablica prikazuje zajedničku raspodjelu dviju kategoričkih
varijabli. Postoci po retku i postoci po stupcu odgovaraju na različita pitanja.

Model nezavisnosti čuva rubne zbrojeve i raspoređuje ih kao da pripadnost jednoj
kategoriji ne mijenja raspodjelu druge. **Hi-kvadrat statistika** zbraja
standardizirana odstupanja opaženih od očekivanih frekvencija. Veliko
odstupanje pokazuje neusklađenost s nezavisnošću, ali još ne pokazuje koje su
ćelije odgovorne.

Standardizirani reziduali vraćaju se u ćelije. Pozitivan rezidual označava više
opažanja od očekivanog, a negativan manje. Cramérovo V sažima jačinu veze na
zajedničkoj ljestvici. Test i veličina veze zato odgovaraju na odvojena pitanja.

## Granice aproksimacije

Hi-kvadrat test oslanja se na aproksimaciju koja slabi kada su očekivane
frekvencije vrlo male. Spajanje kategorija može pomoći samo ako ima sadržajno
opravdanje. Kategorije se ne smiju spojiti zato da bi rezultat postao povoljniji
ili da bi nestala teško objašnjiva skupina.

Za malu tablicu Fisherov egzaktni test računa vjerojatnost mogućih rasporeda uz
fiksne rubne zbrojeve. Njegov naziv ne znači da je svaki drugi test približno
netočan. Označava drugačiji način računanja pod nultim modelom.

Stratificirana analiza zatim pita ostaje li veza slična unutar podskupina.
Simpsonov paradoks iz prvog poglavlja vraća se u formalnijem obliku. Zbirna
tablica može miješati odnose i različitu zastupljenost slojeva
(Simpson, 1951).

## Interakcija — Očekivano i opaženo

Planirani prikaz dopušta mijenjanje opaženih ćelija uz jednake rubne zbrojeve.
Očekivane frekvencije ostaju referentna mreža, a doprinos svake ćelije ukupnoj
statistici postaje vidljiv.

**Što isprobati.**

1. Postavite opažene frekvencije jednake očekivanima.
2. Premjestite opažanja između dviju ćelija uz iste rubne zbrojeve.
3. Smanjite očekivane frekvencije i promatrajte granicu aproksimacije.

**Statistika u divljini.**
**Zbirna tablica upisa.** U Berkeleyjskim podacima zbirni ishod prijave i spol
nisu raspoređeni kao pod jednostavnim modelom nezavisnosti (Bickel, 1975).
Takav rezultat opisuje povezanost u tablici, ali ne određuje mehanizam.

Raspodjela prijava po odjelima mijenja zbirni obrazac. Analiza zato treba
reziduale, veličinu veze i stratifikaciju, a ne samo jednu p-vrijednost.

**Pitajte model.**
Asistent može izraditi kontingencijsku tablicu, očekivane frekvencije i
reziduale. Treba provjeriti koji je nazivnik koristio za postotke, jesu li
očekivane ćelije dovoljno velike i je li uz test izvijestio veličinu veze.
Modeli često značajnu povezanost opisuju kao snažnu.

> Prikaži frekvencije i postotke s jasnim nazivnikom, izračunaj očekivane
> frekvencije i standardizirane reziduale te uz test navedi Cramérovo V.

**Nađite grešku.**
Očekivane frekvencije zadovoljavaju uvjete, a hi-kvadrat test pokazuje
neusklađenost s nezavisnošću. Reziduali otkrivaju ćelije koje najviše
doprinose. Budući da je rezultat značajan, veza je snažna.

Greška je zaključak o snazi veze iz statističke značajnosti. Jačina se
procjenjuje mjerom poput Cramérova V i čita u sadržajnom kontekstu.

## Razrađeni primjer

Ugrađeni podaci `UCBAdmissions` omogućuju reprodukciju zbirne tablice
Berkeleyjskog slučaja (Bickel, 1975). Analiza najprije zbraja odjele i stvara
tablicu ishoda prema spolu. Zatim uspoređuje opažene i očekivane frekvencije.

*Slika. Opažene frekvencije i test nezavisnosti za zbirne podatke. Izrada autora prema @bickel1975.*

Test sažima neusklađenost zbirne tablice s nezavisnošću. Povratak odjelima
pokazuje da taj rezultat miješa više slojeva. Statistički korektan izvještaj
zato ne preuzima kauzalni jezik i ne zaustavlja se na zbirnoj tablici.

## Sažetak

Kategorički podaci traže jasno brojanje i nazivnike prije testiranja. Hi-kvadrat
uspoređuje opažene i očekivane frekvencije, reziduali vraćaju zaključak u
ćelije, a Cramérovo V opisuje jačinu veze. Male očekivane frekvencije i skriveni
slojevi ograničavaju jednostavno čitanje. Sljedeće poglavlje istu logiku
usporedbe prenosi na brojčani ishod i dvije skupine.

## Pojmovi

kontingencijska tablica (*contingency table*), očekivana frekvencija (*expected
frequency*), hi-kvadrat test (*chi-squared test*), standardizirani rezidual
(*standardized residual*), Cramérovo V (*Cramér's V*), Fisherov egzaktni test
(*Fisher's exact test*)

## Zadaci

### Konceptualni

Objasnite razliku između testa nezavisnosti i mjere jačine veze. Predajte dvije
rečenice koje se mogu pojaviti u istom izvještaju.

### Računski

Upotrijebite `UCBAdmissions`. Izračunajte zbirni test i zasebne tablice po
odjelima te predajte usporedbu (Bickel, 1975).

### Kritički

Prosudite što zbirna kontingencijska tablica može reći o upisima, a što gubi
bez odjela (Bickel, 1975). Predajte jedan odlomak.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točne dijagnostičke korake,
jedan pogrešan zaključak i prikladnu mjeru koja nedostaje.

---

# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Cumming je usporedbu skupina smjestio u okvir procjene razlike i njezina
intervala, umjesto odluke koja završava oznakom značajnosti (Cumming, 2014).
Time se uredničko pitanje mijenja. Nije dovoljno znati prolazi li rezultat
prag. Treba znati kolika je razlika i koje su veličine još spojive s podacima.

Isti brojčani ishod može nastati iz dviju neovisnih skupina, iz ponovljenog
mjerenja istih osoba ili iz usporedbe jednog uzorka s referentnom vrijednošću.
Računi izgledaju srodno, ali jedinica neovisnosti nije ista.

Kako jednu usporedbu dviju sredina povezati s dizajnom, učinkom i općim jezikom
modela?

## Jedna razlika, tri dizajna

Jednouzoračni t-test uspoređuje sredinu uzorka s referentnom vrijednošću.
Neovisni t-test uspoređuje dvije skupine različitih jedinica. Upareni t-test
svodi ponovljena mjerenja na razliku unutar iste jedinice i analizira te
razlike. Odabir testa zato počinje pitanjem tko ili što nosi dva rezultata.

Welchova inačica neovisnog testa ne zahtijeva jednake varijance i razuman je
početni izbor kada nema snažnog razloga za strožu pretpostavku. Normalnost se
procjenjuje na razini ostataka ili razlika relevantnih za model, a ne
mehaničkim testom nad svakim stupcem.

Krajnja opažanja traže pregled, ne automatsko brisanje. Mogu biti pogreške,
rijetki legitimni slučajevi ili znak da sredina nije prikladan sažetak.
Wilcoxonov postupak mijenja pitanje prema rangovima i nije samo t-test koji se
uključuje kada jedan test normalnosti prijeđe prag.

## Binarni prediktor kao model

Usporedba dviju skupina može se zapisati linearnim modelom u kojem kategorija
predviđa brojčani ishod. Početna vrijednost predstavlja sredinu referentne
skupine, a koeficijent skupine njihovu razliku. Time t-test postaje poseban
slučaj jezika koji će se proširiti u poglavlju o regresiji.

Model ne zamjenjuje dizajn. Koeficijent opisuje prilagođenu ili neprilagođenu
razliku ovisno o uključenim varijablama, dok kauzalno značenje dolazi iz načina
dodjele skupina. Izvještaj najprije daje razliku u izvornim jedinicama i
interval, zatim test i standardiziranu veličinu učinka.

## Interakcija — Uzorkivač dviju grupa

Uzorkivač dviju grupa prikazuje preklapanje pojedinačnih rezultata i
raspodjelu procijenjene razlike kroz ponavljanja. Čitatelj odvojeno mijenja
stvarnu razliku, varijabilnost i veličinu uzorka.

**Što isprobati.**

1. Povećajte razliku uz jednaku varijabilnost.
2. Povećajte varijabilnost uz jednaku razliku.
3. Pretvorite neovisni dizajn u upareni i promatrajte što se računa.

**Statistika u divljini.**
**Interval umjesto etikete.** Pristup usmjeren na procjenu traži razliku i
interval prije zaključka o testu (Cumming, 2014). Dvije studije mogu imati sličnu
procjenu, ali različitu preciznost, pa će binarna oznaka sakriti ono što ih
najviše razlikuje.

Graf pojedinačnih opažanja dodatno pokazuje preklapanje i krajnje slučajeve.
Sredine bez raspodjela pretvaraju dvije skupine u dvije točke.

**Pitajte model.**
Asistent može odabrati t-test tek nakon što dobije opis dizajna i identifikator
jedinice. Treba provjeriti je li uparivanje sačuvano, koristi li Welchovu
inačicu za neovisne skupine i izvještava li razliku, interval i učinak. Modeli
često zamijene neovisni i upareni dizajn.

> Prepoznaj jesu li mjerenja neovisna ili uparena. Prikaži pojedinačna
> opažanja, procijeni razliku s intervalom i tek zatim provedi odgovarajući
> test.

**Nađite grešku.**
Iste su osobe mjerene prije i nakon intervencije, a svi parovi imaju ispravan
identifikator. Analiza je ipak provedena kao test dviju neovisnih skupina jer
svaki stupac sadrži zasebne vrijednosti.

Greška je zanemarivanje uparenog dizajna. Jedinica analize je promjena unutar
osobe, pa se testiraju razlike parova.

## Razrađeni primjer

Simuliramo dvije neovisne skupine s brojčanim ishodom. Analiza izračunava
razliku sredina, Welchov interval i standardizirani učinak. Simulacija ne
predstavlja stvarnu studiju, nego pokazuje redoslijed izvještavanja.

*Slika. Procjena razlike u simuliranim skupinama. Izrada autora.*

Interval pokazuje koje su razlike usklađene s ovim uzorkom. Izvještaj još
treba opis skupina, raspodjele i dizajn dodjele. Tek nasumična dodjela može
razliku uvjerljivo povezati s intervencijom.

## Sažetak

Usporedba dviju grupa počinje dizajnom i jedinicom neovisnosti. Jednouzoračni,
neovisni i upareni postupak različite su inačice iste logike procjene razlike.
Linearni model s binarnim prediktorom otkriva zajednički okvir, dok učinak i
interval čuvaju sadržajno značenje. Sljedeće poglavlje širi isti model na više
skupina i uvodi problem mnogih usporedbi.

## Pojmovi

neovisne skupine (*independent groups*), upareni podaci (*paired data*),
Welchov t-test (*Welch's t-test*), razlika sredina (*mean difference*),
binarni prediktor (*binary predictor*), Wilcoxonov test (*Wilcoxon test*)

## Zadaci

### Konceptualni

Razlikujte neovisni i upareni dizajn prema jedinici analize. Predajte po jedan
primjer i objasnite što se u svakom uspoređuje.

### Računski

Upotrijebite `sim_dvije`. Izračunajte razliku, interval i Cohenov d te
predajte jedan odlomak interpretacije.

### Kritički

Prosudite zašto interval razlike nosi više informacija od same oznake
značajnosti (Cumming, 2014). Predajte kratku bilješku recenzentu.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte stvarni dizajn, jednu pogrešku u
testu i rezultat koji bi trebalo računati.

---

# Uspoređivanje više grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Analitička fleksibilnost postaje posebno vidljiva kada istraživanje sadrži više
skupina i ishoda. Svaka nova parna usporedba daje još jednu priliku da
slučajnost proizvede privlačan rezultat, čak i kada pojedinačni testovi slijede
uobičajeni prag (Simmons, 2011).

Istraživač zato prvo postavlja zajedničko pitanje o cijelom skupu sredina.
Tek nakon njega traži parove ili kontraste koji nose sadržajnu razliku. Time se
analiza usklađuje s pitanjem, a ne s najpovoljnijim rezultatom.

Kako više skupina usporediti kao jedan model, a zatim objasniti gdje se razlike
nalaze?

## Varijanca između i unutar

Analiza varijance uspoređuje razlike među sredinama s razlikama među
pojedincima unutar skupina. Ako su skupne sredine daleko, a opažanja unutar
svake skupine razmjerno zbijena, omjer tih dviju vrsta varijacije raste.
**F-statistika** sažima upravo taj odnos.

Naziv ANOVA može zavesti jer je ishod usporedba sredina, a račun prolazi kroz
varijancu. Postupak je linearni model s kategoričkim prediktorom. Svaka
kategorija određuje očekivanu vrijednost, dok reziduali opisuju ono što skupna
pripadnost nije objasnila.

Ukupni test ne govori koja se skupina razlikuje. Tukeyjev postupak uspoređuje
parove uz kontrolu obiteljske pogreške. Planirani kontrasti mogu biti
učinkovitiji kada proizlaze iz unaprijed postavljenog pitanja. Naknadno
pregledavanje svih mogućih parova i prijavljivanje samo zanimljivih vraća
problem nevidljivih putova.

## Veličina i pretpostavke

Eta-kvadrat opisuje udio varijabilnosti povezan sa skupnim razlikama, ali može
biti pristran prema većim vrijednostima u malim uzorcima. Omega-kvadrat nudi
konzervativniju procjenu. Obje mjere trebaju interval ili barem jasnu napomenu o
preciznosti i kontekstu.

Pretpostavke se pregledavaju na rezidualima. Neovisnost dolazi iz dizajna,
približna normalnost iz oblika ostataka, a homogenost varijance iz usporedbe
raspršenosti skupina. Kruskal-Wallisov test prelazi na rangove kada je takvo
pitanje prikladnije, ali ni on ne popravlja ovisna opažanja ili loš dizajn.

## Interakcija — Dekompozicija varijance

Planirana dekompozicija prikazuje ukupno odstupanje kao dio između skupina i
dio unutar njih. Pomicanjem sredina ili raspršivanjem opažanja čitatelj vidi
zašto isti razmak sredina ne daje uvijek isti F-omjer.

**Što isprobati.**

1. Izjednačite sredine uz nepromijenjena opažanja.
2. Razmaknite sredine uz jednaku varijabilnost.
3. Povećajte raspršenost unutar skupina bez promjene sredina.

**Statistika u divljini.**
**Mnogo usporedbi, jedna priča.** Fleksibilan izbor ishoda i podskupina može
povećati stopu lažno pozitivnih nalaza i kada svaki pojedinačni test izgleda
uobičajeno (Simmons, 2011).

Zajednički model i unaprijed obrazloženi kontrasti čine obitelj pitanja
vidljivom. Korekcija nije kazna za istraživača, nego računovodstvo prilika koje
je postupak dao slučajnosti.

**Pitajte model.**
Asistent može provesti ANOVA-u i post-hoc usporedbe, ali treba mu zadati
planirane kontraste i referentnu skupinu. Provjeravamo reziduale, broj
usporedbi, korekciju i veličinu učinka. Modeli često iz značajnog ukupnog testa
izvode tvrdnju da se svaka skupina razlikuje od svake druge.

> Prikaži skupne raspodjele, procijeni zajednički model i tek nakon ukupnog
> testa provedi unaprijed obrazložene usporedbe. Izvijesti korekciju, učinak i
> intervale razlika.

**Nađite grešku.**
Ukupni F-test pokazuje da model sa skupinama poboljšava opis podataka, a
reziduali ne otkrivaju ozbiljan problem. Zato se sve skupine međusobno
statistički razlikuju.

Greška je zaključak o svim parovima iz ukupnog testa. Potrebne su planirane ili
post-hoc usporedbe s odgovarajućom kontrolom višestrukosti.

## Razrađeni primjer

Simuliramo tri skupine i brojčani ishod. Graf bi trebao prethoditi modelu, a
kod zatim procjenjuje zajedničku ANOVA-u. Tukeyjev postupak dolazi nakon
ukupnog pitanja i pokazuje koji su parovi dovoljno precizno razdvojeni.

*Slika. Tukeyjeve usporedbe simuliranih skupina. Izrada autora.*

Parne procjene imaju vlastite intervale i ne moraju sve voditi prema istoj
odluci. Sadržajni zaključak vraća se veličinama razlika, a ne samo oznakama
nakon korekcije.

## Sažetak

ANOVA uspoređuje varijaciju između skupina s varijacijom unutar njih i time
više sredina smješta u jedan linearni model. Ukupni test ne identificira
parove, pa nakon njega dolaze planirani kontrasti ili korigirane post-hoc
usporedbe. Veličina učinka i reziduali ostaju nužni za tumačenje. Sljedeće
poglavlje uklanja granicu između „testova" i pokazuje linearni model kao opći
okvir.

## Pojmovi

analiza varijance (*analysis of variance*), F-statistika (*F-statistic*),
varijanca između skupina (*between-group variance*), Tukeyjev HSD (*Tukey's
HSD*), eta-kvadrat (*eta squared*), Kruskal-Wallisov test
(*Kruskal–Wallis test*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Predajte skicu triju sredina koja to pokazuje.

### Računski

Upotrijebite `sim_vise`. Procijenite ukupni model, eta-kvadrat i Tukeyjeve
usporedbe te predajte jednu tablicu.

### Kritički

Prosudite kako broj analitičkih putova utječe na čitanje najmanje p-vrijednosti
među mnogim skupinama (Simmons, 2011). Predajte jedan odlomak.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točan zaključak o ukupnom
modelu, jednu neopravdanu tvrdnju o parovima i potreban nastavak analize.

---

# Regresija, opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Breiman je suprotstavio dvije kulture statističkog modeliranja. Jedna je
naglašavala objašnjenje odnosa kroz podatkovni model, a druga prediktivnu
uspješnost algoritma na novim podacima (Breiman, 2001). Razlika nije bila samo
tehnička. Određivala je što se smatra dobrim odgovorom.

Model može precizno opisati prosječnu povezanost, slabo predviđati pojedince i
ne govoriti ništa sigurno o uzroku. Drugi model može dobro predviđati, a ostati
težak za sadržajno objašnjenje. Isti podatak ne rješava automatski sva tri
zadatka.

Kako linearni model povezati s ranijim usporedbama, a pritom odvojiti opis,
predviđanje i uzročni zaključak?

## Pravac i pogreške

Jednostavna regresija traži pravac koji sažima očekivani ishod duž vrijednosti
prediktora. Svako opažanje ostavlja **rezidual**, okomitu razliku između
opažene i modelirane vrijednosti. Metoda najmanjih kvadrata bira koeficijente
koji čine zbroj kvadrata tih razlika najmanjim.

Nagib opisuje prosječnu promjenu ishoda povezanu s jediničnom promjenom
prediktora. Odsječak je očekivani ishod kada prediktor ima referentnu
vrijednost. Ako ta vrijednost nema smisla u podacima, odsječak je računski
potreban, ali sadržajno slab. Centriranje prediktora može mu dati korisniju
referencu bez promjene pristajanja modela.

R-kvadrat opisuje udio varijabilnosti ishoda koji model sažima u promatranom
uzorku. Nije ocjena istinitosti, ne jamči dobru predikciju na novim podacima i
ne određuje važnost pojedinog koeficijenta. Visoka vrijednost može pripadati
modelu koji promašuje uzročni mehanizam.

## Više prediktora i kontrola

Višestruka regresija procjenjuje povezanost jednog prediktora s ishodom uz
jednake vrijednosti ostalih uključenih prediktora. Izraz „uz kontrolu" opisuje
računsku usporedbu, a ne eksperimentalnu kontrolu. Ako važan konfundirajući
čimbenik nije izmjeren ili je loše izmjeren, koeficijent ga ne može ukloniti.

Prediktori koji nose vrlo sličnu informaciju međusobno dijele objašnjenje.
Koeficijenti tada mogu postati nestabilni i osjetljivi na male promjene uzorka.
Multikolinearnost nije dokaz da su podaci pogrešni. Pokazuje da uzorak teško
razdvaja doprinose prediktora koji se zajedno kreću.

Poglavlja o dvjema i više skupina već su koristila isti okvir. Binarni
prediktor modelira razliku dviju sredina, a kategorički prediktor skup sredina.
T-test i ANOVA nisu otoci izvan regresije, nego posebni oblici istog modela.

## Dijagnostika prije priče

Rezidualni prikaz provjerava ostaje li nakon pravca sustavan obrazac.
Zakrivljenost upućuje na pogrešan funkcijski oblik, lijevak na promjenjivu
varijancu, a izdvojene točke na mogući utjecaj pojedinih opažanja. Dijagnostika
ne daje automatsku odluku o brisanju, nego pokazuje gdje model treba
obrazloženje ili promjenu.

Predviđanje se provjerava na podacima koji nisu sudjelovali u prilagodbi
modela. Dobro pristajanje u uzorku može biti rezultat učenja njegove slučajne
buke. Ta se granica između pristajanja i generalizacije u sljedećem poglavlju
pretvara u središnji problem algoritamskih modela.

Uzročna tvrdnja zahtijeva više od popisa kontrolnih varijabli. Potrebni su
vremenski redoslijed, uvjerljiva struktura konfundiranja i dizajn koji opravdava
usporedbu. Regresija može izvesti prilagođenu povezanost. Ne može iz samih
podataka odlučiti koje je varijable trebalo mjeriti niti jesu li posljedica,
uzrok ili zajednički ishod.

## Interakcija — Regresijski pravac

Regresijski pravac u planiranoj interakciji može se pomicati preko oblaka
točaka. Svaki pomak mijenja reziduale i njihov kvadrat, dok drugi prediktor
pokazuje kako se prilagođeni nagib razlikuje od zbirnog odnosa.

**Što isprobati.**

1. Pomaknite pravac i pronađite položaj s najmanjim kvadratima reziduala.
2. Dodajte jedno utjecajno opažanje.
3. Uključite drugi prediktor i usporedite zbirni s prilagođenim nagibom.

**Statistika u divljini.**
**Dvije kulture modeliranja.** Breiman je opisao napetost između modela
usmjerenih na podatkovni mehanizam i algoritamskih postupaka usmjerenih na
predikciju (Breiman, 2001).

Članak koji model naziva „boljim" mora zato navesti kriterij. Bolje pristajanje,
stabilniji koeficijent, manja pogreška na novim podacima i uvjerljiviji uzročni
dizajn nisu ista postignuća.

**Pitajte model.**
Asistent može prilagoditi model, izraditi dijagnostičke grafove i prevesti
koeficijente u prozu. Treba mu zadati ulogu svake varijable, referentne
kategorije i cilj analize. Provjeravamo kod, jedinice, reziduale, podatke za
provjeru predikcije i svaki prijelaz iz povezanosti prema uzroku.

> Prilagodi linearni model i protumači koeficijente u izvornim jedinicama.
> Prikaži intervale, dijagnostiku reziduala i odvojenu provjeru predikcije.
> Uzročni jezik koristi samo ako ga dizajn izričito opravdava.

**Nađite grešku.**
Model uključuje dob, obrazovanje i početni rezultat, a rezidualni prikazi ne
pokazuju velik problem. Koeficijent korištenja platforme zato predstavlja
čisti uzročni učinak korištenja na ishod.

Greška je pretvaranje prilagođene povezanosti u čisti uzročni učinak. Uključene
kontrole ne jamče da su izmjereni svi konfunderi niti rješavaju obrnuti smjer.

## Razrađeni primjer

Simuliramo odnos vremena provedenog uz sadržaj, prethodnog interesa i
angažmana. Budući da interes utječe i na vrijeme i na ishod, jednostavni nagib
miješa dvije priče. Višestruki model procjenjuje odnos vremena s angažmanom uz
jednaku razinu simuliranog interesa.

*Slika. Koeficijenti jednostavnog i prilagođenog simuliranog modela. Izrada autora.*

Razlika koeficijenata pokazuje što račun znači pod ovom poznatom simulacijom.
U stvarnoj opažačkoj studiji ne bismo znali jesmo li izmjerili sve potrebne
čimbenike. Prilagodba je transparentna usporedba pod uvjetom uključenih
varijabli, a ne automatska identifikacija uzroka.

Model se zatim provjerava na rezidualima i, za predikcijski cilj, na odvojenim
podacima. Koeficijenti služe objašnjenju prosječnih odnosa, a pogreška
predikcije procjenjuje uporabljivost za nove jedinice. Oba rezultata pripadaju
istom modelu, ali odgovaraju na različita pitanja.

## Sažetak

Regresija ujedinjuje usporedbu skupina i odnose brojčanih varijabli u jednom
jeziku očekivanih vrijednosti i reziduala. Više prediktora daje prilagođene
povezanosti, ali riječ „kontrola" ne stvara eksperiment. Dijagnostika pokazuje
gdje model ne pristaje, dok provjera na novim podacima odvaja pristajanje od
predikcije. Sljedeće poglavlje širi predikcijski cilj na klasifikaciju,
algoritamsko rangiranje i društvene posljedice pogrešaka.

## Pojmovi

linearna regresija (*linear regression*), rezidual (*residual*), metoda
najmanjih kvadrata (*least squares*), koeficijent determinacije
(*R-squared*), višestruka regresija (*multiple regression*), multikolinearnost
(*multicollinearity*), predikcija (*prediction*)

## Zadaci

### Konceptualni

Objasnite kako su t-test i ANOVA posebni slučajevi linearnog modela. Predajte
jednu skicu s binarnim i jednom s višerazinskim prediktorom.

### Računski

Upotrijebite `sim_reg`. Usporedite jednostavni i prilagođeni model, nacrtajte
reziduale i predajte tablicu koeficijenata.

### Kritički

Prosudite tvrdnju da model s boljim pristajanjem nužno daje bolje objašnjenje i
predikciju (Breiman, 2001). Predajte dva odvojena kriterija provjere.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite ispravne dijagnostičke tvrdnje,
jedan uzročni skok i dodatni dizajnerski dokaz koji bi bio potreban.

---

# Statistika u doba algoritama

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Chouldechova je analizirala instrumente za predviđanje povratka u kriminal i
pokazala da se poželjna mjerila pravednosti mogu sukobiti kada se temeljne
stope razlikuju među skupinama (Chouldechova, 2017). Jednako tumačenje
predviđenog rizika, jednake stope lažno pozitivnih odluka i jednaka ukupna
točnost ne mogu se uvijek postići istodobno.

To nije samo matematička neugodnost. Prag modela odlučuje tko će biti
zaustavljen, provjeren, preporučen ili uskraćen. Pogreške imaju različite
posljedice, a zbirna ocjena skriva na koga padaju.

Kako statistički čitati algoritam koji ne opisuje samo društvo, nego sudjeluje
u raspodjeli pažnje, prilika i rizika?

## Predikcija na novim podacima

Algoritamski model uči obrazac na skupu za treniranje i provjerava ga na
odvojenom skupu za testiranje. Razdvajanje postoji zato što model može naučiti
slučajnu posebnost podataka koje je već vidio. **Preprilagodba** nastaje kada
pristajanje treningu raste, a sposobnost generalizacije na nove slučajeve
slabi.

Predikcija i objašnjenje postavljaju različite kriterije dobrog modela
(Breiman, 2001). Predikcijski model vrednuje pogrešku na novim podacima.
Objašnjavajući model traži koeficijente i strukturu koje možemo povezati s
teorijom. Visoka prediktivna uspješnost ne pretvara korištene varijable u
uzroke.

Klasifikacija prevodi rezultat modela u kategoriju pomoću praga. Pomicanje
praga mijenja odnos lažno pozitivnih i lažno negativnih odluka. Ne postoji
prag koji minimizira svaku vrstu pogreške bez odluke o njihovoj cijeni.

## Algoritam kao društvena infrastruktura

Sustav preporuke ne predviđa samo što će osoba možda odabrati. Rangiranjem
sadržaja mijenja ono što osoba uopće može vidjeti. Podaci o prethodnom
ponašanju tako postaju ulaz u okruženje koje proizvodi sljedeće ponašanje.
Promatrač i predmet promatranja ulaze u povratnu petlju.

Metrika poput vremena zadržavanja nije neutralna zamjena za zadovoljstvo,
informiranost ili javnu vrijednost. Ona operacionalizira cilj sustava.
Optimizacija zatim vrlo učinkovito povećava ono što je izmjereno, uključujući
slučajeve u kojima mjera slabo predstavlja društvenu svrhu.

Društvenoznanstveno pitanje zato uključuje vlasništvo nad podacima, institucionalni
cilj, mogućnost žalbe i skupine koje nose pogreške. Tehnička dokumentacija
modela nije potpuna bez opisa konteksta njegove uporabe.

## Pravednost i temeljne stope

Mjere pravednosti promatraju različite dijelove tablice odluka. Jednaka stopa
lažno pozitivnih odluka usredotočuje se na osobe bez ishoda. Jednaka
prediktivna vrijednost pita koliko je pozitivnih odluka doista pozitivno.
Kada se temeljne stope razlikuju, ta se mjerila mogu matematički razići
(Chouldechova, 2017; Barocas, 2023).

Izbor mjerila nije samo tehnički. On određuje koju vrstu pogreške i koju
populaciju sustav štiti. Poštena analiza zato prikazuje više mjerila po skupini,
objašnjava prag i navodi institucionalnu posljedicu svake pogreške.

## Jezični modeli kao distribucije

Veliki jezični model proizvodi tekst predviđanjem sljedećih dijelova niza iz
raspodjele naučene na velikom korpusu. Tečnost je rezultat uspješnog
modeliranja jezičnih obrazaca. Nije ugrađena provjera da tvrdnja odgovara
stvarnom izvoru.

Model može dati korisnu strukturu, kod ili alternativno objašnjenje, ali
činjenice moraju ostati vezane uz provjerljive dokumente i podatke. Kada izvor
nije dostupan, odgovoran odgovor označava prazninu. Samouvjerena rečenica bez
podrijetla samo je predikcija koja zvuči kao znanje.

## Interakcija — Istraživač pravednosti

Istraživač pravednosti mijenja klasifikacijski prag za dvije skupine s
različitim temeljnim stopama. Uz isti model čitatelj promatra kako se točnost,
lažno pozitivne i lažno negativne odluke te prediktivna vrijednost ne kreću
zajedno.

**Što isprobati.**

1. Primijenite isti prag na skupine s jednakim temeljnim stopama.
2. Promijenite temeljnu stopu jedne skupine.
3. Pokušajte istodobno izjednačiti više mjerila pravednosti.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Analiza instrumenata za procjenu rizika
pokazala je sukob između kalibracije i jednakosti određenih stopa pogreške kada
se temeljne stope razlikuju (Chouldechova, 2017).

Tvrdnja da je model „pravedan" zato nije potpuna bez imenovanja mjerila,
skupina, praga i posljedica. Agregatna točnost može ostati jednaka dok se vrste
pogrešaka vrlo nejednako raspoređuju.

**Pitajte model.**
Asistent može izračunati tablice zabune i mjerila po skupinama. Treba mu dati
stvarne ishode, predviđene rezultate i prag, bez osobnih identifikatora.
Provjeravamo nazivnike svake stope i tražimo da sukob mjerila ne riješi
neobrazloženom tvrdnjom da je jedno „najpoštenije".

> Izračunaj tablicu zabune i stope pogrešaka zasebno po skupinama. Objasni kako
> prag i temeljne stope mijenjaju mjerila, a vrijednosni izbor ostavi jasno
> označenim.

**Nađite grešku.**
Model ima jednaku ukupnu točnost u dvjema skupinama, a prag je za obje jednak.
Zato je algoritam pravedan i nije potrebno pregledavati zasebne stope pogreške.

Greška je zaključak da jednaka ukupna točnost dokazuje pravednost. Lažno
pozitivne i lažno negativne odluke mogu se različito rasporediti unatoč istoj
točnosti.

## Razrađeni primjer

Simuliramo dvije skupine s različitim temeljnim stopama i isti bučni
prediktivni rezultat. Jedan zajednički prag pretvara rezultat u odluku.
Izračun ne tvrdi da je neka stvarna skupina takva. Pokazuje kako nazivnici
stvaraju različita mjerila.

*Slika. Stope pogrešaka u simuliranom klasifikacijskom primjeru. Izrada autora prema @barocas2023.*

Tablica pokazuje da jedno mjerilo ne opisuje cijelu raspodjelu odluka.
Promjena praga može smanjiti jednu pogrešku i povećati drugu. Odluka o
prihvatljivom odnosu zahtijeva znanje o posljedicama, mogućnosti žalbe i
instituciji koja model primjenjuje.

Ista disciplina vrijedi za sustave preporuke i jezične modele. Prije procjene
rezultata moramo znati koji je cilj optimiziran, na kojim je podacima sustav
učen i kako njegove pogreške ulaze u društvenu praksu.

## Sažetak

Algoritamski model procjenjujemo na novim podacima i prema cilju koji je doista
optimiziran. Klasifikacijski prag raspoređuje vrste pogrešaka, a različite
temeljne stope mogu dovesti mjerila pravednosti u sukob. Sustavi preporuke
mijenjaju okruženje koje mjere, dok jezični modeli proizvode tečan tekst bez
ugrađenog jamstva istinitosti. Statistička pismenost zato ostaje odgovornost za
izvor, nazivnik, cilj i posljedice odluke.

## Pojmovi

skup za treniranje (*training set*), skup za testiranje (*test set*),
preprilagodba (*overfitting*), klasifikacijski prag (*classification
threshold*), tablica zabune (*confusion matrix*), temeljna stopa (*base rate*),
algoritamska pravednost (*algorithmic fairness*)

## Zadaci

### Konceptualni

Objasnite zašto jednaka ukupna točnost ne jamči jednake posljedice za dvije
skupine. Predajte dvije moguće tablice zabune.

### Računski

Promijenite prag u objektu `sim_klasifikacija` i predajte graf dviju stopa
pogreške po skupini.

### Kritički

Prosudite zašto se mjerila pravednosti mogu sukobiti kada se temeljne stope
razlikuju (Chouldechova, 2017; Barocas, 2023). Predajte odlomak bez proglašenja
jednog mjerila univerzalno najboljim.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dvije stvarne provjere, jednu
neopravdanu tvrdnju o pravednosti i mjerila koja još treba prikazati.
