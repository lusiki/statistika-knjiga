# P1B-DATA-LIC — inventar licenci i pristupnih traka

Datum provjere je 3. kolovoza 2026. Paket provodi D08, D12 i prihvaćenu
odluku G-A1c za trenutačne i predložene podatkovne pakete. Ne odabire nove
empirijske datoteke, ne preuzima podatke, ne stvara `data/katalog.yml` i ne
zamjenjuje kasnije paketne provjere izvora, inačice, integriteta i dopuštenja.

## Vlasničke odluke i obvezni handoffi

Autor i vlasnik prava Luka Sikic odobrio je CC BY 4.0 za svaki generirani
nastavni skup. Kao vlasnik podatkovne politike odobrio je tri trake bez
paketne iznimke. U repozitorij se uključuju samo licenčno provjerene datoteke,
portalno posredovani izvori ostaju kod službenoga pružatelja, ograničeni ili
nedovoljno dokazani izvori ostaju vanjski, a svaki obvezni studentski put ima
licenčno čistu lokalnu datoteku ili agregatnu zamjenu.

`H-G-A1C-002`, `H-G-A1C-003` i `H-P1B-NAVARRO-001` pročitani su, priznati i
konzumirani prije prve sadržajne izmjene. Posljednji handoff čuva utvrđenu
granicu. Izvorni autorski tekst, kod i pridružena dokumentacija ostaju pod MIT
licencom, generirani podaci nose zasebnu CC BY 4.0 licencu, a podaci trećih
strana zadržavaju vlastite provjerene uvjete. Tehnički pristup nikada se ne
tumači kao ovlast za redistribuciju.

## Ugovor traka

Svaki paket ima točno jednu trenutačnu traku.

| Traka | Dopuštena radnja | Zabranjena pretpostavka |
|---|---|---|
| `bundled` | Točna datoteka ili reproducibilni izlaz smije se spremiti i dijeliti uz zabilježenu inačicu, atribuciju, licencu, obradu i kontrolu integriteta. | Sama javna adresa ili mogućnost preuzimanja nije dovoljna. |
| `portal-mediated` | Knjiga daje službenu poveznicu, točnu uputu, inačicu i kontrolni trag, a čitatelj preuzima od pružatelja. | Portalni pristup ne prikazuje se kao lokalna datoteka niti kao paritet svih izdanja. |
| `external-only` | Izvor se može navesti kao vanjski slučaj ili neobvezna mogućnost ako su i takva uporaba i citiranje zakoniti. | Datoteka, redci ili izvedeni skup ne ulaze u repozitorij bez nove mjerodavne provjere. |

Traka je sadašnji pravni i urednički status, a ne obećanje buduće promocije.
Kasniji paket smije promijeniti traku samo na temelju svojega propisanog
izvora, vlasničke dispozicije i usklađenja svih pogođenih datoteka.

## Potpuni inventar izvora i prava

### Trenutačni paketi

