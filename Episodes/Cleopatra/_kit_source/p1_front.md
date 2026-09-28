# Cleopatra — Part 1 · Production Kit
*Mode 4 output, B5 rerun, 2026-09-23. Built from `Episodes/Cleopatra/OUTLINE.md` (words approved in `SCRIPT_READ.md`, 2026-09-23) and `CAST.md`, by `_kit_source/build_p1_kit.py`. **No spoken word differs from the outline.** Ids are contiguous (a fresh kit); from here on, an inserted row takes the previous id plus a letter.*

`part` 1 of 2 · guest `@guest_cleopatra` (Reconstructable tier, named figure — no composite card) · host fixed.

**Anchor images** (all checked on disk 2026-09-23; seed frames viewed, montage in `_kit_source/grounding_*.jpg`):
- Host seed frames — `Start_Frames/Host/frame_host.png`, `_b`, `_c`, `_d`, `_e`, `_f`, `_h`, `_i`; direct address `Start_Frames/Host/frame_host_direct.png`, `_b`, `_c`.
- Guest seed frames — `Start_Frames/Cleopatra/frame_cleopatra.png`, `_b`, `_c`, `_e`, `_i` (and `_f`, `_g`, `_h`, made for Part 2); `_d` retired 2026-09-28 (L56).
- Close — the per-part outro wide `Start_Frames/Cleopatra/frame_wide_cleopatra_outro_marked.png` (built from three references, L59; start frame of `BRAND_bumper_out`).
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
| Camera | **chip / preset OFF** — prompt structure v3 (`LOCK` camera paragraph first, `CONT` lighting paragraph last) holds the camera by itself (L51). b-roll moves by its own prompt |
| Every Kling preset | none used (they are prompt text describing what the seed frame already fixes) |
| Prompt enhancer | not available on Turbo; gesture paragraphs stand as written |
| End-frame slot | Turbo has none. **Every silent reaction** (Standard) has its start image in the end slot too (L44) |
| Voice | ElevenLabs speech-to-speech on every talking clip, paid tier |
| Paste | **from this file or the round sheet, never from chat.** One unbroken line per paragraph; studio prompts have no leading spaces (v3, L51) |
| Route | the Kling CLI in waves (`cli_wave.py` → `kling_run.mjs`; b-roll `kling_broll.mjs`), the website as fallback (Mode 4, *Generating*) |

Record any exposed creativity / cfg value the first time it is seen, and keep it for the whole part.

## 2 · Totals

| Category | Clips | Seconds | Rate | Credits |
|---|---|---|---|---|
| Talking (`INTERVIEW` / `INTERJECTION` / `NARRATION`) | {{TALK_N}} | {{TALK_S}} ({{TALK_MS}}) | 10 (8 at 720p for the audio-only clips) | **{{TALK_CR}}** |
| Reactions, silent | {{REACT_N}} | {{REACT_S}} | 8 | {{REACT_CR}} |
| B-roll, generated | {{BROLL_N}} | {{BROLL_S}} | 10 | {{BROLL_CR}} |
| B-roll stills | {{BROLL_N}} | — | — | {{STILLS_CR}} |
| `BRAND_bumper_out` | 1 | 5 + held | 8 | 43 |
| **Total** | **{{GEN_N}} clips + {{BROLL_N}} stills** | **{{GEN_S}}** | | **~{{TOTAL_CR}}** |
| `BRAND_opening`, `BRAND_actbreak` ×2 | fixed | 19.17 + 10 | — | 0 |

{{OFFMIC_N}} talking clips ({{OFFMIC_S}} s) are off-mic — generated, heard, picture discarded. Reactions and b-roll lie over the spine; they add generations, not runtime (except the `BEAT`s and the act breaks). Expected finished length ≈ **10–10½ minutes** with the opening, breaks and close — the outline's read timed the words at ≈ 9:50 (`SCRIPT_READ.md`); the duration model's lead-ins and tails are trimmed in the edit.

**Budget the reruns:** about one retry in six on talking clips (~{{RETRY_CR}} cr), so plan on **~{{PLAN_CR}} credits** for Part 1 — and record the actual figure (NEXT_STEPS A5 is waiting for it).

