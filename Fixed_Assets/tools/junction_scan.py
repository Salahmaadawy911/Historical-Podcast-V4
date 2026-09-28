#!/usr/bin/env python3
"""Phonetic junction gate — HARD RULE, every kit, every episode, before any clip is generated.

Usage:  python3 Fixed_Assets/tools/junction_scan.py Episodes/<Guest>/P<n>_kit.md   (or OUTLINE.md — Mode 3)
Prints every violation and exits 1; prints nothing and exits 0 when the kit is clean.

The rule (skill_mode4_produce.md, "Check the consonant junctions"):
  a word ending in a stop  /p b t d k g/  (alone or closing a cluster: -pt -kt -st -nd -nt ...)
  running straight into a word that opens on a STRESSED vowel.
  "without Egypt" failed five times across 7-13s clips and every position; "without it" was clean.
Punctuation between the words (, . ; : ? ! —) is a release and breaks the junction.
Weak function words (a, an, and, it, of, in, I ...) are unstressed in running speech and do not count.
Pronunciation and stress come from the CMU Pronouncing Dictionary (cmudict.dict beside this file).
Proper names the dictionary lacks go in names.dict (same format).
Words neither file knows are flagged if they open on a vowel letter — check them by ear.
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
STOPS = {'P','B','T','D','K','G'}
WEAK = {'a','an','and','as','at','in','is','it','its',"it's",'of','on','or','if','i','am','are','us','our','was','were','an'}
CMU = {}   # word -> list of pronunciations
for fn in ('names.dict', 'cmudict.dict'):      # names.dict first: the show's own proper names
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        for ln in f:
            ln = ln.split('#')[0].strip()
            if not ln: continue
            w, *ph = ln.split()
            w = re.sub(r'\(\d+\)$', '', w.lower())
            if fn == 'cmudict.dict' and w in CMU and CMU[w][0][0] == 'NAMES': continue
            CMU.setdefault(w, []).append(ph)
    if fn == 'names.dict':
        for w in CMU: CMU[w].insert(0, ['NAMES'])
def prons(w):
    w = w.lower().strip("'").replace('’', "'")
    for k in (w, w[:-2] if w.endswith("'s") else None):
        if k and k in CMU: return [p for p in CMU[k] if p != ['NAMES']]
    return None
def phones(w):
    p = prons(w); return p[0] if p else None
def ends_in_stop(w):
    p = phones(w)
    if p: return p[-1] in STOPS
    return bool(re.search(r"(?:[bcdgkpt]|ed)$", w.lower()))   # unknown word: spelling guess
def opens_on_stressed_vowel(w):
    if w.lower() in WEAK: return False
    p = prons(w)
    if p: return all(x[0][-1] == '1' for x in p)            # primary stress on the opening vowel, every reading
    return bool(re.match(r'[aeiou]', w.lower()))            # unknown: conservative
def scan_line(txt):
    toks = re.findall(r"[A-Za-z][A-Za-z']*|[^\sA-Za-z']", txt)
    out = []
    for a, b in zip(toks, toks[1:]):
        if a[0].isalpha() and b[0].isalpha() and ends_in_stop(a) and opens_on_stressed_vowel(b):
            unk = '' if phones(a) and phones(b) else '  (not in dictionary — check by ear)'
            out.append(f'"{a} {b}"{unk}')
    return out
def main(path):
    s = open(path, encoding='utf-8').read()
    import outline_lines as O
    if O.is_outline(s):
        bad = 0; lines = O.spoken(s)
        for lab, spk, note, line in lines:
            for hit in scan_line(line):
                print(f'{lab}  {hit}   | {line}'); bad += 1
        if not lines: print('STOP — outline has no spoken lines in the HOST:/GUEST: format.'); sys.exit(2)
        if bad: print(f'STOP — {bad} phonetic junction(s) in spoken lines. Rephrase before Mode 4.'); sys.exit(1)
        return
    bad = 0; talk = 0; scanned = 0
    for row in re.split(r'\n(?=\*\*[A-Z0-9]+_\d{3}[a-z]?\*\* · )', s):
        m = re.match(r'\*\*([A-Z0-9]+_\d{3}[a-z]?)\*\*', row)
        if not m: continue
        if re.match(r'\*\*[A-Z0-9]+_\d{3}[a-z]?\*\* · (INTERVIEW|INTERJECTION|NARRATION)', row): talk += 1
        # matches both 'says: "…"' and the inline-delivery form 'says, level and dry: "…"'
        for line in O.kit_spoken(row):           # every segment of a beat map, not just the first quote
            scanned += 1
            for hit in scan_line(line):
                print(f'{m.group(1)}  {hit}   | {line}'); bad += 1
    if talk and scanned < talk:
        # a gate that silently checks nothing is worse than no gate: this happened 2026-09-21, when the
        # attribution format changed to 'says, <note>:' and this scanner found zero lines for a day
        print(f'STOP — {talk} talking rows but only {scanned} spoken lines found. The attribution format changed; fix the scanner.')
        sys.exit(2)
    if bad:
        print(f'STOP — {bad} phonetic junction(s) in spoken lines. Rephrase before generating.')
        sys.exit(1)
if __name__ == '__main__':
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
