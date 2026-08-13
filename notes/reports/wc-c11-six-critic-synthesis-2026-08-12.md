# WC-C11 — sinteza šest kritičara

Panel je radio u dva zaključana read-only prolaza. Prvi prolaz nad SHA-256
`4d1930513ea30c0bde8ef51c0b57df621140b6bb685ad2054bec1e9f996628f8`
pronašao je jedan fatalni i jedan major metodološki nalaz. Autor je 13. kolovoza
2026. odobrio samo ta dva popravka i odredio da minor nalazi ostanu za `C11`.

Svih šest kritičara potom je ponovno, neovisno i u cijelosti pročitalo isti
završni izvor:

- SHA-256: `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`
- git blob: `87db0124679ae2085f87c4e7cc4145f9e3191b8f`

Pokriveni su statističke metode, skepticizam, pedagogija, dokazna osnova,
hrvatski rukopisni stil i struktura.

## Završni ishod

| Težina | Broj |
|---|---:|
| Fatalno | 0 |
| Major | 0 |
| Minor zapisi po lećama | 13 |

Panel prolazi za closeout `WC-C11` i izlaganje autoru u `C11`. Sinteza
preporučuje; ne bilježi prihvaćanje poglavlja niti tvrdi da ga je autor pročitao.

## Razrješenje obveznih nalaza

1. Kod i proza sada odvojeno definiraju strogu nadmoć, izjednačenja i mjeru s
   nasumičnim razrješavanjem izjednačenja. Neovisna reprodukcija daje 53,6 %,
   13,9 % i 60,6 %.
2. Kružni račun opažene snage sada se suprotstavlja unaprijed zadanom sadržajnom
   cilju. Razlika 0,5 uz poznatu SD 1,9 daje `d = 0,2632`, a isti obostrani
   postupak za 80 % snage traži 227,64, odnosno 228 osoba po skupini.

Metodološki kritičar potvrdio je da su prethodni fatalni i major nalaz potpuno
razriješeni. Dokazni kritičar reproducirao je cijele omjere i potvrdio da nove
vrijednosti nisu prikazane kao vanjski empirijski nalaz.

## Minori za C11

Trinaest zapisa po lećama grupira se u šest cjelina:

- poluširina nasuprot ukupnoj širini intervala;
- lokalne uzročne, mjerne i normativne ograde;
- objašnjenje simbola prije formule i razlikovanje ukupnoga `n` od `n` po
  skupini;
- usklađivanje broja ponavljanja i vođenih poteza digitalne i tiskane rute;
- nominalni naslovi, prirodniji prijelazi, uklanjanje ponavljanja i idiomatski
  početak sažetka;
- jedan novi lokalni stilski nalaz o antecedentu „Rečenica tog oblika” i teškom
  redu riječi u uvjetnoj rečenici ciljnoga učinka.

Nijedan minor ne blokira `WC-C11`. Svi ostaju vidljivi za autorsku dispoziciju
u `C11`, sukladno izričitom odobrenju opsega popravka.

## Suglasnost panela

Svih šest leća potvrđuje da završni izvor nema fatalni ni major nalaz. Panel se
slaže da su pretpostavke postupaka jasno omeđene, kanonski poredak vraćen,
tiskana ruta ocjenjiva, citati i podrijetlo provjerljivi te da niska snaga nije
pretvorena u presudu o istinitosti. Završna preporuka je zatvoriti `WC-C11` na
stvarnim provjerama i predati točan commit autoru kroz gate `C11`.
