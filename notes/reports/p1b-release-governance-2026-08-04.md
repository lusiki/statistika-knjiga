# P1B-GOV — predobjavno upravljanje izdanjem

**Paket:** `P1B-GOV`

**Datum provjere:** 4. kolovoza 2026.

**Polazni commit:** `0e2f5eaacab94482619f12445a4045aff86f1f8f`

**Stanje mehanizma:** `pre_release`
**Kontrolni zbroj obuhvata:**
`sha256:dcfcc7d7d8ac052546711f45d38a79b97a52a4d9d3c8a71f06c4d7f92c1ea002`

## Granica paketa i ulazna odluka

Prije prvoga sadržajnog uređivanja u potpunosti su pročitani kanonski plan,
registar, nadzorna ploča i dnevnik primopredaja, lokalne upute vodiča knjige i
ugovor ograničenoga vanjskog upita. Posebno su pročitani ugovor
`release_governance`, D14, svi zapisi R06, prihvaćena odluka `G-A1d`, četiri
riješena upita `OA-G-A1D-*` i `H-G-A1D-001`.

`H-G-A1D-001` prihvaćen je i potrošen prije izmjene izvora mehanizma. Njegova
je dispozicija ostala granica paketa: dopušten je samo lokalni predobjavni
mehanizam; konačni naslov, autorstvo, izdanje, inačica, datum, citat, oznaka,
arhivski identifikator i javna prijava ispravaka nisu zamrznuti. Nisu dopušteni
push, merge, tag, arhivski polog, deployment, objava ni prihvaćanje kasnijega
paketa.

## Uspostavljeni mehanizmi

| Mehanizam | Kanonski izvor | Predobjavno stanje |
|---|---|---|
| naslov, izdanje i inačica | `release/governance.yml` | D14 radni naslov zadržan; konačna polja prazna |
| čitateljski dnevnik promjena | `CHANGELOG.md` | hrvatski odjeljak „Neobjavljeno” s datumom |
| citat | `index.qmd`, `tex/colophon.tex` | uputa za navođenje nacrta; konačni citat i PID prazni |
| podrijetlo artefakata | `release/provenance.yml` | popis i SHA-256 lokalnih izvora; nema release artefakata |
| arhiviranje | `release/archive-plan.md` | plan i vlasnik postoje; usluga, PID i polog prazni |
| zamrzavanje nastavne inačice | `release/term-freeze-policy.md` | politika postoji; vlasnik čeka `G-A5c`, aktivacija čeka `G-A6-DEPLOY` |
| ispravci | `errata.qmd`, `release/errata.yml` | vlasnik i datum postoje; javno odredište i stavke prazni |

Luka Sikic upisan je kao vlasnik izdanja, arhiviranja i ispravaka. Uloga
vlasnika zamrzavanja nastavne inačice nije pretpostavljena prije `G-A5c`.

## Demonstracija bez izdanja

Stroj stanja ima sedam izričitih prijelaza i nula trajno zapisanih prijelaza.
Lokalna demonstracija pokušava prijeći iz `pre_release` u
`metadata_approved`; očekivano završava kao
`blocked_without_required_gate` jer `G-A5b` nije prihvaćen. Provjera potvrđuje
da prijelaz nije zapisan, da su konačna metapodatkovna polja prazna, da nema
release artefakata i da su sve ovlasti za vanjske radnje `false`.

## Provjere

- `scripts/check-release-governance.R` prolazi i ponovno izračunava SHA-256
  svakoga izvora u manifestu.
- Bookwrightov linter za `index.qmd` i `errata.qmd` nalazi nula kandidata; ručni
  hrvatski pregled nije našao preostalu stilsku ili značenjsku pogrešku.
- `scripts/check-tokens.R` prolazi bez odstupanja od dizajnerskih tokena.
- Ciljani HTML renderi naslovnice i stranice ispravaka prolaze. Renderirani
  tekst sadrži predobjavnu granicu citata, vlasnika ispravaka, datum i upozorenje
  da put još nije javno aktiviran.
- Generirani AI izvozi nastali pre-render korakom vraćeni su izvan obuhvata
  paketa; `docs/` i `data/ai-exports.json` nisu promijenjeni.
- `git diff --check` prolazi.
- Kanonski workflow validator i obje obvezne negativne probe prolaze pri
  zatvaranju paketa.

## Budući učinci

Jedna primopredaja nosi kanonske putove i granice prema `P7-FREEZE`,
`P7-CLEAN-BUILD`, `G-A5c`, `P8-META`, `P8-ARCHIVE` i `P8-DEPLOY`. Kasniji
paketi moraju popuniti ista polja i provjeriti isti mehanizam; ne smiju ga
zaobići zasebnim izvorom metapodataka. Ova primopredaja ne prihvaća nijedan od
tih paketa i ne daje ovlast za vanjsku radnju.
