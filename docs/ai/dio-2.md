# DIO II: OPISIVANJE PODATAKA

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Sažimanje podataka

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 21 min | Oblikovanje distribucije | simulirana anketa | pogl. 1 do 3 |

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

## Mjere središta

Ostatak poglavlja radi na simuliranoj anketi o korištenju društvenih mreža sa
`r s4$n` ispitanika, koja bilježi dob, dnevno vrijeme korištenja u minutama i
povjerenje u sadržaj na ljestvici od 1 do 10. Uzorak je proizveden kodom uz
fiksno sjeme i ne opisuje nijednu stvarnu populaciju. Koristan je zato što ima
oblik koji mjere medijskog angažmana redovito imaju, pa se na njemu vidi kako
se sažeci ponašaju kada raspodjela nije simetrična.

Prosjek raspoređuje ukupno izmjereno vrijeme ravnomjerno na sve ispitanike. Ako
svakome pripišemo jednak dio zajedničkog zbroja, svaki dobiva upravo
aritmetičku sredinu. Zapis te operacije koristi $n$ za broj opažanja u uzorku i
$x_i$ za vrijednost izmjerenu kod pojedinog ispitanika, a crta nad slovom kaže
da je riječ o sredini tih vrijednosti.

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

**Aritmetička sredina** je zbroj svih izmjerenih vrijednosti podijeljen njihovim
brojem.

Sredina našeg uzorka iznosi `r hr_broj(s4$sredina, 1)` minuta dnevno. Brojka
zvuči kao opis tipičnog ispitanika, a nije, jer više vremena od nje provodi
samo `r paste0(hr_broj(s4$iznad, 0), " %")` ljudi u uzorku. Sredina koristi
svaku vrijednost i zato je najinformativnija mjera središta, ali ta joj
osjetljivost istodobno dopušta da je nekoliko krajnjih slučajeva odvuče iznad
gotovo svih opažanja.

Kompromis između pune sredine i mjere koja krajnosti ignorira nudi **skraćena
sredina** (*trimmed mean*), koja odbacuje zadani postotak najmanjih i najvećih
vrijednosti pa prosjek računa iz ostatka. Uz odbacivanje po 5 % sa svake
strane naš prosjek pada na `r hr_broj(s4$skracena5, 1)` minuta, a uz 10 %
na `r hr_broj(s4$skracena10, 1)`. Navarro upozorava da se ta mjera u
objavljenim istraživanjima pojavljuje iznenađujuće rijetko iako je u mnogim
situacijama primjerenija od obične sredine (Navarro, 2019).

Skraćivanje dovedeno do kraja daje medijan. Ono što medijan čini drukčijim nije
samo otpornost, nego pitanje na koje odgovara. Sredina je vrijednost koja
minimizira zbroj kvadriranih odstupanja i zato velikim odstupanjima daje veliku
težinu, dok medijan minimizira zbroj apsolutnih odstupanja i sva odstupanja
tretira jednako.

**Medijan** je vrijednost koja poredani niz opažanja dijeli na dvije jednako
velike polovine.

Medijan našeg uzorka iznosi `r hr_broj(s4$medijan, 0)` minuta i time za
sredinom zaostaje `r hr_broj(s4$sredina - s4$medijan, 1)` minuta. Razlika između
dviju mjera time postaje brza dijagnostika oblika, jer sredina veća od medijana
upućuje na rep prema većim vrijednostima. Mod opisuje najčešću vrijednost i za
neprekinuto vrijeme korištenja nije koristan, ali za povjerenje mjereno cijelim
brojevima jest, gdje najčešći odgovor iznosi
`r hr_broj(s4$mod_povjerenja, 0)`. Za kategorije poput dobne skupine mod je
jedina mjera središta koja ima značenje, jer prosjek kategorija ne postoji.

## Mjere raspršenosti

Znati gdje se opažanja grupiraju tek je pola opisa. Dva medijska portala mogu
imati jednak prosječan broj komentara po članku, a na prvome svaki članak
dobiva između 45 i 55 komentara dok na drugome neki prolaze bez ijednoga, a
poneki skupe 200. Prosjek ne razlikuje te dvije situacije, a čitatelju su
potpuno različite.

Najjednostavniji odgovor je raspon, razlika između najveće i najmanje
izmjerene vrijednosti. U našem uzorku vrijeme korištenja ide od
`r hr_broj(s4$najmanje, 0)` do `r hr_broj(s4$najvise, 0)` minuta, pa raspon
iznosi `r hr_broj(s4$raspon, 0)` minuta. Ta brojka ima istu slabost kao
sredina, samo izraženiju, jer ovisi isključivo o dva najekstremnija opažanja i
sve ostale zanemaruje.

Sadržajnija mjera polazi od udaljenosti pojedinog opažanja od sredine. Tu
udaljenost nazivamo odstupanjem, a njezinu veličinu bez obzira na smjer daje
apsolutna vrijednost. Prosječno apsolutno odstupanje zato ima izravno čitljivo
značenje, jer kaže koliko se tipičan ispitanik razlikuje od sredine.

$$
\text{PAO} = \frac{1}{n} \sum_{i=1}^{n} |x_i - \bar{x}|
$$

Za naše podatke ta mjera iznosi `r hr_broj(s4$aad, 1)` minuta. Statistika je
ipak krenula drugim putem, jer apsolutna vrijednost nije diferencijabilna u
nuli i otežava izvođenje svega što na raspršenosti počiva. Kvadriranje
odstupanja daje matematički ugodniju veličinu po cijeni izgubljene
neposrednosti, a rezultat te zamjene je varijanca.

**Varijanca** je prosjek kvadriranih odstupanja opažanja od aritmetičke
sredine, uz djelitelj umanjen za jedan.

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

