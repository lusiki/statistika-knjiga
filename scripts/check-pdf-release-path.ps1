# Deterministic positive and negative fixtures for the fail-closed PDF wrapper.
# The fixtures use a fake Quarto executable in isolated temporary repositories;
# they never render or publish the book and never modify canonical artifacts.
#
# NOTE: keep this file ASCII-only for Windows PowerShell 5.1 compatibility.

[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$root = Split-Path $PSScriptRoot -Parent
$wrapper = Join-Path $root "scripts\render-book-pdf.ps1"
$workflow = Join-Path $root ".github\workflows\publish.yml"
$engine = (Get-Process -Id $PID).Path
$isWindowsHost = $env:OS -eq "Windows_NT"
$tempBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
$fixtureRoot = Join-Path $tempBase ("statistika-pdf-fixtures-" + [guid]::NewGuid().ToString("N"))
$utf8 = New-Object System.Text.UTF8Encoding($false)

function Assert-True([bool]$Condition, [string]$Message) {
  if (-not $Condition) { throw $Message }
}

function Write-Text([string]$Path, [string]$Text) {
  $parent = Split-Path $Path -Parent
  if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
  [System.IO.File]::WriteAllText($Path, $Text, $utf8)
}

function New-FakeQuarto([string]$CaseRoot) {
  if ($isWindowsHost) {
    $fake = Join-Path $CaseRoot "fake-quarto.cmd"
    $body = @'
@echo off
if "%STATISTIKA_PDF_FIXTURE_MODE%"=="success" (
  if not exist pdf mkdir pdf
  > pdf\Statistika.pdf echo %%PDF-1.7
  >> pdf\Statistika.pdf echo fixture-positive
  exit /b 0
)
if "%STATISTIKA_PDF_FIXTURE_MODE%"=="build-failure" (
  if not exist pdf mkdir pdf
  > pdf\Statistika.pdf echo partial
  exit /b 23
)
if "%STATISTIKA_PDF_FIXTURE_MODE%"=="missing-artifact" exit /b 0
exit /b 24
'@
    Write-Text $fake $body
    return $fake
  }

  $fake = Join-Path $CaseRoot "fake-quarto.sh"
  $body = @'
#!/bin/sh
case "$STATISTIKA_PDF_FIXTURE_MODE" in
  success)
    mkdir -p pdf
    printf '%s\n' '%PDF-1.7' 'fixture-positive' > pdf/Statistika.pdf
    exit 0
    ;;
  build-failure)
    mkdir -p pdf
    printf '%s\n' 'partial' > pdf/Statistika.pdf
    exit 23
    ;;
  missing-artifact)
    exit 0
    ;;
esac
exit 24
'@
  Write-Text $fake $body
  & chmod +x $fake
  if ($LASTEXITCODE -ne 0) { throw "could not make fake Quarto executable" }
  return $fake
}

function New-Config([bool]$Valid) {
  if (-not $Valid) {
    return "project:`n  type: book`n"
  }
  $validConfig = @'
project:
  type: book
book:
  references: references.qmd
  appendices:
    - dodaci/a-praktikum.qmd
    - dodaci/b-jamovi.qmd
    - dodaci/c-katalog-podataka.qmd
    - dodaci/d-koji-test.qmd
    - dodaci/e-rjecnik.qmd
    - dodaci/f-ai-protokol.qmd
'@
  return $validConfig + "`n"
}

