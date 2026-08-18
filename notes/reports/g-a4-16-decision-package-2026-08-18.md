# G-A4-16 — odluka o objavljenom regresijskom artefaktu, pravima i mostu za binarni ishod

**Gate:** `G-A4-16`

**Stanje gatea:** prihvaćen kao preporučen.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 18. kolovoza 2026.

**Datum odluke:** 18. kolovoza 2026.

**Zaključano ulazno stanje:** C15 closeout commit
`a9697b1808765038e1d4a176223023e363ad3c3a`.

## Preduvjeti i granica paketa

`C15`, `P0-OUTSIDE`, `P3-ESS` i `P2-SPINE-V` prihvaćeni su. Ratificirana
kralježnica `16-regresija` zahtijeva jedan objavljeni rezultatni artefakt koji
učenik čita bez prilagodbe modela: tablicu, kratak prateći odlomak, referentne
skupine, koeficijente, neizvjesnost, specifikacije i granice tvrdnje. Ista
kralježnica dopušta samo omeđeni most prema binarnom ishodu; ne dopušta
prilagodbu ni izvođenje logističke regresije.

Potpuni pregled 97 handoffa ne nalazi isporuku ciljanu na `G-A4-16`. Zato nema
ulazne isporuke koju bi ovaj gate smio preuzeti ili potrošiti. Isporuke za
`WD-C16` ostaju tom paketu i ne smatraju se unaprijed ispunjenima.

Ovaj je paket samo odluka. Ne dohvaća ni promovira podatke, ne dodaje
bibliografski ključ, ne reproducira analizu, ne izrađuje sliku ili widget i ne
uređuje `chapters/16-regresija.qmd`.

## Preporučena odluka o artefaktu

Za omeđeni zadatak čitanja odabrati **Tablicu 3 i prvi rezultatni odlomak
neposredno pod njom** iz rada:

- Kleppang, A. L., Steigen, A. M., Ma, L., Søberg Finbråten, H. i Hagquist, C.
  (2021), *Electronic media use and symptoms of depression among adolescents
  in Norway*, *PLOS ONE*, 16(7), e0254197;
- članak i puni bibliografski zapis:
  `https://doi.org/10.1371/journal.pone.0254197`;
- točna Tablica 3:
  `https://doi.org/10.1371/journal.pone.0254197.t003`;
- odabrani odlomak počinje riječima `Table 3 presents the odds ratios` i
  završava riječima `3 hours and less per day`; ne preuzima se sljedeći odlomak
  o igranju i interakcijama.

Rad još nema ključ u `references.bib`. `WD-C16` smije ga dodati tek nakon
prihvaćanja ove odluke i zasebne provjere službenih metapodataka; ovaj gate ne
izmišlja ni rezervira ključ.

### Zašto artefakt odgovara 16. poglavlju

Službeni zapis opisuje anonimnu, samoprocjensku i presječnu anketu Ungdata iz
2018. među norveškim učenicima u dobi 15–16 godina. U istraživanju je
sudjelovalo 12.353 adolescenata, uz ukupnu stopu odaziva od 85 %. Ishod je u
radu dihotomiziran na simptome depresije na ili iznad 80. percentila nasuprot
nižem rezultatu. Autori su uporabu društvenih mreža i igranje podijelili na
više od tri sata dnevno nasuprot najviše tri sata te izvijestili binarnu
logističku regresiju.

Artefakt je prikladan jer na jednome malom prostoru omogućuje učeniku da:

- odvoji ishod, prediktor i referentnu skupinu;
- razlikuje `omjer izgleda` od vjerojatnosti, rizika i postotnih bodova;
- čita tri specifikacije i usporedi kako se procjene mijenjaju kada su obje
  uporabe medija u istome modelu;
