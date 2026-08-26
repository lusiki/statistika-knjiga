# Kako brojke zavode

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/03-kako-brojke-zavode.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-26 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 20 min | Istraživač margine pogreške | DIP 2024. (portal) · simulacija | pogl. 1 i 2 |

**Vinjeta.**
Službeno izvješće o izborima za Hrvatski sabor 2024. prikazuje ukupan odaziv
od 62,30 % (Hrvatske}, 2024). Brojnik je 2.216.763 birača koji su pristupili
glasovanju, a nazivnik 3.558.089 birača na obrađenim biračkim mjestima
(Hrvatske}, 2024).
Broj je točno prepisan i račun se slaže s objavom.

U istom izvješću stoji 2.154.733 važećih i 60.476 nevažećih listića
(Hrvatske}, 2024). Njihov je zbroj 2.215.209, dakle 1.554 manje od broja
 pristupilih (Hrvatske}, 2024). Rečenica „glasovalo je
62,30 % birača” zato skriva odluku (Hrvatske}, 2024). Govorimo li o
pristupanju glasovanju ili o biračima prema glasačkim listićima?

Kako javnu brojku provjeriti prije nego što joj naslov podari značenje koje
izvor ne daje?

## Od točnoga broja do potpune tvrdnje

Izvor DIP-a nije novinski sažetak ni preslika na društvenoj mreži. Riječ je o
službenom *Izvješću o provedenim izborima za zastupnike u Hrvatski sabor 2024.*
(Hrvatske}, 2024). Stranica 124 nosi tablicu „Odaziv birača” (Hrvatske}, 2024).
Službeni put i tablica pregledani su dana 5. kolovoza 2026. (Hrvatske}, 2024). Knjiga
nije preuzela ni pohranila izbornu datoteku.
Portalna dostupnost nije dokaz prava na njezinu redistribuciju.

Ta napomena nije administrativni ukras. Ona čitatelju govori tko je objavio
broj, koja je objava pregledana i gdje ga može ponovno pronaći. Tvrdnja bez
takva traga možda je točna, ali se iz same tvrdnje ne može neovisno provjeriti;
provjeravatelj mora pronaći drugi pouzdan put do izvora.

Isti službeni prikaz sadrži pet brojčanih veličina koje se lako stope u jednu
riječ „birači” (Hrvatske}, 2024). Njihove oznake čuvaju različite dijelove
postupka.

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

Druga provjera daje drukčiji račun.

$$
2\,154\,733 + 60\,476 = 2\,215\,209.
$$

Oba su računa točna. Službene oznake opisuju različite operativne faze, pa broj
prema listićima ne nazivamo brojem pristupilih. Razlika od 1.554 tu razliku
čini brojčano vidljivom, ali ne dokazuje kvar u evidenciji niti objašnjava
njegov uzrok (Hrvatske}, 2024). Čak ni jednaki ukupni brojevi ne bi dvije
oznake pretvorili u sinonime.

Put od tablice do naslova ima nekoliko preobrazbi. Izvor najprije objavljuje
polja s vlastitim oznakama. Autor zatim bira brojnik i nazivnik, računa omjer te
mu u rečenici pridružuje glagol i skupinu ljudi. Podaci se u tom nizu ne
moraju promijeniti, a značenje se može promijeniti na svakom koraku. Revizija
zato ne pita samo je li dijeljenje točno. Ona pita kojim su odlukama dva polja
postala javna tvrdnja.

Za odaziv je trag dostatan ovoj omeđenoj portalnoj provjeri. Vodi od datiranoga
izvješća i službenih oznaka, preko nacionalnih zbrojeva i omjera, do rečenice
koja kaže „pristupilo” (Hrvatske}, 2024). Kad asistent vrati samo 62,30 %
(Hrvatske}, 2024), završni je broj
ponovljiv, ali
njegovo značenje nije. Drugi čitatelj ne može znati koji je brojnik odabran ni
je li nazivnik zadržao izvorni obuhvat. Provjerljiv račun zato mora sačuvati i
semantički trag.

