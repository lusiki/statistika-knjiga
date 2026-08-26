# Vjerojatnost koliko treba

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Simulator novčića i kampanje | simulirana populacija | pogl. 3 i 4 |

**Vinjeta.**
Gilovich, Vallone i Tversky ispitali su vjerovanje igrača i navijača da
košarkaš nakon nekoliko pogodaka postaje „vruć” i da mu sljedeći pokušaj ima
veće izglede nego inače (Gilovich, 1985). Analiza zapisa utakmica i kontrolirani
pokus naveli su ih na zaključak da je riječ o krivom čitanju slučajnih nizova
(Gilovich, 1985).

Njihov nalaz nije samo osporio jedan sportski dojam. Tvrdio je da slučajnost
sama proizvodi niz koji izgleda kao obrazac, pa oko njega nema što objašnjavati
(Gilovich, 1985). Kasnija ponovna analiza pokazala je da ni postupak mjerenja tog
obrasca nije bio neutralan (Miller, 2018).

Kako razlikovati obrazac od onoga što slučajnost proizvodi bez ijednog razloga?

## Što vjerojatnost opisuje

Pošten novčić bacimo mnogo puta i nakon svakog bacanja zabilježimo dotadašnji
udio glava. Jedan niz može nakratko izgledati izrazito neuravnoteženo, pa isti
postupak simuliramo triput. Prikaz otkriva što se događa s relativnom
učestalošću dok broj bacanja raste.

*Slika. Kumulativni udio glava u trima neovisnim nizovima bacanja poštenog novčića. Vodoravna crta označuje vrijednost pola.*

Nakon dvadeset bacanja tri se niza razilaze od
`r hr_broj(s7_rani$najmanji, 2)` do `r hr_broj(s7_rani$najveci, 2)`, dovoljno
da bi promatrač mogao zaključiti kako novčić nije pošten. Nakon dvije
tisuće bacanja svi leže između `r hr_broj(s7_kasni$najmanji, 3)` i
`r hr_broj(s7_kasni$najveci, 3)`. Ponavljani proces proizvodi raspodjelu mogućih
nizova. Pojedini se nizovi razlikuju, ali njihova se relativna učestalost glava
sve manje udaljava od polovice.

**Vjerojatnost** je broj od nule do jedinice koji događaju pridružuje
razinu neizvjesnosti unutar jasno opisanoga modela, pri čemu veći broj označuje
veće izglede za taj događaj.

Model može opisivati postupak koji se ponavlja ili jedinstven događaj. U prvom
se slučaju njegova vjerojatnost može usporediti s relativnom učestalošću kroz
mnogo ponavljanja, kao na prikazu. U drugome broj sažima neizvjesnost pod
navedenim informacijama, primjerice izglede reprezentacije na sljedećem
prvenstvu. U oba slučaja treba imenovati model i informacije iz kojih broj
dolazi.

Pravilnost vidljiva na simuliranom prikazu zove se zakon velikih brojeva. Za
neovisna ponavljanja sa stabilnom vjerojatnošću relativna se učestalost s brojem
ponavljanja primiče toj vjerojatnosti.

Ono što zakon ne kaže važnije je od onoga što kaže. Nijedno pojedinačno bacanje
ne zna što se prije dogodilo i ništa ne nadoknađuje. Udio se ne primiče polovici
zato što se višak glava kompenzira viškom pisama, nego zato što svaki novi
rezultat ulazi u sve veći nazivnik i time sve manje pomiče omjer. Rani su ishodi
i dalje u brojniku, samo svaki od njih u dvije tisuće bacanja ima premalen
utjecaj da bi se početna neravnoteža jasno vidjela.

Očekivanje da pošten novčić nakon četiri glave „duguje” pismo zove se kockarska
zabluda. U fiksnom modelu neovisnih bacanja pogrešan je i obrnuti zaključak da
niz glava povećava vjerojatnost još jedne glave. Vjerovanje u vruću ruku ipak
postavlja drukčije pitanje. Možda se mijenja sam proces zbog igračeve forme,
težine šuta, obrane ili odabira pokušaja. Fiksna i neovisna vjerojatnost zato je
nulti model za usporedbu, a ne unaprijed zajamčen opis košarke. Analiza mora
razlikovati promjenjivi proces od širokoga raspona koji već proizvodi
slučajnost.

