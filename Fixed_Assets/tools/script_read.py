#!/usr/bin/env python3
"""Script read — the kit rendered as a clean read-through for a human review, before any generation.

Usage:  python3 Fixed_Assets/tools/script_read.py Episodes/<Guest> --outline   ← THE read Salah approves (Mode 3)
        python3 Fixed_Assets/tools/script_read.py Episodes/<Guest> [part]      ← quick re-check of a kit (Mode 4)
Writes  Episodes/<Guest>/SCRIPT_READ.md (both parts, from OUTLINE.md) or P<n>_SCRIPT_READ.md (from the kit)

Speakers and lines in order, with the delivery note, the silent beats (reactions, b-roll, off-camera
lines, interruptions), context cards and pull-quotes where they land, act breaks, and an approximate
running clock. It reads the kit only; it changes nothing. Mode 3, "The script review".
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def outline_read(ep):
    """Both parts from OUTLINE.md, before any prompt exists. Running time is an estimate (duration v2)."""
    import math, syl
    src = open(os.path.join(ep, 'OUTLINE.md'), encoding='utf-8').read()
    cast = open(os.path.join(ep, 'CAST.md'), encoding='utf-8').read() if os.path.exists(os.path.join(ep, 'CAST.md')) else ''
    g = re.search(r'^# CAST — (.+)$', cast, re.M); GN = g.group(1).strip() if g else 'Guest'
    r = re.search(r'Duration calibration\*\*\s*\|\s*([\d.]+)\s*syl', cast)
    if r: syl.RATE = float(r.group(1))
    OPEN, CLOSE, BEAT = 19.17 + 5.0, 12.0, 2.0          # BRAND_opening + bumper_in; close ~ wide + credits
    mm = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
    out, totals, part, clock, words, hooks = [], [], 0, 0.0, 0, {}
    def part_text(n):
        m = re.search(r'^## Part %d\b.*?(?=^## Part \d|\Z)' % n, src, re.M | re.S)
        return m.group(0) if m else ''
    open_i = 0
    def close_part():
        if part: out.append(f'\n`{mm(clock + CLOSE)}` **[CLOSE]** wide · end card'); totals.append((part, clock + CLOSE, words))
    for ln in src.split('\n'):
        m = re.match(r'^## Part (\d+)(.*)$', ln)
        if m:
            close_part(); part, clock, words = int(m.group(1)), OPEN, 0
            out += ['', f'# Part {part}{m.group(2)}', '', '`0:00` **[OPENING]** disclosure card · hook · intro']
            open_i = len(out) - 1
            continue
        if not part: continue
        if ln.startswith('### '): out += ['', f'## {ln[4:].strip()}', '']; continue
        m = re.match(r'^HOOK:\s*"(.*?)"', ln)
        if m:
            out[open_i] += f' — hook: *"{m.group(1)}"*'
            if not re.search(r'^GUEST[^:\n]*:\s*"[^"\n]*' + re.escape(m.group(1).rstrip('.')), part_text(part), re.M):
                out.append('> ⚠️ *the hook is not a verbatim sentence from this part\'s guest lines*')
            continue
        m = re.match(r'^QUESTION:\s*(.+)$', ln)
        if m: out.append(f'*The question: {m.group(1).strip()}*'); out.append(''); continue
        m = re.match(r'^(HOST|GUEST)\s*(?:\(([^)]*)\))?\s*:\s*"(.*?)"', ln)
        if m:
            spk = 'HOST' if m.group(1) == 'HOST' else GN.upper(); line = m.group(3)
            out.append(f'`{mm(clock)}` **{spk}**{f" *({m.group(2)})*" if m.group(2) else ""}: {line}')
            clock += syl.dur2(line)[2]; words += len(line.split()); continue
        m = re.match(r'^>\s*(\S+)\s*(.*)$', ln)
        if m:
            tag, rest = m.group(1), m.group(2).strip(' —')
            if tag == 'BEAT': out.append('> *[a held beat]*'); clock += BEAT
            elif tag == 'OFFMIC' or tag.startswith('CUT-IN'):
                q = re.search(r'(HOST|GUEST)[^:]*:\s*"(.*?)"', rest)
                who = ('HOST' if q and q.group(1) == 'HOST' else GN.upper()) if q else ''
                label = 'off camera' if tag == 'OFFMIC' else f'interrupts — {tag.split(":")[1] if ":" in tag else ""}'
                out.append(f'> *({label})* **{who}:** {q.group(2)}' if q else f'> *({label})* {rest}')
                if q: words += len(q.group(2).split())
            elif tag == 'CARD':
                c = [x.strip() for x in rest.split('|')]
                out.append(f'> 📌 **{c[1] if len(c) > 1 else rest}** — {c[2] if len(c) > 2 else ""}')
            elif tag == 'PULL': out.append(f'> ❝ pull-quote: {rest}')
            elif tag == 'BROLL': out.append(f'> *[picture: {rest}]*')
            else: out.append(f'> *[{tag.lower()}{": " + rest if rest else ""}]*')
    close_part()
    head = [f'# {GN} — script read, both parts', '',
            '*Generated from `OUTLINE.md` by `script_read.py --outline`. Read it as a viewer — both parts as one arc. '
            'Mark anything that drags, confuses, or does nothing; check that Part 1\'s ending is what Part 2 pays.*', '']
    head += [f'**Part {p} ≈ {mm(t)}** ({w:,} spoken words)' for p, t, w in totals]
    head += ['', '*Times are estimates from the duration model; reactions and pictures over dialogue add nothing.*']
    open(os.path.join(ep, 'SCRIPT_READ.md'), 'w', encoding='utf-8').write('\n'.join(head + out) + '\n')
    print('SCRIPT_READ.md — ' + ' · '.join(f'Part {p} {mm(t)}, {w} words' for p, t, w in totals))

if '--outline' in sys.argv:
    outline_read(sys.argv[1].rstrip('/')); sys.exit(0)
ep = sys.argv[1]; N = (sys.argv[2] if len(sys.argv) > 2 else '1').lstrip('Pp'); PART = f'P{N}'
kit = open(os.path.join(ep, f'{PART}_kit.md'), encoding='utf-8').read()
cast = open(os.path.join(ep, 'CAST.md'), encoding='utf-8').read() if os.path.exists(os.path.join(ep, 'CAST.md')) else ''
gname = re.search(r'^# CAST — (.+)$', cast, re.M); GNAME = gname.group(1).strip() if gname else 'Guest'; GUEST = GNAME.upper()

cards = {}   # shot -> list of (word, name, gloss)
if '### Context cards' in kit:
    sec = kit[kit.index('### Context cards'):]
    for m in re.finditer(r'^\|\s*\d+\s*\|\s*`(P\d_\d+[a-z]?)`\s*\|\s*(.+?)\s*\|\s*[LR]\s*\|\s*\w+\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', sec, re.M):
        cards.setdefault(m.group(1), []).append((m.group(2), m.group(3), m.group(4)))
quotes = {}
for m in re.finditer(r'^\|\s*"(.+?)"\s*\|\s*`(P\d_\d+[a-z]?)`\s*\|\s*`(P\d_\d+[a-z]?)`', kit, re.M):
    quotes.setdefault(m.group(3), []).append(m.group(1))

body = kit[kit.index('## Shot list'):] if '## Shot list' in kit else kit
parts = re.split(r'\n(?=\*\*' + PART + r'_\d{3}[a-z]?\*\* · |### )', body)
out = []; clock = 0.0; words = 0
def mmss(t): return f'{int(t // 60)}:{int(t % 60):02d}'
for p in parts:
    if p.startswith('### '):
        title = p.split('\n')[0][4:].strip()
        if title.startswith(('Act', 'Cold')): out += ['', f'## {title}', '']
        continue
    m = re.match(r'\*\*(' + PART + r'_\d{3}[a-z]?)\*\* · (\w+)(?: · (HOST|GUEST))?(?: · \*\*([\d.]+)s)?', p)
    if not m: continue
    sid, typ, who, dur = m.group(1), m.group(2), m.group(3), float(m.group(4) or 0)
    ep_ = re.search(r'\*\*edit_placement:\*\*\s*([^\n]*)', p); ep_ = ep_.group(1).strip() if ep_ else ''
    if typ == 'BRAND_OPENING':
        hook = re.search(r'nominated line is[^*]*\*\*[^*]*\*"(.+?)"\*', p)
        out.append(f'`{mmss(clock)}` **[OPENING]** disclosure card · hook: *"{hook.group(1) if hook else "—"}"* · intro')
        clock += dur; continue
    if typ == 'BRAND_ACTBREAK':
        out.append(f'\n`{mmss(clock)}` — *act break* —\n'); clock += dur; continue
    if typ.startswith('BUMPER'):
        out.append(f'\n`{mmss(clock)}` **[CLOSE]** the two of them, turning into a drawing · end card'); continue
    if typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION'):
        a = re.search(r'says(?:, ([^:"\n]*))?: "(.*?)"\n', p, re.S) or re.search(r'(?:The host|The \w+) \(([^)"\n]*)\): "(.*?)"', p, re.S)
        if not a: continue
        note, line = a.group(1), a.group(2)
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import outline_lines as O
        line = (O.kit_spoken(p) or [line])[0]   # a beat map reads as all its segments
        spk = 'HOST' if who == 'HOST' else GUEST
        words += len(line.split())
        if 'audio only, under' in ep_:
            out.append(f'> *(off camera)* **{spk}:** {line}')
            continue
        tag = ' *(to camera)*' if typ == 'NARRATION' else ''
        out.append(f'`{mmss(clock)}` **{spk}**{tag}{f" *({note})*" if note else ""}: {line}')
        if 'interrupted by' in ep_ or 'CUT-IN' in ep_:
            out.append(f'> *interruption — {ep_.split("—")[0].strip("` ")}*')
        for w, name, gloss in cards.get(sid, []):
            out.append(f'> 📌 **{name}** — {gloss}')
        clock += dur
    elif typ == 'REACTION':
        who_ = 'Host' if who == 'HOST' else GNAME
        desc = re.search(r'```\n.*?\n\n\s*(.*?)\n', p, re.S)
        d = desc.group(1).split('.')[0] if desc else 'listens'
        out.append(f'> *[{who_}, silent — {d.strip()}]*')
        if ep_.startswith('plays between'): clock += dur
    elif typ == 'BROLL_GEN':
        g = re.search(r'^> (.+)$', p, re.M)
        if g: pic = g.group(1).strip()
        else:
            blk = re.search(r'```\n(.*?)\n```', p, re.S)
            paras = [x.strip() for x in blk.group(1).split('\n\n')] if blk else []
            pic = paras[1].split('.')[0] if len(paras) > 1 else 'b-roll'
        out.append(f'> *[picture: {pic}]*')
    for q in quotes.get(sid, []):
        out.append(f'> ❝ pull-quote: *"{q}"*')
head = [f'# {GNAME} — Part {N} · script read', '',
        f'*Generated from `{PART}_kit.md` by `script_read.py`. Read it as a viewer. Mark anything that drags, confuses, or does nothing.*', '',
        f'**Running time ≈ {mmss(clock)}** (opening, talking and held beats; reactions and pictures over dialogue add nothing) · **{words:,} spoken words**', '']
open(os.path.join(ep, f'{PART}_SCRIPT_READ.md'), 'w', encoding='utf-8').write('\n'.join(head + out) + '\n')
print(f'{PART}_SCRIPT_READ.md — {mmss(clock)}, {words} words')
