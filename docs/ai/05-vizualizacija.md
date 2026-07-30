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

## Graf kao usporedba

Graf nije slika dodana nakon analize. On bira što će se uspoređivati položajem,
duljinom, površinom ili bojom. Položaj na zajedničkoj osi obično dopušta
precizniju usporedbu od površine kruga ili nagiba trodimenzionalnog stupca.
Izbor geometrije zato je izbor načina na koji će čitatelj vidjeti razliku.

Dobra vizualizacija počinje tvrdnjom. Za raspodjelu jedne brojčane varijable
treba prikaz koji čuva oblik. Za usporedbu kategorija treba zajednička početna
točka. Za odnos dviju brojčanih varijabli treba sačuvati pojedinačna opažanja.
Graf koji ne odgovara pitanju može biti uredan i potpuno neinformativan.

Gramatika grafike odvaja podatke, estetska svojstva, geometriju i koordinatni
sustav (Wickham, 2016). Ta ideja vrijedi i bez pisanja koda. Omogućuje da
svaku odluku pregledamo zasebno i pitamo prenosi li značenje ili samo dekorira.

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
Graf prikazuje udjele triju kategorija stupcima na zajedničkoj osi koja počinje
od nule. Kategorije su jasno označene i vrijednosti su ispisane. Za veći dojam
razlike treću kategoriju treba prikazati širom od ostalih.

Greška je različita širina stupca. Površina tada dodaje drugo vizualno značenje
i pojačava razliku koja bi trebala biti kodirana samo duljinom.

## Razrađeni primjer

Podaci `anscombe` ugrađeni su u R i reproduciraju objavljeni kvartet
(Anscombe, 1973). Sažeci četiriju parova gotovo su jednaki. Raspršeni prikazi
zato nose dio analize koji tablica ne može sačuvati.

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

Upotrijebite ugrađene podatke `anscombe`. Izračunajte iste sažetke za sva
četiri skupa i predajte ih uz jednu zajedničku sliku (Anscombe, 1973).

### Kritički

Prosudite što Anscombeov kvartet pokazuje, a što ne pokazuje o ulozi korelacije
(Anscombe, 1973). Predajte odlomak s jednom dopuštenom i jednom pretjeranom
tvrdnjom.

### Revizija modela

Ocijenite prijedlog modela iz okvira. Imenujte točne elemente grafa, jednu
obmanjujuću odluku i način njezina popravka.
