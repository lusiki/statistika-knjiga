# Vizualizacija kao argument

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Isti podaci, četiri grafa | DigiKat, simulirana anketa, Anscombeov kvartet | pogl. 3–4 |

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
sustav postavio Wilkinson (Wilkinson, 2005), a paket ggplot2 postao je jedna od
njezinih najpoznatijih izvedbi (Wickham, 2016). Sama gramatika ne pripada nijednom
programu i primjenjuje se pri čitanju tiskane grafike, bez pisanja koda.

Najprije treba znati što predstavlja jedna oznaka na grafu. Točka može stajati
za ispitanika, državu, godinu ili stranku, a prikazi tu jedinicu mijenjaju bez
najave. Kada agregat zamijeni pojedinca, mijenja se i pitanje na koje graf
odgovara, što je ista opasnost koju opisuje poglavlje o mjerenju i dizajnu.

**Geometrija** određuje prikazuje li se ta jedinica točkom, stupcem, linijom ili
drugom oznakom. Sljedeći korak pridružuje varijable vizualnim kanalima,
položaju na dvjema osima, boji, veličini i obliku.

**Pridruživanje** (*aesthetic mapping*) je odluka koja varijabla ulazi u koji
vizualni kanal, čime se određuje koja usporedba čitatelju postaje neposredno
dostupna.

Pridruživanje je tvrdnja o tome što zaslužuje usporedbu. Kada skupinu nosi
boja, graf poziva na neposrednu usporedbu skupina. Kada je skupina razdvojena u
zasebna polja, graf traži da se obrazac čita u svakom polju. Podaci
ostaju isti, argument se mijenja, a obmane nije bilo.

Najtiša odluka dolazi prije crtanja. Graf redovito nešto izračuna prije nego što
postavi prvu oznaku. Stupac visine prosjeka odbacio je raspodjelu, okvir s
brkovima izgubio je informaciju o broju vrhova, a izglađena linija dodala je
model koji nitko nije zatražio. Poglavlje o sažimanju pokazalo je koji sažetak
što gubi, a gramatika tome dodaje da je i sam graf redovito sažetak, samo
neoznačen. Anscombeov kvartet poseban je slučaj upravo tog pravila
(Anscombe, 1973).

**Ljestvica** je pravilo kojim vrijednost postaje vizualna veličina. Raspon osi,
njezin prekid, logaritamska transformacija i položaj sredine u ljestvici boja
mijenjaju koliko promjena zauzima prostora, a podatke pritom ne mijenjaju.
**Koordinatni sustav** zatvara popis i najčešće služi kao opomena, jer polarne
koordinate duljinu pretvaraju u kut i time istu usporedbu čine težom.

Iz tih odluka slijedi postupak za čitanje tuđega grafa. Što predstavlja jedna
oznaka, što je pridruženo kojem kanalu, što je izračunato prije crtanja i što
dopušta ljestvica jesu pitanja koja se pri čitanju novinske grafike postavljaju
bez ikakva programa. Knjiga taj postupak dalje koristi pri svakom rastavljanju
objavljene tvrdnje.

## Što oko može očitati

Gramatika kaže da oznaka nosi usporedbu, ali ne kaže koliko dobro. Cleveland i
McGill povezali su ranije psihofizičke nalaze s vlastitim pokusima u kojima su
sudionici procjenjivali omjere vrijednosti prikazanih različitim kanalima
(Cleveland, 1984). Izravno su potvrdili prednost položaja pred duljinom i kutom,
a za širi su skup kanala predložili poredak po očekivanoj pogrešci. Na prvom je
mjestu položaj na zajedničkoj osi, zatim položaj na odvojenim osima s
usklađenom ljestvicom, duljina, nagib i površina, a na kraju obujam,
zakrivljenost i zasićenost boje (Cleveland, 1984). Taj je puni poredak hipoteza
utemeljena na više izvora, a ne popis svih kanala izravno uspoređenih u njihovu
pokusu.

Poredak nije popis zabrana nego pravilo raspodjele. Kanal na vrhu poretka
dodjeljuje se veličini koja nosi zaključak, a kanali s dna sekundarnim
razlikama, gdje je gruba procjena dovoljna. Kružni dijagram kodira udio kutom, a
kut leži nisko u poretku, pa isti podaci u stupcima na zajedničkoj osi
proizvode točnije očitanje (Cleveland, 1984). Kada nekoliko udjela treba samo
prepoznati, a ne rangirati, ta razlika prestaje biti važna.

