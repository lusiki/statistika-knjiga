# G-A3-TEXT — odluka o odabiru i pravima tekstnoga paketa

**Gate:** `G-A3-TEXT`

**Stanje gatea:** pripremljen; čeka dvije odvojene točne odluke autora/editora.

**Imenovani vlasnik obiju odluka:** Luka Sikic, autor/editor.

**Datum pripreme:** 18. kolovoza 2026.

**Zaključano ulazno stanje:** G-A4-17 closeout commit
`7298a62a1c030f80c3d65443e8d311c76e1b1205`.

## Preduvjeti, handoffovi i granica paketa

`G-A4-17`, `P0-OUTSIDE` i `P3-CATALOG` prihvaćeni su. Prihvaćeni brif 17.
poglavlja veže tekstni paket uz jednu nastavnu odluku: treba li odabranu
parlamentarnu rečenicu poslati u ljudski pregled za mogući javni sažetak.
Empirijski paket ne dokazuje da je ijedna imenovana ustanova takav sustav
uvela.

`H-P1B-DATA-LIC-003` potrošen je prije claima. On za oba izvora daje samo
opći temelj za traku `bundled`: ParlaMint-HR pod CC BY 4.0 i ParlaSent pod
CC BY-SA 4.0. Opći temelj nije točan paketni zapis. `H-P3-CATALOG-001` priznat
je na gateu `before_close`, ali nije potrošen: closeout još nema autorske
odluke, a P3-TEXT tek mora izraditi i provjeriti točan paketni zapis.

Ovaj gate ne dohvaća arhive, ne stvara kandidata, ne mijenja `data/katalog.yml`,
ne promovira paket, ne dodaje bibliografski ključ i ne mijenja 17. poglavlje,
widget ni zajedničke registre. Ne tvrdi da je zatraženo ili dobiveno posebno
dopuštenje nositelja prava; nijedno nije traženo.

## Službeni zapisi provjereni bez dohvaćanja podataka

Provjera je 18. kolovoza 2026. čitala samo službene metapodatkovne i licenčne
zapise.

| Izvor | Točno izdanje i službena datoteka | Službeni integritet | Objavljena licenca |
|---|---|---|---|
| ParlaMint-HR | ParlaMint 5.0, CLARIN.SI `11356/2004`, izdanje 8. srpnja 2025.; `ParlaMint-HR.tgz` | MD5 `b852098ae5c2561aef1de43f44e09a77` | CC BY 4.0 |
| ParlaSent BCS za učenje | ParlaSent 1.0, CLARIN.SI `11356/1868`, izdanje 18. rujna 2023.; `ParlaSent_BCS.jsonl` | MD5 `c8b59c84c476b031cc553bc3c768e627` | CC BY-SA 4.0 |
| ParlaSent BCS za ispitivanje | isto izdanje; `ParlaSent_BCS_test.jsonl` | MD5 `ee8699a4a7b1a834f79fe74b8ebdfaf1` | CC BY-SA 4.0 |
| ParlaSent opis polja | isto izdanje; `README.txt` | MD5 `583856c8d470334e5638f6a078f727d5` | CC BY-SA 4.0 kao dio zapisa |

Službeni ParlaMint zapis navodi da arhiva sadrži TEI tekst, izvedeni obični
tekst i TSV metapodatke govora. Službeni ParlaSent README navodi polja
`country`, `annotator1`, `annotator2`, `reconciliation`, `label`,
`document_id`, `sentence_id`, `term`, `date`, `name`, `party` i `gender` za
podatke za učenje. Isti zapis otkriva važnu asimetriju: BCS podaci za učenje
označeni su s dva kodera i postupkom usklađenja, dok je BCS skup za ispitivanje
označio jedan uvježbani koder. Paket zato ne smije izmisliti dvije oznake ili
„usklađenje” za ispitne retke.

