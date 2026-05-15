#!/usr/bin/env python3
import sys
import re
from datetime import timedelta

def parse_time(s):
    h, m, rest = s.split(':')
    sec, ms = rest.split(',')
    return timedelta(hours=int(h), minutes=int(m), seconds=int(sec), milliseconds=int(ms))

def format_time(td):
    total_ms = int(td.total_seconds() * 1000)
    if total_ms < 0:
        total_ms = 0
    ms = total_ms % 1000
    s = (total_ms // 1000) % 60
    m = (total_ms // 60000) % 60
    h = total_ms // 3600000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

if len(sys.argv) < 5:
    print("Uso: python shift_from_index.py entrada.srt saida.srt deslocamento_em_segundos start_index")
    print("Exemplo: python shift_from_index.py legenda.srt legenda_corrigida.srt -95 2")
    sys.exit(1)

infile, outfile, shift_str, start_index_str = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
shift = float(shift_str)
start_index = int(start_index_str)
delta = timedelta(seconds=shift)

with open(infile, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

blocks = re.split(r'\n\s*\n', content.strip(), flags=re.MULTILINE)
out_blocks = []
time_re = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})')

for i, block in enumerate(blocks, start=1):
    if i >= start_index:
        def repl(m):
            t1 = parse_time(m.group(1)) + delta
            t2 = parse_time(m.group(2)) + delta
            return f"{format_time(t1)} --> {format_time(t2)}"
        new_block = time_re.sub(repl, block)
        out_blocks.append(new_block)
    else:
        out_blocks.append(block)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write("\n\n".join(out_blocks) + "\n")

print(f"Arquivo salvo: {outfile}")
