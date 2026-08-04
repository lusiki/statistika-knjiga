# P1C-INTEGRITY: blokirajuće provjere integriteta

**Paket:** `P1C-INTEGRITY`

**Stavke:** `R05-CI-token`, `R05-CI-style`, `R05-CI-structure`,
`R05-CI-figure`, `R05-CI-citation`, `R05-CI-concepts`, `R05-CI-data`

**Datum provjere:** 4. kolovoza 2026.

**Dokazani implementacijski izvor:**
`919b0b1ed430e64e653284e7962511ae50335409`

**Kanonski sažetak implementacijskih datoteka:**
`8699a3b2dbd07be1b39a75bd800fafc00e4162c0188ce027aa6139e7b00f4147`

## Granica paketa

`H-P0-REGISTER-005` prihvaćen je prije prve implementacijske izmjene. Paket
uvodi samo blokirajuće provjere dizajnerskih tokena, tvrdih pravila stila,
fiksne jezgre rukopisa, uvoda u figure, citata i obveznih bibliografskih
metapodataka, definicija i pojmovnih artefakata te trenutačnih nastavnih
podataka. Svaka je naredba samostalno poziva.

PDF omotač i njegovi artefakti nisu mijenjani. Paket nije mijenjao AI izvoz,
paritet widgeta, preglednički audit, konfiguracijske inventare, katalog
podataka, poglavlja ni dodatke. Nije pokrenut render, upload, deployment,
objava ni druga vanjska radnja.

## Implementirane blokirajuće naredbe

| Traka | Naredba | Pozitivni dokaz |
|---|---|---|
| Tokeni | `python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R` | svih 19 tokena usklađeno između izvora, SCSS-a i LaTeX-a |
| Tvrdi stil i struktura | `python scripts/check-manuscript-integrity.py` | `MANUSCRIPT_STYLE_OK files=25`; `MANUSCRIPT_STRUCTURE_OK chapters=19` |
| Uvodi u figure | `python scripts/check-figure-introductions.py` | točno jedan registrirani dug, bez neočekivane ili zastarjele iznimke |
| Citati | `python scripts/check-citations.py` | 35 živih ključeva, 35 zapisa, nula nepoznatih i nula `nocite: @*` |
| Pojmovi | `python scripts/check-concepts.py` | 46 jedinstvenih definicija, valjani čvorovi i bridovi, kanonski potrošač i točni otisci prijeratifikacijskog duga |
| Podaci | `python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-data-integrity.R` | dva ponovljiva generirana skupa, 50.300 redaka, jedinstveni ključevi, domene i CC BY 4.0 obavijest |
| Negativne fixture provjere | `python scripts/check-integrity-fixtures.py` | sedam očekivanih nenultih izlaza i `INTEGRITY_NEGATIVE_FIXTURES_OK lanes=7` |

Objavni workflow poziva svaku pozitivnu traku i zbirnu negativnu provjeru kao
običan blokirajući korak. Nijedan od tih koraka nema `continue-on-error`,
pričuvni put ili granu koja pretvara pogrešku u upozorenje. Bookwrightovi R
dijagnostički alati pozivaju se preko checkout-local pokretača i stvarnih
checkout-local skripti.

S7 ritam ostaje odvojena urednička provjera prosudbe. Njegova dva poznata
kandidata nisu pretvorena u tvrde produkcijske pogreške, čime paket ne uvlači
kasniju preradu proze u Phase 1C.

## Točno registrirani dugovi

Pozitivna cijev ne skriva proizvoljne postojeće pogreške. Datoteka
`scripts/integrity-debt.json` dopušta samo ove otprije registrirane i
kriptografski zaključane obveze:

1. `chapters/05-vizualizacija.qmd` / `fig-anscombe`, vezano uz
   `R28-C05-introduction` u `WB-C05`. Svaka dodatna figura bez uvoda ruši
   provjeru, a nakon popravka i sama zaostala iznimka ruši provjeru.
