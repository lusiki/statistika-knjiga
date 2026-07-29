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
