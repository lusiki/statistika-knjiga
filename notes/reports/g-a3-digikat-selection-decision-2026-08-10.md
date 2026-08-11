# G-A3-DIGIKAT — odabir, prava i uloga DigiKatovih podataka

**Vrsta:** vrata odluke (`decision_gate`), redni broj 84, faza 3B.

**Datum:** 10. kolovoza 2026.

**Nositelj odluke:** Luka Šikić, autor i urednik, ujedno vlasnik podatkovne
politike knjige i voditelj projekta DigiKat.

**Izvorno stanje odluke:**
`conversation:G-A3-DIGIKAT-selection-approved-2026-08-10-Luka-Sikic`.

**Autorova dispozicija:** prihvaćeno kako je preporučeno, uz izričitu uputu da
snimka bude **najnovija moguća**.

---

## Što ovaj gate odlučuje

Šest stvari, i ništa izvan njih:

1. koji točno izvadak iz projekta DigiKat ulazi u knjigu i u kojem presjeku;
2. kako se čita autorova uputa „najnovija moguća” za korpus koji još raste;
3. koju ulogu izvadak nosi u poglavljima 4, 5 i 6 i gdje je granica tvrdnji;
4. kako se rješava traka i prava, i pod kojim uvjetima paket smije biti
   promoviran;
5. zatvara li se `digikat_akteri` kao napušten u korist `digikat_mediji` i
   postaje li izostavljanje tablica s imenovanim akterima trajno pravilo;
6. što `P3-DIGIKAT` mora popraviti prije nego što ijedno poglavlje smije iz
   ovoga paketa išta tvrditi.

Vrata ne dohvaćaju podatke, ne mijenjaju `data/katalog.yml`, ne promiču paket i
ne diraju prozu. To je namjerno i slijedi presedan `G-A3-DZS` i `G-A3-DIP`.

---

## Ulazi pročitani prije odluke

- Cjelovit ledger isporuka. Dvije isporuke ciljaju ova vrata i svaka je
  obrađena na svojim vratima: `H-P1B-DATA-LIC-003` (`before_start`) potrošena je
  **prije preuzimanja paketa**, a `H-P3-CATALOG-001` (`before_close`) potvrđena
  je prije prve sadržajne izmjene i potrošena na zatvaranju. Ništa što cilja
  drugi paket nije potrošeno; isporuke za `G-A3-EUROSTAT`, `G-A3-ESS` i
  `G-A3-TEXT` ostaju `pending`.
- `notes/reports/vanjski-izvori-croaicon-digikat-2026-08-05.md` — izvidnica koja
  je matricu prava i tri izvatka pripremila, ali ništa nije zatvorila.
- `notes/reports/g-a3-data-rights-determination-2026-08-05.md` — autorova
  odredba o pravima od 5. kolovoza 2026.
- `data/katalog.yml`, unosi `digikat_mediji`, `digikat_akteri` i `determ_korpus`.
- Ratificirane okosnice poglavlja 4, 5 i 6 (`G-A2b-II`).
- Sam izvadak: sve tri datoteke pročitane su i prebrojane, a ne preuzete na
  riječ. Nalazi su u odjeljku „Provjera izvatka”.

---

## Prihvaćeni odabir

**Paket `digikat_mediji`, tri agregatne datoteke, bez ijedne imenovane osobe.**

| Datoteka | Redaka | Ključ | MD5 |
|---|---|---|---|
| `data/digikat-platforme-godisnje.csv` | 49 | godina + platforma | `fa7ed7c65b0940df9f96a0b3e7fdcff4` |
| `data/digikat-platforme-mjesecno.csv` | 438 | mjesec + platforma | `3f36b9015a7c4634732998f5bf51ed3f` |
| `data/digikat-izvori.csv` | 3.604 | izvor | `fc90ae84bbb0b03d599a7b9cf3fcb08e` |

Izvedene su iz triju od četrnaest praćenih agregatnih tablica projekta
(`platform_summary`, `platform_monthly`, `source_summary`). Puni korpus od
710.307 objava **nije čitan** i ostaje zasebno kao `determ_korpus`, traka
`external-only`, nepromijenjeno.

