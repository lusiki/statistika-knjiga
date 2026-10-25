# Zašto statistika

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/01-zasto-statistika.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

**Podsjetnik.** Udjeli i stope

Jesu li poslijediplomski programi Sveučilišta Kalifornije u Berkeleyju
diskriminirali žene pri upisu 1973. godine? Zbirne stope prijma muškaraca i
žena toliko su se razlikovale da su potaknule sumnju u postupak upisa
(Bickel, 1975).

Istraživači su zatim usporedili prijave unutar svakog odjela. Pokazalo se da
su se žene češće prijavljivale na odjele koji su primali manji udio kandidata.
Zbirna razlika zato nije izravno pokazivala kako su pojedini odjeli odlučivali
o prijavama muškaraca i žena (Bickel, 1975).

Oba su izračuna točna i koriste iste prijave. Ukupne stope pokazuju veliku
razliku, a stope po odjelima otkrivaju koliko na nju utječe raspored prijava.
Koja usporedba odgovara na pitanje koje nas zanima?

Kad pročitamo da je jedna skupina uspješnija od druge, lako je preskočiti
račun i odmah tražiti objašnjenje. Berkeleyjski slučaj poziva nas da zastanemo
kod same usporedbe (Bickel, 1975). Prije odluke o tome što razlika znači
trebamo znati koga uspoređujemo, što je zabilježeno i prema kojoj cjelini
računamo postotak. To su pitanja od kojih ćemo krenuti, bez pretpostavke da
već poznajemo statističke postupke.

U knjizi ćemo učiti pratiti put od istraživačkog pitanja do zaključka. Račun
će nam pomoći opisati podatke, usporediti skupine i procijeniti nesigurnost,
ali morat ćemo odlučiti odgovara li na pitanje koje smo postavili. Za početak
su nam dovoljni poznati postoci, jednostavne tablice i spremnost da provjerimo
što stoji iza broja. Ne trebamo znati programirati. Trebamo moći objasniti
zašto smo nešto podijelili, koga smo izostavili i dokle dobiveni odgovor
vrijedi.

Uz stvarni slučaj prijava koristit ćemo autorski skup `populacija_medija`,
računalno stvorenu populaciju odraslih osoba iz zamišljenoga grada
(Šikić, 2026). Jedan zapis predstavlja jednu zamišljenu osobu. U prvom ćemo
računu povezati njezin glavni izvor vijesti sa spremnošću na plaćanje vijesti.
Usporedit ćemo broj osoba koje bi platile s njihovim udjelom unutar pojedinog
izvora. Tako možemo pratiti svaki korak bez tvrdnje da opisujemo stvarnu
medijsku publiku.

Prijave na studij i spremnost na plaćanje vijesti različite su pojave, ali
pred nas postavljaju sličan problem. Broj dobiva značenje tek kada znamo koje
je ljude ili prijave obuhvatio i s čime ih uspoređujemo. Dok pratimo te
usporedbe, razlikovat ćemo ono što podaci već pokazuju od onoga za što nam
treba dodatno objašnjenje. Tu razliku tražimo i kada čitamo istraživanje,
medijski naslov ili odgovor asistenta.

## Broj nije zaključak

Zbirna stopa govori tko je češće primljen među svim prijavljenim kandidatima.
Stope po odjelima govore kako su prolazili kandidati koji su se prijavili na
isti odjel. Za zaključak moramo znati koju od tih usporedbi trebamo. Sama
računska točnost to ne određuje.

Da bismo procijenili pravednost upisa, morali bismo poznavati i kriterije
odlučivanja te okolnosti koje tablica ne bilježi. Zasad možemo provjeriti kako
raspored prijava i veličina skupina mijenjaju značenje izračuna.

**Statistika** povezuje istraživačko pitanje s podacima i zaključkom koji iz
njih možemo izvesti. Uz račun provjeravamo što je izmjereno i jesu li skupine
koje uspoređujemo prikladne za naše pitanje. Pogreška u tom izboru može
dovesti do pogrešnog zaključka i kada u računanju nema propusta.

Najprije utvrđujemo što predstavlja jedan zapis. U zbirnoj tablici prijava
redak opisuje više prijava iste vrste. U tablici pojedinačnih odgovora redak
može opisivati jednu osobu. Broj redaka zato ne mora biti jednak broju ljudi,
događaja ili neovisnih opažanja.

**Jedinica analize** je ono o čemu donosimo zaključak, primjerice osoba,
kućanstvo, organizacija ili objava. Jedan redak tablice ne mora predstavljati
jednu neovisnu jedinicu.

Ako istu osobu pitamo za mišljenje svakoga od sedam dana, dobivamo sedam
redaka, ali jednu osobu. Njezini odgovori mogu biti slični upravo zato što
pripadaju istoj osobi. Sedam redaka zato ne daje sedam neovisnih potvrda.

**Podsjetnik.** Postotci i postotni bodovi

U skupu `populacija_medija` imamo zapise za 50.000 zamišljenih odraslih
stanovnika (Šikić, 2026). Uz izvor vijesti i spremnost na plaćanje, za svaku su
osobu zabilježeni dob, obrazovanje, povjerenje u medije na ljestvici od 1
do 10 i dnevno praćenje medija. Istom ćemo
se populacijom služiti pri uzorkovanju, usporedbama skupina i regresiji, kako
bismo nove postupke mogli pratiti na poznatom primjeru.

