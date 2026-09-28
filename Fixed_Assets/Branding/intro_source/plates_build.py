#!/usr/bin/env python3
"""
plates_build.py — lower thirds and pull-quotes, rendered per episode.

    python3 plates_build.py <episode dir> [--only lowerthird|pullquote]

Reads §12 of that episode's kit (`P<n>_kit.md`, `--part N`, default 1) — the lower-third names and the
key lines with the shot each lands over — and writes one alpha .mov per plate
into the episode folder. §12 is the single source: text and placement are
decided at Mode 3/4 and never invented at the edit.

Geometry is fixed forever in Branding/PLATE_SPEC.md and is reproduced here:
  plate outer edge flush to frame, bottom edge at 90% of frame height
  _R = guest (screen-right), _L = host (screen-left); the plate flips, words do not
  text x-offsets inside the plate at the 3840 reference, scaled
  no drop shadow baked in - it is applied in the edit so it sits over the picture
"""
import re, sys, os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080; FPS=24
INK=(18,22,28); SECOND=(70,60,56)
REF=3840.0; SC=W/REF                      # 1920 / 3840 reference

PLATE={ "lowerthird": {"file":"BRAND_lowerthird_plate_%s.png", "w":1612, "h":270,
                       "xr":166, "xl":1446},
        "pullquote":  {"file":"BRAND_pullquote_plate_%s.png",  "w":2112, "h":334,
                       "xr":166, "xl":1946} }

def font(n,s): return ImageFont.truetype(f"{B}/fonts/{n}",int(s))
sc=Image.new("RGBA",(10,10)); sd=ImageDraw.Draw(sc)
def layer(t,f,fill):
    w=int(sd.textlength(t,font=f))+8; a,d=f.getmetrics()
    im=Image.new("RGBA",(w,a+d+8),(0,0,0,0)); ImageDraw.Draw(im).text((4,4),t,font=f,fill=fill+(255,))
    return im

def ease(x): return x*x*(3-2*x)
SOFT=90
def wipe(l,p):
    if p>=1.0: return l
    w,h=l.size; x=-SOFT+p*(w+SOFT)
    col=np.clip((x-np.arange(w))/SOFT,0,1).astype(np.float32)
    a=np.asarray(l.split()[3],dtype=np.float32)*col[None,:]
    o=l.copy(); o.putalpha(Image.fromarray(a.astype(np.uint8))); return o
def fade(im,a):
    if a>=1.0: return im
    o=im.copy(); o.putalpha(im.split()[3].point(lambda v:int(v*a))); return o

def render(kind, side, lines, out_mp4, dur):
    """side: 'L' (host, screen-left) or 'R' (guest, screen-right)."""
    spec=PLATE[kind]
    pw,ph=int(spec["w"]*SC), int(spec["h"]*SC)
    plate=Image.open(f"{B}/{spec['file']%side}").convert("RGBA").resize((pw,ph),Image.LANCZOS)
    px = 0 if side=="L" else W-pw                      # outer edge flush to the frame edge
    py = int(0.90*H)-ph                                # bottom edge at 90% of frame height

    if kind=="lowerthird":
        f1=font("Anton-Regular.ttf", 0.44*ph); f2=font("LibreBaskerville-Regular.ttf", 0.16*ph)
        rows=[(layer(lines[0],f1,INK), 0.155), (layer(lines[1],f2,SECOND), 0.70)]
    else:
        f=font("PlayfairDisplay-Italic.ttf", 0.285*ph)
        rows=[(layer(lines[0],f,INK), 0.17)] + ([(layer(lines[1],f,INK), 0.545)] if len(lines)>1 else [])

    items=[]
    for lay_,top in rows:
        if side=="R": x = px+int(spec["xr"]*SC)                       # left-aligned from
        else:         x = px+int(spec["xl"]*SC)-lay_.width            # right-aligned to
        items.append((lay_, x, py+int(top*ph)))

    N=int(FPS*dur); IN_D=0.45; OUT_ST=dur-0.45; OUT_D=0.40
    T=[(0.28,0.45),(0.52,0.55)]
    import tempfile
    d=tempfile.mkdtemp(prefix="plfr_")   # outside the project: the bridge cannot delete inside it (was ./_plfr until 2026-09-23)
    for fr in range(N):
        t=fr/FPS
        a_in=ease(min(1.0,t/IN_D)); a_out=1.0-ease(min(1.0,max(0.0,(t-OUT_ST)/OUT_D)))
        a=a_in*a_out
        im=Image.new("RGBA",(W,H),(0,0,0,0))
        if a>0.003:
            dx=int((-18 if side=="L" else 18)*(1.0-a_in))   # settles in from its own frame edge
            im.alpha_composite(fade(plate,a),(px+dx,py))
            for (l,x,y),(t0,dd) in zip(items,T):
                if t<t0: continue
                im.alpha_composite(fade(wipe(l,ease(min(1.0,(t-t0)/dd))),a),(x+dx,y))
        im.save(f"{d}/f{fr:03d}.png")
    subprocess.run(["ffmpeg","-v","error","-r",str(FPS),"-i",f"{d}/f%03d.png",
                    "-c:v","qtrle","-pix_fmt","argb",out_mp4,"-y"],check=True)
    print(f"  {os.path.basename(out_mp4):38s} {kind:11s} _{side}  {dur}s  {lines[0][:40]}")