- pročita 95-postotni interval prije zvjezdice ili ritualne odluke;
- poveže svaku rečenicu objavljenoga odlomka s točnim ćelijama i bilješkom;
- uoči da prilagodba za izmjerene kovarijate nije uzročna identifikacija;
- imenuje ono što tablica ne daje i zato ne smije rekonstruirati.

Presječni dizajn posebno je dobar za postojeću granicu poglavlja: sami autori
navode da se ne može odrediti smjer povezanosti ni izvesti uzročan zaključak,
a među ograničenjima navode samoprocjenu, moguću pogrešku mjerenja i
neizmjerene čimbenike.

### Točan sadržaj odabrane tablice

`WD-C16` mora precrtati semantički sadržaj tablice u vlastitu pristupačnu
hrvatsku tablicu; snimka zaslona, izdavačev PNG i TIFF nisu dopušteni. Moraju
se sačuvati sva tri stupca analize, obje referentne skupine, četiri procjene i
bilješka o prilagodbi:

| Prediktor i kategorija | Analiza 1: društvene mreže | Analiza 2: igranje | Analiza 3: oba prediktora |
|---|---:|---:|---:|
| Društvene mreže, najviše 3 sata | 1 (referentno) | — | 1 (referentno) |
| Društvene mreže, više od 3 sata | 1,60 (1,43–1,80) | — | 1,51 (1,34–1,70) |
| Igranje, najviše 3 sata | — | 1 (referentno) | 1 (referentno) |
| Igranje, više od 3 sata | — | 1,57 (1,36–1,80) | 1,38 (1,19–1,59) |

Sve su procjene prilagođeni omjeri izgleda s 95-postotnim intervalima;
bilješka izvornika navodi prilagodbu za rod, prijatelje, pušenje, visoko
obrazovanje roditelja i obiteljsku ekonomsku situaciju. Ishod je kodiran kao
simptomi depresije na ili iznad 80. percentila nasuprot rezultatu ispod njega.

Ove se brojke ovdje bilježe kao provjera identiteta i prikladnosti artefakta,
ne kao već unesena proza knjige. `WD-C16` ih mora ponovno provjeriti prema
službenom XML-u/HTML-u i zabilježiti izvorni položaj prije unosa.

### Plan prikaza tablice i odlomka

1. **Mjesto.** Artefakt ulazi u `Razrađeni primjer`, nakon mosta za binarni
   ishod. Ne zamjenjuje postojeću `Statistiku u divljini` o Table 2 Fallacy i
   ne stvara novu vršnu sekciju.
2. **Tablica.** Izraditi semantičku Quarto/Markdown tablicu s hrvatskim
   naslovima, pravilnim zaglavljima redaka, tekstualnim `referentno` i crticom
   samo ondje gdje prediktor nije u modelu. Ne kopirati grafički oblik
   izvornika.
3. **Odlomak.** Izraditi jedan kratki, označeno prilagođeni hrvatski prijevod i
   skraćenje samo odabranoga prvog odlomka. Zadržati vodič kroz stupce,
   prilagođene kovarijate, uspoređene skupine i vrijednost 1,60; ne dodavati
   tvrdnju koje u tome odlomku nema.
4. **Čitateljske oznake.** U autorskoj anotaciji imenovati red, stupac,
   referentnu kategoriju, procjenu, interval i bilješku koji podupiru svaku
   tvrdnju odlomka. Zasebno označiti što nije poduprto.
5. **Specifikacije.** Analize 1, 2 i 3 čitati kao različite specifikacije, ne
   kao tri replikacije i ne kao automatski test uzročnosti. Promjenu 1,60 na
   1,51 i 1,57 na 1,38 opisati uvjetno, bez priče o „nestanku učinka“.
6. **Vidljivo odsutno.** Uz tablicu navesti da ona ne izvještava
   model-specifični `N`, mjeru pristajanja ili dijagnostiku modela, p-vrijednost
   ni zvjezdice, presretanje, osnovne izglede, apsolutni rizik, omjer rizika ili
   predviđenu vjerojatnost. Broj 12.353 smije se navesti samo kao broj
   sudionika opisan u metodama, ne kao dokaz da je svaki model imao isti `N`.
