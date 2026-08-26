# Predgovor

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/00-predgovor.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

**Vinjeta.**
Pri provjeri nastavnoga skupa za ovu knjigu pred nama je bilo nekoliko redaka o
glavnom izvoru vijesti. Redak za portale bio je veći od svakoga drugog retka. Iz
toga su nastale dvije naizgled slične rečenice. Prema prvoj je portal najčešći
glavni izvor vijesti, a prema drugoj je portal glavni izvor vijesti većini
generirane populacije.

Takva razlika ne traži naprednu matematiku. Traži da se broj vrati pitanju,
usporedbi i nazivniku prije nego što postane zaključak. Koju od dviju rečenica
podaci doista podupiru?

## Tvrdnja pod povećalom

Tablica prikazuje cijelu poznatu generiranu populaciju od 50.000 zapisa, a ne
uzorak stvarnih ljudi (Šikić, 2026). Jedan redak predstavlja
jednu generiranu osobu, a kategorije se međusobno isključuju.

| Glavni izvor vijesti | Broj zapisa | Udio u populaciji |
|---|---:|---:|
| portal | 15.101 | 30,202 % |
| društvene mreže | 13.378 | 26,756 % |
| TV | 10.827 | 21,654 % |
| radio | 5.839 | 11,678 % |
| tisak | 4.855 | 9,710 % |

: Izvori vijesti u poznatoj generiranoj populaciji. Izrada autora prema sikic2026.

Skup je generiran upravo zato da poznajemo cijelu populaciju i možemo
provjeriti svaki zbroj. On ne govori ništa o medijskim navikama stvarnih ljudi.
Za početni je zadatak dovoljno pregledati sve retke, usporediti najveći
broj s ostalima i zatim ga usporediti s polovicom ukupnoga broja zapisa. Najveći
redak i većinski udio traže dvije različite usporedbe.

## Ugovor s čitateljem

Ova je knjiga namijenjena studentima društvenih znanosti koji moraju razumjeti
istraživanje, a ne postati profesionalni analitičari. Ne pretpostavlja
programiranje ni matematiku izvan srednjoškolskog gradiva. Pretpostavlja
spremnost da se svaka tvrdnja uspori dovoljno dugo kako bismo vidjeli podatke,
usporedbu i neizvjesnost.

**Statistička pismenost** ovdje obuhvaća četiri sposobnosti. Čitatelj može
kritički prosuditi statističku tvrdnju. Može pošteno opisati i prikazati podatke
te čitati i skromno reproducirati temeljne inferencijalne analize. Može
surađivati s asistentom bez predaje odgovornosti. Taj put vodi od statističkog
mišljenja preko opisivanja i uzorkovanja do zaključivanja, modela i predviđanja.

**Simulacija** dolazi prije formule. Rezultat najprije promatramo dok se podaci
ili slučajni postupak mijenjaju, a tek ga potom imenujemo. **Procjena** i njezina
neizvjesnost dolaze prije testa jer broj čitamo zajedno s rasponom vrijednosti
koje su spojive s podacima. Čitanje tuđih brojki ravnopravan je sadržaj, a ne
motivacijska digresija.

AI asistent može pomoći u svakom koraku, ali snižava cijenu uvjerljiva računa i
time povećava teret neovisne provjere. Račun se može delegirati. Čovjek određuje
pitanje, uspoređuje izlaz s izvorom i potpisuje zaključak. Tu granicu nazivamo
**podjelom odgovornosti s asistentom**.

## Granice i putovi čitanja

Knjiga ne obuhvaća vremenske nizove, faktorsku analizu, psihometriju,
višerazinske modele ni punu Bayesovsku inferenciju. Strojno učenje pojavljuje
se kroz ideje i društvene posljedice, a ne kroz matematičku izgradnju
algoritama. Granica nije tvrdnja da te teme nisu važne, nego odluka da se
obećani put može završiti.

Digitalno izdanje nosi interaktivne prikaze, a tiskano njihove statične
blizance. R praktikum prati provjerenu samostalnu R-rutu, dok je put bez koda
ograničen na 19 podržanih mjerila iz verzioniranog popisa u Dodatku B. Sedam
ograđenih mjerila nije dio toga obećanja, a provjera na čistoj instalaciji još
nije potvrđena. Katalog podataka pokazuje podrijetlo skupova, vodič pomaže pri
odabiru postupka, rječnik povezuje pojmove, a protokol uređuje rad s
asistentom.

### Kritičko-čitalački put

Poglavlja 1–18 čitaju se kanonskim redoslijedom. Poseban je naglasak na
tvrdnjama, izvorima, grafovima i granicama tumačenja u poglavljima 1, 2, 3, 5,
8, 10, 12, 13, 17 i 18. Naglasak usmjerava pozornost, ali ostala poglavlja
nisu preskočiva. Živi preduvjeti vode kroz cijelu knjigu, Poglavlje 13 dolazi
prije Poglavlja 17, a Poglavlje 18 tek nakon svih sedamnaest prethodnih.

### Analitički put

Poglavlja 1–18 i ovdje se čitaju kanonskim redoslijedom, uz naglasak na
podacima, postupcima i provjerljivim rezultatima u poglavljima 1, 2, 4–11,
13–16 i 18. Dodatak A prati provjerenu R-rutu, a Dodatak B samo svoj
dokumentirani opseg bez koda. Oba se puta susreću u provjerljivom tragu računa
jer se sud o tuđem rezultatu ne može trajno odvojiti od razumijevanja kako je
nastao.

