# DIO III: OD UZORKA DO POPULACIJE

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

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

---

# Uzorkovanje

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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
poništavaju. Dobitak zato ne raste s brojem ljudi nego s korijenom toga broja.

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
pretvara u procjenu samo zamjenom jednoga slova. Poglavlje o sažimanju podataka
tu je zamjenu pripremilo kada je varijancu uvelo s djeliteljem umanjenim
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

Svako deseterostruko povećanje uzorka smanjuje standardnu pogrešku za faktor
$\sqrt{10}$, približno 3,16. Da bi se standardna pogreška prepolovila, uzorak se
mora učetverostručiti. Zahtjev za užom slučajnom raspršenošću zato se plaća sve
većim brojem opažanja.

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
jedinica ne nosi gotovo cijeli zbroj. Jedna okrugla granica ne vrijedi za sve
populacije. U našoj simulaciji trideset osoba nije bilo dovoljno da asimetrija
izrazito asimetrične varijable nestane, dok se raspodjela sredina gotovo
simetrične varijable može urediti i pri manjem uzorku. Potrebna veličina ovisi o
obliku i repovima izvorne raspodjele, a ne o jednom broju.

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

## Preciznost ankete od osamsto ljudi

Kada je anketni rezultat udio, pitanje preciznosti postavlja se za **uzorački
udio**, koji označavamo s $\hat{p}$ i koji procjenjuje populacijski udio. Logika
ostaje ista, jer je udio prosjek niza nula i jedinica, pa ga središnji granični
teorem pokriva jednako kao svaku drugu sredinu. Mijenja se samo to što
raspršenost udjela ne treba mjeriti posebno. Kod varijable koja poprima samo
dvije vrijednosti raspršenost je određena samim udjelom, najveća je kada je
populacija podijeljena napola i pada kako se udio primiče nuli ili jedinici.

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
of error*). Budući da je raspršenost najveća pri udjelu od 50 %, uvrštavanjem te
vrijednosti dobiva se najgori slučaj, koji vrijedi bez obzira na to kakav će
rezultat ispasti. Pri razini od 95 % upotrijebljenoj u nastavku margina se tada
svodi na približno jedan podijeljen korijenom veličine uzorka.

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

Kada izvještaj navodi da prva opcija ima 32 %, a druga 29 %, same dvije
procjene i njihove pojedinačne margine nisu dovoljne za tvrdnju da je prva
opcija ispred druge. Razlika dvaju udjela ima vlastitu nesigurnost, koju treba
izračunati iz zajedničkoga nacrta.

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

Margina pogreške ne pokriva sve izvore nesigurnosti. Ona mjeri isključivo
promjenjivost koja dolazi od slučajnog izvlačenja
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
više populacijskih jedinica. Taj doprinos zapisuje **težina uzorkovanja**, koja
se u početku računa kao obrnuta vjerojatnost uključivanja. Procjena bez težina
u takvu nacrtu previše predstavlja često birane jedinice, ali ni ispravna
procjena s težinama sama ne može vratiti skupinu koju okvir uopće nije
pokrivao.

Učinak težina možemo reproducirati bez stvarnih
mikropodataka. Sljedeća tablica prikazuje šest opaženih jedinica iz zasebne
sintetičke konačne populacije od šesnaest osoba, po osam u svakom sloju.
Odgovor jedan znači da osoba podržava zamišljenu mjeru, a odgovor nula da je ne
podržava. Jedinice iz prvoga sloja imale su vjerojatnost uključivanja 0,50, a
jedinice iz drugoga 0,25. Njihove su početne težine zato dva i četiri.

*Slika. Opaženi uzorak iz sintetičke konačne populacije s poznatim vjerojatnostima uključivanja. Izrada autora.*

Bez težina brojnik je
`r hr_broj(s8_tezine_rez$brojnik_bez_tezina, 0)`, nazivnik
`r hr_broj(s8_tezine_rez$nazivnik_bez_tezina, 0)`, a procjena
`r paste0(hr_broj(100 * s8_tezine_rez$procjena_bez_tezina, 1), " %")`. S
težinama brojnik postaje
`r hr_broj(s8_tezine_rez$brojnik_s_tezinama, 0)`, nazivnik
`r hr_broj(s8_tezine_rez$nazivnik_s_tezinama, 0)`, a procjena
`r paste0(hr_broj(100 * s8_tezine_rez$procjena_s_tezinama, 1), " %")`.
Procjena se smanjila jer su dvije jedinice s odgovorom nula iz rjeđe
uključivanoga sloja dobile veći doprinos u nazivniku. Vrijednost 37,5 % i dalje
je procjena, a ne poznati udio cijele sintetičke populacije; težine ne uklanjaju
pogrešku uzorkovanja. Rezultat nije tvrdnja o stvarnoj populaciji, nego provjera
računa na potpuno vidljivoj nastavnoj tablici.

U stvarnoj anketi početne se težine mogu dodatno prilagoditi zbog neodgovora i
zatim prolaze **kalibraciju**, pri kojoj se zbrojevi s težinama za pomoćna
obilježja usklađuju s poznatim populacijskim zbrojevima, primjerice po dobnim
skupinama. Kalibracija može popraviti sastav uzorka samo za opažena pomoćna
obilježja i uz pretpostavku
da ona nose relevantne razlike. Ne može pronaći jedinice izvan okvira, ukloniti
neizmjerene razlike između onih koji jesu i nisu odgovorili ni ispraviti loše
postavljeno pitanje.

Drugi nacrti najprije biraju skupine poput kućanstava, škola ili naselja, a
zatim jedinice unutar njih. Takvo **grupno uzorkovanje** štedi terenski rad.
Kada su osobe iz iste skupine sličnije nego nasumično izabrane osobe iz cijele
populacije, stotinu ljudi iz nekoliko skupina može nositi manje neovisne
informacije od stotinu ljudi raspršenih po populaciji. Obična formula s
korijenom iz $n$ tada bi preciznost prikazala prevelikom.

