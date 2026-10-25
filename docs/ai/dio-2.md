# DIO II: OPISIVANJE PODATAKA

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

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
trebamo riješiti još jedno pitanje. Provjerit ćemo usporedivost zapisa te razlikovati odsutno mjerenje od izmjerene nule.

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
sadržaj. Nastao je zasebnom simulacijom, neovisno o ranije uvedenoj populaciji medijskih navika. Na njemu ćemo usporediti različite opise istih odgovora, a zaključci će se odnositi na te zamišljene osobe.

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
56.500 objava kroz cijeli obuhvaćeni raspon (Šikić, 2026). Prvi broj opisuje platformu i mjesec, a drugi jednu domenu kroz više godina. Oba broje objave; za broj jedinstvenih čitatelja trebali bismo podatke o publici.

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
objava, a interakcije pretvara u oznaku nedostajanja. Tako redak ostaje dostupan za analizu objava, a prosjek interakcija računamo samo iz dostupnih mjerenja.

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
sadržaj na ljestvici od 1 do 10. Skup je generiran zasebno, neovisno o ranije uvedenoj populaciji medijskih navika.

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
oblik omogućuje da vidimo zašto sredina i medijan daju različite opise. Tumačenje zato ostaje unutar zadanog nastavnog primjera.

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
Tri prikazana retka samo su početak toga zbrajanja. Svih 300 odgovora ovdje je dostupno.

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
najmanji zbroj apsolutnih odstupanja, bez njihova kvadriranja. Zato te dvije mjere mogu dati različite vrijednosti središta podataka.

**Medijan** je vrijednost koja poredani niz opažanja dijeli na dvije jednako
velike polovine.

U poredanih 300 odgovora središnja su mjesta 150 i 151. Na njima su
`r sort(s4_minute)[150]` i `r sort(s4_minute)[151]` minuta. Njihov prosjek daje
medijan. Poredak nam omogućuje pronalaženje središnjih mjesta među zapisima istih osoba.

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
Tu razliku u raspodjeli trebamo prikazati uz zajednički prosjek.

Raspon je razlika najveće i najmanje vrijednosti. Vrijeme u našem uzorku kreće
se od `r hr_broj(s4$najmanje, 0)` do `r hr_broj(s4$najvise, 0)` minuta, uz raspon od `r hr_broj(s4$raspon, 0)` minuta. Raspon ovisi samo o dvama krajnjim opažanjima. Za raspored ostalih vrijednosti trebamo dodatne mjere.

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
svaku osobu, zbrajamo svih 300 vrijednosti i dijelimo s 299. Pri kvadriranju zadržavamo punu preciznost odstupanja; prikaz na dvije decimale služi čitanju rezultata.

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
normalnom pravilu. Procjena približne normalnosti traži pregled cijele raspodjele, uz ovo pojedinačno podudaranje.

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
generiranja podataka. Opisuje oblik koji smo zadali simulacijom. Ako u izrazu
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
svih 300 odgovora bez izostavljanja. Svaki transformirani zapis i dalje pripada istom izvornom odgovoru iste osobe.

Nakon logaritmiranja asimetrija iznosi `r hr_broj(s4$asimetrija_log, 2)`, a sredina i medijan bliski
su, `r hr_broj(s4$sredina_log, 2)` i `r hr_broj(s4$medijan_log, 2)`. Sada, međutim, tumačimo drugu ljestvicu.
Eksponenciranjem razlike logaritama dobivamo omjer izvornih vrijednosti.
Rezultat stoga tumačimo kao višekratnik izvorne vrijednosti.

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
povjerenju, svako unutar njegove raspodjele. Vrijeme i povjerenje pritom zadržavaju svako svoje značenje. Standardizacija čuva oblik raspodjele i ograničenja ljestvice, pa uz krajnje vrijednosti i dalje gledamo graf.

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
Odluka i predloženi naslov zamišljeni su za ovaj primjer, a tablica domena preuzeta je iz stvarnog izvora.

Sredina tablice iznosi `r hr_broj(s4_izvori_sazetak$sredina, 1)` objave,
dok je medijan `r hr_broj(s4_izvori_sazetak$medijan, 0)`
(Šikić, 2026). Razlika proizlazi iz dvaju načina sažimanja iste tablice. Kada bi svaka
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
malom dijelu izvora. Za ta dva pitanja biramo različite, jasno imenovane sažetke.

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
za opis ovog korpusa. Doseg procjene određen je uključenim domenama i razdobljem korpusa.

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

---

# Vizualizacija kao argument

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Anscombe je sastavio četiri skupa s gotovo jednakim uobičajenim brojčanim
sažecima i jednakim prilagođenim pravcem, ali vrlo različitim grafovima
(Anscombe, 1973). U jednom se vidjela približno linearna veza, u drugom
zakrivljenost. Treći je imao utjecajnu točku, a četvrti okomit oblak uz
jedno izdvojeno opažanje.

Svi su sažeci bili ispravno izračunati. Četiri različita rasporeda opažanja ipak su opisali gotovo istim brojevima. Razliku među njima vidimo tek na grafovima.

Što graf otkriva o podacima, a što izborom prikaza možemo sakriti?

U poglavlju o sažimanju birali smo mjeru prema obliku raspodjele i pitanju
koje nas zanima. Pred grafom nas čeka slična odluka. Prikaz prosjeka može
olakšati usporedbu skupina, ali sakriti razlike među osobama; prikaz svih
opažanja čuva te razlike, no može otežati čitanje. Želimo naučiti odabrati
prikaz iz kojega se tražena usporedba doista može vidjeti.

Anscombeovim ćemo se skupovima iz vinjete vraćati kao provjeri onoga što
brojčani sažetak izostavlja (Anscombe, 1973). To su namjerno konstruirani
parovi brojčanih vrijednosti. Jedna točka predstavlja jedan takav konstruirani par. Služe nam za ispitivanje prikaza, a doseg zaključka ograničen je na taj nastavni primjer. Usporedbom tablica i
grafova provjerit ćemo što možemo previdjeti kada preuzmemo samo gotove
sažetke.

Poznatu simuliranu anketu `anketa_mreze` iskoristit ćemo za prikaz dnevnih
minuta na društvenim mrežama po dobnim skupinama. Uz nju ćemo
čitati i prikaze stvarnih zbirnih podataka projekta DigiKat, vodeći računa o
njihovu obuhvatu (Šikić, 2026). Primjeri se mijenjaju jer nas zanima ista
odluka u različitim situacijama. Prije čitanja oznake trebamo znati
predstavlja li ona osobu, skupinski sažetak ili zbroj objava.

Izbor prikaza obrazlažemo tako da čitatelj može provjeriti graf i bez
programa kojim je nacrtan. Ljestvica, oznake i opis trebaju pokazati obrazac
koji podaci podupiru te upozoriti na ono što je sažeto ili izostavljeno.

## Gramatika grafike

Grafom odlučujemo što ćemo uspoređivati položajem, duljinom, površinom ili
bojom. Izbor zato počinje pitanjem. Za raspodjelu jedne brojčane varijable
trebamo vidjeti oblik, za usporedbu kategorija zajedničku osnovicu, a za odnos
dviju brojčanih varijabli pojedinačna opažanja. Uredan graf neće pomoći ako
skriva ono što trebamo usporediti.

Nazivi poput stupčanog ili raspršenog dijagrama označuju uobičajene
kombinacije odluka. Svaki graf možemo rastaviti na te odluke i zasebno ih
provjeriti.

**Gramatika grafike** opisuje od čega je graf sastavljen. Određuje što
predstavlja oznaka, koja joj je varijabla pridružena, koji je račun prethodio
crtanju i kako se vrijednosti prenose u vizualne veličine.

Wilkinson je tu ideju razradio u sustav (Wilkinson, 2005), a ggplot2 jedna je
od njegovih poznatih programskih izvedbi (Wickham, 2016). Istim se načinom
razmišljanja možemo služiti pri čitanju tiskanog grafa, bez programiranja.

Najprije provjeravamo jedinicu. Točka može predstavljati ispitanika, državu,
godinu ili stranku. Ako umjesto pojedinaca prikažemo skupinske prosjeke, graf
odgovara na drugo pitanje. Zato promjenu jedinice treba jasno navesti.

**Geometrija** određuje oblik oznake, primjerice točku, stupac ili liniju.
Varijable zatim povezujemo s položajem na osima, bojom, veličinom ili oblikom
oznake.

**Pridruživanje** (*aesthetic mapping*) je odluka o tome koja se varijabla
prikazuje kojim vizualnim obilježjem. Time određujemo što će čitatelj moći
neposredno usporediti.

Ako skupine razlikujemo bojom u istom polju, lako ih uspoređujemo na
zajedničkim osima. Ako ih rasporedimo u zasebna polja, lakše pratimo obrazac
svake skupine. Različitim rasporedom istih podataka naglašavamo različite usporedbe.

Treba provjeriti i što je izračunato prije crtanja. Stupac koji prikazuje
prosjek skriva raspodjelu. Okvir s brkovima ne pokazuje broj njezinih vrhova,
a izglađena linija dodaje procijenjeni model. Graf zato može biti sažetak koji
gubi dio podataka, baš kao brojčana mjera. Anscombeovi skupovi pokazuju zašto
treba pogledati što je sažimanjem izostavljeno (Anscombe, 1973).

**Ljestvica** određuje kako se broj pretvara u vizualnu veličinu. Raspon osi,
prekid, logaritamska transformacija ili sredina ljestvice boja mijenjaju
prostor koji razlika zauzima. **Koordinatni sustav** određuje kako su položaji
raspoređeni. Polarne koordinate, primjerice, uvode kut i mogu otežati
usporedbu koju bismo na ravnoj osi lakše očitali.

Pri čitanju grafa zato tražimo jedinicu oznake, pridružene varijable,
prethodni račun i pravilo ljestvice. Ta pitanja možemo postaviti svakom grafu,
bez pristupa programu u kojem je izrađen.

