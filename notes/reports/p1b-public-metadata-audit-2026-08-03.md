# P1B-META — javni status, navigacija i razvojne naredbe

Provjera je provedena 3. kolovoza 2026. nad granom
`revision/comprehensive-review`, s polazišnog commita
`1a39d85af9ab86c3e0afb795addaa080d9086372`. Polazišni `README.md` imao je Git
blob `8295c15d103d50d64b8f924d9627327e208025a0`; prihvaćeni sadržaj ima Git blob
`e3801fd5b05eafeedae1a82e7d802e5ce49dfd1b`. Jednoredni UTF-8 manifest
`README.md<TAB><Git blob><LF>` daje prihvaćeno implementacijsko stanje
`state:sha256-11be9838488aaa37c614ff0980b66883146a1caae57eaa6230e751420b1ef206`.
Paket mijenja samo javni opis trenutačnog stanja, razvojnih putova i
navigacije. Ne uspostavlja izdanje, verziju, citatni format, changelog,
arhivu, errata-kanal ni mehanizam objave.

U ledgeru nije bilo handoffa usmjerenog na P1B-META, pa prije prve sadržajne
izmjene nije bilo ulazne predaje koju bi trebalo priznati ili konzumirati.

## Usporedba izvornoga stanja {#source-state-comparison}

U cijelosti su pročitani `AGENTS.md`, ratificirani plan, registar, dashboard,
handoff-ledger, checkout-localne upute `book-conductor` i njihov predložak za
ograničen vanjski upit. Za dokumentacijski ugovor pročitani su potpuni zapisi
P1B-META i R06-META-readme. U cijelosti su pročitani i dokumenti na koje README
upućuje: `notes/struktura-knjige.md`, `STYLE.md`, `ENRICHMENT.md`, `DESIGN.md`,
`LICENSE`, `CLAUDE.md`, `widgets/README.md`, `predavanja/README.md` i
`bookwright_plugin/README.md`.

Tvrdnje su zatim uspoređene sa živim konfiguracijama i putovima:
`_quarto.yml`, `_quarto-kolegij.yml`, `_quarto-pdf.yml`, `_quarto-docx.yml`,
`scripts/init-renv.R`, oba PowerShell omotača, `.github/workflows/publish.yml`,
`R/fetch-podaci.R`, `data/README.md`, `data/widgets.json`, checkout-localni
`bookwright_plugin/bookwright/shared/chapter-ledger.json`, dodatak C te javne
izvorne stranice za interakcije, podatke, AI, resurse i nastavu.

| Javna tvrdnja prije izmjene | Živo stanje i mjerodavni ugovor | Dispozicija |
|---|---|---|
| Knjiga je „kostur” i nijedno poglavlje nema sadržaj. | Postoji 19 izvora, predgovor i poglavlja 1–18; svaki ima tekst i ugovorene strukturne sastavnice. Svih 19 zapisa u checkout-localnom ledgeru ostaje `draft`. | Zamijenjeno izrazom „sadržajni nacrt u sveobuhvatnoj reviziji”; nijedan status nije podignut. |
| Povezana mrežna knjiga i PDF opisani su kao knjiga „uživo”. | Konfiguracija, workflow i razvojni artefakti postoje, ali završne provjere i release-governance još nisu provedeni. PDF korak u CI-ju je neblokirajući i može ostaviti prethodni artefakt. | Poveznice su zadržane kao razvojne, bez tvrdnje da predstavljaju objavljeno izdanje. |
| `scripts/init-renv.R` sadržava „sve što knjiga koristi”. | `renv.lock` i `renv/activate.R` ne postoje; skript je pripremni popis instalacija, a čista ponovljiva obnova pripada P1C-LOCK. | Uklonjena je instalacijska garancija i jasno je zabilježena nezaključana ovisnost. |
| Profil `kolegij` otvara kod i prikazuje rješenja. | `_quarto-kolegij.yml` otvara kod, ali u izvorima nema nijednih vrata `when-profile="kolegij"` koja bi ostvarila obećani put rješenja. | Zadržano je samo dokazano otvaranje koda; obećanje rješenja uklonjeno je. |
| Oba omotača privremeno prepisuju `_quarto.yml`. | PDF omotač samo provjerava kanonsku strukturu, renderira profil i kopira rezultat. DOCX omotač privremeno uklanja pre-render hook i mijenja vrata statičkih blizanaca, zatim u `finally` bloku vraća konfiguraciju i izvore. | Opis je usklađen s izvršnim skriptima; goli profil i dalje nije podržan put. |
| Poglavlja su kosturi; podatke i redoslijed treba izravno „dodati” ili „promijeniti”. | Poglavlja su nacrti; podatkovni ulaz je fail-closed i još nema kanonski `data/katalog.yml`; redoslijed je fiksni kanonski ugovor. | Navigacijske oznake sada vode na uređivanje nacrta, provjeru pravila za podatke i provjeru kanonskoga redoslijeda. |
| `STYLE.md` ima tvrda pravila H1–H9. | Živi dokument sadržava H1–H10 i S1–S9. | Broj je ispravljen bez promjene pravila. |
| Izgled nije prenesen. | `DESIGN.md` dokumentira zasebno preslikan prozračni uredništveni identitet, a `knjiga-stil/` je samo referentni paket. | Završna rečenica više ne proturječi živom dizajnerskom ugovoru. |

