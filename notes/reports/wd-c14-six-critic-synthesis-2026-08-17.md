# WD-C14 — sinteza šest završnih kritičara

Svih šest neovisnih read-only leća pregledalo je isti zaključani izvor:

- putanja: `chapters/14-dvije-grupe.qmd`;
- SHA-256: `84b6c8fac8ce4eecf5474a0535ba02030dbf332a37789bcd7347c4ae9a66cfa2`;
- git blob: `6ef3a218dfc61d5ad73f83e236a70e3917909d86`.

Pokriveni su statističke metode, skepticizam, pedagogija, dokazna osnova,
hrvatski rukopisni stil i struktura. Svaka je leća izrijekom potvrdila isti
git blob prije čitanja.

## Ishod prvoga prolaza i provedena revizija

Prvi panel nad ranijim materijalnim stanjem zabilježio je osam velikih i deset
manjih zapisa po lećama. Veliki nalazi odnosili su se na status fiksnoga praga,
uzročni prizvuk dobne analize, opis Belijina uzorka, nepostojeću offline ESS
rutu, ponovljene Welch–OLS brojke, administrativni ton ESS odlomka, nevjeran
statički par te nedostatan audit referentne skupine i pretpostavki.

Revizija je uklonila svih osam velikih zapreka. Ujedno je ispravila uparenu
formulu, opis Shapiro–Wilkova testa, terminologiju Wilcoxonova postupka,
pedagoški redoslijed Welch–OLS načela, pojedine dokazne ograde i lokalne stilske
nespretnosti. Nakon svake materijalne promjene cijeli je izvor ponovno poslan
svih šest kritičara.

## Završni panel

| Leća | Fatalno | Major | Minor |
|---|---:|---:|---:|
| Metode | 0 | 0 | 0 |
| Skepticizam | 0 | 0 | 1 |
| Pedagogija | 0 | 0 | 0 |
| Dokazi i citati | 0 | 0 | 0 |
| Hrvatski stil | 0 | 0 | 3 |
| Struktura | 0 | 0 | 0 |
| **Ukupno po lećama** | **0** | **0** | **4** |

Metodološka leća potvrđuje D02, Welchovu zadanu ulogu, jednakost sirove
procjene s binarnim OLS koeficijentom i različitu neizvjesnost. Skeptička leća
potvrđuje da fiksni prag i procjena ranijega vala više nisu zamijenjeni te da
dobna analiza nema uzročnu dispoziciju. Pedagoška i strukturna leća potvrđuju
reach-back, referentnu skupinu, offline put i vjernost statičkoga para. Dokazna
leća reproducira brojke, citate, agregat i ESS granicu. Stilska leća potvrđuje
da su ranija ponavljanja i administrativni ton uklonjeni.

## Četiri neblokirajuća minora

1. Dva izraza u opažajnom primjeru mogu kratko imati uzročni prizvuk: „učinak”
   i „ishod ovisi o skupini”.
2. Vinjeta na jednom mjestu sudara prezent i perfekt.
3. Završetak uparenoga primjera bez glagola zvuči poput slajdovskoga slogana.
4. Uvod u razrađeni primjer kratko najavljuje buduću strukturu knjige umjesto
   da odmah imenuje svrhu usporedbe dvaju ispisa.

To su zapisi po lećama; prvi skeptički i prvi stilski zapis djelomično se
dotiču iste rečenice, pa ne znače nužno četiri neovisna defekta. Nijedan nije
uređen nakon zaključavanja izvora. Svi ostaju vidljivi za zasebni `C14` gate.

## Suglasnost i nesuglasnost

Svih šest leća slaže se da nema fatalne ili velike zapreke. Slažu se i da
poglavlje čuva procjenu prije testa, zaustavlja se pri ovisnim jedinicama,
razlikuje neovisni i upareni dizajn, ne izvodi uzročni zaključak iz opažajnih
skupina te ograničeno priprema modelni zapis 16. poglavlja.

Jedina razlika u naglasku jest terminološka: skeptička leća uzročni prizvuk
bilježi kao minor normativne preciznosti, dok ga metodološka leća uz postojeće
ograde ne smatra inferencijskom pogreškom. Sinteza zadržava strožu, skeptičku
oznaku i izlaže je autoru.

## Konačna presuda

`WD-C14` prolazi završni šesteročlani panel. Svih osam ranijih velikih zapreka
razriješeno je na istom konačnom izvoru; nema fatalnoga ni major nalaza.
Četiri neblokirajuća minor zapisa ostaju neuređena i čekaju autorsku
dispoziciju u zasebnom `C14` gateu.