7. **Bez ponovne analize.** Učenik dobiva tablicu i odlomak te odgovara
   čitanjem. Nema skupa podataka, rekonstrukcije pojedinačnih redaka,
   prilagodbe modela, R/OJS proizvodnje, izračuna vjerojatnosti iz pretpostavljene
   baze ni traženja pristupa podacima Ungdata.

## Preporučena odluka o pravima

Prihvatiti **prilagođenu tablicu i prilagođeni prijevod odlomka prema licenci
CC BY 4.0** kao dokumentiranu zakonitu osnovu, bez zahtjeva za zasebnim
dopuštenjem i bez tvrdnje da je dopuštenje zatraženo ili dobiveno.

Na službenoj stranici članka stoji da je rad otvoreno dostupan pod licencom
Creative Commons Attribution, koja dopušta uporabu, distribuciju i
reprodukciju u bilo kojem mediju uz navođenje izvornoga autora i izvora.
PLOS-ova politika veže sadržaj uz CC BY 4.0. Službeni sažetak CC BY 4.0
dopušta dijeljenje i prilagodbu, uključujući komercijalnu uporabu, uz primjereno
pripisivanje, poveznicu na licencu, oznaku izmjena i bez dodatnih ograničenja.

Uvjeti koje `WD-C16` mora primijeniti u HTML-u, PDF-u i DOCX-u:

- puna bibliografska atribucija autorima i radu, DOI članka i DOI Tablice 3;
- poveznica `https://creativecommons.org/licenses/by/4.0/` i oznaka
  `CC BY 4.0`;
- jasna napomena da su prijevod, skraćivanje, izbor redaka/zaglavlja i
  preoblikovanje tablice izmjene autora knjige;
- nijedan znak da PLOS ili autori podupiru knjigu ili prilagodbu;
- bez tehnološke ili ugovorne zabrane koja bi primatelju oduzela prava iz
  licence;
- naknada: nema licencne naknade prema javno objavljenim uvjetima;
- datum provjere uvjeta: 18. kolovoza 2026.

Rad dopušta pristup podacima samo istraživačima na zahtjev. Licenca članka ne
pretvara podatke Ungdata u otvorene podatke i ne odobrava njihovo preuzimanje,
pakiranje ili redistribuciju. Ovaj je izbor zato namjerno artefakt za čitanje,
ne podatkovni paket.

Predložena atribucijska formula, koju `WD-C16` mora provjeriti u stvarnom
formatu, glasi sadržajno: prilagođeno prema Kleppang i sur. (2021), Tablica 3,
DOI rada i tablice, CC BY 4.0; prijevod, skraćivanje i preoblikovanje tablice
izradio autor knjige. Gate prihvaća taj ugovor, ali ne unosi konačnu legendu u
poglavlje.

## Preporučena odluka o mostu za binarni ishod

Most se **ne odgađa**: uključiti ga u `WD-C16`, ali samo kao čitateljski most
potreban za odabrani artefakt. Mora doći neposredno prije objavljene tablice i
obuhvatiti:

1. vjerojatnost i izglede kao različite prikaze binarnoga ishoda;
2. referentnu skupinu i smjer usporedbe;
3. `omjer izgleda` kao omjer dvaju izgleda, ne kao omjer vjerojatnosti;
4. 95-postotni interval kao raspon procjena spojivih s podacima i modelom;
5. izričitu zabranu čitanja 1,60 kao „60 postotnih bodova više“, „60 % veća
   vjerojatnost“ ili dokaz uzročnoga učinka;
6. `predviđenu vjerojatnost` kao često razumljiviji prikaz koji iz ove tablice
   nije dostupan, jer nedostaju presretanje, profil kovarijata i osnovni
   izgledi.

