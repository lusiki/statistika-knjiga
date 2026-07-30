# Kategorički podaci

> Iz knjige: Osnove statistike za društvene znanosti
> Autori: Luka Šikić
> Izvor: https://lusiki.github.io/statistika-knjiga/chapters/13-kategoricki-podaci.html
> Tekstualna verzija poglavlja za korištenje s AI-asistentima.
> Generirano: 2026-07-30 · © 2026 Luka Šikić. Tekst za osobno i obrazovno korištenje uz navođenje izvora.

---

| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 5 min | Očekivano i opaženo | UCBAdmissions | pogl. 4, 7, 10 |

**Vinjeta.**
Berkeleyjski podaci mogu se zapisati kao tablica frekvencija. Redovi označuju
ishod prijave, stupci spol, a svaka ćelija broj prijava (Bickel, 1975). Zbirna
tablica pokazuje razliku, ali ne govori koje su ćelije najviše odstupile od
onoga što bismo očekivali kada bi dvije varijable bile nepovezane.

Hi-kvadrat postupak upravo tu počinje. Ne pita jesu li svi postoci jednaki,
nego uspoređuje opažene brojeve s brojevima koje proizvode rubni zbrojevi pod
modelom nezavisnosti.

Kako iz tablice brojanja prepoznati gdje se nalazi veza i koliko je ona snažna?

## Opaženo prema očekivanom

Kategorički podaci počinju frekvencijama i udjelima. Frekvencija govori koliko
je jedinica u ćeliji, a udio je stavlja u odnos prema jasnom nazivniku.
Kontingencijska tablica prikazuje zajedničku raspodjelu dviju kategoričkih
varijabli. Postoci po retku i postoci po stupcu odgovaraju na različita pitanja.

Model nezavisnosti čuva rubne zbrojeve i raspoređuje ih kao da pripadnost jednoj
kategoriji ne mijenja raspodjelu druge. **Hi-kvadrat statistika** zbraja
standardizirana odstupanja opaženih od očekivanih frekvencija. Veliko
odstupanje pokazuje neusklađenost s nezavisnošću, ali još ne pokazuje koje su
ćelije odgovorne.

Standardizirani reziduali vraćaju se u ćelije. Pozitivan rezidual označava više
opažanja od očekivanog, a negativan manje. Cramérovo V sažima jačinu veze na
zajedničkoj ljestvici. Test i veličina veze zato odgovaraju na odvojena pitanja.

## Granice aproksimacije

Hi-kvadrat test oslanja se na aproksimaciju koja slabi kada su očekivane
frekvencije vrlo male. Spajanje kategorija može pomoći samo ako ima sadržajno
opravdanje. Kategorije se ne smiju spojiti zato da bi rezultat postao povoljniji
ili da bi nestala teško objašnjiva skupina.

Za malu tablicu Fisherov egzaktni test računa vjerojatnost mogućih rasporeda uz
fiksne rubne zbrojeve. Njegov naziv ne znači da je svaki drugi test približno
netočan. Označava drugačiji način računanja pod nultim modelom.

Stratificirana analiza zatim pita ostaje li veza slična unutar podskupina.
Simpsonov paradoks iz prvog poglavlja vraća se u formalnijem obliku. Zbirna
tablica može miješati odnose i različitu zastupljenost slojeva
(Simpson, 1951).

## Interakcija — Očekivano i opaženo

Prikaz dopušta mijenjanje opaženih ćelija uz jednake rubne zbrojeve.
Očekivane frekvencije ostaju referentna mreža, a doprinos svake ćelije ukupnoj
statistici postaje vidljiv. Puni krug označuje opaženu frekvenciju, prazni romb
očekivanu, a broj uz njih doprinos ćelije.

*Slika. Opažene i očekivane frekvencije u tablici dva puta dva s jednakim rubnim zbrojevima.*

**Što isprobati.**

1. Postavite opažene frekvencije jednake očekivanima.
2. Pomaknite opažanja u oba smjera i provjerite ostaju li rubni zbrojevi jednaki.
3. Povećajte pomak i pratite doprinose ćelija te Cramérovo V.
4. Smanjite rubni zbroj na deset i provjerite očekivane frekvencije.

