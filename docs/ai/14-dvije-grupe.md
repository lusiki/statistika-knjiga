# Uspoređivanje dviju grupa

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-08-04 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 24 min | Uzorkivač dviju grupa | simulirana populacija | pogl. 10, 11, 13 |

**Vinjeta.**
Cumming je urednicima psihologijskih časopisa predložio promjenu koja izgleda
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

Usporedba dviju sredina izgleda kao jedno pitanje, a zapravo ih je troje.
Razlika je u tome odakle dolaze dva broja koja uspoređujemo, i to pitanje nije
statističko nego pitanje o dizajnu istraživanja.

U prvom slučaju imamo jednu skupinu i vrijednost izvana. Prosječno povjerenje u
našem uzorku uspoređujemo sa službenom vrijednošću iz ranije objavljenog vala
istraživanja ili sa sredinom ljestvice. U drugom slučaju imamo dvije odvojene
skupine sastavljene od različitih ljudi, recimo one koji se prvenstveno
informiraju s televizije i one koji to čine preko društvenih mreža. U trećem
slučaju iste jedinice mjerimo dva puta, prije i poslije nekog događaja, pa svaki
ispitanik nosi oba rezultata.

**Jedinica neovisnosti** je entitet koji se u istraživanju mogao pojaviti ili
izostati neovisno o ostalima, pa njegove vrijednosti nisu unaprijed vezane uz
vrijednosti bilo koje druge jedinice u istom skupu.

Ta jedinica određuje sve ostalo. U usporedbi dviju skupina to je osoba, jer je
svaka osoba u samo jednoj skupini. U ponovljenom mjerenju to je i dalje osoba,
ali sada nosi dva rezultata koja su međusobno povezana, pa se analiza ne provodi
na četrdeset mjerenja nego na dvadeset razlika. Postupak koji tu vezu previdi
računa s dvostruko više podataka nego što ih doista ima.

Prvi korak analize zato nije izbor testa nego rečenica koja imenuje jedinicu.
Ako se ta rečenica ne može napisati, podaci još nisu spremni za bilo kakvu
usporedbu.

## Razlika prije oznake

Poglavlje radi na istoj simuliranoj populaciji kao poglavlja o uzorkovanju i
procjeni. Iz nje je izvučeno `r s14$n` osoba koje se informiraju s televizije ili
preko društvenih mreža, i pitanje glasi razlikuju li se te dvije skupine po
povjerenju u medije.

Redoslijed izvještavanja postavljamo prije nego što bilo što izračunamo. Prvo
dolazi razlika u izvornim jedinicama, zatim interval koji joj pripada, pa tek
onda test i standardizirana veličina. Taj redoslijed nije stvar ukusa. Razlika i
njezin interval odgovaraju na pitanje koliko iznosi učinak, a test odgovara na
mnogo uže pitanje je li podacima uskladiva i nula.

U našem uzorku prosječno povjerenje iznosi
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "TV"], 2)` među onima koji
gledaju televiziju i
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "društvene mreže"], 2)` među
onima koji se informiraju preko društvenih mreža. Razlika iznosi
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
iznosi `r hr_broj(s14$pop_razlika, 2)` boda, dakle unutar intervala koji je
uzorak proizveo. To je jedna potvrda od mnogo mogućih, a koliko ih se u dugom
nizu ponavljanja može očekivati, pokazalo je poglavlje o procjeni.

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
što je u njemu namješteno jest da su dva mjerenja iste osobe povezana, kao što u
ponovljenim mjerenjima uvijek jesu.

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

Koliko se time dobiva, ovisi isključivo o povezanosti dvaju mjerenja. Uparena
raspršenost sadrži faktor koji pada kako povezanost raste, pa je dobitak velik
kad se osobe kroz vrijeme drže svojih razina, a nikakav kad se drugo mjerenje
ponaša kao da s prvim nema veze. Uz povezanost blizu nule upareni postupak
zapravo gubi, jer troši polovicu stupnjeva slobode za ispravak koji nije bio
potreban. Uparivanje se zato planira u dizajnu, gdje se zna hoće li ista osoba
sa sobom donijeti stabilnu razinu, a ne bira nakon što se vide podaci.

## Jedan model iza triju testova

Tri dizajna iz prvog odjeljka izgledaju kao tri postupka, a mogu se zapisati kao
jedan. Pretpostavimo da svaka osoba ima brojčani ishod i pripadnost jednoj od
dviju skupina. Model kaže da očekivani ishod ovisi o toj pripadnosti, i to
jednim brojem po skupini.

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
razlici koju smo već izračunali. Model dakle nije dao novu brojku nego stari
odgovor u novom obliku.

Dobitak od tog oblika pokazat će se kasnije, i to na dva mjesta. Prediktor s više
od dviju kategorija donosi poglavlje o više skupina, a prediktor koji nije
kategorija nego broj donosi poglavlje o regresiji. Test dviju sredina odatle
gledano nije zaseban postupak nego najmanji mogući slučaj jednog jedinog okvira.

