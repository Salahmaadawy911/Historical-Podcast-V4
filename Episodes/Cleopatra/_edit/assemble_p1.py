#!/usr/bin/env python3
"""Mode 6 §3 — assembly of Cleopatra Part 1, built from the kit's edit_placements by measurement.

Usage:  python3 Episodes/Cleopatra/_edit/assemble_p1.py [--full] [--plan]
  --plan   resolve the timeline and write the cut list only (no render)
  --full   render 1920x1080 (default: a 960x540 review proxy small enough for git)
Needs:  _edit/prep_p1.py run first (voice-passed WAVs + words_p1.json), ffmpeg, numpy.
Writes: _edit/P1_assembly_timeline.json, _edit/P1_CUTLIST.md, P1_ASSEMBLY_review.mp4 (or P1_ASSEMBLY_1080.mp4).

Every time below is resolved from the aligned words of the take (never a typed timecode): the kit carries intent,
this script turns it into times. What the assembly leaves for the edit: the hook render, cards, lower thirds,
pull-quotes, subtitles, subscribe, drones — the opening is the fixed BRAND_opening until the hook is re-picked.
"""
import json, os, re, subprocess, sys, shutil
from concurrent.futures import ThreadPoolExecutor
import numpy as np

EP = 'Episodes/Cleopatra'; SH = f'{EP}/Shots'; ED = f'{EP}/_edit'
FA = 'Fixed_Assets'; FPS = 24; SR = 44100
FULL = '--full' in sys.argv; PLAN = '--plan' in sys.argv
OW, OH = (1920, 1080) if FULL else (960, 540)
WORDS = json.load(open(f'{ED}/words_p1.json'))
MAXGAP, NEWGAP = 1.2, 0.55          # dead air over ~1.2 s inside a take is trimmed to a breath (Mode 6 §3.3)
PRE, POST = 0.06, 0.15              # audio handles around the first / last word of a piece
JCUTS = [0.21, 0.17, 0.25, 0.13, 0.29, 0.19]   # incoming picture trails its voice by 3-7 frames, varied (§4)
PUNCH = 1.12                        # <= 15 % (§4)
FLAGS = []
def flag(m):
    if m not in FLAGS: FLAGS.append(m)

_dur = {}
def dur(p):
    if p not in _dur:
        f = p if os.path.sep in p else f'{SH}/{p}.mp4'
        _dur[p] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f],
                                       capture_output=True, text=True).stdout)
    return _dur[p]

# ---- kit: chains and join grades ---------------------------------------------------------------------------------
kit = open(f'{EP}/P1_kit.md').read()
CHAIN = dict((t, s) for t, s in re.findall(r'\| `(P1_\d+\w?)` \| `(P1_\d+\w?)`[^|]*\| (?:INTERVIEW|INTERJECTION|NARRATION|REACTION)', kit))
TYPE = dict(re.findall(r'\*\*(P1_\d+\w?)\*\* · (\w+)', kit))
REACT = {i for i, t in TYPE.items() if t == 'REACTION'}
CONT = {s: t for t, s in CHAIN.items() if t in REACT}          # a reaction chained off a clip continues its picture
GR = {m[0]: tuple(map(float, m[1:])) for m in re.findall(
    r'\| `(P1_\d+\w?)` \| `P1_\d+\w?` \| [\d.]+% \| `colorchannelmixer=rr=([\d.]+):gg=([\d.]+):bb=([\d.]+)`',
    open(f'{SH}/_measure/JOIN_GRADES.md').read())}
def grade(c):   # compounded along the chain: each grade was measured against the source's raw last frame
    g = GR.get(c, (1.0, 1.0, 1.0)); s = CHAIN.get(c)
    return tuple(a * b for a, b in zip(g, grade(s))) if s else g

BROLL = {'P1_031', 'P1_056', 'P1_076', 'P1_097', 'P1_107', 'P1_130'}
# two-up crops (Mode 4 §8b): x of the 960-wide half on the 1916-wide single, per start pose
HX = {'frame_host_e': 150, 'frame_host_d': 260, 'frame_host_b': 260, 'frame_host': 180}
GX = 800

def src_path(c):
    if c in BROLL: return f'{ED}/broll/{c}.mp4'
    return c if os.path.sep in c else f'{SH}/{c}.mp4'

