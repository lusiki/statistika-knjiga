# DIO I: STATISTIČKO MIŠLJENJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Zašto statistika

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/01-zasto-statistika.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 8 min | Simpsonov paradoks | UCBAdmissions | bez preduvjeta |

**Vinjeta.**
Podaci o upisima na Sveučilište Kalifornije u Berkeleyju 1973. godine otvorili
su ozbiljno pitanje. Jesu li njegovi poslijediplomski programi pri upisu
diskriminirali žene (Bickel, 1975)? Zbirni podaci upućivali su upravo na to.
Među prijavama u šest najvećih odjela stopa prijma iznosila je
`r paste0(hr_broj(100 * stopa_muskarci, 1), " %")` za muškarce i
`r paste0(hr_broj(100 * stopa_zene, 1), " %")` za žene (Bickel, 1975).

Istraživački tim zatim je iste prijave razdvojio prema odjelu. Slika se
promijenila. U `r odjeli_prednost_zene` od šest odjela stopa prijma za žene
bila je barem jednaka stopi za muškarce, dok su se žene češće prijavljivale na
odjele na kojima je prijam bio teži za sve kandidate (Bickel, 1975). Zbirni jaz
nije nestao iz tablice, ali njegovo se značenje više nije moglo čitati na isti
način.

Oba su prikaza nastala iz istih prijava i oba su računski točna. Jedan sugerira
veliku razliku, a drugi pokazuje da sastav prijava tu razliku snažno oblikuje.
Kojoj slici treba vjerovati kada ispravan izračun vodi prema pogrešnom
zaključku?

## Broj nije zaključak

Berkeleyjski slučaj ne pokazuje da su podaci nepouzdani. Pokazuje nešto
zahtjevnije. Podaci ne donose zaključak bez pitanja koje im postavljamo i bez
usporedbe kojom na to pitanje odgovaramo. Zbirna stopa odgovara na pitanje tko
je češće primljen u promatranoj skupini prijava. Stope po odjelima odgovaraju na
pitanje kako su prolazili kandidati koji su se prijavili na isti odjel. Ta su
pitanja povezana, ali nisu ista.

**Statistika** počinje upravo na mjestu na kojem prestaje jednostavno
prebrojavanje. Njezina zadaća nije proizvesti broj, nego odrediti što taj broj
može poduprijeti. Pritom mora sačuvati vezu između pitanja, načina mjerenja,
usporedbe i zaključka. Izračun može biti besprijekoran, a tvrdnja izgrađena na
njemu ipak pogrešna jer broj odgovara na drugo pitanje od onoga koje nas
zanima.

Zbog toga podatke nije korisno zamišljati kao suprotnost ljudskom iskustvu.
Anegdota može otkriti problem, predložiti mehanizam ili pokazati posljedicu
koju tablica skriva. Ne može nam sama reći koliko je pojava raširena ni što bi
se dogodilo u drugim okolnostima. Podaci proširuju pogled preko pojedinačnog
slučaja, ali zauzvrat traže odluke o tome koga smo promatrali, što smo mjerili i
s čime rezultat uspoređujemo.

Broj zato ne govori sam za sebe. Govori unutar postupka koji možemo pregledati,
ponoviti i osporiti. Strogost statističkog pristupa ne sastoji se u tome da
svakom dojmu suprotstavimo izračun. Sastoji se u tome da učinimo vidljivima
korake između opažanja i tvrdnje.

## Signal u promjenjivom svijetu

Društvene pojave rijetko se ponavljaju na potpuno isti način. Dvije osobe
izložene istoj poruci ne moraju joj jednako vjerovati. Ista anketa provedena na
drugom uzorku neće vratiti potpuno jednake postotke. Čak se i ponašanje iste
osobe mijenja s vremenom i okolnostima. Ta promjenjivost nije kvar podataka.
Ona je razlog zbog kojeg nam statistika treba.