Umanjeni djelitelj u tom izrazu nije sitnica i naziva se Besselovom
korekcijom. Slijedi iz toga što odstupanja mjerimo od sredine izračunane iz
istih tih podataka. Sredina uzorka po definiciji leži najbliže vlastitim
opažanjima, bliže nego što bi im ležala prava sredina populacije, pa su
odstupanja od nje sustavno premala. Dijeljenje s $n$ zato bi dalo procjenu koja
u prosjeku podcjenjuje raspršenost u populaciji, a umanjeni djelitelj tu
pristranost uklanja.

Razlika između uzorka i populacije od ovog mjesta ulazi i u zapis. Statistike
izračunane iz uzorka nose latinična slova, pa je sredina uzorka $\bar{x}$ a
njegova varijanca $s^2$. Nepoznate vrijednosti koje opisuju populaciju nose
grčka slova, pa je populacijska sredina $\mu$ a populacijska varijanca
$\sigma^2$. Broj opažanja u uzorku ostaje $n$, a slovo $N$ knjiga zadržava za
veličinu populacije.

Navarro otvoreno kaže da je upravo ovaj korak jedno od najtežih mjesta uvodnog
kolegija (Navarro, 2019). Puni se argument ne može izvesti prije nego što
postoji pojam raspodjele uzorkovanja, pa procjena koja u prosjeku pogađa pravu
vrijednost ovdje ostaje tvrdnja, a ne pokazana činjenica. Poglavlje o
uzorkovanju vraća se na nju i pokazuje je simulacijom.

Varijanca našeg uzorka iznosi `r hr_broj(s4$varijanca, 1)`. Broj je velik i
gotovo neupotrebljiv u izvještaju, jer kvadriranje nosi i mjernu jedinicu, pa
je rezultat izražen u kvadriranim minutama. Kvadriranje istodobno objašnjava
zašto je varijanca osjetljiva na krajnje slučajeve, budući da odstupanje
dvostruko veće od drugoga u zbroj ulazi četverostruko.

## Standardna devijacija i kvartili

Korijen varijance vraća mjeru u jedinice u kojima su podaci izmjereni i time
je čini čitljivom.

**Standardna devijacija** je korijen varijance, pa raspršenost izražava u
istim jedinicama kao izmjerene vrijednosti.

$$
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

Standardna devijacija našeg uzorka iznosi `r hr_broj(s4$sd, 1)` minuta, dakle
nešto više od prosječnog apsolutnog odstupanja od `r hr_broj(s4$aad, 1)`
minuta. Taj je odnos pravilo, ne slučajnost, jer kvadriranje pojačava velika
odstupanja pa ih standardna devijacija nosi teže. Zbog toga se standardna
devijacija čita kao tipična udaljenost od sredine samo približno.

Za približno normalnu raspodjelu vrijedi korisno pravilo palca po kojem oko
68 % opažanja leži unutar jedne standardne devijacije od sredine, oko 95 %
unutar dviju i oko 99,7 % unutar triju. Naši podaci pokazuju što se dogodi kada
se pravilo primijeni bez provjere pretpostavke. Unutar jedne standardne
devijacije nalazi se `r paste0(hr_broj(s4$u_jednoj_sd, 1), " %")` ispitanika, a
ne 68 %, a raspon dviju devijacija proteže se od minus
`r hr_broj(abs(s4$donja_dvije), 1)` do `r hr_broj(s4$gornja_dvije, 1)` minuta.
Negativno trajanje ne postoji, pa donja granica sama pokazuje da pretpostavka
ne stoji.

Zanimljiviji je drugi dio provjere. Unutar dviju standardnih devijacija
nalazi se `r paste0(hr_broj(s4$u_dvije_sd, 1), " %")` ispitanika, što se s
pravilom poklapa gotovo točno. Jedna brojka koja izađe kako smo očekivali ne
potvrđuje pretpostavku na kojoj očekivanje počiva, a upravo takva poklapanja
najčešće zaustave provjeru prerano.

Kada sredina i standardna devijacija zataje, opis se prenosi na položaje u
poredanom nizu. **Percentil** je vrijednost ispod koje leži zadani postotak
opažanja, pa je medijan pedeseti percentil. Prvi i treći kvartil odsijecaju
donjih i gornjih 25 %, a razlika između njih opisuje širinu središnje polovine
raspodjele.

*Slika. Percentili dnevnog vremena korištenja u simuliranoj anketi. Izrada autora.*

Interkvartilni raspon našeg uzorka iznosi `r hr_broj(s4$iqr, 1)` minuta i
proteže se od `r hr_broj(s4$q1, 1)` do `r hr_broj(s4$q3, 1)` minuta. Ta mjera
ne reagira na to koliko je krajnje opažanje daleko, nego samo na to koliko ih
je, pa se s medijanom uparuje jednako prirodno kao standardna devijacija sa
sredinom. Izvještaj koji navodi medijan uz standardnu devijaciju miješa dva
različita opisa iste raspodjele.

## Oblik raspodjele i položaj opažanja

Središte i raspršenost ne kazuju je li raspodjela simetrična. Kada lijeva i
desna strana izgledaju kao zrcalne slike, sredina i medijan padaju na isto
mjesto. Dugi rep prema većim vrijednostima povlači sredinu za sobom i ostavlja
medijan gdje je bio, pa razlika između njih mjeri koliko je raspodjela
nagnuta.

**Asimetrija** je mjera nesimetričnosti raspodjele, pozitivna kada je rep
raspodjele okrenut prema većim vrijednostima.

Formalna mjera polazi od standardiziranih odstupanja i diže ih na treću
potenciju. Neparna potencija čuva predznak, pa velika pozitivna odstupanja
zbroj vuku prema pozitivnome, a velika negativna prema negativnome.

$$
\text{asimetrija} = \frac{1}{n} \sum_{i=1}^{n}
  \left( \frac{x_i - \bar{x}}{s} \right)^3
$$

