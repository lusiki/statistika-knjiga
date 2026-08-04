# P2-CLAIMS — kanonska intelektualna arhitektura

**Paket:** `P2-CLAIMS`

**Datum:** 4. kolovoza 2026.

**Ishod:** prihvaćena je kanonska arhitektura tvrdnji, životnog ciklusa,
knjižnih niti, etike i podatkovne znanosti, točno unutar odluke `G-A2a`.

## Autoritet, ulaz i granica

Jedini urednički autoritet jest prihvaćena odluka `G-A2a`, vezana uz
`conversation:G-A2a-governing-system-approved-2026-08-04-Luka-Sikic`.
Prije prve sadržajne izmjene na `before_start` gateu priznat je handoff
`H-G-A2A-001`. Pri zatvaranju je potrošen dispozicijom da se svih 22
upravljanih stavki prenosi u jedan sustav, bez proširenja ovlasti.

Izravni izvori za prijenos bili su odluka `G-A2a`, njezine 22 stavke u
provedbenom registru, ugovor `packet_contracts.shared_architecture` te § 12
izvještaja `comprehensive-book-review-2026-07-31.md`. Arhitektura obuhvaća:

- šest dimenzija tvrdnje i šest pitanja za reviziju;
- devet faza životnog ciklusa i uloge pet dijelova knjige i završnice;
- sedam ponavljajućih niti s ulogama sijanja, razvoja i žetve te izričitim
  isključenjima;
- standard poštene rečenice, karticu za čitanje ankete i usporedbu primarne
  analize s jednom obranjivom alternativom;
- četiri aktivnosti, četiri vrste dokaznog objekta, etiku obične analitičke
  prakse i osam tipova dizajna nastanka podataka.

Paket nije mijenjao prozu poglavlja, nije ratificirao kostur poglavlja ili
terminologiju, nije riješio ugovor provjere znanja ni preduvjete Poglavlja 17
te nije odabrao ili promaknuo podatkovni paket. Nije pokrenut render, objava,
upload ni deployment.

## Kanonski zapisi

Jedini promjenjivi Bookwright izvor ostaje checkout-local direktorij
`bookwright_plugin/bookwright/shared/`. Postojeći četveroregistarski model nije
proširen petim registrom. Umjesto toga, `conventions.json` sada ima strogo
validiran objekt `intellectual_architecture`, unutar kojega su kanonski
registri:

- `claim_registry`;
- `lifecycle_registry`;
- `thread_registry`;
- `ethics_registry`;
- `data_science_registry`.

Njihov kanonski digest, dobiven iz deterministički serijaliziranog objekta
`intellectual_architecture`, jest
`sha256:30e105082ac37f09b40667f6a9a3f4a70345cca4ed16004a09fd483d79816ef8`.
Puna datoteka `conventions.json` ima
`sha256:2132eed75bf5be671bd58da193898c47dcadfaae2349546d92828d920d400abb`,
a shema `conventions.schema.json`
`sha256:38a4bdec948d3171f4c6fedce03b92dc7b9b2914fa0c29bb54f51b03396294c6`.

Shema zahtijeva upravo odluku `G-A2a`, 22 jedinstvene stavke, potpune granice
ovlasti i sve pet registarskih grana. Dodatni deterministički provjerivač
`scripts/check-book-architecture.py` ima
`sha256:58eba81c919ec7df90937148601a9bb2340dfa9fbcd3ab816d0416d0bd1ae600`
i provjerava i shemu i semantičke invarijante prihvaćenog sustava bez nove
vanjske ovisnosti.

## Niti i kontrola opsega

Svaka nit dobila je izričita mjesta i uloge za `plant`, `develop` i `harvest`
te barem jedno isključenje:

| Nit | Sijanje | Razvoj | Znatna žetva |
|---|---|---|---|
| Jedinica analize | 1–2 | 4, 8, 13–14 | 17–18 |
| Selekcija i odsutnost | 2–3 | 6, 8, 12 | 17–18 |
| Nazivnik | 1–3 | 4–5, 13 | 17–18 |
| Proračun nesigurnosti | 2 | 8–12 | 16–18 |
| Posljedice pogreške | 3, 7 | 10–11 | 17–18 |
| Reproducibilnost i podrijetlo | 4–5 | 12 | 18 |
| Komunikacija tvrdnje | 4 | 9, 11, 16 | 18 |

Tablica određuje arhitektonsku ulogu, a ne ratificirani kostur ili gotov tekst.
Globalno pravilo ostaje: kratko sjeme, jedna znatna žetva i kasniji dohvat.
Kasnija pojavljivanja ne smiju postati ponavljane mini-lekcije. Sustav ne
stvara novo numerirano poglavlje, središnji widget ni vrstu callouta.

