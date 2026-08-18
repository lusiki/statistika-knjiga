# G-A4-17 — paket odluke za Tier F brif 17. poglavlja

**Gate:** `G-A4-17`

**Stanje gatea:** prihvaćen kao preporučen.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 18. kolovoza 2026.

**Datum odluke:** 18. kolovoza 2026.

**Zaključano ulazno stanje:** C16 closeout commit
`26197f84889f1b1caffc25e4bbc171631328adb4`.

## Preduvjeti i granica paketa

`C16`, `P0-OUTSIDE` i `P2-IDENTITY` prihvaćeni su. Poglavlje 16 završava
razlikovanjem objašnjenja, predviđanja i uzročnosti te daje ograničeni most za
čitanje binarnoga ishoda. Ratificirana kralježnica Dijela V izričito postavlja
13. poglavlje kao preduvjet 17. poglavlja: uvjetni nazivnici i kontingencijska
tablica već su uvedeni prije nego što isti tablični objekt u klasifikacijskom
kontekstu dobije ime `tablica zabune`.

Ratificirani identitetski brif `c17` traži jedan argument o jednoj
posljedičnoj odluci utemeljenoj na klasifikaciji teksta, od granice korpusa do
nadzora. Odluka `D07` zadržava postojeći widget pravednosti za simulaciju i
ParlaMint-HR/ParlaSent analizu za empirijski razrađeni primjer. Gate zato ne
smije zamijeniti widget, dodati drugi središnji widget ili tekstni paket
pretvoriti u demonstraciju bez pitanja.

Cjeloviti ledger od 97 handoffa nema isporuku ciljanu na `G-A4-17`. Zato ovaj
gate ništa ne priznaje ni troši u ime `G-A3-TEXT`, `P3-TEXT` ili `WD-C17`.
Njihove provjere izvora, prava, podataka i proze ostaju zasebne.

Ovaj paket donosi samo ovu odluku. Ne dohvaća ParlaMint ni ParlaSent, ne odabire
ili promovira datoteku, ne zaključuje prava, ne dodaje bibliografski ključ i ne
mijenja `chapters/17-doba-algoritama.qmd`, widget, podatke, katalog ili
zajedničke registre.

## Preporučena odluka

Prihvaćen je sljedeći povezani Tier F brif.

### Jedno središnje pitanje i jedna odluka

Središnje pitanje glasi:

> Kako nastaje i kako treba nadzirati odluku da se parlamentarna rečenica, na
> temelju klasifikacije njezina tona, pošalje u ljudski pregled za mogući javni
> sažetak — od granice korpusa i zabilježenih oznaka do praga, pogrešaka po
> podskupinama, prigovora i povratne sprege?

Jedina posljedična odluka jest **ulazak rečenice u red za ljudski pregled**.
Klasifikator ne briše sadržaj, ne kažnjava govornika, ne proglašava namjeru i
ne objavljuje automatski oznaku. Ipak, pogreška nije bez posljedice: lažno
pozitivna odluka može nerazmjerno usmjeriti pozornost na govornika ili skupinu,
a lažno negativna može iz javnoga pregleda ukloniti relevantan govor. Ljudski
pregled, obrazloženje, mogućnost ispravka i nadzor zato su dio evaluacije
sustava, a ne naknadni etički dodatak.

To je izričito **nastavna odluka nad provjerenim stvarnim tekstom**, a ne
tvrdnja da je Hrvatski sabor, ParlaMint, ParlaSent ili neka druga imenovana
ustanova uvela takav sustav. `WD-C17` ne smije izmišljenu institucionalnu
primjenu prikazati kao empirijsku činjenicu. Ako buduća vinjeta imenuje stvarni
sustav ili događaj, svaka nosiva tvrdnja traži provjerljiv primarni izvor i
služi istoj odluci, ne drugom narativnom stupu.

Poglavlje podupire opis, povezanost, predviđanje i odluku. Ne podupire
uzročnost, namjeru govornika, prevalenciju tona u parlamentu ni
generalizaciju s odabranoga korpusa na politički govor izvan njega.

### Pravilo odabira i razdvajanja

`G-A3-TEXT` treba operacionalizirati sljedeće pravilo, a `P3-TEXT` ga mora
reproducirati ili pasti zatvoreno:

