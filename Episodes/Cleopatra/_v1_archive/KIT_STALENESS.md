# What a fresh Mode 4 run would change in `P1_kit.md`

**Audited 2026-09-18 against every decision taken since the kit was built.** The kit is not wrong
line by line — the dialogue, provenance, durations, pose assignments and §12 are current. What has
moved is **structure**, and three of the items below are dependencies, not text edits.

**Current kit: 95 rows, 7,638 credits summed, ~8,660 with retries.**

---

## 🔴 Structural — these change the shot list, not just wording

### 1. `P1_005` — the 4s establishing wide must go · **−32 cr**
Removed by decision: the generated two-shot puts the figures at the wrong scale against the chairs,
it is inherited from the seed frame so rerolling does not fix it, and four seconds is long enough
to see it.

⚠️ **It has a dependant.** `P1_095` (the outro) says *"lift a still from `P1_005`, the establishing
wide. Already generated, 0 cr."* Deleting `P1_005` breaks that. **The outro now starts from
`frame_wide_cleopatra_marked.png`** — the seed frame, which already exists, still 0 cr. Fix both or
neither.

Removing a row also **shifts every id after it**, which is why this is a rebuild rather than a
patch.

### 2. `P1_032` and `P1_058` — the two act-transition b-rolls are redundant · **−140 cr + 2 stills**
Both carry `edit_placement: … act transition`. Act breaks are now **`BRAND_actbreak`** — fixed
furniture, 5.0s, **zero credits a part**, alternating vessel and grinding stone. These two rows
existed to *be* the break, so they go with it.

Runtime drops about 9 seconds (14s of b-roll replaced by a 5s break). The drone entry that `P1_032`
carried moves to the break.

### 3. The cold open is in the old order
The kit has the teaser, then the bumper, then `P1_004` — line 143: *"plays after the teaser and
before P1_004."* The opening is now **one built file**: `BRAND_opening.mp4`, 19.17s, disclosure card
0–4s, **hook slot 4.00–8.00**, intro 8–19.17, music unbroken, three clock strikes. The teaser is an
edit-only lift dropped into the slot, not a separate beat before a bumper.

---

## Wording — safe to fix in place

| | |
|---|---|
| `MUSIC_Sting_Transition` (lines ~1339, ~2268) | **cancelled cue.** The act break carries the theme's own strikes. |
| "the credit roll runs over the drawing" (~2140) | **there is no credit roll** — 5s transform, ~3s clean hold, then the end card. |
| §12 | already current: host name filled, placements correct. `CARD_PLACEMENTS.md` is now generated from it by `build_episode_cards.py`. |

---

## Already current — do not re-do

- All 32 of Cleopatra's `Voice:` blocks (placeless English, corrected 2026-09-18)
- Both VERIFY flags cleared; `P1_019` now 13s/130 cr, `P1_045` 10s/100 cr
- `P1_024` retagged `[D]` → `[I]`
- Every b-roll row converted to charcoal, armour error corrected
- Durations against the 3.85 syl/s model

---

## The number

| | |
|---|---|
| kit as written | ~7,638 cr |
| − establishing wide | −32 |
| − two act-transition b-rolls | −146 |
| + the two VERIFY clips lengthening | +20 |
| **rebuilt** | **~7,480 cr**, ~8,480 with retries |

Plus what left the per-part budget entirely this week: the act breaks (fixed furniture, was ~146),
`MUSIC_Sting_Transition` (−720 one-off), and the end card and plates now built by script from the
kit rather than decided at the edit.
