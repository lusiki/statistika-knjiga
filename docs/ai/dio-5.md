# DIO V: MODELI

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Kategorički podaci

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Očekivano i opaženo | `populacija_medija` · simulirano | pogl. 2–4, 10–12 |

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

Obnovljena praksa iz prethodnog poglavlja mijenja i način na koji ulazimo u
modele. Model nije ime postupka ni automat za p-vrijednost, nego opis onoga što
bismo uz izrečene pretpostavke očekivali vidjeti. Od njega tražimo usporedbu
podataka s tim očekivanjem, mjeru veličine odstupanja, provjeru granica i
izvještaj koji čuva nazivnik i neizvjesnost.

Obitelj modela nije zbirka testova. Prvi model
namjerno ostaje izvan linearnoga okvira i cijelo poglavlje čita jednu
kontingencijsku tablicu od odluke što ćelija broji do zaključka koji se smije
braniti. Hi-kvadrat test, reziduali, Cramérovo V i Fisherov postupak odgovaraju
na različita pitanja o istoj tablici, pa nijedan od njih nije zamjensko ime za
cijelu analizu.

## Brojanje prije testiranja

Kategoričke varijable ne mjere količinu nego pripadnost. Dobna skupina, izvor
vijesti, obrazovanje i regija razvrstavaju ljude u kutije, a jedino što se s
kutijama može učiniti jest prebrojati ih. Sve što slijedi u ovom poglavlju
izvedeno je iz tih brojeva, pa je vrijedno zadržati se na tome koliko se lako
prebrojavanje pokvari.

Frekvencija govori koliko je jedinica u nekoj kategoriji. **Uvjetni nazivnik**
određuje unutar koje se skupine udio računa, i tek s tim nazivnikom frekvencija
postaje čitljiva.
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

Glavni primjer koristi lokalno dostupan simulirani skup `populacija_medija`, pa
se cijela analiza može provesti bez mreže. Istu logiku čitatelj može provjeriti
na vlastitoj portalnoj kopiji ESS-a. Tada za svaku analizu mora odrediti valjani
nazivnik i upotrijebiti zadani ponder `anweight`, a dobivene brojke ne zamjenjuju
brojke glavnoga primjera.

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
4. Zadržite pomak u postocima i usporedite mali s velikim rubnim zbrojem.

Posljednji korak pokazuje ono što se u tablici brojeva ne vidi. Isti relativni
pomak u maloj ćeliji daje mnogo manji doprinos nego u velikoj, jer se svako
odstupanje dijeli očekivanom frekvencijom. Postupak zato ne mjeri koliko je
razlika velika u postocima nego koliko je malo vjerojatna uz zadane rubne
zbrojeve. U dva statička panela hi-kvadrat raste s 1,6 na 6,4, dok Cramérovo V
ostaje 0,20 jer relativna jačina obrasca ostaje ista.

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
`r hr_broj(s13$p_gof_pop, 2)`, pa test ne otkriva jasan nesklad s poznatim
populacijskim udjelima. To nije dokaz jednakosti. Najveće opaženo odstupanje
jednog udjela od populacijskoga iznosi
`r hr_broj(s13$gof_max_razlika, 1)` postotnih bodova.

Isti podaci, dva potpuno različita zaključka, i nijedan račun nije pogrešan.
Razlika je u tome što tvrdimo. Prvi test odbacuje pretpostavku koju nitko nije
imao razloga postaviti, a drugi provjerava tvrdnju koja doista nešto znači.
Budući da je populacija u ovom poglavlju simulirana i time poznata, znamo koja
je referencija istinita, što je luksuz kakav stvarno istraživanje nema. U njemu
izbor referentne raspodjele nosi istraživač, i taj se izbor obrazlaže prije
nego što se test provede.

Ista mjerna granica vrijedi kada kategorije nastanu kodiranjem teksta. Jedinica
tada nije tema nego konkretan dokument, objava ili govor koji je mogao ući u
korpus. Prije tablice treba imenovati tko je odredio kodnu knjigu i pravila
pridruživanja, a nazivnik mora obuhvatiti samo jedinice koje su prema tim
pravilima bile podobne za kodiranje. Nekodirane i višestruko kodirane jedinice
ne smiju nestati u tišini.

Retci takve tablice mogu označavati izvor teksta, a stupci kodiranu kategoriju.
Veza koju pronađemo tada pripada i tekstovima i mjernim odlukama koje su ih
pretvorile u kategorije. U poglavlju o algoritmima isti će uvjetni nazivnici i
ista kontingencijska tablica postati temelj za čitanje tablice zabune, pa se
vlasništvo nad kategorijama ne može prepustiti nevidljivom klasifikatoru.

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
egzaktni test enumerira sve tablice moguće uz zadane rubne zbrojeve i svakoj
pridružuje njezinu točnu uvjetnu hipergeometrijsku vjerojatnost. P-vrijednost je
zbroj vjerojatnosti tablica koje su prema unaprijed navedenom pravilu barem
toliko ekstremne kao opažena. Njegovo ime ne znači da je svaki drugi test
netočan, nego da račun dolazi iz točnih uvjetnih vjerojatnosti umjesto iz
aproksimacijske krivulje.

Treći put je unaprijed određena preraspodjela samih kategorija. Ona ne liječi
automatski male ćelije i ne čuva isto pitanje, jer nova kategorija definira novu
varijablu. Autor analize zato prije rezultata mora imenovati sadržajno pravilo
spajanja i preuzeti odgovornost za njega. Kategorije se ne spajaju zato da bi
nesklad postao veći ili da bi nezgodna skupina nestala.

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

Pet kategorija izvora vijesti odgovara na pitanje koji se pojedinačni izvor
bira. Odvojeno i unaprijed određeno pitanje uspoređuje digitalne s
tradicionalnim izvorima. Autor analize u njemu portal i društvene mreže svrstava
u digitalne, a televiziju, tisak i radio u tradicionalne izvore. Ta podjela ne
popravlja prvu tablicu, nego definira novu varijablu čiji se profil i test
prikazuju u nastavku.

Funkcija `table` prebrojava kombinacije dviju varijabli, `prop.table` pretvara
frekvencije u udjele uz zadani smjer, a `chisq.test` prima gotovu tablicu i
vraća statistiku, stupnjeve slobode i p-vrijednost.

Udio digitalnih izvora pada s
`r hr_broj(s13_digitalni[["18 do 29"]])` % u najmlađoj skupini na
`r hr_broj(s13_digitalni[["60 i više"]])` % u najstarijoj. Razlika iznosi
`r hr_broj(s13$razlika_digitalni, 1)` postotnih bodova, uz 95-postotni interval
pouzdanosti od `r hr_broj(s13$ci_digitalni[[1]], 1)` do
`r hr_broj(s13$ci_digitalni[[2]], 1)` postotnih bodova. Statistika iznosi
`r hr_broj(s13$hi_spojena)` uz `r s13$df_spojena` stupnja slobode, a Cramérovo V
iznosi `r hr_broj(s13$v_spojena, 2)`. U peterokategorijskoj tablici V iznosi
`r hr_broj(s13$v, 2)`, ali dvije vrijednosti ne rangiraju dvije kodne sheme.
Prva čuva razlike među pojedinačnim izvorima, a druga odgovara na uži binarni
kontrast, pa njihova usporedba služi provjeri osjetljivosti zaključka na
operacionalizaciju.

Izvještaj s time ipak nije gotov. Tablica opisuje povezanost dobi i izbora
izvora, ali ne kaže zašto ona postoji. Razlika među generacijama može biti
posljedica navike stečene u mladosti, dostupnosti uređaja ili samog položaja u
životnom ciklusu, a ovi podaci među tim objašnjenjima ne biraju. Odvajanje
takvih objašnjenja traži varijable koje tablica ne sadrži i model koji ih može
istovremeno uzeti u obzir, o čemu govori poglavlje o regresiji.

Time se zatvara i pitanje s početka poglavlja. Zbirna tablica prijava u
Berkeleyju doista nije bila usklađena s modelom nezavisnosti, što bi pokazao
hi-kvadrat test nezavisnosti (Bickel, 1975). Cramérovo V opisalo bi jačinu toga
nesklada, a reziduali ćelije koje mu najviše pridonose. Nijedan od tih alata ne
bi dao objašnjenje, jer se odgovor nalazio u varijabli koje u tablici nije bilo.
Prijave su bile neravnomjerno raspoređene po odjelima, a odjeli su se razlikovali
po tome koliko su primali. Kako se takav zbirni obrazac preokrene čim se sloj
vrati u račun, pokazuje poglavlje o povezanosti (Simpson, 1951). Ovdje je dovoljna
pouka da tablica s dvije varijable odgovara točno na jedno pitanje, a da se
pitanje o mehanizmu njome ne može ni postaviti.

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