To je točno preporučena zadana dispozicija iz registra: prijenosni agregat s
javnim oznakama i s upozorenjima na metodološki rez i obuhvat, uz puni Determov
korpus izvan repozitorija.

---

## „Najnovija moguća” — kako se čita i zašto je ovdje provjerljiva

Autorova uputa glasi da snimka bude najnovija moguća. Kod DZS-a je to pravilo
moralo ostati pravilo, jer ondje vrata ništa ne dohvaćaju pa ne mogu potvrditi
što je objavljeno. **Ovdje je drukčije i zato je ovdje činjenica, a ne
pretpostavka:** izvor je autorov lokalni checkout, koji vrata smiju pročitati
bez ijednoga mrežnog poziva.

Provjereno 10. kolovoza 2026.:

- posljednji commit projekta je `278a127f9170c1aca82035a4a8357b8a995f91d8`,
  22. srpnja 2026. u 06:44:43 +0200;
- sve datoteke u `data/processed/` nose datum izmjene 22. srpnja 2026. 06:17;
- `scripts/build-digikat-extracts.R` u načinu provjere danas vraća
  `DIGIKAT_EXTRACTS_OK extracts=3 mode=verify`, dakle sve tri datoteke i dalje
  se reproduciraju **bajt po bajt** iz izvora.

**Zaključak:** stanje od 22. srpnja 2026. jest najnovije koje uopće postoji.
Snimka nije zastarjela u odnosu na izvor; izvor se nije pomaknuo. Korpus seže do
lipnja 2026., pa je to ujedno i najsvježiji podatak koji je moguć bez novoga
prikupljanja, kojemu ova knjiga nije nalogodavac.

**Pravilo za `P3-DIGIKAT`:** ponovno pokreni provjeru na vlastiti datum. Ako se
checkout u međuvremenu pomaknuo, prikvači novo stanje i preračunaj sve kontrolne
zbrojeve; ako nije, zabilježi da nije i zadrži postojeće. Ni u kojem slučaju ne
prepisuj datum dohvata na datum paketa: datum izvora je 22. srpnja 2026. i
ostaje to.

---

## Provjera izvatka — tri stvarna nedostatka

Vrata su izvadak prebrojala, a ne preuzela na riječ. Jedan test prolazi, tri
nalaza ne prolaze. Sva tri su **stvarni nedostaci** i nijedan dosad nigdje nije
zabilježen — ni u katalogu, ni u izvidnici.

### Prolazi: identitet nazivnika

Za svih šest godina zbroj `objave` po platformama točno je jednak stupcu
`objave_godina_ukupno`. Šest od šest, bez tolerancije. Nazivnik je ispravan i
poglavlje 4 smije ga koristiti kao takav.

### D-1 · Oznaka `godina_potpuna` netočna je za 2024.

Katalog definira taj stupac kao „ima li godina svih dvanaest mjeseci”. Prema toj
definiciji 2024. nema dvanaest mjeseci, nego osam:

```text
2024-01   1.911
2024-02       0      ← nema nijednoga retka
2024-03       0      ← nema nijednoga retka
2024-04       0      ← nema nijednoga retka
2024-05       0      ← nema nijednoga retka
2024-06   8.477
```

Uz to je i siječanj 2024. krnj: 1.911 objava naspram prosjeka od približno 6.960
mjesečno u razdoblju 2021.–2023. Stupac `godina_potpuna` ipak za 2024. stoji na
`da`.

To je **netočna oznaka kvalitete u knjizi koja uči čitati oznake kvalitete**, i
to je neprihvatljivo bez obzira na malen brojčani učinak. Popravlja se u
`P3-DIGIKAT`.

### D-2 · Godišnja i mjesečna datoteka ne slažu se međusobno

Od 49 usporedbi platforma × godina, **17 se razilazi**. Najveće razlike:

| Godina | Platforma | Godišnje | Zbroj mjesečnih | Razlika |
|---|---|---|---|---|
| 2022. | web | 68.626 | 69.072 | +446 (+0,65 %) |
| 2024. | web | 82.266 | 81.877 | −389 (−0,47 %) |
| 2023. | web | 66.980 | 66.923 | −57 (−0,09 %) |

