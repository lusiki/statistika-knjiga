# C17 — paket za autorovo prihvaćanje sedamnaestoga poglavlja

**Gate:** `C17`

**Stanje gatea:** prihvaćen; točan autorov odgovor zaprimljen je 19. kolovoza
2026. i uska dispozicija iz ovoga paketa provedena je bez proširenja opsega.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 19. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor sedamnaestoga poglavlja nalazi se u WD-C17 closeout commitu
`bff7106e156a49b51fc55ca4b11c9cd2fc6645f8`. Taj commit sadrži cijeli
vertikalni rez, završne registre, šest kritičarskih izvještaja, sintezu i
closeout dokaze. Poglavlje nakon tog commita nije mijenjano.

- SHA-256 radne datoteke:
  `7e8ff74127f77519434b50afbce50c8354bf019b6a7a2f46684a05c2ecc37e6f`;
- git blob poglavlja: `86e387bbd0df139762001dd22d079d1a51a96c77`;
- izvještaj vertikalnoga reza:
  `notes/reports/wd-c17-2026-08-19.md`;
- sinteza panela:
  `notes/reports/wd-c17-six-critic-synthesis-2026-08-19.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pročitalo je cijeli završni izvor i
potvrdilo upravo navedeni SHA-256 i git blob:

1. metode — `notes/reports/wd-c17-critic-methods-2026-08-19.md`;
2. skepticizam — `notes/reports/wd-c17-critic-skeptic-2026-08-19.md`;
3. pedagogija — `notes/reports/wd-c17-critic-pedagogy-2026-08-19.md`;
4. dokazi i citati — `notes/reports/wd-c17-critic-evidence-2026-08-19.md`;
5. hrvatski stil — `notes/reports/wd-c17-critic-style-2026-08-19.md`;
6. struktura — `notes/reports/wd-c17-critic-structure-2026-08-19.md`.

Završni panel bilježi nula fatalnih, nula velikih, nula manjih i nula korisnih
dodatnih nalaza. Zajednički blob nije mijenjan nakon panela. Ranije
dijagnostičke i međurunde ostaju vidljive u sintezi, ali nisu završna
evidencija.

## Razriješene obvezne zapreke

Prije čistoga završnog panela razriješeno je sljedeće:

1. uzvodna selekcija, labelni put i ParlaSent-only granica točno su opisani;
2. negativni sentiment označen je kao osporiva urednička politika, ne cilj koji
   podatci sami legitimiraju;
3. unutarnja kontrola odvojena je od žalbe pogođene strane, a neovisni uzorak
   nepregledanih rečenica potreban je za procjenu lažno negativnih odluka;
4. tablica zabune, klasifikacijski prag, kodersko pravilo i predviđena
   vjerojatnost ostaju različiti objekti;
5. H10 je zatvoren jednim kratkim vidljivim receiptom u razrađenom primjeru,
   a AI-artefakt sadržava točno jednu pogrešku;
6. završna mapa ima šest revizijskih pitanja i šest dimenzija tvrdnje,
   odgovorivu samoprovjeru i izravan prijelaz u 18. poglavlje;
7. primarni ACL izvor neposredno podupire moderatorski i interkvartilni filtar
   te slučajni odabir testa bez oslanjanja na sentimentne leksikone;
8. H6, H7, nominalni naslov, ritam, personifikacije i revizijski zadatak
   prolaze završni hrvatski stilski pregled.

## Materijalna osnova prihvaćanja

Poglavlje vodi jednu posljedničnu odluku: treba li odabrana parlamentarna
rečenica ući u red za ljudski pregled prije mogućega javnog sažetka. Od te
odluke gradi granicu korpusa, nastanak oznake, razdvajanje dokumenata, prag,
nazivnike, teret pogrešaka, pravednost, prigovor, povratnu spregu i nadzor.
Govorni kontekst, prevalencija, namjera govornika, uzročnost, stvarna
deployment izvedba i prijenos izvan korpusa nisu izmišljeni.

ParlaSentov empirički rad ostaje audit puta oznake, ne izvedba nepostojećega
klasifikatora. Šest sirovih oznaka preslikano je otvoreno. Dva pravila nad 272
retka skupa za provjeru daju TP/FP/FN/TN 122/16/0/134 i 100/1/22/149, FPR
10,7 % i 0,7 %, FNR 0,0 % i 18,0 % te PPV 88,4 % i 99,0 %. Poglavlje izravno
objašnjava zašto dobra izdvojena izvedba ne dokazuje valjanost konstrukta.

w17 ostaje jedini središnji widget. Živi OJS i adapter koriste isti eksplicitni
nekeshirani generator; svih 17 parova prolazi bez širenja tolerancije, a sedam
negativnih fixturea pada zatvoreno. Konceptni graf svjež je s 51 čvorom i 642
brida; terminologija ima 166 kralježničnih oblika i nula divergencija.

Ciljani HTML izvršio je 17 ćelija. Odobreni PDF wrapper vratio je
`PDF_BUILD_OK`, a DOCX wrapper završio je izlazom 0 i obnovio svih 17
privremenih gateova. Stil, struktura, figure, citati, pojmovi, terminologija,
rukopis, spines, inventar, arhitektura, procjene, tokeni, podaci, tekstni paket,
widgeti i paritet prolaze.

## Konačni položaj podataka u knjizi

Katalog ima 20 paketa u tri upravljane putanje:

- devet `bundled` paketa;
- dva `portal-mediated` paketa, `dip_2024` i `ess_r11_hr`, oba nepromovirana;
- devet `external-only` paketa.

Promovirano je točno šest paketa: `anketa_mreze`, `populacija_medija`,
`dzs_turizam`, `eurostat_drustvo`, `parlasent` i `digikat_mediji`. Svih 22
deklariranih snapshotova provjereno je, 50.300 generiranih redaka prolazi
integritet, a nema nedeklarirane datoteke. `parlamint_hr`, `rdp_potpore` i
`bdp_dugi_niz` ostaju bundled, ali nepromovirani. ESS ostaje portalno
posredovan, nepromoviran i bez lokalnih bajtova ili prava na redistribuciju.

ParlaSent-only paket ima 2.698 redaka: 1.090 za učenje, 272 za provjeru i svih
1.336 hrvatskih izvornih testnih redaka za ispitivanje. Uklonjeno je 25
trening-redaka iz 20 dokumenata koji prelaze testnu granicu. Izlazni SHA-256 je
`0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef` i paket
zadržava CC BY-SA 4.0. ParlaMint-HR ostaje nepromoviran i bez govornoga izlaza.

## Provedena točna uska dispozicija

Nakon točnoga odgovora C17 je proveo samo ovo:

- pomaknuti `17-doba-algoritama` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomaknuti samo sljedećih 20 stavki iz `ratified` u `accepted`:
  `R07-C17-full-argument`, `R07-C17-widget-prose-balance`, `R08-SPINE-17`,
  `R13-C17-module-contract`, `R13-C17-boundary-sensitivity`,
  `R13-C17-performance-validity`, `R13-C17-placement`,
  `R14-C17-classification-bridge`, `R23-C17-no-R-production`,
  `R23-C17-visible-receipt`, `R23-C17-no-tokenizer`,
  `R24-C17-primary-sources`, `R24-C17-LLM-prediction`,
  `R24-C17-system-feedback`, `R24-C17-recorded-reference`,
  `R24-C17-label-process`, `R24-C17-selective-observation`,
  `R24-C17-procedural-fairness`, `R24-LADDER-C17` i
  `R35-REACHBACK-17`;
- zapisati da završni panel nema nijedan nalaz koji traži posebnu autorsku
  dispoziciju;
- zatvoriti samo C17, ukloniti njegov write lock i tek tada učiniti `WD-PART`
  mogućim sljedećim paketom.

Nijedna druga stavka, poglavlje ili handoff nije promijenio status. Poglavlje 6
ostaje `draft`; poglavlja 7–16 zadržavaju svoja prihvaćena stanja.

## Granice odluke

C17 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge, tag,
arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao poglavlje.
`WD-PART` je tek nakon ovoga zasebnoga C17 closeouta postao dopušten sljedeći
paket; nije otvoren ni preuzet unutar C17.

C17 closeout ne mijenja izvor poglavlja. Poglavlje 17 prelazi u
`coauthor_review`, točno 20 navedenih stavki prelazi u `accepted`, a C17 write
lock uklonjen je. Ne tvrdi se da je autor pročitao poglavlje ni da je ono
`final`.

## Zaprimljeni točan odgovor autora

Autor je doslovno odgovorio:

```text
C17 accepted for bff7106e156a49b51fc55ca4b11c9cd2fc6645f8 on 2026-08-19
```

Commit i datum podudaraju se s pripremljenim ugovorom. Odgovor prihvaća samo
točno određeno WD-C17 stanje i ne autorizira promjenu proze ni release radnju.
