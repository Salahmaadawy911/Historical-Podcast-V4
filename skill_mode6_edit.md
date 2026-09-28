# SKILL: MODE 6 (ASSEMBLY, FINAL EDIT & BRANDING)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.

> 📂 **Inputs and output.**
> **Reads:** `P<n>_kit.md`, `CARD_PLACEMENTS.md`, `CLIPS.md`, the kept clips in `Shots/`, the voice-passed audio in
> `Voice/P<n>/done/`, the per-episode renders in `Episodes/<Guest>/`, and the fixed assets.
> **Writes:** the clean master and the titled master of the part, `Episodes/<Guest>/P<n>_EDIT_NOTES.md` for anything
> the next part must carry forward, and the publish files — `P<n>_TIMECODES.txt`, `P<n>_captions.srt`,
> `P<n>_PUBLISH.md` (see *Publishing*).
> **Save the output to that file before the mode ends.** Anything that lives only in chat history is lost to the
> next mode.

> 📚 **How this file is kept (cleanup 2026-09-28).** Current rules only, each once, with its reason. History and
> superseded versions: `DECISIONS_ARCHIVE.md`, `Fixed_Assets/LESSONS.md`, `_archive/skills_pre_cleanup_2026-09-28/`.

**Status: partly specified.** Assembly, the audio rules, the cutting grammar, the hook render, the cards, source
attribution and the publish sheet are settled; timeline mechanics and export settings are written against Part 1's
first real edit (decided 2026-09-23), not guessed before it.

## Scope and order

After every clip is generated and the voice pass is done, the edit chat runs, in order:
1. **The opening check** — `batch_check.py` over the whole part (below).
2. **Assembly** — the dialogue cut, built from the kit's `edit_placement`s by measurement (below). Salah signs off the
   cut.
3. **The edit** — hook render, branding, cards, score, subtitles, masters, publish sheet.

The kit decides every placement (Mode 4); the edit executes it. A placement the kit is missing is a Mode 4 gap — fix it
at source, never improvise around it.

---

## 🚫 Tested and ruled out — do not bring these back

- **Slipping converted clips a frame on the timeline** — the apparent 26 ms lag is MP3 head padding (1152 samples),
  not a timing error; strip it (Audio rule 2). With it removed the speech is sample-aligned at 0 ms.
- **Pre-lifting chain frames, or hand-tuning a join** — joins are levelled from `JOIN_GRADES.md`, one filter per clip.
- **Fading a cut-off voice** in an interruption — a fade is a polite ending.
- **A credit roll** — a one-person channel rolling credits performs a scale it does not have; the end card carries the
  disclosure and sources instead.
- **Text on the outro transformation**, or cutting straight from it to text — the transformation is the ending.
- **A whoosh on any plate, or a bell on the subscribe card** — both read as a different kind of channel; the plates get
  one paper settle on the entrance only.
- **`MUSIC_Sting_Transition` and `MUSIC_Bed_Disclaimer`** — cancelled; the theme's own clock strikes do both jobs.
- **Compositing the mark onto wide clips** — there are no wide clips any more; the mark is in the outro still before
  its charcoal pass.
- **Extracting room tone from clips, or crossfading several takes into a bed** — the bed is one generated, seamless
  looping take (`ROOMTONE_studio.wav`); nothing in a finished part carries Kling's studio tone to match.
- **A two-up of two faces only reacting; a held `BEAT` of 2 s** (T6b, L10, L11).
- **Per-take checks during generation** — replaced by the one opening check below (L32).

---

## 1. The opening check — one pass over the whole part (L32)

