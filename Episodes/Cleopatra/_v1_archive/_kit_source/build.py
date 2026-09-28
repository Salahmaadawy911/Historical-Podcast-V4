# -*- coding: utf-8 -*-
"""Rebuild P1_kit.md from parsed.json + tags.py + newshots.py + broll.py.
The kit markdown is the source of truth; this script is the transformer.
Run from Episodes/Cleopatra/:  python3 _kit_source/build.py
"""
import json, re, sys, os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from tags import TAGS
import newshots as NS
from broll import CONVERT

d=json.load(open(os.path.join(HERE,"parsed.json")))
blocks=d["blocks"]

# ---------- 1. build the renumber map -------------------------------------
order=[]
for b in blocks:
    if b["kind"]=="shot":
        order.append(b["id"])
        if b["id"]==NS.NEW_WIDE["after"]: order.append("NEW_WIDE")
        if b["id"]==NS.NEW_HANDOFF["after"]: order.append("NEW_HANDOFF")
NEW={old:"P1_%03d"%(i+1) for i,old in enumerate(order)}

def renum(text):
    return re.sub(r'P1_(\d{3})', lambda m: NEW.get(m.group(0), m.group(0)), text)

# ---------- 2. model + credits --------------------------------------------
def model_for(header):
    t=header.split(" · ")[0].strip()
    if t in ("REACTION","WIDE_SILENT"):  return ("Kling 3.0 Standard, audio OFF", 8)
    if t in ("INTERVIEW","NARRATION","INTERJECTION","BROLL_GEN","WIDE_CREDITS"): return ("Kling 3.0 Turbo, audio on", 10)
    return (None,0)

def dur_of(header):
    m=re.search(r'\*\*(\d+)s\*\*', header)
    return int(m.group(1)) if m else 0

# ---------- 3. emit --------------------------------------------------------
TAGNAME={"D":"Documented","I":"Inferred","V":"Voice"}
out=[]; total_cr=0; total_s=0; still_cr=0
counts={}

def emit_shot(new_id, header, meta, prompt, subtitle, sfx, placement, note, tagkey, extra_tbl=None):
    global total_cr,total_s,still_cr
    mdl,rate=model_for(header)
    dur=dur_of(header)
    line=f"**{new_id}** · {header}"
    if mdl:
        cr=dur*rate; total_cr+=cr; total_s+=dur
        line+=f" · {mdl} · {rate} cr/s · **{cr} cr**"
    out.append(line); out.append("")
    if meta: out.append(renum(meta)); out.append("")
    if prompt:
        out.append("```"); out.append(prompt); out.append("```"); out.append("")
    if extra_tbl: out.append(extra_tbl); out.append("")
    if placement: out.append(f"**edit_placement:** {renum(placement)}")
    if subtitle is not None: out.append(f"**Subtitle:** {subtitle}")
    if tagkey and tagkey in TAGS:
        t,basis=TAGS[tagkey]
        counts[t]=counts.get(t,0)+1
        out.append(f"**provenance:** `[{t}]` {TAGNAME[t]}" + (f" — {basis}" if basis else ""))
    if sfx: out.append(f"**SFX:** {sfx}")
    if note: out.append(""); out.append(renum(note))
    out.append("")

def new_block(spec, tagkey=None):
    emit_shot(NEW[spec.get("_key")], spec["header"], spec["meta"], spec["prompt"],
              spec.get("subtitle"), spec.get("sfx"), spec.get("placement"), spec.get("note"), tagkey)

for b in blocks:
    if b["kind"]=="act":
        out.append(f"### {b['title']}"); out.append(""); continue
    if b["kind"]=="raw":
        if b["text"].strip(): out.append(renum(b["text"]))
        continue
    oid=b["id"]; body="\n".join(b["body"])

    if oid in CONVERT:                      # former Pexels row -> charcoal b-roll
        c=CONVERT[oid]
        still_cr+=3
        pm=re.search(r'^\*\*edit_placement:\*\* (.+)$', body, re.M)
        sm=re.search(r'^\*\*SFX:\*\* (.+)$', body, re.M)
        sfx=sm.group(1) if sm else ""
        sfx=re.sub(r'clip is SILENT', 'generated clip carries only its own ambience', sfx)
        hdr=f"BROLL_GEN · **{c['dur']}s**"
        prompt="**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):\n\n```\n"+c["still"]+"\n```\n\n**STEP 2 — video**, image-to-video from that still:\n\n```\n"+c["video"]+"\n```"
        mdl,rate=model_for(hdr); cr=c['dur']*rate; total_cr+=cr; total_s+=c['dur']
        out.append(f"**{NEW[oid]}** · {hdr} · {mdl} · {rate} cr/s · **{cr} cr** + 3 cr still")
        out.append(""); out.append(f"> {c['desc']}"); out.append("")
        out.append(prompt); out.append("")
        if pm: out.append(f"**edit_placement:** {renum(pm.group(1))}")
        out.append(f"**SFX:** {sfx}")
        out.append("")
        out.append("**changed:** was a Pexels row. The stock tier is gone — see `skill_mode4_produce.md` §10. Two steps because "
                   "the charcoal style is the thing that must not drift, and a start frame is what holds it; 3 credits is cheap insurance.")
        out.append("")
        continue

    if oid in NS.REWRITE:                   # rewritten rows
        r=NS.REWRITE[oid]
        pm=re.search(r'^\*\*edit_placement:\*\* (.+)$', body, re.M)
        placement=r.get("placement") or (pm.group(1) if pm else None)
        emit_shot(NEW[oid], r["header"], r["meta"], r["prompt"], r["subtitle"], r["sfx"], placement, r["note"], oid)
    else:                                   # untouched row
        hdr=b["header"]
        mdl,rate=model_for(hdr); dur=dur_of(hdr)
        line=f"**{NEW[oid]}** · {hdr}"
        if mdl:
            cr=dur*rate; total_cr+=cr; total_s+=dur
            line+=f" · {mdl} · {rate} cr/s · **{cr} cr**"
        out.append(line)
        newbody=renum(body).rstrip()
        if oid in TAGS:
            t,basis=TAGS[oid]; counts[t]=counts.get(t,0)+1
            prov=f"**provenance:** `[{t}]` {TAGNAME[t]}" + (f" — {basis}" if basis else "")
            if re.search(r'^\*\*Subtitle:\*\*', newbody, re.M):
                newbody=re.sub(r'^(\*\*Subtitle:\*\* .+)$', lambda m: m.group(1)+"\n"+prov, newbody, count=1, flags=re.M)
            else:
                newbody+="\n"+prov
        out.append(newbody); out.append("")

    if oid==NS.NEW_WIDE["after"]:
        s=dict(NS.NEW_WIDE); s["_key"]="NEW_WIDE"; new_block(s)
    if oid==NS.NEW_HANDOFF["after"]:
        s=dict(NS.NEW_HANDOFF); s["_key"]="NEW_HANDOFF"
        TAGS["NEW_HANDOFF"]=NS.NEW_HANDOFF["tag"]; new_block(s, "NEW_HANDOFF")

body_md="\n".join(out)
json.dump({"map":NEW,"total_cr":total_cr,"total_s":total_s,"still_cr":still_cr,"counts":counts},
          open(os.path.join(HERE,"build_stats.json"),"w"), indent=1)
open(os.path.join(HERE,"shotlist.md"),"w",encoding="utf-8").write(body_md)
print(f"shots: {len(NEW)}  video: {total_s}s  {total_cr} cr  + stills {still_cr} cr")
print("provenance:",counts)
