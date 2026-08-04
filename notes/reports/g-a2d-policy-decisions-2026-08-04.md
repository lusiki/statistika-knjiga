# G-A2d — politika rješenja, dodataka, AI ljestvice i privatnosti

**Gate:** `G-A2d`

**Datum:** 4. kolovoza 2026.

**Ishod:** pet neovisno zatvorivih dispozicija prihvaćeno je u jednom
datiranom zapisu. Četiri su prihvaćene kako su preporučene; peta, institucijska,
prihvaćena je kao izričita datirana politika kolegija.

## Autoritet, ulaz i granica

Nositelj odluke jest Luka Šikić, docent, Sveučilišni odjel za komunikologiju,
Hrvatsko katoličko sveučilište, u ulozi autora i urednika te nositelja
kolegija. Izvorno stanje odluke jest
`conversation:G-A2d-policy-decisions-approved-2026-08-04-Luka-Sikic`.

Prije zapisa pročitan je cijeli ledger prijenosa. Nijedan dolazni handoff ne
cilja `G-A2d`, pa nije bilo čega priznati na `before_start` ni potrošiti na
`before_close` gateu.

Gate ne mijenja ni jedan redak proze, ne prihvaća `P2-ASSESS` ni bilo koji
kasniji paket, ne ratificira kostur poglavlja, ne bira ni promiče podatkovni
paket i ne odobrava push, merge, tag, arhiviranje, deployment ni objavu.

## 1. D06 — politika rješenja zadataka

Prihvaćeno kako je preporučeno. Nositelj kolegija: Luka Šikić.

Jedan kanonski zapis rješenja po zadatku prikazuje se u dva sloja. Izdanje za
samostalno učenje dobiva sažete provjere, namjerno posijane pogreške i
sastavnice odgovora u namjerno odvojenoj ruti rješenja. Profil `kolegij` dobiva
pune rubrike, alternativna rješenja i nastavničke bilješke. Zaštićena rješenja
isključuju se iz javnih AI izvoza.

Nema drugog izvora odgovora: sve četiri pojavnosti — provjera za studenta,
rubrika za nastavnika, javni izvoz i tiskani put — izvode se iz istoga zapisa.

## 2. D09 — opseg Dodatka B (jamovi)

Prihvaćeno kako je preporučeno. Nositelj provjere na čistoj instalaciji:
Luka Šikić.

Dodatak B podupire samo temeljne analize knjige, i to na istim datotekama,
varijablama, pitanjima i očekivanim vrijednostima kao Dodatak A. Za svaku
podržanu analizu bilježi se inačica i modul proizvoda, tip uvoza, put kroz
izbornik, postavke, filtri i ponderi, očekivani izlaz, zlatne vrijednosti,
izvoz, provjera, tumačenje, granica tvrdnje i nadnevak testiranja.

Nijedno javno obećanje puta bez koda ne smije nadilaziti ono što je stvarno
provjereno na čistoj instalaciji.

## 3. D10 — opseg Dodatka G (numerički podsjetnik)

Prihvaćeno kako je preporučeno.

Dodatak G obuhvaća točno četiri teme: postotke i postotne bodove, udjele i
stope, nagib te logaritamsku skalu. Ništa se ne dodaje ni oduzima. Poveznice na
prvo pojavljivanje koriste sankcionirani `podsjetnik` mehanizam, bez
improviziranog inline stila. Prije dodavanja datoteke ažuriraju se svi
konfiguracijom vođeni inventari.

Dodatak G ne uvodi nijednu metodu izvan pretpostavljene srednjoškolske
numeričke pismenosti i ne postaje poglavlje o metodama.

## 4. D05 i H10 — AI ljestvica kompetencija i granica provjere znanja

Prihvaćeno kako je preporučeno. Nositelj kolegija: Luka Šikić.

Računanje ostaje delegabilno. Nakon Dijela I svaki zadatak koji koristi
asistenta traži čitljiv račun provjere — što je traženo, što je vraćeno, što je
provjereno i kako. Ocjenjuje se prosudba, a ne proizvodnja koda: nijedan
ocijenjeni zadatak ne traži od čitatelja da napiše kod.

Pravilo Dijela I o nevidljivom kodu ostaje na snazi; skrivena infrastruktura je
dopuštena, ocijenjena proizvodnja koda nije. Tri uloge umjetne inteligencije —
instrument, pogrešiv analitičar i predmet istraživanja — zadržavaju se i svaka
značajna pojava dobiva izričitu ulogu uz zadržanu ljudsku odgovornost.
Ljestvica sumnjivog koda raste kroz knjigu s odobrenim iznimkama primjerenima
etapi.

## 5. D15 — datirana politika privatnosti, objave i alata

Prihvaćeno kao izričita, konzervativna politika kolegija.

**Institucija:** Hrvatsko katoličko sveučilište — kao matična ustanova kolegija
i kontekst u kojem se politika primjenjuje.

**Izvor politike:** vlastita politika kolegija uz udžbenik *Osnove statistike za
društvene znanosti*, inačica 1.0. Politika je instrument knjige i kolegija.
**Nije** propis Sveučilišta i ne smije se tako citirati; nijedan vanjski pravni
ili institucijski dokument nije naveden i nijedan se ne smije naknadno izmisliti
kao izvor. Puni tekst objavljuje se u Dodatku F, a Poglavlje 18 na njega
upućuje.

**Nadnevak stanja:** 4. kolovoza 2026.

**Odobrene trake alata.**

