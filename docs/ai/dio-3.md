# DIO III: OD UZORKA DO POPULACIJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

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

---

# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | CLT stroj | simulirana populacija | pogl. 4, 7 |

**Vinjeta.**
Ismay i Kim zaključivanje predaju tako da čitatelj svaki postupak najprije vidi
kao ponovljeno uzorkovanje, a tek ga zatim susretne kao formulu (Ismay, 2019).
Redoslijed nije stvar ukusa. Formula za standardnu pogrešku zapisuje ishod
postupka koji se može odvrtjeti pred očima, pa je onaj tko je vidio postupak
čita kao sažetak, a onaj tko nije mora je primiti na vjeru.

Problem koji taj postupak rješava svakodnevan je. Istraživački tim treba reći
nešto o svim odraslim stanovnicima jednoga grada, a razgovarao je s njih
osamsto. Izračunata brojka točna je za tih osamsto ljudi i ni za koga drugoga.

Uzorak je pritom samo jedan ishod. Drugi uzorak iste veličine, izvučen istim
postupkom istoga dana, dao bi drugu sredinu i drugi udio.

Kako iz jednoga uzorka doznati koliko bi se rezultat mijenjao da smo uzorkovali
ponovno?

## Populacija, uzorak i pogreška uzorkovanja

Statistika postoji zbog jednog nesrazmjera. Tvrdnja se odnosi na skup jedinica
koji ne možemo izmjeriti u cijelosti, a podatak dolazi iz dijela koji smo
uspjeli obuhvatiti. **Populacija** je skup jedinica o kojima želimo zaključivati,
**uzorak** je dio jedinica koje smo stvarno promatrali, a razlika među njima
nije samo u veličini. Uzorak nastaje postupkom odabira, i taj postupak određuje
koje populacijske jedinice uopće imaju priliku postati podatak.

Mjere se razlikuju zajedno s time. Vrijednost izračunata na cijeloj populaciji
naziva se **parametar** i piše se grčkim slovom, pa je $\mu$ populacijska
sredina, a $\sigma$ populacijska standardna devijacija. Vrijednost izračunata
na uzorku naziva se **statistika** i piše se latinicom, kako je poglavlje o
sažimanju podataka već koristilo $\bar{x}$ za uzoračku sredinu i $s$ za
uzoračku standardnu devijaciju. Slovo $n$ i dalje označava broj opažanja u
uzorku, a $N$ veličinu populacije. Statistika je procjena parametra i gotovo
nikada mu nije jednaka.

U stvarnom istraživanju to razlikovanje ostaje neprovjerljivo, jer parametar
nije poznat. Kad bi bio poznat, uzorak ne bi ni trebao. Ovo poglavlje zato radi
na simuliranoj populaciji od `r hr_broj(s8$N, 0)` odraslih osoba izmišljenoga
grada, koju je proizveo kod uz fiksno sjeme i koja ne opisuje nijedno stvarno
mjesto. Njezina je vrijednost upravo u tome što je izmišljena, jer se samo za
izmišljenu populaciju smije reći koliki joj je prosjek prije nego što se
izvuče ijedan uzorak. Prosječno povjerenje u medije u toj populaciji iznosi
`r hr_broj(s8$mu, 2)` na ljestvici od 1 do 10 uz standardnu devijaciju
`r hr_broj(s8$sigma, 2)`, prosječno se dnevno prati
`r hr_broj(s8$mu_minuta, 1)` minuta medijskog sadržaja, a udio onih kojima je
portal primarni izvor vijesti iznosi
`r paste0(hr_broj(100 * s8$udio_portal, 1), " %")`.

Izvučemo li iz te populacije jedan uzorak od stotinu osoba, prosječno
povjerenje u njemu iznosi `r hr_broj(s8$uzorak_sredina, 2)`, a udio korisnika
portala `r paste0(hr_broj(100 * s8$uzorak_portal, 1), " %")`. Obje su
vrijednosti blizu populacijskih, ali nijedna nije jednaka. Razmak koji je pritom
nastao ima ime, i to ime nije optužba.

**Pogreška uzorkovanja** je razlika između vrijednosti izračunate na uzorku i
vrijednosti koju ima cijela populacija, a nastaje zato što je izmjeren dio
umjesto cjeline.

Riječ pogreška ovdje ne označava propust u radu. Nitko nije pogrešno prepisao
odgovor ni krivo postavio pitanje. Kada bi cijeli postupak bio proveden
besprijekorno, razmak bi i dalje postojao, jer stotinu ljudi nije pedeset
tisuća ljudi. Razlikovanje te neizbježne promjenjivosti od pristranosti koja
nastaje lošim odabirom nosi ostatak poglavlja, i vrijedi ga zadržati na umu od
prve stranice.

## Kad uzorkovanje ponovimo

Jedan uzorak ne govori koliko je njegova procjena stabilna. Da bismo to
doznali, moramo napraviti ono što stvarno istraživanje nikada ne radi, a to je
ponoviti cijeli postupak od početka. Tri neovisna uzorka od po stotinu osoba iz
naše populacije daju prosječno povjerenje `r hr_broj(s8$tri[1], 2)`,
`r hr_broj(s8$tri[2], 2)` i `r hr_broj(s8$tri[3], 2)`. Sva tri broja opisuju
istu populaciju, izračunata su istim postupkom i međusobno se razlikuju za
`r hr_broj(s8$raspon_tri, 2)` boda.

