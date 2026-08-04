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
pri svakom renderu i može se pokrenuti ručno. Lokalni hook ostaje best-effort,
a objavni put uvijek poziva `--release` i zato završava nenultim statusom pri
svakoj pogrešci.

| Datoteka | Sadržaj |
|----------|---------|
| `docs/ai/<poglavlje>.md` | jedno poglavlje kao čisti tekst, s kratkim zaglavljem |
| `docs/ai/dio-N.md` | paket svih poglavlja jednog dijela knjige |
| `docs/llms-full.txt` | cijela knjiga u jednoj datoteci |
| `docs/llms.txt` | karta izvoza po konvenciji llmstxt.org |
| `data/ai-exports.json` | manifest koji čita `uci-s-ai.qmd` |

## Što se izbacuje, a što ostaje

Izbacuje se YAML, blokovi koda `{r}` i `{ojs}`, upravljačke ploče i statički
blizanci grafova (sve unutar `when-format="pdf"`). Izbacuje se i sav sadržaj
unutar `content-visible when-profile="…"`. To je strukturno pravilo javnoga
izvoza, pa se ne oslanja na popis riječi poput „rješenje” ili „rubrika”.

Trenutačni obuhvat izvoza čine poglavlja 00–18 iz `book.chapters` u
`_quarto.yml`; dodaci i druge stranice nisu ulaz. Release audit ipak pregledava
i profilne blokove u `dodaci/`, kako sadržaj nastavničke rute ne bi neopaženo
ušao u izlaz ako se obuhvat poslije proširi. Budući D06 sustav rješenja ostaje
u svojem kasnijem paketu, ali mora zadržati jednu od dviju sigurnih granica:
odvojenu rutu izvan ulaza javnoga AI izvoza ili profilni `content-visible` blok
koji ovaj izvoz obvezno odbacuje.

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
traži nikakvu izmjenu. Naslov i predobjavno stanje dolaze iz
`release/governance.yml`; autorstvo, opis i mrežna adresa dolaze iz datoteke
koju njegov `book.authorship_source` navodi. Release način prekida izvoz ako
se kanonski radni naslov i naslov u tom izvoru raziđu. Oznake kutija mijenjaju
se samo ako se kostur poglavlja promijeni.

Za lokalni render cijeli je posao u `tryCatch`-u. Ako paketi nedostaju, izvoz
se preskoči, a posluže već urezane datoteke. Objavni workflow zasebno poziva

```text
python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-ai-exports.R --release
```

zatim renderira knjigu i nakon rendera poziva `--release --validate-only`.
Lokalni pre-render između tih dviju blokirajućih provjera ne može pretvoriti
release pogrešku u uspjeh. Pogreška izgradnje, profilni sadržaj u javnom izlazu
ili metapodatkovni nesklad blokiraju objavu. Skripta
`scripts/check-ai-export-fixtures.py` bez objavljivanja dokazuje pozitivan put
i namjerne kvarove za sve tri granice.

## Licenca izvoza

P1B-NAVARRO razriješio je odluku 5 uklanjanjem svih materijalnih ovisnosti o
Navarrovu tekstu. `LICENSE_LINE` zato u zaglavlju svake izvezene datoteke
navodi MIT i povezuje puni tekst licence. Skupovi podataka i drugi materijali
trećih strana ne prelaze u taj režim.
