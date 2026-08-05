# DIP 2024 — putovnica portalno posredovanoga izvora

**Status:** provjeren portalni put; nema lokalne kopije i paket nije promoviran.

**Datum pregleda:** 5. kolovoza 2026.

**Odluka:** `G-A3-DIP`,
`notes/reports/g-a3-dip-selection-decision-2026-08-05.md`.

## Izvor i točna ruta

Početna stranica službenih otvorenih podataka za izbore za Hrvatski sabor:

<https://www.izbori.hr/site/UserDocsImages/479>

Na toj stranici odaberite **2024.** Poveznica vodi na službeni arhiv:

<https://www.izbori.hr/site/UserDocsImages/2024/rezultati_sabor.zip>

Ovaj paket arhiv nije preuzeo. Pregled zaglavlja HTTP odgovora 5. kolovoza
2026. zabilježio je status 200, `Content-Type: application/x-zip-compressed`,
`Content-Length: 11173400`, `Last-Modified: Mon, 07 Oct 2024 14:53:07 GMT` i
`ETag: "c4d2139fc818db1:0"`. ETag je identifikator odgovora poslužitelja, a ne
kontrolni zbroj lokalne datoteke. Lokalna datoteka ne postoji.

Službeni kontrolni prikaz jest *Izvješće o provedenim izborima za zastupnike u
Hrvatski sabor 2024.*:

<https://www.izbori.hr/site/UserDocsImages/2024/Izbori_za_zastupnike_u_Hrvatski_sabor/Rezultati/Izvje%C5%A1%C4%87e%20o%20provedenim%20izborima%20za%20zastupnike%20u%20Hrvatski%20sabor%202024.pdf>

Zaglavlje odgovora 5. kolovoza 2026. zabilježilo je status 200,
`Content-Type: application/pdf`, `Content-Length: 2883428`, `Last-Modified: Thu,
25 Apr 2024 10:40:55 GMT` i `ETag: "a5d26adfd96da1:0"`. Za nastavnu ulogu
mjerodavna je tablica **Odaziv birača** na stranici 124; pojedinačni redci
izbornih jedinica u istom izvješću daju kontrolu važećih i nevažećih listića.

## Prava i granica pristupa

Službena stranica izvor naziva otvorenim podacima i kaže da su rezultati
dostupni u formatima XLSX i CSV. Na pregledanoj stranici nije pronađena izričita
licenca ni drugi tekst koji bi dokazao pravo knjige da redistribuira lokalnu
kopiju. Dostupnost zato ostaje tehnički pristup, ne redistribucijska ovlast.

Knjiga nije tražila niti dobila dopuštenje nositelja prava i ne smije tvrditi
suprotno. Čitatelju daje službenu poveznicu i postupak provjere. Za svaki obvezni
zadatak bez mrežnoga pristupa ostaje provjereni DZS agregat ili generirani
kategorički skup iz `data/katalog.yml`.

## Jedinica, ključ i polja

Nastavni redak jest jedna izborna jedinica, `I.`–`XII.`. Ključ je oznaka izborne
jedinice. Nacionalna vrijednost `UKUPNO I. - XII.` služi samo usklađenju i ne
ulazi kao trinaesti analitički redak.

Za XII. izbornu jedinicu službena tablica odaziva objavljuje jedinstveni redak
za broj birača i broj pristupilih glasovanju. Važeći i nevažeći listići
provjeravaju se zbrojem šest zasebno objavljenih redaka nacionalnih manjina. Ta
razlika u strukturi mora ostati vidljiva; ne smije se prikazati kao da portal
objavljuje jednu lokalnu pravokutnu datoteku koju je knjiga provjerila.

| Semantička uloga | Oznaka u službenom izvješću | Napomena |
|---|---|---|
| ključ | `Izborna jedinica` | rimske oznake I.–XII. |
| nazivnik izlaznosti | `Ukupno birača` | birači na obrađenim biračkim mjestima; nije isti pojam kao zasebni broj birača iz registra na stranici 123 |
| brojnik izlaznosti | `Pristupilo glasovanju` | brojnik postotka u tablici na stranici 124 |
| kontrola listića | `glasovalo birača (prema glasačkim listićima)` | razlikuje se od broja pristupilih |
| važeći listići | `važećih glasačkih listića` | dio broja prema listićima |
| nevažeći listići | `nevažećih glasačkih listića` | dio broja prema listićima |

Tablica ne prikazuje šifre nedostajućih vrijednosti. Paket zato ne iznosi
tvrdnju o šiframa u sadržaju arhiva koji nije preuzet. U provjerenom prikazu svih
dvanaest redaka nema prazne vrijednosti za nazivnik, brojnik ili postotak.

## Usklađenje na portalu

Usklađenje je izvedeno nad brojevima prikazanima na službenom portalu, bez
spremanja izborne datoteke.

| Kontrola | Objavljena ukupna vrijednost | Zbroj objavljenih sastavnica | Ostatak |
|---|---:|---:|---:|
| birači u nazivniku, I.–XII. | 3558089 | 3558089 | 0 |
| pristupilo glasovanju, I.–XII. | 2216763 | 2216763 | 0 |
| važeći + nevažeći prema listićima | 2215209 | 2154733 + 60476 | 0 |

Objavljeni ukupni odaziv jest 62,30 %, a izračun
`2216763 / 3558089 × 100` daje 62,30 % nakon zaokruživanja na dvije decimale.
Za jedinice I.–X. objavljeni su zbrojevi 3482150 i 2140824, a omjer daje
61,48 %, također bez odstupanja nakon istoga zaokruživanja.

Važećih listića zbrojeno je 2154733, nevažećih 60476, ukupno 2215209 prema
glasačkim listićima. To je 1554 manje od 2216763 birača koji su pristupili
glasovanju. Razlika nije ispravljena ni sakrivena: ona dokazuje zašto se oznake
`pristupilo glasovanju` i `glasovalo birača (prema glasačkim listićima)` ne smiju
zamijeniti.

## Što je, a što nije provjereno

Provjereni su službena ruta, identitet dviju objava, datum pregleda, HTTP
metapodaci, objavljene oznake tablice i gore navedena usklađenja. Provjereno je i
da `data/katalog.yml` za `dip_2024` zadržava `lane: portal-mediated`,
`promoted: false`, `files: []`, `checksum: null`, `promoted_by: null` i
`promoting_gate: null`.

Nije provjeren sadržaj ZIP arhiva, njegovi interni nazivi datoteka, bajtovi,
kontrolni zbroj, pravokutna shema ni šifre nedostajućih vrijednosti. Nijedan od
tih lokalnih testova nije proglašen prolaznim. Paket nije promoviran i nema
zapisa u `promotion_log`.
