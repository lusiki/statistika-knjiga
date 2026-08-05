# Licenca i obavijest uz izvatke skupa `dzs_turizam`

Ova obavijest putuje uz datoteke `dzs-turizam-mjesecno.csv`,
`dzs-turizam-godisnje.csv`, `dzs-turizam-zupanije-2025.csv` i
`dzs-putovanja-stanovnistva-2024.csv` i mora ostati uz njih pri svakom
dijeljenju, preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `dzs_turizam` |
| Izvor | Državni zavod za statistiku, područje Turizam |
| Tablice | `BS_TU11` (Tablica 1.1), `BS_TU12` (Tablica 1.2), `T03` (Tablica 3., Turistička aktivnost stanovništva) |
| Licenca | [Hrvatska otvorena dozvola](https://www.data.gov.hr/hr/open-license) |
| Objava uvjeta | [DZS, otvoreni podaci](https://dzs.gov.hr/o-zavodu/pravo-na-pristup-informacijama/otvoreni-podaci/1812) |
| URI izvora | <https://web.dzs.hr/PxWeb/pxweb/hr/Turizam/> (sučelje), <https://web.dzs.hr/PxWeb/api/v1/hr/Turizam> (API) |
| Datum preuzimanja | 27. srpnja 2026. |
| Izvadak izradio | `scripts/build-dzs-extracts.py` |

Primjer atribucije glasi „Izvor: Državni zavod za statistiku, područje Turizam,
tablice BS_TU11, BS_TU12 i T03, <https://web.dzs.hr/PxWeb/pxweb/hr/Turizam/>,
stanje na dan preuzimanja 27. srpnja 2026.; Hrvatska otvorena dozvola; izmjene
su označene.”

## Oznaka izmjena

Hrvatska otvorena dozvola traži navođenje izvora, datuma posljednje izmjene,
URI-ja i **jasne oznake svake promjene**. U ovim datotekama promijenjeno je
točno ovo i ništa više:

1. **Odabir.** Preuzet je omeđeni izvadak, a ne cijela baza: `BS_TU11` samo za
   cjelovite kalendarske godine 2005.–2025., `BS_TU12` samo kao presjek za 2025.
   i `T03` samo za 2024.
2. **Razdvajanje.** Godišnji i mjesečni redci `BS_TU11`-a stoje u dvjema
   datotekama, kako se ne bi zbrojili zajedno.
3. **Okretanje mjera u stupce.** U `T03` su četiri mjere iz jednoga stupca
   vrijednosti prebačene u četiri stupca, pa svaki stupac ima jednu mjernu
   jedinicu. Nijedna vrijednost nije agregirana ni preračunata.
4. **Jedan izvedeni stupac.** `razina` u županijskoj datoteci označuje je li
   redak država ili županija. To nije nov podatak nego oznaka hijerarhije koju
   objavljena tablica prepušta čitatelju.
5. **Kodiranje.** Iz windows-1250 u UTF-8 bez BOM-a, sa završetkom retka LF.

Oznake razina, brojčane vrijednosti i objavljene šifre nedostajućih vrijednosti
prepisane su **doslovno**. Ništa nije zaokruženo, preimenovano ni ujednačeno.

## Šifre nedostajućih vrijednosti

Objavljene šifre ostaju različite jedna od druge i od nule. Značenja su
preuzeta iz dokumentacije uz izvor:

| Šifra | Značenje | Pojavljuje se u izvatku |
|---|---|---|
| `-` | nema pojave; to je stvarna nula, a ne nedostatak podatka | da, u stupcu `izdaci_hrk` |
| `..` | podatak nije dostupan | ne |
| `....` | podatak još nije objavljen | ne |
| `z` | podatak je povjerljiv i potisnut | ne |

`z` i `-` nikada nisu zamjenjivi: potisnutu vrijednost pročitati kao nulu znači
sustavno podcijeniti male jedinice.

## Što ova licenca ne pokriva

Licenca se odnosi na podatke Državnoga zavoda za statistiku. Izvorni tekst
knjige, kod i pridružena dokumentacija ostaju pod MIT licencom repozitorija, a
generirani nastavni skupovi pod svojom CC BY 4.0 licencom; ta se dva režima ne
miješaju.

**Knjiga nije tražila ni dobila dopuštenje nositelja prava** i nigdje ne smije
tvrditi da jest. Navodi izvor i njegove objavljene uvjete, i ništa više.

## Jedinica se zove dolazak, ne osoba

Od 2017. izvor je sustav eVisitor. Statistika broji **dolaske, a ne različite
osobe**: gost koji promijeni smještaj prijavljuje se ponovno i broji se opet.
Brojka za 2025. znači 20 698 963 dolaska, ne 20,7 milijuna ljudi. Noćenja su
stabilnija mjera obujma.
