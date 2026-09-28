from PIL import Image, ImageDraw, ImageFont
import numpy as np, os
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080; FPS=24; TOTAL=19.166667     # whole opening, for a continuous zoom
INK=(18,22,28); WALNUT=(70,60,56); QUIET=(90,80,73)
PAPER=Image.open(f"{B}/paper_source.png").convert("RGB")
PAPER=PAPER.resize((2560,int(PAPER.height*2560/PAPER.width)),Image.LANCZOS)
def paper_bg(zoom):
    pw,ph=PAPER.size; th=int(pw*H/W)
    im=PAPER.crop((0,(ph-th)//2,pw,(ph-th)//2+th))
    nw,nh=int(im.width/zoom),int(im.height/zoom)
    im=im.crop(((im.width-nw)//2,(im.height-nh)//2,(im.width-nw)//2+nw,(im.height-nh)//2+nh))
    return im.resize((W,H),Image.LANCZOS)
def ease(x): return x*x*(3-2*x)

kick=ImageFont.truetype(f"{B}/fonts/Oswald-SemiBold.ttf",38)
body=ImageFont.truetype(f"{B}/fonts/LibreBaskerville-Regular.ttf",56)
quiet=ImageFont.truetype(f"{B}/fonts/LibreBaskerville-Italic.ttf",29)
mark=Image.open(f"{B}/brand_mark_trimmed.png").convert("RGBA")
mh=42; mw=int(mark.width*mh/mark.height); mark=mark.resize((mw,mh),Image.LANCZOS)
ma=mark.split()[3]
scratch=Image.new("RGBA",(10,10)); sd=ImageDraw.Draw(scratch)

def tracked_width(txt,font,track):
    return sum(sd.textlength(c,font=font)+track for c in txt)-track

# Text is SET, not faded: each line wipes in left to right behind a soft edge, the way
# a line of type appears when it is being printed. A plain fade reads as a slide
# transition; a wipe reads as something being made, which is the whole page's idea.
SOFT=110
def wipe(layer,prog):
    if prog>=1.0: return layer
    w,h=layer.size
    x=-SOFT+prog*(w+SOFT)
    col=np.clip((x-np.arange(w))/SOFT,0,1).astype(np.float32)
    a=np.asarray(layer.split()[3],dtype=np.float32)*col[None,:]
    out=layer.copy(); out.putalpha(Image.fromarray(a.astype(np.uint8))); return out

def line_layer(txt,font,fill,track=0):
    w=int(tracked_width(txt,font,track))+8
    asc,desc=font.getmetrics(); h=asc+desc+8
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    if track:
        x=4
        for c in txt:
            d.text((x,4),c,font=font,fill=fill+(255,)); x+=d.textlength(c,font=font)+track
    else:
        d.text((4,4),txt,font=font,fill=fill+(255,))
    return im

L1=line_layer("AI-GENERATED DRAMATIZATION",kick,WALNUT,7)
L2=line_layer("Historical reconstruction, not a recording.",body,INK)
L3=line_layer("A conversation I wanted to hear.",quiet,QUIET)
POS=[(L1,468),(L2,530),(L3,878)]
# in-point, wipe duration
TIMING=[(0.05,0.65),(0.50,0.85),(1.45,0.60)]
MARK_IN,MARK_D=1.70,0.50
OUT_ST,OUT_D=3.55,0.45

os.makedirs("cardfr",exist_ok=True)
N=96
for i in range(N):
    t=i/FPS
    fr=paper_bg(1.0+0.030*(t/TOTAL)).convert("RGBA")
    fade=1.0-ease(min(1,max(0,(t-OUT_ST)/OUT_D)))
    if fade>0.003:
        lay=Image.new("RGBA",(W,H),(0,0,0,0))
        for (im,y),(t0,dur) in zip(POS,TIMING):
            if t<t0: continue
            p=ease(min(1.0,(t-t0)/dur))
            w2=wipe(im,p)
            if fade<1.0:
                a=np.asarray(w2.split()[3],dtype=np.float32)*fade
                w2=w2.copy(); w2.putalpha(Image.fromarray(a.astype(np.uint8)))
            lay.alpha_composite(w2,(int((W-im.width)/2),y))
        if t>MARK_IN:
            ma_a=ease(min(1,(t-MARK_IN)/MARK_D))*0.85*fade
            m=mark.copy(); m.putalpha(ma.point(lambda v:int(v*ma_a)))
            lay.alpha_composite(m,(int((W-mw)/2),958))
        fr=Image.alpha_composite(fr,lay)
    fr.convert("RGB").save(f"cardfr/f{i:03d}.png")
print("card frames:",N)
