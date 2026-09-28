# P6-VERIFY — zaustavljanje na četiri nesvježa rutna dokaza

Datum: 28. rujna 2026. Deklarirani izvorni commit:
`8a8003a88f63b122d7aae956fb0fdab44a137a17`, grana
`revision/comprehensive-review`. `P6-VERIFY` je i dalje jedini aktivni paket.
Ovo je nastavak zapisa od 31. kolovoza i prvoga zaustavljanja od 28. rujna,
ne novi claim ni zatvaranje P6.

## Već popravljena integracija i provjerena poglavlja

Otisak zadatka u kanonskom zapisu `sol-12-kriticki-01.json` sada je
`sha256:996bfbb5bfd5cc55fd9413105847c73d02c155efc2cd3898377cb3a49ae17e55`.
Doslovni token u assessment provjeritelju odgovara prihvaćenoj formulaciji
„standardiziranom granom provjere osjetljivosti”. Zadatak, brojevi i status
`P6-METHODS` nisu mijenjani u ovom nastavku. Assessment provjeritelj ponovno
prolazi za 95 zapisa i 95 otisaka; generator potvrđuje 95 javnih i 95
zaštićenih projekcija bez drifta. Arhitektura knjige, 19 kralježnica, inventar,
citati, terminologija, koncepti, rukopis, uvodi i ugovori slika prolaze.

Nakon materijalnih izmjena `P6-METHODS` svih šest neovisnih, samo čitateljskih
kritičarskih leća ponovno je pročitalo pune aktualne datoteke Poglavlja 7, 12,
13 i 14 na deklariranom commitu. Svaka leća za svako od četiri poglavlja nalazi
0 fatalnih i 0 velikih nalaza te potvrđuje `coauthor_review`; to nije tvrdnja o
novom autorskom čitanju ni o završnom stupnju. Manji nalazi ostaju vidljivi:
u 7 granica uvjetnog prosjeka i vjerojatnosti idućeg neovisnog pokušaja; u 12
jedinica eksperimenta nasuprot laboratorijskom sažetku, procjena čitanja od 6
minuta i ponovljen evaluativni izraz; u 13 tri usko formulirane dokazne tvrdnje,
izravni zadatak o referentnoj raspodjeli, rezidualima i prijelaz iz vinjete; u
14 uvjetovanje uzročnog tumačenja provedbom i mjerenjem, izravniji zadatak o
Welch/OLS nesigurnosti, konkretan slučaj u vinjeti i ton uvoda primjera. Niti
jedan manji nalaz nije promaknut u popravljeno stanje bez izmjene izvora.

Živi bajtni SHA-256 izvora četiri ponovno čitana poglavlja redom je:
`07=7a23ee64cecd88142954940d89eac9894eefdf15171acab5548a3f38275b92ef`,
`12=9ded7650044636803a6ddb5383fd556a10150681ce9d0137aa9042314268c28d`,
`13=67fe3402e24e832671f4959025633df8ab5391fc42415ca1988cf99213c2a8c5`
i `14=783b4f5193ee12513868fac1aff010eb5dda43da5b4b6da8a873cb8792768aa1`.

Izvorna matrica `P6-STYLE`, završni `P6-PANELS` i `P6-ARC` pročitani su ponovno.
Živi uvodi widgeta, primjera i svih 19 AI-okvira pregledani su; antiteze su
čitane u kontekstu, ne samo prebrojene. Dva razrađena primjera, 10:871–874 i
14:869–873, imaju sličan uvod „može se ispisati u nekoliko redaka i vrijedi ...
jednom vidjeti”; stilska leća 14 označuje to manjim nalazom. Pet djece R30 koja
je prethodno zaustavljanje imenovalo još nije dobilo pojedinačnu završnu
dispoziciju ni promjenu statusa. Njihov se dokaz ne izvodi iz statusa P6-STYLE.

## Pad šire matrice

Provjere su pokrenute na neizmijenjenom izvornom stanju, prije ikakve promjene
kontrolnih zapisa. Sljedeća četiri pozitivna provjeritelja izlaze s kodom 1:

