# DIO IV: ZAKLJUČIVANJE

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Paket poglavlja ovog dijela knjige za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE


---

# Logika testiranja

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/10-logika-testiranja.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Šaljete prijavu za prvi posao i čekate odgovor. Ako poziv izostane,
teško možete znati je li presudilo iskustvo, obrazovanje ili nešto što
poslodavac zaključuje već iz vašeg imena. Vlastita prijava pokazuje samo
jedan ishod. Ne možete vidjeti što bi se dogodilo s drukčijim imenom na
usporedivu životopisu.

U terenskom pokusu u Bostonu i Chicagu istraživači su na oglase za posao
slali izmišljene životopise. Nasumično su im dodjeljivali imena
odabrana da zvuče bjelački ili afroamerički,
a zatim bilježili pozive na razgovor (Bertrand, 2004). Tako su mogli
usporediti reakcije poslodavaca na nasumično dodijeljen signal
percipirane rasne pripadnosti (Bertrand, 2004).

Ako jednoj skupini prijava stigne više poziva, koliko bi takva razlika
bila uvjerljiv dokaz da je ime utjecalo na odgovor?

Procjena s intervalom već nam govori koliku smo razliku našli i koliko smo je
precizno odredili. U istraživačkim izvještajima uz nju često stoji i
p-vrijednost. Da bismo taj broj mogli pročitati, trebamo promijeniti pitanje.
Umjesto traženja raspona za nepoznatu veličinu, pitat ćemo kakve bi rezultate
proizvodio određeni model u kojem nema povezanosti koju istražujemo.

Pitanje iz pokusa odnosi se na razliku udjela poziva. Logiku usporedbe s
nultim modelom najprije ćemo pratiti na poznatim simuliranim podacima,
gdje možemo vidjeti svaki korak premještanja oznaka.
Pri procjeni povjerenja promatrali smo populaciju kao cjelinu. Sada nas zanima
koliko se prosječno povjerenje razlikuje između čitatelja tiska i portala te
koliko je ta procjena nesigurna.

Uzorak od 300 čitatelja tiska i portala izvlačimo zasebno iz nastavne
populacije `populacija_medija`, nakon ograničavanja na ta dva izvora. Svaki
redak predstavlja zamišljenu osobu s izvorom vijesti i povjerenjem na ljestvici
od jedan do deset, bez tvrdnje o stvarnim stanovnicima. Najprije ćemo
prikazati razliku i njezin interval. Potom ćemo pretpostaviti jednaku
raspodjelu povjerenja među skupinama i provjeriti što bismo očekivali kada
oznake izvora ne bi bile povezane s odgovorima.

I u ovoj usporedbi ponavljamo postupak, ali drukčije nego pri uzorkovanju
ili bootstrapu. Ocjene ostaju zabilježene, a oznake skupina
nasumično premještamo među osobama. Svaki takav raspored daje novu razliku. Iz
njihove raspodjele možemo procijeniti koliko su česta odstupanja barem toliko
velika kao opaženo, uz pretpostavke koje dopuštaju premještanje. Tek nakon te
provjere imenovat ćemo nultu hipotezu, testnu statistiku i p-vrijednost.

Odluka na temelju testa može biti pogrešna na dva načina. Možemo prijaviti
razliku koje nema ili propustiti razliku koja postoji. Prag odluke utječe na
obje mogućnosti, a neodbacivanje hipoteze ne potvrđuje njezinu istinitost.
Pitanje o vjerojatnosti hipoteze zahtijeva drugi račun i dodatne
pretpostavke, kakve ćemo upoznati u kratkoj usporedbi s Bayesovim pristupom.
Pri čitanju nalaza zato odvajamo ono što test kaže o podacima od procjene
veličine razlike, njezine važnosti i mogućeg uzroka.

## Sudnica i njezina asimetrija

Prije testa trebamo prikazati veličinu opažene razlike i njezinu nesigurnost.
Trebamo razmotriti i posljedice pogrešne odluke. Hoće li veći problem biti
prijaviti razliku koje nema ili propustiti onu koja postoji? Ta pitanja
određuju kako ćemo koristiti rezultat.

Usporedba podataka s početnom pretpostavkom ima sličnost sa suđenjem. Dokazi se procjenjuju u odnosu na
pretpostavku nevinosti. Ako optužba nije dokazana, time ne mora biti dokazana
nevinost. Slično vrijedi za test. Kada nemamo dovoljno dokaza za odbacivanje
početne hipoteze, još nismo pokazali da je ona istinita.

Usporedba sa suđenjem ima granice. Statističke stope pogreške opisuju kako bi
se postupak ponašao kroz mnogo ponavljanja. One nisu vjerojatnosti da je
odluka u pojedinom istraživanju pogrešna.

Zato prije uvida u podatke zapisujemo nulti model, mjeru odstupanja i prag
odluke. Za tako određen postupak možemo procijeniti stopu pogreške. Ako
postupak prilagođavamo dobivenim rezultatima, ta stopa više nije zajamčena.
Posljedice takvih prilagodbi razmotrit ćemo u poglavlju o krizi i obnovi.

## Kako se gradi svijet bez učinka

Uzorak od 300 čitatelja tiska i portala zadržava izvorne oznake skupina.
Njihove ocjene povjerenja najprije čitamo prije bilo kakva premještanja.

Odabir smo najprije ograničili na osobe kojima je glavni izvor tisak ili
portal, a iz njih izabrali 300 zapisa bez vraćanja. Druge izvore nismo
prekodirali u te dvije skupine. U uzorku je `r sum(s10_skupina == "tisak")`
čitatelja tiska i `r sum(s10_skupina == "portal")` korisnika portala.
Ocjene zbrajamo zasebno i dijelimo odgovarajućim brojem osoba.

*Slika. Od ocjena do dviju sredina u istom uzorku. Izrada autora.*

Od sredine za tisak oduzimamo sredinu za portal. Račun zadržava izvorni raspored opažanja, pa razlika opisuje upravo te skupine.

Najprije navodimo procjenu. Čitatelji tiska imaju u prosjeku `r hr_broj(s10$razlika, 2)` boda
više povjerenja, uz interval pouzdanosti od `r hr_broj(s10$donja, 2)` do `r hr_broj(s10$gornja, 2)`. Testom
ćemo zatim provjeriti koliko su podaci uskladivi s određenim modelom bez
razlike.

Taj 95-postotni interval koristimo kao normalnu približnu procjenu za
razliku neovisnih sredina. Standardnu pogrešku računamo kao
$\sqrt{s_T^2/n_T+s_P^2/n_P}$, gdje su $s_T$ i $s_P$ uzoračke standardne
devijacije tiska i portala, a $n_T$ i $n_P$ njihove brojnosti. Razlici
dodajemo i od nje oduzimamo $1,96$ standardnih pogrešaka. Račun traži
neovisne osobe i dovoljno stabilnu približno normalnu raspodjelu razlike.
Interval se temelji na tom približnom računu standardne pogreške. Premještanje oznaka upotrijebit ćemo za test. Za manje uzorke poglavlje
o dvjema grupama razvija t-prilagodbu i Welchove stupnjeve slobode.

Pretpostavimo da je cijela raspodjela povjerenja jednaka među čitateljima
tiska i portala. Pod tom pretpostavkom oznake izvora vijesti zamjenjive su u
odnosu na ishod. Možemo ih nasumično premjestiti među osobama, ponovno
izračunati razliku sredina i to ponoviti mnogo puta. Dobivene razlike pokazuju
što bismo mogli očekivati pod modelom u kojem oznaka nije povezana s ishodom.

U tablici je prvih šest osoba iz uzorka od 300 čitatelja tiska i portala prije i nakon prvoga
nasumičnog preslagivanja svih 300 oznaka. Ocjena prvog retka ostaje
`r s10_ishod[1]`, a uz nju sada stoji oznaka
„`r s10_prva_permutacija[1]`”. Za novi račun grupiramo ocjene prema desnom
stupcu, pa se mijenjaju skupni zbrojevi, ali ne ukupan zbroj ocjena ni
brojnost tiska i portala.

*Slika. Početak istih zapisa prije i nakon jedne permutacije oznaka. Izrada autora.*

Iz svih 300 redaka nakon toga preslagivanja dobivamo razliku
`r hr_broj(s10_nulte[1], 3)` boda. To je jedna vrijednost nulte raspodjele.
Za sljedeću ponovno preslažemo isti skup oznaka uz iste ocjene.

Početnu pretpostavku sada možemo imenovati.

**Nulta hipoteza** je precizan model postupka koji je proizveo podatke, sastavljen
tako da u njemu nema razlike ni veze koju istražujemo.

Alternativna hipoteza ovdje obuhvaća odstupanja od nultog modela. Nulti model
daje raspodjelu s kojom uspoređujemo opaženi rezultat. Test stoga ne računa
koja je od dviju hipoteza vjerojatnija.

Takvo nasumično premještanje oznaka čini osnovu **permutacijskog testa**.

Nulti model ovog postupka pretpostavlja jednakost cijelih raspodjela, uključujući njihove sredine, raspršenosti i oblike. Pretpostavljamo i da su osobe neovisne jedinice
opažanja. Izvor vijesti nije nasumično dodijeljen, pa zamjenjivost oznaka
ovdje prihvaćamo kao pretpostavku modela. Iz rezultata ne možemo zaključiti da
čitanje određenog izvora uzrokuje povjerenje.

Da bismo usporedili izvorni i premještene rasporede, trebamo isti sažetak za
svaki od njih. Taj broj treba pratiti upravo odstupanje koje nas zanima.

**Testna statistika** je jedan broj izračunat iz podataka koji sažima odstupanje
od nultog modela u obliku usporedivom s odstupanjima koja taj model proizvodi.

Kao testnu statistiku koristimo razliku sredina. Zanimaju nas oba smjera, pa
uspoređujemo apsolutnu opaženu razliku s apsolutnim razlikama nakon
premještanja. Ova jednostavna permutacija ispituje opisani model jednakosti cijelih raspodjela, koji uključuje i njihove oblike i raspršenosti. Slika prikazuje razlike iz
četiri tisuće premještanja i razliku iz izvornog rasporeda oznaka.

*Slika. Razlike sredina kroz četiri tisuće nasumičnih premještanja oznaka skupine, uz okomitu crtu na razlici opaženoj u uzorku. Izrada autora. Podaci i postupak opisani su u tekstu.*

Nulta raspodjela ima sredinu u nuli i standardnu devijaciju od `r hr_broj(s10$sd_nulte, 2)` boda.
U 95 % premještanja apsolutna razlika ne prelazi `r hr_broj(s10$granica, 2)` boda. Opažena
razlika od `r hr_broj(s10$razlika, 2)` boda veća je od te granice.

Prebrojimo sada premještanja u kojima je apsolutna razlika barem toliko velika
kao opažena. Njihov udio koristimo za procjenu p-vrijednosti.

**P-vrijednost** je udio rezultata koje nulti model proizvodi, a koji su s njime
u najmanju ruku jednako neusklađeni kao opaženi rezultat.

U 4 000 preslagivanja nalazimo
`r sum(abs(s10_nulte) >= abs(s10_razlika))` apsolutnih razlika barem
toliko velikih kao opažena. Dodavanjem izvornog rasporeda brojniku i
nazivniku račun postaje
$(`r sum(abs(s10_nulte) >= abs(s10_razlika))` + 1)/(4\,000 + 1)$.
Sva su preslagivanja valjana jer se brojnost obiju skupina čuva.

U uzorku od 300 čitatelja tiska i portala p-vrijednost iznosi `r hr_broj(s10$p, 3)`. To znači da, uz iste opažene
ishode i veličine skupina, nulti model daje apsolutnu razliku ovoliku ili veću
u otprilike `r hr_broj(s10$p * 100, 1)` % simuliranih rasporeda oznaka. U tumačenju moramo
zadržati uvjet da vrijedi nulti model.

Kad bismo pregledali sva moguća premještanja, izračunali bismo točan udio,
uključujući opaženi raspored. Ovdje uzimamo samo konačan broj nasumičnih
premještanja. Ako njihov broj označimo s $B$, a broj apsolutnih razlika barem
toliko velikih kao opažena s $b$, procjenjujemo p-vrijednost kao $(b + 1)/(B +
1)$. Dodavanje opaženog rasporeda sprječava rezultat nula i daje valjanu
procjenu za nasumično uzorkovana premještanja.

## Interakcija — Simulator p-vrijednosti

U početnim postavkama sljedećeg modela dvije skupine imaju po 60 osoba,
a pojedinačni ishodi normalnu raspodjelu sa standardnom devijacijom jedan.
Pod nulom obje sredine iznose nula. U scenariju s vezom druga je sredina
viša za 0,35. Jedna studija uspoređuje dvije uzoračke sredine i dijeli
njihovu razliku poznatom standardnom pogreškom $\sqrt{2/60}$.
Simulacija izravno generira tako standardizirani rezultat, što je u ovom
modelu jednako generiranju svih pojedinačnih ishoda i računanju iz njih.
Digitalni prikaz počinje s 2 000 ponavljanja po scenariju i dopušta promjenu
veličine skupina, učinka i broja ponavljanja. Tiskani prikaz zadržava po
60 osoba i razliku 0,35 te koristi 4 000 ponavljanja po scenariju. Svako
ponavljanje daje jednu p-vrijednost. Svi rezultati ulaze u prikaz.

Dosad smo za jedan uzorak premještali oznake i promatrali raspodjelu razlika.
Sada promatramo p-vrijednosti iz ponovljenih zamišljenih studija. U prvom
scenariju učinka nema, a u drugome postoji.
Koristimo normalne ishode s poznatom varijabilnošću i obostrani z-test.
Neovisnost skupina znači da se varijance njihovih sredina zbrajaju i kada
računamo razliku sredina. Standardna pogreška razlike korijen je toga zbroja.
P-vrijednost obostranog testa zbroj je površina u oba repa standardne
normalne raspodjele, izvan opaženog apsolutnog z-rezultata.
P-vrijednosti ovaj put računamo iz poznate normalne raspodjele, pa korekcija za
konačan broj premještanja nije potrebna. Razliku izražavamo u standardnim
devijacijama, što ćemo podrobnije objasniti u sljedećem poglavlju.

