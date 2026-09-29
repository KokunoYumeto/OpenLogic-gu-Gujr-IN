param([int]$TimeoutMs=1000)
$ErrorActionPreference='Stop'
$GuRepo=Split-Path -Parent $PSScriptRoot
$GuState=Join-Path $GuRepo 'build'
$GuInput=Join-Path $GuRepo 'reader\full-reader.tex'
$GuOutput=Join-Path $GuRepo 'build\full-reader'
$GuJob='gu-full-reader-proof'
$GuReceiptPath=Join-Path $GuOutput 'FULL_READER_BUILD.json'
$GuMutex=[System.Threading.Mutex]::new($false,'Global\InterlanguageTeXSlotV1')
$GuAcquired=$false
$GuReceipt=[ordered]@{schema='openlogic-gu-full-reader-guarded-build/1';started_at_utc=[DateTime]::UtcNow.ToString('o');mutex='Global\InterlanguageTeXSlotV1';timeout_ms=$TimeoutMs;acquired=$false;steps=@();status='starting'}
function Invoke-GuCapturedBuild {
 param([string]$Executable,[string[]]$Arguments,[string]$Directory,[string]$Step,[int]$LimitMs)
 $GuInfo=[System.Diagnostics.ProcessStartInfo]::new()
 $GuInfo.FileName=$Executable
 foreach ($GuArg in $Arguments) {[void]$GuInfo.ArgumentList.Add($GuArg)}
 $GuInfo.WorkingDirectory=$Directory
 $GuInfo.UseShellExecute=$false
 $GuInfo.CreateNoWindow=$true
 $GuInfo.RedirectStandardOutput=$true
 $GuInfo.RedirectStandardError=$true
 $GuProcess=[System.Diagnostics.Process]::new()
 $GuProcess.StartInfo=$GuInfo
 [void]$GuProcess.Start()
 $GuPid=$GuProcess.Id
 $GuStdout=$GuProcess.StandardOutput.ReadToEndAsync()
 $GuStderr=$GuProcess.StandardError.ReadToEndAsync()
 try {
  if (-not $GuProcess.WaitForExit($LimitMs)) {$GuProcess.Kill($true);$GuProcess.WaitForExit();throw "Own $Step process exceeded bounded runtime."}
  $GuProcess.Refresh()
  $GuExit=$GuProcess.ExitCode
  $GuOutText=$GuStdout.GetAwaiter().GetResult()
  $GuErrText=$GuStderr.GetAwaiter().GetResult()
  $GuOutText | Set-Content -LiteralPath (Join-Path $GuOutput ($Step+'.stdout.log')) -Encoding utf8
  $GuErrText | Set-Content -LiteralPath (Join-Path $GuOutput ($Step+'.stderr.log')) -Encoding utf8
  $GuReceipt.steps += [ordered]@{step=$Step;process_id=$GuPid;exit_code=$GuExit}
  if ($GuExit -ne 0) {throw "$Step failed; inspect its saved stdout/stderr and TeX log."}
 } finally {
  if (-not $GuProcess.HasExited) {$GuProcess.Kill($true);$GuProcess.WaitForExit()}
  $GuProcess.Dispose()
 }
}
try {
 [void](New-Item -ItemType Directory -Force -Path $GuOutput)
 try {$GuAcquired=$GuMutex.WaitOne($TimeoutMs)} catch [System.Threading.AbandonedMutexException] {$GuAcquired=$true;$GuReceipt.abandoned_recovery=$true}
 $GuReceipt.acquired=$GuAcquired
 if (-not $GuAcquired) {$GuReceipt.status='slot_occupied_no_tex_started_substantive_edition_work_continues'} else {
  $GuFullOutput=[System.IO.Path]::GetFullPath($GuOutput)
  $GuFullWork=[System.IO.Path]::GetFullPath($GuState)
  if (-not $GuFullOutput.StartsWith($GuFullWork+[System.IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) {throw 'Output escaped own task state.'}
  [void](New-Item -ItemType Directory -Force -Path $GuOutput)
  $env:SOURCE_DATE_EPOCH='1788530400'
  $env:FORCE_SOURCE_DATE='1'
  $env:MIKTEX_ENABLE_INSTALLER='0'
  $env:BIBINPUTS=$GuRepo+';'
  $env:BSTINPUTS=$GuRepo+';'
  $GuTeXArgs=@('--disable-installer','--no-shell-escape','--interaction=nonstopmode','--halt-on-error',('--jobname='+$GuJob),('--output-directory='+$GuOutput),$GuInput)
  Invoke-GuCapturedBuild 'lualatex.exe' $GuTeXArgs $GuRepo 'lualatex-1' 600000
  Invoke-GuCapturedBuild 'lualatex.exe' $GuTeXArgs $GuRepo 'lualatex-2' 600000
  Invoke-GuCapturedBuild 'lualatex.exe' $GuTeXArgs $GuRepo 'lualatex-3' 600000
  $GuLogPath=Join-Path $GuOutput ($GuJob+'.log')
  $GuLog=Get-Content -LiteralPath $GuLogPath -Raw
  $GuReceipt.log=[ordered]@{path=$GuLogPath;sha256=(Get-FileHash -LiteralPath $GuLogPath -Algorithm SHA256).Hash.ToLowerInvariant()}
  $GuReceipt.missing_characters=@([regex]::Matches($GuLog,'(?m)^Missing character:.*$') | ForEach-Object {$_.Value})
  $GuReceipt.undefined_references=@([regex]::Matches($GuLog,"(?m)^(?:LaTeX Warning: Reference|Package natbib Warning: Citation|LaTeX Warning: Label|Package natbib Warning: There were).*(?:undefined|multiply defined).*$") | ForEach-Object {$_.Value})
  if ($GuReceipt.missing_characters.Count -gt 0 -or $GuLog -match 'Emergency stop|Fatal error') {throw 'Font or fatal log defect after full-reader build.'}
  if ($GuReceipt.undefined_references.Count -gt 0) {throw 'Unresolved reference or citation after full-reader build.'}
  $GuPdf=Join-Path $GuOutput ($GuJob+'.pdf')
  if (-not (Test-Path -LiteralPath $GuPdf -PathType Leaf)) {throw 'No full-reader PDF after passes.'}
  $GuReceipt.pdf=[ordered]@{path=$GuPdf;bytes=(Get-Item -LiteralPath $GuPdf).Length;sha256=(Get-FileHash -LiteralPath $GuPdf -Algorithm SHA256).Hash.ToLowerInvariant()}
  $GuReceipt.status='three_lualatex_passes_succeeded_visual_QA_pending'
 }
} catch {$GuReceipt.status='failed';$GuReceipt.error=$_.Exception.Message} finally {
 $GuReceipt.ended_at_utc=[DateTime]::UtcNow.ToString('o')
 $GuRunStamp=[DateTime]::Parse($GuReceipt.started_at_utc).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
 $GuCurrentLog=Join-Path $GuOutput ($GuJob+'.log')
 if ($GuAcquired -and (Test-Path -LiteralPath $GuCurrentLog -PathType Leaf)) {
  $GuText=Get-Content -LiteralPath $GuCurrentLog -Raw
  $GuReceipt.tex_errors=@([regex]::Matches($GuText,'(?m)^! .*$') | ForEach-Object {$_.Value})
  $GuSavedLog=Join-Path $GuOutput ($GuRunStamp+'.tex.log')
  Copy-Item -LiteralPath $GuCurrentLog -Destination $GuSavedLog
  $GuReceipt.saved_log=[ordered]@{path=$GuSavedLog;sha256=(Get-FileHash -LiteralPath $GuSavedLog -Algorithm SHA256).Hash.ToLowerInvariant()}
 }
 $GuJson=$GuReceipt | ConvertTo-Json -Depth 10
 $GuJson | Set-Content -LiteralPath $GuReceiptPath -Encoding utf8
 $GuArchive='FULL_READER_TEX_ATTEMPT_049_'+$GuRunStamp+'.json'
 $GuJson | Set-Content -LiteralPath (Join-Path $GuOutput $GuArchive) -Encoding utf8
 if ($GuAcquired) {$GuMutex.ReleaseMutex()}
 $GuMutex.Dispose()
}
$GuReceipt | ConvertTo-Json -Depth 10
if ($GuReceipt.status -eq 'failed') {exit 1}
