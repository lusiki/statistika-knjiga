# G-A2b-II — ratificirana kralježnica Dijela II

**Gate:** `G-A2b-II`

**Datum odluke:** 4. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** prihvaćeno kako je ovdje nacrtano.

**Izvorno stanje odluke:**
`conversation:G-A2b-II-spine-approved-2026-08-04-Luka-Sikic`, vezano uz nacrt
kralježnice u ovom dokumentu.

## Što ovaj gate odlučuje

Gate odobrava jednu konkretnu nacrtanu kralježnicu Dijela II: nosive aspekte,
nosive pojmove, preduvjete i isključenja za poglavlja 4, 5 i 6, ugovor na razini
dijela te hijerarhiju definicija kojom se rješava stavka
`R04-C04-definition-load`. Ne odobrava prozu, ne dodaje i ne uklanja nijedan
`#def-` blok i ne ratificira nijednu kasniju kralježnicu.

Autorova je namjera zabilježena unaprijed u
`notes/reports/author-pre-dispositions-2026-08-04.md`. Taj dokument izričito nije
ratifikacija. Ovaj se gate zatvara protiv stvarnoga nacrta iz ovoga zapisa.

## Ulazi pročitani prije odluke

Pročitani su u cijelosti: ugovor paketa `decision_gate`, vanjski upit
`OA-G-A2B-II-SPINE`, upravljane stavke `R04-SPINE-II` i `R04-C04-definition-load`,
prihvaćene arhitekture `G-A2a` i `G-A2d`, identitetski brifovi `P2-IDENTITY`,
ratificirane kralježnice predgovora i Dijela I, zabilježena autorova namjera,
pravilo `H10` u `STYLE.md`, pojasevi `bands` u `conventions.json` te sve stavke
registra koje ciljaju poglavlja 4, 5 i 6.

Cjeloviti ledger prijenosa pročitan je prije odluke. Nijedan prijenos ne cilja
`G-A2b-II`, pa nema dolazne isporuke koju bi ovaj gate priznao ili potrošio.
Dva prijenosa dodiruju Dio II i oba ostaju `pending` i nepotrošena ovdje:

- `H-P1C-INTEGRITY-001` cilja `WB-C05` i vlasnik je duga uvoda za
  `fig-anscombe`. Ovaj gate taj dug imenuje, ali ga ne preuzima i ne naplaćuje.
- `H-P1C-INTEGRITY-002` cilja `P2-TERMS` i zamrzava točan skup od 46 živih
  definicija, ledger pojmova i generirani graf. Zato ovaj gate odlučuje samo
  kartu definicija, a nijedan blok ne piše i ne briše.

## Ugovor na razini Dijela II

Dio II nosi tri koraka i ništa više: **analitička se tablica gradi, a ne
nalazi**, zatim **vizualna tvrdnja mora biti poštena**, zatim **povezanost ima
granice**. Poglavlje 4 pokazuje kako izvorni zapisi postaju jedna tablica i tek
onda što se iz nje smije sažeti, poglavlje 5 pokazuje da je prikaz argument koji
se provjerava, a poglavlje 6 pokazuje dokle zajedničko kretanje seže i gdje
prestaje.

Redoslijed je nosiv, a ne uredski. Konvencionalni poredak u kojemu mjere
središta otvaraju dio **izričito je odbijen**: sažetak se ne smije pojaviti prije
nego što je čitatelj vidio kako je nastao redak koji se sažima. Vizualizacija
također ne vodi: prikaz dolazi nakon tablice koju prikazuje.

Dio nosi nit konstruiranih podataka koju kasnije žanju poglavlja 8 i 16.
Poglavlje 8 iz nje uzima da uzorak nije zatečen skup redaka nego rezultat
postupka, a poglavlje 16 da svaka varijabla u modelu nosi trag odluka o
jedinici, spajanju, rekodiranju i nedostajućim vrijednostima.

Dio naglašava tri faze životnoga ciklusa iz prihvaćene arhitekture: provjeru,
pripremu i istraživanje. Sadi dvije niti — reproducibilnost i podrijetlo te
komunikaciju tvrdnje — i razvija tri: jedinicu analize, nazivnik te selekciju i
odsutnost. Na granici dijela nosi punu mapu tvrdnji sa šest dimenzija i šest
revizijskih pitanja te odgovorivu samoprovjeru, prema prihvaćenoj arhitekturi
`G-A2a`.

