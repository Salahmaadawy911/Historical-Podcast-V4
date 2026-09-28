# SKILL: MODE 6 (FINAL EDIT & BRANDING)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.


> 📂 **Inputs and output — added 2026-09-19 so each mode can run in its own chat.**
> **Reads:** `P<n>_kit.md`, `CARD_PLACEMENTS.md`, the generated clips, and the fixed assets.
> **Writes:** the clean master and the titled master of the part, plus `Episodes/<Guest>/P<n>_EDIT_NOTES.md` for anything the next part must carry forward, and the publish files — `P<n>_TIMECODES.txt`, `P<n>_captions.srt`, `P<n>_PUBLISH.md` (see *Publishing*).
> **Save the output to that file before the mode ends.** Anything that lives only in chat history
> is lost to the next mode.


Status: **partly specified.** The audio rules, source attribution, the description's generated source list and the series furniture are settled; timeline mechanics and export settings are still scaffold. Asset specs live in `Fixed_Assets/SERIES_FURNITURE.md`.

## Scope
Mode 6 covers everything that happens after every clip has been generated. Nothing in this phase touches the generator; it is entirely editor work, using edit-phase assets (`MUSIC_*`, `BRAND_*`) that are never uploaded for generation.

Expected to cover:
- Timeline assembly from Mode 4's shot list, in `shot_id` order.
- Score placement per Mode 4's `soundscape_design` — where each `MUSIC_*` tag enters, exits, and ducks under dialogue.
- Room-tone continuity across cuts, and any non-diegetic layer generation could not supply.
- Channel branding: logo/watermark, lower thirds naming the guest, intro and outro bumpers, end card.
- YouTube furniture: subscribe animation, chapter markers, cards, thumbnail hand-off.
- The trust disclaimer's on-screen treatment as a title card, per Mode 4's wording.
- Subtitle burn-in or caption file, built from each shot's `spoken_text`.
- Export settings, matched to the resolution the part was generated at.

## Assets
Branding files live in `Fixed_Assets/Branding/`, score files in `Fixed_Assets/Audio/`, both registered in `STUDIO_ASSETS.md`. **The `BRAND_*` and `MUSIC_*` sets are now fully specified in `Fixed_Assets/SERIES_FURNITURE.md`** — what each one is, how long it runs, where it sits in a part, how it is generated, and the order to build them in. The files themselves do not exist yet; the specs do.

## Scope boundary with Mode 4
Mode 4 assembles each part — dialogue, cutaways, reactions, B-roll, room tone, colour
matching, cutting rhythm — and delivers a finished part, because the person who wrote the
shots knows the intent behind every cut. Mode 6 starts from assembled parts and adds only
what belongs to the whole episode: score placement, branding, titles, subtitles, export.
Mode 6 never re-cuts dialogue.

## Cutting the conversation — the default grammar

Added 2026-09-20; Mode 4 places the moments, this is how they are cut.
- **Emotion first, then story, then rhythm** (Murch). Cut to whoever is worth watching.
- **Speaker changes are J-cuts by default:** the next speaker's audio leads the picture by roughly
  4–8 frames, varied — sometimes longer, sometimes an L-cut holding on the listener through the first
  words of the answer. **Never ping-pong** — a cut exactly on every first syllable reads as automated.
- **Cut at a sentence end or a breath, never mid-word.** A listener's natural blink is a good cut
  point — the eye already reads it as punctuation.
- **Trim silent lead-ins** — a clip can open with seconds of silence before its first word (P1_046: 3.2 s); start it at the word, or ~0.3 s before the cut for an interruption (LESSONS L13).
- **Trim dead air** over ~1.2 s that the kit did not mark as a `BEAT`; hide each trim with a `PUNCH`
  (≤15%), a reaction or a card. Then do an **ears-only pass** — play the part without picture — to
  catch any audio seam the picture was hiding.
