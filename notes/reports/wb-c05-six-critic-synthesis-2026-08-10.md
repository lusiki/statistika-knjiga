# WB-C05 — sinteza šest kritičara

**Konačni izvor:** `chapters/05-vizualizacija.qmd`

**Konačni SHA-256:**
`db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`

Šest neovisnih kritičara samo za čitanje pregledalo je konačno materijalno
stanje. Svaki je potvrdio isti hash prije i nakon pregleda. Nijedan render ni
drugi zapis nije tekao usporedno sa završnim panelom.

## Popravci prije završnoga panela

Raniji dijagnostički prolazi zatvorili su sve fatalne i velike nalaze prije
zaključavanja izvora. Skraćena os sada razlikuje stupce od položajnih prikaza,
Tufteove su mjere ograničene na heuristike, logaritamska os izriče vizualnu
kompresiju i omjerno čitanje, a DigiKatove jedinice, nazivnici, praznina i lom
metode ostaju razdvojeni.

Stilski je uklonjena prezentacijska ordinalna kadenca i neizmjerena tvrdnja o
uštedi vremena. Usklađeni su hrvatski termini, izvorne formule, alternativni
tekstovi i četiri pristupačna stanja widgeta. Cleveland–McGillov puni poredak
više nije prikazan kao rezultat jednoga pokusa, a tablica izbora prikaza više
ne pripisuje violinskom prikazu gubitak vrhova. Prve pojave geometrije,
ljestvice i koordinatnoga sustava slijede ratificirani zapis pojmova bez novih
definicijskih blokova.

## Zajednička dispozicija

Metode, pedagogija, stil i struktura nemaju otvoren nalaz. Dokazni kritičar
potvrdio je sve citate, brojke i granice tvrdnje; njegov jedini manji nalaz
odnosi se na zastarjele javne podatkovne dokumente izvan poglavlja i već je
usmjeren paketu `P5-C` prijenosima `H-WB-C04-001` i `H-P3-CATALOG-002`.

Skeptički kritičar zadržava dva manja, neblokirajuća nalaza. Tablica
histogramu i krivulji gustoće pripisuje čuvanje cijeloga oblika bez spomena
razreda i izglađivanja, a prag od tri ili četiri skupine za boju zvuči
univerzalnije nego što jest. Oba su nalaza lokalna, ne mijenjaju nijedan broj,
izlazni test ni granicu generalizacije i ostaju izrijekom pred autorom u C05.

## Konačni ishod

| Perspektiva | Ocjena | Fatalni | Veliki | Manji |
|---|---:|---:|---:|---:|
| metode | 5/5 | 0 | 0 | 0 |
| skepticizam | 4/5 | 0 | 0 | 2 |
| pedagogija | 5/5 | 0 | 0 | 0 |
| dokazi i citati | 5/5 | 0 | 0 | 1 |
| stil | 5/5 | 0 | 0 | 0 |
| struktura | 5/5 | 0 | 0 | 0 |

Sva četiri upravljana testa `R13-C05-frequency-visual`,
`R28-C05-introduction`, `R28-C05-density` i `R31-C05-Anscombe` prolaze u svih
šest mjerodavnih perspektiva.

**Preporuka panela:** prihvatiti WB-C05 kao dovršen vertikalni rez i predati
konačni izvor imenovanom autoru/editoru na zasebnu odluku C05, uz izričit prikaz
dvaju manjih nalaza u poglavlju i jednoga već usmjerenog dokumentacijskog duga.
Panel ne otvara C05, ne bilježi autorovo čitanje i ne prihvaća poglavlje umjesto
autora.
