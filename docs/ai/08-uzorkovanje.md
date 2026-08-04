# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | CLT stroj | simulirana populacija | pogl. 4, 7 |

**Vinjeta.**
Ismay i Kim zaključivanje predaju tako da čitatelj svaki postupak najprije vidi
kao ponovljeno uzorkovanje, a tek ga zatim susretne kao formulu (Ismay, 2019).
Redoslijed nije stvar ukusa. Formula za standardnu pogrešku zapisuje ishod
postupka koji se može odvrtjeti pred očima, pa je onaj tko je vidio postupak
čita kao sažetak, a onaj tko nije mora je primiti na vjeru.

Problem koji taj postupak rješava svakodnevan je. Istraživački tim treba reći
nešto o svim odraslim stanovnicima jednoga grada, a razgovarao je s njih
osamsto. Izračunata brojka točna je za tih osamsto ljudi i ni za koga drugoga.

Uzorak je pritom samo jedan ishod. Drugi uzorak iste veličine, izvučen istim
postupkom istoga dana, dao bi drugu sredinu i drugi udio.

Kako iz jednoga uzorka doznati koliko bi se rezultat mijenjao da smo uzorkovali
ponovno?

## Populacija, uzorak i pogreška uzorkovanja

Statistika postoji zbog jednog nesrazmjera. Tvrdnja se odnosi na skup jedinica
koji ne možemo izmjeriti u cijelosti, a podatak dolazi iz dijela koji smo
uspjeli obuhvatiti. **Populacija** je skup jedinica o kojima želimo zaključivati,
**uzorak** je dio jedinica koje smo stvarno promatrali, a razlika među njima
nije samo u veličini. Uzorak nastaje postupkom odabira, i taj postupak određuje
koje populacijske jedinice uopće imaju priliku postati podatak.

Mjere se razlikuju zajedno s time. Vrijednost izračunata na cijeloj populaciji
naziva se **parametar** i piše se grčkim slovom, pa je $\mu$ populacijska
sredina, a $\sigma$ populacijska standardna devijacija. Vrijednost izračunata
na uzorku naziva se **statistika** i piše se latinicom, kako je poglavlje o
sažimanju podataka već koristilo $\bar{x}$ za uzoračku sredinu i $s$ za
uzoračku standardnu devijaciju. Slovo $n$ i dalje označava broj opažanja u
uzorku, a $N$ veličinu populacije. Statistika je procjena parametra i gotovo
nikada mu nije jednaka.

U stvarnom istraživanju to razlikovanje ostaje neprovjerljivo, jer parametar
nije poznat. Kad bi bio poznat, uzorak ne bi ni trebao. Ovo poglavlje zato radi
na simuliranoj populaciji od `r hr_broj(s8$N, 0)` odraslih osoba izmišljenoga
grada, koju je proizveo kod uz fiksno sjeme i koja ne opisuje nijedno stvarno
mjesto. Njezina je vrijednost upravo u tome što je izmišljena, jer se samo za
izmišljenu populaciju smije reći koliki joj je prosjek prije nego što se
izvuče ijedan uzorak. Prosječno povjerenje u medije u toj populaciji iznosi
`r hr_broj(s8$mu, 2)` na ljestvici od 1 do 10 uz standardnu devijaciju
`r hr_broj(s8$sigma, 2)`, prosječno se dnevno prati
`r hr_broj(s8$mu_minuta, 1)` minuta medijskog sadržaja, a udio onih kojima je
portal primarni izvor vijesti iznosi
`r paste0(hr_broj(100 * s8$udio_portal, 1), " %")`.

Izvučemo li iz te populacije jedan uzorak od stotinu osoba, prosječno
povjerenje u njemu iznosi `r hr_broj(s8$uzorak_sredina, 2)`, a udio korisnika
portala `r paste0(hr_broj(100 * s8$uzorak_portal, 1), " %")`. Obje su
vrijednosti blizu populacijskih, ali nijedna nije jednaka. Razmak koji je pritom
nastao ima ime, i to ime nije optužba.

**Pogreška uzorkovanja** je razlika između vrijednosti izračunate na uzorku i
vrijednosti koju ima cijela populacija, a nastaje zato što je izmjeren dio
umjesto cjeline.

Riječ pogreška ovdje ne označava propust u radu. Nitko nije pogrešno prepisao
odgovor ni krivo postavio pitanje. Kada bi cijeli postupak bio proveden
besprijekorno, razmak bi i dalje postojao, jer stotinu ljudi nije pedeset
tisuća ljudi. Razlikovanje te neizbježne promjenjivosti od pristranosti koja
nastaje lošim odabirom nosi ostatak poglavlja, i vrijedi ga zadržati na umu od
prve stranice.

