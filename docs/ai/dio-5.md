# DIO V: MODELI

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Kategorički podaci

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Očekivano i opaženo | simulirana populacija | pogl. 4, 8, 10 |

**Vinjeta.**
Sveučilište u Berkeleyju našlo se sredinom sedamdesetih pred pitanjem na koje
je moralo odgovoriti brojkama. Zbirna tablica prijava za poslijediplomski
studij pokazivala je da je udio primljenih muškaraca osjetno veći od udjela
primljenih žena, a takva se tablica čita brzo i zaključuje još brže
(Bickel, 1975).

Ono što je tablica sadržavala bile su samo frekvencije. Četiri broja u dvije
kategorije, bez ijedne informacije o tome kako je do njih došlo. Pitanje pred
istraživačima nije bilo je li razlika velika, nego što bi se u tim ćelijama
uopće trebalo nalaziti da spol i ishod prijave nemaju nikakve veze.

Kako iz same tablice brojanja prepoznati postoji li veza, gdje se ona nalazi i
koliko je snažna?

## Brojanje prije testiranja

Kategoričke varijable ne mjere količinu nego pripadnost. Dobna skupina, izvor
vijesti, obrazovanje i regija razvrstavaju ljude u kutije, a jedino što se s
kutijama može učiniti jest prebrojati ih. Sve što slijedi u ovom poglavlju
izvedeno je iz tih brojeva, pa je vrijedno zadržati se na tome koliko se lako
prebrojavanje pokvari.

Frekvencija govori koliko je jedinica u nekoj kategoriji. Udio istu tu
frekvenciju stavlja u odnos prema nazivniku, i tek s nazivnikom postaje čitljiv.
Rečenica da četrdeset posto ispitanika bira društvene mreže znači nešto sasvim
drugo ako je nazivnik cijeli uzorak, ako je to samo najmlađa dobna skupina ili
ako su to samo oni koji su na pitanje uopće odgovorili. Nazivnik se u
izvještajima izostavlja češće nego bilo koji drugi element, a bez njega se udio
ne može provjeriti.

Prije nego što se bilo što prebroji, netko je odlučio koje kutije postoje.
Dobne skupine mogle su biti podijeljene na drugim granicama, izvori vijesti
razvrstani u tri kategorije umjesto u pet, a portal i društvena mreža smješteni
zajedno ili razdvojeno. Ta odluka pripada operacionalizaciji iz poglavlja o
mjerenju i dizajnu, i donesena je prije podataka. Svaki rezultat u ovom
poglavlju vrijedi uz nju, jer test uspoređuje raspored unutar zadanih
kategorija i ne može propitati kategorije same.

**Kontingencijska tablica** je tablica frekvencija u kojoj svaka ćelija sadrži
broj jedinica koje istovremeno pripadaju jednoj kategoriji retka i jednoj
kategoriji stupca.

Za dvije kategoričke varijable takva tablica sadrži cijelu zajedničku
raspodjelu. Rubni zbrojevi po retcima daju raspodjelu prve varijable, rubni
zbrojevi po stupcima raspodjelu druge, a ćelije govore kako se te dvije
raspodjele preklapaju. Poglavlje radi na simuliranoj populaciji iz koje je
izvučeno `r s13_n` osoba, i sve brojke u njemu potječu iz tog uzorka.

Postoci po retku i postoci po stupcu odgovaraju na različita pitanja i nisu
zamjenjivi. Postotak po retku pita kako se unutar jedne dobne skupine dijele
izvori vijesti. Postotak po stupcu pita kako je unutar jednog izvora
raspoređena dob. Prvi je ovdje pravi jer skupine nisu jednako brojne, pa
apsolutne frekvencije ne bi bile usporedive.

*Slika. Udio pojedinog izvora vijesti unutar svake dobne skupine u simuliranom uzorku od osamsto osoba.*

Obrazac je postupan i ide u jednom smjeru. Među osobama od 18 do 29 godina
društvene mreže bira `r hr_broj(s13_retci["18 do 29", "društvene mreže"])` %
ispitanika, a među osobama od 60 i više godina
`r hr_broj(s13_retci["60 i više", "društvene mreže"])` %. Televizija ide
suprotno, s `r hr_broj(s13_retci["18 do 29", "TV"])` % u najmlađoj i
`r hr_broj(s13_retci["60 i više", "TV"])` % u najstarijoj skupini. Graf je
uvjerljiv, ali uvjerljivost nije dokaz, jer bi i uzorak izvučen iz populacije
bez ikakve veze proizveo neki obrazac.

## Očekivano pod nezavisnošću

Da bismo znali je li opaženi raspored neobičan, treba nam raspored s kojim ga
uspoređujemo. Taj se raspored ne pogađa nego izvodi iz same tablice, i to iz
onog njezina dijela koji nije sporan. Rubni zbrojevi kažu koliko je ljudi u
svakoj dobnoj skupini i koliko ih ukupno bira svaki izvor. Ta dva popisa
uzimamo kao zadana i pitamo se kako bi izgledale ćelije kad pripadnost dobnoj
skupini ne bi mijenjala ništa u izboru izvora.

Odgovor je jednostavan koliko i sama pretpostavka. Ako televiziju bira petina
cijelog uzorka, i ako dob nema nikakve veze s izborom, onda bi televiziju
trebala birati petina svake dobne skupine. Očekivani broj za jednu ćeliju zato
je udio njezina stupca primijenjen na veličinu njezina retka.

**Očekivana frekvencija** ćelije je umnožak zbroja njezina retka i zbroja
njezina stupca podijeljen ukupnim brojem jedinica, dakle broj koji bi se u toj
ćeliji nalazio kad bi dvije varijable bile nezavisne uz nepromijenjene rubne
zbrojeve.

$$E_{ij} = \frac{n_{i\cdot} \times n_{\cdot j}}{n}$$

Oznaka $n_{i\cdot}$ stoji za zbroj i-tog retka, $n_{\cdot j}$ za zbroj j-tog
stupca, a $n$ za ukupan broj jedinica u tablici.

Nezavisnost ovdje ima uzak i provjerljiv smisao. Znati nečiju dobnu skupinu ne
pomaže u pogađanju njezina izvora vijesti. Model nezavisnosti nije tvrdnja o
svijetu nego račun koji svijet privremeno pretpostavlja takvim, kako bi se
izmjerilo koliko podaci od njega odstupaju.

Najmanja očekivana frekvencija u našoj tablici iznosi
`r hr_broj(s13$min_ocekivana)`, što je važno zapamtiti za kasniji odjeljak o
granicama postupka. Za sada je dovoljno da nijedna ćelija nije toliko rijetka
da bi račun postao nepouzdan.

## Interakcija — Očekivano i opaženo

Sljedeći prikaz zadržava rubne zbrojeve nepromijenjenima i dopušta pomicanje
opaženih frekvencija oko očekivanih. Vidljivo postaje ono što tablica brojeva
skriva, a to je da svaka ćelija ima vlastiti doprinos ukupnom odstupanju i da
taj doprinos ne raste jednako brzo za velike i za male ćelije. Puni krug
označuje opaženu frekvenciju, prazni romb očekivanu, a broj uz njih doprinos
te ćelije.

*Slika. Opažene i očekivane frekvencije u tablici dva puta dva s jednakim rubnim zbrojevima.*

**Što isprobati.**

1. Postavite opažene frekvencije jednake očekivanima i pogledajte doprinose.
2. Pomaknite opažanja u oba smjera i provjerite ostaju li rubni zbrojevi jednaki.
3. Povećajte pomak i pratite koliko brže raste ukupno odstupanje od pomaka.
4. Zadržite pomak u postocima, a smanjite rubni zbroj na deset.

Posljednji korak pokazuje ono što se u tablici brojeva ne vidi. Isti relativni
pomak u maloj ćeliji daje mnogo manji doprinos nego u velikoj, jer se svako
odstupanje dijeli očekivanom frekvencijom. Postupak zato ne mjeri koliko je
razlika velika u postocima nego koliko je malo vjerojatna uz zadane rubne
zbrojeve.

## Zbroj odstupanja i njegov raspored

Ono što je widget prikazivao po ćelijama sada dobiva ime. Za svaku ćeliju
uzimamo razliku opažene i očekivane frekvencije, kvadriramo je da se odstupanja
u dva smjera ne ponište, i dijelimo očekivanom frekvencijom da veliki i mali
brojevi budu usporedivi. Zbroj svih tih doprinosa jedna je brojka koja opisuje
cijelu tablicu.

**Hi-kvadrat statistika** je zbroj kvadriranih odstupanja opaženih od očekivanih
frekvencija, pri čemu je svako odstupanje podijeljeno očekivanom frekvencijom
svoje ćelije.

$$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

Oznaka $O_{ij}$ stoji za opaženu, a $E_{ij}$ za očekivanu frekvenciju ćelije u
i-tom retku i j-tom stupcu.

Za našu tablicu ta statistika iznosi `r hr_broj(s13$hi)` uz
`r s13$df` stupnjeva slobode, gdje se stupnjevi slobode računaju kao umnožak
broja redaka umanjenog za jedan i broja stupaca umanjenog za jedan.

Taj se umnožak lako pamti, ali ga vrijedi i razumjeti, jer stoji iza svakog
kasnijeg testa u knjizi. Rubni zbrojevi su fiksirani, pa se ćelije ne mogu
puniti neovisno jedna o drugoj. U tablici s dva retka i dva stupca dovoljno je
odabrati jednu ćeliju, a preostale tri su njome određene. U našoj tablici s
četiri retka i pet stupaca slobodno je `r s13$df` ćelija, a ostalih osam
slijedi iz njih i iz rubova. Stupnjevi slobode zato broje koliko je tablica
zaista mogla biti drugačija, i upravo o tome ovisi koliko je veliko odstupanje
potrebno da bi bilo neobično.

Sama veličina te brojke ne govori mnogo dok se ne usporedi s onim što bi
odstupanje bilo kad veze ne bi bilo. Tu usporedbu obavlja hi-kvadrat raspodjela,
i ona vraća p-vrijednost na uobičajen način. Prag koji dijeli obično od
neobičnog uz jedan stupanj slobode iznosi `r hr_broj(s13$granica, 2)`, a raste
sa svakim dodatnim stupnjem.

Ukupna brojka ima jedno ozbiljno ograničenje. Ona kaže da tablica nije
usklađena s nezavisnošću, ali ne kaže koje su ćelije za to odgovorne. Povratak
na ćelije obavlja se dijeljenjem svakog odstupanja korijenom njegove očekivane
frekvencije.

**Standardizirani rezidual** ćelije je razlika opažene i očekivane frekvencije
podijeljena korijenom očekivane frekvencije, pa se očitava na ljestvici sličnoj
standardiziranim vrijednostima.

$$e_{ij} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}$$

Oznaka $e$ ovdje stoji za ostatak, a ne za korelaciju, koju knjiga bilježi
slovom $r$ i koja s ovim računom nema veze.

Pozitivan rezidual znači da je u ćeliji više opažanja nego što bi ih bilo bez
veze, a negativan da ih je manje. Vrijednosti izvan raspona od minus dva do plus
dva uobičajeno se čitaju kao ćelije koje nose odstupanje, uz istu opreznost s
kojom se čita svaki prag.

U našoj tablici najveći pozitivni rezidual pripada televiziji u skupini od 60 i
više godina i iznosi `r hr_broj(s13_rez["60 i više", "TV"], 2)`. Najveći
negativni pripada društvenim mrežama u istoj skupini i iznosi
`r hr_broj(s13_rez["60 i više", "društvene mreže"], 2)`. U najmlađoj skupini
predznaci su obrnuti, s
`r hr_broj(s13_rez["18 do 29", "društvene mreže"], 2)` za društvene mreže i
`r hr_broj(s13_rez["18 do 29", "TV"], 2)` za televiziju. Reziduali time
pretvaraju jednu brojku o cijeloj tablici u tvrdnju o tome tko točno odstupa i
u kojem smjeru, što je oblik nalaza koji se uopće može upotrijebiti.

## Značajno nije isto što i snažno

Hi-kvadrat statistika raste s veličinom uzorka. Ista tablica postotaka izmjerena
na osam tisuća ljudi umjesto na osamsto dat će deset puta veću statistiku i
p-vrijednost koja se više ne može ispisati. Iz toga slijedi da p-vrijednost ne
može biti mjera jačine veze, jer se mijenja i kad se veza uopće ne mijenja.

Mjera jačine mora zato dijeliti statistiku veličinom uzorka i oblikom tablice.
Cramérovo V upravo to čini i vraća broj između nule i jedinice, gdje nula znači
potpunu nezavisnost, a jedinica da jedna varijabla u potpunosti određuje drugu.

**Cramérovo V** je korijen hi-kvadrat statistike podijeljene umnoškom veličine
uzorka i manje dimenzije tablice umanjene za jedan.

$$V = \sqrt{\frac{\chi^2}{n\,(k-1)}}$$

Oznaka $n$ stoji za ukupan broj jedinica, a $k$ za manji od broja redaka i
broja stupaca.

Za našu tablicu V iznosi `r hr_broj(s13$v, 2)`. Orijentacijske vrijednosti za
takve mjere postoje i najčešće se navode prema Cohenu, ali ih je i sam izvor
ponudio kao pomoć u odsutnosti boljeg oslonca, a ne kao ljestvicu za očitavanje
(Cohen, 1988). Sadržajno značenje broja dolazi iz usporedbe s drugim vezama u
istom području, ne iz tablice pragova.

Korisniji od svakog praga jest prijevod natrag u postotke. Ako televiziju bira
`r hr_broj(s13_retci["18 do 29", "TV"])` % najmlađih i
`r hr_broj(s13_retci["60 i više", "TV"])` % najstarijih ispitanika, onda je to
razlika koju uredništvo može upotrijebiti pri odluci o rasporedu resursa.
Cramérovo V toj odluci ne dodaje ništa što postoci već ne govore, ali čuva
usporedivost među tablicama različitih veličina.

