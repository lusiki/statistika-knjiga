# Licenca i obavijest uz izvatke skupa `bdp_dugi_niz`

Ova obavijest putuje uz datoteke `bdp-hrvatska-izvori.csv`,
`bdp-hrvatska-spojeni.csv` i `bdp-hrvatska-razdoblja.csv` i mora ostati uz njih
pri svakom dijeljenju, preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `bdp_dugi_niz` |
| Licenca izvatka | `CC BY 4.0 za sastav i spojeni niz; pet komponenti nosi vlastite uvjete` |
| Poveznica na licencu | <https://creativecommons.org/licenses/by/4.0/legalcode> |
| Sastavljanje i spajanje | projekt AI.econ / CroAIcon |
| Registar izvora | `data/reference/gdp_sources.json` u repozitoriju CroAIcon |
| Raspon | 1870. — 2025. |
| Izvadak izradio | `scripts/build-croaicon-extracts.py` |

## Pet izvora, pet licenci

Ovaj paket **nije jedan izvor**. Njegovih pet stupaca u
`bdp-hrvatska-izvori.csv` pet su različitih objavljenih procjena, svaka sa
svojom jedinicom, svojim obuhvatom i svojom licencom:

| Stupac | Izvor | Jedinica | Obuhvat | Licenca |
|---|---|---|---|---|
| `eurostat_eur_clv` | Eurostat, nacionalni računi (ESA 2010), `nama_10_pc` | ulančani obujam, euro po stanovniku | 1995.– | ponovna uporaba uz priznanje izvora i propisani disclaimer |
| `maddison_int2011` | Maddison Project Database 2023 | 2011. međunarodni dolar (PPP) | 1952.–2022. | uvjeti MPD-a; traži citiranje izvornih radova |
| `pwt_usd2017` | Penn World Table 10.01 | 2017. USD | 1950.–2019. | CC BY 4.0 |
| `svjetska_banka_usd2015` | Svjetska banka, WDI, `NY.GDP.PCAP.KD` | stalni 2015. USD | 1990.– | CC BY 4.0 |
| `tica_gk1990` | Tica, J. (2004.), *Zagreb International Review of Economics & Business* 7(1):103–133 | Geary-Khamis 1990., autorova rekonstrukcija | 1910.–1989. | otvoreni pristup (Hrčak) |

Citat za Maddison: Bolt, J. i van Zanden, J. L. (2024.). *Maddison style
estimates of the evolution of the world economy: A new 2023 update.* Journal of
Economic Surveys. DOI 10.34894/INZBF2.

Citat za Ticu: Tica, J. (2004.). *The Estimation of 1910–1989 Per Capita GDP in
Croatia.* <https://hrcak.srce.hr/35610>.

## Stanje prava — pročitati prije uporabe

Licenca u tablici gore odnosi se na **sastav i spojeni niz**: odabir, ulančavanje
i sidrenje koje je izveo projekt AI.econ. To je rad autorâ projekta i dijeli se
pod CC BY 4.0. Svaka od pet komponenti i dalje nosi vlastite uvjete iz tablice
iznad i njih ova licenca ne mijenja.

Ovaj paket **još nije promoviran**. Uzvodne su licence povoljne, ali sastavljena
tablica nosi pet skupova uvjeta odjednom, a Eurostatov stupac po katalogu ove
knjige pripada traci `portal-mediated`, u kojoj se datoteka ne pohranjuje nego se
daje uputa za preuzimanje. Prije promocije treba (1) razriješiti Eurostatov
stupac, (2) potvrditi uvjete MPD-a za prikaz jedne zemlje i (3) pribaviti
suglasnost suautora projekta AI.econ za redistribuciju spojenoga niza.

Do tada su ove datoteke građa za pripremu, a ne izvor tvrdnji u knjizi.

## Oznaka izmjena

1. **Imena stupaca.** Prevedena su na hrvatski; jedinica je upisana u samo ime
   stupca, jer se stupci razlikuju upravo po jedinici.
2. **Kod nedostajuće vrijednosti.** Uzvodni `NA` zapisan je kao `..` i znači
   „imenovana procjena ne pokriva tu godinu”. To nije nula.
3. **Razmaci u oznakama razdoblja** zamijenjeni su podvlakom.
4. **Logičke vrijednosti** `TRUE`/`FALSE` zapisane su kao `da`/`ne`.
5. **Izostavljena mjesečna interpolacija za 1991.–1992.** Uzvodni projekt nosi i
   Chow-Lin razdiobu godišnjega niza na mjesece. To je modelirana veličina, a ne
   opažanje, i ovdje je nema.

Nijedna vrijednost nije zaokružena ni popravljena.

## Stupci se ne smiju uspoređivati ni prosječivati

Pet stupaca u `bdp-hrvatska-izvori.csv` **nisu usporedive razine**. Ulančani
euro, međunarodni dolar iz 2011., američki dolar iz 2017., stalni američki dolar
iz 2015. i Geary-Khamis baza iz 1990. pet su različitih mjerila. Prosjek retka
nema značenje. Datoteka postoji upravo zato da se to vidi: ista zemlja, ista
godina, pet brojeva koji se ne slažu, i nijedan nije pogrešan.

## Spojeni niz je konstrukcija

`bdp-hrvatska-spojeni.csv` jedan je niz sastavljen od tri odsječka, ulančan po
stopama rasta i usidren na razinu 2015. = 100, gdje je razina 11.760 eura:

- `tica` 1910.–1951. — rekonstrukcija, autor sam upozorava na oprez;
- `maddison` 1952.–1994.;
- `modern` 1995.– — Eurostat, jedini odsječak s izravno opaženim razinama.

Četiri točke prije 1910. označene su u stupcu `granulacija` kao `benchmark`: to
su pojedinačne referentne procjene, ne godišnji niz.

Stupac `prekid` označava godine 1991.–1995. Te su vrijednosti **rekonstruirane, a
ne opažene**: kroz rat i raspad prethodne države statistički sustav nije
proizvodio usporedivi niz. Svaka tvrdnja o padu i oporavku u tim godinama mora
nositi tu ogradu.

Ratne godine 1914.–1919. i 1940.–1946. u Tičinu izvoru nisu popunjene.

`bdp-hrvatska-razdoblja.csv` sažima spojeni niz u imenovana razdoblja. Granice
razdoblja **odabrao je analitičar**, nisu svojstvo podataka, i drukčiji bi izbor
dao drukčije stope. To je dio pouke, a ne propust.

Licenca izvora odnosi se na podatke. Kod izvatka i tekst knjige ostaju pod
uvjetima repozitorija.