Udaljenost opaženoga od očekivanoga nosi testnu statistiku, ali položaj ćelije
nosi tumačenje. Jedan zbirni rezultat zato nije dovoljan bez reziduala i mjere
jačine veze.

**Statistika u divljini.**
**Zbirna tablica upisa.** U Berkeleyjskim podacima zbirni ishod prijave i spol
nisu raspoređeni kao pod jednostavnim modelom nezavisnosti (Bickel, 1975).
Takav rezultat opisuje povezanost u tablici, ali ne određuje mehanizam.

Raspodjela prijava po odjelima mijenja zbirni obrazac. Analiza zato treba
reziduale, veličinu veze i stratifikaciju, a ne samo jednu p-vrijednost.

**Pitajte model.**
Asistent može izraditi kontingencijsku tablicu, očekivane frekvencije i
reziduale. Treba provjeriti koji je nazivnik koristio za postotke, jesu li
očekivane ćelije dovoljno velike i je li uz test izvijestio veličinu veze.
Modeli često značajnu povezanost opisuju kao snažnu.

> Prikaži frekvencije i postotke s jasnim nazivnikom, izračunaj očekivane
> frekvencije i standardizirane reziduale te uz test navedi Cramérovo V.

**Nađite grešku.**
Očekivane frekvencije zadovoljavaju uvjete, a hi-kvadrat test pokazuje
neusklađenost s nezavisnošću. Reziduali otkrivaju ćelije koje najviše
doprinose. Budući da je rezultat značajan, veza je snažna.

Greška je zaključak o snazi veze iz statističke značajnosti. Jačina se
procjenjuje mjerom poput Cramérova V i čita u sadržajnom kontekstu.

## Razrađeni primjer

Ugrađeni podaci `UCBAdmissions` omogućuju reprodukciju zbirne tablice
Berkeleyjskog slučaja (Bickel, 1975). Analiza najprije zbraja odjele i stvara
tablicu ishoda prema spolu. Zatim uspoređuje opažene i očekivane frekvencije.

*Slika. Opažene frekvencije u zbirnim podacima o prijavama. Izrada autora prema @bickel1975.*

Test sažima neusklađenost zbirne tablice s nezavisnošću. Povratak odjelima
pokazuje da taj rezultat miješa više slojeva. Statistički korektan izvještaj
zato ne preuzima kauzalni jezik i ne zaustavlja se na zbirnoj tablici.

## Sažetak

Kategorički podaci traže jasno brojanje i nazivnike prije testiranja. Hi-kvadrat
uspoređuje opažene i očekivane frekvencije, reziduali vraćaju zaključak u
ćelije, a Cramérovo V opisuje jačinu veze. Male očekivane frekvencije i skriveni
slojevi ograničavaju jednostavno čitanje. Sljedeće poglavlje istu logiku
usporedbe prenosi na brojčani ishod i dvije skupine.

## Pojmovi

kontingencijska tablica (*contingency table*), očekivana frekvencija (*expected
frequency*), hi-kvadrat test (*chi-squared test*), standardizirani rezidual
(*standardized residual*), Cramérovo V (*Cramér's V*), Fisherov egzaktni test
(*Fisher's exact test*)

## Zadaci

### Konceptualni

Objasnite razliku između testa nezavisnosti i mjere jačine veze. Predajte dvije
rečenice koje se mogu pojaviti u istom izvještaju.

### Računski

Upotrijebite `UCBAdmissions`. Izračunajte zbirni test i zasebne tablice po
odjelima te predajte usporedbu (Bickel, 1975).

### Kritički

Prosudite što zbirna kontingencijska tablica može reći o upisima, a što gubi
bez odjela (Bickel, 1975). Predajte jedan odlomak.

### Revizija modela

Ocijenite modelsku analizu iz okvira. Izdvojite točne dijagnostičke korake,
jedan pogrešan zaključak i prikladnu mjeru koja nedostaje.