Isti broj može u tvrdnji imati tri različite uloge. Modelna vjerojatnost slijedi
iz izričitih pretpostavki i dostupnih informacija. Relativna učestalost u
ponovljenim pokušajima jest dokaz kojim se takav model može provjeravati.
Osobna sigurnost samo opisuje koliko je netko uvjeren i ne postaje modelna
vjerojatnost time što je izražena brojem.

**Kalibrirana nesigurnost** povezuje te uloge bez njihova stapanja. Procjena za
jedinstven događaj mora navesti informacije na kojima počiva, a njezina se
kalibracija prosuđuje kroz mnogo usporedivih prognoza. Među prognozama kojima je
dodijeljeno sedamdeset posto događaj bi se trebao ostvariti približno u
sedamdeset posto slučajeva. Jedan se ishod može ostvariti ili izostati, ali sam
ne može pokazati je li osoba ili model dobro kalibriran.

## Tri pravila i jedna pretpostavka

Vjerojatnost da se događaj ne dogodi jednaka je jedinici umanjenoj za
vjerojatnost da se dogodi, što je često najbrži put do odgovora. Vjerojatnosti
dvaju ishoda koji se ne mogu dogoditi istovremeno zbrajaju se, a ako se mogu
preklopiti, od zbroja treba oduzeti preklop kako ne bi bio brojen dvaput. Za
vjerojatnost da se dva događaja dogode zajedno opće pravilo množi vjerojatnost
prvoga s uvjetnom vjerojatnošću drugoga. Samo se uz neovisnost smije rabiti
prečac koji množi njihove dvije rubne vjerojatnosti.

Preklop iz drugog pravila lako se previdi, a razlika koju čini vidljiva je na
podacima. U simuliranoj populaciji `populacija_medija` (Šikić, 2026) portal bira
`r hr_broj(s7$p_portal)` % ljudi, a osobe do dvadeset devete godine čine
`r hr_broj(s7$p_mlad)` % populacije. Zbroj ta dva udjela iznosi
`r hr_broj(s7$p_zbroj)` %, dok je stvarni udio onih koji su mladi ili biraju portal
`r hr_broj(s7$p_portal_ili_mlad)` %. Razlika je točno onih
`r hr_broj(s7$p_portal_i_mlad)` % koji su oboje i koje je zbrajanje izbrojilo
dvaput.

Prečac u trećem pravilu jedini od navedenih zahtijeva sadržajnu pretpostavku.

**Neovisnost** dvaju događaja znači da saznanje o tome je li se jedan dogodio
ne mijenja vjerojatnost drugoga.

Poglavlje radi na simuliranoj populaciji od pedeset tisuća odraslih osoba, istoj
koju koriste poglavlja o uzorkovanju i procjeni, i ta je populacija u cijelosti
poznata. U njoj društvene mreže kao primarni izvor vijesti bira
`r hr_broj(s7$p_mreze)` % ljudi, a osobe do dvadeset devete godine čine
`r hr_broj(s7$p_mlad)` % populacije. Kad bi te dvije okolnosti bile neovisne,
pravilo množenja dalo bi `r hr_broj(s7$p_umnozak)` % ljudi koji su i mladi i biraju
mreže. Stvarni udio iznosi `r hr_broj(s7$p_oboje)` %, dakle znatno više od
umnoška.

Račun je ispravan, a pogrešna je pretpostavka koju je koristio. Neovisnost se
opravdava opisom procesa i dizajnom, a ne bira zato što pojednostavnjuje
množenje. Podaci mogu otkriti njezino kršenje, ali izostanak vidljive razlike ne
može je sam potvrditi. U ovoj potpuno poznatoj simuliranoj populaciji izravno
vidimo da ne vrijedi, pa nam treba pojam koji razlikuje ukupnu vjerojatnost od
vjerojatnosti unutar neke skupine.

**Uvjetna vjerojatnost** je vjerojatnost događaja izračunata unutar skupine u
kojoj je neki drugi događaj već nastupio.

