#!/usr/bin/env python3
"""outro_mark.py — put BRAND_mark on the lit panel of a per-part outro wide (2026-09-28, L59).

Usage: python3 Fixed_Assets/tools/outro_mark.py Start_Frames/<Guest>/frame_wide_<guest>_outro.png
Writes <same>_marked.png. Fixed coordinates from STUDIO_ASSETS.md (plate 2720x1536, panel face x1121-1591 y394-556,
mark 399x129 at (1156,410), dark ink #12161C, brand_mark_trimmed.png). Stops if the panel is not where it should be
(the Seedream composite must keep cam3_wide's framing).
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
src = sys.argv[1]; root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = Image.open(src).convert('RGB')
if base.size != (2720, 1536): base = base.resize((2720, 1536), Image.LANCZOS)
g = np.asarray(base.convert('L')).astype(float)[300:700, 1000:1700] > 195
rows = np.nonzero(g.sum(1) > 200)[0]; cols = np.nonzero(g.sum(0) > 80)[0]
face = (cols.min() + 1000, cols.max() + 1000, rows.min() + 300, rows.max() + 300)
if max(abs(face[0] - 1122), abs(face[1] - 1591), abs(face[2] - 393), abs(face[3] - 555)) > 6:
    sys.exit(f'STOP — panel face found at {face}, expected (1122, 1591, 393, 555): the composite moved the framing; regenerate it')
mk = Image.open(os.path.join(root, 'Fixed_Assets/Branding/brand_mark_trimmed.png')).convert('RGBA').resize((399, 129), Image.LANCZOS)
a = np.asarray(mk.split()[3].filter(ImageFilter.GaussianBlur(0.7))).astype(float) / 255 * 0.94
arr = np.asarray(base).astype(float); x, y = 1156, 410
arr[y:y + 129, x:x + 399] = arr[y:y + 129, x:x + 399] * (1 - a[..., None]) + np.array([0x12, 0x16, 0x1C], float) * a[..., None]
out = src[:-4] + '_marked.png'; Image.fromarray(arr.clip(0, 255).astype(np.uint8)).save(out); print('→', out)
