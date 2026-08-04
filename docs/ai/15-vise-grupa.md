# Uspoređivanje više grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Dekompozicija varijance | simulirana populacija | pogl. 10, 14 |

**Vinjeta.**
Simmons, Nelson i Simonsohn pokazali su da istraživač koji tijekom analize
donosi naizgled bezazlene odluke može doći do statistički značajnog rezultata za
tvrdnju koja ne može biti istinita (Simmons, 2011). Odluke su bile obične, poput
toga koji će ishod izvijestiti, koju će podskupinu pogledati i kada će prestati
prikupljati podatke.

Nijedan pojedinačni test u tom postupku nije bio pogrešno proveden. Problem je
nastao od njihova broja, jer je svaka nova usporedba bila nova prilika da
slučajnost proizvede rezultat vrijedan objave. Broj prilika nije se nigdje
vidio u izvještaju.

Kako više skupina usporediti tako da broj prilika ostane vidljiv, a zatim
utvrditi gdje se razlike zapravo nalaze?

## Cijena mnogih usporedbi

Pet skupina daje deset parova. Očit postupak jest provesti deset usporedbi iz
prethodnog poglavlja i pogledati koje su prošle prag. Prije nego što ga
odbacimo, vrijedi izmjeriti koliko taj postupak zapravo košta, i to na način na
koji je knjiga to radila i za uzorkovanje i za kategoričke podatke.

Postavljamo situaciju u kojoj razlike po konstrukciji nema. Iz iste simulirane
populacije izvučemo pet skupina po četrdeset osoba, dakle skupine koje se ne
razlikuju ni po čemu osim po tome koga je slučaj u njih smjestio. Zatim
provedemo svih deset usporedbi i zabilježimo je li barem jedna prošla prag. Sve
što nađemo je pogreška.

Kroz dvije tisuće ponavljanja barem jedna od deset usporedbi bila je značajna u
`r hr_broj(s15$stopa_parne)` % slučajeva. Postupak koji je zamišljen da griješi
u pet posto slučajeva griješi u više od četvrtine njih, a izvještaj bi u svakom
od tih slučajeva sadržavao uredno provedenu usporedbu s malom p-vrijednošću.

**Stopa obiteljske pogreške** je vjerojatnost da će barem jedan test u
unaprijed određenom skupu testova dati lažno pozitivan rezultat, uz uvjet da u
tom skupu nijedan učinak zaista ne postoji.

Uobičajena formula za tu stopu množi vjerojatnosti neuspjeha svih testova i za
deset testova daje `r hr_broj(s15$formula_neovisnih)` %. Naša izmjerena
vrijednost osjetno je niža, i razlog je vrijedan pažnje. Formula pretpostavlja
da su testovi neovisni, a deset parnih usporedbi među pet skupina dijeli
skupine, pa nisu. Ista simulacija s deset zaista neovisnih usporedbi daje
`r hr_broj(s15$stopa_neovisne)` %, dakle upravo ono što formula predviđa.

Poučak je da formula opisuje gornju granicu, a ne stopu koju parne usporedbe
doista imaju. Obje su brojke daleko iznad pet posto i obje vode istom
zaključku, ali brojku koja se navodi u izvještaju vrijedi izmjeriti umjesto
prepisati.

Postoji i postupak koji cijeli skup pitanja rješava jednim testom. Kad istu
simulaciju provedemo tako da svih pet skupina uđe u jedan zajednički model, on
griješi u `r hr_broj(s15$stopa_ukupni)` % slučajeva, dakle onoliko koliko je i
obećao. Taj postupak razvija ostatak poglavlja.

## Varijanca između i unutar

Zajednički test za više skupina mora nekako sažeti razlike među njima u jednu
brojku. Prva ideja bila bi zbrojiti udaljenosti skupnih sredina od zajedničke
sredine, ali takav zbroj sam po sebi ništa ne znači. Tri sredine razmaknute za
jedan bod velika su razlika ako su ljudi unutar skupina zbijeni, a gotovo ništa
ako su raspršeni preko cijele ljestvice.

Usporedba mora zato ići prema drugoj vrsti raspršenosti. Ukupno rasipanje
podataka razlaže se na dio koji potječe od razlika među skupinama i dio koji
potječe od razlika među pojedincima unutar iste skupine. Prvi dio je ono što
model objašnjava, drugi je ono što ostaje.

