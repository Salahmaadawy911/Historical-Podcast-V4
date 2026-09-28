# SKILL: MODE 4 (PRODUCE EPISODE PART)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.

> 📂 **Inputs and output.**
> **Reads:** `Episodes/<Guest>/OUTLINE.md` (its words **approved** in `SCRIPT_READ.md`), `Episodes/<Guest>/CAST.md`
> and `Episodes/<Guest>/poses.py`; for Part 2, also `P1_kit.md` and `P1_EDIT_NOTES.md`.
> **Mode 4 does not change words.** A line that needs rewording goes back to `OUTLINE.md`, through the outline
> gates, and into the read again — the kit is built from approved text only.
> **Writes:** `Episodes/<Guest>/P<n>_kit.md` (built by a script in `Episodes/<Guest>/_kit_source/`), then the
> per-episode brand renders and `CARD_PLACEMENTS.md` from `build_episode_cards.py`, then the round sheet.
> **Save the output to that file before the mode ends.** Anything that lives only in chat history is lost to the
> next mode.

> 📚 **How this file is kept (cleanup 2026-09-28).** Each rule is stated once, as it stands today, with its reason
> and its lesson number. How a rule was reached, the superseded versions and the measurements behind them are in
> `DECISIONS_ARCHIVE.md` and `Fixed_Assets/LESSONS.md`; the full pre-cleanup text is in
> `_archive/skills_pre_cleanup_2026-09-28/`. **Before changing a rule that looks arbitrary, read its lesson.**

---

## 🔴 Gates — before any clip is generated. A single failure stops the run.

