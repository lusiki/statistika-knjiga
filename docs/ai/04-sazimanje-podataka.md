# Sažimanje podataka

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 21 min | Oblikovanje distribucije | DigiKat i simulirana anketa | pogl. 1 do 3 |

**Vinjeta.**
Istraživački tim projekta DigiKat pripremio je tri agregatna izvatka istoga
korpusa. To su mjesečni retci po platformi, godišnji retci po platformi i retci po
imenovanoj internetskoj domeni (Šikić, 2026). Urednik želi jednu brojku za
„tipičan izvor”. Za nekoliko minuta dobiva prosjek, medijan i tablicu po
platformama. Svi su računi uredni.

Problem nastaje korak prije računa. Redak u prvim dvjema datotekama predstavlja
platformu u vremenskom razdoblju, a u trećoj domenu kroz cijeli promatrani
raspon. Mjesečna i godišnja tablica dijele dva ključa, ne jedan. Neke nule
angažmana označuju da metrika nije bila dostupna. Datoteka domena obuhvaća
551.712 objava, dok platformske datoteke obuhvaćaju 710.307. Jedan nepažljiv
spoj ili nazivnik može zato proizvesti uvjerljiv odgovor na pitanje koje nitko
nije postavio.

Kako iz tih izvora izgraditi tablicu kojoj se smije vjerovati prije nego što je
sažmemo?

## Od izvora do sažetka

Protokol skeptičnoga čitanja s granice Dijela I ovdje mijenja smjer rada. Više
ne rastavljamo tuđu gotovu brojku, nego od provjerljivoga izvora gradimo vlastiti
sažetak. [Analitička tablica]{.pojam
def="Tablica čiji svaki red predstavlja unaprijed imenovanu jedinicu analize i nosi samo provjerene varijable potrebne za pitanje."
en="analysis table" ch="4"} nije datoteka koju pronađemo, nego rezultat odluka
o jedinici, ključu, spajanju, kodovima, filtrima i nedostajućim vrijednostima.
Svaka odluka mora ostaviti trag koji druga osoba može ponoviti.

### Tri tablice, tri jedinice

DigiKatov paket potječe iz korpusa praćenih objava koje sadrže najmanje dva
različita katolička pojma. Nije slučajan uzorak hrvatskih medija, publike ni
korisnika. Ovdje se čitaju samo redistribuirani agregati, ne pojedinačne objave.
Već popis jedinica pokazuje koje se datoteke smiju povezati, a koje ne smiju.

*Slika. Tri pogleda u paketu DigiKat imaju različite jedinice i ključeve. Izvor: DigiKat, agregatni izvadak, CC BY 4.0 [@digikat2026].*

Datoteka izvora nema zajednički ključ s platformskim datotekama i s njima se
ne spaja. Ona će poslije odgovoriti na pitanje kako su objave raspoređene među
imenovanim domenama. Mjesečna i godišnja datoteka mogu se povezati, ali samo na
paru `godina + platforma`. Izostavi li se jedan dio ključa, mijenja se ono što
redak predstavlja.

### Ključ prije sažetka

Mjesečna tablica ima `r hr_broj(nrow(s4_mjesecno), 0)` redaka i jednako toliko
jedinstvenih ključeva `mjesec + platforma`. Godišnja tablica služi samo da joj
pridruži godišnji nazivnik i oznaku potpunosti. Ispravan spoj zadržava i broj
redaka i zbroj objava. Spoj samo po godini svakom mjesečnom retku pridružuje sve
platforme iste godine, pa aritmetika poslije radi nad umnoženim jedinicama.

*Slika. Kontrola retka, ključa i zbroja prije i nakon dvaju spajanja DigiKatovih agregata. Pogrešni redak prikazuje dijagnostiku, ne dopuštenu analizu. Izvor: DigiKat [@digikat2026].*

Provjera nije završena time što se ukupni zbroj dviju izvornih datoteka
poklapa. Mjesečni i godišnji izvadak razlikuju se u
`r hr_broj(s4_broj_odstupanja, 0)` od 49 platformskih godišnjih ćelija, premda
se razlike ukupno poništavaju. Zato spoj ne zamjenjuje mjesečne vrijednosti
godišnjima niti od njih gradi neprekinuti trend. Za sljedeći korak zadržava se
samo potpuna 2025. godina; rupa i lom metode u 2024. ne ulaze u usporedbu.

