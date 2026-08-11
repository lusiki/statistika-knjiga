# G-A3-ESS — odluka o ESS Round 11 paketu

**Status:** paket je pripremljen i čeka točnu odluku autora; ništa nije
promaknuto ni preuzeto.

**Datum pripreme:** 11. kolovoza 2026.

**Vlasnik odluke o odabiru i nastavnoj ulozi:** Luka Sikic, autor/editor.

**Vlasnik odluke o redistribuciji:** ESS data/rights owner. Autorova urednička
odluka ne može zamijeniti pisanu potvrdu nositelja prava.

## Granica paketa

Ovaj gate smije odabrati točno izdanje, hrvatski podskup, varijable, težine,
nastavno pitanje, potrošače i pravnu traku. Ne smije preuzeti mikropodatke,
izračunati ili izmisliti empirijski rezultat, stvoriti lokalnu snimku, promaknuti
paket, urediti poglavlje ni protumačiti portalni pristup kao ovlast za
redistribuciju.

`H-P1B-DATA-LIC-003` zadržava početnu traku `portal-mediated`.
`H-P3-CATALOG-001` zadržava `promoted: false`, prazan `files` i zabranu
promocije bez točnoga izvora, licence, atribucije, kontrolnoga zbroja i
službenoga usklađenja. `H-WC-C07-THREAD-SEQUENCE-001` dopušta nastavak samo
nakon zasebne odluke i zatvorenoga paketa.

## Provjerena polazišta

- Katalog pinna **ESS Round 11, edition 3.0**, objavljen 2. lipnja 2025., i
  jedinicu „jedan ispitanik s težinom uzorkovanja”. Službena objava potvrđuje da
  edition 3.0 uključuje Hrvatsku i 27 drugih zemalja.
- Podaci su zabilježeni kao CC BY-NC-SA 4.0, dokumentacija kao CC BY-SA 4.0,
  ali D08 izričito ne odobrava bundling bez zasebne pisane potvrde. Portal traži
  korisnički zapis i ESS preporučuje službenu distribucijsku traku.
- Službena ESS uputa preporučuje `anweight` kao zadanu analitičku težinu.
  Razlikuje `dweight`, `pspwght`, `pweight` i `anweight`; dostupnost tih
  varijabli ne daje pravo na lokalno udomljavanje mikropodataka.
- Trenutačni katalog navodi samo `WD-C13`, `WD-C14`, `WD-C15` i `WD-C16`.
  Route A čini `WC-C08` stvarnim potrošačem i taj potrošač mora biti dodan tek
  u `P3-ESS`, nakon odluke.
- Lokalni licenčno čisti skupovi `anketa_mreze` i `populacija_medija` nemaju
  anketnu težinu. Ne mogu poduprijeti empirijsku ESS tablicu niti se smiju
  prikazati kao da je imaju.

Službeni izvori pregledani su samo čitanjem dokumentacije, bez dohvata
mikropodataka:

- <https://www.europeansocialsurvey.org/news/article/third-round-11-data-release-published>
- <https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting>
- <https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS_weighting_data_1_1.pdf>
- <https://www.europeansocialsurvey.org/contact/disclaimer>
- <https://ess.sikt.no/en/api>

## Preporučena odluka o odabiru

### Izdanje, podskup i varijable

- izdanje: `ESS11`, integrated main file, edition `3.0`;
- podskup: svi retci za `cntry == "HR"`; bez globalnoga listwise brisanja,
  nego uz analitički imenovan nazivnik i isključenje nevrijedećih odgovora samo
  za varijablu koja ulazi u pojedini izračun;
- identitet i inačica: `essround`, `edition`, `proddate`, `idno`, `cntry`;
- nacrt i težine: `dweight`, `pspwght`, `pweight`, `anweight`, `prob`,
  `stratum`, `psu`;
- nastavni sadržaj: `vote`, `trstprl`, `stflife`, `gndr`, `agea`, `eisced`.

`P3-ESS` mora iz službenoga codebooka prepisati oznake, dopuštene vrijednosti i
šifre nedostajanja doslovno. Gate ne odobrava nijednu šifru koja nije potvrđena
tim izvorom.

### Točno omeđeno nastavno pitanje

> Među ispitanicima ESS Round 11 edition 3.0 u Hrvatskoj koji prema službenoj
> šifri pripadaju nazivniku za pitanje `vote`, koliko se udio onih koji navode
> da su glasali razlikuje između neponderirane procjene i procjene s
> `anweight`, te koje pogreške odabira ili mjerenja ta težina i dalje ne može
> ukloniti?

To je opisna i generalizacijska nastavna tvrdnja, ne provjera službene izlaznosti
i ne uzročna tvrdnja. Samoprijava, neodgovor, nepokrivenost okvira i službeni
cilj populacije ostaju vidljiva ograničenja.

### Uloge težina

- `anweight` je jedina zadana težina za čitatelje i izračun u opcionalnoj ESS
  replikaciji;
- `dweight` se čuva radi objašnjenja nejednakih vjerojatnosti odabira, ali nije
  zadana konačna procjena;
- `pspwght` se čuva radi objašnjenja naknadnoga usklađenja i kontrole
  jednocountry procjene;
