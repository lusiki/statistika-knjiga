# Završni prolaz mrežnog sučelja — 26. listopada 2026.

Opseg je korisnikova odobrena estetska i funkcionalna revizija mrežne knjige.
Ovo nije zatvaranje uredničkih paketa ni potvrda konačnoga izdanja. Tekst
poglavlja, statistički postupci i podatkovne datoteke nisu mijenjani.

| Nalaz pregleda | Provedba |
|---|---|
| N01 | Čišćenje navigacije uspoređuje put s početnom kosom crtom; poglavlje 13 više ne odgovara putu samostalne stranice Podaci. |
| N02 | Jedan vidljiv gumb pretrage u zaglavlju na svim širinama; zatvaranje vraća fokus na gumb. |
| R01 | Široke tablice i formule pomiču se unutar vlastitih označenih regija. Dugi nazivi datoteka prelamaju se, a citirani floatovi ostaju unutar stupca. |
| N03 | Nedovršene stranice uklonjene su iz glavnog izbornika. Stare adrese i dalje postoje te nude dostupne materijale. |
| G01–G04 | Čitljive kategorije u obje teme, vidljiva odabrana definicija na telefonu, jasan prijelaz iz pojma u kategoriju, jedan ulaz tipkovnicom u mrežu i izravan ulaz u A–Ž. Strelice biraju pojam; Shift i strelica pomiču ga. |
| I01 | Graf i osnovne kontrole prethode sklopivom bloku predviđanja i objašnjenja. |
| D01 | Podaci nude šest dostupnih skupova, izravna preuzimanja, tražilicu i odabir poglavlja. Izvorni katalog s metapodacima ostaje u sklopivom bloku; izvorni identifikatori i poveznice ostaju valjani. |
| A01 | Odabir poglavlja je otvoren, odabrani naslov vidljiv, a preuzimanje i kopiranje mentorske upute vode radnju. Neuspjeh kopiranja javlja se korisniku. |
| S01 | Provjere rješenja imaju odabir poglavlja i indeks zadataka. Izravne poveznice otvaraju pripadajuće poglavlje; bez JavaScripta ostaje potpuni izvorni tekst. |
| N04, P01 | Praktikum ima točno aktivno mjesto u izborniku, izbor R/jamovi i brze ulaze. Oporavak sa stranice 404 vodi na prvo poglavlje. |
| T01 | Naslovi se ne rastavljaju spojnicom; sitne oznake imaju veći slog; objašnjenja u rječniku poravnana su lijevo. Način čitanja centrira tekst i premješta rubne bilješke u tok. |
| N05 | Podnožje nudi radni PDF, prijavu problema i predložak navoda. Navod i evidencija jasno ostaju predobjavni. |
| U01 | Stanje sklopivih blokova opisano je točno; dijeljenje nudi kopiranje poveznice; vanjska strelica ostaje samo uz vanjske odlaske. Raspored je preimenovan u Plan učenja i povezuje odgovarajuće odjeljke praktikuma. |
| V01 | Sačuvani su statična naslovnica, izvorne autorske poveznice, profilne stranice, paleta i tri obitelji pisama sustava Zvono. |

Tijekom provjere otkriven je i prazan AI izvoz predgovora. Izvoznik je pogrešno
odbacivao i sadržaj skriven u PDF-u, odnosno vidljiv na webu. Ispravljen je uvjet
vidljivosti. Pozitivna provjera sada zahtijeva sadržaj svih 19 poglavlja i
razlikuje mrežni od isključivo tiskovnog bloka; provjere zaštite nastavničkih
odgovora ostaju aktivne.

## Provjera

- Potpuni HTML render svih 41 kanonskih stranica.
- `audit-site-review.cjs`: 252 kombinacije (42 adrese uključujući korijen,
  tri širine 1440/390/320 px i dvije teme), bez proširenja dokumenta i bez
  nedostajućih oznaka pomicanja tablica. Provjerene su i glavne korisničke radnje.
- `audit-learning-tools.cjs`: svih 17 simulacija, promjena parametara,
  usporedba rezultata, ponovljivost podijeljene poveznice, mobilna širina,
  autorske poveznice i mreža pojmova.
- `audit-rendered-html.js --smoke`: tipkovnica, povratak početnih vrijednosti,
  galerija, duboke poveznice, pomicanje čvorova, smanjeno kretanje i prikaz bez JS-a.
- Inventar, provjere ruta, struktura rukopisa, uvodi figura, citati, pojmovi,
  tokeni i svih 17 parova interakcija i tiskovnih prikaza prošli su lokalne provjere.
- Nova provjera sučelja dio je CI postupka prije objave.

Pregled u pregledniku nije potvrda na fizičkim iOS/Android uređajima ili sa
svim čitačima zaslona. Povijesni validator `check-release-governance.R` uključuje
statične kontrolne zbrojeve staroga dokaza i postojeću granicu kolofona; nije
obnovljen ni proglašen prolaznim ovim zahvatom. Registar uredničke revizije i
pravila zaključavanja konačnoga izdanja ostaju zasebni.