## Referentna raspodjela je istraživačka odluka

Do sada je referentna raspodjela dolazila iz same tablice, jer su je odredili
rubni zbrojevi. Postoji i drugi oblik istog postupka, u kojem se raspodjela
jedne varijable uspoređuje s raspodjelom zadanom izvana. Naziva se testom
prilagodbe i računa se istom formulom, s očekivanim frekvencijama koje dolaze
iz pretpostavljenih udjela umjesto iz umnoška rubova.

Ovdje se otvara pitanje koje se u nastavi lako previdi. Očekivane frekvencije
ovise o tome što smo odabrali za referenciju, pa ista opažena raspodjela može
biti u skladu s jednom pretpostavkom i u snažnom neskladu s drugom. Naš uzorak
to pokazuje na raspodjeli obrazovanja.

Prva pretpostavka jest da su četiri razine obrazovanja jednako zastupljene.
Uz nju statistika iznosi `r hr_broj(s13$gof_ravno)` i nesklad je golem. Druga
pretpostavka koristi stvarne udjele populacije iz koje je uzorak izvučen. Uz nju
statistika pada na `r hr_broj(s13$gof_pop, 2)`, a p-vrijednost iznosi
`r hr_broj(s13$p_gof_pop, 2)`, što znači da uzorak dobro odražava populacijsku
strukturu.

Isti podaci, dva potpuno različita zaključka, i nijedan račun nije pogrešan.
Razlika je u tome što tvrdimo. Prvi test odbacuje pretpostavku koju nitko nije
imao razloga postaviti, a drugi provjerava tvrdnju koja doista nešto znači.
Budući da je populacija u ovom poglavlju simulirana i time poznata, znamo koja
je referencija istinita, što je luksuz kakav stvarno istraživanje nema. U njemu
izbor referentne raspodjele nosi istraživač, i taj se izbor obrazlaže prije
nego što se test provede.

## Kad je aproksimacija tanka

Hi-kvadrat postupak ne računa točnu vjerojatnost nego se oslanja na to da se
raspodjela njegove statistike dovoljno dobro poklapa s hi-kvadrat krivuljom.
To poklapanje ovisi o tome koliko su ćelije popunjene, i slabi kad su očekivane
frekvencije male. Umjesto da se to primi na vjeru, može se izmjeriti.

Postupak je isti kao u poglavlju o uzorkovanju. Konstruiramo situaciju u kojoj
veze zaista nema, izvučemo mnogo tablica i pogledamo kako se statistika
ponaša. Sve što tada padne ispod praga p-vrijednosti je pogreška, jer po
konstrukciji nema što otkriti.

Kad su očekivane frekvencije velike, poklapanje je dobro. Vrijednost ispod koje
leži devedeset pet posto simuliranih statistika iznosi
`r hr_broj(s13$p95_velike, 2)` i praktički se podudara s teorijskom granicom od
`r hr_broj(s13$granica, 2)`, a udio odbacivanja iznosi
`r hr_broj(s13$stopa_velike)` % umjesto očekivanih pet.

Kad su očekivane frekvencije oko dvije, poklapanja više nema. Ista vrijednost
pada na `r hr_broj(s13$p95_male, 2)` i time ispod granice, pa test odbacuje samo
`r hr_broj(s13$stopa_male)` % puta. U ovoj tablici
iskrivljenje ide prema opreznosti, ne prema prekomjernom otkrivanju. To je
korisno znati jer se pravilo o malim ćelijama često prenosi kao zaštita od
lažnih nalaza, a ovdje je zapravo zaštita od nalaza koji se neće pojaviti ni
kad postoji.

Za male tablice postoji postupak koji aproksimaciju uopće ne koristi. Fisherov
egzaktni test prebroji sve rasporede koji su mogući uz zadane rubne zbrojeve i
izračuna koliko je njih barem toliko neuravnoteženo kao opaženi. Njegovo ime ne
znači da je svaki drugi test netočan, nego da p-vrijednost dolazi iz
prebrojavanja umjesto iz krivulje.

Treći put je preraspodjela samih kategorija. Više rijetkih kategorija često nosi
manje informacije od dvije popunjene, pa spajanje istovremeno rješava problem
malih ćelija i izoštrava priču. Uvjet je da spajanje ima sadržajno opravdanje i
da je odlučeno prije nego što se vidi rezultat. Kategorije se ne spajaju zato da
bi nesklad postao veći ili da bi nezgodna skupina nestala.

**Statistika u divljini.**
**Prag pet.** Pravilo da svaka očekivana frekvencija mora biti barem pet
ponavlja se u udžbenicima, u recenzijama i u izlazu statističkih programa kao da
je riječ o matematičkom uvjetu. Nije. Potječe iz rada koji je pregledao kako se
hi-kvadrat postupak ponaša u nezgodnim tablicama i ponudio niz praktičnih
preporuka za njihovo ojačavanje (Cochran, 1954).

Razlika između uvjeta i preporuke nije sitničava. Uvjet se provjerava i time je
posao gotov, a preporuka traži da se zna od čega štiti. Simulacija u ovom
odjeljku pokazuje da iskrivljenje ispod praga ovdje ide prema opreznosti, pa
tablica koja prag ne zadovoljava nije automatski tablica s napuhanim nalazom.
Analitičar koji je prag provjerio i stao nije doznao ništa o svojim podacima
osim da zadovoljavaju konvenciju.

**Pitajte model.**
Asistent lako izradi kontingencijsku tablicu, očekivane frekvencije i reziduale,
i pritom obično točno pogodi funkcije. Provjeravamo tri stvari koje ne pogađa
pouzdano. Prva je nazivnik, jer postoci po retku i po stupcu odgovaraju na
različita pitanja, a model bira onaj koji mu je sintaktički bliži. Druga je
veličina očekivanih ćelija, koju često preskoči. Treća je jezik zaključka, jer
značajnu vezu redovito opisuje kao snažnu i prelazi na uzročnu formulaciju bez
ijednog upozorenja.

> Izradi kontingencijsku tablicu dobne skupine i izvora vijesti, prikaži
> postotke po retku i imenuj nazivnik, ispiši očekivane frekvencije i najmanju
> među njima, a uz test navedi Cramérovo V i standardizirane reziduale.

**Nađite grešku.**
Analiza je provjerila očekivane frekvencije i sve su iznad pet. Hi-kvadrat test
daje vrlo malu p-vrijednost, a standardizirani reziduali pokazuju da najviše
odstupaju televizija u najstarijoj skupini i društvene mreže u najmlađoj.
Budući da je rezultat značajan na razini ispod jedan promil, veza između dobi i
izvora vijesti vrlo je snažna.

Greška je zaključak o jačini veze iz veličine p-vrijednosti. Sve prije
posljednje rečenice je točno. P-vrijednost raste s veličinom uzorka i pri
nepromijenjenoj jačini veze, pa se jačina procjenjuje mjerom poput Cramérova V,
koje u ovoj tablici iznosi `r hr_broj(s13$v, 2)`.

## Razrađeni primjer

Pet kategorija izvora vijesti daje tablicu koju je teško čitati i o kojoj je
još teže odlučivati. Sadržajna podjela na digitalne i tradicionalne izvore
zadržava ono što je u podacima nosivo, a uklanja rijetke ćelije. Analiza koja
slijedi tu podjelu provodi, ispisuje profile po dobnim skupinama i testira
tablicu koja iz njih nastaje.

Funkcija `table` prebrojava kombinacije dviju varijabli, `prop.table` pretvara
frekvencije u udjele uz zadani smjer, a `chisq.test` prima gotovu tablicu i
vraća statistiku, stupnjeve slobode i p-vrijednost.

Udio digitalnih izvora pada s
`r hr_broj(s13_digitalni[["18 do 29"]])` % u najmlađoj skupini na
`r hr_broj(s13_digitalni[["60 i više"]])` % u najstarijoj. Statistika iznosi
`r hr_broj(s13$hi_spojena)` uz `r s13$df_spojena` stupnja slobode, a Cramérovo V
raste na `r hr_broj(s13$v_spojena, 2)` s
`r hr_broj(s13$v, 2)` u tablici sa svih pet izvora. Sažimanje je ovdje pojačalo
mjeru jačine, jer je uklonilo razlike među srodnim kategorijama koje su
razrjeđivale glavni obrazac.

Izvještaj s time ipak nije gotov. Tablica opisuje povezanost dobi i izbora
izvora, ali ne kaže zašto ona postoji. Razlika među generacijama može biti
posljedica navike stečene u mladosti, dostupnosti uređaja ili samog položaja u
životnom ciklusu, a ovi podaci među tim objašnjenjima ne biraju. Odvajanje
takvih objašnjenja traži varijable koje tablica ne sadrži i model koji ih može
istovremeno uzeti u obzir, o čemu govori poglavlje o regresiji.

Time se zatvara i pitanje s početka poglavlja. Zbirna tablica prijava u
Berkeleyju doista nije bila usklađena s modelom nezavisnosti, i svaki bi
postupak iz ovog poglavlja to potvrdio (Bickel, 1975). Ono što nijedan od njih
nije mogao dati jest objašnjenje, jer se odgovor nalazio u varijabli koje u
tablici nije bilo. Prijave su bile neravnomjerno raspoređene po odjelima, a
odjeli su se razlikovali po tome koliko su primali. Kako se takav zbirni obrazac
preokrene čim se sloj vrati u račun, pokazuje poglavlje o povezanosti
(Simpson, 1951). Ovdje je dovoljna pouka da tablica s dvije varijable odgovara
točno na jedno pitanje, a da se pitanje o mehanizmu njome ne može ni postaviti.

## Sažetak

Kategorički podaci počinju brojanjem, a brojanje se čita tek uz jasan nazivnik.
Model nezavisnosti čuva rubne zbrojeve i iz njih izvodi očekivane frekvencije,
a hi-kvadrat statistika zbraja odstupanja opaženog od očekivanog. Ukupna brojka
kaže samo da nesklad postoji, pa je reziduali vraćaju u pojedine ćelije, a
Cramérovo V odvaja jačinu veze od veličine uzorka. Test prilagodbe pokazuje da
referentna raspodjela nije tehnički detalj nego istraživačka odluka. Kad su
očekivane frekvencije male, aproksimacija popušta, i tada pomažu Fisherov
postupak ili sadržajno opravdano spajanje kategorija. Sljedeće poglavlje istu
logiku usporedbe prenosi na brojčani ishod i dvije skupine.

## Pojmovi

kontingencijska tablica (*contingency table*), očekivana frekvencija (*expected
frequency*), hi-kvadrat test (*chi-squared test*), test prilagodbe
(*goodness-of-fit test*), standardizirani rezidual (*standardized residual*),
Cramérovo V (*Cramér's V*), Fisherov egzaktni test (*Fisher's exact test*)

## Zadaci

### Konceptualni

Objasnite razliku između testa nezavisnosti i mjere jačine veze tako da
napišete dvije rečenice koje bi se mogle pojaviti u istom izvještaju, jednu o
tome što test kaže i jednu o tome što V kaže.

### Računski

Tablica ima dva retka s po sto ispitanika i dva stupca s rubnim zbrojevima
stodvadeset i osamdeset. Izračunajte sve četiri očekivane frekvencije, a zatim
za opaženu tablicu sa sedamdeset u prvoj ćeliji izračunajte doprinos svake
ćelije i njihov zbroj. Usporedite ga s graničnom vrijednošću 3,84.

### Kritički

Prosudite što zbirna kontingencijska tablica prijava može reći o upisima, a što
gubi kad se odjeli izostave (Bickel, 1975). Predajte jedan odlomak i imenujte
podatak koji bi vam trebao da razlikujete dva ponuđena objašnjenja.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite dijagnostičke korake koji su
provedeni ispravno, imenujte jedan pogrešan zaključak i navedite koju bi
veličinu izvještaj morao sadržavati da se taj zaključak ne može izvesti.

---

# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Uzorkivač dviju grupa | simulirana populacija | pogl. 10, 11, 13 |

**Vinjeta.**
Cumming je urednicima psihologijskih časopisa predložio promjenu koja izgleda
skromno, a mijenja cijeli izvještaj. Umjesto da rad završi oznakom je li
rezultat prešao prag, treba dati procjenu razlike i interval koji uz nju ide
(Cumming, 2014).

Prijedlog nije bio tehnički. Autor koji piše da razlika postoji rekao je manje
nego autor koji piše koliko ona iznosi i koje su vrijednosti s podacima još
uskladive. Prvi izvještaj se ne može ni s čim usporediti, a drugi ulazi u
sljedeće istraživanje kao brojka.

Kako jednu usporedbu dviju sredina povezati s dizajnom iz kojeg je nastala, s
veličinom koju opisuje i s općim jezikom modela?

## Tko nosi dva rezultata

Usporedba dviju sredina izgleda kao jedno pitanje, a zapravo ih je troje.
Razlika je u tome odakle dolaze dva broja koja uspoređujemo, i to pitanje nije
statističko nego pitanje o dizajnu istraživanja.

U prvom slučaju imamo jednu skupinu i vrijednost izvana. Prosječno povjerenje u
našem uzorku uspoređujemo sa službenom vrijednošću iz ranije objavljenog vala
istraživanja ili sa sredinom ljestvice. U drugom slučaju imamo dvije odvojene
skupine sastavljene od različitih ljudi, recimo one koji se prvenstveno
informiraju s televizije i one koji to čine preko društvenih mreža. U trećem
slučaju iste jedinice mjerimo dva puta, prije i poslije nekog događaja, pa svaki
ispitanik nosi oba rezultata.

