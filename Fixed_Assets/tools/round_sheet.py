#!/usr/bin/env python3
"""Generation sheet for one pass — every prompt to paste, grouped by platform setting, in kit order.

Usage:  python3 Fixed_Assets/tools/round_sheet.py Episodes/<Guest> <1|2> [--part N] [--skip P1_008,P1_057] [--hold frame_x,frame_y]
        --hold: seed frames waiting to be regenerated — their rows are listed as HELD at the top, not to generate yet.
        --part: which part's kit (default 1). The round number is the pass (1 = seed frames, 2 = chained).
Pass 1 = every row that starts from a seed frame (chain SOURCES included); Pass 2 = the chained rows.
Clips already in shots/ are skipped automatically. Writes Episodes/<Guest>/ROUND<n>_prompts.md.
"""
import re, sys, os
ep, n = sys.argv[1], sys.argv[2]
hold = set(sys.argv[sys.argv.index('--hold') + 1].split(',')) if '--hold' in sys.argv else set()
skip = set(sys.argv[sys.argv.index('--skip') + 1].split(',')) if '--skip' in sys.argv else set()
PART = 'P' + (sys.argv[sys.argv.index('--part') + 1].lstrip('Pp') if '--part' in sys.argv else '1')
kit = open(os.path.join(ep, f'{PART}_kit.md'), encoding='utf-8').read()
have = {f[:-4] for f in os.listdir(os.path.join(ep, 'shots')) if f.endswith('.mp4')}
rows = []; held = []; chain = []
for r in re.split(r'\n(?=\*\*' + PART + r'_\d{3}[a-z]?\*\* · )', kit):
    m = re.match(r'\*\*(' + PART + r'_\d{3}[a-z]?)\*\* · (\w+)(?: · (HOST|GUEST))? · \*\*([\d.]+)s\*\*', r)
    if not m: continue
    sid, typ, who, dur = m.groups()
    if typ.startswith('BRAND') or typ.startswith('BUMPER') or sid in skip: continue
    if 'audio only, under' in r and typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION'): pass   # still generated
    sf = re.search(r'`start_frame` ([^\n]*)', r)
    chained = bool(sf and 'chain from' in sf.group(1))
    if n == '2' and not chained: continue   # pass 2 = chained only; pass 1 now carries the chained rows too (2026-09-26)
    if sid in have: continue
    blocks = re.findall(r'```\n(.*?)\n```', r, re.S)
    # Kling strips newlines: every paragraph after the first starts with a space so the join survives the paste
    # (the old leading-space rule dropped with structure v3, L51 — the tested layout has no leading spaces)
    st_ = sf.group(1).split(' · ')[0].strip() if sf else ''
    ef = re.search(r'`end_frame` (`[^`]+`)', r)   # end-frame rule (Mode 4 §7, 2026-09-24): Standard's end-frame slot
    if ef: st_ += f' · **END FRAME {ef.group(1)}** (same seed)'
    if any(f'`{h}`' in st_ for h in hold): held.append((sid, st_)); continue
    if n == '1' and chained: chain.append((sid, typ, who or '', dur, st_, blocks, r)); continue
    rows.append((sid, typ, who or '', dur, st_, blocks, r))
talk_all = [x for x in rows if x[1] in ('INTERVIEW', 'INTERJECTION', 'NARRATION')]
talk = [x for x in talk_all if '720p' not in x[6].split('\n')[0]]   # all made on the website (L32, 2026-09-26)
web = []

talk720 = [x for x in talk_all if '720p' in x[6].split('\n')[0]]   # audio-only clips (Mode 4 §1, 2026-09-24)
react = [x for x in rows if x[1] == 'REACTION']
broll = [x for x in rows if x[1] == 'BROLL_GEN']
out = [f'# Round {n} — generation sheet', '',
       f'Generated from `{PART}_kit.md` by `round_sheet.py`. **{len(rows) + len(chain)} clips.** Made through the Kling CLI in waves (`cli_wave.py`, L52) or by hand on kling.ai as the fallback — same blocks, same settings. **Each kept take lives at `Shots/<id>.mp4`** (a retake replaces the file). No Claude check per take — the full check runs once at the start of the edit (Mode 6).',
       'Every studio clip: 1080p, **camera chip OFF** — the prompt’s own camera + lighting paragraphs hold the frame (L51). Paste each block whole.', '']
if held:
    out += [f'> ⛔ **HELD — {len(held)} clips wait for a regenerated seed frame** ({", ".join(sorted(hold))}); they are not on this sheet. Regenerate the frame (same file name), then rebuild the sheet: ' + ', '.join(f'`{a}`' for a, _ in held), '']
if n == '2':
    out += ['**Pass 2:** start each clip from the listed source clip\'s **last frame, using Kling\'s own last-frame feature**.', '']
def sec(title, setting, lst):
    if not lst: return
    out.extend([f'## {title} — {len(lst)} clips', f'**{setting}**', ''])
    for sid, typ, who, dur, sf, blocks, r in lst:
        out.append(f'### {sid} · {typ} {who} · {dur}s · start: {sf}')
        out.extend(['```', blocks[0], '```', ''])
