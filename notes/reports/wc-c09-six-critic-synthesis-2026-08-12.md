# WC-C09 — sinteza šest kritičara

**Konačni izvor:** `chapters/09-procjena.qmd`

**Konačni SHA-256:**
`42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`

Šest neovisnih kritičara samo za čitanje pregledalo je isto zaključano
materijalno stanje. Svaki je potvrdio isti hash prije i nakon pregleda; nijedan
nije uređivao datoteke. Ovo je preporuka panela, a ne autorsko prihvaćanje C09.

## Predfinalni blokirajući prolaz

Prvi kritičarski krug pronašao je da interaktivne usporedbe nisu još držale
jedan zajednički niz, da je formalni jezik prethodio dovoljnom iskustvu
pokrivenosti, da tiskani put nije nosio punu kontroliranu usporedbu, da je
radni primjer iz cilja preciznosti prelazio u neutemeljenu tvrdnju o promjeni,
da je nepreklapanje intervala preširoko tumačeno te da kritična vrijednost
`z*` nije objašnjena prije formule. Dokazni prolaz usto je tražio preciznije
omeđenje i isto-rečenične citate za Hoekstrin primjer.

Prije zaključavanja uvedeni su zajednička matrica izvlačenja i usporedbe A/B
te A/C, pokrivenost je prikazana prije imenovanja, tiskani parovi nose istu
logiku, razrađeni primjer ima unaprijed zadan cilj margine do deset minuta,
nepreklapanje je svedeno na kompatibilnost uz izravan interval razlike, `z*`
je objašnjen prije formule, a Hoekstrin je primjer označen kao hipotetski i
citiran u istoj rečenici. Svih šest kritičara zatim je ponovno pregledalo
novi, konačni hash. Nijedan završni nalaz nije potaknuo novu promjenu izvora.

## Rezultati po perspektivi

| Perspektiva | Sažeta ocjena | Fatalni | Veliki | Manji | Korisni |
|---|---:|---:|---:|---:|---:|
| metode | 5/5 | 0 | 0 | 0 | 0 |
| skepticizam | 5/5 | 0 | 0 | 1 | 0 |
| pedagogija | 5/5 | 0 | 0 | 0 | 0 |
| dokazi i citati | 5/5 | 0 | 0 | 0 | 0 |
| hrvatski stil | 4–5/5 | 0 | 0 | 3 | 0 |
| struktura | 5/5 | 0 | 0 | 1 | 0 |
| **zbroj zapisa** |  | **0** | **0** | **5** | **0** |

Zbroj označuje zapise u pojedinačnim izvještajima, ne pet jedinstvenih
materijalnih problema. Nijedan zapis ne mijenja aritmetiku, izvor podataka,
estimand, pokrivenost postupka, pseudonasumični slijed ili dosege
generalizacije.

## Zajednički zaključci

Svih šest perspektiva slaže se da:

- nema fatalnoga ni velikoga nalaza na konačnom izvoru;
- `R13-C09-coded-uncertainty`, `R23-C09-code-reading`, `R32-C09-static` i
  `R35-REACHBACK-09` materijalno zadovoljavaju svoje testove, ali ostaju
  `ratified` do C09;
- `R32-CATALOG-paired-views` sada ima i potpuno pomirene datoteke i zadatak
  koji iz analitičkoga prikaza reproducira objavljeni agregat;
- pokrivenost prethodi formalizaciji, a usporedbe razine pouzdanosti i veličine
  uzorka mijenjaju po jednu stvar;
- živi w09 i parity adapter rabe isti necachirajući generator bez promjene
  tolerancije, uz golden dokaz i negativni fixture za asimetrično trošenje
  polarnoga parnjaka;
- uzorkovna, koderska i mjerna nesigurnost ostaju razdvojene;
- šest audit pitanja, šest dimenzija tvrdnje, samoprovjera i sedmopoljna potvrda
  provjere zatvaraju ugovor Part III;
- poglavlje 3 dohvaćeno je točno kroz „Istraživač margine pogreške”, bez
  ponavljanja uzorkovnoga duga poglavlja 8;
- panel ne može zamijeniti zaseban, točan i datiran C09 odgovor autora.

## Otvoreni neblokirajući nalazi

Pet minor zapisa ostaje vidljivo u pojedinačnim izvještajima: jedna
kategorična formulacija o uskom intervalu iz pristranoga uzorka, duljina
sažetka, jedno podebljavanje, izraz „binarni prolaz” i vinjeta koja je više
metodološki scenarij nego imenovan slučaj. Nijedan ne opravdava promjenu izvora
nakon zaključavanja zajedničkoga hasha.

## Preporuka panela

Panel preporučuje prihvatiti WC-C09 kao dovršen vertikalni rez i predati
zaključani izvor zasebnom C09 autorskom/editorijalnom gateu. Svih pet minor
zapisa ostaje vidljivo. Njihovo popravljanje sada promijenilo bi izvor nakon
završnoga panela i poništilo zajednički dokazni hash.

Poglavlje 9 zato ostaje `draft`, a četiri poglavne upravljane stavke ostaju
`ratified` dok autor ne odgovori točno za konačni WC-C09 commit.
