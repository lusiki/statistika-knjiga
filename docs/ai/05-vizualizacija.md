# Vizualizacija kao argument

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Anscombe je sastavio četiri skupa s gotovo jednakim uobičajenim brojčanim
sažecima i jednakim prilagođenim pravcem, ali vrlo različitim grafovima
(Anscombe, 1973). U jednom se vidjela približno linearna veza, u drugom
zakrivljenost. Treći je imao utjecajnu točku, a četvrti okomit oblak uz
jedno izdvojeno opažanje.

Svi su sažeci bili ispravno izračunati. Ipak, nisu sačuvali raspored
pojedinačnih opažanja, pa su četiri različita oblika opisali gotovo istim
brojevima.

Što graf otkriva o podacima, a što izborom prikaza možemo sakriti?

U poglavlju o sažimanju birali smo mjeru prema obliku raspodjele i pitanju
koje nas zanima. Pred grafom nas čeka slična odluka. Prikaz prosjeka može
olakšati usporedbu skupina, ali sakriti razlike među osobama; prikaz svih
opažanja čuva te razlike, no može otežati čitanje. Želimo naučiti odabrati
prikaz iz kojega se tražena usporedba doista može vidjeti.

Anscombeovim ćemo se skupovima iz vinjete vraćati kao provjeri onoga što
brojčani sažetak izostavlja (Anscombe, 1973). To su namjerno konstruirani
parovi brojčanih vrijednosti. Jedna točka predstavlja jedan takav par, bez
stvarne osobe ili društvene pojave iza njega. Zato ih koristimo za ispitivanje
prikaza, a ne za sadržajni zaključak o nekoj populaciji. Usporedbom tablica i
grafova provjerit ćemo što možemo previdjeti kada preuzmemo samo gotove
sažetke.

Poznatu simuliranu anketu `anketa_mreze` iskoristit ćemo za prikaz dnevnih
minuta na društvenim mrežama po dobnim skupinama (Šikić, 2026). Uz nju ćemo
čitati i prikaze stvarnih zbirnih podataka projekta DigiKat, vodeći računa o
njihovu obuhvatu (Šikić, 2026). Primjeri se mijenjaju jer nas zanima ista
odluka u različitim situacijama. Prije čitanja oznake trebamo znati
predstavlja li ona osobu, skupinski sažetak ili zbroj objava.

Izbor prikaza obrazlažemo tako da čitatelj može provjeriti graf i bez
programa kojim je nacrtan. Ljestvica, oznake i opis trebaju pokazati obrazac
koji podaci podupiru te upozoriti na ono što je sažeto ili izostavljeno.

## Gramatika grafike

Grafom odlučujemo što ćemo uspoređivati položajem, duljinom, površinom ili
bojom. Izbor zato počinje pitanjem. Za raspodjelu jedne brojčane varijable
trebamo vidjeti oblik, za usporedbu kategorija zajedničku osnovicu, a za odnos
dviju brojčanih varijabli pojedinačna opažanja. Uredan graf neće pomoći ako
skriva ono što trebamo usporediti.

Nazivi poput stupčanog ili raspršenog dijagrama označuju uobičajene
kombinacije odluka. Svaki graf možemo rastaviti na te odluke i zasebno ih
provjeriti.

**Gramatika grafike** opisuje od čega je graf sastavljen. Određuje što
predstavlja oznaka, koja joj je varijabla pridružena, koji je račun prethodio
crtanju i kako se vrijednosti prenose u vizualne veličine.

Wilkinson je tu ideju razradio u sustav (Wilkinson, 2005), a ggplot2 jedna je
od njegovih poznatih programskih izvedbi (Wickham, 2016). Istim se načinom
razmišljanja možemo služiti pri čitanju tiskanog grafa, bez programiranja.

Najprije provjeravamo jedinicu. Točka može predstavljati ispitanika, državu,
godinu ili stranku. Ako umjesto pojedinaca prikažemo skupinske prosjeke, graf
odgovara na drugo pitanje. Zato promjenu jedinice treba jasno navesti.

**Geometrija** određuje oblik oznake, primjerice točku, stupac ili liniju.
Varijable zatim povezujemo s položajem na osima, bojom, veličinom ili oblikom
oznake.

