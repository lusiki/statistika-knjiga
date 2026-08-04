# Kategorički podaci

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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
usklađena s nezavisnošću, ali ne kaže koje su ćelije za to odgovorne. Rubni su
udjeli procijenjeni iz iste tablice i zato ograničavaju varijabilnost svake
ćelije. Procijenjena standardna devijacija odstupanja zato nije samo korijen
očekivane frekvencije, nego uključuje i udjele pripadnog retka i stupca.

**Prilagođeni standardizirani rezidual** ćelije je razlika opažene i očekivane
frekvencije podijeljena procijenjenom standardnom devijacijom te razlike, koja
uzima u obzir rubne udjele retka i stupca.

$$e_{ij} = \frac{O_{ij} - E_{ij}}
{\sqrt{E_{ij}(1-p_{i\cdot})(1-p_{\cdot j})}}$$

Oznaka $e$ ovdje stoji za ostatak, dok $p_{i\cdot}$ označuje rubni udio retka, a
$p_{\cdot j}$ rubni udio stupca. Korelaciju knjiga bilježi slovom $r$ i ona s
ovim računom nema veze.

Pozitivan rezidual znači da je u ćeliji više opažanja nego što bi ih bilo bez
veze, a negativan da ih je manje. Kad je hi-kvadrat aproksimacija primjerena,
apsolutna vrijednost oko dva služi kao orijentir za neuobičajeno odstupanje.
Orijentir nije zaseban dokaz za svaku ćeliju, osobito kad se nakon ukupnog testa
pregledava mnogo reziduala.

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

Postupak je isti kao u poglavlju o uzorkovanju. Najprije konstruiramo situaciju
u kojoj veze zaista nema, izvučemo četiri tisuće tablica i pogledamo kako se
statistika ponaša. Udio odbacivanja tada procjenjuje pogrešku prve vrste i
kalibraciju postupka, jer po konstrukciji nema što otkriti. Ako se u jednoj
simuliranoj tablici pojavi samo jedna kategorija odgovora, test nije primjenjiv
i to se ponavljanje bilježi kao neodbacivanje.

Kad su očekivane frekvencije velike, poklapanje je dobro. Vrijednost ispod koje
leži devedeset pet posto simuliranih statistika iznosi
`r hr_broj(s13$null_p95_velike, 2)` i praktički se podudara s teorijskom granicom od
`r hr_broj(s13$granica, 2)`, a udio odbacivanja iznosi
`r hr_broj(s13$null_stopa_velike)` % umjesto očekivanih pet.

Kad su očekivane frekvencije oko dvije, poklapanja više nema. Ista vrijednost
pada na `r hr_broj(s13$null_p95_male, 2)` i time ispod granice, pa test odbacuje
`r hr_broj(s13$null_stopa_male)` % puta. U ovoj nultoj simulaciji iskrivljenje
ide prema opreznosti, ne prema prekomjernom odbacivanju. Taj rezultat govori o
kalibraciji pogreške prve vrste i sam po sebi ne govori koliko će često postupak
otkriti vezu koja postoji.

Snaga zahtijeva zasebnu simulaciju pod alternativom. Drugi niz tablica zato u
oba scenarija ugrađuje povezanost kojoj Cramérovo V u generirajućem modelu
iznosi `r hr_broj(s13$ciljani_v, 2)`. U velikoj tablici vjerojatnosti odgovora
iznose `r hr_broj((0.5 + s13_razlika_velike / 2) * 100)` % i
`r hr_broj((0.5 - s13_razlika_velike / 2) * 100)` %, a u maloj
`r hr_broj((0.1 + s13_razlika_male / 2) * 100)` % i
`r hr_broj((0.1 - s13_razlika_male / 2) * 100)` %. Obje primjenjuju Pearsonovu
statistiku bez Yatesove korekcije, isti prag i četiri tisuće ponavljanja. Uz
velike frekvencije postupak vezu otkriva u
`r hr_broj(s13$snaga_velike)` % ponavljanja, dok je u maloj tablici otkriva u
`r hr_broj(s13$snaga_male)` %. Prva simulacija provjerava stopu lažnog
odbacivanja pod nezavisnošću, a druga vjerojatnost otkrivanja jedne unaprijed
određene veze.

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
posao gotov, a preporuka traži da se zna od čega štiti. Nulta simulacija u ovom
odjeljku pokazuje konzervativnu stopu pogreške, dok odvojena alternativa mjeri
snagu za jednu zadanu povezanost. Tablica koja prag ne zadovoljava zato nije
automatski tablica s napuhanim nalazom, ali ni dobra kalibracija pod nulom ne
jamči dovoljnu snagu. Analitičar koji je prag provjerio i stao nije doznao ništa
o smjeru ni veličini pogreške u svojim podacima.

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
> među njima, a uz test navedi Cramérovo V i prilagođene standardizirane
> reziduale.

**Nađite grešku.**
Analiza je provjerila očekivane frekvencije i sve su iznad pet. Hi-kvadrat test
daje vrlo malu p-vrijednost, a prilagođeni standardizirani reziduali pokazuju da
najviše odstupaju televizija u najstarijoj skupini i društvene mreže u
najmlađoj.
Budući da je rezultat značajan na razini ispod jedan promil, veza između dobi i
izvora vijesti vrlo je snažna.

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
kaže samo da nesklad postoji, pa ga prilagođeni standardizirani reziduali
vraćaju u pojedine ćelije, a
Cramérovo V odvaja jačinu veze od veličine uzorka. Test prilagodbe pokazuje da
referentna raspodjela nije tehnički detalj nego istraživačka odluka. Kad su
očekivane frekvencije male, aproksimacija popušta, i tada pomažu Fisherov
postupak ili sadržajno opravdano spajanje kategorija. Sljedeće poglavlje istu
logiku usporedbe prenosi na brojčani ishod i dvije skupine.

## Pojmovi

kontingencijska tablica (*contingency table*), očekivana frekvencija (*expected
frequency*), hi-kvadrat test (*chi-squared test*), test prilagodbe
(*goodness-of-fit test*), prilagođeni standardizirani rezidual (*adjusted
standardized residual*),
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
