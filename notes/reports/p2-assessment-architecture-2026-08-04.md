# P2-ASSESS — kanonska arhitektura provjere znanja i AI kompetencija

**Paket:** `P2-ASSESS`

**Datum:** 4. kolovoza 2026.

**Ishod:** zapisani su kanonska shema rješenja, ugovor vidljivosti odgovora,
ljestvica AI kompetencija i granica H10, točno unutar prihvaćenih odluka D05 i
D06 na gateu `G-A2d`.

## Autoritet, ulazi i granica

Jedini urednički autoritet jest prihvaćena odluka `G-A2d`, vezana uz
`conversation:G-A2d-policy-decisions-approved-2026-08-04-Luka-Sikic`, i njezin
trajni zapis `notes/reports/g-a2d-policy-decisions-2026-08-04.md`. U cijelosti
su pročitane odluke D05 i D06 te stavke `R15-SCHEMA-closure`,
`R24-BOOK-human-AI-competence` i `R24-BOOK-three-roles`.

Prije prve sadržajne izmjene obrađena su sva tri primjenjiva dolazna handoffa.
`H-G-A2D-001` potrošen je dispozicijom da jedna shema bude jedini izvor svih
projekcija odgovora. `H-G-A2D-004` potrošen je dispozicijom da se kompetencija
gradi na specifikaciji zadatka, provjeri, alternativama, podrijetlu i
odgovornosti, bez ocijenjene proizvodnje koda. `H-P1C-EXPORT-001` priznat je
prije sadržajne izmjene, a pri zatvaranju se potrošuje dokazom da je njegova
strukturna granica ugrađena u ugovor vidljivosti.

Paket nije napisao nijedno stvarno rješenje ni nastavničku rubriku, nije dodao
rutu rješenja i nije promijenio izvoznik. Nije mijenjao prozu poglavlja ili
dodataka, ratificirao kostur ili terminologiju, birao podatkovni paket niti
odobrio push, merge, tag, arhiviranje, deployment ili objavu.

## Jedan kanonski zapis rješenja

Shema `bookwright_plugin/bookwright/shared/schemas/solution-record.schema.json`
određuje jedan zapis po zadatku. Stabilni identitet zapisa veže se uz jedinicu,
putanju i sidro zadatka te SHA-256 otisak njegova teksta. Šest sastavnica uvijek
je strojno prepoznatljivo, a neprimjenjiva se sastavnica označuje razlogom
umjesto prešućivanja.

| Sastavnica | Uloga |
|---|---|
| `planted_error` | Jedna namjerno posađena pogreška i objašnjenje zašto je pogrešna. |
| `revealing_diagnostic` | Postupak i očekivani dokaz koji pogrešku razotkrivaju. |
| `plausible_non_answers` | Primjenjivi uvjerljivi odgovori koji ne izvršavaju traženi sud i razlozi njihove nedostatnosti. |
| `model_response_components` | Obvezne tvrdnje i dokazi modelnoga odgovora za konceptualni ili kritički zadatak. |
| `numerical_check` | Očekivani rezultat, tolerancija ili pravilo prihvaćanja, neovisna metoda i dokaz. |
| `severity_ranked_rubric` | Kriteriji poredani po težini od fatalne pogreške do korisnoga poboljšanja. |

Puna rubrika razlikuje četiri razine. `fatal` ruši središnju tvrdnju ili
upravljačku granicu dokaza, estimanda, dizajna ili odgovornosti. `major`
označuje materijalno pogrešan ili izostavljen središnji korak. `minor` je
lokalni nedostatak preciznosti, terminologije, izvještavanja ili dokumentacije
koji ne ruši središnji sud. `useful_improvement` poboljšava jasnoću ili dubinu,
ali njegov izostanak nije pogreška.

Shema ne stvara paralelni izvor. Polja `alternatives` i `instructor_notes` dio
su istoga zapisa, a svaka pojavnost odgovora navodi ugovor
`D06-two-layer-v1`.

## Ugovor vidljivosti

Pet projekcija nastaje iz jednoga zapisa.

