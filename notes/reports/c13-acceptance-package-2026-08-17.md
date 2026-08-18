# C13 — paket za autorovo prihvaćanje trinaestoga poglavlja

**Gate:** `C13`

**Stanje gatea:** autor prihvatio; uska dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum autorove odluke:** 17. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor trinaestoga poglavlja nalazi se u commitu
`a88fc80ad1b323f514e3e50d51c5da49fea07bd8`. Taj commit sadrži cijeli
`WD-C13` vertikalni rez, šest završnih kritičarskih izvještaja, sintezu i
closeout dokaze. Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`;
- git blob poglavlja: `e7ff4e8adc9d2438461ffbddb01e193aba24b671`;
- izvještaj vertikalnoga reza:
  `notes/reports/wd-c13-2026-08-17.md`;
- sinteza panela:
  `notes/reports/wd-c13-six-critic-synthesis-2026-08-17.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pregledalo je upravo navedeni završni
SHA-256:

1. metode — `notes/reports/wd-c13-critic-methods-2026-08-17.md`;
2. skepticizam — `notes/reports/wd-c13-critic-skeptic-2026-08-17.md`;
3. pedagogija — `notes/reports/wd-c13-critic-pedagogy-2026-08-17.md`;
4. dokazi i citati — `notes/reports/wd-c13-critic-evidence-2026-08-17.md`;
5. hrvatski stil — `notes/reports/wd-c13-critic-style-2026-08-17.md`;
6. struktura — `notes/reports/wd-c13-critic-structure-2026-08-17.md`.

Završni panel bilježi nula fatalnih, nula major i četrnaest neblokirajućih
minor zapisa po lećama. Strukturna leća nema završni minor. Zajednički hash
nije mijenjan nakon panela.

## Osam razriješenih obveznih nalaza

Autor je 17. kolovoza 2026. prethodno odobrio točno osam obveznih dorada. Sve
su provedene i ponovno neovisno provjerene:

1. pri nepromijenjenim postotcima veći uzorak pravilno povećava hi-kvadrat i
   smanjuje p-vrijednost;
2. neodbacivanje testa prilagodbe više nije dokaz jednakosti, a prikazuje se i
   najveće opaženo odstupanje udjela;
3. Fisherov egzaktni test enumerira moguće tablice i zbraja njihove točne
   uvjetne hipergeometrijske vjerojatnosti prema unaprijed određenoj
   ekstremnosti;
4. binarno prekodiranje jest unaprijed određeno novo pitanje, a dva Cramérova V
   služe provjeri osjetljivosti bez rangiranja kodnih shema;
5. glavni kontrast udjela dobio je 95-postotni interval pouzdanosti;
6. Berkeleyjev povratak razdvaja globalnu ulogu hi-kvadrat testa, jačinu preko
   V i lokalizaciju preko reziduala;
7. ESS je opcionalna čitateljeva portalna provjera s valjanim nazivnikom i
   `anweight`, bez lažne rute Dodatka C;
8. statički blizanac pokazuje isti relativni pomak uz dva uzorka: hi-kvadrat
   raste s 1,6 na 6,4, dok V ostaje 0,20.

## Četrnaest minor zapisa i autorska dispozicija

Točan odgovor autora prihvaća završni WD-C13 commit i sintezu panela. Sljedeći
zapisi zato su autoru izloženi, poznati i neblokirajući za ovo izdanje; nisu
uređivani nakon zaključavanja izvora.

### Metode — 1

1. Opis stupnjeva slobode mogao bi razlikovati čuvanje opaženih rubova u
   prilagođenom modelu nezavisnosti od rubova unaprijed fiksiranih dizajnom.

### Skepticizam — 2

2. Postotak po retku naziva se „pravim”, iako je preciznije reći da je
   prikladan za postavljeno pitanje.
3. Simulirani nastavni rezultat nakratko prelazi u stvarnu uredničku odluku bez
   imenovane ciljne populacije i kriterija odluke.

### Pedagogija — 3

