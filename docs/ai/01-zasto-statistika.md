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