| Projekcija | Ruta i vidljivost | Sadržaj |
|---|---|---|
| Glavni studentski tekst | poglavlje ili dodatak, javno | Zadatak bez sastavnica odgovora. |
| Provjera za samostalno učenje | namjerno odvojena ruta, javno i odvojeno | Sažeta provjera, pogreška, dijagnostika, neodgovori, sastavnice modela i brojčana provjera. |
| Rubrika `kolegij` | profil ili druga strukturno zaštićena nastavna ruta | Sve studentske sastavnice, puna rangirana rubrika, alternative i nastavničke bilješke. |
| Tiskana provjera | odvojena tiskana ruta | Iste sažete sastavnice kao put za samostalno učenje, bez ovisnosti o widgetu ili instalaciji. |
| Javni AI izvoz | deklarirani javni ulazi | Nijedno polje zapisa rješenja. |

Zaštita je strukturna. Buduća ruta rješenja mora ostati izvan deklariranih
ulaza javnog AI izvoza. Zaštićeni sadržaj koji ipak živi u zajedničkom `.qmd`
izvoru mora biti unutar `content-visible` bloka s atributom `when-profile`.
Naziv poput „rješenje” ili „nastavnik” nije kontrola pristupa. Postojeći
`R/build-ai-exports.R` već uklanja profilne regije, odbija neočekivane zastarjele
artefakte i završava pogreškom kad otkrije curenje. Konačna ruta i negativna
proba ponavljaju se u `P5-ROUTES`.

## Ljestvica AI kompetencija

AI zadržava tri uloge. Kao instrument izvršava omeđenu delegiranu operaciju.
Kao pogrešiv analitičar proizvodi uvjerljiv rezultat koji treba provjeriti. Kao
predmet istraživanja postaje sustav čije podatke, oznake, odluke, povratne
sprege i posljedice proučavamo. Svaka sadržajna pojava mora navesti ulogu i
zadržati ljudsku odgovornost.

Pet dimenzija ima izričite uloge sijanja, razvoja i žetve te izričita
isključenja.

| Dimenzija | Sijanje u Dijelu I | Razvoj | Žetva |
|---|---|---|---|
| Specifikacija zadatka | Pitanje, cilj, jedinica, granica podataka, isporuka i nedostupna tvrdnja. | Transformacije, estimandi, nulte tvrdnje, referentne skupine, trenutak predviđanja, oznake i pragovi. | Potpuna specifikacija završnoga paketa prije delegiranja. |
| Provjera | Podrijetlo, jedinice, nazivnici, citati i sumnjiva preciznost. | Reprodukcija sažetaka i grafova, transformacije, uzorkovanje, nulte tvrdnje, fleksibilnost i reproducibilnost. | Pretpostavke, curenje, oznake, izdvojena provjera, podskupne pogreške, pomak i završna tvrdnja. |
| Alternative | Drugi nazivnik, usporedba, izvor ili odluka koja može promijeniti sud. | Obranjive odluke pripreme, prikaza, uzorkovanja, procjene i testiranja. | Alternativni model, prag, podskup, kodiranje ili analiza osjetljivosti s usporedbom zaključka. |
| Podrijetlo | Provjerljiv izvor svakog broja, citata, skupa i generiranog objekta. | Transformacije, inačice, analitičke grane, izvori treninga, oznake i podaci za provjeru. | Izvor i inačica, dnevnik transformacija, račun provjere, zapis uporabe AI-ja i objava. |
| Odgovornost | Ljudska odgovornost za pitanje, dijeljenje podataka, provjeru, tvrdnju i posljedice. | Izostanci, nesigurnost, fleksibilnost, uzročni jezik, tereti pogreške, praćenje i žalba. | Dokumentirana delegacija, provjera, izazov, objava i ono što je ostalo neprovjereno. |

Nakon Dijela I svaki zadatak koji koristi asistenta nosi čitljiv račun provjere.
Prva četiri obvezna polja bilježe što je traženo, što je vraćeno, što je
provjereno i kako. Zapis dodatno navodi ulogu AI-ja, ono što je ostalo
neprovjereno i odgovornu osobu. Račun sastavljen samo od koda ili sintakse nije
dovoljan.