```bash
python3 Fixed_Assets/tools/batch_check.py Episodes/<Guest>      # one line per clip in Shots/
```
It becomes the edit's to-do list. Claude looks at frames only where a flag says to.
- **PAUSE > 2 s / LEAD > 1.5 s** — trim; hide the trim with a punch, a card or a reaction (L13).
- **TIGHT** — listen to the last word; clipped → retake one second longer (L21, L24).
- **QUIET** — level in the mix (L22); **LOUD-SPAN** — a span > 6 LU above the take's own loudness; known before the mix.
- **SMALL-DRIFT (4–8 px)** — Resolve's stabiliser (camera lock mode) on that clip only; still visible → retake (L31).
- **CAMERA-MOVED / CORNER** — retake from the round sheet (v3 prompt, L51) before the cut is locked (`cam_check.py`, L19).
- **NO-AUDIO** on a talking row — retake.

## 2. The voice pass — folders

Before the voice pass: `python3 Fixed_Assets/tools/voice_folders.py Episodes/<Guest> --part <n>`. It copies every
talking clip (audio-only ones included) from `Shots/` into `Voice/P<n>/1_host/` and `Voice/P<n>/2_guest/`, so each
folder goes through ElevenLabs voice change with one voice (`eleven_multilingual_sts_v2`, settings in
`Fixed_Assets/VOICES.md`). Converted files are saved to `Voice/P<n>/done/` under the same clip name (**MP3**, e.g.
`P1_006.mp3`). The edit lays each MP3 under its clip's picture from `Shots/` (after the head trim, Audio rule 2);
everything else comes straight from `Shots/`. `Shots/` is never changed. Re-run after any retake — it copies only new or
retaken clips and says how many are left.

## 3. Assembly — the dialogue cut

**The kit carries intent; assembly resolves it by measurement.** A row says *"her reaction covers the tail of his
question, cut back on the first word of the answer"* — never a timecode, because nobody knows where his speech ends
until the clip exists. Filenames are the link: a clip is `Shots/<shot_id>.mp4`; a renamed file is unplaceable.
Assemble act by act so problems surface early.

1. **Probe every clip:** duration, speech in/out points (`silencedetect` at −38 dB), noise floor. Never estimate.
2. **Cut in silence, never on a word.** Take a cut a beat *before* a covered line begins, so the reaction is established
   before the words arrive.
3. **Close the gaps:** ~0.3 s between sentences of one utterance, more at a genuine turn; trim silent lead-ins (a clip
   can open with seconds of silence — `P1_046` 3.2 s) and dead air over ~1.2 s that the kit did not mark as a `BEAT`.
4. **Level every chained join** with `JOIN_GRADES.md` — one `colorchannelmixer` filter per chained clip, on the whole
   clip, written by `chain_frames.py`. If a join still shows after it, the fault is content (pose, sharpness, a local
   colour change), not grade — flag it for regeneration.
5. **Normalise each b-roll clip against its own first frame** — generated b-roll warms and darkens across a clip
   (saturation 0.238 → 0.277, shadow 31.4% → 38.1% over 8 s).
6. **Lay the room-tone bed** under everything (Audio rule 3).
7. **Deliver one assembled part**, not a folder of clips; then watch, report, adjust — measurement cannot tell whether
   a pause lands.

## 4. Cutting the conversation — the default grammar

- **Emotion first, then story, then rhythm** (Murch). Cut to whoever is worth watching.
- **Speaker changes are J-cuts by default:** the next speaker's audio leads the picture by ~4–8 frames, varied —
  sometimes an L-cut holding on the listener through the first words. **Never ping-pong** (a cut on every first
  syllable reads as automated).
- **Cut at a sentence end or a breath, never mid-word.** A listener's natural blink is a good cut point.
- **Trim dead air** and hide each trim with a `PUNCH` (≤ 15%, held to the end of its clip, no animation, never two in a
  row), a reaction or a card. Then an **ears-only pass** — play the part without picture — to catch any seam the picture
  was hiding.
- **The guest carries the picture** (Mode 4 §8b): a host question starts on him and cuts to her listening as it turns
  to her; short pushes run wholly under her face; his reactions during her lines are two-ups. If the edit trades a shot,
  trade it in her favour — the kit's `screen:` lines add up to ≥ 65% guest.