4. Cramérovo V pojavljuje se brojčano u widgetu prije kasnijega objašnjenja.
5. Vidljivi račun ne razdvaja sasvim jasno pripremu prekodiranja od
   analitičkoga poziva za čitatelja bez programiranja.
6. Završni zadaci ne traže izrijekom imenovanje uvjetnoga nazivnika.

### Dokazi — 4

7. Tvrdnja da sve brojke potječu iz uzorka od 800 preširoka je za zasebne
   simulacije i teorijsku granicu.
8. Komparativna tvrdnja o učestalosti izostavljanja nazivnika nema izravnu
   dokaznu potporu.
9. Cochran podupire praktični status pravila pet, ali ne i zasebnu tvrdnju o
   njegovoj učestalosti u udžbenicima, recenzijama i programskim izlazima.
10. Tvrdnje o tome što asistenti „obično”, „često” i „redovito” rade nisu
    vezane uz evaluaciju, model ni verziju.

### Hrvatski stil — 4

11. Rečenica o „dva statička panela” izvan je PDF ograde pa HTML čitatelju
    spominje panele koje ne vidi.
12. Prijelaz „Ista mjerna granica” mogao bi imati izravniji antecedent.
13. Niz „Prva je… Druga je… Treća je…” u okviru o modelu kratko djeluje kao
    prikriveni popis.
14. Završni popis pojmova ne slijedi potpuno redoslijed njihova uvođenja.

Broj četrnaest označava zapise po lećama, ne nužno četrnaest potpuno neovisnih
defekata. Nijedan završni kritičar nije ocijenio ijedan zapis fatalnim ili
velikim.

## Materijalna osnova prihvaćanja

Poglavlje otvara Dio V ugovorom o čitanju obitelji modela, a jednu
kontingencijsku tablicu vodi od jedinice, nazivnika i očekivanja do globalnoga
testa, lokalizacije, veličine veze, osjetljivosti i granice tvrdnje. Kodirani
tekst ostaje mjerna odluka s imenovanim vlasnikom kategorije i priprema
tablicu zabune u poglavlju 17. Kritički Berkeleyjev zadatak stvarno dohvaća
Simpsonov paradoks i ne može se riješiti samo trenutačnom metodom.

Konceptni graf svjež je s 49 čvorova i 578 bridova, bez nove definicije.
Widget-registar i statički blizanac prolaze ugovor i paritet. Ciljani HTML,
odobreni PDF wrapper i DOCX wrapper imaju zabilježene prolaze. ESS ostaje
opcionalan, portalno posredovan i nepromoviran, dok `populacija_medija` ostaje
obvezni licencirani lokalni put.

## Provedena uska dispozicija

C13 nakon provjere točnoga odgovora provodi samo sljedeće:

- pomiče `13-kategoricki-podaci` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomiče iz `ratified` u `accepted` samo `R13-C13-contingency`,
  `R27-C13-partV-contract` i `R35-REACHBACK-13`;
- evidentira četrnaest minor zapisa kao autoru izložene, poznate i
  neblokirajuće za ovo izdanje, bez promjene zaključanoga izvora;
- ostavlja poglavlje 6 u fazi `draft` i `H-WB-PART-001` netaknutim;
- ostavlja preostale dostave `H-P3-ESS-001` za WD-C14–WD-C16 i
  `H-WC-PARTS-DOCX-001` za P7-DOCX netaknutima.

Nijedna druga stavka ni poglavlje ne mijenja status.

## Granice odluke

C13 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge, tag,
arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao poglavlje.
`WD-C14` se smije otvoriti tek nakon dovršenoga C13 closeouta, workflow
provjere i zasebnoga lokalnog commita.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
C13 accepted for a88fc80ad1b323f514e3e50d51c5da49fea07bd8 on 2026-08-17.
```

Odgovor navodi točan završni WD-C13 commit i datum odluke. Raniji odgovor bez
prefiksa `C` nije upotrijebljen kao prihvaćanje, stalna delegacija od 5.
kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.
