from PIL import Image, ImageDraw
import numpy as np, os, math
import os as _os; B = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # Fixed_Assets/Branding — relative, so it runs on the Mac and in the cloud alike (was a hard-coded cloud path until 2026-09-23)
W,H=1920,1080
INK=(18,22,28); SAND=(224,176,113); FPS=24; DUR=11.166667; N=int(FPS*DUR)
SKETCH_END=6.166667                # the mark section starts here

PAPER=Image.open(f"{B}/paper_source.png").convert("RGB")
PAPER=PAPER.resize((2560,int(PAPER.height*2560/PAPER.width)),Image.LANCZOS)
def paper_bg(w,h,zoom=1.0):
    pw,ph=PAPER.size; th=int(pw*h/w)
    im=PAPER.crop((0,(ph-th)//2,pw,(ph-th)//2+th))
    if zoom!=1.0:
        nw,nh=int(im.width/zoom),int(im.height/zoom)
        x=(im.width-nw)//2; y=(im.height-nh)//2
        im=im.crop((x,y,x+nw,y+nh))
    return im.resize((w,h),Image.LANCZOS)

sym=Image.open(f"{B}/brand_symbol_720.png").convert("RGBA"); SA=sym.split()[3]
stack=Image.open(f"{B}/brand_mark_stack_900.png").convert("RGBA"); STA=stack.split()[3]
a=np.asarray(STA); rows=(a>40).sum(1); nz=np.nonzero(rows)[0]
y=nz.min()
while y<=nz.max() and rows[y]>0: y+=1
sym_top,sym_bot=nz.min(),y-1
cols=(a[sym_top:sym_bot+1]>40).sum(0); cnz=np.nonzero(cols)[0]

def tint(alpha_img,col,op=1.0,size=None):
    im=Image.new("RGBA",alpha_img.size,col+(0,))
    im.putalpha(alpha_img.point(lambda v:int(v*op)))
    return im.resize(size,Image.LANCZOS) if size else im

S=6.0
TOP=[(44,34),(76,34),(60,63)]; BOT=[(44,92),(76,92),(60,63)]
def sand_layer(size_px,t,reverse=False):
    L=Image.new("L",(720,1036),0); d=ImageDraw.Draw(L)
    def sc(p): return (p[0]*S,p[1]*S)
    tp=[sc(p) for p in TOP]; bp=[sc(p) for p in BOT]
    span=bp[2][1]-tp[0][1]
    surf=bp[2][1]-span*math.sqrt(max(0.0,1.0-t))
    if t<0.999:
        d.polygon([tp[0],tp[1],tp[2]],fill=255)
        d.rectangle([0,0,720,surf],fill=0)
    if reverse: lvl=bp[2][1]+(bp[0][1]-bp[2][1])*math.sqrt(max(0.0,t))
    else:       lvl=bp[2][1]+(bp[0][1]-bp[2][1])*math.sqrt(max(0.0,1.0-t))
    if t>0.001:
        b=Image.new("L",(720,1036),0); db=ImageDraw.Draw(b)
        db.polygon([bp[0],bp[1],bp[2]],fill=255)
        if reverse: db.rectangle([0,lvl,720,1036],fill=0)
        else:       db.rectangle([0,0,720,lvl],fill=0)
        L=Image.fromarray(np.maximum(np.asarray(L),np.asarray(b)))
    if (not reverse) and 0.02<t<0.98:
        ImageDraw.Draw(L).rectangle([360-3,bp[2][1]-2,360+3,lvl],fill=255)
    return L.resize(size_px,Image.LANCZOS)

BIG_H=int(H*0.45); big_cx,big_cy=W//2,int(H*0.47)
stack_h=int(H*0.62); stack_w=int(stack.width*stack_h/stack.height)
stack_x,stack_y=(W-stack_w)//2,int(H*0.50-stack_h*0.5)
ss=stack_h/stack.height; ink_h=911.0; pad_ratio=sym.height/ink_h
tgt_h=(sym_bot-sym_top+1)*ss*pad_ratio
tgt_cx=stack_x+(cnz.min()+cnz.max())/2*ss
tgt_cy=stack_y+(sym_top+sym_bot)/2*ss
def ease(x): return x*x*(3-2*x)

# ---- the studies -------------------------------------------------------------
# Each clip's OWN first frame is the blank page, so ink = how much darker a frame
# got than that. Self-referential, so no tone-matching against paper_source is
# needed and any drift in the generated paper cancels out. The -3 floor discards
# the ~2.4 levels of residual camera drift measured on bare paper.
# Each study is shown FULL FRAME and alone, then dissolves as the next begins.
# Scaled-down studies sharing the page read as incidental; full frame they read as
# the drawing someone is actually making. The dissolve replaces a reverse/erase pass:
# erasing is the same information played backwards and costs as long as drawing did.
# draw_in, hold_until, gone_by  (seconds)
STUDIES=[("hills",   0.00, 1.90, 2.20),
         ("doorway", 1.85, 3.75, 4.05),
         ("hand",    3.70, 5.60, 6.05)]
TRIM=1.30; CLIP_FPS=24; CLIP_N=73; BUILD=1.74      # usable build after the blank lead-in
base={n:np.asarray(Image.open(f"ink/{n}/f000.png"),dtype=np.int16) for n,*_ in STUDIES}

def study_ink(name,local_t):
    k=min(int(round((TRIM+min(local_t,BUILD))*CLIP_FPS)),CLIP_N-1)
    if k<0: return None
    fr=np.asarray(Image.open(f"ink/{name}/f{k:03d}.png"),dtype=np.int16)
    ink=np.clip(base[name]-fr-3,0,255).astype(np.uint8)
    return None if ink.max()==0 else ink.astype(np.float32)

os.makedirs("fr10",exist_ok=True)
for i in range(N):
    t=i/FPS
    zoom=1.0+0.030*((t+8.0)/19.166667)   # continuous across card+hook+bumper
    fr=paper_bg(W,H,zoom)

    if t < SKETCH_END:
        ink=np.zeros((H,W),dtype=np.float32)
        for name,t0,hold,gone in STUDIES:
            if t<t0 or t>=gone: continue
            p=study_ink(name,t-t0)
            if p is None: continue
            a=1.0 if t<hold else 1.0-ease((t-hold)/(gone-hold))
            ink=np.maximum(ink,p*a)
        if ink.max()>0:
            arr=np.asarray(fr,dtype=np.float32)-ink[:,:,None]
            fr=Image.fromarray(np.clip(arr,0,255).astype(np.uint8))
        fr.save(f"fr10/f{i:03d}.png"); continue

    # ---- the mark section, t2 = 0..5 ----
    t2=t-SKETCH_END
    rev=False
    if   t2<0.35: s=0.0; op=ease(min(1,t2/0.35))
    elif t2<2.00: s=ease((t2-0.35)/1.65); op=1.0
    elif t2<2.35: s=1.0; op=1.0
    elif t2<3.10: s=1.0-ease((t2-2.35)/0.75); op=1.0; rev=True
    else:         s=0.0; op=1.0
    if t2<3.20: h=BIG_H; cx,cy=big_cx,big_cy
    else:
        k=ease(min(1,(t2-3.20)/0.95))
        h=BIG_H+(tgt_h-BIG_H)*k
        cx=big_cx+(tgt_cx-big_cx)*k; cy=big_cy+(tgt_cy-big_cy)*k
    w=int(sym.width*h/sym.height); h=int(h)
    body=tint(SA,INK,op,(w,h)); sand=tint(sand_layer((w,h),s,rev),SAND,op)
    fr.paste(body,(int(cx-w/2),int(cy-h/2)),body)
    fr.paste(sand,(int(cx-w/2),int(cy-h/2)),sand)
    if t2>3.70:
        k=ease(min(1,(t2-3.70)/0.60))
        st=tint(STA,INK,k,(stack_w,stack_h))
        m=Image.new("L",(stack_w,stack_h),255)
        ImageDraw.Draw(m).rectangle([0,0,stack_w,int((sym_bot+22)*ss)],fill=0)
        st.putalpha(Image.fromarray((np.asarray(st.split()[3])*(np.asarray(m)/255)).astype(np.uint8)))
        fr.paste(st,(stack_x,stack_y),st)
    fr.save(f"fr10/f{i:03d}.png")
print("frames:",N)
