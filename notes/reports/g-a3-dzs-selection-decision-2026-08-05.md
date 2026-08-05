# G-A3-DZS — odabir, prava i uloga DZS turizma

**Gate:** `G-A3-DZS`

**Datum odluke:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik, ujedno nositelj podatkovne
politike.

**Dispozicija:** prihvaćeno kako je preporučeno, uz izričito pravilo o godini.

**Izvorno stanje odluke:**
`conversation:G-A3-DZS-selection-approved-2026-08-05-Luka-Sikic`.

## Što ovaj gate odlučuje

Tri stvari i ništa više: **koje tablice** ulaze u prvo izdanje, **koja traka**
vrijedi za njih, i **koju ulogu** paket nosi u knjizi. Uz to fiksira pravilo za
godinu snimke.

Gate ne dohvaća nijednu datoteku, ne stvara nijedan zapis u `data/`, ne promiče
nijedan paket i ne mijenja `data/katalog.yml`. Sve to radi `P3-DZS`.

## Ulazi pročitani prije odluke

- `H-P1B-DATA-LIC-003` u cijelosti, potrošen **prije preuzimanja paketa**;
- `H-P3-CATALOG-001`, potvrđen prije prve izmjene i potrošen pri zatvaranju;
- inventar `P1B-DATA-LIC`, redak DZS turizma i ugovor triju traka;
- autorova odredba o pravima od 5. kolovoza 2026.;
- `data/katalog.yml`, zapis `dzs_turizam`;
- vanjski upit `OA-G-A3-DZS-SELECTION` i stavka `R08-DZS-package`.

## Odabir

Prihvaćen je omeđeni odabir koji ratificirani plan već imenuje.

| Tablica | Što ulazi | Zašto |
|---|---|---|
| `BS_TU11` | cjelovita godina, nacionalna razina, mjesečni dolasci i noćenja | mjesečni niz nosi sezonalnost, koja je sadržaj poglavlja 3 |
| `BS_TU12` | jedan županijski presjek | druga geografska razina uz istu definiciju, za usporedbu razina |
| `T01`–`T03` | omeđeni dugi izvadak | zadržava ukupne vrijednosti i semantiku potiskivanja |

Zadržavaju se ukupne vrijednosti i oznake potiskivanja, a godišnji i mjesečni
redci ostaju odvojeni kako se ne bi dvostruko brojali. Puni DZS stog ostaje
vanjski; u knjigu ulazi samo ovaj omeđeni izvadak.

## Godina snimke

**Odluka autora: najnovija moguća godina.**

To se čita kao **najnovija cjelovita kalendarska godina koju je DZS objavio u
trenutku dohvata**, prikvačena točnim izdanjem i datumom preuzimanja da poslije
ne klizi. Nepotpuna tekuća godina ne ulazi, jer bi mjesečni niz bio krnj, a
usporedba razdoblja neispravna.

**Ovaj gate namjerno ne imenuje godinu.** Gate koji ne dohvaća podatke ne može
znati što je objavljeno, a imenovati godinu značilo bi iznijeti tvrdnju o objavi
koju ovaj paket nije provjerio. Godinu, izdanje, datum i kontrolni zbroj
prikvačuje `P3-DZS` kad datoteku doista dohvati.

Ako se pri dohvatu pokaže da najnovija cjelovita godina nije objavljena u obliku
koji zadovoljava odabir, `P3-DZS` staje i vraća pitanje ovome gateu umjesto da
sam spusti kriterij.

## Prava i traka

Traka ostaje **`bundled`** i ne mijenja se ovom odlukom; `data/katalog.yml` je
već tako bilježi.

Temelj je dvostruk. Inventar `P1B-DATA-LIC` utvrdio je da DZS izričito navodi da
su svi njegovi mrežni skupovi dostupni pod Hrvatskom otvorenom dozvolom, koja
traži navođenje izvora, datuma posljednje izmjene, URI-ja i oznake promjena. Uz
to, autorova odredba od 5. kolovoza 2026. utvrdila je da je odabrani izvadak
javno dostupan i da dopuštenje nije potrebno tražiti.