# ---- the timeline ---------------------------------------------------------------------------------------------------
class TL:
    def __init__(s):
        s.t = 0.0; s.audio = []; s.pics = []; s.place = {}; s.end = {}; s.blocks = []; s.jc = 0; s.studio_from = None
        s.broll_audio = []; s.music = []
    # word lookups -> timeline seconds
    def _word(s, c, w, n):
        ws = [x for x in WORDS[c]['words'] if x[0] == w or x[0].rstrip("'s") == w]
        if not ws: raise SystemExit(f'{c}: word "{w}" not aligned')
        return ws[n - 1] if n > 0 else ws[n]
    def _tl(s, c, src):
        pl = s.place[c]; k = max([k for k, p in enumerate(pl) if src >= p[0] - 0.3] or [0])
        return src + pl[k][2]
    def W(s, c, w, n=1): return s._tl(c, s._word(c, w, n)[1])
    def We(s, c, w=None, n=1):
        if w is None: return s._tl(c, s.speech(c)[1])
        return s._tl(c, s._word(c, w, n)[2])
    def speech(s, c):
        ws = WORDS[c]['words']; b = ws[-1][2]
        if WORDS[c].get('unaligned'): b = dur(c) - 0.02      # last words not aligned (P1_055): speech runs to the end
        return ws[0][1], b
    def pieces(s, c, a=None, b=None, maxgap=MAXGAP):
        ws = [x for x in WORDS[c]['words'] if (a is None or x[1] >= a - 0.01) and (b is None or x[2] <= b + 0.05)]
        out = [[ws[0][1], ws[0][2]]]
        for (_, s0, e0), (_, s1, e1) in zip(ws, ws[1:]):
            if s1 - out[-1][1] > maxgap: out.append([s1, e1])
            else: out[-1][1] = e1
        if b is None and WORDS[c].get('unaligned'): out[-1][1] = dur(c) - 0.02
        if b is not None: out[-1][1] = b
        return out

    def brand(s, path, d, at=None, audio=True):
        t = s.t if at is None else at
        if s.studio_from is not None: s.blocks.append((s.studio_from, t))
        s.pics.append(dict(t=t, kind='free', clip=path, s0=0.0))
        if audio: s.audio.append(dict(t=t, path=path, a=0.0, b=d, gain=0.0, raw=True))
        s.t = t + d; s.studio_from = s.t; s.block_start = s.t
        return t

    def say(s, c, gap=0.4, at=None, after=None, gmin=0.35, gmax=1.0, pic='self', pic_t=None, a=None, b=None,
            gain=0.0, punch=False, maxgap=MAXGAP, newgap=NEWGAP, hard_out=False, two=None, hx=None, j=None):
        ps = s.pieces(c, a, b, maxgap)
        if at is not None: start = at
        elif after is not None:          # starts on the last frame of `after`: its source 0 sits at END[after]
            natural = s.end_of(after) + ps[0][0]
            start = min(max(natural, s.t + gmin), s.t + gmax)
            if abs(start - natural) > 0.02:
                FLAGS.append(f'{c}: chained join moved {start - natural:+.2f}s from the exact frame '
                             f'({"freeze on " + after if start > natural else "cut " + after + " early"})')
        else: start = s.t + gap
        placed = []; cur = start
        for k, (pa, pb) in enumerate(ps):
            if k: cur += newgap
            off = cur - pa; placed.append((pa, pb, off))
            s.audio.append(dict(t=cur - PRE, clip=c, a=pa - PRE, b=pb + (0.02 if hard_out and k == len(ps) - 1 else POST),
                                gain=gain))
            cur = pb + off
        s.place[c] = placed; s.end[c] = placed[-1][2] + dur(c)
        prev_t = s.t; s.t = cur
        if pic is None: return start
        off0 = placed[0][2]
        if pic_t is None and j is not None: pic_t = start + j
        if pic_t is None:
            if after is not None: pic_t = min(max(s.end_of(after), off0), start - 0.04)
            else:
                pic_t = start + JCUTS[s.jc % len(JCUTS)]; s.jc += 1
                pe = s.pic_end()               # the outgoing picture runs out: cut to the incoming earlier, on its lead-in
                if pe is not None and pe < pic_t: pic_t = max(pe, off0)
        if two:
            s.two(two, c, pic_t, hx)
        else:
            s.pics.append(dict(t=pic_t, kind='sync', clip=c, punch=punch))
        return start

    def pic_end(s):
        """where the latest picture runs out of frames (a sync take runs on into its chained reaction)"""
        if not s.pics: return None
        p = max(s.pics, key=lambda q: q['t'])
        if p['kind'] == 'free': return p['t'] + dur(p['clip']) - p['s0']
        c = p.get('clip') or p.get('guest')
        if c not in s.end: return None
        e = s.end[c]
        while c in CONT: c = CONT[c]; e += dur(c)
        return e

    def end_of(s, c):
        """timeline time of the last frame of take c itself"""
        if c in s.end: return s.end[c]
        if c in CHAIN: return s.end_of(CHAIN[c]) + dur(c)      # a chained reaction runs on from its source's end
        raise SystemExit(f'end of {c} unknown')

    def cover(s, c, t, s0=0.0, end_at=None):
        if end_at is not None: s0 = max(0.0, dur(c) - (end_at - t))
        s.pics.append(dict(t=t, kind='free', clip=c, s0=s0)); s.end[c] = t + dur(c) - s0
        return t
    def sync(s, c, t, punch=False): s.pics.append(dict(t=t, kind='sync', clip=c, punch=punch))
    def two(s, host, guest, t, hx=None):
        hx = hx if hx is not None else HX[pose(host)]
        s.pics.append(dict(t=t, kind='two', host=host, guest=guest, hx=hx, gx=GX)); s.end[host] = t + dur(host)

def pose(c):
    m = re.search(r'\*\*' + c + r'\*\* ·[^\n]*\n`start_frame` `([^`]+)`', kit)
    return m.group(1) if m else ''

OPEN = f'{FA}/Branding/BRAND_opening.mp4'
BREAK1 = f'{FA}/Branding/BRAND_actbreak_vessel.mp4'; BREAK2 = f'{FA}/Branding/BRAND_actbreak_stone.mp4'
ENDCARD = f'{EP}/BRAND_endcard_p1.mp4'

