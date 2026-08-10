# G-A3-EUROSTAT — odluka o odabiru, pravima i izvornoj ruti

**Datum provjere:** 10. kolovoza 2026.

**Vlasnik odluke:** Luka Sikic, autor i urednik

**Status:** prihvaćeno; autor je odobrio preporučeni ograničeni službeni dohvat

**Izvorno stanje repozitorija:**
`355aecfcb4a4d0dfda33e10438d92aba019f6081`

**Stanje pripremljeno za autorsku odluku:**
`fd626f78f2ffbc93e8f4aca6376a91843ebe2c5f`

**Autorska dispozicija:** razgovor od 10. kolovoza 2026., Luka Sikic:
„Odobravam jedan ograničeni dohvat točno definiranog Eurostatova presjeka za
2025. iz službenog izvora, izvan rendera, uz spremanje upita, izvornog odgovora,
datuma, checksuma i usklađenja.”

**Potrošač:** `WB-C06`

**Granica:** vrata ne dohvaćaju podatke, ne mijenjaju katalog, ne stvaraju
snimku i ne promiču paket

## Preuzeta autorska dispozicija

Ovaj zapis ne ponavlja pitanje na koje je autor već odgovorio u
`notes/reports/author-pre-dispositions-2026-08-10.md`. Prihvaćeni je princip:
najmanji skup od pet do sedam pokazatelja koji odgovara na stvarna pitanja
poglavlja, jedna zajednička godina, vidljive oznake kvalitete i nedostajućih
vrijednosti te najnovija moguća snimka. „Najnovija moguća” znači najnoviju
godinu za koju odabrana kombinacija pokazatelja i zemalja zadovoljava zajednički
rez; ne znači zasebno traženje najnovije godine za svaku ćeliju.

Gate taj princip operacionalizira na šest pokazatelja. Šest je najmanji broj
koji istodobno daje tri sadržajne osi — rad i materijalne uvjete, obrazovanje,
digitalno sudjelovanje — i jednu demografsku treću varijablu potrebnu za
poglavlje o povezanosti. Pet bi tražilo ispuštanje cijele osi ili demografskoga
kontrolnog pitanja, a sedmi ne bi imao zasebno pitanje.

## Odabrani presjek

**Zajednička godina:** 2025.

Službene Eurostatove stranice pregledane su bez preuzimanja podatkovne
datoteke. Svih šest obitelji tablica objavljuje 2025. kao referentnu godinu;
točna potpunost svih ćelija mora se dokazati tek iz ovlaštenoga izvora u
`P3-EUROSTAT`. Ako ijedna od 162 kombinacije zemlje i pokazatelja nije
objavljena niti nosi službenu oznaku nedostajanja, 2025. ne prolazi i paket se
vraća na vrata; ne smije sam prijeći na miješane godine.

| Pokazatelj i točan rez | Eurostatov kod | Pitanje poglavlja 6 |
|---|---|---|
| Stopa zaposlenosti stanovništva od 20 do 64 godine, oba spola, postotak | `lfsi_emp_a` | Kako su uključenost u rad i materijalni uvjeti povezani među zemljama? |
| Osobe u riziku od siromaštva ili socijalne isključenosti, ukupno stanovništvo, oba spola, postotak | `ilc_peps01n` | Ide li viša zaposlenost uz niži rizik i što ta veza ne dokazuje? |
| Osobe od 25 do 34 godine sa završenim tercijarnim obrazovanjem, oba spola, postotak | `sdg_04_20`, izveden iz `edat_lfse_03` | Kako dvije obrazovne mjere opisuju različite rubove sudjelovanja? |
| Osobe od 18 do 24 godine koje rano napuštaju obrazovanje i osposobljavanje, oba spola, postotak | `edat_lfse_14` | Mora li veća tercijarna obrazovanost značiti manje ranoga napuštanja? |
| Osobe od 16 do 74 godine koje su se internetom koristile u prethodna tri mjeseca, sve osobe, postotak | `isoc_ci_ifp_iu` | Kako digitalno sudjelovanje ide uz radne, obrazovne i materijalne pokazatelje? |
| Udio osoba od 65 i više godina u stanovništvu 1. siječnja, oba spola, postotak | `demo_pjanind` | Mijenja li dobna struktura čitanje veze, bez pretvaranja treće varijable u dokaz uzroka? |

