# Cleopatra — Part 1 · Production Kit
*Mode 4 output, B5 rerun, 2026-09-23. Built from `Episodes/Cleopatra/OUTLINE.md` (words approved in `SCRIPT_READ.md`, 2026-09-23) and `CAST.md`, by `_kit_source/build_p1_kit.py`. **No spoken word differs from the outline.** Ids are contiguous (a fresh kit); from here on, an inserted row takes the previous id plus a letter.*

`part` 1 of 2 · guest `@guest_cleopatra` (Reconstructable tier, named figure — no composite card) · host fixed.

**Anchor images** (all checked on disk 2026-09-23; seed frames viewed, montage in `_kit_source/grounding_*.jpg`):
- Host seed frames — `Start_Frames/Host/frame_host.png`, `_b`, `_c`, `_d`, `_e`, `_f`; direct address `Start_Frames/Host/frame_host_direct_b.png`.
- Guest seed frames — `Start_Frames/Cleopatra/frame_cleopatra.png`, `_b`, `_c`, `_d`, `_e`.
- Close — `Start_Frames/Cleopatra/frame_wide_cleopatra_marked.png` (start frame of `BRAND_bumper_out`).
- Fixed furniture — `Fixed_Assets/Branding/BRAND_opening.mp4`, `BRAND_actbreak_vessel`, `BRAND_actbreak_stone`.
- Thumbnail portrait — `Episodes/Cleopatra/thumb_portrait_cleopatra.png` (Mode 2).

**Voices** — Kling `Voice:` block pasted byte-identical in every talking clip (accent lives here); ElevenLabs speech-to-speech supplies timbre only, model `eleven_multilingual_sts_v2`: host `FgXTns6rcAlMbBOnz3nB`, Cleopatra `xMytukqVLj8LlL1L1sOo` (`Fixed_Assets/VOICES.md`).

**Locked blocks** — `LOCK`, both `Voice:` lines and the audio paragraph appear only inside the prompts below, identical in every one (the Voice gate counts exactly two distinct lines). Guest prompt label `The woman`, she/her (`CAST.md` performance profile). Contractions: host yes, guest none.

## 1 · Settings (identical for every clip)

| | |
|---|---|
| Platform | **kling.ai**, 1080p, image-to-video |
| Talking clips | Kling 3.0 **Turbo**, audio on — 10 cr/s |
| Audio-only talking clips (picture never used) | Kling 3.0 **Turbo at 720p**, audio on — **8 cr/s** · marked **720p** in the row header and grouped separately in the round sheet |
| Silent reactions | Kling 3.0 **Standard, audio OFF** — 8 cr/s |
| B-roll | Kling image-generation still (kling.ai, as tested), then Kling 3.0 **Turbo**, audio on — 10 cr/s |
| Camera preset | **stationary preset ON** on every dialogue and reaction clip, plus the full `LOCK` paragraph. **No** preset on b-roll — b-roll moves |
| Every other Kling preset | forbidden on dialogue (they are prompt text describing what the seed frame already fixes) |
| Prompt enhancer | not available on Turbo; gesture paragraphs stand as written |
| End-frame slot | Turbo has none — joins are chains |
| Voice | ElevenLabs speech-to-speech on every talking clip, paid tier |
| Paste | **from this file or the round sheet, never from chat.** Every paragraph after the first starts with one space (Kling strips paragraph breaks) |

Record any exposed creativity / cfg value the first time it is seen, and keep it for the whole part.

## 2 · Totals

| Category | Clips | Seconds | Rate | Credits |
|---|---|---|---|---|
| Talking (`INTERVIEW` / `INTERJECTION` / `NARRATION`) | 93 | 679 (11m 19s) | 10 (8 at 720p for the audio-only clips) | **6,676** |
| Reactions, silent | 30 | 138 | 8 | 1,104 |
| B-roll, generated | 6 | 41 | 10 | 410 |
| B-roll stills | 6 | — | — | 18 |
| `BRAND_bumper_out` | 1 | 5 + held | 8 | 43 |
| **Total** | **130 clips + 6 stills** | **863** | | **~8,251** |
| `BRAND_opening`, `BRAND_actbreak` ×2 | fixed | 19.17 + 10 | — | 0 |

13 talking clips (48 s) are off-mic — generated, heard, picture discarded. Reactions and b-roll lie over the spine; they add generations, not runtime (except the `BEAT`s and the act breaks). Expected finished length ≈ **10–10½ minutes** with the opening, breaks and close — the outline's read timed the words at ≈ 9:50 (`SCRIPT_READ.md`); the duration model's lead-ins and tails are trimmed in the edit.

**Budget the reruns:** about one retry in six on talking clips (~1,110 cr), so plan on **~9,361 credits** for Part 1 — and record the actual figure (NEXT_STEPS A5 is waiting for it).

**Cold-open timing:** first guest word at **~4 s** (the hook), guest on screen in the studio at **~43 s** — under the 40 s ceiling (Mode 4 §0).

## 2b · Screen share — the guest carries the picture

Series rule since 2026-09-24 (Mode 4 §8b): his questions play on her listening, his reactions during her lines are two-ups, at most two full-frame host reactions. Summed from every row's `screen:` line; `screen_share.py` is the gate.

| | on screen | share of studio picture |
|---|---|---|
| **Guest, full frame** | 5:19 | 69% |
| **Two-up** (6; counts as hers) | 0:28 | 6% |
| **Host, full frame** | 1:55 | 25% |
| B-roll (not in the share) | 0:32 | — |

**Guest share: 75%** (target ≥ 65%). Speech-model seconds — the cut trims lead-ins and pauses, so the edit lands a little shorter but in the same proportion.

## 3 · Start frames used

Host: `frame_host`, `frame_host_b`, `frame_host_c`, `frame_host_d`, `frame_host_direct_b`, `frame_host_e`, `frame_host_f`. Guest: `frame_cleopatra`, `frame_cleopatra_b`, `frame_cleopatra_c`, `frame_cleopatra_e`, `frame_cleopatra_i`. Chosen per beat from the two pose registers (`STUDIO_ASSETS.md`, `CAST.md`); no character repeats a variant within three of their on-screen appearances (checked by the builder). Chained clips inherit the pose of the clip they continue. Every gesture sentence describes the frame as it actually is — a prompt that contradicts its start frame asks the model to move the body into the described pose.

## 4 · Generation order

0. **The test batch (§4b)** — `P1_008`, `P1_009`, `P1_019`, `P1_020`, `P1_044`, `P1_045`, `P1_046`, `P1_083`, `P1_084`, `P1_086`, `P1_087`, `P1_088`. First, before any other spend, because each one tests a technique this kit relies on. They are normal kit rows: a clip that passes is kept.
1. **Pass 1** — every row with a seed frame, chain sources included: `python3 Fixed_Assets/tools/round_sheet.py Episodes/Cleopatra 1 --part 1` → `ROUND1_prompts.md`. Clips already in `shots/` (the test batch) are skipped automatically.
   **Duration calibration:** Cleopatra's rate (4.3 syl/s) is measured and on file (`CAST.md`) and the host's carries over, so no separate calibration round — but measure the first three talking clips of Pass 1 (onset, rate, pause per break) and stop if either voice is more than ~10% off.
2. **Chain frames** — `python3 Fixed_Assets/tools/chain_frames.py Episodes/Cleopatra 1`. Time the cut word in `P1_044` first and write it into `P1_045`'s row (`chain from `P1_044` at 6.42s` form).
3. **Pass 2** — the chained rows: `round_sheet.py Episodes/Cleopatra 2 --part 1`, each started from its source clip's last frame **with Kling's own last-frame feature** (the extracted `_start.png` is the fallback). Run `chain_frames.py` again to measure every join → `shots/_measure/JOIN_GRADES.md`.
4. **Voice pass** (ElevenLabs, 93 talking clips; never reactions or b-roll), then **assembly** (§6), then Mode 6.
5. **`BRAND_bumper_out` last** — the charcoal pass on the marked wide, then the 5 s transformation.

### Chain table

| chained shot | starts from the last frame of | source type | start frame file |
|---|---|---|---|
| `P1_003` | `P1_002` | NARRATION | `shots/start_frames/P1_003_start.png` |
| `P1_010` | `P1_008` | INTERVIEW | `shots/start_frames/P1_010_start.png` |
| `P1_012` | `P1_010` | REACTION | `shots/start_frames/P1_012_start.png` |
| `P1_024` | `P1_022` | INTERVIEW | `shots/start_frames/P1_024_start.png` |
| `P1_026` | `P1_024` | REACTION | `shots/start_frames/P1_026_start.png` |
| `P1_035` | `P1_033` | INTERVIEW | `shots/start_frames/P1_035_start.png` |
| `P1_038` | `P1_037` | INTERJECTION | `shots/start_frames/P1_038_start.png` |
| `P1_045` | `P1_044` **at the cut word** *"Caesar"* — **2.95 s** | INTERVIEW | `shots/start_frames/P1_045_start.png` |
| `P1_047` | `P1_046` | INTERVIEW | `shots/start_frames/P1_047_start.png` |
| `P1_049` | `P1_047` | REACTION | `shots/start_frames/P1_049_start.png` |
| `P1_053` | `P1_052` | INTERVIEW | `shots/start_frames/P1_053_start.png` |
| `P1_055` | `P1_053` | REACTION | `shots/start_frames/P1_055_start.png` |
| `P1_060` | `P1_058` | INTERJECTION | `shots/start_frames/P1_060_start.png` |
| `P1_062` | `P1_060` | REACTION | `shots/start_frames/P1_062_start.png` |
| `P1_072` | `P1_071` | INTERVIEW | `shots/start_frames/P1_072_start.png` |
| `P1_080` | `P1_078` | INTERVIEW | `shots/start_frames/P1_080_start.png` |
| `P1_088` | `P1_087` | INTERVIEW | `shots/start_frames/P1_088_start.png` |
| `P1_091` | `P1_090` | INTERVIEW | `shots/start_frames/P1_091_start.png` |
| `P1_093` | `P1_091` | REACTION | `shots/start_frames/P1_093_start.png` |
| `P1_099` | `P1_098` | INTERVIEW | `shots/start_frames/P1_099_start.png` |
| `P1_101` | `P1_099` | REACTION | `shots/start_frames/P1_101_start.png` |
| `P1_109` | `P1_108` | INTERVIEW | `shots/start_frames/P1_109_start.png` |
| `P1_111` | `P1_109` | REACTION | `shots/start_frames/P1_111_start.png` |
| `P1_115` | `P1_113` | INTERJECTION | `shots/start_frames/P1_115_start.png` |
| `P1_117` | `P1_115` | REACTION | `shots/start_frames/P1_117_start.png` |
| `P1_121` | `P1_120` | INTERVIEW | `shots/start_frames/P1_121_start.png` |
| `P1_129` | `P1_128` | INTERVIEW | `shots/start_frames/P1_129_start.png` |

**Pass 1** — every other row, including the chain sources `P1_002`, `P1_008`, `P1_010`, `P1_022`, `P1_024`, `P1_033`, `P1_037`, `P1_044`, `P1_046`, `P1_047`, `P1_052`, `P1_053`, `P1_058`, `P1_060`, `P1_071`, `P1_078`, `P1_087`, `P1_090`, `P1_091`, `P1_098`, `P1_099`, `P1_108`, `P1_109`, `P1_113`, `P1_115`, `P1_120`, `P1_128`.
**Pass 2** — `P1_003`, `P1_010`, `P1_012`, `P1_024`, `P1_026`, `P1_035`, `P1_038`, `P1_045`, `P1_047`, `P1_049`, `P1_053`, `P1_055`, `P1_060`, `P1_062`, `P1_072`, `P1_080`, `P1_088`, `P1_091`, `P1_093`, `P1_099`, `P1_101`, `P1_109`, `P1_111`, `P1_115`, `P1_117`, `P1_121`, `P1_129`, each started from its source clip's last frame **with Kling's own last-frame feature** (colour is matched in the edit, `JOIN_GRADES.md`); `chain_frames.py`'s extracted frame is only the fallback.
No chain is deeper than three links (the longest is the Arsinoe `SPLIT`: two-up reaction → A → B). An `OFFMIC` row never appears in picture, so it neither breaks nor needs a chain.

## 4b · The test batch (Mode 4 §0c) — Part 1 of a new run, before Pass 1

Picked from this kit by the criteria, not from old shot ids. **~724 cr**, all of it normal kit rows.

| # | question | shot(s) | why it qualifies | how to judge |
|---|---|---|---|---|
| T1 | Does a `Pronunciation:` paragraph make Kling say a rare name right? | `P1_013` | — | **✅ settled 2026-09-24:** the paragraph was read aloud (*"Medes"* twice); respelling inside the quote (*"Meeds"*) was right. Rule in Mode 4 §3 3b. `P1_013` is regenerated at 9 s in Pass 1 (the 8 s take ran to its last frame) |
| T2 | Does a **beat map** give each sentence its own temperature, with no extra pauses and no note read aloud? | `P1_019` → `P1_020` | — | **✅ settled 2026-09-24:** each sentence got its own delivery, nothing read aloud (Salah, as a viewer). It took 1.6 s and 1.0 s between segments and ran to the last frame → duration model v3 (1.0 s per break). Beat maps are now the default wherever the outline gives one delivery per sentence. `P1_020` is regenerated at its v3 length |
| T3 | Does a `SPLIT` read as one continuous line? And does lip-sync drift after ~5 s in a whole take? | `P1_087` + `P1_088` | the outline's `SPLIT`, a mood turn at a sentence, a `PUNCH` to hide the seam | **✅ settled 2026-09-24:** cut together in Resolve it reads as one line (Salah); pitch 193 Hz both sides, flat join, only a 6–7 dB loudness step (split level rule). No lip-sync drift in the long beat-map takes, so the control is dropped. Both clips kept |
| T4 | Does a trailing `…` play as a thought let go? | — | **no line in Part 1 uses `…`** | stays open |
| T5 | Does a `CUT-IN` stop read as a real interruption, and does its start frame stay closed-mouthed? | `P1_044` → `P1_045` → `P1_046` | the first `cut` interruption | the stop's mouth closes in the first frames and stays closed; her entry lands on the cut **✅ T5 settled 2026-09-25:** reads as a real interruption (Salah); mouth closes in ~0.4 s; `Shots/_tests/_twoup/CUTIN_T5_test.mp4`. Her 3.2 s silent lead-in is trimmed (audio in 0.3 s before the cut) |
| T6 | Does a two-up hold up in motion — crop, eyelines, the listener clip's length? **Both kinds** (Screen share, 2026-09-24): a host reaction beside her talking, and a shared silence | `P1_008` + `P1_009`; `P1_083` → `P1_084` → `P1_085` + `P1_086` | two-up #1 (his reaction beside her line) and the old #5 (the silence after *"In a sanctuary"*) | build each from the singles (native crop, never scaled); eyelines meet across the divider; his half never looks like a cutaway. **Fail → host reactions fall back to J-cuts, with at most two full frame.** **✅ T6a settled 2026-09-24:** two-up #1 passes (`Shots/_tests/_twoup/TWOUP_01_test.mp4`); `P1_009` regenerated after the nod rule. **❌ T6b failed 2026-09-24:** a two-up with both faces only reacting reads as empty (Salah). **Rule: a two-up always has one person talking; a silence goes on one face, hers.** The old #5 is gone: his *"In a sanctuary"* plays over her face (`P1_086`), then ~1 s of silence. `P1_085` is retired (number kept empty so later clips keep their names) |