def build():
    L = TL()
    # ---------------------------------------------------------------- Opening (hook slot stays the fixed file's)
    L.brand(OPEN, dur(OPEN))
    L.say('P1_002', gap=0.3, pic_t=L.block_start)                       # hard cut in on the first strike
    L.say('P1_003', after='P1_002', gmin=0.45, gmax=1.0)                  # SPLIT seam: plain cut on the pause
    me = L.We('P1_003', 'me')
    L.cover('P1_003a', me + 0.04)                                         # cut to her as the turn lands
    L.say('P1_004', at=me + 1.5 - 0.2, pic_t=me + 1.5)                    # ~1.5 s of her face, then him from the seed
    L.cover('P1_005', L.W('P1_004', 'last') - 0.2)                         # title and thanks on her face
    L.say('P1_006', after='P1_005', gmin=0.7, gmax=1.3)                   # joins P1_005's end frame (same seed)
    # ---------------------------------------------------------------- Act A
    L.say('P1_007', gap=0.5)
    L.say('P1_008', gap=0.4, two='P1_009')                                # two-up #1, the whole line + 1.5 s
    e8 = L.We('P1_008'); L.sync('P1_008', e8 + 1.5)                        # her held face (P1_010 continues P1_008)
    L.say('P1_011', at=e8 + 1.5 + 0.9, pic=None)                          # under her; pull-quote 01 over this
    L.say('P1_012', after='P1_010', gmin=0.45, gmax=1.0)
    L.say('P1_013', gap=0.45)
    L.cover('P1_014', L.W('P1_013', 'hebrews') - 0.2)
    L.say('P1_015', after='P1_014', gmin=0.45, gmax=1.0)                  # joins P1_014's end frame
    L.say('P1_016', gap=0.4)
    L.say('P1_017', gap=0.4)
    L.say('P1_018', gap=0.4)
    L.cover('P1_019', L.W('P1_018', 'why') - 0.2)
    L.say('P1_020', after='P1_019', gmin=0.45, gmax=1.0)
    L.say('P1_021', gap=0.35)
    L.say('P1_022', gap=0.4)
    L.say('P1_023', at=L.We('P1_022', 'exist') + 0.3, pic=None)          # OFFMIC under her tail
    L.say('P1_025', gap=0.5, pic=None)                                    # under P1_024 (continues P1_022)
    L.say('P1_026', after='P1_024', gmin=0.45, gmax=1.0)
    L.say('P1_027', gap=0.4)
    L.say('P1_028', gap=0.4)
    L.say('P1_029', gap=0.4)
    L.say('P1_030', gap=0.4, j=-0.08)                                     # card 03 enters on her first word: on her
    L.cover('P1_031', L.W('P1_030', 'they', 2) - 0.12)                    # from "they handed him the head"
    L.say('P1_032', gap=0.45, pic=None)                                   # his voice under the b-roll
    L.say('P1_033', gap=0.45, pic_t=None)
    L.pics[-1]['t'] = L.W('P1_033', 'he')                                  # cut back on her first word
    L.two('P1_034', 'P1_033', L.W('P1_033', 'rome') - 0.15)               # two-up #2
    e33 = L.We('P1_033'); L.sync('P1_033', e33 + 1.0)                      # held face (P1_035), pull-quote 02
    L.say('P1_036', at=e33 + 3.5)
    L.say('P1_037', gap=0.4)
    L.say('P1_039', gap=1.0, pic=None)                                    # the BEAT on her (P1_038), then his loop
    L.brand(BREAK1, 5.0, at=L.t + 0.45)                                   # cut straight to the act break
    # ---------------------------------------------------------------- Act B
    L.say('P1_041', gap=0.35, pic_t=L.block_start)
    L.say('P1_042', gap=0.35)
    L.say('P1_043', gap=0.4)
    L.say('P1_044', gap=0.4, b=L_word('P1_044', 'seezer')[2] + 0.03, hard_out=True)   # CUT-IN A, ends hard on "Caesar"
    cut = L.place['P1_044'][-1][2] + 2.95                                 # the kit's cut frame (chain_frames: 2.95 s)
    L.cover('P1_045', cut)                                                # B: the stop, from the same frame
    L.say('P1_046', at=cut - 0.3, pic_t=cut + 0.9)                         # C collides ~0.3 s early, picture late
    L.say('P1_048', gap=0.5, pic=None)                                    # under P1_047
    L.say('P1_049', after='P1_047', gmin=0.45, gmax=1.0)
    L.say('P1_051', gap=0.45)
    L.say('P1_052', gap=0.4)
    L.say('P1_054', gap=0.5, pic=None)                                    # the name lands on her (P1_053)
    L.say('P1_055', after='P1_053', gmin=0.45, gmax=1.0)
    L.cover('P1_056', L.W('P1_055', 'led') - 0.12)
    L.say('P1_057', gap=0.5)
    L.say('P1_058', gap=0.4)
    L.say('P1_059', at=L.We('P1_058') + 0.35, pic=None)                   # OFFMIC echo under her tail
    L.say('P1_061', gap=1.0, pic=None)                                    # BEAT, then the question on her (P1_060)
    L.say('P1_062', after='P1_060', gmin=0.45, gmax=1.0, two='P1_063')    # two-up #3
    e62 = L.We('P1_062'); h62 = min(2.0, L.end['P1_062'] - e62 - 0.05)   # ~2 s, as far as the take lasts
    L.say('P1_064', at=e62 + h62 + 0.2, pic_t=e62 + h62)                        # he waits; P1_064 joins P1_063's seed
    L.say('P1_065', gap=0.4)
    L.say('P1_066', gap=0.4)
    L.say('P1_067', gap=0.4)
    L.say('P1_068', gap=0.4)
    L.cover('P1_069', L.W('P1_068', 'who') - 0.2)
    L.say('P1_070', after='P1_069', gmin=0.45, gmax=1.0)                  # end of Act B — subscribe over her tail
    # ---------------------------------------------------------------- Act C
    L.say('P1_071', gap=0.8)                                              # card 05 (R) over him
    L.say('P1_073', gap=0.45, pic=None)                                   # her voice over his face (P1_072)
    L.sync('P1_073', L.W('P1_073', 'he') - 0.12)                          # to her at the sentence after card 05 has gone
                                                                          # (measured: the card leaves before "He had heard")
    L.say('P1_074', gap=0.4)
    L.say('P1_075', gap=0.4)
    L.cover('P1_076', L.W('P1_075', 'so') - 0.12)
    L.sync('P1_075', L.W('P1_075', 'nobody') - 0.12)
    L.say('P1_077', gap=0.4)
    L.say('P1_078', gap=0.4)
    L.two('P1_079', 'P1_078', L.W('P1_078', 'she', -1) - 0.15)            # two-up #4 from "She arrives as a goddess"
    e78 = L.We('P1_078'); L.sync('P1_078', e78 + 1.0)                      # held face (P1_080), pull-quote 03
    L.say('P1_081', at=e78 + 3.5)
    L.say('P1_082', gap=0.45)                                             # the crack
    L.cover('P1_083', L.W('P1_082', 'he') - 0.15)                          # full-frame host reaction 1 of 2
    L.say('P1_084', after='P1_083', gmin=0.8, gmax=1.4, maxgap=0.5, newgap=0.5)
    t86 = L.W('P1_084', 'in') - 0.15
    e84 = L.We('P1_084')
    p87 = e84 + 1.0 - L.speech('P1_087')[0]                               # BEAT ~1 s, then her words; src 0 of P1_087
    L.cover('P1_086', t86, end_at=p87)                                    # use the END of P1_086 (ends on the seed)
    L.say('P1_087', at=e84 + 1.0, pic_t=p87)
    L.say('P1_088', after='P1_087', gmin=0.3, gmax=0.7, punch=True)       # SPLIT B: PUNCH on the seam
    L.say('P1_089', gap=0.45)
    L.say('P1_090', gap=0.4)
    L.say('P1_092', gap=0.5, pic=None)                                    # under P1_091
    L.say('P1_093', after='P1_091', gmin=0.45, gmax=1.0)
    L.say('P1_094', gap=0.4)
    L.say('P1_095', gap=0.4)                                              # CAMERA-MOVED 27 px — retake pending
    L.say('P1_096', gap=0.45)
    L.cover('P1_097', L.W('P1_096', 'silver') - 0.3)                       # from "A silver stage"
    L.say('P1_098', gap=0.45, pic=None)
    L.sync('P1_098', min(L.W('P1_098', 'with') - 0.1, L.end['P1_097']))   # back to her after card 06 has gone
    L.say('P1_100', gap=0.25, pic=None)                                    # under P1_099
    L.say('P1_101', after='P1_099', gmin=0.45, gmax=1.0)
    L.two('P1_102', 'P1_101', L.W('P1_101', 'he') - 0.15)                  # two-up #6
    e101 = L.We('P1_101'); h101 = min(1.0, L.end['P1_101'] - e101 - 0.05)
    L.say('P1_103', at=e101 + h101 + 0.2, pic_t=e101 + h101)                       # P1_103 joins P1_102's seed
    L.say('P1_104', gap=0.4, j=-0.08)                                     # card 07 on her first word: on her
    L.brand(BREAK2, 5.0, at=max(L.end['P1_104'], L.t + 0.6))             # hold P1_104 to its end, then the break
    # ---------------------------------------------------------------- Act D
    L.say('P1_106', gap=0.35, pic_t=L.block_start)
    L.cover('P1_107', L.W('P1_106', 'vestal') - 0.12)
    L.say('P1_108', gap=0.45, pic=None)
    L.sync('P1_108', L.W('P1_108', 'then') - 0.1)                          # back to her after card 08 has gone
    L.say('P1_110', gap=0.5, pic=None)                                    # under P1_109
    L.say('P1_111', after='P1_109', gmin=0.45, gmax=1.0)
    L.say('P1_112', gap=0.4)
    L.say('P1_113', gap=0.4, two='P1_114')                                # two-up #7, the whole line + 1.5 s
    e113 = L.We('P1_113'); L.sync('P1_113', e113 + 1.5)                   # full frame again (P1_115)
    L.say('P1_116', at=e113 + 1.5 + 0.3, pic=None)
    L.say('P1_117', after='P1_115', gmin=0.45, gmax=1.0)
    L.say('P1_118', gap=0.45)
    L.cover('P1_119', L.W('P1_118', 'egypt') - 0.2)                        # the charge plays on her face
    L.say('P1_120', after='P1_119', gmin=0.8, gmax=1.4)
    L.say('P1_121', after='P1_120', gmin=0.3, gmax=0.7, punch=True)       # SPLIT B: PUNCH on the seam, held
    L.say('P1_122', at=L.W('P1_121', 'rome') + 0.3, pic=None, gain=-3.0,
          b=L_word('P1_122', 'that')[2] + 0.03, hard_out=True)            # CUT-IN:hold — "But that's", cut
    L.t = max(L.t, L.We('P1_121'))
    L.say('P1_123', gap=0.45)
    L.say('P1_124', gap=0.35)
    L.say('P1_125', gap=0.45)
    L.cover('P1_126', L.W('P1_125', 'how') - 0.15)
    L.say('P1_127', after='P1_126', gmin=0.45, gmax=1.0)
    # ---------------------------------------------------------------- Close
    L.say('P1_128', gap=0.45, j=-0.08)                                           # card 09 (R) over him
    L.cover('P1_130', L.W('P1_128', 'and') - 0.12)                        # from "and your sixty ships"
    L.say('P1_129', after='P1_128', gmin=0.3, gmax=0.7, pic=None)          # SPLIT B under the b-roll
    L.cover('P1_131', L.W('P1_129', 'did') - 0.15)                        # "Did you run?" on her face
    L.say('P1_132', after='P1_131', gmin=0.8, gmax=1.4)
    L.say('P1_133', gap=0.45)                                             # the hand-off; no goodbye
    t_out = min(L.t + 0.7, L.end['P1_133'])
    L.blocks.append((L.studio_from, t_out)); L.studio_from = None
    L.pics.append(dict(t=t_out, kind='outro'))
    L.outro_t = t_out; L.total = t_out + dur('P1_134') + 3.0 + 20.0 - 1.0
    L.music.append(dict(path=f'{FA}/Audio/MUSIC_Outro_Bed.wav', t=t_out - 10.0))   # peak lands on the transformation
    return L

