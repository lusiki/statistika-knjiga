# Obavijest uz izvadak skupa `eurostat_drustvo`

Ova obavijest putuje uz datoteku `eurostat-drustvo-2025.csv` i mora ostati uz
nju pri svakom dijeljenju, preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `eurostat_drustvo` |
| Izvor | Eurostat, šest imenovanih skupova podataka |
| Referentna godina | 2025. |
| Geografija | 27 država članica Europske unije |
| Datum pristupa | 10. kolovoza 2026. |
| Uvjeti ponovne uporabe | [Eurostat — Copyright notice and free re-use of data](https://ec.europa.eu/eurostat/help/copyright-notice) |
| Izvadak izradio | `scripts/build-eurostat-extracts.py` |

## Atribucija po komponenti

- Source: [Eurostat dataset lfsi_emp_a](https://ec.europa.eu/eurostat/databrowser/view/lfsi_emp_a/default/table?lang=en), 10 August 2026.
- Source: [Eurostat dataset ilc_peps01n](https://ec.europa.eu/eurostat/databrowser/view/ilc_peps01n/default/table?lang=en), 10 August 2026.
- Source: [Eurostat dataset sdg_04_20](https://ec.europa.eu/eurostat/databrowser/view/sdg_04_20/default/table?lang=en), 10 August 2026.
- Source: [Eurostat dataset edat_lfse_14](https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_14/default/table?lang=en), 10 August 2026.
- Source: [Eurostat dataset isoc_ci_ifp_iu](https://ec.europa.eu/eurostat/databrowser/view/isoc_ci_ifp_iu/default/table?lang=en), 10 August 2026.
- Source: [Eurostat dataset demo_pjanind](https://ec.europa.eu/eurostat/databrowser/view/demo_pjanind/default/table?lang=en), 10 August 2026.

## Oznaka izmjena i disclaimer

Modified teaching extract: selection of 2025 and EU-27, joining of six
datasets, Croatian labels and column layout are changes made by the authors.

The European Commission is not liable for any consequence stemming from the
reuse of this publication.

Promjene su ograničene na odabir jedne godine i 27 država, spajanje šest
tablica u dugi raspored, dodavanje hrvatskih oznaka i razdvajanje izvornoga API
statusa na nastavne stupce `obs_status` i `conf_status`. Brojčane vrijednosti
nisu preračunate ni zaokružene. Točan API status ostaje u `status_api`, a
izvorni JSON odgovori ostaju neizmijenjeni u `data/eurostat_drustvo/raw/`.

## Granica sadržaja trećih strana

Spremljeni odgovori nose agencijsku oznaku `ESTAT`, a u metapodacima svih šest
tablica `SOURCE_INSTITUTIONS` glasi `Eurostat`. Nijedan odgovor ne nosi zasebnu
copyright, licence ili third-party napomenu. Izvadak obuhvaća samo države
članice EU-a, nije trgovinska tablica i ne prenosi publikacije, fotografije,
ilustracije, logotipe ni zaštitne znakove. Ako buduća verzija izvora uvede
suprotnu pojedinačnu napomenu, ovaj se izvadak ne smije osvježiti pod ovom
dispozicijom.

Knjiga nije tražila ni dobila dopuštenje nositelja prava i ne tvrdi da jest.
Ponovna se uporaba oslanja samo na objavljene Eurostatove uvjete navedene gore.
