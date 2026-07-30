# Sažimanje podataka

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/04-sazimanje-podataka.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | Oblikovanje distribucije | simulacija | pogl. 1 do 3 |

**Vinjeta.**
Tukey je istraživačku analizu podataka postavio kao postupak u kojem sažetak
otvara pitanja umjesto da ih zatvara (Tukey, 1977). Isti prosjek može pripadati
zbijenoj skupini sličnih opažanja ili raspodjeli u kojoj se većina nalazi
daleko od nekoliko ekstremnih vrijednosti. Broj je u oba slučaja pravilno
izračunat, ali iskustvo tipičnog opažanja nije isto.

U društvenim podacima takva razlika mijenja zaključak. Prosječno vrijeme,
prihod ili broj dijeljenja može snažno povući mala skupina iznimnih slučajeva.
Medijan će ostati stabilniji, ali će zauzvrat zanemariti koliko su ti slučajevi
daleko od sredine.

Koji sažetak čuva ono što je važno u raspodjeli, a što pritom skriva?

## Središte i raspodjela

**Aritmetička sredina** raspoređuje ukupan zbroj ravnomjerno na sva opažanja.
Zato koristi svaku vrijednost i zato je osjetljiva na krajnosti. **Medijan**
traži srednje mjesto nakon poredavanja. On se manje mijenja kada se jedno
opažanje udalji, ali ne govori koliko je udaljeno. Mod opisuje najčešću
vrijednost ili kategoriju i osobito je koristan kada prosjek uopće nema
sadržajno značenje.

Mjera središta ne opisuje koliko se opažanja razlikuju. Dvije skupine mogu
imati jednaku sredinu, a jedna može biti gotovo jednolična dok druga pokriva
širok raspon. Raspon koristi samo krajeve. Interkvartilni raspon prati srednju
polovinu raspodjele. Standardna devijacija opisuje tipičnu udaljenost od
aritmetičke sredine i zbog toga se mijenja zajedno s ekstremnim vrijednostima.

Izbor se ne svodi na pitanje koja je mjera najbolja. Sredina i raspršenost
moraju odgovarati obliku podataka i tvrdnji koju želimo poduprijeti. Kada je
raspodjela asimetrična, medijan i interkvartilni raspon često bolje opisuju
tipično opažanje. Kada je približno simetrična, sredina i standardna devijacija
zajedno daju sadržajan prikaz.

## Položaj unutar skupine

Ponekad nas ne zanima samo sirova vrijednost, nego njezin položaj u odnosu na
druge. **Standardizirana vrijednost** izražava koliko je standardnih devijacija
opažanje udaljeno od sredine. Time vrijednosti na različitim ljestvicama
prevodimo na zajednički jezik položaja, ali ne uklanjamo nepravilnosti
raspodjele.

Desno asimetrični podaci često nastaju kada nekoliko slučajeva može biti vrlo
veliko, dok je donja granica prirodna. Logaritamska transformacija sabija veće
vrijednosti i može učiniti omjere vidljivijima. Ona nije popravak za svaki
neugodan graf. Promijenjena ljestvica mijenja pitanje, pa interpretacija mora
govoriti o razmjernim, a ne apsolutnim razlikama.

## Interakcija — Oblikovanje distribucije

Oblikovatelj raspodjele pomiče jedno krajnje opažanje i širi preostalih devet
oko njihova zajedničkog središta. Sredina, medijan i dvije mjere raspršenosti
mijenjaju se pred čitateljem. Tako postaje vidljivo koje mjere slušaju svaku
vrijednost, a koje prvenstveno čuvaju redoslijed.

*Slika. Reakcija mjera središta i raspršenosti na oblik konstruirane raspodjele.*

**Što isprobati.**

1. Spustite krajnje opažanje sa 70 na 14 i usporedite sredinu s medijanom.
2. Vratite ga na 70 i provjerite koja se mjera središta više pomaknula.
3. Postavite krajnje opažanje na 11 pa povećajte faktor raspršenosti i
   usporedite dvije raspodjele iste sredine.

