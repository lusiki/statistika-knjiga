# Urednički prolaz prirodnosti i jasnoće, 24. listopada 2026.

Prolaz je izveden na aktualnom radnom stablu, zajedno s prethodnim
listopadskim izmjenama. Nije vraćana posljednja Gitova revizija. Autor je
izričito zatražio postupak humanizacije i njegovu primjenu. Ovaj zapis ne
zatvara P6-VERIFY, ne mijenja status poglavlja i ne odobrava objavu knjige.

Postupak je opisan u [protokolu](../humanization-protocol.md). Polazi od
[Humanizera](https://github.com/blader/humanizer/blob/main/SKILL.md), uz
prilagodbu hrvatskom udžbeniku i pravilima `STYLE.md`; dodatni izvori
navedeni su u protokolu. Cilj je jasnije objašnjenje, bez procjenjivanja
autorstva ili pokušaja prolaska kroz detektor umjetne inteligencije.

## Opseg i izvedene izmjene

Deterministički pregled obuhvatio je svih 26 izvora iz aktualnoga poretka:
predgovor, 18 poglavlja i sedam dodataka. Neovisni kritičari pregledali su
glas i razvoj argumenta, uključujući početke, sažetke i odabrane dijelove
središnjega teksta. Urednik je detaljno pročitao izmijenjena poglavlja i
autorske dodatke te provjerio izmjene u kontekstu. To nije tvrdnja da je
svaki neizmijenjeni odlomak knjige prošao potpunu jezičnu redakturu.

| Skup izmjena | Rezultat |
|---|---|
| Poglavlje 3 | Uklonjena suvišna najava prikaza, jasnija rečenica o uredništvu i konkretniji sažetak. |
| Poglavlje 12 | Tri preklopljena prijelaza objedinjena su u jedan; sačuvana su pitanja o ćeliji, nazivniku i sadržajnoj važnosti razlike. |
| Poglavlje 18 | Neposredniji uvod i primjena pravila zaštite osoba na parlamentarne rečenice, umjesto doslovnog ponavljanja poglavlja 17. |
| Dodatak B | Osam zahvata objašnjava postupke, referentne vrijednosti i granice provjera jednostavnijim jezikom. |
| Dodatak F | Dva zahvata jasnije opisuju uporabu različitih asistenata i završni projekt. Inačica sustava navodi se kada je dostupna. |
| Katalog podataka | Tri odlomka Dodatka C i uvod stranice Podaci uređeni su kroz generator. |
| Terminološke tablice | Dodano je 19 čitateljskih objašnjenja, zajedničkih Dodatku E i mrežnom Pojmovniku. |

U prvih pet datoteka provedeno je ukupno **18 ručnih zahvata**. Zajedno s
generiranim dodacima promijenjeno je sedam od 26 knjižnih izvora te dvije
pripadajuće mrežne stranice. Broj izmjena nije bio cilj: korisna ponavljanja,
nužne ograde i ratificirano nazivlje ostali su sačuvani.

U terminološkom registru nova neobvezna polja `reader_reason` služe prikazu
objašnjenja. Nakon njihova uklanjanja registar je potpuno jednak početnom
snimku. Izvorni razlozi odluka, nazivi, iznimke, stabilne oznake i status
neovisne terminološke recenzije nisu promijenjeni. Shema i generator
podržavaju novo polje; bez njega prikazuju postojeći `reason`.

## Odvojeno osvježenje generiranih definicija

Ponovna izgradnja Dodatka E otkrila je devet definicija koje nisu pratile
postojeće listopadske izmjene poglavlja. Generator ih je uskladio s
aktualnim grafom pojmova. To su jedinica analize, operacionalizacija,
konfundirajuća varijabla, standardna devijacija uzorka, gramatika grafike,
pridruživanje, kovarijanca uzorka, Pearsonova korelacija uzorka i stopa
obiteljske pogreške.

Ovo nisu dodatne stilske prerade definicija. Svih **52 definicijskih blokova
u poglavljima identično je početnom snimku**. Provjera koncepata potvrđuje
svježinu grafa, a regenerirani Dodatak E potpuno odgovara izlazu generatora.
U terminološkim tablicama promijenjen je samo posljednji, objašnjavajući
stupac; ostali su stupci jednaki.

Opća zaštitna provjera zato za Dodatak E i dalje prijavljuje promjene
formula, brojki i strukturnih redaka. Taj nalaz nije utišan: pojedinačne
razlike i dokaz podrijetla nalaze se u strojnom zapisu. Za ostalih 25 izvora
zaštitna provjera prolazi. U autorskoj prozi nisu mijenjani podaci, brojke,
formule, citatni ključevi, kod, poveznice ni strukturne oznake.

## Neovisni pregled

Kritičari `humanization_voice` i `humanization_arc` radili su paralelno i
isključivo čitali. Završni pregled svih 18 ručnih zahvata nije utvrdio
gubitak bitnog značenja ni prekid pedagoškoga slijeda. Kritičar glasa tražio
je da protokol izričito obuhvati generirane tablice i razdvoji osvježenje
definicija od stilskog uređivanja; obje su dopune unesene. Prihvaćeno je i
pojašnjenje o dostupnosti inačice asistenta.

Sačuvani su šest revizijskih pitanja iz poglavlja 3, prijelazi prema
uzorkovanju i procjeni, razlika između reprodukcije i valjanosti, zaštita
osoba, granice uporabe jamovija te razlika između politike kolegija i
sveučilišnoga propisa. Panel nije studentsko ispitivanje razumljivosti,
neovisna statistička recenzija ni neovisna terminološka recenzija.

## Provjere

| Provjera | Rezultat |
|---|---|
| Inventar knjige, citati i uvodi u slike | Prolaze. |
| Koncepti | Prolazi: 52 definicije, graf je svjež, nema duga u registru. |
| Bookwrightov stilski linter | Nula kandidata u 26 datoteka. Nakon posljednje dorade ponovno provjereni B i F. |
| Struktura i integritet rukopisa | Prolaze. |
| Dizajnerski tokeni | Prolaze. |
| Dodaci C i E | Prolaze, uključujući ponovnu izgradnju iz izvora. |
| Tri negativne provjere Dodatka E | Sve tri odbijene kako se očekuje: prihvaćanje napuštenog oblika, ispuštanje odstupanja i preimenovanje stabilne oznake. |
| Neobvezno čitateljsko objašnjenje | Provjereni povratak na izvorni razlog, novi prikaz i odbijanje praznog polja. |
| Rute rješenja i putovi čitanja | Prolaze; 95 zapisa rješenja bez pomaka. |
| Arhitektura zadataka | Ne prolazi; svih 25 redaka nalaza potpuno je jednako početnom izvještaju. |
| Dodatak B | Ne prolazi; provjera i prije i poslije traži zapis `Luka Sikic`, dok aktualni izvor navodi `Luka Šikić`. |
| Dodatak F | Ne prolazi zbog već zatečenog zastarjelog otiska registra. |

Početni pokušaji R provjera naslijedili su nevaljanu postavku
`C.UTF-8` na Windowsu. Mjerodavni su ponovljeni rezultati s ispravnom
postavkom `en_US.UTF-8`. Nije mijenjana projektna konfiguracija R-a.
Početni stilski nalazi iz nevaljanog okruženja nisu korišteni kao dokaz
stanja rukopisa.

Četiri kontrolne datoteke comprehensive-review i `references.bib` ostali
su bajtno nepromijenjeni. Otisci nisu osvježavani samo radi prolaska provjere.

## Prikazi i preostala pitanja

HTML je uspješno izgrađen za svih 39 stranica. U izlazu su provjereni
odlomci svih 15 preoblikovanih ručnih zahvata; preostala tri zahvata su
brisanja. Svih 19 čitateljskih objašnjenja prisutno je i u Dodatku E i u
Pojmovniku. Quarto upozorava na nedostupne pakete `downlit` i `xml2` za
povezivanje naziva u kodu; to upozorenje nije prekinulo izgradnju.

Quarto je najprije naišao na nedostupan korisnički Sass cache. Uspješna
izgradnja koristila je zaseban cache u `tmp/` i izričito zadanu postojeću
korisničku R biblioteku. Te su postavke vrijedile samo za proces izgradnje.
Nisu instalirani novi paketi niti promijenjene trajne postavke sustava.

Pristup Firefoxu istekao je dok je alat čekao odobrenje aplikacije.
Vizualni pregled HTML-a u pregledniku zato nije dovršen; provjeren je
generirani tekst, što ne dokazuje izgled svih širina zaslona.

Novi [PDF](../../output/pdf/Statistika-humanized-2026-10-24.pdf) uspješno
je izgrađen od 531 stranice. Vizualno su pregledane PDF stranice 79–80,
87–88, 311–312, 444–445 i 471–472: izmijenjeni odlomci, susjedni sadržaj
i prijelomi čitljivi su, bez uočenog odrezivanja ili preklapanja. To je
pregled pogođenih mjesta, a ne nova likovna recenzija svih 531 stranice.

Otvoreni `pdf/Statistika.pdf` bio je zaključan u Acrobatu. Novi je primjerak
zato nastao u izdvojenoj kopiji izvora; svih 26 knjižnih datoteka prije
izgradnje provjereno je kao bajtno identično aktualnom radnom stablu.
Pokrenut je isključivo projektni `scripts/render-book-pdf.ps1`. Postojeći
TeX nije mogao razriješiti Windowsovu putanju unutar sandboxa, dok je isti
izvršni program izvan njega radio. Završna izgradnja provedena je u tom
provjerenom okruženju. Privremeni parametar PowerShella vrijedio je samo za
proces skripte. Otvoreni izvornik nije zamijenjen; novi je PDF spremljen
pod gornjim, zasebnim imenom. Ni HTML ni PDF nisu objavljeni na mreži.

Izvan ovoga prolaza ostaju sljedeći nalazi za kasniju reviziju:

- U poglavlju 17 izraz „osjetljivost klasifikatora” treba uskladiti s
  registrom koji kratki oblik „osjetljivost” zadržava za robusnost.
  Terminološka odluka nije donesena usputnim stilskim zahvatom.
- Dodatak A još mjestimice govori jezikom provjere i održavanja izvora;
  njegovo dodatno pojednostavnjivanje treba provjeriti uz reproducibilne
  postupke.
- Dio preostalih najava i ponavljanja u poglavljima namjerno je zadržan kao
  pomoć studentu. Daljnje skraćivanje traži čitanje čitavoga nastavnog slijeda.
- Zatečene provjere zadataka i dodataka B/F zahtijevaju zasebno usklađivanje.
  Ovaj prolaz ne daje potvrdu spremnosti za objavu.

[Strojni zapis](humanization-2026-10-24.json) čuva razlike prije i poslije, razloge uredničkih
odluka, otiske, rezultate provjera i dokaz osvježenja generiranih definicija.
Početni snimak cijeloga teksta i radni zapisi ostaju u zanemarenoj mapi
`tmp/humanization-2026-10-24/`.
