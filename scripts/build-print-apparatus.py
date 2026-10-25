"""Build the print reading map, bilingual term index and notation from source."""
from pathlib import Path
import json
import re

def croatian_sort(text):
    alphabet = ['a', 'b', 'c', 'č', 'ć', 'd', 'dž', 'đ', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj', 'o', 'p', 'r', 's',
                'š', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ž']
    alphabet.insert(alphabet.index('r'), 'q')
    units = re.findall(r'dž|lj|nj|.', re.sub(r'[\s-]+', '', text.casefold()))
    return tuple(alphabet.index(c) if c in alphabet else 40 + ord(c) for c in units)

ROOT = Path(__file__).resolve().parents[1]
titles = {}
terms = {}
chapters = []
for path in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.qmd")):
    number = path.name[:2]
    if number == "00":
        continue
    source = path.read_text(encoding="utf-8")
    title = re.search(r'^title:\s*"(.*?)"', source, re.M)[1]
    titles[title] = number
    chapters.append((number, title))
    match = re.search(r"## Pojmovi.*?\n(.*?)(?=\n## )", source, re.S)
    if not match:
        raise ValueError(f"Missing terms: {path}")
    content = " ".join(match[1].split())
    cursor = 0
    for gloss in re.finditer(r"\(\*([^*]+)\*\)", content):
        term = content[cursor:gloss.start()].strip().lstrip(",").strip().strip("*")
        english = gloss[1]
        cursor = gloss.end()
        key = (term, english.strip())
        terms.setdefault(key, []).append(number)

lines = [
    "# Putokaz, pojmovi i oznake {.unnumbered}", "",
    "Broj poglavlja u putokazu odgovara oznaci na njegovoj početnoj stranici.",
    "U rječniku su nazivi iz završnih popisa pojmova. Uz svaki pojam navodimo",
    "poglavlje i stranicu završnog popisa, odakle se možemo vratiti njegovu objašnjenju u tekstu.", "",
    "## Putokaz kroz poglavlja {.unnumbered}", "",
    "| Poglavlje | Tema | Stranica |", "|---:|---|---:|",
]
for number, title in chapters:
    lines.append(f"| {int(number)} | {title} | \\pageref{{audit-ch{number}}} |")
lines += ["", "## Primjeri koji se vraćaju {.unnumbered}", "",
    "Oznake poglavlja i stranice vode na početak poglavlja u kojem je primjer razvijen.",
    "Tablica pomaže povezati njegove različite uporabe u knjizi.", "",
    "| Primjer | Gdje ga tražiti | Poglavlje i stranica |", "|---|---|---|",
    r"| Berkeley | zbirni i odjelni podaci; povratak uz kategoričke podatke | 1, str. \pageref{audit-ch01}; 13, str. \pageref{audit-ch13} |",
    r"| Anscombeov kvartet | isti brojčani sažeci i različiti oblici odnosa | 5, str. \pageref{audit-ch05} |",
    r"| DigiKat | sažimanje digitalnih tragova i izbor ljestvice prikaza | 4, str. \pageref{audit-ch04}; 5, str. \pageref{audit-ch05} |",
    r"| ParlaSent | oznake parlamentarnih rečenica i provjera klasifikatora | 17, str. \pageref{audit-ch17}; 18, str. \pageref{audit-ch18} |",
    r"| Registrirana replikacija (RRR) | usporedba laboratorija, procjena učinka i obnova istraživačke prakse | 12, str. \pageref{audit-ch12} |",
]
lines += ["", "## Hrvatsko-engleski rječnik {.unnumbered}", "",
          "| Hrvatski naziv | Engleski naziv | Poglavlje i stranica |", "|---|---|---|"]
for (term, english), numbers in sorted(terms.items(), key=lambda item: croatian_sort(item[0][0])):
    refs = "; ".join(f"{int(n)}, str. \\pageref{{audit-terms{n}}}" for n in dict.fromkeys(numbers))
    lines.append(f"| {term} | {english} | {refs} |")
lines += ["", "## Dva nastavna skupa podataka {.unnumbered}", "",
    "Skupovi su generirani odvojeno. Jedan redak u svakome predstavlja jednu",
    "zamišljenu osobu; isto ime varijable ne znači da oba skupa mjere isto",
    "obilježje ili obuhvaćaju iste osobe. Brojčani kodovi kategorija služe",
    "razmjeni datoteka i ne pretvaraju kategorije u brojčane mjere.", "",
    "Anketa o društvenim mrežama ima 300 zapisa u datoteci",
    "`data/anketa-mreze.csv`.", "",
    "| Varijabla | Značenje |", "|---|---|",
    "| `ispitanik` | jedinstvena oznaka generirane osobe |",
    "| `dob` | dob u godinama |",
    "| `dobna_skupina`, `dobna_skupina_sifra` | dobna kategorija i njezin brojčani kod |",
    "| `minute_dnevno` | dnevne minute na društvenim mrežama |",
    "| `povjerenje` | generirana ocjena povjerenja od 1 do 10 |", "",
    r"\Needspace{12\baselineskip}", "",
    "Populacija medijskih navika ima 50 000 zapisa u datoteci",
    "`data/populacija-medija.csv`. Iz nje iznova izvlačimo uzorke",
    "jer znamo vrijednosti za cijelu nastavnu populaciju.", "",
    "| Varijabla | Značenje |", "|---|---|",
    "| `osoba` | jedinstveni broj generirane osobe |",
    "| `dob`, `spol` | dob u godinama i generirana kategorija spola |",
    "| `obrazovanje`, `obrazovanje_sifra` | kategorija obrazovanja i njezin kod |",
    "| `izvor_vijesti`, `izvor_vijesti_sifra` | glavni izvor vijesti i njegov kod |",
    "| `povjerenje_medijima` | generirana ocjena povjerenja od 1 do 10 |",
    "| `minute_medija` | dnevne minute praćenja medija |",
    "| `spremnost_platiti` | generirani iznos; nula označuje nespremnost na plaćanje |", "",
    "U popratnim agregatima jedan redak predstavlja dobnu skupinu ili izvor",
    "vijesti. Brojnosti, zbrojevi i prosjeci omogućuju provjeru računa, ali",
    "ne zamjenjuju pojedinačne zapise pri provjeri njihova nastanka.", "",
    "Rezultati tih dvaju skupova ne potkrepljuju tvrdnje o stvarnim stanovnicima",
    "Hrvatske. Opisi stvarnih izvora i njihovih ograničenja nalaze se uz primjere",
    "i u mrežnom katalogu podataka.", "",
    "\\clearpage", "", "## Oznake u formulama {.unnumbered}", "",
    "Ista oznaka čita se uz cilj i jedinicu navedene uz konkretni račun.", "",
    "| Oznaka | Značenje |", "|---|---|",
    r"| $n$, $N$ | broj jedinica u uzorku i u konačnoj populaciji |",
    r"| $\bar{x}$, $\mu$ | uzoračka i populacijska sredina |",
    r"| $s$, $s^2$ | uzoračka standardna devijacija i varijanca |",
    r"| $\sigma$, $\sigma^2$ | populacijska standardna devijacija i varijanca |",
    r"| $\hat p$ | procijenjeni udio; razlikuje se od p-vrijednosti testa |",
    r"| $SE$ | standardna pogreška procjenitelja |",
    r"| $z^*$, $t^*$ | kritične vrijednosti normalne i t-raspodjele |",
    r"| $\alpha$ | unaprijed odabrana razina testa |",
    r"| $d$, $s_{\mathrm{zdr}}$ | standardizirana razlika i združena standardna devijacija |",
    r"| $O_{ij}$, $E_{ij}$ | opažena i očekivana frekvencija ćelije |",
    r"| $\chi^2$, $V$ | hi-kvadrat statistika i Cramérova mjera povezanosti |",
    r"| $df$ | stupnjevi slobode referentne raspodjele |",
    r"| $F$, $\eta^2$ | omjer srednjih kvadrata i udio objašnjene varijabilnosti |",
    r"| $r$, $R^2$ | Pearsonova korelacija i koeficijent determinacije |",
    r"| $\beta_0$, $\beta_j$ | odsječak i koeficijent prediktora u populacijskom modelu |",
    r"| $\varepsilon_i$ | odstupanje ishoda od populacijske regresijske sredine |",
    r"| AOR | prilagođeni omjer izgleda u logističkom modelu |", "",
]
(ROOT / "assessment/print-navigation.json").write_text(json.dumps(titles, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(ROOT / "assessment/print-glossary.md").write_text("\n".join(lines), encoding="utf-8")
print(f"PRINT_APPARATUS_OK chapters={len(chapters)} bilingual_terms={len(terms)}")