def L_word(c, w, n=1):
    ws = [x for x in WORDS[c]['words'] if x[0] == w or x[0].rstrip("'s") == w]
    return ws[n - 1]

# ---- frame map ------------------------------------------------------------------------------------------------------
def frame_map(L):
    pics = sorted(L.pics, key=lambda p: p['t'])
    for p, q in zip(pics, pics[1:] + [dict(t=L.total)]): p['t1'] = q['t']
    N = int(round(L.total * FPS)); fm = [None] * N
    for p in pics:
        f0, f1 = int(round(p['t'] * FPS)), int(round(p['t1'] * FPS))
        if p['kind'] == 'outro':
            for f in range(f0, N): fm[f] = ('outro', f - f0)
            break
        first_piece = None
        for f in range(f0, min(f1, N)):
            t = f / FPS
            if p['kind'] == 'free':
                c = p['clip']; fm[f] = ('v', c, idx(c, p['s0'] + t - p['t']), grade_of(c), 1.0)
            elif p['kind'] == 'sync':
                c, i, k = sync_src(L, p['clip'], t)
                if first_piece is None: first_piece = k
                sc = PUNCH if (p['punch'] or (k - first_piece) % 2 == 1) else 1.0
                fm[f] = ('v', c, idx(c, i), grade_of(c), sc)
            elif p['kind'] == 'two':
                h = p['host']; hi = idx(h, t - p['t'])
                c, i, _ = sync_src(L, p['guest'], t)
                if i > dur(c) - 0.5 / FPS: flag(f'{c}: two-up runs past the end of the take (guest half holds its last frame)')
                if t - p['t'] > dur(h) - 0.5 / FPS: flag(f'{h}: two-up longer than the reaction (host half holds its last frame)')
                fm[f] = ('two', h, hi, grade_of(h), p['hx'], c, idx(c, i), grade_of(c), p['gx'])
    return fm

