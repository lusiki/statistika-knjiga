# Specifikacija AI izvoza

Zašto knjiga izvozi samu sebe u čisti tekst, što točno nastaje i kako se
održava.

## Zašto

Knjiga pretpostavlja da svaki čitatelj ima asistenta. Ako mu ne damo tekst,
asistent će na pitanja o knjizi odgovarati iz općeg znanja, često pogrešno i
uvijek samouvjereno. Izvoz to okreće: čitatelj asistentu priloži poglavlje, a
asistent odgovara iz knjige. Ista datoteka služi i tražilicama i alatima koji
čitaju `llms.txt`.

Izvoz je ujedno i najjeftiniji oblik ugrađenog tutora (otvorena odluka 6 u
[struktura-knjige.md](struktura-knjige.md)). Prije nego se razmatra pravi
razgovorni tutor s API-jem, hostingom i pregledom privatnosti, vrijedi vidjeti
koliko od te vrijednosti isporučuje sam izvoz.

## Što nastaje

Generira `R/build-ai-exports.R`, koji se izvršava kao Quarto `pre-render` hook
pri svakom renderu i može se pokrenuti ručno.

| Datoteka | Sadržaj |
|----------|---------|
| `docs/ai/<poglavlje>.md` | jedno poglavlje kao čisti tekst, s kratkim zaglavljem |
| `docs/ai/dio-N.md` | paket svih poglavlja jednog dijela knjige |
| `docs/llms-full.txt` | cijela knjiga u jednoj datoteci |
| `docs/llms.txt` | karta izvoza po konvenciji llmstxt.org |
| `data/ai-exports.json` | manifest koji čita `uci-s-ai.qmd` |

## Što se izbacuje, a što ostaje

Izbacuje se YAML, blokovi koda `{r}` i `{ojs}`, upravljačke ploče i statički
blizanci grafova (sve unutar `when-format="pdf"`).

Ostaje proza, naslovi, tablice, formule, definicijski divovi i sadržaj
pedagoških kutija. Kutije zadržavaju svoju oznaku kao podebljani uvod
(**Vinjeta.**, **Statistika u divljini.**, **Pitajte model.**, **Nađite
grešku.**), pa asistent zna da čita primjer, a ne argument.

Citati `[@kljuc]` razrješavaju se u „Prezime, godina" iz `references.bib`.
Unutarknjižne reference `@def-…` razrješavaju se u sam pojam, a `@fig-…` i
`@tbl-…` u riječ „slika" odnosno „tablica". Bilješke se skupljaju na kraj.

## Mentorska uputa

Manifest nosi dvije inačice upute. Puna živi na stranici „Uči uz AI" i sadrži
pravila o utemeljenosti, računanju i privatnosti. Kratka ide u URL dubokih
poveznica, pa mora ostati kratka.

**Kratka uputa postoji na dva mjesta** i mora biti ista: `promptShort` u
`R/build-ai-exports.R` i konstanta `UPUTA` u `styles/book-include.html`. Kad se
mijenja jedna, mijenja se i druga.

## Održavanje

Skripta čita redoslijed poglavlja iz `_quarto.yml`, pa dodavanje poglavlja ne
traži nikakvu izmjenu. Mijenjaju se samo konstante na vrhu skripte (adresa,
naslov, opis, autori, licenca) i oznake kutija ako se kostur poglavlja
promijeni.

Cijeli posao je u `tryCatch`-u i nikad ne ruši render. Ako paketi nedostaju,
izvoz se preskoči, a posluže već urezane datoteke.

## Licenca izvoza

P1B-NAVARRO razriješio je odluku 5 uklanjanjem svih materijalnih ovisnosti o
Navarrovu tekstu. `LICENSE_LINE` zato u zaglavlju svake izvezene datoteke
navodi MIT i povezuje puni tekst licence. Skupovi podataka i drugi materijali
trećih strana ne prelaze u taj režim.