Među osobama do dvadeset devete godine društvene mreže bira
`r hr_broj(s7$p_mreze_mlad)` %, a među starijima `r hr_broj(s7$p_mreze_ostali)` %.
Televizija ide obrnuto, s `r hr_broj(s7$p_tv)` % u cijeloj populaciji i
`r hr_broj(s7$p_tv_stariji)` % među osobama od šezdeset godina naviše. Razlika
između ukupne i uvjetne vrijednosti pokazuje da su događaji ovisni; kad
ovisnosti nema, dva se broja poklapaju.

Smjer uvjeta ne smije se preokrenuti. Poglavlje o tome kako brojke zavode
pokazalo je da udio upozorenja među ciljanim zapisima nije udio ciljanih zapisa
među svim upozorenjima. Prvi
se broj računa među ciljanim zapisima, a drugi među upozorenjima. Za drugi su
potrebne i temeljna stopa i stopa pogrešnih upozorenja, jer dva smjera imaju
različite nazivnike.

U izvještaju se isto pitanje može pojaviti bez naziva uvjetne vjerojatnosti.
Udio konverzija među posjetiteljima koji su kliknuli na oglas i udio
otvaranja među poslanim porukama uvjetne su vjerojatnosti i svaka od njih
vrijedi samo za skupinu u čijem je nazivniku. Analiza po segmentima nije ništa
drugo nego niz uvjetnih vjerojatnosti, pa se čita s istim oprezom prema
nazivniku koji je poglavlje o kategoričkim podacima kasnije stavlja u središte.

## Ponovljeni pokušaji s dva ishoda

Mnoga pitanja u društvenim istraživanjima imaju isti oblik. Fiksan je broj
pokušaja, svaki završava na jedan od dva načina, i zanima nas koliko ih je
završilo na prvi. Glasanje, klik, odgovor na poziv i otvaranje poruke stanu u
taj kalup.

**Binomna raspodjela** opisuje broj uspjeha u zadanom broju pokušaja kad svaki
pokušaj ima samo dva ishoda, jednaku vjerojatnost uspjeha i nikakvu vezu s
ostalim pokušajima.

U konstruiranom modelu pretpostavimo dvadeset objava i vjerojatnost od dva posto
da pojedina u sedam dana dosegne unaprijed zadan prag dijeljenja. Prag, razdoblje
i broj izloženih korisnika dio su hipotetske definicije viralnosti; njihova bi
promjena promijenila i model. Zadana je vjerojatnost ulaz modela, a ne izmjeren
udio. Binomna raspodjela tada kaže da nijedna neće biti viralna u
`r hr_broj(s7$nijedna)` % zamišljenih mjeseci. To nije prognoza za jedan mjesec
nego opis onoga što ponavljanja zadanoga modela proizvode.

Svaki uvjet iz definicije treba zasebno opravdati. Vjerojatnost uspjeha nije
jednaka kroz pokušaje ako se objave razlikuju po dosegu, a neovisnost ne vrijedi
ako jedno dijeljenje poveća vidljivost sljedeće objave. Viralnost može nastati
upravo takvim procesom, pa se binomni model ne smije primijeniti bez provjere.
Ni dvije osobe iz istoga kućanstva nisu neovisne samo zato što zauzimaju dva
retka ankete.

Kad su uvjeti ispunjeni, raspodjela daje dvije korisne stvari odjednom. Očekivani
broj
uspjeha jednak je umnošku broja pokušaja i vjerojatnosti uspjeha, pa se lako
pamti i lako provjerava. Raspršenost oko tog broja raste sporije od samog broja
pokušaja, što znači da udio uspjeha postaje sve stabilniji što je kampanja veća,
premda apsolutni broj uspjeha varira sve više. Izvještaj mora držati ta dva
smjera odvojeno, jer veći apsolutni raspon ne znači da je udio nestabilniji nego
prije.

Model zato nije opis svijeta nego kontrolirana slika jednog dijela procesa. Ono
što ga čini korisnim jest da se u njemu točno zna što proizvodi slučajnost, pa
opaženi rezultat ima s čime biti uspoređen.

