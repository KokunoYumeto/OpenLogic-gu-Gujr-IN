[CmdletBinding()]
param([ValidateRange(1, 180000)][int]$AcquireTimeoutMs = 1000, [string]$SourceTree, [switch]$Cumulative)

$ErrorActionPreference = 'Stop'
if (-not $IsWindows) { throw 'This build requires Windows for the shared TeX slot and capped process job.' }
if ($SourceTree) {
    $olp = (Resolve-Path -LiteralPath $SourceTree).Path
    $book = Join-Path $olp 'locale/gu/courses/sets-logic-computation'
    $stage = $olp
    $inputTree = @{olp=$olp; source_units=176; localized_ids=$null}
} else {
    $source = & python (Join-Path $PSScriptRoot 'prepare.py')
    if ($LASTEXITCODE -ne 0) { throw 'Source staging failed.' }
    $inputTree = $source | ConvertFrom-Json
    $book = $inputTree.book
    $stage = $inputTree.stage
}
$driver = if ($Cumulative) { 'slc-screen-gu.tex' } else { 'slc-screen.tex' }
if ($Cumulative) {
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'slc-screen-gu.tex') -Destination $book
}
$pdf = Join-Path $book 'slc-screen.pdf'
$outName = if ($Cumulative) { 'slc-screen-gu-cumulative.pdf' } else { 'slc-screen-gu.pdf' }
$out = Join-Path $PSScriptRoot $outName
$receiptFile = Join-Path $stage 'build.json'
$receipt = [ordered]@{
    status = 'not_started'
    locale_input_units = $inputTree.source_units
    localized_identifiers = $inputTree.localized_ids
    commands = @()
    mutex_acquired = $false
    mutex_released = $false
}

function Invoke-SlcTool([string]$Name, [string[]]$Arguments) {
    $exe = (Get-Command $Name -CommandType Application).Source
    $sequence = $receipt.commands.Count + 1
    $log = Join-Path $stage ('{0:D2}-{1}.txt' -f $sequence, $Name)
    $code = $null
    if ($IsWindows) {
        $job = [GuTeXJob]::CreateJobObject([IntPtr]::Zero, $null)
        if ($job -eq [IntPtr]::Zero) { throw 'Could not create a Windows process job.' }
        $proc = $null
        try {
            [GuTeXJob]::Limit($job)
            $proc = [GuTeXJob]::Launch($exe, ($Arguments -join ' '), $book, $job, $log)
            $clock = [Diagnostics.Stopwatch]::StartNew()
            while (-not $proc.HasExited -or [GuTeXJob]::Active($job) -gt 0) {
                if ($clock.Elapsed.TotalSeconds -gt 240) { throw "$Name exceeded four minutes." }
                Start-Sleep -Milliseconds 100
            }
            $proc.WaitForExit()
            $code = $proc.ExitCode
        } finally {
            if ([GuTeXJob]::Active($job) -gt 0) {
                $null = [GuTeXJob]::TerminateJobObject($job, 125)
                while ([GuTeXJob]::Active($job) -gt 0) { Start-Sleep -Milliseconds 100 }
            }
            $null = [GuTeXJob]::CloseHandle($job)
            if ($proc) { $proc.Dispose() }
        }
    }
    $receipt.commands += @{tool = $Name; log = (Split-Path -Leaf $log); exit_code = $code; job_memory_limit_bytes = 5000000000}
    if ($code -ne 0 -or $null -eq $code) { throw "$Name failed. See $log." }
}

