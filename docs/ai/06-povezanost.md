# Povezanost

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 20 min | Pogodi korelaciju | Eurostat 2025, simulirana anketa, Anscombeov kvartet | pogl. 2, 4, 5 |

**Vinjeta.**
Anscombe je 1973. objavio četiri skupa s gotovo jednakom Pearsonovom korelacijom
i međusobno različitim grafovima (Anscombe, 1973). Njegova je usporedba bila
odgovor na stvaran problem statističke analize, odnosno odluku smije li broj
zamijeniti pregled podataka.

Korelacija je bila točno izračunata. Nije pogriješila u računu, nego je sažela
samo jedan aspekt odnosa. Poteškoća je nastala kada je taj sažetak pročitan kao
potpuna slika.

Koji odnosi ostaju izvan kadra kada se povezanost svede na koeficijent?

## Zajedničko kretanje

Dvije su varijable povezane kada se njihov raspored mijenja zajedno. Pozitivna
veza znači da se veće vrijednosti jedne češće pojavljuju uz veće vrijednosti
druge. Negativna veza spaja veće vrijednosti jedne s manjima druge. Slaba
linearna veza ne znači da odnosa nema, jer zakrivljeni obrazac može imati
koeficijent blizu nule.

Simulirana anketa pruža prvi pogled na takav odnos. Raspršeni dijagram dobi i
dnevnoga vremena korištenja pokazuje silazni oblak koji je strmiji u mlađim
godinama, a zatim se izravnava. Taj oblik treba vidjeti prije nego što se svede
na jedan broj.

*Slika. Dob i dnevno vrijeme korištenja u simuliranoj anketi. Veza je dosljedno silazna, ali nije pravocrtna, pa je mjera koja traži pravac strože kažnjava.*

Do mjere se dolazi usporedbom predznaka odstupanja. Za svakog se ispitanika pita
je li iznad prosjeka u obje varijable, ispod prosjeka u obje, ili iznad u jednoj
i ispod u drugoj. U simuliranoj anketi
`anketa_mreze`, koja ima
`r s6_n` ispitanika i nije mjerenje nego nastavni skup proizveden kodom, na istu
stranu prosjeka u dobi i u dnevnim minutama odstupa
`r paste0(hr_broj(100 * s6_udio_slaganje, 0), " %")` ispitanika. Kada varijable
imaju simetrične raspodjele i neovisna odstupanja, taj bi udio bio blizu
polovine. Nesimetrične rubne raspodjele mogu ga pomaknuti i bez veze, pa udio
nije samostalna mjera. Ovdje vrijednost znatno ispod polovine pokazuje da
odstupanja redovito idu na suprotne strane, dakle da je veza negativna, ali ne
kaže koliko je jaka jer ne razlikuje jedva prijeđeni prosjek od krajnje
vrijednosti.

Odgovor na to daje umnožak. Za svakog se ispitanika pomnože njegova odstupanja
od dviju sredina, čime se veliko slaganje nagrađuje jače od malog, a neslaganje
ulazi s negativnim predznakom. Prosjek tih umnožaka po cijelom uzorku mjera je
zajedničkog kretanja.

**Kovarijanca** je prosjek umnožaka odstupanja dviju varijabli od njihovih
sredina, uz djelitelj umanjen za jedan, pa je pozitivna kada opažanja
odstupaju na istu stranu i negativna kada odstupaju na suprotne.

Zapisano simbolima, gdje $x_i$ i $y_i$ označavaju vrijednosti izmjerene kod
istog opažanja, $\bar{x}$ i $\bar{y}$ njihove sredine, a $n$ broj opažanja,
kovarijanca glasi

$$\operatorname{Cov}(x, y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}).$$

Djelitelj $n-1$ isti je onaj iz poglavlja o sažimanju podataka, a formula je
poopćenje varijance, jer varijanca nastaje kada se ista varijabla stavi na oba
mjesta.

Jedna osobina kovarijancu čini nezgodnom kao samostalan sažetak. Ona nosi
jedinice obiju varijabli pomnožene jedna s drugom. Kovarijanca dobi i dnevnih
minuta u anketi iznosi `r hr_broj(s6_kov, 1)`, a kovarijanca dobi i istog
vremena izraženog u satima `r hr_broj(s6_kov_sati, 1)`. Odnos se nije
promijenio, promijenila se jedinica, a broj se promijenio šezdeset puta.
Vrijednost kovarijance zato ne govori ništa dok se ne zna u čemu je mjereno, a
parovi s različitim jedinicama ne mogu se po njoj izravno uspoređivati.

Zajedničko kretanje ostaje bez jedinica tek nakon standardizacije.

## Od standardizacije do matrice

Rješenje je već napisano u poglavlju o sažimanju podataka. Standardizirana
vrijednost pretvara opažanje u broj standardnih devijacija od sredine i time
odbacuje jedinicu. Ako se prije množenja obje varijable standardiziraju, umnožak
više ne ovisi o tome mjeri li se vrijeme u minutama ili satima.

**Pearsonova korelacija** je prosjek umnožaka standardiziranih vrijednosti
dviju varijabli, pa mjeri smjer i jačinu njihove linearne veze na ljestvici od
$-1$ do $+1$, neovisno o mjernim jedinicama.

Uzoračku korelaciju označavamo slovom $r$, a odgovarajuću vrijednost cijele
populacije grčkim slovom $\rho$. Pravilo je isto. Uzoračka vrijednost nosi
latinicu, a populacijska grčko slovo.
Standardizirane vrijednosti dviju varijabli kod opažanja $i$ označujemo sa
$z_{x_i}$ i $z_{y_i}$, a njihove uzoračke standardne devijacije sa $s_x$ i
$s_y$. Definicija se zapisuje kao

