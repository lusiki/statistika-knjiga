# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Cumming je zagovarao izvještavanje procjena i intervala kao središte
statističkog zaključivanja, umjesto oslanjanja na samu odluku o značajnosti
(Cumming, 2014). Pomak mijenja pitanje koje postavljamo podacima. Umjesto
binarnog prolaza pitamo koliki je učinak i koliko je procjena precizna.

Interval ipak nije ukras oko točkaste procjene. Njegovo značenje dolazi iz
postupka koji bi kroz ponovljene uzorke stvarao intervale, među kojima neki
obuhvaćaju populacijsku vrijednost, a neki je promašuju.

Kako iz jednog opaženog intervala pošteno govoriti o vrijednosti koja ostaje
nepoznata?

## Od točke prema rasponu

**Točkasta procjena** daje jednu vrijednost iz uzorka. Ona je najbolji sažeti
pogodak koji trenutačno imamo, ali drugi bi uzorak dao drugi rezultat. Interval
pouzdanosti toj procjeni dodaje raspon usklađen s njezinom uzoračkom
promjenjivošću.

Širi interval nije znak lošeg istraživača. On može pošteno pokazivati mali
uzorak ili vrlo promjenjive podatke. Uži interval označava veću preciznost pod
pretpostavkama postupka. Ne govori da su mjera, uzorak i model nepristrani.

Razina pouzdanosti pripada dugoročnom postupku. Kada bismo uzorkovanje i izradu
intervala ponavljali, unaprijed određeni udio intervala obuhvatio bi fiksnu
populacijsku vrijednost. Nakon što je jedan interval izračunat, njegova je
granica opažena, a populacijska vrijednost ostaje nepoznata.

## Bootstrap iz uzorka

Bootstrap ponovljeno izvlači opažanja s vraćanjem iz dostupnog uzorka, računa
željenu statistiku i slaže dobivene vrijednosti u raspodjelu (Efron, 1979).
Postupak tako približava pitanje što bi se dogodilo s procjenom kada bismo mogli
ponoviti prikupljanje sličnih podataka.

Njegova snaga je prilagodljivost. Može se primijeniti na medijan, razliku,
korelaciju i druge statistike za koje jednostavna formula nije pri ruci.
Njegova granica ostaje početni uzorak. Ako on ne predstavlja populaciju ili je
premalen da zabilježi važan dio raspodjele, resampling ponavlja tu prazninu.

## Interakcija — Hvatač intervala

Hvatač intervala prikazuje niz ponovljenih uzoraka i njihove intervale oko iste
populacijske vrijednosti. Većina je hvata, a neki je promašuju. Tek niz
intervala čini značenje razine pouzdanosti vidljivim.

**Što isprobati.**

1. Generirajte jedan interval i zabilježite obuhvaća li cilj.
2. Povećajte broj ponavljanja bez promjene postupka.
3. Usporedite preciznost pri različitim veličinama uzorka.

**Statistika u divljini.**
**Procjena prije odluke.** Pristup „novih statistika" stavlja veličinu učinka,
interval i metaanalitičko povezivanje nalaza ispred binarne odluke o
značajnosti (Cumming, 2014).

Interval ne jamči da je istina blizu sredine ni da je istraživanje valjano.
Njegova vrijednost je u tome što čitatelju pokazuje koje su veličine još
usklađene s postupkom i koliko prostora ostaje za znanstvenu nesigurnost.

**Pitajte model.**
Asistent može bootstrapirati gotovo svaku statistiku, ali treba provjeriti
uzorkuje li s vraćanjem, čuva li strukturu uparenih ili grupiranih podataka i
ponavlja li dovoljno puta. Modeli često daju pogrešno probabilističko značenje
već izračunatom intervalu.

> Izračunaj točkastu procjenu i bootstrap interval. Sačuvaj strukturu podataka,
> opiši postupak resamplinga i interpretiraj razinu pouzdanosti kao svojstvo
> ponovljenog postupka.

**Nađite grešku.**
Bootstrap raspodjela je približno simetrična i interval je uredno izračunat iz
njezinih krajeva. Postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

Greška je pripisivanje vjerojatnosti fiksnom parametru nakon izračuna
frekventističkog intervala. Razina pouzdanosti opisuje dugoročni udio intervala
koji obuhvaćaju parametar.

## Razrađeni primjer

Simulirani uzorak sadrži ocjene povjerenja. Zanimaju nas medijan i njegova
nesigurnost jer raspodjela nije savršeno simetrična. Bootstrap uzorci ponovno
izvlače opažene ocjene s vraćanjem i za svaki izračunavaju medijan.

*Slika. Bootstrap procjena medijana simuliranih ocjena. Izrada autora.*

Tablica je rezultat simuliranog nastavnog primjera, a ne nalaz o stvarnom
povjerenju. Ona pokazuje redoslijed izvještavanja. Najprije dolazi procjena,
zatim raspon nesigurnosti i naposljetku ograničenje uzorka i mjere.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval prikazuje
preciznost postupka i mora se tumačiti kroz ponovljeno uzorkovanje. Bootstrap
približava tu promjenjivost resamplingom dostupnog uzorka, bez čarobnog
popravljanja njegove pristranosti. Sljedeće poglavlje uvodi testiranje kao još
jedan način usporedbe opaženog rezultata s raspodjelom mogućih rezultata.

## Pojmovi

točkasta procjena (*point estimate*), interval pouzdanosti (*confidence
interval*), preciznost (*precision*), bootstrap (*bootstrap*), resampling
(*resampling*), parametar (*parameter*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. Predajte jedan odlomak.

### Računski

Upotrijebite `sim_povjerenje`. Bootstrapirajte aritmetičku sredinu i medijan te
predajte usporednu tablicu intervala.

### Kritički

Prosudite zašto izvještaj usmjeren na procjenu i interval daje više informacija
od same odluke o značajnosti (Cumming, 2014). Predajte tri rečenice.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira. Imenujte točan postupak, jednu
pogrešnu rečenicu i frekventistički ispravnu zamjenu.