Kad se svaki od tih dvaju dijelova podijeli brojem veličina koje su ga mogle
proizvesti, dobiju se dvije prosječne raspršenosti koje se mogu staviti u omjer.
Ako skupine nemaju nikakvog učinka, obje mjere istu slučajnost i omjer se vrti
oko jedinice. Ako skupine imaju učinka, brojnik raste, a nazivnik ne.

**F-statistika** je omjer prosječne raspršenosti među skupnim sredinama i
prosječne raspršenosti opažanja oko njihovih skupnih sredina.

$$F = \frac{MS_{\text{između}}}{MS_{\text{unutar}}}$$

Oznaka $MS$ stoji za zbroj kvadriranih odstupanja podijeljen pripadnim
stupnjevima slobode.

Naziv analiza varijance zbog toga zvuči kao da je riječ o raspršenosti, a
pitanje je o sredinama. Raspršenost je ovdje mjerilo, ne predmet. Postupak je i
dalje usporedba skupnih sredina, samo izražena u jedinicama koje su za tu
usporedbu prikladne.

## Interakcija — Dekompozicija varijance

Sljedeći prikaz razdvaja dva izvora rasipanja koje ukupni graf spaja. Okomite
trake pokazuju koliko je svaka skupna sredina udaljena od zajedničke, a točke
koliko su pojedinci raspršeni oko svoje skupne sredine. Čitatelj pomiče sredine
i raspršenost odvojeno, pa se vidi da razmak među skupinama sam po sebi ne
određuje ništa.

*Slika. Dekompozicija varijance — skupne sredine, zajednička sredina i raspršenost pojedinačnih opažanja.*

**Što isprobati.**

1. Postavite sve tri sredine na 52 i zadržite standardnu devijaciju 6.
2. Razmaknite sredine na 46, 52 i 58 te usporedite novi omjer s prvim.
3. Zadržite razdvojene sredine i povećajte standardnu devijaciju na 12.

Treći korak ne mijenja nijednu skupnu sredinu, a omjer svejedno pada. Razmak
među skupinama nije, dakle, veličina koja odlučuje. Odlučuje njegov odnos prema
raspršenosti unutar skupina, jer upravo ona kaže koliko bi razmaka slučaj mogao
proizvesti sam od sebe.

## Isti model, više koeficijenata

Prethodno poglavlje zapisalo je usporedbu dviju skupina kao model s jednim
koeficijentom uz binarni prediktor. Prijelaz na pet skupina ne traži novi okvir
nego više koeficijenata u istome. Jedna kategorija ostaje referentna, a svaka od
preostalih dobiva svoj broj koji kaže koliko se od nje razlikuje.

$$\text{povjerenje} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 +
\beta_4 x_4 + \varepsilon$$

Svaka od varijabli $x_1$ do $x_4$ poprima vrijednost jedan za jednu od
nereferentnih skupina i nulu inače, pa svaka osoba aktivira najviše jedan
koeficijent. Oznaka $\beta_0$ i dalje je sredina referentne skupine, a
$\varepsilon$ ono što model o pojedincu nije objasnio. Pet sredina zapisano je s
pet brojeva, kao što je i moralo biti.

Klasični ukupni test iz prošlog odjeljka postavlja pitanje o svim tim
koeficijentima odjednom. Pita jesu li oni zajedno dovoljno veliki da bi model
sa skupinama opisivao podatke bolje nego model koji ima samo zajedničku sredinu.
Zato je jedan test, a ne deset.

Zajednički su oblik modela sredina i njegove točkaste procjene, ne svaki način
računanja njihove nesigurnosti. Klasična analiza varijance procjenjuje jednu
zajedničku rezidualnu varijancu, kao obični homoskedastični linearni model.
Welchov ukupni test zadržava zasebne skupne varijance i prilagođava stupnjeve
slobode, pa istu hipotezu o sredinama ispituje drugim inferencijskim postupkom.

Naš uzorak od `r s15$n` osoba raspoređen je u pet skupina prema izvoru vijesti.
Klasični ukupni test daje F od `r hr_broj(s15$f, 2)` uz `r s15$df1` i
`r s15$df2` stupnjeva slobode. Prosječna raspršenost među skupinama iznosi
`r hr_broj(s15$ms_izmedu, 1)`, a unutar skupina `r hr_broj(s15$ms_unutar, 1)`,
i njihov je omjer upravo ta F-vrijednost.