## Kad uzorkovanje ponovimo

Jedan uzorak ne govori koliko je njegova procjena stabilna. Da bismo to
doznali, moramo napraviti ono što stvarno istraživanje nikada ne radi, a to je
ponoviti cijeli postupak od početka. Tri neovisna uzorka od po stotinu osoba iz
naše populacije daju prosječno povjerenje `r hr_broj(s8$tri[1], 2)`,
`r hr_broj(s8$tri[2], 2)` i `r hr_broj(s8$tri[3], 2)`. Sva tri broja opisuju
istu populaciju, izračunata su istim postupkom i međusobno se razlikuju za
`r hr_broj(s8$raspon_tri, 2)` boda.

Ponovimo li to ne tri nego tri tisuće puta, dobiveni prosjeci prestaju biti
niz pojedinačnih ishoda i postaju raspodjela s vlastitim oblikom, središtem i
širinom. Ta raspodjela nije opis ljudi. Ona je opis onoga što bi se događalo s
našom procjenom.

**Distribucija uzorkovanja** je raspodjela vrijednosti koje bi neka statistika
poprimila kroz mnogo ponovljenih uzoraka iste veličine iz iste populacije.

Razlika između te raspodjele i raspodjele samih opažanja najvažnije je
razlikovanje u cijelom poglavlju, a lako se izgubi jer obje imaju sredinu i
standardnu devijaciju. Raspodjela opažanja odgovara na pitanje koliko se ljudi
međusobno razlikuju. Distribucija uzorkovanja odgovara na pitanje koliko bi se
razlikovala naša procjena da smo imali sreće drugačije.

*Slika. Raspodjela pojedinačnih ocjena povjerenja u simuliranoj populaciji i raspodjela sredina tri tisuće uzoraka od po sto osoba, na zajedničkoj osi.*

Obje raspodjele leže oko iste vrijednosti, što znači da uzoračka sredina ne
promašuje sustavno ni prema gore ni prema dolje. Procjenitelj koji ima to
svojstvo naziva se **nepristranim**. Zbijenost donjeg panela nije, međutim,
svojstvo ljudi nego svojstvo postupka, i upravo je ona ono što nas zanima kad
pitamo koliko smijemo vjerovati jednoj brojci.

## Standardna pogreška

Širinu distribucije uzorkovanja mjerimo isto kao svaku drugu raspršenost,
standardnom devijacijom. Da bi bilo jasno da je riječ o raspršenosti procjene, a
ne o raspršenosti ljudi, ta mjera nosi vlastito ime.

**Standardna pogreška** je standardna devijacija distribucije uzorkovanja, pa
opisuje koliko bi tipično varirala procjena kroz ponovljene uzorke.

U našoj simulaciji standardna devijacija pojedinačnih ocjena iznosi
`r hr_broj(s8$sigma, 2)`, a standardna devijacija tri tisuće uzoračkih sredina
`r hr_broj(s8$se_empirijska, 3)`. Omjer tih dviju brojki iznosi
`r hr_broj(s8$omjer, 1)`. Uzorci su imali po stotinu osoba, a korijen iz sto je
deset, i to poklapanje nije slučajno.

Razlog se vidi bez računa. Sredina raspoređuje ukupno izmjereno na sve
ispitanike, pa u uzorku od deset ljudi jedan neobičan odgovor nosi desetinu
rezultata, a u uzorku od tisuću ljudi tisućinu. Kako uzorak raste, pojedinačna
odstupanja imaju sve manju priliku pomaknuti zbroj, i to ne zato što bi
odstupanja nestajala, nego zato što se u većem uzorku sve češće međusobno
poništavaju. Dobitak zato ne raste s brojem ljudi nego sa svojim korijenom.

Simulacija dosad koristi **jednostavni slučajni uzorak** (*simple random
sample*). Svaki mogući skup od $n$ jedinica ima jednaku vjerojatnost izbora, a
iz konačne se populacije izvlači bez vraćanja. Izraz u nastavku točan je za
neovisna izvlačenja s vraćanjem i služi kao aproksimacija za jednostavni
slučajni uzorak bez vraćanja kada je $n$ malen prema $N$. Nije opća formula za
svaki uzorak u kojem je odabir uključivao neki slučajni korak.

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

