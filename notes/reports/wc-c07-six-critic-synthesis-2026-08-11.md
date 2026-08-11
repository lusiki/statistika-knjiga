# WC-C07 — sinteza šest kritičara

**Konačni izvor:** `chapters/07-vjerojatnost.qmd`

**Konačni SHA-256:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Šest neovisnih kritičara samo za čitanje pregledalo je isto zaključano
materijalno stanje. Svaki je potvrdio isti hash prije i nakon pregleda; nijedan
nije uređivao datoteke. Ovo je preporuka panela, a ne autorsko prihvaćanje C07.

## Popravci prije zaključavanja panela

Prvi kritičarski krug i izvršna provjera otkrili su nekoliko blokirajućih
granica. Prije konačnoga panela ispravljeni su opće pravilo množenja i njegov
prečac uz neovisnost, značenje osobne sigurnosti i kalibracije, uvjeti i doseg
CLT-a, nulti model vruće ruke, lažni A/B naziv jednoruke kampanje te uzročna i
odlukovna granica razrađenoga primjera.

Widget je dobio izvršivu SVG semantiku, dinamičan naslov i opis, živu regiju sa
sredinom i središnjih 90 % rezultata te izvodiv zadatak. Skriveni i vidljivi
račun e-biltena usklađeni su na sjeme 709, QQ prikaz dobio je lokalno sjeme 710,
a AI okvir zadržava točno jednu pogrešku. Stanka prisjećanja premještena je na
stvarnu sredinu, most od indikatora 0/1 do raspodjele stopa izrečen je, a
`R35-REACHBACK-07` sada zahtijeva brojnosti i svih šest revizijskih pitanja iz
poglavlja 3 uz kanonsko zatvaranje.

Nakon tih popravaka izvor je zaključan. Nijedan završni nalaz nije potaknuo
novu promjenu teksta, pa svi izvještaji i svi renderi ostaju vezani uz isti
hash.

## Zajednička dispozicija

Svih šest perspektiva slaže se u sljedećem:

- nema fatalnoga ni velikoga nalaza;
- `R10-C07-degree-belief`, `R29-C07-retrieval-load` i
  `R35-REACHBACK-07` materijalno zadovoljavaju ratificirane testove;
- prihvaćeni `R09-C07-clt-conditions` ostaje očuvan;
- simulacija prethodi formalizaciji, pet definicijskih blokova odgovara
  kralježnici, a sedmodijelni kostur i četiri razine zadataka ostaju cjeloviti;
- neovisnost, nulti model, podudarnost izračuna, uzročna tvrdnja i odluka imaju
  odvojene granice;
- citati, podrijetlo podataka, brojke i zaokruživanja imaju provjerljiv trag;
- C07 mora ostati zaseban autorski gate i panel ne smije sam prihvatiti stavke
  niti poglavlje.

## Rezultati po perspektivi

| Perspektiva | Sažeta ocjena | Fatalni | Veliki | Manji | Korisni |
|---|---:|---:|---:|---:|---:|
| metode | 4–5/5 | 0 | 0 | 1 | 1 |
| skepticizam | 4–5/5 | 0 | 0 | 2 | 1 |
| pedagogija | 4–5/5 | 0 | 0 | 5 | 2 |
| dokazi i citati | 5/5 | 0 | 0 | 0 | 0 |
| hrvatski stil | 4/5 | 0 | 0 | 11 | 3 |
| struktura | 4–5/5 | 0 | 0 | 1 | 1 |
| **zbroj zapisa** |  | **0** | **0** | **20** | **8** |

Zbroj je broj zapisa u pojedinačnim izvještajima, ne broj jedinstvenih
problema: nekoliko se prijedloga preklapa, osobito oko rane terminologije,
normalne aproksimacije, QQ prikaza, dvodijelnoga konceptualnog zadatka i
čitateljskoga naziva `populacija_medija`.

## Otvoreni neblokirajući nalazi

### Metodološka i skeptička preciznost

- Omeđiti zvonasti opis binomne raspodjele na dovoljno dugačke nizove i
  prikladne vrijednosti `p`.