Na sljedećem prikazu jedan stupac predstavlja dobnu skupinu iz simulirane
ankete `anketa_mreze`. Vodoravni položaj označuje skupinu,
a okomiti položaj vrha prosječne dnevne minute, izračunate prije crtanja.
Stupac zato sažima više osoba i ne pokazuje raspodjelu njihovih odgovora.
Lijevo os počinje od nule, a desno je skraćena. Uspoređujemo iste prosjeke,
ali promjena ljestvice mijenja dojam njihovih razlika.

*Slika. Isti prosjeci na dvjema osima. Lijevi prikaz počinje od nule, desni od 15 minuta, ispod najmanjeg prosjeka. Dvije kose crte označuju prekid desne osi. Vrijednosti su jednake u oba prikaza. Izrada autora.*

## Što oko može očitati

Grafička percepcija jest način na koji iz položaja, duljina i drugih oznaka očitavamo podatke. Neke vizualne usporedbe čitamo točnije od drugih. Cleveland i McGill pokusima
su potvrdili prednost položaja pred duljinom i kutom (Cleveland, 1984).
Povezali su te rezultate s ranijim istraživanjima i predložili širi poredak
kanala. Prema tom se poretku najtočnije očitava položaj na zajedničkoj osi, zatim na
istovjetnim, ali neporavnatim osima, pa duljina, kut, nagib i površina. Obujam,
zakrivljenost i zasićenost boje nalaze se pri dnu (Cleveland, 1984). Cijeli taj poredak predstavlja sintezu više izvora, s različitim stupnjem izravne pokusne provjere pojedinih usporedbi.

Za usporedbu koja određuje zaključak zato biramo kanal koji se lakše očitava.
Boja ili površina mogu poslužiti za razlike kod kojih je dovoljna gruba
procjena. Udjele ćemo točnije usporediti stupcima na zajedničkoj osi nego
kutovima kružnog dijagrama (Cleveland, 1984). Ako trebamo samo prepoznati
nekoliko izrazito različitih udjela, ta prednost može biti manje važna.

Trodimenzionalna perspektiva može otežati usporedbu ravnih podataka jer
duljinu kombinira s površinom i prividnim obujmom, slabijim kanalima u
predloženom poretku (Cleveland, 1984). Zato prije dodavanja treće dimenzije
provjeravamo donosi li novu informaciju ili samo mijenja dojam.

Tufte predlaže da za svaki grafički element pitamo koju informaciju prenosi
(Tufte, 2001). Sjene, obrubi i preljevi mogu odvlačiti pozornost bez korisnog
dodatka. Rešetka, razdjelna crta ili oznaka, s druge strane, mogu olakšati
čitanje. Uklanjanjem elementa možemo provjeriti otežava li njegov izostanak usporedbu
ili snalaženje na grafu.

Tufteov faktor laži uspoređuje relativnu promjenu prikazanu geometrijom s
relativnom promjenom u podacima (Tufte, 2001). Kada duljina ili površina izravno
predstavlja količinu, omjer blizu jedan pokazuje razmjerno kodiranje. Poštenost cijeloga grafa zahtijeva i provjeru ostalih odluka pri prikazu. Skraćena os, perspektiva ili zamjena
duljine površinom mogu povećati dojam i uz točne brojčane oznake. Doseg te mjere ograničen je na određene geometrijske usporedbe.

## Prikaz prema tvrdnji

Prednost zajedničke osi pomaže nam izabrati način usporedbe, ali još trebamo
odlučiti koje podatke graf mora sačuvati. Za oblik raspodjele trebamo drukčiji
prikaz nego za usporedbu skupinskih prosjeka. Sljedeća tablica povezuje ta
pitanja s brojem i vrstom varijabli te pokazuje što pojedini izbor izostavlja.

| Što se prikazuje | Uobičajeni izbor | Što prikaz čuva, a što odbacuje |
|---|---|---|
| jedna brojčana varijabla | histogram, krivulja gustoće | čuva oblik cijele raspodjele, gubi pojedinačno opažanje |
| jedna kategorijalna varijabla | stupci na zajedničkoj osi | čuva učestalosti kategorija, izostavlja pojedinačne zapise i njihova druga obilježja |
| brojčana po skupinama | okvir s brkovima | čuva medijan, kvartile i izdvojena opažanja, odbacuje broj vrhova i položaj većine opažanja |
| dvije brojčane varijable | raspršeni dijagram | čuva svako opažanje, teško podnosi velik broj točaka |
| dvije kategorijalne varijable | grupirani ili složeni stupci | čuva odnos udjela, otežava usporedbu unutar složenih stupaca |

: Prikaz prema vrsti podataka i prema onome što svaki izbor žrtvuje. Izrada autora.

Svaki prikaz zadržava dio informacija i izostavlja ostale. Okvir s brkovima
sažima medijan i kvartile, pa može izgledati jednako za raspodjelu s jednim
ili dvama vrhovima. Histogram raspoređuje opažanja u razrede i prikazuje
njihove učestalosti, zbog čega lakše otkriva oblik. Više skupina, međutim,
može biti teže usporediti histogramima.

Za dvije kategorijalne varijable možemo izabrati stupce jedan uz drugi,
složene stupce ili stupce jednake ukupne visine koji prikazuju udjele.
Usporedni stupci pokazuju apsolutne brojeve. Stupci udjela pokazuju sastav,
ali skrivaju razliku između skupine od dvadeset i skupine od dvjesto osoba.
Za usporedbu brojnosti uz udjele trebamo navesti i veličine skupina.

Kod složenih stupaca samo najdonji segment ima zajedničku osnovicu. Ostali
počinju na različitim visinama, ovisno o prethodnim segmentima. Njihove su
duljine točne, ali ih je teže usporediti bez zajedničkog početka
(Cleveland, 1984). Ako zaključak ovisi o jednom takvom segmentu, korisno ga je
prikazati zasebno.

I riječi možemo uspoređivati kao kategorije, ali tek nakon što odredimo što
ćemo smatrati istom riječju. U šest odabranih naslova o vizualizaciji ukupno je
36 riječi i 28 različitih oblika [Anscombe, 1973; Cleveland, 1984; Tufte, 2001;
Wilkinson, 2005; Wickham, 2016; Matejka, 2017]. Do tih brojeva dolazimo tako da
sva slova pretvorimo u mala i uklonimo interpunkciju. Riječi ne svodimo na
zajednički korijen, pa su `graphs`, `graphical` i `graphics`
različite jedinice. Stupci će zato uspoređivati učestalost točnih oblika koje
smo tako odredili.

Primjer pretvorbe daje naslov *The Grammar of Graphics* (Wilkinson, 2005).
Nakon pretvorbe u mala slova i razdvajanja dobivamo četiri zapisa,
`the`, `grammar`, `of` i `graphics`. Svaki dodaje jedan svome brojaču.
Kad tako obradimo svih šest odabranih naslova, jedinica brojanja postaje pojedino pojavljivanje riječi. U Wickhamovu naslovu o paketu ggplot2 uklanjamo dvotočku,
ali zadržavamo `ggplot2` kao jedan oblik (Wickham, 2016).

Graf izdvaja šest oblika koji se ponavljaju. U zadnjem retku navedena je učestalost koja vrijedi za svaki od preostala dvadeset dva oblika zasebno.

*Slika. Učestalost točnih oblika u šest namjerno odabranih bibliografskih naslova. Izrada autora prema objavljenim naslovima [@anscombe1973; @cleveland1984; @tufte2001; @wilkinson2005; @wickham2016; @matejka2017].*

Rezultat opisuje odabranih šest naslova. Za širi zaključak o literaturi o vizualizaciji ili znanstvenom pisanju trebali bismo odgovarajući izbor tekstova. Pri tumačenju zato navodimo jedinicu,
obradu teksta, nazivnik i obuhvat. Iste ćemo odluke ponovno razmotriti kada
tekst postane ulaz algoritma.

## Dvije varijable u istom prostoru

Stupcima smo uspoređivali količine po kategorijama. Kada želimo sačuvati
odnos dviju brojčanih varijabli za svaku jedinicu, trebamo drugi raspored
oznaka. Raspršeni dijagram može prikazati svako
opažanje kao točku. Iz rasporeda čitamo smjer i zakrivljenost veze, podskupine
i izdvojena opažanja. Zato njime počinjemo provjeru odnosa.

Ako se mnoge točke preklapaju, ne vidimo koliko opažanja stoji na istom
mjestu. Djelomično prozirne točke mogu pokazati gušća područja tamnijima. Kod
diskretnih vrijednosti pomaže blago razmicanje točaka, a za vrlo mnogo
opažanja možemo izravno prikazati procijenjenu gustoću.

Izglađenu liniju na raspršenom dijagramu dobivamo procjenom modela odnosa iz opaženih podataka. Njezin oblik ovisi o postupku procjene i može djelovati
uvjerljivo čak i kad podaci ne podupiru stabilan obrazac. Uvijek je zato
čitamo uz oblak točaka. U poglavlju o regresiji razradit ćemo kako se takve
linije dobivaju i provjeravaju.

## Poštena ljestvica

Vraćamo se simuliranoj anketi `anketa_mreze` iz poglavlja o sažimanju.
Prikazujemo prosječne dnevne minute na društvenim mrežama po dobnim skupinama. Raspon osi može znatno promijeniti dojam. Prosjeci se ovdje
razlikuju za `r hr_broj(s5_raspon_prosjeka, 1)` minuta, odnosno `r paste0(hr_broj(100 * s5_udio_raspona, 1), " %")` najvećeg prosjeka. Ta je
razlika stalna, ali njezina veličina na stranici ovisi o osi.

*Slika. Broj ispitanika, prosjek i medijan dnevnih minuta u četirima dobnim skupinama simuliranoga nastavnog skupa `anketa_mreze`. Izrada autora.*

Tablica skupinskih sažetaka čuva vrijednosti za račun, a
usporedba dviju osi pokazuje koliko dojam o istoj razlici
ovisi o početku osi.