**Zemlje:** svih 27 država članica Europske unije — Austrija (`AT`), Belgija
(`BE`), Bugarska (`BG`), Cipar (`CY`), Češka (`CZ`), Danska (`DK`), Estonija
(`EE`), Finska (`FI`), Francuska (`FR`), Grčka (`EL`), Hrvatska (`HR`), Irska
(`IE`), Italija (`IT`), Latvija (`LV`), Litva (`LT`), Luksemburg (`LU`),
Mađarska (`HU`), Malta (`MT`), Nizozemska (`NL`), Njemačka (`DE`), Poljska
(`PL`), Portugal (`PT`), Rumunjska (`RO`), Slovačka (`SK`), Slovenija (`SI`),
Španjolska (`ES`) i Švedska (`SE`). Agregat `EU27_2020` smije biti kontrolni
red, ali nije jedna od 27 jedinica analize i ne ulazi u korelaciju.

**Potrošač:** samo `WB-C06`. Nijedan drugi potrošač nije dodan prešutno.
Paket služi usporedivosti, vidljivim zastavicama, raspršenom dijagramu,
trećoj varijabli i granici ekološkoga zaključivanja. Ne podupire individualnu,
uzročnu ni izvan-EU tvrdnju.

## Oznake, ključevi i granica zajedničke godine

`P3-EUROSTAT` mora zadržati izvorne `OBS_STATUS` i `CONF_STATUS` oznake uz
vrijednost. Službena baza razlikuje stvarnu nulu od neobjavljene vrijednosti
`:` te, među ostalim, zastavice za prekid niza, različitu definiciju, procjenu,
imputaciju, nedostajanje, nisku pouzdanost, privremenost i povjerljivost.
Nijedna se od njih ne pretvara u nulu, a red se ne uklanja samo zato što je
vrijednost prazna ili označena.

Ključ buduće nastavne tablice jest `geo × pokazatelj × time`, gdje je `time`
svugdje 2025. Dopuštena su točno dva ishoda za svaku od 162 kombinacije:
brojčana vrijednost sa svim izvornim oznakama ili izričito zadržana službena
nedostajuća vrijednost sa svim oznakama. Druga godina nije dopuštena kao
popuna.

## Mjerodavni uvjeti ponovne uporabe

Dana 10. kolovoza 2026. pregledane su:

