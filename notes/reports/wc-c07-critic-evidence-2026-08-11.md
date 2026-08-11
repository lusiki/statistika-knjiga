# WC-C07 — završni pregled dokaza, citata i podrijetla

**Izvor:** `chapters/07-vjerojatnost.qmd`

**SHA-256 prije i poslije pregleda:**
`900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`

Pregled je bio neovisan i samo za čitanje; nijedna datoteka nije uređena ni
stvorena.

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Integritet citata | 5/5 |
| Potpora empirijskim tvrdnjama | 5/5 |
| Brojčana i podatkovna provenijencija | 5/5 |

## Nalazi poglavlja

```yaml
fatal: []
major: []
minor: []
useful_improvement: []
missing_or_unverified: []
```

Svih deset živih citatnih uporaba pripada trima postojećim ključevima: pet
puta `gilovich1985`, četiri puta `miller2018` i jednom `sikic2026`. Metapodaci,
godišta, stranice i DOI-ji dvaju članaka odgovaraju primarnim publikacijama, a
`scripts/check-citations.py` završava s `CITATION_INTEGRITY_OK`.

Tvrdnje o vrućoj ruci odgovaraju dosegu izvora. Gilovich, Vallone i Tversky
podupiru opis vjerovanja, analizu zapisa i kontrolirani pokus; Miller i Sanjurjo
podupiru pristranost odabira niza, ranjivost kanonske studije i njezinih
ponavljanja te preokret zaključka nakon ispravka. Tekst čuva ogradu da taj
ispravak nije sam po sebi dokaz vruće ruke.

Generirana `populacija_medija` vezana je uz `[@sikic2026]` i katalog. Paket je
promoviran, ima generator `simuliraj_populaciju`, sjeme 8001, licencu CC BY
4.0, postojeće snimke i usklađene kontrolne zbrojeve. Generirani, hipotetski i
vanjski empirijski registri ostaju razdvojeni; nijedna simulirana vrijednost ne
prikazuje se kao mjerenje stvarnih ljudi.

## Brojčana reprodukcija

Neovisno izvršavanje deklariranih računa i sjemena potvrdilo je, među ostalim:

- tri niza novčića nakon 20 bacanja od `0,25` do `0,65`, a nakon 2.000 bacanja
  od `0,498` do `0,502`;
- mreže `26,756 %`, mlade `24,720 %`, zajednički udio `11,336 %` i umnožak
  rubnih udjela `6,614083 %`;
- portal `30,202 %`, mladi ili portal `47,046 %`, preklop `7,876 %`;
- mreže među mladima `45,857605 %`, među ostalima `20,483528 %`, televiziju
  ukupno `21,654 %` i među starijima `41,246027 %`;
- područja za minute `70,104 %`, `95,912 %`, `99,138 %`; za sirove iznose
  `87,654 %`, `94,566 %`, `97,630 %`; za logaritmirane pozitivne iznose
  `67,97823 %`, `94,80954 %`, `99,66513 %`;
- udio nultih iznosa `76,11 %`;
- udjele nakon triju pogodaka `0,356`, `0,418` i `0,459`, a nakon jednoga
  pogotka u nizu duljine 100 vrijednost `0,496`;
- vjerojatnost nijedne viralne objave `66,76080 %` i barem jedne od pet
  hipotetskih objava `9,60792 %`, prikazanu kao `9,6 %`;
- analitičku repnu vjerojatnost e-biltena `19,41652 %` i simulacijsku provjeru
  `19,31 %`;
- povratni zadatak `90/585 = 15,38462 %` i temeljnu stopu
  `100/10.000 = 1 %`.

Svi zaokruženi prikazi odgovaraju punim vrijednostima. Skriveni i vidljivi
račun e-biltena koriste isti model i sjeme 709. Widget koristi
`d3.randomLcg(707)`, a statični prikazi sjemena 707 i 710.

## Lokalni podaci i postojeći dokumentacijski dug

`data/katalog.yml` navodi `WC-C07` i Chapter 7 kao potrošače paketa.
`scripts/build-data-snapshots.R` potvrđuje četiri snimke, a
`scripts/check-data-integrity.R` svih 21 validiranih snimki i deset
usklađenja. Postojeće upozorenje o nesinkroniziranom `renv` ne mijenja uspješan
ishod provjera.

Dodatak C ne navodi Chapter 7 u čitateljskom sažetku uporabe
`populacija_medija` i na dva mjesta govori o snimci kao budućoj. To nije nalaz
WC-C07: isti dokumentacijski dug već je u vlasništvu `P5-C` kroz
`H-P3-CATALOG-002`, pa se ovdje ne duplicira.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **0**
- Korisno poboljšanje: **0**
- Nedostaje ili nije verificirano: **0**
- Prethodno postojeći katalog-dokumentacijski dug: **2 opisa, izvan WC-C07**

**Verdikt:** dokazni i citatni prolaz bez otvorenoga nalaza u WC-C07. Odluka o
C07 ostaje autoru/editoru.
