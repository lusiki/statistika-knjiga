# Uspoređivanje više grupa

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Simmons, Nelson i Simonsohn pokazali su kako niz uobičajenih istraživačkih
odluka može dovesti do značajnog rezultata za nemoguću tvrdnju (Simmons, 2011).
Istraživač može birati koji će ishod prikazati, koju podskupinu analizirati i
kada će zaustaviti prikupljanje podataka. Svaki izbor otvara novu mogućnost za
poželjan rezultat.

Pojedinačni testovi pritom mogu biti ispravno izračunati. Problem nastaje kada
izvještaj prikaže samo odabrani nalaz, a prešuti koliko je usporedbi i odluka
do njega dovelo.

Kako usporediti više skupina, uzeti u obzir broj usporedbi i utvrditi gdje su
razlike?

Usporedba televizije i društvenih mreža ostavila je izvan analize korisnike
ostalih izvora vijesti. Ako želimo obuhvatiti sve skupine, mogli bismo
ponavljati postupak iz prethodnog poglavlja za svaki par. No tada više ne
donosimo samo jednu odluku. Moramo razmotriti koliko prilika za lažni nalaz
nastaje kroz sve usporedbe koje ćemo pregledati. Tu ćemo poteškoću najprije
ispitati u simulaciji u kojoj skupine dolaze iz iste raspodjele povjerenja.
Svaku pronađenu razliku tada možemo prepoznati kao lažni nalaz. Povezat ćemo
tu provjeru s onime što smo u poglavlju o krizi i obnovi naučili o odabiru
rezultata. Ovdje je skup usporedbi unaprijed poznat, pa možemo tražiti
postupak koji uvažava cijeli skup odluka.

Za glavnu analizu uzimamo 300 zamišljenih osoba iz `populacija_medija` i
zadržavamo izvor vijesti zadan pri stvaranju podataka (Šikić, 2026). Jedan
redak sadrži osobu, njezin izvor i ocjenu povjerenja. Skupine televizije,
radija, tiska, portala i društvenih mreža zato se sada mogu razlikovati. Ti
rezultati opisuju nastavni skup i služe učenju usporedbe, bez tvrdnje o
stvarnoj publici.

Umjesto jedne razlike sredina sada ispitujemo jesu li sve skupinske sredine
jednake. Razlaganjem varijabilnosti usporedit ćemo razmake među sredinama s
raspršenošću osoba unutar skupina. Iz te ćemo usporedbe razviti analizu
varijance i F-test, uz mjeru veličine učinka. Ukupni nalaz još neće odrediti
koji se parovi razlikuju. Za njih ćemo prikazati procjene i intervale koji
uzimaju u obzir višestruke usporedbe, pa razmotriti i granice pretpostavki.  Tako možemo sastaviti odgovor koji razlikuje ukupni obrazac,
konkretne razlike i nesigurnost svake opravdane usporedbe.

## Cijena mnogih usporedbi

Među pet skupina postoji deset parova. Mogli bismo svaki usporediti zasebnim
testom iz prethodnog poglavlja. Simulacijom ćemo provjeriti koliko često taj
niz testova daje barem jedan lažni nalaz.

Iz poznate simulirane populacije medijskih navika nasumično sastavljamo pet
skupina po četrdeset osoba. Pri tome zanemarujemo njihov izvor vijesti. Sve
skupine nastaju odabirom iz iste raspodjele povjerenja, pa među njima nema
unaprijed zadane razlike. U svakom ponavljanju provodimo deset usporedbi i
bilježimo je li barem jedna značajna. Svako takvo odbacivanje ovdje je
pogrešno. Poslije ćemo se vratiti skupinama prema izvoru vijesti, među kojima
razlike mogu postojati.

Jedno ponavljanje stvara pet skupina po 40 odgovora. Unutar svake skupine
biramo bez vraćanja, ali svaku novu skupinu ponovno izvlačimo iz pune
populacije. Ista osoba zato može biti odabrana u različitim skupinama.
U prvom stvarno izvedenom ponavljanju sredine su
`r paste(hr_broj(vapply(s15_prvo_skupine, mean, numeric(1)), 2), collapse = ", ")`.
Među deset obostranih Welchovih usporedbi najmanja p-vrijednost iznosi
`r hr_broj(min(s15_prvo_p), 3)`, a prag 0,05 prelazi u smjeru odbacivanja
`r sum(s15_prvo_p < 0.05)` usporedbi. Za zbirni rezultat zapisujemo samo
ima li barem jedne takve usporedbe. Dva lažna nalaza u istom ponavljanju
i dalje znače jedno ponavljanje s pogreškom.