- **`PUNCH` holds** to the end of its clip; no zoom animation, no two in a row.
- **`TAIL` lines** (a last word ending on a stop cluster — Mode 3 rule 5, no exceptions since 2026-09-24): there should be none. If an older clip has one, cut away on the end of that word, or run it through Kling's lip-sync tool if the strain shows.
- **Chained joins:** apply `shots/_measure/JOIN_GRADES.md` — one filter per chained clip, on the whole clip, written by `chain_frames.py`. Do not hand-tune; if a join still shows after it, the fault is content (pose, sharpness, a local colour change), not grade — flag it for regeneration.
- **Chapters** from the kit's chapter titles: first at `0:00`, at least three, each ≥ 10 s.
- **Cut the goodbye:** nothing after the tease but `BRAND_bumper_out` and the end card.
- **The guest carries the picture (2026-09-24, Mode 4 §8b *Screen share*).** A host question starts on
  him and cuts to her listening as it turns to her; short pushes run entirely under her face. His
  reactions during her lines are two-ups, not cutaways. If the edit needs to trade a shot, trade it in
  her favour — the kit's `screen:` lines add up to ≥ 65% guest, and the cut should not fall below it.

**Small camera drift (L31):** a kept take marked *small drift* (4–8 px of slow pan in `CLIPS.md`) gets Resolve's
stabiliser (camera lock mode) on that clip only; if it still shows, it goes back as a website retake.

🔴 **First step of every edit: the one full check (Salah, 2026-09-26).** Generation is not checked take by take;
the edit starts with one pass over the whole part:
`python3 Fixed_Assets/tools/batch_check.py Episodes/<Guest>` → one line per clip. It becomes the edit's to-do list:
- **PAUSE > 2 s / LEAD > 1.5 s** — trim (hide with a punch, card or reaction);
- **TIGHT** — listen to the last word; clipped → retake;
- **QUIET** — level in the mix (the ElevenLabs pass re-renders the voice anyway);
- **SMALL-DRIFT (4–8 px)** — Resolve stabiliser (camera lock mode) on that clip; still visible → retake;
- **CAMERA-MOVED / CORNER** — retake from the round sheet (v3 prompt, L51) before the cut is locked.
Claude looks at frames only where a flag says to.

## The host's turn always leaves on a cut to the guest (2026-09-27, L40)

Cut from the turn clip to the guest cut-away (e.g. `P1_003a`) as the turn lands — on the last word or just after — and
never hold on where the turn ends: its end eyeline is not the seed's. About 1.5 s of her face, then the host's next clip,
which starts from the built seed with the right eyeline.

## A turn that lands too fast — retime, don't regenerate (2026-09-26, L38)

When a head turn (the direct-to-guest turn above all) happens in a silent gap and snaps in well under a second:
slow just the turn to ~50–60 % with optical flow (DaVinci: Speed Warp, else Optical Flow), then cut out the still
hold after it so the gap before the next words stays ≤ ~1.5 s. Fill the gap with the clip's own room tone. Check the
ears, hands and mic arm for warping at the slowed frames; if it warps, remake the clip from the round sheet
(the prompt now asks for a slow turn spread over the line).

## Voice pass folders (2026-09-27, Salah)

Before the voice pass, run `python3 Fixed_Assets/tools/voice_folders.py Episodes/<Guest> --part <n>`. It copies every
talking clip (including audio-only ones) from `Shots/` into `Voice/P<n>/1_host/` and `Voice/P<n>/2_guest/`, so each folder
goes through ElevenLabs voice change with one voice. Converted files are saved to `Voice/P<n>/done/` under the same clip name (ElevenLabs returns **MP3 audio**, e.g. `P1_006.mp3`);
the edit lays each MP3 under its clip's picture from `Shots/` (after the 1152-sample head trim), everything else straight from `Shots/`. `Shots/` is never changed. Re-run after any retake
— it copies only new or retaken clips and says how many are left to convert.

## Two-up — both faces at once

