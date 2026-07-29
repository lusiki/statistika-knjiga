# data/

Skupovi podataka koje knjiga koristi, plus dvije generirane datoteke.

| Datoteka | Podrijetlo | Urezuje se? |
|----------|-----------|-------------|
| `ai-exports.json` | generira `R/build-ai-exports.R` pri svakom renderu | da (sjemenska prazna inačica je već tu) |
| `concept-graph.json` | generira `R/build-concept-graph.R`, ručno | da |
| `widgets.json` | održava se ručno; jedini popis widgeta | da |
| ostalo | dohvaća `R/fetch-podaci.R` iz javnih izvora | da, ako licenca dopušta |

Svaki skup podataka mora imati unos u Dodatku C (izvor, licenca, varijable,
putanja). Skup bez tog unosa ne smije se koristiti u poglavlju.

Podaci koji opisuju pojedince ne ulaze ovamo bez anonimizacije, i ne ulaze u
razgovor s AI asistentom ni tada (Dodatak F).
