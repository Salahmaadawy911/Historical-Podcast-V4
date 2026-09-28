#!/usr/bin/env python3
"""
context_build.py — CONTEXT CARDS: who / where / what, on first mention.

Series-fixed design (spec: Branding/PLATE_SPEC.md §Context card, STUDIO_ASSETS.md).
Per-episode text comes ONLY from the kit's §12 "Context cards" table.

    python3 context_build.py plates                 # (re)build the two fixed plates, once
    python3 context_build.py still  <frame.png> <L|R> <LABEL> <NAME> <gloss> <source> <out.png>
    python3 context_build.py mov    <L|R> <LABEL> <NAME> <gloss> <source> <out.mov> [seconds]

Placement is by SCREEN SIDE, not by speaker:
  L = card sits screen-LEFT, bleeding off the left edge  -> used when the GUEST speaks (she sits right)
  R = card sits screen-RIGHT, bleeding off the right edge -> used when the HOST speaks (he sits left)
The card always goes OPPOSITE the speaker, in the upper band of the frame, clear of the face,
the subtitles, the name banner / pull-quote band (bottom) and the watermark (bottom-left).
"""
import os, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(HERE)                       # Fixed_Assets/Branding
REF_W, REF_H = 3840, 2160
# ---- geometry, fractions of the frame (fixed forever) ----
CARD_W, CARD_H = 0.36, 0.25                     # width, height
CARD_TOP = 0.075                                # top edge, fraction of frame height
RULE_W, RULE_INSET = 0.0036, 0.0216             # walnut margin rule, inset from the tear (frame widths)
TEAR_AMP = 0.006                                # tear amplitude, frame widths
INK = (18, 22, 28); SECOND = (70, 60, 56); WALNUT = (156, 107, 63); QUIET = (98, 88, 80)

def _tear_profile(h, amp, seed):
    rng = np.random.default_rng(seed); x = np.zeros(h)
    for octv, a in ((7, 1.0), (23, 0.45), (71, 0.22), (211, 0.1)):
        pts = rng.uniform(-1, 1, octv + 1)
        x += a * np.interp(np.linspace(0, octv, h), np.arange(octv + 1), pts)
    x = (x - x.min()) / (x.max() - x.min())
    return x * amp

def build_plates():
    pw, ph = int(CARD_W * REF_W), int(CARD_H * REF_H)
    src = Image.open(f"{B}/paper_source.png").convert("RGB")
    # a crop the name and pull-quote plates do not use: lower-left of the sheet, so it is not the same paper twice
    crop = src.crop((src.width - pw - 60, 60, src.width - 60, 60 + ph))   # upper-right of the sheet
    amp = TEAR_AMP * REF_W; soft = 3.0
    prof = _tear_profile(ph, amp, seed=1789)
    rw, ri = int(RULE_W * REF_W), int(RULE_INSET * REF_W)
    for side in ("L", "R"):
        a = np.full((ph, pw), 255.0)
        cols = np.arange(pw)[None, :]
        if side == "L":   # bleeds off the LEFT frame edge; torn edge on the right
            edge = pw - 1 - prof[:, None]
            a = np.clip((edge - cols) / soft, 0, 1) * 255
            fibre = np.clip(1 - np.abs(cols - edge) / 6, 0, 1)
        else:             # bleeds off the RIGHT frame edge; torn edge on the left
            edge = prof[:, None]
            a = np.clip((cols - edge) / soft, 0, 1) * 255
            fibre = np.clip(1 - np.abs(cols - edge) / 6, 0, 1)
        rgb = np.asarray(crop).astype(float)
        rgb = rgb * (1 - 0.10 * fibre[..., None]) + 245 * 0.10 * fibre[..., None]   # paler torn fibre
        im = Image.fromarray(np.dstack([rgb, a]).astype(np.uint8), "RGBA")
        d = ImageDraw.Draw(im)
        t, b = int(0.16 * ph), int(0.84 * ph)
        x0 = (pw - ri - rw) if side == "L" else ri
        d.rectangle((x0, t, x0 + rw, b), fill=WALNUT + (255,))
        im.save(f"{B}/BRAND_context_plate_{side}.png")
        print(f"  BRAND_context_plate_{side}.png  {pw}x{ph}")

