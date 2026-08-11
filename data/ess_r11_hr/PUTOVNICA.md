# ESS Round 11 Hrvatska — putovnica portalne rute

**Status:** provjerena i strojno čuvana portalna ruta; paket nije promoviran,
mikropodaci nisu preuzeti i lokalni kontrolni zbroj ne postoji.

**Odluka:** `G-A3-ESS`, prihvaćena 11. kolovoza 2026., zapisana u
`notes/reports/g-a3-ess-selection-decision-2026-08-11.md`.

## Službeni izvor i identitet

Čitatelj podatke preuzima samo iz službenoga ESS Data Portala:

<https://ess.sikt.no/en/>

Na portalu treba odabrati **ESS Round 11 integrated main file, edition 3.0** i
format **SAV**, koji prenosi oznake vrijednosti i korisnički definirane
nedostajuće vrijednosti. Identitet izdanja može se provjeriti prema službenoj
objavi i dokumentaciji:

- <https://www.europeansocialsurvey.org/news/article/third-round-11-data-release-published>
- <https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting>
- <https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS_weighting_data_1_1.pdf>
- <https://www.europeansocialsurvey.org/contact/disclaimer>
- <https://ess.sikt.no/en/api>

Knjiga nije preuzela ni pregledala mikropodatke. Tehnička mogućnost preuzimanja
ne znači da ih knjiga smije redistribuirati. `OA-G-A3-ESS-RIGHTS` ostaje otvoren
i neposlan; bundling je zabranjen bez zasebne pisane potvrde nositelja prava
vezane uz točne datoteke.

## Točna ruta čitatelja

1. Prijavite se kod pružatelja i u službenom portalu pronađite **ESS11 —
   integrated main file — edition 3.0**.
2. Preuzmite izdanje u formatu SAV u vlastitu mapu izvan repozitorija knjige.
   Nemojte spremati datoteku u `data/ess_r11_hr/` niti u drugi put repozitorija.
3. Izračunajte SHA-256 nad netaknutom preuzetom datotekom. U PowerShellu:

   ```powershell
   Get-FileHash -Algorithm SHA256 -LiteralPath 'C:\put\do\vlastite\ESS11.sav'
   ```

   Na sustavu s alatom `shasum`:

   ```bash
   shasum -a 256 /put/do/vlastite/ESS11.sav
   ```

   Zapišite naziv datoteke, vrijeme preuzimanja i dobiveni SHA-256 uz vlastitu
   kopiju, izvan repozitorija. Taj broj pripada čitateljevim bajtovima; nije
   kontrolni zbroj knjige i ne upisuje se u `data/katalog.yml`.
4. Pokrenite `scripts/prepare-ess-r11-hr.R` s ulazom i izlaznom mapom izvan
   repozitorija. Skripta nema mrežnu funkciju i odbija ulaz ili izlaz unutar
   repozitorija.
5. Prije analize usporedite skriptin `ess_r11_hr-schema.json` sa službenim
   codebookom za istu rundu i izdanje. Ako se oznaka, domena ili šifra
   nedostajanja razlikuje, stanite; ne popravljajte izvor napamet.

Primjer, iz korijena repozitorija:

```powershell
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/prepare-ess-r11-hr.R 'C:\korisnikovi-podaci\ESS11.sav' 'C:\korisnikovi-podaci\ess-r11-hr-izlaz'
```

Recept traži R pakete `haven` i `jsonlite`. `haven` namjerno nije obvezna
ovisnost builda knjige jer ESS replikacija nije dio builda ni CI-ja; čitatelj ga
za ovu neobveznu analizu osigurava u vlastitoj R biblioteci. Ako paket ili
izvorna SAV datoteka nedostaje, recept pada zatvoreno i ne stvara izlaz.

## Ugovor odabira i izvorno izložena shema

Skripta prvo provjerava identitet izdanja, zatim zadržava samo `cntry == HR` i
točno ovih 18 varijabli. Formalni ključ retka u ovom podskupu jest
`essround + cntry + idno`; `edition` i `proddate` čuvaju identitet objave.

| Skupina | Varijable | Uloga u ruti |
|---|---|---|
| identitet | `essround`, `edition`, `proddate`, `idno`, `cntry` | runda, izdanje, datum proizvodnje, identifikator retka i hrvatski podskup |
| nacrt | `dweight`, `pspwght`, `pweight`, `anweight`, `prob`, `stratum`, `psu` | ponderi, vjerojatnost uključivanja, stratum i primarna jedinica uzorkovanja |
| nastava | `vote`, `trstprl`, `stflife`, `gndr`, `agea`, `eisced` | glasanje, povjerenje, zadovoljstvo životom, rod/spol, dob i obrazovanje prema službenim ESS oznakama |

