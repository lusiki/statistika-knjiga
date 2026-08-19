# Licenca i atribucija — `parlament_oznake.csv`

Kataloški paket: `parlasent`.

Datoteka `data/parlament_oznake.csv` prilagodba je skupa **The multilingual
sentiment dataset of parliamentary debates ParlaSent 1.0** autora Michala
Mochtaka, Petera Rupnika, Katje Meden i Nikole Ljubešića, koji je objavio Jožef
Stefan Institute u zapisu <http://hdl.handle.net/11356/1868>.

Izvor i ova prilagodba distribuiraju se pod licencom **Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**:
<https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

## Izvorne datoteke

- `ParlaSent_BCS.jsonl`, ParlaSent 1.0, objavljeni MD5
  `c8b59c84c476b031cc553bc3c768e627`, lokalno potvrđeni SHA-256
  `c6a6f51a819941c19f148405ed83adbabc38e3333305a44a7149b23d99b1cc98`;
- `ParlaSent_BCS_test.jsonl`, ParlaSent 1.0, objavljeni MD5
  `ee8699a4a7b1a834f79fe74b8ebdfaf1`, lokalno potvrđeni SHA-256
  `412b3ba399dab24041ff11a0eb1d530b402511615c8206cb1838092bc22ea7a0`;
- `README.txt`, ParlaSent 1.0, objavljeni MD5
  `583856c8d470334e5638f6a078f727d5`, lokalno potvrđeni SHA-256
  `848a892cede62d37f469532eba6d2f5e6f00d29234f0257a67737f8a8646c285`.

## Označene promjene

Prilagodba je nastala 18. kolovoza 2026. i uključuje samo ove promjene:

1. zadržani su svi retci s doslovnom izvornom vrijednošću `country = HR`;
2. iz datoteke za učenje uklonjeni su cijeli dokumenti čiji se
   `document_id` pojavljuje u izvornoj ispitnoj datoteci;
3. preostali dokumenti deterministički su razdvojeni na skup za učenje i skup
   za provjeru javno opisanom SHA-256 funkcijom;
4. izvorna ispitna datoteka zadržana je kao skup za ispitivanje;
5. polja su preimenovana i poredana u UTF-8 CSV-u s LF završecima redaka;
6. nedostupni drugi koder, usklađenje i izvorni split ispitnih redaka označeni
   su doslovno kao `nije_dostupno_iz_izvora`;
7. dodani su izvedeni skup i polje `label_path`, bez promjene izvornoga teksta
   rečenice ili zabilježene oznake.

Promovirana datoteka ima MD5 `55b1c4263009ab783911f094907312d9` i SHA-256
`0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`.

Kod graditelja i provjera ostaje pod licencom repozitorija. Ta licenca ne
obuhvaća podatke treće strane i ne mijenja ShareAlike obvezu ove datoteke.
Nije traženo niti dobiveno posebno dopuštenje nositelja prava; osnova
redistribucije jest objavljena CC BY-SA 4.0 licenca.
