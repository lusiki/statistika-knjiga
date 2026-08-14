# WC-C09 — završni izvještaj kritičara statističkih metoda

**Izvor:** `chapters/09-procjena.qmd`

**SHA-256 prije i poslije pregleda:**
`42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`

Kritičar je radio neovisno i samo za čitanje. Nijedna datoteka nije uređena
niti je stvoren artefakt.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 5/5 |
| Pretpostavke | 5/5 |
| Tumačenje | 5/5 |
| Preciznost | 5/5 |

## Snage

- Pokrivenost se najprije doživljava ponavljanjem i brojčano provjerava, a tek
  se zatim imenuju razina pouzdanosti, kritična vrijednost i formula intervala.
- Usporedbe preseta drže isti pseudoslučajni niz: A i B mijenjaju samo razinu
  pouzdanosti, a A i C veličinu uzorka. Statički i interaktivni put zato nose
  istu statističku priču.
- Margina pogreške dosljedno je poluširina intervala i ograničena na
  nesigurnost uzorkovanja; pristranost, neodgovor, pokrivenost, kodiranje i
  mjerenje nisu pogrešno apsorbirani u interval.
- Primjer čitanja vremena rabi unaprijed zadani cilj preciznosti, ne
  neutemeljenu odluku o promjeni, a bootstrap percentilni interval nije
  prikazan kao dokaz vlastite pokrivenosti.
- Preklapanje intervala dobiva samo jezik kompatibilnosti, uz izričit zahtjev
  da se razlika procijeni izravno i uzme u obzir zavisnost nacrta.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

Nema.

## Prethodni blokirajući nalazi

U predfinalnom prolazu kritičari su utvrdili da usporedba preseta ne drži
jedan zajednički niz, da pokrivenost nije dovoljno iskušena prije imenovanja,
da tiskani put ne nosi punu kontroliranu usporedbu te da je radni primjer
prelazio iz cilja preciznosti u neutemeljenu tvrdnju o promjeni. Prije
zaključavanja izvora uvedeni su zajednička matrica izvlačenja, brojčani prikaz
pokrivenosti, parovi A/B i A/C za tisak te unaprijed zadani prag margine od
deset minuta.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **0**
- Korisno poboljšanje: **0**

**Verdikt:** metodološki prolaz za završni panel. Odluka o C09 ostaje
autoru/editoru.