Oba prikaza koriste iste četiri vrijednosti. Desni im dodjeljuje uži raspon
osi. Kod stupaca duljina predstavlja vrijednost, pa odsijecanje nule narušava
tu razmjernost. U linijskom ili raspršenom grafu uspoređujemo položaje, zbog
čega os može pratiti raspon podataka ako je jasno označena.

Stupce zato crtamo od nule. Oznaka skraćene osi otkriva zahvat, ali ne vraća
ispravan odnos duljina. Za linije i točke uži raspon može pomoći čitanju, uz
jasno vidljiv početak i ljestvicu osi.

Za sljedeći prikaz vraćamo se DigiKatovoj tablici internetskih domena. Svaki
redak sadrži ukupan broj objava jedne domene u odabranom korpusu. Tablica ima
`r hr_broj(s5_izvori_sazetak$izvora, 0)` domene i `r hr_broj(s5_izvori_sazetak$objava, 0)` objava (Šikić, 2026). Medijan je `r hr_broj(s5_izvori_sazetak$medijan, 0)` objave po domeni, a najveći broj `r hr_broj(s5_izvori_sazetak$najvise, 0)`. Na linearnoj bi osi većina domena bila
stisnuta uz početak. Logaritamska os omogućuje da se bolje
vide i manje vrijednosti jer jednak prostor dodjeljuje jednakim omjerima.

*Slika. Raspodjela broja objava među 3 604 imenovane domene na logaritamskoj osi. Izrada autora prema DigiKatu [@digikat2026].*

Na logaritamskoj osi pomak od 10 do 100 jednak je pomaku od 100 do 1.000.
Uspoređujemo omjere, dok apsolutne razlike nisu jednako velike. Promjena osi
ne mijenja zapise, ali mijenja vizualni oblik raspodjele, pa je treba
označiti. I dalje opisujemo samo domene u ovom korpusu, bez zaključivanja o
svim hrvatskim medijima, korisnicima ili pojedinačnim objavama.

## Mala višestruka polja

Kada je na grafu mnogo skupina, linije se mogu preklapati i tražiti stalno
provjeravanje legende. Tada isti oblik grafa možemo ponoviti u zasebnom polju
za svaku skupinu.

**Mala višestruka polja** (*small multiples*) niz su prikaza istoga oblika i
iste ljestvice, po jedan za svaku skupinu, tako da se razlike među skupinama
očitavaju usporedbom položaja između polja.

Za usporedbu razina polja trebaju zajedničku ljestvicu. Ako svako ima svoj
raspon, male i velike razlike mogu izgledati jednako. Različite osi mogu biti
prikladne za usporedbu oblika, ali tu odluku treba jasno navesti.

U DigiKatovu mjesečnom izvatku za 2024. nedostaju retci od veljače do svibnja.
Siječanj je djelomičan, a lipanj donosi promjenu metode i obuhvata
(Šikić, 2026). Prazninu ne pretvaramo u nule niti linijom spajamo siječanj i
lipanj. U tablici zadržavamo svih 12 mjeseci kako bi nedostajanje bilo
vidljivo.

*Slika. Broj objava i udio weba u mjesečnom zbroju platformskoga izvatka za 2024. Duga crta označuje mjesec bez retka, ne nulu. Izrada autora prema DigiKatu [@digikat2026].*

