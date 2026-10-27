# DIO III: OD UZORKA DO POPULACIJE

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Vjerojatnost koliko treba

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/07-vjerojatnost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Košarkaši i navijači često govore o vrućoj ruci, uvjerenju da nakon nekoliko
pogodaka raste vjerojatnost sljedećeg. Jedno je istraživanje provjerilo to vjerovanje kroz zapise utakmica i
kontrolirani pokus. Nalazi su protumačeni kao znak da ljudi u slučajnim
nizovima vide obrazac koji ne postoji (Gilovich, 1985).

Prema tom se tumačenju prividni niz uspjeha mogao objasniti slučajnošću
(Gilovich, 1985). Kasnija ponovna analiza, međutim, otkrila je
pristranost u samom načinu mjerenja tog obrasca (Miller, 2018).

Kako procijeniti je li niz posljedica promjene u procesu ili slučajnosti?

Niz pogodaka može izgledati uvjerljivije od raspršenih uspjeha. Da bismo procijenili taj dojam, trebamo najprije upoznati nizove koje proizvodi proces sa stalnim izgledima za uspjeh. Nakon opisivanja
raspodjela i povezanosti trebamo način da odredimo što bismo očekivali pod
jasno zadanim uvjetima. Vjerojatnost će nam omogućiti da opaženi rezultat
usporedimo s drugim rezultatima koje isti model može proizvesti.

Počet ćemo simuliranim bacanjima novčića. Jedno opažanje bit će ishod bacanja,
a nizovi će pokazati kako se udio glava mijenja kada ponavljamo isti postupak.
Budući da sami zadajemo izglede, možemo provjeriti koliko kratki niz odstupa
od onoga što vrijedi za proces. Jednostavan model služi kao polazište za usporedbu. Tvrdnju o ponašanju košarkaša zatim bismo trebali provjeriti na stvarnim sportskim zapisima.

Za pitanja o preklapanju događaja vratit ćemo se simuliranoj populaciji
`populacija_medija`, koristeći dob osobe i njezin glavni izvor vijesti. Tu možemo prebrojiti koliko osoba zadovoljava jedan uvjet, drugi
uvjet ili oba. Tako ćemo provjeriti kada smijemo zbrajati ili množiti
vjerojatnosti i zašto poznavanje jednog obilježja može promijeniti izglede za
drugo. Populacija medijskih navika stvorena je za nastavu, s jednim retkom za jednu zamišljenu osobu, pa njezini obrasci ne opisuju stvarne stanovnike. U hipotetskoj kampanji e-biltena promatrat ćemo otvaranje poruke kao
pokušaj s dvama mogućim ishodima.

Raspodjele koje smo dosad čitali kao opise podataka sada ćemo koristiti i kao
modele mogućih ishoda. Binomna raspodjela opisat će broj uspjeha pod određenim
pretpostavkama, a normalna krivulja otvoriti pitanje kada je zvonasti oblik
opravdan. Uz svaki ćemo račun zadržati uvjete koji ga omogućuju.

Usporedbom izračuna i ponovljenih simulacija iste kampanje utvrdit ćemo
koliko je rezultat neobičan pod zadanim modelom. Taj račun treba razlikovati
od provjere opisuje li model dobro stvarni svijet.

## Što vjerojatnost opisuje

Računalni model svakom bacanju neovisno daje glavu s vjerojatnošću 0,5.
U prvom generiranom nizu početnih pet ishoda, s jedinicom za glavu i nulom
za pismo, glasi `r paste(head(s7_nizovi$glava, 5), collapse = ", ")`.
Nakon petog bacanja imamo `r sum(head(s7_nizovi$glava, 5))` glava od pet,
pa je udio `r hr_broj(s7_nizovi$udio[5], 2)`. Svaka sljedeća točka iste
linije dodaje jedno bacanje i ponovno dijeli dotadašnji broj glava brojem
svih dotadašnjih bacanja. Cijela linija ima 2 000 takvih koraka.

Simulirat ćemo bacanje poštenog novčića i nakon svakog bacanja zabilježiti
udio glava. Ponavljamo postupak triput kako bismo usporedili moguće nizove.
Kratki odsječci mogu izgledati neuravnoteženo i uz isti pošten novčić.

*Slika. Kumulativni udio glava u trima neovisnim nizovima bacanja poštenog novčića. Vodoravna crta označuje vrijednost pola. Izrada autora. Podaci i postupak opisani su u tekstu.*

Nakon dvadeset bacanja udjeli se kreću od `r hr_broj(s7_rani$najmanji, 2)` do `r hr_broj(s7_rani$najveci, 2)`. Nakon dvije
tisuće između `r hr_broj(s7_kasni$najmanji, 3)` i `r hr_broj(s7_kasni$najveci, 3)`. Nizovi su različiti, ali su u duljim
nizovima njihovi udjeli bliži polovini. Sam kratki neuravnotežen niz zato nije
dovoljan da novčić proglasimo nepoštenim.

**Vjerojatnost** je broj od nule do jedinice koji događaju pridružuje
razinu neizvjesnosti unutar jasno opisanoga modela, pri čemu veći broj označuje
veće izglede za taj događaj.

Model može opisivati ponovljiv postupak ili jedinstven događaj. Za ponovljiv
postupak vjerojatnost uspoređujemo s učestalošću kroz mnogo ponavljanja. Za
jedinstven događaj, poput uspjeha reprezentacije na sljedećem prvenstvu, broj
opisuje neizvjesnost uz dostupne informacije. U oba slučaja trebamo znati
odakle procjena dolazi.

Zakon velikih brojeva opisuje približavanje relativne učestalosti
vjerojatnosti kada raste broj neovisnih ponavljanja sa stabilnom
vjerojatnošću.

Svako neovisno bacanje zadržava iste izglede. Približavanje udjela polovini objašnjavamo rastom nazivnika. Kako niz raste, početna neravnoteža čini sve manji dio ukupnog broja bacanja. Kasniji ishodi pritom nastaju po istom pravilu kao raniji.

Očekivanje da nakon četiri glave pošten novčić duguje pismo nazivamo
kockarskom zabludom. U modelu neovisnih bacanja niz glava ne povećava ni
izglede za novu glavu. Kod košarke je pitanje drukčije jer se mogu mijenjati
forma, težina šuta, obrana ili odabir pokušaja. Fiksna neovisna vjerojatnost
služi nam kao polazni model za usporedbu, bez pretpostavke da potpuno opisuje
igru.

Razlikujemo modelnu vjerojatnost, opaženu učestalost i osobnu sigurnost.
Modelna vjerojatnost proizlazi iz pretpostavki i informacija. Učestalošću kroz
ponavljanja možemo provjeravati model. Za osobno uvjerenje izraženo postotkom tek treba pokazati na čemu se temelji i kako se slaže s ishodima.

**Kalibrirana nesigurnost** znači da se prognozirani izgledi slažu s
učestalostima u mnogo usporedivih prognoza. Među događajima kojima smo
pripisali sedamdeset posto izgleda, približno sedamdeset posto trebalo bi se
ostvariti. Za pojedinu prognozu navodimo njezine informacije i pretpostavke.
Ocjena kalibracije stoga zahtijeva niz usporedivih prognoza i njihovih ishoda.

## Tri pravila i jedna pretpostavka

Da bismo iz poznatih vjerojatnosti dobili novu, najprije razjašnjavamo koje
ishode ubrajamo u događaj koji nas zanima. Vjerojatnost da se taj događaj ne
dogodi dobivamo oduzimanjem njegove vjerojatnosti od jedan. To je pravilo
komplementa. Kada povezujemo
dva događaja
riječju „ili”, njihove vjerojatnosti zbrajamo, ali eventualni preklop oduzimamo
kako iste ishode ne bismo prebrojili dvaput. Za zajedničko nastupanje množimo
vjerojatnost prvog događaja uvjetnom vjerojatnošću drugog. Tek kada saznanje o
prvome ne mijenja izglede drugoga, događaji su neovisni i možemo izravno
pomnožiti njihove pojedinačne vjerojatnosti. Na izboru izvora vijesti vidjet
ćemo zašto je taj uvjet važan.

Brojnosti u tablici omogućuju da nazivnike provjerimo prije računanja
postotaka. Retci razlikuju dob do 29 godina od ostalih, a stupci glavni
izvor vijesti u poznatoj simuliranoj populaciji.

*Slika. Dob i glavni izvor vijesti u simuliranoj populaciji. Izrada autora.*

U simuliranoj populaciji `populacija_medija` portal bira `r hr_broj(s7$p_portal)` % ljudi, a do
dvadeset devet godina ima ih `r hr_broj(s7$p_mlad)` %. Zbrajanjem dobivamo
`r hr_broj(s7$p_zbroj)` %. No udio ljudi koji su mladi ili biraju portal jest `r hr_broj(s7$p_portal_ili_mlad)` %.
Razlika nastaje jer je `r hr_broj(s7$p_portal_i_mlad)` % ljudi istodobno mlado i bira portal, pa smo
ih u zbroju računali dvaput.

Za pojednostavnjeno pravilo množenja trebamo opravdati neovisnost.

**Neovisnost** dvaju događaja znači da saznanje o tome je li se jedan dogodio
ne mijenja vjerojatnost drugoga.

Koristimo potpuno poznatu simuliranu populaciju od pedeset tisuća odraslih
osoba. Društvene mreže kao glavni izvor vijesti bira `r hr_broj(s7$p_mreze)` %, a do
dvadeset devet godina ima `r hr_broj(s7$p_mlad)` % ljudi. Uz neovisnost bismo množenjem
dobili `r hr_broj(s7$p_umnozak)` % ljudi koji zadovoljavaju oba uvjeta. U generiranim podacima
taj je udio `r hr_broj(s7$p_oboje)` %, znatno veći.

Množenje je točno, ali pretpostavka neovisnosti ovdje ne vrijedi. Nju treba
opravdati načinom nastanka podataka i dizajnom. Podaci mogu pokazati
odstupanje od neovisnosti, dok odsutnost uočljive razlike sama ne potvrđuje
pretpostavku. U ovom skupu trebamo razlikovati udio u cijeloj populaciji od
udjela unutar određene skupine.

**Uvjetna vjerojatnost** je vjerojatnost događaja izračunata unutar skupine u
kojoj je neki drugi događaj već nastupio.

Među mlađima od trideset godina mreže bira `r hr_broj(s7$p_mreze_mlad)` %, a među ostalima
`r hr_broj(s7$p_mreze_ostali)` %. Televiziju bira `r hr_broj(s7$p_tv)` % cijele populacije i `r hr_broj(s7$p_tv_stariji)` % onih
od šezdeset godina naviše. Ukupne i uvjetne vrijednosti razlikuju se jer su
dob i izbor izvora povezani.

Uvjetna vjerojatnost ovisi o smjeru pitanja. Udio upozorenja među ciljanim
zapisima računa se s drugim nazivnikom od udjela ciljanih zapisa među
upozorenjima. Taj smo problem susreli u poglavlju o zavaravanju brojkama. Za
drugi smjer trebamo i temeljnu stopu te stopu pogrešnih upozorenja.

Udio konverzija među ljudima koji su kliknuli oglas ili udio otvaranja među
poslanim porukama također su uvjetne vjerojatnosti. Vrijede za skupinu iz
svojeg nazivnika. Pri usporedbi segmenata zato svaki put jasno određujemo na
koga se udio odnosi.

## Ponovljeni pokušaji s dva ishoda

Pravila za pojedine događaje možemo povezati kada se isti pokušaj ponavlja.
Često pratimo unaprijed zadan broj pokušaja s dvama ishodima. Zanima nas,
primjerice, koliko je ljudi kliknulo, odgovorilo na poziv ili otvorilo poruku.
Za takve situacije možemo razmotriti binomni model.

**Binomna raspodjela** opisuje broj uspjeha u zadanom broju pokušaja kad svaki
pokušaj ima samo dva ishoda, jednaku vjerojatnost uspjeha i nikakvu vezu s
ostalim pokušajima.

U hipotetskom modelu promatramo dvadeset objava. Svaka ima zadanu vjerojatnost
od dva posto da u sedam dana prijeđe dogovoreni prag dijeljenja. Prag,
razdoblje i broj izloženih korisnika dio su definicije viralnosti.
Vjerojatnost smo zadali kao pretpostavku modela. Prema binomnom modelu,
nijedna objava ne bi prešla prag u `r hr_broj(s7$nijedna)` % takvih zamišljenih mjeseci.
Time opisujemo ponavljanja modela, bez jamstva za određeni mjesec.

Za pojedinu objavu izostanak viralnosti ima vjerojatnost $1-0,02=0,98$.
Uz neovisnost dvadeset takvih izostanaka množimo, pa je vjerojatnost
nijedne viralne objave $0,98^{20}$. Za barem jednu koristimo suprotni
događaj i računamo $1-0,98^{20}$, odnosno
`r hr_broj(100 * (1 - 0.98^20), 1)` %.

Prije primjene provjeravamo uvjete. Različit doseg objava može značiti
različite vjerojatnosti uspjeha. Ako jedno dijeljenje povećava vidljivost
sljedeće objave, pokušaji nisu neovisni. Slično, odgovori dviju osoba iz istog kućanstva mogu biti povezani zbog zajedničkih okolnosti, premda ih zapisujemo u zasebne retke.

Kada uvjeti vrijede, očekivani broj uspjeha jednak je broju pokušaja
pomnoženom vjerojatnošću uspjeha. S više pokušaja raste raspršenost broja
uspjeha, ali sporije od samog broja pokušaja. Udio uspjeha zato postaje
stabilniji. Veći raspon ukupnog broja ne znači nužno i nestabilniji udio.

Model pojednostavnjuje proces i jasno određuje što može nastati slučajno. Tako
stvarni rezultat imamo s čime usporediti.

## Interakcija — Simulator novčića i kampanje

Sada jednu vrijednost dobivamo tek nakon cijeloga niza. Ako u mogućem
nizu od 20 pokušaja dobijemo šest uspjeha, u histogram unosimo jedan udio
$6/20 = 0,30$. Taj smo niz odabrali radi ilustracije računa.
Za svaki histogram ponavljamo cijele neovisne nizove, a vjerojatnost uspjeha
zadržavamo. Visina stupca broji nizove čiji su udjeli u istom rasponu.

Prikaz uspoređuje ishode ponovljenih nizova uz istu zadanu
vjerojatnost. Duljina niza mijenja raspon simuliranih udjela. Kratki
nizovi daju raspršenije rezultate iako postupak koji ih stvara ostaje isti.
U tiskanom prikazu vjerojatnost uspjeha iznosi 0,30, a za svaku duljinu
ponavljamo cijeli niz 2 000 puta.

*Slika. Raspodjela stopa uspjeha kroz mnoge deterministički simulirane nizove. Okomita crta označuje zadanu vjerojatnost modela.*

**Što isprobati.**

1. Postavite pošten novčić i dvadeset pokušaja pa opišite raspon simuliranih udjela glava.
2. Povećajte niz na dvjesto pokušaja bez promjene vjerojatnosti.
3. Prebacite scenarij na kampanju i postavite zadanu stopu uspjeha na trideset posto.
4. Usporedite jednu krajnju simuliranu stopu s cijelom raspodjelom ponovljenih kampanja.