### Kada nula znači da mjera nije dostupna

U presjeku 2025. svih devet platformskih redaka ima broj objava, ali za tri
platforme pružatelj ne isporučuje usporediv doseg ni interakcije. Te su ćelije
u izvatku zapisane nulom i označene kodom `metrika_dostupna = ne`. Analitička
tablica zato čuva izvorne stupce, a u izvedenim stupcima te nule pretvara u
nedostajuće vrijednosti. Time se ne izmišlja rezultat ondje gdje mjerenja nema.

Trag odluke počinje brojem označenih redaka. Tri su od devet. To su platforme
`reddit`, `forum` i `comment`, koje zajedno nose
`r hr_broj(s4_2025_objave_nemjerene, 0)` objava. Njihovo podudaranje s
metapodacima pokazuje da praznina slijedi način mjerenja, a ne slučajni propust.
Zato broj objava koristi svih devet platformi, dok sažetak angažmana smije
obuhvatiti samo šest platformi s dostupnom metrikom. Osjetljivost toga izbora
provjeravamo na količini izmjerenoj u svim redcima, dakle na broju objava,
nikada na dosegu ili interakcijama.

*Slika. Osjetljivost medijana broja objava na nepotrebno izbacivanje platformi kojima nedostaje druga metrika. Presjek je potpuna 2025. godina; angažman i doseg ne uspoređuju se. Izvor: DigiKat [@digikat2026].*

Procjena se mijenja s `r hr_broj(s4_medijan_sve_platforme, 1)` na
`r hr_broj(s4_medijan_mjerene_platforme, 1)` objava, ali mijenja se i
predstavljeni skup, od svih devet vrsta platforme prema šest vrsta s dostupnom
metrikom angažmana. Neizvjesnost o interakcijama i dosegu preostalih triju time
se ne smanjuje; ona ostaje granica mjerenja, a ne broj koji treba popuniti.

### Nazivnik je dio tvrdnje

Broj bez baze ne govori koliko je pojava raširena. Pod jednim fiksnim pravilom
brojanja, s riječima odvojenima razmakom i bez obzira na velika slova, riječ
*Analysis* pojavljuje se jednom u naslovu *Exploratory Data Analysis*, dakle
jednom među tri riječi (Tukey, 1977). Pojavljuje se jednom i u naslovu
*Statistical Power Analysis for the Behavioral Sciences*, ali ondje među sedam
riječi (Cohen, 1988). Broj je isti; udio nije. Duljina naslova nije prevalencija
riječi, nego njezin nazivnik.

Ista disciplina vrijedi za DigiKat. Datoteka imenovanih domena sadrži
`r hr_broj(nrow(s4_izvori), 0)` redaka i njihove objave zbrajaju se na
`r hr_broj(s4_izvori_sazetak$objave, 0)`. Svaki udio objava iz te datoteke zato
imenuje upravo 551.712 kao nazivnik, ne 710.307 iz platformskih datoteka.

Tek sada prelazimo na ponašanje sažetaka. Za formule i interakciju koristimo
simuliranu anketu o društvenim mrežama s `r s4$n` ispitanika, dobi, dnevnim
vremenom korištenja i povjerenjem na ljestvici od 1 do 10. Uzorak je proizveden
kodom uz fiksno sjeme i ne opisuje nijednu stvarnu populaciju. Njegova je uloga
pokazati kako se mjere ponašaju u unaprijed poznatoj desno asimetričnoj
simulaciji; nije dokaz o medijskoj uporabi izvan te simulacije.

### Mjere središta

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
svaku vrijednost i izravno odgovara na pitanja o ukupnom iznosu raspoređenom
među opažanjima. Ista joj osjetljivost dopušta da je nekoliko krajnjih
slučajeva odvuče iznad gotovo svih opažanja. Nije zato općenito bolja od
medijana; dvije mjere odgovaraju na različita pitanja.

Krajnjim opažanjima može se smanjiti utjecaj i bez potpunog prelaska na
medijan. **Skraćena sredina** (*trimmed mean*) najprije poreda vrijednosti,
zatim s oba kraja uklanja jednak unaprijed zadani udio i računa sredinu
preostalih opažanja. Uz uklanjanje po 5 % s obje strane naš prosjek pada na
`r hr_broj(s4$skracena5, 1)` minuta, a uz 10 % na
`r hr_broj(s4$skracena10, 1)`.

