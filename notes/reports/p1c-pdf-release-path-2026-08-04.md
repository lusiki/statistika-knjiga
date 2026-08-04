# P1C-PDF: blokirajući i stale-safe put PDF-a

**Paket:** `P1C-PDF`

**Stavke:** `R05-PDF-wrapper`, `R05-PDF-fail-blocking`,
`R05-PDF-stale-protection`

**Datum provjere:** 4. kolovoza 2026.

**Dokazani implementacijski izvor:**
`f2c4f8242d14722876549d0cc8fbc25989cdc5c6`

## Granica paketa

Paket mijenja samo odobreni PDF omotač, njegovu determinističku provjeru,
PDF korak u objavnom workflowu i točan javni opis tog puta. Ne uvodi provjere
integriteta rukopisa, izvoze, paritet widgeta, preglednički test, izdanje ni
objavu. `P1C-INTEGRITY`, `P1C-EXPORT` i svi kasniji paketi ostali su
nepokrenuti.

`H-P1B-META-002` prihvaćen je prije prve implementacijske izmjene. Upozorenje
u README-u ostalo je nepromijenjeno dok nisu prošle niže opisane pozitivna
izgradnja i namjerno neuspješne provjere.

## Implementirani put

- `.github/workflows/publish.yml` više nema goli
  `quarto render --profile pdf`, `continue-on-error`, odvojeno kopiranje ni
  granu koja dopušta stari PDF. Jedini PDF poziv jest
  `pwsh -NoProfile -File scripts/render-book-pdf.ps1 -RequireCleanCommit`.
- PDF korak dolazi prije HTML rendera. U načinu `-RequireCleanCommit` omotač
  prije uklanjanja starih artefakata zahtijeva trenutačni commit bez praćenih
  izmjena.
- Omotač zatim uklanja `pdf/Statistika.pdf` i
  `docs/pdf/Statistika.pdf`, provjerava nepromijenjenu kanonsku konfiguraciju,
  pokreće PDF profil te prihvaća samo novu datoteku s potpisom `%PDF-`.
- Poslužna se kopija stvara tek nakon uspješnog rendera. SHA-256 izvornog i
  poslužnog PDF-a mora biti jednak. Svaka pogreška omotača, rendera, potpisa,
  nedostajućeg artefakta ili kopije kroz `finally` ponovno uklanja oba PDF-a.
- `scripts/check-pdf-release-path.ps1` provjerava workflow i omotač u četiri
  izolirana privremena slučaja bez mijenjanja kanonskih artefakata.

## Pozitivna zaključana izgradnja

Odvojena radna kopija stvorena je iz commita `f2c4f82`. U njoj su R
biblioteka i cache, izvorne i binarne pohrane, npm cache i Playwrightovi
preglednici usmjereni u nove prazne direktorije, uz
`RENV_CONFIG_CACHE_ENABLED=FALSE`. Javna naredba
`python scripts/restore-dependencies.py` završila je zapisima
`R_RESTORE_OK`, `BROWSER_RESTORE_OK` i `DEPENDENCY_RESTORE_OK`; radna kopija
nakon obnove nije imala praćene izmjene.

Prije poziva omotača obje urezane PDF kopije imale su SHA-256
`b5b18b1c37ba315d7b4d9113016ae6ba862dc19a4c971a7613074135827f6606`.
Omotač ih nije uporabio kao rezultat: uklonio ih je prije rendera i izradio
novi PDF od 2.570.017 bajtova sa sažetkom
`cb57918e724caf3d3b60605972753b82f57e28354baba3f93f30f80001ae1930`.
Izvorna i poslužna kopija imale su isti sažetak i potpis `%PDF-`, a omotač je
završio zapisom:

```text
PDF_BUILD_OK source_commit=f2c4f8242d14722876549d0cc8fbc25989cdc5c6 sha256=cb57918e724caf3d3b60605972753b82f57e28354baba3f93f30f80001ae1930 bytes=2570017
```

Dokaz je izveden s R-om 4.6.0, Quarto 1.9.38 i Windows PowerShellom
5.1.26100.8457. Privremena radna kopija i njezini cachevi uklonjeni su nakon
provjere; nijedan izgrađeni PDF nije urezan ili objavljen.

## Namjerno neuspješne provjere

Provjera je iz istog commita završila ovim očekivanim ishodima:

```text
EXPECTED_SUCCESS case=positive-replacement exit=0
EXPECTED_FAILURE case=wrapper-preflight-failure exit=1
EXPECTED_FAILURE case=build-command-failure exit=1
EXPECTED_FAILURE case=stale-missing-artifact exit=1
PDF_RELEASE_FIXTURES_OK cases=4 workflow=wrapper-only-blocking
```

U svim trima neuspješnim slučajevima omotač je vratio nenulti izlaz, ostavio
`_quarto.yml` bajtno nepromijenjen i uklonio i izvorni i poslužni PDF. Time su
zasebno dokazani neuspjeh omotača, neuspjeh naredbe za izgradnju te uspješan
izlaz alata bez svježeg artefakta nakon prethodno postavljenih starih kopija.

## Budući učinak

`AGENTS.md` i dalje u odjeljku o deploymentu opisuje stari neblokirajući PDF
korak. Taj upravljački tekst nije dio ovoga uskog produkcijskog paketa;
`H-P1C-PDF-001` predaje njegovo usklađivanje paketu `P2-DOCS`. Provjera
ugrađenih pisama i vizualni pregled stvarnog artefakta ostaju već registrirani
u `P7-PDF`; uspješan izlaz omotača ne zamjenjuje taj dokaz.

Kanonski sažetak četiriju implementacijskih i javnih datoteka jest
`28360c3532803d3f8b32198335f783747bce84223ba2fbe94a6b3a89ae1d4866`.