**Učinak nacrta** uspoređuje varijancu procjene pod stvarnim nacrtom s
varijancom koju bi dao jednostavni slučajni uzorak iste nominalne veličine.
Njegov prijevod u broj čitatelju daje **efektivna veličina uzorka**, odnosno
veličina jednostavnoga slučajnog uzorka koja bi nosila približno jednaku
preciznost. Grupiranje i vrlo nejednake težine mogu smanjiti efektivnu veličinu,
dok je pažljivo raslojavanje može povećati. Učinak nacrta pripada
određenoj procjeni i ne mora biti isti za svaki udio ili sredinu u istoj anketi.

Za takve nacrte procjena, standardna pogreška i margina moraju se računati
postupkom koji poznaje težine, skupine i eventualne slojeve. Čitatelj ne mora
izvoditi te formule, ali mora u izvještaju tražiti kako je nacrt uključen u
račun. Nijedna od dviju jednostavnih formula iz ovoga poglavlja ne prenosi se
nepromijenjena na nejednake vjerojatnosti ili grupiranje.

## Pokrivenost, odabir i odaziv

**Pogreška pokrivenosti** nastaje kada okvir iz kojega se bira ne dopušta svim
jedinicama ciljne populacije da uopće uđu u uzorak. Povećanje broja odabranih
jedinica unutar istoga okvira ne doseže one koji u njemu nedostaju.

Drukčiji problem nastaje kada vjerojatnosti odabira nisu poznate. U prigodni
uzorak istraživač uključuje one koji su mu dostupni. U našoj populaciji skupina
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
`r hr_broj(s8$online_n, 0)` osoba, dakle mnogostruko veći od jednostavnoga
slučajnog uzorka od sto osoba s početka poglavlja. Njegov prosjek dobi iznosi
`r hr_broj(s8$online_dob, 1)`
godina naspram `r hr_broj(s8$dob, 1)` u populaciji, udio korisnika društvenih
mreža `r paste0(hr_broj(100 * s8$online_mreze, 1), " %")` naspram
`r paste0(hr_broj(100 * s8$udio_mreze, 1), " %")`, a prosječno povjerenje
`r hr_broj(s8$online_sredina, 2)` naspram `r hr_broj(s8$mu, 2)`.

Treći oblik pogađa i istraživanja koja su sve napravila ispravno pri odabiru.
Uzorak može biti izvučen slučajno iz dobroga popisa, a onda dio odabranih ne
odgovori. Taj **neodgovor** smanjuje veličinu uzorka, ali ne mora stati na gubitku
preciznosti. Ako oni koji ne odgovaraju nalikuju onima koji odgovaraju u
obilježju koje procjenjujemo, procjena ostaje usmjerena prema istoj vrijednosti.
Ako se razlikuju, primjerice po zanimanju za temu ili povjerenju u onoga tko
pita, procjena može postati pristrana bez obzira na to kako je uzorak odabran.
Postupak odabira i postupak odaziva dva su različita filtra.

Kod tolikog uzorka standardna pogreška može biti sitna, pa bi izvještaj mogao
objaviti vrlo uzak interval oko sustavno pogrešne ciljne vrijednosti. Dok
standardna pogreška u zadanom nacrtu pada s veličinom uzorka, pristranost zbog
nepromijenjenoga mehanizma odabira ne mora padati i standardna je pogreška ne
prikazuje. Veći pristrani uzorak zato može dati vrlo preciznu procjenu pogrešne
ciljne vrijednosti.

Kartica za čitanje ankete iz 3. poglavlja sada dobiva statističku svrhu. Nije
dovoljno prepisati postotak i marginu; svako polje otvara pitanje o tome što
procjena uopće može predstavljati.

| Polje kartice | Pitanje nakon ovoga poglavlja |
|---|---|
| ciljna populacija i okvir | Tko je trebao biti obuhvaćen, a tko nije mogao ući u uzorak? |
| regrutiranje | Je li odabir vjerojatnosan ili se sudionici sami prijavljuju? |
| pozvani i odgovori | Koliki je odaziv i po čemu bi se neodgovori mogli razlikovati? |
| težine i kalibracija | Koje su razlike u uključivanju ili sastavu prilagođene, a koje nisu? |
| datum, formulacija i naručitelj | Može li se rezultat vezati uz točno pitanje, razdoblje i izvor? |
| procjenjivana veličina i podskupina | Koji broj ulazi u stvarni nazivnik procjene? |
| nesigurnost | Uvažava li račun težine, slojeve i skupine stvarnoga nacrta? |

: Kartica za čitanje ankete nakon poglavlja o uzorkovanju. Izrada autora.

## Korpus kao uzorak

Ista pitanja vrijede kada jedinice nisu ljudi nego tekstovi. Želimo li opisati
jezik političke rasprave, „svi dostupni tekstovi” nije populacija. Najprije
treba odrediti ulaze li govori, intervjui ili objave, s kojih platformi ili iz
kojih arhiva, između kojih datuma, na kojim jezicima i od kojih govornika. Svaka
od tih granica mijenja ciljnu populaciju tekstova i okvir iz kojega korpus
stvarno može biti sastavljen.

Arhiv može izostaviti obrisane ili privatne objave, platforma može ograničiti
pristup starijem sadržaju, a pretraga može propustiti tekstove koji ne nose
odabranu ključnu riječ. Velik broj riječi ne uklanja takvu pogrešku pokrivenosti
ni samoodabir govornika koji su se na promatranoj platformi uopće oglasili.
Zaključak zato mora ostati unutar granica govora, platforme, datuma, jezika i
govornika koje je postupak uključivanja doista obuhvatio.

Granica nije dovršena dok se ne odrede jedinica i nazivnik. Brojanje riječi
daje veći doprinos duljim tekstovima, brojanje objava veću ulogu vrlo aktivnim
govornicima, a udio govornika odgovara na treće pitanje. Nijedan od tih izbora
nije automatski pogrešan, ali odgovor o „zastupljenosti” nema jasno značenje dok
se ne kaže predstavlja li jedan slučaj riječ, tekst, govornički istup ili
govornika. Izvještaj o korpusu zato uz granice uključivanja treba navesti i što
je jedinica, mogu li se jedinice istoga govornika ponavljati te koji broj čini
nazivnik svake usporedbe.