kontingencijska tablica (*contingency table*), uvjetni nazivnik (*conditional
denominator*), očekivana frekvencija (*expected frequency*), hi-kvadrat
statistika (*chi-squared statistic*), prilagođeni standardizirani rezidual
(*adjusted standardized residual*), test prilagodbe (*goodness-of-fit test*),
referentna raspodjela (*reference distribution*), Cramérovo V (*Cramér's V*),
Fisherov egzaktni test (*Fisher's exact test*)

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

Vratite se na Simpsonov paradoks iz poglavlja o povezanosti i na Berkeleyjev
slučaj (Bickel, 1975). Skicirajte zbirnu tablicu spola i ishoda prijave te skup
odjelskih tablica koje vraćaju izostavljeni sloj. Objasnite zašto hi-kvadrat
test prve tablice ne može razlikovati razliku u sastavu prijava od razlike u
odlučivanju unutar odjela. Predajte obje sheme, jedan odlomak usporedbe i naziv
varijable bez koje se ta dva objašnjenja ne mogu razdvojiti.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite dijagnostičke korake koji su
provedeni ispravno, imenujte jedan pogrešan zaključak i navedite koju bi
veličinu izvještaj morao sadržavati da se taj zaključak ne može izvesti.

---

# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Uzorkivač dviju grupa | simulirana populacija | pogl. 2, 4, 9–11 |

**Vinjeta.**
Cumming je istraživačima predložio promjenu koja izgleda
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

Usporedba dviju sredina izgleda kao jedno pitanje, a zapravo skriva tri.
Razlika je u tome odakle dolaze dva broja koja uspoređujemo, i to pitanje nije
statističko nego pitanje o dizajnu istraživanja.

U prvom slučaju imamo jednu skupinu i unaprijed zadanu vrijednost, primjerice
sredinu ljestvice ili prag odluke. Procjena iz ranijeg anketnog vala nije takva
konstanta, jer nosi vlastitu uzoračku nesigurnost i možda drugu ciljnu populaciju
ili način mjerenja. Nju treba usporediti kao drugu procjenu, s objema
nesigurnostima. U drugom slučaju imamo dvije odvojene skupine sastavljene od
različitih ljudi, recimo osobe kojima je primarni izvor vijesti TV i osobe koje
navode društvene mreže. U trećem slučaju iste jedinice mjerimo dva puta, prije i
poslije nekog događaja, pa svaki ispitanik nosi oba rezultata.

**Jedinica neovisnosti** je entitet koji se u istraživanju mogao pojaviti ili
izostati neovisno o ostalima, pa njegove vrijednosti nisu unaprijed vezane uz
vrijednosti bilo koje druge jedinice u istom skupu.

Ta jedinica određuje sve ostalo. U usporedbi dviju skupina to je osoba, jer je
svaka osoba u samo jednoj skupini. U ponovljenom mjerenju to je i dalje osoba,
ali sada nosi dva rezultata koja su međusobno povezana, pa se analiza ne provodi
na četrdeset neovisnih mjerenja nego na dvadeset razlika. Postupak koji tu vezu
previdi tretira mjerenja kao neovisne jedinice i izostavlja kovarijancu unutar
para, pa računa pogrešnu nesigurnost. Uz pozitivnu povezanost iz ovog poglavlja
interval je nepotrebno širok.

Prvi korak analize zato nije izbor testa nego rečenica koja imenuje jedinicu.
Ako se ta rečenica ne može napisati, podaci još nisu spremni za bilo kakvu
usporedbu.

Ponovljeno mjerenje nije jedini znak ovisnosti opažanja. Učenici iz istog
razreda, članovi istog kućanstva i osobe povezane društvenom mrežom mogu dijeliti
izvor varijacije, iako u tablici zauzimaju različite retke. Čim dizajn sadrži
takvo gnijezdo ili vezu, zaustavljamo račun za neovisne skupine. Ovo poglavlje
ne uvodi modele za ovisne podatke, nego traži da se zapišu jedinica i veza te
odabere postupak koji tu strukturu može sačuvati.

## Razlika prije oznake

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s14$n` osoba koje navode TV ili društvene mreže
kao primarni izvor vijesti, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije. Glavni primjer i obvezni zadatak dostupni su bez mreže u
lokalnom skupu `populacija_medija` i upravljanom agregatu
`data/populacija-medija-agregat.csv`. Kao neobveznu nadogradnju čitatelj može na
vlastitoj portalnoj kopiji ESS Round 11, edition 3.0 usporediti prijavljeno
glasanje bez pondera i uz `anweight`, nakon što iz službenih metapodataka odredi
valjani nazivnik za `vote`; ESS mikropodaci i rezultat nisu dio knjige. Osobe s
drugim ili nedostajućim primarnim izvorom vijesti ostaju izvan glavne usporedbe.

Redoslijed izvještavanja postavljamo prije nego što bilo što izračunamo. Prvo
dolazi razlika u izvornim jedinicama, zatim interval koji joj pripada, pa tek
onda test i standardizirana razlika. Taj redoslijed nije stvar ukusa. Razlika i
njezin interval odgovaraju na pitanje koliko iznosi učinak, a test odgovara na
mnogo uže pitanje je li podacima uskladiva i nula.

U našem uzorku prosječno povjerenje iznosi
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "TV"], 2)` među onima koji
navode TV kao primarni izvor vijesti i
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "društvene mreže"], 2)` među
onima koji navode društvene mreže. Razlika iznosi
`r hr_broj(s14$razlika, 2)` boda uz interval pouzdanosti od
`r hr_broj(s14$donja, 2)` do `r hr_broj(s14$gornja, 2)`.

To je Welchov interval, koji zadržava zasebnu procjenu varijance za svaku
skupinu. Pripadni dvostrani test postavlja nultu hipotezu da je populacijska
sredina TV skupine minus populacijska sredina skupine društvenih mreža jednaka
nuli, nasuprot mogućnosti da razlika nije nula. Riječ je o razlici
populacijskih sredina, ne o jednakosti cijelih raspodjela.

Interval je ovdje važniji od svega ostaloga. On kaže da su s ovim uzorkom
uskladive i razlike ispod pola boda i razlike blizu dva boda, dakle raspon
unutar kojeg bi se praktične odluke mogle razlikovati. Izvještaj koji bi umjesto
toga napisao samo da je razlika značajna o toj neizvjesnosti ne bi rekao ništa.

Budući da je populacija simulirana, znamo i točan odgovor. Prava razlika u njoj
iznosi `r hr_broj(s14$pop_razlika, 2)` boda i ovaj je interval obuhvaća. Jedan
takav ishod ne provjerava stopu pokrivanja, a što intervali rade u dugom nizu
ponavljanja pokazalo je poglavlje o procjeni.

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
što iz njega učimo jest račun za povezana mjerenja. Pomak, varijance i povezanost
zadani su simulacijom. Bez kontrolne skupine ili randomizacije prosječna promjena
ne bi bila dokaz da ju je događaj uzrokovao.

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

Koliko se time dobiva, ovisi o varijanci razlika, koju određuju raspršenost oba
mjerenja i njihova povezanost. Uz slične rubne varijance veća pozitivna
povezanost obično daje uži interval, dok slaba povezanost ne donosi očekivani
dobitak, a pogrešno sastavljeni parovi mogu ga i poništiti. Uparivanje se zato
određuje dizajnom i stvarnim identitetom jedinice, a ne bira nakon što se vide
podaci.

## Jedan model iza triju testova

Tri dizajna iz prvog odjeljka ostaju tri različite podatkovne situacije. Kod
neovisnih skupina razliku koju smo već procijenili možemo zapisati i kao
koeficijent uz binarnu oznaku skupine. Taj zapis ovdje služi samo kao most prema
kasnijim poglavljima.

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
razlici koju smo već izračunali. Zamijenimo li referentnu skupinu, odsječak i
predznak koeficijenta promijenit će se, ali dvije procijenjene skupne sredine i
podaci neće.

Jednouzoračna usporedba polazi od jedne sredine i vanjske vrijednosti, a uparena
usporedba od sredine razlika unutar parova. Ne treba ih pretvarati u isti ispis
da bi se vidjelo što dijele, a to su procjena, nesigurnost i pitanje o nuli.
Poglavlje o više skupina proširit će oznaku skupine, a poglavlje o regresiji
objasniti širi doseg modelnoga zapisa. Ovdje se zaustavljamo na binarnoj oznaci i
ne izjednačujemo inferenciju različitih dizajna.

Model pritom ne zamjenjuje dizajn. Koeficijent opisuje razliku među skupinama
onako kako su one nastale, a uzročno značenje dolazi isključivo iz načina na koji
je pripadnost skupini dodijeljena. Ako je ljudi biraju sami, model o uzroku ne
govori ništa, koliko god uredno bio ispisan.

## Što razlika sama ne kaže

Razlika u izvornim jedinicama nosi značenje samo dok se zna koliko je ljestvica
raspršena. Bod razlike na ljestvici čije su vrijednosti zbijene znači nešto
sasvim drugo nego bod razlike na ljestvici na kojoj su ljudi raspoređeni široko.
Standardizirana razlika upravo to uzima u obzir.

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
Prosječna dob onih koji navode društvene mreže kao primarni izvor iznosi
`r hr_broj(s14$pop_dob_mreze)` godine, a onih koji navode TV
`r hr_broj(s14$pop_dob_tv)` godine, dok povjerenje u ovoj populaciji raste s
dobi.

Budući da je simulirana populacija poznata, možemo provesti opisnu analizu
osjetljivosti. Ukupna razlika u njoj iznosi
`r hr_broj(s14$pop_razlika, 2)` boda. Promijenimo li ciljnu populaciju na osobe
od trideset do četrdeset devet godina, unutar koje se skupine manje razlikuju po
dobi, razlika iznosi `r hr_broj(s14$pop_razlika_uska, 2)` boda. Taj postupak ne
mjeri „udio zbog dobi” i ne razdvaja uzročne učinke dobi i izvora vijesti.

U našem uzorku u taj raspon upada `r s14$uzak_n` od `r s14$n` osoba, a interval
razlike proteže se od `r hr_broj(s14$uzak_donja, 2)` do
`r hr_broj(s14$uzak_gornja, 2)`, dakle preko nule. U odnosu na ukupnu usporedbu
ovdje je ciljna razlika manja, a procjena manje precizna zbog manjeg broja
jedinica. Koliko podataka treba da bi se razlika zadane veličine mogla razlučiti
objašnjava poglavlje o veličini učinka i snazi.

Razlika vrijedi samo za način na koji su ovdje izmjereni povjerenje i izvor
vijesti te za populaciju koju dizajn može dosegnuti. Odluka traži još jedan
unaprijed izrečen prag. Interval od pola do gotovo dva boda može biti dovoljno
uzak za odluku kojoj je važna bilo koja pozitivna razlika, a preširok za odluku
koja traži barem dva boda. Podaci ne biraju između tih kriterija umjesto
istraživača.

## Pretpostavke i njihove granice

Najvažnija pretpostavka dolazi iz dizajna. Opažanja moraju pripadati neovisnim
jedinicama, a svaka osoba samo jednoj od dviju skupina. Ishod mora biti ispravno
kodirana brojčana varijabla, pripadnost skupini mora imati točnu referentnu
kategoriju, a način uzorkovanja mora podupirati ciljnu populaciju o kojoj se
piše. Nijedan izbor testa ne može popraviti povredu tih uvjeta.

Za točnu t-inferenciju u malim uzorcima ishodi unutar skupina moraju slijediti
normalnu raspodjelu, a u velikima su potrebne konačne varijance i odsutnost
opažanja koje samo određuje rezultat. Kod uparenog dizajna ti se uvjeti odnose
na raspodjelu razlika, ne na raspodjelu pojedinačnih mjerenja.

Welchova standardna pogreška zadržava varijancu i veličinu svake skupine
zasebno, pa ne zahtijeva jednake varijance. Obični linearni model procjenjuje
jednu zajedničku rezidualnu varijancu i raspoređuje je na obje skupine, zbog
čega njegova uobičajena homoskedastična inferencija pretpostavlja jednake
uvjetne rezidualne varijance.

U našem uzorku veličine i varijance skupina nisu jednake, pa Welch ostaje
početni izbor. On i obični linearni model daju istu procijenjenu razliku, ali
nesigurnost računaju pod različitim pretpostavkama. Brojčanu razliku u
standardnim pogreškama, stupnjevima slobode i intervalima prikazuje razrađeni
primjer. Obični linearni model ondje služi kao izričito označena usporedba pod
pretpostavkom jednake rezidualne varijance.

Normalnost se procjenjuje pogledom na raspodjelu, a tek onda testom.
Shapiro-Wilkov rezultat, kao i rezultati drugih testova, snažno ovisi o veličini
uzorka. Velik uzorak može otkriti zanemarivo odstupanje, a mali propustiti ono
koje je važno. Rezultat zato ne može biti prekidač koji sam odlučuje o izboru
postupka.

Krajnja opažanja traže pregled, a ne automatsko brisanje. Mogu biti pogreške u
unosu, mogu biti rijetki ali stvarni slučajevi, a mogu biti i znak da sredina
nije prikladan sažetak te varijable. Analiza provedena s njima i bez njih, uz oba
rezultata u izvještaju, poštenija je od tihe odluke donesene nakon pogleda na
p-vrijednost.

Wilcoxonov postupak radi s rangovima umjesto s izvornim veličinama, pa krajnja
vrijednost obično ima manji utjecaj nego na sredinu, ali postupak nije imun na
neobična opažanja. U uparenoj inačici ispituje raspored predznaka i rangova
razlika, a ne prosječnu razliku, pa nije zamjenski put do iste tvrdnje. U našem
uparenom skupu daje
p-vrijednost od
`r formatC(s14$wilcoxon_p, format = "f", digits = 4, decimal.mark = ",")`, dakle
isti zaključak, ali ne i istu tvrdnju.

**Statistika u divljini.**
**Preklapanje crtica.** Pravilo da razlika nije značajna ako se crtice pogreške
na grafu preklapaju kruži znanstvenim tekstovima kao da je egzaktno. Belia i
suradnici izvijestili su o 473 autora radova iz psihologije, bihevioralne
neuroznanosti i medicine koji su dovršili internetski zadatak pomicanja dviju
sredina s crticama sve dok razlika ne postane taman značajna (Belia, 2005).

Odgovori su pokazali da mnogi vodeći istraživači ne razlikuju interval
pouzdanosti od standardne pogreške i ne uzimaju u obzir jesu li dvije sredine
neovisne ili dolaze iz ponovljenog mjerenja. Upravo to razlikovanje nosi cijelo
ovo poglavlje. Nalaz je pritom o čitanju grafova, a ne o crticama, pa iz njega
slijedi da graf mora reći koju veličinu prikazuje i iz kojeg dizajna dolazi, a ne
da se crtice izbjegavaju.

**Pitajte model.**
Asistent može odmah ponuditi t-test čim vidi jednu kategoričku i jednu brojčanu
varijablu te preskočiti ono što bi moralo doći prvo. Prije poziva mu treba
opis dizajna i identifikator jedinice, jer iz samog oblika tablice ne može znati
jesu li dva stupca dva mjerenja istih osoba. Provjeravamo je li uparivanje
sačuvano, koristi li Welchovu inačicu, izvještava li razliku i interval prije
testa i je li tiho izbacio retke s praznim vrijednostima.

> Opisat ću dizajn i reći koja varijabla identificira jedinicu. Prvo prikaži
> raspodjele obiju skupina, zatim procijeni razliku s intervalom u izvornim
> jedinicama, pa tek onda provedi odgovarajući test i navedi veličinu učinka.

**Nađite grešku.**
Jedinica neovisnosti označena je kao osoba, a svaka je osoba u samo jednoj
skupini. Referentna skupina su društvene mreže, pa pozitivan koeficijent uz TV
znači višu sredinu u TV skupini. Raspodjele i neobična opažanja pregledani su, a
Welchov test ne traži jednake varijance. Analiza je zatim ponovljena među osobama
od 30 do 49 godina, gdje interval razlike obuhvaća nulu. Zaključak izvještaja
glasi da u toj dobnoj skupini primarni izvor vijesti nema veze s povjerenjem.

## Razrađeni primjer

Cijela usporedba dviju skupina može se ispisati u nekoliko redaka, i vrijedi je
jednom vidjeti u obliku u kojem će se od ovog poglavlja nadalje pojavljivati.
Analiza najprije daje Welchovu procjenu i interval, a zatim istu razliku zapisuje
kao koeficijent modela s binarnim prediktorom. Drugi ispis služi usporedbi
postupaka, ne zamjenjuje prvi.

Funkcija `t.test` bez dodatne postavke provodi Welchov postupak. Zapis
`povjerenje_medijima ~ izvor` čita se kao tvrdnja da ishod ovisi o skupini, a
funkcija `lm` procjenjuje takav model uz običnu homoskedastičnu nesigurnost.
Funkcija `df.residual` vraća broj stupnjeva slobode uz taj ispis.

Welchov ispis daje razliku od `r hr_broj(s14$razlika, 3)` boda, standardnu
pogrešku od `r hr_broj(s14$se_welch, 3)` i
`r hr_broj(s14$df_welch, 3)` stupnja slobode. Koeficijent modela nosi točno istu
razliku, jer je koeficijent uz TV razlika sredine televizijske i referentne
skupine društvenih mreža. Njegova obična standardna pogreška ipak iznosi
`r hr_broj(s14$se_ols, 3)` uz `r s14$df_ols` stupnjeva slobode. Interval modela
proteže se od `r hr_broj(s14$ols_donja, 3)` do
`r hr_broj(s14$ols_gornja, 3)`, prema Welchovu intervalu od
`r hr_broj(s14$donja, 3)` do `r hr_broj(s14$gornja, 3)`. Jednakost procjene
razlike zato je egzaktna, a jednakost inferencije nije. Kad broj skupina u
sljedećem poglavlju poraste s dvije na pet, modelni zapis ostaje
srodan, ali izbor postupka za nesigurnost ostaje zasebna odluka.

Izvještaj koji bi na tome stao još ne bi bio potpun. Treba mu opis kako su skupine
nastale, jer ljudi svoj izvor vijesti biraju sami, i napomena da skupine nisu
izjednačene po dobi. Bez toga bi ista brojka lako prešla iz rečenice o razlici u
rečenicu o učinku, a to su dvije različite tvrdnje.

## Sažetak

Usporedba dviju grupa počinje dizajnom i rečenicom koja imenuje jedinicu
neovisnosti. Jednouzoračni, neovisni i upareni postupak procjenjuju razliku iz
različitih podatkovnih situacija. Isti brojevi obrađeni kao upareni i kao
neovisni mogu dati različitu nesigurnost, pa taj izbor nije tehnički detalj.
Binarna oznaka skupine pokazuje da je koeficijent jednak razlici sredina, ali ne
izjednačuje Welchovu i običnu OLS nesigurnost. Standardizirana razlika pomaže
usporedbi razmjera, ali ne uklanja razlike među skupinama koje s ishodom dolaze
zajedno. Sljedeće poglavlje prelazi na više skupina i uvodi cijenu mnogih
usporedbi.

## Pojmovi

jedinica neovisnosti (*unit of independence*), neovisne skupine (*independent
groups*), upareni podaci (*paired data*), razlika aritmetičkih sredina
(*difference in arithmetic means*), Welchov t-test (*Welch's t-test*), referentna
skupina (*reference category*), standardizirana razlika (*Cohen's d*), ovisnost
opažanja (*dependence among observations*)

## Zadaci

### Konceptualni

Za tri istraživačke situacije imenujte jedinicu neovisnosti i odgovarajući
dizajn. Prva uspoređuje prosječno povjerenje u uzorku s unaprijed zadanim pragom
od pet bodova, druga uspoređuje dvije skupine prema primarnom izvoru vijesti, a
treća mjeri iste ispitanike prije i poslije kampanje.

### Računski

Iz upravljanoga agregata `data/populacija-medija-agregat.csv` uzmite retke za TV
i društvene mreže. Za svaki redak podijelite `zbroj_povjerenja` stupcem `broj`,
provjerite pohranjeni prosjek i izračunajte razliku aritmetičkih sredina. Zatim
pretpostavite jednake standardne devijacije 1,6 pa 3,2 i za obje izračunajte
standardiziranu razliku. Objasnite zašto se prva brojka nije promijenila, a druga
jest. Za rad bez datoteke upotrijebite izvadak iz istoga agregata.

*Slika. Izvadak upravljanoga agregata za obvezni zadatak.*

### Kritički

Vratite se operacionalizaciji iz poglavlja 2 i tumačenju intervala iz poglavlja
9. Za glavni primjer najprije napišite što ljestvica povjerenja i kategorija
izvora vijesti ne mjere. Zatim za isti interval usporedite odluku kojoj je važna
bilo koja pozitivna razlika s odlukom koja traži najmanje dva boda. Predajte
kratku bilješku recenzentu i objasnite zašto sama oznaka značajnosti ne može
riješiti ni problem mjerenja ni izbor praga (Cumming, 2014).

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte referentnu skupinu i objasnite što
bi se promijenilo, a što ostalo isto kada bi se referenca zamijenila. Zatim
provjerite jedinicu neovisnosti, vrstu ishoda, odnos prema varijancama i doseg
ciljne populacije. Izdvojite jedinu tvrdnju koja iz rezultata ne slijedi i
napišite rečenicu kojom bi je trebalo zamijeniti.

---

# Uspoređivanje više grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Dekompozicija varijance | `populacija_medija` (CC BY 4.0) | pogl. 9–11, 14 |

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
`r hr_broj(s15$stopa_parne)` % slučajeva. Svaki pojedinačni test nosi stopu od
pet posto, ali cijela obitelj griješi u više od četvrtine ponavljanja. Izvještaj
bi u svakom od njih sadržavao uredno provedenu usporedbu s malom
p-vrijednošću.

**Stopa obiteljske pogreške** je vjerojatnost da će barem jedan test u
unaprijed određenom skupu testova dati lažno pozitivan rezultat, uz uvjet da u
tom skupu nijedan učinak zaista ne postoji.

Definicija opisuje potpunu nultu situaciju koju ovdje simuliramo. Ako neke
razlike postoje, obiteljsko pitanje ostaje isto za preostale istinite nulte
tvrdnje. Pitamo hoće li barem jedna od njih biti pogrešno odbačena.

Uobičajena formula za tu stopu množi vjerojatnosti neuspjeha svih testova i za
deset neovisnih testova daje `r hr_broj(s15$formula_neovisnih)` %. Naša je
izmjerena vrijednost niža jer deset parnih usporedbi među pet skupina dijeli
skupine. Testovi zato nisu neovisni. Zasebna simulacija s deset doista
neovisnih usporedbi daje `r hr_broj(s15$stopa_neovisne)` %, što odgovara
formuli.

Formula je, dakle, referentna vrijednost za neovisne testove, a ne opća gornja
granica za svaki ovisni skup usporedbi. Obje su procjene iz dvije tisuće
ponavljanja daleko iznad pet posto i vode istoj praktičnoj posljedici. Uz
najmanju p-vrijednost moramo znati koliko je prilika za pogrešku postupak
otvorio.

Postoji i postupak koji cijeli skup pitanja rješava jednim testom. Kad istu
simulaciju provedemo tako da svih pet skupina uđe u jedan zajednički model, on
griješi u `r hr_broj(s15$stopa_ukupni)` % slučajeva. Uz konačnih dvije tisuće
ponavljanja ta je procjena u skladu s obećanih pet posto. Taj postupak razvija
ostatak poglavlja.

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

## Veličina i F-omjer

Prikaz je prvo pokazao udio rasipanja koji pripada razlikama među skupnim
sredinama. Zbroj kvadriranih odstupanja označavat ćemo kraticom $SS$.
$SS_{\text{između}}$ sažima odstupanja skupnih sredina od zajedničke sredine,
$SS_{\text{unutar}}$ odstupanja pojedinaca od njihove skupne sredine, a
$SS_{\text{ukupno}}$ sva odstupanja pojedinačnih vrijednosti od zajedničke
sredine. Ukupni zbroj jednak je zbroju dijela između i dijela unutar skupina.
Omjer prvoga i ukupnoga daje veličinu povezanu sa skupinama.

**Eta-kvadrat** je udio ukupne varijabilnosti ishoda koji otpada na razlike među
skupnim sredinama.

$$\eta^2 = \frac{SS_{\text{između}}}{SS_{\text{ukupno}}}$$

Za naš uzorak eta-kvadrat iznosi `r hr_broj(s15$eta2, 3)`. U njemu izvor
vijesti opisuje oko `r hr_broj(s15$eta2 * 100, 0)` % varijabilnosti u
povjerenju, dok većina razlika među ljudima ostaje izvan modela. Taj broj
opisuje uzorak i nema prikazan interval. Omega-kvadrat umanjuje očekivanu
uzoračku pristranost eta-kvadrata i ovdje iznosi
`r hr_broj(s15$omega2, 3)`, ali ni njegova uzoračka neizvjesnost u ovom primjeru
nije kvantificirana.

Nijedna mjera sama ne određuje je li udio sadržajno velik. Isti udio može biti
važan za objašnjenje društvenog stava, a preslab za predviđanje pojedinačnog
ponašanja. Procjenu zato uspoređujemo s unaprijed obrazloženim najmanjim važnim
učinkom i nalazima iz istog područja, a ne s univerzalnom tablicom pragova.

Drugi sažetak iz prikaza uspoređuje prosječne raspršenosti. Ako imamo $k$
skupina i $n$ opažanja, $SS_{\text{između}}$ dijelimo s $k - 1$, a
$SS_{\text{unutar}}$ s $n - k$. Ti djelitelji jesu stupnjevi slobode. Dobivene
prosječne raspršenosti označavamo s $MS_{\text{između}}$ i
$MS_{\text{unutar}}$, pri čemu kratica $MS$ označava srednji kvadrat.

**F-statistika** je omjer prosječne raspršenosti među skupnim sredinama i
prosječne raspršenosti opažanja oko njihovih skupnih sredina.

$$F = \frac{MS_{\text{između}}}{MS_{\text{unutar}}}$$

Kad su populacijske sredine jednake, obje prosječne raspršenosti mjere isti
izvor slučajnosti i F se kreće oko jedan. Stupnjevi slobode $k - 1$ i $n - k$
određuju pripadnu referentnu F-raspodjelu. Što je opaženi omjer dalje iznad
jedan, to je manje uskladiv s jednakim populacijskim sredinama.

Naziv analiza varijance zbog toga zvuči kao da je riječ o raspršenosti, a
pitanje je o sredinama. Raspršenost je ovdje mjerilo, ne predmet. Postupak je i
dalje usporedba skupnih sredina, samo izražena u jedinicama koje su za tu
usporedbu prikladne.

## Isti model, više koeficijenata

Prethodno poglavlje zapisalo je usporedbu dviju skupina kao model s jednim
koeficijentom uz binarni prediktor. Prijelaz na pet skupina ne traži novi okvir
nego više koeficijenata u istome. Jedna kategorija ostaje referentna, a svaka od
preostalih dobiva svoj broj koji kaže koliko se od nje razlikuje.

Četiri binarna pokazatelja, označena s $x_1$ do $x_4$, predstavljaju četiri
nereferentne skupine. Svaki poprima jedan za pripadnike svoje skupine i nulu za
ostale. Koeficijent $\beta_0$ označava sredinu referentne skupine, a svaki od
koeficijenata $\beta_1$ do $\beta_4$ razliku pripadne skupine prema njoj.
Ostatak $\varepsilon$ predstavlja ono što model o pojedincu nije opisao.

$$\text{povjerenje} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 +
\beta_4 x_4 + \varepsilon$$

Svaka osoba aktivira najviše jedan pokazatelj. Pet skupnih sredina tako je
zapisano s pet koeficijenata.

Klasični ukupni test iz prošlog odjeljka postavlja pitanje o svim tim
koeficijentima odjednom. Pita jesu li oni zajedno dovoljno veliki da bi model
sa skupinama opisivao podatke bolje nego model koji ima samo zajedničku sredinu.
Zato je jedan test, a ne deset.

Zajednički su oblik modela sredina i njegove točkaste procjene, ne svaki način
računanja njihove nesigurnosti. Klasična analiza varijance procjenjuje jednu
zajedničku rezidualnu varijancu, kao obični homoskedastični linearni model.
Welchov ukupni test zadržava zasebne skupne varijance i prilagođava stupnjeve
slobode. Sredine i njihove razlike ostaju iste točkaste procjene, ali standardne
pogreške, stupnjevi slobode, intervali i p-vrijednosti ne moraju biti isti.

Brojčani primjer dostupan je bez mreže u simuliranom skupu
`data/populacija-medija.csv`, a obvezni zadatak u agregiranoj tablici od pet
redaka `data/populacija-medija-agregat.csv`. Obje datoteke nose licencu CC BY
4.0. Kao neobaveznu nadogradnju čitatelj može na podacima ESS Round 11, edition
3.0 koje samostalno preuzme s portala usporediti hrvatske skupine uz ponder
`anweight`, nakon što iz službenih metapodataka odredi valjani nazivnik. ESS
mikropodaci i empirijski rezultat nisu dio knjige.

Naš uzorak od `r s15$n` osoba raspoređen je u pet skupina prema izvoru vijesti.
Već smo vidjeli opisani udio u uzorku. Ukupna provjera zatim daje F od
`r hr_broj(s15$f, 2)` uz `r s15$df1` i `r s15$df2` stupnjeva slobode te
p-vrijednost manju od 0,001.
Prosječna raspršenost među skupinama iznosi `r hr_broj(s15$ms_izmedu, 1)`, a
unutar skupina `r hr_broj(s15$ms_unutar, 1)`. Njihov omjer govori da negdje
među sredinama postoji razlika, ali još ne odgovara na pitanje koje su razlike
važne ni koliko su precizno procijenjene.

Model pritom ostaje ono što je bio u prethodnom poglavlju. Ne zna kako su ljudi
u skupine dospjeli i ne tvrdi ništa o uzroku. Izvor vijesti u ovoj populaciji
ljudi biraju sami, pa razlike među skupinama uključuju i sve ono po čemu se ti
ljudi inače razlikuju.

## Nakon ukupnog testa

Ukupni test ovdje sažima globalno pitanje, ali nije cilj analize ni obvezna
dozvola za unaprijed planirane usporedbe. Kaže da model sa skupinama opisuje
podatke bolje od modela bez njih, ali ne kaže koje se skupine razlikuju, koliko,
ni u kojem smjeru. Sadržajni odgovor traži procijenjene razlike i intervale,
nakon što je broj postavljenih pitanja ostao vidljiv.

Ako je usporedba određena prije gledanja rezultata, ona je **planirana
usporedba**. Kad se parovi biraju nakon ukupnog testa, treba imenovati
**post-hoc postupak** i obitelj pitanja koju štiti. U klasičnom modelu sa
zajedničkom rezidualnom varijancom Tukeyjev postupak uspoređuje sve parove i
širi istodobne intervale tako da stopa obiteljske pogreške u tome skupu ostane
na obećanoj razini.

Način na koji ih širi vrijedi razumjeti, jer objašnjava zašto korekcija nije
proizvoljna kazna. Kad se gleda deset razlika, ne odlučuje nijedna pojedinačno
nego najveća među njima, a najveća od deset slučajnih veličina sustavno je veća
od bilo koje pojedinačne. Postupak zato ne pita koliko je vjerojatna ova
razlika, nego koliko je vjerojatan ovako velik raspon među pet sredina.
Odgovor na to drugo pitanje daje širi interval. Njegova širina ovisi o broju
skupina i zajedničkoj raspodjeli svih usporedbi, a ne o proizvoljnoj kazni.

Od `r s15$parova` parova u našem uzorku razlučivi su samo oni u kojima
sudjeluju društvene mreže. One se odvajaju od sva četiri preostala izvora, a ta
četiri međusobno ne. Kao ilustraciju čitamo razliku televizije i društvenih
mreža. Iznosi `r hr_broj(s15$tv_mreze, 2)` boda, uz istodobni
95-postotni interval od `r hr_broj(s15$tv_mreze_donja, 2)` do
`r hr_broj(s15$tv_mreze_gornja, 2)`. Televizija i tisak ostaju nerazlučivi, s
razlikom od `r hr_broj(s15$tv_tisak, 2)` boda i intervalom od
`r hr_broj(s15$tv_tisak_donja, 2)` do `r hr_broj(s15$tv_tisak_gornja, 2)`.

Taj drugi rezultat treba pročitati oprezno. Širina intervala veća je od dva
boda, pa nije riječ o tome da su dva izvora izjednačena, nego o tome da ih ovaj
uzorak ne razlučuje. Odsutnost razlike i odsutnost dokaza o razlici dvije su
različite tvrdnje, a Tukeyjev ispis ih ne razlikuje umjesto nas.

Postoji i bolji postupak od uspoređivanja svega sa svime. Ako se prije podataka
zna koja usporedba nosi istraživačko pitanje, recimo ona između tradicionalnih i
digitalnih izvora, ona se može postaviti kao jedna planirana usporedba. Jedno
pitanje umjesto deset ne traži zaštitu obitelji od deset naknadno odabranih
parova, pa interval može biti uži i razlika razlučivija. Uvjet je da je pitanje
postavljeno prije, a ne odabrano nakon pogleda na sredine.

## Granice pretpostavki

Svaki redak najprije mora odgovarati jednoj jedinici neovisnosti. Ako su iste
osobe mjerene više puta ili redci dijele kućanstvo, razred, školu, grad,
organizaciju ili mrežnu vezu, zaustavljamo običnu inferenciju neovisnih redaka.
Ni klasični test, ni Welchova inačica, ni rangiranje ne popravljaju takvu
ovisnost. Modeli za ponovljena i ugniježđena opažanja ostaju izvan opsega
knjige.

Tek za prihvatljive jedinice gledamo raspodjelu ostataka i skupne
raspršenosti. Približna normalnost odnosi se na ostatke, odnosno na ono što
model nije objasnio. Jednakost varijanci potrebna je klasičnoj inačici, ali
jedna brojka ne može dokazati da je pretpostavka ispunjena.

Omjer najveće i najmanje skupne varijance služi samo kao orijentacijski
pokazatelj. U našem uzorku iznosi `r hr_broj(s15$var_omjer, 2)`. Taj rezultat
čitamo uz grafove skupnih raspodjela i ostataka, veličine skupina i način
nastanka podataka. Ne služi kao dozvola za klasičnu inferenciju. Ako pokazatelj
i grafovi upozore na nejednake varijance, Welchov ukupni test zadržava zasebne
skupne varijance i prilagođava stupnjeve slobode.

Na našim podacima Welchova inačica daje F od `r hr_broj(s15$welch_f, 2)` uz
`r hr_broj(s15$welch_df2, 1)` stupnjeva slobode u nazivniku. Smjer i iznosi
razlika među sredinama ostaju isti, dok se inferencijska neizvjesnost računa
drukčije. To je analiza osjetljivosti na način računanja nesigurnosti, a ne
dokaz da su varijance jednake. Welchova ukupna provjera pritom ne potvrđuje
valjanost prikazanih Tukeyjevih intervala. Ako su nejednake varijance uvjerljive,
parove treba obraditi istodobnim postupkom koji ih dopušta ili parnu inferenciju
ostaviti otvorenom.

Kruskal-Wallisov postupak mijenja pitanje umjesto da popravlja klasični model.
Rangira vrijednosti i uspoređuje raspodjele rangova skupina. Time smanjuje
izravnu ulogu brojčane udaljenosti pojedinačnog krajnjeg opažanja, ali nije
postupak bez pretpostavki. Na našim podacima daje statistiku od
`r hr_broj(s15$kw, 1)` uz jednak broj stupnjeva slobode kao ukupni test.
Tumačenje kao razlike u položaju traži usporediv oblik raspodjela, a nijedno
rangiranje ne uklanja problem ovisnih redaka.

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
Asistent na zahtjev za usporedbom više skupina može ponuditi ukupni test i
odmah zatim sve parove. Prije prihvaćanja ispisa provjeravamo jedinicu
neovisnosti, referentnu skupinu, broj usporedbi i imenovani post-hoc postupak.
Zatim tražimo veličinu učinka te procijenjene razlike s intervalima. Oznaka da
par nije statistički razlučiv ne smije se prevesti u tvrdnju da su skupine
jednake.

> Najprije provjeri jedinicu neovisnosti i prikaži skupne raspodjele. Navedi
> eta-kvadrat prije ukupnog testa. Reci koja je skupina referentna, koliko
> usporedbi provodiš i je li svaka bila planirana ili post-hoc. Razlike prikaži
> s istodobnim intervalima i imenovanim postupkom zaštite obitelji.

**Nađite grešku.**
Asistent je nakon ukupnog testa ponudio sljedeći kod. To je sumnjivi artefakt,
ne uputa za izvršavanje. U njemu je točno jedna pogreška koja mijenja
statističku tvrdnju.

> ```r
> model <- aov(povjerenje_medijima ~ izvor_vijesti, data = pet_izvora)
> pairwise.t.test(
>   pet_izvora$povjerenje_medijima,
>   pet_izvora$izvor_vijesti,
>   p.adjust.method = "none"
> )
> ```

Odredite koju obitelj pogrešaka drugi redak ostavlja nezaštićenom i zašto
uredne pojedinačne p-vrijednosti ne uklanjaju taj prigovor. Ne pišite zamjenski
kod.

## Razrađeni primjer

Cijela analiza pet skupina staje u nekoliko redaka. Redoslijed tumačenja ostaje
važan. Najprije dolazi veličina, zatim ukupna provjera, pa
procijenjene razlike s istodobnim intervalima.

Funkcija `aov` procjenjuje isti oblik modela sredina kao `lm` iz prethodnog
poglavlja, ali ga ispisuje kao razlaganje varijance. Prva izračunata mjera zato
je eta-kvadrat. Uobičajena F-inferencija funkcije `aov` pripada
homoskedastičnom linearnom modelu s jednom zajedničkom rezidualnom varijancom,
a ne Welchovu postupku sa zasebnim skupnim varijancama i prilagođenim
stupnjevima slobode. Funkcija `TukeyHSD` zatim vraća sve parne razlike s
istodobnim intervalima i korigiranim p-vrijednostima za istu klasičnu granu sa
zajedničkom rezidualnom varijancom.

Razlaganje `r hr_broj(s15$ss_izmedu, 1)` prema
`r hr_broj(s15$ss_unutar, 1)` najprije daje opisani udio u uzorku, a F samo
provjerava je li cijela skupina razlika
razlučiva od slučajnosti. Tablica parnih usporedbi daje stvarni sadržaj
rezultata. Društvene mreže odvajaju se od svakog preostalog izvora, dok se ta
četiri međusobno ne razlučuju.

Rečenica koju bi izvještaj smio sadržavati zato ne počinje oznakom ukupnog
testa. U simuliranom uzorku skupna pripadnost opisuje oko desetinu
varijabilnosti, ali neizvjesnost toga udjela ovdje nije kvantificirana. Kao
ilustrativni par, razlika televizije i društvenih mreža iznosi oko 1,59 bodova
na ljestvici od deset, uz istodobni 95-postotni interval od približno 0,71 do
2,46. Razlučive su sve četiri usporedbe s društvenim mrežama. Sve što ide dalje
od opisne veze traži dizajn koji ovi podaci nemaju.

## Sažetak

Deset odvojenih usporedbi među pet skupina otvara mnogo više prilika za pogrešku
nego jedan unaprijed određen postupak. Zajednički model razlaže rasipanje na
varijancu između skupina i varijancu unutar skupina. Eta-kvadrat prvo opisuje
koliki je udio povezan sa skupinama, ali njegova neizvjesnost u ovom primjeru
nije kvantificirana. F-statistika zatim provjerava cijelu obitelj razlika.
Ukupni test nije završni odgovor. Nakon njega dolaze planirane
usporedbe ili imenovani post-hoc postupak s procijenjenim razlikama i
istodobnim intervalima. Orijentacijski omjer varijanci nije dokaz pretpostavke,
a ponovljeni, ugniježđeni ili povezani redci zaustavljaju običnu inferenciju
neovisnih opažanja. Sljedeće poglavlje isti model proširuje na prediktor koji
nije samo kategorija.

## Pojmovi

analiza varijance (*analysis of variance*), stopa obiteljske pogreške
(*familywise error rate*), F-statistika (*F-statistic*), planirana usporedba
(*planned comparison*), post-hoc postupak (*post-hoc procedure*), eta-kvadrat
(*eta squared*), varijanca između skupina (*between-group variance*), varijanca
unutar skupina (*within-group variance*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Skicirajte tri skupne sredine i raspršenosti uz koje bi ukupni test bio značajan,
a samo jedan par razlučiv. Zatim pretpostavite da ste taj par odabrali tek nakon
pregleda svih sredina. Odredite je li usporedba planirana ili post-hoc, imenujte
obitelj koju treba zaštititi i objasnite zašto je ne smijete prikazati kao jedno
unaprijed postavljeno pitanje.

### Računski

Razlaganje daje 120 na razlike među četirima skupinama i 480 na razlike unutar
njih, uz ukupno sto opažanja. Izračunajte obje prosječne raspršenosti, njihov
omjer i eta-kvadrat. Objasnite što bi se s omjerom dogodilo da je drugi broj
dvostruko veći.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi razlike između opisne i uzročne
tvrdnje te poglavlju o veličini učinka i snazi radi najmanjega važnog učinka. U
agregiranoj tablici `data/populacija-medija-agregat.csv` pronađite retke za TV
i društvene mreže.
Prije računanja zapišite najmanju razliku na ljestvici od 0 do 10 koju biste
smatrali sadržajno važnom. Izračunajte populacijsku razliku iz stupaca
`zbroj_povjerenja` i `broj`, usporedite je sa svojim pragom i objasnite zašto
rezultat ne dokazuje da odabir izvora uzrokuje povjerenje.

### Revizija modela

Ocijenite sumnjivi kod iz okvira. Imenujte jedinu pogrešku, odredite koju stopu
pogreške ugrožava i razdvojite fatalni prigovor od dijelova artefakta koji su
još korisni. Ne pokrećite kod i ne pišite njegovu zamjenu.

---

# Regresija — opći okvir

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 32 min | Regresijski pravac | simulirana populacija | pogl. 2, 5, 6, 9 i 13–15 |

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
poglavlja o zaključivanju (Šikić, 2026). Povjerenje u medije mjereno je na
ljestvici od jedan do deset, a zanima nas kako se ono mijenja s dobi. Poglavlje
o povezanosti dalo bi na to pitanje jedan broj o jačini veze. Linearni model
umjesto toga daje modelom predviđeni linearni sažetak povjerenja za svaku dob.

Procjenjivana veličina, odnosno količina koju analiza cilja, jest broj koji
najbolje linearno sažima tih pedeset tisuća zabilježenih odgovora. Budući da su
obuhvaćene sve jedinice ove fiksne nastavne populacije, nema pogreške uzorkovanja
ni intervala koji bi je trebao izraziti. Brojevi iz generatora opisuju latentno
pravilo prije zaokruživanja i rezanja ljestvice. Oni nisu procjenjivana veličina
ove analize.

**Podsjetnik.** Nagib

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata izračunatim na svih pedeset tisuća pojedinačnih odgovora.*

Pravac na slici nije nacrtan kroz sredinu oblaka po oku. Bira ga pravilo koje
za svaku moguću kombinaciju odsječka i nagiba gleda koliko svako pojedino
opažanje promašuje, i uzima onu kombinaciju kojoj ti promašaji zajedno najmanje
teže.

**Rezidual** je razlika između opažene vrijednosti ishoda kod pojedine jedinice
i vrijednosti koju za nju predviđa model, dakle onaj dio ishoda koji model nije
objasnio.

Rezidual $i$-te jedinice označavamo $e_i$, njezinu opaženu vrijednost $y_i$, a
vrijednost koju model predviđa $\hat{y}_i$; kapica označava procjenu.

$$e_i = y_i - \hat{y}_i$$

Zbroj samih reziduala nije upotrebljiv kao mjera promašaja, jer se pozitivna i
negativna odstupanja poništavaju, pa bi loš pravac mogao izgledati savršeno.
Kvadriranje uklanja predznak i istodobno velika odstupanja košta više nego mala,
što je razlog zbog kojeg jedno jako promašeno opažanje pomiče pravac osjetnije
od deset blago promašenih.

**Metoda najmanjih kvadrata** bira koeficijente modela tako da zbroj kvadriranih
reziduala bude najmanji mogući za zadane podatke.

U ovoj je analizi procjenjivana veličina konačnopopulacijski koeficijent
najmanjih kvadrata. Model koji taj postupak daje ima oblik koji su poglavlja o
dvjema i o više skupina već koristila. Opaženi ishod $y_i$ rastavljamo na
modelom predviđenu vrijednost koju čine odsječak $\beta_0$ i nagib $\beta_1$
pomnožen s prediktorom $x_i$, te na odstupanje pojedine jedinice
$\varepsilon_i$.

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

Taj se oblik s jednim brojčanim prediktorom naziva **jednostavna linearna
regresija**.

Odsječak $\beta_0$ ostaje modelom sažeta vrijednost ishoda kada prediktor ima
vrijednost nula. U ovoj analizi $\beta_0$ i $\beta_1$ označavaju koeficijente
najmanjih kvadrata za cijelu fiksnu populaciju, dok je rezidual $e_i$ opaženo
odstupanje pojedine jedinice. Da je pred nama uzorak, kapice bi označavale
procjene tih ciljnih koeficijenata i uz njih bi trebalo prikazati uzoračnu
nesigurnost. Razlika prema poglavlju o dvjema grupama jedino je u tome što $x_i$
sada nije oznaka skupine nego izmjeren broj.

Konačnopopulacijski nagib iznosi `r hr_broj(s16$nagib_jedan, 4)`. Deset godina
dobi u ovoj populaciji povezano je s razlikom od
`r hr_broj(10 * s16$nagib_jedan, 2)` boda povjerenja. Odsječak od
`r hr_broj(s16$presjek_jedan, 2)` boda odnosio bi se na osobu od nula godina,
koje u podacima nema, pa je računski potreban i sadržajno prazan. Kad se
prediktor prije procjene umanji za svoju sredinu, odsječak postane modelom
predviđeni ishod kod osobe prosječne dobi, a nagib se ne promijeni. Isti model
tada ima jedan broj manje bez značenja.

Pravac je pritom linearno sažeta tvrdnja o prosjecima, a ne o pojedincima. Točke
na slici su prosjeci nekoliko stotina ljudi po godini dobi i u ovom skupu leže
blizu pravca, dok pojedinačni odgovori odstupaju od njega za nekoliko bodova u
oba smjera. Rečenica da model za osobe od pedeset godina predviđa viši prosjek
nego za osobe od trideset opisuje linearni sažetak i ne dopušta zaključak o
konkretnoj osobi bilo koje dobi.

## Nagib koji nosi tuđu priču

Konačnopopulacijski nagib za zabilježeno povjerenje iznosi
`r hr_broj(s16$nagib_jedan, 4)` boda po godini. To je ciljna veličina ove
analize, izračunata bez pogreške uzorkovanja. Generator je prije zaokruživanja i
rezanja ishoda koristio latentni nagib od `r hr_broj(s16$latentno_dob, 3)`.
Razlika među tim brojevima nije pogreška procjene, jer oni opisuju različite
veličine. Latentni broj služi samo za pregled mehanizma kojim je nastao
zabilježeni ishod.

Razlog je u drugoj varijabli koja se mijenja zajedno s dobi. Generator najprije
stvara dob, zatim prema njoj raspoređuje izvor vijesti, pa prosječna dob ide od
`r hr_broj(s16$dob_mreze, 1)` godine među onima koji se informiraju preko
društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među slušateljima radija.
Kako povjerenje ovisi i o izvoru, a stariji ljudi biraju izvore uz koje ide više
povjerenja, nagib uz dob pokupi i tu razliku i pripiše je godinama.

Tvrdnja se može provjeriti bez ijednog novog pojma. U ovom poznatom generatoru
isti latentni dobni nagib vrijedi po svim izvorima, pa očekujemo manje nagibe
unutar skupina ljudi koji se informiraju iz istoga izvora, gdje se izvor više
ne mijenja zajedno s dobi.

*Slika. Nagib uz dob izračunat zasebno među korisnicima svakog izvora vijesti, uz zbirni konačnopopulacijski nagib i latentno pravilo prije mjerenja. Izrada autora.*

Nijedna od pet skupina nema nagib blizu zbirnoga. Skupni nagibi kreću se između
`r hr_broj(s16$nagib_unutar_min, 4)` i `r hr_broj(s16$nagib_unutar_max, 4)`, dok
je zbirni nagib veći od svakoga od njih. Njihova blizina latentnom pravilu
korisna je provjera generatora, ali ih ne pretvara u procjene toga pravila.
Ista pojava kojoj je poglavlje o povezanosti dalo ime pri usporedbi
koeficijenata unutar i između skupina ovdje se pojavljuje u modelu i pokazuje
da razlika ne dolazi iz pogreške procjene nego iz toga što se pita.

To nije konfundiranje u strogom uzročnom smislu. Izvor u poznatom generatoru
nastaje nakon dobi i prije povjerenja, pa je nalik posredniku na putu od dobi
prema ishodu. Zbirni koeficijent opisuje ukupni dobni obrazac u populaciji, a
koeficijent uz jednak izvor opisuje drugi, uvjetni obrazac koji taj put zatvara.
Nijedan ne govori koliko bi se povjerenje promijenilo kod iste osobe koja stari.

Ta razlika nema veze s količinom podataka. Model obuhvaća svih pedeset tisuća
ljudi, pa je ciljna konačnopopulacijska vrijednost poznata i nema uzoračne
nesigurnosti. Kad bi se iz te populacije izvukao uzorak, trebalo bi procijeniti
isti cilj i prikazati nesigurnost koja odgovara nacrtu uzorkovanja. Ni tada
interval ne bi mjerio udaljenost od latentnog pravila prije mjerenja.

## Prilagodba i ono što je čini mogućom

Ako opažena povezanost miješa dvije priče, model može zadati usporedbu pri
jednakoj vrijednosti druge varijable. Umjesto rezanja uzorka na skupine iste
dobi i istog izvora, sve koeficijente procjenjuje odjednom.

**Višestruka regresija** procjenjuje modelnu povezanost svakog prediktora s
ishodom pri zadanim jednakim vrijednostima svih ostalih prediktora u modelu.
Koeficijent je uvjetna usporedba koju zadaje model; kao usporedba podataka
obranjiv je samo ondje gdje postoji dovoljno potpore i preklapanja, pa ne mora
označavati stvarno uparene jedinice.

Model s dobi i izvorom vijesti daje uz dob nagib od
`r hr_broj(s16$nagib_dva, 4)`. To je konačnopopulacijski odgovor na prilagođeno
pitanje, a ne procjena latentnog pravila. Broj je blizak latentnom pravilu od
`r hr_broj(s16$latentno_dob, 3)`, što je zasebna provjera poznatog generatora,
ali ta blizina ne određuje je li koeficijent ispravan.

*Slika. Konačnopopulacijski koeficijenti izvora vijesti uz jednaku dob, uz latentna pravila prije mjerenja. Portal je referentna skupina. Izrada autora.*

Stupci namjerno ne nose ista imena. Latentna pravila pripadaju ishodu prije
bilježenja, a koeficijenti pripadaju zabilježenoj ljestvici od jedan do deset.
U ovom su skupu potonji brojevi blago manji jer su vrijednosti zaokružene i
odrezane na krajevima ljestvice. Latentni broj zato nije vrijednost koju model
zabilježenog ishoda mora dosegnuti.

Blizina dvaju stupaca nije potvrda postupka. Vidimo je jer poznajemo generator i
jer su obje varijable koje su sudjelovale u nastanku povjerenja izmjerene. Da
izvor vijesti nije zabilježen, koeficijent uz dob ostao bi na
`r hr_broj(s16$nagib_jedan, 4)` i ništa u ispisu ne bi upozorilo da taj broj
odgovara drugom, neprilagođenom pitanju.

Izraz „uz kontrolu" zato opisuje račun, a ne postupak. U pokusu randomizacija
čini dodjelu neovisnom o početnim obilježjima i uravnotežuje skupine u
očekivanju, premda u konkretnom uzorku ostaje moguća slučajna neravnoteža, a
provedba i osipanje mogu narušiti početnu usporedbu. Kontrola u modelu znači da
je zadana uvjetna usporedba pri jednakim vrijednostima uključenih varijabli.

Iz toga slijedi oblik rečenice koji svaki koeficijent zaslužuje. U području
podataka s dovoljnom potporom model za ljude deset godina starije, uz jednak
izvor vijesti, predviđa prosjek povjerenja viši za
`r hr_broj(10 * s16$nagib_dva, 2)` boda. Rečenica navodi jedinicu prediktora,
jedinicu ishoda i uvjet pod kojim usporedba vrijedi, i bez ijednog od ta tri
dijela koeficijent se ne može provjeriti. Ista se disciplina traži i od
kategorijskih koeficijenata, gdje uvjet uključuje referentnu skupinu.

Riječ „prilagodba” ipak ne govori treba li varijabla ući u model. To ovisi o
njezinu mjestu u pretpostavljenom slijedu događaja. Sljedeći dijagram uspoređuje
tri mjesta koja u ispisu mogu izgledati jednako, a traže različite odluke.

*Slika. Tri uloge treće varijable u uzročnom dijagramu. Prilagodba za zajednički uzrok može zatvoriti neuzročni put, prilagodba za posrednika mijenja cilj s ukupne na izravnu vezu, a prilagodba za kolider može otvoriti novu pristranost. Izrada autora.*

Zajednički uzrok prethodi i pretpostavljenoj izloženosti i ishodu, pa ga je
razumno razmotriti radi poštenije usporedbe. Posrednik nastaje nakon izloženosti;
njegovim uključivanjem više se ne procjenjuje ista ukupna veza nego veza koja
ne prolazi tim putem. Kolider je posljedica obiju varijabli. Uvjetovanje na
njega može povezati inače nepovezane uzroke i stvoriti pristranost. Zato u model
ne ulazi „sve što imamo”. Prvo se određuju vremenski redoslijed, mjerna kvaliteta
i uloga svake varijable, a tek zatim specifikacija modela.

Odsječak u takvom modelu ostaje formalno potreban i sadržajno još slabiji nego
prije, jer sada opisuje osobu od nula godina koja se informira putem portala.
Model se time ne kvari. Kvari se samo pokušaj da se svaki broj iz ispisa
protumači kao da nešto opisuje.

Postoji i slučaj u kojem prilagodba ne uspijeva iako su sve varijable izmjerene.
Kad dva prediktora nose gotovo istu informaciju, podaci ne sadrže usporedbe u
kojima se jedan mijenja, a drugi ne, pa se njihovi pojedinačni doprinosi ne mogu
razdvojiti i koeficijenti postaju osjetljivi na male promjene uzorka. Zbroj tih
prediktora model i dalje koristi jednako dobro, a pitanje o svakome od njih
zasebno u tim podacima nema odgovor.

## Interakcija i regresijski pravac

Višestruki model ne mora pretpostaviti da jedna povezanost vrijedi jednako za
sve. Interakcija dopušta da se nagib jednog prediktora promijeni s vrijednošću
drugoga. U unaprijed planiranoj usporedbi modifikator, kodiranje, kontrast i
postupak zaključivanja zapisani su prije pregleda rezultata, a očekivani smjer
dodaje se kada je hipoteza usmjerena. Naknadno uočena podskupina može biti
korisna za novo pitanje, ali ostaje istraživačka i traži neovisnu provjeru.

Simulirani prikaz namjerno daje skupini A nagib
`r hr_broj(s16$heterogenost_a, 1)`, a skupini B
`r hr_broj(s16$heterogenost_b, 1)`. Zbirni model ih sažima nagibom
`r hr_broj(s16$heterogenost_zbirno, 1)`, koji ne opisuje nijednu skupinu.
Sljedeće predviđene linije zato čuvaju heterogenost koju bi jedan prosječni
koeficijent sakrio.

*Slika. Predviđene vrijednosti u simuliranom primjeru s različitim skupnim nagibima. Deblja zbirna linija opisuje prosjek koji ne vrijedi ni za jednu skupinu. Izrada autora.*

Interakcija se tumači zajednički, preko skupnih nagiba ili predviđenih
vrijednosti, a ne kao izolirani redak ispisa. Prikaz također sprečava čestu
pogrešku u kojoj se značajnost unutar jedne skupine i neznačajnost unutar druge
proglašavaju dokazom njihove razlike. Pitanje o heterogenosti pripada izravnom
testu interakcije i njegovoj nesigurnosti (Nieuwenhuis, 2011). Ovaj
deterministički prikaz demonstrira oblik, ne snagu dokaza; u stvarnim podacima
uz skupne se nagibe izvještava i interval za interakciju.

Sljedeći prikaz razdvaja dvije stvari koje su u prethodna tri odjeljka
ispisane kao gotov rezultat. U digitalnom izdanju čitatelj pomiče pravac i
uključuje treću varijablu, dok tiskani blizanac uspoređuje unaprijed zadani
kandidat s minimumom i prilagođenim pravcem. Podaci su manji i posebno
konstruirani za ovaj prikaz, kako bi se pojedini reziduali mogli vidjeti.

*Slika. Regresijski pravac — pomični pravac, reziduali i usporedba zbirnog s prilagođenim nagibom.*

**Što isprobati.**

1. Mijenjajte odsječak i nagib dok se zbroj kvadrata ne približi prikazanom
   minimumu.
2. Povećajte samo nagib za jednu jedinicu i pratite koji se reziduali najviše
   produljuju.
3. Uključite model s prethodnim interesom i usporedite njegov nagib sa zbirnim
   pravcem.

Zbroj kvadrata oko svojeg minimuma reagira sporo, pa se pravac može osjetno
pomaknuti prije nego što se brojka vidljivo pokvari. Kad podaci dolaze iz
uzorka, ta je geometrija jedan dio računanja intervala za odabranu ciljnu
veličinu. Widget sam ne daje zaključak o uzoračnoj nesigurnosti.

Prije nastavka zastanemo bez vraćanja tekstu. Koju veličinu analiza procjenjuje?
Što rezidual mjeri? O čemu ovisi uzročni doseg koeficijenta? Koji kriterij bira
pravac najmanjih kvadrata?

## Isti model iza ranijih poglavlja

Razlika dviju sredina može se zapisati kao koeficijent binarnog prediktora, a
usporedba više skupina kao niz koeficijenata prema referentnoj skupini. Brojčani
prediktor zatvara popis slučajeva. Vrijedi provjeriti da to nije samo tvrdnja o
zapisu.

Uzorak od sto dvadeset ljudi iz poglavlja o dvjema grupama daje razliku sredina
od `r hr_broj(s16$razlika_dvije, 2)` boda. Koeficijent uz izvor u modelu iznosi
`r hr_broj(s16$koef_dvije, 2)`. To je točna jednakost dvaju načina zapisivanja
iste točkaste procjene.

Omjer koeficijenta i obične homoskedastične standardne pogreške iznosi
`r hr_broj(s16$t_dvije, 2)`. Jednak je združenom Studentovu t-testu, koji u kodu
izričito postavlja `var.equal = TRUE`, pa oba računa pretpostavljaju jednu
zajedničku rezidualnu varijancu i imaju
`r hr_broj(s16$df_student_dvije, 0)` stupnjeva slobode. Welchov zadani postupak
iz poglavlja o dvjema grupama dopušta različite varijance. Na istim podacima
daje t od `r hr_broj(s16$t_welch_dvije, 2)` i
`r hr_broj(s16$df_welch_dvije, 3)` stupnja slobode. Točkasta procjena ostaje
ista, ali inferencija nije isti račun.

Uzorak od tristo ljudi iz poglavlja o više skupina daje ukupni test s
F-vrijednošću `r hr_broj(s16$f_pet, 2)` uz `r s16$df1_pet` i `r s16$df2_pet`
stupnja slobode. To je klasična homoskedastična analiza s jednom rezidualnom
varijancom, ista kao prikazani `aov` u poglavlju o više skupina. Welchov račun
na istim podacima daje F od `r hr_broj(s16$f_welch_pet, 2)` uz
`r hr_broj(s16$df1_welch_pet, 0)` i
`r hr_broj(s16$df2_welch_pet, 1)` stupnjeva slobode. Zajednički model sredina ne
pretvara ta dva postupka računanja nesigurnosti u isti test. Udio objašnjene
varijabilnosti u klasičnom modelu iznosi
`r hr_broj(100 * s16$r2_pet, 1)` %, a to je ista brojka koju je poglavlje o više
skupina nazvalo eta-kvadratom.

Iz toga slijedi praktična posljedica za čitanje tuđih radova. Rad koji
izvještava o t-testu, rad koji izvještava o analizi varijance i rad koji
izvještava o regresiji mogu polaziti od zajedničkog modela sredina, pa se čitaju
istim pitanjima o jedinici analize, o tome što je uspoređeno i uz što je
usporedba provedena. Zatim se zasebno provjerava kako je izračunata nesigurnost
i je li pretpostavljena zajednička ili skupinama svojstvena varijanca.

Ista posljedica vrijedi i za odabir postupka. Tablica koja vodi od vrste
podataka i pitanja do metode, kakva stoji u dodatku o odabiru testa, pomaže dok
se uči, a njezini redovi često polaze od različitih oblika zajedničkog modela.
Pitanja koja ostaju jesu što je ishod, što su prediktori, jesu li jedinice
neovisne i kako treba prikazati nesigurnost. Sam oblik modela ne odlučuje između
Welchove i obične homoskedastične inferencije.

Ako ista osoba daje više redaka ili su osobe ugniježđene u razrede, ustanove ili
gradove, prvo treba ponovno odrediti jedinicu i procjenjivanu veličinu. Osobe s
više redaka inače dobivaju veću težinu, a obična nesigurnost nema opravdanje
neovisnih jedinica. Tu treba stati, imenovati vezu među redcima i odabrati
postupak koji je čuva. Ovo poglavlje takav problem prepoznaje i usmjerava dalje,
ali ne procjenjuje modele za ovisne podatke.

## Pristajanje i njegove granice

Koliko dobro model opisuje podatke mjeri se udjelom varijabilnosti ishoda koji
je model uspio objasniti. Ta mjera nosi ime koje obećava više nego što daje, pa
je vrijedi definirati oprezno.

**Koeficijent determinacije** je udio ukupne varijabilnosti ishoda u promatranom
skupu podataka koji je model objasnio, izračunat kao jedan minus omjer zbroja
kvadrata reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

Označavamo ga $R^2$; $e_i$ je rezidual, $y_i$ opaženi ishod, a $\bar{y}$
zajednička sredina ishoda.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Model samo s dobi objašnjava `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti
povjerenja, a model s dobi i izvorom `r hr_broj(100 * s16$r2_dva, 1)` %. Obje su
brojke male, ali sama niska vrijednost ne razlikuje raznolikost ljudi od mjerne
pogreške ili neprimjerenog oblika modela. Model s izvorom istodobno opisuje
prilagođeni odnos u ovoj konačnoj populaciji i leži blizu latentnoga pravila
generatora. Te dvije veličine ipak nisu iste.

