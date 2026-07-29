# Povezanost

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/06-povezanost.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-29 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

**Vinjeta.**
Anscombeova četiri skupa imaju gotovo jednaku Pearsonovu korelaciju, iako
njihovi grafovi prikazuju različite odnose (Anscombe, 1973). Analitičar koji je
dobio samo koeficijent mogao je uredno izvijestiti o smjeru i jačini linearne
veze, a ipak propustiti zakrivljenost ili jedno opažanje koje određuje cijeli
rezultat.

Korelacija je bila točno izračunata. Nije pogriješila u računu, nego je sažela
samo jedan aspekt odnosa. Poteškoća je nastala kada je taj sažetak pročitan kao
potpuna slika.

Što koeficijent povezanosti čuva, a koje odnose ostavlja izvan kadra?

## Zajedničko kretanje

Dvije su varijable povezane kada se njihov raspored mijenja zajedno. Pozitivna
veza znači da se veće vrijednosti jedne češće pojavljuju uz veće vrijednosti
druge. Negativna veza spaja veće vrijednosti jedne s manjima druge. Slaba
linearna veza ne znači da odnosa nema jer zakrivljeni obrazac može imati
koeficijent blizu nule.

**Kovarijanca** prati zajedničko odstupanje od sredina, ali zadržava jedinice
obiju varijabli. Pearsonova korelacija standardizira taj odnos pa se kreće na
zajedničkoj ljestvici. Ona opisuje smjer i jačinu linearnog odnosa. Spearmanova
korelacija radi s rangovima i zato bolje podnosi monotone odnose i dio krajnjih
vrijednosti.

Koeficijent se uvijek čita uz raspršeni dijagram. Graf otkriva je li odnos
linearan, stvaraju li skupine lažni oblak i određuje li jedno opažanje nagib.
Matrica korelacija može sažeti mnogo parova, ali ne zamjenjuje pregled
najvažnijih odnosa.

## Granice jednog broja

Ograničenje raspona slabi korelaciju jer iz uzorka uklanja dio varijacije koja
je nosila odnos. U skupini u kojoj su svi vrlo slični teško je vidjeti obrazac
koji postoji u široj populaciji. Miješanje različitih podskupina može učiniti
suprotno i proizvesti odnos koji se unutar svake skupine smanji ili preokrene.

Povezanost ne određuje smjer uzroka. Varijabla može utjecati na drugu, smjer
može biti obrnut, obje može oblikovati treći čimbenik, a uzorak može nastati
slučajno. Statistička kontrola sužava neke mogućnosti tek uz uvjerljiv dizajn i
sadržajno obrazloženje.

## Interakcija — Pogodi korelaciju

Planirana igra prikazuje raspršene oblake bez koeficijenta i traži procjenu
smjera i jačine. Nakon odgovora otkriva broj i pokazuje primjere u kojima
ljudsko oko ili Pearsonov sažetak propuštaju nelinearnost i podskupine.

**Što isprobati.**

1. Procijenite znak jasnog linearnog odnosa.
2. Usporedite zbijeni i raspršeni oblak istog nagiba.
3. Pronađite nelinearni odnos kojem je Pearsonova korelacija blizu nule.

**Statistika u divljini.**
**Ista korelacija, različita struktura.** Anscombeov kvartet pokazuje četiri
skupa s gotovo jednakim koeficijentom, ali samo jedan približno odgovara
jednostavnom linearnom sažetku (Anscombe, 1973).

Tvrdnja o „snažnoj povezanosti" zato treba graf, opis uzorka i provjeru
utjecajnih opažanja. Koeficijent je koristan sažetak nakon tih provjera, a ne
zamjena za njih.

**Pitajte model.**
Asistent može izračunati Pearsonovu i Spearmanovu korelaciju i opisati graf.
Treba mu zatražiti provjeru linearnosti, krajnjih vrijednosti, podskupina i
ograničenja raspona. Nakon odgovora valja provjeriti jesu li redovi u dvjema
varijablama ispravno upareni i je li iz povezanosti izveden nedopušten uzrok.

> Usporedi Pearsonovu i Spearmanovu korelaciju, opiši oblik raspršenog
> dijagrama i provjeri utjecaj krajnjih opažanja. Zaključak ograniči na
> povezanost koju dizajn podupire.

**Nađite grešku.**
Raspršeni dijagram pokazuje pozitivan približno linearan odnos bez izdvojenih
točaka, a Pearsonov i Spearmanov koeficijent slični su. Zbog toga veća
vrijednost prve varijable uzrokuje porast druge.

Greška je kauzalni zaključak. Slaganje dvaju koeficijenata i uredan graf
podupiru opis povezanosti, ali ne određuju vremenski smjer ni isključuju treće
varijable.

## Razrađeni primjer

Ponovno koristimo `anscombe`, sada usmjereni na ono što koeficijent čuva.
Računamo Pearsonovu korelaciju za svaki skup i stavljamo je uz opis obrasca.
Rezultati su gotovo jednaki, dok graf iz prethodnog poglavlja pokazuje da su
mehanizmi odnosa različiti (Anscombe, 1973).

*Slika. Pearsonove korelacije Anscombeova kvarteta. Izrada autora prema @anscombe1973.*

Tablica potvrđuje da je Pearsonova korelacija vjerna linearnom sažetku koji je
izračunala. Ne potvrđuje da je linearni sažetak prikladan za svaki skup.
Ispravan izvještaj zato spaja koeficijent, graf, broj opažanja i ograničenje
dizajna.

## Sažetak

Korelacija sažima smjer i jačinu određenog oblika zajedničkog kretanja. Graf
otkriva linearnost, podskupine, ograničenje raspona i utjecajna opažanja koja
jedan koeficijent ne može nositi. Pearsonov i Spearmanov pristup odgovaraju na
različita pitanja, a nijedan sam ne dokazuje uzrok. Sljedeći dio knjige uvodi
vjerojatnost kako bismo razlikovali stabilan obrazac od onoga što može nastati
običnom promjenjivošću.

## Pojmovi

kovarijanca (*covariance*), Pearsonova korelacija (*Pearson correlation*),
Spearmanova korelacija (*Spearman correlation*), linearnost (*linearity*),
ograničenje raspona (*range restriction*), utjecajno opažanje (*influential
observation*)

## Zadaci

### Konceptualni

Nacrtajte dva različita odnosa koja mogu imati sličnu Pearsonovu korelaciju.
Predajte skicu i objašnjenje onoga što se u koeficijentu gubi.

### Računski

Upotrijebite `anscombe`. Izračunajte Pearsonovu i Spearmanovu korelaciju za
svaki skup te predajte usporednu tablicu (Anscombe, 1973).

### Kritički

Prosudite tvrdnju da jednaka korelacija znači jednaku podatkovnu priču.
Upotrijebite Anscombeov kvartet kao provjeru (Anscombe, 1973).

### Revizija modela

Ocijenite modelsku analizu iz okvira. Imenujte točne dijagnostičke provjere,
jedan nedopušten zaključak i dizajn koji bi ga mogao bolje poduprijeti.