Računalno stvaranje tih zapisa slijedi zadana pravila. Najprije nastaju dob
i izvor vijesti, čije se vjerojatnosti mijenjaju s dobi. Povjerenje ovisi o
dobi i izvoru uz slučajno odstupanje, a spremnost na plaćanje o povjerenju i
obrazovanju. Tako nastaju namjerno povezane varijable. Jedna osoba može
odstupati od zadanoga obrasca, a cjelina od 50.000 osoba pokazuje obrazac koji
je autor ugradio u generator (Šikić, 2026).

Prva tri retka pokazuju kako taj skup izgleda prije sažimanja. Svaki redak
čuva više obilježja iste generirane osobe (Šikić, 2026).

*Slika. Tri zapisa iz generirane populacije medijskih navika. Izrada autora prema @sikic2026.*

Broj osobe služi povezivanju njezinih odgovora. Vrijednost u stupcu izvora
vijesti jedna je kategorija, povjerenje je ocjena, a spremnost na plaćanje
u ovoj je tablici prikazana odgovorom da ili ne.
Kada poslije nacrtamo graf ili izvučemo uzorak, mijenjamo način uporabe tih
zapisa, a ne njihovo podrijetlo.

Iz takvih zapisa možemo prebrojiti osobe spremne platiti vijesti. Želimo li
usporediti izvore s različitim brojem korisnika, trebamo i **nazivnik**,
količinu s kojom dijelimo brojnik. Brojnik je broj slučajeva koji
zadovoljavaju uvjet, ovdje osoba spremnih platiti vijesti.
Među 4.855 osoba kojima je tisak glavni izvor vijesti njih 1.289 spremno je
platiti vijesti. Među 15.101 korisnikom portala spremnih je 3.514
(Šikić, 2026). U većoj skupini takvih osoba ima više, ali tek dijeljenjem
možemo usporediti udjele. Jednako treba znati prema kojoj količini računamo
stopu ili prosjek.

Provjeravamo i **podrijetlo podataka**. Treba znati tko ih je proizveo, kojim
postupkom, koju inačicu koristimo i koja su njezina ograničenja. Za naš je
nastavni skup poznat postupak stvaranja i njegovo sjeme, početna postavka koja
omogućuje ponavljanje iste simulacije (Šikić, 2026). Zato možemo provjeriti
račun i tumačenje. Za tvrdnju o hrvatskoj publici trebali bismo podatke
prikupljene od stvarnih ljudi.

Poznavanje podrijetla podataka pomaže nam procijeniti i što možemo doznati iz
osobnog iskustva. Anegdota može upozoriti na
problem, ponuditi moguće objašnjenje ili opisati posljedicu koja se iz tablice
ne vidi. Sama ipak ne pokazuje koliko je pojava raširena ni bi li se ponovila
u drugim okolnostima. Za to trebamo više opažanja, uz jasnu odluku o tome koga
promatramo, što mjerimo i što uspoređujemo.

Iskaz ispitanice o tome zašto je prestala čitati vijesti, primjerice, otkriva
okolnosti i redoslijed događaja koji bi mogli objasniti njezinu odluku. Taj
iskaz upućuje na ono što treba provjeriti. Uređen skup podataka omogućuje da
zatim ispitamo kako se pojava raspoređuje među promatranim ljudima. Želimo li
zaključak proširiti na druge ljude, moramo opravdati i način odabira
sudionika. Iz jednog svjedočenja ne možemo odrediti raširenost pojave, kao što
iz prosjeka ne možemo iščitati iskustvo svake osobe.

Za takve odluke potrebno je poznavanje područja. Teorija i okolnosti slučaja
pomažu nam odabrati usporedive skupine, predložiti objašnjenje i prosuditi
koliko bi velika razlika bila važna. Izračun slijedi te odluke.

Dobar statistički postupak ostavlja jasan trag od opažanja do tvrdnje. Druga
osoba mora moći pregledati te korake, ponoviti račun i provjeriti opravdavaju
li podaci zaključak.

## Odluka koja se donosi bez dokaza

Slične odluke donosimo i izvan istraživanja. Zamislimo portal kojem pada
posjećenost. Urednik smatra da su naslovi dosadni i predlaže drukčiji stil.
Možda je u pravu. Posjećenost se, međutim, mogla promijeniti i zbog vremena
objave, duljine tekstova, nove konkurentske aplikacije ili godišnjeg doba u
kojem publika ima druge navike.

Bez provjere tih objašnjenja lako prevagne mišljenje najupornijeg ili
najutjecajnijeg sugovornika. Isto pitanje nastaje kada ministarstvo
procjenjuje učinak mjere, udruga doseg kampanje ili stranački stožer promjenu
u anketi. Statistički postupak omogućuje da svako objašnjenje usporedimo s
podacima. Odgovor ponekad ostane neodređen, ali postaje jasnije što znamo i
što bi još trebalo provjeriti.

Sociologija, politologija, psihologija, komunikologija i ekonomija empirijske
su discipline. Njihove tvrdnje provjeravamo opažanjem. Tvrdnju da povjerenje u
medije pada treba povezati s mjerenjima povjerenja, a tvrdnju da negativne
vijesti privlače više pozornosti s odgovarajućom usporedbom. Isto vrijedi za
moguću povezanost dohotka i sudjelovanja. U svakom slučaju moramo objasniti
kako podaci podupiru upravo izrečenu tvrdnju.

