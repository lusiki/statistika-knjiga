# Autorove prethodne dispozicije — podatkovni izbori, 10. kolovoza 2026.

**Nositelj:** Luka Šikić, autor i urednik.

**Izvorno stanje:**
`conversation:author-data-pre-dispositions-2026-08-10-Luka-Sikic`.

Ovaj dokument bilježi autorove odgovore dane prije nego što ih je nadležni gate
mogao potrošiti. On **ne zamjenjuje** nijedan gate i ne odobrava nijedan paket.
Svaki gate i dalje mora obaviti vlastiti posao, provjeriti vlastite izvore i
zabilježiti vlastiti dokaz. Ako se dispozicija i nalaz gatea raziđu, gate staje i
vraća pitanje autoru.

Nastavlja `notes/reports/author-pre-dispositions-2026-08-05.md`, koji je istim
obrascem zabilježio odgovore o DZS-u i DIP-u.

## Eurostat — odabir pokazatelja, godina i zemlje

**Pitanje:** kojih pet do sedam pokazatelja, iz koje jedne godine, za koje
zemlje.

**Odgovor:** prihvaćeno kako je preporučeno — **najmanji skup koji odgovara na
pitanja koja poglavlja doista postavljaju, uz vidljivo ostavljene oznake
nedostajućih podataka.** Uz to vrijedi autorova opća uputa da snimka bude
**najnovija moguća**.

**Kako se to čita:**

- *Najmanji skup* znači da svaki pokazatelj mora imenovati poglavlje i pitanje
  zbog kojega ulazi. Pokazatelj koji nema svoje pitanje ne ulazi, koliko god bio
  zanimljiv. Registar traži pet do sedam; donja granica jednako obvezuje kao i
  gornja.
- *Jedna zajednička godina* ostaje uvjet iz `R08-EUROSTAT-package`, čiji test
  izrijekom traži da mješovite godine padnu i da svaka prihvaćena vrijednost
  zemlje i pokazatelja bude iz iste godine ili izričito označena kao
  nedostajuća.
- *Najnovija moguća* čita se kao **najnovija godina u kojoj svih pet do sedam
  pokazatelja postoji za odabrani skup zemalja**, a ne najnovija godina bilo
  kojega pojedinog pokazatelja. Ako bi najnovija godina jednoga pokazatelja
  razbila zajedničku godinu, prednost ima zajednička godina, jer je
  usporedivost cijeli smisao paketa.
- *Oznake ostaju vidljive.* Eurostatove oznake kvalitete i nedostajuće
  vrijednosti prenose se kakve jesu. Ne prekodiraju se u nulu, ne popunjavaju se
  i ne izostavljaju se retci koji ih nose. Zemlja bez objave ostaje vidljiva kao
  zemlja bez objave.

**Zašto tako:** poglavlje 6 na tom paketu uči usporedivost i granicu ekološke
interpretacije. Skup u kojemu su rupe zatrpane ne bi mogao poučiti ni jedno ni
drugo.

**Tko to izvršava:** `G-A3-EUROSTAT` bilježi odabir, zajedničku godinu, zemlje i
potrošače; `P3-EUROSTAT` prikvačuje točne kodove skupova, upit, datum snimke,
kontrolni zbroj i pripisivanje. **Nijedan kod pokazatelja, nijedna godina i
nijedna zemlja nisu ovdje imenovani**, jer bi to bila tvrdnja o objavi koju ovaj
zapis nije provjerio.

## Eurostat — uvjeti ponovne uporabe i pripisivanje

**Pitanje:** utvrđuju li se Eurostatovi uvjeti pripisivanja provjerom ili
autorovom odredbom.

**Odgovor:** autor je uputio da izbor bude **svjesna odluka, a ne propust**.

**Kako se to čita i što je ostalo otvoreno:** `data/katalog.yml` već bilježi
uvjete za `eurostat_drustvo` — ponovna uporaba uz priznanje izvora, oznaku
izmjena i propisani disclaimer, uz iznimke za sadržaj trećih strana. To je zapis
iz inventara `P1B-DATA-LIC`, a **ne** provjera vezana uz točnu snimku i točan
upit, koju `R03-EUROSTAT-rights` traži svojim testom.

Zato ovaj zapis **ne proglašava pitanje riješenim**. `OA-G-A3-EUROSTAT-RIGHTS`
ostaje otvorena i pripada `G-A3-EUROSTAT`, koji mora učiniti jedno od dvoga i
zabilježiti što je učinio:

1. provjeriti mjerodavnu objavljenu obavijest o ponovnoj uporabi i iz nje
   prepisati točan tekst pripisivanja i disclaimera; ili
2. zabilježiti autorovu vlastitu odredbu, kao što je učinjeno za DZS i DIP 5.
   kolovoza 2026.

Razlika je bitna za jednu stvar više nego kod DZS-a: Eurostatovi uvjeti nose
**iznimku za sadržaj trećih strana**, pa `P3-EUROSTAT` mora pokazati da odabrani
pokazatelji u tu iznimku ne ulaze. Katalog to već traži u `integrity.note` toga
paketa.

**Što ostaje zabranjeno:** knjiga ne smije tvrditi da je pribavila dopuštenje
nositelja prava ni za jedan izvor, jer ono nije traženo, i ne smije iz tehničke
dostupnosti API-ja izvesti širu ovlast. `H-P1B-DATA-LIC-003` nije nadomješten i
ostaje obveza `G-A3-EUROSTAT`.

## Što ovaj zapis nije napravio

Nijedan paket nije promoviran, nijedan pokazatelj odabran, nijedan podatak
dohvaćen i nijedan unos u katalogu promijenjen. `eurostat_drustvo` ostaje
`portal-mediated`, `promoted: false`, s praznim popisom datoteka.