$$r = \frac{1}{n-1} \sum_{i=1}^{n} z_{x_i} \, z_{y_i} = \frac{\operatorname{Cov}(x, y)}{s_x \, s_y},$$

Dva zapisa daju isti broj, jer dijeljenje kovarijance standardnim devijacijama
i standardiziranje prije množenja isti su postupak izveden različitim redom.

Da to nije samo tvrdnja, provjerava se izravno. Prosjek umnožaka
standardiziranih vrijednosti dobi i dnevnih minuta u anketi iznosi
`r hr_broj(s6_r_iz_z, 3)`, a ugrađeni izračun korelacije daje
`r hr_broj(s6_r, 3)`. Ista korelacija izračunata na satima umjesto minuta
iznosi `r hr_broj(s6_r_sati, 3)`, dakle nepromijenjeno, dok se kovarijanca u
istoj zamjeni pomaknula šezdeset puta. Standardizacija je učinila upravo ono
zbog čega je uvedena.

Krajnje vrijednosti ljestvice imaju geometrijsko značenje. Vrijednost $+1$ znači
da sve točke leže na jednom uzlaznom pravcu, $-1$ da leže na silaznom, a nula da
linearne veze nema. Sve između mjeri koliko se oblak približio pravcu, i to je
cijeli sadržaj koeficijenta. Ono što on ne mjeri jest nagib tog pravca, pa
korelacija od `r hr_broj(s6_r, 2)` ne govori za koliko se minuta mijenja
vrijeme korištenja po godini dobi. Taj broj daje tek regresija, i to je razlika
koju poglavlje o regresiji razrađuje.

Nakon izračuna redovito slijedi pitanje je li dobiveni broj velik. Cohen je za
društvene znanosti ponudio orijentacijske vrijednosti, po kojima se korelacija
oko 0,10 opisuje kao mala, oko 0,30 kao srednja, a oko 0,50 kao velika
(Cohen, 1988). Te se orijentacijske vrijednosti lako pretvore u univerzalnu
ljestvicu za očitavanje, iako im izvor ne daje takav status.

Uvjet stoji već kod izvora. Vrijednosti su ponuđene za polja u kojima ne postoji
bolja osnova za prosudbu i izričito ustupaju mjesto poznavanju područja
(Cohen, 1988). Isti apsolutni koeficijent zato ne nosi istu važnost u svim
istraživačkim kontekstima. Prosudba se oslanja na predmet, mjeru, posljedice i
literaturu koja proučava usporedive odnose, a ne na sam prag.

Jedna preinaka koeficijenta ipak pomaže prosudbi, jer ga stavlja na ljestvicu
koja se lakše tumači. U jednostavnom linearnom opisu kvadrirana korelacija kaže
koliki udio varijance jedne varijable odgovara linearnoj vezi s drugom. Zato
korelacija od `r hr_broj(s6_r, 2)` znači da linearna veza obuhvaća
`r paste0(hr_broj(100 * s6_r^2, 0), " %")` varijance, dok preostalih
`r paste0(hr_broj(100 * (1 - s6_r^2), 0), " %")` taj opis ne obuhvaća.
Kvadriranje je pritom nemilosrdno prema srednjim vrijednostima. Korelacija od
0,30 u takvu opisu obuhvaća devet posto varijance. Poglavlje o regresiji istu
veličinu koristi kao mjeru prilagodbe modela.

Druga polovina odgovora nema veze s veličinom. Koeficijent izračunat na uzorku
procjena je, pa nosi vlastitu nesigurnost, koja uz isti nacrt i usporedive
neovisne jedinice opada s brojem opažanja.
Korelacija od 0,40 na trideset ispitanika i ista korelacija na tri tisuće
ispitanika dva su vrlo različita nalaza, iako je broj jednak. Dio knjige o
uzorkovanju i procjeni tu nesigurnost izračunava, a do tada vrijedi da se
pouzdanost procjene ne može prosuditi bez broja opažanja uz korelaciju.

Kada se varijabli nakupi, korelacije svih parova slažu se u matricu, koja je
simetrična i na dijagonali nosi jedinice, jer je svaka varijabla savršeno
povezana sama sa sobom.

*Slika. Korelacije triju brojčanih varijabli simulirane ankete. Izrada autora.*

## Matrica, kodovi i rangovi

Matrica je ekonomična i opasna u istoj mjeri. Tri varijable daju tri para,
deset varijabli daje četrdeset pet, a pregled u kojem se traži najveći broj
prestaje biti provjera hipoteze i postaje njezino izmišljanje. Poglavlje o krizi
i obnovi pokazuje što se s takvim pretraživanjem dogodi kada mu se doda
testiranje. Ovdje je dovoljno pravilo da matrica služi za pregled, a da svaki
par koji ulazi u zaključak dobije vlastiti raspršeni dijagram.

I brojčana varijabla može nastati iz teksta. **Kodirana kategorija teksta**
ulazi u odnos zajedno s odlukom osobe koja je sastavila pravilo. U ovoj smo
autorskoj ilustraciji namjerno odabrali šest naslova iz poglavlja o
vizualizaciji i sastavili doslovno pravilo. Ono dodjeljuje jedan ako naslov
sadrži oblik `graphs`, `graphical` ili `graphics`, a nulu u ostalim slučajevima.
Pet naslova dobiva jedan, jedan nulu, a korelacija koda s godinom iznosi
`r hr_broj(s6_r_kod_godina, 2)` [Anscombe, 1973; Cleveland, 1984; Tufte, 2001;
Wilkinson, 2005; Wickham, 2016; Matejka, 2017]. Taj broj opisuje samo namjerno
odabrane dokumente i ne govori kako se znanstveni naslovi mijenjaju kroz
vrijeme.

