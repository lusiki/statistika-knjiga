# Sažimanje podataka

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

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