1. **Javni alati.** Javno dostupne usluge bez ugovorne zaštite unosa. Dopušteni
   samo za javno objavljene podatke, podatke čija provjerena licencija takvu
   uporabu dopušta, simulirane i sintetičke podatke te agregate pripremljene za
   nastavu. Zabranjeni za osobne, identifikacijske i ograničene podatke, za
   posebne kategorije osobnih podataka i za sve ugovorom zaštićene podatke.
2. **Ugovorno zaštićeni alati.** Usluge pod pisanim ugovorom — institucijskom
   ili poslovnom pretplatom — koji izrijekom isključuje uporabu unosa za
   treniranje modela i utvrđuje rok čuvanja. Dopušteni za pseudonimizirane radne
   podatke kad je ta ugovorna odredba provjerena i datirana. Zabranjeni za
   posebne kategorije osobnih podataka i za podatke čiji vlastiti uvjeti
   pristupa to ne dopuštaju.
3. **Institucijski odobreni lokalni alati.** Modeli koji rade na uređaju
   čitatelja ili na poslužitelju pod institucijskom kontrolom, bez izlaza
   podataka izvan tog okruženja. Dopušteni za ograničene podatke samo unutar
   njihovih vlastitih uvjeta pristupa.

**Trajna zabrana.** Nijedan zadatak, vježba, ispit ni prijenosni zadatak u
knjizi ne smije zahtijevati slanje osobnih, identifikacijskih, ograničenih ili
neraspodjeljivih podataka ni u jednu traku. Svaki takav zadatak mora imati
priloženu sigurnu inačicu podataka.

**Pravilo objave uporabe.**

> Uz svaki predani rad nastao uz pomoć asistenta prilaže se kratka izjava o
> uporabi: koji je alat i koja inačica korištena, što je delegirano, kojoj
> traci pripadaju upotrijebljeni podaci, što je autor sam provjerio i kako te
> što je ostalo neprovjereno. Nenavedena uporaba tretira se kao povreda
> akademske čestitosti; navedena uporaba sama po sebi ne umanjuje ocjenu.

**Pravilo datiranja tvrdnji.** Svaka pravna, institucijska ili proizvodna
tvrdnja u knjizi nosi nadnevak stanja i izvor, i nijedna se ne iznosi kao
bezvremena univerzalna pravna ocjena. Ako izvor nije provjerljiv, tvrdnja se ne
piše. Protokol Dodatka F ostaje neovisan o pojedinom modelu.

**Odgovorna osoba:** Luka Šikić, docent, Sveučilišni odjel za komunikologiju,
Hrvatsko katoličko sveučilište, kao nositelj kolegija. Politika se obnavlja i
ponovno datira prije svakog izvođenja kolegija.

## Upravljane stavke i njihovi paketi

| Dispozicija | Stavke | Paket |
|---|---|---|
| D06 rješenja | `R15-SCHEMA-closure` | `P2-ASSESS` |
| D06 rješenja | `R15-POLICY-delivery`, `R15-BOOK-closure-audit` | `P5-ROUTES` |
| D09 Dodatak B | `R21-AB-versioned-core`, `R21-JAMOVI-product-dating`, `R21-TEXT-prepared-route` | `P5-B` |
| D09 Dodatak B | `R21-AB-public-promise` | `P5-ROUTES` |
| D10 Dodatak G | `R34-AG-numeracy-refresher`, `R34-AG-first-use-links` | `P5-G` |
| D05 AI/H10 | `R24-BOOK-human-AI-competence`, `R24-BOOK-three-roles` | `P2-ASSESS` |
| D05 AI/H10 | `R23-BOOK-suspect-code-ladder` | `P6-CONTINUITY` |
| D15 privatnost | `R24-AF-privacy-sources`, `R24-BOOK-no-sensitive-upload` | `P5-F` |
| D15 privatnost | `R24-C18-privacy-sources`, `R24-C18-dated-policy` | `WE-C18` |
| D15 privatnost | `R24-BOOK-dated-legal-claims` | `P6-EVIDENCE` |

## Odbijene alternative

- Objaviti puna rješenja s rubrikama u javnom izdanju ili ih izostaviti u
  cijelosti.
- Održavati zaseban izvor odgovora za studente i zaseban za nastavnike.
- Obećati Dodatkom B potpuni put bez koda kroz cijelu knjigu, uz snimku zaslona
  za svaki mogući izbornik.
- Ostaviti javno obećanje puta bez koda šire od provjerene pokrivenosti.
- Proširiti Dodatak G izvan četiriju tema ili ga izostaviti pa numeričke
  podsjetnike ponavljati unutar poglavlja.
- Ocjenjivati proizvodnju koda ili dopustiti vidljivi kod u Dijelu I.
- Iznijeti privatnost kao bezvremenu univerzalnu pravnu ocjenu.
- Navesti vanjski institucijski propis kao izvor politike bez provjerljivoga
  naslova, poveznice i inačice.
- Voditi jednu traku alata umjesto tri i time izgubiti razliku između javne,
  ugovorno zaštićene i lokalno odobrene uporabe.

## Granica ovlasti

Odluka odblokira `P2-ASSESS` kao sljedeći dopušteni paket i propisuje sadržaj
za `P5-B`, `P5-F`, `P5-G`, `P5-ROUTES`, `P6-CONTINUITY`, `P6-EVIDENCE` i
`WE-C18`. Ne prihvaća nijedan od tih paketa, ne mijenja prozu, ne ratificira
kostur poglavlja ni terminologiju, ne bira podatkovni paket i ne odobrava
push, merge, tag, arhiviranje, deployment ni objavu. Svaka od pet dispozicija
ostaje neovisno zatvoriva i neovisno izmjenjiva na zahtjev nositelja.