```bash
# set once per run — every gate works for any guest and any part:
G=Episodes/<Guest>; N=<part number>; K=$G/P${N}_kit.md
grep -n "VERIFY" $K | grep -vi "cleared" && echo "STOP — unresolved claim in a spoken line"
python3 Fixed_Assets/tools/junction_scan.py $K                       # must print nothing — HARD RULE (§6)
grep -h "^ \?Voice:" $K | sed 's/^ //' | sort | uniq -c              # exactly ONE line per speaker, identical to CAST.md and STUDIO_ASSETS.md
python3 Fixed_Assets/tools/chain_frames.py $G $N                     # continuity: same speaker back to back must chain (§7)
awk '/^```/{f=!f} f && tolower($0) ~ /blink|nod|shakes? (his|her) head|then back|then lowers|briefly/' $K   # must print nothing (§5, L5)
python3 Fixed_Assets/tools/lines_check.py $K                         # banned phrases + every name has a pronunciation row
python3 Fixed_Assets/tools/screen_share.py $K                        # the guest carries the picture (§8b)
python3 Fixed_Assets/tools/prompt_check.py $K                        # the prompt-writing lessons (L-numbers in its header)
python3 Fixed_Assets/tools/pose_check.py $K                          # every prompt written from its frame's pose-table entry (§5)
python3 Fixed_Assets/tools/clip_status.py $K                         # kept / to do / credits left (reads Shots/)
ls $G/STORY_REVIEW.md $G/SCRIPT_READ.md                              # the script review exists and Salah approved it
python3 Fixed_Assets/Branding/intro_source/context_build.py check $K # every context card fits
python3 Fixed_Assets/tools/publish_sheet.py $G --part $N --words-only   # §15 publish words pass (exit 0)
```

Why each one exists, in a line:
- **VERIFY** — the flag sits on a *spoken* line; after generation a one-word fix costs a regeneration and a voice
  pass. `VERIFY CLEARED <date>` is a record and does not fire; never write the bare word in kit prose (the grep
  cannot tell a mention from a flag — it fired on exactly that, 2026-09-23).
- **One `Voice:` line per speaker** — the accent reaches the cut from this line (§1), so a stray variant is a
  different accent in those clips.
- **Continuity** — a fresh seed frame after the same speaker is a pose snap on the same camera. The alternative the
  rule allows is `edit_placement: audio only, under …` on the first clip.
- **Every gate counts what it checked.** A gate that silently checks nothing looks exactly like a pass
  (`junction_scan.py` checked zero lines for a day after an attribution-format change, 2026-09-22) — the tools
  fail if they scan fewer lines than there are talking rows.

**Part-aware.** Every tool takes the part (`chain_frames.py $G $N`, `round_sheet.py $G <pass> --part $N`,
`build_episode_cards.py $G --part $N`). Part 1 keeps its original output names; Part 2+ renders carry a `p<N>` tag.

**Every asset the kit names must exist before generation, and must be produced by a named mode.** "It already
exists" is a statement about one episode, not about the pipeline (Part 1 once shipped naming two files only testing
had made).

**Then scan the spoken lines for falsifiable specifics** — numbers, dates, kinship, who-did-what, absolutes — and make
sure each one in a `[D]` line names respectable support, or retag it `[I]` (§6b). Proportionate: on Part 1 that was
14 lines of 66.

---

## 🚫 Tested and ruled out — do not bring these back

Each of these was tried, measured and rejected, or replaced by something that tested better. A fresh session will
find some of them plausible — that is why they are listed. Evidence: the lesson number, or `DECISIONS_ARCHIVE.md`.

**Camera and prompt layout**
- **The stationary chip / camera preset as a requirement.** Structure v3 (§3) holds the camera with the chip OFF —
  0 px on ~15 clips including 13 s talking clips (L51; supersedes L3, "chip forgotten → camera moved"). Do not reinstate the chip or make a clip depend on it.
- **Earlier camera locks.** *"The camera does not move…"* (drifted — negation). Lock v1 *"The camera is stationary.
  Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom…"* (held only with the chip). Lock v2
  *"Static camera shot…"* opening and closing (drifted even with the chip, L33). Camera words only at the end (L28,
  withdrawn). All replaced by v3. Do not re-open *"naming pan/tilt/zoom invites them"* (L18) without a measured A/B.
- **A leading space before every paragraph of a studio prompt.** It fixed fused paragraphs under the old layout; v3 was
  tested without it (L51). (B-roll and still prompts still start later paragraphs with one space — harmless, and how
  the builder's `para()` writes them.)
- **Any other Kling preset** (Shot type, Light and shadow, Frame, Atmosphere) on a studio clip — each is literal prompt
  text describing what the seed frame already fixes. *"The speed of the camera motion is slow"* presupposes motion;
  *"Shallow depth of field"* invites a re-read of the plate. **Custom saved presets** — dropped: a preset that
  reformats text is an invisible input.

**Writing the prompt**
- **A separate `Pronunciation:` paragraph** — Kling reads it aloud (T1, L2). Respell inside the quote.
- **Respellings with hyphens or inner capitals** (*Arsin-oh-ee*) — said syllable by syllable, like a correction (L49).
- **The outline's delivery note in the bracket** (*"personal, then the decision stated"*) — not Kling vocabulary (L1).
- **The `says, <note>: "…"` attribution** — the label form beat it in an A/B (T8).
- **A timing cue** (*"He begins speaking immediately."*) — bought 0.25 s of onset and gave it back as a longer pause
  while the line ran faster (`P1_008` A/B, 2026-09-21).
- **Pace words** (*unhurried, measured, slowly*) anywhere in a prompt — duration is the pace control; pace words make
  the model spend the budget early and compress the tail.
- **Naming a blink, a nod, a head shake, or any go-and-return gesture** — Kling loops it for the whole clip
  (`P1_056`, `P1_007`, `P1_009`; L5).
- **"toward him / toward her"** — with one person in frame, Kling reads *him* as the viewer and turns to the lens (L58).
- **Removing lean/forward wording** (L25) — reverted (L29); the pose table's wording stands.

**Durations**
- **3.85 syl/s + ~1 s per break**, and *words ÷ 2* — from the previous platform; over-padded every clip.
- **0.5 s per break** (v2) — speech ran to the last frame twice (v3). **1.0 s per break** (v3) — `P1_015` cut off mid
  word (L24). **Rounding down** — `P1_016` ended 0.15 s after its last word (L21). **"Never round up"** — the old rule;
  reversed, because a clip that is too short is a regeneration while spare silence is a trim (L13).

**Silent reactions**
- **On Turbo** — mouthed gibberish; Turbo's audio cannot be switched off (A5b test).
- **Naming speech** (*"no talking, no mouthing"*), **setting a conversation in motion** (*"listens to him as the question
  reaches her"*) or **a visible breath** — `P1_019` came back with an open-mouthed exhale (L4).
- **No end frame** — the host drifted into the corner, 4 takes of 4 (L43, L44).
- **A different image in the end slot than the start** (the seed after a chained start) — Kling morphs between the two;
  `P1_047` dropped its gaze and came back (L45, withdrawn the same day).
- **Ending on a held pose with nothing to do, or implying other people** (*"named to the room"*) — Kling invents motion
  off frame (L42).

**The host's direct-to-guest turn**
- **Standard + end frame on the guest-facing seed** (L34) — failed twice: the head snapped across in dead air (L38, L39).
- **Chaining the next host clip from the turn's last frame** (L39) — Turbo overshoots, so the wrong eyeline is carried
  forward (L40).
- **A mirrored start frame** so Turbo turns the "wrong" way — tried 2026-09-27, dropped.

**Generation route**
- **Every clip by hand on the website, chip on, no CLI** (L32) — replaced by structure v3 + CLI waves (L51, L52). The
  website stays the fallback.
- **Splitting clips between CLI and website by length or movement** (L27, L29, L30) — superseded; v3 holds the camera
  on all lengths.
- **Downloading the CLI's `url`** — carries a KlingAI watermark; only `urlWithoutWatermark` is saved (L20).
- **Per-take checks by Claude during generation** — cost usage for little gain; one `batch_check.py` pass opens the edit.

**Two-shots, wides and chains**
- **Any generated clip with both people in it** — the wide put the figures a size too large for the chairs (from the seed
  frame, so rerolling does not fix it), and a two-speaker clip cannot pass the voice pass (it converts to one voice).
  The **establishing wide**, the **silent wide**, the **conversing wide under credits** (`WIDE_CREDITS`) and the
  **empty-studio wide** are all out. The only two-shot is the per-part outro still (§7).
- **A per-guest pre-made wide / `frame_wide_<guest>_marked.png`** — scale fault and a host pose that never matched his
  last line (L59). The outro wide is built per part.
- **A two-up with nobody talking** — two faces only reacting read as empty (T6b, L10). **A 2 s held `BEAT`** — too long
  (L11).
- **Pre-lifting chain frames to cancel Kling's per-link darkening** — prediction failed once and would fail on any
  platform change; joins are levelled in the edit (2026-09-21).

**B-roll**
- **Seedream for b-roll stills** — the passing test was on Kling image generation (L37).
- **A reference image for anonymous extras** — about twenty clone faces.
- **Photoreal b-roll**; **Pexels** stock — the sketch won on measurement (§10); no stock tier exists.
- **Wide views of ports, towns and fleets without period bans** — came back 18th/19th-century (L55).

**Lines**
- **`TAIL-OK` exceptions** — every stop-cluster last word is rephrased (L12).
- **Chiasmus / mirrored constructions** — alignment slipped across the figure in both orders.

---

## 0. The opening — fixed shape, every part

The first minute decides whether the rest is seen. Not negotiable per episode:

1. **`BRAND_opening.mp4`, 0:00–19.17 — one built file, byte-identical forever** (spec: `SERIES_FURNITURE.md`).
   It carries, on one continuous page with one unbroken piece of music (a clock strike at 0, 4, 8 and 12 s):
   - **0.00–4.00 the disclosure card** — *AI-GENERATED DRAMATIZATION / Historical reconstruction, not a recording.*
     and, small by the mark, *A conversation I wanted to hear.* Fixed wording, series-wide. The full statement lives
     in the description and on the end card, where there is room to read it.
   - **4.00–8.00 the hook slot** — an edit-only lift of the guest's strongest sentence from later in the part, the face
     emerging from the paper (`hook_build.py`). No generation, no credits. Mode 3 nominates a first option; **Mode 6
     picks the final hook from the finished part.**
   - **8.00–19.17 the intro** — the three charcoal studies, then the mark and the hourglass. Never generate a title
     beat per episode: it is the one piece a model would render differently every time.
2. **Composite card — eyewitness episodes only, ~4 s**, at the end of the cold open, immediately before the guest first
   appears in the studio (that is where the question *"is this a real person?"* is live). Rendered per episode by
   `build_episode_cards.py --composite N`. Skip it on named-figure episodes.
3. **One host direct-address hook**, not two — whichever beat carries the *charge*, ending on a hand-off line. Scene
   setting a second beat would do is almost always already inside his first question.
4. **The welcome, in the studio.** The host names the show and the guest (*"Welcome to History Answers Back.
   <guest, styled>. Thank you for being here."*; later parts *"This is History Answers Back. <guest> — welcome back."*
   — listeners and background tabs never see the card). 🔴 **The guest is seen before being heard:** while he names and
   thanks her, the picture is her **silent reaction** receiving it; her lower third opens there; her reply chains from
   it. Each speaker in their own single.
5. **First question.**

**The host never states the disclaimer aloud** — the card, the description and Studio's *altered or synthetic content*
toggle cover it; saying it again costs twelve seconds of the most valuable time in the video.

**Measure the result:** first guest word under ten seconds (the hook), guest on screen in the studio under forty.

## 0b. The last step of Mode 4 — build the episode's brand assets

**Mode 4 ends with the kit *and* every per-episode brand render in the guest folder.** By the time the kit exists,
§12 already carries the names, the pull-quotes, the context cards and the shot each lands over; leaving renders to the
edit means deciding them again, which is where on-screen text drifts from the kit.

```bash
python3 Fixed_Assets/Branding/intro_source/build_episode_cards.py Episodes/<Guest> [--part N] [--composite N]
```

| writes into `Episodes/<Guest>/` | from |
|---|---|
| `BRAND_endcard_p<n>.mp4` + `.png` | `card_data_p<n>.json` |
| `BRAND_lowerthird_host` / `_guest` | §12, `_L` for the host, `_R` for the guest |
| `BRAND_pullquote_01..NN` | §12, on the speaker's side |
| `BRAND_context_01..NN` | §12 *Context cards*, opposite the speaker, as the word is said |
| `BRAND_composite_p<n>.mp4` | `--composite N`, eyewitness episodes only |
| `CARD_PLACEMENTS.md` | which file goes over which shot |

Plates come out as alpha `.mov` (QuickTime Animation) **and** alpha `.webm` (a 5 s RLE plate passes 20 MB).
A long render resumes with `RESUME=1`; render frames are written outside the project.

- **The design is series-fixed; only the render is per episode.** Builders live in `Branding/intro_source/`. Never
  write a render into `Branding/` — one episode's sources sitting in the fixed folder is how the wrong one gets used.
- **The sources block is audited, not generated.** `sources_audit.py` reports what the provenance tags cite against
  what the card lists, both directions. The card is a curated claim; the tags are the evidence. Curate
  `card_data_p<n>.json` from the audit.

## 0c. The test batch — Part 1 of a new guest, before generation

Some techniques are written but not yet proven on Kling. The few clips that test them are generated first, judged, and
folded back into the skills, after the gates pass and before the round sheet's main run. Pick shots **from the kit in
hand by the criteria** (never from old shot ids); tests may share a shot; test clips are normal kit rows and are kept
if they pass. Part 2 inherits whatever passed.

| # | question | status |
|---|---|---|
| T1 | Pronunciation via a separate paragraph, or respelled in the quote? | **settled — respell inside the quote** (§3) |
| T2 | Does a beat map give each sentence its own delivery? | **settled — yes, the default** (§4) |
| T3 | Does a `SPLIT` read as one line; does lip-sync drift in long takes? | **settled — yes, only a loudness step; no drift seen.** `SPLIT` is a fallback (§2) |
| T4 | Does a **trailing `…`** play as a thought let go, not a stop? Qualifies: the first line in a kit that uses `…` | **open** |
| T5 | Does a `CUT-IN` stop read as a real interruption, mouth closing? | **settled — yes** (§8b) |
| T6 | Does a two-up hold up — crop, eyelines, listener length? | **settled — T6a passes; T6b (shared silence) failed → someone always talks** (§8b) |
| T8 | Kling's label form vs `says, <note>:` | **settled — the label form** (§3) |

A test that **passes** becomes the rule here, with its hedge removed. A test that **fails** removes the technique from
Modes 3 and 4 and goes into the ruled-out list above. A test with no qualifying shot stays open.

---

## 1. Pipeline

- **kling.ai**, image-to-video, **1080p**, clips capped at 15 s. **The model is chosen per shot type:**

  | Shot type | Model | Rate |
  |---|---|---|
  | Talking (`INTERVIEW`, `NARRATION`, `INTERJECTION`) | Kling 3.0 **Turbo**, audio on | 10 cr/s |
  | **Audio-only talking** — picture never used (his line under her listening, an `OFFMIC`, a line wholly under b-roll) | Kling 3.0 **Turbo at 720p** | **8 cr/s** |
  | `REACTION` (silent) | Kling 3.0 **Standard, audio off**, end frame = start image | **8 cr/s** |
  | `BROLL_GEN` | Kling image 3.0 still, then Kling 3.0 **Turbo**, audio on | 10 cr/s (+ ~3 cr still) |
  | `BUMPER_OUT` (the outro transformation) | Kling 3.0 **Standard, audio off**, start + end frame | 8 cr/s |

  Why: Standard with audio off is the cheapest clip and removes the audio channel that made Turbo reactions mouth
  words; 720p is the same voice for a clip whose picture is thrown away (the builder marks it from the row's `screen:`
  line; never use 720p for a clip that is on screen even partly). Rates and reasoning: `STUDIO_ASSETS.md`.
- **Camera chip OFF.** The v3 prompt structure holds the camera and the lighting on its own (§3, L51).
- **View every asset before writing a prompt that uses it** — seed frames, stills, furniture — per `STUDIO_ASSETS.md`'s Visual Grounding Requirement; a frame may have been regenerated since it was last seen.
- **Every studio clip starts from a seed frame** (`Start_Frames/Host/`, `Start_Frames/<Guest>/`) or chains from a clip.
  The seed frame carries identity, wardrobe, room, lighting and framing — **the prompt never describes any of them.**
- **Dialogue audio is generated in the clip**; so are ambience and diegetic effects, which is how b-roll arrives with
  its own sound. Suppress the model's music bed in every prompt (the `Audio:` line).
- **Vocal identity comes from ElevenLabs**, not the video model: every talking clip goes through speech-to-speech
  against the character's voice ID in `Fixed_Assets/VOICES.md`, model **`eleven_multilingual_sts_v2`, set explicitly**
  (the API default is English-only and switches silently). Picture and lip-sync survive untouched. Reactions (silent)
  and b-roll are never passed. Platform detail: `skill_elevenlabs.md`.
- 🔴 **The accent is decided in the Kling `Voice:` line, not in ElevenLabs.** Accent is phonetics, and
  speech-to-speech takes phonetics from the *source read*; the target voice supplies timbre only (proven on the host
  clone, 2026-09-18). So the `Voice:` line is byte-identical in every clip of that character, matches `CAST.md` and
  `STUDIO_ASSETS.md`, and names a chosen accent plainly, Kling-style (*"with a light Greek accent"*) — the *never say
  "accent"* rule applies only to the ElevenLabs design text. Wording rules: `skill_mode2_cast.md`.
- **The `Voice:` line still matters beyond accent:** speech-to-speech maps timbre onto the source delivery, so the source
  must be a clean, correctly-timed read in roughly the right register.
- **One part, one set of settings** — resolution, models, platform. A mid-part change alters the performance for no
  visible reason.
- **Keep every raw Kling clip.** If a voice is ever redesigned, raw clips can be re-processed; a discarded original
  means regenerating video. **Download each kept clip the day it is made** — the platforms may delete stored content,
  and a lapsed subscription can take access with it.

## 2. Duration

🔴 **The model — v4 (2026-09-25; L21, L24), implemented as `syl.dur2()` in `Fixed_Assets/tools/syl.py`** (every
builder, `lines_check.py` and `script_read.py` use it):

> **duration = lead (0.8 s from a seed / 0.3 s chained, +0.7 s for a pose entry) + syllables ÷ 4.3 + 1.3 s per
> sentence break or dash + 0.4 s tail, + 0.5 s on any line needing 9 s or more, rounded UP to a whole second
> (`ceil(need + 0.1)`) — never down.**

Why: the model speaks at a **fixed rate** (~4.3 syl/s, 4.1–5.4 measured) and spends any slack as silence — at a
sentence break, or as a silent lead-in. Spare silence costs a trim in the edit; a clip too short cuts off the last
word and costs the whole clip (L13, L21, L24).

- **Re-measured per guest.** The rate is a property of the voice. For every new guest, the **first three to five
  talking clips** are measured (rate, lead-in, pause per break) and written into the *duration calibration* of the
  `CAST.md` performance profile **before the rest is generated**; a rate more than ~10% off 4.3 means that guest's rows
  are recalculated. The host's rate carries over. Part 2 uses Part 1's calibration.
- **A line ending on a comma list of three or more names: +1 s** — the model slows through the commas (`P1_013`).
- **A take whose speech reaches its last frame is regenerated one second longer**, never used — there is no tail to
  cut on.
- **Density.** Above ~1.6 syllables per word a line is too heavy: rewrite it (at the outline), don't add seconds —
  added time spreads over the line, the compression is local.
- **Tail weight.** The last sentence must not carry a disproportionate share of the syllables, and a clip never ends
  on its densest word. Latinate abstractions (*independence, legitimacy*) sit mid-line, never last: *"Or was that the
  moment Egypt stopped being free?"* worked where a 21-syllable version failed on two platforms.
- **Dramatic pauses are cheaper at cuts than inside clips** — silence between shots is free; silence inside one costs
  words.
- **Re-run the duration model on any line that changes** (*"A winter"* is a syllable longer than *"Four months"*).

**One beat, one clip.** A clip carries one delivery well. A line whose mood **turns at a sentence** is carried by a
**beat map in one clip** (§4) — the default, and free. A **`SPLIT`** into two chained clips is the fallback, for:
- a line past the 15 s cap — Mode 4 splits it even if Mode 3 did not mark it (words unchanged; `lines_check.py` warns
  `LONG` on the outline so Mode 3 can mark it); a line of 13–15 s stays whole unless its mood turns;
- a turn the **body** must show.

**Building a `SPLIT`:**
1. Split only at a sentence break — a pitch or energy step sounds natural at a full stop and wrong mid-clause.
2. **A** ends on its sentence; **B** is `chain from A` (0.3 s lead). Each half has its own delivery and its own single
   gesture. The last word of A obeys the tail rule (§6).
3. Every split row names how the seam is hidden, best first: **(a)** a cutaway across the seam (listener, b-roll,
   off-camera line) with A's audio running into B's; **(b)** a `PUNCH` exactly on the seam; **(c)** a plain cut on
   the pause. On direct address only (c).
4. **The edit levels the pair together** (one gain for both), then trims any remaining step at the seam to ≤ 3 dB —
   B came back 6–7 dB louder than A in T3 (L14); per-clip normalisation would flatten the written arc.
5. Budget ~1 s (~10 cr) extra per split. A split counts as a chain link.

## 3. Prompt structure — v3 (L51)

🔴 **Every studio prompt (talking or reaction) is, in this order:**

1. **The camera paragraph, verbatim:**
   `Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.`
2. **ONE paragraph:** `Only one person is in the frame.` (L19 — the off-frame partner wandered in without it) + the
   register sentence + the pose entry if any + the attribution and the line(s) + the gesture or physical beats + the
   eyeline sentence (§5).
3. **The `Voice:` line** (talking clips) — byte-identical, from `CAST.md`.
4. **The `Audio:` line**, verbatim —
   talking: `Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.`
   silent: `Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.`
5. **The lighting paragraph, verbatim:**
   `Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.`

No other camera words anywhere; no leading spaces (studio prompts). The builder writes it (`LOCK`, `ONE`, `CONT`, `para()`);
`prompt_check.py` L51 checks the opening and the close. Measured: camera 0 px on every test clip; brightening across a
clip ~1.4 % against ~1.8 % before.

**The attribution — Kling's label form, quotes kept (T8):**
`The woman (in a coolly polite tone): "Thank you." The woman (plainly): "Usually, others describe me."`
- One label and one bracket per sentence in a beat map; the label repeated each segment; a physical beat (no quotation
  marks in it) between segments where the body moves. Quotes mark where speech starts and stops, and every gate reads
  them (`outline_lines.kit_spoken()` joins all quoted segments).
- **The label is the guest's *prompt label*** from the `CAST.md` performance profile (Cleopatra: `The woman`), fixed for
  the arc; pronouns from the profile. Never copy another guest's label.
- 🔴 **The bracket holds a simple Kling tone** — one to three manner words or one *"in a … tone"*: *in a dry tone*,
  *plainly*, *quietly, in a serious tone*, *in a low, firm tone*. The builder maps every outline note through
  `Fixed_Assets/tools/tone_map.py` (shared by every guest) and **stops on an unmapped note** — add the mapping, never
  pass the raw note (L1). No "then", no job labels, no images.

**The line itself** — in quotation marks, clean: no bracketed cues, capitals or exclamation marks inside (they get read
aloud or over-performed).

🔴 **Pronunciation — respelled inside the quote, from the outline's table (T1, L48, L49, L53).** Every name and place
has a row in the outline's Pronunciation table with a decision, `write: <respelling>` or `plain`; the builder writes
the respelling inside the prompt's quote, and the **Subtitle keeps the true spelling**. A respelling is **one plain word**
(*Meeds, Tolemies, Seezer, Antonee, Arsinowee*). Never a hand-kept list in the builder. A name with no safe respelling
is checked by ear on the take — the ElevenLabs pass keeps the Kling pronunciation, so a wrong name is baked in.
`prompt_check.py` fails a raw `write:` word in a quote, a row with no decision, and a lone stress homograph with no row.

**Never state pace.** Duration is the pace control (§2).

**Formatting — every paragraph is one unbroken line; paragraphs separated by one blank line.** Kling strips newlines
without inserting a space, so a hard-wrapped prompt arrives with words fused (`frame.Soft`). **Paste from the kit or
the round sheet, never from chat** — chat rendering drops spaces (*"stationary.Locked"*).

## 4. Register and emotion

The model infers register from the *content* when the prompt does not state it, and the inferred default is always
more dramatic than this show wants — an accusatory question gets played as an accusation. **Every speaking shot states
its register.**

- **Host default:** curious, level, pressing without prosecuting — an interviewer, never an interrogator.
- **Guest default:** the *default register* and *emotional ceiling* in the `CAST.md` performance profile. Per-shot
  direction states only a deviation.
- **Composite eyewitness guests run the testimony register** — uncertain where the record shows uncertainty, caught out
  where it catches them out, never composed beyond what the sources support (`skill_mode1_pitch.md`).
- **Scope a constraint to tone, never to movement.** *"His tone stays level throughout, never hardening into
  accusation"* works; *"holds the same pace and intensity"* freezes the body too.
- Charged content is where escalation, speed and broken lip-sync live — **direct the most dramatic lines hardest.**

**How an emotion is written:**
1. Prefer manner words (*level, dry, flat, courteous, precise, plain*) to emotion nouns (*angry, devastated*) — the
   model performs nouns at full strength.
2. **Name it, then say where it stops:** *"Dry, and never amused."* *"Steady, and it does not break."*
3. One step at a time; two descriptors maximum.
4. The strongest feeling is usually written as restraint — it reads as more, and it is technically safer.
5. Emotion lives in the delivery, never in the quote.
6. The body carries the rest as observable movement only (*"her hand stops where it is"*, never *"she looks shocked"*).
7. Keep a character's register vocabulary stable across the part.

**The beat map — one delivery per sentence, in one clip — is the default (T2).** Where the outline gives one note per
sentence (`note1 → note2 → …`, same count as the sentences), the builder writes each sentence with its own label and
tone bracket; where the counts differ, one note stays. One or two physical beats between segments at most, from the
guest's gesture range — the beats *are* the gestures, so the separate gesture sentence is dropped. Budget each break
with the duration model.

## 5. Gesture and the pose table

🔴 **Every prompt is written from the pose table — never from memory of the frame.** `Fixed_Assets/tools/poses.py`
(the host, permanent) and `Episodes/<Guest>/poses.py` (written in Mode 2) hold, per seed frame: `desc`; `hold` (the
pose held — inserted into every silent reaction from it); `entry` (what happens as a talking clip begins — required when
a hand is at the face); one-way `settle` / `advance` / `still` gestures; an `avoid` list of contacts the pose does not
have; and the library fields `rank`, `use`, `only`. The builder reads it and **stops on a frame with no entry**;
`pose_check.py` fails a prompt that drops a hold or an entry, names a repeatable gesture, or names a contact in `avoid`.
Change a pose's wording in the table, never in one prompt.

- **Choosing a pose for each row (L47).** Match the row's delivery note to a pose's `use`; never the same pose for the
  same person on consecutive shots unless chained; move at most ~2 `rank` steps across a cut unless the line turns hard;
  `only='react'` poses never start a talking clip. Spread the library so every pose appears. A fresh pose is only right
  where the character had time to move (the other person spoke a full utterance) — across an interjection or a short
  reaction, chain instead.
- 🔴 **Only one-way moves, or stillness (L5).** Kling does not play a gesture once; it makes the named gesture the clip's
  activity and loops it. So a gesture is a move **into a position that then holds** — *her chin lifts a fraction*, *he
  sits back a fraction and stays there*, *his eyes crease with a laugh and stay creased* — or plain stillness. Never a
  blink, nod, head shake, tilt-and-return, look-away-and-back, hand up-then-down. The gate greps for them. A nod the edit
  needs is not generated: a still listener in a two-up already reads as agreement.
- **A hand at the face comes down before the words (L6).** The pose's `entry` sits directly before the first words
  (+0.7 s in the duration) — placed earlier, it was played in the first pause and he spoke with knuckles on his jaw. A
  silent reaction from that pose keeps the hand there.
- **A hand-written gesture names no body contact (L8)** — the start frame is chosen after it is written (*"fingers lift
  from the armrest"* landed on a hands-in-lap pose).
- 🔴 **Every talking prompt says where the eyes stay (L57):** *"Her eyes stay on the person sitting opposite her, off
  frame to the left, from the first word to the last."* (host: *his / him / right*). Positive wording only — naming
  the lens invites it. Exempt: direct address and the turn clip. `prompt_check.py` L57.
- 🔴 **Any movement toward the other person names the side of the frame (L58):** guest *"toward the left of the frame,
  where the person opposite her sits"*, host *"toward the right of the frame"*. `prompt_check.py` L58.
- **Settle versus advance.** Settling gestures (a hand opening and returning to rest, a slow breath, settling back) read
  as ease; advancing ones (a hand pushing forward, a chin lifting, a gaze narrowing) read as pressure. Calm register
  takes settling gestures; advancing ones are reserved for moments that genuinely escalate.
- **One gesture per clip, anchored to a moment in the line** (*"on the last three words"*). Unanchored gestures float;
  two in a short clip read as twitching.
- **Repair kit, for one clip that comes back stiff or fidgeting** — that clip only: state the resting state (what the
  hands do when not gesturing, from the seed frame); state the connective movement into and out of the beat; state one
  involuntary beat (a breath or a settle — never a blink). Still one deliberate gesture.
- **Prompt enhancer:** not available on Turbo, and the gesture paragraphs held without it (`P1_054`). Do not rewrite
  validated wording on a theory.
- **Sound is not written here.** Movement foley on Turbo is thin and inconsistent; the room-tone bed carries the space,
  and a movement that must be heard is placed in the edit.

## 6. Writing the dialogue (checks that still bite at kit stage)

Lines come from the approved outline; these are the checks the kit re-runs, and the reasons they exist.

- 🔴 **Consonant junctions — HARD RULE, enforced by `junction_scan.py`.** A word ending in a stop (/p b t d k g/, alone
  or closing a cluster) running straight into a word whose opening vowel carries primary stress breaks lip-sync.
  *"without Egypt"* failed five times at every duration and position; *"without it"* was clean. The scanner uses the
  CMU dictionary vendored beside it; names it lacks go in `Fixed_Assets/tools/names.dict`. Punctuation counts as a
  release; weak function words do not count as stressed. Fixes that keep the meaning: a pronoun for a just-named noun;
  a vowel-, fricative- or nasal-final word before the name (*"with Antony"*); the name at the start of a sentence; a
  sentence break. **Suspect a junction first** when one patch of a line keeps failing across changes of duration,
  position and phrasing.
- 🔴 **No line ends on a stop-cluster word** (*described, marked, worked, Egypt*) — the last word of a clip is where
  lip-sync is weakest (T8, L12). Also the last word before a `SPLIT` seam. Mode 3 rephrases; a `TAIL` warning in the kit
  means the outline was not fixed — send it back, never reword here.
- **No lone opening word without context** (L50) — *"Allies."* at the top of a clip was said as written. A word that
  fails twice is replaced with a same-meaning wording, with Salah's OK.
- **No mirrored constructions** — say the same thing two different ways instead.
- **Questions end as questions** — a trailing clause after a comma parses as a statement. Two clean interrogatives beat
  one long one.
- **Put the charge, don't make it** — attribute the proposition and invite an answer.
- **Short sentences, simple grammar** — Kling's own guidance; dialogue that cuts off or rushes is script-too-long.
  Never three speakers in one generation.

## 6b. Provenance and the Knowledge Gate — audited before anything is generated

Mode 3 tags every line; Mode 4 carries the tags into the kit and audits them, because an error found after generation
costs credits and one found after publication costs the show's positioning.

| Tag | Meaning | Requirement |
|---|---|---|
| **[D] Documented** | attested in the record | the source is named on the line |
| **[I] Inferred** | consistent with the record, a reasonable reconstruction | the basis is named |
| **[V] Voice** | connective tissue, rapport, phrasing | carries no factual claim |

- **A `[V]` line may not contain a factual assertion** — read down the tag column for smuggled dates, places, numbers.
- **No `VERIFY` survives into a clip** (gate above). The cheapest fix is almost never a rewrite: retag `[D]` → `[I]`
  and let the guest own the claim — a character's characterisation cannot be a lie; the programme's assertion can.
- **Re-read the whole line, not the flagged word** — Part 1's flag said *"'cousin' is loose"*; the same sentence
  asserted a contested will as fact, which was the larger exposure.
- **The Knowledge Gate, re-run on the written lines** (full text in Mode 3): is this in the right mouth (posterity and
  modern framing belong to the host)? did the event happen *the way* the line says? is a named specific available?
- The published source list is audited from the `[D]` and `[I]` tags (§0b): nothing cited that is not used, nothing
  claimed that is not cited.

## 7. Camera, continuity and chains

**Seating never changes.** The host is in the LEFT armchair facing screen-right; the guest in the RIGHT facing
screen-left. `frame_host_direct*` is for direct address only (cold open, narration to camera) — never dialogue.

🔴 **Never cut straight between a direct-address frame and a cross-shot of the same character**, in either direction —
same camera, framing and chair, only the eyes move, which reads as a glitch.

🔴 **The host's turn from camera to the guest (L38, L40):**
- The turn clip is **Turbo, audio on, no end frame**. Its prompt gives the eyeline in frame terms read off the
  guest-facing seed (*a small, slow turn toward the right side of the frame, just past his microphone, eyes level at
  seated head height*), with **no pause between the sentences — the turn takes the whole second sentence, eyes arriving
  on the last word; hands and shoulders stay where they are.**
- **Nothing chains from a turn clip.** Its end eyeline is luck. The builder inserts a **3 s silent guest reaction**
  (Standard, audio off, from a seed, end frame = start) right after it; the edit cuts to her as the turn lands (~1.5 s —
  it doubles as her first look) and the host returns on the built guest-facing seed (`frame_host_b`), whose eyeline is
  right. A snapped take is first retimed in the edit (Mode 6), not regenerated.
- The same logic applies in reverse for a sign-off that turns from the guest to camera.

**Seed frame or chain, decided by what the cut is.** A fresh seed frame is right at a genuine turn (the other person
spoke, or time passed); it is wrong inside one continuous utterance or across an interjection, where the character
would visibly snap back. Those are **chained**: the next clip starts from the previous clip's last frame.
- **The continuity gate** (`chain_frames.py`) fails the same speaker back to back on a fresh seed frame, unless the
  first clip is `audio only` (its picture discarded) or an `OFFMIC` row sits between them (treated as transparent).
- **Chain start frames:** on the website, **Kling's own last-frame feature**; through the CLI, `cli_wave.py` extracts
  the source's last frame with `ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png` — no scale, no range conversion,
  no lift. (A range-converting extractor lifted saturation ~7%, invisible on the frame and obvious at the cut.)
- **A `CUT-IN` stop starts from a frame inside the source clip**, not its last frame — Claude times the cut word and
  extracts that frame to `Shots/start_frames/<ID>_start.png`; the row reads `chain from <src> at <s>s` (L16).
- **Joins are levelled in the edit, not before generation.** Every clip starts ~3.3–4% darker than the image it was
  given. `chain_frames.py` measures each join and writes `JOIN_GRADES.md` — one per-channel gain per chained clip,
  applied to the whole clip in the edit. It fixes brightness and colour-range shifts; it cannot fix clipped highlights,
  a local change, sharpness, or a change of pose or light — **which is why chains stay short: never more than three
  links.**
- **Re-anchor.** Put the host on picture, or a b-roll, every second exchange of a run of her on screen, so her next shot
  can start from a fresh seed.

🔴 **Every silent reaction ends on its own start image (L44):** a seeded reaction has the seed in both slots; a chained
reaction has the source's extracted last frame in both slots — even with the lips a little parted (held a few
seconds it reads as listening, on the point of answering). The end frame pins the whole picture, so nothing wanders in.
**And when the same person speaks next after a seed-start reaction, their clip starts from that seed itself** (L15) —
an exact join with no extraction and no grade (measured: eyeline held, last frame matched the seed; `P1_086`).

**One beat, one clip, one angle.** Each angle is its own performance and audio; cutting angles mid-utterance puts two
performances of one line against each other. An angle change is only ever a turn or a time break.

**Rows added to an existing kit take the previous id plus a letter** (`P1_003a`) so nothing downstream renumbers
(chains, §12, `CARD_PLACEMENTS.md`, kept clips). All tools accept the suffix. A retired row keeps its number empty. A
kit built fresh is numbered contiguously.

**No new pose variant during production** — the library is fixed before the part begins (Mode 2).

**The two-shot appears once: the outro (L59).** No clip with both people in it is generated anywhere else (ruled-out
list). Built per part:
1. **Seedream, three references in order** — `Fixed_Assets/cam3_wide.png` (room, chairs, camera), the host's
   **last clip's** pose frame, the guest's **last clip's** pose frame; no character sheet (the pose frames gave the
   better likeness). The builder writes the prompt with both poses filled in. → `frame_wide_<guest>_outro.png`
2. `outro_mark.py` composites the mark on the panel at the fixed coordinates → `…_outro_marked.png` (the mark goes in
   *before* the charcoal pass, so it is drawn, not stamped).
3. The charcoal end frame on **Kling Image 3.0, 2K, image-to-image**: the series style block + the composition lock.
4. The **5 s transformation**, Standard audio off: start = the marked wide, end = the drawing; v3 camera paragraph, no
   lighting paragraph (the look is meant to change). Prompt: `SERIES_FURNITURE.md`.

The round sheet lists the outro in full until `Shots/<id>.mp4` exists (it was once skipped). ~43 cr a part.

**The act break is `BRAND_actbreak`** — fixed furniture, zero credits, two clips alternated (vessel, stone). Not a
wide and not a charcoal scene: all b-roll is charcoal, so a charcoal scene at a break is invisible as a break.

## 8. Shot types

- `INTERVIEW` — a character speaking on their seed frame or a chain.
- `NARRATION` — the host on `frame_host_direct*`, often covered by b-roll. Same word budget; long narration is
  consecutive clips.
- `INTERJECTION` — two or three words, two or three seconds (*"Mm." "Right." "That's fair."*). Cheap, easy to
  articulate, and the biggest single contributor to the illusion of a real conversation.
- `REACTION` — a character listening, silent. **How it is written (L4, L42, L44):**
  - the mouth described **positively**: *"Her lips stay gently closed and her jaw stays still the whole time; she
    breathes slowly and quietly through her nose."*
  - the eyeline stated: *"Her eyes stay on the person sitting opposite her, off frame to the left."*
  - the pose hold (from the pose table);
  - **one small one-way move and a closing stillness**: *"Her chin lifts a fraction; otherwise she is still."*
  - never a phrase implying other people (*the room, an audience, everyone*); never speech named.
  - end frame = start image (§7).
  - **Generate a distinct reaction for every use** — a reused clip is an obvious repeat.
  - 🔴 **After two failed takes of a short silent reaction, stop paying (L43):** cut the length needed from a kept
    silent reaction of the same guest — same pose as the shot on the other side of the cut if there is one, from a part
    of the episode far from it. A 1–2 s silent face does not read as a repeat.
- `BROLL_GEN` — §10.
- `BUMPER_OUT` — the outro (§7).
- **Repair path for a good take with a bad mouth:** Kling's lip-sync tool remaps mouth movement onto the existing audio
  — cheaper than regenerating and rolling the dice on the performance.

## 8b. Conversational texture — written in, not hoped for

A kit of nothing but `INTERVIEW` rows satisfies every other rule and produces two people reading at each other. Place,
at the moments the drama asks: a **reaction** where the listener's face is the story; an **interjection** where a real
interviewer could not stay silent; a **held beat** where a line needs air; a **cutaway** over the tail of a long line.
**Check:** read down the `type` column — more than three consecutive `INTERVIEW` rows needs a reason; a whole act with
no non-speaking beat is almost certainly wrong. Vary the spacing.

### The director's toolkit — building the outline's tags into rows

Mode 3 chooses the moments; if it marked none where the drama plainly asks, add them here (*would two real people do
this here?*). **Everything is built from single-speaker clips and joined in the edit.**

| tag | rows | `edit_placement` |
|---|---|---|
| `OVERLAP` | a REACTION of the listener (a host reaction during her line becomes a two-up) | `covers [speaker] over [moment], cut back on [cue]` |
| `NOD` | an INTERJECTION on camera; the speaker's next clip chains from it | normal |
| `OFFMIC` | an INTERJECTION, picture discarded (720p) | `audio only, under [other shot] at [moment]` — make sure the covering shot has room |
| `BEAT` | a held listener shot, **on one face**, ~1 s after the last word (≤ 1.5 s once a part) | `plays between [a] and [b], soundscape only` |
| `BROLL` | a BROLL_GEN row | `covers [speaker] from [moment] …` |
| `TWOUP` | the speaker's talking clip + the listener's clip covering the same span | `two-up with [listener shot] from [moment] to [cue]` |
| `SPLIT` | two chained clips (§2) | the seam cover |
| `CUT-IN` | below | below |

#### `CUT-IN` — the talking clip, a chained stop, the interrupter (settled, T5)

The model is **never** asked to stop mid-sentence (it fades or completes the line; both read staged).
1. **A — the talking clip.** Generates the whole line, run-on words included, budgeted for all of it. `spoken_text`
   stops at the cut word with *—*. Cut on a word ending in a vowel or nasal, **where a gesture is in motion** — the join
   hides inside movement.
2. **B — the stop.** REACTION, Standard audio off, 3 s. Starts from **A's frame at the cut word** (§7). Prompt opens
   with the mouth — *"[Pronoun] lips close in the first moment and stay closed."* — then by kind: `cut` *"…her hand stops
   where it is and her eyes go to the left of the frame, where he sits"*; `seen` *"…her hand stops mid-air and her brows
   lift slightly"*; `yield` *"…she lowers her hand, opens it toward the left of the frame, and settles back to listen."*
   Measured: the mouth closes within ~0.4 s and stays closed.
3. **C — the interrupter.** A normal talking clip answering what was heard; register *"comes in over her, firm but not
   loud"*; gesture moving from the first word — no lead-in stillness, or the interruption lands late.
4. **`seen` only — W, the wind-up:** a REACTION of the interrupter drawing breath, covering A a beat before the cut.
5. **`hold` — no chain.** A carries on; the gesture lifts the speaker's chin a fraction at the named word; the attempt
   is a 1–2 s `OFFMIC` (*"But—"*) `audio only, under [A] at "[word]"`.

Placements: A `interrupted by [C] after "[cut word]" — [kind]`; B `follows [A] at the cut, [C]'s audio over it`;
C `enters over [B] — interruption, audio overlaps ~0.3s before the cut`. Until A exists and the word is timed, B's row
says `at cut` and `chain_frames.py` reports it as *needs a cut time*. The reply after a `CUT-IN` may open with seconds of
silence — never on screen: the edit starts her audio ~0.3 s before the cut and her picture after the stop.