Ponovno izvlačimo svih pet skupina 2.000 puta, zadržavajući istu populaciju,
veličine i pravila testiranja. Barem jedan lažni nalaz dobivamo u
`r sum(s15_pod_nultom["barem_jedan", ])` od 2.000 ponavljanja. Svi su
testovi definirani i nijedno ponavljanje nije izostavljeno.

U dvije tisuće ponavljanja barem jedna usporedba bila je značajna u `r hr_broj(s15$stopa_parne)`
% slučajeva. Svaki test koristi prag pet posto, ali cijeli skup daje lažni
nalaz u više od četvrtine ponavljanja. Prikaz samo značajnog para sakrio bi tu
veću stopu pogreške.

**Stopa obiteljske pogreške** je vjerojatnost da će barem jedan test u
unaprijed određenom skupu testova dati lažno pozitivan rezultat, odnosno
pogrešno odbaciti barem jednu istinitu nultu hipotezu.

U našoj su simulaciji sve nulte hipoteze istinite. Kada neke
razlike postoje, pratimo vjerojatnost da pogrešno odbacimo barem jednu od
preostalih istinitih nultih hipoteza.

Postupak koji kontrolira pogrešku samo kada su sve nulte hipoteze istinite
ima slabu kontrolu. Jaka kontrola mora vrijediti i kada dio razlika doista
postoji. Tukeyjev postupak u odgovarajućem normalnom modelu sa zajedničkom
varijancom štiti obitelj parnih usporedbi i u tom drugom slučaju. Primjerice,
ako se samo prva od pet skupina razlikuje od ostalih, ukupni test može lako
odbaciti jednakost svih sredina. Među preostalim četirima ipak postoji šest
usporedbi jednakih populacijskih sredina. Njihovo zasebno testiranje bez
korekcije i dalje otvara mogućnost barem jednoga lažno pozitivnog zaključka.

Za deset neovisnih testova vjerojatnost da nijedan ne pogriješi iznosi
$0,95^{10}$. Suprotni događaj, barem jedna pogreška, zato ima vjerojatnost
$1-0,95^{10}$, približno 0,401.

Za deset neovisnih testova račun daje stopu `r hr_broj(s15$formula_neovisnih)` %. U parnim usporedbama pet skupina ista se opažanja koriste više puta, pa
usporedbe nisu neovisne i u našoj simulaciji daju nižu stopu. Zasebna simulacija deset doista neovisnih usporedbi daje `r hr_broj(s15$stopa_neovisne)`
%, blizu računu.

U zasebnom pokusu svaki od deset testova dobiva svoja dva nova uzorka po
40 osoba, pa testovi više ne dijele iste uzorke. Od 2.000 ponavljanja
`r sum(s15_neovisnih_deset)` sadrži barem jedno odbacivanje, bez isključenih
ponavljanja. Uspoređujemo dvije organizacije testiranja pod nulom, a ne
njihovu snagu. Novi niz izvlačenja dao bi malo drukčije udjele.

Formula za neovisne testove nije opća gornja granica za ovisne usporedbe.
Ipak, oba simulirana skupa daleko prelaze pet posto. Zato uz najmanju
p-vrijednost trebamo znati koliko je usporedbi provedeno i kako su povezane.

Za stopu blizu 5 % uz 2.000 ponavljanja standardna pogreška samoga
simulacijskog postotka iznosi oko 0,49 postotnih bodova. Mala odstupanja od
5 % zato nisu sama po sebi dokaz pogrešno podešena postupka.

Možemo postaviti i jedno ukupno pitanje o jednakosti svih pet sredina. U istoj
simulaciji takav test odbacuje u `r hr_broj(s15$stopa_ukupni)` % slučajeva. Uz dvije tisuće
ponavljanja taj je udio u skladu s planiranih pet posto.

## Varijanca između i unutar

Ukupni test treba prepoznati jesu li razmaci među skupnim sredinama veliki u
odnosu na raspršenost koju već imamo među ljudima. Taj smo odnos susreli pri
usporedbi dviju skupina. Razlika od jednoga boda jače ih statistički razdvaja
kada su osobe unutar skupina slične nego kada su jako raspršene. Sada istu
logiku primjenjujemo na sve skupine zajedno.

