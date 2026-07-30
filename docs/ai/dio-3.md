# DIO III: OD UZORKA DO POPULACIJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.


---

# Vjerojatnost koliko treba

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Simulator novčića i A/B kampanje | simulacija | pogl. 4 |

**Vinjeta.**
Simmons i suradnici pokazali su kako velik broj razumno zvučećih analitičkih
odluka može povećati vjerojatnost lažno pozitivnog rezultata (Simmons, 2011).
Svaka pojedina odluka mogla je izgledati bezazleno. Problem je postao vidljiv
tek kada se promatrao cijeli niz mogućih putova kroz podatke.

Istraživač zato ne pita samo je li opaženi rezultat moguć pod jednom
pretpostavkom. Mora pitati koliko je prilika postupak dao slučajnosti da
proizvede nešto što izgleda uvjerljivo.

Kako računati s neizvjesnošću bez pretvaranja vjerojatnosti u obećanje o jednom
događaju?

## Neizvjesnost kao raspodjela

**Vjerojatnost** povezuje događaj sa skupom mogućih ishoda. U dugom nizu
ponavljanja može se čitati kao relativna učestalost. U situaciji koja se neće
ponoviti može izražavati stupanj uvjerenja pod jasno navedenim informacijama.
Ta dva čitanja ne moraju biti suparnici, ali zahtijevaju da kažemo na što se
broj odnosi.

Pravilo komplementa prevodi vjerojatnost događaja u vjerojatnost da se događaj
ne dogodi. Zbrajanje pripada međusobno isključivim ishodima, dok množenje
povezuje zajedničko pojavljivanje neovisnih događaja. Najčešća pogreška nije
računska, nego sadržajna pretpostavka da su događaji neovisni samo zato što je
to zgodno za račun.

Binomna situacija ima ponovljene pokušaje, dva ishoda i jednaku vjerojatnost
uspjeha u svakom pokušaju. Glasanje, klik i odgovor na pitanje mogu se tako
modelirati samo kada jedinice i pokušaji dovoljno dobro odgovaraju tim
uvjetima. Model nije opis cijelog svijeta, nego kontrolirana slika dijela
procesa.

## Obrasci mnogih ponavljanja

Pojedinačni ishodi mogu biti neuredni, dok raspodjela velikog broja ishoda
pokazuje stabilan oblik. Normalna krivulja opisuje mnoge takve obrasce oko
središta. Pravilo približnih područja oko sredine korisno je za orijentaciju,
ali se ne primjenjuje na svaku asimetričnu ili višemodalnu raspodjelu.

QQ prikaz uspoređuje poredane podatke s poredanim vrijednostima očekivanima pod
odabranom raspodjelom. Točke blizu pravca podupiru približan oblik, dok
sustavna zakrivljenost pokazuje odstupanje. Prikaz ne izdaje presudu o tome je
li analiza dopuštena. On pokazuje gdje pretpostavka pristaje, a gdje se lomi.

## Interakcija — Simulator novčića i A/B kampanje

Simulator povezuje jednostavno bacanje novčića s A/B kampanjom.
Čitatelj mijenja stvarnu stopu uspjeha i broj pokušaja te promatra kako se
kratki nizovi kolebaju, dok se raspodjela mnogih ponavljanja stabilizira.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu stvarnu vjerojatnost.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na A/B kampanju i postavite stvarnu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

**Statistika u divljini.**
**Mnogo prilika za slučajnost.** Analitička fleksibilnost omogućuje da se među
mnogim ishodima, podskupinama i trenucima zaustavljanja izdvoji rezultat koji
izgleda rijetko, iako je cijeli postupak takav nalaz učinio mnogo vjerojatnijim
(Simmons, 2011).

Čitanje jednog rezultata zato mora uključiti broj pokušaja i odluke donesene
nakon gledanja podataka. Vjerojatnost pripada postupku koji je rezultat
proizveo, a ne samo njegovoj posljednjoj tablici.

**Pitajte model.**
Asistent može simulirati postupak i usporediti analitički račun sa
učestalostima u ponavljanjima. Treba mu jasno opisati skup mogućih ishoda,
neovisnost i sve putove kojima je analiza mogla doći do rezultata. Modeli često
računaju pod prešutnom pretpostavkom neovisnosti.

> Simuliraj ovaj slučaj mnogo puta i prikaži raspodjelu ishoda. Prije računanja
> navedi koje pretpostavke koristiš o neovisnosti i jednakoj vjerojatnosti
> pokušaja.

**Nađite grešku.**
U nizu je više puta zaredom zabilježen isti ishod. Budući da se ravnoteža mora
vratiti, sljedeći pokušaj sada ima veću vjerojatnost suprotnog ishoda.
Pojedinačni pokušaji provedeni su pod jednakim uvjetima.