Ponovimo li to ne tri nego tri tisuće puta, dobiveni prosjeci prestaju biti
niz pojedinačnih ishoda i postaju raspodjela s vlastitim oblikom, središtem i
širinom. Ta raspodjela nije opis ljudi. Ona je opis onoga što bi se događalo s
našom procjenom.

**Distribucija uzorkovanja** je raspodjela vrijednosti koje bi neka statistika
poprimila kroz mnogo ponovljenih uzoraka iste veličine iz iste populacije.

Razlika između te raspodjele i raspodjele samih opažanja najvažnije je
razlikovanje u cijelom poglavlju, a lako se izgubi jer obje imaju sredinu i
standardnu devijaciju. Raspodjela opažanja odgovara na pitanje koliko se ljudi
međusobno razlikuju. Distribucija uzorkovanja odgovara na pitanje koliko bi se
razlikovala naša procjena da smo imali sreće drugačije.

*Slika. Raspodjela pojedinačnih ocjena povjerenja u simuliranoj populaciji i raspodjela sredina tri tisuće uzoraka od po sto osoba, na zajedničkoj osi.*

Obje raspodjele leže oko iste vrijednosti, što znači da uzoračka sredina ne
promašuje sustavno ni prema gore ni prema dolje. Procjenitelj koji ima to
svojstvo naziva se **nepristranim**. Zbijenost donjeg panela nije, međutim,
svojstvo ljudi nego svojstvo postupka, i upravo je ona ono što nas zanima kad
pitamo koliko smijemo vjerovati jednoj brojci.

## Standardna pogreška

Širinu distribucije uzorkovanja mjerimo isto kao svaku drugu raspršenost,
standardnom devijacijom. Da bi bilo jasno da je riječ o raspršenosti procjene, a
ne o raspršenosti ljudi, ta mjera nosi vlastito ime.

**Standardna pogreška** je standardna devijacija distribucije uzorkovanja, pa
opisuje koliko bi tipično varirala procjena kroz ponovljene uzorke.

U našoj simulaciji standardna devijacija pojedinačnih ocjena iznosi
`r hr_broj(s8$sigma, 2)`, a standardna devijacija tri tisuće uzoračkih sredina
`r hr_broj(s8$se_empirijska, 3)`. Omjer tih dviju brojki iznosi
`r hr_broj(s8$omjer, 1)`. Uzorci su imali po stotinu osoba, a korijen iz sto je
deset, i to poklapanje nije slučajno.

Razlog se vidi bez računa. Sredina raspoređuje ukupno izmjereno na sve
ispitanike, pa u uzorku od deset ljudi jedan neobičan odgovor nosi desetinu
rezultata, a u uzorku od tisuću ljudi tisućinu. Kako uzorak raste, pojedinačna
odstupanja imaju sve manju priliku pomaknuti zbroj, i to ne zato što bi
odstupanja nestajala, nego zato što se u većem uzorku sve češće međusobno
poništavaju. Dobitak zato ne raste s brojem ljudi nego sa svojim korijenom.

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

U toj jednakosti $SE_{\bar{x}}$ označava standardnu pogrešku uzoračke sredine,
$\sigma$ standardnu devijaciju populacije, a $n$ veličinu uzorka. Za naš slučaj
formula daje `r hr_broj(s8$se_teorijska, 4)`, dok je simulacija dala
`r hr_broj(s8$se_empirijska, 4)`. Dvije brojke dolaze iz dva potpuno različita
smjera, jedna iz algebre i druga iz tri tisuće ponovljenih izvlačenja, a
poklapaju se na tri decimale.

U stvarnom istraživanju $\sigma$ nije poznata, pa se na njezino mjesto stavlja
uzoračka standardna devijacija $s$. Time formula postaje procjena, a ne
identitet. Tu zamjenu poglavlje o sažimanju podataka je pripremilo kada je
varijancu uvelo s djeliteljem umanjenim za jedan i tu odluku ostavilo kao
tvrdnju bez dokaza. Simulacija je sada može provjeriti. Izvučemo li četiri
tisuće uzoraka od po deset osoba i u svakome izračunamo prosjek kvadriranih
odstupanja s djeliteljem deset, prosječan rezultat iznosi
`r hr_broj(s8$var_n, 2)`, dok prava populacijska varijanca iznosi
`r hr_broj(s8$var_prava, 2)`. Isti račun s djeliteljem devet daje
`r hr_broj(s8$var_n1, 2)`. Djelitelj $n$ podcjenjuje sustavno, i to zato što
odstupanja mjeri od uzoračke sredine, koja je sama izračunata iz istih tih
opažanja i zato im leži bliže nego prava populacijska sredina.

Praktična posljedica korijena vidljiva je čim se ispišu veličine uzorka jedna
do druge. Preciznost raste, ali sve sporije, pa svako sljedeće poboljšanje
košta nesrazmjerno više od prethodnoga.

*Slika. Standardna pogreška sredine povjerenja pri osam veličina uzorka, izračunata formulom i izmjerena na tisuću i petsto ponovljenih uzoraka. Izrada autora.*

Prijelaz s deset na sto osoba prepolovljuje standardnu pogrešku dvaput. Prijelaz
sa sto na tisuću, koji stoji desetostruko više, prepolovljuje je nešto više od
jednom i pol puta. Da bi se preciznost udvostručila, uzorak se mora
učetverostručiti, i ta aritmetika objašnjava zašto ankete rijetko rastu preko
nekoliko tisuća ispitanika.

## Oblik koji se pojavljuje

