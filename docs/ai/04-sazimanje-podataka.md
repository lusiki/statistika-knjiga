# Sažimanje podataka

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

DigiKat je istraživački projekt iz kojega koristimo podatke o internetskim
objavama s katoličkim pojmovima. U odabrani korpus, odnosno skup tekstova za
analizu, ulaze praćene objave koje sadrže najmanje dva različita pojma s
projektnog popisa (Šikić, 2026). Pred nama su tri zbirne tablice. Dvije
prikazuju objave po platformama, mjesečno i godišnje, a treća po internetskim
domenama (Šikić, 2026). Zamislimo urednika koji iz njih želi saznati koliko
objava ima tipičan izvor.

Prije tumačenja treba provjeriti što je zapravo uspoređeno. Redak u prvim
dvjema tablicama predstavlja platformu u određenom razdoblju, a u trećoj
domenu tijekom cijelog obuhvata. Mjesečnu i godišnju tablicu povezujemo prema
dvama poljima. Neke nule angažmana označuju nedostupnu metriku. Uz to tablica
domena obuhvaća 551.712 objava, a platformske 710.307. Pogrešan spoj ili
nazivnik zato može promijeniti odgovor i uz točnu aritmetiku.

Kako provjeriti tablicu prije računanja sažetaka?

Što bismo uredniku odgovorili o tipičnom izvoru kada bismo smjeli pokazati
samo jedan broj? Prosjek broja objava čini se prirodnim izborom, ali možda
prikriva da najveći dio objava dolazi iz malog dijela izvora. Prije izračuna
trebamo riješiti još jedno pitanje. Moramo biti sigurni da zbrajamo usporedive
zapise i da odsutno mjerenje nismo zamijenili izmjerenom nulom.

Dosadašnja pitanja o jedinici, nazivniku i podrijetlu podataka sada
primjenjujemo pri pripremi vlastite analize. Polazimo od stvarnih zbirnih
tablica projekta DigiKat (Šikić, 2026). U njima redak predstavlja platformu u
određenom razdoblju ili internetsku domenu tijekom obuhvata datoteke. Broj
objava, doseg i interakcije različite su veličine, a njihova dostupnost nije
jednaka. Provjerit ćemo koji se zapisi mogu spojiti, što pritom mora ostati
nepromijenjeno i koje vrijednosti možemo uključiti u sažetak.

Ponašanje pojedinih mjera zatim ćemo istražiti na skupu `anketa_mreze`,
zasebnoj simuliranoj anketi u kojoj jedan redak predstavlja zamišljenu osobu s
dobi, dnevnim minutama na društvenim mrežama i ocjenom povjerenja u tamošnji
sadržaj. Taj skup nije uzorak iz ranije uvedene populacije
medijskih navika. Na njemu možemo usporediti različite opise istih odgovora,
bez predstavljanja tih odgovora kao nalaza o stvarnim korisnicima.

Sredina i medijan opisuju središte raspodjele, a mjere raspršenosti razlike
među opažanjima. Njihovu prikladnost provjeravamo prema obliku podataka i
reakciji na pomicanje krajnjih vrijednosti. Standardizacijom opisujemo
položaj opažanja u odnosu na ostala. Na kraju se vraćamo DigiKatovim
domenama i sastavljamo brojčani opis s jasno navedenim značenjem i granicom
svake mjere.

## Od izvora do sažetka

