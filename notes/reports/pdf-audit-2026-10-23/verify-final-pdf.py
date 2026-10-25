"""Record text-level and staged-source checks for the delivered PDF candidate."""
from pathlib import Path
import hashlib
import json
import re
import fitz

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[2]
STAGE = ROOT / 'tmp/audit-2026-10-23/render'
PDF = STAGE / 'pdf/Statistika.pdf'
doc = fitz.open(PDF)
pages = [page.get_text() for page in doc]
text = '\n'.join(pages)
flat = re.sub(r'\s+', ' ', text.replace('\u00a0', ' '))
required = {
    'part_I': 'Prije prvoga računa razjašnjavamo',
    'part_II': 'Podatke sada sažimamo sredinama',
    'part_III': 'Opis uzorka nije još tvrdnja o populaciji',
    'part_IV': 'Procjeni i intervalu pridružujemo usporedbu',
    'part_V': 'Ista pitanja o procjeni, nesigurnosti i dosegu',
    'finale': 'Povezujemo pitanje, podatke, model i izvještaj',
    'named_examples': 'Primjeri koji se vraćaju',
    'glossary_full_comma_term': 'razdvajanje na skup za učenje, provjeru i ispitivanje',
    'identifier_description': 'jedinstvena oznaka generirane osobe',
    'notation': 'Oznake u formulama',
    'chapter7_print_answer': 'Poglavlje 7 — Računski zadatak',
    'chapter8_margin': '±2,94',
    'chapter9_interval': '4,525',
}
checks = {key: value in flat for key,value in required.items()}
manifest = json.loads((REPORT / 'render-source-manifest.json').read_text(encoding='utf-8'))
drift = []
for relative, expected in manifest.items():
    for label, base in [('root',ROOT),('staged',STAGE)]:
        path = base / relative
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            drift.append(f'{label}: {relative}')
result = {
    'pdf': str(ROOT / 'pdf/Statistika.pdf'),
    'sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
    'bytes': PDF.stat().st_size,
    'pages': len(doc),
    'unresolved_citation_keys': sorted(set(re.findall(r'(?<!\w)@[A-Za-z][\w:-]+',text))),
    'unresolved_references': text.count('??'),
    'replacement_characters': text.count('\ufffd'),
    'inverted_question_marks': text.count('¿'),
    'continuation_captions': text.count('(nastavak)'),
    'required_print_features': checks,
    'staged_source_count': len(manifest),
    'staged_source_drift': drift,
    'visual_review': 'See visual-review.md for actual inspected pages and limits.',
}
(REPORT / 'pdf-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
assert not result['unresolved_citation_keys']
assert result['unresolved_references'] == 0
assert result['replacement_characters'] == 0
assert result['inverted_question_marks'] == 0
assert all(checks.values()), 'Required text absent; check line-wrap extraction before changing manuscript.'
assert not drift
print('FINAL_PDF_TEXT_AND_SOURCE_CHECK_OK')
