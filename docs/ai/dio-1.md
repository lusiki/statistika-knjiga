# DIO I: STATISTIČKO MIŠLJENJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Zašto statistika

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/01-zasto-statistika.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 18 min | Simpsonov paradoks | UCBAdmissions | bez preduvjeta |

**Vinjeta.**
Podaci o upisima na Sveučilište Kalifornije u Berkeleyju 1973. godine otvorili
su ozbiljno pitanje. Jesu li njegovi poslijediplomski programi pri upisu
diskriminirali žene (Bickel, 1975)? Zbirni podaci upućivali su upravo na to.
Među prijavama u šest najvećih odjela stopa prijma iznosila je
`r paste0(hr_broj(100 * stopa_muskarci, 1), " %")` za muškarce i
`r paste0(hr_broj(100 * stopa_zene, 1), " %")` za žene (Bickel, 1975).

Istraživački tim zatim je iste prijave razdvojio prema odjelu. Slika se
promijenila. U `r odjeli_prednost_zene` od šest odjela stopa prijma za žene
bila je barem jednaka stopi za muškarce, dok su se žene češće prijavljivale na
odjele na kojima je prijam bio teži za sve kandidate (Bickel, 1975). Zbirni jaz
nije nestao iz tablice, ali njegovo se značenje više nije moglo čitati na isti
način.

Oba su prikaza nastala iz istih prijava i oba su računski točna. Jedan sugerira
veliku razliku, a drugi pokazuje da sastav prijava tu razliku snažno oblikuje.
Kojoj slici treba vjerovati kada ispravan izračun vodi prema pogrešnom
zaključku?

## Broj nije zaključak

Berkeleyjski slučaj ne pokazuje da su podaci nepouzdani. Pokazuje nešto
zahtjevnije. Podaci ne donose zaključak bez pitanja koje im postavljamo i bez
usporedbe kojom na to pitanje odgovaramo. Zbirna stopa odgovara na pitanje tko
je češće primljen u promatranoj skupini prijava. Stope po odjelima odgovaraju na
pitanje kako su prolazili kandidati koji su se prijavili na isti odjel. Ta su
pitanja povezana, ali nisu ista.

**Statistika** počinje upravo na mjestu na kojem prestaje jednostavno
prebrojavanje. Njezina zadaća nije proizvesti broj, nego odrediti što taj broj
može poduprijeti. Pritom mora sačuvati vezu između pitanja, načina mjerenja,
usporedbe i zaključka. Izračun može biti besprijekoran, a tvrdnja izgrađena na
njemu ipak pogrešna jer broj odgovara na drugo pitanje od onoga koje nas
zanima.

Zbog toga podatke nije korisno zamišljati kao suprotnost ljudskom iskustvu.
Anegdota može otkriti problem, predložiti mehanizam ili pokazati posljedicu
koju tablica skriva. Ne može nam sama reći koliko je pojava raširena ni što bi
se dogodilo u drugim okolnostima. Podaci proširuju pogled preko pojedinačnog
slučaja, ali zauzvrat traže odluke o tome koga smo promatrali, što smo mjerili i
s čime rezultat uspoređujemo.

Podjela posla među njima prilično je jasna. Pojedinačan slučaj dobro odgovara
na pitanje kako se nešto uopće događa, jer opisuje redoslijed, okolnosti i
iskustvo koje brojka izostavlja. Ispitanica koja objašnjava zašto je prestala
čitati vijesti daje mehanizam koji nijedna stopa ne sadrži. Podaci na razini
skupine odgovaraju na pitanje koliko je često i koliko različito, jer jedino
oni pokazuju kako se slučajevi raspoređuju. Nesporazum nastaje kada odgovor na
jedno pitanje uzmemo kao odgovor na drugo, pa iz jednog uvjerljivog svjedočenja
izvedemo raširenost ili iz prosjeka izvedemo iskustvo pojedinca.

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

Okolnosti su usto takve da se podacima više ne bavi samo istraživač. Svaki
klik, otvorena poruka i sekunda gledanja negdje se bilježe, a odluke o
sadržaju, oglasima i dosegu donose se iz tih zapisa. Tko ne razumije kako
takvi podaci nastaju i što njihovi rezultati ne pokazuju, ne može ravnopravno
sudjelovati u raspravi koju oni oblikuju. Statistička pismenost time postaje
uvjet sudjelovanja, a ne dodatna vještina.

Navarro učenje statistike uspoređuje s kuharskim receptom, gdje niz mehaničkih
uputa najprije izgleda proizvoljno, a razumijevanje počinje kada postane jasno
zašto svaki korak postoji (Navarro, 2019). Recept se tada prestaje slijediti i
počinje se kuhati. Ista razlika dijeli izračun od statističkog mišljenja.
Formula se može primijeniti bez razumijevanja, ali odluka o tome koju usporedbu
uopće treba napraviti ne može.

Vrijedi odmah reći i što statistika ne obećava. Ona ne pretvara nepotpune
podatke u potpune i ne nadoknađuje ono što nije izmjereno. Ne odlučuje umjesto
istraživača koja je usporedba važna, jer taj izbor pripada području o kojem se
raspravlja, a ne računu. Ne uklanja nesigurnost, nego je izražava, pa je pošten
statistički nalaz gotovo uvijek uži i oprezniji od tvrdnje koja mu prethodi.
Očekivanje da će analiza donijeti konačan sud najčešće završava razočaranjem
ili pretjeranom tvrdnjom, a knjiga na oboje pokušava odgovoriti ranije nego
kasnije.

## Gdje intuicija popušta

Protiv takvog postupka govori jedan uporan prigovor. Ako je zaključak
dovoljno očit, čemu formalna provjera. Odgovor je da naša prosudba
promjenjivosti i vjerojatnosti sustavno griješi, i to na predvidljive načine.
Ljudska sklonost prepoznavanju obrazaca izvanredno je korisna, ali radi i kada
obrasca nema.

Slučajnost je prvo mjesto na kojem intuicija popušta. Niz od 10 bacanja
novčića u kojem se pismo i glava savršeno izmjenjuju većini ljudi ne izgleda
slučajno. Neuredan niz s tri uzastopna pisma izgleda mnogo prirodnije. Kod
poštenog novčića svaki od 1024 moguća niza jednako je vjerojatan, pa ni jedan
od njih nije manje slučajan od drugoga. Mi zapravo ne uspoređujemo niz s
vjerojatnošću nego s mentalnom slikom slučajnosti koja je previše uredna.
Stvarna je slučajnost grudasta, pa nizovi, gomilanja i naizgled značajni
obrasci nastaju i kada iza njih ne stoji nikakav uzrok.

Drugo mjesto je pojedinačan slučaj. Ako susjed hvali novu aplikaciju za vijesti
i dvoje kolega kaže isto, dojam dokaza nastaje gotovo automatski. Troje ljudi
ipak ne opisuje populaciju, a ni njihov izbor nije slučajan, jer su za novu
aplikaciju vjerojatno posegnuli oni koji se vijestima ionako više bave.
Tversky i Kahneman opisali su sklonost da učestalost pojave procjenjujemo prema
tome koliko nam lako pada na pamet njezin primjer, što su nazvali heuristikom
dostupnosti (Tversky, 1973). Živopisan i nedavan slučaj time dobiva težinu koju
mu njegova stvarna zastupljenost ne daje.

Treće mjesto je povezanost. Portali koji objavljuju više tekstova imaju više
ukupnih posjeta, iz čega se lako izvodi savjet da treba objavljivati više.
Veći portali istodobno imaju više novinara, veći proračun i stariju publiku,
pa broj tekstova može biti popratna pojava, a ne uzrok. Odnos među dvjema
pojavama može nastati zato što prva utječe na drugu, zato što druga utječe na
prvu ili zato što obje ovise o nečem trećem. Tvrdnja da povezanost nije
uzročnost zvuči kao opće mjesto, ali koraci kojima se ona provjerava predmet su
poglavlja o dizajnu istraživanja i poglavlja o regresiji.