#### Two-up (`TWOUP`) — both singles side by side

- 🔴 **Someone is always talking in a two-up (T6b, L10).** One half speaks, the other listens. A silence goes on one
  face — normally hers: cut to her on his last words, hold the `BEAT`, then her answer. `screen_share.py` fails a
  two-up with no talking row.
- **The default way to show a host reaction while the guest speaks** — his reaction *beside* her, not *instead of* her.
- **Cap: at most 7 per part, 3–6 s each, never two in a row, hard cut in and out.** Past that it reads as a video call.
- **Equal halves**, host left, guest right, each a straight crop of its single at native resolution (960 × 1080),
  **never scaled up**. **Crop per pose** — whole figure and hands in the half, room in front of the face: `frame_host_e`
  x=150, `frame_host_d` x=260, guest `_b`/`_e` x=800 on 1916-wide sources (T6a). Divider: 10 px paper-tone gutter with
  the walnut rule, 16–84% of frame height. Reference: `Fixed_Assets/Branding/reference/splitscreen_reference.png`.
- **The listener's half needs a clip as long as the span** — a silent REACTION or a chained clip already in the kit.
- **No text over a two-up** — no lower third, context card or pull-quote.

### Cutting rhythm — planned in the kit, because only the kit sees the whole part

- **Emotion first** (Murch): the picture belongs to whoever is worth watching. Place host reactions on the guest's
  revelations, not only hers on his questions.