Podacima se pritom služe i ljudi izvan istraživačkih ustanova. Odluke o sadržaju, oglasima i dosegu temelje se i na zapisima o klikovima,
otvaranju poruka i vremenu gledanja. Razumijevanje tih zapisa omogućuje nam da sudjelujemo u
raspravi o odlukama koje se na njima temelje.

Prije primjene formule zato procjenjujemo odgovara li postupak pitanju. Treba
provjeriti jesu li skupine usporedive, što je doista izmjereno i koliko je
rezultat nesiguran. Tek tada možemo reći koju odluku analiza podupire i dokle
njezin zaključak vrijedi.

Izračun ne može nadoknaditi sve što nedostaje u podacima. Istraživač i dalje
mora prosuditi koja je usporedba važna i jesu li mjerenja dovoljna. Statistika
pomaže izraziti nesigurnost, pa zaključak često mora biti oprezniji od početne
pretpostavke. To omogućuje da nalaz upotrijebimo uz razumijevanje njegovih
ograničenja.

## Životni ciklus podataka

Da bismo provjerili urednikovo objašnjenje pada posjećenosti, morali bismo
odabrati zapise, pregledati ih i tek potom usporediti naslove. I druge
istraživačke tvrdnje nastaju kroz takav niz povezanih koraka, koji nazivamo
**životnim ciklusom podataka**. On obuhvaća pribavljanje i analizu podataka,
tumačenje rezultata te praćenje njihove uporabe nakon objave. Tablica
pokazuje koje nas pitanje vodi u svakom koraku.

| Faza | Pitanje koje je vodi |
|---|---|
| pitanje | Koju odluku ili tvrdnju treba razjasniti? |
| pribavljanje | Odakle zapisi dolaze i tko može izostati? |
| provjera | Predstavlja li redak očekivanu jedinicu i jesu li vrijednosti moguće? |
| priprema | Koje su promjene napravljene prije analize? |
| istraživanje | Koji su obrasci, iznimke i alternativna objašnjenja vidljivi? |
| modeliranje | Koja usporedba ili model odgovara pitanju? |
| vrednovanje | Koliko je rezultat stabilan i gdje ne uspijeva? |
| komunikacija | Koju tvrdnju rezultat doista podupire? |
| praćenje | Mijenjaju li se podaci, uporaba ili posljedice nakon objave? |

: Životni ciklus podataka i odluke koje vodi. Izrada autora.

Tijekom analize često se vraćamo na ranije korake. Provjera može pokazati da
smo preuzeli pogrešne zapise, a prvi pregled podataka da pitanje treba suziti.
Takve promjene bilježimo kako bi se poslije moglo razumjeti zašto koristimo
određenu datoteku ili odgovaramo na izmijenjeno pitanje.

Već pri pribavljanju podataka utvrđujemo čiji su zapisi uključeni, što
predstavljaju i koji nazivnik trebamo. Nepoznato podrijetlo, dvostruko
zabilježene jedinice ili mjerenje pogrešnog pojma treba razriješiti prije
modeliranja. Složeniji model sam po sebi ne rješava te probleme.

### Četiri djelatnosti i četiri pitanja

Statistika, podatkovna znanost, strojno učenje i sustavi umjetne inteligencije
sudjeluju u različitim koracima tog postupka. Njihove se zadaće preklapaju,
ali svaka od tih djelatnosti naglašava drugo pitanje.

Model ovdje znači pojednostavljen prikaz pravilnosti u podacima. Na primjer,
može povezati dob osobe s njezinim očekivanim povjerenjem. Prikaz pomaže
opisivanju ili predviđanju, ali sam ne pokazuje što uzrokuje odnos.

| Djelatnost | Vodeće pitanje |
|---|---|
| statistika | Što ovi podaci opravdavaju vjerovati? |
| podatkovna znanost | Kako stvarni izvori podataka mogu postati pouzdana i reproducibilna analiza? |
| strojno učenje | Hoće li naučeni obrazac raditi na doista novim opažanjima? |
| sustav umjetne inteligencije | Mogu li se naučeni obrasci upotrijebiti za generiranje, preporučivanje, klasificiranje ili djelovanje u institucionalnom okruženju? |

: Četiri djelatnosti prema pitanju koje postavljaju. Izrada autora.

**Podatkovna znanost** obuhvaća rad kojim od izvora podataka dolazimo do
analize koju možemo ponoviti. **Strojno učenje** ispituje koliko dobro obrazac
naučen iz jednih podataka djeluje na novim opažanjima. Taj je pristup blizak
algoritamskoj kulturi modeliranja koju je Breiman razlikovao od modeliranja
usmjerenog na objašnjenje (Breiman, 2001). **Sustav umjetne inteligencije**
uključuje model, sučelje i način njegove uporabe u određenoj ustanovi ili
postupku odlučivanja. Pri procjeni takvog sustava razmatramo tehnička
svojstva, ali i pogreške te posljedice uporabe (Barocas, 2023).

Suvremena umjetna inteligencija ovisi o više vrsta rada. Statističko učenje i
algoritmi strojnog učenja povezuju se s digitalnim podacima, optimizacijom i
računalnom opremom. Ljudi označuju podatke, grade programsku infrastrukturu i
provjeravaju rezultate. Podatkovna znanost organizira mnoge od tih koraka, pa
je razlikujemo od samog strojnog učenja.

