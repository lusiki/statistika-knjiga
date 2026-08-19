# Kodna knjiga — `parlament_oznake.csv`

| Stupac | Značenje |
|---|---|
| `record_id` | Stabilni izvedeni ključ: izvorna uloga datoteke i izvorni redni broj retka. |
| `sentence_text` | Izvorni tekst označene rečenice, bez jezične ili sadržajne izmjene. |
| `country_source` | Doslovna izvorna zemlja; u ovom izvatku uvijek `HR`. |
| `source_role` | `train_file` ili `test_file`; navodi iz koje je službene JSONL datoteke redak došao. |
| `source_line` | Redni broj retka u izvornoj datoteci, počevši od 1. |
| `source_document_id` | Izvorni unutarnji ključ dokumenta; služi isključivo grupiranom razdvajanju. |
| `source_sentence_id` | Izvorni unutarnji ključ rečenice. |
| `source_split` | Izvorno polje `split` iz datoteke za učenje; za ispitnu datoteku `nije_dostupno_iz_izvora`. |
| `derived_split` | `ucenje`, `provjera` ili `ispitivanje`, prema pravilu iz putovnice. |
| `annotator1_raw` | Doslovna oznaka prvoga, odnosno jedinoga izvornog kodera. |
| `annotator2_raw` | Doslovna oznaka drugoga kodera; u ispitnoj datoteci `nije_dostupno_iz_izvora`. |
| `reconciliation_raw` | Doslovna usklađena oznaka; u ispitnoj datoteci `nije_dostupno_iz_izvora`. |
| `recorded_label` | Izvorna trostupanjska zabilježena oznaka: `Negative`, `Neutral` ili `Positive`. |
| `label_path` | `dva_kodera_i_uskladjenje` ili `jedan_uvjezbani_koder`. |

`nije_dostupno_iz_izvora` nije prazan tekst, nula ni slaganje kodera. To je
izričit znak da izvorna ispitna datoteka to polje ne pruža.
