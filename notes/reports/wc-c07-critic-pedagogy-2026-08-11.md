# WC-C07 — završni pedagoški pregled

**Izvor:** `chapters/07-vjerojatnost.qmd`

**SHA-256 prije i poslije pregleda:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Pregled je bio neovisan i samo za čitanje; nijedna datoteka nije uređena ni
stvorena.

## Ocjene

- jasnoća: **4/5**
- postavljanje skele: **4/5**
- obrada preduvjeta: **5/5**
- kvaliteta zadataka: **4/5**

## Snage

- Čitatelj najprije vidi tri simulirana niza i tumači približavanje polovici,
  a tek zatim dobiva definiciju vjerojatnosti i naziv zakona velikih brojeva.
- Vjerojatnost kao kalibrirana nesigurnost razvijena je bez potiskivanja
  dugoročne učestalosti; skup prognoza od sedamdeset posto daje konkretan smisao
  kalibraciji.
- Widget je dio argumenta. Uvod, četiri vođena pokušaja i zaključak okružuju
  interakciju; HTML ima označene kontrole, dinamični opis i živu povratnu
  informaciju, a tiskani blizanac prenosi istu usporedbu kratkoga i dugoga niza.
- Most prema CLT-u čuva razliku između pojedinačnih podataka i raspodjele
  stopa. Razrađeni primjer daje vidljivi račun, objašnjava obje funkcije,
  ograničava zaključak i predaje argument poglavlju o uzorkovanju.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

1. **PED-C07-MIN-01 — retci 193, 227–239, 266–268 i definicije 281–304.**
   „Neovisni” se pojavljuje u opisu početne slike, a „uvjetna vjerojatnost” u
   pravilu množenja prije vlastitoga iskustvenog sidra. Rane pojave mogle bi se
   najprije izraziti običnim opisom procesa i nazivnika.
2. **PED-C07-MIN-02 — retci 599–613.** Uvjeti CLT-a ispravni su, ali „konačna
   varijanca”, „slaba ovisnost” i „beskonačna varijanca” ostaju neprozirni
   početniku. Jedna rečenica može pojasniti da je binarni ishod omeđen između
   nule i jedinice, pa mu je raspršenost nužno konačna.
3. **PED-C07-MIN-03 — retci 697–745, 926 i 937–939.** Konstrukcija i čitanje QQ
   prikaza objašnjeni su, ali naziv „QQ prikaz” nije izrečen u tijelu prije
   popisa pojmova i zadatka.
4. **PED-C07-MIN-04 — retci 930–939.** Konceptualni tier spaja razliku poznate
   i nepoznate vjerojatnosti s prosudbom normalnoga pravila i QQ prikaza. Isti
   sadržaj bio bi pregledniji kao dva numerirana zadatka.
5. **PED-C07-MIN-05 — retci 943–964.** Zadatak traži kratku tablicu prema šest
   pitanja, dok zaštićena projekcija rješenja daje sadržajno potpun odgovor u
   prozi. Zatvaranje postoji, ali ne modelira traženi oblik proizvoda.

### Korisna poboljšanja

1. **PED-C07-USE-01 — retci 238–245 i 902–904.** Izrazi „nulti model” i
   „jednostrana repna vjerojatnost” kratko anticipiraju jezik testiranja; mogu
   se zamijeniti običnijim izrazima ili vrlo kratko objasniti.
2. **PED-C07-USE-02 — redak 271.** Interni naziv `populacija_medija` izgleda
   kao programski identifikator u prozi za čitatelja bez programiranja.

## Doslovne dispozicije

- `R10-C07-degree-belief` — **prolazi**. Čitatelj razlikuje osobnu sigurnost,
  modelnu vjerojatnost i ponovljenu učestalost kao dokaz.
- `R29-C07-retrieval-load` — **prolazi**. Stanka počinje približno na 45,5 %
  javnoga nastavnog luka i završava oko 47,3 %, traži dohvat bez gledanja i daje
  popravnu rutu.
- `R35-REACHBACK-07` — **prolazi na razini poglavlja**. Zadatak traži brojnosti
  i svih šest revizijskih pitanja iz poglavlja 3; minor se odnosi samo na oblik
  projekcije rješenja.
- Simulacija prije formalizacije — **prolazi**.
- CLT most — **prolazi**.
- Četiri tiera i zabrana proizvodnje koda — **prolaze**.
- Kanonsko zatvaranje — **prolazi na pedagoškoj razini**.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **5**
- Korisno poboljšanje: **2**

**Verdikt:** pedagoški prolaz. Sedam neblokirajućih prijedloga ostaje vidljivo
za autorsku odluku na C07.