Ukupno kroz cijeli korpus razlika je **točno nula**: 710.307 objava u oba
smjera. Obrazac — mali pomaci u oba smjera, s nultim zbrojem — dosljedan je
učinku granice godine, gdje objave uz prijelaz godine u dvjema tablicama
pripadnu različitoj godini. To je vjerojatno objašnjenje, **nije potvrđeno**, i
ovaj ga gate ne proglašava utvrđenim.

Knjiga ne smije isporučiti dvije datoteke koje se međusobno ne slažu bez ijedne
riječi o tome. Ili se razilaženje objasni i zabilježi s točnim rasponom, ili se
jedna datoteka izostavi.

### D-3 · Nema oznake metodološkoga reza, a rez postoji i velik je

Odobrena dispozicija izrijekom traži označavanje mjesta na kojem se mjerenje
promijenilo. **Ta oznaka u podacima ne postoji.** A promjena je vidljiva golim
okom:

- **Opseg.** Razdoblje 2021.–2023. drži se oko 7.000 objava mjesečno. Od lipnja
  2024. nadalje raspon je 8.458 do 26.155, dakle otprilike trostruko.
- **Obuhvat platformi.** Sedam platformi 2021. i 2022.; TikTok ulazi 2023. (dvije
  objave); Instagram ulazi 2024.; od 2024. ih je devet.
- **Posljednji mjesec.** Lipanj 2026. ima 7.815 objava naspram 20.471 u svibnju,
  što odgovara krnjem završnom mjesecu.

Zbog toga **nijedna usporedba kroz 2024. nije valjana bez izričite ograde**, a
godišnji niz nije vremenski niz. Postojeće upozorenje u katalogu spominje samo
nepotpunu 2026. godinu i time pokriva manji dio problema.

### Uz to: obuhvat datoteke izvora

3.604 izvora nose 551.712 od 710.307 objava, dakle **77,67 % korpusa**. Ostatak
pripada izvorima koje je filtar imenovanja izostavio — stranicama, kanalima i
osobnim računima. Filtar je zabilježen, ali njegova veličina nije. Poglavlje 4
mora znati svoj nazivnik, pa se i taj postotak bilježi.

### Provjerene brojke za poglavlja

Sve su izračunate izravno iz datoteke i slažu se s izvidnicom:

| Mjera | Vrijednost |
|---|---|
| broj izvora | 3.604 |
| sredina objava | 153,08 |
| medijan objava | 4 |
| omjer sredine i medijana | 38,27 |
| najveći izvor | `hkm.hr`, 56.500 objava |
| udio izvora s točno jednom objavom | 30,22 % (1.089) |
| udio deset najvećih u objavama | 26,96 % |
| izvora s dosegom 0 | 515 |
| izvora s interakcijama 0 | 1.367 |
| medijan dosega | 1.080 |

---

## Uloga u poglavljima 4, 5 i 6 i granica tvrdnji

**Poglavlje 4 — sažimanje.** `digikat-izvori.csv` nosi središnji primjer:
3.604 jedinice, sredina 38 puta veća od medijana. Jedan skup na kojemu se vide
sredina, medijan, mod, kvantili i standardizirana vrijednost. Stupac
`metrika_dostupna` nosi okosničinu tezu da je nedostajuća vrijednost
svjedočanstvo o postupku, a ne tehnička smetnja, jer nula ondje nije izmjerena
nula. `objave_godina_ukupno` nosi nazivnik kao odluku. Skripta graditelj nosi
vidljiv trag transformacije.

**Poglavlje 5 — vizualizacija.** Ista datoteka traži logaritamsku os i pokazuje
zašto linearna ovdje ne radi. `digikat-platforme-mjesecno.csv` nosi sastav kroz
vrijeme i razliku udjela od broja — **i, nakon popravka D-1 i D-3, nosi rupu u
2024. kao vidljivu činjenicu na grafu.** To je jači nastavni materijal od
uglađenoga niza i izravno dohvaća poglavlje 3.

**Poglavlje 6 — povezanost.** Objave, interakcije i doseg tri su zakošene
varijable na istim jedinicama: Pearson naspram Spearmana, oblik odnosa,
utjecajna opažanja i ograničenje raspona, pri čemu platforme bez mjerenja daju
stvarno i objašnjivo ograničenje raspona.