Sedam etapa razrađuje isti standard bez pretvaranja u tečaj programiranja.
Dio I provjerava podrijetlo, jedinice, nazivnike, citate i izmišljene brojke bez
vidljivoga koda. Dio II reproducira sažetke i grafove te čita račun. Dio III
razdvaja generiranu sigurnost od uzoračke nesigurnosti i granice
generalizacije. Dio IV provjerava nultu tvrdnju, višestrukost, fleksibilnost i
reproducibilnost. Poglavlja 13–16 provjeravaju referentne skupine, pretpostavke,
izostavljene varijable, uzročni jezik, dijagnostiku, osjetljivost i trenutak
predviđanja. Poglavlje 17 dodaje podjelu podataka, oznake, curenje, pragove,
podskupne pogreške, pomak, praćenje i žalbu. Završnica traži da čitatelj
specificira, delegira, reproducira, ospori, dokumentira, objavi uporabu i
preuzme odgovornost za cijeli dokazni paket.

## Granica H10

Predgovor i Dio I zadržavaju nula vidljivoga koda. Skrivena infrastruktura
ostaje dopuštena, a profil `kolegij` može je otkriti bez stvaranja studentske
obveze. Nakon Dijela I račun i osumnjičeni kod mogu biti predmet čitanja i
dijagnostike, ali ne proizvodnje.

Nijedan ocijenjeni zadatak ne smije tražiti pisanje, dovršavanje, prepisivanje,
popravljanje ili prijevod odgovora u kod. Dopušteno je tražiti objašnjenje
računa, vezu izlaza s pitanjem, dijagnozu statističke ili podatkovne pogreške,
dokaz koji je razotkriva, neovisnu provjeru rezultata i granicu tvrdnje.
Dobrovoljna reprodukcija u dodatku nije ocijenjeni zahtjev. Cjelokupni audit
ljestvice osumnjičenoga koda ostaje u `P6-CONTINUITY`.

## Kanonsko stanje i provjere

`conventions.json` sada ima strogo validiran objekt `assessment_architecture`.
Njegov deterministički digest jest
`assessment:sha256-c1206f08e75502c748c2517a5020b4cd84074f5c2e5a03c5292c67dce928937a`.

| Datoteka | SHA-256 |
|---|---|
| `STYLE.md` | `bfc63643ab6c9c1d7eddfedb14178ac035af916f005ac84a230cf73787d9fdb7` |
| `conventions.json` | `bcce923c8ecaaa691acdb463eaaa4690156b58ed1f6645c83f8a5fead7436c7f` |
| `conventions.schema.json` | `94a14fdd35c4e9743871b5240d7438d44fd77f23c363faa1c9993f4950ae62e0` |
| `solution-record.schema.json` | `ee008a141d83b7a52c0d597669487cb9f7eacd7ddbde382719cfaba410c65524` |
| `check-assessment-architecture.py` | `20f7b0e9a4f0b275e8441632a18bc0385f62374e73cdc7319f13181086f7055b` |

`python scripts/check-book-architecture.py` potvrđuje da je prijašnjih 22
stavki arhitekture tvrdnji nepromijenjeno i da je nula od 19 kostura
ratificirano. `python scripts/check-assessment-architecture.py` potvrđuje tri
upravljane stavke, šest kanonskih sastavnica, pet projekcija s nula polja
rješenja u javnom AI izvozu, četiri razine rubrike, tri AI uloge, pet dimenzija
kompetencije, sedam etapa i nula ocijenjene proizvodnje koda. Inventar i dalje
sadrži 37 stranica, 19 jedinica, šest dodataka i nula ruta rješenja.

Dvije dodatne negativne probe provjerivača vraćaju kod 1. Prva ubacuje punu
rubriku u javni AI izvoz, a druga dopušta proizvodnju koda u Dijelu I. Paket
nije pronašao novi budući učinak koji već nije pokriven postojećim handoffima i
ovisnostima za `P5-ROUTES` i `P6-CONTINUITY`, pa ne stvara novi izlazni handoff.

Na zatvaranju su zajedno ažurirani registar, ledger handoffova i nadzorna
ploča. Workflow validator prolazi s praznim write lockom i paketom
`P2-IDENTITY` kao sljedećim dopuštenim paketom. Obje obvezne negativne probe
vraćaju kod 1: `generic_packet_evidence` odbija nestrukturirani dokaz za
`G-A0`, a `invalid_outside_ask_link` odbija nepoznatu stavku
`R99-NOT-A-REGISTER-ITEM`. Time su potvrđeni pozitivan i fail-closed kontrolni
put prije lokalnog scoped commita. Paket `P2-IDENTITY` nije započet.
