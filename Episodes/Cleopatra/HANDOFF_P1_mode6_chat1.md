# Handoff — Cleopatra Part 1, Mode 6 chat 1 (2026-09-28)

A cloud session ran the start of Mode 6 on Cleopatra Part 1: the opening check (`batch_check.py`), the join grades,
and a scripted assembly. The work is merged to `main` in PR #3. The assembly has **two faults Salah found on review**,
and they are not fixed yet (section 4). **Read section 4 before touching the cut.**

---

## 1. State at handoff

| | |
|---|---|
| Voice pass | done — 93 of 93 talking clips in `Voice/P1/done/` |
| Opening check | run over all 130 clips (section 2) |
| Join grades | measured → `Shots/_measure/JOIN_GRADES.md` |
| Assembly | `Episodes/Cleopatra/P1_ASSEMBLY_review.mp4` — 10:01, 960×540 review proxy, −14 LUFS, 27 MB. **Not signed off; needs rework (section 4)** |
| Cut list | `Episodes/Cleopatra/_edit/P1_CUTLIST.md` (every picture run plus the flags) |
| Merged | PR #3 into `main`. One later commit, which removes a duplicate status paragraph in `NEXT_STEPS.md`, is on branch `claude/eloquent-franklin-585bx1` only, not yet in `main` |
| Running Order | republished (version 34) with the assembly step and a 28 Sep change-log entry |

The assembly contains picture, dialogue, room tone, b-roll ambience, both act breaks and the outro (P1_134 + a 3 s hold
+ a dissolve to `BRAND_endcard_p1.mp4`). It does **not** contain the hook render (the fixed `BRAND_opening.mp4` is in
place), cards, lower thirds, pull-quotes, subscribe, subtitles, source credits or drones. `MUSIC_Outro_Bed` is placed
provisionally, starting 10 s before P1_134. The mix peaks at 0.1 dBFS because the proxy has no limiter.

---

## 2. The opening check — results and tool fixes

### Tool bugs found and fixed (L60)
- **`batch_check.py` printed `cam ?px ✓` for every clip.** `cam_check.py` had crashed (numpy was not installed in the
  cloud container) and the script read "no measurement" as a pass. A check that cannot run now reports
  `CAM-CHECK-FAILED`.
- **The LOUD-SPAN step reused the variable `st`**, which also holds the start frame. As a result, every host clip was
  measured with the guest's check box. The variable is renamed.
- **B-roll and the outro were measured for camera moves** and falsely flagged (they move by design). They are now named
  and skipped.
- **TIGHT now says which case it is.** "ends in silence" means the last 0.12 s is below −55 dB. "STILL SOUNDING at the
  last frame" means listen to it. 18 of 19 TIGHT clips ended in silence.

### Findings
- **P1_095: CAMERA-MOVED, 27 px** (the frame slides and re-frames). **It needs a retake** from the round sheet, row
  as is. It is the first v3 drift in 105 studio clips (L61). The current take stands in the cut until then.
- **P1_090** — *"kingdoms"* is still sounding at the last frame (−39.5 dB). Listen, and if it is clipped, retake it
  1 s longer.
- **P1_055** — *"his triumph"* would not align (it may be clipped). It sits under b-roll P1_056. Listen to it.
- **P1_128** is borderline (−53 dB at the end).
- **PAUSE > 2 s** on 30 talking clips. These are the pauses Kling generated, and Mode 4's duration model
  budgets for them on purpose.
- **LEAD > 1.5 s** on P1_046 (2.2 s) and P1_123 (1.6 s); assembly starts both at the first word.
- There were no QUIET, LOUD-SPAN, CORNER or NO-AUDIO flags.

### `chain_frames.py` side effect
`chain_frames.py` re-extracted `Shots/start_frames/*.png`, which are not in git, when it measured the joins. Those
copies were deleted; only `JOIN_GRADES.md` was kept.

---

## 3. How the assembly was built

### Environment (cloud container)
Nothing was preinstalled. The session installed `ffmpeg` with apt and `numpy pillow pocketsphinx` with pip. The model
hosts for Whisper (HuggingFace, Azure) are blocked by the network policy. **pocketsphinx** ships its English model
inside the pip package, so it was used for **forced alignment**. A SessionStart hook could install all of this
automatically.