**Order (Salah, 2026-09-24): one test at a time — T1 ✅, T2 ✅, then T3, T6a, T6b, T5.** Seed-frame clips first (`P1_008`, `P1_009`, `P1_019`, `P1_044`, `P1_046`, `P1_083`, `P1_086`), then the chained ones in dependency order (`P1_020`, `P1_084`, `P1_087`; then `P1_088`; `P1_045` once the cut word is timed).
**Results fold back into the skills:** a pass → mark it `settled <date>` in Mode 4 §0c and remove the hedge from the section it tested; a fail → remove the technique from Modes 3 and 4 and record it in `DECISIONS_ARCHIVE.md`.

**T3 optional control** (~13 s, chained from `P1_086`, save as `shots/_tests/T3_whole.mp4` — not a kit row, never cut into the part):

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman speaks quietly and seriously, steady and unhurried; the last sentence is low and firm. The woman (quietly, in a serious tone): "In my family, the danger to a queen sat at her own table. Rome had already used her against me once. I would not leave it a second chance." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

### Pronunciation

Every rare name in a Part 1 spoken line (`lines_check.py` checks coverage). Stressed syllable in capitals. **Settled by T1 (2026-09-24): no pronunciation note in any prompt — it is read aloud.** Words likely to go wrong are **respelled inside the quote** (*Medes* → *Meeds*, *Ptolemies* → *Tolemies*); subtitles keep the true spelling. Every other name is checked by ear on its take and respelled on a retake if wrong.

| Word | Say it | note |
|---|---|---|
| Ptolemaic | tol-uh-MAY-ik | |
| Ptolemies | TOL-uh-meez | the P is silent — respelled *Tolemies* in the prompt |
| Ptolemy | TOL-uh-mee | the P is silent |
| Parthia | PAR-thee-uh | |
| Parthians | PAR-thee-unz | |
| Octavian | ok-TAY-vee-un | |
| Octavia | ok-TAY-vee-uh | |
| Actium | AK-tee-um | |
| Arsinoe | ar-SIN-oh-ee | |
| Pelusium | peh-LOO-see-um | |
| Seleucus | seh-LOO-kus | |
| Charmion | KAR-mee-on | hard K |
| Dolabella | dol-uh-BEL-uh | |
| Tarsus | TAR-sus | |
| Medes | MEEDZ | one syllable — respelled *Meeds* in the prompt |
| Meeds | MEEDZ | the prompt respelling of *Medes* |
| Tolemies | TOL-uh-meez | the prompt respelling of *Ptolemies* |
| Aphrodite | af-roh-DYE-tee | |
| Artemis | AR-teh-miss | |
| Cassius | KASS-ee-us | |
| Plutarch | PLOO-tark | |
| Horace | HOR-iss | |
| Dio | DEE-oh | Cassius Dio |
| Seductress | seh-DUCK-tress | |
| Petra | PET-ruh | |

## 5 · Reading a row

Each row header carries id, type, speaker, duration, model, rate and credits. `start_frame` is the still to upload, or `chain from` the clip whose last frame starts this one. Everything inside a code block is pasted whole. **Subtitle** is the burn-in text; **provenance** is the line's source tag; **edit_placement** says what the clip is for — intent, never a timecode (assembly resolves times from the measured audio).

| Tag | Meaning | Rows |
|---|---|---|
| `[D]` Documented | attested; the source is named on the line | 46 |
| `[I]` Inferred | consistent with the record; the basis is named | 19 |
| `[V]` Voice | connective tissue; **carries no factual claim** | 28 |

Every `[D]` source was read on 2026-09-23 in Mode 3; no open verification flag exists anywhere in this kit (the gate greps for the word, so it is not written here). A `[V]` line may not contain a factual assertion — host echoes that restate a documented fact carry the fact's tag.

## Shot list

### Opening

**P1_001** · BRAND_OPENING · **19.17s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_opening.mp4` — one built file, byte-identical in every episode (spec in `Fixed_Assets/SERIES_FURNITURE.md`): the disclosure card 0.00–4.00, **the hook slot 4.00–8.00**, the intro 8.00–19.17, one unbroken piece of music with a clock strike opening each beat.

**edit_placement:** opens the video at 0:00. The nominated line is **`P1_008`, the whole line: *"They came for my treasury. They wrote about my bed."*** — **a first option only** (Salah, 2026-09-23): Mode 6 re-picks the hook from the finished part as its most shocking guest moment, then renders it with `hook_build.py … --face 1365,180,240` (face emerging from the paper; framing from `CAST.md`). Her audio only, no host, no added music. If a take has no clean closed-mouth pause after the line, freeze on the last closed-mouth frame for the rest of the slot.
**Subtitle:** the card's wording is burned into the asset; the hook keeps its own subtitle.
**SFX:** nothing to add — music, strikes, `SFX_sand` and `SFX_plate` are inside the file.

**P1_002** · NARRATION · HOST · **15s** · Kling 3.0 Turbo, audio on · 10 cr/s · **150 cr**
`start_frame` `frame_host_direct_b` · 31 syllables · needs 14.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, direct to camera, level — he lays out the charge without endorsing it. The two names land a little harder and stop short of scorn. The host (in a level, firm tone): "Rome once declared war on a woman — not on the Roman beside her. Then the winners wrote her story. Seductress. Monster." He stays leaning forward, forearms on his thighs and hands clasped, looking into the lens.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Rome once declared war on a woman — not on the Roman beside her. Then the winners wrote her story. Seductress. Monster.
**provenance:** `[D]` Documented — war declared on her: Plutarch, *Life of Antony* 60; Cassius Dio, *Roman History* 50.4. "Monster": Horace, *Odes* 1.37 (*fatale monstrum*). The hostile tradition is Augustan.
**edit_placement:** the host's only direct address. Hard cut in on the first strike after `BRAND_opening`. No lower third (frontal frame). `SPLIT` A — the whole line needs 15.8 s, past the 15 s cap, so it is split at the sentence where it turns quieter. Seam into `P1_003`: a plain cut on the pause (Mode 4 §2, fix c) — no cutaway exists this early and a `PUNCH` is never used on direct address; the chained pose and the join grade carry it.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 12.4 · 2UP 0.0 · BROLL 0.0

**P1_003** · NARRATION · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `chain from P1_002` · 19 syllables · needs 6.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, still to camera, quieter now — a plain statement, then an introduction rather than a flourish. The host (quietly): "Every word of it came from the side that won. She's sitting across from me." He stays leaning forward, hands clasped, and says the first sentence to the lens. Without a pause he begins "She's sitting across from me", and his head makes a small, slow turn toward the right side of the frame, just past his microphone, taking the whole sentence; his eyes come to rest level, at seated head height, on the woman in the armchair opposite him, and stay there. His hands and shoulders stay where they are.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Every word of it came from the side that won. She's sitting across from me.
**provenance:** `[D]` Documented — the surviving narrative sources are Roman and post-Actium: Plutarch, *Life of Antony*; Cassius Dio, *Roman History* 50; Horace, *Odes* 1.37.
**edit_placement:** `SPLIT` B. He turns to her on the last sentence; cut to `P1_003a` as the turn lands (on *"me"* or just after) — never hold on the end of the turn.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 5.7 · 2UP 0.0 · BROLL 0.0

**Turbo, no end frame, and the turn always ends on a cut to her** (Salah, 2026-09-27). Standard + end frame failed twice, and on Turbo the turn goes the right way but its end point is luck (it overshoots). So nothing chains from this clip: the edit cuts to `P1_003a` on her face as the turn lands, and `P1_004` comes back to him from the built seed `frame_host_b`, whose eyeline is right. The turn only has to head toward her.

**P1_003a** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `frame_cleopatra_b` · `end_frame` `frame_cleopatra_b` — **the same seed frame** (Standard's end-frame slot)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap. Her chin lifts a fraction; otherwise she is still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** the cut out of the host's turn: on *"me"* at the end of `P1_003`, about 1.5 s of her face, then `P1_004` on him from the seed. **Her first appearance in the studio — his introduction lands on her face, seen before she is heard.** This cut is what hides the difference between where the turn ended and `frame_host_b`.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**Not generated — cut from `P1_126` (0.0–1.5 s), a kept silent reaction on `_b`** (2026-09-27, L43): four takes on `frame_cleopatra` all had a blurred shape (the host) push into the bottom-left corner. `_b` also keeps her in the same pose either side of his line, since `P1_005` is on `_b`. `Shots/P1_003a.mp4` is a copy of `P1_126`; the edit uses its first 1.5 s. **added 2026-09-27 (Salah).** A turn clip never hands straight to the same speaker's next clip: a short guest reaction sits between them, so the host comes back on a built seed with the right eyeline.

**P1_004** · INTERJECTION · HOST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_host_b` · 29 syllables · needs 11.0s (duration model v4)

*Starts from the built seed `frame_host_b`, not from P1_003: the guest cut-away P1_003a sits between them, so wherever the turn ended never shows.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, now turned to her, warm and formal as he names her, then plain and simple for the thanks. A greeting, not a build — his tone stays level and easy. The host (in a warm, formal tone): "Welcome to History Answers Back. Cleopatra, seventh of the name, last queen of the Tolemies. Thank you for being here." He stays leaning forward, hands clasped between his knees, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Welcome to History Answers Back. Cleopatra, seventh of the name, last queen of the Ptolemies. Thank you for being here.
**provenance:** `[D]` Documented — last reigning Ptolemaic monarch, 51–30 BC: Roller, *Cleopatra: A Biography*.
**edit_placement:** on picture for *"Welcome to History Answers Back. Cleopatra, seventh of the name,"* only — then `P1_005` covers him from *"last queen of the Ptolemies"* to the end. The title and the thanks play on **her** face.
**SFX:** studio room tone only.
**screen:** G 4.1 · H 4.0 · 2UP 0.0 · BROLL 0.0

**P1_005** · REACTION · GUEST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `frame_cleopatra_b` · `end_frame` `frame_cleopatra_b` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence while she is introduced. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap. She receives it with composure, courteous but not warm: her chin lifts a fraction, then her gaze settles on him and holds there, on the point of answering.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_004` from *"last queen of the Ptolemies"* to its end, then holds a beat after he finishes. Her lower third opens here (her first look, `P1_003a`, is too short to carry it). She is still seen before she is heard. `P1_006` chains from this clip.
**Subtitle:** —
**screen:** G 1.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_006** · INTERJECTION · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra_b` · 18 syllables · needs 8.0s (duration model v4)

*Starts from the seed frame that `P1_005` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman answers with cool courtesy — polite, never warm — and the last sentence turns dry. Her tone stays low and level throughout. The woman (in a coolly polite tone): "Thank you." The woman (in a plain tone): "It is rare that I am asked." The woman (in a dry tone): "Usually, others describe me." She stays upright and turned a little toward the left of the frame, hands folded, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Thank you. It is rare that I am asked. Usually, others describe me.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 6.8 · H 0.0 · 2UP 0.0 · BROLL 0.0

**T8 settled on this row (2026-09-24):** Kling's label form won the A/B (`shots/_tests/T_008_A.mp4` vs `T_008_B.mp4`) — clearer change of delivery between sentences, visible in her face. Keep `T_008_B` as `P1_006`. Both takes strain on the last word *"described"* (a /skr/ cluster and a final /bd/) — a word-final stop cluster as a clip's last word; hide it with the cut, or Kling's lip-sync tool.

### Act A — The word

*Question: Is "seductress" a description of her — or a verdict somebody needed?*

**P1_007** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host_c` · 17 syllables · needs 7.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, direct and light, opening the questioning. He places the word plainly and asks the real question openly, his voice lifting at the end — curious, never mocking. The host (in a light tone): "Then let's start with the description." The hand on his shin loosens and rests there. The host (plainly): "Seductress." The host (in a curious tone): "Is any of it true?" His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then let's start with the description. Seductress. Is any of it true?
**provenance:** `[V]` Voice
**edit_placement:** his first proper cross-shot appearance — **the host's lower third opens here**.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 6.6 · 2UP 0.0 · BROLL 0.0

**P1_008** · INTERVIEW · GUEST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_cleopatra_e` · 13 syllables · needs 5.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman corrects the premise coolly. The second sentence is plain, with the weight held underneath it — she does not raise her voice or underline it. The woman (in a cool tone): "They came for my treasury." Her chin lifts a fraction higher. The woman (in a plain, serious tone): "They wrote about my bed." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** They came for my treasury. They wrote about my bed.
**provenance:** `[I]` Inferred — Suetonius, *Julius* 54; Plutarch, *Life of Antony* 25, 56: the Romans who came to her came for money.
**edit_placement:** **HOOK, first option** — Mode 6 re-picks the hook from the finished part. Key line 1. **Two-up #1** with `P1_009` from *"They came for my treasury"* to ~1.5 s after her last word — his nod beside her, not instead of her.
**test:** `T6` (see §4b)
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.0 · 2UP 4.3 · BROLL 0.0
**twoup:** #1