Ta tri promašaja imaju zajednički oblik. U svakome nam nedostaje usporedba.
Ne znamo kako izgledaju ostali nizovi, ne znamo za one koji aplikaciju nisu
pohvalili i ne znamo što bi se dogodilo pri istom broju tekstova na portalu
druge veličine. Statistika popravlja upravo to, tako da usporedbu učini
izričitom umjesto da je prepusti dojmu.

Zbog toga ni količina podataka sama po sebi ne rješava problem. Analitika
velikog portala bilježi milijune interakcija, ali ako bilježi samo one koji su
došli, o onima koji nisu ne govori ništa, koliko god zapisa bilo. Veći skup
smanjuje rasipanje oko procjene, a sustavan propust u tome što je uopće
promatrano ostaje jednako velik u malom i u golemom skupu. Pogreška izbora ne
razrjeđuje se količinom, što je razlika koju poglavlje o uzorkovanju razrađuje
brojčano.

Prigovor da ovakav oprez vodi u nemoć ipak ne stoji. Nesigurno znanje nije isto
što i neznanje, a razlika među njima je upravo ono što statistički postupak
mjeri. Ista disciplina koja zabranjuje preširok zaključak dopušta da uži
zaključak izrečemo s razlogom i da kažemo koliko čvrsto stoji.

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

Iz promjenjivosti slijedi ograničenje koje vrijedi za cijelu knjigu. Jedno
opažanje ne može razriješiti pitanje o obrascu, ma koliko bilo uvjerljivo.
Student koji se puno koristi mrežama i slabo prati vijesti ne pokazuje da veza
postoji, kao što ni student koji je iznimka ne pokazuje da veze nema. Obojica
su podaci, ali obrazac postoji na razini skupine, a ne pojedinca, pa se i
provjeriti može samo na skupini.

Broj promatranih slučajeva zato ulazi u tumačenje rezultata jednako kao i sam
rezultat. Razlika izmjerena na desetak ljudi lako nastaje istom
promjenjivošću koja bi se pri sljedećem prikupljanju podataka okrenula na
drugu stranu. Ista razlika izmjerena na tisućama ljudi mnogo je teže objašnjiva
pukim rasipanjem. Koliko točno uzorak sužava taj prostor, pitanje je poglavlja
o uzorkovanju.

Usporedba je pritom važnija od samog velikog ili malog broja. Pad, rast ili
razlika dobivaju značenje tek kada znamo prema čemu ih mjerimo. Ponekad je
usporedba druga skupina, ponekad ranije razdoblje, a ponekad raspon rezultata
koji bi mogli nastati običnom promjenjivošću. Kasnija poglavlja izgradit će
računske postupke za te usporedbe. Za sada je važan njihov zajednički temelj.
Tvrdnja postaje statistička tek kada jasno kaže što se s čim uspoređuje.

## Razlika koju čini postupak

Prijelaz s dojma na postupak najlakše se opiše kroz ono što postupak od nas
traži da napišemo. Dojam može ostati neodređen i time neoboriv. Zapisana
analiza mora odgovoriti na četiri pitanja, a svako od njih otvara mjesto na
kojem je moguće pogriješiti i na kojem je pogrešku moguće naći.

Prvo pitanje glasi koga smo promatrali. Berkeleyjska tablica ne govori o svim
sveučilištima ni o svim prijavama, nego o šest odjela u jednoj godini
(Bickel, 1975). Doseg tvrdnje nikada nije širi od skupa koji je ušao u izračun,
a najčešća pogreška pri čitanju statistike jest tiho proširenje tog dosega.
Drugo pitanje glasi što smo izmjerili. Stopa prijma bilježi ishod postupka, ne
namjeru onih koji su odlučivali, pa ista brojka podupire tvrdnju o ishodima i
ne podupire tvrdnju o motivima.

Treće pitanje glasi s čime rezultat uspoređujemo. Ono je najzahtjevnije jer
usporedbu obično biramo nesvjesno, a upravo je izbor usporedbe ono što je u
Berkeleyju preokrenulo zaključak. Isti postotak podupire različite tvrdnje ovisno
o tome stoji li uz drugu skupinu, uz prošlu godinu ili uz vrijednost koju bismo
očekivali da nikakve razlike nema. Objava koja navodi samo jedan broj tu je
odluku već donijela umjesto čitatelja, obično prešutno.

Četvrto pitanje glasi koliko bi se rezultat mogao pomaknuti da smo prikupili
druge podatke iste vrste. Nijedno mjerenje ne pogađa istu vrijednost dvaput, pa
svaka procjena ima raspon unutar kojeg se razumno može kretati. Tvrdnja bez
ikakve mjere nesigurnosti zato obećava više nego što podaci nose, a upravo se
takve tvrdnje najlakše šire. Kako se taj raspon računa i kako se pošteno
izriče, predmet je poglavlja o procjeni.

Postupak, dakle, ne jamči točan zaključak. On jamči nešto skromnije i
korisnije. Čini tvrdnju provjerljivom, tako da neslaganje postane rasprava o
podacima, mjerenju i usporedbi umjesto rasprave o tome tko je uvjerljiviji. Kada
dvoje ljudi tvrde suprotno na temelju istog skupa, razlika među njima mora se
moći pokazati u jednom od ta četiri koraka, jer drugih mjesta nema. Ostatak ove
knjige razrađuje upravo ta pitanja, jedno po jedno, i svakom od njih posvećuje
vlastite postupke.

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

Takav se obrat naziva **Simpsonov paradoks**. Riječ je o obrascu u kojem se
povezanost vidljiva u združenim podacima promijeni ili preokrene kada podatke
razdvojimo prema relevantnoj trećoj varijabli (Simpson, 1951). Paradoks nije u
aritmetici. Svaka stopa ostaje točna. Neobičnost nastaje zato što iste brojke
opisuju različite usporedbe, a naš se zaključak promijeni kada to napokon
primijetimo.

Mehanizam se najlakše vidi na konstruiranom primjeru u kojem sve brojke stanu
u jednu rečenicu. Neka portal A objavi 100 videozapisa s prosječnim angažmanom
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

Ostaje pitanje kojem prikazu vjerovati kada se dva razilaze. Odgovor nije
statistički, i to je možda najvažnija pouka ovog poglavlja. Sama aritmetika ne
može odlučiti treba li odjel ući u usporedbu, jer su obje tablice jednako
točne. Odluka ovisi o tome kakvu tvrdnju želimo provjeriti. Za tvrdnju o
odlučivanju unutar odjela usporedba mora biti unutar odjela. Za tvrdnju o
ukupnom ishodu prijava zbirna je stopa upravo ono što treba. Tek kad je pitanje
jasno postavljeno, brojke postaju dokaz, a poglavlje o mjerenju i
istraživačkom dizajnu bavi se time kako se to pitanje postavlja.

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

Posljednji korak pokazuje granicu pojave. Dok su obje skupine jednako
raspoređene po podskupinama, zbirna usporedba slijedi usporedbu unutar
podskupina i obrata nema. Obrat traži da se skupine razlikuju i po tome gdje su
mjerene, a ne samo po tome kako su prošle. Zbirna razlika zato uvijek sadrži
dva sastojka, uspješnost i sastav, koje bez razdvajanja podataka ne možemo
razlučiti.

**Statistika u divljini.**
**Privid pristranosti u zbirnoj stopi.** Tvrdnja da su muškarci u Berkeleyju
1973. primani češće od žena aritmetički je točna za šest najvećih odjela
(Bickel, 1975). Problem nastaje tek kada tu zbirnu razliku pretvorimo u
objašnjenje postupka upisa. Ukupna stopa istodobno spaja odluke različitih
odjela i različitu raspodjelu prijava među njima.

Odgovorno čitanje zato ne odbacuje zbirnu stopu, ali od nje traži pomoćne
informacije. Potrebni su brojevi prijava i primljenih kandidata unutar svakog
odjela te objašnjenje zbog čega je odjel relevantna podjela. Tek tada vidimo
koji dio razlike nastaje unutar usporedivih skupina, a koji zbog njihova
različitog sastava.