### Scripts (per part, like `_kit_source/build_p1_kit.py`)
- **`_edit/prep_p1.py`**
  - Converts each `Voice/P1/done/*.mp3` to `_edit/audio/*.wav` with the 1152-sample head trim and loudnorm to −19
    LUFS (Mode 6 Audio rules 1–2).
  - Aligns the prompt's spoken words (respellings included) against each Kling take and writes
    `_edit/words_p1.json`, word start and end times in source seconds.
  - Respellings (*Seezer, Antonee, Tolemies, Arsinowee*…) and `names.dict` entries are added to the aligner's
    dictionary.
- **`_edit/assemble_p1.py`**
  - One line per kit placement, each time taken from the aligned words (`L.W('P1_018','why')`).
  - `--plan` writes the cut list and the flags only.
  - With no flag it renders the 540p proxy; `--full` renders 1080p (meant for the Mac).
  - It also compounds the join grades along each chain, normalises each b-roll clip against its own first frame, lays
    the room-tone bed (−60 dBFS RMS) under the studio stretches, ducks b-roll ambience by 8 dB under dialogue, and does
    a two-pass loudnorm to −14 LUFS.
  - It checks every context card against the resolved picture: a card must not sit over the other face, a two-up or
    a plate.
- `_edit/.gitignore` keeps the regenerable intermediates (audio, b-roll, render runs) out of git.

### Placement changes made by measurement (L62)
- **Card 05 / P1_072.** The kit said to cut to her on *"to his enemy"*, but the 3 s P1_072 cannot reach it (a 1.2 s
  freeze). Measured, card 05 has already left before *"He had heard"*, so the cut moved there.
- **Card 06 / P1_097.** The cut back to her happens at the end of the b-roll (card 06 is already gone), not on
  *"with"*.
- **Cards 03, 07 and 09.** The card's word is the speaker's first word, so the picture cuts *with* the voice instead
  of on the usual J-cut. Otherwise the other face would sit under the card's first frames.
- **Two-ups #3 and #6.** The hold after the line is capped at what P1_062 and P1_101 actually have.
- **Card 07** would touch act break 2 by 0.23 s. It should leave about 0.25 s early in the edit (not done yet).
- Mode 4 got a rule for this: write the constraint, not only the word; size covering reactions for the span they
  cover; take the two-up hold from the take's own tail.

### Pause trimming (L63) — first render, then changed
- **First render (9:09).** Every pause over 1.2 s was trimmed and each visible trim got a PUNCH. That punched almost
  every take, **including P1_002, direct address, which the kit forbids.**
- **Second render (10:01, the one in the repo).**
  - Pauses on picture are trimmed only past 2 s, to 0.8 s, each with a PUNCH that alternates between trims.
  - Pauses in voices heard off picture keep the 1.2 s rule.
  - P1_002 and P1_003 are never trimmed. P1_003's 2.6 s still pause before the turn is flagged for L38's retime.

---

## 4. ⚠️ Open problems Salah raised on review — fix these before anything else

> *"What was the reason of cutting from the shot (which broke chained shots) and also some of the shots were zoomed in.
> It feels like the edit mode doesn't know how the shots were generated and why."*

**Salah is right. The assembly followed the kit's edit instructions but not the reasons behind how the shots were
generated.**

### 4a. Chained joins were broken
The script set a 0.45–1.0 s target for the gap between speakers and let it override the chain. When a listening
reaction ran longer than the voice under it, the script **cut the reaction early** and brought the chained clip in
partway through, not on its first frame. That undoes the chain's purpose: the chained clip was generated from the
reaction's last frame so the join is invisible.

Joins moved: 18 in total, most of them cut early. The largest:

| join | cut early by |
|---|---|
| P1_010 → P1_012 | 3.1 s |
| P1_131 → P1_132 | 2.3 s |
| P1_083 → P1_084 | 2.0 s |
| P1_060 → P1_062 | 1.9 s |
| P1_069 → P1_070 | 1.7 s |
| P1_091 → P1_093 | 1.5 s |
| P1_109 → P1_111 | 1.2 s |
| P1_053 → P1_055 | 1.1 s |

Seeded exact joins broke the same way, including P1_005 → P1_006, P1_019 → P1_020, P1_119 → P1_120 and
P1_126 → P1_127: those reactions end on the same seed image the next clip starts from. P1_099 → P1_101 went the
other way (+0.37 s, a freeze on the reaction). The full list is in `P1_CUTLIST.md` under Flags. The cut list reported
every one of these as "chained join moved", but it was treated as information rather than a failure.