Iz istog poretka slijedi i zašto trodimenzionalni prikaz ravnih podataka može
pogoršati očitanje. Perspektiva jednostavnu duljinu pretvara u kombinaciju
duljine, površine i prividnoga obujma, a potonji su kanali pri dnu predloženoga
poretka (Cleveland, 1984). Dodavanje ukrasa kanalu koji nosi zaključak pripada
istoj obitelji postupaka kao skraćena os iz poglavlja o zavaravanju brojkama.

Tufte je istom problemu pristupio heuristikom raspodjele tinte na stranici i
predložio da se za svaki element pita nosi li podatak (Tufte, 2001). Sjena ispod
stupca, obrub oko svake oznake i preljev boje mogu trošiti prostor i pažnju bez
nove informacije, pa ih Tufte ubraja u grafički otpad. To nije zabrana svakoga
elementa koji ne prikazuje podatke. Rešetka, razdjelna crta ili izravna oznaka
mogu olakšati očitanje, grupiranje i pristupačnost prikaza. Razuman je test ukloniti element
i provjeriti jesu li usporedba ili snalaženje postali teži. Ako nisu, element
nije potreban.

U prikazima u kojima duljina ili površina izravno predstavlja kvantitativnu
promjenu Tufte uspoređuje veličinu učinka koji graf pokazuje s veličinom učinka
u podacima. Taj omjer naziva faktorom laži (Tufte, 2001). Omjer blizu jedinice
podupire tvrdnju da je geometrijsko kodiranje razmjerno, ali ne dokazuje da je
cijeli graf pošten. Skraćena os, površina umjesto duljine ili perspektiva mogu
omjer povećati bez ijedne netočne brojke. Mjera je zato korisna kao ograničena
provjera jasne geometrijske usporedbe, a ne kao opća ocjena svakoga grafa.

## Prikaz prema tvrdnji

Pitanje kojim graf počinje nije koji je prikaz lijep nego koju tvrdnju treba
provjeriti. Broj i vrsta varijabli tu odluku gotovo određuju, pa je vrijedi
imati pri ruci.

| Što se prikazuje | Uobičajeni izbor | Što prikaz čuva, a što odbacuje |
|---|---|---|
| jedna brojčana varijabla | histogram, krivulja gustoće | čuva oblik cijele raspodjele, gubi pojedinačno opažanje |
| jedna kategorijalna varijabla | stupci na zajedničkoj osi | čuva učestalost, ne kaže ništa o raspršenosti unutar kategorije |
| brojčana po skupinama | okvir s brkovima | čuva medijan, kvartile i izdvojena opažanja, odbacuje broj vrhova i položaj većine opažanja |
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

Prikaz učestalosti riječi najprije traži odluku što se broji. U šest namjerno
odabranih naslova o grafičkom prikazu podataka ima 36 pojavnica i 28 različitih
oblika [Anscombe, 1973; Cleveland, 1984; Tufte, 2001; Wilkinson, 2005;
Wickham, 2016; Matejka, 2017]. Pravilo je skromno i ponovljivo. Sva se slova
pretvaraju u mala, interpunkcija se uklanja, a oblici se ne svode na zajednički
korijen. Zato
`graphs`, `graphical` i `graphics` ostaju tri različite jedinice.

Sljedeći prikaz izdvaja šest ponovljenih oblika i učestalost svakoga od
preostala 22. Naziv zadnjeg retka namjerno govori da njegova duljina vrijedi za
svaki oblik zasebno, a nije njihov zbroj.

*Slika. Učestalost točnih oblika u šest namjerno odabranih bibliografskih naslova. Izrada autora prema objavljenim naslovima [@anscombe1973; @cleveland1984; @tufte2001; @wilkinson2005; @wickham2016; @matejka2017].*

Prikaz opisuje samo tih šest naslova. Ne predstavlja literaturu o
vizualizaciji, a kamoli znanstveno pisanje općenito. Upravo je ta granica dio
čitanja. Prije tumačenja treba imenovati jedinicu, pretvorbu, nazivnik i skup na
koji se zaključak smije odnositi. Poglavlje o algoritmima vratit će isti nadzor kada tekst
postane ulaz algoritma, bez uvođenja obrade prirodnoga jezika ovdje.

## Dvije varijable u istom prostoru

