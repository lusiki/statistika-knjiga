# C16 — paket za autorovo prihvaćanje šesnaestoga poglavlja

**Gate:** `C16`

**Stanje gatea:** aktivan; kompletan paket pripremljen; čeka točan autorov
odgovor. Gate nije zatvoren.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 18. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor šesnaestoga poglavlja nalazi se u WD-C16 closeout commitu
`9cd5a7983d61d27fe9bb8ca77d8764b419ec857a`. Taj commit sadrži cijeli
vertikalni rez, završne registre, šest kritičarskih izvještaja, sintezu i
closeout dokaze. Poglavlje nakon tog commita nije mijenjano.

- SHA-256 radne datoteke:
  `dc31161a54058a92054e3c3d2ac78cc09bad500984be5db5cda9b4e90fcad671`;
- git blob poglavlja: `99e20c5885ab10a0bbdfaa8981431edf20e556a3`;
- izvještaj vertikalnoga reza:
  `notes/reports/wd-c16-2026-08-18.md`;
- sinteza panela:
  `notes/reports/wd-c16-six-critic-synthesis-2026-08-18.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pročitalo je cijeli završni izvor i
prije i poslije pregleda potvrdilo upravo navedeni SHA-256 i git blob:

1. metode — `notes/reports/wd-c16-critic-methods-2026-08-18.md`;
2. skepticizam — `notes/reports/wd-c16-critic-skeptic-2026-08-18.md`;
3. pedagogija — `notes/reports/wd-c16-critic-pedagogy-2026-08-18.md`;
4. dokazi i citati — `notes/reports/wd-c16-critic-evidence-2026-08-18.md`;
5. hrvatski stil — `notes/reports/wd-c16-critic-style-2026-08-18.md`;
6. struktura — `notes/reports/wd-c16-critic-structure-2026-08-18.md`.

Završni panel bilježi nula fatalnih, nula velikih i četiri neblokirajuća minor
zapisa: jedan skeptički, jedan pedagoški i dva stilska. Metodološka, dokazna i
strukturna leća nemaju završni nalaz. Zajednički blob nije mijenjan nakon
panela.

## Razriješene obvezne zapreke

Ranije runde bile su dijagnostičke i nisu završna evidencija. Njihove obvezne
zapreke razriješene su prije pune završne šestostruke runde:

1. posrednik se više ne prikazuje kao konfundirajuća varijabla, a prilagodba
   razdvaja zajednički uzrok, posrednik i kolider;
2. randomizacija se ne prikazuje kao jamstvo savršene ravnoteže u ostvarenom
   uzorku;
3. linearna projekcija, rezidual i $R^2$ tumače se unutar jasno navedenoga
   cilja, bez latentne istine ili uzročnoga prečaca;
4. interakcija razlikuje nagibe 0,6 i -0,2 od neprimjerenoga zbirnog nagiba
   0,2;
5. prediktivna pogreška provjerava se na odvojenim jedinicama, uz vremensku
   granicu protiv curenja informacija;
6. ovisni redci aktiviraju pravilo zaustavljanja prije obične inferencije
   neovisnih opažanja;
7. binarni most ostaje na čitanju ishoda, referentne skupine, omjera izgleda i
   intervala, bez procjenjivanja logističkoga modela;
8. svi simboli dobili su prozno značenje prije formula, a statički blizanac
   vjerno nosi središnji argument widgeta.

## Materijalna osnova prihvaćanja

Poglavlje sada ima stabilan konačnopopulacijski OLS cilj i razdvaja opis,
predviđanje i uzrok. Povezuje regresiju s dvjema i više grupa, prikazuje
prilagodbu i interakciju, ima stvarnu stanku dohvata, pravilo za ovisne jedinice
i omeđeni čitalački most prema binarnom ishodu.

Prihvaćeni G-A4-16 put proveden je bez refita. Semantički prilagođena Tablica 3
i prilagođeni odlomak rada Kleppang i suradnika prenose AOR 1,60 s
95-postotnim intervalom 1,43–1,80. Atribucija bilježi odabir, skraćivanje,
preoblikovanje i hrvatski prijevod pod CC BY 4.0 te ne tvrdi odobrenje ni pravo
na podatke Ungdata.

w16 i proizvodni adapter koriste isti nepodmemorirani Marsaglia-polar tok.
Paritet svih 17 parova prolazi bez širenja tolerancije, a namjenski
cache-asymmetry fixture pada zatvoreno. Konceptni graf svjež je s 49 čvorova,
620 bridova, 257 prikazanih supojavnih i 45 definicijskih bridova.

Ciljani HTML izvršio je 29 ćelija. Odobreni PDF wrapper vratio je
`PDF_BUILD_OK` za 471 stranicu, a DOCX wrapper završio je izlazom 0 i obnovio
svih 17 privremenih gateova. U sva tri formata potvrđeni su Kleppangov rezultat,
CC BY 4.0 atribucija, posrednik i binarni most. Stil, struktura, figure, citati,
pojmovi, terminologija, rukopis, podaci, widgeti, katalog, ESS, tokeni i
workflow prolaze.

## Četiri minor zapisa za autorsku dispoziciju

Sljedeći su zapisi autoru potpuno izloženi. Predložena je dispozicija da budu
poznati i neblokirajući za ovo izdanje, bez izmjene zaključanoga izvora.

1. Skeptički zapis predlaže aritmetički opis reziduala kao modelne razlike
   umjesto kratkoga izraza „neobjašnjeni dio”.
2. Pedagoški zapis predlaže zaseban `#def-` blok za procjenjivanu veličinu.
3. Stilski zapis bilježi nekoliko suvišnih zareza prije sastavnoga „i”.
4. Stilski zapis bilježi generičku uvodnu rečenicu stanke dohvata.