## Interakcija — Simulator novčića i kampanje

Sljedeći prikaz drži zadanu vjerojatnost modela nepromijenjenom i mijenja samo
duljinu niza. Vidljivo postaje ono zbog čega se kratki nizovi mogu pogrešno
pročitati, jer raspon njihovih ishoda ostaje širok i onda kad se generator
uopće ne mijenja.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu vjerojatnost modela.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na kampanju i postavite zadanu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

Neobičnost jedne kampanje prosuđuje se prema cijeloj raspodjeli ishoda koje isti
postupak proizvodi. Ishod u širokoj raspodjeli slabije razlikuje konkurentska
objašnjenja, dok položaj duboko u repu može osporiti zadani model, ali sam ne
otkriva uzrok odstupanja.

Prije nastavka zastajemo radi dohvata. Bez vraćanja na tekst odgovorimo što na
standardiziranoj ljestvici znače nula, jedan i minus jedan. Povežimo zatim
duljinu niza iz widgeta sa širinom raspodjele njegovih stopa, bez promjene zadane
vjerojatnosti modela. Ako te dvije veze nisu jasne, vraćamo se samo na odjeljak o
standardizaciji u poglavlju o sažimanju podataka i prva dva koraka widgeta.

## Zvonasta krivulja i njezino područje

Raspodjela mnogih ponavljanja iz widgeta ima prepoznatljiv oblik. Simetrična je i
najgušća u sredini, a gustoća joj brzo opada prema obama krajevima. Taj oblik u
statistici ima posebno mjesto, i ne zato što ga priroda posebno voli.

**Normalna raspodjela** je simetrična zvonasta raspodjela koju u cijelosti
određuju njezino središte i njezina standardna devijacija.

Standardizirana vrijednost iz poglavlja o sažimanju podataka sada postaje položaj
na toj krivulji.
Nula označuje središte, pozitivna vrijednost položaj iznad sredine, a negativna
položaj ispod nje. Njezin apsolutni iznos govori koliko je standardnih
devijacija vrijednost udaljena od sredine. Novi je korak tek povezati taj
položaj s područjem normalne krivulje.

Svaka stopa u widgetu prosjek je nula i jedinica iz jednoga niza. Neuspjeh nosi
nulu, a uspjeh jedinicu. Histogram zato ne prikazuje raspodjelu pojedinačnih
ishoda, nego raspodjelu prosjeka ili stopa dobivenih iz mnogih ponovljenih
nizova. Ta je razlika ključna za sljedeći rezultat.

Normalna raspodjela povlaštena je zbog središnjega graničnog teorema. U njegovu
osnovnom obliku opažanja dolaze iz iste raspodjele koja se ne mijenja od
opažanja do opažanja, međusobno su neovisna, a ta raspodjela ima konačnu
varijancu. Kako njihov broj raste, raspodjela prosjeka približava se normalnoj
raspodjeli iako sama opažanja ne moraju biti normalna. Druge inačice teorema
dopuštaju primjereno slabu ovisnost, ali ne proizvoljnu povezanost, a teorem ne
pokriva ni raspodjele s beskonačnom varijancom.

Widget pokazuje uži slučaj. Tri pitanja prevode uvjete teorema na njegov model.
Dolaze li svi pokušaji iz istoga stabilnog pravila, je li jedan ishod neovisan o
drugome i ima li binarni ishod konačnu varijancu? Kad su odgovori potvrdni,
povećanjem broja pokušaja simulirane se stope zbijaju i njihov oblik postaje
bliži zvonastome. To ne znači da pojedinačni ishodi postaju normalno
raspodijeljeni. Jaka ovisnost među opažanjima, promjenjiva vjerojatnost ishoda ili
beskonačna varijanca traže drukčiji model ili dodatne uvjete. Poglavlje o
uzorkovanju od ovoga ograničenog slučaja gradi svoj argument.

Sredina i standardna devijacija potpuno određuju položaj i širinu normalne
raspodjele. Unutar jedne standardne devijacije od sredine leži oko 68 %
vrijednosti, unutar dvije oko 95 %, a unutar tri oko 99,7 %.

