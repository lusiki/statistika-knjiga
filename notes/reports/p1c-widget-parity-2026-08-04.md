# P1C-PARITY — blokirajuća provjera pariteta widgeta

Datum: 2026-08-04

Paket: `P1C-PARITY`

Implementacijski commit: `79824e0524ec542b0ec1a8ae0610f1d4140d4053`

Stanje pariteta: `parity:sha256-f22f3df467e42c14d2954820e1a7de39df67c374565123c418c366a0eb51a803`

## Granica paketa

Paket uvodi samo blokirajući numerički ugovor između 17 OJS widgeta i njihovih
17 R blizanaca za tisak. Nije promijenjen nijedan izvor poglavlja, prikaz,
kontrola, simulacijski postupak, sjeme, ponašanje widgeta, tekst poglavlja,
inventar stranica, katalog, procjena, izvoz, opća preglednička provjera ni
release-candidate postupak. Prihvaćeni nalaz `P1A-METHODS` ostaje mjerodavan:
par `w10` provjerava postojeće analitičke normalne p-vrijednosti, a ne naknadno
uvodi Monte Carlo permutacijsku korekciju. Različite populacije i generatori u
`w08` također ostaju namjerni; paritet se ondje odnosi na standardizirano
sužavanje i simetrizaciju, ne na jednakost sirovih podataka.

## Ugovor i naredbe

- `data/widgets.json` je jedini registar parametara, politike sjemena,
  tolerancija, zlatnih vrijednosti po adapteru, adaptera, otisaka izvora i
  granice tvrdnje za svaki par.
- `scripts/widget-parity-ojs.mjs` računa numeričke tvrdnje postojećih OJS
  implementacija uz isti D3 LCG i normalni generator gdje se oni koriste.
- `scripts/widget-parity-r.R` računa iste ograničene tvrdnje iz postojećih R
  blizanaca i njihovih `set.seed()` politika.
- `python scripts/check-widget-parity.py .` provjerava shemu, točno 17 uređenih
  parova, šest egzaktnih i jedanaest distribucijskih klasifikacija, zlatne
  vrijednosti, međuedicijske tolerancije, invarijante i SHA-256 izvora.
- `python scripts/check-widget-parity-fixtures.py` ne mijenja datoteke: u
  memoriji pomiče jednu OJS zlatnu vrijednost i zahtijeva blokirajući izlaz.
- Obje su naredbe samostalne. Objavni workflow poziva pozitivnu provjeru i
  negativnu fixturu kao blokirajuće korake prije PDF-a, rendera, Pages postave i
  prijenosa artefakta; nema `continue-on-error`, pričuvnog puta ni objave.

Otisak OJS izvora nastaje iz svih normaliziranih OJS blokova pripadnog
registriranog poglavlja, uz obvezno točno jedan blok oznake `fig-wNN`. Otisak R
izvora nastaje iz točno jednog normaliziranog R bloka oznake `fig-wNN-print`.
Svaka promjena tih izvora zato traži svjesno ponovno izvođenje i, samo ako je
tvrdnja doista promijenjena, obnovu odgovarajuće zlatne vrijednosti.

Stanje pariteta izračunano je kao SHA-256 uređenog manifesta `putanja<TAB>Git
blob` za workflow, registar, comparator, fixturu i oba adaptera na navedenom
implementacijskom commitu. Git blobovi su:

| Putanja | Git blob |
|---|---|
| `.github/workflows/publish.yml` | `2e0f32d8ef9ac6424e56f1400a8902115a16b040` |
| `data/widgets.json` | `f4367e7588bdd5a71e14ea3267e9141a54ae1e8f` |
| `scripts/check-widget-parity.py` | `5da2aa8616e8092a29999932ac400d073ae1796d` |
| `scripts/check-widget-parity-fixtures.py` | `4cf2b535b2838b5340ada54c1373eb122adda5fe` |
| `scripts/widget-parity-ojs.mjs` | `d5941fb93927b99f734607d73c3ac45575bca9d3` |
| `scripts/widget-parity-r.R` | `1e2cbea265f361ce1ff87af003c8284deb931d55` |

## Svih 17 zapisa

U sljedećoj tablici vektori su navedeni istim redom za OJS i R. Potpuna imena
svake metrike, svi parametri, zasebne i zajedničke politike sjemena, svaka
tolerancija i puni tekst granice tvrdnje zapisani su strojno čitljivo uz
odgovarajući `wNN.parity` u `data/widgets.json`.