Proširi li se pravilo tako da i `visual` znači jedan, svih šest kodova postaje
jednako i korelaciju više nije moguće izračunati [Anscombe, 1973;
Cleveland, 1984; Tufte, 2001; Wilkinson, 2005; Wickham, 2016; Matejka, 2017].
Promijenila se mjera, a ne tekstovi. Kod zato nije objektivno svojstvo autora ni
dokumenta, nego odluka s imenovanim pravilom, vlasnikom kodiranja i skupom na
koji je primijenjena. Ovdje je vlasnik odluke autor poglavlja, a ne citirani
izvori. Kod može ući u povezanost kao nula i jedan, ali koeficijent
sažima odnos prema toj odluci. Poglavlje o kategoričkim podacima vratit će
takve kodove u tablicu, a poglavlje o algoritmima pokazati što se mijenja kada
oznake proizvodi sustav.

Pearsonova korelacija mjeri koliko se oblak približio pravcu, pa je zakrivljena
veza za nju djelomično nevidljiva. Odnos u kojem jedna varijabla stalno raste s
drugom, ali sve sporije, postoji i uredan je, a linearna ga mjera prikazuje
slabijim nego što jest.

Za takve slučajeve podaci se prije računanja zamjenjuju rangovima. Najmanja
vrijednost dobiva prvi rang, sljedeća drugi, a jednake vrijednosti dijele
prosječni rang, nakon čega se na rangove primijeni isti Pearsonov izračun.
Rangiranje čuva poredak i odbacuje razmake, pa rezultat mjeri je li kretanje
dosljedno u jednom smjeru bez zahtjeva da bude pravocrtno. Tako dobiven
**Spearmanov koeficijent ranga**, koji se označava sa $r_s$, mjeri monotonu
vezu. Često se kraće naziva Spearmanovom korelacijom.

Raspršeni dijagram već je pokazao što koeficijenti tek trebaju sažeti. Oblak
pada strmo u mlađim godinama i izravnava se poslije, bez odvojene podskupine
koja bi sama nosila obrazac. Tek uz taj viđeni oblik vrijedi usporediti Pearsonovu
korelaciju od `r hr_broj(s6_r, 2)` i Spearmanovu od
`r hr_broj(s6_rs, 2)`. Njihova je razlika spojiva sa zakrivljenošću koja je na
grafu već vidljiva, ali sama ne otkriva njezin uzrok. Pearsonova korelacija dobi
s logaritmom minuta iznosi `r hr_broj(s6_r_log, 2)` i približava se
Spearmanovoj, što je dodatna provjera ovog simuliranog odnosa, a ne opće pravilo
za izbor mjere.

**Utjecajno opažanje** nije samo krajnja vrijednost, nego ono čije uključivanje
ili uklanjanje materijalno mijenja koeficijent.

Bliske Pearsonove i Spearmanove vrijednosti samo su trag koji je spojiv s
približno pravocrtnom monotonom vezom. Ne dokazuju linearnost, otpornost
rezultata ni odsutnost utjecajnih opažanja, jer isti neobičan raspored može
pomaknuti oba koeficijenta. Njihovo razilaženje također ne postavlja dijagnozu.
Može upozoriti na zakrivljenost, krajnja ili utjecajna opažanja, mnogo vezanih
rangova, miješanje podskupina ili odabir suženog raspona. Zato se najprije
pregledaju oblik, raspon, podskupine i opažanja koja odudaraju, a tek se zatim
koeficijenti koriste kao sekundarni sažeci. Sama razlika nije razlog za
automatski prijelaz na Spearmanovu mjeru.

Nijedna od dviju mjera ne može pouzdano sažeti cijelu vezu koja nije monotona.
Kada je zadovoljstvo niže i pri vrlo malom i pri vrlo velikom opterećenju, oba
koeficijenta mogu ispasti blizu nule, jer se uzlazni i silazni dio međusobno
ponište. To nije znak da odnosa nema nego znak da nijedan broj taj odnos ne
može nositi.

## Ograničenje raspona i odabir

Prvi način na koji koeficijent zavara nije pogreška računanja nego izbor onoga
tko je ušao u uzorak. U približno linearnoj vezi, uz sličnu raspršenost ishoda
duž cijelog odnosa i izravan odabir samo prema jednoj varijabli, sužavanje
njezina raspona često smanjuje apsolutnu korelaciju. Razlike koje nose signal
tada se stisnu, dok preostalo rasipanje ne mora nestati s njima.

**Ograničenje raspona** (*range restriction*) nastaje kada promatrani uzorak
pokriva samo dio mogućih vrijednosti jedne ili obiju varijabli. Ono može
oslabiti izmjerenu povezanost, ali smjer promjene ovisi o obliku odnosa i
pravilu odabira.

Nema univerzalnog pravila po kojem suženje mora smanjiti koeficijent. Kod
zakrivljene veze izrez može zadržati strmiji ili ravniji dio pa korelaciju
pojačati ili oslabiti. Ako odabir ovisi o objema varijablama ili o trećoj
varijabli koja je s njima povezana, može se promijeniti i predznak. Potrebno je
zato usporediti raspršene dijagrame prije i poslije odabira te znati po kojem su
pravilu opažanja zadržana.

