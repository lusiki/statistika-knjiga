# Vjerojatnost koliko treba

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Simulator novčića i A/B kampanje | simulirana populacija | pogl. 4 |

**Vinjeta.**
Igrači, treneri i navijači godinama su tvrdili isto. Košarkaš koji je pogodio
nekoliko puta zaredom u tom je trenutku „vruć", pa mu sljedeći pokušaj ima veće
izglede nego inače. Gilovich, Vallone i Tversky uzeli su tu tvrdnju ozbiljno i
proveli je kroz zapise stvarnih utakmica, a zaključili su da je riječ o krivom
čitanju slučajnih nizova (Gilovich, 1985).

Nalaz nije rekao da se ljudi zanose. Rekao je nešto neugodnije, da niz koji
izgleda kao obrazac slučajnost proizvodi sama od sebe, pa oko njega nema što
objašnjavati. Trideset godina kasnije pokazalo se da ni sam postupak mjerenja
nije bio bezazlen, o čemu ovo poglavlje govori pred kraj.

Kako razlikovati obrazac od onoga što slučajnost proizvodi bez ijednog razloga?

## Što vjerojatnost broji

Pošten novčić bacimo dvadeset puta i prebrojimo glave. Sljedećih dvadeset puta
broj će gotovo sigurno biti drugačiji, a nakon nekoliko takvih serija postaje
jasno da jedan rezultat nije obećanje nego uzorak iz nečega većega. To veće
opisuje vjerojatnost.

**Vjerojatnost** je broj između nule i jedinice koji događaju pridružuje
udio ishoda u kojima se on pojavljuje, pri čemu nula znači da se događaj ne
može dogoditi, a jedinica da se mora dogoditi.

Taj se broj čita na dva načina i oba su u knjizi u upotrebi. U postupku koji se
može ponoviti mnogo puta vjerojatnost je dugoročna učestalost, dakle udio
ponavljanja u kojima se događaj pojavi. U situaciji koja se neće ponoviti isti
broj izražava stupanj uvjerenja pod jasno navedenim informacijama, i tada je
važno reći na temelju čega je postavljen. Vjerojatnost da nogometna
reprezentacija osvoji sljedeće prvenstvo nije udio ničega, jer se to prvenstvo
igra jednom.

Prvo čitanje ima svojstvo koje se može vidjeti. Kratki nizovi kolebaju se
snažno, dugi se smiruju, i to bez ikakve sile koja bi ih smirivala.

*Slika. Kumulativni udio glava u trima neovisnim nizovima bacanja poštenog novčića. Vodoravna crta označuje vrijednost pola.*

Nakon dvadeset bacanja tri se niza razilaze od
`r hr_broj(s7_rani$najmanji, 2)` do `r hr_broj(s7_rani$najveci, 2)`, dakle
dovoljno da bi netko od njih zaključio kako novčić nije pošten. Nakon dvije
tisuće bacanja svi leže između `r hr_broj(s7_kasni$najmanji, 3)` i
`r hr_broj(s7_kasni$najveci, 3)`. Ta pravilnost ima ime i zove se zakon velikih
brojeva, a kaže da se relativna učestalost s brojem ponavljanja primiče
vjerojatnosti.

Ono što zakon ne kaže važnije je od onoga što kaže. Nijedno pojedinačno bacanje
ne zna što se prije dogodilo i ništa ne nadoknađuje. Udio se ne primiče polovici
zato što se višak glava kompenzira viškom pisama, nego zato što svaki novi
rezultat ulazi u sve veći nazivnik i time sve manje pomiče omjer. Rani je višak
i dalje tu, samo je u dvije tisuće bacanja prestao biti vidljiv.

Očekivanje da se ravnoteža mora vratiti dovoljno je rašireno da ima vlastito ime
i zove se kockarska zabluda. Igrač koji je četiri puta zaredom izgubio drži da mu
je peti put dužan, a analitičar koji je imao tri slaba tjedna očekuje jak. Ista
pogreška u obrnutom smjeru stoji iza vjerovanja iz vinjete, gdje niz pogodaka ne
najavljuje pismo nego novi pogodak. Obje verzije pretpostavljaju da nizovi imaju
pamćenje, a ono što stvarno postoji jest raspon ishoda koji slučajnost proizvodi
i koji je u kratkim nizovima mnogo širi nego što se očekuje.

## Tri pravila i jedna pretpostavka