| Par | Vrsta; parametri i sjeme | Zlatne vrijednosti OJS / R | Međuedicijski ugovor i granica |
|---|---|---|---|
| `w01` | egzaktni; udjeli 0,80/0,20; bez RNG-a | zbirno A/B, lako A/B, teško A/B: OJS `0,68; 0,42; 0,8; 0,9; 0,2; 0,3`; R jednako | aps. `1e-10`; samo stope, ne geometrija |
| `w02` | egzaktni; pomak 4; bez RNG-a | zbirni/niski/visoki nagib: OJS `0,274938895; -0,574984740; -0,574984740`; R jednako unutar `1e-15` | aps. `1e-10`; samo nagibi 32 konstruirana opažanja |
| `w03` | egzaktni; `n=250/1000`, udio 0,52, pristranost 0/0,06; bez RNG-a | za svako stanje procjena, istina, margina i granice; puni vektori su u registru | aps. `1e-10`; analitička margina ne obuhvaća sustavnu pristranost |
| `w04` | egzaktni; kompaktno, ekstrem 70, raspon 3; bez RNG-a | sredina/medijan/SD/IQR: `11/11/1,825742/2`; `16,9/11,5/18,746555/2,75`; `11/11/5,477226/6`, oba adaptera | aps. `1e-10`; bez usporedbe slaganja točaka |
| `w05` | distribucijski; `n=72`, sjeme 505, šum 0,85, pomak 0,8; D3 LCG nasuprot `rnorm` | OJS sredina/SD/A/B/razlika/nagib `4,848658; 1,729299; 4,396670; 5,300647; 0,903977; 0,529968`; R `4,857675; 2,037000; 4,405292; 5,310059; 0,904767; 0,670554` | tolerancije `0,35/0,35/0,4/0,4/0,45/0,2`; isti model i pozitivan nagib, ne jednaki retci ili jitter |
| `w06` | distribucijski; četiri `rho`, `n=54`, OJS 606–609, R jedan tok 606 | korelacije OJS `-0,826770; -0,417225; 0,557795; 0,717768`; R `-0,848156; -0,533684; 0,400575; 0,767832` | aps. `0,2`; predznak i približna jakost, ne jednake točke |
| `w07` | distribucijski; `p=0,30`, `n=20/200`, 2.000 ponavljanja, sjeme 707 | OJS sredine/SD/repovi i omjer `0,302375/0,101960/0,15/0,45; 0,300770/0,032435/0,245/0,355; 3,143507`; R `0,300825/0,102936/0,15/0,50; 0,299523/0,032337/0,245/0,355; 3,183195` | tolerancije po registru do `0,05`, omjer `0,5`; ne jednaki nizovi ili binovi |
| `w08` | distribucijski; `n=5/40`, 2.000 ponavljanja, sjeme 808; eksponencijalna OJS populacija i beta R populacija | OJS omjeri SE/asimetrije/pomaci `0,447720/0,880432/0,008852; 0,159044/0,264918/0,001477`, smanjenje `0,615514`; R `0,446027/0,689841/-0,006220; 0,159954/0,195094/0,004330`, smanjenje `0,494747` | provjeravaju se omjeri SE i centriranje te `n40<n5` i pozitivno smanjenje asimetrije; bez tvrdnje o jednakim populacijama |
| `w09` | distribucijski; `n=40`, 50 intervala, kritična 1,96; OJS 908, R 909 | obuhvat/širina/srednja procjena OJS `0,96; 0,619806; -0,017837`; R `0,92; 0,619806; -0,009884` | tolerancije `0,15; 1e-10; 0,2`; postupak obuhvata, ne isti promašeni intervali |
| `w10` | distribucijski; `n=60`, učinak 0,35, prag 0,05, 4.000 ponavljanja, sjeme 1010 | nulta/učinkovita stopa odbacivanja i sredina p: OJS `0,05325; 0,48425; 0,495671; 0,159449`; R `0,051; 0,47725; 0,502124; 0,157769` | aps. `0,04`; samo postojeće analitičke normalne p-vrijednosti, ne permutacijski Monte Carlo |
| `w11` | distribucijski; `d=0,2/0,4/0,6`, `n=40/80/160/300`, 2.000 ponavljanja, sjeme 1111 | svih 12 točaka snage i prvi `n≥0,8` po adapteru; puni vektori su u registru; prvi `n`: OJS/R `null, 100, 50` | snaga aps. `0,06`, prvi `n` `0/30/30`; snaga raste s učinkom, bez generalizacije na druge testove |
| `w12` | distribucijski; 1/12/48 putova, 5.000 ponavljanja, sjeme 1212 | nominalno/korigirano/CDF 0,01 OJS `0,0462/0,0462/0,0096; 0,4524/0,0514/0,1114; 0,9202/0,0486/0,3792`; R `0,0498/0,0498/0,0102; 0,4656/0,0476/0,1098; 0,9146/0,0470/0,3818` | aps. `0,04`, rast nominalne stope; neovisni putovi i Bonferroni, ne stvarno ovisni putovi |
| `w13` | egzaktni; `n=80`, pomaci 0/45/80 %; bez RNG-a | za pomake 0/18/32: doprinos `0/8,1/25,6`, hi-kvadrat `0/32,4/102,4`, V `0/0,45/0,8`, oba adaptera | aps. `1e-10`; frekvencije i statistike, ne položaj oznaka |
| `w14` | distribucijski; neovisni/upareni `n=50`, razlika 5, SD 10, korelacija 0,65, sjeme 1414; 1.500/4.000 ponavljanja | teorijski SE/sredina/SD OJS `2/4,972878/2,031019; 1,183216/4,983955/1,201567`; R `2/5,020459/2,048514; 1,183216/5,002823/1,169182`; omjer oba `0,591608` | teorija i omjer aps. `1e-10`, simulacije `0,15`; upareni SE manji, ne isti uzorci ili binovi |
| `w15` | egzaktni; 24 po skupini, sredine `52/52/52` ili `46/52/58`, SD 6/11; različiti RNG-i standardizirani na iste momente | zajednička sredina/MS između/MS unutar/F: `52/0/36/0`; `52/864/36/24`; `52/864/121/7,140496`, oba adaptera | aps. `1e-10`; ne uspoređuju se standardizirane točke ni jitter |
| `w16` | distribucijski; `n=52`, sjeme 1616, korisnički pravac 10 + 4,5x; različiti RNG i redoslijed | odsječak/zbirni/prilagođeni nagib/minimum SSE/korisnički SSE/omjer OJS `8,687122/4,797800/2,041729/1540,066/1562,032/1,014263`; R `9,098363/4,587964/2,020079/2561,140/2575,906/1,005766` | uspoređuju se koeficijenti i omjer; u oba adaptera korisnički SSE nije manji, a zbirni nagib je veći; sirovi SSE među izdanjima nije tvrdnja |
| `w17` | distribucijski; prag 0,60, temeljne stope 0,20/0,45, 6.000 po klasi, sjeme 1717 | FPR/FNR/PPV-A/točnost-A/PPV-B/točnost-B OJS `0,051333/0,296667/0,774028/0,899600/0,918101/0,838267`; R `0,049500/0,288833/0,782218/0,902633/0,921598/0,842800` | aps. `0,03`, PPV-B veći; zapisani referentni ishod nije proglašen nepogrešivom istinom |