Dio II prvi je dio u kojemu ljestvica AI kompetencija traži **čitljivu potvrdu
provjere**. Vidljivi kod ovdje je potvrda koja se čita, a ne zadatak koji se
piše: nijedan ocijenjeni zadatak nigdje u dijelu ne traži pisanje koda, prema
odluci D05 i pravilu H10.

## Nacrtana kralježnica po poglavljima

### Poglavlje 4 — Sažimanje podataka

**Nosivi aspekti**

1. Analitička se tablica gradi, a ne nalazi: od izvornih zapisa do jedne tablice
   kroz provjeru jedinice, spajanja koja množe retke, rekodiranja, filtre te
   odnos ukupnoga iznosa i sastavnica.
2. Jedan redak, jedna jedinica: dohvat jedinice analize iz poglavlja 1 unutar
   stvarne tablice i trenutak u kojemu spajanje mijenja što redak predstavlja.
3. Nedostajuće vrijednosti kao svjedočanstvo o postupku koji je podatke
   proizveo, a ne kao tehnička smetnja; jedna vidljiva osjetljivost na odluku o
   nedostajućim vrijednostima.
4. Nazivnik kao odluka unutar tablice, pokazana omeđenim primjerom brojanja
   riječi.
5. Mjere središta i raspršenosti kao odgovor na pitanje koje je tablica tek
   omogućila, a ne kao obredni otvor poglavlja.
6. Oblik i položaj: asimetrija čitana iz razmaka sredine i medijana te
   standardizirana vrijednost kao jezik položaja koji kasnija poglavlja
   preuzimaju.
7. Poštena rečenica izvještaja: čitatelj sam izriče procjenu s jedinicom,
   populacijom i granicom, a ne samo revidira tuđu tvrdnju.
8. Vidljiv trag od izvora do tablice: transformacija se može pregledati i
   ponoviti.
9. Asistent kao pogrešiv analitičar čija aritmetika može biti točna nakon
   pogrešnoga spajanja; potvrda provjere imenuje što je provjereno i kako.

**Nosivi pojmovi**: analitička tablica, spajanje, nedostajuća vrijednost,
osjetljivost na odluku o podacima, aritmetička sredina, medijan, standardna
devijacija, standardizirana vrijednost, poštena rečenica izvještaja, trag
transformacije.

**Preduvjeti**: poglavlja 1, 2 i 3.

**Isključenja**: nikakva teorija uzorkovanja, populacijska procjena ni interval,
koji pripadaju poglavljima 8 i 9; nikakav test ni p-vrijednost; nikakva
proizvodnja višestruke imputacije ni napredno rukovanje nedostajućim
vrijednostima, prema odgodi `R11-SCOPE-no-multiple-imputation`; nijedan
ocijenjeni zadatak pisanja koda, uz vidljivi kod koji se čita kao potvrda;
nijedan izmišljen ili neizvorni empirijski primjer, pa tvrdnja o obliku
angažmana mora biti izvorna ili izričito označena kao simulacija; nijedan šesti
`#def-` blok, jer poglavlje ostaje unutar ratificiranoga pojasa; mjere središta
ne otvaraju poglavlje; odabir podatkovnoga paketa ostaje gateovima
`G-A3-DIGIKAT` i `G-A3-EUROSTAT`.

### Poglavlje 5 — Vizualizacija

**Nosivi aspekti**

1. Vizualna tvrdnja mora biti poštena: graf je argument, a argument se
   provjerava.
2. Gramatika grafike kao rječnik koji izbor čini vidljivim: podaci,
   pridruživanje, geometrija i ljestvica.
3. Što oko može očitati: položaj, duljina, kut, površina i boja ne nose istu
   preciznost.
4. Os, ishodište i ljestvica kao tvrdnje, a ne kao ukras; skraćena os mijenja
   zaključak čitatelja i time izravno odgovara na poglavlje 3.
5. Nazivnik dohvaćen vizualno: udio i broj ne daju istu sliku.
6. Anscombeov kvartet nosi razlog zašto sažetak ne može zamijeniti prikaz.
   Njegov uvod prije prikaza obveza je paketa `WB-C05` pod prijenosom
   `H-P1C-INTEGRITY-001` i ovdje se ne naplaćuje.
7. Mala višestruka polja kao pošten način usporedbe skupina bez četiriju
   neusporedivih ljestvica.
8. Prikaz asimetrične učestalosti riječi priprema poglavlje 17 bez poučavanja
   obrade prirodnoga jezika.
