# Kako brojke zavode

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | Istraživač margine pogreške | simulacija | pogl. 1 i 2 |

**Vinjeta.**
Američko statističko udruženje objavilo je izjavu o p-vrijednostima nakon
desetljeća u kojima se jedan prag često koristio kao zamjena za znanstveni sud
(Wasserstein, 2016). Problem nije bio u tome što su istraživači zaboravili
računati. Problem je nastajao kada je jedan broj preuzimao značenje koje mu
postupak nije davao.

Sličan prijenos značenja događa se u naslovima anketa, postocima bez nazivnika
i grafovima kojima odabrani raspon osi pretvara malu promjenu u dramatičan lom.
Broj može biti točan, a prikaz ipak voditi prema zaključku koji podaci ne nose.

Kako razlikovati računsku pogrešku od mnogo češće pogreške u okviru, usporedbi
i jeziku?

## Četiri provjere jedne tvrdnje

Prva provjera traži izvor. Tvrdnja koja navodi istraživanje mora omogućiti
pronalaženje izvornog izvještaja, tablice ili skupa podataka. Poveznica na
drugi članak nije podrijetlo brojke, a navođenje ustanove bez godine i
istraživanja nije dovoljno da bi se nalaz provjerio.

Druga provjera traži nazivnik. Porast od pedeset posto može značiti prijelaz s
dva slučaja na tri ili s dva milijuna na tri milijuna. Postotak opisuje omjer,
dok **postotni bod** opisuje razliku između dvaju postotaka. Njihova zamjena
može višestruko povećati dojam promjene iako je aritmetika pojedinačnih brojeva
točna.

Treća provjera traži usporedbu. Graf bez zajedničke nule nije automatski
nepošten, ali skraćena os mora biti vidljiva i opravdana. Odabir početnog
razdoblja, izostavljanje jedne skupine ili isticanje samo povoljnog ishoda
mijenja priču. Čitatelj zato pita koje bi razumno drugačije uokvirivanje
pokazalo isti podatak.

Četvrta provjera traži neizvjesnost. Rezultat ankete nije svojstvo uzorka koje
će se bez promjene ponoviti u populaciji. Margina pogreške opisuje samo
uzoračku promjenjivost pod određenim pretpostavkama. Ne obuhvaća pristran
okvir, neodaziv, loše pitanje ni naknadno biranje najzanimljivijeg rezultata.

## Protokol skeptičnog čitanja

Skeptičnost nije automatsko odbacivanje. Ona usporava prijelaz od podatka prema
tvrdnji. Najprije utvrđujemo tko je proizveo broj i za koju svrhu. Zatim
provjeravamo jedinicu analize, nazivnik, vremenski okvir i usporednu skupinu.
Tek tada procjenjujemo koliko neizvjesnost i dizajn dopuštaju zaključak.

Isti protokol vrijedi za ljudski i strojno proizveden tekst. Asistent može
izmisliti izvor, popuniti ćeliju koja nedostaje ili zaokružiti rezultat do
lažne preciznosti. Uvjerljiv stil nije dokaz podrijetla. Svaka brojka mora
ostaviti trag do podataka ili postupka iz kojeg je nastala.

## Interakcija — Istraživač margine pogreške

Istraživač prikazuje približnu marginu pogreške uzorka pri različitim
veličinama i procijenjenim udjelima. Zaseban klizač uvodi poznatu sustavnu
pristranost. Interval se tada može sužavati oko precizno procijenjene pogrešne
vrijednosti.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

**Statistika u divljini.**
**Prag koji nije presuda.** Izjava Američkog statističkog udruženja naglasila
je da p-vrijednost sama ne mjeri veličinu ni važnost učinka i ne određuje treba
li rezultat smatrati znanstveno vrijednim (Wasserstein, 2016).

Naslov koji istraživanje svodi na „dokazano" ili „nije dokazano" uklanja
procjenu, neizvjesnost i dizajn. Broj ostaje vidljiv, a upravo informacije
potrebne za njegovo tumačenje nestaju.

**Pitajte model.**
Asistent je koristan kao strogi čitatelj ako dobije izvornu tablicu i jasnu
zabranu nadopunjavanja nedostajućih podataka. Treba tražiti da odvoji provjeru
aritmetike od procjene dizajna i jezika. Nakon odgovora ručno se otvara svaki
navedeni izvor i provjerava postoji li broj u njemu.

> Rastavi ovu statističku tvrdnju na izvor, brojnik, nazivnik, usporedbu,
> neizvjesnost i dopušten zaključak. Ne dopunjuj podatke koji nisu priloženi i
> jasno označi što nije moguće provjeriti.

**Nađite grešku.**
Anketa pokazuje vodstvo jedne opcije, ali se intervali procjena dviju opcija
preklapaju. Zbog preklapanja možemo zaključiti da među njima sigurno nema
razlike. Uzorak je opisan, a postoci se zbrajaju do cjeline.

## Razrađeni primjer

Simuliramo dvije ankete o istoj podršci, jednu s manjim i jednu s većim
uzorkom. Obje su pošteno uzorkovane iz iste zamišljene populacije. Cilj nije
dobiti stvarni izborni rezultat, nego vidjeti što se mijenja kada povećamo broj
opažanja.

*Slika. Simulirane procjene pri dvjema veličinama uzorka. Izrada autora.*

Veći uzorak daje užu marginu, ali obje ankete dijele pretpostavku da je
uzorkovanje nepristrano. Kada bi okvir isključio dio populacije, tablica bi i
dalje mogla pokazivati veliku računsku preciznost. Strog prikaz zato uz marginu
navodi način odabira ispitanika, datum, formulaciju pitanja i naručitelja.

## Sažetak

Brojke zavode kada izgube izvor, nazivnik, usporedbu ili neizvjesnost. Pogreška
ne mora biti u računu jer često nastaje u izboru prikaza i jezika kojim se
rezultat pretvara u tvrdnju. Skeptični protokol jednak je za novinski naslov,
znanstveni sažetak i odgovor modela. U sljedećem dijelu knjige isti se zahtjev
primjenjuje na sažimanje i vizualizaciju vlastitih podataka.

## Pojmovi

nazivnik (*denominator*), postotni bod (*percentage point*), margina pogreške
(*margin of error*), pristranost (*bias*), lažna preciznost (*false
precision*), podrijetlo podatka (*data provenance*)

## Zadaci

### Konceptualni

Objasnite razliku između pedesetpostotnog rasta i rasta od pedeset postotnih
bodova. Predajte vlastiti primjer bez stvarnih empirijskih tvrdnji.

### Računski

Upotrijebite simulirane podatke `sim_ankete`. Dodajte treću veličinu uzorka i
predajte tablicu s pripadajućom marginom pogreške.

### Kritički

Pročitajte izjavu o p-vrijednostima i izdvojite jednu tvrdnju koju ona
dopušta te jednu koju izričito ne dopušta (Wasserstein, 2016). Predajte dvije
rečenice i citat izvora.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Odvojite točne provjere od jedne
pogrešne interpretacije i napišite provjerljiviju zamjenu.
