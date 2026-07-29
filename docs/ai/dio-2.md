# DIO II: OPISIVANJE PODATAKA

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Sažimanje podataka

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Tukey je istraživačku analizu podataka postavio kao postupak u kojem sažetak
otvara pitanja umjesto da ih zatvara (Tukey, 1977). Isti prosjek može pripadati
zbijenoj skupini sličnih opažanja ili raspodjeli u kojoj se većina nalazi
daleko od nekoliko ekstremnih vrijednosti. Broj je u oba slučaja pravilno
izračunat, ali iskustvo tipičnog opažanja nije isto.

U društvenim podacima takva razlika mijenja zaključak. Prosječno vrijeme,
prihod ili broj dijeljenja može snažno povući mala skupina iznimnih slučajeva.
Medijan će ostati stabilniji, ali će zauzvrat zanemariti koliko su ti slučajevi
daleko od sredine.

Koji sažetak čuva ono što je važno u raspodjeli, a što pritom skriva?

## Središte i raspodjela

**Aritmetička sredina** raspoređuje ukupan zbroj ravnomjerno na sva opažanja.
Zato koristi svaku vrijednost i zato je osjetljiva na krajnosti. **Medijan**
traži srednje mjesto nakon poredavanja. On se manje mijenja kada se jedno
opažanje udalji, ali ne govori koliko je udaljeno. Mod opisuje najčešću
vrijednost ili kategoriju i osobito je koristan kada prosjek uopće nema
sadržajno značenje.

Mjera središta ne opisuje koliko se opažanja razlikuju. Dvije skupine mogu
imati jednaku sredinu, a jedna može biti gotovo jednolična dok druga pokriva
širok raspon. Raspon koristi samo krajeve. Interkvartilni raspon prati srednju
polovinu raspodjele. Standardna devijacija opisuje tipičnu udaljenost od
aritmetičke sredine i zbog toga se mijenja zajedno s ekstremnim vrijednostima.

Izbor se ne svodi na pitanje koja je mjera najbolja. Sredina i raspršenost
moraju odgovarati obliku podataka i tvrdnji koju želimo poduprijeti. Kada je
raspodjela asimetrična, medijan i interkvartilni raspon često bolje opisuju
tipično opažanje. Kada je približno simetrična, sredina i standardna devijacija
zajedno daju sadržajan prikaz.

## Položaj unutar skupine

Ponekad nas ne zanima samo sirova vrijednost, nego njezin položaj u odnosu na
druge. **Standardizirana vrijednost** izražava koliko je standardnih devijacija
opažanje udaljeno od sredine. Time vrijednosti na različitim ljestvicama
prevodimo na zajednički jezik položaja, ali ne uklanjamo nepravilnosti
raspodjele.

Desno asimetrični podaci često nastaju kada nekoliko slučajeva može biti vrlo
veliko, dok je donja granica prirodna. Logaritamska transformacija sabija veće
vrijednosti i može učiniti omjere vidljivijima. Ona nije popravak za svaki
neugodan graf. Promijenjena ljestvica mijenja pitanje, pa interpretacija mora
govoriti o razmjernim, a ne apsolutnim razlikama.

## Interakcija — Oblikovanje distribucije

Planirani oblikovatelj raspodjele dopušta pomicanje pojedinačnih točaka i
odmah pokazuje reakciju sredine, medijana i mjera raspršenosti. Tako postaje
vidljivo koje mjere slušaju svako opažanje, a koje prvenstveno čuvaju redoslijed.

**Što isprobati.**

1. Pomaknite jednu središnju točku i usporedite sredinu s medijanom.
2. Udaljite jednu krajnju točku bez mijenjanja redoslijeda.
3. Oblikujte dvije raspodjele iste sredine, ali različite raspršenosti.

**Statistika u divljini.**
**Prosjek kao početak pregleda.** Tukey je zagovarao istraživački pristup u
kojem se podaci pregledavaju iz više kutova prije konačnog modeliranja
(Tukey, 1977). Izvještaj koji navodi samo prosjek uklanja upravo oblik koji bi
mogao objasniti zašto taj prosjek nije tipičan.