2. Prijeratifikacijski nesklad između 46 živih definicija, registra pojmova i
   generiranoga grafa, vezan uz `R04-TERMS-concept-regeneration` u
   `P2-TERMS`. Zaključani su sažeci izvornog i registarskog popisa, točnog
   nesklada te trenutačnog i svježe regeneriranog grafa. Svaka promjena
   definicije, registra, čvora, brida ili potrošača izvan tih otisaka ruši
   provjeru.

`H-P1C-INTEGRITY-001` i `H-P1C-INTEGRITY-002` predaju uklanjanje tih dviju
iznimki točnim kasnijim paketima. To su jedini budući učinci ovoga paketa.

## Pozitivna zaključana provjera

Iz commita `919b0b1` stvorena je odvojena detached radna kopija. R biblioteka
i cache, R izvorne i binarne pohrane, npm cache i Playwrightovi preglednici
usmjereni su u nove prazne direktorije. Javna naredba za obnovu potvrdila je:

```text
R_RESTORE_OK version=4.6.0 direct_packages=19 detected_packages=22
BROWSER_RESTORE_OK version=1.62.1
DEPENDENCY_RESTORE_OK r_lock=renv.lock playwright=1.62.1 node=24.15.0 npm=11.12.1
```

Nakon obnove prošlo je svih sedam gore navedenih pozitivnih traka. Provjera
`git status --short` ostala je prazna i nakon obnove i nakon svih provjera:

```text
P1C_INTEGRITY_CLEAN_PROOF_OK commit=919b0b1ed430e64e653284e7962511ae50335409 worktree_clean=true lanes=7 fixtures=7
```

## Namjerno neuspješne provjere

Zbirna fixture naredba stvorila je izolirane privremene kopije ili memorijske
izmjene, bez promjene kanonskih izvora. Svaki slučaj završio je kodom 1:

| Traka | Namjerni kvar |
|---|---|
| Tokeni | promijenjena vrijednost jednog SCSS tokena |
| Stil | dvotočka u običnoj prozi, protiv H1 |
| Struktura | uklonjena klasa obvezne vinjete |
| Figure | nova neregistrirana figura neposredno nakon naslova |
| Citati | nepoznati ključ `integrityfixture2099` |
| Pojmovi | dvostruki `#def-operacionalizacija` |
| Podaci | dvostruki ključ ispitanika |

Zbirni završni zapis bio je:

```text
EXPECTED_FAILURE lane=token exit=1
EXPECTED_FAILURE lane=style exit=1
EXPECTED_FAILURE lane=structure exit=1
EXPECTED_FAILURE lane=figure exit=1
EXPECTED_FAILURE lane=citation exit=1
EXPECTED_FAILURE lane=concept exit=1
EXPECTED_FAILURE lane=data exit=1
INTEGRITY_NEGATIVE_FIXTURES_OK lanes=7
```

## Kontrolno zatvaranje

Kanonski validator radnog tijeka prošao je nakon zajedničkog ažuriranja
registra, handoff-ledgera i nadzorne ploče te je potvrdio da nema aktivnoga
paketa i da je sljedeći dopušteni paket `P1C-EXPORT`:

```text
Comprehensive-review workflow: OK
branch revision/comprehensive-review
active none
next P1C-EXPORT
parents 36
children 371 zero unmapped
packets 188
manifests 18
handoffs 33
```

Obje obvezne negativne fixture provjere validatora zatim su neovisno vratile
očekivani izlaz 1:

```text
EXPECTED_FAILURE fixture=generic_packet_evidence exit=1
EXPECTED_FAILURE fixture=invalid_outside_ask_link exit=1
```

## Učinci na kasnije pakete

- `WB-C05` uklanja samo iznimku za `fig-anscombe` nakon odobrenoga uvodnog
  odlomka i ponovno pokreće pozitivnu i negativnu provjeru figure.
- `P2-TERMS` nakon ratifikacije usklađuje definicije i registar, regenerira
  graf, uklanja oba pojmovna otiska duga i ponovno pokreće pozitivnu i
  negativnu pojmovnu provjeru.

Nije pronađen drugi budući učinak. `P1C-EXPORT` i svi kasniji paketi ostali su
nepokrenuti.