Za vlastitu analizu trebamo [analitičku tablicu]{.pojam def="Tablica čiji
svaki red predstavlja unaprijed imenovanu jedinicu analize i nosi samo
provjerene varijable potrebne za pitanje." en="analysis table" ch="4"}. Pri
njezinoj izradi određujemo što predstavlja redak, kojim ključem povezujemo
zapise i kako tumačimo kodove. Bilježimo filtre i pravila za nedostajuće
vrijednosti kako bi druga osoba mogla ponoviti postupak.

### Tri tablice, tri jedinice

DigiKatov izbor tekstova određuje i granicu našeg zaključka. Tablice opisuju
objave obuhvaćene pravilima projekta, a ne slučajan uzorak hrvatskih medija,
publike ili korisnika (Šikić, 2026). Raspolažemo već izračunatim zbrojevima,
bez pojedinačnih objava. Prije računanja zato provjeravamo predstavljaju li
retci različitih datoteka usporedive jedinice.

*Slika. Tri pogleda u paketu DigiKat imaju različite jedinice i ključeve. Izvor: DigiKat, agregatni izvadak, CC BY 4.0 [@digikat2026].*

Datoteka domena nema zajednički ključ s platformskim tablicama pa je
analiziramo zasebno. Ona pokazuje raspored objava među domenama. Mjesečne i
godišnje podatke o platformama možemo povezati parom `godina + platforma`. Izostavljanjem
jednog dijela ključa spojili bismo zapise koji ne pripadaju istoj jedinici.

U mjesečnoj tablici, primjerice, jedan redak bilježi 11.701 obuhvaćenu
objavu na webu u siječnju 2021. (Šikić, 2026). U tablici domena redak za `hkm.hr` bilježi
56.500 objava kroz cijeli obuhvaćeni raspon (Šikić, 2026). Prvi broj
opisuje platformu i mjesec, a drugi jednu domenu kroz više godina. Nijedan
ne broji jedinstvene čitatelje.

### Ključ prije sažetka

Mjesečna tablica ima `r hr_broj(nrow(s4_mjesecno), 0)` redaka, svaki s jedinstvenim ključem `mjesec + platforma`.
Iz godišnje joj tablice pridružujemo godišnji nazivnik i oznaku potpunosti.
Nakon ispravnog spajanja broj redaka i ukupan broj objava moraju ostati isti.
Ako spojimo samo po godini, svaki mjesečni redak dobit će par sa svim
platformama te godine i pojavit će se više puta.

Za dva mjesečna zapisa weba vidimo što je spoj dodao. Mjesec i njegov broj
objava dolaze iz mjesečne datoteke, a ukupni godišnji nazivnik iz godišnje.
Tražimo podudaranje i godine i platforme. Oba mjesečna zapisa tako dobivaju
isti godišnji nazivnik, bez ponovnog brojanja njihovih objava.

*Slika. Dva mjesečna retka nakon pridruživanja godišnjeg nazivnika. Izrada autora prema @digikat2026.*

U sljedećoj tablici uspoređujemo broj redaka, jedinstvene mjesečne ključeve
i zbroj objava prije i nakon ispravnog spajanja.

*Slika. Kontrola retka, ključa i zbroja prije i nakon ispravnog spajanja DigiKatovih agregata. Izvor: DigiKat [@digikat2026].*

Provjeravamo i pojedine ćelije, jer jednak ukupan zbroj ne jamči njihovo
slaganje. Mjesečni i godišnji izvadak razlikuju se u `r hr_broj(s4_broj_odstupanja, 0)` od 49
kombinacija platforme i godine, a odstupanja se u ukupnom zbroju poništavaju.
Zato ne zamjenjujemo mjesečne vrijednosti godišnjima i ne gradimo neprekinut
trend. Za daljnju analizu koristimo potpunu 2025. godinu, uz isključenje 2024.
zbog praznine i promjene metode. U 2024. nedostaju mjesečni retci od veljače
do svibnja, siječanj je djelomičan, a lipanj označuje promjenu metode i
obuhvata (Šikić, 2026).

### Kada nula znači da mjera nije dostupna

U podacima za 2025. svih devet platformi ima zabilježen broj objava. Za tri od
njih nema usporedivog podatka o dosegu i interakcijama. Ondje zapisana nula,
uz oznaku `metrika_dostupna = ne`, znači da mjerenje nije dostupno. Izvorni stupac čuvamo, a
za analizu izrađujemo novi u kojem te nule označujemo kao nedostajuće
vrijednosti.

Primjerice, u mjesečnom retku za `reddit` izvorno je uz interakcije zapisana
nula, ali oznaka dostupnosti glasi `ne`. Analitički zapis zato čuva broj
objava, a interakcije pretvara u oznaku nedostajanja. Redak ne brišemo niti
njegovu nulu uključujemo u prosjek interakcija.

To se odnosi na platforme `reddit`, `forum` i `comment`, koje zajedno imaju
`r hr_broj(s4_2025_objave_nemjerene, 0)` objava. Metapodaci potvrđuju da metrika nedostaje zbog načina
mjerenja. Broj objava zato možemo sažeti za svih devet platformi, a angažman
samo za šest s dostupnom metrikom. Učinak sužavanja skupa provjeravamo na
broju objava, koji poznajemo za sve platforme. Doseg i interakcije
nedostajućih platformi ne možemo tako usporediti.

*Slika. Osjetljivost medijana broja objava na nepotrebno izbacivanje platformi kojima nedostaje druga metrika. Presjek je potpuna 2025. godina; angažman i doseg ne uspoređuju se. Izvor: DigiKat [@digikat2026].*

Medijan, središnja vrijednost u poredanom nizu, mijenja se s `r hr_broj(s4_medijan_sve_platforme, 1)` na `r hr_broj(s4_medijan_mjerene_platforme, 1)` objava. Usporedili smo svih devet
vrsta platformi sa šest koje imaju metriku angažmana. Promijenio se skup na
koji se rezultat odnosi. O dosegu i interakcijama preostalih triju platformi i
dalje nemamo podatke.

Za ručnu provjeru poredani brojevi objava po platformama u 2025. iznose
231, 1.641, 1.779, 2.122, 2.724, 4.228, 26.891, 44.502 i 152.048
(Šikić, 2026). Izbacivanjem platformi bez metrike angažmana uklanjamo
vrijednosti 1.641, 1.779 i 4.228 (Šikić, 2026).

### Nazivnik je dio tvrdnje

Za udio trebamo znati i ukupnu količinu. Ako riječi brojimo prema razmacima,
ne razlikujući velika i mala slova, *Analysis* se u naslovu *Exploratory Data
Analysis* pojavljuje jednom među trima riječima (Tukey, 1977). U naslovu
*Statistical Power Analysis for the Behavioral Sciences* također se pojavljuje
jednom, ali među sedam riječi (Cohen, 1988). Učestalost je ista, dok se udjeli
razlikuju zbog duljine naslova.

Tablica imenovanih domena ima `r hr_broj(nrow(s4_izvori), 0)` redaka i ukupno `r hr_broj(s4_izvori_sazetak$objave, 0)` objava. Za
udjele objava među tim domenama zato koristimo nazivnik 551.712. Nazivnik
710.307 iz platformskih tablica odnosi se na drugi obuhvat.

Ponašanje sredine i drugih mjera lakše ćemo pratiti na tablici pojedinačnih
odgovora. Zato prelazimo na skup `anketa_mreze`, simuliranu anketu s `r s4$n`
ispitanika. Jedan redak predstavlja jednu zamišljenu osobu. Za
nju su zadani dob, dnevne minute na društvenim mrežama i povjerenje u tamošnji
sadržaj na ljestvici od 1 do 10. To je zaseban skup, a ne uzorak
iz ranije uvedene populacije medijskih navika.

Generator je zadao četiri dobne skupine s 90, 84, 66 i 60 osoba. Unutar
svake dob je slučajno odabrana iz njezina raspona, a minute nastaju zasebnim
izvlačenjem pozitivnih, desno asimetričnih vrijednosti. Tipična vrijednost
minuta niža je u starijim skupinama. Zaokruživanjem zadržavamo barem jednu
minutu. Povjerenju također zadajemo niže prosjeke u starijim skupinama, uz
slučajna odstupanja i granice ljestvice od 1 do 10.

Nekoliko pojedinačnih zapisa omogućuje da prije prosjeka vidimo što se
zbraja. Oznaka ispitanika služi razlikovanju redaka; dnevne minute i ocjena
povjerenja dvije su odvojene varijable.

*Slika. Tri zapisa iz zasebne simulirane ankete o društvenim mrežama. Izrada autora.*

Na istoj ćemo anketi poslije usporediti grafove, izračunati povezanost i
sastaviti završno istraživanje. Vrijednosti su stvorene tako da većina osoba
provodi kraće vrijeme na mrežama, a manji dio znatno dulje. Takav
oblik omogućuje da vidimo zašto sredina i medijan daju različite opise. Ne
predstavlja nalaz o stvarnim medijskim navikama.

**Dnevnik transformacija** bilježi što smo promijenili između izvora i
analize, prema kojem pravilu i s kakvim učinkom na broj redaka ili rezultat.
Ovdje u njega pripadaju ključ spajanja, isključeno razdoblje i razlikovanje
nedostupne metrike od nule. **Osjetljivost na odluku o podacima** znači da
provjerimo mijenja li se zaključak uz drugu opravdanu odluku, primjerice uz
drukčiji obuhvat dostupnih platformi.

**Poštena rečenica izvještaja** imenuje jedinicu, obuhvat, mjeru i granicu
zaključka. Rečenica o medijanu objava po domeni zato mora reći odnosi li se
na sve domene ili samo one s dostupnom metrikom. Uz uzoračku procjenu dodaje
se odgovarajući opis nesigurnosti. Precizan broj bez tih podataka ostavlja
čitatelju da sam izmisli doseg tvrdnje.

### Mjere središta

Prosjek dobivamo kada ukupno vrijeme ravnomjerno rasporedimo među
ispitanicima. U formuli $n$ označuje broj opažanja, a $x_i$ vrijednost za
pojedinog ispitanika. Crta iznad slova označuje aritmetičku sredinu tih
vrijednosti.

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

**Aritmetička sredina** je zbroj svih izmjerenih vrijednosti podijeljen njihovim
brojem.

Zbroj minuta svih 300 osoba iznosi `r hr_broj(sum(s4_minute), 0)`.
Dijeljenjem toga zbroja s 300 dobivamo `r hr_broj(s4$sredina, 2)` minuta.
Tri prikazana retka samo su početak toga zbrajanja. Nijedan od 300 odgovora
ovdje ne nedostaje.

Sredina iznosi `r hr_broj(s4$sredina, 1)` minuta dnevno, ali samo `r paste0(hr_broj(s4$iznad, 0), " %")` ljudi
provodi više vremena od toga. Ukupno smo vrijeme ravnomjerno podijelili među
svim ispitanicima, pa su i rijetke velike vrijednosti podigle dobiveni broj.
Ako nas zanima osoba u sredini poretka, trebamo drukčiji sažetak. Do njega ćemo
doći promatrajući što se događa kada krajnjim vrijednostima postupno smanjujemo
utjecaj.

Utjecaj krajnjih vrijednosti možemo ublažiti **skraćenom sredinom** (*trimmed
mean*). Poredamo opažanja, uklonimo unaprijed zadan jednak udio s oba kraja i
izračunamo sredinu ostatka. U našem uzorku po 5 % znači 15 najmanjih i 15
najvećih vrijednosti, pa novi zbroj dijelimo s 270. Uz po 10 % ostaje 240
vrijednosti. Nakon uklanjanja po 5 % s oba kraja ovdje dobivamo
`r hr_broj(s4$skracena5, 1)` minuta, a uz po 10 % dobivamo `r hr_broj(s4$skracena10, 1)`.

Nastavimo li uklanjati vrijednosti s oba kraja, približavamo se medijanu,
središtu poredanog niza. Različit odnos prema krajnjim vrijednostima možemo
izraziti i računom odstupanja. Zbroj kvadriranih odstupanja najmanji je kada ih računamo od sredine.
Kvadriranjem velika odstupanja dobivaju veću težinu. Medijan pak daje
najmanji zbroj apsolutnih odstupanja, bez njihova kvadriranja. Zato te dvije mjere ne
moraju odabrati istu vrijednost kao središte podataka.

**Medijan** je vrijednost koja poredani niz opažanja dijeli na dvije jednako
velike polovine.

U poredanih 300 odgovora središnja su mjesta 150 i 151. Na njima su
`r sort(s4_minute)[150]` i `r sort(s4_minute)[151]` minuta. Njihov prosjek daje
medijan. Dakle, mijenjamo redoslijed istih zapisa, a ne osobe koje opisujemo.

Medijan je `r hr_broj(s4$medijan, 0)` minuta, što je `r hr_broj(s4$sredina - s4$medijan, 1)` minuta manje od sredine. Takav
razmak potiče nas da pogledamo graf. Može nastati zbog repa prema velikim
vrijednostima, ali i zbog mješavine skupina ili složenijeg oblika raspodjele.
Još jedna mjera središta, mod, označuje najčešću vrijednost. Za kontinuirano
vrijeme korištenja ovdje nam malo koristi, dok za cjelobrojne odgovore o
povjerenju iznosi `r hr_broj(s4$mod_povjerenja, 0)`. Kod kategorija mod pokazuje koja je najčešća, bez
računanja prosjeka kategorijskih oznaka.

## Mjere raspršenosti

Uz središte trebamo opisati koliko se vrijednosti razlikuju. Zamislimo dva
portala s istim prosjekom komentara po članku. Na prvom svaki članak ima
između 45 i 55 komentara. Na drugom neki nemaju nijedan, a poneki imaju 200.
Prosjek ne pokazuje tu razliku u raspodjeli.

Raspon je razlika najveće i najmanje vrijednosti. Vrijeme u našem uzorku kreće
se od `r hr_broj(s4$najmanje, 0)` do `r hr_broj(s4$najvise, 0)` minuta, uz raspon od `r hr_broj(s4$raspon, 0)` minuta. Raspon
ovisi samo o dvama krajnjim opažanjima, pa ne govori kako su raspoređena
ostala.

Za potpuniji opis razmatramo odstupanje svake vrijednosti od sredine. Njegova
apsolutna vrijednost daje udaljenost bez obzira na smjer. Prosjek tih
udaljenosti, prosječno apsolutno odstupanje, govori koliko se opažanja u
prosjeku udaljavaju od sredine.

$$
\text{PAO} = \frac{1}{n} \sum_{i=1}^{n} |x_i - \bar{x}|
$$

Ovdje prosječno apsolutno odstupanje iznosi `r hr_broj(s4$aad, 1)` minuta. Umjesto
apsolutnih odstupanja mnogi postupci koriste kvadrirana jer ih je lakše
povezati s kasnijim modelima. Tako dolazimo do varijance, koju je nešto teže
izravno protumačiti.

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

Za varijancu uzorka zbroj kvadriranih odstupanja dijelimo s $n-1$. To je
Besselova korekcija. Povezana je s time što smo sredinu procijenili iz istog
uzorka. U poglavlju o uzorkovanju simulacijom ćemo vidjeti zašto takvo
dijeljenje uklanja dugoročnu pristranost procjene.

Uzoračke veličine zapisujemo latiničnim slovima. Sredina je $\bar{x}$, a
varijanca $s^2$. Populacijsku sredinu označujemo grčkim slovom $\mu$, a
populacijsku varijancu oznakom $\sigma^2$. Veličina uzorka je $n$, dok $N$
označuje veličinu populacije.

U toj ćemo simulaciji mnogo puta izvući uzorak iz iste poznate populacije i
usporediti što se dugoročno događa s djeliteljima $n$ i $n-1$.

Prva osoba ima `r s4_minute[1]` minuta. Odstupanje od sredine iznosi
`r hr_broj(s4_minute[1] - s4$sredina, 2)`, a njegov kvadrat
`r hr_broj((s4_minute[1] - s4$sredina)^2, 2)`. Takav kvadrat računamo za
svaku osobu, zbrajamo svih 300 vrijednosti i dijelimo s 299. Kvadrat računamo
iz nezaokruženog odstupanja, a ne iz njegova prikaza na dvije decimale.

Varijanca iznosi `r hr_broj(s4$varijanca, 1)` kvadriranih minuta. Kvadrira se i mjerna jedinica,
zbog čega broj nije lako tumačiti u izvještaju. Kvadriranje također povećava
utjecaj krajnjih vrijednosti. Dvostruko veće odstupanje pridonosi zbroju
četverostruko više.

## Standardna devijacija i kvartili

Vađenjem korijena iz varijance vraćamo se na izvornu mjernu jedinicu, ovdje
minute.

**Standardna devijacija** uzorka korijen je varijance. Varijancu računamo
dijeljenjem zbroja kvadriranih odstupanja od sredine s $n-1$, a korijen vraća
raspršenost u jedinice izvornih vrijednosti.

$$
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

Standardna devijacija ovdje iznosi `r hr_broj(s4$sd, 1)` minuta i veća je od prosječnog
apsolutnog odstupanja od `r hr_broj(s4$aad, 1)` minuta. Kvadriranje daje veću težinu
velikim odstupanjima. Zato standardnu devijaciju možemo samo približno opisati
kao tipičnu udaljenost od sredine.

Za normalnu raspodjelu, koju ćemo razraditi u poglavlju o vjerojatnosti,
postoji korisno pravilo. U približno normalnoj raspodjeli oko 68 % opažanja nalazi se unutar jedne
standardne devijacije od sredine, oko 95 % unutar dviju, a oko 99,7 % unutar
triju. U našem je uzorku unutar jedne devijacije `r paste0(hr_broj(s4$u_jednoj_sd, 1), " %")` ispitanika. Raspon
dviju devijacija ide od minus `r hr_broj(abs(s4$donja_dvije), 1)` do `r hr_broj(s4$gornja_dvije, 1)` minuta. Budući da
trajanje ne može biti negativno, taj raspon upozorava da trebamo provjeriti
odgovara li normalno pravilo podacima. Sam po sebi ipak ne određuje oblik
raspodjele.

Unutar dviju devijacija ovdje se nalazi `r paste0(hr_broj(s4$u_dvije_sd, 1), " %")` ispitanika, gotovo kao prema
normalnom pravilu. Jedno takvo podudaranje ne potvrđuje da je cijela
raspodjela približno normalna. Za to treba pregledati podatke.

Ako želimo opis raspršenosti koji manje ovisi o krajnjim vrijednostima,
možemo se, kao kod medijana, osloniti na položaje u poredanom nizu. **Percentil** je
vrijednost ispod koje se nalazi zadani postotak opažanja, pa je medijan
pedeseti percentil. Prvi kvartil odvaja donjih 25 %, a treći gornjih 25 %.
Njihova razlika obuhvaća raspon središnje polovine podataka.

*Slika. Percentili dnevnog vremena korištenja u simuliranoj anketi. Izrada autora.*

Taj interkvartilni raspon ovdje iznosi `r hr_broj(s4$iqr, 1)` minuta, od `r hr_broj(s4$q1, 1)` do
`r hr_broj(s4$q3, 1)` minuta. Pomicanje opažanja koje već leži daleko izvan središnje
polovine obično ga ne mijenja. Promjena poretka oko kvartila ipak može
utjecati na rezultat. Interkvartilni raspon često navodimo uz medijan, a
standardnu devijaciju uz sredinu. Druge kombinacije mogu biti korisne ako
objasnimo čemu služe.

## Oblik raspodjele i položaj opažanja

Graf nam pokazuje i oblik raspodjele. U simetričnoj raspodjeli dvije strane
približno su zrcalne i sredina je često blizu medijana. Dugi rep prema većim
vrijednostima može povući sredinu naviše. Njihov razmak ipak nije dovoljan
opis oblika. [Asimetrija]{.pojam def="Mjera nesimetričnosti raspodjele,
pozitivna kada je rep okrenut prema većim vrijednostima." en="skewness"
ch="4"} uzima u obzir cijelu raspodjelu.

Dugi rep koji smo naslutili iz razmaka sredine i medijana želimo opisati i
brojem koji razlikuje dvije strane raspodjele. Zato odstupanja najprije
izražavamo u standardnim devijacijama, a zatim ih dižemo na treću potenciju.
Neparna potencija čuva njihov predznak. Velika pozitivna odstupanja tako vuku
zbroj prema pozitivnome, a velika negativna prema negativnome.

$$
\text{asimetrija} = \frac{1}{n} \sum_{i=1}^{n}
  \left( \frac{x_i - \bar{x}}{s} \right)^3
$$

Asimetrija simuliranog uzorka iznosi `r hr_broj(s4$asimetrija, 2)` i proizlazi iz načina
generiranja podataka. Ne govori o stvarnoj medijskoj uporabi. Ako u izrazu
upotrijebimo četvrtu potenciju, dobivamo koeficijent zaobljenosti
(*kurtosis*). Njegov višak nad referentnom normalnom vrijednošću ovdje je
`r hr_broj(s4$visak_zaobljenosti, 2)`. On pomaže pri pregledu repova raspodjele, ali ne objašnjava njihov
uzrok ni broj krajnjih slučajeva. Ovdje koristimo prosjek trećih odnosno
četvrtih potencija odstupanja standardiziranih uzoračkom standardnom
devijacijom, bez korekcije za mali uzorak. Od četvrtog momenta oduzimamo tri.
Drugi programski postupci mogu koristiti drukčiju korekciju, pa uz usporedbu
vrijednosti treba provjeriti i definiciju.

**Podsjetnik.** Logaritamska skala

Za strogo pozitivne vrijednosti možemo razmotriti logaritamsku ljestvicu. Ona
sabija velike vrijednosti i jednake omjere prikazuje jednakim razmacima.
Omjeri 20 prema 10 i 120 prema 60 zato imaju isti razmak. Nulu ne možemo
logaritmirati. Dodavanje jedinice svim vrijednostima mijenja analizu i traži
obrazloženje.

*Slika. Dnevno vrijeme korištenja u izvornim jedinicama i na logaritamskoj ljestvici, sa sredinom i medijanom. Logaritamska ljestvica sažima dugi desni rep. Izrada autora.*

Isti se odgovor sada zapisuje na drugoj ljestvici. Prvih
`r s4_minute[1]` minuta postaje $\ln(`r s4_minute[1]`) =
`r hr_broj(log(s4_minute[1]), 2)`$. Sve su minute pozitivne, pa transformiramo
svih 300 odgovora bez izostavljanja. To nisu nove osobe ni ponovljena mjerenja.

Nakon logaritmiranja asimetrija iznosi `r hr_broj(s4$asimetrija_log, 2)`, a sredina i medijan bliski
su, `r hr_broj(s4$sredina_log, 2)` i `r hr_broj(s4$medijan_log, 2)`. Sada, međutim, tumačimo drugu ljestvicu.
Eksponenciranjem razlike logaritama dobivamo omjer izvornih vrijednosti.
Rezultat govori o višekratniku, a ne o razlici minuta.

Uz oblik raspodjele zanima nas i položaj pojedine osobe u njoj. Dnevnih 100 minuta može biti mnogo u skupini s prosjekom od 15 minuta, a manje
neobično u skupini s prosjekom od 80. Da bismo opisali položaj, udaljenost od
sredine izražavamo brojem standardnih devijacija.

**Standardizirana vrijednost** kaže koliko standardnih devijacija pojedino
opažanje leži iznad ili ispod aritmetičke sredine.

$$
z_i = \frac{x_i - \bar{x}}{s}
$$

Standardizirana varijabla ima sredinu nula i standardnu devijaciju jedan. Tako
možemo usporediti relativni položaj osobe prema vremenu korištenja i prema
povjerenju, svako unutar njegove raspodjele. Time vrijeme i povjerenje ne
postaju isti pojam. Standardizacija također ne mijenja oblik raspodjele ni
ograničenja ljestvice, pa uz krajnje vrijednosti i dalje gledamo graf.

Moramo navesti i referentnu skupinu. Položaj u cijelom uzorku može se
razlikovati od položaja unutar dobne skupine, čak i po predznaku. Za
najstariju skupinu sredina iznosi
`r hr_broj(mean(anketa_mreze$minute_dnevno[anketa_mreze$dobna_skupina == "45 i više"]), 4)`
minute, a standardna devijacija
`r hr_broj(sd(anketa_mreze$minute_dnevno[anketa_mreze$dobna_skupina == "45 i više"]), 4)`
minuta; račun koristi nezaokružene vrijednosti.

*Slika. Tri ispitanika iz najstarije skupine, standardizirani u cijelom uzorku i unutar vlastite skupine. Izrada autora.*

Osobe iz tablice provode manje vremena od prosjeka cijelog uzorka, a u svojoj
su dobnoj skupini među najintenzivnijim korisnicima. Obje tvrdnje mogu biti
točne jer koriste različite referentne skupine. U izvještaju zato navodimo
prema kojoj je skupini položaj izračunat.

## Interakcija — Oblikovanje distribucije

Tri raspodjele prikazuju utjecaj krajnjeg opažanja i raspršenosti ostalih
vrijednosti. Usporedba sredine, medijana i mjera raspršenosti pokazuje koje
mjere jače reagiraju na pojedinu vrijednost, a koje više ovise o poretku.

*Slika. Reakcija mjera središta i raspršenosti na oblik konstruirane raspodjele.*

**Što isprobati.**

1. Spustite krajnje opažanje sa 70 na 14 i usporedite sredinu s medijanom.
2. Vratite ga na 70 i provjerite koja se mjera središta više pomaknula.
3. Postavite krajnje opažanje na 11 pa povećajte faktor raspršenosti i
   usporedite dvije raspodjele iste sredine.

Uz graf su u tablici navedene vrijednosti za sva tri stanja i njihovi sažeci.
Na njima se račun može provjeriti ručno.

*Slika. Točne vrijednosti i sažeci triju prikazanih raspodjela. Izrada autora.*

**Statistika u divljini.**
**Prosječan izvor i tipična domena.** Urednik iz uvodnog primjera želi
opisati koliko se katolička tematika pojavljuje u izvorima koje DigiKat
prati. Za naslov razmatra rečenicu da prosječan izvor ima 153 objave.
U toj zamišljenoj uredničkoj odluci koristimo stvarnu tablicu domena,
ali ne opisujemo naslov koji je netko doista objavio.

Sredina tablice iznosi `r hr_broj(s4_izvori_sazetak$sredina, 1)` objave,
dok je medijan `r hr_broj(s4_izvori_sazetak$medijan, 0)`
(Šikić, 2026). Razlika nije posljedica pogrešnog računa. Kada bi svaka
domena nosila jednak dio svih objava, dobila bi vrijednost sredine.
Kada domene poredamo prema broju objava i pogledamo sredinu toga niza,
dobivamo medijan. Urednik treba odlučiti koju od tih dviju slika želi
prenijeti čitatelju.

Raspored objava objašnjava zašto je odluka važna. Prvih deset domena
ima `r hr_broj(s4_izvori_sazetak$prvih_deset, 0)` od ukupno 551.712
objava, odnosno `r paste0(hr_broj(100 * s4_izvori_sazetak$udio_prvih_deset, 2), " %")`
(Šikić, 2026). Ako naslov treba približiti tipičnu domenu, sama
sredina mogla bi stvoriti dojam da je mnogo objava uobičajeno za većinu
izvora. Ako istraživanje zanima gdje se objave koncentriraju, samo
medijan ne bi pokazao ulogu najvećih domena.

Urednik zato može uz opis tipične domene prikazati koliko objava nose
najveći izvori. Te se informacije dopunjuju. Pritom treba zadržati
ograničenje da opisujemo 3.604 imenovane domene uključene prema
pravilima DigiKatova korpusa, a ne sve hrvatske medije
(Šikić, 2026). Broj objava također nije broj čitatelja. Iz ovih
sažetaka ne zaključujemo koji izvor ima najveći utjecaj ili doseg.

Izbor mjere tako mijenja priču koju ista tablica podržava. Za pitanje
o tipičnom izvoru tražimo njegov položaj u raspodjeli. Za pitanje o
koncentraciji trebamo pogledati koliko ukupnog broja objava pripada
malom dijelu izvora. Riječ prosjek ne može sama obaviti oba posla.

Prije računanja sažetaka trebamo provjeriti što jedan redak predstavlja
nakon povezivanja tablica. Sljedeći zapis omogućuje takav pregled.

**Nađite grešku.**
Prije sažimanja objava po platformi pregledajte zapis spajanja
DigiKatovih tablica (Šikić, 2026). Redak mjesečne tablice predstavlja
platformu u mjesecu, a redak godišnje platformu u godini. U mjesečnoj je
tablici jedinstvena kombinacija `mjesec + platforma`; u godišnjoj se ista
godina pojavljuje uz više platformi.

Asistent je spojio mjesečnu i godišnju tablicu te priložio provjeru.
Zbroj se odnosi na broj objava iz mjesečne tablice.

| Provjera | Prije spajanja | Nakon spajanja |
|---|---:|---:|
| Broj redaka | 438 | `r hr_broj(s4_pogresni_redci, 0)` |
| Različite kombinacije mjeseca i platforme | 438 | `r hr_broj(s4_pogresni_kljucevi, 0)` |
| Zbroj objava | 710.307 | `r hr_broj(s4_pogresni_zbroj, 0)` |

: Provjera ulazne i spojene tablice. Izrada autora prema digikat2026.

> Sve početne kombinacije mjeseca i platforme ostale su u rezultatu.
> Zbroj objava točno odgovara dobivenim redcima. Spoj je zato valjan i
> tablicu možemo sažeti po platformi.

Odlučite može li tablica u sljedeći korak analize. Pokažite koji podatak
podupire vašu odluku, navedite potpuni ključ spajanja i zapišite broj
redaka te zbroj objava koje treba dobiti nakon popravka. Zadržite ono što
je u asistentovoj provjeri doista točno.

## Razrađeni primjer

Na simuliranim minutama vidjeli smo zašto uz sredinu trebamo i druge opise
raspodjele. Sada se vraćamo urednikovu pitanju o tipičnom izvoru u DigiKatovu
izvatku. Redak predstavlja domenu tijekom cijelog obuhvaćenog razdoblja, a
ključ je `izvor`. Datoteka već sadržava samo internetske domene
zapisane malim slovima, bez stranica, kanala i osobnih računa. Najprije
provjeravamo jedinstvenost domena i ukupan broj objava, a zatim biramo sažetke
za opis ovog korpusa. Ne procjenjujemo stanje u cijelom hrvatskom medijskom
prostoru.

Sljedeći programski račun služi dodatnoj provjeri. Objekt `s4_izvori`
sadržava retke datoteke `data/digikat-izvori.csv`, a funkcije za sažimanje
pripadaju paketu dplyr. Priprema podataka opisana je u mrežnom R praktikumu.
Račun i bez pokretanja koda možemo pratiti prema brojčanim provjerama u tekstu.

Ako se domena ponovi ili zbroj odstupi od 551.712, zaustavljamo račun i
provjeravamo razlog. Nakon uspješne provjere možemo sažeti 3.604 različite
domene. Sredina i medijan opisuju različite aspekte raspodjele, a udio objava
prvih deset domena računamo prema ukupnom broju objava u datoteci.

*Slika. Provjereni sažetak objava po imenovanoj domeni. Izvor: DigiKat, datoteka izvora, CC BY 4.0 [@digikat2026].*

Sredina je više od 38 puta veća od medijana. To nije formalna mjera
asimetrije, ali uz koncentraciju objava u prvih deset domena pokazuje zašto
treba pregledati raspodjelu. Prosjek ne predstavlja tipičnu domenu. Doseg i
interakcije izostavljamo jer njihove nule u ovoj datoteci ne možemo pouzdano
protumačiti.

Rezultat možemo opisati ovako. U DigiKatovu filtriranom korpusu od 3.604
imenovane domene medijan je četiri objave po domeni. Prvih deset domena ima
`r paste0(hr_broj(100 * s4_rezultat$prvih_deset / s4_rezultat$objave, 2), " %")` od 551.712 objava. Opis vrijedi za domene uključene prema pravilima
korpusa i ne prenosimo ga na ostale hrvatske medije, objave ili publiku.

## Sažetak

Sažetak može odgovoriti na naše pitanje tek kada znamo što predstavlja svaki
redak, jesu li zapisi ispravno spojeni, kako su označene nedostajuće
vrijednosti i koji nazivnik koristimo. Pogrešan spoj može umnožiti zapise, a
isključivanje redaka mijenja skup koji opisujemo, pa ni točan račun ne može
nadomjestiti te provjere. Na provjerenoj tablici biramo mjere središta i raspršenosti prema obliku
raspodjele. Standardizacijom opisujemo relativni položaj opažanja, a
transformacijom mijenjamo ljestvicu. Uz odabrane mjere zato zadržavamo
jedinicu i obuhvat, kao i ono što se jednim brojem ne može opisati. U poglavlju
o vizualizaciji graf će nam pomoći vidjeti upravo te pojedinosti.

## Pojmovi

analitička tablica (*analysis table*), spajanje (*join*), nedostajuća vrijednost
(*missing value*), osjetljivost na odluku o podacima (*data-decision
sensitivity*), nazivnik (*denominator*), dnevnik transformacija (*transformation log*), poštena rečenica izvještaja (*honest reporting sentence*), aritmetička
sredina (*mean*), skraćena sredina (*trimmed mean*), medijan (*median*), mod
(*mode*), varijanca (*variance*), standardna devijacija (*standard deviation*),
interkvartilni raspon (*interquartile range*), standardizirana vrijednost
(*z-score*), asimetrija (*skewness*), zaobljenost (*kurtosis*)

## Zadaci

Nakon vlastitog pokušaja otvorite naznake i provjere rješenja.

### Konceptualni

Mjesečna datoteka ima ključ `mjesec + platforma`, a godišnja `godina +
platforma`. Objasnite zašto spoj samo po godini može zadržati sva popunjena
polja, a ipak promijeniti jedinicu retka. Uz pomoć kontrolne tablice objasnite što provjeravaju broj redaka,
broj jedinstvenih mjesečnih ključeva i zbroj objava. Zatim navedite koju od te tri provjere nijedna druga ne može
zamijeniti.

### Računski

Iz tablice zadanih vrijednosti uzmite stanja *Zbijena* i *Krajnje opažanje*. Iz svih
deset vrijednosti ručno izračunajte sredine i medijane te ih usporedite s
posljednjim dvama stupcima. U dvije rečenice objasnite zašto se sredina
promijenila više od medijana. Za stanje *Zbijena* izračunajte i uzoračku
standardnu devijaciju, koristeći djelitelj devet. U tablici raspršenosti
usporedite promjene SD-a i IQR-a nakon zamjene krajnjeg opažanja. Koja se
mjera više promijenila i zašto? Ako je standardizirana vrijednost neke osobe
$z=1,5$, opišite njezin položaj prema sredini bez pretvaranja te vrijednosti
u postotak osoba. Zadatak je jednak u digitalnoj i tiskanoj inačici;
interakcija služi samo za dodatne pokuse.

Za drugu provjeru koristimo agregate simulirane ankete, bez dodatnog
zaokruživanja. U svakom su retku uz prosjek navedeni brojnik, nazivnik i
cjelobrojni zbroj.

*Slika. Kontrolni agregat simulirane ankete za ručnu i tiskanu provjeru. Izvor: data/anketa-mreze-agregat.csv, CC BY 4.0.*

Za šifru 1 provjerite `7339 / 90` i `90 / 300`. Zatim zbrojite četiri brojnika i
četiri zbroja minuta. Ako koristite datoteku `data/anketa-mreze.csv`, izdvojite šifru 1 i iz
tih redaka ponovno izračunajte prvi redak zbirne tablice; zadatak ne zahtijeva
pisanje koda. U tisku su svi potrebni brojnici, nazivnici i provjereni
odgovori već u tablici.

### Kritički

Urednik objavljuje naslov „Prosječan izvor ima 153 objave”. Na temelju
DigiKatova razrađenog primjera napišite tri rečenice. Prva objašnjava što
medijan mijenja u čitanju naslova, druga imenuje 551.712 kao nazivnik udjela
prvih deset domena, a treća je poštena rečenica s jedinicom, obuhvatom i
granicom generalizacije. Ne dodajte tvrdnju o hrvatskim medijima, dosegu ili
interakcijama.

### Revizija modela

Provjerite modelsku analizu iz okvira. Najprije potvrdite zbroj u tablici koju
je model proizveo. Zatim usporedite 3.571 redak s 438 jedinstvenih ključeva i
navedite koji dio ključa nedostaje. Napišite ukupan broj objava koji bi dao
ispravan spoj. Završite objašnjenjem zašto točan zbroj ne potvrđuje ispravno
spajanje.
