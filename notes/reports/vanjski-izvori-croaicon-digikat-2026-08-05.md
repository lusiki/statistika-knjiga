# Izvidnica vanjskih izvora — CroAIcon i DigiKat

**Vrsta:** izvidnica i priprema građe. **Nije** paket iz sveobuhvatne revizije i
ne zatvara nijedna vrata.

**Datum:** 5. kolovoza 2026.

**Naručeno:** autorovom uputom da se pregledaju dva vanjska projektna
repozitorija, iz njih odaberu i agregiraju najkorisniji dijelovi, te da se ta
građa učini dostupnom knjizi, uz znanje potrebno za kasniju integraciju.

**Pregledani putovi:**

- `C:\Users\lsikic\projects\CroAIcon` — analitički blog AI.econ; uz repozitorij i
  udaljena MySQL baza `odvjet12_gfi`;
- `C:\Users\lsikic\projects\DigiKat` — projekt *Prikaz i analiza katoličke
  tematike u digitalnom medijskom prostoru*, HKS.

Ništa nije dohvaćeno s mreže osim izravnoga čitanja imenovane MySQL baze, na
koju je autor uputio. Nijedan zapis iz te baze nije prepisan u ovaj repozitorij.

---

## 1. Zašto je ova izvidnica bila potrebna

Katalog podataka knjige već je, u paketu `P3-CATALOG`, registrirao četiri stavke
koje pokrivaju upravo ove dvije baze — i sve četiri ostavio neprohodnima:

| Stavka u katalogu | Traka | Zašto je stala |
|---|---|---|
| `digikat_akteri` | `external-only` | „nema mjerodavne komponentne licencne matrice” |
| `determ_korpus` | `external-only` | ograničeni komercijalni materijal; redistribucija nije dopuštena |
| `gfi_fina` | `external-only` | nema dokaza o javnoj licenci ni ovlasti za redistribuciju |
| `eurostat_drustvo` | `portal-mediated` | točni kodovi, rezovi i datum nisu odabrani |

Prve tri čekaju gate `G-A3-DIGIKAT`, četvrta `G-A3-EUROSTAT`. Ni jedan ni drugi
nisu se mogli pripremiti jer nitko nije bio pročitao izvore. Ova izvidnica
donosi upravo tu činjeničnu podlogu, i **mijenja zaključak za dvije od četiri
stavke**.

---

## 2. Inventar — DigiKat

**Što projekt drži.** Korpus od približno 710.000 medijskih objava, 2021.–2026.,
hrvatski i bosanski, 47 varijabli, kroz web portale, YouTube, Facebook, Twitter,
Reddit, Instagram, TikTok, forume i komentare. Objava ulazi u korpus ako i samo
ako sadrži **najmanje dva različita katolička korijenska pojma**
(`R/religious_terms.R`).

**Kako je podijeljen.** `DATA_AVAILABILITY.md` u repozitoriju projekta izričito
razdvaja dvije razine:

| Sredstvo | U repozitoriju | Licenca | Redistribucija |
|---|---|---|---|
| `data/merged_comprehensive.rds` (master, ≈710k × 47) | ne, gitignoriran | — | **ne** |
| `data/processed/*.rds` (14 praćenih agregatnih tablica; `DATA_AVAILABILITY.md` još govori o deset) | **da, praćene Gitom** | **CC BY 4.0** | **da — agregat, bez osobnih podataka** |
| `data/raw/*.xlsx` | ne | ovisi o izvoru | ne |

**Provjereni raspon korpusa:** 2021-01 do 2026-06. Godina 2026. ima šest od
dvanaest mjeseci.

**Četrnaest agregata, pročitanih redom.** Tri su upotrebljiva za knjigu:

- `platform_summary` (49 × 5) — godina × platforma: objave, interakcije, doseg;
- `platform_monthly` (438 × 5) — mjesec × platforma, isto troje;
- `source_summary` (29.728 × 6) — godina × izvor: objave, interakcije,
  prosječna stopa angažmana, doseg.

Preostalih jedanaest (`*_actors.rds`, `top_*_sources.rds`,
`top_sources_by_year.rds`) tablice su **imenovanih aktera**. Uz medijske kuće
sadrže i imenovane pojedince — političare, svećenike, influencere i privatne
osobe. Nisu preuzete i ne bi ih trebalo preuzeti.

**Tri nalaza o samim brojkama, koji su ujedno razlog odabira:**

