# DIO I: STATISTIČKO MIŠLJENJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Zašto statistika

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/01-zasto-statistika.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Simpsonov paradoks | populacija_medija; Berkeley (objavljeno) | bez preduvjeta |

**Podsjetnik.** Udjeli i stope

**Vinjeta.**
Podaci o upisima na Sveučilište Kalifornije u Berkeleyju 1973. godine otvorili
su ozbiljno pitanje. Jesu li njegovi poslijediplomski programi pri upisu
diskriminirali žene (Bickel, 1975)? Zbirni podaci pokazivali su jaz u stopama
prijma koji je otvorio sumnju u postupak upisa (Bickel, 1975).

Istraživački tim zatim je iste prijave razdvojio prema odjelu. Slika se
promijenila. Žene su se češće prijavljivale na odjele na kojima je prijam bio
teži za sve kandidate, pa zbirni jaz više nije mogao služiti kao neposredna
slika odluka unutar odjela (Bickel, 1975).

Oba su prikaza nastala iz istih prijava i oba su računski točna. Jedan sugerira
veliku razliku, a drugi pokazuje da sastav prijava tu razliku snažno oblikuje.
Koju usporedbu treba čitati kada oba izračuna ostaju točna, a podupiru različite
zaključke?

## Broj nije zaključak

Berkeleyjski slučaj ne pokazuje da su podaci nepouzdani. Pokazuje nešto
zahtjevnije. Podaci ne donose zaključak bez pitanja koje im postavljamo i bez
usporedbe kojom na to pitanje odgovaramo. Zbirna stopa odgovara na pitanje tko
je češće primljen u promatranoj skupini prijava. Stope po odjelima odgovaraju na
pitanje kako su prolazili kandidati koji su se prijavili na isti odjel. Ta su
pitanja povezana, ali nisu ista.

Nijedna od tih usporedbi još ne presuđuje je li postupak upisa bio pravedan.
Za takav bi sud trebalo razmotriti kriterije, mehanizme i podatke koje tablica
ne bilježi. Ovdje pitamo uže pitanje o tome kako sastav prijava i odabrani
broj jedinica s kojim uspoređujemo rezultat mijenjaju značenje točnoga
izračuna.

**Statistika** počinje upravo na mjestu na kojem prestaje jednostavno
prebrojavanje. Njezina zadaća nije proizvesti broj, nego odrediti što taj broj
može poduprijeti. Pritom mora sačuvati vezu između pitanja, načina mjerenja,
usporedbe i zaključka. Izračun može biti besprijekoran, a tvrdnja izgrađena na
njemu ipak pogrešna jer broj odgovara na drugo pitanje od onoga koje nas
zanima.

Prije prvoga izračuna treba znati što jedan zapis predstavlja. U tablici
prijava jedan zapis opisuje skup prijava iste vrste, dok u nastavnom skupu o
medijima jedan redak opisuje jednu generiranu osobu. Broj redaka zato nije sam
po sebi broj ljudi, događaja ili neovisnih opažanja.

**Jedinica analize** je entitet o kojem se izriče zaključak, primjerice osoba,
kućanstvo, organizacija ili objava, pri čemu jedan redak tablice ne mora
automatski predstavljati jednu neovisnu jedinicu.

**Podsjetnik.** Postotci i postotni bodovi

Drugo je pitanje **nazivnik**, količina prema kojoj se brojnik pretvara u udio,
stopu ili prosjek. Tvrdnja da je 1.289 osoba spremno platiti vijesti ne može se
usporediti s brojem 3.514 dok ne znamo veličinu svake skupine. Prvi broj dolazi
iz skupine od 4.855, a drugi iz skupine od 15.101 generirane osobe
(Šikić, 2026). Bez imenovanoga nazivnika postotak nema potpuno značenje.

Treće pitanje prethodi i retku i nazivniku. **Podrijetlo podataka** govori tko
je podatke proizveo, po kojem pravilu, u kojoj inačici i s kojim ograničenjima.
Skup `populacija_medija` generiran je za nastavu uz poznato sjeme i ne opisuje
stvarne stanovnike Hrvatske (Šikić, 2026). Njime se može provjeriti račun i
uvježbati tumačenje, ali ne i iznijeti empirijska tvrdnja o hrvatskoj publici.
Podatak ne postaje prikladan za pitanje samo zato što je uredno zapisan.

Zbog toga podatke nije korisno zamišljati kao suprotnost ljudskom iskustvu.
Anegdota može otkriti problem, predložiti mehanizam ili pokazati posljedicu
koju tablica skriva. Ne može nam sama reći koliko je pojava raširena ni što bi
se dogodilo u drugim okolnostima. Podaci proširuju pogled preko pojedinačnog
slučaja, ali zauzvrat traže odluke o tome koga smo promatrali, što smo mjerili i
s čime rezultat uspoređujemo.

Pojedinačan slučaj može predložiti mogući mehanizam jer opisuje redoslijed,
okolnosti i iskustvo koje brojka izostavlja. Iskaz ispitanice o tome zašto je
prestala čitati vijesti ne utvrđuje sam taj mehanizam, ali pokazuje što bi
trebalo dodatno provjeriti. Strukturirani skup opisuje kako se pojava raspoređuje
među opaženim jedinicama. Prijelaz na širu populaciju traži još i opravdanje
načina na koji su te jedinice odabrane. Nesporazum nastaje kada iz jednoga
uvjerljivog svjedočenja izvedemo raširenost ili iz prosjeka izvedemo iskustvo
pojedinca.

Kvantitativna analiza time ne zamjenjuje poznavanje područja nego o njemu
ovisi. Odluka o tome koje su skupine usporedive, koje objašnjenje zaslužuje
provjeru i koja je razlika dovoljno velika da bi bila važna dolazi iz teorije i
iz poznavanja slučaja. Račun te odluke provodi, ali ih ne donosi.

Broj zato ne govori sam za sebe. Govori unutar postupka koji možemo pregledati,
ponoviti i osporiti. Strogost statističkog pristupa ne sastoji se u tome da
svakom dojmu suprotstavimo izračun. Sastoji se u tome da učinimo vidljivima
korake između opažanja i tvrdnje.

## Odluka koja se donosi bez dokaza

Berkeleyjski slučaj završio je u znanstvenom časopisu, ali oblik problema
svakodnevan je i izvan istraživanja. Zamislimo uredništvo portala u kojem
posjećenost pada. Urednik smatra da su naslovi predosadni i traži drukčiji
stil. Prijedlog zvuči uvjerljivo i moguće je da je točan. Jednako su moguća i
druga objašnjenja, od vremena objave i duljine tekstova do konkurentske
aplikacije koja je upravo izašla ili godišnjeg doba u kojem publika radi nešto
drugo.

Bez podataka takva se rasprava ne može razriješiti. Svaki sudionik ima svoju
teoriju, svaka teorija ima primjer koji joj ide u prilog, a odluka na kraju
pripadne osobi koja je najuvjerljivije govorila. Isti se raspored ponavlja u
ministarstvu koje procjenjuje je li mjera djelovala, u udruzi koja mjeri doseg
kampanje i u stranačkom stožeru koji tumači pomak u anketi. Statistika ne
obećava da će uvijek dati odgovor. Obećava postupak u kojem se neslaganje
premješta s uvjerljivosti govornika na provjerljivost tvrdnje.

Društvene znanosti taj zahtjev nose u vlastitoj definiciji. Sociologija,
politologija, psihologija, komunikologija i ekonomija empirijske su discipline,
pa se njihove tvrdnje moraju moći suočiti s opažanjima. Kada istraživač tvrdi
da je povjerenje u medije palo, da negativne vijesti privlače više pozornosti
ili da neki oblik sudjelovanja slabi s dohotkom, ta tvrdnja mora imati podatke
iza sebe. Podaci pak bez postupka koji ih pretvara u usporedbu ostaju zaliha
brojki koja podupire gotovo svaki zaključak.

Okolnosti su usto takve da se podacima više ne bavi samo istraživač. Mnogi
klikovi, otvorene poruke i sekunde gledanja mogu se bilježiti, a takvi zapisi
često ulaze u odluke o sadržaju, oglasima i dosegu. Tko ne razumije kako
takvi podaci nastaju i što njihovi rezultati ne pokazuju, ne može ravnopravno
sudjelovati u raspravi koju oni oblikuju. Statistička pismenost time postaje
uvjet sudjelovanja, a ne dodatna vještina.

Statističko mišljenje ne počinje formulom, nego procjenom smije li se njome
odgovoriti na postavljeno pitanje. Račun može biti besprijekoran, a zaključak
ipak pogrešan ako su uspoređene pogrešne skupine, zanemarena neizvjesnost ili
podaci ne mjere ono što tvrdnja imenuje. Zato svaku tehniku valja vezati uz
odluku koju omogućuje i granicu preko koje zaključak ne smije prijeći.

Vrijedi odmah reći i što statistika ne obećava. Ona ne pretvara nepotpune
podatke u potpune i ne nadoknađuje ono što nije izmjereno. Ne odlučuje umjesto
istraživača koja je usporedba važna, jer taj izbor pripada području o kojem se
raspravlja, a ne računu. Ne uklanja nesigurnost, nego je izražava, pa je pošten
statistički nalaz gotovo uvijek uži i oprezniji od tvrdnje koja mu prethodi.
Očekivanje da će analiza donijeti konačan sud najčešće završava razočaranjem
ili pretjeranom tvrdnjom, a knjiga na oboje pokušava odgovoriti ranije nego
kasnije.

## Životni ciklus podataka

Broj koji stigne do članka ili zaslona rezultat je niza odluka. Ova knjiga taj
niz naziva **životnim ciklusom podataka**. Ciklus ne počinje preuzetom
datotekom, nego društvenim pitanjem, a ne završava izračunom, nego praćenjem
onoga što se s rezultatom događa.

| Faza | Pitanje koje je vodi |
|---|---|
| pitanje | Koju odluku ili tvrdnju treba razjasniti? |
| pribavljanje | Odakle zapisi dolaze i tko može izostati? |
| provjera | Predstavlja li redak očekivanu jedinicu i jesu li vrijednosti moguće? |
| priprema | Koje su promjene napravljene prije analize? |
| istraživanje | Koji su obrasci, iznimke i alternativna objašnjenja vidljivi? |
| modeliranje | Koja usporedba ili model odgovara pitanju? |
| vrednovanje | Koliko je rezultat stabilan i gdje ne uspijeva? |
| komunikacija | Koju tvrdnju rezultat doista podupire? |
| praćenje | Mijenjaju li se podaci, uporaba ili posljedice nakon objave? |

Nazivi faza ne znače da se analiza uvijek kreće ravnom crtom. Provjera može
otkriti da smo pribavili pogrešne zapise, a istraživanje da pitanje treba
sužavati. Strelica se tada vraća unatrag. Važno je da povratak ostane vidljiv,
jer neobjašnjena promjena datoteke ili pitanja prekida trag od izvora do
zaključka.

Pitanje, pribavljanje i provjera određuju čiji zapis postoji, što jedna jedinica
predstavlja, koji je nazivnik i može li izvor odgovoriti na pitanje. Ni
najnapredniji model ne može naknadno popraviti nepoznato podrijetlo, duplicirane
jedinice ili mjerenje pogrešnoga pojma.

### Četiri djelatnosti i četiri pitanja

Statistika, podatkovna znanost, strojno učenje i sustavi umjetne inteligencije
zauzimaju različite uloge unutar istoga životnog ciklusa. Razlikujemo ih prema
pitanju koje upravlja njihovim radom.

| Djelatnost | Vodeće pitanje |
|---|---|
| statistika | Što ovi podaci opravdavaju vjerovati? |
| podatkovna znanost | Kako stvarni izvori podataka mogu postati pouzdana i reproducibilna analiza? |
| strojno učenje | Hoće li naučeni obrazac raditi na doista novim opažanjima? |
| sustav umjetne inteligencije | Mogu li se naučeni obrasci upotrijebiti za generiranje, preporučivanje, klasificiranje ili djelovanje u institucionalnom okruženju? |

Put od izvora do ponovljiva odgovora pripada **podatkovnoj znanosti**. Pitanje
ponašanja naučenoga obrasca na novim opažanjima pripada **strojnom učenju** i
blisko je algoritamskoj kulturi modeliranja koju je Breiman razlikovao od
modeliranja usmjerenoga na objašnjenje (Breiman, 2001). Kada se takav obrazac
ugradi u sučelje i instituciju koja proizvodi izlaze ili utječe na odluke,
nastaje **sustav umjetne inteligencije**. Njegovu procjenu tada čine tehničke
osobine modela, uporaba, pogreške i posljedice (Barocas, 2023).

Radni okvir ove knjige ne pripisuje suvremenu umjetnu inteligenciju jednoj
djelatnosti. Odvojeno prati statističko učenje, algoritme strojnoga učenja,
digitalne podatke, optimizaciju, računalnu opremu, ljudsko označivanje,
programsku infrastrukturu i sustavno vrednovanje. Podatkovna znanost organizira
mnoge korake oko modela, ali ovdje nije ni drugo ime za strojno učenje ni jedini
izvor sustava umjetne inteligencije.

Granice među djelatnostima čuvaju odgovornost. Ponovljiv podatkovni postupak ne
čini nevaljan zaključak valjanim, a visoka točnost predviđanja ne pretvara
obrazac u uzročno objašnjenje. Obratno vrijedi jednako. Dobar statistički račun
ne može spasiti nepoznato podrijetlo, ishod koji je nehotice procurio u podatke
za učenje ili transformaciju koju nitko ne može ponoviti. U ovoj knjizi te se
djelatnosti susreću, ali svaka zadržava svoje vodeće pitanje.

## Gdje intuicija popušta

Protiv takvog postupka govori jedan uporan prigovor prema kojem je formalna
provjera suvišna kada zaključak izgleda očit. Naša prosudba promjenjivosti i
vjerojatnosti ipak sustavno griješi, i to na predvidljive načine.
Ljudska sklonost prepoznavanju obrazaca izvanredno je korisna, ali radi i kada
obrasca nema.

