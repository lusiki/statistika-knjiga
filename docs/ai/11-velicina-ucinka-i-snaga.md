# Veličina učinka i snaga

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 22 min | Istraživač snage | simulirana populacija | pogl. 9, 10 |

**Vinjeta.**
Cohen je 1994. objavio kritiku prakse u kojoj je statistička značajnost
zamijenila razmišljanje o veličini i važnosti učinka, pod naslovom koji je
podsjećao da neke tvrdnje ne trebaju test (Cohen, 1994). Nije prigovarao računu.
Prigovarao je tome što je jedan broj preuzeo posao prosudbe.

Prigovor je imao vrlo konkretan oblik. Recenzent koji pročita da je razlika
značajna ne doznaje je li riječ o pomaku koji bi promijenio nečiju odluku ili o
razlici koju je otkrio samo dovoljno velik uzorak. Autor mu tu informaciju nije
uskratio namjerno, nego zato što obrazac izvještavanja nije tražio da je napiše.

Koliko podataka trebamo da bismo pouzdano uočili učinak koji je vrijedan
uočavanja?

## Razlika koja nešto znači

Poglavlje nastavlja usporedbu iz prethodnog. Isti simulirani stanovnici, isto
pitanje o povjerenju u medije među čitateljima tiska i portala, ali sada s
punom populacijom umjesto uzorka, jer nas zanima što je istina, a ne kako je
pogađamo.

Razlika iznosi `r hr_broj(s11$razlika, 2)` boda na ljestvici od jedan do deset.
Ta brojka je najvažniji rezultat cijele usporedbe i mora stajati u izvornim
jedinicama, jer se samo tako o njoj može odlučivati. Uredništvo koje razmišlja o
preraspodjeli sadržaja treba znati govori li se o tri četvrtine boda ili o tri
boda.

Sama razlika ipak ne kaže koliko je velika u odnosu na to kako su ljudi
raspoređeni. Bod razlike znači jedno kad su svi odgovori zbijeni oko sredine, a
nešto posve drugo kad se protežu preko cijele ljestvice. Standardizirana mjera
tu usporedbu ugrađuje u sam broj.

**Standardizirana razlika** je razlika dviju sredina podijeljena združenom
standardnom devijacijom skupina, pa se izražava u standardnim devijacijama
umjesto u izvornim jedinicama.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Oznaka $s_{\text{zdr}}$ stoji za združenu standardnu devijaciju, dakle za
zajedničku mjeru raspršenosti unutar obiju skupina.

Povjerenje se u ovoj populaciji raspršuje sa združenom standardnom devijacijom
od `r hr_broj(s11$zdruzena, 2)` boda, pa razlika od `r hr_broj(s11$razlika, 2)`
boda daje standardiziranu razliku od `r hr_broj(s11$d, 2)`. Dvije skupine dakle
dijeli nešto više od trećine standardne devijacije, što znači da se njihove
raspodjele u najvećem dijelu preklapaju i da po jednom ispitaniku ne bi bilo
moguće pogoditi odakle se informira.

Standardna devijacija kao mjerna jedinica ipak ostaje apstraktna, pa isti učinak
vrijedi izraziti i na način koji se može zamisliti. Izvučemo li nasumce jednog
čitatelja tiska i jednog čitatelja portala, prvi ima više povjerenja u
`r hr_broj(s11$nadmoc, 1)` % slučajeva. Kad razlike ne bi bilo, taj bi udio
iznosio pedeset posto, pa je učinak veličine kakvu ovdje gledamo pomak od desetak
postotnih bodova u tako postavljenom pitanju. Rečenica tog oblika prolazi kroz
uredničku raspravu bolje od bilo koje standardizirane mjere, jer nitko ne mora
znati što je standardna devijacija da bi razumio ishod.