**P1_009** · REACTION · HOST · **7s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **56 cr**
`start_frame` `frame_host_e` · `end_frame` `frame_host_e` — **the same seed frame** (Standard's end-frame slot)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host holds her look. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He stays settled back, hands loosely clasped in his lap, shoulders square. He takes it in, his head steady and his shoulders settled; he stays that way.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #1** (left), beside `P1_008` (right) from *"They came for my treasury"* to ~1.5 s after her line. Not on screen alone.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 1.5 · BROLL 0.0
**test:** `T6` (see §4b)

**P1_010** · REACTION · GUEST · **8s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **64 cr**
`start_frame` `chain from P1_008`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds the position she is in, composed and unhurried; her gaze stays on him, and she is otherwise still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** her held face after `P1_008`: **pull-quote 01 lands here** (a 3 s beat), then `P1_011` runs under her. `P1_012` chains from this clip.
**Subtitle:** —
**screen:** G 3.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_011** · INTERVIEW · HOST · **5s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **40 cr** · audio only — picture never used
`start_frame` `frame_host` · 10 syllables · needs 4.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, curious, pressing lightly — he offers the popular version rather than endorsing it. His tone stays easy. The host (in a curious tone): "But the beauty." One hand turns slightly open on the armrest and rests there. The host (in a light, curious tone): "That's the part people know." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** But the beauty. That's the part people know.
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_010` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 3.6 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_012** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `chain from P1_010` · 36 syllables · needs 12.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry and plain. A faint pride comes in on the last sentence and stays kept under — never boastful. The woman (in a dry tone): "I was never the most beautiful woman at my own table." One hand turns slightly open and rests there. The woman (in a plain tone): "I was the one worth talking to." The woman (in a quietly proud tone): "And I could do it in the other man's language." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I was never the most beautiful woman at my own table. I was the one worth talking to. And I could do it in the other man's language.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 27: her beauty "not altogether incomparable"; "converse with her had an irresistible charm"; many languages.
**SFX:** studio room tone only.
**screen:** G 11.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_013** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host_d` · 26 syllables · needs 10.7s (duration model v4, +1.0 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, checking a fact. He reads the list evenly, one name after another, without performing it. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a plain tone): "The sources name seven peoples you spoke to without an interpreter." He leans in a fraction, the lowered hand staying on the armrest. The host (in an even tone): "Hebrews, Arabs, Meeds, Parthians." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** The sources name seven peoples you spoke to without an interpreter. Hebrews, Arabs, Medes, Parthians.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 27.
**edit_placement:** on picture to *"without an interpreter."*, then `P1_014` takes the picture for the list — her languages, on her face. **+1 s:** the line ends on a comma list of names (Mode 4 §2, measured on this clip in T1: the 8 s take ran its speech to the last frame).
**SFX:** studio room tone only.
**screen:** G 1.9 · H 4.2 · 2UP 0.0 · BROLL 0.0

**T1 settled 2026-09-24 on this row:** a separate `Pronunciation:` paragraph was read aloud (*"Medes"* said twice, `shots/_tests/T1_A.mp4`); the respelling *"Meeds"* inside the quote was right (`T1_B.mp4`, 8 s — regenerate at 9 s for a clean tail). The prompt now carries the respelling; the subtitle keeps *Medes*.

**P1_014** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_cleopatra_b` · `end_frame` `frame_cleopatra_b` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap. Her head rests tilted very slightly to one side and stays there; her gaze stays on him.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_013` from *"Hebrews"* to its end. `P1_015` chains from this clip.
**Subtitle:** —
**screen:** G 0.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_015** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_b` · 34 syllables · needs 12.2s (duration model v4)

*Starts from the seed frame that `P1_014` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain. The last sentence is the point, and she makes it a little cooler — never scornful. The woman (in a plain, cool tone): "And Egyptian. My family had been kings of Egypt for nearly three hundred years. I was the first of us who bothered to learn it." On "the first of us" her folded hands loosen slightly and rest. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And Egyptian. My family had been kings of Egypt for nearly three hundred years. I was the first of us who bothered to learn it.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 27; Ptolemy I king from 305 BC: Roller, *Cleopatra: A Biography*.
**edit_placement:** **Context card 01** (the Ptolemies) enters on *"My family"*.
**SFX:** studio room tone only.
**screen:** G 10.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_016** · INTERJECTION · HOST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `frame_host` · 7 syllables · needs 4.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, surprised and quick, then genuinely asking — his voice lifts at the end. Never incredulous. The host (in a surprised tone): "Hold on." He shifts his weight a little forward in the chair, forearms staying on the armrests. The host (in a curious tone): "You're not Egyptian?" His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Hold on. You're not Egyptian?
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 2.9 · 2UP 0.0 · BROLL 0.0

**P1_017** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra` · 28 syllables · needs 10.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, even and factual, dry on the last sentence. Her tone stays low and level. The woman (in an even, dry tone): "Macedonian. My ancestor was one of Alexander's generals. We came to Egypt as its conquerors." She stays upright, hands resting together in her lap, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Macedonian. My ancestor was one of Alexander's generals. We came to Egypt as its conquerors.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 27; Roller, *Cleopatra: A Biography*.
**SFX:** studio room tone only.
**screen:** G 9.1 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_018** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host_b` · 22 syllables · needs 8.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, puzzled, working it out slower. He sets out the premise and asks the question plainly, his voice lifting at the end — curious, not a challenge. The host (in a puzzled tone): "Then here's what I don't understand." His clasped hands loosen a little and stay loosely together; he stays leaning in. The host (in a level tone): "The richest kingdom in the world." The host (in a plain, curious tone): "Why does it need Rome?" His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then here's what I don't understand. The richest kingdom in the world. Why does it need Rome?
**provenance:** `[I]` Inferred
**edit_placement:** on picture to *"in the world."*, then `P1_019` for *"Why does it need Rome?"*
**SFX:** studio room tone only.
**screen:** G 1.2 · H 5.3 · 2UP 0.0 · BROLL 0.0

**P1_019** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `frame_cleopatra_e` · `end_frame` `frame_cleopatra_e` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays settled back, hands loosely clasped in her lap, chin a fraction high. Her chin lifts a fraction; otherwise she is still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_018` from *"Why does it need Rome?"*. `P1_020` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0
**test:** `T2` (see §4b)

**P1_020** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_e` · 29 syllables · needs 11.0s (duration model v4)

*Starts from the seed frame that `P1_019` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman states it flatly. The cost sits under the second sentence; the last is dry. Her voice stays low and never hardens. The woman (flatly): "Because it had no army that Rome could not beat, and Rome knew it." The woman (in a low, serious tone): "My father knew it best." Her chin lifts a fraction higher. The woman (in a dry tone): "He paid Rome to call him king." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Because it had no army that Rome could not beat, and Rome knew it. My father knew it best. He paid Rome to call him king.
**provenance:** `[D]` Documented — Suetonius, *Julius* 54.
**test:** `T2` (see §4b)
**SFX:** studio room tone only.
**screen:** G 9.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_021** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_c` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, short and plain — a follow-up, not a challenge. The host (plainly): "Paid how much?" He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Paid how much?
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.7 · 2UP 0.0 · BROLL 0.0

**P1_022** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_c` · 27 syllables · needs 11.6s (duration model v4, +1.0 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level — she lets the number do the work and does not stress it. The last sentence is dry, never bitter. The woman (in a level, dry tone): "Nearly six thousand talents, to Seezer and Pompee. In Rome you pay first. Then they decide whether you exist." On "In Rome" the open hand in her lap turns a little further open and rests. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Nearly six thousand talents, to Caesar and Pompey. In Rome you pay first. Then they decide whether you exist.
**provenance:** `[D]` Documented — Suetonius, *Julius* 54 ("nearly six thousand talents", in his own name and Pompey's).
**edit_placement:** **Context card 02** (talent) enters on *"talents"*. +1 s of tail so `P1_023` has room under her.
**SFX:** studio room tone only.
**screen:** G 8.9 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_023** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_f` · 2 syllables · needs 1.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, dry and low, almost to himself. No emphasis. The host (in a low, dry voice): "Charming." He stays easy in the chair, one arm over the front of the armrest, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Charming.
**provenance:** `[V]` Voice
**edit_placement:** audio only, under the tail of `P1_022` after *"whether you exist"* — `OFFMIC`. Picture discarded; we stay on her.
**SFX:** studio room tone only.
**screen:** G 0.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_024** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `chain from P1_022`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds his gaze, entirely composed, the faintest dryness at the corner of her mouth.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_022`: carries the tail of her line (with `P1_023`'s *"Charming."* under it) and `P1_025`. `P1_026` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_025** · INTERVIEW · HOST · **5s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **40 cr** · audio only — picture never used
`start_frame` `frame_host_d` · 9 syllables · needs 4.0s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, pressing — curious rather than accusing. His voice lifts at the end. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a curious tone): "Did Rome ever just try to take it?" On "take it" he leans in a fraction, the lowered hand staying on the armrest. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Did Rome ever just try to take it?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_024` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 2.1 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_026** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `chain from P1_024` · 36 syllables · needs 12.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain and exact. The last sentence is dry — a fact of life, not a complaint. The woman (in a plain tone): "When I was a child, a Roman censor tried to make my country pay tribute to Rome." One hand turns slightly open and rests there. The woman (in a precise tone): "He lost the argument." The woman (in a dry tone): "Somebody always tries again." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** When I was a child, a Roman censor tried to make my country pay tribute to Rome. He lost the argument. Somebody always tries again.
**provenance:** `[D]` Documented — Plutarch, *Life of Crassus* 13 (65 BC); the last sentence is `[I]`, her reading.
**SFX:** studio room tone only.
**screen:** G 11.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_027** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_e` · 6 syllables · needs 2.6s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, moving the story on, level and simple. The host (in a level tone): "And when your father died?" He stays settled back, hands clasped in his lap, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And when your father died?
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.4 · 2UP 0.0 · BROLL 0.0

**P1_028** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_i` · 39 syllables · needs 12.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain. An edge comes into the last sentence and stays under control — no heat. The woman (in a plain tone): "He left the kingdom to me and to my brother, and he made Rome swear to see it done." She turns a fraction further toward the left of the frame, where the person opposite her sits, and holds. The woman (in a cooler tone): "Within three years my brother's men had driven me out of my own city." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** He left the kingdom to me and to my brother, and he made Rome swear to see it done. Within three years my brother's men had driven me out of my own city.
**provenance:** `[D]` Documented — Caesar, *Civil War* 3.103, 3.108.
**SFX:** studio room tone only.
**screen:** G 10.4 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_029** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_host_d` · 10 syllables · needs 5.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, setting the scene, then plain on the name. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a calm tone): "Which is where Rome arrives." He settles back a fraction, the lowered hand resting on the armrest. The host (in a plain tone): "Pompee first." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Which is where Rome arrives. Pompey first.
**provenance:** `[D]` Documented — Caesar, *Civil War* 3.103.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 3.6 · 2UP 0.0 · BROLL 0.0

**P1_030** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_e` · 36 syllables · needs 12.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman tells it as cool narration. The last sentence is colder and lower, and it does not break. The woman (in a cool tone): "Pompee came running from Seezer and landed below my brother's camp. They killed him on the shore. When Seezer arrived, they handed him the head." She stays settled back, hands loosely clasped in her lap, chin a fraction high, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Pompey came running from Caesar and landed below my brother's camp. They killed him on the shore. When Caesar arrived, they handed him the head.
**provenance:** `[D]` Documented — Caesar, *Civil War* 3.103–104; Plutarch, *Life of Caesar* 48.
**edit_placement:** **Context card 03** (Pompey) enters on her *"Pompey"* — moved from the host's *"Pompey first."*, where a card on his side (R) would ride onto her face at the cut. `MUSIC_Drone_Low` enters under this line. `P1_031` covers from *"they handed him the head"*.
**SFX:** studio room tone only.
**screen:** G 8.3 · H 0.0 · 2UP 0.0 · BROLL 1.4

**P1_031** · BROLL_GEN · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr** + 3 cr still

> A signet ring in an open palm, cut off at the wrist.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A man's open palm held out toward us, seen close and cut off at the wrist, a heavy signet ring lying loose in the middle of the palm, drawn in the same charcoal greys as everything else. At the wrist, the loose draped fold of a plain wool tunic sleeve. Nothing else in frame, no face. No colour anywhere; no cuff, no buttons, no knitted or tailored sleeve.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly toward the ring.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The fingers close a fraction around the ring and stop. Nothing else moves.

 Audio: ambience only — a faint wash of sea on a shore, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_030` from *"they handed him the head"*, runs under `P1_032` (his *"And Caesar?"* is heard, not seen), and cuts back to her on the first word of `P1_033`. The head is never shown; the ring stands for it (Plutarch, *Life of Caesar* 48).
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 1.0

**P1_032** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, quietly. A prompt, nothing more. The host (quietly): "And Seezer?" He stays settled back, forearms along the armrests, and holds still after the last word. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And Caesar?
**provenance:** `[V]` Voice
**edit_placement:** picture replaced by `P1_031` — his voice runs under the b-roll.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.7

**P1_033** · INTERVIEW · GUEST · **14s** · Kling 3.0 Turbo, audio on · 10 cr/s · **140 cr**
`start_frame` `frame_cleopatra_b` · 29 syllables · needs 13.6s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level. She grows drier through the middle, and the last two sentences are stated as a plain principle — not bitter, not raised. The woman (in a level, dry tone): "He turned from the head. He took the ring, and wept. My brother had expected thanks. Rome does not thank you. It judges you." On "Rome does not thank you" her folded hands loosen slightly and rest. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** He turned from the head. He took the ring, and wept. My brother had expected thanks. Rome does not thank you. It judges you.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 48; Caesar, *Civil War* 3.107 (Caesar claims to arbitrate).
**edit_placement:** Key line 2: *"Rome does not thank you. It judges you."* **Two-up #2** with `P1_034` from *"Rome does not thank you"* to ~1 s after her line.
**SFX:** studio room tone only.
**screen:** G 7.3 · H 0.0 · 2UP 3.4 · BROLL 0.0
**twoup:** #2

**P1_034** · REACTION · HOST · **6s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **48 cr**
`start_frame` `frame_host_b` · `end_frame` `frame_host_b` — **the same seed frame** (Standard's end-frame slot)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He stays leaning forward, elbows on his thighs, hands loosely clasped between his knees. He goes still where he is, his gaze on her.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #2** beside `P1_033`, from *"Rome does not thank you"*. `MUSIC_Drone_Low` fades out across it.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 1.0 · BROLL 0.0

**P1_035** · REACTION · GUEST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `chain from P1_033`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds the position she is in, perfectly still, her gaze level on him.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** her held face after `P1_033`: **pull-quote 02 lands here** (a 3.5 s beat, soundscape only). Then cut to him for `P1_036`.
**Subtitle:** —
**screen:** G 3.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_036** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_e` · 24 syllables · needs 6.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, putting the geography together for himself, level and exact. The host (in a level tone): "So the judge is in your palace, and you're outside the city, with your brother's army between you." On "between you" his clasped hands loosen slightly and rest in his lap. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** So the judge is in your palace, and you're outside the city, with your brother's army between you.
**provenance:** `[D]` Documented — Caesar, *Civil War* 3.103, 3.107.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 5.6 · 2UP 0.0 · BROLL 0.0

**P1_037** · INTERJECTION · GUEST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_cleopatra_i` · 1 syllables · needs 1.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain. One word, nothing added. The woman (plainly): "Yes." She stays square, arms along the armrests, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Yes.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.2 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_038** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `chain from P1_037`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds his gaze and lets the silence sit; nothing else moves.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** the `BEAT` after her *"Yes."* on her face, then `P1_039` under it — the act's open loop plays on her. Cut straight to the act break.
**Subtitle:** —
**screen:** G 1.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_039** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_c` · 6 syllables · needs 2.6s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, leaning in, genuinely curious. The voice lifts at the end. The host (in a curious tone): "So how do you get in?" He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** So how do you get in?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_038` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded. the act's open loop — cut straight to the act break.
**SFX:** studio room tone only.
**screen:** G 1.4 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_040** · BRAND_ACTBREAK · **5.0s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_actbreak_vessel.mp4` — fixed furniture, zero credits.
**edit_placement:** plays between `P1_039` and `P1_041`. Hard cut in, hard cut out at **5.000** — a finished object, never trimmed.
**Subtitle:** —
**SFX:** inside the file.

### Act B — Caesar

*Question: Did she seduce Caesar — or recruit him?*

**P1_041** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_c` · 20 syllables · needs 7.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry and exact. A flicker of pride shows on the last words and is not indulged. The woman (in a dry tone): "In a sack for bedding. Tied with a cord, and carried in through the doors to Seezer." On "carried in" the open hand in her lap turns a little further open and rests. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** In a sack for bedding. Tied with a cord, and carried in through the doors to Caesar.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 49.
**edit_placement:** answers `P1_039` across the break.
**SFX:** studio room tone only.
**screen:** G 6.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_042** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_c` · 5 syllables · needs 2.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, amused, checking the famous version. Light, never mocking. The host (in an amused tone): "Not in a carpet." He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Not in a carpet.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 49.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.2 · 2UP 0.0 · BROLL 0.0

**P1_043** · INTERVIEW · GUEST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `frame_cleopatra_e` · 13 syllables · needs 4.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry, with a trace of amusement she keeps small. The woman (in a dry, amused tone): "The carpet came later, from people who were not there." She stays settled back, hands loosely clasped in her lap, chin a fraction high, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** The carpet came later, from people who were not there.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 49.
**SFX:** studio room tone only.
**screen:** G 3.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_044** · INTERVIEW · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_f` · 11 syllables · needs 3.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, leading her on, a smile under it. His tone stays light and never leering. The host (in a light, teasing tone): "And that night, you and Seezer became lovers." On "you and Caesar" the hand on his thigh lifts and turns outward toward the right of the frame, still moving as he goes on. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And that night, you and Caesar —
**provenance:** `[V]` Voice
**edit_placement:** interrupted by `P1_046` after *"Caesar"* — cut. `CUT-IN` A: the whole line is generated so the model never has to stop; **the subtitle and the cut stop at *"Caesar"***.
**test:** `T5` (see §4b)
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.6 · 2UP 0.0 · BROLL 0.0

**P1_045** · REACTION · HOST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_044 at 2.95s` — the frame at the end of *"Caesar"* (timed on the take); in Kling, set the start frame from `P1_044` at this time

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. His lips close in the first moment and stay gently closed, his jaw still. His hands stay where they are and his eyes go to her.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** follows `P1_044` at the cut, `P1_046`'s audio over it. `CUT-IN` B, the stop.
**Subtitle:** —
**screen:** G 0.0 · H 0.5 · 2UP 0.0 · BROLL 0.0
**test:** `T5` (see §4b)

**P1_046** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra` · 25 syllables · needs 11.9s (duration model v4, +0.5 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman comes in over him, cool and firm but not loud. She is plain in the middle and exact on the last sentence. The woman (in a cool, firm tone): "Not lovers. That night I became his ally. The rest followed the alliance. Not the other way round." From her first word she turns a fraction toward the left of the frame, where the person opposite her sits, and stays turned — already moving as she speaks, no pause before it. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Not lovers. That night I became his ally. The rest followed the alliance. Not the other way round.
**provenance:** `[I]` Inferred — Caesar, *Civil War* 3.107–108 and Plutarch, *Life of Caesar* 49: Caesar takes up her claim to the throne.
**edit_placement:** enters over `P1_045` — interruption, audio overlaps ~0.3 s before the cut. Trim her lead-in: the first word must land on the cut.
**test:** `T5` (see §4b)
**SFX:** studio room tone only.
**screen:** G 9.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_047** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_046`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She takes the point without moving, her gaze steady on him.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_046`: carries `P1_048`. `P1_049` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_048** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **32 cr** · audio only — picture never used
`start_frame` `frame_host_d` · 5 syllables · needs 3.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, pressing — a plain observation, not an accusation. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a firm tone): "It didn't keep you safe." The lowered hand stays on the armrest and he holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** It didn't keep you safe.
**provenance:** `[I]` Inferred — Cassius Dio, *Roman History* 42.38–39.
**edit_placement:** audio only, under `P1_047` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 1.2 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_049** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `chain from P1_047` · 31 syllables · needs 12.3s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain narration. She grows colder toward the last sentence and stays level. The woman (in a cool tone): "No. My brother's people shut us inside the palace quarter for a winter. They made my sister queen. And the harbour burned." On "my sister" one hand turns slightly open and rests there. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** No. My brother's people shut us inside the palace quarter for a winter. They made my sister queen. And the harbour burned.
**provenance:** `[D]` Documented — Cassius Dio, *Roman History* 42.39 (Arsinoe declared queen); Plutarch, *Life of Caesar* 49; Cassius Dio, *Roman History* 42.38 (the fire).
**SFX:** studio room tone only.
**screen:** G 8.4 · H 0.0 · 2UP 0.0 · BROLL 1.4

**P1_051** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_e` · 17 syllables · needs 6.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host offers the famous version, with a small challenge in it. Level, never scoring a point. The host (in a light tone): "And the Library of Alexandria went with it." His clasped hands loosen slightly and rest in his lap. The host (in a lightly challenging tone): "That's the story." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And the Library of Alexandria went with it. That's the story.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 49; Cassius Dio, *Roman History* 42.38.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 5.3 · 2UP 0.0 · BROLL 0.0

**P1_052** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_c` · 21 syllables · needs 7.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, even. She leaves the argument to posterity and does not take a side. The woman (in an even tone): "Books burned, in the fire by the docks." The open hand in her lap turns a little further open and rests. The woman (in an even tone): "How many, and whose, your scholars are still arguing." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Books burned, in the fire by the docks. How many, and whose, your scholars are still arguing.
**provenance:** `[I]` Inferred — Plutarch, *Life of Caesar* 49 and Cassius Dio, *Roman History* 42.38 both report the fire reaching the library; its scale is a modern debate.
**SFX:** studio room tone only.
**screen:** G 6.2 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_053** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `chain from P1_052`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. At her sister's name her gaze holds on him a moment longer; nothing else moves.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_052`: the name lands on **her** face. `P1_055` chains from this clip.
**Subtitle:** —
**screen:** G 0.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_054** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **32 cr** · audio only — picture never used
`start_frame` `frame_host` · 6 syllables · needs 3.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host turns the subject and places the name gently. Quiet, not probing. The host (in a calm tone): "Your sister." The host (gently): "Arsinowee." He stays settled back, forearms along the armrests, and holds still after the last word. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Your sister. Arsinoe.
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_053` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 2.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_055** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `chain from P1_053` · 25 syllables · needs 7.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level. She grows cooler and exact on the triumph, and does not dwell. The woman (in a level tone): "Arsinowee." The woman (in a cooler tone): "When it was over, Seezer took her to Rome and led her through the streets in chains, in his triumph." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Arsinoe. When it was over, Caesar took her to Rome and led her through the streets in chains, in his triumph.
**provenance:** `[D]` Documented — Cassius Dio, *Roman History* 43.19.
**edit_placement:** **Context card 04** (Arsinoe IV) enters on her *"Arsinoe"*. `P1_056` covers from *"led her through the streets"*; the card rides over it.
**SFX:** studio room tone only.
**screen:** G 3.5 · H 0.0 · 2UP 0.0 · BROLL 2.3

**P1_056** · BROLL_GEN · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr** + 3 cr still

> A captive walked through a Roman street in chains, seen from behind a crowd.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A narrow Roman street seen from behind the crowd lining it.

 A Roman street crowd of the late Republic seen from behind and in half-shadow: men in plain off-white wool tunics, a few wrapped in heavy off-white togas; women in long dark stolas with a mantle over the head. Leather sandals and closed shoes. No armour, no plate, no laurel wreaths on the crowd, no purple.

 Beyond their heads, down the middle of the street, a young woman walks away from us in a plain long dress, her wrists bound in front of her with a chain, small in frame, her face not visible.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly over the heads of the crowd.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The crowd shifts and turns to watch; the young woman walks slowly on, away from us.

 Audio: ambience only — a murmuring street crowd, distant and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_055` from *"led her through the streets"* to its end, then cuts to the host on `P1_057`. Arsinoe is seen from behind only — no likeness claim.
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**added in Mode 4.** The outline registers `roman_crowd_late_republic` *"for the triumph row (Arsinoe)"* but marks no `BROLL` for it; the drama asks for the picture (the act's image, per the outline's arc table), so the row is added here.

**P1_057** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_d` · 7 syllables · needs 3.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, quietly — laying the fact beside the last one, not accusing. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (quietly): "And you were in Rome that year." The lowered hand stays on the armrest and he holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And you were in Rome that year.
**provenance:** `[D]` Documented — Cassius Dio, *Roman History* 43.27.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.6 · 2UP 0.0 · BROLL 0.0

**P1_058** · INTERJECTION · GUEST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_cleopatra_e` · 7 syllables · needs 3.8s (duration model v4, +1.0 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain. She adds nothing to it. The woman (plainly): "I was living in his house." She stays settled back, hands loosely clasped in her lap, chin a fraction high, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I was living in his house.
**provenance:** `[D]` Documented — Cassius Dio, *Roman History* 43.27.
**edit_placement:** +1 s of tail so `P1_059` has room under her.
**SFX:** studio room tone only.
**screen:** G 1.6 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_059** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_c` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host repeats it low, thinking aloud. No emphasis. The host (in a low voice): "In his house." He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** In his house.
**provenance:** `[V]` Voice
**edit_placement:** audio only, under the tail of `P1_058` — `OFFMIC`. Picture discarded.
**SFX:** studio room tone only.
**screen:** G 0.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_060** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `chain from P1_058`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds the position she is in, entirely composed; her gaze stays on him and she is otherwise still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_058`: the `BEAT` after his echo, soundscape only, then `P1_061` under it — the question plays on her. `P1_062` chains from this clip.
**Subtitle:** —
**screen:** G 2.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_061** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_b` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, gently. A real question, quietly asked, never prosecuting. The host (gently): "Did you watch?" He stays leaning forward, hands clasped between his knees, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Did you watch?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_060` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 0.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_062** · INTERVIEW · GUEST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `chain from P1_060` · 9 syllables · needs 4.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, even. The second sentence is a fraction lower, and her voice stays steady. The woman (in an even tone): "The crowd pitied her." The woman (in a lower voice): "That much I know." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** The crowd pitied her. That much I know.
**provenance:** `[D]` Documented — Cassius Dio, *Roman History* 43.19.
**edit_placement:** **Two-up #3** with `P1_063` from *"The crowd pitied her"* to ~2 s after her line — he waits, he does not ask again.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.0 · 2UP 3.4 · BROLL 0.0
**twoup:** #3

**P1_063** · REACTION · HOST · **7s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **56 cr**
`start_frame` `frame_host` · `end_frame` `frame_host` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host waits. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He stays settled back, his forearms resting along the armrests. He does not move to ask again; his hands stay where they are, and his gaze stays on her.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #3** beside `P1_062`. `P1_064` chains from this clip, full frame.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 2.0 · BROLL 0.0

**P1_064** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host` · 6 syllables · needs 2.6s (duration model v4)

*Starts from the seed frame that `P1_063` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host moves on, level and plain. The host (in a level tone): "You gave Seezer a son." He stays settled back, forearms along the armrests, and holds still after the last word. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** You gave Caesar a son.
**provenance:** `[D]` Documented — Suetonius, *Julius* 52.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.4 · 2UP 0.0 · BROLL 0.0

**P1_065** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_b` · 25 syllables · needs 10.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain, then deliberate on the last sentence — a decision owned, not a boast. The woman (in a deliberate tone): "I gave him a son, and I gave the boy his name. Seezer. I knew what that name was worth when I chose it." On "I knew" she turns a fraction further toward the left of the frame, where the person opposite her sits. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I gave him a son, and I gave the boy his name. Caesar. I knew what that name was worth when I chose it.
**provenance:** `[D]` Documented — Suetonius, *Julius* 52; Plutarch, *Life of Caesar* 49.
**edit_placement:** the callback Part 2 pays (*"I gave him the name that killed him"*).
**SFX:** studio room tone only.
**screen:** G 8.4 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_066** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_c` · 7 syllables · needs 2.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host turns the story, plain and quiet. The host (in a calm tone): "And then the Eyeds of March." He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And then the Ides of March.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.6 · 2UP 0.0 · BROLL 0.0

**P1_067** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra` · 36 syllables · needs 11.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, cool and exact. The cost sits under the second sentence and stays held — never raised. The woman (in a cool tone): "Twenty-three wounds, at the foot of Pompee's statue." One hand turns slightly open in her lap and rests there. The woman (in a low, serious tone): "The man who stood between Rome and my throne was dead, and I was a foreign queen living in his house." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Twenty-three wounds, at the foot of Pompey's statue. The man who stood between Rome and my throne was dead, and I was a foreign queen living in his house.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 66; Cassius Dio, *Roman History* 43.27.
**SFX:** studio room tone only.
**screen:** G 9.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_068** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_b` · 16 syllables · needs 6.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host lays out the stakes, then presses. His voice lifts on the question; he never prosecutes. The host (in a serious tone): "Rome was about to tear itself apart again." He leans in a fraction further, hands staying clasped between his knees. The host (in a firm tone): "Who did you back?" His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Rome was about to tear itself apart again. Who did you back?
**provenance:** `[I]` Inferred — the civil wars after Caesar's death.
**edit_placement:** on picture to *"apart again."*, then `P1_069` for *"Who did you back?"*
**SFX:** studio room tone only.
**screen:** G 0.9 · H 2.8 · 2UP 0.0 · BROLL 0.0

**P1_069** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `frame_cleopatra_c` · `end_frame` `frame_cleopatra_c` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. Her forearm stays along the armrest and her other hand rests open in her lap. Her chin lifts a fraction.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_068` from *"Who did you back?"*. `P1_070` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_070** · INTERVIEW · GUEST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_cleopatra_c` · 16 syllables · needs 6.2s (duration model v4)

*Starts from the seed frame that `P1_069` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, flat, then dry on the second sentence. Nothing apologetic in it. The woman (in a flat tone): "Whoever was going to win." The woman (in a dry tone): "It took me some time to learn who that was." Her forearm stays along the armrest and her open hand rests in her lap; her gaze stays on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Whoever was going to win. It took me some time to learn who that was.
**provenance:** `[I]` Inferred
**edit_placement:** end of Act B. `BRAND_subscribe` may go over her held tail here (Mode 6).
**SFX:** studio room tone only.
**screen:** G 5.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

### Act C — Antony

*Question: Was Antony a lover — or a policy?*

**P1_071** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_d` · 12 syllables · needs 6.0s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host brightens as the story moves, then plain on the summons. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a brighter tone): "Which brings us to Tarsus." He settles back a fraction, the lowered hand resting on the armrest. The host (in a plain tone): "Antonee summons you." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Which brings us to Tarsus. Antony summons you.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 25–26.
**edit_placement:** **Context card 05** (Tarsus) enters on *"Tarsus"* — side R, over him. `P1_072` holds his face through her first sentence so the card never rides onto hers.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 4.1 · 2UP 0.0 · BROLL 0.0

**P1_072** · REACTION · HOST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_071`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He holds the position he is in and keeps his gaze on her, with the ghost of a smile.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_073` from its first word (J-cut: her voice over his face) to *"to his enemy"* — cut to her on *"to his enemy, Cassius"*, after context card 05 (side R) has gone. Chained from `P1_071`. It exists so the card finishes over his side of the room.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_073** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_i` · 20 syllables · needs 7.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry, then exact on the detail. Her tone stays low. The woman (in a dry tone): "To answer a charge." The fingers of her near hand spread over the end of the armrest and rest. The woman (in a precise tone): "He had heard that I gave money to his enemy, Cassius." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** To answer a charge. He had heard that I gave money to his enemy, Cassius.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 25.
**SFX:** studio room tone only.
**screen:** G 1.6 · H 3.0 · 2UP 0.0 · BROLL 0.0

**P1_074** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_f` · 10 syllables · needs 3.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host echoes it back, amused. Light, never sarcastic. The host (in an amused tone): "You were summoned to answer a charge." He stays easy in the chair, one arm over the front of the armrest, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** You were summoned to answer a charge.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 2.3 · 2UP 0.0 · BROLL 0.0

**P1_075** · INTERVIEW · GUEST · **15s** · Kling 3.0 Turbo, audio on · 10 cr/s · **150 cr**
`start_frame` `frame_cleopatra_b` · 43 syllables · needs 14.3s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, the faintest smile held under the words. Exact through the list, dry on the last sentence, and never boastful. The woman (in a dry, amused tone): "I was." The woman (in a precise tone): "So I came up the river in a barge with a gilded stern and purple sails, rowed with silver oars, dressed as Aphrodite." Her folded hands loosen slightly and rest. The woman (in a dry tone): "Nobody mentioned the charge again." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I was. So I came up the river in a barge with a gilded stern and purple sails, rowed with silver oars, dressed as Aphrodite. Nobody mentioned the charge again.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 26; the last sentence is `[I]`.
**SFX:** studio room tone only.
**screen:** G 2.8 · H 0.0 · 2UP 0.0 · BROLL 7.2

**P1_076** · BROLL_GEN · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr** + 3 cr still

> The barge on the river, a crowd along the bank.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 An ancient royal river barge of the 1st century BC seen from the bank at water level: a long low open hull, one mast with a single square sail, a stern post curving high and ending in a carved lotus flower, a long bank of oars dipping, and a cloth canopy on slender posts over the rear deck with a figure seated beneath it, too small to read as a face. A crowd of small anonymous figures in plain tunics and draped mantles, bareheaded, stands along the near shore watching it pass. No cabin, no deckhouse, no funnel, no hats, no modern clothing.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera drifts slowly sideways along the bank, keeping pace with the barge.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The oars dip and rise together; the sail stirs; the figures on the shore turn to follow it.

 Audio: ambience only — oars in water, wind in the sail, a murmur from the shore, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_075` from *"So I came up the river"* to *"dressed as Aphrodite"*; cut back to her for *"Nobody mentioned the charge again."*
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_077** · INTERVIEW · HOST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `frame_host` · 12 syllables · needs 4.0s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host offers the myth plainly, as the version everyone knows. The host (in a light tone): "That's the most famous seduction in history." On "seduction" one hand turns slightly open on the armrest and rests there. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** That's the most famous seduction in history.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 2.8 · 2UP 0.0 · BROLL 0.0

**P1_078** · INTERVIEW · GUEST · **14s** · Kling 3.0 Turbo, audio on · 10 cr/s · **140 cr**
`start_frame` `frame_cleopatra_e` · 37 syllables · needs 12.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman corrects the premise coolly, then plainly; a quiet edge comes into the last sentence and stays quiet. The woman (in a cool tone): "It was a state visit." Her chin lifts a fraction higher. The woman (in a plain tone): "A queen does not arrive at a trial as the accused." The woman (in a quiet, cool tone): "She arrives as a goddess, and the trial becomes a dinner." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** It was a state visit. A queen does not arrive at a trial as the accused. She arrives as a goddess, and the trial becomes a dinner.
**provenance:** `[I]` Inferred — Plutarch, *Life of Antony* 26.
**edit_placement:** Key line 3: *"A queen does not arrive at a trial as the accused."* **Two-up #4** with `P1_079` from *"She arrives as a goddess"* to ~1 s after her line — his silent laugh beside her.
**SFX:** studio room tone only.
**screen:** G 6.0 · H 0.0 · 2UP 4.0 · BROLL 0.0
**twoup:** #4

**P1_079** · REACTION · HOST · **6s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **48 cr**
`start_frame` `frame_host_e` · `end_frame` `frame_host_e` — **the same seed frame** (Standard's end-frame slot)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He stays settled back, hands loosely clasped in his lap, shoulders square. His eyes crease with a silent laugh and stay creased; his head stays steady.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #4** beside `P1_078`.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 1.0 · BROLL 0.0

**P1_080** · REACTION · GUEST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `chain from P1_078`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds the position she is in, composed, the faintest satisfaction held still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** her held face after `P1_078`: **pull-quote 03 lands here** (a 3.5 s beat). Then cut to him for `P1_081`.
**Subtitle:** —
**screen:** G 3.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_081** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host_b` · 19 syllables · needs 6.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, quieter now. He lays the fact down plainly and does not press it. The host (quietly): "And your sister." The host (in a plain tone): "Arsinowee was still alive, in a temple of Artemis." He stays leaning forward, hands clasped between his knees, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And your sister. Arsinoe was still alive, in a temple of Artemis.
**provenance:** `[D]` Documented — Appian, *Civil Wars* 5.9; Josephus, *Jewish Antiquities* 15.89.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 5.7 · 2UP 0.0 · BROLL 0.0

**P1_082** · INTERVIEW · GUEST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_cleopatra` · 12 syllables · needs 5.3s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level and flat. No apology and no emphasis; her voice stays low and does not waver. The woman (in a level tone): "I asked him for her death." The woman (in a flat tone): "He gave it to me." She stays upright, hands resting together in her lap, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I asked him for her death. He gave it to me.
**provenance:** `[D]` Documented — Appian, *Civil Wars* 5.9; Josephus, *Jewish Antiquities* 15.89.
**edit_placement:** **the crack** — Part 1's one.
**SFX:** studio room tone only.
**screen:** G 1.6 · H 1.2 · 2UP 0.0 · BROLL 0.0

**P1_083** · REACTION · HOST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_d` · `end_frame` `frame_host_d` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. His elbow stays on the armrest and his knuckles stay resting against his jaw; his other hand stays on his thigh. His jaw sets and stays set; his gaze stays on her.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **full-frame host reaction 1 of 2** — the crack: covers the tail of `P1_082` from *"He gave it to me"*, then holds. `P1_084` chains from this clip.
**Subtitle:** —
**screen:** G 0.0 · H 1.5 · 2UP 0.0 · BROLL 0.0
**test:** `T6` (see §4b)

**P1_084** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_host_d` · 10 syllables · needs 5.5s (duration model v4)

*Starts from the seed frame that `P1_083` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, plain — he states it, he does not accuse. The second sentence drops lower. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (plainly, in a calm tone): "She was a suppliant." The host (in a low voice): "In a sanctuary." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** She was a suppliant. In a sanctuary.
**provenance:** `[D]` Documented — Appian, *Civil Wars* 5.9.
**edit_placement:** full frame for *"She was a suppliant."*, then cut to her (`P1_086`) — *"In a sanctuary"* plays off screen over her face. Trim the pause between his two sentences to ~0.5 s under the cut.
**test:** `T6` (see §4b)
**SFX:** studio room tone only.
**screen:** G 1.2 · H 1.2 · 2UP 0.0 · BROLL 0.0

**P1_086** · REACTION · GUEST · **6s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **48 cr**
`start_frame` `frame_cleopatra_b` · `end_frame` `frame_cleopatra_b` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap. She holds his gaze, steady; her hands stay where they are and she is otherwise still.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** full frame on her from *"In a sanctuary"* (his words off screen), then the `BEAT` — about 1 s of silence after his last word, no longer — then `P1_087`. Use the clip's **end** (it ends on its seed frame, so `P1_087` joins exactly).
**Subtitle:** —
**screen:** G 1.0 · H 0.0 · 2UP 0.0 · BROLL 0.0
**test:** `T3 · end-frame test` (see §4b)

**End-frame test (Salah's idea, 2026-09-24) — generate this clip with the end-frame slot set to the same seed frame as its start (`frame_cleopatra_b` → `frame_cleopatra_b`), Standard, audio off, stationary preset on.** Judge: does she drift naturally and come back, or does it read as a loop / a rushed return in the last half-second? **If it passes:** `P1_087` starts from `frame_cleopatra_b` itself instead of this clip's last frame — a pixel-identical join with no extraction and no grade — and the kit is rebuilt so every listening reaction that is followed by its speaker's answer works this way (most of Pass 2 disappears). **If it fails:** keep the chain; `P1_087` starts from this clip's last frame as written.

**P1_087** · INTERVIEW · GUEST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_cleopatra_b` · 17 syllables · needs 5.2s (duration model v4)

*Starts from the seed frame that `P1_086` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman speaks quietly and seriously, steady and unhurried. The woman (quietly, in a serious tone): "In my family, the danger to a queen sat at her own table." She stays upright and turned a little toward the left of the frame, hands folded, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** In my family, the danger to a queen sat at her own table.
**provenance:** `[I]` Inferred — her reading of the dynasty; Cassius Dio, *Roman History* 42.39, 43.19.
**edit_placement:** `SPLIT` A — continues on her from `P1_086` (exact join). Seam into `P1_088`: `PUNCH` on the seam, held to the end of `P1_088` (Mode 4 §2, fix b).
**test:** `T3` (see §4b)
**SFX:** studio room tone only.
**screen:** G 4.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_088** · INTERVIEW · GUEST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `chain from P1_087` · 21 syllables · needs 6.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, the personal now — still low. The last sentence is the decision, stated, not defended. The woman (in a low, firm tone): "Rome had already used her against me once. I would not leave it a second chance." On "I would not" her chin lifts a fraction. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Rome had already used her against me once. I would not leave it a second chance.
**provenance:** `[I]` Inferred — her reading of the dynasty; Cassius Dio, *Roman History* 42.39, 43.19.
**edit_placement:** `SPLIT` B — punch-in at *"Rome had already used her"* (the seam), held to the end of the clip.
**test:** `T3` (see §4b)
**SFX:** studio room tone only.
**screen:** G 6.2 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_089** · INTERVIEW · HOST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `frame_host_c` · 9 syllables · needs 4.6s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host lets it go and moves on, plain and level. The host (in a calm tone): "Then there's Antonee." The hand on his shin loosens and rests there. The host (in a level tone): "Three children." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then there's Antony. Three children.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 36, 54.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 3.4 · 2UP 0.0 · BROLL 0.0

**P1_090** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_c` · 27 syllables · needs 12.9s (duration model v4, +1.0 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, even and exact — a list of facts, weighed but not dwelt on. The woman (in an even tone): "Twins first, a boy and a girl. The Sun and the Moon. Then another son. And with them, cities, coastlines, kingdoms." On "kingdoms" the open hand in her lap turns a little further open and rests. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Twins first, a boy and a girl. The Sun and the Moon. Then another son. And with them, cities, coastlines, kingdoms.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 36, 54.
**edit_placement:** +1 s: the line ends on a comma list (Mode 4 §2).
**SFX:** studio room tone only.
**screen:** G 10.2 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_091** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_090`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She hears the question without a flicker; her gaze stays level on him.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_090`: carries `P1_092` — the question plays on her. `P1_093` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_092** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_b` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host asks the obvious question plainly, so she can refuse it. Never teasing. The host (plainly): "Was it love?" He stays leaning forward, hands clasped between his knees, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Was it love?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_091` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 0.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_093** · INTERJECTION · GUEST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `chain from P1_091` · 7 syllables · needs 2.3s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry — amused only in the words, not the voice. The woman (in a dry tone): "You would like me to say yes." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** You would like me to say yes.
**provenance:** `[V]` Voice
**edit_placement:** the callback Part 2 pays (*"You keep handing me that word"*).
**SFX:** studio room tone only.
**screen:** G 1.6 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_094** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_e` · 8 syllables · needs 3.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, not letting go — level, patient, not pushing harder. The host (in a level, firm tone): "I'd like you to say what it was." He stays settled back, hands clasped in his lap, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** I'd like you to say what it was.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.9 · 2UP 0.0 · BROLL 0.0

**P1_095** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_i` · 34 syllables · needs 12.2s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain and exact, cooler on the last sentence. A transaction described, not confessed. The woman (in a plain tone): "It was the only Roman army in the East, and it was loyal to him." The fingers of her near hand spread over the end of the armrest and rest. The woman (in a precise tone): "I needed it." The woman (in a cooler tone): "He needed my grain and my gold to pay for it." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** It was the only Roman army in the East, and it was loyal to him. I needed it. He needed my grain and my gold to pay for it.
**provenance:** `[I]` Inferred — Plutarch, *Life of Antony* 56 (her ships and money).
**SFX:** studio room tone only.
**screen:** G 10.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_096** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host` · 22 syllables · needs 8.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host reaches for the picture — the place, then the image — even and unhurried in manner, never grand. The host (in a warm tone): "Then Alexandria, thirty-four BC." The host (in a calm tone): "The gymnasium." One hand turns slightly open on the armrest and rests there. The host (in a warm tone): "A silver stage, two golden thrones." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then Alexandria, thirty-four BC. The gymnasium. A silver stage, two golden thrones.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 54.
**edit_placement:** `P1_097` covers from *"A silver stage"*. **Context card 06** (Donations) enters on *"thrones"*, over the b-roll.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 4.3 · 2UP 0.0 · BROLL 2.1

**P1_097** · BROLL_GEN · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr** + 3 cr still

> A raised platform with two thrones in a colonnaded hall, a packed crowd.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A raised platform in a colonnaded hall, two thrones on it with seated figures too small to read as faces; a packed crowd in the foreground.

 A crowd of Alexandrians of the late Ptolemaic period seen from behind: men in knee-length undyed linen and wool tunics, some with a pale mantle over one shoulder, a few with shaven heads in plain white linen; women in long pale chitons with a mantle drawn over the head. Bare feet or simple leather sandals. No Egyptian headdresses, no nemes, no gold collars, no armour.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pulls back slowly from the platform over the heads of the crowd.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The crowd shifts; a few heads turn; the seated figures stay still.

 Audio: ambience only — a large crowd murmuring in a stone hall, low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_096` from *"A silver stage"* and runs under the start of `P1_098`; **cut back to her only after context card 06 has left** (it sits on her side, R), around *"with Caesar's son beside me"*.
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_098** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_b` · 35 syllables · needs 11.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, exact, with weight on the titles — stated, never proud. The woman (in a precise tone): "Antonee named me Queen of Egypt, Syprus, Libya and part of Syria, with Seezer's son beside me." She turns a fraction further toward the left of the frame, where the person opposite her sits. The woman (in a serious tone): "Our own sons, he called Kings of Kings." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Antony named me Queen of Egypt, Cyprus, Libya and part of Syria, with Caesar's son beside me. Our own sons, he called Kings of Kings.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 54.
**SFX:** studio room tone only.
**screen:** G 5.0 · H 0.0 · 2UP 0.0 · BROLL 4.4

**P1_099** · REACTION · GUEST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `chain from P1_098`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She lets him finish, entirely still, the faintest dryness at the corner of her mouth.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_098`: carries `P1_100`. `P1_101` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_100** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **48 cr** · audio only — picture never used
`start_frame` `frame_host_f` · 16 syllables · needs 4.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host gives Rome's view, level and attributed — not his own verdict. The host (in a level tone): "In Rome, that looked like a Roman giving Rome's lands away." On "Rome's lands" the hand hanging over the armrest turns slightly open and stays there. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** In Rome, that looked like a Roman giving Rome's lands away.
**provenance:** `[I]` Inferred — Plutarch, *Life of Antony* 54 (Roman disapproval).
**edit_placement:** audio only, under `P1_099` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 3.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_101** · INTERVIEW · GUEST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `chain from P1_099` · 20 syllables · needs 6.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, dry. The barb in the second sentence is delivered flat, not relished. The woman (in a dry tone): "Some of it was not his to give." The woman (in a dry tone): "He gave my son Parthia, which had just beaten him." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Some of it was not his to give. He gave my son Parthia, which had just beaten him.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 54 (Parthia among the gifts); 37–51 (the failed Parthian campaign).
**edit_placement:** **Two-up #6** with `P1_102` from *"He gave my son Parthia"* to ~1 s after her line — his laugh escapes beside her.
**SFX:** studio room tone only.
**screen:** G 1.9 · H 0.0 · 2UP 2.8 · BROLL 0.0
**twoup:** #6

**P1_102** · REACTION · HOST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `frame_host_d` · `end_frame` `frame_host_d` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. His elbow stays on the armrest and his knuckles stay resting against his jaw; his other hand stays on his thigh. His eyes crease with a laugh he holds in, a smile settled at the corners of his closed mouth; his hands stay where they are.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #6** beside `P1_101`. `P1_103` chains from this clip, full frame.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 1.0 · BROLL 0.0

**P1_103** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_d` · 8 syllables · needs 3.8s (duration model v4)

*Starts from the seed frame that `P1_102` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, sobering — quieter, the lightness gone. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a quiet, serious tone): "And Octavian was listening." The lowered hand stays on the armrest and he holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And Octavian was listening.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.9 · 2UP 0.0 · BROLL 0.0