Sada mijenjamo predmet. Više ne promatramo raspodjelu ponovljenih stopa, nego
raspodjelu pojedinačnih vrijednosti u poznatoj populaciji. Središnji granični
teorem ne čini te vrijednosti normalnima. Pravilo područja stoga provjeravamo
zasebno, na dnevnom vremenu provedenom uz medije i iznosu koji je osoba spremna
platiti za pristup sadržaju.

*Slika. Dnevne minute uz medije i spremnost na plaćanje u simuliranoj populaciji, s isprekidanim crtama na jednoj i dvjema standardnim devijacijama od sredine.*

Za dnevne minute pravilo vrijedi približno. Unutar jedne standardne devijacije
nalazi se
`r hr_broj(s7_podrucja$minute[1])` % populacije, unutar dviju
`r hr_broj(s7_podrucja$minute[2])` %, a unutar triju
`r hr_broj(s7_podrucja$minute[3])` %. Odstupanja od 68, 95 i 99,7 postoje i
posljedica su blage nagnutosti udesno, ali su dovoljno mala da orijentacija
ostane upotrebljiva.

Za spremnost na plaćanje pravilo se raspada. Unutar jedne standardne devijacije
leži `r hr_broj(s7_podrucja$iznos[1])` % populacije umjesto oko 68 %, a unutar
triju samo `r hr_broj(s7_podrucja$iznos[3])` % umjesto oko 99,7 %. Razlog je
vidljiv na grafu. Udio ljudi s nultim iznosom jest
`r hr_broj(s7$bez_platnika)` %, pa se raspodjela nagomilala na nuli i ima dugi
rep udesno. Donja granica od jedne
standardne devijacije ispod sredine pada u negativne iznose, koje nitko ne može
imati, pa ispod nje nema nijedne osobe.

Ako pogledamo samo one koji nešto plaćaju i njihove iznose logaritmiramo, prikaz
postaje bliži zvonastome. Poglavlje o sažimanju podataka pokazalo je isti učinak
promjene ljestvice na primjeru vremena korištenja. Pravilo sada vrijedi gotovo
točno, s
`r hr_broj(s7_podrucja$log_iznos[1])` %,
`r hr_broj(s7_podrucja$log_iznos[2])` % i
`r hr_broj(s7_podrucja$log_iznos[3])` %. Zvonasti oblik dakle ne opisuje sirove
iznose; pojavio se tek nakon isključenja nula i promjene ljestvice.
Isključenje neplatitelja mijenja populaciju i istraživačko pitanje, pa bolji
pristaj normalnoj krivulji sam ne opravdava tu odluku.

## Kad podaci ne pristaju krivulji

Postotci unutar područja govore o cjelini i mogu prikriti gdje točno raspodjela
odstupa. Prikaz koji odgovara na to pitanje poreda opažene vrijednosti po
veličini i svaku od njih stavi nasuprot vrijednosti koja bi na tom mjestu bila
očekivana da raspodjela jest normalna. Kad se oblici poklapaju, točke leže na
pravcu.

*Slika. Poredane vrijednosti triju varijabli nasuprot vrijednostima očekivanima prema normalnoj raspodjeli. Pravac označuje savršeno poklapanje.*

Svaki oblik odstupanja nosi svoju poruku. Dnevne minute prate pravac gotovo
cijelim rasponom i odižu se tek na desnom kraju, što je potpis blagog repa prema
većim vrijednostima. Spremnost na plaćanje leži vodoravno dok traju nule i zatim
naglo skreće uvis, jer normalna raspodjela na tom mjestu očekuje postupan
prijelaz, a podaci ga nemaju. Logaritmirani iznosi vraćaju se na pravac.

Prikaz ne izriče presudu o tome je li analiza dopuštena. On pokazuje gdje
pretpostavka pristaje, a gdje se lomi, i time razdvaja odstupanja koja ne moraju
imati iste posljedice. Važnost blagog odizanja repa ovisi o ciljnoj veličini,
postupku i utjecaju krajnjih vrijednosti. Gomila na nuli jasno pokazuje samo da
normalna raspodjela ne opisuje sirove iznose.

