# Vizualizacija kao argument

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Isti podaci, četiri grafa | Anscombeov kvartet, simulirana anketa | pogl. 4 |

**Vinjeta.**
Anscombe je sastavio četiri skupa podataka s gotovo jednakim uobičajenim
brojčanim sažecima, uključujući isti linearni odnos, ali s posve različitim
grafičkim oblicima (Anscombe, 1973). Jedan je pokazivao približno linearan
obrazac, drugi zakrivljenost, treći utjecajnu točku, a četvrti gotovo okomiti
oblak s jednim izdvojenim opažanjem.

Tablica sažetaka nije sadržavala računsku pogrešku. Upravo je zato primjer bio
uvjerljiv. Četiri različite priče stale su u iste brojke jer sažeci nisu mogli
sačuvati položaj svakog opažanja.

Kada graf razjašnjava podatke, a kada ih pretvara u argument koji prikriva
vlastite odluke?

## Gramatika grafike

Graf nije slika dodana nakon analize. On bira što će se uspoređivati položajem,
duljinom, površinom ili bojom, pa je izbor prikaza ujedno izbor načina na koji
će čitatelj vidjeti razliku. Dobra vizualizacija zato počinje tvrdnjom.
Raspodjela jedne brojčane varijable traži prikaz koji čuva oblik, usporedba
kategorija zajedničku početnu točku, a odnos dviju brojčanih varijabli sačuvana
pojedinačna opažanja. Graf koji ne odgovara pitanju može biti uredan i potpuno
neinformativan.

Uobičajeni popis vrsta grafova, u kojem stupčani dijagram stoji uz kružni i
raspršeni, pritom skriva jednu važnu činjenicu. Vrsta grafa nije osnovna jedinica.
Svaki je prikaz skup odvojenih odluka koje se u praksi tako često pojavljuju
zajedno da je njihova kombinacija dobila ime.

**Gramatika grafike** je opis prikaza kao skupa zasebnih odluka o tome što
jedna oznaka predstavlja, koja je varijabla pridružena kojem vizualnom kanalu,
što je izračunato prije crtanja i kako se vrijednost pretvara u vizualnu
veličinu.

Razlaganje na odluke svaku od njih izlaže zasebnoj provjeri. Ideju je kao
sustav postavio Wilkinson (Wilkinson, 2005), a paket ggplot2 postao je njezina
najraširenija izvedba (Wickham, 2016). Sama gramatika ne pripada nijednom
programu i primjenjuje se pred tiskanom grafikom, bez pisanja koda.

Najprije treba znati što predstavlja jedna oznaka na grafu. Točka može stajati
za ispitanika, državu, godinu ili stranku, a prikazi tu jedinicu mijenjaju bez
najave. Kada agregat zamijeni pojedinca, mijenja se i pitanje na koje graf
odgovara, što je ista opasnost koju opisuje poglavlje o mjerenju i dizajnu.

Sljedeći korak pridružuje varijable vizualnim kanalima, položaju na dvjema
osima, boji, veličini i obliku.

**Pridruživanje** (*aesthetic mapping*) je odluka koja varijabla ulazi u koji
vizualni kanal, čime se određuje koja usporedba čitatelju postaje neposredno
dostupna.

Pridruživanje je tvrdnja o tome što zaslužuje usporedbu. Kada skupinu nosi
boja, graf poziva na neposrednu usporedbu skupina. Kada je skupina razdvojena u
zasebna polja, graf traži da se obrazac čita unutar svake od njih. Podaci
ostaju isti, argument se mijenja, a obmane nije bilo.

Najtiša odluka dolazi prije crtanja. Graf redovito nešto izračuna prije nego što
postavi prvu oznaku. Stupac visine prosjeka odbacio je raspodjelu, okvir s
brkovima izgubio je informaciju o broju vrhova, a izglađena linija dodala je
model koji nitko nije zatražio. Poglavlje o sažimanju pokazalo je koji sažetak
što gubi, a gramatika tome dodaje da je i sam graf redovito sažetak, samo
neoznačen. Anscombeov kvartet poseban je slučaj upravo tog pravila
(Anscombe, 1973).