Model pritom ostaje ono što je bio u prethodnom poglavlju. Ne zna kako su ljudi
u skupine dospjeli i ne tvrdi ništa o uzroku. Izvor vijesti u ovoj populaciji
ljudi biraju sami, pa razlike među skupinama uključuju i sve ono po čemu se ti
ljudi inače razlikuju.

## Što ukupni test ne kaže

Značajan ukupni test kaže da model sa skupinama opisuje podatke bolje od
modela bez njih. Ne kaže koje se skupine razlikuju, koliko, ni u kojem smjeru.
Izvještaj koji na njemu stane predao je jednu bitnu informaciju i nijednu
upotrebljivu.

Postupak koji odgovara na to pitanje mora usporediti parove, ali sada uz
svijest o njihovu broju. Tukeyjev postupak upravo to radi. Uspoređuje sve
parove i pritom širi intervale tako da vjerojatnost barem jedne pogreške u
cijelom skupu usporedbi ostane na obećanoj razini.

Način na koji ih širi vrijedi razumjeti, jer objašnjava zašto korekcija nije
proizvoljna kazna. Kad se gleda deset razlika, ne odlučuje nijedna pojedinačno
nego najveća među njima, a najveća od deset slučajnih veličina sustavno je veća
od bilo koje pojedinačne. Postupak zato ne pita koliko je vjerojatna ova
razlika, nego koliko je vjerojatan ovako velik raspon među pet sredina.
Odgovor na to drugo pitanje daje širi interval, i to točno onoliko širi koliko
je bilo prilika.

Od `r s15$parova` parova u našem uzorku značajno se razlikuju samo oni u kojima
sudjeluju društvene mreže. One se odvajaju od sva četiri preostala izvora, a ta
četiri međusobno ne. Najveća razlika dijeli televiziju od društvenih mreža i
iznosi `r hr_broj(s15$tv_mreze, 2)` boda. Televizija i tisak ostaju nerazlučivi,
s razlikom od `r hr_broj(s15$tv_tisak, 2)` boda i intervalom od
`r hr_broj(s15$tv_tisak_donja, 2)` do `r hr_broj(s15$tv_tisak_gornja, 2)`.

Taj drugi rezultat treba pročitati oprezno. Interval je širok više od dva boda,
pa nije riječ o tome da su dva izvora izjednačena, nego o tome da ih ovaj uzorak
ne razlučuje. Odsutnost razlike i odsutnost dokaza o razlici dvije su različite
tvrdnje, a Tukeyjev ispis ih ne razlikuje umjesto nas.

Postoji i bolji postupak od uspoređivanja svega sa svime. Ako se prije podataka
zna koja usporedba nosi istraživačko pitanje, recimo ona između tradicionalnih i
digitalnih izvora, ona se može postaviti kao jedna planirana usporedba. Jedno
pitanje umjesto deset znači i užu korekciju i veću sposobnost da se razlika
uoči. Uvjet je da je pitanje postavljeno prije, a ne odabrano nakon pogleda na
sredine.

**Statistika u divljini.**
**Značajno ovdje, neznačajno ondje.** Uobičajen način da se dva učinka
usporede jest pogledati je li prvi značajan, a drugi nije, i iz toga zaključiti
da se razlikuju. Nieuwenhuis, Forstmann i Wagenmakers pregledali su 513 radova
iz pet vodećih neuroznanstvenih časopisa i našli 78 radova koji su razliku
dvaju učinaka testirali izravno i 79 radova koji su je izveli iz usporedbe
dviju oznaka značajnosti (Nieuwenhuis, 2011).

Postupak je pogrešan jer prag nije linearan. Učinak s p-vrijednošću tik ispod
praga i učinak s p-vrijednošću tik iznad njega gotovo su jednaki, a dobivaju
suprotne oznake. Usporedba dvaju učinaka zahtijeva test o njihovoj razlici, što
je upravo ono što Tukeyjev postupak i planirane usporedbe rade, a čitanje dviju
zvjezdica jedne pored druge ne radi.