Rezultat jedne kampanje uspoređujemo s cijelom raspodjelom koju proizvodi isti
postupak. Ako je raspodjela široka, jedan ishod teže razlikuje moguća
objašnjenja. Ishod daleko u repu može dovesti model u pitanje, ali ne govori
sam što je uzrok odstupanja.

Uži histogram duljih nizova pokazuje promjenu raspršenosti. Za opis njegova
oblika vratit ćemo se standardiziranoj ljestvici iz poglavlja o sažimanju
podataka. Na njoj nula označuje sredinu, a jedan i minus jedan položaje po
jednu standardnu devijaciju iznad i ispod nje. Taj će nam poznati način
opisivanja položaja pomoći da raspodjelu usporedimo sa zvonastom krivuljom.

## Zvonasta krivulja i njezino područje

Raspodjela mnogih ponovljenih udjela može poprimiti približno simetričan oblik
s najviše vrijednosti oko sredine. Taj zvonasti oblik susrećemo u normalnoj
raspodjeli.

**Normalna raspodjela** je simetrična zvonasta raspodjela koju u cijelosti
određuju njezino središte i njezina standardna devijacija.

Na nacrtanoj normalnoj krivulji udaljenost mjerimo standardnim devijacijama.
Okomite granice omeđuju srednjih približno 68 %, 95 % i 99,7 % površine.
Površina predstavlja udio mogućih vrijednosti, a visina krivulje gustoću.

*Slika. Pravilo 68–95–99,7 za standardnu normalnu raspodjelu. Izrada autora iz matematičkog modela.*

Standardizirana vrijednost određuje položaj na krivulji. Nula je sredina,
pozitivan predznak označuje vrijednost iznad nje, a negativan ispod. Apsolutna
vrijednost govori koliko je standardnih devijacija udaljena od sredine. Na
normalnoj krivulji taj položaj možemo povezati s udjelom površine.

Svaki simulirani udio prosjek je nula za neuspjehe i jedinica za uspjehe u
jednom nizu. Histogram stoga prikazuje raspodjelu udjela iz ponovljenih nizova. Jedna vrijednost u njemu sažima cijeli niz pojedinačnih nula i jedinica.

U našoj simulaciji pokušaji slijede isto stabilno pravilo i međusobno su
neovisni. S duljim nizovima udjeli se manje rasipaju i njihov se histogram
približava zvonastom obliku. Pojedinačni ishodi i dalje ostaju nule ili
jedinice. Razlog tom obrascu i uvjete pod kojima vrijedi razradit ćemo u
poglavlju o uzorkovanju, uz središnji granični teorem.

Sredina i standardna devijacija potpuno određuju položaj i širinu normalne
raspodjele. Unutar jedne standardne devijacije od sredine leži oko 68 %
vrijednosti, unutar dvije oko 95 %, a unutar tri oko 99,7 %.

S raspodjele prosjeka sada prelazimo na pojedinačne vrijednosti u istoj populaciji `populacija_medija`. Njihov oblik trebamo zasebno provjeriti. Pogledat ćemo dnevno vrijeme uz medije i iznos koji je osoba spremna platiti za sadržaj.

*Slika. Dnevne minute uz medije i spremnost na plaćanje u simuliranoj populaciji, s isprekidanim crtama na jednoj i dvjema standardnim devijacijama od sredine. Izrada autora. Podaci i postupak opisani su u tekstu.*

Za dnevne minute unutar jedne standardne devijacije nalazi se `r hr_broj(s7_podrucja$minute[1])` %
populacije, unutar dviju `r hr_broj(s7_podrucja$minute[2])` %, a unutar triju `r hr_broj(s7_podrucja$minute[3])` %. Te su
vrijednosti blizu normalnom pravilu. Blaga asimetrija udesno stvara manja
odstupanja.

Za spremnost na plaćanje odstupanja su mnogo veća. Unutar jedne devijacije
nalazi se `r hr_broj(s7_podrucja$iznos[1])` %, a unutar triju `r hr_broj(s7_podrucja$iznos[3])` % populacije. Graf pokazuje da
`r hr_broj(s7$bez_platnika)` % ljudi navodi nulu, uz dugi rep prema velikim iznosima. Jedna
devijacija ispod sredine već daje negativan iznos, pa ispod te granice nema
opažanja. Normalna raspodjela ne opisuje dobro te sirove vrijednosti.

Promjena ljestvice zahtijeva dva odvojena koraka. Iz istih 50 000 zapisa
prvo izdvajamo `r sum(s7_iznos > 0)` pozitivnih iznosa, a zatim na njih
primjenjujemo prirodni logaritam. Primjerice, za prvi pozitivan iznos od
`r hr_broj(s7_iznos[s7_iznos > 0][1], 1)` eura nova vrijednost iznosi
`r hr_broj(s7_log_iznos[1], 3)`. Nule nemaju konačan logaritam i nisu dio
toga izračuna. Nazivnik svakoga sljedećeg udjela zato su samo platitelji.

Ako izdvojimo osobe spremne nešto platiti i logaritmiramo njihove iznose,
oblik postaje bliži zvonastom. Unutar odgovarajućih raspona sada je `r hr_broj(s7_podrucja$log_iznos[1])`
%, `r hr_broj(s7_podrucja$log_iznos[2])` % i `r hr_broj(s7_podrucja$log_iznos[3])` %. Izdvajanjem smo, međutim, promijenili
populaciju, a logaritmiranjem ljestvicu. Bolje slaganje s normalnom
raspodjelom samo po sebi ne opravdava izostavljanje neplatitelja.

## Kad podaci ne pristaju krivulji

Za sljedeći prikaz uzimamo po 1 200 vrijednosti iz svakoga od triju
prethodno opisanih skupova. Svaki panel ima zaseban slučajni odabir bez
vraćanja, pa se točke ne odnose nužno na iste osobe. Poredak unutar panela
omogućuje usporedbu oblika raspodjele.

Postotci unutar raspona mogu sakriti mjesto odstupanja. QQ prikaz zato poreda
opažene vrijednosti i usporedi ih s vrijednostima koje bismo na istim
položajima očekivali iz normalne raspodjele. Ako se oblici podudaraju, točke
prate pravac. Vodoravna os prikazuje kvantile standardne normalne raspodjele,
a okomita poredane vrijednosti u jedinicama promatrane varijable. Referentni
pravac ovdje prolazi kroz parove prvoga i trećega kvartila. Odstupanja od
njega pokazuju gdje oblik podataka odstupa od normalnoga oblika.

*Slika. Poredane vrijednosti triju varijabli nasuprot kvantilima standardne normalne raspodjele. Referentni pravac određen je prvim i trećim kvartilom. Izrada autora. Podaci i postupak opisani su u tekstu.*

Dnevne minute uglavnom prate pravac, uz odizanje desnog kraja zbog repa prema
višim vrijednostima. Za spremnost na plaćanje točke najprije stoje vodoravno
zbog nula, a zatim skreću prema gore. Nakon izdvajanja platitelja i
logaritmiranja iznosa opet su blizu pravca.

QQ prikaz pokazuje gdje podaci odstupaju od pretpostavke. Prikladnost analize procjenjujemo prema tome koliko su ta odstupanja važna za odabrani postupak. Posljedice blagog odstupanja u repu ovise o
ciljnoj veličini, postupku i utjecajnim opažanjima. Velika skupina nula jasno
pokazuje da normalna raspodjela nije dobar opis sirovih iznosa.

Poznata vjerojatnost i učenje o nepoznatoj stopi različita su pitanja.
Ako smo sami zadali pošten novčić, pet glava ne mijenja sljedeću
vjerojatnost 0,5. Ako ne znamo udio uspješnih objava, pet uspjeha postaje
informacija za njegovu procjenu. Tada nesigurnost proizlazi i iz toga što
pravilo nastanka podataka tek trebamo naučiti.

## Nizovi koje slučajnost proizvodi

Usporedbom s normalnom krivuljom provjeravali smo odgovara li model obliku
podataka. U pitanju o vrućoj ruci trebamo provjeriti i način na koji iz niza
biramo opažanja. **Slučajni niz** nastaje procesom sa slučajnom sastavnicom i ne mora u kratkom
odsječku izgledati pravilno. Za provjeru vruće ruke simuliramo neovisne
pokušaje s fiksnom vjerojatnošću pogotka, kao kod poštenog novčića. Ne
pretpostavljamo da je stvarna košarka takva. Iz svakog niza izdvajamo pokušaje
neposredno nakon triju pogodaka. Želimo vidjeti mijenja li samo to pravilo
odabira prosječan udio pogodaka među izdvojenim pokušajima.

Pravilo odabira možemo vidjeti na namjerno složenom nizu
1, 1, 1, 0, 1, 1, 1, 1. Nakon triju jedinica stoje četvrti i osmi pokušaj,
s ishodima 0 i 1. Udio na odabranim mjestima zato je $1/2$, iako u cijelom
nizu ima sedam jedinica od osam. Posljednja tri pogotka ne stvaraju dodatno
opažanje jer deveti pokušaj ne postoji. U simulaciji umjesto ovoga
ilustrativnog niza svaki put generiramo novi niz neovisnih pokušaja s
vjerojatnošću 0,5.

Za svaku kombinaciju duljine i uvjeta generiramo 8 000 nizova. Najprije
računamo udio odabranih pogodaka unutar svakog niza, a zatim prosjek tih
udjela, dajući svakom uključenom nizu jednaku težinu. Niz bez ijednog
prikladnog mjesta nema definiran udio i izostavljamo ga iz toga prosjeka.
U stupcima „Bez mjesta” prikazujemo koliko je takvih nizova, pa je
nazivnik prosjeka 8 000 umanjeno za taj broj.

*Slika. Prosječan udio pogodaka na pokušajima koji slijede zadani niz pogodaka, u simulaciji poštenog novčića bez ikakve memorije. Izrada autora.*

U nizovima od stotinu pokušaja taj prosječni udio iznosi `r hr_broj(s7$nakon_tri_100, 3)`, a u
nizovima od dvadeset `r hr_broj(s7$nakon_tri_20, 3)`. Oba su ispod polovine, iako smo simulirali
proces bez memorije. Odstupanje stvara odabir mjesta i računanje udjela po
konačnim nizovima.

Mehanizam se vidi već u trima bacanjima, kada tražimo ishod nakon jedne
jedinice. Od osam jednako vjerojatnih nizova šest ima takvo mjesto.
To su 010, 011, 100, 101, 110 i 111. Njihovi udjeli uspjeha na odabranim
mjestima redom su 0, 1, 0, 0, 1/2 i 1. Prosjek tih šest udjela iznosi
5/12, približno 0,417. Nizovi s jednim i dvama odabranim mjestima dobivaju
jednaku težinu. Takvo pridavanje težina spušta prosjek ispod 1/2 uz stalne izglede pri svakom bacanju.
Pristranost je veća u kraćim nizovima i uz dulji uvjet. Nakon samo jednog
pogotka u nizovima od stotinu pokušaja prosječni udio je `r hr_broj(s7$nakon_jednog_100, 3)`, blizu
polovine.

Za niz od stotinu pokušaja odstupanje je oko četiri postotna boda. Takav je
pomak usporediv s razlikom koju bi istraživač mogao tražiti kao dokaz promjene
forme. Zato treba provjeriti koliki dio rezultata nastaje samim postupkom
mjerenja.

Kada iz podataka odabiremo jedinice prema obilježjima tih istih podataka,
pravilo odabira postaje dio analize. Njegov učinak možemo provjeriti na procesu čije je pravilo poznato, ali tada
moramo simulirati i odabir jedinica i završni izračun.

**Statistika u divljini.**
**Vruća ruka i njezin ispravak.** Kada igrač nekoliko puta uzastopno
pogodi, suigrač bi mu mogao ponovno dodati loptu jer očekuje nastavak
niza. To je moguća odluka kojoj pitanje o vrućoj ruci daje smisao.
Zanima nas govori li prethodni uspjeh nešto o sljedećem pokušaju ili
promatramo niz kakav može nastati i bez promjene vjerojatnosti pogotka.

Izvorno istraživanje vruće ruke ponudilo je tumačenje da ljudi u
nizovima vide promjenu koje nema (Gilovich, 1985). Za provjeru takve tvrdnje naizgled je
dovoljno izdvojiti pokušaje nakon pogodaka i usporediti njihovu uspješnost s uspješnošću pokušaja nakon promašaja. No izdvajanjem
mjesta unutar konačnih nizova već smo uveli postupak odabira koji
može promijeniti očekivani rezultat.

Kasnija metodološka analiza pokazala je da je uobičajena mjera
ovisnosti osjetljiva na tu pristranost odabira. Nakon ispravka, ponovna
analiza izvornog kontroliranog pokusa dala je zaključak u prilog vrućoj
ruci (Miller, 2018). Promijenio se referentni račun s kojim se uspoređuje
opaženi niz.

Naša simulacija pokazuje kako postupak odabira i prosječenja proizvodi pomak
iako se zadana vjerojatnost ne mijenja. Prije tumačenja stvarnih pokušaja
zato treba provjeriti cijeli postupak na procesu čije je pravilo poznato.
Tako znamo koliki pomak mogu proizvesti sam odabir i računanje.

Odluka na terenu traži dodatnu prosudbu. Uz moguću promjenu forme treba razmotriti težinu sljedećeg šuta, obranu i raspoložive suigrače. Zato provjeravamo i dojam o vrućoj ruci i mjerni postupak kojim ga
pokušavamo osporiti.

Za planiranje kampanje zanima nas barem jedna objava koja prijeđe prag.
Provjerimo koje informacije taj račun traži uz vjerojatnost jedne objave.

**Nađite grešku.**
U nastavnom modelu svakoj objavi zadajemo vjerojatnost od dva posto
da u sedam dana prijeđe dogovoreni prag dijeljenja. To je pretpostavka
vježbe, a ne izmjeren udio. Urednik pita kolika je vjerojatnost da barem
jedna od pet objava iste kampanje prijeđe prag.

U opisu kampanje piše da objave mogu doći do istih pratitelja i da se
dijele tijekom istog tjedna. Nema podataka o tome pojavljuju li se
njihovi uspjesi zajedno. Asistent je predložio račun komplementom.

> Za jednu objavu vjerojatnost ostanka ispod praga iznosi 0,98.
> Za svih pet ona iznosi 0,98 na petu potenciju, pa komplement daje
> približno 9,6 %. Budući da je svaka objava zasebna jedinica,
> taj broj možemo upotrijebiti kao vjerojatnost uspjeha kampanje.

Napišite uredniku može li broj preuzeti bez dodatnog uvjeta. U odgovoru
zadržite valjan račun, imenujte pretpostavku koju traži jedan njegov
korak i navedite koju bi informaciju o objavama trebalo pribaviti.
Ne morate izračunati novu vjerojatnost ako podaci za nju nisu zadani.

