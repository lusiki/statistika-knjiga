# DIO IV: ZAKLJUČIVANJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Logika testiranja

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Simulator p-vrijednosti | simulacija | pogl. 7–9 |

**Vinjeta.**
Američko statističko udruženje moralo je javno razjasniti p-vrijednost jer je
jedan računski izlaz prečesto služio kao automatska odluka o postojanju učinka
(Wasserstein, 2016). Istraživački izvještaji pretvarali su prag u granicu između
rezultata koji „postoje" i onih koji „ne postoje", iako postupak nije mogao
nositi takvu podjelu.

Testiranje ne počinje pragom. Počinje zamišljenim svijetom u kojem nema učinka
koji tražimo, a zatim pita koliko je opaženi rezultat neobičan u tom svijetu.
Odgovor ovisi o modelu, testnoj statistici i svim odlukama koje su proizvele
podatke.

Što mala p-vrijednost govori o podacima, a što ne može reći o hipotezi?

## Svijet bez učinka

Postupak najprije postavlja **nultu hipotezu**, precizan model svijeta bez
razlike ili veze koju istražujemo. Alternativna hipoteza opisuje odstupanje
koje nas zanima. Te hipoteze nisu dvije jednako dokazane priče. Test je
konstruiran tako da procjenjuje ponašanje podataka pod nultim modelom.

Simulacija tu logiku pokazuje bez formule. Oznake skupina možemo nasumično
premještati kada nulta hipoteza tvrdi da skupine nisu različite. Nakon svakog
premještanja računamo razliku. Dobivena nulta raspodjela govori koliko se velike
razlike pojavljuju samo zbog slučajnog rasporeda.

**P-vrijednost** je udio rezultata pod nultim modelom koji su barem toliko
neusklađeni s njime kao opaženi rezultat. Ona nije vjerojatnost da je nulta
hipoteza istinita, nije vjerojatnost da je nalaz slučajan i ne mjeri važnost
učinka (Wasserstein, 2016).

## Dvije vrste pogreške

Odbacivanje istinite nulte hipoteze stvara pogrešku prve vrste. Neodbacivanje
nulte hipoteze kada relevantan učinak postoji stvara pogrešku druge vrste.
Snižavanje praga otežava prvi tip pogreške, ali uz jednak dizajn može olakšati
drugi. Nema postupka koji obje mogućnosti uklanja besplatno.

Neodbacivanje nije prihvaćanje nulte hipoteze. Rezultat može biti kompatibilan
s nedostatkom učinka, ali i s nizom učinaka koje neprecizan uzorak nije mogao
razlikovati. Zbog toga test čitamo uz procjenu i interval, a ne umjesto njih.

Bayesovski pristup izravnije uspoređuje kako podaci mijenjaju početna uvjerenja
o modelima. U ovoj knjizi ostaje pogled kroz prozor, a ne drugi puni račun.
Važno je prepoznati da odgovara na drugo pitanje i zahtijeva eksplicitne
početne pretpostavke.

## Interakcija — Simulator p-vrijednosti

Simulator p-vrijednosti stvara rezultate kada je nulta hipoteza istinita i
kada nije. Čitatelj promatra koliko se p-vrijednosti mijenjaju od uzorka do
uzorka i zašto jedan rezultat ne može biti potvrda postupka u cjelini. Radi
preglednosti koristi normalne ishode s poznatom varijabilnošću i obostrani test.

*Slika. Raspodjele p-vrijednosti pod nultim modelom i pod odabranim stvarnim učinkom.*

**Što isprobati.**

1. Generirajte više uzoraka pod istinitom nultom hipotezom.
2. Postavite standardiziranu razliku na 0,35 i zadržite uzorak jednakim.
3. Povećajte uzorak bez promjene učinka i usporedite udio rezultata ispod praga.
4. Spustite prag s 0,05 na 0,01 i usporedite obje raspodjele.