Added 2026-09-22 (Mode 4 §8b, `TWOUP`). Crop each single to its half at native resolution — host
centred on his face in the left 960 px, guest in the right — never scale up. 10 px paper-tone gutter
(`#CDC1AC`) with a 3 px walnut rule (`#9C6B3F`) from 16% to 84% of frame height. Hard cut in and out.
The audio is simply the timeline's: the speaker's line, and under it any off-camera line the kit
places. Apply each half's join grade if it is a chained clip. No lower third, card or pull-quote over
it. Reference frame: `Fixed_Assets/Branding/reference/splitscreen_reference.png`.
🔴 **Someone is always talking in a two-up — never both faces only reacting** (T6b, 2026-09-24). A silence goes on one face, and a `BEAT` is held about 1 s after the last word, no more.
**Since 2026-09-24 the two-up is the default for a host reaction during the guest's speech** (up to 7 per
part, 3–6 s each, never two in a row). Cut in on the word the kit names, out on its cue; if a two-up
would run into a lower third, card or pull-quote, end it early rather than lay text over it.

## Split lines — hiding the seam

Added 2026-09-22 (Mode 4 §2, `SPLIT`). One line in two chained clips, A then B. Audio: **A's line, its
natural pause trimmed to a breath, then B's line** — play the seam ears-only; it must sound like one
person continuing. Picture, as `edit_placement` names it, best first: **(a)** cut away across the seam
(listener, b-roll or off-camera line), returning on B; **(b)** a `PUNCH` exactly on the seam; **(c)** a
plain cut on the pause. Apply B's join grade from `JOIN_GRADES.md`. If the seam still shows in pitch or
energy, move it under a cutaway rather than tuning the audio.

## Overlaps and interruptions — cutting what Mode 4 placed

Added 2026-09-20; refine against the first real one. Mode 4 §8b decides every placement; the edit
only executes it.
- **`audio only, under X`** — lay the interjection's voice (after its voice pass) under X at the
  named moment, about 3 dB below the on-screen speaker. Picture discarded.
- **Interruption (`CUT-IN`)** — three pieces from Mode 4: A (the interrupted speaker's talking
  clip), B (their chained stop, silent), C (the interrupter). Never fade a cut-off voice — a fade is a polite ending.
  - **Picture:** A up to the cut word → B from the same frame (the join is invisible if the kit
    chose a word mid-gesture) → C once B has shown the stop, usually 0.6–1.2 s in.
  - **Sound:** A's audio ends hard just after the cut word; C's audio starts **~0.3 s before** that,
    so the voices collide, and runs on under B. Audio early, picture late: that is what reads as
    an interruption rather than a turn.
  - `seen`: the wind-up W goes in over A a beat or two before the cut.
  - `yield`: hold B longer, through the whole overlap — the giving way *is* the shot.
  - `hold`: no B. Stay on A; the off-camera *"But—"* sits under the speaker at the named word, ~3 dB down,
    and they carry on over it.

## Brand overlay on wide shots
Every wide clip gets `BRAND_mark` composited onto the studio panel: dark ink, 85% of the
panel face width, centred, at the fixed coordinates in `STUDIO_ASSETS.md`. The camera never
moves and the panel is generated blank, so this is one static filter at constant coordinates
— no tracking, no per-shot adjustment, identical in every episode.

Cross-shots get `BRAND_symbol` light, **bottom-left**, 40% opacity. Bottom-right collides
with the microphone stand.


## The opening with its hook — rendered per part, first thing in the edit

```bash
python3 Fixed_Assets/Branding/intro_source/hook_build.py Episodes/<Guest>/shots/<hook shot>.mp4 <in s> \
        Episodes/<Guest>/BRAND_opening_p<N>.mp4 --face <CX,CY,H from CAST.md "Hook framing">
```
**Re-pick the hook first (added 2026-09-23).** The kit's hook is Mode 3's first option. Before rendering,
watch the assembled part and choose the **most shocking guest moment on screen**, where line, face and
delivery work together. It can be any guest sentence in the part, and must be a clean single with the
face turned to the camera side and a closed mouth after the line. Run it past Salah, then record the
change in the kit's opening row and in `OUTLINE.md`'s `HOOK:` line.