**Cold-open timing:** first guest word at **~4 s** (the hook), guest on screen in the studio at **~{{GUEST_ON}} s** — under the 40 s ceiling (Mode 4 §0).

## 2b · Screen share — the guest carries the picture

Series rule since 2026-09-24 (Mode 4 §8b): his questions play on her listening, his reactions during her lines are two-ups, at most two full-frame host reactions. Summed from every row's `screen:` line; `screen_share.py` is the gate.

{{SHARE_TABLE}}

## 3 · Start frames used

Host: {{HOST_POSES}}. Guest: {{GUEST_POSES}}. Chosen per beat from the two pose registers (`STUDIO_ASSETS.md`, `CAST.md`); no character repeats a variant within three of their on-screen appearances (checked by the builder). Chained clips inherit the pose of the clip they continue. Every gesture sentence describes the frame as it actually is — a prompt that contradicts its start frame asks the model to move the body into the described pose.

## 4 · Generation order

0. **The test batch (§4b)** — {{TEST_IDS}}. First, before any other spend, because each one tests a technique this kit relies on. They are normal kit rows: a clip that passes is kept.
1. **Every clip, from one sheet** — `python3 Fixed_Assets/tools/round_sheet.py Episodes/Cleopatra 1 --part 1` → `ROUND1_prompts.md`, in kit order, each chained clip directly under its source; made in CLI waves (`cli_wave.py`, which extracts chained start frames itself) with the website as fallback. Clips already kept in `Shots/` are skipped automatically. *(Part 1: every clip made by 2026-09-27.)*
   **Duration calibration:** Cleopatra's rate (4.3 syl/s) is measured and on file (`CAST.md`) and the host's carries over, so no separate calibration round — but measure the first three talking clips of Pass 1 (onset, rate, pause per break) and stop if either voice is more than ~10% off.
2. **The cut-in frame** — time the cut word in `[[B4]]` and write it into `[[B5]]`'s row (`chain from [[B4]] at 6.42s` form).
3. **Measure the joins** — `python3 Fixed_Assets/tools/chain_frames.py Episodes/Cleopatra 1` → `Shots/_measure/JOIN_GRADES.md` for the edit.
4. **Voice pass** (ElevenLabs, {{VOICE_N}} talking clips; never reactions or b-roll), then **assembly** (§6), then Mode 6.
5. **`BRAND_bumper_out` last** — the outro wide (Seedream, three references), the mark, the charcoal still, then the 5 s transformation (its row carries all the steps).

### Chain table

| chained shot | starts from the last frame of | source type | start frame file |
|---|---|---|---|
{{CHAIN_TABLE}}

Chain sources: {{CHAIN_SOURCES}}. Chained: {{CHAINED}} — each made right after its source is kept, from the source's last frame (Kling's last-frame feature on the website, or `cli_wave.py`'s extraction); colour is matched in the edit (`JOIN_GRADES.md`).
No chain is deeper than three links (the longest is the Arsinoe `SPLIT`: two-up reaction → A → B). An `OFFMIC` row never appears in picture, so it neither breaks nor needs a chain.

## 4b · The test batch (Mode 4 §0c) — Part 1 of a new run, before Pass 1

Picked from this kit by the criteria, not from old shot ids. **~{{TEST_CR}} cr**, all of it normal kit rows.