**Pitajte model.**
Asistent može brzo izračunati zbirne stope i ponoviti izračun po podskupinama,
ali mu treba dati stvarne brojnike i nazivnike. Nakon odgovora valja provjeriti
daju li zbrojevi ćelija objavljene ukupne vrijednosti i je li svaka stopa
izračunata s odgovarajućim nazivnikom. Modeli osobito lako nadopune ćeliju
koja nedostaje ili svaku razliku između zbirnog i grupiranog prikaza proglase
Simpsonovim paradoksom.

> Usporedi zbirne stope prijma sa stopama po odjelima. Prikaži broj prijava,
> broj primljenih i nazivnik svake stope. Opiši kako sastav prijava mijenja
> zbirni rezultat, ali nemoj iz tih tablica izvoditi kauzalni zaključak.

**Nađite grešku.**
Zbirna stopa prijma bila je viša za muškarce, dok je u četiri od šest odjela
stopa za žene bila barem jednaka stopi za muškarce (Bickel, 1975). Žene su se
češće prijavljivale na selektivnije odjele (Bickel, 1975). Stoga je izbor
odjela uzrokovao cijeli zbirni jaz.

Greška je kauzalni zaključak u posljednjoj rečenici. Tablica pokazuje da
raspodjela prijava po odjelima objašnjava statističku strukturu zbirnog jaza,
ali sama ne dokazuje zašto su kandidati birali određene odjele niti da je time
objašnjen svaki mogući oblik pristranosti.

## Razrađeni primjer

Berkeleyjski podaci omogućuju da cijeli problem pratimo bez složenog modela.
Svaki redak izvorne tablice govori o ishodu prijave, spolu kandidata i odjelu.
Prvi korak združuje odjele te za svaku skupinu dijeli broj primljenih s ukupnim
brojem prijava.

*Slika. Zbirne stope prijma u šest najvećih odjela. Izrada autora prema @bickel1975.*

Zbirna tablica pokazuje velik jaz. Primljeno je
`r paste0(hr_broj(100 * stopa_muskarci, 1), " %")` muškaraca i
`r paste0(hr_broj(100 * stopa_zene, 1), " %")` žena među prijavama obuhvaćenim
ovim podacima (Bickel, 1975). Kada bismo ovdje stali, bilo bi razumljivo
posumnjati da je ista razlika prisutna u odlukama svakog odjela. Ta pretpostavka
ipak nije sadržana u zbirnoj stopi.

Sljedeći korak ne mijenja nijednu prijavu. Mijenja samo razinu na kojoj ih
uspoređujemo. Stope sada računamo zasebno u svakom odjelu, čime kandidati iz
selektivnog odjela više ne utječu izravno na usporedbu kandidata u odjelu s
višom prolaznošću.

Stope prijma prema odjelu i spolu. Izrada autora prema bickel1975.

Stope po odjelima više ne podržavaju jednostavnu priču prema kojoj se isti jaz
ponavlja posvuda. U četiri od šest odjela stopa za žene barem je jednaka stopi
za muškarce, dok je u preostala dva niža (Bickel, 1975). Presudan je i raspored
prijava. Velik dio prijava žena završio je u odjelima s niskim stopama prijma,
pa su ti odjeli dobili veću težinu u njihovoj zbirnoj stopi (Bickel, 1975).

Zbirna stopa može se zamisliti kao prosjek odjelnih stopa u kojem odjeli nemaju
jednaku težinu. Njihova težina ovisi o broju prijava iz svake skupine. Zato dvije
skupine mogu imati sličan ili obrnut odnos unutar odjela, a ipak vrlo različite
ukupne stope. Obrat ne proizvodi pogrešan račun. Proizvode ga različiti utezi u
dvama zbirnim prosjecima.

Ti se utezi mogu i izmjeriti. Odjeli se u ovim podacima razlikuju znatno više
međusobno nego što se unutar njih razlikuju muškarci i žene, jer ukupna
prolaznost pada s `r paste0(hr_broj(100 * s1$prolaznost_max, 0), " %")` u
najpristupačnijem odjelu na `r paste0(hr_broj(100 * s1$prolaznost_min, 0), " %")`
u najselektivnijem (Bickel, 1975). Na dva najpristupačnija odjela otpada
`r paste0(hr_broj(s1$laksi_m, 0), " %")` svih prijava muškaraca i tek
`r paste0(hr_broj(s1$laksi_z, 0), " %")` prijava žena, dok na dva
najselektivnija otpada `r paste0(hr_broj(s1$tezi_m, 0), " %")` prijava
muškaraca i `r paste0(hr_broj(s1$tezi_z, 0), " %")` prijava žena
(Bickel, 1975). Dvije skupine zapravo nisu prolazile kroz isti postupak
odabira, nego kroz različite mješavine postupaka.

Tek s tim brojevima obrat prestaje biti neobičnost i postaje očekivan. Skupina
čije se prijave gomilaju ondje gdje su svi rijetko primani mora imati nižu
zbirnu stopu, čak i kada je u većini odjela prolazila jednako dobro ili bolje.
Zbirna razlika u tom smislu vjerno mjeri nešto stvarno, samo ne ono što se na
prvi pogled čini. Ona mjeri raspored prijava barem koliko i strogost
odlučivanja.

Ova analiza još ne daje konačan sud o pravednosti upisa. Odjelne tablice ne
govore zašto su prijave raspoređene upravo tako, kako su kandidati usmjeravani
ni jesu li kriteriji unutar odjela bili primijenjeni jednako. One postižu nešto
uže i nužno. Pokazuju da zbirnu razliku ne smijemo tumačiti kao izravnu sliku
odluka unutar svakog odjela. Statistički postupak nije zatvorio pitanje, nego ga
je napokon postavio dovoljno precizno.

## Sažetak

Statistika povezuje podatke s usporedbom koja određenom zaključku daje značenje.
Bez postupka odluku preuzima najuvjerljiviji govornik, a intuicija na tom mjestu
griješi predvidljivo, jer slučajnost tumači kao obrazac i pojedinačan slučaj kao
raširenost. Promjenjivost nije smetnja koju uklanjamo, nego građa iz koje
razlučujemo signal i šum. Simpsonov paradoks pokazuje da točan zbirni rezultat
može zavesti kada skriva sastav podskupina, i da izbor između dvaju točnih
prikaza ovisi o pitanju, a ne o računu. Strog pristup zato ne završava
izračunom, nego provjerava koga smo promatrali, što smo izmjerili, s čime smo
usporedili i koliko bi se rezultat mogao pomaknuti. Sljedeći korak vodi prema
mjerenju i istraživačkom dizajnu, gdje se odlučuje što će uopće postati podatak.

## Pojmovi