U toj jednakosti $SE_{\bar{x}}$ označava standardnu pogrešku uzoračke sredine,
$\sigma$ standardnu devijaciju populacije, a $n$ veličinu uzorka. Za naš slučaj
formula daje `r hr_broj(s8$se_teorijska, 4)`, dok je simulacija dala
`r hr_broj(s8$se_empirijska, 4)`. Dvije brojke dolaze iz dva potpuno različita
smjera, jedna iz algebre i druga iz tri tisuće ponovljenih izvlačenja, a
poklapaju se na tri decimale.

Izvlačenje bez vraćanja donosi još malo preciznosti. Svaka odabrana jedinica
uklanja dio preostale neizvjesnosti, a nakon popisa cijele populacije pogreška
uzorkovanja mora nestati. To smanjenje sažima **korekcija za konačnu
populaciju** (*finite-population correction*), koja jednostavni izraz množi
korijenom omjera preostaloga i početnoga broja dostupnih jedinica.

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
  \sqrt{\frac{N-n}{N-1}}
$$

Drugi korijen blizu je jedinici kada je uzorak malen dio populacije, pa ga tada
prvi izraz dobro aproksimira. Kako se $n$ približava vrijednosti $N$, faktor se
smanjuje i pri popisu cijele populacije postaje nula. Simulacija bez vraćanja
tu korekciju proizvodi sama, dok je stupac s formulom u tablici u nastavku
namjerno zanemaruje kao aproksimaciju za veliku populaciju.

U stvarnom istraživanju $\sigma$ nije poznata, pa je u aproksimaciji za veliku
populaciju zamjenjuje uzoračka standardna devijacija $s$. Kada korekcija za
konačnu populaciju nije zanemariva, procjena standardne pogreške usklađuje i
tu korekciju s djeliteljem koji koristi $s$. Program to obavlja bez novoga
pojma, a ovdje je važno zadržati granicu prema kojoj se populacijski izraz ne
pretvara u procjenu samo zamjenom jednoga slova. Tu zamjenu poglavlje o
sažimanju podataka je pripremilo kada je varijancu uvelo s djeliteljem umanjenim
za jedan i tu odluku ostavilo kao tvrdnju bez dokaza. Simulacija je sada može
provjeriti. Izvučemo li četiri tisuće uzoraka od po deset osoba i u svakome
izračunamo prosjek kvadriranih odstupanja s djeliteljem deset, prosječan
rezultat iznosi
`r hr_broj(s8$var_n, 2)`, dok prava populacijska varijanca iznosi
`r hr_broj(s8$var_prava, 2)`. Isti račun s djeliteljem devet daje
`r hr_broj(s8$var_n1, 2)`. Djelitelj $n$ podcjenjuje sustavno, i to zato što
odstupanja mjeri od uzoračke sredine, koja je sama izračunata iz istih tih
opažanja i zato im leži bliže nego prava populacijska sredina.

Praktična posljedica korijena vidljiva je čim se ispišu veličine uzorka jedna
do druge. Preciznost raste, ali sve sporije, pa svako sljedeće poboljšanje
košta nesrazmjerno više od prethodnoga.

*Slika. Standardna pogreška sredine povjerenja pri osam veličina uzorka, izračunata formulom i izmjerena na tisuću i petsto ponovljenih uzoraka. Izrada autora.*

Prijelaz s deset na sto osoba prepolovljuje standardnu pogrešku dvaput. Prijelaz
sa sto na tisuću, koji stoji desetostruko više, prepolovljuje je nešto više od
jednom i pol puta. Da bi se preciznost udvostručila, uzorak se mora
učetverostručiti, i ta aritmetika objašnjava zašto ankete rijetko rastu preko
nekoliko tisuća ispitanika.

## Oblik koji se pojavljuje

Zbijenost distribucije uzorkovanja objašnjena je. Njezin oblik nije, a upravo
je oblik ono što omogućuje sve što slijedi. Pogledajmo varijablu koja je
koliko god želimo daleko od zvonaste krivulje. Spremnost na plaćanje vijesti u
našoj populaciji ima `r paste0(hr_broj(s8$platiti_nula, 1), " %")` nula i dugi
rep prema velikim iznosima, uz koeficijent asimetrije
`r hr_broj(s8$platiti_asimetrija, 1)`. Nijedan udžbenički postupak ne bi tu
raspodjelu nazvao normalnom.

Izvučemo li iz nje uzorke od po pet osoba i pogledamo raspodjelu njihovih
sredina, asimetrija ostaje visoka i iznosi
`r hr_broj(s8$clt_asimetrija[["5"]], 2)`. Pri uzorcima od petnaest osoba pada na
`r hr_broj(s8$clt_asimetrija[["15"]], 2)`, pri trideset na
`r hr_broj(s8$clt_asimetrija[["30"]], 2)`, a pri sto na
`r hr_broj(s8$clt_asimetrija[["100"]], 2)`. Raspodjela sredina ispravlja se sama
od sebe, iako se izvorna raspodjela nije ni za što promijenila.