U takvoj promjenjivosti pokušavamo razlučiti **signal** od **šuma**. Signal je
obrazac koji nas zanima, poput razlike među skupinama ili povezanosti dviju
pojava. Šum obuhvaća ostale izvore varijacije zbog kojih opažanja ne pristaju
savršeno uz obrazac. Granica među njima nije zadana unaprijed. Ono što je šum
za jedno pitanje može postati signal za drugo.

Ako proučavamo razlikuje li se povjerenje u institucije među dobnim skupinama,
pojedinačne razlike unutar svake skupine otežavaju nam da vidimo opći obrazac.
Ako zatim pitamo zašto se ljudi iste dobi razlikuju, upravo te pojedinačne
razlike postaju predmet istraživanja. Statističko mišljenje zato ne uklanja
varijabilnost. Ono je raspoređuje prema pitanju koje pokušavamo razjasniti.

Usporedba je pritom važnija od samog velikog ili malog broja. Pad, rast ili
razlika dobivaju značenje tek kada znamo prema čemu ih mjerimo. Ponekad je
usporedba druga skupina, ponekad ranije razdoblje, a ponekad raspon rezultata
koji bi mogli nastati običnom promjenjivošću. Kasnija poglavlja izgradit će
računske postupke za te usporedbe. Za sada je važan njihov zajednički temelj.
Tvrdnja postaje statistička tek kada jasno kaže što se s čim uspoređuje.

## Zbirna slika i skrivena struktura

Zbirni rezultat često izgleda kao najpotpuniji prikaz jer obuhvaća sva
opažanja. Ipak, ukupni prosjek ili stopa uvijek su mješavina rezultata
podskupina i zastupljenosti tih podskupina. Skupina koja je brojnija snažnije
povlači ukupni rezultat prema sebi. Promjena sastava stoga može promijeniti
zbirnu stopu čak i kada se ništa nije promijenilo unutar pojedinih podskupina.

U Berkeleyju su se odjeli znatno razlikovali po težini upisa, a prijave
muškaraca i žena nisu bile jednako raspoređene među njima. Žene su se češće
prijavljivale na selektivnije odjele, pa je njihova zbirna stopa snažnije
odražavala upravo te odjele. Usporedba unutar odjela uklonila je taj učinak
sastava iz neposredne usporedbe, zbog čega se obrazac vidljiv u ukupnim
podacima oslabio ili preokrenuo (Bickel, 1975).

Takav se obrat naziva **Simpsonov paradoks**. Riječ je o obrascu u kojem se
povezanost vidljiva u združenim podacima promijeni ili preokrene kada podatke
razdvojimo prema relevantnoj trećoj varijabli (Simpson, 1951). Paradoks nije u
aritmetici. Svaka stopa ostaje točna. Neobičnost nastaje zato što iste brojke
opisuju različite usporedbe, a naš se zaključak promijeni kada to napokon
primijetimo.

Razdvajanje podataka ipak nije čarobni postupak koji uvijek otkriva konačnu
istinu. Podskupine moraju imati sadržajno opravdanje. Ako podatke dijelimo na
dovoljno mnogo proizvoljnih načina, prije ili poslije pronaći ćemo privlačan
obrazac koji nema stabilno značenje. Statistička disciplina traži da objasnimo
zašto je određena podjela važna prije nego što njezin rezultat proglasimo
odgovorom.

Simpsonov paradoks zato nije tek neobičan trik s tablicama. On sažima razlog
postojanja statistike. Promatrani broj moramo povezati sa strukturom podataka
koja ga je proizvela, a zaključak ograničiti na usporedbu koju smo doista
napravili.

## Interakcija — Simpsonov paradoks

Interaktivni prikaz gradi transparentan primjer s dvjema skupinama i dvjema
podskupinama. Stope unutar podskupina ostaju jednake, dok klizači mijenjaju
njihovu zastupljenost u svakoj skupini. Prebacivanje pogleda pokazuje kako
različiti utezi mogu proizvesti zbirni rezultat suprotan obrascu unutar obje
podskupine.