**Pitajte model.**
Asistent će na zahtjev za usporedbom više skupina gotovo uvijek ponuditi ukupni
test i odmah za njim sve parne usporedbe, jer je to najčešći obrazac u kodu na
kojem je učio. Provjeravamo je li referentna skupina ona koju smo htjeli, koliko
je usporedbi zapravo provedeno i je li korekcija imenovana. Provjeravamo i
opisuje li ispis nesignifikantne parove kao jednake, jer je to najčešća
rečenica koju sam doda.

> Reci koja je skupina referentna i koliko usporedbi provodiš. Prikaži skupne
> raspodjele, procijeni zajednički model, navedi veličinu učinka, a parne
> razlike daj s intervalima i imenovanom korekcijom.

**Nađite grešku.**
Ukupni test pokazuje da model sa skupinama opisuje podatke bolje od modela bez
njih, a raspodjela ostataka ne otkriva ozbiljan problem. Veličina učinka
izračunata je i iznosi otprilike deset posto objašnjene varijabilnosti.
Zaključak izvještaja glasi da se svih pet izvora međusobno razlikuje po
percipiranoj vjerodostojnosti.

## Koliki je udio objašnjen

Ukupni test opet ovisi o veličini uzorka, pa uz njega ide mjera koja o njoj ne
ovisi. Prirodna mjera ovdje već postoji u samoj dekompoziciji. Ako je ukupno
rasipanje razloženo na dio među skupinama i dio unutar njih, onda je udio prvoga
u ukupnome mjera koliko je skupna pripadnost objasnila.

**Eta-kvadrat** je udio ukupne varijabilnosti ishoda koji otpada na razlike među
skupnim sredinama.

$$\eta^2 = \frac{SS_{\text{između}}}{SS_{\text{ukupno}}}$$

Za naš uzorak eta-kvadrat iznosi `r hr_broj(s15$eta2, 3)`, dakle izvor vijesti
objašnjava oko `r hr_broj(s15$eta2 * 100, 0)` % varijabilnosti u povjerenju.
Preostalih devedeset posto otpada na razlike među ljudima koje ovaj model uopće
ne vidi, i ta je asimetrija tipična za istraživanja u društvenim znanostima.

Mjera ima jedan poznat nedostatak. Računa se iz istog uzorka iz kojeg su
procijenjene i sredine, pa sustavno precjenjuje udio koji bi se našao u
populaciji. **Omega-kvadrat** ispravlja taj pomak oduzimanjem onoga što bi se od
razlika među skupinama očekivalo i kad ih ne bi bilo. Za naš uzorak iznosi
`r hr_broj(s15$omega2, 3)`, dakle nešto manje od eta-kvadrata, a razlika među
njima pada kako skupine rastu.

Ni jedna ni druga mjera ne govori je li udio velik u sadržajnom smislu. Deset
posto objašnjene varijabilnosti mnogo je za pojedinačni prediktor stava, a malo
za instrument koji bi trebao predviđati pojedinačno ponašanje. Odgovor dolazi iz
usporedbe s drugim nalazima u istom području, ne iz tablice pragova.

## Kad pretpostavke popuste

Zajednički model počiva na istim trima pretpostavkama kao usporedba dviju
skupina, i redoslijed njihove ozbiljnosti je isti. Neovisnost opažanja dolazi iz
dizajna. Približna normalnost odnosi se na raspodjelu ostataka, dakle na ono što
model nije objasnio, a ne na raspodjelu ishoda unutar svake skupine posebno.
Jednakost varijanci potrebna je klasičnoj inačici.

Homogenost se provjerava usporedbom raspršenosti skupina, a najjednostavnija
provjera jest omjer najveće i najmanje varijance. U našem uzorku on iznosi
`r hr_broj(s15$var_omjer, 2)`, dakle skupine su dovoljno slične da klasična
inačica ne bude sporna.

Kad taj omjer naraste, postoji ista rezerva kao u prethodnom poglavlju.
Welchova inačica ukupnog testa ne pretpostavlja jednake varijance i prilagođava
stupnjeve slobode. Na našim podacima daje F od `r hr_broj(s15$welch_f, 2)` uz
`r hr_broj(s15$welch_df2, 1)` stupnjeva slobode u nazivniku, dakle isti
zaključak uz nešto opreznije brojke.

Kruskal-Wallisov postupak mijenja pitanje umjesto da popravlja pretpostavku.
Rangira sve vrijednosti i uspoređuje prosječne rangove skupina, pa ga jedno
krajnje opažanje ne pomiče. Na našim podacima daje statistiku od
`r hr_broj(s15$kw, 1)` uz jednak broj stupnjeva slobode kao ukupni test.
Zaključak je isti, ali tvrdnja nije, jer se odnosi na položaje raspodjela, a ne
na sredine.

