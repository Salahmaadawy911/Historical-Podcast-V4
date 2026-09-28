#!/usr/bin/env python3
"""
sources_audit.py — check the end card's PRIMARY SOURCES block against the kit's
provenance tags.

Why an audit and not a generator: the tags name their sources in prose, inside a
sentence explaining the claim ("Roller, *Cleopatra: A Biography*; Chauveau"), not as
structured citations. Machine-extracting that yields a long, inconsistent list with
every passing mention in it — which is not what the card is for. The card is a curated
claim; the tags are the evidence. So the script audits the relationship instead:

  - anything ON the card that appears in NO tag  -> the card is overclaiming
  - anything in the tags that is NOT on the card -> a candidate the card may be missing

Run it whenever the kit's lines change. Fix the card by hand.
"""
import re, sys, collections

AUTHORS = ("Plutarch|Cassius Dio|Caesar|Cicero|Suetonius|Horace|Propertius|Appian|"
           "Josephus|Strabo|Pliny|Roller|Chauveau|Grant|Schiff|Jones|Burstein")
# ⚠️ Starter list, weighted to the Roman world where the first guest sat. For another era, add the
# era's authors here (or they are still caught as italic work titles). Names on the card are added
# automatically at run time — see main().
ABBREV  = {"Ant.":"Plutarch, Life of Antony", "Att.":"Cicero, Letters to Atticus",
           "Caes.":"Plutarch, Life of Caesar", "Pomp.":"Plutarch, Life of Pompey"}

def _is_title(t):
    """An italic span is a work title, not a stray phrase."""
    if any(c in t for c in "`—\u2014[]()"): return False
    if " - " in t or t.endswith("."): return False
    if t[0].isdigit(): return False
    if len(t.split()) > 6: return False
    if not t[0].isupper(): return False
    return True

def works(kit_text):
    out=collections.Counter()
    for line in kit_text.splitlines():
        if "**provenance:**" not in line: continue
        body=line.split("**provenance:**",1)[1]
        for m in re.findall(r"\*([^*]{3,60})\*", body):
            m=m.strip()
            if m in ABBREV: out[ABBREV[m]]+=1
            elif _is_title(m): out[m]+=1
        for m in re.findall(r"\b("+AUTHORS+r")\b", body): out[m]+=1
    return out

def main(kit_path, card_lines):
    global AUTHORS
    extra=[re.escape(l.split(",")[0].strip()) for l in card_lines if "," in l]
    if extra: AUTHORS = AUTHORS + "|" + "|".join(sorted(set(extra)))
    txt=open(kit_path,encoding="utf-8").read()
    w=works(txt)
    card=" ".join(card_lines)
    print(f"{sum(1 for l in txt.splitlines() if '**provenance:**' in l)} provenance tags scanned\n")
    print("Mentioned in the tags:")
    for k,v in sorted(w.items(), key=lambda kv:(-kv[1],kv[0])):
        mark = "on card" if any(p and p.lower() in card.lower() for p in [k]) else "NOT ON CARD"
        print(f"  {v:3d} x  {k:<46s} {mark}")
    print("\nOn the card but in no tag:")
    miss=[]
    for line in card_lines:
        for item in re.split(r"\s*·\s*", line):
            item=re.sub(r"^(the|The)\s+","",item.strip().rstrip(","))
            if not item: continue
            if item.lower() in txt.lower(): continue
            # try the bare title after "Author, "
            tail=item.split(", ",1)[-1]
            if tail.lower() in txt.lower(): continue
            miss.append(item)
    print("  " + ("\n  ".join(miss) if miss else "nothing — every entry on the card is cited in at least one tag"))

if __name__=="__main__":
    # usage: sources_audit.py <P<n>_kit.md> [card_data_p<n>.json]
    # The card is read from the episode's card_data json — never a list baked into this file
    # (until 2026-09-22 Cleopatra's list was hard-coded here, which would have audited every
    # future guest against her sources).
    import json, os
    kit = sys.argv[1] if len(sys.argv) > 1 else "P1_kit.md"
    data = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(kit)), "card_data_p1.json")
    CARD = json.load(open(data, encoding="utf-8")).get("sources", []) if os.path.exists(data) else []
    if not CARD: print("(no card_data yet — listing what the tags cite, for curating the card)\n")
    main(kit, CARD)
