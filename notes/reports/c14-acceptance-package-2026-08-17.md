# C14 — paket za autorovo prihvaćanje četrnaestoga poglavlja

**Gate:** `C14`

**Stanje gatea:** autor prihvatio; uska dispozicija provedena.

**Imenovani vlasnik odluke:** Luka Sikic, autor/editor.

**Datum pripreme:** 17. kolovoza 2026.

**Datum autorove odluke:** 17. kolovoza 2026.

## Konačno materijalno stanje

Konačni izvor četrnaestoga poglavlja nalazi se u WD-C14 closeout commitu
`378bc362f9090e3bcdf8e9e02090c2c1d732e532`. Taj commit sadrži cijeli
vertikalni rez, šest završnih kritičarskih izvještaja, sintezu, w14
revalidaciju i closeout dokaze. Poglavlje nakon toga commita nije mijenjano.

- SHA-256 radne datoteke:
  `84b6c8fac8ce4eecf5474a0535ba02030dbf332a37789bcd7347c4ae9a66cfa2`;
- git blob poglavlja: `6ef3a218dfc61d5ad73f83e236a70e3917909d86`;
- izvještaj vertikalnoga reza:
  `notes/reports/wd-c14-2026-08-17.md`;
- sinteza panela:
  `notes/reports/wd-c14-six-critic-synthesis-2026-08-17.md`.

## Šest završnih izvještaja

Svih šest neovisnih read-only kritičara pregledalo je upravo navedeni git blob:

1. metode — `notes/reports/wd-c14-critic-methods-2026-08-17.md`;
2. skepticizam — `notes/reports/wd-c14-critic-skeptic-2026-08-17.md`;
3. pedagogija — `notes/reports/wd-c14-critic-pedagogy-2026-08-17.md`;
4. dokazi i citati — `notes/reports/wd-c14-critic-evidence-2026-08-17.md`;
5. hrvatski stil — `notes/reports/wd-c14-critic-style-2026-08-17.md`;
6. struktura — `notes/reports/wd-c14-critic-structure-2026-08-17.md`.

Završni panel bilježi nula fatalnih, nula velikih i četiri neblokirajuća minor
zapisa po lećama. Metodološka, pedagoška, dokazna i strukturna leća nemaju
završni nalaz. Zajednički blob nije mijenjan nakon panela.

## Razriješene obvezne zapreke

Prvi panel nad ranijim stanjem utvrdio je osam velikih zapreka. Konačni izvor
i svih šest završnih pregleda potvrđuju da su razriješene:

1. fiksni teorijski prag više se ne zamjenjuje procjenom ranijega vala s
   vlastitom neizvjesnošću, mjerenjem i ciljnom populacijom;
2. dobna analiza više ne tvrdi uzročni „udio zbog dobi”, nego je opisna
   osjetljivost u promijenjenoj ciljnoj populaciji;
3. Belijinih 473 pravilno se opisuje kao autore koji su dovršili zadatak;
4. uklonjena je netočna tvrdnja da Dodatak C nudi lokalnu ESS datoteku;
5. Welch–OLS načelo više se brojčano ne ponavlja prije razrađenoga primjera;
6. ESS odlomak pisan je iz perspektive čitateljeva rada, uz očuvanu upravljačku
   i licencnu granicu;
7. statički par vjerno prenosi preklapanje skupina i usporedbu neovisnoga s
   uparenim dizajnom;
8. AI artefakt i revizijski zadatak auditiraju referentnu skupinu, jedinicu,
   ishod, varijance i doseg populacije.

## D02 dispozicija

D02 ostaje prihvaćena osnova i nije sadržajno izmijenjen. Procjenjuje se
razlika sredina televizija minus društvene mreže, test je dvostran, a Welchov
postupak zadan.

Oba zapisa daju sirovu procjenu `1,185714285714`. Welch daje standardnu
pogrešku `0,372609208160`, `102,471131550669` stupnjeva slobode,
p-vrijednost `0,001935138042` i 95-postotni interval od `0,446686471421` do
`1,924742100008`. Obični homoskedastični OLS daje standardnu pogrešku
`0,369536997510`, 118 stupnjeva slobode, p-vrijednost `0,001717470691` i
interval od `0,453930424466` do `1,917498146963`.

Stoga C14 ostavlja `R02-C14-welch-ols` u postojećem statusu `accepted` i
bilježi samo njegovu svježu revalidaciju na konačnom izvoru.

## Četiri minor zapisa za autorsku dispoziciju