Podjela već sastavljenoga korpusa na skup za učenje, provjeru i ispitivanje,
provedena na odgovarajućoj jedinici i bez curenja informacija, pokazuje koliko
je prediktivni postupak stabilan na novim jedinicama iz približno istoga procesa
prikupljanja. Ta podjela sama ne popravlja
pokrivenost korpusa i ne daje pravo na zaključak o govornicima ili tekstovima
koji u okvir nisu mogli ući. Populacijsko uopćavanje i prediktivna provjera zato
su dvije različite granice tvrdnje.

**Statistika u divljini.**
**Deset milijuna listića i pogrešan pobjednik.** Časopis *Literary Digest*
razaslao je uoči američkih izbora 1936. milijune probnih listića i na temelju
vraćenih odgovora objavio predviđanje koje je promašilo pobjednika. Istodobne
ankete s drukčijim postupcima odabira razumno su predvidjele ishod
(Squire, 1988).

Uzorak nije zakazao zbog veličine. Popisi iz kojih su adrese izvučene
obuhvaćali su imućnija kućanstva sustavno češće od ostalih, a listić je vratio
tek dio onih koji su ga primili, pa se skupina koja je odgovorila razlikovala od
skupine koja nije (Squire, 1988). Pokrivenost i neodgovor djelovali su u istom
smjeru, a nijedan se nije mogao popraviti slanjem još listića
(Squire, 1988). Slučaj ne pokazuje da je malen uzorak bolji, nego da sama
veličina nije jamstvo valjanoga zaključka.

**Pitajte model.**
Asistent može napisati simulaciju distribucije uzorkovanja, ali treba mu
odvojeno zadati populaciju, postupak odabira, veličinu uzorka i
statistiku koja se računa. Kod jednostavnoga slučajnog uzorka provjeravamo
uzorkuje li s vraćanjem samo kada je to namjera. Kod složenoga nacrta tražimo da
u račun unese težine, skupine i slojeve umjesto da primijeni običnu formulu s
korijenom iz $n$. Važna se pogreška može pojaviti u rečenici koja prati kod,
gdje se raspršenost pojedinaca predstavi kao standardna pogreška procjene.

> Simuliraj mnogo neovisnih uzoraka iz zadane populacije. Prikaži raspodjelu
> uzoračkih sredina i odvojeno navedi standardnu devijaciju opažanja te
> standardnu pogrešku sredine.

**Nađite grešku.**
Veći nasumični uzorak daje užu distribuciju uzoračkih sredina. Budući da je
standardna pogreška manja, vrijednosti pojedinaca u većem uzorku također su
međusobno sličnije.

## Razrađeni primjer

Velik dio aparata zaključivanja koji ova knjiga razvija može se razumjeti kroz
jednu petlju. Izvuci uzorak, izračunaj mjeru, ponovi mnogo puta i pogledaj što je
nastalo. Mnoge formule u sljedećim poglavljima sažimaju ili aproksimiraju ono
što bi takvo ponavljanje pokazalo unutar određenoga modela. Petlju zato vrijedi
jednom vidjeti ispisanu u cijelosti, na najzahtjevnijoj varijabli naše
populacije.

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
standardnoj pogrešci potvrđuje na varijabli za koju bi se očekivalo najveće
odstupanje. Vrijedi zapaziti i što petlja nije popravila. Uzorak od pet
osoba i dalje daje raspodjelu sredina koja je vidljivo iskrivljena, pa
nepristranost i normalnost nisu isto svojstvo i ne stižu u istom trenutku.

Ta je provjera moguća samo zato što je populacija izmišljena. Prvi redak poziva
`populacija_medija` i time čini nešto što nijedno
stvarno istraživanje ne može, jer izvlači uzorke iz cjeline kojoj bi inače bilo
nemoguće pristupiti. Istraživač koji radi s podacima ima jedan uzorak i nijednu
mogućnost da petlju stvarno pokrene. Mnogi postupci u nastavku procjenjuju
njezin rezultat ili njegova bitna svojstva iz jednoga uzorka i unutar
određenoga modela. Poglavlje o procjeni prvo je od tih zaobilaženja. Ono uzorku
dopušta da nakratko preuzme ulogu populacije i time istu petlju vraća u ruke
nekome tko ima samo osamsto ispitanika.

## Sažetak

Uzorak je jedan ishod postupka odabira, a distribucija uzorkovanja opisuje kako
bi se procjena mijenjala kroz ponovljene izvlačenja. Njezinu širinu mjeri
standardna pogreška, koja pripada procjeni, a ne pojedincima, i pada s korijenom
veličine jednostavnoga slučajnog uzorka, uz korekciju kada uzorak obuhvaća
znatan dio konačne populacije. Složeniji nacrti mogu zahtijevati procjene s
težinama, a nesigurnost se računa postupkom koji uvažava težine, skupine i
slojeve. Učinak nacrta i efektivna veličina uzorka sažimaju posljedice toga
nacrta. Kalibracija može približiti uzorak poznatom sastavu populacije, ali ni
ona ni velik uzorak ne popravljaju automatski pogrešku pokrivenosti, neodgovor
ili samoodabir. Isto ograničenje vrijedi za korpus, čije granice govora,
platforme, datuma, jezika i govornika određuju doseg tvrdnje. Poglavlje o
procjeni uzet će distribuciju uzorkovanja i iz nje izgraditi raspon oko
vrijednosti koju ne možemo izravno vidjeti.

## Pojmovi

