# NEXT STEPS

> 📋 **Discussion queue — `DISCUSSION_QUEUE.md`: all 7 points settled (2026-09-23).** ⏰ **Next: the two reminders at the end of the queue** — plan all test takes together (T1–T6), then the Part 1 script decisions (incl. rewriting Part 1's §9 to Mode 4 §15 before its publish sheet is built).
> 🔁 **DECIDED 2026-09-23: rerun Cleopatra from Mode 1** — see **B5** below. The process is mapped in the artifact **The Running Order** (https://claude.ai/artifact/L98t6WjsEfE9G2XuFiHVP7) — **republish it whenever the process changes** (Salah: *"keep it updated always so i can follow up"*).

**Where we are (2026-09-28, Mode 6 chat 1): Cleopatra Part 1 — voice pass done (93/93), opening check run, the
assembly is cut** → `Episodes/Cleopatra/P1_ASSEMBLY_review.mp4` (9:09, 540p review proxy; `--full` rebuilds 1080p on
the Mac), cut list `_edit/P1_CUTLIST.md`. **Waiting on Salah: watch it and sign off the cut** (or list changes — they go
into `_edit/assemble_p1.py`, one line per placement, and the cut is re-rendered).
**Open before the cut is locked:** (1) **retake `P1_095`** — camera moved 27 px (round sheet row as is, v3); (2) listen
to the end of **`P1_090`** (*"kingdoms"* still sounding at the last frame) and **`P1_055`** (*"his triumph"* would not
align); `P1_128` is borderline. (3) Card 07 needs to leave ~0.25 s early (it would touch the act break).
**Then the rest of Mode 6 (same or next chat):** re-pick the hook from the cut → `hook_build.py`; cards, lower thirds,
pull-quotes, subscribe, `[D]` credits, drones, subtitles; two masters; `P1_captions.srt`, `P1_TIMECODES.txt`,
`P1_EDIT_NOTES.md`, `publish_sheet.py`. Thumbnail rebuild and the playlist `TODO` still block publishing.
**Cloud sessions need** `apt-get install -y ffmpeg` and `pip install numpy pillow pocketsphinx` first (none are
preinstalled — see Mode 6 *Tools*); a SessionStart hook would do it automatically.
The B5 log below is the history of how Part 1 got here.

Project-wide work first — everything here is reused by every episode, so a mistake
compounds. Guest-specific work is Part B and waits.

---

# PART A — PROJECT-WIDE

## A1. Generation settings — LOCKED
Registered in `STUDIO_ASSETS.md` (current): **kling.ai**, Kling 3.0 Turbo / Standard by shot type, 1080p (720p for
audio-only talking clips), **camera chip OFF** with prompt structure v3, Seedream 5.0 for studio frames, Kling image
3.0 for b-roll stills. (This item once read "Higgsfield, prompt enhancer ON, Seedream for stills" — all superseded.)
- [ ] Record any exposed creativity/cfg value the first time it is seen

## A2. Brand — COMPLETE
**History Answers Back** — التاريخ يرد. Symbol, mark, stacked, wordmark, avatar, palette —
all final in `Fixed_Assets/Branding/`, registered in `STUDIO_ASSETS.md`.
`cam3_wide.png` rebuilt with a blank lit panel; the mark is composited in the edit at fixed
coordinates. Superseded drafts have been deleted; the final set in `Branding/` is the only version.

## A3. Audio — SUPERSEDED by A9 below

Settled and still true: **ElevenLabs Starter ($6)** covers the voice pass, the score and the
effects under one licence, and **the commercial licence survives cancellation** — *"you will still
have a commercial license to use whatever you generated during that subscription forever."* The
free tier is the trap: its output always requires attribution and cannot be relicensed.

Live status is in **A9**. Everything else in the old A3 — six-take room tone, crossfade assembly,
Kling as a candidate source — is obsolete: the room tone is one seamless looping take, the source
is settled, and the method is in `Fixed_Assets/Audio/GENERATE_THESE.md`.

**Do not generate movement foley.** That decision stands. Generated foley varies clip to clip and is
harder to cut around than silence; the room-tone bed carries the space.

**Pexels is gone.** All fifteen b-roll shots are generated charcoal on Turbo with audio on, so each
carries its own ambience. The bed matters *more* than before, not less: the ElevenLabs pass strips
the studio tone out of every dialogue clip, so without it the whole part sounds vacuum-sealed.

## A4. Series furniture — `BRAND_*` and the bumpers

**Full specs, the placement map and the build order are in `Fixed_Assets/SERIES_FURNITURE.md`.**

- [x] ~~`BRAND_bumper_in`~~ — **DONE**, and superseded by **`BRAND_opening.mp4`** (19.17s: hook slot
      plus intro, music unbroken). See A8.
- [ ] `BRAND_bumper_out` — the studio two-shot transforming into a charcoal drawing of itself.
      Format **tested and approved**; built per part from `frame_wide_[name]_marked.png`, ~43 cr.
      **Since 2026-09-18 this is the only place the two-shot appears** — the 4s establishing wide
      was cut from the cold open (figure-to-chair scale fault, inherited from the seed frame and
      not fixable by rerolling), taking 32 cr a part out of the kit with it.
- [x] ~~`BRAND_disclosure`~~ — **DONE**, folded into `BRAND_opening`. See A8.
- [x] ~~`BRAND_actbreak`~~ — **DONE 2026-09-18.** Two 5.0s clips, vessel and grinding stone, in
      `Branding/`. Fixed furniture, **zero credits a part**, and it killed `MUSIC_Sting_Transition`.
- [x] ~~`BRAND_subscribe`~~ — **DONE.** 4s lower third with alpha, `.mov` (QuickTime Animation) and
      `.webm`. No bell, and the reasoning is in `SERIES_FURNITURE.md` — it is a UI icon in a paper
      identity, and since April 2026 the bell no longer guarantees push delivery anyway.
- [x] ~~`BRAND_endcard`, `BRAND_composite`~~ — **DONE.** ⚠️ **Design fixed, render per part.** The
      builders live in `Branding/intro_source/`; the renders and `card_data_p1.json` live in
      `Episodes/<Guest>/`. `sources_audit.py` checks the card's source list against the kit's
      provenance tags before every render — its first run found four cited sources missing from the
      card.
- [ ] `BRAND_lowerthird`, `BRAND_pullquote` — **the last unbuilt motion graphics.** Treatment
      approved, plates built, geometry fixed in `STUDIO_ASSETS.md`, `SFX_plate` made and waiting.
      Text comes from the kit's §12, never invented at the edit.

## A5. Subscription — DECIDED: do not subscribe yet
**Credits do not roll over.** That changes the question from which tier to whether to
commit at all, because unspent credits are simply lost at month end.

Seedance is dropped — one model, one rate, no discount question.

The numbers, at 2.5 credits/second for Kling 3.0 Pro at 1080p:
- 6000 credits / $250 buys **2,400 generated seconds** a month
- $250 spent on fal pay-per-use buys **1,488 seconds** at $0.168/s
- So the subscription wins above roughly **1,500 generated seconds a month**, and loses below it

A part is somewhere near 750 generated seconds before retakes — finished runtime plus the
cutaways, which cost a generation but add no runtime. Two parts a month clears the bar.
One does not.

**Produce Part 1 on the credits already in the account, count what it actually costs, then
decide.** Committing to a non-refundable monthly spend before a single part exists means
guessing at consumption during exactly the phase where retakes are least predictable. One
real part replaces the guess with a number.
- [ ] Record actual credits consumed producing Part 1, retakes included

## A5b. Testing programme — CLOSED

Platform is **kling.ai**. Rates: Turbo 10 cr/s; Standard 3.0 12 cr/s with audio, **8 cr/s with audio off**.

**All gating tests passed. Nothing in the pipeline is blocked on a test.**
*(This table is the 2026-09-18 record. Some settings in it were later replaced — the preset + lock (now prompt structure
v3, chip off, L51) and the wide (removed). Current rules: the skills; what replaced what: `DECISIONS_ARCHIVE.md` R1–R9.)*

| Test | Result |
|---|---|
| Camera lock, `P1_054` 10s Turbo | **PASS** — frame held. Preset and the rewritten `LOCK` paragraph applied together; keep both. |
| Camera lock on Standard 3.0 | **PASS** — first vs last frame across static regions: 1.44 / 1.69 / 1.28 mean abs diff, under 0.2% of pixels moving more than 25. No per-model camera treatment needed. |
| Gesture without the prompt enhancer | **PASS** — movement natural. Gesture paragraphs stand as written. |
| ElevenLabs voice pass | **PASS** — picture and lip-sync untouched. Adopted. |
| B-roll start frame (Kling image gen) | **PASS** — no character sheet needed for anonymous extras. |
| Style: charcoal sketch vs photoreal | **SKETCH** — decided on measurement, not taste. Photoreal sat almost on the studio's own value and saturation numbers; the sketch reads as a deliberate shift. |
| B-roll video, 8s | **PASS** — style survived motion, no drift to photoreal, shadows tracked the figures. |
| Silent reaction on **Turbo** | **FAIL** — mouthed gibberish. Cause: the native audio track, which Turbo cannot switch off. |
| Silent reaction on **Standard 3.0, audio off** | **PASS** — breath-shaped, not speech-shaped. Mouth mean 1.14 / peak 3.84 against a blink peaking at 9.81. |
| Voice pass: timing, level, room tone | **MEASURED** — see `Fixed_Assets/VOICES.md`. Speech is sample-aligned; the apparent 26 ms offset is one MP3 granule of head padding. Level lands ~10 LUFS low. Room tone does not survive the pass. |
| Custom prompt presets | Dropped, not tested. Prompts stay hand-pasted. |
| Chained clips on kling.ai | **Deferred by decision** — not a separate test. Measure luma at the first real chain (`P1_042`); Kling extracts frames natively, so both chain workarounds may be obsolete. |
| Wide two-shot | **Removed 2026-09-18.** No two-character clip is generated at all. The scale fault (figures too large against the chairs) comes from the seed frame, so rerolling does not fix it; the outro's one-second hold before the charcoal transformation is the only place it does not show. |

### Still open, and neither blocks generation

- **ElevenLabs paid tier.** The proving clip was made on the free tier, which carries no commercial licence and cannot be relicensed. Re-run one conversion on the paid plan before any clip reaches a published part, and record the tuned **host similarity** value in `VOICES.md` — the host's voice is a clone of a non-native speaker, so similarity pulls the accent through and the number differs from the guests'.
- **Music, SFX and brand assets.** **Verify the licence covers monetised video before generating the set**, and generate the whole set on that licensed tier — some platforms cannot retroactively license work made on a free plan. Room tone bed first.

## A6. Housekeeping
- [ ] Delete `Episodes/Cleopatra/tests/_to_delete/` and the empty `work/` directory by hand

## A7. Modes 5 and 6 — scaffolds, deliberately
Both are written against a finished episode, not before one. Every mode in this project
that is actually good got that way through contact with real output: Mode 4 was a
plausible document before testing and wrong in six specific ways after. Writing Mode 6
in the abstract would produce the same kind of document, and it would be rewritten the
first time it met a real timeline. They gate delivering an episode, not producing one.

## A8. The opening — DONE 2026-09-17

**`BRAND_opening.mp4`** — 19.17s, built, byte-identical forever, rebuildable from
`Branding/intro_source/intro_build.py`. A 6.17s black slot for the hook line, then the 13s intro.
Music unbroken from the first frame; strikes at 0, 4, 8 and 12 with no seam at the join.

- [x] **Sand physics on the reverse — fixed.** The reverse was the fall played backwards, which left
      the bottom bulb's sand welded to the floor with its surface sinking. The mass now lifts off
      the floor and its base rises into the neck.
- [x] **The intro extended with charcoal studies.** Three draw-on clips — hills, doorway, hand —
      each full frame and alone, dissolving into the next, then the page clears and the mark is
      alone on clean paper.
- [x] **The intro heard against its music.** `MUSIC_Theme_Main`, `SFX_sand` and `SFX_plate` are cut
      to it and mixed.
- [x] **The hook slot.** Fixed at 6.17s: strike, line, strike. Mode 3 now nominates the line.

### Still open from A8

- [x] **`BRAND_disclosure` — DONE, and folded into `BRAND_opening`.** Four seconds, on paper rather
      than black, two lines and the mark at the foot. It is no longer a separate asset: it is the
      first four seconds of the opening file.
      **The clock counts the show in — strike, card. Strike, hook. Strike, intro.** Each opener
      lands on a struck note four seconds apart, one continuous performance from 0:00 to the
      downbeat.
      ⚠️ The earlier note here said to leave silence between the card and the first strike, to avoid
      unbroken music from 0:00. **That was wrong and is now reversed.** Between strikes the music
      sits at −47 dB — a clock in a room, not a score. A sustained bed would have broken the
      dry-by-default rule; isolated strikes with near-silence between them are *more* austere than
      the separate sting they replaced.
- [x] **`MUSIC_Bed_Disclaimer` — no longer needed.** It existed only so the card would not play in
      true silence. The clock does that job in the show's own voice. **Five music cues left, not
      six.**
- [ ] **B-roll test with a character. THE LAST THING BEFORE GENERATION.** Everything charcoal so far
      has been objects and places — hills, a doorway, a hand, a vessel, a grinding stone, a carved
      wall. Use **Antony** — he is in the story, not a guest — to find out how the style handles a
      person. It is the last untested assumption in the visual system, and the one with the most
      riding on it: **ten b-roll rows in Part 1 are charcoal**, and if the style cannot carry a
      figure, that is a rewrite of the b-roll plan rather than a reroll.
      ⚠️ Watch specifically for the **graphic-novel drift** the style block was rewritten to
      prevent — crisp helmet highlights, gold accents, forms bounded by drawn edges. A person in
      armour is where that failure is most likely, which is exactly why Antony is the right test.

## A9. Audio — **COMPLETE 2026-09-18**

| cue | status |
|---|---|
| `ROOMTONE_studio` | **DONE** — take 04, 1:48 seamless loop |
| `SFX_sand` | **DONE** — take 02, and the bumper cue cut from it |
| `SFX_plate` | **DONE** — take 3 |
| `MUSIC_Theme_Main` | **DONE** — take 01. Also yields the 4.0s `teaser_loop`, which now carries the opening, the teaser **and** the act break |
| `MUSIC_Drone_Low` | **DONE** — take 01. Take 02 rose +3.5 dB/10s: it develops |
| `MUSIC_Drone_High` | **DONE** — take 03 |
| `MUSIC_Outro_Bed` | **DONE** — take 01, cut in at source 10.0s so the peak lands on the transformation |
| ~~`MUSIC_Bed_Disclaimer`~~ | **CANCELLED** — the clock strikes are the card's bed |
| ~~`MUSIC_Sting_Transition`~~ | **CANCELLED** — the act break carries the theme's own strikes |

**Nine items specced, seven built, two killed — and both of the killed ones were replaced by
something the theme already contained.** Worth remembering before commissioning anything new. Full
spend ~4,300 credits against ~9,800 for the original spec.

⚠️ **One brief was wrong and is recorded as such.** `MUSIC_Drone_High` was specced to hold an
unresolved interval; all three takes came back consonant, on A440 with octaves, fourths and fifths.
The reject criterion is withdrawn — the two drones are distinguished by **register** (centroid
2,961 Hz against 1,187 Hz), not by dissonance. `_raw_takes/DRONE_HIGH_detune_test.wav` is a
zero-credit way to add beating if a cut ever wants it.

## A10. Voices — **COMPLETE 2026-09-18**

- [x] **Host clone** — `FgXTns6rcAlMbBOnz3nB`, recorded in Egyptian Arabic.
- [x] **Cleopatra** — `xMytukqVLj8LlL1L1sOo`, designed, 283-credit call.
- [x] ~~Tune similarity by ear~~ — **tested and null.** No audible difference across Similarity
      settings, Speaker Boost on/off, or Multilingual v2 vs English v2. The host uses the same
      settings as the guests; the "host is the exception" rule is withdrawn.

⚠️ **Two corrections came out of this, both recorded in `VOICES.md` and `skill_mode4_produce.md`:**

1. **Accent lives in the KLING prompt, not the ElevenLabs voice.** Accent is phonetic, and
   speech-to-speech takes phonetics from the **source read**; the target voice contributes timbre.
   All 32 of Cleopatra's `Voice:` blocks were rewritten to placeless English to match the defended
   accent decision — the kit had been specifying a Mediterranean colouring the documentation
   explicitly rejects.
2. **The seed is not exposed in the web UI.** So neither voice can be regenerated from parameters:
   the saved voice *is* the asset. **Never delete either voice.**

- [ ] **Generate a reference render** of each voice (Cleopatra's is **done 2026-09-23**, `Episodes/Cleopatra/VOICE_cleopatra_reference.mp3`; the host's is still open) — the only way to A/B a
      future re-design against what exists now. Small, and the one thing standing between "recorded"
      and "recoverable".

---

## A11. Cleanup and skill optimisation

✅ **Skill cleanup DONE 2026-09-28** (Part 1's clips all made, so the load-bearing rules were known). Every skill now
states each current rule once, with its reason and lesson number, and opens with a **"Tested and ruled out"** list so a
fresh chat cannot bring back something that already failed. History moved to `DECISIONS_ARCHIVE.md` ("Relocated in the
skill cleanup"); `LESSONS.md` gained a status column; the pre-cleanup files are kept verbatim in
`_archive/skills_pre_cleanup_2026-09-28/`. The reasoning below is the brief the pass followed.

🔴 **A rule that came out of damaging a file on 2026-09-18: stage the live file and check its size
against the project listing before editing it.** `skill_mode2_cast.md` was edited from a stale
staging copy and written back, destroying ~9 KB including the Period Accuracy Gate and the whole
`CAST.md` output spec. It was recoverable only because `DECISIONS_ARCHIVE.md`, `CAST.md`,
`POSE_LIBRARY.md` and `STUDIO_ASSETS.md` all held evidence of what it had said. **The compression
pass is exactly where this error is invisible, because the whole job is making files smaller.**

Deliberately deferred. The testing phase left scaffolding all over the project, and the skill files
carry a lot of prose that existed to get a decision made rather than to make it again. Once Part 1
is through generation, do a single pass.

### The one test that decides everything

> **Would deleting this let someone repeat a mistake that cost real credits or real credibility?**
> Keep it. Otherwise compress it to the decision.

That distinction is the whole job, and getting it wrong in the cutting direction is expensive. The
files are long *because* of hard-won failure records, and those are the most valuable thing in the
project. A rule with no reasoning attached gets overridden by the next session that thinks it knows
better — which is exactly how the establishing wide, the accent rule and the VERIFY flags each came
back more than once.

**Keep, always:** the aerial-subject failure (delta, coastline) and why the style block forbids it ·
`tri` vs `qsin` and the 3 dB dip · the paper drift and `paper_restore.py` · accent living in the
Kling prompt, not the ElevenLabs voice · `[D]` lines written from memory · the chain luminance loss
and the colour-range conversion · the wide's figure-to-chair scale fault · why there is no credit
roll · why the subscribe card has no bell.

**Compress to the decision:** how each choice was reached once the choice is settled · credit
estimates for cues that were cancelled · superseded plans that the current text already replaces ·
testing procedures for tests that have passed and will not be re-run · anything whose only content
is "we considered X and chose Y" where Y is now simply the way it works.

### Candidate files — verify before deleting, this is a list to check, not a delete script

| | |
|---|---|
| `_PENDING_CHANGES.md` (33 KB) | scratch from the rebuild — read it first, then almost certainly goes |
| `KLING_MIGRATION.md` (10 KB) | the migration is done; keep only the platform facts, and only if they are not already in Mode 4 |
| `Fixed_Assets/Audio/AUDIO_PROMPTS.md.bak` | superseded |
| `Episodes/Cleopatra/tests/` (~32 MB) | the test programme is CLOSED — the clips proved their points and the findings are written down |
| `Episodes/Cleopatra/_kit_source/__pycache__/` | build artefacts |
| `Claude outputs/` (~45 MB) | decision screenshots: thumbnail variants, sand options, endcard options, plate previews |
| `Branding/ACTBREAK_clock_test.mp4`, `ACTBREAK_look.mp4`, `ACTBREAK_v2.mp4` | superseded by the finished `BRAND_actbreak_*` |
| `Branding/*_options.png`, `*_sizes.png`, `*_check.png`, `plate_placement_guide.png` | the same, for the plates and thumbnails |
| unused font weights | ~3 MB, low priority |

**Do not delete:** `_raw_takes/` (every alternate, including rejected ones and the detune test) ·
the four intro draw-on clips and `stone_4s` / `vessel_4s` (the finished breaks are derived from
them) · anything in `intro_source/` · seed frames and pose variants.

### Skill files, by size

`skill_mode4_produce.md` 74 KB · `STUDIO_ASSETS.md` 44 KB · `SERIES_FURNITURE.md` 44 KB ·
`INTRO_SKETCHES.md` 31 KB · `AUDIO_PROMPTS.md` 26 KB · `skill_elevenlabs.md` 24 KB ·
`skill_mode2_cast.md` 25 KB.

Mode 4 is the one that matters — it is read at the start of every production run, so anything in it
that is no longer load-bearing costs attention every single time. Start there, and apply the test
above line by line rather than trimming by feel.

---

# PART B — GUEST-SPECIFIC (Cleopatra)

## B1. Her pose set — DONE
Five cross-shot variants and three wides in `Episodes/Cleopatra/`, verified by measurement,
registered in `Episodes/Cleopatra/CAST.md`. A sixth leaning pose was attempted twice and
abandoned — the model reads a lean as a zoom. The rejected files have been deleted.

## B2. Rebuild the Part 1 kit — **DONE 2026-09-19**

`Episodes/Cleopatra/P1_kit.md` rebuilt and verified: 92 rows, 89 generated clips + 13 stills,
~759 s, **~7,485 cr**. Opening = `BRAND_opening` (P1_001), act breaks = `BRAND_actbreak` vessel
(P1_032) and stone (P1_058), P1_002/003/005 retired, P1_095 starts from
`frame_wide_cleopatra_marked.png`, titles say `Part 1 of 2`. Ids are labels — gaps are kept on
purpose (note in the kit). The VERIFY gate passes. `KIT_STALENESS.md` is now history.

## B3. Produce with a gate — **superseded 2026-09-23 by the B5 rerun** (kept as the log of what was learned)

Run the gate at the top of `skill_mode4_produce.md` first
(`grep -n "VERIFY" P1_kit.md | grep -vi "cleared"` must print nothing). Then, in the kit's
generation order:

1. **Cold open P1_004–P1_007.** P1_004 is the direct-to-camera → facing-guest join:
   `start_frame frame_host_direct_b · end_frame frame_host_b` (13 s). **This is the end-frame test**
   — if the model ignores or breaks the end frame, follow the fallback ladder written in P1_004's
   note. Scope: this join type only; every other join stays a normal chain.
2. **Bring the returned clips back for measurement** (voice, luma drift at the first chain link,
   duration vs. the 3.85 syl/s estimate) before spending more.
3. **The validated pair P1_055 / P1_057**, then the acts in order.
4. **Outro P1_095 last.**
5. After Mode 4 generation, `build_episode_cards.py Episodes/Cleopatra` renders the per-part
   endcard, lower-thirds and pull-quotes into the episode folder (already done for P1 — rerun only
   if §12 changes).

- [x] **Cold open generated and measured — 2026-09-20.** `shots/P1_004, 006, 007`; report in `shots/_measure/COLD_OPEN_MEASURE.md`.
      **Turbo has no end-frame slot** → the join is a chain, now the default (Mode 4 updated). Picture passes: camera lock holds, join seamless in luma (−0.4%, so **no pre-lift**), but **chroma +7.1% across the join** from the extraction — fix in the edit if visible, and use the ffmpeg extraction for every later chain. Two long pauses (2.5s in 004, 2.2s in 006) to judge by ear. Trim ~0.8s from 004's head to bring guest-on-screen under 40s.
      **Phonetic junctions made a HARD RULE 2026-09-20** — `Fixed_Assets/tools/junction_scan.py` is now a gate in Mode 4 and a non-negotiable in Mode 3. It found 21 junctions in 17 unrendered clips; all rewritten (see each row's *changed 2026-09-20 (junction rule)* note). `P1_055` was one of them, so the validated pair is now `P1_057` alone. `P1_077` 12s → 13s (+10 cr). Cold-open clips are clean.
      **Chain frames are now one batch:** `Fixed_Assets/tools/chain_frames.py` — generate every seed-frame row plus the chain sources (`P1_041`, `P1_056`, `P1_092`), run it once, then generate `P1_042`, `P1_057`, `P1_093` from `shots/start_frames/`. Rerun to measure the joins.
      **Continuity gate added 2026-09-20** (`chain_frames.py` now checks it): `P1_015`, `P1_065`, `P1_074` followed the same speaker on fresh seed frames — now chained from `P1_014`, `P1_064`, `P1_073`. Chain table: 7 rows.
      **Director's toolkit added 2026-09-20** — Mode 3 chooses conversational moments (`OVERLAP`, `NOD`, `OFFMIC`, `BEAT`, `BROLL`, `CUT-IN:cut|seen|yield|hold`) when the drama calls for them; Mode 4 §8b builds them (a `CUT-IN` stop is a silent clip chained from the talking clip **at the cut word** — `chain_frames.py` supports `chain from X at 6.42s`); Mode 6 cuts them. Untested; check the first `CUT-IN` at the edit.
      **Context cards added 2026-09-20** — who/where/what explainers on first mention: Mode 3 writes them (researched, sourced), Mode 4 places them in §12, `build_episode_cards.py` renders them (`context_build.py`), Mode 6 cuts them, Mode 5 re-treats them for vertical. Part 1 has 11. **Design APPROVED 2026-09-20**; all 11 rendered (`Episodes/Cleopatra/BRAND_context_01..11.mov` + `.webm`, listed in `CARD_PLACEMENTS.md`). The research caught a `[D]` error in `P1_066` (Armenia) — fixed.
      **Blink rule 2026-09-20:** a named blink comes back as constant blinking (`P1_056` test; `P1_007` measured). All 24 prompts that named one are rewritten (breath, settle or held pose instead); Mode 4 §5 forbids it and the gate greps for it. `P1_056` is ready to regenerate.
      **Measurement takes to REGENERATE when the kit is final:** `P1_055`, `P1_056` (made before the blink rule). `P1_004`/`006`/`007` are also pre-rule and pre-recalculation — review them at the same point.
      **Welcome reshaped 2026-09-20:** new `P1_006a` — her silent reaction as he names and thanks her (her first studio appearance; her lower third opens there); `P1_007` now chains from it and joins the regenerate list. Rule written into Mode 4 §0 item 5 and Mode 3's toolkit (*a line about the listener plays on their face*). Inserted ids take a letter suffix; all tools accept it.
      **Directing pass 2026-09-20** (research: multi-cam podcast editing, YouTube retention, Murch): Mode 3 *Holding attention* (re-hook each act, front-loaded density, the second answer, callbacks, cut the goodbye); Mode 4 *Cutting rhythm* (emotion first, host reactions on her revelations, cadence, `PUNCH` ≤15% zero-credit push-in, dead-air trims) and chapter titles in packaging; Mode 6 *Cutting the conversation* (J-cut default, no ping-pong, ears-only pass). Apply to the Part 1 kit in the recalculation pass.
      **Prompt A/B queued (cheap, one clip):** vendor syntax says the delivery note belongs *inside* the attribution, and temporal markers (*"Immediately"*) control speech onset — our clips all open with 0.7–1.0 s of silence. Spec in Mode 4 §3; run it on the first Act A clip alongside the recalculated durations.
      **P1_057 generated 2026-09-21 — KEEP this take.** Hook changed to *"Egypt did not survive without me."* (in 5.6 s / out 9.6 s, 1.5 s live hold; freeze-frame fallback) — Mode 3 hook section rewritten (it still described the old 6.17 s slot). **Chain luma corrected:** every clip starts 3.3–4% darker than its input image; the −0.4% at 004→006 was confounded by a non-script frame. **Decided 2026-09-21: joins are levelled in the edit, not predicted** — `chain_frames.py` extracts unmodified and writes `shots/_measure/JOIN_GRADES.md` (per-clip `colorchannelmixer` gains) for Mode 6. **Chain frames come from Kling's own last-frame feature**; the script's frame is the fallback. **The recalculation pass can start.**
      **P1_008 A/B done 2026-09-21:** timing cue *not* adopted (0.25 s earlier onset, faster line, longer pause); take A kept. **Round 1 sheet:** `Episodes/Cleopatra/ROUND1_prompts.md` (56 talking, 11 reactions, 12 b-roll, ~5,986 cr), built by `Fixed_Assets/tools/round_sheet.py`. Old measurement takes moved to `shots/_measurement_takes/`; `P1_056` and `P1_057` kept (the hook and its chain).
      **2026-09-21: full regeneration decided** — every clip is regenerated from the final kit (paragraph-space fix included). All earlier takes moved to `shots/_measurement_takes/`; `shots/` is clean. Demo of the opening with the hook: `Episodes/Cleopatra/DEMO_opening_with_hook.mp4` (measurement take of `P1_057`, not for publication).
      Still open: words checked by ear; **ElevenLabs voice pass on all three** (host clone + Cleopatra voice), as planned.

### B3b. The recalculation pass — everything P1 owes, in one sweep

Added 2026-09-20. **Part 1 predates most of the rules written this week**, so they have to be applied
to its kit by hand once. A kit written fresh by Mode 3/4 gets all of it at writing time, and the five
pre-generation gates (VERIFY · junctions · one Voice line per speaker · continuity/chains · no named
blink) stop the old habits from coming back.

**Trigger:** `P1_057` back and measured. Then, in one pass over `P1_kit.md`:

- [x] **Durations** recalculated (2026-09-21, `syl.dur2`: 4.3 syl/s, lead 0.8 s seed / 0.3 s chained, 0.5 s per break, 0.4 s tail) — spine 626 s → 576 s, total ~7,527 → ~7,059 cr. `P1_057` kept at 12 s. Durations from six measured clips (speech rate, lead-in, tail, pause per break); update every talking row, its credits and the §2 totals.
- [x] **Attributions** rewritten to the inline delivery note (Mode 4 §3), with the emotion form — manner **plus its ceiling** (§4).
- [x] **Cutting rhythm** (§8b) — existing host reactions already sit on her four revelations; `PUNCH` on `P1_019`, `036`, `070`, `078`, `084`; dead-air trims left to the edit by ear (v2 durations remove most slack): host reactions placed on *her* revelations, no picture held past ~40 s, `PUNCH` marks where a line carries emphasis, and a dead-air mark wherever the duration model predicts slack.
- [x] **Toolkit pass** — `OFFMIC`: `P1_027`, `P1_067`; second answer: new `P1_073a`; `CUT-IN:hold`: new `P1_070a` (*"But he—"* under her). `P1_028` and `P1_068` now chain across the off-mic lines; the continuity gate treats `OFFMIC` rows as transparent (Mode 3's tools, used where they fit): two or three `OFFMIC`, the *second answer* beat once, and at most one `CUT-IN` — `hold` is the strongest candidate for her.
- [x] **Writing check:** acts B–D open on the central question and end on open loops; callbacks exist (*Ask it plainly* → *Ask it properly*; *seductress* → *his word for me*; *In daylight*; *Paper*). ⚠️ **Act A ends light** (*"Most of it was reading."*) — a breath before Caesar, not an open loop; left for Salah's call each act opens on the central question and ends on an open loop; one callback; no goodbye after the tease.
- [x] **Chapter titles**, one per act, into §14 packaging.
- [x] **Re-run all five gates** — all pass; §12 unchanged, cards still word-anchored, `chain_frames.py`, and `context_build.py check`; re-run `build_episode_cards.py` only if §12 changed.
- [ ] **Regenerate the measurement takes:** `P1_004`, `P1_006`, `P1_007` (now chains from `P1_006a`), `P1_055`, `P1_056`.

**Still decisions, not rules — they need a measurement each:**
- the **timing-marker A/B** (*"Immediately"*) on the first Act A clip — adopt only if speech starts earlier *and* the line does not rush; aim to shorten the lead-in, not delete it (the edit uses it for J-cuts);
- the **first `CUT-IN`** of each kind, checked at the edit before a second is written;
- the **+7.1% chroma** at a chained join — judged at the cut, fixed with `colorchannelmixer` if it shows;
- **`PUNCH`** — confirm 15% still looks clean on a 1080p source in the finished grade.

- [ ] Full run

## B5. The rerun — ⬅ **NEXT (start in a new chat)**

**Pre-rerun cleanup — done 2026-09-23.** Everything the old kit produced was moved (not deleted) to
`Episodes/Cleopatra/_v1_archive/`, so the rerun cannot read a stale file or leave orphans behind:
`P1_kit_v1.md`, the old story review / script read / Round 1 sheet / card placements / staleness audit /
pronunciation test sheet, `_kit_source/`, the mockups and opening demos, every `BRAND_*` render
(`renders/`), and the measurement takes and `_measure/` (`shots/`). **Kept in place:** `CAST.md`, the
portrait, all five seed frames, the wide frames (incl. `_marked`), `THUMB_cleopatra_p1.png`, and
`card_data_p1.json` (the curated sources only — its old next-part title was blanked 2026-09-23; Mode 4
re-audits it). Modes 1–3 read the archive only to check facts against — **never as a draft** (see the clean-room rule, 2026-09-23, below).

Decided 2026-09-23 (all eight picks in *The Running Order* approved; the release plan deferred). Nothing
is patched into the old kit any more — the skills rebuild the part, and any gap found is fixed in the skill.

1. **Chat 1 — Modes 1, 2 (audit) and 3 together.**
   - ✅ **2026-09-23: Mode 1 redone clean-room** → `Episodes/Cleopatra/PITCH.md` (questions and documented record only; no lines, hook, structure or titles). **APPROVED 2026-09-23**; every ancient-source fact checked (two corrections: Arsinoe's death place differs between sources; the Library fire is reported by both ancient sources).
   - ✅ **2026-09-23: Mode 2 audit** → `CAST.md` audit table; nothing regenerated. Added: accent defence, period evidence, marked wides. Salah then added `thumb_portrait_cleopatra.png` (and its prompt, recorded in `CAST.md`) and `VOICE_cleopatra_reference.mp3`, so **Mode 2 is closed**. Global fixes: Mode 2 now writes the voice reference render at cast time and records the portrait prompt; `THUMBNAIL_SYSTEM.md` Step 2 flags its wardrobe words as guest-specific. Next: Mode 3 in the same chat.
   - ✅ **2026-09-23: Mode 3** → `Episodes/Cleopatra/OUTLINE.md` (both parts; 177 spoken lines, every `[D]` source read that day), `STORY_REVIEW.md`, `SCRIPT_READ.md` (Part 1 ≈ 9:50, Part 2 ≈ 9:19). Outline gates clean. **✅ Script read APPROVED by Salah 2026-09-23 — Chat 1 is closed.**, Salah settled §7: Part 2 length accepted, talent card added, both hooks are first options to be re-picked from the finished episode (Mode 6 now does this). Mode 3 gained *Decide, don't ask* (clarity cards, a slightly short runtime and dead lines are its own calls). Changes go into `OUTLINE.md` and the read is rebuilt. Then **Chat 2 — Mode 4, Part 1**, in a new chat.
   - 🧼 **Clean room (added 2026-09-23 after the first attempt).** The first rerun `PITCH.md` copied the old
     Part 1 structure, hook, lines and a next-part title out of the archive — because this plan told it the
     arc was "settled" and to "carry in the hook line". Both were wrong. That draft is kept as
     `_v1_archive/PITCH_draft_anchored.md` (its Part 2 research is a useful fact source) and **Mode 1 is
     redone**. The rule now lives at the top of Modes 1 and 3: **the archive is a fact-check source, never
     a draft** — carry in facts, corrections, sources, pronunciation, cast and the approved charge; never
     lines, the hook, act structure, shot ids or titles.
   - Mode 1 writes `PITCH.md`: guest, the approved charge, and both parts as **questions and documented
     events** — no lines, no hook, no titles.
   - Mode 2 is an **audit only**: check `CAST.md` against today's spec; portrait, seed frames, wide frames,
     voice and thumbnail portrait are kept — nothing is regenerated.
   - Mode 3 writes `OUTLINE.md` for **both parts** in the new outline format, from today's skills. It picks
     its own hook and structure. Facts and corrections come in as facts (the carpet, the library, "a winter",
     Pelusium, the contested will); the old script decisions come in only as **lessons** — a background act
     must open on a question and end on an open loop; give the key political event a picture; place one or
     two two-ups where both faces matter; write §9 to Mode 4 §15.
   - Outline gates → `STORY_REVIEW.md` (both parts) → `SCRIPT_READ.md` → **Salah approves the words.**
2. **Chat 2 — Mode 4, Part 1.** (The old kit is already archived as `_v1_archive/P1_kit_v1.md`, 2026-09-23.) Build
   the fresh kit from the approved outline; gates; `build_episode_cards.py`; `publish_sheet.py --words-only`.
   Then **compare `P1_kit_v1.md` with the new kit** — anything decided that the new kit lacks is a skill gap:
   fix the skill, then the kit. Archive v1 once the comparison is clean.
   - ✅ **2026-09-23: DONE.** `Episodes/Cleopatra/P1_kit.md` — 117 rows (92 talking, 16 reactions, 7 b-roll, opening, 2 act breaks, close),
     ~567 s talking, **~6,730 cr** before retakes (~7,670 with one retry in six). Built by `_kit_source/build_p1_kit.py` from the
     approved outline; **no spoken word differs from `OUTLINE.md`** (checked line by line). **All gates pass** (VERIFY, junctions,
     one Voice line per speaker, continuity/chains — 20 chained rows, no blink, lines/pronunciation, reviews present, context cards,
     sources audit, `publish_sheet.py --words-only` READY). `build_episode_cards.py` rendered the end card (next: *PART 2 · DID SHE RUN?*),
     2 lower thirds, 3 pull-quotes, 9 context cards and `CARD_PLACEMENTS.md`; `card_data_p1.json` curated from the audit (Cicero,
     Propertius, Chauveau, the Alexandrian War and Life of Pompey dropped — no longer cited). `ROUND1_prompts.md` was built once as a
     parser check (95 clips); rebuild it after the test batch so it skips the test clips.
     **Mode 4 calls made (craft, per Salah's standing rule):** two lines split because the v2 model puts them at or past the 15 s cap
     (cold-open narration 15.8 s; her thesis 15.0 s) — words unchanged; three b-roll rows added where the outline named an image but
     marked no row (Arsinoe's triumph, the will taken from the Vestals, the sixty ships); cards 03 and 07 moved to her repeat of the
     word a second later, card 05 covered by a chained host reaction, so no card ever rides onto the other person's face; host lower
     third on his first question (the welcome plays on her face); pull-quote 01 is also the hook's first option — Mode 6 drops the
     card if it keeps that hook.
     **v1 comparison → skill fixes (global):** Mode 4 §4 item 8 (parsers now read every beat-map segment — `outline_lines.kit_spoken()`
     used by junction_scan, lines_check, publish_sheet, script_read); §2 item 6 (Mode 4 splits a line past 15 s; `lines_check.py` warns
     `LONG` on the outline — Part 2's cold-open narration is 15.8 s too); §10 (all b-roll two-step, matching v1 and `round_sheet.py`);
     §13b (a card must never ride onto the other person's face — three fixes in order; the hook line is not pull-quoted if it stays the
     hook); gate note (never write the gate's word in kit prose). Branding builders no longer hard-code a cloud path (7 files), render
     frames outside the project (the bridge cannot delete inside it), and `endcard_build.py` / `build_episode_cards.py` resume with
     `RESUME=1` so a long render can finish across several short runs.
   - 🎬 **2026-09-24 — Screen share, a series rule (Salah): the guest carries the picture.** His questions play on her
     listening (a guest reaction her answer chains from); his reactions during her lines are **two-ups** (≤ 7 per part,
     3–6 s, never two in a row); at most **two** full-frame host reactions; guest **≥ 65%** of studio picture.
     Composite eyewitness guests keep the target but may show host reactions full frame on the hardest testimony.
     Written into Mode 4 §8b (*Screen share*, two-up rule, §13b pull-quotes now land on her held face), Mode 3 toolkit,
     Mode 6 cutting, `STUDIO_ASSETS.md`; new gate `Fixed_Assets/tools/screen_share.py` (reads each row's `screen:` line).
     **P1 kit rebuilt to it:** 133 rows, 30 reactions (15 of them her listening), 7 two-ups, 1 full-frame host reaction
     (the Arsinoe crack), **guest 75% · host 25%** of the studio picture (4:38 + 0:29 two-up vs 1:40), ~**7,230 cr**
     (+~500 for her listening clips). All gates pass; max chain depth 2; `CARD_PLACEMENTS.md` and the round-1 sheet rebuilt.
   - 🧹 **For Salah to delete by hand:** `_to_delete/` in the project root (render frames left by the old builders, ~500 PNGs).
   - ⚠️ `THUMB_cleopatra_p1.png` in the folder is still the **v1** thumbnail — rebuild it with the new statement (kit §11) before
     publishing; `publish_sheet.py` only checks that the file exists.
3. **Test batch** (Mode 4 §0c) ⬅ **NEXT** — the kit's §4b lists the clips (rebuilt 2026-09-24 — T1 `P1_013`, T2 `P1_019`→`P1_020`, T3 `P1_086`→`P1_087`/`P1_088`, T5 `P1_044`→`P1_045`→`P1_046`, T6 two kinds: `P1_008`+`P1_009` and `P1_083`→`P1_084`→`P1_085`+`P1_086`; T4 has no line in Part 1; ~720 cr). `ROUND1_prompts.md` currently includes the test clips — rebuild it after the batch so it skips them.
   - **Order (Salah, 2026-09-24): one test at a time — T1, T2, T3, T6a, T6b, T5** — each judged before the next is paid for.
   - ✅ **T1 settled 2026-09-24 (`P1_013`):** a separate `Pronunciation:` paragraph is **read aloud** (the host said *"Medes"* twice, `shots/_tests/T1_A.mp4`); **respelling inside the quote works** (*"Meeds"*, `T1_B.mp4`). Rule in Mode 4 §3 3b / Mode 3; the kit now respells *Medes* and *Ptolemies* in the prompts (subtitles unchanged). Also found: the 8 s take ran its speech to the **last frame** (1.1 s at the sentence break + a slow comma list) — Mode 4 §2 now adds 1 s to a line ending on a list of names; `P1_013` → 9 s (and `P1_090`'s list line +1 s). Regenerate `P1_013` at 9 s in Pass 1. **Next: T2 — `P1_019` → `P1_020`.**
   - ⚠️ **`P1_019` (first take, 2026-09-24) failed as a silent reaction:** an open-mouthed exhale ~⅓ in; mouth-area motion ~2× the passing reaction test (Standard, audio off). Cause taken to be the wording, not the model — the prompt named talking/mouthing, set a conversation in motion (*"listens to him … as the question reaches her"*) and asked for a visible breath. **All 30 reaction prompts rewritten** to describe the held mouth positively (*"lips stay gently closed … breathes slowly and quietly through her nose"*); rule in Mode 4 §8. Turbo not used — it failed silent reactions in A5b. Retake `P1_019` with the new prompt, then `P1_020`. Also queued: measure colour drift inside `P1_019`/`P1_020` and at their join (Salah's lighting question) — prompt only if there is real drift inside a clip.
   - ✅ **T2 settled 2026-09-24 (`P1_019` retake → `P1_020`):** the beat map gave each sentence its own delivery, nothing read aloud (Salah). **Now the default** — the builder derives it from the outline's `→` notes (20 rows). The retake `P1_019` passed as a silent reaction (mouth mean 0.79 / peak 2.11, below the passing test) with the new positive wording + eyeline.
   - 📏 **Measured on `P1_019`/`P1_020`:** clip starts 3.4% darker than its seed (the known offset); inside each clip it drifts slightly *brighter* (+1.5%, +2.1%), ending ≈ seed level; the join is flat in luma (−0.3%) with blue +4% — the edit grade covers it. **No lighting line added to prompts.** Eyes: `P1_019` ended with her gaze lowered and `P1_020` recovered by luck → the **end-frame test** (start = end = seed on a listening reaction) goes on `P1_086`, first clip of T3.
   - ⏱️ **Duration model v3 (2026-09-24):** break allowance 0.5 → **1.0 s** (`syl.py`) after `P1_013` and `P1_020` both ran speech to their last frame. Kit rebuilt: talking 611 s, **~7,740 cr**; `P1_128` (Actium question) split into `E1a`/`E1b`, seam under the sixty-ships b-roll. `P1_020` (and `P1_013`) are regenerated at their v3 lengths in Pass 1. **Next: T3 — `P1_086` (with the end-frame variant) → `P1_087` → `P1_088`.**
   - ✅ **End-frame rule settled 2026-09-24 (`P1_086_end` vs `P1_086`):** with start = end = `frame_cleopatra_b` the eyeline held on the host, the last frame matched the seed (face diff 4.1 vs 9.4) and there was no rushed return; the free take's gaze sank again (as in `P1_019`). About half the small movement — a stiller listener, accepted. **Rule in Mode 4 §7; kit rebuilt:** 11 seed-start reactions now carry an end frame and their speaker's next clip starts from the seed frame — chained rows **40 → 29**, ~7,810 cr. **Keep `P1_086_end` as `P1_086`.** Next: `P1_087` from `frame_cleopatra_b`, then `P1_088` from `P1_087`'s last frame.
   - ✅ **T8 settled 2026-09-24 (`P1_006`, Salah's A/B):** Kling's **label form with quotes** — `The woman (cool courtesy): "Thank you." The woman (plain): "…"` — beat our `says, <note>: "…"` form: a clearer change of delivery per sentence, visible in her face. **Now the attribution everywhere** (Mode 4 §3); every prompt in the kit rebuilt; gates read both forms. Keep `T_008_B` as `P1_006`. Both takes strained on the last word *"described"* — timing was fine (tails 0.6–1.0 s under v3), so it is the word: a word-final stop cluster. `lines_check.py` now warns `TAIL` (Part 1: `P1_006`, `P1_108`, `P1_123`) — hide at the cut or with Kling's lip-sync tool.
   - 📝 **Tail rule (Salah, 2026-09-24), in Modes 3, 4, 6:** no line ends on a stop-cluster word; `lines_check.py` fails the outline on an unmarked one (`> TAIL-OK` keeps one on purpose). **Outline changed (approved by Salah 2026-09-24):** *marked* → *chosen* (`P1_108`), *worked* → *held* (`P1_123`), P2 *leave Egypt* → *leave Egypt behind*; *described* kept with `TAIL-OK`. Gates clean, `SCRIPT_READ.md` rebuilt (P1 ≈ 10:33, P2 ≈ 9:58 under duration v3), kit rebuilt.
   - 💸 **720p for audio-only talking clips (Salah, 2026-09-24):** a talking clip whose picture is never used is generated with Turbo at **720p, 8 cr/s** (confirmed on kling.ai). Mode 4 §1, `STUDIO_ASSETS.md`; the builder marks them, `round_sheet.py` groups them under their own heading. P1: 15 clips, 53 s, ~106 cr saved → **~7,700 cr**. (Stills-only b-roll and text-to-speech narration were discussed and set aside — Salah, 2026-09-24.)
   - 🗣 **Simple tones in the brackets (Salah, 2026-09-24):** the bracket after the label now carries a Kling-style tone (*in a dry tone*, *quietly, in a serious tone*, *in a low, firm tone*) instead of the outline note (*"personal, then the decision stated"*). Map in `Episodes/Cleopatra/_kit_source/tone_map.py`; the build stops on an unmapped note. Mode 4 §3 item 2d, Mode 3 beat-map rule. Kit rebuilt, all gates pass. `P1_087` was made with the old note → regenerate it with the new tone before judging T3.
   - ✅ **T3 settled (Salah, 2026-09-24):** `P1_087`→`P1_088` cut together in Resolve reads as one line; only the loudness step (split level rule). Both clips kept. `SPLIT` = fallback for >15 s lines or a big physical turn; the beat map in one clip remains the default. Next: T6a (`P1_008` + `P1_009`).
   - 🔁 **Seed frames to regenerate (Salah, 2026-09-24) — they drift from the rest of the set:** `frame_cleopatra_c` (✅ **regenerated 2026-09-25**; was blocking used by `P1_022`, `P1_041`, `P1_052`, `P1_069`, `P1_070`, `P1_090`, `P1_108` — none generated yet), `frame_host_direct_c` ✅ regenerated 2026-09-26 by editing `frame_host_e` (passes); `frame_cleopatra_c` ✅ re-made the same way from `frame_cleopatra` (passes; old clips from it get a 5 px nudge in the edit — CLIPS.md); `frame_wide_cleopatra_b` / `_c` — skipped (not used in P1/P2). Their `_marked` versions are not needed now — the one wide shot is already generated. Regenerate before any `frame_cleopatra_c` row; replace in place with the same file names so the kit needs no change.
   - 🔴 **No repeatable gestures in reactions (Salah, 2026-09-24, `P1_009`):** "a slow nod … then he is still" made him nod all clip long, same as the blink rule. Reactions now name only a move into a held position, or stillness. Five reactions reworded (`P1_009` and four others); blink gate widened to nod/shake/then back/briefly. Mode 4 §5. `P1_009` to regenerate.
   - ✅ **T6a settled (Salah, 2026-09-24):** two-up #1 (`P1_008` + regenerated `P1_009`) reads as one conversation; crops native, eyelines meet, no end frame needed. Both clips kept. Watch: `P1_008` held a 2.4 s pause between its two sentences (model allows 1.0 s) — Kling seems to stretch pauses to fill the clip; keep measuring before touching the duration model. Next: T6b.
   - ✋ **Hand-at-face pose (2026-09-24, before T6b):** `P1_084` (from `frame_host_d`) now lowers the hand from his jaw as he begins; `P1_083` holds it there. Builder bug fixed: beat-map prompts had dropped pose holds with no anchor word — 19 P1 prompts got theirs back. Mode 4 §5. **Superseded the same day by the pose table** (next item).
   - 🧭 **Pose table (Salah, 2026-09-24): the skills know the poses.** `Fixed_Assets/tools/poses.py` (Host) + `Episodes/Cleopatra/poses.py` (Mode 2 writes one per guest): per frame a hold (auto-inserted in every seed reaction), an entry (hand off the jaw for `frame_host_d`, auto-inserted in its 9 talking clips), and one-way settle/advance/still. All go-and-return gestures rewritten one-way. Builder reads it and stops on a missing frame; new gate `pose_check.py` (proven on a broken copy: 13 faults caught). Mode 2, Mode 4 §5, POSE_LIBRARY. **`P1_013` was generated with his knuckles on his jaw** — its Pass 1 regeneration (9 s) now carries the entry.
   - 🧪 **T6b clips in (2026-09-24):** `P1_083` → `P1_084` join is clean (frame diff 1.3; 083 ends on its seed). `P1_084`: "In a sanctuary" is lower (116 vs 125 Hz, −1.2 dB) — subtle, kept. **Found:** he said the first sentence with his hand still on his jaw and lowered it in the pause — the entry sat at the end of the register paragraph. Builder now puts the entry directly before the first words (+0.7 s); `P1_084` → 6 s in the kit. Same 2.3 s pause-stretch as `P1_008` — cover with the cut into two-up #5. Chains use Kling's last-frame feature (Salah) — kit/skill wording fixed.
   - ❌ **T6b failed → rule (Salah, 2026-09-24): a two-up always has someone talking; never both faces only reacting.** A silence is a `BEAT` on one face (hers), held ~1 s after the last word — the 2 s in the test read too long. Moment rebuilt: "She was a suppliant" on him, "In a sanctuary" off screen over her face (`P1_086`), ~1 s, then `P1_087`. `P1_085` retired (number left empty so clips keep their names); OUTLINE picture notes updated (also dropped "looks down, then back"). `screen_share.py` now fails a two-up with no talking row. Mode 3 (TWOUP, BEAT), Mode 4 §8b, Mode 6. Next: T5.
   - 📒 **Clip ledger (Salah, 2026-09-24):** keepers moved to `Shots/<ID>.mp4` (P1_006, 008, 009, 019, 083, 084, 086, 087, 088 — `T_008_B` renamed P1_006); unused takes to `Shots/_tests/_not_used/`. `Episodes/Cleopatra/CLIPS.md` says why for each; `clip_status.py`: 9 kept (490 cr), REGEN P1_013 + P1_020 (200 cr), 7,216 cr left of 7,706. Mode 4.
   - ✂️ **Tail rule — no exceptions (Salah, 2026-09-24):** `TAIL-OK` withdrawn; P1_006 now *"Usually, others describe me."* (OUTLINE, kit, SCRIPT_READ, STORY_REVIEW). `lines_check.py` fails every stop-cluster ending, including the word before a SPLIT seam. Mode 3 rule 5, Mode 4, Mode 6. **REGEN P1_006.** `P1_020` kept after all (9 s, tight cut into his 3-syllable reply). T1_B was a test of P1_013's line, not P1_013 — it is simply generated in Pass 1.
   - 🎬 **T5 started (2026-09-24):** `P1_044` kept; "Caesar" ends at 2.98 s → `Shots/start_frames/P1_045_start.png` extracted (Kling's feature only gives the last frame). Found and fixed: `P1_046`'s gesture named an armrest on a hands-in-lap pose → pose table `avoid` lists + gate; `frame_host_f` and `frame_host_direct` pose-table entries were written from POSE_LIBRARY wording, not the images — corrected from the images (Mode 2 rule: write entries from the image). Next: `P1_045` + `P1_046`.
   - 📚 **LESSONS protocol (Salah, 2026-09-24):** every problem → rule in every skill that could repeat it + a gate where possible + a row in `Fixed_Assets/LESSONS.md` (17 lessons logged). Protocol at the top of all six mode skills. New gate `prompt_check.py` (tone brackets, Pronunciation paragraph, camera lock, speech in reactions). `tone_map.py` moved to `Fixed_Assets/tools/` so every guest shares it.
   - ✅ **T5 settled (Salah, 2026-09-25) — the test batch is complete** (T1 ✅ T2 ✅ T3 ✅ T6a ✅ T6b ❌→rule T5 ✅; T4 has no line in P1). `P1_045` mouth closes in ~0.4 s; `P1_046`'s 3.2 s silent lead-in is trimmed at the cut (LESSONS L13 updated; duration model v3 kept on purpose). Cut: `Shots/_tests/_twoup/CUTIN_T5_test.mp4`. **Next: Pass 1** — rebuild the round sheet from the final kit.
   - ▶️ **Pass 1 started (2026-09-25):** `Episodes/Cleopatra/ROUND1_prompts.md` — 84 clips, ~5,027 cr (53 talking, 14 audio-only 720p, 10 reactions, 7 b-roll). Kept clips skipped. `frame_cleopatra_c` regenerated by Salah (2026-09-25, checked against the pose table: forearm on the near armrest, open hand in lap — matches) → sheet rebuilt with all 91 clips. Takes go to `Shots/_tests/`; Claude checks and files them in batches of ~10.
   - 🔌 **Kling CLI (Salah, 2026-09-25) — logged in, one blocker left.** Chosen over MCP/app for token cost (Claude reads one line per clip). Official `@klingai/cli-global` 0.2.0, installed in the **cloud session's** workspace (`~/.npm-global/bin/kling`) — kling.ai is reachable there; the Cowork-VM install was not reachable. **Login done 16:11** (OAuth; login is per cloud session — a new session means `kling login` again: Claude runs it, Salah opens the link and pastes back the failed `127.0.0.1:8787/callback?…` address). Account: Ultra, 24,418 cr. `file_upload` works (seed frames upload fine).
   - 🎥 **Camera lock v2 (2026-09-25, LESSONS L18):** Kling guides → lead with "Static camera shot", never name camera moves even negated. v1 lock named pan/tilt/travel/zoom. `P1_058` with v2 held (≤ 2 px drift). Builder, Mode 4 §7, SERIES_FURNITURE, `prompt_check.py` L3/L18 updated; ROUND1 rebuilt (84 clips left after P1_002, 006, 058 kept; 6,782 cr to spend). **P1_058 was made WITHOUT the chip (Salah) → the prompt alone locks the camera; the CLI can do studio clips.** New `cam_check.py` measures every take (≤ 3 px). Only blocker for the CLI now: the workspace network (`kling.ai`).
   - 🛠 **CLI process written into Mode 4 (2026-09-25):** CLI runs on Salah's Mac (his sign-in); Claude writes `Fixed_Assets/tools/kling_run.mjs`, Salah starts each batch with one command (= approval), Claude reads `Shots/_tests/kling_log.tsv` + runs checks. ✅ caps read; `kling_run.mjs` written (dry-run OK). CLI facts: reactions → `kling-video-v3_0` with tail_image, **must pass resolution 1080p (default 4k) and prefer_multi_shots false (default true)**; `kling-video-v3_0_turbo` in the CLI lists **no audio switch and no tail image** → batch 1 tests whether it returns audio; fallback talk model `kling-video-v3_0` + enable_audio true (`--talk-model`). Seedream not in the CLI → b-roll stills stay on the website. Batch 1 (test): P1_016, P1_037, P1_023, P1_005, P1_034.
   - 🧪 **CLI batch 1 (2026-09-25):** 5/5 generated (84–185 s each). Turbo via CLI **has audio** ✓; 720p ✓; v3_0 reactions with tail image ✓ (1080p, single shot). **Problems:** (a) **KlingAI watermark on all 5** (L20) — web downloads are clean; checking whether Kling's reply has a clean link (script now saves raw replies); (b) P1_037 camera moved 17 px (turbo, guest, 3 s) — `cam_check` caught it; (c) P1_034 the guest's knee entered the far corner → prompts now say "Only one person is in the frame." (L19), `cam_check` checks the far corner. Account-balance log did not write — to fix. None kept yet (watermark).
   - ✅ **CLI works end to end (2026-09-25):** clean links via `urlWithoutWatermark` (refetched 016/023/005 free); retakes 037/034 clean, camera held. **Credits match the website** (70 cr for 3 s Turbo + 5 s Kling 3.0 reaction). Kept: P1_005, 016, 023, 034. P1_037 *"Yes."* very quiet (−54 dB mean) — Salah to judge by ear. Duration rounding fixed (L21, part now 7,830 cr). Next: batch 2 (10 clips).
   - ⏱ **Duration model v4 (2026-09-25, L24):** P1_015 (12 s) cut off mid last word → 1.3 s per sentence break + 0.5 s on lines ≥ 9 s; P1_015 now 13 s. Part 1 total 8,206 cr (was 7,830), 6,498 left. Credits (Salah): Kling 3.0 + audio 12 cr/s, Kling 3.0 silent 8, Turbo + audio 10. Talk-model test (P1_018 with end frame, P1_025 without) running.
   - 🎬 **CLI batch 3 (2026-09-25):** 7 kept (027, 029, 032, 033, 036, 039, 041); 015, 028, 030 (all 13 s guest) drifted on Turbo → **rule L27: talking ≥ 9 s on Kling 3.0 + audio + end frame by default** (script picks by length). Rate-limit fix L26 (2 parallel, upload once, retry). Balance 22,431.
   - 🔀 **Website/CLI split (Salah, 2026-09-25, L29):** long (≥ 9 s) or body-moving talking clips → website by hand with the camera chip (23 in P1); short still talking, audio-only and reactions → CLI. Lean wording restored. Lock v3 (camera words at the end only) kept. P1_028/030 kept from the end-only test.
   - 🛑 **CLI set aside (Salah, 2026-09-26, L32):** all remaining clips by hand on kling.ai with the stationary chip; takes saved straight to `Shots/<ID>.mp4`; no per-take checks (Claude only on request or for CUT-IN frames); full `batch_check` once at the start of the edit (Mode 6). Camera lock v2 restored. 71 CLI/website clips kept stand. Left in Pass 1: 25 talking (incl. P1_015, P1_043; P1_127 = keep if the 6 px drift is invisible, else retake) + 7 b-roll + 26 chained — all on ONE sheet now (chained section, made right after each source, Kling's last-frame feature; no CUT-IN left in P1).
   - 🎥 **Camera lock v1 restored verbatim (Salah, 2026-09-26, L33):** v2 drifted even with the chip. Prompts open with the original lock, nothing else about the camera. Round sheet rebuilt — use it for everything from now on.
     **What the CLI exposes (`who_am_i`):** `kling-video-v3_0_turbo` = prompt, duration 3–15, resolution 720p/1080p, imageCount — **no audio toggle (always on, as on the web) and no tail/end image**. `kling-video-v3_0` (= "Standard") = prompt, duration, resolution 720p/1080p/4k, `enable_audio`, `prefer_multi_shots`, `tail_image`, elements. **Dangerous defaults on 3.0: resolution 4k, prefer_multi_shots true, enable_audio false** — `kling_run.py` must always pass `--resolution 1080p --prefer_multi_shots false` explicitly. **No camera/stationary parameter exists** — the stationary paragraph in the prompt is all we have; the test answers whether it is enough. No price quote per call — credits measured by account balance before/after.
     **Blocker: downloads.** Kling's file host `s15-kling.klingai.com` is refused by the session network (only `kling.ai` and `klingai.com` themselves are allowed, not subdomains). Salah to add **`*.klingai.com`** in Claude settings → Capabilities (a new cloud session may be needed). Until then takes can be generated but not fetched here.
     Next: (1) the 24 cr test `P1_069` (3.0, 3 s, 1080p, audio off, multi-shot off, start = end = `frame_cleopatra_c`) on Salah's OK — does the camera hold without the web chip? (2) `Fixed_Assets/tools/kling_run.py` (reads ROUND sheet → model/flags per section, uploads frames once, submits, polls, downloads to `Shots/_tests/`, one line per clip; batch only after Salah confirms the credit total). If the camera doesn't hold: studio clips stay on the web with the chip, CLI does b-roll.
   - 📏 **T3 measured 2026-09-24 (`P1_087` from `frame_cleopatra_b` → `P1_088` chained):** pitch identical across the seam (193 Hz), picture join clean (luma −0.4%, face diff 2.5, blue +4.5% — the join grade covers it), but `P1_088` is **~6–7 dB louder** than `P1_087` → Mode 4 §2 now says: normalise a split pair together, then trim the seam step to ≤ 3 dB. `P1_087` also holds 1.45 s after *"In my family,"* (trim or keep as a beat by ear). **Awaiting Salah's ear on whether it reads as one line.** Salah generates them into `shots/`, then a new chat judges them and folds the results into the skills → Pass 1 → calibration check → Pass 2 → voice pass → assembly → Mode 6 → publish.
4. **Part 2** — Mode 4 in its own chat, from the same approved outline, after Part 1's edit notes exist.

## B4. Open items that do not block Part 1

- ~~`MOVE_TO_DELETE.command` not yet run.~~ Its targets are already gone; the script and `CLEANUP.md` were moved to `_archive/` on 2026-09-23.
- After confirming `DECISIONS_ARCHIVE.md` is complete, remove the old `_PENDING_CHANGES.md` by hand.
- ~~**Before Part 2 Mode 3:** `PITCH.md` and `OUTLINE.md` do not exist yet.~~ Covered by the B5 rerun.
- ~~Skill compression (A11) waits until Part 1 is produced~~ — done 2026-09-28 (A11).
- Working method: one mode per chat inside the project; the `history-answers-back` skill is saved.
  Before editing any file: stage it fresh and check its size against the device listing.

---

# SETTLED — do not revisit
*(Corrected in the 2026-09-28 cleanup — four lines here had gone stale: the 3.85 syl/s duration model, chain-frame
pre-compensation, the voice pass as a fallback, and the −50 dB room tone. The current versions are below.)*
- Combined test passed (the test clips were removed in the 2026-09-18 file cleanup; the findings are in the skills)
- Duration model v4 (`syl.py`): lead + syllables ÷ 4.3 + 1.3 s per break + 0.4 s tail (+0.5 s on lines ≥ 9 s), rounded up, re-measured per guest — Mode 4 §2
- Register stated on every speaking shot; pace never stated — duration is the pace control
- Phonetic junctions: word-final stop against a stressed vowel break lip-sync (`junction_scan.py`, hard rule); no line ends on a stop cluster
- Chain frames: Kling's last-frame feature (or `ffmpeg -sseof`, no range conversion, no lift); joins levelled in the edit from `JOIN_GRADES.md`; max three links
- Voice: the ElevenLabs speech-to-speech pass runs on every talking clip (not a fallback); the accent lives in the Kling `Voice:` line; no pace language in it
- Room tone: `ROOMTONE_studio.wav`, one generated seamless take, ~−60 dBFS RMS under the whole part
- Host pose library: eleven frames (eight facing the guest, three direct), registered in `STUDIO_ASSETS.md` and `tools/poses.py`
- Prompt structure v3, camera chip off (L51)

- 🔁 **B-roll stills → Kling image generation (2026-09-26, Salah, L37).** The passing b-roll start-frame test was run on Kling image gen, so the round sheet, builder, Mode 4 and STUDIO_ASSETS now say Kling for b-roll stills; Seedream stays for studio frames and their edits.
- ✅ **frame_host_direct_b regenerated (Seedream edit of frame_host_b) and installed 2026-09-26** — vs frame_host_b: shift 0, scale 0, luma −1.35 %, room 2.7 → PASS (old one: scale +4). Old file in `Start_Frames/_replaced_2026-09-26/`. P1_003 end-frame pair is now clean.
- ✅ **frame_host_direct regenerated (Seedream edit of frame_host) and installed 2026-09-26** — vs frame_host: shift 0, scale 0, luma +0.3 %, room 2.9 → PASS (old: luma −2.1 %). Old file in `_replaced_2026-09-26/`. All Host frames now PASS.
- ✅ **Start frames DONE for Part 1 (2026-09-26, Salah).** All Host and Cleopatra pose frames PASS. `frame_wide_cleopatra_b` (+ marked) left as is on purpose (luma −2.5/−3.3 %) — the only clip using it is already made; regenerate only if a future part needs that wide.
- P1_003 (Standard + end frame) made 2026-09-26, in `Shots/_tests`: turn snaps in ~0.5 s in a 2.6 s silence (2.6–3.9 s), hold, then line 2 at 5.3 s. Wording fixed globally (L38). Choice: retime in edit, or remake with the new prompt.
- 🔁 **P1_003 back on Turbo (2026-09-27, Salah, L39).** Both Standard + end-frame takes failed. New prompt: small slow turn to frame-right past the mic, eyes level, over the whole sentence. P1_004 now **chains from P1_003's last frame** (listed right under it on the sheet). Fallback if Turbo misses twice: intro line over her face.
- 🧪 **P1_003 mirror try (2026-09-27):** Turbo kept turning him frame-LEFT. Start frame = last frame of P1_002 **flipped** (`Shots/_tests/mirror/P1_003_start_MIRRORED.png`), prompt says left (`P1_003_MIRRORED_prompt.txt`); Claude flips the take back. If it works → Mode 4 rule + LESSONS; if not → free fallback (intro over her face).
- ✅ **P1_003 turn settled (2026-09-27, Salah, L40):** Turbo take kept if it heads toward her (overshoot is fine). New **P1_003a** — 3 s silent Cleopatra reaction (Standard, audio off, `frame_cleopatra`) — cut in as the turn lands; **P1_004 back on the seed `frame_host_b`** (not chained). Mirror try dropped (`Shots/_tests/mirror/` unused).
- 🪑 **Chair fix (2026-09-27, Salah, L41):** big chair (`_b/_d/_e`) is the standard. Salah regenerates `frame_cleopatra` and `frame_cleopatra_c` in Seedream by editing `frame_cleopatra_b`; Claude checks (incl. FURNITURE) and installs. Then remake P1_017, 046, 082, 131, 132 (moved to `Shots/_old_small_chair/`) — ~380 cr. Hold P1_003a and every `frame_cleopatra`/`_c` clip until then.
- ✅ **New `frame_cleopatra` + `frame_cleopatra_c` installed 2026-09-27** (Seedream edits of `_b`, overwritten in place by Salah; colour matched to `_b` by Claude, raw in `_replaced_2026-09-27/`). Whole set on the big chair, FURNITURE clean. Remake 10 clips from `Shots/_old_chair/`: P1_017, 046, 082, 131, 132 (base) + P1_022, 041, 052, 069, 070 (old `_c`, chair also off). `frame_cleopatra_d` sits +2.6 % bright — kept (4 clips made), graded at the join.
- ✅ **P1_003a = cut from P1_126** (0–1.5 s, `_b`), 2026-09-27, L43. Four generated takes on new `frame_cleopatra` had the host intruding bottom-left (`_tests/_rejected/`). ⚠ Watch the bottom-left corner on the 5 remakes that start from `frame_cleopatra` (P1_017, 046, 082, 131, 132) — make P1_017 first.
- 🔧 **L44 (2026-09-27):** every silent reaction = same image in start AND end slot (the 12 kept ones all were). P1_003a had none → cause of the corner intrusion. Builder + round sheet fixed; chained reactions: extracted frame in both slots. The frame_cleopatra corner warning is likely moot.
- 📚 **Pose library (2026-09-27, Salah, L47):** ~9 poses per guest with rank/use/only. Cleopatra: 5 existing tagged; 4 planned for Part 2 (`_f` weary, `_g` hand below collarbone, `_h` fingertips at temple — reactions only, `_i` defiant, turned in) in `Episodes/Cleopatra/poses.py` PLANNED. Salah makes them in Seedream from `_b`; Claude checks (room + FURNITURE), writes the entries from the images, then they join `GUEST`.
- 🔤 **L48 (2026-09-27):** respellings from the outline table (write:/plain). P1_046 remake needed ("Al-eyes." — Allies said wrong) + P1_047 remake (chained from it); P1_049 unaffected (seed). Arsinoe → "Arsin-oh-ee" in P1_055, P1_081.
- 🧍 **Host poses (2026-09-27, L47):** `frame_host_h` (redone: one hand open, palm up, by his thigh — approved by eye) and `frame_host_i` (leaning well in, hands apart) installed, colour-matched, PASS. `_g` dropped — `frame_host_c` is already ankle-on-knee. TODO: `Start_Frames/Host/landmarks.json` (furniture check).
- ✅ **Prompt structure v3 adopted (2026-09-27, Salah, L51):** chip OFF, camera paragraph first + lighting paragraph last. Builder, round sheet, checks, Mode 4/6, STUDIO_ASSETS updated; test sheet archived in `_test_structure/`. Test takes P1_026, 035, 038, 041, 043 moved to `Shots/`; old P1_046/047 to `_tests/_rejected/`. CLI batch generation can be re-tested.
- 🖥 **CLI back (2026-09-27, L52):** `cli_wave.py` + `kling_run.mjs` v2 (dry-run OK). First wave (5): P1_060, 065, 069, 071, 082.
- 🎙 **Voice: ElevenLabs voice change stays (2026-09-27, Salah).** TTS from STT timestamps considered and dropped: TTS can report word times but not follow them; break tags only place sentence starts, so words drift off the lips. Pronunciation and emotion are handled in the Kling prompt.
- 🔤 **L53 (2026-09-27):** every name/place gets a Pronunciation row (possessives own row); Cleopatra table now 48 rows (Antonee, Seezer, Pompee, Syprus, Eyeds respelled). P1_106 → regen (take in `_tests/_rejected/`).
- 💡 Future option (Salah, 2026-09-27): upgrade the video model to Seedance if the show takes off.
- 🎬 **End card support lines (2026-09-27, Salah):** added to `endcard_build.py` (series-fixed); `BRAND_endcard_p1.mp4` re-rendered (old in `_replaced_2026-09-27/`). No pinned-comment corrections line (Salah: sources differ, not logical).
- ✅ **Cleopatra Part 1 — every clip made (2026-09-27).** Studio clips + 6 b-roll in `Shots/` (P1_050 retired). Next: ElevenLabs voice pass, then Mode 6 (edit) in a new chat — first step `batch_check.py`.
- 🎙 **Voice folders (2026-09-27, Salah):** `voice_folders.py` → `Voice/P1/1_host` (49) + `2_guest` (44); converted files go to `Voice/P1/done/` same name. Mode 6 updated.
- 🔁 **frame_cleopatra_d retired (2026-09-28, Salah — pose mistake):** 8 clips remade on `_i` (P1_028, 037, 038, 073, 095, 119, 120, 121); 6 talking ones need a new voice pass.
- ✅ **`_d` → `_i` remake complete (2026-09-28):** all 8 kept; L57 eyeline + L58 side-of-frame wording. Voice pass for P1_028 (and any of 037/073/095/120/121 not yet converted).
- 🎬 **Outro built (2026-09-28):** outro wide from 3 Seedream refs (true scale, host in his last pose), mark composited, charcoal on Kling Image 3.0, P1_134 transformation; preview `Episodes/Cleopatra/_preview/P1_outro_preview.mp4`. **P1_004** welcome now names the show (remake + voice).