Greška je kockarska zabluda. Ako su pokušaji neovisni i uvjeti jednaki,
prethodni niz ne mijenja vjerojatnost sljedećeg ishoda.

## Razrađeni primjer

Simuliramo mnogo kampanja s jednakom stvarnom stopom odgovora. Svaka kampanja
daje nešto drukčiji udio, iako se temeljni proces ne mijenja. Histogram
prikazuje koliko je raspršena ta slučajna varijacija.

Raspodjela simuliranih stopa uspjeha. Izrada autora.

Jedna kampanja može završiti daleko od središta bez promjene stvarne stope.
Zaključak se zato ne temelji na tome izgleda li jedan rezultat neobično, nego
na usporedbi s raspodjelom koju bi cijeli postupak mogao proizvesti.

## Sažetak

Vjerojatnost opisuje neizvjesnost unutar jasno određenog skupa mogućnosti.
Pravila računanja vrijede samo uz sadržajne pretpostavke o događajima i
neovisnosti. Simulacija pokazuje kako stabilna raspodjela nastaje iz neurednih
pojedinačnih ishoda. Poglavlje o uzorkovanju tu će logiku primijeniti na
statistike koje se mijenjaju od uzorka do uzorka.

## Pojmovi

vjerojatnost (*probability*), događaj (*event*), neovisnost (*independence*),
binomna raspodjela (*binomial distribution*), normalna raspodjela (*normal
distribution*), QQ prikaz (*Q–Q plot*)

## Zadaci

### Konceptualni

Objasnite zašto niz jednakih ishoda ne mijenja vjerojatnost sljedećeg pokušaja
ako su pokušaji neovisni. Predajte jedan odlomak.

### Računski

Promijenite veličinu pokušaja u objektu `sim_kampanje` i predajte dva histograma
s kratkom usporedbom raspršenosti.

### Kritički

Objasnite kako više analitičkih putova mijenja čitanje rijetkog rezultata
(Simmons, 2011). Predajte dijagram mogućih odluka.

### Revizija modela

Ocijenite analizu modela iz okvira. Imenujte pretpostavku koju navodi, jednu
pogrešku i ispravnu vjerojatnostnu interpretaciju.

---

# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

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

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

U toj jednakosti $SE_{\bar{x}}$ označava standardnu pogrešku uzoračke sredine,
$\sigma$ standardnu devijaciju populacije, a $n$ veličinu uzorka. Za naš slučaj
formula daje `r hr_broj(s8$se_teorijska, 4)`, dok je simulacija dala
`r hr_broj(s8$se_empirijska, 4)`. Dvije brojke dolaze iz dva potpuno različita
smjera, jedna iz algebre i druga iz tri tisuće ponovljenih izvlačenja, a
poklapaju se na tri decimale.

U stvarnom istraživanju $\sigma$ nije poznata, pa se na njezino mjesto stavlja
uzoračka standardna devijacija $s$. Time formula postaje procjena, a ne
identitet. Tu zamjenu poglavlje o sažimanju podataka je pripremilo kada je
varijancu uvelo s djeliteljem umanjenim za jedan i tu odluku ostavilo kao
tvrdnju bez dokaza. Simulacija je sada može provjeriti. Izvučemo li četiri
tisuće uzoraka od po deset osoba i u svakome izračunamo prosjek kvadriranih
odstupanja s djeliteljem deset, prosječan rezultat iznosi
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
teorem** (*central limit theorem*) tvrdi da se distribucija uzorkovanja sredine
približava normalnoj raspodjeli kako uzorak raste, bez obzira na oblik
raspodjele iz koje se uzorkuje. Uobičajeno pravilo palca stavlja granicu oko
trideset opažanja, ali naša simulacija pokazuje i zašto je to pravilo grubo.
Kod izrazito asimetrične varijable trideset osoba nije bilo dovoljno da
asimetrija nestane, dok bi kod raspodjele koja je već gotovo simetrična i deset
osoba bilo dovoljno. Granica ovisi o tome koliko je izvorna raspodjela
iskrivljena, a ne o okruglom broju.

Praktična vrijednost teorema je u tome što oslobađa gotovo cijelo zaključivanje
od pretpostavke o obliku podataka. Postupci koji slijede ne traže da su
pojedinačna opažanja normalno raspodijeljena, nego da je normalna raspodjela
procjene, a to je nešto što uzorak proizvodi sam. Ta razlika objašnjava zašto se
isti alati primjenjuju na dohotke, brojanja i ocjene na ljestvici od jedan do
deset, iako nijedna od tih raspodjela nije zvonasta.

## Interakcija — CLT stroj