- **Tighter early, freer later:** a visual change every ~10–20 s in the first three minutes, ~20–40 s after. **No single
  picture holds past ~40 s** — watch chained runs and b-roll-free stretches.
- **`PUNCH`** — a zero-credit push-in of **at most 15%** on the same clip (1080p source; more turns soft). Two uses:
  emphasis on a key line (held to the end of the clip), and hiding a trim. `edit_placement: punch-in at "[word]"`. Never
  on two consecutive shots, never on direct address; keep the face clear of the subtitles.
- **Dead air** over ~1.2 s inside a talking clip that is not a written `BEAT` is trimmed in the edit, covered by a
  `PUNCH`, a reaction, a card or b-roll.

### Screen share — the guest carries the picture (series rule, 2026-09-24)

The guest is the reason anyone clicks; the host is the lens.
- **Target: the guest ≥ 65% of studio time** (aim 65–70%) — her full frame plus two-up time, over her full frame + his
  full frame + two-up. B-roll and furniture are left out; two-up time is reported separately so a kit cannot reach the
  target by living in split screen. `screen_share.py` is the gate.
- **His questions, charges and pushes play on her face:** the line starts on him and cuts to her **listening** (a guest
  REACTION her answer chains from, or starts from its seed) as it turns to her; a short push runs wholly under her
  (his clip then 720p audio-only).
