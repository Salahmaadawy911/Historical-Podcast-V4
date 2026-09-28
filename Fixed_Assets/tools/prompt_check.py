"""Prompt gate — the prompt-writing lessons from testing, checked on every kit.

  python3 Fixed_Assets/tools/prompt_check.py Episodes/<Guest>/P<n>_kit.md

Each check is a lesson in Fixed_Assets/LESSONS.md (L-numbers). pose_check.py covers the pose lessons.
  L1  the bracket before a quote is a simple Kling tone: no "then", no ";", at most 6 words      (T8/tones)
  L2  no separate "Pronunciation:" paragraph — Kling reads it aloud; respell inside the quote     (T1)
  L51 every talking/reaction prompt opens "Camera: locked-off static shot. Movement: hold one fixed camera position…"
      and closes "Maintain absolute visual continuity. …" (structure v3, 2026-09-27; chip OFF). Supersedes L3/L33.
  L19 every studio prompt says "Only one person is in the frame." — the off-frame partner wandered in (P1_034)
  L4  a silent reaction never names talking, mouthing or speech                                  (P1_019)
  L42 a silent reaction names no audience/other people (the room, crowd, everyone…) and
      closes on stillness (still / nothing else moves / without moving / composed)             (P1_003a)
"""
import re, sys
kit = sys.argv[1]; t = open(kit).read(); bad = []; n = 0
# L48 (2026-09-27): every Pronunciation-table word carries a decision — `write: X` or `plain` — and a `write:` word
# never appears raw inside a spoken quote. Also stress homographs (noun/verb) need a table row.
import os
_o = os.path.join(os.path.dirname(os.path.abspath(kit)), 'OUTLINE.md'); PR = {}
if os.path.exists(_o):
    _s = open(_o, encoding='utf-8').read()
    if '### Pronunciation' in _s:
        _sec = _s[_s.index('### Pronunciation'):]; _sec = _sec[:_sec.find('\n## ')]
        for _m in re.finditer(r"^\| ([A-Z][\w'’]+) \|[^|\n]*\|([^|\n]*)\|", _sec, re.M):
            if _m.group(1) == 'Word': continue
            _d = _m.group(2); PR[_m.group(1)] = 'write' if 'write:' in _d else ('plain' if 'plain' in _d else None)
            _w = re.search(r'write:\s*([^·|]+)', _d)
            if _w and re.search(r'[-\s]|.[A-Z]', _w.group(1).strip()): bad.append(f'OUTLINE  L49 respelling "{_w.group(1).strip()}" for {_m.group(1)} — one plain word, no hyphens or capitals inside (hyphens make her spell it out)')
    for w, d in PR.items():
        if d is None: bad.append(f'OUTLINE  L48 pronunciation row "{w}" has no decision — add `write: <respelling>` or `plain`')
HOMO = r'\b(allies|ally|record|present|conduct|contract|object|permit|rebel|produce|refuse|contest|convict|desert|project|subject|progress|survey|content|minute)\b'
for m in re.finditer(r'^\*\*(P\d_\d+)\*\* · ([A-Z-]+)[^\n]*\n(?:(?!^\*\*P\d_)[\s\S])*?^```\n([\s\S]*?)^```', t, re.M):
    rid, typ, pr = m.groups(); low = pr.lower()
    if typ.startswith('BROLL') or typ.startswith('BUMPER'): continue
    n += 1
    for b in re.findall(r'\(([^()"\n]*)\):\s*"', pr):
        if re.search(r'\bthen\b|;', b) or len(b.split()) > 6:
            bad.append(f'{rid}  L1 bracket "({b})" — use a simple Kling tone (tone_map.py)')
    if re.search(r'^\s*pronunciation:', pr, re.M | re.I): bad.append(f'{rid}  L2 "Pronunciation:" paragraph — respell inside the quote')
    for q in re.findall(r'\):\s*"([^"]*)"', pr):
        for w, d in PR.items():
            if d == 'write' and re.search(r'\b' + re.escape(w) + r'(?![\w])', q): bad.append(f'{rid}  L48 "{w}" written raw in the line — use its respelling')
        for h in re.findall(r'(?:^|[.!?]\s)(' + HOMO[3:-3] + r')[.!?]', q, re.I):
            if h.capitalize() not in PR: bad.append(f'{rid}  L48 stress homograph "{h}" standing alone — add a Pronunciation row (write:/plain)')
    if not low.lstrip().startswith('camera: locked-off static shot. movement: hold one fixed camera position'): bad.append(f'{rid}  L51 prompt does not open with the v3 camera paragraph')
    if 'maintain absolute visual continuity' not in low: bad.append(f'{rid}  L51 missing the closing lighting-continuity paragraph')
    if 'only one person is in the frame' not in low: bad.append(f'{rid}  L19 missing "Only one person is in the frame."')
    if typ == 'REACTION' and re.search(r'\b(talk|talks|talking|speak|speaks|speaking|mouth(s|ing)? words?|says)\b', low):
        bad.append(f'{rid}  L4 silent reaction names speech')
    if typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION') and 'to the lens' not in low and 'direct' not in low[:0] and not re.search(r'eyes stay on the person sitting opposite', low) and 'turns slowly from the lens' not in low and 'to camera' not in low:
        bad.append(f'{rid}  L57 talking prompt does not say where the eyes stay (the person opposite, off frame)')
    if re.search(r'\btowards? (him|her)\b', low.split('voice:')[0]):
        bad.append(f'{rid}  L58 "toward him/her" — name the side of the frame (Kling can read "him" as the viewer and turn to the lens)')
    if typ == 'REACTION':
        body = re.sub(r'room tone', '', low.split('audio:')[0])
        if re.search(r'\b(to the room|the room|audience|crowd|everyone|onlookers|applause)\b', body):
            bad.append(f'{rid}  L42 silent reaction implies other people/an audience')
        if not re.search(r'(still\b|nothing else moves|without moving|without a flicker|composed\.)', body):
            bad.append(f'{rid}  L42 silent reaction does not close on stillness')
for b in bad: print(b)
print(f'-- prompt check: {n} prompts, {len(bad)} problems' + (' — FAIL' if bad else ''))
sys.exit(1 if bad else 0)