Slučajnost brzo otkriva tu slabost. To se vidi u usporedbi dvaju nizova od 10
bacanja novčića. U prvome se pismo i glava savršeno izmjenjuju, a drugi je
neuredan i sadrži tri uzastopna pisma. Drugi može djelovati prirodnije, ali kod
poštenog novčića svaki od 1024 moguća niza jednako je vjerojatan, pa ni jedan
od njih nije manje slučajan od drugoga. Mi zapravo ne uspoređujemo niz s
vjerojatnošću nego s mentalnom slikom slučajnosti koja je previše uredna.
Stvarna je slučajnost grudasta, pa nizovi, gomilanja i naizgled značajni
obrasci nastaju i kada iza njih ne stoji nikakav uzrok.

Isti problem prelazi na pojedinačan slučaj. Ako susjed hvali novu aplikaciju za vijesti
i dvoje kolega kaže isto, dojam dokaza nastaje gotovo automatski. Troje ljudi
ipak ne opisuje populaciju, a ni njihov izbor nije slučajan, jer su za novu
aplikaciju vjerojatno posegnuli oni koji se vijestima ionako više bave.
Tversky i Kahneman opisali su sklonost da učestalost pojave procjenjujemo prema
tome koliko nam lako pada na pamet njezin primjer, što su nazvali heuristikom
dostupnosti (Tversky, 1973). Živopisan i nedavan slučaj time dobiva težinu koju
mu njegova stvarna zastupljenost ne daje.

Kod povezanosti nedostajuća usporedba postaje još manje vidljiva. Portali koji
objavljuju više tekstova imaju više ukupnih posjeta, iz čega se lako izvodi
savjet da treba objavljivati više.
Veći portali istodobno imaju više novinara, veći proračun i stariju publiku,
pa broj tekstova može biti popratna pojava, a ne uzrok. Odnos među dvjema
pojavama može nastati zato što prva utječe na drugu, zato što druga utječe na
prvu ili zato što obje ovise o nečem trećem. Tvrdnja da povezanost nije
uzročnost zvuči kao opće mjesto, ali koraci kojima se ona provjerava predmet su
poglavlja o dizajnu istraživanja i poglavlja o regresiji.

U sva tri slučaja nedostaje usporedba.
Ne znamo kako izgledaju ostali nizovi, ne znamo za one koji aplikaciju nisu
pohvalili i ne znamo što bi se dogodilo pri istom broju tekstova na portalu
druge veličine. Statistika popravlja upravo to, tako da usporedbu učini
izričitom umjesto da je prepusti dojmu.

Zbog toga ni količina podataka sama po sebi ne rješava problem. Analitika
velikog portala može bilježiti milijune interakcija, ali ako bilježi samo one
koji su došli, o onima koji nisu ne govori ništa, koliko god zapisa bilo. Veći
skup može smanjiti rasipanje oko procjene kada nastaje istim postupkom i kada
jedinice nose dovoljno neovisne informacije. Sustavan propust u tome što je
uopće promatrano ne nestaje povećanjem broja zapisa.

Prigovor da ovakav oprez vodi u nemoć ipak ne stoji. Nesigurno znanje nije isto
što i neznanje. Statistički postupak pod svojim pretpostavkama može
kvantificirati dio nesigurnosti, dok mjerenje, odabir i promjena konteksta
traže dodatnu prosudbu. Ista disciplina koja zabranjuje preširok zaključak
dopušta da uži zaključak izrečemo s razlogom.

## Signal u promjenjivom svijetu

Društvene pojave rijetko se ponavljaju na potpuno isti način. Dvije osobe
izložene istoj poruci ne moraju joj jednako vjerovati. Ista anketa provedena na
drugom uzorku neće vratiti potpuno jednake postotke. Čak se i ponašanje iste
osobe mijenja s vremenom i okolnostima. Ta promjenjivost nije kvar podataka.
Ona je razlog zbog kojeg nam statistika treba.

U takvoj promjenjivosti pokušavamo razlučiti **signal** od **šuma**. Signal je
obrazac koji nas zanima, poput razlike među skupinama ili povezanosti dviju
pojava. Šum obuhvaća ostale izvore varijacije zbog kojih opažanja ne pristaju
savršeno uz obrazac. Granica među njima nije zadana unaprijed. Ono što je šum
za jedno pitanje može postati signal za drugo.

Ako proučavamo razlikuje li se povjerenje u institucije među dobnim skupinama,
pojedinačne razlike unutar svake skupine otežavaju nam da vidimo opći obrazac.
Ako zatim pitamo zašto se ljudi iste dobi razlikuju, upravo te pojedinačne
razlike postaju predmet istraživanja. Statističko mišljenje zato ne uklanja
varijabilnost. Ono je raspoređuje prema pitanju koje pokušavamo razjasniti.

Ta pokretljiva granica objašnjava zašto se u društvenim znanostima toliko
raspravlja o tome što je u nekom nalazu zapravo objašnjeno. Ista razlika u
sudjelovanju može se pripisati dobi, obrazovanju, dohotku ili mjestu
stanovanja, ovisno o tome koje smo od tih obilježja uvrstili u usporedbu.
Nijedan od tih izbora nije pogrešan sam po sebi, ali svaki proizvodi drukčiju
podjelu na obrazac i ostatak. Zbog toga se rezultati različitih istraživanja o
istoj pojavi razilaze i onda kada su svi izračuni ispravni.

Jedno opažanje ne može razriješiti pitanje o raširenosti ili povezanosti, ma
koliko bilo uvjerljivo. Student koji se puno koristi mrežama i slabo prati
vijesti ne pokazuje da veza postoji, kao što ni student koji je iznimka ne
pokazuje da veze nema. Osoba i dalje može biti jedinica analize, ali se obrazac
procjenjuje iz odnosa među većim brojem pojedinačnih opažanja.

Broj promatranih slučajeva zato ulazi u tumačenje rezultata zajedno s načinom
njihova nastanka. Uz isti postupak prikupljanja i dovoljno neovisne jedinice,
razlika izmjerena na desetak ljudi lakše nastaje običnim rasipanjem nego ista
razlika izmjerena na tisućama. Duplicirani ili snažno povezani zapisi ne nose
istu količinu nove informacije kao neovisna opažanja.

Usporedba je pritom važnija od samog velikog ili malog broja. Pad, rast ili
razlika dobivaju značenje tek kada znamo prema čemu ih mjerimo. Ponekad je
usporedba druga skupina, ponekad ranije razdoblje, a ponekad raspon rezultata
koji bi mogli nastati običnom promjenjivošću. Kasnija poglavlja izgradit će
računske postupke za te usporedbe. Za sada je važan njihov zajednički temelj.
Tvrdnja postaje statistička tek kada jasno kaže što se s čim uspoređuje.

## Razlika koju čini postupak

Prijelaz s dojma na postupak počinje imenovanjem vrste tvrdnje. Opis govori što
je zabilježeno, povezanost uspoređuje pojave, generalizacija prenosi nalaz izvan
promatranih jedinica, predviđanje procjenjuje nova opažanja, uzročna tvrdnja
govori što bi promjena proizvela, a odluka povezuje dokaz s djelovanjem i
posljedicama. Isti broj može biti dobar opis i loš temelj za uzročnu tvrdnju.

Svaku takvu tvrdnju u knjizi prati šest pitanja za provjeru.

| Pitanje provjere | Što treba biti vidljivo |
|---|---|
| Koja je jedinica? | Što predstavlja zapis i na kojoj se razini izriče zaključak? |
| Tko ili što nedostaje? | Kako su jedinice ušle u podatke i tko je mogao izostati? |
| Koji je cilj tvrdnje? | Je li riječ o opisu, povezanosti, generalizaciji, predviđanju, uzročnosti ili odluci? |
| Gdje je neizvjesnost? | Dolazi li iz mjerenja, uzorkovanja, modela ili promjene okolnosti? |
| Koje drugo objašnjenje ostaje? | Koji bi još proces mogao proizvesti isti obrazac? |
| Tko snosi posljedice? | Tko dobiva korist, tko pogrešku i postoji li način osporavanja? |

Berkeleyjski slučaj pokazuje vrijednost toga reda pitanja. Njegova je jedinica
prijava, a ne osoba kroz cijeli obrazovni put. Bilježi povijesno određen skup
prijava, pa mu nedostaju druga razdoblja i procesi prije prijave (Bickel, 1975).
Zbirne stope opisuju ishode zabilježenih prijava. Ne procjenjuju same po sebi
motiv donositelja odluka niti posljedice različitih kriterija.

Postupak ne jamči točan zaključak. Čini tvrdnju dovoljno određenom da se može
pregledati, ponoviti i osporiti. Odgovori na šest pitanja pokazuju koja je vrsta
tvrdnje dostupna i na kojem je koraku njezina najslabija pretpostavka.

## Zbirna slika i skrivena struktura

Zbirni rezultat često izgleda kao najpotpuniji prikaz jer obuhvaća sva
opažanja. Ipak, ukupni prosjek ili stopa uvijek su mješavina rezultata
podskupina i zastupljenosti tih podskupina. Skupina koja je brojnija snažnije
povlači ukupni rezultat prema sebi. Promjena sastava stoga može promijeniti
zbirnu stopu čak i kada se ništa nije promijenilo unutar pojedinih podskupina.

U Berkeleyju su se odjeli znatno razlikovali po težini upisa, a prijave
muškaraca i žena nisu bile jednako raspoređene među njima. Žene su se češće
prijavljivale na selektivnije odjele, pa je njihova zbirna stopa snažnije
odražavala upravo te odjele. Usporedba unutar odjela uklonila je taj učinak
sastava iz neposredne usporedbe, zbog čega se obrazac vidljiv u ukupnim
podacima oslabio ili preokrenuo (Bickel, 1975).

**Simpsonov paradoks** je obrazac u kojem se smjer povezanosti u združenim
podacima promijeni ili preokrene kada se podaci razdvoje prema relevantnoj
trećoj varijabli (Simpson, 1951).

Paradoks nije u aritmetici. Svaka stopa ostaje točna. Neobičnost nastaje zato
što iste brojke opisuju različite usporedbe, a naš se zaključak promijeni kada
to napokon primijetimo.

Mehanizam se najlakše vidi u transparentnoj simulaciji u kojoj sve brojke stanu
u jednu rečenicu. Simulacija nije empirijski opis portala. Neka portal A objavi
100 videozapisa s prosječnim angažmanom
od 200 reakcija i 10 tekstova s prosjekom od 50, a portal B neka objavi 10
videozapisa s prosjekom od 220 i 100 tekstova s prosjekom od 60. Portal B je
uspješniji u obama formatima. Njegov je zbirni prosjek ipak znatno niži i
iznosi `r hr_broj(s1$b_zbirno, 0)` naprema `r hr_broj(s1$a_zbirno, 0)`
reakcija po objavi.

Razlika nastaje zato što zbirni prosjek nije prosjek dvaju formata nego prosjek
svih objava. Video kod portala A čini `r hr_broj(s1$udio_videa_a, 0)` % objava,
a kod portala B samo `r hr_broj(s1$udio_videa_b, 0)` %. Format s višim
angažmanom time u jednom zbroju sudjeluje s velikom težinom, a u drugom s
malom. Zbirna mjera tako mjeri i uspješnost i sastav proizvodnje, a čitatelj
koji vidi samo nju ne može znati koliko je koji sastojak pridonio.

Razdvajanje podataka ipak nije čarobni postupak koji uvijek otkriva konačnu
istinu. Podskupine moraju imati sadržajno opravdanje. Ako podatke dijelimo na
dovoljno mnogo proizvoljnih načina, prije ili poslije pronaći ćemo privlačan
obrazac koji nema stabilno značenje. Statistička disciplina traži da objasnimo
zašto je određena podjela važna prije nego što njezin rezultat proglasimo
odgovorom.

Ostaje pitanje kojem prikazu vjerovati kada se dva razilaze. Odgovor nije samo
aritmetički. Ovisi o tvrdnji, mjerenju, dizajnu, podrijetlu i usporedbi koju
želimo provjeriti. Za tvrdnju o odlučivanju unutar odjela usporedba mora biti
unutar odjela. Za tvrdnju o ukupnom ishodu prijava zbirna je stopa upravo ono
što treba. Brojke mogu postati dokaz tek kada su ti dijelovi međusobno
usklađeni.

Simpsonov paradoks zato nije tek neobičan trik s tablicama. On sažima razlog
postojanja statistike. Promatrani broj moramo povezati sa strukturom podataka
koja ga je proizvela, a zaključak ograničiti na usporedbu koju smo doista
napravili.

## Interakcija — Simpsonov paradoks

Interaktivni prikaz gradi transparentan primjer s dvjema skupinama i dvjema
podskupinama. Stope unutar podskupina ostaju jednake, dok klizači mijenjaju
njihovu zastupljenost u svakoj skupini. Prebacivanje pogleda pokazuje kako
različiti utezi mogu proizvesti zbirni rezultat suprotan obrascu unutar obje
podskupine.

*Slika. Zbirne stope i stope po podskupinama u konstruiranom primjeru Simpsonova paradoksa.*

**Što isprobati.**

1. Najprije usporedite samo zbirne stope i zapišite koja skupina izgleda
   uspješnije.
2. Uključite prikaz podskupina i provjerite ostaje li smjer razlike jednak.
3. Promijenite zastupljenost podskupina bez mijenjanja njihovih stopa i
   promatrajte kada se zbirni zaključak preokrene.
4. Postavite obje zastupljenosti na istu vrijednost i provjerite je li obrat
   tada uopće moguć.

Granica pojave slijedi iz sastava skupina. Dok su obje jednako raspoređene po
podskupinama, zbirna usporedba slijedi usporedbu unutar podskupina i obrata
nema. Obrat traži da se skupine razlikuju i po tome gdje su mjerene, a ne samo
po tome kako su prošle. Zbirna razlika zato uvijek sadrži dva sastojka,
uspješnost i sastav, koje bez razdvajanja podataka ne možemo razlučiti.