- **He stays on his own face for:** his fixed slots (cold-open address, sign-off, Part 2's re-open), a line that turns
  to a new subject, his first question (his lower third), short re-anchoring interjections, and lines where his face
  *is* the moment.
- **At most two full-frame host reactions per part** (the crack, or a card that needs his side of the room). A `CUT-IN`
  stop does not count.
- **Composite eyewitness guests:** full-frame host reactions are allowed on the hardest testimony so a witness defending
  the indefensible is never left unanswered on screen; the 65% target stands. The gate relaxes the count when the kit
  header says `composite: yes`.

Every talking, reaction and b-roll row carries a `screen:` line (`G 3.2 · H 1.1 · 2UP 0 · BROLL 0`), and the row that
opens a two-up carries `twoup: #n`. The builder computes them; the gate sums them.

---

## Generating

🔴 **Through the Kling CLI, in waves (L52).** Claude runs
`python3 Fixed_Assets/tools/cli_wave.py Episodes/<Guest> --max N`: it lists the clips that are READY (seed start, or
chained from a clip already kept in `Shots/`), extracts each chained clip's start frame, and prints the one
`node Fixed_Assets/tools/kling_run.mjs …` command. **Salah runs it on the Mac — running it is the approval of the
spend.** Takes land in `Shots/_tests/`; Salah looks at them; Claude moves the kept ones to `Shots/<ID>.mp4`, which makes
the next wave (their chained clips) ready. The first wave on a new guest or a new prompt structure is five mixed clips.
- Settings come from each sheet header: Standard audio off (reactions, same image as `--tailImage`), Standard audio on,
  Turbo 720p (audio only), Turbo 1080p. **Kling 3.0's CLI defaults are dangerous** — 4k, multi-shot on, audio off — so
  `kling_run.mjs` always passes `resolution 1080p` and `prefer_multi_shots false`.
- **Downloads use `urlWithoutWatermark` only** (L20); `--refetch ID:gen` re-downloads clean for free.
- **2 clips at a time; each image uploaded once per run; automatic wait-and-retry** on a rate-limit reply (L26).
- **B-roll through the CLI in two steps (L54):** `kling_broll.mjs <Guest> stills <ids>` (Kling image 3.0, 16:9, 2k →
  `Shots/stills/`); Claude checks the stills for anachronism (§10); then `kling_broll.mjs <Guest> video <ids>` (Turbo
  1080p from each still → `Shots/_tests/`).
- **The website is the fallback** — the round sheet (`round_sheet.py`) lists every clip in kit order with its settings,
  each chained clip directly under its source (marked *↳ chained*, made right after the source is saved, from Kling's
  last-frame feature). Paste each block whole, chip OFF. A seed frame waiting to be regenerated holds its rows
  (`round_sheet.py … --hold frame_x`).
- The last-frame button is web-only; the CLI route extracts it itself (§7).

🔴 **No per-take checking by Claude during generation.** Salah judges each take by eye. Claude measures a take only when
asked, or when something must be measured before the next clip can be made — the frame at a `CUT-IN` cut word.
Loudness, pauses, lead-ins, tight endings and small drifts are handled once, at the start of the edit
(`batch_check.py`, Mode 6).

🔴 **The clip ledger (L17).** A kept clip lives at `Episodes/<Guest>/Shots/<ID>.mp4` — that file IS the record.
`clip_status.py` reads the folder and lists kept / to do / credits left. `CLIPS.md` holds notes only where there is
something to say (a take kept with a known flaw, a retake reason, `REGEN <ID>`). Rejected takes go to
`Shots/_tests/_rejected/` or `_not_used/`, never deleted by Claude.

**Watch the first clips from any newly edited seed frame for corner intrusion** (`batch_check.py` CORNER).

---

## 9. The kit — format

### Header and front matter
`part`; `anchor_images` (every asset with its path, viewed before writing — seed frames, stills, furniture); the
locked blocks (both `Voice:` lines, the audio lines); the voices (ElevenLabs IDs); guest prompt label and pronouns;
§1 Settings (the model table above, **chip OFF**, v3 structure); §2 Totals; §2b Screen share; §3 Start frames used;
§4 Generation order and **the chain table**; §4b the test batch (new guest, Part 1); §5 Reading a row.

### Shot list — sequential, in final timeline order, one row per clip
- `shot_id` — `P[part]_[###]`, the number is assembly order; inserted rows take a letter.
- `type`, speaker, **duration** (§2) and credits in the row header, with the model line.
- `start_frame` — the exact seed frame, or `chain from [id]` (or `at <s>s` for a cut-in). A row without it is not
  finished. `end_frame` on every reaction.
- `prompt` — paste-ready, v3 structure (§3), one line per paragraph.
- `spoken_text` / Subtitle — true spelling, no direction.
- `sfx` — diegetic sound named inside the prompt; post additions only from the registered set (`SFX_sand`,
  `SFX_plate`, `ROOMTONE_studio`) or with a new asset registered in `STUDIO_ASSETS.md`.
- `screen:` line (§8b), provenance tag, and `edit_placement`.
- **`edit_placement` — required on every silent row.** Intent, never timings (in and out points are measured at
  assembly). One of:
  - `covers [id] over [moment], cut back on [cue]`
  - `covers the tail of [id], then holds a beat` — also hides the point where a mouth is weakest
  - `plays between [id] and [id], soundscape only`
  - `audio only, under [id] at [moment]`
  - `diegetic only` (b-roll on its own sound)
  - `two-up with [id] from [moment] to [cue]`
  - `interrupted by [id] after "[word]" — [kind]` / `follows [id] at the cut, [id]'s audio over it` /
    `enters over [id] — interruption, audio overlaps ~0.3s before the cut`
  - `punch-in at "[word]"`

Runtime is the sum of on-screen time; a cutaway adds a generation but no runtime, so **budget on generated seconds**.

### The chain table — required
Every row whose start is `chain from` is listed (`chained shot | starts from | source type | start frame file`); a
`CUT-IN` stop says *at the cut word*. The table must agree with the rows — `chain_frames.py` reads the rows. If a kit
has none, the table is present and says *none*.

### The completeness test
The kit is generated blind and assembled later. **Every decision needed to cut the part must be in the kit** — which
shot covers which, whose audio runs under a silent row, where a beat is held, what a reaction reacts to. Read the shot
list as if you had never seen the script and had to cut it; anything you would have to ask about is missing.

### Budget
**Runtime is the cost.** The talking spine is ~85% of a part's spend; every minute of talking is ~600 credits at
Turbo 1080p. Target 10–12 minutes of spine. Cutting b-roll to save money is a false economy — cut a question instead.

## 9b. Assembly

Assembly runs after the voice pass, at the start of the edit chat, and its procedure is in **Mode 6, *Assembly*** —
one place, so the two files cannot drift. The kit carries intent; assembly resolves it by measurement.

## 10. B-roll

**All generated b-roll is charcoal and graphite on toned paper.** Tested against photoreal and won on measurement: the
sketch (value 0.471, saturation 0.236) reads as a deliberate shift from the studio (0.354 / 0.463), where photoreal
(0.314 / 0.496) sat almost on the studio's own numbers — the ambiguity a reconstruction show must avoid. The style
held through an 8 s clip with no drift to photoreal.

### The style block — pasted byte-identical

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.
```

For a video prompt add: *"It stays a drawing for every frame of the clip; the tone and the paper grain remain visible
throughout, and it never resolves into photographic footage."* — stating the style once is not enough.

Why the wording: the first sketch came back **graphic-novel** (hard helmet highlights, gold accents, drawn contours).
*"Forms built from tone rather than outline"* is the load-bearing phrase; any highlight material (*white chalk*) invites
hard glints; the model adds warm metal to armour and jewellery unless it is excluded. The block does not name what it
avoids (*"not a graphic novel"*) — naming it puts it in the prompt. When in doubt, push toward wash.

### Two steps, every row
1. **A still — Kling image generation** (image 3.0, 16:9, 2k, as tested), in the charcoal style, holding the pose the
   video will move out of: the subject at rest, nobody mid-stride.
   - **No reference image for anonymous extras** (clone faces). Identity for a crowd comes from the registered
     **wardrobe text block** (`STUDIO_ASSETS.md`), pasted byte-identical, plus the composition.
   - **Describe crowds by arrangement, not count** (*"seen from behind, one rank behind another, receding"*).
   - **Run the Period Accuracy Gate** (Mode 2) on anything worn or carried.
   - 🔴 **Date every object, and ban what comes later (L55).** Name the place and year (*"the Great Harbour of Alexandria
     in 48 BC"*), give each object its period form (*"ancient oared war galleys: long low hulls, a bronze ram, one mast,
     a single square sail"*), and end with the later forms it must not show (*"no cannon or gun smoke, no ship with more
     than one mast, no pitched roofs, no hats, no colour"*). **Claude checks every still for anachronism before the
     video step.**
   - **Prefer a close shot of one period object** (a ring, a shrine niche, amphorae on a quay, a ram at the waterline) —
     close shots were right first time; wide views of ports and fleets drifted to later centuries. A wide gets one
     retry, then becomes a close shot.
2. **The video**, image-to-video from that still, Turbo, audio on.

### The video prompt describes MOTION, not content — four paragraphs, no more
1. **The move** — one camera move, named. 2. **The medium, stated as persisting.** 3. **What moves** in the frame.
4. **The audio.** Re-describing the still invites reinterpretation instead of animation.

**Camera moves are allowed on b-roll** (and forbidden in the studio): slow push in (drawn toward something), slow pull
back (reveals, endings), slow tilt (scale, detail to context), slow lateral drift (reliefs, objects, texture). One move,
slow, with a reason; never handheld. The locked interview is what gives a moving cutaway its value.

**"Nothing happens" is correct for b-roll under dialogue** — an event on screen pulls attention off the line.

**IP filter safety applies hardest here:** describe the aesthetic, never the label, in visual prompts (the spoken line
may name people and places freely). Period place-and-year dating for anachronism is the exception the image model needs.

*Assembly note:* b-roll warms and darkens slightly across a clip — normalised against its own first frame in the edit.

## 11. Supporting sections of the kit

- `primary_sources` — the texts and scholarship behind the guest's lines.
- `trust_disclaimer` (§8) — the disclosure wording, carried into Mode 5 in short form.
- `youtube_metadata` (§9) — written to the fixed labels in **§15**. The source list lives in `card_data_p<n>.json`.
  **The series index is `Part N of 2`, on every title** — an arc is two parts; a stale part count is the one metadata
  error every viewer sees.
- `soundscape` (§10) — room-tone continuity, the `MUSIC_*` cues and where each enters and exits, any non-diegetic
  layer. Diegetic sound is named per shot. The show runs dry by default (`SERIES_FURNITURE.md`).

## 12. Structure

- **Part 1:** the opening (§0), the acts with their two act breaks, and a close on a tease that works as an invitation
  rather than a withheld ending, then `BRAND_bumper_out` and the end card. No goodbye after the tease.
- **Part 2:** first re-reads Part 1's kit and carries its voices, seating, wardrobe, disclaimer wording and established facts forward unchanged; it re-establishes the stakes in **one exchange** (not a recap), the host's welcome-back, and closes
  definitively. The end card's "next" is the next guest or nothing.
- **An arc is two parts.** Part 1 must work as a complete argument on its own — it is the only entry point the arc has.

## 13. Saving

Save the kit as `Episodes/<Guest>/P<N>_kit.md`, built by `Episodes/<Guest>/_kit_source/build_p<N>_kit.py`, so the
folder stays self-contained and the kit can be rebuilt after any outline or pose-table change.

## 13b. On-screen text — placed in the kit

**Key lines — three or four per part**: short, self-contained, strong read cold in silence. One set feeds three
consumers — the `BRAND_pullquote` graphics, the thumbnail overlay candidates (§14) and the reel hooks (Mode 5).
*"You assume those were two things. For me they were one."* qualifies; a line that needs the scene around it does not.

- **A pull-quote lands after its line, over the guest's own held face** — a beat at the head of her listening clip —
  never over the line itself (the subtitle already carries it) and never over a two-up. Three or four per part is the
  ceiling.
- **The hook line is not pull-quoted if it stays the hook.** Place it if it earns one and flag it in §12; Mode 6 drops
  that pull-quote if it keeps the line as the hook.
- **Lower thirds — two per part:** the host on his first question, the guest on her first appearance (the welcome
  reaction). Never on the hook. Contents and treatment: `STUDIO_ASSETS.md`.
- **Context cards** (Mode 3 writes them; §12 carries the table `# | Lands on | Word | Side | Label | Name | Gloss |
  Source`):
  - **Side** is opposite the voice: `L` when the guest speaks, `R` when the host speaks.
  - **Enters as the word is said, holds 5.5 s.** May ride over or enter on a b-roll cutaway; never overlaps a reaction
    of the other person, a lower third or a pull-quote.
  - 🔴 **A card never rides onto the other person's face — including their talking shot.** Check the time left in the
    speaker's picture after the word: ≥ 5.5 s. If not, in order: (1) move the anchor to the other person's mention of
    the word, if they say it (the card flips side); (2) cover the start of the reply with a listener reaction chained
    from the speaker's clip until the card has gone; (3) ride the card over a b-roll row covering the join.
  - **Write the constraint, not only the word (L62).** When a placement names a word only to satisfy timing — *"cut
    back to her after card 06 has gone, around 'with'"* — the constraint is the instruction and the word an estimate
    from model durations; the edit moves the cut to the nearest sentence boundary that keeps it. Size a covering
    reaction for the span it must cover (Cleopatra `P1_072`, 3 s, was 1.2 s short of *"to his enemy"*), and a two-up's
    hold after the line from the take's own tail, not a fixed ~1.5–2 s. A card whose word is the speaker's **first**
    word cuts to the speaker with the voice, not on the usual J-cut — note it in the row.
  - **One text at a time** — where a `[D]` source credit (Mode 6) would land at the same moment, the card's source line
    is that credit.
  - `context_build.py check` fails any gloss past three lines.

## 14. Packaging — delivered with the kit

- **Three title options** — written in §9 to the §15 rules (the Test & compare set).
- **Chapter titles, one per act** (plus `0:00` for the opening) — short, specific, curiosity-led. Mode 6 fills the
  timecodes. YouTube needs the first at `0:00`, at least three, each ≥ 10 s.
- **Three thumbnail overlay lines** — 3–5 words, all caps, readable at phone size, lifted from what the guest says.
  The title carries the subject, the thumbnail the provocation — **never the same thing**. No question marks. The guest
  name and part number sit in a small kicker above the line (`CLEOPATRA VII · PART 1`) — for a series grid, the name
  indexes the channel page.
- **On composite eyewitness episodes** the title and overlay foreground the *event*, never the character's defence —
  *"STALINGRAD, FROM INSIDE THE POCKET"*, not *"A GERMAN SOLDIER TELLS THE TRUTH"*.
- **The thumbnail system is settled — `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`:** the guest's photoreal portrait lit
  for paper (made once at casting, reused for both parts), the fixed toned-paper ground, ink type. Two separate
  generations composited — never one prompt for a photoreal figure in a drawn world. Only the kicker and the statement
  change per part. `THUMB_<guest>_p<n>.png` is rebuilt for every part.

## 15. The publish words — kit §9, assembled into `P<n>_PUBLISH.md`

Uploading a part is copy-paste, not writing. Mode 4 writes the *words* into §9 under fixed bold labels;
`publish_sheet.py` assembles them with the chapters (§11), the sources (`card_data_p<n>.json`), the disclosure (§8) and
Mode 6's timecodes into one sheet in YouTube Studio's field order.

```
## 9 · YouTube metadata

**Titles** (Test & Compare set — the first is the primary)
1. …
2. …
3. …

**Description hook.** …
**Summary.** …
**Heard vs the record.**
- *Heard:* … *Record:* … (`P<n>_0xx`)
**Tags.** a, b, c, …
**Hashtags.** #A #B #C
**Pinned comment.** …
**Playlists.** …
**End screen.** …
**Series index:** `[Part N of 2]`
```

| Label | Rule | Why |
|---|---|---|
| **Titles** | Exactly three, each ≤ 70 characters, each with the series index; the primary names the guest; **words in quotation marks are the guest's line verbatim** (the tool checks); the three differ in *angle* (quote / charge / event) | Test & compare picks on watch time, so a misleading title loses by itself; a misquote is a factual error on the most-read line |
| **Description hook** | Two sentences; the guest's name and the subject's search word in the first 150 characters | That is all that shows above "…more" |
| **Summary** | 200–300 words of plain prose in the words people search; no keyword lists | Real language for the index |
| **Heard vs the record** | 1–3 items: a popular belief, what the sources say, the shot id carrying the correction | The show's strongest evidence of method |
| **Tags** | 10–15, ≤ 500 characters: name and spellings, period, place, events, the format | They catch misspellings |
| **Hashtags** | Exactly three: guest, period, `#History` | YouTube shows the first three |
| **Pinned comment** | One question a viewer answers from their own opinion | An engagement signal beats "like and subscribe" |
| **Playlists** | The series playlist + the guest's two-part playlist | Carries viewers from Part 1 to Part 2 |
| **End screen** | Part 2 (on Part 2: the next guest's Part 1) + subscribe | |
| **Series index** | `[Part N of 2]` | §11 |

**Check before the kit is done:** `publish_sheet.py Episodes/$G --part $N --words-only` (exit 0). **The sheet itself is
built in Mode 6** once the cut exists. The tool also carries the settings Studio asks for every time — **Altered or
synthetic content → Yes**, category, language, captions, audience. Channel-level values live in
`Fixed_Assets/publish_defaults.json`; a `TODO` there blocks the sheet.