Orijentacijske vrijednosti za takve mjere postoje i najčešće se navode prema
Cohenu, koji ih je ponudio kao pomoć u odsutnosti boljeg oslonca, a ne kao
ljestvicu za očitavanje (Cohen, 1988). Što je učinak ove veličine sadržajno,
odlučuje usporedba s drugim učincima u istom području i cijena postupanja, a ne
tablica pragova. Standardizacija služi tome da se ta usporedba uopće može
napraviti, jer razlike izmjerene u minutama, bodovima i postocima inače nemaju
zajednički jezik.

## Kad je značajno, a nije važno

Test odgovara na pitanje je li s podacima uskladiva i nula. To pitanje s
veličinom učinka ima manje veze nego što se pretpostavlja, i najlakše se to vidi
kad je uzorak vrlo velik.

Zamislimo portal koji uspoređuje dvije naslovnice. Prva ima stvarnu stopu klika
od 2,00 %, druga od 2,05 %, a svaka je prikazana pola milijuna puta. Podaci
ispod su konstruirani za ovu svrhu i nisu nalaz ni o kojoj stvarnoj kampanji.

U simuliranom pokusu prva je naslovnica postigla `r hr_broj(s11$ab_a, 3)` %, a
druga `r hr_broj(s11$ab_b, 3)` %. Razlika iznosi
`r hr_broj(s11$ab_razlika, 3)` postotnog boda uz interval od
`r hr_broj(s11$ab_donja, 3)` do `r hr_broj(s11$ab_gornja, 3)`, a p-vrijednost
je `r formatC(s11$ab_p, format = "f", digits = 5, decimal.mark = ",")`. Po
svakom kriteriju iz prethodnog poglavlja rezultat je jasan, jer nulti model
ovakvu razliku gotovo nikada ne proizvodi.

Prevedeno natrag u odluku, dobitak je jedan dodatni klik na otprilike tisuću
prikaza. Isplati li se zbog toga mijenjati naslovnicu, ovisi o trošku promjene i
o tome što jedan klik vrijedi, a ni jedno ni drugo nije u podacima. Statistička
značajnost ovdje govori samo to da je uzorak bio dovoljno velik da razliku ove
veličine odvoji od nule.

Ista logika radi i u suprotnom smjeru. Razlika koja bi promijenila uredničku
odluku može ostati neznačajna ako je uzorak malen, i tada izostanak značajnosti
ne govori o svijetu nego o količini prikupljenih podataka. Zbog toga se
značajnost i važnost izvještavaju odvojeno, i zbog toga procjena s intervalom
uvijek stoji ispred testa.

## Snaga kao svojstvo plana

Vjerojatnost da postupak pronađe učinak koji postoji nije svojstvo testa nego
kombinacije nekoliko odluka, od kojih se većina donosi prije podataka.

**Statistička snaga** je vjerojatnost da postupak odbaci nultu hipotezu kad je
ona lažna, dakle udio ponavljanja u kojima bi učinak zadane veličine bio
otkriven.

Prethodno je poglavlje na ovoj populaciji izmjerilo da postupak stvarnu razliku
pronalazi u otprilike četiri od pet uzoraka od tristo osoba. Ta brojka upravo je
snaga, i sada je vrijedi izmjeriti na više veličina uzorka.

Mjerenje zadržava permutacijski postupak iz prethodnog poglavlja i njegove
granice. Nulti model tvrdi da je cijela raspodjela povjerenja jednaka u objema
skupinama, tako da su oznake izvora zamjenjive u odnosu na ishod. Obostrana
testna statistika jest apsolutna sirova razlika sredina. Osobe se tretiraju kao
zasebne jedinice bez zajedničke ovisnosti, dok simulacija bez ponavljanja izvlači
uzorke iz jedne konačne simulirane populacije u kojoj razlika po izvoru postoji.
Svaka točka krivulje obuhvaća tristo zamišljenih studija. U svakoj se
p-vrijednost procjenjuje iz dvjesto nasumičnih premještanja uz korekciju
$(b + 1)/(B + 1)$. Pritom $B$ predstavlja broj premještanja, a $b$ broj rezultata
barem toliko ekstremnih kao opaženi. Krivulja zato procjenjuje snagu samo za taj
mehanizam podataka i taj postupak, a ne opće svojstvo uzorka određene veličine.

