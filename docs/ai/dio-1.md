# DIO I: STATISTIČKO MIŠLJENJE

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Zašto statistika

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/01-zasto-statistika.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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
kod same usporedbe (Bickel, 1975). Zapisi su nastali u postupku prijave na studij i čuvaju stvarni sastav prijava po odjelima (Bickel, 1975). Prije odluke o tome što razlika znači
trebamo znati koga uspoređujemo, što je zabilježeno i prema kojoj cjelini
računamo postotak. To su pitanja od kojih ćemo krenuti, bez pretpostavke da
već poznajemo statističke postupke.

U knjizi ćemo učiti pratiti put od istraživačkog pitanja do zaključka. Račun
će nam pomoći opisati podatke, usporediti skupine i procijeniti nesigurnost,
ali morat ćemo odlučiti odgovara li na pitanje koje smo postavili. Za početak
su nam dovoljni poznati postoci, jednostavne tablice i spremnost da provjerimo
što stoji iza broja. U središtu je sposobnost da objasnimo zašto smo nešto podijelili, koga smo izostavili i dokle dobiveni odgovor vrijedi. To možemo vježbati uz prikazane račune.

Uz stvarne prijave na studij koristit ćemo i skup podataka o medijskim
navikama stanovnika zamišljenoga grada, nazvan `populacija_medija`.
Stvorili smo ga računalnom simulacijom. Svaki redak njegove tablice opisuje
jednu zamišljenu odraslu osobu. U prvom ćemo
računu povezati njezin glavni izvor vijesti sa spremnošću na plaćanje vijesti.
Usporedit ćemo broj osoba koje bi platile s njihovim udjelom unutar pojedinog
izvora. Tako možemo pratiti svaki korak na populaciji čiji su odnosi unaprijed zadani.

Prijave na studij i spremnost na plaćanje vijesti različite su pojave, ali
pred nas postavljaju sličan problem. Broj dobiva značenje tek kada znamo koje
je ljude ili prijave obuhvatio i s čime ih uspoređujemo. Dok pratimo te
usporedbe, razlikovat ćemo ono što podaci već pokazuju od onoga za što nam
treba dodatno objašnjenje. Tu razliku tražimo i kada čitamo istraživanje,
medijski naslov ili odgovor asistenta.

## Broj nije zaključak

Zbirna stopa govori tko je češće primljen među svim prijavljenim kandidatima.
Stope po odjelima govore kako su prolazili kandidati koji su se prijavili na
isti odjel. Izbor usporedbe ovisi o pitanju koje istražujemo. Računom zatim provjeravamo rezultat te odabrane usporedbe.

Da bismo procijenili pravednost upisa, morali bismo poznavati i kriterije
odlučivanja te okolnosti koje tablica ne bilježi. Zasad možemo provjeriti kako
raspored prijava i veličina skupina mijenjaju značenje izračuna.

**Statistika** povezuje istraživačko pitanje s podacima i zaključkom koji iz
njih možemo izvesti. Uz račun provjeravamo što je izmjereno i jesu li skupine
koje uspoređujemo prikladne za naše pitanje. Pogreška u tom izboru može
dovesti do pogrešnog zaključka i kada u računanju nema propusta.

Najprije utvrđujemo što predstavlja jedan zapis. U zbirnoj tablici prijava
redak opisuje više prijava iste vrste. U tablici pojedinačnih odgovora redak
može opisivati jednu osobu. Veza između broja redaka i broja ljudi, događaja ili neovisnih opažanja ovisi o načinu bilježenja podataka.

**Jedinica analize** je ono o čemu donosimo zaključak, primjerice osoba,
kućanstvo, organizacija ili objava. Jedan redak tablice ne mora predstavljati
jednu neovisnu jedinicu.

Ako istu osobu pitamo za mišljenje svakoga od sedam dana, dobivamo sedam zapisa o jednoj osobi. Njezini odgovori mogu biti slični upravo zato što potječu od iste osobe. Pri zaključivanju zato tih sedam redaka promatramo kao ponovljena opažanja unutar iste jedinice.

**Podsjetnik.** Postotci i postotni bodovi

U skupu `populacija_medija` imamo zapise za 50.000 zamišljenih odraslih
stanovnika. Uz izvor vijesti i spremnost na plaćanje, za svaku su
osobu zabilježeni dob, obrazovanje, povjerenje u medije na ljestvici od 1
do 10 i dnevno praćenje medija. Istom ćemo
se populacijom služiti pri uzorkovanju, usporedbama skupina i regresiji, kako
bismo nove postupke mogli pratiti na poznatom primjeru.

Računalno stvaranje tih zapisa slijedi zadana pravila. Najprije nastaju dob
i izvor vijesti, čije se vjerojatnosti mijenjaju s dobi. Povjerenje ovisi o
dobi i izvoru uz slučajno odstupanje, a spremnost na plaćanje o povjerenju i
obrazovanju. Tako nastaju namjerno povezane varijable. Jedna osoba može
odstupati od zadanoga obrasca, a cjelina od 50.000 osoba pokazuje obrazac koji
je autor ugradio u generator. Ti zapisi ne opisuju stvarne stanovnike.

Prva tri retka pokazuju kako taj skup izgleda prije sažimanja. Svaki redak
čuva više obilježja iste zamišljene osobe.

*Slika. Tri zapisa iz generirane populacije medijskih navika. Izrada autora.*

Broj osobe služi povezivanju njezinih odgovora. Vrijednost u stupcu izvora
vijesti jedna je kategorija, povjerenje je ocjena, a spremnost na plaćanje
u ovoj je tablici prikazana odgovorom da ili ne.
Grafom prikazujemo te zapise, a uzorkovanjem odabiremo dio njih. U oba postupka zadržavamo podatak o tome kako su nastali.

Iz takvih zapisa možemo prebrojiti osobe spremne platiti vijesti. Želimo li
usporediti izvore s različitim brojem korisnika, trebamo i **nazivnik**,
količinu s kojom dijelimo brojnik. Brojnik je broj slučajeva koji
zadovoljavaju uvjet, ovdje osoba spremnih platiti vijesti.
Među 4.855 osoba kojima je tisak glavni izvor vijesti njih 1.289 spremno je
platiti vijesti. Među 15.101 korisnikom portala spremnih je 3.514. U većoj skupini takvih osoba ima više, ali tek dijeljenjem
možemo usporediti udjele. Jednako treba znati prema kojoj količini računamo
stopu ili prosjek.

Provjeravamo i **podrijetlo podataka**. Treba znati tko ih je proizveo, kojim
postupkom, koju inačicu koristimo i koja su njezina ograničenja. Za naš je
nastavni skup poznat postupak stvaranja i njegovo sjeme, početna postavka koja
omogućuje ponavljanje iste simulacije. Zato možemo provjeriti
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
naučen iz jednih podataka djeluje na novim opažanjima. Takav pristup stavlja uspješnost predviđanja u prvi plan, dok je drugi
pristup modeliranju više usmjeren na objašnjenje odnosa (Breiman, 2001). **Sustav umjetne inteligencije**
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
vijestima bave više od drugih pa su zato i isprobali aplikaciju. Sklonost da učestalost procjenjujemo prema tome koliko se lako prisjetimo
nekog primjera poznata je kao heuristika dostupnosti (Tversky, 1973). Živopisan ili nedavan slučaj tako može ostaviti pretjerano
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

Provjera obuhvata potrebna je i pri velikom broju zapisa. Milijuni interakcija na portalu opisuju zabilježene aktivnosti njegovih posjetitelja. Za upoznavanje ostale publike trebalo bi prikupiti dodatne podatke.
Odgovori većega broja zasebno odabranih ljudi obično daju stabilniji
postotak od odgovora male skupine. Korist je manja kada se isti odgovori ponavljaju, a sustavno izostavljen dio publike ostaje izvan obuhvata.

Unatoč tim ograničenjima možemo donositi korisne zaključke. Statistički
postupci, kada su njihove pretpostavke opravdane, omogućuju da izračunamo dio
nesigurnosti. Mjerenje, odabir sudionika i promjenu okolnosti moramo zasebno procijeniti. Tako možemo obrazložiti što zaključujemo i zašto zaključak
ograničavamo na određene uvjete.

## Signal u promjenjivom svijetu

I unutar dobro odabrane usporedbe opažanja se međusobno razlikuju.
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

Povezanost korištenja društvenih mreža i praćenja vijesti procjenjujemo usporedbom većeg broja studenata. Navike pojedinog studenta mogu se uklapati u zajednički obrazac ili odstupati od njega. Osoba je jedinica analize, a obrazac opisuje odnos u promatranoj skupini.

Važni su i broj opažanja i način na koji su nastala. Uz isti postupak
prikupljanja i dovoljno neovisne jedinice, razlika među desetak ljudi lakše
može nastati slučajnim rasipanjem nego jednaka razlika među tisućama.
Ponavljanje istih zapisa ili dodavanje snažno povezanih opažanja donosi manje nove informacije nego uključivanje dodatnih neovisnih jedinica.

Za tumačenje rasta, pada ili razlike trebamo znati s čime uspoređujemo
rezultat. To može biti druga skupina, ranije razdoblje ili raspon vrijednosti
koje bi nastale slučajnom promjenjivošću.  Najprije treba jasno imenovati obje strane usporedbe.

## Razlika koju čini postupak

Imenovanje obiju strana usporedbe pomaže nam odrediti i kakav zaključak
tražimo. Opis govori što smo zabilježili, a
povezanost kako se pojave mijenjaju zajedno. Generalizacijom nalaz prenosimo
na jedinice koje nismo promatrali. Predviđanjem procjenjujemo nove ishode, dok
uzročna tvrdnja govori što bi određena promjena proizvela. Odluka uz nalaz
uključuje i procjenu mogućih postupaka te njihovih posljedica. Prijelaz od opisa podataka do uzročnog zaključka traži dodatno obrazloženje načina na koji je usporedba nastala.

Za isti skup podataka možemo postaviti različita pitanja. Sljedećim zamišljenim formulacijama ilustriramo vrste tvrdnji.

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
pretpostavka traži najviše provjere. Tako drugi mogu razumjeti na čemu zaključak počiva, provjeriti ga i uočiti moguću pogrešku.

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

*Slika. Prijave i prijam u šest najvećih odjela Berkeleyja 1973. Podaci UCBAdmissions prema @bickel1975. Postoci izračunati iz prikazanih brojnosti.*

U odjele A i B, koji imaju visoke stope prijma, prijavilo se
`r sum(berkeley1$Prijave[berkeley1$Gender == "Male" & berkeley1$Dept %in% c("A", "B")])`
od `r sum(berkeley1$Prijave[berkeley1$Gender == "Male"])` muškaraca iz ovoga
podskupa, a samo
`r sum(berkeley1$Prijave[berkeley1$Gender == "Female" & berkeley1$Dept %in% c("A", "B")])`
od `r sum(berkeley1$Prijave[berkeley1$Gender == "Female"])` žena (Bickel, 1975).
Razlikuju se i stope unutar odjela i udjeli prijava usmjerenih u pojedine
odjele. Zbirni postotak uključuje oboje. Tablica sama ne objašnjava
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
Pri računanju svaki prosjek važemo brojem objava pripadajućeg formata.
B postiže bolji rezultat u svakom formatu, ali njegov
ukupni prosjek iznosi približno `r hr_broj(s1$b_zbirno, 0)`, naspram približno
`r hr_broj(s1$a_zbirno, 0)` reakcija po objavi na
portalu A.

Ukupni prosjek računamo preko svih objava, pa format s više objava ima veću
težinu. Videozapisi čine `r hr_broj(s1$udio_videa_a, 0)` % objava portala A i samo `r hr_broj(s1$udio_videa_b, 0)` %
objava portala B. A zato ima veći udio formata koji privlači više reakcija. Viši ukupni prosjek ovdje proizlazi iz sastava objava, dok usporedbu uspješnosti po formatu čitamo iz zasebnih prosjeka.

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

Kada su skupine jednako raspoređene po podskupinama, zbirna usporedba zadržava smjer razlike unutar podskupina. Za obrat je potreban drukčiji sastav skupina. Razdvajanjem podataka možemo utvrditi koliko ukupnoj razlici pridonose stope uspjeha, a koliko zastupljenost podskupina.