def grade_of(c): return grade(c) if c in TYPE else (1.0, 1.0, 1.0)
def idx(c, s):
    n = int(round(dur(c) * FPS)) - 1
    return min(max(int(s * FPS + 1e-6), 0), n)
def sync_src(L, c, t):
    pl = L.place[c]
    k = max([k for k, p in enumerate(pl) if k == 0 or t >= p[0] + p[2] - PRE - 0.1])
    s = t - pl[k][2]
    while s > dur(c) - 0.5 / FPS and c in CONT:            # the chained reaction continues the picture
        s -= dur(c); c = CONT[c]
    return c, s, k

def runs(fm):
    out = []
    for x in fm:
        if out:
            r = out[-1]; y = r['x']
            if x[0] == 'outro' and y[0] == 'outro': r['n'] += 1; continue
            if x[0] == 'two' and y[0] == 'two' and (x[1], x[3], x[4], x[5], x[7], x[8]) == (y[1], y[3], y[4], y[5], y[7], y[8]):
                r['n'] += 1; continue                    # both halves play on; tpad holds a half that runs out
            if x[0] == 'v' and y[0] == 'v' and (x[1], x[3], x[4]) == (y[1], y[3], y[4]):
                last = r['i0'] if r['freeze'] else r['i0'] + r['n'] - 1
                if r['n'] == 1 and x[2] == last: r['freeze'] = True; r['n'] += 1; continue
                if x[2] == last and r['freeze']: r['n'] += 1; continue
                if x[2] == last + 1 and not r['freeze']: r['n'] += 1; continue
        out.append(dict(x=x, i0=x[2] if x[0] in ('v', 'two') else 0, n=1, freeze=False))
    return out