*Slika. Udio uzoraka u kojima permutacijski postupak prelazi prag od 0,05 pri stvarnoj razlici od 0,74 boda. Tristo simuliranih studija po retku. Izrada autora.*

Rast nije ravnomjeran i to je najvažnije u tablici. Podizanje uzorka sa
šezdeset na tristo osoba snagu diže s `r hr_broj(s11$snaga_60, 1)` % na
`r hr_broj(s11$snaga_300, 1)` %, a svako daljnje ulaganje kupuje sve manje, jer
je udio ograničen odozgo. Studija sa šezdeset osoba nije upola lošija od studije
s tristo, nego je gotovo beskorisna za ovo pitanje.

Četiri stvari određuju gdje se na toj krivulji nalazimo. Veći stvarni učinak
lakše se otkriva, veći uzorak daje precizniju procjenu, manja raspršenost ishoda
čisti signal, a blaži prag propušta više rezultata. Prve dvije obično su jedine
koje istraživač može mijenjati, i samo je druga u njegovim rukama nakon što je
pitanje postavljeno.

Konvencija traži barem 80 %, i kao svaka konvencija služi kao polazište, a ne
kao dokaz. Ako propuštena razlika nosi ozbiljnu posljedicu, osamdeset posto je
premalo, a ako je istraživanje prvo u nizu i služi kao provjera izvedivosti,
može biti previše.

## Interakcija — Istraživač snage

Sljedeći prikaz odvaja tri odluke koje se u praksi donose zajedno. Čitatelj
mijenja stvarnu veličinu učinka, broj jedinica i prag, svaki put samo jedno, i
prati kako se pomiče udio uzoraka u kojima bi postupak nešto našao.

Prikaz koristi idealizirani model u kojem nulta hipoteza postavlja
standardiziranu razliku na nulu. Testna statistika je apsolutna z-vrijednost, a
postupak je obostran. Model pretpostavlja dvije neovisne skupine jednake
veličine, neovisne normalne ishode i zajedničku poznatu standardnu devijaciju.
Za svaku točku izravno simulira z-vrijednosti iz pripadne normalne raspodjele,
pa broj ponavljanja određuje samo Monte Carlo nesigurnost prikazane snage.

*Slika. Simulirana snaga kroz veličine uzorka u idealiziranom postupku s poznatom varijabilnošću.*

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Spustite prag odluke i provjerite koliko je jedinica potrebno za istu snagu.
4. Postavite standardiziranu razliku na 0,10 i pokušajte dosegnuti 80 %.

Posljednji korak ne uspijeva unutar ponuđenog raspona, i to je poanta. Za male
učinke potreban uzorak raste brže nego što većina istraživanja može podnijeti,
pa odluka o tome koji je učinak vrijedan traženja mora doći prije odluke o
uzorku.

## Podsnažene studije pretjeruju

Uobičajena pouka o slaboj snazi glasi da se stvarni učinci propuštaju. To je
točno, a nije najgori dio. Studija sa slabom snagom kvari i one nalaze koje
proizvede, i to se na poznatoj populaciji može izmjeriti.

Ponovili smo isto pitanje na tri tisuće studija sa šezdeset osoba. Prosjek svih
procjena iznosi `r hr_broj(s11$prosjek_svih, 2)` boda i praktički se poklapa sa
stvarnom razlikom od `r hr_broj(s11$razlika, 2)`, dakle postupak sam po sebi
nije pristran.

