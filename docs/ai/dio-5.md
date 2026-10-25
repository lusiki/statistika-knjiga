# DIO V: MODELI

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Kategorički podaci

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Sumnja u pravednost Berkeleyjskih upisa tražila je usporedbu prijava i ishoda
za muškarce i žene (Bickel, 1975). Zbirne i odjelne stope otvorile su različita
pitanja, iako su nastale iz istih zapisa. Izbor usporedbe određivao je što se
iz tablice moglo zaključiti.

Kad jednom odaberemo usporedbu, preostaje procijeniti koliko se opaženi
raspored razlikuje od onoga koji bismo očekivali bez povezanosti. Bi li sam
nalaz povezanosti bio dovoljan za zaključak o pravednosti upisa?

Zbirne i odjelne stope prijma na Sveučilište Berkeley pokazale su koliko
tumačenje postotka ovisi o nazivniku i okolnostima nastanka podataka
(Bickel, 1975). Za analizu kategorija trebamo povezati taj uvid s opisom
raspodjele i povezanosti, procjenom nesigurnosti te razlikom između
statističke značajnosti i veličine učinka.

Takve podatke često susrećemo u društvenim znanostima. Zanima nas koji izvor
vijesti osoba bira, kojoj obrazovnoj skupini pripada ili podržava li neki
prijedlog. Odgovore možemo prebrojiti, ali samo brojanje još ne daje odgovor
na istraživačko pitanje. Ako mlađi i stariji biraju različite izvore vijesti,
kako ćemo opisati tu razliku i procijeniti što nam uzorak govori o populaciji?

Logika zaključivanja koju smo dosad usvojili ostaje ista. Najprije postavljamo
nulti model u kojem dvije varijable nisu povezane. Zatim uspoređujemo opažene
podatke s onime što bismo pod tim modelom očekivali. Ovdje ćemo tu usporedbu
provesti na frekvencijama u kontingencijskoj tablici. Uz rezultat testa i
dalje trebamo pokazati veličinu razlike, njezinu nesigurnost i nazivnike na
kojima se temelje prikazani udjeli.

Postupak ćemo razviti na uzorku od 800 zamišljenih osoba iz već poznatog skupa
`populacija_medija` (Šikić, 2026). Riječ je o računalno stvorenim podacima za
nastavu, pa rezultati ne opisuju stvarne medijske navike stanovnika Hrvatske.
Iz svakog zapisa izdvojit ćemo dobnu skupinu i glavni izvor vijesti,
televiziju, radio, tisak, portal ili društvene mreže. Želimo saznati kako se
izbor izvora razlikuje među dobnim skupinama.

Najprije ćemo prebrojiti odgovore i usporediti postotke unutar skupina. Potom
ćemo izračunati očekivane frekvencije pod pretpostavkom nezavisnosti i
hi-kvadrat testom procijeniti ukupno odstupanje od toga modela. Reziduali će
nam pomoći pronaći ćelije s izraženim odstupanjima, a Cramérovo V opisati
jačinu povezanosti. Razmotrit ćemo i kako se analiza mijenja kada raspodjelu
uspoređujemo s unaprijed zadanim udjelima ili kada su očekivani brojevi u
ćelijama mali.

Izbor kategorija i usporedbe oblikuje zaključak. Pri opisu povezanosti dobi
i izvora vijesti zato ćemo navesti i što nam još treba za njezino
objašnjenje.

## Brojanje prije testiranja

Kategoričke varijable razvrstavaju jedinice u skupine. Dobna skupina, izvor
vijesti, obrazovanje i regija primjeri su takvih varijabli. Analiza počinje
brojanjem jedinica u svakoj kategoriji, pa prvo trebamo provjeriti što smo i
koga prebrojili.

Frekvencija je broj jedinica u kategoriji. Za udio trebamo i **uvjetni
nazivnik**, skupinu unutar koje računamo postotak. Tvrdnja da četrdeset posto
ispitanika bira društvene mreže može se odnositi na cijeli uzorak, samo
najmlađu dobnu skupinu ili samo osobe koje su odgovorile. Bez navedenog
nazivnika čitatelj ne može provjeriti značenje postotka.

Prije brojanja određujemo kategorije. Dob možemo podijeliti na različite
skupine, a portal i društvene mreže promatrati zajedno ili odvojeno. To je dio
operacionalizacije. Test zatim uspoređuje raspored unutar tih kategorija, ali
ne provjerava jesmo li ih sadržajno dobro odabrali.

**Kontingencijska tablica** je tablica frekvencija u kojoj svaka ćelija sadrži
broj jedinica koje istovremeno pripadaju jednoj kategoriji retka i jednoj
kategoriji stupca.

U našoj će tablici retci predstavljati dobne skupine, a stupci izvore vijesti.
Ćelija na sjecištu najmlađe skupine i televizije pokazat će koliko najmlađih
bira televiziju. Zbroj cijelog retka obuhvatit će sve osobe te dobi, neovisno o
njihovu izvoru, a zbroj stupca sve korisnike televizije, neovisno o dobi. Takvi
rubni zbrojevi daju raspodjelu svake varijable zasebno, dok unutarnje ćelije
čuvaju njihove kombinacije.

Prijelaz od zapisa do tablice možemo provjeriti na najmlađoj skupini.
Svaka od njezinih `r sum(s13_tablica[1, ])` osoba ulazi u točno jednu ćeliju.
Među njima `r s13_tablica[1, "društvene mreže"]` bira društvene mreže, pa
njihov udio računamo kao `r s13_tablica[1, "društvene mreže"]` podijeljeno s
`r sum(s13_tablica[1, ])`. Ostale retke gradimo istim prebrojavanjem.

*Slika. Dob i glavni izvor vijesti u istom simuliranom uzorku. Izrada autora.*

Postoci po retku pokazuju kako su izvori vijesti raspoređeni unutar dobne
skupine. Postoci po stupcu pokazuju dobni sastav korisnika pojedinog izvora.
Ovdje koristimo postotke po retku jer želimo usporediti izbor izvora među
dobnim skupinama različitih veličina. Kad bi nas umjesto toga zanimalo
koji dio televizijske publike čine najstariji, koji bismo nazivnik trebali
odabrati? Sada bismo broj najstarijih korisnika televizije dijelili brojem
svih korisnika televizije. Promijenilo se pitanje, pa isti zapisi traže
postotak po stupcu. Duljine stupaca na sljedećoj slici ipak prikazuju prvo
pitanje, udjele izvora unutar svake dobne skupine.

*Slika. Udio pojedinog izvora vijesti unutar svake dobne skupine u simuliranom uzorku od osamsto osoba. Raspodjele izvora razlikuju se među dobnim skupinama; udjeli se unutar svake skupine zbrajaju do 100 %. Izrada autora prema @sikic2026.*

Društvene mreže bira `r hr_broj(s13_retci["18 do 29", "društvene mreže"])` % osoba od 18 do 29 godina, a `r hr_broj(s13_retci["60 i više", "društvene mreže"])` % osoba
od 60 i više godina. Televiziju bira `r hr_broj(s13_retci["18 do 29", "TV"])` % najmlađih i `r hr_broj(s13_retci["60 i više", "TV"])` %
najstarijih. Obrazac je jasan u uzorku. Sada trebamo provjeriti koliko bi
takav raspored bio neobičan kada u populaciji ne bi bilo veze.

## Očekivano pod nezavisnošću

Opažene razlike među dobnim skupinama sada trebamo usporediti s rasporedom u
kojem dobi i izvoru vijesti ne bismo pripisali povezanost. Pritom zadržavamo
broj osoba u svakoj dobnoj skupini i ukupan broj korisnika svakog izvora. Iz
tih rubnih zbrojeva možemo izračunati očekivane frekvencije pod pretpostavkom
nezavisnosti.

Ako televiziju bira petina cijelog uzorka, pod nezavisnošću bismo očekivali
isti udio u svakoj dobnoj skupini. Očekivani broj u ćeliji dobivamo primjenom
udjela stupca na broj osoba u retku.

**Očekivana frekvencija** ćelije je umnožak zbroja njezina retka i zbroja
njezina stupca podijeljen ukupnim brojem jedinica, dakle broj koji bi se u toj
ćeliji nalazio kad bi dvije varijable bile nezavisne uz nepromijenjene rubne
zbrojeve.

Oznaka $E_{ij}$ predstavlja očekivanu frekvenciju u i-tom retku i j-tom
stupcu. Oznaka $n_{i\cdot}$ predstavlja zbroj i-tog retka, $n_{\cdot j}$ zbroj j-tog
stupca, a $n$ ukupan broj jedinica.

$$E_{ij} = \frac{n_{i\cdot} \times n_{\cdot j}}{n}$$

U istoj tablici televiziju bira ukupno `r sum(s13_tablica[, "TV"])` od
800 osoba. Za najmlađe zato očekujemo
$`r sum(s13_tablica[1, ])` \times `r sum(s13_tablica[, "TV"])` / 800 =
`r hr_broj(s13_test$expected[1, "TV"], 2)`$ korisnika televizije, a opažamo
ih `r s13_tablica[1, "TV"]`. Očekivani broj smije imati decimale jer opisuje
modelsku referencu, a ne dodatne osobe koje smo zabilježili.

Prije nastavka možemo dopuniti isti račun za najstariju skupinu. U njoj je
`r sum(s13_tablica[4, ])` osoba, a zajednički udio korisnika televizije i
dalje iznosi `r sum(s13_tablica[, "TV"])` podijeljeno s 800. Koji broj
dobivamo kada taj udio primijenimo na veličinu najstarije skupine i zašto
u nazivnik ne stavljamo samo broj najstarijih? Vrijedi zapisati račun prije
čitanja objašnjenja u sljedećem odlomku.

Dobivamo `r hr_broj(s13_test$expected[4, "TV"], 2)` očekivanih korisnika
televizije. Udio iz cijelog uzorka određuje referencu pod nezavisnošću,
a broj najstarijih određuje na koliko osoba primjenjujemo tu referencu.
Kad bismo umjesto toga uzeli opaženi udio televizije među najstarijima,
samo bismo rekonstruirali opaženi broj i izgubili usporedbu s nultim modelom.

Nezavisnost znači da se raspodjela izvora vijesti ne mijenja s dobnom
skupinom. To privremeno pretpostavljamo kako bismo izračunali očekivanja i
usporedili ih s podacima.

Najmanja očekivana frekvencija iznosi `r hr_broj(s13$min_ocekivana)`. U našoj tablici nema vrlo
rijetkih očekivanih ćelija. Očekivana frekvencija manja od pet uobičajen je
znak za dodatnu provjeru hi-kvadrat aproksimacije (Cochran, 1954). Taj prag
služi kao upozorenje, a ne kao jamstvo valjanosti ili najava smjera pogreške.
Poslije ćemo provjeriti kako se postupak ponaša uz rijetke ćelije.

Za sljedeći prikaz trebamo dvije sažete mjere. Hi-kvadrat statistika zbraja
doprinose $(O-E)^2/E$ svih ćelija, pa veći broj označuje veće odstupanje od
nezavisnosti uz zadane rubove. Cramérovo V dijeli tu statistiku veličinom
uzorka i dimenzijom tablice prije vađenja korijena. Za tablicu dva puta dva
vrijedi $V=\sqrt{\chi^2/n}$. Tako razdvajamo količinu dokaza od veličine
povezanosti. Nakon prikaza razvijamo opće formule i njihove pretpostavke.

## Interakcija — Očekivano i opaženo

Za ovaj prikaz konstruiramo novu tablicu dviju skupina A i B s odgovorima
„da” i „ne”. Ona ne nastaje izvlačenjem osoba iz prethodnog uzorka. Svaka
skupina ima zadani broj osoba, a ukupno je jednako odgovora „da” i „ne”.
Ako svaka skupina ima 20 osoba, nezavisnost daje po 10 u svakoj ćeliji.
Pomak od 20 % dodaje dva odgovora ćelijama A–da i B–ne, a oduzima dva
preostalima. Dobivamo retke 12 i 8 te 8 i 12, uz nepromijenjene rubne
zbrojeve. Njihov doprinos računamo kao $(12-10)^2/10=0,4$ za prvu ćeliju,
a isto pravilo vrijedi za ostale tri. Zbroj je $4\times0,4=1,6$,
uz $n=40$, pa je $V=\sqrt{1,6/40}=0,20$. Ako sve frekvencije pomnožimo
s četiri, doprinos svake ćelije i hi-kvadrat postaju četiri puta veći,
dok V ostaje 0,20. Prikaz uspoređuje unaprijed zadane
tablice i ne procjenjuje stopu pogreške kroz slučajne uzorke.
Kontrole digitalnog izdanja mijenjaju zadani raspored.

Najprije u svakom retku uspoređujemo opaženu i očekivanu frekvenciju.
Puni krug označuje opaženu vrijednost.
Prazni romb označuje očekivanu, a broj uz oznake doprinos ćelije.
[Prazni krug označuje očekivanu vrijednost. Prvi panel pokazuje podudaranje
opaženoga s očekivanim. U drugome svaka skupina ima 20 osoba, a u trećemu 80. Treći panel zato ima četiri puta veće frekvencije od drugoga uz jednake
postotke. Uz naslove su ukupni hi-kvadrat i Cramérovo V.]

*Slika. Opažene i očekivane frekvencije u tablici dva puta dva s jednakim rubnim zbrojevima.*

**Što isprobati.**

1. Postavite opažene frekvencije jednake očekivanima i pogledajte doprinose.
2. Pomaknite opažanja u oba smjera i provjerite ostaju li rubni zbrojevi jednaki.
3. Povećajte pomak i pratite koliko brže raste ukupno odstupanje od pomaka.
4. Zadržite pomak u postocima i usporedite mali s velikim rubnim zbrojem.

Prije usporedbe rezultata možemo predvidjeti što bi se dogodilo kada bismo
učetverostručili sve četiri frekvencije, a zadržali iste postotke. Bi li
hi-kvadrat ostao isti i bi li se jednako ponašalo Cramérovo V? Ovdje
mijenjamo brojnosti zamišljene tablice radi usporedbe. Kopiranje zapisa
stvarnog istraživanja ne bi stvorilo dodatna neovisna opažanja.

Isti relativni pomak daje veće ukupno odstupanje kada imamo više opažanja. Pri
pomaku od 20 % i povećanju rubnog zbroja svake skupine s 20 na 80 hi-kvadrat
raste s 1,6 na 6,4, a Cramérovo V ostaje 0,20. Relativna jačina veze nije se
promijenila. Promijenila se količina podataka s kojom uspoređujemo opaženi
obrazac i model nezavisnosti. Pri učetverostručenju frekvencija i očekivanja
svaka razlika postaje četiri puta veća. Njezin kvadrat postaje šesnaest puta
veći, a očekivanje u nazivniku četiri puta veće, pa se svaki doprinos i njihov
zbroj učetverostručuju. U računu za V hi-kvadrat i broj osoba rastu zajedno,
zato V ostaje isti.

## Hi-kvadrat i njegova referentna raspodjela

Doprinose ćelija računamo tako da oduzmemo očekivanu frekvenciju od opažene,
razliku kvadriramo i podijelimo očekivanom frekvencijom. Kvadriranjem
sprječavamo poništavanje pozitivnih i negativnih odstupanja. Zbroj doprinosa
sažima odstupanje cijele tablice.

**Hi-kvadrat statistika** je zbroj kvadriranih odstupanja opaženih od očekivanih
frekvencija, pri čemu je svako odstupanje podijeljeno očekivanom frekvencijom
svoje ćelije.

Zbroj označujemo s $\chi^2$. Oznaka $O_{ij}$ predstavlja opaženu, a $E_{ij}$ očekivanu frekvenciju u i-tom
retku i j-tom stupcu.

$$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

Za našu tablicu statistika iznosi `r hr_broj(s13$hi)`, uz `r s13$df` stupnjeva slobode.
Približna p-vrijednost iz hi-kvadrat referentne raspodjele iznosi
`r format.pval(pchisq(s13$hi, s13$df, lower.tail = FALSE), digits = 2, eps = 0.001)`.
Stupnjeve slobode računamo množenjem broja redaka umanjenog za jedan i broja stupaca
umanjenog za jedan.

Stupnjevi slobode proizlaze iz ograničenja rubnih zbrojeva. U tablici dva puta
dva, uz zadane rubove, odabir jedne ćelije određuje preostale tri. U našoj
tablici s četiri retka i pet stupaca možemo slobodno zadati `r s13$df` ćelija.
Ostalih osam određuju rubovi. Broj stupnjeva slobode zato utječe na referentnu
raspodjelu odstupanja.

U poglavlju o testiranju opaženu smo statistiku uspoređivali s vrijednostima
koje nastaju ponavljanjem pod nultim modelom. Ovdje istu ulogu ima teorijska
hi-kvadrat raspodjela odgovarajućih stupnjeva slobode, kada je to približenje
primjereno. Usporedbom naše statistike s tom raspodjelom dobivamo p-vrijednost.
Za jedan stupanj slobode granica na razini 0,05 iznosi `r hr_broj(s13$granica, 2)`. S više
stupnjeva slobode granica je viša.

Hi-kvadrat nam je sažeo odstupanje cijele tablice, ali iz tog broja još ne
vidimo gdje se ono pojavljuje. Za povratak konkretnim dobnim skupinama i
izvorima računamo rezidual svake ćelije. Budući da rubne udjele procjenjujemo
iz iste tablice, oni ograničavaju promjenjivost ćelija. Pri standardiziranju
odstupanja zato uz očekivanu frekvenciju uzimamo u obzir i udjele retka i
stupca. Ako u tablici 2 × 2 uz zadane rubove povećamo jednu ćeliju,
preostale tri moraju se odgovarajuće promijeniti. Četiri odstupanja zato
nisu četiri slobodna podatka.

**Prilagođeni standardizirani rezidual** ćelije je razlika opažene i očekivane
frekvencije podijeljena procijenjenom standardnom devijacijom te razlike, koja
uzima u obzir rubne udjele retka i stupca.

Oznaka $e$ označuje ostatak, $p_{i\cdot}$ rubni udio retka, a $p_{\cdot j}$
rubni udio stupca. Slovo $r$ u knjizi zadržavamo za korelaciju.

$$e_{ij} = \frac{O_{ij} - E_{ij}}
{\sqrt{E_{ij}(1-p_{i\cdot})(1-p_{\cdot j})}}$$

Pozitivan rezidual pokazuje više opažanja nego što model očekuje, a negativan
manje. Kada je aproksimacija primjerena, apsolutna vrijednost oko dva može
upozoriti na neuobičajeno odstupanje. To je orijentir za čitanje. Pregled
mnogo reziduala nakon ukupnog testa zahtijeva oprez zbog višestrukih
usporedbi.

Najveći pozitivan rezidual pripada televiziji među osobama od 60 i više godina
i iznosi `r hr_broj(s13_rez["60 i više", "TV"], 2)`. Najveći negativan pripada društvenim mrežama u istoj
skupini i iznosi `r hr_broj(s13_rez["60 i više", "društvene mreže"], 2)`. Među najmlađima predznaci su obrnuti, s `r hr_broj(s13_rez["18 do 29", "društvene mreže"], 2)`
za mreže i `r hr_broj(s13_rez["18 do 29", "TV"], 2)` za televiziju. Tako ukupno odstupanje možemo povezati s
konkretnim skupinama i izvorima.

## Značajno nije isto što i snažno

Hi-kvadrat raste s veličinom uzorka. Uz iste postotke tablica na osam tisuća
osoba daje deset puta veću statistiku nego tablica na osamsto. Zato
p-vrijednost ne može mjeriti jačinu veze. Mijenja se i kada relativni obrazac
ostane isti.

Cramérovo V prilagođava hi-kvadrat veličini uzorka i dimenzijama tablice.
Kreće se između nule i jedinice. Nula označuje nezavisnost u tablici, a
jedinica najjaču povezanost koju ta mjera može prikazati.

**Cramérovo V** je korijen hi-kvadrat statistike podijeljene umnoškom veličine
uzorka i manje dimenzije tablice umanjene za jedan.

Oznakom $V$ označujemo tu mjeru. U formuli je $n$ ukupan broj jedinica, a $k$ manji od broja redaka i broja
stupaca.

$$V = \sqrt{\frac{\chi^2}{n\,(k-1)}}$$

U našoj tablici V iznosi `r hr_broj(s13$v, 2)`. Jednaka vrijednost V-a ne nosi univerzalnu oznaku male ili velike veze
za tablice različitih dimenzija. Važnost veze trebamo
procijeniti prema pitanju i ranijim nalazima iz istog područja.

Za odluku su često jasniji postoci. Televiziju bira `r hr_broj(s13_retci["18 do 29", "TV"])` % najmlađih i
`r hr_broj(s13_retci["60 i više", "TV"])` % najstarijih ispitanika. Uredništvo može tu razliku povezati s
raspodjelom resursa. V sažima jačinu veze, ali ne zamjenjuje čitanje pojedinih
udjela.

## Referentna raspodjela je istraživačka odluka

Dosad smo uspoređivali dob i izvor vijesti. Na istih 800 zapisa možemo
postaviti drukčije pitanje, odgovara li sastav uzorka prema obrazovanju
poznatom sastavu naše simulirane populacije. Zadržavamo osobe, ali sada
brojimo samo razine obrazovanja. Za svaku razinu očekivani broj dobivamo
množenjem 800 s njezinim udjelom u populaciji. U tablici je uz taj broj i
druga moguća referenca, 200 osoba po razini, koja bi slijedila iz pretpostavke
o četiri jednako zastupljene kategorije.

*Slika. Ista opažanja prema dvjema referencama. Izrada autora.*

Prvi redak sada možemo usporediti s dvama različitim očekivanjima, a zatim
isti račun ponoviti za preostale razine. Taj postupak zovemo **testom
prilagodbe**. Zbrajanje kvadriranih odstupanja podijeljenih očekivanim
brojevima ostaje isto kao prije. Uz četiri izvana zadane kategorijske vjerojatnosti raspodjela ima tri stupnja slobode, jedan manje od broja kategorija. Očekivanja ovdje zadajemo izvana, umjesto da ih računamo iz rubnih zbrojeva
tablice dviju varijabli.

Ako pretpostavimo jednaku zastupljenost četiriju razina obrazovanja,
statistika iznosi `r hr_broj(s13$gof_ravno)`, uz p-vrijednost manju od 0,001. To pokazuje velik nesklad. Ako koristimo poznate
udjele simulirane populacije, statistika iznosi `r hr_broj(s13$gof_pop, 2)`, uz p-vrijednost
`r hr_broj(s13$p_gof_pop, 2)`. Drugi test ne pokazuje jasan nesklad, ali ne dokazuje jednakost.
Najveća opažena razlika jednog udjela prema populacijskom iznosi `r hr_broj(s13$gof_max_razlika, 1)`
postotnih bodova.

Oba računa mogu biti točna jer ispituju različite tvrdnje. Jednaki udjeli
ovdje nemaju sadržajno opravdanje, dok poznata populacijska raspodjela ima. U
stvarnom istraživanju referenca obično nije tako sigurno poznata. Trebamo je
odabrati i obrazložiti prije testa.

Ista pitanja o kategorijama i nazivnicima pojavljuju se kada brojimo kodirane
tekstove. Jedinica tada može biti dokument, objava ili govor. Prije tablice
navodimo tko je odredio kodnu knjigu i pravila razvrstavanja, a nazivnik usklađujemo s jedinicama koje zadovoljavaju uvjete za kodiranje. Posebno prikazujemo nekodirane
jedinice i one kojima je dodijeljeno više oznaka.

Ako retci predstavljaju izvor teksta, a stupci kodiranu kategoriju, nalaz
ovisi i o tekstovima i o pravilima kodiranja. U poglavlju o algoritmima istu
ćemo logiku primijeniti na tablicu zabune. I ondje moramo znati kako su
kategorije nastale i koji je nazivnik svakog udjela.

## Kad je aproksimacija tanka

U prethodnoj analizi 800 simuliranih osoba najmanja očekivana frekvencija
iznosi `r hr_broj(s13$min_ocekivana)` pa nijedna ćelija nije osobito rijetka.
Da bismo vidjeli što se događa kada očekivani brojevi postanu mali, privremeno
napuštamo taj uzorak i pojednostavljujemo pitanje. U zasebnom nastavnom
pokusu imamo dvije hipotetske dobne skupine i samo odgovor koristi li osoba
određenu društvenu mrežu. To nisu novi podaci o Hrvatskoj niti podskup
prethodnih 800 zapisa.

Najprije nas zanima koliko često test prijavljuje vezu koje u modelu nema.
Svakoj zamišljenoj osobi neovisno dodjeljujemo odgovor „da” s unaprijed
zadanom vjerojatnošću, a inače odgovor „ne”. Jednake vjerojatnosti u objema
skupinama stvaraju nulti model. U većem uzorku generiramo po 200 osoba, a u
manjem po 20. Donja dva retka tablice mijenjaju pitanje i poslužit će poslije
za procjenu snage, kada je veza ugrađena u model.

| Svrha i uzorak | Osoba po skupini | „Da” među mlađima | „Da” među starijima |
|---|---:|---:|---:|
| Nula, veći | 200 | 50 % | 50 % |
| Nula, manji | 20 | 10 % | 10 % |
| Snaga, veći | 200 | 60 % | 40 % |
| Snaga, manji | 20 | 16 % | 4 % |

: Pravila zasebnoga nastavnog pokusa. Izrada autora.

Prema prvom nultom modelu u svakoj skupini očekujemo $200 \times 0,50 = 100$
odgovora „da” i 100 odgovora „ne”. U manjem modelu očekujemo
$20 \times 0,10 = 2$ odgovora „da” i 18 odgovora „ne”. To su očekivanja iz
pravila generatora. U pojedinoj izvučenoj tablici ukupan broj korisnika
mreže varira, pa test očekivane frekvencije ponovno računa iz njezinih
ostvarenih rubnih zbrojeva.

Jedno ponavljanje manjega pokusa znači generirati svih 40 odgovora,
prebrojiti ih u tablici i izračunati jednu Pearsonovu statistiku i njezinu
p-vrijednost. Sljedeću smo moguću tablicu namjerno odabrali radi preglednog
računa. Ona nije nasumično izdvojeno ponavljanje iz simulacije.