Računanje s vjerojatnostima oslanja se na tri pravila koja se pamte u jednom
odlomku. Vjerojatnost da se događaj ne dogodi jednaka je jedinici umanjenoj za
vjerojatnost da se dogodi, što je često najbrži put do odgovora. Vjerojatnosti
dvaju ishoda koji se ne mogu dogoditi istovremeno zbrajaju se, a ako se mogu
preklopiti, od zbroja treba oduzeti preklop kako ne bi bio brojen dvaput. Za
vjerojatnost da se dva događaja dogode zajedno pravilo množenja vrijedi samo uz
dodatnu pretpostavku.

Preklop iz drugog pravila lako se previdi, a razlika koju čini vidljiva je na
podacima. U populaciji na kojoj poglavlje radi portal bira
`r hr_broj(s7$p_portal)` % ljudi, a osoba do dvadeset devete godine ima
`r hr_broj(s7$p_mlad)` %. Zbroj ta dva udjela iznosi `r hr_broj(s7$p_zbroj)` %,
dok je stvarni udio onih koji su mladi ili biraju portal
`r hr_broj(s7$p_portal_ili_mlad)` %. Razlika je točno onih
`r hr_broj(s7$p_portal_i_mlad)` % koji su oboje i koje je zbrajanje izbrojilo
dvaput.

Treće pravilo nosi pretpostavku i jedino je od navedenih sadržajno.

**Neovisnost** dvaju događaja znači da saznanje o tome je li se jedan dogodio
ne mijenja vjerojatnost drugoga.

Poglavlje radi na simuliranoj populaciji od pedeset tisuća odraslih osoba, istoj
koju koriste poglavlja o uzorkovanju i procjeni, i ta je populacija u cijelosti
poznata. U njoj društvene mreže kao primarni izvor vijesti bira
`r hr_broj(s7$p_mreze)` % ljudi, a osoba do dvadeset devete godine ima
`r hr_broj(s7$p_mlad)` %. Kad bi te dvije okolnosti bile neovisne, pravilo
množenja dalo bi `r hr_broj(s7$p_umnozak)` % ljudi koji su i mladi i biraju
mreže. Stvarni udio iznosi `r hr_broj(s7$p_oboje)` %, dakle gotovo dvostruko
više.

Račun je ispravan, a pogrešna je pretpostavka koju je koristio. Neovisnost je
tvrdnja o svijetu i provjerava se u podacima, a ne bira zato što pojednostavljuje
množenje. Kad ne vrijedi, potreban je pojam koji razlikuje ukupnu vjerojatnost od
vjerojatnosti unutar neke skupine.

**Uvjetna vjerojatnost** je vjerojatnost događaja izračunata unutar skupine u
kojoj je neki drugi događaj već nastupio.

Među osobama do dvadeset devete godine društvene mreže bira
`r hr_broj(s7$p_mreze_mlad)` %, a među starijima `r hr_broj(s7$p_mreze_ostali)` %.
Televizija ide obrnuto, s `r hr_broj(s7$p_tv)` % u cijeloj populaciji i
`r hr_broj(s7$p_tv_stariji)` % među osobama od šezdeset godina naviše. Razlika
između ukupne i uvjetne vrijednosti upravo je mjera ovisnosti, i kad je nema,
dva se broja poklapaju.

Isto se pitanje u svakodnevnim izvještajima postavlja stalno, iako se rijetko
tako zove. Udio konverzija među posjetiteljima koji su kliknuli na oglas i udio
otvaranja među poslanim porukama uvjetne su vjerojatnosti, i svaka od njih
vrijedi samo za skupinu u čijem je nazivniku. Analiza po segmentima nije ništa
drugo nego niz uvjetnih vjerojatnosti, pa se čita s istim oprezom prema
nazivniku koji je poglavlje o kategoričkim podacima kasnije stavlja u središte.

## Ponovljeni pokušaji s dva ishoda

Mnoga pitanja u društvenim istraživanjima imaju isti oblik. Fiksan je broj
pokušaja, svaki završava na jedan od dva načina, i zanima nas koliko ih je
završilo na prvi. Glasanje, klik, odgovor na poziv i otvaranje poruke stanu u
taj kalup.

**Binomna raspodjela** opisuje broj uspjeha u zadanom broju pokušaja kad svaki
pokušaj ima samo dva ishoda, jednaku vjerojatnost uspjeha i nikakvu vezu s
ostalim pokušajima.