*Slika. Procijenjena razlika u tri tisuće studija sa šezdeset osoba, sve zajedno i samo one koje su prešle prag. Okomita crta označuje stvarnu razliku u populaciji.*

Donji panel prikazuje ono što bi se objavilo. Među studijama koje su prešle prag
prosječna procjena iznosi `r hr_broj(s11$prosjek_znacajnih, 2)` boda, dakle
`r hr_broj(s11$faktor, 1)` puta više od istine. Razlog je mehanički i nema veze
s poštenjem istraživača. Uz slabu snagu prag prelaze samo uzorci u kojima je
slučajnost razliku slučajno uvećala, jer manja procjena s ovako malim uzorkom
prag ne može prijeći. Najmanja značajna procjena u ovoj simulaciji iznosi
`r hr_broj(s11$najmanja_znacajna, 2)` boda.

Drugi smjer rjeđi je, ali nije nemoguć. Među značajnim nalazima
`r hr_broj(s11$krivi_predznak, 2)` % ima suprotan predznak od stvarne razlike,
dakle tvrdi da čitatelji portala imaju više povjerenja. Takav bi rad prošao
recenziju jednako lako kao svaki drugi, jer je iznutra besprijekoran.

Ista simulacija s pet stotina osoba daje procjene koje istinu premašuju za
faktor `r hr_broj(s11$faktor_veliki, 2)`, dakle iskrivljenja praktički nema.
Pretjerivanje nije svojstvo područja ni teme, nego posljedica toga što se prag
primjenjuje na procjene koje su preraspršene za veličinu učinka koji se traži.

Za čitatelja objavljenih radova iz toga slijedi konkretan postupak. Kad rad na
malom uzorku izvještava o velikom učinku uz p-vrijednost tik ispod praga,
najvjerojatnije objašnjenje nije da je učinak zaista tolik nego da je uzorak
propustio samo one procjene koje su slučajno ispale velike. Interval to obično
odaje, jer se u takvim radovima proteže od jedva zamjetne do nevjerojatno velike
vrijednosti. Zato se prvo gleda koliko je jedinica bilo i koliko je interval
širok, a tek onda što piše u zaključku.

## Planiranje unatrag

Iz svega prethodnog slijedi da uzorak nije stvar raspoloživosti nego odluke, i
da ta odluka počinje na kraju.

**Najmanji važan učinak** je najmanja razlika koja bi promijenila zaključak,
odluku ili postupanje, određena sadržajno i prije prikupljanja podataka.

Postavlja ga istraživač, a ne račun, i obrazlaže se troškom postupanja,
ozbiljnošću ishoda i onim što je u istom području već izmjereno. Tek kad je
zapisan, pitanje o veličini uzorka ima odgovor, jer se snaga uvijek računa za
neku određenu veličinu učinka.

Redoslijed je time obrnut od uobičajenog. Ne pita se koliko se ispitanika može
prikupiti pa se nada da će biti dovoljno, nego se kreće od razlike koja bi nešto
značila, dodaje se željena snaga, i iz toga izlazi broj jedinica. Ako je taj broj
neizvediv, to je nalaz sam po sebi i treba ga znati prije istraživanja, a ne
poslije.

Postoji i drugi način planiranja, bliži načelu po kojem je ova knjiga napisana.
Umjesto da se pita koliko je jedinica potrebno da bi se prešao prag, pita se
koliko ih je potrebno da bi procjena bila dovoljno precizna. Uz raspršenost iz
ove populacije interval razlike širok je `r hr_broj(s11$sirina_100, 2)` boda pri
stotinu ljudi po skupini, `r hr_broj(s11$sirina_300, 2)` pri tristo i
`r hr_broj(s11$sirina_800, 2)` pri osamsto. Istraživač koji zna da mu je za
odluku potrebna procjena unutar pola boda odatle čita odgovor izravno, bez
ijedne pretpostavke o tome koliki je stvarni učinak.