populacija (*population*), uzorak (*sample*), parametar (*parameter*),
statistika (*statistic*), pogreška uzorkovanja (*sampling error*), distribucija
uzorkovanja (*sampling distribution*), nepristranost (*unbiasedness*),
standardna pogreška (*standard error*), središnji granični teorem (*central
limit theorem*), uzorački udio (*sample proportion*), margina pogreške (*margin
of error*), jednostavni slučajni uzorak (*simple random sample*), korekcija za
konačnu populaciju (*finite-population correction*), vjerojatnosno uzorkovanje
(*probability sampling*), težina uzorkovanja (*sampling weight*), procjena s
težinama (*weighted estimate*), kalibracija (*calibration*), grupno uzorkovanje
(*cluster sampling*), učinak nacrta (*design effect*), efektivna veličina uzorka
(*effective sample size*), pokrivenost (*coverage*), neodgovor (*nonresponse*),
prigodni uzorak (*convenience sample*), samoodabir (*self-selection*)

## Zadaci

### Konceptualni

Razlikujte raspodjelu pojedinačnih opažanja od distribucije uzoračkih sredina.
Za svaku navedite što joj je jedinica, što mjeri njezina širina i što se s njom
događa kada uzorak naraste. Predajte skicu obiju raspodjela i dva popratna
objašnjenja.

### Računski

Upotrijebite tablicu opaženoga uzorka iz sintetičke konačne populacije. Bez
programa izračunajte brojnik, nazivnik i postotak prvo bez težina, a zatim s
težinama uzorkovanja. Objasnite zašto se procjena pomaknula prema dolje i
navedite jednu pogrešku koju taj pomak ne može ispraviti. Predajte oba računa i
dvije rečenice tumačenja.

Neobvezna nadogradnja dostupna je samo čitatelju s vlastitom službeno preuzetom
kopijom ESS Round 11, edition 3.0. Slijedeći portalnu putovnicu iz kataloga,
ograničite podatke na Hrvatsku, za `vote` primijenite njegov službeni valjani
nazivnik te usporedite procjenu bez težina s procjenom uz zadani `anweight`.
Navedite i jednu pogrešku odabira ili mjerenja koju ta težina ne može ukloniti.
Rezultat tumačite kao samoprijavu, ne kao provjeru službene izlaznosti. ESS
mikropodaci i rezultat te provjere nisu dio knjige ni obveznoga zadatka.

### Kritički

Vratite se na početnu karticu za čitanje ankete iz 3. poglavlja i primijenite je
na slučaj časopisa *Literary Digest* (Squire, 1988). Za ciljnu populaciju, okvir,
regrutiranje, broj pozvanih i odgovora, datume, formulaciju pitanja, težine,
naručitelja i marginu pogreške označite što je iz prikazanoga slučaja poznato,
a što nije. Zatim odvojite pogrešku pokrivenosti i neodgovor od slučajne
promjenjivosti te objasnite zašto veći broj poslanih listića ne rješava prva dva
problema. Ne dopunjujte nepoznata polja pretpostavkama. Predajte ispunjenu
karticu i jedan odlomak zaključka.

### Revizija modela

Ocijenite analizu modela iz okvira o pogrešci. Izdvojite tvrdnju koja je točna,
imenujte zamjenu dviju razina varijabilnosti i napišite ispravljenu verziju
druge rečenice koja zadržava sve što je u njoj bilo točno.

---

# Procjena

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

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

Prije nego što rasponu damo ime, vratimo se poznatoj populaciji. Deset tisuća
puta izvukli smo po dvjesto osoba. Oko svake dobivene sredine povukli smo
raspon od 1,96 njezinih standardnih pogrešaka na svaku stranu i provjerili
siječe li fiksnu populacijsku vrijednost. Cilj je obuhvaćen u
`r paste0(hr_broj(s9$pokrivenost, 1), " %")` raspona, a promašen u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja.
Pojedini raspon može promašiti, ali postupak kroz ponavljanja pokazuje stabilan
udio pogodaka.

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

Slovo $z^{*}$ označava koliko standardnih pogrešaka širimo na svaku stranu.
Bira ga željena razina, pa je za 95 % jednako 1,96.

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

Za naš uzorak taj račun daje raspon od `r hr_broj(s9$donja, 2)` do
`r hr_broj(s9$gornja, 2)`, a prava populacijska vrijednost iznosi
`r hr_broj(s9$mu, 2)` i nalazi se unutra.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Vrijedi obratiti pozornost na to gdje u toj definiciji stoji obećanje. Ono ne
stoji uz raspon nego uz postupak, i upravo se ta razlika u praksi najčešće gubi.

Polovica ukupne širine toga raspona jest **margina pogreške**. Poglavlje o tome
kako brojke zavode ostavilo ju je kao dug kada je uz anketni postotak prikazalo
znak ±, a sada je vidljivo što taj znak sažima. U ovom postupku margina iznosi
$z^{*} \cdot SE$ i pokriva promjenjivost koju bi ponovljeno uzorkovanje
proizvelo pod pretpostavkama postupka. Ne pokriva pristran okvir, neodgovor,
formulaciju pitanja ni pogrešku mjerenja. Zato manja margina znači uži raspon
uzoračke neizvjesnosti, a ne općenito bolju anketu.

## Obećanje razine pouzdanosti

Simulirani postupak radi približno onako kako obećava, i vrijedi zadržati riječ
približno. Broj pogodaka u konačnom nizu nije unaprijed propisan. Zamjena
nepoznate populacijske raspršenosti onom izmjerenom u uzorku
unosi vlastitu nesigurnost, koja je pri dvjesto osoba mala, a pri dvadeset osoba
ne bi bila. Ispravak koji to nadoknađuje širi interval za mali uzorak i knjiga
ga uvodi u poglavlju o usporedbi dviju grupa, gdje ga postupak prvi put stvarno
treba.

Ono što se u brojci od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne vidi jest
sudbina pojedinačnog intervala. Svaki od tih deset tisuća raspona ili sadrži
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
Vrijednosti unutar granica uskladive su s podacima, a one izvan njih slabo su
uskladive pod pretpostavkama postupka. Širina također pokazuje ispunjava li
raspon unaprijed zadani cilj preciznosti, primjerice marginu manju od deset
minuta. Interval za jedan parametar ipak ne govori može li se razlučiti razlika
ili promjena, jer za to treba procijeniti samu razliku i njezinu nesigurnost.
Ne pripisujemo mu ni vjerojatnost da parametar leži unutra niti očekivanje da
će se ponovljeno istraživanje smjestiti unutar istih granica, jer bi ono imalo
vlastiti uzorak i vlastiti interval.

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

