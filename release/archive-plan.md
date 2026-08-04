# Plan arhiviranja izdanja

Ovaj dokument opisuje budući postupak. Nije arhivski polog, ne dodjeljuje
trajni identifikator i ne daje ovlast za vanjsku radnju.

- Odgovorna osoba za arhiviranje: Luka Sikic.
- Trenutačno stanje: plan je spreman, polog nije dopušten.
- Izvršni uvjet: neposredna i točno ograničena ovlast `G-A6-ARCHIVE`.
- Ulaz: prihvaćeni kandidat za izdanje, konačni metapodaci i točno odobrena
  oznaka izdanja.
- Još neodređena polja: arhivska usluga, trajni identifikator i datum pologa.

Kad uvjet bude ispunjen, vlasnik plana provjerava da oznaka pokazuje na točno
prihvaćeni commit, polaže upravo tu oznaku, uspoređuje kontrolni zbroj pologa s
izvornim stanjem i upisuje trajni identifikator u središnji zapis,
čitateljski citat i kolofon. Svaka od tih radnji ostaje zasebno dokaziva.

Neuspješan ili nepotpun polog ne mijenja stanje u `archived`. Nova verzija
nakon pologa dobiva novu oznaku i novi arhivski zapis; postojeći se polog ne
prepisuje.
