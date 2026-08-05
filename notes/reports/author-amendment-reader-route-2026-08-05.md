# Autorova izmjena — čitateljski pilot se ukida, autor čita gotovu knjigu

**Datum:** 5. kolovoza 2026.

**Nositelj odluke:** Luka Sikić, autor i urednik.

**Dispozicija:** izmjena ratificiranoga plana; pilot s pet čitatelja uklanja se
iz prvoga izdanja, a čitanje se premješta na kraj i obavlja ga autor.

**Izvorno stanje odluke:**
`conversation:author-amendment-reader-route-2026-08-05-Luka-Sikic`.

## Što se mijenja

Ratificirani plan od 3. kolovoza 2026. predviđao je dva čitateljska kruga s
regrutiranim novacima: pilot s pet čitatelja nad poglavljima 1, 8 i 16 **prije**
velikoga pisanja, i usmjerenu čitateljsku provjeru poglavlja 3, 12, 17 i 18
pred izdanje.

Autor prvi krug ukida, a drugi preuzima na sebe. Nijedan čitatelj se ne
regrutira, ne poziva i ne imenuje.

Redoslijed rada zato glasi: **napiši sve, pa autor pročita cjelinu, pa se
mijenja.**

Povučeno je točno sljedeće i ništa više:

- paket `P3-PILOT` — izvan opsega prvoga izdanja, uz zabilježen razlog;
- vanjski upit `OA-P3-PILOT-RECRUITMENT` — `withdrawn_with_reason`;
- vanjski upit `OA-P7-PILOT-RECRUITMENT` — `withdrawn_with_reason`;
- stavka `R26-PILOT-five-reader` — `rejected_with_reason`;
- stavka `R26-META-reading-time` — `rejected_with_reason`, vidi niže.

Paket `P7-PILOT` **nije** ukinut. On ostaje, ali mu se mijenja čitatelj: umjesto
regrutiranih novaka, knjigu u cjelini čita autor. Time se `R26-P7-reader-validation`
i dalje može ispuniti, samo drugim čitateljem.

## Ovisnosti koje se prekidaju

Tri su paketa tražila pilot kao preduvjet. Dvije se veze prekidaju, jedna ostaje.

| Paket | Prije | Sada |
|---|---|---|
| `P3-VERIFY-A` | tražio `P3-PILOT` | veza uklonjena |
| `G-A4-03` | tražio `P3-PILOT` | veza uklonjena |
| `G-A5a` | traži `P7-PILOT` | nepromijenjeno, jer `P7-PILOT` ostaje |

Time pisanje više ne čeka nijednu vanjsku osobu. Prvi paket proze,
`WA-C00`, ovisi još samo o `P3-VERIFY-A`, a taj o registraciji postojećih
podataka i o dvama podatkovnim paketima.

## Prihvaćanje poglavlja: stalna delegacija

Registar nosi devetnaest autorskih vrata prihvaćanja, `C00` do `C18`, po jedna
iza svakoga poglavlja. Autor koji čita tek na kraju ne može ih proći redom.

Autor zato izriče **stalnu delegaciju**: prihvaćanje pojedinoga poglavlja obavlja
unutarnja provjera — panel od šest kritičara i svi deterministički provjeritelji
— a autorov potpis premješta se na jedno čitanje cijele knjige na kraju.

Tri granice te delegacije:

1. Delegacija pokriva **samo** autorsko prihvaćanje. Ne pokriva panel, ne
   pokriva nijednu determinističku provjeru i ne dopušta da se poglavlje zatvori
   s neriješenim fatalnim ili velikim nalazom.
2. Nijedan paket ne smije zabilježiti da je autor pročitao poglavlje. Dokaz za
   klauzulu autorskoga prihvaćanja jest **ova delegacija**, imenovana kao takva,
   i ništa drugo.
3. Autor pri završnom čitanju smije ponovno otvoriti bilo koje poglavlje.
   Ponovno otvaranje ide postojećim mehanizmom poništavanja, a zahvaćena vrata i
   provjere se ponavljaju.

## Vremena čitanja: autorova odluka i njezina granica

Stavka `R26-META-reading-time` tražila je da svako vidljivo vrijeme čitanja dobije
jednu od tri dispozicije: izmjereno, izričito procijenjeno ili uklonjeno.

Autor je 5. kolovoza 2026. odlučio **zadržati postojeća vremena nepromijenjena i
neoznačena**. To je četvrta mogućnost, koju test stavke ne dopušta, pa se stavka
bilježi kao `rejected_with_reason`, a ne kao ispunjena.

Iz toga slijedi obvezujuća granica. Prvo izdanje **ne smije nigdje tvrditi** da su
vremena čitanja izmjerena, testirana na čitateljima ili utemeljena na dokazu — ni
u knjizi, ni u predgovoru, ni u opisu kolegija, ni u metapodacima izdanja. Ta
granica veže `WA-C00`, svaki poglavljni paket, `P5-ROUTES`, `P6-CONTINUITY` i
`P8-META`.

Ista granica vrijedi i za čitatelje općenito: knjiga **ne smije tvrditi** da je
prošla provjeru s novim čitateljima, jer ta provjera nije obavljena. To je isti
oblik granice koju je autor 5. kolovoza 2026. već postavio za nazivlje.

## Što ostaje na snazi

Panel od šest kritičara po poglavlju ostaje. Svi deterministički provjeritelji
ostaju. Svako poglavlje i dalje mora proći svoju kralježnicu, svoje provjere
citata, podataka, figura i strukture, i svoja vrata prihvaćanja. Mijenja se samo
tko potpisuje i kada.

Ostaje i obveza da se nijedan podatak, broj, studija ni izvor ne izmišlja.
Nedostatak čitatelja ne ublažava nijedno pravilo o dokazima.

## Granica ovlasti

Ova izmjena uklanja čitateljski pilot i premješta autorsko čitanje. Ne mijenja
nijednu kralježnicu, nijedan identitetski brif, nijednu prihvaćenu arhitekturu,
nijedno pravilo stila, nijedan `#def-` blok, nijedan skup podataka i nijednu
odluku o pravima. Ne odobrava render, generirani artefakt, push, merge, tag,
arhiviranje, deployment ni objavu.