Skraćivanje dovedeno do kraja daje medijan. Ono što medijan čini drukčijim nije
samo otpornost, nego pitanje na koje odgovara. Sredina je vrijednost koja
minimizira zbroj kvadriranih odstupanja i zato velikim odstupanjima daje veliku
težinu, dok medijan minimizira zbroj apsolutnih odstupanja i sva odstupanja
tretira jednako.

**Medijan** je vrijednost koja poredani niz opažanja dijeli na dvije jednako
velike polovine.

Medijan našeg uzorka iznosi `r hr_broj(s4$medijan, 0)` minuta i time za
sredinom zaostaje `r hr_broj(s4$sredina - s4$medijan, 1)` minuta. Razmak između
dviju mjera prvi je signal za pregled oblika. Sredina veća od medijana može
upućivati na rep prema većim vrijednostima, ali isti znak mogu proizvesti
mješavine skupina i složeniji oblici, pa zaključak traži graf. Mod opisuje
najčešću vrijednost i za
neprekinuto vrijeme korištenja nije koristan, ali za povjerenje mjereno cijelim
brojevima jest, gdje najčešći odgovor iznosi
`r hr_broj(s4$mod_povjerenja, 0)`. Za kategorije poput dobne skupine mod je
jedina mjera središta koja ima značenje, jer prosjek kategorija ne postoji.

## Mjere raspršenosti

Znati gdje se opažanja grupiraju tek je pola opisa. Zamislimo dva portala u
konstruiranom primjeru. Mogu imati jednak prosječan broj komentara po članku,
a na prvome svaki članak
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

Za naše podatke ta mjera iznosi `r hr_broj(s4$aad, 1)` minuta. Mnoge statističke
metode umjesto apsolutnih koriste kvadrirana odstupanja jer se takvi izrazi
lakše povezuju s kasnijim modelima. Cijena je izgubljena neposrednost, a
rezultat te zamjene je varijanca.

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

U uzorku se zbroj kvadriranih odstupanja dijeli s $n-1$, a ne s $n$. Taj se
izbor naziva Besselovom korekcijom. Za sada je dovoljno zapamtiti da sredinu
procjenjujemo iz istih podataka; zašto taj korak uklanja dugoročnu pristranost
provjerit ćemo simulacijom u poglavlju o uzorkovanju.

Razlika između uzorka i populacije od ovog mjesta ulazi i u zapis. Statistike
izračunane iz uzorka nose latinična slova, pa je sredina uzorka $\bar{x}$ a
njegova varijanca $s^2$. Nepoznate vrijednosti koje opisuju populaciju nose
grčka slova, pa je populacijska sredina $\mu$ a populacijska varijanca
$\sigma^2$. Broj opažanja u uzorku ostaje $n$, a slovo $N$ knjiga zadržava za
veličinu populacije.

U toj ćemo simulaciji mnogo puta izvući uzorak iz iste poznate populacije i
usporediti što se dugoročno događa s djeliteljima $n$ i $n-1$.

Varijanca našeg uzorka iznosi `r hr_broj(s4$varijanca, 1)`. Broj je velik i
gotovo neupotrebljiv u izvještaju, jer kvadriranje nosi i mjernu jedinicu, pa
je rezultat izražen u kvadriranim minutama. Kvadriranje istodobno objašnjava
zašto je varijanca osjetljiva na krajnje slučajeve, budući da odstupanje
dvostruko veće od drugoga u zbroj ulazi četverostruko.

## Standardna devijacija i kvartili

Korijen varijance vraća mjeru u jedinice u kojima su podaci izmjereni i time
je čini čitljivom.

**Standardna devijacija** uzorka korijen je varijance, pri čemu je varijanca
zbroj kvadriranih odstupanja od aritmetičke sredine podijeljen s $n-1$; korijen
raspršenost vraća u iste jedinice kao izmjerene vrijednosti.

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
Negativno trajanje nema sadržajno značenje. Takva donja referentna točka zato
upozorava da normalno pravilo ovdje treba provjeriti na grafu; sama po sebi ne
dokazuje oblik raspodjele.

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
proteže se od `r hr_broj(s4$q1, 1)` do `r hr_broj(s4$q3, 1)` minuta. Pomicanje
već krajnjeg opažanja obično ga ne mijenja dok to opažanje ostaje izvan
središnje polovine, premda promjena poretka na granici kvartila može promijeniti
rezultat. Zato se ta mjera s medijanom uobičajeno uparuje kao standardna
devijacija sa sredinom. Drukčiji par nije aritmetički zabranjen, ali traži
objašnjenje pitanja na koje odgovara.