Ukupnu varijabilnost zato razdvajamo na odstupanja među skupnim sredinama i
odstupanja pojedinaca unutar skupina. Model sa skupinama opisuje prvi dio, dok
drugi ostaje neobjašnjen.

Da bismo razlaganje vidjeli na manjem prikazu, prelazimo na tri skupine po
24 točke bez stvarne mjerne jedinice. Počinjemo normalnim slučajnim
vrijednostima, ali ih zatim u svakoj skupini centriramo i skaliramo tako da
njihova ostvarena sredina i standardna devijacija budu točno zadane.
To je ilustracija razlaganja, ne ponovljeno uzorkovanje za provjeru testa.
Pri sredinama 46, 52 i 58 zajednička je sredina 52. Skupina A pridonosi
zbroju između skupina s $24(46-52)^2 = 864$. Isti račun radimo za B i C,
dok unutar skupina zbrajamo kvadrate udaljenosti svake od 72 točke od
njezine skupne sredine.

Zbroj između skupina iznosi $864+0+864=1\,728$. Dijeljenjem s
$3-1=2$ dobivamo srednji kvadrat 864. Uz standardnu devijaciju 6,
zbroj unutar skupina iznosi $3\times23\times6^2=2\,484$; nakon dijeljenja
sa $72-3=69$ srednji kvadrat iznosi 36. Omjer je zato $F=864/36=24$.
Srednji kvadrat u nazivniku ima istu mjernu jedinicu kao onaj u brojniku,
pa je F bez mjerne jedinice.

Kad su sve tri sredine 52, zbroj između skupina iznosi nula, zbroj unutar
ostaje $2\,484$ i F je nula. U trećem stanju zbroj između ostaje $1\,728$,
a uz standardnu devijaciju 11 zbroj unutar iznosi
$3\times23\times11^2=8\,349$. Srednji kvadrat unutar skupina tada je 121,
pa je $F=864/121\approx7,14$.

Okomite trake prikazuju udaljenost skupnih sredina od zajedničke sredine.
Točke prikazuju raspršenost osoba oko sredine njihove skupine. Usporedba
stanja pokazuje kako isti razmak sredina izgleda uz različitu raspršenost
unutar skupina.

*Slika. Dekompozicija varijance — skupne sredine, zajednička sredina i raspršenost pojedinačnih opažanja.*

**Što isprobati.**

1. Postavite sve tri sredine na 52 i zadržite standardnu devijaciju 6.
2. Razmaknite sredine na 46, 52 i 58 te usporedite novi omjer s prvim.
3. Zadržite razdvojene sredine i povećajte standardnu devijaciju na 12.

U trećem stanju sredine su iste kao u drugome, ali je raspršenost unutar skupina veća, pa
omjer pada. Uz standardnu devijaciju 11 njegova je vrijednost
$864/121\approx7,14$, umjesto $864/36=24$ uz standardnu devijaciju šest.
Za procjenu odstupanja od nultog modela trebamo oba izvora
varijacije.

## Veličina i F-omjer

Zbroj kvadriranih odstupanja označujemo s $SS$. Dio $SS_{\text{između}}$
sažima odstupanja skupnih sredina od zajedničke, a $SS_{\text{unutar}}$
odstupanja pojedinaca od njihove skupne sredine. Ukupni zbroj
$SS_{\text{ukupno}}$ jednak je zbroju tih dijelova. Udio prvog dijela u
ukupnom pokazuje koliko je varijabilnosti povezano sa skupinama.

**Eta-kvadrat** je udio ukupne varijabilnosti ishoda koji otpada na razlike među
skupnim sredinama.

$$\eta^2 = \frac{SS_{\text{između}}}{SS_{\text{ukupno}}}$$

Sada prelazimo s početne simulacije nasumično sastavljenih skupina na uzorak
iz poznate simulirane populacije medijskih navika. Zadržavamo oznake pet
izvora vijesti zadane pri stvaranju podataka i uspoređujemo povjerenje
njihovih korisnika (Šikić, 2026). Skupine zato mogu imati različite prosjeke
i prije uzorkovanja.

Uzorak od 300 osoba izvukli smo bez vraćanja iz pune populacije, zasebno
od uzorka prethodnog poglavlja. tablica pokazuje broj odgovora i sredinu
koju model pridružuje svakoj osobi iste skupine.