Dopušten je samo kratki hipotetski aritmetički primjer pretvaranja jedne jasno
izmišljene vjerojatnosti u izglede i natrag, ako je potreban za pojam. Mora biti
označen kao hipotetski i ne smije se pripisati radu. Nisu dopušteni formula i
izvod logističke funkcije, prilagodba logističkoga modela, procjena iz
pojedinačnih podataka, računanje empirijske predviđene vjerojatnosti ili
uvođenje novoga ocijenjenog postupka.

Most rabi ratificirane oblike `omjer izgleda` i `predviđena vjerojatnost`.
`Izgledi` ostaju postojeći ključni pojam kralježnice; ovaj gate ne odobrava novi
`#def-` blok. Postojeći središnji widget `w16` ostaje regresijski pravac i
njegov statički blizanac; nema drugoga widgeta.

## Uloga u argumentu 16. poglavlja

Odluka ne mijenja sedmodijelni kostur. `WD-C16` treba povezati artefakt s
ratificiranom kralježnicom ovim redom:

1. izgraditi linearnu regresiju kao sintezu pravca, sredine, reziduala,
   najmanjih kvadrata i uvjetne procjene;
2. odvojiti opis, prilagodbu za kovarijate, predviđanje i uzročnu tvrdnju;
3. zadržati `w16` kao jedinu interakciju za nagib, presretanje i reziduale;
4. sačuvati postojeći slučaj Table 2 Fallacy kao upozorenje da koeficijent
   mijenja značenje među specifikacijama;
5. uvesti omeđeni binarni most samo zato što izabrana tablica izvještava
   omjere izgleda;
6. u razrađenom primjeru prvo pročitati strukturu tablice, zatim svaku tvrdnju
   odlomka vezati uz dokaz i naposljetku zapisati nedostupne tvrdnje;
7. završiti uvjetnim izvještajem: povezanost u presječnom uzorku i zadanom
   modelu, uz navedene kovarijate, bez uzročne ili individualne prognoze.

## Tvrdnje koje artefakt ne dopušta

Ovaj izbor ne dopušta tvrdnju:

- da je više od tri sata društvenih mreža ili igranja uzrokovalo simptome
  depresije;
- da omjer izgleda 1,60 znači 60 % veću vjerojatnost ili 60 postotnih bodova;
- da je omjer rizika jednak omjeru izgleda;
- kolika je predviđena vjerojatnost za bilo kojeg učenika ili skupinu;
- da je ukupnih 12.353 ušlo u svaki model;
- da su svi relevantni čimbenici kontrolirani ili da su skupine usporedive kao
  u randomiziranom pokusu;
- da interval opisuje 95 % pojedinaca ili jamči praktičnu važnost;
- da mala promjena procjene među stupcima dokazuje stabilnost, medijaciju ili
  odsutnost pristranosti;
- da neobjavljeni p-pokazatelj, zvjezdica, pristajanje ili dijagnostika prolazi
  samo zato što ih tablica ne prikazuje;
- da licenca članka dopušta preuzimanje ili redistribuciju podataka Ungdata.

Ako `WD-C16` ne može potvrditi bilo koju nosivu brojku, metapodatak ili uvjet
licence iz službenoga zapisa, ne smije ga nadomjestiti približnom ili
zapamćenom vrijednošću. Mora zabilježiti blocker i vratiti izbor autoru.

## Alternative i razlozi odbijanja

1. **Westreich i Greenland (2013), postojeći slučaj Table 2 Fallacy.** Izravno
   podupire najvažnije upozorenje o promjeni procjenjivane veličine među
   specifikacijama i ostaje u `Statistici u divljini`. Nije odabran kao
   rezultatni artefakt jer nije jedna kompaktna empirijska tablica s kratkim
   odlomkom za čitanje, a službena izdavačeva stranica ne daje jednako jasnu
   CC BY osnovu za prilagodbu tablice.