Simulacija koja je upravo prošla kroz četiri veličine uzorka fiksirala je oblik
populacije. Widget odvaja te dvije stvari, pa se oblik populacije, veličina
uzorka i broj ponavljanja mijenjaju neovisno. Time postaje vidljivo koje je
svojstvo posljedica čega, jer oblik raspodjele sredina ovisi o obojemu, a
njezina širina samo o veličini uzorka.

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

$$
SE_{\hat{p}} = \sqrt{\frac{\hat{p}\,(1 - \hat{p})}{n}}
$$

Polovica širine intervala oko procjene naziva se **margina pogreške** (*margin
of error*), i to je brojka koju medijski izvještaji navode uz anketu. Budući da
je raspršenost najveća pri udjelu od 50 %, uvrštavanjem te vrijednosti dobiva se
najgori slučaj, koji vrijedi bez obzira na to kakav će rezultat ispasti. Za
uobičajenu razinu od 95 % margina se tada svodi na približno jedan podijeljen
korijenom veličine uzorka.

*Slika. Najveća margina pogreške za udio pri razini od 95 % i uzorak potreban za zadanu marginu. Izrada autora.*

Tablica objašnjava zašto se veličine anketnih uzoraka tako uporno grupiraju
između pet stotina i dvije tisuće ispitanika. Ispod te granice margina postaje
prevelika da bi se o razlikama uopće govorilo, a iznad nje trošak raste brže od
koristi. Anketa na osamsto ljudi daje marginu od približno
`r paste0("±", hr_broj(100 * s8$moe(800), 1), " %")`, i ta je preciznost dovoljna
da se razaznaju razlike od desetak postotnih bodova, a nedovoljna za razlike od
dva ili tri.

Odatle slijedi pravilo čitanja koje vrijedi više od svega ostaloga u ovom
poglavlju. Kada izvještaj navodi da prva opcija ima 32 %, a druga 29 %, razlika
od tri postotna boda manja je od margine pogreške tipične ankete, pa podaci ne
podupiru tvrdnju da je prva opcija ispred druge. Uz to, margina se odnosi na
svaku procjenu zasebno, a razlika dvaju udjela ima vlastitu, još veću
nesigurnost.

U formuli za marginu pogreške nedostaje jedna veličina koju bi svatko očekivao
da je ondje, a to je veličina populacije. Preciznost ovisi o tome koliko smo
ljudi pitali i koliko su njihovi odgovori raspršeni, ne o tome koliko ih ima.
Provjeriti se to može izravno. Uzorak od osamsto osoba izvučen iz cijele naše
populacije daje standardnu pogrešku `r hr_broj(s8$se_velika, 4)`, a isti takav
uzorak izvučen iz njezina deset puta manjeg dijela daje
`r hr_broj(s8$se_mala, 4)`. Populacija veća za red veličine donijela je razliku
u preciznosti manju od desetine. Zbog toga anketa na tisuću ljudi jednako dobro
opisuje grad od pedeset tisuća stanovnika i državu od četiri milijuna, što je
vjerojatno najmanje intuitivan rezultat u cijelom poglavlju i redovito zvuči
kao pogreška onima koji ga prvi put čuju.

Preostaje reći što margina pogreške ne pokriva, jer se upravo o tome najčešće
šuti. Ona mjeri isključivo promjenjivost koja dolazi od slučajnog izvlačenja
ispitanika. Ne mjeri ljude koji nikada nisu bili u okviru iz kojega se
uzorkovalo, ne mjeri one koji su bili pozvani ali nisu odgovorili, i ne mjeri
učinak formulacije pitanja ni redoslijeda ponuđenih odgovora. Anketa uz koju
piše da je margina ±3 % nudi tri postotna boda opreza za jedan izvor pogreške i
nijedan za ostale tri. Rečenica da je nešto „unutar margine pogreške" zato je
tvrdnja o slučaju, a ne potvrda da je istraživanje dobro provedeno.

## Kad slučajnost nije bila slučajna

Sve dosad rečeno počiva na jednoj pretpostavci koju je lako previdjeti jer se
rijetko izgovara. Formula za standardnu pogrešku i središnji granični teorem
vrijede za **slučajni uzorak**, u kojem svaka jedinica populacije ima poznatu i
različitu od nule vjerojatnost da bude odabrana. Kada ta pretpostavka padne,
brojke se i dalje uredno izračunaju, ali više ne mjere ono što tvrde.

Prigodni uzorak najčešći je oblik takvog pada. Istraživač anketira one koji su
mu dostupni, obično studente vlastitog kolegija. U našoj populaciji skupina
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
statistiku koja se računa. Provjeravamo uzorkuje li s vraćanjem samo kada je to
namjera, jer je zadana postavka mnogih funkcija suprotna od potrebne. Najčešća
pogreška u odgovoru nije u kodu nego u rečenici koja ga prati, gdje se
raspršenost pojedinaca predstavi kao standardna pogreška procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno navedi standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

