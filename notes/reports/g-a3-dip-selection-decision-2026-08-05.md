# G-A3-DIP — odabir, prava i uloga podataka DIP-a

**Gate:** `G-A3-DIP`

**Datum odluke:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik, ujedno nositelj podatkovne
politike.

**Dispozicija:** odabir i portalno posredovana traka prihvaćeni su kako je
preporučeno.

**Izvorno stanje odluke:**
`conversation:DIP-selection-and-portal-mediated-route-approved-2026-08-05-Luka-Sikic`.

## Što ovaj gate odlučuje

Gate određuje točan izborni slučaj, redak i skup varijabli, njegovu ograničenu
ulogu u poglavlju 3 te način pristupa koji je dopušten bez dokazane ovlasti za
redistribuciju lokalne kopije.

Gate ne dohvaća datoteku, ne stvara lokalno zrcalo, ne zapisuje kontrolni zbroj,
ne promiče paket i ne mijenja `data/katalog.yml`. `P3-DIP` izrađuje provjerljiv
portalni zapis prema ovoj odluci, ali ne stvara ni ne promiče lokalni podatkovni
paket.

## Ulazi pročitani prije odluke

- `H-P1B-DATA-LIC-003` u cijelosti, potrošen **prije preuzimanja paketa**;
- `H-P3-CATALOG-001`, potvrđen prije prve izmjene i namijenjen potrošnji pri
  zatvaranju;
- inventar `P1B-DATA-LIC`, redak DIP-a 2024. i ugovor triju traka;
- autorova odredba o pravima i ranija predispozicija o traci od 5. kolovoza
  2026.;
- `data/katalog.yml`, zapis `dip_2024`;
- `OA-G-A3-DIP-SELECTION`, `R03-DIP-rights` i `R08-DIP-package`;
- izvještaj `P3-DZS` i njegov `H-P3-DZS-003`, kako se ugovor o promicanju ne bi
  pogrešno prenio na nepromovirani portalni izvor.

## Prihvaćeni odabir

Odabir je **izbor zastupnika u Hrvatski sabor 2024.** Redak omeđenoga nastavnog
izvatka jest jedna službeno objavljena izborna jedinica. Nacionalna službena
ukupna vrijednost služi samo provjeri usklađenja i nije dodatni analitički redak
koji se smije zbrajati s izbornim jedinicama.

Zadržavaju se ove semantičke varijable, pod nazivima koje izvor stvarno objavi:

- oznaka i naziv izborne jedinice;
- broj birača u izvorovu nazivniku;
- broj birača koji su pristupili glasovanju kao brojnik izlaznosti;
- broj važećih listića;
- broj nevažećih listića.

Rezultati izbornih lista, pojedina biračka mjesta i osobni zapisi ne ulaze u
odabir. `P3-DIP` ne smije izmišljati stabilna imena stupaca prije pregleda
izvora: u putovnici preslikava točne izvorne nazive na ovih pet semantičkih
uloga.

## Uloga u poglavlju 3 i granica tvrdnji

Slučaj odgovara na pitanje: **kako se izlaznost mijenja po izbornim jedinicama i
što joj je nazivnik?** Čitatelj provjerava brojnik, nazivnik i učinak agregiranja
prije nego što prihvati postotak.

Dopuštena je samo opisna tvrdnja o službeno zabilježenim agregatima i izlaznosti
uz izričito imenovan nazivnik. Nisu dopuštene tvrdnje o pojedinom biraču,
uzrocima izlaznosti, političkoj potpori listama ni zaključivanje s agregata na
pojedinca. Usklađenje s nacionalnom objavljenom ukupnom vrijednošću jest
kontrola izvora, a ne novi nalaz knjige.

## Prava, pristup i nepromocija

Traka ostaje **`portal-mediated`**. Inventar na pregledanoj službenoj stranici
nije našao izričitu licencu ili drugi temelj za redistribuciju lokalne kopije.
Autorova odredba da su izborni zapisi javno dostupni i da se ne šalje upit za
dopuštenje ne pretvara tehničku dostupnost u redistribucijsku ovlast.

`P3-DIP` je ovlašten za jedan omeđen, datiran i samo-čitajući pregled službenoga
portala. Mora zabilježiti točnu službenu adresu i identitet objave, datum
pregleda, korake kojima čitatelj dolazi do istoga izvora, preslikavanje
semantičkih varijabli te usklađenje s ukupnim vrijednostima koje portal
objavljuje. Ne smije zadržati izbornu datoteku u repozitoriju, u lokalnom zrcalu
paketa ili u izvještaju.