*Slika. Raspodjele p-vrijednosti pod nultim modelom i pod odabranim stvarnim učinkom.*

**Što isprobati.**

1. Postavite stvarnu razliku na nulu i opišite oblik gornje raspodjele.
2. Podignite stvarnu razliku na 0,35 uz nepromijenjen uzorak.
3. Povećajte uzorak bez promjene razlike i usporedite udio rezultata ispod praga.
4. Spustite prag s 0,05 na 0,01 i pogledajte obje raspodjele.

Kada vrijedi nulti model ove simulacije, p-vrijednosti su ravnomjerno
raspoređene između nule i jedinice. Jednako široki rasponi oko 0,03 i 0,53
zato su jednako vjerojatni. Prag od 0,05 izdvaja donjih pet posto raspodjele.
Upravo taj dugoročni udio odbacivanja pod nultim modelom prag ograničava.

## Dvije vrste pogreške

Prag je u prethodnom prikazu izdvojio i neke rezultate nastale bez učinka. Ako
na temelju njih odbacimo istinitu nultu hipotezu, činimo pogrešku prve vrste. U
drugoj simulaciji učinak postoji, ali dio p-vrijednosti ostaje iznad praga.
**Pogreška druge vrste** nastaje kada tako ne odbacimo nultu hipotezu iako je
lažna. Isti postupak odlučivanja stoga trebamo procijeniti u oba uvjeta.

**Pogreška prve vrste** je odbacivanje nulte hipoteze koja je istinita. Pod
pretpostavkama modela postupak ograničava dugoročni udio takvih odbacivanja
odabranim pragom.

Istraživački tim, primjerice, treba odlučiti hoće li poduprijeti tvrdnju da se
skupine razlikuju. Pogreška prve vrste dovela bi do neutemeljene usporedbe
skupina. Pogreška druge vrste mogla bi prikriti postojeću razliku i zaustaviti
njezino daljnje istraživanje. Posljedice snose i čitatelji i osobe o kojima se
zaključuje. Tim zato treba objasniti koju je pogrešku smatrao ozbiljnijom pri
izboru praga.

Stopu pogreške prve vrste možemo provjeriti simulacijom u kojoj nulti model
sigurno vrijedi. Iz poznate populacije svaki put uzimamo `r s10$n` ishoda, pa
im nasumično dodjeljujemo jednako mnogo oznaka A i B. Oznaka je neovisna o
ishodu. Tako obje skupine nastaju iz iste pune raspodjele povjerenja.

Sada jedno vanjsko ponavljanje sadrži cijeli test. Odaberemo novih 300
ishoda, nasumično im dodijelimo po 150 oznaka A i B, a zatim za taj uzorak
provedemo 300 unutarnjih permutacija i izračunamo jednu p-vrijednost.
Ponavljamo to 800 puta i broj p-vrijednosti ispod 0,05 dijelimo s 800.
Drugi scenarij uzima nove uzorke iz podskupa tiska i portala s njihovim
postojećim oznakama, u kojem veza postoji. To mijenja i sastav skupina,
čije brojnosti nisu unaprijed izjednačene. U oba niza sva su ponavljanja
definirana i nijedno nije izostavljeno.

Na osamsto takvih uzoraka permutacijski postupak odbacuje nultu hipotezu uz
prag 0,05 u `r hr_broj(s10$stopa_nulta, 1)` % slučajeva. Zbog konačnog broja premještanja i
slučajnog kolebanja među uzorcima udio ne mora biti točno pet posto. Ovdje
provjeravamo postupak u uvjetima koji zadovoljavaju njegovu pretpostavku
zamjenjivosti.

*Slika. Udio uzoraka u kojima permutacijska p-vrijednost ne prelazi prag od 0,05, za dva pitanja s poznatim odgovorom. Osamsto uzoraka po pitanju, u svakome tristo premještanja. Izrada autora.*

Drugi redak tablice pokazuje što se događa kada razlika postoji. U populaciji
razlika prema izvoru vijesti iznosi `r hr_broj(s10$istina_izvor, 2)` boda. Postupak je otkriva u
`r hr_broj(s10$stopa_izvor, 1)` % uzoraka. U preostalih `r hr_broj(s10$promasaj, 1)` % ne bismo imali dovoljno dokaza
za odbacivanje nulte hipoteze, iako razlika postoji.

Na zajedničkoj osi prikazane su raspodjela pod nultim modelom i raspodjela
procijenjene razlike kada učinak postoji. Prva premješta oznake u istom uzorku od 300 čitatelja tiska i portala, a druga nastaje novim izvlačenjima iz iste podpopulacije. Iste granične crte određuju odluku u oba slučaja.

*Slika. Geometrija dviju pogrešaka — uvjetna nulta raspodjela iz glavnog uzorka i raspodjela procijenjene razlike kroz uzorke kad učinak postoji. Isprekidane crte prikazuju granične vrijednosti glavnog uzorka, pa plohe ne prikazuju stope iz tablice. Izrada autora. Podaci i postupak opisani su u tekstu.*

Pomaknemo li granične crte prema van, rjeđe odbacujemo istinitu nultu
hipotezu. Istodobno veći dio raspodjele s postojećim učinkom ostaje između
crta, pa češće propuštamo razliku. Pri istom pragu veći uzorak ili preciznije
mjerenje mogu smanjiti pogrešku druge vrste, uz zadržano ograničenje pogreške
prve vrste. S više informacija možemo razmotriti i stroži prag, ali trebamo
ponovno procijeniti odnos obiju pogrešaka.

Površine na slici objašnjavaju odnos pogrešaka, ali nisu izmjerene stope iz
tablice. Gornja raspodjela prikazuje 4 000 premještanja oznaka iz glavnoga
uzorka, a donja 4 000 novih uzoraka iz populacije u kojoj razlika postoji.
Snaga postupka ovisi o veličini učinka, varijabilnosti,
veličini i nacrtu uzorka, testnoj statistici i pragu odluke.

### Referentna oznaka nije isto što i istina

Stope pogrešaka mogli smo prebrojiti jer smo u simulaciji zadali kako podaci
nastaju. Pri procjeni algoritama susrest ćemo srodno, ali drukčije pitanje,
slaže li se predviđena kategorija s **referentnom oznakom**, primjerice ručno
dodijeljenom kategorijom. Ta oznaka, za razliku od poznate istine simulacije,
može biti pogrešna. Ovisi o mjerenju, uputama za označavanje i načinu
rješavanja spornih slučajeva.

Neslaganje s referencom zato može potjecati i od postupka koji ispitujemo i od
same reference. U izvještaju navodimo kako su referentne oznake nastale i jesu
li neslaganja ponovno pregledana. To će biti posebno važno pri procjeni
algoritama. Uz precizno izračunatu stopu neslaganja potrebna je i provjera kvalitete same reference.

Vratimo se prijavama za posao. U objavljenom pokusu životopisi s imenima
prepoznatima kao bjelačka dobivali su više poziva na razgovor od
životopisa s imenima prepoznatima kao afroamerička (Bertrand, 2004).
Nulta pretpostavka bez učinka dodijeljenog imena dopuštala bi razlike
nastale samom nasumičnom dodjelom. Test bi pitao koliko su odstupanja
barem toliko velika kao opaženo česta pod takvim postupkom. Račun mora
pritom pratiti stvarnu dodjelu prijava i njihovo slanje na iste oglase,
umjesto da sve retke automatski smatra neovisnima.

Nasumična dodjela daje osnovu da razliku u odgovorima povežemo s
dodijeljenim imenima. Izmjereni ishod ipak je bio poziv na razgovor
na obuhvaćenim oglasima, a ne kasnije zaposlenje ili plaća
(Bertrand, 2004). Za osobu koja traži posao i ta je prva prepreka važna.
Zaključak o njoj zahtijeva zajedno opis pokusa, veličinu razlike i
njezinu nesigurnost. Mala p-vrijednost sama ne bi opravdala tvrdnju o
svakom poslodavcu ili o drugom tržištu rada.

## Prag je konvencija, a ne mjera

Rezultat nazivamo statistički značajnim kada mu p-vrijednost ne prelazi
unaprijed odabrani prag.

Koristimo **prag značajnosti** 0,05, ali moguće je odabrati i
0,01 ili 0,10. Izbor određuje dopuštenu dugoročnu stopu odbacivanja istinite
nulte hipoteze. Treba ga obrazložiti stručnim običajima i posljedicama
pogreške. Stroži prag ima smisla kada je lažni nalaz osobito skup, uz
uvažavanje povećanog rizika da propustimo postojeći učinak.

Rezultati neposredno ispod i iznad praga daju gotovo jednaku količinu dokaza.
P-vrijednosti 0,048 i 0,052 ne opravdavaju zaključke da u prvom slučaju učinak
postoji, a u drugom ga nema. Zato Američko statističko udruženje traži da
znanstveni zaključak ne ovisi samo o prelasku praga (Wasserstein, 2016).

Izjava u šest načela objašnjava da p-vrijednost opisuje neusklađenost podataka
s određenim modelom. Ne daje vjerojatnost hipoteze, vjerojatnost da je
rezultat „nastao slučajno” ni veličinu ili važnost učinka. Za zaključivanje su
potrebni potpuno izvještavanje, transparentnost i drugi znanstveni dokazi
(Wasserstein, 2016).

Kada izvještaj sve svede na oznaku „statistički značajan”, čitatelj lako
izgubi veličinu procjene, njezinu nesigurnost i posljedice odluke. Te
informacije trebaju ostati vidljive bez obzira na položaj p-vrijednosti u
odnosu na prag.

P-vrijednost pridonosi znanstvenom argumentu zajedno s procjenom učinka, kvalitetom nacrta i ostalim dokazima. U našem izvještaju zato najprije navodimo procjenu i interval,
objašnjavamo pretpostavke i razmatramo posljedice obiju pogrešaka.

P-vrijednost se mijenja i kada ponavljamo potpuno isti postupak. Na osamsto
uzoraka iz naše populacije, uz uvijek jednaku stvarnu razliku, polovica
p-vrijednosti bila je ispod `r hr_broj(s10$ples_sredina, 3)`, četvrtina iznad `r hr_broj(s10$ples_cetvrtina, 3)`, a desetina
iznad `r hr_broj(s10$ples_gornji, 3)`. Vrijednosti su se protezale preko dva reda veličine. U
`r hr_broj(s10$udio_iznad_deset, 1)` % uzoraka bile su veće od 0,10.

Uzoračka promjenjivost ostaje prisutna i u rezultatu prikazanom na tri decimale. S uzorkom se mijenjaju i procjena i njezin interval. Stavljamo ih na prvo mjesto jer
izravno odgovaraju na pitanje kolika je razlika i koliko smo je precizno
procijenili.

## Što p-vrijednost nije

Za kalibraciju zasebno uzimamo 300 vrijednosti povjerenja iz cijele simulirane populacije i nasumično im dodjeljujemo oznake A i B. Te oznake nisu izvori vijesti. Razlika iznosi
`r hr_broj(s10$razlika_nulta, 2)` boda, interval ide od `r hr_broj(s10$donja_nulta, 2)` do `r hr_broj(s10$gornja_nulta, 2)`, a p-vrijednost je
`r hr_broj(s10$p_nulta, 2)`. U ovoj simulaciji znamo da nulti model vrijedi jer oznake nastaju
neovisno o ishodu.

Ipak, sam rezultat testa ne dokazuje da razlike nema. Interval obuhvaća
vrijednosti u oba smjera, među kojima neke mogu biti sadržajno važne. Velika
p-vrijednost govori da podaci ne daju snažan razlog za odbacivanje nultog
modela.

Kod male p-vrijednosti česta je obrnuta pogreška. Vrijednost `r hr_broj(s10$p, 3)` odnosi
se na rezultate pod pretpostavljenim modelom. Ne daje vjerojatnost modela
nakon što smo vidjeli podatke. To su različite uvjetne vjerojatnosti, kakve
smo razdvojili u poglavlju o vjerojatnosti.

P-vrijednost ne daje ni vjerojatnost da je nalaz „slučajan”. Račun
pretpostavlja određeni nulti model i ne utvrđuje uzrok opaženog rezultata.
Također ne mjeri veličinu učinka. Uz dovoljno velik uzorak i mala, praktično
nevažna razlika može dati malu p-vrijednost.

## Drugo pitanje i drugi račun

Ponekad nas zanima koliko je određena veličina učinka vjerojatna nakon uvida u
podatke. Test iz ovog poglavlja ne odgovara na to pitanje. On uspoređuje
podatke s preciznim nultim modelom i omogućuje procjenu dugoročnog ponašanja
unaprijed određenog postupka. Nulti model posebno je koristan kada odsutnost
razlike ili zadana referentna vrijednost ima jasno značenje za odluku.

Bayesovski pristup povezuje početnu raspodjelu vjerojatnosti učinka s modelom
koji opisuje podatke pri različitim vrijednostima učinka. Dobivamo ažuriranu
raspodjelu vjerojatnosti. Iz nje možemo, uz prihvaćene pretpostavke,
procijeniti vjerojatnost da je učinak veći od nule ili neke sadržajno važne
granice.

U oba pristupa trebamo navesti pretpostavke. Bayesovski zaključak ovisi o
početnoj raspodjeli i modelu podataka, pa izvještavamo koliko je osjetljiv na
te izbore. Frekvencijski zaključak ovisi o modelu uzorkovanja ili dodjele,
testnoj statistici i unaprijed zadanom postupku. Pristupi postavljaju
različita pitanja i drukčije provjeravaju posljedice svojih pretpostavki.