**Statistika u divljini.**
**Prosjek kao početak pregleda.** Tukey je zagovarao istraživački pristup u
kojem se podaci pregledavaju iz više kutova prije konačnog modeliranja
(Tukey, 1977). Izvještaj koji navodi samo prosjek uklanja upravo oblik koji bi
mogao objasniti zašto taj prosjek nije tipičan.

Odgovorna tablica zato uparuje mjeru središta s mjerom raspršenosti i brojem
opažanja. Graf zatim pokazuje asimetriju, praznine i krajnje slučajeve koje tri
sažetka ne mogu nositi.

**Pitajte model.**
Asistent može izraditi tablicu sažetaka, ali mu treba zatražiti broj valjanih
opažanja i postupanje s nedostajućim vrijednostima. Treba provjeriti računa li
svaku skupinu iz ispravnog podskupa i je li za asimetričnu raspodjelu ponudio
mjeru koja opisuje tipično opažanje.

> Sažmi svaku skupinu brojem opažanja, prikladnom mjerom središta i prikladnom
> mjerom raspršenosti. Obrazloži izbor nakon pregleda oblika raspodjele i
> prikaži koliko vrijednosti nedostaje.

**Nađite grešku.**
Raspodjela broja dijeljenja izrazito je desno asimetrična. Medijan i
interkvartilni raspon zato opisuju tipičnu objavu. Budući da je medijan otporan
na krajnje vrijednosti, takve vrijednosti možemo ukloniti prije svake daljnje
analize.

Greška je automatsko uklanjanje krajnjih vrijednosti. Otpornost medijana
objašnjava njegovu stabilnost, ali ne određuje jesu li krajnji slučajevi
pogreške, legitimna opažanja ili predmet istraživanja.

## Razrađeni primjer

Simulirani niz predstavlja angažman objava. Jedna objava privukla je mnogo više
reakcija od ostalih. Usporedba sredine i medijana pokazuje kako taj slučaj
mijenja pojam tipične objave, dok interkvartilni raspon opisuje središnji dio
raspodjele.

*Slika. Sažeci simulirane raspodjele angažmana. Izrada autora.*

Nijedan sažetak nije pogrešan. Sredina odgovara na pitanje o ravnomjernoj
raspodjeli ukupnog angažmana, a medijan o položaju srednje objave. Izvještaj
treba imenovati pitanje i pokazati raspodjelu kako čitatelj ne bi morao
nagađati koje značenje nosi riječ „prosječno".

## Sažetak

Sažetak je odluka o tome koji dio raspodjele čuvamo u malom broju vrijednosti.
Mjera središta bez raspršenosti ostavlja pola priče neispričanom, a obje zajedno
još ne pokazuju oblik. Standardizacija opisuje položaj, dok transformacija
mijenja ljestvicu i traži novu interpretaciju. Sljedeće poglavlje zato podatke
vraća u prostor i pokazuje kako graf postaje dio argumenta.

## Pojmovi

aritmetička sredina (*mean*), medijan (*median*), interkvartilni raspon
(*interquartile range*), standardna devijacija (*standard deviation*),
standardizirana vrijednost (*z-score*), asimetrija (*skewness*)

## Zadaci

### Konceptualni

Predvidite kako će se sredina, medijan i interkvartilni raspon promijeniti kada
jedno najveće opažanje dodatno poraste. Predajte obrazloženje bez računanja.

### Računski

Upotrijebite `sim_angazman`. Izračunajte sažetke prije i nakon uklanjanja
najveće vrijednosti te predajte jednu usporednu tablicu.

### Kritički

Objasnite zašto istraživačka analiza ne završava jednom mjerom središta
(Tukey, 1977). Predajte popis triju dodatnih provjera u punim rečenicama.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dobar izbor sažetka, jednu
neopravdanu odluku i postupak kojim biste je provjerili.
