# WC-C08 — završni pregled dokaza, citata i podrijetla

**Izvor:** `chapters/08-uzorkovanje.qmd`

**SHA-256 prije i poslije pregleda:**
`9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04`

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
minor:
  - optional ESS passport is not yet exposed in the reader-facing data catalogue
useful_improvement: []
missing_or_unverified: []
```

Svi živi citatni ključevi postoje u `references.bib`, a
`scripts/check-citations.py` završava zapisom
`CITATION_INTEGRITY_OK files=37 live_keys=44 records=44 blanket_nocite=0`.
Tvrdnje o pogrešci anketa Literary Digesta i lekciji o okviru i neodgovoru
omeđene su onime što podupire postojeći Squireov zapis; u završnom stanju nema
nepotkrijepljene povijesne pojedinosti.

Sintetička konačna populacija izrijekom je autorski nastavni primjer, ne
empirijski rezultat. Skrivena provjera potvrđuje šest opaženih jedinica,
poznate vjerojatnosti uključivanja 0,50 i 0,25, inverzne težine 2 i 4,
`3/6 = 50,0 %` te `6/16 = 37,5 %`. Nijedan rezultat nije pripisan ESS-u.

ESS put poziva se samo na službeno preuzetu vlastitu kopiju Round 11
integriranoga glavnog skupa, edition 3.0, hrvatski podskup, varijablu `vote`,
analizi prilagođen nazivnik valjanih odgovora i zadanu težinu `anweight`.
Poglavlje ne sadrži ESS mikropodatke, broj ispitanika ni empirijski postotak i
ne tvrdi da težina uklanja mjernu ili selekcijsku pogrešku.

## Minor izvan zaključanoga izvora

Fakultativna ESS putovnica još nije izložena u čitateljskom `podaci.qmd` ili
Dodatku C. To nije nedostatak provenijencije poglavlja ni razlog za promjenu
zaključanoga hasha. Isti katalog-dokumentacijski posao već pripada `P5-C` kroz
`H-P3-CATALOG-002`; WC-C08 ga ne duplicira.

## Prethodni blokirajući nalaz

Predfinalni pregled zatražio je čvršću potporu formulaciji o Literary Digestu.
Tekst je prije završnoga panela sveden na tvrdnje koje podupire postojeći
Squireov izvor i svaka je takva tvrdnja dobila citat u istoj rečenici.

## Otvoreni nalazi

- Fatal: **0**
- Major: **0**
- Minor: **1**
- Korisno poboljšanje: **0**
- Nedostaje ili nije verificirano: **0**

**Verdikt:** dokazni i citatni prolaz. Jedini minor već ima vlasnika izvan
WC-C08; odluka o C08 ostaje autoru/editoru.