U sljedećim poglavljima nastavljamo s frekvencijskim postupcima. Bayesovski
pristup ovdje samo ukratko upoznajemo, a ponovno ćemo ga spomenuti uz
regresiju. U oba pristupa veličina učinka i njezina nesigurnost ostaju važne
za tumačenje rezultata.

**Statistika u divljini.**
**Mala p-vrijednost pred uredničkom odlukom.** Pretpostavimo da
redakcija dobije istraživački izvještaj o razlici u povjerenju između
dviju skupina čitatelja. Autor navodi malu p-vrijednost i predlaže
naslov prema kojem je dokazao svoje objašnjenje razlike. Urednik
treba odlučiti što od toga može prenijeti publici. Uz točnost prepisanog broja urednik treba utvrditi što je njime provjereno.

Takve je prijelaze lakše prepoznati kad ih vidimo na konkretnim
tumačenjima. Jedan pregled okuplja dvadeset pet pogrešnih tumačenja
p-vrijednosti, intervala i snage, kao pomoć pri čitanju i pisanju
istraživačkih zaključaka (Greenland, 2016). Među njima je zamjena vjerojatnosti podataka pod
pretpostavljenim modelom vjerojatnošću da je sama hipoteza istinita.
Mala p-vrijednost ne daje postotak sigurnosti u autorovo objašnjenje
(Greenland, 2016).

Urednik bi zato u našem zamišljenom slučaju najprije trebao
potražiti procijenjenu razliku i njezin interval. Zatim treba
pročitati kako su čitatelji odabrani, što test uzima kao nulti
model i jesu li skupine samo opažene ili je provedena nasumična
dodjela. Ako je usporedba opažačka, uvjerljivo odstupanje od
nultog modela još ne pokazuje što je uzrokovalo razliku.

Važan je i put do objavljenog rezultata. Autori pregleda
upozoravaju da biranje analiza prema dobivenim p-vrijednostima
može proizvesti male vrijednosti čak i kada provjeravana nulta
hipoteza vrijedi (Greenland, 2016). Redakcija zato ima razlog
zatražiti podatak je li prikazana usporedba bila unaprijed
određena i koje su druge analize provedene. Takva provjera razjašnjava postupak odabira analize, uz otvoreno pitanje razloga autorovih odluka.

Nakon toga vijest može prenijeti opaženu razliku, njezinu
nesigurnost i ograničenje objašnjenja. Ako te informacije
nedostaju, urednik može odgoditi snažan naslov.  Test je usporedio podatke s određenim modelom, dok
predloženi naslov tvrdi nešto o tome zašto se ljudi razlikuju.
Između te dvije rečenice mora stajati dokaz koji sama
p-vrijednost ne sadrži.

**Nađite grešku.**
Provjerite odlomak o razlici povjerenja između čitatelja tiska i
portala u poznatoj simuliranoj populaciji. U uzorku je procjena razlike
tisak minus portal `r hr_broj(s10$razlika, 2)` boda, uz 95 % interval
od `r hr_broj(s10$donja, 2)` do `r hr_broj(s10$gornja, 2)`. Osobe su zasebne jedinice opažanja.

Za test se zadaje nulti model jednake pune raspodjele povjerenja, pod
kojim su oznake skupina zamjenjive. Asistentov zapis postupka glasi ovako.

Od 4.000 premještanja njih 64 daje apsolutnu razliku barem toliko veliku
kao opažena. Korigirani račun zato daje 65 / 4.001, približno 0,016. U izvještaju je asistent napisao sljedeće.

> Pod zadanim nultim modelom opažena je razlika neuobičajena. Skupine
> su promatračke, pa rezultat ne pokazuje uzrok razlike. P-vrijednost
> 0,016 znači da je vjerojatnost da između skupina nema razlike 1,6 %.

Povežite brojnik 65 s onim što je postupak prebrojio. Zatim uredite
posljednju rečenicu, uz jasno imenovan uvjet pod kojim se vjerojatnost
računa. Sačuvajte procjenu razlike, njezinu nesigurnost i ograničenje
uzročnog tumačenja.

## Razrađeni primjer

Na istom uzorku od 300 čitatelja tiska i portala usporedbu povjerenja provodimo od opažene
razlike do njezina položaja u nultoj raspodjeli. Najprije računamo razliku
sredina s izvornim oznakama. Zatim zadržavamo ocjene, premještamo oznake
skupina i svaki put računamo istu razliku. Prebrojavanjem odstupanja barem
toliko velikih kao opaženo procjenjujemo koliko je naš rezultat neobičan pod
nultim modelom.

U ovom pozivu `sample` bez dodatnih argumenata nasumično mijenja poredak
oznaka, dok `replicate` ponavlja račun i sprema razlike. Za razliku od
bootstrap izvlačenja osoba, ovdje svako premještanje zadržava iste ocjene i
iste veličine skupina. Ne zadajemo parametarski oblik raspodjele, ali i dalje
pretpostavljamo neovisne jedinice i zamjenjivost oznaka pod nultim modelom
jednake pune raspodjele. Brojimo odstupanja u oba repa jer je test obostran.
Jedinicu dodajemo brojniku i nazivniku radi korekcije za konačan broj
nasumičnih premještanja.

U izvještaju povezujemo veličinu razlike s rezultatom testa. Čitatelji tiska imaju u prosjeku
`r hr_broj(s10$razlika, 2)` boda više povjerenja od čitatelja portala, uz interval od `r hr_broj(s10$donja, 2)`
do `r hr_broj(s10$gornja, 2)`. Nulti model daje apsolutnu razliku ovoliku ili veću u `r hr_broj(s10$p * 100, 1)`
% simuliranih rasporeda opaženih oznaka. Te brojke opisuju samo naš simulirani
uzorak. U stvarnoj anketi takva bi usporedba pokazivala razliku među skupinama.
Za zaključak da čitanje tiska mijenja povjerenje trebali bismo i odgovarajući
istraživački nacrt.

Uzročni zaključak zahtijevao bi istraživački nacrt koji razdvaja moguća objašnjenja razlike. Zasebno procjenjujemo koliko je razlika važna za istraživačko pitanje te opravdava li neku odluku.

## Sažetak

Testom smo opaženi rezultat usporedili s raspodjelom nultog modela, koju smo
ovdje izgradili premještanjem oznaka. P-vrijednost opisuje udio odstupanja
barem toliko velikih kao opaženo, uz zadržan uvjet da vrijedi taj model, pa ne
dobivamo vjerojatnost hipoteze ni važnost učinka. Izbor praga povezuje dvije
moguće pogreške jer stroži prag smanjuje stopu prve, ali pri istim podacima
povećava stopu druge, dok više informacija može smanjiti drugu pri istom pragu.
Simulacijom s nasumičnim oznakama provjerili smo postupak kada nulti model
vrijedi, a uz postojeću razliku od `r hr_broj(s10$istina_izvor, 2)` boda vidjeli smo da je
propušta u `r hr_broj(s10$promasaj, 1)` % uzoraka. Ta nas propuštanja vode pitanju kako
prije prikupljanja podataka planirati uzorak za učinak koji vrijedi uočiti. U
sljedećem poglavlju odgovorit ćemo na njega pomoću veličine učinka i snage.

## Pojmovi

nulta hipoteza (*null hypothesis*), nulti model (*null model*), obostrani test (*two-sided test*), testna statistika (*test statistic*),
p-vrijednost (*p-value*), pogreška prve vrste (*Type I error*), pogreška druge
vrste (*Type II error*), prag značajnosti (*significance threshold*),
permutacijski test (*permutation test*), referentna oznaka (*reference label*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto p-vrijednost nije vjerojatnost nulte hipoteze,
tako da napišete dvije rečenice koje se razlikuju samo po tome što je uvjet, a
što zaključak. Imenujte podatak koji bi bio potreban da se od prve dođe do
druge.

### Računski

Nulta raspodjela iz ovog poglavlja ima sredinu nula i standardnu devijaciju
`r hr_broj(s10$sd_nulte, 2)` boda. Primijenite pravilo područja iz poglavlja o vjerojatnosti
i procijenite granice koje su dvije standardne devijacije udaljene od nule.
Prije računa imenujte testnu statistiku i postupak kojim je nulta raspodjela
izgrađena, pa procjenu usporedite s graničnom vrijednošću
`r hr_broj(s10$granica, 2)`. Zatim
pretpostavite da je isti uzorak prikupljen dobrovoljnom poveznicom na jednom
portalu. Pozivajući se na razliku između slučajnosti uzorkovanja i selekcije iz
poglavlja o uzorkovanju, odredite koju tvrdnju o populaciji ni mala p-vrijednost ne bi
mogla opravdati. [Na kraju u HTML widgetu postavite stvarnu razliku na nulu i
zabilježite približan udio uzoraka ispod praga.]
[U tiskanom ili dokumentnom izdanju na kraju očitajte udio iz prvoga retka
tablice stopa odbacivanja, u kojem stvarne razlike nema.]

### Kritički

Prosudite zašto je jednom strukovnom udruženju trebalo objaviti izjavu o
pojedinačnom statističkom postupku, a skupini statističara popis od dvadeset pet
pogrešnih tumačenja (Wasserstein, 2016; Greenland, 2016). Predajte kratku
uredničku bilješku i navedite jedno pravilo izvještavanja koje bi uklonilo
najviše pogrešaka odjednom. Dodajte tko u glavnom primjeru snosi posljedice
svake vrste pogreške i zašto procijenjena stopa pogreške prema referentnim
oznakama ne dokazuje da su te oznake nepogrešive.

### Revizija modela

Ocijenite analizu iz okvira o pogrešci. Imenujte korake koji su provedeni
ispravno, redak koda iz kojeg izlazi izvještajna brojka, rečenicu koja iz nje ne
slijedi i njezinu ispravljenu inačicu.

---

# Veličina učinka i snaga

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/11-velicina-ucinka-i-snaga.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Otvaramo društvenu mrežu i uz poziv na izbore ugledamo lica prijatelja
koji su označili da su već glasovali. Možda smo ionako namjeravali izaći,
a možda nas baš taj podsjetnik pokrene. Kako bismo prepoznali njegov
doprinos među svim razlozima zbog kojih ljudi odlaze na biralište?

U velikom pokusu tijekom američkih izbora istraživači su nasumično
dodjeljivali različite poruke korisnicima mreže (Bond, 2012).
Neke su prikazivale fotografije prijatelja koji su označili da su glasovali,
a druge istu poruku bez tih fotografija (Bond, 2012). Glasovanje su mogli
provjeriti u biračkim evidencijama samo za upareni podskup korisnika
(Bond, 2012).

Za odluku o takvoj poruci trebamo procijeniti veličinu učinka i što bi on
značio pri širokoj primjeni, uz granice skupine za koju je ishod provjeren.
Koliki bi pomak bio sadržajno važan i koliko podataka trebamo da bismo ga
pouzdano uočili?

Pri planiranju istraživanja polazimo od razlike koju bi vrijedilo uočiti. Zatim provjeravamo možemo li je planiranim postupkom dovoljno pouzdano razlikovati od slučajne promjenjivosti. Time
pitanje iz prethodnog poglavlja okrećemo prema planiranju. Umjesto da tek
nakon analize čitamo rezultat testa, unaprijed provjeravamo kakav bi nam
odgovor istraživanje moglo dati.

Razliku u povjerenju čitatelja tiska i portala već smo procijenili s
intervalom. Sada nas zanima njezina veličina i koliko je često uzorak može
uočiti. Za poznatu referencu služe svi čitatelji tiska i portala u populaciji
`populacija_medija`, umjesto prethodnog uzorka od 300 čitatelja tiska i portala.

Svaki redak predstavlja jednu zamišljenu osobu s izvorom vijesti i povjerenjem
na ljestvici od jedan do deset. Podaci su stvoreni za nastavu i ne opisuju
stvarne stanovnike. Poznatu razliku uspoređujemo s rezultatima ponovljenih
izvlačenja kako bismo prebrojili koliko je često postupak uočava.

Razliku najprije izražavamo u bodovima povjerenja, a zatim je uspoređujemo s
raspršenošću odgovora i opisujemo Cohenovim d. Sredina i standardna
devijacija iz opisne statistike tako zajedno daju standardiziranu veličinu
učinka. Važnost pomaka ipak trebamo obrazložiti sadržajem pitanja i mogućim
posljedicama odluke. Vrlo malen pomak može postati statistički značajan uz
dovoljno opažanja, što ćemo provjeriti simulacijom dviju naslovnica.

Snagu ćemo proučavati mijenjanjem učinka, veličine uzorka, raspršenosti i
praga odluke. Provjerit ćemo i što se događa kada iz malih istraživanja
zadržimo samo značajne rezultate.

Planirati možemo i unatrag, od razlike na koju bi zamišljeno uredništvo
reagiralo prema potrebnom broju osoba. Drugi je mogući cilj prihvatljiva
širina intervala. Usporedba tih ciljeva pomaže nam obrazložiti što od uzorka
očekujemo prije nego što vidimo nalaz i prepoznati kada je nesigurnost
prevelika za namjeravanu odluku.

## Razlika koja nešto znači

Veličina učinka brojčano opisuje razmjer razlike ili odnosa. Možemo je
izraziti u izvornim jedinicama, kao razliku bodova, ili bez njih, kao
standardiziranu razliku, korelaciju ili omjer. Njezinu sadržajnu važnost procjenjujemo prema istraživačkom pitanju i posljedicama odluke.

Povjerenje u medije bilježimo bodovima na ljestvici, pa razliku među
čitateljima tiska i portala prvo čitamo u tim jedinicama.

Za ovu referencu služe svi čitatelji tiska i portala u populaciji,
ukupno `r s11_N` osoba. Zbroj ocjena
među `r s11_n2` čitatelja tiska iznosi
`r sum(s11_skupine[["tisak"]])`, a među `r s11_n1` korisnika portala
`r sum(s11_skupine[["portal"]])`. Dijeljenjem svakog zbroja njegovim
brojem osoba dobivamo sredine `r hr_broj(mean(s11_skupine[["tisak"]]), 3)`
i `r hr_broj(mean(s11_skupine[["portal"]]), 3)`, pa ih možemo oduzeti.

Razlika iznosi `r hr_broj(s11$razlika, 2)` boda na ljestvici od jedan do deset. Navodimo je u
izvornim jedinicama kako bismo je mogli povezati s odlukom. Uredništvu koje
razmatra preraspodjelu sadržaja nije svejedno razlikuju li se skupine za tri
četvrtine boda ili za tri boda.

Razliku možemo usporediti i s raspršenošću odgovora. Jedan bod izgleda
drukčije kada su odgovori zbijeni oko sredine nego kada zauzimaju cijelu
ljestvicu. Standardizirana mjera izražava taj odnos.

**Standardizirana razlika** je razlika dviju sredina podijeljena združenom
standardnom devijacijom skupina, pa se izražava u standardnim devijacijama
umjesto u izvornim jedinicama.

$$d = \frac{\bar{x}_2 - \bar{x}_1}{s_{\text{zdr}}}$$

Oznakom $s_{\text{zdr}}$ označavamo združenu standardnu devijaciju, zajedničku
mjeru raspršenosti unutar dviju skupina.

Za zajedničku raspršenost povezujemo dvije varijance. Svaka dobiva težinu
jednaku broju osoba u skupini umanjenom za jedan, pa veća skupina više
pridonosi. Tek nakon toga vadimo korijen. Skupina 1 ovdje je portal, a
skupina 2 tisak. Brojeve osoba označavamo s $n_1$ i $n_2$, a standardne
devijacije s $s_1$ i $s_2$. Za dva uzorka račun glasi

$$s_{\mathrm{zdr}}=\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}.$$