def _font(n, s): return ImageFont.truetype(f"{B}/fonts/{n}", max(8, int(s)))
def _wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > maxw and cur: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur); return lines

def card_layer(W, H, side, label, name, gloss, source):
    """Full-frame RGBA with the card placed. Also returns the drawn text boxes for the wipe."""
    sc = W / REF_W
    plate = Image.open(f"{B}/BRAND_context_plate_{side}.png").convert("RGBA")
    pw, ph = int(plate.width * sc), int(plate.height * sc)
    plate = plate.resize((pw, ph), Image.LANCZOS)
    px = 0 if side == "L" else W - pw
    py = int(CARD_TOP * H)
    # text column: between the frame-edge inset and the margin rule, always LEFT-aligned (type never mirrors)
    rule_x = int((RULE_INSET + RULE_W) * W)
    if side == "L": tx0, tx1 = px + int(0.030 * W), px + pw - rule_x - int(0.014 * W)
    else:           tx0, tx1 = px + rule_x + int(0.016 * W), px + pw - int(0.022 * W)
    fl = _font("Oswald-SemiBold.ttf", 0.075 * ph); fn = _font("Anton-Regular.ttf", 0.185 * ph)
    fg = _font("LibreBaskerville-Regular.ttf", 0.105 * ph); fs = _font("LibreBaskerville-Italic.ttf", 0.078 * ph)
    scratch = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    size = 0.185 * ph
    while scratch.textlength(name, font=fn) > (tx1 - tx0) and size > 0.12 * ph:   # long names shrink, never wrap
        size *= 0.95; fn = _font("Anton-Regular.ttf", size)
    glines = _wrap(scratch, gloss, fg, tx1 - tx0)
    rows = [(label, fl, WALNUT, 0.085, 0.20)]          # text, font, colour, top (frac of plate), tracking (em)
    rows.append((name, fn, INK, 0.175, 0.0))
    y = 0.435
    for g in glines[:3]:
        rows.append((g, fg, SECOND, y, 0.0)); y += 0.125
    if len(glines) > 3: raise SystemExit(f'context card gloss runs to {len(glines)} lines — three is the maximum; shorten it: {gloss!r}')
    rows.append((source, fs, QUIET, y + 0.03, 0.0))
    text = []
    for t, f, col, top, trk in rows:
        w = int(scratch.textlength(t, font=f) + trk * f.size * len(t)) + 8
        a_, d_ = f.getmetrics(); lay = Image.new("RGBA", (w, a_ + d_ + 8), (0, 0, 0, 0)); dd = ImageDraw.Draw(lay)
        if trk:
            x = 4
            for c in t: dd.text((x, 4), c, font=f, fill=col + (255,)); x += scratch.textlength(c, font=f) + trk * f.size
        else: dd.text((4, 4), t, font=f, fill=col + (255,))
        text.append((lay, tx0, py + int(top * ph)))
    return plate, (px, py), text, len(glines)

def shadow(plate, W):
    s = plate.split()[3].filter(ImageFilter.GaussianBlur(9 * W / REF_W))
    sh = Image.new("RGBA", plate.size, (0, 0, 0, 0)); sh.putalpha(s.point(lambda v: int(v * 0.6))); return sh