- **`TAIL` lines** (a last word on a stop cluster) should not exist (Mode 3 rule 5, L12). If an older clip has one, cut away on
  the end of the word, or use Kling's lip-sync tool if the strain shows.
- **Chapters** from the kit's chapter titles: first at `0:00`, at least three, each ≥ 10 s.
- **Cut the goodbye:** nothing after the tease but `BRAND_bumper_out` and the end card.

### The host's turn to the guest (L38, L40)
Cut from the turn clip to the guest cut-away (e.g. `P1_003a`) **as the turn lands** — on the last word or just after —
and never hold on where the turn ends: its end eyeline is not the seed's. About 1.5 s of her face, then the host's next
clip from the built seed.
**A turn that snaps in silence — retime, don't regenerate:** slow just the turn to ~50–60% with optical flow (DaVinci
Speed Warp, else Optical Flow), cut the still hold after it so the gap before the next words is ≤ ~1.5 s, fill the gap
with the clip's own room tone. Check ears, hands and mic arm for warping; if it warps, remake from the round sheet.

### Two-up — both faces at once
Crop each single to its half at native resolution (host in the left 960 px, guest in the right; the crop per pose is
in Mode 4 §8b) — never scale up. 10 px paper-tone gutter (`#CDC1AC`) with a 3 px walnut rule (`#9C6B3F`) from 16% to 84%
of frame height. Hard cut in and out. Audio is the timeline's. Apply each half's join grade if it is chained. **No text
over it.** 🔴 **Someone is always talking in a two-up;** a silence goes on one face, and a `BEAT` is held ~1 s after
the last word. Up to 7 per part, 3–6 s each, never two in a row. If a two-up would run into a card or plate, end it early.
Reference: `Fixed_Assets/Branding/reference/splitscreen_reference.png`.

### Split lines — hiding the seam
Audio: A's line, its pause trimmed to a breath, then B's — play the seam ears-only; it must sound like one person
continuing. **Level the pair together (one gain), then trim any remaining step at the seam to ≤ 3 dB** (L14).
Picture as `edit_placement` names it: (a) cut away across the seam, returning on B; (b) a `PUNCH` exactly on the seam;
(c) a plain cut on the pause. Apply B's join grade. If the seam still shows in pitch or energy, move it under a cutaway.

### Overlaps and interruptions — cutting what Mode 4 placed
- **`audio only, under X`** — lay the interjection's voice-passed audio under X at the named moment, ~3 dB below the
  on-screen speaker. Picture discarded.
- **`CUT-IN`** — A (talking), B (the chained silent stop), C (the interrupter). Never fade a cut-off voice.
  - **Picture:** A up to the cut word → B from the same frame → C once B has shown the stop, usually 0.6–1.2 s in.
  - **Sound:** A's audio ends hard just after the cut word; C's starts **~0.3 s before** that, so the voices collide,
    and runs on under B. Audio early, picture late: that reads as an interruption, not a turn.
  - `seen`: the wind-up W over A a beat or two before the cut. `yield`: hold B through the whole overlap.
    `hold`: no B — stay on A; the off-camera *"But—"* sits under the speaker ~3 dB down, and they carry on.
  - The reply's silent lead-in never shows: her audio starts ~0.3 s before the cut, her picture after the stop.

## 5. The opening with its hook — rendered per part

**Re-pick the hook first.** The kit's hook is Mode 3's first option. Watch the assembled part and choose the **most
shocking guest moment on screen**, where line, face and delivery work together — any guest sentence in the part, a
clean single with the face turned to the camera side and a closed mouth after the line. Run it past Salah, then record
it in the kit's opening row and `OUTLINE.md`'s `HOOK:` line. If the hook line is also a pull-quote, drop that
pull-quote.