2. **Sserunkuuma i sur. (2023), PLOS ONE, hijerarhijska linearna regresija
   problematične uporabe medija i depresije.** Ima otvorenu CC BY rutu i ostaje
   zakonita pričuvna mogućnost s kontinuiranim ishodom. Nije preporučena jer je
   tablica osjetno gušća, uzorak je mali presječni pilot među studentima
   medicine, a pet modela bi opteretilo osnovnu čitateljsku zadaću i uklonilo
   ratificirani binarni most.
3. **Chouldechova (2017), regresijska tablica u slučaju pravednosti
   predviđanja recidivizma.** Sadržajno je snažna, ali pripada nosivom luku 17.
   poglavlja o klasifikaciji i pravednosti. Uvođenje ovdje unaprijed bi potrošilo
   njegov glavni slučaj, a dostupnost rukopisa sama ne rješava uvjete
   preoblikovanja točne objavljene tablice.
4. **Izmišljena ili sintetička regresijska tablica.** Odbija se jer obveza
   traži objavljen rezultat i jer bi izmišljena empirijska tvrdnja prekršila
   dokazni ugovor knjige.
5. **Ponovna prilagodba na ESS-u ili podacima Ungdata.** Odbija se. ESS ostaje
   neobvezan, portalom posredovan i nepromoviran; podaci Ungdata nisu preuzeti
   ni licencirani za paket. Obvezni izvanmrežni zadatak `WD-C16` mora ostati na
   već licenciranoj `populacija_medija` i ne smije glumiti replikaciju
   objavljenoga rada.

## Blokirane ovisnosti

Do sva tri točna odgovora autora ostaju blokirani `G-A4-16`, `WD-C16`, `C16` i
`G-A4-17`, a time i:

- `R16-ARTIFACT-selection`;
- `R16-C16-table`, `R16-C16-paragraph` i `R16-C16-no-refit`;
- bilo koji bibliografski unos, prilagođena tablica, prijevod odlomka ili most
  za binarni ishod u poglavlju 16;
- svaka tvrdnja da su prava riješena za sva tri ciljna formata.

Gate ne prihvaća te sadržajne stavke. On samo zaključava odluku po kojoj ih
`WD-C16` mora dokazati na konačnom izvornom stanju.

## Granica ovlasti

Prihvaćanje triju preporuka odobrava samo točan izbor Tablice 3 i prvoga
rezultatnog odlomka, opisani CC BY 4.0 ugovor za prilagođenu tablicu i
prilagođeni prijevod te omeđeni čitateljski most za binarni ishod. Ne odobrava
pristup ili redistribuciju podataka, izravnu kopiju izdavačeve grafike,
logističku regresiju kao novi postupak, novu interakciju, konačnu prozu,
neprovjerenu brojku, zatvaranje sadržajne stavke ni početak `WD-C16` prije
zasebnoga closeouta i commita ovoga gatea.

Poglavlje 6 ostaje `draft`. Nema vanjske poruke, pusha, mergea, taga,
arhiviranja, deploymenta ni objave.

## Odluka autora

Autor/editor Luka Sikic prihvatio je sve tri preporuke doslovnim odgovorom:

```text
G-A4-16 ARTIFACT accepted as recommended for a9697b1808765038e1d4a176223023e363ad3c3a on 2026-08-18.
G-A4-16 RIGHTS accepted as recommended for a9697b1808765038e1d4a176223023e363ad3c3a on 2026-08-18: use the CC BY 4.0 adapted-table and adapted-paragraph route.
G-A4-16 BRIDGE accepted as recommended for a9697b1808765038e1d4a176223023e363ad3c3a on 2026-08-18: include the bounded binary-outcome reading bridge in WD-C16.
```

Ova odluka zatvara samo `G-A4-16`. `WD-C16` smije početi tek nakon zasebnoga
closeouta, provjera i lokalnoga commita ovoga gatea.