Uz dvadeset objava i vjerojatnost od dva posto da pojedina postane viralna,
raspodjela kaže da nijedna neće biti viralna u `r hr_broj(s7$nijedna)` %
mjeseci. To nije prognoza za jedan mjesec nego opis onoga što niz mjeseci
proizvodi, i upravo takav opis nedostaje kad se jedan loš mjesec tumači kao
promjena u kvaliteti sadržaja.

Tri uvjeta iz definicije rijetko vrijede svi odjednom, i njihovo je propadanje
poučnije od samog računa. Vjerojatnost uspjeha nije jednaka kroz pokušaje ako
se objave razlikuju po dosegu, a pokušaji nisu neovisni ako jedno dijeljenje
poveća vidljivost i time izazove sljedeće. Viralnost je ime za točno to kršenje
neovisnosti, pa je binomna raspodjela za nju loš model, koliko god račun bio
uredan. Isto vrijedi za anketu u kojoj se ispituju dvije osobe iz istog
kućanstva.

Kad uvjeti drže, raspodjela daje dvije korisne stvari odjednom. Očekivani broj
uspjeha jednak je umnošku broja pokušaja i vjerojatnosti uspjeha, pa se lako
pamti i lako provjerava. Raspršenost oko tog broja raste sporije od samog broja
pokušaja, što znači da udio uspjeha postaje sve stabilniji što je kampanja veća,
premda apsolutni broj uspjeha varira sve više. Ta dva smjera stalno se brkaju u
izvještajima, u kojima veći apsolutni raspon prolazi kao znak nestabilnosti, iako
je udio zapravo precizniji nego prije.

Model zato nije opis svijeta nego kontrolirana slika jednog dijela procesa. Ono
što ga čini korisnim jest da se u njemu točno zna što proizvodi slučajnost, pa
opaženi rezultat ima s čime biti uspoređen.

## Interakcija — Simulator novčića i A/B kampanje

Sljedeći prikaz drži stvarnu vjerojatnost uspjeha nepromijenjenom i mijenja samo
duljinu niza. Vidljivo postaje ono zbog čega se kratki nizovi tako lako
pogrešno čitaju, a to je da raspon njihovih ishoda ostaje širok i onda kad se
proces uopće ne mijenja.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu stvarnu vjerojatnost.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na A/B kampanju i postavite stvarnu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

Posljednji korak pokazuje odnos koji stoji iza svega u ovom dijelu knjige. Jedna
kampanja ne može biti neobična sama po sebi, jer se neobičnost mjeri prema
rasponu ishoda koji isti postupak proizvodi. Kad je taj raspon širok, krajnji
rezultat nije dokaz ni o čemu osim o širini raspona.

## Zvonasta krivulja i njezino područje

Raspodjela mnogih ponavljanja iz widgeta ima prepoznatljiv oblik. Simetrična je,
najgušća je u sredini, i prema objema stranama se prorjeđuje sve brže. Taj oblik
u statistici ima posebno mjesto, i ne zato što ga priroda posebno voli.

**Normalna raspodjela** je simetrična zvonasta raspodjela koju u cijelosti
određuju njezino središte i njezina standardna devijacija.

Razlog njezine povlaštenosti nije u tome što je česta u prirodi, nego u tome što
nastaje kad se mnogo malih i međusobno neovisnih doprinosa zbroji. Visina, mjerna
pogreška i rezultat na testu takvi su zbrojevi, a to je i svaki prosjek. Zbog
toga se ista krivulja pojavljuje i tamo gdje pojedinačna opažanja nisu ni blizu
zvonastog oblika, pod uvjetom da ih se dovoljno zbroji. Widget je tu tvrdnju već
pokazao, jer je raspodjela stopa uspjeha zvonasta iako pojedini pokušaj ima samo
dva ishoda. Poglavlje o uzorkovanju od te činjenice gradi cijeli svoj argument.

Dva parametra znače da je oblik uvijek isti, a mijenja se samo gdje leži i
koliko je širok. Iz toga slijedi svojstvo korisno za brzu orijentaciju. Unutar
jedne standardne devijacije od sredine leži oko 68 % vrijednosti, unutar dvije
oko 95 %, a unutar tri oko 99,7 %.

Umjesto da se to pravilo primi na vjeru, izmjerimo ga na dvjema varijablama iste
poznate populacije. Prva je dnevno vrijeme provedeno uz medije, druga je iznos
koji je osoba spremna platiti za pristup sadržaju.

*Slika. Dnevne minute uz medije i spremnost na plaćanje u simuliranoj populaciji, s isprekidanim crtama na jednoj i dvjema standardnim devijacijama od sredine.*