### Tiskane postavke za vježbu

Čitatelj tiskanoga izdanja iste dvije usporedbe može provesti bez widgeta.
Sljedeće tri postavke nastale su iz normalne populacije sa sredinom nula i
standardnom devijacijom jedan. Svaka sadrži pedeset intervala iz fiksnoga
simulacijskog niza. Postavke A i B razlikuju se samo po razini pouzdanosti, a A
i C samo po veličini uzorka.

*Slika. Tri fiksne postavke za usporedbu širine i promašaja intervala u tiskanom izdanju. Izrada autora.*

Isti sintetički podaci dostupni su kao pojedinačni zapisi i kao sažetak po
primarnom izvoru vijesti. Sljedeća tablica prikazuje sažetak bez novoga
računanja i bez zaokruživanja pohranjenih vrijednosti. Ona priprema kasniju
provjeru istih rezultata iz pojedinačnih zapisa. Budući da je populacija
sintetička, tablica provjerava postupak i ne iznosi empirijsku tvrdnju o
stvarnim stanovnicima.

*Slika. Brojnici, nazivnici i agregatne vrijednosti za portal u sintetičkoj populaciji. Izrada autora prema javnom agregatnom prikazu sintetičkih podataka.*

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
svojstvo koje se bira i plaća širinom. U ovoj knjizi 95 % služi kao uobičajena
nastavna postavka, a ne kao prirodna granica. Uz svaki interval zato navodimo
razinu na kojoj je izračunat.

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

Nepreklapanje usporedivih intervala može biti snažan dokaz da jednakost nije
dobro uskladiva s podacima pod pretpostavkama postupka. Iz preklapanja ipak ne
slijedi da razlike nema, a ni jedan ni drugi obrazac ne daje vjerojatnost da je
razlika „stvarna”. Ovisnost procjena i istraživački nacrt dodatno određuju kako
se takva slika čita. Pošten odgovor zato traži interval za samu razliku, a ne
dva intervala jedan pokraj drugoga. Taj postupak knjiga uvodi u poglavlju o
usporedbi dviju grupa.

Postoji i druga zamjena koja se često javlja u istom odlomku. Interval
pouzdanosti govori gdje je prosjek, a ne gdje su ljudi. Za naš uzorak od
dvjesto osoba raspon oko sredine dug je
`r hr_broj(s9$gornja - s9$donja, 2)` boda. Ako su pojedinačne ocjene približno
normalno raspoređene, sredina plus ili minus 1,96 uzoračkih standardnih
devijacija daje opisni raspon po normalnom pravilu širok približno
`r hr_broj(2 * s9$normalni_poluraspon, 1)` boda, u kojem bi pod tim modelom
ležalo oko 95 % ocjena. Za izrazito asimetrične, ograničene ili diskretne
raspodjele takav opisni obuhvat ne slijedi. Taj prikaz nije interval predviđanja
za novu osobu, jer ne uključuje nesigurnost procjene središta i raspršenosti
niti određuje iz koje bi populacije buduća osoba došla. Interval za sredinu
odnosi se na parametar i sužava se s većim uzorkom, dok opisni raspon prikazuje
raspršenost pojedinačnih ocjena.

*Slika. Interval pouzdanosti za sredinu i opisni raspon po normalnom pravilu za pojedinačne ocjene na istom uzorku i istoj osi.*

## Bootstrap kao vlastiti izum

Sve dosad počiva na jednoj formuli za standardnu pogrešku, a upotrebljiv
zatvoren račun nije jednako dostupan za svaku mjeru. Za sredinu je jednostavan,
za udio također, dok za medijan, razliku percentila ili omjer može biti
nepraktičan ili tražiti dodatne pretpostavke. Odgovor za slučaj kada takav račun
nemamo može se smisliti bez ijedne nove ideje, uz uvjet da se prethodno
poglavlje shvatilo ozbiljno.

Standardna pogreška bila je definirana kroz ponovljene uzorke iz populacije.
Kad bismo populaciji imali pristup, izvukli bismo tisuću uzoraka, izračunali
tisuću medijana i pogledali koliko se razilaze. Populaciji pristupa nemamo,
imamo samo uzorak. Njegova empirijska raspodjela može privremeno glumiti
populaciju samo ako opažene jedinice razumno predstavljaju ciljnu populaciju.
U jednostavnom bootstrapu redaka pretpostavljamo i da su jedinice neovisne i
međusobno zamjenjive na razini na kojoj su bile uzorkovane. Uparena,
grupirana ili ponovljena opažanja zato se ne rastavljaju na proizvoljne retke,
nego se ponovno uzorkuju cijeli parovi, skupine ili osobe. Pod tim uvjetima
uzorci jednake veličine iz opaženih podataka oponašaju promjene sastava koje
bismo vidjeli pri novom uzorkovanju iz populacije.

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
središnji percentilni raspon od `r hr_broj(s9$boot_donja, 1)` do
`r hr_broj(s9$boot_gornja, 1)` minuta. Poznata populacijska vrijednost od
`r hr_broj(s9$medijan_pop, 1)` minuta u ovom se jednom slučaju nalazi unutar
granica. Slika zato pokazuje konstrukciju raspona iz jednoga uzorka, a ne
njegovu dugoročnu pokrivenost.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću.*

Histogram ima vidljiv stubast oblik jer medijan maloga, zaokruženog uzorka može
poprimiti samo ograničen skup vrijednosti. Ta diskretnost nije računalna
pogreška, ali granice percentilnog raspona čini grubima. Veći broj bootstrap
ponavljanja smanjuje slučajno kolebanje izračunanih percentila, no ne dodaje
nove vrijednosti u siromašan početni uzorak i ne uklanja grube granice ni
nestabilnost koje je mali uzorak već zadao.