Greška je zamjena dviju razina varijabilnosti. Veći uzorak sužava raspodjelu
procjene, ali očekivana raspršenost pojedinaca ostaje jednaka populacijskoj, jer
je svojstvo ljudi, a ne postupka.

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
veličine uzorka, pa preciznost postaje sve skuplja. Njezin oblik se s porastom
uzorka približava normalnoj raspodjeli bez obzira na to iz čega se uzorkuje, i
upravo to čini ostatak knjige mogućim. Ništa od toga ne popravlja pristran
odabir, jer standardna pogreška mjeri samo ono što bi se mijenjalo kroz
ponavljanja istoga postupka, a ne ono što je taj postupak sustavno izostavio.
Poglavlje o procjeni uzet će tu raspodjelu i iz nje izgraditi raspon oko
vrijednosti koju ne možemo izravno vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), parametar (*parameter*),
statistika (*statistic*), pogreška uzorkovanja (*sampling error*), distribucija
uzorkovanja (*sampling distribution*), nepristranost (*unbiasedness*),
standardna pogreška (*standard error*), središnji granični teorem (*central
limit theorem*), uzorački udio (*sample proportion*), margina pogreške (*margin
of error*), slučajni uzorak (*random sample*), prigodni uzorak (*convenience
sample*), samoodabir (*self-selection*)

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

---

# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 21 min | Hvatač intervala | simulirana populacija | pogl. 8 |

**Vinjeta.**
Cumming je zagovarao izvještavanje procjena i intervala kao središte
statističkog zaključivanja, umjesto oslanjanja na samu odluku o značajnosti
(Cumming, 2014). Pomak mijenja pitanje koje postavljamo podacima. Umjesto
binarnog prolaza pitamo koliki je učinak i koliko je procjena precizna.

Poglavlje o uzorkovanju pokazalo je zašto takvo pitanje uopće ima smisla. Naša
procjena samo je jedan ishod iz raspodjele mogućih ishoda, a širina te
raspodjele poznata je u simulaciji jer smo uzorkovanje ponovili tri tisuće puta.

Istraživač koji objavljuje rezultat nema tri tisuće uzoraka. Ima jedan, i iz
njega mora reći koliko je siguran.

Kako iz jednoga opaženog uzorka pošteno govoriti o vrijednosti koja ostaje
nepoznata?

## Od točke prema rasponu

Uzorak od `r hr_broj(s9$n, 0)` osoba iz naše populacije daje prosječno
povjerenje u medije od `r hr_broj(s9$sredina, 2)`. Ta jedna vrijednost naziva se
**točkasta procjena** (*point estimate*) i najbolji je sažeti pogodak koji
trenutačno imamo. Njezina je slabost u tome što ne nosi nikakav trag vlastite
nesigurnosti. Ista brojka mogla je nastati iz uzorka od dvadeset ljudi i iz
uzorka od dvadeset tisuća, a te dvije situacije ne zaslužuju jednako povjerenje.

Sve što nedostaje već je izračunato u prethodnom poglavlju. Standardna pogreška
mjeri koliko bi procjena tipično varirala kroz ponovljena uzorkovanja, a za naš
uzorak iznosi `r hr_broj(s9$se, 3)`. Uz nju procjena prestaje biti gola brojka i
postaje brojka s poznatom skalom vlastitog kolebanja.

Središnji granični teorem kazuje i kakav oblik to kolebanje ima. Raspodjela
uzoračkih sredina približno je normalna, a za normalnu raspodjelu znamo koliki
udio vrijednosti pada unutar zadanog broja standardnih devijacija od središta,
što je pravilo koje je poglavlje o vjerojatnosti već postavilo. Približno 95 %
vrijednosti leži unutar 1,96 standardnih devijacija.

Odatle slijedi konstrukcija koja se čini gotovo previše jednostavnom da bi
radila. Ako je naša sredina u 95 % slučajeva unutar 1,96 standardnih pogrešaka
od populacijske vrijednosti, tada je i populacijska vrijednost u 95 % slučajeva
unutar te iste udaljenosti od naše sredine. Razmak oko procjene dug 1,96
standardnih pogrešaka na svaku stranu zato će hvatati cilj u 95 % ponavljanja.

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

Slovo $z^{*}$ označava koliko standardnih pogrešaka širimo na svaku stranu, i
bira ga željena razina, pa je za 95 % ono jednako 1,96. Za naš uzorak taj račun
daje raspon od `r hr_broj(s9$donja, 2)` do `r hr_broj(s9$gornja, 2)`, a prava
populacijska vrijednost iznosi `r hr_broj(s9$mu, 2)` i nalazi se unutra.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Vrijedi obratiti pozornost na to gdje u toj definiciji stoji obećanje. Ono ne
stoji uz raspon nego uz postupak, i upravo se ta razlika u praksi najčešće gubi.