function Invoke-Fixture(
  [string]$Name,
  [bool]$ValidConfig,
  [string]$Mode,
  [bool]$ExpectSuccess
) {
  $caseRoot = Join-Path $fixtureRoot $Name
  $caseScripts = Join-Path $caseRoot "scripts"
  New-Item -ItemType Directory -Force -Path $caseScripts | Out-Null
  Copy-Item -LiteralPath $wrapper -Destination (Join-Path $caseScripts "render-book-pdf.ps1")
  Write-Text (Join-Path $caseRoot "_quarto.yml") (New-Config $ValidConfig)
  Write-Text (Join-Path $caseRoot "pdf\Statistika.pdf") "STALE_SOURCE"
  Write-Text (Join-Path $caseRoot "docs\pdf\Statistika.pdf") "STALE_SERVED"
  $configHashBefore = (Get-FileHash -LiteralPath (Join-Path $caseRoot "_quarto.yml") -Algorithm SHA256).Hash
  $fake = New-FakeQuarto $caseRoot

  $oldMode = $env:STATISTIKA_PDF_FIXTURE_MODE
  $oldErrorAction = $ErrorActionPreference
  $env:STATISTIKA_PDF_FIXTURE_MODE = $Mode
  $ErrorActionPreference = "Continue"
  try {
    $childArgs = @("-NoProfile")
    if ($isWindowsHost) { $childArgs += @("-ExecutionPolicy", "Bypass") }
    $childArgs += @(
      "-File",
      (Join-Path $caseScripts "render-book-pdf.ps1"),
      "-QuartoPath",
      $fake
    )
    $output = @(& $engine @childArgs 2>&1)
    $exitCode = $LASTEXITCODE
  }
  finally {
    $env:STATISTIKA_PDF_FIXTURE_MODE = $oldMode
    $ErrorActionPreference = $oldErrorAction
  }

  $sourcePdf = Join-Path $caseRoot "pdf\Statistika.pdf"
  $servedPdf = Join-Path $caseRoot "docs\pdf\Statistika.pdf"
  $configHashAfter = (Get-FileHash -LiteralPath (Join-Path $caseRoot "_quarto.yml") -Algorithm SHA256).Hash
  Assert-True ($configHashBefore -eq $configHashAfter) "$Name changed _quarto.yml"

  if ($ExpectSuccess) {
    Assert-True ($exitCode -eq 0) "$Name unexpectedly failed: $($output -join ' | ')"
    Assert-True (Test-Path -LiteralPath $sourcePdf -PathType Leaf) "$Name produced no source PDF"
    Assert-True (Test-Path -LiteralPath $servedPdf -PathType Leaf) "$Name produced no served PDF"
    $sourceHash = (Get-FileHash -LiteralPath $sourcePdf -Algorithm SHA256).Hash
    $servedHash = (Get-FileHash -LiteralPath $servedPdf -Algorithm SHA256).Hash
    Assert-True ($sourceHash -eq $servedHash) "$Name copied a mismatched PDF"
    Assert-True (([System.IO.File]::ReadAllText($sourcePdf)) -notmatch 'STALE') "$Name retained stale PDF content"
    Assert-True (($output -join "`n") -match 'PDF_BUILD_OK') "$Name produced no success receipt"
  }
  else {
    Assert-True ($exitCode -ne 0) "$Name unexpectedly succeeded"
    Assert-True (-not (Test-Path -LiteralPath $sourcePdf)) "$Name left a stale or partial source PDF"
    Assert-True (-not (Test-Path -LiteralPath $servedPdf)) "$Name left a stale or partial served PDF"
  }
  $expectedLabel = if ($ExpectSuccess) { "SUCCESS" } else { "FAILURE" }
  Write-Host "EXPECTED_$expectedLabel case=$Name exit=$exitCode"
}

if (-not (Test-Path -LiteralPath $wrapper -PathType Leaf)) {
  throw "missing PDF wrapper: $wrapper"
}
if (-not (Test-Path -LiteralPath $workflow -PathType Leaf)) {
  throw "missing publish workflow: $workflow"
}

$workflowText = [System.IO.File]::ReadAllText($workflow)
$pdfStep = [regex]::Match(
  $workflowText,
  '(?ms)^      - name: Render fresh PDF through approved wrapper\s*$.*?(?=^      - name:|\z)'
)
Assert-True $pdfStep.Success "publish workflow has no approved PDF wrapper step"
Assert-True ($pdfStep.Value -match '(?m)^        run: pwsh -NoProfile -File scripts/render-book-pdf\.ps1 -RequireCleanCommit\s*$') "PDF step does not invoke the exact approved wrapper command"
Assert-True ($pdfStep.Value -notmatch 'continue-on-error') "PDF wrapper step is nonblocking"
Assert-True ($workflowText -notmatch 'quarto render --profile pdf') "publish workflow contains a bare PDF profile command"
Assert-True ($workflowText -notmatch 'Copy freshly-built PDF|Warn if PDF render failed') "publish workflow retains the old copy or warning branch"
Assert-True ($workflowText.IndexOf('Render fresh PDF through approved wrapper') -lt $workflowText.IndexOf('Render HTML book')) "PDF clean-source gate must run before generated HTML changes"

New-Item -ItemType Directory -Force -Path $fixtureRoot | Out-Null
try {
  Invoke-Fixture "positive-replacement" $true "success" $true
  Invoke-Fixture "wrapper-preflight-failure" $false "success" $false
  Invoke-Fixture "build-command-failure" $true "build-failure" $false
  Invoke-Fixture "stale-missing-artifact" $true "missing-artifact" $false
}
finally {
  $resolvedFixture = [System.IO.Path]::GetFullPath($fixtureRoot)
  if ($resolvedFixture.StartsWith($tempBase, [System.StringComparison]::OrdinalIgnoreCase) -and
      (Split-Path $resolvedFixture -Leaf).StartsWith("statistika-pdf-fixtures-")) {
    Remove-Item -LiteralPath $resolvedFixture -Recurse -Force -ErrorAction SilentlyContinue
  }
  else {
    throw "refusing to remove unsafe fixture path: $resolvedFixture"
  }
}

Write-Host "PDF_RELEASE_FIXTURES_OK cases=4 workflow=wrapper-only-blocking"