Model pritom ne zamjenjuje dizajn. Koeficijent opisuje razliku među skupinama
onako kako su one nastale, a uzročno značenje dolazi isključivo iz načina na koji
je pripadnost skupini dodijeljena. Ako je ljudi biraju sami, model o uzroku ne
govori ništa, koliko god uredno bio ispisan.

## Što razlika sama ne kaže

Razlika u izvornim jedinicama nosi značenje samo dok se zna koliko je ljestvica
raspršena. Bod razlike na ljestvici čije su vrijednosti zbijene znači nešto
sasvim drugo nego bod razlike na ljestvici na kojoj su ljudi raspoređeni široko.
Standardizirana veličina učinka upravo to uzima u obzir.

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
Prosječna dob onih koji se informiraju preko društvenih mreža iznosi
`r hr_broj(s14$pop_dob_mreze)` godine, a onih koji gledaju televiziju
`r hr_broj(s14$pop_dob_tv)` godine, dok povjerenje u ovoj populaciji raste s
dobi.

Budući da je populacija poznata, taj se udio može izmjeriti umjesto pretpostaviti.
Ukupna razlika u njoj iznosi `r hr_broj(s14$pop_razlika, 2)` boda. Ograničimo li
je na osobe između trideset i pedeset godina, dakle na raspon unutar kojeg se dob
dviju skupina znatno manje razlikuje, razlika pada na
`r hr_broj(s14$pop_razlika_uska, 2)` boda. Otprilike trećina onoga što bi
neoprezan izvještaj pripisao izvoru vijesti pripada dobi.

U našem uzorku od `r s14$n` osoba u taj uski raspon upada tek `r s14$uzak_n`
njih, i interval razlike proteže se od `r hr_broj(s14$uzak_donja, 2)` do
`r hr_broj(s14$uzak_gornja, 2)`, dakle preko nule. Uzorak koji je za ukupnu
razliku bio dovoljan za razliku unutar dobnog raspona više nije, a o tome koliko
podataka treba da bi se učinak zadane veličine uopće mogao razlučiti govori
poglavlje o veličini učinka i snazi.

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

U našem uzorku društvene mreže imaju `r s14$n_mreze` opažanja i varijancu
`r hr_broj(s14$var_mreze, 3)`, a televizija `r s14$n_tv` opažanja i varijancu
`r hr_broj(s14$var_tv, 3)`. Oba postupka procjenjuju razliku od
`r hr_broj(s14$razlika, 3)` boda, ali Welchova standardna pogreška iznosi
`r hr_broj(s14$se_welch, 3)` uz `r hr_broj(s14$df_welch, 3)` stupnja slobode,
dok obični linearni model daje `r hr_broj(s14$se_ols, 3)` uz
`r s14$df_ols` stupnjeva slobode. Njihovi se intervali na dvije decimale oba
ispisuju kao 0,45 do 1,92, ali ta podudarnost nakon zaokruživanja ne čini ih
istim inferencijskim postupkom. Welch zato ostaje početni izbor, a obični
linearni model služi kao izričito označena usporedba pod pretpostavkom jednake
rezidualne varijance.

Normalnost se procjenjuje pogledom na raspodjelu, a tek onda testom.
Shapiro-Wilkov test ima istu osjetljivost na veličinu uzorka kao svaki drugi
test, pa će na velikom uzorku prijaviti odstupanja bez ikakvih posljedica, a na
malom propustiti ozbiljna. Njegov rezultat zato ne može biti prekidač koji sam
odlučuje o izboru postupka.

Krajnja opažanja traže pregled, a ne automatsko brisanje. Mogu biti pogreške u
unosu, mogu biti rijetki ali stvarni slučajevi, a mogu biti i znak da sredina
nije prikladan sažetak te varijable. Analiza provedena s njima i bez njih, uz oba
rezultata u izvještaju, poštenija je od tihe odluke donesene nakon pogleda na
p-vrijednost.

Wilcoxonov postupak radi s rangovima umjesto s vrijednostima, pa ga jedno krajnje
opažanje ne može pomaknuti. Njegovo pitanje ipak nije isto, jer se ne odnosi na
razliku sredina nego na položaje raspodjela. U našem uparenom skupu daje
p-vrijednost od
`r formatC(s14$wilcoxon_p, format = "f", digits = 4, decimal.mark = ",")`, dakle
isti zaključak, ali ne i istu tvrdnju.

**Statistika u divljini.**
**Preklapanje crtica.** Pravilo da razlika nije značajna ako se crtice pogreške
na grafu preklapaju kruži znanstvenim tekstovima kao da je egzaktno. Belia i
suradnici pozvali su 473 autora radova iz psihologije, bihevioralne neuroznanosti
i medicine da na internetskom prikazu pomiču dvije sredine s crticama sve dok
razlika ne postane taman značajna (Belia, 2005).