**Statistika u divljini.**
**Zbirna stopa i sumnja u pristranost.** Iza Berkeleyjske tablice stajalo
je pitanje o postupanju prema kandidatima, a ne samo zadatak računanja
postotaka. Niža ukupna stopa prijma žena potaknula je sumnju u upisni
postupak (Bickel, 1975). Istraživanje se zato usmjerilo na pitanje kako su se prijave i odluke
raspoređivale po odjelima, jer je svaki odjel zasebno odlučivao o prijmu
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
upisnih povjerenstava. Otvorenima ostaju pitanja zašto su prijave bile tako raspoređene i jesu li kandidati imali jednake mogućnosti prije prijave.

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
brojnosti potrebne za provjeru asistentove bilješke. Svaka
zamišljena osoba pripada samo jednom retku.

| Glavni izvor | Osobe | Spremni platiti |
|---|---:|---:|
| TV i radio zajedno | 16.666 | 4.301 |
| Tisak | 4.855 | 1.289 |

: Spremnost na plaćanje u dvjema odvojenim skupinama izvora. Izrada autora.

> Među korisnicima tiska spremno je platiti 1.289 od 4.855 osoba, odnosno
> 26,55 %. Televizija i radio zajedno imaju 4.301 takvih osoba, više nego tisak. Prema tome,
> televizija i radio zajedno imaju veći udio osoba spremnih platiti.

Dopunite izvadak udjelom za televiziju i radio zajedno. Potom napišite dvije rečenice za
izvještaj, jednu o usporedbi brojeva i drugu o usporedbi udjela. Označite
koju rečenicu bilješke treba zamijeniti i objasnite zašto točan račun za
tisak nije dovoljan za njezin zaključak.

## Razrađeni primjer

Razliku između broja i udjela možemo provjeriti za sve izvore vijesti u
istom simuliranom skupu podataka `populacija_medija`. Za svaki izvor
pitamo koliki je udio njegovih korisnika spreman platiti vijesti. Jedinica
analize ostaje zamišljena osoba, a veličina skupine daje nazivnik. Time
povezujemo pitanje s računom koji na njega odgovara. Rezultat će opisivati
tu generiranu populaciju, bez objašnjenja uzroka razlika ili zaključka o
stvarnim ljudima.

Za svaki izvor tablica sadržava broj osoba, broj onih koji bi platili vijesti
i njihov udio. Stupac `Osobe` daje nazivnik, a `Spremni platiti` brojnik. Redoslijed
izvora određen je udjelom.

*Slika. Spremnost platiti prema glavnom izvoru vijesti u generiranoj populaciji. Izrada autora.*

Među osobama kojima je portal glavni izvor vijesti njih 3.514 spremno je
platiti vijesti, što je najveći broj među skupinama. No ta je
skupina i najveća. Dijeljenjem s 15.101 dobivamo udio od 23,27 %.
Za tisak dijelimo 1.289 s 4.855 i dobivamo 26,55 %. Portal ima
više osoba spremnih platiti, a tisak njihov veći udio.

Pri tumačenju polazimo od cijele generirane populacije od 50.000 zapisa, pa udjele poznajemo točno za taj skup. Njihov se doseg završava opisom simulacije. Primjena na stvarnu publiku zahtijevala bi stvarne podatke i provjeru prikladnosti postupka, a objašnjenje uzroka odgovarajući istraživački dizajn. Nastavni primjer omogućuje da razmotrimo i posljedice tumačenja. U stvarnoj bi analizi zamjena broja udjelom mogla usmjeriti resurse prema većoj skupini samo zbog njezine veličine.

Zaključak stoga glasi da u generiranoj populaciji tisak ima najveći udio osoba
spremnih platiti vijesti, a portal najveći broj takvih osoba. Pri
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
s društvenim mrežama i razliku zaokružite na dvije decimale.

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

---

# Mjerenje i istraživački dizajn

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/02-mjerenje-i-dizajn.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Koliko ste vremena jučer proveli na mobitelu? Prije nego što pogledate
zapis uređaja, pokušajte procijeniti. Možda se sjećate dugog razgovora, a
teže prizivate kratka provjeravanja poruka između drugih obveza. I što
biste ubrojili u odgovor, razgovor s prijateljem, slušanje glazbe sa
zaključanim zaslonom ili samo vrijeme dok gledate u njega?

Sličan se problem pojavljuje u istraživanjima digitalnih medija. Sustavni
pregled usporedio je samoprocjene uporabe sa zapisima uređaja i aplikacija,
a pokazalo se da se ta dva načina mjerenja često razilaze (Parry, 2021).
Za istraživača koji vrijeme uz ekran želi povezati s učenjem ili
zadovoljstvom životom to je važno već prije prvog računa.

Ako se vaša procjena i zapis uređaja razlikuju, koji broj odgovara onome
što zapravo želite saznati o svojem danu?

Broj minuta dobiva značenje tek kada odredimo koje aktivnosti obuhvaća.
Povjerenje u medije možemo pokušati mjeriti anketnim odgovorom, a izloženost
medijima vremenom provedenim uz sadržaj. Prije nego što usporedimo takve
brojeve, moramo odlučiti što bi oni trebali predstavljati. Ako dvije osobe pod povjerenjem razumiju različite stvari, njihovi uredno zabilježeni odgovori mogu predstavljati različite pojave. U ovom ćemo poglavlju istražiti kako od društvenog
pitanja dolazimo do opažanja koja na njega mogu odgovoriti.

U poglavlju o statističkom mišljenju tražili smo jedinicu analize, nazivnik i
podrijetlo podataka. Sada se vraćamo korak prije gotove tablice. Odredit ćemo
koje obilježje bilježimo, kojim pitanjem ili postupkom i prema kojim pravilima
osoba ili zapis ulazi u istraživanje. Razlikovat ćemo mjerenje koje daje
dosljedne rezultate od mjerenja koje dobro obuhvaća pojavu koja nas zanima. To
će nam pomoći procijeniti što smijemo uspoređivati i prije nego što odaberemo
račun.

Mjerenje ćemo proučiti na primjerima anketnih pitanja, bilježenja ponašanja
i usporedbi eksperimentalnih uvjeta. U razrađenom primjeru sastavit ćemo mjeru povjerenja
u lokalne institucije od konstruiranih tvrdnji i odgovora. Jedan redak toga
nastavnog primjera predstavlja zamišljenog ispitanika, a stupci njegove
odgovore. Provjerit ćemo znače li viši odgovori na svim tvrdnjama doista više
povjerenja, prije nego što ih spojimo u zajednički rezultat.

Uz mjerenje ćemo ispitati i istraživački nacrt. Usporedba ljudi koji su sami
odabrali neku aktivnost razlikuje se od pokusa u kojem im nasumično
dodjeljujemo uvjete. Simulirani primjer pokazat će kako treći čimbenik može
promijeniti tumačenje veze. Pri čitanju istraživanja moći ćemo obrazložiti što
podaci govore o promatranim osobama, što bi opravdalo uzročni zaključak i na
koga bi se on mogao odnositi.

## Od pojma do podatka

Povjerenje, političku otuđenost ili osjećaj sigurnosti proučavamo putem odabranih opažanja. Zato najprije određujemo po čemu ćemo te pojave prepoznati. Isto vrijedi i za naizgled jednostavan pojam poput
izloženosti medijima.

**Operacionalizacija** je postupak kojim određujemo kako ćemo mjeriti
teorijski pojam. Navodimo što ćemo opažati i po kojem ćemo pravilu svakom
opažanju pridružiti vrijednost.

Za povjerenje u medije mogli bismo postaviti jedno anketno pitanje, sastaviti
nekoliko tvrdnji ili promatrati izbor izvora vijesti. Time bismo dobili
različite moguće pokazatelje, čiju vezu s povjerenjem tek treba opravdati.
Uz odgovore i zabilježeno ponašanje možemo
koristiti i procjenu promatrača, ali svaki od tih izbora obuhvaća neki dio
pojave, a druge dijelove izostavlja.

Kada koristimo više tvrdnji, njihove odgovore možemo sažeti u jedan rezultat.
Tako pojedina formulacija manje utječe na ukupnu mjeru, koja može postati
dosljednija. Dobiveni rezultat tumačimo prema sadržaju svih uključenih tvrdnji, kao zajedničku mjeru.

Povjerenje u medije, primjerice, razlikuje se od odgovora na pitanje koliko
netko vjeruje nekom izvoru na ljestvici od 1 do 10. Odgovor je nesavršena
mjera povjerenja. Kvaliteta istraživanja ovisi o tome koliko dobro ta mjera
odgovara pojmu koji proučavamo. I uz kvalitetan instrument mjera ostaje odabrani prikaz širega pojma.

Zamislimo dva istraživanja društvenih mreža i političke polarizacije. Jedno
polarizaciju mjeri razlikama u stavovima pristaša stranaka, a drugo
učestalošću neprijateljskih izjava o protivnicima. Njihovi se nalazi mogu
razlikovati jer prvo prati udaljenost mišljenja, a drugo ton rasprave. Prije
usporedbe zaključaka treba provjeriti jesu li istraživači doista mjerili istu
pojavu.

Ono što mjerimo bilježimo kao opažanje, a svojstvo koje može imati različite
vrijednosti nazivamo **varijablom**. Ako 300 ljudi upitamo koliko minuta
dnevno provode na mrežama, imamo 300 opažanja jedne varijable. Postavimo li
svakome 10 pitanja, imamo 300 opažanja za svaku od 10 varijabli. Odabirom
pitanja određujemo koje ćemo razlike među ljudima moći proučavati.

Te odluke donosimo prije prikupljanja podataka. Ljestvica s pet stupnjeva čuva odgovore u pet ponuđenih kategorija. Za razlikovanje deset stupnjeva trebalo bi primijeniti drukčiju ljestvicu. Usporedba grada i sela zahtijeva zabilježeno mjesto stanovanja. Mogućnosti analize ovise o onome što smo prikupili.

Pri čitanju istraživanja zato najprije tražimo opis mjerenja i jedinicu
analize. Treba znati odnosi li se nalaz na osobu, objavu, kućanstvo ili,
primjerice, sat gledanja. Metodološki odjeljak objašnjava i što odabrana mjera
obuhvaća, a što izostavlja. Puno značenje varijable dobivamo iz toga opisa.

U anketi na mjerenje utječu formulacija, ponuđeni odgovori i redoslijed
pitanja. Zamislimo osobu koja je upravo odgovorila na niz pitanja o
nesigurnosti. Ona bi povjerenje u institucije mogla procijeniti drukčije nego
da joj je to pitanje postavljeno prvo. Zato uz rezultate treba pročitati i
upitnik.

## Prihvatljivost, isključenja i filtri

Uz odluku što pitamo, trebamo odrediti i kome pitanje postavljamo. Ista mjera
primijenjena na drukčiji krug ljudi može dati drukčiju sliku pojave. **Prihvatljivost** je pravilo po
kojem jedinica pripada ciljanoj skupini. Isključenje je obrazložen razlog da
neku inače prihvatljivu jedinicu ipak ne analiziramo. Filtrom ta pravila
primjenjujemo na zapise. Time određujemo na koju će se populaciju moći
odnositi zaključak.

Na turizmu možemo vidjeti kako nastaju različite mjere iste šire pojave.
U lokalnom administrativnom izvatku Državnog zavoda za statistiku (DZS) za
`r s2_dzs_dolasci$godina`. domaćim turistima pripada
`r hr_broj(s2_dzs_dolasci$dolasci, 0)` dolazaka u komercijalni smještaj
(statistiku}, 2026). Izvadak anketne tablice T03 za istu godinu daje procjenu od
`r hr_broj(s2_dzs_putovanja$putovanja, 0)` privatnih putovanja s noćenjem
unutar Hrvatske (statistiku}, 2026). Anketa obuhvaća stanovnike od
`r s2_dzs_dob_min` godina naviše u privatnim kućanstvima, a putovanja uključuju
i nekomercijalni smještaj (statistiku}, 2025). Dolazak nastaje prijavom u smještaj,
pa promjena objekta može istoga gosta ponovno ubrojiti (statistiku}, 2026).
Brojevi zato opisuju različite jedinice i obuhvate. Prije usporedbe trebamo
zapisati koji se događaj broji, koga izvor obuhvaća i kako podatak nastaje.

