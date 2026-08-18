# Autorski amandman za niz C15 do G-A4-17

**Odluka:** `A-THREAD-C15-G-A4-17-2026-08-17`

**Broj amandmana niti:** 9

**Autor i urednik:** Luka Sikic

**Datum odluke:** 17. kolovoza 2026.

**Datum evidentiranja:** 18. kolovoza 2026.

## Prihvaćeni slijed

Za ovu nit vrijedi strogi slijed pet paketa:

1. `C15`;
2. `G-A4-16`;
3. `WD-C16`;
4. `C16`;
5. `G-A4-17`.

Ovaj je amandman deveti, nov i odvojen od svih ranijih amandmana niti, čiji
su nizovi završili. Nadomješta samo uobičajenu obvezu zaustavljanja nakon
jednoga paketa za imenovani niz. Ne spaja pakete i ne dopušta dva istodobna
write locka. Svaki se paket zasebno potpuno evidentira, provjerava, zatvara i
lokalno commitira prije claimanja sljedećega. Nijedan packet ili item
preduvjet nije ukinut.

## Stajališta na kojima se nit mora zaustaviti

`C15`, `G-A4-16`, `C16` i `G-A4-17` traže autorovu odluku. Zaustavljanje na
svakome od tih mjesta očekivani je ishod. Stalna delegacija od 5. kolovoza
2026. ne može zamijeniti točan odgovor za prihvaćanje poglavlja. Nijedan zapis
ne smije tvrditi da je autor pročitao poglavlje.

`C15` je pri primitku odluke već bio claiman i u stanju `in_progress`, s
pripremljenim paketom
`notes/reports/c15-acceptance-package-2026-08-17.md`. Ne claimanja se ponovno,
ne vraća se stablo i ne prepisuje se pripremljeni paket. Točan autorov odgovor
`C15 accepted for a385ddc85c11e5d1cf63b33043c1df2a90cff6fb on 2026-08-17`
u ovoj niti dopušta samo usku dispoziciju navedenu u paketu.

`G-A4-16` je odluka o jednom stvarnom objavljenom regresijskom artefaktu,
pravima za točno predloženi prikaz i granici mosta prema binarnom ishodu.
Paket priprema potpun brief po uzoru na `G-A4-03` i `G-A4-12`, ali ne dohvaća
ni promovira podatke, ne piše prozu poglavlja i ne odgovara umjesto autora.

`WD-C16` jedini je paket u nizu koji može završiti bez autorova odgovora. Mora
slijediti ratificirani spine `G-A2b-V` i odluku `G-A4-16`, potrošiti sve stvarno
primjenjive handoffe, poštovati portalnu i nepromoviranu ESS granicu, navesti
obvezni lokalni offline put te provesti završni paralelni panel svih šest
read-only kritičara. Fatalni ili neriješeni veliki nalaz zaustavlja paket.

`C16` traži točan odgovor `C16 accepted for <commit> on <date>` vezan uz
završni WD-C16 commit. `G-A4-17` priprema potpuni brief unutar ratificiranih
granica 17. poglavlja i zaustavlja se za točan autorov odgovor.

## Trajne granice

Poglavlje 6 ostaje `draft` pod `H-WB-PART-001`. Poglavlja 7–12 ostaju
ponovno prihvaćena pod `C07-C12-REACCEPT`, a poglavlja 13–15 ne mijenjaju se
nakon vlastitih acceptance gateova. Vrijede sve granice za DigiKat, Eurostat,
ESS, vremena čitanja, nove čitatelje, terminološku recenziju i prava. Ne smije
se izmisliti broj, izvor, studija, citat ili dopuštenje. Push, merge, tag,
arhiviranje, deployment i objava nisu autorizirani.