| # | question | shot(s) | why it qualifies | how to judge |
|---|---|---|---|---|
| T1 | Does a `Pronunciation:` paragraph make Kling say a rare name right? | `[[A5]]` | — | **✅ settled 2026-09-24:** the paragraph was read aloud (*"Medes"* twice); respelling inside the quote (*"Meeds"*) was right. Rule in Mode 4 §3 3b. `[[A5]]` is regenerated at 9 s in Pass 1 (the 8 s take ran to its last frame) |
| T2 | Does a **beat map** give each sentence its own temperature, with no extra pauses and no note read aloud? | `[[LA9]]` → `[[A10]]` | — | **✅ settled 2026-09-24:** each sentence got its own delivery, nothing read aloud (Salah, as a viewer). It took 1.6 s and 1.0 s between segments and ran to the last frame → duration model v3 (1.0 s per break). Beat maps are now the default wherever the outline gives one delivery per sentence. `[[A10]]` is regenerated at its v3 length |
| T3 | Does a `SPLIT` read as one continuous line? And does lip-sync drift after ~5 s in a whole take? | `[[C13]]` + `[[C14]]` | the outline's `SPLIT`, a mood turn at a sentence, a `PUNCH` to hide the seam | **✅ settled 2026-09-24:** cut together in Resolve it reads as one line (Salah); pitch 193 Hz both sides, flat join, only a 6–7 dB loudness step (split level rule). No lip-sync drift in the long beat-map takes, so the control is dropped. Both clips kept |
| T4 | Does a trailing `…` play as a thought let go? | — | **no line in Part 1 uses `…`** | stays open |
| T5 | Does a `CUT-IN` stop read as a real interruption, and does its start frame stay closed-mouthed? | `[[B4]]` → `[[B5]]` → `[[B6]]` | the first `cut` interruption | the stop's mouth closes in the first frames and stays closed; her entry lands on the cut **✅ T5 settled 2026-09-25:** reads as a real interruption (Salah); mouth closes in ~0.4 s; `Shots/_tests/_twoup/CUTIN_T5_test.mp4`. Her 3.2 s silent lead-in is trimmed (audio in 0.3 s before the cut) |
| T6 | Does a two-up hold up in motion — crop, eyelines, the listener clip's length? **Both kinds** (Screen share, 2026-09-24): a host reaction beside her talking, and a shared silence | `[[A2]]` + `[[A2r]]`; `[[C9r]]` → `[[C10]]` → `P1_085` + `[[C12]]` | two-up #1 (his reaction beside her line) and the old #5 (the silence after *"In a sanctuary"*) | build each from the singles (native crop, never scaled); eyelines meet across the divider; his half never looks like a cutaway. **Fail → host reactions fall back to J-cuts, with at most two full frame.** **✅ T6a settled 2026-09-24:** two-up #1 passes (`Shots/_tests/_twoup/TWOUP_01_test.mp4`); `P1_009` regenerated after the nod rule. **❌ T6b failed 2026-09-24:** a two-up with both faces only reacting reads as empty (Salah). **Rule: a two-up always has one person talking; a silence goes on one face, hers.** The old #5 is gone: his *"In a sanctuary"* plays over her face (`[[C12]]`), then ~1 s of silence. `P1_085` is retired (number kept empty so later clips keep their names) |

**Order (Salah, 2026-09-24): one test at a time — T1 ✅, T2 ✅, then T3, T6a, T6b, T5.** Seed-frame clips first (`[[A2]]`, `[[A2r]]`, `[[LA9]]`, `[[B4]]`, `[[B6]]`, `[[C9r]]`, `[[C12]]`), then the chained ones in dependency order (`[[A10]]`, `[[C10]]`, `[[C13]]`; then `[[C14]]`; `[[B5]]` once the cut word is timed).
**Results fold back into the skills:** a pass → mark it `settled <date>` in Mode 4 §0c and remove the hedge from the section it tested; a fail → remove the technique from Modes 3 and 4 and record it in `DECISIONS_ARCHIVE.md`.

**T3 optional control** (~{{T3_CONTROL_DUR}} s, chained from `[[C12]]`, save as `shots/_tests/T3_whole.mp4` — not a kit row, never cut into the part):

```
{{T3_CONTROL}}
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
| `[D]` Documented | attested; the source is named on the line | {{PROV_D}} |
| `[I]` Inferred | consistent with the record; the basis is named | {{PROV_I}} |
| `[V]` Voice | connective tissue; **carries no factual claim** | {{PROV_V}} |

Every `[D]` source was read on 2026-09-23 in Mode 3; no open verification flag exists anywhere in this kit (the gate greps for the word, so it is not written here). A `[V]` line may not contain a factual assertion — host echoes that restate a documented fact carry the fact's tag.
