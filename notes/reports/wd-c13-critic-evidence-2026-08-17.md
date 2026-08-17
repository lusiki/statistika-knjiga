# WD-C13 — dokazni kritičar

Read-only pregled izveden je nad cijelim zaključanim izvorom:

- očekivani i opaženi SHA-256:
  `6cd97e3dae0a83dcf3daa8f7450fac0324390ef14b7df87308a29a6caa240015`
- podudaranje: da

## Ocjene

| Dimenzija | Ocjena |
|---|---:|
| Integritet citata | 5/5 |
| Potpora tvrdnjama | 4/5 |

## Snage

- Sva četiri citatna ključa postoje u `references.bib`. Bickel i suradnici
  podupiru Berkeley, Cochran povijest i nijansirani status praga pet, Cohen
  ograničenje orijentacijskih pragova, a Simpson opasnost agregiranja slojeva.
- Neovisna reprodukcija u čistom procesu R 4.6.0 potvrdila je `N = 800`,
  hi-kvadrat `149,783993`, 12 stupnjeva slobode, najmanju očekivanu frekvenciju
  `14,34375`, `V = 0,249820`, sve navedene postotke i reziduale, oba testa
  prilagodbe, spojenu tablicu te sve simulacije s 4.000 ponavljanja.
- `populacija_medija` označena je kao simulirana prije prve podatkovne brojke.
  Sjemena su 8001 za generator, 1313 za poglavni uzorak i 1314 za simulacije;
  lokalni MD5 zapisi podudaraju se s katalogom.
- ESS ostaje neobvezan, portalan i u vlasništvu čitatelja, s analitički
  specifičnim nazivnikom i ponderom `anweight`; knjiga ne nosi mikropodatke ni
  ESS rezultat.

## Nalazi

Sva su četiri nalaza minor:

1. Tvrdnja da „sve brojke” potječu iz uzorka od 800 nije točna jer kasniji
   rezultati dolaze iz zasebnih simulacija i teorijske hi-kvadrat granice.
   Tvrdnju treba ograničiti na glavni primjer s medijima.
2. „ESS ruta iz Dodatka C” ne postoji u trenutačnom Dodatku C; stvarni se zapis
   nalazi u `data/ess_r11_hr/PUTOVNICA.md`. Proza treba izravno uputiti na
   putovnicu ili ne tvrditi da Dodatak C sadrži rutu.
3. Komparativna tvrdnja da se nazivnik izostavlja češće od bilo kojeg drugog
   elementa i tvrdnja o raširenosti pravila pet u udžbenicima, recenzijama i
   programskim izlazima nisu izravno potkrijepljene. Treba ih ublažiti ili
   dodati provjeren izvor.
4. Generalizacije o tome što asistenti „obično”, „često” i „redovito” rade
   nemaju imenovanu evaluaciju ni omeđen model i verziju. Treba ih preoblikovati
   kao moguće pogreške koje čitatelj provjerava ili ih potkrijepiti.

## Nedostaje ili nije provjereno

- Nema citatnog ključa odsutnog iz bibliografije.
- „Sve brojke potječu iz uzorka od 800” proturječi kodu.
- „ESS ruta iz Dodatka C” nije prisutna u trenutačnom dodatku.
- Tri opće tvrdnje o učestalosti nemaju dovoljnu dokaznu osnovu.

## Presuda

Citatni i središnji podatkovni temelj prolaze bez fatalnog ili major nalaza;
četiri omeđene minor praznine ostaju za autorsku dispoziciju.

## Završni ponovni pregled nakon odobrene dorade

Ponovni read-only pregled cijeloga izvora potvrdio je SHA-256
`b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`.
Svih osam odobrenih dorada prolazi. Četiri citatna ključa postoje u
`references.bib`; interval `47,4–65,3`, GOF odstupanje od `1,8` postotnih
bodova te parovi hi-kvadrat/V neovisno su reproducirani. Nijedna dorada nije
uvela izmišljeni rezultat, citat, ESS nalaz ili empirijski broj.

| Dimenzija | Ocjena |
|---|---:|
| Integritet citata | 5/5 |
| Potpora tvrdnjama | 4/5 |

### Snage

- `bickel1975`, `cochran1954`, `cohen1988` i `simpson1951` podupiru pripadne
  tvrdnje.
- Simulirani status `populacija_medija`, sjeme i licencni trag ostaju jasni.
- Lažna ESS ruta iz Dodatka C više nije prisutna.

### Preostali nalazi

1. **Minor — podrijetlo svih brojki.** Tvrdnja da sve brojke potječu iz uzorka
   od 800 proturječi zasebnim simulacijama i teorijskoj hi-kvadrat granici;
   treba je ograničiti na glavni primjer.
2. **Minor — učestalost izostavljenoga nazivnika.** Komparativna tvrdnja da se
   nazivnik izostavlja češće od bilo kojeg drugog elementa nema izravnu
   dokaznu potporu.
3. **Minor — raširenost pravila pet.** Cochran podupire status praktične
   preporuke, ali ne i zasebnu tvrdnju o učestalosti u udžbenicima, recenzijama
   i programskim izlazima.
4. **Minor — ponašanje asistenata.** Tvrdnje da asistenti „obično”, „često” i
   „redovito” griješe nisu vezane uz evaluaciju, model ni verziju.

Nema ključa odsutnoga iz bibliografije ni nereproducirane poglavne brojke.
Četiri samostalna minora ostaju za `C13`.

### Završna presuda

Nema fatalnoga ni major nalaza. Dokazni ponovni pregled prolazi uz četiri
neblokirajuća minora.
