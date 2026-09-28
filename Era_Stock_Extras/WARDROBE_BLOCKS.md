# Era Stock Extras — wardrobe blocks

**These replaced the character sheets, and the change was not cosmetic.**

Two findings retired the sheets together:

1. **B-roll is charcoal and graphite drawing on toned paper.** A photoreal character sheet cannot drive a charcoal frame, so the sheets had nothing left to generate.
2. **Passing a reference image for anonymous extras produces rows of identical faces.** Measured: "the nearest man matching the reference" returned roughly twenty clone faces. Anonymous crowds are generated from description alone, with no reference.

An era extra is therefore a **fixed block of wardrobe text**, pasted byte-identical into every b-roll still prompt that needs it, exactly the way `LOCK` is pasted into every dialogue prompt. It fixes continuity and period accuracy at once, and unlike a reference image it cannot clone a face.

## The gate this exists to enforce

`roman_legionary.png` was generated showing **lorica segmentata** — banded iron plate, Imperial kit, generally dated to the early first century **AD**. Cleopatra died in 30 BC. At Actium the legions wore **lorica hamata**, chain mail, with Montefortino-type bronze helmets. The asset was roughly fifty years early, and it came from a prompt written in this project that nobody period-checked.

Retiring the sheets **moves** that gate, it does not relax it. The same error would now land in a block instead of a PNG, and charcoal hides fine detail but mail against banded plate is a silhouette and texture difference that still reads.

Before registering a block: establish the **date** of the scenes it appears in, verify costume and equipment against that date rather than against the general image of the culture, state the evidence in one line, and **name what is absent** — models default to the famous silhouette, so the block must exclude it explicitly or the default wins.

Also: **describe crowds by arrangement, not by count.** "A column" rendered as a line abreast; "seen from behind, one rank behind another, receding into the distance" rendered correctly.

---

## `legionary_late_republic`

For any arc touching the Roman military sphere c. 100–30 BC: invasions, sieges, escorts, advancing-forces threat b-roll.

```
Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool
tunics, plain bronze helmets with a small flared neck guard and hinged cheek pieces, deep red
wool cloaks, wide leather belts with hanging studded straps, heavy open-laced leather sandals.
No metal shin guards. No plate or banded armour.
```

*Evidence: lorica hamata with Montefortino-type helmets is the standard reconstruction for Republican legions through the Actium period. Lorica segmentata is an Imperial development and does not belong before the first century AD.*

---

## Retired image assets

`roman_legionary.png`, `court_attendant.png` and `antony.png` were moved to `_to_delete/retired_character_sheets/` in the kling.ai rebuild. They are superseded by wardrobe blocks and charcoal start frames.

**Antony's casting prompt was never saved anywhere** — only the generated PNG existed, and it is now retired. If he is ever cast as a guest in his own right he will appear in the studio photoreal and will need a fresh character sheet, written from scratch through Mode 2 with the period gate applied.

That is the better outcome. The retired image showed a brown leather cuirass with bronze fittings, which is defensible for a Roman commander c. 40–30 BC but was **never actually verified** — the same unchecked path that produced the legionary error. Starting over forces the check.