*Slika. Izrazito asimetrična populacijska varijabla i raspodjele njezinih uzoračkih sredina pri četiri veličine uzorka. Svaki panel ima vlastitu os.*

Ono što smo upravo vidjeli ima ime i status teorema. **Središnji granični
teorem** (*central limit theorem*) u ovom modelu tvrdi da se distribucija
uzorkovanja sredine približava normalnoj raspodjeli kako jednostavni slučajni
uzorak raste, pod uvjetom da populacija ima konačnu varijancu i da nekolicina
jedinica ne nosi gotovo cijeli zbroj. Uobičajeno pravilo palca stavlja granicu
oko trideset opažanja, ali naša simulacija pokazuje i zašto je to pravilo grubo.
Kod izrazito asimetrične varijable trideset osoba nije bilo dovoljno da
asimetrija nestane, dok bi kod raspodjele koja je već gotovo simetrična i deset
osoba bilo dovoljno. Granica ovisi o obliku i repovima izvorne raspodjele, a ne
o okruglom broju.

Praktična vrijednost teorema je u tome što mnoge postupke oslobađa pretpostavke
da su pojedinačna opažanja normalno raspodijeljena. Ne uklanja pretpostavke o
načinu odabira ni o ovisnosti među jedinicama. U složenijem nacrtu uzorka oblik
i širinu raspodjele procjene određuju i težine te skupine iz kojih jedinice
zajedno ulaze u uzorak, pa se zaključivanje mora prilagoditi tim obilježjima.

## Interakcija — CLT stroj

Simulacija koja je upravo prošla kroz četiri veličine uzorka fiksirala je oblik
populacije. Widget odvaja te dvije stvari, pa se oblik populacije, veličina
uzorka i broj ponavljanja mijenjaju neovisno. Time postaje vidljivo koje je
svojstvo posljedica čega, jer oblik raspodjele sredina ovisi o obojemu, a
njezina širina o veličini uzorka i raspršenosti populacije. Pri fiksnoj
populaciji širina se smanjuje s korijenom veličine uzorka.

*Slika. Izvorna populacija i raspodjela sredina mnogih uzoraka na zajedničkoj osi. Okomita crta označuje populacijsku sredinu simulacije.*

**Što isprobati.**

1. Odaberite simetričnu populaciju i uzorak veličine dva pa usporedite širine dvaju histograma.
2. Promijenite populaciju u desno asimetričnu bez povećanja uzorka.
3. Povećajte uzorak na četrdeset i odvojeno opišite promjenu oblika i širine raspodjele sredina.
4. Odaberite dvovršnu populaciju i pronađite veličinu uzorka pri kojoj se dvije populacijske skupine više ne vide u sredinama.

## Zašto ankete od osamsto ljudi rade

Anketni rezultati rijetko su sredine. Češće su udjeli, pa se pitanje preciznosti
postavlja za **uzorački udio**, koji označavamo s $\hat{p}$ i koji procjenjuje
populacijski udio. Logika ostaje ista, jer je udio prosjek niza nula i jedinica,
pa ga središnji granični teorem pokriva jednako kao svaku drugu sredinu. Mijenja
se samo to što raspršenost udjela ne treba mjeriti posebno. Kod varijable koja
poprima samo dvije vrijednosti raspršenost je određena samim udjelom, najveća je
kada je populacija podijeljena napola i pada kako se udio primiče nuli ili
jedinici.

Sljedeći izraz procjenjuje standardnu pogrešku jednoga ukupnog udjela u istom
modelu jednostavnoga slučajnog uzorka i velike populacije. Uzorački udio
$\hat{p}$ ulazi umjesto nepoznatoga populacijskog udjela, pa je i dobivena
standardna pogreška procjena.

$$
SE_{\hat{p}} = \sqrt{\frac{\hat{p}\,(1 - \hat{p})}{n}}
$$

Kod jednostavnoga slučajnog uzorka bez vraćanja izraz se množi istom korekcijom
za konačnu populaciju kao i standardna pogreška sredine. Kod nejednakih
vjerojatnosti odabira ili grupnog uzorkovanja ne smije se prenijeti bez
prilagodbe nacrtu.

