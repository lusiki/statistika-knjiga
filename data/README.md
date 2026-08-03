# data/

Ova mapa prima samo licenčno provjerene podatkovne pakete u traci `bundled` i
tri metapodatkovna artefakta knjige. Mrežni pristup datoteci nije dovoljan za
njezino spremanje ili redistribuciju.

| Datoteka | Podrijetlo | Urezuje se? |
|----------|-----------|-------------|
| `ai-exports.json` | generira `R/build-ai-exports.R` pri svakom renderu | da (sjemenska prazna inačica je već tu) |
| `concept-graph.json` | generira `R/build-concept-graph.R`, ručno | da |
| `widgets.json` | održava se ručno; jedini popis widgeta | da |
| ostalo | dohvaća `R/fetch-podaci.R` samo iz provjerenih izvora | da, samo uz izričito provjerenu redistribuciju i traku `bundled` |

JSON datoteke iz tablice nisu nastavni skupovi podataka. Svaki nastavni paket
mora imati zapis o izvoru, inačici, licenci, atribuciji, pristupu,
redistribuciji, jednoj traci i zakonitoj zamjeni za svaki obvezni studentski
put. Skup bez tog zapisa ne smije se koristiti u poglavlju. Paketi u trakama
`portal-mediated` i `external-only` ne pohranjuju se u ovoj mapi.

Simulirani nastavni skupovi ne stoje ovdje kao datoteke. Generator je
`R/podaci-nastavni.R`, poziva ga `R/setup.R`, a skupovi `anketa_mreze` i
`populacija_medija` time su dostupni svakom poglavlju. Oba izlazna skupa i
svaka njihova buduća datotečna snimka nose [CC BY 4.0 obavijest](LICENCA-generirani-podaci.md).
Kod generatora ostaje pod MIT licencom repozitorija. Nijedna simulirana brojka
ne smije se navesti kao mjerenje.

Podaci koji opisuju pojedince ne ulaze ovamo bez anonimizacije, i ne ulaze u
razgovor s AI asistentom ni tada (Dodatak F).

Puni inventar prava i opreznih traka iz paketa P1B-DATA-LIC nalazi se u
`notes/reports/p1b-data-licence-access-inventory-2026-08-03.md`. Kanonski
strojno čitljiv katalog nastaje tek u paketu P3-CATALOG.