**P1_104** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra` · 18 syllables · needs 7.7s (duration model v4, +1.0 s room)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, cool, then drier on the second sentence. Her tone stays low and even. The woman (in a cool tone): "Octavian was always listening." Her chin lifts a fraction. The woman (in a drier tone): "He needed Rome to hear it his way." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Octavian was always listening. He needed Rome to hear it his way.
**provenance:** `[I]` Inferred
**edit_placement:** **Context card 07** (Octavian) enters on her *"Octavian"* — moved from his, for the same reason as card 03. +1 s of tail so the card has left before the act break. The act's open loop — hold the clip to its end, then the break.
**SFX:** studio room tone only.
**screen:** G 5.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_105** · BRAND_ACTBREAK · **5.0s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_actbreak_stone.mp4` — fixed furniture, zero credits.
**edit_placement:** plays between `P1_104` and `P1_106`. Hard cut in, hard cut out at **5.000** — a finished object, never trimmed.
**Subtitle:** —
**SFX:** inside the file.

### Act D — The charge

*Question: Why did Rome declare war on her, and not on Antony?*

**P1_106** · INTERVIEW · HOST · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr**
`start_frame` `frame_host_b` · 14 syllables · needs 4.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host lays it out plainly, a step in the story. The host (in a plain tone): "So he goes to the Vestal Virgins for Antonee's will." On "will" his clasped hands loosen a little and stay loosely together; he stays leaning in. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** So he goes to the Vestal Virgins for Antony's will.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 58.
**edit_placement:** `MUSIC_Drone_High` enters here. `P1_107` covers from *"Vestal Virgins"*; **context card 08** enters on *"Vestal"*, over the b-roll.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.2 · 2UP 0.0 · BROLL 2.1

