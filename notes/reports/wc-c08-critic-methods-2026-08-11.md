# WC-C08 — završni izvještaj kritičara statističkih metoda

**Izvor:** `chapters/08-uzorkovanje.qmd`

**SHA-256 prije i poslije pregleda:**
`9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04`

Kritičar je radio neovisno i samo za čitanje. Nijedna datoteka nije uređena
niti je stvoren artefakt.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 4/5 |
| Pretpostavke | 5/5 |
| Tumačenje | 4/5 |
| Preciznost | 4/5 |

## Snage

- Simulacija ponovljenih jednostavnih slučajnih uzoraka prethodi standardnoj
  pogrešci i središnjem graničnom teoremu; pojedinačni podaci, procjene i
  raspodjela uzorkovanja ostaju razdvojeni.
- Tekst točno navodi da deseterostruko veći `n` smanjuje standardnu pogrešku
  za faktor `sqrt(10)`, a za prepolovljavanje standardne pogreške treba
  učetverostručiti `n`.
- Sintetička tablica ima poznate vjerojatnosti uključivanja i reproducira
  `3/6 = 50,0 %` bez težina te `6/16 = 37,5 %` s inverznim težinama. Tekst
  izrijekom kaže da je ponderirani udio i dalje procjena te da težine ne
  uklanjaju pogrešku uzorkovanja.
- Granice kalibracije, neodgovora, pokrivenosti, grupiranja, učinka nacrta i
  efektivne veličine uzorka odgovaraju razini statističke pismenosti bez
  izvođenja formule varijance.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

1. U objašnjenju sintetičke tablice rečenica da bi razlika između procjene i
   populacijskoga udjela „i dalje postojala” uz drugi uzorak zvuči
   kategoričnije nego što dopušta slučajnost. Drugi uzorak može slučajno dati
   i nultu razliku; preciznije bi bilo reći da mogućnost razlike ostaje.
2. Widget prikazuje jednu fiksnu populacijsku realizaciju, dok novi nizovi
   nastaju generatorom s istom referentnom sredinom. Ta je namjera čitljiva,
   ali bi jedna kratka rečenica mogla jasnije razlikovati prikazanu konačnu
   populaciju od generativnoga modela ponavljanja.

## Prethodni blokirajući nalaz

U predfinalnom prolazu otkrivena je pogrešna tvrdnja da deseterostruko veći
uzorak prepolovljuje standardnu pogrešku. Ispravljena je prije zaključavanja
izvora; završni panel pregledao je samo gore navedeni hash i potvrđuje točan
odnos korijena iz `n`.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **2**
- Korisno poboljšanje: **0**

**Verdikt:** metodološki prolaz za završni panel. Odluka o C08 ostaje
autoru/editoru.