Bootstrap ne pretpostavlja imenovani oblik populacijske raspodjele, ali nije
bez pretpostavki. Shema se mora prilagoditi statistici i dizajnu. Kod
korelacije ponovno uzorkujemo cijele parove vrijednosti, kod razlike između
neovisnih skupina svaku skupinu zasebno, a kod ovisnih podataka cijele neovisne
jedinice. Postupak također ne može obnoviti rijetke ili krajnje vrijednosti koje
početni uzorak nije zabilježio. Procjene repova, poput vrlo visokog percentila,
zato su osobito osjetljive na mali uzorak i raspodjele s teškim repovima, dok
je medijan manje ovisan o repovima, ali pri mnogo vezanih vrijednosti i dalje
daje grube granice. Ako uzorak ne predstavlja ciljnu populaciju, bootstrap
precizno ponavlja isti problem umjesto da ga ukloni.

### Kodirani udio i dvije nesigurnosti

Kada je podatak nastao kodiranjem teksta, procijenjeni udio nosi najmanje dva
odvojena izvora nesigurnosti. **Uzoračka nesigurnost** dolazi od toga koji su
tekstovi ušli u korpus ili uzorak. **Nesigurnost kodiranja** dolazi od pravila
po kojem je tekst svrstan, rubnih slučajeva i odluka kodera ili klasifikatora.
Mjerenje može dodati još jedan izvor ako kodirana kategorija samo približno
predstavlja pojam koji istraživanje želi zahvatiti.

Bootstrap redaka s već dodijeljenim oznakama mijenja sastav opaženih tekstova i
zato može prikazati uzoračku komponentu pod pretpostavkom da je jedinica
ponovnog uzorkovanja ispravna. Ne mijenja pravilo kodiranja i ne provjerava
jesu li oznake valjane. Kada bi se rubni tekstovi razvrstali drugim obranjivim
pravilom, procijenjeni udio mogao bi se pomaknuti iako bi bootstrap interval za
svaku od dviju inačica bio uzak. Pošten izvještaj zato uz procjenu i interval
navodi jedinicu teksta, ciljnu populaciju tekstova, postupak odabira i pravilo
kodiranja te izrijekom kaže koju je nesigurnost račun obuhvatio, a koju nije.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživači su studentima i aktivnim
znanstvenicima predočili interval iz zamišljenoga istraživanja i uz njega šest
tvrdnji o njegovu značenju, među kojima nijedna nije bila točna (Hoekstra, 2014).
Velik dio ispitanika u svim skupinama, uključujući iskusne istraživače,
prihvatio je barem neke od njih (Hoekstra, 2014).

Tvrdnje nisu bile besmislene. Upravo ih uvjerljivost čini poučnima. Sve su govorile o
vjerojatnosti da se prava vrijednost nalazi unutar granica, ili o tome koliko
je vjerojatno da bi se ponovljeno istraživanje unutar njih smjestilo. Postupak
koji smo izgradili takva obećanja ne daje, jer se njegov postotak odnosi na
udio intervala koje bi ponovljeno uzorkovanje proizvelo. Nalaz ne pokazuje da
su intervali loš alat nego da je rečenica kojom ih opisujemo teža od računa
koji ih proizvodi.

**Pitajte model.**
Asistent može bootstrapirati mnoge statistike, ali ispravan kod ne jamči
ispravan plan ponovnog uzorkovanja. Provjeravamo predstavlja li početni uzorak
ciljnu populaciju i koja je stvarno neovisna jedinica. Zatim gledamo uzorkuje li
s vraćanjem na punoj veličini uzorka i čuva li parove, skupine ili ponovljena
opažanja. Broj ponavljanja također mora biti dovoljan da računalno kolebanje
granica bude malo. Ključna pogreška koju ovdje provjeravamo nije u kodu nego u
zaključnoj rečenici, gdje se već izračunatom intervalu pripiše vjerojatnost.

> Izračunaj točkastu procjenu i bootstrap interval. Uzorkuj s vraćanjem na
> punoj veličini uzorka, sačuvaj strukturu podataka i interpretiraj razinu
> pouzdanosti kao svojstvo ponovljenog postupka.

**Nađite grešku.**
Za vektor `minute` s jednom vrijednošću po neovisno uzorkovanoj osobi asistent
je vratio kratak račun za bootstrap medijana.

Objasnio je da `replicate` ponavlja postupak, `sample` na punoj veličini uzorka
i s vraćanjem mijenja njegov sastav, `median` u svakom ponavljanju računa istu
mjeru, a `quantile` uzima središnjih 95 % dobivenih vrijednosti. Zatim je
zaključio da postoji devedesetpetpostotna vjerojatnost da se fiksna
populacijska vrijednost nalazi unutar upravo ovog opaženog intervala.

## Razrađeni primjer

Naručitelja istraživanja zanima koliko vremena dnevno stanovnici grada provode
uz medije. Procjena mu je uporabiva samo ako njezina margina nije veća od deset
minuta, a na raspolaganju je uzorak od šezdeset ljudi.

Prvi izbor nije statistički nego opisni. Dnevne minute imaju rep prema velikim
vrijednostima, a poglavlje o sažimanju podataka pokazalo je da prosjek takav
rep povlači za sobom, dok medijan ostaje kod tipičnog ispitanika. Za pitanje o
tome koliko vremena uz medije provodi uobičajena osoba medijan je pošteniji
odgovor. Cijena tog izbora vidi se tek sada, jer za sredinu imamo jednostavan
račun standardne pogreške, dok bi račun za medijan tražio dodatne pretpostavke.
Upravo zato ovaj primjer i postoji.

Cijeli bootstrap stane u istu petlju koju je poglavlje o uzorkovanju već
pokazalo, uz jednu izmjenu. Umjesto iz populacije, izvlačimo iz uzorka, i to s
vraćanjem.