Zamislimo plan istraživanja televizijskih vijesti o prosvjedu. To je primjer
planiranja, bez stvarnog nalaza. Ovisno o pitanju, možemo proučavati priloge,
govorne iskaze ili pojedine riječi. U istraživanje bismo mogli uključiti sve
priloge odabranih informativnih emisija u unaprijed određenom razdoblju. Ako
isključimo reprize, priloge bez govora ili nečitljive zapise, trebamo
zabilježiti koliko ih je isključeno i zašto. Zaključak će se odnositi na tako
sužen skup.

Nedostajući odgovor razlikuje se od isključenja osobe. Sudionik koji preskoči
jedno pitanje i dalje pripada istraživanju, ali za tu varijablu nemamo
vrijednost. Ako zbog toga izbrišemo cijeli redak, uvodimo dodatni filtar. To
može promijeniti rezultat, osobito kada preskakanje pitanja ovisi o iskustvu
koje proučavamo. Zato zasebno bilježimo neprihvatljive jedinice, opravdana
isključenja i nedostajuće vrijednosti uključenih jedinica.

Za analizu jezika također trebamo mjerno pravilo. **Kodiranje kao mjerenje**
određuje kojoj izjavi pripada koja oznaka, što ne kodiramo i kako rješavamo
dvosmislene slučajeve. U našem primjeru oznaku pripisivanja odgovornosti mogli
bismo dati samo izjavi koja jasno imenuje aktera i radnju. Neizravna naznaka
mogla bi dobiti oznaku nejasno. Isključimo li takve izjave, dobiveni udio
opisivat će samo jednoznačne iskaze.

Slaganje dvaju kodera pokazuje koliko dosljedno primjenjuju pravilo, odnosno
njegovu pouzdanost. Zasebno provjeravamo prepoznaje li to pravilo doista
pripisivanje odgovornosti, što je pitanje valjanosti. Dvosmisleni slučajevi
pomažu uočiti ograničenja mjere. I etička pravila mogu suziti podatke kojima
raspolažemo. Zaštita sudionika može opravdati izostavljanje osjetljivih
zapisa, ali u izvještaju treba objasniti tko je time izostao i kako to
ograničava zaključak.

Kad nekoga pozovemo u istraživanje, tražimo da nam povjeri dio svojega
iskustva. Prije nego što pristane, treba razumjeti čemu istraživanje služi,
što ćemo ga pitati, može li mu sudjelovanje biti neugodno i tko će vidjeti
njegove odgovore. Objašnjavamo i kako može odustati. Ako poziv dolazi od
nastavnika ili poslodavca, posebno pazimo da osoba može slobodno odbiti,
bez osjećaja da mora sudjelovati. Prije početka provjeravamo i koja
odobrenja i posebne uvjete traži naša ustanova.

Povjerenje te osobe trebamo sačuvati i nakon što ispuni upitnik.
Uklonimo li ime, još uvijek može ostati prepoznatljiva. Zamislimo da u
tablici pišu njezina dob, malo mjesto u kojem živi i rijetko zanimanje.
Netko tko poznaje to mjesto mogao bi povezati odgovore s njom. Zato već pri
sastavljanju upitnika razmišljamo koji su nam podaci doista potrebni,
tko će im moći pristupiti, kako ćemo ih čuvati i kada izbrisati.

Ponekad ime zamijenimo šifrom, a zasebno čuvamo ključ koji ih povezuje.
Taj postupak zovemo pseudonimizacijom. On skriva ime u radnoj tablici,
ali onaj tko ima ključ i dalje može prepoznati osobu. I prije dijeljenja
zbirne tablice trebamo pogledati krije li se iza neke male skupine samo
jedna prepoznatljiva osoba. Ako je ne možemo dovoljno zaštititi, biramo
sigurniji način dijeljenja ili prikazujemo podatke za veće skupine.
Na to mislimo i kad tražimo pomoć asistenta, jer slanjem tablice također
otvaramo pristup odgovorima koje nam je netko povjerio.

## Razine mjerenja

Kada svakom opažanju pridružimo vrijednost, još trebamo znati što s tim
vrijednostima možemo smisleno uspoređivati. Oznakom izvora vijesti razlikujemo kategorije, a brojem minuta mjerimo trajanje uporabe. Uobičajena podjela na četiri razine mjerenja razlikuje oznake,
poredak, jednake razmake i smislenu nulu (Stevens, 1946). Ta nam podjela pomaže razumjeti
varijablu, premda sama ne određuje sve dopuštene analize.

Vrsta medija, država prebivališta, stranačka bliskost i status zaposlenosti
imaju kategorije bez zadanog poretka. To je **nominalna razina**. Na
**ordinalnoj razini** vrijednosti možemo poredati, ali razmaci među njima ne
moraju biti jednaki. **Intervalna razina** ima jednake razmake uz proizvoljno
ishodište, a **omjerna razina** uz to ima apsolutnu nulu. Zato možemo odrediti
medijan, srednji odgovor po poretku, ali ne i smislen prosjek vrsta medija. Izjava da je
nešto dvostruko veće odgovara omjernim varijablama poput vremena, broja
dijeljenja ili dohotka.

Ljestvica slaganja ima poredak. Kada odgovore zbrajamo ili računamo prosjek,
pretpostavljamo da razmake među stupnjevima možemo tumačiti brojčano. Spajanje
više tvrdnji može povećati dosljednost, ali ne jamči jednake razmake. Ako ta
pretpostavka utječe na zaključak, rezultat treba usporediti s prikazom koji
koristi samo poredak. Razliku od dvije desetine boda tako tumačimo uz
pretpostavku o ljestvici.

Varijable mogu biti i diskretne ili kontinuirane. Diskretna varijabla ima
odvojene moguće vrijednosti. Broj komentara, primjerice, poprima cjelobrojne vrijednosti. Kontinuirana varijabla poput vremena na stranici može poprimiti bilo
koju vrijednost unutar raspona. Ta razlika utječe na izbor grafa i analize.
Diskretne varijable s mnogo mogućih vrijednosti, poput broja bodova na nekim
testovima, u praksi se katkad analiziraju kao kontinuirane.

Sažimanjem podataka zadržavamo odabranu razinu pojedinosti. Dob u godinama možemo razvrstati u dobne skupine. Nakon takva razvrstavanja sama oznaka skupine govori samo raspon dobi. Isto vrijedi za pretvaranje minuta uporabe u kategorije čestih i
rijetkih korisnika. Ako anketa od početka nudi samo razrede, točne vrijednosti
ostaju nepoznate.

Mjerenje zato planiramo prema istraživačkom pitanju i čuvamo potrebne
pojedinosti. Za izbor analize zatim uz razinu mjerenja razmatramo dizajn,
raspodjelu podataka, način izgradnje ljestvice i pretpostavke postupka.
Podjela na razine mjerenja pruža polazište za tu širu prosudbu.

## Pouzdanost i valjanost

Uz razinu mjerenja procjenjujemo i kvalitetu mjere. Od nje očekujemo dosljednost i smislen sadržaj. Vaga koja pri uzastopnom
vaganju iste osobe pokazuje različite težine upozorava na problem
dosljednosti.

**Pouzdanost** je stupanj u kojem instrument daje dosljedne rezultate pri
ponovljenom mjerenju istog stanja u istim uvjetima.

Pouzdanost mjerenja razlikuje se od razine pouzdanosti intervala koju ćemo
upoznati u poglavlju o procjeni. Prva opisuje dosljednost instrumenta,
a druga svojstvo postupka intervalne procjene.

Pouzdanost provjeravamo na nekoliko načina. Pri ponovljenom mjerenju
uspoređujemo rezultate istog instrumenta u dva trenutka, pod pretpostavkom da
se mjereno stanje nije promijenilo. Kada ljudi kodiraju tekstove, provjeravamo
njihovo međusobno slaganje. Kod ljestvice s više tvrdnji koje mjere isti pojam
provjeravamo internu konzistentnost, odnosno koliko se odgovori na te tvrdnje
slažu. Za nju se može navesti Cronbachov alfa, a za slaganje kodera Cohenova
kappa ili Krippendorffova alfa. Uobičajene granice prihvatljivosti dogovorene
su konvencije o kojima se raspravlja, pa ih treba tumačiti u kontekstu
mjerenja.

U radu s višestavčanom ljestvicom zato tražimo prikladnu mjeru interne
konzistentnosti. U analizi sadržaja tražimo mjeru slaganja kodera i broj
jedinica na kojima je izračunata. Indeks koji namjerno spaja različite
sastavnice može zahtijevati drukčiju provjeru. Kad izvještaj izostavi te podatke, dosljednost mjerenja ostaje otvoreno pitanje koje traži dodatnu provjeru.

Razlika između ponovljenih mjerenja može nastati i zbog stvarne promjene.
Nakon velikog medijskog skandala povjerenje u medije moglo bi pasti i uz posve
pouzdan instrument. Da bismo razlikovali promjenu stavova od nestabilnosti
mjere, moramo poznavati događaje između dvaju mjerenja.

Dosljedan rezultat vrijedi nam samo ako mjeri pojam koji istražujemo.

**Valjanost** je stupanj u kojem instrument mjeri upravo onaj pojam o kojem
se namjerava zaključivati, a ne neki drugi s kojim je povezan.

Kad bismo kvalitetu novinarstva mjerili brojem zareza, različiti bi brojači
mogli dobiti isti rezultat. Mjera bi bila pouzdana, ali ne bi valjano mjerila
kvalitetu novinarstva. Pouzdanost je zato potreban, ali nedovoljan uvjet dobre
mjere.

Mjerna pogreška može utjecati i na procijenjenu povezanost. Ako su slučajne
pogreške dviju mjera približno neovisne i ne ovise o skupini ni ishodu,
opažena veza može biti slabija od veze među samim pojmovima. U tim uvjetima
šum može prikriti obrazac.

Drukčije pogreške mogu imati drukčije posljedice. Sustavna pogreška,
povezanost pogrešaka ili različita pogreška među skupinama mogu vezu oslabiti,
pojačati, stvoriti ili preokrenuti. Zato nalaz ne postaje uvjerljiviji samo
zato što se pojavio uz slabu pouzdanost. Moramo znati kako pogreška nastaje da
bismo procijenili njezin mogući utjecaj.

Pri provjeri valjanosti pitamo obuhvaća li instrument važne dijelove pojma.
Upitnik o medijskoj pismenosti koji izostavi digitalne sadržaje, primjerice,
propušta dio predmeta. Provjeravamo i mjeri li odabrani pokazatelj baš ono što
tvrdimo. Klik, vrijeme na stranici i komentar mogu upućivati na početni
interes, čitanje ili želju za javnim očitovanjem. Uz instrument treba
razmotriti i uvjete istraživanja. Reakcija na neistinitu vijest na praznom
zaslonu može se razlikovati od reakcije na istu vijest među porukama
prijatelja. Pojmovi interne i eksterne valjanosti, koje ćemo uskoro uvesti,
odnose se na taj dizajn i doseg zaključka.

Vratimo se jučerašnjoj uporabi mobitela. Za usporedbu samoprocjene i zapisa
trebali bismo uskladiti dan, uređaj i aktivnosti koje brojimo. Ako nas
zanima gledanje sadržaja, zapis trajanja uključenog zaslona može biti
koristan pokazatelj. Ako nas zanima pažnja posvećena učenju, trebamo znati
i što smo za to vrijeme radili. Zamislimo otvoren tekst pokraj kojeg
razgovaramo s prijateljem. Uređaj može dosljedno bilježiti trajanje, dok
naše pitanje traži nešto više od trajanja.

Neslaganje samoprocjene i zapisa tako postaje početak provjere mjerenja.
Pregled istraživanja pokazao je i da su upitničke mjere problematične
uporabe još slabije povezane sa zapisanim vremenom uporabe (Parry, 2021).
Trajanje aktivnosti i teškoće koje osoba uz nju doživljava različita su
obilježja. Izbor među njima ovisi o pitanju na koje želimo odgovoriti.

## Treći čimbenik i logika eksperimenta

Čak i kada dobro izmjerimo dvije pojave, njihova povezanost ostavlja otvoreno
pitanje uzroka. Trebamo razmotriti kako su nastale razlike koje uspoređujemo.
U eksperimentu varijablu čiju vrijednost istraživač dodjeljuje nazivamo
nezavisnom, a mjereni ishod zavisnom varijablom. U opažačkoj studiji
prikladniji su nazivi prediktor i ishod jer vrijednosti samo opažamo. Dob ili
obrazovanje sudionika, primjerice, ne dodjeljujemo.