## Što razina pouzdanosti obećava

Provjera je moguća jer populaciju poznajemo. Ponovimo cijeli postupak deset
tisuća puta, svaki put izvučemo novi uzorak od dvjesto osoba, izračunamo
njegovu sredinu i standardnu pogrešku, sastavimo interval i prebrojimo koliko
ih je obuhvatilo pravu vrijednost. Cilj je obuhvaćen u
`r paste0(hr_broj(s9$pokrivenost, 1), " %")` slučajeva, a promašen u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja.

Postupak dakle radi približno onako kako obećava, i vrijedi zadržati riječ
približno. Zamjena nepoznate populacijske raspršenosti onom izmjerenom u uzorku
unosi vlastitu nesigurnost, koja je pri dvjesto osoba mala, a pri dvadeset osoba
ne bi bila. Ispravak koji to nadoknađuje širi interval za mali uzorak i knjiga
ga uvodi u poglavlju o usporedbi dviju grupa, gdje ga postupak prvi put stvarno
treba.

Ono što se u brojci od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne vidi jest
sudbina pojedinačnog intervala. Svaki od tih dvije tisuće raspona ili sadrži
pravu vrijednost ili je ne sadrži, i nakon što je izračunat, u njemu nema
ničega slučajnog. Slučajan je bio uzorak koji ga je proizveo. Populacijska
sredina fiksan je broj i ne kreće se, pa rečenica o vjerojatnosti da se ona
nalazi unutar zadanih granica opisuje nešto što nema promjenjivosti koju bi ta
vjerojatnost mjerila.

Analogija koja to drži na okupu jest bacanje obruča na fiksni kolac. Obruč je
interval, kolac je parametar, a razina pouzdanosti opisuje koliko često obruč
pada oko kolca kroz mnogo bacanja. Nakon jednoga bacanja obruč je pao ili nije,
a mi ga gledamo zatvorenih očiju. Postotak opisuje ruku koja baca, ne ovaj
pojedini obruč.

Zbog te razlike korisno je znati što čitatelj objavljenog intervala smije reći.
Smije reći da su vrijednosti unutar granica uskladive s podacima, a one izvan
njih slabo uskladive, i to pod pretpostavkama koje je postupak koristio. Smije
reći da je istraživanje bilo dovoljno precizno da razluči razlike veće od
širine raspona, i da za manje razlike nije. Ne smije reći koliko je vjerojatno
da parametar leži unutra, niti da će se ponovljeno istraživanje smjestiti
unutar tih istih granica, jer bi drugo istraživanje imalo vlastiti uzorak i
vlastiti interval. Prve dvije rečenice pokrivaju gotovo sve što se u praksi
treba zaključiti, i obje govore o rasponu vrijednosti, a nijedna o
vjerojatnosti.

## Interakcija — Hvatač intervala

Prebrojavanje iz prethodnog odjeljka dalo je jednu brojku i sakrilo postupak koji
je do nje doveo. Widget taj postupak vraća na vidjelo, jer prikazuje same
intervale, jedan ispod drugoga, oko iste nepomične ciljne crte. Veličina uzorka i
razina pouzdanosti mijenjaju se odvojeno, pa se vidi da prva mijenja širinu
intervala, a druga mijenja i širinu i učestalost promašaja.

*Slika. Intervali iz ponovljenih simuliranih uzoraka oko fiksne populacijske sredine. Istaknuti intervali promašuju okomitu ciljnu crtu.*

**Što isprobati.**

1. Zadržite pedeset intervala i prebrojite one koji ne sijeku okomitu ciljnu crtu.
2. Povećajte broj intervala na sto bez promjene veličine uzorka ili razine pouzdanosti.
3. Usporedite širinu intervala pri uzorcima veličine dvadeset i sto.
4. Promijenite razinu pouzdanosti s devedeset na devedeset i devet posto te opišite odnos širine i obuhvata.

## Preciznost nasuprot pouzdanosti

Dva pomaka koja widget dopušta imaju vrlo različite učinke i lako ih je pobrkati
jer oba mijenjaju širinu. Veći uzorak sužava interval time što smanjuje
standardnu pogrešku, pa uz jednako obećanje o obuhvatu dobivamo precizniji
odgovor. Prosječna širina intervala pri uzorku od pedeset osoba iznosi
`r hr_broj(s9$sirine[["50"]], 2)` boda, pri dvjesto
`r hr_broj(s9$sirine[["200"]], 2)`, a pri osamsto
`r hr_broj(s9$sirine[["800"]], 2)`.

