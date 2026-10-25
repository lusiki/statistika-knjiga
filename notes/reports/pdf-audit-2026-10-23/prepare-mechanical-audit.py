"""Rebase the supplied audit's page map; preserve its substantive checks."""
from pathlib import Path
import fitz,re,json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3]
REPORT=Path(__file__).resolve().parent
PDF=ROOT/'tmp/audit-2026-10-23/render/pdf/Statistika.pdf'
original=Path(r'C:\Users\lsikic\Dropbox\temp\stat\mechanical_checks.R')
source=original.read_text(encoding='utf-8-sig')
(REPORT/'mechanical_checks.original.R').write_text(source,encoding='utf-8')
doc=fitz.open(PDF);toc=doc.get_toc()
titles=[re.search(r'^title:\s*"(.*?)"',p.read_text(encoding='utf-8'),re.M)[1]
        for p in sorted((ROOT/'chapters').glob('[0-9][0-9]-*.qmd'))]
by_title={t:p for level,t,p in toc}
offset=by_title[titles[0]]-1
keys=['00_predgovor','01_zasto_statistika','02_mjerenje','03_kako_brojke_zavode',
      '04_sazimanje','05_vizualizacija','06_povezanost','07_vjerojatnost','08_uzorkovanje',
      '09_procjena','10_logika_testiranja','11_velicina_ucinka','12_kriza_obnova',
      '13_kategoricki','14_dvije_grupe','15_vise_grupa','16_regresija','17_algoritmi',
      '18_prvo_istrazivanje','19_provjere','20_literatura']
starts=[by_title[t] for t in titles]+[by_title['Putokaz, pojmovi i oznake'],by_title['Literatura']]
boundaries=sorted({p for level,t,p in toc if level==1} | set(starts) | {len(doc)+1})
ranges={key:[start-offset,min(p for p in boundaries if p>start)-1-offset]
        for key,start in zip(keys,starts)}
# The checks chapter includes the newly added glossary/navigation apparatus.
ranges['19_provjere'][1]=by_title['Literatura']-1-offset
new_ranges='ranges <- list(\n'+',\n'.join(f'  "{k}" = c({a}, {b})' for k,(a,b) in ranges.items())+')'
source=re.sub(r'offset <- 4[^\n]*',f'offset <- {offset}  # updated from current PDF navigation',source,count=1)
source=re.sub(r'ranges <- list\(.*?\)\s*\nfor \(nm',new_ranges+'\nfor (nm',source,count=1,flags=re.S)
source=source.replace('Sys.setlocale("LC_ALL", "C.UTF-8")','Sys.setlocale("LC_ALL", "English_United States.utf8")')
raw=subprocess.run([r'C:\Program Files\Git\mingw64\bin\pdftotext.exe',
    '-layout','-enc','UTF-8',str(PDF),'-'],capture_output=True,check=True).stdout
# This installed Poppler emits CESU-8 surrogate pairs for supplementary math
# characters. Decode the pairs losslessly; do not discard or replace glyphs.
extracted=raw.decode('utf-8','surrogatepass')
extracted=re.sub('[\ud800-\udbff][\udc00-\udfff]',
    lambda m:m[0].encode('utf-16-le','surrogatepass').decode('utf-16-le'),extracted)
# Layout ordering also separates a few surrogate pairs with intervening
# superscript/diacritic characters. Preserve those code units as explicit
# escapes; their formulas are checked in rendered page images separately.
isolated=[{'page':extracted[:m.start()].count('\f')+1,'code_unit':hex(ord(m[0]))}
          for m in re.finditer('[\ud800-\udfff]',extracted)]
extracted=re.sub('[\ud800-\udfff]',lambda m:'\\u%04x'%ord(m[0]),extracted)
(REPORT/'poppler-decoding-notes.json').write_text(json.dumps(isolated,indent=2)+'\n')
text_path=REPORT/'mechanical-extracted.txt'
text_path.write_text(extracted,encoding='utf-8')
source=source.replace('txt <- system2("pdftotext", c("-layout", "-enc", "UTF-8", shQuote(pdf), "-"), stdout = TRUE)',
    'txt <- readLines("'+text_path.as_posix()+'", encoding = "UTF-8", warn = FALSE)')
source=source.replace('"-o", "/dev/null"','"-o", "NUL"')
source=source.replace('i - 4,','i - offset,')
(REPORT/'mechanical_checks_repaginated.R').write_text(source,encoding='utf-8')
(REPORT/'page-map.json').write_text(json.dumps({'pdf':str(PDF),'pages':len(doc),
  'offset':offset,'ranges':ranges,'sha256':hashlib.sha256(PDF.read_bytes()).hexdigest()},
  ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('MECHANICAL_AUDIT_MAP_OK',len(doc),'pages; offset',offset)