Opaženu vezu može objasniti treća varijabla koja djeluje na obje promatrane
pojave. Ona može stvoriti privid veze ili prikriti postojeći odnos.

**Konfundirajuća varijabla** je zajednički uzrok koji prethodi
pretpostavljenom uzroku i ishodu te utječe na oboje. Ako ga zanemarimo,
opažena veza sadržava i njegov utjecaj.

Ako adolescenti koji više koriste Instagram imaju niže samopoštovanje,
nekoliko objašnjenja ostaje moguće. Korištenje bi moglo snižavati
samopoštovanje, niže samopoštovanje poticati korištenje, a društvena
izoliranost mogla bi istodobno povećavati korištenje i snižavati
samopoštovanje.

Ta objašnjenja traže različite provjere. Za obrnuti smjer djelovanja korisno
je poznavati vremenski redoslijed mjerenja. Za pristranost odabira
provjeravamo kako su sudionici ušli u uzorak i razlikuju li se od populacije.
Kod konfundiranja razmatramo zajednički uzrok. Ako je izmjeren, njegov utjecaj
možemo pokušati uzeti u obzir u analizi. Izbor varijabli za model zato povezujemo s provjerom svakoga od tih mogućih objašnjenja.

Ulogu treće varijable određujemo prema vremenskom redoslijedu i znanju o
pojavi. **Medijator** nastaje djelovanjem pretpostavljenog uzroka i prenosi
dio njegova djelovanja na ishod. Uključivanjem medijatora u prilagodbu
mijenjamo pitanje o učinku. **Kolider** je u najjednostavnijem slučaju zajednička posljedica
pretpostavljenog uzroka i ishoda. Prilagodba ili odabir prema njemu može
stvoriti novu vezu. Izbor varijabli koje treba kontrolirati zato temeljimo i na poznavanju procesa koji proučavamo. Računski ćemo postupak učiti u poglavlju o regresiji, gdje ćemo i dalje
morati obrazložiti izbor varijabli.

U zamišljenom primjeru izoliranost može prethoditi i uporabi mreža i
samopoštovanju. Usporedba osoba slične izoliranosti pokušava razdvojiti taj
zajednički uzrok. Drukčiji je pretpostavljeni put od uporabe mreža preko
manje sna do slabijega rezultata na ispitu. San je tada medijator, pa njegovo
izjednačavanje uklanja dio puta koji želimo proučiti. Za kolider zamislimo
prijam na program na temelju ocjena ili sportskog uspjeha. Među primljenima
slabije ocjene mogu biti povezane s boljim sportskim rezultatom jer je za
prijam dovoljan jedan od dvaju razloga. Odabir samo primljenih stvara vezu
koja ne mora postojati među svim kandidatima.

Umjesto da naknadno pokušavamo razdvojiti utjecaje, možemo već pri nastanku
skupina promijeniti način dodjele uvjeta. **Randomizacija** je nasumična dodjela jedinica uvjetima eksperimenta. Njome
prekidamo sustavnu vezu između početnih obilježja sudionika i uvjeta koji će
primiti. Istraživač dodjeljuje vrijednost nezavisne varijable i nastoji ostale
postupke održati jednakima. Kroz mnogo ponavljanja takve dodjele početna bi
obilježja, poznata i nepoznata, u prosjeku bila uravnotežena. U jednom pokusu
ipak mogu ostati slučajne razlike, osobito uz male skupine. Randomizacija
podupire usporedbu dodijeljenih uvjeta. Želimo li zaključivati o učinku
primljenog tretmana, trebamo provjeriti jesu li se sudionici pridržavali
dodjele. Učinak ponude tretmana može se razlikovati od učinka njegova
primanja.

Zamislimo isti tekst s dvama naslovima, suzdržanim i zaoštrenim. Čitatelje
nasumično rasporedimo tako da svatko vidi samo jedan naslov, a zatim
usporedimo udjele otvaranja. Istraživač tako dodjeljuje naslov, a čitatelj ga
ne bira. Tekst, vrijeme objave i položaj na stranici ostaju jednaki u obje
skupine kako se učinak naslova ne bi pomiješao s tim okolnostima.

Kad bi čitatelji sami birali naslov, skupine bi se mogle razlikovati već po
sklonosti zaoštrenom sadržaju. Razlika u otvaranju tada bi mogla odražavati i
naslov i sastav publike. I uz veći broj zapisa ostala bi potreba da razdvojimo učinak naslova od razlika u sastavu publike. Za
tumačenje je presudno kako su skupine nastale.

Za proučavanje obrazovanja, odrastanja u siromaštvu ili godina provedenih na platformi često koristimo opažački dizajn. Te životne okolnosti zatičemo kod sudionika, a mogućnosti istraživačke intervencije ograničene su i etičkim razlozima. Zaključke tada prilagođavamo načinu na koji su skupine nastale.

Interna valjanost odnosi se na to koliko uvjerljivo razliku u ishodu možemo
pripisati ispitivanom uzroku. U eksperimentu je mogu ugroziti događaji nakon
dodjele. Tretman se može preliti na drugu skupinu, vanjski događaj različito
zahvatiti uvjete ili se sudionici nejednako osipati. Ishod se može mjeriti
drukčije među skupinama. Sudionici mogu i naslutiti svrhu istraživanja pa
odgovarati prema očekivanjima, primjerice pokazivati veću kritičnost prema
medijima nego u svakodnevici.

## Opažačke studije i ankete

Opažačka studija prati postojeće vrijednosti i njihove odnose. Ako utvrdimo
negativnu vezu korištenja mreža i političke informiranosti, sam taj nalaz ne
govori smanjuju li mreže informiranost, koriste li ih slabije informirani više
ili dob i obrazovanje utječu na oboje. Takva studija ipak omogućuje
proučavanje svakodnevnih okolnosti i ljudi koje laboratorij teško može
obuhvatiti.

U kvazieksperimentu intervencija, prag, pravilo ili vanjski događaj stvara
usporedbu bez randomizacije. Treba obrazložiti zašto su nastale skupine
dovoljno usporedive. Zamislimo da se stipendija dodjeljuje prema unaprijed
određenom bodovnom pragu. Usporedba kandidata neposredno iznad i ispod praga
može biti korisna ako ne mogu precizno namjestiti bodove i ako se na istom
pragu ne mijenja još nešto važno. Bez takva obrazloženja razlika ostaje
opažena povezanost.
Studije slučaja i kvalitativne metode mogu samostalno odgovoriti na pitanja
značenja, procesa i iskustva. Mogu također osporiti korištene kategorije ili
predložiti hipotezu za drugi dizajn.

U anketi uz sadržaj upitnika treba provjeriti **okvir uzorkovanja**, skup iz
kojeg se jedinice mogu odabrati. Ako on sustavno izostavlja dio populacije, i veći broj odgovora opisivat će samo obuhvaćeni dio. Taj ćemo problem
razraditi u poglavlju o uzorkovanju.

Treba znati i tko se od pozvanih nije odazvao. Neodaziv može stvoriti
pristranost ako vjerojatnost odgovora ovisi o ishodu koji procjenjujemo. Sama
stopa odaziva ne pokazuje ni veličinu ni smjer te pristranosti. Težina određuje koliko pojedini odgovor pridonosi procjeni, primjerice
kako bi slabije zastupljena skupina dobila veći doprinos. Takvo vaganje prema
zabilježenim obilježjima može pomoći ako ta obilježja objašnjavaju odaziv i
ishod. Ne može ukloniti razlike o kojima podaci ništa ne bilježe. Zato tražimo
podatke o pozvanima, postupku izrade težina i njegovim pretpostavkama.

Prije tumačenja postotaka i margine pogreške možemo podatke o anketi
zabilježiti u sljedeću karticu. Neispunjeno polje pokazuje što ne možemo
provjeriti, bez pretpostavke da je istraživanje na tom mjestu pogrešno.

| Polje | Što treba pronaći u izvještaju |
|---|---|
| okvir i pozivanje | Tko je mogao biti izabran i kojim je putem pozvan? |
| odaziv i nedostajanje | Koliko je pozvanih sudjelovalo i za koja pitanja odgovori nedostaju? |
| procjena s težinama | Koje varijable ulaze u težine, što one pretpostavljaju o odazivu i koji mogući neodaziv ostaje? |
| mjerenje | Kako pitanje točno glasi, koji su odgovori ponuđeni i kojim je redom postavljeno? |
| provedba | Kada, kojim načinom i na kojim jezicima je anketa provedena? |
| doseg | Koji dio ciljane populacije okvir, odaziv ili filtri ne pokrivaju? |
| nesigurnost | Što pripada uzoračkoj pogrešci, a što mjerenju, obuhvatu i neodazivu? |

: Kartica za čitanje ankete. Izrada autora.

Uzoračku pogrešku odvajamo od ostalih izvora nesigurnosti. Veći uzorak može
smanjiti rasipanje zbog slučajnog odabira. Različito razumijevanje pitanja, nepotpun okvir i sustavan neodaziv zahtijevaju zasebnu procjenu. Navedena margina pogreške opisuje samo dio nesigurnosti ankete.

## Doseg zaključka

Okvir i odaziv ograničavaju na koga se anketni rezultat odnosi. Srodno pitanje
postavljamo i drugim istraživanjima, čak i kada su dobro provedena.
Eksterna valjanost odnosi se na mogućnost prenošenja nalaza na druge ljude,
okolnosti i razdoblja. Nalaz dobiven na studentima jednog fakulteta ne mora
vrijediti za druge skupine. Ponašanje pod nadzorom može se razlikovati od
svakodnevnog, a promjene platformi i navika mogu ograničiti primjenu starijih
rezultata. To vrijedi i za dobro proveden eksperiment.

Internu i eksternu valjanost zato provjeravamo zasebno. Laboratorijski pokus
može dobro odvojiti uzrok od drugih objašnjenja, dok terenski pokus može
zadržati nasumičnu dodjelu u svakodnevnim uvjetima. Za svaki dizajn pitamo što
skupine čini usporedivima i kamo možemo prenijeti rezultat. Prikladan je onaj
dizajn koji može odgovoriti na naše pitanje.

Metode možemo i povezati. Razgovori mogu pomoći odrediti važne kategorije,
anketa opisati njihovu raširenost, a pokus ispitati uže uzročno pitanje.
Kvalitativno istraživanje može biti i cjelovit odgovor na pitanje o značenju
ili procesu, ili pokazati da kvantitativni instrument pogrešno dijeli pojavu.
Kombinaciju biramo prema pitanju.

Nesigurnost već sada možemo razmotriti, iako je još ne izražavamo jednim
brojem. Za mjerenje pitamo bi li druga formulacija, koder ili instrument dali
drukčiji rezultat. Za dizajn provjeravamo mogu li nalaz objasniti obrnuti
smjer, neizmjeren zajednički uzrok, osipanje ili prelijevanje. Za doseg
zaključka bilježimo koga izostavljaju okvir, pravila ulaska i isključenja te
neodaziv.

Kasniji računi obuhvatit će dio nesigurnosti povezane s uzorkom i modelom. Uz
interval ili test ipak ostaje provjera mjerenja, dizajna i odabira jedinica.
Ograničenja izvan dosega izračuna ostaju važna i uz uži interval.

## Interakcija — Prikaz konfundirajuće varijable

Ovdje prelazimo na zasebnu, namjerno konstruiranu ilustraciju s 32 točke,
po 16 za svaku razinu treće varijable. Nižoj razini treće varijable pridružili smo niže izloženosti, a višoj
više. Treća varijabla tako razdvaja obje promatrane veličine. Unutar obiju skupina ishod pada za 0,55 uz jedinicu
izloženosti, uz male unaprijed zadane pomake točaka. Višoj skupini dodajemo
zajednički pomak ishoda od četiri proizvoljne jedinice. Točke nisu odgovori
iz ankete ni novi slučajni uzorci. Tiskani prikaz zadržava tu postavku.
Digitalne kontrole mogu promijeniti pomak uz iste točke.

Na prikazu uspoređujemo odnos dviju varijabli u svim opažanjima zajedno i
unutar podskupina određenih trećom varijablom. Podaci su isti. Ako treća
varijabla pomiče ishod, ukupna veza može imati suprotan smjer od veze unutar
podskupina.