Svaki dio postupka treba zasebno provjeriti. Analizu možemo uspješno ponoviti,
a da je njezin zaključak i dalje pogrešan. Model može dobro predviđati, a da
ne objašnjava uzrok. Jednako tako, dobar statistički račun ostaje upitan ako
ne znamo podrijetlo podataka, ako je ishod nehotice dospio među podatke za
učenje ili ako nitko ne može ponoviti pripremu podataka. Ako među
prediktorima već stoji odgovor koji navodno predviđamo, prividni uspjeh
ne govori kako bismo predviđali novu osobu. Tom se problemu vraćamo u
poglavljima o regresiji i algoritmima.

## Gdje intuicija popušta

Zaključak se katkad čini toliko očitim da provjera izgleda suvišna. Ipak, pri
procjeni slučajnosti i promjenjivosti lako uočimo obrazac i ondje gdje ga
nema.

Uzmimo dva niza od 10 bacanja poštenog novčića. U prvom se pismo i glava
pravilno izmjenjuju. U drugom nema pravilne izmjene, a pismo se pojavljuje i
triput zaredom. Drugi niz može izgledati prirodnije, ali svaki od 1024 moguća
niza ima jednaku vjerojatnost. Dojam nastaje zato što očekujemo da slučajan
niz izgleda na određen način. Slučajnost može proizvesti i pravilnu izmjenu i
nekoliko jednakih ishoda zaredom.

Slično zaključujemo iz poznatih primjera. Ako susjed i dvoje kolega hvale novu
aplikaciju za vijesti, mogli bismo pomisliti da je ona općenito dobro
prihvaćena. Troje poznanika ipak ne predstavlja cijelu publiku. Možda se
vijestima bave više od drugih pa su zato i isprobali aplikaciju. Tversky i
Kahneman nazvali su heuristikom dostupnosti sklonost da učestalost
procjenjujemo prema tome koliko se lako prisjetimo nekog primjera
(Tversky, 1973). Živopisan ili nedavan slučaj tako može ostaviti pretjerano
snažan dojam.

Zamislimo i usporedbu u kojoj portali s više objavljenih tekstova imaju više
posjeta. Iz nje se lako izvodi preporuka da treba više objavljivati. Veći
portali, međutim, mogu imati i više novinara, veći proračun te drukčiju,
stariju publiku. Treba razmotriti utječe li broj tekstova na posjete, potiče
li veća posjećenost objavljivanje ili oboje ovisi o drugim obilježjima
portala. Postupke kojima provjeravamo takva objašnjenja razradit ćemo u
poglavljima o istraživačkom dizajnu i regresiji.

Za svaki od tih zaključaka trebamo dodatnu usporedbu. Niz bacanja uspoređujemo
s ostalim mogućim nizovima, pohvale aplikacije s iskustvima šire publike, a
posjete portalima uzimajući u obzir njihovu veličinu. Time postaje vidljivo na
čemu se zaključak temelji.

Velik broj zapisa ne može zamijeniti tu provjeru. Portal može zabilježiti
milijune interakcija, a i dalje ništa ne znati o ljudima koji ga ne posjećuju.
Odgovori većega broja zasebno odabranih ljudi obično daju stabilniji
postotak od odgovora male skupine. Ponavljanje istih odgovora ne donosi
istu korist. Sustavno izostavljanje
dijela publike pritom ostaje.

Unatoč tim ograničenjima možemo donositi korisne zaključke. Statistički
postupci, kada su njihove pretpostavke opravdane, omogućuju da izračunamo dio
nesigurnosti. Mjerenje, odabir sudionika i promjenu okolnosti moramo zasebno procijeniti. Tako možemo obrazložiti što zaključujemo i zašto zaključak
ograničavamo na određene uvjete.

## Signal u promjenjivom svijetu

Čak i kada dobro odaberemo usporedbu, opažanja se neće savršeno slagati.
Dvije osobe mogu različito reagirati na istu poruku. Ista anketa na drugom
uzorku dat će nešto drukčije postotke, a ponašanje jedne osobe može se
mijenjati s vremenom. Statistika nam pomaže proučavati društvene pojave uz tu
promjenjivost.

Pritom pokušavamo razlikovati **signal**, obrazac koji nas zanima, od
**šuma**, ostalih izvora varijacije. Signal može biti razlika među skupinama
ili povezanost dviju pojava. Šum otežava da taj obrazac razaberemo iz
pojedinačnih opažanja. Što smatramo signalom ovisi o pitanju koje postavljamo.

Kad uspoređujemo povjerenje u institucije među dobnim skupinama, razlike među
ljudima iste dobi mogu otežati uočavanje dobnog obrasca. Ako zatim počnemo
istraživati zašto se ljudi iste dobi razlikuju, te razlike postaju ono što
želimo objasniti. Isti podaci tako mogu poslužiti različitim pitanjima.

I usporedba političkog sudjelovanja može dati različite rezultate ovisno o
tome razmatramo li dob, obrazovanje, dohodak ili mjesto stanovanja. Svaki od
tih izbora izdvaja drugi dio promjenjivosti. Zbog toga se nalazi o istoj
pojavi mogu razlikovati i kada su svi računi točni. Pri čitanju istraživanja
treba provjeriti koja su obilježja uključena u usporedbu.