Nijedan od tih postupaka ne popravlja ovisna opažanja. Ako su ista lica mjerena
u više uvjeta ili su ljudi grupirani unutar razreda, škola ili gradova, potreban
je model koji tu strukturu uzima u obzir. Takvi modeli izlaze iz opsega ove
knjige, a njihov je zajednički korijen upravo okvir iz sljedećeg poglavlja.

## Razrađeni primjer

Cijela analiza pet skupina staje u nekoliko redaka, i vrijedi je vidjeti u
redoslijedu kojim je poglavlje izgrađeno. Zajednički model dolazi prvi, parne
usporedbe tek nakon njega.

Funkcija `aov` procjenjuje isti oblik modela sredina kao `lm` iz prethodnog
poglavlja, ali ga ispisuje u obliku razlaganja varijance. Njezina uobičajena
F-inferencija pripada homoskedastičnom linearnom modelu s jednom zajedničkom
rezidualnom varijancom, a ne Welchovu postupku sa zasebnim skupnim varijancama i
prilagođenim stupnjevima slobode. Funkcija `TukeyHSD` prima takav model i vraća
sve parne razlike s intervalima i korigiranim p-vrijednostima.

Ispis potvrđuje ono što je poglavlje izgradilo. Redak modela nosi razlaganje
`r hr_broj(s15$ss_izmedu, 1)` prema `r hr_broj(s15$ss_unutar, 1)`, iz čega
slijede F i eta-kvadrat. Tablica parnih usporedbi zatim pokazuje da se društvene
mreže odvajaju od svakog preostalog izvora, dok se ta četiri međusobno ne
razlučuju.

Rečenica koju bi izvještaj smio sadržavati zato je uža od one koju bi ukupni
test sam sugerirao. Razlika među izvorima postoji, nosi je jedna skupina, iznosi
oko boda i pol na ljestvici od deset, i objašnjava desetinu ukupne
varijabilnosti. Sve što ide dalje od toga traži dizajn koji ovi podaci nemaju.

## Sažetak

Deset odvojenih usporedbi među pet skupina griješi mnogo češće nego što obećava,
i simulacija to pokazuje bez ijedne formule. Zajednički model rješava isti
problem jednim testom tako da razlaže rasipanje na dio među skupinama i dio
unutar njih te ih stavlja u omjer. Taj model nije nov nego je prošireni model iz
poglavlja o dvjema grupama, s jednim koeficijentom po nereferentnoj skupini.
Ukupni test ne imenuje parove, pa nakon njega dolaze planirane usporedbe ili
korigirane parne razlike s intervalima. Eta-kvadrat i omega-kvadrat opisuju
objašnjeni udio, a pretpostavke se čitaju iz ostataka. Sljedeće poglavlje
uklanja i posljednju granicu, jer isti okvir prima prediktor koji uopće nije
kategorija.

## Pojmovi

analiza varijance (*analysis of variance*), stopa obiteljske pogreške
(*familywise error rate*), F-statistika (*F-statistic*), Tukeyjev postupak
(*Tukey's HSD*), planirana usporedba (*planned contrast*), eta-kvadrat (*eta
squared*), Kruskal-Wallisov test (*Kruskal–Wallis test*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Skicirajte tri skupne sredine i raspršenosti uz koje bi ukupni test bio značajan,
a samo jedan par razlučiv.

### Računski

Razlaganje daje 120 na razlike među četirima skupinama i 480 na razlike unutar
njih, uz ukupno sto opažanja. Izračunajte obje prosječne raspršenosti, njihov
omjer i eta-kvadrat. Objasnite što bi se s omjerom dogodilo da je drugi broj
dvostruko veći.

### Kritički

Prosudite kako broj analitičkih odluka mijenja čitanje najmanje p-vrijednosti
među mnogim skupinama i ishodima (Simmons, 2011). Predajte jedan odlomak i
navedite podatak koji bi u izvještaju taj broj učinio vidljivim.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite tvrdnju o ukupnom modelu koja
stoji, imenujte tvrdnju o parovima koja ne slijedi i napišite rečenicu kojom bi
je trebalo zamijeniti.
