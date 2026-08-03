# P1B-NAVARRO — revizija podrijetla i licence

Datum provjere je 3. kolovoza 2026. Paket provodi odluke D11 i G-A1c samo za
Navarrovo gradivo. Ne obuhvaća podatkovne licence, opći bibliografski pregled
ni metapodatke knjige.

## Odluka vlasnika i ulazni handoff

Autor i vlasnik licence Luka Sikic odobrio je nultu javnu uporabu Navarra.
`H-G-A1C-001` pročitan je i prihvaćen kao supersedirana polazna odluka, a
`H-G-A1C-004` konzumiran je prije prve izmjene rukopisa kao njezina stroža
zamjena. Kandidat se smije ukloniti ili nužno objašnjenje izgraditi iznova;
brisanje atribucije uz zadržavanje izvedenog izraza ili strukture nije
dopušteno. Paket se mora zaustaviti ako nakon revizije ostane materijalna
ovisnost ili obveza ShareAlike.

## Provjereni izvor i licenca

Mjerodavni izvor za postojeći bibliografski zapis bila je Navarrova knjiga
*Learning Statistics with R*, inačica 0.6. [Autoricina stranica inačice
0.6](https://old.learningstatisticswithr.com/) izričito je označava kao CC
BY-SA 4.0 i povezuje PDF i izvorni repozitorij. Provjeren je PDF s adrese
<https://old.learningstatisticswithr.com/lsr-0.6.pdf>:

- naslovnica navodi Danielle Navarro, University of New South Wales i
  „Version 0.6";
- datoteka ima 613 stranica i 7 620 603 bajta;
- SHA-256 je
  `CEB73307B5B0D310120E3E1470917B80189AFA11BEC3487F3910C8B1FA5BFE16`;
- metapodatak izrade glasi 1. svibnja 2018.;
- licenčna stranica i predgovor inačice 0.6 izričito navode CC BY-SA 4.0.

Raniji zapis `navarro2019` nije pouzdano vezao godinu i adresu uz provjerenu
inačicu. Korijenska adresa danas vodi na novije izdanje, a [trenutačni GitHub
repozitorij](https://github.com/djnavarro/rbook) navodi da izvorne datoteke
knjige više nisu u njemu. Zapis je zato bio slab identifikator čak i prije
odluke o nultoj uporabi.

[Pravni tekst CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
određuje prilagođeni materijal kao autorskopravno zaštićen materijal izveden
iz licenciranog izvora i nalaže istu ili kompatibilnu licencu kada se takva
prilagodba javno dijeli. [Službeni popis kompatibilnih
licenci](https://creativecommons.org/compatible-licenses/) za BY-SA 4.0
navodi BY-SA 4.0 ili noviju, odgovarajuće prenesene inačice, Free Art License
1.3 i jednosmjerno GPLv3; MIT nije na popisu. WIPO-ov Ugovor o autorskom pravu,
[članak 2](https://www.wipo.int/en/web/copyright), razdvaja zaštićeni izraz od
ideja, postupaka, metoda i matematičkih koncepata.

Operativni zaključak paketa stoga nije da citat sam uklanja licenčni rizik.
Izraz ili prepoznatljiva izvedena struktura morali bi nositi atribuciju i
kompatibilan ShareAlike režim. Opći statistički pojmovi i matematičke metode
mogu se objasniti samostalno, ali tek nakon provjere da izvorni izraz i
prepoznatljiva izvedena struktura nisu zadržani.

## Revizija korespondencije na razini odlomka

| Oznaka | Mjesto u rukopisu | Korespondencija s inačicom 0.6 | Dispozicija |
|---|---|---|---|
| N01 | Poglavlje 1, odlomak o kuharskom receptu u odjeljku „Zašto društvene znanosti trebaju statistiku" | Potpuno su pročitani predgovor i 1. poglavlje izvora te pretraženi izrazi povezani s receptom, kuhanjem, mehaničkim uputama i proizvoljnim koracima. Nije pronađen odlomak koji podupire pripisanu analogiju; jedina pojava riječi „recipe" u PDF-u pripada nepovezanom odlomku u završnom dijelu knjige. | Uklonjeni su ime, citat, analogija i njezin slijed. Nužna razlika između ispravnog računa i opravdanog pitanja izgrađena je novim odlomkom iz vlastite argumentacijske osi knjige. |
| N02 | Poglavlje 2, dvije rečenice nakon Instagram-primjera u odjeljku o konfundiranju | Potpuno su pročitani relevantni odjeljci 2.6 i 2.7. Izvor definira konfundirajuću varijablu kao dodatnu varijablu povezanu s prediktorom i ishodom, ali ne koristi pripisani naziv „problem treće varijable" niti podupire pripisanu formulaciju. | Dvije su rečenice uklonjene. Prethodna definicija i sljedeća razdioba obrnutog smjera, odabira i konfundiranja već daju samostalno i potpunije objašnjenje. |
| N03 | Poglavlje 4, odlomak o skraćenoj sredini | Potpuno je pročitan odjeljak 5.1.6 i susjedni odjeljci o mjerama središta. Izvor objašnjava postupak i kaže da se mjera povremeno izvještava, ali ne podupire pripisanu tvrdnju da je iznenađujuće rijetka i često primjerenija. | Uklonjeni su ime, citat i nepoduprta procjena uporabe. Cijela je definicija preoblikovana neovisno oko algoritma poredavanja, simetričnog uklanjanja i izračuna na lokalno generiranim podacima. |
| N04 | Poglavlje 4, odlomci o djelitelju $n-1$ i odgođenoj demonstraciji | Potpuno su pročitani odjeljci 5.2.1–5.2.7. Izvor u odjeljku o varijanci gradi iznenađenje razlikom između $N$ i $N-1$ te dokaz odgađa do 10. poglavlja; ne sadrži pripisanu tvrdnju da je to jedno od najtežih mjesta uvodnog kolegija. Taj je argumentacijski slijed bio materijalno blizak kandidatu i nije bilo dovoljno samo izbrisati citat. | Uklonjena je pripisana tvrdnja, a nužno objašnjenje izgrađeno je iznova preko ograničenja da je zbroj odstupanja nula, jednog potrošenog stupnja slobode i unaprijed najavljene simulacijske usporedbe djelitelja $n$ i $n-1$ u poglavlju 8. Redoslijed cijelog dijela sada slijedi vlastiti par sredina–standardna devijacija nasuprot medijanu–interkvartilni raspon. |

Nakon tih zahvata nijedan kandidat nije zadržan. N01, N03 i N04 samostalno su
prepisani samo u opsegu nužnom za argument knjige; N02 je uklonjen bez zamjene.
Nijedan novi empirijski nalaz, broj ili izvor nije uveden.

## Usklađenje datoteka

| Datoteka | Usklađenje | Zakoniti izlazni režim |
|---|---|---|
| `chapters/01-zasto-statistika.qmd` | Kandidat N01 prepisan je bez analogije, imena i citata; bilješka o podrijetlu pokazuje što je uklonjeno. | Izvorni autorski tekst pod MIT licencom repozitorija. |
| `chapters/02-mjerenje-i-dizajn.qmd` | Kandidat N02 uklonjen je; bilješka o podrijetlu bilježi negativnu korespondenciju. | Izvorni autorski tekst pod MIT licencom repozitorija. |
| `chapters/04-sazimanje-podataka.qmd` | Kandidati N03 i N04 prepisani su neovisno; bilješka više ne tvrdi naslijeđeni slijed. | Izvorni autorski tekst pod MIT licencom repozitorija. |
| `references.bib` | Uklonjeni su neupotrijebljeni i verzijski nepouzdani zapis `navarro2019` te zastarjela upozoravajuća bilješka. | Nema javne bibliografske uporabe Navarra. |
| `LICENSE` | Uklonjeno je uvjetno upozorenje o mogućem ShareAlike režimu nakon što je revizija utvrdila da kandidat nije preživio. Standardni MIT tekst ostaje neizmijenjen. | MIT za autorski tekst, kod i pridruženu dokumentaciju. |
| `README.md` | Dodan je izričit opis MIT opsega i izdvajanje zasebnih uvjeta za podatke i materijale trećih strana. | MIT nije proširen na tuđe podatke ili materijale. |
| `notes/struktura-knjige.md` | Odluka 5 označena je razriješenom uz vezu na ovu reviziju. | Plan više ne prikazuje završenu licenčnu odluku kao otvorenu. |
| `notes/plan-prijenosa.md` | Povijesna uputa dobila je bilješku o kasnijem uklanjanju ovisnosti, bez brisanja činjenice da je Navarro bio izvor u fazi prijenosa. | Provenijencija je sačuvana, ali više ne tvrdi otvorenu izloženost. |
| `notes/ai-export-spec.md` i `R/build-ai-exports.R` | Privremena restriktivna rečenica zamijenjena je MIT oznakom i vezom na puni tekst licence. | Budući AI izvozi slijede licencu autorskog teksta; materijali trećih strana ostaju izdvojeni. |

## Provjere rukopisa

- Checkout-localni deterministički linter nije pronašao kandidata za povredu
  STYLE.md ni u jednom od triju izmijenjenih poglavlja.
- Sva tri poglavlja pročitana su od početka do kraja prema ručnom postupku
  H1–H10; nisu pronađene preostale stilske povrede.
- Ciljani HTML renderi poglavlja 1, 2 i 4 uspjeli su u privremenom izlaznom
  direktoriju. Jedina upozorenja odnosila su se na nedostupno povezivanje
  izvornog koda paketima `downlit` i `xml2`, a ne na rukopis, navode ili
  izvršavanje poglavlja. Praćeni AI izvozi koje je pre-render hook pritom
  obnovio vraćeni su bit-po-bit na stanje prije paketa; `docs/` i `data/` nisu
  dio promjene.
- Pregled vidljivog teksta nakon uklanjanja HTML komentara ne nalazi
  `Navarro`, `navarro2019` ni *Learning Statistics with R* u rukopisu, a
  bibliografski ključ `navarro2019` više ne postoji.

## Završni licenčni zaključak

U renderiranom javnom rukopisu nakon revizije nema Navarrova imena, citata,
bibliografskog zapisa, analogije, primjera, prepoznatljivog argumentacijskog
slijeda ni materijalno izvedenog izraza. Interni trag ostaje upravo zato da
pokaže uklanjanje ovisnosti, a ne prikrivanje izvora. Na toj utvrđenoj
činjeničnoj osnovi nema preživjelog prilagođenog Navarrova materijala na koji
bi se primijenio ShareAlike. MIT režim knjige zato se može zadržati bez dodatne
vlasničke odluke iz H-G-A1C-004.