**P1_107** · BROLL_GEN · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr** + 3 cr still

> A sealed scroll drawn from a niche in a small shrine, a fire on the hearth.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A small round shrine: a low fire burning on a stone hearth, and in a niche in the wall behind it, sealed scrolls laid side by side. A man's hand in the fold of a heavy wool sleeve reaches into the niche. No faces.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in slowly toward the niche.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The hand draws one sealed scroll out of the niche; the fire moves on the hearth.

 Audio: ambience only — a low fire in a quiet stone room. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_106` from *"Vestal Virgins"* and runs under `P1_108` through *"because they refused him"*; cut back to her on *"Then he read the Senate"* — after context card 08 (side R) has left.
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**added in Mode 4.** Act D had no picture in the outline; the will seized from the Vestals is the act's key political event (a lesson carried in from v1: *give the key political event a picture*), and it gives card 08 somewhere to sit that is not her face.

**P1_108** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra_c` · 26 syllables · needs 8.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, exact on the seizure, then dry on the reading. Her tone stays low. The woman (in a precise tone): "Goes to them, and takes it, because they refused him." The open hand in her lap turns a little further open and rests. The woman (in a dry tone): "Then he read the Senate the parts he had chosen." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Goes to them, and takes it, because they refused him. Then he read the Senate the parts he had chosen.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 58.
**SFX:** studio room tone only.
**screen:** G 2.8 · H 0.0 · 2UP 0.0 · BROLL 3.3

