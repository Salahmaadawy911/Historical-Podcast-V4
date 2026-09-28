#!/usr/bin/env python3
"""cli_wave.py — prepare the next CLI batch ("wave") from the round sheet (2026-09-27, L52).

Usage:  python3 Fixed_Assets/tools/cli_wave.py Episodes/<Guest> [--part 1] [--max 10] [--ids P1_060,...]
A clip is READY when it is not yet in Shots/ and either starts from a seed frame, or is chained from a clip
that IS in Shots/ (kept). For each ready chained clip the source's last frame is extracted to
Shots/start_frames/<ID>_start.png — ffmpeg -sseof -0.08, no scale, no lift (what Kling's last-frame button gives).
Prints the one command Salah runs on his Mac. B-roll is skipped (website). Takes land in Shots/_tests/;
Salah looks at them, and Claude moves the kept ones into Shots/ — which makes the next wave ready.
"""
import re, sys, os, subprocess
a = sys.argv[1:]; G = a[0]
part = a[a.index('--part') + 1] if '--part' in a else '1'
MAX = int(a[a.index('--max') + 1]) if '--max' in a else 10
only = a[a.index('--ids') + 1].split(',') if '--ids' in a else None
P = f'P{part.lstrip("Pp")}'
sheet = open(os.path.join(G, ('' if P == 'P1' else f'{P}_') + 'ROUND1_prompts.md'), encoding='utf-8').read()
shots = os.path.join(G, 'Shots'); have = {f[:-4] for f in os.listdir(shots) if f.endswith('.mp4')}
tests = os.path.join(shots, '_tests'); pending = {f[:-4] for f in os.listdir(tests) if f.endswith('.mp4')} if os.path.isdir(tests) else set()
os.makedirs(os.path.join(shots, 'start_frames'), exist_ok=True)
ready, waiting = [], []
for m in re.finditer(rf'^### ({P}_\d{{3}}[a-z]?) · (\S+)[^\n]*?· ([\d.]+)s · ([^\n]*)$', sheet, re.M):
    sid, kind, dur, head = m.groups()
    if 'still' in head or kind.startswith('B'): continue
    if sid in have or sid in pending or (only and sid not in only): continue
    src = re.search(r'last frame of `([^`]+)`', head)
    if src:
        s = src.group(1)
        if s not in have: waiting.append(f'{sid} (waits for {s})'); continue
        out = os.path.join(shots, 'start_frames', f'{sid}_start.png')
        if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(os.path.join(shots, s + '.mp4')):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.08', '-i', os.path.join(shots, s + '.mp4'), '-frames:v', '1', out], check=True)
    ready.append((sid, float(dur), head))
ready = ready[:MAX]
def rate(h): return 8 if ('720p' in h or 'audio OFF' in h) else 12 if 'Standard · audio ON' in h else 10
cr = sum(d * rate(h) for _, d, h in ready)
print(f'READY {len(ready)} clips, ~{int(cr)} cr: ' + ', '.join(s for s, _, _ in ready))
if waiting: print('WAITING (their source is not kept yet): ' + ', '.join(waiting))
if ready:
    print('\nRun on the Mac, from the project folder:\n')
    print(f'node Fixed_Assets/tools/kling_run.mjs {G} 1 --part {part.lstrip("Pp")} --ids ' + ','.join(s for s, _, _ in ready))