def vf_single(c, g, sc):
    w = 1916 if c in TYPE else 1920
    fl = []
    if g != (1.0, 1.0, 1.0): fl.append('colorchannelmixer=rr=%.4f:gg=%.4f:bb=%.4f' % g)
    if sc != 1.0:
        cw, ch = int(w / sc) // 2 * 2, int(1080 / sc) // 2 * 2
        x = 0 if pose_side(c) == 'H' else w - cw                         # keep the face in, headroom kept
        fl.append(f'crop={cw}:{ch}:{x}:{int((1080 - ch) * 0.2)}')
    fl.append(f'scale={OW}:{OH}:flags=lanczos,setsar=1,fps={FPS},format=yuv420p')
    return ','.join(fl)

def pose_side(c):
    base = c
    while base in CHAIN: base = CHAIN[base]
    p = pose(base)
    if p.startswith('frame_host'): return 'H'
    return 'G'

ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14' if FULL else '16', '-pix_fmt', 'yuv420p', '-an']

def render_run(k, r, tmp):
    out = f'{tmp}/r{k:04d}.mp4'
    if os.path.exists(out): return out
    x = r['x']; n = r['n']
    if x[0] == 'v':
        c = x[1]; path = src_path(c); vf = vf_single(c, x[3], x[4])
        if r['freeze']:
            cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', '%.4f' % (r['i0'] / FPS), '-i', path, '-vf',
                   vf + f',trim=end_frame=1,tpad=stop={n - 1}:stop_mode=clone', '-frames:v', str(n)] + ENC + [out]
        else:
            cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', '%.4f' % (r['i0'] / FPS), '-i', path, '-vf',
                   vf + f',tpad=stop={n}:stop_mode=clone', '-frames:v', str(n)] + ENC + [out]
    elif x[0] == 'two':
        _, h, hi, hg, hx, gc, gi, gg, gx = x
        def half(lbl, g, cx):
            s = f'[{lbl}:v]'
            if g != (1.0, 1.0, 1.0): s += 'colorchannelmixer=rr=%.4f:gg=%.4f:bb=%.4f,' % g
            return s + f'crop=960:1080:{cx}:0,tpad=stop={n}:stop_mode=clone'
        fc = (f'{half(0, hg, hx)}[h];{half(1, gg, gx)}[g];[h][g]hstack,'
              f'drawbox=x=955:y=0:w=10:h=1080:color=0xCDC1AC:t=fill,'
              f'drawbox=x=958:y={int(1080 * .16)}:w=3:h={int(1080 * .68)}:color=0x9C6B3F:t=fill,'
              f'scale={OW}:{OH}:flags=lanczos,setsar=1,fps={FPS},format=yuv420p[v]')
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', '%.4f' % (hi / FPS), '-i', src_path(h), '-ss', '%.4f' % (gi / FPS),
               '-i', src_path(gc), '-filter_complex', fc, '-map', '[v]', '-frames:v', str(n)] + ENC + [out]
    elif x[0] == 'outro':   # 5 s transformation clean, ~3 s clean hold, 1 s dissolve into the 20 s end card
        d = dur('P1_134')
        fc = (f'[0:v]tpad=stop_duration=3.0:stop_mode=clone,scale={OW}:{OH},setsar=1,fps={FPS},format=yuv420p[a];'
              f'[1:v]scale={OW}:{OH},setsar=1,fps={FPS},format=yuv420p[b];'
              f'[a][b]xfade=transition=fade:duration=1.0:offset={d + 3.0 - 1.0:.3f}[v]')
        cmd = ['ffmpeg', '-v', 'error', '-y', '-i', src_path('P1_134'), '-i', ENDCARD, '-filter_complex', fc,
               '-map', '[v]', '-frames:v', str(n)] + ENC + [out]
    subprocess.run(cmd, check=True)
    return out

# ---- b-roll: normalised against its own first frame (Mode 6 §3.5) ----------------------------------------------------
def prep_broll():
    os.makedirs(f'{ED}/broll', exist_ok=True)
    for c in sorted(BROLL):
        out = f'{ED}/broll/{c}.mp4'
        if os.path.exists(out): continue
        W_, H_ = 1916, 1080
        rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', f'{SH}/{c}.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                              stdout=subprocess.PIPE)
        def frames():
            while True:
                b = rd.stdout.read(W_ * H_ * 3)
                if len(b) < W_ * H_ * 3: return
                yield np.frombuffer(b, np.uint8).reshape(H_, W_, 3)
        fr = frames(); first = next(fr); m0 = first.reshape(-1, 3).mean(0)
        import itertools; fr = itertools.chain([first], fr)
        p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W_}x{H_}',
                              '-r', str(FPS), '-i', '-', '-i', f'{SH}/{c}.mp4', '-map', '0:v', '-map', '1:a?',
                              '-c:v', 'libx264', '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'copy', out],
                             stdin=subprocess.PIPE)
        for f in fr:
            g = m0 / np.maximum(f.reshape(-1, 3).mean(0), 1)
            p.stdin.write(np.clip(f.astype(np.float32) * g, 0, 255).astype(np.uint8).tobytes())
        p.stdin.close(); p.wait(); rd.wait()