**Jedinica neovisnosti** je entitet koji se u istraživanju mogao pojaviti ili
izostati neovisno o ostalima, pa njegove vrijednosti nisu unaprijed vezane uz
vrijednosti bilo koje druge jedinice u istom skupu.

Ta jedinica određuje sve ostalo. U usporedbi dviju skupina to je osoba, jer je
svaka osoba u samo jednoj skupini. U ponovljenom mjerenju to je i dalje osoba,
ali sada nosi dva rezultata koja su međusobno povezana, pa se analiza ne provodi
na četrdeset mjerenja nego na dvadeset razlika. Postupak koji tu vezu previdi
računa s dvostruko više podataka nego što ih doista ima.

Prvi korak analize zato nije izbor testa nego rečenica koja imenuje jedinicu.
Ako se ta rečenica ne može napisati, podaci još nisu spremni za bilo kakvu
usporedbu.

## Razlika prije oznake

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s14$n` osoba koje se informiraju s televizije ili
preko društvenih mreža, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije.

Redoslijed izvještavanja postavljamo prije nego što bilo što izračunamo. Prvo
dolazi razlika u izvornim jedinicama, zatim interval koji joj pripada, pa tek
onda test i standardizirana veličina. Taj redoslijed nije stvar ukusa. Razlika i
njezin interval odgovaraju na pitanje koliko iznosi učinak, a test odgovara na
mnogo uže pitanje je li podacima uskladiva i nula.

U našem uzorku prosječno povjerenje iznosi
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "TV"], 2)` među onima koji
gledaju televiziju i
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "društvene mreže"], 2)` među
onima koji se informiraju preko društvenih mreža. Razlika iznosi
`r hr_broj(s14$razlika, 2)` boda uz interval pouzdanosti od
`r hr_broj(s14$donja, 2)` do `r hr_broj(s14$gornja, 2)`.

Interval je ovdje važniji od svega ostaloga. On kaže da su s ovim uzorkom
uskladive i razlike ispod pola boda i razlike blizu dva boda, dakle raspon
unutar kojeg bi se praktične odluke mogle razlikovati. Izvještaj koji bi umjesto
toga napisao samo da je razlika značajna o toj neizvjesnosti ne bi rekao ništa.

Budući da je populacija simulirana, znamo i točan odgovor. Prava razlika u njoj
iznosi `r hr_broj(s14$pop_razlika, 2)` boda, dakle unutar intervala koji je
uzorak proizveo. To je jedna potvrda od mnogo mogućih, a koliko ih se u dugom
nizu ponavljanja može očekivati, pokazalo je poglavlje o procjeni.

## Interakcija — Uzorkivač dviju grupa

Sljedeći prikaz razdvaja dvije stvari koje se u praksi redovito brkaju.
Preklapanje pojedinačnih rezultata dviju skupina jedna je stvar, a preciznost
procijenjene razlike druga. Čitatelj odvojeno mijenja stvarnu razliku,
raspršenost ishoda i broj jedinica, i može prebaciti dizajn iz neovisnog u
upareni uz nepromijenjene ostale postavke.

*Slika. Jedan simulirani uzorak dviju skupina i raspodjela procijenjene razlike kroz ponovljene uzorke.*

**Što isprobati.**

1. Povećajte stvarnu razliku uz jednaku raspršenost.
2. Povećajte raspršenost uz jednaku razliku i pogledajte oba panela.
3. Povećajte broj jedinica bez promjene razlike i raspršenosti.
4. Prebacite dizajn u upareni uz sve ostalo nepromijenjeno.

Posljednji korak pomiče samo jednu postavku, a raspodjela procjena vidljivo se
sužava. Uparivanje ne mijenja ni stvarnu razliku ni raspršenost ishoda, nego
uklanja onaj dio razlike među mjerenjima koji potječe od razlika među samim
jedinicama. Ta dobit postoji samo dok analiza vezu unutar para zadrži.

## Ista razlika, dva dizajna

Tvrdnja da dizajn mijenja zaključak zvuči apstraktno dok se ne vidi na jednom
skupu brojeva. Zato konstruiramo mjerenje `r s14$np` osoba prije i poslije
jednog događaja. Skup je izmišljen za ovu svrhu i nije nalaz ni o kome, a jedino
što je u njemu namješteno jest da su dva mjerenja iste osobe povezana, kao što u
ponovljenim mjerenjima uvijek jesu.

Povezanost dvaju mjerenja iznosi `r hr_broj(s14$r_parova, 2)`. Osobe koje su
imale visoku vrijednost prije imale su je uglavnom i poslije, pa najveći dio
raspršenosti u oba mjerenja potječe od razlika među osobama, a ne od promjene
koja nas zanima.

Prosječna promjena iznosi `r hr_broj(s14$m_razlika, 2)` uz standardnu devijaciju
razlika od `r hr_broj(s14$sd_razlika, 2)`. Analiza koja pare zadrži daje interval
od `r hr_broj(s14$up_donja, 2)` do `r hr_broj(s14$up_gornja, 2)` i p-vrijednost
od `r formatC(s14$up_p, format = "f", digits = 4, decimal.mark = ",")`.

Ista mjerenja, obrađena kao da su dvije neovisne skupine, daju interval od
`r hr_broj(s14$nez_donja, 2)` do `r hr_broj(s14$nez_gornja, 2)` i p-vrijednost
od `r formatC(s14$nez_p, format = "f", digits = 3, decimal.mark = ",")`. Isti
podaci, ista prosječna promjena, i dva zaključka koja bi u izvještaju izgledala
suprotno.

Razlog nije u računu nego u nazivniku. Neovisna analiza mjeri razliku prema
raspršenosti među osobama, koja je ovdje velika. Uparena analiza mjeri je prema
raspršenosti promjena unutar osoba, koja je mnogo manja jer je razlika među
osobama oduzeta. Uparivanje zato nije trik za manju p-vrijednost nego posljedica
toga da je promjena unutar osobe druga veličina od razlike među osobama.

Koliko se time dobiva, ovisi isključivo o povezanosti dvaju mjerenja. Uparena
raspršenost sadrži faktor koji pada kako povezanost raste, pa je dobitak velik
kad se osobe kroz vrijeme drže svojih razina, a nikakav kad se drugo mjerenje
ponaša kao da s prvim nema veze. Uz povezanost blizu nule upareni postupak
zapravo gubi, jer troši polovicu stupnjeva slobode za ispravak koji nije bio
potreban. Uparivanje se zato planira u dizajnu, gdje se zna hoće li ista osoba
sa sobom donijeti stabilnu razinu, a ne bira nakon što se vide podaci.

## Jedan model iza triju testova

Tri dizajna iz prvog odjeljka izgledaju kao tri postupka, a mogu se zapisati kao
jedan. Pretpostavimo da svaka osoba ima brojčani ishod i pripadnost jednoj od
dviju skupina. Model kaže da očekivani ishod ovisi o toj pripadnosti, i to
jednim brojem po skupini.

$$\text{povjerenje} = \beta_0 + \beta_1 \cdot \text{skupina} + \varepsilon$$

Oznaka $\beta_0$ stoji za očekivani ishod u skupini koja je uzeta kao polazna,
$\beta_1$ za razliku između druge i te polazne skupine, a $\varepsilon$ za ono
što model o pojedinoj osobi nije objasnio. Varijabla skupine poprima vrijednost
nula za polaznu i jedan za drugu skupinu, pa se sve svodi na dva broja.

**Referentna skupina** je kategorija prema kojoj se izražavaju sve ostale
kategorije istog prediktora, pa njezina sredina postaje polazna vrijednost
modela, a koeficijenti ostalih kategorija odstupanja od nje.

U našem uzorku polazna je skupina onih koji se informiraju preko društvenih
mreža, pa $\beta_0$ iznosi `r hr_broj(s14$presjek, 2)` i jednak je njihovoj
sredini. Koeficijent $\beta_1$ iznosi `r hr_broj(s14$nagib, 2)` i jednak je
razlici koju smo već izračunali. Model dakle nije dao novu brojku nego stari
odgovor u novom obliku.

Dobitak od tog oblika pokazat će se kasnije, i to na dva mjesta. Prediktor s više
od dviju kategorija donosi poglavlje o više skupina, a prediktor koji nije
kategorija nego broj donosi poglavlje o regresiji. Test dviju sredina odatle
gledano nije zaseban postupak nego najmanji mogući slučaj jednog jedinog okvira.

Model pritom ne zamjenjuje dizajn. Koeficijent opisuje razliku među skupinama
onako kako su one nastale, a uzročno značenje dolazi isključivo iz načina na koji
je pripadnost skupini dodijeljena. Ako je ljudi biraju sami, model o uzroku ne
govori ništa, koliko god uredno bio ispisan.

## Što razlika sama ne kaže

Razlika u izvornim jedinicama nosi značenje samo dok se zna koliko je ljestvica
raspršena. Bod razlike na ljestvici čije su vrijednosti zbijene znači nešto
sasvim drugo nego bod razlike na ljestvici na kojoj su ljudi raspoređeni široko.
Standardizirana veličina učinka upravo to uzima u obzir.

Standardiziranu razliku uvelo je poglavlje o veličini učinka i snazi, gdje je
razlika sredina podijeljena združenom standardnom devijacijom skupina, pa se
izražava u standardnim devijacijama umjesto u izvornim jedinicama.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Za naše dvije skupine ta veličina iznosi `r hr_broj(s14$d, 2)`. Uobičajene
orijentacijske vrijednosti postoje i najčešće se navode prema Cohenu, ali ih je i
sam izvor ponudio kao pomoć u odsutnosti boljeg oslonca (Cohen, 1988). Kod
uparenog dizajna nazivnik je drugi, jer se dijeli standardnom devijacijom
razlika, pa dvije veličine s istim imenom nisu izravno usporedive. Naš upareni
skup daje `r hr_broj(s14$up_d, 2)`.

Standardizacija ipak ne rješava ono zbog čega usporedbe dviju skupina najčešće
zavaravaju. U našim podacima skupine se ne razlikuju samo po izvoru vijesti.
Prosječna dob onih koji se informiraju preko društvenih mreža iznosi
`r hr_broj(s14$pop_dob_mreze)` godine, a onih koji gledaju televiziju
`r hr_broj(s14$pop_dob_tv)` godine, dok povjerenje u ovoj populaciji raste s
dobi.

Budući da je populacija poznata, taj se udio može izmjeriti umjesto pretpostaviti.
Ukupna razlika u njoj iznosi `r hr_broj(s14$pop_razlika, 2)` boda. Ograničimo li
je na osobe između trideset i pedeset godina, dakle na raspon unutar kojeg se dob
dviju skupina znatno manje razlikuje, razlika pada na
`r hr_broj(s14$pop_razlika_uska, 2)` boda. Otprilike trećina onoga što bi
neoprezan izvještaj pripisao izvoru vijesti pripada dobi.

U našem uzorku od `r s14$n` osoba u taj uski raspon upada tek `r s14$uzak_n`
njih, i interval razlike proteže se od `r hr_broj(s14$uzak_donja, 2)` do
`r hr_broj(s14$uzak_gornja, 2)`, dakle preko nule. Uzorak koji je za ukupnu
razliku bio dovoljan za razliku unutar dobnog raspona više nije, a o tome koliko
podataka treba da bi se učinak zadane veličine uopće mogao razlučiti govori
poglavlje o veličini učinka i snazi.

## Pretpostavke i njihove granice

Postupci iz ovog poglavlja počivaju na trima pretpostavkama, i njihova se
ozbiljnost razlikuje. Neovisnost opažanja dolazi iz dizajna i ne može se
popraviti nikakvim izborom postupka. Približna normalnost odnosi se na raspodjelu
ostataka, a kod uparenog dizajna na raspodjelu razlika, ne na raspodjelu
pojedinačnih mjerenja. Jednakost varijanci potrebna je samo klasičnoj inačici
testa.

Ta se treća pretpostavka rješava izborom postupka. Welchova inačica ne zahtijeva
jednake varijance i plaća to prilagođenim stupnjevima slobode, koji zato nisu
cijeli broj. U našem uzorku varijance iznose `r hr_broj(s14$var1, 2)` i
`r hr_broj(s14$var2, 2)`, dakle vrlo su bliske, pa Welchova inačica troši
`r hr_broj(s14$df_welch, 1)` stupnjeva slobode prema `r s14$df_student` koliko ih
troši klasična. Kad su varijance slične, razlika je zanemariva, a kad nisu, Welch
je točniji. Postupak koji ništa ne gubi kad pretpostavka vrijedi i nešto dobiva
kad ne vrijedi razuman je početni izbor.

Normalnost se procjenjuje pogledom na raspodjelu, a tek onda testom.
Shapiro-Wilkov test ima istu osjetljivost na veličinu uzorka kao svaki drugi
test, pa će na velikom uzorku prijaviti odstupanja bez ikakvih posljedica, a na
malom propustiti ozbiljna. Njegov rezultat zato ne može biti prekidač koji sam
odlučuje o izboru postupka.

Krajnja opažanja traže pregled, a ne automatsko brisanje. Mogu biti pogreške u
unosu, mogu biti rijetki ali stvarni slučajevi, a mogu biti i znak da sredina
nije prikladan sažetak te varijable. Analiza provedena s njima i bez njih, uz oba
rezultata u izvještaju, poštenija je od tihe odluke donesene nakon pogleda na
p-vrijednost.

Wilcoxonov postupak radi s rangovima umjesto s vrijednostima, pa ga jedno krajnje
opažanje ne može pomaknuti. Njegovo pitanje ipak nije isto, jer se ne odnosi na
razliku sredina nego na položaje raspodjela. U našem uparenom skupu daje
p-vrijednost od
`r formatC(s14$wilcoxon_p, format = "f", digits = 4, decimal.mark = ",")`, dakle
isti zaključak, ali ne i istu tvrdnju.

**Statistika u divljini.**
**Preklapanje crtica.** Pravilo da razlika nije značajna ako se crtice pogreške
na grafu preklapaju kruži znanstvenim tekstovima kao da je egzaktno. Belia i
suradnici pozvali su 473 autora radova iz psihologije, bihevioralne neuroznanosti
i medicine da na internetskom prikazu pomiču dvije sredine s crticama sve dok
razlika ne postane taman značajna (Belia, 2005).

Odgovori su pokazali da mnogi vodeći istraživači ne razlikuju interval
pouzdanosti od standardne pogreške i ne uzimaju u obzir jesu li dvije sredine
neovisne ili dolaze iz ponovljenog mjerenja. Upravo to razlikovanje nosi cijelo
ovo poglavlje. Nalaz je pritom o čitanju grafova, a ne o crticama, pa iz njega
slijedi da graf mora reći koju veličinu prikazuje i iz kojeg dizajna dolazi, a ne
da se crtice izbjegavaju.

**Pitajte model.**
Asistent gotovo uvijek ponudi t-test čim vidi jednu kategoričku i jednu brojčanu
varijablu, i obično ne pita ono što bi moralo doći prvo. Prije poziva mu treba
opis dizajna i identifikator jedinice, jer iz samog oblika tablice ne može znati
jesu li dva stupca dva mjerenja istih osoba. Provjeravamo je li uparivanje
sačuvano, koristi li Welchovu inačicu, izvještava li razliku i interval prije
testa i je li tiho izbacio retke s praznim vrijednostima.

> Opisat ću dizajn i reći koja varijabla identificira jedinicu. Prvo prikaži
> raspodjele obiju skupina, zatim procijeni razliku s intervalom u izvornim
> jedinicama, pa tek onda provedi odgovarajući test i navedi veličinu učinka.

**Nađite grešku.**
Usporedba povjerenja u medije između dviju skupina provedena je Welchovim testom,
uz prikazane raspodjele i interval razlike. Analiza je zatim ponovljena unutar
dobne skupine od trideset do pedeset godina, gdje interval razlike obuhvaća nulu.
Zaključak izvještaja glasi da unutar te dobne skupine izvor vijesti nema veze s
povjerenjem.

Greška je čitanje nesignifikantnog rezultata kao dokaza da razlike nema. Interval
u toj podskupini proteže se preko nule u oba smjera i uključuje razlike veće od
one koju je isti uzorak izmjerio ukupno, pa podskupina razliku jednostavno nema
čime razlučiti. Stvarna razlika u simuliranoj populaciji unutar tog dobnog
raspona iznosi 0,90 boda.

## Razrađeni primjer

Cijela usporedba dviju skupina može se ispisati u nekoliko redaka, i vrijedi je
jednom vidjeti u obliku u kojem će se od ovog poglavlja nadalje pojavljivati.
Analiza procjenjuje model s binarnim prediktorom, ispisuje njegova dva broja s
intervalima i tek zatim provodi test.

Zapis `povjerenje_medijima ~ izvor` čita se kao tvrdnja da ishod ovisi o skupini.
Funkcija `lm` procjenjuje takav model, `coef` vraća njegova dva broja, a
`confint` intervale koji uz njih idu.

Ispis modela i ispis testa nose istu razliku od `r hr_broj(s14$razlika, 2)` boda,
s istim intervalom, samo drugačije poredanu. To nije podudarnost nego identitet,
jer je neovisni t-test upravo test o koeficijentu ovog modela. Kad u sljedećem
poglavlju skupina bude pet umjesto dvije, mijenja se samo broj koeficijenata.

Izvještaj koji bi na tome stao još ne bi bio potpun. Treba mu opis kako su skupine
nastale, jer ljudi svoj izvor vijesti biraju sami, i napomena da skupine nisu
izjednačene po dobi. Bez toga bi ista brojka lako prešla iz rečenice o razlici u
rečenicu o učinku, a to su dvije različite tvrdnje.

## Sažetak

Usporedba dviju grupa počinje dizajnom i rečenicom koja imenuje jedinicu
neovisnosti. Jednouzoračni, neovisni i upareni postupak tri su lica iste procjene
razlike, a razlikuju se po tome prema čemu se razlika mjeri. Isti brojevi
obrađeni kao upareni i kao neovisni daju suprotne zaključke, pa taj izbor nije
tehnički detalj. Linearni model s binarnim prediktorom otkriva zajednički okvir u
kojem je test dviju sredina najmanji mogući slučaj. Standardizirana veličina
učinka čuva usporedivost, ali ne uklanja razlike među skupinama koje s ishodom
dolaze zajedno. Sljedeće poglavlje isti model širi na više skupina i uvodi cijenu
mnogih usporedbi.

## Pojmovi

jedinica neovisnosti (*unit of independence*), neovisne skupine (*independent
groups*), upareni podaci (*paired data*), Welchov t-test (*Welch's t-test*),
referentna skupina (*reference category*), standardizirana razlika (*Cohen's d*),
Wilcoxonov test (*Wilcoxon test*)

## Zadaci

### Konceptualni

Za tri istraživačke situacije imenujte jedinicu neovisnosti i odgovarajući
dizajn. Prva uspoređuje prosječno povjerenje u uzorku sa službenom vrijednošću iz
ranijeg vala istraživanja, druga uspoređuje dvije skupine gledatelja, a treća
mjeri iste ispitanike prije i poslije kampanje.

### Računski

Dvije skupine imaju po dvadeset pet ispitanika, sredine 5,4 i 4,6 te jednake
standardne devijacije od 1,6. Izračunajte razliku i standardiziranu razliku, a
zatim ponovite račun uz standardnu devijaciju 3,2. Objasnite zašto se prva brojka
nije promijenila, a druga jest.

### Kritički

Prosudite koliko izvještaj gubi kad umjesto procjene razlike s intervalom ponudi
samo oznaku značajnosti (Cumming, 2014). Predajte kratku bilješku recenzentu i
navedite jednu odluku koja bi se bez intervala mogla donijeti pogrešno.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte korake koji su provedeni ispravno,
izdvojite tvrdnju koja iz rezultata ne slijedi i napišite rečenicu kojom bi je
trebalo zamijeniti.

---

# Uspoređivanje više grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Dekompozicija varijance | simulirana populacija | pogl. 10, 14 |

**Vinjeta.**
Simmons, Nelson i Simonsohn pokazali su da istraživač koji tijekom analize
donosi naizgled bezazlene odluke može doći do statistički značajnog rezultata za
tvrdnju koja ne može biti istinita (Simmons, 2011). Odluke su bile obične, poput
toga koji će ishod izvijestiti, koju će podskupinu pogledati i kada će prestati
prikupljati podatke.

Nijedan pojedinačni test u tom postupku nije bio pogrešno proveden. Problem je
nastao od njihova broja, jer je svaka nova usporedba bila nova prilika da
slučajnost proizvede rezultat vrijedan objave. Broj prilika nije se nigdje
vidio u izvještaju.

Kako više skupina usporediti tako da broj prilika ostane vidljiv, a zatim
utvrditi gdje se razlike zapravo nalaze?

## Cijena mnogih usporedbi

Pet skupina daje deset parova. Očit postupak jest provesti deset usporedbi iz
prethodnog poglavlja i pogledati koje su prošle prag. Prije nego što ga
odbacimo, vrijedi izmjeriti koliko taj postupak zapravo košta, i to na način na
koji je knjiga to radila i za uzorkovanje i za kategoričke podatke.

Postavljamo situaciju u kojoj razlike po konstrukciji nema. Iz iste simulirane
populacije izvučemo pet skupina po četrdeset osoba, dakle skupine koje se ne
razlikuju ni po čemu osim po tome koga je slučaj u njih smjestio. Zatim
provedemo svih deset usporedbi i zabilježimo je li barem jedna prošla prag. Sve
što nađemo je pogreška.

Kroz dvije tisuće ponavljanja barem jedna od deset usporedbi bila je značajna u
`r hr_broj(s15$stopa_parne)` % slučajeva. Postupak koji je zamišljen da griješi
u pet posto slučajeva griješi u više od četvrtine njih, a izvještaj bi u svakom
od tih slučajeva sadržavao uredno provedenu usporedbu s malom p-vrijednošću.

**Stopa obiteljske pogreške** je vjerojatnost da će barem jedan test u
unaprijed određenom skupu testova dati lažno pozitivan rezultat, uz uvjet da u
tom skupu nijedan učinak zaista ne postoji.

Uobičajena formula za tu stopu množi vjerojatnosti neuspjeha svih testova i za
deset testova daje `r hr_broj(s15$formula_neovisnih)` %. Naša izmjerena
vrijednost osjetno je niža, i razlog je vrijedan pažnje. Formula pretpostavlja
da su testovi neovisni, a deset parnih usporedbi među pet skupina dijeli
skupine, pa nisu. Ista simulacija s deset zaista neovisnih usporedbi daje
`r hr_broj(s15$stopa_neovisne)` %, dakle upravo ono što formula predviđa.

Poučak je da formula opisuje gornju granicu, a ne stopu koju parne usporedbe
doista imaju. Obje su brojke daleko iznad pet posto i obje vode istom
zaključku, ali brojku koja se navodi u izvještaju vrijedi izmjeriti umjesto
prepisati.

Postoji i postupak koji cijeli skup pitanja rješava jednim testom. Kad istu
simulaciju provedemo tako da svih pet skupina uđe u jedan zajednički model, on
griješi u `r hr_broj(s15$stopa_ukupni)` % slučajeva, dakle onoliko koliko je i
obećao. Taj postupak razvija ostatak poglavlja.

## Varijanca između i unutar

Zajednički test za više skupina mora nekako sažeti razlike među njima u jednu
brojku. Prva ideja bila bi zbrojiti udaljenosti skupnih sredina od zajedničke
sredine, ali takav zbroj sam po sebi ništa ne znači. Tri sredine razmaknute za
jedan bod velika su razlika ako su ljudi unutar skupina zbijeni, a gotovo ništa
ako su raspršeni preko cijele ljestvice.

Usporedba mora zato ići prema drugoj vrsti raspršenosti. Ukupno rasipanje
podataka razlaže se na dio koji potječe od razlika među skupinama i dio koji
potječe od razlika među pojedincima unutar iste skupine. Prvi dio je ono što
model objašnjava, drugi je ono što ostaje.

Kad se svaki od tih dvaju dijelova podijeli brojem veličina koje su ga mogle
proizvesti, dobiju se dvije prosječne raspršenosti koje se mogu staviti u omjer.
Ako skupine nemaju nikakvog učinka, obje mjere istu slučajnost i omjer se vrti
oko jedinice. Ako skupine imaju učinka, brojnik raste, a nazivnik ne.

**F-statistika** je omjer prosječne raspršenosti među skupnim sredinama i
prosječne raspršenosti opažanja oko njihovih skupnih sredina.

$$F = \frac{MS_{\text{između}}}{MS_{\text{unutar}}}$$

Oznaka $MS$ stoji za zbroj kvadriranih odstupanja podijeljen pripadnim
stupnjevima slobode.

Naziv analiza varijance zbog toga zvuči kao da je riječ o raspršenosti, a
pitanje je o sredinama. Raspršenost je ovdje mjerilo, ne predmet. Postupak je i
dalje usporedba skupnih sredina, samo izražena u jedinicama koje su za tu
usporedbu prikladne.

## Interakcija — Dekompozicija varijance

Sljedeći prikaz razdvaja dva izvora rasipanja koje ukupni graf spaja. Okomite
trake pokazuju koliko je svaka skupna sredina udaljena od zajedničke, a točke
koliko su pojedinci raspršeni oko svoje skupne sredine. Čitatelj pomiče sredine
i raspršenost odvojeno, pa se vidi da razmak među skupinama sam po sebi ne
određuje ništa.

*Slika. Dekompozicija varijance — skupne sredine, zajednička sredina i raspršenost pojedinačnih opažanja.*

**Što isprobati.**

1. Postavite sve tri sredine na 52 i zadržite standardnu devijaciju 6.
2. Razmaknite sredine na 46, 52 i 58 te usporedite novi omjer s prvim.
3. Zadržite razdvojene sredine i povećajte standardnu devijaciju na 12.

Treći korak ne mijenja nijednu skupnu sredinu, a omjer svejedno pada. Razmak
među skupinama nije, dakle, veličina koja odlučuje. Odlučuje njegov odnos prema
raspršenosti unutar skupina, jer upravo ona kaže koliko bi razmaka slučaj mogao
proizvesti sam od sebe.

## Isti model, više koeficijenata

Prethodno poglavlje zapisalo je usporedbu dviju skupina kao model s jednim
koeficijentom uz binarni prediktor. Prijelaz na pet skupina ne traži novi okvir
nego više koeficijenata u istome. Jedna kategorija ostaje referentna, a svaka od
preostalih dobiva svoj broj koji kaže koliko se od nje razlikuje.

$$\text{povjerenje} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 +
\beta_4 x_4 + \varepsilon$$

Svaka od varijabli $x_1$ do $x_4$ poprima vrijednost jedan za jednu od
nereferentnih skupina i nulu inače, pa svaka osoba aktivira najviše jedan
koeficijent. Oznaka $\beta_0$ i dalje je sredina referentne skupine, a
$\varepsilon$ ono što model o pojedincu nije objasnio. Pet sredina zapisano je s
pet brojeva, kao što je i moralo biti.

Ukupni test iz prošlog odjeljka postavlja pitanje o svim tim koeficijentima
odjednom. Pita jesu li oni zajedno dovoljno veliki da bi model sa skupinama
opisivao podatke bolje nego model koji ima samo zajedničku sredinu. Zato je
jedan test, a ne deset.

Naš uzorak od `r s15$n` osoba raspoređen je u pet skupina prema izvoru vijesti.
Ukupni test daje F od `r hr_broj(s15$f, 2)` uz `r s15$df1` i `r s15$df2`
stupnjeva slobode. Prosječna raspršenost među skupinama iznosi
`r hr_broj(s15$ms_izmedu, 1)`, a unutar skupina `r hr_broj(s15$ms_unutar, 1)`,
i njihov je omjer upravo ta F-vrijednost.

Model pritom ostaje ono što je bio u prethodnom poglavlju. Ne zna kako su ljudi
u skupine dospjeli i ne tvrdi ništa o uzroku. Izvor vijesti u ovoj populaciji
ljudi biraju sami, pa razlike među skupinama uključuju i sve ono po čemu se ti
ljudi inače razlikuju.

## Što ukupni test ne kaže

Značajan ukupni test kaže da model sa skupinama opisuje podatke bolje od
modela bez njih. Ne kaže koje se skupine razlikuju, koliko, ni u kojem smjeru.
Izvještaj koji na njemu stane predao je jednu bitnu informaciju i nijednu
upotrebljivu.

Postupak koji odgovara na to pitanje mora usporediti parove, ali sada uz
svijest o njihovu broju. Tukeyjev postupak upravo to radi. Uspoređuje sve
parove i pritom širi intervale tako da vjerojatnost barem jedne pogreške u
cijelom skupu usporedbi ostane na obećanoj razini.

Način na koji ih širi vrijedi razumjeti, jer objašnjava zašto korekcija nije
proizvoljna kazna. Kad se gleda deset razlika, ne odlučuje nijedna pojedinačno
nego najveća među njima, a najveća od deset slučajnih veličina sustavno je veća
od bilo koje pojedinačne. Postupak zato ne pita koliko je vjerojatna ova
razlika, nego koliko je vjerojatan ovako velik raspon među pet sredina.
Odgovor na to drugo pitanje daje širi interval, i to točno onoliko širi koliko
je bilo prilika.

Od `r s15$parova` parova u našem uzorku značajno se razlikuju samo oni u kojima
sudjeluju društvene mreže. One se odvajaju od sva četiri preostala izvora, a ta
četiri međusobno ne. Najveća razlika dijeli televiziju od društvenih mreža i
iznosi `r hr_broj(s15$tv_mreze, 2)` boda. Televizija i tisak ostaju nerazlučivi,
s razlikom od `r hr_broj(s15$tv_tisak, 2)` boda i intervalom od
`r hr_broj(s15$tv_tisak_donja, 2)` do `r hr_broj(s15$tv_tisak_gornja, 2)`.

Taj drugi rezultat treba pročitati oprezno. Interval je širok više od dva boda,
pa nije riječ o tome da su dva izvora izjednačena, nego o tome da ih ovaj uzorak
ne razlučuje. Odsutnost razlike i odsutnost dokaza o razlici dvije su različite
tvrdnje, a Tukeyjev ispis ih ne razlikuje umjesto nas.

Postoji i bolji postupak od uspoređivanja svega sa svime. Ako se prije podataka
zna koja usporedba nosi istraživačko pitanje, recimo ona između tradicionalnih i
digitalnih izvora, ona se može postaviti kao jedna planirana usporedba. Jedno
pitanje umjesto deset znači i užu korekciju i veću sposobnost da se razlika
uoči. Uvjet je da je pitanje postavljeno prije, a ne odabrano nakon pogleda na
sredine.

**Statistika u divljini.**
**Značajno ovdje, neznačajno ondje.** Uobičajen način da se dva učinka
usporede jest pogledati je li prvi značajan, a drugi nije, i iz toga zaključiti
da se razlikuju. Nieuwenhuis, Forstmann i Wagenmakers pregledali su 513 radova
iz pet vodećih neuroznanstvenih časopisa i našli 78 radova koji su razliku
dvaju učinaka testirali izravno i 79 radova koji su je izveli iz usporedbe
dviju oznaka značajnosti (Nieuwenhuis, 2011).

Postupak je pogrešan jer prag nije linearan. Učinak s p-vrijednošću tik ispod
praga i učinak s p-vrijednošću tik iznad njega gotovo su jednaki, a dobivaju
suprotne oznake. Usporedba dvaju učinaka zahtijeva test o njihovoj razlici, što
je upravo ono što Tukeyjev postupak i planirane usporedbe rade, a čitanje dviju
zvjezdica jedne pored druge ne radi.

**Pitajte model.**
Asistent će na zahtjev za usporedbom više skupina gotovo uvijek ponuditi ukupni
test i odmah za njim sve parne usporedbe, jer je to najčešći obrazac u kodu na
kojem je učio. Provjeravamo je li referentna skupina ona koju smo htjeli, koliko
je usporedbi zapravo provedeno i je li korekcija imenovana. Provjeravamo i
opisuje li ispis nesignifikantne parove kao jednake, jer je to najčešća
rečenica koju sam doda.

> Reci koja je skupina referentna i koliko usporedbi provodiš. Prikaži skupne
> raspodjele, procijeni zajednički model, navedi veličinu učinka, a parne
> razlike daj s intervalima i imenovanom korekcijom.

**Nađite grešku.**
Ukupni test pokazuje da model sa skupinama opisuje podatke bolje od modela bez
njih, a raspodjela ostataka ne otkriva ozbiljan problem. Veličina učinka
izračunata je i iznosi otprilike deset posto objašnjene varijabilnosti.
Zaključak izvještaja glasi da se svih pet izvora međusobno razlikuje po
percipiranoj vjerodostojnosti.

Greška je zaključak o svakom paru izveden iz ukupnog testa. Ukupni test tvrdi
samo da negdje među skupinama postoji razlika. U ovim podacima od deset parova
značajno se razlikuju samo četiri, svi s društvenim mrežama, dok portal,
televizija, radio i tisak ostaju međusobno nerazlučivi.

## Koliki je udio objašnjen

Ukupni test opet ovisi o veličini uzorka, pa uz njega ide mjera koja o njoj ne
ovisi. Prirodna mjera ovdje već postoji u samoj dekompoziciji. Ako je ukupno
rasipanje razloženo na dio među skupinama i dio unutar njih, onda je udio prvoga
u ukupnome mjera koliko je skupna pripadnost objasnila.

**Eta-kvadrat** je udio ukupne varijabilnosti ishoda koji otpada na razlike među
skupnim sredinama.

$$\eta^2 = \frac{SS_{\text{između}}}{SS_{\text{ukupno}}}$$

Za naš uzorak eta-kvadrat iznosi `r hr_broj(s15$eta2, 3)`, dakle izvor vijesti
objašnjava oko `r hr_broj(s15$eta2 * 100, 0)` % varijabilnosti u povjerenju.
Preostalih devedeset posto otpada na razlike među ljudima koje ovaj model uopće
ne vidi, i ta je asimetrija tipična za istraživanja u društvenim znanostima.

Mjera ima jedan poznat nedostatak. Računa se iz istog uzorka iz kojeg su
procijenjene i sredine, pa sustavno precjenjuje udio koji bi se našao u
populaciji. **Omega-kvadrat** ispravlja taj pomak oduzimanjem onoga što bi se od
razlika među skupinama očekivalo i kad ih ne bi bilo. Za naš uzorak iznosi
`r hr_broj(s15$omega2, 3)`, dakle nešto manje od eta-kvadrata, a razlika među
njima pada kako skupine rastu.

Ni jedna ni druga mjera ne govori je li udio velik u sadržajnom smislu. Deset
posto objašnjene varijabilnosti mnogo je za pojedinačni prediktor stava, a malo
za instrument koji bi trebao predviđati pojedinačno ponašanje. Odgovor dolazi iz
usporedbe s drugim nalazima u istom području, ne iz tablice pragova.

## Kad pretpostavke popuste

Zajednički model počiva na istim trima pretpostavkama kao usporedba dviju
skupina, i redoslijed njihove ozbiljnosti je isti. Neovisnost opažanja dolazi iz
dizajna. Približna normalnost odnosi se na raspodjelu ostataka, dakle na ono što
model nije objasnio, a ne na raspodjelu ishoda unutar svake skupine posebno.
Jednakost varijanci potrebna je klasičnoj inačici.

Homogenost se provjerava usporedbom raspršenosti skupina, a najjednostavnija
provjera jest omjer najveće i najmanje varijance. U našem uzorku on iznosi
`r hr_broj(s15$var_omjer, 2)`, dakle skupine su dovoljno slične da klasična
inačica ne bude sporna.

Kad taj omjer naraste, postoji ista rezerva kao u prethodnom poglavlju.
Welchova inačica ukupnog testa ne pretpostavlja jednake varijance i prilagođava
stupnjeve slobode. Na našim podacima daje F od `r hr_broj(s15$welch_f, 2)` uz
`r hr_broj(s15$welch_df2, 1)` stupnjeva slobode u nazivniku, dakle isti
zaključak uz nešto opreznije brojke.

Kruskal-Wallisov postupak mijenja pitanje umjesto da popravlja pretpostavku.
Rangira sve vrijednosti i uspoređuje prosječne rangove skupina, pa ga jedno
krajnje opažanje ne pomiče. Na našim podacima daje statistiku od
`r hr_broj(s15$kw, 1)` uz jednak broj stupnjeva slobode kao ukupni test.
Zaključak je isti, ali tvrdnja nije, jer se odnosi na položaje raspodjela, a ne
na sredine.

Nijedan od tih postupaka ne popravlja ovisna opažanja. Ako su ista lica mjerena
u više uvjeta ili su ljudi grupirani unutar razreda, škola ili gradova, potreban
je model koji tu strukturu uzima u obzir. Takvi modeli izlaze iz opsega ove
knjige, a njihov je zajednički korijen upravo okvir iz sljedećeg poglavlja.

## Razrađeni primjer

Cijela analiza pet skupina staje u nekoliko redaka, i vrijedi je vidjeti u
redoslijedu kojim je poglavlje izgrađeno. Zajednički model dolazi prvi, parne
usporedbe tek nakon njega.

Funkcija `aov` procjenjuje isti model kao `lm` iz prethodnog poglavlja, ali ga
ispisuje u obliku razlaganja varijance. Funkcija `TukeyHSD` prima takav model i
vraća sve parne razlike s intervalima i korigiranim p-vrijednostima.

Ispis potvrđuje ono što je poglavlje izgradilo. Redak modela nosi razlaganje
`r hr_broj(s15$ss_izmedu, 1)` prema `r hr_broj(s15$ss_unutar, 1)`, iz čega
slijede F i eta-kvadrat. Tablica parnih usporedbi zatim pokazuje da se društvene
mreže odvajaju od svakog preostalog izvora, dok se ta četiri međusobno ne
razlučuju.

Rečenica koju bi izvještaj smio sadržavati zato je uža od one koju bi ukupni
test sam sugerirao. Razlika među izvorima postoji, nosi je jedna skupina, iznosi
oko boda i pol na ljestvici od deset, i objašnjava desetinu ukupne
varijabilnosti. Sve što ide dalje od toga traži dizajn koji ovi podaci nemaju.

## Sažetak

Deset odvojenih usporedbi među pet skupina griješi mnogo češće nego što obećava,
i simulacija to pokazuje bez ijedne formule. Zajednički model rješava isti
problem jednim testom tako da razlaže rasipanje na dio među skupinama i dio
unutar njih te ih stavlja u omjer. Taj model nije nov nego je prošireni model iz
poglavlja o dvjema grupama, s jednim koeficijentom po nereferentnoj skupini.
Ukupni test ne imenuje parove, pa nakon njega dolaze planirane usporedbe ili
korigirane parne razlike s intervalima. Eta-kvadrat i omega-kvadrat opisuju
objašnjeni udio, a pretpostavke se čitaju iz ostataka. Sljedeće poglavlje
uklanja i posljednju granicu, jer isti okvir prima prediktor koji uopće nije
kategorija.

## Pojmovi

analiza varijance (*analysis of variance*), stopa obiteljske pogreške
(*familywise error rate*), F-statistika (*F-statistic*), Tukeyjev postupak
(*Tukey's HSD*), planirana usporedba (*planned contrast*), eta-kvadrat (*eta
squared*), Kruskal-Wallisov test (*Kruskal–Wallis test*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Skicirajte tri skupne sredine i raspršenosti uz koje bi ukupni test bio značajan,
a samo jedan par razlučiv.

### Računski

Razlaganje daje 120 na razlike među četirima skupinama i 480 na razlike unutar
njih, uz ukupno sto opažanja. Izračunajte obje prosječne raspršenosti, njihov
omjer i eta-kvadrat. Objasnite što bi se s omjerom dogodilo da je drugi broj
dvostruko veći.

### Kritički

Prosudite kako broj analitičkih odluka mijenja čitanje najmanje p-vrijednosti
među mnogim skupinama i ishodima (Simmons, 2011). Predajte jedan odlomak i
navedite podatak koji bi u izvještaju taj broj učinio vidljivim.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite tvrdnju o ukupnom modelu koja
stoji, imenujte tvrdnju o parovima koja ne slijedi i napišite rečenicu kojom bi
je trebalo zamijeniti.

---

# Regresija, opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 32 min | Regresijski pravac | simulirana populacija | pogl. 6, 14 i 15 |

**Vinjeta.**
Breiman je 2001. napisao da se statističko modeliranje razdvojilo na dvije
kulture koje jedna drugu jedva primjećuju (Breiman, 2001). Jedna pretpostavlja da
podatke stvara model koji treba pogoditi i protumačiti, a druga postupak
ocjenjuje po tome koliko dobro pogađa ishode koje još nije vidjela.

Prigovor nije bio matematički. Breiman je tvrdio da prva kultura svoje modele
ocjenjuje mjerama pristajanja koje ne provjeravaju ono što obećavaju, pa
istraživač lako ostane uvjeren da je opisao mehanizam, a zapravo je opisao samo
uzorak koji ima pred sobom.

Ista jednadžba pritom služi za sve. Opisati prosječan odnos, predvidjeti ishod
za novu osobu i tvrditi da bi promjena jedne varijable promijenila drugu tri su
različita zadatka. Kako znati na koji od njih model zapravo odgovara?

## Pravac kao tvrdnja o prosjeku

Vraćamo se simuliranoj populaciji od pedeset tisuća odraslih koju su koristila
poglavlja o zaključivanju. Povjerenje u medije mjereno je na ljestvici od jedan
do deset, a zanima nas kako se ono mijenja s dobi. Poglavlje o povezanosti dalo
bi na to pitanje jedan broj o jačini veze. Model daje nešto drugo, jer imenuje
očekivano povjerenje za svaku pojedinu dob.

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata procijenjenim na svih pedeset tisuća pojedinačnih odgovora.*

Pravac na slici nije nacrtan kroz sredinu oblaka po oku. Bira ga pravilo koje
za svaku moguću kombinaciju odsječka i nagiba gleda koliko svako pojedino
opažanje promašuje, i uzima onu kombinaciju kojoj ti promašaji zajedno najmanje
teže.

**Rezidual** je razlika između opažene vrijednosti ishoda kod pojedine jedinice
i vrijednosti koju za nju predviđa model, dakle onaj dio ishoda koji model nije
objasnio.

$$e_i = y_i - \hat{y}_i$$

Oznaka $y_i$ stoji za opaženu vrijednost kod $i$-te jedinice, a $\hat{y}_i$ za
vrijednost koju model za nju predviđa, pri čemu kapica i ovdje označava
procjenu.

Zbroj samih reziduala nije upotrebljiv kao mjera promašaja, jer se pozitivna i
negativna odstupanja poništavaju, pa bi loš pravac mogao izgledati savršeno.
Kvadriranje uklanja predznak i istodobno velika odstupanja košta više nego mala,
što je razlog zbog kojeg jedno jako promašeno opažanje pomiče pravac osjetnije
od deset blago promašenih.

**Metoda najmanjih kvadrata** bira koeficijente modela tako da zbroj kvadriranih
reziduala bude najmanji mogući za zadane podatke.

Model koji taj postupak daje ima oblik koji su poglavlja o dvjema i o više
skupina već koristila. Očekivano povjerenje raste od polazne vrijednosti za
onoliko koliko nalaže nagib pomnožen s dobi, a ostatak pripada onome što model
o pojedinoj osobi ne zna.

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

Oznaka $\beta_0$ ostaje očekivani ishod kada prediktor ima vrijednost nula,
$\beta_1$ je promjena očekivanog ishoda po jednoj jedinici prediktora, a
$\varepsilon_i$ je odstupanje pojedine jedinice od tog očekivanja. Ta se oznaka
odnosi na model, a rezidual $e_i$ na ono što od nje vidimo nakon što su
koeficijenti procijenjeni, pa je jedno pretpostavka o svijetu, a drugo mjerljiva
posljedica procjene. Razlika prema poglavlju o dvjema grupama je jedino u tome
što $x_i$ sada nije oznaka skupine nego izmjeren broj.

Procijenjeni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`, što znači da je deset
godina dobi u ovoj populaciji povezano s razlikom od
`r hr_broj(10 * s16$nagib_jedan, 2)` boda povjerenja. Odsječak od
`r hr_broj(s16$presjek_jedan, 2)` boda odnosio bi se na osobu od nula godina,
koje u podacima nema, pa je računski potreban i sadržajno prazan. Kad se
prediktor prije procjene umanji za svoju sredinu, odsječak postane očekivani
ishod kod osobe prosječne dobi, a nagib se ne promijeni. Isti model tada ima
jedan broj manje bez značenja.