Simulacija razdvaja dvije činjenice. Kada je nulta hipoteza istinita, prag
unaprijed određuje dugoročnu stopu pogreške. Kada učinak postoji, veličina
uzorka mijenja koliko ga često postupak otkriva.

**Statistika u divljini.**
**Značajnost bez veličine.** Izjava Američkog statističkog udruženja navodi da
znanstveni zaključak ili odluka ne bi smjeli ovisiti samo o tome prelazi li
p-vrijednost određeni prag (Wasserstein, 2016).

Naslov koji rezultat pretvara u „dokazano" uklanja nulti model, veličinu
učinka, interval i kvalitetu dizajna. Odgovorno čitanje vraća te dijelove prije
nego što procijeni doprinos nalaza.

**Pitajte model.**
Asistent može provesti test i simulirati nultu raspodjelu, ali mu treba zatražiti
da prvo imenuje nultu hipotezu, testnu statistiku i jedinicu permutiranja.
Provjeravamo odgovara li test dizajnu, jesu li opažanja neovisna i tumači li
p-vrijednost kao vjerojatnost hipoteze.

> Opiši nultu hipotezu, izgradi nultu raspodjelu simulacijom i usporedi opaženu
> statistiku s njome. Izvijesti procjenu i interval prije p-vrijednosti.

**Nađite grešku.**
Test je prikladan za dizajn, procjena i interval su prikazani, a p-vrijednost
je mala. Zato je vjerojatnost da je nulta hipoteza istinita jednaka toj
p-vrijednosti.

Greška je zamjena uvjetnih vjerojatnosti. P-vrijednost opisuje podatke pod
nultim modelom, a ne vjerojatnost nultog modela nakon opaženih podataka.

## Razrađeni primjer

Simuliramo dvije skupine bez stvarne razlike i promatramo jednu opaženu razliku
sredina. Permutacijski postupak miješa oznake skupina, čuva sve ishode i gradi
raspodjelu razlika usklađenu s nultom hipotezom.

Nulta raspodjela razlike sredina u simuliranom primjeru. Izrada autora.

Graf pokazuje koliko je opažena razlika udaljena od onoga što stvara postupak
bez grupnog učinka. Zaključak ne završava odbacivanjem ili neodbacivanjem.
Vraća se procjeni razlike, njezinoj preciznosti i dizajnu koji određuje smijemo
li govoriti o uzroku.

## Sažetak

Testiranje uspoređuje opaženi rezultat s raspodjelom pod preciznom nultom
hipotezom. P-vrijednost opisuje tu neusklađenost i ne govori kolika je
vjerojatnost hipoteze ni koliko je učinak važan. Dvije vrste pogreške povezuju
prag s posljedicama odluke. Sljedeće poglavlje zato stavlja veličinu učinka i
snagu ispred rituala značajnosti.

## Pojmovi

nulta hipoteza (*null hypothesis*), alternativna hipoteza (*alternative
hypothesis*), testna statistika (*test statistic*), p-vrijednost (*p-value*),
pogreška prve vrste (*Type I error*), pogreška druge vrste (*Type II error*)

## Zadaci

### Konceptualni

Objasnite zašto p-vrijednost nije vjerojatnost nulte hipoteze. Predajte
objašnjenje koje razlikuje uvjetovanje na model od uvjerenja o modelu.

### Računski

Promijenite veličinu razlike u objektu `sim_test`. Predajte dvije nulte
raspodjele i usporedbu opaženih statistika.

### Kritički

Prosudite tvrdnju da prelazak praga sam određuje znanstvenu važnost nalaza
(Wasserstein, 2016). Predajte kratku uredničku bilješku.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira. Imenujte ispravan postupak, jednu
zamjenu vjerojatnosti i ispravnu rečenicu o rezultatu.

---

# Veličina učinka i snaga

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Istraživač snage | simulacija | pogl. 9, 10 |