Viša razina pouzdanosti također širi interval, ali ništa ne dobiva na
preciznosti. Na istom našem uzorku raspon od 90 % širok je
`r hr_broj(s9$razine[["90"]], 2)` boda, onaj od 95 %
`r hr_broj(s9$razine[["95"]], 2)`, a onaj od 99 %
`r hr_broj(s9$razine[["99"]], 2)`. Podaci se nisu promijenili, promijenio se
zahtjev. Interval koji obuhvaća cilj u 100 % slučajeva postoji i proteže se od
minus do plus beskonačno, čime savršena pouzdanost postaje savršeno beskorisna.

**Preciznost** je zato svojstvo koje se plaća podacima, a **pouzdanost** je
svojstvo koje se bira i plaća širinom. Konvencija od 95 % nema dublje
opravdanje od uobičajenosti, i to je razlog više da se uz svaki interval navede
razina na kojoj je izračunat.

Širok interval ne znači loše obavljen posao. Češće znači mali uzorak ili
podatke koji su stvarno raspršeni, i tada je široki raspon iskren opis stanja, a
ne priznanje nesposobnosti. Suprotan je slučaj mnogo opasniji. Uzak interval
oko procjene iz pristranog uzorka izgleda kao preciznost, a jest sigurnost u
pogrešnu vrijednost, jer interval mjeri samo ono što bi se mijenjalo kroz
ponavljanja istoga postupka.

Iz širine slijedi i način na koji se intervali čitaju kada ih je više na istoj
slici, što je najčešći oblik u kojem ih društveni znanstvenik susreće. Grafovi
koji uz svaku skupinu crtaju raspon umjesto samog stupca odmah pokazuju koje su
procjene oslonjene na malo ljudi, a koje na mnogo, i time govore više od
tablice prosjeka. Iskušenje je da se iz njih očita i zaključak o razlici.

Pravilo koje se pritom obično primjenjuje nije simetrično i vrijedi to znati.
Kada se dva intervala uopće ne preklapaju, razlika među skupinama gotovo je
sigurno stvarna. Kada se preklapaju, iz toga ne slijedi da razlike nema, jer
umjereno preklapanje i dalje je uskladivo s pravom razlikom. Preklapanje je
zato slab dokaz u jednom smjeru i jak u drugom, a pošten odgovor traži interval
za samu razliku, a ne dva intervala jedan pokraj drugoga. Taj postupak knjiga
uvodi u poglavlju o usporedbi dviju grupa.

Postoji i druga zamjena koja se često javlja u istom odlomku. Interval
pouzdanosti govori gdje je prosjek, a ne gdje su ljudi. Za naš uzorak od
dvjesto osoba raspon oko sredine dug je
`r hr_broj(s9$gornja - s9$donja, 2)` boda, dok bi raspon unutar kojega leži
otprilike 95 % pojedinačnih ocjena bio širok približno
`r hr_broj(2 * s9$predikcijski, 1)` boda. Prvi se odnosi na parametar i sužava
se s uzorkom, drugi na buduće opažanje i ne sužava se gotovo nimalo.

*Slika. Interval pouzdanosti za sredinu i raspon unutar kojega leži otprilike 95 % pojedinačnih ocjena, na istom uzorku i istoj osi.*

## Bootstrap kao vlastiti izum

Sve dosad počiva na jednoj formuli za standardnu pogrešku, a ta formula postoji
samo za neke mjere. Za sredinu je poznata, za udio također, a za medijan,
razliku percentila ili omjer dviju mjera nije jednostavna ili je uopće nema.
Pitanje što učiniti kada formule nema ima odgovor koji se može smisliti bez
ijedne nove ideje, uz uvjet da se prethodno poglavlje shvatilo ozbiljno.

Standardna pogreška bila je definirana kroz ponovljene uzorke iz populacije.
Kad bismo populaciji imali pristup, izvukli bismo tisuću uzoraka, izračunali
tisuću medijana i pogledali koliko se razilaze. Populaciji pristupa nemamo,
imamo samo uzorak. Uzorak je pritom najbolja slika populacije kojom
raspolažemo, jer je iz nje izvučen slučajno i njezine razmjere nosi u sebi. Ako
mu dopustimo da privremeno glumi populaciju i iz njega izvlačimo nove uzorke
jednake veličine, dobit ćemo raspodjelu koja oponaša onu koju bismo dobili iz
prave populacije.

Izvlačenje mora biti s vraćanjem, i to nije tehnički detalj. Izvlačenjem bez
vraćanja iz uzorka od šezdeset osoba dobili bismo šezdeset istih osoba u drugom
poretku, pa bi svaki takav uzorak dao identičan medijan i raspodjela ne bi
imala nikakvu širinu. Vraćanjem opažanja u posudu dopuštamo da neka uđu
dvaput, a neka nijednom, i upravo ta promjena sastava oponaša promjenu sastava
koja nastaje pri izvlačenju iz populacije. Postupak nosi ime **bootstrap** i
uveden je kao način procjene nesigurnosti kada teorijski račun nije pri ruci
(Efron, 1979).