| Paket | Izvor i inačica | Licenca | Atribucija | Pristup | Redistribucija |
|---|---|---|---|---|---|
| `anketa_mreze` | `R/podaci-nastavni.R`; zadano 300 opažanja, sjeme 4001; inačica je deklarirano stanje izvora P1B-DATA-LIC. | CC BY 4.0 za izlaz; kod generatora ostaje MIT. | Luka Sikic; *Osnove statistike za društvene znanosti*; ime skupa; generator; poveznica na licencu; oznaka izmjena. | Lokalno generiranje bez mreže. | Dopuštena je za izlaz generatora i buduće neizmijenjene snimke uz uvjete CC BY 4.0. |
| `populacija_medija` | `R/podaci-nastavni.R`; zadano 50 000 opažanja, sjeme 8001; inačica je deklarirano stanje izvora P1B-DATA-LIC. | CC BY 4.0 za izlaz; kod generatora ostaje MIT. | Luka Sikic; *Osnove statistike za društvene znanosti*; ime skupa; generator; poveznica na licencu; oznaka izmjena. | Lokalno generiranje bez mreže. | Dopuštena je za izlaz generatora i buduće neizmijenjene snimke uz uvjete CC BY 4.0. |
| `UCBAdmissions` | Paket `datasets` u R-u 4.6.0; dokumentirani izvor su podaci o prijavama na Berkeley uz `@bickel1975`. | Lokalni opis paketa kaže da je paket dio R-a 4.6.0; zasebna licenca ili obavijest o redistribuciji skupa nije pronađena. | Izvorna studija i službena R dokumentacija; točan dodatni licenčni navod ostaje neriješen. | Iz lokalne instalacije R-a. | Nije dokazana za kopiju u `data/`; dostupnost kroz R nije dopuštenje. |
| `anscombe` | Paket `datasets` u R-u 4.6.0; dokumentirani izvor je Anscombeov kvartet uz `@anscombe1973`. | Lokalni opis paketa kaže da je paket dio R-a 4.6.0; zasebna licenca ili obavijest o redistribuciji skupa nije pronađena. | F. J. Anscombe, izvorni članak i službena R dokumentacija; točan dodatni licenčni navod ostaje neriješen. | Iz lokalne instalacije R-a. | Nije dokazana za kopiju u `data/`; dostupnost kroz R nije dopuštenje. |

### Predloženi paketi