Asimetrija našeg uzorka iznosi `r hr_broj(s4$asimetrija, 2)`. Takav oblik u
podacima o medijskoj uporabi nije iznimka nego očekivanje, i to iz strukturnog
razloga. Vrijeme, dijeljenja i pratitelji imaju prirodnu donju granicu na nuli
a nikakvu gornju, pa se većina opažanja skuplja pri dnu dok pojedinci mogu
otići vrlo visoko. Isti izraz s eksponentom četiri mjeri zaobljenost
(*kurtosis*) i opisuje težinu repova, a naš višak nad vrijednošću očekivanom
za normalnu raspodjelu iznosi `r hr_broj(s4$visak_zaobljenosti, 2)`, što znači
da krajnjih slučajeva ima više nego što bi zvonasta krivulja predvidjela.

Kada raspodjela ima takav oblik, promjena ljestvice često pomaže više od
promjene mjere. Logaritam sabija velike vrijednosti i razmake pretvara u
omjere, pa razlika između 10 i 20 minuta postaje jednako velika kao razlika
između 60 i 120.

*Slika. Dnevno vrijeme korištenja u izvornim jedinicama i na logaritamskoj ljestvici, sa sredinom i medijanom.*

Na logaritamskoj ljestvici asimetrija pada na
`r hr_broj(s4$asimetrija_log, 2)`, a sredina i medijan gotovo se poklapaju na
`r hr_broj(s4$sredina_log, 2)` i `r hr_broj(s4$medijan_log, 2)`.
Transformacija time nije popravila podatke, nego je promijenila pitanje.
Rezultati na toj ljestvici govore o razmjernim razlikama, pa svaka tvrdnja
izvedena iz njih mora reći da je razlika višekratnik, a ne broj minuta.

Oblik odlučuje i o tome kada je pojedino opažanje neobično. Dnevnih 100 minuta
znači jedno u skupini koja se u prosjeku zadržava 15 minuta, a nešto posve
drugo u skupini koja se zadržava 80. Položaj postaje čitljiv kada udaljenost od
sredine izrazimo u standardnim devijacijama.

**Standardizirana vrijednost** kaže koliko standardnih devijacija pojedino
opažanje leži iznad ili ispod aritmetičke sredine.

$$
z_i = \frac{x_i - \bar{x}}{s}
$$

Standardizirana varijabla uvijek ima sredinu nula i standardnu devijaciju
jedan, pa vrijednosti izmjerene u minutama i vrijednosti izmjerene na ljestvici
povjerenja od 1 do 10 postaju usporedive. Prevođenje na zajednički jezik
položaja ipak ne uklanjava oblik raspodjele. U desno nagnutim podacima ostaje
nemoguće da neko opažanje bude tri standardne devijacije ispod sredine, dok ih
iznad nje može biti pet.

Odluka koja se lako preskoči jest odluka o skupini prema kojoj se položaj mjeri.
Standardizacija u cijelom uzorku i standardizacija unutar dobne skupine
odgovaraju na različita pitanja, a njihovi se odgovori mogu razlikovati i u
predznaku.

*Slika. Tri ispitanika iz najstarije skupine, standardizirani u cijelom uzorku i unutar vlastite skupine. Izrada autora.*

Ispitanici u tablici provode manje vremena od prosjeka cijelog uzorka i unutar
svoje dobne skupine pripadaju najintenzivnijim korisnicima. Obje su tvrdnje
istinite i opisuju isti podatak, pa izvještaj mora reći prema čemu je položaj
mjeren. Kada referentna skupina ostane neimenovana, čitatelj joj pridaje onu
koja mu je bliža i zaključak se tiho mijenja.

## Interakcija — Oblikovanje distribucije

Oblikovatelj raspodjele pomiče jedno krajnje opažanje i širi preostalih devet
oko njihova zajedničkog središta. Sredina, medijan i dvije mjere raspršenosti
mijenjaju se pred čitateljem. Tako postaje vidljivo koje mjere slušaju svaku
vrijednost, a koje prvenstveno čuvaju redoslijed.

*Slika. Reakcija mjera središta i raspršenosti na oblik konstruirane raspodjele.*

**Što isprobati.**

1. Spustite krajnje opažanje sa 70 na 14 i usporedite sredinu s medijanom.
2. Vratite ga na 70 i provjerite koja se mjera središta više pomaknula.
3. Postavite krajnje opažanje na 11 pa povećajte faktor raspršenosti i
   usporedite dvije raspodjele iste sredine.

**Statistika u divljini.**
**Prosjek kao početak pregleda.** Tukey je zagovarao istraživački pristup u
kojem se podaci pregledavaju iz više kutova prije konačnog modeliranja
(Tukey, 1977). Izvještaj koji navodi samo prosjek uklanja upravo oblik koji bi
mogao objasniti zašto taj prosjek nije tipičan.

Odgovorna tablica zato uparuje mjeru središta s mjerom raspršenosti i brojem
opažanja. Graf zatim pokazuje asimetriju, praznine i krajnje slučajeve koje tri
sažetka ne mogu nositi.

**Pitajte model.**
Asistent lako izradi tablicu sažetaka i pritom obično pretpostavi simetriju
koju nije provjerio. Vrijedi zatražiti broj valjanih opažanja, postupanje s
nedostajućim vrijednostima i medijan uz svaku sredinu, a zatim provjeriti je li
za nagnutu raspodjelu ponudio mjeru koja opisuje tipično opažanje. Dvije
provjere hvataju većinu grešaka. Zbroj opažanja po skupinama mora dati ukupan
broj, a granica raspona izvedena iz sredine i standardne devijacije ne smije
pasti izvan mogućih vrijednosti mjere.

> Sažmi svaku skupinu brojem opažanja, prikladnom mjerom središta i prikladnom
> mjerom raspršenosti. Obrazloži izbor nakon pregleda oblika raspodjele i
> prikaži koliko vrijednosti nedostaje.

