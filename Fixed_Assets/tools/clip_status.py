"""Clip status — which kit rows have a kept clip, which must be regenerated, what is left to spend.

  python3 Fixed_Assets/tools/clip_status.py Episodes/<Guest>/P<n>_kit.md

Kept   = Shots/<ID>.mp4 exists (the ledger CLIPS.md says why it was kept).
Regen  = the ledger's not-used table says "REGEN <ID>".
To do  = everything else in the kit. Also flags a file in Shots/ that no kit row names, and a
         kept clip that the ledger does not list (so nothing is kept by accident).
"""
import os, re, sys
kit = sys.argv[1]; g = os.path.dirname(os.path.abspath(kit))
t = open(kit).read()
rows = re.findall(r'^\*\*(P\d_\d{3}[a-z]?)\*\* · ([A-Z_-]+)[^\n]*?\*\*(\d+) cr\*\*', t, re.M)
shots = os.path.join(g, 'Shots') if os.path.isdir(os.path.join(g, 'Shots')) else os.path.join(g, 'shots')
files = {f[:-4] for f in os.listdir(shots) if f.endswith('.mp4')}
led = open(os.path.join(g, 'CLIPS.md')).read() if os.path.exists(os.path.join(g, 'CLIPS.md')) else ''
regen = set(re.findall(r'REGEN (P\d_\d{3}[a-z]?)', led))
listed = set(re.findall(r'^\| (P\d_\d{3}[a-z]?) \|', led, re.M))
ids = {r[0] for r in rows}; part = rows[0][0][:2] if rows else 'P?'
kept = [r for r in rows if r[0] in files and r[0] not in regen]
rg = [r for r in rows if r[0] in regen]
todo = [r for r in rows if r[0] not in files and r[0] not in regen]
cr = lambda rs: sum(int(r[2]) for r in rs)
print(f'kept   {len(kept):3d} clips  {cr(kept):6,} cr   {" ".join(r[0] for r in kept)}')
print(f'regen  {len(rg):3d} clips  {cr(rg):6,} cr   {" ".join(r[0] for r in rg)}')
print(f'to do  {len(todo):3d} clips  {cr(todo):6,} cr')
print(f'left to spend: {cr(rg) + cr(todo):,} cr of {cr(rows):,}')
bad = [f for f in sorted(files) if f.startswith(part) and f not in ids]
bad += [f'{f} kept but not in CLIPS.md' for f in sorted(files) if f in ids and f not in listed]
for b in bad: print('WARN  ' + (b if ' ' in b else f'{b}.mp4 in Shots/ matches no kit row'))