Zbijenost distribucije uzorkovanja objašnjena je. Njezin oblik nije, a upravo
je oblik ono što omogućuje sve što slijedi. Pogledajmo varijablu koja je
koliko god želimo daleko od zvonaste krivulje. Spremnost na plaćanje vijesti u
našoj populaciji ima `r paste0(hr_broj(s8$platiti_nula, 1), " %")` nula i dugi
rep prema velikim iznosima, uz koeficijent asimetrije
`r hr_broj(s8$platiti_asimetrija, 1)`. Nijedan udžbenički postupak ne bi tu
raspodjelu nazvao normalnom.

Izvučemo li iz nje uzorke od po pet osoba i pogledamo raspodjelu njihovih
sredina, asimetrija ostaje visoka i iznosi
`r hr_broj(s8$clt_asimetrija[["5"]], 2)`. Pri uzorcima od petnaest osoba pada na
`r hr_broj(s8$clt_asimetrija[["15"]], 2)`, pri trideset na
`r hr_broj(s8$clt_asimetrija[["30"]], 2)`, a pri sto na
`r hr_broj(s8$clt_asimetrija[["100"]], 2)`. Raspodjela sredina ispravlja se sama
od sebe, iako se izvorna raspodjela nije ni za što promijenila.

*Slika. Izrazito asimetrična populacijska varijabla i raspodjele njezinih uzoračkih sredina pri četiri veličine uzorka. Svaki panel ima vlastitu os.*

Ono što smo upravo vidjeli ima ime i status teorema. **Središnji granični
teorem** (*central limit theorem*) tvrdi da se distribucija uzorkovanja sredine
približava normalnoj raspodjeli kako uzorak raste, bez obzira na oblik
raspodjele iz koje se uzorkuje. Uobičajeno pravilo palca stavlja granicu oko
trideset opažanja, ali naša simulacija pokazuje i zašto je to pravilo grubo.
Kod izrazito asimetrične varijable trideset osoba nije bilo dovoljno da
asimetrija nestane, dok bi kod raspodjele koja je već gotovo simetrična i deset
osoba bilo dovoljno. Granica ovisi o tome koliko je izvorna raspodjela
iskrivljena, a ne o okruglom broju.

Praktična vrijednost teorema je u tome što oslobađa gotovo cijelo zaključivanje
od pretpostavke o obliku podataka. Postupci koji slijede ne traže da su
pojedinačna opažanja normalno raspodijeljena, nego da je normalna raspodjela
procjene, a to je nešto što uzorak proizvodi sam. Ta razlika objašnjava zašto se
isti alati primjenjuju na dohotke, brojanja i ocjene na ljestvici od jedan do
deset, iako nijedna od tih raspodjela nije zvonasta.

## Interakcija — CLT stroj

Simulacija koja je upravo prošla kroz četiri veličine uzorka fiksirala je oblik
populacije. Widget odvaja te dvije stvari, pa se oblik populacije, veličina
uzorka i broj ponavljanja mijenjaju neovisno. Time postaje vidljivo koje je
svojstvo posljedica čega, jer oblik raspodjele sredina ovisi o obojemu, a
njezina širina samo o veličini uzorka.

*Slika. Izvorna populacija i raspodjela sredina mnogih uzoraka na zajedničkoj osi. Okomita crta označuje populacijsku sredinu simulacije.*

**Što isprobati.**

1. Odaberite simetričnu populaciju i uzorak veličine dva pa usporedite širine dvaju histograma.
2. Promijenite populaciju u desno asimetričnu bez povećanja uzorka.
3. Povećajte uzorak na četrdeset i odvojeno opišite promjenu oblika i širine raspodjele sredina.
4. Odaberite dvovršnu populaciju i pronađite veličinu uzorka pri kojoj se dvije populacijske skupine više ne vide u sredinama.

## Zašto ankete od osamsto ljudi rade

Anketni rezultati rijetko su sredine. Češće su udjeli, pa se pitanje preciznosti
postavlja za **uzorački udio**, koji označavamo s $\hat{p}$ i koji procjenjuje
populacijski udio. Logika ostaje ista, jer je udio prosjek niza nula i jedinica,
pa ga središnji granični teorem pokriva jednako kao svaku drugu sredinu. Mijenja
se samo to što raspršenost udjela ne treba mjeriti posebno. Kod varijable koja
poprima samo dvije vrijednosti raspršenost je određena samim udjelom, najveća je
kada je populacija podijeljena napola i pada kako se udio primiče nuli ili
jedinici.

$$
SE_{\hat{p}} = \sqrt{\frac{\hat{p}\,(1 - \hat{p})}{n}}
$$

Polovica širine intervala oko procjene naziva se **margina pogreške** (*margin
of error*), i to je brojka koju medijski izvještaji navode uz anketu. Budući da
je raspršenost najveća pri udjelu od 50 %, uvrštavanjem te vrijednosti dobiva se
najgori slučaj, koji vrijedi bez obzira na to kakav će rezultat ispasti. Za
uobičajenu razinu od 95 % margina se tada svodi na približno jedan podijeljen
korijenom veličine uzorka.

*Slika. Najveća margina pogreške za udio pri razini od 95 % i uzorak potreban za zadanu marginu. Izrada autora.*

Tablica objašnjava zašto se veličine anketnih uzoraka tako uporno grupiraju
između pet stotina i dvije tisuće ispitanika. Ispod te granice margina postaje
prevelika da bi se o razlikama uopće govorilo, a iznad nje trošak raste brže od
koristi. Anketa na osamsto ljudi daje marginu od približno
`r paste0("±", hr_broj(100 * s8$moe(800), 1), " %")`, i ta je preciznost dovoljna
da se razaznaju razlike od desetak postotnih bodova, a nedovoljna za razlike od
dva ili tri.