Ljestvica je pravilo kojim vrijednost postaje vizualna veličina. Raspon osi,
njezin prekid, logaritamska transformacija i položaj sredine u ljestvici boja
mijenjaju koliko promjena zauzima prostora, a podatke pritom ne mijenjaju.
Koordinatni sustav zatvara popis i najčešće služi kao opomena, jer polarne
koordinate duljinu pretvaraju u kut i time istu usporedbu čine težom.

Iz tih odluka slijedi postupak za čitanje tuđega grafa. Što predstavlja jedna
oznaka, što je pridruženo kojem kanalu, što je izračunato prije crtanja i što
dopušta ljestvica jesu pitanja koja se pred novinskom grafikom postavljaju bez
ikakva programa. Knjiga taj postupak dalje koristi pri svakom rastavljanju
objavljene tvrdnje.

## Što oko može očitati

Gramatika kaže da oznaka nosi usporedbu, ali ne kaže koliko dobro. To pitanje
nije stvar ukusa i ima izmjeren odgovor. Cleveland i McGill zadavali su
sudionicima parove vrijednosti prikazane različitim kanalima i mjerili koliko
im omjer promaši (Cleveland, 1984). Iz tih pokusa slijedi poredak elementarnih
zadataka po pogrešci koju proizvode, u kojem je očitavanje položaja na
zajedničkoj osi najtočnije, zatim slijede položaj na odvojenim osima s
usklađenom ljestvicom, duljina, nagib, površina, te na kraju obujam, zakrivljenost
i zasićenost boje (Cleveland, 1984).

Poredak nije popis zabrana nego pravilo raspodjele. Kanal na vrhu poretka
dodjeljuje se veličini koja nosi zaključak, a kanali s dna sekundarnim
razlikama, gdje je gruba procjena dovoljna. Kružni dijagram udio kodira kutom, a
kut leži nisko u poretku, pa isti podaci u stupcima na zajedničkoj osi
proizvode točnije očitanje (Cleveland, 1984). Kada nekoliko udjela treba samo
prepoznati, a ne rangirati, ta razlika prestaje biti važna.

Iz istog poretka slijedi i zašto trodimenzionalni prikaz ravnih podataka
pogoršava očitanje. Perspektiva duljinu pretvara u obujam, a obujam se u
pokusima nalazi među najlošije očitanim kanalima (Cleveland, 1984). Ukras se
dodaje kanalu koji nosi zaključak, i to je ista obitelj postupaka kojoj
pripada skraćena os iz poglavlja o zavaravanju brojkama.

Tufte je isti problem postavio kao pitanje raspodjele tinte na stranici, gdje se
svaki element grafa mjeri time nosi li podatak ili ne nosi (Tufte, 2001). Sjena
ispod stupca, rešetka u pozadini, obrub oko svake oznake i preljev boje troše
prostor i pažnju, a ne dodaju nijednu vrijednost, pa ih Tufte skupno naziva
grafičkim otpadom. Njegovo je pravilo da se takav element ukloni i da se
provjeri je li se išta izgubilo, jer ako nije, nije ni trebao biti ondje.

Postoji i oštriji oblik istog mjerenja. Tufte uspoređuje veličinu učinka koji
graf pokazuje s veličinom učinka koji u podacima postoji, a omjer tih dviju
veličina naziva faktorom laži (Tufte, 2001). Pošten graf ima taj omjer blizu
jedinice. Kada ga skraćena os, površina umjesto duljine ili perspektiva podignu,
graf tvrdi više nego što podaci nose, i to bez ijedne netočne brojke. Vrijednost
te mjere nije u tome što se često računa nego u tome što obmanu premješta iz
područja ukusa u područje provjere.

