"""Camera check — did the camera hold still? Measures background drift in a clip, one line per clip.

  python3 Fixed_Assets/tools/cam_check.py Episodes/<Guest>/Shots/P1_058.mp4 [more clips…]

Phase-correlates two background patches (away from the person) against the first frame, sampled
through the clip. Host clips (P*_ rows with frame_host*) use the lamp and the slat wall; guest clips
the slat wall and the bookshelf. PASS = drift ≤ 3 px at every sample. Added 2026-09-25 (LESSONS L18):
the camera lock is prompt-only now (no web chip needed), so every take is measured, not eyeballed.
Side is guessed from the kit's start frame when the kit sits next to Shots/; pass `clip.mp4:H|G` to force it.
"""
import os, re, subprocess, sys
import numpy as np
BOX = {'H': [(620, 0, 300, 260), (1320, 40, 540, 440)], 'G': [(40, 40, 520, 440), (1530, 180, 360, 260)]}   # guest bookshelf box moved clear of her hair (P1_124 false alarm)
def frames(f, box):
    x, y, w, h = box
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', f'scale=1920:1080,crop={w}:{h}:{x}:{y},format=gray',
                          '-f', 'rawvideo', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(float)
def shift(a, b):
    A = np.fft.fft2(a - a.mean()); B = np.fft.fft2(b - b.mean()); R = A * np.conj(B); R /= np.abs(R) + 1e-9
    r = np.abs(np.fft.ifft2(R)); i = np.unravel_index(r.argmax(), r.shape)
    return [int(v if v < s // 2 else v - s) for v, s in zip(i, r.shape)]
def side_of(f):
    if ':' in f: return f.rsplit(':', 1)
    sid = os.path.basename(f)[:6]; g = os.path.dirname(os.path.dirname(os.path.abspath(f)))
    for k in sorted(os.listdir(g)):
        if k.endswith('_kit.md'):
            m = re.search(r'\*\*' + sid + r'\*\* · [^\n]*\n`start_frame` `([^`]+)`', open(os.path.join(g, k)).read())
            if m: return f, ('H' if 'host' in m.group(1) else 'G')
    return f, 'G'
def intrusion(f, s):
    # the far bottom corner, away from the person: host clips bottom-right, guest clips bottom-left (L19, P1_034)
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', 'scale=192:108,format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    F = np.frombuffer(raw, np.uint8).reshape(-1, 108, 192).astype(float)
    c = F[:, 81:, 168:] if s == 'H' else F[:, 81:, :24]
    return float(np.abs(np.diff(c, axis=0)).mean(axis=(1, 2)).max())
bad = 0
for arg in sys.argv[1:]:
    f, s = side_of(arg); worst = 0
    for box in BOX[s]:
        F = frames(f, box); n = len(F)
        for i in list(range(0, n, max(1, n // 8))) + [n - 1]:
            dy, dx = shift(F[0], F[i]); worst = max(worst, abs(dx) + abs(dy))
    edge = intrusion(f, s)
    ok = worst <= 3 and edge < 2.0   # 4-8 px of pure pan = SMALL: stabilise in the edit if it shows (L31); bad += not ok
    print(f'{os.path.basename(f):14s} camera {"held" if worst <= 3 else "MOVED"}  max background drift {worst} px'
          + ('' if edge < 2.0 else f'  ·  SOMETHING ENTERS the far corner (motion {edge:.1f})'))
sys.exit(1 if bad else 0)