## Razrađeni primjer

Zamislimo da je e-bilten poslan na pedeset adresa i otvoren četrnaest puta.
Zadajemo hipotetski model s poznatom vjerojatnošću otvaranja od dvadeset dva
posto za svaku poruku i neovisnim otvaranjima. Koliko je pod tim modelom
vjerojatno četrnaest ili više otvaranja? Rezultat ćemo izračunati binomnom
raspodjelom i provjeriti kroz dvadeset tisuća simuliranih kampanja. Primjer
nije mjerenje stvarne kampanje. Za traženu vjerojatnost koristimo već poznato
pravilo komplementa. Od svih mogućih ishoda izostavit ćemo one s najviše
trinaest otvaranja, pa ostaju četrnaest ili više.

Jedna simulirana kampanja sadrži 50 neovisnih odgovora „otvoreno” ili
„nije otvoreno”, s istih 22 % izgleda za svaku poruku. Njihov zbroj daje
broj otvaranja jedne kampanje. Prvih pet generiranih zbrojeva iznosi
`r paste(s7_kampanje[1:5], collapse = ", ")`. Svaki uspoređujemo s 14,
a među svih 20 000 kampanja taj prag doseže njih
`r sum(s7_kampanje >= 14)`. Dijeljenjem s 20 000 dobit ćemo simuliranu
vjerojatnost. Sva ponavljanja imaju definiran rezultat i ulaze u nazivnik.

Poziv `pbinom` provodi prvi dio tog računa, zbraja vjerojatnosti od nula
do trinaest otvaranja. Oduzimanje od jedan ostavlja traženi dio raspodjele.
Poziv `rbinom` zatim simulira kampanje prema istim pretpostavkama. Udio
kampanja s najmanje četrnaest otvaranja trebao bi biti blizu izračunatoj
vjerojatnosti, pa možemo usporediti računski rezultat s ponavljanjem postupka.

Izračun daje `r hr_broj(s7$tocno)` %, a simulacija `r hr_broj(s7$simulirano)` %. Razlikuju se malo jer smo
simulirali konačan broj kampanja. Podudaranje provjerava račun u zadanom
modelu, bez neovisne potvrde modela u stvarnosti.

Četrnaest ili više otvaranja nastalo bi otprilike u jednom od pet ponavljanja.
Ishod zato nije posebno neobičan pod modelom, ali to ne potvrđuje sve njegove
pretpostavke. Ni mnogo rjeđi ishod sam ne bi dokazao učinak naslova jer bi
publika, vrijeme slanja i doseg ostali moguća objašnjenja. Za učinak naslova
trebali bismo usporediti nasumično dodijeljene inačice. Za uredničku odluku uz
to trebamo cilj i troškove pogreške.

Izračunali smo vjerojatnost ishoda u jednom repu raspodjele pod izričitim
modelom.

## Sažetak

Vjerojatnost nam omogućuje da opaženi rezultat usporedimo s ishodima koje
proizvodi jasno zadan model, a kalibraciju prognoza provjeravamo kroz mnogo
usporedivih predviđanja. Prije zbrajanja i množenja određujemo događaje,
njihove preklape i uvjete, kao što binomni model traži neovisne binarne
pokušaje s jednakom vjerojatnošću. Ponavljanjem vidimo i zašto raspodjela
prosjeka pod uvjetima središnjega graničnog teorema može postati približno
normalna, iako pojedinačni podaci to nisu. Pravilo o 68, 95 i 99,7 %
primjenjujemo na onu raspodjelu koja je doista približno normalna. Simulacija
vruće ruke pokazala je da u provjeru treba uključiti i pravilo odabira, jer i
ono može promijeniti rezultat. U poglavlju o uzorkovanju istim ćemo
ponavljanjem proučiti procjene iz različitih uzoraka.

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

Vratite se na hipotetsku provjeru zapisa iz poglavlja o tome kako brojke
zavode. Od 10 000 zapisa njih 100 stvorio je program. Provjera označuje 90 od
tih 100 i pogrešno označuje 495 od preostalih 9 900. Na tvrdnju da je provjera
pouzdana jer pronalazi devedeset posto ciljanih zapisa primijenite svih šest
revizijskih pitanja. Iz navedenih brojnosti izračunajte udio upozorenja među
ciljanim zapisima, udio ciljanih zapisa među svim upozorenjima i temeljnu
stopu. Predajte kratku revizijsku tablicu, račun i dvije rečenice o tome što
rezultati dopuštaju zaključiti.

Vraćamo se hipotetskom modelu dvadeset neovisnih objava, od kojih svaka ima
vjerojatnost uspjeha 0,02. Najprije izračunajte vjerojatnost da nijedna ne
uspije, a zatim pravilom komplementa vjerojatnost barem jednoga uspjeha.
Navedite zašto isti račun nije opravdan ako uspjeh jedne objave mijenja
vjerojatnost uspjeha sljedeće.

### Kritički

Prosudite kako je nalaz o vrućoj ruci prešao put od mjerenja do općenite tvrdnje
o ljudskoj procjeni slučajnosti, i što se u toj tvrdnji promijenilo nakon
ispravka mjere (Gilovich, 1985; Miller, 2018). Predajte jedan odlomak i imenujte
rečenicu koju bi popularni prikaz smio zadržati.

### Revizija modela

Provjerite analizu iz okvira. Izdvojite ispravne računske korake i
označite račun koji vrijedi samo uz neovisnost. Zatim izdvojite rečenicu koja
neovisnost neopravdano smatra potvrđenom. Napišite zamjenu koja jasno ograničava zaključak.

---

# Uzorkovanje

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/08-uzorkovanje.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Kad uz internetsku anketu vidimo velik broj odgovora, lako joj pripišemo
veću uvjerljivost. Zamislimo dvije prognoze istih izbora, jednu s nekoliko
stotina sudionika i drugu s milijunima. Prije nego što pročitamo kako su
prikupljene, koja nam ulijeva više povjerenja?

Časopis *Literary Digest* pred američke predsjedničke izbore 1936. poslao
je milijune probnih listića i iz vraćenih odgovora predvidio pobjedu Alfa
Landona. Pobijedio je Franklin Roosevelt (Squire, 1988). Pogrešna prognoza
imala je iza sebe golemu količinu odgovora stvarnih ljudi.

Kako toliki broj odgovora može promašiti čak i pobjednika, a znatno manji
uzorak ipak pružiti korisnu procjenu?

Da bismo razumjeli taj promašaj, trebamo odvojiti dvije stvari. Jedna je
koliko bi se rezultat mijenjao pri ponavljanju odabira, a druga kamo nas
sam postupak odabira sustavno usmjerava. Slučajnost iz prethodnog poglavlja sada ulazi u sam odabir ljudi koje
promatramo. Ako iz iste populacije uzmemo drugi uzorak, promijenit će se
sastav sudionika, a s njime i izračunati prosjek. Uz razlike među ljudima sada istražujemo koliko bi se mijenjao naš odgovor na istraživačko pitanje kada bismo odabir mogli ponavljati.

Za tu ćemo provjeru iskoristiti prednost nastavne simulacije. Skup
`populacija_medija` sadrži 50.000 računalno stvorenih odraslih osoba i
omogućuje nam da poznajemo cijelu populaciju. Jedan redak
predstavlja jednu osobu, a pratit ćemo povjerenje u medije, dnevno praćenje
medija, izvor vijesti i spremnost na plaćanje. To je ista zamišljena
populacija kojom smo se već služili, odvojena od manje ankete `anketa_mreze`.
Iz nje možemo izvlačiti uzorke i njihove rezultate uspoređivati s poznatom
ciljnom vrijednošću. Ti zapisi ne opisuju stvarne stanovnike. U stvarnom istraživanju ciljnu vrijednost obično ne vidimo.

Ponavljanjem odabira dobit ćemo raspodjelu uzoračkih rezultata, čije ćemo
središte i širinu opisati sredinom i standardnom devijacijom. Standardnu
pogrešku procjene pritom ćemo razlikovati od raspršenosti pojedinačnih
odgovora. Mijenjanjem veličine uzorka i oblika populacije ispitat ćemo kada
raspodjela sredina postaje približno zvonasta i zašto se njezina širina
smanjuje sporije nego što raste broj sudionika.

Ta promjenjivost samo je dio problema ankete. Vratit ćemo se okviru
uzorkovanja, odazivu i istraživačkom nacrtu iz poglavlja o mjerenju te
provjeriti što veći uzorak može popraviti, a što ostaje izvan računa. Ista
pitanja postavit ćemo i izboru tekstova u korpus. Pri procjeni uvjerljivosti
istraživanja moći ćemo razlikovati slučajnu nesigurnost od sustavnog
izostavljanja jedinica. Za to najprije trebamo jasno odvojiti populaciju koju
želimo opisati od uzorka koji nam je dostupan.

## Populacija, uzorak i pogreška uzorkovanja

**Populacija** je skup jedinica o kojima želimo zaključivati, a **uzorak** dio
koji smo promatrali. Postupak odabira povezuje ih tako što određuje koje
populacijske jedinice mogu ući u uzorak i s kojim izgledima.

**Parametar** je vrijednost koja opisuje populaciju. Populacijsku sredinu
označujemo s $\mu$, a standardnu devijaciju s $\sigma$. **Statistika** je
vrijednost izračunata iz uzorka, primjerice sredina $\bar{x}$ ili standardna
devijacija $s$. Veličine uzorka i populacije označujemo s $n$ i $N$.
Statistiku koristimo za procjenu parametra, uz očekivanje da se mogu
razlikovati.

Prije izvlačenja uzoraka izračunajmo parametre cijele `populacija_medija`.
Te će nam vrijednosti služiti kao cilj s kojim uspoređujemo svaku uzoračku
procjenu.

Prosječno povjerenje u medije je `r hr_broj(s8$mu, 2)` na ljestvici od 1 do
10, uz standardnu devijaciju `r hr_broj(s8$sigma, 2)`. Prosječno dnevno
praćenje medija iznosi `r hr_broj(s8$mu_minuta, 1)` minuta, a portal kao
glavni izvor bira `r paste0(hr_broj(100 * s8$udio_portal, 1), " %")` osoba.
To su svojstva naše simulirane populacije, bez tvrdnje o stvarnom gradu.

Za jedan od tih računa nasumično odabiremo 100 različitih osoba bez
vraćanja. Početak izvučenog uzorka prikazan je u tablici. Prvi odgovor
povjerenja iznosi `r s8_jedan$povjerenje_medijima[1]`, ali se sredina
računa iz svih 100 odgovora. Njihov zbroj
`r sum(s8_jedan$povjerenje_medijima)` dijelimo sa 100. Za udio portala
umjesto zbroja ocjena brojimo `r sum(s8_jedan$izvor_vijesti == "portal")`
osoba s tom oznakom izvora, uz isti nazivnik.

*Slika. Prvih pet zapisa jednog uzorka od 100 osoba. Izrada autora.*

U jednom uzorku od stotinu osoba prosječno povjerenje iznosi `r hr_broj(s8$uzorak_sredina, 2)`, a udio
korisnika portala `r paste0(hr_broj(100 * s8$uzorak_portal, 1), " %")`. Vrijednosti su bliske populacijskima, ali nisu
jednake.

**Pogreška uzorkovanja** je razlika između vrijednosti izračunate na uzorku i
vrijednosti koju ima cijela populacija, a nastaje zato što je izmjeren dio
umjesto cjeline.

Pogreška ovdje označuje razliku koja nastaje zato što promatramo samo dio populacije. Moguća je i uz potpuno ispravan unos podataka i postavljanje pitanja. Tu
slučajnu promjenjivost treba razlikovati od sustavnog odstupanja zbog
pristranog odabira.

Pri novom odabiru ponovno je dostupna cijela populacija. Unutar jednog
uzorka osoba ulazi najviše jednom, ali može ući u više različitih uzoraka.
Svako novo izvlačenje ponovno kreće iz cijele populacije, a prethodnih 100 zapisa čini samo jedan od mogućih uzoraka. Populacija i
pravilo odabira ostaju fiksni, mijenjaju se odabrane osobe. Tri neovisna uzorka od po
stotinu osoba daju sredine `r hr_broj(s8$tri[1], 2)`, `r hr_broj(s8$tri[2], 2)` i `r hr_broj(s8$tri[3], 2)`. Dobivene su iz
iste populacije istim postupkom, uz raspon od `r hr_broj(s8$raspon_tri, 2)` boda.

Nakon tri tisuće ponavljanja sredine možemo prikazati kao raspodjelu. Ona
pokazuje gdje se procjene skupljaju i koliko se međusobno razlikuju. Njezine
jedinice su procjene iz uzoraka.

**Distribucija uzorkovanja** je raspodjela vrijednosti koje bi neka statistika
poprimila kroz mnogo ponovljenih uzoraka iste veličine iz iste populacije.

Dvije raspodjele odgovaraju na različita pitanja. Raspodjela opažanja pokazuje
koliko se ljudi razlikuju. Distribucija uzorkovanja pokazuje koliko se mijenja
procjena kroz različite uzorke. Obje imaju sredinu i standardnu devijaciju, pa
je važno svaki put navesti što raspodjela opisuje.

*Slika. Raspodjela pojedinačnih ocjena povjerenja u simuliranoj populaciji i raspodjela sredina tri tisuće uzoraka od po sto osoba, na zajedničkoj osi. Izrada autora. Podaci i postupak opisani su u tekstu.*

Uzoračke sredine ovdje su raspoređene oko populacijske sredine. Procjenitelj
zato dugoročno ne promašuje sustavno naviše ili naniže i nazivamo ga
**nepristranim**. Uži donji panel pokazuje manju promjenjivost sredina
uzoraka. Pojedinačne ocjene ljudi ostaju jednako raspršene.

## Standardna pogreška

Uži donji panel sada želimo opisati brojem. Raspršenost procjena također
mjerimo standardnom devijacijom. Da bismo je
razlikovali od raspršenosti pojedinačnih opažanja, nazivamo je standardnom
pogreškom.

**Standardna pogreška** je standardna devijacija distribucije uzorkovanja, pa
opisuje koliko bi tipično varirala procjena kroz ponovljene uzorke.

Pojedinačne ocjene imaju standardnu devijaciju `r hr_broj(s8$sigma, 2)`, dok standardna
devijacija sredina iz tri tisuće uzoraka iznosi `r hr_broj(s8$se_empirijska, 3)`. Potonja je
standardna pogreška, a prva je od nje `r hr_broj(s8$omjer, 1)` puta veća. Uzorci imaju
po stotinu osoba, a korijen iz sto jest deset. U rezultatima se tako već
nazire odnos koji će opisati formula.

U sredini malog uzorka svaka osoba ima veću težinu. Jedan odgovor u uzorku od
deset ljudi čini desetinu računa, a u uzorku od tisuću ljudi tisućinu. U većem
se uzorku neovisna pozitivna i negativna odstupanja više poništavaju. Zato
sredina manje varira. Dobitak u preciznosti raste s korijenom broja opažanja.