**Statistika u divljini.**
**Granica zbirne stope kao dokaza o pristranosti.** Zbirni obrazac u
Berkeleyjskim prijavama otvorio je sumnju u postupak upisa (Bickel, 1975).
Problem nastaje kada taj obrazac sam pretvorimo u objašnjenje odluka unutar
odjela. Ukupna stopa istodobno spaja odluke različitih odjela i različitu
raspodjelu prijava među njima.

Odgovorno čitanje zato ne odbacuje zbirnu stopu, ali od nje traži pomoćne
informacije. Potrebni su brojevi prijava i primljenih kandidata unutar svakog
odjela te objašnjenje zbog čega je odjel relevantna podjela. Tek tada vidimo
koji dio razlike nastaje unutar usporedivih skupina, a koji zbog njihova
različitog sastava.

**Pitajte model.**
Asistent može brzo usporediti brojeve i udjele, ali mu treba dati izvor, opis
jedinice i stvarne nazivnike. Nakon odgovora valja provjeriti može li se svaka
navedena vrijednost ponovno izračunati iz agregata i je li granica tvrdnje
sačuvana. Generirani skup služi provjeri računa, a ne opisu hrvatske publike
(Šikić, 2026).

> U datoteci `populacija-medija-agregat.csv` usporedi broj i udio osoba koje bi
> platile za vijesti prema primarnom izvoru. Za svaki udio prikaži brojnik i
> nazivnik. Odvoji opis generirane populacije od tvrdnji koje ti podaci ne mogu
> poduprijeti.

**Nađite grešku.**
U generiranoj populaciji tisak ima najveći udio osoba spremnih platiti za
vijesti, 1.289 od 4.855, odnosno 26,55 % (Šikić, 2026). Portal ima 3.514 takvih
osoba, više nego tisak (Šikić, 2026). Prema tome, portal ima veći udio osoba
spremnih platiti.

## Razrađeni primjer

Pitanje glasi koji primarni izvor vijesti u generiranoj populaciji ima najveći
udio osoba spremnih platiti za vijesti. Prije računanja bilježimo podrijetlo i
granicu. Skup je autorska simulacija od 50.000 osoba, a ne uzorak stvarnih ljudi
(Šikić, 2026). Jedinica analize jedna je generirana osoba. Tvrdnja će zato biti
opis te poznate generirane populacije, bez generalizacije i bez uzročnog
tumačenja.

Agregat čuva tri nužne vrijednosti za svaku skupinu. Stupac `Osobe` daje
nazivnik, stupac `Spremni platiti` brojnik, a njihov omjer udio. Tablica je
razvrstana prema udjelu, ne prema broju.

*Slika. Spremnost platiti prema primarnom izvoru vijesti u generiranoj populaciji. Izrada autora prema @sikic2026.*

Portal ima najveći broj osoba spremnih platiti, njih 3.514, jer je njegova
skupina i najveća (Šikić, 2026). Njegov udio iznosi 3.514 podijeljeno s 15.101,
odnosno 23,27 % (Šikić, 2026). Tisak ima samo 1.289 osoba spremnih platiti, ali
se taj broj dijeli s 4.855, pa udio iznosi 26,55 % (Šikić, 2026). Odgovor na
pitanje o najvećem broju zato je portal, a odgovor na pitanje o najvećem udjelu
tisak.

Šest auditnih pitanja ograničava tumačenje. Analizirani zapisi predstavljaju
generirane osobe, a ne stvarne ispitanike. Obuhvaćaju cijelu poznatu generiranu
populaciju, dok je svaka stvarna publika izvan okvira. Zato je dostupan samo
opis udjela, a ne generalizacija, uzročnost ni odluka. U svih 50.000 generiranih
zapisa nema uzorkovne neizvjesnosti (Šikić, 2026), ali ostaje neizvjesnost o
tome bi li generativno pravilo bilo korisno za neku drugu svrhu. Budući da uzrok
nije ni tvrđen, analiza ne bira među alternativnim objašnjenjima razlike.
Pogrešno čitanje ovdje ne pogađa stvarnu osobu, ali ista bi zamjena broja
udjelom u stvarnoj odluci mogla preusmjeriti resurse prema većoj skupini samo
zato što je veća.

Analiza završava užom tvrdnjom od početnoga dojma. U ovoj generiranoj populaciji
tisak ima najveći udio osoba spremnih platiti za vijesti, dok portal ima najveći
broj takvih osoba (Šikić, 2026). Razlika između tih rečenica nije stilska. U
prvoj je nazivnik broj osoba unutar svakoga izvora, a u drugoj uspoređujemo
brojnike.

## Sažetak

Kontekst određuje što broj može značiti. Podrijetlo, jedinica analize i nazivnik
povezuju izvor s usporedbom, a životni ciklus čuva taj trag do komunikacije i
posljedica. Šest pitanja za provjeru otkriva gdje se opis pretvara u jaču tvrdnju
nego što podaci nose. Simpsonov paradoks pokazuje cijenu zanemarivanja te veze,
jer dvije točne usporedbe mogu odgovoriti na različita pitanja. Statistika,
podatkovna znanost, strojno učenje i sustavi umjetne inteligencije djeluju u
istom ciklusu, ali zadržavaju različita vodeća pitanja. Berkeleyjski slučaj
ostavlja otvorenim ono što same stope ne bilježe, pa mjerenje i istraživački
dizajn određuju sljedeći korak.

## Pojmovi

