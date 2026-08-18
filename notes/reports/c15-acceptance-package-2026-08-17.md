# C15 — paket za autorovo prihvaćanje petnaestoga poglavlja

**Gate:** `C15`

**Stanje gatea:** autor prihvatio; uska dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 17. kolovoza 2026.

**Datum autorove odluke:** 17. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor petnaestoga poglavlja nalazi se u WD-C15 closeout commitu
`a385ddc85c11e5d1cf63b33043c1df2a90cff6fb`. Taj commit sadrži cijeli
vertikalni rez, završne registre, šest kritičarskih izvještaja, sintezu i
closeout dokaze. Poglavlje nakon tog commita nije mijenjano.

- SHA-256 radne datoteke:
  `fd8337520901df9bbce56e25880f12b889fd54d46e4c1bb3e8f17da3ca49d813`;
- git blob poglavlja: `aa644049bacb62e7fc05ab75d3b6157b83165b96`;
- izvještaj vertikalnoga reza:
  `notes/reports/wd-c15-2026-08-17.md`;
- sinteza panela:
  `notes/reports/wd-c15-six-critic-synthesis-2026-08-17.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pročitalo je cijelo poglavlje i prije
i poslije pregleda potvrdilo upravo navedeni SHA-256 i git blob:

1. metode — `notes/reports/wd-c15-critic-methods-2026-08-17.md`;
2. skepticizam — `notes/reports/wd-c15-critic-skeptic-2026-08-17.md`;
3. pedagogija — `notes/reports/wd-c15-critic-pedagogy-2026-08-17.md`;
4. dokazi i citati — `notes/reports/wd-c15-critic-evidence-2026-08-17.md`;
5. hrvatski stil — `notes/reports/wd-c15-critic-style-2026-08-17.md`;
6. struktura — `notes/reports/wd-c15-critic-structure-2026-08-17.md`.

Završni panel bilježi nula fatalnih, nula velikih i četiri neblokirajuća minor
zapisa, sva četiri iz stilskoga objektiva. Metodološka, skeptička, pedagoška,
dokazna i strukturna leća nemaju završni fatalni, veliki ni minor nalaz.
Zajednički blob nije mijenjan nakon panela.

## Razriješene obvezne zapreke

Prvi dijagnostički panel pregledao je raniji blob i nije upotrijebljen kao
završni dokaz. Njegovih šest velikih prigovora riješeno je prije obveznoga
drugog panela:

1. simulacija dekompozicije sada prethodi oznakama i formulama;
2. SS, MS, `k`, `n`, `k - 1` i `n - k` poučeni su prije računskoga zadatka;
3. odjeljak o pretpostavkama premješten je prije divljine i AI okvira, pa
   fiksna jezgra ostaje neprekinuta;
4. eta- i omega-kvadrat ograničeni su na uzoračke točkaste opise bez
   izmišljene intervalne preciznosti;
5. Tukeyjeva zaštita izrijekom pripada klasičnoj grani zajedničke rezidualne
   varijance, a Welch je ne potvrđuje;
6. sve oznake i koeficijenti dobili su prozno značenje prije formula.

Usput su riješeni svi dijagnostički minor prigovori o potpunoj i djelomičnoj
nultoj situaciji, Monte Carlo nesigurnosti, omnibusu kao lažnoj dozvoli,
planiranim i post-hoc pitanjima, uzročnom jeziku, netočnom superlativu i
neutemeljenoj učestalosti ponašanja asistenta.

## Materijalne obveze i provjere

- `R09-C15-variance-ratio` prolazi: omjer `1,432656498313` samo je
  orijentacijski pokazatelj i nije dokaz pretpostavke ni dozvola za klasičnu
  inferenciju.
- `R23-C15-suspect-code` prolazi: neizvršivi artefakt ima točno jednu pogrešku
  koja mijenja tvrdnju, `p.adjust.method = "none"`; zadatak traži dijagnozu
  fatalnog i korisnog, bez pisanja zamjenskoga koda.
- `R35-REACHBACK-15` prolazi: zadatak dohvaća opisnu nasuprot uzročnoj tvrdnji
  te najmanji važan učinak, a lokalni agregat daje približno `1,30` boda uz
  izričitu zabranu uzročnoga zaključka.
- `R02-C15-dependent-revalidation` ostaje prihvaćen i svježe je revalidiran:
  klasična i Welchova grana dijele skupne sredine i kontraste kao točkaste
  procjene, ali ne i standardne pogreške, stupnjeve slobode, intervale i
  p-vrijednosti.
- Poglavlje 15 podmiruje svoj dio `R22-C14-C16-dependence`: ponovljeni,
  ugniježđeni i povezani redci zaustavljaju običnu inferenciju neovisnih
  opažanja. Višepoglavna stavka i dalje pripada `WD-PART` do poglavlja 16.

Sve klasične, Welchove, rangovne, Tukeyjeve, simulacijske i agregatne brojke
reproducirane su u čistoj sesiji. Citati, podaci, licenca, katalog i ESS granica
prolaze. ESS ostaje neobvezan, portalno posredovan i nepromoviran, bez lokalnih
mikropodataka, checksuma, rezultata ili tvrdnje o redistribucijskom pravu;
obvezni put koristi lokalne CC BY 4.0 datoteke `populacija_medija`.

Widget i statički par prolaze ugovor i paritet. Konceptni graf svjež je s 49
čvorova, 608 bridova, 249 prikazanih ko-pojava i 45 definicijskih bridova.
Ciljani HTML izvršio je svih 13 ćelija; odobreni PDF i DOCX omotači završili su
uspješno u izoliranom worktreeju koji je nakon provjere uklonjen.

## Četiri minor zapisa za autorsku dispoziciju

Sljedeća su četiri stilska zapisa autoru potpuno izložena i prihvaćena kao
poznata i neblokirajuća za ovo izdanje. Nijedan ne mijenja
statističku tvrdnju, rezultat, pretpostavku, citat, odgovor zadatka, ugovor
widgeta ili fiksnu strukturu poglavlja.

1. “Na način na koji je knjiga to radila” kratko personificira knjigu i zvuči
   poput metarečenice o konstrukciji rukopisa.
2. Oznake widgeta “prosjek između” i “prosjek unutar” sintaktički su kraće od
   proznoga termina “prosječne raspršenosti”.
3. Inverzija u rečenici “Zajednički su oblik modela sredina i njegove točkaste
   procjene…” nakratko otežava ključnu razliku između procjene i nesigurnosti.
4. Osam kratkih rečenica u sažetku niže teme inventarnije od ostatka poglavlja.

Prihvaćena dispozicija ostavlja ih bez izmjene zaključanoga izvora.

## Provedena uska dispozicija

Nakon provjere niže navedenoga točnog odgovora C15 provodi samo ovo:

- pomiče `15-vise-grupa` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomiče samo `R09-C15-variance-ratio`, `R23-C15-suspect-code` i
  `R35-REACHBACK-15` iz `ratified` u `accepted`;
- ostavlja `R02-C15-dependent-revalidation` u postojećem statusu `accepted`,
  uz njegovu svježu revalidaciju na konačnom WD-C15 izvoru;
- ostavlja `R22-C14-C16-dependence` u `ratified`, uz već zapisani prolaz
  petnaestoga poglavlja i vlasništvo `WD-PART`;
- evidentira četiri stilska minor zapisa kao autoru izložena, poznata i
  neblokirajuća za ovo izdanje, bez promjene zaključanoga izvora;
- zatvara samo C15, uklanja njegov write lock i tek tada čini `G-A4-16`
  mogućim sljedećim paketom.

Nijedna druga stavka, poglavlje, handoff ili zapis ne mijenja status. Poglavlje
6 ostaje `draft`; poglavlja 7–14 zadržavaju svoja prihvaćena stanja.

## Granice odluke

C15 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge, tag,
arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao poglavlje.
`G-A4-16` ne smije se otvoriti prije točnoga odgovora i zasebnoga C15 closeouta.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
C15 accepted for a385ddc85c11e5d1cf63b33043c1df2a90cff6fb on 2026-08-17
```

Odgovor navodi točan završni WD-C15 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.