9. Pristupačnost kao dio argumenta: prikaz preživljava gubitak boje, a njegov
   uvod i tekstualni opis nose značenje.
10. Svaki prikaz ima vlastitu argumentacijsku funkciju; gustoća se prikaza
    prosuđuje po toj funkciji, a ne po broju.

**Nosivi pojmovi**: gramatika grafike, pridruživanje, ljestvica, skraćena os,
mala višestruka polja, Anscombeov kvartet, prikaz učestalosti riječi,
pristupačnost prikaza.

**Preduvjeti**: poglavlja 3 i 4.

**Isključenja**: nijedan novi središnji widget; postojeći par `w05` ostaje;
nikakav test, interval ni model, koji pripadaju poglavljima 9, 10 i 16; nijedan
ocijenjeni zadatak pisanja koda, uz vidljivi kod prikaza koji se čita kao trag
računa; nijedan izmišljen ili neizvorni empirijski primjer; nikakva metoda
obrade prirodnoga jezika, jer je prikaz učestalosti prikaz, a ne postupak;
nikakav improviziran ugrađeni stil ni vlastiti `<div>`; dug uvoda za
`fig-anscombe` ostaje paketu `WB-C05`.

### Poglavlje 6 — Povezanost

**Nosivi aspekti**

1. Povezanost ima granice: dvije veličine koje se kreću zajedno tvrde upravo
   toliko i ništa više.
2. Dijagram raspršenja prva je dijagnostika, a koeficijent je izvedeni sažetak.
3. Kovarijanca i korelacija kao ista zamisao u dvjema ljestvicama, jedna s
   jedinicama i jedna bez njih.
4. Što jedan koeficijent može i ne može reći: oblik odnosa, netipična i utjecajna
   opažanja ostaju nevidljivi u jednom broju.
5. Rangovi umjesto vrijednosti: podudarnost Pearsonova i Spearmanova koeficijenta
   samo je naznaka, a njihovo neslaganje poziv na pogled u podatke.
6. Ograničenje raspona kao problem selekcije: slabljenje ovisi o obliku odnosa,
   raspršenosti i načinu odabira, a moguće je i jačanje i obrat predznaka.
7. Predznak se može preokrenuti: Simpsonov paradoks iz poglavlja 1 dohvaćen
   unutar stvarne povezanosti, a uzročni rječnik poglavlja 2 dohvaćen kao granica
   tvrdnje.
8. Kodirana kategorija teksta može ući u povezanost i pritom ostaje mjerna
   odluka.
9. Granica tvrdnje: povezanost podupire tvrdnju o povezanosti, dok generalizacija
   i uzročnost traže ono čime ovo poglavlje ne raspolaže.
10. Granica Dijela II: puna mapa tvrdnji sa šest dimenzija i šest revizijskih
    pitanja, odgovoriva samoprovjera, prvi zadatak dohvata unatrag i nastavak
    niti o komunikaciji tvrdnje.

**Nosivi pojmovi**: kovarijanca, korelacija, Spearmanov koeficijent ranga,
ograničenje raspona, utjecajno opažanje, oblik odnosa, kodirana kategorija
teksta, granica tvrdnje o povezanosti.

**Preduvjeti**: poglavlja 2, 4 i 5.

**Isključenja**: nikakav pravac regresije kao model ni metoda najmanjih kvadrata,
koji pripadaju poglavlju 16; nikakav test koeficijenta ni interval, koji
pripadaju poglavljima 9 i 10; nikakva formalna uzročna identifikacija, jer se
uzročna granica dohvaća na razini pismenosti iz poglavlja 2, a rješava u
poglavlju 16; dijagram raspršenja ne smije se podrediti koeficijentu; nikakva
metoda obrade prirodnoga jezika; nijedan ocijenjeni zadatak pisanja koda;
nijedan izmišljen ili neizvorni empirijski primjer; odabir podatkovnoga paketa
ostaje gateovima `G-A3-DIGIKAT` i `G-A3-EUROSTAT`.

## Hijerarhija definicija za Dio II

Ovaj gate rješava stavku `R04-C04-definition-load`. Pregled je našao da
poglavlje 4 nosi šest `#def-` blokova, a ratificirani pojas
`bands.definitions_per_chapter` dopušta jedan do pet. Svaka od šest definicija
ovdje dobiva izričitu dispoziciju prema svojoj nosivoj ulozi.

