# WC-C07 — završni skeptički pregled

**Izvor:** `chapters/07-vjerojatnost.qmd`

**SHA-256 prije i poslije pregleda:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Pregled je bio neovisan i samo za čitanje; nijedna datoteka nije uređena ni
stvorena.

## Ocjene

- pokrivenost osporavanja: **5/5**
- poštenje prema drugim pogledima: **5/5**
- normativna iskrenost: **4/5**

## Snage

1. Modelna vjerojatnost, osobna sigurnost i dugoročna frekvencijska provjera
   jasno su odvojene. Kalibracija je konkretno objašnjena skupom usporedivih
   prognoza, bez uvođenja pune Bayesovske inferencije.
2. Neovisnost je sadržajna pretpostavka vezana uz proces i dizajn. Podaci mogu
   otkriti kršenje, ali ga izostanak razlike ne potvrđuje. Viralnost je
   operacionalizirana pragom, razdobljem i izloženošću.
3. Tekst razlikuje raspodjelu pojedinačnih vrijednosti od raspodjele stopa ili
   prosjeka, omeđuje CLT i priznaje da isključenje nula i promjena ljestvice
   mijenjaju populaciju i istraživačko pitanje.
4. Fiksni neovisni proces samo je nulti model vruće ruke, simulacijska i
   analitička podudarnost samo je interna provjera, a rijedak ishod jednoruke
   kampanje ne identificira naslov kao uzrok.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

1. **Retci 169–182, završno pitanje vinjete.** Izraz „ono što slučajnost
   proizvodi bez ijednog razloga” može sugerirati da je slučajni ishod
   ontološki bez uzroka. Preciznije bi bilo „ono što slučajnost proizvodi bez
   sustavne promjene procesa” ili ekvivalentna modelno uvjetovana formulacija.
2. **Retci 669–675.** Tvrdnja da su odstupanja „dovoljno mala da orijentacija
   ostane upotrebljiva” ne imenuje svrhu ni dio raspodjele. Korisnost bi trebalo
   omeđiti na grubu orijentaciju u središnjem dijelu, ne na repove ili pragove
   odluke.

### Korisno poboljšanje

- **Retci 785–788.** Usporedba simulacijskoga pomaka od približno četiri
  postotna boda s razlikom koju bi „netko tražio” ostavlja sadržajni prag
  neimenovanim. Relevantnu minimalnu razliku trebalo bi odrediti prije gledanja
  rezultata; ovdje je dostatno reći da pristranost može biti usporediva s
  učinkom koji se istražuje.

## Upravljane dispozicije

- `R10-C07-degree-belief` — zadovoljeno.
- `R29-C07-retrieval-load` — zadovoljeno; stanka zauzima približno 49,3 %
  čitateljske proze prije nje.
- `R35-REACHBACK-07` — zadovoljeno; zadatak traži brojnosti i svih šest
  revizijskih pitanja iz poglavlja 3 te ima kanonsko zatvaranje.
- Granica vruće ruke — zadovoljena: nulti model, promjenjivi proces, težina
  šuta, obrana i selekcija pokušaja ostaju razdvojeni.
- Granica kampanje — zadovoljena: widget prikazuje jednu kampanju pod zadanim
  modelom i ne nosi lažni A/B naziv.
- Uzročna i odlukovna granica — zadovoljena: primjer odbija pripisivanje ishoda
  naslovu bez nasumične usporedbe te odvaja statističku neobičnost od ciljeva
  i troškova odluke.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **2**
- Korisno poboljšanje: **1**

**Verdikt:** skeptički prolaz. Otvoreni lokalni nalazi nisu blokirajući, a
odluka o C07 ostaje autoru/editoru.