*Slika. Pet skupina u glavnom uzorku od 300 osoba. Izrada autora.*

Prva uzorkovana osoba navodi `r as.character(pet_izvora$izvor_vijesti[1])`
i povjerenje `r pet_izvora$povjerenje_medijima[1]`. Njezina skupna sredina
je `r hr_broj(fitted(s15_model)[1], 3)`, pa u zbroj unutar skupina ulazi
$(`r pet_izvora$povjerenje_medijima[1]` - `r hr_broj(fitted(s15_model)[1], 3)`)^2$.
Za zbroj između skupina kvadriramo razliku svake skupne i zajedničke sredine
te je množimo brojem osoba u toj skupini. Tako dobivamo
`r hr_broj(s15$ss_izmedu, 2)` između i `r hr_broj(s15$ss_unutar, 2)` unutar.
Njihov zbroj, `r hr_broj(s15$ss_izmedu + s15$ss_unutar, 2)`, nazivnik je
eta-kvadrata. Svih 300 odgovora ulazi u oba opisa.

U našem uzorku eta-kvadrat iznosi `r hr_broj(s15$eta2, 3)`. Razlike među izvorima vijesti
opisuju oko `r hr_broj(s15$eta2 * 100, 0)` % varijabilnosti povjerenja. Većina razlika među ljudima
ostaje izvan modela. Za tu mjeru ovdje ne prikazujemo interval, pa njezina uzoračka nesigurnost nije kvantificirana.

Je li takav udio važan, ovisi o pitanju. Može biti koristan za razumijevanje
društvenog stava, a nedovoljan za precizno predviđanje pojedinca. Procjenu
zato povezujemo s ranijim nalazima i unaprijed obrazloženim najmanjim važnim
učinkom.

Eta-kvadrat opisao je koliki dio ukupne varijabilnosti otpada na razlike među
skupinama. Za test jednakosti sredina trebamo još usporediti raspršenost između
skupina s onom koja ostaje unutar njih. Sirove zbrojeve zato najprije
pretvaramo u usporedive srednje kvadrate. Za $k$ skupina i
$n$ opažanja dijelimo $SS_{\text{između}}$ s $k - 1$, a
$SS_{\text{unutar}}$ s $n - k$. Ti djelitelji predstavljaju stupnjeve
slobode. Dobivamo $MS_{\text{između}}$ i $MS_{\text{unutar}}$, gdje $MS$
označuje prosječnu kvadriranu raspršenost.

**F-statistika** je omjer prosječne raspršenosti među skupnim sredinama i
prosječne raspršenosti opažanja oko njihovih skupnih sredina.

$$F = \frac{MS_{\text{između}}}{MS_{\text{unutar}}}$$

Pod nultim modelom jednakih populacijskih sredina i zajedničke
varijance, uz neovisna opažanja, oba srednja kvadrata procjenjuju tu varijancu, pa se njihov omjer F obično nalazi blizu jedinice. Stupnjevi
slobode $k - 1$ i $n - k$ određuju referentnu F-raspodjelu. Veći omjer daje
više razloga za preispitivanje jednakosti sredina.

Referentna F-raspodjela opisuje koje bismo omjere dobivali pod tim nultim
modelom uz normalne pogreške. Njezina dva parametra ovdje iznose
`r s15$df1` i `r s15$df2`. Gornjih 5 % raspodjele počinje kod
`r hr_broj(qf(0.95, s15$df1, s15$df2), 2)`, dok naš opaženi omjer iznosi
`r hr_broj(s15$f, 2)`. Tu usporedbu koristimo za test; veličinu i važnost
razlika i dalje čitamo iz sredina, eta-kvadrata i intervala.

Postupak se zove analiza varijance jer uspoređuje izvore varijabilnosti. Njime
ipak ispitujemo pitanje o jednakosti skupnih sredina.

## Isti model, više koeficijenata

U prethodnom poglavlju binarna oznaka skupine imala je jedan koeficijent
razlike. Za pet skupina trebamo četiri takva koeficijenta. Jedna skupina
ostaje referentna, a ostale uspoređujemo s njom. U našem je računu to portal.

Pokazatelji $x_1$ do $x_4$ označuju četiri nereferentne skupine. Svaki ima
vrijednost jedan za svoju skupinu i nula za ostale. Koeficijent $\beta_0$ daje
sredinu reference, a koeficijenti $\beta_1$ do $\beta_4$ razlike prema njoj.
Populacijska pogreška $\varepsilon$ opisuje odstupanje od modelne
skupne sredine. Nakon prilagodbe opaženo odstupanje zovemo rezidualom.