Pravac je pritom tvrdnja o prosjecima, a ne o pojedincima. Točke na slici su
prosjeci nekoliko stotina ljudi po godini dobi i leže blizu pravca, dok
pojedinačni odgovori odstupaju od njega za nekoliko bodova u oba smjera.
Rečenica da osobe od pedeset godina imaju u prosjeku više povjerenja od osoba
od trideset opisuje te prosjeke točno i ne dopušta nikakav zaključak o
konkretnoj osobi bilo koje dobi.

## Nagib koji nosi tuđu priču

Populacija je simulirana, pa se zna po kojem je pravilu nastala. Povjerenje u
njoj raste s dobi za točno `r hr_broj(s16$istina_dob, 3)` boda po godini, a
procijenjeni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`. Procjena je za
trećinu veća od vrijednosti koju procjenjuje, i to nije pogreška uzorkovanja jer
je model procijenjen na cijeloj populaciji.

Razlog je u drugoj varijabli koja se mijenja zajedno s dobi. Izvor vijesti nije
jednako raspoređen po dobi, pa prosječna dob ide od
`r hr_broj(s16$dob_mreze, 1)` godine među onima koji se informiraju preko
društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među slušateljima radija.
Kako povjerenje ovisi i o izvoru, a stariji ljudi biraju izvore uz koje ide više
povjerenja, nagib uz dob pokupi i tu razliku i pripiše je godinama.

Tvrdnja se može provjeriti bez ijednog novog pojma. Ako nagib doista nosi tuđu
priču, onda bi unutar skupine ljudi koji se informiraju iz istoga izvora morao
biti manji, jer se ondje izvor više ne mijenja zajedno s dobi.

*Slika. Nagib uz dob procijenjen zasebno među korisnicima svakog izvora vijesti, uz zbirni nagib i vrijednost ugrađenu u generator populacije. Izrada autora.*

Nijedna od pet skupina nema nagib blizu zbirnoga. Svi se kreću između
`r hr_broj(s16$nagib_unutar_min, 4)` i `r hr_broj(s16$nagib_unutar_max, 4)`, oko
vrijednosti koja je u populaciju ugrađena, dok je zbirni nagib veći od svakoga
od njih. Ista pojava kojoj je poglavlje o povezanosti dalo ime pri usporedbi
koeficijenata unutar i između skupina ovdje se pojavljuje u modelu, i pokazuje
da razlika ne dolazi iz podataka nego iz toga što se pita.

To je konfundiranje iz poglavlja o mjerenju, sada u obliku broja umjesto
dijagrama. Koeficijent uz dob odgovara na pitanje koliko se povjerenje razlikuje
među ljudima različite dobi, a ne koliko bi se promijenilo kod jedne osobe koja
stari. Prvo je pitanje o usporedbi skupina i model na njega odgovara točno.
Drugo je pitanje o promjeni i na njega nije ni odgovarao.

Vrijedi zadržati da razlika nema veze s količinom podataka. Model je procijenjen
na svih pedeset tisuća ljudi, pa nikakvo povećanje uzorka zbirni nagib ne bi
pomaknulo prema vrijednosti koju je generator ugradio. Veći uzorak sužava
interval oko krive vrijednosti, i to je razlog zbog kojeg se preciznost i
točnost u izvještaju nikada ne miješaju.

## Prilagodba i ono što je čini mogućom

Ako opažena povezanost miješa dvije priče, izlaz je usporediti ljude koji se u
drugoj od njih ne razlikuju. Umjesto da se uzorak reže na skupine iste dobi i
istog izvora, model to radi računski, procjenjujući sve koeficijente odjednom.

**Višestruka regresija** procjenjuje povezanost svakog prediktora s ishodom pri
jednakim vrijednostima svih ostalih prediktora u modelu, pa je svaki koeficijent
usporedba jedinica koje se razlikuju po tom prediktoru, a po ostalima ne.

Model s dobi i izvorom vijesti daje uz dob nagib od
`r hr_broj(s16$nagib_dva, 4)`, praktički onu vrijednost koja je u populaciju i
ugrađena. Uspoređujući ljude koji se informiraju iz istog izvora, model je
oporavio pravilo po kojem su podaci nastali.

*Slika. Procijenjeni učinci izvora vijesti uz jednaku dob, uz vrijednosti ugrađene u generator populacije. Portal je referentna skupina. Izrada autora.*

Procjene su blago manje od ugrađenih vrijednosti, i to nije slučajnost.
Povjerenje je u populaciji zaokruženo na cijeli broj i odrezano na krajevima
ljestvice, pa mjerenje gubi dio razlika koje generator proizvodi. Isti se učinak
javlja u svakom istraživanju s ljestvicom od nekoliko stupnjeva, gdje grubo
mjerilo procjene sustavno vuče prema nuli.

Slaganje u tablici izgleda kao potvrda da postupak radi, i jest, ali samo pod
uvjetom koji se u stvarnom istraživanju nikada ne može provjeriti. Model je
pogodio jer su obje varijable koje su sudjelovale u nastanku povjerenja i
izmjerene. Da izvor vijesti nije zabilježen, koeficijent uz dob ostao bi na
`r hr_broj(s16$nagib_jedan, 4)` i ništa u ispisu ne bi upozorilo da je pogrešan.

Izraz „uz kontrolu" zato opisuje račun, a ne postupak. Kontrola u pokusu znači
da je istraživač sam dodijelio uvjete, pa se skupine ne razlikuju ni po čemu
drugome, uključujući ono što nikome nije palo na pamet izmjeriti. Kontrola u
modelu znači da su uspoređene jedinice s jednakim vrijednostima onih varijabli
koje su ušle u model.

Iz toga slijedi oblik rečenice koji svaki koeficijent zaslužuje. Uz jednak izvor
vijesti, ljudi stariji za deset godina imaju u prosjeku
`r hr_broj(10 * s16$nagib_dva, 2)` boda više povjerenja. Rečenica navodi jedinicu
prediktora, jedinicu ishoda i uvjet pod kojim usporedba vrijedi, i bez ijednog
od ta tri dijela koeficijent se ne može provjeriti. Ista se disciplina traži i
od kategorijskih koeficijenata, gdje uvjet uključuje i referentnu skupinu prema
kojoj se svaki od njih mjeri.

Odsječak u takvom modelu ostaje formalno potreban i sadržajno još slabiji nego
prije, jer sada opisuje osobu od nula godina koja se informira putem portala.
Model se time ne kvari. Kvari se samo pokušaj da se svaki broj iz ispisa
protumači kao da nešto opisuje.

Postoji i slučaj u kojem prilagodba ne uspijeva iako su sve varijable izmjerene.
Kad dva prediktora nose gotovo istu informaciju, podaci ne sadrže usporedbe u
kojima se jedan mijenja a drugi ne, pa se njihovi pojedinačni doprinosi ne mogu
razdvojiti i koeficijenti postaju osjetljivi na male promjene uzorka. Zbroj tih
prediktora model i dalje koristi jednako dobro, a pitanje o svakome od njih
zasebno u tim podacima nema odgovor.

## Interakcija — Regresijski pravac

Sljedeći prikaz razdvaja dvije stvari koje su u prethodna tri odjeljka
ispisane kao gotov rezultat. Čitatelj sam pomiče pravac i vidi kako zbroj
kvadrata reagira na svaki pomak, a zatim uključuje treću varijablu i uspoređuje
zbirni nagib s onim koji vrijedi pri njezinoj jednakoj vrijednosti. Podaci su
manji i posebno konstruirani za ovaj prikaz, kako bi se pojedini reziduali
mogli vidjeti.

*Slika. Regresijski pravac — pomični pravac, reziduali i usporedba zbirnog s prilagođenim nagibom.*

**Što isprobati.**

1. Mijenjajte odsječak i nagib dok se zbroj kvadrata ne približi prikazanom
   minimumu.
2. Povećajte samo nagib za jednu jedinicu i pratite koji se reziduali najviše
   produljuju.
3. Uključite model s prethodnim interesom i usporedite njegov nagib sa zbirnim
   pravcem.

Zbroj kvadrata oko svojeg minimuma reagira sporo, pa se pravac može osjetno
pomaknuti prije nego što se brojka vidljivo pokvari. To je ista činjenica koju
poglavlje o procjeni izražava intervalom, jer sve te bliske vrijednosti nagiba
podaci podnose gotovo jednako dobro.

## Isti model iza ranijih poglavlja

Poglavlje o dvjema grupama zapisalo je usporedbu dviju sredina kao model s
binarnim prediktorom, a poglavlje o više skupina proširilo ga je na četiri
koeficijenta. Ovdje je isti model dobio prediktor koji je broj, čime je popis
slučajeva zatvoren. Vrijedi provjeriti da to nije bila samo tvrdnja o zapisu.

Uzorak od sto dvadeset ljudi iz poglavlja o dvjema grupama daje razliku sredina
od `r hr_broj(s16$razlika_dvije, 2)` boda. Koeficijent uz izvor u modelu iznosi
`r hr_broj(s16$koef_dvije, 2)`, a omjer tog koeficijenta i njegove standardne
pogreške iznosi `r hr_broj(s16$t_dvije, 2)`, jednako kao vrijednost koju daje
t-test na istim podacima. Riječ je o jednom računu s dva imena.

Uzorak od tristo ljudi iz poglavlja o više skupina daje ukupni test s
F-vrijednošću `r hr_broj(s16$f_pet, 2)` uz `r s16$df1_pet` i `r s16$df2_pet`
stupnja slobode, što je vrijednost koju je to poglavlje ispisalo. Udio
objašnjene varijabilnosti u tom modelu iznosi
`r hr_broj(100 * s16$r2_pet, 1)` %, a to je ista brojka koju je poglavlje o više
skupina nazvalo eta-kvadratom.

Iz toga slijedi praktična posljedica za čitanje tuđih radova. Rad koji
izvještava o t-testu, rad koji izvještava o analizi varijance i rad koji
izvještava o regresiji ne koriste tri različita aparata, pa se mogu čitati istim
pitanjima o jedinici analize, o tome što je uspoređeno i uz što je usporedba
provedena.

Ista posljedica vrijedi i za odabir postupka. Tablica koja vodi od vrste
podataka i pitanja do metode, kakva stoji u dodatku o odabiru testa, pomaže dok
se uči, a njezini redovi nisu odvojeni postupci nego različiti oblici jednog
istog modela. Pitanje koje ostaje jest što je ishod, što su prediktori i jesu li
jedinice neovisne, a ime testa iz tih odgovora slijedi.

Okvir se pritom širi dalje nego što ova knjiga ide. Ishod koji nije broj nego
kategorija, mjerenja ponovljena na istim ljudima i podaci grupirani po
razredima ili gradovima traže preinake koje pripadaju literaturi izvan opsega
ovog udžbenika. Zajedničko im je da se i dalje piše model, imenuje ishod i
imenuju prediktori, pa čitatelj koji je razumio ovo poglavlje takav rad može
čitati i kad njegovu procjenu ne bi znao ponoviti.

## Pristajanje i njegove granice

Koliko dobro model opisuje podatke mjeri se udjelom varijabilnosti ishoda koji
je model uspio objasniti. Ta mjera nosi ime koje obećava više nego što daje, pa
je vrijedi definirati oprezno.

**Koeficijent determinacije** je udio ukupne varijabilnosti ishoda u promatranom
uzorku koji je model objasnio, izračunat kao jedan minus omjer zbroja kvadrata
reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Model samo s dobi objašnjava `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti
povjerenja, a model s dobi i izvorom `r hr_broj(100 * s16$r2_dva, 1)` %. Obje su
brojke male, a model s izvorom je istodobno onaj koji je oporavio pravilo po
kojem su podaci nastali. Ljudi se međusobno razlikuju iz mnoštva razloga koje
nijedno istraživanje ne bilježi, pa niska vrijednost ovdje ne znači loš model
nego da su ljudi raznoliki.