Javni README ne izlistava zasebnu shemu ispitne datoteke. Službeni metapodaci
zato čine zemljopisni rez i pokušaj veze po dokumentu i rečenici izvedivima za
podatke za učenje, ali **ne dokazuju** da ispitna datoteka nosi ista polja niti
da je svaki stvarni ključ jedinstven i spojiv. `P3-TEXT` mora to provjeriti nad
bajtovima; izostanak zemlje ili stabilnoga ključa u ispitnom skupu, orphan
zapis, višestruka veza ili curenje po dokumentu zaustavljaju paket i vraćaju
točan nalaz autoru.

## OA-G-A3-TEXT-SELECTION — preporučena odluka

### Točno omeđeni izvori i redci

1. Iz ParlaSenta ulaze samo dvije službene BCS datoteke navedene gore.
   Zadržavaju se **svi i samo** retci čije dokazano izvorno polje `country`
   označuje Hrvatsku. Ne uzorkuje se prema oznaci, govorniku, stranci, spolu
   ili rezultatu i ne uravnotežuju se klase. `P3-TEXT` mora zapisati doslovnu
   izvornu vrijednost hrvatske kategorije prije transformacije. Ako BCS
   ispitna datoteka ne nosi zemlju ili jednako pouzdanu službenu vezu na
   hrvatski izvor, implementacija se zaustavlja; zemlja se ne izvodi iz imena
   govornika, stranke ili teksta.
2. BCS ispitna datoteka ostaje netaknut `skup za ispitivanje`. Ako hrvatski
   ispitni redak nema jednu jedinstvenu vezu na ParlaMint-HR, paket pada
   zatvoreno; redak se ne izbacuje naknadno da bi se uljepšao rezultat.
3. Iz BCS datoteke za učenje prvo se uklanjaju samo retci čiji se
   `document_id` pojavljuje u ispitnoj datoteci, kako nijedan dokument ne bi
   prešao granicu ispitivanja. Preostali jedinstveni dokumenti razdvajaju se
   deterministički približno 80:20 na `skup za učenje` i `skup za provjeru`,
   uz što bližu raspodjelu trostupanjske oznake. Razdvajanje je po dokumentu ili
   govoru, nikad po retku, i mora biti ponovljivo iz javno zapisane SHA-256
   funkcije i konstante, bez naknadnoga ugađanja.
4. Iz `ParlaMint-HR.tgz` ne ulazi puni hrvatski korpus. Ulaze samo jedinstveni
   dokumenti i govori na koje upućuju zadržani hrvatski ParlaSent redci, točna
   označena rečenica, minimalni pripadni kontekst govora te nužni datum,
   govornik, stranka i uloga. Lingvistički označena arhiva `11356/2005`,
   strojni prijevodi `11356/2006`, ostale zemlje i nepovezani govori izričito
   su isključeni.

### Tri povezane razine

`P3-TEXT` treba proizvesti samo tri nastavne razine, sa stabilnim izvornim i
izvedenim ključevima:

| Izlaz | Jedinica | Najmanji potreban sadržaj |
|---|---|---|
| `parlament_govori.csv` | jedan zadržani ParlaMint-HR govor | izvorni dokument/govor, datum, govornik, stranka, uloga, tekst govora i oznaka granice korpusa |
| `parlament_mjere.csv` | jedan zadržani govor | broj rečenica, broj površinskih tokena i broj povezanih označenih rečenica, uz sirovi broj i isti broj na 1.000 površinskih tokena; nema lematizacije ni tvrdnje da je ta mjera valjan sentimentni konstrukt |
| `parlament_oznake.csv` | jedna zadržana ParlaSent rečenica | izvorni tekst, zemlja, dokument i rečenica, izvorna uloga datoteke, izvedeni skup, pojedinačne oznake i usklađenje samo gdje postoje, trostupanjska zabilježena oznaka, put proizvodnje oznake i veza na govor |

Sirovi šestostupanjski zapisi ostaju vidljivi gdje ih izvor daje; trostupanjski
`label` služi klasifikacijskoj tablici, ali se nikad ne zove istinom.
`put_oznake` mora razlikovati „dva kodera + usklađenje” od „jedan uvježbani
koder”. Nedostupne pojedinačne oznake u ispitnom skupu ostaju nedostupne, ne
pretvaraju se u praznu potvrdu slaganja.