1. **Nula koja nije nula.** Na platformama `reddit`, `forum` i `comment`
   interakcije i doseg iznose točno 0 u svih šest godina. Servis za praćenje
   medija za te vrste izvora ne isporučuje mjere angažmana. Izvor ne razlikuje
   „nula” od „nije mjereno”.
2. **Prosjek omjera.** `avg_engagement_rate` u `source_summary` prosjek je stopa
   po objavi, a ne omjer zbrojeva. Za izvor s jednom objavom i tridesetak
   interakcija daje stopu od 9,77 — veću nego bilo koja velika kuća.
3. **Rep.** Raspodjela izvora po produktivnosti je izrazito zakošena; vidi
   mjere u odjeljku 5.

---

## 3. Inventar — CroAIcon

### 3.1 Udaljena baza `odvjet12_gfi`

75 tablica na `91.234.46.219:3306`. Najveće:

| Tablica | Redaka | Sadržaj |
|---|---|---|
| `gfi_all`, `db_afs` | po ≈2,29 mil. | FINA, godišnji financijski izvještaji |
| `financial_indicators`, `financial_risk_scores` | ≈2,0 / 2,1 mil. | izvedeni pokazatelji i bodovi rizika |
| `subjekti`, `subjekti_26012026` | 699k / 895k | registar poslovnih subjekata |
| `data_api_persons_current_data`, `data_api_person_roles_current_data` | 722k / 1,1 mil. | **osobe i njihove uloge u subjektima** |
| `stg_eurostat_observations` | 643k | zrcalo Eurostatovih serija |
| `leads`, `lead_enrichment_*` | 330k | komercijalna prodajna baza |

**Odluka: iz ove baze nije preuzet nijedan redak.** Tri razloga, svaki dovoljan
sam za sebe. Financijski dio je `gfi_fina` iz kataloga — komercijalni izvor bez
ovlasti za redistribuciju. Tablice `data_api_person*` i `leads` sadrže osobne
podatke i ne smiju ni prići ovom repozitoriju. Vjerodajnice za bazu stoje u
`.env` datoteci vanjskoga projekta i **ne smiju** se pojaviti ovdje ni u kakvu
obliku; render knjige ne dohvaća ovaj izvor.

**Nalaz o Eurostatovu zrcalu, za gate `G-A3-EUROSTAT`.** `stg_eurostat_observations`
drži osam skupova (`une_rt_a`, `lfsi_emp_a`, `nama_10_pc`, `prc_hicp_aind`,
`sdg_08_10`, `tec00114`, `nama_10r_2gdp`, `demo_r_pjangrp3`), za 27 zemalja,
2000.–2025. Sadržajno je to točno ono što bi `eurostat_drustvo` trebao biti.
**Ali to je staging tablica i ponavlja retke** — ista opažena vrijednost pojavljuje
se više puta iz uzastopnih dohvata, bez sloja za uklanjanje duplikata. Zrcalo
zato **nije valjan lanac provenijencije**. Ostaje zaključak iz kataloga:
`eurostat_drustvo` uzima se s Eurostatova sučelja ili API-ja, u traci
`portal-mediated`, s vlastitim datumom preuzimanja.

### 3.2 Repozitorij i njegovi izlazi

`outputs/tables/` drži 43 provjerene agregatne tablice iz deset objavljenih
analiza. **Sve su gitignorirane** — javno je samo renderirani HTML na
`MislavSag.github.io/CroAIcon`. Autorov lokalni checkout zato je izvor zapisa,
jednako kao što je DZS-ovo zrcalo izvor za `P3-DZS`.

Pregledane su sve tablice. Po podrijetlu se dijele u tri skupine:

| Skupina | Tablice | Uzvodni izvor | Upotrebljivo? |
|---|---|---|---|
| Državne potpore | 10 | **javni registar** `rdp.gov.hr/javno` + izvješća MFin-a | **da** |
| Dugi niz BDP-a | 5 | Eurostat, Maddison, PWT, Svjetska banka, Tica (2004.) | **da, uz uvjete** |
| Firme, sektori, turizam, zombi-firme, Zagreb | 28 | **FINA GFI** (`db_afs`) | **ne** — to je `gfi_fina` |

Treća je skupina analitički najbogatija i pravno neprohodna. Sektorski panel
2002.–2024. (21 djelatnost × 23 godine), zaduženost, marže, zombi-firme i
turistički prihod po noćenju — sve to počiva na komercijalnoj bazi. Uzeta nije
nijedna, uključujući i one koje na prvi pogled izgledaju bezazleno.