- `pweight` se čuva radi cjelovitosti službenoga recepta, ali se ne koristi za
  hrvatsku jednocountry tablicu niti kao povod za prekograničnu analizu;
- `prob`, `stratum` i `psu` ostaju izloženi u shemi kao opis nacrta, bez tečaja
  o složenoj varijanci.

### Potrošači i nastavne trake

Potrošači postaju točno `WC-C08`, `WD-C13`, `WD-C14`, `WD-C15` i `WD-C16`.
ESS mikropodaci ostaju **neobvezna portalna empirijska replikacija**. Nijedan
obvezni R, jamovi, HTML ili tiskani zadatak ne ovisi o njima.

Za `R12-C08-weighted-table` preporučuje se zasebna, jasno označena **sintetička
tablica konačne nastavne populacije** s unaprijed navedenim vjerojatnostima
odabira, odgovorom i težinom `1 / vjerojatnost odabira`. Poglavlje 8 iz nje
prikazuje neponderirani i ponderirani postotak, cijeli nazivnik i svaku težinu.
To nije empirijski ESS rezultat i ne smije biti tako opisano.

Obvezni offline zadatak koristi istu malu tiskanu sintetičku tablicu i traži da
čitatelj ručno reproducira oba postotka. Opcionalna portalna ESS replikacija
postavlja isto pitanje nad `vote` i `anweight`, ali njezin rezultat ne ulazi u
obvezni zadatak, build, CI ili lokalni paket. Time je unaprijed zatvorena
napetost između obvezne ponderirane tablice i neobvezne ESS empirijske trake.

## Prava i traka

Preporuka je zadržati `lane: portal-mediated`, `promoted: false`, `files: []`,
bez lokalnih bajtova i bez lokalnoga kontrolnoga zbroja. Licenca otvorena za
nekomercijalnu ponovnu uporabu ne nadjačava D08, a mogućnost preuzimanja nakon
registracije ne dokazuje ovlast za redistribuciju u knjizi.

`OA-G-A3-ESS-RIGHTS` ostaje zaseban, neposlan i otvoren upit. Nije potreban za
portalni `P3-ESS`; potreban je prije svake buduće odluke o bundlingu. Ovaj gate
ne šalje poruku nositelju prava i ne glumi njegov odgovor.

## Odbijene alternative

1. **Bundled extract sada.** Odbijeno: D08 i `R03-ESS-permission-gate`
   zahtijevaju zasebnu pisanu potvrdu.
2. **Portalna ESS tablica kao obvezni Chapter 8 zadatak.** Odbijeno: registracija
   i nedostatak lokalnih bajtova učinili bi obvezni put netestabilnim offline.
3. **Dodati težinu lokalnim generiranim podacima poslije činjenice.** Odbijeno:
   to bi izmislilo nacrt koji generator nema.
4. **Koristiti `pweight` za hrvatsku jednocountry tablicu.** Odbijeno: ta
   težina rješava razlike veličina populacija među zemljama, a pitanje je
   omeđeno Hrvatskom.
5. **Odabrati sve ESS varijable.** Odbijeno: povećava dokazni, privatnosni i
   nastavni opseg bez uloge u pet imenovanih potrošača.

## Što odluka blokira

Bez točnoga odgovora autora ne mogu se zatvoriti `G-A3-ESS` ni pokrenuti
`P3-ESS`. Posljedično ostaju blokirani `WC-C08`, njegova četiri pojedinačna
ESS-preduvjeta i cijeli kasniji lanac. `OA-G-A3-ESS-RIGHTS` ne blokira portalni
put, ali apsolutno blokira bundling.

## Točan odgovor potreban za nastavak

Ako prihvaćate preporuku, odgovorite doslovno:

```text
ESS selection approved on 2026-08-11: use ESS Round 11 integrated main file edition 3.0, subset cntry == HR with analysis-specific valid-response denominators, identity variables essround/edition/proddate/idno/cntry, design variables dweight/pspwght/pweight/anweight/prob/stratum/psu, teaching variables vote/trstprl/stflife/gndr/agea/eisced, default analysis weight anweight, consumers WC-C08/WD-C13/WD-C14/WD-C15/WD-C16, and the bounded vote question recorded in notes/reports/g-a3-ess-selection-decision-2026-08-11.md. Keep ESS portal-mediated, unpromoted and optional; keep OA-G-A3-ESS-RIGHTS open and bundling prohibited. Chapter 8's mandatory weighted table and offline task use the separately labelled synthetic finite-population table with known inclusion probabilities, not ESS microdata.
```

Ako ne prihvaćate preporuku, navedite jednu točnu zamjenu za varijable,
podskup, pitanje, težinu ili offline tablicu. Odluku o bundlingu nemojte
uključiti prešutno: za nju je potreban zaseban odgovor nositelja prava na
`OA-G-A3-ESS-RIGHTS`.

## Granica ovlasti nakon odgovora

Točan odgovor dopušta samo closeout `G-A3-ESS`. `P3-ESS` se potom zasebno
claima, dokazuje i commitira. Ne dopušta preuzimanje mikropodataka, bundling,
uređivanje poglavlja, push, merge, tag, arhiviranje, deployment ni objavu.
