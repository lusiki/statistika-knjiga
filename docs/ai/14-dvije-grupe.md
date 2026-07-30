# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Uzorkivač dviju grupa | simulacija | pogl. 4, 9–11 |

**Vinjeta.**
Cumming je usporedbu skupina smjestio u okvir procjene razlike i njezina
intervala, umjesto odluke koja završava oznakom značajnosti (Cumming, 2014).
Time se uredničko pitanje mijenja. Nije dovoljno znati prolazi li rezultat
prag. Treba znati kolika je razlika i koje su veličine još spojive s podacima.

Isti brojčani ishod može nastati iz dviju neovisnih skupina, iz ponovljenog
mjerenja istih osoba ili iz usporedbe jednog uzorka s referentnom vrijednošću.
Računi izgledaju srodno, ali jedinica neovisnosti nije ista.

Kako jednu usporedbu dviju sredina povezati s dizajnom, učinkom i općim jezikom
modela?

## Jedna razlika, tri dizajna

Jednouzoračni t-test uspoređuje sredinu uzorka s referentnom vrijednošću.
Neovisni t-test uspoređuje dvije skupine različitih jedinica. Upareni t-test
svodi ponovljena mjerenja na razliku unutar iste jedinice i analizira te
razlike. Odabir testa zato počinje pitanjem tko ili što nosi dva rezultata.

Welchova inačica neovisnog testa ne zahtijeva jednake varijance i razuman je
početni izbor kada nema snažnog razloga za strožu pretpostavku. Normalnost se
procjenjuje na razini ostataka ili razlika relevantnih za model, a ne
mehaničkim testom nad svakim stupcem.

Krajnja opažanja traže pregled, ne automatsko brisanje. Mogu biti pogreške,
rijetki legitimni slučajevi ili znak da sredina nije prikladan sažetak.
Wilcoxonov postupak mijenja pitanje prema rangovima i nije samo t-test koji se
uključuje kada jedan test normalnosti prijeđe prag.

## Binarni prediktor kao model

Usporedba dviju skupina može se zapisati linearnim modelom u kojem kategorija
predviđa brojčani ishod. Početna vrijednost predstavlja sredinu referentne
skupine, a koeficijent skupine njihovu razliku. Time t-test postaje poseban
slučaj jezika koji će se proširiti u poglavlju o regresiji.

Model ne zamjenjuje dizajn. Koeficijent opisuje prilagođenu ili neprilagođenu
razliku ovisno o uključenim varijablama, dok kauzalno značenje dolazi iz načina
dodjele skupina. Izvještaj najprije daje razliku u izvornim jedinicama i
interval, zatim test i standardiziranu veličinu učinka.

## Interakcija — Uzorkivač dviju grupa

Uzorkivač dviju grupa prikazuje preklapanje pojedinačnih rezultata i
raspodjelu procijenjene razlike kroz ponavljanja. Čitatelj odvojeno mijenja
stvarnu razliku, varijabilnost i veličinu uzorka. Uparena simulacija zadržava
fiksnu pozitivnu povezanost dvaju mjerenja iste jedinice.

*Slika. Jedan simulirani uzorak dviju skupina i raspodjela procijenjene razlike kroz ponovljene uzorke.*

**Što isprobati.**

1. Povećajte razliku uz jednaku varijabilnost.
2. Povećajte varijabilnost uz jednaku razliku.
3. Povećajte uzorak bez promjene razlike i varijabilnosti.
4. Pretvorite neovisni dizajn u upareni i usporedite raspodjelu procjena.

Preklapanje pojedinačnih ishoda i preciznost procijenjene razlike nisu ista
stvar. Uparivanje povećava preciznost samo kada analiza sačuva vezu između
dvaju mjerenja iste jedinice.

**Statistika u divljini.**
**Interval umjesto etikete.** Pristup usmjeren na procjenu traži razliku i
interval prije zaključka o testu (Cumming, 2014). Dvije studije mogu imati sličnu
procjenu, ali različitu preciznost, pa će binarna oznaka sakriti ono što ih
najviše razlikuje.

Graf pojedinačnih opažanja dodatno pokazuje preklapanje i krajnje slučajeve.
Sredine bez raspodjela pretvaraju dvije skupine u dvije točke.

**Pitajte model.**
Asistent može odabrati t-test tek nakon što dobije opis dizajna i identifikator
jedinice. Treba provjeriti je li uparivanje sačuvano, koristi li Welchovu
inačicu za neovisne skupine i izvještava li razliku, interval i učinak. Modeli
često zamijene neovisni i upareni dizajn.

> Prepoznaj jesu li mjerenja neovisna ili uparena. Prikaži pojedinačna
> opažanja, procijeni razliku s intervalom i tek zatim provedi odgovarajući
> test.

**Nađite grešku.**
Iste su osobe mjerene prije i nakon intervencije, a svi parovi imaju ispravan
identifikator. Analiza je ipak provedena kao test dviju neovisnih skupina jer
svaki stupac sadrži zasebne vrijednosti.

Greška je zanemarivanje uparenog dizajna. Jedinica analize je promjena unutar
osobe, pa se testiraju razlike parova.

## Razrađeni primjer

Simuliramo dvije neovisne skupine s brojčanim ishodom. Analiza izračunava
razliku sredina, Welchov interval i standardizirani učinak. Simulacija ne
predstavlja stvarnu studiju, nego pokazuje redoslijed izvještavanja.

*Slika. Procjena razlike u simuliranim skupinama. Izrada autora.*

Interval pokazuje koje su razlike usklađene s ovim uzorkom. Izvještaj još
treba opis skupina, raspodjele i dizajn dodjele. Tek nasumična dodjela može
razliku uvjerljivo povezati s intervencijom.

## Sažetak

Usporedba dviju grupa počinje dizajnom i jedinicom neovisnosti. Jednouzoračni,
neovisni i upareni postupak različite su inačice iste logike procjene razlike.
Linearni model s binarnim prediktorom otkriva zajednički okvir, dok učinak i
interval čuvaju sadržajno značenje. Sljedeće poglavlje širi isti model na više
skupina i uvodi problem mnogih usporedbi.

## Pojmovi

neovisne skupine (*independent groups*), upareni podaci (*paired data*),
Welchov t-test (*Welch's t-test*), razlika sredina (*mean difference*),
binarni prediktor (*binary predictor*), Wilcoxonov test (*Wilcoxon test*)

## Zadaci

### Konceptualni

Razlikujte neovisni i upareni dizajn prema jedinici analize. Predajte po jedan
primjer i objasnite što se u svakom uspoređuje.

### Računski

Upotrijebite `sim_dvije`. Izračunajte razliku, interval i Cohenov d te
predajte jedan odlomak interpretacije.

### Kritički

Prosudite zašto interval razlike nosi više informacija od same oznake
značajnosti (Cumming, 2014). Predajte kratku bilješku recenzentu.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte stvarni dizajn, jednu pogrešku u
testu i rezultat koji bi trebalo računati.
