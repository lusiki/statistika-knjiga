# data/

Ova mapa prima samo licenčno provjerene podatkovne pakete u traci `bundled` i
tri metapodatkovna artefakta knjige. Mrežni pristup datoteci nije dovoljan za
njezino spremanje ili redistribuciju.

| Datoteka | Podrijetlo | Urezuje se? |
|----------|-----------|-------------|
| `katalog.yml` | kanonski katalog podataka; jedini strojno čitljiv zapis | da |
| `katalog.schema.json` | shema kataloga; provjerava je `scripts/check-katalog.py` | da |
| `ai-exports.json` | generira `R/build-ai-exports.R` pri svakom renderu | da (sjemenska prazna inačica je već tu) |
| `concept-graph.json` | generira `R/build-concept-graph.R`, ručno | da |
| `widgets.json` | održava se ručno; jedini popis widgeta | da |
| `*-mreze*.csv`, `*-medija*.csv` | snimke generiranih nastavnih skupova; piše ih `scripts/build-data-snapshots.R` | da, uz kontrolni zbroj u katalogu |
| `*.LICENCA.md` | obavijest o licenci koja putuje uz svaku snimku | da |
| ostalo | dohvaća `R/fetch-podaci.R` samo iz provjerenih izvora | da, samo uz izričito provjerenu redistribuciju i traku `bundled` |

JSON datoteke iz tablice nisu nastavni skupovi podataka. Svaki nastavni paket
mora imati zapis o izvoru, inačici, licenci, atribuciji, pristupu,
redistribuciji, jednoj traci i zakonitoj zamjeni za svaki obvezni studentski
put. Skup bez tog zapisa ne smije se koristiti u poglavlju. Paketi u trakama
`portal-mediated` i `external-only` ne pohranjuju se u ovoj mapi.

Izvor simuliranih nastavnih skupova ostaje kod. Generator je
`R/podaci-nastavni.R`, poziva ga `R/setup.R`, a skupovi `anketa_mreze` i
`populacija_medija` time su dostupni svakom poglavlju bez učitavanja datoteke.
Od paketa P3-EXISTING uz njih stoje i determinističke CSV snimke, koje postoje
zbog jamovija, tiska i preuzimanja, a ne zato da bi zamijenile generator:

| Skup | Analitička datoteka | Agregatna datoteka | Obavijest |
|---|---|---|---|
| `anketa_mreze` | `anketa-mreze.csv` | `anketa-mreze-agregat.csv` | `anketa-mreze.LICENCA.md` |
| `populacija_medija` | `populacija-medija.csv` | `populacija-medija-agregat.csv` | `populacija-medija.LICENCA.md` |

Snimke piše isključivo `scripts/build-data-snapshots.R` s argumentom
`--write`; bez njega ista skripta samo provjerava poklapaju li se bajtovi s
onim što generator proizvede iz deklariranoga sjemena. Render nikada ne piše u
ovu mapu. Agregatna datoteka uz svaki udio drži brojnik i nazivnik, a uz svaki
prosjek njegov zbroj, pa se svaki redak može provjeriti rukom i u tisku.

Oba izlazna skupa i svaka njihova datotečna snimka nose
[CC BY 4.0 obavijest](LICENCA-generirani-podaci.md), a svaka snimka uz sebe ima
i vlastitu obavijest s izravnom poveznicom na licencu. Kod generatora ostaje
pod MIT licencom repozitorija. Nijedna simulirana brojka ne smije se navesti
kao mjerenje.

Ugrađeni R skupovi `UCBAdmissions` i `anscombe` **nisu** ovdje i ne smiju biti.
Njihova traka je `external-only` jer za same skupove ne postoji obavijest o
redistribuciji: `datasets` pod R 4.6.0 nosi samo oznaku „Part of R 4.6.0”.
Dostupnost kroz lokalnu instalaciju nije dopuštenje.

Podaci koji opisuju pojedince ne ulaze ovamo bez anonimizacije, i ne ulaze u
razgovor s AI asistentom ni tada (Dodatak F).

Puni inventar prava i opreznih traka iz paketa P1B-DATA-LIC nalazi se u
`notes/reports/p1b-data-licence-access-inventory-2026-08-03.md`. Kanonski
strojno čitljiv katalog je `katalog.yml`, a njegov ugovor promocije i granica
prava opisani su u `notes/reports/p3-catalog-2026-08-05.md`.