**Vinjeta.**
Cohen je kritizirao praksu u kojoj je statistička značajnost zamjenjivala
razmišljanje o veličini i važnosti učinka (Cohen, 1994). Vrlo velik uzorak može
malu razliku učiniti lako uočljivom, dok mali uzorak može propustiti učinak
koji bi bio važan ljudima na koje se odluka odnosi.

Problem zato nije riješen pitanjem postoji li razlika. Istraživač mora prije
prikupljanja podataka odrediti koja bi razlika promijenila zaključak ili
postupanje. Tek tada veličina uzorka postaje planska odluka.

Koliko podataka trebamo da bismo pouzdano uočili učinak koji je vrijedan
uočavanja?

## Razlika koja nešto znači

**Veličina učinka** opisuje koliko su skupine, uvjeti ili varijable udaljeni na
ljestvici koja omogućuje usporedbu. Sirova razlika čuva izvorne jedinice i
često je najlakša za sadržajno tumačenje. Standardizirana razlika poput
Cohenova d izražava pomak u jedinicama zajedničke standardne devijacije
(Cohen, 1988).

Standardizacija ne odlučuje što je važno. Pragovi za „mali", „srednji" i
„veliki" učinak mogu služiti kao gruba orijentacija, ali društvena posljedica
ovisi o ishodu, trošku, vremenu i populaciji. Mala promjena može biti važna kada
se odnosi na mnogo ljudi ili na ozbiljan ishod.

Statistička i praktična važnost zato se izvještavaju odvojeno. Procjena i
interval govore koje su veličine usklađene s podacima. Sadržajna prosudba
govori koje bi od tih veličina opravdale odluku.

## Planiranje unatrag

**Statistička snaga** je vjerojatnost da postupak prepozna određeni učinak kada
on postoji. Raste s većim učinkom, većim uzorkom, manjom varijabilnošću i
liberalnijim pragom. Ti se čimbenici ne mogu tumačiti odvojeno od dizajna i
posljedica pogrešaka.

Slaba snaga ne proizvodi samo više propuštenih nalaza. Među rezultatima koji
ipak prijeđu prag procijenjeni učinci mogu biti nestabilni i pretjerani.
Planiranje zato počinje najmanjim učinkom vrijednim pažnje, željenom
preciznošću i dostupnim resursima, a ne pitanjem koliko je sudionika ostalo do
kraja semestra.

## Interakcija — Istraživač snage

Istraživač snage povezuje veličinu učinka, uzorak i prag. Čitatelj mijenja
jedan element dok ostale drži jednakima i vidi da ista odluka ima različite
posljedice za male i velike učinke.

*Slika. Simulirana snaga kroz veličine uzorka u idealiziranom postupku s poznatom varijabilnošću.*

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Spustite prag odluke i provjerite koliko je jedinica potrebno za istu snagu.
4. Povećajte broj ponavljanja i promatrajte koliko se krivulja zaglađuje.

Krivulja pokazuje zašto snaga nije trajno svojstvo testa. Ona pripada
određenoj kombinaciji učinka, uzorka, varijabilnosti i praga, pa se mora
planirati za rezultat koji bi bio sadržajno važan.

**Statistika u divljini.**
**Zemlja je okrugla.** Cohenov naslov sažima kritiku rituala u kojem poznata ili
trivijalna razlika dobiva oznaku važnosti samo zato što je p-vrijednost mala
(Cohen, 1994).

Odgovoran izvještaj navodi učinak i njegov interval, a zatim objašnjava što
raspon znači u sadržajnom kontekstu. Prag ne može obaviti tu prosudbu umjesto
istraživača i čitatelja.

**Pitajte model.**
Asistent može izračunati standardizirani učinak i provesti analizu snage, ali
mu treba dati dizajn, očekivanu varijabilnost i najmanji važan učinak.
Provjeravamo koristi li neovisni ili upareni postupak, brka li postignutu snagu
s kvalitetom rezultata i tretira li konvencionalni prag kao sadržajnu činjenicu.

> Planiraj uzorak iz najmanjeg učinka vrijednog pažnje, željene snage i
> odabranog dizajna. Prikaži osjetljivost zaključka na svaku pretpostavku.

