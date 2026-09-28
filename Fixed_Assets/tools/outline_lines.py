"""Shared reader for OUTLINE.md (Mode 3's script format). Used by script_read.py, junction_scan.py
and lines_check.py so the words can be checked and read before Mode 4 builds a single prompt.

Format (Mode 3, "The outline file"):
  ## Part N — title                    ### Act / Opening / Close headings
  HOOK: "exact guest sentence"          QUESTION: the act's question
  HOST: "line" [V]                      GUEST (note): "line" [D — source]
  > TAG ...                             direction: OVERLAP NOD OFFMIC BEAT BROLL CUT-IN:<kind> SPLIT TWOUP CARD PULL
"""
import re
SPEAK = re.compile(r'^(HOST|GUEST)\s*(?:\(([^)]*)\))?\s*:\s*"(.*?)"\s*(\[[^\]]*\])?(.*)$')
OFFMIC = re.compile(r'^>\s*(?:OFFMIC|CUT-IN:\w+\s*—)\s*(HOST|GUEST)\s*(?:\(([^)]*)\))?\s*:\s*"(.*?)"')

def is_outline(text):
    return bool(re.search(r'^(HOST|GUEST)\s*(\([^)]*\))?\s*:\s*"', text, re.M)) and \
           not re.search(r'^\*\*P\d+_\d{3}[a-z]?\*\* · ', text, re.M)

def spoken(text):
    """Every spoken line, on or off camera: [(label, speaker, note, line)]. Label = P<n>:L<lineno>."""
    out, part = [], 0
    for i, ln in enumerate(text.split('\n'), 1):
        m = re.match(r'^## Part (\d+)', ln)
        if m: part = int(m.group(1)); continue
        m = SPEAK.match(ln) or OFFMIC.match(ln)
        if m: out.append((f'P{part}:L{i}', m.group(1), m.group(2) or '', m.group(3)))
    return out


# ---- kit side, added 2026-09-23 (Mode 4, beat maps) ----
# A kit prompt may carry a BEAT MAP (Mode 4 §4 item 8): one attribution paragraph holding several quoted
# segments —  The woman says, flatly: "A." Then, plainly: "B." She lets the hand settle. Then, dry: "C."
# Every gate must read EVERY segment, not the first quote (or, worse, the stage text between quotes).
ATTR = re.compile(r'(?:\bsays\b[^"\n]*?|\([^)"\n]*\)):\s*"')   # `says, <note>: "…"` or the label form `Name (<note>): "…"` (T8, 2026-09-24)
def kit_spoken(text):
    """Every spoken line in kit text: one string per attribution paragraph, all its quoted segments
    joined by a space. Stage directions between segments are dropped. Works on a row or a whole kit."""
    out = []
    for ln in text.split('\n'):
        m = ATTR.search(ln)
        if not m: continue
        segs = re.findall(r'"([^"]*)"', ln[m.start():])
        if segs: out.append(' '.join(x.strip() for x in segs))
    return out