U ovom primjeru račun obavljamo na cijeloj poznatoj sintetičkoj populaciji.
Zato dobivena razlika i njezina standardizacija opisuju te zapise bez
uzoračke nesigurnosti. Uzoračka procjena iste veličine zahtijevala bi i
interval. U brojnik ulazi
$(`r s11_n1`-1)\times `r hr_broj(var(s11_skupine[["portal"]]),3)` +
(`r s11_n2`-1)\times `r hr_broj(var(s11_skupine[["tisak"]]),3)`$,
a nazivnik je `r s11_n1+s11_n2-2`. Račun koristi nezaokružene varijance.

Združena standardna devijacija u ovoj populaciji iznosi `r hr_broj(s11$zdruzena, 2)` boda.
Razlika od `r hr_broj(s11$razlika, 2)` boda zato daje standardiziranu razliku od `r hr_broj(s11$d, 2)`.
Skupine dijeli nešto više od trećine standardne devijacije, a njihove se
raspodjele velikim dijelom preklapaju. Ista ocjena povjerenja može pripadati korisnicima obaju izvora, pa ona
sama ne određuje izvor vijesti pojedine osobe.

Preklapanje raspodjela možemo približiti i pitanjem o nasumično izabranom paru
osoba. Čitatelj tiska ima strogo više povjerenja od čitatelja portala u
`r hr_broj(s11$nadmoc_stroga, 1)` % parova, dok je `r hr_broj(s11$izjednaceno, 1)` % parova izjednačeno. Kada
polovicu izjednačenja pripišemo svakoj strani, prilagođena vjerojatnost nadmoći
iznosi `r hr_broj(s11$nadmoc, 1)` %. Za jednake raspodjele iznosila bi pedeset posto.
Razliku među skupinama tako opisujemo usporedbom ljudi, što može biti
razumljivo i čitatelju koji ne poznaje standardnu devijaciju.

Sadržajnu važnost učinka procjenjujemo prema ranijim
nalazima iz istog područja i posljedicama odluke. Standardizacija olakšava usporedbu različitih ljestvica, a prosudba važnosti ostaje vezana uz sadržaj istraživanja.

## Kad je značajno, a nije važno

Rezultat nazivamo statistički značajnim kada njegova p-vrijednost ne
prelazi unaprijed odabrani prag odluke. Uz statističku značajnost navodimo i procjenu veličine učinka kako bismo opisali razmjer razlike. To se posebno
jasno vidi na vrlo velikom uzorku.

Zamislimo pokus u kojem portal uspoređuje dvije naslovnice. Stvarna stopa
klika prve iznosi 2,00 %, a druge 2,05 %. Svaku prikazuje pola milijuna puta.
Podatke u nastavku simuliramo za tu zamišljenu usporedbu.

Jedno opažanje predstavlja jedan hipotetski prikaz naslovnice i njegov
ishod, klik ili izostanak klika. Pretpostavljamo neovisne prikaze s istom
vjerojatnošću unutar naslovnice. Račun generira zbroj klikova u svakoj od
dviju skupina od 500 000 prikaza. Za prvu dobivamo
`r round(s11_ab_a * s11_ab_n)` klikova, a za drugu
`r round(s11_ab_b * s11_ab_n)`. Dijeljenjem svakog broja s 500 000 nastaju
stope koje uspoređujemo. Ovo je jedan simulirani pokus, ne procjena snage
preko ponovljenih pokusa.

Prikazani 95-postotni interval i p-vrijednost koriste normalni Waldov
račun za razliku dvaju neovisnih udjela, s procijenjenim varijancama obiju
skupina. Ostvarena razlika veća je od zadane razlike od 0,05 postotnih
bodova. To je slučajno precjenjivanje u ovome pokusu, a ne promjena
poznatoga učinka. Značajnost ovog jednog rezultata ne mjeri snagu nacrta.

Uz zadane stope i broj prikaza normalno približenje daje snagu od oko 43 %.
Otkrivanje stvarnoga pomaka zato je u ovom nacrtu rjeđe od njegova propuštanja.

U simulaciji prva naslovnica postiže `r hr_broj(s11$ab_a, 3)` %, a druga `r hr_broj(s11$ab_b, 3)` % klikova.
Procijenjena razlika iznosi `r hr_broj(s11$ab_razlika, 3)` postotnog boda, uz interval od `r hr_broj(s11$ab_donja, 3)`
do `r hr_broj(s11$ab_gornja, 3)`. P-vrijednost iznosi `r formatC(s11$ab_p, format = "f", digits = 5, decimal.mark = ",")`. Pod nultim modelom ovako velika
ili veća odstupanja bila bi vrlo rijetka.

Dobivena razlika znači otprilike jedan dodatni klik na tisuću prikaza.
Opravdava li promjenu naslovnice, ovisi o trošku promjene i vrijednosti klika.
Trošak i vrijednost klika trebamo utvrditi iz dodatnih izvora. Velik uzorak omogućio nam je razlikovati mali pomak od nule, a te će informacije pomoći u obrazlaganju odluke.

U malom uzorku možemo propustiti i razliku koja bi bila važna za uredničku
odluku. Izostanak značajnosti zato ne dokazuje da je učinak nevažan. Procjenu
i interval izvještavamo prije testa kako bi čitatelj mogao razmotriti i
veličinu i nesigurnost rezultata.

Poruka s fotografijama prijatelja iz početnog pokusa pokazuje zašto i
malen pomak zaslužuje sadržajno tumačenje. Među korisnicima čije je
glasovanje provjereno u evidenciji procijenjena razlika prema poruci
bez fotografija iznosila je 0,39 postotnog boda, uz standardnu pogrešku
0,17 postotnog boda (Bond, 2012). Normalnim približenjem
$0,39 \pm 1,96 \times 0,17$ iz tih objavljenih vrijednosti dobivamo
približan 95-postotni interval od 0,06 do 0,72 postotnog boda
(Bond, 2012). Procjena je mala za pojedinca, a njezina nesigurnost ostaje
važna i uz vrlo mnogo korisnika.

U zamišljenoj primjeni na milijun usporedivih ljudi pomak od 0,39
postotnog boda odgovarao bi približno 3.900 dodatnih izlazaka. To je
ilustracija razmjera, uz pretpostavku da se učinak može prenijeti na
tu skupinu. Za stvarnu odluku trebalo bi provjeriti taj prijenos,
trošak poruke i prihvatljivost korištenja prijateljskih veza za
poticanje ponašanja. U samom su pokusu istraživači zasebno proučavali
i širenje učinka kroz mrežu prijatelja (Bond, 2012). Jednostavno
množenje izravnog učinka zato još ne daje ukupan društveni učinak.

## Snaga kao svojstvo plana

Prije prikupljanja podataka možemo procijeniti koliko bi često naš plan otkrio
zadani učinak. Za to trebamo odrediti postupak, veličinu učinka, uzorak,
raspršenost i prag odluke.

Ako nakon istraživanja opaženi učinak proglasimo stvarnim i iz njega
izračunamo snagu, račun je kružan. Uz isti uzorak i prag takva snaga prati
već opaženu testnu statistiku i ne daje neovisnu provjeru je li dizajn mogao
otkriti unaprijed važan učinak.

**Statistička snaga** je vjerojatnost da postupak odbaci nultu hipotezu kad je
ona lažna, dakle udio ponavljanja u kojima bi učinak zadane veličine bio
otkriven.

U prethodnom poglavlju postupak je otkrio stvarnu razliku u otprilike četiri
od pet uzoraka od tristo osoba. Taj udio procjenjuje snagu. Sada ćemo ga
usporediti za nekoliko veličina uzorka.

Zadržavamo permutacijski test iz prethodnog poglavlja. Nulti model
pretpostavlja jednaku cijelu raspodjelu povjerenja u objema skupinama, pa su
oznake zamjenjive u odnosu na ishod. Statistika je apsolutna razlika sredina,
a osobe smatramo neovisnim jedinicama. Iz podskupa koji čine svi čitatelji tiska i portala u populaciji izvlačimo uzorke bez vraćanja. Za svaku veličinu provodimo
tristo zamišljenih studija. U svakoj koristimo dvjesto nasumičnih premještanja
i korekciju $(b + 1)/(B + 1)$, gdje je $B$ broj premještanja, a $b$ broj barem
toliko ekstremnih rezultata kao opaženi. Krivulja procjenjuje snagu za taj
postupak i način nastanka podataka.

Veličina uzorka u ovoj tablici jest ukupan broj osoba iz obiju skupina,
čije brojnosti nisu unaprijed izjednačene. Kasniji plan s jednakim skupinama
navodi broj po skupini. Uz 200 permutacija moguće p-vrijednosti razlikuju
se za 1/201, približno 0,005. Odluka neposredno uz prag zato može ovisiti
o slučajnom izboru premještanja.

U svakom retku brojimo studije s p-vrijednošću koja ne prelazi 0,05 i dijelimo
brojem valjanih studija. Ako bi uzorak sadržavao samo jednu skupinu, test
ne bi bio definiran i studiju bismo isključili, uz prikazan broj isključenja.
U ovoj izvedbi takvih studija ima `r sum(s11_krivulja$izostavljeni)`.
Tristo ponavljanja daje razmjerno grubu procjenu snage. Oko snage od 80 %
simulacijska standardna pogreška iznosi približno 2,3 postotna boda.

*Slika. Udio uzoraka u kojima permutacijska p-vrijednost ne prelazi prag od 0,05 pri stvarnoj razlici od 0,74 boda. Tristo simuliranih studija po retku. Izrada autora.*

Kada povećamo uzorak sa šezdeset na tristo osoba, procijenjena snaga raste s
`r hr_broj(s11$snaga_60, 1)` % na `r hr_broj(s11$snaga_300, 1)` %. Rast se postupno usporava kako se približavamo
gornjoj granici. Sa šezdeset osoba ovaj bi postupak propustio stvarnu razliku
u približno tri od četiri studije.

Snaga raste s većim učinkom i većim uzorkom. Pomažu i manja raspršenost ishoda
te blaži prag odluke. Istraživač može planirati uzorak i prag, a nacrtom i
kvalitetom mjerenja utjecati na raspršenost. Veličina stvarnog učinka ostaje nepoznata, pa snagu treba razmotriti za više mogućih veličina.

Često se planira snaga od 80 %, ali taj izbor treba opravdati (Cohen, 1988).
Ako bi propuštena razlika imala ozbiljne posljedice, možda trebamo višu snagu.
Istraživanje izvedivosti može imati drukčiji cilj i zahtjeve.

## Odabir značajnih nalaza pri niskoj snazi

Slaba snaga povećava broj propuštenih učinaka. Može utjecati i na veličinu
procjena koje objavljujemo ako zadržavamo samo značajne rezultate. To možemo
provjeriti u simulaciji s poznatom populacijom.

Za sljedeću usporedbu ponovno izvlačimo uzorke iz istoga podskupa
tiska i portala, svaki put po 60 osoba. Svaka studija daje jednu procjenu razlike i jednu
permutacijsku p-vrijednost. Tablica donosi prvih pet valjanih studija u
redoslijedu generiranja. Oznaka u posljednjem stupcu pokazuje bi li studija bila objavljena kada
bismo zadržali samo rezultate ispod 0,05.

*Slika. Pet simuliranih studija prije odabira prema pragu. Izrada autora.*

Prva procjena iznosi `r hr_broj(s11_male[1, 1], 3)` boda i ulazi u
prosjek svih studija. U prosjek odabranih ulazi samo ako zadovolji prag.
Od 3 000 pokušaja neprimjenjivo je `r s11_male_izostavljene`, pa prosjek
svih računamo na `r nrow(s11_male)` valjanih studija, a prosjek značajnih
na `r nrow(s11_znacajne)`. Isti manji nazivnik koristimo za udio značajnih
procjena s pogrešnim predznakom. Kod zasebnih 1 000 studija s po 500 osoba
izostavljeno je `r s11_velike_izostavljene`, a prag prolazi
`r nrow(s11_znacajne_velike)` studija.

Proveli smo tri tisuće zamišljenih studija sa šezdeset osoba. Prosjek svih
procjena iznosi `r hr_broj(s11$prosjek_svih, 2)` boda, blizu stvarne razlike od `r hr_broj(s11$razlika, 2)`. Prije
odabira prema pragu procjene u ovoj simulaciji ne pokazuju pristranost.

