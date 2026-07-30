# Reproducible build for the book Word document (word/Statistika.docx).
#
# This is the DOCX twin of scripts/render-book-pdf.ps1. The Word file is a local
# manuscript artifact: it is NOT served from the website (nothing is copied into
# docs/) and word/ is gitignored except the canonical .docx.
#
# This script makes temporary, always-restored edits to the source tree, renders
# the book to one Word file, then restores everything (try/finally, even on
# error or interruption). After it runs the tree is byte-identical.
#
#   1) FIGURE TWINS. Every widget is a twin pair: an OJS interactive chart gated
#      `.content-visible when-format="html"` and a static R "print" chart gated
#      `.content-visible when-format="pdf"`. For DOCX neither gate matches, so
#      both twins are stripped and the Word file would have almost no figures.
#      Quarto resolves when-format BEFORE any user filter and does not honour
#      multi-format gate values, so the only fix is to make the gate literally
#      say "docx": this script rewrites `when-format="pdf"` -> `when-format="docx"`
#      in the chapters and appendices for the render.
#
#   2) PRE-RENDER HOOK. The AI export hook is disabled while gates are swapped,
#      so transient DOCX source never rewrites tracked website exports.
#
# The canonical config already declares references.qmd separately and includes
# only appendices A-F. This script validates that structure but does not rewrite
# the appendix block.
#
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as the ANSI
# codepage, so non-ASCII in the source corrupts string terminators and breaks
# parsing. (Chapter content is read/written as UTF-8 below, so Croatian
# diacritics in the .qmd files are preserved.)
#
# Usage:  powershell -File scripts/render-book-docx.ps1
# Output: word/Statistika.docx

$ErrorActionPreference = "Stop"

$root      = Split-Path $PSScriptRoot -Parent
$cfg       = Join-Path $root "_quarto.yml"
$bak       = Join-Path $root "_quarto.yml.docxbuild.bak"
$srcDirs   = @((Join-Path $root "chapters"), (Join-Path $root "dodaci"))
$utf8      = New-Object System.Text.UTF8Encoding($false)
$gateFrom  = 'when-format="pdf"'
$gateTo    = 'when-format="docx"'

if (-not (Test-Path $cfg)) { throw "_quarto.yml not found at $cfg" }

# Restore any file from a sibling .docxbuild.bak, then delete the .bak. Used both
# as a pre-flight (recover from a crashed prior run) and in the finally block.
function Restore-DocxBaks {
  $suffix = ".docxbuild.bak"
  $all = @(Get-ChildItem -Path $root -Filter "*$suffix" -File -ErrorAction SilentlyContinue)
  foreach ($d in $srcDirs) {
    if (Test-Path $d) {
      $all += @(Get-ChildItem -Path $d -Filter "*$suffix" -File -ErrorAction SilentlyContinue)
    }
  }
  $all | ForEach-Object {
    $orig = $_.FullName.Substring(0, $_.FullName.Length - $suffix.Length)
    Copy-Item $_.FullName $orig -Force
    Remove-Item $_.FullName -Force -ErrorAction SilentlyContinue
  }
}

# Pre-flight: if a previous run crashed mid-build, recover the original sources
# BEFORE we snapshot anything (otherwise we would back up already-patched files).
Restore-DocxBaks

# Validate the canonical print structure before making temporary source edits.
$configText = [System.IO.File]::ReadAllText($cfg, $utf8)
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

$quarto = (Get-Command quarto -ErrorAction SilentlyContinue).Source
if (-not $quarto) { $quarto = "C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe" }
if (-not (Test-Path $quarto)) { throw "Quarto not found (not on PATH, not at $quarto)" }

Copy-Item $cfg $bak -Force

try {
  # --- (1) Drop the pre-render hook -------------------------------------------
  # The hook (R/build-ai-exports.R) regenerates the website AI exports from the
  # chapters, but here the chapters are temporarily gate-swapped, so letting it
  # run would dirty the tracked docs/ai/*, docs/llms*.txt and data/ai-exports.json
  # with content derived from the transient build state.
  $lines = Get-Content $cfg -Encoding UTF8
  $out = New-Object System.Collections.Generic.List[string]
  $i = 0; $foundPreRender = $false
  while ($i -lt $lines.Count) {
    if ($lines[$i] -match '^  pre-render:\s*$') {
      $foundPreRender = $true
      $i++
      while ($i -lt $lines.Count) {
        $l = $lines[$i]
        if ($l -match '^    ' -or $l -match '^  #' -or $l -match '^\s*$') { $i++; continue }
        break
      }
      continue
    }
    $out.Add($lines[$i]); $i++
  }

  if (-not $foundPreRender) {
    throw "project.pre-render block not found in _quarto.yml; aborting (config untouched)"
  }
  $patchedText = ($out -join "`r`n") + "`r`n"
  if ($patchedText -match '(?m)^  pre-render:\s*$') {
    throw "temporary _quarto.yml still contains project.pre-render"
  }
  if ($patchedText -notmatch '(?m)^  references:\s+references\.qmd\s*$') {
    throw "temporary config lost book.references; aborting (will restore)"
  }
  $patchedAppendices = [regex]::Match(
    $patchedText,
    '(?m)^  appendices:\s*\r?\n(?<body>(?:    - [^\r\n]+\r?\n)+)'
  )
  if (-not $patchedAppendices.Success) {
    throw "temporary config lost book.appendices; aborting (will restore)"
  }
  $patchedAppendixList = @(
    [regex]::Matches($patchedAppendices.Groups['body'].Value, '(?m)^    - ([^\r\n]+)\s*$') |
      ForEach-Object { $_.Groups[1].Value.Trim() }
  )
  if (($patchedAppendixList.Count -ne $expectedAppendices.Count) -or
      (($patchedAppendixList -join "`n") -ne ($expectedAppendices -join "`n"))) {
    throw "temporary config changed book.appendices; aborting (will restore)"
  }

  [System.IO.File]::WriteAllText($cfg, $patchedText, $utf8)

  # --- (2) Swap the print-twin gate when-format="pdf" -> "docx" ----------------
  $swapped = 0
  foreach ($d in $srcDirs) {
    if (-not (Test-Path $d)) { continue }
    Get-ChildItem -Path $d -Filter *.qmd -File | ForEach-Object {
      $text = [System.IO.File]::ReadAllText($_.FullName, $utf8)
      if ($text.Contains($gateFrom)) {
        Copy-Item $_.FullName ($_.FullName + ".docxbuild.bak") -Force
        [System.IO.File]::WriteAllText($_.FullName, $text.Replace($gateFrom, $gateTo), $utf8)
        $swapped++
      }
    }
  }
  Write-Host "Swapped print-twin gate to docx in $swapped source files."

  Write-Host "Rendering book DOCX (print figures shown)..."
  & $quarto render --to docx --profile docx
  if ($LASTEXITCODE -ne 0) { throw "quarto render failed (exit $LASTEXITCODE)" }

  $docx = Join-Path $root "word\Statistika.docx"
  if (-not (Test-Path $docx)) { throw "expected DOCX not produced: $docx" }

  Write-Host "Book DOCX rebuilt -> word/Statistika.docx"
}
finally {
  if (Test-Path $bak) {
    Copy-Item $bak $cfg -Force
    Remove-Item $bak -Force -ErrorAction SilentlyContinue
  }
  Restore-DocxBaks
  Write-Host "Source tree restored."
}