**P1_109** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_108`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds his gaze, composed.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_108`: carries `P1_110`. `P1_111` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_110** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_e` · 7 syllables · needs 2.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, plainly — a prompt. The host (plainly): "And the part that mattered?" He stays settled back, hands clasped in his lap, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And the part that mattered?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_109` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 1.6 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_111** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `chain from P1_109` · 22 syllables · needs 8.4s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level. A thin edge comes in on the last sentence and stays thin. The woman (in a level, cool tone): "That when he died, he wished to be sent to me. In Egypt. Even if he died in Rome." She holds the position she is already in, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** That when he died, he wished to be sent to me. In Egypt. Even if he died in Rome.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 58.
**edit_placement:** the callback Part 2 pays (*"So Antony's will got its way after all"*).
**SFX:** studio room tone only.
**screen:** G 7.7 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_112** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host` · 6 syllables · needs 2.6s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host states the charge plainly, low. The host (plainly): "And Rome declared war." He stays settled back, forearms along the armrests, and holds still after the last word. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And Rome declared war.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 60.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.4 · 2UP 0.0 · BROLL 0.0

**P1_113** · INTERJECTION · GUEST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_cleopatra` · 5 syllables · needs 3.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, flat, then exact on the second sentence. Nothing raised. The woman (in a flat tone): "On me." Her chin lifts a fraction. The woman (in a precise tone): "Not on him." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** On me. Not on him.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 60; Cassius Dio, *Roman History* 50.4.
**edit_placement:** **Two-up #7** with `P1_114` for the whole line and ~1.5 s after — he lets it land, beside her.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.0 · 2UP 2.5 · BROLL 0.0
**twoup:** #7