**Nađite grešku.**
Prosječno dnevno korištenje u uzorku iznosi `r hr_broj(s4$sredina, 1)` minuta
uz standardnu devijaciju od `r hr_broj(s4$sd, 1)` minuta. Tipičan ispitanik
dakle provodi oko 50 minuta dnevno na društvenim mrežama, a polovina uzorka
nalazi se iznad te vrijednosti. Raspršenost je znatna, pa razlike među dobnim
skupinama treba dodatno ispitati.

Greška je tvrdnja da se polovina uzorka nalazi iznad sredine. To vrijedi za
simetričnu raspodjelu, a ovdje iznad sredine leži
`r paste0(hr_broj(s4$iznad, 0), " %")` ispitanika, jer sredinu prema gore
povlači rep krajnjih slučajeva. Podjelu na polovine opisuje medijan, koji
iznosi `r hr_broj(s4$medijan, 0)` minuta.

## Razrađeni primjer

Zadatak je opisati koliko se vremena u anketi provodi na društvenim mrežama i
razlikuju li se dobne skupine. Prvi je korak odluka o mjerama, a oblik
raspodjele tu odluku već je donio. Zbirna raspodjela nagnuta je prema većim
vrijednostima, pa uz sredinu treba stajati medijan, a uz standardnu devijaciju
interkvartilni raspon.

Blok dijeli uzorak po dobnoj skupini i za svaku ponavlja isti niz mjera. Znak
`|>` vodi podatke iz jednog koraka u sljedeći, `group_by` određuje po čemu se
uzorak dijeli, a `summarise` svakoj skupini vraća jedan red. Taj se obrazac
vraća u svakom kasnijem poglavlju koje sažima podatke po skupinama.

*Slika. Dnevno vrijeme korištenja prema dobnoj skupini u simuliranoj anketi. Izrada autora.*

Tablica pokazuje uređen pad kroz dobne skupine, od
`r hr_broj(s4_najmladi$medijan, 0)` minuta u najmlađoj do
`r hr_broj(s4_najstariji$medijan, 0)` minuta u najstarijoj po medijanu. Zbirna
sredina od `r hr_broj(s4$sredina, 1)` minuta ne opisuje nijednu od tih skupina,
jer leži između njih i istodobno je povučena repom najintenzivnijih korisnika.
Sažetak cijelog uzorka ovdje opisuje mješavinu, a ne populaciju.

Raspršenost pada zajedno sa središtem, i to je nalaz sam za sebe. Standardna
devijacija u najmlađoj skupini iznosi `r hr_broj(s4_najmladi$sd, 1)` minuta, a
u najstarijoj `r hr_broj(s4_najstariji$sd, 1)`, pa se skupine ne razlikuju samo
po tome koliko koriste mreže nego i po tome koliko su međusobno slične. Skupina
s najvišim medijanom ujedno je najmanje homogena.

Ono što tablica ne može pokazati jest odakle raspršenost dolazi. Interkvartilni
raspon u najmlađoj skupini iznosi `r hr_broj(s4_najmladi$iqr, 1)` minuta, dok
standardna devijacija govori o širini koja uključuje i krajnje slučajeve.
Razlika između tih dviju brojki mjeri koliko opis skupine ovisi o nekolicini
najintenzivnijih korisnika, a odgovor na pitanje jesu li ti korisnici pogreška
mjerenja, legitimna manjina ili sam predmet istraživanja ne daje nijedan
sažetak.

## Sažetak

Sažetak je odluka o tome koji dio raspodjele čuvamo u malom broju vrijednosti.
Mjera središta bez raspršenosti ostavlja pola priče neispričanom, a obje
zajedno još ne pokazuju oblik, pa nagnuta raspodjela svaku od njih čini
podložnom pogrešnom čitanju. Standardizacija opisuje položaj i time uvodi
pitanje prema kojoj se skupini položaj mjeri, dok transformacija ljestvice
mijenja jedinicu tvrdnje. Razlika između uzorka i populacije ovdje je ušla u
zapis i čeka poglavlje o uzorkovanju da je opravda. Sljedeće poglavlje podatke
vraća u prostor i pokazuje kako graf postaje dio argumenta.

## Pojmovi

aritmetička sredina (*mean*), skraćena sredina (*trimmed mean*), medijan
(*median*), mod (*mode*), varijanca (*variance*), standardna devijacija
(*standard deviation*), interkvartilni raspon (*interquartile range*),
standardizirana vrijednost (*z-score*), asimetrija (*skewness*), zaobljenost
(*kurtosis*)

## Zadaci

### Konceptualni

Predvidite kako će se sredina, medijan, standardna devijacija i interkvartilni
raspon promijeniti kada jedno najveće opažanje dodatno poraste. Predajte
obrazloženje bez računanja, s izričitim razlikovanjem mjera koje reagiraju na
veličinu odstupanja od onih koje reagiraju samo na njegovo postojanje.

### Računski

Upotrijebite interakciju poglavlja. Pri početnim postavkama pročitajte s prikaza
svih deset vrijednosti, ručno izračunajte sredinu i medijan i usporedite ih s
brojkama koje prikaz ispisuje. Zatim krajnje opažanje spustite na najmanju
dopuštenu vrijednost i oba izračuna ponovite. Predajte četiri broja i dvije
rečenice o tome koja se mjera promijenila više i zašto joj je promjena veća.

S prikaza oblika raspodjele potom pročitajte položaj sredine i medijana u
izvornim jedinicama i na logaritamskoj ljestvici te u jednoj rečenici objasnite
zašto se razlika među njima mijenja. Postupak za isti izračun nad cijelim skupom
podataka nalazi se u praktikumu.

### Kritički

Objasnite zašto istraživačka analiza ne završava jednom mjerom središta
(Tukey, 1977). Predajte popis triju dodatnih provjera u punim rečenicama, uz
navod što bi svaka od njih otkrila na podacima iz ovog poglavlja.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte jedan opravdan izbor, jednu
neopravdanu tvrdnju i izračun kojim biste je provjerili u tri koraka.

---

# Vizualizacija kao argument

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

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

---