Polovica širine intervala oko procjene naziva se **margina pogreške** (*margin
of error*), i to je brojka koju medijski izvještaji navode uz anketu. Budući da
je raspršenost najveća pri udjelu od 50 %, uvrštavanjem te vrijednosti dobiva se
najgori slučaj, koji vrijedi bez obzira na to kakav će rezultat ispasti. Za
uobičajenu razinu od 95 % margina se tada svodi na približno jedan podijeljen
korijenom veličine uzorka.

Margina u nastavku jednaka je 1,96 puta procijenjena standardna pogreška, a
potreban uzorak dobiven je obrnutim računom iz zadane margine. Formula za
standardnu pogrešku nasljeđuje jednostavni slučajni nacrt i aproksimaciju
velikom populacijom. Množenje s 1,96 i obrnuti račun dodatno traže da normalna
aproksimacija bude razumna, što nije slučaj kada je očekivani broj jedinica u
jednoj od dviju kategorija malen.

*Slika. Najveća margina pogreške za udio pri razini od 95 % i uzorak potreban za zadanu marginu. Izrada autora.*

Tablica opisuje samo odnos veličine i preciznosti za jedan ukupni udio u
jednostavnom slučajnom uzorku, pri razini od 95 % i uz zanemarenu korekciju za
konačnu populaciju. U tom modelu uzorak od osamsto ljudi daje najveću marginu
od približno
`r paste0("±", hr_broj(100 * s8$moe(800), 1), " %")`, i ta je preciznost dovoljna
da se razaznaju razlike od desetak postotnih bodova, a nedovoljna za razlike od
dva ili tri. Druga procjenjivana veličina, drukčiji nacrt ili uži zahtjev za
preciznošću mijenjaju taj račun.

Odatle slijedi pravilo čitanja koje vrijedi više od svega ostaloga u ovom
odjeljku. Kada izvještaj navodi da prva opcija ima 32 %, a druga 29 %, razlika
od tri postotna boda manja je od margine iz prikazanoga modela, pa sama ta
usporedba ne podupire tvrdnju da je prva opcija ispred druge. Margina se odnosi
na svaku procjenu zasebno, a razlika dvaju udjela ima vlastitu nesigurnost koju
treba izračunati iz zajedničkoga nacrta.

U pojednostavljenoj formuli za marginu pogreške nema veličine populacije zato
što je korekcija za konačnu populaciju zanemarena. Kada je udio uzorkovanih
jedinica malen, taj je faktor blizu jedinici i veličina populacije malo mijenja
preciznost. Provjeriti se to može izravno. Uzorak od osamsto osoba izvučen iz
cijele naše populacije daje standardnu pogrešku
`r hr_broj(s8$se_velika, 4)`, a isti takav uzorak izvučen iz njezina deset puta
manjeg dijela daje `r hr_broj(s8$se_mala, 4)`. Manja populacija ovdje daje nešto
precizniju procjenu ponajprije zato što isti uzorak obuhvaća veći dio nje.
Raspršenosti dviju populacija iznose `r hr_broj(s8$sigma, 3)` i
`r hr_broj(s8$sigma_mala, 3)`, pa nisu posve jednake. Formula s korekcijom
predviđa standardne pogreške `r hr_broj(s8$se_velika_fpc, 4)` i
`r hr_broj(s8$se_mala_fpc, 4)`, koje su blizu simuliranim vrijednostima i
odvajaju učinak veličine populacije od te male razlike u raspršenosti.

Tvrdnja da je uzorak od približno tisuću ljudi dovoljan nema smisla bez pet
odluka. Najprije se imenuje procjenjivana veličina, jer ukupni udio, sredina,
rijedak udio i razlika dviju skupina nemaju istu standardnu pogrešku. Zatim se
navodi nacrt, jer težine i grupiranje mijenjaju preciznost, te postupak odabira
i odaziva, jer veličina ne popravlja sustavno izostavljene ljude. Procjena za
podskupinu oslanja se na broj osoba u toj podskupini, a ne na ukupan uzorak.
Tek željena preciznost određuje je li preostali broj dovoljan. Tisuću je zato
korisna orijentacija za jedan ukupni udio u pojednostavljenom nacrtu, a ne
jamstvo za svaki cilj, nacrt, populaciju ili usporedbu.

Preostaje reći što margina pogreške ne pokriva, jer se upravo o tome najčešće
šuti. Ona mjeri isključivo promjenjivost koja dolazi od slučajnog izvlačenja
ispitanika. Ne mjeri ljude koji nikada nisu bili u okviru iz kojega se
uzorkovalo, ne mjeri one koji su bili pozvani ali nisu odgovorili, i ne mjeri
učinak formulacije pitanja ni redoslijeda ponuđenih odgovora. Anketa uz koju
piše da je margina ±3 % nudi tri postotna boda opreza za jedan izvor pogreške i
nijedan za ostale tri. Rečenica da je nešto „unutar margine pogreške" zato je
tvrdnja o slučaju, a ne potvrda da je istraživanje dobro provedeno.

