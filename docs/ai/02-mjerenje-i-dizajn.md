# Mjerenje i istraživački dizajn

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/02-mjerenje-i-dizajn.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Berkeleyjski podaci iz prethodnog poglavlja bilježili su prijave, ishode upisa,
spol kandidata i odjel. Nisu bilježili kvalitetu prijave, savjet koji je
kandidat dobio prije prijave ni način na koji su pojedini odjeli donosili
odluke (Bickel, 1975). Tablica je zato mogla pokazati raspored ishoda, ali nije
mogla izravno izmjeriti svaki postupak koji je do tih ishoda doveo.

Istraživači su se morali vratiti korak unatrag. Prije pitanja o razlici trebalo
je utvrditi što pojedini redak predstavlja, koje su usporedbe opravdane i koje
alternativne priče podaci još dopuštaju. Više računanja nije moglo nadomjestiti
ono što nije bilo izmjereno.

Kako društvenu pojavu pretvaramo u podatke, a da pritom ne zamijenimo mjeru za
pojavu koju želimo razumjeti?

## Mjerenje prije računanja

Društvene znanosti najčešće proučavaju pojave koje ne možemo položiti na vagu.
Povjerenje, politička otuđenost, osjećaj sigurnosti i izloženost medijima
moraju se prevesti u opažanja. Taj se prijevod naziva **operacionalizacija**.
Isto teorijsko pitanje može postati jedno anketno pitanje, skup tvrdnji,
ponašajni trag ili procjena promatrača. Svaki izbor zahvaća dio pojave i
istodobno nešto izostavlja.

Varijabla nije samo stupac s urednim imenom. Ona je trag odluke o tome što će
se računati kao razlika među opažanjima. Nominalna mjera razvrstava u
kategorije, ordinalna čuva redoslijed, intervalna dopušta usporedbu razlika, a
omjerna ima smisleno ishodište. Razina mjerenja ne određuje koliko je tema
važna. Određuje koje će računske operacije imati sadržajno značenje.

Dobra mjera mora biti dovoljno postojana da slične slučajeve ne raspoređuje
proizvoljno. Tu postojanost nazivamo **pouzdanošću**. Istodobno mora zahvatiti
upravo pojavu o kojoj želimo zaključivati, što opisujemo **valjanošću**.
Pouzdana mjera može svaki put jednako promašiti cilj. Valjana mjera bez
pouzdanosti ne dopušta razlikovanje stvarne promjene od pogreške mjerenja.

## Dizajn i doseg zaključka

Podaci nasljeđuju snage i slabosti postupka kojim su nastali. U eksperimentu
istraživač mijenja jedan uvjet i nasumično raspoređuje jedinice, pa skupine
prije intervencije nastoji učiniti usporedivima. U opažačkoj studiji bilježi
svijet kakav jest. Takva studija može obuhvatiti prirodnije okolnosti i širu
populaciju, ali razliku među skupinama ne može automatski pripisati jednom
uzroku.

Treća varijabla koja je povezana i s mogućim uzrokom i s ishodom može stvoriti
ili prikriti vezu. Nazivamo je **konfundirajućom varijablom**. Njezino
prepoznavanje počinje sadržajnim znanjem, a ne naredbom u programu. Program
može prilagoditi model za dob, obrazovanje ili prethodno ponašanje tek nakon što
netko obrazloži zašto su baš te varijable važne i kako su izmjerene.

Anketa dodaje još jednu razinu dizajna. Formulacija pitanja određuje što
ispitanik razumije, ponuđeni odgovori određuju što smije reći, a okvir
uzorkovanja određuje tko uopće može biti izabran. Velik broj odgovora ne
popravlja sustavno izostavljanje dijela populacije. Precizno mjerenje pogrešne
skupine ostaje precizno mjerenje pogrešne skupine.

## Interakcija — Prikaz konfundera

Planirani prikaz pokazuje odnos dviju varijabli prije i nakon uključivanja
treće. Opažanja ostaju ista, ali se mijenja usporedba. Čitatelj tako vidi da
statistička prilagodba ne briše podatke, nego pita kako bi izgledala veza među
jedinicama koje su slične prema relevantnom obilježju.

**Što isprobati.**

1. Promatrajte početnu vezu bez treće varijable.
2. Uključite konfundirajuću varijablu i usporedite smjer veze.
3. Promijenite njezinu povezanost s ishodom i pronađite slučaj u kojem se
   početni zaključak preokreće.