**P1_114** · REACTION · HOST · **5s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `frame_host_e` · `end_frame` `frame_host_e` — **the same seed frame** (Standard's end-frame slot)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He stays settled back, hands loosely clasped in his lap, shoulders square. He lets it land, entirely still, his gaze on her.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** **the host's half of two-up #7** beside `P1_113`.
**Subtitle:** —
**screen:** G 0.0 · H 0.0 · 2UP 1.5 · BROLL 0.0

**P1_115** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `chain from P1_113`

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She meets the question without moving, her chin a fraction high.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** chained from `P1_113` (full frame again after the two-up): carries `P1_116`. `P1_117` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_116** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_c` · 2 syllables · needs 1.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host asks the real question, quiet and direct. The host (in a curious tone): "Why you?" He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Why you?
**provenance:** `[V]` Voice
**edit_placement:** audio only, under `P1_115` — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.
**SFX:** studio room tone only.
**screen:** G 0.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_117** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `chain from P1_115` · 30 syllables · needs 9.0s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman corrects the premise coolly, then plainly; the barb at the end stays held under. The woman (in a cool tone): "Because a Roman cannot march in triumph over Romans. Over a foreign queen, he can march as often as he likes." On "a foreign queen" one hand turns slightly open and rests there. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Because a Roman cannot march in triumph over Romans. Over a foreign queen, he can march as often as he likes.
**provenance:** `[I]` Inferred — Cassius Dio, *Roman History* 50.4–6 (war declared on her, so Antony's side could desert him as patriots).
**SFX:** studio room tone only.
**screen:** G 8.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_118** · INTERVIEW · HOST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_host_c` · 36 syllables · needs 12.7s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host puts Rome's case, attributed and level — he is quoting the charge, not making it. He reads the two names evenly and makes the challenge plainly, never hardening into accusation. The host (in a level tone): "Then the case against you, the way Rome would put it: Egypt stayed free because you sold it, one Roman at a time." The host (in an even tone): "Seezer, then Antonee." He tips his head slightly toward the right of the frame, where the person opposite him sits, the hand staying on his shin. The host (in a firm tone): "Answer that." His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then the case against you, the way Rome would put it: Egypt stayed free because you sold it, one Roman at a time. Caesar, then Antony. Answer that.
**provenance:** `[I]` Inferred — the Augustan account, put as Rome's case.
**edit_placement:** on picture to *"the way Rome would put it:"*, then `P1_119` from *"Egypt stayed free"* — the charge plays on her face.
**SFX:** studio room tone only.
**screen:** G 8.2 · H 2.8 · 2UP 0.0 · BROLL 0.0

**P1_119** · REACTION · GUEST · **10s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **80 cr**
`start_frame` `frame_cleopatra_i` · `end_frame` `frame_cleopatra_i` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays square in the chair, turned a little toward the left of the frame, both arms along the armrests. She lets him finish; her chin lifts a fraction and she holds his gaze.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_118` from *"Egypt stayed free"* to its end, then holds a beat. `P1_120` chains from this clip.
**Subtitle:** —
**screen:** G 1.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_120** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_cleopatra_i` · 29 syllables · needs 9.7s (duration model v4)

*Starts from the seed frame that `P1_119` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, plain, then asserting on the second sentence. Her voice stays low and never rises. The woman (in a firm tone): "Egypt had grain, gold, and no army that could stop Rome. So I made myself the one thing each of them could not do without." On "the one thing" the fingers of her near hand spread over the end of the armrest and rest. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Egypt had grain, gold, and no army that could stop Rome. So I made myself the one thing each of them could not do without.
**provenance:** `[I]` Inferred — Suetonius, *Julius* 54; Plutarch, *Life of Antony* 56.
**edit_placement:** `SPLIT` A — her thesis needs 15.0 s whole, at the cap; split where the weight comes on. Seam into `P1_121`: `PUNCH` exactly on the seam (Mode 4 §2, fix b), held to the end of `P1_121`.
**SFX:** studio room tone only.
**screen:** G 8.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_121** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `chain from P1_120` · 26 syllables · needs 8.0s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman puts weight on the first sentence; the last is quieter — an admission, not a plea. Her voice stays low and never rises. The woman (in a quiet, serious tone): "Rome calls that seduction. It is what a kingdom without an army does, if it wants to stay a kingdom." On "Rome calls that seduction" her chin lifts a fraction. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Rome calls that seduction. It is what a kingdom without an army does, if it wants to stay a kingdom.
**provenance:** `[I]` Inferred — Suetonius, *Julius* 54; Plutarch, *Life of Antony* 56.
**edit_placement:** `SPLIT` B, and `CUT-IN:hold` A — `P1_122` sits under her at *"Rome calls that seduction"*, ~3 dB down; she does not stop. **Stay on her**; punch-in at *"Rome calls that seduction"*, held to the end. Her thesis — key line 4 (thumbnail and reels, no pull-quote).
**SFX:** studio room tone only.
**screen:** G 7.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_122** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **24 cr** · audio only — picture never used
`start_frame` `frame_host_b` · 7 syllables · needs 2.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host starts to come in over her, firm but not loud, as though he has an objection ready. His tone stays level and never becomes a raised voice. The host (in a firm tone): "But that's not how Rome told it." On "But" he leans in a fraction further, hands staying clasped between his knees. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** But that's—
**provenance:** `[V]` Voice — an attempt, not a claim; only "But that's" is heard.
**edit_placement:** audio only, under `P1_121` at *"Rome calls that seduction"* — the failed attempt of a `CUT-IN:hold`. **Cut the audio after "But that's"**; she carries on over it. Picture discarded.
**SFX:** studio room tone only.
**screen:** G 0.5 · H 0.0 · 2UP 0.0 · BROLL 0.0

The outline gives the heard words, *"But that's—"*. The run-on words are generated only so the model is never asked to stop mid-sentence (Mode 4 §8b); they are never heard and carry no claim.

**P1_123** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_f` · 3 syllables · needs 1.9s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host, quietly — conceding the point plainly. The host (quietly): "And it held." He stays easy in the chair, one arm over the front of the armrest, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** And it held.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.
**screen:** G 0.0 · H 0.7 · 2UP 0.0 · BROLL 0.0

**P1_124** · INTERJECTION · GUEST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_cleopatra_e` · 4 syllables · needs 2.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, even. Nothing added. The woman (in an even tone): "For twenty years." She stays settled back, hands loosely clasped in her lap, chin a fraction high, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** For twenty years.
**provenance:** `[I]` Inferred — her reign, 51–31 BC.
**SFX:** studio room tone only.
**screen:** G 0.9 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_125** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_host_d` · 10 syllables · needs 5.5s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host turns it, then asks plainly. His voice lifts at the end; never accusing. He lowers the hand from his jaw and rests it on the armrest, where it stays. The host (in a calm tone): "Until the war." He settles back a fraction, the lowered hand resting on the armrest. The host (in a plain, curious tone): "How much of it was yours?" His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Until the war. How much of it was yours?
**provenance:** `[V]` Voice
**edit_placement:** on picture for *"Until the war."*, then `P1_126` for the question.
**SFX:** studio room tone only.
**screen:** G 1.4 · H 0.9 · 2UP 0.0 · BROLL 0.0

**P1_126** · REACTION · GUEST · **3s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **24 cr**
`start_frame` `frame_cleopatra_b` · `end_frame` `frame_cleopatra_b` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap. Her gaze stays on him; nothing moves.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_125` from *"How much of it was yours?"*. `P1_127` chains from this clip.
**Subtitle:** —
**screen:** G 0.3 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_127** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_b` · 23 syllables · needs 7.8s (duration model v4)

*Starts from the seed frame that `P1_126` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, exact on the numbers, then dry. She does not stress them. The woman (in a precise tone): "Two hundred of Antonee's ships, and twenty thousand talents." Her folded hands loosen slightly and rest. The woman (in a dry tone): "I paid for a good part of it." Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Two hundred of Antony's ships, and twenty thousand talents. I paid for a good part of it.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 56.
**SFX:** studio room tone only.
**screen:** G 6.6 · H 0.0 · 2UP 0.0 · BROLL 0.0

### Close

**P1_128** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host_e` · 28 syllables · needs 10.8s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host sets the scene slowly and evenly — no drama in the voice. The host (in a calm tone): "Actium. Thirty-one BC. The middle of the battle, and your sixty ships raise their sails and go straight through the fighting." He stays settled back, hands clasped in his lap, and holds her gaze to the end. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Actium. Thirty-one BC. The middle of the battle, and your sixty ships raise their sails and go straight through the fighting.
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 64–66.
**edit_placement:** `SPLIT` A — the whole line needs 15 s under duration model v3, at the cap. **Context card 09** (Actium) enters on *"Actium"*, over him. `P1_130` covers from *"and your sixty ships"* across the seam into `P1_129` (Mode 4 §2, fix a). `MUSIC_Drone_High` peaks under the b-roll.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 4.3 · 2UP 0.0 · BROLL 3.5

**P1_129** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **48 cr** · audio only — picture never used
`start_frame` `chain from P1_128` · 14 syllables · needs 5.3s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host asks the question plainly — no drama in the voice, and never an accusation. The host (in a plain tone): "Antonee leaves his fleet and follows you. Did you run?" On "Did you run" he leans in a fraction. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Antony leaves his fleet and follows you. Did you run?
**provenance:** `[D]` Documented — Plutarch, *Life of Antony* 64–66.
**edit_placement:** `SPLIT` B — `P1_130` runs on over *"Antony leaves his fleet and follows you"*; `P1_131` covers *"Did you run?"* and the silence after — the question plays on her face.
**SFX:** studio room tone only.
**screen:** G 0.7 · H 0.0 · 2UP 0.0 · BROLL 2.6

**P1_130** · BROLL_GEN · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr** + 3 cr still

> Sixty ships raising sail through the battle line, seen from the water.

**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 The battle of Actium, 31 BC, seen from low on the water: a line of ancient oared war galleys — long low hulls, banks of oars, a bronze ram at the waterline, one mast each — hoisting single square sails and pulling away through a gap between other galleys locked together in the middle distance; smoke from burning ships drifting low across the water. No faces. No cannon or gun smoke, no tall sterns or towering hulls, no ships with more than one mast, no rigging of later sailing ships.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera drifts slowly to the left, following the ships.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The sails rise and fill; the ships pull away through the gap; smoke drifts across the water.

 Audio: ambience only — wind, oars and water, distant shouting, low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers `P1_128` from *"and your sixty ships"* to `P1_129`'s *"follows you"* — it also hides the split seam; context card 09 rides over its start.
**Subtitle:** — (the covered line's subtitle continues)
**SFX:** its own generated ambience, ducked under the dialogue it covers.
**screen:** G 0.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**added in Mode 4.** The outline names *"sixty ships through the line"* as Act D's image but marks no `BROLL`; this is that picture. Seen from the water, never from above (the aerial-subject failure).

**P1_131** · REACTION · GUEST · **4s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_cleopatra` · `end_frame` `frame_cleopatra` — **the same seed frame** (Standard's end-frame slot); the next clip starts from it

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She stays upright, back against the chair, hands resting together in her lap. She holds his eyes; nothing else moves.

Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**edit_placement:** covers `P1_129` from *"Did you run?"* to its end, then holds the silence. `P1_132` chains from this clip.
**Subtitle:** —
**screen:** G 2.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_132** · INTERVIEW · GUEST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**
`start_frame` `frame_cleopatra` · 17 syllables · needs 5.2s (duration model v4)

*Starts from the seed frame that `P1_131` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The woman, level. It opens more than it closes — no defence in it, and no appeal. The woman (in a level tone): "Everyone who wrote that battle down was watching from the other side." She stays upright, hands resting together in her lap, her gaze on him. Her eyes stay on the person sitting opposite her, off frame to the left, from the first word to the last.

Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Everyone who wrote that battle down was watching from the other side.
**provenance:** `[I]` Inferred
**SFX:** studio room tone only.
**screen:** G 4.0 · H 0.0 · 2UP 0.0 · BROLL 0.0

**P1_133** · INTERVIEW · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_b` · 8 syllables · needs 3.1s (duration model v4)

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

Only one person is in the frame. The host hands it to her, quiet and warm, speaking to her rather than to the audience. The host (quietly, in a warm tone): "Then next time, you tell it from yours." On "you tell it" his clasped hands loosen a little and stay loosely together; he stays leaning in. His eyes stay on the person sitting opposite him, off frame to the right, from the first word to the last.

Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.

Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.
```

**Subtitle:** Then next time, you tell it from yours.
**provenance:** `[V]` Voice
**edit_placement:** the hand-off; nothing after it but the close. No goodbye.
**SFX:** studio room tone only.
**screen:** G 0.0 · H 1.9 · 2UP 0.0 · BROLL 0.0

**P1_134** · BUMPER_OUT · **5s transform, then held** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr** + 3 cr still

`BRAND_bumper_out` — the studio two-shot turns into a charcoal drawing of itself on camera. The only place the two-shot appears. Format tested and approved (`SERIES_FURNITURE.md`).

**STEP 1 — the outro wide** (Seedream, three reference images, in this order): 1 `Fixed_Assets/cam3_wide.png` (the empty studio) · 2 `Start_Frames/Host/frame_host_b.png` (his last clip's pose) · 3 `Start_Frames/Cleopatra/frame_cleopatra.png` (her last clip's pose). Make 3–4, keep the best, save as `Start_Frames/Cleopatra/frame_wide_cleopatra_outro.png`. **No character sheet** — the pose frames gave the better likeness (tested 2026-09-28).

```
Keep image 1 exactly as it is — the same room, the same two armchairs at exactly the same size and position, the same table, microphones, lamp, shelves, blank panel, framing, lens, lighting, colour grade and film grain. Seat the man from image 2 in the armchair on the left and the woman from image 3 in the armchair on the right, each exactly as they appear in their own image: same face, hair, clothing and posture. He is leaning forward slightly, elbows on his thighs, hands loosely clasped between his knees, looking at her. She is upright and composed, back against the chair, hands resting in her lap, looking at him. Both are life-size adults sitting deep in the armchairs: the chairs stay the size they are in image 1, their seated bodies fill the seats the way real people do, their hips at the back of the seat, the chair backs rising to their shoulder blades. Neither person is enlarged. The camera does not move closer. Only these two people are in the room. Photorealistic still, 16:9.
```

**STEP 2 — the mark:** Claude runs `python3 Fixed_Assets/tools/outro_mark.py Start_Frames/Cleopatra/frame_wide_cleopatra_outro.png` → `…_outro_marked.png` (fixed panel coordinates; stops if the framing moved).

**STEP 3 — the charcoal end frame:** Kling Image 3.0, 2K, 16:9, image-to-image from the marked wide — save as `…_outro_charcoal.png`:

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Keep the composition, the framing and both figures exactly as they are in the source image — same positions, same postures, same scale, same size in frame.
```

**STEP 4 — the transformation** → `Shots/P1_134.mp4`: start = the marked wide, end = the charcoal still, **5 s, Kling 3.0 Standard, audio off, chip off**. Camera paragraph first; no lighting paragraph (the look is meant to change):

```
Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.

The photographed room becomes a charcoal drawing of itself. The change begins at the edges of the frame and moves inward, so the two figures are the last thing to turn. Colour drains away to the warm grey of toned paper; shadows deepen into smudged charcoal and the paper grain rises through the whole image. Both people stay exactly where they are, at the same scale and in the same posture, through the whole change. Nobody moves, enters or leaves.

Audio: quiet room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**STEP 5 — hold** the last frame ~3 s, clean, then cross-dissolve to `BRAND_endcard_p1.mp4`.

**edit_placement:** the close, straight after the host's hand-off in `P1_133`. `MUSIC_Outro_Bed` already running before the transformation begins; it decays, it does not resolve.
**Subtitle:** —
**SFX:** room tone under the music.

## 6 · Assembly

Done here (Mode 4 §9b), not handed off. Drop each clip into `Episodes/Cleopatra/shots/` named exactly by its id (`P1_014.mp4`); the filename is the only link to its row.

1. **Voice pass first** on all talking clips, before trimming; keep the raw Kling clips beside the converted ones.
2. **Strip 1152 samples from the head of every converted clip and loudness-normalise it** — ElevenLabs' MP3 carries one granule (26.1 ms) of head padding; the pass returns ~10 LUFS low. Both are measured properties of the pass, not per-clip judgements:
   ```bash
   ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
   ```
3. Probe every clip: duration, `silencedetect` at −38 dB for speech in/out, the noise floor.
4. Trim heads and tails **in silence**, never mid-phoneme. Close gaps to ~0.3 s inside an utterance, more at a genuine turn. A pause over ~1.2 s that is not a written `BEAT` is trimmed and hidden (punch, reaction, card or b-roll).
5. Lay reactions, b-roll and two-ups at the points their `edit_placement` names; J-cut speaker changes (the incoming voice leads the picture by a few frames).
6. **Level every chained join** with the per-clip gain in `shots/_measure/JOIN_GRADES.md` (`chain_frames.py` writes it after Pass 2). Normalise each b-roll clip against its own first frame (b-roll warms and darkens across a clip).
7. **`ROOMTONE_studio` under the entire part**, constant, never ducking — the voice pass strips the studio floor out of every clip.
8. Subtitles from the **Subtitle** fields; on-screen source credits on `[D]` lines only (a context card's source line *is* the credit when both would show at once).
9. **Finish twice:** a clean master (no text of any kind — Mode 5 cuts reels from it) and the titled master that is published.

What assembly cannot judge is a performance. If a take is clean and the read is wrong, the line goes back to `OUTLINE.md`, never rewritten here.

## 7 · Primary sources

- Plutarch, *Life of Antony* — the principal narrative (Tarsus, the Donations, the will, Actium), written over a century later from hostile Augustan material; used for events, not motive.
- Plutarch, *Life of Caesar* (the bedding sack, the ring, the fire, the Ides) and *Life of Crassus* (the attempt to annex Egypt, 65 BC).
- Caesar, *Civil War*, Book 3 — the contemporary Roman account of Pompey's death and Caesar in Alexandria.
- Cassius Dio, *Roman History*, Books 42–50 — the siege, Arsinoe proclaimed and led in triumph, Cleopatra in Rome, the war declared on her.
- Suetonius, *Julius* (the six thousand talents; Caesarion) and *Augustus*.
- Appian, *Civil Wars* 5.9, and Josephus, *Jewish Antiquities* 15.89 — Arsinoe's death at Ephesus.
- Horace, *Odes* 1.37 — the "fatal monster", written soon after her death.
- Modern: Duane Roller, *Cleopatra: A Biography*.

No verbatim quotation of Cleopatra survives. Her lines are reconstructed from documented actions and the sources above; `[I]` lines are her reading, and say so in their tags.

**Corrections the part makes on purpose** (named in the description, §9): the carpet (`P1_041`, a bedding sack per Plutarch), the Library (`P1_052`, books burned by the docks, scale disputed), and Tarsus as seduction (`P1_078`, a summons to answer a charge).

## 8 · Trust disclaimer

**On screen** — the first four seconds of `BRAND_opening` (`P1_001`), fixed wording, byte-identical in every episode: *AI-GENERATED DRAMATIZATION / Historical reconstruction, not a recording. / A conversation I wanted to hear.* The host does not say it aloud.

**In the description and on the end card** — the full statement:

> This programme is an AI-voiced dramatization. The guest is a historical reconstruction, not a recording. Dialogue is built from documented actions, primary sources, and academic consensus.

Studio's **Altered or synthetic content → Yes**, every part. Short version for reels: *"AI dramatization. Historical reconstruction, not a recording."* The on-screen guest is a direct AI portrayal built from coin portraiture and period evidence, not the cinematic image (`CAST.md`).

## 9 · YouTube metadata

**Titles** (Test & Compare set — the first is the primary)
1. Cleopatra: "They Wrote About My Bed" [Part 1 of 2]
2. Why Rome Declared War on Cleopatra, Not Antony [Part 1 of 2]
3. Cleopatra Answers for Caesar and Antony [Part 1 of 2]

**Description hook.** Rome declared war on Cleopatra, not on the Roman beside her — and the winners wrote her story. In Part 1, Cleopatra VII answers the charge that she seduced Rome.

**Summary.** Cleopatra VII sits down with History Answers Back to answer the word Rome gave her: seductress. In Part 1 of 2 she takes the charge apart from the beginning. Her family were Macedonian Greeks who had ruled Egypt for nearly three hundred years, and she was the first of them to learn Egyptian. Her kingdom was the richest in the Mediterranean and could not defend itself: her father paid Julius Caesar and Pompey nearly six thousand talents to be recognised as king. She tells how Pompey was killed on the shore at Pelusium and his head handed to Caesar; how she reached Caesar in Alexandria carried in a bedding sack, not rolled in a carpet; the siege of the palace quarter and the fire by the docks; her sister Arsinoe paraded in chains in Caesar's triumph; and Caesarion, the son she named Caesar. With Mark Antony the story moves from Tarsus, where she was summoned to answer a charge and arrived as Aphrodite, to the Donations of Alexandria, where Antony gave her children kingdoms Rome saw as its own. She answers for her sister's death, asked of Antony while Arsinoe was a suppliant in the temple of Artemis at Ephesus. Then Octavian takes Antony's will from the Vestal Virgins, reads it to the Senate, and Rome declares war on her, not on him. The part ends in 31 BC at the Battle of Actium, with the question the record leaves open: did she run? Every claim is tagged to Plutarch, Cassius Dio, Caesar, Suetonius, Appian, Josephus and Horace; her lines are a reconstruction.

**Heard vs the record.**
- *Heard:* she was smuggled to Caesar rolled in a carpet. *Record:* Plutarch says a bedding sack tied with a cord; the carpet came later. (`P1_041`)
- *Heard:* Caesar burned the Library of Alexandria. *Record:* the fire of 48 BC reached books by the docks; how many, and whether the Library itself, is still argued. (`P1_052`)
- *Heard:* Tarsus was the great seduction. *Record:* Antony summoned her to answer a charge of funding his enemy; she turned the hearing into a state visit. (`P1_078`)

**Tags.** Cleopatra, Cleopatra VII, Kleopatra, Julius Caesar, Mark Antony, Octavian, Ptolemaic Egypt, Arsinoe IV, Donations of Alexandria, Battle of Actium, ancient Egypt, Roman Republic, historical interview, history podcast, AI history

**Hashtags.** #Cleopatra #AncientRome #History

**Pinned comment.** She says "seductress" is what Rome calls a kingdom without an army staying alive. Statecraft or surrender — where do you land, and why?

**Playlists.** History Answers Back — the series playlist; Cleopatra — both parts in order.

**End screen.** Cleopatra, Part 2 of 2, and subscribe.

**Series index:** `[Part 1 of 2]`

⚠️ The quote in title 1 is her line in `P1_008`, verbatim. The primary title names the guest in its first word. `publish_sheet.py --words-only` checks both, and the three angles differ (quote / charge / event).

## 10 · Soundscape

**Dry by default.** Voice and `ROOMTONE_studio` carry the part; music sits at structural points only.

| Cue | Where |
|---|---|
| `ROOMTONE_studio` | under the whole part, constant, never ducking |
| `MUSIC_Theme_Main` | inside `BRAND_opening` and both `BRAND_actbreak` files — nothing to place |
| `MUSIC_Drone_Low` | enters under `P1_030` (Pompey killed, the head handed over), out across `P1_034` — the darkest passage of Acts A–C |
| `MUSIC_Drone_High` | enters under `P1_106` (the will), rises through the war and peaks under `P1_130` (the sixty ships), out on `P1_132`'s last word |
| `MUSIC_Outro_Bed` | already running before `P1_134`'s transformation; decays under the drawing and the end card |
| `SFX_plate` | one soft paper settle on every lower-third, pull-quote and context-card entrance; exits are silent |

**Everywhere else is dry — including the Arsinoe crack (`P1_082`–`P1_088`).** The two-up and the silence carry it; a bed there would tell the viewer what to feel. B-roll arrives with its own ambience, ducked under any dialogue it covers. No movement foley.

## 11 · Packaging

**Chapter titles** — Mode 6 fills the timecodes into `P1_TIMECODES.txt` from the cut.

| chapter | starts at |
|---|---|
| Seductress, or a verdict? | `0:00` — the opening |
| A kingdom that paid to exist | `P1_007` |
| Carried in to Caesar | `P1_041` |
| Lover, or policy | `P1_071` |
| A war declared on her | `P1_106` |

**Thumbnail overlay lines** — 3–5 words, all caps, her own words where possible; not the title's words:
1. **"THEY CAME FOR MY TREASURY"** — the other half of the title's quote; the two read as one sentence across title and thumbnail without repeating.
2. **ROME DECLARED WAR ON HER** — the charge, for pairing with title 3.
3. **"A KINGDOM WITHOUT AN ARMY"** — her thesis (`P1_121`), for pairing with title 2.

**Thumbnail** — built in Mode 6 from `thumb_portrait_cleopatra.png` by `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`: kicker `CLEOPATRA VII · PART 1`, statement from the list above, output `THUMB_cleopatra_p1.png`. ⚠️ The file of that name in the folder today is the **v1** thumbnail (kept for comparison, `CAST.md`); the rerun's statement is new, so the thumbnail is rebuilt before publishing — `publish_sheet.py` would otherwise find the old file and pass.

## 12 · On-screen text

Placed here, rendered by `build_episode_cards.py`, never invented at the edit. One piece of text on screen at a time.

### Lower thirds — two, that is all

| | Opens over | Reads |
|---|---|---|
| Host | `P1_007` — his first cross-shot question | SALAH ALMAADAWY / *History Answers Back* |
| Guest | `P1_005` — her first appearance, the reaction as he names her | CLEOPATRA VII / *Last queen of Ptolemaic Egypt · 51–30 BC* |

Not over the hook or the direct address (frontal — no side to enter from). The host's welcome plays mostly on her face, so his banner waits for his first question.

### Key lines — three pull-quotes, and a fourth line for thumbnail and reels

| Line | Said in | Pull-quote lands over |
|---|---|---|
| "They came for my treasury. They wrote about my bed." | `P1_008` | `P1_010` — her held face, after the line |
| "Rome does not thank you. It judges you." | `P1_033` | `P1_035` — her held face, after the line |
| "A queen does not arrive at a trial as the accused." | `P1_078` | `P1_080` — her held face, after the line |

Key line 4, **no pull-quote** (no silent beat follows it, and her thesis should not be interrupted by a card): *"Rome calls that seduction. It is what a kingdom without an army does, if it wants to stay a kingdom."* (`P1_121`) — for the thumbnail and Mode 5.
⚠️ Pull-quote 01 is also the hook's first option. **If Mode 6 keeps it as the hook, drop `BRAND_pullquote_01`** — the same sentence three times is wallpaper.

### Context cards — who, where, what, on first mention

Opposite the speaker, upper band, 5.5 s, entering **as the word is said**: `L` when she speaks, `R` when he speaks. Glosses are Mode 3's, sourced like `[D]` lines. **A card never rides onto the other person's face** — each placement below was checked against the rows around it, and three cards moved from the host's mention to hers a second later for that reason (03, 07) or got a cover (05, 06, 08).

| # | Lands on | Word | Side | Label | Name | Gloss | Source |
|---|---|---|---|---|---|---|---|
| 01 | `P1_015` | My family | L | WHAT | THE PTOLEMIES | Macedonian Greek dynasty founded by Alexander's general Ptolemy; ruled Egypt 305–30 BC. | Roller, *Cleopatra* |
| 02 | `P1_022` | talents | L | WHAT | TALENT | Greek unit of weight: about 26 kg of silver. Six thousand is about 155 tonnes. | Suetonius, *Julius* 54; Britannica, "Attic talent" |
| 03 | `P1_030` | Pompey | L | WHO | POMPEY | Roman general, Caesar's great rival in the civil war of 49–48 BC. | Caesar, *Civil War* 3 |
| 04 | `P1_055` | Arsinoe | L | WHO | ARSINOE IV | Cleopatra's sister, proclaimed queen against her in Alexandria in 48 BC. | Cassius Dio 42.39 |
| 05 | `P1_071` | Tarsus | R | WHERE | TARSUS | City in Cilicia, southern Asia Minor, where Antony summoned Cleopatra in 41 BC. | Plutarch, *Antony* 25–26; Roller |
| 06 | `P1_096` | thrones | R | WHAT | DONATIONS OF ALEXANDRIA | 34 BC ceremony: Antony proclaimed Cleopatra and her children rulers of eastern kingdoms. | Plutarch, *Antony* 54 |
| 07 | `P1_104` | Octavian | L | WHO | OCTAVIAN | Julius Caesar's adopted heir and Antony's rival; later Augustus, Rome's first emperor. | Suetonius, *Augustus* |
| 08 | `P1_106` | Vestal | R | WHAT | THE VESTAL VIRGINS | Priestesses of Vesta in Rome, who held Antony's will in trust. | Plutarch, *Antony* 58 |
| 09 | `P1_128` | Actium | R | WHERE | ACTIUM | Promontory in western Greece; the sea battle off it in 31 BC decided the war. | Plutarch, *Antony* 62–66 |

**How each clears a face:** 01, 02, 03, 04, 07 sit over her own long line (≥ 5.5 s of it left after the word; 04 rides on over `P1_056`). 05 holds over the host through `P1_072`, a chained reaction covering her first sentence. 06 and 08 ride over b-roll (`P1_097`, `P1_107`), which cuts back to her only after the card has gone. 09 sits over him and runs on over `P1_130`. None overlaps a lower third or a pull-quote.

## 13 · Still outstanding for Part 1

- **The test batch** (§4b) — six questions; T4 has no qualifying line here and stays open.
- **The hook** — first option only; re-picked by Mode 6 from the finished part.
- **The thumbnail** — rebuild with the new statement (§11) before publishing.
- **`publish_defaults.json`** still has the series playlist as `TODO` — blocks the publish sheet, not generation.
- **ElevenLabs** on the paid tier for every published clip (free-tier output cannot be relicensed).
- **Credits** — record the actual Part 1 spend, retakes included (NEXT_STEPS A5).