Poziv `sample` uz argument `replace` izvlači s vraćanjem i jedini je novi
element u odnosu na prethodno poglavlje, dok `quantile` odsijeca zadani udio
raspodjele s obje strane. Blok proizvodi upravo one tri brojke koje je odjeljak
o bootstrapu već naveo, jer je riječ o istoj analizi ispisanoj u cijelosti.

Odgovor najprije imenuje populaciju i jedinicu, a tek zatim broj. Za ciljnu
populaciju odraslih stanovnika simuliranoga grada, gdje je jedinica jedna
osoba, medijan dnevnog praćenja medija procjenjujemo na
`r hr_broj(s9$medijan_uzorak, 1)` minuta. Percentilni bootstrap raspon od 95 %
proteže se od `r hr_broj(s9$boot_donja, 1)` do
`r hr_broj(s9$boot_gornja, 1)` minuta i opisuje uzoračku promjenjivost medijana
pod navedenim uvjetima. Raspon je širok gotovo
`r hr_broj(s9$boot_gornja - s9$boot_donja, 0)` minuta, pa njegova margina
iznosi približno
`r hr_broj((s9$boot_gornja - s9$boot_donja) / 2, 0)` minuta. Time unaprijed
zadani cilj od najviše deset minuta nije ispunjen. Poštena je odluka izvijestiti
o stvarnoj širini ili prikupiti dovoljno informacija za precizniju procjenu, a
ne iz ovoga raspona zaključivati o promjeni. Kada odabrane osobe ne bi
predstavljale ciljnu populaciju, populacijska bi se tvrdnja povukla i ostao bi
samo opis uzorka, jer bootstrap tu pogrešku ne uključuje.

Budući da populaciju poznajemo, možemo napraviti i ono što stvarno istraživanje
ne može. Prava vrijednost iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i nalazi
se unutar granica. Taj jedan pogodak ne potvrđuje niti opovrgava percentilni
bootstrap. Deset tisuća ponavljanja iz ranijeg odjeljka provjerava drugi
postupak, normalni interval za sredinu. Pokrivenost raspona za medijan trebalo bi
provjeriti ponavljanjem cijeloga lanca, od novog uzorka od šezdeset osoba do
novoga bootstrap raspona u svakom ponavljanju, pa zatim prebrojiti koliko takvih
raspona obuhvaća populacijski medijan. Takva provjera ovdje nije provedena, pa
primjer pokazuje konstrukciju i ograničenja raspona, a ne dokazuje njegovu
nominalnu pokrivenost.

Redoslijed kojim su tri brojke ispisane isti je onaj kojim se rezultat i
izvještava. Najprije dolazi procjena, jer je ona odgovor na postavljeno pitanje.
Zatim dolazi raspon, jer bez njega procjena tvrdi više nego što zna. Tek na
kraju dolazi ograda, koja ovdje kaže da su podaci simulirani, da je mjera
medijan, a ne prosjek, i da šezdeset ljudi nije mnogo. Ista tri koraka vrijede
za nalaz čija je populacija stvarna, s tom razlikom da se ondje srednji korak
mora izvesti bez izravne provjere prema poznatom parametru u istom istraživanju,
i upravo zato mora biti izveden pažljivo.

## Granica Dijela III — Od procjene do tvrdnje

Šest revizijskih pitanja povezuje vjerojatnost, uzorkovanje i procjenu. Ona
sprječavaju da uzak raspon postane dopuštenje za širu tvrdnju od one koju
podaci i postupak mogu nositi. Na razrađenom primjeru odgovori izgledaju ovako.

| Pitanje revizije | Primjena na bootstrap medijana |
|---|---|
| Što predstavlja jedan redak ili jedno opažanje? | jednu generiranu odraslu osobu s jednim zapisom dnevnih minuta |
| Tko ili što nije moglo ući u ove podatke? | uzorak je slučajno izvučen iz poznate sintetičke populacije, pa ne predstavlja stvarni grad ni osobe izvan te populacije |
| Koja je ciljana količina i vrsta tvrdnje? | populacijski medijan dnevnih minuta, opisan procjenom i rasponom uzoračke nesigurnosti |
| Koji su izvori nesigurnosti obuhvaćeni, a koji ostaju izvan izračuna? | bootstrap mijenja sastav uzorka pod zadanom jedinicom, ali ne provjerava pokrivenost ovoga postupka, mjerenje minuta ni doseg na stvarne stanovnike |
| Koja bi razumna alternativna odluka mogla bitno promijeniti odgovor? | prosjek bi odgovarao na drugo pitanje i jače bi pratio desni rep, a veći uzorak mogao bi dati uži raspon za isti medijan |
| Na koga može utjecati pogrešan zaključak ili odluka? | u ovoj sintetičkoj vježbi nitko stvaran, a u analognoj odluci naručitelj i stanovnici mogli bi dobiti neopravdano preciznu tvrdnju |

: Šest revizijskih pitanja primijenjenih na procjenu iz simulirane populacije. Izrada autora.

Odgovori određuju rečenicu koja se smije prenijeti. Oni ne pretvaraju
sintetičku populaciju u empirijski dokaz, a izostavljenu mjernu nesigurnost ili
nesigurnost kodiranja ne skrivaju unutar uzoračkoga raspona. Karta tvrdnji zato
razdvaja šest mogućih dosega iste analize.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje medijan i raspodjelu minuta u opaženom sintetičkom uzorku |
| povezanost | nije poduprta jer primjer ne uspoređuje dvije varijable |
| generalizacija | usmjerena je na poznatu sintetičku populaciju pod postupkom slučajnoga odabira, bez prava prijenosa na stvarni grad |
| predviđanje | nije poduprto jer nije izgrađeno ni provjereno pravilo za nova opažanja |
| uzročnost | nije poduprta jer nema intervencije ni usporedbe mogućih ishoda |
| odluka | poduprta je odluka da raspon ne ispunjava unaprijed zadanu marginu od najviše deset minuta, ali ne tvrdnja o promjeni ni odluka o medijskoj politici |

: Šest dimenzija tvrdnje na granici Dijela III. Izrada autora.