| Definicija poglavlja 4 | Dispozicija | Razlog i imenovani kasniji ovisnik |
|---|---|---|
| aritmetička sredina | zadržati | Poglavlje 8 gradi distribuciju uzorkovanja sredine, poglavlje 9 interval za sredinu, poglavlja 14 do 16 razliku sredina |
| medijan | zadržati | Poglavlje 9 gradi bootstrap medijana ondje gdje formule nema |
| varijanca | spojiti u standardnu devijaciju | Ista veličina u dvjema ljestvicama; jedan blok definira standardnu devijaciju i unutar iste rečenice imenuje varijancu kao njezin kvadrat |
| standardna devijacija | zadržati kao nositelj spoja | Poglavlje 8 iz nje izvodi standardnu pogrešku, poglavlje 15 omjer varijanci, poglavlje 16 raspršenost oko modela |
| asimetrija | spustiti u prozu uz `.pojam` | Nijedno kasnije poglavlje ne ovisi o formalnoj definiciji; pojam radi kao opisni rječnik za čitanje oblika, a poglavlje 9 asimetriju imenuje bez bloka |
| standardizirana vrijednost | zadržati | Poglavlje 6 njome gradi Pearsonov koeficijent, poglavlje 7 položaj na normalnoj krivulji, poglavlje 11 standardiziranu razliku |

Nijedna se definicija ne premješta u drugo poglavlje. Premještanje bi značilo da
pojam prvi put treba drugdje, a sva četiri zadržana pojma prvi put stvarno
trebaju upravo u poglavlju 4, gdje ih tablica omogućuje.

Poglavlje 4 time prelazi sa šest na četiri bloka i ulazi u pojas. Poglavlja 5 i 6
zadržavaju svoja postojeća tri bloka nepromijenjena: `gramatika grafike`,
`pridruživanje` i `mala polja` u poglavlju 5 te `kovarijanca`, `korelacija` i
`ograničenje raspona` u poglavlju 6.

Neto učinak na zamrznuti skup jest smanjenje sa 46 na 44 žive definicije. Ovaj
gate nijedan blok ne piše i ne briše. Kartu provode `WB-C04` nad stvarnom
prozom i `P2-TERMS` nad ledgerom i grafom pojmova, nakon što `G-A2c` utvrdi
kanonske hrvatske oblike.

Prvi je susret uvijek prije formalizacije. Nijedan `#def-` blok ne stoji prije
nego što je pojam doživljen u prozi, prikazu ili widgetu.

## Podudarnost sa zabilježenom namjerom

| Zabilježena namjera | Gdje je provedena |
|---|---|
| Nosiv slijed: tablica se gradi, vizualna tvrdnja mora biti poštena, povezanost ima granice | Ugovor dijela i prvi aspekt svakoga od triju poglavlja |
| Dio nosi nit konstruiranih podataka koju žanju poglavlja 8 i 16 | Ugovor dijela; aspekti 4.1, 4.2, 4.3 i 4.8 |
| Vizualizacija ne vodi | Ugovor dijela; poglavlje 5 ima poglavlje 4 kao preduvjet |
| Konvencionalni poredak sa sažecima na početku izričito je odbijen | Ugovor dijela; aspekt 4.5 i sedmo isključenje poglavlja 4 |
| Riješiti `R04-C04-definition-load` po nosivoj ulozi svake definicije | Hijerarhija definicija; svih šest definicija ima izričitu dispoziciju |

Ostali aspekti nisu novi zahtjevi. Svaki provodi već ratificiranu stavku registra
ili prihvaćenu arhitekturu.

| Aspekt | Već ratificirani izvor |
|---|---|
| 4.1 i 4.2 gradnja tablice i jedinica retka | `R11-C04-raw-to-table`, nit `unit_of_analysis` |
| 4.3 nedostajuće vrijednosti i osjetljivost | `R11-C04-missingness` |
| 4.4 nazivnik u tablici | `R13-C04-denominators`, nit `denominator` |
| 4.7 poštena rečenica | `claim_registry.honest_sentence_standard`, mjesto sadnje `04-sazimanje-podataka` |
| 4.8 trag transformacije | nit `reproducibility_and_provenance`, mjesto sadnje |
| 4.9 pogrešno spajanje s točnom aritmetikom | `R11-C04-wrong-join-AI`, ljestvica `part_ii` |
| 5.6 i 5.10 Anscombe i gustoća prikaza | `R31-C05-Anscombe`, `R28-C05-density`, dug u `R28-C05-introduction` |
| 5.8 prikaz učestalosti riječi | `R13-C05-frequency-visual` |
| 6.2, 6.5 i 6.6 dijagram, rangovi i ograničenje raspona | prihvaćeni `R09-C06-scatterplot-primary`, `R09-C06-pearson-spearman-agree`, `R09-C06-pearson-spearman-disagree`, `R09-C06-range-restriction` |
| 6.8 kodirana kategorija | `R13-C06-coded-association` |
| 6.10 granica dijela | `G-A2a` `claim_registry.placement_rule`, `R35-SELF-CHECK-II` |
| prijelaz 3 na 4 kao odgovor na zavodljiv prikaz | `R27-C03-04-transition` |
| zahtjev za čitljivom potvrdom provjere | `assessment_architecture.ai_competence_registry.stage_ladder.part_ii` |

