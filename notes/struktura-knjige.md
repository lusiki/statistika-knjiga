# Osnove statistike za društvene znanosti

Radni dokument strukture knjige. Verzija 1, srpanj 2026.

> **Napomena o statusu.** Ovo je izvorni plan knjige, prenesen doslovno. On je
> mjerodavan za opseg, redoslijed i sadržaj poglavlja. `AGENTS.md` je operativni
> priručnik i preslikava ga; ako se njih dvoje raziđu, ovaj dokument ima
> prednost, a `AGENTS.md` se ispravlja. Dopune zabilježene pri postavljanju
> repozitorija su na dnu, jasno odvojene.
>
> **Dopuna od 5. kolovoza 2026.** Ta prednost vrijedi i dalje, ali samo ondje
> gdje ratificirana odluka nije rekla drukčije. Program sveobuhvatne revizije ima
> vlastiti upravljački sloj — plan iz
> `notes/reports/comprehensive-review-implementation-plan-2026-08-03.md`, registar
> `comprehensive-review-implementation-register.yml`, ledger prosljeđivanja i
> nadzornu ploču. Ondje gdje je ratificirana odluka toga programa izmijenila
> nešto iz ovoga dokumenta, vrijedi ta odluka i zabilježena je u registru s
> vlastitom stavkom. Ovaj dokument ostaje nacrt knjige, a ne paralelni popis
> zadataka.
>
> Odjeljak „Otvorene odluke" na dnu popisuje pitanja otvorena u srpnju 2026.
> Dio ih je otada zatvoren odlukama `D01`–`D16` i gateovima `G-A0` do `G-A2c`,
> pa taj popis više nije mjerodavan za to što je otvoreno. Mjerodavan je
> registar.

Purpose. This document elaborates the five part structure into a chapter level
blueprint, with source mapping to the existing course, per chapter scope, the
interactive inventory, datasets, and a production plan. It is written to drop
into the new repo as the planning note that AGENTS.md and the bookwright skills
read.

## Publika i obećanje

Audience. Undergraduate students across the social sciences, sociology,
political science, psychology, communication, economics, with no assumed
mathematics beyond secondary school and no assumed programming. The reader who
must understand research, not the reader who must become an analyst.

The book promises four abilities. After reading, the student can critically
judge statistical claims met in media, reports and AI output. They can describe
and visualize a dataset honestly. They can read, interpret and modestly
reproduce the inferential analyses that dominate published social science, tests
of association, group comparison and regression. And they can work with an AI
assistant on quantitative tasks in a disciplined way, delegating computation
while keeping judgment, verification and responsibility.

Out of scope, stated early and explicitly. Time series, factor analysis and
psychometrics, multilevel models, the mathematics of machine learning, though
its concepts and social consequences receive a full chapter, and full Bayesian
inference, which appears as a framed outlook rather than a chapter.

## Četiri načela dizajna

1. Simulation before formulas. Every inferential idea is first experienced
   through resampling, then named.
2. Estimation over ritual. Effect sizes and intervals lead, significance testing
   is taught with its history and its abuses.
3. Literacy as content. Reading other people's numbers is a first class subject,
   not a motivational aside.
4. Computation in the browser. Interactive widgets carry the demonstrations,
   code is folded, print receives static figures through the existing filter
   chain.
5. AI as instrument and as subject. The book assumes every reader has an AI
   assistant and teaches disciplined use of it, and it treats algorithms as
   objects of social scientific study in their own right, deserving the same
   skeptical attention as any poll.

## Arhitektura izdanja

One repository, two Quarto profiles. The book profile folds all code, renders
widgets in HTML and swaps them for static figures in PDF via strip ojs and the
SVG pipeline. The course profile adds the seminar materials, the weekly schedule
and the unfolded code, so the HKS kolegij keeps running from the same chapter
files. The print paperback builds from the book profile with the statecraft
class, colophon and typst booklet already in the engine.

## Kostur svakog poglavlja

Each chapter follows a fixed skeleton, mapped onto the existing callout system.

1. Vinjeta. A real opening case, one page, always a question someone actually
   faced.
2. Izgradnja pojma. Prose and figures develop the idea, lecture style, analogies
   carry the load.
3. Interakcija. One central widget in the digital edition, its static
   counterpart in print.