statistika (*statistics*), signal (*signal*), šum (*noise*), heuristika
dostupnosti (*availability heuristic*), zbirni podaci (*aggregate data*),
podskupina (*subgroup*), Simpsonov paradoks (*Simpson's paradox*)

## Zadaci

### Konceptualni

Objasnite kako dvije računski točne stope mogu poduprijeti različite zaključke.
U odgovoru razlikujte zbirnu usporedbu od usporedbe unutar podskupina.

Zatim opišite situaciju iz vlastitog područja u kojoj bi pojedinačan slučaj
bio bolji izvor od podataka o skupini, i situaciju u kojoj bi bilo obrnuto.
Predajte dva kratka odlomka i u svakome imenujte pitanje na koje odabrani izvor
odgovara.

### Računski

Upotrijebite konstruirani primjer dvaju portala iz odjeljka o zbirnoj slici.
Izračunajte ručno zbirni prosjek angažmana za svaki portal i provjerite da
odgovara brojkama u tekstu. Zatim portalu B zamijenite broj videozapisa i broj
tekstova, ostavite sve prosjeke unutar formata nepromijenjenima i ponovno
izračunajte oba zbirna prosjeka. Predajte četiri broja i jednu rečenicu o tome
koji se zbirni prosjek promijenio i zašto, iako se nijedan prosjek unutar
formata nije promijenio.

Zatim se vratite na tablicu zbirnih stopa prijma i na sliku stopa po odjelima
iz razrađenog primjera. Pročitajte s njih u koliko odjela žene imaju barem
jednaku stopu prijma i zapišite u jednoj rečenici zašto to ne proturječi nižoj
zbirnoj stopi. Postupak za isti izračun nad cijelim skupom podataka nalazi se
u praktikumu.

### Kritički

Prosudite tvrdnju da zbirni jaz u stopama prijma sam po sebi dokazuje
pristranost svakog odjela u Berkeleyju (Bickel, 1975). Navedite koju dodatnu
usporedbu tvrdnja preskače i što ni ta dodatna usporedba ne može dokazati.

Pronađite zatim u medijima jednu tvrdnju koja uspoređuje dvije skupine pomoću
jednog zbirnog broja. Za nju odgovorite na četiri pitanja iz odjeljka o
postupku, koja se odnose na promatrani skup, izmjerenu veličinu, usporedbu i
nesigurnost. Predajte tvrdnju, njezin izvor i po jednu rečenicu o svakom
pitanju, uključujući pitanja na koja objava ne daje odgovor.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte točne korake, izdvojite jednu
neopravdanu tvrdnju i napišite njezinu oprezniju zamjenu. U obrazloženju
navedite koji bi podatak trebalo imati da bi izvorna tvrdnja postala opravdana.

---

# Mjerenje i istraživački dizajn

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/02-mjerenje-i-dizajn.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Prikaz konfundera | konstruirani primjeri | pogl. 1 |

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

Društvene znanosti najčešće proučavaju pojave koje ne možemo položiti na vagu.
Povjerenje, politička otuđenost, osjećaj sigurnosti i izloženost medijima
postoje kao pojmovi prije nego što postoje kao brojke, pa se moraju prevesti u
opažanja.

**Operacionalizacija** je postupak kojim se teorijski pojam pretvara u
određeni način mjerenja, tako da se navede što će se opažati i po kojem
pravilu će se opažanju pridružiti vrijednost.

Isto teorijsko pitanje može postati jedno anketno pitanje, skup tvrdnji,
ponašajni trag ili procjena promatrača. Svaki izbor zahvaća dio pojave i
istodobno nešto izostavlja.

Rijetko se pritom oslanjamo na jedno pitanje. Uobičajen je postupak da se isti
pojam zahvati s nekoliko tvrdnji koje se potom sažimaju u jedan rezultat.
Razlog nije temeljitost nego to što svaka pojedina tvrdnja uz zajednički pojam
nosi i vlastite osobitosti, poput riječi koju dio ispitanika razumije drukčije.
Kada se odgovori zbroje, zajednički se dio pojačava, a pojedinačne osobitosti
djelomično poništavaju. Cijena je što izvedeni rezultat više ne odgovara
nijednom stvarno postavljenom pitanju, pa se mora tumačiti kroz sadržaj svih
tvrdnji koje su u nj ušle.

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

Ta odluka pada prije prikupljanja podataka i poslije se ne može popraviti.
Ispitanik koji je odgovarao na ljestvici s pet stupnjeva ne može naknadno biti
smješten na ljestvicu s deset. Anketa koja nije pitala za mjesto stanovanja ne
može naknadno razlikovati grad i selo. Analiza radi s onim što je mjerenje
propustilo kroz sebe, pa je operacionalizacija najutjecajniji korak
istraživanja i istodobno onaj koji se u izvještajima najkraće opisuje.

Zbog toga se pri čitanju tuđeg istraživanja isplati zastati na tri pitanja
prije nego što se pogleda ijedan rezultat. Kako je ključni pojam izmjeren, ne
kako je nazvan. Koja je jedinica analize, jer ista riječ može označavati osobu,
objavu, sat gledanja ili kućanstvo, a nalaz se mijenja s tim izborom. I što je
mjerenje moralo izostaviti, jer svaki instrument nešto ne vidi. Odgovori na ta
tri pitanja obično stoje u dva odlomka metodologije koje je najlakše preskočiti
i koji najviše određuju kako valja čitati sve ostalo.

Anketno pitanje pritom nije neutralan prozor prema stavu nego dio mjernog
instrumenta. Formulacija određuje što ispitanik razumije, ponuđeni odgovori
određuju što uopće može reći, a redoslijed pitanja može promijeniti okvir u
kojem odgovara. Ispitanik koji je upravo odgovarao na niz pitanja o
nesigurnosti drukčije će ocijeniti povjerenje u institucije nego onaj kojemu je
isto pitanje postavljeno prvo. Ništa od toga nije razlog za odbacivanje anketa.
Razlog je za to da se rezultat čita zajedno s upitnikom, a ne umjesto njega.

## Razine mjerenja

Brojevi u podacima ne znače uvijek isto. Stevens je 1946. godine predložio
podjelu na četiri razine mjerenja, koja se u društvenim znanostima koristi i
danas jer određuje koje računske operacije na nekoj varijabli imaju sadržajno
značenje (Stevens, 1946). Podjela ne govori o važnosti teme nego o tome što se
smije izvesti iz zapisanih vrijednosti.

Na **nominalnoj razini** brojevi ili oznake samo imenuju kategorije i među njima
nema poretka. Vrsta medija, država prebivališta, stranačka bliskost i status
zaposlenosti pripadaju ovamo. S takvim se podacima može prebrojavati i računati
udio, ali prosjek nema smisla, jer prosječna vrsta medija ne postoji.
**Ordinalna razina** dodaje poredak bez jamstva da su razmaci jednaki. Odgovori
na ljestvici slaganja imaju jasan smjer, a tvrdnja da je razlika između
neslaganja i neutralnosti jednaka razlici između slaganja i potpunog slaganja
ostaje pretpostavka. Medijan je ovdje smislen, dok je prosjek kompromis.

**Intervalna razina** ima jednake razmake, ali proizvoljno ishodište, pa
dopušta zbrajanje i oduzimanje, a ne i omjere. **Omjerna razina** ima i
apsolutnu nulu, zbog čega je izjava o dvostruko većoj vrijednosti opravdana.
Vrijeme provedeno na platformi, broj dijeljenja i dohodak omjerne su varijable,
jer nula ondje doista znači odsutnost pojave.

Praksa je pritom manje uredna od podjele. Ljestvice slaganja strogo su
ordinalne, a u velikom se dijelu objavljene literature zbrajaju i prosječuju
kao da su intervalne. Taj kompromis nije nemaran koliko se čini, jer zbroj više
tvrdnji koje mjere isti pojam ponaša se stabilnije od svake pojedine, ali
ostaje pretpostavka koju vrijedi izreći umjesto prešutjeti. Čitatelj koji zna
da je prosjek ordinalne ljestvice pretpostavka, a ne činjenica, drukčije čita
razliku od dvije desetine bodova između dviju skupina.

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
Anketa koja odmah nudi razrede umjesto broja štedi ispitaniku nekoliko sekundi
i trajno oduzima analizi mogućnosti.

Iz toga slijedi savjet koji vrijedi za svako prikupljanje podataka. Razina se
planira unaprijed, prema analizama koje namjeravamo provesti, a ne bira
naknadno. Ako je cilj prosjek ili korelacija, potrebna je barem intervalna
mjera. Ako je cilj samo raspodjela po kategorijama, nominalna je dovoljna.
Odgovor na to pitanje pripada nacrtu istraživanja, a ne obradi podataka, i
najjeftinije je pravilo u ovom poglavlju, jer se poštuje bez ikakva troška i
krši uz trošak koji se ne može nadoknaditi.

## Pouzdanost i valjanost

Dobra mjera mora zadovoljiti dva odvojena zahtjeva koja se lako brkaju. Prvi je
postojanost. Vaga koja pri tri uzastopna vaganja pokaže tri različite težine
beskorisna je iako mjeri pravu veličinu.

**Pouzdanost** je stupanj u kojem instrument daje dosljedne rezultate pri
ponovljenom mjerenju istog stanja u istim uvjetima.

Pouzdanost se u društvenim znanostima provjerava na tri načina koje ćete
sretati u metodološkim odjeljcima objavljenih radova. Ponovljeno mjerenje
uspoređuje rezultate istog instrumenta u dva trenutka, uz pretpostavku da se u
međuvremenu nije promijenilo ono što se mjeri. Slaganje među procjenjivačima
važno je svugdje gdje ljudi kodiraju građu, pa dva kodera koja isti tekst
ocijene različito otkrivaju problem instrumenta, a ne razliku u građi. Interna
konzistentnost pita slažu li se čestice istog upitnika međusobno, jer bi sve
trebale zahvaćati isti pojam. Cronbachov alfa najčešća je mjera te treće
vrste, dok se za slaganje među koderima najčešće navode Cohenova kappa i
Krippendorffova alfa. Granice koje se u praksi spominju kao prihvatljive
konvencija su o kojoj se i dalje raspravlja, pa ih ne treba čitati kao prag
položenog ispita.

Za čitatelja iz toga slijedi konkretna provjera. Rad koji se oslanja na
upitnik trebao bi za svaku ljestvicu navesti mjeru interne konzistentnosti, a
rad koji kodira sadržaj trebao bi navesti mjeru slaganja među koderima i broj
jedinica na kojima je izračunata. Izostanak tih podataka ne dokazuje da je
mjerenje loše, ali uklanja jedini način na koji bi se to izvana moglo
provjeriti, pa je razlog za oprez pri tumačenju.

Kod ponovljenog mjerenja krije se zamka koja je za društvene znanosti
specifična. Stavovi se doista mijenjaju, pa razlika između dva termina može
značiti da instrument nije pouzdan ili da se svijet u međuvremenu promijenio.
Ako se između dvaju mjerenja povjerenja u medije dogodio velik skandal, pad
rezultata nalaz je, a ne pogreška. Razlikovanje nestabilnosti instrumenta od
stvarne promjene predmeta ne rješava se računom nego poznavanjem razdoblja.

Drugi zahtjev odnosi se na sadržaj, a ne na postojanost.

**Valjanost** je stupanj u kojem instrument mjeri upravo onaj pojam o kojem
se namjerava zaključivati, a ne neki drugi s kojim je povezan.

Ta su dva svojstva neovisna, što je najlakše vidjeti na primjeru mjere koja ima
jedno bez drugoga. Kvaliteta novinarstva mjerena
brojem zareza u tekstu bila bi izvrsno pouzdana, jer bi svaka dva brojača došla
do istog rezultata, i posve nevaljana. Pouzdanost je nužan uvjet, a ne dovoljan,
i pouzdana mjera može svaki put jednako promašiti cilj.

Nepouzdanost pritom ne ostaje tehnička sitnica nego ulazi u same rezultate, i
to na način koji je važno predvidjeti. Ako mjera uz stvarnu vrijednost bilježi i
slučajnu pogrešku, dio razlika među ispitanicima nastao je od pogreške, a ne od
pojave. Kada dvije takve mjere povežemo, njihova zajednička kretanja moraju se
probiti kroz dva sloja šuma, pa izmjerena veza redovito izgleda slabijom nego
što je veza među samim pojmovima. Loše mjerenje time obično ne izmišlja nalaz
nego ga skriva.

Posljedica je protivna očekivanju, pa je vrijedi izreći izravno. Nalaz da veze
nema slabiji je dokaz nego što se čini kada su mjere nepouzdane, jer je izostanak
veze mogao proizvesti sam instrument. Nalaz da veza postoji unatoč nepouzdanim
mjerama u tom je smislu čvršći, jer je pogreška radila protiv njega. Zbog toga
podatak o pouzdanosti mijenja tumačenje rezultata u oba smjera i ne služi samo
kao potvrda da je posao obavljen uredno.

Valjanost se rastavlja na nekoliko pitanja. Pokriva li instrument sve važne
dijelove pojma, pa upitnik o medijskoj pismenosti koji ne spominje digitalne
sadržaje propušta bitan dio predmeta. Mjeri li instrument doista pojam koji
imenuje, a ne nešto susjedno, jer klikovi, vrijeme na stranici i komentari svi
nose ime angažmana, dok zapravo mjere početni interes, dubinu čitanja i
motivaciju za javno očitovanje. Vrijede li rezultati izvan uvjeta u kojima su
dobiveni, što je pitanje koje se najoštrije postavlja kod laboratorijskih
studija. Reakcija na neistinitu vijest prikazanu na praznom zaslonu ne mora
odgovarati reakciji iste osobe koja isti sadržaj sretne među porukama prijatelja
i obavijestima.

## Treći čimbenik i logika eksperimenta

Varijable u istraživanju nisu ravnopravne. Ona za koju pretpostavljamo da
djeluje naziva se nezavisnom varijablom, a ona koja bilježi ishod zavisnom. U
opažačkim se studijama ista razlika češće izriče kao odnos prediktora i ishoda,
jer ondje istraživač ničim ne manipulira i terminologija manipulacije zavarava.
Nitko ne dodjeljuje ispitanicima dob ni obrazovanje.

Opasnost koja iz toga slijedi glavna je tema ovog poglavlja. Varijabla povezana
i s pretpostavljenim uzrokom i s ishodom može proizvesti privid veze između njih
ili prikriti vezu koja postoji.

**Konfundirajuća varijabla** je varijabla koja je povezana i s
pretpostavljenim uzrokom i s ishodom, pa dio opažene veze među njima potječe
od nje, a ne od djelovanja uzroka na ishod.

Ako podaci pokažu da adolescenti koji više koriste Instagram imaju niže
samopoštovanje, moguće je da korištenje snižava samopoštovanje, da niže
samopoštovanje potiče korištenje ili da društvena izoliranost povećava oboje.
Navarro tu pojavu naziva problemom treće varijable i drži je razlogom zbog kojeg
povezanost ne dokazuje uzročnost (Navarro, 2019).

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
Nijedan postupak ne može iz same tablice pročitati koje varijable pripadaju
objašnjenju, jer se odnosi među stupcima ne razlikuju po tome je li stupac uzrok
ili posljedica. Program može prilagoditi model za dob, obrazovanje ili
prethodno ponašanje tek nakon što netko obrazloži zašto su baš te varijable
važne i kako su izmjerene. Poglavlje o regresiji tu prilagodbu razrađuje
računski, ali odluku o njezinu sadržaju ostavlja ondje gdje je i sada.

Eksperiment je dizajn koji taj problem rješava u korijenu. Istraživač sam
određuje vrijednost nezavisne varijable, jedinice raspoređuje nasumično i sve
ostalo drži jednakim. Nasumična dodjela najvažniji je od ta tri elementa, jer
ne izjednačava skupine samo po obilježjima kojih se istraživač sjetio nego i po
onima koje nije izmjerio ni zamislio. Ako se skupine razlikuju samo po uvjetu
koji smo mi postavili, razlika u ishodu ima samo jedno raspoloživo objašnjenje.
To je jedini dizajn koji kauzalni zaključak nosi po svojoj konstrukciji.

Kako to izgleda u praksi, najlakše je vidjeti na pokusu s dvjema inačicama
poruke. Isti se tekst opremi dvama naslovima, jednim suzdržanim i jednim
zaoštrenim, a čitatelji se nasumično razdijele tako da svaka polovica vidi samo
jedan. Nakon nekog vremena uspoređuje se udio onih koji su tekst otvorili.
Manipulacija je ovdje u tome što naslov dodjeljuje istraživač, a ne čitatelj.
Nasumičnost je u tome što nitko ne bira koju će inačicu vidjeti. Kontrola je u
tome što su tekst, vrijeme objave i položaj na stranici jednaki u obje skupine.

Vrijedi razmisliti što bi se dogodilo da nasumičnosti nema. Ako bi čitatelji
sami birali koji naslov otvaraju, skupina koja bira zaoštrene naslove bila bi
sastavljena od ljudi koji su ionako skloniji takvim sadržajima. Razlika u
otvaranju tada bi mjerila i naslov i sklonost čitatelja, bez ikakva načina da
ih razdvojimo. Upravo je to razlika između pokusa i naizgled sličnog
prikupljanja podataka o tome što ljudi već rade, i ona ne ovisi o količini
podataka nego o načinu na koji su nastali.

Isti nacrt istodobno pokazuje granicu eksperimenta. Mnogo toga što društvene
znanosti zanima ne može se dodijeliti. Nitko ne može nasumično odrediti kome će
pripasti niže obrazovanje, tko će odrastati u siromaštvu ni koliko će godina
netko provoditi uz određenu platformu. Pitanja koja se najviše tiču društvenih
nejednakosti time su sustavno ona na koja najjači dizajn ne može odgovoriti,
zbog čega su opažačke studije u ovim disciplinama pravilo, a ne ustupak.

Stupanj u kojem u to možemo biti sigurni naziva se internom valjanošću, a
prijetnje njoj su sve situacije u kojima se među skupine uvuče neplanirana
sustavna razlika. Vanjski događaj između prvog i drugog mjerenja može
promijeniti ishod neovisno o intervenciji. Nejednako osipanje sudionika po
skupinama iskrivljuje usporedbu, jer preostali sudionici više nisu ono što je
nasumična dodjela stvorila. Sudionici koji naslute svrhu istraživanja mogu se
ponašati u skladu s pretpostavljenim očekivanjem, pa u ispitivanju medijske
pismenosti odgovaraju kritičnije nego što doista jesu.

## Opažačke studije i doseg zaključka

Većina istraživanja u društvenim znanostima nije eksperimentalna, i to iz
razloga koji nije lijenost. Mnoge varijable koje nas zanimaju ne mogu se
dodijeliti. Nikome se ne može nasumično odrediti dohodak, razina obrazovanja,
izloženost siromaštvu ni količina vremena provedena na mrežama tijekom
odrastanja. Ondje gdje bi dodjela bila moguća, često ne bi bila etična.

U opažačkoj studiji istraživač mjeri varijable onakve kakve jesu i analizira
veze među njima. Cijena je poznata i sastoji se u tome da se suparnička
objašnjenja ne mogu razlučiti samim podacima. Negativna veza između korištenja
mreža i političke informiranosti dopušta tri čitanja koja podaci ne razdvajaju,
jer mreže mogu smanjivati informiranost, slabije informirani mogu više
posezati za mrežama, a obrazovanje ili dob mogu oblikovati oboje. Zauzvrat
takva studija promatra pojavu u njezinim prirodnim okolnostima, na velikim i
raznolikim uzorcima, bez ograničenja koja laboratorij nameće.

Između tih krajnosti stoji kvazieksperiment, u kojem se uspoređuju skupine koje
su se razlikovale bez istraživačeva zahvata. Usporedba korisnika koji su
doživjeli curenje podataka s onima koji nisu koristi razliku koju je proizveo
svijet, a ne nacrt istraživanja. Takav dizajn dopušta oprezniju formulaciju, u
kojoj se govori o povezanosti koja opstaje i nakon uzimanja u obzir niza
izmjerenih čimbenika, uz izričito priznanje da neizmjereni čimbenici ostaju
mogući. Na trećem se kraju nalaze studije slučaja i kvalitativni pristupi, koji
daju dubinu i mehanizam, ali ne procjenjuju raširenost. Oni su izvor hipoteza
koje kvantitativni dizajni potom provjeravaju, pa im je odnos komplementaran, a
ne natjecateljski.

Anketa dodaje još jednu razinu dizajna. Formulacija pitanja određuje što
ispitanik razumije, ponuđeni odgovori određuju što smije reći, a **okvir
uzorkovanja** određuje tko uopće može biti izabran. Velik broj odgovora ne
popravlja sustavno izostavljanje dijela populacije. Precizno mjerenje pogrešne
skupine ostaje precizno mjerenje pogrešne skupine, a poglavlje o uzorkovanju
pokazuje zašto se ta pogreška povećanjem uzorka ne smanjuje.

Uz okvir dolazi i pitanje tko je pozvan, a nije odgovorio. Ljudi koji odbijaju
sudjelovanje obično se od sudionika razlikuju upravo po onome što se ispituje,
pa istraživanje o povjerenju u institucije teže dopire do onih koji institucijama
najmanje vjeruju. Ta pojava ne pogađa uzorak nasumično nego pristrano, i zato
je opasnija od običnog smanjenja broja odgovora. Naknadno vaganje odgovora
prema dobi, spolu i obrazovanju popravlja razlike u obilježjima koja su
zabilježena, a razliku u sklonosti odgovaranju ostavlja netaknutom. Podatak o
stopi odgovora zbog toga pripada svakom poštenom izvještaju o anketi jednako
kao i sam rezultat.

Preostaje pitanje koje vrijedi i za najbolje izveden eksperiment. Vrijede li
rezultati izvan okolnosti u kojima su dobiveni. To je pitanje eksterne
valjanosti i postavlja se u tri smjera. Prema populaciji, jer nalaz na
studentima jednog fakulteta ne mora vrijediti za druge dobne skupine ni za
druge sredine. Prema kontekstu, jer se ponašanje u nadziranim uvjetima razlikuje
od ponašanja u svakodnevnoj upotrebi. Prema vremenu, jer se platforme, norme i
navike mijenjaju dovoljno brzo da nalaz od prije nekoliko godina opisuje svijet
kojeg više nema.

Interna i eksterna valjanost pritom su u napetosti. Što je situacija
kontroliranija, to je zaključak o uzroku čvršći i to je manje nalik prilikama u
kojima pojava inače nastaje. Nijedan pojedinačan dizajn ne postiže oboje, pa
najuvjerljiviji nalazi u društvenim znanostima obično dolaze iz niza studija
različitih dizajna koje pokazuju u istom smjeru. Kada čitate jedno istraživanje,
korisnije je pitati koju je od dviju valjanosti platilo nego ga ocjenjivati kao
dobro ili loše u cjelini.

Dizajni se zato najbolje zamišljaju kao raspon, a ne kao ljestvica kvalitete.
Na jednom kraju stoje pokusi, s najviše kontrole i najslabijom sličnošću
svakodnevici. U sredini su kvazieksperimenti i opažačke studije s uzimanjem
drugih čimbenika u obzir, koje kupuju prirodnost po cijenu slabijeg kauzalnog
zaključka. Na drugom su kraju studije slučaja i kvalitativni pristupi, koji
daju mehanizam i jezik za pojavu koju još ne znamo dobro opisati. Pitanje nije
koji je dizajn najbolji nego koji odgovara na pitanje koje smo postavili.

Praksa se u novije vrijeme sve češće oslanja na kombinaciju. Razgovori s manjim
brojem sudionika mogu otkriti koje varijable uopće treba mjeriti, anketa na
velikom uzorku može utvrditi koliko su te veze raširene, a pokus na kraju može
provjeriti smjer djelovanja za nalaz koji se pokazao najvažnijim. Takav redoslijed
ne miješa metode nego ih raspoređuje prema onome što svaka može, i najbliži je
odgovor koji ova disciplina ima na to što ni jedan dizajn ne može sve.

## Interakcija — Prikaz konfundera

Prikaz pokazuje odnos dviju varijabli prije i nakon razlikovanja jedinica prema
trećoj varijabli. Opažanja ostaju ista, ali se mijenja usporedba. Pomak ishoda
povezan s trećom varijablom može zbirnu vezu preokrenuti iako je odnos unutar
obiju podskupina stabilan.

*Slika. Ista opažanja prikazana zbirno i prema trećoj varijabli u konstruiranom primjeru.*

**Što isprobati.**

1. Promatrajte početnu vezu bez treće varijable.
2. Uključite konfundirajuću varijablu i usporedite smjer veze.
3. Promijenite njezinu povezanost s ishodom i pronađite slučaj u kojem se
   početni zaključak preokreće.
4. Postavite tu povezanost na nulu i provjerite razlikuju li se tada dva
   prikaza uopće.

Posljednji korak imenuje uvjet. Dok treća varijabla ne pomiče ishod, oba
prikaza govore isto i njezino uključivanje ništa ne mijenja. Konfundiranje traži
da varijabla bude povezana s objema promatranim veličinama istodobno, a ne samo
da postoji u podacima. Odatle slijedi i praktična posljedica. Popis mogućih
konfundera nije popis svega što je izmjereno, nego kratak popis onoga za što
imamo razlog vjerovati da djeluje na obje strane, i taj razlog dolazi iz teorije,
a ne iz tablice.

**Statistika u divljini.**
**Što mjeri stopa prijma.** Zbirna stopa u Berkeleyju opisivala je ishod
prijava, ali nije sama mjerila namjeru, kriterije odlučivanja ni iskustvo
kandidata (Bickel, 1975). Pretvaranje te stope u potpunu ocjenu pravednosti
preskače operacionalizaciju pojma pravednosti. Pravednost se može
operacionalizirati kao jednak ishod među skupinama, kao jednak postupak prema
jednako kvalificiranim kandidatima ili kao jednaka dostupnost samog odjela, i
te tri mjere u ovim podacima ne daju isti odgovor.

Odgovorno čitanje zato najprije pita koja je jedinica analize i koje su
varijable dostupne. Jedinica su ovdje prijave, a ne osobe, pa kandidat koji se
prijavio na dva odjela ulazi dvaput. Dostupne su varijable ishod, spol i odjel,
dok kvaliteta prijave i savjet primljen prije prijave nisu izmjereni. Tek nakon
toga ima smisla procjenjivati koji dizajn može razlikovati suparnička
objašnjenja, a ovaj skup podataka nastao je bez ikakva dizajna, jer su ga
proizveli sami upisni postupci.

**Pitajte model.**
Asistent može pretvoriti istraživačko pitanje u nacrt varijabli i upozoriti na
moguće konfundere. Njegov popis nije dokaz da su mjere valjane. Treba provjeriti
odgovara li svaka predložena varijabla stvarnom instrumentu, tko nedostaje iz
okvira uzorkovanja i dopušta li dizajn kauzalni zaključak.

Dva su promašaja ovdje osobito česta. Modeli redovito predlažu popis
konfundera koji je dug i uvjerljiv, a pritom ne razlikuju varijable koje
prethode pretpostavljenom uzroku od onih koje su njegova posljedica, iako se
prilagodba za posljedicu ne smije provesti. Uz to skloni su kauzalnom jeziku i
za nacrte koji ga ne podnose, pa opažačku studiju opisuju glagolima poput
utječe ili smanjuje. Provjerite svaku predloženu varijablu prema tome kada
nastaje i preformulirajte svaku rečenicu koja tvrdi djelovanje.

> Za ovo istraživačko pitanje predloži jedinicu analize, način mjerenja ishoda,
> mogući konfundirajući čimbenik i dizajn. Za svaku predloženu varijablu navedi
> nastaje li prije ili poslije pretpostavljenog uzroka. Za svaku odluku navedi
> što se iz prikupljenih podataka neće moći zaključiti.

**Nađite grešku.**
U opažačkoj anketi studenti koji dulje koriste društvene mreže prijavili su
niže povjerenje u institucije. Obje su varijable izmjerene istim upitnikom i
analiza je uključila dob. Rezultat zato dokazuje da dulje korištenje društvenih
mreža smanjuje povjerenje.

Greška je tvrdnja o dokazanom uzroku. Istodobno mjerenje dviju varijabli i
prilagodba za dob ne uklanjaju obrnuti smjer veze ni druge neizmjerene
konfundirajuće čimbenike.

## Razrađeni primjer

Zamislimo istraživanje povjerenja u lokalne institucije. Pojam je apstraktan i
nijedno pitanje ga ne zahvaća samo, pa ga operacionaliziramo s četiri tvrdnje na
istoj ljestvici od 1 do 5. Tri su tvrdnje formulirane potvrdno, tako da viši
odgovor znači više povjerenja. Četvrta je namjerno formulirana niječno, jer se
tako u anketama razbija navika da ispitanik mehanički zaokružuje isti stupac.
Ta odluka o formulaciji vratit će se kao problem u računu.

Prije nego što četiri odgovora spojimo u jedan rezultat, provjeravamo ponašaju
li se doista kao mjere istog pojma. Najjednostavnija provjera uspoređuje svaku
tvrdnju sa zbrojem preostalih. Ako sve mjere isto, svaka bi se trebala kretati
u istom smjeru kao ostatak instrumenta.

*Slika. Povezanost svake tvrdnje s ostatkom instrumenta, prije i nakon okretanja niječne tvrdnje. Izrada autora.*

Tablica odmah pokazuje nepravilnost. Prve tri tvrdnje snažno se slažu s
ostatkom instrumenta, dok četvrta ide u suprotnom smjeru i s ostatkom je
povezana negativno, na razini od `r hr_broj(s2$t4_prije, 2)`. To nije znak da je
tvrdnja loša. To je posljedica njezine niječne formulacije, zbog koje visok
odgovor na njoj znači nisko povjerenje. Ista brojka koja u prve tri tvrdnje
znači povjerenje u četvrtoj znači njegovu odsutnost.

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

Nalaz iz ove dijagnostike vrijedi zapamtiti kao obrazac, jer se sreće i u tuđim
podacima. Stavka koja je s ostatkom instrumenta povezana negativno gotovo je
uvijek niječno formulirana stavka koju je netko zaboravio okrenuti. Prije nego
što se takva tvrdnja proglasi lošom i izbaci, treba pogledati njezin puni tekst.
Ako je tvrdnja niječna, popravak je okretanje, a ne izbacivanje, i instrument
ostaje potpun. Ako tvrdnja nije niječna, a ipak ide protiv ostatka, tada doista
mjeri nešto drugo i pitanje postaje sadržajno.

Ono što je ovim postupkom postignuto ipak treba precizno imenovati. Pokazali smo
da se četiri tvrdnje kreću zajedno, što je dokaz o unutarnjoj dosljednosti
instrumenta. Nismo pokazali da mjere povjerenje. Četiri tvrdnje koje bi sve
mjerile opću sklonost slaganju s bilo čime slagale bi se jednako lijepo i dale
bi jednako urednu tablicu. Dosljednost je nužan uvjet, a valjanost se brani
sadržajem tvrdnji, načinom na koji ih ispitanici razumiju i usporedbom s
mjerama za koje već znamo što znače.

Doseg zaključka na kraju određuje ono što ovdje nije prikazano. Ne znamo tko je
ušao u uzorak ni tko je odbio sudjelovati, ne znamo kako je pitanje glasilo u
punom tekstu i mjerili smo u jednom trenutku. Ta tri podatka ne mijenjaju
nijedan broj u tablici, a mijenjaju sve što o njima smijemo reći. Zbog toga
metodološki odjeljak objavljenog rada nije formalnost nego mjesto na kojem se
odlučuje koliko njegovi rezultati vrijede.

## Sažetak

Mjerenje prevodi teorijske pojave u opažanja, a istraživački dizajn određuje
dokle zaključak smije dosegnuti. Pouzdanost, valjanost i razina mjerenja nisu
tehnički dodatci nakon prikupljanja podataka, nego svojstva odluka donesenih
prije njega, a razrađeni primjer pokazao je da jedna previđena formulacija može
prepoloviti razlike među ispitanicima bez ijedne pogreške u računu. Konfundirajuća
varijabla objašnjava zašto povezanost sama ne nosi uzrok, a nasumična dodjela
zašto pokus taj problem rješava ondje gdje je uopće izvediva. Kako se ta
prilagodba za treće čimbenike provodi računski, pokazuje poglavlje o regresiji.
Sljedeće poglavlje okreće pogled prema tvrdnjama koje sve te odluke skrivaju.

## Pojmovi

operacionalizacija (*operationalization*), varijabla (*variable*), razina
mjerenja (*level of measurement*), pouzdanost (*reliability*), valjanost
(*validity*), konfundirajuća varijabla (*confounder*), interna valjanost
(*internal validity*), eksterna valjanost (*external validity*), okvir
uzorkovanja (*sampling frame*)

## Zadaci

### Konceptualni

Razlikujte pouzdanu mjeru od valjane mjere na vlastitom primjeru. Predajte
objašnjenje u kojem ista mjera može biti pouzdana, ali nevaljana.

Odaberite zatim jedan pojam iz svojeg područja i predložite dvije različite
operacionalizacije istog pojma. Za svaku navedite što zahvaća i što izostavlja
te opišite nalaz koji bi jedna proizvela, a druga ne bi.

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
dizajnu pripada. Predajte odlomak u kojem imenujete dizajn, navodite jedan
zaključak koji taj dizajn nosi i jedan koji autori izvode šire nego što dizajn
dopušta.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte dizajn, prepoznajte jednu
neopravdanu tvrdnju i napišite inačicu koja poštuje ograničenja dizajna. Uz
ispravak navedite koji bi dizajn bio potreban da izvorna tvrdnja postane
opravdana i zašto taj dizajn ovdje vjerojatno nije izvediv.

---

# Kako brojke zavode

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | Istraživač margine pogreške | simulacija | pogl. 1 i 2 |

**Vinjeta.**
Američko statističko udruženje objavilo je izjavu o p-vrijednostima nakon
desetljeća u kojima se jedan prag često koristio kao zamjena za znanstveni sud
(Wasserstein, 2016). Problem nije bio u tome što su istraživači zaboravili
računati. Problem je nastajao kada je jedan broj preuzimao značenje koje mu
postupak nije davao.

Sličan prijenos značenja događa se u naslovima anketa, postocima bez nazivnika
i grafovima kojima odabrani raspon osi pretvara malu promjenu u dramatičan lom.
Broj može biti točan, a prikaz ipak voditi prema zaključku koji podaci ne nose.

Kako razlikovati računsku pogrešku od mnogo češće pogreške u okviru, usporedbi
i jeziku?

## Četiri provjere jedne tvrdnje

Prva provjera traži izvor. Tvrdnja koja navodi istraživanje mora omogućiti
pronalaženje izvornog izvještaja, tablice ili skupa podataka. Poveznica na
drugi članak nije podrijetlo brojke, a navođenje ustanove bez godine i
istraživanja nije dovoljno da bi se nalaz provjerio.

Druga provjera traži nazivnik. Porast od pedeset posto može značiti prijelaz s
dva slučaja na tri ili s dva milijuna na tri milijuna. Postotak opisuje omjer,
dok **postotni bod** opisuje razliku između dvaju postotaka. Njihova zamjena
može višestruko povećati dojam promjene iako je aritmetika pojedinačnih brojeva
točna.

Treća provjera traži usporedbu. Graf bez zajedničke nule nije automatski
nepošten, ali skraćena os mora biti vidljiva i opravdana. Odabir početnog
razdoblja, izostavljanje jedne skupine ili isticanje samo povoljnog ishoda
mijenja priču. Čitatelj zato pita koje bi razumno drugačije uokvirivanje
pokazalo isti podatak.

Četvrta provjera traži neizvjesnost. Rezultat ankete nije svojstvo uzorka koje
će se bez promjene ponoviti u populaciji. Margina pogreške opisuje samo
uzoračku promjenjivost pod određenim pretpostavkama. Ne obuhvaća pristran
okvir, neodaziv, loše pitanje ni naknadno biranje najzanimljivijeg rezultata.

## Protokol skeptičnog čitanja

Skeptičnost nije automatsko odbacivanje. Ona usporava prijelaz od podatka prema
tvrdnji. Najprije utvrđujemo tko je proizveo broj i za koju svrhu. Zatim
provjeravamo jedinicu analize, nazivnik, vremenski okvir i usporednu skupinu.
Tek tada procjenjujemo koliko neizvjesnost i dizajn dopuštaju zaključak.

Isti protokol vrijedi za ljudski i strojno proizveden tekst. Asistent može
izmisliti izvor, popuniti ćeliju koja nedostaje ili zaokružiti rezultat do
lažne preciznosti. Uvjerljiv stil nije dokaz podrijetla. Svaka brojka mora
ostaviti trag do podataka ili postupka iz kojeg je nastala.

## Interakcija — Istraživač margine pogreške

Istraživač prikazuje približnu marginu pogreške uzorka pri različitim
veličinama i procijenjenim udjelima. Zaseban klizač uvodi poznatu sustavnu
pristranost. Interval se tada može sužavati oko precizno procijenjene pogrešne
vrijednosti.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

**Statistika u divljini.**
**Prag koji nije presuda.** Izjava Američkog statističkog udruženja naglasila
je da p-vrijednost sama ne mjeri veličinu ni važnost učinka i ne određuje treba
li rezultat smatrati znanstveno vrijednim (Wasserstein, 2016).

Naslov koji istraživanje svodi na „dokazano" ili „nije dokazano" uklanja
procjenu, neizvjesnost i dizajn. Broj ostaje vidljiv, a upravo informacije
potrebne za njegovo tumačenje nestaju.

**Pitajte model.**
Asistent je koristan kao strogi čitatelj ako dobije izvornu tablicu i jasnu
zabranu nadopunjavanja nedostajućih podataka. Treba tražiti da odvoji provjeru
aritmetike od procjene dizajna i jezika. Nakon odgovora ručno se otvara svaki
navedeni izvor i provjerava postoji li broj u njemu.

> Rastavi ovu statističku tvrdnju na izvor, brojnik, nazivnik, usporedbu,
> neizvjesnost i dopušten zaključak. Ne dopunjuj podatke koji nisu priloženi i
> jasno označi što nije moguće provjeriti.

**Nađite grešku.**
Anketa pokazuje vodstvo jedne opcije, ali se intervali procjena dviju opcija
preklapaju. Zbog preklapanja možemo zaključiti da među njima sigurno nema
razlike. Uzorak je opisan, a postoci se zbrajaju do cjeline.

Greška je zaključak da preklapanje intervala dokazuje nepostojanje razlike.
Odnos dviju procjena mora se procijeniti izravno, uz dizajn ankete i ovisnost
procjena, a ne samo pogledom na dva odvojena intervala.

## Razrađeni primjer

Simuliramo dvije ankete o istoj podršci, jednu s manjim i jednu s većim
uzorkom. Obje su pošteno uzorkovane iz iste zamišljene populacije. Cilj nije
dobiti stvarni izborni rezultat, nego vidjeti što se mijenja kada povećamo broj
opažanja.

*Slika. Simulirane procjene pri dvjema veličinama uzorka. Izrada autora.*

Veći uzorak daje užu marginu, ali obje ankete dijele pretpostavku da je
uzorkovanje nepristrano. Kada bi okvir isključio dio populacije, tablica bi i
dalje mogla pokazivati veliku računsku preciznost. Strog prikaz zato uz marginu
navodi način odabira ispitanika, datum, formulaciju pitanja i naručitelja.

## Sažetak

Brojke zavode kada izgube izvor, nazivnik, usporedbu ili neizvjesnost. Pogreška
ne mora biti u računu jer često nastaje u izboru prikaza i jezika kojim se
rezultat pretvara u tvrdnju. Skeptični protokol jednak je za novinski naslov,
znanstveni sažetak i odgovor modela. U sljedećem dijelu knjige isti se zahtjev
primjenjuje na sažimanje i vizualizaciju vlastitih podataka.

## Pojmovi

nazivnik (*denominator*), postotni bod (*percentage point*), margina pogreške
(*margin of error*), pristranost (*bias*), lažna preciznost (*false
precision*), podrijetlo podatka (*data provenance*)

## Zadaci

### Konceptualni

Objasnite razliku između pedesetpostotnog rasta i rasta od pedeset postotnih
bodova. Predajte vlastiti primjer bez stvarnih empirijskih tvrdnji.

### Računski

Upotrijebite simulirane podatke `sim_ankete`. Dodajte treću veličinu uzorka i
predajte tablicu s pripadajućom marginom pogreške.

### Kritički

Pročitajte izjavu o p-vrijednostima i izdvojite jednu tvrdnju koju ona
dopušta te jednu koju izričito ne dopušta (Wasserstein, 2016). Predajte dvije
rečenice i citat izvora.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Odvojite točne provjere od jedne
pogrešne interpretacije i napišite provjerljiviju zamjenu.
