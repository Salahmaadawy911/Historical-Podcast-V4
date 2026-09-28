#!/usr/bin/env python3
"""Spoken-line gate: banned phrases + pronunciation coverage. Every kit, every part, before generation.

Usage:  python3 Fixed_Assets/tools/lines_check.py Episodes/<Guest>/P<n>_kit.md [--require-prompt-notes]   (or OUTLINE.md — Mode 3)

1. BANNED PHRASES — AI-cliché and melodrama phrasing (project rule: zero melodrama). Any hit stops the run.
2. PRONUNCIATION — every rare proper name in a spoken line must have an entry in the kit's
   "### Pronunciation" table (| Word | Say it | ... |). "Rare" = a capitalised word the CMU dictionary does
   not know, or one we added ourselves in names.dict. Common names (Rome, Egypt, Caesar) pass.
   With --require-prompt-notes, every prompt whose line contains a listed word must also carry a
   'Pronunciation:' paragraph (turn on once the pronunciation A/B has passed — Mode 4 §3).
Exits 1 on any failure; prints what it scanned so a silent zero is impossible.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import junction_scan as J

BANNED = [
    "tapestry", "delicate dance", "alas", "testament to", "sands of time",
    "echoes through", "echoed through", "annals of", "stood the test of time", "little did",
    "the rest is history", "delve", "unravel", "shed light", "a pivotal", "at the end of the day",
    "in a world where", "stark reminder", "rich history", "journey through", "navigate the",
    "woven into", "fabric of", "whispers of", "the weight of history", "beacon of", "a force to be reckoned",
]
NAMES_DICT = set()
for ln in open(os.path.join(J.HERE, 'names.dict'), encoding='utf-8'):
    ln = ln.split('#')[0].strip()
    if ln: NAMES_DICT.add(re.sub(r'\(\d+\)$', '', ln.split()[0].lower()))

def rare(word):
    w = word.lower().replace('’', "'")
    if w.endswith("'s"): w = w[:-2]
    for cand in (w, w[:-1] if w.endswith('s') else None):
        if cand and cand in NAMES_DICT: return True
    return J.prons(w) is None and (not w.endswith('s') or J.prons(w[:-1]) is None)

def tail_hit(line):
    ws = re.findall(r"[A-Za-z']+", line)
    if not ws: return None
    ph = J.phones(ws[-1])
    return ws[-1] if ph and len(ph) >= 2 and ph[-1] in J.STOPS and ph[-2] in J.STOPS else None

def tail_warn(lab, line):
    # added 2026-09-24 (T8, "described"): a clip's LAST word ending in two stops (/bd/, /kt/, /pt/ …) is where
    # lip-sync strains — warning only; Mode 3 can reorder, Mode 4/6 hide it with the cut or the lip-sync tool
    ws = re.findall(r"[A-Za-z']+", line)
    if not ws: return
    ph = J.phones(ws[-1])
    if ph and len(ph) >= 2 and ph[-1] in J.STOPS and ph[-2] in J.STOPS:
        print(f'{lab}  TAIL "{ws[-1]}" ends the line on a stop cluster — expect a strained last word   | {line[:60]}')

SERIES_NAME = 'History Answers Back'   # the show's own name, said in every welcome (2026-09-28) — not a guest's name
COMMON_CAPS = {'Death','East','West','North','South','Gulf','Kings','King','Library','March','Moon','Partners','Queen','Red','Sea','Senate','Sun','God','Gods','Mother','Father','Lord','Lady','Sir','Madam'}
def main(path, require_notes):
    s = open(path, encoding='utf-8').read()
    table = {}
    # L48 (2026-09-27): the OUTLINE's Pronunciation table is the only source of respellings. A kit is checked against
    # its own table AND the guest's OUTLINE.md table, and a `write: X` respelling (which the builder puts inside the
    # quote) counts as covered — the gate used to flag the kit's own respellings (Seezer, Antonee) as unlisted names.
    srcs = [s]
    _ol = os.path.join(os.path.dirname(os.path.abspath(path)), 'OUTLINE.md')
    if os.path.abspath(path) != _ol and os.path.exists(_ol): srcs.append(open(_ol, encoding='utf-8').read())
    for src in srcs:
        if '### Pronunciation' not in src: continue
        sec = src[src.index('### Pronunciation'):]
        sec = sec[:sec.find('\n## ', 1) if '\n## ' in sec[1:] else None]
        for m in re.finditer(r'^\|\s*([A-Z][\w’\']+)\s*\|\s*([^|]+?)\s*\|([^\n]*)', sec, re.M):
            if m.group(1) == 'Word': continue
            table[m.group(1).lower()] = m.group(2)
            w_ = re.search(r'write:\s*([^|·\s]+)', m.group(3))
            if w_: table.setdefault(w_.group(1).lower(), 'respelling of ' + m.group(1))
    bad = 0; scanned = 0; talk = 0; need = {}
    import outline_lines as O
    rows = [(lab, f'"{line}"\n', line) for lab, spk, note, line in O.spoken(s)] if O.is_outline(s) else None
    if rows is not None:
        import syl as _syl
        raw = s.split('\n')
        for lab, _, line in rows:
            scanned += 1; low = line.lower()
            # TAIL RULE (Salah, 2026-09-24): in the OUTLINE a line may not end on a word-final stop cluster
            # (described /bd/, marked /kt/, Egypt /pt/) — the clip's last word is where lip-sync strains.
            # Rephrase — always (TAIL-OK withdrawn 2026-09-24).
            w_ = tail_hit(line)
            if w_:
                ln = int(lab.split(':L')[1]); nxt = next((x for x in raw[ln:] if x.strip()), '')
                # no exceptions since 2026-09-24 (Salah): TAIL-OK is withdrawn
                print(f'{lab}  TAIL "{w_}" — the line ends on a stop cluster; rephrase (Mode 3 rule 5, no exceptions)   | {line[:60]}'); bad += 1
            # the word before a SPLIT seam ends clip A — same rule
            ln = int(lab.split(':L')[1]); sp = next((x for x in raw[ln:ln + 3] if x.startswith('> SPLIT at')), '')
            m_ = re.search(r'SPLIT at "([^"]+)"', sp)
            if m_ and m_.group(1) in line:
                wa = tail_hit(line[:line.index(m_.group(1))])
                if wa: print(f'{lab}  TAIL "{wa}" before the SPLIT seam (end of clip A); rephrase   | {line[:60]}'); bad += 1
            # OPEN1 (L50, 2026-09-27, warn only): a line that opens on a lone word gives the voice no context —
            # Kling read "Allies." letter by letter (P1_046). Names, yes/no and table words with a decision are fine.
            _f = re.match(r'\s*([A-Za-z’\']+)[.!?](\s|$)', line)
            if _f and _f.group(1).lower() not in ('no','yes','never','always','exactly','perhaps','please','enough','nothing','no one','both','neither','again','later','once','twice','why','how','what','when','who') \
               and _f.group(1).lower() not in table and not re.search(r'[a-z,;]\s' + _f.group(1) + r'\b', s):   # a proper noun appears capitalised mid-sentence somewhere
                print(f'{lab}  OPEN1 "{_f.group(1)}." — the line opens on a lone word; give it context ("{_f.group(1)}, not …") or a Pronunciation row (write:/plain)   | {line[:60]}')
            # NAME (L53, 2026-09-27, Salah): EVERY name and place in a spoken line has a Pronunciation row — its own
            # row for a possessive/plural ("Antony's" was said "Antoy's", P1_106). Common capitalised words are exempt.
            for _n in re.findall(r"(?<=[a-z,;:—–-] )([A-Z][a-z]+(?:['’]s)?)", line.replace(SERIES_NAME, '')):
                if _n.lower() not in table and _n not in COMMON_CAPS:
                    print(f'{lab}  NAME "{_n}" has no Pronunciation row — add one (write: <respelling> or plain)   | {line[:60]}'); bad += 1
            if _syl.dur2(line)[1] > 15:   # added 2026-09-23: warn only — Mode 3 marks a SPLIT, or Mode 4 splits it
                print(f'{lab}  LONG {_syl.dur2(line)[1]} s — past the 15 s clip cap; mark a SPLIT at a sentence   | {line[:60]}…')
            for b in BANNED:
                if re.search(r'\b' + re.escape(b) + r'\b', low):
                    print(f'{lab}  BANNED "{b}"   | {line}'); bad += 1
            for w in re.findall(r"\b[A-Z][a-z]+(?:['’]s)?\b", line):
                base = re.sub(r"['’]s$", '', w)
                if rare(base): need.setdefault(base, []).append(lab)
        if not rows: print('STOP — outline has no spoken lines in the HOST:/GUEST: format.'); sys.exit(2)
    for row in ([] if rows is not None else re.split(r'\n(?=\*\*[A-Z0-9]+_\d{3}[a-z]?\*\* · )', s)):
        m = re.match(r'\*\*([A-Z0-9]+_\d{3}[a-z]?)\*\* · (\w+)', row)
        if not m: continue
        if m.group(2) in ('INTERVIEW', 'INTERJECTION', 'NARRATION'): talk += 1
        for line in O.kit_spoken(row):           # every segment of a beat map, not just the first quote
            scanned += 1; tail_warn(m.group(1), line)
            low = line.lower()
            for b in BANNED:
                if re.search(r'\b' + re.escape(b) + r'\b', low):
                    print(f'{m.group(1)}  BANNED "{b}"   | {line}'); bad += 1
            for w in re.findall(r"\b[A-Z][a-z]+(?:['’]s)?\b", line):
                base = re.sub(r"['’]s$", '', w)
                if rare(base):
                    need.setdefault(base, []).append(m.group(1))
                    if require_notes and base.lower() in table and 'Pronunciation:' not in row:
                        print(f'{m.group(1)}  "{base}" is listed but the prompt has no Pronunciation: line'); bad += 1
    missing = {k: v for k, v in need.items() if k.lower() not in table}
    for k, v in sorted(missing.items()):
        print(f'NO PRONUNCIATION  "{k}"  — in {", ".join(sorted(set(v)))}'); bad += 1
    print(f'-- scanned {scanned} spoken lines ({talk} talking rows); {len(need)} rare names, {len(table)} in the Pronunciation table')
    if talk and scanned < talk:
        print('STOP — fewer spoken lines than talking rows: the attribution format changed; fix the scanner.'); sys.exit(2)
    if bad: print(f'STOP — {bad} problem(s) in spoken lines.'); sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    main(sys.argv[1], '--require-prompt-notes' in sys.argv)
