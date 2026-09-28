from PIL import Image, ImageDraw, ImageFont
import numpy as np, os, sys
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080
INK=(18,22,28); WALNUT=(140,88,48); QUIET=(90,80,73); BODY=(30,28,30)
F=lambda n,s: ImageFont.truetype(f"{B}/fonts/{n}",s)
kick   = F("Oswald-SemiBold.ttf",27)
body   = F("LibreBaskerville-Regular.ttf",29)
src    = F("LibreBaskerville-Regular.ttf",25)
nexttl = F("Anton-Regular.ttf",46)
pers   = F("LibreBaskerville-Italic.ttf",27)
sig    = F("LibreBaskerville-Italic.ttf",23)

PAPER=Image.open(f"{B}/paper_source.png").convert("RGB")
PAPER=PAPER.resize((2560,int(PAPER.height*2560/PAPER.width)),Image.LANCZOS)
_cache={}
def paper_bg(zoom):
    k=round(zoom,4)
    if k in _cache: return _cache[k]
    pw,ph=PAPER.size; th=int(pw*H/W)
    im=PAPER.crop((0,(ph-th)//2,pw,(ph-th)//2+th))
    nw,nh=int(im.width/zoom),int(im.height/zoom)
    im=im.crop(((im.width-nw)//2,(im.height-nh)//2,(im.width-nw)//2+nw,(im.height-nh)//2+nh))
    im=im.resize((W,H),Image.LANCZOS)
    if len(_cache)<120: _cache[k]=im
    return im

mark=Image.open(f"{B}/brand_mark_trimmed.png").convert("RGBA")
MH=110; MW=int(mark.width*MH/mark.height); mark=mark.resize((MW,MH),Image.LANCZOS)

scratch=Image.new("RGBA",(10,10)); sd=ImageDraw.Draw(scratch)
def tw(t,f,tr=0): return sum(sd.textlength(c,font=f)+tr for c in t)-tr if tr else sd.textlength(t,font=f)
def layer(t,f,fill,tr=0):
    w=int(tw(t,f,tr))+8; a,d=f.getmetrics(); h=a+d+8
    im=Image.new("RGBA",(w,h),(0,0,0,0)); dr=ImageDraw.Draw(im)
    if tr:
        x=4
        for c in t:
            dr.text((x,4),c,font=f,fill=fill+(255,)); x+=dr.textlength(c,font=f)+tr
    else: dr.text((4,4),t,font=f,fill=fill+(255,))
    return im

X=106                     # 5.5% margin
# ---------------------------------------------------------------------------
# endcard_build.py — the end card. The DESIGN is series-fixed; the CONTENT is
# per part, so the render belongs in Episodes/<Guest>/, not in Branding/.
#
#   python3 endcard_build.py <Episodes/Guest/card_data.json> <output dir>
#
# card_data.json:
#   { "sources": ["...", "..."], "next": "PART 2 · ..." }
#
# Everything else on the card is series-fixed and lives below: the disclosure
# statement, the personal line, the signature, the mark. Those change for the
# whole series at once or not at all.
#
# Before rendering, run sources_audit.py against the part's kit. The sources
# block is the claim the show makes about itself; it must match the provenance
# tags the script actually leans on.
# ---------------------------------------------------------------------------
import json
DATA=json.load(open(sys.argv[1],encoding="utf-8")) if len(sys.argv)>1 else {}
OUTDIR=sys.argv[2] if len(sys.argv)>2 else "ecfr"

DISCLOSURE=["This programme is an AI-voiced dramatization. The guest is a historical",
            "reconstruction, not a recording. Dialogue is built from documented actions,",
            "primary sources, and academic consensus."]
EP=dict(disclosure=DISCLOSURE,
        sources=DATA.get("sources",["[no sources in card_data.json]"]),
        nxt=DATA.get("next","[no next title in card_data.json]"))
PERSONAL=["For most of my life these conversations only happened in my head.",
          "This is the first time I could build one and show it to someone."]
SIGN="— Salah"
# support lines (2026-09-27, Salah): true as written — no promise about who comes next, no apology for AI flaws
SUPPORT=["This series is independent — subscribing keeps it going.",
         "Who should sit in that chair next? Tell us in the comments."]

# ---- build the stack, top-down, and report the geometry
items=[]   # (layer, x, y, group)
y=146
items.append((layer("AI-GENERATED DRAMATIZATION",kick,WALNUT,6),X,y,0)); y+=48
for ln in EP["disclosure"]:
    items.append((layer(ln,body,BODY),X,y,0)); y+=38
y+=16
items.append((layer("PRIMARY SOURCES",kick,WALNUT,6),X,y,1)); y+=44
for ln in EP["sources"]:
    items.append((layer(ln,src,BODY),X,y,1)); y+=28
y+=24
items.append((layer("NEXT",kick,WALNUT,6),X,y,2)); y+=44
items.append((layer(EP["nxt"],nexttl,INK),X,y,2)); y+=62
y+=18
# a short walnut rule separates the personal note from the NEXT block, so the line
# does not read as a subtitle of the next part's title. Same rule the plates carry.
RULE=Image.new("RGBA",(150,3),WALNUT+(190,))
items.append((RULE,X,y,3)); y+=30
for ln in PERSONAL:
    items.append((layer(ln,pers,QUIET),X,y,3)); y+=31
items.append((layer(SIGN,sig,QUIET),X,y+6,3)); y+=36
y+=12
for ln in SUPPORT:
    items.append((layer(ln,pers,INK),X,y,4)); y+=30
MARK_Y=1012-MH
print("text stack ends at y =",y,"  mark at",MARK_Y,"  mark bottom",MARK_Y+MH)
if y > MARK_Y - 12: sys.exit(f"STOP — the text stack ({y}) runs into the mark ({MARK_Y}); shorten the sources list or the lines")
widest=max(l.width for l,_,_,_ in items)
print("widest line:",widest,"px  right edge at x =",X+widest,f"({(X+widest)/W:.1%} of frame)")
print("right third clear from x =",int(0.65*W))

# ---------------- render ----------------
SOFT=130
def ease(x): return x*x*(3-2*x)
def wipe(l,p):
    if p>=1.0: return l
    w,h=l.size; x=-SOFT+p*(w+SOFT)
    col=np.clip((x-np.arange(w))/SOFT,0,1).astype(np.float32)
    a=np.asarray(l.split()[3],dtype=np.float32)*col[None,:]
    o=l.copy(); o.putalpha(Image.fromarray(a.astype(np.uint8))); return o

FPS=24; DUR=20.0; N=int(FPS*DUR)
# groups set in sequence: disclosure, sources, next, personal — then the mark
GROUP_IN={0:0.35, 1:2.10, 2:3.70, 3:5.10, 4:6.00}
STAGGER=0.11; WIPE=0.55
MARK_IN, MARK_D = 7.00, 0.70

out=OUTDIR; os.makedirs(out,exist_ok=True)
gi={}
for l,x,y,g in items:
    gi.setdefault(g,[]).append(None)
idx={}
for i,(l,x,y,g) in enumerate(items):
    idx[i]=len([1 for j,(_,_,_,g2) in enumerate(items) if j<i and g2==g])

for f in range(N):
    # RESUME=1: skip frames already rendered (a long render can be finished across several short runs; added 2026-09-23)
    if os.environ.get("RESUME") and os.path.exists(f"{out}/f{f:04d}.png"):
        try: Image.open(f"{out}/f{f:04d}.png").load(); continue     # a frame cut off by a timeout is re-rendered
        except Exception: pass
    t=f/FPS
    fr=paper_bg(1.0+0.024*ease(min(1.0,t/DUR))).convert("RGBA")
    lay=Image.new("RGBA",(W,H),(0,0,0,0))
    for i,(l,x,y,g) in enumerate(items):
        t0=GROUP_IN[g]+idx[i]*STAGGER
        if t<t0: continue
        lay.alpha_composite(wipe(l,ease(min(1.0,(t-t0)/WIPE))),(x,y))
    if t>MARK_IN:
        a=ease(min(1,(t-MARK_IN)/MARK_D))
        m=mark.copy(); m.putalpha(mark.split()[3].point(lambda v:int(v*a)))
        lay.alpha_composite(m,(X-4,MARK_Y))
    Image.alpha_composite(fr,lay).convert("RGB").save(f"{out}/f{f:04d}.png")
    if f%60==0: print("frame",f,flush=True)
print("done",N)
