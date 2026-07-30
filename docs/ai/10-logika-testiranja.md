# Logika testiranja

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Simulator p-vrijednosti | simulacija | pogl. 7–9 |

**Vinjeta.**
Američko statističko udruženje moralo je javno razjasniti p-vrijednost jer je
jedan računski izlaz prečesto služio kao automatska odluka o postojanju učinka
(Wasserstein, 2016). Istraživački izvještaji pretvarali su prag u granicu između
rezultata koji „postoje" i onih koji „ne postoje", iako postupak nije mogao
nositi takvu podjelu.

Testiranje ne počinje pragom. Počinje zamišljenim svijetom u kojem nema učinka
koji tražimo, a zatim pita koliko je opaženi rezultat neobičan u tom svijetu.
Odgovor ovisi o modelu, testnoj statistici i svim odlukama koje su proizvele
podatke.

Što mala p-vrijednost govori o podacima, a što ne može reći o hipotezi?

## Svijet bez učinka

Postupak najprije postavlja **nultu hipotezu**, precizan model svijeta bez
razlike ili veze koju istražujemo. Alternativna hipoteza opisuje odstupanje
koje nas zanima. Te hipoteze nisu dvije jednako dokazane priče. Test je
konstruiran tako da procjenjuje ponašanje podataka pod nultim modelom.

Simulacija tu logiku pokazuje bez formule. Oznake skupina možemo nasumično
premještati kada nulta hipoteza tvrdi da skupine nisu različite. Nakon svakog
premještanja računamo razliku. Dobivena nulta raspodjela govori koliko se velike
razlike pojavljuju samo zbog slučajnog rasporeda.

**P-vrijednost** je udio rezultata pod nultim modelom koji su barem toliko
neusklađeni s njime kao opaženi rezultat. Ona nije vjerojatnost da je nulta
hipoteza istinita, nije vjerojatnost da je nalaz slučajan i ne mjeri važnost
učinka (Wasserstein, 2016).

## Dvije vrste pogreške

Odbacivanje istinite nulte hipoteze stvara pogrešku prve vrste. Neodbacivanje
nulte hipoteze kada relevantan učinak postoji stvara pogrešku druge vrste.
Snižavanje praga otežava prvi tip pogreške, ali uz jednak dizajn može olakšati
drugi. Nema postupka koji obje mogućnosti uklanja besplatno.

Neodbacivanje nije prihvaćanje nulte hipoteze. Rezultat može biti kompatibilan
s nedostatkom učinka, ali i s nizom učinaka koje neprecizan uzorak nije mogao
razlikovati. Zbog toga test čitamo uz procjenu i interval, a ne umjesto njih.

Bayesovski pristup izravnije uspoređuje kako podaci mijenjaju početna uvjerenja
o modelima. U ovoj knjizi ostaje pogled kroz prozor, a ne drugi puni račun.
Važno je prepoznati da odgovara na drugo pitanje i zahtijeva eksplicitne
početne pretpostavke.

## Interakcija — Simulator p-vrijednosti

Simulator p-vrijednosti stvara rezultate kada je nulta hipoteza istinita i
kada nije. Čitatelj promatra koliko se p-vrijednosti mijenjaju od uzorka do
uzorka i zašto jedan rezultat ne može biti potvrda postupka u cjelini. Radi
preglednosti koristi normalne ishode s poznatom varijabilnošću i obostrani test.

*Slika. Raspodjele p-vrijednosti pod nultim modelom i pod odabranim stvarnim učinkom.*

**Što isprobati.**

1. Generirajte više uzoraka pod istinitom nultom hipotezom.
2. Postavite standardiziranu razliku na 0,35 i zadržite uzorak jednakim.
3. Povećajte uzorak bez promjene učinka i usporedite udio rezultata ispod praga.
4. Spustite prag s 0,05 na 0,01 i usporedite obje raspodjele.

Simulacija razdvaja dvije činjenice. Kada je nulta hipoteza istinita, prag
unaprijed određuje dugoročnu stopu pogreške. Kada učinak postoji, veličina
uzorka mijenja koliko ga često postupak otkriva.

**Statistika u divljini.**
**Značajnost bez veličine.** Izjava Američkog statističkog udruženja navodi da
znanstveni zaključak ili odluka ne bi smjeli ovisiti samo o tome prelazi li
p-vrijednost određeni prag (Wasserstein, 2016).

Naslov koji rezultat pretvara u „dokazano" uklanja nulti model, veličinu
učinka, interval i kvalitetu dizajna. Odgovorno čitanje vraća te dijelove prije
nego što procijeni doprinos nalaza.

**Pitajte model.**
Asistent može provesti test i simulirati nultu raspodjelu, ali mu treba zatražiti
da prvo imenuje nultu hipotezu, testnu statistiku i jedinicu permutiranja.
Provjeravamo odgovara li test dizajnu, jesu li opažanja neovisna i tumači li
p-vrijednost kao vjerojatnost hipoteze.

> Opiši nultu hipotezu, izgradi nultu raspodjelu simulacijom i usporedi opaženu
> statistiku s njome. Izvijesti procjenu i interval prije p-vrijednosti.

**Nađite grešku.**
Test je prikladan za dizajn, procjena i interval su prikazani, a p-vrijednost
je mala. Zato je vjerojatnost da je nulta hipoteza istinita jednaka toj
p-vrijednosti.

Greška je zamjena uvjetnih vjerojatnosti. P-vrijednost opisuje podatke pod
nultim modelom, a ne vjerojatnost nultog modela nakon opaženih podataka.

## Razrađeni primjer

Simuliramo dvije skupine bez stvarne razlike i promatramo jednu opaženu razliku
sredina. Permutacijski postupak miješa oznake skupina, čuva sve ishode i gradi
raspodjelu razlika usklađenu s nultom hipotezom.

Nulta raspodjela razlike sredina u simuliranom primjeru. Izrada autora.

Graf pokazuje koliko je opažena razlika udaljena od onoga što stvara postupak
bez grupnog učinka. Zaključak ne završava odbacivanjem ili neodbacivanjem.
Vraća se procjeni razlike, njezinoj preciznosti i dizajnu koji određuje smijemo
li govoriti o uzroku.

## Sažetak

Testiranje uspoređuje opaženi rezultat s raspodjelom pod preciznom nultom
hipotezom. P-vrijednost opisuje tu neusklađenost i ne govori kolika je
vjerojatnost hipoteze ni koliko je učinak važan. Dvije vrste pogreške povezuju
prag s posljedicama odluke. Sljedeće poglavlje zato stavlja veličinu učinka i
snagu ispred rituala značajnosti.

## Pojmovi

nulta hipoteza (*null hypothesis*), alternativna hipoteza (*alternative
hypothesis*), testna statistika (*test statistic*), p-vrijednost (*p-value*),
pogreška prve vrste (*Type I error*), pogreška druge vrste (*Type II error*)

## Zadaci

### Konceptualni

Objasnite zašto p-vrijednost nije vjerojatnost nulte hipoteze. Predajte
objašnjenje koje razlikuje uvjetovanje na model od uvjerenja o modelu.

### Računski

Promijenite veličinu razlike u objektu `sim_test`. Predajte dvije nulte
raspodjele i usporedbu opaženih statistika.

### Kritički

Prosudite tvrdnju da prelazak praga sam određuje znanstvenu važnost nalaza
(Wasserstein, 2016). Predajte kratku uredničku bilješku.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira. Imenujte ispravan postupak, jednu
zamjenu vjerojatnosti i ispravnu rečenicu o rezultatu.
