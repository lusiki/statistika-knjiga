# WC-C07 — završni strukturni pregled

**Izvor:** `chapters/07-vjerojatnost.qmd`

**SHA-256 prije i poslije pregleda:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Pregled je bio neovisan i samo za čitanje; nijedna datoteka nije uređena ni
stvorena. Ratificirana kralježnica bila je fiksna osnova pregleda.

## Ocjene

| Kriterij | Ocjena |
|---|---:|
| Vjernost vinjete | 5/5 |
| Izbor definicija | 5/5 |
| Uvodi u prikaze | 4/5 |
| Pokrivenost zadacima | 5/5 |
| Slijed argumenta | 5/5 |
| Ravnoteža | 5/5 |

## Snage i kostur

Vinjeta, simulacija slučajnih nizova i okvir iz divljine tvore zatvoren luk:
početno pitanje vraća se s jasnijim mjernim problemom bez lažne konačne presude
o vrućoj ruci. Prvo iskustvo prethodi formalizaciji, a widget prethodi
normalnoj raspodjeli i uvjetima CLT-a. Digitalni widget i tiskani blizanac nose
isti središnji argument. Završni sklop povezuje provjere asistenta, jednu
realističnu pogrešku, razrađeni primjer i prijelaz prema uzorkovanju.

Sedmodijelni kostur ostaje cjelovit i u propisanom redoslijedu: vinjeta,
izgradnja pojma, interakcija i statički blizanac, statistika u divljini,
pitajte model s jednom pogreškom, razrađeni primjer te sažetak, pojmovi i četiri
razine zadataka. Nema dodatnoga dijela izvan kostura.

Poglavlje ima 11 odjeljaka H2: osam sadržajnih i tri završna. Sažetak je jedan
neprekinuti odlomak od pet rečenica. Pet definicijskih blokova odgovara
ratificiranoj karti: vjerojatnost, neovisnost, uvjetna vjerojatnost, binomna i
normalna raspodjela.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

- **Retci 371–374 nasuprot kontrolama 382–398 i koracima 558–563.** Uvod kaže
  da prikaz drži zadanu vjerojatnost nepromijenjenom i mijenja samo duljinu
  niza, premda widget dopušta promjenu scenarija, vjerojatnosti i broja
  ponavljanja, a treći korak mijenja scenarij i vjerojatnost. Tvrdnju bi trebalo
  omeđiti na prvu usporedbu ili izrijekom razlikovati središnju usporedbu od
  dodatnih kontrola.

### Korisno poboljšanje

- **Retci 932–939.** Konceptualni zadatak spaja poznatu nasuprot nepoznatoj
  vjerojatnosti s normalnošću i QQ prikazom. Pokrivenost je dobra, ali isti bi
  sadržaj bio pregledniji kao podzadaci (a) i (b).

## Dispozicija upravljanih stavki

- `R10-C07-degree-belief` — prolazi.
- `R29-C07-retrieval-load` — prolazi; stanka je nakon četvrtoga od osam
  sadržajnih odjeljaka, na stvarnom strukturnom središtu.
- `R35-REACHBACK-07` — prolazi; zadatak zahtijeva brojnosti i svih šest
  revizijskih pitanja iz poglavlja 3 te ima kanonsko zatvaranje.

Administrativno prihvaćanje tih stavki ostaje nadležnost autora na C07.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **1**
- Korisno poboljšanje: **1**

**Verdikt:** strukturni prolaz; nema neriješenoga fatalnog ni velikog nalaza.
