#!/usr/bin/env python3
"""Chain start frames — one batch, every chained row in a kit.

Usage:  python3 Fixed_Assets/tools/chain_frames.py Episodes/<Guest> [part]     part: 1 (default), 2, … or P2
Reads  Episodes/<Guest>/P<n>_kit.md for every row whose start frame says "chain from P1_xxx".
Clips are expected in      Episodes/<Guest>/shots/<ID>.mp4
Start frames are written to Episodes/<Guest>/shots/start_frames/<TARGET>_start.png
  - named after the shot that USES the frame, so the upload is unambiguous
  - extracted with the approved command only:  ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png
    (no scale filter), then PRE-LIFTED by LIFT% luma: Kling's first frame lands ~3.3-4% darker than
    the image it was given (measured on every clip, 2026-09-21), so the start frame is handed over
    brighter by that much and the join lands level. The join is measured against A's RAW last frame.
  - an existing start frame is never overwritten (delete it by hand to re-extract)
A row may chain from a CUT POINT instead of the end (a CUT-IN's silent stop, Mode 4 §8b):
  "chain from P1_xxx at cut"    -> reported as needing a cut time
  "chain from P1_xxx at 6.42s"  -> that exact frame is extracted
When the chained clip itself is back, the join is measured: luma and chroma, last frame vs first.

Also a CONTINUITY GATE (runs first, needs no clips): two talking rows by the same speaker, back to back
with nothing cut in between, must be chained — or the first must be placed "audio only, under ..."
(its picture discarded). A fresh seed frame there is a pose snap on the same camera. Exits 1 if found.
"""
import re, sys, os, subprocess, tempfile
import numpy as np
from PIL import Image

LIFT = 0.0   # percent. 0 since 2026-09-21: joins are levelled in the EDIT from the grade this script writes
             # (JOIN_GRADES.md), which fixes whatever the shift turns out to be instead of predicting it.
def _lift(p):
    a = np.asarray(Image.open(p).convert('RGB')).astype(float) * (1 + LIFT / 100)
    Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8)).save(p)
def last_frame(src, out, lift=True):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.08', '-i', src, '-frames:v', '1', out], check=True)
    if lift: _lift(out)
def frame_at(src, t, out):
    # -ss AFTER -i: frame-accurate decode to the exact time, no range conversion, no scaling
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-ss', str(t), '-frames:v', '1', out], check=True)
def first_frame(src, out):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-frames:v', '1', out], check=True)
def means(p):
    return np.asarray(Image.open(p).convert('RGB')).astype(float).reshape(-1, 3).mean(0)
def stats(p):
    a = np.asarray(Image.open(p).convert('YCbCr')).astype(float)
    return a[..., 0].mean(), np.hypot(a[..., 1] - 128, a[..., 2] - 128).mean()