## Okvir, os i rijedak ishod

Postotak uvijek nosi pitanje „od čega?”. Odaziv 62,30 % postaje razumljiv tek
uz imenovani nazivnik (Hrvatske}, 2024). Stupac koji prikazuje samo postotak sakrio bi oba
izvorna broja. Graf čija os počinje tik ispod opaženih vrijednosti dodatno bi
uvećao vidljivu razliku među jedinicama. Skraćena os nije automatski nepoštena,
ali njezin raspon mora biti vidljiv i opravdan pitanjem.

Važno je razlikovati postotak od **postotnog boda**. Ako se dvije stope razlikuju
za 0,82 na postotnoj ljestvici, razlika iznosi 0,82 postotna boda
(Hrvatske}, 2024). Relativni
postotni rast postavlja drugo pitanje i traži dijeljenje početnom stopom.
Zamjena tih dvaju izraza mijenja veličinu priče bez promjene ijednog polaznog
broja.

Zamislimo 10.000 zapisa. Njih 100 stvorio je model umjesto bilježenja stvarnog
događaja. To je hipotetska situacija, a ne empirijski nalaz. Provjera pronađe
90 od tih 100 zapisa, ali pogrešno označi i 495 ostalih. Dobiva 585 upozorenja,
od kojih je ispravnih samo 90, približno 15,4 %. Tvrdnja „provjera je pronašla
90 % ciljanih zapisa” zato nije odgovor na pitanje „koliki je udio ispravnih
upozorenja?”.

**Temeljna stopa** jest udio ishoda u relevantnoj populaciji prije nego što se
uzme u obzir novi signal, test ili model.

U prvom je primjeru temeljna stopa 100 od 10.000 zapisa, odnosno 1 %. Taj je
udio postojao prije rezultata provjere i određuje kako čitamo njezino
upozorenje.

Promijenimo samo temeljnu stopu. Ako je među 10.000 zapisa njih 1.000
sintetičkih, ista bi provjera pronašla 900 takvih zapisa i pogrešno označila 450
ostalih. Tada bi bilo ispravno 900 od 1.350 upozorenja, odnosno dvije trećine.
Provjera nije postala tehnički bolja. Promijenila se baza na koju se primjenjuje,
pa se promijenilo i značenje njezina upozorenja.

Pouka nije da treba odbaciti svaku provjeru rijetkog ishoda. Treba razlikovati
koliko često ona nalazi ciljani ishod od toga koliko joj treba vjerovati kada
izda upozorenje. Za drugo pitanje trebamo i stopu pogrešnih upozorenja i
temeljnu stopu. Poglavlje o dobu algoritama vratit će se toj vezi kada
upozorenje postane klasifikacijska odluka s nejednakim posljedicama.

U izbornom izvješću srodnu ulogu ima baza kojoj pripisujemo broj. Udio
nevažećih listića može se računati među listićima, među pristupilima ili među
svim biračima u objavljenom nazivniku. Svaki omjer odgovara na drugo pitanje.

## Anketa, obuhvat i biranje trešanja

DIP-ova tablica sažima administrativni zapis izbora. Ona nije procjena iz
uzorka ispitanika. Nasuprot tomu, anketa pokušava iz odgovora dijela ljudi
zaključivati o široj ciljnoj populaciji. Ista riječ „postotak” ne čini ta dva
dokazna puta jednakima.

Prije čitanja rezultata ankete vrijedi sastaviti početnu karticu provjere. U nju
zapisujemo ciljnu populaciju i okvir iz kojega su ljudi mogli biti dosegnuti,
način regrutacije, broj pozvanih i broj odgovora, datume terena, formulaciju
pitanja, ponderiranje, neodaziv, naručitelja i objavljenu marginu pogreške. Ako
neka stavka nedostaje, bilježimo je kao nepoznatu. Ne popunjavamo je
pretpostavkom.