Jedan student koji se mnogo koristi društvenim mrežama i slabo prati vijesti
nije dovoljan dokaz o povezanosti tih navika. Ni student s drukčijim navikama
sam ne opovrgava tu povezanost. Osoba je jedinica analize, ali obrazac
procjenjujemo usporedbom većeg broja osoba.

Važni su i broj opažanja i način na koji su nastala. Uz isti postupak
prikupljanja i dovoljno neovisne jedinice, razlika među desetak ljudi lakše
može nastati slučajnim rasipanjem nego jednaka razlika među tisućama.
Ponavljanje istih zapisa ili dodavanje snažno povezanih opažanja ne donosi
jednaku količinu nove informacije.

Za tumačenje rasta, pada ili razlike trebamo znati s čime uspoređujemo
rezultat. To može biti druga skupina, ranije razdoblje ili raspon vrijednosti
koje bi nastale slučajnom promjenjivošću.  Najprije treba jasno imenovati obje strane usporedbe.

## Razlika koju čini postupak

Imenovanje obiju strana usporedbe pomaže nam odrediti i kakav zaključak
tražimo. Opis govori što smo zabilježili, a
povezanost kako se pojave mijenjaju zajedno. Generalizacijom nalaz prenosimo
na jedinice koje nismo promatrali. Predviđanjem procjenjujemo nove ishode, dok
uzročna tvrdnja govori što bi određena promjena proizvela. Odluka uz nalaz
uključuje i procjenu mogućih postupaka te njihovih posljedica. Broj koji dobro
opisuje podatke zato ne mora biti dovoljan za uzročni zaključak.

Za isti skup podataka možemo postaviti različita pitanja. Sljedeće su
formulacije primjeri vrsta tvrdnji, a ne dodatni empirijski nalazi.

| Vrsta tvrdnje | Primjer pitanja |
|---|---|
| opis | Koliki udio zabilježenih osoba koristi portal? |
| povezanost | Razlikuje li se povjerenje među dobnim skupinama? |
| generalizacija | Što odgovori iz uzorka govore o svim odraslim stanovnicima? |
| predviđanje | Hoće li nova osoba biti spremna platiti vijesti? |
| uzročnost | Bi li promjena cijene promijenila spremnost iste publike na plaćanje? |
| odluka | Isplati li se promijeniti cijenu uz očekivanu korist i trošak pogreške? |

: Šest vrsta tvrdnji i pitanja koja ih razlikuju. Izrada autora.

Pri procjeni zaključaka koristimo **šest revizijskih pitanja**. Pitanja ostaju ista i u kasnijim poglavljima, a odgovori ovise o podacima i
postupku.

| Revizijsko pitanje | Što treba biti vidljivo |
|---|---|
| Koja je jedinica? | Što predstavlja zapis i na kojoj se razini izriče zaključak? |
| Tko ili što nedostaje? | Kako su jedinice ušle u podatke i tko je mogao izostati? |
| Koji je cilj tvrdnje? | Je li riječ o opisu, povezanosti, generalizaciji, predviđanju, uzročnosti ili odluci? |
| Gdje je neizvjesnost? | Dolazi li iz mjerenja, uzorkovanja, modela ili promjene okolnosti? |
| Koje drugo objašnjenje ostaje? | Koji bi još proces mogao proizvesti isti obrazac? |
| Tko snosi posljedice? | Tko dobiva korist, tko pogrešku i postoji li način osporavanja? |

: Šest revizijskih pitanja. Izrada autora.

U Berkeleyjskim podacima promatramo prijave iz određenog razdoblja. Nemamo
cijeli obrazovni put kandidata ni podatke o procesima koji su prethodili
prijavi (Bickel, 1975). Iz stopa možemo opisati ishode tih prijava. Za motive
ljudi koji su odlučivali ili posljedice drukčijih kriterija trebali bismo
dodatne podatke.

Odgovori na šest pitanja pomažu odrediti što podaci podupiru i koja
pretpostavka traži najviše provjere. To ne jamči da ćemo biti u pravu, ali
omogućuje da drugi razumiju i provjere naš zaključak.

## Zbirna slika i skrivena struktura

Vratimo se sada razlici između ukupne stope prijma i stopa po odjelima.
Ukupni prosjek ili stopa ovisi o rezultatima podskupina i o tome koliko je
svaka podskupina zastupljena. Brojnija podskupina više utječe na ukupni
rezultat. Zato se zbirna stopa može promijeniti samo zbog drukčijeg sastava,
čak i ako stope unutar podskupina ostanu jednake.

U Berkeleyju su se odjeli razlikovali po tome koliko je teško bilo upisati ih.
Žene su češće birale selektivnije odjele, pa su ti odjeli više utjecali na
njihovu ukupnu stopu prijma. Usporedba unutar pojedinih odjela uklonila je taj
utjecaj rasporeda prijava. Razlika vidljiva u zbirnim podacima tada se
smanjila ili preokrenula (Bickel, 1975).

Brojnosti pokazuju oba pogleda na Berkeley. Za cijelo sveučilište bilo je
8 442 prijave muškaraca, od kojih je prihvaćeno 3 738, te 4 321 prijava
žena, od kojih je prihvaćeno 1 494 (Bickel, 1975). To daje 44,3 % i
34,6 %. Sljedeća tablica prikazuje šest najvećih odjela iz istoga slučaja,
sačuvanih u skupu `UCBAdmissions`. Njihovih 4 526 prijava čini podskup,
pa njegov zbirni postotak nije postotak cijeloga sveučilišta (Bickel, 1975).

