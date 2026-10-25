#!/usr/bin/env python3
"""Izvedi sažete javne provjere 19 okvira iz kanonskih zapisa rješenja."""
from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import re
from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT/'pdf/Provjere-nadite-gresku.pdf')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('routes', ROOT/'scripts/build-solution-routes.py')
    routes = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(routes)
    tokens = (ROOT/'design-tokens.yml').read_text(encoding='utf-8')
    for role, key in [('BodyFace', 'base'), ('TitleFace', 'display'), ('CodeFace', 'monospace')]:
        family = re.search(r'\n  '+key+r':\s*\n\s*family: "([^\n]+?)"', tokens).group(1)
        family = family.split(',')[0].strip(" '")
        font = ROOT/'fonts/print'/(family.replace(' ', '')+'-Regular.ttf')
        pdfmetrics.registerFont(TTFont(role, str(font)))
    body = ParagraphStyle('body', fontName='BodyFace', fontSize=10.5, leading=15,
                          spaceAfter=9, alignment=TA_LEFT)
    title = ParagraphStyle('title', fontName='TitleFace', fontSize=21, leading=25,
                           spaceAfter=14)
    label = ParagraphStyle('label', fontName='CodeFace', fontSize=8, leading=11,
                           spaceAfter=11)
    note = ParagraphStyle('note', parent=body, fontSize=8.5, leading=12, spaceAfter=18)
    story = []
    digest = hashlib.sha256()
    for number in range(19):
        unit = f'{number:02d}'
        path = ROOT/f'assessment/solution-records/unit-{unit}/sol-{unit}-callout-greska-01.json'
        raw = path.read_bytes(); digest.update(raw)
        record = json.loads(raw)
        if number:
            story.append(PageBreak())
        chapter_title = routes.source_title(ROOT, record['source_anchor']['path'])
        story.append(Paragraph('NAĐITE GREŠKU · PROVJERA RJEŠENJA', label))
        heading = 'Predgovor · digitalno izdanje' if number == 0 else f'{number}. {chapter_title}'
        story.append(Paragraph(html.escape(heading), title))
        if number == 0:
            story.append(Paragraph('Ove provjere čitajte nakon vlastitog pokušaja. '
                'Izvedene su iz istih zapisa kao javna stranica rješenja; nastavničke rubrike nisu uključene.', note))
        answer = record['answer_components']
        parts = [('planted.why_wrong', answer['planted_error']['why_wrong'])]
        parts += [('diagnostic.expected_evidence', paragraph) for paragraph in
                  answer['revealing_diagnostic']['expected_evidence'].split('\n\n')]
        # Use only the public explanation and repair. Protected criteria never enter this route.
        for field, value in parts:
            text = routes.reader_text(value, record['record_id'], field)
            text = html.escape(text)
            text = re.sub(r'`([^`]+)`', r'<font name="CodeFace">\1</font>', text)
            story.append(Paragraph(text, body))
        story.append(Spacer(1, 4*mm))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(args.output), pagesize=(176*mm, 250*mm),
                           leftMargin=22*mm, rightMargin=22*mm,
                           topMargin=19*mm, bottomMargin=19*mm,
                           title='Nađite grešku — provjere rješenja',
                           author='Statistika 101: Intuitivni uvod u analizu podataka',
                           subject='Javne provjere iz kanonskih zapisa rješenja',
                           keywords='records-sha256='+digest.hexdigest())
    def footer(canvas, document):
        canvas.saveState()
        canvas.setFont('CodeFace', 8)
        canvas.drawCentredString(88*mm, 10*mm, str(document.page))
        canvas.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'ERROR_EXERCISE_CHECKS_PDF_OK records=19 output={args.output}')


if __name__ == '__main__':
    main()