Vrijednost ima i mehaničko svojstvo koje je čini nedostatnom za izbor modela.
Na istim redcima i istom ishodu nikada ne pada kad se doda prediktor, pa i onaj
koji s ishodom nema nikakve veze podigne ju za nešto. U uzorku od dvjesto osoba
dodavanje pet potpuno slučajnih brojeva podiže udio objašnjene varijabilnosti s
`r hr_broj(100 * s16$r2_bez, 1)` % na `r hr_broj(100 * s16$r2_sa, 1)` %, dok
prilagođeni koeficijent determinacije, koji kažnjava svaki dodani prediktor,
pada s `r hr_broj(100 * s16$prilagodeni_bez, 1)` % na
`r hr_broj(100 * s16$prilagodeni_sa, 1)` %. Prilagođena inačica ublažava
automatski rast, ali ostaje heuristika. Ni ona sama ne presuđuje o predviđanju,
uzroku ili sadržajnoj valjanosti.

Postoji i druga strana iste mehanike, po kojoj vrijednost pada iako se odnos ne
mijenja. Ograničimo li populaciju na ljude između trideset i pedeset godina,
nagib uz dob ostaje `r hr_broj(s16$nagib_usko, 4)`, praktički kao prije, a udio
objašnjene varijabilnosti pada s `r hr_broj(100 * s16$r2_jedan, 1)` % na
`r hr_broj(100 * s16$r2_usko, 1)` % u skupu od
`r hr_broj(s16$n_usko, 0)` ljudi.
Ograničenje raspona iz poglavlja o povezanosti radi i ovdje. Koeficijent
determinacije nije stabilno svojstvo odnosa neovisno o populaciji i rasponu
podataka.