## Nizovi koje slučajnost proizvodi

**Slučajni niz** je slijed ishoda koje proizvodi proces s poznatom slučajnom
sastavnicom, bez zahtjeva da kratki odsječak izgleda pravilno. Vratimo se
pitanju iz vinjete, jer ono ima odgovor koji se može izmjeriti.
Za mjerenje učinka samoga odabira simuliramo uži nulti model. Svaki je pokušaj
neovisno bacanje poštenoga novčića s fiksnom vjerojatnošću pogotka. Taj model ne
tvrdi da se stvarna igračeva vjerojatnost ne može mijenjati. U svakom nizu
izdvajamo pokušaje koji dolaze neposredno iza tri uzastopna pogotka. Bez učinka
odabira očekivali bismo da među izdvojenima pogodaka bude pola.

*Slika. Prosječan udio pogodaka na pokušajima koji slijede zadani niz pogodaka, u simulaciji poštenog novčića bez ikakve memorije. Izrada autora.*

Udio je manji od polovice. U nizu od stotinu pokušaja prosječan udio iza tri
pogotka iznosi
`r hr_broj(s7$nakon_tri_100, 3)`, a u nizu od dvadeset pokušaja pada na
`r hr_broj(s7$nakon_tri_20, 3)`. Postupak pritom nema nikakvu memoriju, jer smo
ga sami napravili takvim. Odstupanje ne dolazi iz procesa nego iz odabira.

Razlog je u konačnosti niza. Kad iz jednog niza izdvojimo upravo ona mjesta koja
dolaze iza tri pogotka, sam uvjet troši pogotke. Niz s malo pogodaka rijetko
uopće nudi takvo mjesto, a u nizu koji ga nudi tri su pogotka već potrošena na
uvjet, pa ih je za promatrano mjesto ostalo manje nego što ih niz prosječno ima.
Prosjek takvih udjela zato leži ispod stvarne vjerojatnosti, i to više što je niz
kraći i uvjet dulji. Uz uvjet od samo jednog pogotka u nizu od stotinu pokušaja
odstupanje pada na `r hr_broj(s7$nakon_jednog_100, 3)` i jedva se primjećuje.

Veličina tog odstupanja nije akademska sitnica. U nizu od stotinu pokušaja ono
iznosi oko četiri postotna boda, što je istog reda kao razlika koju bi netko
tražio da pokaže postojanje forme. Postupak mjerenja time proizvodi pomak u
smjeru zaključka koji se donosi.

Pouka nadilazi košarku i nije o tome tko je bio u pravu. Analiza koja iz podataka
izdvoji jedinice po nekom svojstvu tih istih podataka nije više neutralan pogled
na njih, jer je odabir dio postupka jednako kao i račun koji slijedi.
Najizravniji način u ovom poglavlju da se to provjeri jest primijeniti cijeli
postupak, s odabirom uključenim, na podatke u kojima se odgovor unaprijed zna.
Upravo to knjiga radi otkad je populacija poznata, i to je razlog zbog kojeg
simulacija u ovim poglavljima dolazi prije formule.

**Statistika u divljini.**
**Vruća ruka i njezin ispravak.** Gilovich, Vallone i Tversky protumačili su
svoje nalaze kao dokaz da se nizovi pogodaka pogrešno čitaju kao promjena
igračeve vjerojatnosti pogotka (Gilovich, 1985). Miller i Sanjurjo pokazali su
da uobičajena mjera uvjetne ovisnosti nosi pristranost odabira niza, da su
izvorna studija i njezina ponavljanja na nju osjetljivi te da se zaključak
izvorne studije nakon ispravka obrće (Miller, 2018).

Promijenio se postupak čitanja istih podataka. Simulacija u prethodnom odjeljku
mjeri vrstu pristranosti koju Miller i Sanjurjo izvode za konačne nizove
(Miller, 2018). Iz toga ne slijedi da je vruća ruka dokazana, nego da izvorni
nalaz nije podupirao zaključak koji mu je pripisan. Tvrdnja o odsutnosti učinka
traži jednako pažljivo mjerenje kao tvrdnja o njegovu postojanju. Stvarna bi
promjena forme morala biti razlučena i od težine šuta, obrane te odabira
pokušaja; niz sam po sebi ne bira među tim objašnjenjima.

