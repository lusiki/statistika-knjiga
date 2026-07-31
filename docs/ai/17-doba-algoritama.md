# Statistika u doba algoritama

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-31 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 6 min | Istraživač pravednosti | simulacija | pogl. 7 i 16 |

**Vinjeta.**
Chouldechova je analizirala instrumente za predviđanje povratka u kriminal i
pokazala da se poželjna mjerila pravednosti mogu sukobiti kada se temeljne
stope razlikuju među skupinama (Chouldechova, 2017). Jednako tumačenje
predviđenog rizika, jednake stope lažno pozitivnih odluka i jednaka ukupna
točnost ne mogu se uvijek postići istodobno.

To nije samo matematička neugodnost. Prag modela odlučuje tko će biti
zaustavljen, provjeren, preporučen ili uskraćen. Pogreške imaju različite
posljedice, a zbirna ocjena skriva na koga padaju.

Kako statistički čitati algoritam koji ne opisuje samo društvo, nego sudjeluje
u raspodjeli pažnje, prilika i rizika?

## Predikcija na novim podacima

Algoritamski model uči obrazac na skupu za treniranje i provjerava ga na
odvojenom skupu za testiranje. Razdvajanje postoji zato što model može naučiti
slučajnu posebnost podataka koje je već vidio. **Preprilagodba** nastaje kada
pristajanje treningu raste, a sposobnost generalizacije na nove slučajeve
slabi.

Predikcija i objašnjenje postavljaju različite kriterije dobrog modela
(Breiman, 2001). Predikcijski model vrednuje pogrešku na novim podacima.
Objašnjavajući model traži koeficijente i strukturu koje možemo povezati s
teorijom. Visoka prediktivna uspješnost ne pretvara korištene varijable u
uzroke.

Klasifikacija prevodi rezultat modela u kategoriju pomoću praga. Pomicanje
praga mijenja odnos lažno pozitivnih i lažno negativnih odluka. Ne postoji
prag koji minimizira svaku vrstu pogreške bez odluke o njihovoj cijeni.

## Algoritam kao društvena infrastruktura

Sustav preporuke ne predviđa samo što će osoba možda odabrati. Rangiranjem
sadržaja mijenja ono što osoba uopće može vidjeti. Podaci o prethodnom
ponašanju tako postaju ulaz u okruženje koje proizvodi sljedeće ponašanje.
Promatrač i predmet promatranja ulaze u povratnu petlju.

Metrika poput vremena zadržavanja nije neutralna zamjena za zadovoljstvo,
informiranost ili javnu vrijednost. Ona operacionalizira cilj sustava.
Optimizacija zatim vrlo učinkovito povećava ono što je izmjereno, uključujući
slučajeve u kojima mjera slabo predstavlja društvenu svrhu.

Društvenoznanstveno pitanje zato uključuje vlasništvo nad podacima, institucionalni
cilj, mogućnost žalbe i skupine koje nose pogreške. Tehnička dokumentacija
modela nije potpuna bez opisa konteksta njegove uporabe.

## Pravednost i temeljne stope

Mjere pravednosti promatraju različite dijelove tablice odluka. Jednaka stopa
lažno pozitivnih odluka usredotočuje se na osobe bez ishoda. Jednaka
prediktivna vrijednost pita koliko je pozitivnih odluka doista pozitivno.
Kada se temeljne stope razlikuju, ta se mjerila mogu matematički razići
(Chouldechova, 2017; Barocas, 2023).

Izbor mjerila nije samo tehnički. On određuje koju vrstu pogreške i koju
populaciju sustav štiti. Poštena analiza zato prikazuje više mjerila po skupini,
objašnjava prag i navodi institucionalnu posljedicu svake pogreške.

## Jezični modeli kao distribucije

Veliki jezični model proizvodi tekst predviđanjem sljedećih dijelova niza iz
raspodjele naučene na velikom korpusu. Tečnost je rezultat uspješnog
modeliranja jezičnih obrazaca. Nije ugrađena provjera da tvrdnja odgovara
stvarnom izvoru.

Model može dati korisnu strukturu, kod ili alternativno objašnjenje, ali
činjenice moraju ostati vezane uz provjerljive dokumente i podatke. Kada izvor
nije dostupan, odgovoran odgovor označava prazninu. Samouvjerena rečenica bez
podrijetla samo je predikcija koja zvuči kao znanje.