- službena Eurostatova [obavijest o autorskim pravima i slobodnoj ponovnoj
  uporabi](https://ec.europa.eu/eurostat/help/copyright-notice);
- [pravna obavijest Europske
  komisije](https://commission.europa.eu/legal-notice_en);
- službene stranice i objave uz šest imenovanih kodova, uključujući aktualne
  objave za 2025. godinu.

Objavljena obavijest dopušta komercijalnu i nekomercijalnu ponovnu uporabu
Eurostatovih statističkih podataka i metapodataka uz priznanje izvora. Za
prilagođeni skup propisuje ovaj točan obrazac:

> Source: [Eurostat dataset datacode link], [access date]

Promjene podataka ili teksta moraju biti jasno označene i mora se dodati
disclaimer o Eurostatovoj neodgovornosti. Obavijest ne daje jednu propisanu
rečenicu baš za prilagođeni podatkovni izvadak; zato je ne smijemo izmisliti i
predstaviti kao Eurostatov citat. Ovaj gate umjesto toga veže paket uz dvije
točne rečenice: prva opisuje naše promjene, a druga doslovno preuzima
standardni disclaimer koji Eurostat stavlja u aktualne publikacije:

> Modified teaching extract: selection of 2025 and EU-27, joining of six
> datasets, Croatian labels and column layout are changes made by the authors.

> The European Commission is not liable for any consequence stemming from the
> reuse of this publication.

`P3-EUROSTAT` mora uz svaku od šest komponenti popuniti službeni obrazac
njezinom datacode poveznicom i stvarnim datumom pristupa; današnji datum nije
unaprijed upisan kao budući datum snimke. U putovnici i obavijesti uz snimku
moraju stajati i obje gornje rečenice bez parafraze. To je zapisano kao točan
tekst koji knjiga rabi, ne kao tvrdnja da je prva rečenica službeni Eurostatov
citat.

## Provjera iznimke za sadržaj trećih strana

Odabrani presjek ne ulazi u objavljene iznimke:

1. Službene stranice odabranih tablica i njima vezane aktualne objave navode
   Eurostat kao izvor. Obavijest izričito dopušta da se podaci objavljeni na
   Eurostatovoj stranici smatraju Eurostatovima za svrhu ponovne uporabe, osim
   ako su označeni drukčije; na pregledanim odabranim proizvodima takva oznaka
   nije pronađena.
2. Presjek sadrži samo države članice EU-a. Ne uključuje Sjedinjene Države,
   Japan, Kinu ni drugu geografiju obuhvaćenu ograničenjem komercijalne ponovne
   uporabe podataka izvan EU-a, EFTA-e te pristupnih i kandidatnih država.
3. Nijedan od šest pokazatelja nije trgovinska tablica. Posebne iznimke za
   švicarske, lihtenštajnske i austrijske trgovinske podatke zato nisu
   primjenjive.
4. Paket ne prenosi publikaciju, fotografiju, ilustraciju, logotip, zaštitni
   znak ni drugo zasebno autorsko djelo. Činjenica da neke Eurostatove vijesti
   uz podatke nose fotografije trećih strana ne daje pravo na njih; one u paket
   ne ulaze.

Ovaj zaključak vrijedi samo za šest imenovanih tablica, rez 2025. i 27 država
članica. `P3-EUROSTAT` mora ponovno pasti zatvoreno ako službena stranica ili
metapodatak uz stvarni izvorni materijal pokaže zaseban copyright ili drugoga
izvora. To nije tvrdnja da je pribavljeno dopuštenje nositelja prava; nije
traženo i nije potrebno prema objavljenoj općoj dozvoli dok iznimka nije
aktivirana.

## Izvorna ruta: prihvaćeni ograničeni dohvat

Repozitorij nema lokalno Eurostatovo zrcalo. MySQL tablica
`stg_eurostat_observations` u CroAIconu izričito je odbačena: staging ponavlja
retke iz uzastopnih dohvata i nema valjan lanac provenijencije. Njezinih se
vrijednosti ova vrata nisu dotaknula. U repozitoriju nema datoteke iz koje bi
`P3-EUROSTAT` mogao izračunati checksum ili provesti službeno usklađenje.

Read-only pregled portala dovoljan je za imenovanje proizvoda, najnovije
zajedničke godine i objavljenih uvjeta. Nije izvor za gradnju lokalne snimke.
Autor je zato 10. kolovoza 2026. izričito odobrio prvu od tri ponuđene rute:

- **prihvaćeno:** jedan ograničen dohvat točno ovoga presjeka iz službenoga Eurostatova izvora,
  izvan rendera, s upitom, izvornim odgovorom, datumom, checksumom i
  usklađenjem;
- **odbijeno:** lokalno zrcalo koje autor dostavi i imenuje točnim putem, iz kojega se isti
  trag može reproducirati;
- **odbijeno:** zadržavanje paketa kao `portal-mediated`, `promoted: false`, s praznim
  `files`, uz autorsku izmjenu kojom se `P3-EUROSTAT` descopira ili mu se
  mijenja ugovor.

Ovlast je jednokratna i odnosi se samo na šest imenovanih Eurostatovih tablica,
2025. godinu, 27 država članica i metapodatke nužne za dokaz. Ne dopušta drugi
Eurostatov pokazatelj, drugu godinu, drugu zemlju, drugi izvor, CroAIconovo
nevaljano staging zrcalo, dohvat tijekom rendera ni opće ukidanje zabrane
mrežnoga dohvata. `P3-EUROSTAT` mora zadržati stvarni upit i neizmijenjeni
izvorni odgovor, zabilježiti datum, checksum i usklađenje, te pasti zatvoreno
ako 2025. nije zajednička godina, ako izvorne zastavice nestanu ili ako se
pojavi pojedinačna obavijest treće strane.

Ovim je izvorna ruta riješena i `P3-EUROSTAT` smije početi tek nakon što se ova
vrata zasebno zatvore i commitaju. `eurostat_drustvo` do tada ostaje
`portal-mediated`, `promoted: false`, s praznim `files`; odluka sama promovira
nula paketa.

## Što tada nosi poglavlje 6

Ako autor odabere trajno portalno posredovanu i nepromoviranu rutu, poglavlje 6
ne smije glumiti da ima Eurostatovu usporednu snimku. Njegov računski temelj
ostaje već promovirani generirani paket `anketa_mreze`, na kojemu se poučavaju
oblik veze, Pearsonov i Spearmanov koeficijent, ograničenje raspona i granica
tvrdnje. Empirijski prijenos nosi već promovirani `digikat_mediji`, s vidljivim
lomom metode, neujednačenim mjerenjem platformi i zabranom trenda kroz 2024.
Time se povezanost i mjerna granica mogu poučiti, ali nestaje planirani stvarni
presjek zemalja za usporedivost i ekološku pogrešku. To mora biti otvoreno
izostavljanje, ne zamjena neprovjerenim brojkama.

## Granica ovlasti

Ova odluka prihvaća `G-A3-EUROSTAT` i ovlašćuje samo `P3-EUROSTAT` da jednom
dohvati točno imenovani presjek iz službenoga Eurostatova izvora, izvan
rendera, te spremi upit, neizmijenjeni odgovor, datum, checksum i usklađenje.
Sama odluka ne dohvaća ni jednu vrijednost, ne stvara snimku, ne mijenja
`data/katalog.yml` i ne promiče paket. Ne uređuje poglavlje ni Bookwrightove
zajedničke registre. Push, merge, tag, arhiviranje, deployment i objava ostaju
neovlašteni.