Administrativni zapis i anketa mogu govoriti o sličnoj temi, ali broj nastaje
drukčijim postupkom. Administrativna tablica nastoji obuhvatiti događaje koji
prema unaprijed utvrđenom operativnom pravilu ulaze u evidenciju. Provjera
takva zapisa obuhvaća pokrivenost, ispravnost zapisa, dosljednost oznaka i
obradbu. Anketa bilježi odgovore
odabranih ljudi. Uz ista pitanja o mjerenju nosi i uzoračku promjenjivost,
okvir, regrutaciju i neodaziv. Te se nesigurnosti ne zbrajaju u jedan opći znak
±.

Velik broj odgovora zato nije zamjena za dobar put od ciljne populacije do
ispitanika. Dobrovoljna internetska anketa može prikupiti mnogo odgovora i
ipak sustavno promašiti ljude koji se razlikuju u onome što mjerimo. Manji
vjerojatnosni uzorak može imati veću uzoračku promjenjivost, ali jasniji doseg.
To još nije teorija uzorkovanja. To je razlog da veličinu uzorka nikada ne
čitamo odvojeno od načina odabira.

Formalna margina pogreške ovdje ostaje najavljeni dug. Widget u nastavku gradi
intuiciju da veličina uzorka mijenja uzoračku promjenjivost, a sustavna
pristranost ne nestaje s većim uzorkom. Poglavlja o uzorkovanju i procjeni
razriješit će uvjete, izračun i tumačenje. Anketa se ne proglašava dobrom samo
zato što uz postotak navodi znak ±.

Službeno izvješće omogućuje neposrednu provjeru izbora obuhvata. Za izborne
jedinice I.–X. zbroj je 2.140.824 pristupilih od 3.482.150 birača, što daje
61,48 % (Hrvatske}, 2024). Za sve jedinice I.–XII. objavljeni je rezultat
62,30 % (Hrvatske}, 2024). Razlika je 0,82 postotna boda (Hrvatske}, 2024).

Obuhvat I.–X. nije neutralna zamjena za službeni ukupni obuhvat. On odgovara na
drugo, unaprijed postavljeno pitanje o tim redcima. Bez sadržajnog razloga za
takvo pitanje služi samo kao dijagnostika učinka odabira. Izabrati podskupinu
tek nakon što vidimo da daje privlačniju stopu bilo bi biranje trešanja.

Isti bi razmak na osi od 0 % do 100 % izgledao skromno, a na osi od 61 % do 63 %
zauzeo bi velik dio prikaza (Hrvatske}, 2024). Skraćena os ne mijenja razliku
od 0,82 postotna boda niti dokazni doseg (Hrvatske}, 2024). Mijenja samo
njezinu vizualnu istaknutost, pa raspon osi mora biti vidljiv i obrazložen.

## Interakcija — Istraživač margine pogreške

Ovdje prelazimo s administrativnog zapisa na konstruiranu anketnu situaciju.
Istraživač računa uobičajenu približnu 95-postotnu marginu za jednostavan
neovisan uzorak. Ne uključuje složen dizajn, ponderiranje, neodaziv ni mjernu
nesigurnost. Zaseban klizač ručno uvodi poznatu sustavnu pristranost, pa se
raspon može sužavati oko pogrešne vrijednosti. Prikaz gradi intuiciju. Ne
izvodi formalnu marginu pogreške i nije dokaz za DIP-ovu tablicu.

*Slika. Približna margina pogreške i položaj pretpostavljene istinite vrijednosti u konstruiranoj anketi.*

**Što isprobati.**

1. Povećavajte uzorak i promatrajte brzinu sužavanja margine.
2. Zadržite uzorak jednakim, a promijenite procijenjeni udio.
3. Uključite sustavnu pristranost i provjerite zašto uži interval ne mora biti
   bliži istini.