# ---- audio ----------------------------------------------------------------------------------------------------------
def load(path, a=0.0, b=None, sr=SR):
    cmd = ['ffmpeg', '-v', 'error', '-ss', '%.4f' % max(a, 0), '-i', path]
    if b is not None: cmd += ['-t', '%.4f' % (b - max(a, 0))]
    x = subprocess.run(cmd + ['-f', 'f32le', '-ac', '2', '-ar', str(sr), '-'], capture_output=True).stdout
    return np.frombuffer(x, np.float32).reshape(-1, 2).copy()

def lufs(path):
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s*(-?[\d.]+) LUFS', r)[-1])

def mix(L):
    n = int(L.total * SR) + SR; dia = np.zeros((n, 2), np.float32); oth = np.zeros((n, 2), np.float32)
    fade = int(0.005 * SR)
    for e in L.audio:
        if e.get('raw'): x = load(e['path'], 0, e['b']); tgt = oth
        else:
            x = load(f'{ED}/audio/{e["clip"]}.wav', e['a'], e['b']); tgt = dia
            x *= 10 ** (e['gain'] / 20)
        if len(x) > 2 * fade:
            ramp = np.linspace(0, 1, fade, dtype=np.float32)[:, None]; x[:fade] *= ramp; x[-fade:] *= ramp[::-1]
        i = int(round(max(e['t'], 0) * SR)); tgt[i:i + len(x)] += x[:n - i]
    # dialogue envelope for ducking b-roll ambience and music
    env = np.abs(dia).max(1); k = int(0.25 * SR)
    act = np.convolve((env > 10 ** (-40 / 20)).astype(np.float32), np.ones(k, np.float32) / k, 'same') > 0.02
    duck = np.convolve(act.astype(np.float32), np.ones(int(0.2 * SR), np.float32) / int(0.2 * SR), 'same')
    # b-roll native ambience at about -32 LUFS, ducked 8 dB under any dialogue it covers (Mode 6 Audio rule 1)
    for p in L.pics:
        if p['kind'] == 'free' and p['clip'] in BROLL:
            src = f'{ED}/broll/{p["clip"]}.mp4'; d = p['t1'] - p['t']
            x = load(src, p['s0'], p['s0'] + d)
            if not len(x): continue
            g = 10 ** ((-32 - lufs(f'{SH}/{p["clip"]}.mp4')) / 20); x *= g
            i = int(p['t'] * SR); seg = slice(i, i + len(x))
            x *= (1 - duck[seg][:, None] * (1 - 10 ** (-8 / 20))).astype(np.float32)[:len(x)]
            r = min(int(0.03 * SR), len(x) // 2); ramp = np.linspace(0, 1, r, dtype=np.float32)[:, None]
            x[:r] *= ramp; x[-r:] *= ramp[::-1]; oth[seg] += x
    # the room-tone bed under every studio stretch, never ducking, ~-60 dBFS RMS (Audio rule 3)
    rt = load(f'{FA}/Audio/ROOMTONE_studio.wav'); rt *= 10 ** (-60 / 20) / np.sqrt((rt ** 2).mean())
    for a, b in L.blocks:
        i, j = int(a * SR), int(b * SR); m = j - i
        bed = np.tile(rt, (m // len(rt) + 1, 1))[:m]
        r = int(0.02 * SR); ramp = np.linspace(0, 1, r, dtype=np.float32)[:, None]; bed[:r] *= ramp; bed[-r:] *= ramp[::-1]
        oth[i:j] += bed
    # outro bed (provisional — the score pass sets its level): cut in 10 s before the transformation, decays
    for m in L.music:
        x = load(m['path']); x *= 10 ** ((-26 - lufs(m['path'])) / 20); i = int(m['t'] * SR)
        x = x[:n - i]; x *= (1 - duck[i:i + len(x)][:, None] * (1 - 10 ** (-10 / 20))).astype(np.float32)
        r = int(2.0 * SR); x[:r] *= np.linspace(0, 1, r, dtype=np.float32)[:, None]; oth[i:i + len(x)] += x
    out = (dia + oth)[:int(L.total * SR)]
    tmp = f'{ED}/_mix_raw.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'pcm_f32le', tmp],
                   input=out.tobytes(), check=True)
    # master to -14 LUFS integrated, -1.5 dBTP (two-pass loudnorm)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', tmp, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    j = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af',
                    f'loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j["input_i"]}:measured_TP={j["input_tp"]}:'
                    f'measured_LRA={j["input_lra"]}:measured_thresh={j["input_thresh"]}:offset={j["target_offset"]}:linear=true',
                    '-ar', str(SR), f'{ED}/_mix.wav'], check=True)
    os.remove(tmp)
    return f'{ED}/_mix.wav'

