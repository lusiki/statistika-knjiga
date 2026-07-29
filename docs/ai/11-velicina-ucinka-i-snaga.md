# Veličina učinka i snaga

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Cohen je kritizirao praksu u kojoj je statistička značajnost zamjenjivala
razmišljanje o veličini i važnosti učinka (Cohen, 1994). Vrlo velik uzorak može
malu razliku učiniti lako uočljivom, dok mali uzorak može propustiti učinak
koji bi bio važan ljudima na koje se odluka odnosi.

Problem zato nije riješen pitanjem postoji li razlika. Istraživač mora prije
prikupljanja podataka odrediti koja bi razlika promijenila zaključak ili
postupanje. Tek tada veličina uzorka postaje planska odluka.

Koliko podataka trebamo da bismo pouzdano uočili učinak koji je vrijedan
uočavanja?

## Razlika koja nešto znači

**Veličina učinka** opisuje koliko su skupine, uvjeti ili varijable udaljeni na
ljestvici koja omogućuje usporedbu. Sirova razlika čuva izvorne jedinice i
često je najlakša za sadržajno tumačenje. Standardizirana razlika poput
Cohenova d izražava pomak u jedinicama zajedničke standardne devijacije
(Cohen, 1988).

Standardizacija ne odlučuje što je važno. Pragovi za „mali", „srednji" i
„veliki" učinak mogu služiti kao gruba orijentacija, ali društvena posljedica
ovisi o ishodu, trošku, vremenu i populaciji. Mala promjena može biti važna kada
se odnosi na mnogo ljudi ili na ozbiljan ishod.

Statistička i praktična važnost zato se izvještavaju odvojeno. Procjena i
interval govore koje su veličine usklađene s podacima. Sadržajna prosudba
govori koje bi od tih veličina opravdale odluku.

## Planiranje unatrag

**Statistička snaga** je vjerojatnost da postupak prepozna određeni učinak kada
on postoji. Raste s većim učinkom, većim uzorkom, manjom varijabilnošću i
liberalnijim pragom. Ti se čimbenici ne mogu tumačiti odvojeno od dizajna i
posljedica pogrešaka.

Slaba snaga ne proizvodi samo više propuštenih nalaza. Među rezultatima koji
ipak prijeđu prag procijenjeni učinci mogu biti nestabilni i pretjerani.
Planiranje zato počinje najmanjim učinkom vrijednim pažnje, željenom
preciznošću i dostupnim resursima, a ne pitanjem koliko je sudionika ostalo do
kraja semestra.

## Interakcija — Istraživač snage

Istraživač snage povezuje veličinu učinka, uzorak i prag. Čitatelj mijenja
jedan element dok ostale drži jednakima i vidi da ista odluka ima različite
posljedice za male i velike učinke.

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Usporedite snagu s očekivanom širinom intervala.

**Statistika u divljini.**
**Zemlja je okrugla.** Cohenov naslov sažima kritiku rituala u kojem poznata ili
trivijalna razlika dobiva oznaku važnosti samo zato što je p-vrijednost mala
(Cohen, 1994).

Odgovoran izvještaj navodi učinak i njegov interval, a zatim objašnjava što
raspon znači u sadržajnom kontekstu. Prag ne može obaviti tu prosudbu umjesto
istraživača i čitatelja.

**Pitajte model.**
Asistent može izračunati standardizirani učinak i provesti analizu snage, ali
mu treba dati dizajn, očekivanu varijabilnost i najmanji važan učinak.
Provjeravamo koristi li neovisni ili upareni postupak, brka li postignutu snagu
s kvalitetom rezultata i tretira li konvencionalni prag kao sadržajnu činjenicu.

> Planiraj uzorak iz najmanjeg učinka vrijednog pažnje, željene snage i
> odabranog dizajna. Prikaži osjetljivost zaključka na svaku pretpostavku.

**Nađite grešku.**
Procjena učinka i interval pravilno su izračunati, a dizajn je uzet u obzir.
Budući da je test statistički značajan, učinak je nužno dovoljno velik da bude
praktično važan.

Greška je izjednačavanje statističke značajnosti s praktičnom važnošću.
Praktična važnost zahtijeva sadržajni prag i tumačenje procjene u izvornim
jedinicama.

## Razrađeni primjer

Planiramo simuliranu usporedbu dviju neovisnih skupina. Ne polazimo od
očekivanja da ćemo „dobiti značajnost", nego od standardizirane razlike koju bi
imalo smisla pouzdano uočiti. Funkcija zatim pokazuje potreban broj jedinica po
skupini.

*Slika. Planiranje uzorka za nekoliko simuliranih scenarija. Izrada autora prema @cohen1988.*

Tablica pokazuje cijenu traženja manjih učinaka pod istim kriterijima. Konačan
plan ipak treba provjeru odustajanja, kvalitete mjerenja i izvedivosti. Račun
ne odlučuje koji je učinak vrijedan ulaganja.

## Sažetak

Veličina učinka vraća sadržaj pitanju koliko je razlika velika, a interval
pokazuje koliko je procjena precizna. Snaga povezuje učinak, uzorak,
varijabilnost i prag prije prikupljanja podataka. Statistička značajnost ne
određuje praktičnu važnost, a mali uzorci mogu iskriviti i otkrivene učinke.
Sljedeće poglavlje pokazuje što se događa kada sustav nagrađuje odluku, a
skriva cijeli put koji je do nje doveo.

## Pojmovi

veličina učinka (*effect size*), Cohenov d (*Cohen's d*), praktična važnost
(*practical significance*), statistička snaga (*statistical power*), najmanji
važan učinak (*smallest effect size of interest*), planiranje uzorka (*sample
size planning*)

## Zadaci

### Konceptualni

Objasnite kako velik uzorak može proizvesti statistički značajan, ali praktično
nevažan rezultat. Predajte jedan primjer bez stvarnih empirijskih brojki.

### Računski

Proširite objekt `scenariji` drugom željenom snagom i predajte tablicu potrebnih
uzoraka.

### Kritički

Prosudite Cohenovu kritiku odlučivanja samo prema pragu (Cohen, 1994). Predajte
kratak urednički standard za izvještavanje.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točne računske korake, jednu
pogrešnu prosudbu važnosti i podatak koji bi za tu prosudbu bio potreban.