# Povezanost

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 20 min | Pogodi korelaciju | simulirana anketa, Anscombeov kvartet | pogl. 4, 5 |

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
linearna veza ne znači da odnosa nema, jer zakrivljeni obrazac može imati
koeficijent blizu nule.

Do mjere se dolazi pitanjem koje se može postaviti za svakog pojedinog
ispitanika. Je li iznad prosjeka u obje varijable, ispod prosjeka u obje, ili
iznad u jednoj i ispod u drugoj. U simuliranoj anketi `anketa_mreze`, koja ima
`r s6_n` ispitanika i nije mjerenje nego nastavni skup proizveden kodom, na istu
stranu prosjeka u dobi i u dnevnim minutama odstupa
`r paste0(hr_broj(100 * s6_udio_slaganje, 0), " %")` ispitanika. Kada varijable
ne bi bile povezane, taj bi udio bio blizu polovine, jer bi predznaci dvaju
odstupanja bili neovisni. Udio znatno ispod polovine znak je da odstupanja
redovito idu na suprotne strane, dakle da je veza negativna. Sam udio ipak ne
kaže koliko je veza jaka, jer ne razlikuje jedva prijeđeni prosjek od krajnje
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

Jedna osobina kovarijancu čini neupotrebljivom za izvještavanje. Ona nosi
jedinice obiju varijabli pomnožene jedna s drugom. Kovarijanca dobi i dnevnih
minuta u anketi iznosi `r hr_broj(s6_kov, 1)`, a kovarijanca dobi i istog
vremena izraženog u satima `r hr_broj(s6_kov_sati, 1)`. Odnos se nije
promijenio, promijenila se jedinica, a broj se promijenio šezdeset puta.
Vrijednost kovarijance zato ne govori ništa dok se ne zna u čemu je mjereno,
i nijedan se par varijabli po njoj ne može usporediti s drugim parom.

## Zajedničko kretanje bez jedinica

Rješenje je već napisano u poglavlju o sažimanju podataka. Standardizirana
vrijednost pretvara opažanje u broj standardnih devijacija od sredine i time
odbacuje jedinicu. Ako se prije množenja obje varijable standardiziraju,
umnožak više ne ovisi o tome mjeri li se vrijeme u minutama ili satima.

**Pearsonova korelacija** je prosjek umnožaka standardiziranih vrijednosti
dviju varijabli, pa mjeri smjer i jačinu njihove linearne veze na ljestvici od
$-1$ do $+1$, neovisno o mjernim jedinicama.

Uzoračku korelaciju označavamo slovom $r$, a odgovarajuću vrijednost cijele
populacije grčkim slovom $\rho$, po istom pravilu po kojem su u poglavlju o
sažimanju podataka uzorak nosio latinicu, a populacija grčka slova. Definicija
se zapisuje kao

$$r = \frac{1}{n-1} \sum_{i=1}^{n} z_{x_i} \, z_{y_i} = \frac{\operatorname{Cov}(x, y)}{s_x \, s_y},$$

gdje su $z_{x_i}$ i $z_{y_i}$ standardizirane vrijednosti dviju varijabli kod
istog opažanja, a $s_x$ i $s_y$ njihove standardne devijacije. Dva zapisa daju
isti broj, jer dijeljenje kovarijance standardnim devijacijama i
standardiziranje prije množenja isti su postupak izveden različitim redom.

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

## Koliko znači jedan koeficijent

Nakon izračuna redovito slijedi pitanje je li dobiveni broj velik. Cohen je za
društvene znanosti ponudio orijentacijske vrijednosti, po kojima se korelacija
oko 0,10 opisuje kao mala, oko 0,30 kao srednja, a oko 0,50 kao velika
(Cohen, 1988). Te se vrijednosti citiraju toliko često da su stekle status
ljestvice za očitavanje, što nisu.

Uvjet stoji već kod izvora. Vrijednosti su ponuđene za polja u kojima ne postoji
bolja osnova za prosudbu i izričito ustupaju mjesto poznavanju područja
(Cohen, 1988). U predviđanju pojedinačnog ponašanja korelacija od 0,30 ozbiljan
je nalaz, a u provjeri pouzdanosti mjernog instrumenta 0,50 je razlog za
odbacivanje instrumenta. Isti broj u dvama kontekstima nosi suprotne prosudbe,
pa se veličina ne očitava iz tablice nego iz literature koja mjeri isto što i
mi.

Jedna preinaka koeficijenta ipak pomaže prosudbi, jer ga stavlja na ljestvicu
koja se lakše tumači. Kvadrirana korelacija kaže koliki je udio varijance jedne
varijable zajednički s drugom, pa korelacija od `r hr_broj(s6_r, 2)` znači da
dvije varijable dijele `r paste0(hr_broj(100 * s6_r^2, 0), " %")` varijance,
dok preostalih `r paste0(hr_broj(100 * (1 - s6_r^2), 0), " %")` ostaje
neobjašnjeno. Kvadriranje je pritom nemilosrdno prema srednjim vrijednostima,
jer korelacija od 0,30, koju bi mnogi opisali kao osrednju, dijeli devet posto
varijance. Poglavlje o regresiji istu veličinu koristi kao mjeru prilagodbe
modela.

Druga polovina odgovora nema veze s veličinom. Koeficijent izračunat na uzorku
procjena je, pa nosi vlastitu nesigurnost, koja opada s brojem opažanja.
Korelacija od 0,40 na trideset ispitanika i ista korelacija na tri tisuće
ispitanika dva su vrlo različita nalaza, iako je broj jednak. Dio knjige o
uzorkovanju i procjeni tu nesigurnost izračunava, a do tada vrijedi da se
korelacija bez broja opažanja uz sebe ne može prosuditi.

Kada se varijabli nakupi, korelacije svih parova slažu se u matricu, koja je
simetrična i na dijagonali nosi jedinice, jer je svaka varijabla savršeno
povezana sama sa sobom.

*Slika. Korelacije triju brojčanih varijabli simulirane ankete. Izrada autora.*