Izloženost i ishod u oba prikaza imaju isto značenje. Razlikuje se ono što
uspoređujemo. Zbirni pravac koristi sva opažanja, a razdvojeni pravci jedinice
iste razine treće varijable.

Moguću ulogu treće varijable kao zajedničkog uzroka procjenjujemo prema vremenskom redoslijedu i znanju o pojavi. Prikaz pokazuje moguću
posljedicu zanemarivanja takvog čimbenika.

*Slika. Ista opažanja prikazana zbirno i prema trećoj varijabli u konstruiranom primjeru.*

**Što isprobati.**

1. Promatrajte početnu vezu bez treće varijable.
2. U izborniku „Pogled” odaberite „Prema trećoj varijabli” i usporedite
   smjerove veza.
3. Pomaknite klizač „Dodatni pomak ishoda pri jednakoj izloženosti” i
   pronađite slučaj u kojem se početni zaključak preokreće.
4. Postavite taj dodatni pomak na nulu i provjerite ostaje li smjer zbirne i
   unutargrupnih veza jednak.

Konfundirajući čimbenik mora djelovati na obje promatrane veličine. Sama
prisutnost treće varijable u tablici nije dovoljna. U ovom primjeru, bez
dodatnog pomaka ishoda pri jednakoj izloženosti, zbirne i unutargrupne veze
imaju isti smjer, iako strmine mogu ostati različite. Moguće konfundirajuće varijable zato
biramo prema sadržajnom razlogu da utječu na obje pojave.

**Statistika u divljini.**
**Pravednost koju tablica može vidjeti.** Za procjenu upisnog postupka
možemo tražiti jednake ukupne ishode, jednako postupanje prema jednako
kvalificiranim kandidatima ili jednaku mogućnost pristupa različitim
studijima. Ti zahtjevi zvuče blisko, ali svaki traži drukčije podatke.
Berkeleyjska tablica sadržavala je ishode prijava, spol i odjel, bez
potpunih podataka o kvalifikacijama kandidata i okolnostima njihova izbora
(Bickel, 1975).

Zamislimo da iz takve tablice trebamo pripremiti prijedlog poboljšanja
upisa. Ako nas zanima postupanje povjerenstva, trebali bismo znati koje je
kriterije koristilo i jesu li uspoređene prijave bile slične po tim
kriterijima. Ako nas zanima dostupnost studija, trebali bismo pratiti i
ljude koji se nisu prijavili te razloge zbog kojih neki studij nisu
razmatrali. Za njihov bismo put trebali zasebne podatke, izvan tablice podnesenih prijava.

Važna je i jedinica zapisa. Berkeleyjska analiza polazi od prijava
koje su nakon povlačenja ili preusmjeravanja ostale u postupku do
zabilježene odluke (Bickel, 1975). Takav obuhvat nije popis svih ljudi
koji su u nekom trenutku željeli upisati studij. Za pitanje o njihovu
konačnom uspjehu trebalo bi pratiti i one koji su odustali te
utvrditi što se s njima dalje dogodilo.

Statistička teškoća ovdje prethodi izboru testa. Pojam pravednosti treba
povezati s opažanjima koja ga mogu poduprijeti ili osporiti. U zamišljenom
prijedlogu možemo opisati razlike koje tablica pokazuje i navesti koje bi
dodatne informacije omogućile provjeru postupka. Praznine bilježimo kao otvorena pitanja za daljnje istraživanje nejednakosti.

Koristan rezultat takve analize može biti preciznije sljedeće pitanje.
Treba li pregledati kriterije povjerenstva, savjetovanje prije prijave ili
dostupnost prethodnog obrazovanja ovisi o tome koju prepreku želimo
istražiti. Stopa prijma pomaže tek kada znamo koji dio toga puta mjeri.

Razlika između opažene povezanosti i uzročnog učinka vrijedi i za ankete o
uporabi društvenih mreža.

**Nađite grešku.**
Nakon rasprave o opažačkim studijama pregledajte ovaj konstruirani
istraživački zapis. Nije riječ o nalazu stvarne ankete.

Studenti su u jednom upitniku naveli dnevno vrijeme na društvenim mrežama,
trenutačno povjerenje u institucije i dob. Istraživači nisu određivali
njihovo vrijeme korištenja niti su ih pratili prije i poslije promjene
navika. U ovom zadanom primjeru niže povjerenje prati dulje korištenje,
a isti smjer ostaje i pri usporedbi studenata jednake dobi.

Asistent je za izvještaj pripremio sljedeći tekst.

> U opažačkoj anketi dulje korištenje mreža povezano je s nižim
> povjerenjem. Obje su varijable izmjerene istim upitnikom, a usporedba
> uzima u obzir dob. Rezultat zato pokazuje da dulje korištenje društvenih
> mreža smanjuje povjerenje.

Sastavite kratku bilješku istraživačkom timu. Sačuvajte opis opaženog
odnosa, zamijenite nepoduprtu tvrdnju i navedite jedno drugo objašnjenje
koje opisani postupak ne isključuje. Napišite koji bi dodatni podatak ili
promjena dizajna pomogli razlikovati ta objašnjenja.

## Razrađeni primjer

Dosad smo operacionalizaciju promatrali kao izbor opažanja koja predstavljaju
pojam. U primjeru povjerenja u lokalne institucije pratimo kako odabrane odgovore
spajamo u zajedničku mjeru. Koristimo četiri konstruirane
tvrdnje s istom ljestvicom odgovora od 1 do 5, jer jedna tvrdnja ne obuhvaća
cijeli pojam. Prije spajanja provjerit ćemo znači li viši odgovor na svakoj
tvrdnji doista više povjerenja.

| Oznaka | Konstruirana tvrdnja | Smjer višeg odgovora |
|---|---|---|
| t1 | Mogu se osloniti na odluke lokalnih institucija. | više povjerenja |
| t2 | Lokalne institucije postupaju pošteno prema građanima. | više povjerenja |
| t3 | Lokalne institucije objavljuju informacije kojima mogu vjerovati. | više povjerenja |
| t4 | Lokalne institucije često skrivaju važne informacije. | manje povjerenja |

: Četiri tvrdnje konstruirane za nastavni primjer i njihov smjer. Izrada autora.

Prve tri tvrdnje izrečene su potvrdno, a četvrta niječno. U zamišljenom nacrtu
niječna je formulacija trebala prekinuti mehaničko ponavljanje odgovora. Ona
može i zbuniti ispitanika, a pri računanju zahtijeva posebno kodiranje.

Za račun smo ručno sastavili odgovore 12 zamišljenih osoba. Nema slučajnog
uzorkovanja ni nedostajućih odgovora. Svih dvanaest redaka pokazuje vrijednosti
prije ikakve promjene kodiranja. Odgovori služe provjeri kodiranja i opisuju samo ovaj nastavni primjer.

*Slika. Početni odgovori u namjerno konstruiranom instrumentu. Izrada autora.*

Za osobu I01 zbroj prvih triju odgovora iznosi 13, dok je odgovor na četvrtu
tvrdnju 2. Taj par, zajedno s odgovarajućim parovima preostalih 11 osoba,
ulazi u provjeru povezanosti četvrte tvrdnje s ostatkom instrumenta.

Smjer tvrdnje provjeravamo i u samim odgovorima. Ako osoba na jednoj tvrdnji
iskazuje više povjerenja, očekujemo da će ga iskazati više i na ostalima koje
mjere isti pojam. Zato svaku tvrdnju uspoređujemo sa zbrojem preostalih i
tražimo pozitivnu povezanost. Računamo Pearsonovu korelaciju stavke i zbroja
ostalih stavki. To je korigirana korelacija stavke s ukupnim rezultatom jer
se stavka ne pojavljuje i u vlastitom usporednom zbroju. Njezina vrijednost može biti od −1 do 1.
Pozitivan predznak znači kretanje u istom smjeru, a negativan u suprotnom.
Postupak računanja upoznat ćemo u poglavlju o povezanosti.

*Slika. Povezanost svake tvrdnje s ostatkom instrumenta, prije i nakon okretanja niječne tvrdnje. Izrada autora.*

Prve tri tvrdnje u tablici pozitivno su povezane s ostatkom instrumenta.
Četvrta ima negativnu povezanost, `r hr_broj(s2$t4_prije, 2)`. U ovom primjeru znamo razlog jer
smo sami konstruirali tvrdnje. Visok odgovor na četvrtoj znači nisko
povjerenje, dok na ostalima znači visoko povjerenje. U stvarnom istraživanju
negativna povezanost sama ne bi bila dovoljna za takvu dijagnozu.

Za četvrtu tvrdnju okrećemo ljestvicu. Od najveće moguće vrijednosti uvećane
za jedan oduzimamo zabilježeni odgovor. Na ljestvici od 1 do 5 to znači
$6 - \text{odgovor}$. Za I01 tako 2 postaje 4. Njezin prvotni prosjek
$(4+5+4+2)/4 = 3,75$ postaje $(4+5+4+4)/4 = 4,25$. Isti postupak primjenjujemo
na četvrti odgovor svih 12 osoba, čuvajući ostale odgovore.
Povezanost s ostatkom tada iznosi
`r hr_broj(s2$t4_poslije, 2)`. Sve tvrdnje sada imaju isti smjer, što omogućuje njihovo smisleno
zbrajanje.

*Slika. Odgovori nakon okretanja niječne tvrdnje i izvedena mjera povjerenja. Izrada autora.*

Bez okretanja raspon prosječnih rezultata iznosio bi `r hr_broj(s2$raspon_naivno, 2)` boda. Nakon
ispravka iznosi `r hr_broj(s2$raspon_ispravno, 2)`. Niječna tvrdnja prije ispravka poništavala je dio
razlika koje su bilježile ostale tvrdnje. Iako bi sam račun bio točan,
dobili bismo pogrešan dojam da se ispitanici vrlo malo razlikuju u povjerenju.

U stvarnim podacima prvo bismo provjerili ključ kodiranja. Negativna
povezanost može nastati i zato što tvrdnja mjeri drugu dimenziju, prijevod
mijenja značenje, formulacija je dvosmislena ili sudionici odgovaraju
nepažljivo. Zato pregledavamo puni tekst tvrdnje i obrasce odgovora. Okretanje
je opravdano tek kad odgovara sadržaju. Automatsko okretanje ili izbacivanje
tvrdnje moglo bi sakriti drugi mjerni problem.

Nakon ispravka tvrdnje se u ovom konstruiranom skupu kreću zajedno, što
podupire njihovu internu konzistentnost. Za valjanost trebamo dodatnu provjeru.
Sve bi tvrdnje mogle bilježiti, primjerice, sklonost slaganju umjesto
povjerenja. Zato uz dosljednost razmatramo njihov sadržaj, način na koji ih
ispitanici razumiju i odnos s drugim opravdanim mjerama.

Primjer se odnosi na jedno konstruirano mjerenje. Za primjenu u stvarnom istraživanju trebalo bi dodatno proučiti sudjelovanje, odbijanje poziva i razumijevanje tvrdnji. Te okolnosti određuju doseg zaključka uz prikazani račun. Zbog
toga pri čitanju nalaza uvijek trebamo i opis postupka.

## Sažetak

Mjerenjem pretvaramo teorijski pojam u opažanja, a pravilima ulaska,
isključenja i postupanja s nedostajućim odgovorima određujemo koga ona
predstavljaju. Na primjeru niječne tvrdnje vidjeli smo zašto prije sažimanja
treba provjeriti značenje odgovora, pa tek zatim dosljednost i valjanost mjere.
Uz dobro mjerenje, uzročni zaključak zahtijeva i odgovarajući dizajn. Randomizacija uravnotežuje skupine u očekivanju, ali i dalje treba
provjeriti provedbu, pridržavanje dodjele, osipanje, prelijevanje i
mjerenje. Ta pitanja ostaju važna i uz interval ili test. Već u sljedećem poglavlju
poslužit će nam za čitanje tvrdnji koje prešućuju kako su nastali njihovi
brojevi.

## Pojmovi

operacionalizacija (*operationalization*), varijabla (*variable*), prihvatljivost
(*eligibility*), kodiranje kao mjerenje (*coding as measurement*), razina
mjerenja (*level of measurement*), pouzdanost (*reliability*), valjanost
(*validity*), konfundirajuća varijabla (*confounder*), medijator (*mediator*),
kolider (*collider*), randomizacija (*randomization*), interna valjanost
(*internal validity*), okvir uzorkovanja (*sampling frame*), eksterna valjanost
(*external validity*), opažačka studija (*observational study*),
kvazieksperiment (*quasi-experiment*), neodaziv (*nonresponse*),
interna konzistentnost (*internal consistency*)