```bash
python3 Fixed_Assets/Branding/intro_source/hook_build.py Episodes/<Guest>/Shots/<hook shot>.mp4 <in s> \
        Episodes/<Guest>/BRAND_opening_p<N>.mp4 --face <CX,CY,H from CAST.md "Hook framing">
```
Re-measure the in point on the final take (the line starts ~0.4 s after it). The script reports where the line ends
and whether it had to freeze. Use the **voice-passed** hook audio. Use `BRAND_opening_p<N>.mp4` at 0:00 in place of
`BRAND_opening.mp4` — never edit the fixed file.

## 6. Series furniture in the edit — built once, placed here

Full specs and the placement map: `Fixed_Assets/SERIES_FURNITURE.md`.

- **`BRAND_opening`** (via its per-part hook render) at 0:00 — the disclosure card (0–4 s, on paper), the hook (4–8 s),
  the intro (8–19.17 s), one unbroken piece of music. The disclosure is not a separate asset any more.
- **`BRAND_composite_p<n>`** — eyewitness episodes only, end of the cold open, immediately before the guest first
  appears in the studio.
- **`BRAND_actbreak_vessel` / `_stone`** — at each act break, alternated; 5.000 s finished files with the bed laid in.
  Drop one in and cut out on its last frame.
- **`BRAND_subscribe`** — ~4 s lower third with alpha (`.mov` / `.webm`), once per part, **after** a strong beat of
  Act B or C, never over one. No bell, no sound.
- **`BRAND_bumper_out`** — the kit's outro clip (`Shots/<id>.mp4`): the 5 s transformation **clean**, the last frame
  held ~3 s **clean**, then a cross-dissolve to the end card. `MUSIC_Outro_Bed` is already running (cut in at source
  10.0 s so its peak lands on the transformation) and decays; no cue on the dissolve.
- **`BRAND_endcard_p<n>`** — the per-part render (disclosure, primary sources from the audit, next part, personal line,
  support lines, mark), 20 s, right third clear for YouTube end screens.
- **Watermark:** `BRAND_symbol` light, **bottom-left**, 40% opacity, on the studio singles (bottom-right collides with
  the microphone stand). `brand_symbol_720.png` is the INK version — export a light PNG from `brand_symbol_light.svg`.

## 7. On-screen text — placed by the kit, built by `build_episode_cards.py`

Positions and design are fixed in `STUDIO_ASSETS.md`; the kit's §12 and `CARD_PLACEMENTS.md` say which file goes over
which shot.
- **`BRAND_lowerthird`** — twice per part, host and guest, on first proper appearance; never over the hook.
- **`BRAND_pullquote`** — three or four per part, **after** the line, over the guest's own held face (her listening
  clip); never over the line itself, never over a two-up.
- **`BRAND_context_NN`** — enters **on the word** named in `CARD_PLACEMENTS.md` (its first syllable), holds 5.5 s,
  opposite the speaker, upper band. Never over a reaction of the other person. Where a `[D]` source credit would land at
  the same moment, drop the credit — the card's source line carries it.
- **Plates carry `SFX_plate` on the entrance only** — one soft paper settle, mixed far under dialogue (quieter on the
  frequent context cards). Exits are silent: a sound on the way out draws attention to something leaving.
- **One text at a time.** Subtitles stay at the bottom.

### Source attribution on screen
When the guest states a checkable fact on a **`[D]` line**, put its source on screen for two or three seconds —
*Plutarch, Life of Antony*. `[I]` lines are not attributed (a citation under an inference reads as a claim the source
does not make); `[V]` lines carry no fact. It is the most legible evidence that the episode is researched, not
generated.

### The description's source list is audited from the tags
Built from the `[D]` and `[I]` lines' named sources (`card_data_p<n>.json`, curated from `sources_audit.py`): **nothing
cited that is not used, nothing claimed that is not cited.** Where the episode corrects a popular story, the
description says so — the *Heard vs the record* items.

## 8. Audio — the rules, all measured

