# WD-C13 — sinteza šest kritičara

Svih šest neovisnih read-only leća pregledalo je isti zaključani izvor:

- putanja: `chapters/13-kategoricki-podaci.qmd`
- SHA-256: `6cd97e3dae0a83dcf3daa8f7450fac0324390ef14b7df87308a29a6caa240015`
- git blob: `9b7b44cc7376c12814c47090c0215879df5112b5`

Pokriveni su statističke metode, skepticizam, pedagogija, dokazna osnova,
hrvatski rukopisni stil i struktura. Mehanički prelet prije panela imao je nula
stilskih i strukturnih kandidata, sve uvedene figure, svjež graf pojmova, četiri
valjana citatna ključa i prolaz ciljanog HTML prikaza.

## Ishod prvoga prolaza

| Težina | Broj združenih nalaza |
|---|---:|
| Fatalno | 2 |
| Major | 6 |
| Minor zapisi po lećama | 13 |

Poglavlje još ne prolazi `WD-C13`. Fatalni i major nalazi moraju biti
popravljeni uz autorovo odobrenje, a zatim cijeli izmijenjeni izvor mora dobiti
svježih šest neovisnih pregleda.

## Obvezni nalazi, združeni po problemu

1. **Fatalno — smjer p-vrijednosti u kanonskom rješenju.** Rješenje usađene
   pogreške kaže da p-vrijednost raste s veličinom uzorka. Pri istim postotcima
   hi-kvadrat raste, a p-vrijednost pada. Rješenje zato samo uvodi novu
   statističku pogrešku.
2. **Fatalno — neodbacivanje kao potvrdan dokaz slaganja.** Test prilagodbe
   tumači p-vrijednost kao dokaz da uzorak dobro odražava populacijsku
   strukturu. Dopušten je samo zaključak da nije otkriven jasan nesklad s
   poznatim simuliranim udjelima; potvrdna blizina traži zasebno prikazane
   razlike ili intervale.
3. **Major — Fisherov egzaktni test kao brojanje tablica.** Moguće tablice s
   fiksnim rubovima nisu jednako vjerojatne. Opis mora govoriti o enumeriranju i
   zbrajanju točnih uvjetnih, hipergeometrijskih vjerojatnosti prema unaprijed
   određenom pravilu ekstremnosti.
4. **Major — prekodiranje i neusporedivi Cramérovi V.** Puna tablica nema rijetke
   očekivane ćelije, a binarna varijabla odgovara na drugo pitanje i mijenja
   normalizaciju V. Prekodiranje ne smije izgledati kao rezultatno vođeno
   uklanjanje ćelija niti veći V kao dokaz bolje ili jače verzije iste veze.
5. **Major — neizvjesnost izostaje iz završnog izvještaja.** Ugovor Dijela V
   obećava očuvanu neizvjesnost, ali razrađeni primjer uz glavni kontrast daje
   samo postotke, V i test. Glavni kontrast treba dobiti interval neizvjesnosti
   i zaključak omeđen tim intervalom.
6. **Major — uloge alata u povratku Berkeleyju.** Nije svaki postupak iz
   poglavlja test globalnog nesklada s neovisnošću. Treba imenovati hi-kvadrat
   test nezavisnosti, a V i reziduale ostaviti kao mjeru jačine i lokalizaciju.
7. **Major — upravljački ton ESS odlomka.** „Obvezni lokalni put”, „ruta” i
   „knjiga ne nosi” prekidaju rukopisni glas, a navedena ruta iz Dodatka C ne
   postoji. Analitička granica treba ostati, ali iz perspektive čitateljeva
   rada na lokalnom simuliranom skupu ili vlastitoj portalnoj kopiji ESS-a.
8. **Major — statički blizanac ne nosi cijeli argument widgeta.** Digitalni
   prikaz mijenja relativni pomak i rubne zbrojeve te prikazuje hi-kvadrat i V;
   statički prikaz mijenja samo pomak. Tiskani čitatelj zato ne vidi da isti
   relativni pomak mijenja hi-kvadrat s veličinom ćelije, dok V ostaje isti.

## Predložena ograničena dorada

Ako autor odobri obvezne nalaze, `WD-C13` će napraviti samo sljedeće:

1. ispraviti kanonsko rješenje: pri stalnim postotcima veći uzorak daje veći
   hi-kvadrat i manju p-vrijednost, dok jačinu opisuju V i sadržajni kontrasti;
2. drugi test prilagodbe opisati kao izostanak otkrivenoga nesklada, uz
   neposredan prikaz najvećega opaženog odstupanja udjela od poznate simulirane
   populacije;
3. Fisherov postupak opisati kao zbroj točnih uvjetnih vjerojatnosti mogućih
   tablica prema unaprijed zadanom pravilu ekstremnosti;
4. binarni rez digitalno/tradicionalno imenovati kao unaprijed određeno drugo
   pitanje s jasnim pravilom klasifikacije; ukloniti razlog rijetkih ćelija i
   jezik „pojačavanja”, a peterokategorijski rezultat zadržati kao usporedbu
   osjetljivosti bez rangiranja dvaju V;
