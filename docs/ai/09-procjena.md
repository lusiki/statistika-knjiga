# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 21 min | Hvatač intervala | simulirana populacija | pogl. 8 |

**Vinjeta.**
Cumming je zagovarao izvještavanje procjena i intervala kao središte
statističkog zaključivanja, umjesto oslanjanja na samu odluku o značajnosti
(Cumming, 2014). Pomak mijenja pitanje koje postavljamo podacima. Umjesto
binarnog prolaza pitamo koliki je učinak i koliko je procjena precizna.

Poglavlje o uzorkovanju pokazalo je zašto takvo pitanje uopće ima smisla. Naša
procjena samo je jedan ishod iz raspodjele mogućih ishoda, a širina te
raspodjele poznata je u simulaciji jer smo uzorkovanje ponovili tri tisuće puta.

Istraživač koji objavljuje rezultat nema tri tisuće uzoraka. Ima jedan, i iz
njega mora reći koliko je siguran.

Kako iz jednoga opaženog uzorka pošteno govoriti o vrijednosti koja ostaje
nepoznata?

## Od točke prema rasponu

Uzorak od `r hr_broj(s9$n, 0)` osoba iz naše populacije daje prosječno
povjerenje u medije od `r hr_broj(s9$sredina, 2)`. Ta jedna vrijednost naziva se
**točkasta procjena** (*point estimate*) i najbolji je sažeti pogodak koji
trenutačno imamo. Njezina je slabost u tome što ne nosi nikakav trag vlastite
nesigurnosti. Ista brojka mogla je nastati iz uzorka od dvadeset ljudi i iz
uzorka od dvadeset tisuća, a te dvije situacije ne zaslužuju jednako povjerenje.

Sve što nedostaje već je izračunato u prethodnom poglavlju. Standardna pogreška
mjeri koliko bi procjena tipično varirala kroz ponovljena uzorkovanja, a za naš
uzorak iznosi `r hr_broj(s9$se, 3)`. Uz nju procjena prestaje biti gola brojka i
postaje brojka s poznatom skalom vlastitog kolebanja.

Središnji granični teorem kazuje i kakav oblik to kolebanje ima. Raspodjela
uzoračkih sredina približno je normalna, a za normalnu raspodjelu znamo koliki
udio vrijednosti pada unutar zadanog broja standardnih devijacija od središta,
što je pravilo koje je poglavlje o vjerojatnosti već postavilo. Približno 95 %
vrijednosti leži unutar 1,96 standardnih devijacija.

Odatle slijedi konstrukcija koja se čini gotovo previše jednostavnom da bi
radila. Ako je naša sredina u 95 % slučajeva unutar 1,96 standardnih pogrešaka
od populacijske vrijednosti, tada je i populacijska vrijednost u 95 % slučajeva
unutar te iste udaljenosti od naše sredine. Razmak oko procjene dug 1,96
standardnih pogrešaka na svaku stranu zato će hvatati cilj u 95 % ponavljanja.

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

Slovo $z^{*}$ označava koliko standardnih pogrešaka širimo na svaku stranu, i
bira ga željena razina, pa je za 95 % ono jednako 1,96. Za naš uzorak taj račun
daje raspon od `r hr_broj(s9$donja, 2)` do `r hr_broj(s9$gornja, 2)`, a prava
populacijska vrijednost iznosi `r hr_broj(s9$mu, 2)` i nalazi se unutra.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Vrijedi obratiti pozornost na to gdje u toj definiciji stoji obećanje. Ono ne
stoji uz raspon nego uz postupak, i upravo se ta razlika u praksi najčešće gubi.

## Što razina pouzdanosti obećava

Provjera je moguća jer populaciju poznajemo. Ponovimo cijeli postupak deset
tisuća puta, svaki put izvučemo novi uzorak od dvjesto osoba, izračunamo
njegovu sredinu i standardnu pogrešku, sastavimo interval i prebrojimo koliko
ih je obuhvatilo pravu vrijednost. Cilj je obuhvaćen u
`r paste0(hr_broj(s9$pokrivenost, 1), " %")` slučajeva, a promašen u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja.

Postupak dakle radi približno onako kako obećava, i vrijedi zadržati riječ
približno. Zamjena nepoznate populacijske raspršenosti onom izmjerenom u uzorku
unosi vlastitu nesigurnost, koja je pri dvjesto osoba mala, a pri dvadeset osoba
ne bi bila. Ispravak koji to nadoknađuje širi interval za mali uzorak i knjiga
ga uvodi u poglavlju o usporedbi dviju grupa, gdje ga postupak prvi put stvarno
treba.