U tiskanom izdanju usporedite prvo i drugo stanje da biste vidjeli učinak većega
uzorka. Potom usporedite drugo i treće stanje. Veličina uzorka i procijenjeni
udio ostaju jednaki, ali pretpostavljena istina izlazi iz uskoga intervala kada
se uključi sustavna pristranost. Promjena procijenjenoga udjela zaseban je pokus
dostupan samo u digitalnom izdanju.

Veći uzorak sužava ovako prikazanu uzoračku promjenjivost. Ne pomiče procjenu
prema istini kada je u postupak ugrađena sustavna pristranost. Uži raspon zato
ne jamči točniji odgovor.

## Podrijetlo ljudskog i strojnog broja

**Statistika u divljini.**
**Kada „glasovalo” postane preširoka riječ.** Službena tablica navodi odaziv
62,30 %, uz 2.216.763 pristupilih i nazivnik od 3.558.089 birača na obrađenim
biračkim mjestima (Hrvatske}, 2024). Zasebno, važeći i nevažeći listići daju
2.215.209 birača prema glasačkim listićima (Hrvatske}, 2024).

Naslov „Glasovalo je 62,30 % birača” može biti bezazlena kolokvijalna kratica
za sudjelovanje (Hrvatske}, 2024). Za provjerljivu je tvrdnju ipak nedovoljno
precizan jer briše službenu razliku među brojnicima i skraćuje nazivnik.
Poštenija rečenica glasi ovako.
„Službeno izvješće DIP-a bilježi da je glasovanju pristupilo 2.216.763 od
3.558.089 birača na obrađenim biračkim mjestima, odnosno 62,30 %” [Hrvatske}, 2024,
str. 124]. Ona još ne
govori tko je izašao, zašto je izašao ni za koga je glasovao.

Asistent može brzo provjeriti zbroj, usporediti dva nazivnika i predložiti
oprezniju rečenicu. Ne može vlastitim samopouzdanjem nadomjestiti izvor. Za
svaki broj koji proizvede tražimo pet veza. To su točna objava, ulazni podaci,
transformacija, nazivnik i citat koji zaista vodi do brojke. Ako jedna veza
nedostaje, nedostaje i dio podrijetla tvrdnje.

**Pitajte model.**
Asistentu dajemo točan naslov službene objave, stranicu i pet objavljenih
vrijednosti iz tablice. Tražimo da ne objašnjava razliku od 1.554 bez novoga
izvora te da odvoji provjeru aritmetike od dosega tvrdnje. Nakon odgovora ručno
otvaramo citirani dokument i pronalazimo svaki broj.

> Na temelju stranice 124 priloženog izvješća provjeri tvrdnju o odazivu.
> Odvoji izvor, jedinicu, brojnik, nazivnik, račun, razumno alternativno
> uokvirivanje i dopušten zaključak. Ne objašnjavaj razliku među službenim
> brojnicima ako izvor ne daje objašnjenje. Označi svaku stavku koju ne možeš
> provjeriti.

**Nađite grešku.**
Prema službenom izvješću, 2.154.733 važećih i 60.476 nevažećih listića zbrajaju
se u 2.215.209 birača prema glasačkim listićima (Hrvatske}, 2024). To je
1.554 manje od 2.216.763 pristupilih (Hrvatske}, 2024). Razlika iznosi
približno 0,07 % broja pristupilih (Hrvatske}, 2024), pa je dovoljno
mala da se dvije službene oznake u izvještavanju mogu rabiti kao sinonimi.

Provjera podrijetla ne završava na tablicama. Slika, zvučna snimka ili video
mogu biti sintetički, a istodobno izgledati uvjerljivo. Obrnuto, čudan izgled
nije dokaz da je zapis umjetno nastao. Razdvajamo podrijetlo datoteke,
integritet i poznate preobrazbe zapisa te istinitost tvrdnje o prikazanom
događaju. Dokaz za jedan sud ne zatvara druga dva.

