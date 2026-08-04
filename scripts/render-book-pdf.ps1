# Reproducible, fail-closed build for the book PDF.
#
# This is the only supported PDF entry point. It removes both eligible PDF
# outputs before validation or rendering, invokes the PDF profile, validates a
# newly created PDF, and copies only that file into docs/pdf. Any wrapper,
# render, or artifact failure leaves neither PDF eligible for publication.
#
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as the ANSI
# codepage, so non-ASCII text in the source can corrupt parsing.
#
# Usage:  powershell -File scripts/render-book-pdf.ps1
# CI:     pwsh -NoProfile -File scripts/render-book-pdf.ps1 -RequireCleanCommit
# Output: pdf/Statistika.pdf  (+ verified copy in docs/pdf/Statistika.pdf)

[CmdletBinding()]
param(
  [string]$QuartoPath = "",
  [switch]$RequireCleanCommit
)

$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
$cfg = Join-Path $root "_quarto.yml"
$pdf = Join-Path $root "pdf\Statistika.pdf"
$servedPdf = Join-Path $root "docs\pdf\Statistika.pdf"
$sourceCommit = "working-tree"
$locationPushed = $false
$buildAccepted = $false

function Remove-PdfOutputs {
  foreach ($candidate in @($pdf, $servedPdf)) {
    if (Test-Path -LiteralPath $candidate -PathType Leaf) {
      Remove-Item -LiteralPath $candidate -Force
    }
  }
}

function Assert-PdfFile([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    throw "expected fresh PDF not produced: $Path"
  }

  $item = Get-Item -LiteralPath $Path
  if ($item.Length -lt 8) {
    throw "fresh PDF is unexpectedly small: $Path"
  }

  $stream = [System.IO.File]::OpenRead($Path)
  try {
    $header = New-Object byte[] 5
    if ($stream.Read($header, 0, 5) -ne 5) {
      throw "could not read PDF header: $Path"
    }
    if ([System.Text.Encoding]::ASCII.GetString($header) -ne "%PDF-") {
      throw "fresh artifact has no PDF signature: $Path"
    }
  }
  finally {
    $stream.Dispose()
  }
}

try {
  Push-Location $root
  $locationPushed = $true

  $git = Get-Command git -ErrorAction SilentlyContinue
  $gitMarker = Join-Path $root ".git"
  if ($git -and (Test-Path -LiteralPath $gitMarker)) {
    $sourceCommit = (& $git.Source -C $root rev-parse --verify HEAD 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($sourceCommit)) {
      throw "could not resolve the source commit"
    }
  }
  elseif ($RequireCleanCommit) {
    throw "git is required when -RequireCleanCommit is set"
  }

  if ($RequireCleanCommit) {
    $trackedChanges = @(& $git.Source -C $root status --porcelain --untracked-files=no)
    if ($LASTEXITCODE -ne 0) {
      throw "could not inspect the tracked source state"
    }
    if ($trackedChanges.Count -ne 0) {
      throw "-RequireCleanCommit requires zero tracked changes before the PDF build"
    }
  }

  # Stale committed artifacts become ineligible before any wrapper validation.
  Remove-PdfOutputs

  if (-not (Test-Path -LiteralPath $cfg -PathType Leaf)) {
    throw "_quarto.yml not found at $cfg"
  }

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

  if ($QuartoPath) {
    $resolvedQuarto = Resolve-Path -LiteralPath $QuartoPath -ErrorAction Stop
    $quarto = $resolvedQuarto.Path
  }
  else {
    $quartoCommand = Get-Command quarto -ErrorAction SilentlyContinue
    if ($quartoCommand) {
      $quarto = $quartoCommand.Source
    }
    else {
      $quarto = "C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe"
    }
  }
  if (-not (Test-Path -LiteralPath $quarto -PathType Leaf)) {
    throw "Quarto not found (not on PATH, not at $quarto)"
  }

  Write-Host "Rendering fresh book PDF through the approved wrapper..."
  & $quarto render --profile pdf
  if ($LASTEXITCODE -ne 0) {
    throw "quarto render failed (exit $LASTEXITCODE)"
  }

  Assert-PdfFile $pdf

  New-Item -ItemType Directory -Force -Path (Split-Path $servedPdf -Parent) | Out-Null
  Copy-Item -LiteralPath $pdf -Destination $servedPdf -Force
  Assert-PdfFile $servedPdf

  $sourceHash = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
  $servedHash = (Get-FileHash -LiteralPath $servedPdf -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($sourceHash -ne $servedHash) {
    throw "served PDF copy does not match the fresh source artifact"
  }

  $buildAccepted = $true
  $bytes = (Get-Item -LiteralPath $pdf).Length
  Write-Host "PDF_BUILD_OK source_commit=$sourceCommit sha256=$sourceHash bytes=$bytes"
  Write-Host "Book PDF rebuilt -> pdf/Statistika.pdf + docs/pdf/Statistika.pdf"
}
finally {
  if (-not $buildAccepted) {
    Remove-PdfOutputs
    Write-Host "PDF_BUILD_FAILED stale and partial PDF outputs removed"
  }
  if ($locationPushed) {
    Pop-Location
  }
}