Simulirana anketa pokazuje zašto se to pravilo ne smije preskočiti. U cijelom
uzorku korelacija dobi i dnevnih minuta iznosi `r hr_broj(s6_r, 2)`. U
najmlađoj dobnoj skupini ostaje `r s6_n_uzak` ispitanika sa sedam zabilježenih
dobi, od 18 do 24 godine, a korelacija iznosi `r hr_broj(s6_r_uzak, 2)` i
mijenja predznak. To nije čisti prikaz istog linearnog odnosa u užem rasponu.
Generator razlikuje
dobne skupine, ali unutar najmlađe skupine minute ne ovise o točnoj dobi, pa je
populacijska korelacija unutar nje nula. Dobivena vrijednost od
`r hr_broj(s6_r_uzak, 2)` posljedica je promjenjivosti uzorka od
`r s6_n_uzak` opažanja.

Nalaz iz najmlađe skupine zato ne opovrgava vezu u cijelom simuliranom uzorku,
ali je ni ne procjenjuje oslabljenim oblikom istog koeficijenta. Odgovara na
uže pitanje o jednoj skupini čiji je odnos drukčije proizveden. Studija
provedena na studentima jedne generacije jednako tako ne može sama riješiti
pitanje o dobi kroz cijelu odraslu populaciju. Za uzorke primljenih kandidata,
zaposlenih radnika ili preživjelih poduzeća prije tumačenja treba utvrditi kako
je odabir promijenio raspon, oblik i sastav oblaka. Poglavlje o mjerenju i
dizajnu isti postupak opisuje kao pitanje o tome tko je ušao u skup.

Isti izračun pokazao je i drugi način na koji koeficijent zavara, jer je broj
različit od nule ovdje nastao iz uzorka u kojem veze nema. U ostalim jednakim
uvjetima odstupanje barem ovako veliko od nule vjerojatnije je kada je opažanja
manje, pa koeficijent bez broja opažanja uz sebe ne nosi dovoljno da bi se
prosudio. Treći je način
osjetljivost na pojedinačno opažanje, jer jedna vrijednost daleko od ostalih
pomiče oba prosjeka i obje
standardne devijacije, a s njima i sam koeficijent. Sva tri načina nose isti
simptom, dakle broj koji izgleda uvjerljivo. Otkrivaju se pregledom raspršenog
dijagrama, označenih podskupina i pravila odabira prije nego što se koeficijent
izračuna ili zapiše.

## Podskupine i obrat predznaka

Najteži slučaj nije oslabljen nego preokrenut koeficijent. On nastaje kada
uzorak sadrži podskupine koje se razlikuju po razini obiju varijabli, a
promatraju se zbirno.

Zamislimo tri odjela jedne organizacije, koji se razlikuju po tome koliko su
njihovi zaposlenici iskusni i koliko su zadovoljni poslom. Podaci koji slijede
konstruirani su za ovu svrhu i nisu mjerenje. Unutar svakog odjela zadovoljstvo
blago opada s godinama staža, dok su odjeli s iskusnijim zaposlenicima ujedno
oni s višim zadovoljstvom.

*Slika. Konstruirani podaci u kojima zbirni oblak raste, a oblak unutar svakoga od triju odjela pada. Četiri polja prikazuju iste točke bez regresijskih pravaca.*

Zbirna korelacija staža i zadovoljstva iznosi `r hr_broj(s6_r_zbirno, 2)`, dakle
jasno pozitivna. Unutar odjela ona iznosi
`r hr_broj(s6_r_odjeli$r[[1]], 2)`, `r hr_broj(s6_r_odjeli$r[[2]], 2)` i
`r hr_broj(s6_r_odjeli$r[[3]], 2)`, dakle negativna u sva tri. Nijedan broj nije
pogrešno izračunat i nijedan ne proturječi drugome, jer odgovaraju na različita
pitanja. Zbirni koeficijent mjeri i razliku među odjelima i odnos unutar njih
odjednom, a razlika među odjelima ovdje je toliko veća da određuje predznak.

Ista je pojava koju je Simpson opisao na tablicama frekvencija (Simpson, 1951), a
poglavlje o statističkom mišljenju pokazalo je na stvarnom slučaju prijamnog
postupka u Berkeleyju, gdje se zbirna razlika u stopama prijma raspala čim su
odjeli razdvojeni (Bickel, 1975). Vizualni oblik iste pojave nose mala višestruka
polja iz poglavlja o vizualizaciji. Zajedničko im je da razlika među skupinama i
odnos unutar skupina nisu ista veličina, i da ih zbirni broj spaja u jedan.

Društvene znanosti isti problem susreću i kada se skrivena podjela zamijeni
pogrešnom jedinicom analize. Korelacije se mogu računati na zemljama, županijama
ili školama, dakle na prosjecima koji su dostupni kao agregati.
Agregiranje uklanja dio razlika unutar skupina, pa korelacija među
agregatima može biti drukčija, katkad i znatno jača, od korelacije među
pojedincima, a njezin smjer ne mora vrijediti unutar tih jedinica.
Zaključak o pojedincu izveden iz veze među skupinama naziva se **ekološkom
pogreškom** (*ecological fallacy*). Ponovni izračun istih agregata ne može
opravdati tvrdnju o pojedincima; za nju su potrebni podaci i dizajn na
individualnoj razini. Tvrdnja izračunata na razini zemalja legitiman je nalaz o
zemljama, i ništa više od toga.

## Država kao jedinica

