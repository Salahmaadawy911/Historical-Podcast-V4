# Cleanup pass — 2026-09-18

**I cannot delete files on your machine** — the Linux workspace on this device will not start, so
the bridge can write files but not remove them. Everything below is a list for you to action in
Finder. Nothing here is needed to produce Part 1.

**Total: roughly 95 MB, none of it load-bearing.**

---

## Tier 1 — delete, no checking needed

Verified: **no `.md` file in the project references any of these.** I checked before listing them,
rather than assuming.

### `Claude outputs/` — delete the whole folder · ~46 MB
Eighteen decision screenshots: thumbnail variants, sand options, end-card options, plate previews,
an intro preview GIF. Every one of them existed to answer a question that is now answered, and the
answer is in the built asset. **The folder is not referenced anywhere.**

### `Episodes/Cleopatra/tests/` — delete the whole folder · ~35 MB
`T1`, `T2A`, `T3_ClipA`, `T3_ClipB`, `T4`, `TEST_COMBINED_v3`, two extracted end frames, and
`COMBINED_TEST_v2.md`. **The test programme is CLOSED** — camera lock, gesture, the voice pass,
b-roll start frames, the charcoal style, b-roll under motion and the silent reaction all passed,
and every finding is written into the skills with its measurements. The clips proved their points.

### `Fixed_Assets/Branding/` — three superseded experiments · ~12 MB
`ACTBREAK_clock_test.mp4` · `ACTBREAK_look.mp4` · `ACTBREAK_v2.mp4`
The look tests that got us to the act break. Superseded by the finished
`BRAND_actbreak_vessel.mp4` and `BRAND_actbreak_stone.mp4`.

### `Fixed_Assets/Branding/` — decision screenshots · ~25 MB
`lowerthird_paper_options.png` · `lowerthird_paper_sizes.png` · `lowerthird_paper_sides.png` ·
`lowerthird_mockup.png` · `plate_placement_guide.png` · `panel_mark_check.png` · `paper_check.png` ·
`endcard_guide.png` · `cam3_wide_branded_reference.png` · `intro_source/intro_keyframes.png`

All comparison sheets from decisions now settled and built. The geometry that came out of them is
recorded as numbers in `PLATE_SPEC.md` and `SERIES_FURNITURE.md`, which is the durable form.

### Build artefacts and a stale backup
`Episodes/Cleopatra/_kit_source/__pycache__/` (whole folder) · `Fixed_Assets/Audio/AUDIO_PROMPTS.md.bak`

### The renamed archive
`_PENDING_CHANGES.md` — **delete only after confirming `DECISIONS_ARCHIVE.md` is there.** Same
content, corrected header. The old name said "pending" while the file's own first line said the
opposite, which is how it ended up on a delete list in the first place.

---

## Tier 2 — look before deleting

`Fixed_Assets/Branding/thumbnail_reference.png` and `thumbnail_reference_sizes.png` · ~5.6 MB
No `.md` references them by that name, but `THUMBNAIL_SYSTEM.md` exists and the approved thumbnail
treatment came from somewhere. If they are the approved reference build, keep them and add a line
to `THUMBNAIL_SYSTEM.md` naming them. If they are just another options sheet, delete.

---

## 🔴 Tier 3 — do NOT delete

| | why |
|---|---|
| `Fixed_Assets/Audio/_raw_takes/` | every alternate, **including the rejected ones**, plus `DRONE_HIGH_detune_test.wav` and `TICK_candidates.wav`. If a cue is ever re-cut, the alternates are worth more than the prompt. |
| `doorway.mp4`, `hills.mp4`, `hand.mp4`, `vessel.mp4` | the intro draw-on sources. `BRAND_bumper_in` is rebuildable from them and from nothing else. |
| `stone_4s.mp4`, `vessel_4s.mp4` | the raw act-break generations. The finished breaks are **derived** from them by `paper_restore.py`; lose these and the correction cannot be re-run. |
| everything in `intro_source/` | every build script in the project. |
| `DECISIONS_ARCHIVE.md` | the evidence behind rules the skills state flatly. |
| `KLING_MIGRATION.md` | it is not a migration note — it holds the **commercial-use licence position** (the Paid Services Agreement grants commercial use) and the privacy analysis. That is the show's legal footing. |
| seed frames, pose variants, `frame_wide_*_marked.png` | the whole identity system. |

---

## What is deliberately NOT being done yet — the skill compression

`skill_mode4_produce.md` is 74 KB, `STUDIO_ASSETS.md` and `SERIES_FURNITURE.md` 44 KB each. Trimming
them is the other half of this pass and **it should wait until Part 1 has actually been produced.**

**The reason is that Part 1's production run is the only thing that reveals which parts of Mode 4
are load-bearing.** Trimming a production skill before ever running a production is guessing, and
the failure is silent and permanent: a rule loses its reasoning, and six weeks later a session
overrides it because it reads as arbitrary. That has already happened three times in this project —
the establishing wide, the accent rule, and the VERIFY flags all came back after being settled.

When it is done, the test is the one already in `NEXT_STEPS.md` §A11 — *would deleting this let
someone repeat a mistake that cost real credits or real credibility?* — and the move is **relocate,
not delete**: reasoning goes to `DECISIONS_ARCHIVE.md` and the skill keeps the one-line rule with a
pointer. That is what the archive is for.