Ono što se u brojci od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne vidi jest
sudbina pojedinačnog intervala. Svaki od tih dvije tisuće raspona ili sadrži
pravu vrijednost ili je ne sadrži, i nakon što je izračunat, u njemu nema
ničega slučajnog. Slučajan je bio uzorak koji ga je proizveo. Populacijska
sredina fiksan je broj i ne kreće se, pa rečenica o vjerojatnosti da se ona
nalazi unutar zadanih granica opisuje nešto što nema promjenjivosti koju bi ta
vjerojatnost mjerila.

Analogija koja to drži na okupu jest bacanje obruča na fiksni kolac. Obruč je
interval, kolac je parametar, a razina pouzdanosti opisuje koliko često obruč
pada oko kolca kroz mnogo bacanja. Nakon jednoga bacanja obruč je pao ili nije,
a mi ga gledamo zatvorenih očiju. Postotak opisuje ruku koja baca, ne ovaj
pojedini obruč.

Zbog te razlike korisno je znati što čitatelj objavljenog intervala smije reći.
Smije reći da su vrijednosti unutar granica uskladive s podacima, a one izvan
njih slabo uskladive, i to pod pretpostavkama koje je postupak koristio. Smije
reći da je istraživanje bilo dovoljno precizno da razluči razlike veće od
širine raspona, i da za manje razlike nije. Ne smije reći koliko je vjerojatno
da parametar leži unutra, niti da će se ponovljeno istraživanje smjestiti
unutar tih istih granica, jer bi drugo istraživanje imalo vlastiti uzorak i
vlastiti interval. Prve dvije rečenice pokrivaju gotovo sve što se u praksi
treba zaključiti, i obje govore o rasponu vrijednosti, a nijedna o
vjerojatnosti.

## Interakcija — Hvatač intervala

Prebrojavanje iz prethodnog odjeljka dalo je jednu brojku i sakrilo postupak koji
je do nje doveo. Widget taj postupak vraća na vidjelo, jer prikazuje same
intervale, jedan ispod drugoga, oko iste nepomične ciljne crte. Veličina uzorka i
razina pouzdanosti mijenjaju se odvojeno, pa se vidi da prva mijenja širinu
intervala, a druga mijenja i širinu i učestalost promašaja.

*Slika. Intervali iz ponovljenih simuliranih uzoraka oko fiksne populacijske sredine. Istaknuti intervali promašuju okomitu ciljnu crtu.*

**Što isprobati.**

1. Zadržite pedeset intervala i prebrojite one koji ne sijeku okomitu ciljnu crtu.
2. Povećajte broj intervala na sto bez promjene veličine uzorka ili razine pouzdanosti.
3. Usporedite širinu intervala pri uzorcima veličine dvadeset i sto.
4. Promijenite razinu pouzdanosti s devedeset na devedeset i devet posto te opišite odnos širine i obuhvata.

## Preciznost nasuprot pouzdanosti

Dva pomaka koja widget dopušta imaju vrlo različite učinke i lako ih je pobrkati
jer oba mijenjaju širinu. Veći uzorak sužava interval time što smanjuje
standardnu pogrešku, pa uz jednako obećanje o obuhvatu dobivamo precizniji
odgovor. Prosječna širina intervala pri uzorku od pedeset osoba iznosi
`r hr_broj(s9$sirine[["50"]], 2)` boda, pri dvjesto
`r hr_broj(s9$sirine[["200"]], 2)`, a pri osamsto
`r hr_broj(s9$sirine[["800"]], 2)`.

Viša razina pouzdanosti također širi interval, ali ništa ne dobiva na
preciznosti. Na istom našem uzorku raspon od 90 % širok je
`r hr_broj(s9$razine[["90"]], 2)` boda, onaj od 95 %
`r hr_broj(s9$razine[["95"]], 2)`, a onaj od 99 %
`r hr_broj(s9$razine[["99"]], 2)`. Podaci se nisu promijenili, promijenio se
zahtjev. Interval koji obuhvaća cilj u 100 % slučajeva postoji i proteže se od
minus do plus beskonačno, čime savršena pouzdanost postaje savršeno beskorisna.

**Preciznost** je zato svojstvo koje se plaća podacima, a **pouzdanost** je
svojstvo koje se bira i plaća širinom. Konvencija od 95 % nema dublje
opravdanje od uobičajenosti, i to je razlog više da se uz svaki interval navede
razina na kojoj je izračunat.

