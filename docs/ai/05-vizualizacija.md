# Vizualizacija kao argument

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/05-vizualizacija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Isti podaci, četiri grafa | Anscombeov kvartet | pogl. 4 |

**Vinjeta.**
Anscombe je sastavio četiri skupa podataka s gotovo jednakim uobičajenim
brojčanim sažecima, uključujući isti linearni odnos, ali s posve različitim
grafičkim oblicima (Anscombe, 1973). Jedan je pokazivao približno linearan
obrazac, drugi zakrivljenost, treći utjecajnu točku, a četvrti gotovo okomiti
oblak s jednim izdvojenim opažanjem.

Tablica sažetaka nije sadržavala računsku pogrešku. Upravo je zato primjer bio
uvjerljiv. Četiri različite priče stale su u iste brojke jer sažeci nisu mogli
sačuvati položaj svakog opažanja.

Kada graf razjašnjava podatke, a kada ih pretvara u argument koji prikriva
vlastite odluke?

## Gramatika grafike

Graf nije slika dodana nakon analize. On bira što će se uspoređivati položajem,
duljinom, površinom ili bojom, pa je izbor prikaza ujedno izbor načina na koji
će čitatelj vidjeti razliku. Dobra vizualizacija zato počinje tvrdnjom.
Raspodjela jedne brojčane varijable traži prikaz koji čuva oblik, usporedba
kategorija zajedničku početnu točku, a odnos dviju brojčanih varijabli sačuvana
pojedinačna opažanja. Graf koji ne odgovara pitanju može biti uredan i potpuno
neinformativan.

Uobičajeni popis vrsta grafova, u kojem stupčani dijagram stoji uz kružni i
raspršeni, pritom skriva jednu važnu činjenicu. Vrsta grafa nije osnovna jedinica.
Svaki je prikaz skup odvojenih odluka koje se u praksi tako često pojavljuju
zajedno da je njihova kombinacija dobila ime. **Gramatika grafike** razdvaja te
odluke i time svaku izlaže zasebnoj provjeri (Wickham, 2016). Sama ideja ne
pripada nijednom programu i primjenjuje se bez pisanja koda.

Najprije treba znati što predstavlja jedna oznaka na grafu. Točka može stajati
za ispitanika, državu, godinu ili stranku, a prikazi tu jedinicu mijenjaju bez
najave. Kada agregat zamijeni pojedinca, mijenja se i pitanje na koje graf
odgovara, što je ista opasnost koju opisuje poglavlje o mjerenju i dizajnu.

Sljedeći korak pridružuje varijable vizualnim kanalima, položaju na dvjema
osima, boji, veličini i obliku. **Pridruživanje** je tvrdnja o tome što
zaslužuje usporedbu. Kada skupinu nosi boja, graf poziva na neposrednu usporedbu
skupina. Kada je skupina razdvojena u zasebna polja, graf traži da se obrazac
čita unutar svake od njih. Podaci ostaju isti, argument se mijenja, a obmane
nije bilo.

Najtiša odluka dolazi prije crtanja. Graf redovito nešto izračuna prije nego što
postavi prvu oznaku. Stupac visine prosjeka odbacio je raspodjelu, okvir s
brkovima izgubio je informaciju o broju vrhova, a izglađena linija dodala je
model koji nitko nije zatražio. Poglavlje o sažimanju pokazalo je koji sažetak
što gubi, a gramatika tome dodaje da je i sam graf redovito sažetak, samo
neoznačen. Anscombeov kvartet poseban je slučaj upravo tog pravila
(Anscombe, 1973).

Izbor oznake koja nosi usporedbu određuje preciznost koju čitateljevo oko može
postići. Trodimenzionalni kružni dijagram nije neuredan, nego nudi usporedbu
koju istraživanja grafičke percepcije nalaze manje pouzdanom od usporedbe
položaja na zajedničkoj osi, pa pripada istoj obitelji postupaka kao skraćena os
iz poglavlja o zavaravanju brojkama.