Za dnevne minute pravilo drži. Unutar jedne standardne devijacije nalazi se
`r hr_broj(s7_podrucja$minute[1])` % populacije, unutar dviju
`r hr_broj(s7_podrucja$minute[2])` %, a unutar triju
`r hr_broj(s7_podrucja$minute[3])` %. Odstupanja od 68, 95 i 99,7 postoje i
posljedica su blage nagnutosti udesno, ali su dovoljno mala da orijentacija
ostane upotrebljiva.

Za spremnost na plaćanje pravilo se raspada. Unutar jedne standardne devijacije
leži `r hr_broj(s7_podrucja$iznos[1])` % populacije umjesto oko 68 %, a unutar
triju samo `r hr_broj(s7_podrucja$iznos[3])` % umjesto oko 99,7 %. Razlog je
vidljiv na grafu. Ništa ne plaća `r hr_broj(s7$bez_platnika)` % ljudi, pa se
raspodjela nagomilala na nuli i ima dugi rep udesno. Donja granica od jedne
standardne devijacije ispod sredine pada u negativne iznose, koje nitko ne može
imati, pa ispod nje nema nijedne osobe.

Promjena ljestvice vraća oblik. Ako se pogledaju samo oni koji nešto plaćaju i
njihovi se iznosi logaritmiraju, kako je poglavlje o sažimanju podataka već
pokazalo na vremenu korištenja, pravilo se vraća gotovo točno, s
`r hr_broj(s7_podrucja$log_iznos[1])` %,
`r hr_broj(s7_podrucja$log_iznos[2])` % i
`r hr_broj(s7_podrucja$log_iznos[3])` %. Zvonasti oblik dakle nije bio svojstvo
tih ljudi nego svojstvo ljestvice na kojoj su mjereni.

## Kad podaci ne pristaju krivulji

Postotci unutar područja govore o cjelini i mogu prikriti gdje točno raspodjela
odstupa. Prikaz koji odgovara na to pitanje poreda opažene vrijednosti po
veličini i svaku od njih stavi nasuprot vrijednosti koja bi na tom mjestu bila
očekivana da raspodjela jest normalna. Kad se oblici poklapaju, točke leže na
pravcu.

*Slika. Poredane vrijednosti triju varijabli nasuprot vrijednostima očekivanima pod normalnom raspodjelom. Pravac označuje savršeno poklapanje.*

Svaki oblik odstupanja nosi svoju poruku. Dnevne minute prate pravac gotovo
cijelim rasponom i odižu se tek na desnom kraju, što je potpis blagog repa prema
većim vrijednostima. Spremnost na plaćanje leži vodoravno dok traju nule i zatim
naglo skreće uvis, jer normalna raspodjela na tom mjestu očekuje postupan
prijelaz, a podaci ga nemaju. Logaritmirani iznosi vraćaju se na pravac.

Prikaz ne izriče presudu o tome je li analiza dopuštena. On pokazuje gdje
pretpostavka pristaje, a gdje se lomi, i time razdvaja dvije vrste odstupanja
koje se lako izjednače. Blago odizanje repa uz veliki uzorak rijetko išta
mijenja, dok raspodjela s gomilom na nuli traži drugu ljestvicu ili drugi model.

## Nizovi koje slučajnost proizvodi

Vratimo se pitanju iz vinjete, jer ono ima odgovor koji se može izmjeriti.
Postavimo postupak koji sigurno nema nikakvu memoriju, dakle bacanje poštenog
novčića, i u svakom nizu izdvojimo one pokušaje koji dolaze neposredno iza tri
uzastopna pogotka. Ako su pokušaji neovisni, među izdvojenima bi pogodaka trebalo
biti pola.

*Slika. Prosječan udio pogodaka na pokušajima koji slijede zadani niz pogodaka, u simulaciji poštenog novčića bez ikakve memorije. Izrada autora.*

Pola ih nije. U nizu od stotinu pokušaja prosječan udio iza tri pogotka iznosi
`r hr_broj(s7$nakon_tri_100, 3)`, a u nizu od dvadeset pokušaja pada na
`r hr_broj(s7$nakon_tri_20, 3)`. Postupak pritom nema nikakvu memoriju, jer smo
ga sami napravili takvim. Odstupanje ne dolazi iz procesa nego iz odabira.