Kada obje varijable nose brojeve, raspršeni dijagram može sačuvati svako
opažanje bez prethodnoga sažimanja. Svaka točka je jedno opažanje na svojem
mjestu, pa se iz oblaka čita smjer veze, njezina zakrivljenost, postojanje
podskupina i položaj opažanja koja odudaraju. Zbog toga je u ovom poglavlju
raspršeni dijagram polazište provjere odnosa.

Njegova slabost je vlastiti uspjeh. Kada opažanja ima mnogo, točke se
preklapaju, a gustoća prestaje biti vidljiva, jer sto opažanja na istom mjestu
izgleda kao jedno. Uobičajeni popravak je djelomična prozirnost oznake, čime
preklopljena područja postaju tamnija, pa gustoća opet nosi značenje. Drugi je
popravak lagano razmicanje oznaka, koje se koristi kada je jedna varijabla
zapravo diskretna, a treći prelazak na prikaz koji gustoću računa izravno.

Na raspršeni se dijagram redovito dodaje izglađena linija koja kroz oblak
provlači procijenjeni prosječni odnos. Ta linija nije podatak nego model, što je
ključna napomena za njezino čitanje. Ona pretpostavlja oblik veze,
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

*Slika. Broj ispitanika, prosjek i medijan dnevnih minuta u četirima dobnim skupinama simuliranoga nastavnog skupa `anketa_mreze`. Izrada autora.*

Tablica skupinskih sažetaka čuva vrijednosti za račun, a
usporedba dviju osi pokazuje koliko dojam o istoj razlici
ovisi o početku osi.

*Slika. Isti prosjeci na dvjema osima. Lijevi prikaz počinje od nule, desni od najmanje vrijednosti, a razlika među skupinama nije se promijenila.*

Desni prikaz nije izmislio nijedan broj. Sve četiri vrijednosti stoje ondje gdje
i lijevo, a promijenio se samo raspon koji im je dodijeljen. Kod stupaca je to
ozbiljna pogreška, jer duljina stupca nosi značenje, pa skraćena os duljinu
pretvara u veličinu koja više ne odgovara vrijednosti. Kod linijskog grafa i
raspršenog dijagrama, gdje značenje nosi položaj, a ne duljina, raspon smije
slijediti podatke, uz obvezu da os bude označena tako da čitatelj vidi odakle
počinje.

Odatle slijedi pravilo koje vrijedi i za tuđi i za vlastiti graf. Skraćena os
može biti opravdana u linijskom ili raspršenom prikazu kada položaj, a ne
duljina od nule, nosi usporedbu. Odsjecanje tada mora biti vidljivo. Kod stupaca
vidljiva oznaka jasno pokazuje zahvat, ali ne vraća duljini njezino značenje, pa
os treba početi od nule. Neoznačeno skraćivanje dodatno uskraćuje informaciju
potrebnu za prosudbu tvrdnje.

DigiKatov izvadak sadrži `r hr_broj(s5_izvori_sazetak$izvora, 0)` imenovane
domene i `r hr_broj(s5_izvori_sazetak$objava, 0)` objava unutar toga korpusa
(Šikić, 2026). Medijan je `r hr_broj(s5_izvori_sazetak$medijan, 0)` objave po
domeni, a najveća vrijednost `r hr_broj(s5_izvori_sazetak$najvise, 0)`. Na
linearnoj osi raspon od jedan do najveće vrijednosti stisnuo bi većinu domena
uz lijevi rub. Logaritamski prikaz zato zadržava broj objava,
ali jednake razmake na osi dodjeljuje jednakim omjerima.

*Slika. Raspodjela broja objava među 3.604 imenovane domene na logaritamskoj osi. Izrada autora prema DigiKatu [@digikat2026].*

Logaritamska os ne mijenja izvorne vrijednosti, ali sažima vizualne razmake među
velikim vrijednostima i time mijenja prividni oblik raspodjele. Pomak od 10 do
100 jednak je pomaku od 100 do 1.000, pa se na toj osi uspoređuju omjeri, a ne
apsolutne razlike. Zato naziv osi mora izreći pretvorbu. Tvrdnja ostaje
ograničena na imenovane domene u korpusu; graf ne opisuje sve hrvatske medije,
njihove korisnike ni pojedinačne objave. Poglavlje o sažimanju podataka istu je
pretvorbu uvelo brojčano, i graf od nje ne traži ništa novo.