Ta je razlika u pristupu važnija nego što izgleda. Planiranje prema snazi
zahtijeva da se pogodi veličina učinka koji se traži, a upravo je ta veličina
ono što se ne zna i zbog čega se istraživanje provodi. Planiranje prema
preciznosti tu pretpostavku ne treba, jer širina intervala ovisi samo o
raspršenosti i broju jedinica. Studija planirana na taj način ne obećava da će
nešto naći, nego da će, što god nađe, biti dovoljno precizno da se o tome može
odlučivati.

## Razrađeni primjer

Pretpostavimo da bi uredništvo reagiralo na razliku od pola boda i da očekuje
raspršenost sličnu onoj u ovoj populaciji. Analiza ispod za nekoliko veličina
uzorka broji u kolikom udjelu simuliranih studija bi takva razlika bila
otkrivena.

Nulta hipoteza u ovom računu tvrdi da je razlika sredina nula, a testna
statistika dijeli opaženu razliku poznatom standardnom pogreškom. Simulacija
pretpostavlja dvije neovisne skupine, neovisne normalne ishode, jednaku i poznatu
standardnu devijaciju od 1,9 boda te obostrani z-postupak s pragom 0,05. Za svaku
veličinu uzorka proizvodi dvije tisuće novih parova skupina. Izračunana snaga
vrijedi samo pod tim pretpostavkama i za unaprijed zadanu razliku od pola boda.

Funkcija `replicate` ponavlja cijelu zamišljenu studiju dvije tisuće puta, a
`sapply` isti račun provodi za svaku ponuđenu veličinu uzorka. Granica 1,96
dolazi iz standardne normalne raspodjele i pripada upravo opisanom obostranom
z-postupku, a ne permutacijskom postupku iz prvog prikaza snage.

*Slika. Udio simuliranih studija u kojima bi razlika od pola boda bila otkrivena, pri četirima veličinama uzorka po skupini. Izrada autora.*

Za razliku od pola boda treba između dvjesto i dvjesto pedeset ljudi po skupini
da bi se dosegla uobičajena granica od osamdeset posto. Ako uredništvo može
prikupiti stotinu, plan je i dalje moguć, ali izvještaj mora unaprijed reći da
će studija razliku te veličine propustiti u više od polovice slučajeva.

Račun ne odlučuje ništa od onoga što je važno. Pola boda kao granicu postavio je
netko tko zna što se s tom razlikom radi, raspršenost je procijenjena iz ranijih
mjerenja, a odustajanje ispitanika i kvaliteta mjerenja nisu ni ušli u simulaciju.
Ono što račun daje jest jedini pošten oblik rečenice o uzorku, u kojem broj
jedinica stoji uz učinak koji se njime može uočiti.

**Statistika u divljini.**
**Neuspjeh snage.** Skupina istraživača objavila je pregled u kojem tvrdi da je
prosječna statistička snaga studija u neuroznanosti vrlo niska, i da posljedice
toga uključuju precijenjene veličine učinka i slabu ponovljivost rezultata
(Button, 2013). Rad je naslovljen kao neuspjeh snage i čitan je najčešće kao
poziv na veće uzorke.

Ono što se u tom čitanju gubi jest drugi dio tvrdnje. Niska snaga ne smanjuje
samo izglede da se pravi učinak pronađe, nego smanjuje i vjerojatnost da
statistički značajan nalaz odgovara stvarnom učinku. To je ista mehanika koju
simulacija u prethodnom odjeljku mjeri, gdje su procjene koje su prešle prag u
prosjeku dvostruko veće od istine. Iz toga slijedi da podsnaženo područje ne
proizvodi samo manje nalaza nego i lošije, pa preporuka nije čitati takve radove
opreznije, nego ne vjerovati veličini učinka koju objavljuju.