| Dobna skupina | Koristi mrežu | Ne koristi mrežu | Ukupno |
|---|---:|---:|---:|
| Mlađi | 4 | 16 | 20 |
| Stariji | 0 | 20 | 20 |
| Ukupno | 4 | 36 | 40 |

: Mogući ishod manjega pokusa, odabran za ilustraciju. Izrada autora.

Mrežu koristi 4 od 20 mlađih, odnosno 20 %, i 0 od 20 starijih.
Pod nezavisnošću primjenjujemo zajednički udio $4/40$ na svaku skupinu od
20 osoba. Očekivani brojevi zato su 2 i 18 u oba retka. Ovdje se slučajno
podudaraju s očekivanjima generatora. Da smo dobili ukupno šest korisnika,
test bi očekivao po tri u svakoj skupini. Za prikazanu tablicu četiri
doprinosa Pearsonovoj statistici iznose $4/2$, $4/18$, $4/2$ i $4/18$,
jer je svako opažanje od svoga očekivanja udaljeno za dva. Njihov je zbroj
`r hr_broj(unname(s13_mali_pearson$statistic), 2)`.

Jedan takav ishod ne govori koliko često postupak griješi. Zato svaki
scenarij ponavljamo 4 000 puta. Veličine skupina i vjerojatnosti ostaju
zadane, a svaki put generiramo nove neovisne odgovore. Brojimo koliko puta
Pearsonov test, odnosno test sa zbrojem (opaženo − očekivano)²/očekivano, bez korekcije kontinuiteta daje p-vrijednost manju od 0,05.
Broj odbacivanja dijelimo s 4 000, uključujući ponavljanja bez ijednog
korisnika mreže ili bez ijednog nekorisnika. U njima test nije definiran i
ovdje ih računamo kao neodbacivanja. Tablica ih pokazuje zasebno kako bi
nazivnik ostao vidljiv.

*Slika. Odbacivanja u po 4 000 ponavljanja. Neprimjenjiva ponavljanja ostaju u nazivniku kao neodbacivanja. Izrada autora.*

Prva dva retka procjenjuju lažna odbacivanja jer u njihovim modelima nema
veze. Dobivenih `r hr_broj(s13$null_stopa_velike)` % i
`r hr_broj(s13$null_stopa_male)` % treba čitati uz slučajnu promjenjivost
simulacije. Oko stope od 5 % standardna pogreška na 4 000 ponavljanja iznosi
oko 0,34 postotna boda. Male razlike u postocima zato nisu same po sebi
dokaz razlike u ponašanju postupaka. Rezultat manjega scenarija odnosi se i
na naše pravilo o neprimjenjivim tablicama. U ovom scenariju s malim očekivanim
frekvencijama stopa je ispod 5 %, pa je postupak
konzervativan. Ovaj pokus zato ne pokazuje povećanu pogrešku prve vrste.
Male očekivane frekvencije upozoravaju na nepouzdanu aproksimaciju, ali ne
određuju unaprijed smjer odstupanja.

Vratimo se tablici s četiri korisnika među mlađima i nijednim među starijima.
Želimo provjeriti koliko je taj raspored neobičan bez oslanjanja na glatku
hi-kvadrat krivulju. Zadržimo po 20 osoba u skupinama i ukupno četiri
korisnika mreže. Tada su mogući samo sljedeći rasporedi korisnika, dok
brojeve nekorisnika dobivamo oduzimanjem od 20.

*Slika. Rasporedi četiriju korisnika uz fiksne rubne zbrojeve. Izrada autora.*

Tablice nisu jednako vjerojatne. Dva korisnika u svakoj skupini mogu nastati
na više načina nego sva četiri u jednoj, kada svaki izbor četiriju osoba
među njih 40 ima jednaku vjerojatnost. Primjerice, vjerojatnost posljednjeg
retka dobivamo dijeljenjem broja izbora četiriju među 20 mlađih brojem
izbora četiriju među svih 40 osoba. Za srednji redak biramo dvije među 20
mlađih i dvije među 20 starijih. Tako nastaju uvjetne vjerojatnosti u tablici.

Na tom računu počiva **Fisherov egzaktni test**. Za dvostranu p-vrijednost
ovdje zbrajamo vjerojatnosti svih tablica čija je uvjetna vjerojatnost
manja ili jednaka vjerojatnosti opažene tablice. Posljednjem retku zato
pridružujemo prvi i dobivamo približno
`r hr_broj(s13_fisher$p.value, 3)`. Pearsonov račun bez korekcije za istu
tablicu daje približno `r hr_broj(s13_mali_pearson$p.value, 3)`.
Razlika pokazuje da način računanja referentne vjerojatnosti može promijeniti
odluku pri pragu 0,05. Ne pokazuje da je Fisherova p-vrijednost uvijek veća,
niti jedna odabrana tablica utvrđuje opće ponašanje tih testova. Egzaktnost
se odnosi na račun uz zadane rubove, a ne uklanja nesigurnost malog uzorka,
pogreške mjerenja ili ograničenja nacrta.

Preostaje drugo pitanje, koliko često otkrivamo vezu koja postoji u modelu.
Za **snagu** zato trebamo promijeniti pravila generiranja. Donja dva retka
nacrta daju mlađima i starijima različite vjerojatnosti odgovora „da”. Uz
jednako velike skupine obje razlike odgovaraju populacijskom Cramérovu V od
0,20. U većem scenariju razlika udjela iznosi 0,20 uz zajednički udio 0,50,
a u manjem 0,12 uz zajednički udio 0,10. Standardiziranje tih razlika daje
istu vrijednost V, iako su apsolutne razlike različite. Za dvije jednako velike skupine vrijedi $V=|p_1-p_2|/[2\sqrt{\bar p(1-\bar p)}]$. Zato su računi $0,20/[2\sqrt{0,50\cdot0,50}]=0,20$ i $0,12/[2\sqrt{0,10\cdot0,90}]=0,20$.

Sada svaki odbačeni nulti model znači otkrivenu ugrađenu vezu. Od po 4 000
ponavljanja odbacujemo u `r hr_broj(s13$snaga_velike)` % većih i
`r hr_broj(s13$snaga_male)` % manjih uzoraka. Između scenarija mijenjaju se
i broj osoba i učestalost korištenja mreže, pa cijelu razliku u snazi ne
možemo pripisati samo veličini uzorka. Ta dva retka ne procjenjuju pogrešku
prve vrste niti pouzdanost pojedine odluke.

U početnoj analizi dobi i izvora vijesti ove provjere usmjeravaju čitanje
tablice. Najprije provjeravamo brojanja i očekivane frekvencije, zatim
primjerenost referentnog računa, a uz test i dalje navodimo udjele, njihovu
razliku i nesigurnost. Pouzdaniji račun p-vrijednosti ne zamjenjuje pitanje
što kategorije predstavljaju i na koga se uzorak odnosi.

Odluka o spajanju kategorija traži i sadržajno opravdanje. Sljedeći
primjer pokazuje što se pritom može izgubiti iz istraživačkog pitanja.

**Statistika u divljini.**
**Gdje su nestali slušatelji radija?**

Zamislimo da gradska knjižnica želi saznati kako stanovnici doznaju za
njezina događanja. Treba odlučiti gdje će objavljivati obavijesti i na koje
će kanale usmjeriti ograničeno vrijeme zaposlenika. U anketi zato pita za
dob i glavni izvor informacija. Među odgovorima su društvene mreže, portal,
radio i tiskane obavijesti.

Tim sastavlja tablicu i pokreće hi-kvadrat test. U nekim kombinacijama dobi
i izvora očekivani su brojevi manji od pet. Netko predlaže da radio i
tiskane obavijesti spoje u kategoriju „ostalo”. Nakon spajanja upozorenje programa nestaje i tim smatra da je analiza
spremna za izvještaj.

Ali vratimo se odluci zbog koje je anketa provedena. Knjižnica želi znati
kojim kanalima može dosegnuti različite stanovnike. Ako su radio i tiskane
obavijesti spojeni, nova tablica više ne pokazuje njihove zasebne obrasce.
Čak i kada je takva podjela opravdana za određeni test, iz nje ne možemo
odgovoriti treba li knjižnica nastaviti suradnju s radijem ili drukčije
rasporediti tiskane obavijesti.

Tako se tehničko pitanje o očekivanim frekvencijama pretvorilo u pitanje o
sadržaju istraživanja. Preporuka o pragu pet služi procjeni hi-kvadrat
aproksimacije (Cochran, 1954). Sama po sebi ne govori koje odgovore ima
smisla spojiti niti koji je komunikacijski kanal važan za knjižnicu. Mali
broj odgovora također ne znači da su ljudi iza tih odgovora nevažni. Znači
da o njihovim navikama možda imamo malo informacija.

Tim zato najprije treba sačuvati pregled izvornih frekvencija i udjela.
Zatim može procijeniti prikladnost postupka, razmotriti drugi način
računanja p-vrijednosti ili obrazložiti podjelu kategorija koja odgovara
istraživačkom pitanju. Ako podaci nisu dovoljni za odluku o pojedinom
kanalu, i to treba jasno napisati.

Prisjetimo se simulacije iz ovoga poglavlja. Provjeravali smo i lažne uzbune
i sposobnost otkrivanja postojeće veze. Nestanak upozorenja iz programa ne
jamči da imamo dovoljno podataka za odgovor koji knjižnici treba.

Prije spajanja kategorija zato pitajmo što ćemo nakon spajanja još moći
saznati. U ovom slučaju to pitanje određuje hoće li slušatelji radija ostati
vidljivi u zaključku istraživanja.

**Nađite grešku.**
Može li ovaj zaključak u izvještaj?

Upravo smo vidjeli da pri tumačenju testa trebamo provjeriti očekivane
frekvencije i razlikovati statističku značajnost od jačine povezanosti.
Vratimo se sada uzorku od 800 zamišljenih osoba i pogledajmo kako se te
provjere koriste pri pisanju izvještaja.

Kolegica je analizirala povezanost dobne skupine i glavnog izvora vijesti.
Prije predaje rada zamolila vas je da pregledate njezin zaključak.
Poslala vam je sažetak rezultata.

| Što je provjereno ili izračunano | Rezultat |
|---|---:|
| Broj osoba u simuliranom uzorku | 800 |
| Broj dobnih skupina i izvora vijesti | 4 skupine i 5 izvora |
| Najmanja očekivana frekvencija | 14,3 |
| Hi-kvadrat statistika | 149,8 |
| Stupnjevi slobode | 12 |
| p-vrijednost | < 0,001 |
| Cramérovo V | 0,25 |

: Sažetak analize simuliranog uzorka. Izrada autora prema sikic2026.

U izvještaju je zadržala i dio opisa koji čitatelju pokazuje kako se
skupine razlikuju.

| Dobna skupina | Televizija kao glavni izvor | Društvene mreže kao glavni izvor |
|---|---:|---:|
| Od 18 do 29 godina | 12,2 % | 42,1 % |
| 60 i više godina | 45,2 % | 2,2 % |

: Dio postotaka po dobnim skupinama. Izrada autora prema sikic2026.

Postoci su izračunani unutar svake dobne skupine. Prikazana su dva od pet
izvora, pa se postoci u retku ne zbrajaju do sto.

Ispod tablica napisala je sljedeće.

> Sve očekivane frekvencije veće su od pet. Hi-kvadrat test daje
> p-vrijednost manju od 0,001, pa podaci snažno odstupaju od modela
> nezavisnosti. Budući da je p-vrijednost tako mala, povezanost dobi i
> izvora vijesti vrlo je snažna.

Prije nego što joj odgovorite, povežite svaku rečenicu s rezultatom na
koji se oslanja.

1. Koja rečenica izvodi zaključak koji navedeni pokazatelj ne opravdava?
2. Koji rezultat trebate koristiti za opis jačine povezanosti, a koji dio
   prikaza pomaže objasniti njezino praktično značenje?
3. Prepravite završnu rečenicu. Zadržite ono što rezultati pokazuju, ali
   nemojte veličinu povezanosti zaključivati iz p-vrijednosti.

## Razrađeni primjer

Spajanje kategorija možemo razmotriti na pitanju koje smo sadržajno odredili
prije računa. Umjesto razlika među svih pet izvora sada nas zanima razlikuje li
se izbor digitalnih i tradicionalnih izvora među dobnim skupinama. Portal i
društvene mreže svrstavamo u digitalne, a televiziju, tisak i radio u
tradicionalne izvore. Ta podjela odgovara novom pitanju i stvara novu varijablu. Najprije ćemo pročitati njezine
udjele, a zatim ukupno odstupanje od nezavisnosti.

Vraćamo se istim zapisima svih 800 osoba, a zasebni pokus s dvjema skupinama
ovdje završava. Nijednu osobu ne izbacujemo. Primjerice, u najmlađem retku
zbrajamo `r s13_tablica[1, "portal"]` korisnika portala i
`r s13_tablica[1, "društvene mreže"]` korisnika mreža, što daje
`r s13_spojena[1, "digitalni"]` digitalnih korisnika. Preostali izvori daju
`r s13_spojena[1, "tradicionalni"]` tradicionalnih korisnika. Nazivnik
retka ostaje `r sum(s13_tablica[1, ])`.

*Slika. Iste osobe nakon spajanja izvora u dvije kategorije. Izrada autora.*

Za konkretnu usporedbu najmlađih i najstarijih čitamo udjele digitalnih izvora.
Bira ih `r hr_broj(s13_digitalni[["18 do 29"]])` % najmlađih i `r hr_broj(s13_digitalni[["60 i više"]])` % najstarijih. Razlika
iznosi `r hr_broj(s13$razlika_digitalni, 1)` postotnih bodova, uz 95-postotni interval od
`r hr_broj(s13$ci_digitalni[[1]], 1)` do `r hr_broj(s13$ci_digitalni[[2]], 1)`. Ukupni test, koji obuhvaća sve dobne
skupine, odgovara na šire pitanje o povezanosti u cijeloj tablici. Hi-kvadrat
iznosi `r hr_broj(s13$hi_spojena)`, uz `r s13$df_spojena` stupnja slobode, a V iznosi
`r hr_broj(s13$v_spojena, 2)`. Za pet kategorija V je bio `r hr_broj(s13$v, 2)`. Razlika tih
vrijednosti ne govori koja je podjela bolja. Prva čuva razlike među
pojedinačnim izvorima, a druga opisuje digitalno-tradicionalnu podjelu.
Usporedba pokazuje koliko zaključak ovisi o operacionalizaciji. Interval
razlike udjela računan je normalnom aproksimacijom s odvojenim procjenama
varijance dvaju udjela, bez korekcije kontinuiteta. Pretpostavlja neovisne
osobe i skupine te dovoljno velike brojnosti u svakoj od četiriju ćelija.

Tablica opisuje povezanost dobi i izbora izvora. Ne utvrđuje potječe li ona od
ranije stečenih navika, dostupnosti uređaja ili životnog razdoblja. Za
razdvajanje tih objašnjenja trebali bismo dodatne varijable i prikladan nacrt.
U poglavlju o regresiji naučit ćemo zajedno razmatrati više varijabli.

Iz dobivenih rezultata sada možemo sastaviti kratak izvještaj.

> U slučajnom uzorku od 800 osoba iz nastavne simulacije usporedili smo
> izbor digitalnih i tradicionalnih izvora među dobnim skupinama
> (Šikić, 2026). Digitalne izvore bira
> `r hr_broj(s13_digitalni[["18 do 29"]])` % osoba od 18 do 29 godina i
> `r hr_broj(s13_digitalni[["60 i više"]])` % osoba od 60 i više godina. Razlika iznosi
> `r hr_broj(s13$razlika_digitalni, 1)` postotnih bodova uz 95-postotni
> interval od `r hr_broj(s13$ci_digitalni[[1]], 1)` do
> `r hr_broj(s13$ci_digitalni[[2]], 1)`. Za cijelu tablicu hi-kvadrat iznosi
> `r hr_broj(s13$hi_spojena)`, uz `r s13$df_spojena` stupnja slobode
> i p-vrijednost manju od 0,001, a Cramérovo V `r hr_broj(s13$v_spojena, 2)`. Rezultat opisuje
> generirane osobe i ne daje procjenu medijskih navika stanovnika Hrvatske
> niti dokaz da dob uzrokuje izbor izvora.

Prva rečenica određuje pitanje i podatke. Sljedeće daju opaženi obrazac
i preciznost usporedbe najmlađih s najstarijima. Ukupni test i V odnose se
na sve četiri dobne skupine, pa ne zamjenjuju taj konkretni kontrast.
Završna rečenica određuje doseg nalaza. Za uredničku publiku mogli bismo
u prvi plan staviti razliku u postotnim bodovima, a tehničke pokazatelje
ostaviti u pratećoj tablici. Oznaka simulacije, nazivnici i granice zaključka
moraju ostati i u kraćoj verziji.

Za dodatnu provjeru slijedi programski račun prethodne analize.

Kod preuzima uzorak i učitane pakete iz već pripremljene analize poglavlja. U računu pratimo isti put kojim smo čitali prethodnu tablicu. Poziv
`table` prebroji kombinacije dobne skupine i nove podjele izvora, a
`prop.table` pretvori frekvencije u udjele prema zadanom smjeru. Tek potom
`chisq.test` sažima odstupanje od nezavisnosti u hi-kvadrat, određuje
stupnjeve slobode i računa p-vrijednost prema referentnoj raspodjeli. Za tablicu 2 × 2 R zadano primjenjuje korekciju kontinuiteta, koja ublažava prijelaz s diskretnih brojanja na kontinuiranu krivulju. Za ovdje opisani nekorigirani račun treba navesti `correct = FALSE`.

Vratimo se Berkeleyju. Zbirna tablica pokazivala je povezanost spola i ishoda
prijave (Bickel, 1975). Hi-kvadrat, V i reziduali mogli bi opisati taj obrazac,
ali ne i objasniti ga. Nedostajao je odjel prijave. Muškarci i žene nisu se
jednako raspoređivali po odjelima, a odjeli su imali različite stope prijma. U
poglavlju Zašto statistika vidjeli smo Berkeleyjev primjer, a u poglavlju
o povezanosti pokazali smo kako dodavanje takva sloja može
promijeniti zbirni obrazac (Simpson, 1951). Statistički opis dviju varijabli
zato treba razlikovati od objašnjenja mehanizma.

## Sažetak

Od brojanja kategorija prelazimo na usporedbu tek kada odredimo nazivnik svakog
udjela. Model nezavisnosti tada iz rubnih zbrojeva daje očekivane frekvencije s
kojima uspoređujemo opaženu tablicu. Hi-kvadrat sažima ukupno odstupanje,
reziduali ga vraćaju konkretnim ćelijama, a Cramérovo V pomaže odvojiti jačinu
veze od količine podataka. Ako umjesto nezavisnosti provjeravamo podudaranje sa
zadanom raspodjelom, trebamo obrazložiti tu referencu. Male očekivane
frekvencije mogu oslabiti aproksimaciju, pa razmatramo Fisherov postupak ili
sadržajno opravdanu novu podjelu kategorija, svjesni da potonjom mijenjamo
pitanje. U sljedećem poglavlju zadržat ćemo usporedbu skupina, ali ćemo umjesto
rasporeda kategorija promatrati brojčani ishod.

Nazivi neovisnost i nezavisnost u ovom probabilističkom značenju označavaju isti odnos. Neovisnost znači da zajedničku vjerojatnost možemo dobiti množenjem pojedinačnih vjerojatnosti. Zato očekivane frekvencije u tablici nastaju umnoškom rubnih udjela i ukupnog broja osoba.

## Pojmovi

