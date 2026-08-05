# Licenca i obavijest uz snimke skupa `anketa_mreze`

Ova obavijest putuje uz datoteke `anketa-mreze.csv` i
`anketa-mreze-agregat.csv` i mora ostati uz njih pri svakom dijeljenju,
preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `anketa_mreze` |
| Datoteke | `anketa-mreze.csv` (analitička), `anketa-mreze-agregat.csv` (agregatna) |
| Nositelj prava | Luka Sikic, 2026. |
| Licenca | [Creative Commons Imenovanje 4.0 međunarodna (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) |
| Izvor | `R/podaci-nastavni.R`, funkcija `simuliraj_anketu`, 300 opažanja, sjeme 4001 |
| Snimatelj | `scripts/build-data-snapshots.R` |
| Puna obavijest | [`LICENCA-generirani-podaci.md`](LICENCA-generirani-podaci.md) |

Primjer atribucije glasi „Luka Sikic, *Osnove statistike za društvene
znanosti*, `anketa_mreze`, generirano skriptom `R/podaci-nastavni.R`, CC BY
4.0; izmjene su označene.”

Pri dijeljenju ili prilagodbi treba navesti nositelja prava, knjigu, ime skupa,
generator, poveznicu na licencu i **oznaku svake izmjene**.

Licenca se odnosi na podatke. Kod generatora, izvorni tekst knjige i pridružena
dokumentacija ostaju pod MIT licencom repozitorija, a materijali trećih strana
vode se pod vlastitim uvjetima i ova ih obavijest ne obuhvaća.

**Ovo nije mjerenje.** Ispitanici su izmišljeni po pravilu iz generatora.
Nijedna brojka izvedena iz ovoga skupa ne smije se navesti kao tvrdnja o
stvarnom korištenju društvenih mreža, u Hrvatskoj ni igdje drugdje.

## Napomena o preciznosti

Analitička datoteka drži cjelobrojne vrijednosti onako kako ih generator
proizvodi. Agregatna datoteka uz svaki udio drži i brojnik i nazivnik, a uz
svaki prosjek i njegov zbroj, pa se svaki redak može provjeriti ručno. Prosjeci
su zapisani punom preciznošću; zaokruživanje postoji samo u prikazu u knjizi.