*Slika. Prijave i prijam u šest najvećih odjela Berkeleyja 1973. Podaci UCBAdmissions prema @bickel1975; postoci izračunati iz prikazanih brojnosti.*

U odjele A i B, koji imaju visoke stope prijma, prijavilo se
`r sum(berkeley1$Prijave[berkeley1$Gender == "Male" & berkeley1$Dept %in% c("A", "B")])`
od `r sum(berkeley1$Prijave[berkeley1$Gender == "Male"])` muškaraca iz ovoga
podskupa, a samo
`r sum(berkeley1$Prijave[berkeley1$Gender == "Female" & berkeley1$Dept %in% c("A", "B")])`
od `r sum(berkeley1$Prijave[berkeley1$Gender == "Female"])` žena (Bickel, 1975).
Razlikuju se i stope unutar odjela i udjeli prijava usmjerenih u pojedine
odjele. Zbirni postotak uključuje oboje; tablica sama ne objašnjava
zašto je izbor odjela bio tako raspoređen.

**Simpsonov paradoks** je obrazac u kojem se smjer povezanosti u združenim
podacima promijeni ili preokrene kada se podaci razdvoje prema relevantnoj
trećoj varijabli (Simpson, 1951).

Sve izračunate stope pritom mogu biti točne. Zaključak se mijenja zato što
zbirna usporedba i usporedba po podskupinama odgovaraju na različita pitanja.

To možemo vidjeti na konstruiranom primjeru dvaju portala. Brojevi služe
prikazu postupka i nisu podaci o stvarnim portalima. Portal A objavljuje 100
videozapisa s prosječno 200 reakcija i 10 tekstova s prosječno 50 reakcija.
Portal B objavljuje 10 videozapisa s prosjekom od 220 reakcija i 100 tekstova
s prosjekom od 60. Za A zato najprije računamo ukupne reakcije,
$100 \times 200 + 10 \times 50 = 20\,500$, pa dijelimo sa 110 objava.
Za B račun glasi $(10 \times 220 + 100 \times 60)/110$.
Ne dijelimo zbroj dvaju prosjeka s dva jer formati nemaju jednak broj objava.
B postiže bolji rezultat u svakom formatu, ali njegov
ukupni prosjek iznosi približno `r hr_broj(s1$b_zbirno, 0)`, naspram približno
`r hr_broj(s1$a_zbirno, 0)` reakcija po objavi na
portalu A.

Ukupni prosjek računamo preko svih objava, pa format s više objava ima veću
težinu. Videozapisi čine `r hr_broj(s1$udio_videa_a, 0)` % objava portala A i samo `r hr_broj(s1$udio_videa_b, 0)` %
objava portala B. A zato ima veći udio formata koji privlači više reakcija. Iz
njegova višeg ukupnog prosjeka ne možemo zaključiti da je bolji u svakom
formatu.

Podjela na podskupine mora odgovarati istraživačkom pitanju. Ako podatke
dijelimo na mnogo proizvoljnih načina, možemo naići na uvjerljiv obrazac koji
se u drugim podacima neće ponoviti. Zato prije tumačenja obrazlažemo zašto smo
odabrali baš tu podjelu.

Izbor prikaza ovisi o tvrdnji koju provjeravamo, načinu mjerenja, dizajnu i
podrijetlu podataka. Ako nas zanima odlučivanje unutar odjela, uspoređujemo
prijave unutar odjela. Ako želimo opisati ukupne ishode svih prijava,
koristimo zbirnu stopu. Usporedba mora odgovarati pitanju.

Pri tumačenju Simpsonova paradoksa zato trebamo znati kako su podaci
sastavljeni. Zaključak ograničavamo na usporedbu koju smo napravili.

## Interakcija — Simpsonov paradoks

Za sljedeći prikaz namjerno zadajemo stope, bez izvlačenja slučajnih ishoda.
U pristupačnijoj podskupini uspjeh je 80 % za A i 90 % za B, a u zahtjevnijoj
20 % i 30 %. U početnoj raspodjeli 80 % skupine A i 20 % skupine B pripada
pristupačnijoj podskupini. Ukupno za A dobivamo
$0,80 \times 0,80 + 0,20 \times 0,20 = 0,68$, a za B
$0,20 \times 0,90 + 0,80 \times 0,30 = 0,42$.
Promjenom rasporeda mijenjamo težine, dok četiri stope unutar podskupina
ostaju zadane.

Zastupljenost podskupina određuje koliko koja stopa pridonosi zbirnom
rezultatu. U tiskanom primjeru A ima četiri petine jedinica u
pristupačnijoj podskupini, a B samo jednu petinu. To je mehanizam obrata,
iako B postiže višu stopu u objema podskupinama.

| Skupina | Pristupačnija podskupina | Zahtjevnija podskupina |
|---|---:|---:|
| A | 80 % | 20 % |
| B | 20 % | 80 % |

: Sastav skupina u konstruiranom tiskanom primjeru. Izrada autora.

Sljedeći prikaz uspoređuje zbirne stope s usporedbama unutar podskupina.
Promatramo kako njihov različit sastav mijenja smjer zbirne razlike.

*Slika. Zbirne stope i stope po podskupinama u konstruiranom primjeru Simpsonova paradoksa.*

**Što isprobati.**

