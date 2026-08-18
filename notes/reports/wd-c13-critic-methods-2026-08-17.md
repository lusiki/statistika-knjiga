# WD-C13 — metodološki kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom
`chapters/13-kategoricki-podaci.qmd`:

- SHA-256: `6cd97e3dae0a83dcf3daa8f7450fac0324390ef14b7df87308a29a6caa240015`
- podudaranje zadanog i opaženog izvora: da

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 2/5 |
| Pretpostavke | 3/5 |
| Interpretacija | 2/5 |
| Preciznost | 2/5 |

## Snage

- Prilagođeni standardizirani rezidual pravilno je definiran s korekcijom za
  rubne udjele, izračunan preko `stdres`, označen kao `e_ij` i jasno odvojen od
  Pearsonova reziduala i korelacije.
- Kalibracija pod nulom i snaga pod alternativom doista su dvije odvojene
  simulacije; alternative imaju unaprijed zadani populacijski Cramérov
  `V = 0,20`, isti prag i jasno evidentirane neprimjenjive tablice.
- Uvjetni nazivnici, vlasništvo nad kategorijama i kodiranje teksta kao mjerenje
  dobro ograničavaju interpretaciju te pripremaju kontingencijsku logiku za
  tablicu zabune u poglavlju 17.
- Glavnina poglavlja razlikuje globalni test, dijagnostiku ćelija i veličinu
  povezanosti te ne izvodi uzročni zaključak iz tablice.

## Nalazi

1. **Fatalno — rješenje okvira s pogreškom.** Tvrdnja da p-vrijednost raste s
   veličinom uzorka pogrešna je pri nepromijenjenim postotcima: hi-kvadrat
   statistika raste, a p-vrijednost pada. Kanonsko rješenje mora navesti taj
   smjer i jačinu vezati uz Cramérovo V ili sadržajni kontrast.
2. **Fatalno — tumačenje drugoga testa prilagodbe.** Neodbacivanje uz
   p-vrijednost ne znači da uzorak dobro odražava populacijsku strukturu.
   Zaključak treba ograničiti na to da test nije našao jasan nesklad s poznatim
   populacijskim udjelima, uz zaseban prikaz opaženih odstupanja ili intervala.
3. **Major — Fisherov egzaktni test.** Tablice s fiksnim rubovima nisu jednako
   vjerojatne. Opis treba govoriti o enumeriranju mogućih tablica i zbrajanju
   njihovih točnih uvjetnih, hipergeometrijskih vjerojatnosti prema unaprijed
   navedenom pravilu ekstremnosti.
4. **Major — izravna usporedba Cramérova V nakon prekodiranja.** Tablice `4 × 5`
   i `4 × 2` mjere povezanost s različito definiranom varijablom i imaju drukčiji
   normalizacijski član; puna tablica pritom ima najmanju očekivanu frekvenciju
   14,34. Digitalno/tradicionalno treba prikazati kao unaprijed sadržajno
   određenu, drukčiju procjenjivanu povezanost, bez tvrdnje da je ista veza
   ojačala ili da su uklonjene rijetke ćelije.
5. **Major — neizvjesnost u razrađenom primjeru.** Uvodni ugovor obećava
   izvještaj koji čuva neizvjesnost, a primjer daje postotke, V i testnu
   p-vrijednost bez intervala glavne procjene ili kontrasta. Potrebno je dodati
   odgovarajući interval i zaključak vezati uz ono što on dopušta.
6. **Major — povratak Berkeleyjevu slučaju.** Nije točno da bi „svaki postupak”
   iz poglavlja potvrdio nesklad s neovisnošću: test nezavisnosti daje globalni
   test, V mjeri jačinu, a reziduali lokaliziraju odstupanje. Treba imenovati
   hi-kvadrat test nezavisnosti i zadržati ostale alate u njihovim ulogama.
7. **Minor — rubni zbrojevi i stupnjevi slobode.** Treba razlikovati očuvanje
   opaženih rubova u prilagođenom nultom modelu od rubova fiksiranih dizajnom;
   samo Fisherov uvjetni račun izričito uvjetuje na oba ruba.

## Presuda

Poglavlje ne prolazi metodološki pregled dok se ne isprave smjer p-vrijednosti,
tumačenje neodbacivanja i ostale navedene inferencijske nepreciznosti.

## Završni ponovni pregled nakon odobrene dorade

Ponovni read-only pregled cijeloga izvora potvrdio je SHA-256
`b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`.
Svih osam odobrenih dorada prolazi: smjer p-vrijednosti, ograda testa
prilagodbe, Fisherov uvjetni račun, novo pitanje nakon prekodiranja, interval
glavnoga kontrasta, Berkeleyjeve uloge testa/V/reziduala, čitateljska ESS ruta
i statički blizanac s dva uzorka i stalnim `V = 0,20`.

| Dimenzija | Ocjena |
|---|---:|
| Točnost | 5/5 |
| Pretpostavke | 4/5 |
| Interpretacija | 5/5 |
| Preciznost | 4/5 |

### Snage

- P1A zaštite za prilagođeni standardizirani rezidual te odvojenu kalibraciju
  i snagu ostale su netaknute.
- Test, dijagnostika ćelija i veličina povezanosti dosljedno imaju zasebne
  uloge.
- Razrađeni primjer zajedno izvještava kontrast, interval, hi-kvadrat i V uz
  očuvanu uzročnu granicu.

### Preostali nalazi

1. **Minor — rubni zbrojevi i stupnjevi slobode.** U odjeljku „Zbroj odstupanja
   i njegov raspored” ostaje korisno razlikovati čuvanje opaženih rubova u
   prilagođenom modelu nezavisnosti od rubova unaprijed fiksiranih dizajnom;
   Fisherov račun zasebno uvjetuje na njih. Ovaj samostalni minor ostaje za
   `C13`.

### Završna presuda

Nema fatalnoga ni major nalaza. Konačni izvor prolazi metodološki ponovni
pregled uz jedan neblokirajući minor.