**Potrošači paketa su točno `WB-C04`, `WB-C05` i `WB-C06`.**

**Izričito se ne dodjeljuje poglavljima 2 i 3.** Izvidnica ih je predložila, ali
ta su poglavlja već prihvaćena (`C02`, `C03`) i stoje na `coauthor_review`.
Dodjela unatrag otvorila bi prihvaćeno poglavlje kroz sporedna vrata, a za to
postoji vlastiti mehanizam poništenja. Poglavlja 8, 13, 15, 17 i 18 nisu ovdje
ni odobrena ni odbijena; predložiti ih smiju samo njihova vlastita vrata.

**Dopuštene tvrdnje** ostaju kakve katalog već bilježi: opis broja objava po
platformi i po izvoru unutar ovoga korpusa, opis oblika raspodjele, usporedba
platformi uz uvažavanje stupca `metrika_dostupna`.

**Nedostupne tvrdnje**, uz one koje katalog već nabraja: svaka tvrdnja o
hrvatskom medijskom prostoru u cjelini, o javnom mnijenju, o broju različitih
osoba, usporedba interakcija između platforme s mjerenjem i one bez njega, i
svaka tvrdnja o pojedinačnoj objavi ili imenovanom akteru. **Ovaj gate dodaje
dvije:** nijedna tvrdnja o rastu ili trendu kroz 2024., i nijedna usporedba
razdoblja prije i poslije lipnja 2024. bez izrečenoga metodološkog reza.

---

## Prava, traka i uvjeti promocije

**Matrica prava je riješena i povoljna je.** `DATA_AVAILABILITY.md` projekta
DigiKat objavljuje `data/processed/*.rds` pod **CC BY 4.0**, uz izričitu tvrdnju
da su agregati bez osobnih podataka i da se smiju redistribuirati. Autor knjige
i voditelj projekta ista su osoba, pa je riječ o **vlasničkoj dispoziciji**, ne o
zaključku izvedenom iz dostupnosti. Autor ju je potvrdio 5. kolovoza 2026. i
ovim je vratima potvrđuje izrijekom, kako izvidnica i traži: stav da su agregati
projektovi ne smije se prešutno naslijediti.

`OA-G-A3-DIGIKAT-RIGHTS` time je **materijalno i formalno odgovorena, bez
ijedne poslane vanjske poruke.** To je autorova vlastita odredba kao odgovorne
strane, jednako kao kod DZS-a i DIP-a.

**Što se time ne tvrdi.** Knjiga i dalje **ne tvrdi da je pribavila dopuštenje
nositelja prava** ni za jedan izvor, jer ono ni od koga nije traženo.
`rights_boundary` u katalogu ostaje na `rights_holder_permission_obtained:
false`. `H-P1B-DATA-LIC-003` nije nadomješten.

**Master korpus ostaje vani.** `determ_korpus` zadržava traku `external-only` i
zabranu redistribucije. Brojanje objava nije redistribucija Determova sadržaja,
ali sadržaj sam ostaje njihov.

### Usklađenje sa službenim izvorom — izričita izmjena ugovora o promociji

Ovo je jedina stavka na kojoj bi odobreni plan inače stao, pa se rješava ovdje i
naglas.

`H-P3-CATALOG-001` traži sedam uvjeta zajedno prije svake promocije, a među
njima i **zabilježeno usklađenje sa službenim izvorom**. `digikat_mediji` ga
nema i **ne može ga imati**: riječ je o vlasničkom korpusu, a ne o službenoj
statistici. Ne postoji nikakav službeni ukupan iznos s kojim bi se agregat
uskladio. Doslovno primijenjen, taj uvjet zauvijek blokira paket koji je autor
upravo odobrio.

**Odluka:** uvjet se **ne ukida i ne slabi**, nego dobiva imenovanu zamjenu za
izvore koji nisu službena statistika. Za takav izvor usklađenje se dokazuje
trima testovima zajedno:

1. **Reprodukcija iz izvora.** Graditelj u načinu provjere reproducira svaku
   datoteku bajt po bajt iz uzvodnoga agregata. Danas prolazi.
