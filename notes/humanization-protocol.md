# Postupak uređivanja prirodnosti i jasnoće rukopisa

Verzija 2, 24. listopada 2026. Primjenjuje se na aktualne izvore knjige,
uključujući nezabilježene izmjene u radnom stablu. Mjerodavan je `STYLE.md`.
Humanizacija ovdje znači urednički rad za čitatelja. Ne utvrđuje autorstvo
teksta i ne služi postizanju rezultata na detektoru umjetne inteligencije.

## Cilj i glas

Tekst treba zvučati kao pažljivo napisan hrvatski udžbenik. Autor objašnjava
postupak studentu društvenih znanosti koji ne mora znati programirati.
Čuvamo miran, analitičan glas, autorsko „mi” i namjernu postupnost. Ne
dodajemo osobna iskustva, mišljenja, razgovorne dosjetke ni izmišljene primjere.
Upute čitatelju ostaju ondje gdje ih dopušta `STYLE.md`; završno istraživanje
zadržava svoj zajednički, postupni glas.

## Izvori i prilagodba

[Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md), pregledan
24. listopada 2026., verzija 3.1.0, služi kao popis uredničkih pitanja.
Preuzimamo pregled cjeline, popravak praznog naglašavanja i ponavljanja te
usporedbu značenja prije i poslije izmjene. Ne primjenjujemo njegove engleske
popise riječi kao hrvatski filtar. Zadržavamo hrvatske navodnike, propisane
naslove, definicije i korisna suprotstavljanja pojmova. Kod, podaci i poveznice
ne mijenjaju se u ovom prolazu.