stupnjevi slobode (*degrees of freedom*), doprinos ćelije (*cell contribution*),
kontingencijska tablica (*contingency table*), uvjetni nazivnik (*conditional
denominator*), očekivana frekvencija (*expected frequency*), hi-kvadrat
statistika (*chi-squared statistic*), prilagođeni standardizirani rezidual
(*adjusted standardized residual*), test prilagodbe (*goodness-of-fit test*),
referentna raspodjela (*reference distribution*), Cramérovo V (*Cramér's V*),
Fisherov egzaktni test (*Fisher's exact test*)

## Zadaci

Nakon vlastitog pokušaja otvorite naznake i provjere rješenja.

### Konceptualni

Objasnite razliku između testa nezavisnosti i mjere jačine veze tako da
napišete dvije rečenice koje bi se mogle pojaviti u istom izvještaju, jednu o
tome što test kaže i jednu o tome što V kaže.

Zatim izvještaj iz razrađenog primjera preoblikujte u tri rečenice za
novinara. Zadržite oznaku simulacije, dobne skupine, nazivnike postotaka,
razliku s intervalom i granicu zaključka. Obrazložite koji biste tehnički
pokazatelj ostavili u pratećoj tablici i zašto njegovo izostavljanje iz
glavnog teksta ne mijenja značenje nalaza.

### Računski

Tablica ima dva retka s po sto ispitanika i dva stupca s rubnim zbrojevima
stodvadeset i osamdeset. Izračunajte sve četiri očekivane frekvencije, a zatim
za opaženu tablicu sa sedamdeset u prvoj ćeliji izračunajte doprinos svake
ćelije i njihov zbroj. Usporedite ga s graničnom vrijednošću 3,84.

### Kritički

Vratite se na Simpsonov paradoks iz poglavlja Zašto statistika i na Berkeleyjev
slučaj (Bickel, 1975). Skicirajte zbirnu tablicu spola i ishoda prijave te skup
odjelskih tablica koje vraćaju izostavljeni sloj. Objasnite zašto hi-kvadrat
test prve tablice ne može razlikovati razliku u sastavu prijava od razlike u
odlučivanju unutar odjela. Predajte obje sheme, jedan odlomak usporedbe i naziv
varijable bez koje se ta dva objašnjenja ne mogu razdvojiti.

### Revizija modela

Vratite se izvještaju iz okvira o pogrešci. Izdvojite dijagnostičke
korake koji su provedeni ispravno i jedan pogrešan zaključak. Napišite
zamjenski odlomak koji rabi već navedeno Cramérovo V i uspoređuje udjele
unutar dobnih skupina. Objasnite što provjera očekivanih frekvencija
potvrđuje, a koje pretpostavke njome još nisu provjerene. Ne dodjeljujte
jačini univerzalnu oznaku bez sadržajnog obrazloženja.

---

# Uspoređivanje dviju grupa

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/14-dvije-grupe.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Cumming predlaže da usporedbu skupina izvještavamo procjenom razlike i
njezinim intervalom (Cumming, 2014). Tako čitatelj vidi više od oznake da je
rezultat statistički značajan.

Iz procjene saznajemo kolika je razlika, a iz intervala koliko smo je precizno
odredili. Te brojke možemo usporediti s ranijim nalazima i s razlikom koja bi
bila važna za odluku.

Kako odabrati usporedbu koja odgovara istraživačkom nacrtu i iz nje napisati
jasan zaključak?

Oznaka glavnoga izvora vijesti u prethodnom nam je poglavlju služila za
brojanje osoba u kategorijama. Sada uz oznaku skupine promatramo brojčani
odgovor. Zanima nas koliko se prosječno povjerenje u medije razlikuje među
skupinama i koliko smo tu razliku precizno procijenili. Poznato pitanje o
povezanosti time dobiva drukčiji oblik podataka i drukčiji račun.

U glavnom primjeru koristimo uzorak od 120 zamišljenih osoba iz skupa
`populacija_medija` kojima su televizija ili društvene mreže glavni izvor
vijesti (Šikić, 2026). Svaki redak predstavlja jednu osobu s ocjenom povjerenja
u medije. Time mijenjamo skupine u odnosu na usporedbu tiska i portala iz
poglavlja o testiranju. Podaci i dalje pripadaju nastavnoj simulaciji. Na njima možemo usporediti postupke za isti jasno određen odnos.

Za izbor postupka vratit ćemo se nacrtu istraživanja. Razlika između rezultata različitih ljudi i promjena izmjerena na istim
ljudima traže različite račune. Zasebno ćemo razmotriti i usporedbu jedne sredine s unaprijed
zadanom vrijednošću. Na simuliranim ponovljenim mjerenjima provjerit ćemo kako
očuvanje parova mijenja procjenu nesigurnosti. To nas vodi do različitih
oblika t-testa, uz isto polazište u procjeni razlike.

Intervale, veličinu učinka i pogreške odluke već poznajemo, pa možemo
usmjeriti pozornost na to koji račun odgovara kojim opažanjima. Welchov
postupak usporedit ćemo s linearnim modelom u kojem oznaka skupine postaje
prediktor, odnosno varijabla kojom model opisuje razlike u ishodu. Provjerit
ćemo zašto jednaka procjena razlike ne mora značiti
jednaku standardnu pogrešku. Grafovima ćemo pregledati pretpostavke i
razmotriti što mijenja postupak temeljen na rangovima. Naš će izvještaj
povezati nacrt, procjenu i njezine granice. Sama razlika u povjerenju neće nam
reći što bi se dogodilo kada bi osoba promijenila izvor vijesti.

## Tko nosi dva rezultata

Prije nego što izaberemo račun za razliku, trebamo razjasniti što uspoređujemo.
Jesu li to odgovori različitih ljudi, dva mjerenja istih ljudi ili rezultat
jedne skupine prema zadanoj vrijednosti? Ta tri pitanja vode različitim
postupcima.

Možemo usporediti sredinu jedne skupine s unaprijed zadanom vrijednošću,
primjerice sredinom ljestvice ili pragom odluke. Procjena iz ranije ankete
nije takva konstanta. Ima vlastitu nesigurnost, a možda i drukčiju ciljnu
populaciju ili mjerenje, pa pri usporedbi trebamo uvažiti obje procjene. Druga
situacija obuhvaća dvije skupine različitih ljudi, primjerice korisnike
televizije i društvenih mreža. U trećoj iste osobe mjerimo dvaput, prije i
poslije događaja.

**Jedinica neovisnosti** je entitet koji se u istraživanju mogao pojaviti ili
izostati neovisno o ostalima, pa njegove vrijednosti nisu unaprijed vezane uz
vrijednosti bilo koje druge jedinice u istom skupu.

U našoj usporedbi dviju neovisnih skupina jedinica je osoba. Kod ponovljenog
mjerenja osoba ostaje jedinica, ali daje dva povezana rezultata. Dvadeset
osoba mjerenih dvaput zato daje dvadeset razlika, a ne četrdeset neovisnih
mjerenja. Ako zanemarimo povezanost unutar para, pogrešno računamo
nesigurnost. Uz pozitivnu povezanost iz primjera koji slijedi interval postaje
nepotrebno širok.

Najprije zato imenujemo jedinicu i opisujemo veze među mjerenjima. Tek potom
biramo postupak usporedbe.

Ovisnost može nastati i među različitim osobama. Učenici istog razreda ili
članovi istog kućanstva mogu dijeliti uvjete koji utječu na rezultat. Povezani
mogu biti i ljudi u društvenoj mreži. Tada zaseban redak u tablici ne znači
neovisno opažanje. Trebamo zabilježiti strukturu i odabrati postupak koji je
uvažava. Takvi modeli prelaze opseg ovog poglavlja.

## Razlika prije oznake

U usporedbi televizije i društvenih mreža zadržavamo osobe koje navode jedan
od ta dva glavna izvora. Osobe s drugim izvorom ostaju izvan analize, pa se
procjena odnosi samo na odabranu usporedbu unutar simulirane populacije.

U izvještaju prvo navodimo razliku u izvornim jedinicama i njezin interval.
Zatim prikazujemo test i standardiziranu razliku. Tako čitatelj prije odluke o
nuli može procijeniti veličinu i nesigurnost opaženog odnosa.

Nakon ograničavanja populacije na ta dva izvora izvukli smo 120 osoba bez
ponavljanja. To je novi uzorak, ne podskup ranijih 800 osoba. Broj korisnika
svakog izvora nije unaprijed zadan. Zbrajanjem njihovih odgovora i dijeljenjem
odgovarajućim brojem osoba dobivamo dvije sredine.

*Slika. Od odgovora do sredina u novom uzorku od 120 osoba. Izrada autora.*

U retku društvenih mreža dijelimo `r sum(s14_mreze)` s
`r length(s14_mreze)`, a u retku televizije `r sum(s14_tv)` s
`r length(s14_tv)`. Zatim od televizijske sredine oduzimamo sredinu mreža.
Kada raspršenost procjenjujemo iz istog uzorka, njezina nesigurnost također
ulazi u zaključak. **t-raspodjela** zvonasta je referentna krivulja s debljim
repovima od normalne. Pri manje podataka zato traži veću udaljenost od
nule. Kako raste broj stupnjeva slobode, približava se normalnoj krivulji.
**Kritična t-vrijednost** omeđuje središnjih 95 % te referentne raspodjele
za obostrani 95-postotni interval.

Stupnjevi slobode opisuju koliko neovisnih odstupanja ostaje nakon procjene
sredina. U jednoj skupini procijenjena sredina veže zbroj odstupanja na nulu,
pa ostaje n − 1. Združeni postupak za dvije skupine koristi n₁ + n₂ − 2
uz pretpostavku zajedničke varijance. Welchov postupak umjesto toga računa
efektivnu vrijednost prema doprinosu nesigurnosti svake skupine. Ona može
biti razlomljena i ne predstavlja broj osoba.

Za interval trebamo i nesigurnost te razlike. Welchov račun zbraja dvije
procijenjene varijance sredina, $s_T^2/n_T+s_M^2/n_M$,
i iz njihova zbroja vadi korijen. Dobivenu standardnu pogrešku
`r hr_broj(s14$se_welch, 3)` množimo pripadnom kritičnom t-vrijednošću i
oduzimamo od razlike te joj dodajemo. Nema izostavljenih odgovora.

U ovome računu Welchovi stupnjevi slobode iznose
`r hr_broj(s14$df_welch, 3)`, a pripadna kritična vrijednost
`r hr_broj(qt(.975, s14$df_welch), 3)`. Za test nulte razlike dijelimo
opaženu razliku njezinom standardnom pogreškom. Dobivenu t-statistiku
uspoređujemo s oba repa iste t-raspodjele. Taj račun pretpostavlja neovisne
skupine i jedinice te približno normalne sredine; za male skupine posebno
je važan oblik raspodjele bez dominantnih krajnjih vrijednosti.

U našem uzorku prosječno povjerenje iznosi
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "TV"], 2)` među onima koji
navode TV kao glavni izvor vijesti i
`r hr_broj(s14_sazetak$sredina[s14_sazetak$izvor == "društvene mreže"], 2)` među
onima koji navode društvene mreže. Razlika iznosi
`r hr_broj(s14$razlika, 2)` boda uz interval pouzdanosti od
`r hr_broj(s14$donja, 2)` do `r hr_broj(s14$gornja, 2)`.

Koristimo Welchov interval, koji zasebno procjenjuje varijancu svake skupine.
Pripadni obostrani test ispituje je li populacijska sredina TV skupine minus
sredina skupine društvenih mreža jednaka nuli. Ovdje uspoređujemo sredine. Ne
testiramo jednakost cijelih raspodjela.

Interval obuhvaća razlike ispod pola boda i blizu dva boda. Te vrijednosti
mogu voditi različitim praktičnim odlukama. Sama oznaka značajnosti ne bi
pokazala koliko je procjena još neprecizna.

U simulaciji znamo da stvarna razlika iznosi `r hr_broj(s14$pop_razlika, 2)` boda i da je interval
obuhvaća. Jedan pogodak nije provjera dugoročnog obuhvata. Za to su potrebna
ponavljanja kakva smo koristili u poglavlju o procjeni.

## Interakcija — Uzorkivač dviju grupa

Ovo je zaseban normalni model bez ljestvice povjerenja. U prikazanoj postavci
svaka skupina ima 50 ishoda, sredine su 0 i 5, a standardna devijacija 10.
U neovisnom nacrtu svaki ishod izvlačimo zasebno. U uparenom dva ishoda iste
osobe dijele dio slučajnog odstupanja, tako da je zadana korelacija 0,65.
Za jedan skup oduzimamo sredinu A od sredine B, odnosno računamo prosjek
promjena unutar parova.

Raspodjelu tih razlika ovdje stvaramo kraćim računom. Za zadani normalni
model poznajemo njezinu sredinu i standardnu pogrešku, pa razlike izvlačimo
izravno iz te raspodjele, bez stvaranja svih pojedinaca svakoga novog
uzorka. Digitalni prikaz koristi 1.500 takvih razlika, a tiskani 4.000 po
nacrtu. Nijedno ponavljanje nije izostavljeno. Njihov raspon pokazuje preciznost procjene, ne
snagu testa ni udio intervala koji obuhvaćaju istinu. Oblik histograma može
se malo promijeniti pri novom izvlačenju.

Na slici uspoređujemo raspršenost pojedinačnih rezultata i preciznost
procijenjene razlike. Uz ishode skupina prikazane su raspodjele razlika za
neovisna i uparena mjerenja. Veličina uzorka, stvarna razlika i raspršenost ishoda
jednake su, pa možemo vidjeti učinak uparivanja. Okomite crte označuju
zadane sredine ishoda u prva dva panela i stvarnu razliku u preostala dva.
Okomite ljestvice prilagođene su pojedinom panelu, pa uspoređujemo širinu
raspodjela na zajedničkoj vodoravnoj osi.

*Slika. Jedan simulirani uzorak dviju skupina i raspodjela procijenjene razlike kroz ponovljene uzorke.*

**Što isprobati.**

1. Povećajte stvarnu razliku uz jednaku raspršenost.
2. Povećajte raspršenost uz jednaku razliku i pogledajte oba panela.
3. Povećajte broj jedinica bez promjene razlike i raspršenosti.
4. Prebacite dizajn u upareni uz sve ostalo nepromijenjeno.

U ovom primjeru uparena mjerenja daju užu raspodjelu procijenjenih razlika.
Kada računamo promjenu unutar osobe, uklanjamo dio varijacije koji potječe od
trajnih razlika među osobama. Taj dobitak zadržavamo samo ako u analizi
sačuvamo parove.

## Ista razlika, dva dizajna

Pogledajmo to na `r s14$np` simuliranih osoba izmjerenih prije i poslije
događaja. Pomak, varijance i povezanost zadani su kako bismo uvježbali račun
za povezana mjerenja. Podaci ne opisuju stvarne ljude. Ni u stvarnom
istraživanju takva promjena sama, bez kontrolne skupine ili randomizacije, ne
bi dokazivala učinak događaja.

Vraćamo se računu iz pojedinačnih zapisa, ali stvaramo nove osobe. Svakoj
od 60 osoba najprije generiramo zajedničku osnovu iz normalne raspodjele sa
sredinom 5 i standardnom devijacijom 1,6. Početnom mjerenju dodajemo
neovisno odstupanje standardne devijacije 0,7. Završnom dodajemo zadani
pomak 0,45 i drugo takvo odstupanje. Prva tri para prikazuju ostvarene
vrijednosti i njihovo oduzimanje. Ishodi ovdje nisu zaokruženi ni ograničeni
na ljestvicu od 1 do 10.

*Slika. Tri od 60 zasebno simuliranih parova prije računanja prosječne promjene. Izrada autora.*

Za pregled uparenih podataka potrebna su dva pogleda. Na prvome svaka točka
povezuje dva mjerenja iste osobe, a dijagonala znači jednaka mjerenja.
Na drugome pregledavamo raspodjelu razlika, jer se na njih odnosi upareni
postupak. Ne možemo je zamijeniti zasebnim histogramima prije i poslije.

*Slika. Parovi i njihove razlike u zasebno konstruiranoj nastavnoj simulaciji. Izrada autora.*

Prva promjena iznosi `r hr_broj(s14_poslije[1], 2)` minus
`r hr_broj(s14_prije[1], 2)`, odnosno `r hr_broj(s14_razlike[1], 2)`.
Zbroj svih 60 promjena dijelimo sa 60, a njihovu standardnu devijaciju s
$\sqrt{60}$ za standardnu pogrešku sredine. Nijedan par ne isključujemo.

Uparena t-statistika zato je sredina promjena podijeljena sa
$s_{\mathrm{promjena}}/\sqrt{60}$. Referentna t-raspodjela ima 59 stupnjeva
slobode. P-vrijednost zbraja oba repa iza apsolutne opažene statistike.
Neovisnost se ovdje traži među osobama, dok se povezanost dvaju mjerenja
iste osobe čuva izračunavanjem njezine promjene.

Korelacija mjerenja iznosi `r hr_broj(s14$r_parova, 2)`. Osobe s višim početnim rezultatom
uglavnom imaju viši i završni rezultat. Velik dio raspršenosti zato odražava
razlike među osobama, dok nas zanima njihova promjena. Za svaku osobu najprije
oduzmemo početni rezultat od završnoga. Dobivene razlike čine jedan uzorak čiju
sredinu možemo usporediti s nulom, pa upareni račun prepoznajemo kao
jednouzoračni postupak primijenjen na promjene.

Prosječna promjena iznosi `r hr_broj(s14$m_razlika, 2)`, a standardna devijacija pojedinačnih
razlika `r hr_broj(s14$sd_razlika, 2)`. Uparena analiza daje interval od `r hr_broj(s14$up_donja, 2)` do `r hr_broj(s14$up_gornja, 2)`, uz
p-vrijednost `r formatC(s14$up_p, format = "f", digits = 4, decimal.mark = ",")`.

Ako iste podatke pogrešno obradimo kao neovisne skupine, dobivamo interval od
`r hr_broj(s14$nez_donja, 2)` do `r hr_broj(s14$nez_gornja, 2)` i p-vrijednost `r formatC(s14$nez_p, format = "f", digits = 3, decimal.mark = ",")`. Prosječna promjena ostaje
ista, ali procijenjena nesigurnost znatno se mijenja.

Neovisna analiza koristi raspršenost među osobama, koja je ovdje velika.
Uparena koristi raspršenost promjena unutar osoba, koja je manja. Budući da su
iste osobe izmjerene dvaput, upareni postupak odgovara nacrtu istraživanja. Ne
biramo ga prema tome daje li manju p-vrijednost.

Dobitak ovisi o varijanci razlika, a ona o raspršenosti obaju mjerenja i
njihovoj povezanosti. Uz slične varijance veća pozitivna povezanost obično
daje uži interval. Slaba povezanost daje manji dobitak, a pogrešno spojeni
parovi mogu ga ukloniti. Parove zato određujemo prema identitetu jedinica i
nacrtu.

## Razlika skupina u linearnom modelu

Razliku dviju neovisnih skupina dosad smo dobivali oduzimanjem njihovih
sredina. Istu procjenu možemo zapisati modelom koji svakoj osobi pridružuje
sredinu njezine skupine. Za to je dovoljna oznaka nula ili jedan, a koeficijent
uz nju postaje razlika sredina. Pritom čuvamo razliku među trima opisanim nacrtima i njihovim postupcima.

$$\text{povjerenje} = \beta_0 + \beta_1 \cdot \text{skupina} + \varepsilon$$

Oznaka $\beta_0$ predstavlja očekivani ishod u polaznoj skupini, a $\beta_1$
razliku druge skupine prema njoj. Oznaka $\varepsilon$ obuhvaća odstupanje
pojedine osobe od modela. Varijabla skupine ima vrijednost nula za polaznu i
jedan za drugu skupinu.

**Referentna skupina** je kategorija prema kojoj se izražavaju sve ostale
kategorije istog prediktora, pa njezina sredina postaje polazna vrijednost
modela, a koeficijenti ostalih kategorija odstupanja od nje.

Osobi iz referentne skupine model daje predviđanje $\beta_0$, jer se
koeficijent razlike množi nulom. Osobi iz druge daje $\beta_0 + \beta_1$.
Svi ljudi iste skupine dobivaju isti predviđeni prosjek, ali zadržavaju
vlastite opažene odgovore i različite reziduale, odnosno razlike između
opaženih i modelom predviđenih odgovora.

Kao referencu uzimamo društvene mreže. Zato $\beta_0$ iznosi `r hr_broj(s14$presjek, 2)` i
jednak je sredini te skupine. Koeficijent $\beta_1$ iznosi `r hr_broj(s14$nagib, 2)` i jednak
je prethodno izračunatoj razlici. Promjena reference mijenja odsječak i
predznak koeficijenta, ali ostavlja iste procijenjene sredine skupina.

Jednouzoračni postupak uspoređuje sredinu s vanjskom vrijednošću, a upareni
analizira sredinu razlika unutar parova. Svi postupci daju procjenu,
nesigurnost i usporedbu s nulom, ali njihove pretpostavke nisu iste.

Koeficijent sam po sebi ne daje uzročno značenje. Za to trebamo opravdanje iz
nacrta i načina nastanka skupina. U našem primjeru ljudi sami biraju izvor
vijesti, pa koeficijent opisuje razliku među njima.

## Što razlika sama ne kaže

Model nam je dao drugi zapis iste razlike, ali još trebamo procijeniti njezin
razmjer. Tu se vraćamo raspršenosti unutar skupina. Jedan bod predstavlja veće
razdvajanje kada su odgovori zbijeni nego kada su široko raspršeni.

Standardiziranu razliku računamo dijeljenjem razlike sredina združenom
standardnom devijacijom. Tako rezultat izražavamo u standardnim devijacijama,
kako smo učinili u poglavlju o veličini učinka.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Združena varijanca ponderirani je prosjek dviju varijanci, s težinama
$n_1-1$ i $n_2-1$; nakon korjenovanja dobivamo združenu standardnu devijaciju.
Za `r s14$n_mreze` korisnika mreža i `r s14$n_tv` korisnika televizije
račun iz nezaokruženih podataka daje `r hr_broj(s14_zdruzena, 4)`.
Razlika sredina iznosi `r hr_broj(s14$razlika, 4)`, pa njihov omjer daje
$d\approx$ `r hr_broj(s14$d, 4)`, odnosno `r hr_broj(s14$d, 2)`.
Račun iz ranije tablice može se malo razlikovati jer su njezine standardne
devijacije zaokružene.

Sadržajnu važnost procjenjujemo prema usporedivim nalazima i posljedicama
razlike u izvornim jedinicama. U uparenom primjeru dijelimo standardnom devijacijom razlika i
dobivamo `r hr_broj(s14$up_d, 2)`. Budući da nazivnici nisu isti, te dvije standardizirane
mjere nisu izravno usporedive.

Standardizacija ne uklanja druge razlike među skupinama. U našoj populaciji
korisnici društvenih mreža imaju prosječno `r hr_broj(s14$pop_dob_mreze)` godine, a korisnici
televizije `r hr_broj(s14$pop_dob_tv)` godine. Povjerenje pritom raste s dobi.
Dob je moguća konfundirajuća varijabla, u smislu objašnjenom u poglavlju
o mjerenju i dizajnu.

Provjerimo zato osjetljivost usporedbe na dobni raspon. U cijeloj simuliranoj
populaciji razlika iznosi `r hr_broj(s14$pop_razlika, 2)` boda. Među osobama od trideset do
četrdeset devet godina, gdje su dobne razlike skupina manje, iznosi `r hr_broj(s14$pop_razlika_uska, 2)`
boda. Time smo promijenili ciljnu populaciju. Nismo izmjerili udio razlike
koji je uzrokovan dobi niti odvojili uzročne učinke dobi i izvora vijesti.

U našem uzorku tom dobnom rasponu pripada `r s14$uzak_n` od `r s14$n` osoba.
Razlika sredina iznosi `r hr_broj(diff(s14_uzak_test$estimate), 2)` boda.
Interval ide od `r hr_broj(s14$uzak_donja, 2)` do `r hr_broj(s14$uzak_gornja, 2)` i obuhvaća nulu. Ciljana razlika je
manja, a zbog manjeg broja osoba procjena je manje precizna. Za planiranje
uzorka potrebnog za takvu razliku koristimo znanje o snazi i preciznosti.

Zaključak vrijedi za ovdje korištene mjere i populaciju koju nacrt može
dosegnuti. Za odluku trebamo i sadržajni kriterij. Interval od nepunih pola do gotovo dva boda može biti dovoljno informativan kada nas zanima bilo koja pozitivna
razlika, a nedovoljan kada tražimo najmanje dva boda. Taj kriterij moramo
obrazložiti prije čitanja rezultata.

## Pretpostavke i njihove granice

Za neovisnu usporedbu provjeravamo da jedinice nisu povezane i da svaka osoba
pripada samo jednoj skupini. Ishod treba biti ispravno kodiran, referentna
skupina jasno određena, a uzorkovanje primjereno ciljnoj populaciji. Izbor
testa ne može nadoknaditi probleme tih dijelova istraživanja.

U malim uzorcima t-aproksimacija ovisi o približnoj normalnosti ishoda unutar
skupina. U velikima su važne konačne varijance i odsutnost opažanja koje samo
određuje rezultat. Kod uparenog postupka pregledavamo raspodjelu razlika
unutar parova.

Welchov postupak zasebno koristi varijancu i veličinu svake skupine te ne
zahtijeva jednake varijance. Uobičajena inferencija običnog linearnog modela
koristi zajedničku rezidualnu varijancu i pretpostavlja jednake uvjetne
rezidualne varijance.

Budući da veličine i varijance naših skupina nisu jednake, koristimo Welchov
postupak. Obični linearni model daje istu procjenu razlike, ali nesigurnost
računa drukčije. U razrađenom primjeru usporedit ćemo standardne pogreške,
stupnjeve slobode i intervale te jasno navesti pretpostavku zajedničke
rezidualne varijance.

Raspodjelu najprije pregledavamo grafički. Test normalnosti ne treba sam
određivati izbor analize. U velikom uzorku može otkriti nevažno odstupanje, a
u malom propustiti ozbiljno. To vrijedi i za Shapiro-Wilkov test.

Krajnje vrijednosti pregledavamo pojedinačno. Mogu biti pogrešno unesene,
rijetke ali stvarne ili znak da sredina loše opisuje ishod. Opravdanu provjeru
s njima i bez njih treba prikazati s oba rezultata. Opažanja ne uklanjamo tiho
prema tome kako mijenjaju p-vrijednost.

Možemo se pitati nose li zaključak velike brojčane udaljenosti ili
dosljednost smjera promjene. Za tu provjeru koristimo Wilcoxonov postupak
predznačenih rangova. Uzimamo iste promjene 60 osoba,
poredamo njihove apsolutne iznose i vratimo svakom rangu predznak promjene.
Prva osoba dobiva rang `r rank(abs(s14_razlike))[1]` i
`r ifelse(s14_razlike[1] > 0, "pozitivan", "negativan")` predznak.
Zatim uspoređujemo zbrojeve rangova pozitivnih i negativnih promjena.
U ovom skupu nema nultih razlika ni vezanih rangova. Za tumačenje kao
provjere središta promjena potrebno je i opravdanje simetričnosti njihove
raspodjele.

Uz pretpostavku simetrične raspodjele postupak provjerava je li središte
promjena jednako nuli. To nije isto pitanje kao provjera prosječne promjene.
U našem primjeru daje p-vrijednost `r formatC(s14$wilcoxon_p, format = "f", digits = 4, decimal.mark = ",")`. Zaključci su slični, ali odnose
se na različite veličine.

**Statistika u divljini.**
**Preklapanje crtica.** Na grafu su dvije sredine i oko svake
crtice pogreške. Čitatelj želi znati razlikuju li se skupine, pa
pogleda dodiruju li se crtice. Takav brz postupak može djelovati
uvjerljivo dok ne saznamo što crtice prikazuju i kako su mjerenja
nastala. Ista slika ne mora predstavljati istu usporedbu.

Belia i suradnici taj su problem proučili s autorima znanstvenih
radova. Internetski zadatak dovršila su 473 autora iz psihologije,
bihevioralne neuroznanosti i medicine. Trebali su pomaknuti
prikazane sredine do razlike koju smatraju upravo statistički
značajnom (Belia, 2005). Mnogi nisu dovoljno razlikovali standardne
pogreške od intervala pouzdanosti ni neovisne skupine od
ponovljenih mjerenja (Belia, 2005).

Posljedicu možemo razmotriti na zamišljenoj procjeni radionice.
Ako graf prikazuje rezultate istih polaznika prije i poslije
radionice, zanima nas promjena svake osobe. Interval za tu
promjenu ovisi i o povezanosti njezinih dvaju mjerenja.
Odvojene crtice oko sredine prije i sredine poslije tu
informaciju ne prenose. Zaključak da radionica nije povezana s promjenom, izveden samo iz
preklapanja crtica, zato preskače potrebnu uparenu analizu.

Kod dviju neovisnih skupina trebamo drukčiji račun
nesigurnosti razlike. I tu opis crtica prethodi zaključku.
Standardna devijacija opisuje raspršenost opažanja, standardna
pogreška nesigurnost procjene sredine, a interval pouzdanosti
određen je postupkom s odabranom razinom pouzdanosti. Nijednu
od tih oznaka ne smijemo prešutno zamijeniti drugom.

Autor izvještaja može pomoći čitatelju tako da uz graf navede
nacrt i značenje crtica te izravno prikaže procjenu razlike
s njezinim intervalom. Ako je radionica procijenjena samo
prije i poslije, ni dobro izračunata promjena sama ne
isključuje druga objašnjenja. Prije zaključka o dvjema sredinama zato procjenjujemo nesigurnost njihove
razlike. Preklapanje dvaju zasebnih raspona nije dovoljno.

**Nađite grešku.**
Za izvještaj o televiziji i društvenim mrežama pregledajte usporedbu
među osobama od 30 do 49 godina iz našeg simuliranog uzorka. Ishod je
povjerenje u medije na ljestvici od jedan do deset, a razlika se računa
kao televizija minus društvene mreže. Svaka osoba pripada jednoj skupini.

| Rezultat u dobnoj podskupini | Vrijednost |
|---|---:|
| Ukupan broj osoba | `r s14$uzak_n` |
| Procijenjena razlika sredina | 0,77 boda |
| Welchov 95-postotni interval razlike | od −0,34 do 1,88 boda |

: Usporedba dviju skupina u simuliranom uzorku. Izrada autora prema sikic2026.

Asistentov osvrt na postupak i rezultat glasi ovako.

> Jedinica neovisnosti je osoba. Referentna skupina su društvene mreže,
> pa pozitivan koeficijent uz TV znači višu sredinu u TV skupini.
> Raspodjele i neobična opažanja pregledani su, a Welchov test ne traži
> jednake varijance. Interval razlike obuhvaća nulu, pa u toj dobnoj
> skupini glavni izvor vijesti nema veze s povjerenjem.

Uz nulu navedite još dvije različite vrijednosti razlike koje pripadaju
prikazanom intervalu. Upotrijebite ih u obrazloženju je li posljednja
rečenica prihvatljiva. Zatim napišite zamjenu koja zadržava smjer
usporedbe, procjenu i granice intervala, bez odbacivanja valjanih
provjera postupka.

## Razrađeni primjer

Za usporedbu televizije i društvenih mreža zadržavamo iste osobe, isto
povjerenje i istu ciljanu razliku. Najprije ćemo je procijeniti Welchovim
postupkom, a zatim zapisati kao koeficijent uz binarnu oznaku skupine. Budući
da se točkasta procjena time ne mijenja, možemo se usredotočiti na pretpostavke
i račun njezine nesigurnosti.

U tablici uspoređujemo procjenu i njezin interval prije čitanja
programskog računa. Sve su vrijednosti u bodovima povjerenja, a stupci
Donja i Gornja granice su 95-postotnog intervala. Razlika je u oba retka
televizija minus društvene mreže.
Za glavni zaključak zadržavamo Welchov postupak, dok drugi redak pokazuje
što se mijenja kada model pretpostavi zajedničku rezidualnu varijancu.

*Slika. Ista procjena razlike i dva računa nesigurnosti u simuliranom uzorku. Izrada autora.*

U izvještaju možemo navesti da u uzorku od 120 simuliranih osoba
korisnici televizije imaju prosječno `r hr_broj(s14$razlika, 2)` boda više
povjerenja od korisnika društvenih mreža, uz Welchov 95-postotni interval
od `r hr_broj(s14$donja, 2)` do `r hr_broj(s14$gornja, 2)` boda
(Šikić, 2026). To je razlika među skupinama koje same biraju izvor vijesti.
Nije procjena promjene povjerenja koju bi izazvalo prebacivanje iste osobe
na televiziju. Cijeli interval ostaje ispod dva boda, pa podaci ne podupiru
odluku koja zahtijeva najmanje toliku razliku.

Welchov postupak daje razliku `r hr_broj(s14$razlika, 3)` boda, standardnu pogrešku `r hr_broj(s14$se_welch, 3)` i
`r hr_broj(s14$df_welch, 3)` stupnja slobode. Koeficijent uz TV jednak je toj razlici jer su
društvene mreže referenca. Obična standardna pogreška modela iznosi `r hr_broj(s14$se_ols, 3)`,
uz `r s14$df_ols` stupnjeva slobode. Njegov interval ide od `r hr_broj(s14$ols_donja, 3)` do `r hr_broj(s14$ols_gornja, 3)`,
dok Welchov ide od `r hr_broj(s14$donja, 3)` do `r hr_broj(s14$gornja, 3)`. Procjene su jednake, ali njihova
nesigurnost nije. Ovdje su intervali bliski jer su skupne standardne
devijacije slične. Uz izrazito različite varijance i brojnosti razlika
u standardnim pogreškama može biti mnogo veća. I pri proširenju na više skupina moramo zasebno odabrati
način računanja nesigurnosti.

Uz brojke navodimo da ljudi sami biraju izvor vijesti i da se skupine
razlikuju po dobi. Time čitatelju objašnjavamo zašto rezultat opisuje razliku
među skupinama i ne utvrđuje učinak medija.

Za provjeru računa slijedi isti postupak u R-u. Prvi prolaz kroz primjer
može završiti prethodnim tumačenjem. Ovdje provjeravamo kako program dobiva
procjenu i zašto se njegova dva intervala razlikuju.

Oba računa uspoređuju isto povjerenje u istim skupinama. Poziv `t.test` prima
njihove vrijednosti odvojeno i u zadanoj postavci provodi Welchov postupak. U
pozivu `lm` zapis `povjerenje_medijima ~ izvor` povezuje brojčani ishod s
oznakom skupine. Uobičajeni ispis toga modela računa nesigurnost uz pretpostavku
jednake rezidualne varijance u skupinama, odnosno homoskedastičnosti. Pozivom
`df.residual` izdvajamo i rezidualne stupnjeve slobode kako bismo mogli
usporediti način računanja intervala. Kod je izvadak iz analize poglavlja i pretpostavlja već pripremljen objekt `dvije_skupine`. Vrijednost `welch$stderr` daje Welchovu standardnu pogrešku.

## Sažetak

Ista brojčana razlika može potjecati iz različitih nacrta, pa usporedbu
počinjemo jedinicom neovisnosti i odnosom među mjerenjima. Tako razlikujemo
jednouzoračni, neovisni i upareni postupak te vidimo zašto zanemarivanje parova
može znatno promijeniti procijenjenu nesigurnost. Razliku neovisnih sredina
možemo zapisati i koeficijentom uz binarnu oznaku skupine, ali jednak
koeficijent ne jamči jednak interval u Welchovu i običnom postupku najmanjih kvadrata (OLS).
Standardizirana razlika pomaže usporediti razmjer, dok druga obilježja po
kojima se skupine razlikuju i dalje ograničavaju tumačenje. U sljedećem
poglavlju isti model proširujemo na više skupina, pa ćemo uz pojedinu razliku
morati razmotriti i cijeli skup usporedbi.

Prediktor je varijabla kojom model opisuje razlike u ishodu. Homoskedastičnost
označuje jednaku rezidualnu varijancu, pretpostavku obične modelne standardne
pogreške o kojoj smo govorili uz usporedbu s Welchovim postupkom.

## Pojmovi

homoskedastičnost (*homoskedasticity*), Wilcoxonov postupak predznačenih rangova (*Wilcoxon signed-rank test*), prediktor (*predictor*),
jedinica neovisnosti (*unit of independence*), neovisne skupine (*independent
groups*), upareni podaci (*paired data*), razlika sredina
(*difference in means*), Welchov postupak (*Welch's t-test*), t-raspodjela (*t distribution*), kritična t-vrijednost (*critical t value*), stupnjevi slobode (*degrees of freedom*), referentna
skupina (*reference category*), standardizirana razlika (*Cohen's d*), ovisnost
opažanja (*dependence among observations*)

## Zadaci

Nakon vlastitog pokušaja otvorite naznake i provjere rješenja.

### Konceptualni

Za tri istraživačke situacije imenujte jedinicu neovisnosti i odgovarajući
dizajn. Prva uspoređuje prosječno povjerenje u uzorku s unaprijed zadanim pragom
od pet bodova, druga uspoređuje dvije skupine prema glavnom izvoru vijesti, a
treća mjeri iste ispitanike prije i poslije kampanje.

### Računski

Iz upravljanoga agregata `data/populacija-medija-agregat.csv` uzmite retke za TV
i društvene mreže. Za svaki redak podijelite `zbroj_povjerenja` stupcem `broj`,
provjerite pohranjeni prosjek i izračunajte razliku aritmetičkih sredina. Zatim
pretpostavite jednake standardne devijacije 1,6 pa 3,2 i za obje izračunajte
standardiziranu razliku. Objasnite zašto se prva brojka nije promijenila, a druga
jest. Za rad bez datoteke upotrijebite izvadak iz istoga agregata.

*Slika. Izvadak upravljanoga agregata za obvezni zadatak.*

### Kritički

Vratite se operacionalizaciji iz poglavlja o mjerenju i istraživačkom dizajnu
i tumačenju intervala iz poglavlja o procjeni. Za glavni primjer najprije napišite što ljestvica povjerenja i kategorija
izvora vijesti ne mjere. Zatim za isti interval usporedite odluku kojoj je važna
bilo koja pozitivna razlika s odlukom koja traži najmanje dva boda. Predajte
kratku bilješku recenzentu i objasnite zašto sama oznaka značajnosti ne može
riješiti ni problem mjerenja ni izbor praga (Cumming, 2014).

### Revizija modela

Ocijenite usporedbu dviju skupina iz okvira. Imenujte referentnu skupinu i objasnite što
bi se promijenilo, a što ostalo isto kada bi se referenca zamijenila. Zatim
provjerite jedinicu neovisnosti, vrstu ishoda, odnos prema varijancama i doseg
ciljne populacije. Izdvojite jedinu tvrdnju koja iz rezultata ne slijedi i
napišite rečenicu kojom bi je trebalo zamijeniti.

---

# Uspoređivanje više grupa

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/15-vise-grupa.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Simmons, Nelson i Simonsohn pokazali su kako niz uobičajenih istraživačkih
odluka može dovesti do značajnog rezultata za nemoguću tvrdnju (Simmons, 2011).
Istraživač može birati koji će ishod prikazati, koju podskupinu analizirati i
kada će zaustaviti prikupljanje podataka. Svaki izbor otvara novu mogućnost za
poželjan rezultat.

Pojedinačni testovi pritom mogu biti ispravno izračunati. Problem nastaje kada
izvještaj prikaže samo odabrani nalaz, a prešuti koliko je usporedbi i odluka
do njega dovelo.

Kako usporediti više skupina, uzeti u obzir broj usporedbi i utvrditi gdje su
razlike?

Usporedba televizije i društvenih mreža ostavila je izvan analize korisnike
ostalih izvora vijesti. Ako želimo obuhvatiti sve skupine, mogli bismo
ponavljati postupak iz prethodnog poglavlja za svaki par. No tada više ne
donosimo samo jednu odluku. Moramo razmotriti koliko prilika za lažni nalaz
nastaje kroz sve usporedbe koje ćemo pregledati. Tu ćemo poteškoću najprije
ispitati u simulaciji u kojoj skupine dolaze iz iste raspodjele povjerenja.
Svaku pronađenu razliku tada možemo prepoznati kao lažni nalaz. Povezat ćemo
tu provjeru s onime što smo u poglavlju o krizi i obnovi naučili o odabiru
rezultata. Ovdje je skup usporedbi unaprijed poznat, pa možemo tražiti
postupak koji uvažava cijeli skup odluka.

Za glavnu analizu uzimamo 300 zamišljenih osoba iz `populacija_medija` i
zadržavamo izvor vijesti zadan pri stvaranju podataka (Šikić, 2026). Jedan
redak sadrži osobu, njezin izvor i ocjenu povjerenja. Skupine televizije,
radija, tiska, portala i društvenih mreža zato se sada mogu razlikovati. Ti
rezultati opisuju nastavni skup i služe učenju usporedbe, bez tvrdnje o
stvarnoj publici.

Umjesto jedne razlike sredina sada ispitujemo jesu li sve skupinske sredine
jednake. Razlaganjem varijabilnosti usporedit ćemo razmake među sredinama s
raspršenošću osoba unutar skupina. Iz te ćemo usporedbe razviti analizu
varijance i F-test, uz mjeru veličine učinka. Ukupni nalaz još neće odrediti
koji se parovi razlikuju. Za njih ćemo prikazati procjene i intervale koji
uzimaju u obzir višestruke usporedbe, pa razmotriti i granice pretpostavki.  Tako možemo sastaviti odgovor koji razlikuje ukupni obrazac,
konkretne razlike i nesigurnost svake opravdane usporedbe.

## Cijena mnogih usporedbi

Među pet skupina postoji deset parova. Mogli bismo svaki usporediti zasebnim
testom iz prethodnog poglavlja. Simulacijom ćemo provjeriti koliko često taj
niz testova daje barem jedan lažni nalaz.

Iz poznate simulirane populacije medijskih navika nasumično sastavljamo pet
skupina po četrdeset osoba. Pri tome zanemarujemo njihov izvor vijesti. Sve
skupine nastaju odabirom iz iste raspodjele povjerenja, pa među njima nema
unaprijed zadane razlike. U svakom ponavljanju provodimo deset usporedbi i
bilježimo je li barem jedna značajna. Svako takvo odbacivanje ovdje je
pogrešno. Poslije ćemo se vratiti skupinama prema izvoru vijesti, među kojima
razlike mogu postojati.

Jedno ponavljanje stvara pet skupina po 40 odgovora. Unutar svake skupine
biramo bez vraćanja, ali svaku novu skupinu ponovno izvlačimo iz pune
populacije. Ista osoba zato može biti odabrana u različitim skupinama.
U prvom stvarno izvedenom ponavljanju sredine su
`r paste(hr_broj(vapply(s15_prvo_skupine, mean, numeric(1)), 2), collapse = ", ")`.
Među deset obostranih Welchovih usporedbi najmanja p-vrijednost iznosi
`r hr_broj(min(s15_prvo_p), 3)`, a prag 0,05 prelazi u smjeru odbacivanja
`r sum(s15_prvo_p < 0.05)` usporedbi. Za zbirni rezultat zapisujemo samo
ima li barem jedne takve usporedbe. Dva lažna nalaza u istom ponavljanju
i dalje znače jedno ponavljanje s pogreškom.

Ponovno izvlačimo svih pet skupina 2.000 puta, zadržavajući istu populaciju,
veličine i pravila testiranja. Barem jedan lažni nalaz dobivamo u
`r sum(s15_pod_nultom["barem_jedan", ])` od 2.000 ponavljanja. Svi su
testovi definirani i nijedno ponavljanje nije izostavljeno.

U dvije tisuće ponavljanja barem jedna usporedba bila je značajna u `r hr_broj(s15$stopa_parne)`
% slučajeva. Svaki test koristi prag pet posto, ali cijeli skup daje lažni
nalaz u više od četvrtine ponavljanja. Prikaz samo značajnog para sakrio bi tu
veću stopu pogreške.

**Stopa obiteljske pogreške** je vjerojatnost da će barem jedan test u
unaprijed određenom skupu testova dati lažno pozitivan rezultat, odnosno
pogrešno odbaciti barem jednu istinitu nultu hipotezu.

U našoj su simulaciji sve nulte hipoteze istinite. Kada neke
razlike postoje, pratimo vjerojatnost da pogrešno odbacimo barem jednu od
preostalih istinitih nultih hipoteza.

Postupak koji kontrolira pogrešku samo kada su sve nulte hipoteze istinite
ima slabu kontrolu. Jaka kontrola mora vrijediti i kada dio razlika doista
postoji. Tukeyjev postupak u odgovarajućem normalnom modelu sa zajedničkom
varijancom štiti obitelj parnih usporedbi i u tom drugom slučaju. Primjerice,
ako se samo prva od pet skupina razlikuje od ostalih, ukupni test može lako
odbaciti jednakost svih sredina. Među preostalim četirima ipak postoji šest
usporedbi jednakih populacijskih sredina. Njihovo zasebno testiranje bez
korekcije i dalje otvara mogućnost barem jednoga lažno pozitivnog zaključka.

Za deset neovisnih testova vjerojatnost da nijedan ne pogriješi iznosi
$0,95^{10}$. Suprotni događaj, barem jedna pogreška, zato ima vjerojatnost
$1-0,95^{10}$, približno 0,401.

Za deset neovisnih testova račun daje stopu `r hr_broj(s15$formula_neovisnih)` %. U parnim usporedbama pet skupina ista se opažanja koriste više puta, pa
usporedbe nisu neovisne i u našoj simulaciji daju nižu stopu. Zasebna simulacija deset doista neovisnih usporedbi daje `r hr_broj(s15$stopa_neovisne)`
%, blizu računu.

U zasebnom pokusu svaki od deset testova dobiva svoja dva nova uzorka po
40 osoba, pa testovi više ne dijele iste uzorke. Od 2.000 ponavljanja
`r sum(s15_neovisnih_deset)` sadrži barem jedno odbacivanje, bez isključenih
ponavljanja. Uspoređujemo dvije organizacije testiranja pod nulom, a ne
njihovu snagu. Novi niz izvlačenja dao bi malo drukčije udjele.

Formula za neovisne testove nije opća gornja granica za ovisne usporedbe.
Ipak, oba simulirana skupa daleko prelaze pet posto. Zato uz najmanju
p-vrijednost trebamo znati koliko je usporedbi provedeno i kako su povezane.

Za stopu blizu 5 % uz 2.000 ponavljanja standardna pogreška samoga
simulacijskog postotka iznosi oko 0,49 postotnih bodova. Mala odstupanja od
5 % zato nisu sama po sebi dokaz pogrešno podešena postupka.

Možemo postaviti i jedno ukupno pitanje o jednakosti svih pet sredina. U istoj
simulaciji takav test odbacuje u `r hr_broj(s15$stopa_ukupni)` % slučajeva. Uz dvije tisuće
ponavljanja taj je udio u skladu s planiranih pet posto.

## Varijanca između i unutar

Ukupni test treba prepoznati jesu li razmaci među skupnim sredinama veliki u
odnosu na raspršenost koju već imamo među ljudima. Taj smo odnos susreli pri
usporedbi dviju skupina. Razlika od jednoga boda jače ih statistički razdvaja
kada su osobe unutar skupina slične nego kada su jako raspršene. Sada istu
logiku primjenjujemo na sve skupine zajedno.

Ukupnu varijabilnost zato razdvajamo na odstupanja među skupnim sredinama i
odstupanja pojedinaca unutar skupina. Model sa skupinama opisuje prvi dio, dok
drugi ostaje neobjašnjen.

Da bismo razlaganje vidjeli na manjem prikazu, prelazimo na tri skupine po
24 točke bez stvarne mjerne jedinice. Počinjemo normalnim slučajnim
vrijednostima, ali ih zatim u svakoj skupini centriramo i skaliramo tako da
njihova ostvarena sredina i standardna devijacija budu točno zadane.
To je ilustracija razlaganja, ne ponovljeno uzorkovanje za provjeru testa.
Pri sredinama 46, 52 i 58 zajednička je sredina 52. Skupina A pridonosi
zbroju između skupina s $24(46-52)^2 = 864$. Isti račun radimo za B i C,
dok unutar skupina zbrajamo kvadrate udaljenosti svake od 72 točke od
njezine skupne sredine.

Zbroj između skupina iznosi $864+0+864=1\,728$. Dijeljenjem s
$3-1=2$ dobivamo srednji kvadrat 864. Uz standardnu devijaciju 6,
zbroj unutar skupina iznosi $3\times23\times6^2=2\,484$; nakon dijeljenja
sa $72-3=69$ srednji kvadrat iznosi 36. Omjer je zato $F=864/36=24$.
Srednji kvadrat u nazivniku ima istu mjernu jedinicu kao onaj u brojniku,
pa je F bez mjerne jedinice.

Kad su sve tri sredine 52, zbroj između skupina iznosi nula, zbroj unutar
ostaje $2\,484$ i F je nula. U trećem stanju zbroj između ostaje $1\,728$,
a uz standardnu devijaciju 11 zbroj unutar iznosi
$3\times23\times11^2=8\,349$. Srednji kvadrat unutar skupina tada je 121,
pa je $F=864/121\approx7,14$.

Okomite trake prikazuju udaljenost skupnih sredina od zajedničke sredine.
Točke prikazuju raspršenost osoba oko sredine njihove skupine. Usporedba
stanja pokazuje kako isti razmak sredina izgleda uz različitu raspršenost
unutar skupina.

*Slika. Dekompozicija varijance — skupne sredine, zajednička sredina i raspršenost pojedinačnih opažanja.*

**Što isprobati.**

1. Postavite sve tri sredine na 52 i zadržite standardnu devijaciju 6.
2. Razmaknite sredine na 46, 52 i 58 te usporedite novi omjer s prvim.
3. Zadržite razdvojene sredine i povećajte standardnu devijaciju na 12.

U trećem stanju sredine su iste kao u drugome, ali je raspršenost unutar skupina veća, pa
omjer pada. Uz standardnu devijaciju 11 njegova je vrijednost
$864/121\approx7,14$, umjesto $864/36=24$ uz standardnu devijaciju šest.
Za procjenu odstupanja od nultog modela trebamo oba izvora
varijacije.

## Veličina i F-omjer

Zbroj kvadriranih odstupanja označujemo s $SS$. Dio $SS_{\text{između}}$
sažima odstupanja skupnih sredina od zajedničke, a $SS_{\text{unutar}}$
odstupanja pojedinaca od njihove skupne sredine. Ukupni zbroj
$SS_{\text{ukupno}}$ jednak je zbroju tih dijelova. Udio prvog dijela u
ukupnom pokazuje koliko je varijabilnosti povezano sa skupinama.

**Eta-kvadrat** je udio ukupne varijabilnosti ishoda koji otpada na razlike među
skupnim sredinama.

$$\eta^2 = \frac{SS_{\text{između}}}{SS_{\text{ukupno}}}$$

Sada prelazimo s početne simulacije nasumično sastavljenih skupina na uzorak
iz poznate simulirane populacije medijskih navika. Zadržavamo oznake pet
izvora vijesti zadane pri stvaranju podataka i uspoređujemo povjerenje
njihovih korisnika (Šikić, 2026). Skupine zato mogu imati različite prosjeke
i prije uzorkovanja.

Uzorak od 300 osoba izvukli smo bez vraćanja iz pune populacije, zasebno
od uzorka prethodnog poglavlja. tablica pokazuje broj odgovora i sredinu
koju model pridružuje svakoj osobi iste skupine.

*Slika. Pet skupina u glavnom uzorku od 300 osoba. Izrada autora.*

Prva uzorkovana osoba navodi `r as.character(pet_izvora$izvor_vijesti[1])`
i povjerenje `r pet_izvora$povjerenje_medijima[1]`. Njezina skupna sredina
je `r hr_broj(fitted(s15_model)[1], 3)`, pa u zbroj unutar skupina ulazi
$(`r pet_izvora$povjerenje_medijima[1]` - `r hr_broj(fitted(s15_model)[1], 3)`)^2$.
Za zbroj između skupina kvadriramo razliku svake skupne i zajedničke sredine
te je množimo brojem osoba u toj skupini. Tako dobivamo
`r hr_broj(s15$ss_izmedu, 2)` između i `r hr_broj(s15$ss_unutar, 2)` unutar.
Njihov zbroj, `r hr_broj(s15$ss_izmedu + s15$ss_unutar, 2)`, nazivnik je
eta-kvadrata. Svih 300 odgovora ulazi u oba opisa.

U našem uzorku eta-kvadrat iznosi `r hr_broj(s15$eta2, 3)`. Razlike među izvorima vijesti
opisuju oko `r hr_broj(s15$eta2 * 100, 0)` % varijabilnosti povjerenja. Većina razlika među ljudima
ostaje izvan modela. Za tu mjeru ovdje ne prikazujemo interval, pa njezina uzoračka nesigurnost nije kvantificirana.

Je li takav udio važan, ovisi o pitanju. Može biti koristan za razumijevanje
društvenog stava, a nedovoljan za precizno predviđanje pojedinca. Procjenu
zato povezujemo s ranijim nalazima i unaprijed obrazloženim najmanjim važnim
učinkom.

Eta-kvadrat opisao je koliki dio ukupne varijabilnosti otpada na razlike među
skupinama. Za test jednakosti sredina trebamo još usporediti raspršenost između
skupina s onom koja ostaje unutar njih. Sirove zbrojeve zato najprije
pretvaramo u usporedive srednje kvadrate. Za $k$ skupina i
$n$ opažanja dijelimo $SS_{\text{između}}$ s $k - 1$, a
$SS_{\text{unutar}}$ s $n - k$. Ti djelitelji predstavljaju stupnjeve
slobode. Dobivamo $MS_{\text{između}}$ i $MS_{\text{unutar}}$, gdje $MS$
označuje prosječnu kvadriranu raspršenost.

**F-statistika** je omjer prosječne raspršenosti među skupnim sredinama i
prosječne raspršenosti opažanja oko njihovih skupnih sredina.

$$F = \frac{MS_{\text{između}}}{MS_{\text{unutar}}}$$

Pod nultim modelom jednakih populacijskih sredina i zajedničke
varijance, uz neovisna opažanja, oba srednja kvadrata procjenjuju tu varijancu, pa se njihov omjer F obično nalazi blizu jedinice. Stupnjevi
slobode $k - 1$ i $n - k$ određuju referentnu F-raspodjelu. Veći omjer daje
više razloga za preispitivanje jednakosti sredina.

Referentna F-raspodjela opisuje koje bismo omjere dobivali pod tim nultim
modelom uz normalne pogreške. Njezina dva parametra ovdje iznose
`r s15$df1` i `r s15$df2`. Gornjih 5 % raspodjele počinje kod
`r hr_broj(qf(0.95, s15$df1, s15$df2), 2)`, dok naš opaženi omjer iznosi
`r hr_broj(s15$f, 2)`. Tu usporedbu koristimo za test; veličinu i važnost
razlika i dalje čitamo iz sredina, eta-kvadrata i intervala.

Postupak se zove analiza varijance jer uspoređuje izvore varijabilnosti. Njime
ipak ispitujemo pitanje o jednakosti skupnih sredina.

## Isti model, više koeficijenata

U prethodnom poglavlju binarna oznaka skupine imala je jedan koeficijent
razlike. Za pet skupina trebamo četiri takva koeficijenta. Jedna skupina
ostaje referentna, a ostale uspoređujemo s njom. U našem je računu to portal.

Pokazatelji $x_1$ do $x_4$ označuju četiri nereferentne skupine. Svaki ima
vrijednost jedan za svoju skupinu i nula za ostale. Koeficijent $\beta_0$ daje
sredinu reference, a koeficijenti $\beta_1$ do $\beta_4$ razlike prema njoj.
Populacijska pogreška $\varepsilon$ opisuje odstupanje od modelne
skupne sredine. Nakon prilagodbe opaženo odstupanje zovemo rezidualom.

$$\text{povjerenje} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 +
\beta_4 x_4 + \varepsilon$$

Svaka osoba pripada samo jednoj skupini. Pet koeficijenata tako opisuje pet
skupnih sredina.

Klasični ukupni test zajednički ispituje četiri koeficijenta razlike.
Uspoređuje model sa skupnim sredinama i model sa samo jednom zajedničkom
sredinom. To je jedno globalno pitanje, različito od deset zasebnih parnih
usporedbi.

Klasični i Welchov postupak koriste iste točkaste procjene sredina, ali
drukčije računaju nesigurnost. Klasična analiza varijance, kao obični
homoskedastični linearni model, procjenjuje zajedničku rezidualnu varijancu.
Welch zadržava zasebne skupne varijance i prilagođava stupnjeve slobode. Zato
intervali i p-vrijednosti ne moraju biti jednaki.

Taj model sada primjenjujemo na pojedinačne zapise iz skupa `populacija_medija`.
Svakoj osobi pridružujemo sredinu njezina izvora vijesti, pa odstupanja oko tih
pet sredina uspoređujemo s odstupanjima oko jedne zajedničke sredine.

Uzorak od `r s15$n` osoba dijelimo prema pet izvora vijesti. Ukupni test daje
F od `r hr_broj(s15$f, 2)`, uz `r s15$df1` i `r s15$df2` stupnjeva slobode te p-vrijednost
manju od 0,001. Srednji kvadrat između skupina iznosi `r hr_broj(s15$ms_izmedu, 1)`, a unutar njih
`r hr_broj(s15$ms_unutar, 1)`. Opaženi rezultat teško se uklapa u pretpostavku jednakih populacijskih
sredina. Još trebamo procijeniti pojedine razlike i njihovu nesigurnost.

Ljudi sami biraju izvor vijesti, pa se skupine mogu razlikovati i po drugim
obilježjima. Model opisuje njihove razlike u povjerenju, ali ne utvrđuje
učinak izbora izvora.

Oblik razlika provjeravamo na samim odgovorima. Kutije prikazuju srednjih
50 % vrijednosti, vodoravna crta medijan, a točke pojedinačne odgovore.
Raspršenost i preklapanje ostaju vidljivi uz razlike sredina.

*Slika. Povjerenje po glavnom izvoru vijesti u istom nastavnom uzorku. Izrada autora prema simuliranom skupu @sikic2026.*

## Nakon ukupnog testa

Ukupni test ne govori koje se skupine razlikuju, za koliko i u kojem smjeru.
Nije ni obvezan uvjet za provođenje unaprijed planirane usporedbe. Za
sadržajni odgovor trebamo pojedine procjene s intervalima i jasan popis
pitanja koja smo postavili.

Usporedbu određenu prije pregleda rezultata zovemo **planirana usporedba**. Za
naknadne usporedbe navodimo **post-hoc postupak** i obitelj pitanja koju
štiti. Tukeyjev postupak u klasičnom modelu sa zajedničkom rezidualnom
varijancom obuhvaća sve parove. Daje istodobne intervale koji u toj obitelji
kontroliraju stopu pogreške.

Zašto tim razlikama pridružujemo šire intervale nego jednoj zasebnoj usporedbi?
Promatramo ih više, pa najveća među deset razlika može biti velika i kada
nijednu nismo unaprijed odabrali. Tukeyjev račun uzima u obzir taj izbor
koristeći raspodjelu raspona među skupnim sredinama. Širina istodobnih
intervala zato ovisi o broju skupina i povezanosti usporedbi.

Za jedan par sada oduzmemo dvije sredine iz tablice. Razlici televizije
prema mrežama pridružujemo marginu `r hr_broj((s15$tv_mreze_gornja - s15$tv_mreze_donja)/2, 2)`
boda, izračunatu zajedničkom rezidualnom varijancom, brojnostima tih dviju
skupina i Tukeyjevim pravilom za svih pet skupina. Oduzimanjem i dodavanjem
te margine nastaju granice intervala. Svih deset usporedbi koristi iste
izvorne odgovore, a ne deset novih uzoraka.

Među `r s15$parova` parova statistički su razlučive četiri usporedbe s društvenim
mrežama. Televizija se od njih razlikuje za `r hr_broj(s15$tv_mreze, 2)` boda, uz istodobni
95-postotni interval od `r hr_broj(s15$tv_mreze_donja, 2)` do `r hr_broj(s15$tv_mreze_gornja, 2)`. Razlika tiska prema televiziji
iznosi `r hr_broj(s15$tv_tisak, 2)` boda, uz interval od `r hr_broj(s15$tv_tisak_donja, 2)` do `r hr_broj(s15$tv_tisak_gornja, 2)`. Taj par ovim
uzorkom ne razlučujemo.

Na zajedničkoj osi možemo pregledati svih deset razlika. U nazivu para
prvu skupinu uspoređujemo s drugom, pa pozitivna vrijednost znači višu
sredinu prve skupine. Crte su istodobni 95-postotni Tukeyjevi intervali;
okomita crta označuje izostanak razlike.

*Slika. Svih deset parnih razlika iz istoga modela, uz istodobne intervale. Izrada autora.*

Interval za televiziju i tisak širok je više od dva boda. Takav rezultat ne
pokazuje da su skupine jednake. Pokazuje da procjena nije dovoljno precizna za
razlučivanje razlike od nule.

Ako nas unaprijed zanima određena usporedba, primjerice tradicionalnih i
digitalnih izvora, možemo je izravno planirati. Tada ne štitimo obitelj od
deset naknadno odabranih parova. Interval može biti uži, ali samo ako je
pitanje doista određeno prije pregleda sredina. Naknadni izbor ne smijemo
prikazati kao unaprijed planiran.

## Granice pretpostavki

Najprije provjeravamo neovisnost jedinica. Ponovljena mjerenja istih ljudi i
zajedničko kućanstvo, razred, škola, grad, organizacija ili mrežna veza mogu
stvarati ovisnost. Obični klasični, Welchov i rangovni postupak takvu
strukturu ne rješavaju. Modeli za ponovljene i ugniježđene podatke prelaze
opseg knjige.

Zatim pregledavamo ostatke i skupne raspršenosti. Pretpostavka približne
normalnosti odnosi se na ostatke. Klasična inačica pretpostavlja jednake
varijance, što trebamo procijeniti iz više informacija, a ne iz jednog
pokazatelja.

Omjer najveće i najmanje skupne varijance iznosi `r hr_broj(s15$var_omjer, 2)`. Koristimo ga kao
orijentir uz grafove, veličine skupina i način nastanka podataka. Sam ne
potvrđuje valjanost klasičnog testa. Ako nejednake varijance izgledaju
uvjerljivo, Welchov ukupni test zadržava njihove zasebne procjene.

Welchov test daje F od `r hr_broj(s15$welch_f, 2)`, uz četiri stupnja slobode u brojniku i `r hr_broj(s15$welch_df2, 1)` u nazivniku.
Procijenjene sredine i razlike ostaju iste. Provjerili smo osjetljivost
ukupnog zaključka na račun nesigurnosti, ali time nismo dokazali jednake
varijance ni opravdali Tukeyjeve intervale. Ako varijance nisu jednake, za
parove možemo provesti Welchove usporedbe uz Bonferronijevu korekciju. Svaku uspoređujemo s pragom 0,05 podijeljenim brojem planiranih parova. To je zasebno od Tukeyjeva postupka.

Kruskal-Wallisov postupak rangira vrijednosti i uspoređuje raspodjele rangova.
Utjecaj krajnjeg opažanja zato više ne ovisi izravno o njegovoj brojčanoj
udaljenosti, ali postupak i dalje ima pretpostavke i ispituje drugo pitanje. U našem uzorku
statistika iznosi `r hr_broj(s15$kw, 1)`. Uspoređujemo je s približnom
hi-kvadrat raspodjelom uz `r s15_k - 1` stupnjeva slobode, jedan manje od
broja skupina. Na razini 0,05 kritična vrijednost te hi-kvadrat raspodjele iznosi
`r hr_broj(qchisq(0.95, s15_k - 1), 2)`. To nije F-raspodjela s dvama
brojevima stupnjeva slobode.
Za tumačenje razlike u položaju potrebni su usporedivi oblici raspodjela.
Rangiranje također ne uklanja ovisnost redaka.

**Statistika u divljini.**
**Značajno ovdje, neznačajno ondje.** Pretpostavimo da istražujemo
program pomoći pri učenju u dvjema dobnim skupinama. U svakoj
uspoređujemo sudionike programa s odgovarajućom kontrolnom
skupinom. Prvi rezultat označen je kao značajan, a drugi
nije. U sažetku zato napišemo da program djeluje samo na
mlađe i predložimo da se ubuduće nudi samo njima. Ta je
odluka ovdje zamišljena, ali pogreška na kojoj počiva
dokumentirana je u istraživačkoj literaturi.

Nieuwenhuis, Forstmann i Wagenmakers pregledali su 513 neuroznanstvenih
radova iz pet vodećih časopisa. Među njima su
pronašli 78 koji su izravno testirali razliku dvaju učinaka
i 79 koji su je zaključili iz toga što je jedan učinak bio
značajan, a drugi nije (Nieuwenhuis, 2011). Zasebni testovi
odgovaraju razlikuje li se svaki učinak od svoje nulte
vrijednosti. Ne odgovaraju razlikuju li se učinci međusobno.

U našem bi primjeru procjene koristi programa mogle biti
slične, dok bi jedna imala širi interval zbog manjeg uzorka
ili veće raspršenosti. Tada bi različite oznake značajnosti
odražavale različitu preciznost, a ne dokaz da dob mijenja
korist programa. Kad bismo prema tim oznakama suzili
buduću primjenu, sadržajnu bismo odluku oslonili na
usporedbu koja još nije provedena.

Potrebno je izravno procijeniti razliku između dvaju učinaka i njezinu
nesigurnost. Kao i pri razlikovanju ukupnog testa od pojedinačnih usporedbi,
prvo određujemo koju razliku tvrdnja traži. Pritom treba opravdati nacrt
unutar svake dobne skupine. Dodatni račun ne može nadoknaditi loše
osmišljenu usporedbu.

Ako je interval razlike učinaka širok, možda još ne
možemo odlučiti treba li program prilagoditi dobi. To
je korisnije znati nego jednu skupinu proglasiti
neprikladnom za program. Razlika između dviju oznaka
značajnosti može biti povod za pitanje, ali odgovor
traži procjenu razlike o kojoj stvarno odlučujemo.

**Nađite grešku.**
Nakon ukupnog testa razlika u povjerenju među korisnicima pet izvora
vijesti tim želi pregledati sve parove. Podaci su iz poznate simulacije
(Šikić, 2026). U ovoj nastavnoj provjeri pretpostavke o neovisnosti,
raspodjelama i jednakim varijancama smatramo zadovoljenima. Zadatak je
procijeniti postupak donošenja odluka o parovima.

Asistent je pripremio ovaj zapis, koji treba čitati, a ne izvršavati.

> ```r
> model <- aov(povjerenje_medijima ~ izvor_vijesti,
             data = pet_izvora)