Četiri oznake sprječavaju da nastavno pomagalo postane lažni dokaz.

| Oznaka | Što predmet jest | Što ne smije poduprijeti |
|---|---|---|
| simulacija | podaci proizvedeni poznatim mehanizmom radi učenja postupka | nalaz o stvarnoj populaciji |
| sintetički zapis | umjetno stvoren zapis koji oponaša oblik podatka ili medija | tvrdnju da se prikazani događaj doista zbio |
| hipotetski izlaz modela | uvjetni odgovor izrađen radi provjere zaključivanja | tvrdnju da je određeni sustav taj odgovor stvarno dao u zabilježenoj uporabi |
| izmišljeni dokaz | nepostojeći broj, opažanje ili izvor prikazan kao stvaran | bilo koju empirijsku tvrdnju |

: Četiri vrste dokaznog predmeta i njihove granice. Izrada autora.

Ni detektor sintetičkog sadržaja sam po sebi nije dokaz podrijetla. Njegov je
rezultat novi modelom proizveden broj koji ovisi o podacima za učenje, inačici,
postavkama i pragu. Temeljna stopa ponovno je važna. U zbirci u kojoj je
sintetički sadržaj rijedak i umjerena stopa pogrešnih upozorenja može nadjačati
točna upozorenja. Ocjena detektora zato može otvoriti istragu, ali ne smije
zatvoriti zaključak.

Podrijetlo može biti nepotpuno i kada je zapis autentičan. Preslika zaslona
može izgubiti metapodatke, a izvorna datoteka može biti nedostupna. Obrnuto,
uredni metapodatci ne jamče istinit sadržaj. Neovisna potvrda događaja ne
autentificira određenu datoteku. Tada je pošten ishod „nije provjereno”, a ne
automatski „sintetičko” ili „autentično”. Revizija traži put do prve objave,
bilješku o poznatim preobrazbama i zaseban dokaz za tvrdnju o događaju.

Generirani skup iz računskog zadatka pripada prvom retku. Widget je
konstruirani kalkulator, a ne simulirani dokazni predmet. Kratki pogrešni
odgovor modela pripada trećem retku. DIP-ova tablica nije ni jedno ni drugo.
Ona je službeni administrativni izvor s datiranim portalnim putem. Zamjena tih
oznaka uništila bi upravo trag koji pokušavamo sačuvati.

## Razrađeni primjer

Vraćamo se početnoj tvrdnji i prolazimo cijeli revizijski put. Cilj nije
pronaći skriveni „pravi” odaziv, nego odrediti što objavljeni dokaz doista
podupire.

Predmet provjere jest tablica „Odaziv birača” na stranici 124 *Izvješća o
provedenim izborima za zastupnike u Hrvatski sabor 2024.* (Hrvatske}, 2024).
Izdavač je Državno izborno povjerenstvo Republike Hrvatske (Hrvatske}, 2024).
Službeni je put pregledan 5. kolovoza 2026. (Hrvatske}, 2024). Knjiga ne posjeduje
lokalnu kopiju izborne datoteke i ne tvrdi da ima dopuštenje za njezinu
redistribuciju.

Taj zapis bilježi identitet i datum pregledane objave, ali ne zamrzava njezin
sadržaj. Ako se datoteka na istoj adresi promijeni ili nestane, ne posjedujemo
pregledane bajtove ni njihov kontrolni zbroj. Zato ne tvrdimo da je budući
prikaz na portalu istovjetan onomu koji smo pregledali.

Službena tablica ima dvanaest redaka izbornih jedinica, I.–XII., te nacionalni
ukupni redak za usklađenje (Hrvatske}, 2024). Nacionalni redak nije
trinaesta analitička jedinica. Nazivnik „ukupno birača” odnosi se na birače na
obrađenim biračkim mjestima u toj tablici (Hrvatske}, 2024). Ne smije se bez
provjere zamijeniti drugim brojem birača iz drugoga dijela izvješća.

