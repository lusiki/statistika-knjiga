# WD-C13 — strukturni kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom:

- očekivani i opaženi SHA-256:
  `6cd97e3dae0a83dcf3daa8f7450fac0324390ef14b7df87308a29a6caa240015`
- podudaranje: da
- status kralježnice: ratificirana

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Vjernost otvarača | 5/5 |
| Izbor definicija | 5/5 |
| Uvodi u figure | 5/5 |
| Pokrivenost zadacima | 5/5 |

## Snage

- Vinjeta o Berkeleyju vjerno postavlja stvaran slučaj, ne rješava ga unaprijed
  i završava pitanjem postoji li veza, gdje je i koliko je snažna.
- Otvaranje Dijela V nastavlja ugovor reformirane prakse, a hi-kvadrat,
  reziduali, Cramérovo V i Fisherov postupak razdvojeni su kao različita pitanja
  o istoj tablici.
- Pet definicijskih blokova čuva najnosivije tehničke objekte. Uvjetni nazivnik
  opravdano ostaje prozna definicija: primijenjen je na retke i stupce, ponovljen
  u AI-provjeri, sažetku i pojmovima te prenesen prema poglavlju 17.
- Lokalna simulirana i neobvezna ESS ruta razdvojene su; kodirani tekst imenuje
  jedinicu, vlasnika kategorija, podobnost za nazivnik te nekodirane i višestruko
  kodirane jedinice. Kritički zadatak valjano dohvaća Simpsonov paradoks.

## Nalaz

**Major — nevjeran statički blizanac widgeta.** Interaktivni prikaz mijenja
relativni pomak i veličinu rubnih zbrojeva te prikazuje ukupni hi-kvadrat i
Cramérovo V. Statički blizanac drži očekivanu frekvenciju na 40 i mijenja samo
pomak, pa ne pokazuje ključni zaključak da isti relativni pomak daje različit
doprinos u malim i velikim ćelijama. Izostaje i odnos hi-kvadrata i V.

Statički prikaz treba dobiti početni panel bez odstupanja i barem dva panela s
jednakim relativnim pomakom, ali različitim rubnim zbrojevima. Oznaka panela ili
sam prikaz treba navesti ukupni hi-kvadrat i Cramérovo V, tako da su oba
upravljačka argumenta vidljiva bez interakcije.

## Presuda

Poglavlje je vjerno ratificiranoj kralježnici i trima stavkama WD-C13, ali
strukturni prolaz ovisi o vjernijem statičkom blizancu.

## Završni ponovni pregled nakon odobrene dorade

Ponovni read-only pregled cijeloga izvora, kralježnice i konvencija potvrdio je
SHA-256 `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`.
Svih osam odobrenih dorada prolazi, a statički blizanac sada pokazuje dva ista
relativna pomaka uz različite rubne zbrojeve, rast hi-kvadrata i stabilni
`V = 0,20`.

| Dimenzija | Ocjena |
|---|---:|
| Vjernost otvarača | 5/5 |
| Odabir definicija | 5/5 |
| Uvodi u figure | 5/5 |
| Pokrivenost zadacima | 5/5 |

### Snage

- Vinjeta ostaje stvarni Berkeleyjev problem i završava pitanjem poglavlja.
- Pet formalnih definicija dobro je odmjereno; uvjetni nazivnik ostaje dovoljno
  jasno definiran u prozi bez neopravdanoga šestog bloka.
- Widget i statički blizanac sada nose isti argument, a kodirani tekst i
  Simpsonov reach-back ostaju strukturno čisti.

### Preostali nalazi

Nema strukturnoga nalaza.

### Završna presuda

Nema fatalnoga ni major nalaza. Konačni izvor potpuno prolazi strukturni
ponovni pregled.