# ONE list in kit order, every chained clip placed directly after its source (Salah, 2026-09-26) — each entry
# carries its own settings, so the sheet reads top to bottom on kling.ai.
def setting(x):
    typ, head = x[1], x[6].split('\n')[0]
    if typ == 'REACTION': return 'Kling 3.0 Standard · audio OFF · 8 cr/s · chip OFF'
    if '720p' in head: return 'Kling 3.0 Turbo **720p** · audio ON · 8 cr/s · voice only (picture unused)'
    if 'Kling 3.0 Standard, audio ON' in head: return '**Kling 3.0 Standard · audio ON** · 12 cr/s · chip OFF'
    return 'Kling 3.0 Turbo · audio ON · 10 cr/s · chip OFF'
studio = sorted(talk + talk720 + react + chain, key=lambda x: x[0])
by_src = {}
for x in chain:
    src = (re.search(r'chain from (P\d_\d{3}[a-z]?)', x[4]) or [None, ''])[1]; by_src.setdefault(src, []).append(x)
on_sheet = {x[0] for x in studio}
def root_seed(i, depth=0):
    row = next((x for x in rows + chain if x[0] == i), None)
    k = re.search(r'`start_frame` `(frame_[a-z_]+)`', kit.split(f'**{i}**', 1)[1].split('\n**P', 1)[0]) if f'**{i}**' in kit else None
    if k: return k.group(1)
    c = re.search(r'chain from `?(P\d_\d{3}[a-z]?)', kit.split(f'**{i}**', 1)[1].split('\n**P', 1)[0]) if f'**{i}**' in kit else None
    return root_seed(c.group(1), depth + 1) if c and depth < 6 else None
order, seen = [], set()
def emit(x):
    if x[0] in seen: return
    seen.add(x[0]); order.append(x)
    for c in sorted(by_src.get(x[0], []), key=lambda y: y[0]): emit(c)
for x in studio:
    src = (re.search(r'chain from (P\d_\d{3}[a-z]?)', x[4]) or [None, ''])[1]
    if src and src in on_sheet: continue          # placed right after its source
    emit(x)
out.extend([f'## Studio clips — {len(order)}, in order', 'Top to bottom. A clip marked **↳ chained** starts from the LAST frame of the clip just above it (Kling\'s own last-frame feature) — make it right after that one is saved.', ''])
for x in order:
    sid, typ, who, dur, sf, blocks, r = x
    src = (re.search(r'chain from (P\d_\d{3}[a-z]?)', sf) or [None, ''])[1]
    if src:
        start = f'**↳ chained** — start: last frame of `{src}`' + ('' if src in on_sheet else ' (already in Shots/)')
        efm = re.search(r'`end_frame` `([^`]+)`', r)
        if efm: start += f' · **END FRAME `{efm.group(1)}`**'
        elif typ == 'REACTION':                  # L45: end on the source clip's seed, not on its (mid-speech) last frame
            start += ' · **END FRAME = the same extracted frame** (put it in both slots — L44; L45 withdrawn)'
    else:
        start = f'start: {sf}'
    out.append(f'### {sid} · {typ} {who} · {dur}s · {setting(x)} · {start}')
    out.extend(['```', blocks[0], '```', ''])
if broll:
    out.extend([f'## B-roll step 1 — stills, {len(broll)} images', '**Kling Image 3.0, 2K, 16:9** (text-to-image, no reference image) — as tested; via `kling_broll.mjs … stills` or on kling.ai. Save each as `shots/stills/<id>.png`.', ''])
    for sid, typ, who, dur, sf, blocks, r in broll:
        out.extend([f'### {sid} · still', '```', blocks[0], '```', ''])
    out.extend([f'## B-roll step 2 — video, {len(broll)} clips', '**Kling 3.0 Turbo, audio ON · 10 cr/s**, image-to-video from the matching still. **No** stationary preset — b-roll moves.', ''])
    for sid, typ, who, dur, sf, blocks, r in broll:
        out.extend([f'### {sid} · {dur}s · from `shots/stills/{sid}.png`', '```', blocks[1] if len(blocks) > 1 else '', '```', ''])
cr = sum(float(x[3]) * (8 if (x[1] == 'REACTION' or '720p' in x[6].split('\n')[0]) else 12 if 'Kling 3.0 Standard, audio ON' in x[6].split('\n')[0] else 10) for x in rows + chain) + 3 * len(broll)
out.insert(3, f'Estimated **{int(cr):,} credits** before retakes.')
# L59 (2026-09-28): the outro (BUMPER_OUT) was never on the sheet, so it was missed until the edit. It is listed here, in
# full, whenever its clip is not yet in Shots/.
for _b in re.finditer(r'(^\*\*(' + PART + r'_\d{3}[a-z]?)\*\* · BUMPER_OUT[\s\S]*?)(?=^\*\*' + PART + r'_\d{3}|^## |\Z)', kit, re.M):
    if not os.path.exists(os.path.join(ep, 'Shots', _b.group(2) + '.mp4')):
        out.extend(['## The outro — ' + _b.group(2) + ' (made per part, in steps)', '', _b.group(1).strip(), ''])
open(os.path.join(ep, (f'{PART}_' if PART != 'P1' else '') + f'ROUND{n}_prompts.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'ROUND{n}_prompts.md: {len(order)} studio clips in order ({len(chain)} chained under their source) + {len(broll)} b-roll — ~{int(cr):,} cr'); print or None  #  + {len(talk720)} audio-only 720p, {len(react)} reactions, {len(broll)} b-roll — ~{int(cr):,} cr')