jedinica analize (*unit of analysis*), nazivnik (*denominator*), Simpsonov
paradoks (*Simpson's paradox*), životni ciklus podataka (*data lifecycle*),
statistika (*statistics*), podatkovna znanost (*data science*), strojno učenje
(*machine learning*), sustav umjetne inteligencije (*artificial intelligence
system*)

## Zadaci

### Konceptualni

Objasnite kako dvije računski točne stope mogu poduprijeti različite zaključke.
U odgovoru razlikujte zbirnu usporedbu od usporedbe unutar podskupina te
imenujte jedinicu i nazivnik svake usporedbe.

Odaberite dvije faze životnoga ciklusa podataka. Za svaku napišite jednu
pogrešku koju kasniji izračun ne može automatski popraviti. Predajte dva kratka
odlomka bez prijedloga programskoga koda.

Razvrstajte četiri zadatka prema njihovoj vodećoj djelatnosti. Zadaci su
provjera što podaci opravdavaju vjerovati, izrada ponovljiva puta od izvora do
tablice, vrednovanje predviđanja na novim opažanjima i praćenje preporučivačkog
sustava nakon uvođenja u ustanovu. Za svaki imenujte statistiku, podatkovnu
znanost, strojno učenje ili sustav umjetne inteligencije i jednom rečenicom
obrazložite izbor.

### Računski

Upotrijebite prikazanu tablicu spremnosti platiti. Za portal i tisak ručno
podijelite vrijednost `Spremni platiti` s vrijednošću `Osobe` te rezultat
pretvorite u postotak. Predajte dva razlomka, dva postotka i jednu rečenicu koja
objašnjava zašto portal ima veći broj, a tisak veći udio. Zatim usporedite tisak
s društvenim mrežama i razliku zaokružite na dvije decimale (Šikić, 2026).

U simulaciji su stope skupine A u pristupačnijoj i zahtjevnijoj podskupini 80 %
i 20 %, a stope skupine B 90 % i 30 %. Pretpostavite da obje skupine imaju po
50 % jedinica u svakoj podskupini. Izračunajte dvije zbirne stope i objasnite
zašto obrata nema. U digitalnom izdanju rezultat možete provjeriti widgetom.

### Kritički

Pronađite u medijima jednu tvrdnju koja uspoređuje dvije skupine pomoću jednoga
zbirnog broja. Primijenite svih šest pitanja za provjeru. Predajte tvrdnju,
izvor, imenovani nazivnik i po jednu rečenicu o svakom pitanju, uključujući ona
na koja objava ne daje odgovor. Završite procjenom podupire li broj opis,
povezanost, generalizaciju, predviđanje, uzročnost ili odluku.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte točne brojnike i nazivnike,
izdvojite jednu pogrešnu rečenicu i napišite njezinu ispravnu zamjenu. Zatim
objasnite zašto čak ni ispravljen odgovor ne smije biti prenesen na stvarne
stanovnike Hrvatske.

---

# Mjerenje i istraživački dizajn

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/02-mjerenje-i-dizajn.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 26 min | Prikaz konfundera | konstruirani primjeri | pogl. 1 |

**Vinjeta.**
Berkeleyjski podaci iz prethodnog poglavlja bilježili su prijave, ishode upisa,
spol kandidata i odjel. Nisu bilježili kvalitetu prijave, savjet koji je
kandidat dobio prije prijave ni način na koji su pojedini odjeli donosili
odluke (Bickel, 1975). Tablica je zato mogla pokazati raspored ishoda, ali nije
mogla izravno izmjeriti svaki postupak koji je do tih ishoda doveo.

Istraživači su se morali vratiti korak unatrag. Prije pitanja o razlici trebalo
je utvrditi što pojedini redak predstavlja, koje su usporedbe opravdane i koje
alternativne priče podaci još dopuštaju. Više računanja nije moglo nadomjestiti
ono što nije bilo izmjereno.

Kako društvenu pojavu pretvaramo u podatke, a da pritom ne zamijenimo mjeru za
pojavu koju želimo razumjeti?

## Od pojma do podatka

Društvene znanosti proučavaju pojave koje ne možemo položiti na vagu.
Povjerenje, politička otuđenost, osjećaj sigurnosti i izloženost medijima
postoje kao pojmovi prije nego što postoje kao brojke, pa se moraju prevesti u
opažanja.

**Operacionalizacija** je postupak kojim se teorijski pojam pretvara u
određeni način mjerenja, tako da se navede što će se opažati i po kojem
pravilu će se opažanju pridružiti vrijednost.

Isto teorijsko pitanje može postati jedno anketno pitanje, skup tvrdnji,
ponašajni trag ili procjena promatrača. Svaki izbor zahvaća dio pojave i
istodobno nešto izostavlja.

Isti se pojam može zahvatiti s nekoliko tvrdnji koje se potom sažimaju u jedan
rezultat. Namjera je da svaka tvrdnja pridonese zajedničkom pojmu, a da posebnost
jedne formulacije ne odredi cijelu mjeru. Takav sažetak može biti dosljedniji od
pojedine tvrdnje, ali cijena je što više ne odgovara nijednom stvarno
postavljenom pitanju. Tumačiti se mora kroz sadržaj svih tvrdnji koje su u nj
ušle.

Razlika između pojma i njegove mjere temeljna je i ne nestaje boljim
instrumentom. Povjerenje u medije mentalno je stanje. Odgovor na pitanje o tome
koliko netko vjeruje određenom izvoru na ljestvici od 1 do 10 opažanje je koje
to stanje odražava nesavršeno. Kvaliteta istraživanja ovisi upravo o veličini
tog razmaka, a rasprava o nalazu koja ga previdi zapravo raspravlja o dvjema
različitim stvarima pod istim imenom.

Posljedica je vidljiva u svakoj literaturi koja se čini proturječnom. Dva
istraživanja o utjecaju društvenih mreža na političku polarizaciju mogu doći do
suprotnih zaključaka i pritom oba biti korektno provedena, ako je jedno
polarizaciju operacionaliziralo kao razliku u stavovima među pristašama
stranaka, a drugo kao učestalost neprijateljskih izjava o protivnicima. Prva
mjera bilježi udaljenost mišljenja, druga ton javne rasprave. Kada se nalazi
razilaze, prvo pitanje nije tko je pogriješio nego jesu li mjerili isto.

Jedinica koju mjerimo naziva se opažanjem, a svojstvo koje se među opažanjima
mijenja naziva se **varijablom**. Ako 300 ljudi upitamo koliko minuta dnevno
provode na mrežama, imamo 300 opažanja jedne varijable. Ako svakome postavimo
10 pitanja, imamo 300 opažanja za svaku od 10 varijabli. Varijabla zato nije
samo stupac s urednim imenom. Ona je trag odluke o tome što će se uopće
računati kao razlika među jedinicama.

Ta odluka pada prije prikupljanja podataka i poslije se ne može potpuno
popraviti. Ispitanik koji je odgovarao na ljestvici s pet stupnjeva ne može
naknadno biti smješten na ljestvicu s deset. Anketa koja nije pitala za mjesto
stanovanja ne može naknadno razlikovati grad i selo. Analiza radi samo s onim
što je mjerenje propustilo kroz sebe.

Zbog toga se pri čitanju tuđeg istraživanja prije ijednog rezultata valja
zapitati kako je ključni pojam izmjeren, koja je jedinica analize i što je
mjerenje moralo izostaviti. Način mjerenja važniji je od samog naziva, a ista
riječ može označavati osobu, objavu, sat gledanja ili kućanstvo. Odgovori se
traže u metodološkom odjeljku jer određuju kako valja čitati ostatak rada.

Anketno pitanje pritom nije neutralan prozor prema stavu nego dio mjernog
instrumenta. Formulacija određuje što ispitanik razumije, ponuđeni odgovori
određuju što uopće može reći, a redoslijed pitanja može promijeniti okvir u
kojem odgovara. U zamišljenom primjeru ispitanik koji je upravo odgovarao na niz
pitanja o nesigurnosti mogao bi drukčije ocijeniti povjerenje u institucije od
onoga kojemu je isto pitanje postavljeno prvo. To nije razlog za odbacivanje
anketa, nego za čitanje rezultata zajedno s upitnikom.

## Prihvatljivost, isključenja i filtri

Prije analitičke tablice postoji odluka o tome tko ili što u nju uopće može
ući. **Prihvatljivost** je pravilo koje određuje pripada li jedinica ciljanoj
skupini slučajeva, a isključenje je zabilježen razlog zbog kojeg se inače
prihvatljiva jedinica ne analizira. Filtar je postupak kojim se ta pravila
provode nad zapisima. Ta tri koraka nisu naknadno čišćenje podataka. Oni
određuju populaciju o kojoj će završna rečenica moći govoriti.

Najprije zato treba odvojiti jedinicu koja je opažena od jedinice o kojoj se
zaključuje. Jedna osoba može dati više odgovora, jedna objava može sadržavati
više izjava, a jedno kućanstvo može imati nekoliko članova. Pet redaka iste
osobe nisu pet osoba. Ako se pitanje odnosi na ljude, a tablica broji njihove
pojedinačne odgovore, prijelaz od retka do osobe mora biti izrečen prije
računanja. Poglavlje o sažimanju podataka pokazat će kako se od izvornih zapisa
konstruira analitička tablica; ovdje se postavlja ugovor prema kojem nijedan
redak u toj tablici ne nastaje bez imenovane jedinice i pravila ulaska.

Zamislimo konstruirani nacrt o načinu na koji televizijske vijesti opisuju
prosvjed. Nacrt ne daje empirijski nalaz, nego pokazuje red odluka. Jedinica
može biti prilog, govorni iskaz ili pojedina riječ, a svaki izbor odgovara na
drugo pitanje. Pravilo prihvatljivosti može obuhvatiti sve priloge u odabranim
informativnim emisijama tijekom unaprijed određenog razdoblja. Ako se zatim
isključe reprize, prilozi bez govora ili zapisi loše kvalitete, treba navesti
koliko je jedinica uklonjeno i zbog čega. Zaključak se više ne odnosi na sve
priloge iz početnog okvira, nego na užu skupinu koja je preživjela ta pravila.

Nedostajanje nije isto što i isključenje. Prihvatljiva osoba koja nije
odgovorila na jedno pitanje i dalje pripada istraživanju, ali za tu varijablu
nema opaženu vrijednost. Brisanje cijeloga retka pretvara nedostajanje u novi
filtar i može promijeniti analitički skup i doseg zaključka, osobito ako je
nedostajanje povezano s iskustvom koje se ispituje. Pošten trag zato razlikuje jedinice
koje nisu mogle ući, one koje su opravdano isključene i one koje su ušle, ali
im dio vrijednosti nedostaje.

I jezik postaje podatak tek nakon mjernog pravila. **Kodiranje kao mjerenje**
određuje koja će izjava dobiti koju oznaku, koje se pojave ne kodiraju i kako
se postupa s dvosmislenim slučajem. U konstruiranom nacrtu izraz se može
označiti kao pripisivanje odgovornosti samo ako izričito imenuje aktera i
radnju. Izjava koja odgovornost tek naslućuje može dobiti oznaku nejasno,
umjesto da je koder prisilno svrsta. Ako se svi nejasni iskazi isključe,
dobiveni udio opisuje samo jednoznačne iskaze, a ne sav jezik u prilozima.

Slaganje dvaju kodera tada je pitanje dosljednosti, odnosno pouzdanosti, dok
pitanje zahvaća li pravilo doista pripisivanje odgovornosti ostaje pitanje
pogođenosti cilja, odnosno valjanosti. Dvosmislenost nije smetnja koju treba
nevidljivo ukloniti, nego podatak o granici instrumenta.
Isto vrijedi za etička isključenja. Zaštita sudionika može opravdano suziti
pristup osjetljivim zapisima, ali metodološki izvještaj mora navesti što je
zaštićeno, tko je zbog toga izostao i kako se promijenio doseg tvrdnje.

## Razine mjerenja

Brojevi u podacima ne znače uvijek isto. Stevens je 1946. godine predložio
podjelu na četiri razine mjerenja (Stevens, 1946). Ona opisuje jesu li vrijednosti
samo oznake, nose li poredak, jesu li razmaci usporedivi i ima li nula
sadržajno značenje. Ne čini, međutim, potpunu ni bezvremensku tablicu dopuštenih
analiza.

Vrijednosti koje samo imenuju kategorije bez poretka nalaze se na **nominalnoj
razini**; tu pripadaju vrsta medija, država prebivališta, stranačka bliskost i
status zaposlenosti. Kada oznake dobiju poredak, ali ne i zajamčeno jednake
razmake, riječ je o **ordinalnoj razini**. Jednaki razmaci obilježavaju
**intervalnu razinu**, čije je ishodište proizvoljno, dok **omjerna razina**
dodaje apsolutnu nulu i time dopušta smislenu usporedbu omjera. Zato prosjek
nema smisla za vrstu medija, medijan je opravdan za uređene odgovore, a izjava
o dvostruko većoj vrijednosti pripada omjernim varijablama poput vremena, broja
dijeljenja i dohotka.

Ljestvica slaganja ordinalna je, a njezino zbrajanje ili prosječenje uvodi
pretpostavku da se razlike među stupnjevima mogu čitati brojčano. Spajanje više
tvrdnji može dati dosljedniji rezultat, ali samo po sebi ne stvara jednake
razmake. Kada brojčana odluka mijenja zaključak, vrijedi je usporediti s prikazom
koji poštuje samo poredak. Razlika od dvije desetine boda zato nije gola
činjenica nego rezultat zajedno s pretpostavkom o ljestvici.

Uz razinu mjerenja ide i razlika između diskretnih i kontinuiranih varijabli.
Diskretna varijabla poprima odvojene vrijednosti, poput broja komentara, koji
ne može iznositi tri i pol. Kontinuirana može poprimiti bilo koju vrijednost
unutar raspona, poput vremena na stranici. Razlika utječe na izbor grafičkog
prikaza i na izbor postupka, a u praksi diskretne varijable s velikim rasponom
tretiramo kao kontinuirane. Broj bodova na testu tehnički je diskretan, ali su
susjedne vrijednosti toliko blizu da ga ništa ne priječi da se ponaša
kontinuirano.

Praktična važnost svega toga leži u jednom svojstvu razina. Kretanje prema
nižoj razini uvijek je moguće, a prema višoj nikada. Iz zabilježene dobi u
godinama možemo napraviti dobne skupine kad god poželimo, dok iz zabilježenih
skupina ne možemo vratiti godine. Iz izmjerenih minuta možemo izvesti podjelu
na česte i rijetke korisnike, dok iz te podjele ne možemo izvesti minute.
Anketa koja odmah nudi razrede umjesto broja trajno oduzima analizi mogućnosti.

Iz toga slijedi savjet koji vrijedi za svako prikupljanje podataka. Mjeru valja
planirati unaprijed i sačuvati onoliko pojedinosti koliko istraživačko pitanje
traži, jer se izgubljene minute, godine ili izvorni odgovori ne mogu vratiti iz
naknadno stvorenih kategorija. Analitički se postupak ipak ne bira mehanički iz
naziva razine. Ovisi i o pitanju, dizajnu, raspodjeli podataka, načinu izgradnje
ljestvice te pretpostavkama postupka. Stevensove razine zato su koristan prvi
opis varijable i upozorenje za tumačenje, a ne konačna dozvola ili zabrana za
pojedini račun.

## Pouzdanost i valjanost

Dobra mjera mora zadovoljiti dva odvojena zahtjeva koja se lako brkaju. Prvi je
postojanost. Vaga koja pri tri uzastopna vaganja pokaže tri različite težine
beskorisna je iako mjeri pravu veličinu.

**Pouzdanost** je stupanj u kojem instrument daje dosljedne rezultate pri
ponovljenom mjerenju istog stanja u istim uvjetima.

Tri provjere ilustriraju različita značenja dosljednosti. Ponovljeno mjerenje
uspoređuje rezultate istog instrumenta u dva trenutka, uz pretpostavku da se u
međuvremenu nije promijenilo ono što se mjeri. Slaganje među procjenjivačima
važno je kada ljudi kodiraju građu, pa dva kodera koja isti tekst ocijene
različito otkrivaju problem instrumenta, a ne razliku u građi. Interna
konzistentnost pita slažu li se čestice višestavčane ljestvice koja bi trebala
zahvaćati jedan pojam. Za nju se može navesti Cronbachov alfa, a za slaganje
među koderima Cohenova kappa ili Krippendorffova alfa. Granice koje se navode
kao prihvatljive samo su konvencije o kojima se raspravlja, pa ih ne treba
čitati kao prag položenog ispita.

Iz toga slijedi konkretna provjera. Rad koji se oslanja na višestavčanu
ljestvicu čije bi stavke trebale odražavati isti pojam trebao bi navesti mjeru
interne konzistentnosti, a rad koji kodira sadržaj mjeru slaganja među koderima
i broj jedinica na kojima je izračunata. Za indeks sastavljen od namjerno
različitih sastavnica prikladna provjera može biti drukčija. Izostanak potrebnih
podataka ne dokazuje da je mjerenje loše, ali uklanja važnu mogućnost vanjske
provjere i razlog je za oprez pri tumačenju.

Kod ponovljenog mjerenja krije se važna zamka. Stavovi se mogu promijeniti, pa
razlika između dva termina može
značiti da instrument nije pouzdan ili da se svijet u međuvremenu promijenio.
Ako se između dvaju mjerenja povjerenja u medije dogodio velik skandal, pad
rezultata nalaz je, a ne pogreška. Razlikovanje nestabilnosti instrumenta od
stvarne promjene predmeta ne rješava se računom nego poznavanjem razdoblja.

Drugi zahtjev odnosi se na sadržaj, a ne na postojanost.

**Valjanost** je stupanj u kojem instrument mjeri upravo onaj pojam o kojem
se namjerava zaključivati, a ne neki drugi s kojim je povezan.

Ta se dva svojstva mogu mijenjati neovisno jedno o drugome, što je najlakše
vidjeti na primjeru mjere koja ima jedno bez drugoga. Kvaliteta novinarstva mjerena
brojem zareza u tekstu bila bi izvrsno pouzdana, jer bi svaka dva brojača došla
do istog rezultata, i posve nevaljana. Pouzdanost je nužan uvjet, a ne dovoljan,
i pouzdana mjera može svaki put jednako promašiti cilj.

Nepouzdanost pritom ne ostaje tehnička sitnica nego ulazi u same rezultate. Ako
dvije mjere uz stvarnu vrijednost bilježe približno neovisnu slučajnu pogrešku
koja ne ovisi o skupini ni ishodu, opažena veza može izgledati slabijom od veze
među samim pojmovima. U tom ograničenom slučaju šum može prikriti obrazac.

Smjer pogreške ipak nije opće pravilo. Sustavna, korelirana ili različita
pogreška među skupinama može vezu oslabiti, pojačati, stvoriti ili preokrenuti.
Zato nepouzdana mjera čini i prisutnost i odsutnost veze manje sigurnima; nalaz
koji se održao unatoč niskoj pouzdanosti nije samim time čvršći. Podatak o
pouzdanosti vrijedi tek uz pitanje kako pogreška nastaje.

Valjanost mjerenja rastavlja se na nekoliko pitanja. Pokriva li instrument sve
važne dijelove pojma, pa upitnik o medijskoj pismenosti koji ne spominje
digitalne sadržaje propušta bitan dio predmeta. Mjeri li instrument doista pojam
koji imenuje, a ne nešto susjedno, jer klikovi, vrijeme na stranici i komentari
mogu predstavljati početni interes, dubinu čitanja ili motivaciju za javno
očitovanje. Izrazi interna i eksterna valjanost koji slijede odnose se na dizajn
i doseg zaključka, a ne na svojstvo instrumenta. Reakcija na neistinitu vijest
prikazanu na praznom zaslonu, primjerice, ne mora odgovarati reakciji iste osobe
koja isti sadržaj sretne među porukama prijatelja i obavijestima.

## Treći čimbenik i logika eksperimenta

Varijable u istraživanju nisu ravnopravne. Ona za koju pretpostavljamo da
djeluje naziva se nezavisnom varijablom, a ona koja bilježi ishod zavisnom. U
opažačkim je studijama prikladnije govoriti o odnosu prediktora i ishoda jer
istraživač ničim ne manipulira i terminologija manipulacije zavarava.
Nitko ne dodjeljuje ispitanicima dob ni obrazovanje.

Varijabla povezana i s pretpostavljenim uzrokom i s ishodom može proizvesti
privid veze između njih ili prikriti vezu koja postoji.

**Konfundirajuća varijabla** je zajednički uzrok koji prethodi i
pretpostavljenom uzroku i ishodu te djeluje na oboje, pa njihova opažena veza
bez njegova uzimanja u obzir ne opisuje samo odnos koji nas zanima.

Ako podaci pokažu da adolescenti koji više koriste Instagram imaju niže
samopoštovanje, moguće je da korištenje snižava samopoštovanje, da niže
samopoštovanje potiče korištenje ili da društvena izoliranost povećava oboje.

Konfundiranje je pritom samo jedno od nekoliko objašnjenja koja opažena veza
dopušta, i vrijedi ih držati odvojenima jer se različito rješavaju. Obrnuti
smjer djelovanja tvrdi da ishod djeluje na pretpostavljeni uzrok, pa bi niže
samopoštovanje vodilo većem korištenju umjesto obrnuto. Protiv njega pomaže
vremenski razmak među mjerenjima, a ne dodavanje varijabli u model. Pristranost
odabira tvrdi da je u uzorak ušla posebna skupina ljudi, pa veza vrijedi za nju,
a ne za populaciju. Protiv nje pomaže način prikupljanja podataka. Konfundiranje
u užem smislu tvrdi da postoji zajednički uzrok obiju veličina, i jedino se
protiv njega može nešto učiniti prilagodbom u analizi, i to samo ako je taj
uzrok izmjeren.

Prepoznavanje konfundera počinje sadržajnim znanjem, a ne naredbom u programu.
Vremenski redoslijed i pretpostavka o uzrocima razlikuju ga od varijabli koje
ne treba automatski uključiti u model. **Medijator** nastaje djelovanjem
pretpostavljenog uzroka i prenosi dio njegova djelovanja prema ishodu, pa
prilagodba za njega mijenja pitanje koje postavljamo. **Kolider** je zajednička
posljedica pretpostavljenog uzroka i ishoda, a odabir ili prilagodba prema njemu
može stvoriti vezu koje prije nije bilo. Program zato ne može iz same tablice
odlučiti što treba kontrolirati. Poglavlje o regresiji prilagodbu razrađuje
računski, ali odluku o njezinu sadržaju ostavlja ondje gdje je i sada.

**Randomizacija** je postupak nasumične dodjele koji u eksperimentu prekida
sustavnu vezu između obilježja jedinica prije tretmana i uvjeta koji će primiti.
Istraživač određuje vrijednost nezavisne varijable, jedinice raspoređuje
nasumično i nastoji sve
ostale postupke održati jednakima. Kad bismo dodjelu mnogo puta ponovili,
poznata i nepoznata početna obilježja bila bi u prosjeku uravnotežena među
skupinama. U jednom stvarnom pokusu slučajna neravnoteža ipak može ostati,
osobito kada je skupina mala. Nasumična dodjela zato daje ravnotežu u
očekivanju, a ne jamči ostvarenu jednakost svake skupine. Ona podupire
usporedbu dodijeljenih uvjeta. Da bismo razliku tumačili i kao učinak primljenog
tretmana, moramo provjeriti pridržavanje dodjele, jer učinak ponude ili dodjele
nije isto što i učinak primanja tretmana.

Kako to izgleda u praksi, najlakše je vidjeti na pokusu s dvjema inačicama
poruke. Isti se tekst opremi dvama naslovima, jednim suzdržanim i jednim
zaoštrenim, a čitatelji se nasumično rasporede tako da svatko vidi samo jedan.
Nakon nekog vremena uspoređuje se udio onih koji su tekst otvorili.
Manipulacijom se naslov dodjeljuje umjesto da ga čitatelj odabire, a nasumična
dodjela određuje koju će inačicu svatko vidjeti. Tekst, vrijeme objave i položaj
na stranici ostaju jednaki u obje skupine, čime se čuva kontrola nad ostalim
okolnostima.

Vrijedi razmisliti što bi se dogodilo da nasumičnosti nema. Ako bi čitatelji
sami birali koji naslov otvaraju, skupina koja bira zaoštrene naslove bila bi
sastavljena od ljudi koji su ionako skloniji takvim sadržajima. Razlika u
otvaranju tada bi mjerila i naslov i sklonost čitatelja, bez ikakva načina da
ih razdvojimo. Upravo je to razlika između pokusa i naizgled sličnog
prikupljanja podataka o tome što ljudi već rade, i ona ne ovisi o količini
podataka nego o načinu na koji su nastali.

Isti nacrt istodobno pokazuje granicu eksperimenta. Obrazovanje, odrastanje u
siromaštvu i godine provedene uz određenu platformu ne mogu se jednostavno
nasumično dodijeliti, a neke bi dodjele bile neetične. Opažačka studija tada
nije lijen nadomjestak, nego dizajn čije tvrdnje moraju poštovati način na koji
su skupine nastale.

Stupanj u kojem u to možemo biti sigurni naziva se internom valjanošću, a
prijetnje njoj su situacije u kojima se nakon dodjele pojavi neplanirana
sustavna razlika. Tretman se može preliti na drugu skupinu, vanjski događaj može
različito zahvatiti uvjete ili djelovati zajedno s tretmanom, a nejednako
osipanje može ostaviti skupine koje više nisu usporedive. Razlika može nastati i ako se ishod mjeri
drukčije ili s drukčijom pogreškom među uvjetima. Sudionici koji naslute svrhu
istraživanja mogu se ponašati u skladu s pretpostavljenim očekivanjem, pa u
ispitivanju medijske pismenosti odgovaraju kritičnije nego što doista jesu.

## Opažačke studije i ankete

U opažačkoj studiji istraživač mjeri varijable onakve kakve jesu i analizira
veze među njima. Suparnička se objašnjenja tada ne mogu razlučiti samim
podacima. Negativna veza između korištenja
mreža i političke informiranosti dopušta tri čitanja koja podaci ne razdvajaju,
jer mreže mogu smanjivati informiranost, slabije informirani mogu više
posezati za mrežama, a obrazovanje ili dob mogu oblikovati oboje. Zauzvrat
takva studija može promatrati pojavu u njezinim prirodnim okolnostima i
obuhvatiti jedinice koje laboratorij ne bi dosegnuo.

Kvazieksperiment traži više od razlike koja se prirodno pojavila. Intervencija,
prag, pravilo ili vanjski događaj bez randomizacije mora stvoriti kontrast koji
se može braniti kao vjerodostojno usporediv. Curenje podataka može poslužiti
samo ako mehanizam izloženosti nije jednostavno odraz ranijih razlika korisnika;
inače usporedba ostaje opažačka bez obzira na broj prilagođenih varijabli.
Studije slučaja i kvalitativni pristupi nalaze se izvan te usporedbe. Mogu
samostalno odgovoriti na pitanja značenja, procesa i iskustva te osporiti
kategorije koje kvantitativni nacrt uzima zdravo za gotovo; mogu i otvoriti
hipotezu koju će drugi dizajn ispitati.

Anketa dodaje još jednu razinu dizajna. Formulacija pitanja određuje što
ispitanik razumije, ponuđeni odgovori određuju što smije reći, a **okvir
uzorkovanja** određuje tko uopće može biti izabran. Velik broj odgovora ne
popravlja sustavno izostavljanje dijela populacije. Precizno mjerenje pogrešne
skupine ostaje precizno mjerenje pogrešne skupine, a poglavlje o uzorkovanju
pokazuje zašto se ta pogreška povećanjem uzorka ne smanjuje.

Uz okvir dolazi i pitanje tko je pozvan, a nije odgovorio. Neodaziv stvara
pristranost kada je vjerojatnost odgovora povezana s ishodom koji se procjenjuje,
ali sama stopa odgovora ne otkriva ni smjer ni veličinu te pristranosti.
Naknadno vaganje prema zabilježenim obilježjima može smanjiti dio problema ako
ta obilježja objašnjavaju i odaziv i ishod. Ne može popraviti razlike povezane s
odazivom koje u podacima nisu zastupljene, pa izvještaj mora pokazati tko je
pozvan, kako su težine nastale i koje pretpostavke nose.

Prije postotka ili margine pogreške vrijedi ispuniti prvu karticu za čitanje
ankete. Prazno polje nije dokaz pogreške, ali označava granicu koju čitatelj ne
može provjeriti.

| Polje | Što treba pronaći u izvještaju |
|---|---|
| okvir i pozivanje | Tko je mogao biti izabran i kojim je putem pozvan? |
| odaziv i nedostajanje | Koliko je pozvanih sudjelovalo i za koja pitanja odgovori nedostaju? |
| procjena s težinama | Koje varijable ulaze u težine, što one pretpostavljaju o odazivu i koji mogući neodaziv ostaje? |
| mjerenje | Kako pitanje točno glasi, koji su odgovori ponuđeni i kojim je redom postavljeno? |
| provedba | Kada, kojim načinom i na kojim jezicima je anketa provedena? |
| doseg | Koji dio ciljane populacije okvir, odaziv ili filtri ne pokrivaju? |
| nesigurnost | Što pripada uzoračkoj pogrešci, a što mjerenju, obuhvatu i neodazivu? |

Kartica namjerno drži uzoračku pogrešku odvojeno od ostalih izvora. Veći uzorak
može smanjiti rasipanje koje nastaje slučajnim odabirom, ali ne popravlja pitanje
koje različiti ljudi razumiju različito, okvir koji nekoga ne sadrži ni
sustavni neodaziv. Poglavlja o uzorkovanju i procjeni razradit će uzoračku
pogrešku i intervale. Do tada
je dovoljno ne dopustiti da jedna navedena margina preuzme sav teret
nesigurnosti istraživanja.

## Doseg zaključka

Čak se i dobro izveden eksperiment može prenijeti izvan okolnosti u kojima je
proveden samo uz dodatne pretpostavke. Ta se granica naziva eksternom valjanošću
i odnosi se na druge ljude, okolnosti i razdoblja. Nalaz na studentima jednog
fakulteta ne mora vrijediti za druge dobne skupine ni sredine, ponašanje u
nadziranim uvjetima može odstupati od svakodnevice, a promjene platformi, normi
i navika mogu ograničiti prijenos starijeg nalaza.

Interna i eksterna valjanost dva su odvojena pitanja koja ponekad ulaze u
napetost, ali ne čine jednu ljestvicu. Laboratorijski pokus može snažno odvojiti
uzrok od suparničkih objašnjenja, a terenski pokus istodobno zadržati nasumičnu
dodjelu i svakodnevni kontekst. Za svaki dizajn zato treba zasebno pitati što
podupire usporedivost skupina te na koje ljude, okolnosti i vrijeme nalaz može
dosegnuti. Pitanje nije koji je dizajn najbolji nego koji nosi tvrdnju koja se
postavlja.

Jedan mogući slijed kombinira razgovore koji otvaraju relevantne kategorije,
anketu koja opisuje njihovu raširenost u određenom okviru i pokus koji ispituje
smjer djelovanja za uže pitanje. To nije jedini red. Kvalitativno istraživanje
može biti dovršen odgovor na interpretivno ili procesno pitanje, a može i
pokazati da kvantitativni instrument pogrešno dijeli pojavu. Metode se povezuju
prema pitanju, bez pretpostavke da jedna mora završiti posao druge.

Prvi proračun nesigurnosti ovdje još nije broj, nego popis mjesta na kojima bi
zaključak mogao odstupati od pojave koju želi opisati. Mjerna nesigurnost pita
bi li drukčija formulacija, koder ili instrument dao drukčiju vrijednost.
Dizajnerska nesigurnost pita bi li obrnut smjer, neizmjereni zajednički uzrok,
osipanje ili prelijevanje dopustili drugu priču. Nesigurnost dosega pita koga su
okvir, prihvatljivost, isključenja i neodaziv ostavili izvan tvrdnje.

Kasniji će računi obuhvatiti dio uzorkovne i modelne nesigurnosti. Neće
automatski obuhvatiti dijelove ovoga popisa. Zato uz svaki budući interval ili
test treba pitati što je izračun kvantificirao, a što je i dalje ostalo u
dizajnu, mjerenju i izboru jedinica. Jedan uži interval ne može poništiti širi
proračun nesigurnosti.

## Interakcija — Prikaz konfundera

Prikaz pokazuje odnos dviju varijabli prije i nakon razlikovanja jedinica prema
trećoj varijabli. Opažanja ostaju ista, ali se mijenja usporedba. Pomak ishoda
povezan s trećom varijablom može zbirnu vezu preokrenuti iako je odnos unutar
obiju podskupina stabilan.

U oba pogleda izloženost i ishod znače isto. Zbirni pogled uspoređuje sva
opažanja kao jednu cjelinu, a razdvojeni uspoređuje jedinice unutar iste razine
treće varijable. Razlika među pravcima zato ne nastaje iz novih podataka, nego
iz drukčije određenog skupa usporedivih jedinica.

Sam prikaz ipak ne može dokazati da je treća varijabla zajednički uzrok.
Vremenski redoslijed i sadržajno znanje moraju opravdati tu ulogu prije analize.
Graf pokazuje što se može dogoditi kada takav čimbenik zanemarimo, a ne postupak
kojim se uzročna uloga otkriva iz tablice.

*Slika. Ista opažanja prikazana zbirno i prema trećoj varijabli u konstruiranom primjeru.*

**Što isprobati.**

1. Promatrajte početnu vezu bez treće varijable.
2. U izborniku „Pogled” odaberite „Prema trećoj varijabli” i usporedite
   smjerove veza.
3. Pomaknite klizač „Dodatni pomak ishoda pri jednakoj izloženosti” i
   pronađite slučaj u kojem se početni zaključak preokreće.
4. Postavite taj dodatni pomak na nulu i provjerite ostaje li smjer zbirne i
   unutargrupnih veza jednak.

Konfundiranje traži da treća varijabla bude povezana s objema promatranim
veličinama istodobno, a ne samo da postoji u podacima. Kada se dodatni pomak
ishoda pri jednakoj izloženosti postavi na nulu, zbirne i unutargrupne veze u
ovom primjeru imaju isti smjer, iako se njihove točne strmine još mogu
razlikovati. Popis mogućih konfundera zato nije popis svega što je izmjereno,
nego kratak popis onoga za što postoji razlog vjerovati da djeluje na obje
strane. Taj razlog dolazi iz teorije, a ne iz tablice.

**Statistika u divljini.**
**Što mjeri stopa prijma.** Zbirna stopa u Berkeleyju opisivala je ishod
prijava, ali nije sama mjerila namjeru, kriterije odlučivanja ni iskustvo
kandidata (Bickel, 1975). Pretvaranje te stope u potpunu ocjenu pravednosti
preskače operacionalizaciju pojma pravednosti. Pravednost se može
operacionalizirati kao jednak ishod među skupinama, kao jednak postupak prema
jednako kvalificiranim kandidatima ili kao jednaka dostupnost samog odjela, i
te tri mjere u ovim podacima ne daju isti odgovor.

Odgovorno čitanje zato najprije pita koja je jedinica analize i koje su
varijable dostupne. Jedinica analize ovdje je prijava, a ne osoba, pa kandidat
koji se prijavio na dva odjela ulazi dvaput. Analizirani zapisi odnosili su se
na prijave za jesenski upis 1973. koje su ostale u postupku do zabilježene
odluke, nakon povlačenja ili preusmjeravanja dijela prijava (Bickel, 1975).
Dostupne su varijable ishod, spol i odjel, dok kvaliteta prijave i savjet
primljen prije prijave nisu izmjereni. Zapisi nisu nastali istraživačkom
nasumičnom dodjelom, ali upisni postupak jest proces koji ih je proizveo i
filtrirao.

**Pitajte model.**
Asistent može pretvoriti istraživačko pitanje u nacrt varijabli i upozoriti na
moguće konfundere. Njegov popis nije dokaz da su mjere valjane. Treba provjeriti
odgovara li svaka predložena varijabla stvarnom instrumentu, tko nedostaje iz
okvira uzorkovanja, koja pravila prihvatljivosti i isključenja mijenjaju ciljnu
skupinu te dopušta li dizajn kauzalni zaključak.

Dva su moguća promašaja posebno važna za ovu provjeru. Model može ponuditi dug
i uvjerljiv popis varijabli, a ne razlikovati zajedničke uzroke od medijatora i
kolidera. Slijepa prilagodba tada može ukloniti dio odnosa koji nas zanima ili
stvoriti novu pristranost. Može i opisati opažačku studiju glagolima poput
*utječe* ili *smanjuje*. Zato svaku predloženu varijablu treba provjeriti prema
tome kada nastaje, a svaku tvrdnju o djelovanju prema dizajnu koji je nosi.

> Za ovo istraživačko pitanje predloži jedinicu analize, ciljnu skupinu, pravilo
> prihvatljivosti, jedno opravdano isključenje, način mjerenja ishoda, mogući
> konfundirajući čimbenik i dizajn. Ako se kodira jezik, napiši pravilo za jednu
> oznaku i postupak za dvosmislen slučaj. Za svaku varijablu navedi nastaje li
> prije ili poslije pretpostavljenog uzroka, a za svaku odluku što se iz
> prikupljenih podataka neće moći zaključiti.

**Nađite grešku.**
U opažačkoj anketi studenti koji dulje koriste društvene mreže prijavili su
niže povjerenje u institucije. Obje su varijable izmjerene istim upitnikom i
analiza je uključila dob. Rezultat zato dokazuje da dulje korištenje društvenih
mreža smanjuje povjerenje.

## Razrađeni primjer

Zamislimo istraživanje povjerenja u lokalne institucije. Pojam je apstraktan i
nijedna ga tvrdnja sama ne zahvaća, pa ga operacionaliziramo četirima
konstruiranim tvrdnjama na istoj ljestvici od 1 do 5.

| Oznaka | Konstruirana tvrdnja | Smjer višeg odgovora |
|---|---|---|
| t1 | Mogu se osloniti na odluke lokalnih institucija. | više povjerenja |
| t2 | Lokalne institucije postupaju pošteno prema građanima. | više povjerenja |
| t3 | Lokalne institucije objavljuju informacije kojima mogu vjerovati. | više povjerenja |
| t4 | Lokalne institucije često skrivaju važne informacije. | manje povjerenja |

Prve tri tvrdnje formulirane su potvrdno. Četvrta je niječna. Zamišljeni ju je
istraživač uvrstio kako bi pokušao prekinuti mehaničko ponavljanje odgovora, ali
takva formulacija može i zbuniti ispitanika. Ta odluka vratit će se kao problem
u računu.

Prije nego što četiri odgovora spojimo u jedan rezultat, provjeravamo ponašaju
li se doista kao mjere istog pojma. Najjednostavnija provjera uspoređuje svaku
tvrdnju sa zbrojem preostalih. Ako sve mjere isto, svaka bi se trebala kretati
u istom smjeru kao ostatak instrumenta. Dijagnostička vrijednost može biti
između −1 i 1. Pozitivan predznak znači kretanje u istom smjeru, a negativan u
suprotnom. Puni račun povezanosti dolazi u poglavlju o povezanosti.

*Slika. Povezanost svake tvrdnje s ostatkom instrumenta, prije i nakon okretanja niječne tvrdnje. Izrada autora.*

Tablica odmah pokazuje nepravilnost. Prve tri tvrdnje snažno se slažu s
ostatkom instrumenta, dok četvrta ide u suprotnom smjeru i s ostatkom je
povezana negativno, na razini od `r hr_broj(s2$t4_prije, 2)`. U ovom
konstruiranom primjeru uzrok znamo unaprijed jer smo četvrtu tvrdnju namjerno
napisali niječno i zadržali izvorno kodiranje. Visok odgovor na njoj znači
nisko povjerenje, dok ista brojka u prve tri tvrdnje znači više povjerenja.
Sama negativna povezanost u stvarnom instrumentu ne bi dokazala taj uzrok.

Popravak je jednostavan i sastoji se u okretanju ljestvice te jedne tvrdnje,
tako da od najveće moguće vrijednosti uvećane za jedan oduzmemo dani odgovor.
Nakon tog zahvata četvrta se tvrdnja slaže s ostatkom jednako kao i ostale, na
razini od `r hr_broj(s2$t4_poslije, 2)`, i sve četiri mjere idu u istu stranu.
Tek sada zbrajanje ima smisla.

*Slika. Odgovori nakon okretanja niječne tvrdnje i izvedena mjera povjerenja. Izrada autora.*

Cijena propuštenog koraka nije mala. Da smo sve četiri tvrdnje zbrojili bez
okretanja, rezultati ispitanika razlikovali bi se za najviše
`r hr_broj(s2$raspon_naivno, 2)` boda, dok se nakon ispravka razlikuju za
`r hr_broj(s2$raspon_ispravno, 2)`. Niječna tvrdnja poništavala bi ono što
ostale mjere, pa bi instrument izgledao kao da su svi ispitanici slični.
Zaključak takve analize bio bi da se povjerenje među ljudima jedva razlikuje, i
to bez ijedne pogreške u samom računu.

Nalaz iz ove dijagnostike vrijedi zapamtiti kao upozorenje, a ne kao dokaz o
jednom uzroku. Zaboravljeno obrnuto kodiranje prva je mogućnost koju treba
provjeriti. Negativna se povezanost može pojaviti i kada tvrdnja zahvaća drugu
dimenziju pojma, kada je prijevod promijenio njezino značenje, kada je
formulacija dvosmislena ili kada dio ispitanika odgovara nepažljivo. Dijagnoza
zato traži puni tekst tvrdnje, ključ kodiranja, obrasce odgovora i provjeru što
se događa nakon sadržajno opravdanog okretanja. Automatsko okretanje ili
izbacivanje bez tih provjera može samo prikriti drukčiji mjerni problem.

Postupak je pokazao da se četiri tvrdnje u ovom konstruiranom skupu kreću
zajedno, što daje ograničenu potporu unutarnjoj dosljednosti instrumenta. Nije
pokazao da mjere povjerenje. Četiri tvrdnje koje bi sve mjerile opću sklonost
slaganju s bilo čime mogle bi se također uredno slagati. Dosljednost je nužan
uvjet za ovaj skup pokazatelja istoga pojma, a valjanost se brani sadržajem
tvrdnji, načinom na koji ih ispitanici razumiju i usporedbom s drugim
opravdanim mjerama.

Doseg zaključka na kraju određuje ono što ovdje nije prikazano. Ne znamo tko je
ušao u uzorak ni tko je odbio sudjelovati, ne znamo kako bi stvarni ispitanici
razumjeli konstruirane tvrdnje i mjerili smo u jednom trenutku. Te granice ne
mijenjaju nijedan broj u tablici, a mijenjaju što o njemu smijemo reći. Zbog
toga metodološki odjeljak objavljenog rada nije formalnost nego mjesto na kojem
se odlučuje koliko njegovi rezultati vrijede.

## Sažetak

Mjerenje prevodi teorijske pojave u opažanja, a istraživački dizajn određuje
dokle zaključak smije dosegnuti. Jedinica, prihvatljivost, isključenja, filtri i
nedostajanje određuju tko postaje redak i na koga se rezultat može odnositi;
kodiranje jezika ista je vrsta mjerne odluke. Pouzdanost, valjanost i razina
mjerenja nisu tehnički dodatci nakon prikupljanja podataka, nego svojstva odluka
donesenih prije njega, a razrađeni primjer pokazao je da jedna previđena
formulacija može prepoloviti razlike među ispitanicima bez ijedne pogreške u
računu. Zajednički uzrok objašnjava zašto povezanost sama ne nosi uzrok, dok
nasumična dodjela stvara ravnotežu u očekivanju i traži provjeru provedbe,
pridržavanja, prelijevanja, osipanja i mjerenja. Prvi proračun nesigurnosti zato
počinje prije brojčanog intervala. Kako se promišljena prilagodba za zajedničke
uzroke provodi računski, pokazuje poglavlje o regresiji, a sljedeće poglavlje
okreće pogled prema tvrdnjama koje sve te odluke skrivaju.

## Pojmovi

operacionalizacija (*operationalization*), varijabla (*variable*), prihvatljivost
(*eligibility*), kodiranje kao mjerenje (*coding as measurement*), razina
mjerenja (*level of measurement*), pouzdanost (*reliability*), valjanost
(*validity*), konfundirajuća varijabla (*confounder*), medijator (*mediator*),
kolider (*collider*), randomizacija (*randomization*), interna valjanost
(*internal validity*), okvir uzorkovanja (*sampling frame*), eksterna valjanost
(*external validity*)

## Zadaci

### Konceptualni

Razlikujte pouzdanu mjeru od valjane mjere na vlastitom primjeru. Predajte
objašnjenje u kojem ista mjera može biti pouzdana, ali nevaljana.

Odaberite zatim jedan pojam iz svojeg područja i predložite dvije različite
operacionalizacije istog pojma. Za svaku navedite što zahvaća i što izostavlja
te opišite nalaz koji bi jedna proizvela, a druga ne bi. Za jednu od njih
imenujte jedinicu, ciljnu skupinu, pravilo prihvatljivosti i jedno isključenje
te objasnite kako bi to isključenje suzilo doseg zaključka. Imenujte i razinu
mjerenja. Ako operacionalizacija kodira jezik, dodajte pravilo za jednu oznaku
i postupak za dvosmislen slučaj.

U zamišljenom opažačkom nacrtu pratite korištenje političkih vijesti i
povjerenje u institucije. Razvrstajte političko zanimanje prije praćenja,
znanje stečeno nakon praćenja i ulazak u analizu koji ovisi i o korištenju
vijesti i o povjerenju kao zajednički uzrok, medijator ili kolider te obrazložite
svaki izbor. Zatim objasnite što bi randomizacija korištenja vijesti
uravnotežila u očekivanju i zašto ne bi jamčila jednaku početnu skupinu u jednom
malom pokusu.

### Računski

Upotrijebite tablicu povezanosti stavki iz razrađenog primjera. Za četvrtu
tvrdnju ručno provjerite kako se odgovor mijenja pri okretanju ljestvice, tako
da za odgovore od 1 do 5 zapišete okrenute vrijednosti. Zatim za prva tri
ispitanika iz tablice s odgovorima izračunajte prosjek četiriju tvrdnji prije i
nakon okretanja i predajte šest brojeva.

Iz dobivenih brojeva odgovorite u jednoj rečenici zašto propušteno okretanje
smanjuje razlike među ispitanicima umjesto da ih poveća. Postupak za istu
provjeru nad cijelim skupom podataka nalazi se u praktikumu.

### Kritički

Prosudite što se iz Berkeleyjskih podataka može zaključiti o ishodima, a što
ne može o postupku odlučivanja (Bickel, 1975). Predajte dva stupca s dopuštenim i
nedopuštenim zaključcima.

Pronađite zatim objavljeno istraživanje iz svojeg područja i utvrdite kojem
dizajnu pripada. Predajte ispunjenu karticu za čitanje njegova uzorka ili
ankete te odlomak u kojem imenujete dizajn, jedinicu, jedno pravilo ulaska ili
isključenja i jedan izvor nedostajanja. Dodajte proračun nesigurnosti s
odvojenim stupcima za mjerenje, dizajn i doseg te po jedan provjerljiv rizik u svakom.
Navedite jedan zaključak koji dizajn nosi, a zatim ili jedan autorski zaključak
koji prelazi taj doseg ili obrazloženje da autori ostaju unutar njega.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte dizajn, prepoznajte jednu
neopravdanu tvrdnju i napišite inačicu koja poštuje ograničenja dizajna. Uz
ispravak navedite koji bi dizajn bio potreban da izvorna tvrdnja postane
opravdana i zašto taj dizajn ovdje vjerojatno nije izvediv.

---

# Kako brojke zavode

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 20 min | Istraživač margine pogreške | DIP 2024. (portal) · simulacija | pogl. 1 i 2 |

**Vinjeta.**
Službeno izvješće o izborima za Hrvatski sabor 2024. prikazuje ukupan odaziv
od 62,30 % (Hrvatske}, 2024). Brojnik je 2.216.763 birača koji su pristupili
glasovanju, a nazivnik 3.558.089 birača na obrađenim biračkim mjestima
(Hrvatske}, 2024).
Broj je točno prepisan i račun se slaže s objavom.

