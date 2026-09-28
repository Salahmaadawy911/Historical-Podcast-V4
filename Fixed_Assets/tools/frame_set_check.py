"""Frame-set check — is everything except the person identical across a set of start frames?

  python3 Fixed_Assets/tools/frame_set_check.py                 # all sets in Start_Frames/
  python3 Fixed_Assets/tools/frame_set_check.py Start_Frames/Cleopatra

Each frame is compared with its set's reference (Host: frame_host; direct pairs against their guest-facing twin;
guest: frame_<guest>; wide: frame_wide_<guest>). The frame is cut into a 8x6 grid; each cell is aligned by phase
correlation; the cells with the largest leftover difference (where the person changed) are dropped, and the rest —
the room — give: SHIFT (median px), SCALE (px of spread between the left and right of frame = zoom), LUMA (% change),
COLOUR (mean RGB change) and RESIDUAL (room difference left after alignment). Units are px at 1920x1080.
PASS: shift <= 2 px, scale <= 3 px, |luma| <= 2 %, colour <= 3, room <= 7 (wide <= 12) — calibrated on the set. Added 2026-09-26 (Salah): start and
end frames of one clip must share the room exactly; Mode 2 runs this on every new guest before approval.
"""
import os, re, sys, glob
import numpy as np
from PIL import Image
W, H = 1920, 1080
def load(p): return np.asarray(Image.open(p).convert('RGB').resize((W, H), Image.LANCZOS)).astype(float)
def shift(a, b):
    A = np.fft.fft2(a - a.mean()); B = np.fft.fft2(b - b.mean()); R = A * np.conj(B); R /= np.abs(R) + 1e-9
    r = np.abs(np.fft.ifft2(R)); i = np.unravel_index(r.argmax(), r.shape)
    return [int(v if v < s // 2 else v - s) for v, s in zip(i, r.shape)]   # dy, dx
def compare(ref, img):
    ga, gb = ref.mean(2), img.mean(2); cells = []
    cw, ch = W // 8, H // 6
    for gy in range(6):
        for gx in range(8):
            y, x = gy * ch, gx * cw
            a, b = ga[y:y+ch, x:x+cw], gb[y:y+ch, x:x+cw]
            if a.std() < 4: continue                      # featureless wall: no signal
            dy, dx = shift(a, b)
            bb = np.roll(np.roll(b, dy, 0), dx, 1)
            res = np.abs(a - bb)[8:-8, 8:-8].mean()
            cells.append((res, dx, dy, x + cw / 2, (ref[y:y+ch, x:x+cw] - img[y:y+ch, x:x+cw]).reshape(-1, 3).mean(0)))
    cells.sort(key=lambda c: c[0]); keep = cells[:max(6, int(len(cells) * 0.6))]   # drop the person's cells
    dxs = np.array([c[1] for c in keep]); dys = np.array([c[2] for c in keep]); xs = np.array([c[3] for c in keep])
    sh = (float(np.median(dxs)), float(np.median(dys)))
    left, right = dxs[xs < W / 2], dxs[xs >= W / 2]
    scale = float(np.median(right) - np.median(left)) if len(left) and len(right) else 0.0
    col = np.mean([c[4] for c in keep], axis=0)
    luma = -float(col.mean()) / max(ref.mean(), 1) * 100
    return sh, scale, luma, float(np.abs(col).max()), float(np.median([c[0] for c in keep]))
def verdict(sh, sc, lu, co, re_, wide=False):
    bad = []
    if max(abs(sh[0]), abs(sh[1])) > 2: bad.append('SHIFT')
    if abs(sc) > 3: bad.append('SCALE')
    if abs(lu) > 2: bad.append('LUMA')
    if co > 3: bad.append('COLOUR')
    if re_ > (12 if wide else 7): bad.append('ROOM')   # calibrated: good studio frames sit at 4-6 (grain), wide 8-11
    return 'PASS' if not bad else 'CHECK ' + ' '.join(bad)
# L41 — furniture landmarks. The grid check drops the cells with the highest residual as "person", and the chair
# sits right beside the person, so a bigger chair was dropped with her (Cleopatra b/d/e passed with a taller chair).
# A set may carry landmarks.json: windows that each hold one horizontal furniture edge; the edge row is found in each.
import json
def edge_rows(path, wins):
    g = np.asarray(Image.open(path).convert('L').resize((1920, 1080))).astype(float); out = {}
    for n, (x0, x1, y0, y1) in wins.items():
        prof = np.median(g[y0:y1, x0:x1], 1); d = np.abs(np.diff(np.convolve(prof, np.ones(3) / 3, 'same'))); d[:2] = 0; d[-2:] = 0
        out[n] = int(np.argmax(d) + y0)
    return out
def furniture(d, a, b):
    lp = os.path.join(d, 'landmarks.json')
    if not os.path.exists(lp) or 'wide' in b: return ''
    wins = {k: v for k, v in json.load(open(lp)).items() if not k.startswith('_')}
    ra, rb = edge_rows(a, wins), edge_rows(b, wins); moved = [k for k in wins if abs(ra[k] - rb[k]) > 12]
    return ('  FURNITURE ' + ', '.join(f'{k} {rb[k]-ra[k]:+d}px' for k in moved)) if len(moved) >= 2 else ''

def pairs(d):
    fs = sorted(glob.glob(os.path.join(d, 'frame_*.png'))); names = {os.path.basename(f)[:-4]: f for f in fs}
    out = []
    if os.path.basename(d) == 'Host':
        for k in names:
            if k != 'frame_host' and not k.startswith('frame_host_direct'): out.append(('frame_host', k))
        twin = {'frame_host_direct': 'frame_host', 'frame_host_direct_b': 'frame_host_b', 'frame_host_direct_c': 'frame_host_e'}
        for a, b in twin.items():
            if a in names and b in names: out.append((b, a))
    else:
        g = os.path.basename(d).lower()
        for k in names:
            if k.startswith('frame_wide') :
                ref = f'frame_wide_{g}' + ('_marked' if k.endswith('_marked') else '')
                if k != ref and ref in names: out.append((ref, k))
            elif k != f'frame_{g}' and f'frame_{g}' in names: out.append((f'frame_{g}', k))
    return [(names[a], names[b]) for a, b in out]
dirs = sys.argv[1:] or [d for d in sorted(glob.glob('Start_Frames/*')) if os.path.isdir(d) and not os.path.basename(d).startswith('_')]
bad = 0
for d in dirs:
    print(f'== {d}')
    cache = {}
    for a, b in pairs(d):
        ra = cache.setdefault(a, load(a)); rb = load(b)
        sh, sc, lu, co, re_ = compare(ra, rb); v = verdict(sh, sc, lu, co, re_, 'wide' in b)
        fu = furniture(d, a, b)
        if fu: v = ('CHECK' if v == 'PASS' else v) + fu
        bad += v != 'PASS'
        print(f'  {os.path.basename(b)[:-4]:26s} vs {os.path.basename(a)[:-4]:22s} shift {sh[0]:+.0f},{sh[1]:+.0f}  scale {sc:+.0f}  luma {lu:+.1f}%  colour {co:.1f}  room {re_:.1f}  {v}')
sys.exit(1 if bad else 0)