Turistički dio dodatno se preklapa s paketom `dzs_turizam`, koji je već u
izradi i ima čistu Hrvatsku otvorenu dozvolu.

---

## 4. Matrica prava — glavni nalaz

Ovo je dio zbog kojega je izvidnica napravljena.

| Izvor | Nositelj / uvjeti | Zaključak kataloga prije | Nakon izvidnice |
|---|---|---|---|
| DigiKat, `data/processed/*.rds` | Luka Šikić, HKS; **CC BY 4.0**, izričito objavljeno u `DATA_AVAILABILITY.md`; agregat bez osobnih podataka | „nema licencne matrice” | **matrica postoji i povoljna je** |
| DigiKat, master korpus | Determ, komercijalni servis | redistribucija nije dopuštena | **nepromijenjeno** |
| DigiKat, tablice aktera | isto CC BY 4.0, ali **imenovani pojedinci** | nije razmatrano zasebno | **izostavljeno odlukom, ne pravom** |
| FINA GFI (`db_afs`) | komercijalna baza | redistribucija nije dopuštena | **nepromijenjeno, potvrđeno** |
| Registar državnih potpora | javno tijelo; registar javan | nije bio u katalogu | **nov kandidat; uvjeti ponovne uporabe nisu objavljeni** |
| BDP, pet procjena | četiri CC BY 4.0 / otvoreni pristup, jedna Eurostat | nije bio u katalogu | **nov kandidat; Eurostatov stupac ostaje portalni** |
| Eurostatovo zrcalo u MySQL-u | staging s duplikatima | portal-mediated | **nepromijenjeno; zrcalo odbačeno kao lanac** |

**Što se promijenilo za `digikat_akteri`.** Zapreka nije bila pravna nego
informacijska: nitko nije pročitao `DATA_AVAILABILITY.md`. Projekt je sam,
javno i pod imenom voditelja, objavio agregate pod CC BY 4.0 uz tvrdnju da ne
sadrže osobne podatke. Autor knjige i voditelj projekta ista su osoba, pa je
riječ o vlasničkoj dispoziciji, kakvu je `P3-EXISTING` već prihvatio kao temelj
promocije za generirane skupove.

Ostaje jedno pitanje koje nije tehničko i koje pripada autoru: agregati su
izvedeni iz korpusa prikupljenog preko Determa. Brojanje objava nije
redistribucija njihova sadržaja, i projekt je zauzeo stav da su agregati
njegovi — ali taj stav treba stajati na gateu izrijekom, a ne biti prešutno
naslijeđen.

**Zbog toga ovaj izvadak nije nazvan `digikat_akteri`.** Registrirana stavka
opisuje presjek imenovanih aktera po platformama; ono što je ovdje izvučeno
nema aktera i ne bi trebalo naslijediti njezino ime. Predlaže se novi
identifikator `digikat_mediji`, a `digikat_akteri` da se na gateu zatvori kao
napušten.

---

## 5. Što je izvučeno

Dvanaest datoteka u tri paketa. Nijedan još nije promoviran i nijedan nije
upisan u `katalog.yml`; vidi odjeljak 8.

### Paket A — `digikat_mediji` (digitalni mediji, komunikologija)

Gradi `scripts/build-digikat-extracts.R`; obavijest `data/digikat-mediji.LICENCA.md`.

| Datoteka | Redaka | MD5 |
|---|---|---|
| `data/digikat-platforme-godisnje.csv` | 49 | `fa7ed7c65b0940df9f96a0b3e7fdcff4` |
| `data/digikat-platforme-mjesecno.csv` | 438 | `3f36b9015a7c4634732998f5bf51ed3f` |
| `data/digikat-izvori.csv` | 3.604 | `fc90ae84bbb0b03d599a7b9cf3fcb08e` |

`digikat-izvori.csv` zadržava samo izvore čije je ime gola internetska domena, pa
u njemu nema nijedne imenovane osobe. Njegova raspodjela:

| Mjera | Objave | Doseg |
|---|---|---|
| aritmetička sredina | 153,1 | 376.786 |
| medijan | **4** | **1.080** |
| najveći | 56.500 (`hkm.hr`) | — |
| udio izvora s točno jednom objavom | **30,2 %** | — |
| udio deset najvećih u ukupnim objavama | 27,0 % | — |
| izvora s dosegom 0 | — | 515 |

Sredina je 38 puta veća od medijana. To je gotov predložak za poglavlje 4.