## Oblik raspodjele i položaj opažanja

Središte i raspršenost ne kazuju je li raspodjela simetrična. Kada lijeva i
desna strana izgledaju kao zrcalne slike, sredina i medijan često padaju blizu
istoga mjesta. Dugi rep prema većim vrijednostima može povući sredinu za sobom,
ali njihov razmak nije samostalna mjera oblika. [Asimetrija]{.pojam
def="Mjera nesimetričnosti raspodjele, pozitivna kada je rep okrenut prema većim vrijednostima."
en="skewness" ch="4"} se zato procjenjuje iz cijele raspodjele.

Formalna mjera polazi od standardiziranih odstupanja i diže ih na treću
potenciju. Neparna potencija čuva predznak, pa velika pozitivna odstupanja
zbroj vuku prema pozitivnome, a velika negativna prema negativnome.

$$
\text{asimetrija} = \frac{1}{n} \sum_{i=1}^{n}
  \left( \frac{x_i - \bar{x}}{s} \right)^3
$$

Asimetrija simuliranoga uzorka iznosi `r hr_broj(s4$asimetrija, 2)`. Taj je
oblik svojstvo generatora ovoga nastavnog skupa, ne opća tvrdnja o medijskoj
uporabi. Isti izraz s eksponentom četiri daje koeficijent zaobljenosti
(*kurtosis*); ovdje višak nad referentnom normalnom vrijednošću iznosi
`r hr_broj(s4$visak_zaobljenosti, 2)`. Koeficijent je trag za pregled repova,
ne dokaz o njihovu uzroku ni samostalan broj krajnjih slučajeva.

**Podsjetnik.** Logaritamska skala

Kada strogo pozitivne vrijednosti imaju takav oblik, promjena ljestvice može
pomoći više od promjene mjere. Logaritam sabija velike vrijednosti i omjere
pretvara u jednake razmake, pa su omjeri 20 prema 10 i 120 prema 60 jednaki na
logaritamskoj ljestvici. Nula nema logaritam; mehaničko dodavanje jedinice nije
neutralan popravak nego nova analitička odluka.

*Slika. Dnevno vrijeme korištenja u izvornim jedinicama i na logaritamskoj ljestvici, sa sredinom i medijanom.*

Na logaritamskoj ljestvici asimetrija pada na
`r hr_broj(s4$asimetrija_log, 2)`, a sredina i medijan gotovo se poklapaju na
`r hr_broj(s4$sredina_log, 2)` i `r hr_broj(s4$medijan_log, 2)`.
Transformacija time nije popravila podatke, nego je promijenila pitanje.
Razliku dviju logaritmiranih vrijednosti treba eksponencirati da bismo dobili
njihov omjer; tek tada tvrdnja govori o višekratniku, a ne o broju minuta.

Oblik odlučuje i o tome kada je pojedino opažanje neobično. Dnevnih 100 minuta
znači jedno u skupini koja se u prosjeku zadržava 15 minuta, a nešto posve
drugo u skupini koja se zadržava 80. Položaj postaje čitljiv kada udaljenost od
sredine izrazimo u standardnim devijacijama.

**Standardizirana vrijednost** kaže koliko standardnih devijacija pojedino
opažanje leži iznad ili ispod aritmetičke sredine.

$$
z_i = \frac{x_i - \bar{x}}{s}
$$

Standardizirana varijabla ima sredinu nula i standardnu devijaciju jedan, pa
položaji vrijednosti izmjerenih u minutama i na ljestvici povjerenja postaju
usporedivi u odnosu na vlastite referentne raspodjele. Time sami konstrukti ne
postaju zamjenjivi. Standardizacija ne uklanja oblik raspodjele ni ograničenja
izvorne ljestvice, pa se krajnji položaj uvijek tumači uz prikaz podataka.

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

Za tisak i za ručnu provjeru tri stanja imaju iste točne ulaze i provjerene
sažetke. Graf pokazuje oblik, a tablica čuva brojke potrebne za račun.

*Slika. Točne vrijednosti i provjereni sažeci triju stanja widgeta 04.1. Izrada autora.*