Paket ostaje `promoted: false`. Nema `promoted_by`, nema zapisa u
`promotion_log` i pravila koja `H-P3-DZS-003` postavlja promoviranim paketima ne
aktiviraju se. Postojeći `promoting_gate: G-A3-DIP` zato je neoperativan i
`P3-DIP` ga mora izrijekom ukloniti, a ne premjestiti: nije riječ o odgođenoj
promociji, nego o namjerno nepromoviranom portalnom zapisu.

**Knjiga ne smije tvrditi da je pribavila dopuštenje nositelja prava**, jer ono
nije traženo. Smije navesti službeni izvor i njegove objavljene uvjete.

## Izričita izmjena dokaza za P3-DIP

Ratificirani ugovor `P3-DIP` nastao je uz pretpostavku lokalne datoteke pa traži
kontrolni zbroj, provjeru ključa i šifri nedostajućih vrijednosti nad lokalnim
bajtovima. Autor je odobrio portalni put upravo zato što takva lokalna kopija
nije dopuštena. Zaobići te testove ili izmisliti zbroj bilo bi neprihvatljivo.

Zato se testovi **ne proglašavaju prolaznima**. Njihova je izričita
traka-specifična dispozicija:

- lokalna datoteka, lokalni kontrolni zbroj i lokalna promocija moraju biti
  dokazano odsutni;
- izvorni ključ, nedostajuće vrijednosti i shema opisuju se onoliko koliko ih
  službeni portal prikazuje, bez tvrdnje da su lokalno izvršeni;
- umjesto kontrolnoga zbroja lokalne kopije bilježe se identitet službene
  objave, datum pregleda, točna ruta do izvora i usklađenje s objavljenim
  ukupnim vrijednostima;
- `checksum: null` ostaje istinit zapis, a ne praznina koja se prikriva
  izmišljenom vrijednošću;
- zakonita zamjena ostaje obvezna za svaki zadatak koji mora raditi bez portala:
  provjereni DZS agregat ili generirani kategorički skup.

Ta izmjena vrijedi samo za `dip_2024` pod odobrenom portalnom trakom. Ne slabi
ugovor o kontrolnim zbrojevima za ijedan promovirani paket.

## Razmotrene alternative

1. **Autorovo lokalno zrcalo poput DZS-ova.** Nije odabrano jer takvo zrcalo
   nije dostavljeno, a pravni temelj za njegovu redistribuciju nije dokazan.
2. **Jednokratan dohvat i lokalno pakiranje.** Odbijeno: autor je odabrao
   portalni put bez lokalne kopije.
3. **Promocija pod `G-A3-DIP` ili premještanje `promoting_gate` na `P3-DIP`.**
   Odbijeno: portalno posredovan paket nije promoviran; polje se uklanja.
4. **Izmisliti ili prepisati kontrolni zbroj bez datoteke.** Odbijeno: to ne bi
   bio dokaz o bajtovima koje knjiga posjeduje.
5. **Proširiti odabir na rezultate lista ili biračka mjesta.** Odbijeno: autor
   je odobrio omeđenu ulogu provjere izlaznosti po izbornim jedinicama.
6. **Izbaciti DIP i koristiti samo zamjenu.** Odbijeno: portalni izvor daje
   sljediv domaći primjer, dok zamjena osigurava zakonit i pouzdan obvezni put.

## Granica autoriteta

Odluka ovlašćuje samo `P3-DIP` da izradi datiran portalni put, putovnicu i
izvještaj usklađenja prema prihvaćenom odabiru te da katalog uskladi s
nepromoviranim stanjem uklanjanjem neoperativnoga `promoting_gate`. Ne ovlašćuje
zadržavanje ili distribuciju izborne datoteke, promociju, promjenu druge trake,
uređivanje poglavlja ni tvrdnju o dopuštenju nositelja prava.

Ne odobrava generirani artefakt knjige, push, merge, tag, arhiviranje,
deployment ni objavu.

## Blokirane ovisnosti koje se ovime otključavaju

| Stavka ili paket | Stanje nakon ovoga gatea |
|---|---|
| `R03-DIP-rights` | odblokirana za portalno specifičnu provjeru u `P3-DIP` |
| `R08-DIP-package` | odblokirana kao portalni dokazni paket, ne lokalna snimka |
| `P3-DIP` | sljedeći dopušteni paket |
| `dip_2024` u katalogu | `portal-mediated`, `promoted: false`; neoperativni `promoting_gate` uklanja `P3-DIP` |
| `OA-G-A3-DIP-SELECTION` | `done`, bez ijedne poslane vanjske poruke |