## Dokaz iz čiste zaključane okoline

Iz commita `79824e0524ec542b0ec1a8ae0610f1d4140d4053` stvorena je odvojena
detached radna kopija. R biblioteka, R cache, izvorne i binarne pohrane,
`R_LIBS_USER`, npm cache i Playwrightovi preglednici bili su usmjereni u nove
prazne direktorije; `RENV_CONFIG_CACHE_ENABLED=FALSE`. Javna naredba
`python scripts/restore-dependencies.py` iz zaključanih datoteka završila je:

```text
R_RESTORE_OK version=4.6.0 direct_packages=19 detected_packages=22
BROWSER_RESTORE_OK version=1.62.1
DEPENDENCY_RESTORE_OK r_lock=renv.lock playwright=1.62.1 node=24.15.0 npm=11.12.1
```

Pozitivna provjera u istoj okolini završila je:

```text
WIDGET_PARITY_OK pairs=17 exact=6 distributional=11
WIDGET_PARITY_NEGATIVE_FIXTURES_OK fixtures=1
CLEAN_LOCKED_WORKTREE_OK
```

Izravna namjerna regresija `expected-value-regression` pomaknula je samo
memorijsku vrijednost `w01/ojs/default.aggregate_a` s
`0.6800000000000002` na `0.6900000000000002`. Comparator je prijavio zlatno
i međuedicijsko odstupanje te završio izlazom 1:

```text
WIDGET_PARITY_FAILED errors=2
EXPECTED_PARITY_FAILURE fixture=expected-value-regression exit=1
```

Nakon obnove, pozitivne i negativne provjere `git status --short` nije vratio
nijedan zapis. Nisu pokrenuti render, upload, deploy ni publish.

Završni `scripts/check-review-workflow.R` prihvatio je zatvoreno stanje s
`next_permitted_packet: P1C-INVENTORY`. Obvezne kontrolne fixture
`generic_packet_evidence` i `invalid_outside_ask_link` obje su namjerno
završile izlazom 1.

## Budući učinci

Paket nije otkrio nov budući učinak. `P1-VERIFY` već izravno ovisi o
`P1C-PARITY`, a blokirajući workflow i otisci izvora automatski prenose ugovor
na svaku kasniju promjenu widgeta i na kasnije release provjere. Zasebni
`P1C-INVENTORY`, inventari, šira preglednička i konačna cross-format provjera
ostaju u već ratificiranim paketima; novi handoff bi duplicirao postojeće
ovisnosti.