Sljedeći su zapisi autoru potpuno izloženi i prihvaćeni kao poznati i
neblokirajući za ovo izdanje, bez izmjene zaključanoga izvora.

### Skepticizam — 1

1. Izrazi „koliko iznosi učinak” i „ishod ovisi o skupini” mogu kratko imati
   uzročni prizvuk u opažajnom primjeru, iako neposredne ograde izrijekom
   odbijaju uzročno tumačenje.

### Hrvatski stil — 3

2. Jedna rečenica u vinjeti sudara prezent i perfekt.
3. Završetak uparenoga primjera bez glagola zvuči poput slajdovskoga slogana i
   ima suvišan zarez prije sastavnoga „i”.
4. Uvod u razrađeni primjer nakratko najavljuje buduću strukturu knjige umjesto
   da odmah imenuje svrhu usporedbe Welchova i OLS ispisa.

Prvi skeptički i prvi stilski zapis djelomično se dotiču iste rečenice, pa četiri
zapisa po lećama ne znače nužno četiri potpuno neovisna defekta. Nijedan
kritičar nije ijedan od njih ocijenio fatalnim ili velikim.

## Materijalna osnova prihvaćanja

Poglavlje vodi čitatelja od jedinice neovisnosti, procjene i intervala do
Welchova testa, standardizirane razlike i ograničenoga binarnog modelnog
zapisa. Neovisni, upareni i jednouzorački dizajn razdvojeni su, ovisnost
aktivira pravilo zaustavljanja, a opažajne se skupine ne tumače uzročno.

Kritički zadatak stvarno dohvaća operacionalizaciju iz 2. i intervale iz 9.
poglavlja. Obvezni offline zadatak ima izvadak upravljanoga agregata u svim
formatima. ESS ostaje neobvezan, portalno posredovan i nepromoviran, uz
`anweight` i nazivnik valjanih odgovora za konkretnu analizu.

w14 živi izvor i produkcijski adapter imaju isti nepodmemorirani polarni tok,
statički par vjeran je živom argumentu, tolerancija nije proširena, a
asimetrični cache fixture pada zatvoreno. Ciljani HTML, odobreni PDF wrapper i
DOCX wrapper prolaze. Konceptni graf svjež je s 49 čvorova i 602 brida.

## Provedena uska dispozicija

Nakon provjere niže navedenoga točnog odgovora C14 provodi samo ovo:

- pomiče `14-dvije-grupe` iz `draft` u `coauthor_review`, uz izričitu
  bilješku da prihvaćanje ne znači da je autor pročitao poglavlje i da to nije
  faza `final`;
- pomiče samo `R35-REACHBACK-14` iz `ratified` u `accepted`;
- ostavlja `R02-C14-welch-ols` u postojećem statusu `accepted`, uz zapis svježe
  revalidacije D02 na finalnom WD-C14 izvoru;
- ostavlja `R22-C14-C16-dependence` u `ratified`, jer 14. poglavlje sada podmiruje
  svoj dio, ali višepoglavni ugovor ostaje pod `WD-PART` do provjere poglavlja
  15 i 16;
- evidentira četiri minor zapisa kao autoru izložena, poznata i
  neblokirajuća za ovo izdanje, bez promjene zaključanoga izvora;
- zatvara samo C14, uklanja njegov write lock i tek tada čini WD-C15
  mogućim sljedećim paketom.

Nijedna druga stavka, poglavlje, handoff ili zapis ne mijenja status. Poglavlje
6 ostaje `draft`; prihvaćena poglavlja 7–13 ostaju netaknuta.

## Granice odluke

C14 ne autorizira promjenu proze, novi panel, vanjsku poruku, push, merge, tag,
arhiviranje, deployment ili objavu. Ne tvrdi se da je autor pročitao
poglavlje. `WD-C15` se ne smije otvoriti prije točnoga odgovora i zasebnoga
C14 closeouta.

C14 closeout ne mijenja zaključani izvor. Poglavlje 14 napreduje samo u
`coauthor_review`, `R35-REACHBACK-14` u `accepted`, a write lock se uklanja.
To ne znači da je autor pročitao poglavlje i ne daje mu fazu `final`.

## Točan odgovor autora

Odgovor je primljen u aktivnoj niti i zapisan doslovno:

```text
C14 accepted for 378bc362f9090e3bcdf8e9e02090c2c1d732e532 on 2026-08-17
```

Odgovor navodi točan završni WD-C14 commit i datum odluke. Stalna delegacija od
5. kolovoza nije upotrijebljena i ne tvrdi se da je autor pročitao poglavlje.
