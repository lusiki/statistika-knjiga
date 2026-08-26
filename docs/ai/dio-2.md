# DIO II: OPISIVANJE PODATAKA

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

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

---

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

---

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
