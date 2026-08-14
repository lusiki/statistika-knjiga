# WC-C10 — sinteza šest kritičara

**Konačni izvor:** `chapters/10-logika-testiranja.qmd`

**Konačni SHA-256:**
`b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236`

Šest neovisnih kritičara samo za čitanje pregledalo je isto zaključano
materijalno stanje. Svaki je potvrdio isti hash prije i nakon pregleda; nijedan
nije uređivao datoteke. Ovo je preporuka panela, a ne autorsko prihvaćanje C10.

## Predfinalni blokirajući prolaz

Prvi krug pronašao je tri velika nalaza: tiskani čitatelj nije mogao izvršiti
widget-korak računskoga zadatka, cijene pogrešaka nisu imenovale odluku ni
osobe koje snose posljedice, a tvrdnja o promjenjivosti p-vrijednosti
preopćenito je prelazila prikazanu simulaciju. Našao je i lokalne dugove u
imenovanju permutacijskoga testa, tumačenju standardizirane razlike,
permutacijskom uvjetovanju, uvodu u treću sliku, frekvencijskim tvrdnjama o
asistentu i čitateljima te ritmu proze.

Prije zaključavanja tiskani je put vezan uz prvi redak tablice s poznatom
nulom; hipotetska odluka imenuje istraživački tim, čitatelje i opisane skupine;
promjenjivost je omeđena ovom simulacijom; permutacijski udio govori o
rasporedima oznaka uz fiksne ishode i veličine skupina; nosivi naziv i
standardizirana ljestvica dobili su sidra; treća je slika uvedena svrhom; a
neprovjerene učestalosti neutralizirane su. Svih šest kritičara zatim je
ponovno pregledalo novi konačni hash.

## Rezultati po perspektivi

| Perspektiva | Sažeta ocjena | Fatalni | Veliki | Manji | Korisni |
|---|---:|---:|---:|---:|---:|
| metode | 5/5 | 0 | 0 | 0 | 0 |
| skepticizam | 5/5 | 0 | 0 | 0 | 0 |
| pedagogija | 4–5/5 | 0 | 0 | 1 | 0 |
| dokazi i citati | 5/5 | 0 | 0 | 0 | 0 |
| hrvatski stil | 4–5/5 | 0 | 0 | 3 | 0 |
| struktura | 5/5 | 0 | 0 | 0 | 0 |
| **zbroj zapisa** |  | **0** | **0** | **4** | **0** |

## Zajednički zaključci

Svih šest perspektiva slaže se da:

- nema fatalnoga ni velikoga nalaza na konačnom izvoru;
- D01 ostaje cijeli: puna nula i razmjenjivost, neovisne jedinice,
  promatračka granica, obostrana sirova razlika sredina, apsolutni rep,
  `(b + 1)/(B + 1)`, istinita puna nula i omeđeni Bayes;
- veličina i posljedice vode Dio IV, a svijet bez učinka doživljen je prije
  imenovanja nulte hipoteze;
- ASA je glavni nastavni dom epizode i razdvaja što je struka rekla, zašto i
  što je promijenila;
- pogrešivost referentne oznake ostaje omeđena i priprema poglavlje 17;
- dohvat poglavlja o vjerojatnosti i uzorkovanju ima HTML i tiskani put te
  kanonsko zatvaranje bez ocijenjene proizvodnje koda;
- živi w10 i OJS adapter rabe isti necachirajući generator, registrirani zlatni
  izlazi ostaju nepromijenjeni, tolerancija nije proširena, a w10-specifični
  cached-pair fixture pada zatvoreno;
- `R13-C10-label-fallibility`, `R31-C10-ASA-home` i `R35-REACHBACK-10`
  materijalno prolaze, ali ostaju `ratified` do C10;
- panel ne može zamijeniti zaseban, točan i datiran C10 odgovor autora.

## Otvoreni neblokirajući nalazi

Četiri minor zapisa ostaju vidljiva. Pedagoški izvještaj predlaže da osam
pojmova slijedi redoslijed prvih pojava. Stilski izvještaj bilježi jednu
kurikularnu formulaciju, jedno ordinalno nabrajanje u AI okviru i dvije
brojčane uputnice umjesto tematskih. Nijedan nalaz ne mijenja metodu, dokaz,
spine, dostupnost zadatka ili widget ugovor, pa ne opravdava novu promjenu
izvora nakon zajedničkoga završnog pregleda.

## Preporuka panela

Panel preporučuje prihvatiti WC-C10 kao dovršen vertikalni rez i predati
zaključani izvor zasebnom C10 autorskom/editorijalnom gateu. Sva četiri minor
zapisa ostaju vidljiva.

Poglavlje 10 zato ostaje `draft`, a tri poglavne upravljane stavke ostaju
`ratified` dok autor ne odgovori točno za konačni WC-C10 commit.
