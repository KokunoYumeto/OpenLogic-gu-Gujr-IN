param(
 [int]$TimeoutMs = 1000,
 [ValidateSet('sets','foundations','functions','size','arithmetization')][string]$Edition = 'sets',
 [string]$StateDirectory = $env:INTERLANGUAGE_STATE_DIR
)
$ErrorActionPreference = 'Stop'
$GuRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$GuState = if ([string]::IsNullOrWhiteSpace($StateDirectory)) {
 Join-Path $GuRepo 'build'
} else {
 [System.IO.Path]::GetFullPath($StateDirectory)
}
[void](New-Item -ItemType Directory -Force -Path $GuState)
$GuJob = "gu-$Edition"
$GuReceiptName = switch ($Edition) { 'sets' { 'BUILD_RECEIPT.json' } 'foundations' { 'BUILD_RECEIPT_002.json' } 'functions' { 'BUILD_RECEIPT_003.json' } 'size' { 'BUILD_RECEIPT_004.json' } 'arithmetization' { 'BUILD_RECEIPT_005.json' } }
$GuLogPrefix = if ($Edition -eq 'sets') { 'pass' } else { "$Edition-pass" }
$GuMutex = [System.Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$GuAcquired = $false
$GuAbandoned = $false
$GuReceipt = [ordered]@{
 schema='openlogic-gu-guarded-tex/1'; started_utc=[DateTime]::UtcNow.ToString('o')
 mutex='Global\InterlanguageTeXSlotV1'; timeout_ms=$TimeoutMs; acquired=$false
 abandoned_recovery=$false; passes=@(); status='starting'
}
try {
 try { $GuAcquired = $GuMutex.WaitOne($TimeoutMs) }
 catch [System.Threading.AbandonedMutexException] { $GuAcquired = $true; $GuAbandoned = $true }
 $GuReceipt.acquired = $GuAcquired
 $GuReceipt.abandoned_recovery = $GuAbandoned
 if (-not $GuAcquired) {
  $GuReceipt.status='slot_occupied_no_tex_started'
 } else {
  $env:SOURCE_DATE_EPOCH='1788530400'
  $env:FORCE_SOURCE_DATE='1'
  $env:MIKTEX_ENABLE_INSTALLER='0'
  for ($GuPass=1; $GuPass -le 3; $GuPass++) {
   $GuOut=Join-Path $GuRepo "build\$GuLogPrefix-$GuPass.stdout.log"
   $GuErr=Join-Path $GuRepo "build\$GuLogPrefix-$GuPass.stderr.log"
   $GuStart=[DateTime]::UtcNow
   $GuInfo=[System.Diagnostics.ProcessStartInfo]::new()
   $GuInfo.FileName='lualatex.exe'
   $GuInfo.Arguments="--disable-installer --no-shell-escape --interaction=nonstopmode --halt-on-error --output-directory=build $GuJob.tex"
   $GuInfo.WorkingDirectory=$GuRepo
   $GuInfo.UseShellExecute=$false
   $GuInfo.CreateNoWindow=$true
   $GuInfo.RedirectStandardOutput=$true
   $GuInfo.RedirectStandardError=$true
   $GuProcess=[System.Diagnostics.Process]::new()
   $GuProcess.StartInfo=$GuInfo
   [void]$GuProcess.Start()
   $GuStdoutTask=$GuProcess.StandardOutput.ReadToEndAsync()
   $GuStderrTask=$GuProcess.StandardError.ReadToEndAsync()
   try {
    if (-not $GuProcess.WaitForExit(180000)) {
      $GuProcess.Kill($true)
      $GuProcess.WaitForExit()
      throw 'Own captured LuaLaTeX process exceeded 180-second limit.'
    }
    $GuProcess.Refresh()
    $GuExit=$GuProcess.ExitCode
    $GuStdout=$GuStdoutTask.GetAwaiter().GetResult().Replace($env:USERPROFILE,'{USERPROFILE}').Replace($env:USERPROFILE.Replace('\','/'),'{USERPROFILE}')
    $GuStderr=$GuStderrTask.GetAwaiter().GetResult().Replace($env:USERPROFILE,'{USERPROFILE}').Replace($env:USERPROFILE.Replace('\','/'),'{USERPROFILE}')
    $GuStdout | Set-Content -LiteralPath $GuOut -Encoding utf8
    $GuStderr | Set-Content -LiteralPath $GuErr -Encoding utf8
    $GuLogPath=Join-Path $GuRepo "build\$GuJob.log"
    if (Test-Path -LiteralPath $GuLogPath) {
     $GuSanitized=(Get-Content -LiteralPath $GuLogPath -Raw).Replace($env:USERPROFILE,'{USERPROFILE}').Replace($env:USERPROFILE.Replace('\','/'),'{USERPROFILE}')
     $GuSanitized | Set-Content -LiteralPath $GuLogPath -Encoding utf8
    }
    $GuReceipt.passes += [ordered]@{pass=$GuPass; process_id=$GuProcess.Id; exit_code=$GuExit; seconds=([DateTime]::UtcNow-$GuStart).TotalSeconds}
    if ($GuExit -ne 0) { throw "LuaLaTeX pass $GuPass failed, exit $GuExit. Inspect own captured logs." }
   } finally {
    if (-not $GuProcess.HasExited) { $GuProcess.Kill($true); $GuProcess.WaitForExit() }
    $GuProcess.Dispose()
   }
   $GuLog=Get-Content -LiteralPath (Join-Path $GuRepo "build\$GuJob.log") -Raw
   if ($GuLog -match 'Missing character:|^!|Emergency stop|Fatal error') { throw 'Deterministic TeX log defect; inspect own build log.' }
   $GuHash=(Get-FileHash -LiteralPath (Join-Path $GuRepo "build\$GuJob.pdf") -Algorithm SHA256).Hash.ToLower()
   $GuReceipt.passes[-1].pdf_sha256=$GuHash
  }
  $GuReceipt.replay_equal=($GuReceipt.passes[1].pdf_sha256 -eq $GuReceipt.passes[2].pdf_sha256)
  $GuReceipt.log_warnings=@([regex]::Matches($GuLog,'(?m)^.*(?:Warning:|Overfull|Underfull).*$') | ForEach-Object { $_.Value })
  $GuReceipt.status='built_pending_visual_and_semantic_qa'
 }
} catch {
 $GuReceipt.status='failed'
 $GuReceipt.error=$_.Exception.Message
} finally {
 $GuReceipt.ended_utc=[DateTime]::UtcNow.ToString('o')
 $GuReceipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $GuState $GuReceiptName) -Encoding utf8
 if ($GuAcquired) { $GuMutex.ReleaseMutex() }
 $GuMutex.Dispose()
}
$GuReceipt | ConvertTo-Json -Depth 8