2. **Unutarnji identitet.** Zbroj `objave` po platformama jednak je stupcu
   `objave_godina_ukupno` za svaku godinu, bez tolerancije. Danas prolazi, 6/6.
3. **Zabilježeno razilaženje.** Razlika između godišnje i mjesečne datoteke
   mora biti zapisana s točnim najvećim odstupanjem po ćeliji i s dokazanim
   nultim zbrojem kroz korpus. Danas **ne postoji** i traži se u `P3-DIGIKAT`.

Treći test je bitan jer je stroži od onoga koji zamjenjuje: tjera paket da
imenuje vlastitu nesuglasicu umjesto da je prešuti. Ugovor je time **pooštren za
ovaj razred izvora, a ne potrošen**, jednako kao što je `P3-DZS` pooštrio
pravila promocije umjesto da ih iscrpi.

`P3-DIGIKAT` mora tu zamjenu upisati u `data/katalog.yml` i
`data/katalog.schema.json` kao imenovano polje, i priložiti negativni fixture
koji pada kad se zamjena proglasi zadovoljenom bez sva tri testa. Zamjena vrijedi
**samo** za izvore koji nisu službena statistika i ne dira nijedan drugi paket.

### Promocija ostaje uskraćena na ovim vratima

`digikat_mediji` ostaje `promoted: false`, `promoted_total` ostaje 3, a traka
ostaje `bundled` kakva jest. Vrata odluke ne promiču ništa — to je pravilo koje
je `P3-DZS` već učvrstio i koje ova vrata poštuju. Promociju izvodi
`P3-DIGIKAT`, i tek nakon što D-1, D-2 i D-3 budu popravljeni.

Do promocije **obvezni studentski put ostaje** `anketa_mreze` ili njegov
agregat, kako katalog već bilježi.

---

## `digikat_akteri` i pravilo o imenovanim osobama

**`digikat_akteri` se zatvara kao napušten**, u korist `digikat_mediji`.
Registrirana stavka opisuje presjek **imenovanih aktera** po platformama; ono
što je izvučeno aktera nema i namjerno ih izostavlja, pa ne smije naslijediti
njezino ime ni njezin opis. Njezin jedini potrošač bio je `WB-C04` i ta uloga
prelazi na `digikat_mediji`. `P3-DIGIKAT` mora stavku označiti napuštenom s
razlogom i s uputom na nasljednika, a ne je izbrisati: brisanje bi izgubilo trag
odluke.

**Izostavljanje jedanaest uzvodnih tablica s imenovanim akterima potvrđuje se
kao trajno pravilo prvoga izdanja, a ne kao jednokratni izbor.** Pravilo glasi:
knjiga ne objavljuje tablicu koja imenuje pojedinca, **i onda kada je licenca
čista**. Licenca CC BY 4.0 pokriva i te tablice; izostavljene su odlukom, ne
pravom, i tako se i bilježi. Razlog je da teret krive brojke pada na imenovanu
osobu, a knjiga taj teret ne prenosi na nikoga tko ga nije prihvatio.

### Ispravak jedne tvrdnje iz izvidnice

Izvidnica kaže da je „preostalih jedanaest” tablica s imenovanim akterima. To
nije točno i ispravlja se ovdje. Deset ih je takvih (`*_actors.rds` i
`top_*_sources.rds`, uključujući `top_sources_by_year.rds`). Jedanaesta je
`proportions_summary.rds`, koja **ne imenuje nikoga**: sadrži uzvodne udjele u
pomičnom zarezu (`post_share`, `interaction_share`, `reach_share`). Ona je
odbijena iz drugoga razloga, koji izvidnica također bilježi — udio se u ovom
katalogu ne prenosi, nego se prenosi nazivnik. Zaključak je isti, obrazloženje
nije, i evidencija mora razlikovati to dvoje.

---

## Razmotrene alternative

1. **Uzeti i tablice imenovanih aktera, jer je licenca čista.** Odbijeno:
   licenca dopušta, uređivačko pravilo ne dopušta.
2. **Zadržati ime `digikat_akteri` za novi izvadak.** Odbijeno: opis stavke
   govori o akterima kojih u izvatku nema.
