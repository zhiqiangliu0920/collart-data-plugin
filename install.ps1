param()
$ErrorActionPreference = 'Stop'
$marketplaceName = 'personal'
$repositoryUrl = 'https://github.com/zhiqiangliu0920/collart-data-plugin.git'
if (-not (Get-Command codex -ErrorAction SilentlyContinue)) {
    throw 'Codex CLI was not found. Install or update Codex first.'
}
$raw = & codex plugin marketplace list --json
if ($LASTEXITCODE -ne 0) { throw 'Unable to inspect marketplaces.' }
$existing = @(($raw | Out-String | ConvertFrom-Json).marketplaces | Where-Object name -EQ $marketplaceName)
if ($existing.Count -gt 1) { throw 'Ambiguous personal marketplace; inspect its sources first.' }
if ($existing.Count -eq 1) {
    $source = $existing[0].marketplaceSource
    if ($source.sourceType -ne 'git' -or $source.source.TrimEnd('/') -notin @($repositoryUrl, $repositoryUrl.Replace('.git',''))) {
        throw 'The personal marketplace points elsewhere. No existing source was changed.'
    }
    & codex plugin marketplace upgrade $marketplaceName
} else {
    & codex plugin marketplace add $repositoryUrl --ref main
}
if ($LASTEXITCODE -ne 0) { throw 'Marketplace registration/refresh failed.' }
& codex plugin add "collart-data-assistant@$marketplaceName"
if ($LASTEXITCODE -ne 0) { throw 'Plugin installation failed; inspect the Codex error.' }
Write-Host 'Installed from GitHub. Open a new Codex task to use the updated plugin.'