## Zadaci

### Konceptualni

Na vlastitom primjeru objasnite kako mjera može biti pouzdana, a nevaljana.
Jasno navedite što je u mjerenju dosljedno i zašto rezultat ipak ne mjeri
željeni pojam.

Odaberite pojam iz svojeg područja i predložite dva načina njegova mjerenja.
Za svaki opišite što obuhvaća i što izostavlja te nalaz koji bi jedan način
pokazao, a drugi ne bi. Za jedan prijedlog navedite jedinicu analize, ciljnu
skupinu, pravilo prihvatljivosti, jedno isključenje i razinu mjerenja.
Objasnite kako isključenje sužava doseg zaključka. Ako kodirate jezik,
navedite pravilo za jednu oznaku i postupak za dvosmislen slučaj.

U zamišljenoj opažačkoj studiji pratite korištenje političkih vijesti i
povjerenje u institucije. Razmotrite političko zanimanje prije praćenja,
znanje stečeno nakon praćenja te ulazak u analizu koji ovisi o korištenju
vijesti i povjerenju. Svaku od tih varijabli razvrstajte kao zajednički uzrok,
medijator ili kolider i obrazložite izbor. Zatim objasnite što bi nasumična
dodjela korištenja vijesti uravnotežila kroz ponavljanja te zašto u jednom
malom pokusu skupine mogu ostati različite.

### Računski

Upotrijebite tablicu povezanosti stavki iz razrađenog primjera. Za četvrtu
tvrdnju ručno provjerite kako se svaki odgovor od 1 do 5 mijenja pri okretanju
ljestvice i zapišite okrenute vrijednosti. Zatim iz tablice s odgovorima uzmite
prva tri ispitanika. Za svakoga izračunajte prosjek četiriju tvrdnji prije i nakon
okretanja. Predajte svih šest prosjeka.

Jednom rečenicom objasnite zašto propušteno okretanje smanjuje razlike među
ispitanicima. Postupak za provjeru cijelog skupa podataka nalazi se u
praktikumu.

### Kritički

Prosudite što se iz Berkeleyjskih podataka može zaključiti o ishodima, a što
ne može o postupku odlučivanja (Bickel, 1975). Predajte dva stupca s dopuštenim i
nedopuštenim zaključcima.

Pronađite objavljeno istraživanje iz svojeg područja. Ispunite karticu za
čitanje ankete i napišite odlomak koji navodi dizajn, jedinicu
analize, jedno pravilo ulaska ili isključenja te jedan izvor nedostajanja.
Zasebno razmotrite nesigurnost mjerenja, dizajna i dosega. Za svaku u vlastitoj trorednoj tablici
navedite jedan rizik koji se može provjeriti. Zatim navedite zaključak koji
dizajn opravdava. Procijenite prelaze li autori taj doseg, uz primjer
pretjerane tvrdnje ili obrazloženje zašto su ostali unutar njega.

### Revizija modela

Provjerite analizu iz okvira iznad. Navedite dizajn, izdvojite
neopravdanu tvrdnju i preoblikujte je prema onome što zadani primjer dopušta.
Predložite dizajn koji bi bolje razlikovao uzrok od povezanosti i navedite
jedno njegovo ograničenje. Razlikujte prijedlog budućeg istraživanja od
onoga što je u opisanoj anketi već učinjeno.

---

# Kako brojke zavode

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Pripremate kratku vijest o odazivu. U službenom izvješću
o izborima za Hrvatski sabor 2024. nalazite 62,30 % (Hrvatske}, 2024).
Rečenica da je toliko birača glasovalo djeluje jasna. Podatak dolazi iz
službenog izvora, a račun možete provjeriti.

No u istoj tablici broj pristupilih glasovanju nije jednak broju birača
prema glasačkim listićima (Hrvatske}, 2024). Obje biste veličine u
razgovoru mogli nazvati brojem ljudi koji su glasovali. Za vijest ipak
trebate odabrati riječi koje odgovaraju upravo onome što izvor broji.

Što zapravo potvrđuje provjera postotka? Može li naslov sadržavati točan
broj, a čitatelju ipak prenijeti pogrešno značenje?

Iza postotka iz izbornog izvješća stoji nekoliko odluka o tome što se broji
(Hrvatske}, 2024). One lako nestanu kada tablicu skratimo u naslov. U prvim
smo poglavljima naučili tražiti jedinicu i nazivnik te razlikovati pojavu od
načina na koji je mjerimo. Sada ćemo tim pitanjima provjeravati tvrdnje koje
već dolaze s gotovim brojem, grafom ili uvjerljivim objašnjenjem.

Glavni primjer počiva na stvarnoj objavljenoj tablici Državnoga izbornog
povjerenstva (Hrvatske}, 2024). Njezine stavke predstavljaju nacionalne zbrojeve s različitim značenjima. Usporedit
ćemo broj pristupilih glasovanju, broj prema listićima i broj birača koji
služi kao nazivnik. Cilj je utvrditi koju rečenicu možemo napisati na temelju
tih podataka. Razliku među evidencijama opisat ćemo u granicama onoga što je dokumentirano.

Od provjere omjera prijeći ćemo na načine prikazivanja. Ispitat ćemo kako
promjena osnovice ili raspona osi mijenja dojam, zašto postotna promjena nije
isto što i promjena u postotnim bodovima te kako zanemarivanje rijetkosti neke
pojave može zavesti. Pri čitanju ankete povezat ćemo objavljenu marginu
pogreške s onime što smo naučili o obuhvatu i odazivu. Konstruirani anketni primjeri
poslužit će nam da odvojeno mijenjamo veličinu uzorka i sustavnu pristranost.
Njihove rezultate nećemo čitati kao izbornu prognozu.

Provjera završava povratkom izvoru i usporedbom računa s riječima kojima je opisan. To vrijedi i
kada analizu sastavi asistent. Tražit ćemo trag do tablice, provjeriti račun
koji nosi tvrdnju i zabilježiti što nedostaje za njezino tumačenje. Tako ćemo
sastaviti protokol skeptičnoga čitanja koji razlikuje potvrđenu brojku,
nedostajući podatak i zaključak koji prelazi dokaz.

## Od točnoga broja do potpune tvrdnje

Polazimo od službenog *Izvješća o provedenim izborima za zastupnike u Hrvatski
sabor 2024.*, koje je objavilo Državno izborno povjerenstvo (Hrvatske}, 2024).
Tablica „Odaziv birača” nalazi se na stranici 124 i provjerena je na službenom
portalu 5. kolovoza 2026. (Hrvatske}, 2024). Za provjeru koristimo
objavljenu tablicu. Izborna datoteka nije preuzeta ni pohranjena uz knjigu, a
dostupnost na portalu sama ne znači dopuštenje za njezino daljnje dijeljenje.

Naslov dokumenta, izdavač i stranica omogućuju drugoj osobi da pronađe broj.
Bez tih podataka tvrdnja može biti točna, ali provjera zahtijeva dodatno
traženje izvora.

U tablici je pet različitih veličina koje bismo u običnom govoru mogli nazvati
brojem birača (Hrvatske}, 2024). Za račun trebamo sačuvati njihove pune
oznake.

| Službena veličina | Vrijednost | Uloga u čitanju |
|---|---:|---|
| ukupno birača | 3.558.089 | nazivnik na obrađenim biračkim mjestima |
| pristupilo glasovanju | 2.216.763 | brojnik objavljenog odaziva |
| glasovalo prema glasačkim listićima | 2.215.209 | kontrola prema pronađenim listićima |
| važeći listići | 2.154.733 | dio broja prema listićima |
| nevažeći listići | 60.476 | drugi dio broja prema listićima |

: Nacionalne vrijednosti izbora za Hrvatski sabor 2024. Izrada autora prema
Hrvatske}, 2024, str. 124.

Objavljeni postotak slijedi iz prvoga i drugoga retka (Hrvatske}, 2024).

$$
\frac{2\,216\,763}{3\,558\,089}\times 100 = 62{,}30\,\%.
$$

Za provjeru broja prema listićima trebamo drugu operaciju. Zbrajamo važeće i
nevažeće listiće, jer zajedno čine sve pronađene listiće iz tablice
(Hrvatske}, 2024).

$$
2\,154\,733 + 60\,476 = 2\,215\,209.
$$

Oba su računa točna i odnose se na različite faze postupka. Razlika od 1.554 izražava odstupanje broja pristupilih od broja prema listićima (Hrvatske}, 2024). Za objašnjenje uzroka, uključujući provjeru moguće pogreške u evidenciji, trebali bismo dodatne podatke. Značenje svake oznake određuje se pravilima evidentiranja, neovisno o tome jesu li zbrojevi jednaki ili različiti.

Pri pisanju naslova biramo podatke, računamo omjer i odlučujemo kako ćemo ga
opisati. Na svakom koraku možemo promijeniti značenje, iako nismo promijenili
brojeve. Zato uz dijeljenje provjeravamo i odgovaraju li riječi u tvrdnji
oznakama iz izvora.

U ovom primjeru možemo povezati izvješće, njegove oznake, nacionalne zbrojeve
i omjer s tvrdnjom o pristupanju glasovanju (Hrvatske}, 2024). Ako asistent
vrati samo 62,30 %, nedostaje objašnjenje što je podijelio [Hrvatske}, 2024, str.
124]. Uz rezultat treba zadržati brojnik, nazivnik i njihov obuhvat kako bi se
mogao provjeriti i račun i tumačenje.

## Nazivnik, os i rijedak ishod

Uz svaki postotak pitamo na koju se cjelinu odnosi. Odaziv od 62,30 % zato
čitamo zajedno s nazivnikom (Hrvatske}, 2024). Graf koji prikazuje samo
postotak izostavlja izvorne brojeve. Ako mu os počinje neposredno ispod
opaženih vrijednosti, male razlike mogu izgledati velike. Skraćena os može
biti korisna, ali njezin raspon mora biti vidljiv i odgovarati pitanju.

Značenje razlike čuvamo i izborom mjere promjene. Kada dvije stope oduzmemo,
razliku izražavamo u **postotnim bodovima**. Za relativnu postotnu promjenu tu
razliku još dijelimo početnom stopom. Prvi račun govori koliko su stope
udaljene na istoj ljestvici, a drugi kolika je promjena u odnosu na polazište.
U nastavku ćemo tu razliku provjeriti usporedbom dvaju obuhvata izbornog
izvješća.

Nazivnik odlučuje o značenju postotka i kada procjenjujemo uspješnost nekog
postupka. Sintetički zapis stvorio je program. Detektor je postupak koji pokušava
prepoznati takvo podrijetlo, a upozorenje je njegova oznaka da bi zapis
mogao biti sintetički.

Udio pronađenih sintetičkih zapisa, primjerice, nije isto što i udio
ispravnih upozorenja. Uzmimo hipotetski skup od 10.000 zapisa. Program je stvorio njih 100, a ostali
bilježe stvarne događaje. Detektor prepoznaje 90 od tih 100 sintetičkih zapisa
i pogrešno označava 495 ostalih. Te brojeve namjerno zadajemo za ilustraciju rada zamišljenog sustava. Preostala mjesta dopunjavamo do
100 sintetičkih i 9.900 ostalih zapisa.

| Stvarno podrijetlo | Upozorenje | Bez upozorenja | Ukupno |
|---|---:|---:|---:|
| sintetički zapis | 90 | 10 | 100 |
| stvarni događaj | 495 | 9.405 | 9.900 |
| ukupno | 585 | 9.415 | 10.000 |

: Namjerno zadana brojanja za usporedbu nazivnika. Izrada autora.

Prvi redak daje $90/100 = 90$ % pronađenih sintetičkih zapisa. Drugi daje
$495/9\,900 = 5$ % pogrešnih upozorenja među ostalima. Za udio ispravnih upozorenja
treba nam prvi stupac. Od ukupno 585 upozorenja ispravno je samo 90,
približno 15,4 %. Detektor je pronašao 90 % sintetičkih zapisa, ali većina
njegovih upozorenja ipak je pogrešna. Udio pronađenih zapisa razlikuje se od
udjela ispravnih upozorenja.