**Nađite grešku.**
Procjena učinka i interval pravilno su izračunati, a dizajn je uzet u obzir.
Budući da je test statistički značajan, učinak je nužno dovoljno velik da bude
praktično važan.

Greška je izjednačavanje statističke značajnosti s praktičnom važnošću.
Praktična važnost zahtijeva sadržajni prag i tumačenje procjene u izvornim
jedinicama.

## Razrađeni primjer

Planiramo simuliranu usporedbu dviju neovisnih skupina. Ne polazimo od
očekivanja da ćemo „dobiti značajnost", nego od standardizirane razlike koju bi
imalo smisla pouzdano uočiti. Funkcija zatim pokazuje potreban broj jedinica po
skupini (Cohen, 1988).

*Slika. Planiranje uzorka za nekoliko simuliranih scenarija. Izrada autora.*

Tablica pokazuje cijenu traženja manjih učinaka pod istim kriterijima. Konačan
plan ipak treba provjeru odustajanja, kvalitete mjerenja i izvedivosti. Račun
ne odlučuje koji je učinak vrijedan ulaganja.

## Sažetak

Veličina učinka vraća sadržaj pitanju koliko je razlika velika, a interval
pokazuje koliko je procjena precizna. Snaga povezuje učinak, uzorak,
varijabilnost i prag prije prikupljanja podataka. Statistička značajnost ne
određuje praktičnu važnost, a mali uzorci mogu iskriviti i otkrivene učinke.
Sljedeće poglavlje pokazuje što se događa kada sustav nagrađuje odluku, a
skriva cijeli put koji je do nje doveo.

## Pojmovi

veličina učinka (*effect size*), Cohenov d (*Cohen's d*), praktična važnost
(*practical significance*), statistička snaga (*statistical power*), najmanji
važan učinak (*smallest effect size of interest*), planiranje uzorka (*sample
size planning*)

## Zadaci

### Konceptualni

Objasnite kako velik uzorak može proizvesti statistički značajan, ali praktično
nevažan rezultat. Predajte jedan primjer bez stvarnih empirijskih brojki.

### Računski

Proširite objekt `scenariji` drugom željenom snagom i predajte tablicu potrebnih
uzoraka.

### Kritički

Prosudite Cohenovu kritiku odlučivanja samo prema pragu (Cohen, 1994). Predajte
kratak urednički standard za izvještavanje.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točne računske korake, jednu
pogrešnu prosudbu važnosti i podatak koji bi za tu prosudbu bio potreban.

---

# Kriza i obnova

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/12-kriza-i-obnova.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 6 min | Pješčanik p-hakiranja | simulacija | pogl. 10, 11 |

**Vinjeta.**
Velika suradnja istraživača pokušala je ponoviti niz objavljenih psiholoških
studija prema zajedničkom protokolu. Replikacijski rezultati u cjelini bili su
slabiji od slike koju je ostavljala izvorna literatura (Collaboration}, 2015). Rasprava
koja je slijedila nije se mogla svesti na podjelu između dobrih i loših
istraživača.

Objavljivanje je dugo nagrađivalo nov, jasan i statistički značajan rezultat.
Istraživači su istodobno donosili mnogo odluka o uzorku, ishodima, podskupinama
i modelima. Čak i bez svjesne prevare, fleksibilan put kroz podatke mogao je
završiti pričom koja izgleda unaprijed planirana (Simmons, 2011; Gelman, 2013).

Kako znanstveni sustav može učiniti vlastite rezultate provjerljivijima bez
pretvaranja skepticizma u cinizam?

## Putovi koji ostaju nevidljivi

P-hakiranje obuhvaća prilagođavanje analize sve dok se ne pojavi poželjan
rezultat. Može uključivati promjenu ishoda, pravila isključivanja, trenutka
zaustavljanja ili skupa kontrolnih varijabli. Svaka odluka može imati razumno
obrazloženje, ali njihova kombinacija mijenja vjerojatnost konačnog nalaza
(Simmons, 2011).