Odatle slijedi pravilo čitanja koje vrijedi više od svega ostaloga u ovom
poglavlju. Kada izvještaj navodi da prva opcija ima 32 %, a druga 29 %, razlika
od tri postotna boda manja je od margine pogreške tipične ankete, pa podaci ne
podupiru tvrdnju da je prva opcija ispred druge. Uz to, margina se odnosi na
svaku procjenu zasebno, a razlika dvaju udjela ima vlastitu, još veću
nesigurnost.

U formuli za marginu pogreške nedostaje jedna veličina koju bi svatko očekivao
da je ondje, a to je veličina populacije. Preciznost ovisi o tome koliko smo
ljudi pitali i koliko su njihovi odgovori raspršeni, ne o tome koliko ih ima.
Provjeriti se to može izravno. Uzorak od osamsto osoba izvučen iz cijele naše
populacije daje standardnu pogrešku `r hr_broj(s8$se_velika, 4)`, a isti takav
uzorak izvučen iz njezina deset puta manjeg dijela daje
`r hr_broj(s8$se_mala, 4)`. Populacija veća za red veličine donijela je razliku
u preciznosti manju od desetine. Zbog toga anketa na tisuću ljudi jednako dobro
opisuje grad od pedeset tisuća stanovnika i državu od četiri milijuna, što je
vjerojatno najmanje intuitivan rezultat u cijelom poglavlju i redovito zvuči
kao pogreška onima koji ga prvi put čuju.

Preostaje reći što margina pogreške ne pokriva, jer se upravo o tome najčešće
šuti. Ona mjeri isključivo promjenjivost koja dolazi od slučajnog izvlačenja
ispitanika. Ne mjeri ljude koji nikada nisu bili u okviru iz kojega se
uzorkovalo, ne mjeri one koji su bili pozvani ali nisu odgovorili, i ne mjeri
učinak formulacije pitanja ni redoslijeda ponuđenih odgovora. Anketa uz koju
piše da je margina ±3 % nudi tri postotna boda opreza za jedan izvor pogreške i
nijedan za ostale tri. Rečenica da je nešto „unutar margine pogreške" zato je
tvrdnja o slučaju, a ne potvrda da je istraživanje dobro provedeno.

## Kad slučajnost nije bila slučajna

Sve dosad rečeno počiva na jednoj pretpostavci koju je lako previdjeti jer se
rijetko izgovara. Formula za standardnu pogrešku i središnji granični teorem
vrijede za **slučajni uzorak**, u kojem svaka jedinica populacije ima poznatu i
različitu od nule vjerojatnost da bude odabrana. Kada ta pretpostavka padne,
brojke se i dalje uredno izračunaju, ali više ne mjere ono što tvrde.

Prigodni uzorak najčešći je oblik takvog pada. Istraživač anketira one koji su
mu dostupni, obično studente vlastitog kolegija. U našoj populaciji skupina
mlađih od dvadeset pet godina s višim obrazovanjem broji
`r hr_broj(s8$prigodni_n, 0)` osoba i njihovo prosječno povjerenje u medije
iznosi `r hr_broj(s8$prigodni_sredina, 2)`, naspram
`r hr_broj(s8$mu, 2)` u cijeloj populaciji. Razmak je veći od cijele margine
pogreške ankete na tisuću ljudi, a ne bi se smanjio ni da smo anketirali sve te
mlade ljude do posljednjega.

Samoodabir djeluje suptilnije jer proizvodi velike uzorke. Zamislimo mrežnu
anketu na koju odgovaraju oni koji su na internetu, koji su vidjeli poziv i koji
su se odlučili javiti, pri čemu svaki od tih koraka propušta drugačiji dio
populacije. Simulacija takvog postupka na našoj populaciji daje uzorak od
`r hr_broj(s8$online_n, 0)` osoba, dakle mnogostruko veći od bilo koje
telefonske ankete. Njegov prosjek dobi iznosi `r hr_broj(s8$online_dob, 1)`
godina naspram `r hr_broj(s8$dob, 1)` u populaciji, udio korisnika društvenih
mreža `r paste0(hr_broj(100 * s8$online_mreze, 1), " %")` naspram
`r paste0(hr_broj(100 * s8$udio_mreze, 1), " %")`, a prosječno povjerenje
`r hr_broj(s8$online_sredina, 2)` naspram `r hr_broj(s8$mu, 2)`.

Treći oblik pogađa i istraživanja koja su sve napravila ispravno. Uzorak može
biti izvučen savršeno slučajno iz besprijekornog popisa, a onda dio odabranih
ne odgovori. Ako oni koji ne odgovaraju nalikuju onima koji odgovaraju, gubi se
samo veličina uzorka i s njom nešto preciznosti. Ako se razlikuju, a upravo se
najčešće razlikuju po zauzetosti, zanimanju za temu i povjerenju u onoga tko
pita, tada preostali dio uzorka više nije slučajan bez obzira na to kako je
odabran. Postupak odabira i postupak odaziva dva su različita filtra, i drugi
je izvan nadzora istraživača.

Kod tolikog uzorka standardna pogreška je sitna, pa bi izvještaj mogao objaviti
vrlo uzak interval oko sustavno pogrešne vrijednosti. To je najvažnija
asimetrija u poglavlju. Slučajna promjenjivost pada s veličinom uzorka i mjeri
se standardnom pogreškom, dok pristranost odabira ne ovisi o veličini uzorka i
standardna je pogreška uopće ne vidi. Velik pristran uzorak zato je opasniji od
malog slučajnog, jer nosi jednaku netočnost i uz nju uvjerljivost koju mala
brojka nikada ne bi imala.

