# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Uzorkivač dviju grupa | simulirana populacija | pogl. 2, 4, 9–11 |

**Vinjeta.**
Cumming je istraživačima predložio promjenu koja izgleda
skromno, a mijenja cijeli izvještaj. Umjesto da rad završi oznakom je li
rezultat prešao prag, treba dati procjenu razlike i interval koji uz nju ide
(Cumming, 2014).

Prijedlog nije bio tehnički. Autor koji piše da razlika postoji rekao je manje
nego autor koji piše koliko ona iznosi i koje su vrijednosti s podacima još
uskladive. Prvi izvještaj se ne može ni s čim usporediti, a drugi ulazi u
sljedeće istraživanje kao brojka.

Kako jednu usporedbu dviju sredina povezati s dizajnom iz kojeg je nastala, s
veličinom koju opisuje i s općim jezikom modela?

## Tko nosi dva rezultata

Usporedba dviju sredina izgleda kao jedno pitanje, a zapravo skriva tri.
Razlika je u tome odakle dolaze dva broja koja uspoređujemo, i to pitanje nije
statističko nego pitanje o dizajnu istraživanja.

U prvom slučaju imamo jednu skupinu i unaprijed zadanu vrijednost, primjerice
sredinu ljestvice ili prag odluke. Procjena iz ranijeg anketnog vala nije takva
konstanta, jer nosi vlastitu uzoračku nesigurnost i možda drugu ciljnu populaciju
ili način mjerenja. Nju treba usporediti kao drugu procjenu, s objema
nesigurnostima. U drugom slučaju imamo dvije odvojene skupine sastavljene od
različitih ljudi, recimo osobe kojima je primarni izvor vijesti TV i osobe koje
navode društvene mreže. U trećem slučaju iste jedinice mjerimo dva puta, prije i
poslije nekog događaja, pa svaki ispitanik nosi oba rezultata.

**Jedinica neovisnosti** je entitet koji se u istraživanju mogao pojaviti ili
izostati neovisno o ostalima, pa njegove vrijednosti nisu unaprijed vezane uz
vrijednosti bilo koje druge jedinice u istom skupu.

Ta jedinica određuje sve ostalo. U usporedbi dviju skupina to je osoba, jer je
svaka osoba u samo jednoj skupini. U ponovljenom mjerenju to je i dalje osoba,
ali sada nosi dva rezultata koja su međusobno povezana, pa se analiza ne provodi
na četrdeset neovisnih mjerenja nego na dvadeset razlika. Postupak koji tu vezu
previdi tretira mjerenja kao neovisne jedinice i izostavlja kovarijancu unutar
para, pa računa pogrešnu nesigurnost. Uz pozitivnu povezanost iz ovog poglavlja
interval je nepotrebno širok.

Prvi korak analize zato nije izbor testa nego rečenica koja imenuje jedinicu.
Ako se ta rečenica ne može napisati, podaci još nisu spremni za bilo kakvu
usporedbu.

Ponovljeno mjerenje nije jedini znak ovisnosti opažanja. Učenici iz istog
razreda, članovi istog kućanstva i osobe povezane društvenom mrežom mogu dijeliti
izvor varijacije, iako u tablici zauzimaju različite retke. Čim dizajn sadrži
takvo gnijezdo ili vezu, zaustavljamo račun za neovisne skupine. Ovo poglavlje
ne uvodi modele za ovisne podatke, nego traži da se zapišu jedinica i veza te
odabere postupak koji tu strukturu može sačuvati.