**Temeljna stopa** jest udio ishoda u relevantnoj populaciji prije nego što se
uzme u obzir novi signal, test ili model.

Sintetički zapisi u tom
primjeru čine 100 od 10.000 zapisa, odnosno 1 %. To je
temeljna stopa. Pri tumačenju upozorenja treba uzeti u obzir koliko je tražena
pojava uopće česta.

Ako je u skupu iste veličine 1.000 sintetičkih zapisa, isti detektor pronašao
bi njih 900 i pogrešno označio 450 ostalih. Od 1.350 upozorenja sada bi bilo
ispravno 900, odnosno dvije trećine. Promijenio se udio sintetičkih zapisa,
dok je detektor zadržao istu sposobnost prepoznavanja i istu stopu pogrešnog
označavanja.

Da bismo procijenili koliko vjerovati upozorenju, trebamo znati koliko
detektor propušta traženih zapisa, koliko pogrešno označava ostale i kolika je
temeljna stopa. Tu ćemo vezu ponovno razmotriti u poglavlju o algoritmima,
kada klasifikacija vodi odlukama koje različito pogađaju ljude.

I pri čitanju izbornog izvješća rezultat ovisi o odabranom nazivniku. Nevažeće
listiće možemo izraziti kao udio svih listića, pristupilih ili svih birača u
objavljenom obuhvatu. Svaki omjer ima svoje značenje.

## Anketa, obuhvat i biranje trešanja

DIP-ova tablica sažima administrativnu evidenciju izbora. Anketa, naprotiv,
koristi odgovore dijela ljudi kako bi zaključivala o široj populaciji.
Postotci iz tih izvora zahtijevaju različite provjere.

Pri čitanju ankete ponovno koristimo sedam polja kartice iz prethodnog
poglavlja. Bilježimo ciljnu
populaciju, okvir iz kojeg su ljudi odabrani i način regrutacije. Tražimo broj
pozvanih i odgovora, datume, formulaciju pitanja, ponderiranje, odnosno primjenu težina, neodaziv,
naručitelja te objavljenu marginu pogreške. Ono što nije navedeno ostavljamo
označeno kao nepoznato.

Za administrativnu evidenciju provjeravamo koji događaji prema pravilima ulaze
u nju, jesu li zapisi ispravni, oznake dosljedne i obrada uredna. Za anketu uz
mjerenje provjeravamo izbor sudionika, okvir, regrutaciju i neodaziv. Anketa
ima i promjenjivost koja nastaje odabirom uzorka. Margina uz znak ± odnosi se na određeni dio te nesigurnosti, pa ostale izvore procjenjujemo zasebno.

Dobrovoljna internetska anketa može prikupiti mnogo odgovora, a ipak
izostaviti ljude koji se sustavno razlikuju u onome što mjerimo. Manji
vjerojatnosni uzorak može imati veću slučajnu promjenjivost, ali jasnije
pokazivati na koga možemo prenijeti nalaz. Veličinu uzorka zato uvijek čitamo
uz način odabira.

Učinak odabira redaka možemo provjeriti i u izbornom izvješću. Za jedinice
I.–X. zabilježeno je 2.140.824 pristupilih od 3.482.150 birača, što daje 61,48
% (Hrvatske}, 2024). Uključimo li sve jedinice I.–XII., odaziv iznosi 62,30
%, odnosno 0,82 postotna boda više (Hrvatske}, 2024).

Prije tumačenja razlike moramo provjeriti usporedivost nazivnika.
Za XI. i XII. jedinicu tablica odaziva navodi jednake brojeve birača i
pristupilih, 41 120 i 34 819. Na prethodnoj stranici zasebni su registrirani
brojevi 222 300 birača XI. jedinice i ukupno 275 521 pripadnik navedenih
manjina (Hrvatske}, 2024). Stopa od 100 % u tablici odaziva stoga
ne znači da su glasovali svi iz tih registarskih populacija.

Zbroj I.–X. i zbroj I.–XII. opisuju različite obuhvate. Izbor užega nije
sam po sebi biranje trešanja. To postaje kad ga biramo radi poželjnijeg
rezultata, a prešutimo što izostavljamo i zašto se nazivnici razlikuju.
Sljedeća tablica donosi brojnosti po izbornim jedinicama za provjeru
zbrojeva iz izvješća (Hrvatske}, 2024).

| Jedinica | Birači u tablici odaziva | Pristupili |
|---|---:|---:|
| I. | 341 023 | 235 854 |
| II. | 345 398 | 208 757 |
| III. | 349 058 | 218 626 |
| IV. | 351 860 | 208 606 |
| V. | 336 652 | 183 593 |
| VI. | 352 234 | 242 083 |
| VII. | 340 923 | 201 408 |
| VIII. | 355 951 | 211 123 |
| IX. | 350 941 | 208 648 |
| X. | 358 110 | 222 126 |
| XI. | 41 120 | 41 120 |
| XII. | 34 819 | 34 819 |

: Sastavnice odaziva za provjeru zbrojeva. Izrada autora prema Hrvatske}, 2024, str. 124.

U odnosu na zaokruženu stopu I.–X. relativna razlika iznosi
$(62,30-61,48)/61,48\times100\approx1,33$ %. Time uspoređujemo dva obuhvata istih izbora u istom razdoblju.

Razlika od 0,82 postotna boda izgledala bi mala na osi od 0 % do 100 %, a
mnogo istaknutija na osi od 61 % do 63 % (Hrvatske}, 2024). Broj i njegovo
značenje ostaju isti. Mijenja se vizualni dojam, zbog čega raspon osi treba
jasno označiti i opravdati.

## Interakcija — Istraživač margine pogreške

U ovom prikazu udio i veličinu uzorka zadajemo izravno. Početnih 52 % može
značiti 130 odgovora od 250 ili 520 od 1.000. Iz zadanoga udjela i veličine uzorka računamo približnu marginu koju
oduzimamo od procjene i dodajemo procjeni.
Postupak radi izravno sa zadanim sažetkom ankete. Zadanom
pristranošću odvajamo procjenu od pretpostavljene istine, pa se može vidjeti
zašto uži interval sam ne popravlja sustavan pomak.

Prikazane su tri konstruirane anketne situacije s približnom 95-postotnom
marginom za jednostavan neovisan uzorak. Primjer ne uključuje složen dizajn,
ponderiranje, neodaziv ili mjernu nesigurnost. Prve dvije situacije razlikuju
se po veličini uzorka. Treća pokazuje kako sustavna pristranost može pomaknuti
uzak interval dalje od istine. Prikaz služi razumijevanju uzoračke
nesigurnosti i ne izračunava pogrešku DIP-ove tablice. Margina je udaljenost
od procjene do svakog kraja simetričnog intervala, prikazanog sivom crtom.
Oznaka 95 % opisuje postupak koji bi, uz navedene pretpostavke i mnogo novih
uzoraka, obuhvatio pravu vrijednost u približno 95 % intervala. Nije
vjerojatnost da je pojedini anketni odgovor točan. Račun ćemo razraditi u
poglavljima o uzorkovanju i procjeni.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

U drugoj je situaciji uzorak veći nego u prvoj, pa je interval uži. U trećoj
veličina uzorka i procijenjeni udio ostaju kao u drugoj, ali uz
pretpostavljenu sustavnu pristranost istinita vrijednost leži izvan intervala.

Veći uzorak smanjuje slučajno rasipanje procjene. Pri sustavnom promašivanju istine veći uzorak daje uži interval oko pomaknute procjene. Preciznost tada prati pristranost.

## Podrijetlo ljudskog i strojnog broja

**Statistika u divljini.**
**Kada „glasovalo” postane preširoka riječ.** U zamišljenoj redakciji
pripremamo kratku vijest o izlaznosti na izbore. Pred nama je stvarno
izvješće DIP-a, u kojem tablica odaziva navodi 62,30 %
(Hrvatske}, 2024). Naslov „Glasovalo je 62,30 % birača” čini se
prirodnim sažetkom tog podatka. Prije objave ipak trebamo utvrditi što
glagol glasovalo prenosi iz tablice, a što mu čitatelj može pridodati.

U početnoj smo tablici već razlikovali broj pristupilih od broja birača
prema glasačkim listićima (Hrvatske}, 2024). U naslovu svaku veličinu navodimo pod njezinim izvornim nazivom, a za tumačenje razlike tražimo dodatne podatke.

Redakcijska provjera zato uz dijeljenje obuhvaća i značenje upotrijebljenih pojmova.
Kad bismo odaziv opisali kao udio birača koji su dali važeći glas nekoj
listi, promijenili bismo značenje brojnika. Kad bismo nazivnik zamijenili
svim punoljetnim stanovnicima, odgovorili bismo na drugo pitanje.
Nijednu od tih promjena ne opravdava to što početni postotak dolazi iz
službenog izvora.

Vijest zato možemo vezati uz imenovanu mjeru. Prema izvješću DIP-a,
glasovanju je pristupilo 62,30 % birača na obrađenim biračkim mjestima
(Hrvatske}, 2024). Uz poveznicu na tablicu čitatelj može provjeriti
brojnik, nazivnik i obuhvat. Uredništvo je sačuvalo glavnu informaciju i preciziralo na što se ona odnosi.

Razloge izlaska i političke stavove birača istražujemo zasebno od evidencije izlaznosti.

Asistent može zbrojiti vrijednosti, usporediti nazivnike i predložiti jasniju
rečenicu. Svaki dobiveni broj ipak povezujemo s objavom i ulaznim podacima.
Provjeravamo što je izračunato, koji je nazivnik korišten i vodi li citat do
tog podatka.

**Nađite grešku.**
Prije objave vijesti provjeravate asistentov sažetak iste DIP-ove tablice
koju smo već čitali. Izvadak zadržava službene oznake i brojnosti
(Hrvatske}, 2024).

| Oznaka u izvješću | Broj |
|---|---:|
| Pristupili glasovanju | 2.216.763 |
| Birači prema glasačkim listićima | 2.215.209 |
| Važeći glasački listići | 2.154.733 |
| Nevažeći glasački listići | 60.476 |

: Izvadak službenih izbornih brojnosti. Izrada autora prema Hrvatske}, 2024, str. 124.

> Važećih 2.154.733 i nevažećih 60.476 listića daju ukupno 2.215.209.
> To je 1.554 manje od broja pristupilih, odnosno približno 0,07 % broja
> pristupilih. Razlika je tako mala da u vijesti možemo na oba mjesta
> napisati „pristupili glasovanju”.

Na bilješci odvojeno označite provjerene račune i predloženu uredničku
izmjenu. Napišite prihvatljivu zamjenu posljednje rečenice. Ako biste
željeli objasniti nastanak razlike, navedite što biste još morali
provjeriti u izvoru.

Provjera izvora potrebna je i za slike, zvuk i video. Uvjerljiv zapis može
biti umjetno stvoren, a neobičan izgled ne mora značiti da je lažan. Zasebno
provjeravamo odakle datoteka dolazi, je li izmijenjena i je li se prikazani
događaj zbio. Za svako od tih pitanja potreban je zaseban dokaz.

Za tumačenje materijala razlikujemo sljedeće četiri oznake.

| Oznaka | Što predmet jest | Što ne smije poduprijeti |
|---|---|---|
| simulacija | podaci proizvedeni poznatim mehanizmom radi učenja postupka | nalaz o stvarnoj populaciji |
| sintetički zapis | umjetno stvoren zapis koji oponaša oblik podatka ili medija | tvrdnju da se prikazani događaj doista zbio |
| hipotetski izlaz modela | uvjetni odgovor izrađen radi provjere zaključivanja | tvrdnju da je određeni sustav taj odgovor stvarno dao u zabilježenoj uporabi |
| izmišljeni dokaz | nepostojeći broj, opažanje ili izvor prikazan kao stvaran | bilo koju empirijsku tvrdnju |

: Četiri vrste dokaznog predmeta i njihove granice. Izrada autora.

Primjer s rijetkim sintetičkim zapisima pokazao je zašto sama oznaka
detektora nije dovoljna. Detektor sintetičkog sadržaja također proizvodi procjenu. Ona ovisi o podacima
na kojima je učen, inačici, postavkama i pragu. Ako je sintetički sadržaj
rijedak, čak i umjerena stopa lažnih upozorenja može dati više pogrešnih nego
točnih oznaka. Rezultat detektora zato koristimo kao poticaj za daljnju provjeru podrijetla.