Ljestvica je pravilo kojim vrijednost postaje vizualna veličina. Raspon osi,
njezin prekid, logaritamska transformacija i položaj sredine u ljestvici boja
mijenjaju koliko promjena zauzima prostora, a podatke pritom ne mijenjaju.

Ostaje odluka o tome hoće li se skupine preslagati jedna preko druge ili
razdvojiti u ponovljena polja. Mala višestruka polja čuvaju zajedničku ljestvicu
i pokazuju raznolikost koju jedna prosječna linija skriva, pa su vizualni oblik
iste pojave koju je Simpson opisao brojčano (Simpson, 1951). Koordinatni sustav
zatvara popis i najčešće služi kao opomena, jer polarne koordinate duljinu
pretvaraju u kut i time istu usporedbu čine težom.

Iz tih odluka slijedi postupak za čitanje tuđega grafa. Što predstavlja jedna
oznaka, što je pridruženo kojem kanalu, što je izračunato prije crtanja i što
dopušta ljestvica jesu pitanja koja se pred novinskom grafikom postavljaju bez
ikakva programa. Knjiga taj postupak dalje koristi pri svakom rastavljanju
objavljene tvrdnje.

## Poštena vidljivost

Osi određuju koliko će promjena zauzeti prostora. Skraćena os može biti
opravdana kada želimo vidjeti male razlike, ali prekid mora biti vidljiv, a
tvrdnja ne smije glumiti promjenu od nule. Kod stupaca je zajedničko ishodište
posebno važno jer duljina nosi značenje. Kod linijskog grafa raspon može
slijediti podatke, ali vremenski i sadržajni kontekst moraju ostati čitljivi.

Mala višestruka polja ponavljaju isti graf za skupine i time čuvaju zajedničku
ljestvicu. Ona često pokazuju heterogenost koju jedna prosječna linija skriva.
Pristupačnost traži dodatni korak. Boja ne smije biti jedini nosač značenja,
tekst mora opisati uzorak, a graf treba preživjeti crno-bijeli tisak.

## Interakcija — Isti podaci, četiri grafa

Interakcija prikazuje iste simulirane podatke četirima geometrijama. Promjena
grafa ne mijenja opažanja, ali mijenja usporedbu koja postaje laka ili teška.
Čitatelj tako bira prikaz prema tvrdnji, a ne prema dojmu atraktivnosti.

*Slika. Isti simulirani podaci prikazani odabranom geometrijom. Izbor prikaza mijenja vidljivu usporedbu, ne opažanja.*

**Što isprobati.**

1. Odaberite raspršeni dijagram i opišite odnos varijabli bez sažimanja po skupinama.
2. Prijeđite na histogram i utvrdite koja je prethodna informacija nestala.
3. Usporedite raspodjelu po skupinama s prikazom njihovih sredina.
4. Odaberite graf za tvrdnju o razlikama među tipičnim ishodima i obrazložite izbor.

**Statistika u divljini.**
**Četiri jednaka sažetka.** Anscombeov kvartet pokazuje da jednake sredine,
standardne devijacije i korelacije ne jamče jednaku strukturu podataka
(Anscombe, 1973). Raspršeni dijagram odmah razdvaja linearnost, zakrivljenost i
utjecaj izdvojenog opažanja.

Pouka nije da brojeve zamijenimo slikom. Tablica i graf provjeravaju različite
dijelove iste tvrdnje. Njihovo neslaganje razlog je za novu analizu, ne za
odabir prikaza koji nam se više sviđa.

**Pitajte model.**
Asistent može predložiti geometriju i napisati alt-tekst, ali treba dobiti
pitanje koje graf mora odgovoriti. Nakon izrade provjeravamo zajedničke osi,
nazive jedinica, redoslijed kategorija i nosi li boja značenje koje nestaje u
tisku. Modeli često dodaju ukrase koji povećavaju gustoću, a ne razumijevanje.

> Predloži najjednostavniji graf za ovu tvrdnju. Obrazloži koja usporedba nosi
> zaključak, navedi potrebnu ljestvicu i napiši alt-tekst bez tumačenja koje
> podaci ne podupiru.