## Prikaz prema tvrdnji

Pitanje kojim graf počinje nije koji je prikaz lijep nego koju tvrdnju treba
provjeriti. Broj i vrsta varijabli tu odluku gotovo određuju, pa je vrijedi
imati pri ruci.

| Što se prikazuje | Uobičajeni izbor | Što prikaz čuva, a što odbacuje |
|---|---|---|
| jedna brojčana varijabla | histogram, krivulja gustoće | čuva oblik cijele raspodjele, gubi pojedinačno opažanje |
| jedna kategorijalna varijabla | stupci na zajedničkoj osi | čuva učestalost, ne kaže ništa o raspršenosti unutar kategorije |
| brojčana po skupinama | okvir s brkovima, violina | čuva položaj i raspon, odbacuje broj vrhova i pojedinačna opažanja |
| dvije brojčane varijable | raspršeni dijagram | čuva svako opažanje, teško podnosi velik broj točaka |
| dvije kategorijalne varijable | grupirani ili složeni stupci | čuva odnos udjela, otežava usporedbu unutar složenih stupaca |

: Prikaz prema vrsti podataka i prema onome što svaki izbor žrtvuje. Izrada autora.

Desni stupac tablice nosi cijeli argument. Svaki prikaz nešto sačuva i nešto
odbaci, pa se izbor donosi prema tome što tvrdnja treba, a ne prema tome što
izgleda uredno. Okvir s brkovima izračunava medijan i kvartile prije crtanja,
pa raspodjela s dva vrha i raspodjela s jednim mogu proizvesti isti okvir.
Histogram ne računa ništa osim razreda, pa taj oblik čuva, ali skupine
uspoređuje teže.

Posljednji redak tablice krije odluku koja se rijetko izriče. Kada se dvije
kategorijalne varijable prikazuju stupcima, stupci se mogu poredati jedan uz
drugi ili složiti jedan na drugi, a treća mogućnost svaki stupac rastegne na
punu visinu i time prikaže udjele. Prvi izbor čuva apsolutne brojeve i
omogućuje usporedbu veličine skupina. Treći ih odbacuje i pokazuje samo sastav,
zbog čega skupina od dvadeset ispitanika izgleda jednako pouzdano kao skupina od
dvjesto. Nijedan izbor nije pogrešan, ali izvještaj koji tvrdi da je neka
skupina brojnija, a prikazuje udjele, tvrdi nešto što njegov graf ne pokazuje.

Složeni stupac uz to skriva zamku koju je lako previdjeti. Samo najdonji segment
u nizu počinje od zajedničke crte, dok svi ostali počinju ondje gdje je
prethodni završio. Duljina im ostaje točna, ali položaj im je pomaknut za
vrijednost koja se mijenja od stupca do stupca, pa se usporedba srednjih
segmenata svodi na očitavanje duljine bez zajedničke početne točke, što je
prema poretku iz prethodnog odjeljka osjetno teži zadatak (Cleveland, 1984). Kada
usporedba jednog segmenta nosi zaključak, on dobiva vlastiti prikaz.

Ono što je odbačeno vidi se tek kada se vrati na graf. Simulirana anketa
`anketa_mreze` sadrži `r s5_n` ispitanika s dnevnim vremenom korištenja
društvenih mreža, i nije mjerenje nego nastavni skup proizveden kodom. Kada se
uz okvire nacrtaju i opažanja iz kojih su izračunati, razlika između sažetka i
podatka prestaje biti apstraktna.

*Slika. Okvir s brkovima i opažanja iz kojih je nastao. Kutija stoji na kvartilima, a točke pokazuju raspored koji kvartili ne mogu prenijeti.*