3. **Izostaviti mjesečnu datoteku i time izbjeći D-2.** Odbijeno: mjesečni je
   sastav ratificirana potreba poglavlja 5, a razilaženje je manje štetno
   zabilježeno nego izbjegnuto. Ostaje otvorenom mogućnošću **samo** ako
   `P3-DIGIKAT` razilaženje ne uspije zabilježiti s točnim rasponom.
4. **Ukloniti ili skratiti korpus na 2021.–2023., prije metodološkoga reza.**
   Odbijeno i suprotno autorovoj uputi: time bi otpalo razdoblje s najviše
   podataka i najnovije stanje.
5. **Isključiti 2024. zbog rupe.** Odbijeno: rupa je nastavni sadržaj, a ne
   smetnja. Skriti je bilo bi upravo ono protiv čega knjiga uči.
6. **Popustiti uvjet usklađenja jer izvor nije službeni.** Odbijeno: uvjet
   dobiva stroži imenovani ekvivalent s tri testa i fixtureom.
7. **Promovirati paket na ovim vratima, jer su prava riješena.** Odbijeno:
   dostupnost i riješena prava nisu promocija, a tri nedostatka nisu popravljena.
8. **Dodijeliti izvadak i poglavljima 2 i 3, kako izvidnica predlaže.**
   Odbijeno: oba su prihvaćena i imaju vlastiti mehanizam ponovnog otvaranja.

---

## Granica autoriteta

Ova odluka ovlašćuje `P3-DIGIKAT` da popravi tri imenovana nedostatka, upiše
zamjensko usklađenje s njegovim fixtureom, zatvori `digikat_akteri` kao
napuštenoga, upiše potrošače `WB-C04`, `WB-C05` i `WB-C06`, prikvači stanje
izvora na vlastiti datum i tek tada promiče paket.

Ne ovlašćuje: nikakvu izmjenu proze ni jednoga poglavlja, nikakvu promociju na
ovim vratima, nikakvu izmjenu trake bilo kojega drugog paketa, nikakav dohvat s
mreže, nikakvo preuzimanje master korpusa, nikakvu tvrdnju o dopuštenju
nositelja prava, nikakav generirani artefakt knjige, te nikakav `push`, `merge`,
`tag`, arhiviranje, objavu ni postavljanje.

Sva 19 jedinica ostaju `draft`. Nijedna datoteka podataka, nijedan unos u
katalogu i nijedan redak proze nisu ovim vratima promijenjeni.

---

## Blokirane ovisnosti koje se ovime otključavaju

| Što | Stanje |
|---|---|
| `P3-DIGIKAT` | sljedeći dopušteni paket |
| `R03-DIGIKAT-rights` | odblokiran; zatvara ga `P3-DIGIKAT` |
| `R08-DIGIKAT-package` | odblokiran; zatvara ga `P3-DIGIKAT` |
| `OA-G-A3-DIGIKAT-SELECTION` | `done`, bez poslane poruke |
| `OA-G-A3-DIGIKAT-RIGHTS` | `done`, bez poslane poruke |

Kasnija vrata ostaju obvezna: `P3-VERIFY-B`, pa `WB-C04`, `WB-C05` i `WB-C06`.

---

## Zabilježeno, a ne potrošeno: Eurostat

Autor je istoga dana odobrio i Eurostatov odabir. Ta odluka **pripada
`G-A3-EUROSTAT`** i ovdje se ne troši, jednako kao što je autorov odgovor o DIP-u
5. kolovoza bio zabilježen kao prethodna dispozicija umjesto da ga potroši
`G-A3-DZS`. Zapis je
`notes/reports/author-pre-dispositions-2026-08-10.md`.

Uz odobrenje ide i pitanje Eurostatovih uvjeta pripisivanja
(`OA-G-A3-EUROSTAT-RIGHTS`). Ono se ovdje **ne rješava i ne proglašava
riješenim**: katalog već bilježi objavljene uvjete, ali njihovu mjerodavnu
provjeru uz točan upit i datum snimke duguje `G-A3-EUROSTAT`. Ovaj gate to
izrijekom ostavlja otvorenim kako ne bi ispalo preskočeno.