**Pridruživanje** (*aesthetic mapping*) je odluka o tome koja se varijabla
prikazuje kojim vizualnim obilježjem. Time određujemo što će čitatelj moći
neposredno usporediti.

Ako skupine razlikujemo bojom u istom polju, lako ih uspoređujemo na
zajedničkim osima. Ako ih rasporedimo u zasebna polja, lakše pratimo obrazac
svake skupine. Podaci se ne mijenjaju, ali naglašavamo različite usporedbe.

Treba provjeriti i što je izračunato prije crtanja. Stupac koji prikazuje
prosjek skriva raspodjelu. Okvir s brkovima ne pokazuje broj njezinih vrhova,
a izglađena linija dodaje procijenjeni model. Graf zato može biti sažetak koji
gubi dio podataka, baš kao brojčana mjera. Anscombeovi skupovi pokazuju zašto
treba pogledati što je sažimanjem izostavljeno (Anscombe, 1973).

**Ljestvica** određuje kako se broj pretvara u vizualnu veličinu. Raspon osi,
prekid, logaritamska transformacija ili sredina ljestvice boja mijenjaju
prostor koji razlika zauzima. **Koordinatni sustav** određuje kako su položaji
raspoređeni. Polarne koordinate, primjerice, uvode kut i mogu otežati
usporedbu koju bismo na ravnoj osi lakše očitali.

Pri čitanju grafa zato tražimo jedinicu oznake, pridružene varijable,
prethodni račun i pravilo ljestvice. Ta pitanja možemo postaviti svakom grafu,
bez pristupa programu u kojem je izrađen.

Na sljedećem prikazu jedan stupac predstavlja dobnu skupinu iz simulirane
ankete `anketa_mreze` (Šikić, 2026). Vodoravni položaj označuje skupinu,
a okomiti položaj vrha prosječne dnevne minute, izračunate prije crtanja.
Stupac zato sažima više osoba i ne pokazuje raspodjelu njihovih odgovora.
Lijevo os počinje od nule, a desno je skraćena. Uspoređujemo iste prosjeke,
ali promjena ljestvice mijenja dojam njihovih razlika.

*Slika. Isti prosjeci na dvjema osima. Lijevi prikaz počinje od nule, desni od 15 minuta, ispod najmanjeg prosjeka. Dvije kose crte označuju prekid desne osi. Vrijednosti su jednake u oba prikaza. Izrada autora.*

## Što oko može očitati

Grafička percepcija jest način na koji iz položaja, duljina i drugih oznaka očitavamo podatke. Neke vizualne usporedbe čitamo točnije od drugih. Cleveland i McGill pokusima
su potvrdili prednost položaja pred duljinom i kutom (Cleveland, 1984).
Povezali su te rezultate s ranijim istraživanjima i predložili širi poredak
kanala. Prema tom se poretku najtočnije očitava položaj na zajedničkoj osi, zatim na
istovjetnim, ali neporavnatim osima, pa duljina, kut, nagib i površina. Obujam,
zakrivljenost i zasićenost boje nalaze se pri dnu (Cleveland, 1984). Cijeli taj
poredak nije provjeren jednim pokusom, nego je prijedlog oslonjen na više
izvora.

Za usporedbu koja određuje zaključak zato biramo kanal koji se lakše očitava.
Boja ili površina mogu poslužiti za razlike kod kojih je dovoljna gruba
procjena. Udjele ćemo točnije usporediti stupcima na zajedničkoj osi nego
kutovima kružnog dijagrama (Cleveland, 1984). Ako trebamo samo prepoznati
nekoliko izrazito različitih udjela, ta prednost može biti manje važna.

Trodimenzionalna perspektiva može otežati usporedbu ravnih podataka jer
duljinu kombinira s površinom i prividnim obujmom, slabijim kanalima u
predloženom poretku (Cleveland, 1984). Zato prije dodavanja treće dimenzije
provjeravamo donosi li novu informaciju ili samo mijenja dojam.

Tufte predlaže da za svaki grafički element pitamo koju informaciju prenosi
(Tufte, 2001). Sjene, obrubi i preljevi mogu odvlačiti pozornost bez korisnog
dodatka. Rešetka, razdjelna crta ili oznaka, s druge strane, mogu olakšati
čitanje. Uklanjanjem elementa možemo provjeriti otežava li njegov izostanak usporedbu
ili snalaženje na grafu.