**Granica koja se ne prelazi.** Utvrđen je **opći** pravni temelj, ne točan
paketni zapis. Ovaj gate zato ratificira traku i odabir, a ne promociju.
Promocija traži da `P3-DZS` zabilježi točno izdanje, datum preuzimanja, niz
atribucije, kontrolni zbroj i usklađenje s objavljenim ukupnim vrijednostima.
Bez toga katalog pada zatvoreno, što je već strojno provjereno.

**Knjiga ne smije tvrditi da je pribavila dopuštenje nositelja prava**, jer ono
nije traženo. Smije navesti izvor i njegove objavljene uvjete.
`H-P1B-DATA-LIC-003` nije nadomješten.

## Uloga u knjizi i granica tvrdnji

Paket služi poglavlju 3 kao jedna sljediva javna tvrdnja koju čitatelj rastavlja.

Dopuštene tvrdnje: opis zabilježenih dolazaka i noćenja, i usporedba razdoblja
uz istu definiciju.

Nedopuštene tvrdnje: uzročnost, zaključak o pojedinačnom gostu iz agregata, i
svaka usporedba koja miješa godišnje i mjesečne retke ili dvije geografske
razine bez imenovanja nazivnika.

Zamjena za obvezni studentski put ostaje zabilježena u katalogu i ne mijenja se:
dok `P3-DZS` ne prođe, obvezni zadatak koristi licencno čist generirani paket ili
njegov agregat.

## Razmotrene alternative

Šest je alternativa razmotreno i odbijeno.

1. **Imenovati konkretnu godinu u ovom gateu.** Odbijeno: gate ne dohvaća
   podatke i ne može provjeriti što je objavljeno.
2. **Uzeti tekuću, nepotpunu godinu jer je „najnovija".** Odbijeno: krnj mjesečni
   niz i neispravna usporedba razdoblja.
3. **Uzeti puni DZS stog umjesto omeđenoga izvatka.** Odbijeno: ratificirani plan
   drži puni stog vanjskim, a veličina ne služi nijednoj pouci.
4. **Promovirati paket ovdje, jer je pravni temelj utvrđen.** Odbijeno: opći
   temelj nije paketni zapis, a promocija traži izdanje, zbroj i usklađenje.
5. **Spustiti traku na `portal-mediated` iz opreza.** Odbijeno: Hrvatska otvorena
   dozvola je izričita i autorova odredba stoji, pa bi oprez ovdje bio netočan.
6. **Dodati drugu DZS domenu u prvo izdanje.** Odbijeno: `dzs_drugi_domen` ostaje
   odgođen za drugo izdanje i nije potreban za nijedan obvezni put.

## Granica autoriteta

Ova odluka ovlašćuje `P3-DZS` da izgradi i provjeri omeđeni paket prema ovdje
prihvaćenom odabiru. Ne ovlašćuje ništa drugo.

Ne dohvaća i ne stvara nijednu datoteku, ne mijenja `data/katalog.yml`, ne
promiče nijedan paket, ne mijenja nijednu drugu traku i ne otvara nijedan drugi
`G-A3` gate. Ne mijenja prozu nijednoga poglavlja. Ne tvrdi nikakvo dopuštenje
nositelja prava. Ne odobrava render, generirani artefakt, push, merge, tag,
arhiviranje, deployment ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

| Stavka ili paket | Stanje nakon ovoga gatea |
|---|---|
| `R08-DZS-package` | odblokirana za `P3-DZS` |
| `P3-DZS` | sljedeći dopušteni paket |
| `dzs_turizam` u katalogu | traka potvrđena, promocija i dalje zabranjena do `P3-DZS` |
| `OA-G-A3-DZS-SELECTION` | `done`, bez ijedne poslane vanjske poruke |