### Paket B — `rdp_potpore` (javne politike, politička ekonomija)

Gradi `scripts/build-croaicon-extracts.py`; obavijest `data/rdp-potpore.LICENCA.md`.

| Datoteka | Redaka | MD5 |
|---|---|---|
| `data/rdp-potpore-skupine.csv` | 3 | `4e1e1e01f82ac9dcbd719345dd076069` |
| `data/rdp-potpore-godisnje.csv` | 9 | `07de4f9a255867c8d7fa5037f7c70446` |
| `data/rdp-potpore-velicina.csv` | 5 | `d897df1defcfeb34bcf944530a3ed7e0` |
| `data/rdp-potpore-vrsta.csv` | 7 | `d27279aa779577ce82ad75fc03a0143a` |
| `data/rdp-potpore-obuhvat.csv` | 3 | `72360d93345ce45c90dcf96c273f1fc8` |
| `data/rdp-potpore-sazetak.csv` | 15 | `dec148517924041650657bc2a206506f` |

Naslovne brojke: 25.739 primatelja, 96.402 dodjele, 5,40 mlrd. eura,
2017.–2025. **Medijan po primatelju 7.000 eura, sredina 209.852 eura.** Gornjih
1 % primatelja (258 njih) nosi 71,57 % iznosa; gornjih 10 % nosi 94,48 %.
Gini 0,953.

Uz to ide tablica obuhvata, koja istu snimku registra uspoređuje sa službenim
godišnjim iznosom Ministarstva financija: **2021. reproducira 0,93 %, a 2023.
95,18 %**. Zbog nje `rdp-potpore-godisnje.csv` nije vremenska serija.

### Paket C — `bdp_dugi_niz` (ekonomska povijest, mjerenje i usporedivost)

Gradi ista skripta; obavijest `data/bdp-hrvatska.LICENCA.md`.

| Datoteka | Redaka | MD5 |
|---|---|---|
| `data/bdp-hrvatska-izvori.csv` | 103 | `0f24ccc32f0b8a8f58cd4cc84e9271c4` |
| `data/bdp-hrvatska-spojeni.csv` | 107 | `934e850d5ab213c266fc833f8981230c` |
| `data/bdp-hrvatska-razdoblja.csv` | 8 | `10ed2e5f9da4f5a045e39ebbeafbc9f4` |

Prva datoteka drži pet objavljenih procjena BDP-a po stanovniku jednu do druge,
1870.–2025., svaku u vlastitoj jedinici i s vlastitim obuhvatom. Redak se **ne
smije prosječiti**. Druga drži jedan spojeni niz s označenim šavovima i s
godinama 1991.–1995. označenima kao rekonstruirane. Treća sažima niz u razdoblja
čije je granice **odabrao analitičar**.

### Ponašanje skripti

Obje slijede obrazac iz `scripts/build-dzs-extracts.py`: bez `--write` samo
provjeravaju reproducira li se izvadak iz izvora bajt po bajt. Obje su provjerene
i prolaze. Ni jedna ne dira mrežu. Pet oblikovnih pravila (UTF-8 bez BOM-a, LF,
zarez kao razdjelnik, nijedna vrijednost ne sadrži razdjelnik ni navodnik,
nijedna prazna ćelija, puna preciznost) provodi se kodom, a ne dogovorom.

---

## 6. Karta integracije — gdje svaka datoteka zarađuje mjesto

Ovo je operativni dio izvidnice. Nijedan od ovih poteza nije napravljen; svaki
čeka svoje poglavlje i svoj gate.