Zbog toga usporedba te mjere među različitim populacijama ili rasponima često
ne odgovara na korisno pitanje. Istraživanje na cijeloj populaciji i istraživanje
na uskoj dobnoj skupini mogu naći sličan nagib i izvijestiti o vrijednostima koje
se razlikuju šest puta. Ni koeficijenti nisu automatski usporedivi. Traže isti
ishod i ljestvicu, usporedivu populaciju, kodiranje i skup prilagodbi, a uz
uzorak i interval koji odgovara nacrtu.

Isti svakodnevni naziv također može sakriti različit nacrt. U lokalnoj
simuliranoj populaciji „medijska aktivnost” znači dnevne minute zabilježene za
osobu u konačnom skupu odraslih (Šikić, 2026). DigiKat bilježi objave vidljive
platformi koje zadovoljavaju pravila korpusa, s jedinicom objave ili agregata i
populacijom obuhvaćenog medijskog sadržaja (Šikić, 2026). Nevidljivo privatno
ponašanje u prvom i sadržaj izvan praćenog korpusa u drugom slučaju ostaju izvan
analize. Zato se regresija osobne uporabe ne može protumačiti kao regresija
platformskih objava niti se skupni trag smije pripisati pojedincu. Zajednički
naziv ne stvara isti konstrukt, jedinicu, populaciju ni granicu vidljivosti.