Za jedinicu XII. broj važećih i nevažećih listića provjerava se zbrojem šest
objavljenih manjinskih redaka (Hrvatske}, 2024). Ta asimetrija znači da portal ne
opisujemo kao jednu provjerenu lokalnu pravokutnu datoteku. Provjeren je
službeni prikaz, ne sadržaj arhiva.

Zbroj dvanaest objavljenih nazivnika daje 3.558.089 (Hrvatske}, 2024). Zbroj
brojeva pristupilih daje 2.216.763 (Hrvatske}, 2024). Oba se zbroja potpuno
slažu s objavljenim nacionalnim retkom (Hrvatske}, 2024).

Važeći i nevažeći listići zbrajaju se u 2.215.209 (Hrvatske}, 2024). I taj
se zbroj slaže s objavljenom ukupnom vrijednošću prema listićima [Hrvatske}, 2024,
str. 124]. Usporedba s brojem pristupilih ostavlja razliku od 1.554
(Hrvatske}, 2024). Račun čini operativnu razliku vidljivom, ali je ne stvara.

Omjer 2.216.763 i 3.558.089 daje 62,30 % nakon množenja sa sto i zaokruživanja
na dvije decimale (Hrvatske}, 2024). To je potvrda objavljenoga odaziva. Nije
potvrda tvrdnje o ponašanju pojedinog birača.

### Doseg revidirane tvrdnje

Provjera obuhvata I.–X. daje 61,48 %, a službeni ukupni obuhvat I.–XII. daje
62,30 % (Hrvatske}, 2024). Razlika od 0,82 postotna boda pokazuje da obuhvat
pripada rezultatu (Hrvatske}, 2024). Uži obuhvat nije neutralna zamjena za nacionalni rezultat.
Smije se rabiti samo za zasebno, unaprijed opravdano pitanje o tim redcima.

DIP-ova tablica podržava opis administrativno zabilježenoga odaziva u
objavljenom obuhvatu. Redci izbornih jedinica mogu poduprijeti opisnu usporedbu
ili povezanost na toj razini ako se takva analiza provede. Ne podupiru zaključak
o pojedincima, potpori listama, uzrocima izlaska, budućim izborima ni populaciji
izvan izvora. Ovaj primjer podupire omeđenu uredničku odluku o tome kako
formulirati i provjeriti javnu tvrdnju.

Administrativni ukupni broj nije anketna procjena, pa mu ne pridružujemo
marginu pogreške iz widgeta. To ne znači da je bez ikakve nesigurnosti.
Obuhvat, definicije, obrada i moguće pogreške zapisa ostaju pitanja izvora i
postupka. Izvješće ovdje ne daje brojčanu mjeru za svaku od njih.

Uređena tvrdnja zato imenuje obje veličine. Prema službenom izvješću DIP-a za
izbore za Hrvatski sabor 2024., glasovanju je pristupilo 2.216.763 od 3.558.089
birača na obrađenim biračkim mjestima, odnosno 62,30 % (Hrvatske}, 2024).
Važeći i nevažeći listići zajedno daju 2.215.209 birača prema listićima, 1.554
manje od broja pristupilih (Hrvatske}, 2024). Oznake ne tretiramo kao
sinonime jer opisuju različite faze, ne zato što je razlika velika ili mala.

Zaključak bi se morao mijenjati kada bi se promijenio službeni izvor, obuhvat
obrađenih biračkih mjesta, značenje neke oznake ili usklađenje sastavnica s
ukupnim vrijednostima. Ne mijenja se zato što nam je drugi naslov privlačniji.

### Granica Dijela I — Protokol skeptičnoga čitanja

Skeptičnost nije navika odbacivanja. Ona usporava prijelaz od podatka do suda i
ostavlja vidljiv trag. Šest pitanja na granici Dijela I sažimaju taj postupak.