| Paket | Izvor i inačica | Licenca | Atribucija | Pristup | Redistribucija |
|---|---|---|---|---|---|
| DZS turizam | Državni zavod za statistiku; planirane tablice BS_TU11, BS_TU12 i T01–T03; točno izdanje, datum i kontrolni zbroj određuje P3-DZS. | Hrvatska otvorena dozvola. DZS izričito navodi da su svi njegovi mrežni skupovi dostupni bez ograničenja pod tom dozvolom. | DZS kao izvor, datum posljednje izmjene, URI izvora i jasna oznaka svake promjene. | Službene DZS tablice ili sučelje. | Dopuštena je uz uvjete Hrvatske otvorene dozvole; exactna snimka ipak mora proći P3-DZS. |
| Drugi DZS domen | Izvor je DZS, ali domena, tablice i inačica nisu odabrani; prijedlog je odgođen za drugo izdanje. | Opća DZS obavijest postoji, ali ne postoji određen paket nad kojim bi se provjerili sadržaj i atribucija. | Nije moguće dovršiti prije odabira tablica. | Službeni DZS izvor. | Ne odobrava se redistribucija neodređenoga budućeg paketa. |
| DIP 2024 | Državno izborno povjerenstvo; izbori za zastupnike u Hrvatski sabor 2024.; službena stranica nudi CSV/XLSX rezultate, a točna datoteka i kontrolni zbroj pripadaju P3-DIP. | Na pregledanoj službenoj stranici pristupa nije pronađena izričita licenca ili drugi temelj za redistribuciju. | DIP, točni izbori, datum, službeni URL i opis obrade; konačni oblik ovisi o G-A3-DIP. | Službena stranica otvorenih podataka. | Nije dokazana za lokalnu kopiju. |
| DigiKat agregat aktera | Predloženi lokalni agregat iz komponenti DigiKata; komponentne inačice i prava nisu još evidentirani. | Nema mjerodavne komponentne licenčne matrice. | Nije moguće dovršiti prije G-A3-DIGIKAT i P3-DIGIKAT. | Vanjsko projektno okruženje. | Nije dokazana. |
| Determ puni korpus | Puni korpus u vanjskom projektnom okruženju Determ; točna inačica nije kandidat za javni repozitorij knjige. | Ograničeni projektni materijal; nije dostavljena ovlast za javnu redistribuciju. | Vanjski projekt i vlasnici pojedinih komponenti prema budućoj provjeri. | Samo izvan repozitorija knjige. | Nije dopuštena ovim paketom. |
| Eurostat EU society | Eurostat; predloženi skup društvenih pokazatelja; točni kodovi, rezovi i datum još nisu odabrani. | Eurostat dopušta ponovnu uporabu svojih statističkih podataka uz priznanje izvora, oznaku izmjena i propisani disclaimer, ali navodi iznimke za sadržaj trećih strana i druge kategorije. | Eurostat kao izvor, naslov skupa, oznaka izmjena i propisani disclaimer. | Službena baza ili API. | Ne potvrđuje se za neodabrane pokazatelje dok P3-EUROSTAT ne isključi iznimke i zabilježi točan upit. |
| ESS R11 Hrvatska | European Social Survey, Round 11, edition 3.0, uključuje Hrvatsku; izdanje objavljeno 2. lipnja 2025. | Podaci CC BY-NC-SA 4.0, dokumentacija CC BY-SA 4.0; ESS preporučuje službeni portal umjesto vanjskog hostinga i traži oznaku inačice i izmjena. | Propisani ESS navod, runda, izdanje, datum, licenca i oznaka izmjena. | ESS Data Portal, uz pravila portala. | Vlasnička odluka D08 ne odobrava bundling bez posebne pisane potvrde. |
| V-Dem v16 | Službena stranica navodi V-Dem Dataset v16; točne varijable nisu odabrane. | Na pregledanoj stranici skupa nije utvrđena mjerodavna licenca za planiranu datoteku. | Budući točni navod skupa v16 i njegovih autora; nije dovršen. | Službeni V-Dem izvor. | Nije dokazana. |
| COVIDiSTRESS II | Podatkovni članak upućuje na zapis na OSF-u; točna datoteka i inačica nisu odabrane. | Otvoreni pristup članku i tehnička dostupnost OSF zapisa ne dokazuju licencu same podatkovne datoteke. | Autori podatkovnoga skupa, točna OSF inačica i njezina licenca; nije dovršeno. | Vanjski OSF zapis. | Nije dokazana. |
| World Development Indicators | Svjetska banka; pokazatelj, izdanje i datum nisu odabrani. | Svjetska banka navodi CC BY 4.0 kao zadani režim za podatke koje sama proizvodi, ali upozorava da pojedini skupovi imaju druge licence. | Svjetska banka, točan pokazatelj, izvorna agencija, inačica, licenca i oznaka izmjena. | DataBank ili službeni API. | Nije dokazana za neodabrani pokazatelj. |
| ParlaMint-HR | CLARIN.SI zapis 11356/2004, ParlaMint 5.0; hrvatska arhiva ima zasebno objavljeni MD5; izdanje 8. srpnja 2025. | CC BY 4.0. | Cjeloviti navod korpusa iz repozitorijskoga zapisa, inačica 5.0, CLARIN trajni zapis, licenca i oznaka izmjena. | Izravno iz službenoga CLARIN.SI repozitorija. | Dopuštena je uz CC BY 4.0; P3-TEXT mora prenijeti puni MD5, točan podskup i obavijest bez prepisivanja iz sjećanja. |
| ParlaSent | CLARIN.SI zapis 11356/1868, ParlaSent 1.0; 18 200 označenih rečenica prema službenom zapisu. | CC BY-SA 4.0. | Cjeloviti navod skupa iz repozitorijskoga zapisa, inačica 1.0, trajni zapis, licenca i oznaka izmjena. | Izravno iz službenoga CLARIN.SI repozitorija. | Dopuštena je uz CC BY-SA 4.0; izvedeni skup koji prilagođava oznake zadržava odgovarajući ShareAlike režim. |
| GFI/FINA | Predloženi vanjski komercijalni ili administrativni izvor; nije odabran točan skup ni inačica. | Nema dokaza o javnoj licenci ili ovlasti za redistribuciju. | Moguće je samo točno citiranje objavljenoga agregata nakon zasebne provjere. | Vanjski izvor prema njegovim uvjetima. | Nije dopuštena ovim paketom. |

## Traka i zakonita zamjena

