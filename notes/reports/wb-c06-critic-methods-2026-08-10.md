# WB-C06 — završno izvješće kritičara metoda

**Izvor:** `chapters/06-povezanost.qmd`

**Konačni SHA-256:**
`4b5e538138a6b385e4d970b193d2ea29e3cf71d934e2700fdf37a7e65633efa8`

Kritičar je radio neovisno i samo za čitanje te je hash potvrdio prije i nakon
pregleda. Pearsonova korelacija, kovarijanca i standardizirani zapis međusobno
su usklađeni. Ponovni račun daje $r=-0{,}559289$, a kovarijanca se pri pretvorbi
minuta u sate mijenja točno šezdeset puta. Spearmanov koeficijent ispravno je
izveden kao Pearsonova korelacija rangova, uključujući prosječne rangove za
vezane vrijednosti; oba puta daju $r_s=-0{,}680151$.

Granice su izrečene precizno. Kvadrirana korelacija tumači se samo u
jednostavnom linearnom opisu, nesigurnost je uvjetovana istim nacrtom i
usporedivim neovisnim jedinicama, a ograničenje raspona može oslabiti, pojačati
ili preokrenuti koeficijent, ovisno o obliku i selekciji. Simpsonov obrat,
ekološka pogreška i uzročna granica odvajaju zbirnu od unutargrupne veze,
državu od pojedinca i povezanost od uzroka. Regresija ostaje samo najavljena
granica kasnijega poglavlja; nema `geom_smooth`, `stat_smooth`, `lm(` ni metode
najmanjih kvadrata.

Okvir s pogreškom sada ima točno jednu pogrešku. Podskup 18–24 ima $n=90$ i
$r=0{,}180377$; jedini je promašaj prijenos toga nalaza na cijeli simulirani
uzorak. Populacijski skok više nije prisutan. Eurostatove vrijednosti
$r=0{,}449994$ i $r_s=0{,}508016$ ostaju ograničene na 27 država EU-a 2025.

## Završna ocjena

- točnost: 5/5
- pretpostavke: 5/5
- tumačenje: 5/5
- preciznost: 5/5
- fatalni / veliki / manji nalazi: 0 / 0 / 0

`R13-C06-coded-association` i `R35-REACHBACK-06` ostaju `ratified` do
zasebnoga C06.

**Verdikt:** metodološki prolaz bez otvorenoga nalaza. To nije autorsko
prihvaćanje.