$$\text{povjerenje} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 +
\beta_4 x_4 + \varepsilon$$

Svaka osoba pripada samo jednoj skupini. Pet koeficijenata tako opisuje pet
skupnih sredina.

Klasični ukupni test zajednički ispituje četiri koeficijenta razlike.
Uspoređuje model sa skupnim sredinama i model sa samo jednom zajedničkom
sredinom. To je jedno globalno pitanje, različito od deset zasebnih parnih
usporedbi.

Klasični i Welchov postupak koriste iste točkaste procjene sredina, ali
drukčije računaju nesigurnost. Klasična analiza varijance, kao obični
homoskedastični linearni model, procjenjuje zajedničku rezidualnu varijancu.
Welch zadržava zasebne skupne varijance i prilagođava stupnjeve slobode. Zato
intervali i p-vrijednosti ne moraju biti jednaki.

Taj model sada primjenjujemo na pojedinačne zapise iz skupa `populacija_medija`.
Svakoj osobi pridružujemo sredinu njezina izvora vijesti, pa odstupanja oko tih
pet sredina uspoređujemo s odstupanjima oko jedne zajedničke sredine.

Uzorak od `r s15$n` osoba dijelimo prema pet izvora vijesti. Ukupni test daje
F od `r hr_broj(s15$f, 2)`, uz `r s15$df1` i `r s15$df2` stupnjeva slobode te p-vrijednost
manju od 0,001. Srednji kvadrat između skupina iznosi `r hr_broj(s15$ms_izmedu, 1)`, a unutar njih
`r hr_broj(s15$ms_unutar, 1)`. Opaženi rezultat teško se uklapa u pretpostavku jednakih populacijskih
sredina. Još trebamo procijeniti pojedine razlike i njihovu nesigurnost.

Ljudi sami biraju izvor vijesti, pa se skupine mogu razlikovati i po drugim
obilježjima. Model opisuje njihove razlike u povjerenju, ali ne utvrđuje
učinak izbora izvora.

Oblik razlika provjeravamo na samim odgovorima. Kutije prikazuju srednjih
50 % vrijednosti, vodoravna crta medijan, a točke pojedinačne odgovore.
Raspršenost i preklapanje ostaju vidljivi uz razlike sredina.

*Slika. Povjerenje po glavnom izvoru vijesti u istom nastavnom uzorku. Izrada autora prema simuliranom skupu @sikic2026.*

## Nakon ukupnog testa

Ukupni test ne govori koje se skupine razlikuju, za koliko i u kojem smjeru.
Nije ni obvezan uvjet za provođenje unaprijed planirane usporedbe. Za
sadržajni odgovor trebamo pojedine procjene s intervalima i jasan popis
pitanja koja smo postavili.

Usporedbu određenu prije pregleda rezultata zovemo **planirana usporedba**. Za
naknadne usporedbe navodimo **post-hoc postupak** i obitelj pitanja koju
štiti. Tukeyjev postupak u klasičnom modelu sa zajedničkom rezidualnom
varijancom obuhvaća sve parove. Daje istodobne intervale koji u toj obitelji
kontroliraju stopu pogreške.

Zašto tim razlikama pridružujemo šire intervale nego jednoj zasebnoj usporedbi?
Promatramo ih više, pa najveća među deset razlika može biti velika i kada
nijednu nismo unaprijed odabrali. Tukeyjev račun uzima u obzir taj izbor
koristeći raspodjelu raspona među skupnim sredinama. Širina istodobnih
intervala zato ovisi o broju skupina i povezanosti usporedbi.

Za jedan par sada oduzmemo dvije sredine iz tablice. Razlici televizije
prema mrežama pridružujemo marginu `r hr_broj((s15$tv_mreze_gornja - s15$tv_mreze_donja)/2, 2)`
boda, izračunatu zajedničkom rezidualnom varijancom, brojnostima tih dviju
skupina i Tukeyjevim pravilom za svih pet skupina. Oduzimanjem i dodavanjem
te margine nastaju granice intervala. Svih deset usporedbi koristi iste
izvorne odgovore, a ne deset novih uzoraka.

