# G-A4-12 — odluka o brifu, dokaznom artefaktu i obrisu 12. poglavlja

**Gate:** `G-A4-12`

**Stanje gatea:** prihvaćen kao preporučen.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 13. kolovoza 2026.

**Datum odluke:** 13. kolovoza 2026.

**Zaključano ulazno stanje:** C11 closeout commit
`afd7f474700bcb2a1d63e7ea63543dc7f27dc1d5`.

## Preduvjeti i granica paketa

`C11`, `P0-OUTSIDE` i `P2-IDENTITY` prihvaćeni su. Ratificirani identitetski
brif `c12` i kralježnica `12-kriza-i-obnova` zahtijevaju jedan provjeren
istraživački artefakt koji nosi cijeli put od tvrdnje i protokola do rezultata,
provjere, reforme i njezinih granica. Poglavlje mora ostati jedan argument, ne
popis reformi.

Nijedan handoff nema isporuku ciljanu na `G-A4-12`. Zato nema ulazne isporuke
koju bi ovaj gate smio preuzeti ili potrošiti. Postojeće obveze ciljane na
`P3-EVIDENCE12` i `WC-C12` ostaju njihovim paketima.

Ovaj je paket samo odluka. Ne preuzima ni promovira podatke, ne dodaje
bibliografski ključ, ne izrađuje forest plot i ne uređuje prozu 12. poglavlja.

## Preporučena odluka

Prihvatiti kao središnji dokazni artefakt **Registered Replication Report o
izravnoj multilaboratorijskoj replikaciji studije Stracka, Martina i Steppera**:

- Wagenmakers, E.-J. i sur. (2016), *Registered Replication Report: Strack,
  Martin, & Stepper (1988)*, DOI `10.1177/1745691616674458`;
- službena stranica Association for Psychological Science:
  `https://www.psychologicalscience.org/publications/replication-strack-martin-stepper`;
- službena stranica članka:
  `https://journals.sagepub.com/doi/10.1177/1745691616674458`;
- službeni OSF projekt s podacima i registriranim protokolima:
  `https://osf.io/pkd65/`.

Artefakt se bira kao **portalom posredovan primarni slučaj**. `P3-EVIDENCE12`
smije iz njega izvesti samo minimalan, neidentificirajući zapis na razini
laboratorija i autorski izrađen prikaz. Ne preuzima se objavljena slika i ne
pakiraju se sirovi podaci sudionika. Točna licenca, verzija, popis datoteka,
datumi pristupa i kontrolne sume moraju biti provjereni prije bilo kakve lokalne
datoteke; javna dostupnost sama nije dopuštenje za redistribuciju.

### Zašto artefakt odgovara brifu

Službeni članak opisuje 17 neovisnih izravnih replikacija prema zajedničkom
provjerenom protokolu i ukupno 1.894 uključena sudionika. Primarna analiza je
unaprijed registrirana metaanaliza sirove razlike: članak izvještava objedinjenu
procjenu 0,03 i 95-postotni interval od −0,11 do 0,16, dok je izvorna studija
izvijestila razliku 0,82. Plan, kod i ogledni prikazi izrađeni su prije uvida u
stvarne podatke, a službena stranica povezuje podatke i registrirane protokole.

Te se vrijednosti u ovom gateu rabe samo za dokaz prikladnosti kandidata. Nisu
još usvojene kao brojke knjige. `P3-EVIDENCE12` ih mora neovisno reproducirati
iz točno imenovanoga službenog artefakta ili se zaustaviti s preciznim
neslaganjem.

Slučaj istodobno daje:

- tvrdnju koja je postala poznata prije replikacijskoga projekta;
- unaprijed uređeni protokol, pravila uključivanja i laboratorijske prilagodbe;
- javni trag protokola, analitičkoga plana, koda i podataka;
- studijske procjene, intervale i objedinjenu procjenu za forest plot;
- kontekstualnu heterogenost i dokumentirane razlike među laboratorijima;
- registrirani izvještaj kao promjenu postupka, ali ne kao jamstvo istine;
- jasnu granicu: rezultat jedne paradigme ne presuđuje cijeloj teoriji.

## Točan ugovor za P3-EVIDENCE12

Ako se preporuka prihvati, sljedeći paket mora dokazati sve sljedeće prije
promocije bilo kojega rezultata:

1. **Identitet izvora.** DOI, bibliografski metapodaci, službeni APS/SAGE zapis,
   OSF projekt, točna verzija svake uporabljene datoteke, datum pristupa i
   kontrolna suma.
2. **Prava i privatnost.** Licenca za članak, protokol, kod i svaku podatkovnu
   datoteku provjerava se zasebno. Bez jasne dozvole ostaje portalom posredovana
   ruta; sirovi podaci sudionika i snimke nikad ne ulaze u repozitorij.
