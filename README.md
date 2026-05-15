# srt-shifter

Script para deslocar timestamps em arquivos SRT a partir de um índice específico.

## Requisitos
- Python 3.x
- Git
- FFmpeg (opcional, para testar queima de legendas)
- PowerShell (Windows) para o script de lote

## Arquivos
- `shift_from_index.py` : desloca timestamps a partir de um índice (ex.: a partir da 2ª legenda).
- `shift_srt.py` : desloca todo o arquivo SRT.
- `scripts/batch_process.ps1` : PowerShell para processar todos os `.srt` na pasta com backup automático.
- `examples/` : pasta sugerida para exemplos de entrada e saída.

## Uso básico

### Ajustar a partir de um índice
```powershell
python shift_from_index.py entrada.srt saida.srt -26.06 2
