# G-A4-03 — paket odluke za Tier F reviziju trećega poglavlja

**Gate:** `G-A4-03`

**Stanje gatea:** spreman za odluku autora/editora; prihvaćanje nije dano ni
zabilježeno.

**Imenovani vlasnik odluke:** Luka Šikić, autor/editor.

**Datum pripreme:** 6. kolovoza 2026.

## Jedna potrebna odluka

Potrebno je prihvatiti ili točno izmijeniti jedan povezani Tier F ugovor za
`chapters/03-kako-brojke-zavode.qmd`: javnu tvrdnju, njezin upravljani paket
dokaza, argumentacijski obris i granice opsega. Ovaj gate ništa ne dohvaća,
ne piše podatkovnu datoteku, ne promovira paket i ne mijenja prozu poglavlja.

## Dostupni dokazi i ispunjeni preduvjeti

- `C02` je prihvaćen za završni izvor drugoga poglavlja u commitu
  `0552e4a35052f7f7736b267a0f367f30df02d9c7`; jedinica, nazivnik,
  prihvatljivost, mjerenje i dizajn zato su dostupni preduvjeti.
- `P2-IDENTITY` u
  `notes/reports/p2-identity-briefs-2026-08-04.md` veže poglavlje uz jednu
  sljedivu javnu tvrdnju i devet koraka argumenta.
- Ratificirana kralježnica u
  `bookwright_plugin/bookwright/shared/chapter-spine.json` traži deset aspekata,
  šest pojmova, poglavlja 1 i 2 kao preduvjete te osam isključenja.
- `P3-DIP` u `notes/reports/p3-dip-2026-08-05.md` provjerava portalno
  posredovanu tablicu odaziva na izborima za Hrvatski sabor 2024., njezine
  službene oznake i objavljene ukupne vrijednosti, bez lokalne kopije.
- `P3-DZS` u `notes/reports/p3-dzs-2026-08-05.md` daje promoviran zakonit
  izvanmrežni put i dvije važne granice: turistička je jedinica dolazak, ne
  osoba, a administrativne i anketne brojke ne mjere isto i ne zbrajaju se.
- `P3-PILOT` nije preduvjet. Autor ga je 5. kolovoza 2026. izričito uklonio iz
  prvoga izdanja i iz `G-A4-03`; njegov status `descoped` ne prisvaja nijedan
  rezultat pilota.

## Preporučena dispozicija

Preporuka je prihvatiti DIP-ov portalno posredovani zapis kao jedini središnji
javni slučaj, pod ovom poštenom početnom tvrdnjom:

> Službeno izvješće DIP-a za izbore za Hrvatski sabor 2024. prikazuje ukupan
> odaziv od 62,30 %: 2.216.763 birača pristupilo je glasovanju od 3.558.089
> birača na obrađenim biračkim mjestima.

Tvrdnja se ne preuzima kao zaključak nego rastavlja. Dvanaest redaka izbornih
jedinica zbraja se u oba objavljena ukupna broja. Zbroj 2.154.733 važeća i
60.476 nevažećih listića daje 2.215.209 birača prema listićima, što je 1.554
manje od broja pristupilih. Te službene oznake nisu zamjenjive. Poglavlje smije
poduprijeti opis, povezanost i odluku; ne smije iz tablice izvesti potporu
listama, tvrdnju o pojedincu, uzročnost, ekološki zaključak, predikciju ni
generalizaciju izvan populacije izvora.

Izvor ostaje `portal-mediated`, `promoted: false`, s `files: []` i
`checksum: null`. Knjiga ne tvrdi da paket posjeduje, redistribuira ili ima
dopuštenje nositelja prava. Točan službeni izvor i datum pregleda moraju pratiti
svaku brojku. Svaki obvezni zadatak koji mora raditi bez portala koristi
promoviran DZS agregat ili upravljan generirani skup kao izvanmrežnu zamjenu;
zamjena ne postaje drugi narativni stup poglavlja.

## Tier F obris

Jedan argument teče ovim redom, bez pretvaranja u redni popis u rukopisu:

1. javna tvrdnja o ukupnom odazivu i točan službeni izvor;
2. os, jedinica, brojnik, nazivnik i razlika među službenim brojnicima;
3. temeljna stopa kao uvjet suda o rijetkom ishodu;
4. rana kartica za čitanje ankete, uz izričit dug prema poglavljima 8 i 9 za
   uzorkovanje i marginu pogreške;
5. biranje trešanja kroz razdoblje, podskupinu ili usporedbu;
6. broj koji je proizveo asistent i provjera izvora, podataka, transformacije,
   nazivnika i citata;
7. sintetički medij i pitanje podrijetla;
8. razlikovanje simulacije, sintetičkoga zapisa, hipotetskoga izlaza modela i
   izmišljenoga dokaza;
9. protokol skeptičnoga čitanja koji završava punom mapom tvrdnji, šest
   revizijskih pitanja i odgovorivom samoprovjerom Dijela I.

Poglavlje dobiva točno jedan novi definicijski blok, `temeljna stopa`, i nijedan
drugi. Središnji widget ostaje postojeći istraživač margine pogreške nad
simuliranom anketom; widget ne izvodi formalnu marginu pogreške i nije dokaz za
DIP-ovu administrativnu tablicu.

## Isključenja i granica ovlasti

- glavna epizoda Američkoga statističkog udruženja ostaje u poglavlju 10;
- nema izvođenja margine pogreške prije poglavlja 8 i 9;
- nema vidljivoga koda u Dijelu I ni ocijenjenoga pisanja koda;
- nema drugoga središnjeg widgeta, nove vrste okvira ni tekstno-računalnoga
  aparata;
- nema izmišljene brojke, slučaja, studije, citata ni neizvornoga hrvatskog
  primjera;
- nema uzročne, individualne, listovne ni ekološke tvrdnje iz DIP-ove tablice;
- nema tvrdnje da je DIP-ova datoteka lokalno spremljena, da sve edicije imaju
  portalni paritet ili da je pribavljeno dopuštenje nositelja prava;
- nema miješanja DZS-ovih dolazaka s osobama ni zbrajanja anketnih i
  administrativnih procjena;
- nema oslanjanja na uklonjeni početnički pilot;
- ovaj paket ne odobrava `WA-C03`, push, merge, tag, arhiviranje, deployment ni
  objavu.

## Alternative

1. **DZS kao središnji slučaj.** Jedna javna turistička tvrdnja može nositi
   lekciju o jedinici, ukupnom iznosu, komponentama i razlici između
   administrativnoga brojanja i anketne procjene. Prednost je potpuno
   izvanmrežan promovirani paket; cijena je slabija veza s postojećim
   istraživačem izborne ankete i javnom tvrdnjom o odazivu.
2. **Vratiti na doradu prije odabira.** Autor može navesti točnu promjenu javne
   tvrdnje, izvora, obrisa ili isključenja. `G-A4-03` tada ostaje `ratified`, a
   `WA-C03` se ne smije pokrenuti.

Nije dopuštena alternativa koja uvodi neprovjeren skup, spaja DIP i DZS u jednu
empirijsku brojku, premješta ASA epizodu natrag u poglavlje 3 ili pretvara
portalni pristup u pravo redistribucije.

## Što odluka blokira

Bez eksplicitne odluke ostaju blokirani `G-A4-03`, `WA-C03` i stavke
`R07-C03-full-argument`, `R10-C03-base-rate`, `R12-C03-poll-literacy`,
`R12-C03-margin-debt`, `R23-C03-no-R-production`,
`R24-C03-synthetic-media`, `R24-C03-AI-provenance`,
`R30-C03-slide-enumeration` i `R31-C03-public-case`.

## Potrebna autorova odluka

Nakon što Codex preda točan lokalni C02 closeout commit, preporučeni odgovor
glasi:

```text
G-A4-03 accepted as recommended for [C02 closeout commit] on 2026-08-06.
```

Ako se preporuka ne prihvaća, odgovor treba navesti točne blokirajuće izmjene
javne tvrdnje, dokaza, obrisa ili opsega protiv istoga commita. Do takve odluke
`G-A4-03` ostaje `ratified`; `WA-C03` nije pokrenut, a njegovi handoffovi ostaju
`pending`.