# ---------------- §12 parsing ----------------
def section12(kit):
    t=open(kit,encoding="utf-8").read()
    i=t.index("## 12 · On-screen text"); j=t.index("\n## ",i+10)
    return t[i:j]

def parse(kit):
    s=section12(kit)
    lower=[]
    for m in re.finditer(r"^\|\s*(Host|Guest)\s*\|\s*`(P\d_\d+[a-z]?)`[^|]*\|\s*(.+?)\s*\|$", s, re.M):
        who,shot,reads=m.groups()
        reads=reads.replace("*","")
        name,_,second=reads.partition("/")
        lower.append(dict(who=who, shot=shot, name=name.strip(), second=second.strip()))
    quotes=[]
    for m in re.finditer(r'^\|\s*"(.+?)"\s*\|\s*`(P\d_\d+[a-z]?)`\s*\|\s*`(P\d_\d+[a-z]?)`(.*?)\|$', s, re.M):
        quotes.append(dict(line=m.group(1), said_in=m.group(2), over=m.group(3)))
    return lower, quotes

def wrap(t, n=34):
    w=t.split(); a=[]; cur=""
    for x in w:
        if len(cur)+len(x)+1>n and cur: a.append(cur); cur=x
        else: cur=(cur+" "+x).strip()
    a.append(cur); return a[:2]

if __name__=="__main__":
    ep=sys.argv[1]
    PART="P"+(sys.argv[sys.argv.index("--part")+1].lstrip("Pp") if "--part" in sys.argv else "1")
    kit=os.path.join(ep,f"{PART}_kit.md")
    TAG="" if PART=="P1" else PART.lower()+"_"      # Part 1 keeps its original names
    lower,quotes=parse(kit)
    print(f"§12: {len(lower)} lower thirds, {len(quotes)} pull-quotes\n")
    for l in lower:
        side = "L" if l["who"]=="Host" else "R"
        render("lowerthird", side, [l["name"], l["second"]],
               os.path.join(ep,f"BRAND_lowerthird_{l['who'].lower()}.mov"), 4.5)
    ktxt=open(kit,encoding="utf-8").read()
    def side_of(shot):   # the pull-quote sits on the SPEAKER's side: host L, guest R
        m=re.search(r"\*\*"+re.escape(shot)+r"\*\* · \w+ · (HOST|GUEST)",ktxt)
        return "L" if m and m.group(1)=="HOST" else "R"
    for i,q in enumerate(quotes,1):
        render("pullquote", side_of(q["said_in"]), wrap(q["line"]),
               os.path.join(ep,f"BRAND_pullquote_{TAG}{i:02d}.mov"), 5.0)
    print("\nPlacement (from §12 — do not invent at the edit):")
    for l in lower: print(f"  lowerthird_{l['who'].lower():5s} opens over {l['shot']}")
    for i,q in enumerate(quotes,1): print(f"  pullquote_{i:02d}      lands over {q['over']}   \"{q['line'][:46]}\"")