4. Statistika u divljini. A box dissecting a genuine published claim, poll,
   headline or chart.
5. Pitajte model. A recurring box in two beats. First, how to use an assistant
   for this chapter's task, what to ask, what to verify, where models typically
   fail. Second, a planted error exercise, a short AI produced analysis
   containing one realistic mistake the reader must find.
6. Razrađeni primjer. One complete analysis, narrated, code folded beneath the
   prose.
7. Sažetak i pojmovi. Closing summary, key terms in Croatian and English, and
   four exercise tiers, conceptual, computational, critical, and a model audit
   tier where the reader grades an AI generated solution.

## Dio I. Statističko mišljenje

### Poglavlje 1. Zašto statistika

Izvor. Week 1, heavy port.
Sadržaj. Signal and noise, anecdote against data, Simpsonov paradoks in media
polls, the difference a rigorous approach makes. Establishes the book's voice
and the running promise.
Widget. Simpson paradox toggle, aggregate and grouped views of one dataset.
Opseg. Around 4500 words.

### Poglavlje 2. Mjerenje i istraživački dizajn

Izvor. Week 1 second half, moderate rewrite plus new material.
Sadržaj. Levels of measurement, reliability and validity, operationalization in
social science, experiments against observational studies, confounding
introduced informally, survey design and sampling frames. Causality is planted
here as a seed the regression chapter later waters.
Widget. Confounder illustration, a third variable switched on and off.
Opseg. Around 5500 words.

### Poglavlje 3. Kako brojke zavode

Izvor. New chapter, assembled partly from week 1 fragments.
Sadržaj. Misleading axes and chart crimes, base rate neglect, percentages
against percentage points, margins of error in headlines, cherry picking, a
checklist for reading a poll, and a section on judging AI generated analysis,
hallucinated numbers, spurious precision, confident nonsense, synthetic media
and the provenance question. Ends with the reader's first tool, a skeptic's
protocol for claims made by humans and machines alike.
Widget. Margin of error explorer over a simulated election poll.
Opseg. Around 5000 words. This chapter is the book's public face and its
marketing.

## Dio II. Opisivanje podataka

### Poglavlje 4. Sažimanje podataka

Izvor. Week 5, heavy port.
Sadržaj. Central tendency, variability, standardization and z values, when the
mean deceives, distribution shape and skew, log transformation intuition.
Widget. Distribution sculptor, the reader drags points and watches mean, median
and deviation respond.
Opseg. Around 5000 words.

### Poglavlje 5. Vizualizacija kao argument

Izvor. Week 6, moderate rewrite, code demoted.
Sadržaj. Anscombeov kvartet, the grammar of graphics as an idea rather than an
API, choosing the chart for the claim, small multiples, honest scales,
accessibility. The ggplot2 mechanics move to the praktikum.
Widget. Same data rendered through four chart choices, reader votes on which
claim each supports.
Opseg. Around 4500 words.

### Poglavlje 6. Povezanost

Izvor. Extracted from week 5, expanded.
Sadržaj. Covariance intuition, Pearson and Spearman, correlation matrices read
visually, restriction of range, correlation against causation with real social
science cases, Simpson returns quantitatively.
Widget. Guess the correlation game with a running score.
Opseg. Around 4000 words.

## Dio III. Od uzorka do populacije

### Poglavlje 7. Vjerojatnost koliko treba

Izvor. Week 7, trimmed port.
Sadržaj. Probability as long run frequency and as degree of belief, the three
basic rules, binomial situations, the normal curve and the 68, 95, 99.7 rule, QQ
intuition. Everything not used later is cut.
Widget. Coin and A/B campaign simulator with adjustable true rates.
Opseg. Around 4500 words.

### Poglavlje 8. Uzorkovanje

Izvor. Week 8 first half, rebuilt around simulation.
Sadržaj. Population against sample, the sampling distribution generated live,
central limit theorem as an observed fact, standard error, sample size
intuition, why polls of 800 people work.
Widget. The CLT machine, population shape adjustable, thousands of sample means
accumulating.
Opseg. Around 4500 words. Pedagoški the hinge of the book.

### Poglavlje 9. Procjena