## Mala višestruka polja

Kada prikaz ima više od tri ili četiri skupine, boja prestaje raditi. Krivulje se
preklapaju, legenda traži stalno vraćanje pogleda, a čitatelj usporedbu
provodi po sjećanju. Alternativa je da se isti graf ponovi za svaku skupinu.

**Mala višestruka polja** (*small multiples*) niz su prikaza istoga oblika i
iste ljestvice, po jedan za svaku skupinu, tako da se razlike među skupinama
očitavaju usporedbom položaja između polja.

Zajednička ljestvica je uvjet bez kojega postupak gubi smisao. Kada svako polje
dobije vlastiti raspon, niz polja s malim razlikama izgleda jednako dramatično
kao niz polja s velikima, pa se usporedba koja je bila svrha prikaza više ne
može provesti. Slobodne osi imaju svoje mjesto tamo gdje se uspoređuje oblik, a
ne razina, ali to je iznimka koja se izrijekom navodi, a ne zadana postavka.

DigiKatov mjesečni izvadak za 2024. nema retke od veljače do svibnja, siječanj
je djelomičan, a lipanj označuje lom metode i promjenu obuhvata
(Šikić, 2026). Nedostatak retka nije nula. Zato tablica prikazuje svih 12
mjeseci, a graf ne spaja siječanj s lipnjem i ne popunjava prazninu.

*Slika. Broj objava i udio weba u mjesečnom zbroju platformskoga izvatka za 2024. Duga crta označuje mjesec bez retka, ne nulu. Izrada autora prema DigiKatu [@digikat2026].*