## Nacrt uzorka i pristranost odabira

Jednostavni slučajni uzorak nije jedini valjani način slučajnog odabira. U
širem **vjerojatnosnom uzorkovanju** svaka jedinica ima poznatu i pozitivnu
vjerojatnost ulaska, ali te vjerojatnosti ne moraju biti jednake. Jedinica koja
je imala upola manju priliku ulaska tada u procjeni zastupa približno dvostruko
više populacijskih jedinica. Taj doprinos zapisuje **težina uzorka**, koja se
temelji na obrnutoj vjerojatnosti odabira. Neponderirana sredina u takvu nacrtu
previše predstavlja često birane jedinice, ali ni ispravno ponderiranje samo ne
može vratiti skupinu koju okvir uopće nije pokrivao.

Drugi nacrti najprije biraju skupine poput kućanstava, škola ili naselja, a
zatim jedinice unutar njih. Takvo **grupno uzorkovanje** štedi terenski rad, ali
osobe iz iste skupine često su sličnije nego nasumično izabrane osobe iz cijele
populacije. Stotinu ljudi iz nekoliko skupina zato obično nosi manje neovisne
informacije od stotinu ljudi raspršenih po populaciji. Obična formula s
korijenom iz $n$ tu bi preciznost prikazala prevelikom.

**Učinak nacrta** uspoređuje varijancu procjene pod stvarnim nacrtom s
varijancom koju bi dao jednostavni slučajni uzorak iste nominalne veličine.
Njegov prijevod u broj čitatelju daje **efektivna veličina uzorka**, odnosno
veličina jednostavnoga slučajnog uzorka koja bi nosila približno jednaku
preciznost. Grupiranje i vrlo nejednake težine često smanjuju efektivnu
veličinu, dok je pažljivo raslojavanje može povećati. Učinak nacrta pripada
određenoj procjeni i ne mora biti isti za svaki udio ili sredinu u istoj anketi.

Za takve nacrte procjena, standardna pogreška i margina moraju se računati
postupkom koji poznaje težine, skupine i eventualne slojeve. Čitatelj ne mora
izvoditi te formule, ali mora u izvještaju tražiti kako je nacrt uključen u
račun. Nijedna od dviju jednostavnih formula iz ovoga poglavlja ne prenosi se
nepromijenjena na nejednake vjerojatnosti ili grupiranje.

Drukčiji problem nastaje kada vjerojatnosti odabira nisu poznate. Prigodni
uzorak najčešći je oblik takvog pada. Istraživač anketira one koji su mu
dostupni, obično studente vlastitog kolegija. U našoj populaciji skupina
mlađih od dvadeset pet godina s višim obrazovanjem broji
`r hr_broj(s8$prigodni_n, 0)` osoba i njihovo prosječno povjerenje u medije
iznosi `r hr_broj(s8$prigodni_sredina, 2)`, naspram
`r hr_broj(s8$mu, 2)` u cijeloj populaciji. Razmak je veći od cijele margine
pogreške ankete na tisuću ljudi, a ne bi se smanjio ni da smo anketirali sve te
mlade ljude do posljednjega.

Samoodabir djeluje suptilnije jer proizvodi velike uzorke. Zamislimo mrežnu
anketu na koju odgovaraju oni koji su na internetu, koji su vidjeli poziv i koji
su se odlučili javiti, pri čemu svaki od tih koraka propušta drugačiji dio
populacije. Simulacija takvog postupka na našoj populaciji daje uzorak od
`r hr_broj(s8$online_n, 0)` osoba, dakle mnogostruko veći od bilo koje
telefonske ankete. Njegov prosjek dobi iznosi `r hr_broj(s8$online_dob, 1)`
godina naspram `r hr_broj(s8$dob, 1)` u populaciji, udio korisnika društvenih
mreža `r paste0(hr_broj(100 * s8$online_mreze, 1), " %")` naspram
`r paste0(hr_broj(100 * s8$udio_mreze, 1), " %")`, a prosječno povjerenje
`r hr_broj(s8$online_sredina, 2)` naspram `r hr_broj(s8$mu, 2)`.