| Poglavlje | Datoteka | Što nosi |
|---|---|---|
| **2 · mjerenje i dizajn** | `digikat-platforme-godisnje` | Što je „doseg”? Procjena pružatelja, ne izbrojene osobe. `metrika_dostupna` pokazuje da mjerni instrument ne pokriva sve platforme jednako. |
| | `bdp-hrvatska-izvori` | Pet mjerila iste stvari. Jedinica je dio mjerenja, ne detalj. |
| **3 · kako brojke zavode** | `rdp-potpore-obuhvat` | **Najjači slučaj u cijelom portfelju.** Ista baza, ista metoda, dvije godine: 0,93 % i 95,18 % službenoga iznosa. Rast u registru nije rast u svijetu. Kandidat za `callout-divljina`. |
| | `bdp-hrvatska-razdoblja` | Granice razdoblja bira analitičar; pomakni ih i priča se mijenja. |
| | `digikat-izvori` | Stopa angažmana s nazivnikom od jedne objave. Zamka omjera. |
| **4 · sažimanje** | `rdp-potpore-sazetak` | Medijan 7.000 prema sredini 209.852. Jedan redak koji sam objašnjava zašto medijan postoji. |
| | `digikat-izvori` | Zakošena raspodjela s 3.604 jedinice: sredina, medijan, mod, kvantili, Gini — sve na istom skupu. |
| **5 · vizualizacija** | `digikat-izvori` | Histogram koji traži logaritamsku os. Zašto linearna os ovdje ne radi. |
| | `bdp-hrvatska-spojeni` | Indeks 2015. = 100, označen šav i označene rekonstruirane godine. Kako se crta niz koji nije jednorodan. |
| | `digikat-platforme-mjesecno` | Sastav kroz vrijeme; udjeli koji se zbrajaju u cjelinu. |
| **6 · povezanost** | `digikat-izvori` | Objave, interakcije i doseg — tri zakošene varijable. Korelacija prije i poslije logaritmiranja. |
| **8 · uzorkovanje** | `rdp-potpore-obuhvat` | Okvir uzorkovanja nije populacija. Registar je *pokušaj* popisa, ne popis. |
| | `digikat-platforme-godisnje` | Korpus s pravilom ulaska „najmanje dva pojma” — namjerna selekcija, poznata i zapisana. |
| **13 · kategorički podaci** | `rdp-potpore-velicina`, `rdp-potpore-vrsta` | Udjeli po kategorijama; `Nepoznato` kao objavljena kategorija, ne kao rupa. |
| | `digikat-platforme-godisnje` | Platforma × godina kao kontingencijska tablica. |
| **15 · više grupa** | `rdp-potpore-velicina` | Pet razreda veličine, prosječna dodjela od 20.828 do 606.576 eura. |
| **17 · doba algoritama** | `digikat-platforme-godisnje`, `digikat-izvori` | Digitalni trag kao predmet društvene znanosti: što platforma mjeri, što ne mjeri i tko odlučuje o kategorijama. |
| **18 · vaše prvo istraživanje** | `digikat-izvori` | Skup dovoljno velik da se u njemu nešto nađe, dovoljno mali da ga student obradi, i s dokumentiranim granicama. |

**Pokrivenost područja.** S već postojećim paketima portfelj bi izgledao ovako:
generirani skupovi (metodologija), `dzs_turizam` (službena statistika,
geografija), `digikat_mediji` (komunikologija, digitalni mediji), `rdp_potpore`
(javne politike, politička ekonomija), `bdp_dugi_niz` (ekonomska povijest).

**Što i dalje nedostaje:** stavovi i psihologija na razini osobe. Nijedan od dva
pregledana izvora nema anketni skup s pojedincem kao jedinicom. To pokrivaju
`ess_r11_hr`, `vdem_v16`, `covidistress_ii`, `parlamint_hr` i `parlasent`, koji
su u katalogu registrirani i neriješeni. Ova izvidnica ih ne pomiče.

---

## 7. Što je odbijeno i zašto

Zapisano zato da se odluke ne moraju ponavljati.

| Odbijeno | Razlog |
|---|---|
| Cijela MySQL baza `odvjet12_gfi` | `gfi_fina`; komercijalna; osobni podaci u `data_api_person*` i `leads` |
| 28 tablica CroAIcona izvedenih iz FINA GFI | isto |
| 11 DigiKatovih tablica imenovanih aktera | imenovani pojedinci; knjiga ne objavljuje takvu tablicu |
| DigiKatov master korpus | `determ_korpus`; redistribucija nije dopuštena |
| Eurostatovo zrcalo u MySQL-u | staging s ponovljenim retcima; nije lanac provenijencije |
| Chow-Lin mjesečna razdioba BDP-a 1991.–1992. | modelirana veličina, ne opažanje; traži vlastiti gate |
| CroAIconove turističke tablice | preklapanje s `dzs_turizam`, koji ima čistu dozvolu |
| `avg_engagement_rate` | prosjek omjera; ne smije se zbrajati kroz godine |
| Uzvodni udjeli u pomičnom zarezu | zamijenjeni nazivnikom, po konvenciji kataloga |

---

## 8. Položaj prema upravljačkom sloju

**Ovo nije paket i ništa ne zatvara.** U trenutku pisanja
`active_write_packet` je `P3-DZS`, a `next_permitted_packet` je `null`.