1. **Izvorni okvir.** Kandidati su samo rečenice iz točno prikovanoga izdanja
   ParlaSent koje pripadaju objavljenoj bosansko-hrvatsko-srpskoj komponenti,
   nose zemlju, pojedinačne oznake kodera, usklađenu oznaku i izvorni indikator
   podjele te se stabilnim ključem mogu povezati s govorom ili dokumentom u
   točno prikovanom izdanju ParlaMint-HR. Gate preporučuje trenutačno
   evidentirane kandidate ParlaMint 5.0 i ParlaSent 1.0, ali ne zamjenjuje
   zasebnu provjeru inačice i prava.
2. **Bez odabira prema rezultatu.** U nastavni paket ulaze sve jedinice koje
   zadovolje unaprijed zapisane jezične, zemljopisne, vremenske i povezne
   uvjete. Nema dodatnoga uravnoteživanja oznaka ili podskupina i nema
   izbacivanja neslaganja među koderima. Broj jedinica, gubici pri povezivanju i
   svaki razlog isključenja moraju biti vidljivi.
3. **Izvorno razdvajanje ostaje vidljivo.** Izvorni testni dio ostaje netaknut
   `skup za ispitivanje` i ne služi odabiru praga. Izvorni dio za učenje dijeli
   se deterministički po stabilnom ključu govora ili dokumenta, ne po retku:
   približno 80 % čini `skup za učenje`, a približno 20 % `skup za provjeru`, uz
   što bližu raspodjelu zemlje i usklađene oznake. Nijedan govor, dokument ili
   izvedeni tekstni blizanac ne smije prijeći među skupovima.
4. **Jedna uporaba ispitnoga skupa.** Postupak označavanja i prag zaključavaju
   se na skupu za učenje i skupu za provjeru. Skup za ispitivanje služi jednoj
   završnoj tablici izvedbe i nije izvor naknadnoga ugađanja. Svaka kasnija
   promjena pravila otvara novu, izričito označenu analizu.
5. **Nema prevalencijske tvrdnje.** ParlaSentov odabir rečenica koje nose
   sentiment i razlika u konstrukciji izvornih dijelova znače da udio oznaka u
   nastavnom paketu nije procjena udjela negativnoga tona u parlamentu.
   `Skup za učenje` pogotovo nije uzorak za takvu populacijsku tvrdnju.

Ako službeni metapodaci ne omogućuju zemljopisni rez, stabilnu vezu izvora ili
grupirano razdvajanje bez curenja, `G-A3-TEXT` ne smije izmisliti ključ,
zemlju ili podjelu. Mora vratiti točno neslaganje autoru. Dopuštena rezerva je
zasebno označena ParlaMint-only opisna vježba bez prenesenih sentimentnih
oznaka; ona ne ispunjava cijeli preporučeni brif i zahtijevala bi novu
dispoziciju gatea.

## Uloga povezanoga tekstnog paketa

Paket ima tri povezane, ali nezamjenjive razine sa stabilnim ključevima:

| Razina | Jedinica i uloga | Što ne dokazuje |
|---|---|---|
| pregledni tekst | govor i pripadna rečenica s nužnim kontekstom i metapodacima | da je izdvojeni korpus populacijski reprezentativan ili da tekst otkriva namjeru |
| pripremljeni brojevi | govor ili dokument × unaprijed imenovana tekstna mjera | da jedna normalizacija, granica korpusa ili rječnik valjano mjeri društveni konstrukt |
| označene rečenice | rečenica × oznaka kodera × usklađena zabilježena oznaka × skup | da je usklađena oznaka istina ili da dobra izvedba potvrđuje valjanost konstrukta |

Na tim se razinama izvodi jedna trostruka usporedba odluke:

- sirovi broj i broj na zajedničku duljinu pokazuju osjetljivost zaključka na
  normalizaciju;
- označene rečenice i njihovi puni povezani govori pokazuju osjetljivost na
  granicu korpusa;
- ljudska pojedinačna oznaka, usklađena zabilježena oznaka te pripremljena
  rječnička ili modelska oznaka pokazuju kako postupak kodiranja mijenja
  tablicu odluka.

Riječ `osjetljivost` ovdje označuje **analizu osjetljivosti zaključka na
obranjivu odluku**. Nikad ne smije biti hrvatsko ime za stopu iz tablice
zabune. Svaka stopa u toj tablici piše se punim nazivom i s vidljivim uvjetnim
nazivnikom.

Empirijski paket daje pogrešive zabilježene oznake, stvarnu selekciju i
provjerljiv trag transformacije. Postojeći `w17` ostaje odvojena simulacija u
kojoj je generirajući mehanizam poznat i u kojoj čitatelj pomiče zajednički
klasifikacijski prag. Widget ne prikazuje empirijske rezultate, ne nosi
objašnjenje sam i ne dobiva stvarne osobe ili skupine.

