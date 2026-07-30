# Vjerojatnost koliko treba

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Simulator novčića i A/B kampanje | simulacija | pogl. 4 |

**Vinjeta.**
Simmons i suradnici pokazali su kako velik broj razumno zvučećih analitičkih
odluka može povećati vjerojatnost lažno pozitivnog rezultata (Simmons, 2011).
Svaka pojedina odluka mogla je izgledati bezazleno. Problem je postao vidljiv
tek kada se promatrao cijeli niz mogućih putova kroz podatke.

Istraživač zato ne pita samo je li opaženi rezultat moguć pod jednom
pretpostavkom. Mora pitati koliko je prilika postupak dao slučajnosti da
proizvede nešto što izgleda uvjerljivo.

Kako računati s neizvjesnošću bez pretvaranja vjerojatnosti u obećanje o jednom
događaju?

## Neizvjesnost kao raspodjela

**Vjerojatnost** povezuje događaj sa skupom mogućih ishoda. U dugom nizu
ponavljanja može se čitati kao relativna učestalost. U situaciji koja se neće
ponoviti može izražavati stupanj uvjerenja pod jasno navedenim informacijama.
Ta dva čitanja ne moraju biti suparnici, ali zahtijevaju da kažemo na što se
broj odnosi.

Pravilo komplementa prevodi vjerojatnost događaja u vjerojatnost da se događaj
ne dogodi. Zbrajanje pripada međusobno isključivim ishodima, dok množenje
povezuje zajedničko pojavljivanje neovisnih događaja. Najčešća pogreška nije
računska, nego sadržajna pretpostavka da su događaji neovisni samo zato što je
to zgodno za račun.

Binomna situacija ima ponovljene pokušaje, dva ishoda i jednaku vjerojatnost
uspjeha u svakom pokušaju. Glasanje, klik i odgovor na pitanje mogu se tako
modelirati samo kada jedinice i pokušaji dovoljno dobro odgovaraju tim
uvjetima. Model nije opis cijelog svijeta, nego kontrolirana slika dijela
procesa.

## Obrasci mnogih ponavljanja

Pojedinačni ishodi mogu biti neuredni, dok raspodjela velikog broja ishoda
pokazuje stabilan oblik. Normalna krivulja opisuje mnoge takve obrasce oko
središta. Pravilo približnih područja oko sredine korisno je za orijentaciju,
ali se ne primjenjuje na svaku asimetričnu ili višemodalnu raspodjelu.

QQ prikaz uspoređuje poredane podatke s poredanim vrijednostima očekivanima pod
odabranom raspodjelom. Točke blizu pravca podupiru približan oblik, dok
sustavna zakrivljenost pokazuje odstupanje. Prikaz ne izdaje presudu o tome je
li analiza dopuštena. On pokazuje gdje pretpostavka pristaje, a gdje se lomi.

## Interakcija — Simulator novčića i A/B kampanje

Simulator povezuje jednostavno bacanje novčića s A/B kampanjom.
Čitatelj mijenja stvarnu stopu uspjeha i broj pokušaja te promatra kako se
kratki nizovi kolebaju, dok se raspodjela mnogih ponavljanja stabilizira.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu stvarnu vjerojatnost.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na A/B kampanju i postavite stvarnu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

**Statistika u divljini.**
**Mnogo prilika za slučajnost.** Analitička fleksibilnost omogućuje da se među
mnogim ishodima, podskupinama i trenucima zaustavljanja izdvoji rezultat koji
izgleda rijetko, iako je cijeli postupak takav nalaz učinio mnogo vjerojatnijim
(Simmons, 2011).

Čitanje jednog rezultata zato mora uključiti broj pokušaja i odluke donesene
nakon gledanja podataka. Vjerojatnost pripada postupku koji je rezultat
proizveo, a ne samo njegovoj posljednjoj tablici.

**Pitajte model.**
Asistent može simulirati postupak i usporediti analitički račun sa
učestalostima u ponavljanjima. Treba mu jasno opisati skup mogućih ishoda,
neovisnost i sve putove kojima je analiza mogla doći do rezultata. Modeli često
računaju pod prešutnom pretpostavkom neovisnosti.

> Simuliraj ovaj slučaj mnogo puta i prikaži raspodjelu ishoda. Prije računanja
> navedi koje pretpostavke koristiš o neovisnosti i jednakoj vjerojatnosti
> pokušaja.

**Nađite grešku.**
U nizu je više puta zaredom zabilježen isti ishod. Budući da se ravnoteža mora
vratiti, sljedeći pokušaj sada ima veću vjerojatnost suprotnog ishoda.
Pojedinačni pokušaji provedeni su pod jednakim uvjetima.

Greška je kockarska zabluda. Ako su pokušaji neovisni i uvjeti jednaki,
prethodni niz ne mijenja vjerojatnost sljedećeg ishoda.

## Razrađeni primjer

Simuliramo mnogo kampanja s jednakom stvarnom stopom odgovora. Svaka kampanja
daje nešto drukčiji udio, iako se temeljni proces ne mijenja. Histogram
prikazuje koliko je raspršena ta slučajna varijacija.

Raspodjela simuliranih stopa uspjeha. Izrada autora.

Jedna kampanja može završiti daleko od središta bez promjene stvarne stope.
Zaključak se zato ne temelji na tome izgleda li jedan rezultat neobično, nego
na usporedbi s raspodjelom koju bi cijeli postupak mogao proizvesti.

## Sažetak

Vjerojatnost opisuje neizvjesnost unutar jasno određenog skupa mogućnosti.
Pravila računanja vrijede samo uz sadržajne pretpostavke o događajima i
neovisnosti. Simulacija pokazuje kako stabilna raspodjela nastaje iz neurednih
pojedinačnih ishoda. Poglavlje o uzorkovanju tu će logiku primijeniti na
statistike koje se mijenjaju od uzorka do uzorka.

## Pojmovi

vjerojatnost (*probability*), događaj (*event*), neovisnost (*independence*),
binomna raspodjela (*binomial distribution*), normalna raspodjela (*normal
distribution*), QQ prikaz (*Q–Q plot*)

## Zadaci

### Konceptualni

Objasnite zašto niz jednakih ishoda ne mijenja vjerojatnost sljedećeg pokušaja
ako su pokušaji neovisni. Predajte jedan odlomak.

### Računski

Promijenite veličinu pokušaja u objektu `sim_kampanje` i predajte dva histograma
s kratkom usporedbom raspršenosti.

### Kritički

Objasnite kako više analitičkih putova mijenja čitanje rijetkog rezultata
(Simmons, 2011). Predajte dijagram mogućih odluka.

### Revizija modela

Ocijenite analizu modela iz okvira. Imenujte pretpostavku koju navodi, jednu
pogrešku i ispravnu vjerojatnostnu interpretaciju.
