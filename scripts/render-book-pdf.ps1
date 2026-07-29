# Reproducible build for the book PDF (pdf/Statistika.pdf).
#
# WHY THIS SCRIPT EXISTS: the PDF should carry only the bibliography and the six
# appendices, while the website keeps the full appendix set (pojmovnik,
# interakcije, podaci, resursi, uci-s-ai, predavanja, silabus, raspored). Quarto
# profiles merge book.appendices arrays ADDITIVELY, so _quarto-pdf.yml cannot
# shrink the list: a short list there just gets appended to the full list in
# _quarto.yml.
#
# So this script temporarily rewrites the appendices block in _quarto.yml to the
# print set, runs the PDF render, and then ALWAYS restores _quarto.yml
# (try/finally - even on error or interruption). The HTML build is never
# affected; _quarto.yml is byte-identical after this runs.
#
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as the ANSI
# codepage, so non-ASCII (em-dashes, Croatian diacritics) in the source corrupts
# string terminators and breaks parsing.
#
# Usage:  powershell -File scripts/render-book-pdf.ps1
# Output: pdf/Statistika.pdf  (+ copy in docs/pdf/Statistika.pdf)

$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
$cfg  = Join-Path $root "_quarto.yml"
$bak  = Join-Path $root "_quarto.yml.pdfbuild.bak"

# The appendix set that belongs in print. Edit here if an appendix is added.
$printAppendices = @(
  '    - references.qmd',
  '    - dodaci/a-praktikum.qmd',
  '    - dodaci/b-jamovi.qmd',
  '    - dodaci/c-katalog-podataka.qmd',
  '    - dodaci/d-koji-test.qmd',
  '    - dodaci/e-rjecnik.qmd',
  '    - dodaci/f-ai-protokol.qmd'
)

if (-not (Test-Path $cfg)) { throw "_quarto.yml not found at $cfg" }

# Locate quarto (PATH first, then the RStudio-bundled copy).
$quarto = (Get-Command quarto -ErrorAction SilentlyContinue).Source
if (-not $quarto) { $quarto = "C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe" }
if (-not (Test-Path $quarto)) { throw "Quarto not found (not on PATH, not at $quarto)" }

# Snapshot the real config so we can restore it no matter what.
Copy-Item $cfg $bak -Force

try {
  # Rewrite the `  appendices:` block (a book-level, two-space-indented key).
  # Done line-by-line on structure (not regex): copy lines until `  appendices:`,
  # emit the print block, then SKIP the old block body (its `    - ...` children,
  # `  #` comments, and interleaved blank lines) and resume at the next `  `-level
  # key (e.g. bibliography:). This can never spill into bibliography:/crossref:.
  $lines = Get-Content $cfg -Encoding UTF8
  $out = New-Object System.Collections.Generic.List[string]
  $i = 0; $found = $false
  while ($i -lt $lines.Count) {
    if ($lines[$i] -match '^  appendices:\s*$') {
      $found = $true
      $out.Add('  appendices:')
      foreach ($a in $printAppendices) { $out.Add($a) }
      $i++
      while ($i -lt $lines.Count) {
        $l = $lines[$i]
        if ($l -match '^    ' -or $l -match '^  #' -or $l -match '^\s*$') { $i++; continue }
        break
      }
      $out.Add('')
      continue
    }
    $out.Add($lines[$i]); $i++
  }

  if (-not $found) {
    throw "appendices block not found in _quarto.yml; aborting (config untouched)"
  }
  $patchedText = ($out -join "`r`n") + "`r`n"
  if ($patchedText -notmatch '(?m)^  appendices:\r?\n    - references\.qmd\r?\n') {
    throw "patched _quarto.yml does not look right; aborting (will restore)"
  }
  if (($patchedText -notmatch '(?m)^bibliography:') -or ($patchedText -notmatch '(?m)^crossref:')) {
    throw "patch removed bibliography or crossref; aborting (will restore)"
  }

  # Write the temporary config (UTF-8, no BOM, to match Quarto's reader).
  [System.IO.File]::WriteAllText($cfg, $patchedText, (New-Object System.Text.UTF8Encoding($false)))

  Write-Host "Rendering book PDF with the print appendix set..."
  & $quarto render --profile pdf
  if ($LASTEXITCODE -ne 0) { throw "quarto render failed (exit $LASTEXITCODE)" }

  $pdf = Join-Path $root "pdf\Statistika.pdf"
  if (-not (Test-Path $pdf)) { throw "expected PDF not produced: $pdf" }

  New-Item -ItemType Directory -Force -Path (Join-Path $root "docs\pdf") | Out-Null
  Copy-Item $pdf (Join-Path $root "docs\pdf\Statistika.pdf") -Force
  Write-Host "Book PDF rebuilt -> pdf/Statistika.pdf + docs/pdf/Statistika.pdf"
}
finally {
  # Always restore the canonical _quarto.yml.
  if (Test-Path $bak) {
    Copy-Item $bak $cfg -Force
    Remove-Item $bak -Force -ErrorAction SilentlyContinue
    Write-Host "_quarto.yml restored."
  }
}
