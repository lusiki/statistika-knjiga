# P1B-BIB — uporaba citata i bibliografski metapodaci

Provjera je provedena 3. kolovoza 2026. nad deklariranim stanjem sadržajnih
datoteka
`state:sha256-8e9a96cf20573f7f96f95155189f20dfdb6e4e26de773545b415683ce102abd0`.
Polazišni commit bio je
`81869631d0faf8a99af809ea2a5c01ee26dd5a9b`. Paket obuhvaća uporabu citata,
metapodatke bibliografije i jednu nužnu uskladbu tvrdnje s izvorom. Ne otvara
P1B-META ni kasniji dokazni pregled.

## Obvezni handoff

`H-P1B-NAVARRO-001` pročitan je, priznat i konzumiran prije prve sadržajne
izmjene. Ponovljena provjera nije pronašla `@navarro2019` ni zapis
`navarro2019` u bibliografiji. Očuvano je verificirano nulto stanje. Navarro se
ne smije vratiti bez nove neovisno određene potrebe, mjerodavnih metapodataka
točne inačice i obnovljene analize prava.

## Izvještaj o uporabi citata {#citation-usage-report}

Iz svih živih `.qmd` izvora pročitani su svi citatni konteksti. HTML komentari
izuzeti su jer ih Pandoc ne prikazuje. Pronađeno je 121 živo pojavljivanje 35
ključeva u 21 datoteci. Svih 35 ključeva sada ima točno jedan zapis u
`references.bib`, nema neriješenoga ključa i nema bibliografskog zapisa bez
žive uporabe. Uklonjen je jedini neupotrijebljeni sjemenski zapis
`ioannidis2005`. Njegov DOI
[`10.1371/journal.pmed.0020124`](https://doi.org/10.1371/journal.pmed.0020124)
provjeren je prije uklanjanja, pa odluka nije donesena na temelju nepoznatog
identiteta rada.

| Izvorna datoteka | Živa pojavljivanja | Različiti ključevi |
|---|---:|---:|
| `chapters/00-predgovor.qmd` | 3 | 1 |
| `chapters/01-zasto-statistika.qmd` | 18 | 3 |
| `chapters/02-mjerenje-i-dizajn.qmd` | 4 | 2 |
| `chapters/03-kako-brojke-zavode.qmd` | 3 | 1 |
| `chapters/04-sazimanje-podataka.qmd` | 3 | 1 |
| `chapters/05-vizualizacija.qmd` | 19 | 6 |
| `chapters/06-povezanost.qmd` | 7 | 5 |
| `chapters/07-vjerojatnost.qmd` | 5 | 2 |
| `chapters/08-uzorkovanje.qmd` | 4 | 2 |
| `chapters/09-procjena.qmd` | 4 | 3 |
| `chapters/10-logika-testiranja.qmd` | 5 | 2 |
| `chapters/11-velicina-ucinka-i-snaga.qmd` | 4 | 3 |
| `chapters/12-kriza-i-obnova.qmd` | 11 | 3 |
| `chapters/13-kategoricki-podaci.qmd` | 6 | 4 |
| `chapters/14-dvije-grupe.qmd` | 4 | 3 |
| `chapters/15-vise-grupa.qmd` | 3 | 2 |
| `chapters/16-regresija.qmd` | 4 | 3 |
| `chapters/17-doba-algoritama.qmd` | 8 | 3 |
| `chapters/18-vase-prvo-istrazivanje.qmd` | 2 | 1 |
| `dodaci/a-praktikum.qmd` | 2 | 1 |
| `dodaci/c-katalog-podataka.qmd` | 2 | 2 |
| **Ukupno** | **121** | **35 jedinstvenih** |

Uklanjanjem `nocite: @*` stranica Literatura sada se gradi samo iz stvarnih
uporaba. Komentar u `references.qmd` i zaglavlje u `references.bib` usklađeni
su s održavanim, a ne sjemenskim statusom popisa.

## Mjerodavna provjera metapodataka {#authoritative-metadata-verification}

Svaki DOI u živom popisu upitan je izravno kroz Crossref REST zapis. Svih 29
upita vratilo je registrirani DOI i naslov koji odgovara zapisu. Razlike u
veličini slova DOI-ja, interpunkciji naslova i registriranim podnaslovima nisu
pretvorene u nove bibliografske tvrdnje.

### Dopunjeni DOI-ji

| Ključ | Verificirani DOI | Mjerodavni rezultat |
|---|---|---|
| `anscombe1973` | [`10.1080/00031305.1973.10478966`](https://doi.org/10.1080/00031305.1973.10478966) | Crossref i zapis izdavača podudaraju autora, naslov, časopis, godinu i stranice. |
| `wickham2016` | [`10.1007/978-3-319-24277-4`](https://doi.org/10.1007/978-3-319-24277-4) | Springer potvrđuje drugo izdanje iz 2016. |
| `simpson1951` | [`10.1111/j.2517-6161.1951.tb00088.x`](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x) | Crossref potvrđuje naslov, časopis, godište i stranice. |
| `efron1979` | [`10.1214/aos/1176344552`](https://doi.org/10.1214/aos/1176344552) | Project Euclid/Crossref potvrđuju zapis članka. |
| `cumming2014` | [`10.1177/0956797613504966`](https://doi.org/10.1177/0956797613504966) | SAGE/Crossref potvrđuju puni naslov i bibliografske podatke. |
| `cohen1994` | [`10.1037/0003-066X.49.12.997`](https://doi.org/10.1037/0003-066X.49.12.997) | APA/Crossref potvrđuju zapis članka. |
| `wasserstein2016` | [`10.1080/00031305.2016.1154108`](https://doi.org/10.1080/00031305.2016.1154108) | Taylor & Francis/Crossref potvrđuju ASA izjavu. |
| `simmons2011` | [`10.1177/0956797611417632`](https://doi.org/10.1177/0956797611417632) | SAGE/Crossref potvrđuju puni zapis članka. |
| `osc2015` | [`10.1126/science.aac4716`](https://doi.org/10.1126/science.aac4716) | Science/Crossref potvrđuju korporativnog autora i broj članka. |
| `breiman2001` | [`10.1214/ss/1009213726`](https://doi.org/10.1214/ss/1009213726) | Project Euclid/Crossref potvrđuju rad i raspon stranica. |
| `chouldechova2017` | [`10.1089/big.2016.0047`](https://doi.org/10.1089/big.2016.0047) | Izdavačev zapis potvrđuje naslov, godište i stranice 153–163. |

### Ponovno provjereni postojeći DOI-ji

| Ključ | DOI | Ishod Crossref provjere |
|---|---|---|
| `wilkinson2005` | [`10.1007/0-387-28695-0`](https://doi.org/10.1007/0-387-28695-0) | podudaranje |
| `cleveland1984` | [`10.1080/01621459.1984.10478080`](https://doi.org/10.1080/01621459.1984.10478080) | podudaranje |
| `matejka2017` | [`10.1145/3025453.3025912`](https://doi.org/10.1145/3025453.3025912) | podudaranje |
| `tversky1973` | [`10.1016/0010-0285(73)90033-9`](https://doi.org/10.1016/0010-0285(73)90033-9) | podudaranje |
| `stevens1946` | [`10.1126/science.103.2684.677`](https://doi.org/10.1126/science.103.2684.677) | podudaranje |
| `bickel1975` | [`10.1126/science.187.4175.398`](https://doi.org/10.1126/science.187.4175.398) | podudaranje |
| `squire1988` | [`10.1086/269085`](https://doi.org/10.1086/269085) | podudaranje |
| `gilovich1985` | [`10.1016/0010-0285(85)90010-6`](https://doi.org/10.1016/0010-0285(85)90010-6) | podudaranje |
| `miller2018` | [`10.3982/ECTA14943`](https://doi.org/10.3982/ECTA14943) | podudaranje |
| `hoekstra2014` | [`10.3758/s13423-013-0572-3`](https://doi.org/10.3758/s13423-013-0572-3) | podudaranje |
| `greenland2016` | [`10.1007/s10654-016-0149-3`](https://doi.org/10.1007/s10654-016-0149-3) | podudaranje |
| `button2013` | [`10.1038/nrn3475`](https://doi.org/10.1038/nrn3475) | podudaranje |
| `cochran1954` | [`10.2307/3001616`](https://doi.org/10.2307/3001616) | podudaranje |
| `belia2005` | [`10.1037/1082-989X.10.4.389`](https://doi.org/10.1037/1082-989X.10.4.389) | podudaranje |
| `nieuwenhuis2011` | [`10.1038/nn.2886`](https://doi.org/10.1038/nn.2886) | podudaranje |
| `westreich2013` | [`10.1093/aje/kws412`](https://doi.org/10.1093/aje/kws412) | podudaranje |
| `shmueli2010` | [`10.1214/10-STS330`](https://doi.org/10.1214/10-STS330) | podudaranje |
| `ismay2019` | [`10.1201/9780367409913`](https://doi.org/10.1201/9780367409913) | podudaranje |

Tri ranije oprezno izostavljena raspona sada su unesena tek nakon provjere
izvan nepotpunoga Crossref polja. [Oxford Academic](https://academic.oup.com/poq/article-abstract/52/1/125/1878544)
potvrđuje 125–133 za `squire1988`, [mjerodavni EPA HERO
zapis](https://hero.epa.gov/reference/6766388/) potvrđuje 417–451 za
`cochran1954`, a [izvorni PDF na Project
Euclidu](https://projecteuclid.org/journals/statistical-science/volume-25/issue-3/To-Explain-or-to-Predict/10.1214/10-STS330.pdf)
potvrđuje 289–310 za `shmueli2010`.

### Zapisi bez DOI-ja i stabilni lokatori {#no-doi-locators}

| Ključ | Provjereni identitet i lokator | DOI dispozicija |
|---|---|---|
| `tukey1977` | [WorldCatov zapis](https://search.worldcat.org/title/03058187) potvrđuje autora, naslov, Addison-Wesley, Reading i 1977. | Točno pretraživanje Crossrefa i knjižnični zapis nisu dali DOI za citirano izdanje; DOI nije unesen. |
| `tufte2001` | [Autorova/izdavačeva stranica](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/) potvrđuje drugo izdanje iz 2001. | Izdavačev zapis ne navodi DOI; DOI nije unesen. |
| `cohen1988` | [WorldCatov zapis](https://search.worldcat.org/title/Statistical-power-analysis-for-the-behavioral-sciences/oclc/299414673) potvrđuje drugo izdanje, autora, izdavača, mjesto i godinu. | Crossref nalazi DOI kasnijega Routledgeova izdanja, ne citiranoga izdanja iz 1988.; tuđi DOI nije pripisan. |
| `gelman2013` | [Columbijin popis neobjavljenih radova](https://sites.stat.columbia.edu/gelman/research/unpublished/) i [izvorni PDF](https://sites.stat.columbia.edu/gelman/research/unpublished/forking.pdf) potvrđuju autore, puni naslov i inačicu od 14. studenoga 2013. | Izvor i Crossref ne daju DOI. U zapis su uneseni točna inačica i stabilni institucionalni URL. |
| `barocas2023` | [MIT Press](https://mitpress.mit.edu/9780262048613/fairness-and-machine-learning/) potvrđuje autore, naslov, 2023. i ISBN 9780262048613; [autorsko mrežno izdanje](https://fairmlbook.org/) daje stabilan puni tekst. | Izdavačev zapis ne navodi DOI; dodani su verificirani ISBN i URL. |
| `wickham2023` | [O'Reillyjev zapis](https://www.oreilly.com/library/view/r-for-data/9781492097396/copyright-page01.html) potvrđuje autore, drugo izdanje, izdavača i izdanje iz lipnja 2023.; zapis već vodi na autorsko mrežno izdanje. | Izdavačev zapis ne navodi DOI; DOI nije unesen. |

Time svaki članak i rad u zborniku ima verificirani DOI, a svaki živi zapis
bez DOI-ja ima verificirani identitet i lokator ili izričit checked-no-DOI
ishod. Nijedan DOI, lokator, broj stranice ni inačica nije izveden iz sjećanja.

## Zapis uklapanja tvrdnje i izvora {#claim-source-fit}

Svih 121 uporaba pročitana je u rečenici, odlomku, natpisu ili zadatku u kojem
se prikazuje. Ponavljanja istoga rada grupirana su po ključu. Oznaka „usklađeno”
znači da primarni rad ili mjerodavno izdanje nosi pripisanu metodu, nalaz,
brojku ili povijesnu tvrdnju. Simulacije i autorske izvedbe provjerene su kao
takve i nisu prikazane kao izvorni empirijski nalazi.

| Ključ | Uporabe | Provjerena funkcija u rukopisu | Dispozicija |
|---|---:|---|---|
| `anscombe1973` | 8 | četiri brojčano slična skupa s različitim grafičkim oblicima i isti regresijski pravac | usklađeno |
| `barocas2023` | 3 | definicije mjerila pravednosti, sukob pri različitim temeljnim stopama i autorska simulacija prema izvoru | usklađeno |
| `belia2005` | 1 | zadatak procjene preklapanja traka pogreške među 473 autora | usklađeno |
| `bickel1975` | 24 | Berkeley 1973., šest odjela, zbirne i odjelne stope te granice zaključka | usklađeno |
| `breiman2001` | 2 | dvije kulture modeliranja i razlika prediktivnoga i podatkovnog modeliranja | usklađeno |
| `button2013` | 2 | niska snaga, precijenjeni učinci i slaba pouzdanost neuroznanstvene literature | usklađeno |
| `chouldechova2017` | 4 | kalibracija/prediktivna parnost i uvjetne stope pogreške pri različitim prevalencijama | usklađeno nakon jedne ispravke opisane niže |
| `cleveland1984` | 8 | pokusi grafičke percepcije, poredak kanala i ograničen doseg nalaza | usklađeno |
| `cochran1954` | 1 | prag očekivane frekvencije kao praktična preporuka, a ne matematički zakon | usklađeno |
| `cohen1988` | 6 | orijentacijske vrijednosti veličina učinka uz izvorno upozorenje o kontekstu | usklađeno |
| `cohen1994` | 1 | kritika ritualnoga oslanjanja na prag statističke značajnosti | usklađeno |
| `cumming2014` | 5 | procjene, intervali i „nova statistika” kao alternativa odluci na pragu | usklađeno |
| `efron1979` | 1 | uvođenje bootstrap postupka za procjenu nesigurnosti | usklađeno |
| `gelman2013` | 3 | vrt račvajućih putova bez nužne namjerne potrage kroz više analiza | usklađeno |
| `gilovich1985` | 3 | izvorni zaključak o vrućoj ruci i slučajnim nizovima | usklađeno i upareno s kasnijim ispravkom |
| `greenland2016` | 2 | 25 pogrešnih tumačenja testova, p-vrijednosti, intervala i snage | usklađeno |
| `hoekstra2014` | 2 | šest tvrdnji o intervalu pouzdanosti i njihovo pogrešno prihvaćanje | usklađeno |
| `ismay2019` | 1 | resampling/simulacija prije formule u nastavnoj arhitekturi | usklađeno |
| `matejka2017` | 1 | skupovi koji čuvaju sažetke do druge decimale uz vrlo različite oblike | usklađeno |
| `miller2018` | 2 | pristranost izvorne mjere vruće ruke i preokret zaključka nakon ispravka | usklađeno |
| `nieuwenhuis2011` | 1 | pregled 513 radova i razlika između izravnoga testa interakcije i usporedbe dviju oznaka značajnosti | usklađeno |
| `osc2015` | 3 | zajednički protokol za 100 replikacija i oprezno tumačenje reproducibilnosti literature | usklađeno |
| `shmueli2010` | 1 | razlika objašnjavajućega i prediktivnoga cilja kroz tijek modeliranja | usklađeno |
| `simmons2011` | 7 | analitička fleksibilnost, lažno pozitivni nalazi i simulacija više mogućih ishoda | usklađeno |
| `simpson1951` | 4 | promjena ili preokret odnosa pri razdvajanju kontingencijske tablice | usklađeno |
| `squire1988` | 3 | oba filtra neuspjeha ankete Literary Digesta, okvir uzorka i neodaziv | usklađeno |
| `stevens1946` | 1 | povijesni prijedlog četiriju razina mjerenja | usklađeno uz izričitu ogradu da nije bezvremenska tablica analiza |
| `tufte2001` | 2 | podatkovna tinta, grafički otpad i faktor laži | usklađeno |
| `tukey1977` | 3 | istraživačka analiza kao višestruki pregled koji otvara pitanja | usklađeno |
| `tversky1973` | 1 | heuristika dostupnosti | usklađeno |
| `wasserstein2016` | 9 | šest načela ASA izjave i zabrana svođenja znanstvenoga zaključka na prag | usklađeno |
| `westreich2013` | 2 | „Table 2 fallacy” i nejednako uzročno značenje koeficijenata kontrola | usklađeno |
| `wickham2016` | 1 | ggplot2 kao izvedba gramatike grafike | usklađeno |
| `wickham2023` | 2 | slobodno mrežno izdanje i sustavniji tidyverse put u praktikumu | usklađeno |
| `wilkinson2005` | 1 | gramatika grafike kao sustav neovisan o pojedinom programu | usklađeno |

Jedini otkriveni nesklad bio je u vinjeti poglavlja 17. Izvor dokazuje sukob
kalibracije/prediktivne parnosti sa stopama lažno pozitivnih i lažno negativnih
odluka kada se temeljne stope razlikuju. Rukopis je treći član pogrešno
zamijenio „jednakom ukupnom točnošću”. Rečenica je usklađena sa stvarnim
rezultatom izvora bez dodavanja novoga nalaza ili ključa. Cijelo poglavlje je
pročitano, a Bookwrightov linter prije izmjene nije našao deterministički
stilski pogodak.

## Usklađenje pogođenih datoteka {#affected-file-reconciliation}

| Datoteka | Usklađenje |
|---|---|
| `_quarto.yml` | Uklonjeni su `nocite: @*` i zastarjeli privremeni komentar. |
| `references.bib` | Sjemenski status zamijenjen je održavanim; uklonjen je jedini neupotrijebljeni zapis; dodano je 11 DOI-ja, među kojima jedan DOI knjige, tri verificirana raspona stranica te verificirani lokatori/inačice za Gelman–Loken i Barocas–Hardt–Narayanan. |
| `references.qmd` | Komentar sada točno kaže da se prikazuju samo korišteni, provjereni unosi. |
| `chapters/17-doba-algoritama.qmd` | Jedna tvrdnja u vinjeti vraćena je kriterijima koje Chouldechova stvarno dokazuje. |
| `README.md` | Nije mijenjan. Javni status i ostali metapodaci pripadaju isključivo sljedećem paketu P1B-META. |

Manifest sadržajnoga stanja izvan kontrolne transakcije jest sljedeći.

| Putanja | Git blob |
|---|---|
| `_quarto.yml` | `562a8815eb2e18e4f529777d58bc29880fba4374` |
| `chapters/17-doba-algoritama.qmd` | `051d659935d8940155c7ed9acfd9f4d4570afd14` |
| `references.bib` | `b64974b22f1417fe6e42993ca950163f1fe14846` |
| `references.qmd` | `b4aecb20fd1568047d5082ea1b696450729ccd5b` |

SHA-256 je izračunan nad UTF-8 manifestom putanje i Git blob identifikatora,
poredanim kao u tablici i završenim jednim znakom novoga retka.

## Buduće obveze

Paket nije pronašao novi učinak koji bi morao ograničiti kasniji paket. P6-EVIDENCE
će prema već ratificiranom opsegu ponoviti cjelokupnu provjeru dokaznih
uporišta, ali P1B-BIB mu ne predaje novu neriješenu tvrdnju. P1B-META smije
početi tek nakon zatvaranja ovoga paketa i ne smije vratiti sjemenski opis ili
blanket `nocite`.