**Pitajte model.**
Asistent pouzdano izračuna standardiziranu razliku i provede analizu snage, a
sam ne zna ono što u nju ulazi. Prije poziva mu treba dizajn, očekivana
raspršenost ishoda i najmanji učinak koji bi nešto značio, jer bez posljednjega
snaga nema referencu. Provjeravamo tri stvari. Prva je koristi li nazivnik koji
odgovara dizajnu, budući da se kod uparenih mjerenja dijeli standardnom
devijacijom razlika. Druga je uzima li konvencionalne pragove kao sadržajnu
činjenicu i naziva li učinak malim prije nego što je pitao o čemu se radi. Treća
je računa li snagu iz učinka koji je već opažen, što je najčešća i najskuplja
pogreška u ovom području.

> Reci mi koji ulaz nedostaje prije nego što izračunaš snagu. Zatim izračunaj
> potreban uzorak za nekoliko veličina učinka i pokaži koliko se odgovor mijenja
> ako je stvarni učinak upola manji od pretpostavljenog.

**Nađite grešku.**
Nakon male studije s tridesetero ljudi po skupini asistent je uz nalaz priložio
i ovu provjeru.

Uz ispis je dodao obrazloženje. Opažena razlika daje standardiziranu razliku
oko 0,78, a snaga izračunata za tu vrijednost i trideset ljudi po skupini iznosi
0,84. Budući da je snaga iznad uobičajene granice, zaključuje da je studija
bila dovoljno velika i da se procijenjenoj razlici može vjerovati.

## Sažetak

Veličina učinka vraća pitanju koliko je razlika velika, a standardizirana mjera
čini je usporedivom preko različitih ljestvica. Statistička značajnost i
praktična važnost odgovaraju na različita pitanja, pa golem uzorak proizvodi
značajnost za razlike koje nikoga ne zanimaju, dok premali uzorak propušta one
koje bi promijenile odluku. Snaga povezuje učinak, uzorak, raspršenost i prag, a
mjerenje na poznatoj populaciji pokazuje koliko brzo pada kad uzorak popusti.
Studije sa slabom snagom pritom ne griješe samo propuštanjem, jer među njihovim
objavljenim nalazima procjene su u prosjeku dvostruko veće od istine, a poneka
ima i pogrešan predznak. Sljedeće poglavlje pokazuje što se događa kada sustav
nagrađuje objavljeni nalaz, a skriva cijeli put koji je do njega doveo.

## Pojmovi

veličina učinka (*effect size*), standardizirana razlika (*Cohen's d*),
praktična važnost (*practical significance*), statistička snaga (*statistical
power*), najmanji važan učinak (*smallest effect size of interest*), planiranje
uzorka (*sample size planning*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto među objavljenim nalazima podsnaženih studija
procjene učinka sustavno premašuju istinu, iako nijedan pojedinačni istraživač
nije napravio ništa nedopušteno. Imenujte korak u kojem nastaje iskrivljenje.

### Računski

Dvije skupine imaju sredine 5,4 i 4,6 uz združenu standardnu devijaciju 1,9.
Izračunajte razliku i standardiziranu razliku, a zatim ponovite račun uz
združenu standardnu devijaciju 3,8. Objasnite koja se od dviju brojki promijenila
i zašto. Zatim u widgetu poglavlja pronađite koliko je jedinica po skupini
potrebno da se manja od dviju standardiziranih razlika otkrije u četiri od pet
pokušaja.

### Kritički

Prosudite tvrdnju da niska prosječna snaga nekog područja znači samo da
istraživanja propuštaju stvarne učinke (Button, 2013). Predajte kratku uredničku
bilješku i navedite podatak koji bi vam trebao da procijenite koliko je
objavljena veličina učinka precijenjena.

### Revizija modela

Ocijenite provjeru iz okvira o pogrešci. Imenujte što je u pozivu ispravno,
argument u kojem stoji kružnost, redak koda u kojem ona ulazi u račun, i
napišite čime bi taj argument trebalo zamijeniti.