### Jedinica, pitanje, potrošač i granica tvrdnje

- ParlaMintova jedinica jest **jedan zadržani govor**; označena rečenica služi
  kao poveznica i minimalni kontekst, a nije novi reprezentativni uzorak.
- ParlaSentova jedinica jest **jedna označena hrvatska rečenica** iz BCS
  datoteke, s vidljivim putem nastanka oznake i izvornom ulogom datoteke.
- Nastavno pitanje glasi: **kako odluka da se rečenica pošalje u ljudski
  pregled ovisi o granici korpusa, načinu nastanka zabilježene oznake,
  razdvajanju bez curenja, klasifikacijskom pragu i uvjetnim nazivnicima
  pogrešaka?**
- Jedini izravni analitički potrošač jest `WD-C17`, uključujući isti HTML,
  PDF, DOCX, no-code i tiskani put. `P3-TEXT` gradi paket, a `P3-VERIFY` ga
  provjerava; to nisu dodatni sadržajni potrošači. Nijedno drugo poglavlje ili
  dodatak ne dobiva podatke bez nove evidentirane odluke.

Nisu dopuštene tvrdnje o prevalenciji tona u Hrvatskome saboru, namjeri
govornika, uzročnosti ni generalizaciji izvan odabranoga korpusa. Datoteka za
učenje izvorno je obogaćena sentimentno izraženijim rečenicama, a ispitni je
dio proizveden drukčije; ta se razlika prikazuje, ne zaglađuje.

### Alternative

1. **Cijeli ParlaMint-HR korpus.** Odbija se kao 398 MB širok i nepotreban za
   jedno poglavlje.
2. **Sve BCS zemlje.** Odbija se jer povećava opseg i uvodi jezično i
   institucionalno uspoređivanje koje brif ne traži.
3. **Uravnoteženi uzorak oznaka ili slučajni retci.** Odbija se jer skriva
   selekciju i dopušta curenje istoga dokumenta među skupovima.
4. **ParlaMint-only rezerva.** Dopuštena je samo nakon novoga autorskog
   odgovora ako veza ili prava povezanoga paketa padnu; sama ne ispunjava
   prihvaćeni klasifikacijski brif.

## OA-G-A3-TEXT-RIGHTS — preporučena odluka

### Odvojeni licenčni režimi

1. `parlament_govori.csv` i `parlament_mjere.csv`, ako su izvedeni isključivo
   iz ParlaMint-HR, distribuiraju se pod **CC BY 4.0**. Obavijest navodi
   autore ParlaMinta prema službenom zapisu, naslov i inačicu 5.0, CLARIN ERIC,
   `http://hdl.handle.net/11356/2004`, poveznicu na CC BY 4.0 i točan opis
   izmjena: hrvatski rez, odabir povezanih govora, pretvorba u UTF-8 CSV i
   izračun unaprijed navedenih mjera.
2. `parlament_oznake.csv`, njegov kodni opis i svaki redistribuirani izvedeni
   rezultat koji prenosi ili prilagođava ParlaSentove rečenice ili oznake
   distribuiraju se pod **CC BY-SA 4.0**. Obavijest navodi Michala Mochtaka,
   Petera Rupnika, Katju Meden i Nikolu Ljubešića, puni naslov ParlaSent 1.0,
   Jožef Stefan Institute, `http://hdl.handle.net/11356/1868`, poveznicu na
   CC BY-SA 4.0 i točan opis izmjena: hrvatski rez, preimenovanje polja,
   evidentiranje puta oznake, dokumentno razdvajanje i povezivanje s
   ParlaMintom.
3. Ako jedan izlaz spaja ParlaSentov tekst ili oznaku s ParlaMintovim
   sadržajem u jednoj izvedenoj datoteci, cijeli taj **spojeni izvedeni izlaz**
   nosi CC BY-SA 4.0, uz atribuciju oba izvora. Ne pokušava se dio izveden iz
   ParlaSenta preimenovati u CC BY 4.0.
