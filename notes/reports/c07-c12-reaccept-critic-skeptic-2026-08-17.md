# C07–C12 reacceptance — kritičar skepticizma i prejakih tvrdnji

**Gate:** `C07-C12-REACCEPT`

**Leća:** skrivene pretpostavke, alternativna objašnjenja i prejak doseg

**Način:** neovisni read-only pregled svih šest izvora

**Izvorni commit:** `ddde7f6cabc0d4335660755c6fbc7601937b4318`

## Potvrda izvora

Svih šest radnih izvora bajtno odgovara imenovanom commitu i očekivanom
manifestu.

| Poglavlje | SHA-256 |
|---|---|
| 07 | `900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5` |
| 08 | `9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04` |
| 09 | `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f` |
| 10 | `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236` |
| 11 | `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1` |
| 12 | `4a6d173d7e995e1f251e34003121a8eae7be2a3f7753b538634bc96a0d49a1b4` |

## Ocjene

- pokrivenost osporavanja: 5/5;
- pošten odnos prema drugim pogledima: 5/5;
- normativna iskrenost: 4/5.

## Snage

- Poglavlje 7 dobro razdvaja ono što proizvodi fiksni slučajni model od
  stvarnih promjena procesa te uz vruću ruku navodi težinu šuta, obranu i
  odabir pokušaja kao konkurentska objašnjenja.
- Poglavlja 8 i 9 odvajaju uzoračku preciznost od selekcije, pokrivenosti,
  neodgovora, mjerenja i nesigurnosti kodiranja; velik ili bootstrapiran uzorak
  nigdje ne postaje automatsko dopuštenje za populacijski doseg.
- Poglavlje 10 prikazuje i granice frekvencijskoga postupka i legitimno
  drukčije Bayesovsko pitanje bez proglašavanja jednoga pristupa opće
  nadmoćnim.
- Poglavlja 11 i 12 izbjegavaju moraliziranje: nalaz o precjenjivanju ostaje
  omeđen vlastitom simulacijom, niska snaga nije presuda cijeloj literaturi, a
  predregistracija, reproducibilnost i otvorenost nisu jamstva valjanosti.

## Nalazi

Nema fatalnih ni velikih nalaza.

1. `{ severity: minor, location: chapters/10-logika-testiranja.qmd:591-598, reason: Rečenica da se nijedan od dvaju rizika ne može ukloniti univerzalnija je od onoga što postupak opravdava. Degenerirano pravilo koje nikada ne odbacuje može ukloniti pogrešku prve vrste uz potpunu cijenu u pogrešci druge vrste, i obratno. Prava je tvrdnja da se oba rizika ne mogu istodobno ukloniti u informativnom postupku., fix: Napisati da se u postupku koji zadržava mogućnost obiju odluka oba rizika ne mogu istodobno svesti na nulu te da pomicanje praga smanjuje jedan uz povećanje drugoga. }`
2. `{ severity: minor, location: chapters/11-velicina-ucinka-i-snaga.qmd:442-448, reason: Tvrdnja da će studija planirana prema preciznosti, što god pronašla, biti dovoljno precizna za odluku zvuči kao jamstvo. Plan pod pretpostavljenom raspršenošću cilja očekivanu ili tipičnu širinu; ostvarena raspršenost, osipanje, mjerenje i položaj procjene prema odlukaškoj granici još mogu ostaviti neodlučan rezultat., fix: Napisati da plan pod navedenim pretpostavkama cilja unaprijed zadanu širinu, a da se nakon prikupljanja mora provjeriti ostvareni interval i njegova dostatnost za konkretnu odluku. }`

## Presuda

**Prolaz uz dva neblokirajuća manja nalaza.** Nema fatalne ili velike
pretpostavke, prejakoga kauzalnog dosega ni skrivenoga normativnog izbora koji
bi priječio zajedničko ponovno prihvaćanje.

Kritičar nije mijenjao nijednu datoteku.