Dosad koristimo **jednostavni slučajni uzorak** (*simple random sample*), u
kojem svaki mogući skup od $n$ jedinica ima jednaku vjerojatnost odabira.
Jedinice iz konačne populacije biramo bez vraćanja. Sljedeća formula točna je
za neovisne odabire s vraćanjem, a dobra je aproksimacija za odabir bez
vraćanja ako je $n$ malen prema $N$. Za druge nacrte slučajnog uzorkovanja
može trebati drukčiji račun.

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

Oznaka $SE_{\bar{x}}$ znači standardnu pogrešku sredine, $\sigma$ populacijsku
standardnu devijaciju, a $n$ veličinu uzorka. Formula ovdje daje `r hr_broj(s8$se_teorijska, 4)`,
dok iz ponavljanja dobivamo `r hr_broj(s8$se_empirijska, 4)`. Rezultati se slažu na tri decimale,
iako su dobiveni različitim postupcima.

Odabir bez vraćanja dodatno smanjuje nesigurnost. Ako uključimo cijelu
populaciju, pogreške uzorkovanja više nema. **Korekcija za konačnu
populaciju** (*finite-population correction*) uzima u obzir taj dobitak
množenjem početnog izraza korijenskim faktorom.

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
  \sqrt{\frac{N-n}{N-1}}
$$

Kada je uzorkovan malen dio populacije, drugi korijen blizu je jedan i malo
mijenja rezultat. Kako se $n$ približava $N$, faktor se smanjuje do nule.
Simulacija bez vraćanja već uključuje taj učinak. U sljedećoj tablici stupac s
formulom koristi aproksimaciju za veliku populaciju, bez te korekcije.

Svaka simulacijska standardna pogreška u tablici ispod nastaje iz
1 500 uzoračkih sredina za navedeni broj osoba. Računamo standardnu
devijaciju tih 1 500 brojeva, bez izostavljenih ponavljanja. To mjeri
preciznost, dok udaljenost njihova prosjeka od poznate populacijske sredine
služi provjeri pristranosti. Konačan broj ponavljanja donosi i malo
simulacijsko kolebanje, pa sitne razlike prema formuli ne tumačimo kao
dokaz sustavnoga odstupanja.

U praksi nepoznatu $\sigma$ procjenjujemo uzoračkom standardnom devijacijom
$s$. Sada možemo provjeriti i
raniji izbor djelitelja $n-1$ za varijancu. U četiri tisuće uzoraka od po
deset osoba dijeljenje kvadriranih odstupanja s deset daje prosječno
`r hr_broj(s8$var_n, 2)`, dok je populacijska varijanca `r hr_broj(s8$var_prava, 2)`. Dijeljenje s devet daje
`r hr_broj(s8$var_n1, 2)`. Djelitelj $n$ sustavno podcjenjuje varijancu jer odstupanja
računamo od sredine istog uzorka, koja tim vrijednostima pristaje bliže od
populacijske sredine.

Tablica pokazuje kako preciznost raste s veličinom uzorka. Za svako dodatno
smanjenje standardne pogreške trebamo sve više opažanja.

*Slika. Standardna pogreška sredine povjerenja pri osam veličina uzorka, izračunata formulom i izmjerena na tisuću i petsto ponovljenih uzoraka. Izrada autora.*

Svako deseterostruko povećanje uzorka smanjuje standardnu pogrešku za faktor
$\sqrt{10}$, približno 3,16. Da bi se standardna pogreška prepolovila, uzorak se
mora učetverostručiti. Za svako daljnje smanjenje slučajne raspršenosti zato treba prikupiti sve
više opažanja.

## Oblik koji se pojavljuje

Zadržavamo istu populaciju osoba, ali povjerenje zamjenjujemo iznosom
spremnosti na plaćanje. Za svaku od veličina 5, 15, 30 i 100 izvučemo
4 000 novih uzoraka bez vraćanja i za svaki spremimo jednu sredinu.
Nule su valjani odgovori i ostaju u svim računima. Tako promjena oblika
koju ćemo gledati nastaje usrednjavanjem, bez uklanjanja neplatitelja.

Uz širinu treba pogledati i oblik distribucije uzorkovanja. Spremnost na
plaćanje u populaciji ima `r paste0(hr_broj(s8$platiti_nula, 1), " %")` nula i dug desni rep, uz asimetriju
`r hr_broj(s8$platiti_asimetrija, 1)`. Izvorne vrijednosti izrazito odstupaju od normalne raspodjele.

Za uzorke od pet osoba asimetrija raspodjele sredina je `r hr_broj(s8$clt_asimetrija[["5"]], 2)`. Za petnaest
pada na `r hr_broj(s8$clt_asimetrija[["15"]], 2)`, za trideset na `r hr_broj(s8$clt_asimetrija[["30"]], 2)`, a za sto na `r hr_broj(s8$clt_asimetrija[["100"]], 2)`. Mijenja se
raspodjela sredina, dok izvorna populacija ostaje ista.

*Slika. Izrazito asimetrična populacijska varijabla i raspodjele njezinih uzoračkih sredina pri četiri veličine uzorka. Svaki panel ima vlastitu os. Izrada autora. Podaci i postupak opisani su u tekstu.*

**Središnji granični teorem** (*central limit theorem*) u ovom modelu opisuje
približavanje distribucije sredine normalnoj raspodjeli s rastom jednostavnog
slučajnog uzorka. Potrebna je konačna varijanca i raspodjela u kojoj
nekolicina jedinica ne nosi gotovo cijeli zbroj. Dovoljna veličina uzorka
ovisi o obliku i repovima populacije. U našem je primjeru i pri trideset osoba
ostalo dosta asimetrije, dok za gotovo simetričnu populaciju manji uzorak može
biti dovoljan.

Mnogi se postupci zato oslanjaju na približnu normalnost raspodjele procjene, dok pojedinačna opažanja mogu imati drukčiji oblik. Primjena teorema i dalje zahtijeva odgovarajuće uvjete odabira i neovisnosti. Kod složenijeg uzorkovanja
težine i zajednički odabir skupina mogu promijeniti i oblik i širinu
raspodjele procjene. Račun mora pratiti taj nacrt.

Dva prikaza empirijske standardne pogreške potječu iz zasebnih simulacija.
Raspodjela sredina pri stotinu osoba ima 3 000 ponavljanja, a usporedna
tablica za svaku veličinu uzorka koristi 1 500 novih ponavljanja. Male razlike
njihovih procjena SE-a zato odražavaju i konačan broj simulacija.

## Interakcija — CLT stroj

Za interaktivni pokus napuštamo mjerne jedinice medijskih podataka i
koristimo zasebne umjetne raspodjele. Tiskani prikaz polazi od 5 000
generiranih vrijednosti između nule i jedinice, s mnogo malih vrijednosti
i sve manje velikih. Iz tog fiksnog skupa izvlačimo s vraćanjem, po 2 000
uzoraka veličine pet i četrdeset. Jedno izvlačenje daje jedan broj, a
prosjek cijelog uzorka jednu vrijednost donjeg histograma. Ovdje je
vraćanje dio zadanoga modela uzorkovanja iz poznate populacije.

Uz populacijsku raspodjelu prikazane su raspodjele uzoračkih
sredina za dvije veličine uzorka. Populacija je u oba slučaja ista.
Usporedba pokazuje kako veći uzorak mijenja oblik raspodjele sredina i
smanjuje njezinu širinu. Pri fiksnoj populaciji standardna pogreška
smanjuje se s korijenom veličine uzorka.

*Slika. Izvorna populacija i raspodjela sredina mnogih uzoraka na zajedničkoj osi. Okomita crta označuje populacijsku sredinu simulacije.*

**Što isprobati.**

1. Odaberite simetričnu populaciju i uzorak veličine dva pa usporedite širine dvaju histograma.
2. Promijenite populaciju u desno asimetričnu bez povećanja uzorka.
3. Povećajte uzorak na četrdeset i odvojeno opišite promjenu oblika i širine raspodjele sredina.
4. Odaberite dvovršnu populaciju i pronađite veličinu uzorka pri kojoj se dvije populacijske skupine više ne vide u sredinama.

## Preciznost ankete od osamsto ljudi

U anketi često želimo procijeniti udio, primjerice koliko ljudi bira portal,
umjesto prosječne ocjene povjerenja. Za to možemo iskoristiti poznati račun.
Izbor portala označimo jedinicom, a ostale izbore nulom, pa sredina tih
vrijednosti daje **uzorački udio**, označen s $\hat{p}$. Njime
procjenjujemo populacijski udio, uz istu logiku uzorkovanja sredine koju smo
upravo upoznali. Raspršenost binarne varijable određena je njezinim udjelom.
Najveća je kada je populacija podijeljena napola, a manja blizu nule ili jedan.

Standardnu pogrešku ukupnog udjela u velikoj populaciji procjenjujemo
sljedećim izrazom za jednostavni slučajni uzorak. Nepoznati populacijski udio
zamjenjujemo procjenom $\hat{p}$, pa je i standardna pogreška procijenjena.

$$
SE_{\hat{p}} = \sqrt{\frac{\hat{p}\,(1 - \hat{p})}{n}}
$$

Kod jednostavnoga slučajnog uzorka bez vraćanja izraz se množi istom korekcijom
za konačnu populaciju kao i standardna pogreška sredine. Kod nejednakih
vjerojatnosti odabira ili grupnog uzorkovanja ne smije se prenijeti bez
prilagodbe nacrtu.

**Margina pogreške** (*margin of error*) polovica je širine intervala oko
procjene. U prikazanom računu najveća je za udio od 50 %, jer je tada
raspršenost najveća. Za razinu od 95 % i veliku populaciju približno iznosi
jedan podijeljen korijenom veličine uzorka.

U sljedećem računu marginu dobivamo množenjem procijenjene standardne pogreške
s 1,96. Obrnutim računom određujemo potreban uzorak za željenu marginu.
Vrijede pretpostavke jednostavnog slučajnog uzorka i velike populacije te
razumna normalna aproksimacija. Ona može biti neprikladna ako je očekivan broj
jedne kategorije malen.

*Slika. Najveća margina pogreške za udio pri razini od 95 % i uzorak potreban za zadanu marginu. Izrada autora.*

Tablica se odnosi na jedan ukupni udio, jednostavni slučajni uzorak i razinu
od 95 %, bez korekcije za konačnu populaciju. Za osamsto ljudi najveća margina
je približno `r paste0("±", hr_broj(100 * s8$moe(800), 1), " %")`. Takva procjena razlikuje veličine udaljene desetak
postotnih bodova bolje nego one udaljene dva ili tri. Drugi cilj procjene,
nacrt ili zahtjev za preciznošću traži novi račun.

Kada izvještaj navodi da prva opcija ima 32 %, a druga 29 %, same dvije
procjene i njihove pojedinačne margine nisu dovoljne za tvrdnju da je prva
opcija ispred druge. Razlika dvaju udjela ima vlastitu nesigurnost, koju treba
izračunati iz zajedničkoga nacrta.

Veličina populacije izostaje iz jednostavne formule jer smo zanemarili
korekciju za konačnu populaciju. To je opravdano kada uzimamo malen dio
populacije. Manju populaciju čini slučajno izdvojenih `r length(s8_mala_pop)` vrijednosti povjerenja iz iste populacije `populacija_medija`. Iz tako određenih cjelina zasebno izvlačimo uzorke. U simulaciji uzorak od osamsto osoba iz cijele populacije daje
standardnu pogrešku `r hr_broj(s8$se_velika, 4)`, a iz deset puta manje populacije `r hr_broj(s8$se_mala, 4)`.
Uzorak u drugom slučaju obuhvaća veći dio cjeline, pa je precizniji.
Populacijske devijacije iznose `r hr_broj(s8$sigma, 3)` i `r hr_broj(s8$sigma_mala, 3)`. Formula s korekcijom
uzima u obzir i tu malu razliku te daje `r hr_broj(s8$se_velika_fpc, 4)` i `r hr_broj(s8$se_mala_fpc, 4)`, blizu
simuliranim rezultatima.

Dovoljnu veličinu uzorka određujemo prema pitanju koje istražujemo. Trebamo znati procjenjujemo li ukupni udio, sredinu, rijetku pojavu ili razliku skupina.
Trebamo i nacrt, način odabira i odaziva te željenu preciznost. Preciznost za podskupinu ovisi o broju njezinih članova. Oko tisuću može biti korisna orijentacija za jedan ukupni udio u jednostavnom nacrtu. Za ostale ciljeve veličinu određujemo zasebno.

Margina pogreške opisuje promjenjivost zbog slučajnog odabira. Ne uključuje
ljude izvan okvira, neodaziv ni učinak formulacije i redoslijeda pitanja.
Oznaka ±3 % u tom kontekstu znači tri postotna boda margine za uzorkovnu
promjenjivost. Tvrdnja da je razlika unutar margine zato ne potvrđuje
kvalitetu svih ostalih dijelova istraživanja.

## Nacrt uzorka i pristranost odabira

Dosadašnji račun polazio je od jednakih izgleda za odabir. U stvarnoj anketi
neke osobe mogu imati veće izglede od drugih, pa njihov doprinos procjeni
trebamo prilagoditi. U **vjerojatnosnom uzorkovanju** svaka jedinica ima poznatu pozitivnu
vjerojatnost uključivanja, ali ona ne mora biti jednaka za sve. Jedinici s
upola manjom vjerojatnošću dajemo približno dvostruk doprinos procjeni.
Početna **težina uzorkovanja** računa se kao obrnuta vjerojatnost
uključivanja. Bez težina bismo previše zastupali češće birane jedinice. Ni
pravilne težine, međutim, ne vraćaju ljude koji su potpuno izostali iz okvira.

Učinak težina prikazat ćemo na šest odabranih jedinica iz zasebne sintetičke
populacije od šesnaest osoba. U svakom od dvaju slojeva ima osam osoba.
Jedinica označuje potporu zamišljenoj mjeri, a nula izostanak potpore.
Vjerojatnosti uključivanja su 0,50 u prvom i 0,25 u drugom sloju, pa su težine
dva i četiri.

*Slika. Opaženi uzorak iz sintetičke konačne populacije s poznatim vjerojatnostima uključivanja. Izrada autora.*

Bez težina dijelimo brojnik `r hr_broj(s8_tezine_rez$brojnik_bez_tezina, 0)` nazivnikom `r hr_broj(s8_tezine_rez$nazivnik_bez_tezina, 0)` i dobivamo
`r paste0(hr_broj(100 * s8_tezine_rez$procjena_bez_tezina, 1), " %")`. S težinama dobivamo brojnik `r hr_broj(s8_tezine_rez$brojnik_s_tezinama, 0)`, nazivnik `r hr_broj(s8_tezine_rez$nazivnik_s_tezinama, 0)` i udio
`r paste0(hr_broj(100 * s8_tezine_rez$procjena_s_tezinama, 1), " %")`. Procjena pada jer dvije nule iz rjeđe biranog sloja više pridonose
nazivniku. Dobivenih 37,5 % i dalje je procjena, s mogućom pogreškom
uzorkovanja. Primjer provjerava račun na vidljivoj sintetičkoj tablici, bez
tvrdnje o stvarnim ljudima.