Vrt račvajućih putova širi problem. Istraživač ne mora isprobati deset analiza
i sakriti devet. Podaci mogu usmjeriti jednu odabranu analizu kroz niz odluka
koje bi bile drukčije da su podaci izgledali drukčije (Gelman, 2013). Konačni
tekst pokazuje samo put kojim se prošlo, ne sve putove koji su bili mogući.

Publikacijska pristranost zatim djeluje na razini literature. Rezultati koji
izgledaju jasni i novi lakše postaju vidljivi, dok neodređeni i neuspjeli
pokušaji ostaju u ladicama. Metaanaliza tada može precizno sažeti odabrani dio
istraživačkog zapisa i dati varljiv osjećaj stabilnosti.

## Reforma kao promjena postupka

Predregistracija vremenski odvaja plan od ishoda. Ona ne jamči dobar plan ni
istinito mjerenje, ali čitatelju pokazuje koje su odluke donesene prije gledanja
podataka. Registrirani izvještaj ide dalje jer se pitanje i metoda vrednuju
prije nego što je rezultat poznat.

Otvoreni podaci, materijali i kod omogućuju provjeru i ponavljanje. Otvorenost
ne uklanja etičke i privatnosne granice. Podaci o ljudima ne postaju sigurni
samim objavljivanjem, pa transparentnost mora uključiti razloge zbog kojih neki
materijali ne mogu biti javni.

Replikacija nije glasanje o tome je li izvorni autor bio u pravu. Rezultati se
mogu razlikovati zbog uzoračke varijacije, konteksta, mjerenja ili stvarne
heterogenosti učinka. Obnova zato traži kumulativno čitanje procjena i uvjeta,
a ne zamjenu jednog spektakularnog nalaza drugim.

## Asistent u dvostrukoj ulozi

Generativni modeli mogu ubrzati izradu koda, provjeru tablica i usporedbu
izvještaja s analizom. Isti kapacitet može proizvoditi uvjerljive izvore koji ne
postoje, sintetičke rukopise i velik broj varijanti iste tvrdnje. Brzina
pojačava i provjeru i proizvodnju šuma.

Disciplina rada s asistentom zato mora ostaviti trag. Čuvamo ulazne podatke,
upit, kod, verziju alata i ručnu provjeru. Model ne dobiva osjetljive
ispitanikove podatke, a njegov tekst ne postaje izvor. Izvor ostaje publikacija,
skup podataka ili reproducibilan postupak koji se može otvoriti bez modela.

## Interakcija — Pješčanik p-hakiranja

Pješčanik omogućuje biranje ishoda, podskupina i trenutka zaustavljanja na
podacima bez stvarnog učinka. Čitatelj promatra kako rast broja odluka povećava
priliku za privlačan rezultat i kako korekcija za cijeli postupak mijenja sliku.
Radi preglednosti svaki je analitički put u simulaciji neovisan. Stvarni putovi
često dijele podatke, ali idealizacija izdvaja cijenu njihova broja.

*Slika. Udio simuliranih istraživanja s barem jednim rezultatom ispod odabranog praga nakon pretraživanja više neovisnih analitičkih putova.*

**Što isprobati.**

1. Provedite jednu unaprijed određenu analizu.
2. Dodajte ishode, a podskupine i trenutke provjere ostavite jednakima.
3. Dodajte podskupinske inačice i trenutke provjere bez promjene broja ishoda.
4. Usporedite nominalni prag 0,05 s pragom korigiranim za sve putove.

Najmanja p-vrijednost nije sažetak jedne unaprijed određene analize kada je
nastala pretraživanjem. Zaključak tada mora opisati cijeli skup mogućnosti ili
koristiti postupak koji njihov broj uzima u obzir.