| Pitanje revizije | Primjena na tvrdnju o odazivu |
|---|---|
| Što je jedinica opažanja? | redak izborne jedinice; nacionalni je redak kontrolni zbroj |
| Tko ili što nedostaje, a što je odabrano? | nema individualnih obilježja; obuhvat su birači na obrađenim biračkim mjestima, a izbor I.–X. ili I.–XII. mora biti vidljiv |
| Koji je cilj i koja vrsta tvrdnje? | opis zabilježenog odaziva, ne tvrdnja o pojedincu ili uzroku |
| Koja je neizvjesnost obuhvaćena, a koja izostavljena? | aritmetika je provjerena; obuhvat i moguća pogreška zapisa nisu svedeni na marginu ankete |
| Koja je razumna alternativa? | broj prema listićima za drugo operativno pitanje; uži obuhvat samo uz unaprijed obrazložen cilj |
| Koje su posljedice pogreške? | naslov može zamijeniti službene veličine i čitatelju pripisati zaključak koji tablica ne nosi |

: Šest revizijskih pitanja primijenjenih na isti javni slučaj. Izrada autora.

Pitanja ne rade kao šest pečata koje tvrdnja automatski dobiva. Odgovor na prvo
može promijeniti drugo, a razumna alternativa može otkriti da je početni
nazivnik bio preuzak. Posljedice pogreške određuju koliko provjera mora biti
stroga. Pogrešno imenovanje brojnika u naslovu nije isto što i pogrešna odluka
koja nekome uskraćuje pravo, ali u oba slučaja mora ostati vidljivo tko snosi
teret pogreške.

Pitanja vode do pune karte tvrdnji. Vrsta tvrdnje i njezin doseg dvije su
odvojene odluke. Dokaz može dobro opisati određenu administrativnu populaciju,
a istodobno ne opravdavati generalizaciju na druge izbore ili uzročnu priču o
pojedincima.

| Dimenzija tvrdnje | Što DIP-ov dokaz dopušta u ovom primjeru |
|---|---|
| opis | poduprti su objavljeni odaziv i usklađenje službenih veličina |
| povezanost | samo na razini izbornih jedinica i tek nakon odgovarajuće analize; nacionalni ukupni redak sam nije povezanost |
| generalizacija | ne izvan populacije i obuhvata službenog izvora |
| predviđanje | nije poduprto jer tablica nije model budućih izbora |
| uzročnost | nije poduprta jer iz tablice ne saznajemo zašto je netko pristupio |
| odluka | poduprta je omeđena urednička odluka o tome je li javna formulacija provjerljiva i poštena |

: Šest dimenzija tvrdnje na granici Dijela I. Izrada autora.

Karta zaustavlja uobičajenu nadogradnju tvrdnje. Opis ne postaje uzrok zato što
je broj precizan, a usporedba izbornih jedinica ne postaje objašnjenje ponašanja
njihovih stanovnika. Odluka je zasebna dimenzija jer traži i posljedice, ne samo
račun. U ovom primjeru dopuštena je odluka o formulaciji naslova. Odluka o
izbornoj politici tražila bi dodatne ciljeve, dokaze i vrijednosne kriterije.

| Provjera | Pitanje |
|---|---|
| brojnik | Koja dva službena brojnika ne smijemo zamijeniti? |
| anketa | Zašto uzorak od nekoliko tisuća ljudi ne uklanja moguću sustavnu pristranost ankete? |
| temeljna stopa | Ako su udio pronađenih ciljanih zapisa i stopa pogrešnih upozorenja poznati, koji još podatak treba za udio ispravnih upozorenja? |
| podrijetlo | Navedite bilo koje dvije zajedničke provjere za broj i sintetičku sliku. |

: Samoprovjera Dijela I. Izrada autora.

## Sažetak

