from PIL import Image, ImageDraw, ImageFont
import numpy as np, os
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080; FPS=24; DUR=4.0; N=int(FPS*DUR)
INK=(18,22,28); WALNUT=(140,88,48)
F=lambda n,s: ImageFont.truetype(f"{B}/fonts/{n}",s)
kick=F("Oswald-SemiBold.ttf",24); body=F("LibreBaskerville-Regular.ttf",30)

plate=Image.open(f"{B}/BRAND_lowerthird_plate_L.png").convert("RGBA")
PW=806; PH=int(plate.height*PW/plate.width)          # 1612x270 @3840 -> 806x135 @1920
plate=plate.resize((PW,PH),Image.LANCZOS)
PX=0                                                  # outer edge flush to frame edge
PY=int(0.90*H)-PH                                     # bottom edge at 90% of frame height
TX=int(1446/1612*PW)                                  # text right-aligns to this x inside the plate

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

L1=layer("SUBSCRIBE",kick,WALNUT,6)
L2=layer("One conversation at a time.",body,INK)
# right-aligned to TX, inside the plate
ITEMS=[(L1,PX+TX-L1.width,PY+int(0.15*PH)),
       (L2,PX+TX-L2.width,PY+int(0.50*PH))]
print("plate",PW,PH,"at",PX,PY,"| text right edge x =",PX+TX)
for l,x,y in ITEMS: print("   line w",l.width,"x",x,"y",y)

SOFT=90
def ease(x): return x*x*(3-2*x)
def wipe(l,p):
    if p>=1.0: return l
    w,h=l.size; x=-SOFT+p*(w+SOFT)
    col=np.clip((x-np.arange(w))/SOFT,0,1).astype(np.float32)
    a=np.asarray(l.split()[3],dtype=np.float32)*col[None,:]
    o=l.copy(); o.putalpha(Image.fromarray(a.astype(np.uint8))); return o
def fade(im,a):
    if a>=1.0: return im
    o=im.copy(); o.putalpha(im.split()[3].point(lambda v:int(v*a))); return o

IN_D=0.45; OUT_ST=3.55; OUT_D=0.40
T_IN=[(0.30,0.45),(0.55,0.55)]
out="subfr"; os.makedirs(out,exist_ok=True)
for f in range(N):
    t=f/FPS
    fr=Image.new("RGBA",(W,H),(0,0,0,0))
    a_in=ease(min(1.0,t/IN_D))
    a_out=1.0-ease(min(1.0,max(0.0,(t-OUT_ST)/OUT_D)))
    a=a_in*a_out
    if a>0.003:
        dx=int(-18*(1.0-a_in))                        # settles in from the frame edge
        fr.alpha_composite(fade(plate,a),(PX+dx,PY))
        for (l,x,y),(t0,d) in zip(ITEMS,T_IN):
            if t<t0: continue
            fr.alpha_composite(fade(wipe(l,ease(min(1.0,(t-t0)/d))),a),(x+dx,y))
    fr.save(f"{out}/f{f:03d}.png")
print("subscribe frames:",N)