**1. Loudness-normalise every converted clip to −19 LUFS, then master the part to −14 LUFS integrated.** ElevenLabs
speech-to-speech returns audio ~10 LUFS below source (−34.0 against −23.6, Speaker Boost on), and the offset is not
constant — normalise, never apply a fixed gain.
- **Kling's own loudness:** the per-clip normalisation evens out a take Kling voiced hot. A loud moment *inside* one take
  is handled by `LRA=7`, then a gentle dialogue-bus compressor
  (`acompressor=threshold=-24dB:ratio=2.5:attack=15:release=250`) and the −1.5 dBTP limiter; if a span still reads as
  shouted, lower that span by clip gain, never the whole clip.
- **Kling's native audio where it is kept** (b-roll ambience) goes to its own lower target, about −32 LUFS.

**2. Strip the MP3 head padding — 1152 samples, every converted file.** ElevenLabs' MP3 export is exactly one MP3
granule (26.1 ms) longer than its source, written as head padding without gapless flagging. Deterministic on every clip.
The Starter tier is MP3-only, so the trim is a standing step (it disappears only on a lossless tier). It also applies to
looping sound effects — the room-tone bed included. One pass does both:

```bash
ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,\
loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
```

**3. `ROOMTONE_studio.wav` runs under the whole part, never ducking.** Speech-to-speech resynthesises the voice, so
the studio tone does not survive (source floor −79 dBFS with a structured 120–500 Hz room; converted −86 dBFS flat
dither). Reactions have no audio track; b-roll has its own ambience. Without the bed the part sounds vacuum-sealed.
Level **about −60 dBFS RMS** (~40 dB below dialogue at −19 LUFS). The test: mute it and listen to a cut, unmute — right
when the cut stops being audible **and the bed itself still isn't**. It runs under held silences too.

**4. Score is dry by default** — music at the structural points (opening, act breaks, close) and a drone only where the
content earns it (`SERIES_FURNITURE.md`). If a dry stretch feels flat, that is a writing note, not a scoring one.

## 9. Two masters

Finish every part twice: a **clean master** (picture, dialogue, room tone, music — no text of any kind) and the **titled
master** (subtitles, lower thirds, pull-quotes, context cards, source credits) that is published. Mode 5 cuts reels from
the clean master; cutting from the titled one is a mistake invisible until the reel is vertical.

## 10. Publishing — the copy-paste sheet

The last step of every part, after the masters are exported:
1. **Write `P<n>_TIMECODES.txt`** from the finished timeline — one line per chapter shot in the kit's §11, giving where it
   starts **in the final master** (opening included), plus the master's length. Round down to the second. Chapter 1 is
   `0:00` and needs no line.
   ```
   P1_008 1:12
   P1_033 3:40
   end 11:48
   ```
2. **Export `P<n>_captions.srt`** from the spoken text (true spellings). Uploading it beats auto-captions, which get the
   names wrong.
3. **Run** `python3 Fixed_Assets/tools/publish_sheet.py Episodes/<Guest> --part <n>` → `P<n>_PUBLISH.md`, exit 0 only
   when ready (three titles with the series index and verbatim quotes, the guest named in the first 150 characters,
   three hashtags, tags ≤ 500 characters, description ≤ 5000 and free of `<` `>`, ≥ 3 chapters from `0:00` each ≥ 10 s,
   a source list, the AI-disclosure statement, the thumbnail file, no `TODO` in `publish_defaults.json`).
4. **Upload by following the sheet top to bottom** (Studio's order), with **Altered or synthetic content → Yes**.
   The sheet only checks the thumbnail exists — make sure `THUMB_<guest>_p<n>.png` is this part's.

The sheet is generated, never edited: a wrong word is fixed in the kit (§9, §11), `card_data`, or the timecodes, and
the tool re-run.

## 11. `P<n>_EDIT_NOTES.md`

Anything Part 2's Mode 4 must know: takes kept with known flaws, what the edit had to fix (and whether a skill or gate
now prevents it — LESSONS protocol), the final hook, measured loudness steps, joins that needed more than the grade.
