# C07–C12 reacceptance — kritičar statističkih metoda

**Gate:** `C07-C12-REACCEPT`

**Leća:** statistička točnost, pretpostavke, tumačenje i preciznost

**Način:** neovisni read-only pregled svih šest izvora

**Izvorni commit:** `ddde7f6cabc0d4335660755c6fbc7601937b4318`

## Potvrda izvora

Svježa metodološka runda obuhvatila je svih šest poglavlja. Žive datoteke ne
odstupaju od imenovanoga commita.

| Poglavlje | SHA-256 |
|---|---|
| 07 | `900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5` |
| 08 | `9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04` |
| 09 | `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f` |
| 10 | `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236` |
| 11 | `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1` |
| 12 | `4a6d173d7e995e1f251e34003121a8eae7be2a3f7753b538634bc96a0d49a1b4` |

Pregled se ne oslanja na ranije pojedinačne panele ni na continuity panel
`WC-PARTS` kao zamjenu za ovu svježu leću.

## Ocjene

- točnost: 5/5;
- pretpostavke: 4/5;
- tumačenje: 4/5;
- preciznost: 4/5.

## Snage

- Simulacija dosljedno prethodi formalizmu: dugoročna učestalost, distribucija
  uzorkovanja, pokrivenost intervala, nulta raspodjela, snaga i višestruki
  analitički putovi najprije se vide, a tek zatim imenuju.
- Nosiva razlikovanja ostaju statistički čista kroz svih šest poglavlja:
  opažanja nasuprot procjenama, standardna devijacija nasuprot standardnoj
  pogrešci, svojstvo postupka nasuprot pojedinačnom intervalu, p-vrijednost
  nasuprot vjerojatnosti hipoteze te značajnost nasuprot veličini i važnosti
  učinka.
- Pretpostavke su dobro omeđene za uvodni udžbenik: uvjeti CLT-a, konačna
  populacija, složeni nacrti, jedinica bootstrapa, zamjenjivost u permutaciji,
  idealizirani model snage i neovisnost putova u widgetu o analitičkoj
  fleksibilnosti izričito su navedeni.
- Kumulativni put drži: vjerojatnost omogućuje uzorkovanje, uzorkovanje
  procjenu, procjena testiranje, testiranje vodi veličini učinka i snazi, a
  poglavlje 12 cijeli lanac vraća u istraživački sustav i njegov provjerljiv
  trag.

## Nalazi

Nema fatalnih ni velikih nalaza.

1. `{ severity: minor, location: chapters/11-velicina-ucinka-i-snaga.qmd:233-249, reason: Veliko preklapanje raspodjela ne znači da skupinu pojedinca ne bi bilo moguće pogoditi. Odmah navedena vjerojatnost nadmoći veća od 50 % pokazuje slabu diskriminacijsku informaciju, samo nedovoljnu za pouzdanu klasifikaciju., fix: Napisati da se skupina pojedinca ne bi mogla pouzdano pogoditi ili da bi pojedinačna klasifikacija ostala vrlo nesigurna. }`
2. `{ severity: minor, location: chapters/11-velicina-ucinka-i-snaga.qmd:265-281, reason: Generator zadaje stvarnu razliku 2,05 % − 2,00 % = 0,05 postotnog boda, približno jedan dodatni klik na dvije tisuće prikaza. Rečenica o jednom kliku na tisuću prevodi opaženu procjenu od 0,101 postotnog boda kao da je poznata dobit., fix: Napisati „procijenjeni dobitak” i prenijeti interval u praktične jedinice ili kao poznatu razliku generatora navesti približno jedan klik na dvije tisuće prikaza. }`
3. `{ severity: minor, location: chapters/12-kriza-i-obnova.qmd:677-700, reason: Granične tablice sažimaju dvije razine u jednu. Jedan red izvedenoga zapisa jest laboratorij, ali laboratorijska razlika nastaje iz sudionika i eksperimentalnih uvjeta; istodobno redovi o povezanosti i uzročnosti nedovoljno razdvajaju eksperimentalni kontrast od objašnjenja međustudijske razlike., fix: Navesti sudionika kao jedinicu unutar laboratorija i laboratorijsku procjenu kao jedinicu sinteze, zatim odvojiti doseg učinka dodijeljenoga uvjeta od nepodržanoga uzročnog objašnjenja razlika među studijama. }`

## Presuda

**Prolaz uz tri neblokirajuća manja nalaza.** Statistički je luk C07–C12 točan
i kumulativno čvrst, bez fatalnoga ili velikoga metodološkog problema.

Kritičar nije mijenjao nijednu datoteku.
