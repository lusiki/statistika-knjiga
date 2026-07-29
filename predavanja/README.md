# predavanja/

Reveal.js prezentacije za nastavu. Prate poglavlja, ali ih ne ponavljaju: deck
nosi ono što se na satu pokazuje uživo, prije svega interaktivni graf
poglavlja, a proza ostaje u knjizi.

## Model isporuke

Prezentacije **nisu** dio knjige u smislu `_quarto.yml` `book.chapters`. Svaki
deck je samostalan dokument koji se renderira zasebno, a rezultat se u knjigu
uvlači kao resurs.

1. Izvor je `_-prefiksiran` (`_01-zasto-statistika.qmd`), pa ga Quarto ne
   pokupi pri renderu knjige.
2. Deck se renderira ručno:
   `quarto render predavanja/_01-zasto-statistika.qmd --to revealjs`
3. Nastali `.html` se **urezuje** (commit) i dodaje u `resources:` u
   `_quarto.yml`, pa se pri svakom renderu knjige kopira u `docs/predavanja/`.
4. Kartica se dodaje u `predavanja.qmd`.

Razlog za taj zaobilazni put je što reveal.js i knjiga imaju nespojive
postavke formata, a decka je premalo da opravdaju vlastiti profil.

## Tema

`predavanja/theme.scss` čita iste tokene kao knjiga. Ne upisujte boje u deck.

## Kostur decka

Vinjeta, jedan pojam, widget uživo, jedan slučaj iz divljine, pitanje za
raspravu. Deck koji ima više od dvadeset slajdova radi posao poglavlja, ne
predavanja.