def still(frame, side, label, name, gloss, source, out):
    bg = Image.open(frame).convert("RGB"); W = 1920
    H = int(round(bg.height * W / bg.width)); bg = bg.resize((W, H), Image.LANCZOS).crop((0, (H - 1080) // 2, W, (H - 1080) // 2 + 1080)).convert("RGBA")
    W, H = bg.size
    plate, (px, py), text, n = card_layer(W, H, side, label, name, gloss, source)
    off = (int(4 * W / REF_W), int(6 * W / REF_W))
    bg.alpha_composite(shadow(plate, W), (px + off[0], py + off[1])); bg.alpha_composite(plate, (px, py))
    for lay, x, y in text: bg.alpha_composite(lay, (x, y))
    bg.convert("RGB").save(out); print(f"  {out}  ({n} gloss lines)")

# ---- §12 "Context cards" table ----
def parse(kit):
    import re
    t = open(kit, encoding="utf-8").read()
    i = t.index("### Context cards"); j = t.find("\n## ", i); sec = t[i:j if j > 0 else None]
    rows = []
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*`(P\d_\d+[a-z]?)`\s*\|\s*(.+?)\s*\|\s*([LR])\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", sec, re.M):
        n, shot, word, side, label, name, gloss, src = m.groups()
        rows.append(dict(n=n, shot=shot, word=word, side=side, label=label, name=name, gloss=gloss, source=src.replace("*", "")))
    return rows

def ease(x): return x * x * (3 - 2 * x)
def mov(side, label, name, gloss, source, out, dur=5.5, W=1920, H=1080, FPS=24):
    """Alpha .mov. Enters from its own frame edge (the side it bleeds off), text sets in line by line,
    exits by fading — same motion family as the name banner and pull-quote."""
    plate, (px, py), text, _ = card_layer(W, H, side, label, name, gloss, source)
    sh = shadow(plate, W); off = (int(4 * W / REF_W), int(6 * W / REF_W))
    import tempfile
    d = tempfile.mkdtemp(prefix="ctxfr_")      # frames outside the project: the bridge cannot delete inside it
    N = int(FPS * dur); SOFT = 90
    def wipe(l, p):
        if p >= 1: return l
        w = l.size[0]; x = -SOFT + p * (w + SOFT)
        col = np.clip((x - np.arange(w)) / SOFT, 0, 1).astype(np.float32)
        a = np.asarray(l.split()[3], dtype=np.float32) * col[None, :]; o = l.copy(); o.putalpha(Image.fromarray(a.astype(np.uint8))); return o
    def fade(im, a):
        if a >= 1: return im
        o = im.copy(); o.putalpha(im.split()[3].point(lambda v: int(v * a))); return o
    for fr in range(N):
        t = fr / FPS; a = ease(min(1, t / 0.45)) * (1 - ease(min(1, max(0, (t - (dur - 0.45)) / 0.40))))
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        if a > 0.003:
            dx = int((-18 if side == "L" else 18) * (1 - ease(min(1, t / 0.45))))
            im.alpha_composite(fade(sh, a), (px + dx + off[0], py + off[1])); im.alpha_composite(fade(plate, a), (px + dx, py))
            for i, (lay, x, y) in enumerate(text):
                t0 = 0.25 + 0.12 * i
                if t >= t0: im.alpha_composite(fade(wipe(lay, ease(min(1, (t - t0) / 0.5))), a), (x + dx, y))
        im.save(f"{d}/f{fr:03d}.png")
    subprocess.run(["ffmpeg", "-v", "error", "-r", str(FPS), "-i", f"{d}/f%03d.png", "-c:v", "qtrle", "-pix_fmt", "argb", out, "-y"], check=True)
    webm = out[:-4] + ".webm"
    subprocess.run(["ffmpeg", "-v", "error", "-r", str(FPS), "-i", f"{d}/f%03d.png", "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "32", webm, "-y"], check=True)
    print(f"  {os.path.basename(out)} + .webm  {side}  {dur}s  {name}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "plates": build_plates()
    elif cmd == "still": still(*sys.argv[2:9])
    elif cmd == "check":            # validate every card in a kit fits (name width, gloss <= 3 lines)
        for r in parse(sys.argv[2]):
            _, _, _, n = card_layer(1920, 1080, r["side"], r["label"], r["name"], r["gloss"], r["source"])
            print(f"  {r['n']}  {r['shot']}  {r['side']}  {r['name']:26s} {n} gloss lines")
    elif cmd == "mov": mov(*sys.argv[2:8], *( [float(sys.argv[8])] if len(sys.argv) > 8 else []))
    else: sys.exit(__doc__)