def main(ep, part='1'):
    part = part if str(part).upper().startswith('P') else f'P{part}'
    part = part.upper()
    kit = open(os.path.join(ep, f'{part}_kit.md'), encoding='utf-8').read()
    shots = os.path.join(ep, 'shots'); outd = os.path.join(shots, 'start_frames')
    os.makedirs(outd, exist_ok=True)
    pairs = []
    for row in re.split(r'\n(?=\*\*' + part + r'_\d{3}[a-z]?\*\* · )', kit):
        m = re.match(r'\*\*(' + part + r'_\d{3}[a-z]?)\*\*', row)
        c = re.search(r'`start_frame`[^\n]*?chain from `?(' + part + r'_\d{3}[a-z]?)`?(?: at (cut|[\d.]+s))?', row)
        if m and c: pairs.append((c.group(1), m.group(1), c.group(2)))
    # continuity gate
    TALK = ('INTERVIEW', 'INTERJECTION', 'NARRATION')
    seq = []
    for row in re.split(r'\n(?=\*\*' + part + r'_\d{3}[a-z]?\*\* · )', kit):
        m = re.match(r'\*\*(' + part + r'_\d{3}[a-z]?)\*\* · (\w+)(?: · (HOST|GUEST))?', row)
        if m: seq.append((m.group(1), m.group(2), m.group(3), 'chain from' in (re.search(r'`start_frame`[^\n]*', row) or [''])[0], 'audio only, under' in row))
    # an OFFMIC row ("audio only, under ...") never appears in picture: it is transparent for continuity,
    # so the rows either side of it are adjacent on screen (e.g. P1_066 -> [P1_067 off-mic] -> P1_068).
    pic = [r for r in seq if not (r[1] in TALK and r[4])]
    bad = [(a[0], b[0]) for a, b in zip(pic, pic[1:])
           if a[1] in TALK and b[1] in TALK and a[2] == b[2] and not b[3]]
    for a, b in bad:
        print(f'  CONTINUITY  {b} follows {a} (same speaker, nothing between) on a fresh seed frame — chain it, or place {a} "audio only, under ..."')
    if bad:
        print('STOP — fix continuity before generating.'); sys.exit(1)
    print(f'{len(pairs)} chained rows in {part}_kit.md\n')
    todo = []; grades = []
    for src, tgt, at in pairs:
        s_clip = os.path.join(shots, src + '.mp4'); t_clip = os.path.join(shots, tgt + '.mp4')
        frame = os.path.join(outd, tgt + '_start.png')
        if not os.path.exists(s_clip):
            print(f'  {tgt}  waiting — generate {src} first'); todo.append(src); continue
        made = ''
        if at == 'cut':
            print(f'  {tgt}  needs a cut time — time the cut word in {src}, then write "chain from {src} at <seconds>s" in its row'); continue
        if not os.path.exists(frame):
            if at: frame_at(s_clip, float(at[:-1]), frame); _lift(frame); made = f'  NEW (at {at}, the cut point, +{LIFT}%)'
            else:  last_frame(s_clip, frame); made = f'  NEW (+{LIFT}%)'
        line = f'  {tgt}  start frame ready: shots/start_frames/{tgt}_start.png{made}'
        if os.path.exists(t_clip):
            tmp = os.path.join(tempfile.gettempdir(), tgt + '_first.png'); first_frame(t_clip, tmp)   # outside the project: the bridge cannot delete there
            raw = os.path.join(tempfile.gettempdir(), tgt + '_srcraw.png')
            if at and at != 'cut': frame_at(s_clip, float(at[:-1]), raw)
            else: last_frame(s_clip, raw, lift=False)
            (y0, c0), (y1, c1) = stats(raw), stats(tmp)
            g = means(raw) / np.maximum(means(tmp), 1e-6)
            os.remove(tmp); os.remove(raw)
            grades.append((tgt, src, g))
            dy, dc = (y1 / y0 - 1) * 100, (c1 / c0 - 1) * 100
            flag = '' if abs(dy) < 2 and abs(dc) < 3 else '   ⚠️ CHECK THE CUT'
            line += f'\n        join measured: luma {dy:+.1f}%  chroma {dc:+.1f}%{flag}'
        print(line)
    if todo: print(f'\nStill to generate before the chained shots: {", ".join(todo)}')
    if grades:
        out = ['# Join grades — written by chain_frames.py. Apply in the edit; do not hand-tune.', '',
               'Each chained clip is levelled to the last frame of the clip it continues: one per-channel gain, '
               'applied to the WHOLE chained clip. Only same-camera joins need it; a cut to the other camera hides a few percent.', '',
               '| clip | continues | shift at the join | ffmpeg filter for the chained clip |', '|---|---|---|---|']
        for tgt, src, g in grades:
            off = max(abs(x - 1) for x in g) * 100
            f = 'none needed' if off < 1.0 else f'`colorchannelmixer=rr={g[0]:.3f}:gg={g[1]:.3f}:bb={g[2]:.3f}`'
            out.append(f'| `{tgt}` | `{src}` | {off:.1f}% | {f} |')
        open(os.path.join(shots, '_measure', 'JOIN_GRADES.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
        print('\nJoin grades written: shots/_measure/JOIN_GRADES.md')

if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    main(*sys.argv[1:])