Hrvatsko izdanje Komisijina priručnika
[Pišimo jasno](https://op.europa.eu/en/publication-detail/-/publication/725b7eb0-d92e-11e5-8fea-01aa75ed71a1/language-hr)
podsjeća da savjete treba prilagoditi svrsi teksta i njegovim čitateljima.
[Digital.gov](https://digital.gov/guides/plain-language/principles) također
polazi od publike, razumljivih riječi i provjere razumijevanja. Primjenjujemo
taj pristup uz pravila knjige. Ne pretvaramo argument u popise niti uvodimo
jednaku duljinu svih rečenica i odlomaka.

## Zaštićeni sadržaj

Stilski zahvat čuva tvrdnju, njezin doseg i uvjete. Posebno se provjeravaju
razlike između povezanosti i uzroka, procjene i poznate vrijednosti, pojedinca
i distribucije procjena te simuliranih i opaženih podataka. Riječi poput
„može”, „približno” i „uz pretpostavku” ostaju kada određuju valjanost tvrdnje.
Ne zamjenjujemo ratificirane statističke termine sinonimima radi raznolikosti.
Ponavljanje ostaje kada novi primjer traži novu primjenu istog ograničenja.

Za ovaj konzervativni prolaz ne mijenjamo brojke, formule, citatne ključeve,
citirane iskaze, nazive i adrese datoteka, tablice, naslove, definicijske
oznake, programske blokove ni vidljivost sadržaja po izdanjima. Zadatke i
namjerno pogrešne analize pregledavamo, ali ih ne popravljamo kao prozu.
Njihova izmjena zahtijeva usklađivanje s kanonskim zapisom rješenja.
Sadržajna dopuna slijedi zaseban postupak iz `ENRICHMENT.md`.

Uska iznimka dopušta jasnije objašnjenje u posljednjem stupcu generiranih
terminoloških tablica. U registru se dodaje neobvezno polje `reader_reason`;
izvorni `reason`, kanonski nazivi, dopuštene iznimke, granice značenja i
status recenzije ostaju sačuvani. Mijenja se izvor za generator, a zatim se
prikaz ponovno izgradi i provjeri. Ista se objašnjenja prikazuju u Dodatku E
i mrežnom Pojmovniku. Katalog podataka također se uređuje kroz generator.

Ako ponovno generiranje otkrije zastarjelu definiciju u izvedenom prikazu,
njezino usklađivanje s aktualnim izvorom bilježi se odvojeno od stilskog
zahvata. Svi definicijski blokovi u poglavljima moraju ostati jednaki
početnom snimku, graf mora proći provjeru svježine, a novi prikaz mora
odgovarati izlazu generatora. Opća zaštitna provjera i dalje prijavljuje
promjene formula, brojki ili strukturnih redaka: nalaz se ne utišava niti se
proglašava stilski nevažnim. Dodatni zapis dokazuje podrijetlo svake razlike.

## Redoslijed rada

1. Utvrditi aktualni opseg iz `_quarto.yml`, pročitati pravila i zabilježiti
   početno radno stablo. Ne vraćati datoteke na Gitovu posljednju reviziju.
   Provjeriti status comprehensive-review. Ovaj izričito zatraženi urednički
   prolaz ne zatvara P6-VERIFY niti mijenja status poglavlja.
2. Spremiti lokalni početni snimak i provesti postojeće provjere prije
   uređivanja. Odvojiti zatečene probleme od novonastalih. Snimak s cijelim
   tekstom ostaje u zanemarenom `tmp/`; trajni zapis čuva otiske i razlike.
3. Pročitati prozu u kontekstu i pregledati kandidate detektora. Provjeriti
   prazne najave, ponovljene završetke, apstraktne imenice, urednički žargon,
   nejasnog vršitelja radnje i jednoličan ritam. Nijedan izraz sam po sebi
   nije dokaz pogreške. Izostanak kandidata nije potvrda kvalitete.
4. Za svaki zahvat imenovati problem i preoblikovati najmanju cjelinu koja
   ga rješava. Ponovno pročitati susjedne odlomke. Ako su dvije formulacije
   jednako dobre, zadržati izvornu. Broj izmjena nije cilj.
5. Odvojeno pregledati glas i razvoj argumenta kroz Bookwrightov panel
   `critic_voice` i `critic_arc`. Kritičari su neovisni i ne pišu u rukopis.
   Urednik bilježi što prihvaća, što zadržava i zašto. Njihove ocjene nisu
   studentsko ispitivanje razumljivosti.
6. Usporediti tvrdnje prije i poslije. Pokrenuti zaštitnu provjeru, stilski
   linter, provjere citata, koncepata i uvoda u slike te primjerene provjere
   rukopisa i zadataka. Pregledati razliku prema početnom snimku, ne samo
   razliku prema Gitovu HEAD-u. Nijedan kontrolni otisak ne osvježavati samo
   zato da provjera prođe.
7. Izgraditi aktualni prikaz u HTML-u i PDF-u prema projektnim naredbama.
   PDF se gradi isključivo skriptom `scripts/render-book-pdf.ps1`.
   Pregledati izmijenjene odlomke i prijelome. Zabilježiti ograničenja provjere,
   rezultate naredbi, trag izmjena i nalaze važne za kasniji pregled.

## Naredbe

Alat samo čita i izvještava. Ne sadrži automatsko prepisivanje.

```text
python scripts/audit-humanization.py snapshot --output tmp/humanization/baseline.json
python scripts/audit-humanization.py scan --output tmp/humanization/candidates.json
python scripts/audit-humanization.py read --files chapters/08-uzorkovanje.qmd
python scripts/audit-humanization.py verify --baseline tmp/humanization/baseline.json --output notes/reports/humanization-changes.json
python bookwright_plugin/bookwright/scripts/run_rscript.py bookwright_plugin/bookwright/skills/book-style/scripts/style_lint.R "chapters/*.qmd" "dodaci/*.qmd"
```

Zaštitna provjera uspoređuje YAML, kod, formule, brojke, citatne oznake,
poveznice, komentare i strukturne retke. Nije potpuni Quarto parser i ne može
prepoznati promijenjeno značenje rečenice. Uredničko čitanje ostaje obvezno.
Nalazi skenera služe traženju mjesta za pregled; njihov broj nije ocjena
prirodnosti, cilj prolaza ni mjera AI autorstva.

## Zapis dovršenog prolaza

Zapis mora navesti pregledane i izmijenjene datoteke, početne i završne
otiske, konkretne izmjene, razloge zadržavanja važnih obrazaca, izvješća
kritičara i stvarne rezultate provjera. Treba jasno razlikovati završetak
ovoga prolaza od završetka knjige, uredničku prosudbu od studentskog pilota
te lokalnu izgradnju od objave. Otvorena pitanja koja zahvaćaju kasnije
revizije ostaju u datiranom izvješću uz ovaj postupak.

## Potpuni prolaz kroz rukopis

Nakon izričitog zahtjeva za cijelu knjigu pregled obuhvaća svaki čitateljski
odlomak svih 26 izvora u aktualnom redoslijedu, uključujući sedam dodataka,
tablice, opise slika, oba izlazna oblika i zadatke. Obuhvaća i tiskane
provjere rješenja, putokaz, rječnik, uvode dijelova, kolofon, literaturu i
naslovnu stranicu. Evidencija razlikuje potpuno čitanje od skeniranja i
od naknadnog pregleda izmijenjenih mjesta. Tekst koji već dobro objašnjava
zadržava se; nije potrebno mijenjati svaki odlomak.

Za ovaj puni prolaz dopuštene su tri dodatne, točno evidentirane vrste
zahvata. Dva vidljiva naslova Dodatka B mogu se preoblikovati uz iste
identifikatore, razinu, položaj i svrhu. Prikazni nazivi polja i pravopis
Kataloga mogu se urediti u generatoru, uz nepromijenjen kanonski katalog i
sve njegove odluke. Javna polja `self_study.hint`, `worked_answer` i
`why_adequate` uređuju se u kanonskim zapisima, a tiskani i mrežni prikazi
ponovno se generiraju. Brojevi, formule, citati, zadaci, namjerne greške,
rubrike i svi ostali dijelovi zapisa ostaju jednaki početnom snimku.

Opća zaštitna provjera ostaje stroga. Zaseban dokaz mora imenovati svaku
prikaznu iznimku; nije dopušteno prešutno zanemariti cijelu kategoriju
razlika. Pregled glasa raspoređuje se po nepreklapajućim skupinama poglavlja,
a zasebni kritičar provjerava razvoj argumenta. Urednik prihvaća i spaja
prijedloge te provjerava njihov učinak u kontekstu. Samo urednik piše izvore.