**Statistika u divljini.**
**Replikacija kao zajedničko mjerenje.** Open Science Collaboration koristio je
zajednički postupak za procjenu reproducibilnosti niza psiholoških nalaza
(Collaboration}, 2015). Rezultat nije jednostavna stopa istine jer se izvorne i replikacijske
studije razlikuju u preciznosti, kontekstu i mogućim učincima.

Vrijednost projekta leži i u tome što je privatni problem pojedinačnih sumnji
pretvorio u podatke o sustavu. Čitatelj može procjenjivati obrasce bez
pretpostavke da svaki neuspjeh ima isti uzrok.

**Pitajte model.**
Asistent može usporediti registrirani plan, kod i rukopis te označiti
neslaganja. Ne smije izmišljati nedostajuće datoteke ni procjenjivati
reproducibilnost samo prema tonu teksta. Svaki nalaz mora imati put do retka
koda, tablice ili dokumenta.

> Usporedi istraživački plan, analitički kod i izvještaj. Navedi svako
> odstupanje s točnim mjestom u dokumentima i odvoji potvrđene razlike od
> informacija koje nedostaju.

**Nađite grešku.**
Studija je predregistrirala ishod, pravilo isključivanja i model prije
prikupljanja podataka. Kod i anonimizirani materijali dostupni su za provjeru.
Zbog predregistracije rezultat mora biti istinit.

Greška je pretvaranje predregistracije u jamstvo istine. Ona povećava
vidljivost analitičkih odluka, ali ne uklanja pogrešku mjerenja, uzoračku
varijaciju, slabu teoriju ni neprikladan model.

## Razrađeni primjer

Simuliramo podatke bez stvarne grupne razlike, ali s više mogućih ishoda.
Analitičar koji prijavi samo najmanju p-vrijednost prikazuje rezultat jedne
odabrane analize, dok je stvarni postupak uključivao mnogo prilika
(Simmons, 2011).

*Slika. Najmanja p-vrijednost među simuliranim ishodima bez učinka. Izrada autora prema @simmons2011.*

Tablica je jedna realizacija simulacije i ne mora svaki put sadržavati
privlačan rezultat. Upravo je to poanta. Kada se cijeli postupak ponavlja,
neki će nizovi ponuditi malu p-vrijednost bez učinka. Predregistracija,
izvještavanje svih ishoda i korekcija za višestrukost čine tu priliku vidljivom.

Reforma ne traži da prestanemo istraživati neočekivane obrasce. Traži da
razlikujemo potvrđujuću analizu od naknadnog istraživanja i da novu hipotezu
predstavimo kao početak sljedeće provjere.

## Sažetak

Kriza reproducibilnosti nastaje iz spoja uzoračke varijacije, analitičke
fleksibilnosti i poticaja koji nagrađuju jasan pozitivan nalaz. Predregistracija,
registrirani izvještaji i otvoreni materijali povećavaju vidljivost postupka, ali
ne jamče istinu. Replikacija procjenjuje stabilnost nalaza kroz nove podatke i
uvjete. Asistent može pomoći u provjeri samo kada njegov rad ostaje
reproducibilan, provjerljiv i odvojen od izvora.

## Pojmovi

p-hakiranje (*p-hacking*), vrt račvajućih putova (*garden of forking paths*),
publikacijska pristranost (*publication bias*), predregistracija
(*preregistration*), registrirani izvještaj (*registered report*), replikacija
(*replication*), otvorena znanost (*open science*)

## Zadaci

### Konceptualni

Razlikujte p-hakiranje od vrta račvajućih putova. Predajte dva kratka scenarija
koja pokazuju razliku (Simmons, 2011; Gelman, 2013).

### Računski

Ponovite simulaciju `sim_putovi` mnogo puta i predajte raspodjelu najmanjih
p-vrijednosti.

### Kritički

Prosudite što veliki replikacijski projekt može reći o literaturi, a što ne
može o svakoj pojedinačnoj studiji (Collaboration}, 2015). Predajte dva odlomka.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dvije dobre prakse, jednu
pretjeranu tvrdnju i ograničenje koje ostaje nakon predregistracije.
