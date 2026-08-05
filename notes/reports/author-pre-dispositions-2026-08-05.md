# Autorove prethodne dispozicije — podatkovni izbori, 5. kolovoza 2026.

**Nositelj:** Luka Sikić, autor i urednik.

**Izvorno stanje:**
`conversation:author-data-pre-dispositions-2026-08-05-Luka-Sikic`.

Ovaj dokument bilježi autorove odgovore dane prije nego što ih je nadležni gate
mogao potrošiti. On **ne zamjenjuje** nijedan gate i ne odobrava nijedan paket.
Svaki gate i dalje mora obaviti vlastiti posao, provjeriti vlastite izvore i
zabilježiti vlastiti dokaz. Ako se dispozicija i nalaz gatea raziđu, gate staje i
vraća pitanje autoru.

## DZS turizam — godina snimke

**Pitanje:** koja godina ulazi u snimku.

**Odgovor:** najnovija moguća godina.

**Kako se to čita:** najnovija **cjelovita kalendarska godina** koju je DZS
objavio u trenutku dohvata, prikvačena točnim izdanjem i datumom da kasnije ne
klizi. Nepotpuna tekuća godina ne ulazi, jer bi mjesečni niz bio krnj i
usporedba razdoblja neispravna.

**Tko to izvršava:** `G-A3-DZS` bilježi pravilo, `P3-DZS` prikvačuje stvarnu
godinu, izdanje, datum i kontrolni zbroj kad datoteku doista dohvati. Nijedna
godina nije ovdje imenovana, jer bi to bila tvrdnja o objavi koju ovaj zapis nije
provjerio.

## DIP 2024 — traka

**Pitanje:** ostaje li izborna datoteka portalno posredovana ili se pakira uz
knjigu.

**Odgovor:** ostaje **portalno posredovana**, opcija A.

**Kako se to čita:** knjiga daje službenu poveznicu na izbori.hr, točnu uputu,
izdanje i kontrolni trag, a čitatelj datoteku preuzima sam. Datoteka ne ulazi u
repozitorij.

**Zašto:** inventar `P1B-DATA-LIC` na pregledanoj službenoj stranici nije našao
izričitu licencu ni drugi temelj za redistribuciju. Autorova odredba od 5.
kolovoza 2026. utvrdila je da je izvadak javno dostupan i da dopuštenje nije
potrebno tražiti, ali to nije isto što i objavljena ovlast za ponovnu objavu.
Autor je izabrao opreznu traku. Trenje za čitatelja je malo, a poglavlje 3 upravo
uči prepoznavati tvrdnje koje se ne mogu provjeriti, pa knjiga ondje ne
redistribuira datoteku na neizrečenom dopuštenju.

**Tko to izvršava:** `G-A3-DIP` i `P3-DIP`. Traka u `data/katalog.yml` već jest
`portal-mediated` i ovom se odlukom **ne mijenja**; gate to potvrđuje i bilježi
zakonitu zamjenu za svaki obvezni studentski zadatak.

**Što ostaje zabranjeno:** knjiga ne smije tvrditi da je pribavila dopuštenje
nositelja prava ni za jedan izvor, jer ono nije traženo. `H-P1B-DATA-LIC-003`
nije nadomješten i ostaje obveza `G-A3-DIP`.
