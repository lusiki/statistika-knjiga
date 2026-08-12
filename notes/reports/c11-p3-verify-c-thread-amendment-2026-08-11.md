# Autorski amandman za nit C11–P3-VERIFY-C

**Odluka:** `A-THREAD-C11-P3-VERIFY-C-2026-08-11`

**Datum odluke:** 11. kolovoza 2026.

**Datum zapisa:** 12. kolovoza 2026.

**Autor i urednik:** Luka Sikic

## Odluka

Za ovu nit uobičajeno pravilo zaustavljanja nakon jednoga paketa zamjenjuje se
strogim slijedom od pet paketa:

```text
WC-C11 -> C11 -> G-A4-12 -> P3-EVIDENCE12 -> P3-VERIFY-C
```

Ovo je nova i zasebna odluka. Ne zamjenjuje
`A-THREAD-C07-C09-2026-08-11` ni `A-THREAD-C08-C10-2026-08-12`; oba su njihova
lanca završila. Svaki od pet paketa ostaje zasebna jedinica rada. Najviše jedan
paket smije imati aktivnu pisanu bravu. Svaki se zasebno claim-a, dokazuje,
handoff-disponira, zatvara, provjerava kroz `scripts/check-review-workflow.R` i
commit-a prije claimanja sljedećega. Dokaz, brava ili nedovršena dispozicija ne
prenose se preko paketne granice. Amandman ne ukida nijedan paketni ni stavkovni
preduvjet.

## Paketne granice

- `WC-C11` provodi samo ratificirani vertikalni rez jedanaestoga poglavlja.
  Prije prvoga sadržajnog uređivanja priznaje `H-P2-VERIFY-001`,
  `H-P3-EXISTING-002` i `H-WB-C06-001`, a prije closeouta svaku isporuku troši
  s točnom dispozicijom i dokazom. Vraća kanonski sedmerodijelni redoslijed,
  zatvara samo `R04-C11-fixed-order` i izrijekom ostavlja tri druga otvorena
  djeteta R04 njihovim vlasnicima. Završni izvor dobiva šest neovisnih
  read-only kritičara u paralelnom panelu.
- `C11` se ne smije zatvoriti bez točnoga, datiranog odgovora autora vezanog uz
  završni WC-C11 commit. Stalna delegacija od 5. kolovoza nije zamjena, a
  prihvaćanje ne znači da je autor pročitao poglavlje.
- `G-A4-12` je samo odluka o briefu, javnoj tvrdnji i izvorima, argumentacijskom
  nacrtu, definicijama i widgetu, podacima i pravima, nedostupnim tvrdnjama,
  alternativama, granici ovlasti i blokiranim ovisnostima za poglavlje 12. Ne
  dohvaća podatke, ne promovira paket i ne uređuje prozu.
- `P3-EVIDENCE12` gradi samo provjerljiv dokazni paket za životni ciklus,
  osjetljivost i šumski prikaz poglavlja 12. Svaka tvrdnja mora se vezati uz
  stvaran provjeren izvor i točan ključ u `references.bib`; neprovjerljiva se
  tvrdnja izrijekom isključuje.
- `P3-VERIFY-C` provjerava svaki preduvjet zasebno protiv jednoga deklariranog
  izvornog stanja, na njegovu vlastitom ugovoru, ponavlja determinističke i
  negativne provjere te ne skriva blokator agregiranom ocjenom.

## Trajne granice

Poglavlje 6 ostaje namjerno u fazi `draft` pod `H-WB-PART-001` do svježega
panela u `P6-PANELS`; ova ga nit ne uređuje, ne unapređuje i ne panelira.
DigiKat i Eurostat zadržavaju sve ratificirane granice metodskoga prekida,
nazivnika, mjerljivosti platformi i jaza 2024. ESS ostaje portalno posredovan i
nepromoviran, bez lokalnoga paketa, tvrdnje o paritetu izdanja ili dopuštenju
vlasnika prava. Nijedan paket ne smije tvrditi da su vremena čitanja izmjerena
ili čitateljski testirana, da su novi čitatelji validirali knjigu ili da je
terminologija neovisno recenzirana.

## Uvjeti zaustavljanja i granica ovlasti

Nit se zaustavlja prije sljedećega paketa ako stvarni dokaz ne zadovolji izlazni
test, ako ostane fatalan ili neriješen veliki nalaz panela, ako se sedmerodijelni
redoslijed jedanaestoga poglavlja ne može čisto vratiti ili ako bi zatvaranje
zahtijevalo izmišljanje broja, izvora, studije ili citata. Djelomično i pošteno
zaustavljanje tada je ispravan ishod.

Odluka ne spaja pakete, ne dopušta drugu pisanu bravu, ne ukida preduvjet,
handoff, stavku, panel, determinističku provjeru ni autorski odgovor. Samo
root/conductor smije pisati kontrolne datoteke i Bookwright registre; kritičari
ostaju read-only. Odluka ne autorizira push, merge, tag, arhiviranje, deployment
ili objavu.