## Interakcija — Istraživač pravednosti

Istraživač pravednosti mijenja klasifikacijski prag za dvije skupine s
različitim temeljnim stopama, ali jednakom kvalitetom rezultata uvjetno na
stvarni ishod. Tako se vidi kako zajednički prag može izjednačiti neke stope
pogreške, a ipak proizvesti različitu prediktivnu vrijednost i točnost.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Analiza instrumenata za procjenu rizika
pokazala je sukob između kalibracije i jednakosti određenih stopa pogreške kada
se temeljne stope razlikuju (Chouldechova, 2017).

Tvrdnja da je model „pravedan" zato nije potpuna bez imenovanja mjerila,
skupina, praga i posljedica. Agregatna točnost može ostati jednaka dok se vrste
pogrešaka vrlo nejednako raspoređuju.

**Pitajte model.**
Asistent može izračunati tablice zabune i mjerila po skupinama. Treba mu dati
stvarne ishode, predviđene rezultate i prag, bez osobnih identifikatora.
Provjeravamo nazivnike svake stope i tražimo da sukob mjerila ne riješi
neobrazloženom tvrdnjom da je jedno „najpoštenije".

> Izračunaj tablicu zabune i stope pogrešaka zasebno po skupinama. Objasni kako
> prag i temeljne stope mijenjaju mjerila, a vrijednosni izbor ostavi jasno
> označenim.

**Nađite grešku.**
Model ima jednaku ukupnu točnost u dvjema skupinama, a prag je za obje jednak.
Zato je algoritam pravedan i nije potrebno pregledavati zasebne stope pogreške.

Greška je zaključak da jednaka ukupna točnost dokazuje pravednost. Lažno
pozitivne i lažno negativne odluke mogu se različito rasporediti unatoč istoj
točnosti.

## Razrađeni primjer

Simuliramo dvije skupine s različitim temeljnim stopama i isti bučni
prediktivni rezultat. Jedan zajednički prag pretvara rezultat u odluku.
Izračun ne tvrdi da je neka stvarna skupina takva. Pokazuje kako nazivnici
stvaraju različita mjerila.

*Slika. Stope pogrešaka u simuliranom klasifikacijskom primjeru. Izrada autora prema @barocas2023.*

Tablica pokazuje da jedno mjerilo ne opisuje cijelu raspodjelu odluka.
Promjena praga može smanjiti jednu pogrešku i povećati drugu. Odluka o
prihvatljivom odnosu zahtijeva znanje o posljedicama, mogućnosti žalbe i
instituciji koja model primjenjuje.

Ista disciplina vrijedi za sustave preporuke i jezične modele. Prije procjene
rezultata moramo znati koji je cilj optimiziran, na kojim je podacima sustav
učen i kako njegove pogreške ulaze u društvenu praksu.

## Sažetak

Algoritamski model procjenjujemo na novim podacima i prema cilju koji je doista
optimiziran. Klasifikacijski prag raspoređuje vrste pogrešaka, a različite
temeljne stope mogu dovesti mjerila pravednosti u sukob. Sustavi preporuke
mijenjaju okruženje koje mjere, dok jezični modeli proizvode tečan tekst bez
ugrađenog jamstva istinitosti. Statistička pismenost zato ostaje odgovornost za
izvor, nazivnik, cilj i posljedice odluke.

## Pojmovi

skup za treniranje (*training set*), skup za testiranje (*test set*),
preprilagodba (*overfitting*), klasifikacijski prag (*classification
threshold*), tablica zabune (*confusion matrix*), temeljna stopa (*base rate*),
algoritamska pravednost (*algorithmic fairness*)

## Zadaci

### Konceptualni

Objasnite zašto jednaka ukupna točnost ne jamči jednake posljedice za dvije
skupine. Predajte dvije moguće tablice zabune.

### Računski

Promijenite prag u objektu `sim_klasifikacija` i predajte graf dviju stopa
pogreške po skupini.

### Kritički

Prosudite zašto se mjerila pravednosti mogu sukobiti kada se temeljne stope
razlikuju (Chouldechova, 2017; Barocas, 2023). Predajte odlomak bez proglašenja
jednog mjerila univerzalno najboljim.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dvije stvarne provjere, jednu
neopravdanu tvrdnju o pravednosti i mjerila koja još treba prikazati.