Tufteov faktor laži uspoređuje relativnu promjenu prikazanu geometrijom s
relativnom promjenom u podacima (Tufte, 2001). Kada duljina ili površina izravno
predstavlja količinu, omjer blizu jedan pokazuje razmjerno kodiranje. Ne
potvrđuje da je cijeli graf pošten. Skraćena os, perspektiva ili zamjena
duljine površinom mogu povećati dojam i uz točne brojčane oznake. Ta mjera
služi određenim geometrijskim usporedbama, a ne općem ocjenjivanju svih
grafova.

## Prikaz prema tvrdnji

Prednost zajedničke osi pomaže nam izabrati način usporedbe, ali još trebamo
odlučiti koje podatke graf mora sačuvati. Za oblik raspodjele trebamo drukčiji
prikaz nego za usporedbu skupinskih prosjeka. Sljedeća tablica povezuje ta
pitanja s brojem i vrstom varijabli te pokazuje što pojedini izbor izostavlja.

| Što se prikazuje | Uobičajeni izbor | Što prikaz čuva, a što odbacuje |
|---|---|---|
| jedna brojčana varijabla | histogram, krivulja gustoće | čuva oblik cijele raspodjele, gubi pojedinačno opažanje |
| jedna kategorijalna varijabla | stupci na zajedničkoj osi | čuva učestalosti kategorija, izostavlja pojedinačne zapise i njihova druga obilježja |
| brojčana po skupinama | okvir s brkovima | čuva medijan, kvartile i izdvojena opažanja, odbacuje broj vrhova i položaj većine opažanja |
| dvije brojčane varijable | raspršeni dijagram | čuva svako opažanje, teško podnosi velik broj točaka |
| dvije kategorijalne varijable | grupirani ili složeni stupci | čuva odnos udjela, otežava usporedbu unutar složenih stupaca |

: Prikaz prema vrsti podataka i prema onome što svaki izbor žrtvuje. Izrada autora.

Svaki prikaz zadržava dio informacija i izostavlja ostale. Okvir s brkovima
sažima medijan i kvartile, pa može izgledati jednako za raspodjelu s jednim
ili dvama vrhovima. Histogram raspoređuje opažanja u razrede i prikazuje
njihove učestalosti, zbog čega lakše otkriva oblik. Više skupina, međutim,
može biti teže usporediti histogramima.

Za dvije kategorijalne varijable možemo izabrati stupce jedan uz drugi,
složene stupce ili stupce jednake ukupne visine koji prikazuju udjele.
Usporedni stupci pokazuju apsolutne brojeve. Stupci udjela pokazuju sastav,
ali skrivaju razliku između skupine od dvadeset i skupine od dvjesto osoba.
Tvrdnju da je skupina brojnija zato ne možemo opravdati samo grafom udjela.

Kod složenih stupaca samo najdonji segment ima zajedničku osnovicu. Ostali
počinju na različitim visinama, ovisno o prethodnim segmentima. Njihove su
duljine točne, ali ih je teže usporediti bez zajedničkog početka
(Cleveland, 1984). Ako zaključak ovisi o jednom takvom segmentu, korisno ga je
prikazati zasebno.

I riječi možemo uspoređivati kao kategorije, ali tek nakon što odredimo što
ćemo smatrati istom riječju. U šest odabranih naslova o vizualizaciji ukupno je
36 riječi i 28 različitih oblika [Anscombe, 1973; Cleveland, 1984; Tufte, 2001;
Wilkinson, 2005; Wickham, 2016; Matejka, 2017]. Do tih brojeva dolazimo tako da
sva slova pretvorimo u mala i uklonimo interpunkciju. Riječi ne svodimo na
zajednički korijen, pa su `graphs`, `graphical` i `graphics`
različite jedinice. Stupci će zato uspoređivati učestalost točnih oblika koje
smo tako odredili.

Primjer pretvorbe daje naslov *The Grammar of Graphics* (Wilkinson, 2005).
Nakon pretvorbe u mala slova i razdvajanja dobivamo četiri zapisa,
`the`, `grammar`, `of` i `graphics`. Svaki dodaje jedan svome brojaču.
Kad tako obradimo svih šest odabranih naslova, brojimo pojavljivanja riječi,
a ne broj knjiga. U Wickhamovu naslovu o paketu ggplot2 uklanjamo dvotočku,
ali zadržavamo `ggplot2` kao jedan oblik (Wickham, 2016).