3. **Minimalan izvedeni artefakt.** Jedan red po laboratoriju s nazivom,
   procjenom sirove razlike, donjom i gornjom granicom 95-postotnoga intervala i
   uporabljiva `n`, plus posebno označeni izvorni rezultat i objedinjena
   replikacijska procjena. Svako polje mora imati izvorni stupac ili tablični
   položaj.
4. **Forest plot.** Knjiga izrađuje vlastiti crno-bijeli prikaz iz provjerenoga
   izvedenog zapisa. Prikaz odvaja izvorni rezultat od 17 replikacija i od
   objedinjene replikacijske procjene; ne prepisuje izdavačevu sliku.
5. **Jedna usporedba osjetljivosti.** Primarna metaanaliza sirovih razlika
   uspoređuje se s autorima unaprijed pripremljenom analizom standardiziranih
   učinaka iz istoga registriranog plana. Usporedba mora navesti procjene,
   intervale, sadržajni zaključak i da se predstavljena populacija laboratorija
   ne mijenja. Ne smije se svesti na „značajno / nije značajno”.
6. **Vidljivi trag životnoga ciklusa.** Kratak receipt povezuje protokol,
   pravila uključivanja, lokalne prilagodbe, analitički plan, kod, izvedeni
   zapis, prikaz i rukopis. Vidljivi isječci služe čitanju i provjeri; nijedan
   ocijenjeni zadatak ne traži pisanje ili mijenjanje koda.
7. **Granice tvrdnje.** Nema uzročne generalizacije iz sinteze, nema tvrdnje da
   predregistracija ili reproducibilnost jamče valjan zaključak, nema presude o
   cijeloj teoriji na temelju jedne paradigme i nema izmišljene heterogenosti.
8. **Dopunski primarni izvori.** Postojeći `simmons2011`, `gelman2013` i
   `osc2015` ostaju izvori za analitičku fleksibilnost, račvajuće putove i širi
   replikacijski kontekst. Novi RRR ključ dodaje se u `references.bib` tek nakon
   provjere metapodataka. Svaka dodatna tvrdnja o učinku reforme traži vlastiti
   primarni ili neovisno provjereni izvor.

Ako službeni materijali ne omogućuju točnu reprodukciju bilo koje nosive brojke
ili analize standardiziranih učinaka, `P3-EVIDENCE12` ne smije nadomjestiti
prazninu približnom ili zapamćenom vrijednošću. Mora zabilježiti blocker i
vratiti izbor autoru.

## Ratificirani obris 12. poglavlja

Obris podređuje postojeći sedmodijelni kostur jednoj istraživačkoj priči:

1. **Vinjeta:** poznata tvrdnja o facijalnoj povratnoj sprezi i pitanje što
   zajednički replikacijski postupak doista može promijeniti.
2. **Izgradnja pojma I — put tvrdnje:** izvorna studija, selekcija vidljivih
   nalaza i razlika između namjernoga p-hakiranja i račvajućih putova.
3. **Izgradnja pojma II — podatkovni i analitički trag:** prikupljanje,
   uključivanje, lokalne prilagodbe, rekodiranje, nedostajanje i izbor mjerila
   prikazani kao analitička fleksibilnost i dužnost reproducibilnosti.
4. **Izgradnja pojma III — kumulativni dokaz:** 17 laboratorija čita se kroz
   procjene i intervale; replikacija nije natjecanje pobjednika i gubitnika.
5. **Izgradnja pojma IV — forest plot i osjetljivost:** čitanje pojedinačnih i
   objedinjene procjene te usporedba sirove i standardizirane analize bez
   binarnoga rituala značajnosti.
6. **Izgradnja pojma V — reforma i granice:** predregistracija, registrirani
   izvještaji i otvoreni materijali mijenjaju redoslijed i vidljivost odluka,
   ali ne popravljaju loše mjerenje, nevaljanu inferenciju ili neprimjenjiv
   kontekst.
7. **Interakcija:** postojeći `w12` ostaje simulacijski stroj za cijenu više
   analitičkih putova; stvarni RRR nije pretvoren u novi widget.
8. **Statistika u divljini:** autorski forest plot RRR-a čita se od laboratorija
   prema sintezi, uz granice selekcije, konteksta i jedne paradigme.
9. **Pitajte model i pogreška:** asistent uspoređuje registrirani plan, kod,
   izvedeni zapis i rukopis; pogrešna analiza zaključuje da predregistracija
   jamči istinu.
10. **Razrađeni primjer:** čitljiv receipt vodi od službenoga artefakta preko
    minimalne provjere do sirove i standardizirane procjene, bez ocijenjene
    proizvodnje koda.