Zbog toga ova izvidnica **nije dirala** registar provedbe, ledger isporuka ni
nadzornu ploču. Dirala je `katalog.yml` i njegovu shemu, i to samo onoliko
koliko je autorska odluka zabilježena niže u ovom odjeljku tražila.

**Zašto se moralo pitati autora.** Dvanaest izvadaka prvo je bilo u `data/` i to
je oborilo dvoja vrata: `check-katalog.py` i `check-data-integrity.R` oba traže
da svaka materijalizirana snimka u `data/` bude prijavljena u katalogu. To je
ispravno ponašanje i nije zaobiđeno.

Prijava, međutim, nije bila moguća bez odluke. `portfolio_caps` broji
**prijavljene** pakete, ne samo promovirane, i **svih osam nacrta stajalo je na
svojoj granici**:

| Nacrt | Granica | Prijavljeno |
|---|---|---|
| `seeded_simulation_known_population` | 3 | 3 |
| `probability_survey_with_weights` | 1 | 1 |
| `administrative_or_electoral_count` | 2 | 2 |
| `official_aggregate_statistics` | 4 | 4 |
| `expert_coded_latent_index` | 1 | 1 |
| `digital_trace_or_selected_corpus` | 3 | 3 |
| `volunteer_open_survey` | 1 | 1 |
| `restricted_commercial_or_administrative_source` | 2 | 2 |

Portfelj prvoga izdanja zatvoren je namjerno. Katalog izrijekom kaže da
prekoračenje granice traži **izričito autorsko odobrenje** i da „ne može nastati
u ovom paketu”. Nijedan od tri kandidata nije stao bez te odluke, a odluka
pripada autoru i ne smije se izmisliti kao zapis o gateu.

### Autorska odluka od 5. kolovoza 2026.

Autor je odlučio troje:

1. **Granice se podižu i sva tri paketa se prijavljuju**, bez ijedne promocije.
2. **DigiKatovi agregati su naši.** Brojanje objava nije redistribucija
   Determova sadržaja; objavljena dispozicija iz `DATA_AVAILABILITY.md` vrijedi
   i za knjigu. Master korpus ostaje `external-only`.
3. **Suglasnost suautora projekta AI.econ već postoji.** Preostale zapreke za
   dva CroAIcon paketa su uvjeti izvora (`rdp.gov.hr`) i Eurostatov stupac.

Odluka je izvedena ovako:

- `portfolio_caps` dobio je blok `author_approvals`, koji imenuje datum,
  odobravatelja, zapis, i za svaki nacrt granicu prije i poslije te paket zbog
  kojega je podignuta. Shema (`data/katalog.schema.json`) proširena je tim
  blokom, jer polja za bilježenje odobrenja dotad nije bilo — a odobrenje koje
  se ne može strojno pročitati nije zapis nego sjećanje.
- `digital_trace_or_selected_corpus` 3 → 4, `administrative_or_electoral_count`
  2 → 3, `official_aggregate_statistics` 4 → 5.
- Tri paketa upisana su sa statusom `registered_not_promoted`, `promoted: false`
  i bez `promoted_by`. Svaki nosi puni kodeks stupaca u `file_records`, s MD5
  po datoteci, rasponom redaka, ključem, jedinicom i kodom nedostajuće
  vrijednosti za svaki stupac.
- Vrata za svaki paket rezervirana su i imenovana: `G-A3-DIGIKAT`, `G-A3-RDP`,
  `G-A3-BDP`. Nijedan se ne smije promovirati pod tuđim gateom.

**Što odluka nije napravila.** Nijedan paket nije promoviran, `promoted_total`
ostaje 3 i nijedno poglavlje ne smije iz njih tvrditi ništa. `digikat_akteri`
ostaje u katalogu kakav je bio; prijedlog da ga se zatvori kao napuštenoga u
korist `digikat_mediji` odluka je za `G-A3-DIGIKAT` i nije prejudicirana.

### Stanje vrata nakon zahvata

```text
KATALOG_OK packages=20 promoted=3 bundled=8 portal=3 external=9 snapshots=20
DATA_INTEGRITY_OK snapshots=20 validated=20 reconciliations=9 undeclared=0
DATA_NEGATIVE_FIXTURES_OK cases=41
```

Izvadci se u svakom trenutku obnavljaju iz autorovih lokalnih checkoutova:

```text
Rscript scripts/build-digikat-extracts.R --checkout C:\Users\lsikic\projects\DigiKat
python scripts/build-croaicon-extracts.py --checkout C:\Users\lsikic\projects\CroAIcon
```