Matrica je ekonomična i opasna u istoj mjeri. Tri varijable daju tri para,
deset varijabli daje četrdeset pet, a pregled u kojem se traži najveći broj
prestaje biti provjera hipoteze i postaje njezino izmišljanje. Poglavlje o krizi
i obnovi pokazuje što se s takvim pretraživanjem dogodi kada mu se doda
testiranje. Ovdje je dovoljno pravilo da matrica služi za pregled, a da svaki
par koji ulazi u zaključak dobije vlastiti raspršeni dijagram.

## Rangovi umjesto vrijednosti

Pearsonova korelacija mjeri koliko se oblak približio pravcu, pa je zakrivljena
veza za nju djelomično nevidljiva. Odnos u kojem jedna varijabla stalno raste s
drugom, ali sve sporije, postoji i uredan je, a mjeren pravcem izgleda slabije
nego što jest.

Za takve slučajeve podaci se prije računanja zamjenjuju rangovima. Najmanja
vrijednost dobiva prvi rang, sljedeća drugi, i tako redom, nakon čega se na
rangove primijeni isti Pearsonov izračun. Rangiranje čuva poredak i odbacuje
razmake, pa rezultat mjeri je li kretanje dosljedno u jednom smjeru bez zahtjeva
da bude pravocrtno. Tako dobivena **Spearmanova korelacija**, koja se označava
sa $r_s$, mjeri monotonu vezu.

*Slika. Dob i dnevno vrijeme korištenja u simuliranoj anketi. Veza je dosljedno silazna, ali nije pravocrtna, pa je mjera koja traži pravac strože kažnjava.*

Oblak pada strmo u mlađim godinama i izravnava se poslije, što je oblik koji
pravac ne može pratiti. Pearsonova korelacija dobi i dnevnih minuta iznosi
`r hr_broj(s6_r, 2)`, a Spearmanova `r hr_broj(s6_rs, 2)`. Razlika u istom
smjeru redovit je znak da je veza monotona, ali zakrivljena. Potvrda dolazi
odmah, jer korelacija dobi s logaritmom minuta, koja zakrivljenost uklanja,
iznosi `r hr_broj(s6_r_log, 2)` i približila se Spearmanovoj vrijednosti.

Iz toga slijedi jednostavna dijagnostika. Kada se dva koeficijenta slažu, veza
je približno pravocrtna i Pearsonov je izbor u redu. Kada se razilaze,
zakrivljenost je vjerojatna i graf će je pokazati. Spearmanova mjera uz to slabije
reagira na pojedinačno krajnje opažanje, jer krajnja vrijednost dobiva samo
sljedeći rang umjesto vlastite udaljenosti, pa se koristi i kada podaci sadrže
malo opažanja koja izrazito odudaraju.

Nijedna od dviju mjera ne vidi vezu koja nije monotona. Kada je zadovoljstvo
niže i pri vrlo malom i pri vrlo velikom opterećenju, oba koeficijenta mogu
ispasti blizu nule, jer se uzlazni i silazni dio međusobno ponište. To nije
znak da odnosa nema nego znak da nijedan jedan broj taj odnos ne može nositi.

## Kada koeficijent zavarava

Prvi način na koji koeficijent zavara nije pogreška računanja nego izbor onoga
tko je birao uzorak. Korelacija mjeri koliko varijacije jedne varijable prati
varijaciju druge, pa uklanjanje varijacije uklanja i mjeru.

**Ograničenje raspona** (*range restriction*) je smanjenje izmjerene
povezanosti do kojeg dolazi kada uzorak pokriva samo dio raspona jedne
varijable, pa unutar njega ostaje premalo varijacije da bi se odnos vidio.

Anketa to pokazuje na sebi. U cijelom uzorku korelacija dobi i dnevnih minuta
iznosi `r hr_broj(s6_r, 2)`. Ograničimo li se na najmlađu dobnu skupinu, u kojoj
je `r s6_n_uzak` ispitanika unutar raspona od sedam godina, ista korelacija
iznosi `r hr_broj(s6_r_uzak, 2)`, dakle slabo i k tome u suprotnom smjeru.
Vrijedi znati odakle taj drugi broj dolazi. Generator koji je skup proizveo
razlikuje dobne skupine, a unutar skupine svim ispitanicima dodjeljuje istu
raspodjelu, pa je prava vrijednost unutar te skupine nula. Dobivenih
`r hr_broj(s6_r_uzak, 2)` cijelim je iznosom ono što promjenjivost uzorka
proizvede na `r s6_n_uzak` opažanja.

Veza između dobi i vremena korištenja time nije opovrgnuta. Nestao je raspon
dobi unutar kojeg se mogla očitati, i to je razlog zbog kojeg se studija
provedena na studentima jedne generacije ne može uzeti kao dokaz da dob nije
važna. Isto vrijedi za svaku selekciju koja prethodi mjerenju, dakle za uzorke
sastavljene od primljenih kandidata, zaposlenih radnika ili preživjelih
poduzeća. Poglavlje o mjerenju i dizajnu isti postupak opisuje kao pitanje o
tome tko je ušao u skup.

Isti izračun pokazao je i drugi način na koji koeficijent zavara, jer je broj
različit od nule ovdje nastao iz uzorka u kojem veze nema. Što je opažanja
manje, to je takav ishod vjerojatniji, pa koeficijent bez broja opažanja uz sebe
ne nosi dovoljno da bi se prosudio. Treći je način osjetljivost na pojedinačno
opažanje, jer jedna vrijednost daleko od ostalih pomiče oba prosjeka i obje
standardne devijacije, a s njima i sam koeficijent. Sva tri načina nose isti
simptom, dakle broj koji izgleda uvjerljivo, i sva tri otkriva isti postupak,
dakle pogled na raspršeni dijagram prije nego što se broj negdje zapiše.

## Kada se predznak preokrene