Neizmijenjene javne tvrdnje također su provjerene. Svih deset relativnih
Markdown poveznica u README-u razrješava se u postojećoj putanji. U
`data/widgets.json` registrirano je 17 widgeta, a `scripts/check-widgets.py`
potvrđuje HTML graf, statički blizanac i potpun zapis za svih 17. Adresa
repozitorija i stranice podudara se između `_quarto.yml`,
`design-tokens.yml` i `R/build-ai-exports.R`. Licenčni odjeljak ostao je
nepromijenjen jer se podudara s `LICENSE`, podatkovnom licenčnom obavijesti i
zatvorenim P1B-DATA-LIC zapisom.

Vanjska dostupnost poveznice nije korištena kao dokaz izdanja. Dokaz ovoga
paketa jest stanje repozitorija i njegovih ugovora, ne postojanje udaljenoga
artefakta u određenom trenutku.

## Razlika javnih metapodataka {#public-metadata-diff}

| Odjeljak `README.md` | Prihvaćena promjena |
|---|---|
| Zaglavlje i stanje | „Knjiga uživo” postala je „Radna mrežna inačica”; prazan kostur zamijenjen je sadržajnim nacrtom; svih 19 jedinica izričito ostaje `draft`; HTML, PDF i DOCX označeni su razvojnim artefaktima. |
| Lokalni pregled | Uklonjen je nedokazani potpuni instalacijski recept; navedeni su izostanak `renv.lock` i uvjet da su Quarto i R ovisnosti već dostupni. |
| Naredbe | HTML, profil kolegija, PDF i DOCX opisani su prema stvarnim izlazima; uklonjeno je nepostojeće prikazivanje rješenja. |
| Ispisni omotači | Razdvojeno je stvarno ponašanje PDF i DOCX skripta te je zadržana zabrana golog profila. |
| Navigacija | „Kostur”, izravno dodavanje podataka i slobodna promjena redoslijeda zamijenjeni su poveznicama na nacrte, podatkovna pravila i kanonski redoslijed. |
| Uređivački ugovor | H1–H9 usklađeno je na H1–H10. |
| Razvojna objava | Javna adresa više nije predstavljena kao dokaz izdanja; zabilježeno je stvarno neblokirajuće ponašanje PDF koraka. |
| Podrijetlo dizajna | Opis sada upućuje na dokumentirano zasebno preslikavanje identiteta. |

Nisu dodani bibliografski ključ, empirijska tvrdnja, mjereni rezultat, broj
inačice ni obećanje dostupnosti. Brojevi 18, 19 i 17 opisuju neposredno
strojno provjerljiv inventar repozitorija, a ne društveno-znanstveni nalaz.

## Usklađenje pogođenih datoteka {#affected-file-reconciliation}

| Datoteka | Usklađenje |
|---|---|
| `README.md` | Jedina javna datoteka promijenjena u paketu; status, razvojne naredbe i navigacija usklađeni su sa živim stanjem. |
| `notes/reports/p1b-public-metadata-audit-2026-08-03.md` | Ovaj trajni zapis nosi usporedbu izvornoga stanja, javni diff, granice paketa, provjere i buduće učinke. |
| `notes/reports/comprehensive-review-implementation-register.yml` | P1B-META i R06-META-readme primaju strukturirane dokaze i prihvaćeni status; pokazivač prelazi samo na G-A1d. |
| `notes/reports/comprehensive-review-forward-handoffs.yml` | Četiri stvarno buduća učinka prenose se točno vlasničkim paketima; packet review deklarira potpunost. |
| `notes/reports/comprehensive-review-dashboard.md` | Brojevi, stanje, closeout i sljedeći prompt usklađuju se s registrom i ledgerom. |

Poglavlja, dodaci, javne Quarto stranice, konfiguracije, skripte, podaci,
bibliografija, `docs/` i `_freeze/` nisu mijenjani. P1B-META nije pokrenuo
G-A1d, P1B-GOV ni bilo koji kasniji paket.

## Budući učinci {#buduci-ucinci}

- `H-P1B-META-001` predaje P1C-LOCK obvezu da nakon stvarno zaključane i
  provjerene čiste obnove zamijeni sadašnje upozorenje točnim javnim receptom.
- `H-P1B-META-002` predaje P1C-PDF obvezu da nakon blocking, wrapper-only i
  stale-safe CI puta uskladi README s novim, dokazanim ponašanjem.
- `H-P1B-META-003` predaje P5-ROUTES obvezu da ponovno provjeri svako javno
  obećanje o putovima, osobito rješenja i put bez koda, prije objave.
- `H-P1B-META-004` predaje P2-DOCS zatečene zastarjele unutarnje komentare:
  `_quarto-kolegij.yml` još najavljuje nepostojeća profilna rješenja,
  `_quarto.yml` još kaže da vizualni identitet nije odabran, a
  `bookwright_plugin/README.md` neke već ratificirane konvencije naziva
  privremenima. P1B-META ih nije mijenjao jer nisu javni README i pripadaju
  međudokumentnom usklađenju.

## Provjere

Closeout je potvrdio:

- inventar 19 ledger-jedinica, sve `draft`, svi izvori prisutni;
- 17 registriranih widgeta i prolaz `scripts/check-widgets.py`;
- razrješavanje svih relativnih README poveznica;
- izostanak `renv.lock` i profilnih vrata za rješenja;
- stvarno ponašanje PDF/DOCX omotača i neblokirajući PDF korak u CI-ju;
- `git diff --check` i ograničenje diffa na vlasničke putanje;
- prolaz workflow validatora;
- očekivani pad fixturea `generic_packet_evidence` i
  `invalid_outside_ask_link`.