Odgovorna tablica zato uparuje mjeru središta s mjerom raspršenosti i brojem
opažanja. Graf zatim pokazuje asimetriju, praznine i krajnje slučajeve koje tri
sažetka ne mogu nositi.

**Pitajte model.**
Asistent može izraditi tablicu sažetaka, ali mu treba zatražiti broj valjanih
opažanja i postupanje s nedostajućim vrijednostima. Treba provjeriti računa li
svaku skupinu iz ispravnog podskupa i je li za asimetričnu raspodjelu ponudio
mjeru koja opisuje tipično opažanje.

> Sažmi svaku skupinu brojem opažanja, prikladnom mjerom središta i prikladnom
> mjerom raspršenosti. Obrazloži izbor nakon pregleda oblika raspodjele i
> prikaži koliko vrijednosti nedostaje.

**Nađite grešku.**
Raspodjela broja dijeljenja izrazito je desno asimetrična. Medijan i
interkvartilni raspon zato opisuju tipičnu objavu. Budući da je medijan otporan
na krajnje vrijednosti, takve vrijednosti možemo ukloniti prije svake daljnje
analize.

Greška je automatsko uklanjanje krajnjih vrijednosti. Otpornost medijana
objašnjava njegovu stabilnost, ali ne određuje jesu li krajnji slučajevi
pogreške, legitimna opažanja ili predmet istraživanja.

## Razrađeni primjer

Simulirani niz predstavlja angažman objava. Jedna objava privukla je mnogo više
reakcija od ostalih. Usporedba sredine i medijana pokazuje kako taj slučaj
mijenja pojam tipične objave, dok interkvartilni raspon opisuje središnji dio
raspodjele.

*Slika. Sažeci simulirane raspodjele angažmana. Izrada autora.*

Nijedan sažetak nije pogrešan. Sredina odgovara na pitanje o ravnomjernoj
raspodjeli ukupnog angažmana, a medijan o položaju srednje objave. Izvještaj
treba imenovati pitanje i pokazati raspodjelu kako čitatelj ne bi morao
nagađati koje značenje nosi riječ „prosječno".

## Sažetak

Sažetak je odluka o tome koji dio raspodjele čuvamo u malom broju vrijednosti.
Mjera središta bez raspršenosti ostavlja pola priče neispričanom, a obje zajedno
još ne pokazuju oblik. Standardizacija opisuje položaj, dok transformacija
mijenja ljestvicu i traži novu interpretaciju. Sljedeće poglavlje zato podatke
vraća u prostor i pokazuje kako graf postaje dio argumenta.

## Pojmovi

aritmetička sredina (*mean*), medijan (*median*), interkvartilni raspon
(*interquartile range*), standardna devijacija (*standard deviation*),
standardizirana vrijednost (*z-score*), asimetrija (*skewness*)

## Zadaci

### Konceptualni

Predvidite kako će se sredina, medijan i interkvartilni raspon promijeniti kada
jedno najveće opažanje dodatno poraste. Predajte obrazloženje bez računanja.

### Računski

Upotrijebite `sim_angazman`. Izračunajte sažetke prije i nakon uklanjanja
najveće vrijednosti te predajte jednu usporednu tablicu.

### Kritički

Objasnite zašto istraživačka analiza ne završava jednom mjerom središta
(Tukey, 1977). Predajte popis triju dodatnih provjera u punim rečenicama.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dobar izbor sažetka, jednu
neopravdanu odluku i postupak kojim biste je provjerili.

---

# Vizualizacija kao argument

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

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

## Graf kao usporedba

Graf nije slika dodana nakon analize. On bira što će se uspoređivati položajem,
duljinom, površinom ili bojom. Položaj na zajedničkoj osi obično dopušta
precizniju usporedbu od površine kruga ili nagiba trodimenzionalnog stupca.
Izbor geometrije zato je izbor načina na koji će čitatelj vidjeti razliku.

Dobra vizualizacija počinje tvrdnjom. Za raspodjelu jedne brojčane varijable
treba prikaz koji čuva oblik. Za usporedbu kategorija treba zajednička početna
točka. Za odnos dviju brojčanih varijabli treba sačuvati pojedinačna opažanja.
Graf koji ne odgovara pitanju može biti uredan i potpuno neinformativan.

