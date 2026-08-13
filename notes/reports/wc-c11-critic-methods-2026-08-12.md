# WC-C11 — metodološki kritičar

Prvi pregled izveden je read-only nad zaključanim izvorom
`chapters/11-velicina-ucinka-i-snaga.qmd`:

- SHA-256: `4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
- git blob: `e4577e72897a6c450aba04f11270ca97bf19c26b`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 3/5 |
| Pretpostavke | 5/5 |
| Interpretacija | 3/5 |
| Preciznost | 4/5 |

## Snage

- Permutacijska demonstracija ispravno navodi puni distribucijski nul-model,
  razmjenjivost, neovisne jedinice, obostranu sirovu razliku sredina,
  uzorkovanje bez ponavljanja i obje Monte Carlo razine. Korekcija
  `(b + 1) / (B + 1)` uključuje izjednačenja i pravilno je ograničena na
  zadani mehanizam.
- Widget, tiskani par i razrađeni primjer dosljedno koriste obostrani
  z-postupak za dvije neovisne jednako velike skupine, normalne ishode i
  poznatu zajedničku standardnu devijaciju. Pomak `d sqrt(n / 2)` i kritične
  vrijednosti matematički su ispravni.
- Pretjerivanje značajnih procjena izričito je ograničeno na simulaciju. Niska
  snaga vodi prema nesigurnosti, selekciji, prethodnim dokazima i replikaciji,
  bez univerzalnog faktora ili paušalne presude.
- Tiskane vrijednosti reproduciraju se iz izvora: 42,5 %, 72,4 %, 94,6 % i
  99,9 %; agregatni prosjeci i razlika također se točno slažu. Razrađeni plan
  reproducira 46,2 %, 63,5 %, 75,05 % i 83,25 %.

## Nalazi

### Fatalno — mjera s izjednačenjima pogrešno je imenovana

Mjesto: retci 125 i 230.

Kod računa `P(tisak > portal) + 0,5 P(tisak = portal)`, ali proza dobivenih
približno 60,7 % tumači kao vjerojatnost da čitatelj tiska ima strogo više
povjerenja. Na diskretnoj ljestvici izjednačenja nisu zanemariva: stroga
vjerojatnost iznosi 53,64 %, vjerojatnost izjednačenja 13,94 %, a mjera s
polovicom izjednačenja 60,61 %.

Preporučeni popravak: izvijestiti strogu nadmoć i izjednačenja zasebno ili
jasno definirati mjeru kao vjerojatnost nadmoći uz nasumično razrješavanje
izjednačenja.

### Major — netočna tvrdnja o potrebnom uzorku

Mjesto: redak 755, osobito 761.

Ispravak opažene snage tvrdi da bi unaprijed zadana razlika „ove veličine”
zahtijevala znatno više od 30 osoba po skupini. Sam izvor učinka ne mijenja
račun: za unaprijed zadani `d = 0,78` isti postupak daje 80 % snage pri
približno 27 osoba po skupini. Više jedinica treba samo ako je sadržajno
opravdani ciljni učinak manji.

Preporučeni popravak: izbrisati tvrdnju ili imenovati manji ciljni učinak,
primjerice 0,5 boda uz SD 1,9 (`d` približno 0,26), za koji je potrebno
približno 228 osoba po skupini.

### Minor — nejasna širina intervala

Mjesto: redak 421.

„Procjena unutar pola boda” ne razlikuje poluširinu od ukupne širine intervala,
a prikazane širine počivaju na jednakim veličinama skupina i poznatoj
zajedničkoj raspršenosti.

Preporučeni popravak: napisati „poluširina intervala najviše 0,5 boda” i
lokalno navesti jednake neovisne skupine te poznatu zajedničku standardnu
devijaciju.

## Presuda prvoga prolaza

Poglavlje metodološki ne prolazi: postoji jedan fatalni i jedan neriješeni
major nalaz. Dva su nužna popravka lokalna i ne ruše nosivu logiku poglavlja.

## Završna ponovna provjera

Nakon autorova odobrenja dvaju obveznih popravaka kritičar je read-only
pregledao cijeli završni izvor:

- SHA-256: `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`
- git blob: `87db0124679ae2085f87c4e7cc4145f9e3191b8f`

Završne ocjene su točnost 5/5, pretpostavke 5/5, interpretacija 5/5 i
preciznost 4/5. Prethodni fatalni nalaz potpuno je razriješen: kod i proza sada
odvajaju 53,6 % stroge nadmoći, 13,9 % izjednačenja i 60,6 % prilagođene mjere.
Prethodni major nalaz također je razriješen: unaprijed zadana razlika 0,5 uz
SD 1,9 daje `d = 0,2632`, a `power.t.test` vraća `n = 227,64`, ispravno
zaokruženo na 228 osoba po skupini.

Ostaje jedan ranije evidentirani minor o tome označuje li „procjena unutar pola
boda” poluširinu ili ukupnu širinu intervala te o lokalnom imenovanju jednakih
neovisnih skupina i poznate zajedničke raspršenosti. Završna presuda glasi:
metodološki prolaz bez fatalnih ili major nalaza, uz jedan minor za dispoziciju
u `C11`.
