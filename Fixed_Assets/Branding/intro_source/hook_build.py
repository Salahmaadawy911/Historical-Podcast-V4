#!/usr/bin/env python3
"""
hook_build.py — the opening's hook slot: the guest's face emerging from the paper.

    python3 hook_build.py <hook_clip.mp4> <in_seconds> <out_opening.mp4>
                          --face CX,CY,H  [--freeze auto|off]

Series-fixed design (approved 2026-09-22 from Salah's mockup; spec in SERIES_FURNITURE.md):
  * the 4.00–8.00 s slot of BRAND_opening.mp4 becomes the same paper as the card and the intro,
    with the SAME continuous slow zoom, so 0:00–0:19 stays one unbroken page;
  * the guest's face, cropped from the hook clip and pushed in close, is laid onto the paper inside
    a soft, hand-cut polygon that deliberately keeps a little of the studio around the head —
    it must read as a frame lifted from the show, not a cut-out;
  * the paper's grain shows through the face (a portrait printed on the page) and eats the edge;
  * VOICE BEFORE FACE: the line starts on an almost-invisible face; she is fully present by the end
    of the line; a held beat on the closed-mouth face; a quick fade back to bare paper just before
    the strike at 8.00, where the first charcoal study begins.

--face CX,CY,H : the head in the hook clip's frame — centre x, centre y and crown-to-chin height,
                 in pixels of the 1920×1080 source. Per guest, fixed by the seed frames; recorded in
                 the guest's CAST.md (performance profile → "Hook framing").
--freeze auto  : if the take does not pause cleanly after the line (speech resumes before 8.00),
                 hold the last closed-mouth frame and cut the audio there. Default auto.
"""
import os, sys, subprocess, tempfile
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(HERE)
W, H, FPS = 1920, 1080, 24
SLOT0, SLOT1, TOTAL = 4.0, 8.0, 19.166667           # slot in BRAND_opening; total, for the paper zoom
FACE_OUT = (960, 470)                                 # where the head centre lands on the page
HEAD_OUT = 650                                        # crown-to-chin on the page, px
PUSH = 0.035                                          # slow push-in across the slot