**Statistika u divljini.**
**Deset milijuna listića i pogrešan pobjednik.** Časopis *Literary Digest*
razaslao je uoči američkih izbora 1936. milijune probnih listića i na temelju
vraćenih odgovora objavio predviđanje koje je promašilo pobjednika, dok su
istodobne ankete na uzorcima manjima za red veličine pogodile ishod
(Squire, 1988).

Uzorak nije zakazao zbog veličine. Popisi iz kojih su adrese izvučene
obuhvaćali su imućnija kućanstva sustavno češće od ostalih, a listić je vratio
tek dio onih koji su ga primili, pa se skupina koja je odgovorila razlikovala od
skupine koja nije (Squire, 1988). Oba filtra djeluju u istom smjeru i nijedan se
ne popravlja slanjem još listića. Slučaj se često prepričava kao upozorenje da
uzorci trebaju biti veliki, iako pokazuje upravo suprotno.

**Pitajte model.**
Asistent može napisati simulaciju distribucije uzorkovanja u nekoliko sekundi,
ali treba mu odvojeno zadati populaciju, postupak odabira, veličinu uzorka i
statistiku koja se računa. Provjeravamo uzorkuje li s vraćanjem samo kada je to
namjera, jer je zadana postavka mnogih funkcija suprotna od potrebne. Najčešća
pogreška u odgovoru nije u kodu nego u rečenici koja ga prati, gdje se
raspršenost pojedinaca predstavi kao standardna pogreška procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno navedi standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

Greška je zamjena dviju razina varijabilnosti. Veći uzorak sužava raspodjelu
procjene, ali očekivana raspršenost pojedinaca ostaje jednaka populacijskoj, jer
je svojstvo ljudi, a ne postupka.

## Razrađeni primjer

Cijeli aparat zaključivanja koji slijedi u ostatku knjige svodi se na jednu
petlju. Izvuci uzorak, izračunaj mjeru, ponovi mnogo puta i pogledaj što je
nastalo. Sve ostalo su prečice do rezultata te petlje. Vrijedi je zato jednom
vidjeti ispisanu u cijelosti, na najgoroj varijabli koju naša populacija ima.

Pitanje glasi koliko su prosjeci pouzdani kada se računaju na varijabli s
mnoštvom nula i dugim repom, dakle u okolnostima u kojima bi se svaka
pretpostavka o zvonastom obliku odmah raspala. Postavljamo ga tako da usporedimo
dvije veličine uzorka i za obje pogledamo gdje se sredine skupljaju i koliko su
raspršene.

Funkcija `replicate` ponavlja zadani izraz traženi broj puta i skuplja rezultate
u vektor, pa je ona jedini novi glagol u ovom bloku. Prosjek četiri tisuće
sredina iz uzoraka od pet osoba iznosi `r hr_broj(s8_p$m5, 2)` kuna, a iz
uzoraka od šezdeset osoba `r hr_broj(s8_p$m60, 2)` kuna, dok prava populacijska
vrijednost iznosi `r hr_broj(s8_p$mu, 2)` kuna. Nijedna od dviju veličina uzorka
ne promašuje cilj sustavno, što je nepristranost o kojoj je već bilo riječi.

Razlikuju se u nečemu drugome. Standardna pogreška pri pet osoba iznosi
`r hr_broj(s8_p$se5, 2)`, a pri šezdeset `r hr_broj(s8_p$se60, 2)`, dakle
`r hr_broj(s8_p$omjer, 1)` puta manje. Odnos je približno jednak korijenu iz
dvanaest, koliko puta je veći uzorak, i time se algebra iz odjeljka o
standardnoj pogrešci potvrđuje na varijabli za koju bi se očekivalo da je
najviše izmiče. Vrijedi zapaziti i što petlja nije popravila. Uzorak od pet
osoba i dalje daje raspodjelu sredina koja je vidljivo iskrivljena, pa
nepristranost i normalnost nisu isto svojstvo i ne stižu u istom trenutku.

Vrijedi zapaziti i što je u ovom bloku bilo moguće samo zato što je populacija
izmišljena. Prvi redak poziva `populacija_medija` i time čini nešto što nijedno
stvarno istraživanje ne može, jer izvlači uzorke iz cjeline kojoj bi inače bilo
nemoguće pristupiti. Istraživač koji radi s podacima ima jedan uzorak i nijednu
mogućnost da petlju stvarno pokrene. Sve što slijedi u knjizi način je da se do
rezultata te petlje dođe bez nje, a poglavlje o procjeni prvo je od tih
zaobilaženja. Ono uzorku dopušta da nakratko preuzme ulogu populacije, i time
istu petlju vrati u ruke nekome tko ima samo osamsto ispitanika.

## Sažetak