Složeni uzorci traže dodatne prilagodbe. **Kalibracija težina** usklađuje
ponderirane zbrojeve s poznatim obilježjima populacije. Pri **grupnom
uzorkovanju** biramo skupine, primjerice škole, pa osobe unutar njih.
Sličnost tih osoba može smanjiti količinu neovisne informacije. **Učinak
nacrta** uspoređuje varijancu procjene s onom jednostavnoga slučajnog uzorka,
a **efektivna veličina uzorka** izražava istu preciznost brojem jedinica
takva uzorka.

Pri čitanju izvještaja provjeravamo uključuje li račun nesigurnosti težine,
skupine i slojeve. Neodaziv i potpunost okvira zahtijevaju zasebnu provjeru i obrazložene prilagodbe. Neobvezni odjeljak praktikuma
podrobnije objašnjava te prilagodbe.

## Pokrivenost, odabir i odaziv

Težinama smo uzeli u obzir različite izglede uključenih jedinica. One ipak
ne rješavaju problem ljudi koji uopće nisu mogli biti odabrani.
**Pogreška pokrivenosti** nastaje kada okvir iz kojega se bira ne dopušta svim
jedinicama ciljne populacije da uopće uđu u uzorak. Povećanje broja odabranih
jedinica unutar istoga okvira ne doseže one koji u njemu nedostaju.

U prigodnom uzorku biramo dostupne ljude, bez poznatih vjerojatnosti odabira.
U našoj populaciji mlađih od dvadeset pet godina s višim obrazovanjem ima
`r hr_broj(s8$prigodni_n, 0)`. Njihovo prosječno povjerenje iznosi `r hr_broj(s8$prigodni_sredina, 2)`, dok je populacijsko
`r hr_broj(s8$mu, 2)`. Razlika nadmašuje cijelu marginu ankete s tisuću ljudi.
Uključivanjem svih članova te uske skupine točno bismo opisali upravo nju, uz istu razliku prema cijeloj populaciji.

U sljedećem modelu samoodabira ponovno razmatramo svih 50 000 osoba.
Osobi mlađoj od 30 koja bira mreže dajemo 15 % izgleda za uključivanje,
a ostalima te dobi 8 %. U dobi od 30 do 49 godina izgledi su 6 % za
portal ili mreže i 3 % za ostale izvore. Od 50 godina naviše odgovarajući
izgledi iznose 2 % i 0,5 %. Svakoj osobi zatim neovisno odredimo ulazi li
u anketu. Ta smo pravila zadali za ovu ilustraciju samoodabira.

U dobrovoljnu mrežnu anketu ulaze ljudi koji su na internetu, vide poziv i
odluče odgovoriti. Svaki korak može mijenjati sastav. Simulacija takvog
odabira daje `r hr_broj(s8$online_n, 0)` odgovora, mnogo više od početnog slučajnog uzorka od
sto osoba. Prosječna dob je `r hr_broj(s8$online_dob, 1)`, umjesto populacijskih `r hr_broj(s8$dob, 1)` godina.
Mreže bira `r paste0(hr_broj(100 * s8$online_mreze, 1), " %")`, naspram `r paste0(hr_broj(100 * s8$udio_mreze, 1), " %")`, a povjerenje je `r hr_broj(s8$online_sredina, 2)`, naspram
`r hr_broj(s8$mu, 2)`.

Čak i uz dobar okvir i slučajni odabir dio pozvanih može izostati.
**Neodgovor** smanjuje uzorak i preciznost, a može donijeti i pristranost. Ako
se odazvani i neodazvani razlikuju u obilježju koje procjenjujemo, primjerice
zbog interesa za temu ili povjerenja u istraživača, sam slučajni odabir nije
dovoljan. Provjeravamo i odabir i odaziv.

Velik pristran uzorak može dati uzak interval oko sustavno pogrešne
vrijednosti. Standardna pogreška prikazuje slučajnu promjenjivost pod nacrtom,
ali ne i svu pristranost odabira. Povećanje uzorka uz isti pristrani postupak
zato ne jamči točniju procjenu.

Sada možemo objasniti promašaj časopisa *Literary Digest*. Na temelju
naknadne Gallupove ankete Squire je utvrdio da su pogrešnoj prognozi
pridonijeli i sastav primatelja i njihov nejednak odaziv (Squire, 1988).
Njegova analiza upućuje na to da bi potpuni odaziv izabranih primatelja,
unatoč problemu njihova odabira, barem ispravno imenovao Roosevelta kao
pobjednika (Squire, 1988). Zato popis onih kojima smo poslali pitanje i
popis onih koji su odgovorili pregledavamo zasebno. Još odgovora
prikupljenih na isti način može smanjiti slučajno kolebanje, dok
sustavno odstupanje ostaje.

Zadržavamo sedam polja kartice za čitanje ankete iz poglavlja o mjerenju.
Sada pitanja unutar tih polja preciziramo znanjem o procjeni i margini.
Svako polje pokazuje dio postupka koji određuje na koga se rezultat može
odnositi.

| Polje kartice | Pitanje nakon ovoga poglavlja |
|---|---|
| okvir i pozivanje | Koja je ciljna populacija, tko je mogao ući u uzorak i je li odabir vjerojatnosan? |
| odaziv i nedostajanje | Koliko je pozvanih odgovorilo i kako bi se neodazvani mogli razlikovati? |
| procjena s težinama | Kako su uključivanje i sastav prilagođeni težinama i što ostaje neprilagođeno? |
| mjerenje | Kako glasi pitanje i koji odgovor ulazi u brojnik i nazivnik? |
| provedba | Kada i kako je anketa provedena te tko ju je naručio? |
| doseg | Na koju se podskupinu procjena odnosi i koga okvir, odaziv ili filtri izostavljaju? |
| nesigurnost | Uvažava li račun težine, slojeve i skupine stvarnoga nacrta? |

: Kartica za čitanje ankete nakon poglavlja o uzorkovanju. Izrada autora.

## Korpus kao uzorak

Iste granice odabira susrećemo kada umjesto ljudi prikupljamo njihove
tekstove. I korpus tekstova zahtijeva ciljnu populaciju. Za opis političke rasprave
trebamo navesti uključujemo li govore, intervjue ili objave, s kojih platformi
ili arhiva, iz kojeg razdoblja, na kojim jezicima i od kojih govornika. Dostupnost tekstova tek je polazište. Populaciju određujemo prema sadržajnom pitanju i navedenom obuhvatu.

Obrisane i privatne objave mogu izostati iz arhiva, stariji sadržaj biti
nedostupan, a odabrana ključna riječ propustiti relevantne tekstove. Veći broj
riječi ne uklanja takve propuste ni činjenicu da su se neki govornici sami
odlučili oglasiti. Zaključak zato ograničavamo na obuhvaćene vrste tekstova,
platforme, datume, jezike i govornike.

Treba odrediti i jedinicu brojanja. Brojanje riječi daje više težine duljim
tekstovima, a brojanje objava aktivnijim govornicima. Udio govornika odgovara
na drugo pitanje. Uz zastupljenost zato navodimo brojimo li riječi, tekstove,
istupe ili ljude, ponavljaju li se jedinice istog govornika i koji nazivnik
koristimo.

Jedan dio korpusa možemo upotrijebiti za izradu pravila, a drugi sačuvati za
provjeru na jedinicama koje pri izradi nismo vidjeli. Ista osoba ili gotovo
isti tekst ne smije se naći s obiju strana takve provjere. Time provjeravamo
predviđanje na novim jedinicama iz sličnog procesa prikupljanja. Ta podjela ne
popravlja pokrivenost korpusa niti opravdava zaključak o izostavljenim
tekstovima i govornicima. Prediktivna provjera i populacijsko uopćavanje
zahtijevaju zasebna obrazloženja.

**Statistika u divljini.**
**Isti upitnik, različiti putovi do sudionika.** Usporedba Pew Research
Centera, objavljena 2023., koristila je isti upitnik u šest internetskih
uzoraka odraslih stanovnika SAD-a. Tri su nastala iz panela s
vjerojatnosnim početnim odabirom, a tri dobrovoljnim pristupanjem.
Procjene su uspoređene s vanjskim referentnim vrijednostima, među kojima
su bili službeni izborni rezultati i podaci kvalitetnih državnih anketa
(Mercer, 2023). Ispunjavanje obrasca na internetu bilo je zajedničko
svima. Put kojim je osoba došla do obrasca razlikovao se.

Procjene iz panela s vjerojatnosnim odabirom u toj su usporedbi u prosjeku
manje odstupale od referentnih vrijednosti, uz isti postupak ponderiranja
svih uzoraka (Mercer, 2023). Referentne vrijednosti također mogu imati
pogrešku, pa ih čitamo kao najbolju dostupnu usporedbu (Mercer, 2023).
Kad sljedeći put otvorimo mrežnu anketu, vrijedi pogledati kako smo dobili
poziv i tko ga uopće može dobiti. Oznaka „internetska anketa” sama po sebi
još ništa ne govori o tom odabiru.

Pri objašnjavanju koristi većeg uzorka brojčani rezultat treba povezati
s onim što je u postupku uzorkovanja doista postalo preciznije.

**Nađite grešku.**
Za objašnjenje standardne pogreške pripremamo nastavnu usporedbu
dviju veličina uzorka. U zadanom modelu nasumično i neovisno izvlačimo
osobe iz iste zamišljene populacije. Standardna devijacija njihova
dnevnog vremena uz medije iznosi 20 minuta. Tablica sadrži teorijske
vrijednosti prema tom modelu, a ne rezultate provedene ankete.

| Veličina uzorka | Standardna devijacija u populaciji | Standardna pogreška sredine |
|---|---:|---:|
| 25 osoba | 20 minuta | 4 minute |
| 100 osoba | 20 minuta | 2 minute |

: Dvije veličine uzorka iz iste populacije. Konstruirana nastavna vježba, izrada autora.

Asistent je ispod usporedbe napisao objašnjenje.

> Veći nasumični uzorak daje užu distribuciju uzoračkih sredina.
> Standardna pogreška pada s četiri na dvije minute, pa se i vremena
> pojedinaca u većem uzorku međusobno razlikuju upola manje.

Uz svaki od posljednjih dvaju stupaca dopišite čiju raspršenost
opisuje. Provjerite račune standardne pogreške, a zatim preoblikujte
drugu rečenicu objašnjenja tako da zadrži točan podatak iz tablice.

## Razrađeni primjer

Za spremnost na plaćanje sada povezujemo dvije provjere koje smo dosad
promatrali odvojeno. Želimo znati gdje su procjene usredotočene i koliko su
raspršene, iako izvorna varijabla ima mnogo nula i dug desni rep. Odaberemo
uzorak, izračunamo sredinu i postupak ponovimo mnogo puta. Mnoge kasnije
formule opisivat će ili približno izražavati rezultat takvog ponavljanja unutar
određenog modela.

Jedan korak možemo pratiti na zasebnoj, namjerno sastavljenoj ilustraciji
s iznosima 0, 0, 10, 20 i 70 eura. Sredina je $100/5 = 20$
eura. U ponavljanju zamjenjujemo cijeli uzorak, uključujući moguće nule,
novim odabirom iz svih 50 000 osoba. Svaki novi uzorak ostavlja samo
jednu sredinu u raspodjeli koju uspoređujemo.

Isti ćemo postupak provesti s dvjema veličinama uzorka. Ako veći uzorak daje
užu raspodjelu sredina, provjerit ćemo smanjuje li se njezina širina onako kako
predviđa odnos s korijenom veličine uzorka. Zasebno ćemo pregledati je li se
promijenio i njezin oblik.

`replicate` ponavlja izraz i sprema rezultate. Prosjek četiri tisuće sredina iz
uzoraka od pet osoba je `r hr_broj(s8_p$m5, 2)` eura, a iz uzoraka od šezdeset `r hr_broj(s8_p$m60, 2)`
eura. Populacijska sredina je `r hr_broj(s8_p$mu, 2)` eura. Obje veličine uzorka daju
procjene usredotočene blizu nje, u skladu s nepristranošću.

Standardna pogreška pada s `r hr_broj(s8_p$se5, 2)` za pet osoba na `r hr_broj(s8_p$se60, 2)` za šezdeset,
odnosno `r hr_broj(s8_p$omjer, 1)` puta. To je približno korijen iz dvanaest, koliko smo puta
povećali uzorak. Raspodjela sredina za pet osoba ipak ostaje vidljivo
asimetrična. Nepristranost procjenitelja zato treba razlikovati od normalnog
oblika njegove raspodjele.

Provjeru smo mogli napraviti jer poznajemo cijelu generiranu `populacija_medija`. U
stvarnom istraživanju obično raspolažemo samo jednim uzorkom i ne možemo
ponavljati odabir iz potpuno poznate cjeline. Zato svojstva distribucije
uzorkovanja procjenjujemo iz tog uzorka, uz pretpostavke. U poglavlju o
procjeni uzorak će privremeno preuzeti ulogu populacije i omogućiti novo
ponavljanje postupka.

Za računsku provjeru pretpostavimo neovisna opažanja i standardnu devijaciju
od 12 minuta. Pri 36 opažanja standardna pogreška sredine iznosi
$12/\sqrt{36}=2$ minute, a pri 144 opažanja jednu minutu. Raspršenost
pojedinačnih odgovora ostaje 12 minuta. Četverostruko veći uzorak prepolovio je nesigurnost sredine, uz istu raspršenost odgovora pojedinačnih ljudi.

Približenje $1/\sqrt{n}$ za 95-postotnu marginu udjela odnosi se na
jednostavni slučajni uzorak, malu uzoračku frakciju i najnepovoljniji udio
od 0,5. Nastaje iz $1,96\sqrt{0,25/n}$ uz zaokruživanje 0,98 na jedan.
Nije opća formula za svaki udio i svaki nacrt. Kalibracija težina usklađuje
ponderirane zbrojeve s poznatim obilježjima populacije. Razlikuje se od
kalibracije prognoze, koja uspoređuje najavljene vjerojatnosti s ishodima.

## Sažetak

Ponavljanjem odabira dobili smo distribuciju uzorkovanja i razdvojili
promjenjivost procjene od razlika među pojedinačnim osobama. Standardna
devijacija te distribucije jest standardna pogreška, koja za sredinu u
jednostavnom slučajnom uzorku pada približno s korijenom veličine uzorka, uz
dodatnu korekciju kada obuhvaćamo znatan dio populacije. Kad nacrt uključuje
težine, skupine i slojeve, račun mora pratiti te odluke, a njihove posljedice
za preciznost opisujemo učinkom nacrta i efektivnom veličinom uzorka. Takav
račun ne obuhvaća automatski probleme pokrivenosti, neodaziva ili samoodabira,
koje ni veći uzorak ni kalibracija sami ne uklanjaju. I za korpus tekstova zato
odvojeno obrazlažemo odabir i procijenjenu nesigurnost. U poglavlju o procjeni
iz te nesigurnosti gradimo interval za nepoznatu populacijsku vrijednost.