Uzmimo uzorak od `r hr_broj(s9$mali_n, 0)` osoba i pitajmo se koliko iznosi
medijan dnevnih minuta praćenja medija. U uzorku on iznosi
`r hr_broj(s9$medijan_uzorak, 1)` minuta. Četiri tisuće bootstrap uzoraka daju
raspon od `r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta,
unutar kojega leži prava populacijska vrijednost od
`r hr_broj(s9$medijan_pop, 1)` minuta.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću.*

Histogram ima vidljiv stubast oblik jer medijan uzorka od šezdeset brojeva može
poprimiti samo ograničen skup vrijednosti, što je svojstvo mjere, a ne mana
postupka. Snaga bootstrapa upravo je u tome što ga takve neugodnosti ne
zaustavljaju. Isti se postupak bez izmjene primjenjuje na sredinu, medijan,
korelaciju ili razliku dviju skupina, jer nigdje ne pretpostavlja oblik
raspodjele.

Njegova granica ostaje početni uzorak, i granica je stroga. Bootstrap ponovno
koristi opažanja koja već imamo, pa ne može otkriti dio populacije koji u
uzorak nikada nije mogao ući. Ako je uzorak prigodan, postupak će pouzdano
opisati promjenjivost pogrešne procjene. Ako je premalen da zabilježi rijetke
ali važne slučajeve, ta praznina ostaje u svakom od četiri tisuće ponavljanja.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživači su studentima i aktivnim
znanstvenicima predočili objavljeni interval pouzdanosti i uz njega šest
tvrdnji o njegovu značenju, među kojima nijedna nije bila točna (Hoekstra, 2014).
Velik dio ispitanika u svim skupinama, uključujući iskusne istraživače,
prihvatio je barem neke od njih.

Tvrdnje nisu bile besmislene, i u tome je poanta okvira. Sve su govorile o
vjerojatnosti da se prava vrijednost nalazi unutar granica, ili o tome koliko
je vjerojatno da bi se ponovljeno istraživanje unutar njih smjestilo. Postupak
koji smo izgradili takva obećanja ne daje, jer se njegov postotak odnosi na
udio intervala koje bi ponovljeno uzorkovanje proizvelo. Nalaz ne pokazuje da
su intervali loš alat nego da je rečenica kojom ih opisujemo teža od računa
koji ih proizvodi.

**Pitajte model.**
Asistent može bootstrapirati gotovo svaku statistiku i obično to učini
ispravno. Provjeravamo tri stvari koje redovito promakne. Uzorkuje li s
vraćanjem i na punoj veličini uzorka, jer bez toga raspodjela nema smisla. Čuva
li strukturu podataka, jer se kod uparenih ili grupiranih opažanja izvlače
jedinice, a ne redovi. Ponavlja li dovoljno puta, jer nekoliko stotina
ponavljanja daje granice koje se mijenjaju od pokretanja do pokretanja.
Najčešća pogreška ipak nije u kodu nego u zaključnoj rečenici, gdje se već
izračunatom intervalu pripiše vjerojatnost.

> Izračunaj točkastu procjenu i bootstrap interval. Uzorkuj s vraćanjem na
> punoj veličini uzorka, sačuvaj strukturu podataka i interpretiraj razinu
> pouzdanosti kao svojstvo ponovljenog postupka.

**Nađite grešku.**
Bootstrap raspodjela je približno simetrična i interval je uredno izračunat iz
njezinih krajeva. Postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

Greška je pripisivanje vjerojatnosti fiksnom parametru nakon izračuna
frekventističkog intervala. Prva rečenica je točna i postupak je proveden
ispravno. Razina pouzdanosti opisuje udio intervala koji obuhvaćaju parametar
kroz ponovljeno uzorkovanje, a ne položaj parametra u odnosu na ovaj raspon.

## Razrađeni primjer

Pitanje je ono koje bi postavio naručitelj istraživanja. Koliko vremena dnevno
stanovnici našega grada provode uz medije, i koliko je taj odgovor pouzdan ako
je anketirano šezdeset ljudi.

Prvi izbor nije statistički nego opisni. Dnevne minute imaju rep prema velikim
vrijednostima, a poglavlje o sažimanju podataka pokazalo je da prosjek takav
rep povlači za sobom, dok medijan ostaje kod tipičnog ispitanika. Za pitanje o
tome koliko medija prati uobičajena osoba medijan je pošteniji odgovor. Cijena
tog izbora vidi se tek sada, jer za sredinu postoji formula za standardnu
pogrešku, a za medijan ne postoji nijedna koja bi se dala napisati u jednom
retku. Upravo zato ovaj primjer i postoji.

Cijeli bootstrap stane u istu petlju koju je poglavlje o uzorkovanju već
pokazalo, uz jednu izmjenu. Umjesto iz populacije, izvlačimo iz uzorka, i to s
vraćanjem.

Poziv `sample` uz argument `replace` izvlači s vraćanjem i jedini je novi
element u odnosu na prethodno poglavlje, dok `quantile` odsijeca zadani udio
raspodjele s obje strane. Blok proizvodi upravo one tri brojke koje je odjeljak
o bootstrapu već naveo, jer je riječ o istoj analizi ispisanoj u cijelosti.

Odgovor naručitelju glasi da tipičan stanovnik prati medije oko
`r hr_broj(s9$medijan_uzorak, 1)` minuta dnevno, uz raspon od
`r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta koji
opisuje koliko bi se ta procjena mijenjala kroz ponovljena istraživanja iste
veličine. Raspon je širok gotovo `r hr_broj(s9$boot_gornja - s9$boot_donja, 0)`
minuta, što je pošten opis onoga što šezdeset ljudi može reći, i ujedno
najkorisnija brojka u cijelom izvještaju. Naručitelj koji je htio razlučiti
promjenu od deset minuta iz ovih podataka odgovor neće dobiti bez većeg uzorka.