Graf izdvaja šest oblika koji se ponavljaju. Zadnji redak pokazuje učestalost
svakog od preostala dvadeset dva oblika zasebno, a ne njihov zajednički zbroj.

*Slika. Učestalost točnih oblika u šest namjerno odabranih bibliografskih naslova. Izrada autora prema objavljenim naslovima [@anscombe1973; @cleveland1984; @tufte2001; @wilkinson2005; @wickham2016; @matejka2017].*

Rezultat opisuje samo odabranih šest naslova. Ne predstavlja svu literaturu o
vizualizaciji ili znanstveno pisanje. Pri tumačenju zato navodimo jedinicu,
obradu teksta, nazivnik i obuhvat. Iste ćemo odluke ponovno razmotriti kada
tekst postane ulaz algoritma.

## Dvije varijable u istom prostoru

Stupcima smo uspoređivali količine po kategorijama. Kada želimo sačuvati
odnos dviju brojčanih varijabli za svaku jedinicu, trebamo drugi raspored
oznaka. Raspršeni dijagram može prikazati svako
opažanje kao točku. Iz rasporeda čitamo smjer i zakrivljenost veze, podskupine
i izdvojena opažanja. Zato njime počinjemo provjeru odnosa.

Ako se mnoge točke preklapaju, ne vidimo koliko opažanja stoji na istom
mjestu. Djelomično prozirne točke mogu pokazati gušća područja tamnijima. Kod
diskretnih vrijednosti pomaže blago razmicanje točaka, a za vrlo mnogo
opažanja možemo izravno prikazati procijenjenu gustoću.

Izglađena linija na raspršenom dijagramu procijenjeni je model odnosa. Nije
dodatno opažanje. Njezin oblik ovisi o postupku procjene i može djelovati
uvjerljivo čak i kad podaci ne podupiru stabilan obrazac. Uvijek je zato
čitamo uz oblak točaka. U poglavlju o regresiji razradit ćemo kako se takve
linije dobivaju i provjeravaju.

## Poštena ljestvica

Vraćamo se simuliranoj anketi `anketa_mreze` iz poglavlja o sažimanju.
Prikazujemo prosječne dnevne minute na društvenim mrežama po dobnim skupinama
(Šikić, 2026). Raspon osi može znatno promijeniti dojam. Prosjeci se ovdje
razlikuju za `r hr_broj(s5_raspon_prosjeka, 1)` minuta, odnosno `r paste0(hr_broj(100 * s5_udio_raspona, 1), " %")` najvećeg prosjeka. Ta je
razlika stalna, ali njezina veličina na stranici ovisi o osi.

*Slika. Broj ispitanika, prosjek i medijan dnevnih minuta u četirima dobnim skupinama simuliranoga nastavnog skupa `anketa_mreze`. Izrada autora.*

Tablica skupinskih sažetaka čuva vrijednosti za račun, a
usporedba dviju osi pokazuje koliko dojam o istoj razlici
ovisi o početku osi.

Oba prikaza koriste iste četiri vrijednosti. Desni im dodjeljuje uži raspon
osi. Kod stupaca duljina predstavlja vrijednost, pa odsijecanje nule narušava
tu razmjernost. U linijskom ili raspršenom grafu uspoređujemo položaje, zbog
čega os može pratiti raspon podataka ako je jasno označena.

Stupce zato crtamo od nule. Oznaka skraćene osi otkriva zahvat, ali ne vraća
ispravan odnos duljina. Za linije i točke uži raspon može pomoći čitanju, uz
jasno vidljiv početak i ljestvicu osi.

Za sljedeći prikaz vraćamo se DigiKatovoj tablici internetskih domena. Svaki
redak sadrži ukupan broj objava jedne domene u odabranom korpusu. Tablica ima
`r hr_broj(s5_izvori_sazetak$izvora, 0)` domene i `r hr_broj(s5_izvori_sazetak$objava, 0)` objava (Šikić, 2026). Medijan je `r hr_broj(s5_izvori_sazetak$medijan, 0)` objave po domeni, a najveći broj `r hr_broj(s5_izvori_sazetak$najvise, 0)`. Na linearnoj bi osi većina domena bila
stisnuta uz početak. Logaritamska os omogućuje da se bolje
vide i manje vrijednosti jer jednak prostor dodjeljuje jednakim omjerima.