1. Najprije usporedite samo zbirne stope i zapišite koja skupina izgleda
   uspješnije.
2. Uključite prikaz podskupina i provjerite ostaje li smjer razlike jednak.
3. Promijenite zastupljenost podskupina bez mijenjanja njihovih stopa i
   promatrajte kada se zbirni zaključak preokrene.
4. Postavite obje zastupljenosti na istu vrijednost i provjerite je li obrat
   tada uopće moguć.

Kada su skupine jednako raspoređene po podskupinama, takav obrat nije moguć.
Zbirna usporedba tada zadržava smjer razlike unutar podskupina. Za obrat je
potreban i drukčiji sastav skupina, pa bez razdvajanja podataka ne možemo
odrediti koliko ukupnoj razlici pridonose stope uspjeha, a koliko
zastupljenost podskupina.

**Statistika u divljini.**
**Zbirna stopa i sumnja u pristranost.** Iza Berkeleyjske tablice stajalo
je pitanje o postupanju prema kandidatima, a ne samo zadatak računanja
postotaka. Niža ukupna stopa prijma žena potaknula je sumnju u upisni
postupak (Bickel, 1975). Bickel i suradnici zato su ispitali kako se prijave i odluke
raspoređuju po odjelima, koji su zasebno odlučivali o prijmu
(Bickel, 1975).

Vratimo se toj sumnji nakon prikaza obrata. Kada bismo sastavljali izvještaj
za nekoga tko treba provjeriti upisni postupak, zbirna stopa bila bi važan
početak. Pokazala bi razliku u ishodima svih zabilježenih prijava. No iz nje još ne bismo mogli utvrditi u kojem dijelu postupka nastaje
razlika. Za to
trebamo uz svaku stopu vidjeti koliko je prijava upućeno pojedinom odjelu i
koliko ih je prihvaćeno.

U izvornom slučaju žene su se češće prijavljivale na odjele koji su primali
manji udio kandidata obaju spolova (Bickel, 1975). Zato ukupni postotak
istodobno opisuje postupanje odjela i raspored prijava među njima.
Razdvajanjem tih sastavnica mijenja se ono što možemo tvrditi o radu
upisnih povjerenstava. Pritom ne nestaje pitanje zašto su prijave bile tako
raspoređene ni jesu li kandidati imali jednake mogućnosti prije prijave.

Dobar bi izvještaj zato zadržao oba pogleda. Zbirne stope pokazuju ukupnu
razliku u ishodima, a odjelne usporedbe približavaju nas odluci koja nas
zanima. Kad bismo prikazali samo prvi pogled, mogli bismo razliku
neopravdano pripisati povjerenstvima. Kad bismo prikazali samo drugi,
mogli bismo prerano zatvoriti pitanje nejednakosti.

Izbor usporedbe ovdje određuje što treba dalje istražiti. Prije nego što
stopu uspjeha pretvorimo u ocjenu ustanove, trebamo znati koje su odluke
ušle u njezin brojnik i kako su ljudi dospjeli u njezin nazivnik.

U našoj generiranoj populaciji isti se problem javlja pri usporedbi broja osoba
spremnih platiti vijesti i njihova udjela unutar izvora.

**Nađite grešku.**
U usporedbi izvora vijesti zanima nas koliko je njihovih korisnika
spremno platiti vijesti. Sljedeći izvadak iz poznate simulacije daje
brojnosti potrebne za provjeru asistentove bilješke (Šikić, 2026). Svaka
zamišljena osoba pripada samo jednom retku.

| Glavni izvor | Osobe | Spremni platiti |
|---|---:|---:|
| TV i radio zajedno | 16.666 | 4.301 |
| Tisak | 4.855 | 1.289 |

: Spremnost na plaćanje u dvjema odvojenim skupinama izvora. Izrada autora prema sikic2026.

> Među korisnicima tiska spremno je platiti 1.289 od 4.855 osoba, odnosno
> 26,55 %. Televizija i radio zajedno imaju 4.301 takvih osoba, više nego tisak. Prema tome,
> televizija i radio zajedno imaju veći udio osoba spremnih platiti.

Dopunite izvadak udjelom za televiziju i radio zajedno. Potom napišite dvije rečenice za
izvještaj, jednu o usporedbi brojeva i drugu o usporedbi udjela. Označite
koju rečenicu bilješke treba zamijeniti i objasnite zašto točan račun za
tisak nije dovoljan za njezin zaključak.

## Razrađeni primjer

Razliku između broja i udjela možemo provjeriti za sve izvore vijesti u
poznatoj autorskoj simulaciji od 50.000 osoba (Šikić, 2026). Za svaki izvor
pitamo koliki je udio njegovih korisnika spreman platiti vijesti. Jedinica
analize ostaje generirana osoba, a veličina skupine daje nazivnik. Time
povezujemo pitanje s računom koji na njega odgovara. Rezultat će opisivati
tu generiranu populaciju, bez objašnjenja uzroka razlika ili zaključka o
stvarnim ljudima.

Za svaki izvor tablica sadržava broj osoba, broj onih koji bi platili vijesti
i njihov udio. Stupac `Osobe` daje nazivnik, a `Spremni platiti` brojnik. Redoslijed
izvora određen je udjelom.

*Slika. Spremnost platiti prema glavnom izvoru vijesti u generiranoj populaciji. Izrada autora prema @sikic2026.*