Širok interval ne znači loše obavljen posao. Češće znači mali uzorak ili
podatke koji su stvarno raspršeni, i tada je široki raspon iskren opis stanja, a
ne priznanje nesposobnosti. Suprotan je slučaj mnogo opasniji. Uzak interval
oko procjene iz pristranog uzorka izgleda kao preciznost, a jest sigurnost u
pogrešnu vrijednost, jer interval mjeri samo ono što bi se mijenjalo kroz
ponavljanja istoga postupka.

Iz širine slijedi i način na koji se intervali čitaju kada ih je više na istoj
slici, što je najčešći oblik u kojem ih društveni znanstvenik susreće. Grafovi
koji uz svaku skupinu crtaju raspon umjesto samog stupca odmah pokazuju koje su
procjene oslonjene na malo ljudi, a koje na mnogo, i time govore više od
tablice prosjeka. Iskušenje je da se iz njih očita i zaključak o razlici.

Pravilo koje se pritom obično primjenjuje nije simetrično i vrijedi to znati.
Kada se dva intervala uopće ne preklapaju, razlika među skupinama gotovo je
sigurno stvarna. Kada se preklapaju, iz toga ne slijedi da razlike nema, jer
umjereno preklapanje i dalje je uskladivo s pravom razlikom. Preklapanje je
zato slab dokaz u jednom smjeru i jak u drugom, a pošten odgovor traži interval
za samu razliku, a ne dva intervala jedan pokraj drugoga. Taj postupak knjiga
uvodi u poglavlju o usporedbi dviju grupa.

Postoji i druga zamjena koja se često javlja u istom odlomku. Interval
pouzdanosti govori gdje je prosjek, a ne gdje su ljudi. Za naš uzorak od
dvjesto osoba raspon oko sredine dug je
`r hr_broj(s9$gornja - s9$donja, 2)` boda, dok bi raspon unutar kojega leži
otprilike 95 % pojedinačnih ocjena bio širok približno
`r hr_broj(2 * s9$predikcijski, 1)` boda. Prvi se odnosi na parametar i sužava
se s uzorkom, drugi na buduće opažanje i ne sužava se gotovo nimalo.

*Slika. Interval pouzdanosti za sredinu i raspon unutar kojega leži otprilike 95 % pojedinačnih ocjena, na istom uzorku i istoj osi.*

## Bootstrap kao vlastiti izum

Sve dosad počiva na jednoj formuli za standardnu pogrešku, a ta formula postoji
samo za neke mjere. Za sredinu je poznata, za udio također, a za medijan,
razliku percentila ili omjer dviju mjera nije jednostavna ili je uopće nema.
Pitanje što učiniti kada formule nema ima odgovor koji se može smisliti bez
ijedne nove ideje, uz uvjet da se prethodno poglavlje shvatilo ozbiljno.

Standardna pogreška bila je definirana kroz ponovljene uzorke iz populacije.
Kad bismo populaciji imali pristup, izvukli bismo tisuću uzoraka, izračunali
tisuću medijana i pogledali koliko se razilaze. Populaciji pristupa nemamo,
imamo samo uzorak. Uzorak je pritom najbolja slika populacije kojom
raspolažemo, jer je iz nje izvučen slučajno i njezine razmjere nosi u sebi. Ako
mu dopustimo da privremeno glumi populaciju i iz njega izvlačimo nove uzorke
jednake veličine, dobit ćemo raspodjelu koja oponaša onu koju bismo dobili iz
prave populacije.

Izvlačenje mora biti s vraćanjem, i to nije tehnički detalj. Izvlačenjem bez
vraćanja iz uzorka od šezdeset osoba dobili bismo šezdeset istih osoba u drugom
poretku, pa bi svaki takav uzorak dao identičan medijan i raspodjela ne bi
imala nikakvu širinu. Vraćanjem opažanja u posudu dopuštamo da neka uđu
dvaput, a neka nijednom, i upravo ta promjena sastava oponaša promjenu sastava
koja nastaje pri izvlačenju iz populacije. Postupak nosi ime **bootstrap** i
uveden je kao način procjene nesigurnosti kada teorijski račun nije pri ruci
(Efron, 1979).