*Slika. Zbirne stope i stope po podskupinama u konstruiranom primjeru Simpsonova paradoksa.*

**Što isprobati.**

1. Najprije usporedite samo zbirne stope i zapišite koja skupina izgleda
   uspješnije.
2. Uključite prikaz podskupina i provjerite ostaje li smjer razlike jednak.
3. Promijenite zastupljenost podskupina bez mijenjanja njihovih stopa i
   promatrajte kada se zbirni zaključak preokrene.

**Statistika u divljini.**
**Privid pristranosti u zbirnoj stopi.** Tvrdnja da su muškarci u Berkeleyju
1973. primani češće od žena aritmetički je točna za šest najvećih odjela
(Bickel, 1975). Problem nastaje tek kada tu zbirnu razliku pretvorimo u
objašnjenje postupka upisa. Ukupna stopa istodobno spaja odluke različitih
odjela i različitu raspodjelu prijava među njima.

Odgovorno čitanje zato ne odbacuje zbirnu stopu, ali od nje traži pomoćne
informacije. Potrebni su brojevi prijava i primljenih kandidata unutar svakog
odjela te objašnjenje zbog čega je odjel relevantna podjela. Tek tada vidimo
koji dio razlike nastaje unutar usporedivih skupina, a koji zbog njihova
različitog sastava.

**Pitajte model.**
Asistent može brzo izračunati zbirne stope i ponoviti izračun po podskupinama,
ali mu treba dati stvarne brojnike i nazivnike. Nakon odgovora valja provjeriti
daju li zbrojevi ćelija objavljene ukupne vrijednosti i je li svaka stopa
izračunata s odgovarajućim nazivnikom. Modeli osobito lako nadopune ćeliju
koja nedostaje ili svaku razliku između zbirnog i grupiranog prikaza proglase
Simpsonovim paradoksom.

> Usporedi zbirne stope prijma sa stopama po odjelima. Prikaži broj prijava,
> broj primljenih i nazivnik svake stope. Opiši kako sastav prijava mijenja
> zbirni rezultat, ali nemoj iz tih tablica izvoditi kauzalni zaključak.

**Nađite grešku.**
Zbirna stopa prijma bila je viša za muškarce, dok je u četiri od šest odjela
stopa za žene bila barem jednaka stopi za muškarce (Bickel, 1975). Žene su se
češće prijavljivale na selektivnije odjele (Bickel, 1975). Stoga je izbor
odjela uzrokovao cijeli zbirni jaz.

Greška je kauzalni zaključak u posljednjoj rečenici. Tablica pokazuje da
raspodjela prijava po odjelima objašnjava statističku strukturu zbirnog jaza,
ali sama ne dokazuje zašto su kandidati birali određene odjele niti da je time
objašnjen svaki mogući oblik pristranosti.

## Razrađeni primjer

Berkeleyjski podaci omogućuju da cijeli problem pratimo bez složenog modela.
Svaki redak izvorne tablice govori o ishodu prijave, spolu kandidata i odjelu.
Prvi korak združuje odjele te za svaku skupinu dijeli broj primljenih s ukupnim
brojem prijava.

*Slika. Zbirne stope prijma u šest najvećih odjela. Izrada autora prema @bickel1975.*

Zbirna tablica pokazuje velik jaz. Primljeno je
`r paste0(hr_broj(100 * stopa_muskarci, 1), " %")` muškaraca i
`r paste0(hr_broj(100 * stopa_zene, 1), " %")` žena među prijavama obuhvaćenim
ovim podacima (Bickel, 1975). Kada bismo ovdje stali, bilo bi razumljivo
posumnjati da je ista razlika prisutna u odlukama svakog odjela. Ta pretpostavka
ipak nije sadržana u zbirnoj stopi.

