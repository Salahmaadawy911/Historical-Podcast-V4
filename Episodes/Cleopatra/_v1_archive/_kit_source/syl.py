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
RATE, LEAD_SEED, LEAD_CHAIN, BREAK, TAIL = 4.3, 0.8, 0.3, 0.5, 0.4
def breaks_in(line):
    return max(0, len(re.findall(r"[.!?](?=\s|$)", line)) - 1) + line.count("—")
def dur2(line, chained=False, extra=0.0):
    s = count(line)[0]
    need = (LEAD_CHAIN if chained else LEAD_SEED) + s / RATE + BREAK * breaks_in(line) + TAIL + extra
    import math
    return s, round(need, 1), min(15, max(3, math.ceil(need - 0.05)))