Uzmimo uzorak od `r hr_broj(s9$mali_n, 0)` osoba i pitajmo se koliko iznosi
medijan dnevnih minuta praćenja medija. U uzorku on iznosi
`r hr_broj(s9$medijan_uzorak, 1)` minuta. Četiri tisuće bootstrap uzoraka daju
raspon od `r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta,
unutar kojega leži prava populacijska vrijednost od
`r hr_broj(s9$medijan_pop, 1)` minuta.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću.*

Histogram ima vidljiv stubast oblik jer medijan uzorka od šezdeset brojeva može
poprimiti samo ograničen skup vrijednosti, što je svojstvo mjere, a ne mana
postupka. Snaga bootstrapa upravo je u tome što ga takve neugodnosti ne
zaustavljaju. Isti se postupak bez izmjene primjenjuje na sredinu, medijan,
korelaciju ili razliku dviju skupina, jer nigdje ne pretpostavlja oblik
raspodjele.

Njegova granica ostaje početni uzorak, i granica je stroga. Bootstrap ponovno
koristi opažanja koja već imamo, pa ne može otkriti dio populacije koji u
uzorak nikada nije mogao ući. Ako je uzorak prigodan, postupak će pouzdano
opisati promjenjivost pogrešne procjene. Ako je premalen da zabilježi rijetke
ali važne slučajeve, ta praznina ostaje u svakom od četiri tisuće ponavljanja.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživači su studentima i aktivnim
znanstvenicima predočili objavljeni interval pouzdanosti i uz njega šest
tvrdnji o njegovu značenju, među kojima nijedna nije bila točna (Hoekstra, 2014).
Velik dio ispitanika u svim skupinama, uključujući iskusne istraživače,
prihvatio je barem neke od njih.

Tvrdnje nisu bile besmislene, i u tome je poanta okvira. Sve su govorile o
vjerojatnosti da se prava vrijednost nalazi unutar granica, ili o tome koliko
je vjerojatno da bi se ponovljeno istraživanje unutar njih smjestilo. Postupak
koji smo izgradili takva obećanja ne daje, jer se njegov postotak odnosi na
udio intervala koje bi ponovljeno uzorkovanje proizvelo. Nalaz ne pokazuje da
su intervali loš alat nego da je rečenica kojom ih opisujemo teža od računa
koji ih proizvodi.

**Pitajte model.**
Asistent može bootstrapirati gotovo svaku statistiku i obično to učini
ispravno. Provjeravamo tri stvari koje redovito promakne. Uzorkuje li s
vraćanjem i na punoj veličini uzorka, jer bez toga raspodjela nema smisla. Čuva
li strukturu podataka, jer se kod uparenih ili grupiranih opažanja izvlače
jedinice, a ne redovi. Ponavlja li dovoljno puta, jer nekoliko stotina
ponavljanja daje granice koje se mijenjaju od pokretanja do pokretanja.
Najčešća pogreška ipak nije u kodu nego u zaključnoj rečenici, gdje se već
izračunatom intervalu pripiše vjerojatnost.

> Izračunaj točkastu procjenu i bootstrap interval. Uzorkuj s vraćanjem na
> punoj veličini uzorka, sačuvaj strukturu podataka i interpretiraj razinu
> pouzdanosti kao svojstvo ponovljenog postupka.

**Nađite grešku.**
Bootstrap raspodjela je približno simetrična i interval je uredno izračunat iz
njezinih krajeva. Postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

Greška je pripisivanje vjerojatnosti fiksnom parametru nakon izračuna
frekventističkog intervala. Prva rečenica je točna i postupak je proveden
ispravno. Razina pouzdanosti opisuje udio intervala koji obuhvaćaju parametar
kroz ponovljeno uzorkovanje, a ne položaj parametra u odnosu na ovaj raspon.

## Razrađeni primjer

Pitanje je ono koje bi postavio naručitelj istraživanja. Koliko vremena dnevno
stanovnici našega grada provode uz medije, i koliko je taj odgovor pouzdan ako
je anketirano šezdeset ljudi.

Prvi izbor nije statistički nego opisni. Dnevne minute imaju rep prema velikim
vrijednostima, a poglavlje o sažimanju podataka pokazalo je da prosjek takav
rep povlači za sobom, dok medijan ostaje kod tipičnog ispitanika. Za pitanje o
tome koliko medija prati uobičajena osoba medijan je pošteniji odgovor. Cijena
tog izbora vidi se tek sada, jer za sredinu postoji formula za standardnu
pogrešku, a za medijan ne postoji nijedna koja bi se dala napisati u jednom
retku. Upravo zato ovaj primjer i postoji.

Cijeli bootstrap stane u istu petlju koju je poglavlje o uzorkovanju već
pokazalo, uz jednu izmjenu. Umjesto iz populacije, izvlačimo iz uzorka, i to s
vraćanjem.

Poziv `sample` uz argument `replace` izvlači s vraćanjem i jedini je novi
element u odnosu na prethodno poglavlje, dok `quantile` odsijeca zadani udio
raspodjele s obje strane. Blok proizvodi upravo one tri brojke koje je odjeljak
o bootstrapu već naveo, jer je riječ o istoj analizi ispisanoj u cijelosti.

Odgovor naručitelju glasi da tipičan stanovnik prati medije oko
`r hr_broj(s9$medijan_uzorak, 1)` minuta dnevno, uz raspon od
`r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta koji
opisuje koliko bi se ta procjena mijenjala kroz ponovljena istraživanja iste
veličine. Raspon je širok gotovo `r hr_broj(s9$boot_gornja - s9$boot_donja, 0)`
minuta, što je pošten opis onoga što šezdeset ljudi može reći, i ujedno
najkorisnija brojka u cijelom izvještaju. Naručitelj koji je htio razlučiti
promjenu od deset minuta iz ovih podataka odgovor neće dobiti bez većeg uzorka.