The in point and the hook shot are in the kit's `P1_001` row (re-measure on the final take: the line
should start ~0.4 s after the in point). The script reports where the line ends and whether it had to
freeze. Use `BRAND_opening_p<N>.mp4` at 0:00 in place of `BRAND_opening.mp4` — never edit the fixed file.
Use the **voice-passed** hook audio (the clip after its ElevenLabs pass), so the hook sounds like the episode.

## Fixed brand assets — built once, reused every episode

- **`BRAND_disclosure`** — the 0:00 card, 3 seconds. Black, brand mark small at the foot, one soft brand sting under it, never true silence. Two lines exactly:

  > AI-GENERATED DRAMATIZATION
  >
  > Historical reconstruction, not a recording.

  Byte-identical in every episode, never rewritten per guest; if it changes, it changes for the whole series at once. The full statement — *"This programme is an AI-voiced dramatization. The guest is a historical reconstruction, not a recording. Dialogue is built from documented actions, primary sources, and academic consensus."* — goes in the video description and on `BRAND_endcard`, not on the opening card.
- **`BRAND_composite`** — eyewitness episodes only. Placed at the end of the cold open, immediately before the guest first appears in the studio, not at 0:00. Same visual treatment as the disclosure card, ~4 seconds. Wording fixed in shape, filled per episode:

  > This guest is a composite. No such individual existed.
  > The character is assembled from [N] first-hand accounts, listed in the description.

  Never used on a named-figure episode.

- **`BRAND_bumper_in` — BUILT.** `Branding/BRAND_bumper_in.mp4`, 5s, drop it in as-is. **Cut `MUSIC_Theme_Main` so its strongest beat lands at 2.35s**, where the sand reverses — that is where the show's premise arrives and it must be heard as well as seen. The music stops dead with the sand at 2.0s; do not duck through the pause, gap it.
- **`BRAND_endcard` — a clean paper card**, cross-dissolved to from the held drawing, carrying the disclosure, the sources generated from the provenance tags, the next part, and the mark. **No credit roll** — see `SERIES_FURNITURE.md` for why. Keep the right third clear for end screens.
- **The ending is three beats:** the 5s transformation clean, the drawing held ~3s clean, then the card. Do not put text on the transformation.
- **`BRAND_bumper_out`**, **`BRAND_subscribe`** — fully specified in **`Fixed_Assets/SERIES_FURNITURE.md`**, which also carries the placement map for a whole part, the six `MUSIC_*` generation prompts, and the room-tone build procedure. Read it before building any of them.

  The intro and the cards are motion graphics and need no generation. The outro is a single clip of the **empty** studio, generated once from `cam3_wide.png` — it is guest-agnostic, which is what lets it be a fixed asset at all, and it removes a 150-credit-per-part wide along with the only two-character generation in the pipeline.

The brand sign is composited onto the wide shot here, not generated into the plate — **except in the outro**, where it goes onto the still *before* the charcoal pass so that it is drawn rather than stamped. See `Fixed_Assets/SERIES_FURNITURE.md`.

## Lower thirds and pull-quotes

Both are built here, both are **fully specified in `STUDIO_ASSETS.md`** — geometry *and* visual treatment, the latter approved against real frames — and both are *placed* in Mode 4 — the kit says which shot each one opens over. Do not invent placements at the edit; if a kit is missing them, that is a Mode 4 gap to fix at source, not to improvise around.

- **`BRAND_lowerthird`** — twice per part only, host and guest, on first proper appearance. Never over the teaser.
- **Both plates carry `SFX_plate` on the entrance only** — one soft paper settle, dry and close, mixed far under dialogue. **Exits are silent**: a sound on the way out draws attention to something leaving, which is backwards. Never a whoosh — same rule as the subscribe card.
- **`BRAND_pullquote`** — three or four per part, each landing over the silent reaction shot that follows its line, never over the line itself.
- **`BRAND_context_NN`** — context cards, rendered from the kit. Enter **on the word** named in `CARD_PLACEMENTS.md` (the first syllable, not the end of the line), hold 5.5 s, opposite the speaker, upper band. `SFX_plate` on the entrance only, and quieter than on the name banner — these come often. Where a `[D]` source credit would land at the same moment, drop the credit: the card's source line already carries it. Never over a reaction of the other person.