Uzorak je jedan ishod postupka odabira, a distribucija uzorkovanja opisuje kako
bi se procjena mijenjala kroz ponovljene izvlačenja. Njezinu širinu mjeri
standardna pogreška, koja pripada procjeni, a ne pojedincima, i pada s korijenom
veličine uzorka, pa preciznost postaje sve skuplja. Njezin oblik se s porastom
uzorka približava normalnoj raspodjeli bez obzira na to iz čega se uzorkuje, i
upravo to čini ostatak knjige mogućim. Ništa od toga ne popravlja pristran
odabir, jer standardna pogreška mjeri samo ono što bi se mijenjalo kroz
ponavljanja istoga postupka, a ne ono što je taj postupak sustavno izostavio.
Poglavlje o procjeni uzet će tu raspodjelu i iz nje izgraditi raspon oko
vrijednosti koju ne možemo izravno vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), parametar (*parameter*),
statistika (*statistic*), pogreška uzorkovanja (*sampling error*), distribucija
uzorkovanja (*sampling distribution*), nepristranost (*unbiasedness*),
standardna pogreška (*standard error*), središnji granični teorem (*central
limit theorem*), uzorački udio (*sample proportion*), margina pogreške (*margin
of error*), slučajni uzorak (*random sample*), prigodni uzorak (*convenience
sample*), samoodabir (*self-selection*)

## Zadaci

### Konceptualni

Razlikujte raspodjelu pojedinačnih opažanja od distribucije uzoračkih sredina.
Za svaku navedite što joj je jedinica, što mjeri njezina širina i što se s njom
događa kada uzorak naraste. Predajte skicu obiju raspodjela i dva popratna
objašnjenja.

### Računski

Upotrijebite tablicu margine pogreške iz ovog poglavlja. Anketa na tisuću
ispitanika izvještava da prva opcija ima 44 %, a druga 39 %. Izračunajte marginu
pogreške te ankete, presudite je li razlika od pet postotnih bodova veća od
margine i objasnite zašto usporedba dviju procjena traži više opreza od
prosudbe svake zasebno. Zatim odredite koliki bi uzorak trebao da margina padne
na polovicu i provjerite rezultat u istoj tablici. Postupak s cijelim skupom
podataka opisan je u Dodatku A.

### Kritički

Pročitajte slučaj časopisa *Literary Digest* iz okvira o statistici u divljini
(Squire, 1988). Objasnite zašto povećanje broja poslanih listića ne bi ispravilo
nijedan od dvaju opisanih problema i navedite koji bi podatak o toj anketi bio
najkorisniji za prosudbu njezine vjerodostojnosti. Predajte jedan odlomak.

### Revizija modela

Ocijenite analizu modela iz okvira o pogrešci. Izdvojite tvrdnju koja je točna,
imenujte zamjenu dviju razina varijabilnosti i napišite ispravljenu verziju
druge rečenice koja zadržava sve što je u njoj bilo točno.

---

# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

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

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

Slovo $z^{*}$ označava koliko standardnih pogrešaka širimo na svaku stranu, i
bira ga željena razina, pa je za 95 % ono jednako 1,96. Za naš uzorak taj račun
daje raspon od `r hr_broj(s9$donja, 2)` do `r hr_broj(s9$gornja, 2)`, a prava
populacijska vrijednost iznosi `r hr_broj(s9$mu, 2)` i nalazi se unutra.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Vrijedi obratiti pozornost na to gdje u toj definiciji stoji obećanje. Ono ne
stoji uz raspon nego uz postupak, i upravo se ta razlika u praksi najčešće gubi.

## Što razina pouzdanosti obećava

Provjera je moguća jer populaciju poznajemo. Ponovimo cijeli postupak deset
tisuća puta, svaki put izvučemo novi uzorak od dvjesto osoba, izračunamo
njegovu sredinu i standardnu pogrešku, sastavimo interval i prebrojimo koliko
ih je obuhvatilo pravu vrijednost. Cilj je obuhvaćen u
`r paste0(hr_broj(s9$pokrivenost, 1), " %")` slučajeva, a promašen u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja.

Postupak dakle radi približno onako kako obećava, i vrijedi zadržati riječ
približno. Zamjena nepoznate populacijske raspršenosti onom izmjerenom u uzorku
unosi vlastitu nesigurnost, koja je pri dvjesto osoba mala, a pri dvadeset osoba
ne bi bila. Ispravak koji to nadoknađuje širi interval za mali uzorak i knjiga
ga uvodi u poglavlju o usporedbi dviju grupa, gdje ga postupak prvi put stvarno
treba.

Ono što se u brojci od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne vidi jest
sudbina pojedinačnog intervala. Svaki od tih dvije tisuće raspona ili sadrži
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
Smije reći da su vrijednosti unutar granica uskladive s podacima, a one izvan
njih slabo uskladive, i to pod pretpostavkama koje je postupak koristio. Smije
reći da je istraživanje bilo dovoljno precizno da razluči razlike veće od
širine raspona, i da za manje razlike nije. Ne smije reći koliko je vjerojatno
da parametar leži unutra, niti da će se ponovljeno istraživanje smjestiti
unutar tih istih granica, jer bi drugo istraživanje imalo vlastiti uzorak i
vlastiti interval. Prve dvije rečenice pokrivaju gotovo sve što se u praksi
treba zaključiti, i obje govore o rasponu vrijednosti, a nijedna o
vjerojatnosti.

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
svojstvo koje se bira i plaća širinom. Konvencija od 95 % nema dublje
opravdanje od uobičajenosti, i to je razlog više da se uz svaki interval navede
razina na kojoj je izračunat.

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

Pravilo koje se pritom obično primjenjuje nije simetrično i vrijedi to znati.
Kada se dva intervala uopće ne preklapaju, razlika među skupinama gotovo je
sigurno stvarna. Kada se preklapaju, iz toga ne slijedi da razlike nema, jer
umjereno preklapanje i dalje je uskladivo s pravom razlikom. Preklapanje je
zato slab dokaz u jednom smjeru i jak u drugom, a pošten odgovor traži interval
za samu razliku, a ne dva intervala jedan pokraj drugoga. Taj postupak knjiga
uvodi u poglavlju o usporedbi dviju grupa.