Najteži slučaj nije oslabljen nego preokrenut koeficijent. On nastaje kada
uzorak sadrži podskupine koje se razlikuju po razini obiju varijabli, a
promatraju se zbirno.

Zamislimo tri odjela jedne organizacije, koji se razlikuju po tome koliko su
njihovi zaposlenici iskusni i koliko su zadovoljni poslom. Podaci koji slijede
konstruirani su za ovu svrhu i nisu mjerenje. Unutar svakog odjela zadovoljstvo
blago opada s godinama staža, dok su odjeli s iskusnijim zaposlenicima ujedno
oni s višim zadovoljstvom.

*Slika. Konstruirani podaci u kojima zbirna veza raste, a veza unutar svakog odjela pada. Isti su podaci prikazani jednom bez oznake odjela i jednom s njom.*

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

Društvene znanosti taj problem susreću u obliku koji nema ni jednu podskupinu
nego samo pogrešnu jedinicu analize. Korelacije se često računaju na zemljama,
županijama ili školama, dakle na prosjecima, jer su podaci u tom obliku
dostupni. Prosjeci su glatkiji od pojedinaca, pa su korelacije među njima
redovito znatno jače, a njihov smjer ne mora vrijediti unutar tih jedinica.
Zaključak o pojedincu izveden iz veze među skupinama naziva se **ekološkom
pogreškom** (*ecological fallacy*), i ne otklanja se boljim izračunom nego samo
podacima o pojedincima. Tvrdnja izračunata na razini zemalja legitiman je nalaz
o zemljama, i ništa više od toga.

Odatle slijedi ono što se o uzroku smije reći. Varijabla koja je povezana i s
pretpostavljenim uzrokom i s ishodom prisvaja dio veze koja se pripisuje uzroku,
i to je konfundirajuća varijabla iz poglavlja o mjerenju i dizajnu. Odjel je
ovdje takva varijabla, jer određuje i staž i zadovoljstvo. Kada je poznata i
izmjerena, razdvajanje je popravlja. Kada nije izmjerena, ona i dalje djeluje, a
koeficijent o njoj ne javlja ništa.

Zbog toga povezanost sama ne određuje uzrok. Veza između dviju varijabli
podnosi četiri objašnjenja, jer prva može djelovati na drugu, druga na prvu,
obje može oblikovati treća, ili je obrazac nastao pukom promjenjivošću uzorka.
Koeficijent je jednak u sva četiri slučaja i ne razlikuje ih. Razlikuje ih
dizajn istraživanja, o kojem je poglavlje o mjerenju i dizajnu već govorilo, pa
je smjer tvrdnje koju o povezanosti smijemo iznijeti određen prije nego što je
izračunata.

## Interakcija — Pogodi korelaciju

Igra prikazuje četiri raspršena oblaka bez koeficijenta i traži procjenu
smjera i jačine. Rezultat se mijenja sa svakom procjenom, pa se vidljivi oblik
može izravno usporediti s veličinom Pearsonove korelacije.

*Slika. Četiri deterministički simulirana oblaka bez prikazanih koeficijenata. Zajedničke osi omogućuju usporedbu smjera i zbijenosti.*

**Što isprobati.**

1. Procijenite samo znak svake povezanosti i provjerite jesu li klizači na pravoj strani nule.
2. Usporedite oblake A i D te procijenite koji je odnos bliže savršenoj povezanosti.
3. Fino namjestite procjene za slabije oblake B i C bez mijenjanja prvih dviju.
4. Pokušajte ostvariti četiri pogotka, zatim opišite koji je oblak bilo najteže procijeniti.

**Statistika u divljini.**
**Dinosaur s urednim sažetkom.** Anscombeove je skupove trebalo sastaviti ručno,
pa je dugo ostajalo otvoreno koliko je takvih slučajeva uopće moguće. Matejka i
Fitzmaurice odgovorili su postupkom koji polazi od zadanog skupa i sitnim
pomacima točaka mijenja njegov oblik, a pritom sredine, standardne devijacije i
korelaciju drži nepromijenjenima do druge decimale (Matejka, 2017). Iz istog
sažetka tako su izveli niz oblika, među njima zvijezde, križeve i obris
dinosaura.

Dohvat nalaza vrijedi izmjeriti. Rad ne pokazuje da je korelacija nestabilna
niti da je pogrešno izračunata, jer je u svim tim skupovima ista i točna. Ono
što pokazuje jest da sažetak od nekoliko brojeva ne određuje skup podataka, pa
put od podataka do sažetka ide samo u jednom smjeru. Iz toga slijedi obveza koja
je skromnija od pouke koja se uz rad obično navodi, dakle da se uz koeficijent
prikaže i oblik iz kojeg je nastao, a ne da se koeficijent napusti.

**Pitajte model.**
Asistent može izračunati Pearsonovu i Spearmanovu korelaciju i opisati graf.
Treba mu zatražiti provjeru linearnosti, krajnjih vrijednosti, podskupina i
ograničenja raspona. Nakon odgovora valja provjeriti jesu li redovi u dvjema
varijablama ispravno upareni i je li iz povezanosti izveden nedopušten uzrok.

Tri promašaja ponavljaju se dovoljno često da ih vrijedi tražiti unaprijed.
Asistent rado veličinu koeficijenta očitava s Cohenove ljestvice bez uvjeta koji
uz nju ide (Cohen, 1988). Rado navodi korelaciju bez broja opažanja, pa se
nesigurnost procjene ne može prosuditi. I rado prelazi s opisa veze na jezik
učinka, u kojem jedna varijabla „dovodi do" druge, iako je izračunao samo
zajedničko kretanje.

> Usporedi Pearsonovu i Spearmanovu korelaciju, opiši oblik raspršenog
> dijagrama i provjeri utjecaj krajnjih opažanja. Zaključak ograniči na
> povezanost koju dizajn podupire.