**Pitajte model.**
Asistent može izračunati vjerojatnost pod zadanim modelom i izvesti simulaciju,
ali slaganje tih putova provjerava samo unutarnju dosljednost računa, ne i model
stvarnoga procesa. U odgovoru zato tražimo tri moguća promašaja. Neovisnost može
ostati neizrečena, ukupna i uvjetna vjerojatnost mogu dobiti zamijenjene
nazivnike, a vjerojatnost ishoda pod modelom može postati neopravdana
vjerojatnost samoga modela.

> Navedi koje pretpostavke o neovisnosti i jednakoj vjerojatnosti koristiš prije
> nego što bilo što izračunaš. Zapiši događaj i njegov komplement, izračunaj
> rezultat analitički, zatim ga približno provjeri simulacijom sa sjemenom 709 te
> pokaži da se dobiveni broj nalazi između nule i jedan.

| Polje računa | Zapis |
|---|---|
| Što je traženo | analitička i simulacijska vjerojatnost istoga ishoda pod izričitim modelom |
| Što je vraćeno | dva broja, sjeme, korištene pretpostavke i granica zaključka |
| Što je provjereno | događaj, komplement, nazivnik, neovisnost, jednaka vjerojatnost i podudaranje dvaju putova |
| Kako je provjereno | ručnim čitanjem komplementa, provjerom granica i izvršivom simulacijom sa sjemenom 709 |
| Uloga AI-ja | instrument za račun i pogrešiv analitičar pri tumačenju |
| Što je ostalo neprovjereno | opisuje li zadani model stvarni proces i jesu li dostupne informacije potpune |
| Odgovorna osoba | osoba koja potpisuje zaključak |

**Nađite grešku.**
U hipotetskom modelu svakoj se objavi zadaje vjerojatnost od dva posto da u
sedam dana prijeđe unaprijed dogovoren prag dijeljenja. To je ulaz modela, a ne
izmjeren udio. Na pitanje koliko je vjerojatno da barem jedna od pet objava iste
kampanje prijeđe prag asistent je napisao ovu analizu.

Uz ispis je dodao obrazloženje. Vjerojatnost da pojedina objava ne postane
viralna iznosi 0,98, vjerojatnost da nijedna od pet ne postane viralna je
0,98 na petu potenciju, a komplement toga daje 9,6 %. Budući da su objave
zasebne jedinice iste kampanje, zaključuje da je račun potpun.

## Razrađeni primjer

Zamislimo e-bilten poslan na pedeset adresa i otvoren četrnaest puta. Radi
provjere računa zadajemo referentni model u kojem svaka poruka ima jednaku,
poznatu vjerojatnost otvaranja od dvadeset dva posto, a otvaranja su međusobno
neovisna. Brojevi su hipotetski i nisu mjerenje stvarne kampanje. Pitanje glasi
koliko je četrnaest ili više otvaranja neobično pod tim modelom. Vjerojatnost
računamo iz binomne raspodjele, a zatim je približno provjeravamo brojanjem u
dvadeset tisuća simuliranih kampanja.

Funkcija `pbinom` vraća vjerojatnost da uspjeha bude najviše onoliko koliko je
zadano, pa je komplement te vrijednosti pri trinaest upravo vjerojatnost od
četrnaest naviše. Funkcija `rbinom` izvlači slučajne ishode iz iste raspodjele,
pa njihov udio daje približno isti broj kada su kod i pretpostavke dosljedni.

Analitički put daje `r hr_broj(s7$tocno)` %, a simulacija
`r hr_broj(s7$simulirano)` %. Mala razlika nastaje zato što je broj simuliranih
kampanja konačan. Njihova blizina interna je računska provjera, a ne neovisan
dokaz da model opisuje stvarni proces.

