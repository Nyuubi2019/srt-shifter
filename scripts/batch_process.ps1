# Batch process para Windows PowerShell
# Faz backup automático dos arquivos originais antes de processar
# Editar $offset e $startIndex conforme necessário

$offset = -26.06
$startIndex = 2
$backupFolder = "backup_srt_$(Get-Date -Format 'yyyyMMdd_HHmmss')"

New-Item -ItemType Directory -Path $backupFolder | Out-Null

Get-ChildItem -Filter *.srt | ForEach-Object {
    $in = $_.FullName
    $base = [IO.Path]::GetFileNameWithoutExtension($in)
    $out = "$base`_corrigida.srt"
    $backup = Join-Path $backupFolder $_.Name

    Write-Host "Backup $in -> $backup"
    Copy-Item -Path $in -Destination $backup -Force

    Write-Host "Processando $in -> $out (offset $offset startIndex $startIndex)"
    python shift_from_index.py $in $out $offset $startIndex

    if (Test-Path $out) {
        Write-Host "OK: $out gerado."
    } else {
        Write-Host "Erro ao gerar $out"
    }
}