| Paket | Trenutačna traka | Obvezni studentski put i zakonita zamjena |
|---|---|---|
| `anketa_mreze` | `bundled` | Generator sada pokriva R i renderirane zadatke; buduća CC BY 4.0 snimka pokriva jamovi i preuzimanje. |
| `populacija_medija` | `bundled` | Generator sada pokriva R i renderirane zadatke; buduća CC BY 4.0 snimka pokriva jamovi i preuzimanje. |
| `UCBAdmissions` | `external-only` | Lokalna instalacija R-a ostaje neobvezni put; obvezna kategorička vježba koristi `populacija_medija` ili njegov licenčno čist agregat. |
| `anscombe` | `external-only` | Lokalna instalacija R-a ostaje neobvezni put; obvezna vježba vizualizacije ili povezanosti koristi `anketa_mreze` ili njegov licenčno čist agregat. |
| DZS turizam | `bundled` | Nakon P3-DZS ista provjerena snimka i agregat moraju opslužiti R, jamovi, preglednik i tisak. |
| Drugi DZS domen | `external-only` | Nije potreban za prvo izdanje; DZS turizam, Eurostat nakon provjere ili generirani skup nose obvezni put. |
| DIP 2024 | `portal-mediated` | Portal je neobvezna replikacija; obvezni administrativni ili izborni zadatak koristi provjereni DZS agregat ili generirani kategorički skup. |
| DigiKat agregat aktera | `external-only` | Dok prava komponenti nisu riješena, obvezna vježba koristi `anketa_mreze`, DZS agregat ili dokumentirani izostanak toga slučaja. |
| Determ puni korpus | `external-only` | Nije temelj obveznoga puta; koristi se samo vanjski opis provenijencije bez podataka. |
| Eurostat EU society | `portal-mediated` | Dok P3-EUROSTAT ne promiče točan skup, obvezni put koristi DZS paket ili generirani skup. |
| ESS R11 Hrvatska | `portal-mediated` | Empirijska replikacija ostaje neobvezna; obvezni putevi u poglavljima 13–16 koriste `populacija_medija` ili drugi licenčno čist paket i njegov agregat. |
| V-Dem v16 | `external-only` | Nije temelj obveznoga puta; dopušten je samo kasnije provjeren slučaj ili izostavljanje. |
| COVIDiSTRESS II | `external-only` | Nije temelj obveznoga puta; dopušten je samo kasnije provjeren slučaj ili izostavljanje. |
| World Development Indicators | `external-only` | Nije temelj obveznoga puta; DZS ili provjereni Eurostat paket nose usporedni zadatak. |
| ParlaMint-HR | `bundled` | Nakon P3-TEXT točan CC BY 4.0 podskup i njegovi agregati pokrivaju analitički i tiskani put. |
| ParlaSent | `bundled` | Nakon P3-TEXT zasebno označeni CC BY-SA 4.0 podskup pokriva sentimentni put; ako kompozicija ne prođe provjeru, koristi se ParlaMint-only opisna vježba bez prenesenih oznaka sentimenta. |
| GFI/FINA | `external-only` | Nije temelj obveznoga puta; dopušten je samo provjeren citirani agregat ili izostavljanje. |

Time su sva četiri trenutačna i svih trinaest predloženih zapisa dobili jednu
traku. Nijedan nedovoljno dokazani paket nije proglašen redistributivnim.

## Mjerodavni izvori

Provjera se oslanja na sljedeće primarne ili službene zapise, pregledane 3.
kolovoza 2026.

- [Pravni tekst CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)
  dopušta dijeljenje i prilagodbu uz propisanu atribuciju, poveznicu na licencu
  i oznaku izmjena te obuhvaća prava na baze podataka koja davatelj licence
  stvarno ima.