Vrijednost ima i mehaničko svojstvo koje je čini neupotrebljivom za usporedbu
modela. Nikada ne pada kad se doda prediktor, pa i onaj koji s ishodom nema
nikakve veze podigne ju za nešto. U uzorku od dvjesto osoba dodavanje pet
potpuno slučajnih brojeva podiže udio objašnjene varijabilnosti s
`r hr_broj(100 * s16$r2_bez, 1)` % na `r hr_broj(100 * s16$r2_sa, 1)` %, dok
prilagođeni koeficijent determinacije, koji kažnjava svaki dodani prediktor,
pada s `r hr_broj(100 * s16$prilagodeni_bez, 1)` % na
`r hr_broj(100 * s16$prilagodeni_sa, 1)` %. Prvi broj tvrdi da je model bolji,
drugi da je gori, i drugi je u pravu.

Postoji i druga strana iste mehanike, po kojoj vrijednost pada iako se odnos ne
mijenja. Ograničimo li populaciju na ljude između trideset i pedeset godina,
nagib uz dob ostaje `r hr_broj(s16$nagib_usko, 4)`, praktički kao prije, a udio
objašnjene varijabilnosti pada s `r hr_broj(100 * s16$r2_jedan, 1)` % na
`r hr_broj(100 * s16$r2_usko, 1)` % na `r hr_broj(s16$n_usko, 0)` ljudi.
Ograničenje raspona iz poglavlja o povezanosti radi i ovdje, jer je udio
objašnjenoga svojstvo uzorka koji je ušao u analizu, a ne odnosa među
varijablama.

