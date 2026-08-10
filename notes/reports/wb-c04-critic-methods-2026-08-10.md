# WB-C04 — završno izvješće kritičara metoda

**Izvor:** `chapters/04-sazimanje-podataka.qmd`

**Konačni SHA-256:**
`7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`

Kritičar je radio neovisno i samo za čitanje. Konačni prolaz potvrđuje ispravne
jedinice, ključeve, nazivnike, granice mjerenja i tri točna stanja widgeta.

Početni su nalazi uklonili dvije netočne prečace: raspon oko sredine nije
raspon mogućih opažanja, a razlika standardne devijacije i interkvartilnoga
raspona nije mjera ovisnosti o krajnjim vrijednostima. Naknadni je prolaz
otkrio da pogrešni spoj sufiksira stupac kao `platforma.x`; audit sada koristi
upravo taj stupac i blokirajuće potvrđuje 438 ključeva, 3.571 redak i zbroj
5.959.081.

Provjera stvarnoga HTML izlaza potom je otkrila preuranjeno prepisivanje
stupca `objave` u `summarise()`. Konačni izvor prvo računa sredinu, medijan i
prvih deset domena, zatim ukupan zbroj, te asercijama zaključava 153,0832, 4,
148.748 i nazivnik 551.712. Render prikazuje 153,1, 4 i 26,96 %.

## Završna ocjena

- točnost: 5/5
- pretpostavke: 5/5
- tumačenje: 5/5
- preciznost: 5/5
- fatalni / veliki / manji nalazi: 0 / 0 / 0

**Verdikt:** ACCEPT za navedeni konačni hash.