Sljedeći korak ne mijenja nijednu prijavu. Mijenja samo razinu na kojoj ih
uspoređujemo. Stope sada računamo zasebno u svakom odjelu, čime kandidati iz
selektivnog odjela više ne utječu izravno na usporedbu kandidata u odjelu s
višom prolaznošću.

Stope prijma prema odjelu i spolu. Izrada autora prema bickel1975.

Stope po odjelima više ne podržavaju jednostavnu priču prema kojoj se isti jaz
ponavlja posvuda. U četiri od šest odjela stopa za žene barem je jednaka stopi
za muškarce, dok je u preostala dva niža (Bickel, 1975). Presudan je i raspored
prijava. Velik dio prijava žena završio je u odjelima s niskim stopama prijma,
pa su ti odjeli dobili veću težinu u njihovoj zbirnoj stopi (Bickel, 1975).

Zbirna stopa može se zamisliti kao prosjek odjelnih stopa u kojem odjeli nemaju
jednaku težinu. Njihova težina ovisi o broju prijava iz svake skupine. Zato dvije
skupine mogu imati sličan ili obrnut odnos unutar odjela, a ipak vrlo različite
ukupne stope. Obrat ne proizvodi pogrešan račun. Proizvode ga različiti utezi u
dvama zbirnim prosjecima.

Ova analiza još ne daje konačan sud o pravednosti upisa. Odjelne tablice ne
govore zašto su prijave raspoređene upravo tako, kako su kandidati usmjeravani
ni jesu li kriteriji unutar odjela bili primijenjeni jednako. One postižu nešto
uže i nužno. Pokazuju da zbirnu razliku ne smijemo tumačiti kao izravnu sliku
odluka unutar svakog odjela. Statistički postupak nije zatvorio pitanje, nego ga
je napokon postavio dovoljno precizno.

## Sažetak

Statistika povezuje podatke s usporedbom koja određenom zaključku daje značenje.
Promjenjivost nije smetnja koju uklanjamo, nego građa iz koje razlučujemo signal
i šum. Simpsonov paradoks pokazuje da točan zbirni rezultat može zavesti kada
skriva sastav podskupina. Strog pristup zato ne završava izračunom, nego
provjerava kako su podaci nastali, što je uspoređeno i dokle zaključak smije
dosegnuti. Sljedeći korak vodi prema mjerenju i istraživačkom dizajnu, gdje se
odlučuje što će uopće postati podatak.

## Pojmovi

