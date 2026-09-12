param()
$ErrorActionPreference = 'Stop'
$distributionRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$manifestPath = Join-Path $distributionRoot '.agents/plugins/marketplace.json'
$marketplace = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
$marketplaceName = $marketplace.name
$pluginName = 'collart-data-assistant'
if (-not (Get-Command codex -ErrorAction SilentlyContinue)) {
    throw 'Codex CLI was not found. Install or update Codex, then run this script again.'
}
if ($marketplaceName -notmatch '^[a-z0-9][a-z0-9._-]*$') {
    throw 'Invalid marketplace name.'
}

# The implicit personal marketplace can be absent from marketplace list.
$implicitPath = Join-Path $HOME '.agents/plugins/marketplace.json'
if ((Test-Path -LiteralPath $implicitPath) -and ([IO.Path]::GetFullPath($implicitPath) -ne $manifestPath)) {
    $implicit = Get-Content -LiteralPath $implicitPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($implicit.name -eq $marketplaceName) {
        throw "Another implicit marketplace is named '$marketplaceName'. Resolve the naming conflict before installing; no existing source was changed."
    }
}
$listOutput = & codex plugin marketplace list --json
if ($LASTEXITCODE -ne 0) { throw 'Unable to inspect configured marketplaces.' }
$configured = ($listOutput | Out-String | ConvertFrom-Json).marketplaces
foreach ($entry in $configured) {
    if ($entry.name -eq $marketplaceName -and [IO.Path]::GetFullPath($entry.root) -ne $distributionRoot) {
        throw "Marketplace '$marketplaceName' already points elsewhere. Resolve the naming conflict before installing; no existing source was changed."
    }
}
& codex plugin marketplace add $distributionRoot
if ($LASTEXITCODE -ne 0) { throw 'Marketplace registration failed. Plugin installation was not attempted.' }
& codex plugin add "$pluginName@$marketplaceName"
if ($LASTEXITCODE -ne 0) { throw 'Plugin installation failed. The local marketplace is registered; inspect the Codex error and retry.' }
Write-Host 'Installed Collart Data Assistant. Open a new Codex task to use the two skills.'