U istom izvješću stoji 2.154.733 važećih i 60.476 nevažećih listića
(Hrvatske}, 2024). Njihov je zbroj 2.215.209, dakle 1.554 manje od broja
 pristupilih (Hrvatske}, 2024). Rečenica „glasovalo je
62,30 % birača” zato skriva odluku (Hrvatske}, 2024). Govorimo li o
pristupanju glasovanju ili o biračima prema glasačkim listićima?

Kako javnu brojku provjeriti prije nego što joj naslov podari značenje koje
izvor ne daje?

## Od točnoga broja do potpune tvrdnje

Izvor DIP-a nije novinski sažetak ni preslika na društvenoj mreži. Riječ je o
službenom *Izvješću o provedenim izborima za zastupnike u Hrvatski sabor 2024.*
(Hrvatske}, 2024). Stranica 124 nosi tablicu „Odaziv birača” (Hrvatske}, 2024).
Službeni put i tablica pregledani su dana 5. kolovoza 2026. (Hrvatske}, 2024). Knjiga
nije preuzela ni pohranila izbornu datoteku.
Portalna dostupnost nije dokaz prava na njezinu redistribuciju.

Ta napomena nije administrativni ukras. Ona čitatelju govori tko je objavio
broj, koja je objava pregledana i gdje ga može ponovno pronaći. Tvrdnja bez
takva traga možda je točna, ali se iz same tvrdnje ne može neovisno provjeriti;
provjeravatelj mora pronaći drugi pouzdan put do izvora.

