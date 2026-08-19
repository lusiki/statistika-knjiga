# Autorski amandman za niz G-A3-TEXT do C17

**Odluka:** `A-THREAD-G-A3-TEXT-C17-2026-08-17`

**Broj amandmana niti:** 10

**Autor i urednik:** Luka Sikic

**Datum odluke:** 17. kolovoza 2026.

**Datum evidentiranja:** 18. kolovoza 2026.

## Prihvaćeni slijed

Za ovu nit vrijedi strogi slijed pet paketa:

1. `G-A3-TEXT`;
2. `P3-TEXT`;
3. `P3-VERIFY`;
4. `WD-C17`;
5. `C17`.

Ovaj je amandman deseti, nov i odvojen od svih devet ranijih amandmana niti,
čiji su nizovi završili. Nadomješta samo uobičajenu obvezu zaustavljanja nakon
jednoga paketa za imenovani niz. Ne spaja pakete i ne dopušta dva istodobna
write locka. Svaki se paket zasebno potpuno claima, evidentira, provjerava,
handoff-disponira, zatvara i lokalno commitira prije claimanja sljedećega.
Nijedan paketni ni stavkovni preduvjet nije ukinut.

## Stajališta na kojima se nit mora zaustaviti

`G-A3-TEXT` i `C17` traže točnu autorovu odluku. Zaustavljanje na oba mjesta
očekivani je ishod. Stalna delegacija od 5. kolovoza 2026. ne može zamijeniti
odgovor na autorsko pitanje ni prihvaćanje poglavlja. Nijedan zapis ne smije
tvrditi da je autor pročitao poglavlje.

`G-A3-TEXT` odvojeno priprema odluku o točnom malom odabiru ParlaMint-HR i
ParlaSent materijala te odluku o dvama različitim licenčnim režimima. Prije
claima troši `H-P1B-DATA-LIC-003`; prije prve sadržajne izmjene priznaje
`H-P3-CATALOG-001`, koji se može potrošiti tek pri closeoutu. Ne dohvaća ni
promovira podatke i ne tvrdi da je pribavljeno dopuštenje nositelja prava.

`P3-TEXT` gradi samo ono što je autor ratificirao. Svaki paket dobiva točan
izvor, inačicu, licencu, atribuciju, kontrolni zbroj s imenovanim algoritmom i
stvarno usklađenje ili dokumentiranu nemogućnost. Ako paket ostane
nepromoviran, to se dokazuje nad repozitorijskim stanjem.

`P3-VERIFY` je omnibus samo za `P3-VERIFY-A`, `P3-VERIFY-B`, `P3-VERIFY-C`,
`P3-VERIFY-D` i `P3-TEXT`. Svaki preduvjet provjerava zasebno nad jednim
deklariranim stanjem izvora i ponovno pokreće svaku determinističku provjeru i
svaki namjerni negativni fixture.

`WD-C17` je potpuni vertikalni presjek prema ratificiranoj kralježnici
`G-A2b-V` i brifu `G-A4-17`. Svih sedam ciljanih handoffova obrađuje na
njihovim točnim gateovima. Šest neovisnih read-only kritičara čita jedno
završno materijalno stanje; fatalni ili neriješeni veliki nalaz zaustavlja
paket. Samo root/conductor mijenja kontrolne datoteke i zajedničke registre.

`C17` prikazuje završni source commit, šest izvještaja, sintezu, svaku
neriješenu ili namjerno prikazanu manju primjedbu i predloženu dispoziciju
ledgera. Zaustavlja se za odgovor `C17 accepted for <commit> on <date>`.

## Trajne granice

Poglavlje 6 ostaje `draft` pod `H-WB-PART-001`; ne mijenja se niti napreduje u
ovom nizu. Poglavlja 7–12 zadržavaju stanje iz `C07-C12-REACCEPT`.
Terminologija `G-A2c`, preduvjet 13. poglavlja i sve granice za DigiKat,
Eurostat, ESS, vremena čitanja, nove čitatelje, terminološku recenziju i prava
ostaju obvezni. Ne smije se izmisliti broj, izvor, studija, citat ili
dopuštenje. Push, merge, tag, arhiviranje, deployment i objava nisu
autorizirani.