## Terminološki i pojmovni ugovor

`WD-C17` mora primijeniti ratificirani `G-A2c` bez nove terminološke odluke:

- `predviđanje` je kanonska imenica za čin i rezultat;
- `predikcija` je dopuštena samo u ratificiranoj sintagmi `sustav predikcije`;
- puni naziv glasi `razdvajanje na skup za učenje, provjeru i ispitivanje`, a
  sastavnice su `skup za učenje`, `skup za provjeru` i `skup za ispitivanje`;
- `tablica zabune` i kontingencijska tablica iz 13. poglavlja jedan su
  tablični objekt pod kontekstualno odabranim imenom, ne dvije metode;
- `zabilježeni referentni ishod` nikad nije `istina`, `stvarna istina` ili
  `ground truth`;
- `osjetljivost` nikad ne imenuje stopu iz tablice zabune.

Poglavlje dobiva točno dva nova `#def-` bloka: `zabilježeni referentni ishod` i
`klasifikacijski prag`. Ostalih deset pojmova iz kralježnice ostaje u prozi i
po potrebi u `.pojam`: `tekstna jedinica`, `granica korpusa`, `okvir kodiranja`,
`tablica zabune`, `pogreške po podskupinama`, `algoritamska pravednost`,
`razdvajanje na skup za učenje, provjeru i ispitivanje`, `preprilagodba`,
`pomak distribucije` i `jezični model kao sustav predikcije`.

Nema tvrdnje da je terminologiju neovisno pregledao vanjski recenzent.
Terminološka odluka i pregled za prvo izdanje ostaju autorova odgovornost.

## Tier F obris 17. poglavlja

Jedan argument prolazi kroz postojeći sedmodijelni kostur ovim redom:

1. **Vinjeta:** jedna provjerljiva parlamentarna rečenica i pitanje treba li je
   pripremljeni sustav poslati u ljudski pregled. Odmah se imenuju odluka,
   moguća posljedica obiju pogrešaka i činjenica da zabilježena oznaka nije
   istina.
2. **Korpus, jedinica i odsutnost:** razlikuju se govor, rečenica, govornik i
   redak; čitatelj vidi tko ili što nije moglo ući te zašto se odabrani korpus
   ne pretvara u populaciju političkoga govora.
3. **Okvir kodiranja i proizvodnja oznake:** ljudska oznaka, rječničko pravilo i
   modelska oznaka čitaju se kao konkurentska mjerenja. Neslaganje kodera i
   usklađenje ostaju vidljivi.
4. **Razdvajanje i evaluacija:** razlikuju se populacijska generalizacija iz 8.
   poglavlja i razdvajanje radi prediktivne evaluacije. Curjenje po govoru ili
   dokumentu prikazuje se kao neuspjeh nacrta, a ne kao tehnički detalj.
5. **Vjerojatnost, prag i tablica zabune:** dohvaća se most iz 16. poglavlja i
   uvjetni nazivnici iz 13. Procijenjena vjerojatnost, odluka nakon praga i
   pogreška ostaju tri različite stvari.
6. **Pogreške po podskupinama i pravednost:** temeljne stope iz 3. poglavlja i
   posljedice pogreške iz 10. i 11. poglavlja objašnjavaju zašto jedna ukupna
   točnost ili jedna paritetna mjera ne zatvara pitanje pravednosti.
7. **Interakcija:** `w17` dolazi tek nakon proznoga objašnjenja. Simulira
   promjenu praga i sukob mjerila; nije empirijski prikaz ParlaSenta i ne nosi
   cijeli argument.
8. **Sporna oznaka i postupovna pravednost:** mijenja se postupak proizvodnje
   oznake i pokazuje kako se mijenjaju stope. Obavijest, obrazloženje, prigovor,
   ispravak i žalba dio su sustava.
9. **Sustav nakon ugradnje:** analiza prati podatke, sučelje, odluku, ljudski
   pregled, povratnu spregu, pomak distribucije i nadzor. Dobra izvedba na
   izdvojenim podacima nije potvrda valjanosti konstrukta ni trajna dozvola za
   uporabu.
10. **Jezični modeli:** jezični model čita se kao sustav predikcije koji
    proizvodi vjerojatan nastavak, ne kao provjerena baza dokaza. Svaka tvrdnja
    o aktualnom sustavu datira se i podupire primarnim izvorom.
11. **Statistika u divljini:** Chouldechovina analiza i pripadni primarni izvori
    ostaju ograničeni dokaz da se mjerila mogu sukobiti pri različitim
    temeljnim stopama. Kaznenopravni slučaj nije drugi empirijski razrađeni
    primjer niti se njegove skupine prenose u widget.