Pristajanje pritom ništa ne govori o tome gdje model griješi, a to se vidi tek
kad se reziduali pogledaju nasuprot vrijednostima koje model predviđa. Vrijeme
provedeno uz medije u ovoj populaciji raste s dobi za
`r hr_broj(s16$nagib_minute, 2)` minute po godini, i taj je pravac sasvim
razuman, ali njegovi reziduali nisu jednako raspršeni po cijelom rasponu.

*Slika. Reziduali modela za dnevno vrijeme uz medije nasuprot vrijednostima koje model predviđa, na slučajnom podskupu od dvije tisuće osoba.*

Raspršenost reziduala raste s `r hr_broj(s16$rasprsenost_dolje, 0)` na
`r hr_broj(s16$rasprsenost_gore, 0)` minuta, od šestine s najnižim do šestine s
najvišim predviđanjima. Agregatna rezidualna raspršenost zato ne opisuje uvjetnu
predikcijsku pogrešku u svakom dijelu raspona. Kad bi podaci bili uzorak,
inferencija bi morala dopustiti promjenjivu varijancu. Prikaz reziduala kaže gdje
model ne pristaje, a ne što s tim učiniti, i ta razlika između nalaza i odluke
ostaje na istraživaču.

Bayesovski pristup može istu strukturu modela dopuniti prethodnim raspodjelama i
vratiti raspodjelu nesigurnosti za koeficijente ili predviđene vrijednosti.
Time se mijenja način izražavanja nesigurnosti, ali se ne popravljaju pogrešna
mjera, ovisne jedinice, curenje informacija ni neopravdana uzročna pretpostavka.
Ovdje taj pogled ostaje kratka najava, a ne drugi sustav zaključivanja.

## Objašnjenje i predviđanje

Dva zadatka koja ista jednadžba obavlja razlikuju se po tome što od modela
traže. Objašnjenje traži sadržajno određenu i protumačivu povezanost, dok
predviđanje traži malu pogrešku na jedinicama koje model nije vidio. Uzročno
objašnjenje dodatno traži prikladan dizajn i identifikacijske pretpostavke.
Shmueli je pokazala da se ta dva cilja razilaze već u izboru varijabli i mjera,
pa model koji je bolji za jedno može biti lošiji za drugo (Shmueli, 2010).

Prediktivni primjeri u ovom odjeljku imaju istu vremensku granicu. Povjerenje
treba predvidjeti za novu osobu neposredno prije nego što ona odgovori na pitanje
o povjerenju. Dob i izvor vijesti tada su dostupni. Umjetni slučajni stupci u
primjeru prekomjernog pristajanja također su zapisani prije te granice i postoje
u istom obliku za skup učenja i odvojeni skup, premda ne nose korisnu
informaciju. Sve što nastaje nakon odgovora o povjerenju isključeno je.

Razilaženje počinje već kod izbora varijabli. Spremnost na plaćanje vijesti u
ovoj populaciji nastaje pod utjecajem povjerenja, dakle nakon ishoda koji se
modelira. Kao prediktor povjerenja ipak radi, jer podiže udio objašnjene
varijabilnosti s `r hr_broj(100 * s16$r2_dva, 1)` % na
`r hr_broj(100 * s16$r2_posljedica, 1)` % i smanjuje preostalu raspršenost. Za
odabranu vremensku granicu to nije prediktivni dobitak nego curenje informacija.
Spremnost na plaćanje još ne postoji kad predviđanje treba nastati, pa takav
model ne bi mogao proizvesti valjano predviđanje za novu osobu.

Razlika se dalje ne vidi dok se model ocjenjuje na podacima na kojima je
procijenjen. Predviđanje izvan uzorka provjerava se na skupu odvojenom prije
postavljanja modela. Takva je provjera ovdje interna i vrijedi za isti
simulirani mehanizam; sama ne dokazuje prijenos u drugo vrijeme, sustav ili
populaciju. Oba modela u tablici koriste samo prediktore dostupne do iste
vremenske granice.

*Slika. Prosječna pogreška predviđanja dvaju modela na podacima na kojima su procijenjeni i na odvojenom skupu, u bodovima povjerenja. Izrada autora.*