Razlog je u konačnosti niza. Kad iz jednog niza izdvojimo upravo ona mjesta koja
dolaze iza tri pogotka, sam uvjet troši pogotke. Niz s malo pogodaka rijetko
uopće nudi takvo mjesto, a u nizu koji ga nudi tri su pogotka već potrošena na
uvjet, pa ih je za promatrano mjesto ostalo manje nego što ih niz prosječno ima.
Prosjek takvih udjela zato leži ispod stvarne vjerojatnosti, i to više što je niz
kraći i uvjet dulji. Uz uvjet od samo jednog pogotka u nizu od stotinu pokušaja
odstupanje pada na `r hr_broj(s7$nakon_jednog_100, 3)` i jedva se primjećuje.

Veličina tog odstupanja nije akademska sitnica. U nizu od stotinu pokušaja ono
iznosi oko četiri postotna boda, što je istog reda kao razlika koju bi netko
tražio da pokaže postojanje forme. Postupak mjerenja time proizvodi pomak u
smjeru zaključka koji se donosi.

Pouka nadilazi košarku i nije o tome tko je bio u pravu. Analiza koja iz podataka
izdvoji jedinice po nekom svojstvu tih istih podataka nije više neutralan pogled
na njih, jer je odabir dio postupka jednako kao i račun koji slijedi. Jedini
pouzdan način da se to provjeri jest pustiti cijeli postupak, s odabirom
uključenim, na podatke u kojima se odgovor unaprijed zna. Upravo to knjiga radi
otkad je populacija poznata, i to je razlog zbog kojeg simulacija u ovim
poglavljima dolazi prije formule.

**Statistika u divljini.**
**Vruća ruka i njezin ispravak.** Zaključak da je vjerovanje u vruću ruku krivo
čitanje slučajnih nizova ušao je u udžbenike i u popularne prikaze kao gotova
činjenica o ljudskoj pameti (Gilovich, 1985). Miller i Sanjurjo pokazali su
poslije da mjera koja se u toj literaturi koristi nosi suptilnu ali znatnu
pristranost, da je izvorna studija na nju osjetljiva i da se nakon ispravka
dugogodišnji zaključak obrće (Miller, 2018).

Ono što se u ovoj epizodi promijenilo nije bio podatak nego postupak njegova
čitanja, i to je razlog zbog kojeg okvir stoji u poglavlju o vjerojatnosti.
Pristranost koju simulacija u prethodnom odjeljku mjeri ista je ona koja je
tridesetak godina ostala neopažena u nizu recenziranih radova. Iz toga ne
slijedi da je vruća ruka dokazana, nego da izvorni nalaz nije bio ono za što je
uzet, i da tvrdnja o odsutnosti učinka traži jednako pažljivo mjerenje kao
tvrdnja o njegovu postojanju.

**Pitajte model.**
Asistent lako izračuna vjerojatnost pod zadanim modelom i obično točno pogodi
funkciju. Provjeravamo ono što ne pogađa pouzdano. Prvo je pretpostavka
neovisnosti, koju redovito uzima prešutno, pa množi vjerojatnosti i tamo gdje
jedinice dijele kućanstvo, razred ili algoritamski doseg. Drugo je nazivnik, jer
ukupnu i uvjetnu vjerojatnost u odgovoru zna zamijeniti. Treće je smjer
zaključka, jer vjerojatnost jednog ishoda pod modelom lako predstavi kao
vjerojatnost samog modela.

> Navedi koje pretpostavke o neovisnosti i jednakoj vjerojatnosti koristiš prije
> nego što bilo što izračunaš, a zatim isti rezultat dobij i simulacijom pa
> usporedi dva broja.

**Nađite grešku.**
Na pitanje koliko je vjerojatno da barem jedna od pet objava iste kampanje
postane viralna asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Vjerojatnost da pojedina objava ne postane
viralna iznosi 0,98, vjerojatnost da nijedna od pet ne postane viralna je
0,98 na petu potenciju, a komplement toga daje 9,6 %. Budući da su objave
zasebne jedinice iste kampanje, zaključuje da je račun potpun.

Greška je posljednja rečenica, u kojoj zasebne jedinice postaju neovisne
jedinice. Potenciranje vrijedi samo uz neovisnost, a objave iste kampanje dijele
publiku i algoritamski doseg, pa jedna viralna objava povećava izglede sljedeće.
Račun i komplement su ispravni, ali vrijede za model koji ovdje ne pristaje.
Popravak je ili opravdati neovisnost podacima, ili simulirati proces u kojem
uspjeh jedne objave mijenja vjerojatnost ostalih.