12. **Pitajte model i pogreška:** asistent auditira jedinicu, granicu korpusa,
    oznake, curenje, prag, nazivnike, pogreške po podskupinama, pomak i
    valjanost kodiranja. Jedina posađena greška zamjenjuje dobru ispitnu
    izvedbu dokazom valjana mjerenja.
13. **Razrađeni primjer:** povezani paket vodi od teksta i oznaka preko
    zaključanoga praga do tablice zabune, podskupinskih pogrešaka, jedne
    usporedbe granice/normalizacije/kodiranja i odluke o ljudskom pregledu.
    Čitatelj prima kratke vidljive računske potvrde i pripremljene tablice;
    skriveni kod ne postaje ocijenjena proizvodnja R-a.
14. **Sažetak, pojmovi i četiri razine zadataka:** računski zadatak radi iz
    potpune tiskane tablice, kritički zadatak osporava jednu oznaku i jedno
    mjerilo pravednosti, revizija modela auditira cijeli sustav, a reach-back
    dohvaća najmanje 13. i 16. poglavlje. Završni prijelaz predaje 18. poglavlju
    prag, teret pogreške, nadzor, prigovor i odgovorno delegiranje.

Strojno učenje ostaje na razini pojmova i društvenih posljedica. Nema izvoda,
funkcije gubitka, optimizacije, vektorskih reprezentacija, ugrađivanja,
tokenizatora, lematizatora, treniranja modela ili tečaja obrade prirodnoga
jezika.

## Dokazni ugovor za kasnije pakete

Prihvaćanje brifa ne prihvaća nijednu brojku. `G-A3-TEXT` i `P3-TEXT` prije
proze moraju dokazati:

1. trajne službene zapise, točna izdanja, datoteke, datume pristupa, službene
   kontrolne sume i potpune navode za oba izvora;
2. zasebne CC BY 4.0 i CC BY-SA 4.0 obveze, uključujući atribuciju, oznaku
   izmjena i ShareAlike granicu svakoga izvedenog izlaza;
3. stabilne ključeve, jedinice, granice korpusa, gubitke povezivanja, UTF-8,
   dopuštene oznake, nedostajanje i izvorno razdvajanje;
4. tri povezane razine bez orphan zapisa, udvostručavanja ili curenja;
5. točne brojnosti izvora i izvedenoga paketa te neovisno ponovljivu
   transformaciju bez mreže tijekom renderiranja;
6. pripremljene tablice i kratke vidljive potvrde dostatne za HTML, PDF, DOCX,
   jamovi/put bez koda i ručni tiskani zadatak;
7. odgovorivu granicu: nema prevalencijske, uzročne ili populacijski
   generalizirane tvrdnje te nema predstavljanja zabilježene oznake kao istine.

Ako bilo koji nosivi rezultat, veza, oznaka, licenčna obveza ili brojnost nije
provjerljiva iz službenoga artefakta, paket staje s blockerom. Ne rabi približnu
vrijednost, zapis iz sjećanja ili izmišljeni bibliografski ključ.

`WD-C17` potom mora proći determinističke provjere, ciljane HTML/PDF/DOCX
rendere i završni panel šest neovisnih kritičara. Ne tvrdi se da je poglavlje
čitao novi čitatelj niti da je mjereno vrijeme čitanja.

## Alternative i razlozi odbijanja

1. **COMPAS/Chouldechova kao jedini nosivi slučaj.** Izvor ostaje ključan za
   sudar mjerila, ali nije klasifikacija teksta i ne ispunjava D07 ni tekstni
   modul.
2. **Samo ParlaMintova opisna analiza riječi.** Može biti zakonita rezerva ako
   povezani paket padne, ali sama ne daje oznake, izdvojenu evaluaciju, prag,
   tablicu zabune ni spornu referentnu oznaku.
3. **Samo ParlaSentova klasifikacijska tablica.** Daje evaluaciju, ali bez
   govora, korpusne granice i pripremljenih brojeva gubi mjerenje teksta i
   analizu osjetljivosti.
4. **Uravnotežen uzorak oznaka ili slučajni redci.** Odbija se jer skriva
   selekciju, omogućuje curenje među rečenicama istoga govora i poziva na
   lažnu prevalencijsku tvrdnju.
5. **Samo skup za učenje i ispitivanje.** Odbija se jer odabir praga na
   ispitnom skupu pretvara završnu evaluaciju u ugađanje. Tri sastavnice i puni
   izraz razdvajanja ostaju obvezni.