Nakon vlastitog pokušaja čitatelj može otvoriti [Provjere
rješenja](../rjesenja.qmd). Javna stranica donosi sažete provjere, dok puni
kriteriji, prihvatljive alternative i napomene nastavniku pripadaju samo
zaštićenom kolegijskom sloju.

Svaki broj iz proze mora ostaviti **provjerljiv trag računa** do podataka i
postupka kojim je dobiven. Predgovor i prvi dio ne prikazuju vidljivi kod, a
nijedna ocijenjena aktivnost u knjizi ne traži njegovo pisanje. Trag računa
ipak ne jamči da su podaci prikladni, dizajn valjan ili tumačenje pošteno. On
omogućuje provjeru računanja, ne zamjenjuje prosudbu.

**Statistika u divljini.**
**Jedan broj nije presuda.** Američko statističko udruženje u izjavi o
p-vrijednostima razdvaja prelazak unaprijed zadanog praga od znanstvenog
zaključka. P-vrijednost sama ne pokazuje veličinu učinka ni važnost rezultata,
pa zaključak ne smije počivati samo na prelasku praga
(Wasserstein, 2016).

**Pitajte model.**
Asistent može provjeriti račun iz tablice, ali zadatak mora imenovati brojnik,
nazivnik i usporedbu. Rezultat zatim uspoređujemo s izvornim retkom i ručno
provjeravamo zaključak. Ovaj nastavni skup nema stvarne ispitanike, a stvarni
osobni podaci ne prenose se javnom modelu.

> Izračunaj udio zapisa kojima je portal glavni izvor vijesti. Imenuj brojnik i
> nazivnik, usporedi rezultat s polovinom populacije i napiši što iz ove
> generirane populacije ne smijemo zaključiti o stvarnim ljudima.

**Nađite grešku.**
Portal je glavni izvor vijesti za 15.101 od 50.000 zapisa, odnosno 30,202 %
(Šikić, 2026).
To je više nego u bilo kojoj drugoj kategoriji (Šikić, 2026), pa većina ove
generirane populacije ima portal kao glavni izvor vijesti. Rezultat se ne odnosi
na stvarne ljude.

## Razrađeni primjer

Tvrdnja da je portal najčešći izvor traži usporedbu njegova broja sa svakim
drugim retkom. Broj 15.101 veći je od 13.378, 10.827, 5.839 i 4.855, pa je ta
tvrdnja točna za poznatu generiranu populaciju (Šikić, 2026).

Tvrdnja o većini traži drugu usporedbu. Polovina od 50.000 iznosi 25.000, a
broj 15.101 manji je od toga (Šikić, 2026). Isti se odnos vidi u računu
$15\,101 / 50\,000 = 0{,}30202$, odnosno 30,202 %
(Šikić, 2026). Pošten zaključak glasi da su portali najčešća
pojedinačna kategorija, ali nisu izvor većine zapisa.

Ta usporedba razdvaja najčešću kategoriju od većine. Budući da tablica obuhvaća
svih 50.000 zapisa poznate generirane populacije, o udjelu portala u tim
zapisima nema uzorkovne neizvjesnosti (Šikić, 2026). Podrijetlo i konstrukcija
skupa ipak ograničavaju tumačenje, pa nema temelja da se udio prenese na stvarne
ljude. Poglavlje o životnom ciklusu podataka smjestit će ista pitanja u širi put
od nastanka podatka do nadzora nad zaključkom.

## Sažetak

Statistička pismenost povezuje pitanje, podatke, usporedbu, neizvjesnost i
ograničen zaključak. Simulacija i procjena čine postupke vidljivima, a
provjerljiv trag računa omogućuje da se delegirano računanje pregleda. Podjela
odgovornosti s asistentom ostavlja pitanje, provjeru izvora i zaključak čovjeku.
Prvo poglavlje započinje životnim ciklusom koji svakom od tih poslova određuje
mjesto.

## Pojmovi

statistička pismenost (*statistical literacy*), simulacija (*simulation*),
procjena (*estimation*), podjela odgovornosti s asistentom (*division of
responsibility with an assistant*), provjerljiv trag računa (*auditable
calculation trail*)

## Zadaci

### Konceptualni

Kritičko-čitalački i analitički put različito ulaze u isti problem. U tri
rečenice objasnite od čega svaki put polazi, gdje se susreću u provjerljivom
tragu računa i koja odgovornost ostaje čitatelju kada račun predloži asistent.

### Računski

Izračunajte udio zapisa kojima su društvene mreže glavni izvor vijesti i
usporedite ga s udjelom portala. Predajte račun s brojnikom i nazivnikom te
jednu rečenicu zaključka, bez pisanja koda.

### Kritički

Prosudite objavljenu tvrdnju iz okvira „Jedan broj nije presuda”. Predajte dvije
rečenice. U prvoj navedite što prelazak zadanog praga sam po sebi ne pokazuje, a
u drugoj imenujte jedan dodatni podatak ili argument koji biste morali provjeriti
prije znanstvenog zaključka
(Wasserstein, 2016).

### Revizija modela

Model predlaže ovu analizu. „Društvene mreže glavni su izvor vijesti za
13.378 od 50.000 zapisa, odnosno 26,756 % (Šikić, 2026). Zaključak se odnosi samo
na generiranu populaciju. Budući da je račun jasno zapisan, nije ga potrebno
neovisno usporediti s izvornom tablicom.” Ocijenite analizu. Predajte dva točna
elementa, jedinu pogrešku, potrebnu ljudsku provjeru i jednu rečenicu o tome što
provjerljiv trag računa ne jamči.