Distribucija i raspodjela ovdje su sinonimi. Statistika kao broj iz uzorka razlikuje se od statistike kao znanstvene discipline. Ponderiranje znači primjenu težina. Neodaziv, nazvan i neodgovor, znači da za pozvane jedinice nedostaju odgovori.

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

U zasebnom jednostavnom slučajnom uzorku iz velike populacije standardna
devijacija obilježja iznosi 12. Izračunajte standardnu pogrešku sredine za
uzorke od 64 i 256 osoba. Koliko se puta mora povećati uzorak da se pogreška
prepolovi? Za udio 0,5 u uzorku od 400 osoba procijenite 95-postotnu marginu
pravilom $1/\sqrt{n}$ i navedite pretpostavke toga pravila.

Za obje veličine uzorka izračunajte i 1,96 standardnih pogrešaka te navedite
približan raspon odstupanja uzoračke sredine od populacijske sredine kada
vrijedi normalno približenje. Riječima protumačite dobivenu marginu udjela.

Neobvezna nadogradnja dostupna je samo čitatelju s vlastitom službeno preuzetom
kopijom ESS Round 11, edition 3.0. Slijedeći portalnu putovnicu iz kataloga,
ograničite podatke na Hrvatsku, za `vote` primijenite njegov službeni valjani
nazivnik te usporedite procjenu bez težina s procjenom uz zadani `anweight`.
Navedite i jednu pogrešku odabira ili mjerenja koju ta težina ne može ukloniti.
Rezultat tumačite kao samoprijavu, ne kao provjeru službene izlaznosti. ESS
mikropodaci i rezultat te provjere nisu dio knjige ni obveznoga zadatka.

### Kritički

Vratite se na karticu za čitanje ankete iz poglavlja o mjerenju i dizajnu i primijenite je
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

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/09-procjena.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Zamislimo da otvaramo ljestvicu školskih postignuća i odmah tražimo
Hrvatsku. Iznad nje nekoliko poznatih zemalja, ispod nje neke druge.
Takav je poredak lako pročitati kao ocjenu škole koju smo pohađali ili
u koju ćemo upisati dijete. Svako mjesto izgleda određeno.

U istraživanju PISA 2022. postignuća petnaestogodišnjaka procijenjena su
iz uzoraka učenika, pa OECD uz prosječne rezultate objavljuje intervale
pouzdanosti i raspone mogućih mjesta na ljestvici ({OECD}, 2023).
Zemlje s bliskim prosjecima tako mogu zauzimati više mogućih mjesta,
ovisno o nesigurnosti procjene ({OECD}, 2023).

Koliko zapravo znamo o nečijem mjestu na ljestvici kad znamo samo njegov
procijenjeni prosjek?

U simulacijama uzorkovanja mogli smo iznova odabirati ljude iz poznate
populacije i pratiti kako se mijenjaju uzoračke sredine. Istraživač obično nema tu
mogućnost. Pred njim je jedan skup odgovora, a treba navesti koliko bi se
njegova procjena mogla promijeniti s drugim sudionicima. Standardna pogreška
iz prethodnog poglavlja daje nam polazište za takav opis nesigurnosti.

Za razumijevanje intervala poslužit će nam jednostavniji nacrt od PISA-ina.
Nastavljamo s nastavnom populacijom `populacija_medija`. Uzorak od 200 osoba
izvlačimo iz nje zasebno od ranijih uzoraka, za procjenu prosječnog povjerenja
u medije. Svako opažanje pripada jednoj računalno stvorenoj osobi i sadrži
njezinu ocjenu povjerenja na ljestvici od jedan do deset. Zapisi ne opisuju
stvarne stanovnike. Pri izgradnji procjene koristit ćemo uzorak, a poznatu
populacijsku vrijednost zatim iskoristiti za provjeru postupka.

Oko procjene ćemo konstruirati interval i pratiti što se događa kroz
ponovljena uzorkovanja. Pitanje je koliko često tako izrađen raspon obuhvaća
ciljnu vrijednost. To će nam omogućiti da pouzdanost vežemo uz postupak, a
širinu intervala uz preciznost. Usporedit ćemo što se mijenja kada tražimo
višu pouzdanost i što dobivamo prikupljanjem više podataka. Posebno ćemo
odvojiti nesigurnost procijenjenog prosjeka od razlika među pojedinačnim
odgovorima.

Za procjenu medijana dnevnog praćenja medija poslužit će nam uzorak od 60 osoba,
izvučen zasebno iz iste simulirane populacije. Njegove ćemo zapise ponovno
izvlačiti, dopuštajući da ista osoba bude odabrana više puta. Taj postupak,
bootstrap, omogućit će nam procijeniti promjenjivost i kada ne polazimo od
gotove formule za odabranu mjeru. Razmotrit ćemo koliko takva provjera ovisi o
uzorku kojim raspolažemo.

Uz procjenu u izvještaju navodimo raspon njezine nesigurnosti i objašnjavamo
što bi precizniji odgovor zahtijevao. Interval pritom neće ukloniti
ograničenja mjerenja ili odabira ljudi koja smo upoznali ranije.

## Od točke prema rasponu

Uzorak od 200 osoba sada koristimo za procjenu povjerenja. Za svaku osobu koristimo povjerenje u
medije na ljestvici od jedan do deset. Prosjek uzorka iznosi `r hr_broj(s9$sredina, 2)`. Tu vrijednost zovemo **točkasta procjena** (*point
estimate*). Ona sažima rezultat, a njegovu nesigurnost opisujemo zasebno. Isti
prosjek možemo dobiti na dvadeset i na dvadeset tisuća ljudi, iako bi se pri
ponovnom uzorkovanju te procjene mogle znatno različito mijenjati.

Za opis te promjenjivosti služi standardna pogreška, koju smo upoznali u
prethodnom poglavlju. Ona procjenjuje koliko bi se rezultat tipično mijenjao
kroz ponovljena uzorkovanja. U našem uzorku iznosi `r hr_broj(s9$se, 3)`.

Račun intervala možemo pratiti od zbroja ocjena do njegovih granica. Zbroj svih
ocjena u uzorku iznosi `r sum(s9_x)`, pa dijeljenjem s 200 dobivamo
`r hr_broj(s9$sredina, 3)`. Uzoračka standardna devijacija
`r hr_broj(s9$sd, 3)` podijeljena korijenom iz 200 daje standardnu
pogrešku `r hr_broj(s9$se, 3)`. Umnožak te pogreške s 1,96 iznosi
`r hr_broj(1.96 * s9$se, 3)`, što oduzimamo od sredine i dodajemo joj.
Dobivene granice uspoređujemo s jednom fiksnom populacijskom sredinom,
`r hr_broj(s9$mu, 3)`.

Provjerimo što iz toga možemo zaključiti u simulaciji s poznatom populacijom.
Deset tisuća puta izvukli smo po dvjesto različitih osoba bez vraćanja,
svaki put iz cijele populacije. Ponovno računamo i sredinu i standardnu
pogrešku, pa se obje granice mijenjaju. Oko svake uzoračke sredine
označili smo raspon od 1,96 njezinih standardnih pogrešaka na svaku stranu.
Populacijska vrijednost nalazi se u `r paste0(hr_broj(s9$pokrivenost, 1), " %")` raspona. Izvan raspona ostaje u
`r hr_broj(s9$promasaji, 0)` od `r hr_broj(s9$ponavljanja, 0)` ponavljanja. Vidimo da pojedini raspon može promašiti
cilj, ali i da možemo pratiti koliko ga često postupak obuhvaća.
U račun uključujemo svih 10 000 intervala. Broj onih čije granice obuhvaćaju cilj dijelimo s 10 000.
Dobiveni udio nazivamo obuhvatom intervala.

Središnji granični teorem pomaže objasniti taj rezultat. Pod njegovim uvjetima
raspodjela uzoračkih sredina približno je normalna. U normalnoj raspodjeli oko
95 % vrijednosti nalazi se unutar 1,96 standardnih devijacija od središta. Za
raspodjelu procjena tu udaljenost mjerimo standardnom pogreškom.

Ako je uzoračka sredina dovoljno blizu populacijskoj vrijednosti, i
populacijska vrijednost jednako je blizu uzoračkoj sredini. Zato raspon od
1,96 standardnih pogrešaka na svaku stranu od procjene obuhvaća populacijsku
vrijednost u približno 95 % ponavljanja, kada vrijede pretpostavke postupka.

Oznaka $z^{*}$ govori koliko standardnih pogrešaka odmjeravamo na svaku stranu
od procjene. Za razinu pouzdanosti od 95 % ona iznosi 1,96.

Normalne kritične vrijednosti za obostrane intervale iznose 1,645 za
90 %, 1,960 za 95 % i 2,576 za 99 %. Koristimo ih kada je raspodjela
procjenitelja približno normalna i standardna pogreška dovoljno dobro
poznata. Za ovdje prikazane jednostavne sredine potrebna su neovisna
opažanja iz odgovarajuće populacije, konačna varijanca i uzorak bez
dominantnih krajnjih vrijednosti. Pri malim uzorcima i procjeni raspršenosti
iz istih podataka prikladan t-postupak upoznat ćemo uz usporedbu skupina.

$$
\bar{x} \pm z^{*} \cdot SE_{\bar{x}}
$$

U našem uzorku dobivamo raspon od `r hr_broj(s9$donja, 2)` do `r hr_broj(s9$gornja, 2)`. Poznata populacijska
vrijednost iznosi `r hr_broj(s9$mu, 2)` i ovaj je raspon obuhvaća.

**Interval pouzdanosti** je raspon oko procjene, izračunat postupkom koji kroz
ponovljena uzorkovanja obuhvaća nepoznati parametar u unaprijed određenom udjelu
slučajeva.

Razina pouzdanosti opisuje koliko često postupak obuhvaća cilj kada se
uzorkovanje ponavlja. Tu razliku trebamo zadržati i kada tumačimo samo jedan
izračunati interval.

Ovdje pouzdanost opisuje postupak intervalne procjene. U poglavlju o mjerenju ista se riječ odnosila na dosljednost mjerenja. Obuhvat intervala označuje
koliko intervala sadrži cilj, a obuhvat okvira uzorkovanja govori tko je
uopće mogao biti odabran.

U simetričnom intervalu udaljenost od procjene do bilo koje granice jest
**margina pogreške**. Ona je polovica ukupne širine i broj uz znak ± koji
smo susreli uz anketne rezultate. U ovom postupku iznosi $z^{*}\cdot SE$.
Asimetričan interval može imati različite udaljenosti od procjene do
donje i gornje granice, pa ih treba navesti odvojeno. Opisuje promjenjivost zbog uzorkovanja pod pretpostavkama postupka. Ne
uključuje pristran okvir uzorkovanja, neodgovor, formulaciju pitanja ni
pogrešku mjerenja. Manja margina zato sama po sebi ne znači da je anketa
kvalitetnija.

## Obećanje razine pouzdanosti

Za provjeru granice postupka vratimo se izrazito asimetričnoj raspodjeli
spremnosti na plaćanje iz prethodnog poglavlja. Iz nje smo
`r hr_broj(length(s9_asimetricni_obuhvat), 0)` puta izvukli po 20 osoba i svaki
put izračunali isti interval za sredinu. Poznatu populacijsku sredinu
obuhvatilo je `r hr_broj(sum(s9_asimetricni_obuhvat), 0)` intervala, odnosno
`r hr_broj(100 * mean(s9_asimetricni_obuhvat), 1)` %. U malom
uzorku iz takve raspodjele normalno približenje i procjena standardne
pogreške nisu dovoljno pouzdani da bi postupak postigao zadanu razinu od 95 %.

U prethodnoj simulaciji povjerenja, s po dvjesto osoba, dobili smo obuhvat
blizak zadanoj razini, ali podudaranje nije savršeno. Dobiveni obuhvat približan je iz dvaju razloga. U konačnom broju simulacija
udio pogodaka slučajno se mijenja. Osim toga, nepoznatu populacijsku
raspršenost procjenjujemo iz uzorka, što donosi dodatnu nesigurnost. Pri
dvjesto osoba ona je mala, a pri dvadeset može biti važna. U poglavlju o
dvjema grupama uvest ćemo postupak koji zbog toga širi interval u malim
uzorcima.

Obuhvat od `r paste0(hr_broj(s9$pokrivenost, 1), " %")` ne govori koji su pojedinačni intervali pogodili cilj.
Svaki izračunati interval ili sadrži populacijsku vrijednost ili je ne sadrži.
U frekventističkom postupku parametar je fiksan, a slučajan je uzorak iz
kojega računamo granice. Zato razinu pouzdanosti ne tumačimo kao vjerojatnost
da fiksni parametar leži unutar upravo opaženih granica.

Možemo to zamisliti kao bacanje obruča na kolac. Kolac stoji na istom mjestu,
a obruči padaju na različita mjesta. Razina pouzdanosti opisuje koliko često
obruč obuhvati kolac kroz mnogo bacanja. Nakon pojedinoga bacanja pogodak je
već određen, čak i ako ga ne možemo vidjeti.

Iz objavljenog intervala možemo čitati koje su vrijednosti uskladive s
podacima pod pretpostavkama postupka. Njegova širina pokazuje i jesmo li
postigli željenu preciznost, primjerice marginu manju od deset minuta. Za pitanje o razlici ili promjeni trebamo interval za samu razliku. Predviđanje rezultata sljedećeg istraživanja zaseban je zadatak jer će ono imati vlastiti uzorak i vlastiti interval.

## Interakcija — Hvatač intervala

Za prikaz intervala prelazimo na zaseban normalni model sa sredinom
nula i poznatom standardnom devijacijom jedan. Pojedinačno opažanje sada
je umjetno generirani broj, bez jedinice povjerenja. Iz svakog skupa od
40 neovisnih brojeva računamo sredinu i oko nje raspon
$1,96/\sqrt{40}$ na svaku stranu. Tiskani prikaz ponavlja to 50 puta.
Ovdje je standardna pogreška poznata iz modela, za razliku od prethodnog
računa u kojem smo je procjenjivali iz uzorka.

Na slici su intervali iz ponovljenih uzoraka poredani jedan ispod drugoga.
Okomita crta označuje populacijsku vrijednost. Intervali koji je sijeku
obuhvaćaju cilj. U tablici zatim uspoređujemo veličinu uzorka i razinu
pouzdanosti. Obje utječu na širinu, a razina pouzdanosti određuje i dugoročnu
učestalost obuhvata.

*Slika. Intervali iz ponovljenih simuliranih uzoraka oko fiksne populacijske sredine. Istaknuti intervali promašuju okomitu ciljnu crtu.*

**Što isprobati.**

1. Zadržite pedeset intervala i prebrojite one koji ne sijeku okomitu ciljnu crtu.
2. Povećajte broj intervala na sto bez promjene veličine uzorka ili razine pouzdanosti.
3. Usporedite širinu intervala pri uzorcima veličine dvadeset i sto.
4. Promijenite razinu pouzdanosti s devedeset na devedeset i devet posto te opišite odnos širine i obuhvata.