Isti službeni prikaz sadrži pet brojčanih veličina koje se lako stope u jednu
riječ „birači” (Hrvatske}, 2024). Njihove oznake čuvaju različite dijelove
postupka.

| Službena veličina | Vrijednost | Uloga u čitanju |
|---|---:|---|
| ukupno birača | 3.558.089 | nazivnik na obrađenim biračkim mjestima |
| pristupilo glasovanju | 2.216.763 | brojnik objavljenog odaziva |
| glasovalo prema glasačkim listićima | 2.215.209 | kontrola prema pronađenim listićima |
| važeći listići | 2.154.733 | dio broja prema listićima |
| nevažeći listići | 60.476 | drugi dio broja prema listićima |

: Nacionalne vrijednosti izbora za Hrvatski sabor 2024. Izrada autora prema
Hrvatske}, 2024, str. 124.

Objavljeni postotak slijedi iz prvoga i drugoga retka (Hrvatske}, 2024).

$$
\frac{2\,216\,763}{3\,558\,089}\times 100 = 62{,}30\,\%.
$$

Druga provjera daje drukčiji račun.

$$
2\,154\,733 + 60\,476 = 2\,215\,209.
$$

Oba su računa točna. Službene oznake opisuju različite operativne faze, pa broj
prema listićima ne nazivamo brojem pristupilih. Razlika od 1.554 tu razliku
čini brojčano vidljivom, ali ne dokazuje kvar u evidenciji niti objašnjava
njegov uzrok (Hrvatske}, 2024). Čak ni jednaki ukupni brojevi ne bi dvije
oznake pretvorili u sinonime.