Na skupu za učenje od `r s16$n_ucenje` osoba bogatiji model objašnjava
`r hr_broj(100 * s16$r2_bogat, 1)` % varijabilnosti, prema
`r hr_broj(100 * s16$r2_skroman, 1)` % kod skromnijeg. Na tim podacima griješi
manje, ali na `r s16$n_provjera` osoba koje nije vidio griješi više od
skromnijeg modela i više nego postupak koji svakome pripiše prosjek skupa za
učenje. Model je naučio raspored slučajnih brojeva u svojem uzorku i taj raspored
u novim podacima ne postoji.

Skromniji model pritom je bolji od bogatijega na ovom odvojenom skupu.
Povjerenje se u populaciji raspršuje sa standardnom devijacijom
`r hr_broj(s16$sd_ishoda, 2)` boda, a nakon što model uzme u obzir dob i izvor
ostaje rezidualna raspršenost od `r hr_broj(s16$sd_ostatka, 2)`. Dio te
raspršenosti dolazi od slučajne sastavnice generatora, a dio može pripadati
nepotpunom obliku modela. Zato sama rezidualna standardna devijacija nije
dokazana donja granica pogreške nekog boljeg prediktivnog postupka.

Tvrdnja o predviđanju stoga se provjerava na podacima koji u procjeni nisu
sudjelovali i smije koristiti samo
informacije dostupne u trenutku primjene. Prvi uvjet sprječava da model ocjenjuje
sam sebe, a drugi curenje informacija iz budućnosti. Poglavlje o algoritmima na toj
razlici gradi cijeli argument, budući da postupci koji odlučuju o kreditima,
sadržaju i rangiranju svoju vrijednost mjere uspješnošću na jedinicama koje još
nisu viđene.

## Granica prema uzroku

Konfundirajuća varijabla prethodi i pretpostavljenom uzroku i ishodu. Regresija
može izračunati uvjetnu usporedbu uz takvu varijablu, ali njezinu ulogu ne može
otkriti iz ispisa. Za to su potrebni sadržajno znanje, vremenski redoslijed i
dizajn istraživanja.

U poznatom generatoru izvor vijesti ne igra tu ulogu. Nastaje nakon dobi i prije
povjerenja, pa prilagodba za izvor zatvara mogući posrednički put i mijenja
procjenjivanu veličinu sa zbirnog na uvjetni dobni obrazac. Prilagođeni se
koeficijent približava latentnom izravnom pravilu zato što poznajemo način
nastanka podataka. To slaganje nije dokaz da bi isti postupak u stvarnom
istraživanju otkrio učinak.

Prilagođena povezanost zato nije sama po sebi uzročni učinak. Vremenski red,
izostanak neizmjerenih zajedničkih uzroka i izbjegavanje prilagodbe za posljedice
pretpostavljenog uzroka jesu važni, ali nisu dovoljni uvjeti. Uzročna
identifikacija traži i valjano mjerenje, dovoljno preklapanja usporedivih
jedinica, dobro definiranu intervenciju, zaštitu od selekcijske pristranosti i
primjeren oblik modela. Ovo poglavlje te uvjete imenuje, ali njima ne uspostavlja
uzročnu identifikaciju.

Dob dodatno nema jednostavno intervencijsko tumačenje. U stvarnom istraživanju
o vremenskom redu, ulozi izvora i opravdanosti svake usporedbe raspravljalo bi
se prije računanja, a nijedan modelni ispis ne bi potvrdio da su pretpostavke
zadovoljene.

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
**Od omjera do dopuštene rečenice.** Kad je ishod binaran, vjerojatnost je udio
usporedivih jedinica s ishodom 1. Označimo li tu vjerojatnost s $p$, izgledi su
omjer $p$ i njegove nadopune, $p/(1-p)$. Omjer izgleda uspoređuje izglede dviju
skupina; omjer rizika uspoređuje njihove vjerojatnosti. Omjer izgleda zato ne
znači promjenu u postotnim bodovima i ne smije se preimenovati u omjer rizika.
Ako 20 od 100 ljudi ima ishod, vjerojatnost je 0,20, a izgledi su 20 prema 80,
odnosno 0,25.

Kategorijski prediktor čita se prema referentnoj skupini, čiji je omjer izgleda
jedan. Vrijednost iznad jedan znači veće izglede od referentnih, a vrijednost
ispod jedan manje. Interval od 95 % koji obuhvaća vrijednost jedan spojiv je i s
jednakim izgledima. Predviđena vjerojatnost zahtijeva cijelu
specifikaciju, odsječak i vrijednosti ostalih prediktora, pa se ne može obnoviti
iz izdvojenog omjera izgleda kad ti dijelovi nisu objavljeni. Ovdje učimo samo
čitati ishod, referentnu skupinu, omjer i interval; procjenjivanje logističkog
modela, njegova jednadžba i dijagnostika ostaju izvan opsega knjige.

Kleppang i suradnici analizirali su
samoprijavljene presječne podatke istraživanja Ungdata iz 2018. za 12.353
norveških adolescenata u dobi od 15 do 16 godina, uz ukupni odaziv od 85 %
(Kleppang, 2021). Presječni nacrt ne određuje vremenski smjer i ne podupire
uzročnu tvrdnju.

| Prediktor i kategorija | Model 1, društvene mreže AOR (95 % interval) | Model 2, igranje AOR (95 % interval) | Model 3, oba prediktora AOR (95 % interval) |
|---|---:|---:|---:|
| Društvene mreže, do 3 sata | 1 (ref.) | nije u modelu | 1 (ref.) |
| Društvene mreže, više od 3 sata | 1,60 (1,43–1,80) | nije u modelu | 1,51 (1,34–1,70) |
| Igranje, do 3 sata | nije u modelu | 1 (ref.) | 1 (ref.) |
| Igranje, više od 3 sata | nije u modelu | 1,57 (1,36–1,80) | 1,38 (1,19–1,59) |

: Prilagođeni omjeri izgleda za simptome depresije prema uporabi društvenih mreža i igranju. Sadržajno skraćena, preoblikovana i na hrvatski prevedena prilagodba Tablice 3 iz rada Kleppang i suradnika (Kleppang, 2021).

Ishod je kodiran kao simptomi depresije na ili iznad 80. percentila nasuprot
vrijednosti ispod 80. percentila. AOR označava omjer izgleda prilagođen za rod ili
spol, imanje prijatelja, pušenje, visoko obrazovanje roditelja i obiteljsko
materijalno stanje. Stupac Model 1 sadrži društvene mreže, Model 2 igranje, a
Model 3 oba prediktora uz isti navedeni skup prilagodbi (Kleppang, 2021).