*Slika. Raspodjela broja objava među 3 604 imenovane domene na logaritamskoj osi. Izrada autora prema DigiKatu [@digikat2026].*

Na logaritamskoj osi pomak od 10 do 100 jednak je pomaku od 100 do 1.000.
Uspoređujemo omjere, dok apsolutne razlike nisu jednako velike. Promjena osi
ne mijenja zapise, ali mijenja vizualni oblik raspodjele, pa je treba
označiti. I dalje opisujemo samo domene u ovom korpusu, bez zaključivanja o
svim hrvatskim medijima, korisnicima ili pojedinačnim objavama.

## Mala višestruka polja

Kada je na grafu mnogo skupina, linije se mogu preklapati i tražiti stalno
provjeravanje legende. Tada isti oblik grafa možemo ponoviti u zasebnom polju
za svaku skupinu.

**Mala višestruka polja** (*small multiples*) niz su prikaza istoga oblika i
iste ljestvice, po jedan za svaku skupinu, tako da se razlike među skupinama
očitavaju usporedbom položaja između polja.

Za usporedbu razina polja trebaju zajedničku ljestvicu. Ako svako ima svoj
raspon, male i velike razlike mogu izgledati jednako. Različite osi mogu biti
prikladne za usporedbu oblika, ali tu odluku treba jasno navesti.

U DigiKatovu mjesečnom izvatku za 2024. nedostaju retci od veljače do svibnja.
Siječanj je djelomičan, a lipanj donosi promjenu metode i obuhvata
(Šikić, 2026). Prazninu ne pretvaramo u nule niti linijom spajamo siječanj i
lipanj. U tablici zadržavamo svih 12 mjeseci kako bi nedostajanje bilo
vidljivo.

*Slika. Broj objava i udio weba u mjesečnom zbroju platformskoga izvatka za 2024. Duga crta označuje mjesec bez retka, ne nulu. Izrada autora prema DigiKatu [@digikat2026].*

