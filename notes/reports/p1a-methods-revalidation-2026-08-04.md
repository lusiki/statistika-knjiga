---
packet: P1A-METHODS
date: "2026-08-04"
source_state: "commit:89229759ed61ce3a3bced127496b731dfdd7cf73"
source_tree: "tree:59bbab72e2a10ea8bbd9fc5d9e95cd724a423568"
revalidates: "commit:7832b07ee92e98a962fc79b291389118e95f29b6"
status: passed
---

# P1A-METHODS — revalidacija agregatnog gatea

## Ovlast, opseg i izvor

Autor Luka Sikic 4. kolovoza 2026. odobrio je evidence-only ponovno otvaranje
`P1A-C02` i `P1A-METHODS`, bez izmjene proze. Ovaj gate ponovno provjerava
samo izvorni nesklad koji je otkrio `P1-VERIFY`; ne otvara druge prihvaćene
korekcije i ne počinje `G-A2a`.

Jedinstveno dokazno stanje je commit
`89229759ed61ce3a3bced127496b731dfdd7cf73` i tree
`59bbab72e2a10ea8bbd9fc5d9e95cd724a423568`. Jedina razlika među dvanaest
izvornih P1A chapter blobova jest odobrena kasnija promjena Poglavlja 2. Svih
ostalih jedanaest blobova jednako je izvornom agregatu na commitu `7832b07`.

## Revalidacijska matrica {#revalidation-matrix}

| Preduvjet | Numerički primitak | Neovisno čitanje | Trenutačni blob | Revalidacijski nalaz |
|---|---|---|---|---|
| `P1A-C02` | PASS — osam R/OJS blokova izvan je kasnijega diffa | PASS — novi `critic_methods` primitak, 5/5 u sve četiri dimenzije, bez nalaza | `908780ee6fdb` | PASS — `p1a-c02-methods-revalidation-2026-08-04.md` |
| `P1A-C06` | PASS | PASS | `c3177eb7cc5a` | PASS — blob nepromijenjen |
| `P1A-C07` | PASS | PASS | `8deb7a2b6867` | PASS — blob nepromijenjen |
| `P1A-C08` | PASS | PASS | `b9a435a2ebb1` | PASS — blob nepromijenjen |
| `P1A-C09` | PASS | PASS | `67380c04d31d` | PASS — blob nepromijenjen |
| `P1A-C10` | PASS | PASS | `a90549950c4f` | PASS — blob nepromijenjen |
| `P1A-C11` | PASS | PASS | `2aaede845c2a` | PASS — blob nepromijenjen |
| `P1A-C13` | PASS | PASS | `9242e057c660` | PASS — blob nepromijenjen |
| `P1A-C14` | PASS | PASS | `449c88f25e03` | PASS — blob nepromijenjen |
| `P1A-C15` | PASS | PASS | `0eadfd02627a` | PASS — blob nepromijenjen |
| `P1A-C16` | PASS | PASS | `ba93f9a62965` | PASS — blob nepromijenjen |
| `P1A-C18` | PASS | PASS | `f291e6317389` | PASS — blob nepromijenjen |

Izvorna matrica i dalje nosi 36/36 strukturiranih required-evidence primitaka,
24/24 output primitka i 36/36 prolaznih izlaznih testova. Za `P1A-C02` je
stari exact-source critic primitak zamijenjen novim primitkom na blobu
`908780ee…`; njegov byte-identični računski izvor čuva numerički primitak. Za
ostalih jedanaest redaka izvor, izvještaj, primitci i packet review ostaju
identični.

## Točan popis blokatora {#exact-blocker-list}

Nerazriješenih blokatora nema. Prethodni blokator bio je samo izvorni nesklad
`P1A-C02`: izvještaj je dokazivao `ccae632a…`, a živi chapter blob bio je
`908780ee…`. Novi neovisni methods primitak, novi durable report te ažurirani
strukturirani primitci sada su vezani uz `908780ee…`.

`R09-C15-variance-ratio` i sva druga kasnija poglavna zaduženja ostaju izvan
ovoga gatea i nisu proglašena završenima.

## Izlazni nalaz i budući učinci

Sva tri `P1A-METHODS` izlazna testa ponovno prolaze. Nijedan nedostatak nije
skriven agregacijom, matrica je vezana uz jedan commit i tree, a ovaj izvještaj
dokazuje revalidacijski opseg umjesto generičkoga ugovora.

Nema novoga downstream učinka. Postojeće ovisnosti već vode `P1A-METHODS` u
`P1-VERIFY`; ovaj primitak samo razrješava njegovu točno zabilježenu blokadu.
Nije promijenjeno nijedno poglavlje, implementacija, inventar, lock, generirani
artefakt ili release metapodatak.