Izvor. Week 8 second half, rebuilt.
Sadržaj. Point estimates, the bootstrap as the reader's own invention,
confidence intervals constructed and then interpreted correctly, the procedure
framing, precision against confidence.
Widget. Interval catcher, one hundred intervals drawn, the reader watches
roughly five miss.
Opseg. Around 4000 words.

## Dio IV. Zaključivanje

### Poglavlje 10. Logika testiranja

Izvor. Week 9 first half, port with restructuring.
Sadržaj. The courtroom analogy, null and alternative, test statistic and p value
defined through simulation, errors of both types, what a p value is not. A
framed box introduces the Bayesian alternative in two pages.
Widget. P value simulator under a true and a false null.
Opseg. Around 4500 words.

### Poglavlje 11. Veličina učinka i snaga

Izvor. Week 9 second half, expanded.
Sadržaj. Cohenov d, practical against statistical significance, power and its
determinants, why underpowered studies mislead in both directions, planning a
study backwards from the effect worth caring about.
Widget. Power explorer, effect size, n and alpha on sliders.
Opseg. Around 4000 words.

### Poglavlje 12. Kriza i obnova

Izvor. New chapter.
Sadržaj. The replication crisis told as a story, p hacking and the garden of
forking paths, publication bias, preregistration and registered reports, open
data and materials, how to read a published study skeptically but fairly, and
AI's double role in the story, as an engine of fabricated papers and paper
mills, and as a tool for large scale reproducibility checking. Closes with what
reform means for a student reader.
Widget. P hacking sandbox, the reader tortures a dataset until significance
appears, then sees the multiplicity cost.
Opseg. Around 5000 words. With chapter 3, the second pillar of the book's
contemporary identity.

## Dio V. Modeli

### Poglavlje 13. Kategorički podaci

Izvor. Week 10, heavy port.
Sadržaj. Contingency tables, chi square goodness of fit and independence,
standardized residuals, Cramérovo V, Fisherov egzaktni test, the generational
media gap case. Kept deliberately outside the linear model frame.
Widget. Expected against observed frequency visualizer.
Opseg. Around 4500 words.

### Poglavlje 14. Uspoređivanje dviju grupa

Izvor. Week 11, moderate rewrite.
Sadržaj. The three t test variants taught once as one linear model with a binary
predictor, assumptions checked visually, Cohenov d again in context, Wilcoxon as
the fallback. The model formula appears beside every test from here on.
Widget. Two group sampler with adjustable true difference.
Opseg. Around 4500 words.

### Poglavlje 15. Uspoređivanje više grupa

Izvor. Week 12, moderate rewrite.
Sadržaj. Why ten t tests explode the error rate, ANOVA as the linear model with
a categorical predictor, the F logic as variance ratio, Tukeyjev HSD, eta
squared, Kruskal Wallis.
Widget. Between and within variance decomposition, group means draggable.
Opseg. Around 4000 words.

### Poglavlje 16. Regresija, opći okvir

Izvor. Week 13, expanded into the synthesis chapter.
Sadržaj. Simple regression, least squares seen geometrically, R squared,
multiple regression and control, diagnostics through residual plots, the reveal
that chapters 14 and 15 were regression all along, prediction against
explanation, a bridge passage on where prediction becomes machine learning,
preparing chapter 17, and the causal seed from chapter 2 harvested, what
regression can and cannot say about cause.
Widget. Draggable regression line with live residuals, then a second predictor
switched on.
Opseg. Around 6000 words. The summit chapter.

### Poglavlje 17. Statistika u doba algoritama

Izvor. New chapter.
Sadržaj. Written for the social science reader, concepts without code.
Prediction against explanation formalized, training and test data, overfitting
as the failure to generalize, classification and thresholds, how recommender
systems and content ranking shape what societies see, algorithmic bias and
fairness with the base rate arithmetic that makes fairness definitions collide,
and a closing section that reads large language models statistically, next word
prediction, distributions over text, why fluency is not truth. The chapter arms
the reader to study algorithms as social forces, not to build them.
Widget. Fairness explorer, a classification threshold slider showing error rates
diverging across two groups.
Opseg. Around 5500 words. With chapters 3 and 12, the third pillar of the book's
contemporary identity.

## Završnica

### Poglavlje 18. Vaše prvo istraživanje