Bez `--write` obje skripte samo provjeravaju reproducira li se svaka datoteka
bajt po bajt; s `--write` je prepisuju.

### Mjesto u ratificiranom redoslijedu

Paketi nisu na redu i to nije zastoj nego raspored. Registar provedbe drži ovaj
niz:

| Redni broj | Paket | Vrsta | Stanje |
|---|---|---|---|
| 68 | `G-A3-DZS` | odluka | prihvaćena |
| **69** | **`P3-DZS`** | podatkovni | **u tijeku — aktivni paket** |
| 70–71 | `G-A3-DIP`, `P3-DIP` | odluka, podatkovni | ratificirani |
| 72 | `P3-PILOT` | čitateljski dokaz | **descopiran** autorskom izmjenom od 5. kolovoza 2026. |
| 73 | `P3-VERIFY-A` | pregled | ratificiran |
| 74–83 | `WA-C00` … `WA-PART` | poglavlja 0–3 | ratificirani |
| **84** | **`G-A3-DIGIKAT`** | odluka | **ratificiran, neizvršen** |
| **85** | **`P3-DIGIKAT`** | podatkovni | ratificiran |
| 86–87 | `G-A3-EUROSTAT`, `P3-EUROSTAT` | odluka, podatkovni | ratificirani |

`digikat_mediji` čeka vrata na 84. To je petnaest koraka od aktivnoga paketa i
dolazi tek nakon prvoga vala poglavlja. Do tada paket miruje u katalogu, što je
i smisao registracije bez promocije.

`rdp_potpore` i `bdp_dugi_niz` **nemaju redni broj u programu**. Ratificirani
plan nikada nije predvidio CroAIcon kao izvor; predvidio je samo `gfi_fina`, i
to je zabranio. Vrata `G-A3-RDP` i `G-A3-BDP` imenovana su u katalogu, ali još
nisu upisana u registar, i ta je praznina zabilježena kao caveat uz oba paketa.
Njihovo uvođenje mijenja registar i traži autorsko odobrenje na zatvaranju
paketa; ne može nastati usput.

### Dva vanjska pitanja koja ova izvidnica zatvara

Registar drži dva `outside ask`-a vezana uz `G-A3-DIGIKAT`, oba u stanju
`drafted_unsent`:

- **`OA-G-A3-DIGIKAT-RIGHTS`** — tražila je „component-by-component rights
  matrix”. Spremnost joj je stajala na `waiting_for_component_terms`. Matrica je
  u odjeljku 4 ovoga izvještaja, a autor je 5. kolovoza 2026. prihvatio
  dispoziciju. **Materijalno je odgovorena**; formalno je zatvara `G-A3-DIGIKAT`.
- **`OA-G-A3-DIGIKAT-SELECTION`** — tražila je „one dated selection disposition
  naming actors, platforms, snapshot, exclusions, and claim boundary”. Spremnost
  joj je stajala na `waiting_for_catalogue_contract`; taj ugovor sada postoji.
  Sve četiri stavke su u ovom izvještaju i u zapisu paketa `digikat_mediji`.
  Preostaje jedna razlika koju gate mora presuditi: ask govori o **akterima**, a
  ovaj izvadak aktera nema i namjerno ih izostavlja.

Preporučena zadana dispozicija iz registra glasi „Use a portable aggregate with
public labels and method-break/coverage caveats; keep the full Determ corpus
external”. To je točno ono što je izgrađeno.

**Što još treba prije nego što ijedno poglavlje smije iz njih tvrditi bilo što:**

1. **`G-A3-DIGIKAT`** — ostaju dvije stavke: (a) zatvara li se `digikat_akteri`
   kao napušten u korist `digikat_mediji`; (b) potvrđuje li se izostavljanje
   tablica s imenovanim akterima kao trajno pravilo, a ne kao jednokratni izbor.
   Pitanje prava riješeno je odlukom od 5. kolovoza 2026.
2. **`G-A3-RDP`** — utvrditi objavljene uvjete ponovne uporabe registra
   `rdp.gov.hr`. Suglasnost suautora više nije zapreka. Dok uvjeti izvora nisu
   utvrđeni, licenca u katalogu pokriva **samo izvedene agregate**, ne i sam
   registar, i tako je i zapisana.
3. **`G-A3-BDP`** — razriješiti Eurostatov stupac (traka `portal-mediated`) i
   potvrditi uvjete MPD-a za prikaz jedne zemlje. Licenca u katalogu pokriva
   **samo sastav i spojeni niz**; pet komponenti zadržava vlastite uvjete.