Među `r s15$parova` parova statistički su razlučive četiri usporedbe s društvenim
mrežama. Televizija se od njih razlikuje za `r hr_broj(s15$tv_mreze, 2)` boda, uz istodobni
95-postotni interval od `r hr_broj(s15$tv_mreze_donja, 2)` do `r hr_broj(s15$tv_mreze_gornja, 2)`. Razlika tiska prema televiziji
iznosi `r hr_broj(s15$tv_tisak, 2)` boda, uz interval od `r hr_broj(s15$tv_tisak_donja, 2)` do `r hr_broj(s15$tv_tisak_gornja, 2)`. Taj par ovim
uzorkom ne razlučujemo.

Na zajedničkoj osi možemo pregledati svih deset razlika. U nazivu para
prvu skupinu uspoređujemo s drugom, pa pozitivna vrijednost znači višu
sredinu prve skupine. Crte su istodobni 95-postotni Tukeyjevi intervali;
okomita crta označuje izostanak razlike.

*Slika. Svih deset parnih razlika iz istoga modela, uz istodobne intervale. Izrada autora.*

Interval za televiziju i tisak širok je više od dva boda. Takav rezultat ne
pokazuje da su skupine jednake. Pokazuje da procjena nije dovoljno precizna za
razlučivanje razlike od nule.

Ako nas unaprijed zanima određena usporedba, primjerice tradicionalnih i
digitalnih izvora, možemo je izravno planirati. Tada ne štitimo obitelj od
deset naknadno odabranih parova. Interval može biti uži, ali samo ako je
pitanje doista određeno prije pregleda sredina. Naknadni izbor ne smijemo
prikazati kao unaprijed planiran.

## Granice pretpostavki

Najprije provjeravamo neovisnost jedinica. Ponovljena mjerenja istih ljudi i
zajedničko kućanstvo, razred, škola, grad, organizacija ili mrežna veza mogu
stvarati ovisnost. Obični klasični, Welchov i rangovni postupak takvu
strukturu ne rješavaju. Modeli za ponovljene i ugniježđene podatke prelaze
opseg knjige.

Zatim pregledavamo ostatke i skupne raspršenosti. Pretpostavka približne
normalnosti odnosi se na ostatke. Klasična inačica pretpostavlja jednake
varijance, što trebamo procijeniti iz više informacija, a ne iz jednog
pokazatelja.

Omjer najveće i najmanje skupne varijance iznosi `r hr_broj(s15$var_omjer, 2)`. Koristimo ga kao
orijentir uz grafove, veličine skupina i način nastanka podataka. Sam ne
potvrđuje valjanost klasičnog testa. Ako nejednake varijance izgledaju
uvjerljivo, Welchov ukupni test zadržava njihove zasebne procjene.

Welchov test daje F od `r hr_broj(s15$welch_f, 2)`, uz četiri stupnja slobode u brojniku i `r hr_broj(s15$welch_df2, 1)` u nazivniku.
Procijenjene sredine i razlike ostaju iste. Provjerili smo osjetljivost
ukupnog zaključka na račun nesigurnosti, ali time nismo dokazali jednake
varijance ni opravdali Tukeyjeve intervale. Ako varijance nisu jednake, za
parove možemo provesti Welchove usporedbe uz Bonferronijevu korekciju. Svaku uspoređujemo s pragom 0,05 podijeljenim brojem planiranih parova. To je zasebno od Tukeyjeva postupka.

Kruskal-Wallisov postupak rangira vrijednosti i uspoređuje raspodjele rangova.
Utjecaj krajnjeg opažanja zato više ne ovisi izravno o njegovoj brojčanoj
udaljenosti, ali postupak i dalje ima pretpostavke i ispituje drugo pitanje. U našem uzorku
statistika iznosi `r hr_broj(s15$kw, 1)`. Uspoređujemo je s približnom
hi-kvadrat raspodjelom uz `r s15_k - 1` stupnjeva slobode, jedan manje od
broja skupina. Na razini 0,05 kritična vrijednost te hi-kvadrat raspodjele iznosi
`r hr_broj(qchisq(0.95, s15_k - 1), 2)`. To nije F-raspodjela s dvama
brojevima stupnjeva slobode.
Za tumačenje razlike u položaju potrebni su usporedivi oblici raspodjela.
Rangiranje također ne uklanja ovisnost redaka.