Izvor. New, built from the course practical project.
Sadržaj. One complete guided study, question, design, data collection or
acquisition, description, visualization, model, interpretation, written report.
Reporting standards for social science, writing about uncertainty honestly, and
the full collaborator protocol with an AI assistant, prompt, verify, reproduce,
disclose, including the privacy rule that respondent data never enters a public
model. The chapter is deliberately narrated in the first person plural.
Opseg. Around 5000 words.

## Dodaci

Dodatak A. R praktikum. Weeks 2 through 4 condensed to about 12000 words,
installation, tidyverse verbs, import and cleaning, writing functions,
reproducible scripts. Written to be readable standalone.

Dodatak B. Put bez koda. A jamovi companion, four pages per part, mapping every
analysis in the book onto menu driven software for departments that do not teach
programming.

Dodatak C. Katalog podataka. Every dataset used, source, license, variables,
download path. Core sources, the European Social Survey Croatian waves, DZS,
Eurostat, plus the course's media engagement datasets carried over as one
example thread.

Dodatak D. Koji test kada. A one spread decision tree from data type and
question to chapter and method, plus a compact formula reference.

Dodatak E. Rječnik pojmova. Croatian and English terminology side by side, since
Croatian statistical vocabulary is inconsistent across faculties and students
read international literature.

Dodatak F. Protokol za rad s asistentom. The book's AI usage rules gathered on
four pages. Privacy and GDPR duties when data describes people, verification and
reproduction habits, disclosure norms for coursework and publication, and a
short guide for instructors on assessment that stays meaningful when every
student has an assistant, critique tasks, local data, in class simulation games.

## Interaktivni inventar

Seventeen widgets total, one in every numbered chapter from 1 through 17; the
preface and capstone are exempt. Build order follows pedagogical weight, the CLT
machine first, then the interval
catcher, the p value simulator and the p hacking sandbox, since these four carry
the book's core argument. All widgets ship with a static figure twin for print,
produced through the existing filter chain.

## Plan proizvodnje

Faza 1. Template repo from the engine, seed chapter smoke test, canonical
AGENTS.md with a CLAUDE.md import shim, and STYLE.md rewritten for this book. A
few days.

Faza 2. Port wave, chapters 1, 4, 7, 13 and the praktikum, where existing
lectures carry most of the load. This wave builds momentum and validates the
pipeline on real content.

Faza 3. Rewrite wave, chapters 2, 5, 6, 8, 9, 10, 11, 14, 15, 16, where course
material is restructured around simulation and the model frame, and the four
flagship widgets are built.

Faza 4. New wave, chapters 3, 12, 17 and 18, the literacy chapter, the open
science chapter, the algorithms chapter and the capstone, written fresh.

Faza 5. Cross cutting passes, the divljina and AI boxes seeded through every
chapter, exercises, glossary, decision tree, then review cycles through the
bookwright skills, regeneration of the machine readable exports through the
existing build script so that any reader's assistant answers from the book's own
text, and an AI production disclosure in the colophon consistent with current
publishing norms.

Ukupni opseg. Roughly 84000 words of main text plus 17000 in appendices, on the
order of 350 to 380 printed pages, comparable to the policy book's production
profile.

> **Dopuna od 5. kolovoza 2026.** Ta je brojka **dijagnostika za cijelu knjigu,
> a ne kvota**. Nije udio po poglavlju, nije uvjet dovršenosti i nijedan je
> paket ne smije navesti kao razlog da sadržaj traži ili odbije. Poglavlje je
> dovršeno kad nosi svoju ratificiranu kralježnicu i kad mu argument drži od
> početka do kraja; prolaz kroz strukturne pojaseve i pogođen broj riječi to ne
> dokazuju. Ista granica stoji u `STYLE.md` uz strukturne pojaseve i u
> `ENRICHMENT.md` uz test asimetrije.

## Otvorene odluke

1. Naslov. Working options, Statistika za društvene znanosti, or Brojke koje
   govore with a descriptive subtitle. Decide before the repo is named.
2. Bayes. Confirmed as a framed box in chapter 10 and an outlook paragraph in
   chapter 16, not a chapter. Revisit only if reviewers push.
3. Dubina jamovi dodatka. Screenshots age fast, decide whether Dodatak B
   documents exact menus or stays conceptual.
4. Jezik primjera. Whether flagship examples stay Croatian only or each chapter
   carries one international case for portability.