4. **Usklađenje sa službenim izvorom.** Nijedan od tri paketa nema
   `official_reconciliation` i to je zapisano kao takvo. Za `rdp_potpore` ga ne
   može ni biti — datoteka obuhvata upravo je zapis o neusklađenosti. Za
   `bdp_dugi_niz` je nemoguće jer pet stupaca nose pet jedinica. Za
   `digikat_mediji` ne postoji jer nije riječ o službenoj statistici. Sva tri
   razloga stoje u `integrity.note`.
5. **Zapis o pravima.** `rights_boundary` u katalogu i dalje stoji na
   `rights_holder_permission_obtained: false` i to je točno: dopuštenje ni od
   koga nije traženo. Ono što postoji za DigiKat jest **vlastita objavljena
   dispozicija voditelja projekta**, što nije isto i tako je i upisano u polje
   `redistribution` toga paketa.

---

## 9. Kako se portfelj širi dalje

Autorova je uputa bila da se pripremi i položaj prema budućem proširenju. Ovo je
obrazac koji je izvidnica ostavila iza sebe.

**Jedna skripta po vanjskom izvoru, uvijek isti oblik.** `--checkout` ili
`--mirror` pokazuje na autorovu lokalnu kopiju; bez `--write` skripta samo
provjerava reproducira li se izvadak bajt po bajt. Nijedna ne dira mrežu.
Sada ih je tri: `build-dzs-extracts.py`, `build-croaicon-extracts.py`,
`build-digikat-extracts.R`.

**Redoslijed koji se pokazao ispravnim, i koji treba ponoviti:**

1. Pročitaj izvorov **vlastiti** zapis o pravima prije podataka. Za DigiKat je
   `DATA_AVAILABILITY.md` promijenio zaključak; za CroAIcon je `.gitignore`
   pokazao da izlazi nisu javni.
2. Razdvoji izvor na razine. Gotovo svaki ima jednu razinu koja se smije dijeliti
   i drugu koja se ne smije. Master naspram agregata, javni registar naspram
   komercijalne kopije.
3. Odbaci sve što imenuje pojedinca, i onda kada je licenca čista.
4. Traži skup koji nosi **metodološku pouku**, ne samo brojke. Tablica obuhvata
   državnih potpora vrijedi više od cijeloga sektorskog panela, jer panel govori
   o gospodarstvu, a tablica obuhvata govori o podacima.
5. Zapiši nedostajuće vrijednosti prije nego što ih itko vidi. Nula, „nije
   mjereno” i „nije objavljeno” tri su različite stvari i izvori ih redovito
   miješaju.
6. Ne zaobilazi katalog. Datoteka u `data/` bez zapisa u `katalog.yml` nije
   nastavni skup, koliko god bila zanimljiva.

**Prvi sljedeći kandidati, po omjeru koristi i troška prava:** anketni skup s
pojedincem kao jedinicom (`ess_r11_hr`), koji je jedina veća rupa u pokrivenosti
područja; zatim `eurostat_drustvo` s Eurostatova sučelja, koji je jeftin jer je
traka već određena.

---

## Prilog — datoteke nastale u ovoj izvidnici

**Nove datoteke:**

| Putanja | Vrsta |
|---|---|
| `scripts/build-digikat-extracts.R` | graditelj izvatka |
| `scripts/build-croaicon-extracts.py` | graditelj izvatka |
| `data/digikat-mediji.LICENCA.md` | obavijest o licenci |
| `data/rdp-potpore.LICENCA.md` | obavijest o licenci |
| `data/bdp-hrvatska.LICENCA.md` | obavijest o licenci |
| dvanaest izvadaka iz odjeljka 5 | podatkovne snimke u `data/` |
| `notes/reports/vanjski-izvori-croaicon-digikat-2026-08-05.md` | ovaj izvještaj |

**Izmijenjene datoteke:**

| Putanja | Izmjena |
|---|---|
| `data/katalog.yml` | tri nova paketa; `author_approvals`; tri podignute granice |
| `data/katalog.schema.json` | dodan blok `author_approvals` u `portfolio_caps` |

Registar provedbe, ledger isporuka i nadzorna ploča nisu dirani. Sva troja
vrata — `check-katalog.py`, `check-data-integrity.R` i
`check-data-fixtures.py` sa 41 negativnim slučajem — prolaze.
