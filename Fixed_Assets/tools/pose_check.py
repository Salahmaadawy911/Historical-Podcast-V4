"""Pose gate — every prompt is written from its seed frame's entry in the pose table.

  python3 Fixed_Assets/tools/pose_check.py Episodes/<Guest>/P<n>_kit.md     # must print nothing but the last line

Checks, per row:
  - a seed start frame has an entry in the pose table (Fixed_Assets/tools/poses.py + Episodes/<Guest>/poses.py)
  - a silent reaction from a seed frame names the pose, held (`hold`)
  - a talking clip from a seed frame with an `entry` (hand at the face) carries it
  - no prompt from a seed frame names a body contact that frame does not have (pose `avoid`)
  - no prompt names a repeatable gesture (blink, nod, head shake, look away and back, lift and settle back)
Added 2026-09-24 (Salah): the skills know the poses, so a prompt is right without anyone catching it by eye.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import poses

kit = sys.argv[1]
P = poses.load(os.path.dirname(os.path.abspath(kit)))
t = open(kit).read()
bad = []; n = 0
for m in re.finditer(r'^\*\*(P\d_\d+)\*\* · ([A-Z-]+)[^\n]*\n`start_frame` `([^`]+)`[^\n]*\n(?:(?!^\*\*P\d_)[\s\S])*?^```\n([\s\S]*?)^```', t, re.M):
    rid, typ, st, prompt = m.groups(); n += 1
    low = prompt.lower()
    for g in re.finditer(poses.REPEATABLE, low):
        bad.append(f'{rid}  REPEATABLE gesture "{g.group(0)}" — a move that goes and comes back loops (Mode 4 §5)')
    if st.startswith('chain') or not st.startswith('frame_'): continue
    if st not in P:
        bad.append(f'{rid}  NO POSE ENTRY for {st} — add it to the pose table'); continue
    e = P[st]
    for w in e.get('avoid', []):
        if w in low: bad.append(f'{rid}  names "{w}" — {st} has no such contact ({e["desc"]})')
    if typ == 'REACTION':
        if e['hold'] not in prompt: bad.append(f'{rid}  REACTION from {st} does not hold the pose: "{e["hold"]}"')
    elif re.search(r'\):\s*"', prompt) and e.get('entry') and e['entry'] not in prompt:
        bad.append(f'{rid}  TALKING from {st} lacks its entry: "{e["entry"]}"')
for b in bad: print(b)
print(f'-- pose check: {n} prompts, {len(bad)} problems' + ('' if not bad else ' — FAIL'))
sys.exit(1 if bad else 0)
