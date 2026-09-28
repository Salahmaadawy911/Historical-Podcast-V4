#!/usr/bin/env python3
"""voice_folders.py — split a part's kept clips for the ElevenLabs voice pass (2026-09-27, Salah).

Usage:  python3 Fixed_Assets/tools/voice_folders.py Episodes/<Guest> [--part 1]
Reads P<n>_kit.md and copies every TALKING clip in Shots/ (interview, interjection, narration — including the
audio-only 720p ones) into
    Episodes/<Guest>/Voice/P<n>/1_host/     ← voice change with the host voice
    Episodes/<Guest>/Voice/P<n>/2_guest/    ← voice change with the guest's voice
Save each converted file into Voice/P<n>/done/ under the SAME name (P1_006.mp3 — ElevenLabs returns audio; the edit lays it under the clip's picture from Shots/). Reactions, b-roll and cards stay
in Shots/ only — they get no voice pass. Shots/ is never changed (it stays the ledger every tool reads).
Re-run any time: it copies ONLY clips that still need converting (no file in done/, or retaken since), so 1_host/ and
2_guest/ can be emptied after each voice pass — they are just the to-do inbox.
"""
import re, sys, os, shutil
a = sys.argv[1:]; G = a[0]; part = (a[a.index('--part') + 1] if '--part' in a else '1').lstrip('Pp')
kit = open(os.path.join(G, f'P{part}_kit.md'), encoding='utf-8').read()
shots = os.path.join(G, 'Shots'); base = os.path.join(G, 'Voice', f'P{part}')
dirs = {'HOST': os.path.join(base, '1_host'), 'GUEST': os.path.join(base, '2_guest')}
done = os.path.join(base, 'done')
for d in list(dirs.values()) + [done]: os.makedirs(d, exist_ok=True)
n = {'HOST': 0, 'GUEST': 0}; new = 0; todo = []
for m in re.finditer(rf'^\*\*(P{part}_\d{{3}}[a-z]?)\*\* · (INTERVIEW|INTERJECTION|NARRATION) · (HOST|GUEST)', kit, re.M):
    sid, typ, who = m.groups(); src = os.path.join(shots, sid + '.mp4')
    if not os.path.exists(src): continue
    dst = os.path.join(dirs[who], sid + '.mp4'); n[who] += 1
    conv = [os.path.join(done, sid + e) for e in ('.mp3', '.mp4', '.wav', '.m4a') if os.path.exists(os.path.join(done, sid + e))]
    if conv and os.path.getmtime(conv[0]) >= os.path.getmtime(src): continue      # converted, and not retaken since
    todo.append(sid)
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        shutil.copy2(src, dst); new += 1
print(f'Voice/P{part}: {n["HOST"]} host + {n["GUEST"]} guest talking clips ({new} copied now). Still to convert: {len(todo)}')