Nacrt ne odstupa od zabilježene namjere ni u jednoj točki.

## Razmotrene alternative

1. **Zadržati konvencionalni poredak u kojemu mjere središta otvaraju poglavlje
   4.** Odbijeno: proturječi zabilježenoj namjeri i stavci `R11-C04-raw-to-table`,
   a čitatelja uči sažimati redak prije nego što zna što redak predstavlja.
2. **Staviti vizualizaciju pred sažimanje.** Odbijeno: proturječi zabilježenoj
   namjeri i odluci D03 o očuvanju makro-poretka; prikaz bez konstruirane tablice
   nema što provjeriti.
3. **Ostaviti svih šest definicija poglavlja 4 nepromijenjenima.** Odbijeno:
   ostavlja poglavlje izvan ratificiranoga pojasa i ne rješava stavku
   `R04-C04-definition-load`.
4. **Spustiti u prozu i asimetriju i standardiziranu vrijednost.** Odbijeno:
   standardizirana vrijednost ima tri imenovana kasnija ovisnika, pa bi njezino
   spuštanje razbilo lanac prema poglavljima 6, 7 i 11.
5. **Premjestiti varijancu u poglavlje 8 uz standardnu pogrešku.** Odbijeno:
   varijanca je potrebna već u poglavlju 4 da bi standardna devijacija imala
   smisla, a premještanje bi stvorilo unatražnu ovisnost.
6. **Dodati poglavlju 4 blok za analitičku tablicu.** Odbijeno: stavka koja se
   ovdje rješava traži smanjenje definicijskoga opterećenja, a pojam nosi vidljiv
   postupak gradnje tablice, ne formalna definicija.
7. **Preuzeti dug uvoda za `fig-anscombe` u ovaj gate.** Odbijeno: dug je
   vlasništvo prijenosa `H-P1C-INTEGRITY-001` prema `WB-C05` i naplaćuje se nad
   stvarnom prozom, a ne nad registrom.

## Granica autoriteta

Ovaj gate odobrava isključivo kralježnicu Dijela II i njezinu hijerarhiju
definicija. Ne odobrava prozu poglavlja 4, 5 ni 6 i ne mijenja nijednu datoteku
poglavlja. Ne dodaje, ne briše i ne spaja nijedan `#def-` blok i ne regenerira
graf pojmova; to ostaje paketima `WB-C04`, `WB-C05`, `WB-C06` i `P2-TERMS`. Ne
troši `H-P1C-INTEGRITY-001` ni `H-P1C-INTEGRITY-002`, koji ostaju obveze paketa
`WB-C05` i `P2-TERMS`. Ne utvrđuje kanonsku terminologiju, koja ostaje gateu
`G-A2c`. Ne ratificira nijednu kasniju kralježnicu. Ne bira slučaj, izvor ni
podatkovni paket. Ne mijenja fazu nijedne jedinice, koja ostaje `draft`. Ne
odobrava render, generirani artefakt, push, merge, tag, arhiviranje, deployment
ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

- stavke `R04-SPINE-II` i `R04-C04-definition-load`;
- paket `P2-SPINE-II`, koji ovu kralježnicu upisuje u
  `bookwright_plugin/bookwright/shared/chapter-spine.json`.

Ovisnosti koje ostaju blokirane: `WB-C04`, `WB-C05` i `WB-C06` čekaju
`P3-VERIFY-B`, podatkovne gateove `G-A3-DIGIKAT` i `G-A3-EUROSTAT` te svoje
gateove prihvaćanja `C04`, `C05` i `C06`; `P2-TERMS` čeka `G-A2c`; `WB-PART`
čeka svoja tri poglavlja.