Zbog toga usporedba te mjere među radovima gotovo nikada ništa ne znači.
Istraživanje na cijeloj populaciji i istraživanje na uskoj dobnoj skupini mogu
naći potpuno isti odnos i izvijestiti o vrijednostima koje se razlikuju šest
puta. Broj koji se uspoređuje jest procijenjeni koeficijent sa svojim
intervalom, jer je jedini izražen u jedinicama koje su u oba rada iste.

Pristajanje pritom ništa ne govori o tome gdje model griješi, a to se vidi tek
kad se reziduali pogledaju nasuprot vrijednostima koje model predviđa. Vrijeme
provedeno uz medije u ovoj populaciji raste s dobi za
`r hr_broj(s16$nagib_minute, 2)` minute po godini, i taj je pravac sasvim
razuman, ali njegovi reziduali nisu jednako raspršeni po cijelom rasponu.

*Slika. Reziduali modela za dnevno vrijeme uz medije nasuprot vrijednostima koje model predviđa, na slučajnom podskupu od dvije tisuće osoba.*

Raspršenost reziduala raste sa `r hr_broj(s16$rasprsenost_dolje, 0)` minuta u
šestini s najnižim predviđanjima na `r hr_broj(s16$rasprsenost_gore, 0)` u
šestini s najvišima. Model je time u jednom dijelu raspona precizniji nego u
drugome, pa jedna zajednička mjera nesigurnosti za sve vrijedi u prosjeku i ni
za koga posebno. Prikaz reziduala kaže gdje model ne pristaje, a ne što s tim
učiniti, i ta razlika između nalaza i odluke ostaje na istraživaču.