Samoprovjera na granici dijela obuhvaća četiri povezana pitanja. Zašto pedeset
intervala u widgetu ne mora sadržavati točno pet posto promašaja? Zašto
bootstrap redaka s gotovim oznakama ne uključuje nesigurnost kodiranja? Koje
elemente mora sadržavati poštena rečenica o procjeni i što mora doći prije
brojke? Zašto
podjela već sastavljenih podataka na skupove za učenje i provjeru ne zamjenjuje
vjerojatnosni uzorak za populacijsku generalizaciju?

Kratki račun provjere čini delegirani bootstrap čitljivim i bez pisanja koda.
Svako polje povezuje zahtjev, izlaz i odgovornost s dokazom koji je vidljiv u
ovom poglavlju.

| Polje računa | Bootstrap medijana |
|---|---|
| Što je traženo | procijeniti populacijski medijan dnevnih minuta i njegovu uzoračku nesigurnost iz uzorka neovisnih osoba |
| Što je vraćeno | točkasta procjena te donja i gornja granica središnjega percentilnog raspona |
| Što je provjereno | puna veličina ponovnog uzorka, izvlačenje s vraćanjem, ista statistika u svakom ponavljanju i redoslijed izvještavanja |
| Kako je provjereno | čitanjem poziva `sample`, `median`, `replicate` i `quantile` te usporedbom ispisa s brojkama u prozi |
| Uloga AI-ja | instrument i pogrešiv analitičar |
| Što je ostalo neprovjereno | dugoročna pokrivenost percentilnoga postupka za medijan, reprezentativnost u stvarnom istraživanju i valjanost mjerenja minuta |
| Odgovorna osoba | osoba koja odabire procjenjivanu količinu, provjerava račun i potpisuje zaključak |

: Čitljiv račun provjere za procjenu iz Dijela III. Izrada autora.

## Sažetak

Procjena počinje jednom vrijednošću, ali ne završava njome. Interval pouzdanosti
uzima standardnu pogrešku i oblik koji je dao središnji granični teorem te oko
procjene gradi raspon čije obećanje pripada postupku, a ne pojedinačnom rasponu
koji imamo pred sobom. Preciznost se kupuje podacima, a pouzdanost se bira i
plaća širinom, pa uz svaki raspon mora stajati razina na kojoj je izračunat.
Bootstrap istu ideju oslobađa formule tako što uzorku dopušta da privremeno
glumi populaciju kada uzorak i jedinica ponovnog uzorkovanja odgovaraju ciljnom
načinu uzorkovanja. Time otvara mjere za koje jednostavan račun ne postoji, ali
ne popravlja premalen ili nereprezentativan uzorak niti pogrešno odabranu
jedinicu ponovnog uzorkovanja. Kodirani udio nosi i nesigurnost kodiranja i
nesigurnost mjerenja, koje bootstrap već zadanih oznaka ne obuhvaća. Poštena
rečenica zato imenuje populaciju i jedinicu, navodi procjenu, mjernu jedinicu i
raspon te završava konkretnim ograničenjem koje bi moglo promijeniti zaključak.
Sljedeće poglavlje uzima isti aparat i mijenja mu pitanje, jer umjesto raspona
usklađenog s podacima traži koliko su podaci neobični pod jednom određenom
pretpostavkom.

## Pojmovi

procjena (*estimate*), interval pouzdanosti (*confidence interval*), razina
pouzdanosti (*confidence level*), margina pogreške (*margin of error*),
preciznost (*precision*), bootstrap (*bootstrap*), percentilni raspon
(*percentile interval*), jedinica ponovnog uzorkovanja (*resampling unit*),
nesigurnost kodiranja (*coding uncertainty*)

## Zadaci

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica te zašto bootstrap gotovih oznaka teksta ne
obuhvaća nesigurnost pravila kodiranja. Predajte jedan odlomak.

### Računski

Iz tiskane tablice s trima postavkama izračunajte širinu svakog intervala kao
$2z^*/\sqrt{n}$ i usporedite rezultat s objavljenom širinom i brojem promašaja.
Objasnite što se mijenja između postavki A i B, a što između A i C. Zatim u
alatu iz Dodatka A ili B otvorite analitičku datoteku
`data/populacija-medija.csv`, zabilježite ukupan broj redaka pa izdvojite retke
za koje je `izvor_vijesti_sifra` jednak 1. Reproducirajte broj izdvojenih
redaka, ukupan nazivnik, zbroj `povjerenje_medijima`, udio portala i prosječno
povjerenje među korisnicima portala. Usporedite svih pet rezultata s
agregatnom tablicom u ovom poglavlju i s datotekom
`data/populacija-medija-agregat.csv`.
Predajte račun za tri postavke, pet reproduciranih vrijednosti i jednu rečenicu
o slaganju analitičkog i agregatnog prikaza. Ocjenjuje se rezultat i provjera,
ne pisanje koda.

### Kritički

Vratite se prikazu **Istraživač margine pogreške** u poglavlju o tome kako
brojke zavode. Usporedite stanje s uzorkom od 1000 osoba bez pristranosti i
stanje s jednakim uzorkom te pristranošću od šest postotnih bodova. Oba
pokazuju procjenu od 52 %. Primijenite ondje uvedeni protokol čitanja ankete i
sadašnje znanje o intervalima. Objasnite zašto ista uska margina pogreške ne
može obuhvatiti pristranost odabira, navedite koji je izvor nesigurnosti unutar,
a koji izvan intervala te napišite ispravljenu tvrdnju za pristrano stanje.
Predajte usporedbu dvaju stanja i ispravljenu tvrdnju.

### Revizija modela

Pročitajte modelov račun iz okvira o pogrešci. Za svaki od poziva `replicate`,
`sample`, `median` i `quantile` jednom rečenicom povežite redak koda s pojmom
koji provodi. Zatim izdvojite jedinu pogrešnu rečenicu i napišite
frekventistički ispravnu zamjenu koja zadržava razinu od 95 % i ne uvodi nove
tvrdnje o podacima. Kod ne treba prepisivati ni mijenjati.