**Statistika u divljini.**
**Značajno ovdje, neznačajno ondje.** Pretpostavimo da istražujemo
program pomoći pri učenju u dvjema dobnim skupinama. U svakoj
uspoređujemo sudionike programa s odgovarajućom kontrolnom
skupinom. Prvi rezultat označen je kao značajan, a drugi
nije. U sažetku zato napišemo da program djeluje samo na
mlađe i predložimo da se ubuduće nudi samo njima. Ta je
odluka ovdje zamišljena, ali pogreška na kojoj počiva
dokumentirana je u istraživačkoj literaturi.

Nieuwenhuis, Forstmann i Wagenmakers pregledali su 513 neuroznanstvenih
radova iz pet vodećih časopisa. Među njima su
pronašli 78 koji su izravno testirali razliku dvaju učinaka
i 79 koji su je zaključili iz toga što je jedan učinak bio
značajan, a drugi nije (Nieuwenhuis, 2011). Zasebni testovi
odgovaraju razlikuje li se svaki učinak od svoje nulte
vrijednosti. Ne odgovaraju razlikuju li se učinci međusobno.

U našem bi primjeru procjene koristi programa mogle biti
slične, dok bi jedna imala širi interval zbog manjeg uzorka
ili veće raspršenosti. Tada bi različite oznake značajnosti
odražavale različitu preciznost, a ne dokaz da dob mijenja
korist programa. Kad bismo prema tim oznakama suzili
buduću primjenu, sadržajnu bismo odluku oslonili na
usporedbu koja još nije provedena.

Potrebno je izravno procijeniti razliku između dvaju učinaka i njezinu
nesigurnost. Kao i pri razlikovanju ukupnog testa od pojedinačnih usporedbi,
prvo određujemo koju razliku tvrdnja traži. Pritom treba opravdati nacrt
unutar svake dobne skupine. Dodatni račun ne može nadoknaditi loše
osmišljenu usporedbu.

Ako je interval razlike učinaka širok, možda još ne
možemo odlučiti treba li program prilagoditi dobi. To
je korisnije znati nego jednu skupinu proglasiti
neprikladnom za program. Razlika između dviju oznaka
značajnosti može biti povod za pitanje, ali odgovor
traži procjenu razlike o kojoj stvarno odlučujemo.

**Nađite grešku.**
Nakon ukupnog testa razlika u povjerenju među korisnicima pet izvora
vijesti tim želi pregledati sve parove. Podaci su iz poznate simulacije
(Šikić, 2026). U ovoj nastavnoj provjeri pretpostavke o neovisnosti,
raspodjelama i jednakim varijancama smatramo zadovoljenima. Zadatak je
procijeniti postupak donošenja odluka o parovima.

Asistent je pripremio ovaj zapis, koji treba čitati, a ne izvršavati.

> ```r
> model <- aov(povjerenje_medijima ~ izvor_vijesti,
             data = pet_izvora)
> pairwise.t.test(
>   pet_izvora$povjerenje_medijima,
>   pet_izvora$izvor_vijesti,
>   p.adjust.method = "none"
> )
> ```

> Ukupni test ispituje jesu li sve skupne sredine jednake. S pet
> skupina imamo deset parova. Nakon značajnog ukupnog testa svaki par
> možemo prosuditi na razini 0,05 bez prilagodbe, a da vjerojatnost barem
> jedne pogrešne tvrdnje o parovima ostane zaštićena na toj razini.

Odvojite pitanje ukupnog testa od pitanja pojedinačnih parova. Navedite
koju tvrdnju o zaštiti treba popraviti i predložite postupak iz poglavlja
kojim bi tim izvijestio parne razlike uz odgovarajuću nesigurnost.
Sačuvajte ispravno određene skupine i broj usporedbi. Ne pišite zamjenski kod.

## Razrađeni primjer

U povjerenju korisnika pet izvora vijesti želimo razdvojiti dva pitanja. Prvo
se odnosi na ukupan obrazac skupnih sredina, a drugo na veličinu konkretnih
razlika među izvorima. Najprije ćemo prikazati veličinu učinka i ukupni test, a
zatim parne razlike s istodobnim intervalima. Tako će uz svaku usporedbu ostati
vidljivo da je dio šireg skupa odluka.

Račun počinje modelom skupnih sredina. Poziv `aov` procjenjuje isti
model kao `lm`, ali prikazuje razlaganje varijance iz kojega prvo
računamo eta-kvadrat. Uobičajeni F-test zatim uspoređuje srednje kvadrate uz
pretpostavku zajedničke rezidualne varijance. Pod istom pretpostavkom
`TukeyHSD` daje parne razlike, istodobne intervale i korigirane
p-vrijednosti. Zato te rezultate čitamo kao klasičnu analizu, uz ranije
objašnjenu razliku prema Welchovu postupku.