## Source attribution on screen

When the guest states a checkable fact, put the source on screen as a small lower-third for two or three seconds — *Plutarch, Life of Antony*; *Cassius Dio, Book 42*.

**Which lines get one is not a judgement made here.** Every line in the kit carries a provenance tag from Mode 3 (`[D]` documented, `[I]` inferred, `[V]` voice). On-screen attribution goes on **`[D]` lines**, using the source named on the line. `[I]` lines are not attributed on screen — an inference with a citation under it reads as a claim the source does not make — and `[V]` lines carry no factual content by definition.

This is cheap and it is the most legible evidence that the episode is researched rather than generated. Most of what separates this show from templated AI output happens upstream and is invisible on the watch page; on-screen sourcing is one of the few places it becomes visible to a viewer, and to a reviewer, in the first minute.

## The description's source list is generated, never assembled

Publishing a source list is making a claim, so the list is **derived from the kit's provenance tags** — built from every `[D]` and `[I]` line's named source or basis, deduplicated.

The two checks that make the claim honest: **nothing cited that is not used**, and **nothing claimed that is not cited**. A list written alongside the script rather than out of it will drift from what the episode actually says, and it drifts in the direction that looks better.

Where the episode corrects a popular story rather than repeating it, say so in the description and name the correction. Those lines are the show's best evidence of its own method.

## Publishing — the copy-paste sheet

**Added 2026-09-23.** The last step of every part, after the master is exported:

1. **Write `Episodes/<Guest>/P<n>_TIMECODES.txt`** from the finished timeline — one line per chapter shot listed in the kit's §11, giving where that shot starts **in the final master** (the opening included), plus the master's length:
   ```
   P1_008 1:12
   P1_033 3:40
   P1_059 6:05
   P1_077 8:52
   end 11:48
   ```
   Round down to the second. Chapter 1 is always `0:00` and needs no line.
2. **Export the caption file** as `P<n>_captions.srt` beside it, from the spoken text. Uploading it beats auto-captions, which get the names wrong (*Ptolemy*, *Actium*).
3. **Run** `python3 Fixed_Assets/tools/publish_sheet.py Episodes/<Guest> --part <n>`. It writes `P<n>_PUBLISH.md` and exits 0 only when the sheet is ready. It checks: three titles with the series index and verbatim quotes, the guest named in the first 150 characters, exactly three hashtags, tags ≤ 500 characters, description ≤ 5000 characters and free of `<` `>`, ≥ 3 chapters starting at `0:00` and each ≥ 10 s, a source list, the AI-disclosure statement, the thumbnail file, and no `TODO` in `publish_defaults.json`.
4. **Upload by following the sheet top to bottom** — it is in Studio's order: Details → Show more → Video elements → Test & compare → after it is live (pinned comment).

The sheet is generated, never edited. A wrong word is fixed in the kit's §9 (or §11, `card_data`, the timecodes) and the tool re-run.

## Audio — three rules, all measured

The voice pass changes the audio in ways that are invisible until several clips sit together. All three of these are mechanical and belong in one batch step before assembly.

**1. Loudness-normalise every converted clip to one fixed target.** ElevenLabs speech-to-speech returns audio roughly **10 LUFS below source** — measured at −34.0 LUFS against the source clip's −23.6, with Speaker Boost already on. That is headroom, not a defect, but the offset is not guaranteed constant across clips, so normalise rather than applying a fixed gain. Target −19 LUFS per clip, then master the assembled part to −14 LUFS integrated for YouTube.

