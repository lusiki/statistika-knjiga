# WC-C07 — završni izvještaj kritičara statističkih metoda

**Izvor:** `chapters/07-vjerojatnost.qmd`

**SHA-256 prije i poslije pregleda:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Kritičar je radio neovisno i samo za čitanje. Nijedna datoteka nije uređena
niti je stvoren artefakt.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 4/5 |
| Pretpostavke | 5/5 |
| Tumačenje | 5/5 |
| Preciznost | 4/5 |

## Snage

- Modelna vjerojatnost, osobna sigurnost i ponovljena učestalost jasno su
  razdvojene, a kalibracija je operacionalizirana preko skupova usporedivih
  prognoza (retci 247–258).
- Komplement, zbrajanje, opće pravilo množenja i prečac uz neovisnost
  metodološki su točni. Neovisnost se opravdava procesom i dizajnom; podaci
  mogu otkriti kršenje, ali ne mogu sami potvrditi pretpostavku (retci
  262–300).
- Binomni računi i simulacije podudaraju se: `1−0,98^5 ≈ 9,6 %`,
  `P(X≥14)=19,416523 %`, a simulacija sa sjemenom 709 daje `19,31 %`.
  Widget i statički blizanac nose isti zaključak o sužavanju raspodjele stopa
  pri većem `n`.
- CLT je odvojen od oblika pojedinačnih podataka, simulacija vruće ruke
  omeđuje nulti model, a razrađeni primjer odvaja internu računsku provjeru,
  pristajanje modela i uzročni zaključak.

## Nalazi

### Fatal

Nema.

### Major

Nema.

### Minor

- **Lokacija:** odjeljak „Zvonasta krivulja i njezino područje”, retci
  576–580.
- **Razlog:** raspodjela stopa iz widgeta bez ograde se opisuje kao simetrična
  i zvonasta, iako dopušteni izbori poput `p=0,10` i `n=10` daju diskretnu i
  zamjetno asimetričnu binomnu raspodjelu. Kasniji odlomak ispravno kaže da
  oblik postaje bliži zvonastome rastom `n`, pa je problem lokalna preširoka
  formulacija.
- **Predloženi popravak:** napisati da je raspodjela pri prikazanim postavkama
  i dovoljno dugim nizovima približno simetrična ili odmah imenovati male `n`
  i krajnje `p` kao protuprimjer.

### Korisno poboljšanje

- **Lokacija:** objašnjenje i oznaka osi QQ prikaza, retci 699–707 i 724–731.
- **Razlog:** `stat_qq()` na vodoravnoj osi prikazuje teorijske kvantile
  standardne normalne raspodjele, dok „očekivana vrijednost” može zvučati kao
  sredina ili vrijednost u izvornoj mjernoj jedinici.
- **Predloženi popravak:** os označiti kao „Očekivani standardizirani položaj”
  ili „Teorijski kvantil standardne normalne raspodjele”.

## Dispozicija upravljanih stavki

- `R10-C07-degree-belief` — zadovoljen. Tri uloge vjerojatnosnoga broja ostaju
  razdvojene, a kalibracija dobiva provjerljivo značenje.
- `R29-C07-retrieval-load` — zadovoljen. Stanka na sadržajnoj sredini dohvaća
  standardiziranu vrijednost iz poglavlja 4 i povezuje je sa širinom
  raspodjele iz widgeta.
- `R35-REACHBACK-07` — zadovoljen. Zadatak zahtijeva povratak protokolu i
  brojnostima iz poglavlja 3, svih šest revizijskih pitanja te ispravne račune
  90 %, približno 15,4 % i temeljne stope 1 %.
- `R09-C07-clt-conditions` — očuvan. Ostaju stabilna zajednička raspodjela,
  neovisnost, konačna varijanca i ograda prema samo primjereno slaboj
  ovisnosti. Tekst ne tvrdi da CLT normalizira pojedinačne podatke.

Prethodni veliki nalaz o prešutnim pretpostavkama razrađenoga primjera zatvoren
je: jednaki poznati `p`, neovisnost i hipotetski status modela sada su izrečeni,
repna vjerojatnost nije potvrda modela, a uzročna tvrdnja upućena je na
nasumičnu dodjelu. AI okvir sadrži točno jednu statističku pogrešku:
neopravdano izvođenje neovisnosti iz zasebnosti jedinica.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **1**
- Korisno poboljšanje: **1**

**Verdikt:** metodološki prolaz za završni panel. Odluka o C07 ostaje
autoru/editoru.