Među osobama kojima je portal glavni izvor vijesti njih 3.514 spremno je
platiti vijesti, što je najveći broj među skupinama (Šikić, 2026). No ta je
skupina i najveća. Dijeljenjem s 15.101 dobivamo udio od 23,27 % (Šikić, 2026).
Za tisak dijelimo 1.289 s 4.855 i dobivamo 26,55 % (Šikić, 2026). Portal ima
više osoba spremnih platiti, a tisak njihov veći udio.

Pri tumačenju polazimo od toga da imamo cijelu generiranu populaciju. U
tih 50.000 zapisa nema nesigurnosti koja bi nastala odabirom uzorka
(Šikić, 2026). Ipak, ne znamo bi li pravilo kojim su podaci generirani bilo
korisno za neku drugu svrhu. Iz ovih udjela ne zaključujemo o stvarnoj
publici, uzrocima razlika ili odluci koju bi trebalo donijeti. Budući da ne
istražujemo uzrok, ne biramo ni među mogućim uzročnim objašnjenjima. Ovdje
pogrešno tumačenje ne pogađa stvarne ljude, ali u stvarnoj bi analizi zamjena
broja udjelom mogla usmjeriti resurse prema većoj skupini samo zbog njezine
veličine.

Zaključak stoga glasi da u generiranoj populaciji tisak ima najveći udio osoba
spremnih platiti vijesti, a portal najveći broj takvih osoba (Šikić, 2026). Pri
usporedbi udjela uzimamo u obzir veličinu svake skupine. Pri usporedbi brojeva
promatramo samo brojnike.

## Sažetak

Za razumijevanje broja trebamo znati odakle podaci dolaze, što predstavlja
jedinica analize i prema čemu računamo udio ili usporedbu. Te odluke pratimo
od postavljanja pitanja do uporabe rezultata. Šest revizijskih pitanja pomaže
prepoznati kada zaključak prelazi ono što smo doista provjerili. Simpsonov paradoks pokazuje
kako dvije točne usporedbe mogu dati različite odgovore jer se odnose na
različita pitanja. Statistika, podatkovna znanost, strojno učenje i sustavi
umjetne inteligencije pridonose tom radu različitim postupcima. Koliko će
zaključak biti koristan ovisi već o izboru onoga što mjerimo i o istraživačkom
dizajnu.

## Pojmovi

zbirna stopa (*aggregate rate*), signal (*signal*), šum (*noise*),
brojnik (*numerator*), šest revizijskih pitanja (*six audit questions*),
jedinica analize (*unit of analysis*), nazivnik (*denominator*), Simpsonov
paradoks (*Simpson's paradox*), životni ciklus podataka (*data lifecycle*),
statistika (*statistics*), podatkovna znanost (*data science*), strojno učenje
(*machine learning*), sustav umjetne inteligencije (*artificial intelligence
system*)

## Zadaci

### Konceptualni

Objasnite kako dvije računski točne stope mogu poduprijeti različite zaključke.
U odgovoru razlikujte zbirnu usporedbu od usporedbe unutar podskupina te
imenujte jedinicu i nazivnik svake usporedbe.

Odaberite dvije faze životnog ciklusa podataka. Za svaku u kratkom odlomku
opišite jednu pogrešku koju kasniji izračun ne može sam popraviti. Nije
potrebno predlagati programski kod.

Za svaki od sljedećih zadataka odredite pripada li ponajprije statistici,
podatkovnoj znanosti, strojnom učenju ili radu sa sustavom umjetne
inteligencije. Zadaci su provjera zaključka koji podaci podupiru, izrada
ponovljivog postupka od izvora do tablice, provjera predviđanja na novim
opažanjima i praćenje preporučivačkog sustava nakon uvođenja u ustanovu. Svaki
izbor obrazložite jednom rečenicom.

### Računski

Upotrijebite tablicu spremnosti na plaćanje. Za portal i tisak ručno
podijelite vrijednost `Spremni platiti` s vrijednošću `Osobe` te rezultat
pretvorite u postotak. Predajte dva razlomka, dva postotka i jednu rečenicu koja
objašnjava zašto portal ima veći broj, a tisak veći udio. Zatim usporedite tisak
s društvenim mrežama i razliku zaokružite na dvije decimale (Šikić, 2026).

U simulaciji su stope skupine A u pristupačnijoj i zahtjevnijoj podskupini 80 %
i 20 %, a stope skupine B 90 % i 30 %. Pretpostavite da obje skupine imaju po
50 % jedinica u svakoj podskupini. Izračunajte dvije zbirne stope i objasnite
zašto obrata nema. U digitalnom izdanju rezultat možete provjeriti widgetom.

### Kritički

Pronađite medijsku tvrdnju koja uspoređuje dvije skupine jednim zbirnim
brojem. Navedite tvrdnju, izvor i nazivnik pa odgovorite na svih šest revizijskih pitanja, na svako jednom rečenicom. Označite i pitanja na koja objava ne
daje odgovor. Na kraju procijenite podupire li broj opis, povezanost,
generalizaciju, predviđanje, uzročnost ili odluku.

### Revizija modela

Provjerite bilješku asistenta uz tablica Navedite točne brojnike i nazivnike,
izdvojite pogrešnu rečenicu i napišite ispravnu. Objasnite zašto se ni
ispravljena analiza ne može primijeniti na stvarne stanovnike Hrvatske.
