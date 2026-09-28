#!/usr/bin/env python3
"""Screen-share gate — the guest carries the picture. Mode 4 §8b, *Screen share* (Salah, 2026-09-24).

Usage:  python3 Fixed_Assets/tools/screen_share.py Episodes/<Guest>/P<n>_kit.md

Every talking, reaction and b-roll row carries a line
    **screen:** G 3.2 · H 1.1 · 2UP 0 · BROLL 0
(seconds of speech-model time on screen for each), and the row that opens a two-up carries
    **twoup:** #n
The builder computes both from the placements; this gate only adds them up and checks the rules:

  1. guest share = (G + 2UP) / (G + H + 2UP) >= 65 %  (B-roll and furniture are left out)
  2. two-ups: at most 7, each 3-6 s of screen time, never two within two rows of each other, and
     every two-up has someone TALKING in it — never both faces only reacting (Salah, 2026-09-24, T6b)
  3. full-frame host reactions (a REACTION · HOST row with H > 0): at most 2 — except a CUT-IN stop
     (edit_placement "follows ..."), which is part of his own line. Relaxed if the kit header says
     `composite: yes` (eyewitness episodes: the host may answer hard testimony on screen).
Prints the table and exits 1 on any failure. Fails if it found no screen lines (a gate that checks
nothing must not look like a pass).
"""
import re, sys

def main(path):
    kit = open(path, encoding='utf-8').read()
    composite = bool(re.search(r'^composite:\s*yes', kit, re.M | re.I))
    rows = re.split(r'\n(?=\*\*P\d+_\d{3}[a-z]?\*\* · )', kit)
    tot = {'G': 0.0, 'H': 0.0, '2UP': 0.0, 'BROLL': 0.0}
    need = seen = 0; idx = 0; twoups = []; host_full = []; err = []
    for r in rows:
        m = re.match(r'\*\*(P\d+_\d{3}[a-z]?)\*\* · (\w+)(?: · (HOST|GUEST))?', r)
        if not m: continue
        sid, typ, who = m.groups(); idx += 1
        if typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION', 'REACTION', 'BROLL_GEN'): need += 1
        s = re.search(r'^\*\*screen:\*\*\s*(.+)$', r, re.M)
        if not s: continue
        seen += 1
        vals = dict((k, float(v)) for k, v in re.findall(r'(G|H|2UP|BROLL)\s+([\d.]+)', s.group(1)))
        for k, v in vals.items(): tot[k] += v
        t = re.search(r'^\*\*twoup:\*\*\s*#(\d+)', r, re.M)
        if t: twoups.append([sid, 0.0, int(t.group(1)), idx, False])
        if twoups and vals.get('2UP', 0):
            twoups[-1][1] += vals['2UP']
            if typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION'): twoups[-1][4] = True
        place = (re.search(r'^\*\*edit_placement:\*\*\s*(.*)$', r, re.M) or [None, ''])[1]
        if typ == 'REACTION' and who == 'HOST' and vals.get('H', 0) > 0 and not place.startswith('follows'):
            host_full.append(sid)
    if not seen:
        print('STOP — no **screen:** lines in the kit; the gate checked nothing.'); sys.exit(2)
    if seen < need: err.append(f'{need - seen} talking/reaction/b-roll rows have no screen: line')
    studio = tot['G'] + tot['H'] + tot['2UP']
    share = (tot['G'] + tot['2UP']) / studio if studio else 0
    mm = lambda x: f'{int(x // 60)}:{x % 60:04.1f}'
    print(f'guest full frame  {mm(tot["G"])}\nhost full frame   {mm(tot["H"])}\ntwo-up            {mm(tot["2UP"])}  ({len(twoups)} of them)\nb-roll            {mm(tot["BROLL"])}  (not in the share)')
    print(f'guest share of studio picture: {share:.0%}   (host {tot["H"] / studio:.0%})')
    if share < 0.65: err.append(f'guest share {share:.0%} < 65% — put more host questions on her face (Mode 4 §8b)')
    if len(twoups) > 7: err.append(f'{len(twoups)} two-ups — at most 7 per part')
    for sid, secs, n, _, talk in twoups:
        if not talk:
            err.append(f'two-up #{n} at {sid} has nobody talking in it — a silence goes on one face, hers (Mode 4 §8b)')
        if not 3.0 <= secs + 1e-6 <= 6.0 + 1e-6 and secs:
            err.append(f'two-up #{n} at {sid} runs {secs:.1f} s — keep each to 3-6 s')
    for a, b in zip(twoups, twoups[1:]):
        if b[3] - a[3] <= 2: err.append(f'two-ups #{a[2]} and #{b[2]} are back to back ({a[0]}, {b[0]}) — never two in a row')
    if len(host_full) > 2 and not composite:
        err.append(f'{len(host_full)} full-frame host reactions ({", ".join(host_full)}) — at most 2 (two-ups for the rest)')
    print(f'full-frame host reactions: {len(host_full)} {host_full}')
    for e in err: print('FAIL  ' + e)
    print('screen share: ' + ('PASS' if not err else f'STOP ({len(err)})'))
    sys.exit(1 if err else 0)

if __name__ == '__main__':
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