## Objašnjenje i predviđanje

Dva zadatka koje ista jednadžba obavlja razlikuju se po tome što od modela
traže. Objašnjenje traži koeficijent koji odgovara nekom stvarnom odnosu, a
predviđanje traži malu pogrešku na jedinicama koje model nije vidio. Shmueli je
pokazala da se ta dva cilja razilaze već u izboru varijabli i mjera, pa model
koji je bolji za jedno može biti lošiji za drugo (Shmueli, 2010).

Razilaženje počinje već kod izbora varijabli. Spremnost na plaćanje vijesti u
ovoj populaciji nastaje pod utjecajem povjerenja, dakle nakon ishoda koji se
modelira. Kao prediktor povjerenja ipak radi, jer podiže udio objašnjene
varijabilnosti s `r hr_broj(100 * s16$r2_dva, 1)` % na
`r hr_broj(100 * s16$r2_posljedica, 1)` % i smanjuje preostalu raspršenost. Za
predviđanje je to dobitak, a za objašnjenje besmislica, budući da nitko ne može
znati koliko će netko platiti prije nego što ta osoba to i odluči.

Razlika se dalje ne vidi dok se model ocjenjuje na podacima na kojima je
procijenjen. Vidi se čim se podaci razdvoje na skup na kojem model uči i skup
koji je odvojen prije nego što je model postavljen.

*Slika. Prosječna pogreška predviđanja dvaju modela na podacima na kojima su procijenjeni i na odvojenom skupu, u bodovima povjerenja. Izrada autora.*

Bogatiji model objašnjava `r hr_broj(100 * s16$r2_bogat, 1)` % varijabilnosti u
`r s16$n_ucenje` osoba na kojima je procijenjen, prema
`r hr_broj(100 * s16$r2_skroman, 1)` % kod skromnijeg, i na tim podacima griješi
manje. Na `r s16$n_provjera` osoba koje nije vidio griješi više od skromnijeg
modela i više nego postupak koji svakome pripiše prosjek skupa za učenje. Model
je naučio raspored slučajnih brojeva u svojem uzorku i taj raspored u novim
podacima ne postoji.

Skromniji model pritom nije samo bolji od bogatijeg nego je blizu najboljega što
je na ovim podacima uopće moguće. Povjerenje se u populaciji raspršuje sa
standardnom devijacijom `r hr_broj(s16$sd_ishoda, 2)` boda, a nakon što model
uzme u obzir dob i izvor ostaje raspršenost od `r hr_broj(s16$sd_ostatka, 2)`.
Ta je preostala raspršenost u populaciju ugrađena kao slučajni dio ishoda i
nijedan je model ne može ukloniti, pa je pogreška predviđanja odozdo ograničena
bez obzira na to koliko se varijabli doda.

Za istraživanje iz toga slijedi jedno pravilo. Tvrdnja o predviđanju provjerava
se na podacima koji u procjeni nisu sudjelovali, jer se pristajanje uvijek može
podići dodavanjem varijabli. Poglavlje o algoritmima na toj razlici gradi cijeli
argument, budući da postupci koji odlučuju o kreditima, sadržaju i rangiranju
svoju vrijednost mjere isključivo uspješnošću na jedinicama koje još nisu
viđene.

## Granica prema uzroku

Poglavlje o mjerenju uvelo je konfundirajuću varijablu kao razlog zbog kojeg
opažena veza ne dokazuje uzrok, i obećalo da će se pitanje vratiti kad za njega
bude postojao račun. Račun sada postoji i vrijedi biti precizan o tome što je
njime dobiveno.

Uz izvor vijesti u modelu, koeficijent uz dob poklopio se s pravilom po kojem je
populacija nastala. Uspjeh nije proizašao iz postupka nego iz toga što je
generator poznat, pa se znalo koje dvije varijable treba uključiti. Stvarno
istraživanje tu informaciju nema, i nijedan ispis modela ne razlikuje slučaj u
kojem su svi važni čimbenici izmjereni od slučaja u kojem nisu.

Prilagođena povezanost zato nije uzročni učinak nego usporedba pod uvjetom
uključenih varijabli. Da bi postala uzročna tvrdnja, potrebno je znati da je
uzrok prethodio ishodu, da su svi čimbenici koji djeluju na oboje izmjereni i
da nijedna uključena varijabla nije posljedica pretpostavljenog uzroka.
Posljednji uvjet je najmanje poznat, jer prilagodba za posljedicu uzroka može
uvesti pristranost ondje gdje je prije nije bilo.

Ta tri uvjeta nisu statistička nego sadržajna, pa se o njima raspravlja prije
podataka. Za pitanje o dobi i povjerenju prvi je uvjet trivijalno zadovoljen,
drugi ovisi o tome je li išta osim izvora vijesti povezano i s dobi i s
povjerenjem, a treći traži provjeru da izvor vijesti nije nešto što ljudi biraju
zbog razine povjerenja koju već imaju. Ovdje je i taj posljednji odgovor poznat,
jer generator izvor određuje prije povjerenja. U stvarnom istraživanju o tom bi
se redoslijedu raspravljalo, a ne računalo.

Odatle slijedi i skromnost u jeziku. Model daje razliku između usporedivih
skupina, i tu rečenicu treba napisati doslovno tako. Rečenica o tome što bi se
dogodilo da se nešto promijeni pripada dizajnu koji tu promjenu doista provodi
ili opravdava, a to je pitanje poglavlja o mjerenju i dizajnu, ne poglavlja o
modelima.

Postoji koristan test koji ne traži nikakav račun. Prije nego što se koeficijent
opiše kao učinak, napiše se rečenica o tome što bi se moralo dogoditi da tvrdnja
bude pogrešna, i provjeri se može li ijedan podatak iz istraživanja tu rečenicu
opovrgnuti. Ako odgovor ovisi isključivo o pretpostavci koju podaci ne dodiruju,
tvrdnja je pretpostavka napisana kao nalaz.

**Statistika u divljini.**
**Druga tablica.** Westreich i Greenland opisali su uobičajen postupak u kojem
autor u jednoj tablici prikaže sve koeficijente višestrukog modela, s
koeficijentom glavne varijable i koeficijentima kontrola jedan ispod drugoga
(Westreich, 2013). Tvrde da takva tablica potiče čitatelja da svaki redak
protumači kao učinak varijable iz tog retka, iako uvjeti pod kojima to vrijedi
ne mogu biti ispunjeni za sve retke istodobno.

Razlog je u tome što je model postavljen s obzirom na jednu varijablu. Skup
kontrola izabran je tako da usporedba po njoj bude poštena, a za neku od tih
kontrola isti skup u pravilu nije prikladan, jer među preostalim varijablama
može biti i posljedica te kontrole. Tablica pritom izgleda jednako uredno u oba
slučaja. Rad koji uz nju napiše da su svi navedeni čimbenici povezani s ishodom
ostaje točan, a rad koji svaki redak pretvori u učinak izrekao je nekoliko
tvrdnji za koje njegov dizajn jamči samo jednu.

**Pitajte model.**
Asistent pouzdano prilagodi model, izradi dijagnostičke prikaze i prevede
koeficijente u prozu. Prije poziva treba mu zadati ulogu svake varijable,
referentne kategorije i cilj analize, jer isti podaci uz isti kod daju različit
model ovisno o tome je li pitanje opisno, prediktivno ili uzročno. Provjeravamo
tri stvari. Prva je tumači li koeficijent u izvornim jedinicama i uz uvjet
ostalih varijabli, umjesto da ga opiše kao učinak. Druga je predlaže li skup
kontrola prema tome koje su varijable dostupne, umjesto prema tome koje bi
pitanje tražilo. Treća je ocjenjuje li predikciju na podacima koji su
sudjelovali u procjeni, što je najčešća pogreška u ovom zadatku.

> Prilagodi model i protumači koeficijent glavne varijable u izvornim
> jedinicama, s intervalom. Za svaku kontrolu napiši zašto je u modelu i može li
> biti posljedica glavne varijable. Predikciju ocijeni na odvojenom skupu.

**Nađite grešku.**
Na traženje da procijeni koliko dobro model predviđa povjerenje kod novih
korisnika asistent je priložio ovaj račun.

Uz ispis je napisao obrazloženje. Model objašnjava osjetno veći udio
varijabilnosti nego prethodni, a prosječna pogreška iznosi manje od dva boda
na ljestvici od jedan do deset. Iz toga zaključuje da model dovoljno pouzdano
predviđa povjerenje kod korisnika koje nije vidio i preporučuje ga za primjenu
na novim podacima.

Greška je ocjena predviđanja na podacima na kojima je model procijenjen. Račun
je ispravan i obje su brojke točne, ali obje opisuju pristajanje na skupu za
učenje, koje je uvijek bolje od uspješnosti na novim jedinicama i to postaje
prividno bolje sa svakom dodanom varijablom. Tablica u ovom poglavlju mjeri
koliko je razlika velika, jer je model s dodanim slučajnim brojevima na svojem
uzorku griješio manje, a na odvojenom skupu više nego postupak koji svakome
pripiše prosjek. Odgovor bi tražio skup podataka odvojen prije procjene, i tek
tada izračunatu pogrešku.

