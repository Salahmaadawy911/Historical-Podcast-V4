# Duration model for Kling talking clips.
# The model speaks at a fixed articulation rate (~3.85 syllables/sec) and pads
# the remainder with pauses. Duration is therefore set by syllable count, not
# word count. floor = syllables/3.85 + 1s per sentence break + 0.5s tail.
# Generate at floor + ~1s. Never state pace in a prompt; duration is the control.
import re
def syl(word):
    w=re.sub(r"[^a-z']",'',word.lower())
    if not w: return 0
    w=re.sub(r"e$",'',w) if not re.search(r"[aeiouy]e$",w) and len(w)>2 else w
    g=re.findall(r"[aeiouy]+",w); n=len(g)
    if re.search(r"[^aeiouy]le$",word.lower()): n+=1
    return max(1,n)
def count(line):
    words=re.findall(r"[A-Za-z']+",line)
    return sum(syl(w) for w in words), len(re.findall(r"[.!?]", line))
def dur(line, pad=1.0):
    s,sent=count(line)
    breaks=max(0,sent-1)
    floor=s/3.85 + breaks*1.0 + 0.5
    return s, sent, round(floor,1), min(15, max(3, round(floor+pad)))

# ---- v2, 2026-09-21: recalibrated on six measured Kling Turbo clips (P1_004/006/007/055/057) ----
# measured: articulation 4.1-5.3 syl/s (mean ~4.5); lead-in 0.7-1.0 s from a seed frame, 0.3 s chained;
# the model spends any slack as one long pause, so break allowance is the natural minimum, not a pad.
# ---- v3, 2026-09-24: BREAK 0.5 -> 1.0. Measured on today's takes: T1_B (P1_013) 1.12 s at its sentence break,
# P1_020 (beat map) 1.57 s and 0.96 s, and the earlier P1_008 1.1 / 0.6 / 1.2 s. With 0.5 s allowed, two clips in a
# row ran their speech to the LAST FRAME (no tail to cut on). Surplus silence is trimmed in the edit; a missing tail
# means a regeneration. Rate (4.3-4.5 syl/s) and lead-ins were confirmed; only the break allowance moved.
# 2026-09-25 check on 7 kept takes: every one ends 0.25-0.6 s after its last word; spare time lands as a long
# pause or a silent lead-in (P1_046: 3.2 s). Kept v3 — silence is an edit trim, a short clip is a regeneration.
# v4, 2026-09-25: BREAK 1.0 -> 1.3. P1_015 (2 breaks, 12 s) ran out of time — her pauses measured 1.45 and 1.6 s and
# the last word was cut with her mouth open (Salah). Measured sentence pauses across kept takes average ~1.3 s (L24).
RATE, LEAD_SEED, LEAD_CHAIN, BREAK, TAIL = 4.3, 0.8, 0.3, 1.3, 0.4
def breaks_in(line):
    return max(0, len(re.findall(r"[.!?](?=\s|$)", line)) - 1) + line.count("—")
def dur2(line, chained=False, extra=0.0):
    s = count(line)[0]
    need = (LEAD_CHAIN if chained else LEAD_SEED) + s / RATE + BREAK * breaks_in(line) + TAIL + extra
    import math
    # 2026-09-25: no rounding down — P1_016 (need 4.06 s → 4 s) ended 0.15 s after its last word (L21)
    if need >= 9: need += 0.5   # v4: long lines drift slower than 4.3 syl/s (P1_015 4.1) — half a second of margin (L24)
    return s, round(need, 1), min(15, max(3, math.ceil(need + 0.1)))