Upravljani Eurostatov izvadak omogućuje da se ta granica vidi na stvarnim
službenim agregatima. Sadrži po šest pokazatelja za svih 27 država članica EU-a
u 2025., dakle 162 ključa `država + godina + pokazatelj` i 161 brojčanu
vrijednost [{Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026]. Jedini izostali broj jest rano napuštanje obrazovanja
u Luksemburgu ({Eurostat}, 2026). Redak ostaje u datoteci kao `:`, s
izvornom oznakom `u` za nisku pouzdanost i bez oznake povjerljivosti
({Eurostat}, 2026). Nije pretvoren u nulu niti popunjen drugom godinom.

Izvorne oznake ostaju vidljive i kada ih analiza ne koristi kao filtar. One ne
znače isto što i odsutnost. Hrvatska vrijednost ranog napuštanja od 2,1 također
nosi `u`, ali jest objavljena brojčana vrijednost ({Eurostat}, 2026).
Oznaka `b` bilježi prekid u vremenskoj seriji [{Eurostat}, 2026;
{Eurostat}, 2026]. To ne pretvara ovaj jednogodišnji presjek u analizu
trenda.

*Slika. Izvorne statusne oznake u cijelom izvatku od 162 retka. Izrada autora prema šest Eurostatovih skupova za 2025. [@eurostatemployment2026; @eurostatpoverty2026; @eurostattertiary2026; @eurostatearlyleaving2026; @eurostatinternet2026; @eurostatpopulation2026].*

Za glavnu ilustraciju biramo tercijarno obrazovanje i uporabu interneta zbog
sadržajne veze obrazovnoga i digitalnoga sudjelovanja te potpunoga obuhvata
EU-27 ({Eurostat}, 2026; {Eurostat}, 2026). Odabir je istraživački
prikaz, a ne unaprijed registrirana hipoteza. Prvi je pokazatelj udio osoba od
25 do 34 godine s tercijarnim obrazovanjem, a drugi udio osoba od 16 do 74 godine
koje su se koristile internetom u prethodna tri mjeseca
({Eurostat}, 2026; {Eurostat}, 2026). Svaka točka u sljedećem
raspršenom dijagramu jest jedna
država članica, a oblik točke čuva izvornu oznaku uz treći pokazatelj, udio
stanovništva od 65 godina naviše. Tako graf prvo pokazuje zemljopisnu jedinicu,
oblik veze i kvalitetu izvora, prije nego što ih koeficijent sažme. Veličina
točke dodaje vrijednost trećeg pokazatelja, pa se pitanje dobne strukture vidi
bez prilagođavanja modela.

*Slika. Tercijarno obrazovanje i uporaba interneta u 27 država članica EU-a 2025. Veličina točke pokazuje udio stanovništva od 65 godina naviše, a oblik prenosi njegovu statusnu oznaku. Oznaka e znači procjenu, p privremenu vrijednost, a ep procijenjenu i privremenu vrijednost. Izrada autora prema Eurostatu [@eurostattertiary2026; @eurostatinternet2026; @eurostatpopulation2026].*

Pearsonova korelacija među 27 država iznosi `r hr_broj(s6_r_eu, 2)`, a
Spearmanova `r hr_broj(s6_rs_eu, 2)` [{Eurostat}, 2026;
{Eurostat}, 2026]. Njihova blizina spojiva je s uglavnom
uzlaznim oblakom, ali ne dokazuje linearnost ni otpornost rezultata. Dopuštena
rečenica glasi da su u 27 država članica EU-a u 2025. viši državni udjeli
tercijarno obrazovanih osoba od 25 do 34 godine bili povezani s višim državnim
udjelima uporabe interneta među osobama od 16 do 74 godine
({Eurostat}, 2026; {Eurostat}, 2026). Ne govori da se
obrazovanija osoba češće koristi internetom, jer datoteka nema osobe kao retke.

Veličina točaka otvara pitanje mijenja li dobna struktura čitanje te agregatne
veze [{Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026]. Graf ne dokazuje da je ona objašnjenje početnog odnosa.
Za to bi najprije trebalo pregledati oba njezina raspršena dijagrama s glavnim
varijablama i pribaviti dizajn koji razdvaja konkurentska objašnjenja.
Jednogodišnji presjek ne podupire trend, tvrdnju izvan EU-27, zaključak o
pojedincu ni uzrok [{Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026].

Odatle slijedi ono što se o uzroku smije reći. Kao moguću konfundirajuću
varijablu razmatramo prethodnu zajedničku odrednicu povezanu s objema
promatranim veličinama. Njezin se položaj određuje sadržajnim uzročnim
redoslijedom i dizajnom, a ne mjestom ili veličinom točke na grafu. Odjel je u
konstruiranom primjeru takva zajednička odrednica staža i zadovoljstva. Kada je
poznata i izmjerena, razdvajanje po njezinim razinama može pokazati kako se
povezanost mijenja, ali samo po sebi ne uspostavlja uzrok. Kada nije izmjerena,
koeficijent o njezinoj ulozi ne javlja ništa.

Zbog toga povezanost sama ne određuje uzrok. Veza između dviju varijabli može
imati barem četiri objašnjenja. Prva može djelovati na drugu, druga na prvu,
obje može oblikovati treća, ili je obrazac nastao pukom promjenjivošću uzorka.
Ista vrijednost koeficijenta spojiva je sa svakim od tih objašnjenja i ne
razlikuje ih. Razlikuje ih dizajn istraživanja, o kojem je poglavlje o mjerenju
i dizajnu već govorilo, pa je smjer tvrdnje koju o povezanosti smijemo iznijeti
određen prije nego što je izračunata.

## Interakcija — Pogodi korelaciju

Digitalna igra prikazuje četiri raspršena oblaka bez koeficijenta i traži
procjenu smjera i jačine. Tiskana inačica polazi od četiriju zadanih procjena.
U oba se puta vidljivi oblik najprije prosuđuje, a tek zatim uspoređuje s
Pearsonovom korelacijom.

*Slika. Četiri deterministički simulirana oblaka bez prikazanih koeficijenata. Zajedničke osi omogućuju usporedbu smjera i zbijenosti.*

**Što isprobati.**

1. Procijenite samo znak svake povezanosti i provjerite jesu li klizači na pravoj strani nule.
2. Usporedite oblake A i D te procijenite koji je odnos bliže savršenoj povezanosti.
3. Fino namjestite procjene za slabije oblake B i C bez mijenjanja prvih dviju.
4. Otvorite rješenje, usporedite četiri odstupanja i opišite koji je oblak bilo najteže procijeniti.

Predznak je u sva četiri oblaka lakše procijeniti od točne jačine. Usporedba
A i D dodatno pokazuje da vizualni dojam zbijenosti treba kalibrirati istom
ljestvicom, ali koeficijent ni tada ne zamjenjuje pregled oblika.

**Statistika u divljini.**
**Dinosaur s urednim sažetkom.** Matejka i Fitzmaurice razvili su postupak koji
polazi od zadanog skupa i sitnim pomacima točaka mijenja njegov oblik, a pritom
sredine, standardne devijacije i
korelaciju drži nepromijenjenima do druge decimale (Matejka, 2017). Iz istog
sažetka tako su izveli niz oblika, među njima zvijezde, križeve i obris
dinosaura.

Doseg nalaza vrijedi odmjeriti. Rad ne pokazuje da je korelacija nestabilna
niti da je pogrešno izračunata, jer je u svim tim skupovima ista i točna. Ono
što pokazuje jest da sažetak od nekoliko brojeva ne određuje skup podataka, pa
put od podataka do sažetka ide samo u jednom smjeru. Iz toga slijedi obveza koja
je uska i provjerljiva. Uz koeficijent treba prikazati i oblik iz kojeg je
nastao, a ne napustiti koeficijent.

**Pitajte model.**
Asistent može najprije opisati raspršeni dijagram, a zatim izračunati Pearsonovu
i Spearmanovu korelaciju. Treba mu zatražiti provjeru oblika, krajnjih i
utjecajnih opažanja, podskupina i ograničenja raspona prije usporedbe
koeficijenata. Nakon odgovora valja provjeriti jesu li redovi u dvjema
varijablama ispravno upareni i je li iz povezanosti izveden nedopušten uzrok.
Kod službenih agregata asistent mora imenovati državu kao jedinicu, sačuvati
odsutne vrijednosti i izvorne statusne oznake te odvojiti nalaz o državama od
tvrdnje o ljudima. Kod kodiranoga teksta mora ponoviti pravilo kodiranja i
označiti tko ga je sastavio, jer račun ne može provjeriti je li kategorija
valjano izmjerena.

Tri moguća promašaja vrijedi tražiti unaprijed. Asistent može veličinu
koeficijenta očitati s Cohenove ljestvice bez uvjeta koji uz nju ide
(Cohen, 1988). Korelacija bez broja opažanja ne dopušta prosudbu nesigurnosti.
Jezik učinka stvara treći promašaj kada jedna varijabla „dovodi do" druge, iako
je izračunato samo zajedničko kretanje.

> Najprije imenuj što predstavlja jedan redak, provjeri uparivanje, odsutne
> vrijednosti, statusne oznake i pravilo svakoga koda. Zatim opiši oblik,
> raspon, podskupine i utjecajna opažanja na raspršenom dijagramu, usporedi
> Pearsonovu i Spearmanovu korelaciju te zaključak ograniči na povezanost koju
> dizajn podupire.

**Nađite grešku.**
Na pitanje o odnosu dobi i vremena korištenja asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Korelacija u toj skupini iznosi
`r hr_broj(s6_r_uzak, 2)` uz `r s6_n_uzak` ispitanika. Zaključuje da dob i
vrijeme korištenja nisu negativno povezani u cijelom simuliranom uzorku.

## Razrađeni primjer

Dob i dnevno vrijeme korištenja društvenih mreža u simuliranoj anketi traže
izvještaj koji čuva oblik odnosa, obje mjere i granicu zaključka. Raspršeni
dijagram zato prethodi računu, a rečenica dolazi tek nakon njih.

Cjevovod i poziv `summarise` poznati su iz poglavlja o sažimanju podataka.
Funkcija `cor` računa korelaciju dvaju stupaca, po zadanom Pearsonovu, a argument
`method` mijenja mjeru u Spearmanovu. Isti obrazac čitanja koda tako ostaje
primjenjiv i kada se sažimaju dvije varijable zajedno.

Raspršeni dijagram iz odjeljka o zajedničkom kretanju pokazao je da veza pada
strmo u mlađim godinama i izravnava se poslije. Tek nakon tog pregleda dva koeficijenta
imaju smisla zajedno. Pearsonova vrijednost od `r hr_broj(s6_r, 2)` sažima
koliko je oblak blizu pravca, a Spearmanova od `r hr_broj(s6_rs, 2)` koliko je
kretanje dosljedno silazno. Njihova je razlika spojiva s već viđenom
zakrivljenošću, ali bez grafa je ne bi mogla sama dijagnosticirati.

Pošteni izvještaj glasi ovako. U ovom simuliranom uzorku od `r s6_n` ispitanika
dob i dnevno vrijeme korištenja povezani su negativno i dosljedno, uz
Spearmanovu korelaciju od `r hr_broj(s6_rs, 2)`, dok je veza na raspršenom
dijagramu zakrivljena i Pearsonova vrijednost od `r hr_broj(s6_r, 2)` manjeg
apsolutnog iznosa. Rečenica navodi mjeru, njezinu veličinu, broj opažanja i
oblik odnosa, a ne navodi uzrok, jer podaci dolaze iz prikaza bez intervencije i
vremenskoga redoslijeda.

## Od odnosa do tvrdnje

Na granici Dijela II opisati podatke nije isto što i dobiti dopuštenje za svaku
tvrdnju o njima. Šest revizijskih pitanja prati put od retka u datoteci do
rečenice koju čitatelj smije prenijeti drugome. Ovdje su primijenjena na
Eurostatov presjek.

| Pitanje revizije | Primjena na Eurostatov odnos |
|---|---|
| Što predstavlja jedan redak? | nakon spajanja pokazatelja, jednu državu članicu EU-a u 2025. |
| Tko ili što nije moglo ući u podatke? | pojedinci unutar država, zemlje izvan EU-27 i druga razdoblja nisu jedinice ovoga presjeka |
| Koja je ciljna količina i koja je vrsta tvrdnje? | Pearsonov i Spearmanov koeficijent opisuju povezanost dvaju državnih udjela |
| Koje izvore neizvjesnosti račun predstavlja, a koje ostavlja izvan? | statusne oznake čuvaju upozorenja izvora, ali koeficijenti ne kvantificiraju mjernu ni uzoračku neizvjesnost i presjek ne predstavlja promjenu kroz godine |
| Koja bi razumna alternativna odluka mogla materijalno promijeniti odgovor? | druga dobna definicija, drugi pokazatelj, rangovi umjesto vrijednosti ili unaprijed opravdan odnos prema statusnim oznakama mijenjaju pitanje i mogu promijeniti sažetak |
| Tko može snositi posljedice ako je zaključak pogrešan? | stanovnici i države mogu biti pogrešno opisani, a urednička ili javna odluka može dobiti dokaz koji podaci ne nose |

: Šest revizijskih pitanja primijenjenih na povezanost službenih agregata. Izrada autora prema Eurostatu ({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026).

Odgovori se ne provjeravaju odvojeno. Promijeni li se jedinica, mijenjaju se
ciljna količina, razumna alternativa i ljudi koji mogu snositi posljedice.
Statusna oznaka pritom nije dopuštenje za proizvoljno odbacivanje retka;
postupanje prema njoj mora biti unaprijed opravdano i vidljivo u izvještaju.

Pitanja vode do **granice tvrdnje o povezanosti**. Jedinica, obuhvat i način
mjerenja određuju čemu se koeficijent smije pripisati. Karta zatim odvaja šest
vrsta tvrdnji koje se u javnoj komunikaciji lako stapaju u jednu.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opis vrijednosti i izvornih statusnih oznaka za šest pokazatelja u EU-27 2025. |
| povezanost | odnos državnih udjela tercijarnoga obrazovanja i uporabe interneta u istom presjeku |
| generalizacija | nije poduprta izvan država, godine i dobnih obuhvata koje izvori navode |
| predviđanje | nije poduprto jer nijedno prediktivno pravilo nije izgrađeno ni provjereno na doista novim opažanjima |
| uzročnost | nije poduprta jer vremenski redoslijed i konkurentska objašnjenja nisu razdvojeni |
| odluka | poduprta je omeđena urednička odluka o poštenoj formulaciji nalaza, ali ne obrazovna ili digitalna politika |

: Šest dimenzija tvrdnje na granici Dijela II. Izrada autora prema Eurostatu ({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026).

Pošten izvještaj uz odnos navodi jedinicu, vrijeme, obuhvat i granicu. Za ovaj
presjek možemo priopćiti da su dva državna udjela u EU-27 2025. bila pozitivno
povezana ({Eurostat}, 2026; {Eurostat}, 2026). Ne možemo tu rečenicu
pretvoriti u tvrdnju o pojedincu, uzroku, budućnosti ili zemljama izvan
presjeka. Sljedeći dio knjige dodaje uzorkovanje i neizvjesnost, pa pita kada
opaženi odnos smijemo proširiti izvan podataka pred nama.

Samoprovjera na granici Dijela II obuhvaća četiri pitanja. Što predstavlja
jedna točka Eurostatova dijagrama? Zašto glavni odnos zadržava Luksemburg, a odnos koji
uključuje rano napuštanje obrazovanja ne može? Zašto se Pearsonov i Spearmanov
koeficijent čitaju tek nakon raspršenoga dijagrama? Koje tri analitičke
dimenzije tvrdnje ovaj presjek ne podupire i što bi svaka tražila?

Račun provjere mora biti čitljiv i bez otvaranja koda. Za svaku od triju
delegiranih operacija u Dijelu II bilježi što je traženo i vraćeno, što je
provjereno i kako, ulogu asistenta, ono što je ostalo neprovjereno i odgovornu
osobu. Sljedeći zapis povezuje tri zadatka s
asistentom s dokazom koji je već vidljiv u poglavljima.

| Polje računa | Sažetak u poglavlju 4 | Graf u poglavlju 5 | Povezanost u poglavlju 6 |
|---|---|---|---|
| Što je traženo | spojiti mjesečnu i godišnju DigiKatovu tablicu uz puni ključ te vratiti kontrolne brojnosti | predložiti najjednostavniji graf, obrazložiti usporedbu, navesti ljestvicu i napisati alternativni tekst | opisati raspršeni dijagram, usporediti Pearsonovu i Spearmanovu korelaciju te omeđiti zaključak |
| Što je vraćeno | broj redaka i jedinstvenih ključeva, zbroj objava i ocjena valjanosti spoja | programski zapis stupčastoga grafa, oznake vrijednosti i obrazloženje širine stupaca | jedan Pearsonov koeficijent nakon filtra, broj opažanja i zaključna rečenica |
| Što je provjereno | jedinica retka, puni ključ, broj redaka, jedinstvenost, zbroj i dostupnost metrike | geometrija, početak osi, redoslijed kategorija, nositelj skupne razlike i alternativni tekst | uparivanje, oblik, utjecajna opažanja, podskupine, raspon i jezik uzročnosti |
| Kako je provjereno | usporedbom stanja prije i nakon spajanja u tablici kontrole retka, ključa i zbroja iz poglavlja 4 te čitanjem oznake dostupnosti | usporedbom s tablicom izbora prikaza i dvama prikazima istih prosjeka na različitim osima iz poglavlja 5 te provjerom čitljivosti bez boje | čitanjem filtra, usporedbom s cijelim skupom i pregledom zakrivljenoga oblika u ranijem raspršenom dijagramu ovoga poglavlja |
| Uloga AI-ja | instrument i pogrešiv analitičar | instrument i pogrešiv analitičar | instrument i pogrešiv analitičar |
| Što je ostalo neprovjereno | valjanost istraživačkoga pitanja, značenje nedostupnih metrika i doseg izvan korpusa | konačni urednički cilj i čitljivost u svakom stvarnom formatu | populacijski doseg i uzročnost, koje podaci i dizajn ne podupiru |
| Odgovorna osoba | osoba koja potpisuje sažetak | osoba koja objavljuje graf | osoba koja potpisuje tumačenje |

: Čitljiv račun provjere za tri zadatka s asistentom u Dijelu II. Izrada autora.

## Sažetak

Kovarijanca mjeri zajedničko odstupanje od sredina, a korelacija je ista mjera
očišćena od jedinica, pa se kreće između minus jedan i plus jedan i mjeri koliko
je oblak blizu pravca. Spearmanov koeficijent radi s rangovima, pa mjeri
dosljednost smjera bez zahtjeva da veza bude pravocrtna. Slaganje i razilaženje
dvaju koeficijenata samo su tragovi koji se tumače nakon oblika, raspona,
podskupina i utjecajnih opažanja na raspršenom dijagramu. Ograničenje raspona
može oslabiti vezu u poznatim uvjetima, ali kod zakrivljenosti i odabira smjer
promjene nije zadan. Kodirana kategorija teksta ostaje mjerna odluka i nakon što
uđe u izračun, a korelacija među državama podupire tvrdnju o državama, ne o
pojedincima. Povezanost ne određuje uzrok; šest revizijskih pitanja i šest
dimenzija tvrdnje određuju što poštena rečenica smije prenijeti, a sljedeći dio
knjige uvodi vjerojatnost i pita koliko se od opaženoga obrasca može očekivati i
kad veze nema.

## Pojmovi

kovarijanca (*covariance*), korelacija (*correlation*), Pearsonova korelacija
(*Pearson correlation*), linearnost (*linearity*), oblik odnosa (*shape of a
relationship*), matrica korelacija (*correlation matrix*), kodirana kategorija
teksta (*coded text category*), Spearmanov koeficijent ranga (*Spearman rank
correlation*), monotona veza (*monotonic relationship*), utjecajno opažanje
(*influential observation*), ograničenje raspona (*range restriction*),
ekološka pogreška (*ecological fallacy*), konfundirajuća varijabla
(*confounder*), granica tvrdnje o povezanosti (*boundary of an association
claim*)

## Zadaci

### Konceptualni

Vratite se u poglavlje o sažimanju podataka i primijenite ondje uvedena pravila
o jedinici retka, ključu i odsutnoj vrijednosti na Eurostatov izvadak iz ovoga
poglavlja. Objasnite zašto glavni odnos tercijarnoga obrazovanja i uporabe
interneta zadržava Luksemburg i 27 država, zašto bi odnos koji uključuje rano
napuštanje obrazovanja imao najviše 26 potpunih parova te zašto hrvatska
vrijednost 2,1 sa statusom `u` ostaje broj, dok luksemburški zapis `:` s istim
statusom ne postaje nula [{Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026]. Predajte tablicu s tri retka, odlukom o uključivanju
i razlogom, zatim jednu poštenu rečenicu o glavnom odnosu na razini država.

### Računski

Upotrijebite tablicu korelacija triju varijabli simulirane ankete. Za svaki od
triju parova zapišite smjer Pearsonove veze. Za par dobi i minuta zatim prema
raspršenom dijagramu procijenite bi li se Spearmanova vrijednost razlikovala i u
kojem smjeru. Za preostala dva para zapišite zašto se to ne može prosuditi bez
njihovih dijagrama i što bi na njima trebalo pregledati. U digitalnom izdanju
unesite četiri procjene u interakciju i otvorite rješenje; u tisku uzmite četiri
zadane procjene i koeficijente iz tablice. Za svaki oblak
izračunajte apsolutno odstupanje procjene. Predajte tablicu sa sedam redaka i
jednom rečenicom obrazloženja u svakom. Postupak za ponavljanje izračuna nad
cijelim skupom nalazi se u praktikumu.

### Kritički

Usporedite objavljene Eurostatove tablice o tercijarnome obrazovanju i uporabi
interneta s prikazom u ovom poglavlju [{Eurostat}, 2026;
{Eurostat}, 2026]. Imenujte jedinicu analize i napišite dopuštenu rečenicu
na razini država. Zatim objasnite zašto iste tablice ne podupiru tvrdnju
„Tercijarno obrazovanje povećava individualnu uporabu interneta". Pronađite
ekološki i uzročni skok te postavite pitanje o dobnoj strukturi kao mogućem
trećem čimbeniku. Navedite kakvi bi podaci i dizajn bili potrebni za tvrdnju o
pojedincu i uzroku. Predajte odlomak s presudom i jednom poštenom zamjenom
sporne rečenice.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte što je u pozivu ispravno
izvedeno, redak koda koji mijenja ciljnu skupinu, razlog zbog kojeg dobiveni
koeficijent ne odgovara na pitanje o cijelom rasponu dobi i napišite ispravljenu
rečenicu izvještaja.