*Slika. Procijenjena razlika u tri tisuće studija sa šezdeset osoba, sve zajedno i samo one koje su prešle prag. Okomita crta označuje stvarnu razliku u populaciji. Izrada autora. Podaci i postupak opisani su u tekstu.*

Donji panel zadržava samo rezultate koji su prešli prag značajnosti. Njihov
prosjek iznosi `r hr_broj(s11$prosjek_znacajnih, 2)` boda, odnosno `r hr_broj(s11$faktor, 1)` puta onoliko koliko iznosi stvarna razlika.
U malom uzorku prag najčešće prelaze procjene koje je slučajnost povećala.
Najmanja apsolutna vrijednost značajne procjene u ovoj simulaciji iznosi `r hr_broj(s11$najmanja_znacajna, 2)` boda.
Sam odabir rezultata prema pragu može stvoriti to iskrivljenje, čak i kada istraživač postupa u dobroj vjeri.

Među `r nrow(s11_znacajne)` značajnih procjena njih `r sum(s11_znacajne[, 1] < 0)` ima suprotan predznak od
stvarne razlike. Račun može biti točan, a pojedinačni zaključak o smjeru
učinka pogrešan.

S pet stotina osoba značajne procjene premašuju stvarnu razliku za faktor
`r hr_broj(s11$faktor_veliki, 2)`, pa je iskrivljenje mnogo manje. Ti brojevi vrijede za ovu
populaciju, uzorke, postupak i prag. Ne možemo ih prenijeti na svaki nalaz iz
maloga uzorka.

Pri čitanju rada zato provjeravamo širinu intervala, način odabira rezultata i
odnos prema ranijim dokazima. Velik učinak uz p-vrijednost blizu praga sam po
sebi ne dokazuje precjenjivanje. Sličan rezultat iz neovisne replikacije daje
dodatni razlog za povjerenje u procjenu. Niska snaga upozorava na nesigurnost
i moguću selekciju nalaza.

## Planiranje unatrag

Veličinu uzorka planiramo prema pitanju koje želimo riješiti. Najprije trebamo
odrediti kolika bi razlika bila dovoljna da promijeni postupanje.

**Najmanji važan učinak** je najmanja razlika koja bi promijenila zaključak,
odluku ili postupanje, određena sadržajno i prije prikupljanja podataka.

Tu granicu obrazlažemo troškovima odluke, ozbiljnošću ishoda i ranijim
nalazima iz područja. Tako obrazložena granica postaje ulaz u račun potrebnog broja opažanja za željenu snagu.

Polazimo od važne razlike i željene snage, pa računamo potreban broj jedinica.
Zatim provjeravamo je li takav uzorak izvediv. Ako nije, ograničenje znamo
prije prikupljanja podataka i možemo prilagoditi plan ili doseg istraživanja.

Veličinu uzorka možemo odrediti i vraćanjem na pitanje iz poglavlja o procjeni.
Koliko uzak interval trebamo da bi procjena bila korisna? Uz raspršenost iz ove
populacije interval razlike širok je `r hr_broj(s11$sirina_100, 2)` boda pri stotinu osoba po
skupini, `r hr_broj(s11$sirina_300, 2)` pri tristo i `r hr_broj(s11$sirina_800, 2)` pri osamsto. Margina je
polovica ukupne širine, pa za marginu do pola boda tražimo širinu do jednoga
boda. Ulazi u taj plan jesu željena širina intervala, razina pouzdanosti i pretpostavljena raspršenost.

Uz iste pretpostavke kao u završnom planu, poznatu standardnu devijaciju
1,9 i dvije jednake neovisne skupine, margina do 0,5 traži
$n\geq 2(1,96\times1,9/0,5)^2$, odnosno
`r ceiling(2*(qnorm(.975)*1.9/.5)^2)` osoba po skupini. Za otkrivanje
razlike od 0,5 uz snagu oko 80 % normalno približenje daje
$n\approx2[(1,96+0,842)1,9/0,5]^2$, približno
`r ceiling(2*((qnorm(.975)+qnorm(.8))*1.9/.5)^2)` osoba po skupini.
Broj 0,842 jest kvantil standardne normalne raspodjele ispod kojega leži
80 % površine. U ovoj približnoj planskoj formuli odgovara ciljanoj snazi
od 80 %, dok 1,96 dolazi iz obostranoga testa na razini 5 %. Ta dva plana
odgovaraju na različita pitanja pod jednakim pretpostavkama.

Planiranje prema snazi zahtijeva pretpostavljeni učinak, koji još ne znamo. U
ovom modelu planiranje prema preciznosti polazi od razine pouzdanosti,
pretpostavljene raspršenosti i prihvatljive širine intervala. Cilj je dovoljno
precizna procjena, bez obzira na to gdje će se nalaziti. Ostvarena preciznost
ipak ovisi o tome koliko su planske pretpostavke odgovarale podacima.

## Interakcija — Istraživač snage

Dosad smo mijenjali veličinu uzorka iz populacije sa zadanom razlikom. Sada
želimo vidjeti i što se događa kada pretpostavimo manji ili veći učinak. Zato
prelazimo na jednostavan model u kojem učinak možemo mijenjati, a raspršenost
zadržati jednakom. Krivulje prikazuju snagu za različite uzorke i zadane
učinke. Za isti učinak veći uzorak povećava vjerojatnost otkrivanja, dok je uz
isti uzorak manji učinak teže otkriti.

Jedna točka krivulje sažima zamišljene studije za zadani učinak
i broj osoba po skupini. [Digitalni prikaz počinje s 1 500 ponavljanja po
točki, učinkom 0,35 i odabranim uzorkom od po 80 osoba. Sve te postavke
možemo mijenjati.]{.content-visible when-format="html"} Tiskani prikaz koristi 2 000 ponavljanja po točki i
učinke 0,2, 0,4 i 0,6. Primjerice, za razliku 0,4 i po 100 osoba
standardna je pogreška razlike $\sqrt{2/100}$ kada je poznata standardna
devijacija ishoda jedan. Svaka studija daje razliku podijeljenu tom
pogreškom. Broj rezultata kojima je apsolutna vrijednost iznad 1,96
dijelimo s brojem ponavljanja za tu točku. Svi rezultati ulaze u nazivnik. Krivulja ne broji
pojedinačne osobe, a njezina mala kolebanja potječu od simulacije.

Prikaz pretpostavlja dvije neovisne skupine jednake veličine, neovisne
normalne ishode i zajedničku poznatu standardnu devijaciju. Nulta hipoteza
zadaje standardiziranu razliku nula. Obostrani test koristi apsolutnu
z-vrijednost. Za svaku točku simuliramo z-vrijednosti iz odgovarajuće normalne
raspodjele. Više ponavljanja daje manju simulacijsku nesigurnost procjene
snage.

*Slika. Simulirana snaga kroz veličine uzorka u idealiziranom postupku s poznatom varijabilnošću.*

**Što isprobati.**

1. Zadržite učinak jednakim i povećavajte uzorak.
2. Zadržite uzorak jednakim i smanjujte učinak.
3. Spustite prag odluke i provjerite koliko je jedinica potrebno za istu snagu.
4. Postavite standardiziranu razliku na 0,10 i pokušajte dosegnuti 80 %.

Za najmanju prikazanu standardiziranu razliku, 0,2, tristo jedinica po
skupini još ne daje snagu od 80 %. Trebao bi veći uzorak. Zato pri planiranju moramo jasno reći koju
veličinu učinka želimo moći otkriti.

**Statistika u divljini.**
**Velik objavljeni učinak i plan male studije.** Za novi istraživački
projekt privlačno je uzeti učinak iz prethodnog rada i prema njemu
odrediti potreban broj sudionika. Ako je objavljena razlika velika,
plan može izgledati izvedivo i uz skroman uzorak. No prije nego
što tu brojku pretvorimo u obećanje budućeg istraživanja, trebamo
razmotriti kako je dospjela u literaturu.

Analiza istraživanja u neuroznanosti pokazala je i drugu posljedicu
niske snage. Uz propuštanje postojećih učinaka, mala istraživanja mogu
ostaviti i pretjeran dojam o njihovoj veličini ako se nalazi odabiru
za objavu prema značajnosti (Button, 2013). U takvom izboru lakše prolaze rezultati koji su,
uz postojeći učinak, dobili i povoljan slučajni pomak.

Zamislimo tim koji na temelju jednoga takvog nalaza planira
ponavljanje. Ako precijenjenu razliku prihvati kao realan cilj,
mogao bi odabrati uzorak koji ima premalu snagu za skromniji,
ali sadržajno važan učinak. Tada neodlučan rezultat ne bi jasno
razlikovao izostanak učinka od nedostatka informacija. Velik
broj u prvom radu tako može dovesti do premalog plana u drugome.
Zamišljeni tim ilustrira moguću posljedicu takvog planiranja.

Odgovor je pregledati interval iz prethodnog istraživanja,
neovisna ponavljanja i širi skup dostupnih nalaza. Uz njih tim
treba odrediti najmanju razliku koja bi promijenila njegov
sadržajni zaključak te ispitati koliko sudionika treba za
nekoliko uvjerljivih veličina učinka. Ako izvediv uzorak ne
može dovoljno precizno odgovoriti na pitanje, korisno je to
znati prije prikupljanja.

Naša simulacija pokazala je mehanizam odabira, ali njezin faktor
precjenjivanja vrijedi za zadanu populaciju i postupak. Ne
možemo njime korigirati sve objavljene radove. Za planiranje
je korisnija promjena polaznog pitanja. Umjesto da pitamo
koliko je ljudi dovoljno za objavljenu brojku, pitamo kakav
nam je uzorak potreban da razlučimo mogućnosti koje su važne
za naše istraživanje.

**Nađite grešku.**
Pregledavate završni izvještaj male studije. Za ovu je vježbu
konstruiran nalaz standardizirane razlike od 0,78 uz trideset osoba po
skupini. Prije prikupljanja tim je kao najmanju važnu razliku odredio
0,5 boda i za planiranje pretpostavio standardnu devijaciju od 1,9 boda.
Te su vrijednosti pretpostavke nastavnog primjera, a ne objavljen nalaz.

Asistent je nakon uvida u rezultat izračunao sljedeće.

Za zadane ulaze poziv vraća snagu približno 0,84. Uz ispis stoji
obrazloženje.

> Opaženu standardiziranu razliku unijeli smo kao `delta`, a
> standardnu devijaciju postavili na jedan jer računamo na
> standardiziranoj skali. Dobivena snaga veća je od 0,80, pa potvrđuje
> da je završena studija bila dovoljno velika za naše pitanje.

Sastavite odgovor timu. Objasnite što račun od 0,84 vrijedi uz zadane
ulaze, a što iz njega ne slijedi. Predložite vrijednost učinka za
planiranje nove studije na temelju prethodno određenog cilja i navedite
koji biste podatak iz završene analize još tražili za prosudbu preciznosti.

## Razrađeni primjer

Planiranje unatrag sada možemo provesti za konkretnu uredničku odluku.
Pretpostavimo da bi uredništvo reagiralo na razliku od pola boda, uz očekivanu
raspršenost sličnu onoj u našoj populaciji. Ta je granica pretpostavka primjera
koju bi u stvarnom istraživanju trebalo opravdati. Za nekoliko veličina uzorka
procijenit ćemo koliko bi često simulirana studija otkrila zadanu razliku.

Nulta hipoteza zadaje razliku sredina nula, a testna statistika dijeli opaženu
razliku poznatom standardnom pogreškom. Pretpostavljamo dvije neovisne
skupine, neovisne normalne ishode i jednaku poznatu standardnu devijaciju od
1,9 boda. Koristimo obostrani z-test s pragom 0,05. Za svaku veličinu uzorka
simuliramo dvije tisuće parova skupina. Dobivena snaga vrijedi za te uvjete i
zadanu razliku od pola boda.

Prva studija s po 100 opažanja počinje vrijednostima
`r paste(hr_broj(s11_plan_prva[1:3], 2), collapse = ", ")` u prvoj skupini
i `r paste(hr_broj(s11_plan_druga[1:3], 2), collapse = ", ")` u drugoj.
To su generirani ishodi na centriranoj, neograničenoj normalnoj ljestvici,
pa nisu doslovne ocjene od jedan do deset. Iz svih 100 vrijednosti po
skupini dobivamo sredine `r hr_broj(mean(s11_plan_prva), 3)` i
`r hr_broj(mean(s11_plan_druga), 3)`. Njihovu razliku dijelimo s
$1,9\sqrt{2/100}$ i uspoređujemo apsolutni rezultat s 1,96.
Svako novo ponavljanje generira svih 200 ishoda iznova. Broj otkrivenih
razlika dijelimo s 2 000, bez isključenih studija.

Za svaku ponuđenu veličinu uzorka ponavljamo studiju dvije tisuće puta.
Granica 1,96 dolazi iz
standardne normalne raspodjele. Pripada ovom obostranom z-testu, a ne
permutacijskom testu iz prvog prikaza snage.

*Slika. Udio simuliranih studija u kojima bi razlika od pola boda bila otkrivena, pri četirima veličinama uzorka po skupini. Izrada autora.*

Za snagu od približno 80 % pri razlici od pola boda potrebno je između dvjesto
i dvjesto pedeset osoba po skupini. Ako je izvedivo samo stotinu, istraživanje
možemo provesti uz jasno ograničenje. Pod planskim pretpostavkama propustilo
bi takvu razliku u više od polovice ponavljanja.

Račun povezuje planirani uzorak s učinkom koji želimo otkriti. Granicu od pola
boda trebamo opravdati sadržajno, a očekivanu raspršenost ranijim mjerenjima.
Simulacija ovdje ne uključuje odustajanje ispitanika ni probleme mjerenja, pa
i njih treba razmotriti pri konačnom planiranju.

## Sažetak

