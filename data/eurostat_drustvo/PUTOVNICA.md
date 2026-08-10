# Putovnica skupa `eurostat_drustvo`

**Snimka izvora:** jedan odobreni batch od šest GET zahtjeva prema službenom
Eurostatovu Dissemination API-ju, dovršen 10. kolovoza 2026. između
12:39:03 i 12:39:10 UTC, bez ponavljanja zahtjeva. Točni URL-ovi stoje u
`UPITI.json`, a neizmijenjeni odgovori u mapi `raw/`.

**Jedinica:** jedna država članica EU-a za jedan pokazatelj u 2025. godini.
Redak nije osoba. Tablica zato može opisivati razlike i povezanosti među
državama, ali ne ponašanje pojedinaca niti uzrok tih razlika.

**Ključ:** `geo + godina + pokazatelj`. Postoji svih 162 očekivanih ključeva:
27 država puta šest pokazatelja. Brojčanu vrijednost ima 161 ključ; jedan
zadržava službenu odsutnost vrijednosti.

## Odabrani rezovi

| Pokazatelj | Skup i izvorni rez |
|---|---|
| Stopa zaposlenosti od 20 do 64 godine | `lfsi_emp_a`: `EMP_LFS`, `T`, `Y20-64`, `PC_POP` |
| Rizik od siromaštva ili socijalne isključenosti | `ilc_peps01n`: `TOTAL`, `T`, `PC` |
| Tercijarno obrazovanje od 25 do 34 godine | `sdg_04_20`: `T`, `Y25-34`, `PC`, `ED5-8` |
| Rano napuštanje obrazovanja od 18 do 24 godine | `edat_lfse_14`: `T`, `POP`, `Y18-24`, `PC` |
| Uporaba interneta u prethodna tri mjeseca | `isoc_ci_ifp_iu`: `I_IU3`, `PC_IND`, `IND_TOTAL` |
| Udio stanovništva od 65 godina naviše | `demo_pjanind`: `PC_Y65_MAX` |

Svaki je rez godišnji (`freq = A`), svaka je godina `2025`, a geografije su
točno `AT`, `BE`, `BG`, `CY`, `CZ`, `DK`, `EE`, `FI`, `FR`, `DE`, `EL`, `HR`,
`HU`, `IE`, `IT`, `LV`, `LT`, `LU`, `MT`, `NL`, `PL`, `PT`, `RO`, `SK`, `SI`,
`ES` i `SE`. Agregat `EU27_2020` nije dohvaćen i nije jedinica analize.

## Datoteke i dokaz

| Datoteka | Uloga | Kontrolni zbroj |
|---|---|---|
| `data/eurostat-drustvo-2025.csv` | nastavni izvadak, 162 retka | MD5 `1dc076aeac134b6bbf9022ece6475747` |
| `data/eurostat_drustvo/UPITI.json` | šest točnih upita prije dohvata | SHA-256 `d80278ea9e454e10af504ccb3560df977275060136e0156ac3985593d3147074` |
| `data/eurostat_drustvo/PREUZIMANJE.json` | datum, HTTP trag i checksum svakoga odgovora | SHA-256 `335fab2e89eeb473ba7fa31d872fde3eb2f5feed1435cc63fb4b738e12941481` |
| `data/eurostat_drustvo/USKLADJENJE.json` | 162 usporedbe s izvornim ćelijama | SHA-256 `1b381e306c1ee2243af08ef41e9ade453a8cedd0f35e8f614d936580e8ad4180` |

Skripta `scripts/build-eurostat-extracts.py` u načinu bez argumenata ponovno
gradi CSV i usklađenje isključivo iz lokalnih sirovih odgovora. Provjerava oba
checksuma svakoga odgovora, svih šest izvornih rezova, 27 geografija, 162
jedinstvena ključa, sve vrijednosti i statuse, pa uspoređuje izvedene datoteke
bajt po bajt. Tolerancija je nula.

## Izvorne verzije

| Skup | Verzija strukture | Vrijeme ažuriranja podataka u odgovoru |
|---|---:|---|
| `lfsi_emp_a` | 47.0 | 11. lipnja 2026. u 23:00 +0200 |
| `ilc_peps01n` | 80.0 | 8. lipnja 2026. u 23:00 +0200 |
| `sdg_04_20` | 44.0 | 11. lipnja 2026. u 23:00 +0200 |
| `edat_lfse_14` | 48.0 | 11. lipnja 2026. u 23:00 +0200 |
| `isoc_ci_ifp_iu` | 52.0 | 17. travnja 2026. u 11:00 +0200 |
| `demo_pjanind` | 33.0 | 10. kolovoza 2026. u 11:00 +0200 |

## Oznake kvalitete i nedostajanje

Eurostatov JSON-stat odgovor za odabrane ćelije daje jedan točan statusni
token. `status_api` prenosi ga doslovno. `obs_status` klasificira opažačku
oznaku, a `conf_status` oznaku povjerljivosti. U odabranom presjeku svi
objavljeni tokeni jesu opažačke oznake i nijedan nije oznaka povjerljivosti;
`conf_status` zato je u svih 162 retka `bez_objavljene_oznake`. Sirovi token
ostaje zasebno vidljiv, pa razdvajanje ništa ne skriva.

| Token | Izvorno značenje | Broj redaka |
|---|---|---:|
| `bez_objavljene_oznake` | izvor nije objavio statusni token | 150 |
| `b` | break in time series | 2 |
| `d` | definition differs (see metadata) | 4 |
| `e` | estimated | 1 |
| `ep` | estimated, provisional | 1 |
| `p` | provisional | 2 |
| `u` | low reliability | 2 |

Jedina odsutna brojčana vrijednost jest Luksemburg u pokazatelju ranoga
napuštanja obrazovanja. Ostaje kao `vrijednost = :`, `status_api = u` i
`vrijednost_dostupna = ne`. Nije pretvorena u nulu, nije ispuštena i nije
popunjena drugom godinom. Hrvatska vrijednost istoga pokazatelja također nosi
`u`, ali je objavljena kao 2.1; zastavica zato nije isto što i nedostajanje.

## Putovi uporabe

- U R-u se `vrijednost` prvo čita kao tekst; `:` se pretvara u nedostajuću
  vrijednost tek nakon što se sačuvaju `status_api`, `obs_status` i
  `conf_status`. Kontrole su 162 retka, 161 broj i jedan `:`.
- U podržanom putu bez koda `vrijednost` ostaje tekst pri uvozu, a zasebna se
  brojčana kopija stvara bez zamjene `:` nulom. Ključ mora ostati trodijelan.
- U tisku statična tablica ili graf mora označiti Luksemburg kao nedostupan i u
  legendi objasniti svaki prikazani status. Interaktivni portal nije potreban.

## Dopuštene i nedopuštene tvrdnje

Dopušten je opis usporedivih državnih agregata u zajedničkoj 2025. godini,
raspršeni dijagram, koeficijent povezanosti među državama i pitanje mijenja li
dobna struktura čitanje veze. Oznake kvalitete moraju ostati vidljive.

Nije dopušten zaključak o pojedincu, uzročnosti, zemlji izvan EU-a, miješanje
godina ni tvrdnja da statusom označene vrijednosti imaju jednaku kvalitetu kao
neoznačene. Jedan presjek ne pokazuje promjenu kroz vrijeme.

Točna atribucija, oznaka izmjena, disclaimer i granica sadržaja trećih strana
stoje u `data/eurostat-drustvo.LICENCA.md`. Dohvat se ne ponavlja u renderu.
