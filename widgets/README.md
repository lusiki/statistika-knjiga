# Interaktivni grafovi (widgeti)

Sedamnaest widgeta, jedan po poglavlju osim završnice. Popis je
[`data/widgets.json`](../data/widgets.json) i on je jedini izvor istine —
stranica `interakcije.qmd` ga čita, a ovaj dokument opisuje kako se widget
gradi.

## Redoslijed izrade

Četiri widgeta nose glavnu argumentaciju knjige i grade se prvi, prije nego
ijedno poglavlje bude dovršeno. Ako oni rade, radi i knjiga.

| Red | Widget | Poglavlje | Zašto prvi |
|-----|--------|-----------|------------|
| 1 | `w08` CLT stroj | Uzorkovanje | pedagoški zglob cijele knjige |
| 2 | `w09` Hvatač intervala | Procjena | tumačenje intervala pada ili prolazi ovdje |
| 3 | `w10` Simulator p-vrijednosti | Logika testiranja | definira p-vrijednost bez formule |
| 4 | `w12` Pješčanik p-hakiranja | Kriza i obnova | čitatelj sam proizvede lažni nalaz |

Ostali slijede redoslijed pisanja poglavlja.

## Anatomija widgeta

Svaki widget ima četiri dijela, i sva četiri su obavezna.

1. **Uvodni pasus** u glasu poglavlja, prije grafa. Kaže što se vidi i zašto je
   važno baš ovdje. Naslov iznad grafa ga ne zamjenjuje (STYLE.md).
2. **Upravljačka ploča** — jedan `Inputs.form`. Ne stilizira se i ne omata
   ručno; `styles/book-include.html` je automatski sklapa u `<details>`,
   dodaje ispunu klizača i gumb za povratak na početne vrijednosti.
3. **Graf** — jedan OJS blok s `label` i `fig-cap`, i uvijek `fig-alt`.
4. **Blok „Što isprobati"** — podebljani uvod pa numerirani pokusi, od očitog
   slučaja prema protuintuitivnom. Također se automatski sklapa.

Uz njih ide **statički blizanac** za tisak, R blok iza
`when-format="pdf"` gate-a. Obrazac je u `CLAUDE.md`.

## Pravila

- **Bez vanjskih biblioteka.** Observable stdlib, `d3` i `Plot` dolaze s
  Quartom. Sve ostalo je ovisnost koja jednog dana pukne.
- **Bez sirovih boja.** Boje se čitaju iz CSS varijabli, pa widget prati temu i
  radi u tamnom načinu:
  ```js
  const boja = getComputedStyle(document.documentElement)
    .getPropertyValue("--tok-accent").trim();
  ```
- **Determinizam gdje je moguć.** Simulacija koja se pokreće sama od sebe treba
  vlastiti generator sa sjemenom (`d3.randomLcg(42)`), inače se pri svakom
  otvaranju vidi druga slika i tekst uz nju laže.
- **Početne vrijednosti su one koje se predaju.** Graf mora biti razumljiv prije
  nego čitatelj išta pomakne, jer većina neće.
- **Jedna ideja po widgetu.** Ako ploča ima više od četiri kontrole, widget
  vjerojatno radi dva posla.
- **Pristupačnost.** `fig-alt` opisuje što se vidi pri početnim vrijednostima.
  Widget nije jedini put do tvrdnje; proza je nosi i bez njega.

## Predložak

`widgets/_predlozak.qmd` sadrži gotov par (ploča, graf, blizanac) koji se
kopira u poglavlje i preimenuje.

## Statički blizanci

Blizanac ne mora biti isti graf. Mora nositi istu tvrdnju pri jednoj razumnoj
postavci parametara. Gdje interaktivni graf pokazuje kretanje, blizanac često
pokazuje tri stanja jedno uz drugo (mali višekratnici).

Blizanci se crtaju s `theme_knjiga()` i paletom `boje_knjige`, ili sivim nizom
`sivo` ako se tiska jednobojno.