Zbrojevi kvadrata `r hr_broj(s15$ss_izmedu, 1)` između skupina i `r hr_broj(s15$ss_unutar, 1)` unutar njih daju
opisani udio varijabilnosti. F-test provjerava ukupno odstupanje od jednakih
sredina. Na prethodnom prikazu parova vidimo da se društvene mreže odvajaju od svakog
preostalog izvora, dok ostale parove ne razlučujemo.

U izvještaju možemo navesti da skupine u simuliranom uzorku opisuju oko
desetinu varijabilnosti, uz napomenu da nesigurnost toga udjela ovdje nije
procijenjena. Razlika televizije i društvenih mreža iznosi oko 1,59 bodova na
ljestvici od deset, uz istodobni 95-postotni interval približno od 0,71 do
2,46. Sve četiri usporedbe s društvenim mrežama razlučive su pod
pretpostavkama prikazanog postupka. Podaci ipak ne opravdavaju uzročni
zaključak.

## Sažetak

Kada usporedbu proširimo na više skupina, trebamo pratiti i veću mogućnost
barem jednoga lažnog nalaza. Razlaganje varijabilnosti između skupina i unutar
njih omogućuje jedno ukupno pitanje o jednakosti sredina, na koje odgovara
F-test. Eta-kvadrat opisuje udio varijabilnosti povezan sa skupinama, uz
ograničenje da njegovu uzoračku nesigurnost u ovom primjeru nismo
kvantificirali. Za odgovor o konkretnoj razlici ipak trebamo planiranu
usporedbu ili imenovani post-hoc postupak s odgovarajućim intervalima. Njihove
pretpostavke procjenjujemo prema nacrtu, grafovima i skupnim podacima, a za
ovisna opažanja trebamo drukčiji postupak. Dosad je model povezivao povjerenje
s oznakom skupine, dok ćemo ga u sljedećem poglavlju proširiti na brojčane
prediktore i više varijabli zajedno.

## Pojmovi

Tukeyjev postupak (*Tukey HSD*), Kruskal-Wallisov postupak (*Kruskal-Wallis test*),
analiza varijance (*analysis of variance*), stopa obiteljske pogreške
(*familywise error rate*), F-statistika (*F-statistic*), planirana usporedba
(*planned comparison*), post-hoc postupak (*post-hoc procedure*), eta-kvadrat
(*eta squared*), varijanca između skupina (*between-group variance*), varijanca
unutar skupina (*within-group variance*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Skicirajte tri skupne sredine i raspršenosti uz koje bi ukupni test bio značajan,
a samo jedan par razlučiv. Zatim pretpostavite da ste taj par odabrali tek nakon
pregleda svih sredina. Odredite je li usporedba planirana ili post-hoc, imenujte
obitelj koju treba zaštititi i objasnite zašto je ne smijete prikazati kao jedno
unaprijed postavljeno pitanje.

### Računski

Razlaganje daje 120 na razlike među četirima skupinama i 480 na razlike unutar
njih, uz ukupno sto opažanja. Izračunajte obje prosječne raspršenosti, njihov
omjer i eta-kvadrat. Objasnite što bi se s omjerom dogodilo da je drugi broj
dvostruko veći.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi razlike između opisne i uzročne
tvrdnje te poglavlju o veličini učinka i snazi radi najmanjega važnog učinka. U
agregiranoj tablici `data/populacija-medija-agregat.csv` pronađite retke za TV
i društvene mreže.
Prije računanja zapišite najmanju razliku na ljestvici od 1 do 10 koju biste
smatrali sadržajno važnom. Izračunajte populacijsku razliku iz stupaca
`zbroj_povjerenja` i `broj`, usporedite je sa svojim pragom i objasnite zašto
rezultat ne dokazuje da odabir izvora uzrokuje povjerenje.

### Revizija modela

Ocijenite postupak i obrazloženje iz okvira. Imenujte jedinu pogrešku,
odredite koju stopu pogreške ugrožava i razdvojite taj prigovor od dijelova
analize koji su još korisni. Predložite način izvještavanja parnih razlika
koji odgovara cijeloj obitelji usporedbi. Ne pokrećite kod i ne pišite
njegovu zamjenu.