> pairwise.t.test(
>   pet_izvora$povjerenje_medijima,
>   pet_izvora$izvor_vijesti,
>   p.adjust.method = "none"
> )
> ```

> Ukupni test ispituje jesu li sve skupne sredine jednake. S pet
> skupina imamo deset parova. Nakon značajnog ukupnog testa svaki par
> možemo prosuditi na razini 0,05 bez prilagodbe, a da vjerojatnost barem
> jedne pogrešne tvrdnje o parovima ostane zaštićena na toj razini.

Odvojite pitanje ukupnog testa od pitanja pojedinačnih parova. Navedite
koju tvrdnju o zaštiti treba popraviti i predložite postupak iz poglavlja
kojim bi tim izvijestio parne razlike uz odgovarajuću nesigurnost.
Sačuvajte ispravno određene skupine i broj usporedbi. Ne pišite zamjenski kod.

## Razrađeni primjer

U povjerenju korisnika pet izvora vijesti želimo razdvojiti dva pitanja. Prvo
se odnosi na ukupan obrazac skupnih sredina, a drugo na veličinu konkretnih
razlika među izvorima. Najprije ćemo prikazati veličinu učinka i ukupni test, a
zatim parne razlike s istodobnim intervalima. Tako će uz svaku usporedbu ostati
vidljivo da je dio šireg skupa odluka.

Račun počinje modelom skupnih sredina. Poziv `aov` procjenjuje isti
model kao `lm`, ali prikazuje razlaganje varijance iz kojega prvo
računamo eta-kvadrat. Uobičajeni F-test zatim uspoređuje srednje kvadrate uz
pretpostavku zajedničke rezidualne varijance. Pod istom pretpostavkom
`TukeyHSD` daje parne razlike, istodobne intervale i korigirane
p-vrijednosti. Zato te rezultate čitamo kao klasičnu analizu, uz ranije
objašnjenu razliku prema Welchovu postupku.

Zbrojevi kvadrata `r hr_broj(s15$ss_izmedu, 1)` između skupina i `r hr_broj(s15$ss_unutar, 1)` unutar njih daju
opisani udio varijabilnosti. F-test provjerava ukupno odstupanje od jednakih
sredina. Na prethodnom prikazu parova vidimo da se društvene mreže odvajaju od svakog
preostalog izvora, dok ostale parove ne razlučujemo.

U izvještaju možemo navesti da skupine u simuliranom uzorku opisuju oko
desetinu varijabilnosti, uz napomenu da nesigurnost toga udjela ovdje nije
procijenjena. Razlika televizije i društvenih mreža iznosi oko 1,59 bodova na
ljestvici od deset, uz istodobni 95-postotni interval približno od 0,71 do
2,46. Sve četiri usporedbe s društvenim mrežama razlučive su pod
pretpostavkama prikazanog postupka. Podaci ipak ne opravdavaju uzročni
zaključak.

## Sažetak

Kada usporedbu proširimo na više skupina, trebamo pratiti i veću mogućnost
barem jednoga lažnog nalaza. Razlaganje varijabilnosti između skupina i unutar
njih omogućuje jedno ukupno pitanje o jednakosti sredina, na koje odgovara
F-test. Eta-kvadrat opisuje udio varijabilnosti povezan sa skupinama, uz
ograničenje da njegovu uzoračku nesigurnost u ovom primjeru nismo
kvantificirali. Za odgovor o konkretnoj razlici ipak trebamo planiranu
usporedbu ili imenovani post-hoc postupak s odgovarajućim intervalima. Njihove
pretpostavke procjenjujemo prema nacrtu, grafovima i skupnim podacima, a za
ovisna opažanja trebamo drukčiji postupak. Dosad je model povezivao povjerenje
s oznakom skupine, dok ćemo ga u sljedećem poglavlju proširiti na brojčane
prediktore i više varijabli zajedno.

## Pojmovi

Tukeyjev postupak (*Tukey HSD*), Kruskal-Wallisov postupak (*Kruskal-Wallis test*),
analiza varijance (*analysis of variance*), stopa obiteljske pogreške
(*familywise error rate*), F-statistika (*F-statistic*), planirana usporedba
(*planned comparison*), post-hoc postupak (*post-hoc procedure*), eta-kvadrat
(*eta squared*), varijanca između skupina (*between-group variance*), varijanca
unutar skupina (*within-group variance*)

## Zadaci

### Konceptualni

Objasnite zašto značajan ukupni test ne znači da se svaki par skupina razlikuje.
Skicirajte tri skupne sredine i raspršenosti uz koje bi ukupni test bio značajan,
a samo jedan par razlučiv. Zatim pretpostavite da ste taj par odabrali tek nakon
pregleda svih sredina. Odredite je li usporedba planirana ili post-hoc, imenujte
obitelj koju treba zaštititi i objasnite zašto je ne smijete prikazati kao jedno
unaprijed postavljeno pitanje.

### Računski

Razlaganje daje 120 na razlike među četirima skupinama i 480 na razlike unutar
njih, uz ukupno sto opažanja. Izračunajte obje prosječne raspršenosti, njihov
omjer i eta-kvadrat. Objasnite što bi se s omjerom dogodilo da je drugi broj
dvostruko veći.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi razlike između opisne i uzročne
tvrdnje te poglavlju o veličini učinka i snazi radi najmanjega važnog učinka. U
agregiranoj tablici `data/populacija-medija-agregat.csv` pronađite retke za TV
i društvene mreže.
Prije računanja zapišite najmanju razliku na ljestvici od 1 do 10 koju biste
smatrali sadržajno važnom. Izračunajte populacijsku razliku iz stupaca
`zbroj_povjerenja` i `broj`, usporedite je sa svojim pragom i objasnite zašto
rezultat ne dokazuje da odabir izvora uzrokuje povjerenje.

### Revizija modela

Ocijenite postupak i obrazloženje iz okvira. Imenujte jedinu pogrešku,
odredite koju stopu pogreške ugrožava i razdvojite taj prigovor od dijelova
analize koji su još korisni. Predložite način izvještavanja parnih razlika
koji odgovara cijeloj obitelji usporedbi. Ne pokrećite kod i ne pišite
njegovu zamjenu.

---

# Regresija — opći okvir

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/16-regresija.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Breiman je 2001. opisao dva pristupa statističkom modeliranju (Breiman, 2001).
U prvome istraživač postavlja model nastanka podataka i tumači njegove
parametre. U drugome postupak procjenjuje prema tome koliko dobro predviđa
nove ishode.

Upozorio je da dobro pristajanje opaženim podacima nije dovoljno za procjenu
modela. Model može dobro opisati postojeći skup, a slabo predviđati nove
rezultate ili pogrešno prikazivati mehanizam nastanka podataka.

Istom jednadžbom možemo opisivati odnos, predviđati novu osobu ili pokušati
procijeniti uzročni učinak. Za ta tri cilja trebaju različiti dokazi. Kako
prepoznati što model doista omogućuje?

Uspoređivali smo prosječno povjerenje među korisnicima različitih izvora
vijesti. Sada nas zanima kako se ono razlikuje s dobi, bez razvrstavanja ljudi
u dobne skupine. Možemo
postaviti pravac koji za svaku dob daje predviđeni prosjek i zatim provjeriti
što takav opis propušta.

Regresija povezuje nekoliko postupaka koje već poznajemo. Korelacija nas je
naučila čitati smjer i jačinu linearne veze, a usporedbe dviju i više skupina
pokazale su kako oznake skupina ulaze u linearni model. Sada ćemo brojčani i
kategorički prediktor promatrati zajedno. Pitanje iz poglavlja o mjerenju i
dizajnu pritom ostaje otvoreno. Trebamo procijeniti opisuje li model odnos ili
imamo i razloge za uzročno tumačenje.

Polazimo od svih 50.000 zamišljenih odraslih osoba u skupu
`populacija_medija`, koristeći dob, glavni izvor vijesti i povjerenje u medije
(Šikić, 2026). Jedan zapis pripada jednoj osobi. Budući da za ovaj opis
koristimo cijelu konačnu simuliranu populaciju, ne procjenjujemo nepoznatu
vrijednost iz uzorka. Koeficijenti će sažeti zabilježene odgovore, a od njih
ćemo odvojiti pravila kojima su ti odgovori stvoreni. Pri povratku ranijim
uzorcima ponovno ćemo razmotriti i njihovu nesigurnost.

Odabrani pravac usporedit ćemo s opažanjima preko njihovih odstupanja,
reziduala. Tako ćemo razumjeti metodu najmanjih kvadrata prije tumačenja
koeficijenata. Dodavanjem izvora vijesti usporedit ćemo zbirni odnos dobi i
povjerenja s odnosom pri jednakom izvoru, a interakcijom dopustiti da nagib
ovisi o drugoj varijabli. Grafovi reziduala pomoći će nam provjeriti
prilagodbu.

Model ćemo na kraju prosuđivati prema svrsi. Dobar opis opaženih odgovora,
uspješno predviđanje nove osobe i objašnjenje uzroka traže različite provjere.
Trebamo znati što koeficijent uspoređuje, što je ostalo izvan modela i koji bi
dodatni dokaz podupro jači zaključak.

## Pravac kao tvrdnja o prosjeku

Povjerenje u medije bilježimo na ljestvici od jedan do deset, a dob u
godinama (Šikić, 2026). Korelacija bi sažela jačinu linearne veze. Regresijski
pravac omogućuje da za odabranu razliku u godinama očitamo modelom
predviđenu razliku u bodovima povjerenja.

**Podsjetnik.** Nagib

Cilj analize je linearni sažetak zabilježenih odgovora svih pedeset tisuća
osoba. Budući da analiziramo cijelu zadanu populaciju, nema nesigurnosti zbog
uzorkovanja. Pravilo kojim su podaci generirani odnosi se na vrijednosti prije
zaokruživanja i ograničavanja ljestvice. Njegove koeficijente trebamo
razlikovati od koeficijenata za zabilježene odgovore. Procjenjivane veličine
u ovom su poglavlju koeficijenti najmanjih kvadrata za cijelu konačnu populaciju.

*Slika. Prosječno povjerenje po godini dobi u simuliranoj populaciji, s pravcem najmanjih kvadrata izračunatim na svih pedeset tisuća pojedinačnih odgovora. Izrada autora; podaci i postupak opisani su u tekstu.*

Na slici jedna točka sažima sve osobe iste cijele godine dobi. Za nju
zbrajamo njihove ocjene i dijelimo njihovim brojem. Pravac ipak računamo iz
svih pojedinačnih odgovora, pa dob s više osoba nosi veću težinu. Ne
prilagođavamo ga dobnim prosjecima kojima bismo dali jednaku težinu.

Za svaki odabrani odsječak i nagib možemo izračunati odstupanje svakog
opažanja od pravca. Tražimo kombinaciju koja daje najmanji
zbroj kvadrata tih odstupanja.

**Rezidual** je razlika između opažene vrijednosti ishoda kod pojedine jedinice
i vrijednosti koju za nju predviđa model, dakle onaj dio ishoda koji model nije
objasnio.

Rezidual osobe $i$ označujemo s $e_i$, opaženi ishod s $y_i$, a modelom
predviđenu vrijednost s $\hat{y}_i$. Kapica označuje vrijednost dobivenu prilagodbom modela. U konačnoj
populaciji možemo je izračunati bez uzorkovanja. Rezidual $e_i$ opaženo je
odstupanje od prilagođenog pravca, dok $\varepsilon_i$ označuje neopaženo
odstupanje od pretpostavljene populacijske regresijske sredine.

$$e_i = y_i - \hat{y}_i$$

Sami reziduali mogu se poništiti jer su jedni pozitivni, a drugi negativni.
Zato ih kvadriramo prije zbrajanja. Kvadrat daje veću težinu velikim
odstupanjima, pa krajnja opažanja mogu snažno utjecati na odabrani pravac.

**Metoda najmanjih kvadrata** bira koeficijente modela tako da zbroj kvadriranih
reziduala bude najmanji mogući za zadane podatke.

Ovdje računamo koeficijente najmanjih kvadrata za cijelu konačnu populaciju.
Model ima poznati oblik iz usporedbe skupina. Ishod $y_i$ opisujemo odsječkom
$\beta_0$, nagibom $\beta_1$ pomnoženim s prediktorom $x_i$ i odstupanjem
$\varepsilon_i$.

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

Model s jednim brojčanim prediktorom zovemo **jednostavna linearna
regresija**.

Odsječak $\beta_0$ daje modelsku vrijednost ishoda kada je prediktor nula.
Ovdje $\beta_0$ i $\beta_1$ pripadaju cijeloj fiksnoj populaciji, a $e_i$ je
izračunati rezidual osobe. Kada bismo koristili uzorak, procjene ciljnih
koeficijenata označili bismo kapicama i prikazali njihovu nesigurnost. Za
razliku od binarne usporedbe skupina, $x_i$ sada predstavlja izmjeren broj.

Pogledajmo tri pojedinačna zapisa prije tumačenja koeficijenata. Stupac
predviđanja dobivamo uvrštavanjem dobi u izračunati pravac, a rezidual
oduzimanjem toga predviđanja od zabilježenoga odgovora.

*Slika. Prva tri opažanja i njihovi reziduali u zbirnom modelu dobi. Izrada autora.*

Za prvu osobu račun glasi
$`r hr_broj(s16$presjek_jedan, 4)` + `r hr_broj(s16$nagib_jedan, 4)`
\times `r populacija_medija$dob[1]`$, približno
`r hr_broj(fitted(m16_jedan)[1], 3)` boda. Kvadrat njezina reziduala,
`r hr_broj(residuals(m16_jedan)[1]^2, 3)`, jedan je od 50.000 članova zbroja
koji smo minimizirali. Za račun koristimo nezaokružene koeficijente.

Nagib iznosi `r hr_broj(s16$nagib_jedan, 4)` boda po godini. Deset godina veća dob povezana je s
modelskom razlikom od `r hr_broj(10 * s16$nagib_jedan, 2)` boda povjerenja. Odsječak `r hr_broj(s16$presjek_jedan, 2)` odnosio bi
se na dob nula, izvan naših podataka. Možemo ga učiniti razumljivijim ako od
dobi oduzmemo njezinu sredinu. Tada odsječak opisuje osobu prosječne dobi, a
nagib ostaje isti.

Pravac sažima prosječan odnos. Točke na slici predstavljaju prosjeke nekoliko
stotina ljudi iste dobi i leže blizu pravca. Pojedinačni odgovori ipak
odstupaju po nekoliko bodova. Viši predviđeni prosjek za pedesetogodišnjake
nego za tridesetogodišnjake ne određuje odgovor konkretne osobe.

## Nagib koji nosi tuđu priču

Koeficijent za zabilježeno povjerenje iznosi `r hr_broj(s16$nagib_jedan, 4)` boda po godini. Znamo
ga bez uzoračne nesigurnosti jer imamo cijelu populaciju. Generator je prije
zaokruživanja i ograničavanja ishoda koristio latentni, neposredno neopaženi nagib `r hr_broj(s16$latentno_dob, 3)`.
Razlika tih brojeva ne znači pogrešan izračun. Oni opisuju različite veličine.

U generatoru se s dobi mijenja i izvor vijesti. Prosječna dob kreće se od
`r hr_broj(s16$dob_mreze, 1)` godine među korisnicima društvenih mreža do `r hr_broj(s16$dob_radio, 1)` među
slušateljima radija. Povjerenje ovisi o oba obilježja. Zbirni nagib uz dob
zato uključuje i razlike povezane s izborom izvora.

Provjerimo odnos unutar svakog izvora. Generator zadaje isti latentni dobni
nagib svim skupinama. Očekujemo da će njihovi zasebni nagibi biti manji od
zbirnoga jer unutar skupine izvor ostaje isti.

*Slika. Nagib uz dob izračunat zasebno među korisnicima svakog izvora vijesti, uz zbirni konačnopopulacijski nagib i latentno pravilo prije mjerenja. Izrada autora.*

Skupni nagibi kreću se od `r hr_broj(s16$nagib_unutar_min, 4)` do `r hr_broj(s16$nagib_unutar_max, 4)`. Zbirni nagib veći je od
svakoga. Blizina skupnih nagiba latentnom pravilu pomaže provjeriti generator,
ali to su i dalje koeficijenti zabilježenih odgovora. Kao u poglavlju o
povezanosti, odnos unutar skupina razlikuje se od ukupnog odnosa.

Izvor ovdje nije konfundirajuća varijabla u strogom uzročnom smislu. U
poznatom generatoru nastaje nakon dobi i prije povjerenja, pa nalikuje
posredniku. Zbirni koeficijent opisuje ukupni dobni obrazac, a koeficijent pri
jednakom izvoru uvjetni obrazac koji isključuje taj put. Nijedan ne pokazuje
kako bi se mijenjalo povjerenje iste osobe tijekom starenja.

Različiti odgovori ne nastaju zbog manjka podataka. Analiziramo svih pedeset
tisuća osoba. Kada bismo uzeli uzorak, procjenjivali bismo iste ciljane
koeficijente uz odgovarajuću nesigurnost. Interval ni tada ne bi opisivao
udaljenost od latentnog pravila prije mjerenja.

## Prilagodba i ono što je čini mogućom

Zasebni nagibi pokazali su nam odnos dobi i povjerenja unutar svakog izvora.
Ako dob i izvor uključimo u isti model, možemo zajedno izračunati dobni nagib
pri jednakom izvoru i razlike među izvorima pri jednakoj dobi. Time pitanje o
zbirnom odnosu pretvaramo u skup uvjetnih usporedbi.

**Višestruka regresija** procjenjuje modelnu povezanost svakog prediktora s
ishodom pri zadanim jednakim vrijednostima svih ostalih prediktora u modelu.
Koeficijent je uvjetna usporedba koju zadaje model; kao usporedba podataka
obranjiv je samo ondje gdje postoji dovoljno potpore i preklapanja, pa ne mora
označavati stvarno uparene jedinice.

Na primjer, usporedbu četrdesetogodišnjaka koji prate televiziju i portale
možemo poduprijeti podacima ako obje skupine sadrže dovoljno ljudi blizu te
dobi. Kad jedna skupina sadrži samo mnogo starije osobe, procjena za
četrdesetogodišnjake produžuje pravac izvan opaženoga raspona. To zovemo
ekstrapolacijom. Samo uključivanje dobi u formulu ne stvara nedostajuće usporedive osobe.

Za ovaj model napišimo cijelu jednadžbu. Oznaka $I_{\mathrm{TV},i}$ ima
vrijednost jedan za korisnika televizije i nula za ostale, a jednako
definiramo indikatore radija, tiska i društvenih mreža. Portal je referenca
za koju su sva četiri indikatora nula.

$$
y_i=\beta_0+\beta_1\,\mathrm{dob}_i+
\beta_2 I_{\mathrm{TV},i}+\beta_3 I_{\mathrm{radio},i}+
\beta_4 I_{\mathrm{tisak},i}+\beta_5 I_{\mathrm{mreže},i}+\varepsilon_i.
$$

Koeficijenti daju konkretan račun za svih pedeset tisuća simuliranih osoba.
Ovdje su opis konačne populacije, pa im ne pridružujemo interval uzorkovanja.

*Slika. Svi koeficijenti modela s dobi i glavnim izvorom vijesti. Portal je referenca. Izrada autora.*

Svaka osoba ostaje u istom retku, ali pravac sada dobiva i dodatak za
njezin izvor. Za portal je dodatak nula. Za korisnika televizije od 40
godina zbrajamo odsječak `r hr_broj(coef(m16_dva)[1], 3)`, dobni dio
$40 \times `r hr_broj(coef(m16_dva)["dob"], 4)`$ i televizijski dodatak
`r hr_broj(coef(m16_dva)["izvor_vijestiTV"], 3)`. Rezultat je
`r hr_broj(predict(m16_dva, data.frame(dob = 40, izvor_vijesti = "TV")), 3)`
boda. To je modelno predviđanje za zadana obilježja, ne odgovor određene
osobe. Za korisnika portala iste dobi mijenja se samo dodatak izvora.

U modelu s dobi i izvorom nagib uz dob iznosi `r hr_broj(s16$nagib_dva, 4)`. To je uvjetni
linearni sažetak ove populacije. Blizak je latentnom pravilu `r hr_broj(s16$latentno_dob, 3)`, ali ne
procjenjuje istu veličinu. Slaganje koristimo samo za zasebnu provjeru
poznatog generatora.

*Slika. Konačnopopulacijski koeficijenti izvora vijesti uz jednaku dob, uz latentna pravila prije mjerenja. Portal je referentna skupina. Izrada autora.*

Stupci tablice razlikuju latentno pravilo i koeficijente zabilježene
ljestvice. Potonji su ovdje blago manji zbog zaokruživanja i ograničavanja
vrijednosti na jedan do deset. Ne očekujemo da budu posve jednaki brojevima
prije tih promjena.

Uvid u generator ovdje nam omogućuje usporedbu koju u stvarnom istraživanju
obično nemamo. Bez zabilježenog izvora vijesti nagib uz dob ostao bi
`r hr_broj(s16$nagib_jedan, 4)`. Ispis sam ne bi objasnio da taj broj odgovara zbirnom, a ne
uvjetnom pitanju.

„Kontrola” u regresiji znači usporedbu pri jednakim vrijednostima uključenih
varijabli. Ona nije zamjena za randomizaciju. U pokusu randomizacija čini
dodjelu neovisnom o početnim obilježjima i uravnotežuje skupine u očekivanju.
U konkretnom uzorku mogu ostati slučajne razlike, a provedba i osipanje mogu
narušiti usporedbu.

Koeficijent možemo opisati ovako. Ondje gdje podaci podupiru usporedbu, deset
godina veća dob uz jednak izvor vijesti povezana je s modelskim prosjekom
povjerenja višim za `r hr_broj(10 * s16$nagib_dva, 2)` boda. Naveli smo jedinicu prediktora, jedinicu
ishoda i uvjet usporedbe. Za kategorički prediktor navodimo i referentnu
skupinu.

Mogli bismo sada pomisliti da će uključivanje svake dostupne varijable dati
bolju usporedbu. No već je izvor vijesti promijenio pitanje na koje odgovara
dobni koeficijent. Prije sljedeće prilagodbe zato trebamo razmotriti ulogu te
varijable u nastanku podataka. Dijagram razlikuje tri uloge zbog kojih ista
računska radnja može imati različite posljedice.

*Slika. Tri uloge treće varijable u uzročnom dijagramu. Prilagodba za zajednički uzrok može zatvoriti neuzročni put, prilagodba za posrednika mijenja cilj s ukupne na izravnu vezu, a prilagodba za kolider može otvoriti novu pristranost. Izrada autora.*

Zajednički uzrok prethodi izloženosti i ishodu te može opravdati prilagodbu.
Posrednik nastaje nakon izloženosti, pa njegovim uključivanjem mijenjamo
ukupnu usporedbu. Kolider je posljedica obiju varijabli. Uvjetovanje na njega
može stvoriti povezanost među inače nepovezanim uzrocima. Prije izbora modela
zato razmatramo vremenski redoslijed, kvalitetu mjerenja i ulogu svake
varijable.

Odsječak sada opisuje osobu dobi nula koja koristi portal. Takve osobe nema u
podacima. Koeficijent je potreban za zapis modela, ali ga ne trebamo sadržajno
tumačiti.

Kada dva prediktora nose gotovo istu informaciju, teško je razdvojiti njihove
pojedinačne koeficijente. Nedostaju usporedbe u kojima se jedan mijenja, a
drugi ostaje isti. Male promjene podataka tada mogu znatno promijeniti
koeficijente, iako njihova zajednička predviđanja ostaju slična.

## Interakcija i regresijski pravac

U dosadašnjem modelu s dobi i izvorom vijesti nagib uz dob jednak je za sve
izvore. Ako nas zanima razlikuje li se nagib među skupinama, trebamo modelu
dopustiti i tu mogućnost. To čini interakcija, kojom nagib jednog prediktora
može ovisiti o drugome. Za planiranu provjeru unaprijed navodimo modifikator,
kodiranje, kontrast i postupak zaključivanja, a kod usmjerene hipoteze i
očekivani smjer. Naknadno uočena razlika među podskupinama može dati novo
pitanje, ali zahtijeva neovisnu provjeru. Modifikator je varijabla prema
kojoj se nagib razlikuje. Kodiranje određuje njezin brojčani zapis,
a kontrast konkretnu razliku koju uspoređujemo.

Sljedeće dvije linije namjerno konstruiramo izvan medijske populacije.
Za svaku cjelobrojnu vrijednost $x$ od 0 do 10 upisujemo $2 + 0,6x$ u A i
$8 - 0,2x$ u B, bez slučajnog odstupanja. Pri $x=5$ vrijednosti su 5 i 7.
Od $x=5$ do $x=6$ prva raste za 0,6, a druga pada za 0,2. Jednako mnogo
točaka na istim vrijednostima $x$ daje zbirnom pravcu prosjek tih nagiba.

U prikazu smo skupini A zadali nagib `r hr_broj(s16$heterogenost_a, 1)`, a skupini B `r hr_broj(s16$heterogenost_b, 1)`. Zbirni
nagib iznosi `r hr_broj(s16$heterogenost_zbirno, 1)` i ne opisuje nijednu skupinu zasebno. Dvije linije
prikazuju razliku koju bi zajednički koeficijent sakrio. Ako je $B=1$
za drugu skupinu, a $B=0$ za prvu, obje zapisujemo jednadžbom
$\hat y=2+0,6x+6B-0,8xB$. Član $xB$ mijenja nagib iz 0,6 u −0,2.
Taj namjerno izražen primjer služi učenju interakcije; ne tvrdi da su
takve razlike nagiba prisutne u prethodnoj medijskoj populaciji.

*Slika. Predviđene vrijednosti u simuliranom primjeru s različitim skupnim nagibima. Deblja zbirna linija opisuje prosjek koji ne vrijedi ni za jednu skupinu. Izrada autora.*

Interakciju čitamo kroz skupne nagibe ili predviđene vrijednosti. Značajan
nagib u jednoj i neznačajan u drugoj skupini ne dokazuje da se nagibi
razlikuju. Potrebna je izravna procjena interakcije s nesigurnošću
(Nieuwenhuis, 2011). Ovaj deterministički primjer pokazuje oblik odnosa. U
stvarnoj analizi trebalo bi prikazati i interval za razliku nagiba.

Za pomicanje pravca stvaramo drugi nastavni skup od 52 zapisa, s vremenom,
angažmanom i prethodnim interesom. Interes generiramo normalno sa sredinom
nula i standardnom devijacijom jedan. Vrijeme nastaje kao $5 + 1,8$
puta interes, uz neovisno odstupanje standardne devijacije 1,5 i donju
granicu nula. Angažman je $20 + 2,3$ puta vrijeme $+ 7$ puta interes,
uz drugo neovisno odstupanje standardne devijacije 4,5. Zato prethodni
interes ovdje prethodi objema varijablama i utječe na obje. To je drukčije
pravilo od dobnog puta preko izvora vijesti u glavnom primjeru.

Sljedeći prikaz povezuje položaj pravca i duljinu reziduala. Zadani pravac
uspoređujemo s pravcem najmanjih kvadrata i s pravcem prilagođenim za
prethodni interes. Koristimo manji simulirani skup kako bismo mogli vidjeti
pojedinačna odstupanja.

*Slika. Regresijski pravac — pomični pravac, reziduali i usporedba zbirnog s prilagođenim nagibom.*

**Što isprobati.**

1. Mijenjajte odsječak i nagib dok se zbroj kvadrata ne približi prikazanom
   minimumu.
2. Povećajte samo nagib za jednu jedinicu i pratite koji se reziduali najviše
   produljuju.
3. Uključite model s prethodnim interesom i usporedite njegov nagib sa zbirnim
   pravcem.

Blizu minimuma manji pomaci pravca mogu samo malo povećati zbroj kvadrata. Kod
uzorka je taj odnos dio računa nesigurnosti koeficijenata. Ovaj prikaz sam ne
daje interval ni procjenu uzoračne nesigurnosti.

Prije nastavka vratite se glavnom primjeru s povjerenjem. Pokušajte bez
ponovnog čitanja objasniti koju veličinu ondje računamo, što mjeri rezidual,
kako biramo pravac i što bi bilo potrebno za uzročni zaključak.

## Isti model iza ranijih poglavlja

Model s binarnim prediktorom daje razliku dviju sredina. Model s više
kategorija daje razlike prema referentnoj skupini. Sada smo dodali brojčani
prediktor. Provjerimo vezu s ranijim računima.

Uzorak od sto dvadeset osoba iz poglavlja o dvjema grupama daje razliku
sredina `r hr_broj(s16$razlika_dvije, 2)` boda. Koeficijent uz izvor u modelu iznosi `r hr_broj(s16$koef_dvije, 2)`. To su
dva zapisa iste točkaste procjene.

Omjer koeficijenta i obične homoskedastične standardne pogreške iznosi
`r hr_broj(s16$t_dvije, 2)`. Jednak je združenom Studentovu t-testu s postavkom `var.equal = TRUE`. Oba
koriste zajedničku rezidualnu varijancu i `r hr_broj(s16$df_student_dvije, 0)` stupnjeva slobode. Welchov
postupak dopušta različite varijance te daje t od `r hr_broj(s16$t_welch_dvije, 2)` i `r hr_broj(s16$df_welch_dvije, 3)`
stupnja slobode. Procijenjena razlika ostaje jednaka, ali račun nesigurnosti
se mijenja.

Na tristo osoba iz poglavlja o više skupina klasični model daje F od
`r hr_broj(s16$f_pet, 2)`, uz `r s16$df1_pet` i `r s16$df2_pet` stupnjeva slobode. To je isti
homoskedastični postupak kao `aov` iz poglavlja Više grupa. Welch daje F od `r hr_broj(s16$f_welch_pet, 2)`,
uz `r hr_broj(s16$df1_welch_pet, 0)` i `r hr_broj(s16$df2_welch_pet, 1)` stupnja slobode. Zajednički model sredina ne znači
jednak test. Objašnjeni udio varijabilnosti u klasičnom modelu iznosi
`r hr_broj(100 * s16$r2_pet, 1)` %, koliko i prethodno izračunati eta-kvadrat.

T-test, analiza varijance i regresija zato mogu dijeliti model sredina. U
svakom izvještaju pitamo koja je jedinica, što se uspoređuje i pod kojim
uvjetima. Zasebno provjeravamo pretpostavke i način računanja nesigurnosti.

Tablica za odabir postupka u mrežnom dodatku pomaže povezati vrstu podataka i
istraživačko pitanje. Pri tom odabiru i dalje provjeravamo ishod, prediktore, neovisnost i
nesigurnost. Sam zapis modela ne određuje trebamo li Welchovu
ili običnu homoskedastičnu inferenciju.

Ako jedna osoba daje više redaka ili osobe dijele razred, ustanovu ili grad,
ponovno provjeravamo jedinicu i ciljanu veličinu. Više redaka može nekim
osobama dati veću težinu, a uobičajena nesigurnost više nema opravdanje
neovisnosti. Trebamo postupak koji uvažava tu strukturu. Takve modele ovdje ne
procjenjujemo.

## Pristajanje i njegove granice

Vezu regresije s analizom varijance možemo iskoristiti i za procjenu
pristajanja. Ondje nas je zanimalo koliki dio varijabilnosti opisuju skupne
sredine. Sada isto pitanje postavljamo za vrijednosti koje predviđa cijeli
model, neovisno o tome sadrži li oznake skupina ili brojčane prediktore.

**Koeficijent determinacije** je udio ukupne varijabilnosti ishoda u promatranom
skupu podataka koji je model objasnio, izračunat kao jedan minus omjer zbroja
kvadrata reziduala i zbroja kvadrata odstupanja od zajedničke sredine.

Mjeru označujemo s $R^2$. U formuli je $e_i$ rezidual, $y_i$ opaženi ishod, a
$\bar{y}$ njegova zajednička sredina.

$$R^2 = 1 - \frac{\sum e_i^2}{\sum (y_i - \bar{y})^2}$$

Za model s dobi zbroj kvadrata 50.000 reziduala iznosi
`r hr_broj(sum(residuals(m16_jedan)^2), 1)`. Bez prediktora svakoj bismo
osobi dodijelili zajednički prosjek. Zbroj kvadrata odstupanja od njega
iznosi `r hr_broj(sum((populacija_medija$povjerenje_medijima - mean(populacija_medija$povjerenje_medijima))^2), 1)`.
Dijeljenjem prvoga zbroja drugim dobivamo preostali dio varijabilnosti, pa
ga oduzimamo od jedan. Usporedba koristi iste osobe i isti ishod.

Model s dobi opisuje `r hr_broj(100 * s16$r2_jedan, 1)` % varijabilnosti povjerenja, a s dobi i izvorom
`r hr_broj(100 * s16$r2_dva, 1)` %. Nizak udio može odražavati razlike među ljudima, mjernu pogrešku
ili neprikladan oblik modela. Sama mjera ne razlikuje te mogućnosti. Blizina
prilagođenog koeficijenta latentnom pravilu također ne mijenja činjenicu da su
to različite veličine.

Za sljedeću provjeru uzimamo novi slučajni uzorak od 200 osoba bez
vraćanja iz te populacije. Svakoj dodajemo pet neovisnih normalnih brojeva
sa sredinom nula i standardnom devijacijom jedan. Ti stupci po pravilu
nastanka nemaju vezu s povjerenjem, iako je u konačnom uzorku mogu slučajno
pokazati. Uspoređujemo dva modela na istih 200 potpunih redaka.

U toj usporedbi osnovni model sadrži dob i glavni izvor vijesti. Prošireni
model istim prediktorima dodaje pet neovisno generiranih normalnih slučajnih
varijabli, označenih `sum1` do `sum5`. Oba se prilagođavaju istim dvjema
stotinama osoba. Dodatne varijable nemaju sadržajno opravdanje.

Na istim redcima i istom ishodu dodavanje prediktora ne smanjuje obični
objašnjeni udio. U uzorku od dvjesto osoba pet slučajnih stupaca povećava ga s
`r hr_broj(100 * s16$r2_bez, 1)` % na `r hr_broj(100 * s16$r2_sa, 1)` %. Prilagođeni koeficijent determinacije uzima u
obzir broj prediktora i pada s `r hr_broj(100 * s16$prilagodeni_bez, 1)` % na `r hr_broj(100 * s16$prilagodeni_sa, 1)` %. Ta prilagodba
pomaže pri usporedbi, ali sama ne provjerava predviđanje, uzročnost ni
sadržajnu valjanost.

Ograničenje raspona također mijenja ovu mjeru. Među osobama od trideset do
pedeset godina nagib iznosi `r hr_broj(s16$nagib_usko, 4)`, gotovo kao prije. Objašnjeni udio ipak
pada s `r hr_broj(100 * s16$r2_jedan, 1)` % na `r hr_broj(100 * s16$r2_usko, 1)` % u skupu od `r hr_broj(s16$n_usko, 0)` ljudi. Koeficijent
determinacije zato ovisi o populaciji i rasponu podataka.

Slični nagibi u različitim populacijama mogu imati vrlo različite objašnjene
udjele. Za usporedbu koeficijenata trebamo provjeriti ishod, ljestvicu,
populaciju, kodiranje i uključene prilagodbe. Kod uzoraka trebamo i intervale
koji odgovaraju nacrtu.

Ni zajednički naziv ne jamči usporedive podatke. U našoj simulaciji „medijska
aktivnost” označuje dnevne minute osobe iz konačne populacije odraslih
(Šikić, 2026). DigiKat obuhvaća platformske objave prema pravilima korpusa, s
jedinicom objave ili agregata (Šikić, 2026). Osobne minute ne prikazuju svako
privatno ponašanje, a korpus ne obuhvaća sadržaj izvan svojeg izbora.
Regresija objava zato ne opisuje osobnu uporabu, a skupni obrazac ne možemo
pripisati pojedincu. Trebamo usporediti konstrukt, jedinicu, populaciju i
obuhvat mjerenja.

Pri sužavanju dobi vraćamo se cijeloj populaciji i zadržavamo osobe od
30 do 50 godina, a ne podskup prethodnih 200. Za sljedeći dijagnostički
primjer ponovno koristimo svih 50.000 osoba, ali mijenjamo ishod iz
povjerenja u dnevne minute. Te su minute generirane tako da s dobi rastu
i očekivana vrijednost i raspršenost (Šikić, 2026).

Jedan objašnjeni udio ipak ne otkriva gdje model slabije odgovara podacima. Za
to se vraćamo pojedinačnim odstupanjima, rezidualima. U našoj populaciji
linearni odnos dnevnog praćenja medija i dobi ima nagib `r hr_broj(s16$nagib_minute, 2)` minute
po godini. Reziduali oko tog pravca nisu jednako raspršeni duž cijelog raspona,
što možemo vidjeti na njihovu prikazu.

*Slika. Reziduali modela za dnevno vrijeme uz medije nasuprot vrijednostima koje model predviđa, na slučajnom podskupu od dvije tisuće osoba. Izrada autora; podaci i postupak opisani su u tekstu.*

Od šestine s najnižim do šestine s najvišim predviđanjima raspršenost
reziduala raste s `r hr_broj(s16$rasprsenost_dolje, 0)` na `r hr_broj(s16$rasprsenost_gore, 0)` minuta. Jedna ukupna mjera zato ne
opisuje pogrešku u svakom dijelu raspona. Kada bismo imali uzorak, račun
nesigurnosti trebao bi dopustiti promjenjivu varijancu. Graf otkriva problem,
a sljedeći korak biramo prema cilju analize.

Vrijeme ne može pasti ispod nule. Zbog te granice donji rub ostataka slijedi
kosu crtu, a osobe s nulom gomilaju se na njoj. Zakrivljenost oblaka i širenje
ostatka prema većim predviđanjima upozoravaju da jedan pravac sa stalnom
varijancom ne opisuje sve dijelove raspodjele jednako dobro. Promjena računa
standardne pogreške može ublažiti problem nesigurnosti, ali ne ispravlja
pogrešan oblik sredine ni predviđanja izvan mogućeg raspona.

Izbor načina izražavanja nesigurnosti ne uklanja potrebu za tim pregledom
modela. Bayesovski pristup, koji smo kratko upoznali uz testiranje, može istom
modelu pridružiti prethodne raspodjele i dati raspodjelu nesigurnosti
koeficijenata ili predviđanja. I tada trebamo dobro mjerenje, prikladne
jedinice i opravdane pretpostavke. Takav račun sam ne rješava curenje
informacija ni uzročno zaključivanje, a ovdje ostajemo na tom kratkom osvrtu.

## Objašnjenje i predviđanje

Za opis odnosa tražimo sadržajno smislen i razumljiv model. Za predviđanje
tražimo malu pogrešku na novim jedinicama. Uzročno objašnjenje zahtijeva
dodatno opravdanje iz nacrta i identifikacijskih pretpostavki, uvjeta
pod kojima opažene odnose možemo pripisati pretpostavljenom uzroku. Shmueli
pokazuje da se ti ciljevi razlikuju već pri izboru mjera i varijabli
(Shmueli, 2010). Model dobar za jedan cilj može biti loš za drugi.

U sljedećim primjerima povjerenje predviđamo neposredno prije nego što nova
osoba odgovori na pitanje o povjerenju. Tada znamo dob i izvor vijesti.
Slučajni stupci kojima ćemo pokazati preprilagodbu također su
dostupni prije odgovora i jednako definirani u oba skupa. Informacije koje
nastaju poslije ishoda ne smijemo koristiti.

Spremnost na plaćanje vijesti u generatoru nastaje nakon povjerenja i pod
njegovim utjecajem. Ako je dodamo modelu povjerenja, objašnjeni udio raste s
`r hr_broj(100 * s16$r2_dva, 1)` % na `r hr_broj(100 * s16$r2_posljedica, 1)` %. Za naš trenutak primjene to je curenje
informacija. Prediktor tada još nije dostupan, pa poboljšanje na postojećim
podacima nije valjan prediktivni dobitak.

Sada izvlačimo zasebnih 150 osoba za učenje, a iz preostalih osoba 2.000
za provjeru. Skupovi se ne preklapaju. Svakom skupu dodajemo 25 neovisnih
normalnih stupaca sa sredinom nula i standardnom devijacijom jedan. To je
novi pokus, različit od prethodnih pet stupaca na 200 osoba. Složeniji
model koristi svih 25 dodataka, a jednostavniji samo dob i izvor. Oba
procjenjujemo na 150 osoba. Dobivene koeficijente zatim zamrzavamo prije
predviđanja za 2.000 odvojenih osoba.

Predviđanje provjeravamo na podacima odvojenima prije procjene modela. Pogrešku
mjerimo srodno ranijem računu reziduala. Odstupanja opaženih odgovora od
predviđanja kvadriramo, izračunamo njihovu sredinu i izvadimo korijen kako
bismo se vratili u bodove povjerenja. Tako možemo usporediti pogrešku na
podacima za učenje s pogreškom na odvojenim osobama. Ovdje je to interna
provjera istog simuliranog mehanizma koja ne dokazuje prijenos u drugo vrijeme,
sustav ili populaciju. Oba uspoređena modela koriste samo informacije dostupne
do zadanog trenutka.

Prva tri zapisa iz skupa za provjeru pokazuju kako nastaje njegova
pogreška. Svako predviđanje dobiveno je bez uporabe odgovora te osobe pri
procjeni koeficijenata. Takvo predviđanje za osobe koje nisu sudjelovale u
prilagodbi modela zovemo predviđanjem izvan uzorka.

*Slika. Odvojene osobe, predviđanja jednostavnijeg modela i kvadrirane pogreške. Izrada autora.*

Prvi kvadrat ulazi u zbroj s još 1.999 takvih kvadrata. Zbroj dijelimo s
2.000 i vadimo korijen. Za učenje je nazivnik 150. Svi su odgovori i
predviđanja definirani, pa nema izostavljanja. Tablica koja slijedi sažima
iste račune za oba modela i za predviđanje prosjekom skupa za učenje.

*Slika. Prosječna pogreška predviđanja dvaju modela na podacima na kojima su procijenjeni i na odvojenom skupu, u bodovima povjerenja. Izrada autora.*

Na skupu za učenje od `r s16$n_ucenje` osoba složeniji model opisuje `r hr_broj(100 * s16$r2_bogat, 1)` %
varijabilnosti, a jednostavniji `r hr_broj(100 * s16$r2_skroman, 1)` %. Na tih istih podacima složeniji
griješi manje. Na odvojenih `r hr_broj(s16$n_provjera, 0)` osoba griješi više od jednostavnijeg
modela, pa i od predviđanja zajedničkim prosjekom skupa za učenje. Prilagodio
se slučajnim obrascima koji se ne ponavljaju u novim podacima.

Jednostavniji model bolji je na ovom odvojenom skupu. Standardna devijacija
povjerenja u populaciji iznosi `r hr_broj(s16$sd_ishoda, 2)` boda, a rezidualna raspršenost nakon
uključivanja dobi i izvora `r hr_broj(s16$sd_ostatka, 2)`. Ostatak uključuje slučajnu sastavnicu
generatora, ali možda i neprimjerenost oblika modela. Ne možemo ga proglasiti
najmanjom pogreškom koju bi bilo koji model mogao postići.

Valjana provjera predviđanja zato zahtijeva odvojene podatke i prediktore
dostupne u trenutku primjene.

## Granica prema uzroku

Konfundirajuća varijabla prethodi pretpostavljenom uzroku i ishodu. Regresija
može za nju prilagoditi usporedbu, ali iz samog ispisa ne možemo utvrditi
njezinu ulogu. Za to trebamo sadržajno znanje, vremenski redoslijed i nacrt
istraživanja.

U našem generatoru izvor vijesti nastaje poslije dobi i prije povjerenja.
Prilagodba za izvor zato zatvara mogući posrednički put i mijenja cilj sa
zbirnog na uvjetni odnos. Blizinu prilagođenog koeficijenta latentnom izravnom
pravilu razumijemo jer poznajemo generator. U stvarnom istraživanju takvo
slaganje ne bismo mogli pretpostaviti.

Prilagođena povezanost sama ne dokazuje uzrok. Trebamo opravdati vremenski
red, izostanak neizmjerenih zajedničkih uzroka i izbor prilagodbi. Važni su i
valjano mjerenje, dovoljno preklapanja usporedivih jedinica, jasno definirana
intervencija, selekcija i oblik modela. Navođenje tih uvjeta još nije dokaz da
su zadovoljeni.

Dob je posebno zahtjevna jer nema jednostavno intervencijsko tumačenje. U
stvarnom istraživanju ulogu dobi i izvora trebali bismo razmotriti prije
računanja. Modelni ispis ne može potvrditi te pretpostavke.

Zato u izvještaju opisujemo usporedbu koju smo doista napravili. Tvrdnja o
tome što bi se dogodilo kada bismo nešto promijenili traži nacrt i
pretpostavke koji opravdavaju takvu promjenu.

Prije riječi „učinak” korisno je zapisati koja bi druga objašnjenja proizvela
isti obrazac i kako ih nacrt isključuje. Ako se ključna pretpostavka ne može
provjeriti ovim podacima, trebamo je jasno navesti uz zaključak.

**Statistika u divljini.**
**Od omjera do dopuštene rečenice.** Školski stručni tim mogao bi
iz istraživanja o društvenim mrežama pokušati zaključiti bi li
ograničenje vremena uporabe smanjilo simptome depresije. U toj
zamišljenoj primjeni nalaz treba pročitati prije nego što ga
pretvorimo u preporuku. Kleppang i suradnici analizirali su
samoprijavljene presječne podatke istraživanja Ungdata iz 2018.,
koji obuhvaćaju 12.353 norveških adolescenata od 15 do 16 godina,
uz ukupni odaziv od 85 % (Kleppang, 2021). Njihov je predmet
povezanost uporabe medija i simptoma, a ne učinak provedene
zabrane.

Ishod u modelu razlikuje rezultat na mjeri simptoma depresije
na ili iznad 80. percentila od nižih rezultata
(Kleppang, 2021). To nije isto što i klinička dijagnoza.
Sljedeći izvadak prikazuje kako se omjeri mijenjaju kada
se društvene mreže i igranje uključe zasebno ili zajedno.

| Prediktor i kategorija | Model 1, društvene mreže AOR (95 % interval) | Model 2, igranje AOR (95 % interval) | Model 3, oba prediktora AOR (95 % interval) |
|---|---:|---:|---:|
| Društvene mreže, do 3 sata | 1 (ref.) | nije u modelu | 1 (ref.) |
| Društvene mreže, više od 3 sata | 1,60 (1,43–1,80) | nije u modelu | 1,51 (1,34–1,70) |
| Igranje, do 3 sata | nije u modelu | 1 (ref.) | 1 (ref.) |
| Igranje, više od 3 sata | nije u modelu | 1,57 (1,36–1,80) | 1,38 (1,19–1,59) |

: Prilagođeni omjeri izgleda za simptome depresije prema uporabi društvenih mreža i igranju. Sadržajno skraćena, preoblikovana i na hrvatski prevedena prilagodba Tablice 3 iz rada Kleppang i suradnika (Kleppang, 2021).

Binarni ishod u ovome radu analizira se logističkom regresijom. Taj model
povezuje prediktore s logaritmom izgleda, a ne s neograničenom sredinom
binarnoga ishoda. Izgledi su omjer vjerojatnosti ishoda i vjerojatnosti
njegova izostanka. Eksponiranjem odgovarajućega koeficijenta dobiva se omjer
izgleda uz ostale prediktore u modelu. Ovdje učimo čitati objavljeni
rezultat; prilagodba i provjera logističkog modela izvan su opsega knjige
(Kleppang, 2021).

AOR označuje prilagođeni omjer izgleda. Sva tri modela
uključuju rod ili spol, imanje prijatelja, pušenje, visoko
obrazovanje roditelja i obiteljsko materijalno stanje
(Kleppang, 2021). Model 3 istodobno uključuje obje aktivnosti, pa je omjer
za mreže prilagođen i za igranje, a omjer za igranje i za uporabu mreža.
Referentne su skupine označene jedinicom.
Prije čitanja nalaza treba razlikovati izglede od vjerojatnosti.
U zamišljenoj skupini u kojoj ishod ima 20 od 100 osoba,
vjerojatnost je 0,20, a izgledi su 20 prema 80, odnosno 0,25.
Za vjerojatnost $p$ isti račun zapisujemo kao $p/(1-p)$.
Omjer izgleda uspoređuje te izglede, a omjer rizika uspoređuje
vjerojatnosti. Nijedan nije razlika u postotnim bodovima.

U Modelu 1 procijenjeni izgledi za ishod kod uporabe mreža
dulje od tri sata iznose 1,60 puta izglede referentne skupine,
uz interval od 1,43 do 1,80 (Kleppang, 2021). Vrijednosti iznad
jedan znače veće, a ispod jedan manje izglede. Interval koji
obuhvaća jedan dopušta i jednake izglede. Tim stoga ne može
nalaz prepričati kao povećanje vjerojatnosti za 60 postotnih
bodova ili kao dokaz da će ograničenje uporabe ukloniti
odgovarajući dio simptoma.

Za predviđenu vjerojatnost trebaju odsječak, ostali
koeficijenti i vrijednosti prediktora. Izvadak ne daje
nazivnike modela, mjere pristajanja ni dijagnostiku, pa
ne omogućuje provjeru gubitka redaka i pristajanja.
Koeficijenti prilagodbenih varijabli nisu automatski
njihovi uzročni učinci (Westreich, 2013).

Školskom timu nalaz pokazuje povezanost vrijednu daljnjeg
proučavanja. Presječni nacrt, samoprijava i mogući neizmjereni
čimbenici ne dopuštaju uzročni zaključak (Kleppang, 2021).
Tablica tako čuva opaženi nalaz, a pokazuje koji dokaz još
nedostaje za odluku o ograničavanju uporabe.

Izvor su Annette Løvheim Kleppang, Anne Mari Steigen, Li Ma,
Hanne Søberg Finbråten i Curt Hagquist, „Electronic media use
and symptoms of depression among adolescents in Norway”,
*PLOS ONE* 16(7), e0254197, 2021,
članak (https://doi.org/10.1371/journal.pone.0254197) i
izvorna Tablica 3 (https://doi.org/10.1371/journal.pone.0254197.t003).
Licenca je
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
Tablica je skraćena, preoblikovana i prevedena na hrvatski.
Brojevi i granice intervala sačuvani su. Prilagodba ne podrazumijeva
odobrenje autora ni PLOS-a.

**Nađite grešku.**
Tim želi provjeriti predviđa li model povjerenje kod novih korisnika
uz korijen srednje kvadratne pogreške manji od dva boda. To je unaprijed
zadan kriterij ove nastavne vježbe. Za prilagodbu je uzeto prvih 200
zapisa simulirane populacije (Šikić, 2026). U zamišljenoj primjeni svi
prediktori dostupni su prije odgovora o povjerenju.

Asistentov račun rabi naziv `uzorak` za tih istih 200 zapisa.

Ispis daje $R^2 =$ `r hr_broj(summary(s16_greska_model)$r.squared, 2)` i
korijen srednje kvadratne pogreške
`r hr_broj(s16_greska_rmse, 2)` boda na ljestvici povjerenja od jedan do
deset. U zapisu nema drugog skupa podataka. Asistent zaključuje sljedeće.

> Izračunane vrijednosti opisuju pristajanje modela navedenim zapisima.
> Pogreška je manja od dva boda, pa je zadani kriterij za nove korisnike
> zadovoljen i model možemo preporučiti za primjenu.

Pratite iz kojih redaka dolaze koeficijenti, a iz kojih pogreške. Napišite
što ovaj ispis već podupire i koju provjeru treba provesti prije odluke
o primjeni. Vaša preporuka treba odrediti kako bi se novi rezultat
usporedio s unaprijed zadanim kriterijem.

## Razrađeni primjer

Vratimo se pitanju s početka poglavlja. Koliko se povjerenje razlikuje s dobi i
što se u tom odgovoru promijeni kada uspoređujemo osobe s jednakim izvorom
vijesti? Izračunat ćemo oba nagiba na istim zabilježenim odgovorima svih
pedeset tisuća osoba. Tako razliku među koeficijentima možemo povezati s
promjenom pitanja, bez promjene analizirane populacije.

Funkcija `lm` ovdje računa opis cijele konačne populacije. Zato ne
koristimo `confint` za uzoračne intervale. Uobičajeni interval te funkcije
odnosio bi se na drugi modelni ili nadpopulacijski cilj. To znači
zaključivanje o zamišljenom procesu koji bi stvarao i druge populacije,
a taj cilj ovdje nismo odabrali.

*Slika. Konačnopopulacijski nagib uz dob u dvama modelima za zabilježeni ishod. Izrada autora.*

Oba nagiba znamo točno za zadanu populaciju. Zbirni uključuje dobni obrazac
povezan s izborom izvora, dok prilagođeni uspoređuje pri jednakom izvoru.
Različite brojke proizlaze iz različitih pitanja. Izvještaj mora pokazati koje
je pitanje postavljeno.

U zbirnom modelu deset godina veća dob povezana je s predviđenim prosjekom
povjerenja višim za `r hr_broj(10 * s16$nagib_jedan, 2)` boda. Uz jednak izvor razlika iznosi `r hr_broj(10 * s16$nagib_dva, 2)`
boda. Prva rečenica opisuje ukupni, a druga uvjetni linearni odnos.

Ovim smo koeficijentima opisali cijelu zadanu populaciju, pa im ne pridružujemo
uzoračni interval. Kada bismo istu usporedbu procjenjivali iz uzorka, trebali
bismo odgovarajuću nesigurnost. Za predviđanje odgovora nove osobe trebali
bismo i provjeru na odvojenim podacima, uz prediktore dostupne u trenutku
primjene. Uzročna tvrdnja tražila bi dodatno opravdanje izvan ovog računa.

Granica našeg opisa ovisi i o onome što smo uključili u model. Uz dva odabrana
prediktora u stvarnom bismo istraživanju razmotrili, primjerice, obrazovanje,
iskustvo s redakcijama ili političke sklonosti. Njihovo uključivanje moglo bi
promijeniti ciljanu uvjetnu usporedbu i koeficijent.

Ni jedan prikazani nagib ne govori kako bi se povjerenje iste osobe
promijenilo starenjem ili promjenom izvora vijesti. Opisali smo populaciju u
jednom trenutku. Za promjenu unutar osobe trebaju podaci koji je prate kroz
vrijeme, a ovdje ih nemamo.

## Sažetak

Regresiju možemo čitati kao nastavak ranijih usporedbi, u kojem najmanji
kvadrati biraju koeficijente prema odstupanjima opažanja od predviđenih
vrijednosti. Dodavanjem prediktora prelazimo na uvjetne usporedbe, a
interakcijom dopuštamo da se nagibi razlikuju. Naš je primjer pokazao zašto
koeficijente zabilježenih odgovora, nakon zaokruživanja i ograničavanja
ljestvice, trebamo razlikovati od pravila kojima smo podatke stvorili.
Reziduali pomažu provjeriti pristajanje, a veći objašnjeni udio ne jamči
bolje predviđanje novih osoba jer ga mogu povećati i slučajni prediktori. Zato
predviđanje provjeravamo na odvojenim jedinicama uz informacije dostupne u
trenutku primjene, dok uzročno tumačenje prilagođene povezanosti traži dodatno
opravdanje. S tom razlikom između opisa, predviđanja i uzroka možemo u
sljedećem poglavlju prosuditi kako se modeli koriste u odlukama o ljudima.

## Pojmovi

linearna regresija (*linear regression*), procjenjivana veličina (*estimand*),
rezidual (*residual*), metoda najmanjih kvadrata (*least squares*), višestruka
regresija (*multiple regression*), prilagođena povezanost (*adjusted
association*), koeficijent determinacije (*R-squared*), interakcija
(*interaction*), curenje informacija (*information leakage*), predviđanje izvan
uzorka (*out-of-sample prediction*), izgledi (*odds*), omjer izgleda (*odds ratio*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto se nagib uz dob mijenja kada u model uđe izvor
vijesti, a nijedan podatak o dobi pritom nije promijenjen. Imenujte pitanje na
koje odgovara svaki od dvaju nagiba. Na prikazu interakcije zatim odredite koji
nagib opisuje skupinu A, koji skupinu B i zašto zbirni nagib ne opisuje nijednu.

### Računski

Zbirni nagib iznosi `r hr_broj(s16$nagib_jedan, 4)` boda po godini. Izračunajte
modelom predviđenu razliku prosjeka između dobi od 25 i 55 godina, a zatim isti
račun ponovite s prilagođenim nagibom
`r hr_broj(s16$nagib_dva, 4)` uz jednak izvor vijesti. Predajte obje brojke i
objasnite zašto nijedna ne određuje ostvarenu razliku dviju konkretnih osoba.

### Kritički

Vratite se poglavlju o mjerenju i dizajnu radi operacionalizacije i vremenskog
reda te poglavlju o tome kako brojke zavode radi razlike između točne brojke i
preširoke tvrdnje. U prilagođenoj tablici iz okvira odredite što je mjereno,
koja je referentna skupina, koju količinu podupire ćelija 1,60 i koja bi dodatna
količina trebala za tvrdnju o apsolutnoj vjerojatnosti. Zatim preuredite naslov
„Više od tri sata na društvenim mrežama povećava depresiju za 60 %” u jednu
rečenicu koju presječni nacrt i prikazani omjer izgleda doista podupiru.

### Revizija modela

Ocijenite račun i zaključak iz okvira o pogrešci. Imenujte što je u kodu
ispravno i povežite obje prijavljene veličine sa skupom na kojem su dobivene.
Napišite zaključak koji bi isti ispis podnio te opišite provjeru potrebnu za
nove korisnike. Objasnite zašto unaprijed dostupni prediktori sami ne
potvrđuju uspješnost predviđanja na novim podacima.

---

# Statistika u doba algoritama

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/17-doba-algoritama.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-24 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

ParlaSent je skup rečenica iz parlamentarnih rasprava kojima su ljudi označili
ton. Koristimo njegov hrvatski dio kako bismo pratili što
model uči iz takvih oznaka i kako provjeravamo njegove pogreške
(Mochtak, 2023). Jedan redak sadrži jednu rečenicu i njezinu oznaku, a ne
cijeli govor ili mišljenje zastupnika.

„Da li je pošteno da se ukida prethodna stopa i da se povećava u odnosu na
prethodnu?” Tako glasi prvi hrvatski redak nastavne datoteke ParlaSent 1.0.
Jedan ga je koder označio neutralnim uz negativan ton, a drugi negativnim.
Nakon usklađenja zabilježena je oznaka `Negative` (Mochtak, 2023).

Zamislimo da urednički sustav šalje negativno označene rečenice na ljudski
pregled prije mogućeg javnog sažetka. Oznaka se ne objavljuje automatski, ali
određuje koji tekst dobiva dodatnu pozornost. Pogrešno uključivanje može
neopravdano istaknuti rečenicu, a pogrešno izostavljanje sakriti važan dio
govora.

Prije primjene trebamo opravdati zašto negativan ton uopće daje prednost pri
pregledu. To je urednička odluka. Možemo je usporediti sa slučajnim pregledom
ili izborom prema javnoj relevantnosti neovisno o tonu.

Treba li početnu rečenicu poslati na pregled? Najprije trebamo znati što je
jedinica analize, kako je odabrana i označena te tko može osporiti oznaku.

Kod regresije smo razlikovali opis postojećih podataka od predviđanja novih
ishoda. Sada nas zanima što se događa kada predviđanje pokrene postupak prema
nekoj osobi ili tekstu. U zamišljenom uredničkom sustavu iz vinjete
procijenjeni ton odlučuje koja će rečenica dobiti dodatni pregled. Za procjenu
takva sustava trebamo pratiti i nastanak oznake i posljedice pogrešne odluke.

Hrvatski dio ParlaSenta sadrži stvarne parlamentarne rečenice s ljudskim
oznakama tona (Mochtak, 2023). Jedan redak predstavlja rečenicu, a ne
zastupnika ili cijeli govor. Pratit ćemo tekst, dostupne oznake kodera i
podjelu podataka. U nastavnom primjeru iz tih ćemo oznaka izvesti jednostavan
rezultat za usporedbu pravila slanja na pregled. Time provjeravamo kako izbor
praga mijenja odluku. Uspješnost uvježbanoga klasifikatora ovdje ne mjerimo.

U tom se zadatku sastaju ranija pitanja o mjerenju, uzorkovanju i pogreškama.
Ljudska oznaka nije nepogrešiva mjera tona, a odabrani korpus nije automatski
slika svih parlamentarnih rasprava. Razmotrit ćemo zašto podatke razdvajamo za
učenje, provjeru i ispitivanje te kako prilagođavanje poznatim primjerima može
prikriti slabo predviđanje novih. Za svaku procjenu trebamo znati na kojim je
podacima nastala i što je već moglo utjecati na odluke o modelu.

Promjenom praga usporedit ćemo pogrešna uključivanja i propuštanja. U zasebnoj
simulaciji s dvjema skupinama istražit ćemo zašto se mjerila pravednosti mogu
razilaziti kada se razlikuju učestalosti ishoda. ParlaSentu pritom nećemo
pripisivati skupinska obilježja koja u paketu ne postoje. Provjeru ćemo
proširiti na mogućnost osporavanja oznake, odgovornost za postupak i uporabu
jezičnih modela. Umjesto samog postotka točnosti moći ćemo tražiti opis toga
što sustav predviđa, prema kojoj oznaci mjeri uspjeh i tko snosi posljedice.
Te odluke počinju izborom korpusa i jedinice koju sustav razvrstava.

## Odluka, korpus i jedinica

Klasifikator može procijeniti vjerojatnost pripadnosti kategoriji. Institucija
zatim bira prag koji pokreće pregled i određuje daljnje postupanje. Procjena,
odluka i njezine posljedice zasebni su dijelovi sustava.

Predviđanje procjenjujemo na novim podacima, a objašnjenje prema sadržajnom
pitanju, teoriji i nacrtu (Breiman, 2001; Shmueli, 2010). Dobro predviđen ton ne
otkriva namjeru govornika ni uzrok njegova izražavanja.

Naša [tekstna jedinica]{.pojam def="Jedan unaprijed određen komad teksta koji
se zasebno označava i analizira." en="text unit" ch="17"} jest rečenica. Ona
ne predstavlja cijeli govor, osobu ili sjednicu. [Granica korpusa]{.pojam
def="Pravilo koje određuje koji tekstovi mogu ući u analizu, a koji ostaju
izvan nje." en="corpus boundary" ch="17"} ovdje obuhvaća retke ParlaSenta s
oznakom `country = HR`. Paket ne daje govornika, stranku, datum, položaj vlasti ili
oporbe ni poveznicu na cijeli govor.

Nedostajući kontekst ne smijemo nadomjestiti nagađanjem. Izvorni autori
izostavili su moderatorske rečenice i zadržali duljine između prvog i trećeg
kvartila (Mochtak, 2024). Dio za učenje stratificirano su odabrali
prema prisutnosti pozitivnih, negativnih ili nijedne leksikonske riječi.
Ispitni dio odabrali su slučajno, uz iste filtre duljine i moderatora
(Mochtak, 2023; Mochtak, 2024). Zbog takvog odabira udio negativnih
oznaka ne procjenjuje udio negativnog tona u Hrvatskom saboru. Iz rečenice
također ne zaključujemo o osobini ili namjeri govornika.

Nastavna prilagodba ParlaSenta 1.0 sadrži stvarne parlamentarne rečenice s
oznakom zemlje `HR`, pod licencom CC BY-SA 4.0 (Mochtak, 2023). Ima 2.698
redaka. Sve rečenice istog dokumenta zadržane su u jednom izvedenom skupu.

Sljedeća tablica prikazuje broj redaka u svakom skupu. Račun čita pripremljenu
datoteku, pa brojnosti možemo reproducirati.

*Slika. Oznake i brojnosti u nastavnom paketu ParlaSent. Izrada autora prema @mochtak2023.*

Za učenje je izdvojeno 1.090 redaka, za provjeru 272, a za ispitivanje 1.336.
Zadržani su svi izvorni ispitni redci. Iz izvornog dijela za učenje uklonjeno
je 25 redaka iz 20 dokumenata koji su se pojavljivali i u ispitnom dijelu.
Uklanjanje nije ovisilo o oznaci. Koraci i kontrolne sume zapisani su u
podatkovnoj putovnici `data/parlament_tekst/PUTOVNICA.md`. Te brojnosti opisuju nastavni paket.

## Nastanak oznake

Izdvojili smo rečenice koje možemo analizirati, ali njihova oznaka tona još
nije sama po sebi razumljiva. [Okvir kodiranja]{.pojam def="Skup pravila po kojima se tekst pretvara u
kategorije koje analiza rabi." en="coding frame" ch="17"} određuje značenje
oznaka `Negative`, `Neutral` i `Positive`. Dodijeljena oznaka ovisi o uputama,
prosudbi kodera i načinu rješavanja neslaganja.

Izvorni dio za učenje sadrži dvije pojedinačne oznake i usklađenu oznaku. U
ispitnom dijelu dostupna je samo oznaka jednog uvježbanog kodera. Iako oba
dijela imaju stupac `recorded_label`, oznake nisu nastale jednakim postupkom.

**Zabilježeni referentni ishod** jest ishod ili oznaka zapisana određenim
postupkom mjerenja, prema kojoj se vrednuje klasifikator, ali koja može
sadržavati pogrešku.

Neslaganje kodera može upozoriti na nejasan pojam ili teško primjenjivo
pravilo. Drukčije upute ili usklađivanje mogu promijeniti referentnu oznaku.
Time se mijenja i ocjena klasifikatora, čak i ako njegova predviđanja ostanu
ista.

## Tri skupa, dva pitanja

Jedno je pitanje kojim ćemo modelom i pragom razvrstavati rečenice.
Drugo je koliko taj zaključani postupak uspješno radi na novim rečenicama.

U regresiji smo odvojili podatke na kojima ćemo provjeriti predviđanje novih
osoba. Ako sada na izdvojenim podacima biramo model ili prag, i oni utječu na
konačni postupak. Za njegovu završnu provjeru zato trebamo sačuvati još jedan
skup. [Razdvajanje na skup za učenje, provjeru i ispitivanje]{.pojam def="Odvajanje
podataka za prilagodbu modela, izbor postupka i jednu završnu procjenu."
en="train-validation-test split" ch="17"} odvaja tri zadatka. Model
prilagođavamo na učenju, pravilo i prag biramo na provjeri, a završnu
uspješnost jednom procjenjujemo na sačuvanom ispitnom skupu. Ovdje ispitni dio
ima drukčiji odabir i način označavanja, pa ga ne možemo koristiti za izravno
usporedivu završnu provjeru.

Paket razdvaja cijele dokumente. Dokumente iz izvorne ispitne datoteke
uklonili smo iz dijela za učenje, a preostale prema ponovljivom pravilu
podijelili na učenje i provjeru. Tako rečenice istog dokumenta ne prelaze
granice skupova i ne stvaraju privid provjere na neovisnom tekstu.
Takvo preklapanje dokumenata bilo bi još jedan oblik curenja informacija.

[Preprilagodba]{.pojam def="Učenje posebnosti viđenih podataka koje poboljšava
pristajanje njima, ali pogoršava predviđanje novih jedinica." en="overfitting"
ch="17"} nastaje kada model nauči posebnosti viđenih podataka pa njima
bolje pristaje, ali lošije predviđa nove jedinice. Zato ga provjeravamo
na odvojenim jedinicama. Ta provjera
ipak ne stvara reprezentativan uzorak. Populacijski doseg ovisi o odabiru
podataka. Čak ni dobar rezultat na pravilno izdvojenom skupu ne opravdava
prijenos na sve tekstove. Ovdje različit odabir i označavanje ispitnog dijela
dodatno ograničavaju usporedbu.

## Od vjerojatnosti do pravednosti

Uz prag 0,60 rečenica s procjenom 0,59 ne ulazi u pregled, a ona s 0,61 ulazi.
Mala razlika u broju tako mijenja postupanje. Izbor praga treba povezati s
posljedicama obiju vrsta pogreške.

**Klasifikacijski prag** jest unaprijed određena vrijednost koja predviđenu
vjerojatnost pretvara u kategoričku odluku; njegovim se pomicanjem mijenja
odnos vrsta pogrešaka.

Svaka rečenica sada završava među poslanima na pregled ili među
izostavljenima. Tu odluku možemo usporediti s njezinom zabilježenom oznakom,
kao što smo u poglavlju o kategoričkim podacima križali dob i izvor vijesti.
Pozitivna odluka ovdje znači slanje na pregled, a tražena je oznaka negativnog
tona. [Tablica zabune]{.pojam def="Kontingencijska tablica koja križa
klasifikacijsku odluku i zabilježeni referentni ishod." en="confusion matrix"
ch="17"} jest kontingencijska tablica odluka i referentnih oznaka. Stopa lažno
pozitivnih odluka računa se među zabilježenim nenegativnim rečenicama. Stopa
lažno negativnih računa se među zabilježenim negativnima. Pozitivna
prediktivna vrijednost pita koliko je zabilježenih negativnih među svima
poslanima na pregled. Ukupna točnost spaja uspjeh u obje skupine prema
njihovim brojnostima, pa može sakriti neravnomjerno raspoređene pogreške.

Nazivnik određuje značenje svake stope. Osjetljivost, odnosno odziv
(*recall*), računa se kao $TP/(TP+FN)$, a specifičnost kao
$TN/(TN+FP)$. Pozitivna prediktivna vrijednost, u klasifikaciji zvana i
preciznost (*precision*), računa se kao $TP/(TP+FP)$. Točnost
(*accuracy*) jest $(TP+TN)/n$. Kratice TP i TN znače točno pozitivne i
točno negativne odluke, a FP i FN lažno pozitivne i lažno negativne.
Klasifikacijska preciznost zato nije isto što i uski interval procjene.

Brojeve ćemo u razrađenom primjeru dobiti prebrojavanjem ljudskih glasova,
a ne provjerom gotovoga algoritma. Za prag od barem jednoga negativnog
glasa tablica daje $TP=122$, $FP=16$, $FN=0$ i $TN=134$.
Osjetljivost je $122/122$, specifičnost $134/150$, pozitivna prediktivna
vrijednost $122/138$, a točnost $256/272$. Ti različiti nazivnici
objašnjavaju zašto jedan postotak ne može opisati cijelu odluku.
Lažna uzbuna podsjeća na pogrešku prve vrste iz testiranja, ali ovdje
brojimo odluke prema referentnoj oznaci pojedinih rečenica, a ne
odbacivanja statističke hipoteze kroz ponovljene uzorke.

Temeljna stopa ovdje je udio zabilježenih negativnih ishoda prije odluke
modela. Ako se razlikuje među skupinama, jednake stope lažno pozitivnih i
lažno negativnih odluka mogu dati različite pozitivne prediktivne vrijednosti.
Zato se neka poželjna mjerila pravednosti ne mogu uvijek istodobno izjednačiti
(Chouldechova, 2017; Barocas, 2023). Uz broj pogrešaka trebamo razmotriti i
njihove posljedice.

Za [pogreške po podskupinama]{.pojam def="Odvojeni prikaz vrsta pogreške
unutar unaprijed smislenih skupina." en="subgroup errors" ch="17"} trebamo
pouzdanu skupnu varijablu. Nastavni paket takve podatke nema. Ne izvodimo ih
nagađanjem iz teksta ili imena. Zato za prikaz koristimo izmišljene skupine A
i B, a empirijski primjer ostaje bez podskupinske analize. To ograničenje ne
dokazuje da su pogreške pravedno raspoređene.

[Algoritamska pravednost]{.pojam def="Ocjena raspodjele koristi, pogrešaka i
mogućnosti osporavanja u cijelom sustavu odluke." en="algorithmic fairness"
ch="17"} zahtijeva više od jedne stope. Uz nazivnike i posljedice pogrešaka
razmatramo obavijest, obrazloženje te mogućnost prigovora i žalbe.

## Interakcija — Istraživač pravednosti

Za ovaj pokus zadajemo referentne ishode 0 i 1, ne ton stvarnih rečenica.
Za ishod 0 generiramo 6.000 rezultata iz normalne raspodjele sa sredinom
0,30 i standardnom devijacijom 0,18, a za ishod 1 drugih 6.000 sa sredinom
0,70 i istom standardnom devijacijom. Vrijednosti ispod nule zamjenjujemo
nulom, a iznad jedan jedinicom. Tako dobiveni brojevi služe razvrstavanju,
bez pretpostavke da su kalibrirane vjerojatnosti. Kalibracija iz poglavlja
o vjerojatnosti tražila bi slaganje najavljenih izgleda s učestalošću ishoda
među usporedivim prognozama. Ovdje to nismo provjerili.

Pri pragu 0,60 rezultat 0,65 vodi pozitivnoj odluci. Ako je referentni ishod
0, taj zapis ulazi u brojnik lažno pozitivnih. Taj broj dijelimo sa svih
6.000 zapisa ishoda 0. Analogno među 6.000 zapisa ishoda 1 brojimo rezultate
ispod praga za stopu lažno negativnih. Sve vrijednosti zadržavamo, uključujući
one ograničene na nulu i jedan.

Skupine A i B zatim slažemo ponderiranjem istih dviju uvjetnih raspodjela,
u prikazanoj postavci s udjelima ishoda 1 od 20 % i 45 %. Ne izvlačimo nove
osobe za svaku skupinu. Primjerice, u A udio točno pozitivnih među svima
iznosi $0,20(1-\text{stopa lažno negativnih})$, a udio lažno pozitivnih
$0,80 \times \text{stopa lažno pozitivnih}$. Njihov zbroj nazivnik je
pozitivne prediktivne vrijednosti. U B mijenjaju se težine u 0,45 i 0,55.
Uvjetne stope zato su u prikazu točno jednake po konstrukciji. Novi niz
simuliranih rezultata malo bi promijenio njihove vrijednosti.

Na slici uspoređujemo dvije simulirane skupine s različitim temeljnim stopama.
Za isti referentni ishod raspodjele rezultata jednake su u obje skupine.
Zajednički prag zato može dati jednake uvjetne stope pogreške, ali različitu
točnost i prediktivnu vrijednost. Prikaz ne opisuje ParlaSent ni stvarne
skupine ljudi.

Rezultat se učitava.

*Slika. Istraživač pravednosti — četiri mjerila po skupini pri zajedničkom klasifikacijskom pragu.*

**Što isprobati.**

1. Postavite obje temeljne stope na 20 % i usporedite sva četiri mjerila.
2. Vratite skupinu B na 45 % te pronađite mjerila koja se razilaze iako je
   prag zajednički.
3. Pomaknite prag prema 0,30 pa prema 0,70 i provjerite može li jedno
   podešenje istodobno smanjiti obje vrste pogreške.

Kada su jednake i temeljne stope, sva četiri mjerila poklapaju se. Kada
temeljne stope promijenimo, razlikuju se pozitivna prediktivna vrijednost i
točnost, iako uvjetne stope pogreške ostaju jednake. Prikaz objašnjava
matematički odnos koji smo susreli u poglavlju o zavaravajućim brojkama. Sam
ne dokazuje nejednako postupanje u stvarnom sustavu.

## Osporiva oznaka i postupak

U simulaciji smo točno znali koji je referentni ishod. Vratimo se sada početnoj
rečenici, čija je oznaka nastala ljudskom prosudbom. Nakon usklađenja nosi
negativnu oznaku, dok je prvi koder odabrao neutralnu kategoriju s negativnim
tonom. Trebamo pregledati upute i obrazloženje te procijeniti bi li drugo
opravdano pravilo dalo drukčiji rezultat. Takva provjera može dovesti do
ispravka reference prema kojoj ocjenjujemo odluke.

Osoba koja pregledava rečenicu treba vidjeti izvorni tekst, pravilo i razlog
slanja na pregled. Treba moći zabilježiti obrazloženje i osporiti oznaku. Ako
odluka utječe na govornika ili javni prikaz njegova govora, potreban je i
postupak obavijesti i žalbe. Paket bez identiteta govornika to sam ne
omogućuje. Ljudski pregled također treba jasne upute, odgovornost i nadzor.

Promjena referentne oznake mijenja ćelije tablice zabune. Prethodno lažno
pozitivna odluka može postati točno pozitivna bez promjene predviđanja. Zato
čuvamo inačicu kodnih pravila, datum i razlog ispravka. Samo tako možemo
uspoređivati mjerila kroz vrijeme.

U primjeni pratimo i podatke, prag, sučelje, pregled, prigovore i daljnje
učenje. Ako nove oznake dobivaju samo pregledane rečenice, sustav uči uglavnom
iz teksta koji je već odabrao. Pogreške među izostavljenim rečenicama teže će
biti otkrivene.

Tako nastaje povratna sprega između odluka i budućih podataka. Slično je kod
preporuka. Rangiranje određuje što korisnici vide, a njihovo ponašanje postaje
podatak za novo rangiranje. Vrijeme zadržavanja pritom ne mjeri automatski
zadovoljstvo, informiranost ni javnu vrijednost (Barocas, 2023).

[Pomak distribucije]{.pojam def="Promjena odnosa u novim podatcima zbog koje
stara procjena uspješnosti više ne opisuje sadašnji rad sustava."
en="distribution shift" ch="17"} može nastati zbog novih tema, jezika, odabira
tekstova ili načina označavanja. Nakon primjene pratimo pregledane i
nepregledane tekstove, sporne oznake, vrijeme ispravka i promjene korpusa. Za
procjenu lažno negativnih odluka trebamo zasebno i usporedivo označiti
slučajni ili unaprijed stratificirani uzorak nepregledanih rečenica. Ranija
uspješnost ne jamči trajno dobar rad ni valjano mjerenje tona.

## Jezični modeli kao sustavi predikcije

I asistent kojim se služimo proizvodi predviđanja. [Jezični model kao sustav
predikcije]{.pojam def="Sustav koji iz prethodnoga teksta procjenjuje
vjerojatne nastavke i iz njih proizvodi novi tekst." en="language model as a
prediction system" ch="17"} možemo razumjeti na primjeru autoregresivnog GPT-3
iz 2020., koji generira nastavke uvjetovane prethodnim tekstom (Brown, 2020).
Tečan odgovor zato ne potvrđuje izvor, brojku ni zaključak. Predviđanje teksta
samo po sebi ne daje ni uzročno objašnjenje odgovora.

U odgovoru asistenta provjeravamo podatke, jedinicu, planiranu odluku i
način otkrivanja pogreške. Asistent može predložiti račun ili tablicu. Ne smije
nadomjestiti nedostajuća predviđanja izmišljenim stupcem, nagađati kontekst
ili tretirati referentnu oznaku kao nepogrešivu.

Odnos temeljnih stopa i mjerila susrećemo i u drugim primjenama klasifikacije.

**Statistika u divljini.**
**Jednaka ocjena, različite pogreške.** Procjena da je osoba
visokorizična može utjecati na odluku koja se na nju odnosi.
Chouldechova je u istraživanju instrumenata za procjenu
ponavljanja kaznenog djela razmotrila kako različita mjerila
pravednosti mogu dati različite ocjene istog sustava
(Chouldechova, 2017). Spor se ne može riješiti samo podatkom
da je model ukupno dovoljno točan.

Jedan zahtjev polazi od značenja ocjene. Među ljudima s
jednakom ocjenom rizika zabilježeni bi ishod trebao biti
podjednako čest u različitim skupinama. Drugi zahtjev
polazi od pogrešno označenih ljudi. Među onima kod kojih
ishod nije zabilježen želimo usporediti koliko ih je ipak
označeno visokorizičnima. Ti zahtjevi koriste različite
nazivnike, pa jednakost prema jednome ne jamči jednakost
prema drugome.

Za cijelu skupinu označenu visokorizičnom možemo tražiti
jednak udio zabilježenih pozitivnih ishoda. Chouldechova
je pokazala zašto taj zahtjev pri različitim temeljnim
stopama u pravilu dolazi u sukob s jednakošću obiju stopa
pogreške (Chouldechova, 2017). Takav sukob ne javlja se
kod savršenog predviđanja, ali njega ne možemo
pretpostaviti u stvarnoj primjeni.
Taj matematički nalaz ne određuje koju bi pogrešku društvo
trebalo smatrati prihvatljivom niti opravdava njezine
posljedice za osobu.

Zato bi prije uporabe takve procjene trebalo razjasniti
što referentni ishod bilježi, kome pogrešna oznaka šteti
i kako se odluka može osporiti. Promjena praga može
promijeniti raspored pogrešaka, ali ne može sama dati
odgovor na ta pitanja. Ni dobro slaganje s postojećim
zapisima ne potvrđuje da oni potpuno opisuju pojavu
koju želimo procjenjivati.

U našem parlamentarnom primjeru posljedice i jedinice
drukčije su. Pogrešno uključena rečenica dobiva dodatni
pregled, a pogrešno izostavljena ostaje izvan njega.
Kaznenopravne skupine i njihove temeljne stope ne
prenosimo u taj korpus. Prenosimo način postavljanja
pitanja. Tvrdnja da je sustav pravedan treba imenovati
ishod, skupine, prag i pogrešku čije posljedice
procjenjujemo. Bez toga jednaka ocjena modela može
prikrivati različita iskustva ljudi na koje se odnosi.

Plan vrednovanja treba odrediti što će se provjeravati i koju će odluku
dobiveni rezultat poduprijeti. Sljedeći prijedlog povezuje te dvije zadaće.

**Nađite grešku.**
Tim priprema plan vrednovanja klasifikatora parlamentarnih rečenica.
U nastavnom paketu ParlaSent rečenice su razdvojene po dokumentima.
Izvorni dio za učenje ima dvije pojedinačne i usklađenu oznaku, dok
ispitni dio ima oznaku jednog uvježbanog kodera
(Mochtak, 2023; Mochtak, 2024). To su dva različita puta nastanka
oznake koje smo već upoznali.

Predloženi plan predviđa zaključavanje modela i praga prije otvaranja
ispitnog skupa. Točnost bi se računala kao udio predviđanja koja se
podudaraju sa zabilježenim oznakama. Tim još nije proveo tu provjeru ni
neovisno ponovno kodiranje ispitnih rečenica. Asistent je predložio
rečenicu za plan.

> Izdvojeni skup omogućit će provjeru slaganja predviđanja sa
> zabilježenim oznakama, uz ograničenja odabira i različitog kodiranja.
> Ako model na njemu postigne visoku točnost, time ćemo dokazati da
> ispravno mjeri ton rečenica.

Uredite plan tako da jasno kaže što će se tom provjerom doznati.
Navedite jednu dodatnu provjeru mjerenja i objasnite što bi ona mogla
otkriti čak i kada bi podudarnost modela s postojećim oznakama bila
visoka. Ne pripisujte klasifikatoru rezultat koji još nije izmjeren.

## Razrađeni primjer

Neslaganje kodera iz početne rečenice sada pretvaramo u pitanje o pravilu
pregleda. Je li dovoljan jedan negativan glas ili ćemo zahtijevati oba?
Usporedbu provodimo samo na 272 retka skupa za provjeru, s dvije pojedinačne i
usklađenom oznakom. Iz glasova kodera računamo rezultat 0, 0,5 ili 1. Oznake
`Negative` i `M_Negative` računamo kao negativne, a `Positive`,
`M_Positive`, `N_Neutral` i `P_Neutral` kao nenegativne. Ta nastavna
podjela zahtijeva provjeru osjetljivosti. Rezultat nije vjerojatnost
klasifikatora ni neovisno predviđanje. Usklađena referenca nastala je iz istih
ulaza, pa primjer pokazuje kako način označavanja oblikuje mjerila.

To objašnjava i nulu u ćeliji lažno negativnih pri blažem pravilu. Svaka
referentno negativna rečenica u ovom paketu ima barem jedan negativan glas.
Nula stoga proizlazi iz odnosa glasova i njihove usklađene oznake, a nije
dokaz savršenog prepoznavanja novih rečenica. Pri strožem pravilu postoji
jedna rečenica s dva negativna glasa i nenegativnom usklađenom oznakom,
`train-2089`. To je stvarno neslaganje zapisa, koje čuvamo vidljivim.

Od svih 2.698 zapisa sada zadržavamo samo 272 s oznakom `provjera`, bez
daljnjeg izostavljanja. Za mali prikaz namjerno biramo prvi redak sa svakom
od triju mogućih vrijednosti glasovanja. Broj retka odnosi se na cijelu
nastavnu datoteku, pa se zapis može ponovno pronaći.

*Slika. Tri odabrana koderska zapisa prije tablice zabune. Izrada autora prema @mochtak2023.*

Dva negativna glasa daju $(1+1)/2 = 1$, a jedan $(1+0)/2 = 0,5$.
U svakom retku odluku uspoređujemo s referencom. Slanje uz negativnu
referencu dodaje jedan točno pozitivnima, a slanje uz nenegativnu jedan
lažno pozitivnima. Neslanje analogno puni preostale dvije ćelije. Tako
prebrojavamo svih 272 zapisa, bez procjene klasifikatora.

Prvo pravilo postavlja prag na 0,5, pa rečenica ulazi na pregled ako je barem
jedan koder dao negativan glas. Taj prag primjenjujemo na glasove, za razliku
od ranijeg praga modelom predviđene vjerojatnosti. Poziv `mutate()` donosi
odluku za svaki redak, a `count()` zatim prebroji njezine kombinacije s
referentnom oznakom u četiri ćelije tablice.

Brojanja pri prvom pragu možemo pročitati kao običnu kontingencijsku
tablicu. Njezini se redci odnose na referentnu oznaku, a stupci na odluku.

| Referentna oznaka | Poslano na pregled | Nije poslano | Ukupno |
|---|---:|---:|---:|
| negativna | 122 | 0 | 122 |
| nenegativna | 16 | 134 | 150 |
| ukupno | 138 | 134 | 272 |

: Brojanja za prag 0,5 na istom skupu za provjeru. Izrada autora prema mochtak2023.

Stopa lažno pozitivnih je $16/150$, a pozitivna prediktivna vrijednost
$122/138$. Ista ćelija zato može sudjelovati u različitim pitanjima, uz
drukčiji nazivnik.

Da bismo vidjeli što traženje suglasnosti obaju kodera mijenja, na iste
rečenice primjenjujemo i prag 1. Sljedeća tablica uspoređuje ga s pragom 0,5,
uz isti zabilježeni referentni ishod. Sve su vrijednosti izračunate iz
pripremljenog paketa.

*Slika. Dvije odluke o ljudskom pregledu prema istom zabilježenom referentnom ishodu u skupu za provjeru. Izrada autora prema @mochtak2023.*

U tablici prve četiri brojnosti koriste upravo definirane kratice, a
sljedeća tri retka pokazuju nazivnike stopa. Posljednji redak daje ukupnu
točnost, udio ispravnih odluka među svim rečenicama. Jedna lažno pozitivna odluka
pri strožem pragu znači $1/150$, odnosno 0,7 %. Još jedna takva odluka
udvostručila bi taj postotak. Taj mali broj ne opravdava preciznu tvrdnju
o stopi u budućim tekstovima.

Pri nižem pragu na pregled ulaze sve 122 rečenice sa zabilježenim negativnim
ishodom i 16 od 150 nenegativnih. Stopa lažno pozitivnih odluka iznosi 10,7 %,
a lažno negativnih 0,0 %. Pri strožem pragu izostaju 22 od 122 negativne
rečenice, a ulazi jedna od 150 nenegativnih. Stope tada iznose 0,7 % i 18,0 %.

Za izbor pravila trebamo znati kapacitet pregleda, posljedice nepotrebnog
uključivanja i izostavljanja te mogućnost prigovora. Prije toga uredništvo
mora opravdati izbor negativnog tona kao kriterija. Treba ga usporediti sa
slučajnim pregledom ili kriterijem relevantnosti. Tablica pokazuje posljedice
praga, ali ne donosi tu odluku umjesto uredništva.

U ispitnom dijelu nemamo drugog kodera ni usklađenje, pa pravilo dvaju glasova
ne možemo jednako primijeniti i ocijeniti. Završnu uspješnost zato ne
izvještavamo. Za budući klasifikator trebali bismo unaprijed zaključati model,
prag i usporediv referentni postupak, spremiti predviđanja i jednom provesti
završnu provjeru. Ovdje provjeravamo podatke i pravilo odluke, bez tvrdnje o
izvedbi modela koji nije izgrađen.

Sada znamo zašto je oznaka početne rečenice sporna i što bi značilo
uključivanje u pregled. Još ne znamo namjeru govornika. Odluku treba vezati uz
izvorni tekst, obrazloženje, mogućnost ispravka i praćenje posljedica praga.

## Od modela do odluke

U tablici provjeravamo jedinicu i obuhvat podataka, vrstu tvrdnje,
nesigurnost, alternative i osobe na koje odluka može utjecati. Tako određujemo
doseg ovog primjera.

| Revizijsko pitanje | Primjena na odluku o ljudskom pregledu |
|---|---|
| Koja je jedinica? | jedna odabrana parlamentarna rečenica s putom nastanka zabilježene oznake, ne govor, govornik ili sjednica |
| Tko ili što nedostaje? | rečenice moderatora i rečenice izvan srednjega raspona duljine isključene su uzvodno; paket nema govornika, cijeli govor ni obranjivu skupnu varijablu |
| Koji je cilj tvrdnje? | tablica uspoređuje dva pravila slanja u pregled prema zabilježenom negativnom ishodu; riječ je o opisu i provjeri odluke, ne izvedbi postojećega klasifikatora |
| Gdje je neizvjesnost? | osjetljivost na prag; ne provjeravamo reprezentativnost, valjanost oznake, pogrešku kodiranja ni budući pomak distribucije |
| Koje drugo objašnjenje ostaje? | stroži prag mijenja pogreške; slučajni pregled ili kriterij relevantnosti mijenjaju i cilj odabira |
| Tko snosi posljedice? | pregledavatelji troše vrijeme, važan tekst može izostati, a govornik i javnost mogu dobiti iskrivljen prikaz |

: Šest revizijskih pitanja za odluku o ljudskom pregledu. Izrada autora prema Mochtak, 2023 i mochtakparlasent2024.

Sljedeća tablica razlikuje šest vrsta tvrdnji. Svaka traži odgovarajuće dokaze, pa
analiza ne mora niti može odgovoriti na sve.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje brojnosti, put oznake i posljedice dvaju pravila unutar pripremljenoga paketa |
| povezanost | pokazuje povezanost dvaju koderskih glasova s usklađenom oznakom, uz izričitu ovisnost jer su isti glasovi sudjelovali u njezinu nastanku |
| generalizacija | ne podupire prijenos na sav parlamentarni govor, govornike ili tekstove izvan odabranih rečenica |
| predviđanje | ne ocjenjuje postojeći model; buduća bi procjena tražila zaključan model, prag, usporediv referentni postupak i jedan izdvojeni ispitni skup |
| uzročnost | ne pokazuje što uzrokuje ton, uredničku važnost ili bilo koju posljedicu za govornika |
| odluka | podupire provjeru tereta dvaju pragova, ali ne dokazuje da je negativan sentiment legitiman cilj usmjeravanja pozornosti |

: Šest dimenzija tvrdnje na završetku dijela o modelima. Izrada autora prema mochtak2023.

Zašto razdvajanje na skup za učenje, provjeru i ispitivanje ne stvara
populacijsku reprezentativnost? Kako izbor rečenica i način njihova označavanja ograničavaju ono što možemo
zaključiti iz tablice zabune? Zašto jednake uvjetne stope
pogreške ne jamče jednaku pozitivnu prediktivnu vrijednost? Nakon primjene
sustava, koje rečenice moramo dodatno pregledati da bismo mogli procijeniti
koliko je negativnih slučajeva sustav propustio?

U završnom poglavlju sastavit ćemo vlastiti istraživački protokol. U njega
uključujemo pragove odluke, posljedice pogreške, nadzor i prigovor. Asistentu
možemo povjeriti račun i provjeru dosljednosti, dok cilj, prosudba dokaza i
odgovornost za zaključak ostaju naši.

Zaštitu osoba povezujemo s pravilima iz poglavlja o mjerenju i dizajnu.
Javna dostupnost zapisa sama ne uklanja mogućnost identifikacije ni štetu
od njegova povezivanja s drugim podacima. Prije dijeljenja provjeravamo
svrhu, nužnost pojedinih obilježja i prikladnost alata za osjetljivost
podataka. Pravila određenoga kolegija dodatni su uvjet u toj nastavi,
a nisu univerzalna zamjena za odgovornost prema sudionicima.

## Sažetak

Ocjenu algoritma počinjemo pitanjem što model može naučiti iz odabranih
podataka i što možemo provjeriti prema referentnim oznakama. Odvajanje skupova pomaže provjeri
predviđanja, ali samo ne stvara reprezentativnost ni valjano mjerenje. Kada
rezultat pretvorimo u odluku, prag mijenja raspodjelu pogrešaka, a različite
temeljne stope mogu dovesti mjerila pravednosti u sukob. Nakon primjene ostajemo odgovorni za pregled, ispravke, prigovor i nadzor,
uključujući provjeru izostavljenih slučajeva. Izvore i zaključke provjeravamo i u odgovoru jezičnog modela, koliko god bio
tečan.

## Pojmovi

osjetljivost klasifikatora (*sensitivity*), specifičnost (*specificity*),
preciznost odnosno pozitivna prediktivna vrijednost (*precision; positive predictive value*),
ukupna točnost (*accuracy*),

tekstna jedinica (*text unit*), granica korpusa (*corpus boundary*), okvir
kodiranja (*coding frame*), zabilježeni referentni ishod (*recorded reference
outcome*), razdvajanje na skup za učenje, provjeru i ispitivanje
(*train-validation-test split*), preprilagodba (*overfitting*), klasifikacijski
prag (*classification threshold*), tablica zabune (*confusion matrix*),
pogreške po podskupinama (*subgroup errors*), algoritamska pravednost
(*algorithmic fairness*), pomak distribucije (*distribution shift*), jezični
model kao sustav predikcije (*language model as a prediction system*)

## Zadaci

### Konceptualni

Objasnite kako razdvajanje na skup za učenje, provjeru i ispitivanje otkriva
preprilagodbu te zašto dokument koji prijeđe među skupovima stvara curenje
informacija. Zatim povežite tablicu zabune s kontingencijskom tablicom iz
poglavlja o kategoričkim podatcima i objasnite zašto predviđena vjerojatnost iz
poglavlja o regresiji još nije odluka. Imenujte oba uvjetna nazivnika pogreške.

### Računski

U pripremljenoj tablici odluka nalazi se 90 točno pozitivnih, 30 lažno
pozitivnih, 10 lažno negativnih i 170 točno negativnih slučajeva. Izračunajte
stopu lažno pozitivnih odluka, stopu lažno negativnih odluka, pozitivnu
prediktivnu vrijednost i točnost. Uz svaki rezultat napišite njegov nazivnik i
jednu moguću posljedicu za red ljudskoga pregleda.

### Kritički

Osporite zabilježenu oznaku početne rečenice. Napišite koje biste dijelove
okvira kodiranja, izvornih oznaka i usklađenja trebali vidjeti prije odluke.
Zatim objasnite zašto promjena oznake može promijeniti mjerila pravednosti bez
ijedne promjene modela.

### Revizija modela

Ocijenite tvrdnju iz okvira o pogrešci. Navedite jednu prihvatljivu tvrdnju,
jedan pogrešan prijelaz i dokaz koji pokazuje razliku. Zatim u sažetom odgovoru revidirajte tvrdnju tako da obuhvati jedinicu, granicu korpusa, put
oznake, curenje, prag, dostupne podskupine, pomak distribucije te postupak
obavijesti, prigovora i žalbe. Objasnite zašto tečan odgovor jezičnoga modela
ne dokazuje nijednu nedostupnu sastavnicu.