**1b. Kling's own loudness is handled too (2026-09-28, Salah).** Kling sometimes voices a line louder than it needs to be —
a whole take hot, or one sentence pushed. Voice change keeps the take's dynamics, so the edit handles both:
- **Whole-take level** — the per-clip normalisation above brings every clip to −19 LUFS whatever level Kling made it at.
- **A loud moment inside one take** — `LRA=7` narrows the range, and the dialogue bus then gets a gentle compressor
  (`acompressor=threshold=-24dB:ratio=2.5:attack=15:release=250`) and the −1.5 dBTP limiter, so a pushed sentence sits
  with the rest instead of jumping out. If a moment still reads as shouted, lower that span by hand (clip gain), never
  the whole clip.
- **Kling's native audio where it is kept** — b-roll ambience and effects are normalised to their own lower target
  (about −32 LUFS, under the dialogue), not to the dialogue target.
The Mode 6 opening check (`batch_check.py`) lists QUIET clips; it also lists any clip whose short-term loudness jumps
more than 6 LU above its own average, so those spans are known before the mix.

**2. Strip the MP3 head padding — do NOT slip clips on the timeline.** ElevenLabs' MP3 export is longer than its source by **exactly 1152 samples: one MP3 granule, 26.1 ms**, written as head padding without gapless flagging, so decoders play it as leading silence. It looks like a lip-sync error and is not one — with those samples removed, the speech is **sample-aligned with the source at exactly 0 ms**, correlation unchanged. Control test: round-tripping the source through identical MP3 settings in ffmpeg shifts by 0 ms, so this is specific to how ElevenLabs writes the file, and it is deterministic on every clip regardless of length or content.

   📖 `skill_elevenlabs.md` §1 explains why this is permanent: lossless output begins at the Pro
   tier ($99). **It also applies to generated effects** — a looping sound effect is MP3 only,
   because ElevenLabs offers WAV export for non-looping effects alone. So the room-tone bed
   carries the same padding as dialogue and takes the same trim.

   **On this project's tier there is no WAV option** — ElevenLabs Starter offers MP3 44.1 kHz 128 kbps only — so the padding arrives on every clip and **the trim is a standing step, not a conditional one.** It costs nothing: it rides in the same ffmpeg pass as (1). (If the account ever moves to a tier exposing WAV/PCM, take it: the padding disappears and so does one lossy generation before YouTube's encode.)

   ```bash
   ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,\
   loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
   ```

**3. The room-tone bed runs under the whole episode, not just the joins.** Speech-to-speech resynthesises the voice rather than passing the source through, so the studio room tone **does not survive the pass** — and "Remove Background Noise: off" preserves nothing, because there is nothing to preserve. Measured: the source floor sits at −79 dBFS with a 950 Hz centroid and 58% of its energy in 120–500 Hz, which is a structured room; the converted floor is −86 dBFS, flat across every band at 17–22%, centroid 3417 Hz, which is broadband dither.

   Both floors are below audibility, so there is no pumping at the cuts. The consequence is the opposite: **no clip in the episode has an acoustic floor at all**, and without a bed the whole part sounds vacuum-sealed. `ROOMTONE_studio.wav` therefore runs continuously beneath everything — dialogue, reactions, b-roll, held silences — at low level, never ducking.

   **The bed is generated, not extracted.** Nothing in a finished part carries the video model's native studio tone: dialogue is resynthesised, reactions and silent wides have no audio track at all, b-roll has its own ambience. The bed is not matching a room, it **is** the room. Target roughly **−60 dBFS RMS** — about 40 dB below dialogue normalised to −19 LUFS. The test: mute it, listen to a cut, unmute. It is right when the cut stops being audible **and the bed itself still isn't**. Prompt and build procedure in `Fixed_Assets/SERIES_FURNITURE.md`.

**B-roll gets its own normalisation.** Generated b-roll warms and darkens across a clip — measured over 8s, saturation 0.238 → 0.277 and shadow 31.4% → 38.1%. Normalise each b-roll clip **against its own first frame**, the same way chain luma is compensated.