### Tiskane postavke za vježbu

Tri prikazane postavke koriste normalnu populaciju sa sredinom nula i
standardnom devijacijom jedan. Svaka sadrži pedeset intervala iz istoga
zadanog simulacijskog niza. A i B razlikuju se samo po razini pouzdanosti, a A
i C samo po veličini uzorka.

*Slika. Tri fiksne postavke za usporedbu širine i promašaja intervala u tiskanom izdanju. Izrada autora.*

Za zasebnu računsku provjeru na kraju poglavlja trebat će nam i sažetak cijele
poznate sintetičke populacije po glavnom izvoru vijesti. Sljedeća tablica
čuva točne cjelobrojne brojnosti i zbroj za portal, dok su udio i prosjek
zaokruženi na pet decimala. Iz tih ćemo brojeva provjeriti dva dijeljenja.
Provjera ne potvrđuje kako su pojedinačni zapisi zbrojeni. Taj je dodatni
korak moguć u dobrovoljnoj mrežnoj vježbi. Podaci služe vježbi i ne opisuju stvarne stanovnike.

*Slika. Brojnici, nazivnici i agregatne vrijednosti za portal u sintetičkoj populaciji. Izrada autora prema javnom agregatnom prikazu sintetičkih podataka.*

## Preciznost nasuprot pouzdanosti

Za sljedeću usporedbu širina vraćamo se ocjenama povjerenja iz medijske
populacije. Za svaku veličinu 50, 200 i 800 izvlačimo 400 novih uzoraka,
računamo njihove intervale istim postupkom sa standardnom pogreškom iz
uzorka i prosječimo 400 širina. Usporedba razina 90 %, 95 % i 99 % potom
zadržava jedan isti početni uzorak od 200 osoba i mijenja samo množitelj.

Dvije usporedbe iz prikaza sada možemo razdvojiti i brojčano. Veći uzorak
smanjuje standardnu pogrešku i sužava interval pri istoj razini
pouzdanosti. Prosječna širina intervala pri pedeset osoba iznosi `r hr_broj(s9$sirine[["50"]], 2)`
boda, pri dvjesto `r hr_broj(s9$sirine[["200"]], 2)`, a pri osamsto `r hr_broj(s9$sirine[["800"]], 2)`. S više podataka dobivamo
precizniju procjenu.

Povećanje razine pouzdanosti djeluje drukčije. Na istim podacima tražimo češći
obuhvat, pa raspon mora biti širi. U našem uzorku interval od 90 % širok je
`r hr_broj(s9$razine[["90"]], 2)` boda, interval od 95 % `r hr_broj(s9$razine[["95"]], 2)`, a interval od 99 % `r hr_broj(s9$razine[["99"]], 2)`. Viši zahtjev za obuhvat ovdje plaćamo širim rasponom, odnosno manjom preciznošću.

**Preciznost** opisuje širinu procjene, a **pouzdanost** odabranu dugoročnu
učestalost obuhvata. Za isti postupak i razinu pouzdanosti više podataka
obično daje uži interval. Za iste podatke viša razina pouzdanosti daje širi
interval. U knjizi najčešće koristimo 95 %, no to je uobičajen izbor koji
treba navesti uz rezultat.

Širok interval može biti primjeren opis maloga uzorka ili jako raspršenih
podataka. Uzak interval također treba provjeriti. Ako je uzorak pristran,
interval može biti uzak oko pogrešne vrijednosti jer ne obuhvaća pristranost
postupka odabira.

Na grafu s više skupina intervali pokazuju koliko su njihove procjene
precizne. Širina ovisi i o broju opažanja i o njihovoj raspršenosti. Takav
graf govori više od prikaza samih prosjeka, ali za tumačenje razlika među
skupinama treba još jedan korak.

Nepreklapanje usporedivih intervala može upućivati na razliku, ali preklapanje
ne dokazuje jednakost. Tumačenje ovisi i o nacrtu istraživanja te o tome jesu
li procjene povezane. Najizravnije je izračunati interval za samu razliku. To
ćemo učiniti u poglavlju o dvjema grupama. Ni iz takve usporedbe ne dobivamo
vjerojatnost da je razlika „stvarna”.

Treba razlikovati i nesigurnost prosjeka od raspršenosti pojedinačnih
vrijednosti. Interval za sredinu u uzorku od 200 osoba širok je
`r hr_broj(s9$gornja - s9$donja, 2)` boda. Ako su ocjene približno normalno raspoređene, raspon sredine
plus ili minus 1,96 uzoračkih standardnih devijacija opisivao bi oko 95 %
pojedinačnih ocjena. Taj je raspon širok približno `r hr_broj(2 * s9$normalni_poluraspon, 1)` boda. Normalno
pravilo ne daje takav obuhvat za izrazito asimetrične, ograničene ili
diskretne raspodjele. Taj opisni raspon nije ni interval predviđanja za novu
osobu, jer ne uključuje nesigurnost procjene središta i raspršenosti niti
određuje populaciju buduće osobe. Veći uzorak sužava interval za sredinu, dok razlike među ljudima ostaju svojstvo populacije.

*Slika. Interval pouzdanosti za sredinu i opisni raspon po normalnom pravilu za pojedinačne ocjene na istom uzorku i istoj osi. Izrada autora. Podaci i postupak opisani su u tekstu.*

U PISA-inoj tablici prirodoslovne pismenosti za Hrvatsku je objavljena
procjena od 483 boda, uz 95-postotni interval od 478 do 487 bodova i
raspon mjesta od osamnaestoga do trideset petoga među sudionicama
istraživanja ({OECD}, 2023). Taj raspon mjesta uzima u obzir nesigurnost
procjena i višestruke usporedbe zemalja sličnih rezultata
({OECD}, 2023). Iz njega možemo vidjeti zašto jedno precizno ispisano
mjesto prenosi više sigurnosti nego što je imamo. Raspon se odnosi na
položaj procijenjenoga nacionalnog prosjeka. Za iskustvo pojedinoga
učenika trebali bismo pogledati i razlike unutar zemlje.

Kad bismo pripremali naslov o tim rezultatima, uz procjenu bismo zadržali
njezinu nesigurnost i imenovali područje koje je ispitano. PISA pritom
koristi složen uzorak škola i učenika te postupke procjene postignuća
koje račun nesigurnosti mora uvažiti ({OECD}, 2023). Ovdje čitamo
objavljene rezultate. Jednostavno ponovno izvlačenje pojedinačnih
redaka, koje ćemo sada upoznati na našim simuliranim podacima, ne bi
sačuvalo taj istraživački nacrt.

## Bootstrap kao vlastiti izum

Za sredinu imamo jednostavnu formulu standardne pogreške. Za medijan, razliku
percentila ili omjer račun može biti složeniji ili zahtijevati dodatne
pretpostavke. Tada nam može pomoći ponovno uzorkovanje opaženih podataka.

Kad bismo mogli uzimati nove uzorke iz populacije, izračunali bismo medijan u
svakome i promatrali koliko se mijenja. Budući da imamo samo jedan uzorak,
pokušavamo ponoviti taj postupak izvlačenjem iz njegovih vrijednosti. Uzorak
pritom mora razumno predstavljati ciljnu populaciju. Jednostavno ponovno
uzorkovanje redaka pretpostavlja neovisne i međusobno zamjenjive jedinice na
razini uzorkovanja. Ako su podaci upareni, grupirani ili ponovljeni, čuvamo tu
strukturu i izvlačimo cijele parove, skupine ili osobe. Pod tim uvjetima novi
uzorci iste veličine približno oponašaju promjene koje bi nastale ponovnim
uzorkovanjem iz populacije.

Izvlačimo **s vraćanjem**. Bez vraćanja bismo iz uzorka od šezdeset osoba
dobili istih šezdeset osoba u drugom redoslijedu, pa bi medijan uvijek bio
jednak. S vraćanjem neke osobe ulaze više puta, a neke izostanu. Zbog promjene
sastava mijenja se i procjena. Taj postupak zovemo **bootstrap**. Uveden je za
procjenu nesigurnosti kada teorijski račun nije lako dostupan (Efron, 1979).

Percentilni bootstrap interval uzima odabrane percentile ponovljenih
procjena. Njegova je primjena najjednostavnija kada bootstrap raspodjela
dobro oponaša raspršenost procjenitelja, bez izražene pristranosti ili
asimetrije. Postoje i drugi bootstrap intervali koji korigiraju pomak ili
asimetriju. Ovdje učimo samo najjednostavniji percentilni postupak. Ni taj postupak ne jamči točno zadanu razinu obuhvata.
Mali ili diskretni uzorci, pristranost procjenitelja i vrlo asimetrične
raspodjele mogu oslabiti približenje. Ponavljanje odabira iz postojećih
redaka ne dodaje ljude koji su sustavno izostali iz početnog uzorka.

Sada uzimamo novi početni uzorak od 60 osoba iz iste medijske populacije.
Izvlačimo ga zasebno od prethodnih 200 osoba, a pratimo dnevne minute umjesto povjerenja. U lijevoj polovici tablice vidimo prvih osam zapisa toga
uzorka, a u desnoj prvih osam izvlačenja iz prvoga bootstrap uzorka.
Broj retka desno upućuje na zapis u cijelom početnom uzorku od 60 osoba.
Svako ponavljanje broja retka upućuje na ponovljen odabir iste osobe.

*Slika. Početak izvornog uzorka i prvoga ponovnog uzorka. Svaki puni uzorak ima 60 zapisa. Izrada autora.*

Prvo ponovno izvlačenje uzima redak `r s9_prvi_i[1]`, pa prenosi njegovih
`r s9_mali$minute_medija[s9_prvi_i[1]]` minuta. Nakon svih 60 izvlačenja
imamo `r length(unique(s9_prvi_i))` različitih osoba, a medijan cijeloga
ponovnog uzorka iznosi `r hr_broj(s9_boot_medijan[1], 1)` minuta. Taj jedan
broj ulazi u sljedeći histogram. Postupak 4 000 puta počinje od istoga
početnog uzorka, svaki put s novim izvlačenjem s vraćanjem. Sva su
ponavljanja definirana. Poredamo 4 000 medijana i uzmemo percentile 2,5 i
97,5, ostavljajući približno 100 vrijednosti sa svake strane.

