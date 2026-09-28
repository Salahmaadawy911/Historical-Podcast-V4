import numpy as np, os, subprocess, shutil
from PIL import Image
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1916,1080
paper=Image.open(f"{B}/paper_source.png").convert("RGB")
# paper_source is 2720x1536 (16:9.03) -> resize to the clip size
paper=paper.resize((W,H),Image.LANCZOS)
P=np.asarray(paper,dtype=np.float32)

def margin_mean(a):
    m=int(H*0.05)
    band=np.concatenate([a[:m].reshape(-1,3),a[-m:].reshape(-1,3),
                         a[:,:m].reshape(-1,3),a[:,-m:].reshape(-1,3)])
    return band.mean(0)

report={}
for name in ("vessel_4s","stone_4s"):
    src=f"raw_{name}"; dst=f"fix_{name}"
    shutil.rmtree(src,ignore_errors=True); shutil.rmtree(dst,ignore_errors=True)
    os.makedirs(src); os.makedirs(dst)
    subprocess.run(["ffmpeg","-v","error","-i",f"{B}/{name}.mp4",f"{src}/f%04d.png","-y"],check=True)
    files=sorted(os.listdir(src))
    f0=np.asarray(Image.open(f"{src}/{files[0]}").convert("RGB"),dtype=np.float32)
    m0=margin_mean(f0)
    drift=[]
    for i,fn in enumerate(files):
        a=np.asarray(Image.open(f"{src}/{fn}").convert("RGB"),dtype=np.float32)
        g=margin_mean(a)/np.maximum(m0,1e-3)          # this frame's paper gain vs frame 0
        drift.append(g)
        a=a/np.maximum(g,1e-3)                         # remove the drift
        r=np.clip(a/np.maximum(f0,1.0),0.0,1.0)        # ink transmittance, ink only darkens
        out=np.clip(P*r,0,255).astype(np.uint8)
        Image.fromarray(out).save(f"{dst}/f{i:04d}.png")
    d=np.array(drift)
    report[name]=dict(m0=m0, drift_end=d[-1], drift_max=d.max(0), drift_min=d.min(0))
    print(name,"frames",len(files),"frame0 margin",np.round(m0,1),
          "end gain",np.round(d[-1],4),"min",np.round(d.min(0),4))
print("REPORT_DONE")

# ---------------------------------------------------------------------------
# paper_restore.py — put the real page back under a generated draw-on clip.
#
# Why: the video model reproduces paper_source.png closely but not exactly, and
# it drifts darker across the clip. Measured on the 4s break clips (2026-09-18):
#   frame 0 margin sits ~1% under paper_source
#   by frame 96 the paper has darkened a further 1.0-1.5%
# Invisible in isolation, visible when the clip is cut against the opening,
# which uses the real page.
#
# How: a drawing on paper is multiplicative - what you see is paper x ink.
#   1. measure each frame's paper gain from the outer 5% margin, where no
#      drawing ever reaches, and divide it out. That removes the drift exactly.
#   2. divide the frame by its own frame 0 to get ink transmittance alone.
#   3. multiply by the real paper_source.
# The clip's own frame 0 is the blank page, so nothing has to be tone-matched
# against paper_source by hand and any paper the model invented is discarded.
#
# Run it on every draw-on clip before the clip becomes an asset.
# ---------------------------------------------------------------------------