| Provjera | Točna prva nesukladnost |
|---|---|
| `python scripts/check-appendix-c.py` | `APPENDIX_C_CHECK_FAIL: route artefakt nema kontrolni zbroj sadašnjega kataloga`; `config/appendix-c-data-route.json` čuva MD5 `8d81b7600cb2f92ebab8a9244ffa6c3e`, a živi `data/katalog.yml` ima bajtni MD5 `be71ea85ee726061aeb43554cc2dc749` (Git LF blob `6dcc9659e6802b706384d965f44ffcec`). |
| `python scripts/check-appendix-e.py` | `APPENDIX_E_CHECK_FAILED route artifact conventions hash is stale`; ruta čuva `37b78905f8887b313b11771e40784df8fe2ecfbb9a615dca4769539982713522`, a živi `conventions.json` ima bajtni SHA-256 `1d54f8cba9f62744d8c5b3a220ba00167181f846b3b19b59f13285a2f6122add` (Git LF blob `a2b05f067889a831efe808b17f841f34dd42b2a71b768d1167365c8c51a92dda`). |
| `python scripts/check-appendix-f.py` | `APPENDIX_F_CHECK_FAILED conventions file hash is stale`; ruta čuva `d6cce018793ede2266d0c980331a6f5c6d9eac7bcc074458ec9c086fc25beb44`, a isti živi `conventions.json` ima gornji bajtni SHA-256. |
| `python scripts/check-appendix-g.py` | `APPENDIX_G_CHECK_FAILED route artifact is stale`; usporedba spremljene rute i `build-appendix-g-route.py` razlikuje SHA polja Dodatka G, bibliografije, prvih izvora u poglavljima 1, 4 i 16, inventara widgeta, četiri uputnice prvoga pojavljivanja te kompozit `pathway.declared_inputs_hash`. Primjer: spremljeni `appendix_g.sha256=ea3d4b8f2cff02a2c393ca040ff9b1944d64b54946c7b64e42542816a1d081a9`, očekivani živi bajtni `9bb6149cd28da5f08a25fb04027ed204c292981042c5ee1698869bd9a4371fd6`. |

`git status --short` bio je čist. `git ls-files --eol` potvrđuje `i/lf w/crlf`
za katalog, konvencije i sve četiri rute; `core.autocrlf=true`. Zato su u
tablici odvojeni živi bajtni i Git LF otisci. Čak ni Git LF otisci kataloga i
konvencija nisu jednaki spremljenima. Nije dokazano da je sam završetak retka
jedini uzrok; četiri rute zahtijevaju zasebno usklađenje s kanonskim sadržajem.
Nijedan provjeritelj ni generirani artefakt nije promijenjen kako bi se pad
prikrio. Neovisni `KATALOG_OK` (20 paketa, 6 promoviranih) i
`PATHWAYS_CHECK_OK` ne zamjenjuju četiri pala rutna testa.

Prvi pokušaj `check-concepts.py` i `check-manuscript-integrity.py` naslijedio je
Windowsu nepodržani `LC_ALL=C.UTF-8`/`LC_CTYPE=C.UTF-8`. Nakon uklanjanja samo
tih varijabli oba su prošla na istim izvornim datotekama:
`CONCEPT_INTEGRITY_OK definitions=52 ledger_debt=0 graph_fresh=true` i
`MANUSCRIPT_INTEGRITY_OK lane=all`.

Nakon zapisivanja ovog stop stanja projektni launcher pokrenuo je
`scripts/check-review-workflow.R` uz uklonjene dvije nepodržane `LC_*`
varijable: exit 0, točna grana `revision/comprehensive-review`, samo aktivni
`P6-VERIFY`, 371 djece i 146 handoffa. Obje potrebne negativne probe ponovno
padaju zatvoreno: `BOOK_ARCHITECTURE_NEGATIVE_FIXTURE=missing_claim_dimension`
izlazi 1 jer nedostaje jedna od šest dimenzija, a
`ASSESSMENT_ARCHITECTURE_NEGATIVE_FIXTURE=protected_export_field` izlazi 1 zbog
zaštićenog polja u javnom AI izvozu. `git diff --check` prolazi.

## Zaustavljena dispozicija

Četiri pozitivna rutna testa jesu stvaran pad šire matrice. Po pravilu paketa
provjera ovdje staje. R04, R07, R27, R28–R31, R33 i R36 nisu promaknuti;
pet otvorenih R30 stavki ostaje `ratified`, a svih 19 poglavlja ostaje na
`coauthor_review`. Dostave `H-P2-VERIFY-001` i `H-P2-VERIFY-002` ostaju
`acknowledged`, ne `consumed`: njihove činjenice su provjerene, ali P6-VERIFY
nije zatvoren. `H-P6-EVIDENCE-008` i dalje čuva invalidaciju Dodatka G za P7.
Ni RDP/BDP obavijesti ni autorska suglasnost nisu pretvorene u dopuštenje
nositelja prava; knjizi nije pripisana neovisna terminološka recenzija.

Sljedeći nastavak istoga paketa mora prvo utvrditi zbog čega svaka od četiri
rute ne odgovara sadašnjim kanonskim ulazima i riješiti to bez slabljenja
provjeritelja ili izmišljanja prava. Tek zatim se mogu dovršiti pojedinačne
R30 presude i ostatak P6 matrice. Nema novoga buduće relevantnog učinka koji
nije ovdje zabilježen; nema novog izlaznog handoffa. Nisu izvršeni push,
merge, tag, arhiviranje, deployment ni objava.