Da bismo planirali istraživanje, trebamo odrediti koliku bi razliku vrijedilo
uočiti, jer statistička značajnost sama ne govori je li ona važna.
Standardizacija pomaže usporediti veličine učinka na različitim ljestvicama,
a njihovo sadržajno značenje prosuđujemo zasebno. Snaga povezuje zadani učinak,
uzorak, raspršenost i prag, dok planiranje prema preciznosti pita koliko nam
uzak interval treba. Velik uzorak može otkriti i vrlo malu razliku, a u našoj simulaciji maloga uzorka procjene odabrane prema značajnosti bile
su u prosjeku dvostruko veće od stvarne razlike. Taj faktor opisuje odabir prema pragu u prikazanom
scenariju i ne prenosimo ga na druga istraživanja. U poglavlju o krizi i obnovi
vidjet ćemo kako istraživačke odluke i objavljivanje dodatno oblikuju nalaze
koje čitatelj uopće može vidjeti.

## Pojmovi

veličina učinka (*effect size*), standardizirana razlika (*Cohen's d*),
sadržajna važnost (*practical significance*), statistička snaga (*statistical
power*), precjenjivanje pri odabiru značajnih nalaza (*selection-induced effect-size exaggeration*), najmanji važan učinak (*smallest effect size of interest*),
planiranje veličine uzorka (*sample size planning*), širina intervala (*interval
width*)

## Zadaci

### Konceptualni

Objasnite u jednom odlomku zašto u simulaciji ovoga poglavlja podskup procjena
koje su prešle prag u prosjeku premašuje poznatu razliku, iako prosjek svih
procjena ostaje blizu istini. Imenujte korak u kojem nastaje iskrivljenje i
objasnite zašto se dobiveni faktor ne smije prenijeti na svako područje.

### Računski

Iz upravljanoga agregata `data/populacija-medija-agregat.csv` uzmite retke za
portal i tisak. U tiskanom ili dokumentnom izdanju iste su vrijednosti u tablici
uz statični prikaz. Za svaki redak podijelite zbroj povjerenja brojem osoba,
usporedite rezultat s pohranjenim prosjekom i izračunajte razliku prosjeka.
Zatim za standardiziranu razliku 0,4 zabilježite snagu pri 40, 80, 160 i 300
jedinica po skupini. U HTML-u upotrijebite widget.
[U tiskanom izdanju tablicu sa zadanom postavkom upotrijebite kao izvor
vrijednosti.]

Vratite se objašnjenju standardne pogreške i širine intervala u poglavlju o
procjeni. Objasnite zašto veći uzorak istodobno sužava interval i povećava snagu,
ali ne mijenja unaprijed zadanu veličinu učinka. Predajte dva računa prosjeka,
njihovu razliku, četiri vrijednosti snage i jedan odlomak koji povezuje preciznost
sa snagom. Ocjenjuje se račun i tumačenje, ne pisanje koda.

### Kritički

Prosudite tvrdnju da niska prosječna snaga nekog područja znači samo da
istraživanja propuštaju stvarne učinke (Button, 2013). Predajte kratku uredničku
bilješku i navedite podatak koji bi vam trebao da procijenite koliko je
objavljena veličina učinka precijenjena.

### Revizija modela

Ocijenite provjeru iz okvira o pogrešci. Imenujte što je u pozivu ispravno,
argument u kojem stoji kružnost, redak koda u kojem ona ulazi u račun, i
napišite čime bi taj argument trebalo zamijeniti.

---

# Kriza i obnova

> Iz knjige: Statistika 101
> Autori: Luka Šikić, Petra Palić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/12-kriza-i-obnova.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-10-27 · © 2026 Luka Šikić, Petra Palić. MIT licenca: https://github.com/lusiki/statistika-knjiga/blob/main/LICENSE

---

Možemo li se oraspoložiti tako da najprije promijenimo izraz lica? Ta je
zamisao privlačna jer nam daje nešto jednostavno što možemo pokušati u
lošem danu. Za njezinu znanstvenu provjeru ipak treba smisliti kako
promijeniti izraz lica, a da sudionicima ne sugeriramo kako bi se trebali
osjećati.

U poznatom pokusu sudionici su ocjenjivali stripove držeći olovku zubima ili
usnama. Razlika u ocjenama protumačena je kao potpora tvrdnji da položaj
mišića lica može utjecati na doživljaj zabave (Wagenmakers, 2016). Gotovo tri
desetljeća poslije 17 laboratorija ponovilo je postupak prema zajedničkom
protokolu, s planom i analitičkim kodom pripremljenima prije uvida u podatke
(Wagenmakers, 2016).

Što bismo trebali promijeniti u svojem uvjerenju ako takvo ponavljanje
pruži drukčiju sliku? Možemo li iz njega naučiti nešto određenije od toga
da je jedna studija bila „uspješna”, a druga „neuspješna”?

Procjenu i njezin interval sada znamo čitati uz veličinu učinka, snagu i
pogreške testiranja. Pri usporedbi izvornog nalaza s replikacijom otvara se
i novo pitanje. Vidimo li sve što je istraživač mogao analizirati ili
samo rezultat koji je na kraju odabran za objavu? Razloge odabira rezultata tražimo u zapisima istraživačkih odluka, uz provjeru samoga računa.

Pokus iz vinjete pratit ćemo kroz objavljene rezultate laboratorija koji su
ponovili postupak (Wagenmakers, 2016). U tablicama s kojima radimo jedan redak sažima rezultate jednog laboratorija. Uspoređivat ćemo
razlike u ocjenama zabavnosti između uvjeta držanja olovke, njihove intervale
i brojnosti skupina. Ti sažeci pokazuju koliko se procjene razlikuju među stvarnim provedbama zajedničkog postupka (Wagenmakers, 2016). Od njih ćemo jasno
odvojiti nastavne simulacije u kojima sami određujemo koliko se analiza
iskušava.

Mijenjanje ishoda, podskupina ili trenutka zaustavljanja utječe na mogućnost
lažnog nalaza, što možemo provjeriti simulacijom. Pritom razlikujemo
namjerno traženje poželjnog rezultata od odluka koje ovise o viđenim
podacima čak i kada istraživač provede samo jednu analizu. Izbor se
nastavlja među studijama koje postaju dostupne čitateljima. Zato pogreške
pojedinog testa razmatramo zajedno s postupkom kojim je od više mogućih
nalaza odabrana objavljena tvrdnja.

Obnovu istraživačke prakse zato povezujemo s dostupnošću plana, podataka i
analitičkih odluka. Pri čitanju laboratorijskih procjena oslanjamo se na
intervale i veličine učinka iz prethodnih poglavlja, a u razrađenom primjeru
uspoređujemo sirovu i standardiziranu sintezu. Doseg novoga rezultata određujemo prema onome što je točno ponovljeno, preciznosti procjena i razlikama u postupku koje još treba istražiti. Na toj osnovi procjenjujemo nalaz i predlažemo sljedeću provjeru,
uz dovoljno jasan zapis da je druga osoba može ponoviti.

## Od jedne tvrdnje do provjerljivoga pitanja

Istraživanje uključuje mnogo odluka prije završne tablice. Određujemo tko može
sudjelovati, kako provodimo zadatak, što mjerimo, kako postupamo s nepotpunim
odgovorima i koju usporedbu smatramo glavnom. Čitatelj treba znati koje smo
odluke donijeli unaprijed, a koje nakon pregleda podataka. Inače ne može
procijeniti koliko je rezultat utjecao na izbor analize.

[P-hakiranje]{.pojam def="Prilagođavanje ili selektivno izvještavanje analiza
dok se ne dobije poželjan rezultat." en="p-hacking" ch="12"} nastaje kada
istraživač iskušava ishode, podskupine, pravila isključivanja ili trenutke
zaustavljanja kako bi dobio poželjan nalaz, pa prikaže samo odabrani postupak.
Metodološko istraživanje pokazalo je da takva neprikazana fleksibilnost povećava
udio lažno pozitivnih zaključaka (Simmons, 2011). Uobičajena p-vrijednost
vrijedi za unaprijed određen postupak. Nakon pretraživanja ne opisuje stopu
pogreške cijelog procesa odabira.

[Vrt račvajućih putova]{.pojam def="Skup analiza koje bi bile odabrane ovisno
o obrascima u podacima, čak i kada istraživač provede samo jednu." en="garden
of forking paths" ch="12"} može nastati i bez svjesnog traženja poželjnog
nalaza. Istraživač provede jednu analizu, ali bi odabrao drugu da su podaci
izgledali drukčije. Odluka je zato ovisila o podacima čak i ako ostale
mogućnosti nisu izračunate (Gelman, 2013). P-hakiranje opisuje namjerno
ponašanje, a račvajući putovi obilježje postupka koje treba prepoznati i
dokumentirati.

Izbor ne završava analizom unutar jedne studije.
[Publikacijska pristranost]{.pojam def="Selekcija istraživačkih rezultata pri
kojoj vjerojatnost javne vidljivosti ovisi o njihovu smjeru, jasnoći ili
poželjnosti." en="publication bias" ch="12"} nastaje pri odabiru onoga što
postaje dostupno čitateljima. Čak i korektno provedene studije mogu dati
iskrivljenu sliku ako objavljivanje ovisi o rezultatu. Open Science
Collaboration pokazao je važnost sustavnog proučavanja replikabilnosti većeg
skupa nalaza (Collaboration}, 2015). Za razumijevanje literature trebamo razmotriti i
pokušaje koji su ostali neobjavljeni.

## Analitička fleksibilnost prije modela

U jednom je istraživanju 29 timova analiziralo iste početne podatke i
dobilo različite procjene povezanosti boje kože nogometaša i crvenih kartona
(Silberzahn, 2018). Razlike među rezultatima sada nastaju promjenom analize,
dok smo pri uzorkovanju mijenjali uzorke. Uspoređujemo veličinu procijenjene
veze, njezinu nesigurnost i opravdanost postupaka.

**Analitička fleksibilnost** je prostor više obranjivih odluka duž cijeloga puta
podataka, od prikupljanja, uključivanja i spajanja do rekodiranja, postupanja s
nedostajućim vrijednostima i izbora analize.

U registriranom replikacijskom izvještaju (RRR) laboratoriji su unaprijed
dogovorili kriterije uključivanja, računanje ocjene i glavnu sirovu razliku
među skupinama. Plan i kod pripremili su prije stvarnih podataka
(Wagenmakers, 2016). Lokalne prilagodbe i dalje su bile moguće, ali trebalo ih
je zabilježiti i usporediti s planom. Tako čitatelj može provjeriti kada je
odluka donesena i što je promijenila.

**Reproducibilnost** je mogućnost da druga osoba iz istih podataka, materijala i
opisanoga postupka ponovno dobije iste rezultate i utvrdi gdje su nastali.

Pri reproduciranju ponovno izvodimo račun iz istih podataka i materijala.
[Replikacija]{.pojam def="Nova studija koja istu ciljnu tvrdnju provjerava
novim podacima i dovoljno usporedivim postupkom." en="replication" ch="12"}
jest nova studija koja istu ciljnu tvrdnju provjerava novim podacima i dovoljno usporedivim postupkom. Reproduciranjem možemo ponoviti i račun temeljen na
lošem mjerenju. Replikacija pak može dati drukčiji rezultat zbog uzoračke
promjenjivosti ili konteksta. Obje provjere pridonose prosudbi zaključka, zajedno s procjenom mjerenja, nacrta i konteksta.

## Replikacija kao kumulativno mjerenje

Da bismo procijenili što smo naučili iz replikacije, trebamo usporediti
rezultate laboratorija na istoj ljestvici. Služimo se podacima iz objavljenog
izvještaja, u kojem svaki laboratorij daje procjenu razlike između dvaju načina
držanja olovke i njezin interval (Wagenmakers, 2016). Laboratorij tako postaje jedinica usporedbe.

Svaki od 17 laboratorija daje procjenu i interval na istoj ljestvici
(Wagenmakers, 2016). Devet procjena bilo je pozitivno, ali nijedan interval
nije bio u cijelosti iznad nule (Wagenmakers, 2016). Samo dva intervala
obuhvatila su izvornu razliku od 0,82 boda (Wagenmakers, 2016). Podjela na
devet „uspješnih” i osam „neuspješnih” replikacija zanemarila bi veličinu i
nesigurnost tih procjena.

Objedinjena procjena sažima prosječnu razliku u replikacijama provedenima
prema zajedničkom protokolu. Vrijednost 0,03 uz interval od −0,11 do 0,16
uskladiva je s malim razlikama u oba smjera (Wagenmakers, 2016). Interval ne
obuhvaća vrijednosti blizu izvornih 0,82 boda. To ograničava povjerenje u
prijenos izvorne veličine na ovaj postupak, ali ne isključuje svaki mali
učinak ni druge načine mjerenja facijalne povratne sprege (Wagenmakers, 2016).

Najprije zato čitamo istraživačko pitanje i nacrt, zatim pojedinačne procjene
i intervale, pa objedinjeni rezultat. Razlike među laboratorijima mogu
potjecati od uzorkovanja, lokalnog konteksta, mjerenja ili provedbe. Ovdje možemo opisati rezultate i oprezno ih prenijeti na usporedive postupke. Utvrđivanje uzroka razlika zahtijevalo bi dodatno istraživanje.

## Cijeli zapis u forest plotu

Procjene i intervale svih laboratorija lakše ćemo usporediti ako ih vidimo
zajedno. Na prikazu [forest plot]{.pojam def="Prikaz procjena i njihovih intervala iz
više studija, uz odvojenu objedinjenu procjenu i jasno označenu referentnu
vrijednost." en="forest plot" ch="12"} svaki redak predstavlja jedan
laboratorij. Točka označuje procijenjenu razliku, a vodoravna crta njezin
95-postotni interval. Puna okomita crta označuje nulu, odnosno jednake
prosječne ocjene. Isprekidana crta na 0,82 prikazuje izvornu procjenu za
usporedbu (Wagenmakers, 2016). Služi kao vanjska referenca uz laboratorije uključene u objedinjavanje.

Oznaka `smile` u izvornim podacima znači držanje olovke zubima, a `pout`
držanje usnama (Wagenmakers, 2016). Pozitivna razlika `smile − pout` znači da je
skupina s olovkom među zubima dala višu prosječnu ocjenu stripovima.

Pogledajmo prvo kako nastaje jedna točka. Tablica izdvaja prve tri
laboratorijske usporedbe iz provjerenog izvornog poretka. Brojnosti su u
osobama, a sredine na ljestvici ocjene stripova od 0 do 9 (Wagenmakers, 2016).

*Slika. Skupne sredine prije laboratorijske razlike. Izrada autora iz lokalne rekonstrukcije prema @wagenmakers2016.*

U prvom laboratoriju od `r hr_broj(w12_rrr$mean_smile[1], 3)` oduzimamo
`r hr_broj(w12_rrr$mean_pout[1], 3)` i dobivamo približno
`r hr_broj(w12_rrr$raw_mean_difference[1], 3)` boda (Wagenmakers, 2016). Razlika postaje položaj
točke. Raspršenost ocjena i broj osoba u objema skupinama određuju njezinu
standardnu pogrešku i interval. Za račun čuvamo nezaokružene sažetke. Razlika dviju prikazanih zaokruženih sredina zato može odstupati od zaokružene razlike.

Metaanaliza je objedinjavanje usporedivih rezultata više istraživanja.
Ovdje odgovara na drugo pitanje, kolika je prosječna razlika kroz
laboratorije. Njihove procjene množimo težinama i zbrajamo. Težine ovise o
nesigurnosti pojedine procjene i procijenjenoj varijabilnosti među
laboratorijima, pa svaki sudionik i svaki laboratorij nemaju automatski
jednaku težinu. U razrađenom primjeru pokazat ćemo kako model slučajnih učinaka određuje te
težine. U našoj rekonstrukciji sirove sinteze prvi laboratorij nosi
`r hr_broj(100 * w12_sirova$tezine[1], 1)` % ukupne težine (Wagenmakers, 2016). Svih 17 težina
zbraja se na 100 %, a izvorni pokus iz 1988. nije među njima
(Wagenmakers, 2016). Slika povezuje tako dobivene procjene i intervale.

*Slika. Procjene sirove razlike smile − pout i 95-postotni intervali u 17 laboratorija. Objedinjena procjena RRR-a iznosi 0,03 [−0,11; 0,16], a isprekidana crta označuje izvornu procjenu 0,82, koja ne ulazi u sintezu. Izrada autora iz lokalne rekonstrukcije službenoga arhiva prema @wagenmakers2016.*

Točke se nalaze oko nule i svi je intervali presijecaju (Wagenmakers, 2016).
Objedinjena procjena ima uži interval jer koristi informacije iz više
laboratorija. I dalje se odnosi na laboratorije i postupak uključene u ovaj
RRR. Značenje prikaza možemo čitati iz položaja, duljine crta i oznake
objedinjene procjene i u crno-bijelom tisku.

Razlike smo dosad izrazili u bodovima ocjene stripova. Iz prethodnog poglavlja
znamo da ih možemo izraziti i u jedinicama standardne devijacije, pa želimo
provjeriti ovisi li tumačenje o tom izboru. Provjera [osjetljivosti]{.pojam def="Provjera mijenja li se sadržajni
zaključak kada se primarna analiza usporedi s jednom unaprijed obranjivom
alternativom." en="sensitivity analysis" ch="12"} uspoređuje sirovu razliku s
Cohenovim *d*. U našoj standardiziranoj rekonstrukciji iz objavljenih
laboratorijskih sažetaka procjena iznosi `r hr_broj(w12_standardna$procjena, 2)`,
uz interval od `r hr_broj(w12_standardna$donja, 2)` do
`r hr_broj(w12_standardna$gornja, 2)`. Objavljena sirova procjena iznosila je
0,03, uz interval od −0,11 do 0,16 (Wagenmakers, 2016). Razlikujemo objavljeni
rezultat od vlastitoga preračuna. Obje analize koriste iste laboratorije, ali
standardizacija mijenja ciljanu veličinu i relativni doprinos laboratorija.
Sadržajni zaključak ostaje sličan. Procjene su blizu nule i intervali
obuhvaćaju male vrijednosti u oba smjera. Ovom usporedbom provjeravamo ovisi
li zaključak o izboru mjerila.

## Reforma redoslijeda i vidljivosti

[Predregistracija]{.pojam def="Vremenski označeno bilježenje istraživačkoga
pitanja, ishoda i glavne analize prije uvida u podatke koji mogu utjecati na
te odluke." en="preregistration" ch="12"} jest vremenski označen zapis pitanja, ishoda i glavne analize prije uvida u podatke koji bi mogli utjecati na te odluke. Omogućuje razlikovanje planiranih
analiza od onih potaknutih podacima. Neočekivane obrasce možemo istraživati,
ali ih trebamo označiti kao naknadne, istraživačke analize. Potvrđujuća (konfirmatorna) analiza
provjerava unaprijed određenu tvrdnju. Istraživačka (eksploratorna) analiza
traži obrasce i oblikuje nova pitanja. U ovom RRR-u unaprijed su
pripremljeni i kod i ogledni prikazi. Dobiveni rezultat zato možemo usporediti
s postupkom koji je bio vidljiv prije podataka (Wagenmakers, 2016).

[Registrirani izvještaj]{.pojam def="Format u kojem se istraživačko pitanje i
metoda vrednuju prije nego što je glavni rezultat poznat, a konačni se rad
ponovno procjenjuje nakon provedbe." en="registered report" ch="12"} mijenja
redoslijed uredničke procjene. Urednik i recenzenti razmatraju pitanje i
metodu prije nego što znaju je li nalaz velik, nov ili značajan
(Wagenmakers, 2016). U ovom slučaju povezani su službeni članak, projekt, plan,
kod i podaci. To je omogućilo neovisnu provjeru laboratorijskih procjena
(Wagenmakers, 2016).

Kad želimo da drugi provjere istraživanje, trebamo im pokazati kako
smo došli do rezultata, a pritom sačuvati privatnost ljudi koji su u njemu
sudjelovali i poštovati uvjete uporabe materijala. Za naše je usporedbe
dovoljno imati rezultate pojedinih laboratorija. U knjigu smo zato
uključili samo izvedene sažetke na toj razini, iz kojih se sudionici ne
mogu prepoznati. Pojedinačne odgovore, službeni kod, plan i izdavačev graf
nismo preuzeli. Uz prikaz razlikujemo što možemo provjeriti ovdje, a za
što se trebamo vratiti službenom izvoru.

Tvrdnje razlikujemo prema tome opisuju li, povezuju, uopćavaju, predviđaju,
objašnjavaju uzrok ili podupiru odluku. Ovaj RRR omogućuje opis i usporedbu
eksperimentalnih uvjeta, ograničen prijenos na provedene postupke te procjenu
težine izvornog nalaza. Ne daje alat za predviđanje ni objašnjenje uzroka
razlike između izvornog i replikacijskog rezultata.

Prije prihvaćanja zaključka provjeravamo jedinicu opažanja, izostavljene
jedinice, ciljanu veličinu i vrstu tvrdnje. Pitamo koju nesigurnost interval
uključuje, mijenja li razumna alternativa zaključak i tko snosi posljedice
pogreške. Reformirani postupci trebaju te odgovore učiniti dostupnima za provjeru, a njihovu kvalitetu zatim procjenjujemo na temelju priloženih dokaza.

Priča o izrazu lica nastavila se i nakon replikacije s olovkom. Suradnja
Many Smiles okupila je istraživače različitih polazišta u unaprijed
registriranom istraživanju s 3.878 sudionika iz 19 zemalja
(Coles, 2022). Usporedili su više načina izazivanja izraza lica. Oponašanje
osmijeha i namjerno pomicanje mišića lica pružili su potporu utjecaju na
osjećaj sreće, dok su nalazi za olovku u ustima bili manje uvjerljivi
(Coles, 2022). Različiti postupci nisu dali jednak odgovor.

Na početno pitanje sada možemo odgovoriti preciznije. Slabija potpora
učinku pri ponavljanju traži promjenu uvjerenja o tom postupku i veličini njegova
učinka. Drukčija manipulacija otvara zasebnu provjeru, s vlastitim ishodom
i ograničenjima. Ocjena zabavnosti stripa i procjena vlastite sreće nisu
ista mjera. Istraživanje napreduje kada tu razliku pretvorimo u jasno
pitanje, unaprijed dogovorimo provjeru i dopustimo da nas rezultat iznenadi.

## Interakcija — Pješčanik p-hakiranja

Sljedeći prikaz pokazuje što se događa kada, uz odsutnost učinka, povećavamo
broj analitičkih putova. Više ishoda, podskupina ili trenutaka provjere daje
više prilika za rezultat ispod praga. Usporedba s korigiranim pragom pokazuje
kako uzeti u obzir cijelu obitelj analiza.

Za ovu zasebnu nastavnu simulaciju izravno generiramo p-vrijednosti. Pod idealiziranim nultim
modelom svaki put daje neovisan broj jednoliko raspoređen između nule i
jedinice. Jedno zamišljeno istraživanje s tri puta moglo bi dati 0,21,
0,03 i 0,54. To je namjerno sastavljen primjer. Ako prijavimo najmanji
broj, 0,03 prolazi prag 0,05 iako u modelu učinka nema. Za unaprijed
zadana tri puta korigirani prag bio bi $0,05/3$, koji taj broj ne prolazi.

Prikaz provodi isti odabir najmanje vrijednosti za 1, 12 i 48 putova.
Za svaki broj putova generiramo 5 000 cijelih istraživanja. Na svakom
pragu brojimo istraživanja čija je najmanja p-vrijednost ispod ili na
pragu i dijelimo s 5 000. Svi rezultati su definirani i ulaze u račun.
Visina krivulje zato prikazuje rizik barem jednoga lažnog nalaza po
istraživanju, a ne postotak pogrešnih testova među svim provedenim testovima.

Simulacija pretpostavlja neovisne putove, pravilno kalibrirane p-vrijednosti
pod nultim modelom i unaprijed određen skup analiza. Stvarne analize često
koriste iste podatke, pa krivulja može izgledati drukčije. Korekcija za
poznati skup analiza ne rješava skrivene odluke ni neprijavljeno
prilagođavanje postupka podacima.

*Slika. Udio simuliranih istraživanja s barem jednim rezultatom ispod odabranog praga nakon pretraživanja više neovisnih analitičkih putova.*

Ako unaprijed određeni broj putova označimo s $m$, prag $0{,}05/m$ dijeli
dopušteni ukupni rizik među njima. Svaka analiza mora zadovoljiti stroži prag.
To je Bonferronijeva korekcija. Razinu 0,05 dijelimo brojem usporedbi u unaprijed određenoj obitelji. O obitelji testova više ćemo govoriti u poglavlju Više grupa. Takva korekcija ograničava rizik lažnih nalaza u unaprijed određenom skupu
analiza, ali ne uklanja sve probleme analitičke fleksibilnosti.

**Što isprobati.**

1. Provedite jednu unaprijed određenu analizu.
2. Dodajte ishode, a podskupine i trenutke provjere ostavite jednakima.
3. Dodajte podskupinske inačice i trenutke provjere bez promjene broja ishoda.
4. Usporedite nominalni prag 0,05 s pragom korigiranim za sve putove.

Kada odaberemo najmanju p-vrijednost nakon pretraživanja, trebamo opisati kako
smo do nje došli. Tumačenje mora uzeti u obzir cijeli postupak odabira i
moguće analize.

**Statistika u divljini.**
**Sedamnaest procjena nije referendum.** Nakon ponavljanja pokusa
s olovkom i procjenom duhovitosti crteža trebalo je odlučiti što
zajednički rezultati govore o izvornom nalazu. Prema izvještaju o replikaciji, devet je laboratorija dalo pozitivnu,
a osam negativnu točkastu procjenu (Wagenmakers, 2016). Kad bismo
prebrojili samo predznake, mogli bismo zaključiti da su dokazi
gotovo ravnomjerno podijeljeni.

Takvo prebrojavanje svakoj procjeni daje ulogu glasa za ili
protiv. Mala razlika neposredno iznad nule tada vrijedi jednako
kao velika, precizno procijenjena razlika. Nestaju i veličina
i nesigurnost nalaza, upravo informacije zbog kojih je
ponavljanje više laboratorija korisno.

U ovom slučaju nijedan laboratorijski interval nije bio u
cijelosti iznad nule, a samo su dva obuhvaćala izvornu razliku
od 0,82 boda (Wagenmakers, 2016). Objedinjena procjena iznosila
je 0,03 boda, uz 95-postotni interval od −0,11 do 0,16
(Wagenmakers, 2016). Te brojke govore nešto određenije od
raspodjele pozitivnih i negativnih predznaka. Pod uvjetima
zajedničkog postupka ne podupiru ponavljanje izvorno velike
razlike, a ostavljaju nesigurnost oko malih razlika u oba smjera.

Za istraživača koji odlučuje na čemu graditi sljedeći pokus
to znači da treba promijeniti očekivanje o veličini nalaza.
Polaznu vrijednost za planiranje treba procijeniti u svjetlu novih, znatno manjih procjena. Rezultat pritom pripada određenoj manipulaciji, mjerenju i protokolu. Drugi načini povezivanja izraza lica s doživljajem ostaju predmet zasebnih provjera.

Pojedinačne procjene zato čitamo uz objedinjenu, a razlike
među laboratorijima ne pretvaramo u objašnjenja bez dodatnih
dokaza. Uži zajednički interval nije prognoza točne vrijednosti
sljedeće replikacije. Korist ponavljanja ovdje je u tome što
sužava raspon uvjerljivih tvrdnji. Umjesto pitanja koliko je
laboratorija glasovalo za učinak, možemo pitati koliko velik
učinak njihov zajednički rad još dopušta.

Unaprijed vidljiv plan omogućuje nam provjeru istraživačkih odluka. U sljedećem
obrazloženju procijenimo što na temelju samog postojanja takva plana možemo
zaključiti o valjanosti nalaza.

**Nađite grešku.**
Za bilješku o ponavljanju pokusa s izrazom lica asistent je izdvojio
sljedeće podatke. RRR je unaprijed odredio glavni ishod, pravila
uključivanja i primarnu analizu (Wagenmakers, 2016). Objedinjena razlika
u ocjenama stripova iznosi 0,03 boda, uz 95-postotni interval od −0,11 do 0,16
(Wagenmakers, 2016).

Urednički zapis navodi da su plan i završni izvještaj dostupni, ali ih
urednik još nije usporedio. To je zamišljena situacija pregleda ovoga
rada, a ne tvrdnja o propustu njegovih autora. Asistent predlaže bilješku.

> Glavni ishod i analiza određeni su prije uvida u rezultate.
> Objedinjena procjena blizu je nule, uz interval koji dopušta male
> razlike u oba smjera. Predregistracija je zato dovoljan razlog da
> prihvatimo zaključak bez usporedbe provedene analize s planom.

Napišite uredniku što iz bilješke može zadržati, a koji korak pregleda
još treba obaviti. Predložite jednu konkretnu usporedbu plana i završnog
izvještaja te napišite zamjenu posljednje rečenice. Ne pretpostavljajte
da provjera mora otkriti odstupanje.

## Razrađeni primjer

Dosadašnji zaključak počiva na razlici izraženoj u bodovima ocjene stripova.
Provjerit ćemo ostaje li sadržajno sličan kada iste laboratorijske rezultate
izrazimo standardiziranom razlikom. Prije te usporedbe trebamo potvrditi da
obje analize polaze od istih provjerenih zapisa. Službeni arhiv sadrži
sudioničke zapise iz 17 laboratorija, koje knjiga ne redistribuira
(Wagenmakers, 2016). Iz njih je neovisnom provjerom izvedena tablica grupnih
sažetaka, procjena i intervala. Redci se zbrajaju na 1.894 sudionika i
odgovaraju objavljenim sažetcima, uz jedno odstupanje u zaokruživanju
standardne devijacije koje ne koristimo u tvrdnjama knjige (Wagenmakers, 2016).

Tablicu možemo provjeriti bez pisanja koda. Svaki redak predstavlja
laboratorij, a `n` broj uključenih sudionika. Interval pripada sirovoj
razlici prosječnih ocjena između skupina koje su olovku držale zubima
(`smile`) i usnama (`pout`).

*Slika. Sirove laboratorijske procjene iz RRR-a. Izrada autora iz lokalne rekonstrukcije službenoga arhiva prema @wagenmakers2016.*

Pri standardizaciji svaku laboratorijsku razliku dijelimo združenom
standardnom devijacijom dviju skupina u tom laboratoriju. U prvom laboratoriju
`r hr_broj(w12_rrr$raw_mean_difference[1], 3)` boda tako postaje
$d = `r hr_broj(w12_rrr$cohen_d[1], 3)`$. Mijenjaju se mjerna jedinica,
standardna pogreška i težina, a sudionici i smjer oduzimanja ostaju isti.
U obje analize zadržavamo svih 17 laboratorija.

Za objedinjavanje koristimo model slučajnih učinaka. Težina laboratorija
prije normalizacije iznosi $w_i=1/(SE_i^2+\tau^2)$, gdje $SE_i$ opisuje
nesigurnost njegove razlike, a $\tau^2$ procijenjenu varijancu razlika među
laboratorijima. Postupak REML procjenjuje tu drugu varijancu iz svih
laboratorijskih sažetaka. Veći laboratorij zato ne mora dobiti težinu
razmjernu samo broju sudionika. Objavljena sirova analiza i naša
standardizirana rekonstrukcija imaju različite jedinice i težine.

Sljedeća tablica prikazuje obje rekonstrukcije iz istih 17 laboratorija.
Intervali su normalni Waldovi intervali. Procjeni dodajemo i od nje
oduzimamo $1,96\sqrt{1/\sum_i w_i}$. Taj račun tretira procijenjenu
među-laboratorijsku varijancu kao zadanu, pa ne obuhvaća svu njezinu
nesigurnost. U ovome poglavlju učimo čitati sintezu. Procjena REML-a nije
zadatak za ručno računanje.

*Slika. Autorska rekonstrukcija dviju sinteza iz laboratorijskih sažetaka prema @wagenmakers2016. Standardizirani redak nije zasebno objavljeni nalaz.*

Sirova procjena iznosi `r hr_broj(w12_sirova$procjena, 2)`, uz interval od
`r hr_broj(w12_sirova$donja, 2)` do `r hr_broj(w12_sirova$gornja, 2)`.
Standardizirana rekonstrukcija iznosi `r hr_broj(w12_standardna$procjena, 2)`,
uz interval od `r hr_broj(w12_standardna$donja, 2)` do
`r hr_broj(w12_standardna$gornja, 2)`. U laboratorijskoj tablici ima
`r sum(w12_rrr$raw_mean_difference > 0)` pozitivnih procjena,
`r sum(w12_rrr$raw_ci_low > 0)` intervala u cijelosti iznad nule i
`r sum(w12_rrr$raw_ci_low <= 0.82 & w12_rrr$raw_ci_high >= 0.82)` intervala
koja obuhvaćaju 0,82. Ta brojanja opisuju raspored procjena. Zaključak temeljimo na njihovoj veličini i nesigurnosti.

Prema zajedničkom protokolu prosječna razlika u replikacijama bila je blizu
nule i mnogo manja od izvornih 0,82 boda (Wagenmakers, 2016). Sirovi i
standardizirani interval iz naše rekonstrukcije obuhvaćaju male razlike u oba smjera. Zaključak se odnosi na ispitani način mjerenja facijalne povratne sprege. Uzroci razlika među procjenama i eventualni utjecaj predregistracije zahtijevali bi zasebne usporedbe osmišljene upravo za ta pitanja.

Takav zaključak povezuje opaženi rezultat s provedenim postupkom. Pri odluci o
težini izvornog nalaza uzimamo u obzir obje analize, uz navedene granice
prijenosa.

## Od testa do provjerljivog zaključka

Sada možemo zajedno razmotriti nulti model, veličinu učinka, interval,
posljedice pogreške i način odabira analize. Dokumentirani postupak omogućuje
provjeru tih dijelova. I dalje trebamo posebno opravdati uzročni zaključak,
predviđanje ili prijenos na drugo okruženje.

U tablici su odgovori na šest pitanja za višelaboratorijski RRR i njegove
dvije analize (Wagenmakers, 2016). Povezuju rezultat s jedinicom, postupkom i
dopuštenim zaključkom.

| Revizijsko pitanje | Primjena na provjereni zapis |
|---|---|
| Koja je jedinica? | zapis za jedan laboratorij sa sažetkom razlike između eksperimentalnih uvjeta i njezine nesigurnosti |
| Tko ili što nedostaje? | ljudi izvan uključenih uzoraka, drugi laboratoriji i drukčije operacionalizacije facijalne povratne sprege |
| Koji je cilj tvrdnje? | prosječna razlika ocjena između uvjeta u zajedničkom postupku, opisana sirovom i standardiziranom sintezom |
| Gdje je neizvjesnost? | preciznost laboratorijskih i objedinjenih procjena. Ne obuhvaćaju sve probleme mjerenja, odabira i provedbe |
| Koje drugo objašnjenje ostaje? | standardizacija mijenja ciljanu veličinu i doprinos laboratorija, pa rezultate uspoređujemo sadržajno |
| Tko snosi posljedice? | istraživači, urednici i čitatelji koji procjenjuju koliko vjerovati izvornom nalazu |

: Šest revizijskih pitanja primijenjenih na provjereni RRR. Izrada autora prema wagenmakers2016.

Karta tvrdnji u nastavku pokazuje što iz ove analize možemo prenijeti i gdje
su granice pojedine tvrdnje.

| Dimenzija tvrdnje | Što ovaj dokaz dopušta |
|---|---|
| opis | opisuje laboratorijske procjene, intervale i dvije objedinjene analitičke grane |
| povezanost | povezuje prosječnu ocjenu s eksperimentalnim uvjetom u provedenom postupku |
| generalizacija | oprezno prenosi zaključak na usporedive provedene postupke, ne na svaku populaciju ili operacionalizaciju |
| predviđanje | nije poduprto jer analiza ne gradi ni provjerava pravilo za novi laboratorij ili novoga sudionika |
| uzročnost | ne podupire uzročno objašnjenje razlike između izvorne i replikacijskih procjena |
| odluka | podupire opreznije odmjeravanje težine izvorne procjene uz obje grane i njihove intervale |

: Šest dimenzija tvrdnje na granici Dijela IV. Izrada autora prema wagenmakers2016.

Na kraju dijela provjerite četiri povezane teme. Zašto p-vrijednost ne daje
vjerojatnost nulte hipoteze, a nalaz blizu nule ne dokazuje njezinu
istinitost? Kako čitamo učinak i interval te zašto opaženi učinak nije
neovisan ulaz za naknadnu provjeru snage? Kako pretraživanje analiza mijenja
tumačenje najmanje p-vrijednosti? Koji dokumenti omogućuju provjeru rezultata
i gdje bi zaključak prekoračio doseg nacrta?

U idućim analizama uvijek ćemo navesti ciljanu tvrdnju, primarni postupak,
jednu razumnu alternativu, podrijetlo podataka i ograničenja. Počinjemo
kategoričkim tablicama. Prije hi-kvadrat testa trebamo utvrditi koga smo
prebrojili, što predstavlja ćelija, koji je nazivnik svakog postotka i kakvu
razliku smatramo sadržajno važnom.

## Sažetak

Nalaz možemo procijeniti tek kada uz završni račun vidimo kako su podaci
prikupljeni, pripremljeni i analizirani te kako je rezultat odabran za objavu.
P-hakiranje i račvajući putovi upozoravaju na različite oblike ovisnosti
analize o podacima, zbog kojih je važan zapis trenutka i razloga odluke.
Reproduciranjem provjeravamo račun na istom materijalu, a replikacijom
prikupljamo nove podatke za usporedbu. U višelaboratorijskom primjeru čitanje
procjena i intervala dalo je više od brojanja predznaka, a sirova i
standardizirana analiza poduprle su sličan, ograničen zaključak o razlici blizu
nule. Predregistracija, registrirani izvještaji i otvoreni materijali čine
takvu provjeru dostupnijom, iako sami ne jamče dobro mjerenje ni valjan
zaključak. U sljedećim analizama zato ćemo uz metodu pratiti i odluke koje su
nas do nje dovele.

## Pojmovi

potvrđujuća analiza (*confirmatory analysis*), istraživačka analiza (*exploratory analysis*),
p-hakiranje (*p-hacking*), vrt račvajućih putova (*garden of forking paths*),
publikacijska pristranost (*publication bias*), analitička fleksibilnost
(*analytical flexibility*), reproducibilnost (*reproducibility*), replikacija
(*replication*), forest plot (*forest plot*), provjera osjetljivosti (*sensitivity
analysis*), predregistracija (*preregistration*), registrirani izvještaj
(*registered report*)

## Zadaci

### Konceptualni

Istraživač je nakon pregleda podataka iskušao pet pravila isključivanja i
objavio jedino ono koje je dalo poželjan rezultat. Druga je istraživačica prije
analize odlučila „upotrijebit ću medijan ako je raspodjela jako asimetrična, a
sredinu inače” i zatim provela samo odabranu granu. Objasnite koji primjer
prikazuje p-hakiranje, a koji vrt račvajućih putova. Za svaki navedite koji bi
trag postupka čitatelju omogućio provjeru i pokažite gdje se u primjeru nalazi
analitička fleksibilnost (Simmons, 2011; Gelman, 2013). Na kraju jednom rečenicom
razlikujte reproducibilnost takve provjere od replikacije koja bi prikupila nove
podatke.

### Računski

Koristite samo tiskanu tablicu laboratorijskih procjena, bez pisanja koda.
Prebrojite koliko je od
17 točkastih procjena veće od nule i izračunajte taj udio u postocima
(Wagenmakers, 2016). Zatim prebrojite koliko je 95-postotnih intervala u cijelosti
iznad nule i koliko ih obuhvaća izvornu procjenu 0,82 (Wagenmakers, 2016).
Napišite dvije rečenice koje objašnjavaju zašto prvi udio nije stopa „uspjelih
replikacija”.

### Kritički

Vratite se definiciji intervala iz poglavlja Procjena i logici nultoga modela iz poglavlja Logika testiranja. Forest plot temelji se na objavljenoj replikaciji (Wagenmakers, 2016). Zamislite sljedeći pogrešan komentar. „Niti jedan laboratorij nije dobio značajan rezultat, pa je dokazano da učinak ne postoji.” Revidirajte tu tvrdnju u tri rečenice. Uključite objedinjenu
procjenu s intervalom, objasnite što nula u prikazu znači, usporedite primarnu
analizu sa standardiziranom granom provjere osjetljivosti te navedite jednu
populacijsku ili kontekstualnu granicu koju forest plot ne uklanja. Dodajte
jednu rečenicu o tome kako bi publikacijska pristranost promijenila tumačenje
sinteze kada nevidljive studije ovise o rezultatu.

### Revizija modela

Revidirajte analizu iz okvira o pogrešci. Predajte zapis s četiri polja. U
prvome prepišite provjerene brojke, u drugome označite jedinu pogrešnu tvrdnju,
u trećemu napišite ispravljeni zaključak, a u četvrtome navedite koji biste
dokument ili redak postupka provjerili prije prihvaćanja analize i objasnite
koju dodatnu vidljivost daje registrirani izvještaj. Ne traži se novi kod.