PAPER = Image.open(f"{B}/paper_source.png").convert("RGB")
PAPER = PAPER.resize((2560, int(PAPER.height * 2560 / PAPER.width)), Image.LANCZOS)
def paper_bg(zoom):                                   # identical to card_build / intro_build
    pw, ph = PAPER.size; th = int(pw * H / W)
    im = PAPER.crop((0, (ph - th) // 2, pw, (ph - th) // 2 + th))
    nw, nh = int(im.width / zoom), int(im.height / zoom)
    im = im.crop(((im.width - nw) // 2, (im.height - nh) // 2, (im.width - nw) // 2 + nw, (im.height - nh) // 2 + nh))
    return im.resize((W, H), Image.LANCZOS)

def ease(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

def speech(clip, t_in, dur):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t_in), '-t', str(dur), '-i', clip, '-ac', '1', '-ar', '16000',
                          '-f', 's16le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768
    w = 800; n = len(a) // w
    db = 20 * np.log10(np.sqrt((a[:n * w].reshape(n, w) ** 2).mean(1) + 1e-12))
    on = np.where(db > -40)[0]
    if not len(on): return None, None, None
    start = on[0] * 0.05
    # end of the first spoken sentence = first gap >= 0.45 s after the onset
    end = None; resume = None
    for i in range(on[0], n):
        if db[i] <= -40:
            j = i
            while j < n and db[j] <= -40: j += 1
            if (j - i) * 0.05 >= 0.45: end = i * 0.05; resume = j * 0.05 if j < n else None; break
    return start, end if end is not None else n * 0.05, resume

def mask(seed=1789):
    """Soft hand-cut polygon: head and shoulders, with a little studio left in on purpose."""
    rng = np.random.default_rng(seed); cx, cy = FACE_OUT[0], FACE_OUT[1] + 90
    rx, ry_top, ry_bot = 420, 470, 620; pts = []          # paper stays visible above the head
    for k in range(13):
        a = 2 * np.pi * k / 13 + rng.uniform(-0.12, 0.12)
        r = 1 + rng.uniform(-0.09, 0.07)
        ry = ry_top if np.sin(a) < 0 else ry_bot
        pts.append((cx + rx * r * np.cos(a), cy + ry * r * np.sin(a)))
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon(pts, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(55))
    a = np.asarray(m).astype(np.float32) / 255
    # the paper eats the edge: grain decides where the soft edge breaks up
    g = np.asarray(paper_bg(1.0).convert('L')).astype(np.float32)
    g = (g - g.mean()) / (g.std() + 1e-6)
    edge = 4 * a * (1 - a)                                        # 1 at the middle of the feather
    return np.clip(a + 0.35 * edge * g, 0, 1)

def main():
    clip, t_in, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    cx, cy, hh = [float(v) for v in sys.argv[sys.argv.index('--face') + 1].split(',')]
    freeze = sys.argv[sys.argv.index('--freeze') + 1] if '--freeze' in sys.argv else 'auto'
    dur = SLOT1 - SLOT0
    s_on, s_end, s_resume = speech(clip, t_in, dur + 0.6)
    print(f'line: {s_on:.2f}–{s_end:.2f} s into the slot; next speech at {s_resume}')
    frz = None
    if freeze == 'auto' and s_resume is not None and s_resume < dur:
        frz = min(s_end + 0.25, dur); print(f'take resumes before the strike → freeze at {frz:.2f} s, audio cut there')
    # timing, in slot seconds
    fin0, fin1 = 0.05, min(s_end + 0.10, 2.9)        # voice before face: full presence at the end of the line
    fout0, fout1 = 3.55, 3.96                          # held beat, then back to bare paper before the strike
    M = mask()[:, :, None]
    tmp = tempfile.mkdtemp(prefix='hook_')
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t_in), '-t', str(dur), '-i', clip, '-vf', 'scale=1920:1080',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    src = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    N = int(round(dur * FPS))
    for i in range(N):
        t = i / FPS
        k = min(i, len(src) - 1) if frz is None else min(i, int(frz * FPS), len(src) - 1)
        paper = paper_bg(1.0 + 0.030 * ((SLOT0 + t) / TOTAL))
        P = np.asarray(paper).astype(np.float32)
        a = ease((t - fin0) / (fin1 - fin0)) * (1 - ease((t - fout0) / (fout1 - fout0)))
        if a > 0.002:
            s = HEAD_OUT / hh * (1 + PUSH * t / dur)
            sw, sh = W / s, H / s
            x0 = cx - FACE_OUT[0] / s; y0 = cy - FACE_OUT[1] / s
            face = Image.fromarray(src[k]).crop((int(x0), int(y0), int(x0 + sw), int(y0 + sh))).resize((W, H), Image.LANCZOS)
            face = face.filter(ImageFilter.UnsharpMask(radius=2.2, percent=70, threshold=2))
            F = np.asarray(face).astype(np.float32)
            F = F * (P / P.mean((0, 1))) ** 0.55                  # the page shows through the face
            F = F * 0.93 + P * 0.07                                 # a breath of paper tone
            out_ = P * (1 - a * M) + F * (a * M)
        else:
            out_ = P
        Image.fromarray(np.clip(out_, 0, 255).astype(np.uint8)).save(f'{tmp}/f{i:03d}.png')
    slot = f'{tmp}/slot.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-r', str(FPS), '-i', f'{tmp}/f%03d.png', '-c:v', 'libx264', '-crf', '14',
                    '-pix_fmt', 'yuv420p', slot], check=True)
    a_end = frz if frz is not None else dur
    opening = f'{B}/BRAND_opening.mp4'
    fc = (f"[1:v]setpts=PTS-STARTPTS+{SLOT0}/TB[s];[0:v][s]overlay=0:0:enable='between(t,{SLOT0},{SLOT1 - 0.001})':eof_action=pass[v];"
          f"[2:a]atrim=0:{a_end:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={max(0, a_end - 0.04):.3f}:d=0.04,"
          f"aresample=44100,adelay={int(SLOT0 * 1000)}|{int(SLOT0 * 1000)}[h];[0:a][h]amix=inputs=2:normalize=0:duration=first[a]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', opening, '-i', slot, '-ss', str(t_in), '-t', str(dur), '-i', clip,
                    '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out], check=True)
    print('written', out)

if __name__ == '__main__': main()
