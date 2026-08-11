# WC-C08 — sinteza šest kritičara

**Konačni izvor:** `chapters/08-uzorkovanje.qmd`

**Konačni SHA-256:**
`9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04`

Šest neovisnih kritičara samo za čitanje pregledalo je isto zaključano
materijalno stanje. Svaki je potvrdio isti hash prije i nakon pregleda; nijedan
nije uređivao datoteke. Ovo je preporuka panela, a ne autorsko prihvaćanje C08.

## Predfinalni blokirajući prolaz

Prvi kritičarski krug pronašao je pogrešan odnos veličine uzorka i standardne
pogreške, preširoke tvrdnje o opstanku selekcijske pristranosti i „cijelom
zaključivanju” te nedovoljno omeđenu povijesnu formulaciju o Literary Digestu.
Prije zaključavanja panela tekst je ispravljen: deseterostruko veći uzorak sada
smanjuje standardnu pogrešku za `sqrt(10)`, a prepolovljavanje zahtijeva četiri
puta veći `n`; selekcijske i inferencijalne tvrdnje dobile su potrebne granice;
Squireove tvrdnje svedene su na potkrijepljeni doseg i citirane u istoj
rečenici.

Nakon tih popravaka svih je šest kritičara ponovno pregledalo konačni hash.
Nijedan završni nalaz nije potaknuo novu promjenu izvora.

## Rezultati po perspektivi

| Perspektiva | Sažeta ocjena | Fatalni | Veliki | Manji | Korisni |
|---|---:|---:|---:|---:|---:|
| metode | 4–5/5 | 0 | 0 | 2 | 0 |
| skepticizam | 5/5 | 0 | 0 | 2 | 0 |
| pedagogija | 4–5/5 | 0 | 0 | 2 | 0 |
| dokazi i citati | 5/5 | 0 | 0 | 1 | 0 |
| hrvatski stil | 4/5 | 0 | 0 | 6 | 0 |
| struktura | 4–5/5 | 0 | 0 | 4 | 0 |
| **zbroj zapisa** |  | **0** | **0** | **17** | **0** |

Zbroj označuje zapise u pojedinačnim izvještajima, ne sedamnaest jedinstvenih
problema. Pedagogija i struktura preklapaju se oko procjene učinka nacrta i
efektivne veličine uzorka; skepticizam i struktura različito osvjetljavaju
vinjetinu granicu; dokazni i stilski pregled bilježe različite strane
čitateljske vidljivosti fakultativnoga ESS puta.

## Zajednički zaključci

Svih šest perspektiva slaže se da:

- nema fatalnoga ni velikoga nalaza na konačnom izvoru;
- `R12-C08-survey-realism`, `R12-C08-weighted-table`,
  `R13-C08-corpus-selection` i `R35-REACHBACK-08` materijalno zadovoljavaju
  ratificirane testove, ali ostaju `ratified` do C08;
- središnja simulacija jednostavnoga slučajnog uzorkovanja ostaje očuvana, a
  formalizacija dolazi nakon iskustva ponavljanja;
- tablica `3/6 = 50,0 %` nasuprot `6/16 = 37,5 %` potpuno je reproducibilna i
  pošteno označena kao sintetička;
- ESS mikropodaci, empirijski ESS postotak i izmišljeni nazivnik nisu ušli u
  knjigu; portalni put ostaje fakultativan, nepromoviran i odvojen od obveznoga
  zadatka;
- težine, kalibracija, grupiranje, učinak nacrta i efektivni `n` imaju jasne
  granice, a zadaci ne izvode formulu varijance;
- korpusni odabir i podjela na skupove za učenje, provjeru i ispitivanje nisu
  zamijenjeni jedan drugim;
- citati, brojke i podrijetlo imaju provjerljiv trag;
- panel ne može zamijeniti zaseban, točan i datiran C08 odgovor autora.

## Otvoreni neblokirajući nalazi

Sedamnaest minor zapisa ostaje u pojedinačnim izvještajima. Najvažnije skupine
su lokalna preciznost dviju rečenica o uzorkovanju, potpuniji prikaz preduvjeta,
izravna provjera učinka nacrta u zadacima, jače sidro mjerenja u anketnoj
kartici, redoslijed završnih pojmova te nekoliko hrvatskih ritamskih i
provedbeno-žargonskih mjesta. Nijedan ne mijenja aritmetiku, estimand,
provenijenciju, pravo uporabe ili dosege generalizacije.

Dokazni minor da fakultativna ESS putovnica još nije izložena u čitateljskom
katalogu već pripada `P5-C` kroz `H-P3-CATALOG-002`; WC-C08 ne stvara
duplicirani handoff.

## Preporuka panela

Panel preporučuje prihvatiti WC-C08 kao dovršen vertikalni rez i predati
zaključani izvor zasebnom C08 autorskom/editorijalnom gateu. Svih 17 minor
zapisa ostaje vidljivo. Njihovo popravljanje sada promijenilo bi izvor nakon
završnoga panela i poništilo zajednički dokazni hash.

Poglavlje 8 zato ostaje `draft`, a četiri upravljane stavke ostaju `ratified`
dok autor ne odgovori točno za konačni WC-C08 commit.