5. Licenca. Resolved in P1B-NAVARRO on 2026-08-03. Every candidate tied to
   Navarro was removed or independently rebuilt, and the passage-level audit
   found no surviving material dependency or ShareAlike obligation. The book
   retains MIT for its original text, code and associated documentation;
   third-party materials keep separately stated terms. The internal record is
   `notes/reports/p1b-navarro-provenance-and-licence-audit-2026-08-03.md`.
6. Ugrađeni tutor. Whether the digital edition embeds a chat tutor grounded in
   the book through an API, a genuine differentiator with real costs, hosting,
   privacy review and maintenance duty. Decide after the exports ship, since the
   exports alone deliver most of that value.

---

# Dopune zabilježene pri postavljanju repozitorija (2026-07-29)

Ove su stavke uočene pri prenošenju plana u repozitorij i nisu izmjene plana
nego pitanja za autora.

## Broj widgeta je razriješen

Opisi poglavlja navode sedamnaest widgeta, po jedan za svako poglavlje od 1 do
17, pa je stara zbirna brojka četrnaest ispravljena. `data/widgets.json` je
operativni izvor istine; predgovor i završno poglavlje 18 nemaju widget.

## Naslov i adresa repozitorija

Adresa je razriješena: repozitorij je `github.com/lusiki/statistika-knjiga`, knjiga se
objavljuje na `lusiki.github.io/statistika-knjiga`. (Postojeći `lusiki/Osnove-statistike`
je stranica kolegija, ne knjiga.) Naslov („Osnove statistike za društvene
znanosti") i autorstvo i dalje su radne vrijednosti iz otvorene odluke 1.

Adresa je upisana na tri mjesta i mijenja se zajedno: `site-url` i `repo-url` u
`_quarto.yml`, `link` u `design-tokens.yml` i `SITE_URL` u
`R/build-ai-exports.R`. Konstanta `UPUTA` u `styles/book-include.html` nosi samo
tekst upute — poveznicu na poglavlje gradi iz `location.origin`, pa se ne dira.

## Naslijeđeni engine nije prenesen doslovno

Plan spominje „the statecraft class, colophon and typst booklet already in the
engine". Prenesena je mehanika, ne izgled: LaTeX sloj, kolofon, filtri i lanac
SVG u PNG postoje, ali je paleta neutralni placeholder jer knjiga treba vlastiti
identitet (vidi `DESIGN.md`). Typst booklet nije prenesen; bio je vezan uz
priručnik za građane koji ova knjiga nema. Ako zatreba format džepnog izdanja,
prenosi se zasebno.

## Predgovor

Plan nema uvodno poglavlje prije Dijela I. Repozitorij ima
`chapters/00-predgovor.qmd` jer knjiga treba mjesto na kojem se izriče obećanje
i opseg. Ako to preuzme naslovnica, poglavlje se briše iz `_quarto.yml`.

Napomena od 2026-07-30. Predgovor od sada nosi kratak odlomak o čitanju koda
(vidi niže). Ako se poglavlje ipak obriše, taj odlomak seli na početak Dodatka A
uz poveznicu s naslovnice, jer se kod pojavljuje već u poglavlju o sažimanju
podataka i orijentacija mu mora prethoditi.

---

# Kod u knjizi (2026-07-30)

Načelo 4 kaže da je kod presavijen, ali ne kaže čemu služi kada ga čitatelj
otvori. Odluka je zapisana ovdje, a ne u `STYLE.md`, jer određuje kralježnicu i
provlači se kroz svih osamnaest poglavlja. `STYLE.md` H10 nosi njezin urednički
oblik.

## Načelo

Čitatelj ne piše R. Čitatelj uči čitati R, jer je čitanje koda način na koji
tvrdnja postaje provjerljiva. To čini kod predmetom knjige, a ne vještinom koju
knjiga zahtijeva, i pošten je oblik četvrtog obećanja. Asistent napiše poziv u
nekoliko sekundi, pa ono što preživljava tu automatizaciju jest sud o tome
odgovara li poziv na postavljeno pitanje.

## Tri registra

Pogonski kod crta figure i tablice. U knjižnom je profilu skriven jer projekt
sada ima `execute: echo: false`, a nastavni ga profil otkriva svojim
`echo: true`, pa seminar iz istih izvora dobiva otvoreno izdanje.

Račun stoji otvoren, i to samo u razrađenom primjeru. On pokazuje kako su
dobivene brojke koje proza navodi. Nije zadatak i ne prepisuje se.

Osumnjičeni kod napisao je asistent i nosi jednu stvarnu pogrešku. Živi u okviru
o pogrešci i u četvrtoj razini zadataka. Račun i osumnjičenik ista su vještina u
dva raspoloženja.

## Ljestvica izlaganja

Mijenja se ono čemu kod služi, a ne njegova težina. Težina ostaje ravna
namjerno.

Dio I nema vidljivog koda. Prva tri poglavlja odlučuju kakvu knjigu čitatelj
misli da drži u rukama, a blok koda na dvanaestoj stranici na to pitanje
odgovara pogrešno i trajno. Njihovo je gradivo ionako tvrdnje i grafovi.

Dio II uvodi kod kao račun. Poglavlje o sažimanju uvodi niz glagola, poglavlje o
vizualizaciji specifikaciju grafa i jedinu dopuštenu anatomiju poziva u knjizi, a
poglavlje o povezanosti ne uvodi ništa novo. To treće poglavlje je dokaz da
sustav radi, jer čitatelj u njemu čita kod koji ga nitko nije učio.

Dio III kod pretvara u samu demonstraciju, jer se svaka inferencijalna ideja
prvo doživi kroz ponovno uzorkovanje. Distribucija uzorkovanja je jedna linija
koja povuče uzorak, izračuna mjeru i to ponovi mnogo puta. Poglavlje o
uzorkovanju izriče da je cijeli aparat zaključivanja petlja, i to je najjači
argument za prisutnost koda u knjizi. Bez njega čitatelj mehaniku mora primiti
na vjeru, što je obrnuto od svrhe knjige.

Dio IV kod izlaže kao dokaz o zloupotrebi. Vrtlarenje po stazama koje se
razdvajaju niz je odluka u skripti (gelman2013), pa poglavlje o krizi i obnovi
pokazuje isti skup analiziran na četiri obranjiva načina s četiri različite
p-vrijednosti. Taj se argument ne može iznijeti u prozi, a čitatelj i dalje ne
piše ništa nego čita razdvajanje.

Dio V kod svodi na jedan poziv i jedan ispis. Težina nakon simulacijskih
poglavlja pada, i to je pedagoški ispravno jer je test kratica za simulaciju
koju čitatelj već razumije. Poglavlje o regresiji ponovno koristi gramatiku iz
poglavlja o vizualizaciji za dijagnostiku. Poglavlje o algoritmima registar
mijenja posljednji put, jer je tamo kod predmet proučavanja, a ne alat.

Završnica ne uvodi nijedan novi obrazac. Poglavlje 18 sastavlja postojeće u
jedan pripovjedni niz i jedino je mjesto na kojem bi motiviran čitatelj mogao
reproducirati cjelinu, s Dodatkom A u drugoj ruci.

## Pet obrazaca, ukupno

Niz glagola, specifikacija grafa, simulacijska petlja, poziv modela s ispisom i
njihovo sastavljanje. Svaki se uvodi jednom, u poglavlju koje ga traži, i nijedan
se ne predaje kao programiranje. To je cijela površina R-a u knjizi.

## Sintaksa

Nigdje u poglavljima. Predgovor nosi pola stranice o tome kako se blok koda čita
i obećanje da ga čitatelj nikada ne mora napisati, jer su tri znaka dovoljna.
Znak `|>` znači „pa onda", znak `+` dodaje sloj grafu, a `aes` imenuje
pridruživanje. Sve ostalo su imena glagola. Dodatak A uči pisanje, Dodatak B nudi
put bez koda.

## Posljedica za zadatke

Računska razina nikada ne pretpostavlja instaliran R. Radi s brojevima koji se
mogu izračunati ručno, s tablicom koju poglavlje već ispisuje ili s widgetom
poglavlja, a čitatelja koji želi cijeli skup upućuje na Dodatak A ili B. Četvrta
razina od poglavlja o vizualizaciji nadalje ocjenjuje artefakt zajedno s njegovim
kodom, jer je to jedino mjesto na kojem čitanje koda postaje obvezno. Bez toga
četvrto obećanje ostaje ukras.