statistika (*statistics*), signal (*signal*), šum (*noise*), zbirni podaci
(*aggregate data*), podskupina (*subgroup*), Simpsonov paradoks
(*Simpson's paradox*)

## Zadaci

### Konceptualni

Objasnite kako dvije računski točne stope mogu poduprijeti različite zaključke.
U odgovoru razlikujte zbirnu usporedbu od usporedbe unutar podskupina.

### Računski

Upotrijebite podatke `UCBAdmissions` iz R-a. Izračunajte stopu prijma prema
spolu najprije bez odjela, a zatim zasebno po odjelima. Predajte dvije tablice i
jedan odlomak koji opisuje promjenu obrasca.

### Kritički

Prosudite tvrdnju da zbirni jaz u stopama prijma sam po sebi dokazuje
pristranost svakog odjela u Berkeleyju (Bickel, 1975). Navedite koju dodatnu
usporedbu tvrdnja preskače i što ni ta dodatna usporedba ne može dokazati.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Imenujte točne korake, izdvojite jednu
neopravdanu tvrdnju i napišite njezinu oprezniju zamjenu.

---

# Mjerenje i istraživački dizajn

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/02-mjerenje-i-dizajn.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Prikaz konfundera | simulacija | pogl. 1 |

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

Prikaz pokazuje odnos dviju varijabli prije i nakon razlikovanja jedinica prema
trećoj varijabli. Opažanja ostaju ista, ali se mijenja usporedba. Pomak ishoda
povezan s trećom varijablom može zbirnu vezu preokrenuti iako je odnos unutar
obiju podskupina stabilan.

*Slika. Ista opažanja prikazana zbirno i prema trećoj varijabli u konstruiranom primjeru.*

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

---

# Kako brojke zavode

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 4 min | Istraživač margine pogreške | simulacija | pogl. 1 i 2 |

**Vinjeta.**
Američko statističko udruženje objavilo je izjavu o p-vrijednostima nakon
desetljeća u kojima se jedan prag često koristio kao zamjena za znanstveni sud
(Wasserstein, 2016). Problem nije bio u tome što su istraživači zaboravili
računati. Problem je nastajao kada je jedan broj preuzimao značenje koje mu
postupak nije davao.

Sličan prijenos značenja događa se u naslovima anketa, postocima bez nazivnika
i grafovima kojima odabrani raspon osi pretvara malu promjenu u dramatičan lom.
Broj može biti točan, a prikaz ipak voditi prema zaključku koji podaci ne nose.

Kako razlikovati računsku pogrešku od mnogo češće pogreške u okviru, usporedbi
i jeziku?

## Četiri provjere jedne tvrdnje

Prva provjera traži izvor. Tvrdnja koja navodi istraživanje mora omogućiti
pronalaženje izvornog izvještaja, tablice ili skupa podataka. Poveznica na
drugi članak nije podrijetlo brojke, a navođenje ustanove bez godine i
istraživanja nije dovoljno da bi se nalaz provjerio.

Druga provjera traži nazivnik. Porast od pedeset posto može značiti prijelaz s
dva slučaja na tri ili s dva milijuna na tri milijuna. Postotak opisuje omjer,
dok **postotni bod** opisuje razliku između dvaju postotaka. Njihova zamjena
može višestruko povećati dojam promjene iako je aritmetika pojedinačnih brojeva
točna.

Treća provjera traži usporedbu. Graf bez zajedničke nule nije automatski
nepošten, ali skraćena os mora biti vidljiva i opravdana. Odabir početnog
razdoblja, izostavljanje jedne skupine ili isticanje samo povoljnog ishoda
mijenja priču. Čitatelj zato pita koje bi razumno drugačije uokvirivanje
pokazalo isti podatak.

Četvrta provjera traži neizvjesnost. Rezultat ankete nije svojstvo uzorka koje
će se bez promjene ponoviti u populaciji. Margina pogreške opisuje samo
uzoračku promjenjivost pod određenim pretpostavkama. Ne obuhvaća pristran
okvir, neodaziv, loše pitanje ni naknadno biranje najzanimljivijeg rezultata.

## Protokol skeptičnog čitanja

Skeptičnost nije automatsko odbacivanje. Ona usporava prijelaz od podatka prema
tvrdnji. Najprije utvrđujemo tko je proizveo broj i za koju svrhu. Zatim
provjeravamo jedinicu analize, nazivnik, vremenski okvir i usporednu skupinu.
Tek tada procjenjujemo koliko neizvjesnost i dizajn dopuštaju zaključak.

Isti protokol vrijedi za ljudski i strojno proizveden tekst. Asistent može
izmisliti izvor, popuniti ćeliju koja nedostaje ili zaokružiti rezultat do
lažne preciznosti. Uvjerljiv stil nije dokaz podrijetla. Svaka brojka mora
ostaviti trag do podataka ili postupka iz kojeg je nastala.

## Interakcija — Istraživač margine pogreške

Istraživač prikazuje približnu marginu pogreške uzorka pri različitim
veličinama i procijenjenim udjelima. Zaseban klizač uvodi poznatu sustavnu
pristranost. Interval se tada može sužavati oko precizno procijenjene pogrešne
vrijednosti.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

**Statistika u divljini.**
**Prag koji nije presuda.** Izjava Američkog statističkog udruženja naglasila
je da p-vrijednost sama ne mjeri veličinu ni važnost učinka i ne određuje treba
li rezultat smatrati znanstveno vrijednim (Wasserstein, 2016).

Naslov koji istraživanje svodi na „dokazano" ili „nije dokazano" uklanja
procjenu, neizvjesnost i dizajn. Broj ostaje vidljiv, a upravo informacije
potrebne za njegovo tumačenje nestaju.

**Pitajte model.**
Asistent je koristan kao strogi čitatelj ako dobije izvornu tablicu i jasnu
zabranu nadopunjavanja nedostajućih podataka. Treba tražiti da odvoji provjeru
aritmetike od procjene dizajna i jezika. Nakon odgovora ručno se otvara svaki
navedeni izvor i provjerava postoji li broj u njemu.

> Rastavi ovu statističku tvrdnju na izvor, brojnik, nazivnik, usporedbu,
> neizvjesnost i dopušten zaključak. Ne dopunjuj podatke koji nisu priloženi i
> jasno označi što nije moguće provjeriti.

**Nađite grešku.**
Anketa pokazuje vodstvo jedne opcije, ali se intervali procjena dviju opcija
preklapaju. Zbog preklapanja možemo zaključiti da među njima sigurno nema
razlike. Uzorak je opisan, a postoci se zbrajaju do cjeline.

Greška je zaključak da preklapanje intervala dokazuje nepostojanje razlike.
Odnos dviju procjena mora se procijeniti izravno, uz dizajn ankete i ovisnost
procjena, a ne samo pogledom na dva odvojena intervala.

## Razrađeni primjer

Simuliramo dvije ankete o istoj podršci, jednu s manjim i jednu s većim
uzorkom. Obje su pošteno uzorkovane iz iste zamišljene populacije. Cilj nije
dobiti stvarni izborni rezultat, nego vidjeti što se mijenja kada povećamo broj
opažanja.

*Slika. Simulirane procjene pri dvjema veličinama uzorka. Izrada autora.*

Veći uzorak daje užu marginu, ali obje ankete dijele pretpostavku da je
uzorkovanje nepristrano. Kada bi okvir isključio dio populacije, tablica bi i
dalje mogla pokazivati veliku računsku preciznost. Strog prikaz zato uz marginu
navodi način odabira ispitanika, datum, formulaciju pitanja i naručitelja.

## Sažetak

Brojke zavode kada izgube izvor, nazivnik, usporedbu ili neizvjesnost. Pogreška
ne mora biti u računu jer često nastaje u izboru prikaza i jezika kojim se
rezultat pretvara u tvrdnju. Skeptični protokol jednak je za novinski naslov,
znanstveni sažetak i odgovor modela. U sljedećem dijelu knjige isti se zahtjev
primjenjuje na sažimanje i vizualizaciju vlastitih podataka.

## Pojmovi

nazivnik (*denominator*), postotni bod (*percentage point*), margina pogreške
(*margin of error*), pristranost (*bias*), lažna preciznost (*false
precision*), podrijetlo podatka (*data provenance*)

## Zadaci

### Konceptualni

Objasnite razliku između pedesetpostotnog rasta i rasta od pedeset postotnih
bodova. Predajte vlastiti primjer bez stvarnih empirijskih tvrdnji.

### Računski

Upotrijebite simulirane podatke `sim_ankete`. Dodajte treću veličinu uzorka i
predajte tablicu s pripadajućom marginom pogreške.

### Kritički

Pročitajte izjavu o p-vrijednostima i izdvojite jednu tvrdnju koju ona
dopušta te jednu koju izričito ne dopušta (Wasserstein, 2016). Predajte dvije
rečenice i citat izvora.

### Revizija modela

Ocijenite analizu modela iz okvira iznad. Odvojite točne provjere od jedne
pogrešne interpretacije i napišite provjerljiviju zamjenu.