Odgovori su pokazali da mnogi vodeći istraživači ne razlikuju interval
pouzdanosti od standardne pogreške i ne uzimaju u obzir jesu li dvije sredine
neovisne ili dolaze iz ponovljenog mjerenja. Upravo to razlikovanje nosi cijelo
ovo poglavlje. Nalaz je pritom o čitanju grafova, a ne o crticama, pa iz njega
slijedi da graf mora reći koju veličinu prikazuje i iz kojeg dizajna dolazi, a ne
da se crtice izbjegavaju.

**Pitajte model.**
Asistent gotovo uvijek ponudi t-test čim vidi jednu kategoričku i jednu brojčanu
varijablu, i obično ne pita ono što bi moralo doći prvo. Prije poziva mu treba
opis dizajna i identifikator jedinice, jer iz samog oblika tablice ne može znati
jesu li dva stupca dva mjerenja istih osoba. Provjeravamo je li uparivanje
sačuvano, koristi li Welchovu inačicu, izvještava li razliku i interval prije
testa i je li tiho izbacio retke s praznim vrijednostima.

> Opisat ću dizajn i reći koja varijabla identificira jedinicu. Prvo prikaži
> raspodjele obiju skupina, zatim procijeni razliku s intervalom u izvornim
> jedinicama, pa tek onda provedi odgovarajući test i navedi veličinu učinka.

**Nađite grešku.**
Usporedba povjerenja u medije između dviju skupina provedena je Welchovim testom,
uz prikazane raspodjele i interval razlike. Analiza je zatim ponovljena unutar
dobne skupine od trideset do pedeset godina, gdje interval razlike obuhvaća nulu.
Zaključak izvještaja glasi da unutar te dobne skupine izvor vijesti nema veze s
povjerenjem.

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
razlike zato je egzaktna, a jednakost inferencije nije. Kad u sljedećem
poglavlju skupina bude pet umjesto dvije, zajednički oblik modela ostaje, ali
izbor postupka za nesigurnost ostaje zasebna odluka.

Izvještaj koji bi na tome stao još ne bi bio potpun. Treba mu opis kako su skupine
nastale, jer ljudi svoj izvor vijesti biraju sami, i napomena da skupine nisu
izjednačene po dobi. Bez toga bi ista brojka lako prešla iz rečenice o razlici u
rečenicu o učinku, a to su dvije različite tvrdnje.

## Sažetak

Usporedba dviju grupa počinje dizajnom i rečenicom koja imenuje jedinicu
neovisnosti. Jednouzoračni, neovisni i upareni postupak tri su lica iste procjene
razlike, a razlikuju se po tome prema čemu se razlika mjeri. Isti brojevi
obrađeni kao upareni i kao neovisni daju suprotne zaključke, pa taj izbor nije
tehnički detalj. Linearni model s binarnim prediktorom otkriva zajednički okvir u
kojem je test dviju sredina najmanji mogući slučaj. Standardizirana veličina
učinka čuva usporedivost, ali ne uklanja razlike među skupinama koje s ishodom
dolaze zajedno. Sljedeće poglavlje isti model širi na više skupina i uvodi cijenu
mnogih usporedbi.

## Pojmovi

jedinica neovisnosti (*unit of independence*), neovisne skupine (*independent
groups*), upareni podaci (*paired data*), Welchov t-test (*Welch's t-test*),
referentna skupina (*reference category*), standardizirana razlika (*Cohen's d*),
Wilcoxonov test (*Wilcoxon test*)

## Zadaci

### Konceptualni

Za tri istraživačke situacije imenujte jedinicu neovisnosti i odgovarajući
dizajn. Prva uspoređuje prosječno povjerenje u uzorku sa službenom vrijednošću iz
ranijeg vala istraživanja, druga uspoređuje dvije skupine gledatelja, a treća
mjeri iste ispitanike prije i poslije kampanje.

### Računski

Dvije skupine imaju po dvadeset pet ispitanika, sredine 5,4 i 4,6 te jednake
standardne devijacije od 1,6. Izračunajte razliku i standardiziranu razliku, a
zatim ponovite račun uz standardnu devijaciju 3,2. Objasnite zašto se prva brojka
nije promijenila, a druga jest.

### Kritički

Prosudite koliko izvještaj gubi kad umjesto procjene razlike s intervalom ponudi
samo oznaku značajnosti (Cumming, 2014). Predajte kratku bilješku recenzentu i
navedite jednu odluku koja bi se bez intervala mogla donijeti pogrešno.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte korake koji su provedeni ispravno,
izdvojite tvrdnju koja iz rezultata ne slijedi i napišite rečenicu kojom bi je
trebalo zamijeniti.
