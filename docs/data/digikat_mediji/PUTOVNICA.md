# Putovnica skupa `digikat_mediji`

**Snimka izvora:** agregati projekta DigiKat na commitu
`278a127f9170c1aca82035a4a8357b8a995f91d8`, s datumom izvora
22. srpnja 2026. Checkout je ponovno provjeren 10. kolovoza 2026. i nije se
pomaknuo. Puni korpus nije čitan.

**Jedinica:** agregatna ćelija. U godišnjoj datoteci redak je platforma u
godini, u mjesečnoj platforma u mjesecu, a u datoteci izvora jedna gola
internetska domena kroz cijeli raspon. Redak nije objava ni osoba.

**Pravilo ulaska:** korpus obuhvaća praćene objave koje sadrže najmanje dva
različita katolička pojma iz projektnoga popisa. Nije slučajan uzorak hrvatskih
medija, javnosti ni korisnika platforme.

## Datoteke i provjera

| Datoteka | Redaka | Ključ | MD5 |
|---|---:|---|---|
| `data/digikat-platforme-godisnje.csv` | 49 | `godina + platforma` | `d3b5c32aac2a42c72e93d84472d4ca58` |
| `data/digikat-platforme-mjesecno.csv` | 438 | `mjesec + platforma` | `8809a751fdc05236fc54d55986c366ed` |
| `data/digikat-izvori.csv` | 3.604 | `izvor` | `fc90ae84bbb0b03d599a7b9cf3fcb08e` |

Skripta `scripts/build-digikat-extracts.R` ponovno gradi sva tri izvatka iz
triju uzvodnih agregata i uspoređuje ih bajt po bajt. Šest godišnjih nazivnika
jednako je zbroju pripadnih platformi bez tolerancije.

Godišnja i mjesečna datoteka odstupaju u 17 od 49 ćelija. Razlika je definirana
kao mjesečno minus godišnje: najveća je +446 za `web` 2022., najmanja −389 za
`web` 2024., a ukupan je zbroj razlika točno 0. Obje datoteke nose 710.307
objava. To nije usklađenje sa službenom statistikom, koje za ovaj vlasnički
korpus ne postoji, nego treći dio imenovane zamjene koja traži i reprodukciju
bajt po bajt i identitet nazivnika.

## Oznake kvalitete

`godina_potpuna` je `da` samo za 2021., 2022., 2023. i 2025. Godini 2024.
nedostaju veljača–svibanj, a siječanj joj je djelomičan s 1.911 objava. Godina
2026. završava u lipnju.

`lom_metode` razlikuje razdoblje prije promjene obuhvata, ulazak TikToka od
srpnja 2023., lom serije u lipnju 2024. i ulazak Instagrama od srpnja 2024.
Mjesečna rupa 2024. mora ostati vidljiva; ne interpolira se i ne izglađuje.

`metrika_dostupna = ne` znači da nula u interakcijama i dosegu nije izmjerena
nula. Zato se platforma bez mjerenja ne uspoređuje s platformom koja mjerenje
ima.

Datoteka izvora sadrži 3.604 domene s ukupno 551.712 objava, odnosno 77,67 % od
710.307. Svaki udio iz te datoteke koristi 551.712 kao nazivnik.

## Dopuštene i nedopuštene tvrdnje

Dopušten je opis raspodjele broja objava po platformama i domenama unutar
odabranoga korpusa, uz oznake kvalitete i mjerenja. Nisu dopuštene tvrdnje o
hrvatskom medijskom prostoru ili javnom mnijenju, o broju različitih osoba koje
su nešto vidjele, o pojedinačnoj objavi ili imenovanom akteru, o trendu kroz
2024. ni usporedba prije i nakon lipnja 2024. bez navedenoga loma metode.

## Putovi uporabe

- U R-u se tri CSV datoteke čitaju kao UTF-8, bez pretvaranja oznaka
  `lom_metode` i `metrika_dostupna` u brojeve. Kontrolni su rezultati 49, 438 i
  3.604 redaka te zbrojevi 710.307, 710.307 i 551.712 objava.
- U podržanom putu bez koda uvoz mora zadržati `mjesec` kao tekst `YYYY-MM` i
  oznake kao kategorije. Isti kontrolni zbrojevi moraju se dobiti bez
  popunjavanja rupe u 2024.
- Za tisak ova putovnica daje provjerljivu statičnu kontrolnu tablicu. Paketi
  `WB-C04`, `WB-C05` i `WB-C06` iz nje grade svoje konkretne tablice zadatka;
  ne smiju pretpostaviti da čitatelj ima interaktivni prikaz.

Paket je pod CC BY 4.0. Točna atribucija, oznake izmjena i granica između
agregata i nedostupnoga punog korpusa nalaze se u
`data/digikat-mediji.LICENCA.md`. Knjiga ne tvrdi da je pribavila dopuštenje
nositelja prava; ono nije traženo.