6. **Automatska sankcija ili uklanjanje sadržaja.** Odbija se kao nepotrebno
   proširenje posljedice i moguća izmišljena institucionalna praksa. Ljudski
   pregled zadržava stvaran ulog uz vidljiv put prigovora.
7. **Drugi widget ili empirijski ParlaSent widget.** Odbija se. Jedan postojeći
   widget nosi poznati simulacijski mehanizam, dok stvarni tekst nosi razrađeni
   primjer i tiskane tablice.
8. **Tehnički NLP ili matematički tečaj strojnoga učenja.** Odbija se prema
   opsegu knjige. Studentski posao je prosuditi mjerenje, evaluaciju i odluku,
   ne izgraditi tokenizer ili istrenirati model.
9. **Više nepovezanih sustava ili katalog aktualnih alata.** Odbija se jer bi
   identitetski stup ponovno postao popis. Dodatni izvor ulazi samo ako
   podupire jedan korak istoga argumenta i prođe provjeru primarnoga izvora.

## Ovisnosti nakon odluke

Prihvaćanje uklanja autorski blocker samo s `G-A3-TEXT`, koji postaje sljedeći
dopušteni paket. `P3-TEXT`, `P3-VERIFY` i `WD-C17` i dalje čekaju vlastite
preduvjete, dok sljedeće sadržajne obveze ostaju `ratified` do njihova stvarnog
dokaza i implementacije:

- `R07-C17-full-argument`, `R07-C17-widget-prose-balance` i `R08-SPINE-17`;
- `R13-C17-module-contract`, `R13-C17-boundary-sensitivity`,
  `R13-C17-performance-validity` i `R13-C17-placement`;
- `R14-C17-classification-bridge`;
- `R23-C17-no-R-production`, `R23-C17-visible-receipt` i
  `R23-C17-no-tokenizer`;
- `R24-C17-primary-sources`, `R24-C17-LLM-prediction`,
  `R24-C17-system-feedback`, `R24-C17-recorded-reference`,
  `R24-C17-label-process`, `R24-C17-selective-observation` i
  `R24-C17-procedural-fairness`;
- `R24-LADDER-C17` i `R35-REACHBACK-17`.

Gate ne prihvaća te stavke. On samo zaključava pitanje, pravilo odabira, uloge
tekstnoga paketa, obris i isključenja prema kojima ih kasniji paketi moraju
dokazati.

## Granice podataka i ovlasti

DigiKat i Eurostat nisu izvori 17. poglavlja i ovaj ih brif ne prenamjenjuje.
Ako reach-back ili kasnija usporedba ipak spomene njihove već prihvaćene
rezultate, ostaju obvezne sve žive granice: nema DigiKatove tvrdnje o rastu ili
trendu preko 2024.; nema usporedbe prije i poslije prekida metode iz lipnja
2024. bez izričite napomene; nazivnik datoteke imenovanih domena ostaje
551.712; nema usporedbe interakcije ili dosega između mjerene i nemjerene
platforme; jaz iz 2024. ostaje vidljiv i neizglađen. Eurostat ostaje jedan
zajednički presjek za 2025. sa službenim zastavicama i nedostajanjem, bez
miješanja godina ili individualne i uzročne tvrdnje.

Poglavlje 6 ostaje `draft` i iz njega se ne izvodi nova prihvaćena tvrdnja.
Prihvaćanje brifa ne odobrava podatkovni paket, licencu, brojku, citat, prozu,
widget, zatvaranje sadržajnih stavki ni promjenu faze poglavlja. Ne tvrdi da je
autor pročitao poglavlje, da je poglavlje testirao novi čitatelj ili da je
terminologiju neovisno pregledala treća osoba.

Nema vanjske poruke, pusha, mergea, taga, arhiviranja, deploymenta ni objave.

## Odluka autora

Autor/editor Luka Sikic prihvatio je preporuku točnim odgovorom:

```text
G-A4-17 accepted as recommended for 26197f84889f1b1caffc25e4bbc171631328adb4 on 2026-08-18.
```

Odluka je vezana uz C16 closeout commit
`26197f84889f1b1caffc25e4bbc171631328adb4` i ne oslanja se na raniju opću
delegaciju. Zatvara samo `G-A4-17`; ne tvrdi da je autor pročitao 17. poglavlje
i ne prihvaća podatke, prava, rezultate, prozu ili ijednu od 20 kasnijih
sadržajnih obveza. `G-A3-TEXT` smije se preuzeti tek nakon zasebnoga closeouta,
provjera i lokalnoga commita ovoga gatea.
