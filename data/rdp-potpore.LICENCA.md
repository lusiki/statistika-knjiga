# Licenca i obavijest uz izvatke skupa `rdp_potpore`

Ova obavijest putuje uz datoteke `rdp-potpore-skupine.csv`,
`rdp-potpore-godisnje.csv`, `rdp-potpore-velicina.csv`, `rdp-potpore-vrsta.csv`,
`rdp-potpore-obuhvat.csv` i `rdp-potpore-sazetak.csv` i mora ostati uz njih pri
svakom dijeljenju, preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `rdp_potpore` |
| Licenca izvatka | `CC BY 4.0 za izvedene agregate; uvjeti ponovne uporabe izvornoga registra nisu objavljeni` |
| Poveznica na licencu | <https://creativecommons.org/licenses/by/4.0/legalcode> |
| Izvorna baza | Registar državnih potpora i potpora male vrijednosti |
| URI izvora | <https://rdp.gov.hr/javno> |
| Nadležno tijelo | Ministarstvo financija Republike Hrvatske |
| Snimka registra dovršena | 19. srpnja 2026. |
| Razdoblje dodjela | 2017. — 2025. |
| Referentni službeni iznosi | [Godišnje izvješće o državnim potporama za 2023.](https://mfin.gov.hr/UserDocsImages/dokumenti/koncesije-dp/izvjesca/Godi%C5%A1nje%20izvje%C5%A1%C4%87e%20o%20dr%C5%BEavnim%20potporama%202023.pdf), str. 14 |
| Izračun agregata | projekt AI.econ / CroAIcon |
| Izvadak izradio | `scripts/build-croaicon-extracts.py` |

Primjer atribucije glasi „Registar državnih potpora i potpora male vrijednosti,
Ministarstvo financija Republike Hrvatske, <https://rdp.gov.hr/javno>, snimka od
19. srpnja 2026.; agregati izračunati u projektu AI.econ; izmjene su označene.”

## Stanje prava — pročitati prije uporabe

Licenca u tablici gore odnosi se na **izvedene agregate**: brojanje, zbrajanje i
udjele koje je izračunao projekt AI.econ. Ti su izračuni rad autorâ projekta i
dijele se pod CC BY 4.0.

Ne odnosi se na sam registar. Registar je javan i pretraživ, ali za njega u ovom
trenutku **nije zabilježena mjerodavna objava uvjeta ponovne uporabe**, kakvu
DZS ima kroz Hrvatsku otvorenu dozvolu. Dostupnost nije dopuštenje.

Zato ovaj paket **još nije promoviran** i nalazi se u repozitoriju kao kandidat,
a ne kao odobren nastavni skup.

Uz to, agregati nisu izračunati iz javnoga sučelja registra nego iz radne kopije
u analitičkom okruženju projekta AI.econ, u kojem autor ove knjige surađuje s
drugim autorom. Prije nego što ijedna brojka odavde uđe u poglavlje, potreban je
gate koji utvrđuje (1) uvjete ponovne uporabe registra i (2) suglasnost
suautora projekta AI.econ za redistribuciju izvedenih agregata.

Do tada su ove datoteke građa za pripremu, a ne izvor tvrdnji u knjizi.

## Oznaka izmjena

U ovim datotekama promijenjeno je točno ovo:

1. **Razina.** Preuzeti su isključivo agregati. Nijedan redak ne opisuje
   pojedinačnu dodjelu ni imenovanog primatelja, i OIB-i se nigdje ne pojavljuju.
2. **Odabir.** Preuzeto je šest od osam objavljenih agregatnih tablica.
   Razrada po djelatnostima i razrada unutar vrste potpore nisu preuzete.
3. **Imena stupaca.** Prevedena su na hrvatski.
4. **Razmaci u oznakama.** U stupcima `skupina`, `velicina` i `vrsta` razmaci u
   izvornim oznakama zamijenjeni su podvlakom, kako datoteka ne bi trebala
   navodnike. Same oznake nisu skraćene ni preformulirane.
5. **Dodani nazivnici.** U `rdp-potpore-skupine.csv` uz svaki udio stoje i
   `primatelji_ukupno` i `iznos_ukupno_eur`, pa se svaki postotak može provjeriti
   ručno.
6. **Izostavljen stupac `scope`.** U tablici obuhvata bio je isti u sva tri
   retka i sadržavao zarez; njegov je sadržaj ovdje: *„Državne potpore i potpore
   male vrijednosti, uključujući poljoprivredu i ribarstvo”*.
7. **Izračunat prosjek po primatelju.** U `rdp-potpore-sazetak.csv` redak
   `iznos_prosjek_po_primatelju` jest `iznos_ukupno / primatelji`. To je jedina
   izvedena brojka u paketu i postoji zato da stoji uz medijan.

Nijedna vrijednost nije zaokružena ni popravljena.

## Obuhvat — zašto ovo nije nacionalna vremenska serija

`rdp-potpore-godisnje.csv` izgleda kao vremenska serija i **nije** je dopušteno
tako čitati. Datoteka `rdp-potpore-obuhvat.csv` pokazuje zašto: ista snimka
registra za 2021. reproducira **0,93 %** službenoga godišnjeg iznosa
Ministarstva financija, a za 2023. **95,2 %**. Rast iznosa kroz godine u ovoj
snimci prije svega mjeri kako se punio registar, a ne koliko je potpora
dodijeljeno.

To je razlog zbog kojega je paket odabran. Tablica obuhvata nije napomena uz
podatke — ona je podatak.

## Ostala ograničenja

- Uključene su dodjele sa statusom `Ispravan` i pozitivnim iznosom. Redci sa
  statusom `Upozorenje` isključeni su; najveći pozitivan zapis među njima iznosi
  oko 18,7 milijardi eura i njegovo bi uključivanje poništilo smisao usporedbe.
  Taj je iznos u `rdp-potpore-sazetak.csv`, da isključivanje ostane vidljivo.
- Iznos je *element potpore*, a ne proračunska isplata i ne mjera učinka.
- `Nepoznato` u stupcu `velicina` objavljena je kategorija, a ne nedostajuća
  vrijednost. Nosi oko 16 % iznosa.
- Veličina se odnosi na pojedinu dodjelu i može se mijenjati kroz vrijeme.
- Naslovni iznos izvješća za 2024. nije izravno usporediv s ranijim izvješćima,
  jer to izvješće prvi put odvojeno prikazuje poljoprivredu i ribarstvo.

Licenca izvora odnosi se na podatke. Kod izvatka i tekst knjige ostaju pod
uvjetima repozitorija.
