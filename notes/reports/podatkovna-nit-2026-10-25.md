# Podatkovna nit — 25. listopada 2026.

Stage 1 dovršen je do §9.3 u zasebnom worktreeu `Statistika-podatkovna-nit`, na grani `copy/podatkovna-nit-2026-10-25`, iz `origin/main` na `1167353`. Ovo nije comprehensive-review packet. P6-VERIFY i njegove kontrolne datoteke ostaju netaknuti. Nijedan prijedlog P1–P5 nije proveden.

Uvodima su dodani izvor, jedinica i granica zaključka; uzorci imaju dosljedna imena, a poglavlja 10–16 prate isto pitanje o povjerenju. Predgovor i generirana karta povezuju povratke skupovima. Katalog sada bilježi četiri dodatne nastavne varijante, ukupno 17, i usklađene potrošače. Kuna je zamijenjena eurom na šest mjesta, bez promjene iznosa.

Neto dodatak iznosi **1.129 riječi**, najviše **73 u jednom poglavlju**. Kanonska karta uključena je jednom; mrežna projekcija broji se odvojeno. W1 ima 170 zapisa, uključujući konstrukcije i citirane slučajeve. Karta prikazuje registrirane pakete i dopuštene varijante: zato ne prikazuje sve W1 konstrukcije, laboratorijski dokazni CSV ni neregistrirane uzorke poglavlja 9. Ta je granica izričita, a ne proglašena potpunom jednakošću W1 i karte.

Usporediv početni i završni rezultat provjera je **27/30**. Iste postojeće pogreške ostaju u B (trag „Luka Sikic”), D (`print-reference-spread-markers`) i E (zastarjeli hash conventions). Prvi sirovi baseline bio je 23/30 jer worktree nije imao postojeće ignorirane ParlaSent ulaze; četiri provjere prošle su nakon lokalne kopije s jednakim hashovima, bez mrežnog dohvata podataka. Detaljni zapisi nalaze se u [JSON izvještaju](podatkovna-nit-2026-10-25.json).

Sva tri neovisna kritičara potvrdila su izmjene nakon jednog ponovnog pregleda. Deterministički stilski linter nema pogodaka; meka strukturna upozorenja pojedinačno su razvrstana i nisu razlog za preuređivanje ratificiranih odjeljaka u ovom prolazu. **331 usporedba zaštićenih cjelina i datoteka prolazi prema sadržajnom HEAD-u.**

PDF kroz obvezni wrapper, cijeli HTML, provjera renderiranog HTML-a i AI release validation prolaze. Svi izmijenjeni odlomci poglavlja vizualno su pregledani u oba izdanja. Dodaci A–C i stranica Podaci postoje samo u HTML-u prema postojećem filtru tiskanog izdanja. Širine stupaca nove karte ispravljene su nakon pregleda. Ostaje sitna tipografska napomena: na PDF stranici 148 identifikator `anketa_mreze` rastavljen je preko retka, bez izgubljenog teksta. Izlazi `docs/`, `_freeze/`, `pdf/` i `word/` nisu dio commitova.

## Odluke P1–P5

| Prijedlog | Preporuka |
|---|---|
| **P1 — zajednički uzorak** | **Ne konsolidirati.** Jedini dopušteni kandidat, postojeći uzorak 800/1313, ruši intervalnu premisu vježbe 14 i tvrdnju TV–tisak u 15. |
| **P2 — novi položaji odobrenih izvora** | DZS usporedba administrativnog dolaska i anketnog putovanja u **poglavlju 2**; jedan Eurostatov prikaz zaposlenosti i siromaštva u **6**. ESS sada bez promjene. |
| **P3 — stvarne uvodne odluke** | Zamijeniti uvode **11 (Bond), 14 (Allcott) i 16 (Chetty)**; zadržati 9 i 15 uz navedenu uredničku granicu. Primarni puni tekstovi provjereni; nacrti i bibliografski zapisi samo su u prijedlogu. |
| **P4 — pokrivenost područja** | Prvo P2/P3. BDP, RDP i V-Dem ostaju kandidati iza zasebnih licenčnih i autorskih zapreka. |
| **P5 — laboratorijski CSV** | Zadržati kao urednički dokaz izvan portfelja; eventualno dodati odvojenu poveznicu na dokazni izvještaj. Bez promocije ili promjene ograničenja broja paketa. |

P1 daje grupe portal 233, mreže 197, TV 185, radio 100 i tisak 85. U podskupini 30–49 interval postaje **[0,389; 1,505]**, pa više ne obuhvaća nulu. Tukeyjev interval TV–tisak postaje **[−1,337; −0,022]**. Potpuna usporedba svih zadanih sidara, reproducibilni skript, provjerene lokacije troška te nacrti P2–P5 nalaze se pod `proposals` u JSON-u.

G-A3-ESS dopušta opcionalne portalne uporabe u 8, 13, 14, 15 i 16; nije ograničen samo na 8. D08 ipak ne dopušta bundling ni promociju. Novi MD5 kataloga trebat će svjesno uskladiti kad se P6-VERIFY nastavi; njegova zaustavljena matrica ovdje nije mijenjana.

Odgovor za odluku može glasiti:

`Odobravam P2-DZS u poglavlju 2 i P3-14; odbijam P1. P2-Eurostat, P3-11, P3-16, P4 i P5 odgađam.`

Lokalni commitovi su autorizirani. Nema pusha, pull requesta, mergea ni početka Stage 2.