Treći oblik pogađa i istraživanja koja su sve napravila ispravno. Uzorak može
biti izvučen savršeno slučajno iz besprijekornog popisa, a onda dio odabranih
ne odgovori. Ako oni koji ne odgovaraju nalikuju onima koji odgovaraju, gubi se
samo veličina uzorka i s njom nešto preciznosti. Ako se razlikuju, a upravo se
najčešće razlikuju po zauzetosti, zanimanju za temu i povjerenju u onoga tko
pita, tada preostali dio uzorka više nije slučajan bez obzira na to kako je
odabran. Postupak odabira i postupak odaziva dva su različita filtra, i drugi
je izvan nadzora istraživača.

Kod tolikog uzorka standardna pogreška je sitna, pa bi izvještaj mogao objaviti
vrlo uzak interval oko sustavno pogrešne vrijednosti. To je najvažnija
asimetrija u poglavlju. Slučajna promjenjivost pada s veličinom uzorka i mjeri
se standardnom pogreškom, dok pristranost odabira ne ovisi o veličini uzorka i
standardna je pogreška uopće ne vidi. Velik pristran uzorak zato je opasniji od
malog slučajnog, jer nosi jednaku netočnost i uz nju uvjerljivost koju mala
brojka nikada ne bi imala.

**Statistika u divljini.**
**Deset milijuna listića i pogrešan pobjednik.** Časopis *Literary Digest*
razaslao je uoči američkih izbora 1936. milijune probnih listića i na temelju
vraćenih odgovora objavio predviđanje koje je promašilo pobjednika, dok su
istodobne ankete na uzorcima manjima za red veličine pogodile ishod
(Squire, 1988).

Uzorak nije zakazao zbog veličine. Popisi iz kojih su adrese izvučene
obuhvaćali su imućnija kućanstva sustavno češće od ostalih, a listić je vratio
tek dio onih koji su ga primili, pa se skupina koja je odgovorila razlikovala od
skupine koja nije (Squire, 1988). Oba filtra djeluju u istom smjeru i nijedan se
ne popravlja slanjem još listića. Slučaj se često prepričava kao upozorenje da
uzorci trebaju biti veliki, iako pokazuje upravo suprotno.

**Pitajte model.**
Asistent može napisati simulaciju distribucije uzorkovanja u nekoliko sekundi,
ali treba mu odvojeno zadati populaciju, postupak odabira, veličinu uzorka i
statistiku koja se računa. Kod jednostavnoga slučajnog uzorka provjeravamo
uzorkuje li s vraćanjem samo kada je to namjera. Kod složenoga nacrta tražimo da
u račun unese težine, skupine i slojeve umjesto da primijeni običnu formulu s
korijenom iz $n$. Najčešća pogreška u odgovoru ipak nije u kodu nego u rečenici
koja ga prati, gdje se raspršenost pojedinaca predstavi kao standardna pogreška
procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno navedi standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

## Razrađeni primjer

Cijeli aparat zaključivanja koji slijedi u ostatku knjige svodi se na jednu
petlju. Izvuci uzorak, izračunaj mjeru, ponovi mnogo puta i pogledaj što je
nastalo. Sve ostalo su prečice do rezultata te petlje. Vrijedi je zato jednom
vidjeti ispisanu u cijelosti, na najgoroj varijabli koju naša populacija ima.

Pitanje glasi koliko su prosjeci pouzdani kada se računaju na varijabli s
mnoštvom nula i dugim repom, dakle u okolnostima u kojima bi se svaka
pretpostavka o zvonastom obliku odmah raspala. Postavljamo ga tako da usporedimo
dvije veličine uzorka i za obje pogledamo gdje se sredine skupljaju i koliko su
raspršene.

Funkcija `replicate` ponavlja zadani izraz traženi broj puta i skuplja rezultate
u vektor, pa je ona jedini novi glagol u ovom bloku. Prosjek četiri tisuće
sredina iz uzoraka od pet osoba iznosi `r hr_broj(s8_p$m5, 2)` kuna, a iz
uzoraka od šezdeset osoba `r hr_broj(s8_p$m60, 2)` kuna, dok prava populacijska
vrijednost iznosi `r hr_broj(s8_p$mu, 2)` kuna. Nijedna od dviju veličina uzorka
ne promašuje cilj sustavno, što je nepristranost o kojoj je već bilo riječi.