Gramatika grafike odvaja podatke, estetska svojstva, geometriju i koordinatni
sustav (Wickham, 2016). Ta ideja vrijedi i bez pisanja koda. Omogućuje da
svaku odluku pregledamo zasebno i pitamo prenosi li značenje ili samo dekorira.

## Poštena vidljivost

Osi određuju koliko će promjena zauzeti prostora. Skraćena os može biti
opravdana kada želimo vidjeti male razlike, ali prekid mora biti vidljiv, a
tvrdnja ne smije glumiti promjenu od nule. Kod stupaca je zajedničko ishodište
posebno važno jer duljina nosi značenje. Kod linijskog grafa raspon može
slijediti podatke, ali vremenski i sadržajni kontekst moraju ostati čitljivi.

Mala višestruka polja ponavljaju isti graf za skupine i time čuvaju zajedničku
ljestvicu. Ona često pokazuju heterogenost koju jedna prosječna linija skriva.
Pristupačnost traži dodatni korak. Boja ne smije biti jedini nosač značenja,
tekst mora opisati uzorak, a graf treba preživjeti crno-bijeli tisak.

## Interakcija — Isti podaci, četiri grafa

Planirana interakcija prikazuje iste podatke četirima geometrijama. Promjena
grafa ne mijenja opažanja, ali mijenja usporedbu koja postaje laka ili teška.
Čitatelj tako bira prikaz prema tvrdnji, a ne prema dojmu atraktivnosti.

**Što isprobati.**

1. Odaberite prikaz za usporedbu veličine kategorija.
2. Promijenite raspon osi bez promjene podataka.
3. Isključite boju i provjerite ostaje li značenje čitljivo.

**Statistika u divljini.**
**Četiri jednaka sažetka.** Anscombeov kvartet pokazuje da jednake sredine,
standardne devijacije i korelacije ne jamče jednaku strukturu podataka
(Anscombe, 1973). Raspršeni dijagram odmah razdvaja linearnost, zakrivljenost i
utjecaj izdvojenog opažanja.

Pouka nije da brojeve zamijenimo slikom. Tablica i graf provjeravaju različite
dijelove iste tvrdnje. Njihovo neslaganje razlog je za novu analizu, ne za
odabir prikaza koji nam se više sviđa.

**Pitajte model.**
Asistent može predložiti geometriju i napisati alt-tekst, ali treba dobiti
pitanje koje graf mora odgovoriti. Nakon izrade provjeravamo zajedničke osi,
nazive jedinica, redoslijed kategorija i nosi li boja značenje koje nestaje u
tisku. Modeli često dodaju ukrase koji povećavaju gustoću, a ne razumijevanje.

> Predloži najjednostavniji graf za ovu tvrdnju. Obrazloži koja usporedba nosi
> zaključak, navedi potrebnu ljestvicu i napiši alt-tekst bez tumačenja koje
> podaci ne podupiru.

**Nađite grešku.**
Graf prikazuje udjele triju kategorija stupcima na zajedničkoj osi koja počinje
od nule. Kategorije su jasno označene i vrijednosti su ispisane. Za veći dojam
razlike treću kategoriju treba prikazati širom od ostalih.

Greška je različita širina stupca. Površina tada dodaje drugo vizualno značenje
i pojačava razliku koja bi trebala biti kodirana samo duljinom.

## Razrađeni primjer

Podaci `anscombe` ugrađeni su u R i reproduciraju objavljeni kvartet
(Anscombe, 1973). Sažeci četiriju parova gotovo su jednaki. Raspršeni prikazi
zato nose dio analize koji tablica ne može sačuvati.

*Slika. Anscombeov kvartet — jednaki sažeci, različiti oblici. Izrada autora prema @anscombe1973.*

Prvi skup približno odgovara linearnoj priči. Drugi traži zakrivljeni opis.
Treći i četvrti pokazuju koliko jedno opažanje može određivati pravac.
Zaključak zato ne glasi da je korelacija beskorisna. Glasi da se brojčani
sažetak čita uz prikaz strukture iz koje je nastao.

## Sažetak