## Razrađeni primjer

Novi naslov newslettera poslan je na pedeset adresa i otvoren je četrnaest puta.
Dosadašnja stopa otvaranja iznosi dvadeset dva posto, pa pitanje glasi je li
četrnaest otvaranja dovoljno neobično da bi se o novom naslovu smjelo tvrditi
išta. Račun ispod daje istu vjerojatnost na dva načina, prvo iz binomne
raspodjele, a zatim brojanjem u dvadeset tisuća simuliranih kampanja.

Funkcija `pbinom` vraća vjerojatnost da uspjeha bude najviše onoliko koliko je
zadano, pa je komplement te vrijednosti pri trinaest upravo vjerojatnost od
četrnaest naviše. Funkcija `rbinom` izvlači slučajne ishode iz iste raspodjele,
pa udio među njima mora dati približno isti broj.

Oba puta daju istu vrijednost, `r hr_broj(s7$tocno)` % iz raspodjele i
`r hr_broj(s7$simulirano)` % iz simulacije. Podudaranje nije iznenađenje nego
provjera, jer je raspodjela sažetak upravo onoga što simulacija radi jedan po
jedan slučaj.

Odgovor uredništvu zato nije ohrabrujući. Kampanja koja ne bi bila ni po čemu
posebna proizvela bi četrnaest ili više otvaranja u otprilike jednom od pet
slučajeva, pa opaženi rezultat nije neobičan i sam ne nosi nikakvu tvrdnju o
novom naslovu. Odluka koja iz toga slijedi jest poslati više poruka, a ne
donijeti zaključak iz ovih.

Postupak kojim smo došli do te rečenice ima ime i cijelo poglavlje. Pretpostavili
smo da se ništa nije promijenilo, izračunali koliko je opaženi ishod vjerojatan
pod tom pretpostavkom, i tek onda odlučili što nam taj broj dopušta reći.

## Sažetak

Vjerojatnost opisuje što ponovljena slučajnost proizvodi, i ta se tvrdnja u
kratkim nizovima ne vidi. Tri pravila računanja su jednostavna, a jedina
sadržajna odluka u njima jest pretpostavka neovisnosti, koja se u podacima
provjerava i u ovoj populaciji ne vrijedi. Binomna raspodjela pokriva ponovljene
pokušaje s dva ishoda dok ta pretpostavka drži, a normalna raspodjela opisuje
oblik koji se pojavljuje u zbroju mnogih ishoda, s pravilom područja koje na
asimetričnim varijablama otkazuje. Odabir pokušaja koji slijede niz uspjeha
pokazao je da i sam postupak mjerenja može proizvesti pomak veličine koju
tražimo. Poglavlje o uzorkovanju tu logiku prenosi na statistike koje se
mijenjaju od uzorka do uzorka.

## Pojmovi

vjerojatnost (*probability*), zakon velikih brojeva (*law of large numbers*),
uvjetna vjerojatnost (*conditional probability*), neovisnost (*independence*),
binomna raspodjela (*binomial distribution*), normalna raspodjela (*normal
distribution*), QQ prikaz (*Q–Q plot*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto niz od pet glava zaredom ne mijenja
vjerojatnost sljedećeg bacanja, a niz od pet viralnih objava iste kampanje
mijenja procjenu za sljedeću. Imenujte svojstvo po kojem se dva slučaja
razlikuju.

### Računski

U populaciji iz ovog poglavlja portal kao primarni izvor vijesti bira
`r hr_broj(s7$p_portal)` % ljudi. Izračunajte vjerojatnost da nijedna od pet
neovisno izabranih osoba ne bira portal, a zatim vjerojatnost da ga bira barem
jedna. Zatim u widgetu poglavlja postavite stvarnu vjerojatnost na tu vrijednost
i pet pokušaja pa opišite koliko se pojedinačni nizovi razlikuju od izračunatog
prosjeka.

### Kritički

Prosudite kako je nalaz o vrućoj ruci prešao put od mjerenja do općenite tvrdnje
o ljudskoj procjeni slučajnosti, i što se u toj tvrdnji promijenilo nakon
ispravka mjere (Gilovich, 1985; Miller, 2018). Predajte jedan odlomak i imenujte
rečenicu koju bi popularni prikaz smio zadržati.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte korake računa koji su ispravni,
redak koda u kojem stoji pretpostavka koja ne vrijedi, i napišite rečenicu kojom
bi izvještaj morao ograničiti svoj zaključak.