Broj objava odgovara na pitanje o mjesečnoj količini, a udio weba na pitanje o
sastavu iste mjesečne količine. Nazivnik udjela u [mjesečnoj
tablici](#tbl-s5-digikat-2024) jest zbroj platformskih redaka toga mjeseca. To
nije zbroj 551.712 iz datoteke imenovanih domena, jer dvije datoteke nemaju istu
jedinicu ni zajednički ključ. Mala višestruka polja zato
prikazuju samo broj objava, uz zajedničku logaritamsku os za četiri platforme s
najvećim zbrojem objava u dostupnim mjesecima 2024. i njihov objedinjeni ostatak.

*Slika. Mjesečni broj objava za četiri platforme s najvećim zbrojem u dostupnim mjesecima 2024. i objedinjene ostale platforme. Praznina od veljače do svibnja znači da nema redaka; isprekidana crta i odvojene točke u lipnju označuju lom metode. Zajednička okomita os je logaritamska. Izrada autora prema DigiKatu [@digikat2026].*

Ni u jednom polju linija ne prelazi četveromjesečnu prazninu, a lipanjska je
točka odvojena od niza nakon promjene obuhvata. Zbog djelomičnoga siječnja i
loma metode prikaz ne podupire tvrdnju o trendu, rastu ni razlici prije i
poslije lipnja. On pokazuje samo raspored dostupnih brojeva objava među
platformama i istodobno čuva trag onoga što nije zabilježeno.

## Graf pred čitateljem

Graf mora raditi u tri okolnosti koje autor pri crtanju obično ne vidi.
Netko ga čita u crno-bijelom tisku, netko preko čitača zaslona, a netko razlikuje
boje drukčije od autora.

Boja nikada ne smije biti jedini nosač značenja. Kada se skupine razlikuju samo
bojom, njezino uklanjanje uklanja podatak, pa graf u tiskanom izdanju prestaje
prenositi tu razliku. Kanal koji nosi razliku zato se
udvostručuje oblikom oznake, vrstom linije ili izravnom oznakom uz krivulju.
Paleta ove knjige zbog istog je razloga poredana po svjetlini, a ne po tonu, pa
u tisku daje razlučive sive razine.

Alternativni tekst prenosi ono što se na grafu vidi, a ne način na koji je
nastao. Dobar opis imenuje varijable, smjer i najizrazitiju osobinu obrasca kako
bi čitatelj koji sliku ne vidi dobio isti nalaz, a ne popis elemenata. Opis koji
glasi „graf prikazuje odnos dviju varijabli" ne ispunjava tu obvezu jer ne
prenosi ništa što naslov već ne kaže.

Izravne oznake uklanjaju put između legende i grafa na kojem čitatelj mora
pamtiti par boje i imena. Isto vrijedi za redoslijed kategorija, koji abecedni
poredak rijetko čini informativnim. Kategorije poredane po veličini čitaju se
bez napora, a poredane po abecedi traže da čitatelj sam obavi rangiranje koje
je graf mogao obaviti umjesto njega.

Odluke o boji, alternativnom tekstu i oznakama vrijede za graf koji sami crtamo.
Pri čitanju tuđega grafa iste odluke postaju provjera gramatike iz prvog
odjeljka. Desno polje sa skraćenom osi pokazuje kako ta provjera radi.

Jedinica prikaza u tom je polju dobna skupina. Jedan stupac zato predstavlja
agregat, a ne ispitanika, pa se iz njega ne smije zaključivati ništa o pojedincu.
Pridruživanje povezuje kategoriju s vodoravnim položajem, a prosjek s duljinom
stupca. Boja i širina ne nose ništa, što je uredno, jer bi svaka razlika u njima
sugerirala razliku koje u podacima nema.

Sažimanje prethodi crtanju jer je po skupini izračunata aritmetička sredina.
Time su odbačene sve raspodjele, a s njima i dugi desni rep koji je histogram
pokazao. Stupac visok `r hr_broj(s5_najmladi$prosjek, 0)` minuta nije
pojedinačno opažanje, nego izračunati prosjek, dok medijan iste skupine iznosi
`r hr_broj(s5_najmladi$medijan, 0)` minuta. Ljestvica otkriva da os ne počinje
od nule, premda je ta nastavna intervencija jasno označena.

Takva provjera daje presudu precizniju od dojma. Prikaz nije brojčano netočan,
nego kombinira odbačenu raspodjelu s vidljivo označenim, ali za stupce
neprikladnim odsjecanjem. Duljina stupca zato ne odgovara prikazanoj vrijednosti,
a prosjek ne opisuje nužno tipičnoga ispitanika. Oznaka pomaže otkriti zahvat,
ali ga ne čini ispravnim kodiranjem. Ista se provjera primjenjuje na novinsku
grafiku, sliku iz izvještaja i graf koji je proizveo asistent.

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
nego kut, i taj nalaz ostaje valjan (Cleveland, 1984). Iz njega slijedi da udio koji nosi
zaključak ne treba kodirati kutom.

Ne slijedi zabrana. Pokusi su mjerili točnost očitavanja omjera dviju
istaknutih vrijednosti, a ne razumijevanje prikaza u kontekstu, pamćenje ni
brzinu prepoznavanja (Cleveland, 1984). Prikaz u kojem treba vidjeti da jedna
kategorija drži otprilike polovinu, a ne rangirati sedam bliskih udjela, ne pada
pod izmjereni nedostatak. Kratki oblik tvrdnje sadrži pravi nalaz i izgubljen
uvjet pod kojim vrijedi, što je jedan čest način na koji izmjeren rezultat
postane pravilo.

**Pitajte model.**
Asistent može predložiti geometriju i napisati alternativni tekst, ali treba
dobiti pitanje na koje graf mora odgovoriti. Nakon izrade provjeravamo zajedničke osi,
nazive jedinica, redoslijed kategorija i nosi li boja značenje koje nestaje u
tisku.

Dva promašaja ponavljaju se dovoljno često da ih vrijedi tražiti unaprijed.
Asistent rado dodaje izglađenu liniju kroz raspršeni dijagram, čime u prikaz
uvodi model koji nitko nije zatražio i koji poglavlje o regresiji tek uvodi.
I rado veže boju uz kategoriju bez drugoga nosača razlike, pa graf koji je na
zaslonu čitljiv u tisku više ne pokazuje varijablu pripadnosti skupini.

> Predloži najjednostavniji graf za ovu tvrdnju. Obrazloži koja usporedba nosi
> zaključak, navedi potrebnu ljestvicu i napiši alternativni tekst bez tumačenja koje
> podaci ne podupiru.

**Nađite grešku.**
Za usporedbu udjela triju kategorija asistent je predložio ovaj poziv.

Os počinje od nule, kategorije su označene, a vrijednosti stoje uz stupce. Šira
treća kategorija, prema obrazloženju, samo popravlja optičku ravnotežu prikaza.

## Razrađeni primjer

Zadatak je provjeriti koliko brojčani sažetak sam po sebi otkriva o strukturi
podataka. Anscombeovi su skupovi za to izabrani zato što su im sažeci gotovo
jednaki po konstrukciji (Anscombe, 1973), pa ostaje samo pitanje što prikaz
dodaje. Podaci `anscombe` ugrađeni su u R i reproduciraju objavljeni kvartet.

Sličnost sažetaka najprije treba brojčano provjeriti. Zaokružene na dvije
decimale, sve četiri aritmetičke sredine ishoda iznose
`r hr_broj(s5_ans$sredina_y[[1]], 2)`, a sve četiri standardne devijacije
`r hr_broj(s5_ans$sd_y[[1]], 2)`. Tablica tih sažetaka zato ne bi razlikovala
oblike četiriju skupova.

Prvi dio slaže četiri skupa u jednu tablicu s jednim opažanjem u svakom redu.
Drugi dio ispisuje odluke gramatike u redoslijedu u kojem smo ih izgradili. Poziv
`aes` pridružuje varijable osima, `geom_point` bira oznaku, `geom_smooth` dodaje
izračun koji nastaje prije crtanja, a `facet_wrap` razdvaja skupove u ponovljena
polja. Dodani pravac procijenjen je iz opažanja i u izvornom je radu jednak u
sva četiri skupa (Anscombe, 1973), a poglavlje o regresiji pokazuje kako se
dobiva.
Ta četiri imena daju rječnik za čitanje kasnijih poziva, u kojima se iste
odluke vraćaju.

Sažeci četiriju parova gotovo su jednaki (Anscombe, 1973). Uspoređujemo sva
četiri polja i pitamo u kojem oblik podataka najviše proturječi priči koju bi ti
sažeci ispričali, pri jednakom rasponu osi i jednakom pravcu.

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
mala višestruka polja i oslanjanje na boju mijenjaju što će čitatelj vidjeti bez ijedne
promjene u podacima, što graf čini argumentom koji podliježe istoj provjeri kao
brojka. Prikaz učestalosti riječi uz to ovisi o jedinici, pretvorbi, nazivniku i
granici skupa na koji se zaključak odnosi; isti se nadzor vraća u poglavlju o
algoritmima. Poglavlje o povezanosti uzima jedan od tih prikaza, raspršeni
dijagram, sažima ga u jedan koeficijent i pita što je pritom izgubljeno.

## Pojmovi

gramatika grafike (*grammar of graphics*), pridruživanje (*aesthetic mapping*),
geometrija grafa (*geom*), ljestvica (*scale*), grafička percepcija (*graphical
perception*), prikaz učestalosti riječi (*word-frequency plot*), logaritamska
ljestvica (*logarithmic scale*), skraćena os (*truncated axis*), mala višestruka
polja (*small multiples*), pristupačnost prikaza (*visualization accessibility*),
alternativni tekst (*alternative text*), Anscombeov kvartet (*Anscombe's quartet*), utjecajno
opažanje (*influential observation*)

## Zadaci

### Konceptualni

Odaberite graf za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Za svaki izbor navedite što prikaz odbacuje.
Za jedan izbor dodajte alternativni tekst koji prenosi glavni nalaz i provjerite ostaje
li taj nalaz čitljiv bez boje. Predajte tri izbora s obrazloženjem, jedan
alternativni tekst i presudu o boji.

### Računski

Iz tablice skupinskih sažetaka uzmite najveći i najmanji
prosjek dnevnih minuta. Izračunajte njihovu razliku, a zatim je podijelite s
većim prosjekom i pretvorite u postotak. Usporedite dobiveni postotak s [dvama
prikazima osi](#fig-skraceni-raspon) i objasnite zašto se brojčana razlika nije
promijenila, premda se promijenio vizualni dojam. Predajte račun, postotak i
dvije rečenice prosudbe. Svi potrebni podaci nalaze se u tablici.

### Kritički

Pronađite objavljeni graf sa skraćenom osi i prosudite je li odsjecanje
opravdano. Odredite koliko bi razlika zauzela prostora na osi od nule, je li
prekid vidljivo označen i mijenja li se zaključak teksta uz graf. Predajte
odlomak s presudom i s uvjetom pod kojim bi presuda bila suprotna.

### Revizija modela

Ocijenite prijedlog modela iz okvira. Imenujte odluke gramatike koje su ispravno
odgovorene i onu koja obmanjuje. Opišite kako se grafička odluka treba promijeniti
da prikaz ponovno kodira udio samo duljinom, bez pisanja ili popravljanja koda.
Predajte prosudbu i opis promjene.