Kutija sažima svaku skupinu u pet brojeva. U najmlađoj skupini polovina
ispitanika leži između `r hr_broj(s5_najmladi$q1, 0)` i
`r hr_broj(s5_najmladi$q3, 0)` minuta, a u najstarijoj između
`r hr_broj(s5_najstariji$q1, 0)` i `r hr_broj(s5_najstariji$q3, 0)`. Točke iza
kutije pokazuju što je taj sažetak potrošio, jer se iz njih vidi koliko je
opažanja stisnuto uz donji rub i koliko rijetko rep doseže svoje najveće
vrijednosti. Kutija bi bila ista i da su opažanja unutar nje raspoređena posve
drukčije, što je isti nalaz koji poglavlje o sažimanju podataka izvodi
brojčano.

## Dvije varijable u istom prostoru

Kada obje varijable nose brojeve, raspršeni dijagram jedini je prikaz koji ne
mora ništa izračunati. Svaka točka je jedno opažanje na svojem mjestu, pa se iz
oblaka čita smjer veze, njezina zakrivljenost, postojanje podskupina i položaj
opažanja koja odudaraju. Zbog toga je to prikaz s najvećom informacijskom
gustoćom u knjizi i prikaz kojim počinje svaka provjera odnosa.

Njegova slabost je vlastiti uspjeh. Kada opažanja ima mnogo, točke se
preklapaju, a gustoća prestaje biti vidljiva, jer sto opažanja na istom mjestu
izgleda kao jedno. Uobičajeni popravak je djelomična prozirnost oznake, čime
preklopljena područja postaju tamnija, pa gustoća opet nosi značenje. Drugi je
popravak lagano razmicanje oznaka, koje se koristi kada je jedna varijabla
zapravo diskretna, a treći prelazak na prikaz koji gustoću računa izravno.

*Slika. Dob i dnevno vrijeme korištenja u simuliranoj anketi. Lijevo su neprozirne oznake, desno prozirne, a razlika je u tome što se vidi gdje je opažanja mnogo.*

Oba polja sadrže istih `r s5_n` opažanja i oba pokazuju da vrijeme korištenja
opada s dobi. Desno polje uz to pokazuje gdje ih je mnogo, a gdje malo, i time
odgovara na pitanje koliko je obrazac tipičan, a ne samo postoji li. Prozirnost
ovdje nije ukras nego pridruživanje gustoće tami oznake, dakle odluka gramatike
kao i svaka druga.

Na raspršeni se dijagram redovito dodaje izglađena linija koja kroz oblak
provlači procijenjeni prosječni odnos. Ta linija nije podatak nego model, i to
je najvažnija stvar koju o njoj treba znati. Ona pretpostavlja oblik veze,
zaglađuje ono što joj ne odgovara i ostaje uvjerljiva i onda kada oblak ispod nje
nema nikakav stabilan obrazac. Poglavlje o regresiji pokazuje kako se takva
linija dobiva i pod kojim je uvjetima opravdana, a do tada vrijedi pravilo da
se linija čita zajedno s oblakom iz kojega je izvučena, nikada umjesto njega.

## Poštena ljestvica

Ljestvica je mjesto na kojem se najlakše pogriješi i najlakše prevari, jer je
mijenja jedan broj, a mijenja se cijeli dojam. Prosjeci dnevnih minuta po
dobnim skupinama razlikuju se za `r hr_broj(s5_raspon_prosjeka, 0)` minuta, što
je `r paste0(hr_broj(100 * s5_udio_raspona, 0), " %")` najvećeg među njima.
Koliko će ta razlika zauzeti prostora ne ovisi o podacima nego o rasponu osi.

*Slika. Isti prosjeci na dvjema osima. Lijevi prikaz počinje od nule, desni od najmanje vrijednosti, a razlika među skupinama nije se promijenila.*

