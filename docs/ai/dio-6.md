# ZAVRŠNICA

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Vaše prvo istraživanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/18-vase-prvo-istrazivanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | bez widgeta | simulacija | pogl. 2, 5 i 16 |

**Vinjeta.**
Na kraju kolegija istraživački tim ima rok, zanimljivo pitanje i datoteku koja
još nije spremna za analizu. Jedan član želi odmah otvoriti model, drugi želi
prvo popraviti mjerenje, a treći predlaže da cijelu datoteku pošalju javnom AI
asistentu kako bi uštedjeli vrijeme.

Moramo odlučiti što je jedinica analize, odakle podaci dolaze, koja je tvrdnja
unaprijed postavljena i koje su varijable osjetljive. Tek nakon toga možemo
opisati uzorak, nacrtati raspodjele i odabrati model.

Kako završiti prvo istraživanje tako da se svaki zaključak može provjeriti i da
odgovornost ne nestane između podataka, koda i asistenta?

## Istraživanje kao trag odluka

Počinjemo pitanjem koje se može povezati s jedinicom analize, populacijom,
mjerama i usporedbom. Razlikujemo opisno pitanje od prediktivnog i uzročnog.
Ta odluka određuje dizajn, a dizajn granicu zaključka koju ne smijemo kasnije
proširiti zato što rezultat izgleda zanimljivo.

Prije analize stvaramo zapis podrijetla podataka, licence, načina prikupljanja i
svih koraka čišćenja. Ne prepisujemo izvornu datoteku. Svaka izvedena varijabla
dobiva objašnjenje, a svako isključivanje razlog koji se može pregledati.

Plan razlikuje potvrđujuće odluke donesene prije gledanja ishoda od
istraživačkih odluka koje su nastale nakon njega. Neočekivan obrazac smijemo
istražiti. Ne smijemo ga naknadno predstaviti kao jedinu unaprijed postavljenu
hipotezu.

**Statistika u divljini.**
**Izvještaj koji nosi procjenu.** Pristup usmjeren na procjene traži da
izvještaj vodi veličinom učinka i intervalom, a ne samo binarnom odlukom
(Cumming, 2014).

U našem radu to znači da tablica i graf moraju pokazati jedinice, ljestvice i
neizvjesnost. Metoda dolazi uz razlog odabira, a zaključak uz granicu
generalizacije.

**Pitajte model.**
Asistent može predložiti kod, provjeriti dosljednost i kritizirati nacrt
izvještaja. Dajemo mu strukturu ili potpuno simulirane podatke, a ne osobne
odgovore ispitanika. Svaki dobiveni kod pokrećemo lokalno, svaku brojku
uspoređujemo s izlazom i svaki izvor otvaramo.

> Pomozi mi provjeriti ovaj plan i reproducibilan kod. Odvoji statistički račun
> od sadržajne prosudbe, označi što moram ručno provjeriti i ne traži osobne
> podatke sudionika.

**Nađite grešku.**
Tim je sačuvao izvornu datoteku, dokumentirao čišćenje i pokrenuo kod lokalno.
Kako bi dobio bolji opis uzorka, učitao je neanonimiziranu datoteku s odgovorima
i kontaktnim podacima u javni model.

Greška je slanje osobnih podataka javnom modelu. Reproducibilnost i korisnost
alata ne uklanjaju obvezu privatnosti, minimizacije podataka i odobrenog načina
obrade.

## Razrađeni primjer

Vodimo jedno potpuno simulirano istraživanje o odnosu vremena izloženosti
informativnom sadržaju i rezultata na kratkom testu znanja. Simulacija nam
omogućuje prikaz cijelog postupka bez izmišljanja empirijskog nalaza o stvarnim
studentima.

### Pitanje i jedinica analize

Najprije zapisujemo pitanje. Zanima nas opisna povezanost dviju varijabli u
simuliranom uzorku, ne uzročni učinak. Jedinica analize je osoba, a ishod
rezultat testa. Dodatno bilježimo prethodni interes jer može biti povezan i s
izloženošću i sa znanjem.

### Simulacija i provjera podataka

Prije modela pregledavamo nedostajuće vrijednosti, raspodjele i moguće
nemoguće vrijednosti. Simulacija nema nedostajuće podatke, ali kod za provjeru
ostaje dio analize jer stvarna datoteka gotovo nikada nije tako uredna.

*Slika. Opis simuliranih varijabli prvog istraživanja. Izrada autora.*

### Graf prije modela

Graf prethodi modelu jer moramo vidjeti linearnost, krajnja opažanja i
raspršenost. Ne tumačimo nagib prije nego što provjerimo odgovara li pravac
obliku podataka.

Sljedeća slika prikazuje rezultat te provjere za simulirani uzorak.

Izloženost i znanje u simuliranom istraživanju. Izrada autora.

### Zbirni i prilagođeni model

Jednostavni model opisuje zbirni odnos. Prilagođeni model dodaje prethodni
interes i pokazuje kako se koeficijent mijenja kada uspoređujemo osobe s
jednakim simuliranim interesom.

*Slika. Koeficijent izloženosti u dvama simuliranim modelima. Izrada autora.*

### Ograničeni zaključak i trag odluka

Zaključak pišemo skromno. U simuliranom uzorku veća izloženost povezana je s
višim rezultatom, a dio zbirne povezanosti dijeli se s prethodnim interesom.
Ne tvrdimo da izloženost uzrokuje znanje jer opažački model i uključivanje
jedne kontrole ne identificiraju uzrok.

Na kraju spremamo skriptu, verziju podataka, izlaz i bilješku o korištenju
asistenta. Čitatelj mora moći ponoviti tablicu i graf bez pristupa našem
razgovoru s modelom. Objavljujemo samo ono za što imamo pravo i uklanjamo
izravne identifikatore prema unaprijed odobrenom protokolu.

## Sažetak

Prvo istraživanje završavamo tragom odluka od pitanja do ograničenog zaključka.
Mjerenje, dizajn, opis, graf i model moraju govoriti o istoj jedinici i istoj
populaciji. Asistent može ubrzati račun i provjeru, ali ne dobiva osobne podatke
i ne postaje izvor. Reproducibilan rad omogućuje da nalaz provjerimo i kada
rezultat nije onakav kakav smo očekivali.

## Pojmovi

istraživački plan (*research plan*), trag odluka (*decision trail*),
potvrđujuća analiza (*confirmatory analysis*), istraživačka analiza
(*exploratory analysis*), reproducibilan tijek rada (*reproducible workflow*),
minimizacija podataka (*data minimization*), objava uporabe AI-ja (*AI
disclosure*)

## Zadaci

### Konceptualni

Napišite istraživačko pitanje i odvojite opisni, prediktivni i uzročni oblik
istog pitanja. Predajte tri rečenice s granicom svakog zaključka.

### Računski

Upotrijebite `sim_projekt`. Reproducirajte tablicu, graf i oba modela te
predajte jednu izvršivu skriptu i kratak izvještaj.

### Kritički

Uredite izvještaj tako da procjena i interval prethode odluci o testu
(Cumming, 2014). Predajte izvorni i revidirani odlomak.

### Revizija modela

Ocijenite postupak iz okvira. Imenujte dobre reproducibilne odluke, jednu
povredu privatnosti i siguran način dobivanja iste vrste pomoći.