**Statistika u divljini.**
**Što mjeri stopa prijma.** Zbirna stopa u Berkeleyju opisivala je ishod
prijava, ali nije sama mjerila namjeru, kriterije odlučivanja ni iskustvo
kandidata (Bickel, 1975). Pretvaranje te stope u potpunu ocjenu pravednosti
preskače operacionalizaciju pojma pravednosti.

Odgovorno čitanje zato najprije pita koja je jedinica analize i koje su
varijable dostupne. Tek nakon toga procjenjuje koji dizajn može razlikovati
suparnička objašnjenja.

**Pitajte model.**
Asistent može pretvoriti istraživačko pitanje u nacrt varijabli i upozoriti na
moguće konfundere. Njegov popis nije dokaz da su mjere valjane. Treba provjeriti
odgovara li svaka predložena varijabla stvarnom instrumentu, tko nedostaje iz
okvira uzorkovanja i dopušta li dizajn kauzalni zaključak.

> Za ovo istraživačko pitanje predloži jedinicu analize, način mjerenja ishoda,
> mogući konfundirajući čimbenik i dizajn. Za svaku odluku navedi što se iz
> prikupljenih podataka neće moći zaključiti.

**Nađite grešku.**
U opažačkoj anketi studenti koji dulje koriste društvene mreže prijavili su
niže povjerenje u institucije. Obje su varijable izmjerene istim upitnikom i
analiza je uključila dob. Rezultat zato dokazuje da dulje korištenje društvenih
mreža smanjuje povjerenje.

Greška je tvrdnja o dokazanom uzroku. Istodobno mjerenje dviju varijabli i
prilagodba za dob ne uklanjaju obrnuti smjer veze ni druge neizmjerene
konfundirajuće čimbenike.

## Razrađeni primjer

Zamislimo istraživanje povjerenja u lokalne institucije. Teorijski pojam
pretvaramo u tri tvrdnje s istom ljestvicom odgovora. Prije računanja ukupnog
rezultata pregledavamo nedostajuće vrijednosti, smjer svake tvrdnje i slažu li
se odgovori dovoljno da ih ima smisla sažeti.

Sljedeći kod stvara mali simulirani primjer. Tablica nije nalaz o stvarnoj
populaciji. Ona pokazuje postupak kojim se odgovori pretvaraju u mjeru i čuva
pojedinačne stavke uz izvedeni rezultat.

*Slika. Simulirani odgovori i izvedena mjera povjerenja. Izrada autora.*

Prosjek stavki sažima odgovore, ali ne dokazuje valjanost instrumenta.
Istraživač još mora obrazložiti sadržaj tvrdnji, provjeriti kako ih ispitanici
razumiju i opisati tko je mogao ući u uzorak. Analiza počinje tek kada su te
odluke vidljive.

## Sažetak

Mjerenje prevodi teorijske pojave u opažanja, a istraživački dizajn određuje
dokle zaključak smije dosegnuti. Pouzdanost, valjanost i razina mjerenja nisu
tehnički dodatci nakon prikupljanja podataka, nego svojstva odluka donesenih
prije njega. Eksperiment i opažačka studija odgovaraju na različito snažna
pitanja, osobito kada je riječ o uzrocima. Sljedeće poglavlje okreće taj pogled
prema tvrdnjama koje skrivaju upravo te odluke.

## Pojmovi

operacionalizacija (*operationalization*), razina mjerenja (*level of
measurement*), pouzdanost (*reliability*), valjanost (*validity*),
konfundirajuća varijabla (*confounder*), okvir uzorkovanja (*sampling frame*)

## Zadaci

### Konceptualni

Razlikujte pouzdanu mjeru od valjane mjere na vlastitom primjeru. Predajte
objašnjenje u kojem ista mjera može biti pouzdana, ali nevaljana.

### Računski

Upotrijebite simulirane podatke `sim_mjerenje`. Izračunajte izvedenu mjeru
nakon izostavljanja svake pojedine tvrdnje i predajte tablicu usporedbe.

### Kritički

Prosudite što se iz Berkeleyjskih podataka može zaključiti o ishodima, a što
ne može o postupku odlučivanja (Bickel, 1975). Predajte dva stupca s dopuštenim i
nedopuštenim zaključcima.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte dizajn, prepoznajte jednu
neopravdanu tvrdnju i napišite inačicu koja poštuje ograničenja dizajna.