**Statistika u divljini.**
**Mogući urednički naslov glasi „Prosječan izvor ima 153 objave.”** U DigiKatovoj
datoteci imenovanih domena
aritmetička sredina iznosi `r hr_broj(s4_izvori_sazetak$sredina, 1)` objave, ali
medijan samo `r hr_broj(s4_izvori_sazetak$medijan, 0)`. Prvih deset domena nosi
`r hr_broj(s4_izvori_sazetak$prvih_deset, 0)` od 551.712 objava, odnosno
`r paste0(hr_broj(100 * s4_izvori_sazetak$udio_prvih_deset, 2), " %")`
(Šikić, 2026). Prosjek je točan, ali bez medijana i raspodjele nije opis
tipične domene.

Tvrdnja vrijedi samo za 3.604 imenovane domene koje su prošle filtar ovoga
korpusa. Ne opisuje prosječan hrvatski medij, objavu ni korisnika, a izvorna
datoteka ne razlikuje izmjerenu nulu dosega od nedostupne metrike. Zato se iz
nje ovdje ne uspoređuju ni doseg ni interakcije.

**Pitajte model.**
Asistent može točno računati nad pogrešno izgrađenom tablicom. Prije sažetka
vrijedi mu zadati kontrolni ugovor. Neka imenuje jedinicu svakog izvora, očekuje
jedinstvenost ključa na strani šifrarnika, prijavi broj redaka i jedinstvenih
ključeva prije i nakon spajanja te uskladi ukupni zbroj. Tek poslije toga smije
primijeniti filtar, pravilo za nedostajuće vrijednosti i sažetak. Provjera
oblika raspodjele ostaje odvojena od provjere aritmetike.

> Spoji mjesečnu i godišnju DigiKatovu tablicu. Prije računa napiši što
> predstavlja redak i navedi puni ključ spajanja. Vrati broj redaka, broj
> jedinstvenih ključeva `mjesec + platforma` i zbroj objava prije i poslije
> spoja. Kod `metrika_dostupna = ne` ne tumači nulu kao izmjerenu vrijednost.

**Nađite grešku.**
Mjesečnu i godišnju tablicu spojio sam po stupcu `godina`. Dobio sam
`r hr_broj(s4_pogresni_redci, 0)` redaka i zbroj od
`r hr_broj(s4_pogresni_zbroj, 0)` objava. Tablica i dalje sadrži svih
`r hr_broj(s4_pogresni_kljucevi, 0)` različitih kombinacija
`mjesec + platforma`, a zbroj se točno dobiva iz prikazanih redaka. Spoj je
zato valjan i može se sažeti po platformi.

## Razrađeni primjer

Zadatak je opisati raspodjelu objava među imenovanim domenama u DigiKatovu
izvatku. Jedinica je domena kroz cijeli obuhvaćeni raspon, ključ je `izvor`, a
cilj nije procjena hrvatskoga medijskog prostora. Datoteka je već filtrirana na
gole internetske domene i svedena na mala slova; stranice, kanali i osobni
računi nisu u njoj. Trag transformacije zato počinje provjerom jedinstvenosti
ključa i nazivnika, ne računanjem sredine.

Provjera zaustavlja račun ako se domena ponovi ili ako zbroj više nije 551.712.
Tek nakon toga jedan redak sažetka doista opisuje 3.604 različite domene. Sredina
i medijan odgovaraju na različita pitanja, a brojnik prvih deset postaje udio
tek kada mu se pridruži puni nazivnik.

*Slika. Provjereni sažetak objava po imenovanoj domeni. Izvor: DigiKat, datoteka izvora, CC BY 4.0 [@digikat2026].*

Omjer sredine i medijana veći je od 38. Taj razmak nije formalna mjera
asimetrije, ali uz udio prvih deset domena opravdava pregled raspodjele i
upozorava da prosjek nije vrijednost tipične domene. Doseg i interakcije nisu
sažeti jer datoteka izvora nema oznaku kojom bi se njihove nule razdvojile na
izmjerene i nedostupne.

Poštena rečenica izvještaja čuva procjenu, jedinicu, predstavljeni skup i
granicu u istom dahu. Među 3.604 imenovane domene u DigiKatovu filtriranom
korpusu medijan iznosi četiri objave po domeni, dok prvih deset domena nosi
`r paste0(hr_broj(100 * s4_rezultat$prvih_deset / s4_rezultat$objave, 2), " %")`
od 551.712 objava u toj datoteci; opis se ne može generalizirati na hrvatske
medije, objave ni publiku izvan pravila ulaska u korpus.