I autentičan zapis može imati nepotpun trag podrijetla. Snimka zaslona može
izgubiti metapodatke, a izvorna datoteka postati nedostupna. S druge strane,
uredni metapodaci ne jamče istinitost sadržaja. Neovisna potvrda događaja
također ne dokazuje autentičnost određene snimke. Kad nema dovoljno dokaza,
bilježimo da podrijetlo nije provjereno. Tražimo prvu objavu, poznate izmjene
i zasebnu potvrdu događaja.

Generirani podaci u računskom zadatku pripadaju simulaciji. Služe vježbi
postupka, bez tvrdnje o stvarnim događajima. Pogrešni odgovor iz okvira Nađite grešku jest hipotetski izlaz modela. DIP-ova tablica službeni je administrativni izvor.
Oznaka uz svaki materijal određuje za kakav ga zaključak možemo koristiti.

## Razrađeni primjer

Početnu tvrdnju o odazivu sada možemo provjeriti od izvora do konačne rečenice.
Već smo razlikovali službene oznake i njihove nazivnike. Preostaje provjeriti
slažu li se zbrojevi pojedinih izbornih jedinica s nacionalnim retkom te
sačuvati to značenje pri pisanju zaključka.

Vraćamo se tablici „Odaziv birača” na stranici 124 izvješća Državnog izbornog
povjerenstva Republike Hrvatske o izborima za Hrvatski sabor 2024. [Hrvatske}, 2024,
str. 124]. Provjera na službenom portalu obavljena je 5. kolovoza 2026., pa uz
račun zadržavamo i taj datum (Hrvatske}, 2024). Uz knjigu nije pohranjena izborna
datoteka niti se pretpostavlja dopuštenje za njezino daljnje dijeljenje.

Datum pregleda bilježimo kako bi se znalo kada smo provjerili dokument. Ne jamči da će
dokument zauvijek ostati isti. Ako se sadržaj na adresi promijeni ili nestane,
bez spremljene datoteke i njezina kontrolnog zbroja nećemo moći potvrditi
istovjetnost s pregledanom inačicom.

Tablica sadržava dvanaest redaka izbornih jedinica I.–XII. i nacionalni zbroj
(Hrvatske}, 2024). Nacionalni redak služi provjeri zbrojeva, dok jedinice za usporedbu čine pojedini izborni redci. Nazivnik se odnosi na birače na obrađenim biračkim
mjestima, pa ga ne zamjenjujemo drugim ukupnim brojem birača bez provjere
obuhvata (Hrvatske}, 2024).

Zbrojeve za odaziv možemo ponovno provjeriti iz
tablice izbornih jedinica. Zbrajanje dvanaest redaka daje
3.558.089 birača i 2.216.763 pristupilih, jednako nacionalnom retku izvješća
(Hrvatske}, 2024). Njihov omjer daje objavljenih 62,30 %
(Hrvatske}, 2024).

Za glasačke listiće ovdje koristimo nacionalne vrijednosti iz početne
tablice (Hrvatske}, 2024). Ondje smo već provjerili njihov zbroj i razliku
prema broju pristupilih. Ovaj prikaz ne uključuje zasebnu provjeru svih
izbornih i manjinskih redaka za listiće.

### Doseg revidirane tvrdnje

Izbor jedinica I.–X. daje 61,48 %, a svih jedinica I.–XII. 62,30 %, uz razliku
od 0,82 postotna boda (Hrvatske}, 2024). Uz rezultat zato uvijek navodimo
obuhvat. Uži skup koristimo samo ako imamo zasebno obrazloženo pitanje o tim
jedinicama.

DIP-ova tablica omogućuje opis zabilježenog odaziva u navedenom obuhvatu.
Redci izbornih jedinica mogu poslužiti za usporedbu ili analizu povezanosti na
toj razini. Ne pokazuju zašto je pojedinac izašao, kojoj je listi dao potporu
ni što će se dogoditi na budućim izborima. Ovdje ih koristimo da bismo
odabrali točnu i provjerljivu formulaciju javne tvrdnje.

Administrativnom ukupnom broju ne pridružujemo marginu pogreške namijenjenu
anketnoj procjeni. I dalje mogu postojati nesigurnosti u obuhvatu,
definicijama, obradi i zapisima. Za svaku od njih ovo izvješće ne daje posebnu
brojčanu mjeru.

Provjerena tvrdnja glasi da je prema izvješću DIP-a za izbore za Hrvatski
sabor 2024. glasovanju pristupilo 2.216.763 od 3.558.089 birača na obrađenim
biračkim mjestima, odnosno 62,30 % (Hrvatske}, 2024). Zbroj važećih i
nevažećih listića iznosi 2.215.209, što je 1.554 manje (Hrvatske}, 2024).
Oznake ostaju različite jer opisuju različite faze postupka, bez obzira na
veličinu razlike.

Tvrdnju bismo ponovno provjerili kada bi se promijenio službeni izvor,
obuhvat, značenje oznake ili slaganje sastavnica s ukupnim vrijednostima.

## Protokol skeptičnoga čitanja

Provjeru odaziva možemo upotrijebiti i kao obrazac za druge javne tvrdnje. U
tablici se vraćamo na šest pitanja iz poglavlja o statističkom mišljenju, ali
sada uz svako možemo navesti što smo u izbornom izvješću doista provjerili.

| Revizijsko pitanje | Primjena na tvrdnju o odazivu |
|---|---|
| Koja je jedinica? | redak izborne jedinice. Nacionalni je redak kontrolni zbroj |
| Tko ili što nedostaje? | nema individualnih obilježja. Obuhvat su birači na obrađenim biračkim mjestima, a izbor I.–X. ili I.–XII. mora biti vidljiv |
| Koji je cilj tvrdnje? | opis zabilježenog odaziva, ne tvrdnja o pojedincu ili uzroku |
| Gdje je neizvjesnost? | aritmetika je provjerena. Obuhvat i moguća pogreška zapisa nisu svedeni na marginu ankete |
| Koje drugo objašnjenje ostaje? | broj prema listićima za drugo operativno pitanje. Uži obuhvat samo uz unaprijed obrazložen cilj |
| Tko snosi posljedice? | naslov može zamijeniti službene veličine i čitatelju pripisati zaključak koji tablica ne nosi |

: Šest revizijskih pitanja primijenjenih na isti javni slučaj. Izrada autora.

Odgovori se nadopunjuju. Provjera jedinice može promijeniti naš izbor
nazivnika, a drugo moguće objašnjenje pokazati da je početna usporedba bila
preuska. Koliko ćemo provjeravati ovisi i o posljedicama pogreške. Netočan
naziv u naslovu i odluka koja nekome uskraćuje pravo imaju različite
posljedice, ali u oba slučaja treba znati koga pogreška pogađa.

Zasebno određujemo vrstu tvrdnje i njezin doseg. Podaci mogu dobro opisati
administrativno obuhvaćenu populaciju, a da ništa ne govore o drugim izborima
ili uzrocima ponašanja pojedinaca.

| Dimenzija tvrdnje | Što DIP-ov dokaz dopušta u ovom primjeru |
|---|---|
| opis | poduprti su objavljeni odaziv i usklađenje službenih veličina |
| povezanost | samo na razini izbornih jedinica i tek nakon odgovarajuće analize. Nacionalni ukupni redak sam nije povezanost |
| generalizacija | ne izvan populacije i obuhvata službenog izvora |
| predviđanje | nije poduprto jer tablica nije model budućih izbora |
| uzročnost | nije poduprta jer iz tablice ne saznajemo zašto je netko pristupio |
| odluka | poduprta je omeđena urednička odluka o tome je li javna formulacija provjerljiva i poštena |

: Šest dimenzija tvrdnje na granici Dijela I. Izrada autora.

Uzročno objašnjenje zahtijeva podatke o nastanku opaženih razlika. Za objašnjenje ponašanja stanovnika trebali bismo i podatke na razini pojedinaca. Za odluku uz račun trebamo
razmotriti ciljeve i posljedice. Tablica je dovoljna za izbor provjerljive
formulacije naslova, dok bi promjena izborne politike zahtijevala dodatne
dokaze i vrijednosne kriterije.

| Provjera | Pitanje |
|---|---|
| brojnik | Koja dva službena brojnika ne smijemo zamijeniti? |
| anketa | Zašto uzorak od nekoliko tisuća ljudi ne uklanja moguću sustavnu pristranost ankete? |
| temeljna stopa | Ako su udio pronađenih ciljanih zapisa i stopa pogrešnih upozorenja poznati, koji još podatak treba za udio ispravnih upozorenja? |
| podrijetlo | Navedite bilo koje dvije zajedničke provjere za broj i sintetičku sliku. |

: Samoprovjera Dijela I. Izrada autora.

## Sažetak

Javni postotak možemo provjeriti kada znamo njegov izvor, jedinicu, brojnik,
nazivnik i obuhvat. Promjena bilo koje od tih sastavnica mijenja značenje
rezultata, a za tumačenje upozorenja o rijetkom ishodu trebamo i temeljnu
stopu. Veći uzorak može smanjiti slučajnu promjenjivost ankete, ali ne uklanja
sustavnu pristranost. Račun margine pogreške slijedi u poglavljima o
uzorkovanju i procjeni. Odgovore asistenta i sintetičke medije također pratimo
do izvora i načina nastanka. Pritom razlikujemo simulaciju, sintetički zapis,
hipotetski izlaz i izmišljeni dokaz. Šest revizijskih pitanja pomoći će nam i
pri pripremi vlastite tablice te izboru sažetka u sljedećem poglavlju.

## Pojmovi

postotak i postotni bod (*percentage and percentage point*), temeljna stopa
(*base rate*), margina pogreške (*margin of error*), podrijetlo tvrdnje
(*claim provenance*), sintetički zapis (*synthetic record*), protokol
skeptičnoga čitanja (*skeptical reading protocol*)

## Zadaci

### Konceptualni

Objasnite zašto broj pristupilih ne možemo zamijeniti zbrojem važećih i
nevažećih listića. Navedite što razlika od 1.554 pokazuje, a što ne možemo
zaključiti o njezinu uzroku (Hrvatske}, 2024). Zatim, bez novog računa,
objasnite zašto se u dvama hipotetskim primjerima mijenja udio ispravnih
upozorenja, iako detektor zadržava iste stope pronalaženja ciljanih zapisa i
pogrešnog označavanja.

### Računski

Koristite zbirnu tablicu generiranog skupa `populacija_medija` iz datoteke `data/populacija-medija-agregat.csv`. U generiranom skupu
portal je glavni izvor vijesti za 15.101 od 50.000 zamišljenih osoba, a
televizija za 10.827. Izračunajte udjele, razliku u
postotnim bodovima i relativnu razliku prema udjelu televizije. Uz rezultate
napišite da opisuju simulaciju. Dopušten je kalkulator ili proračunska tablica. Ne predaje se kod.

### Kritički

Polazište je nacionalni redak službene tablice „Odaziv birača” [Hrvatske}, 2024, str.
124]. Usporedite tri ponuđene uredničke prerade toga retka. To su „Na izborima
je glasovalo 62,30 % birača”, „DIP bilježi da je glasovanju pristupilo 62,30 %
birača na obrađenim biračkim mjestima” i „Većina građana podržala je
pobjedničke liste” (Hrvatske}, 2024). Za svaku navedite je li poduprta
prikazanim dokazom.
Najbolju preradu doradite tako da uključi brojnik, nazivnik, izvor i jednu
važnu granicu.

Razvrstajte generiranu populaciju iz računskog zadatka, pogrešni odgovor
modela iz okvira, umjetno stvorenu izbornu fotografiju označenu kao takvu i
nepostojeću stranicu izvješća navedenu kao izvor. Svakom predmetu dodijelite
oznaku simulacija, hipotetski izlaz modela, sintetički zapis ili izmišljeni
dokaz. Objasnite koji zaključak ne možemo opravdati takvim predmetom.

### Revizija modela

Provjerite odgovor modela iz okvira. Ponovno zbrojite listiće i izračunajte
razliku prema broju pristupilih (Hrvatske}, 2024). Napišite ispravljeni
odgovor u najviše četiri rečenice. Jasno odvojite ono što izvor potvrđuje od
objašnjenja za koje bismo trebali dodatni dokaz.