Put od tablice do naslova ima nekoliko preobrazbi. Izvor najprije objavljuje
polja s vlastitim oznakama. Autor zatim bira brojnik i nazivnik, računa omjer te
mu u rečenici pridružuje glagol i skupinu ljudi. Podaci se u tom nizu ne
moraju promijeniti, a značenje se može promijeniti na svakom koraku. Revizija
zato ne pita samo je li dijeljenje točno. Ona pita kojim su odlukama dva polja
postala javna tvrdnja.

Za odaziv je trag dostatan ovoj omeđenoj portalnoj provjeri. Vodi od datiranoga
izvješća i službenih oznaka, preko nacionalnih zbrojeva i omjera, do rečenice
koja kaže „pristupilo” (Hrvatske}, 2024). Kad asistent vrati samo 62,30 %
(Hrvatske}, 2024), završni je broj
ponovljiv, ali
njegovo značenje nije. Drugi čitatelj ne može znati koji je brojnik odabran ni
je li nazivnik zadržao izvorni obuhvat. Provjerljiv račun zato mora sačuvati i
semantički trag.

## Okvir, os i rijedak ishod

Postotak uvijek nosi pitanje „od čega?”. Odaziv 62,30 % postaje razumljiv tek
uz imenovani nazivnik (Hrvatske}, 2024). Stupac koji prikazuje samo postotak sakrio bi oba
izvorna broja. Graf čija os počinje tik ispod opaženih vrijednosti dodatno bi
uvećao vidljivu razliku među jedinicama. Skraćena os nije automatski nepoštena,
ali njezin raspon mora biti vidljiv i opravdan pitanjem.

Važno je razlikovati postotak od **postotnog boda**. Ako se dvije stope razlikuju
za 0,82 na postotnoj ljestvici, razlika iznosi 0,82 postotna boda
(Hrvatske}, 2024). Relativni
postotni rast postavlja drugo pitanje i traži dijeljenje početnom stopom.
Zamjena tih dvaju izraza mijenja veličinu priče bez promjene ijednog polaznog
broja.

Zamislimo 10.000 zapisa. Njih 100 stvorio je model umjesto bilježenja stvarnog
događaja. To je hipotetska situacija, a ne empirijski nalaz. Provjera pronađe
90 od tih 100 zapisa, ali pogrešno označi i 495 ostalih. Dobiva 585 upozorenja,
od kojih je ispravnih samo 90, približno 15,4 %. Tvrdnja „provjera je pronašla
90 % ciljanih zapisa” zato nije odgovor na pitanje „koliki je udio ispravnih
upozorenja?”.

**Temeljna stopa** jest udio ishoda u relevantnoj populaciji prije nego što se
uzme u obzir novi signal, test ili model.

U prvom je primjeru temeljna stopa 100 od 10.000 zapisa, odnosno 1 %. Taj je
udio postojao prije rezultata provjere i određuje kako čitamo njezino
upozorenje.

Promijenimo samo temeljnu stopu. Ako je među 10.000 zapisa njih 1.000
sintetičkih, ista bi provjera pronašla 900 takvih zapisa i pogrešno označila 450
ostalih. Tada bi bilo ispravno 900 od 1.350 upozorenja, odnosno dvije trećine.
Provjera nije postala tehnički bolja. Promijenila se baza na koju se primjenjuje,
pa se promijenilo i značenje njezina upozorenja.

Pouka nije da treba odbaciti svaku provjeru rijetkog ishoda. Treba razlikovati
koliko često ona nalazi ciljani ishod od toga koliko joj treba vjerovati kada
izda upozorenje. Za drugo pitanje trebamo i stopu pogrešnih upozorenja i
temeljnu stopu. Poglavlje o dobu algoritama vratit će se toj vezi kada
upozorenje postane klasifikacijska odluka s nejednakim posljedicama.

U izbornom izvješću srodnu ulogu ima baza kojoj pripisujemo broj. Udio
nevažećih listića može se računati među listićima, među pristupilima ili među
svim biračima u objavljenom nazivniku. Svaki omjer odgovara na drugo pitanje.

## Anketa, obuhvat i biranje trešanja

DIP-ova tablica sažima administrativni zapis izbora. Ona nije procjena iz
uzorka ispitanika. Nasuprot tomu, anketa pokušava iz odgovora dijela ljudi
zaključivati o široj ciljnoj populaciji. Ista riječ „postotak” ne čini ta dva
dokazna puta jednakima.

Prije čitanja rezultata ankete vrijedi sastaviti početnu karticu provjere. U nju
zapisujemo ciljnu populaciju i okvir iz kojega su ljudi mogli biti dosegnuti,
način regrutacije, broj pozvanih i broj odgovora, datume terena, formulaciju
pitanja, ponderiranje, neodaziv, naručitelja i objavljenu marginu pogreške. Ako
neka stavka nedostaje, bilježimo je kao nepoznatu. Ne popunjavamo je
pretpostavkom.

Administrativni zapis i anketa mogu govoriti o sličnoj temi, ali broj nastaje
drukčijim postupkom. Administrativna tablica nastoji obuhvatiti događaje koji
prema unaprijed utvrđenom operativnom pravilu ulaze u evidenciju. Provjera
takva zapisa obuhvaća pokrivenost, ispravnost zapisa, dosljednost oznaka i
obradbu. Anketa bilježi odgovore
odabranih ljudi. Uz ista pitanja o mjerenju nosi i uzoračku promjenjivost,
okvir, regrutaciju i neodaziv. Te se nesigurnosti ne zbrajaju u jedan opći znak
±.

Velik broj odgovora zato nije zamjena za dobar put od ciljne populacije do
ispitanika. Dobrovoljna internetska anketa može prikupiti mnogo odgovora i
ipak sustavno promašiti ljude koji se razlikuju u onome što mjerimo. Manji
vjerojatnosni uzorak može imati veću uzoračku promjenjivost, ali jasniji doseg.
To još nije teorija uzorkovanja. To je razlog da veličinu uzorka nikada ne
čitamo odvojeno od načina odabira.

Formalna margina pogreške ovdje ostaje najavljeni dug. Widget u nastavku gradi
intuiciju da veličina uzorka mijenja uzoračku promjenjivost, a sustavna
pristranost ne nestaje s većim uzorkom. Poglavlja o uzorkovanju i procjeni
razriješit će uvjete, izračun i tumačenje. Anketa se ne proglašava dobrom samo
zato što uz postotak navodi znak ±.

Službeno izvješće omogućuje neposrednu provjeru izbora obuhvata. Za izborne
jedinice I.–X. zbroj je 2.140.824 pristupilih od 3.482.150 birača, što daje
61,48 % (Hrvatske}, 2024). Za sve jedinice I.–XII. objavljeni je rezultat
62,30 % (Hrvatske}, 2024). Razlika je 0,82 postotna boda (Hrvatske}, 2024).

Obuhvat I.–X. nije neutralna zamjena za službeni ukupni obuhvat. On odgovara na
drugo, unaprijed postavljeno pitanje o tim redcima. Bez sadržajnog razloga za
takvo pitanje služi samo kao dijagnostika učinka odabira. Izabrati podskupinu
tek nakon što vidimo da daje privlačniju stopu bilo bi biranje trešanja.

Isti bi razmak na osi od 0 % do 100 % izgledao skromno, a na osi od 61 % do 63 %
zauzeo bi velik dio prikaza (Hrvatske}, 2024). Skraćena os ne mijenja razliku
od 0,82 postotna boda niti dokazni doseg (Hrvatske}, 2024). Mijenja samo
njezinu vizualnu istaknutost, pa raspon osi mora biti vidljiv i obrazložen.

## Interakcija — Istraživač margine pogreške

Ovdje prelazimo s administrativnog zapisa na konstruiranu anketnu situaciju.
Istraživač računa uobičajenu približnu 95-postotnu marginu za jednostavan
neovisan uzorak. Ne uključuje složen dizajn, ponderiranje, neodaziv ni mjernu
nesigurnost. Zaseban klizač ručno uvodi poznatu sustavnu pristranost, pa se
raspon može sužavati oko pogrešne vrijednosti. Prikaz gradi intuiciju. Ne
izvodi formalnu marginu pogreške i nije dokaz za DIP-ovu tablicu.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

U tiskanom izdanju usporedite prvo i drugo stanje da biste vidjeli učinak većega
uzorka. Potom usporedite drugo i treće stanje. Veličina uzorka i procijenjeni
udio ostaju jednaki, ali pretpostavljena istina izlazi iz uskoga intervala kada
se uključi sustavna pristranost. Promjena procijenjenoga udjela zaseban je pokus
dostupan samo u digitalnom izdanju.

Veći uzorak sužava ovako prikazanu uzoračku promjenjivost. Ne pomiče procjenu
prema istini kada je u postupak ugrađena sustavna pristranost. Uži raspon zato
ne jamči točniji odgovor.

## Podrijetlo ljudskog i strojnog broja

**Statistika u divljini.**
**Kada „glasovalo” postane preširoka riječ.** Službena tablica navodi odaziv
62,30 %, uz 2.216.763 pristupilih i nazivnik od 3.558.089 birača na obrađenim
biračkim mjestima (Hrvatske}, 2024). Zasebno, važeći i nevažeći listići daju
2.215.209 birača prema glasačkim listićima (Hrvatske}, 2024).

Naslov „Glasovalo je 62,30 % birača” može biti bezazlena kolokvijalna kratica
za sudjelovanje (Hrvatske}, 2024). Za provjerljivu je tvrdnju ipak nedovoljno
precizan jer briše službenu razliku među brojnicima i skraćuje nazivnik.
Poštenija rečenica glasi ovako.
„Službeno izvješće DIP-a bilježi da je glasovanju pristupilo 2.216.763 od
3.558.089 birača na obrađenim biračkim mjestima, odnosno 62,30 %” [Hrvatske}, 2024,
str. 124]. Ona još ne
govori tko je izašao, zašto je izašao ni za koga je glasovao.

Asistent može brzo provjeriti zbroj, usporediti dva nazivnika i predložiti
oprezniju rečenicu. Ne može vlastitim samopouzdanjem nadomjestiti izvor. Za
svaki broj koji proizvede tražimo pet veza. To su točna objava, ulazni podaci,
transformacija, nazivnik i citat koji zaista vodi do brojke. Ako jedna veza
nedostaje, nedostaje i dio podrijetla tvrdnje.

**Pitajte model.**
Asistentu dajemo točan naslov službene objave, stranicu i pet objavljenih
vrijednosti iz tablice. Tražimo da ne objašnjava razliku od 1.554 bez novoga
izvora te da odvoji provjeru aritmetike od dosega tvrdnje. Nakon odgovora ručno
otvaramo citirani dokument i pronalazimo svaki broj.

> Na temelju stranice 124 priloženog izvješća provjeri tvrdnju o odazivu.
> Odvoji izvor, jedinicu, brojnik, nazivnik, račun, razumno alternativno
> uokvirivanje i dopušten zaključak. Ne objašnjavaj razliku među službenim
> brojnicima ako izvor ne daje objašnjenje. Označi svaku stavku koju ne možeš
> provjeriti.

**Nađite grešku.**
Prema službenom izvješću, 2.154.733 važećih i 60.476 nevažećih listića zbrajaju
se u 2.215.209 birača prema glasačkim listićima (Hrvatske}, 2024). To je
1.554 manje od 2.216.763 pristupilih (Hrvatske}, 2024). Razlika iznosi
približno 0,07 % broja pristupilih (Hrvatske}, 2024), pa je dovoljno
mala da se dvije službene oznake u izvještavanju mogu rabiti kao sinonimi.

Provjera podrijetla ne završava na tablicama. Slika, zvučna snimka ili video
mogu biti sintetički, a istodobno izgledati uvjerljivo. Obrnuto, čudan izgled
nije dokaz da je zapis umjetno nastao. Razdvajamo podrijetlo datoteke,
integritet i poznate preobrazbe zapisa te istinitost tvrdnje o prikazanom
događaju. Dokaz za jedan sud ne zatvara druga dva.

Četiri oznake sprječavaju da nastavno pomagalo postane lažni dokaz.

| Oznaka | Što predmet jest | Što ne smije poduprijeti |
|---|---|---|
| simulacija | podaci proizvedeni poznatim mehanizmom radi učenja postupka | nalaz o stvarnoj populaciji |
| sintetički zapis | umjetno stvoren zapis koji oponaša oblik podatka ili medija | tvrdnju da se prikazani događaj doista zbio |
| hipotetski izlaz modela | uvjetni odgovor izrađen radi provjere zaključivanja | tvrdnju da je određeni sustav taj odgovor stvarno dao u zabilježenoj uporabi |
| izmišljeni dokaz | nepostojeći broj, opažanje ili izvor prikazan kao stvaran | bilo koju empirijsku tvrdnju |

: Četiri vrste dokaznog predmeta i njihove granice. Izrada autora.