# ---- context cards: entering on the word, 5.5 s, never over the other person's face (kit §12) --------------------
CARDS = [('01', 'P1_015', 'family', 1, 'L'), ('02', 'P1_022', 'talents', 1, 'L'), ('03', 'P1_030', 'pompee', 1, 'L'),
         ('04', 'P1_055', 'arsinowee', 1, 'L'), ('05', 'P1_071', 'tarsus', 1, 'R'), ('06', 'P1_096', 'thrones', 1, 'R'),
         ('07', 'P1_104', 'octavian', 1, 'L'), ('08', 'P1_106', 'vestal', 1, 'R'), ('09', 'P1_128', 'actium', 1, 'R')]
def face_at(L, fm, t):
    x = fm[min(int(t * FPS), len(fm) - 1)]
    if x is None or x[0] != 'v': return x[0] if x else '?'
    c = x[1]
    if c in BROLL: return 'broll'
    if c not in TYPE: return 'brand'
    return pose_side(c)
def card_check(L, fm):
    out = []
    for n, c, w, k, side in CARDS:
        if c == 'P1_055' and not any(x[0] == w for x in WORDS[c]['words']): t0 = L.place[c][0][0] + L.place[c][0][2]
        else: t0 = L.W(c, w, k)
        bad = [round(t0 + d / 10, 1) for d in range(56) if face_at(L, fm, t0 + d / 10) == ('H' if side == 'L' else 'G')
               or face_at(L, fm, t0 + d / 10) in ('two', 'brand')]
        out.append((n, t0, side, bad))
        if bad: flag(f'context card {n} (side {side}, {tc(t0)}) rides onto the other face / a two-up / a plate from {tc(bad[0])}')
    return out

# ---- report -----------------------------------------------------------------------------------------------------------
def tc(t): return f'{int(t // 60)}:{t % 60:05.2f}'
def report(L, fm, rs):
    lines = ['# Cleopatra P1 — assembly cut list', '',
             f'*Written by `_edit/assemble_p1.py`. Length **{tc(L.total)}**. Times are in the assembled part (opening included).*', '',
             '| at | picture | from source | frames |', '|---|---|---|---|']
    for r in rs:
        x = r['x']; t = sum(q['n'] for q in rs[:rs.index(r)]) / FPS
        if x[0] == 'v':
            what = os.path.basename(x[1]).replace('.mp4', '') + (' PUNCH' if x[4] != 1 else '') + (' **FREEZE**' if r['freeze'] else '')
            lines.append(f'| {tc(t)} | {what} | {r["i0"] / FPS:.2f}s | {r["n"]} |')
        elif x[0] == 'two': lines.append(f'| {tc(t)} | two-up {x[1]} + {x[5]} | {x[2] / FPS:.2f}s / {x[6] / FPS:.2f}s | {r["n"]} |')
        else: lines.append(f'| {tc(t)} | outro P1_134 + hold + end card | 0 | {r["n"]} |')
    fr = [r for r in rs if r['freeze'] and r['n'] > 3]
    lines += ['', '## Flags', ''] + [f'- {f}' for f in FLAGS] + \
             [f'- FREEZE {r["n"] / FPS:.2f}s on {os.path.basename(r["x"][1])} at {tc(sum(q["n"] for q in rs[:rs.index(r)]) / FPS)}' for r in fr]
    open(f'{ED}/P1_CUTLIST.md', 'w').write('\n'.join(lines) + '\n')
    json.dump(dict(total=L.total, pics=L.pics, audio=L.audio, blocks=L.blocks, place=L.place),
              open(f'{ED}/P1_assembly_timeline.json', 'w'), indent=0, default=str)
    return fr

if __name__ == '__main__':
    L = build(); fm = frame_map(L); rs = runs(fm); CARDS_AT = card_check(L, fm)
    missing = [f for f, x in enumerate(fm) if x is None]
    if missing: raise SystemExit(f'{len(missing)} frames with no picture, first at {tc(missing[0] / FPS)}')
    fr = report(L, fm, rs)
    print(f'assembled length {tc(L.total)} · {len(rs)} picture runs · {len(FLAGS)} flags · {len(fr)} freezes > 3 frames')
    for f in FLAGS: print('  ' + f)
    for r in fr: print(f'  FREEZE {r["n"] / FPS:.2f}s on {os.path.basename(r["x"][1])}')
    if PLAN: sys.exit(0)
    prep_broll()
    tmp = f'{ED}/_runs_{OW}'; os.makedirs(tmp, exist_ok=True)
    with ThreadPoolExecutor(4) as ex: files = list(ex.map(lambda kr: render_run(kr[0], kr[1], tmp), enumerate(rs)))
    open(f'{tmp}/list.txt', 'w').write(''.join(f"file '{os.path.abspath(f)}'\n" for f in files))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-c', 'copy', f'{tmp}/video.mp4'], check=True)
    wav = mix(L)
    out = f'{EP}/P1_ASSEMBLY_1080.mp4' if FULL else f'{EP}/P1_ASSEMBLY_review.mp4'
    venc = ['-c:v', 'libx264', '-preset', 'slow', '-crf', '18'] if FULL else \
           ['-c:v', 'libx264', '-preset', 'slow', '-crf', '27', '-maxrate', '700k', '-bufsize', '1400k']
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{tmp}/video.mp4', '-i', wav, '-map', '0:v', '-map', '1:a'] + venc +
                   ['-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', '-shortest', out], check=True)
    print(f'-> {out}  ({os.path.getsize(out) / 1e6:.1f} MB)')