Postoji i druga zamjena koja se često javlja u istom odlomku. Interval
pouzdanosti govori gdje je prosjek, a ne gdje su ljudi. Za naš uzorak od
dvjesto osoba raspon oko sredine dug je
`r hr_broj(s9$gornja - s9$donja, 2)` boda, dok bi raspon unutar kojega leži
otprilike 95 % pojedinačnih ocjena bio širok približno
`r hr_broj(2 * s9$predikcijski, 1)` boda. Prvi se odnosi na parametar i sužava
se s uzorkom, drugi na buduće opažanje i ne sužava se gotovo nimalo.

*Slika. Interval pouzdanosti za sredinu i raspon unutar kojega leži otprilike 95 % pojedinačnih ocjena, na istom uzorku i istoj osi.*

## Bootstrap kao vlastiti izum

Sve dosad počiva na jednoj formuli za standardnu pogrešku, a ta formula postoji
samo za neke mjere. Za sredinu je poznata, za udio također, a za medijan,
razliku percentila ili omjer dviju mjera nije jednostavna ili je uopće nema.
Pitanje što učiniti kada formule nema ima odgovor koji se može smisliti bez
ijedne nove ideje, uz uvjet da se prethodno poglavlje shvatilo ozbiljno.

Standardna pogreška bila je definirana kroz ponovljene uzorke iz populacije.
Kad bismo populaciji imali pristup, izvukli bismo tisuću uzoraka, izračunali
tisuću medijana i pogledali koliko se razilaze. Populaciji pristupa nemamo,
imamo samo uzorak. Uzorak je pritom najbolja slika populacije kojom
raspolažemo, jer je iz nje izvučen slučajno i njezine razmjere nosi u sebi. Ako
mu dopustimo da privremeno glumi populaciju i iz njega izvlačimo nove uzorke
jednake veličine, dobit ćemo raspodjelu koja oponaša onu koju bismo dobili iz
prave populacije.

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
raspon od `r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta,
unutar kojega leži prava populacijska vrijednost od
`r hr_broj(s9$medijan_pop, 1)` minuta.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću.*

Histogram ima vidljiv stubast oblik jer medijan uzorka od šezdeset brojeva može
poprimiti samo ograničen skup vrijednosti, što je svojstvo mjere, a ne mana
postupka. Snaga bootstrapa upravo je u tome što ga takve neugodnosti ne
zaustavljaju. Isti se postupak bez izmjene primjenjuje na sredinu, medijan,
korelaciju ili razliku dviju skupina, jer nigdje ne pretpostavlja oblik
raspodjele.

Njegova granica ostaje početni uzorak, i granica je stroga. Bootstrap ponovno
koristi opažanja koja već imamo, pa ne može otkriti dio populacije koji u
uzorak nikada nije mogao ući. Ako je uzorak prigodan, postupak će pouzdano
opisati promjenjivost pogrešne procjene. Ako je premalen da zabilježi rijetke
ali važne slučajeve, ta praznina ostaje u svakom od četiri tisuće ponavljanja.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživači su studentima i aktivnim
znanstvenicima predočili objavljeni interval pouzdanosti i uz njega šest
tvrdnji o njegovu značenju, među kojima nijedna nije bila točna (Hoekstra, 2014).
Velik dio ispitanika u svim skupinama, uključujući iskusne istraživače,
prihvatio je barem neke od njih.

Tvrdnje nisu bile besmislene, i u tome je poanta okvira. Sve su govorile o
vjerojatnosti da se prava vrijednost nalazi unutar granica, ili o tome koliko
je vjerojatno da bi se ponovljeno istraživanje unutar njih smjestilo. Postupak
koji smo izgradili takva obećanja ne daje, jer se njegov postotak odnosi na
udio intervala koje bi ponovljeno uzorkovanje proizvelo. Nalaz ne pokazuje da
su intervali loš alat nego da je rečenica kojom ih opisujemo teža od računa
koji ih proizvodi.

**Pitajte model.**
Asistent može bootstrapirati gotovo svaku statistiku i obično to učini
ispravno. Provjeravamo tri stvari koje redovito promakne. Uzorkuje li s
vraćanjem i na punoj veličini uzorka, jer bez toga raspodjela nema smisla. Čuva
li strukturu podataka, jer se kod uparenih ili grupiranih opažanja izvlače
jedinice, a ne redovi. Ponavlja li dovoljno puta, jer nekoliko stotina
ponavljanja daje granice koje se mijenjaju od pokretanja do pokretanja.
Najčešća pogreška ipak nije u kodu nego u zaključnoj rečenici, gdje se već
izračunatom intervalu pripiše vjerojatnost.

> Izračunaj točkastu procjenu i bootstrap interval. Uzorkuj s vraćanjem na
> punoj veličini uzorka, sačuvaj strukturu podataka i interpretiraj razinu
> pouzdanosti kao svojstvo ponovljenog postupka.

**Nađite grešku.**
Bootstrap raspodjela je približno simetrična i interval je uredno izračunat iz
njezinih krajeva. Postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

Greška je pripisivanje vjerojatnosti fiksnom parametru nakon izračuna
frekventističkog intervala. Prva rečenica je točna i postupak je proveden
ispravno. Razina pouzdanosti opisuje udio intervala koji obuhvaćaju parametar
kroz ponovljeno uzorkovanje, a ne položaj parametra u odnosu na ovaj raspon.

## Razrađeni primjer

Pitanje je ono koje bi postavio naručitelj istraživanja. Koliko vremena dnevno
stanovnici našega grada provode uz medije, i koliko je taj odgovor pouzdan ako
je anketirano šezdeset ljudi.

Prvi izbor nije statistički nego opisni. Dnevne minute imaju rep prema velikim
vrijednostima, a poglavlje o sažimanju podataka pokazalo je da prosjek takav
rep povlači za sobom, dok medijan ostaje kod tipičnog ispitanika. Za pitanje o
tome koliko medija prati uobičajena osoba medijan je pošteniji odgovor. Cijena
tog izbora vidi se tek sada, jer za sredinu postoji formula za standardnu
pogrešku, a za medijan ne postoji nijedna koja bi se dala napisati u jednom
retku. Upravo zato ovaj primjer i postoji.

Cijeli bootstrap stane u istu petlju koju je poglavlje o uzorkovanju već
pokazalo, uz jednu izmjenu. Umjesto iz populacije, izvlačimo iz uzorka, i to s
vraćanjem.

Poziv `sample` uz argument `replace` izvlači s vraćanjem i jedini je novi
element u odnosu na prethodno poglavlje, dok `quantile` odsijeca zadani udio
raspodjele s obje strane. Blok proizvodi upravo one tri brojke koje je odjeljak
o bootstrapu već naveo, jer je riječ o istoj analizi ispisanoj u cijelosti.

Odgovor naručitelju glasi da tipičan stanovnik prati medije oko
`r hr_broj(s9$medijan_uzorak, 1)` minuta dnevno, uz raspon od
`r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta koji
opisuje koliko bi se ta procjena mijenjala kroz ponovljena istraživanja iste
veličine. Raspon je širok gotovo `r hr_broj(s9$boot_gornja - s9$boot_donja, 0)`
minuta, što je pošten opis onoga što šezdeset ljudi može reći, i ujedno
najkorisnija brojka u cijelom izvještaju. Naručitelj koji je htio razlučiti
promjenu od deset minuta iz ovih podataka odgovor neće dobiti bez većeg uzorka.