**Nađite grešku.**
Za usporedbu udjela triju kategorija asistent je predložio ovaj poziv.

Os počinje od nule, kategorije su označene, a vrijednosti stoje uz stupce. Šira
treća kategorija, prema obrazloženju, samo popravlja optičku ravnotežu prikaza.

Greška je različita širina stupca. Površina tada nosi drugo vizualno značenje i
pojačava razliku koja bi trebala biti kodirana samo duljinom.

## Razrađeni primjer

Zadatak je provjeriti koliko brojčani sažetak sam po sebi jamči o strukturi
podataka. Anscombeovi su skupovi za to izabrani zato što su im sažeci gotovo
jednaki po konstrukciji (Anscombe, 1973), pa ostaje samo pitanje što prikaz
dodaje. Podaci `anscombe` ugrađeni su u R i reproduciraju objavljeni kvartet.

Prvi blok slaže četiri skupa u jednu tablicu s jednim opažanjem u svakom redu.
Drugi ispisuje odluke gramatike u redoslijedu u kojem smo ih izgradili. Poziv
`aes` pridružuje varijable osima, `geom_point` bira oznaku, `geom_smooth` dodaje
izračun koji nastaje prije crtanja, a `facet_wrap` razdvaja skupove u ponovljena
polja. Dodani pravac je onaj najmanjih kvadrata, u izvornom radu jednak u sva
četiri skupa (Anscombe, 1973), a poglavlje o regresiji pokazuje kako se dobiva.
Nakon ovog imenovanja svaki se graf u knjizi može pročitati bez novoga
objašnjenja, jer se iste četiri odluke vraćaju u svakom pozivu.

Anscombeov kvartet s jednakim sažecima i različitim oblicima. Izrada autora
prema anscombe1973.

Prvi skup približno odgovara linearnoj priči. Drugi traži zakrivljeni opis.
Treći i četvrti pokazuju koliko jedno opažanje može određivati pravac.
Zaključak zato ne glasi da je korelacija beskorisna. Glasi da se brojčani
sažetak čita uz prikaz strukture iz koje je nastao.

## Sažetak

Vizualizacija kodira usporedbe i zato pripada argumentu, a ne ukrasu. Izbor
geometrije, ljestvice i podjele na skupine određuje koji obrazac postaje
vidljiv. Pošten graf čuva kontekst, ostaje čitljiv bez boje i ne dodjeljuje
vizualnu težinu bez podatkovnog značenja. Sljedeće poglavlje iz tog prikaza
izdvaja mjeru povezanosti i ispituje što ona može sažeti.

## Pojmovi

geometrija grafa (*geom*), ljestvica (*scale*), mala višestruka polja (*small
multiples*), pristupačnost (*accessibility*), alt-tekst (*alternative text*),
utjecajno opažanje (*influential observation*)

## Zadaci

### Konceptualni

Odaberite graf za raspodjelu jedne varijable, usporedbu kategorija i odnos
dviju brojčanih varijabli. Predajte tri izbora s obrazloženjem.

### Računski

Upotrijebite interakciju poglavlja. Za svaki od četiriju prikaza zapišite što
čuva, što izračunava prije crtanja i koju usporedbu olakšava, a zatim iste
odluke pročitajte s Anscombeovih prikaza iz razrađenog primjera (Anscombe, 1973).
Predajte tablicu s četirima redovima i jednom rečenicom obrazloženja u svakom.
Postupak za ponavljanje izračuna nad cijelim skupom nalazi se u praktikumu.

### Kritički

Prosudite što Anscombeov kvartet pokazuje, a što ne pokazuje o ulozi korelacije
(Anscombe, 1973). Predajte odlomak s jednom dopuštenom i jednom pretjeranom
tvrdnjom.

### Revizija modela

Ocijenite prijedlog modela iz okvira. Imenujte odluke gramatike koje su
ispravno odgovorene, jednu koja obmanjuje, redak koda u kojem ta odluka stoji i
način njezina popravka.