Ni detektor sintetičkog sadržaja sam po sebi nije dokaz podrijetla. Njegov je
rezultat novi modelom proizveden broj koji ovisi o podacima za učenje, inačici,
postavkama i pragu. Temeljna stopa ponovno je važna. U zbirci u kojoj je
sintetički sadržaj rijedak i umjerena stopa pogrešnih upozorenja može nadjačati
točna upozorenja. Ocjena detektora zato može otvoriti istragu, ali ne smije
zatvoriti zaključak.

Podrijetlo može biti nepotpuno i kada je zapis autentičan. Preslika zaslona
može izgubiti metapodatke, a izvorna datoteka može biti nedostupna. Obrnuto,
uredni metapodatci ne jamče istinit sadržaj. Neovisna potvrda događaja ne
autentificira određenu datoteku. Tada je pošten ishod „nije provjereno”, a ne
automatski „sintetičko” ili „autentično”. Revizija traži put do prve objave,
bilješku o poznatim preobrazbama i zaseban dokaz za tvrdnju o događaju.

Generirani skup iz računskog zadatka pripada prvom retku. Widget je
konstruirani kalkulator, a ne simulirani dokazni predmet. Kratki pogrešni
odgovor modela pripada trećem retku. DIP-ova tablica nije ni jedno ni drugo.
Ona je službeni administrativni izvor s datiranim portalnim putem. Zamjena tih
oznaka uništila bi upravo trag koji pokušavamo sačuvati.

## Razrađeni primjer

Vraćamo se početnoj tvrdnji i prolazimo cijeli revizijski put. Cilj nije
pronaći skriveni „pravi” odaziv, nego odrediti što objavljeni dokaz doista
podupire.

Predmet provjere jest tablica „Odaziv birača” na stranici 124 *Izvješća o
provedenim izborima za zastupnike u Hrvatski sabor 2024.* (Hrvatske}, 2024).
Izdavač je Državno izborno povjerenstvo Republike Hrvatske (Hrvatske}, 2024).
Službeni je put pregledan 5. kolovoza 2026. (Hrvatske}, 2024). Knjiga ne posjeduje
lokalnu kopiju izborne datoteke i ne tvrdi da ima dopuštenje za njezinu
redistribuciju.

Taj zapis bilježi identitet i datum pregledane objave, ali ne zamrzava njezin
sadržaj. Ako se datoteka na istoj adresi promijeni ili nestane, ne posjedujemo
pregledane bajtove ni njihov kontrolni zbroj. Zato ne tvrdimo da je budući
prikaz na portalu istovjetan onomu koji smo pregledali.

Službena tablica ima dvanaest redaka izbornih jedinica, I.–XII., te nacionalni
ukupni redak za usklađenje (Hrvatske}, 2024). Nacionalni redak nije
trinaesta analitička jedinica. Nazivnik „ukupno birača” odnosi se na birače na
obrađenim biračkim mjestima u toj tablici (Hrvatske}, 2024). Ne smije se bez
provjere zamijeniti drugim brojem birača iz drugoga dijela izvješća.

Za jedinicu XII. broj važećih i nevažećih listića provjerava se zbrojem šest
objavljenih manjinskih redaka (Hrvatske}, 2024). Ta asimetrija znači da portal ne
opisujemo kao jednu provjerenu lokalnu pravokutnu datoteku. Provjeren je
službeni prikaz, ne sadržaj arhiva.

Zbroj dvanaest objavljenih nazivnika daje 3.558.089 (Hrvatske}, 2024). Zbroj
brojeva pristupilih daje 2.216.763 (Hrvatske}, 2024). Oba se zbroja potpuno
slažu s objavljenim nacionalnim retkom (Hrvatske}, 2024).

Važeći i nevažeći listići zbrajaju se u 2.215.209 (Hrvatske}, 2024). I taj
se zbroj slaže s objavljenom ukupnom vrijednošću prema listićima [Hrvatske}, 2024,
str. 124]. Usporedba s brojem pristupilih ostavlja razliku od 1.554
(Hrvatske}, 2024). Račun čini operativnu razliku vidljivom, ali je ne stvara.

Omjer 2.216.763 i 3.558.089 daje 62,30 % nakon množenja sa sto i zaokruživanja
na dvije decimale (Hrvatske}, 2024). To je potvrda objavljenoga odaziva. Nije
potvrda tvrdnje o ponašanju pojedinog birača.

### Doseg revidirane tvrdnje

Provjera obuhvata I.–X. daje 61,48 %, a službeni ukupni obuhvat I.–XII. daje
62,30 % (Hrvatske}, 2024). Razlika od 0,82 postotna boda pokazuje da obuhvat
pripada rezultatu (Hrvatske}, 2024). Uži obuhvat nije neutralna zamjena za nacionalni rezultat.
Smije se rabiti samo za zasebno, unaprijed opravdano pitanje o tim redcima.

DIP-ova tablica podržava opis administrativno zabilježenoga odaziva u
objavljenom obuhvatu. Redci izbornih jedinica mogu poduprijeti opisnu usporedbu
ili povezanost na toj razini ako se takva analiza provede. Ne podupiru zaključak
o pojedincima, potpori listama, uzrocima izlaska, budućim izborima ni populaciji
izvan izvora. Ovaj primjer podupire omeđenu uredničku odluku o tome kako
formulirati i provjeriti javnu tvrdnju.

Administrativni ukupni broj nije anketna procjena, pa mu ne pridružujemo
marginu pogreške iz widgeta. To ne znači da je bez ikakve nesigurnosti.
Obuhvat, definicije, obrada i moguće pogreške zapisa ostaju pitanja izvora i
postupka. Izvješće ovdje ne daje brojčanu mjeru za svaku od njih.

Uređena tvrdnja zato imenuje obje veličine. Prema službenom izvješću DIP-a za
izbore za Hrvatski sabor 2024., glasovanju je pristupilo 2.216.763 od 3.558.089
birača na obrađenim biračkim mjestima, odnosno 62,30 % (Hrvatske}, 2024).
Važeći i nevažeći listići zajedno daju 2.215.209 birača prema listićima, 1.554
manje od broja pristupilih (Hrvatske}, 2024). Oznake ne tretiramo kao
sinonime jer opisuju različite faze, ne zato što je razlika velika ili mala.

Zaključak bi se morao mijenjati kada bi se promijenio službeni izvor, obuhvat
obrađenih biračkih mjesta, značenje neke oznake ili usklađenje sastavnica s
ukupnim vrijednostima. Ne mijenja se zato što nam je drugi naslov privlačniji.

### Granica Dijela I — Protokol skeptičnoga čitanja

Skeptičnost nije navika odbacivanja. Ona usporava prijelaz od podatka do suda i
ostavlja vidljiv trag. Šest pitanja na granici Dijela I sažimaju taj postupak.

| Pitanje revizije | Primjena na tvrdnju o odazivu |
|---|---|
| Što je jedinica opažanja? | redak izborne jedinice; nacionalni je redak kontrolni zbroj |
| Tko ili što nedostaje, a što je odabrano? | nema individualnih obilježja; obuhvat su birači na obrađenim biračkim mjestima, a izbor I.–X. ili I.–XII. mora biti vidljiv |
| Koji je cilj i koja vrsta tvrdnje? | opis zabilježenog odaziva, ne tvrdnja o pojedincu ili uzroku |
| Koja je neizvjesnost obuhvaćena, a koja izostavljena? | aritmetika je provjerena; obuhvat i moguća pogreška zapisa nisu svedeni na marginu ankete |
| Koja je razumna alternativa? | broj prema listićima za drugo operativno pitanje; uži obuhvat samo uz unaprijed obrazložen cilj |
| Koje su posljedice pogreške? | naslov može zamijeniti službene veličine i čitatelju pripisati zaključak koji tablica ne nosi |

: Šest revizijskih pitanja primijenjenih na isti javni slučaj. Izrada autora.

Pitanja ne rade kao šest pečata koje tvrdnja automatski dobiva. Odgovor na prvo
može promijeniti drugo, a razumna alternativa može otkriti da je početni
nazivnik bio preuzak. Posljedice pogreške određuju koliko provjera mora biti
stroga. Pogrešno imenovanje brojnika u naslovu nije isto što i pogrešna odluka
koja nekome uskraćuje pravo, ali u oba slučaja mora ostati vidljivo tko snosi
teret pogreške.

Pitanja vode do pune karte tvrdnji. Vrsta tvrdnje i njezin doseg dvije su
odvojene odluke. Dokaz može dobro opisati određenu administrativnu populaciju,
a istodobno ne opravdavati generalizaciju na druge izbore ili uzročnu priču o
pojedincima.

| Dimenzija tvrdnje | Što DIP-ov dokaz dopušta u ovom primjeru |
|---|---|
| opis | poduprti su objavljeni odaziv i usklađenje službenih veličina |
| povezanost | samo na razini izbornih jedinica i tek nakon odgovarajuće analize; nacionalni ukupni redak sam nije povezanost |
| generalizacija | ne izvan populacije i obuhvata službenog izvora |
| predviđanje | nije poduprto jer tablica nije model budućih izbora |
| uzročnost | nije poduprta jer iz tablice ne saznajemo zašto je netko pristupio |
| odluka | poduprta je omeđena urednička odluka o tome je li javna formulacija provjerljiva i poštena |

: Šest dimenzija tvrdnje na granici Dijela I. Izrada autora.

Karta zaustavlja uobičajenu nadogradnju tvrdnje. Opis ne postaje uzrok zato što
je broj precizan, a usporedba izbornih jedinica ne postaje objašnjenje ponašanja
njihovih stanovnika. Odluka je zasebna dimenzija jer traži i posljedice, ne samo
račun. U ovom primjeru dopuštena je odluka o formulaciji naslova. Odluka o
izbornoj politici tražila bi dodatne ciljeve, dokaze i vrijednosne kriterije.

| Provjera | Pitanje |
|---|---|
| brojnik | Koja dva službena brojnika ne smijemo zamijeniti? |
| anketa | Zašto uzorak od nekoliko tisuća ljudi ne uklanja moguću sustavnu pristranost ankete? |
| temeljna stopa | Ako su udio pronađenih ciljanih zapisa i stopa pogrešnih upozorenja poznati, koji još podatak treba za udio ispravnih upozorenja? |
| podrijetlo | Navedite bilo koje dvije zajedničke provjere za broj i sintetičku sliku. |

: Samoprovjera Dijela I. Izrada autora.

## Sažetak

Broj može biti aritmetički točan i voditi pogrešnom zaključku. Zato čuvamo
izvor, jedinicu, brojnik, nazivnik, obuhvat, usporedbu i neizvjesnost. Temeljna
stopa sprječava da uspješnost testa zamijenimo vjerodostojnošću njegova
upozorenja. Margina pogreške ne popravlja pristranost i ovdje ostaje dug prema
poglavljima o uzorkovanju i procjeni.

Isti protokol vrijedi za službenu tablicu, anketu, odgovor asistenta i
sintetički medij. Razlikujemo simulaciju, sintetički zapis, hipotetski izlaz
modela i izmišljeni dokaz. Na granici Dijela I skeptično čitanje postaje
izvediv postupak. Šest pitanja određuje koju od šest dimenzija tvrdnje dokaz može
nositi i gdje joj završava doseg. Sljedeće poglavlje preuzima isti zahtjev pri
izgradnji analitičke tablice, provjeri transformacija i izboru poštenoga
sažetka.

## Pojmovi

postotak i postotni bod (*percentage and percentage point*), temeljna stopa
(*base rate*), margina pogreške (*margin of error*), podrijetlo tvrdnje
(*claim provenance*), sintetički zapis (*synthetic record*), protokol
skeptičnoga čitanja (*skeptical reading protocol*)

## Zadaci

### Konceptualni

Početna tvrdnja rabi broj pristupilih kao brojnik. Objasnite zašto zbroj
važećih i nevažećih listića nije zamjenjiv brojnik, iako su sva tri broja iz
istoga izvješća. Navedite što se može zaključiti iz razlike od 1.554, a što ne
(Hrvatske}, 2024). Zatim objasnite, bez novoga računa, zašto se udio
ispravnih upozorenja u dva hipotetska primjera mijenja iako provjera jednako
često nalazi ciljane zapise i jednako često pogrešno upozorava.

### Računski

Upotrijebite izvanmrežni agregat generiranoga skupa `populacija_medija` iz
datoteke `data/populacija-medija-agregat.csv` (Šikić, 2026). U izmišljenom gradu
portal je glavni izvor vijesti za 15.101 od 50.000 generiranih osoba, a
televizija za 10.827 (Šikić, 2026). Izračunajte oba udjela, razliku u postotnim
bodovima i relativnu razliku prema udjelu televizije. Jasno napišite da rezultat
opisuje simulaciju, ne stvarnu populaciju. Dopušten je kalkulator ili proračunska
tablica; ne predaje se kod.

### Kritički

Polazište je nacionalni redak službene tablice „Odaziv birača” [Hrvatske}, 2024, str.
124]. Usporedite tri ponuđene uredničke prerade toga retka. To su „Na izborima
je glasovalo 62,30 % birača”, „DIP bilježi da je glasovanju pristupilo 62,30 %
birača na obrađenim biračkim mjestima” i „Većina građana podržala je
pobjedničke liste” (Hrvatske}, 2024). Za svaku navedite je li poduprta
prikazanim dokazom.
Najbolju preradu doradite tako da uključi brojnik, nazivnik, izvor i jednu
važnu granicu.

Zatim razvrstajte četiri dokazna predmeta. To su generirana populacija iz
računskoga zadatka, pogrešni odgovor modela iz okvira, umjetno stvorena i tako
označena izborna fotografija te nepostojeća stranica izvješća prikazana kao
izvor. Svakom predmetu pridružite jednu od četiriju oznaka. Oznake su
simulacija, hipotetski izlaz modela, sintetički zapis i izmišljeni dokaz.
Objasnite koju tvrdnju svaka oznaka zabranjuje.

### Revizija modela

Ocijenite odgovor modela iz okvira iznad. Ponovite zbroj listića i razliku prema
broju pristupilih (Hrvatske}, 2024), a zatim napišite zamjenski odgovor od
najviše četiri rečenice. Odvojite ono što je izvorno potvrđeno od objašnjenja
koje bi tražilo nov dokaz.