U uzorku od 60 osoba medijan dnevnog praćenja medija iznosi `r hr_broj(s9$medijan_uzorak, 1)`
minuta. Iz četiri tisuće bootstrap uzoraka dobivamo središnji percentilni
raspon od `r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta. On obuhvaća poznati populacijski
medijan od `r hr_broj(s9$medijan_pop, 1)` minuta. Na slici vidimo kako nastaje raspon iz jednoga
uzorka. Za provjeru dugoročnog obuhvata trebali bismo ponavljati cijeli
postupak s novim početnim uzorcima.

*Slika. Raspodjela četiri tisuće bootstrap medijana iz jednog uzorka, s granicama središnjih 95 % vrijednosti i pravom populacijskom vrijednošću. Izrada autora. Podaci i postupak opisani su u tekstu.*

Histogram je stubast jer medijan maloga, zaokruženog uzorka može poprimiti
samo ograničen broj vrijednosti. Zato su i granice percentilnog raspona grube.
Više bootstrap ponavljanja smanjuje računalno kolebanje percentila, ali ne
nadoknađuje vrijednosti koje nedostaju u početnom uzorku.

Bootstrap ne zahtijeva da unaprijed imenujemo oblik populacijske raspodjele,
no način izvlačenja mora odgovarati statistici i nacrtu istraživanja. Za
korelaciju izvlačimo cijele parove vrijednosti. Za razliku neovisnih skupina
uzorkujemo svaku skupinu zasebno. Kod ovisnih podataka izvlačimo cijele
neovisne jedinice. Postupak ne može dodati rijetke ili krajnje vrijednosti
kojih u uzorku nema. Zato su vrlo visoki percentili posebno osjetljivi na male
uzorke i teške repove. Medijan manje ovisi o repovima, ali mnogo jednakih
vrijednosti može dati grube granice. Bootstrap također ne uklanja
nereprezentativnost početnog uzorka.

### Kodirani udio i dvije nesigurnosti

U poglavlju o povezanosti promjena pravila kodiranja promijenila je oznake
istih naslova. Ponovno izvlačenje tih naslova ne bi samo po sebi provjerilo
to pravilo. Kod udjela dobivenog kodiranjem teksta zato razlikujemo barem dva izvora
nesigurnosti. **Uzoračka nesigurnost** odnosi se na odabir tekstova.
**Nesigurnost kodiranja** odnosi se na pravila razvrstavanja, rubne slučajeve
i odluke kodera ili klasifikatora. Ako kodirana kategorija samo približno
odgovara istraživačkom pojmu, trebamo razmotriti i nesigurnost mjerenja.

Bootstrap redaka s gotovim oznakama mijenja sastav tekstova, ali zadržava
njihove oznake. Uz ispravno odabranu jedinicu ponovnog uzorkovanja opisuje
uzoračku nesigurnost. Valjanost kodiranja zahtijeva zasebnu provjeru oznaka i pravila. Drugo opravdano
pravilo moglo bi promijeniti oznake rubnih tekstova i pomaknuti procijenjeni
udio, čak i kada oba izračuna daju uske intervale. U izvještaju zato navodimo
jedinicu teksta, ciljnu populaciju, način odabira i pravilo kodiranja te
objašnjavamo koju nesigurnost interval uključuje.

**Statistika u divljini.**
**Šest tvrdnji o jednom intervalu.** Istraživač može uredno
izračunati interval, a ipak pogrešno objasniti što iz njega slijedi.
U istraživanju razumijevanja intervala studenti i istraživači
prosuđivali su šest tumačenja rezultata iz zamišljenog istraživanja
(Hoekstra, 2014). Sve su tvrdnje bile netočne, ali su ih obje skupine
u prosjeku prihvatile više od tri (Hoekstra, 2014). Pogreška se
dogodila pri čitanju rezultata, nakon što je račun već bio zadan.

Razmotrimo vlastiti zamišljeni primjer. Studentska anketa treba
procijeniti prosječno vrijeme putovanja na fakultet. U izvještaju
stoji 95-postotni interval od 30 do 40 minuta. Autor bi mogao
napisati da se unutar njega nalazi vrijeme putovanja 95 % studenata.
Time bi raspon nesigurnosti procijenjenog prosjeka pretvorio u opis
razlika među ljudima. Podaci o pojedinačnim putovanjima mogli bi
biti mnogo raspršeniji.

Drugo bi iskušenje bilo napisati da je nakon ovog računa
vjerojatnost položaja prave sredine između granica jednaka 95 %.
U frekvencijskom postupku koji smo učili razina pouzdanosti pripada
postupku ponovljenog uzorkovanja. Ako njegove pretpostavke vrijede,
približno taj udio tako dobivenih intervala obuhvaćao bi pravu
sredinu. Ne raspoređujemo vjerojatnost nepoznate sredine unutar
ovoga već izračunatog intervala.

Za čitatelja studentskog izvještaja ta razlika ima praktičnu
posljedicu. Interval prosjeka može pomoći da procijeni tipično
opterećenje putovanjem, ali ne govori koliko studenata putuje
izrazito dugo. Za odluku o pomoći tim studentima trebala bi
raspodjela pojedinačnih vremena i prag koji za tu odluku ima smisla.

Autor zato treba imenovati veličinu koju procjenjuje i objasniti
koju nesigurnost interval opisuje. U našem primjeru to je
nesigurnost procjene prosječnog vremena pod uvjetima odabranog
postupka. Prije pisanja zaključka zato razdvajamo nesigurnost prosjeka od razlika među pojedinačnim putovanjima. Razinu pouzdanosti pritom vežemo uz dugoročni obuhvat postupka, uz fiksnu nepoznatu populacijsku sredinu.

**Nađite grešku.**
Vraćamo se uzorku od šezdeset osoba iz simuliranoga grada. Želimo
procijeniti populacijski medijan dnevnog vremena uz medije. Vektor
`minute` sadrži njihove pojedinačne vrijednosti, a osobe su uzorkovane
neovisno. Asistent je vratio račun percentilnog bootstrap intervala.

Izračunani medijan uzorka iznosi `r hr_broj(median(s9_mali$minute_medija), 1)`
minuta, a granice intervala
`r hr_broj(quantile(s9_boot_medijan, .025), 0)` i
`r hr_broj(quantile(s9_boot_medijan, .975), 0)` minuta. To su rezultati
nastavne simulacije. Uz njih stoji asistentovo objašnjenje.

> U svakom ponavljanju uzorkujemo s vraćanjem isti broj osoba i računamo
> medijan. Granice izdvajaju središnjih 95 % bootstrap medijana.
> Zato postoji 95 % vjerojatnosti da je fiksni populacijski medijan
> između upravo dobivenih granica.

Napišite zamjensko objašnjenje za čitatelja izvještaja. Zadržite
procjenu, granice i opis ponavljanja, a razinu od 95 % povežite s onim
čemu ona pripada. Navedite što bi se mijenjalo kad bismo uzeli novi
uzorak iz iste populacije.

## Razrađeni primjer

Zamislimo naručitelja koji želi procijeniti koliko vremena dnevno odrasli
stanovnici grada provode uz medije i koji traži marginu ne veću od deset
minuta. Za vježbu tog zadatka koristimo već uvedeni uzorak od 60 osoba iz
simuliranoga grada. Trebamo povezati izbor mjere s njegovim pitanjem, a zatim
provjeriti daje li uzorak traženu preciznost.

Najprije biramo mjeru koja odgovara pitanju. Dnevne minute imaju dug rep prema
velikim vrijednostima, koji povlači prosjek prema gore. Za opis uobičajene
osobe zato biramo medijan. Budući da za njegovu standardnu pogrešku nemamo
jednako jednostavan račun kao za sredinu, nesigurnost ćemo procijeniti
bootstrapom.

Postupak je sličan simulaciji iz prethodnog poglavlja. Ovaj put izvlačimo iz
opaženog uzorka, s vraćanjem, i u svakom ponavljanju računamo medijan.

Poziv `sample` uz argument `replace` mijenja sastav ponovnog
uzorka tako što dopušta višekratni izbor iste osobe. Nakon računanja medijana u
svakom ponavljanju, funkcija `quantile` određuje granice odsijecanjem
zadanog udjela raspodjele sa svake strane. Tako kod povezuje ponovno izvlačenje
s trima već prikazanim vrijednostima, medijanom uzorka i granicama njegova
bootstrap raspona.

Za odrasle stanovnike simuliranoga grada procjenjujemo medijan dnevnog
praćenja medija na `r hr_broj(s9$medijan_uzorak, 1)` minuta. Jedinica je jedna osoba. Percentilni
bootstrap raspon od 95 % ide od `r hr_broj(s9$boot_donja, 1)` do `r hr_broj(s9$boot_gornja, 1)` minuta i pod navedenim
uvjetima opisuje uzoračku promjenjivost medijana. Ukupna širina iznosi
`r hr_broj(s9$boot_gornja - s9$boot_donja, 0)` minuta. Udaljenost od procjene
do donje granice iznosi `r hr_broj(s9$medijan_uzorak - s9$boot_donja, 1)`,
a do gornje `r hr_broj(s9$boot_gornja - s9$medijan_uzorak, 1)` minuta.
Veća od tih udaljenosti prelazi traženih deset minuta. Trebamo izvijestiti o toj
nepreciznosti ili prikupiti dodatne informacije. Iz raspona ne zaključujemo o
promjeni. Kada uzorak ne bi predstavljao ciljnu populaciju, rezultat bismo
ograničili na opis uzorka.

U simulaciji znamo da populacijski medijan iznosi `r hr_broj(s9$medijan_pop, 1)` minuta i da je
unutar dobivenih granica. Jedan pogodak ipak ne provjerava pouzdanost
postupka. Ranijih deset tisuća ponavljanja odnosilo se na normalni interval za
sredinu. Za provjeru bootstrap raspona medijana morali bismo svaki put izvući
novi uzorak od 60 osoba, iz njega izračunati novi bootstrap raspon i
prebrojiti obuhvate populacijskog medijana. To ovdje nismo učinili, pa prikaz
ne dokazuje zadanu razinu obuhvata.

U izvještaju najprije navodimo procjenu, njezin raspon nesigurnosti i
ograničenja. Ovdje trebamo reći da su
podaci simulirani, da procjenjujemo medijan i da raspolažemo sa šezdeset
osoba. Isti oblik izvještaja koristimo u stvarnom istraživanju, iako ondje
obično ne znamo parametar s kojim bismo usporedili rezultat.

## Od procjene do tvrdnje

Procjenu i širinu raspona već smo izračunali, ali naručitelju trebamo objasniti
i na koga se rezultat odnosi. Šest pitanja u tablici povezuje naš račun s
odabirom osoba, mjerenjem minuta i zahtjevom za preciznošću. Tako vidimo koje
bi ograničenje moglo promijeniti konačnu rečenicu.

| Revizijsko pitanje | Primjena na bootstrap medijana |
|---|---|
| Koja je jedinica? | jedna zamišljena odrasla osoba s jednim zapisom dnevnih minuta |
| Tko ili što nedostaje? | uzorak je slučajno izvučen iz poznate sintetičke populacije, pa ne predstavlja stvarni grad ni osobe izvan te populacije |
| Koji je cilj tvrdnje? | populacijski medijan dnevnih minuta, opisan procjenom i rasponom uzoračke nesigurnosti |
| Gdje je neizvjesnost? | promjene sastava uzorka. Ne provjerava dugoročni obuhvat, mjerenje minuta ni prijenos na stvarne stanovnike |
| Koje drugo objašnjenje ostaje? | u stvarnoj anketi slab obuhvat, neodgovor ili pogrešno mjerenje mogli bi objasniti pomak procjene. Bootstrap takve izvore pogreške ne uklanja |
| Tko snosi posljedice? | ovdje nema stvarnih sudionika. U stvarnom projektu pretjerana preciznost mogla bi zavesti naručitelja i stanovnike |

: Šest revizijskih pitanja primijenjenih na procjenu iz simulirane populacije. Izrada autora.

Ti odgovori ograničavaju zaključak na ono što smo doista procijenili.
Sintetički podaci služe provjeri postupka u zadanom modelu. Uzorački interval opisuje promjenjivost zbog odabira, dok nesigurnost mjerenja ili kodiranja treba zasebno procijeniti. Karta tvrdnji u nastavku
pokazuje šest različitih dosega analize.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje medijan i raspodjelu minuta u opaženom sintetičkom uzorku |
| povezanost | nije poduprta jer primjer ne uspoređuje dvije varijable |
| generalizacija | usmjerena je na poznatu sintetičku populaciju pod postupkom slučajnoga odabira, bez prava prijenosa na stvarni grad |
| predviđanje | nije poduprto jer nije izgrađeno ni provjereno pravilo za nova opažanja |
| uzročnost | nije poduprta jer nema intervencije ni usporedbe mogućih ishoda |
| odluka | poduprta je odluka da raspon ne ispunjava unaprijed zadanu marginu od najviše deset minuta, ali ne tvrdnja o promjeni ni odluka o medijskoj politici |

: Šest dimenzija tvrdnje na granici Dijela III. Izrada autora.

Na kraju ovoga dijela provjerite možete li odgovoriti na četiri pitanja. Zašto
među pedeset simuliranih intervala ne mora biti točno pet posto promašaja?
Zašto bootstrap gotovih oznaka ne uključuje nesigurnost kodiranja? Što trebamo
navesti uz procjenu i zašto najprije imenujemo populaciju? Zašto povećanje
prigodnog uzorka ne uklanja razliku između ljudi koji su u njega mogli ući
i ciljne populacije?

Tablica provjere pokazuje što smo tražili od asistenta, što je vratio i kako
smo provjerili rezultat. Možemo je pročitati i bez pisanja koda.

| Polje računa | Bootstrap medijana |
|---|---|
| Što je traženo | procijeniti populacijski medijan dnevnih minuta i njegovu uzoračku nesigurnost iz uzorka neovisnih osoba |
| Što je vraćeno | točkasta procjena te donja i gornja granica središnjega percentilnog raspona |
| Što je provjereno | puna veličina ponovnog uzorka, izvlačenje s vraćanjem, ista statistika u svakom ponavljanju i redoslijed izvještavanja |
| Kako je provjereno | čitanjem poziva `sample`, `median`, `replicate` i `quantile` te usporedbom ispisa s brojkama u prozi |
| Uloga AI-ja | instrument i pogrešiv analitičar |
| Što je ostalo neprovjereno | dugoročni obuhvat percentilnoga postupka za medijan, reprezentativnost u stvarnom istraživanju i valjanost mjerenja minuta |
| Odgovorna osoba | osoba koja odabire procjenjivanu količinu, provjerava račun i potpisuje zaključak |

: Čitljiv račun provjere za procjenu iz Dijela III. Izrada autora.

## Sažetak

Točkasta procjena postaje informativnija kada uz nju prikažemo interval i
objasnimo koju nesigurnost on obuhvaća. Razina pouzdanosti opisuje dugoročni
obuhvat postupka, pa viša razina na istim podacima širi interval, dok ga veći
uzorak obično sužava. Kada nemamo jednostavnu formulu, bootstrapom ponovno
izvlačimo iz opaženoga uzorka i procjenjujemo uzoračku promjenjivost, čuvajući
jedinicu i strukturu nacrta. Time ne popravljamo premalen ili pristran uzorak,
a pri ponovnom izvlačenju gotovih oznaka teksta ne uključujemo nesigurnost
kodiranja ili mjerenja. U izvještaju zato povezujemo ciljnu populaciju i
jedinicu s procjenom, mjernom jedinicom, intervalom i ograničenjima. U
poglavlju o testiranju toj procjeni pridružujemo drugo pitanje, koliko bi
opaženi rezultat bio neobičan pod određenom pretpostavkom.

## Pojmovi

točkasta procjena (*point estimate*), kritična vrijednost (*critical value*),
obuhvat intervala (*coverage*),

procjena (*estimate*), interval pouzdanosti (*confidence interval*), razina
pouzdanosti (*confidence level*), margina pogreške (*margin of error*),
preciznost (*precision*), bootstrap (*bootstrap*), percentilni raspon
(*percentile interval*), jedinica ponovnog uzorkovanja (*resampling unit*),
nesigurnost kodiranja (*coding uncertainty*)

## Zadaci

Nakon vlastitog pokušaja otvorite naznake i provjere rješenja.

### Konceptualni

Objasnite zašto razina pouzdanosti pripada postupku, a ne nepoznatom parametru
nakon izračuna intervala. U objašnjenju navedite što je u postupku slučajno, a
što fiksno, zašto ta podjela isključuje rečenicu o vjerojatnosti da parametar
leži unutar zadanih granica te zašto bootstrap gotovih oznaka teksta ne
obuhvaća nesigurnost pravila kodiranja. Predajte jedan odlomak.

### Računski

Najprije razlikujte točkastu procjenu, standardnu pogrešku i marginu pogreške.
U ranijem uzorku od 200 osoba prosjek povjerenja iznosi 4,815, a standardna
devijacija zaokruženo 2,093 boda. Iz tih vrijednosti izračunajte standardnu
pogrešku, marginu $1,96 \cdot SE$ i obje granice približnoga 95-postotnog
intervala. Jednom rečenicom protumačite čemu pripada razina od 95 %.

Za ručnu demonstraciju bootstrapa uzmite prvih pet već prikazanih vrijednosti
dnevnih minuta, 83, 82, 134, 139 i 164. Zadajemo ponovno izvlačenje redaka
1, 1, 2, 4 i 5. Zapišite dobivene vrijednosti i usporedite njihov medijan s
medijanom početnih pet vrijednosti. Objasnite zašto jedno takvo izvlačenje
još ne daje interval pouzdanosti.

U tiskanoj tablici s trima postavkama najprije promotrite samo veličinu uzorka
i razinu pouzdanosti. Predvidite poredak širina i dugoročni obuhvat.
Izračunajte širine kao $2z^*/\sqrt{n}$ i usporedite ih s tablicom. Očitajte
promašaje i objasnite zašto njihov manji broj u C nego u A ne znači višu
razinu pouzdanosti. Iz agregatne tablice podijelite broj korisnika portala
ukupnim brojem osoba, a zbroj njihova povjerenja brojem korisnika portala.
Predajte predviđanje, usporedbu s rezultatima, tri računa širine i dva
dijeljenja uspoređena s objavljenim vrijednostima. Objasnite zašto iz agregata
možemo provjeriti račun, ali ne potvrditi kako su pojedinačni zapisi zbrojeni.

Za dobrovoljnu provjeru pojedinačnih zapisa mrežni dodaci A i B pokazuju
kako otvoriti `data/populacija-medija.csv` i usporediti isti podskup s
agregatom. Ta provjera nije uvjet tiskanoga zadatka.

### Kritički

Vratite se prikazu Istraživač margine pogreške u poglavlju o tome kako
brojke zavode. Usporedite stanje s uzorkom od 1000 osoba bez pristranosti i
stanje s jednakim uzorkom te pristranošću od šest postotnih bodova. Oba
pokazuju procjenu od 52 %. Primijenite karticu za čitanje ankete iz poglavlja o mjerenju i
sadašnje znanje o intervalima. Objasnite zašto ista uska margina pogreške ne
može obuhvatiti pristranost odabira, navedite koji je izvor nesigurnosti unutar,
a koji izvan intervala te napišite ispravljenu tvrdnju za pristrano stanje.
Predajte usporedbu dvaju stanja i ispravljenu tvrdnju.

### Revizija modela

Pročitajte račun iz okvira o pogrešci. Za svaki od poziva `replicate`,
`sample`, `median` i `quantile` jednom rečenicom povežite redak koda s pojmom
koji provodi. Zatim izdvojite jedinu pogrešnu rečenicu i napišite
frekventistički ispravnu zamjenu koja zadržava razinu od 95 %, procjenu i
granice intervala. Kod ne treba prepisivati ni mijenjati.
