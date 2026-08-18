# WD-C13 — pedagoški kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom:

- SHA-256: `6cd97e3dae0a83dcf3daa8f7450fac0324390ef14b7df87308a29a6caa240015`

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Jasnoća | 4/5 |
| Postupnost | 4/5 |
| Preduvjeti | 5/5 |
| Kvaliteta zadataka | 4/5 |

## Snage

- Otvaranje Dijela V jasno nastavlja obnovljenu praksu iz poglavlja 12 i model
  određuje kao očekivanje uz pretpostavke, usporedbu, jačinu, granice i
  odgovorno izvještavanje.
- Slijed je prikladan početniku: brojanje i nazivnik prethode neovisnosti;
  widget prethodi formuli; zatim dolaze statistika, reziduali, V, referentna
  raspodjela te odvojene simulacije kalibracije i snage.
- Most prema poglavlju 17 imenuje tekstnu jedinicu, prihvatljivost za korpus,
  vlasnika kodne knjige, nekodirane i višestruko kodirane jedinice te uvjetni
  nazivnik.
- Sva četiri tiera zadataka postoje bez proizvodnje koda, a kritički dohvat
  traži stvarnu usporedbu zbirne i odjelskih shema Simpsonova paradoksa.

## Nalazi

Sva su tri nalaza minor:

1. Widget prikazuje Cramérovo V oko 240 redaka prije njegova sadržajnog
   objašnjenja. U toj fazi status bi mogao imenovati samo ukupno odstupanje, a
   čitatelja se na V može vratiti nakon njegove definicije.
2. Vidljivi račun razrađenoga primjera počinje internim objektom i nosi
   neprotumačeno prekodiranje kroz `mutate`, `if_else` i `%in%`. Prekodiranje i
   pripremu tablice valja premjestiti u skriveni blok ili ih izravno objasniti,
   a vidljivi račun svesti na čitljiv analitički trag.
3. Uvjetni nazivnik nosiv je pojam i most prema poglavlju 17, ali nema kanonski
   `#def-` blok ni izričitu provjeru u zadacima. Definicija i zahtjev da student
   imenuje nazivnike pojačali bi dohvat bez dodavanja koda.

## Presuda

Pedagoški prolaz bez fatalnih ili major nalaza; tri manja popravka učinila bi
widget, račun i završnu provjeru dosljednijima početniku.

## Završni ponovni pregled nakon odobrene dorade

Ponovni read-only pregled cijeloga izvora potvrdio je SHA-256
`b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`.
Svih osam odobrenih dorada prolazi. Digitalni i statički put sada nose isti
uvid o veličini uzorka i V, interval dovršava ugovor o neizvjesnosti, a
Berkeleyjev dohvat traži stvarni povratak Simpsonovu paradoksu.

| Dimenzija | Ocjena |
|---|---:|
| Jasnoća | 4/5 |
| Pedagoška skela | 4/5 |
| Preduvjeti | 5/5 |
| Kvaliteta zadataka | 4/5 |

### Snage

- Ograda GOF zaključka, razdvajanje uloga testa/V/reziduala i novo pitanje
  nakon prekodiranja sada su jasno čitljivi početniku.
- Četiri razreda zadataka ostaju rješiva bez proizvodnje koda.
- Kodirani tekst i imenovani nazivnik grade uredan most prema poglavlju 17.

### Preostali nalazi

1. **Minor — rana pojava V.** Widget i statički blizanac prikazuju Cramérovo V
   prije njegova kasnijeg objašnjenja; kratka najava mogla bi reći da V prati
   relativnu jačinu.
2. **Minor — vidljiva priprema računa.** U razrađenom primjeru `mutate`,
   `if_else` i `%in%` početniku ne razdvajaju pripremu od analitičkoga poziva;
   budući prolaz može to kratko protumačiti ili sakriti pripremu.
3. **Minor — provjera uvjetnoga nazivnika.** Nosivi pojam ostaje bez izričitoga
   zahtjeva u završnim zadacima; ako ne dobije novi `#def-` blok, zadatak može
   tražiti imenovanje nazivnika.

Sva tri samostalna minora ostaju za `C13`.

### Završna presuda

Nema fatalnoga ni major nalaza. Pedagoški ponovni pregled prolazi uz tri
neblokirajuća minora.