5. glavnom kontrastu udjela digitalnih izvora između najmlađe i najstarije
   skupine dodati 95-postotni interval te tumačenje ograničiti na njega;
6. u Berkeleyjevu povratku imenovati samo hi-kvadrat test nezavisnosti kao
   globalni test, uz zasebne uloge V i reziduala;
7. ESS odlomak prepisati u rukopisni glas: glavni primjer radi na lokalnom
   simuliranom skupu, a čitateljeva vlastita ESS analiza traži valjani nazivnik
   i `anweight`, bez tvrdnje o nepostojećoj ruti u Dodatku C;
8. statički blizanac dati u tri panela: bez odstupanja, 20-postotni pomak uz
   rubni zbroj 20 i isti pomak uz rubni zbroj 80; uz panele prikazati ukupni
   hi-kvadrat i Cramérovo V, tako da V ostane 0,20 u oba pomaknuta stanja.

Time se ne odobrava nijedan samostalni minor zahvat. Minori ostaju vidljivi za
`C13`, osim ondje gdje ih obvezna dorada nužno ukloni.

## Suglasnost i nesuglasnost panela

- Sve leće potvrđuju stvarni Berkeley otvarač, ugovor Dijela V, mjernu granicu
  kodiranoga teksta, reach-back prema Simpsonovu paradoksu i očuvanu ESS
  licencnu granicu.
- Dokazna leća reproducirala je sve brojke i nije pronašla izmišljeni citat,
  izvor ili rezultat.
- Metodološka i skeptička leća neovisno su pronašle prejak zaključak testa
  prilagodbe i problem prekodiranja.
- Pedagoška leća predlaže formalni `#def-` blok za uvjetni nazivnik, dok
  strukturna leća njegov prozni status smatra opravdanim. Budući da je riječ o
  minor nesuglasnosti i kralježnica već ograničava izbor definicija, taj se blok
  ne predlaže za ovu doradu.

## Nedostaje ili nije provjereno

- Nema nedostajućega bibliografskog ključa ni nereproducirane brojke.
- Nisu potkrijepljene opće tvrdnje o učestalosti izostavljanja nazivnika,
  raširenosti pravila pet i tipičnom ponašanju AI-asistenata.
- Dodatak C trenutačno nema opisanu ESS rutu; dorada neće tvrditi da je ima.

Završna presuda ostaje otvorena do autorova odobrenja ograničene dorade i
svježega šestokritičarskog prolaza nad konačnim izvorom.

## Autorsko odobrenje dorade

Autor je 17. kolovoza 2026. odobrio točno osam združenih dorada i odgodio sve
samostalne minore doslovnim odgovorom:

```text
Odobravam osam WD-C13 dorada; samostalne minore ostaviti za C13.
```

Nijedan samostalni minor nije uređen. Dokazni minor o lažnoj ESS ruti nužno je
nestao unutar sedme odobrene dorade; to nije zaseban dodatni zahvat.

## Konačni izvor i provedba osam dorada

- SHA-256: `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`
- git blob: `e7ff4e8adc9d2438461ffbddb01e193aba24b671`

Konačni izvor ispravlja smjer p-vrijednosti, ograničava GOF neodbacivanje,
točno objašnjava Fisherov uvjetni račun, prekodiranje predstavlja kao novo
unaprijed određeno pitanje, glavnom kontrastu dodaje 95-postotni interval,
razdvaja Berkeleyjeve uloge testa/V/reziduala, ESS vraća u čitateljski glas bez
lažne rute te statičkom blizancu daje isti argument o uzorku i V kao digitalnoj
inačici.

Izmjena tiskane inačice zahtijevala je usklađivanje `data/widgets.json#w13` s
novim R hashom i trima zlatnim scenarijima. Widget ugovor i paritet prolaze bez
širenja tolerancije.

## Završni šesteročlani panel

Svih šest kritičara ponovno je read-only pročitalo cijeli isti konačni izvor.

| Težina | Broj zapisa po lećama |
|---|---:|
| Fatalno | 0 |
| Major | 0 |
| Minor | 14 |

Raspodjela minora jest metode 1, skepticizam 2, pedagogija 3, dokazi 4, stil 4
i struktura 0. Svih šest leća izrijekom potvrđuje svih osam odobrenih dorada i
prolaz bez fatalnoga ili major nalaza.

Preostali minori ostaju vidljivi za `C13`: preciznost rubnih zbrojeva; izraz
„pravi” nazivnik i hipotetska urednička odluka; rana pojava V, čitljivost
vidljive pripreme računa i zadatak o uvjetnom nazivniku; preširoko podrijetlo
svih brojki te tri nepotkrijepljene tvrdnje o učestalosti; formatno specifičan
prijelaz, antecedent mjerne granice, prikriveni popis i redoslijed pojmova.
Broj 14 označava zapise po lećama, ne nužno 14 neovisnih defekata.

## Konačna presuda

`WD-C13` prolazi šesteročlani panel. Svih osam odobrenih dorada riješeno je na
istom konačnom izvoru; nema fatalnoga ni major nalaza. Četrnaest samostalnih
minora nije uređeno niti se smatra autorom prihvaćenim prije zasebnoga `C13`
gatea.