Izvor su Annette Løvheim Kleppang, Anne Mari Steigen, Li Ma, Hanne Søberg
Finbråten i Curt Hagquist, „Electronic media use and symptoms of depression
among adolescents in Norway”, *PLOS ONE* 16(7), e0254197, 2021,
članak (https://doi.org/10.1371/journal.pone.0254197) i
izvorna Tablica 3 (https://doi.org/10.1371/journal.pone.0254197.t003)
(Kleppang, 2021). Izvor je pod licencom
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Ovdje su odabrani
redci i tri modelna stupca preoblikovani, skraćeni i prevedeni na hrvatski;
brojčane vrijednosti i granice intervala nisu promijenjene. Prilagodba ne
podrazumijeva odobrenje autora ni PLOS-a.

U prilagođenom i skraćenom prijevodu prvog odlomka rezultata tablica prikazuje
omjere izgleda za simptome depresije prema uporabi društvenih mreža u prvom
stupcu, igranju u drugom te objema varijablama u trećem, nakon prilagodbe za
navedene čimbenike. U modelu prilagođenom za rod ili spol, imanje prijatelja,
pušenje, visoko obrazovanje roditelja i obiteljsko materijalno stanje,
adolescenti koji društvene mreže rabe više od tri sata na dan imali su 1,60
puta onolike izglede da budu na ili iznad 80. percentila simptoma kao oni koji
ih rabe do tri sata (AOR 1,60; 95 % interval 1,43–1,80) (Kleppang, 2021).

Prva rečenica prijevoda oslanja se na naslove triju stupaca i bilješku o
prilagodbama. Druga se oslanja na ćeliju 1,60 s intervalom od 1,43 do 1,80 u
Modelu 1 i na referentni redak iznad nje. Ni ta ćelija ni cijela tablica ne daju
apsolutne vjerojatnosti, omjere rizika ili predviđene vjerojatnosti. Ne daju ni
presjek modela potreban za njihov izračun (Kleppang, 2021).

Izvadak namjerno ne prikazuje modelno specifične nazivnike, odsječak, mjere
pristajanja, dijagnostiku, p-vrijednosti ni zvjezdice. Intervali nose
nesigurnost, ali bez tih elemenata nije moguće provjeriti gubitak redaka,
usporediti pristajanje modela ili obnoviti apsolutni rizik. Koeficijenti
prilagodbenih varijabli također ne bi automatski bili njihovi učinci, jer je
njihova uzročna uloga drugačija za svako pitanje (Westreich, 2013). Samoprijava,
neizmjereni čimbenici i presječni nacrt dodatno ograničavaju zaključak
(Kleppang, 2021).

**Pitajte model.**
Asistent može prilagoditi model, izraditi dijagnostičke prikaze i prevesti
koeficijente u prozu. Prije poziva treba mu zadati ulogu svake varijable,
referentne kategorije, procjenjivanu veličinu i cilj analize, jer različite
specifikacije odgovaraju opisnom, prediktivnom ili uzročnom pitanju. Za
prediktivni cilj treba zadati i trenutak primjene.

U odgovoru se provjerava tumači li koeficijent u izvornim jedinicama i uz uvjet
ostalih varijabli, umjesto kao učinak, te bira li prilagodbe prema pitanju, a ne
prema tome što je pri ruci. Predviđanje smije koristiti samo informacije
dostupne do trenutka primjene i mora se ocijeniti na podacima koji nisu
sudjelovali u procjeni.

> Prilagodi model i protumači koeficijent glavne varijable u izvornim
> jedinicama, s mjerom nesigurnosti koja odgovara ciljnoj veličini i nacrtu. Za
> svaku kontrolu napiši zašto je u modelu i može li biti posljedica glavne
> varijable.
> Imenuj trenutak predviđanja, isključi poslijeishodne podatke i predviđanje
> ocijeni na odvojenom skupu.

**Nađite grešku.**
Na traženje da procijeni koliko dobro model predviđa povjerenje kod novih
korisnika asistent je priložio ovaj račun. U zamišljenoj primjeni sve navedene
varijable zabilježene su prije odgovora o povjerenju, pa je vremenska granica
zadovoljena.

Uz ispis je napisao obrazloženje. Model objašnjava osjetno veći udio
varijabilnosti nego prethodni, a prosječna pogreška iznosi manje od dva boda
na ljestvici od jedan do deset. Iz toga zaključuje da model dovoljno pouzdano
predviđa povjerenje kod korisnika koje nije vidio i preporučuje ga za primjenu
na novim podacima.

## Razrađeni primjer

Pitanje je kako se povjerenje u medije mijenja s dobi, a analiza daje dva
odgovora ovisno o tome opisuje li se zbirni obrazac ili obrazac pri jednakom
izvoru. Ciljne su veličine u oba slučaja koeficijenti najmanjih kvadrata za
zabilježene odgovore svih pedeset tisuća ljudi.

Funkcija `lm` ovdje izračunava opisne koeficijente iz cijele konačne populacije.
Nijedna jedinica nije uzorkovana, pa uz te brojeve nema uzoračne nesigurnosti.
Funkcija `confint` zato se ne poziva. Njezin uobičajeni interval odnosio bi se na
drugi, modelni ili nadpopulacijski cilj koji ovo poglavlje nije odabralo.

*Slika. Konačnopopulacijski nagib uz dob u dvama modelima za zabilježeni ishod. Izrada autora.*

Razlika među nagibima nije stvar uzoračne nepreciznosti. Oba su poznata točno za
ovu populaciju, ali odgovaraju na različita pitanja. Zbirni nagib obuhvaća dobni
obrazac koji prolazi i kroz izbor izvora, a prilagođeni je modelna usporedba pri
jednakom izvoru i zatvara taj put. Izvještaj koji bi naveo samo prvi broj ne bi
sadržavao netočnu brojku i svejedno bi zamaglio razliku između pitanja.

Zaključak se zato piše u dva dijela. Zbirni model za deset godina veću dob
predviđa prosjek povjerenja viši za
`r hr_broj(10 * s16$nagib_jedan, 2)` boda. Pri jednakom izvoru model predviđa
razliku od `r hr_broj(10 * s16$nagib_dva, 2)` boda. Prva rečenica opisuje ukupni
linearni obrazac, druga uvjetni obrazac, i tek zajedno kažu što je model našao.

Uvjetni oblik izvještaja čuva granicu zaključka. Ako je cilj opisati ovu
simuliranu konačnu populaciju, navode se oba koeficijenta bez uzoračnog
intervala. Za širu populaciju iz uzorka isti bi koeficijenti trebali interval
koji odgovara nacrtu. Predviđanje nove osobe traži pogrešku na odvojenim
podacima i trenutak dostupnosti prediktora. Nijedan od tih oblika sam po sebi ne
podupire uzročnu rečenicu.

Izvještaj uz to mora reći što je izostavljeno. Model sadrži dvije varijable, dok
bi obrazovanje, iskustvo s pojedinim redakcijama ili političke sklonosti bili
mogući, ovdje neizmjereni čimbenici koje bi stvarno istraživanje moralo
razmotriti. Njihovo uključivanje moglo bi promijeniti ciljnu uvjetnu usporedbu i
njezinu veličinu.

Ostaje i pitanje na koje ova analiza uopće nije odgovarala. Nijedna od dviju
rečenica ne kaže da bi se povjerenje neke osobe promijenilo time što ona
ostari, ni da bi se promijenilo time što promijeni izvor vijesti. Analiza
opisuje kako izgleda populacija u jednom trenutku, a promjena kod iste osobe
kroz vrijeme zahtijeva podatke koji istu osobu prate, kojih ovdje nema.

## Sažetak

Linearni model povezuje ishod s prediktorima kroz modelom predviđene vrijednosti i
reziduale, a metoda najmanjih kvadrata bira koeficijente po jasnom kriteriju
koji se u widgetu može vidjeti kako radi. Više prediktora daje povezanosti pri
jednakim vrijednostima ostalih varijabli, dok interakcija dopušta različite
nagibe i traži zajedničko tumačenje predviđenih vrijednosti. Koeficijenti za
cijelu konačnu populaciju opisuju zabilježeni ishod bez uzoračne nesigurnosti i
nisu latentni parametri generatora; udio objašnjene varijabilnosti raste i kad
se doda čista buka, pa pristajanje samo ne ocjenjuje generalizaciju, dok
reziduali pokazuju gdje model ne odgovara podacima. Objašnjenje i predviđanje
odatle se razdvajaju, jer se drugo provjerava na jedinicama koje model nije
vidio i samo s informacijama dostupnima u trenutku primjene. Kod binarnog
ishoda omjer izgleda nije omjer rizika ni razlika vjerojatnosti, a referentna
skupina i interval sastavni su dijelovi čitanja; prilagođena povezanost nije
sama po sebi učinak, pa izvještaj mora imenovati procjenu, jedinice, populaciju,
nesigurnost i uzročni doseg koji dizajn podupire. Sljedeće poglavlje uzima
kriterij predviđanja ozbiljno i pita što se događa kad postupci koji ga
zadovoljavaju počnu odlučivati o ljudima.

## Pojmovi

linearna regresija (*linear regression*), procjenjivana veličina (*estimand*),
rezidual (*residual*), metoda najmanjih kvadrata (*least squares*), višestruka
regresija (*multiple regression*), prilagođena povezanost (*adjusted
association*), koeficijent determinacije (*R-squared*), interakcija
(*interaction*), curenje informacija (*information leakage*), predviđanje izvan
uzorka (*out-of-sample prediction*), izgledi (*odds*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto se nagib uz dob mijenja kada u model uđe izvor
vijesti, a nijedan podatak o dobi pritom nije promijenjen. Imenujte pitanje na
koje odgovara svaki od dvaju nagiba. Na prikazu interakcije zatim odredite koji
nagib opisuje skupinu A, koji skupinu B i zašto zbirni nagib ne opisuje nijednu.

### Računski

Zbirni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)` boda po godini. Izračunajte
modelom predviđenu razliku prosjeka između dobi od 25 i 55 godina, a zatim isti
račun ponovite s prilagođenim nagibom
`r hr_broj(s16$nagib_dva, 4)` uz jednak izvor vijesti. Predajte obje brojke i
objasnite zašto nijedna ne određuje ostvarenu razliku dviju konkretnih osoba.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi operacionalizacije i vremenskog
reda te poglavlju o tome kako brojke zavode radi razlike između točne brojke i
preširoke tvrdnje. Na prilagođenoj Tablici 3 iz okvira odredite što je mjereno,
koja je referentna skupina, koju količinu podupire ćelija 1,60 i koja bi dodatna
količina trebala za tvrdnju o apsolutnoj vjerojatnosti. Zatim preuredite naslov
„Više od tri sata na društvenim mrežama povećava depresiju za 60 %” u jednu
rečenicu koju presječni nacrt i prikazani omjer izgleda doista podupiru.

### Revizija modela

Ocijenite račun i zaključak iz okvira o pogrešci. Imenujte što je u kodu
ispravno, redak u kojem se pogreška događa, razlog zbog kojeg obje priložene
brojke izgledaju uvjerljivo i napišite zaključak koji bi isti ispis podnio.
Objasnite i zašto pogreška nije curenje informacija iz budućnosti u zadanoj
vremenskoj granici, nego pogrešna provjera na skupu za učenje.

---

# Statistika u doba algoritama

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| nije mjereno | Istraživač pravednosti | ParlaSent 1.0 i simulacija | obvezno kategorički podatci; dohvat mjerenja, zavaravajućih brojki, uzorkovanja, testiranja, veličine učinka i regresije |

**Vinjeta.**
„Da li je pošteno da se ukida prethodna stopa i da se povećava u odnosu na
prethodnu?” Prvi je to hrvatski redak nastavne datoteke ParlaSent 1.0. Jedan
ga je koder označio neutralnim uz negativan ton, drugi negativnim, a postupak
usklađenja zabilježio je oznaku `Negative` (Mochtak, 2023).

Zamislimo urednički sustav koji rečenice označene kao negativne šalje u red za
ljudski pregled prije mogućega javnog sažetka. Sustav ne briše tekst, ne
kažnjava govornika i ne objavljuje oznaku automatski. Ipak, odluka određuje
koje će rečenice dobiti dodatnu pozornost. Pogrešan ulazak može neopravdano
usmjeriti pozornost, a pogrešno izostavljanje može sakriti važan dio govora.

Veza između negativnoga tona i potrebe za pregledom osporiva je urednička
politika, a ne posljedica podataka. Treba je zasebno obrazložiti i usporediti s
neutralnom alternativom, primjerice slučajnom provjerom ili kriterijem javne
relevantnosti koji ne ovisi o sentimentu.

Treba li ova rečenica ući u red? Odgovor ne počinje izborom modela. Počinje
pitanjima što je jedinica, tko je mogao biti opažen, kako je oznaka nastala i
tko je može osporiti.

## Odluka, korpus i jedinica

Klasifikator može ponuditi predviđenu vjerojatnost da rečenica pripada
određenoj kategoriji. Institucija tek zatim određuje koja će vrijednost
pokrenuti ljudski pregled. Model proizvodi broj, prag ga pretvara u odluku, a
postupak odlučuje što se događa nakon te odluke.

Predviđanje i objašnjenje nisu dva naziva za isti cilj [Breiman, 2001;
Shmueli, 2010]. Model za predviđanje prosuđujemo prema ponašanju na podacima koje
nije rabio za učenje. Od objasnidbenoga modela tražimo odgovor na pitanje kako
su varijable povezane s ishodom i može li se ta povezanost braniti teorijom i
nacrtom. Uspješno predviđanje tona ne pokazuje što je govornik namjeravao niti
što je ton uzrokovalo.

U ovom je primjeru [tekstna jedinica]{.pojam
def="Jedan unaprijed određen komad teksta koji se zasebno označava i analizira."
en="text unit" ch="17"} jedna rečenica. Redak nije cijeli govor, osoba ni
parlamentarna sjednica. [Granica korpusa]{.pojam
def="Pravilo koje određuje koji tekstovi mogu ući u analizu, a koji ostaju izvan nje."
en="corpus boundary" ch="17"} obuhvaća samo retke koje je izvorna datoteka
ParlaSent označila s `country = HR`. Paket ne sadržava govornika, stranku,
datum, položaj vlasti ili oporbe ni vezu na cijeli govor.

Ta odsutnost nije prazno polje koje smijemo nadopuniti nagađanjem. Uzvodni je
odabir također selektivan. Izvorni su autori isključili rečenice moderatora i
zadržali samo rečenice duljine između prvoga i trećega kvartila
(Mochtak, 2024). Rečenice u
dijelu namijenjenom učenju zatim su stratificirano uzorkovane prema tome
sadrže li pozitivne, negativne ili nijednu riječ iz sentimentnih leksikona,
dok je ispitni dio odabran slučajno, bez oslanjanja na sentimentne leksikone,
ali pod istim ograničenjem duljine i moderatorskim filtrom
(Mochtak, 2023; Mochtak, 2024). Zato udio negativnih oznaka nije procjena udjela negativnoga
tona u Hrvatskome saboru. Nije dopušten ni prijelaz s rečenice na namjeru ili
osobinu govornika. Dobra analiza najprije imenuje što nije moglo ući u podatke,
a tek zatim opisuje ono što jest.

ParlaSent 1.0 donosi stvarne označene parlamentarne rečenice, a nastavna
prilagodba pod licencom CC BY-SA 4.0 zadržava samo retke s izvornom oznakom
zemlje `HR` (Mochtak, 2023). Paket ima 2.698 redaka, a svi su dokumenti
držani unutar jednoga izvedenog skupa.

Provjerni račun čita već pripremljenu datoteku i broji retke. Njegov je izlaz
tablica s brojnostima triju skupova; računsko zaleđe ostaje skriveno jer ovdje
čitatelju treba trag rezultata, a ne sintaksa uređivanja kategorija.

*Slika. Oznake i brojnosti u nastavnom paketu ParlaSent. Izrada autora prema @mochtak2023.*

Brojnosti opisuju paket, ne parlament. Skup za učenje ima 1.090 redaka, skup
za provjeru 272, a skup za ispitivanje 1.336. Svih 1.336 ispitnih redaka
zadržano je. U ovoj je prilagodbi iz izvornoga dijela za učenje uklonjeno 25
redaka iz 20 dokumenata koji su prelazili ispitnu granicu. Nijedan redak nije
uklonjen prema oznaci. Transformacijski trag s ulaznim i izlaznim kontrolnim
sumama te tim dvjema brojnostima nalazi se u podatkovnoj putovnici
`data/parlament_tekst/PUTOVNICA.md`.

## Nastanak oznake

[Okvir kodiranja]{.pojam
def="Skup pravila po kojima se tekst pretvara u kategorije koje analiza rabi."
en="coding frame" ch="17"} govori što riječi `Negative`, `Neutral` i `Positive`
trebaju značiti. Oznaka nije prirodno svojstvo retka koje čeka da ga otkrijemo.
Ona je rezultat uputa, osobe koja kodira i postupka rješavanja neslaganja.

Putovi nastanka oznake u paketu namjerno ostaju različiti. U dijelu izvorno
namijenjenom učenju dostupne su dvije pojedinačne oznake i usklađenje. U
izvornom ispitnom dijelu dostupna je jedna oznaka uvježbanoga kodera; drugi
koder i usklađenje nisu dostupni iz izvora. Učenje i ispitivanje zato nemaju
jednak postupak mjerenja, premda oba završavaju stupcem `recorded_label`.

**Zabilježeni referentni ishod** jest ishod ili oznaka zapisana određenim
postupkom mjerenja, prema kojoj se vrednuje klasifikator, ali koja može
sadržavati pogrešku.

Neslaganje kodera nije samo smetnja koju usklađenje briše. Ono otkriva mjesta
na kojima je konstrukt nejasan ili pravilo teško primjenjivo. Ako promijenimo
upute, kodere ili postupak usklađenja, možemo promijeniti zabilježeni
referentni ishod. Tada se mijenja i tablica prema kojoj ocjenjujemo model, čak
i ako su njegova predviđanja ostala ista.

## Tri skupa, dva pitanja

Puni naziv postupka glasi [razdvajanje na skup za učenje, provjeru i
ispitivanje]{.pojam
def="Odvajanje podataka za prilagodbu modela, izbor postupka i jednu završnu procjenu."
en="train-validation-test split" ch="17"}. Skup za učenje služi prilagodbi
modela, skup za provjeru izboru pravila i praga, a skup za ispitivanje čuva se
za jednu završnu procjenu nakon tih izbora. U ovom je paketu usporediva završna
procjena blokirana jer ispitni dio ima drukčiji
postupak odabira i drugi referentni postupak.

ParlaSentov nastavni paket dijeli cijele dokumente, ne pojedine rečenice.
Dokument koji se pojavio u izvornoj ispitnoj datoteci uklonjen je iz izvornoga
dijela za učenje, a preostali su dokumenti deterministički raspoređeni u
učenje i provjeru. Tako rečenice istoga dokumenta ne cure preko granice i ne
stvaraju privid provjere na novom tekstu.

[Preprilagodba]{.pojam
def="Učenje posebnosti viđenih podataka koje poboljšava pristajanje njima, ali pogoršava predviđanje novih jedinica."
en="overfitting" ch="17"} objašnjava zašto je odvajanje potrebno. Ono ipak ne
rješava pitanje uzorkovanja o dosegu populacije. U pravilno projektiranom
razdvajanju procjenjujemo ponašanje na izdvojenim jedinicama iz istoga
podatkovnog postupka, dok nacrt uzorkovanja određuje na koju populaciju smijemo
generalizirati. ParlaSentov se ispitni dio razlikuje i odabirom i putem oznake,
pa ovdje ne daje usporedivu završnu validaciju. Dobar ispitni rezultat ni u
idealnom slučaju ne pretvara odabrani korpus u reprezentativan uzorak.

## Od vjerojatnosti do pravednosti

Ako je prag za slanje u pregled 0,60, rečenica s predviđenom vjerojatnošću
0,59 ne ulazi u red, a ona s 0,61 ulazi. Razlika od dvije stotinke postaje
razlika u postupanju. Prag zato nije samo tehničko podešenje. Njegov izbor
govori koji je teret pogreške institucija spremna prihvatiti.

**Klasifikacijski prag** jest unaprijed određena vrijednost koja predviđenu
vjerojatnost pretvara u kategoričku odluku; njegovim se pomicanjem mijenja
odnos vrsta pogrešaka.

[Tablica zabune]{.pojam
def="Kontingencijska tablica koja križa klasifikacijsku odluku i zabilježeni referentni ishod."
en="confusion matrix" ch="17"} isti je tablični objekt koji smo u poglavlju o
kategoričkim podatcima čitali kao kontingencijsku tablicu. Ovdje redovi mogu
označivati zabilježeni referentni ishod, a stupci odluku o pregledu. Stopa lažno pozitivnih odluka ima
u nazivniku sve zabilježene nenegativne rečenice, dok stopa lažno negativnih
odluka polazi od svih zabilježenih negativnih rečenica. Pozitivna prediktivna
vrijednost zatim pita koliki udio među svim rečenicama poslanima u pregled ima
zabilježeni negativni ishod. Ukupna točnost ponderira uspjeh u dvjema uvjetnim
skupinama njihovim temeljnim stopama, pa može sakriti teret pojedine vrste
pogreške.

Temeljna stopa, uvedena u poglavlju o tome kako brojke zavode, ovdje određuje
koliko je zabilježeno negativnih ishoda prije odluke modela. Čak i kada dvije
skupine imaju jednake uvjetne stope lažno pozitivnih i lažno negativnih
odluka, različite temeljne stope mogu dati različitu pozitivnu prediktivnu
vrijednost. Poglavlja o testiranju i veličini učinka podsjećaju nas da isti
broj pogrešaka nije jednako važan kada su posljedice odluka različite. Zato se
više poželjnih mjerila pravednosti ne može uvijek izjednačiti istodobno
(Chouldechova, 2017; Barocas, 2023).

[Pogreške po podskupinama]{.pojam
def="Odvojeni prikaz vrsta pogreške unutar unaprijed smislenih skupina."
en="subgroup errors" ch="17"} imaju smisla samo ako paket doista sadržava
obranjivu skupnu varijablu. Nastavni paket ParlaSent takve podatke nema. Ne
smijemo iz imena, teksta ili nedostupnoga govornog konteksta izvesti skupine
koje datoteka nije isporučila. Widget zato rabi izmišljene skupine A i B, a
empirijski primjer ne glumi podskupinsku analizu.
Nemogućnost izračuna podskupinskih stopa nije dokaz da su pogreške pravedno
raspoređene; to je ograničenje onoga što paket može provjeriti.

[Algoritamska pravednost]{.pojam
def="Ocjena raspodjele koristi, pogrešaka i mogućnosti osporavanja u cijelom sustavu odluke."
en="algorithmic fairness" ch="17"} nije jedna stopa. Traži da zajedno čitamo
nazivnike, posljedice, obavijest, obrazloženje, prigovor i žalbu.

## Interakcija — Istraživač pravednosti

Istraživač pravednosti mijenja klasifikacijski prag za dvije skupine s
različitim temeljnim stopama, ali jednakom kvalitetom rezultata uvjetno na
zabilježeni referentni ishod. Skupine i brojke generira poznati simulacijski
mehanizam; one ne opisuju ParlaSent ni stvarne ljude. Prikaz pokazuje kako
zajednički prag može izjednačiti neke stope pogreške, a ipak proizvesti
različitu prediktivnu vrijednost i točnost.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

Widget drži uvjetne stope pogreške jednakima u objema skupinama jer za obje
rabi iste simulirane raspodjele rezultata. Kad su i temeljne stope jednake,
poklapaju se sva četiri mjerila. Kad se temeljne stope razdvoje, pozitivna
prediktivna vrijednost i točnost više se ne poklapaju. Time se vraćamo
posljedici različitih temeljnih stopa objašnjenoj u poglavlju o zavaravajućim
brojkama, a ne dokazujemo da je jedna skupina povlaštena u nekom stvarnom
sustavu.

## Osporiva oznaka i postupak

Vratimo se početnoj rečenici. Postupkom usklađenja rečenica je označena
negativnom, ali prvi je koder odabrao neutralnu kategoriju s negativnim tonom. Razumno je
pitati je li kodna uputa dovoljno jasna i bi li drugi postupak dao drukčiji
ishod. Takav prigovor ne briše podatak, nego zahtijeva otvaranje traga odluke i
može dovesti do ispravka zabilježenoga referentnog ishoda.

Postupovna pravednost u našem primjeru ima prepoznatljiv redoslijed. Interna
kontrola kvalitete traži da osoba zadužena za pregled zna zašto je rečenica
ušla u red, vidi izvornu rečenicu i pravilo, zabilježi obrazloženje te može
osporiti oznaku. Odvojeno od toga, odluka važna za govornika ili uredničku sliku
javnoga govora traži obavijest pogođenoj strani, pravo na žalbu i osobu koja o
njoj odlučuje. Nastavni paket nema identitet govornika i sam ne može uspostaviti
taj institucionalni postupak. Ljudski pregled nije čarobni popravak; i on treba
upute, odgovornost i nadzor.

Promjena oznake mijenja nazivnike i brojnike tablice zabune. Rečenica koja je
bila lažno pozitivna može postati točno pozitivna samo zato što je promijenjen
referentni zapis. Zato se uz rezultate čuva inačica okvira kodiranja, datum
ispravka i razlog promjene. Mjerilo bez puta nastanka oznake nema stabilno
značenje.

Sustav u primjeni nije samo model. Čine ga podatci, pravilo praga, sučelje,
red za ljudski pregled, način bilježenja prigovora i odluka što se iz pregleda
vraća u buduće podatke. Ako se za daljnje učenje biraju samo pregledane
rečenice, sustav češće dobiva nove oznake upravo za tekst koji je već smatrao
zanimljivim. Pogreške u neopaženom tekstu tada teže ulaze u podatke za ispravak
modela.

To je povratna sprega između predviđanja i podataka. Sličan obrazac vrijedi za
sustave preporuke. Rangiranje sadržaja mijenja ono što ljudi vide, a njihovo
ponašanje nakon toga postaje novi podatak za rangiranje. Mjera poput vremena
zadržavanja pritom nije isto što i zadovoljstvo, informiranost ili javna
vrijednost. Ona je operacionalizirani cilj sustava (Barocas, 2023).

[Pomak distribucije]{.pojam
def="Promjena odnosa u novim podatcima zbog koje stara procjena uspješnosti više ne opisuje sadašnji rad sustava."
en="distribution shift" ch="17"} može nastati promjenom jezika, tema, izbora
tekstova ili načina označavanja. Nadzor zato ne pita samo je li ukupna točnost
pala. Operativni pregled prati količinu pregledanoga i nepregledanoga teksta,
sporne oznake, vrijeme do ispravka i promjene granice korpusa. Zaseban slučajni
ili unaprijed stratificirani uzorak nepregledanih rečenica mora dobiti neovisan
i usporediv postupak označavanja. Bez takve provjere ne možemo procijeniti
stopu lažno negativnih odluka nakon ugradnje. Dobra uspješnost na izdvojenim
podatcima nije trajna dozvola za uporabu niti potvrda da oznaka valjano mjeri
ton.

## Jezični modeli kao sustavi predikcije

Asistent kojim smo se služili kroz knjigu pripada istoj obitelji prediktivnih
sustava. Pojam [jezični model kao sustav predikcije]{.pojam
def="Sustav koji iz prethodnoga teksta procjenjuje vjerojatne nastavke i iz njih proizvodi novi tekst."
en="language model as a prediction system" ch="17"} određuje što u toj vezi
provjeravamo. Autoregresivni GPT-3 iz 2020. opisan je kao model koji proizvodi
nastavke uvjetovane prethodnim tekstom (Brown, 2020). Njegov tečan izlaz zato
nije sam po sebi potvrda izvora, ispravnosti brojke ili valjanosti zaključka.
Kao u poglavlju o regresiji, predviđena vjerojatnost ne govori zašto je
pojedinačan tekst dobio određeni odgovor niti sama podupire uzročnu tvrdnju.

Statističko čitanje takva izlaza vraća nas na isti lanac. Pitamo iz kojih su
podataka mogli nastati obrasci, što je jedinica izlaza, koja se odluka na njemu
temelji i kako se pogreška otkriva. Asistent može predložiti klasifikacijsku
tablicu ili izračun, ali ne smije izmisliti stupac s predviđanjima, zamijeniti
nedostupni kontekst pretpostavkom ili proglasiti zabilježenu oznaku
nepogrešivom.

Isti se matematički sukob mjerila pojavljuje i izvan analize parlamentarnoga
govora.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Analiza instrumenata za procjenu rizika
pokazala je sukob između kalibracije i jednakosti određenih stopa pogreške kada
se temeljne stope razlikuju (Chouldechova, 2017).

To je ograničen dokaz o matematičkom odnosu mjerila, ne predložak za prenošenje
kaznenopravnih skupina u naš parlamentarni primjer. Tvrdnja da je model
„pravedan” nije potpuna bez imenovanja zabilježenoga referentnog ishoda,
mjerila, skupina, praga i posljedica. Agregatna točnost može ostati jednaka dok
se vrste pogrešaka vrlo nejednako raspoređuju.

**Pitajte model.**
Asistent može provjeriti pripremljenu tablicu, ali najprije mora dobiti opis
jedinice, granice korpusa, puta oznake i triju skupova. Zatim provjerava
curenje informacija, prag, uvjetne nazivnike, pogreške po dostupnim
podskupinama, promjene distribucije i valjanost kodiranja. Ne dajemo mu osobne
identifikatore niti dopuštamo da nedostupno polje dopuni iz teksta.

> Provjeri ovu pripremljenu klasifikacijsku tablicu. Odvoji ono što podatci
> pokazuju od onoga što ne mogu pokazati. Provjeri jedinicu, granicu korpusa,
> put oznake, razdvajanje dokumenata, prag i svaki uvjetni nazivnik. Navedi
> koje postupke prigovora, ispravka i nadzora ta odluka zahtijeva.

**Nađite grešku.**
Ako model na izdvojenom skupu za ispitivanje postigne visoku točnost prema
zabilježenim oznakama, time je dokazano da ispravno mjeri ton.

## Razrađeni primjer

Račun ispituje samo 272 retka skupa za provjeru, u kojem su dostupne dvije
pojedinačne oznake i usklađena zabilježena oznaka. Za nastavnu provjeru gradimo
jednostavan rezultat s mogućim vrijednostima 0, 0,5 i 1. U ovoj se nastavnoj
redukciji oznake `Negative` i `M_Negative` računaju kao negativan glas, a
`Positive`, `M_Positive`, `N_Neutral` i `P_Neutral` kao nenegativan glas. To je
odluka koju treba provjeriti na osjetljivost. Rezultat nije predviđena
vjerojatnost modela, jezični model ni neovisna provjera. Usklađena oznaka nastala je iz
istih koderskih ulaza, pa račun namjerno pokazuje ovisnost mjerila o postupku
proizvodnje oznake.

U razrađenom računu prag pravila odluke postavljamo na 0,5. To nije
klasifikacijski prag nad predviđenom vjerojatnošću, nego strukturno slično
pravilo nad dvama koderskim glasovima koje služi samo provjeri puta oznake.
Rečenica ulazi u red ako je barem jedan koder dao negativan glas. `mutate()`
primjenjuje tu odluku na svaki redak, a `count()`
ispisuje četiri ćelije kontingencijske tablice poznate iz poglavlja o
kategoričkim podatcima.

Prag 0,5 uspoređujemo sa strožim pragom 1, kod kojega oba kodera moraju
odabrati negativnu kategoriju. Brojevi u tablici izravno se reproduciraju iz
pripremljenoga paketa.

*Slika. Dvije odluke o ljudskom pregledu prema istom zabilježenom referentnom ishodu u skupu za provjeru. Izrada autora prema @mochtak2023.*

Uz niži prag svih je 122 rečenica sa zabilježenim negativnim ishodom poslano u
pregled, ali je u red ušlo i 16 od 150 rečenica sa zabilježenim nenegativnim
ishodom. Uz stroži prag nisu ušle 22 od 122 rečenice sa zabilježenim negativnim
ishodom, dok je među 150 rečenica sa zabilježenim nenegativnim ishodom samo
jedna ušla. Niži prag zato ima stopu lažno
pozitivnih odluka 10,7 % i stopu lažno negativnih odluka 0,0 %. Stroži prag
ima odgovarajuće stope 0,7 % i 18,0 %.

Ne možemo iz same tablice proglasiti jedno pravilo najboljim. Uredništvo mora
odrediti posljedicu nepotrebnoga pregleda, posljedicu izostavljanja, raspoloživ
kapacitet i put prigovora. Prije toga mora obrazložiti zašto negativan polaritet
uopće određuje red te usporediti takvu politiku sa slučajnom provjerom ili
kriterijem relevantnosti koji ne ovisi o sentimentu. Provjera osjetljivosti
zaključka na prag pokazuje da odluka o redu nije sadržana u podatcima.

Ispitni dio postavlja važno ograničenje. Ondje nije dostupan drugi koder ni
usklađenje, pa se pravilo dvaju glasova ne može primijeniti ni vrednovati na
isti način. Pošten izvještaj zato ne izmišlja završnu uspješnost. Za budući bi
klasifikator trebalo unaprijed zaključati model, prag i usporediv referentni
postupak, sačuvati njegova predviđanja te tek jednom otvoriti skup za
ispitivanje. Ovaj paket podupire provjeru podataka i odluke, ali ne tvrdnju o
izvedbi nepostojećega modela izvan korpusa.

Povratak početnoj rečenici sada daje drukčiji odgovor. Znamo zašto je njezina
oznaka sporna i što bi slanje u pregled učinilo, ali nemamo osnovu tvrditi što
je govornik namjeravao. Razumna odluka zahtijeva pregled izvornoga teksta,
vidljivo obrazloženje, mogućnost ispravka i praćenje učinka praga.

## Granica Dijela V — Od modela do sustava u primjeni

Na prijelazu iz modela u sustav u primjeni provjeravamo jedinicu i granice
podataka, vrstu tvrdnje, izvore nesigurnosti, razumne alternative i osobe koje
odluka može pogoditi. Primjena na ljudski pregled pokazuje dokle ovaj dokaz
seže.

| Pitanje revizije | Primjena na odluku o ljudskom pregledu |
|---|---|
| Što predstavlja jedan redak ili jedno opažanje? | jednu odabranu parlamentarnu rečenicu s putom nastanka zabilježene oznake, ne govor, govornika ili sjednicu |
| Tko ili što nije moglo ući u ove podatke? | rečenice moderatora i rečenice izvan srednjega raspona duljine isključene su uzvodno; paket nema govornika, cijeli govor ni obranjivu skupnu varijablu |
| Koja je ciljana količina i vrsta tvrdnje? | tablica uspoređuje dva pravila slanja u pregled prema zabilježenom negativnom ishodu; riječ je o opisu i provjeri odluke, ne izvedbi postojećega klasifikatora |
| Koji su izvori nesigurnosti obuhvaćeni, a koji ostaju izvan izračuna? | prikazana je osjetljivost odluke na prag pravila, ali ne i uzoračka reprezentativnost, valjanost sentimenta, pogreška kodiranja ili budući pomak distribucije |
| Koja bi razumna alternativna odluka mogla bitno promijeniti odgovor? | stroži prag mijenja teret pogrešaka, a slučajna provjera ili kriterij relevantnosti mijenjaju i sam cilj uredničkoga reda |
| Na koga može utjecati pogrešan zaključak ili odluka? | pregledavatelji mogu trošiti pozornost na pogrešne retke, važan tekst može biti izostavljen, a govornik ili javnost mogu dobiti iskrivljenu uredničku sliku |

: Šest revizijskih pitanja za odluku o ljudskom pregledu. Izrada autora prema Mochtak, 2023 i mochtakparlasent2024.

Isti dokaz zatim raspoređujemo u šest dimenzija tvrdnje. One nisu ljestvica na
kojoj svaka analiza mora dosegnuti vrh, nego karta različitih zahtjeva za
dokazom.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje brojnosti, put oznake i posljedice dvaju pravila unutar pripremljenoga paketa |
| povezanost | pokazuje povezanost dvaju koderskih glasova s usklađenom oznakom, uz izričitu ovisnost jer su isti glasovi sudjelovali u njezinu nastanku |
| generalizacija | ne podupire prijenos na sav parlamentarni govor, govornike ili tekstove izvan odabranih rečenica |
| predviđanje | ne ocjenjuje postojeći model; buduća bi procjena tražila zaključan model, prag, usporediv referentni postupak i jedan izdvojeni ispitni skup |
| uzročnost | ne pokazuje što uzrokuje ton, uredničku važnost ili bilo koju posljedicu za govornika |
| odluka | podupire provjeru tereta dvaju pragova, ali ne dokazuje da je negativan sentiment legitiman cilj usmjeravanja pozornosti |

: Šest dimenzija tvrdnje na granici Dijela V. Izrada autora prema mochtak2023.

Zašto razdvajanje na skup za učenje, provjeru i ispitivanje ne stvara
populacijsku reprezentativnost? Kako uzvodni
odabir i put oznake ograničavaju tablicu zabune? Zašto jednake uvjetne stope
pogreške ne jamče jednaku pozitivnu prediktivnu vrijednost? Što nakon ugradnje
moramo opažati izvan redovnoga reda za pregled da bismo uopće mogli procijeniti
lažno negativne odluke?

Završno poglavlje preuzima prag, teret pogreške, nadzor i put prigovora kao
dijelove vlastitoga istraživačkog protokola. Asistentu se može odgovorno
delegirati račun i provjera dosljednosti, ali izbor cilja, procjena dokaza i
odgovornost za objavljenu odluku ostaju na istraživaču.

## Sažetak

Algoritamska odluka počinje granicom korpusa i postupkom mjerenja, a ne
modelom. Razdvajanje na skup za učenje, provjeru i ispitivanje štiti procjenu
predviđanja, ali ne stvara populacijsku reprezentativnost ni valjan konstrukt.
Klasifikacijski prag raspoređuje vrste pogrešaka, a temeljne stope mogu dovesti
mjerila pravednosti u sukob. Nakon ugradnje podatci, sučelje, ljudski pregled,
prigovor, povratna sprega i nadzor čine jedan sustav. Jezični model proizvodi
vjerojatan nastavak; provjera izvora i odgovornost za odluku ostaju ljudske.
U završnom poglavlju isti se zahtjev pretvara u cjelovit protokol u kojem prag,
teret pogreške, nadzor, prigovor i odgovorno delegiranje moraju ostati vidljivi
od pitanja do objave.

## Pojmovi

tekstna jedinica (*text unit*), granica korpusa (*corpus boundary*), okvir
kodiranja (*coding frame*), zabilježeni referentni ishod (*recorded reference
outcome*), razdvajanje na skup za učenje, provjeru i ispitivanje
(*train-validation-test split*), preprilagodba (*overfitting*), klasifikacijski
prag (*classification threshold*), tablica zabune (*confusion matrix*),
pogreške po podskupinama (*subgroup errors*), algoritamska pravednost
(*algorithmic fairness*), pomak distribucije (*distribution shift*), jezični
model kao sustav predikcije (*language model as a prediction system*)

## Zadaci

### Konceptualni

Objasnite kako razdvajanje na skup za učenje, provjeru i ispitivanje otkriva
preprilagodbu te zašto dokument koji prijeđe među skupovima stvara curenje
informacija. Zatim povežite tablicu zabune s kontingencijskom tablicom iz
poglavlja o kategoričkim podatcima i objasnite zašto predviđena vjerojatnost iz
poglavlja o regresiji još nije odluka. Imenujte oba uvjetna nazivnika pogreške.

### Računski

U pripremljenoj tablici odluka nalazi se 90 točno pozitivnih, 30 lažno
pozitivnih, 10 lažno negativnih i 170 točno negativnih slučajeva. Izračunajte
stopu lažno pozitivnih odluka, stopu lažno negativnih odluka, pozitivnu
prediktivnu vrijednost i točnost. Uz svaki rezultat napišite njegov nazivnik i
jednu moguću posljedicu za red ljudskoga pregleda.

### Kritički

Osporite zabilježenu oznaku početne rečenice. Napišite koje biste dijelove
okvira kodiranja, izvornih oznaka i usklađenja trebali vidjeti prije odluke.
Zatim objasnite zašto promjena oznake može promijeniti mjerila pravednosti bez
ijedne promjene modela.

### Revizija modela

Ocijenite tvrdnju iz okvira o pogrešci. Navedite jednu prihvatljivu tvrdnju,
jedan pogrešan prijelaz i dokaz koji pokazuje razliku. Zatim u najviše šest
rečenica revidirajte tvrdnju tako da obuhvati jedinicu, granicu korpusa, put
oznake, curenje, prag, dostupne podskupine, pomak distribucije te postupak
obavijesti, prigovora i žalbe. Objasnite zašto tečan odgovor jezičnoga modela
ne dokazuje nijednu nedostupnu sastavnicu.