Vizualizacija kodira usporedbe i zato pripada argumentu, a ne ukrasu. Izbor
geometrije, ljestvice i podjele na skupine određuje koji obrazac postaje
vidljiv. Pošten graf čuva kontekst, ostaje čitljiv bez boje i ne dodjeljuje
vizualnu težinu bez podatkovnog značenja. Sljedeće poglavlje iz tog prikaza
izdvaja mjeru povezanosti i ispituje što ona može sažeti.

## Pojmovi

geometrija grafa (*geom*), ljestvica (*scale*), mala višestruka polja (*small
multiples*), pristupačnost (*accessibility*), alt-tekst (*alternative text*),
utjecajno opažanje (*influential observation*)

## Zadaci

### Konceptualni

Odaberite graf za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Predajte tri izbora s obrazloženjem.

### Računski

Upotrijebite ugrađene podatke `anscombe`. Izračunajte iste sažetke za sva
četiri skupa i predajte ih uz jednu zajedničku sliku (Anscombe, 1973).

### Kritički

Prosudite što Anscombeov kvartet pokazuje, a što ne pokazuje o ulozi korelacije
(Anscombe, 1973). Predajte odlomak s jednom dopuštenom i jednom pretjeranom
tvrdnjom.

### Revizija modela

Ocijenite prijedlog modela iz okvira. Imenujte točne elemente grafa, jednu
obmanjujuću odluku i način njezina popravka.

---

# Povezanost

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Anscombeova četiri skupa imaju gotovo jednaku Pearsonovu korelaciju, iako
njihovi grafovi prikazuju različite odnose (Anscombe, 1973). Analitičar koji je
dobio samo koeficijent mogao je uredno izvijestiti o smjeru i jačini linearne
veze, a ipak propustiti zakrivljenost ili jedno opažanje koje određuje cijeli
rezultat.

Korelacija je bila točno izračunata. Nije pogriješila u računu, nego je sažela
samo jedan aspekt odnosa. Poteškoća je nastala kada je taj sažetak pročitan kao
potpuna slika.

Što koeficijent povezanosti čuva, a koje odnose ostavlja izvan kadra?

## Zajedničko kretanje

Dvije su varijable povezane kada se njihov raspored mijenja zajedno. Pozitivna
veza znači da se veće vrijednosti jedne češće pojavljuju uz veće vrijednosti
druge. Negativna veza spaja veće vrijednosti jedne s manjima druge. Slaba
linearna veza ne znači da odnosa nema jer zakrivljeni obrazac može imati
koeficijent blizu nule.

**Kovarijanca** prati zajedničko odstupanje od sredina, ali zadržava jedinice
obiju varijabli. Pearsonova korelacija standardizira taj odnos pa se kreće na
zajedničkoj ljestvici. Ona opisuje smjer i jačinu linearnog odnosa. Spearmanova
korelacija radi s rangovima i zato bolje podnosi monotone odnose i dio krajnjih
vrijednosti.

Koeficijent se uvijek čita uz raspršeni dijagram. Graf otkriva je li odnos
linearan, stvaraju li skupine lažni oblak i određuje li jedno opažanje nagib.
Matrica korelacija može sažeti mnogo parova, ali ne zamjenjuje pregled
najvažnijih odnosa.

## Granice jednog broja

Ograničenje raspona slabi korelaciju jer iz uzorka uklanja dio varijacije koja
je nosila odnos. U skupini u kojoj su svi vrlo slični teško je vidjeti obrazac
koji postoji u široj populaciji. Miješanje različitih podskupina može učiniti
suprotno i proizvesti odnos koji se unutar svake skupine smanji ili preokrene.

Povezanost ne određuje smjer uzroka. Varijabla može utjecati na drugu, smjer
može biti obrnut, obje može oblikovati treći čimbenik, a uzorak može nastati
slučajno. Statistička kontrola sužava neke mogućnosti tek uz uvjerljiv dizajn i
sadržajno obrazloženje.

## Interakcija — Pogodi korelaciju

Planirana igra prikazuje raspršene oblake bez koeficijenta i traži procjenu
smjera i jačine. Nakon odgovora otkriva broj i pokazuje primjere u kojima
ljudsko oko ili Pearsonov sažetak propuštaju nelinearnost i podskupine.