## Razlika prije oznake

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s14$n` osoba koje navode TV ili društvene mreže
kao primarni izvor vijesti, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije. Glavni primjer i obvezni zadatak dostupni su bez mreže u
lokalnom skupu `populacija_medija` i upravljanom agregatu
`data/populacija-medija-agregat.csv`. Kao neobveznu nadogradnju čitatelj može na
vlastitoj portalnoj kopiji ESS Round 11, edition 3.0 usporediti prijavljeno
glasanje bez pondera i uz `anweight`, nakon što iz službenih metapodataka odredi
valjani nazivnik za `vote`; ESS mikropodaci i rezultat nisu dio knjige. Osobe s
drugim ili nedostajućim primarnim izvorom vijesti ostaju izvan glavne usporedbe.

Redoslijed izvještavanja postavljamo prije nego što bilo što izračunamo. Prvo
dolazi razlika u izvornim jedinicama, zatim interval koji joj pripada, pa tek
onda test i standardizirana razlika. Taj redoslijed nije stvar ukusa. Razlika i
njezin interval odgovaraju na pitanje koliko iznosi učinak, a test odgovara na
mnogo uže pitanje je li podacima uskladiva i nula.

U našem uzorku prosječno povjerenje iznosi
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "TV"], 2)` među onima koji
navode TV kao primarni izvor vijesti i
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "društvene mreže"], 2)` među
onima koji navode društvene mreže. Razlika iznosi
`r hr_broj(s14$razlika, 2)` boda uz interval pouzdanosti od
`r hr_broj(s14$donja, 2)` do `r hr_broj(s14$gornja, 2)`.

To je Welchov interval, koji zadržava zasebnu procjenu varijance za svaku
skupinu. Pripadni dvostrani test postavlja nultu hipotezu da je populacijska
sredina TV skupine minus populacijska sredina skupine društvenih mreža jednaka
nuli, nasuprot mogućnosti da razlika nije nula. Riječ je o razlici
populacijskih sredina, ne o jednakosti cijelih raspodjela.

Interval je ovdje važniji od svega ostaloga. On kaže da su s ovim uzorkom
uskladive i razlike ispod pola boda i razlike blizu dva boda, dakle raspon
unutar kojeg bi se praktične odluke mogle razlikovati. Izvještaj koji bi umjesto
toga napisao samo da je razlika značajna o toj neizvjesnosti ne bi rekao ništa.

Budući da je populacija simulirana, znamo i točan odgovor. Prava razlika u njoj
iznosi `r hr_broj(s14$pop_razlika, 2)` boda i ovaj je interval obuhvaća. Jedan
takav ishod ne provjerava stopu pokrivanja, a što intervali rade u dugom nizu
ponavljanja pokazalo je poglavlje o procjeni.

## Interakcija — Uzorkivač dviju grupa

Sljedeći prikaz razdvaja dvije stvari koje se u praksi redovito brkaju.
Preklapanje pojedinačnih rezultata dviju skupina jedna je stvar, a preciznost
procijenjene razlike druga. Čitatelj odvojeno mijenja stvarnu razliku,
raspršenost ishoda i broj jedinica, i može prebaciti dizajn iz neovisnog u
upareni uz nepromijenjene ostale postavke.

*Slika. Jedan simulirani uzorak dviju skupina i raspodjela procijenjene razlike kroz ponovljene uzorke.*

**Što isprobati.**

1. Povećajte stvarnu razliku uz jednaku raspršenost.
2. Povećajte raspršenost uz jednaku razliku i pogledajte oba panela.
3. Povećajte broj jedinica bez promjene razlike i raspršenosti.
4. Prebacite dizajn u upareni uz sve ostalo nepromijenjeno.

Posljednji korak pomiče samo jednu postavku, a raspodjela procjena vidljivo se
sužava. Uparivanje ne mijenja ni stvarnu razliku ni raspršenost ishoda, nego
uklanja onaj dio razlike među mjerenjima koji potječe od razlika među samim
jedinicama. Ta dobit postoji samo dok analiza vezu unutar para zadrži.

## Ista razlika, dva dizajna

Tvrdnja da dizajn mijenja zaključak zvuči apstraktno dok se ne vidi na jednom
skupu brojeva. Zato konstruiramo mjerenje `r s14$np` osoba prije i poslije
jednog događaja. Skup je izmišljen za ovu svrhu i nije nalaz ni o kome, a jedino
što iz njega učimo jest račun za povezana mjerenja. Pomak, varijance i povezanost
zadani su simulacijom. Bez kontrolne skupine ili randomizacije prosječna promjena
ne bi bila dokaz da ju je događaj uzrokovao.

Povezanost dvaju mjerenja iznosi `r hr_broj(s14$r_parova, 2)`. Osobe koje su
imale visoku vrijednost prije imale su je uglavnom i poslije, pa najveći dio
raspršenosti u oba mjerenja potječe od razlika među osobama, a ne od promjene
koja nas zanima.

Prosječna promjena iznosi `r hr_broj(s14$m_razlika, 2)` uz standardnu devijaciju
razlika od `r hr_broj(s14$sd_razlika, 2)`. Analiza koja pare zadrži daje interval
od `r hr_broj(s14$up_donja, 2)` do `r hr_broj(s14$up_gornja, 2)` i p-vrijednost
od `r formatC(s14$up_p, format = "f", digits = 4, decimal.mark = ",")`.

Ista mjerenja, obrađena kao da su dvije neovisne skupine, daju interval od
`r hr_broj(s14$nez_donja, 2)` do `r hr_broj(s14$nez_gornja, 2)` i p-vrijednost
od `r formatC(s14$nez_p, format = "f", digits = 3, decimal.mark = ",")`. Isti
podaci, ista prosječna promjena, i dva zaključka koja bi u izvještaju izgledala
suprotno.

Razlog nije u računu nego u nazivniku. Neovisna analiza mjeri razliku prema
raspršenosti među osobama, koja je ovdje velika. Uparena analiza mjeri je prema
raspršenosti promjena unutar osoba, koja je mnogo manja jer je razlika među
osobama oduzeta. Uparivanje zato nije trik za manju p-vrijednost nego posljedica
toga da je promjena unutar osobe druga veličina od razlike među osobama.

Koliko se time dobiva, ovisi o varijanci razlika, koju određuju raspršenost oba
mjerenja i njihova povezanost. Uz slične rubne varijance veća pozitivna
povezanost obično daje uži interval, dok slaba povezanost ne donosi očekivani
dobitak, a pogrešno sastavljeni parovi mogu ga i poništiti. Uparivanje se zato
određuje dizajnom i stvarnim identitetom jedinice, a ne bira nakon što se vide
podaci.

## Jedan model iza triju testova

Tri dizajna iz prvog odjeljka ostaju tri različite podatkovne situacije. Kod
neovisnih skupina razliku koju smo već procijenili možemo zapisati i kao
koeficijent uz binarnu oznaku skupine. Taj zapis ovdje služi samo kao most prema
kasnijim poglavljima.

$$\text{povjerenje} = \beta_0 + \beta_1 \cdot \text{skupina} + \varepsilon$$

Oznaka $\beta_0$ stoji za očekivani ishod u skupini koja je uzeta kao polazna,
$\beta_1$ za razliku između druge i te polazne skupine, a $\varepsilon$ za ono
što model o pojedinoj osobi nije objasnio. Varijabla skupine poprima vrijednost
nula za polaznu i jedan za drugu skupinu, pa se sve svodi na dva broja.

**Referentna skupina** je kategorija prema kojoj se izražavaju sve ostale
kategorije istog prediktora, pa njezina sredina postaje polazna vrijednost
modela, a koeficijenti ostalih kategorija odstupanja od nje.

U našem uzorku polazna je skupina onih koji se informiraju preko društvenih
mreža, pa $\beta_0$ iznosi `r hr_broj(s14$presjek, 2)` i jednak je njihovoj
sredini. Koeficijent $\beta_1$ iznosi `r hr_broj(s14$nagib, 2)` i jednak je
razlici koju smo već izračunali. Zamijenimo li referentnu skupinu, odsječak i
predznak koeficijenta promijenit će se, ali dvije procijenjene skupne sredine i
podaci neće.

Jednouzoračna usporedba polazi od jedne sredine i vanjske vrijednosti, a uparena
usporedba od sredine razlika unutar parova. Ne treba ih pretvarati u isti ispis
da bi se vidjelo što dijele, a to su procjena, nesigurnost i pitanje o nuli.
Poglavlje o više skupina proširit će oznaku skupine, a poglavlje o regresiji
objasniti širi doseg modelnoga zapisa. Ovdje se zaustavljamo na binarnoj oznaci i
ne izjednačujemo inferenciju različitih dizajna.

Model pritom ne zamjenjuje dizajn. Koeficijent opisuje razliku među skupinama
onako kako su one nastale, a uzročno značenje dolazi isključivo iz načina na koji
je pripadnost skupini dodijeljena. Ako je ljudi biraju sami, model o uzroku ne
govori ništa, koliko god uredno bio ispisan.

## Što razlika sama ne kaže

Razlika u izvornim jedinicama nosi značenje samo dok se zna koliko je ljestvica
raspršena. Bod razlike na ljestvici čije su vrijednosti zbijene znači nešto
sasvim drugo nego bod razlike na ljestvici na kojoj su ljudi raspoređeni široko.
Standardizirana razlika upravo to uzima u obzir.

Standardiziranu razliku uvelo je poglavlje o veličini učinka i snazi, gdje je
razlika sredina podijeljena združenom standardnom devijacijom skupina, pa se
izražava u standardnim devijacijama umjesto u izvornim jedinicama.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Za naše dvije skupine ta veličina iznosi `r hr_broj(s14$d, 2)`. Uobičajene
orijentacijske vrijednosti postoje i najčešće se navode prema Cohenu, ali ih je i
sam izvor ponudio kao pomoć u odsutnosti boljeg oslonca (Cohen, 1988). Kod
uparenog dizajna nazivnik je drugi, jer se dijeli standardnom devijacijom
razlika, pa dvije veličine s istim imenom nisu izravno usporedive. Naš upareni
skup daje `r hr_broj(s14$up_d, 2)`.

Standardizacija ipak ne rješava ono zbog čega usporedbe dviju skupina najčešće
zavaravaju. U našim podacima skupine se ne razlikuju samo po izvoru vijesti.
Prosječna dob onih koji navode društvene mreže kao primarni izvor iznosi
`r hr_broj(s14$pop_dob_mreze)` godine, a onih koji navode TV
`r hr_broj(s14$pop_dob_tv)` godine, dok povjerenje u ovoj populaciji raste s
dobi.

Budući da je simulirana populacija poznata, možemo provesti opisnu analizu
osjetljivosti. Ukupna razlika u njoj iznosi
`r hr_broj(s14$pop_razlika, 2)` boda. Promijenimo li ciljnu populaciju na osobe
od trideset do četrdeset devet godina, unutar koje se skupine manje razlikuju po
dobi, razlika iznosi `r hr_broj(s14$pop_razlika_uska, 2)` boda. Taj postupak ne
mjeri „udio zbog dobi” i ne razdvaja uzročne učinke dobi i izvora vijesti.

U našem uzorku u taj raspon upada `r s14$uzak_n` od `r s14$n` osoba, a interval
razlike proteže se od `r hr_broj(s14$uzak_donja, 2)` do
`r hr_broj(s14$uzak_gornja, 2)`, dakle preko nule. U odnosu na ukupnu usporedbu
ovdje je ciljna razlika manja, a procjena manje precizna zbog manjeg broja
jedinica. Koliko podataka treba da bi se razlika zadane veličine mogla razlučiti
objašnjava poglavlje o veličini učinka i snazi.

Razlika vrijedi samo za način na koji su ovdje izmjereni povjerenje i izvor
vijesti te za populaciju koju dizajn može dosegnuti. Odluka traži još jedan
unaprijed izrečen prag. Interval od pola do gotovo dva boda može biti dovoljno
uzak za odluku kojoj je važna bilo koja pozitivna razlika, a preširok za odluku
koja traži barem dva boda. Podaci ne biraju između tih kriterija umjesto
istraživača.

## Pretpostavke i njihove granice

Najvažnija pretpostavka dolazi iz dizajna. Opažanja moraju pripadati neovisnim
jedinicama, a svaka osoba samo jednoj od dviju skupina. Ishod mora biti ispravno
kodirana brojčana varijabla, pripadnost skupini mora imati točnu referentnu
kategoriju, a način uzorkovanja mora podupirati ciljnu populaciju o kojoj se
piše. Nijedan izbor testa ne može popraviti povredu tih uvjeta.

Za točnu t-inferenciju u malim uzorcima ishodi unutar skupina moraju slijediti
normalnu raspodjelu, a u velikima su potrebne konačne varijance i odsutnost
opažanja koje samo određuje rezultat. Kod uparenog dizajna ti se uvjeti odnose
na raspodjelu razlika, ne na raspodjelu pojedinačnih mjerenja.

Welchova standardna pogreška zadržava varijancu i veličinu svake skupine
zasebno, pa ne zahtijeva jednake varijance. Obični linearni model procjenjuje
jednu zajedničku rezidualnu varijancu i raspoređuje je na obje skupine, zbog
čega njegova uobičajena homoskedastična inferencija pretpostavlja jednake
uvjetne rezidualne varijance.

U našem uzorku veličine i varijance skupina nisu jednake, pa Welch ostaje
početni izbor. On i obični linearni model daju istu procijenjenu razliku, ali
nesigurnost računaju pod različitim pretpostavkama. Brojčanu razliku u
standardnim pogreškama, stupnjevima slobode i intervalima prikazuje razrađeni
primjer. Obični linearni model ondje služi kao izričito označena usporedba pod
pretpostavkom jednake rezidualne varijance.

Normalnost se procjenjuje pogledom na raspodjelu, a tek onda testom.
Shapiro-Wilkov rezultat, kao i rezultati drugih testova, snažno ovisi o veličini
uzorka. Velik uzorak može otkriti zanemarivo odstupanje, a mali propustiti ono
koje je važno. Rezultat zato ne može biti prekidač koji sam odlučuje o izboru
postupka.

Krajnja opažanja traže pregled, a ne automatsko brisanje. Mogu biti pogreške u
unosu, mogu biti rijetki ali stvarni slučajevi, a mogu biti i znak da sredina
nije prikladan sažetak te varijable. Analiza provedena s njima i bez njih, uz oba
rezultata u izvještaju, poštenija je od tihe odluke donesene nakon pogleda na
p-vrijednost.

Wilcoxonov postupak radi s rangovima umjesto s izvornim veličinama, pa krajnja
vrijednost obično ima manji utjecaj nego na sredinu, ali postupak nije imun na
neobična opažanja. U uparenoj inačici ispituje raspored predznaka i rangova
razlika, a ne prosječnu razliku, pa nije zamjenski put do iste tvrdnje. U našem
uparenom skupu daje
p-vrijednost od
`r formatC(s14$wilcoxon_p, format = "f", digits = 4, decimal.mark = ",")`, dakle
isti zaključak, ali ne i istu tvrdnju.

**Statistika u divljini.**
**Preklapanje crtica.** Pravilo da razlika nije značajna ako se crtice pogreške
na grafu preklapaju kruži znanstvenim tekstovima kao da je egzaktno. Belia i
suradnici izvijestili su o 473 autora radova iz psihologije, bihevioralne
neuroznanosti i medicine koji su dovršili internetski zadatak pomicanja dviju
sredina s crticama sve dok razlika ne postane taman značajna (Belia, 2005).

Odgovori su pokazali da mnogi vodeći istraživači ne razlikuju interval
pouzdanosti od standardne pogreške i ne uzimaju u obzir jesu li dvije sredine
neovisne ili dolaze iz ponovljenog mjerenja. Upravo to razlikovanje nosi cijelo
ovo poglavlje. Nalaz je pritom o čitanju grafova, a ne o crticama, pa iz njega
slijedi da graf mora reći koju veličinu prikazuje i iz kojeg dizajna dolazi, a ne
da se crtice izbjegavaju.

**Pitajte model.**
Asistent može odmah ponuditi t-test čim vidi jednu kategoričku i jednu brojčanu
varijablu te preskočiti ono što bi moralo doći prvo. Prije poziva mu treba
opis dizajna i identifikator jedinice, jer iz samog oblika tablice ne može znati
jesu li dva stupca dva mjerenja istih osoba. Provjeravamo je li uparivanje
sačuvano, koristi li Welchovu inačicu, izvještava li razliku i interval prije
testa i je li tiho izbacio retke s praznim vrijednostima.

> Opisat ću dizajn i reći koja varijabla identificira jedinicu. Prvo prikaži
> raspodjele obiju skupina, zatim procijeni razliku s intervalom u izvornim
> jedinicama, pa tek onda provedi odgovarajući test i navedi veličinu učinka.

**Nađite grešku.**
Jedinica neovisnosti označena je kao osoba, a svaka je osoba u samo jednoj
skupini. Referentna skupina su društvene mreže, pa pozitivan koeficijent uz TV
znači višu sredinu u TV skupini. Raspodjele i neobična opažanja pregledani su, a
Welchov test ne traži jednake varijance. Analiza je zatim ponovljena među osobama
od 30 do 49 godina, gdje interval razlike obuhvaća nulu. Zaključak izvještaja
glasi da u toj dobnoj skupini primarni izvor vijesti nema veze s povjerenjem.

## Razrađeni primjer

Cijela usporedba dviju skupina može se ispisati u nekoliko redaka, i vrijedi je
jednom vidjeti u obliku u kojem će se od ovog poglavlja nadalje pojavljivati.
Analiza najprije daje Welchovu procjenu i interval, a zatim istu razliku zapisuje
kao koeficijent modela s binarnim prediktorom. Drugi ispis služi usporedbi
postupaka, ne zamjenjuje prvi.

Funkcija `t.test` bez dodatne postavke provodi Welchov postupak. Zapis
`povjerenje_medijima ~ izvor` čita se kao tvrdnja da ishod ovisi o skupini, a
funkcija `lm` procjenjuje takav model uz običnu homoskedastičnu nesigurnost.
Funkcija `df.residual` vraća broj stupnjeva slobode uz taj ispis.

Welchov ispis daje razliku od `r hr_broj(s14$razlika, 3)` boda, standardnu
pogrešku od `r hr_broj(s14$se_welch, 3)` i
`r hr_broj(s14$df_welch, 3)` stupnja slobode. Koeficijent modela nosi točno istu
razliku, jer je koeficijent uz TV razlika sredine televizijske i referentne
skupine društvenih mreža. Njegova obična standardna pogreška ipak iznosi
`r hr_broj(s14$se_ols, 3)` uz `r s14$df_ols` stupnjeva slobode. Interval modela
proteže se od `r hr_broj(s14$ols_donja, 3)` do
`r hr_broj(s14$ols_gornja, 3)`, prema Welchovu intervalu od
`r hr_broj(s14$donja, 3)` do `r hr_broj(s14$gornja, 3)`. Jednakost procjene
razlike zato je egzaktna, a jednakost inferencije nije. Kad broj skupina u
sljedećem poglavlju poraste s dvije na pet, modelni zapis ostaje
srodan, ali izbor postupka za nesigurnost ostaje zasebna odluka.

Izvještaj koji bi na tome stao još ne bi bio potpun. Treba mu opis kako su skupine
nastale, jer ljudi svoj izvor vijesti biraju sami, i napomena da skupine nisu
izjednačene po dobi. Bez toga bi ista brojka lako prešla iz rečenice o razlici u
rečenicu o učinku, a to su dvije različite tvrdnje.

## Sažetak

Usporedba dviju grupa počinje dizajnom i rečenicom koja imenuje jedinicu
neovisnosti. Jednouzoračni, neovisni i upareni postupak procjenjuju razliku iz
različitih podatkovnih situacija. Isti brojevi obrađeni kao upareni i kao
neovisni mogu dati različitu nesigurnost, pa taj izbor nije tehnički detalj.
Binarna oznaka skupine pokazuje da je koeficijent jednak razlici sredina, ali ne
izjednačuje Welchovu i običnu OLS nesigurnost. Standardizirana razlika pomaže
usporedbi razmjera, ali ne uklanja razlike među skupinama koje s ishodom dolaze
zajedno. Sljedeće poglavlje prelazi na više skupina i uvodi cijenu mnogih
usporedbi.

## Pojmovi

jedinica neovisnosti (*unit of independence*), neovisne skupine (*independent
groups*), upareni podaci (*paired data*), razlika aritmetičkih sredina
(*difference in arithmetic means*), Welchov t-test (*Welch's t-test*), referentna
skupina (*reference category*), standardizirana razlika (*Cohen's d*), ovisnost
opažanja (*dependence among observations*)

## Zadaci

### Konceptualni

Za tri istraživačke situacije imenujte jedinicu neovisnosti i odgovarajući
dizajn. Prva uspoređuje prosječno povjerenje u uzorku s unaprijed zadanim pragom
od pet bodova, druga uspoređuje dvije skupine prema primarnom izvoru vijesti, a
treća mjeri iste ispitanike prije i poslije kampanje.

### Računski

Iz upravljanoga agregata `data/populacija-medija-agregat.csv` uzmite retke za TV
i društvene mreže. Za svaki redak podijelite `zbroj_povjerenja` stupcem `broj`,
provjerite pohranjeni prosjek i izračunajte razliku aritmetičkih sredina. Zatim
pretpostavite jednake standardne devijacije 1,6 pa 3,2 i za obje izračunajte
standardiziranu razliku. Objasnite zašto se prva brojka nije promijenila, a druga
jest. Za rad bez datoteke upotrijebite izvadak iz istoga agregata.

*Slika. Izvadak upravljanoga agregata za obvezni zadatak.*

### Kritički

Vratite se operacionalizaciji iz poglavlja 2 i tumačenju intervala iz poglavlja
9. Za glavni primjer najprije napišite što ljestvica povjerenja i kategorija
izvora vijesti ne mjere. Zatim za isti interval usporedite odluku kojoj je važna
bilo koja pozitivna razlika s odlukom koja traži najmanje dva boda. Predajte
kratku bilješku recenzentu i objasnite zašto sama oznaka značajnosti ne može
riješiti ni problem mjerenja ni izbor praga (Cumming, 2014).

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte referentnu skupinu i objasnite što
bi se promijenilo, a što ostalo isto kada bi se referenca zamijenila. Zatim
provjerite jedinicu neovisnosti, vrstu ishoda, odnos prema varijancama i doseg
ciljne populacije. Izdvojite jedinu tvrdnju koja iz rezultata ne slijedi i
napišite rečenicu kojom bi je trebalo zamijeniti.