Desni prikaz nije izmislio nijedan broj. Sve četiri vrijednosti stoje ondje gdje
i lijevo, a promijenio se samo raspon koji im je dodijeljen. Kod stupaca je to
ozbiljna pogreška, jer duljina stupca nosi značenje, pa odsječena os duljinu
pretvara u veličinu koja više ne odgovara vrijednosti. Kod linijskog grafa i
raspršenog dijagrama, gdje značenje nosi položaj a ne duljina, raspon smije
slijediti podatke, uz obavezu da os bude označena tako da čitatelj vidi odakle
počinje.

Odatle slijedi pravilo koje vrijedi i za tuđi i za vlastiti graf. Odsječena os
dopuštena je kada je razlika koju treba vidjeti manja od šuma na osi od nule, a
uvjet je da odsjecanje bude vidljivo. Sakriveno odsjecanje čitatelju oduzima
podatak koji mu treba da bi prosudio tvrdnju, a to je isti postupak koji
poglavlje o zavaravanju brojkama opisuje kao odabir prikaza prema željenom
zaključku.

Ista logika vrijedi za logaritamsku ljestvicu, koja dugi desni rep raspodjele
stišće i time pokazuje strukturu koja se na izvornoj ljestvici zbila u jedan
stupac. Ona ne krivotvori ništa, ali mijenja što znači jednaki razmak, pa graf
koji je koristi mora to reći u oznaci osi. Poglavlje o sažimanju podataka istu
je pretvorbu uvelo brojčano, i graf od nje ne traži ništa novo.

## Mala višestruka polja

Kada skupina ima više od tri ili četiri, boja prestaje raditi. Krivulje se
preklapaju, legenda traži stalno vraćanje pogleda, a čitatelj usporedbu
provodi po sjećanju. Alternativa je da se isti graf ponovi za svaku skupinu.

**Mala višestruka polja** (*small multiples*) niz su prikaza istoga oblika i
iste ljestvice, po jedan za svaku skupinu, tako da se razlike među skupinama
očitavaju usporedbom položaja između polja.

Zajednička ljestvica je uvjet bez kojega postupak gubi smisao. Kada svako polje
dobije vlastiti raspon, panel s malim razlikama izgleda jednako dramatično kao
panel s velikima, pa se usporedba koja je bila svrha prikaza više ne može
provesti. Slobodne osi imaju svoje mjesto tamo gdje se uspoređuje oblik, a ne
razina, ali to je iznimka koja se izriče, a ne zadana postavka.

*Slika. Ista raspodjela u zbirnom polju i u četirima skupinskim poljima uz zajedničku os. Zbirni oblik nastaje preklapanjem raspodjela različitih položaja.*

Gornji prikaz ima jedan vrh i dugi rep. Donji pokazuje da taj oblik nije
svojstvo nijedne skupine nego posljedica njihova zbrajanja, jer se vrh pomiče
prema manjim vrijednostima kako dob raste. Zbirna raspodjela postoji, uredno je
izračunata i ne opisuje nijednog stvarnog ispitanika osobito dobro.

To je vizualni oblik pojave koju je Simpson opisao brojčano na tablicama
frekvencija (Simpson, 1951), i razlog zbog kojeg poglavlje o povezanosti tom
pitanju vraća s koeficijentom u ruci. Prikaz koji skupine zbraja nije pogrešan,
nego odgovara na drugo pitanje od prikaza koji ih razdvaja. Nevolja nastaje kada
se odgovor na prvo pitanje objavi kao odgovor na drugo.

## Graf pred čitateljem

Graf mora raditi u tri okolnosti koje autor pri crtanju obično ne vidi.
Netko ga čita u crno-bijelom tisku, netko preko čitača zaslona, a netko razlikuje
boje drukčije od autora.

Prva obveza je da boja nikada ne bude jedini nosač značenja. Kada se skupine
razlikuju samo tinkturom, uklanjanje boje uklanja podatak, pa graf koji je u
digitalnom izdanju čitljiv u tiskanom prestaje biti graf. Rješenje je da kanal
koji nosi razliku bude udvostručen, dakle da uz boju stoji i oblik oznake,
vrsta linije ili izravna oznaka uz krivulju. Paleta ove knjige zbog istog je
razloga poredana po svjetlini, a ne po tonu, pa u tisku daje razlučive sive
razine.

