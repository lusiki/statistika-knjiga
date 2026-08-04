---
packet: P1A-C02
date: "2026-08-04"
source_state: "chapter:sha1-908780ee6fdb2916afb1b1226bb3c9f567a81ce2"
revalidates: "chapter:sha1-ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00"
status: passed
---

# P1A-C02 — revalidacija metodološkog dokaza

## Ovlast i ograničeni opseg

Autor Luka Sikic 4. kolovoza 2026. izričito je odobrio ponovno otvaranje
`P1A-C02` i `P1A-METHODS` samo radi revalidacije trenutačnoga bloba Poglavlja
2, bez izmjene proze. Ovaj zapis ne ponavlja korekcijski paket, ne mijenja
rukopis i ne otvara kasnije stavke Poglavlja 2.

Provjera je provedena na commitu
`89229759ed61ce3a3bced127496b731dfdd7cf73`, stablu
`59bbab72e2a10ea8bbd9fc5d9e95cd724a423568` i bloba
`908780ee6fdb2916afb1b1226bb3c9f567a81ce2`. Kritičar je prije i nakon
čitanja dobio isti blob; poglavlje nema radnu razliku.

## Promjena nakon izvornoga primitka

Usporedba s izvornim prihvaćenim blobom
`ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00` pokazuje samo:

- proširenu internu bilješku o P1B-NAVARRO provjeri; i
- uklanjanje dviju rečenica koje su Navarru pripisivale naziv problema treće
  varijable i opći zaključak da povezanost ne dokazuje uzročnost.

Definicija konfundera, primjer triju mogućih smjerova, razlika između obrnutog
smjera, pristranosti odabira i zajedničkog uzroka te razlika između konfundera,
posrednika i kolajdera ostali su netaknuti i samodostatni. Svih osam R/OJS
blokova nalazi se izvan diffa, pa izvorni numerički primitak i reproducirane
vrijednosti ostaju vezani uz byte-identičan računski izvor. Nije promijenjen
widget, statični blizanac, konstruirani skup, formula, sjeme ili prikazana
vrijednost.

## Neovisno metodološko čitanje {#neovisno-metodolosko-citanje}

Neovisni read-only `critic_methods` pročitao je cijelo trenutačno poglavlje,
izvorni `P1A-C02` izvještaj, nacrt knjige i checkout-localnu kralježnicu. Prazan
i neratificiran zapis kralježnice nije upotrijebljen kao dokaz ispravnosti.

Ocjene su:

| Dimenzija | Ocjena |
|---|---:|
| Korektnost | 5/5 |
| Pretpostavke | 5/5 |
| Tumačenje | 5/5 |
| Preciznost | 5/5 |

Kritičar je zasebno potvrdio sva četiri registrirana područja:

- nasumična dodjela daje ravnotežu u očekivanju, ne jamstvo u jednoj
  realizaciji, a učinak dodjele ili ponude odvojen je od učinka primljenog
  tretmana;
- negativna povezanost stavke s ostatkom instrumenta ostaje dijagnostika uz
  obrnuto kodiranje, višedimenzionalnost, prijevod, formulaciju i nepažljivo
  odgovaranje kao moguća objašnjenja;
- Stevensove razine ostaju povijesno utjecajan i praktičan opis informacije,
  a ne bezvremenska tablica dopuštenih analiza; i
- konfunder je prethodni zajednički uzrok, odvojen od posrednika i kolajdera,
  bez preporuke automatske prilagodbe za sve dostupne varijable.

Popis nalaza je prazan: nema fatalnog, velikog ni manjeg nalaza. Brisanje
Navarrove rečenice uklonilo je nepouzdanu atribuciju, ali nije stvorilo
metodološku prazninu.

## Izlazni nalaz

Sva tri izlazna testa `P1A-C02` ponovno prolaze. Ispravci i njihovi zavisni
rezultati ostaju reproducibilni jer se računski izvor nije promijenio;
neovisni metodološki dokaz sada je vezan uz trenutačni blob; a opseg je dokazan
ovim packet-specifičnim primitkom i izričitom autorskom ovlašću.

Nije promijenjena proza ni bilo koja implementacijska datoteka. Revalidacija
ne otkriva novi budući učinak; njezina jedina posljedica jest uklanjanje točno
zabilježenoga `P1A-C02` izvornog nesklada u `P1A-METHODS` i `P1-VERIFY`.
