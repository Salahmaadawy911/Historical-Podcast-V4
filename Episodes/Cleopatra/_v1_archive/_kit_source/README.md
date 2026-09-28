# `_kit_source/` — how P1_kit.md was rebuilt

`build.py` (the original 93-row data structure) was lost with a cloud container. This folder is the replacement, and it works the other way round: **`P1_kit.md` is the source of truth, and these scripts transform it.**

| File | What it is |
|---|---|
| `parsed.json` | snapshot of the **pre-rebuild** kit, parsed into shot blocks |
| `tags.py` | provenance tag + source for all 65 original spoken lines, keyed by **old** shot id |
| `newshots.py` | rewritten rows (the two that carried the live-event frame, the closing wide) and the two new shots |
| `broll.py` | the five former Pexels rows, as charcoal b-roll |
| `broll2.py` | the ten originally-generated b-roll rows, converted to charcoal + armour corrected |
| `build.py` | renumbers, applies tags and models, emits `shotlist.md` |
| `assemble.py` | writes the head sections + shotlist + tail into `P1_kit.md` |
| `apply_broll2.py` | applies `broll2.py` over the assembled kit |
| `syl.py` | the duration model — syllables ÷ 3.85 + 1s per sentence break + 0.5s tail |

## ⚠️ Do not re-run the pipeline blind

`parsed.json` is a snapshot of the **old** kit. Re-running `build.py` + `assemble.py` now would regenerate from that stale snapshot and discard everything done since. If the kit needs another structural pass, re-parse the current `P1_kit.md` first.

For ordinary edits, edit `P1_kit.md` directly. These scripts exist for structural passes — renumbering, retagging, a format migration — not for changing a line.

## Shot numbering

Part 1 went from 93 to 95 shots in this rebuild. Two were added: a 4s silent establishing wide in the cold open, and the host's hand-off before the closing wide. Everything from the old `P1_005` onward shifted by one, then by two after the hand-off. `build_stats.json` holds the full old → new map.
