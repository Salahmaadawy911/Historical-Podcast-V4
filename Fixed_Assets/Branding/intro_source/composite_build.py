from PIL import Image, ImageDraw, ImageFont
import numpy as np, os, sys
N_ACCOUNTS = sys.argv[1] if len(sys.argv)>1 else "[N]"
OUTDIR = sys.argv[2] if len(sys.argv)>2 else "cofr"
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080; FPS=24; DUR=4.0; N=int(FPS*DUR)
INK=(18,22,28); WALNUT=(70,60,56); QUIET=(90,80,73)
F=lambda n,s: ImageFont.truetype(f"{B}/fonts/{n}",s)
kick=F("Oswald-SemiBold.ttf",38); body=F("LibreBaskerville-Regular.ttf",50); sub=F("LibreBaskerville-Regular.ttf",32)

PAPER=Image.open(f"{B}/paper_source.png").convert("RGB")
PAPER=PAPER.resize((2560,int(PAPER.height*2560/PAPER.width)),Image.LANCZOS)
_c={}
def paper_bg(z):
    k=round(z,4)
    if k in _c: return _c[k]
    pw,ph=PAPER.size; th=int(pw*H/W)
    im=PAPER.crop((0,(ph-th)//2,pw,(ph-th)//2+th))
    nw,nh=int(im.width/z),int(im.height/z)
    im=im.crop(((im.width-nw)//2,(im.height-nh)//2,(im.width-nw)//2+nw,(im.height-nh)//2+nh)).resize((W,H),Image.LANCZOS)
    _c[k]=im; return im
mark=Image.open(f"{B}/brand_mark_trimmed.png").convert("RGBA")
MH=42; MW=int(mark.width*MH/mark.height); mark=mark.resize((MW,MH),Image.LANCZOS); ma=mark.split()[3]

sc=Image.new("RGBA",(10,10)); sd=ImageDraw.Draw(sc)
def tw(t,f,tr=0): return sum(sd.textlength(c,font=f)+tr for c in t)-tr if tr else sd.textlength(t,font=f)
def layer(t,f,fill,tr=0):
    w=int(tw(t,f,tr))+8; a,d=f.getmetrics(); h=a+d+8
    im=Image.new("RGBA",(w,h),(0,0,0,0)); dr=ImageDraw.Draw(im)
    if tr:
        x=4
        for c in t: dr.text((x,4),c,font=f,fill=fill+(255,)); x+=dr.textlength(c,font=f)+tr
    else: dr.text((4,4),t,font=f,fill=fill+(255,))
    return im

# ---------------------------------------------------------------------------
# composite_build.py — eyewitness episodes only. Never on a named-figure episode.
#
#   python3 composite_build.py <N> <output dir>
#
# N is the number of first-hand accounts the character is assembled from. The
# wording is fixed in shape for the whole series; only N changes, so the RENDER
# is per part and belongs in Episodes/<Guest>/, not in Branding/.
# ---------------------------------------------------------------------------
L1=layer("COMPOSITE CHARACTER",kick,WALNUT,7)
L2=layer("This guest is a composite. No such individual existed.",body,INK)
L3=layer(f"The character is assembled from {N_ACCOUNTS} first-hand accounts,",sub,QUIET)
L4=layer("listed in the description.",sub,QUIET)
POS=[(L1,430),(L2,498),(L3,606),(L4,650)]
TIMING=[(0.05,0.60),(0.45,0.80),(1.20,0.55),(1.40,0.55)]
MARK_IN,MARK_D=1.80,0.50; OUT_ST,OUT_D=3.55,0.45
for l,y in POS: print("line w",l.width,"y",y,"fits" if l.width<W-212 else "TOO WIDE")

SOFT=110
def ease(x): return x*x*(3-2*x)
def wipe(l,p):
    if p>=1.0: return l
    w,h=l.size; x=-SOFT+p*(w+SOFT)
    col=np.clip((x-np.arange(w))/SOFT,0,1).astype(np.float32)
    a=np.asarray(l.split()[3],dtype=np.float32)*col[None,:]
    o=l.copy(); o.putalpha(Image.fromarray(a.astype(np.uint8))); return o

out=OUTDIR; os.makedirs(out,exist_ok=True)
for f in range(N):
    t=f/FPS
    fr=paper_bg(1.0+0.030*(t/19.166667)).convert("RGBA")
    fd=1.0-ease(min(1,max(0,(t-OUT_ST)/OUT_D)))
    if fd>0.003:
        lay=Image.new("RGBA",(W,H),(0,0,0,0))
        for (im,y),(t0,d) in zip(POS,TIMING):
            if t<t0: continue
            w2=wipe(im,ease(min(1.0,(t-t0)/d)))
            if fd<1.0:
                a=np.asarray(w2.split()[3],dtype=np.float32)*fd
                w2=w2.copy(); w2.putalpha(Image.fromarray(a.astype(np.uint8)))
            lay.alpha_composite(w2,(int((W-im.width)/2),y))
        if t>MARK_IN:
            aa=ease(min(1,(t-MARK_IN)/MARK_D))*0.85*fd
            m=mark.copy(); m.putalpha(ma.point(lambda v:int(v*aa)))
            lay.alpha_composite(m,(int((W-MW)/2),958))
        fr=Image.alpha_composite(fr,lay)
    fr.convert("RGB").save(f"{out}/f{f:03d}.png")
print("composite frames:",N)
