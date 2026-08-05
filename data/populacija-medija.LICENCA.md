# Licenca i obavijest uz snimke skupa `populacija_medija`

Ova obavijest putuje uz datoteke `populacija-medija.csv` i
`populacija-medija-agregat.csv` i mora ostati uz njih pri svakom dijeljenju,
preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `populacija_medija` |
| Datoteke | `populacija-medija.csv` (analitička), `populacija-medija-agregat.csv` (agregatna) |
| Nositelj prava | Luka Sikic, 2026. |
| Licenca | [Creative Commons Imenovanje 4.0 međunarodna (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) |
| Izvor | `R/podaci-nastavni.R`, funkcija `simuliraj_populaciju`, 50 000 opažanja, sjeme 8001 |
| Snimatelj | `scripts/build-data-snapshots.R` |
| Puna obavijest | [`LICENCA-generirani-podaci.md`](LICENCA-generirani-podaci.md) |

Primjer atribucije glasi „Luka Sikic, *Osnove statistike za društvene
znanosti*, `populacija_medija`, generirano skriptom `R/podaci-nastavni.R`, CC
BY 4.0; izmjene su označene.”

Pri dijeljenju ili prilagodbi treba navesti nositelja prava, knjigu, ime skupa,
generator, poveznicu na licencu i **oznaku svake izmjene**.

Licenca se odnosi na podatke. Kod generatora, izvorni tekst knjige i pridružena
dokumentacija ostaju pod MIT licencom repozitorija, a materijali trećih strana
vode se pod vlastitim uvjetima i ova ih obavijest ne obuhvaća.

**Ovo nije mjerenje.** Grad iz kojega ova populacija dolazi ne postoji, a sve
su vrijednosti proizvod generatora slučajnih brojeva. Nastavna vrijednost skupa
leži upravo u tome što je izmišljen: samo za izmišljenu populaciju smije se
reći koliki joj je prosjek prije nego što se uzme ijedan uzorak.

## Napomena o preciznosti i o nuli

Analitička datoteka drži cjelobrojne vrijednosti onako kako ih generator
proizvodi. Stupac `spremnost_platiti` ima mnogo stvarnih nula: nula znači da
osoba ne bi platila ništa i nije oznaka nedostajuće vrijednosti. Nedostajućih
vrijednosti u ovim snimkama nema, pa nijedna ćelija nije prazna.

Agregatna datoteka uz svaki udio drži i brojnik i nazivnik, a uz svaki prosjek
i njegov zbroj, pa se svaki redak može provjeriti ručno. Prosjeci su zapisani
punom preciznošću; zaokruživanje postoji samo u prikazu u knjizi.
