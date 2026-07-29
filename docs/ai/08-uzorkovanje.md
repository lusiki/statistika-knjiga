# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Efron je bootstrap predstavio kao način procjene nesigurnosti kada imamo jedan
uzorak, a teorijski račun nije jednostavan (Efron, 1979). Postupak se ponaša kao
da uzorak predstavlja malu dostupnu populaciju i iz njega mnogo puta izvlači
nova opažanja s vraćanjem.

Ta ideja ima smisla tek kada razumijemo što se događa prije bootstrapiranja.
Svaki stvarni uzorak samo je jedan mogući ishod postupka odabira. Drugi uzorak
iz iste populacije dao bi drugu sredinu, udio ili korelaciju.

Kako iz jednog uzorka učimo o cijeloj raspodjeli rezultata koje nismo vidjeli?

## Od populacije do uzorka

**Populacija** je skup jedinica o kojima želimo zaključivati. **Uzorak** je dio
jedinica koje smo stvarno promatrali. Razlika nije samo u veličini. Uzorak
nastaje postupkom odabira, a taj postupak određuje koje populacijske jedinice
imaju priliku postati podatak.

Kada bismo nasumično uzorkovanje ponovili mnogo puta, svaki bi uzorak dao
drugačiju statistiku. Raspodjela tih mogućih statistika naziva se
**distribucija uzorkovanja**. Ona ne opisuje raspršenost pojedinaca, nego
raspršenost procjene kroz ponovljene uzorke.

Standardna pogreška sažima tu raspršenost. S rastom uzorka procjene se obično
zbijaju jer svako pojedinačno opažanje nosi manji dio ukupnog rezultata. Dobit
nije linearna. Udvostručavanje uzorka ne prepolovljuje automatski standardnu
pogrešku, pa vrlo veliki uzorci mogu biti skupi za sve manji dobitak preciznosti.

## Oblik koji se pojavljuje

Središnji granični teorem najprije se može vidjeti. Iz asimetrične populacije
uzimamo mnogo uzoraka, računamo njihove sredine i slažemo ih u novi histogram.
Kako uzorci rastu, histogram sredina postaje pravilniji i zbijeniji iako
izvorna populacija nije normalna.

Taj obrazac omogućuje približne račune za mnoge procjene, ali ne popravlja
pristran odabir. Tisuće odgovora iz zatvorenog okvira ne postaju
reprezentativne samo zato što im je standardna pogreška mala. Slučajna
promjenjivost i sustavna pristranost različiti su problemi.

## Interakcija — CLT stroj

CLT stroj gradi distribuciju uzorkovanja pred čitateljem. Izvorna populacija,
veličina uzorka i broj ponavljanja mogu se mijenjati odvojeno, pa je vidljivo
što utječe na oblik, a što na raspršenost uzoračkih sredina.

**Što isprobati.**

1. Uzimajte male uzorke iz simetrične populacije.
2. Promijenite populaciju u snažno asimetričnu.
3. Povećajte uzorak i odvojeno promatrajte oblik i širinu distribucije sredina.

**Statistika u divljini.**
**Jedan uzorak kao privremena populacija.** Bootstrap iznova uzorkuje opažanja
iz dostupnog uzorka kako bi približio promjenjivost procjene (Efron, 1979).
Postupak ne stvara nove vrste jedinica i ne nadoknađuje dio populacije koji
nikada nije mogao ući u uzorak.

Tvrdnja da je rezultat „bootstrapiran" zato govori o procjeni slučajne
nesigurnosti. Ne dokazuje reprezentativnost niti valjanost mjerenja.

**Pitajte model.**
Asistent može napisati simulaciju distribucije uzorkovanja, ali treba mu
odvojeno zadati populaciju, postupak odabira, veličinu uzorka i statistiku.
Provjeravamo uzorkuje li s vraćanjem samo kada je to namjera i brka li
raspršenost pojedinaca sa standardnom pogreškom procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno opiši standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

Greška je zamjena dviju razina varijabilnosti. Veći uzorak sužava raspodjelu
procjene, ali ne mora smanjiti razlike među pojedincima u svakom uzorku.

## Razrađeni primjer

Stvaramo desno asimetričnu simuliranu populaciju i iz nje ponavljano uzimamo
uzorke dviju veličina. Za svaki uzorak računamo sredinu. Usporedba dviju
distribucija pokazuje da veći uzorci daju zbijenije procjene.

*Slika. Distribucije sredina pri dvjema veličinama uzorka. Izrada autora.*

Izvorna populacija ostaje asimetrična u oba slučaja. Mijenja se ponašanje
sredine kroz ponavljanja. Ta razlika između raspodjele opažanja i raspodjele
statistike nosi cijelo kasnije zaključivanje.

## Sažetak

Uzorak je jedan ishod postupka odabira, a distribucija uzorkovanja opisuje kako
bi se procjena mijenjala kroz ponavljanja. Standardna pogreška pripada procjeni,
ne pojedincima. Veći uzorci obično povećavaju preciznost, ali ne uklanjaju
sustavnu pristranost. Poglavlje o procjeni upotrijebit će tu raspodjelu kako bi
izgradilo interval oko vrijednosti koju ne možemo izravno vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), distribucija uzorkovanja
(*sampling distribution*), standardna pogreška (*standard error*), središnji
granični teorem (*central limit theorem*), reprezentativnost
(*representativeness*)

## Zadaci

### Konceptualni

Razlikujte raspodjelu opažanja od distribucije uzoračkih sredina. Predajte
skicu i dva popratna objašnjenja.

### Računski

Promijenite veličine uzorka u simulaciji `sim_sredine` i predajte graf koji
pokazuje promjenu širine distribucije.

### Kritički

Objasnite što bootstrap može, a što ne može nadoknaditi kada je početni uzorak
pristran (Efron, 1979). Predajte jedan odlomak.

### Revizija modela

Ocijenite analizu modela iz okvira. Izdvojite točan zaključak o preciznosti,
jednu zamjenu razina varijabilnosti i njezin popravak.