Pod zadanim bi modelom četrnaest ili više otvaranja nastalo otprilike jednom u
pet ponavljanja. Ishod zato nije osobito neobičan za taj model, ali time model
nije potvrđen. Čak ni mnogo rjeđi ishod ne bi pokazao da ga je uzrokovao naslov.
Publika, vrijeme slanja, doseg i drugi dijelovi procesa ostali bi moguća
objašnjenja. Tvrdnja o učinku naslova tražila bi usporedbu nasumično dodijeljenih
inačica, a urednička odluka još i cilj te troškove pogreške.

Ovdje čitamo samo jednostranu repnu vjerojatnost pod izričitim modelom. Sljedeće
poglavlje pita kako se statistika mijenja od uzorka do uzorka; formalna pravila
testiranja i odluke dolaze poslije toga.

## Sažetak

Vjerojatnost pripada opisanom modelu i informacijama; modelna vjerojatnost nije
isto što i osobna sigurnost, a kalibraciju procjenjujemo kroz ishode mnogih
usporedivih prognoza. Komplement, zbrajanje i opće pravilo množenja traže jasno
imenovane događaje i nazivnike, dok prečac s umnoškom rubnih vjerojatnosti traži
neovisnost. Binomna raspodjela opisuje ponovljene binarne pokušaje kada su
njezini uvjeti ispunjeni, a središnji granični teorem pod svojim uvjetima govori
o raspodjeli zbrojeva ili prosjeka, ne o obliku pojedinačnih podataka. Pravilo
68–95–99,7 vrijedi za približno normalne raspodjele, dok je simulacija nizova
pokazala da i postupak odabira može proizvesti pomak koji tražimo. Poglavlje o
uzorkovanju tu logiku prenosi na statistike koje se mijenjaju od uzorka do
uzorka.

## Pojmovi

vjerojatnost (*probability*), zakon velikih brojeva (*law of large numbers*),
kalibrirana nesigurnost (*calibrated uncertainty*), neovisnost
(*independence*), uvjetna vjerojatnost (*conditional probability*), binomna
raspodjela (*binomial distribution*), normalna raspodjela (*normal
distribution*), QQ prikaz (*Q–Q plot*), slučajni niz (*random sequence*)

## Zadaci

### Konceptualni

Usporedite niz od pet glava iz modela poštenoga novčića s poznatom
vjerojatnošću i pet uspješnih objava kampanje čija stopa uspjeha nije poznata.
Objasnite zašto zadana vjerojatnost sljedećeg bacanja ostaje ista, dok uspjesi
mogu promijeniti uvjerenje o nepoznatoj stopi kampanje čak i kada uspjeh jedne
objave ne mijenja izglede sljedeće. Odvojeno navedite koji bi dokaz bio potreban
za tvrdnju da takva promjena ipak postoji. Na kraju prosudite smije li se pravilo
68–95–99,7 primijeniti na raspodjelu s velikom skupinom nula i navedite što bi u
QQ prikazu poduprlo vaš odgovor.

### Računski

Vratite se na hipotetsku provjeru zapisa i protokol skeptičnoga čitanja iz
poglavlja o tome kako brojke zavode. Iz ranijega primjera dohvatite potrebne
brojnosti, a na tvrdnju „provjera je pouzdana jer nalazi devedeset posto ciljanih
zapisa” primijenite svih šest ondje razvijenih revizijskih pitanja. Zatim
izračunajte udio upozorenja među ciljanim zapisima, udio ciljanih zapisa među
svim upozorenjima i temeljnu stopu. Predajte kratku revizijsku tablicu, račun i
dvije rečenice koje jasno omeđuju tumačenje. Bez ranijega protokola račun nije
potpun odgovor.

### Kritički

Prosudite kako je nalaz o vrućoj ruci prešao put od mjerenja do općenite tvrdnje
o ljudskoj procjeni slučajnosti, i što se u toj tvrdnji promijenilo nakon
ispravka mjere (Gilovich, 1985; Miller, 2018). Predajte jedan odlomak i imenujte
rečenicu koju bi popularni prikaz smio zadržati.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte korake računa koji su ispravni,
označite račun koji vrijedi samo uz neovisnost, zatim izdvojite rečenicu u kojoj
je neovisnost neopravdano proglašena potvrđenom i napišite rečenicu kojom bi
izvještaj morao ograničiti svoj zaključak.
