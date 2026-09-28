# -*- coding: utf-8 -*-
import re,sys,os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from broll2 import ROWS, SKETCH, PERSIST
p=os.path.join(os.path.dirname(HERE),"P1_kit.md")
s=open(p,encoding="utf-8").read()
done=[]
for sid,(subj,move,motion,audio,note) in ROWS.items():
    pat=re.compile(r'(^\*\*'+sid+r'\*\* · BROLL_GEN[^\n]*\n)(.*?)(?=^\*\*P1_\d+\*\* · |\Z)', re.M|re.S)
    m=pat.search(s)
    assert m, "no match "+sid
    hdr=m.group(1); body=m.group(2)
    pm=re.search(r'^\*\*edit_placement:\*\* (.+)$', body, re.M)
    sm=re.search(r'^\*\*SFX:\*\* (.+)$', body, re.M)
    hdr=re.sub(r' · @\w+', '', hdr).rstrip("\n")
    hdr=hdr.rstrip()+" + 3 cr still\n" if "+ 3 cr still" not in hdr else hdr+"\n"
    new=(hdr+"\n"
      "**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):\n\n```\n"+SKETCH+"\n\n"+subj+
      "\n\nWide still image, nothing in motion. Composition balanced and simple.\n```\n\n"
      "**STEP 2 — video**, image-to-video from that still:\n\n```\n"+move+"\n\n"+PERSIST+"\n\n"+motion+"\n\n"+audio+"\n```\n\n")
    if pm: new+="**edit_placement:** "+pm.group(1)+"\n"
    if sm: new+="**SFX:** "+sm.group(1)+"\n"
    new+="\n**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.\n"
    if note: new+="\n"+note+"\n"
    new+="\n"
    s=s[:m.start()]+new+s[m.end():]
    done.append(sid)
open(p,"w",encoding="utf-8").write(s)
print("converted:",len(done),done)