Budući da populaciju poznajemo, možemo napraviti i ono što stvarno istraživanje
ne može. Prava vrijednost iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i nalazi
se unutar granica. Iz toga ne slijedi da postupak radi, jer bi i loš postupak
pogodio pokoji put. Ono što o postupku govori jest prebrojavanje deset tisuća
ponavljanja iz ranijeg odjeljka, a ovaj pojedinačni pogodak samo je jedan od
njih, viđen iznutra kako ga vidi istraživač.

Redoslijed kojim su tri brojke ispisane isti je onaj kojim se rezultat i
izvještava. Najprije dolazi procjena, jer je ona odgovor na postavljeno pitanje.
Zatim dolazi raspon, jer bez njega procjena tvrdi više nego što zna. Tek na
kraju dolazi ograda, koja ovdje kaže da su podaci simulirani, da je mjera
medijan, a ne prosjek, i da šezdeset ljudi nije mnogo. Ista tri koraka vrijede
za nalaz čija je populacija stvarna, s tom razlikom da se ondje srednji korak
mora izvesti bez ikakve mogućnosti provjere, i upravo zato mora biti izveden
pažljivo.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval pouzdanosti
uzima standardnu pogrešku i oblik koji je dao središnji granični teorem te oko
procjene gradi raspon čije obećanje pripada postupku, a ne pojedinačnom rasponu
koji imamo pred sobom. Preciznost se kupuje podacima, a pouzdanost se bira i
plaća širinom, pa uz svaki raspon mora stajati razina na kojoj je izračunat.
Bootstrap istu ideju oslobađa formule tako što uzorku dopušta da privremeno
glumi populaciju, i time otvara mjere za koje račun ne postoji, ne popravljajući
pritom nijednu slabost samoga uzorka. Sljedeće poglavlje uzima isti aparat i
mijenja mu pitanje, jer umjesto raspona usklađenog s podacima traži koliko su
podaci neobični pod jednom određenom pretpostavkom.

## Pojmovi

točkasta procjena (*point estimate*), interval pouzdanosti (*confidence
interval*), razina pouzdanosti (*confidence level*), preciznost (*precision*),
bootstrap (*bootstrap*), uzorkovanje s vraćanjem (*sampling with replacement*),
parametar (*parameter*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, i zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica. Predajte jedan odlomak.

### Računski

Upotrijebite widget Hvatač intervala. Postavite pedeset intervala pri uzorku od
četrdeset osoba i razini od 95 % pa zabilježite koliko ih promašuje cilj.
Ponovite mjerenje pri razini od 99 % i pri uzorku od sto šezdeset osoba,
mijenjajući svaki put samo jednu postavku. Predajte tablicu s tri retka u kojoj
su navedeni postavka, širina tipičnog intervala i broj promašaja te jednu
rečenicu o tome koja postavka mijenja preciznost, a koja učestalost promašaja.

### Kritički

Pronađite u medijskom izvještaju ili sažetku rada rečenicu koja tumači interval
pouzdanosti. Prosudite pripisuje li vjerojatnost parametru, brka li raspon
sredine s rasponom pojedinačnih opažanja ili je ispravna, i napišite verziju
koja je vjerna postupku bez gubitka informacije (Hoekstra, 2014). Predajte
izvornu rečenicu, prosudbu i ispravak.

### Revizija modela

Ocijenite modelsku interpretaciju iz okvira o pogrešci. Imenujte što je u njoj
točno, izdvojite jednu pogrešnu rečenicu i napišite frekventistički ispravnu
zamjenu koja zadržava razinu od 95 % i ne uvodi nove tvrdnje o podacima.