Ova tablica navodi odabrana polja i njihove nastavne uloge, ali ne izmišlja
brojčane domene ni šifre. Točne oznake varijabli, oznake vrijednosti,
`na_values` i `na_range` moraju doći iz SAV metapodataka edition 3.0. Skripta ih
izvozi bez ručnoga prepisivanja u `ess_r11_hr-schema.json`; taj je datirani trag
čitateljev codebook za njegove bajtove.

## Uloge pondera

- `anweight` je jedini zadani ponder za opcionalne nastavne procjene.
- `dweight` pokazuje korekciju nejednakih vjerojatnosti odabira, ali nije zadana
  konačna procjena.
- `pspwght` ostaje radi čitanja naknadnoga usklađenja u jednoj zemlji.
- `pweight` se čuva radi cjelovitosti službene sheme, ali se ne rabi u hrvatskoj
  jednocountry tablici.
- `prob`, `stratum` i `psu` opisuju nacrt; ova knjiga iz njih ne izvodi tečaj
  složene anketne varijance.

Ponderiranje ne uklanja samoprijavu, pogrešku mjerenja, neodgovor koji pomoćne
varijable ne mogu objasniti ni osobe izvan okvira uzorkovanja.

## Službene šifre nedostajanja i nazivnici

Svaka nastavna varijabla ima vlastitu domenu i analitički specifičan nazivnik.
Nema jednoga globalnog listwise-complete podskupa. Skripta zato za `vote`,
`trstprl`, `stflife`, `gndr`,
`agea` i `eisced` odvojeno zapisuje:

- službenu oznaku varijable;
- sve izvorne oznake vrijednosti;
- korisnički definirane pojedinačne nedostajuće vrijednosti (`na_values`);
- korisnički definirani raspon nedostajanja (`na_range`), ako postoji;
- broj redaka u hrvatskom podskupu i broj valjanih odgovora nakon primjene
  upravo tih izvornih pravila.

Službeno usklađenje prolazi samo ako se taj zapis podudara s codebookom ESS11
edition 3.0. CSV nije dopušten kao početni format jer bi mogao izgubiti
metapodatke potrebne za provjeru. Nula ostaje valjana ondje gdje je dio službene
domene; nijedna šifra odbijanja, neznanja, neodgovora ili nepripadanja
nazivniku ne pretvara se u nulu.

## Omeđeno pitanje i putovi uporabe

Opcionalna ESS replikacija pita:

> Među ispitanicima ESS Round 11 edition 3.0 u Hrvatskoj koji prema službenoj
> šifri pripadaju nazivniku za `vote`, koliko se prijavljeni udio glasalih
> razlikuje između neponderirane procjene i procjene s `anweight`, te koje
> pogreške odabira ili mjerenja taj ponder i dalje ne može ukloniti?

To je opisna i generalizacijska usporedba samoprijave, ne provjera službene
izlaznosti i ne uzročna tvrdnja. Nazivnik se izvodi iz službenih metapodataka
`vote`, a ne iz zapamćenoga popisa kodova.

- **R:** čitatelj rabi vlastiti izlaz skripte izvan repozitorija i za svaki
  izračun imenuje varijablu, valjani nazivnik i ponder.
- **Bez koda:** čitatelj može otvoriti istu vlastitu SAV kopiju u jamoviju,
  provjeriti službene nedostajuće vrijednosti, filtrirati `cntry == HR` i
  primijeniti `anweight`; to je neobvezna replikacija.
- **Tisak i obvezni offline zadatak u 8. poglavlju:** koriste zasebno označenu
  sintetičku konačnu populaciju s poznatim vjerojatnostima uključivanja,
  opaženim odgovorima i ponderima `1 / vjerojatnost uključivanja`. Ne koriste
  ESS mikropodatke ni rezultat portalne replikacije.
- **Obvezni putovi poglavlja 13–16:** koriste `populacija_medija` ili drugi
  licenčno čist lokalni paket iz kataloga.

## Što lokalni validator dokazuje

`scripts/check-ess-portal.py` ne kontaktira mrežu. Dokazuje da je katalog
omeđen na točno izdanje, varijable, potrošače i pitanje; da su `lane:
portal-mediated`, `promoted: false`, `files: []` i `checksum: null`; da ESS nije
u dnevniku promocije; da `data/ess_r11_hr/` sadrži samo ovu putovnicu; te da
recept zahtijeva ulaz i izlaz izvan repozitorija i čuva izvorne metapodatke.

Validator ne tvrdi da je provjerio redove, empirijski nazivnik, postotak,
lokalni checksum ni sadržaj službenoga codebooka. Ti testovi pripadaju
čitateljevoj vlastitoj portalnoj kopiji. P3-ESS dokazuje zakonitu i ponovljivu
rutu te odsutnost lokalnih bajtova, ne rezultat analize koju nije izveo.