- [DZS otvoreni podaci](https://dzs.gov.hr/o-zavodu/pravo-na-pristup-informacijama/otvoreni-podaci/1812)
  upućuju na Hrvatsku otvorenu dozvolu za sve mrežne skupove, a
  [službeni tekst dozvole](https://www.data.gov.hr/hr/open-license) propisuje
  navođenje izvora, datuma posljednje izmjene, URI-ja i oznake promjena.
- [DIP otvoreni podaci](https://www.izbori.hr/site/en/general-information/open-data-1840/open-data/1851)
  dokazuju pristup izbornim rezultatima u CSV/XLSX obliku, ali pregledana
  stranica ne daje izričitu dozvolu redistribucije.
- [Eurostatova obavijest o autorskim pravima](https://ec.europa.eu/eurostat/help/copyright-notice)
  dopušta ponovnu uporabu uz uvjete i upozorava na iznimke koje se moraju
  provjeriti nad točno odabranim pokazateljima.
- [ESS Data Portal](https://www.europeansocialsurvey.org/data-portal) određuje
  trenutačno izdanje R11, a [ESS disclaimer](https://www.europeansocialsurvey.org/contact/disclaimer)
  navodi licence i uvjete hostinga, inačice i izmjena.
- [ParlaMint 5.0](https://www.clarin.si/repository/xmlui/handle/11356/2004)
  i [ParlaSent 1.0](https://www.clarin.si/repository/xmlui/handle/11356/1868)
  daju trajne zapise, inačice, datoteke i zasebne CC BY 4.0 odnosno CC BY-SA
  4.0 uvjete.
- [World Bank Public Licenses](https://datacatalog.worldbank.org/public-licenses)
  potvrđuje zadani režim i potrebu da se provjeri licenca svakoga točnog skupa.
- [Službena stranica V-Dem skupa](https://v-dem.net/data/the-v-dem-dataset/)
  potvrđuje v16, ali nije bila dovoljna za odobrenje redistribucije odabranih
  podataka.
- [Podatkovni članak COVIDiSTRESS](https://pmc.ncbi.nlm.nih.gov/articles/PMC9213519/)
  potvrđuje vanjski zapis podataka, ali ne zamjenjuje licencu točne datoteke.
- Službene R stranice za
  [`UCBAdmissions`](https://search.r-project.org/R/refmans/datasets/html/UCBAdmissions.html)
  i [`anscombe`](https://search.r-project.org/R/refmans/datasets/html/anscombe.html)
  potvrđuju sadržaj i podrijetlo, dok je lokalni `datasets/DESCRIPTION` potvrdio
  inačicu 4.6.0 i samo oznaku „Part of R 4.6.0”. To nije pretvoreno u
  pretpostavljenu ovlast za repozitorijsku kopiju.

Za DigiKat, Determ i GFI/FINA nije pronađena ili dostavljena mjerodavna
paketna ovlast. Oprezna traka zato nije tvrdnja da je svaka uporaba zabranjena,
nego zabrana da ovaj projekt bez dokaza javno redistribuira materijal.

## Licenca generiranih skupova i granica MIT-a

`data/LICENCA-generirani-podaci.md` primjenjuje vlasničku odluku na
`anketa_mreze`, `populacija_medija` i svaku njihovu buduću datotečnu snimku.
Ista oznaka sada postoji u generatoru, podatkovnoj mapi, javnoj stranici i
Dodatku C. Budući download mora nositi tu datoteku ili izravnu poveznicu na
nju.

CC BY 4.0 odnosi se na generirane podatke, ne na kod generatora. MIT ostaje za
izvorni tekst, kod i pridruženu dokumentaciju knjige. Licenca MIT ne proteže
se na ESS, ParlaMint, ParlaSent, DZS, Eurostat ili bilo koji drugi materijal
treće strane. ParlaSentov ShareAlike režim također ostaje odvojen od MIT koda
i aktivira se na njegovim prilagodbama, ne na cijeloj knjizi pukim držanjem
zasebno označenoga podatkovnog paketa.

## Usklađenje pogođenih datoteka

| Datoteka | Usklađenje |
|---|---|
| `R/podaci-nastavni.R` | Dodana je CC BY 4.0 obavijest za oba izlazna skupa i izričita granica prema MIT kodu. |
| `data/LICENCA-generirani-podaci.md` | Stvorena je jedinstvena obavijest s opsegom, nositeljem prava, atribucijom, oznakom izmjena i pravilom za buduće snimke. |
| `data/README.md` | Razdvojeni su metapodatkovni artefakti od nastavnih podataka te su zapisani polja inventara i tri trake. |
| `R/fetch-podaci.R` | Kostur sada odbija svaki unos koji nije `bundled` s provjerenom redistribucijom; portalni i vanjski paketi ne mogu se tehnički preuzeti ovom skriptom. |
| `podaci.qmd` | Uklonjena je netočna tvrdnja da je svaki skup javno preuzimljiv; dodani su ugovor traka, zamjene i generirana licenca. |
| `dodaci/c-katalog-podataka.qmd` | „Nije primjenjiva” zamijenjeno je CC BY 4.0 za oba generirana skupa, a ugrađeni R skupovi dobili su opreznu traku i zamjene. |
| `README.md` | Očuvana je MIT granica i dodana zasebna poveznica na CC BY 4.0 generirane podatke. |
| `data/katalog.yml` | Datoteka ne postoji i nije prerano stvorena; njezin strojno čitljiv, validiran oblik pripada P3-CATALOG. |

## Deklarirano stanje izvora

Implementacijsko stanje sedam sadržajnih datoteka izvan kontrolne transakcije
jest
`state:sha256-2e0f065b18182f1ccce781a48458cebf49d0e3e9c59790e64fb97f776a110c32`.
Izračun je SHA-256 nad UTF-8 manifestom putanje i Git blob identifikatora,
poredanim istim redoslijedom kao u sljedećoj tablici i završeno jednim znakom
novoga retka.

| Putanja | Git blob |
|---|---|
| `data/LICENCA-generirani-podaci.md` | `5757fea6d6559a4b0a0f933999a298d0626a1f8f` |
| `data/README.md` | `747b28d2598f2d563c6f226045dabe67f13c8c29` |
| `dodaci/c-katalog-podataka.qmd` | `4b90efdfa976745485462bbeb96272c103b32fbe` |
| `podaci.qmd` | `e289d9dafc1bbd6bbfb63c1e18034a47a3e4598a` |
| `R/fetch-podaci.R` | `089939ad7dcb4f220042def0d966152eba3bd405` |
| `R/podaci-nastavni.R` | `abe4005a4629f61782dd202429b098f645472387` |
| `README.md` | `8295c15d103d50d64b8f924d9627327e208025a0` |

## Buduće obveze

P3-EXISTING ne smije stvoriti ili urezati kopiju `UCBAdmissions` ili
`anscombe` dok ne utvrdi točan paketni temelj redistribucije. Mora ujedno
osigurati da svaka materijalizirana snimka dvaju generiranih skupova zadrži CC
BY 4.0 obavijest.

P3-CATALOG mora ovaj inventar pretvoriti u jedini strojno čitljiv katalog s
obveznim poljima za izvor, inačicu, licencu, atribuciju, pristup,
redistribuciju, traku, zamjenu i integritet. Ne smije automatski promovirati
portalni ili vanjski paket.

P3-DZS, P3-DIP, P3-DIGIKAT, P3-EUROSTAT, G-A3-ESS i P3-TEXT moraju poštovati
ovdje zabilježene početne trake. DZS turizam, ParlaMint i ParlaSent već imaju
utvrđen opći pravni temelj za `bundled`, ali njihov točan sadržaj, inačica,
obavijest i kontrolni zbroj i dalje moraju proći vlastiti paket. DIP,
Eurostat i ESS ostaju `portal-mediated` dok točno propisani kasniji dokaz ne
opravda promjenu. DigiKat, Determ, V-Dem, COVIDiSTRESS, WDI i GFI/FINA ostaju
`external-only` dok mjerodavan dokaz nad točnim paketom ne utvrdi drukčije.