Broj može biti aritmetički točan i voditi pogrešnom zaključku. Zato čuvamo
izvor, jedinicu, brojnik, nazivnik, obuhvat, usporedbu i neizvjesnost. Temeljna
stopa sprječava da uspješnost testa zamijenimo vjerodostojnošću njegova
upozorenja. Margina pogreške ne popravlja pristranost i ovdje ostaje dug prema
poglavljima o uzorkovanju i procjeni.

Isti protokol vrijedi za službenu tablicu, anketu, odgovor asistenta i
sintetički medij. Razlikujemo simulaciju, sintetički zapis, hipotetski izlaz
modela i izmišljeni dokaz. Na granici Dijela I skeptično čitanje postaje
izvediv postupak. Šest pitanja određuje koju od šest dimenzija tvrdnje dokaz može
nositi i gdje joj završava doseg. Sljedeće poglavlje preuzima isti zahtjev pri
izgradnji analitičke tablice, provjeri transformacija i izboru poštenoga
sažetka.

## Pojmovi

postotak i postotni bod (*percentage and percentage point*), temeljna stopa
(*base rate*), margina pogreške (*margin of error*), podrijetlo tvrdnje
(*claim provenance*), sintetički zapis (*synthetic record*), protokol
skeptičnoga čitanja (*skeptical reading protocol*)

## Zadaci

### Konceptualni

Početna tvrdnja rabi broj pristupilih kao brojnik. Objasnite zašto zbroj
važećih i nevažećih listića nije zamjenjiv brojnik, iako su sva tri broja iz
istoga izvješća. Navedite što se može zaključiti iz razlike od 1.554, a što ne
(Hrvatske}, 2024). Zatim objasnite, bez novoga računa, zašto se udio
ispravnih upozorenja u dva hipotetska primjera mijenja iako provjera jednako
često nalazi ciljane zapise i jednako često pogrešno upozorava.

### Računski

Upotrijebite izvanmrežni agregat generiranoga skupa `populacija_medija` iz
datoteke `data/populacija-medija-agregat.csv` (Šikić, 2026). U izmišljenom gradu
portal je glavni izvor vijesti za 15.101 od 50.000 generiranih osoba, a
televizija za 10.827 (Šikić, 2026). Izračunajte oba udjela, razliku u postotnim
bodovima i relativnu razliku prema udjelu televizije. Jasno napišite da rezultat
opisuje simulaciju, ne stvarnu populaciju. Dopušten je kalkulator ili proračunska
tablica; ne predaje se kod.

### Kritički

Polazište je nacionalni redak službene tablice „Odaziv birača” [Hrvatske}, 2024, str.
124]. Usporedite tri ponuđene uredničke prerade toga retka. To su „Na izborima
je glasovalo 62,30 % birača”, „DIP bilježi da je glasovanju pristupilo 62,30 %
birača na obrađenim biračkim mjestima” i „Većina građana podržala je
pobjedničke liste” (Hrvatske}, 2024). Za svaku navedite je li poduprta
prikazanim dokazom.
Najbolju preradu doradite tako da uključi brojnik, nazivnik, izvor i jednu
važnu granicu.

Zatim razvrstajte četiri dokazna predmeta. To su generirana populacija iz
računskoga zadatka, pogrešni odgovor modela iz okvira, umjetno stvorena i tako
označena izborna fotografija te nepostojeća stranica izvješća prikazana kao
izvor. Svakom predmetu pridružite jednu od četiriju oznaka. Oznake su
simulacija, hipotetski izlaz modela, sintetički zapis i izmišljeni dokaz.
Objasnite koju tvrdnju svaka oznaka zabranjuje.

### Revizija modela

Ocijenite odgovor modela iz okvira iznad. Ponovite zbroj listića i razliku prema
broju pristupilih (Hrvatske}, 2024), a zatim napišite zamjenski odgovor od
najviše četiri rečenice. Odvojite ono što je izvorno potvrđeno od objašnjenja
koje bi tražilo nov dokaz.