**Što isprobati.**

1. Procijenite znak jasnog linearnog odnosa.
2. Usporedite zbijeni i raspršeni oblak istog nagiba.
3. Pronađite nelinearni odnos kojem je Pearsonova korelacija blizu nule.

**Statistika u divljini.**
**Ista korelacija, različita struktura.** Anscombeov kvartet pokazuje četiri
skupa s gotovo jednakim koeficijentom, ali samo jedan približno odgovara
jednostavnom linearnom sažetku (Anscombe, 1973).

Tvrdnja o „snažnoj povezanosti" zato treba graf, opis uzorka i provjeru
utjecajnih opažanja. Koeficijent je koristan sažetak nakon tih provjera, a ne
zamjena za njih.

**Pitajte model.**
Asistent može izračunati Pearsonovu i Spearmanovu korelaciju i opisati graf.
Treba mu zatražiti provjeru linearnosti, krajnjih vrijednosti, podskupina i
ograničenja raspona. Nakon odgovora valja provjeriti jesu li redovi u dvjema
varijablama ispravno upareni i je li iz povezanosti izveden nedopušten uzrok.

> Usporedi Pearsonovu i Spearmanovu korelaciju, opiši oblik raspršenog
> dijagrama i provjeri utjecaj krajnjih opažanja. Zaključak ograniči na
> povezanost koju dizajn podupire.

**Nađite grešku.**
Raspršeni dijagram pokazuje pozitivan približno linearan odnos bez izdvojenih
točaka, a Pearsonov i Spearmanov koeficijent slični su. Zbog toga veća
vrijednost prve varijable uzrokuje porast druge.

Greška je kauzalni zaključak. Slaganje dvaju koeficijenata i uredan graf
podupiru opis povezanosti, ali ne određuju vremenski smjer ni isključuju treće
varijable.

## Razrađeni primjer

Ponovno koristimo `anscombe`, sada usmjereni na ono što koeficijent čuva.
Računamo Pearsonovu korelaciju za svaki skup i stavljamo je uz opis obrasca.
Rezultati su gotovo jednaki, dok graf iz prethodnog poglavlja pokazuje da su
mehanizmi odnosa različiti (Anscombe, 1973).

*Slika. Pearsonove korelacije Anscombeova kvarteta. Izrada autora prema @anscombe1973.*

Tablica potvrđuje da je Pearsonova korelacija vjerna linearnom sažetku koji je
izračunala. Ne potvrđuje da je linearni sažetak prikladan za svaki skup.
Ispravan izvještaj zato spaja koeficijent, graf, broj opažanja i ograničenje
dizajna.

## Sažetak

Korelacija sažima smjer i jačinu određenog oblika zajedničkog kretanja. Graf
otkriva linearnost, podskupine, ograničenje raspona i utjecajna opažanja koja
jedan koeficijent ne može nositi. Pearsonov i Spearmanov pristup odgovaraju na
različita pitanja, a nijedan sam ne dokazuje uzrok. Sljedeći dio knjige uvodi
vjerojatnost kako bismo razlikovali stabilan obrazac od onoga što može nastati
običnom promjenjivošću.

## Pojmovi

kovarijanca (*covariance*), Pearsonova korelacija (*Pearson correlation*),
Spearmanova korelacija (*Spearman correlation*), linearnost (*linearity*),
ograničenje raspona (*range restriction*), utjecajno opažanje (*influential
observation*)

## Zadaci

### Konceptualni

Nacrtajte dva različita odnosa koja mogu imati sličnu Pearsonovu korelaciju.
Predajte skicu i objašnjenje onoga što se u koeficijentu gubi.

### Računski

Upotrijebite `anscombe`. Izračunajte Pearsonovu i Spearmanovu korelaciju za
svaki skup te predajte usporednu tablicu (Anscombe, 1973).

### Kritički

Prosudite tvrdnju da jednaka korelacija znači jednaku podatkovnu priču.
Upotrijebite Anscombeov kvartet kao provjeru (Anscombe, 1973).

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte točne dijagnostičke provjere,
jedan nedopušten zaključak i dizajn koji bi ga mogao bolje poduprijeti.