Druga obveza je opis. Svaki graf u knjizi nosi alternativni tekst koji kaže što
se na njemu vidi, a ne kako je nastao. Dobar opis imenuje varijable, smjer i
najizrazitiju osobinu obrasca, i piše se tako da čitatelj koji sliku ne vidi
dobije isti nalaz, a ne popis elemenata. Opis koji glasi „graf prikazuje odnos
dviju varijabli" nije ispunio obvezu, jer ne prenosi ništa što naslov već ne
kaže.

Treća obveza je izravno označavanje. Legenda traži da čitatelj pamti par boje i
imena dok pogled putuje između legende i grafa, a oznaka postavljena uz krivulju
taj put uklanja. Isto vrijedi za redoslijed kategorija, koji abecedni poredak
gotovo nikada ne pogađa. Kategorije poredane po veličini čitaju se bez napora,
a poredane po abecedi traže da čitatelj sam obavi rangiranje koje je graf mogao
obaviti umjesto njega.

Tri obveze vrijede za graf koji sami crtamo. Pred tuđim grafom iste odluke
postaju pitanja, i tada gramatika iz prvog odjeljka radi kao popis provjere.
Vrijedi ga provesti do kraja na primjeru koji je već pred nama, dakle na desnom
polju s odsječenom osi.

Prvo pitanje glasi što predstavlja jedna oznaka. Ondje jedan stupac stoji za
jednu dobnu skupinu, dakle za agregat, a ne za ispitanika, pa se iz njega ne
smije zaključivati ništa o pojedincu. Drugo pitanje traži pridruživanja, a ona
su dva, jer kategorija određuje vodoravni položaj, a prosjek duljinu stupca.
Boja i širina ne nose ništa, što je uredno, budući da bi svaka razlika u njima
sugerirala razliku koje u podacima nema.

Treće pitanje je najtiše i ovdje najvažnije. Prije crtanja izračunata je
aritmetička sredina po skupini, čime su odbačene sve raspodjele, a s njima i
dugi desni rep koji je histogram pokazao. Stupac visok
`r hr_broj(s5_najmladi$prosjek, 0)` minuta postoji, ali ne postoji ispitanik
kojemu ta vrijednost pripada, jer je medijan iste skupine
`r hr_broj(s5_najmladi$medijan, 0)` minuta. Četvrto pitanje odnosi se na
ljestvicu i otkriva ono zbog čega je prikaz uopće sporan, dakle da os ne počinje
od nule i da to nije označeno.

Iz četiri odgovora slijedi presuda koja je preciznija od dojma. Prikaz nije
netočan, nego kombinira odbačenu raspodjelu s neoznačenim odsjecanjem, pa
duljina stupca ne odgovara ni vrijednosti ni tipičnom ispitaniku. Isti se popis
primjenjuje na novinsku grafiku, na sliku iz izvještaja i na graf koji je
proizveo asistent, i traži manje vremena nego čitanje teksta koji uz njega
stoji.

## Interakcija — Isti podaci, četiri grafa

Interakcija prikazuje iste simulirane podatke četirima geometrijama. Promjena
grafa ne mijenja opažanja, ali mijenja usporedbu koja postaje laka ili teška.
Čitatelj tako bira prikaz prema tvrdnji, a ne prema dojmu atraktivnosti.

*Slika. Isti simulirani podaci prikazani odabranom geometrijom. Izbor prikaza mijenja vidljivu usporedbu, ne opažanja.*

**Što isprobati.**

1. Odaberite raspršeni dijagram i opišite odnos varijabli bez sažimanja po skupinama.
2. Prijeđite na histogram i utvrdite koja je prethodna informacija nestala.
3. Usporedite raspodjelu po skupinama s prikazom njihovih sredina.
4. Odaberite graf za tvrdnju o razlikama među tipičnim ishodima i obrazložite izbor.