## Razrađeni primjer

Ponavljamo cijeli argument na jednom mjestu i u obliku u kojem bi se pojavio u
izvještaju. Pitanje je kako se povjerenje u medije mijenja s dobi, a analiza
daje dva odgovora ovisno o tome uspoređuju li se svi ljudi ili samo oni koji se
informiraju iz istog izvora.

Funkcija `confint` uz procjenu vraća i granice intervala pouzdanosti iz
poglavlja o procjeni, pa svaki nagib dolazi s rasponom vrijednosti koje su s
podacima uskladive. Funkcija `rbind` slaže dva takva raspona jedan ispod
drugoga.

*Slika. Nagib uz dob u dvama modelima, s intervalom pouzdanosti, uz vrijednost ugrađenu u generator populacije. Izrada autora.*

Intervali dvaju modela se ne preklapaju, pa razlika među njima nije stvar
nepreciznosti. Zbirni nagib je za trećinu veći od vrijednosti koju procjenjuje,
dok prilagođeni tu vrijednost dohvaća na gornjem rubu svojeg intervala, uz malo
zaostajanje koje dolazi od zaokruživanja ljestvice. Izvještaj koji bi naveo samo prvi broj ne bi
sadržavao nijednu netočnu rečenicu o podacima, i svejedno bi ostavio dojam da
dob s povjerenjem ima jaču vezu nego što je ima.

Zaključak se zato piše u dva dijela. Ljudi različite dobi razlikuju se u
povjerenju za `r hr_broj(10 * s16$nagib_jedan, 2)` boda po desetljeću, a među
ljudima koji se informiraju iz istog izvora ta razlika iznosi
`r hr_broj(10 * s16$nagib_dva, 2)` boda. Prva rečenica opisuje populaciju kakva
jest, druga izdvaja dob od izbora izvora, i tek zajedno kažu ono što je model
doista našao.

Izvještaj uz to mora reći što je izostavljeno. Model sadrži dvije varijable, a
povjerenje u medije ovisi i o obrazovanju, iskustvu s pojedinim redakcijama i
političkim sklonostima, koje ovdje nisu ni izmjerene. Nijedna od njih ne bi
promijenila to da je opisana usporedba točna, i svaka od njih mogla bi
promijeniti veličinu razlike koja ostaje kad se izjednače.

Ostaje i pitanje na koje ova analiza uopće nije odgovarala. Nijedna od dviju
rečenica ne kaže da bi se povjerenje neke osobe promijenilo time što ona
ostari, ni da bi se promijenilo time što promijeni izvor vijesti. Analiza
opisuje kako izgleda populacija u jednom trenutku, a promjena kod iste osobe
kroz vrijeme zahtijeva podatke koji istu osobu prate, kojih ovdje nema.

## Sažetak

Linearni model povezuje ishod s prediktorima kroz očekivane vrijednosti i
reziduale, a metoda najmanjih kvadrata bira koeficijente po jasnom kriteriju
koji se u widgetu može vidjeti kako radi. Više prediktora daje povezanosti pri
jednakim vrijednostima ostalih varijabli, i na poznatoj populaciji to je
dovoljno da se pravilo po kojem su podaci nastali oporavi, ali samo zato što se
znalo što treba izmjeriti. Udio objašnjene varijabilnosti raste i kad se doda
čista buka, pa pristajanje nije ocjena, dok reziduali pokazuju gdje model ne
odgovara podacima. Objašnjenje i predviđanje odatle se razdvajaju, jer se drugo
provjerava isključivo na jedinicama koje model nije vidio. Sljedeće poglavlje
uzima taj kriterij ozbiljno i pita što se događa kad postupci koji ga
zadovoljavaju počnu odlučivati o ljudima.

## Pojmovi

linearna regresija (*linear regression*), rezidual (*residual*), metoda
najmanjih kvadrata (*least squares*), koeficijent determinacije (*R-squared*),
višestruka regresija (*multiple regression*), prilagođena povezanost
(*adjusted association*), predviđanje izvan uzorka (*out-of-sample
prediction*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto se nagib uz dob mijenja kada u model uđe izvor
vijesti, a nijedan podatak o dobi pritom nije promijenjen. Imenujte pitanje na
koje odgovara svaki od dvaju nagiba.

### Računski

Poglavlje navodi da je zbirni nagib `r hr_broj(s16$nagib_jedan, 4)` boda po
godini. Izračunajte očekivanu razliku u povjerenju između osobe od 25 i osobe od
55 godina prema tom modelu, a zatim isti račun ponovite s prilagođenim nagibom
`r hr_broj(s16$nagib_dva, 4)`. Predajte obje brojke i jednu rečenicu o tome koja
od njih odgovara na pitanje o dvjema stvarnim osobama iz ove populacije.

### Kritički

Pronađite objavljeni rad ili novinski članak koji uz koeficijent iz višestrukog
modela navodi da je nešto „utjecalo" na ishod. Prosudite ga prema pitanju koje
tablica koeficijenata potiče, a dizajn ne pokriva (Westreich, 2013). Predajte
kratku bilješku s popisom varijabli za koje bi taj koeficijent bio ispravno
protumačen i onih za koje ne bi.

### Revizija modela

Ocijenite račun i zaključak iz okvira o pogrešci. Imenujte što je u kodu
ispravno, redak u kojem se pogreška događa, razlog zbog kojeg obje priložene
brojke izgledaju uvjerljivo, i napišite zaključak koji bi isti ispis podnio.

---

# Statistika u doba algoritama

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 6 min | Istraživač pravednosti | simulacija | pogl. 7 i 16 |

**Vinjeta.**
Chouldechova je analizirala instrumente za predviđanje povratka u kriminal i
pokazala da se poželjna mjerila pravednosti mogu sukobiti kada se temeljne
stope razlikuju među skupinama (Chouldechova, 2017). Jednako tumačenje
predviđenog rizika, jednake stope lažno pozitivnih odluka i jednaka ukupna
točnost ne mogu se uvijek postići istodobno.

To nije samo matematička neugodnost. Prag modela odlučuje tko će biti
zaustavljen, provjeren, preporučen ili uskraćen. Pogreške imaju različite
posljedice, a zbirna ocjena skriva na koga padaju.

Kako statistički čitati algoritam koji ne opisuje samo društvo, nego sudjeluje
u raspodjeli pažnje, prilika i rizika?

## Predikcija na novim podacima

Algoritamski model uči obrazac na skupu za treniranje i provjerava ga na
odvojenom skupu za testiranje. Razdvajanje postoji zato što model može naučiti
slučajnu posebnost podataka koje je već vidio. **Preprilagodba** nastaje kada
pristajanje treningu raste, a sposobnost generalizacije na nove slučajeve
slabi.

Predikcija i objašnjenje postavljaju različite kriterije dobrog modela
(Breiman, 2001). Predikcijski model vrednuje pogrešku na novim podacima.
Objašnjavajući model traži koeficijente i strukturu koje možemo povezati s
teorijom. Visoka prediktivna uspješnost ne pretvara korištene varijable u
uzroke.

Klasifikacija prevodi rezultat modela u kategoriju pomoću praga. Pomicanje
praga mijenja odnos lažno pozitivnih i lažno negativnih odluka. Ne postoji
prag koji minimizira svaku vrstu pogreške bez odluke o njihovoj cijeni.

## Algoritam kao društvena infrastruktura

Sustav preporuke ne predviđa samo što će osoba možda odabrati. Rangiranjem
sadržaja mijenja ono što osoba uopće može vidjeti. Podaci o prethodnom
ponašanju tako postaju ulaz u okruženje koje proizvodi sljedeće ponašanje.
Promatrač i predmet promatranja ulaze u povratnu petlju.

Metrika poput vremena zadržavanja nije neutralna zamjena za zadovoljstvo,
informiranost ili javnu vrijednost. Ona operacionalizira cilj sustava.
Optimizacija zatim vrlo učinkovito povećava ono što je izmjereno, uključujući
slučajeve u kojima mjera slabo predstavlja društvenu svrhu.

Društvenoznanstveno pitanje zato uključuje vlasništvo nad podacima, institucionalni
cilj, mogućnost žalbe i skupine koje nose pogreške. Tehnička dokumentacija
modela nije potpuna bez opisa konteksta njegove uporabe.

## Pravednost i temeljne stope

Mjere pravednosti promatraju različite dijelove tablice odluka. Jednaka stopa
lažno pozitivnih odluka usredotočuje se na osobe bez ishoda. Jednaka
prediktivna vrijednost pita koliko je pozitivnih odluka doista pozitivno.
Kada se temeljne stope razlikuju, ta se mjerila mogu matematički razići
(Chouldechova, 2017; Barocas, 2023).

Izbor mjerila nije samo tehnički. On određuje koju vrstu pogreške i koju
populaciju sustav štiti. Poštena analiza zato prikazuje više mjerila po skupini,
objašnjava prag i navodi institucionalnu posljedicu svake pogreške.

## Jezični modeli kao distribucije

Veliki jezični model proizvodi tekst predviđanjem sljedećih dijelova niza iz
raspodjele naučene na velikom korpusu. Tečnost je rezultat uspješnog
modeliranja jezičnih obrazaca. Nije ugrađena provjera da tvrdnja odgovara
stvarnom izvoru.

Model može dati korisnu strukturu, kod ili alternativno objašnjenje, ali
činjenice moraju ostati vezane uz provjerljive dokumente i podatke. Kada izvor
nije dostupan, odgovoran odgovor označava prazninu. Samouvjerena rečenica bez
podrijetla samo je predikcija koja zvuči kao znanje.

## Interakcija — Istraživač pravednosti

Istraživač pravednosti mijenja klasifikacijski prag za dvije skupine s
različitim temeljnim stopama, ali jednakom kvalitetom rezultata uvjetno na
stvarni ishod. Tako se vidi kako zajednički prag može izjednačiti neke stope
pogreške, a ipak proizvesti različitu prediktivnu vrijednost i točnost.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Analiza instrumenata za procjenu rizika
pokazala je sukob između kalibracije i jednakosti određenih stopa pogreške kada
se temeljne stope razlikuju (Chouldechova, 2017).

Tvrdnja da je model „pravedan" zato nije potpuna bez imenovanja mjerila,
skupina, praga i posljedica. Agregatna točnost može ostati jednaka dok se vrste
pogrešaka vrlo nejednako raspoređuju.

**Pitajte model.**
Asistent može izračunati tablice zabune i mjerila po skupinama. Treba mu dati
stvarne ishode, predviđene rezultate i prag, bez osobnih identifikatora.
Provjeravamo nazivnike svake stope i tražimo da sukob mjerila ne riješi
neobrazloženom tvrdnjom da je jedno „najpoštenije".

> Izračunaj tablicu zabune i stope pogrešaka zasebno po skupinama. Objasni kako
> prag i temeljne stope mijenjaju mjerila, a vrijednosni izbor ostavi jasno
> označenim.

**Nađite grešku.**
Model ima jednaku ukupnu točnost u dvjema skupinama, a prag je za obje jednak.
Zato je algoritam pravedan i nije potrebno pregledavati zasebne stope pogreške.

Greška je zaključak da jednaka ukupna točnost dokazuje pravednost. Lažno
pozitivne i lažno negativne odluke mogu se različito rasporediti unatoč istoj
točnosti.

## Razrađeni primjer

Simuliramo dvije skupine s različitim temeljnim stopama i isti bučni
prediktivni rezultat. Jedan zajednički prag pretvara rezultat u odluku.
Izračun ne tvrdi da je neka stvarna skupina takva. Pokazuje kako nazivnici
stvaraju različita mjerila.

*Slika. Stope pogrešaka u simuliranom klasifikacijskom primjeru. Izrada autora prema @barocas2023.*

Tablica pokazuje da jedno mjerilo ne opisuje cijelu raspodjelu odluka.
Promjena praga može smanjiti jednu pogrešku i povećati drugu. Odluka o
prihvatljivom odnosu zahtijeva znanje o posljedicama, mogućnosti žalbe i
instituciji koja model primjenjuje.

Ista disciplina vrijedi za sustave preporuke i jezične modele. Prije procjene
rezultata moramo znati koji je cilj optimiziran, na kojim je podacima sustav
učen i kako njegove pogreške ulaze u društvenu praksu.

## Sažetak

Algoritamski model procjenjujemo na novim podacima i prema cilju koji je doista
optimiziran. Klasifikacijski prag raspoređuje vrste pogrešaka, a različite
temeljne stope mogu dovesti mjerila pravednosti u sukob. Sustavi preporuke
mijenjaju okruženje koje mjere, dok jezični modeli proizvode tečan tekst bez
ugrađenog jamstva istinitosti. Statistička pismenost zato ostaje odgovornost za
izvor, nazivnik, cilj i posljedice odluke.

## Pojmovi

skup za treniranje (*training set*), skup za testiranje (*test set*),
preprilagodba (*overfitting*), klasifikacijski prag (*classification
threshold*), tablica zabune (*confusion matrix*), temeljna stopa (*base rate*),
algoritamska pravednost (*algorithmic fairness*)

## Zadaci

### Konceptualni

Objasnite zašto jednaka ukupna točnost ne jamči jednake posljedice za dvije
skupine. Predajte dvije moguće tablice zabune.

### Računski

Promijenite prag u objektu `sim_klasifikacija` i predajte graf dviju stopa
pogreške po skupini.

### Kritički

Prosudite zašto se mjerila pravednosti mogu sukobiti kada se temeljne stope
razlikuju (Chouldechova, 2017; Barocas, 2023). Predajte odlomak bez proglašenja
jednog mjerila univerzalno najboljim.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte dvije stvarne provjere, jednu
neopravdanu tvrdnju o pravednosti i mjerila koja još treba prikazati.