Brojem objava opisujemo mjesečnu količinu, a udjelom weba njezin sastav.
Nazivnik u mjesečnoj tablici zbroj je svih platformi
tog mjeseca. Ne koristimo 551.712 iz datoteke domena jer ona ima drugu
jedinicu i nema zajednički ključ. U [malim višestrukim
poljima](#fig-mala-polja) prikazujemo broj objava za četiri platforme s
najviše objava u dostupnim mjesecima 2024. i za objedinjeni ostatak. Sva polja
imaju istu logaritamsku os.

*Slika. Mjesečni broj objava za četiri platforme s najvećim zbrojem u dostupnim mjesecima 2024. i objedinjene ostale platforme. Praznina od veljače do svibnja znači da nema redaka; isprekidana crta i odvojene točke u lipnju označuju lom metode. Zajednička okomita os je logaritamska. Izrada autora prema DigiKatu [@digikat2026].*

Linije ostavljaju četveromjesečnu prazninu, a lipanjska točka odvojena je od
kasnijeg niza. Zbog nepotpunog siječnja i promjene metode ne zaključujemo o
trendu, rastu ili učinku promjene nakon lipnja. Možemo usporediti dostupne
brojeve uz vidljiva ograničenja zapisa.

## Graf pred čitateljem

Zajednička ljestvica omogućuje usporedbu samo ako čitatelj može razaznati
oznake i njihov smisao. Pri izradi grafa zato treba predvidjeti crno-bijeli tisak, čitače zaslona i
različite sposobnosti razlikovanja boja.

Razliku među skupinama zato uz boju označujemo oblikom točke, vrstom linije
ili izravnim nazivom. Tako značenje ostaje čitljivo i bez boje. Paleta knjige
koristi i razlike u svjetlini kako bi se kategorije mogle razlikovati u sivim
tonovima.

Alternativni tekst treba prenijeti nalaz osobi koja ne vidi graf. Navodimo
varijable, smjer veze i najizraženije obilježje obrasca. Opis konkretizira odnos, primjerice njegov smjer i oblik, kako bi čitatelj mogao razumjeti nalaz.

Pristupačnost prikaza znači da podatke može pročitati i osoba kojoj boja ili sitan tekst nisu dostupni. Izravnim oznakama uz podatke smanjujemo potrebu za traženjem naziva u legendi.
Pomaže i smislen redoslijed kategorija. Kada želimo usporediti veličine,
poredak po vrijednosti olakšava čitanje više od abecednog.

Iste odluke provjeravamo i pri čitanju grafa. Primijenimo ih na desno polje u slika

Jedan stupac predstavlja dobnu skupinu i služi zaključivanju na toj razini. Za opis pojedinog ispitanika trebali bismo njegove odgovore. Skupina određuje vodoravni položaj, a
prosjek duljinu stupca. Boja i širina su jednake jer ne prikazuju dodatnu
varijablu.

Prije crtanja izračunat je prosjek svake skupine, čime je skriven oblik
raspodjele i njezin dugi desni rep. Stupac od `r hr_broj(s5_najmladi$prosjek, 1)` minuta prikazuje
prosjek, dok medijan iste skupine iznosi `r hr_broj(s5_najmladi$medijan, 1)` minuta. Os uz to ne počinje
od nule, što je u nastavnom primjeru označeno.

 Prosjek skriva raspodjelu, a skraćena os
prikazuje neprimjerene odnose duljina. Brojevi su točni, ali graf može navesti
na pretjeran dojam razlike i pogrešno shvaćanje tipičnog ispitanika. Oznaka
zahvata omogućuje da problem uočimo, ali ga ne uklanja.

Histogram grupira brojčane vrijednosti u razrede. Visina stupca ovdje
broji opažanja u razredu jednake širine, a drukčija širina razreda može
promijeniti dojam o obliku. Krivulja gustoće zaglađuje raspodjelu, pa njezina
visina nije broj osoba. Kutijasti prikaz čuva medijan i srednjih 50 %
opažanja između prvoga i trećega kvartila. U sljedećem prikazu brkovi sežu
do najudaljenijih opažanja unutar 1,5 interkvartilnog raspona od kutije;
udaljenija opažanja prikazuju se zasebno. Takva točka nije automatski pogreška.

Sažimanje u dvije sredine skriva razlike među pojedincima. Zasebno pitanje jest nesigurnost procjene populacijske sredine. Nju procjenjujemo prema načinu odabira opažanja, što ćemo razraditi uz uzorkovanje i procjenu.

## Interakcija — Isti podaci, četiri grafa

Za ovu ilustraciju stvaramo zaseban skup od 72 opažanja, po 36 u dvjema
skupinama. U svakoj ravnomjerno rasporedimo vrijednosti $x$ od 1 do 10.
Polazište ishoda je $1,5 + 0,55x$, skupini B dodajemo 0,8, a svakoj točki
neovisno normalno odstupanje sa sredinom nula i standardnom devijacijom
0,85. Na primjer, pri $x=1$ polazište je 2,05 za A i 2,85 za B, prije
slučajnog odstupanja. Varijable nemaju stvarnu mjernu jedinicu. Četiri grafa prikazuju isti skup od 72 zapisa.

Isti simulirani podaci prikazani su na četiri načina. Svaki graf
olakšava jednu usporedbu i skriva dio drugih informacija. Raspršeni
dijagram čuva odnos dviju varijabli, dok prikaz sredina sažima razliku
među skupinama. Izbor ovisi o pitanju na koje želimo odgovoriti.

*Slika. Isti simulirani podaci prikazani odabranom geometrijom. Izbor prikaza mijenja vidljivu usporedbu, ne opažanja.*

**Što isprobati.**

1. Odaberite raspršeni dijagram i opišite odnos varijabli bez sažimanja po skupinama.
2. Prijeđite na histogram i utvrdite koja je prethodna informacija nestala.
3. Usporedite raspodjelu po skupinama s prikazom njihovih sredina.
4. Odaberite graf za tvrdnju o razlikama među tipičnim ishodima i obrazložite izbor.

**Statistika u divljini.**
**Kružni dijagram pred konkretnim zadatkom.** Pretpostavimo da kulturna
ustanova priprema prikaz posjećenosti svojih programa. Treba pokazati
koji programi okupljaju sličan udio publike, a koji se jasno izdvajaju.
Netko predlaže kružni dijagram jer svaki program zauzima dio ukupne
posjećenosti. Drugi ga odbacuje pozivajući se na pravilo da se takvi
grafovi nikada ne koriste. Prije izbora valja razjasniti što čitatelj
treba moći usporediti.

Cleveland i McGill istraživali su upravo točnost očitavanja grafičkih
prikaza. U njihovim su pokusima sudionici procjenjivali omjer dviju
istaknutih vrijednosti. Položaj na zajedničkoj osi omogućavao je
preciznije usporedbe od kuta (Cleveland, 1984). Nalaz daje razlog za
izbor prikaza, ali taj je razlog vezan uz određeni zadatak.

U našem zamišljenom izvještaju osobito nas zanimaju programi s bliskim
udjelima. Na kružnici bismo uspoređivali slične kutove u različitim
položajima. Na poredanim stupcima s istom početnom osi možemo usporediti
njihove završetke, a uz oznake pročitati i točne udjele. Takav izbor
olakšava upravo usporedbu zbog koje pripremamo izvještaj. Iz samoga
grafa ipak ne saznajemo zašto neki program privlači više ljudi ni
zaslužuje li zato više sredstava.

Kad bi nam namjera bila samo pokazati da jedan program zauzima približno
polovinu cjeline, zahtjev za preciznošću bio bi drukčiji. Clevelandov
i McGillov pokus ne predstavlja ispitivanje svake moguće uporabe,
pamćenja ili razumijevanja grafa u stvarnom izvještaju
(Cleveland, 1984). Zato iz njega ne izvodimo zabranu koja bi zamijenila
prosudbu o publici i svrsi prikaza.

Ustanova može izabrati stupce i objasniti zašto ih bira. Pritom treba
imenovati broji li posjete ili različite posjetitelje, jer dobar oblik
grafa ne popravlja nejasnu jedinicu. Prikladnost grafa procjenjujemo prema tome koliko jasno prikazuje usporedbu važnu za naše pitanje.

**Nađite grešku.**
Za izvještaj treba usporediti udjele triju kategorija. U ovoj
konstruiranoj vježbi kategorijama A, B i C pripada 30 %, 40 % i 30 % iste
cjeline. Asistent je iz tih podataka nacrtao sljedeći prijedlog. Pregledajte
odnos između oznaka, visina i izgleda stupaca.

*Slika. Prijedlog prikaza triju udjela za urednički pregled. Konstruirana nastavna vježba, izrada autora.*

Odluka o širini vidi se i u dijelu poziva kojim je prijedlog izrađen.

> Os počinje od nule, sve kategorije imaju oznaku i vrijednosti su
> prikazane. Šira treća kategorija samo popravlja optičku ravnotežu i
> ne mijenja dojam o odnosu udjela.

Usporedite posebno A i C. Pripremite uputu osobi koja uređuje graf,
s jednom potrebnom izmjenom i dvjema odlukama koje treba zadržati.
Objasnite na kojem dijelu prikaza temeljite izmjenu. Ne trebate pisati kod.

## Razrađeni primjer

Za odgovor na pitanje iz vinjete trebamo usporedbu koja čuva pojedinačna
opažanja. Anscombeov kvartet već smo upoznali kao četiri konstruirana skupa s
gotovo jednakim sažecima (Anscombe, 1973). Sada ćemo njihove točke rasporediti u
mala višestruka polja i provjeriti što zajedničke osi otkrivaju. R-ovi ugrađeni
podaci `anscombe` reproduciraju taj objavljeni primjer.

U svakom od četiriju skupova ima 11 parova. Prva tri para iz prvih dvaju
skupova pokazuju da ista vrijednost $x$ može biti povezana s drukčijim $y$.

*Slika. Prva tri para u dvama Anscombeovim skupovima iz ugrađenoga skupa u R-u prema @anscombe1973.*

U prvom retku oba skupa imaju $x=10$, ali ishode 8,04 i 9,14.
Za sredinu prvoga skupa zbrajamo svih 11 ishoda, dobivamo
`r hr_broj(sum(anscombe$y1), 2)` i dijelimo s 11. Isti račun ponavljamo za
ostala tri skupa, a grafovima zadržavamo svaki izvorni par.

Kod u ovom primjeru koristi pakete ggplot2, dplyr i tibble, učitane u pripremi knjige. Njihova je priprema opisana u mrežnom R praktikumu. Najprije provjeravamo sažetke. Zaokružene na dvije decimale, sve četiri
sredine ishoda iznose `r hr_broj(s5_ans$sredina_y[[1]], 2)`, a standardne devijacije `r hr_broj(s5_ans$sd_y[[1]], 2)`. Iz tih se
vrijednosti razlike u obliku ne mogu prepoznati.

U prvom dijelu postupka svaki par vrijednosti dobiva vlastiti redak, kako bi u
drugome mogao postati jedna točka. Poziv `aes` određuje koja
vrijednost ide na koju os, a `geom_point` crta te točke. Da bismo usporedili
oblik podataka s njihovim linearnim sažetkom, `geom_smooth` dodaje
procijenjeni odnos, dok `facet_wrap` odvaja skupove u zasebna polja. Upisom
`p_anscombe` prikazujemo pohranjeni graf. Dodani pravci gotovo se podudaraju, kao u izvornom primjeru (Anscombe, 1973). U kasnijim je primjerima dovoljno
prepoznati koju od tih odluka pojedini naziv provodi.

Uz gotovo jednake sažetke četiriju skupova (Anscombe, 1973), graf koristi
jednake osi i gotovo podudarne pravce. Tako razlike među poljima proizlaze iz rasporeda
opažanja.

Anscombeov kvartet s gotovo jednakim sažecima i različitim oblicima. Izrada autora
prema anscombe1973.

Prvi skup približno prati pravac, a drugi zakrivljenu vezu. U trećem i
četvrtom izdvojeno opažanje snažno utječe na pravac. Brojčani sažetak zato čitamo
zajedno s oblikom podataka koje sažima.

## Sažetak

Graf počinje od usporedbe koju želimo omogućiti, pa jedinicu oznake, varijable,
prethodni račun i ljestvicu biramo zajedno. Tim izborom dio podataka
pokazujemo, a dio sažimamo ili izostavljamo, kao što su gotovo jednaki
Anscombeovi sažeci skrivali različite oblike. Položaj i drugi vizualni kanali
ne omogućuju jednako precizno očitanje (Cleveland, 1984), pa zajedničke osi,
prikladno razdvajanje skupina i oznake uz boju pomažu da tražena usporedba
ostane čitljiva. Kada prikazujemo riječi, isto obrazloženje obuhvaća pravilo
brojanja i izbor tekstova. U poglavlju o povezanosti krenut ćemo od raspršenog
dijagrama i provjeriti koliko njegova oblika možemo sažeti jednim
koeficijentom.

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

Odaberite prikaz za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Za svaki obrazložite izbor i navedite što
izostavlja. Za jedan graf napišite alternativni tekst koji prenosi nalaz te
provjerite je li nalaz razumljiv i bez boje.

### Računski

Iz tablice skupinskih sažetaka uzmite najveći i najmanji
prosjek dnevnih minuta. Izračunajte njihovu razliku, a zatim je podijelite s
većim prosjekom i pretvorite u postotak. Usporedite dobiveni postotak s [dvama
prikazima osi](#fig-skraceni-raspon) i objasnite zašto se brojčana razlika nije
promijenila, premda se promijenio vizualni dojam. Predajte račun, postotak i
dvije rečenice prosudbe. Svi potrebni podaci nalaze se u tablici.

### Kritički

Pronađite objavljeni graf sa skraćenom osi i prosudite je li odsjecanje
opravdano. Odredite koliki bi udio visine osi zauzela razlika kada bi donja granica bila nula, a gornja ostala ista, je li
prekid vidljivo označen i mijenja li se zaključak teksta uz graf. Predajte
odlomak s presudom i s uvjetom pod kojim bi presuda bila suprotna.

### Revizija modela

Provjerite prijedlog grafa iz okvira o pogrešci. Navedite ispravne grafičke odluke i
izdvojite onu koja obmanjuje. Opišite što treba promijeniti da udio ponovno
bude prikazan samo duljinom stupca. Opis predajte bez pisanja ili popravljanja
koda.

---

# Povezanost

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-25 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Anscombeove smo skupove već usporedili grafički. Njihova gotovo jednaka
Pearsonova korelacija sada postavlja preciznije pitanje. Koliko o odnosu
znamo ako vidimo samo koeficijent (Anscombe, 1973)?

Korelacija je u svakom skupu točno izračunata. Razlike su ostale skrivene jer
je sažela samo jedan aspekt odnosa.

Što bismo propustili kada bismo povezanost opisali samo tim brojem?

Sada kada znamo pročitati raspršeni dijagram, možemo preciznije pitati kako se
dvije varijable mijenjaju zajedno. U dosadašnjim smo sažecima dnevne minute i
dob često promatrali odvojeno. Zanima nas i njihov odnos. Želimo ga opisati
usporedivim brojem, a pritom sačuvati ono što smo iz grafova naučili o
zakrivljenosti, podskupinama i izdvojenim opažanjima.

Glavni primjer ostaje simulirana anketa `anketa_mreze` iz prethodnih poglavlja. Jedan redak predstavlja jednu zamišljenu osobu, pa njezinu dob
povezujemo s njezinim dnevnim vremenom na društvenim mrežama. Za pregled više
parova uključit ćemo i povjerenje u sadržaj. Podaci su konstruirani za
nastavu. Na njima učimo opisivati odnos, bez zaključka o stvarnim navikama ili
o tome što bi promjena vremena na mrežama izazvala.

Mjeru zajedničkog kretanja gradimo od odstupanja od sredine i
standardizacije, koje već poznajemo. Pearsonova korelacija sažima linearnu
vezu, a Spearmanov koeficijent polazi od poretka vrijednosti. Izdvojena
točka, uži raspon dobi ili spajanje podskupina mogu promijeniti koeficijent
i njegov smisao. Usporedbom tih slučajeva vraćamo se problemu zbirne slike
iz Berkeleyjskog slučaja, sada s dvjema brojčanim varijablama.

Provjeru ćemo proširiti na stvarne Eurostatove pokazatelje obrazovanja i
uporabe interneta, gdje jedinica postaje država umjesto osobe
({Eurostat}, 2026; {Eurostat}, 2026). Ta promjena određuje što
povezanost smije značiti. Uočen odnos među državama nećemo pripisati njihovim
pojedinim stanovnicima. Prikladnost koeficijenta provjeravamo uz graf i opis odabranih jedinica.
Tako vidimo koliko dobro sažima odnos i što izostavlja. Za pitanje o uzroku
trebamo odgovarajući nacrt i dodatne podatke, a počinjemo pregledom oblika
odnosa koji već vidimo.

## Zajedničko kretanje

Dvije su varijable povezane kada se vrijednosti jedne razlikuju ovisno o
vrijednostima druge. Pri pozitivnoj vezi veće vrijednosti jedne češće dolaze
uz veće vrijednosti druge. Pri negativnoj dolaze uz manje vrijednosti druge.
Koeficijent blizu nule može značiti slabu linearnu vezu, ali pritom može
postojati zakrivljen odnos.

Na grafu dobi i dnevnih minuta iz ankete `anketa_mreze` svaka točka povezuje
vrijednosti iste zamišljene osobe. Točke tvore silazni oblak.
Pad je strmiji među mlađima i poslije se izravnava. Graf nam pokazuje taj
oblik prije računanja koeficijenta.

*Slika. Dob i dnevno vrijeme korištenja u simuliranoj anketi. Oblak pokazuje silazan, zakrivljen obrazac. Pearsonov koeficijent sažima samo njegov linearni dio. Izrada autora; podaci i postupak opisani su u tekstu.*

Najprije uspoređujemo na koju stranu od prosjeka odstupa svaki ispitanik u
objema varijablama. U generiranom nastavnom skupu `anketa_mreze` s `r s6_n`
ispitanika, `r paste0(hr_broj(100 * s6_udio_slaganje, 0), " %")` odstupa na istu stranu u dobi i dnevnim minutama. Uz
simetrične raspodjele i neovisna odstupanja očekivali bismo udio blizu
polovine. Asimetrija ga može promijeniti i bez povezanosti, pa sam udio nije
mjera veze. U ovom primjeru češća su odstupanja na suprotne strane, što
odgovara negativnom obrascu na grafu. Za jačinu veze trebamo uz smjer uzeti u
obzir i veličinu odstupanja.

Zato za svaku osobu množimo odstupanja od dviju sredina. Umnožak je pozitivan
ako oba odstupanja imaju isti predznak, a negativan ako imaju suprotne. Velika
odstupanja pridonose više od malih. Zbrajanjem tih umnožaka i dijeljenjem
dobivamo mjeru zajedničkog kretanja.

**Kovarijanca** uzorka je zbroj umnožaka odstupanja dviju varijabli od
njihovih sredina, podijeljen brojem opažanja umanjenim za jedan. Pozitivan
predznak upućuje na prevladavanje odstupanja u istom smjeru, a negativan u
suprotnom.

Zapisano simbolima, gdje $x_i$ i $y_i$ označavaju vrijednosti izmjerene kod
istog opažanja, $\bar{x}$ i $\bar{y}$ njihove sredine, a $n$ broj opažanja,
kovarijanca glasi

$$\operatorname{Cov}(x, y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}).$$

Djelitelj $n-1$ isti je onaj iz poglavlja o sažimanju podataka, a formula je
poopćenje varijance, jer varijanca nastaje kada se ista varijabla stavi na oba
mjesta.

Za provjeru računa potrebne su obje sredine i standardne devijacije. U
anketi je sredina dobi `r hr_broj(mean(s6_dob), 3)`, a njezina standardna
devijacija `r hr_broj(sd(s6_dob), 3)` godina. Za dnevne minute odgovarajuće
vrijednosti iznose `r hr_broj(mean(s6_minute), 3)` i
`r hr_broj(sd(s6_minute), 3)`. Račun u nastavku koristi nezaokružene
vrijednosti; prikaz na tri decimale služi ručnoj približnoj provjeri.

Na prvoj osobi iz poznate ankete možemo pregledati jedan član zbroja.
Dob je `r s6_dob[1]`, a vrijeme `r s6_minute[1]` minuta. Odstupanja od
dviju sredina iznose `r hr_broj(s6_dob[1] - mean(s6_dob), 2)` godina i
`r hr_broj(s6_minute[1] - mean(s6_minute), 2)` minuta. Njihov je umnožak
`r hr_broj((s6_dob[1] - mean(s6_dob)) * (s6_minute[1] - mean(s6_minute)), 2)`.
Račun ponavljamo na svih 300 parova, zbrajamo umnoške i dijelimo s 299.
Svi su parovi potpuni, a dob jedne osobe uvijek ostaje uz njezine minute.

Veličina kovarijance ovisi o mjernim jedinicama. Za dob i dnevne minute ovdje
iznosi `r hr_broj(s6_kov, 1)`. Ako iste minute pretvorimo u sate, dobivamo `r hr_broj(s6_kov_sati, 1)`,
šezdeset puta drukčiju vrijednost. Odnos je ostao isti. Kovarijancu zato
moramo čitati uz jedinice i ne možemo njome izravno uspoređivati parove
mjerene različitim jedinicama.

Za usporedbu različitih parova potrebna nam je mjera neovisna o jedinicama.

## Od standardizacije do matrice

Standardizacijom vrijednosti pretvaramo u broj standardnih devijacija od
sredine. Ako to učinimo s objema varijablama prije množenja, račun daje jednak rezultat za vrijeme izraženo u minutama i u satima.

**Pearsonova korelacija** uzorka jest zbroj umnožaka uzorački standardiziranih
vrijednosti dviju varijabli, podijeljen s $n-1$. Mjeri smjer i jačinu njihove
linearne veze na ljestvici od
$-1$ do $+1$, neovisno o mjernim jedinicama.

Uzoračku korelaciju označujemo s $r$, a populacijsku s $\rho$. Standardizirane
vrijednosti opažanja $i$ jesu $z_{x_i}$ i $z_{y_i}$, dok su $s_x$ i $s_y$
uzoračke standardne devijacije. Korelaciju možemo zapisati na dva jednaka
načina

$$r = \frac{1}{n-1} \sum_{i=1}^{n} z_{x_i} \, z_{y_i} = \frac{\operatorname{Cov}(x, y)}{s_x \, s_y},$$

Dva zapisa daju isti broj. U prvome standardiziramo prije množenja, a u
drugome kovarijancu dijelimo standardnim devijacijama. Računamo isto, samo
drugim redoslijedom.

Nakon standardizacije prva osoba ima $z_x = `r hr_broj(s6_z_dob[1], 2)`$
i $z_y = `r hr_broj(s6_z_min[1], 2)`$, pa u zbroj ulazi njihov umnožak
`r hr_broj(s6_z_dob[1] * s6_z_min[1], 3)`. Svih 300 takvih umnožaka opet
dijelimo s 299, jer smo standardizirali uzoračkim standardnim devijacijama.

U anketi račun preko standardiziranih vrijednosti daje `r hr_broj(s6_r_iz_z, 3)`, a ugrađeni
izračun korelacije `r hr_broj(s6_r, 3)`. Ako umjesto minuta koristimo sate, rezultat
ostaje `r hr_broj(s6_r_sati, 3)`. Kovarijanca se pri toj promjeni jedinice promijenila
šezdeset puta, a korelacija ostaje ista.

Kada je korelacija $+1$, sve točke leže na uzlaznom pravcu, a pri $-1$ na
silaznom. Vrijednost nula znači da nema linearne veze. Međuvrijednosti opisuju
koliko raspored točaka prati pravac. Nagib pravca odgovara na zasebno pitanje, za koliko se minuta vrijeme korištenja mijenja uz jednu godinu dobi. Uz korelaciju `r hr_broj(s6_r, 2)` za taj ćemo opis trebati i regresiju.

Cohen je kao orijentaciju u društvenim znanostima predložio korelacije oko
0,10, 0,30 i 0,50 za male, srednje i velike odnose (Cohen, 1988). Služe kao početna orijentacija koju prilagođavamo području i istraživačkom pitanju.

Cohen ih preporučuje kada nemamo bolju osnovu u poznavanju područja
(Cohen, 1988). Važnost koeficijenta zato procjenjujemo prema pojavi, načinu
mjerenja, posljedicama i nalazima usporedivih istraživanja.

U jednostavnom linearnom opisu kvadrat korelacije pokazuje udio varijance
povezan s tim opisom. Za korelaciju `r hr_broj(s6_r, 2)` to je `r paste0(hr_broj(100 * s6_r^2, 0), " %")` varijance.
Preostalih `r paste0(hr_broj(100 * (1 - s6_r^2), 0), " %")` linearni opis ne obuhvaća. Primjerice, korelacija 0,30
daje devet posto. U poglavlju o regresiji tu ćemo veličinu koristiti za opis
prilagodbe modela.

Uz veličinu veze treba procijeniti nesigurnost. Korelacija iz uzorka može
odstupati od populacijske, a uz isti nacrt i usporedive neovisne jedinice veći
uzorak obično daje precizniju procjenu. Vrijednost 0,40 na trideset i na tri
tisuće osoba zato nema jednaku nesigurnost. Uz koeficijent uvijek navodimo
broj opažanja, a račun nesigurnosti slijedi u poglavljima o uzorkovanju i
procjeni.

U poznatoj anketi uz dob i dnevne minute imamo i povjerenje, pa možemo
promatrati više odnosa. Umjesto da koeficijente zapisujemo odvojeno, slažemo ih
u matricu u kojoj svaki redak i stupac pripada jednoj varijabli. Isti se par
pojavljuje s obje strane dijagonale, pa je matrica simetrična. Na dijagonali su
jedinice jer je svaka varijabla savršeno povezana sama sa sobom.

*Slika. Korelacije triju brojčanih varijabli simulirane ankete. Izrada autora.*

## Matrica, kodovi i rangovi

Matrica olakšava pregled, ali i traženje slučajno velikih koeficijenata. Tri
varijable daju tri para, a deset ih daje četrdeset pet. Hipoteza nastala traženjem najvećeg broja ima istraživački status, različit od hipoteze postavljene prije pregleda rezultata. Posljedice za testiranje razmotrit ćemo u poglavlju o krizi i
obnovi. Svaki par koji namjeravamo tumačiti najprije prikazujemo raspršenim
dijagramom.

U usporedbu možemo uključiti i tekst pretvoren u brojčanu varijablu kodiranjem, uz pravila mjerenja koja smo već upoznali. **Kodirana kategorija
teksta** ovisi o pravilu koje smo odabrali. Za šest namjerno izabranih naslova
iz poglavlja o vizualizaciji dodjeljujemo jedan ako naslov sadržava `graphs`,
`graphical` ili `graphics`, a inače nulu. Pet naslova dobiva jedan, a jedan nulu.
Korelacija s godinom iznosi `r hr_broj(s6_r_kod_godina, 2)` [Anscombe, 1973; Cleveland, 1984;
Tufte, 2001; Wilkinson, 2005; Wickham, 2016; Matejka, 2017]. Taj rezultat opisuje
samo izabrane naslove i ne pokazuje opću promjenu znanstvenih naslova kroz
vrijeme.

Ako pravilu dodamo oblik `visual`, svih šest naslova dobiva jedan i
korelacija se više ne može izračunati jer nema razlika u kodu [Anscombe, 1973;
Cleveland, 1984; Tufte, 2001; Wilkinson, 2005; Wickham, 2016; Matejka, 2017].
Tekstovi su isti, a mjera se promijenila. Autor poglavlja sastavio je pravilo za potrebe ovog primjera. Zato uz kod navodimo pravilo, osobu koja ga je
odredila i tekstove na koje je primijenjen. Kasnije ćemo takve kategorije
proučavati u tablicama i razmotriti što se mijenja kada ih dodjeljuje
algoritam.

Izbor brojčanog prikaza važan je i kada izvorno imamo brojčana mjerenja.
Pearsonova korelacija koristi njihove razmake i sažima linearnu vezu. No dob i
minute u našoj anketi mogu se dosljedno kretati u suprotnim smjerovima, a da ne
prate pravac. Ako želimo opisati tu dosljednost poretka, trebamo mjeru koja
neće tražiti jednake promjene kroz cijeli raspon.

Vrijednosti zamjenjujemo rangovima. Najmanja dobiva prvi rang, sljedeća drugi,
a jednake dijele prosječni rang. Zatim na rangovima računamo Pearsonovu
korelaciju. **Spearmanov koeficijent ranga**, označen s $r_s$, tako mjeri
dosljednost kretanja u jednom smjeru, odnosno monotonu vezu. Naziva se i
Spearmanovom korelacijom. Rangovi čuvaju poredak, ali ne i izvorne razmake.

Pravilo za vezane rangove možemo vidjeti na namjerno zadanom nizu
10, 20, 20, 50. Rangovi su 1, 2,5, 2,5 i 4. Dvije dvadesetice dijele
prosjek drugoga i trećega mjesta. U anketi tako zasebno rangiramo svih 300
dobi i svih 300 vremena, pa povezujemo rangove koji pripadaju istoj osobi.

Na grafu dobi i minuta vidjeli smo strmiji pad među mlađima i izravnavanje
poslije, bez odvojene podskupine koja sama stvara odnos. Uz taj graf
uspoređujemo Pearsonovu korelaciju `r hr_broj(s6_r, 2)` i Spearmanovu `r hr_broj(s6_rs, 2)`. Razlika
odgovara vidljivoj zakrivljenosti, ali sama je ne bi dokazala. Pearsonova
korelacija dobi i logaritma minuta iznosi `r hr_broj(s6_r_log, 2)` i bliža je Spearmanovoj.
To je dodatna provjera ovog simuliranog odnosa, bez općeg pravila za izbor
mjere.

**Utjecajno opažanje** je opažanje čije uključivanje ili uklanjanje znatno
mijenja koeficijent. Ne mora svaka krajnja vrijednost biti utjecajna.

Sličnost Pearsonova i Spearmanova koeficijenta može odgovarati približno
pravocrtnoj monotonoj vezi, ali ne jamči takav oblik ni otpornost nalaza. Oba
koeficijenta može pomaknuti isti neobičan raspored. Njihova razlika također
nema jedno objašnjenje. Može nastati zbog zakrivljenosti, utjecajnih točaka,
vezanih rangova, podskupina ili suženog raspona. Zato najprije pregledavamo
graf i način odabira podataka. Sama razlika nije dovoljan razlog da odaberemo
Spearmanovu mjeru.

Ako veza nije monotona, oba koeficijenta mogu biti blizu nule. Zadovoljstvo,
primjerice, može biti nisko pri vrlo malom i vrlo velikom opterećenju. Uzlazni
i silazni dio tada se u koeficijentu poništavaju, iako graf pokazuje odnos.

## Ograničenje raspona i odabir

Uz izbor koeficijenta važno je razmotriti i izbor opažanja jer oba utječu na opis povezanosti. U približno linearnoj vezi sa sličnom
raspršenošću ishoda, odabir prema užem rasponu jedne varijable često smanjuje
apsolutnu korelaciju. Raspon koji nosi signal postaje manji, dok preostalo
rasipanje može ostati slično.

**Ograničenje raspona** (*range restriction*) nastaje kada promatrani uzorak
pokriva samo dio mogućih vrijednosti jedne ili obiju varijabli. Ono može
oslabiti izmjerenu povezanost, ali smjer promjene ovisi o obliku odnosa i
pravilu odabira.

Za čist prikaz slabljenja konstruirajmo 27 parova. Svaku vrijednost x od
jedan do devet ponovimo triput, a y dobijemo dodavanjem −2, 0 i 2. Unutar
svake vrijednosti x rasipanje je zato isto. Potom zadržimo samo x od četiri
do šest. Tako sužavamo raspon uz očuvano pravilo nastanka y.

*Slika. Isti linearni mehanizam prije i nakon ograničenja raspona. Konstruirani nastavni primjer, izrada autora.*

Manji raspon x uz isto rasipanje oko pravca daje slabiju korelaciju.
Sužavanje raspona ne mora uvijek smanjiti koeficijent. U zakrivljenoj vezi
možemo izdvojiti dio koji bolje ili slabije prati pravac. Ako odabir ovisi o
objema varijablama ili povezanoj trećoj, može se promijeniti i predznak. Zato
uspoređujemo grafove prije i nakon odabira te provjeravamo pravilo
uključivanja.

U cijeloj simuliranoj anketi korelacija dobi i minuta je `r hr_broj(s6_r, 2)`. Najmlađa
skupina ima `r s6_n_uzak` osoba sa sedam različitih dobi, od 18 do 24 godine.
Njezina korelacija iznosi `r hr_broj(s6_r_uzak, 2)` i ima drugi predznak. To se ne može
tumačiti samo kao slabljenje iste linearne veze. Generator razlikuje dobne
skupine, ali unutar najmlađe minute ne ovise o točnoj dobi. Populacijska
korelacija unutar nje zato je nula, a opaženih `r hr_broj(s6_r_uzak, 2)` proizlazi iz
promjenjivosti uzorka od `r s6_n_uzak` osoba.

Nalaz za najmlađu skupinu i veza u cijelom skupu odgovaraju na pitanja različitog obuhvata. Slično, istraživanje jedne studentske generacije opisuje uzak raspon dobi, dok zaključak o cijeloj odrasloj populaciji traži širi obuhvat. Za primljene kandidate,
zaposlene radnike ili preživjela poduzeća trebamo provjeriti kako je odabir
promijenio raspon, oblik i sastav opažanja.

U primjeru dobivamo koeficijent različit od nule iako je populacijska
korelacija unutar skupine nula. U usporedivim uvjetima takva su odstupanja češća u
manjim uzorcima. Na koeficijent može snažno utjecati i jedna udaljena točka
jer mijenja sredine, standardne devijacije i zajednička odstupanja. Zato uz
broj opažanja pregledavamo graf, podskupine i način odabira.

## Podskupine i obrat predznaka

Odabirom jedne dobne skupine promijenili smo odnos koji opisujemo. Sada
ispitujemo obrnut potez, spajanje različitih skupina u jedan prikaz. Kada
podskupine imaju različite razine obiju varijabli, zbirna korelacija može
imati suprotan predznak od korelacija unutar podskupina.

To ćemo prikazati konstruiranim podacima o trima odjelima, bez tvrdnje o
stvarnoj organizaciji. Unutar svakog odjela zadovoljstvo blago opada sa
stažem. Odjeli s iskusnijim zaposlenicima ipak imaju više prosječno
zadovoljstvo.

Za svaki odjel generirali smo 60 osoba. Staž je jednoliko raspoređen od 2
do 7 godina u A, od 7 do 12 u B i od 12 do 17 u C. U sredini tih raspona
zadovoljstvu zadajemo 3,6, 5,7 i 7,7. Za svaku godinu iznad sredine odjela
oduzimamo 0,42 i dodajemo neovisno normalno odstupanje standardne devijacije
0,5. Tako odjel istodobno određuje polazišta staža i zadovoljstva.
Zadovoljstvo je ovdje konstruirana kontinuirana vrijednost bez unaprijed
ograničenog raspona, a ne odgovor na stvarnu anketnu ljestvicu.
Četiri polja sljedećeg grafa pregrupiraju istih 180 generiranih zapisa.

*Slika. Konstruirani podaci u kojima zbirni oblak raste, a oblak unutar svakoga od triju odjela pada. To je konstruirani prikaz Simpsonova paradoksa. Četiri polja prikazuju iste točke bez regresijskih pravaca. Izrada autora; podaci i postupak opisani su u tekstu.*

Zbirna korelacija staža i zadovoljstva je pozitivna, `r hr_broj(s6_r_zbirno, 2)`. Unutar odjela
iznosi `r hr_broj(s6_r_odjeli$r[[1]], 2)`, `r hr_broj(s6_r_odjeli$r[[2]], 2)` i `r hr_broj(s6_r_odjeli$r[[3]], 2)`, pa su sve tri negativne. Svaki je
račun točan. Zbirni rezultat uključuje i razlike među odjelima, koje su ovdje
dovoljno velike da odrede pozitivan predznak.

To je pojava koju je Simpson opisao na frekvencijskim tablicama
(Simpson, 1951). Već smo je susreli u Berkeleyjskim stopama prijma, gdje se
zbirna razlika promijenila nakon razdvajanja odjela (Bickel, 1975). Grafovima
po skupinama možemo odvojiti razlike među skupinama od odnosa unutar njih.

Poseban problem nastaje kada iz korelacije među skupinama zaključujemo o
pojedincima. Zemlje, županije ili škole često su dostupne samo kao agregati.
Njihovom korelacijom ne dobivamo odnos među ljudima unutar njih. Agregiranje
uklanja dio unutarnjih razlika pa koeficijent može biti drukčiji, jači ili
drugog smjera. Zaključivanje o pojedincima iz takvih odnosa nazivamo
**ekološkom pogreškom** (*ecological fallacy*). Za individualni zaključak
trebamo podatke i dizajn na individualnoj razini. Odnos među zemljama ostaje
nalaz o zemljama.

## Država kao jedinica

Na objavljenim pokazateljima možemo provjeriti kako promjena jedinice
ograničava tumačenje povezanosti. S pojedinačnih osoba sada prelazimo
na države. Eurostat, statistički ured
Europske unije, objavljuje pokazatelje kojima uspoređujemo obrazovanje,
zaposlenost, siromaštvo, uporabu interneta i dobnu strukturu stanovništva
[{Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026].
Analiza se ovdje oslanja na objavljene vrijednosti. U izvornoj tablici jedan
redak pripada jednom pokazatelju za jednu državu i godinu. Kada pokazatelje
spojimo za graf, jedna točka predstavlja državu.

Za Hrvatsku i Francusku u nastavku vidimo po dva izvorna retka. Obrazovanje
se odnosi na osobe od 25 do 34 godine, a uporaba interneta na osobe od 16 do
74 godine ({Eurostat}, 2026; {Eurostat}, 2026). Povezivanjem
redaka iste države dobivamo par vrijednosti za jednu točku na grafu.

*Slika. Dva pokazatelja za dvije države u Eurostatovu izvatku za 2025. Izrada autora prema @eurostattertiary2026 i @eurostatinternet2026.*

U tablici su udjeli za čitanje zaokruženi na jednu decimalu. Za graf i
izračun povezanosti zadržavamo izvorne brojčane vrijednosti.

Eurostatov izvadak sadržava šest pokazatelja za 27 članica EU-a u 2025.,
odnosno 162 kombinacije `država + godina + pokazatelj` i 161 brojčanu
vrijednost [{Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026;
{Eurostat}, 2026]. Nedostaje samo rano napuštanje obrazovanja za
Luksemburg ({Eurostat}, 2026). Zadržan je zapis `:` s izvornom
oznakom `u` za nisku pouzdanost, bez oznake povjerljivosti
({Eurostat}, 2026). Ne zamjenjujemo ga nulom ni vrijednošću druge
godine.

Oznaka kvalitete razlikuje se od nedostajuće vrijednosti. Hrvatska vrijednost
ranog napuštanja obrazovanja iznosi 2,1 i također nosi `u`, ali je
objavljena kao broj ({Eurostat}, 2026). Oznaku `b`, koja
bilježi prekid vremenske serije, također čuvamo [{Eurostat}, 2026;
{Eurostat}, 2026]. Analiza ipak ostaje presjek jedne godine.

*Slika. Izvorne statusne oznake u cijelom izvatku od 162 retka. Izrada autora prema šest Eurostatovih skupova za 2025. [@eurostatemployment2026; @eurostatpoverty2026; @eurostattertiary2026; @eurostatearlyleaving2026; @eurostatinternet2026; @eurostatpopulation2026].*

Za ilustraciju biramo tercijarno obrazovanje i uporabu interneta jer nas
zanima odnos obrazovnog i digitalnog sudjelovanja, a oba pokazatelja pokrivaju
EU-27 ({Eurostat}, 2026; {Eurostat}, 2026). To je istraživački
izbor, bez unaprijed registrirane hipoteze. Prvi pokazuje udio osoba od 25 do
34 godine s tercijarnim obrazovanjem, a drugi udio osoba od 16 do 74 godine
koje su koristile internet u prethodna tri mjeseca [{Eurostat}, 2026;
{Eurostat}, 2026]. Svaka točka predstavlja državu. Veličina joj prikazuje
udio stanovništva od 65 godina naviše, a oblik čuva izvornu oznaku uz taj
pokazatelj. Tako prije koeficijenta vidimo odnos i moguću ulogu dobnog
sastava.

*Slika. Tercijarno obrazovanje i uporaba interneta u 27 država članica EU-a 2025. Veličina točke pokazuje udio stanovništva od 65 godina naviše, a oblik prenosi njegovu statusnu oznaku. Oznaka e znači procjenu, p privremenu vrijednost, a ep procijenjenu i privremenu vrijednost. Izrada autora prema Eurostatu [@eurostattertiary2026; @eurostatinternet2026; @eurostatpopulation2026].*

Za 27 država Pearsonova korelacija iznosi `r hr_broj(s6_r_eu, 2)`, a Spearmanova `r hr_broj(s6_rs_eu, 2)`
({Eurostat}, 2026; {Eurostat}, 2026). Bliske su i odgovaraju
uglavnom uzlaznom oblaku, ali ne dokazuju linearnost ili otpornost nalaza. U
EU-27 tijekom 2025. viši državni udjeli tercijarno obrazovanih osoba od 25 do
34 godine povezani su s višim udjelima uporabe interneta među osobama od 16 do
74 godine ({Eurostat}, 2026; {Eurostat}, 2026). To ne pokazuje odnos
obrazovanja i uporabe interneta kod pojedine osobe.

Veličina točaka potiče provjeru dobne strukture kao mogućeg trećeg čimbenika
({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026). Za tu bismo provjeru trebali ispitati odnos dobne strukture s objema glavnim
varijablama i razmotriti dizajn koji odvaja moguća objašnjenja. Ovaj presjek ne pokazuje
trend, uzrok, odnos među pojedincima ili nalaz izvan EU-27
({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026).

Moguća konfundirajuća varijabla mora prethoditi objema pojavama i utjecati na
njih. To prosuđujemo prema sadržaju i dizajnu. U konstruiranom primjeru odjel
tako oblikuje staž i zadovoljstvo. Razdvajanjem odjela vidimo promjenu
povezanosti, ali sama ta promjena ne dokazuje uzročnost. O neizmjerenom
čimbeniku koeficijent ne daje izravnu obavijest.

Isti koeficijent može odgovarati različitim objašnjenjima. Prva varijabla može
utjecati na drugu ili obrnuto, obje mogu ovisiti o trećoj, a obrazac može
nastati slučajnom promjenjivošću uzorka. Za razlikovanje tih mogućnosti
trebamo istraživački dizajn. Smjer uzroka procjenjujemo na temelju takvog dizajna i znanja o pojavi.

## Interakcija — Pogodi korelaciju

Svaki oblak ovdje je novi nastavni skup s 54 para bez mjerne jedinice.
Za jednu točku neovisno izvlačimo dvije normalne vrijednosti sa sredinom
nula i standardnom devijacijom jedan. Prva postaje $x$, a $y$ dobivamo
miješanjem dijela prvoga izvlačenja i dijela drugoga. Više zajedničkoga
dijela znači jaču vezu, a negativan predznak zajedničkoga dijela silaznu vezu.
Generator zadaje četiri različite populacijske korelacije, dok koeficijent
svakog konačnog oblaka računamo iz njegovih 54 para. Uzorački koeficijenti pritom mogu odstupati od zadanih populacijskih vrijednosti. Točke ostaju iste dok čitatelj iskušava vlastite procjene.

Četiri raspršena oblaka omogućuju usporedbu smjera i jačine
povezanosti. Najprije promatramo oblik svakog oblaka. Tablica koja slijedi
donosi Pearsonove korelacije i zadane procjene, pa se može provjeriti
koliko su procjene blizu izračunanim vrijednostima.

*Slika. Četiri deterministički simulirana oblaka bez prikazanih koeficijenata. Zajedničke osi omogućuju usporedbu smjera i zbijenosti.*

**Što isprobati.**

1. Procijenite samo znak svake povezanosti i provjerite jesu li klizači na pravoj strani nule.
2. Usporedite oblake A i D te procijenite koji je odnos bliže savršenoj povezanosti.
3. Fino namjestite procjene za slabije oblake B i C bez mijenjanja prvih dviju.
4. Otvorite rješenje, usporedite četiri odstupanja i opišite koji je oblak bilo najteže procijeniti.

Predznak je lakše uočiti nego točnu jačinu veze. Pri usporedbi oblaka A i D
trebamo i jednake ljestvice. Uz dobro procijenjen koeficijent potreban je i pregled oblika oblaka.

**Statistika u divljini.**
**Dinosaur s urednim sažetkom.** Zamislimo da na pregled dobijemo analizu
povezanosti dviju varijabli. Priložene su njihove sredine, standardne
devijacije i Pearsonov koeficijent, ali nema grafa. Račun možemo
ponoviti i dobiti iste brojeve. Prije nego što prihvatimo opis odnosa,
još trebamo saznati kako su opažanja raspoređena.

Matejka i Fitzmaurice pokazali su koliko toga takav sažetak može
izostaviti. Njihov postupak sitnim pomacima točaka mijenja izgled skupa,
a zadane sažetke čuva do druge decimale (Matejka, 2017). Polazeći od
Cairova obrisa dinosaura, proizveli su skupove koji izgledaju poput
zvijezde, kruga ili nizova crta, uz iste zaokružene sredine,
standardne devijacije i korelaciju (Matejka, 2017). Podaci su namjerno konstruirani za tu demonstraciju.

Takva demonstracija mijenja našu procjenu izvještaja. Podudaranje
sažetaka potvrđuje da smo ponovili račun, ali ne potvrđuje da je
koeficijent dovoljan opis. Slaba linearna povezanost može pratiti
uređen zakrivljeni oblik. Može se pojaviti i u skupu s odvojenim
nakupinama. Te razlike traže različita daljnja pitanja, iako se ne
vide u jednome broju.

U zamišljenoj analizi zato bismo zatražili raspršeni dijagram svih
parova. Ako on pokaže zakrivljenost, rečenicu o slaboj vezi trebali
bismo ograničiti na linearnu povezanost. Ako pokaže skupine ili
izdvojena opažanja, provjerili bismo što predstavljaju prije
izračunavanja novih koeficijenata. Njihovo bi eventualno uklanjanje zahtijevalo obrazloženje povezano s kvalitetom podataka ili istraživačkim pitanjem.

Dinosaur je pamtljiv zato što radikalno razdvaja ono što vidimo od
onoga što koeficijent sažima. U stvarnim podacima raspored će rijetko
biti tako upadljiv, ali odluka ostaje ista. Uz provjeru je li broj
točan trebamo provjeriti i koju bi važnu osobinu odnosa čitatelj
propustio kada bismo mu pokazali samo taj broj.

**Nađite grešku.**
U simuliranoj anketi od 300 osoba provjeravamo odnos dobi i dnevnih
minuta na društvenim mrežama. Asistentu je postavljeno
pitanje o cijelom uzorku. Vratio je ovaj račun.

Za provjeru su dostupni isti sažeci koje smo usporedili uz raspršeni
dijagram. Pearsonov koeficijent u tablici opisuje linearnu povezanost.

| Uključene osobe | Broj osoba | Pearsonov koeficijent |
|---|---:|---:|
| Cijeli simulirani uzorak | 300 | −0,56 |
| Osobe od 18 do 24 godine | `r s6_n_uzak` | `r hr_broj(s6_r_uzak, 2)` |

: Dob i dnevno vrijeme u dvama obuhvatima. Izrada autora.

> Račun daje korelaciju `r hr_broj(s6_r_uzak, 2)` uz `r s6_n_uzak`
> ispitanika. Prema tome, dob i vrijeme korištenja nisu negativno
> povezani u cijelom simuliranom uzorku.

Pridružite ispis jednom retku tablice. Označite mjesto na kojem se
odgovor udaljio od postavljenog pitanja i napišite zamjenski zaključak
koji opisuje oba obuhvata. Sačuvajte točan rezultat asistentova računa.

## Razrađeni primjer

U odnosu dobi i dnevnog vremena korištenja već smo vidjeli zašto koeficijent
trebamo čitati uz graf. Sada te provjere povezujemo u jedno izvješće o
simuliranoj anketi. Graf pokazuje oblik odnosa. Pearsonov koeficijent sažima
koliko odnos prati pravac, a Spearmanov koliko dosljedno slijedi silazni
poredak. Zaključak se odnosi na te simulirane podatke.

Za oba opisa koristimo iste parove dobi i minuta. Poziv `summarise`, koji
već poznajemo, okuplja sažetke, a funkcija `cor` računa korelaciju
dvaju stupaca. Zadana je Pearsonova korelacija. Odabirom Spearmanove u
argumentu `method` mijenjamo način sažimanja odnosa, dok osobe i njihove
vrijednosti ostaju iste.

Graf pokazuje da se pad vremena s dobi poslije izravnava. Pearsonova
vrijednost `r hr_broj(s6_r, 2)` opisuje linearnu vezu, a Spearmanova `r hr_broj(s6_rs, 2)`
dosljednost silaznog poretka. Razlika je spojiva sa zakrivljenošću koju smo
vidjeli, ali bez grafa ne bi bila dovoljna za taj zaključak.

Rezultat možemo navesti ovako. U simuliranom uzorku od `r s6_n` ispitanika
dob i dnevno vrijeme korištenja negativno su povezani. Graf pokazuje
zakrivljen silazni odnos, uz Spearmanovu korelaciju `r hr_broj(s6_rs, 2)` i Pearsonovu
`r hr_broj(s6_r, 2)`, manjeg apsolutnog iznosa. Ne zaključujemo o uzroku jer je skup
simuliran i presječan, bez istraživačke intervencije ili zabilježenog
vremenskog redoslijeda.

## Od odnosa do tvrdnje

Na Eurostatovu presjeku pratimo kako od izvornog retka dolazimo do rečenice
o povezanosti i što usput treba provjeriti.

| Revizijsko pitanje | Primjena na Eurostatov odnos |
|---|---|
| Koja je jedinica? | nakon spajanja pokazatelja, jedna država članica EU-a u 2025. |
| Tko ili što nedostaje? | pojedinci unutar država, zemlje izvan EU-27 i druga razdoblja nisu jedinice ovoga presjeka |
| Koji je cilj tvrdnje? | Pearsonov i Spearmanov koeficijent opisuju povezanost dvaju državnih udjela |
| Gdje je neizvjesnost? | statusne oznake prenose upozorenja izvora; koeficijenti ne mjere uzoračku ni mjernu nesigurnost, a presjek ne pokazuje promjenu kroz vrijeme |
| Koje drugo objašnjenje ostaje? | druga dobna skupina ili pokazatelj, rangovi umjesto vrijednosti ili drukčije opravdano postupanje sa statusnim oznakama |
| Tko snosi posljedice? | pogrešan opis stanovnika ili država može dovesti do neutemeljene uredničke ili javne odluke |

: Šest revizijskih pitanja primijenjenih na povezanost službenih agregata. Izrada autora prema Eurostatu ({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026).

Promjena jedinice mijenja i ono što procjenjujemo, moguća objašnjenja te
posljedice zaključka. Statusna oznaka također traži prosudbu. O uključivanju retka odlučujemo prema značenju oznake; pravilo unaprijed obrazlažemo i navodimo u izvještaju.

**Granica tvrdnje o povezanosti** ovisi o jedinici, obuhvatu i načinu
mjerenja. Sljedeća tablica pokazuje koje vrste tvrdnji ti podaci podupiru.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opis vrijednosti i izvornih statusnih oznaka za šest pokazatelja u EU-27 2025. |
| povezanost | odnos državnih udjela tercijarnoga obrazovanja i uporabe interneta u istom presjeku |
| generalizacija | nije poduprta izvan država, godine i dobnih obuhvata koje izvori navode |
| predviđanje | nije poduprto jer nijedno prediktivno pravilo nije izgrađeno ni provjereno na doista novim opažanjima |
| uzročnost | nije poduprta jer vremenski redoslijed i konkurentska objašnjenja nisu razdvojeni |
| odluka | poduprta je omeđena urednička odluka o poštenoj formulaciji nalaza, ali ne obrazovna ili digitalna politika |

: Šest dimenzija tvrdnje na granici Dijela II. Izrada autora prema Eurostatu ({Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026; {Eurostat}, 2026).

Za ovaj presjek možemo reći da su dva državna udjela u EU-27 2025. pozitivno
povezana ({Eurostat}, 2026; {Eurostat}, 2026). Iz toga ne izvodimo
zaključak o pojedincima, uzrocima, budućnosti ili drugim zemljama.

Za samoprovjeru možemo odgovoriti na četiri pitanja. Što predstavlja točka
Eurostatova grafa? Zašto je Luksemburg uključen u glavni odnos, ali ne i u
odnos s ranim napuštanjem obrazovanja? Zašto prije usporedbe koeficijenata
pregledavamo graf? Koje tri vrste zaključka ovaj presjek ne podupire i što bi
nam za njih trebalo?

Tri pogrešna tumačenja iz ovoga dijela knjige možemo provjeriti istim redom.
Najprije ustanovimo što je doista u podacima, zatim usporedimo tvrdnju s
odgovarajućim prikazom i na kraju odredimo granicu zaključka. Tako se
provjere tablice, grafa i koeficijenta nadovezuju jedna na drugu.

| Provjera | Sažetak u poglavlju o sažimanju | Graf u poglavlju o vizualizaciji | Povezanost u ovom poglavlju |
|---|---|---|---|
| Pogrešan zaključak | spoj po godini valjan je jer se zbroj prikazanih redaka može izračunati | treći stupac može biti širi radi optičke ravnoteže | povezanost u jednoj dobnoj podskupini određuje smjer veze u cijelom uzorku |
| Što gledamo | jedinicu retka, puni ključ, broj redaka i zbroj prije i nakon spajanja | jednake širine stupaca, os od nule i čitljivost bez boje | filtrirani uzorak, cijeli oblak točaka i oblik veze |
| Gdje je provjera | tablica kontrole spajanja i oznaka dostupnosti metrike | usporedba dviju osi i tablica izbora prikaza | raspršeni dijagram dobi i minuta te koeficijenti za cijeli uzorak |
| Granica | opis vrijedi za uključeni DigiKatov korpus | graf ne nadomješta provjeru podataka i uredničkoga pitanja | povezanost ne pokazuje uzrok ni populacijski doseg |

: Tri provjere pogrešnih analiza u Dijelu II. Izrada autora.

## Sažetak

Od zajedničkih odstupanja dviju varijabli izgradili smo kovarijancu, a
standardizacijom Pearsonovu korelaciju, mjeru linearne veze između minus jedan
i plus jedan koja ne ovisi o mjernim jedinicama. Kada vrijednosti zamijenimo
rangovima, Spearmanovim koeficijentom opisujemo monotonost, pri čemu gubimo
izvorne razmake. Graf nam pomaže protumačiti obje mjere jer pokazuje
podskupine, utjecajna opažanja i oblik koji se može promijeniti sužavanjem
raspona. Na rezultat utječu i pravilo kojim tekst pretvaramo u brojčane oznake
te izbor jedinice, pa povezanost među državama ne prenosimo na pojedince. Za uzročni zaključak i dalje trebamo odgovarajući dizajn. U
sljedećem dijelu vjerojatnost će nam pomoći razumjeti kakve obrasce može
proizvesti sam slučajni postupak.

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
njihovih dijagrama i što bi na njima trebalo pregledati.
[U digitalnom izdanju unesite četiri procjene u interakciju i otvorite
rješenje.]
U tisku uzmite četiri zadane procjene i koeficijente iz tablice.
Za svaki oblak
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
