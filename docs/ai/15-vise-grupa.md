# Uspoređivanje više grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Dekompozicija varijance | simulacija | pogl. 14 |

**Vinjeta.**
Analitička fleksibilnost postaje posebno vidljiva kada istraživanje sadrži više
skupina i ishoda. Svaka nova parna usporedba daje još jednu priliku da
slučajnost proizvede privlačan rezultat, čak i kada pojedinačni testovi slijede
uobičajeni prag (Simmons, 2011).

Istraživač zato prvo postavlja zajedničko pitanje o cijelom skupu sredina.
Tek nakon njega traži parove ili kontraste koji nose sadržajnu razliku. Time se
analiza usklađuje s pitanjem, a ne s najpovoljnijim rezultatom.

Kako više skupina usporediti kao jedan model, a zatim objasniti gdje se razlike
nalaze?

## Varijanca između i unutar

Analiza varijance uspoređuje razlike među sredinama s razlikama među
pojedincima unutar skupina. Ako su skupne sredine daleko, a opažanja unutar
svake skupine razmjerno zbijena, omjer tih dviju vrsta varijacije raste.
**F-statistika** sažima upravo taj odnos.

Naziv ANOVA može zavesti jer je ishod usporedba sredina, a račun prolazi kroz
varijancu. Postupak je linearni model s kategoričkim prediktorom. Svaka
kategorija određuje očekivanu vrijednost, dok reziduali opisuju ono što skupna
pripadnost nije objasnila.

Ukupni test ne govori koja se skupina razlikuje. Tukeyjev postupak uspoređuje
parove uz kontrolu obiteljske pogreške. Planirani kontrasti mogu biti
učinkovitiji kada proizlaze iz unaprijed postavljenog pitanja. Naknadno
pregledavanje svih mogućih parova i prijavljivanje samo zanimljivih vraća
problem nevidljivih putova.

## Veličina i pretpostavke

Eta-kvadrat opisuje udio varijabilnosti povezan sa skupnim razlikama, ali može
biti pristran prema većim vrijednostima u malim uzorcima. Omega-kvadrat nudi
konzervativniju procjenu. Obje mjere trebaju interval ili barem jasnu napomenu o
preciznosti i kontekstu.

Pretpostavke se pregledavaju na rezidualima. Neovisnost dolazi iz dizajna,
približna normalnost iz oblika ostataka, a homogenost varijance iz usporedbe
raspršenosti skupina. Kruskal-Wallisov test prelazi na rangove kada je takvo
pitanje prikladnije, ali ni on ne popravlja ovisna opažanja ili loš dizajn.

## Interakcija — Dekompozicija varijance

Prikaz razdvaja odstupanje skupnih sredina od raspršenosti pojedinaca oko tih
sredina. Promjena bilo koje od četiri veličine odmah mijenja F-omjer, pa se
vidi zašto razmak među skupinama nije dovoljan bez usporedbe s varijacijom
unutar njih.

*Slika. Dekompozicija varijance — skupne sredine, zajednička sredina i raspršenost pojedinačnih opažanja.*

**Što isprobati.**

1. Postavite sve tri sredine na 52 i zadržite standardnu devijaciju 6.
2. Postavite sredine na 46, 52 i 58 te usporedite novi F-omjer s prvim.
3. Zadržite razdvojene sredine, povećajte standardnu devijaciju na 12 i
   pratite koliko se F-omjer smanjuje.

**Statistika u divljini.**
**Mnogo usporedbi, jedna priča.** Fleksibilan izbor ishoda i podskupina može
povećati stopu lažno pozitivnih nalaza i kada svaki pojedinačni test izgleda
uobičajeno (Simmons, 2011).

Zajednički model i unaprijed obrazloženi kontrasti čine obitelj pitanja
vidljivom. Korekcija nije kazna za istraživača, nego računovodstvo prilika koje
je postupak dao slučajnosti.

**Pitajte model.**
Asistent može provesti ANOVA-u i post-hoc usporedbe, ali treba mu zadati
planirane kontraste i referentnu skupinu. Provjeravamo reziduale, broj
usporedbi, korekciju i veličinu učinka. Modeli često iz značajnog ukupnog testa
izvode tvrdnju da se svaka skupina razlikuje od svake druge.

> Prikaži skupne raspodjele, procijeni zajednički model i tek nakon ukupnog
> testa provedi unaprijed obrazložene usporedbe. Izvijesti korekciju, učinak i
> intervale razlika.

**Nađite grešku.**
Ukupni F-test pokazuje da model sa skupinama poboljšava opis podataka, a
reziduali ne otkrivaju ozbiljan problem. Zato se sve skupine međusobno
statistički razlikuju.

Greška je zaključak o svim parovima iz ukupnog testa. Potrebne su planirane ili
post-hoc usporedbe s odgovarajućom kontrolom višestrukosti.

## Razrađeni primjer

Simuliramo tri skupine i brojčani ishod. Graf bi trebao prethoditi modelu, a
kod zatim procjenjuje zajedničku ANOVA-u. Tukeyjev postupak dolazi nakon
ukupnog pitanja i pokazuje koji su parovi dovoljno precizno razdvojeni.

*Slika. Tukeyjeve usporedbe simuliranih skupina. Izrada autora.*

Parne procjene imaju vlastite intervale i ne moraju sve voditi prema istoj
odluci. Sadržajni zaključak vraća se veličinama razlika, a ne samo oznakama
nakon korekcije.

## Sažetak

ANOVA uspoređuje varijaciju između skupina s varijacijom unutar njih i time
više sredina smješta u jedan linearni model. Ukupni test ne identificira
parove, pa nakon njega dolaze planirani kontrasti ili korigirane post-hoc
usporedbe. Veličina učinka i reziduali ostaju nužni za tumačenje. Sljedeće
poglavlje uklanja granicu između „testova" i pokazuje linearni model kao opći
okvir.

## Pojmovi

analiza varijance (*analysis of variance*), F-statistika (*F-statistic*),
varijanca između skupina (*between-group variance*), Tukeyjev HSD (*Tukey's
HSD*), eta-kvadrat (*eta squared*), Kruskal-Wallisov test
(*Kruskal–Wallis test*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Predajte skicu triju sredina koja to pokazuje.

### Računski

Upotrijebite `sim_vise`. Procijenite ukupni model, eta-kvadrat i Tukeyjeve
usporedbe te predajte jednu tablicu.

### Kritički

Prosudite kako broj analitičkih putova utječe na čitanje najmanje p-vrijednosti
među mnogim skupinama (Simmons, 2011). Predajte jedan odlomak.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točan zaključak o ukupnom
modelu, jednu neopravdanu tvrdnju o parovima i potreban nastavak analize.