Brojem objava opisujemo mjesečnu količinu, a udjelom weba njezin sastav.
Nazivnik u mjesečnoj tablici zbroj je svih platformi
tog mjeseca. Ne koristimo 551.712 iz datoteke domena jer ona ima drugu
jedinicu i nema zajednički ključ. U [malim višestrukim
poljima](#fig-mala-polja) prikazujemo broj objava za četiri platforme s
najviše objava u dostupnim mjesecima 2024. i za objedinjeni ostatak. Sva polja
imaju istu logaritamsku os.

*Slika. Mjesečni broj objava za četiri platforme s najvećim zbrojem u dostupnim mjesecima 2024. i objedinjene ostale platforme. Praznina od veljače do svibnja znači da nema redaka; isprekidana crta i odvojene točke u lipnju označuju lom metode. Zajednička okomita os je logaritamska. Izrada autora prema DigiKatu [@digikat2026].*

Linije ostavljaju četveromjesečnu prazninu, a lipanjska točka odvojena je od
kasnijeg niza. Zbog nepotpunog siječnja i promjene metode ne zaključujemo o
trendu, rastu ili učinku promjene nakon lipnja. Možemo usporediti dostupne
brojeve uz vidljiva ograničenja zapisa.

## Graf pred čitateljem

Zajednička ljestvica omogućuje usporedbu samo ako čitatelj može razaznati
oznake i njihov smisao. Pri izradi grafa zato treba predvidjeti crno-bijeli tisak, čitače zaslona i
različite sposobnosti razlikovanja boja.

Razliku među skupinama zato uz boju označujemo oblikom točke, vrstom linije
ili izravnim nazivom. Tako značenje ostaje čitljivo i bez boje. Paleta knjige
koristi i razlike u svjetlini kako bi se kategorije mogle razlikovati u sivim
tonovima.

Alternativni tekst treba prenijeti nalaz osobi koja ne vidi graf. Navodimo
varijable, smjer veze i najizraženije obilježje obrasca. Opis da graf
prikazuje odnos dviju varijabli nije dovoljan jer ne govori kakav je taj
odnos.

Pristupačnost prikaza znači da podatke može pročitati i osoba kojoj boja ili sitan tekst nisu dostupni. Izravnim oznakama uz podatke smanjujemo potrebu za traženjem naziva u legendi.
Pomaže i smislen redoslijed kategorija. Kada želimo usporediti veličine,
poredak po vrijednosti olakšava čitanje više od abecednog.

Iste odluke provjeravamo i pri čitanju grafa. Primijenimo ih na desno polje u slika

Jedan stupac predstavlja dobnu skupinu. Ne prikazuje pojedinog ispitanika, pa
iz njega ne zaključujemo o pojedincu. Skupina određuje vodoravni položaj, a
prosjek duljinu stupca. Boja i širina su jednake jer ne prikazuju dodatnu
varijablu.

Prije crtanja izračunat je prosjek svake skupine, čime je skriven oblik
raspodjele i njezin dugi desni rep. Stupac od `r hr_broj(s5_najmladi$prosjek, 1)` minuta prikazuje
prosjek, dok medijan iste skupine iznosi `r hr_broj(s5_najmladi$medijan, 1)` minuta. Os uz to ne počinje
od nule, što je u nastavnom primjeru označeno.

 Prosjek skriva raspodjelu, a skraćena os
prikazuje neprimjerene odnose duljina. Brojevi su točni, ali graf može navesti
na pretjeran dojam razlike i pogrešno shvaćanje tipičnog ispitanika. Oznaka
zahvata omogućuje da problem uočimo, ali ga ne uklanja.

Histogram grupira brojčane vrijednosti u razrede. Visina stupca ovdje
broji opažanja u razredu jednake širine, a drukčija širina razreda može
promijeniti dojam o obliku. Krivulja gustoće zaglađuje raspodjelu, pa njezina
visina nije broj osoba. Kutijasti prikaz čuva medijan i srednjih 50 %
opažanja između prvoga i trećega kvartila. U sljedećem prikazu brkovi sežu
do najudaljenijih opažanja unutar 1,5 interkvartilnog raspona od kutije;
udaljenija opažanja prikazuju se zasebno. Takva točka nije automatski pogreška.

Sažimanje u dvije sredine skriva razlike među pojedincima. To nije isto što
i nesigurnost procjene populacijske sredine. Za nju trebamo znati kako su
opažanja odabrana, što ćemo razraditi uz uzorkovanje i procjenu.

## Interakcija — Isti podaci, četiri grafa

Za ovu ilustraciju stvaramo zaseban skup od 72 opažanja, po 36 u dvjema
skupinama. U svakoj ravnomjerno rasporedimo vrijednosti $x$ od 1 do 10.
Polazište ishoda je $1,5 + 0,55x$, skupini B dodajemo 0,8, a svakoj točki
neovisno normalno odstupanje sa sredinom nula i standardnom devijacijom
0,85. Na primjer, pri $x=1$ polazište je 2,05 za A i 2,85 za B, prije
slučajnog odstupanja. Varijable nemaju stvarnu mjernu jedinicu. Četiri grafa
preoblikuju istih 72 zapisa i ne generiraju nove ishode.

Isti simulirani podaci prikazani su na četiri načina. Svaki graf
olakšava jednu usporedbu i skriva dio drugih informacija. Raspršeni
dijagram čuva odnos dviju varijabli, dok prikaz sredina sažima razliku
među skupinama. Izbor ovisi o pitanju na koje želimo odgovoriti.

*Slika. Isti simulirani podaci prikazani odabranom geometrijom. Izbor prikaza mijenja vidljivu usporedbu, ne opažanja.*

**Što isprobati.**

1. Odaberite raspršeni dijagram i opišite odnos varijabli bez sažimanja po skupinama.
2. Prijeđite na histogram i utvrdite koja je prethodna informacija nestala.
3. Usporedite raspodjelu po skupinama s prikazom njihovih sredina.
4. Odaberite graf za tvrdnju o razlikama među tipičnim ishodima i obrazložite izbor.

**Statistika u divljini.**
**Kružni dijagram pred konkretnim zadatkom.** Pretpostavimo da kulturna
ustanova priprema prikaz posjećenosti svojih programa. Treba pokazati
koji programi okupljaju sličan udio publike, a koji se jasno izdvajaju.
Netko predlaže kružni dijagram jer svaki program zauzima dio ukupne
posjećenosti. Drugi ga odbacuje pozivajući se na pravilo da se takvi
grafovi nikada ne koriste. Prije izbora valja razjasniti što čitatelj
treba moći usporediti.

Cleveland i McGill istraživali su upravo točnost očitavanja grafičkih
prikaza. U njihovim su pokusima sudionici procjenjivali omjer dviju
istaknutih vrijednosti. Položaj na zajedničkoj osi omogućavao je
preciznije usporedbe od kuta (Cleveland, 1984). Nalaz daje razlog za
izbor prikaza, ali taj je razlog vezan uz određeni zadatak.

U našem zamišljenom izvještaju osobito nas zanimaju programi s bliskim
udjelima. Na kružnici bismo uspoređivali slične kutove u različitim
položajima. Na poredanim stupcima s istom početnom osi možemo usporediti
njihove završetke, a uz oznake pročitati i točne udjele. Takav izbor
olakšava upravo usporedbu zbog koje pripremamo izvještaj. Iz samoga
grafa ipak ne saznajemo zašto neki program privlači više ljudi ni
zaslužuje li zato više sredstava.

Kad bi nam namjera bila samo pokazati da jedan program zauzima približno
polovinu cjeline, zahtjev za preciznošću bio bi drukčiji. Clevelandov
i McGillov pokus ne predstavlja ispitivanje svake moguće uporabe,
pamćenja ili razumijevanja grafa u stvarnom izvještaju
(Cleveland, 1984). Zato iz njega ne izvodimo zabranu koja bi zamijenila
prosudbu o publici i svrsi prikaza.

Ustanova može izabrati stupce i objasniti zašto ih bira. Pritom treba
imenovati broji li posjete ili različite posjetitelje, jer dobar oblik
grafa ne popravlja nejasnu jedinicu. Prikladan graf prepoznajemo po
usporedbi koju čini čitljivom, a ne po tome pripada li unaprijed
odobrenoj vrsti.

**Nađite grešku.**
Za izvještaj treba usporediti udjele triju kategorija. U ovoj
konstruiranoj vježbi kategorijama A, B i C pripada 30 %, 40 % i 30 % iste
cjeline. Asistent je iz tih podataka nacrtao sljedeći prijedlog. Pregledajte
odnos između oznaka, visina i izgleda stupaca.

*Slika. Prijedlog prikaza triju udjela za urednički pregled. Konstruirana nastavna vježba, izrada autora.*

Odluka o širini vidi se i u dijelu poziva kojim je prijedlog izrađen.

> Os počinje od nule, sve kategorije imaju oznaku i vrijednosti su
> prikazane. Šira treća kategorija samo popravlja optičku ravnotežu i
> ne mijenja dojam o odnosu udjela.

Usporedite posebno A i C. Pripremite uputu osobi koja uređuje graf,
s jednom potrebnom izmjenom i dvjema odlukama koje treba zadržati.
Objasnite na kojem dijelu prikaza temeljite izmjenu. Ne trebate pisati kod.

## Razrađeni primjer

Za odgovor na pitanje iz vinjete trebamo usporedbu koja čuva pojedinačna
opažanja. Anscombeov kvartet već smo upoznali kao četiri konstruirana skupa s
gotovo jednakim sažecima (Anscombe, 1973). Sada ćemo njihove točke rasporediti u
mala višestruka polja i provjeriti što zajedničke osi otkrivaju. R-ovi ugrađeni
podaci `anscombe` reproduciraju taj objavljeni primjer.

U svakom od četiriju skupova ima 11 parova. Prva tri para iz prvih dvaju
skupova pokazuju da ista vrijednost $x$ može biti povezana s drukčijim $y$.

*Slika. Prva tri para u dvama Anscombeovim skupovima iz ugrađenoga skupa u R-u prema @anscombe1973.*

U prvom retku oba skupa imaju $x=10$, ali ishode 8,04 i 9,14.
Za sredinu prvoga skupa zbrajamo svih 11 ishoda, dobivamo
`r hr_broj(sum(anscombe$y1), 2)` i dijelimo s 11. Isti račun ponavljamo za
ostala tri skupa, a grafovima zadržavamo svaki izvorni par.

Kod u ovom primjeru koristi pakete ggplot2, dplyr i tibble, učitane u pripremi knjige. Njihova je priprema opisana u mrežnom R praktikumu. Najprije provjeravamo sažetke. Zaokružene na dvije decimale, sve četiri
sredine ishoda iznose `r hr_broj(s5_ans$sredina_y[[1]], 2)`, a standardne devijacije `r hr_broj(s5_ans$sd_y[[1]], 2)`. Iz tih se
vrijednosti razlike u obliku ne mogu prepoznati.

U prvom dijelu postupka svaki par vrijednosti dobiva vlastiti redak, kako bi u
drugome mogao postati jedna točka. Poziv `aes` određuje koja
vrijednost ide na koju os, a `geom_point` crta te točke. Da bismo usporedili
oblik podataka s njihovim linearnim sažetkom, `geom_smooth` dodaje
procijenjeni odnos, dok `facet_wrap` odvaja skupove u zasebna polja. Upisom
`p_anscombe` prikazujemo pohranjeni graf. Dodani pravci gotovo se podudaraju, kao u izvornom primjeru (Anscombe, 1973). U kasnijim je primjerima dovoljno
prepoznati koju od tih odluka pojedini naziv provodi.

Uz gotovo jednake sažetke četiriju skupova (Anscombe, 1973), graf koristi
jednake osi i gotovo podudarne pravce. Tako razlike među poljima proizlaze iz rasporeda
opažanja.

Anscombeov kvartet s gotovo jednakim sažecima i različitim oblicima. Izrada autora
prema anscombe1973.

Prvi skup približno prati pravac, a drugi zakrivljenu vezu. U trećem i
četvrtom izdvojeno opažanje snažno utječe na pravac. Brojčani sažetak zato čitamo
zajedno s oblikom podataka koje sažima.

## Sažetak

Graf počinje od usporedbe koju želimo omogućiti, pa jedinicu oznake, varijable,
prethodni račun i ljestvicu biramo zajedno. Tim izborom dio podataka
pokazujemo, a dio sažimamo ili izostavljamo, kao što su gotovo jednaki
Anscombeovi sažeci skrivali različite oblike. Položaj i drugi vizualni kanali
ne omogućuju jednako precizno očitanje (Cleveland, 1984), pa zajedničke osi,
prikladno razdvajanje skupina i oznake uz boju pomažu da tražena usporedba
ostane čitljiva. Kada prikazujemo riječi, isto obrazloženje obuhvaća pravilo
brojanja i izbor tekstova. U poglavlju o povezanosti krenut ćemo od raspršenog
dijagrama i provjeriti koliko njegova oblika možemo sažeti jednim
koeficijentom.

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

Odaberite prikaz za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Za svaki obrazložite izbor i navedite što
izostavlja. Za jedan graf napišite alternativni tekst koji prenosi nalaz te
provjerite je li nalaz razumljiv i bez boje.

### Računski

Iz tablice skupinskih sažetaka uzmite najveći i najmanji
prosjek dnevnih minuta. Izračunajte njihovu razliku, a zatim je podijelite s
većim prosjekom i pretvorite u postotak. Usporedite dobiveni postotak s [dvama
prikazima osi](#fig-skraceni-raspon) i objasnite zašto se brojčana razlika nije
promijenila, premda se promijenio vizualni dojam. Predajte račun, postotak i
dvije rečenice prosudbe. Svi potrebni podaci nalaze se u tablici.

### Kritički

Pronađite objavljeni graf sa skraćenom osi i prosudite je li odsjecanje
opravdano. Odredite koliki bi udio visine osi zauzela razlika kada bi donja granica bila nula, a gornja ostala ista, je li
prekid vidljivo označen i mijenja li se zaključak teksta uz graf. Predajte
odlomak s presudom i s uvjetom pod kojim bi presuda bila suprotna.

### Revizija modela

Provjerite prijedlog grafa iz okvira o pogrešci. Navedite ispravne grafičke odluke i
izdvojite onu koja obmanjuje. Opišite što treba promijeniti da udio ponovno
bude prikazan samo duljinom stupca. Opis predajte bez pisanja ili popravljanja
koda.
