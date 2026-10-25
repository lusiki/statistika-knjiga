# Licenca i obavijest uz izvatke skupa `digikat_mediji`

Ova obavijest putuje uz datoteke `digikat-platforme-godisnje.csv`,
`digikat-platforme-mjesecno.csv` i `digikat-izvori.csv` i mora ostati uz njih
pri svakom dijeljenju, preuzimanju ili prilagodbi.

| Polje | Vrijednost |
|---|---|
| Skup | `digikat_mediji` |
| Izvor | DigiKat — *Prikaz i analiza katoličke tematike u digitalnom medijskom prostoru*, Hrvatsko katoličko sveučilište |
| Voditelj projekta i nositelj prava | doc. dr. sc. Luka Šikić |
| Uzvodne datoteke | `data/processed/platform_summary.rds`, `platform_monthly.rds`, `source_summary.rds` |
| Licenca | [Creative Commons Imenovanje 4.0 međunarodna (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode) |
| Objava uvjeta | [`DATA_AVAILABILITY.md`](https://github.com/lusiki/DigiKat/blob/main/DATA_AVAILABILITY.md) u repozitoriju projekta |
| URI izvora | <https://github.com/lusiki/DigiKat> (repozitorij), <https://lusiki.github.io/DigiKat/> (stranica projekta) |
| Raspon korpusa | siječanj 2021. — lipanj 2026. |
| Izvadak izradio | `scripts/build-digikat-extracts.R` |

Primjer atribucije glasi „Šikić, L. i sur. (2025.–2027.). *Prikaz i analiza
katoličke tematike u digitalnom medijskom prostoru*. Hrvatsko katoličko
sveučilište, agregati `data/processed/`, CC BY 4.0; izmjene su označene.”

## Što je licencirano, a što nije

DigiKat izričito razdvaja dvije stvari. **Puni korpus** od približno 710.000
objava nije u repozitoriju projekta, nije redistribuiran i **ne ulazi ovamo**;
u katalogu ove knjige on stoji zasebno kao `determ_korpus` u traci
`external-only`, jer potječe iz komercijalnog servisa za praćenje medija.
**Agregatne tablice** iz `data/processed/` projekt objavljuje pod CC BY 4.0 uz
izričitu napomenu da ne sadrže osobne podatke. Ovi izvadci nastali su isključivo
iz tih agregatnih tablica.

To znači i sljedeće: nijedna brojka odavde ne može se raščlaniti natrag na
pojedinačnu objavu, i to nije nedostatak izvatka nego uvjet pod kojim postoji.

## Oznaka izmjena

CC BY 4.0 traži navođenje izvora, poveznicu na licencu i **oznaku svake
izmjene**. U ovim datotekama promijenjeno je točno ovo i ništa više:

1. **Odabir.** Checkout projekta drži četrnaest praćenih agregatnih tablica.
   Preuzete su tri. Deset preostalih tablica imenuje aktere i nisu preuzete.
   Jedanaesta, `proportions_summary.rds`, ne imenuje nikoga, ali nosi udjele u
   pomičnom zarezu bez nazivnika, pa je izostavljena iz zasebnoga razloga.
   (Projektni `DATA_AVAILABILITY.md` govori o deset tablica; to je njegov
   zastarjeli broj, ne drukčiji skup.)
2. **Imena stupaca.** Prevedena su na hrvatski. Izvorne oznake platformi
   (`web`, `youtube`, `facebook`, `twitter`, `reddit`, `forum`, `instagram`,
   `comment`, `tiktok`) prenesene su doslovno i nisu prevedene.
3. **Zbrajanje po godinama.** U `digikat-izvori.csv` godišnji redci uzvodne
   tablice zbrojeni su u jedan redak po izvoru, a `godine_prisutnosti` bilježi
   koliko je godina izvor uopće bio prisutan.
4. **Filtar imenovanja.** U `digikat-izvori.csv` zadržani su samo izvori čije je
   ime gola internetska domena. Stranice, kanali i osobni računi — koji u
   uzvodnoj tablici uključuju imenovane pojedince — **izostavljeni su u
   cijelosti**.
5. **Mala slova.** Imena domena svedena su na mala slova, pa se `Bitno.net` i
   `bitno.net` broje kao isti izvor.
6. **Dodan stupac `metrika_dostupna`.** Nova je oznaka, ne nova brojka; vidi
   sljedeći odjeljak.
7. **Dodan stupac `objave_godina_ukupno`.** Nazivnik godišnjeg udjela, upisan
   umjesto uzvodnog udjela u pomičnom zarezu.
8. **Izostavljen `avg_engagement_rate`.** Uzvodni je stupac prosjek omjera po
   objavi i ne smije se zbrajati kroz godine. Čitatelj koji želi stopu gradi je
   iz dvaju zbrojeva, što je omjer zbrojeva i ispravna veličina.
9. **Ispravljena oznaka `godina_potpuna`.** Oznaka se izvodi iz svih dvanaest
   opaženih mjeseci. Zato je `ne` za 2024., kojoj nedostaju veljača–svibanj i
   kojoj je siječanj djelomičan, te za završnu 2026.
10. **Dodan `lom_metode`.** Oznaka čuva ulazak TikToka od srpnja 2023., lom
    serije u lipnju 2024. i ulazak Instagrama od srpnja 2024. kao dijelove
    podataka, a ne kao napomenu koju je lako previdjeti.

Nijedna brojčana mjera nije zaokružena, popravljena ni pretvorena. Promijenjene
su samo izvedene oznake kvalitete opisane gore.

## Nula koja nije nula

Ovo je najvažnija napomena uz skup i ona je razlog zašto je uopće odabran.

Uzvodni agregat upisuje **0** za interakcije i **0** za doseg na platformama
`reddit`, `forum` i `comment`, i to u svih šest godina. To nije izmjerena nula:
servis za praćenje medija za te vrste izvora **uopće ne isporučuje mjere
angažmana**. Konvencija ove knjige traži da nula i nedostajuća vrijednost ostanu
različite, a prekodiranje tuđe brojke nije posao izvatka. Zato izvadak radi oboje:
prenosi uzvodnu vrijednost doslovno **i** nosi stupac `metrika_dostupna`
(`da`/`ne`).

Tko prosječi interakcije po platformama ne pogledavši `metrika_dostupna`, dobit
će krivi odgovor. To je namjerno.

U `digikat-izvori.csv` istoga stupca nema, jer uzvodna tablica ondje ne razlikuje
platforme; 515 izvora ima doseg 0 i za njih vrijedi ista sumnja. Datoteka ima
3.604 imenovane domene i one nose 551.712 od ukupno 710.307 objava, odnosno
77,67 %. Svaki udio iz te datoteke zato ima nazivnik 551.712, ne 710.307.

## Što ovaj skup jest, a što nije

Korpus **nije uzorak hrvatskoga medijskog prostora**. Objava ulazi u njega ako i
samo ako sadrži **najmanje dva različita katolička pojma** iz projektnog popisa.
To je namjerno selektiran korpus s poznatim pravilom ulaska, a ne slučajan uzorak
iz poznate populacije. Svaka tvrdnja iz ovih datoteka odnosi se na *objave o
katoličkim temama u praćenim izvorima*, nikada na medije općenito, i nikada na
javno mnijenje.

Godini 2024. nedostaju veljača–svibanj, a siječanj joj je djelomičan s 1.911
objava. Godina 2026. obuhvaća samo šest mjeseci. Obje nose
`godina_potpuna = ne`. Mjesečni prikaz mora pokazati rupu 2024., bez
interpolacije ili izglađivanja.

Godišnja i mjesečna datoteka odstupaju u 17 od 49 ćelija platforma–godina. U
smjeru mjesečno minus godišnje najveće je odstupanje +446 za `web` 2022., a
najmanje −389 za `web` 2024. Zbroj odstupanja iznosi točno 0 i obje datoteke
zbrajaju 710.307 objava. Odstupanje je zato zabilježeno i provjerava se, a nije
skriveno prepisivanjem jedne datoteke preko druge.

Nema zakonite tvrdnje o rastu ili trendu kroz 2024. Usporedba razdoblja prije i
nakon lipnja 2024. mora izrijekom navesti lom metode i promjenu obuhvata
platformi; stupac `lom_metode` služi upravo tome.

„Doseg” je procjena pružatelja usluge, a ne izmjeren broj ljudi. Nije zbroj
različitih osoba i ista se osoba može brojiti više puta.

Licenca se odnosi na podatke. Kod izvatka, izvorni tekst knjige i pridružena
dokumentacija ostaju pod MIT licencom repozitorija, a materijali trećih strana
vode se pod vlastitim uvjetima i ova ih obavijest ne obuhvaća.