## Sažetak

Sažetak počinje prije formule. Analitička tablica mora zadržati imenovanu
jedinicu, puni ključ, provjerljiv broj redaka, pravilo za nedostajuće vrijednosti
i nazivnik tvrdnje. Točna aritmetika ne popravlja spoj koji je umnožio retke,
a izbacivanje redaka kojima nedostaje druga metrika može promijeniti i procjenu
i predstavljeni skup. Tek nakon tih provjera odabir mjera središta,
raspršenosti i oblika određuje koji dio raspodjele čuvamo u malom broju
vrijednosti.
Standardizacija opisuje relativni položaj, transformacija mijenja ljestvicu
tvrdnje, a poštena rečenica imenuje jedinicu, obuhvat i granicu. Sljedeće
poglavlje provjerenu tablicu vraća u prostor i pokazuje kako graf postaje dio
argumenta.

## Pojmovi

analitička tablica (*analysis table*), spajanje (*join*), nedostajuća vrijednost
(*missing value*), osjetljivost na odluku o podacima (*data-decision
sensitivity*), nazivnik (*denominator*), trag transformacije (*transformation
trail*), poštena rečenica izvještaja (*honest reporting sentence*), aritmetička
sredina (*mean*), skraćena sredina (*trimmed mean*), medijan (*median*), mod
(*mode*), varijanca (*variance*), standardna devijacija (*standard deviation*),
interkvartilni raspon (*interquartile range*), standardizirana vrijednost
(*z-score*), asimetrija (*skewness*), zaobljenost (*kurtosis*)

## Zadaci

### Konceptualni

Mjesečna datoteka ima ključ `mjesec + platforma`, a godišnja `godina +
platforma`. Objasnite zašto spoj samo po godini može zadržati sva popunjena
polja, a ipak promijeniti jedinicu retka. Predajte predviđanje za broj redaka,
broj jedinstvenih mjesečnih ključeva i zbroj objava prije nego što pogledate
kontrolnu tablicu. Zatim navedite koju od te tri provjere nijedna druga ne može
zamijeniti.

### Računski

Iz tablice preseta 04.1 odaberite stanja *Zbijena* i *Krajnje opažanje*. Ručno
izračunajte njihove sredine i medijane iz svih deset navedenih vrijednosti, pa
rezultate provjerite prema posljednja dva stupca. U dvije rečenice objasnite
zašto se sredina promijenila više od medijana. Zadatak je jednak u digitalnoj i
tiskanoj inačici; interakcija služi samo za dodatne pokuse.

Druga provjera koristi upravljani agregat simulirane ankete, prikazan bez
ponovnoga zaokruživanja. Svaki redak nosi brojnik, nazivnik i cjelobrojni zbroj
uz prosjek.

*Slika. Kontrolni agregat simulirane ankete za ručnu i tiskanu provjeru. Izvor: data/anketa-mreze-agregat.csv, CC BY 4.0.*

Za šifru 1 provjerite `7339 / 90` i `90 / 300`, a zatim zbrojite četiri
brojnika i četiri zbroja minuta. Ako radite s datotekom, filtrirajte
`data/anketa-mreze.csv` na šifru 1 i iz analitičkih redaka ponovno proizvedite
cijeli prvi agregatni red; zadatak ne zahtijeva pisanje koda. U tisku su svi
potrebni brojnici, nazivnici i provjereni odgovori već u tablici.

### Kritički

Urednik objavljuje naslov „Prosječan izvor ima 153 objave”. Na temelju
DigiKatova razrađenog primjera napišite tri rečenice. Prva objašnjava što
medijan mijenja u čitanju naslova, druga imenuje 551.712 kao nazivnik udjela
prvih deset domena, a treća je poštena rečenica s jedinicom, obuhvatom i
granicom generalizacije. Ne dodajte tvrdnju o hrvatskim medijima, dosegu ili
interakcijama.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Potvrdite da je zbroj točan za tablicu
koju je model proizveo, a zatim dokažite jednu pogrešku. Usporedite 3.571 redak
s 438 jedinstvenih ključeva, imenujte izostavljeni dio ključa i navedite kakav
bi zbroj dao ispravan spoj. Završite rečenicom o tome zašto točna aritmetika
nije odgovor na pogrešno definiranu jedinicu.