$mutex = $null
$previousBst = $env:BSTINPUTS
$previousEpoch = $env:SOURCE_DATE_EPOCH
$previousForceDate = $env:FORCE_SOURCE_DATE
try {
    if ($IsWindows) {
        Add-Type -Path (Join-Path $PSScriptRoot 'WindowsTeXJob.cs')
        $mutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
        try { $receipt.mutex_acquired = $mutex.WaitOne($AcquireTimeoutMs) }
        catch [Threading.AbandonedMutexException] { $receipt.mutex_acquired = $true }
        if (-not $receipt.mutex_acquired) {
            $receipt.status = 'slot_occupied'
            throw 'The TeX slot is occupied. No compiler was started.'
        }
    }

    $env:BSTINPUTS = (Join-Path $inputTree.olp 'bib') + [IO.Path]::PathSeparator
    $env:SOURCE_DATE_EPOCH = '1786722663'
    $env:FORCE_SOURCE_DATE = '1'
    $platformOptions = if (Get-Command miktex -ErrorAction SilentlyContinue) { @('--disable-installer') } else { @() }
    $texArgs = @($platformOptions) + @('-no-shell-escape','-interaction=nonstopmode',
        '-halt-on-error','-file-line-error','-recorder','-jobname=slc-screen',$driver)
    $bibArgs = @($platformOptions) + @('slc-screen')
    $indexArgs = @('-s','slc-screen.ist','-t','slc-screen.glg','-o','slc-screen.gls','slc-screen.glo')
    Invoke-SlcTool lualatex $texArgs
    $firstLog = Get-Content -LiteralPath (Join-Path $book 'slc-screen.log') -Raw
    if (($firstLog -replace '\s+', ' ') -match 'requested but not marked gu') {
        throw "A localized import was skipped. See $book/slc-screen.log."
    }
    Invoke-SlcTool bibtex $bibArgs
    Invoke-SlcTool makeindex $indexArgs
    Invoke-SlcTool lualatex $texArgs
    Invoke-SlcTool bibtex $bibArgs
    Invoke-SlcTool makeindex $indexArgs

    $checks = @(
        'There were undefined (?:references|citations)',
        '(?:Reference|Citation) [^\r\n]{0,200} undefined',
        'Label\(s\) may have changed',
        'Rerun to get (?:cross-references|outlines) right',
        'multiply defined',
        'Token [^\r\n]{0,200} undefined',
        'requested but not marked gu',
        'Missing character:'
    )
    $warnings = @()
    for ($pass = 3; $pass -le 7; $pass++) {
        Invoke-SlcTool lualatex $texArgs
        $texLog = Get-Content -LiteralPath (Join-Path $book 'slc-screen.log') -Raw
        $warnings = @($checks | Where-Object { $texLog -match $_ })
        if ($warnings.Count -eq 0) { break }
    }
    $receipt.remaining_log_checks = $warnings
    if ($warnings.Count -gt 0) { throw "Unsettled build. See $book/slc-screen.log." }
    if (-not (Test-Path -LiteralPath $pdf -PathType Leaf)) { throw 'The screen PDF is absent.' }
    $inventory = & python (Join-Path $PSScriptRoot 'check-build.py') $book ([string]$Cumulative.IsPresent)
    if ($LASTEXITCODE -ne 0) { throw 'Textbook content inventory did not pass.' }
    $receipt.inventory = $inventory | ConvertFrom-Json
    Copy-Item -LiteralPath $pdf -Destination $out
    $receipt.pdf_sha256 = (Get-FileHash -LiteralPath $out -Algorithm SHA256).Hash.ToLowerInvariant()
    $receipt.status = 'complete'
} catch {
    if ($receipt.status -ne 'slot_occupied') { $receipt.status = 'failed' }
    $receipt.error = $_.Exception.Message
    throw
} finally {
    $env:BSTINPUTS = $previousBst
    $env:SOURCE_DATE_EPOCH = $previousEpoch
    $env:FORCE_SOURCE_DATE = $previousForceDate
    if ($mutex) {
        if ($receipt.mutex_acquired) {
            $mutex.ReleaseMutex()
            $receipt.mutex_released = $true
        }
        $mutex.Dispose()
    }
    $receipt | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $receiptFile -Encoding utf8
}
Write-Output $out