Razlikuju se u nečemu drugome. Standardna pogreška pri pet osoba iznosi
`r hr_broj(s8_p$se5, 2)`, a pri šezdeset `r hr_broj(s8_p$se60, 2)`, dakle
`r hr_broj(s8_p$omjer, 1)` puta manje. Odnos je približno jednak korijenu iz
dvanaest, koliko puta je veći uzorak, i time se algebra iz odjeljka o
standardnoj pogrešci potvrđuje na varijabli za koju bi se očekivalo da je
najviše izmiče. Vrijedi zapaziti i što petlja nije popravila. Uzorak od pet
osoba i dalje daje raspodjelu sredina koja je vidljivo iskrivljena, pa
nepristranost i normalnost nisu isto svojstvo i ne stižu u istom trenutku.

Vrijedi zapaziti i što je u ovom bloku bilo moguće samo zato što je populacija
izmišljena. Prvi redak poziva `populacija_medija` i time čini nešto što nijedno
stvarno istraživanje ne može, jer izvlači uzorke iz cjeline kojoj bi inače bilo
nemoguće pristupiti. Istraživač koji radi s podacima ima jedan uzorak i nijednu
mogućnost da petlju stvarno pokrene. Sve što slijedi u knjizi način je da se do
rezultata te petlje dođe bez nje, a poglavlje o procjeni prvo je od tih
zaobilaženja. Ono uzorku dopušta da nakratko preuzme ulogu populacije, i time
istu petlju vrati u ruke nekome tko ima samo osamsto ispitanika.

## Sažetak

Uzorak je jedan ishod postupka odabira, a distribucija uzorkovanja opisuje kako
bi se procjena mijenjala kroz ponovljene izvlačenja. Njezinu širinu mjeri
standardna pogreška, koja pripada procjeni, a ne pojedincima, i pada s korijenom
veličine jednostavnoga slučajnog uzorka, uz korekciju kada uzorak obuhvaća
znatan dio konačne populacije. Složeniji nacrti mogu zahtijevati ponderirane
procjene, a nesigurnost se računa postupkom koji uvažava težine, skupine i
slojeve. Učinak nacrta i efektivna veličina uzorka sažimaju posljedice toga
nacrta. Nijedan od tih računa ne popravlja pristran odabir, jer standardna
pogreška mjeri samo ono što bi se mijenjalo kroz ponavljanja istoga postupka, a
ne ono što je taj postupak sustavno izostavio. Poglavlje o procjeni uzet će tu
raspodjelu i iz nje izgraditi raspon oko vrijednosti koju ne možemo izravno
vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), parametar (*parameter*),
statistika (*statistic*), pogreška uzorkovanja (*sampling error*), distribucija
uzorkovanja (*sampling distribution*), nepristranost (*unbiasedness*),
standardna pogreška (*standard error*), središnji granični teorem (*central
limit theorem*), uzorački udio (*sample proportion*), margina pogreške (*margin
of error*), jednostavni slučajni uzorak (*simple random sample*), korekcija za
konačnu populaciju (*finite-population correction*), težina uzorka (*sampling
weight*), grupno uzorkovanje (*cluster sampling*), učinak nacrta (*design
effect*), efektivna veličina uzorka (*effective sample size*), prigodni uzorak
(*convenience sample*), samoodabir (*self-selection*)

## Zadaci

### Konceptualni

Razlikujte raspodjelu pojedinačnih opažanja od distribucije uzoračkih sredina.
Za svaku navedite što joj je jedinica, što mjeri njezina širina i što se s njom
događa kada uzorak naraste. Predajte skicu obiju raspodjela i dva popratna
objašnjenja.

### Računski

Upotrijebite tablicu margine pogreške iz ovog poglavlja. Anketa na tisuću
ispitanika izvještava da prva opcija ima 44 %, a druga 39 %. Izračunajte marginu
pogreške te ankete, presudite je li razlika od pet postotnih bodova veća od
margine i objasnite zašto usporedba dviju procjena traži više opreza od
prosudbe svake zasebno. Zatim odredite koliki bi uzorak trebao da margina padne
na polovicu i provjerite rezultat u istoj tablici. Postupak s cijelim skupom
podataka opisan je u Dodatku A.

### Kritički

Pročitajte slučaj časopisa *Literary Digest* iz okvira o statistici u divljini
(Squire, 1988). Objasnite zašto povećanje broja poslanih listića ne bi ispravilo
nijedan od dvaju opisanih problema i navedite koji bi podatak o toj anketi bio
najkorisniji za prosudbu njezine vjerodostojnosti. Predajte jedan odlomak.

### Revizija modela

Ocijenite analizu modela iz okvira o pogrešci. Izdvojite tvrdnju koja je točna,
imenujte zamjenu dviju razina varijabilnosti i napišite ispravljenu verziju
druge rečenice koja zadržava sve što je u njoj bilo točno.