Budući da populaciju poznajemo, možemo napraviti i ono što stvarno istraživanje
ne može. Prava vrijednost iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i nalazi
se unutar granica. Iz toga ne slijedi da postupak radi, jer bi i loš postupak
pogodio pokoji put. Ono što o postupku govori jest prebrojavanje deset tisuća
ponavljanja iz ranijeg odjeljka, a ovaj pojedinačni pogodak samo je jedan od
njih, viđen iznutra kako ga vidi istraživač.

Redoslijed kojim su tri brojke ispisane isti je onaj kojim se rezultat i
izvještava. Najprije dolazi procjena, jer je ona odgovor na postavljeno pitanje.
Zatim dolazi raspon, jer bez njega procjena tvrdi više nego što zna. Tek na
kraju dolazi ograda, koja ovdje kaže da su podaci simulirani, da je mjera
medijan, a ne prosjek, i da šezdeset ljudi nije mnogo. Ista tri koraka vrijede
za nalaz čija je populacija stvarna, s tom razlikom da se ondje srednji korak
mora izvesti bez ikakve mogućnosti provjere, i upravo zato mora biti izveden
pažljivo.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval pouzdanosti
uzima standardnu pogrešku i oblik koji je dao središnji granični teorem te oko
procjene gradi raspon čije obećanje pripada postupku, a ne pojedinačnom rasponu
koji imamo pred sobom. Preciznost se kupuje podacima, a pouzdanost se bira i
plaća širinom, pa uz svaki raspon mora stajati razina na kojoj je izračunat.
Bootstrap istu ideju oslobađa formule tako što uzorku dopušta da privremeno
glumi populaciju, i time otvara mjere za koje račun ne postoji, ne popravljajući
pritom nijednu slabost samoga uzorka. Sljedeće poglavlje uzima isti aparat i
mijenja mu pitanje, jer umjesto raspona usklađenog s podacima traži koliko su
podaci neobični pod jednom određenom pretpostavkom.

## Pojmovi

točkasta procjena (*point estimate*), interval pouzdanosti (*confidence
interval*), razina pouzdanosti (*confidence level*), preciznost (*precision*),
bootstrap (*bootstrap*), uzorkovanje s vraćanjem (*sampling with replacement*),
parametar (*parameter*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, i zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica. Predajte jedan odlomak.

### Računski

Upotrijebite widget Hvatač intervala. Postavite pedeset intervala pri uzorku od
četrdeset osoba i razini od 95 % pa zabilježite koliko ih promašuje cilj.
Ponovite mjerenje pri razini od 99 % i pri uzorku od sto šezdeset osoba,
mijenjajući svaki put samo jednu postavku. Predajte tablicu s tri retka u kojoj
su navedeni postavka, širina tipičnog intervala i broj promašaja te jednu
rečenicu o tome koja postavka mijenja preciznost, a koja učestalost promašaja.

### Kritički

Pronađite u medijskom izvještaju ili sažetku rada rečenicu koja tumači interval
pouzdanosti. Prosudite pripisuje li vjerojatnost parametru, brka li raspon
sredine s rasponom pojedinačnih opažanja ili je ispravna, i napišite verziju
koja je vjerna postupku bez gubitka informacije (Hoekstra, 2014). Predajte
izvornu rečenicu, prosudbu i ispravak.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira o pogrešci. Imenujte što je u njoj
točno, izdvojite jednu pogrešnu rečenicu i napišite frekventistički ispravnu
zamjenu koja zadržava razinu od 95 % i ne uvodi nove tvrdnje o podacima.