Nijedan zapis ne mijenja procjenjivanu veličinu, brojčani rezultat,
pretpostavku, citat, odgovor zadatka, widget ugovor ni fiksnu strukturu.

## Točna uska dispozicija koja bi slijedila prihvaćanje

Ako autor pošalje niže navedeni točan odgovor, C16 smije provesti samo ovo:

- pomaknuti `16-regresija` iz `draft` u `coauthor_review`, uz izričitu bilješku
  da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije faza
  `final`;
- pomaknuti samo `R08-C16-cross-design`, `R14-C16-binary-reading`,
  `R14-C16-interaction`, `R14-C16-adjustment-contract`, `R16-C16-table`,
  `R16-C16-paragraph`, `R16-C16-no-refit`, `R29-C16-retrieval` i
  `R35-REACHBACK-16` iz `ratified` u `accepted`;
- ostaviti `R02-C16-dependent-revalidation`, `R09-C16-estimand`,
  `R09-C16-uncertainty` i `R09-C16-leakage-time` u postojećem statusu
  `accepted`, uz zapis njihove svježe revalidacije na konačnom izvoru;
- ostaviti `R22-C14-C16-dependence` u `ratified`: poglavlje 16 podmiruje svoj
  dio, ali višepoglavna stavka ostaje u vlasništvu `WD-PART`;
- evidentirati četiri minor zapisa kao autoru izložena, poznata i
  neblokirajuća za ovo izdanje, bez promjene zaključanoga izvora;
- zatvoriti samo C16, ukloniti njegov write lock i tek tada učiniti `G-A4-17`
  mogućim sljedećim paketom.

Nijedna druga stavka, poglavlje, handoff ili zapis ne mijenja status. Poglavlje
6 ostaje `draft`; poglavlja 7–15 zadržavaju svoja prihvaćena stanja.

## Granice odluke

C16 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge, tag,
arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao poglavlje.
`G-A4-17` se ne smije otvoriti prije točnoga odgovora i zasebnoga C16
closeouta.

Ovaj pripremni korak ne zatvara C16 i ne provodi nijednu predloženu ledger
promjenu. Poglavlje 16 ostaje `draft`, devet novih stavki ostaje `ratified`, a
write lock ostaje na C16 dok čeka autora.

## Točan odgovor autora

Za prihvaćanje ovoga točno određenog stanja odgovorite doslovno:

```text
C16 accepted for 9cd5a7983d61d27fe9bb8ca77d8764b419ec857a on 2026-08-18
```

Svaki drukčiji commit ili datum zahtijeva novu provjeru podudaranja. Umjesto
prihvaćanja možete navesti točne blokirajuće dorade; u tom slučaju C16 ostaje
otvoren i izvor se ne mijenja bez zasebne dispozicije.