11. **Sažetak, pojmovi i četiri razine zadataka:** kritički zadatak čita forest
    plot, računski zadatak radi iz potpune tiskane tablice, a reach-back dohvaća
    intervale iz 9. i logiku tvrdnje iz 10. poglavlja.
12. **Prijelaz 12 → 13:** ugovor o reformiranoj praksi zahtijeva da svaka
    kasnija analiza imenuje ciljnu tvrdnju, primarnu analizu, jednu obranjivu
    alternativu, podrijetlo podataka i granicu zaključka.

Dva odobrena nova `#def-` bloka ostaju `analitička fleksibilnost` i
`reproducibilnost`. Ostalih osam ratificiranih pojmova ostaje u prozi i kroz
`.pojam`; G-A4-12 ne uređuje definicije ni konceptni graf.

## Alternative i razlozi odbijanja

1. **Open Science Collaboration 2015 kao jedini nosivi artefakt.** Zadržava se
   kao važan širi kontekst, ali nije odabran za jedinstveni forest plot jer
   okuplja različite ciljne učinke koje nije opravdano svesti na jednu
   zajedničku objedinjenu procjenu.
2. **Many Analysts, One Data Set kao nosivi artefakt.** Izvanredno pokazuje
   varijaciju obranjivih analitičkih odluka i ima otvorene materijale, ali 29
   analiza istoga skupa nisu 29 neovisnih replikacija i ne daju prikladnu
   kumulativnu objedinjenu procjenu. Ne uključuje se kao drugi glavni slučaj jer
   bi razbio pravilo jednoga argumenta.
3. **COVIDiSTRESS kao lokalni paket.** Ostaje odgođen prema D16; velik
   dobrovoljački uzorak ne ispunjava istu ulogu kao registrirani multilab
   protokol, a novi paket bi proširio podatkovni portfelj bez potrebe.
4. **Samo simulacija `w12`.** Zadržava se za učenje mehanizma, ali ne može
   dokazati stvarni životni ciklus, protokol, laboratorijske prilagodbe ni
   otvorene materijale.
5. **Preuzimanje objavljenoga forest plota.** Odbija se. Knjiga izrađuje vlastiti
   prikaz iz provjerenih numeričkih činjenica i vodi zaseban zapis prava.
6. **Popis reformi ili tečaj metaanalize.** Odbija se prema identitetskom brifu i
   kralježnici. Čitatelj interpretira procjene, intervale, sintezu i
   heterogenost; ne računa metaanalizu niti bira procjenitelj.

## Blokirane ovisnosti

Do prihvaćanja ove odluke ostaju blokirani `P3-EVIDENCE12`, `P3-VERIFY-C` i
`WC-C12`, a time i sljedeće sadržajne obveze:

- `R07-C12-full-argument`, `R08-SPINE-12` i
  `R11-C12-pipeline-flexibility`;
- `R19-C12-forest-plot` i `R19-C12-replication-cumulative`;
- `R23-C12-no-R-production`, `R23-C12-visible-receipt` i
  `R23-C12-code-ladder`;
- `R24-C12-primary-sources` i `R35-REACHBACK-12`.

Gate ne prihvaća te stavke; on samo zaključava brif po kojemu će ih kasniji
paketi dokazivati.

## Granica ovlasti

Prihvaćanje odobrava samo opisani brif, izbor portalom posredovanoga artefakta,
ugovor za njegovu provjeru i obris. Ne odobrava nijednu još nereproduciranu
brojku kao tvrdnju knjige, ne utvrđuje pravo redistribucije, ne dodaje podatke,
citacije, figure ili kod, ne mijenja `chapters/12-kriza-i-obnova.qmd`, ne
zatvara nijednu sadržajnu stavku i ne pokreće `P3-EVIDENCE12` prije zasebnoga
closeouta i commita.

Poglavlje 6 ostaje `draft`. Nema vanjske poruke, pusha, mergea, taga,
arhiviranja, deploymenta ni objave.

## Odluka autora

Autor/editor Luka Sikic prihvatio je preporučenu odluku doslovnim odgovorom:

```text
G-A4-12 accepted as recommended for afd7f474700bcb2a1d63e7ea63543dc7f27dc1d5 on 2026-08-13.
```

Ako preporuka nije prihvatljiva, umjesto toga treba navesti točne izmjene
artefakta, izvora, obrisa ili opsega vezane uz isto ulazno stanje.

Ova odluka zatvara samo `G-A4-12`. `P3-EVIDENCE12` smije početi tek nakon
zasebnoga closeouta, provjera i lokalnoga commita ovoga gatea.