**Statistika u divljini.**
**Kružni dijagram nikada.** Zabrana kruži uredništvima i priručnicima kao
utvrđena činjenica, a redovito se poziva na jedan izvor. Cleveland i McGill
doista su izmjerili da sudionici točnije očitavaju položaj na zajedničkoj osi
nego kut, i taj nalaz stoji (Cleveland, 1984). Iz njega slijedi da udio koji nosi
zaključak ne treba kodirati kutom.

Ne slijedi zabrana. Pokusi su mjerili točnost očitavanja omjera dviju
istaknutih vrijednosti, a ne razumijevanje prikaza u kontekstu, pamćenje ni
brzinu prepoznavanja (Cleveland, 1984). Prikaz u kojem treba vidjeti da jedna
kategorija drži otprilike polovinu, a ne rangirati sedam bliskih udjela, ne pada
pod izmjereni nedostatak. Kratki oblik tvrdnje sadrži pravi nalaz i izgubljen
uvjet pod kojim vrijedi, što je najčešći način na koji izmjeren rezultat
postane pravilo.

**Pitajte model.**
Asistent može predložiti geometriju i napisati alt-tekst, ali treba dobiti
pitanje koje graf mora odgovoriti. Nakon izrade provjeravamo zajedničke osi,
nazive jedinica, redoslijed kategorija i nosi li boja značenje koje nestaje u
tisku.

Dva promašaja ponavljaju se dovoljno često da ih vrijedi tražiti unaprijed.
Asistent rado dodaje izglađenu liniju kroz raspršeni dijagram, čime u prikaz
uvodi model koji nitko nije zatražio i koji poglavlje o regresiji tek uvodi.
I rado veže boju uz kategoriju bez drugoga nosača razlike, pa graf koji je na
zaslonu čitljiv u tisku ostaje bez jednog stupca podataka.

> Predloži najjednostavniji graf za ovu tvrdnju. Obrazloži koja usporedba nosi
> zaključak, navedi potrebnu ljestvicu i napiši alt-tekst bez tumačenja koje
> podaci ne podupiru.

**Nađite grešku.**
Za usporedbu udjela triju kategorija asistent je predložio ovaj poziv.

Os počinje od nule, kategorije su označene, a vrijednosti stoje uz stupce. Šira
treća kategorija, prema obrazloženju, samo popravlja optičku ravnotežu prikaza.

Greška je različita širina stupca. Površina tada nosi drugo vizualno značenje i
pojačava razliku koja bi trebala biti kodirana samo duljinom.

## Razrađeni primjer

Zadatak je provjeriti koliko brojčani sažetak sam po sebi jamči o strukturi
podataka. Anscombeovi su skupovi za to izabrani zato što su im sažeci gotovo
jednaki po konstrukciji (Anscombe, 1973), pa ostaje samo pitanje što prikaz
dodaje. Podaci `anscombe` ugrađeni su u R i reproduciraju objavljeni kvartet.

Prije crtanja vrijedi vidjeti koliko je sličnost bliska. Aritmetičke sredine
ishoda u četirima skupovima iznose `r hr_broj(s5_ans$sredina_y[[1]], 2)`,
`r hr_broj(s5_ans$sredina_y[[2]], 2)`, `r hr_broj(s5_ans$sredina_y[[3]], 2)` i
`r hr_broj(s5_ans$sredina_y[[4]], 2)`, a standardne devijacije
`r hr_broj(s5_ans$sd_y[[1]], 2)`, `r hr_broj(s5_ans$sd_y[[2]], 2)`,
`r hr_broj(s5_ans$sd_y[[3]], 2)` i `r hr_broj(s5_ans$sd_y[[4]], 2)`. Tablica
sastavljena od tih osam brojeva ne bi imala što reći, jer se skupovi po njoj ne
razlikuju.

