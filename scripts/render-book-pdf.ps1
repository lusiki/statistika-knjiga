# Reproducible build for the book PDF (pdf/Statistika.pdf).
#
# WHY THIS SCRIPT EXISTS: it is the single supported local entry point for the
# PDF build. The canonical config keeps references.qmd separate from the
# appendix list, and book.appendices contains only appendices A-F, so no
# temporary config rewrite is needed.
#
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as the ANSI
# codepage, so non-ASCII text in the source can corrupt parsing.
#
# Usage:  powershell -File scripts/render-book-pdf.ps1
# Output: pdf/Statistika.pdf  (+ copy in docs/pdf/Statistika.pdf)

$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
$cfg  = Join-Path $root "_quarto.yml"

if (-not (Test-Path $cfg)) { throw "_quarto.yml not found at $cfg" }

# Fail early if the canonical print structure drifts. This is validation only;
# the wrapper never modifies _quarto.yml.
$configText = [System.IO.File]::ReadAllText($cfg)
if ($configText -notmatch '(?m)^  references:\s+references\.qmd\s*$') {
  throw "_quarto.yml must declare book.references: references.qmd"
}

$expectedAppendices = @(
  'dodaci/a-praktikum.qmd',
  'dodaci/b-jamovi.qmd',
  'dodaci/c-katalog-podataka.qmd',
  'dodaci/d-koji-test.qmd',
  'dodaci/e-rjecnik.qmd',
  'dodaci/f-ai-protokol.qmd'
)
$appendixMatch = [regex]::Match(
  $configText,
  '(?m)^  appendices:\s*\r?\n(?<body>(?:    - [^\r\n]+\r?\n)+)'
)
if (-not $appendixMatch.Success) {
  throw "_quarto.yml must contain a non-empty book.appendices block"
}
$actualAppendices = @(
  [regex]::Matches($appendixMatch.Groups['body'].Value, '(?m)^    - ([^\r\n]+)\s*$') |
    ForEach-Object { $_.Groups[1].Value.Trim() }
)
if (($actualAppendices.Count -ne $expectedAppendices.Count) -or
    (($actualAppendices -join "`n") -ne ($expectedAppendices -join "`n"))) {
  throw "_quarto.yml book.appendices must contain exactly appendices A-F in canonical order"
}

# Locate quarto (PATH first, then the RStudio-bundled copy).
$quarto = (Get-Command quarto -ErrorAction SilentlyContinue).Source
if (-not $quarto) { $quarto = "C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe" }
if (-not (Test-Path $quarto)) { throw "Quarto not found (not on PATH, not at $quarto)" }

Write-Host "Rendering book PDF..."
& $quarto render --profile pdf
if ($LASTEXITCODE -ne 0) { throw "quarto render failed (exit $LASTEXITCODE)" }

$pdf = Join-Path $root "pdf\Statistika.pdf"
if (-not (Test-Path $pdf)) { throw "expected PDF not produced: $pdf" }

New-Item -ItemType Directory -Force -Path (Join-Path $root "docs\pdf") | Out-Null
Copy-Item $pdf (Join-Path $root "docs\pdf\Statistika.pdf") -Force
Write-Host "Book PDF rebuilt -> pdf/Statistika.pdf + docs/pdf/Statistika.pdf"