- Oznaku vodoravne osi QQ prikaza učiniti preciznijom.
- Vignetinu formulaciju „bez ijednog razloga” vezati uz odsutnost sustavne
  promjene procesa.
- Korisnost normalne orijentacije ograničiti na središnji dio, ne repove i
  pragove odluke.
- Relevantnu minimalnu razliku odrediti prije gledanja rezultata.

### Pedagoška sidra i zadaci

- U ranim pojavama neovisnosti i uvjetne vjerojatnosti prvo dati običan opis.
- Početniku kratko objasniti zašto binarni ishod ima konačnu varijancu.
- Izreći naziv „QQ prikaz” u tijelu prije popisa pojmova i zadatka.
- Podijeliti konceptualni tier na dvije udaljene cjeline.
- Projekciju rješenja za povratni zadatak oblikovno uskladiti sa zatraženom
  tablicom od šest redaka.
- Razmotriti običniji jezik za „nulti model” i „jednostranu repnu
  vjerojatnost” te čitateljski naziv simulirane populacije.

### Hrvatski rukopisni prolaz

Stilski kritičar bilježi jedanaest lokalnih minor skupina: tvrde rekcije i
kolokacije u uvodu vjerojatnosti; interni naziv skupa i personifikaciju
poglavlja; tri kolokacije u uvjetnim udjelima; prevedene glagolske konstrukcije
u prijelazu prema widgetu; „dohvat” i personifikaciju ishoda; ponavljanje i
neprirodne izraze u CLT odlomku; dvije vidljive uredničke skele; personifikacije
u opisu raspodjela i QQ prikaza; ponavljanje naslova i definicije slučajnoga
niza; razgovorni ili meta-strukturni registar u raspravi pristranosti; te tri
izolirane standardnojezične konstrukcije pri kraju. Tri korisne dorade odnose
se na registar vinjete, dosljedan izraz za zaključivanje prema modelu i naziv
pravila 68, 95 i 99,7 %. Točne lokacije i formulacije ostaju u stilskom
izvještaju.

### Strukturna preciznost

- Uvod widgeta preusko opisuje samo središnju usporedbu, premda dodatne
  kontrole mijenjaju scenarij, `p` i broj ponavljanja.
- Konceptualni zadatak bio bi pregledniji s podzadacima (a) i (b).

## Dokazni dug izvan paketa

Dokazni pregled ne nalazi problem u zaključanom poglavlju. Dodatak C i jedna
`fallback` formulacija u katalogu zaostaju za kanonskim stanjem
`populacija_medija`. To je postojeća obveza `P5-C` kroz
`H-P3-CATALOG-002`; WC-C07 je ne duplicira i ne mijenja tuđi opseg.

Odvojeni kontrolni audit, koji nije sedma kritičarska leća poglavlja, pronašao
je nepodudaranje budućih preduvjeta: četiri WC-C08 stavke zahtijevaju još
ratificirani `P3-ESS` koji u registru dolazi poslije WC-C08. Nalaz je zapisan u
`H-WC-C07-WC-C08-PREREQUISITE-001`. Ne mijenja ocjenu Chapter 7 ni mogućnost
C07 odluke, ali zabranjuje claim WC-C08 bez zasebno autoriziranoga rješenja.

## Dispozicija i preporuka panela

Panel preporučuje prihvatiti WC-C07 kao dovršen vertikalni rez i predati
zaključani izvor zasebnom C07 autorskom/editorijalnom gateu. Dvadeset minor i
osam useful zapisa ostaju javno vidljivi kao neblokirajuće mogućnosti za neki
budući, posebno autoriziran kontinuirani prolaz. Njihovo popravljanje sada bi
promijenilo izvor nakon završnoga panela i poništilo zajednički dokazni hash.

`R10-C07-degree-belief`, `R29-C07-retrieval-load` i `R35-REACHBACK-07` zato
ostaju `ratified`, a Chapter 7 ostaje `draft` do točnoga datiranog odgovora
autora na C07. Ranije prihvaćeni `R09-C07-clt-conditions` ostaje `accepted`.