**Nađite grešku.**
Na pitanje o odnosu dobi i vremena korištenja asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Korelacija u toj skupini iznosi
`r hr_broj(s6_r_uzak, 2)` uz `r s6_n_uzak` ispitanika, dakle slaba je i
pozitivna. Budući da je skupina dobno homogena i bez krajnjih vrijednosti,
procjena je čista od miješanja naraštaja, pa zaključuje da dob i vrijeme
korištenja praktički nisu povezani.

Greška je posljednja rečenica, u kojoj nalaz iz jedne dobne skupine postaje
tvrdnja o dobi uopće. Redak `filter` zadržava ispitanike unutar sedam godina
dobi i time uklanja upravo onu varijaciju dobi koja je nosila odnos, pa
homogenost skupine nije prednost procjene nego njezino ograničenje. Na cijelom
uzorku ista korelacija iznosi `r hr_broj(s6_r, 2)`. Popravak je izračunati je na
cijelom rasponu, a nalaz iz podskupine izvijestiti kao nalaz o toj podskupini.

## Razrađeni primjer

Zadatak je ispravno izvijestiti o povezanosti dviju varijabli iz simulirane
ankete, dakle dobi i dnevnog vremena korištenja društvenih mreža. Postupak ima
tri koraka i svaki od njih odgovara jednoj provjeri iz ovog poglavlja. Najprije
se pogleda oblik, zatim se izračunaju obje mjere, i tek se onda piše rečenica.

Poziv `summarise` i njegov niz glagola dolaze iz poglavlja o sažimanju podataka,
a funkcija `cor` jedina je novost i računa korelaciju dvaju stupaca, po zadanom
Pearsonovu. Argument `method` mijenja mjeru u Spearmanovu. Ovo poglavlje ne
uvodi nijedan novi obrazac čitanja koda, što je i njegova svrha, jer se ista
tri elementa pojavljuju od poglavlja o sažimanju nadalje.

Raspršeni dijagram iz odjeljka o rangovima pokazao je da veza pada strmo u
mlađim godinama i izravnava se poslije. Uz taj oblik dva koeficijenta imaju
smisla zajedno, jer Pearsonova vrijednost od `r hr_broj(s6_r, 2)` mjeri koliko
je oblak blizu pravca, a Spearmanova od `r hr_broj(s6_rs, 2)` koliko je kretanje
dosljedno silazno. Razlika među njima nije neslaganje nego opis zakrivljenosti.

Iz toga slijedi rečenica koju je dopušteno napisati. U ovom simuliranom uzorku
od `r s6_n` ispitanika dob i dnevno vrijeme korištenja povezani su negativno i
dosljedno, uz Spearmanovu korelaciju od `r hr_broj(s6_rs, 2)`, dok je veza
zakrivljena, pa je Pearsonova vrijednost od `r hr_broj(s6_r, 2)` niža. Rečenica
navodi mjeru, njezinu veličinu, broj opažanja i oblik odnosa, a ne navodi uzrok,
jer podaci dolaze iz jednokratnog mjerenja bez ikakve intervencije.

## Sažetak

Kovarijanca mjeri zajedničko odstupanje od sredina, a korelacija je ista mjera
očišćena od jedinica, pa se kreće između minus jedan i plus jedan i mjeri koliko
je oblak blizu pravca. Spearmanova inačica radi s rangovima, pa mjeri
dosljednost smjera bez zahtjeva da veza bude pravocrtna, a njihovo je
razilaženje najjeftinija dijagnostika zakrivljenosti u knjizi. Jedan broj ne
može nositi ni oblik odnosa, ni širinu raspona iz kojeg je izračunat, ni
podskupine koje ga mogu preokrenuti, i sve troje otkriva prikaz iz prethodnog
poglavlja. Iz povezanosti se ne izvodi uzrok, jer četiri različita objašnjenja
proizvode isti koeficijent, a razlikuje ih dizajn a ne izračun. Sve dosad
izračunato odnosilo se na uzorak pred nama, pa sljedeći dio knjige uvodi
vjerojatnost i pita koliko se od takvog obrasca može očekivati i kad veze nema.

## Pojmovi

kovarijanca (*covariance*), Pearsonova korelacija (*Pearson correlation*),
Spearmanova korelacija (*Spearman correlation*), monotona veza (*monotonic
relationship*), linearnost (*linearity*), matrica korelacija (*correlation
matrix*), ograničenje raspona (*range restriction*), utjecajno opažanje
(*influential observation*), konfundirajuća varijabla (*confounder*), ekološka
pogreška (*ecological fallacy*)

## Zadaci

### Konceptualni

Nacrtajte dva različita odnosa koja mogu imati sličnu Pearsonovu korelaciju, i
uz svaki napišite što bi izvještaj koji navodi samo koeficijent propustio.
Predajte skicu i objašnjenje.

### Računski

Upotrijebite tablicu korelacija koju poglavlje ispisuje za tri varijable
simulirane ankete. Za svaki od triju parova zapišite smjer veze i procijenite,
prema onome što ste vidjeli na raspršenom dijagramu dobi i minuta, bi li se
Spearmanova vrijednost razlikovala od Pearsonove i u kojem smjeru. Zatim
upotrijebite interakciju poglavlja i za svaki od četiriju oblaka zabilježite
koliko je vaša procjena promašila. Predajte tablicu sa sedam redaka i jednom
rečenicom obrazloženja u svakom. Postupak za ponavljanje izračuna nad cijelim
skupom nalazi se u praktikumu.

### Kritički

Pronađite objavljenu tvrdnju u kojoj se iz povezanosti dviju društvenih pojava
izvodi preporuka za djelovanje. Odredite koje od četiriju objašnjenja veze tekst
pretpostavlja, koju bi treću varijablu trebalo isključiti i kakav bi dizajn to
mogao učiniti. Predajte odlomak s presudom i s uvjetom pod kojim bi preporuka
bila opravdana.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte što je u pozivu ispravno
izvedeno, redak koda koji proizvodi pogrešan zaključak, mehanizam zbog kojeg
koeficijent pada, i napišite ispravljenu rečenicu izvještaja.