Budući da populaciju poznajemo, možemo napraviti i ono što stvarno istraživanje
ne može. Prava vrijednost iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i nalazi
se unutar granica. Iz toga ne slijedi da postupak radi, jer bi i loš postupak
pogodio pokoji put. Ono što o postupku govori jest prebrojavanje deset tisuća
ponavljanja iz ranijeg odjeljka, a ovaj pojedinačni pogodak samo je jedan od
njih, viđen iznutra kako ga vidi istraživač.

Redoslijed kojim su tri brojke ispisane isti je onaj kojim se rezultat i
izvještava. Najprije dolazi procjena, jer je ona odgovor na postavljeno pitanje.
Zatim dolazi raspon, jer bez njega procjena tvrdi više nego što zna. Tek na
kraju dolazi ograda, koja ovdje kaže da su podaci simulirani, da je mjera
medijan, a ne prosjek, i da šezdeset ljudi nije mnogo. Ista tri koraka vrijede
za nalaz čija je populacija stvarna, s tom razlikom da se ondje srednji korak
mora izvesti bez ikakve mogućnosti provjere, i upravo zato mora biti izveden
pažljivo.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval pouzdanosti
uzima standardnu pogrešku i oblik koji je dao središnji granični teorem te oko
procjene gradi raspon čije obećanje pripada postupku, a ne pojedinačnom rasponu
koji imamo pred sobom. Preciznost se kupuje podacima, a pouzdanost se bira i
plaća širinom, pa uz svaki raspon mora stajati razina na kojoj je izračunat.
Bootstrap istu ideju oslobađa formule tako što uzorku dopušta da privremeno
glumi populaciju, i time otvara mjere za koje račun ne postoji, ne popravljajući
pritom nijednu slabost samoga uzorka. Sljedeće poglavlje uzima isti aparat i
mijenja mu pitanje, jer umjesto raspona usklađenog s podacima traži koliko su
podaci neobični pod jednom određenom pretpostavkom.

## Pojmovi

točkasta procjena (*point estimate*), interval pouzdanosti (*confidence
interval*), razina pouzdanosti (*confidence level*), preciznost (*precision*),
bootstrap (*bootstrap*), uzorkovanje s vraćanjem (*sampling with replacement*),
parametar (*parameter*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, i zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica. Predajte jedan odlomak.

### Računski

Upotrijebite widget Hvatač intervala. Postavite pedeset intervala pri uzorku od
četrdeset osoba i razini od 95 % pa zabilježite koliko ih promašuje cilj.
Ponovite mjerenje pri razini od 99 % i pri uzorku od sto šezdeset osoba,
mijenjajući svaki put samo jednu postavku. Predajte tablicu s tri retka u kojoj
su navedeni postavka, širina tipičnog intervala i broj promašaja te jednu
rečenicu o tome koja postavka mijenja preciznost, a koja učestalost promašaja.

### Kritički

Pronađite u medijskom izvještaju ili sažetku rada rečenicu koja tumači interval
pouzdanosti. Prosudite pripisuje li vjerojatnost parametru, brka li raspon
sredine s rasponom pojedinačnih opažanja ili je ispravna, i napišite verziju
koja je vjerna postupku bez gubitka informacije (Hoekstra, 2014). Predajte
izvornu rečenicu, prosudbu i ispravak.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira o pogrešci. Imenujte što je u njoj
točno, izdvojite jednu pogrešnu rečenicu i napišite frekventistički ispravnu
zamjenu koja zadržava razinu od 95 % i ne uvodi nove tvrdnje o podacima.