### 4b. Punch-ins the kit never placed
The kit places only **two** PUNCHes, on the split seams P1_088 and P1_121. The assembly added **26 more** (28 punched runs in the cut list) to hide
pause trims. The pauses were long *by design*: duration model v4 budgets 1.3 s per sentence break, and Kling fills the
clip (L13, L24). Three chained reactions (P1_053, P1_091, P1_099) also inherited the zoomed framing from the take they
continue.

### 4c. Root cause
Mode 6 says to *level* chained joins with `JOIN_GRADES.md`, but **nowhere says a chained join is never moved**. It
also has no section on why the shots are the way they are. So the script treated chains as preferences.

### 4d. Proposed fix (agreed in principle, not yet done)
1. **Chains and seeded exact joins are fixed.**
   - A reaction plays to its last frame and the chained clip starts on frame 0.
   - Spare time is absorbed by where the audio-only host line sits inside the reaction.
   - A silence that still comes out too long is **flagged for Salah**, never cut.
2. **PUNCH only where the kit's `edit_placement` names one.** Pauses on picture are not punched.
3. **Mode 6 gets a "how the shots were made" section to read before any cut:**
   - the chain table;
   - the end-frame rule (L44), meaning seeded reactions join exactly;
   - why durations are generous (L13, L24);
   - which rows the kit marked for PUNCH;
   - that the turn is cut to her (L40);
   - plus a LESSONS row (next number L64).
4. **A gate in `assemble_p1.py --plan`.** It fails when a chain or seeded join moves, or when a PUNCH appears that the
   kit did not place.

### 4e. Salah's decision, still pending
The opening check flagged 30 takes with pauses over 2 s; most are on picture. Two options:
- **(a)** Leave them all as generated and list their times so Salah can judge each one while watching.
- **(b)** Trim only where the kit already has a cutaway near the pause.

Once decided: apply the fix, re-run `--plan` (it must come out clean), re-render and push.

---

## 5. Other items still open for Part 1
- **Retake P1_095**, and listen to P1_090 and P1_055 (P1_128 is borderline).
- **Card 07** must leave about 0.25 s early.
- **P1_003:** retime the turn (L38).
- **P1_099:** a 0.33 s hold on her still face (the P1_100 line is longer than the reaction). Re-check it after fix 4d.
- **The rest of Mode 6**, after the cut is signed off:
  - re-pick the hook from the cut and run `hook_build.py` (if P1_008 stays the hook, drop pull-quote 01);
  - cards, lower thirds, pull-quotes, subscribe, `[D]` credits, drones;
  - subtitles and `P1_captions.srt`;
  - clean and titled masters, with a limiter;
  - `P1_TIMECODES.txt`, `P1_EDIT_NOTES.md`, `publish_sheet.py`.
- **Still blocking publishing:** the thumbnail rebuild and the playlist `TODO` in `publish_defaults.json`.

---

## 6. Files changed in this chat
- `Fixed_Assets/tools/batch_check.py` — the fixes in section 2.
- `Fixed_Assets/LESSONS.md` — L60 (silent check failure), L61 (P1_095 drift), L62 (placements resolved by
  measurement), L63 (pause trims and punches). **L63's "trim past 2 s with a PUNCH" is itself superseded by 4b** and
  should be marked so when the fix lands.
- `skill_mode6_edit.md`:
  - a Tools line;
  - the new batch_check flags;
  - an assembly-scripts paragraph in §3 (this also describes the chain behaviour that 4a says is wrong — rewrite it);
  - the pause rule.
- `skill_mode4_produce.md` — the L62 rule under Context cards (write the constraint, not only the word).
- `NEXT_STEPS.md` — the current status paragraph.
- New files:
  - `Episodes/Cleopatra/Shots/_measure/JOIN_GRADES.md`
  - `Episodes/Cleopatra/_edit/` (`prep_p1.py`, `assemble_p1.py`, `words_p1.json`, `P1_CUTLIST.md`,
    `P1_assembly_timeline.json`, `.gitignore`)
  - `Episodes/Cleopatra/P1_ASSEMBLY_review.mp4`