Prvi blok slaže četiri skupa u jednu tablicu s jednim opažanjem u svakom redu.
Drugi ispisuje odluke gramatike u redoslijedu u kojem smo ih izgradili. Poziv
`aes` pridružuje varijable osima, `geom_point` bira oznaku, `geom_smooth` dodaje
izračun koji nastaje prije crtanja, a `facet_wrap` razdvaja skupove u ponovljena
polja. Dodani pravac je onaj najmanjih kvadrata, u izvornom radu jednak u sva
četiri skupa (Anscombe, 1973), a poglavlje o regresiji pokazuje kako se dobiva.
Nakon ovog imenovanja svaki se graf u knjizi može pročitati bez novoga
objašnjenja, jer se iste četiri odluke vraćaju u svakom pozivu.

Anscombeov kvartet s jednakim sažecima i različitim oblicima. Izrada autora
prema anscombe1973.

Prvi skup približno odgovara linearnoj priči. Drugi traži zakrivljeni opis.
Treći i četvrti pokazuju koliko jedno opažanje može određivati pravac.
Zaključak zato ne glasi da je korelacija beskorisna. Glasi da se brojčani
sažetak čita uz prikaz strukture iz koje je nastao.

## Sažetak

Graf je skup odluka o tome što jedna oznaka predstavlja, koja varijabla ulazi u
koji kanal, što je izračunato prije crtanja i kako se vrijednost pretvara u
vizualnu veličinu. Te se odluke provjeravaju pojedinačno, a njihov redoslijed
nije stvar ukusa, jer je izmjereno da kanali nose usporedbu različito točno
(Cleveland, 1984). Svaki prikaz nešto čuva i nešto odbaci, pa se bira prema
tvrdnji koju treba provjeriti, a ne prema izgledu. Raspon osi, razdvajanje u
mala polja i oslanjanje na boju mijenjaju što će čitatelj vidjeti bez ijedne
promjene u podacima, što graf čini argumentom koji podliježe istoj provjeri kao
brojka. Sljedeće poglavlje uzima jedan od tih prikaza, raspršeni dijagram,
sažima ga u jedan koeficijent i pita što je pritom izgubljeno.

## Pojmovi

gramatika grafike (*grammar of graphics*), pridruživanje (*aesthetic mapping*),
geometrija grafa (*geom*), ljestvica (*scale*), grafička percepcija (*graphical
perception*), mala višestruka polja (*small multiples*), pristupačnost
(*accessibility*), alt-tekst (*alternative text*), utjecajno opažanje
(*influential observation*)

## Zadaci

### Konceptualni

Odaberite graf za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Za svaki izbor navedite što prikaz odbacuje.
Predajte tri izbora s obrazloženjem.

### Računski

Upotrijebite interakciju poglavlja. Za svaki od četiriju prikaza zapišite što
čuva, što izračunava prije crtanja i koju usporedbu olakšava, a zatim iste
odluke pročitajte s Anscombeovih prikaza iz razrađenog primjera (Anscombe, 1973).
Predajte tablicu s četirima redovima i jednom rečenicom obrazloženja u svakom.
Postupak za ponavljanje izračuna nad cijelim skupom nalazi se u praktikumu.

### Kritički

Pronađite objavljeni graf sa skraćenom osi i prosudite je li odsjecanje
opravdano. Odredite koliko bi razlika zauzela prostora na osi od nule, je li
prekid vidljivo označen i mijenja li se zaključak teksta uz graf. Predajte
odlomak s presudom i s uvjetom pod kojim bi presuda bila suprotna.

### Revizija modela

Ocijenite prijedlog modela iz okvira. Imenujte odluke gramatike koje su
ispravno odgovorene, jednu koja obmanjuje, redak koda u kojem ta odluka stoji i
način njezina popravka.
