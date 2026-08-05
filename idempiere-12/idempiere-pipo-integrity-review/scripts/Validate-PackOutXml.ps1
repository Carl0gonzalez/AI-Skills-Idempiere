param(
    [Parameter(Mandatory = $true)]
    [string]$ZipPath
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

if (-not (Test-Path -LiteralPath $ZipPath -PathType Leaf)) {
    Write-Error "PackOut file not found: $ZipPath"
    exit 2
}

$zip = [IO.Compression.ZipFile]::OpenRead((Resolve-Path -LiteralPath $ZipPath))
try {
    $badPaths = @($zip.Entries | Where-Object { $_.FullName -match '\\' })
    if ($badPaths.Count -gt 0) {
        Write-Output 'BLOCKER: ZIP contains paths with backslashes.'
        $badPaths | ForEach-Object { Write-Output "  $($_.FullName)" }
        exit 2
    }

    $xmlEntry = $zip.Entries | Where-Object { $_.FullName -match '(^|/)dict/PackOut\.xml$' } | Select-Object -First 1
    if ($null -eq $xmlEntry) {
        Write-Output 'BLOCKER: dict/PackOut.xml is missing from the ZIP.'
        exit 2
    }

    $reader = New-Object IO.StreamReader($xmlEntry.Open())
    try {
        $document = New-Object System.Xml.XmlDocument
        $document.Load($reader)
    } finally {
        $reader.Dispose()
    }

    $blockers = 0
    $columns = @($document.SelectNodes("//*[*[local-name()='AD_Column_UU'] and *[local-name()='ColumnName']]"))
    $duplicates = $columns | Group-Object { "$(([string]$_.AD_Table_ID).'#text')|$(([string]$_.ColumnName).Trim().ToLowerInvariant())" } | Where-Object Count -gt 1
    foreach ($duplicate in $duplicates) {
        Write-Output "BLOCKER: duplicate column metadata for $($duplicate.Name) ($($duplicate.Count) entries)."
        $blockers++
    }

    foreach ($column in $columns) {
        $name = ([string]$column.ColumnName).Trim()
        if ([string]::IsNullOrEmpty($name) -or [string]::IsNullOrEmpty(([string]$column.AD_Column_UU).Trim())) {
            Write-Output "BLOCKER: column metadata is missing ColumnName or AD_Column_UU."
            $blockers++
        }
    }

    $validObscureTypes = @('904', '944', 'A04', 'A44')
    $fields = $document.SelectNodes("//*[*[local-name()='AD_Field_UU'] and *[local-name()='AD_Column_ID']]")
    foreach ($field in $fields) {
        $obscureType = ([string]$field.ObscureType).Trim()
        if (-not [string]::IsNullOrEmpty($obscureType) -and $validObscureTypes -notcontains $obscureType) {
            Write-Output "BLOCKER: AD_Field '$(([string]$field.Name).Trim())' has invalid ObscureType '$obscureType'."
            $blockers++
        }
    }

    if ($blockers -gt 0) {
        Write-Output "RESULT=BLOCKED blockers=$blockers"
        exit 2
    }
    Write-Output 'RESULT=READY blockers=0'
} finally {
    $zip.Dispose()
}