## Životni ciklus, tvrdnje i podatkovna znanost

Životni ciklus je stabilan slijed `question`, `acquire`, `validate`, `prepare`,
`explore`, `model`, `evaluate`, `communicate`, `monitor`. Uvodi se u Poglavlju
1; predgovor samo izriče obećanje i upućuje čitatelja. Naglasci dijelova
kumulativni su i neisključivi. Vjerojatnosno uzorkovanje za generalizaciju ne
zamjenjuje odvajanje treninga, validacije i testa, niti obratno.

Karta tvrdnji razlikuje opis, povezanost, generalizaciju, predviđanje,
uzročnost i odluku. Doseg na populaciju zasebna je os, ne sinonim vrste
tvrdnje. Audit pita o jedinici opažanja, odsutnosti i selekciji, cilju i vrsti
tvrdnje, obuhvaćenoj i izostavljenoj nesigurnosti, razumnoj alternativi te
posljedicama pogreške.

Podatkovna znanost ostaje način ostvarivanja četiriju postojećih obećanja, a
ne peto obećanje ili novo tehničko poglavlje. Omjer `70/20/10` zapisan je
isključivo kao približna, neobvezujuća urednička dijagnostika: nije kvota,
formula broja stranica ni razlog da se sadržaj zahtijeva ili odbije. Statistika,
podatkovna znanost, strojno učenje i sustavi umjetne inteligencije ostaju četiri
različite aktivnosti s vlastitim vodećim pitanjem.

Osam tipova dizajna organizirano je po načinu nastanka podataka, ne po
disciplini ili broju skupova. Svaki kandidat nosi oznaku svojega točnog
kasnijeg gatea. Prioritet tekstualnog paketa nad neobveznim WDI proširenjem,
uvjetnost V-Dema i niži prioritet COVIDiSTRESS-a ako je opseg tijesan zapisani
su kao arhitektura portfelja, ne kao odabir ili promocija paketa.

## Etika i dokazni objekti

Etika je ugrađena u definiranje kategorija, izostavljanje, objavu malih ćelija,
proxy-varijable, izbor modela, komunikaciju i raspodjelu pogrešaka. Nije
ograničena na privatnost, otvorenu znanost ili algoritamsku pravednost.

Registar strogo razlikuje simulaciju s poznatim mehanizmom, sintetičke podatke,
modelom generirane hipotetske odgovore i izmišljena empirijska opažanja. Za
svaki objekt navodi dopuštenu uporabu i zabranjenu tvrdnju. Generirani
ispitanici ne mogu poduprijeti populacijsku tvrdnju, a izmišljena opažanja ne
mogu poduprijeti nikakvu empirijsku tvrdnju.

## Provjere i budući učinci

`python scripts/check-book-architecture.py` prolazi: JSON je valjan prema
shemi, svih 22 stavki prisutno je u stabilnom redoslijedu, svih sedam niti ima
potpune uloge i isključenja, `70/20/10` je neobvezujući, nijedan paket podataka
nije odabran, a nula od 19 kostura poglavlja ostaje ratificirano.
`python -m json.tool` prolazi za registar i shemu, a `git diff --check` nema
nalaza.

Paket nije otkrio novi učinak važan budućem paketu koji već nije izražen
postojećim ovisnostima i gateovima. Zato nema novog izlaznog handoffa:
potrošači već ovise o `P2-CLAIMS`, a prava i odabir svakog paketa, kosturi,
terminologija, procjena znanja i preduvjeti Poglavlja 17 ostaju na svojim
točnim kasnijim gateovima.

Nakon zajedničkog zatvaranja registra, handoff ledgera i nadzorne ploče
workflow validator prolazi s `active packet: none`, `next permitted packet:
G-A2d`, 371 atomskom stavkom i 36 handoffova. Obje obvezne in-memory negativne
probe završavaju kodom 1 iz točnoga razloga:

```text
EXPECTED_FAILURE fixture=generic_packet_evidence exit=1
Terminal packet completion_evidence must be a structured mapping: G-A0

EXPECTED_FAILURE fixture=invalid_outside_ask_link exit=1
Outside ask OA-G-A1A-C10-SPEC links unknown items: R99-NOT-A-REGISTER-ITEM
```

Time su dokazani pozitivni i fail-closed kontrolni put. `P2-CLAIMS` je
zatvoren, a `G-A2d` je samo sljedeći dopušteni paket i nije pokrenut.