4. Izvorni graditelj, provjere i zasebna autorska dokumentacija mogu ostati pod
   MIT licencom repozitorija samo ako njihove obavijesti jasno kažu da MIT ne
   obuhvaća podatke trećih strana. Ne postavlja se dodatno ograničenje koje bi
   suzilo CC prava primatelja i ne implicira se podrška izvornoga izdavatelja.

### Kompatibilnost s ostalim podacima knjige

Ova je raspodjela kompatibilna s postojećim načinom distribucije jer
`README.md` i `data/README.md` već odvajaju MIT kod i tekst knjige od zasebno
označenih licenci svakoga podatkovnog paketa. CC BY-SA 4.0 nije licenca svih
podataka knjige niti cijele knjige: veže ParlaSentov licencirani materijal i
njegove prilagodbe. Generirani skupovi ostaju CC BY 4.0; ParlaMint-only izlazi
ostaju CC BY 4.0; zasebne datoteke nisu prelicencirane pukim zajedničkim
smještajem u repozitoriju. Konzervativno pravilo za stvarno spojenu izvedenu
datoteku jest CC BY-SA 4.0.

Gate ne tvrdi posebno dopuštenje nositelja prava. Pravna osnova preporuke jesu
objavljene CC licence na točnim službenim zapisima. `P3-TEXT` mora uz svaku
datoteku zapisati vlastitu licencu, URI, atribuciju, oznaku izmjena i kontrolni
zbroj te dokazati da nijedna obavijest ne flattena dvije licence u jednu.

### Alternative

1. **Sve datoteke pod CC BY 4.0.** Odbija se jer bi uklonilo ParlaSentov
   ShareAlike uvjet.
2. **Cijeli paket pod CC BY-SA 4.0.** Zakonito je konzervativno za spojeni
   izlaz, ali nepotrebno skriva da ParlaMint-only datoteke imaju blaži CC BY
   režim; preporuka zato zadržava licencu po datoteci.
3. **Portalni ili ParlaMint-only put.** Ostaje zakonita rezerva ako autor ne
   prihvati ShareAlike režim, ali tada povezani empirijski brif nije ispunjen i
   traži novu dispoziciju prije P3-TEXT.

## Blokirane ovisnosti i ovlast

Dok obje odluke nisu primljene, `G-A3-TEXT` ostaje `in_progress`.
`P3-TEXT`, `P3-VERIFY`, `WD-C17` i `C17` ostaju blokirani. Svih 20 sadržajnih
stavki 17. poglavlja ostaje `ratified`; 17. poglavlje i njegov widget ostaju
nepromijenjeni. Poglavlje 6 ostaje namjerno `draft`.

Ovaj gate ne prihvaća podatkovne bajtove, brojnosti, uspjeh povezivanja,
kontrolni zbroj izvedene datoteke, empirijski rezultat, prozu ni sadržajnu
stavku. Ne tvrdi mjereno vrijeme čitanja, testiranje novim čitateljima,
neovisnu terminološku recenziju ili autorovo čitanje poglavlja. Push, merge,
tag, arhiviranje, deployment i objava nisu autorizirani.

## Potrebne odluke autora

Za prihvaćanje odabira potreban je točno ovaj odgovor:

```text
G-A3-TEXT-SELECTION accepted as recommended for 7298a62a1c030f80c3d65443e8d311c76e1b1205 on 2026-08-18.
```

Za prihvaćanje prava potreban je zaseban točan odgovor:

```text
G-A3-TEXT-RIGHTS accepted as recommended for 7298a62a1c030f80c3d65443e8d311c76e1b1205 on 2026-08-18.
```

Ako preporuka nije prihvatljiva, treba navesti jednu točnu promjenu u
odgovarajućoj odluci protiv istoga ulaznog stanja. Do dvaju odgovora gate se ne
zatvara, `H-P3-CATALOG-001` se ne troši i `P3-TEXT` se ne claima.
