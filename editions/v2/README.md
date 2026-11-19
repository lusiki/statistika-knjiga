# Druga radna inačica

[Otvori drugi PDF](../../pdf/Statistika-v2.pdf) ·
[Otvori sačuvani prvi PDF](https://github.com/lusiki/statistika-knjiga/blob/e240baee664772257895ccd388672d65e25c3911/pdf/Statistika.pdf)

Ova zasebna stilska revizija od 19. studenoga 2026. povezuje odlomke koji
razvijaju istu misao i produljuje odabrane kratke rečenice prema njihovu
značenjskom odnosu. Obuhvaćeni su predgovor, svih 18 poglavlja i objašnjenja
u svih sedam mrežnih dodataka. Definicije, zadaci, postupci u programu i
rječničke natuknice zadržavaju granice potrebne za čitanje i provjeru.
PDF zadržava opseg tiskanoga izdanja; mrežni dodaci priloženi su kao izvori.
Naziv korpusa usklađen je i u dvama zapisima iz kojih se generiraju rješenja.

Empirijski medijski izvadak opisuje se kao **korpus digitalnih medija**,
uz zadržane granice tematskog odabira, obuhvata, mjerenja i dopuštenih
zaključaka. To je opisna oznaka istog nastavnog izvatka. Izvorna atribucija
i licenca ostaju uz neizmijenjene podatke; bibliografski zapis jasno
razlikuje opisnu oznaku izvatka od naslova izvornoga istraživačkog rada.

Prva inačica temelji se na snimci
`e240baee664772257895ccd388672d65e25c3911`. Njezine izvorne datoteke i PDF
nisu promijenjeni. [Manifest](edition.json) čuva njihove SHA-256 sažetke,
uključujući datoteke podataka. Izvori u ovom direktoriju primjenjuju se
preko te snimke u zasebnom radnom direktoriju; nisu novi neovisni projekt.
Izvorne tehničke putanje i identifikatori ostaju radi ponovljivosti.
Za tekst se bilježi i sažetak s LF završecima redaka kako Gitova pretvorba
završetaka na drugom sustavu ne bi izgledala kao izmjena sadržaja.

## Ponovna izgradnja i provjera

Iz korijena repozitorija, uz dostupan navedeni Git commit i instalirane
ovisnosti knjige:

```powershell
python scripts/check-edition-v2.py
python scripts/render-edition-v2.py
```

Izgradnja poziva odobreni PDF omotač u izoliranom direktoriju ispod `tmp/`.
Tek nakon njegova uspjeha kopira novi PDF u `pdf/Statistika-v2.pdf`.
Prvi PDF provjerava se prije i poslije izgradnje. Skripta ne mijenja
izvorne podatke, konfiguraciju prve inačice ni objavljenu mrežnu knjigu.

Provjera uspoređuje izvršivi kod, ugrađene R izraze, citatne ključeve,
brojčani sadržaj tablica, prikazane formule i granice Quarto blokova.
Urednička provjera uključuje čitanje izmijenjenih odlomaka, stilski linter
te neovisne provjere glasa i slijeda izlaganja. Rezultat provjera i sažetak
izgrađenog PDF-a nalaze se u [zapisu provjere](validation.json).

Ovo je autorski zatražena stilska inačica. Ne mijenja status sveobuhvatne
recenzije, poglavlja ni njezine upravljačke registre.
