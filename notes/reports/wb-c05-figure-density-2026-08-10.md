# WB-C05 — obrazloženje gustoće slika u petom poglavlju

**Izvor:** `chapters/05-vizualizacija.qmd`

**Konačni SHA-256:**
`db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`

## Odluka

Poglavlje zadržava šest logičkih slika, odnosno gornju granicu ratificiranoga
pojasa od jedne do šest. Sedam izvornih varijanti nastaje zato što središnja
interakcija ima HTML i tiskani blizanac; to je jedna logička slika, a ne dvije.
Deterministički detektor potvrđuje šest logičkih slika, sedam varijanti i
uvodni odlomak neposredno prije svake slike.

Šest je opravdano predmetom poglavlja. Svaka slika nosi drugu odluku gramatike
grafike ili drugi način na koji prikaz može čuvati i odbacivati informaciju.
Nijedna nije ukrasna ilustracija i nijedna ne ponavlja isti nastavni posao.

| Logička slika | Nastavna uloga | Dispozicija |
|---|---|---|
| `fig-ucestalost-rijeci` | Pokazuje da prikaz tekstualne učestalosti počinje jedinicom, pravilom pretvorbe, nazivnikom i granicom generalizacije; priprema disciplinirano čitanje tekstualnih prikaza u 17. poglavlju. | Nova upravljana uloga za `R13-C05-frequency-visual`; zamjenjuje zasebnu demonstraciju prozirnosti. |
| `fig-skraceni-raspon` | Drži iste skupinske prosjeke na dvjema osima i izolira učinak početka osi na vizualni dojam. | Zadržana bez promjene uloge. |
| `fig-digikat-log` | Pokazuje zašto jako zakošena raspodjela broja objava među imenovanim domenama traži izričito označenu logaritamsku os. | Zamjenjuje okvir s brkovima i provodi točno dodijeljenu ulogu `digikat-izvori.csv`. |
| `fig-mala-polja` | Razdvaja mjesečni broj objava po platformama uz zajedničku ljestvicu te čuva siječanj, rupu od veljače do svibnja, lipanjski lom i razdoblje nakon promjene kao odvojene režime. | Retargetirana s nastavne ankete na upravljani mjesečni DigiKatov izvadak. |
| `fig-w05` s `fig-w05-print` | Jedini interaktivni nositelj poglavlja; na istim opažanjima mijenja geometriju i pokazuje što svaki izbor čuva ili sažima. | Zadržana kao jedna logička slika s obveznim tiskanim blizancem. |
| `fig-anscombe` | Sjedinjuje sažetak i vizualnu strukturu, zaključuje poglavlje i prenosi pitanje prema koeficijentu u šestom poglavlju. | Zadržana; dodan je neposredni interpretativni uvod. |

## Zakonite zamjene

`fig-rasprseni` je uklonjen jer su raspršena geometrija i gubitak strukture već
vidljivi u središnjoj interakciji, Anscombeovu kvartetu i nastavku u šestom
poglavlju. Prozirnost ostaje objašnjena u prozi, ali više ne zauzima samostalnu
sliku. Time je otvoreno mjesto za doslovni, ograničeni prikaz učestalosti riječi
bez širenja poglavlja iznad dopuštene granice.

`fig-okvir-gubi` je uklonjen jer tablica izbora prikaza i ostatak poglavlja već
izričito objašnjavaju što sažetak odbacuje. Njegovo mjesto preuzima
`fig-digikat-log`, koji ispunjava zasebnu, ranije nepokrivenu obvezu o
logaritamskoj osi na upravljanom izvatku imenovanih domena.

Izvorni `fig-mala-polja` na simuliranoj anketi zamijenjen je mjesečnim DigiKatovim
prikazom. Definicija, zajednička ljestvica i usporedba polja ostaju isti nastavni
cilj, ali novi sklop tablice i slike razdvaja broj od udjela te čuva vidljivu
granicu onoga što u 2024. nije zabilježeno. Tablica uz sliku čuva točne
vrijednosti za tisak i ne računa se kao dodatna konceptualna slika.

## Granica čitanja

Pet je slika statično i jedna je interaktivna sa statičnim blizancem. Redoslijed
je od jednostavne učestalosti i osi, preko usporedbe polja, do promjene
geometrije i završne sinteze. Poglavlje 4 ima dvije, a poglavlje 6 tri logičke
slike; veća gustoća petoga poglavlja nije predložak za susjedna poglavlja nego
posljedica njegova predmeta, vizualne pismenosti.

Daljnje spajanje učestalosti riječi, logaritamske osi ili mjesečnih polja u jednu
složenu sliku spojilo bi različite jedinice i tvrdnje. Daljnje uklanjanje ostavilo
bi jednu od četiri upravljane obveze bez vlastitoga vidljivog dokaza. Zato je
šest najmanji broj koji istodobno čuva upravljane uloge i razdvaja njihove
nazivnike, pretvorbe i granice zaključivanja.
