# Cleopatra — Part 1 · Production Kit
*Mode 4 output. Generated from `Episodes/Cleopatra/CAST.md` and the Part 1 research file.*
*Rebuilt after the kling.ai migration and the test programme. Shots are renumbered; the builder that produces this file lives in `_kit_source/`.*

## 1 · Settings (identical for every clip)

| | |
|---|---|
| Platform | **kling.ai** (official, not a reseller) |
| Model — picture | **chosen per shot type**, see below |
| Model — voice | **ElevenLabs** speech-to-speech, every talking clip, ~$2/part |
| Camera preset | **stationary preset ON**, plus the full `LOCK` paragraph |
| Stills | Seedream 5.0 — ~3 cr via Higgsfield starter, or ~$0.07 on fal |
| Resolution | 1080p |
| Prompt enhancer | **not available on Turbo** — see below |
| End frame slot | **Turbo has none** (found 2026-09-20). Only Standard offers it — silent clips and the draw-ons |

### Model per shot type — measured, and it inverts the old assumption

| Shot type | Model | Rate |
|---|---|---|
| `INTERVIEW`, `NARRATION`, `INTERJECTION` | Kling 3.0 **Turbo** | 10 cr/s |
| `REACTION`, `WIDE_SILENT` | Kling 3.0 **Standard, audio OFF** | **8 cr/s** |
| `BROLL_GEN` | Kling 3.0 **Turbo**, audio on | 10 cr/s |
| `WIDE_CREDITS` | Kling 3.0 **Turbo**, audio on | 10 cr/s |

**For any clip with no dialogue, Standard with audio off is cheaper than Turbo** — 8 against 10. Every row below carries its own model and credit cost.

**Why reactions are not on Turbo.** The first silent-reaction test came back mouthing gibberish. The cause is the native audio track, not weak instruction-following: a face plus an audio channel with no dialogue assigned invites the model to invent speech, and the mouth follows what it is generating. Turbo has no way to switch that off; Standard does. Re-tested on Standard with audio off and it passed — mouth movement measured at mean 1.14 / peak 3.84, against a blink peaking at **9.81**. Breath-shaped, not speech-shaped.

**The camera lock holds, on both models.** Test A ran `P1_054` at 10s on Turbo with the stationary preset and the rewritten `LOCK` paragraph: the frame held. The same check run free on the Standard reaction clip gave first-frame-against-last differences of 1.44 / 1.69 / 1.28 across static regions, with under 0.2% of pixels moving more than 25. No separate camera treatment is needed per model.

⚠️ **Recorded honestly: two things changed at once in Test A** — the preset was applied *and* the `LOCK` paragraph was rewritten. Which one fixed the drift is unknown. It does not matter operationally, since both are always used together; it matters only for portability, if the kit ever moves to a platform with no such preset.

**Voice comes from ElevenLabs, not Kling.** All 66 talking clips go through a speech-to-speech pass against the character's voice ID in `Fixed_Assets/VOICES.md`. Tested: picture and lip-sync survive untouched. Reactions are silent, b-roll has no dialogue, and the wide's audio is discarded, so none of those need it. The voice block stays in each prompt — speech-to-speech maps timbre onto the *source* delivery, so the generated performance still has to be clean and roughly the right register. Process on the paid plan; free-tier output cannot be relicensed.

**A two-speaker clip cannot pass the voice pass.** Speech-to-speech converts a clip to *one* voice, so both characters would come back sounding identical. This is why the wide never carries dialogue and why the closing exchange lives in singles. Structural, not a reliability judgement.

**Turbo has no prompt enhancer, and so far that has cost nothing.** `P1_054` was generated on Turbo with the existing wording and came back with natural hand movement, so the gesture paragraphs stand as written — do not rewrite them on a theory. Losing the enhancer is arguably a gain: the prompt reaching the model is now the prompt we wrote. If an individual clip comes back stiff, `skill_mode4_produce.md` §5 has a repair kit for that clip.

Record any exposed creativity / cfg value the first time you generate, and keep it fixed for the whole part.

## 2 · Totals

| Category | Clips | Seconds | Rate | Credits |
|---|---|---|---|---|
| Talking spine (`INTERVIEW` / `INTERJECTION` / `NARRATION`) | 67 | 576 (9m 36s) | 10 | **5,760** |
| Reactions, silent | 12 | 50 | 8 | 400 |
| B-roll, generated | 12 | 82 | 10 | 820 |
| Closing bumper | 1 | 5 + held | 8 | **43** — `BRAND_bumper_out`, charcoal still + a generated transformation |
| Start frames for b-roll | 12 stills | — | — | ~36 |
| **Total** | **92 generated clips + 13 stills** | **713s** | | **~7,059** |
| `BRAND_opening`, fixed asset | 1 | 19.17 | — | free — card, hook slot and intro in one file |
| `BRAND_actbreak` ×2, fixed asset | 2 | 10 | — | free — `P1_032` and `P1_058` |

**Recalculated 2026-09-21 (duration model v2, six measured clips): spine 9m 36s generated**, of which ~10 s is off-mic audio laid under other shots — the same words as before with the dead air taken out, ~470 credits cheaper. It sits just under the 10–12 minute target *because the pacing tightened, not because content was cut*; reactions, b-roll, the act breaks, the opening and the close bring the finished part to roughly ten and a half minutes. Reactions and b-roll overlay the spine rather than extending it, so the finished part runs a little over eleven minutes once the cold open and credit roll are counted.

Budget the reruns, not just the clips. Assume roughly one retry in six on talking clips — about 1,040 extra credits — so plan on **~8,660 credits** for Part 1.

**This is five times the old figure, and nothing got more expensive.** The previous total of ~1,710 was written for Higgsfield's 2.0 cr/s; kling.ai charges 10 cr/s for the same Turbo model and sells credits at a completely different price. Compare the money, not the credits: at Ultra-tier pricing Part 1 runs about **$46**. Do not carry the old credit numbers forward anywhere.

**Where the +280 credits went.** The five Pexels rows became generated charcoal b-roll (28s at 10 cr/s, plus 15 cr of stills). That buys one coherent visual language, no third-party licence surface, and no search step during writing — for about $1.72 a part.

**Two rows left the budget entirely.** The title beat is now `BRAND_bumper_in` and the close is `BRAND_bumper_out`, both fixed series assets built once and reused in every episode — see `Fixed_Assets/SERIES_FURNITURE.md`. That is ~200 credits a part removed, and it deletes the only two-character generation in the kit. The outro is not fully free — it is one ~3-credit charcoal pass on a still the part already contains — but it buys a better ending than a fixed clip would.

**Every b-roll row is two steps** — a still first, then image-to-video from it — and **every one is charcoal**. The abstract rows used to go straight to text-to-video, but the charcoal style is the thing that must not drift across fifteen clips, and a start frame is what holds it. Fifteen stills at three credits is 45 credits, cheap insurance against the one thing that would make the b-roll look like a different show each time.

**Four b-roll rows carried the armour error.** `P1_013`, `P1_071` and `P1_091` specified *segmented iron armour* — lorica segmentata, Imperial kit from the first century AD, about fifty years after Cleopatra died. All now use the registered `legionary_late_republic` wardrobe block (mail, Montefortino helmets) and drop the reference tag, since passing a reference for anonymous extras produced rows of clone faces. `P1_061` no longer depends on the retired `@antony` sheet: the commander is drawn from behind with his face not visible, so the shot makes no likeness claim and needs no character sheet.

## 3 · Start frames used

Host: `frame_host`, `_b`, `_c`, `_d`, `_e`, plus `frame_host_direct_b` and `_c` for the cold open.
Cleopatra: `frame_cleopatra`, `_b`, `_c`, `_d`, `_e`.
Wide: `frame_wide_cleopatra` (establishing, near the top) and `frame_wide_cleopatra_c` (the close — `CAST.md` designates `_c` for openings and closings).
Extras: **retired.** `@antony` and `@roman_legionary` are no longer character sheets. B-roll is charcoal, which a photoreal sheet cannot drive, and passing a reference for anonymous extras produced roughly twenty clone faces in testing. Identity for crowds now comes from the registered **wardrobe text block** in `STUDIO_ASSETS.md`, pasted byte-identical, with no reference image.

No speaker starts two consecutive turns from the same pose. The apparent repeats are deliberate: the two cold-open direct addresses are continuous, and the chained clips inherit their start frame from the previous clip's end frame.

## 4 · Generation order

1. **Cold open** — `P1_004` to `P1_007`. Confirm the direct-address framing and the voice before committing to anything else. **`P1_004` also tests the start+end frame join into `P1_006`** — check that the last seconds don't rush the line and that Turbo accepted the end frame; if not, fall back to the chain as its row says. (`P1_001` is the built opening and generates nothing; `P1_005` was removed.)
2. **The validated pair** — P1_055 and P1_057. These two are known to work; generating them early confirms nothing has drifted on the platform side. ⚠️ **2026-09-20: `P1_055` was rewritten under the junction rule, so only `P1_057` is still the validated line.** Generate both here anyway; judge `P1_055` as a normal clip.
3. **Act A**, then B, C, D in order, talking clips first.
4. **Reactions** last within each act, once you know the exact tail you need to cover.
5. **B-roll stills** in one batch, then the b-roll videos in a second batch.
6. **The outro, `P1_095`,** last — the charcoal pass on `frame_wide_cleopatra_marked.png`, then the 5s transformation. There is no other wide in the part; the establishing wide was removed on 2026-09-18.

**At the first chained clip, measure before trusting the chain procedure.** Kling extracts the end frame natively and applies it as the next start frame in-app. Both chain procedures in §5 were workarounds for faults introduced by *our own* ffmpeg extraction and by luma measurements taken on a different platform, so they may no longer apply. Compare the mean luma of the source clip's last frame against the new clip's first frame. If they match, drop both procedures and reconsider the three-link cap. If they do not, keep them exactly as written — and note that pre-lifting a frame to correct a loss that is not happening would make each link progressively *brighter*.

### Chain table

| chained shot | starts from | source type | start frame file |
|---|---|---|---|
| `P1_006` | `P1_004` | NARRATION (direct → cross join) | `shots/start_frames/P1_006_start.png` — **done** |
| `P1_007` | `P1_006a` | REACTION (her first appearance) | `shots/start_frames/P1_007_start.png` |
| `P1_015` | `P1_014` | INTERJECTION, same speaker | `shots/start_frames/P1_015_start.png` |
| `P1_028` | `P1_026` | INTERVIEW, same speaker (his `OFFMIC` P1_027 in between) | `shots/start_frames/P1_028_start.png` |
| `P1_042` | `P1_041` | REACTION | `shots/start_frames/P1_042_start.png` |
| `P1_057` | `P1_056` | REACTION | `shots/start_frames/P1_057_start.png` — **done, kept** |
| `P1_065` | `P1_064` | INTERJECTION, same speaker | `shots/start_frames/P1_065_start.png` |
| `P1_068` | `P1_066` | INTERVIEW, same speaker (his `OFFMIC` P1_067 in between) | `shots/start_frames/P1_068_start.png` |
| `P1_074` | `P1_073` | INTERVIEW, same speaker (his silent `P1_073a` in between) | `shots/start_frames/P1_074_start.png` |
| `P1_093` | `P1_092` | REACTION | `shots/start_frames/P1_093_start.png` |

**Pass 1** — every other row, from its seed frame, including the chain sources `P1_006a`, `P1_014`, `P1_026`, `P1_041`, `P1_064`, `P1_066`, `P1_073`, `P1_092`.
**Then** `python3 Fixed_Assets/tools/chain_frames.py Episodes/Cleopatra` extracts all start frames at once (unmodified), and after Pass 2 writes `shots/_measure/JOIN_GRADES.md` — the per-clip grade the edit applies to level each join.
**Pass 2** — `P1_007`, `P1_015`, `P1_028`, `P1_042`, `P1_065`, `P1_068`, `P1_074`, `P1_093`, each started from its source clip's last frame **using Kling's own last-frame feature** (settled 2026-09-21; `_start.png` is the fallback). Rerun the script to measure the joins.
All chains are one link deep. An `OFFMIC` row never appears in picture, so the shots either side of it are adjacent on screen and chain.

### Pronunciation

Added 2026-09-22. Every rare name in a spoken line (`lines_check.py` finds them). Stressed syllable in
capitals. **Not yet in the prompts** — pending the A/B on `P1_024` (Mode 4 §3, block 3b).

| Word | Say it | Lines |
|---|---|---|
| Ptolemaic | tol-uh-MAY-ik | `P1_024` |
| Parthia | PAR-thee-uh | `P1_060`, `P1_066` |
| Octavian | ok-TAY-vee-un | `P1_065`, `P1_069`, `P1_072`, `P1_077` |
| Actium | AK-tee-um | `P1_082` |

## 5 · Reading a row

Each row header carries the shot id, type, duration, **model, rate and credit cost**.

`start_frame` is the still to upload. Everything inside a code block is pasted into the prompt field, whole and unedited. **Subtitle** is the burn-in text. **provenance** is the line's source tag — see below. **edit_placement** on silent rows says what the clip is for, not a timecode; the exact cut is decided at assembly against the real durations. Rows carrying a **changed:** note were altered in this rebuild, and the note says why.

### Provenance tags — what backs every spoken line

| Tag | Meaning | Count |
|---|---|---|
| `[D]` **Documented** | attested in the record; the source is named on the line | 39 |
| `[I]` **Inferred** | consistent with the record, a reasonable reconstruction; the basis is named | 14 |
| `[V]` **Voice** | connective tissue, rapport, phrasing; **carries no factual claim** | 13 |

**A `[V]` line may not contain a factual assertion.** That rule is what makes the published source list honest, and the audit that applied it here moved seven lines out of `[V]` — host echoes like *"They had handed him his enemy's head"* restate a documented fact and are still asserting it.

**§7's source list is generated from these tags**, not assembled beside them: nothing cited that is not used, nothing claimed that is not cited.

~~Two tags carry an explicit **VERIFY** instruction.~~ **Both cleared 2026-09-18** — P1_019 (the kinship term, and the contested will the flag had not noticed) and P1_045 (the four-month siege figure, withdrawn for 'a winter'). Two more flag a deliberate correction of a popular story, P1_042 and P1_047, which the description should name.

### Chained rows

**Batch process — settled 2026-09-20.** Only rows marked `chain from` need an extracted frame; every
other row starts from a seed frame and can be generated at any time. So a part is generated in
**two passes**, never shot by shot:
1. **Pass 1 — everything with a seed frame**, including every chain *source* (in Part 1 those are the
   reactions `P1_041`, `P1_056`, `P1_092`). Drop the clips into `Episodes/<Guest>/shots/` named by id.
2. **Extract all chain frames at once:**
   `python3 Fixed_Assets/tools/chain_frames.py Episodes/<Guest>` → `shots/start_frames/<TARGET>_start.png`,
   named after the shot that **uses** the frame, extracted with the approved ffmpeg command only.
   It lists any source still missing and never overwrites an existing frame.
3. **Pass 2 — the chained shots**, each uploading its `<TARGET>_start.png`.
4. **Run the script again** — with the chained clips present it measures every join (luma and chroma,
   last frame vs first) and flags any that needs checking at the cut.
**Never use the platform's extract-frame button or a screenshot for a chain frame** — that is where the
+7.1% chroma jump at `P1_004` → `P1_006` came from.


Chained rows say `chain from P1_0xx`: take that clip's **end frame** and use it as this clip's start frame. Kling does this natively in-app. The fallback — extract with `ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png`, no scale filter, no range conversion, and lift the frame about 1.5% before uploading — applies only if the native path proves lossy when measured at the first chain. Never exceed three links.

---

## Shot list

### Cold Open

**P1_001** · BRAND_OPENING · **19.17s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_opening.mp4` — one built file, byte-identical in every episode. Full spec in `Fixed_Assets/SERIES_FURNITURE.md`.

**The whole front of the show is one object.** Three beats, one unbroken piece of music, a clock strike opening each:

| time | picture | sound |
|---|---|---|
| **0.00–4.00** | the disclosure card, on paper — `AI-GENERATED DRAMATIZATION` / *Historical reconstruction, not a recording.* / *A conversation I wanted to hear.* | **first strike**, then the theme decays to −47 dB |
| **4.00–8.00** | **the hook slot** — the guest, speaking | **second strike**, punctuating the line |
| **8.00–19.17** | the intro — three charcoal studies draw themselves, the page clears, the mark, the sand falls and runs back up | **third strike**, then the downbeat |

**edit_placement:** opens the video at 0:00. **Lay the hook clip into 4.00–8.00** — an edit-only lift of the guest's strongest sentence from later in the part, her audio only, no host, no added music. The nominated line is **`P1_057`'s third sentence: *"Egypt did not survive without me."*** — chosen 2026-09-21 on the generated take (it was *"You assume those were two things. For me they were one."*, which fills the whole 3.9 s with no room to hold). **Cut points in the measurement take were in 5.6 s / out 9.6 s — re-measure on the regenerated take.** Rendered with `hook_build.py … --face 1365,180,240` as the face emerging from the paper (2026-09-22; demo `DEMO_opening_hook_paper.mp4`) — her voice enters ~0.4 s after the strike, the line runs 6.0–8.1 s, and **1.5 s of live hold** follows on her composed face, mouth closed, before she draws breath for the next sentence at ~9.5 s. If a future take has no clean pause after the line, **freeze the frame on the last closed-mouth frame** for the remainder of the slot instead. The episode repeats the line in context — that second hearing is the payoff. The slot is fixed furniture; the clip is cut to it, never the other way round.
**Subtitle:** the card's wording is burned into the asset. The hook clip keeps its own subtitle.
**SFX:** nothing to add — the music, the three strikes, `SFX_sand` and `SFX_plate` are all inside the file.

**changed 2026-09-18.** This was three rows: a 3s disclosure card, a 5s teaser, and a 4s bumper, in that order. They are now **one 19.17s asset with the teaser inside it**. The card is 4s not 3s, the hook is 4.00s not 5s, and the music runs unbroken from the first frame instead of entering at the bumper. **`P1_002` and `P1_003` are retired and their ids are not reused.**

**P1_004** · NARRATION · HOST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_host_direct_b` · ~~`end_frame` `frame_host_b`~~ **no end frame — Turbo has no slot; chain into `P1_006`** · 35 syllables · needs 11.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, direct to camera, level — he states the charge without endorsing it, and the last line lands as a simple announcement rather than a flourish.

 The host says, level, without endorsing it: "Its last ruler has been called a seductress for two thousand years. Mostly by the men who conquered her. Tonight she answers for herself."

 On the last sentence he lifts one hand slightly from his clasped hands, turns it open, and lets it settle back into the clasp. As he says "Tonight she answers for herself" he turns his head from the lens toward the person sitting opposite, and holds there, looking at her.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Its last ruler has been called a seductress for two thousand years. Mostly by the men who conquered her. Tonight she answers for herself.
**provenance:** `[D]` Documented — Augustan-era hostile characterisation of Cleopatra: Cassius Dio 50; Horace, Odes 1.37; Propertius; Plutarch, Life of Antony.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

⚠️ **The join into `P1_006` — start AND end frame, settled 2026-09-19.**

This is the only direct-address shot in the part and it cuts straight into `P1_006`, the host in
cross-shot. Direct and cross share a camera, a framing and a chair, so a plain cut moves the eyes
and nothing else — a jump cut. **The establishing wide used to sit between them and absorb it**;
removing the wide exposed the join.

**The fix: `P1_006`'s start frame is `P1_004`'s end frame.** Generate `P1_004` with **both** frames
set — start `frame_host_direct_b`, end `frame_host_b` — and the model animates him from the lens to
the guest. `P1_006` then opens on `frame_host_b`, so **the last frame of one clip is the first frame
of the next, exactly.**

**Scope: this join only.** Every other join in the kit keeps the proven chain method unchanged — this is the one case where the cut exists *to* change the eyeline, so it gets its own method.

**Why it is the best of the options, not just a working one:**
- **The two poses are the same body.** Both lean forward, forearms on thighs, hands clasped — only
  the eyeline differs. The model only has to turn a head.
- **Both ends are vetted seed frames.** No extracted frame, so no colour-range conversion and no
  chain luminance loss.
- **No serial dependency.** Both frames already exist, so `P1_004` and `P1_006` can generate in
  parallel.
- **The turn is motivated.** It lands on *"Tonight she answers for herself"* — he turns to present
  her as he says it. The handoff is enacted, not just cut.

**13s rather than 12, +10 cr, and worth it.** The floor is 11.6s. An end frame on a talking clip is
**unproven**, and the obvious failure is the model rushing the dialogue to reach the end pose in
time. A second of headroom removes the pressure to rush, on the first spoken shot of the show.

**RESULT 2026-09-20 — Turbo has no end-frame slot, so fix 1 cannot be run on Turbo; `P1_004` was made by the chain (fix 2), and it passed.** `P1_004` start frame only; its last frame extracted and used as `P1_006`'s start. Measured (`shots/_measure/COLD_OPEN_MEASURE.md`):
- **The turn happened anyway, from the prompt alone** — head turns 9.5–11.0s, in the pause, landing on "Tonight". Not rushed. The body stays in the `direct_b` position, so `P1_006` opens on that pose, not on `frame_host_b` — which is correct for a chain.
- **Join:** 1.76 mean abs luma diff, 0% of pixels >25, luma −0.4%. Seamless in picture.
- ⚠️ **Chroma +7.1% across the join** (16.49 → 17.66), blue channel down ~4.7% — the documented colour-range-conversion signature, from the extraction step. Invisible in a split-frame still; judge it at the cut. Edit fix if it shows: `colorchannelmixer=rr=0.994:gg=1.005:bb=1.049` on `P1_006` (tested on its first frame: chroma back to 16.81, diff to 2.13). For every later chain extract with the ffmpeg line in *Chained rows*, no range conversion.

⚠️ **Superseded by the result above — kept as the record of what was planned.** ~~Untested on a talking clip — so this shot is the test.~~ Start+end frames are proven on silent
clips (the draw-ons, `BRAND_bumper_out`). On dialogue they may pull on the performance, and it is not
yet confirmed that **Turbo** accepts an end frame at all. `P1_004` is already the first shot of the
3-shot gate, so the test costs nothing extra. **Fallback ladder, in order:**

1. **Start + end frame** — as above. Reject if the last seconds rush the line or the mouth distorts.
2. **Chain** — generate `P1_004` with the start frame only, then start `P1_006` from `P1_004`'s end
   frame via Kling's native extraction. Proven; one link, so the luminance loss is negligible.
3. **Cut mid-turn** onto a fresh `frame_host_b` — the weakest: the eyeline matches but the pose can
   jump.




**P1_006** · INTERJECTION · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` **chain from `P1_004`** (its last frame — the head is already turned to her; *not* `frame_host_b`, see P1_004's result) · 20 syllables · needs 6.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, in the studio now and turned to her, warm and straightforward. This is a greeting, not a build — his tone stays level and easy.

 The host says, warm and easy: "Cleopatra the Seventh. Last ruler of Egypt. Thank you for sitting down with me."

 He leans forward slightly with his hands clasped between his knees, then settles back as he finishes.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Cleopatra the Seventh. Last ruler of Egypt. Thank you for sitting down with me.
**provenance:** `[D]` Documented — Last reigning Ptolemaic monarch, 51-30 BC. Caesarion was nominal co-ruler; the lower third says 'Last ruler of Ptolemaic Egypt' for that reason.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 8s → 7s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_006a** · REACTION · GUEST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_cleopatra_c`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman listens as he names her and thanks her. She does not speak and her lips stay closed throughout — no talking, no mouthing of words. She receives the introduction with composure, courteous but not warm: a very slight inclination of the head in acknowledgement, then her gaze settles on him, on the point of answering. Her right hand rests on the arm of the chair and her left hand lies open in her lap throughout.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_006 from *"Thank you for sitting down with me"* to its end, then holds a beat before her reply. **Her first appearance in the studio** — she is seen being introduced before she is heard. Her lower third opens here.
**Subtitle:** — (P1_006's subtitle continues under it)

**added 2026-09-20 (director's toolkit):** the welcome used to cut straight from him naming her to her answering. A line *about* the other person — naming, introducing, thanking, charging them — plays on **their** face: the viewer meets her on the listen, then hears her. `P1_007` now chains from this clip. The id is `006a` because ids in an edited kit stay stable (see §9's note on gaps): an inserted row takes the previous id plus a letter.

**P1_007** · INTERJECTION · GUEST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**

`start_frame` `chain from P1_006a` · 16 syllables · needs 5.4s (duration model v2)
> ⚠️ **REGENERATE when the kit is final** — the current take started from `frame_cleopatra_c` directly, before `P1_006a` was added; it now chains from the reaction.

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman answers evenly, courteous but not warm, with the faintest dryness under it. Her tone stays low and level throughout.

 The woman says, evenly, courteous but not warm: "You have questions. Ask them plainly — I have heard the polite versions."

 She holds his gaze, her right hand resting on the arm of the chair and her left hand open in her lap, and holds there to the end.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** You have questions. Ask them plainly — I have heard the polite versions.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 7s → 6s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed:** the original ran *"Ask them while I still have the time"*, which put a clock on her life and belongs to the live-event frame this series does not use. The replacement establishes in her first line that she has been asked before — which is the retrospective frame stated in her own voice.

**changed 2026-09-19 (visual grounding, B3):** the gesture line said *hands folded in her lap*; `frame_cleopatra_c` has her right hand on the chair arm and her left hand open in her lap. A prompt that contradicts the start frame asks the model to move her into the described pose — an unscripted gesture on her first line. The line now describes the frame as it is. Same fix on `P1_004`: his hands are clasped between his knees, not on his lap.

### Act A — The Inherited Position

**P1_008** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host` · 36 syllables · needs 10.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, calm and genuinely curious, opening rather than pressing. His tone stays level and warm throughout, and his voice lifts a little at the end so the last line reads as an invitation.

 The host says, calm and curious, opening: "Let's start with what you were handed. You inherit a kingdom that is enormously wealthy and cannot defend itself. Describe where that left you."

 He shifts his weight slightly in the chair and opens one hand from the armrest on the last sentence, then lets it settle back.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Let's start with what you were handed. You inherit a kingdom that is enormously wealthy and cannot defend itself. Describe where that left you.
**provenance:** `[D]` Documented — Egypt's grain wealth and absence of a standing legionary force: Roller, *Cleopatra: A Biography*; Chauveau, *Egypt in the Age of Cleopatra*.
**SFX:** studio room tone only.

**2026-09-21: take A won the A/B; it is regenerated anyway with the rest of the part** (moved to `shots/_measurement_takes/`). A/B against *"He begins speaking immediately."* (take B, `_measurement_takes/P1_008_B.mp4`): see Mode 4 §3.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_009** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra` · 28 syllables · needs 8.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman answers evenly, stating known facts rather than defending anything. Her tone stays low and level throughout, never rising, never pleading.

 The woman says, evenly, stating known facts: "Egypt fed Rome. Grain, gold, papyrus, glass. We were the granary of an empire that had legions, and we did not."

 She settles slightly, hands staying folded in her lap.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Egypt fed Rome. Grain, gold, papyrus, glass. We were the granary of an empire that had legions, and we did not.
**provenance:** `[D]` Documented — Egyptian exports to Rome - grain above all, with gold, papyrus and glass: Roller; Chauveau.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_010** · BROLL_GEN · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr** + 3 cr still

> Standing grain moving in wind.

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A dense field of tall ripe grain filling the frame, heads heavy at the top of each stalk, a low flat horizon behind. No figures, no buildings, no machinery.

 Wide still image, nothing in motion, no figures. Composition balanced and simple, with clear empty space for on-screen text.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly toward the standing grain.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The heads of grain bend and recover in a slow travelling wave as the wind crosses the field, the nearest stalks moving most.

 Audio: ambience only, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_009 over the list of goods, cut back before her last sentence
**SFX:** generated clip carries only its own ambience — room tone bed carries it, nothing to duck

**changed:** was a Pexels row. The stock tier is gone — see `skill_mode4_produce.md` §10. Two steps because the charcoal style is the thing that must not drift, and a start frame is what holds it; 3 credits is cheap insurance.

**P1_011** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_e`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host listens, entirely still. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. He takes one slow breath and holds his gaze on her.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_010, then holds a beat
**Subtitle:** —

**P1_012** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_d` · 34 syllables · needs 10.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is unhurried and faintly dry, as though the point is obvious. Her tone stays low and even throughout, never sharpening.

 The woman says, unhurried and faintly dry: "Wealth without an army is not power. It is an invitation. Every Roman who needed money knew exactly where it was."

 On the second sentence she tilts her head very slightly, then stills.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Wealth without an army is not power. It is an invitation. Every Roman who needed money knew exactly where it was.
**provenance:** `[I]` Inferred — Consistent with the documented pattern of Roman financiers lending against Egyptian revenue; the aphorism is hers, the situation is attested.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_013** · BROLL_GEN · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool tunics, plain bronze helmets with a small flared neck guard and hinged cheek pieces, deep red wool cloaks, wide leather belts with hanging studded straps, heavy open-laced leather sandals. No metal shin guards. No plate or banded armour. A body of them on dry open ground, seen from behind, one rank behind another and receding into the distance, dust hanging low around their legs. Drawn from knee height looking along the ranks.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly along the ranks.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The ranks advance away from the camera at a steady walking pace, shoulders and cloaks swinging slightly with the stride, dust stirring around their legs as they go.

 Audio: low dust and wind, the muffled tread of many feet, distant and unemphatic. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_012 from the second sentence to its end, cut back on her last word
**SFX:** generated footfalls and armour ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**armour corrected.** The original read *segmented iron armour* — lorica segmentata, Imperial kit from the first century **AD**, roughly fifty years after Cleopatra died. Replaced with the registered `legionary_late_republic` wardrobe block: mail, not plate. **Crowd described by arrangement, not by count** — "a column" previously rendered as a line abreast.

**P1_014** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host` · 5 syllables · needs 2.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, quiet and brief, thinking aloud rather than replying. His tone stays level and low, no emphasis, no rise.

 The host says, quietly, thinking aloud: "Mm. And they all knew."

 He gives a single small nod on the first sound, then goes still.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Mm. And they all knew.
**provenance:** `[I]` Inferred — Echoes her preceding claim rather than adding one; retagged from [V] because 'they all knew' is an assertion about Roman awareness of Egyptian wealth.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_015** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `chain from P1_014` · 31 syllables · needs 8.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and factual, setting up rather than accusing. His tone does not harden at any point.

 The host says, level and factual, never hardening: "Your father dealt with that by borrowing. Enormous sums, from Roman financiers, to buy recognition as a friend of Rome."

 He rests his knuckles against his jaw on the second sentence and holds there.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Your father dealt with that by borrowing. Enormous sums, from Roman financiers, to buy recognition as a friend of Rome.
**provenance:** `[D]` Documented — Ptolemy XII's borrowing from Roman financiers (Rabirius Postumus) to purchase recognition as *amicus et socius populi Romani*, c. 59 BC: Cicero, *Pro Rabirio Postumo*.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (continuity):** was a fresh seed frame (`frame_host_d`) straight after P1_014, the same speaker with nothing cut in between — a pose snap on the same camera. Mode 4 §7: *"Across an interjection or a two-second reaction they cannot have changed posture, so chain instead."* Now chained from P1_014.

**P1_016** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_b` · 23 syllables · needs 7.5s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is precise and unsentimental, correcting the framing rather than defending her father. Her tone stays low and even.

 The woman says, precise and unsentimental: "He bought friendship with debt. I inherited both. They are the same object seen from two sides."

 She turns very slightly toward him on the last sentence, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** He bought friendship with debt. I inherited both. They are the same object seen from two sides.
**provenance:** `[I]` Inferred — She inherited both the debt and the client relationship; the equation of the two is her framing, not a source's.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_017** · BROLL_GEN · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A scatter of worn coins on dark stone, close, lit hard from one side so the relief on each face catches the light. No hands, no figures.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera drifts slowly sideways across the coins.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 Only the light moves — the highlights on the raised relief shift and travel across each face as the angle changes. The coins themselves are still.

 Audio: near silence, faint room air, a single soft metallic settle. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_016, then holds a beat
**SFX:** generated ambience ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**P1_018** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host_b` · 35 syllables · needs 10.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and factual, laying out context rather than pressing. His tone stays warm and does not sharpen.

 The host says, level and factual: "And Rome had already argued about swallowing Egypt whole. There were bills put before the senate. It was a live proposal, not a fear."

 He leans forward slightly with his hands clasped between his knees as he sets it out.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** And Rome had already argued about swallowing Egypt whole. There were bills put before the senate. It was a live proposal, not a fear.
**provenance:** `[D]` Documented — Annexation of Egypt was repeatedly raised at Rome: Cicero, *De Rege Alexandrino*; Suetonius, *Julius* 11.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_019** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_c` · 42 syllables · needs 12.0s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is even and unhurried, treating it as ordinary administration. Her tone stays low and level throughout, never rising.

 The woman says, even and unhurried, never rising: "Twice in my father's lifetime. A dead cousin of his was supposed to have willed our kingdom to Rome, and Rome kept the document. They were waiting for a reason."

 She holds his gaze, hands folded in her lap.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** `PUNCH` at *"They were waiting"* — push in ≤15% on the cut, hold to the end of the clip.
**Subtitle:** Twice in my father's lifetime. A dead cousin of his was supposed to have willed our kingdom to Rome, and Rome kept the document. They were waiting for a reason.
**provenance:** `[D]` Documented — **VERIFY CLEARED 2026-09-18.** Ptolemy XI Alexander II was the son of Ptolemy X; Ptolemy XII Auletes was an illegitimate son of Ptolemy IX, and the two were brothers. So Ptolemy XI was **her father's cousin**, not hers — 'a dead cousin' out of her mouth was wrong by a generation, and the line now reads 'a dead cousin of his'. The second correction was not in the original flag: **the will itself is contested.** Sulla displayed it in Rome as justification for installing his candidate, and the sources treat that as a pretext rather than a straightforward bequest — Cicero, *De Rege Alexandrino*. The line no longer asserts it, and 'was supposed to have willed' is both the safer claim and the better performance: she is a hostile witness and gets to be contemptuous of it. Clip goes 12s → 13s for the six added syllables.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_020** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_e`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host takes that in. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. He takes one slow breath and keeps his gaze on her.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_019, then holds a beat
**Subtitle:** —

**P1_021** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host_c` · 33 syllables · needs 9.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, dry and light, telling it back to her rather than challenging. His tone stays warm throughout.

 The host says, dry and light: "You were eighteen. Co-ruling with your younger brother, under advisors who decided quite quickly that they preferred him alone."

 He settles further back with one ankle crossed and lets one hand rest open on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** You were eighteen. Co-ruling with your younger brother, under advisors who decided quite quickly that they preferred him alone.
**provenance:** `[D]` Documented — Accession at about eighteen in 51 BC, co-rule with Ptolemy XIII, and the court faction that displaced her: Plutarch; Cassius Dio.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_022** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra` · 28 syllables · needs 8.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is flat and factual, offering no drama at all. Her tone stays low and even, never rising.

 The woman says, flat and factual: "They removed me. I went to the eastern frontier, raised troops there, and came back with an army at the border."

 She holds his gaze, hands folded in her lap.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** They removed me. I went to the eastern frontier, raised troops there, and came back with an army at the border.
**provenance:** `[D]` Documented — Expulsion, the raising of forces on the eastern frontier, and the return to the border at Pelusium: Caesar, *Civil War* 3; Plutarch.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed 2026-09-20 (junction rule):** "They removed me. I went east, raised troops on the frontier, and came back with an army at the border." → rephrased to remove went east — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_023** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_b` · 9 syllables · needs 3.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, light and genuinely amused, not scoring a point. His tone stays warm and easy.

 The host says, lightly, genuinely amused: "You say that like a change of address."

 He leans forward slightly with a small half-smile, then settles.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** You say that like a change of address.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 3s → 4s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_024** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_e` · 41 syllables · needs 11.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is level and unbothered, correcting a premise rather than defending herself. Her tone stays low and even throughout, never rising, never pleading.

 The woman says, level and unbothered, never pleading: "That is what a Ptolemaic succession was. My family had been killing each other for the throne for two hundred years. I was raised inside that arithmetic."

 She settles a little further back into the chair on the last sentence, chin a fraction higher.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** That is what a Ptolemaic succession was. My family had been killing each other for the throne for two hundred years. I was raised inside that arithmetic.
**provenance:** `[I]` Inferred — **Retagged from [D] 2026-09-18.** The pattern is documented and is the standard characterisation of the later dynasty (Roller; Chauveau); the round figure is hers. Anchored: Ptolemy IV's accession purge in 222 BC — his uncle Lysimachus, his brother Magas scalded in his bath, his mother Berenice II poisoned — is **174 years** before she speaks, and the killing of rival brothers runs back further still, to Ptolemy II. So 'two hundred years' is a fair characterisation and a false precision at the same time. **Nothing changes in the line; the tag stops asserting the number as the record's.** No regeneration.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 14s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_025** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_host_c` · 30 syllables · needs 8.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, curious and light, offering it as an observation rather than a test. His tone stays warm and level.

 The host says, curious and light: "Your family was Macedonian Greek. Three hundred years in Egypt, and you were the first of them who learned the language."

 He settles back with one ankle crossed and rests one hand open on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Your family was Macedonian Greek. Three hundred years in Egypt, and you were the first of them who learned the language.
**provenance:** `[D]` Documented — Macedonian Greek dynasty; she was the first Ptolemy recorded as learning Egyptian: Plutarch, *Life of Antony* 27.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_026** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_cleopatra_b` · 28 syllables · needs 9.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is matter-of-fact, offering no pride in it at all. Her tone stays low and even throughout.

 The woman says, matter-of-fact, without pride: "Nine languages. Egyptian was the one that mattered. My ancestors ruled a country they could not speak to."

 She turns very slightly toward him on the last sentence, hands staying folded, and holds his gaze after the last word.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Nine languages. Egyptian was the one that mattered. My ancestors ruled a country they could not speak to.
**provenance:** `[I]` Inferred — Plutarch (*Ant.* 27) says she rarely needed an interpreter and lists the peoples she addressed directly; **the figure 'nine' is a modern enumeration of that list, not Plutarch's own count.** Keep or change the number deliberately.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_027** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_e` · 5 syllables · needs 2.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, quiet and brief, thinking aloud rather than asking. His tone stays flat and low, no emphasis.

 The host says, quietly, thinking aloud: "And that changed things."

 A single small nod, then stillness.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** audio only, under the tail of P1_026 after her last word — `OFFMIC`: his thought heard, her face kept. Picture discarded.
**Subtitle:** And that changed things.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_028** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `chain from P1_026` · 32 syllables · needs 9.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is precise and unhurried, explaining a mechanism rather than making a claim. Her tone stays low and level.

 The woman says, precise and unhurried: "It let me be crowned as a pharaoh and not merely as a Greek who held the throne. The priests mattered. The grain came through them."

 She holds still to the end, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** It let me be crowned as a pharaoh and not merely as a Greek who held the throne. The priests mattered. The grain came through them.
**provenance:** `[D]` Documented — Coronation in Egyptian pharaonic form and the role of the priesthood in grain administration: Roller.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed 2026-09-20 (junction rule):** "It let me be crowned as a pharaoh and not merely as a Greek occupying the throne. The priests mattered. The grain came through them." → rephrased to remove Greek occupying — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_029** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_d` · 20 syllables · needs 6.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, genuinely curious and a little informal. His tone stays warm, and his voice lifts at the end so the question stays open.

 The host says, curious, a little informal: "What did the work really consist of? Day to day, I mean. Not the ceremonies."

 He rests his knuckles against his jaw and tilts his head slightly as he waits.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** What did the work really consist of? Day to day, I mean. Not the ceremonies.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 8s → 7s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "What did the job actually consist of? Day to day, I mean. Not the ceremonies." → rephrased to remove job actually — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_030** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_cleopatra_e` · 31 syllables · needs 9.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is dry and slightly weary, as though the answer disappoints people. Her tone stays low and even throughout.

 The woman says, dry and slightly weary: "Grain prices. Who got which temple. Arguments between Greeks and Egyptians who hated one another. Most of it was reading."

 She settles a little further back into the chair on the last sentence, hands clasped in her lap.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Grain prices. Who got which temple. Arguments between Greeks and Egyptians who hated one another. Most of it was reading.
**provenance:** `[D]` Documented — Administrative activity in her own hand - the 'ginesthō' royal subscription - and the papyrological record of grain and temple business: Roller; the papyri.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "Grain prices. Who got which temple. Arguments between Greeks and Egyptians who hated each other. Most of it was reading." → rephrased to remove hated each — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_031** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_b`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host reacts with quiet amusement at the ordinariness of it. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. A small breath of a smile, and he holds his gaze on her.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_030, then holds a beat
**Subtitle:** —

**P1_032** · BRAND_ACTBREAK · **5.0s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_actbreak_vessel.mp4` — the first break of the part. The stone takes the second.

**edit_placement:** plays between `P1_031` and `P1_033`. Hard cut in, hard cut out at **5.000** — it is a finished object and is never trimmed.
**Subtitle:** —
**SFX:** nothing to add; the bed is inside the file at −5 dB under the opening's. One chime opens the break, the study draws itself on the page, the finished page holds, and a second chime closes it. **`MUSIC_Drone_Low` enters on the cut back into `P1_033`**, not under the break.

**changed 2026-09-18.** Was a 6s generated charcoal b-roll of a carved wall — 60 cr plus a 3 cr still — carrying `MUSIC_Sting_Transition` on the cut in. Act breaks are fixed furniture now: **−63 cr**, and **the sting cue was cancelled outright**, because the break carries the theme's own strikes. Same instrument as the title music, so the break belongs to the same piece instead of sounding like a cue laid over it.

### Act B — Caesar

**P1_033** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host` · 38 syllables · needs 10.5s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and unhurried, laying out events. His tone stays warm and does not darken on the last clause.

 The host says, level and unhurried: "Then Rome's civil war arrives on your doorstep. Pompey loses to Caesar, runs to Egypt for shelter, and your brother's court makes a decision."

 He shifts his weight slightly and lets one hand rest open on the armrest.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Then Rome's civil war arrives on your doorstep. Pompey loses to Caesar, runs to Egypt for shelter, and your brother's court makes a decision.
**provenance:** `[D]` Documented — Pompey's defeat at Pharsalus, flight to Egypt, and the decision of Ptolemy XIII's court: Caesar, *Civil War* 3; Plutarch, *Life of Pompey* 77-80.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_034** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra_d` · 29 syllables · needs 8.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is controlled, with the faintest contempt held well under the surface. Her tone stays low and even, never rising.

 The woman says, controlled, contempt held well under: "They killed him at the shoreline and kept the head. They meant to present it to Caesar as a courtesy. A gift."

 She holds still throughout, chin a fraction higher on the last two words.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** They killed him at the shoreline and kept the head. They meant to present it to Caesar as a courtesy. A gift.
**provenance:** `[D]` Documented — Pompey killed at the shoreline, head retained and presented to Caesar: Plutarch, *Pompey* 77-80; Cassius Dio 42.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_035** · BROLL_GEN · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr** + 3 cr still

> Waves breaking on a shoreline in low light.

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A low shoreline seen close to the waterline, a wave curling and breaking across the frame, wet sand catching the light in the foreground. No figures, no boats, no buildings.

 Wide still image, nothing in motion, no figures. Composition balanced and simple, with clear empty space for on-screen text.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pulls back very slowly from the water's edge.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 A wave gathers, breaks along the shoreline and draws back, then another behind it. The foam spreads and thins across the wet sand each time.

 Audio: ambience only, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_034, then holds a beat
**SFX:** clip carries its own surf — duck under the line

**changed:** was a Pexels row. The stock tier is gone — see `skill_mode4_produce.md` §10. Two steps because the charcoal style is the thing that must not drift, and a start frame is what holds it; 3 credits is cheap insurance.

**P1_036** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_c` · 36 syllables · needs 10.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is precise, laying out reasoning rather than asserting. Her tone stays low and even throughout.

 The woman says, precise, never asserting: "Caesar wept in front of them. Whether the grief was real I cannot tell you. But the miscalculation was total, and I saw it before they did."

 On the last sentence she lifts one hand slightly from her lap, turns it open, and lets it settle back.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** `PUNCH` at *"But the miscalculation"* — push in ≤15% on the cut, hold to the end of the clip.
**Subtitle:** Caesar wept in front of them. Whether the grief was real I cannot tell you. But the miscalculation was total, and I saw it before they did.
**provenance:** `[D]` Documented — Caesar's weeping at the presentation of the head is reported in the ancient accounts: Plutarch; Dio 42.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_037** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_d`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host listens, weighing what he has heard. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. His knuckles rest against his jaw and he takes one slow breath.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_036, then holds a beat
**Subtitle:** —

**P1_038** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host_b` · 22 syllables · needs 7.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, genuinely asking rather than testing. His tone stays level and warm, and his voice lifts clearly at the end so the last line lands as a real question.

 The host says, genuinely asking, never testing: "Understood what, exactly? They had handed him his enemy's head. What did they get wrong?"

 He leans forward with his elbows on his thighs, hands clasped, and holds her gaze as he asks.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Understood what, exactly? They had handed him his enemy's head. What did they get wrong?
**provenance:** `[D]` Documented — Restates the documented act - the head presented to Caesar: Plutarch, *Pompey* 77-80; Dio 42. Retagged from [V]: a host echo that restates a fact is still asserting it.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_039** · INTERVIEW · GUEST · **13s** · Kling 3.0 Turbo, audio on · 10 cr/s · **130 cr**
`start_frame` `frame_cleopatra_d` · 44 syllables · needs 12.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is even and unhurried, taking no relish in it. Her tone stays low and level throughout, never sharpening.

 The woman says, evenly, taking no relish in it: "That Romans may destroy each other. Foreigners may not. They killed a Roman consul to flatter another Roman, and made themselves the only barbarians in the room."

 She settles her shoulders square and holds entirely still through the last sentence.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** That Romans may destroy each other. Foreigners may not. They killed a Roman consul to flatter another Roman, and made themselves the only barbarians in the room.
**provenance:** `[I]` Inferred — Interpretation of the court's miscalculation, consistent with the Roman reaction the sources record; the reading is hers.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 14s → 13s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_040** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host_c` · 26 syllables · needs 7.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, light and a little playful, testing her rather than pressing. His tone stays warm throughout.

 The host says, lightly, a little playful: "And you got into that palace past your brother's guards. The story everyone knows involves a carpet."

 He tilts his head slightly on the last word, one hand resting open on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** And you got into that palace past your brother's guards. The story everyone knows involves a carpet.
**provenance:** `[D]` Documented — The carpet is the popular modern version; the host states it as the received story, which is what it is.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_041** · REACTION · GUEST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_cleopatra_e`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman listens, unreadable. She does not speak and her lips stay closed throughout — no talking, no mouthing of words. Her gaze steadies on him. By the end of the clip she has settled into a still, composed position facing him, on the point of answering.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_040, then holds a beat
**Subtitle:** —

**P1_042** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `chain from P1_041` · 36 syllables · needs 10.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is dry and unhurried, with a flicker of impatience she does not let surface. Her tone stays low and even.

 The woman says, dry, impatience held under: "A bedding sack, in the account you inherited. You have made a romance of it. It was trespass. It was also the only door still open."

 She turns very slightly toward him on the last sentence, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** A bedding sack, in the account you inherited. You have made a romance of it. It was trespass. It was also the only door still open.
**provenance:** `[D]` Documented — Plutarch, *Life of Caesar* 49 - a bedding sack (στρωματόδεσμον), not a carpet. **A deliberate correction of a popular story - flag it in the description.**
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_043** · BROLL_GEN · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A lamplit stone corridor at night, flames in wall niches, long shadows thrown across worn flagstones, the corridor running away from the viewer into darkness. Empty — no figures.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera moves slowly forward down the corridor.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The flames waver in their niches and the shadows they throw stretch and contract along the walls and floor as the view advances.

 Audio: low flame flicker, faint echo of distant movement, quiet air. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_042 from the second sentence to its end, cut back on her last word
**SFX:** generated flame ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**P1_044** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host_d` · 27 syllables · needs 8.0s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and factual, laying out the cost rather than pressing her with it. His tone stays warm and does not harden.

 The host says, level and factual, never hardening: "Backing you cost him. Caesar spent that winter besieged inside your palace quarter, with the harbour on fire."

 He rests his knuckles against his jaw through the second sentence, then lowers the hand.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Backing you cost him. Caesar spent that winter besieged inside your palace quarter, with the harbour on fire.
**provenance:** `[D]` Documented — The siege of the palace quarter and the harbour fire: Caesar, *Civil War* 3.106ff; the *Alexandrian War*.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_045** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra_d` · 26 syllables · needs 8.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is flat and factual, offering no drama. Her tone stays low and even throughout, never rising.

 The woman says, flat and factual: "A winter. Three thousand men against an entire city. I was inside those walls with him for all of it."

 She holds entirely still, forearms along the armrests.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** A winter. Three thousand men against an entire city. I was inside those walls with him for all of it.
**provenance:** `[D]` Documented — **VERIFY CLEARED 2026-09-18.** Caesar's force on arrival was roughly 3,200 legionaries with 800 cavalry; the siege ran through the winter of 48-47 BC. **'Four months' is withdrawn — the sources genuinely disagree.** One account runs the siege August 48 to January 47; another has Caesar relieved by Mithridates of Pergamon in March 47, which from his arrival days after Pompey's death makes it nearer six. Four months is not wrong so much as **unsupported precision**, which is the one thing a `[D]` tag must not carry. 'A winter' is what every account agrees on and what this tag already documented. ⚠️ It is **one syllable longer**, not shorter — 'Four months' is two syllables, 'A winter' three — which pushes the floor to 9.3s against a 9s clip, so the clip goes to **10s, 100 cr**. A one-word change moving a clip past its floor is exactly the thing the duration model exists to catch.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_046** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host` · 5 syllables · needs 2.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host asks it quietly and simply. His tone stays level and low, with a small lift at the end.

 The host says, quietly and simply: "And the library?"

 He tilts his head very slightly and holds the look, waiting.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** And the library?
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_047** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_b` · 32 syllables · needs 10.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is precise, correcting a record rather than defending herself. Her tone stays low and even throughout.

 The woman says, precise, correcting the record: "Warehouses on the dock caught fire. Books burned. Not the library. That version of the story grew later, and it grew in Rome."

 She turns very slightly toward him on the last sentence, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Warehouses on the dock caught fire. Books burned. Not the library. That version of the story grew later, and it grew in Rome.
**provenance:** `[I]` Inferred — Modern scholarly consensus is that dockside warehouses and stored books burned in 48 BC and that the Library itself was not destroyed then; the ancient sources diverge. Roller; Chauveau. **A deliberate correction - flag it in the description.**
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_048** · BROLL_GEN · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr** + 3 cr still

> Embers and sparks drifting against darkness.

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Scattered points of ember light drifting against a deep dark ground, brightest low in the frame and thinning toward the top, with faint smoke shapes between them. No fire source visible, no figures, no buildings.

 Wide still image, nothing in motion, no figures. Composition balanced and simple, with clear empty space for on-screen text.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera tilts slowly upward, following the embers as they rise.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 Embers lift and drift upward across the frame, wandering as they go, some fading out before they leave the top of the frame. The darkness behind them is still.

 Audio: ambience only, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_047 from the third sentence to its end, cut back on her last word
**SFX:** generated clip carries only its own ambience — add fire crackle from the SFX set, or leave to room tone

**changed:** was a Pexels row. The stock tier is gone — see `skill_mode4_produce.md` §10. Two steps because the charcoal style is the thing that must not drift, and a start frame is what holds it; 3 credits is cheap insurance.

**P1_049** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_host_b` · 29 syllables · needs 8.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and observational, not yet pressing. His tone stays warm throughout and the last line is dry rather than pointed.

 The host says, level and observational, dry: "Within a year you have Caesar's backing, your brother is dead, and you have a son you name for him. That is a fast year."

 He leans forward with his elbows on his thighs and clasps his hands as he lists the three things.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Within a year you have Caesar's backing, your brother is dead, and you have a son you name for him. That is a fast year.
**provenance:** `[D]` Documented — Caesarion, born 47 BC and named for Caesar: Plutarch; Dio.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_050** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_cleopatra_d` · 30 syllables · needs 9.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is entirely direct, offering no defensiveness whatever. Her tone stays low and level throughout, never pleading.

 The woman says, entirely direct, never pleading: "I made my country necessary to the most dangerous man alive. The child was part of that. I will not deny it."

 She holds absolutely still, forearms along the armrests.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** I made my country necessary to the most dangerous man alive. The child was part of that. I will not deny it.
**provenance:** `[I]` Inferred — Motive. The actions are documented; the calculation behind them is reconstruction and is written as hers.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed 2026-09-20 (junction rule):** "I made Egypt necessary to the most dangerous man alive. The child was part of that. I will not pretend otherwise." → rephrased to remove made Egypt · pretend otherwise — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_051** · BROLL_GEN · **5s** · Kling 3.0 Turbo, audio on · 10 cr/s · **50 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A single small oil lamp burning in a shallow clay dish on a stone ledge, deep shadow beyond it, the flame the only light in the frame.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly on the lamp.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The flame wavers and leans, brightening and dimming slightly, and the shadow it throws behind the dish shifts with it. Nothing else moves.

 Audio: faint flame, very quiet room air. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_050, then holds a beat
**SFX:** generated flame ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**P1_052** · INTERVIEW · HOST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_host_c` · 23 syllables · needs 7.0s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and observational, not yet pressing. His tone stays warm throughout.

 The host says, level and observational: "You went to Rome after that. Two years living in his gardens across the river, with the boy."

 He settles back with one ankle crossed and lets one hand rest open on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** You went to Rome after that. Two years living in his gardens across the river, with the boy.
**provenance:** `[D]` Documented — Her residence in Caesar's gardens across the Tiber, 46-44 BC: Cicero, *Letters to Atticus*.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 8s → 7s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_053** · INTERVIEW · GUEST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_cleopatra_c` · 30 syllables · needs 9.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is controlled and unhurried, with nothing performed in it. Her tone stays low and level throughout.

 The woman says, controlled, nothing performed: "I was there the day they killed him. I left within the month. Everyone he had favoured was suddenly in danger."

 On the last sentence she lifts one hand slightly from her lap, turns it open, and lets it settle back.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** I was there the day they killed him. I left within the month. Everyone he had favoured was suddenly in danger.
**provenance:** `[D]` Documented — She was in Rome at the assassination and left within weeks: Cicero, *Att.* 14.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_054** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_d`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host absorbs it without responding. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. His knuckles rest against his jaw and he takes one slow breath.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_053, then holds a beat
**Subtitle:** —

**P1_055** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_host_b` · 26 syllables · needs 8.2s (duration model v2)
> ⚠️ **REGENERATE when the kit is final** — the current take (2026-09-20) was made from the pre-blink-rule prompt. Kept only as a measurement take.
> ~~VALIDATED — this exact line and register tested clean at 10s and 12s~~ — no longer: the line changed on 2026-09-20 (junction rule). The register is unchanged.

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, calm and genuinely curious, asking rather than accusing. His tone stays level and warm throughout, never hardening or rising into accusation, but his voice lifts clearly at the end so the last line lands as a real question.

 The host says, calmly, asking rather than accusing: "Here's the question this series turns on. Was that statecraft? Or was that the day Egypt stopped being free?"

 As he speaks he shifts his weight slightly and lifts one hand in a small open gesture on the second question, then lets it settle. He tilts his head a little as he waits.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Here's the question this series turns on. Was that statecraft? Or was that the day Egypt stopped being free?
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed 2026-09-20 (junction rule):** "Here's the question this series turns on. Was that statecraft? Or was that the moment Egypt stopped being free?" → rephrased to remove moment Egypt — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged. ⚠️ **This was half of the validated pair.** Rewritten under the hard rule anyway; the platform-drift check now rests on `P1_057` alone, and this clip is judged like any other.

**P1_056** · REACTION · GUEST · **5s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `frame_cleopatra`
> 🔁 **Regenerate** (2026-09-21: every clip is regenerated from the final kit; earlier takes are in `shots/_measurement_takes/`).

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman listens. She does not speak and her lips stay closed throughout — no talking, no mouthing of words. She is composed and unreadable, taking in what she has just heard without reacting to it emotionally. Early in the clip her gaze steadies on him. By the end of the clip she has settled into a still, upright, composed position facing him, on the point of answering.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_055, then holds a beat
**Subtitle:** —

**P1_057** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `chain from P1_056` · 29 syllables · floor 11.0s

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman answers calmly and without apology, correcting a premise rather than defending herself. Her tone stays low and even throughout, never rising, never pleading, never sharpening into anger.

 The woman says: "You assume those were two things. For me they were one. Egypt did not survive without me. And I was nothing without it."

 On the last sentence she lifts one hand slightly from her lap, turns it open, and lets it settle back. She holds his gaze.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** You assume those were two things. For me they were one. Egypt did not survive without me. And I was nothing without it.
**provenance:** `[I]` Inferred — 'Egypt did not survive without me' - the Ptolemaic kingdom did end with her, which is documented; the claim of mutual dependency is her reading. Retagged from [V].
**SFX:** studio room tone only.

**2026-09-21 measurement take** (now in `shots/_measurement_takes/`; the whole part is regenerated from the final kit — re-measure the hook cut points on the new take). Measured: sentences at 0.3–2.1 · 3.15–4.2 · 6.0–8.1 · 9.9–11.35 s, lead-in only 0.3 s. **Join from `P1_056`: luma −3.3%** (Kling's per-link loss, the start frame was not yet pre-lifted) — level it with the grade in `shots/_measure/JOIN_GRADES.md` (`colorchannelmixer=rr=1.033:gg=1.031:bb=1.056` on this whole clip).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_058** · BRAND_ACTBREAK · **5.0s** · FIXED SERIES ASSET · **0 cr**

`Fixed_Assets/Branding/BRAND_actbreak_stone.mp4` — the second break of the part, alternating with the vessel at `P1_032`.

**edit_placement:** plays between `P1_057` and `P1_059`. Hard cut in, hard cut out at **5.000**.
**Subtitle:** —
**SFX:** nothing to add; the bed is inside the file. **`MUSIC_Drone_High` does not enter here** — it enters under `P1_077`, as the cue map says.

**changed 2026-09-18.** Was an 8s generated b-roll — 80 cr plus a 3 cr still — and the last photographic row in the kit before it was converted to charcoal. Replaced by fixed furniture: **−83 cr**. Alternating the two studies is what stops the break reading as a repeat.

### Act C — The Decade with Antony

**P1_059** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_host_c` · 28 syllables · needs 8.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, matter-of-fact and unhurried, laying out the sequence. His tone stays level and does not sharpen on the last clause.

 The host says, matter-of-fact and unhurried: "Caesar is assassinated. Rome fractures again. And you do the same thing a second time, with Antony."

 He settles back with one ankle crossed, one hand resting on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Caesar is assassinated. Rome fractures again. And you do the same thing a second time, with Antony.
**provenance:** `[D]` Documented — Caesar's assassination, the fracturing of Rome, and the alliance with Antony from 41 BC: Plutarch, *Life of Antony*.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "Caesar is assassinated. Rome fractures again. And you do the same thing a second time, with Mark Antony." → rephrased to remove Mark Antony — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_060** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_b` · 41 syllables · needs 11.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is brisk and businesslike, treating it as an arrangement rather than a romance. Her tone stays low and even.

 The woman says, brisk and businesslike: "Antony needed money and an eastern base for a campaign against Parthia. I needed a Roman who would not annex me. We were useful to each other."

 She turns slightly toward him on the last sentence, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Antony needed money and an eastern base for a campaign against Parthia. I needed a Roman who would not annex me. We were useful to each other.
**provenance:** `[D]` Documented — Antony's need for funds and an eastern base for the Parthian campaign: Plutarch, *Ant.*; Dio 49.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 14s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_061** · BROLL_GEN · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A Roman commander of the late Republic standing over a low table spread with maps and wax tablets in lamplight, seen from behind and slightly to one side with his head lowered toward the table, one hand flat on it. A sculpted leather cuirass with bronze fittings over a wool tunic, a deep red cloak over one shoulder. His face is not visible.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly toward the table.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 His shoulders rise and fall with his breathing and his hand shifts across the map; the lamplight wavers over the surface of the table.

 Audio: quiet room air, faint lamp flame, the small sound of a hand moving on parchment. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_060 from the second sentence to its end, cut back on her last word
**SFX:** generated ambience ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**changed:** the `@antony` character sheet is retired — b-roll is charcoal, which a photoreal sheet cannot drive. The figure is now **drawn from behind with his face not visible**, so the shot carries no likeness claim about a real named person and needs no sheet. The cuirass is described rather than referenced; a sculpted leather cuirass on a Roman commander c. 40–30 BC is defensible, but it was never verified and the framing no longer depends on it.

**P1_062** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host_d` · 32 syllables · needs 9.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, precise and level, with a slightly harder edge that never becomes accusation. His tone does not rise.

 The host says, precise, never accusing: "Ten years. Three children. And then a public ceremony where Roman territory is handed to your sons, in front of a crowd."

 He rests his knuckles against his jaw through the list, then lowers the hand on the last clause.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Ten years. Three children. And then a public ceremony where Roman territory is handed to your sons, in front of a crowd.
**provenance:** `[D]` Documented — Three children - Alexander Helios, Cleopatra Selene, Ptolemy Philadelphus - and the public ceremony of 34 BC: Plutarch, *Ant.* 54; Dio 49.41.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_063** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_d` · 22 syllables · needs 7.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman does not hedge at all. Her tone stays low and level, chin steady.

 The woman says, without hedging, level: "The Donations of Alexandria. Yes. We did that in daylight, in front of everyone."

 She holds still to the end, forearms along the armrests.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** The Donations of Alexandria. Yes. We did that in daylight, in front of everyone.
**provenance:** `[D]` Documented — The Donations of Alexandria, 34 BC: Plutarch, *Ant.* 54; Dio 49.41.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_064** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host` · 3 syllables · needs 1.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host repeats it back quietly, thinking aloud rather than challenging. His tone stays flat and low, no emphasis.

 The host says, quietly, thinking aloud: "In daylight."

 A single small nod, then stillness.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** In daylight.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_065** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `chain from P1_064` · 27 syllables · needs 8.0s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, precise and level, asking for the record rather than challenging it. His tone stays warm and even.

 The host says, precise, asking for the record: "Tell me what was actually granted. Not what Octavian said later. What the ceremony gave your children."

 He settles square in the chair and rests both hands open on his knees.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Tell me what was actually granted. Not what Octavian said later. What the ceremony gave your children.
**provenance:** `[D]` Documented — Presupposes that Octavian's later account diverged from what the ceremony granted, which is documented: Dio 50.1-5. Retagged from [V].
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (continuity):** was a fresh seed frame (`frame_host_c`) straight after P1_064, the same speaker with nothing cut in between — a pose snap on the same camera. Mode 4 §7: *"Across an interjection or a two-second reaction they cannot have changed posture, so chain instead."* Now chained from P1_064.

**changed 2026-09-20 (junction rule):** "Set out what was actually granted. Not what Octavian said afterwards. What the ceremony gave your children." → rephrased to remove Set out · said afterwards — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_066** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_b` · 31 syllables · needs 10.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is dry and unhurried, aware of how thin it sounds. Her tone stays low and even throughout.

 The woman says, dry, aware how thin it sounds: "Titles over kingdoms that were barely ours. Armenia, just conquered. Parthia, never taken. Kingdoms drawn on paper."

 She turns slightly toward him on the list of names, hands staying folded, and holds his gaze after the last word.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Titles over kingdoms that were barely ours. Armenia, just conquered. Parthia, never taken. Kingdoms drawn on paper.
**provenance:** `[D]` Documented — Alexander Helios proclaimed king of Armenia, Media and Parthia: Plutarch, *Ant.* 54; Dio 49.41. **Armenia had been taken that same year** — Antony marched on Artaxata and seized its king Artavasdes II in 34 BC: Dio 49.39–40. Parthia was never taken. 'Barely ours' is her judgement.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (fact error, found while researching the context cards):** the line said the titles were over countries *"Antony had not yet taken"*, naming Armenia. **Wrong for Armenia** — Antony invaded it and captured its king in 34 BC, months before the Donations (Dio 49.39–40). A `[D]` line written from memory, the exact failure Mode 3 rule 1 exists to stop. Rewritten to what the record supports; same point, same duration.

**changed 2026-09-20 (junction rule):** "Titles over land Rome did not hold and Antony had not yet taken. Armenia. Media. Kingdoms drawn on paper." → rephrased to remove and Antony — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_067** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_e` · 2 syllables · needs 1.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host repeats the word quietly, thinking aloud. His tone stays flat and low, no emphasis at all.

 The host says, quietly, thinking aloud: "Paper."

 A single slow breath, then stillness.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** audio only, under the tail of P1_066 after *"drawn on paper"* — `OFFMIC`: the echo heard over her face; she picks the word up in P1_068. Picture discarded.
**Subtitle:** Paper.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_068** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `chain from P1_066` · 31 syllables · needs 8.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is level with the faintest edge of amusement she does not let surface. Her tone stays low and even.

 The woman says, level, amusement kept under: "Paper is how every empire begins. Rome was a paper claim over Italy once, and nobody laughs at that now."

 She settles a little further back into the chair, chin a fraction higher, hands staying folded, and holds his gaze.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Paper is how every empire begins. Rome was a paper claim over Italy once, and nobody laughs at that now.
**provenance:** `[I]` Inferred — Rhetorical analogy. Rome's early expansion as claimed before it was held is a defensible characterisation, offered as her argument rather than as a statement of record. Retagged from [V].
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 10s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_069** · INTERVIEW · HOST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_host_b` · 36 syllables · needs 10.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, neutral, laying out the charge rather than making it. His tone stays level throughout.

 The host says, neutral, laying out the charge: "Octavian took that ceremony back to Rome. He used it to argue that a Roman general had been captured by a foreign queen."

 He leans forward slightly with his hands clasped between his knees as he sets out the argument.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Octavian took that ceremony back to Rome. He used it to argue that a Roman general had been captured by a foreign queen.
**provenance:** `[D]` Documented — Octavian's use of the Donations in the propaganda campaign at Rome: Dio 50.1-5.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_070** · INTERVIEW · GUEST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_cleopatra_c` · 38 syllables · needs 11.5s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is quicker here, with controlled anger held well under the surface. Her tone stays low and even and never breaks into heat.

 The woman says, quicker, anger held under: "Because he could not say what it really was. Rome does not celebrate a man for making war on other Romans. He needed a foreign woman to blame."

 On "other Romans" her chin lifts a fraction and she carries straight on without looking away. On the last sentence she lifts one hand from her lap, turns it open, and lets it settle back.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** `CUT-IN:hold` — P1_070a's *"But he—"* sits under her at *"other Romans"*, ~3 dB down; she does not stop. **Stay on her.** Then `PUNCH` at *"He needed a foreign woman"*, held to the end of the clip.
**Subtitle:** Because he could not say what it really was. Rome does not celebrate a man for making war on other Romans. He needed a foreign woman to blame.
**provenance:** `[I]` Inferred — Interpretation of Octavian's motive, well supported by the shape of the propaganda campaign the sources describe, but a reading rather than a statement.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_070a** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_b` · 7 syllables

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host starts to come in over her, firm but not loud, as though he has an objection ready. His tone stays level and never becomes a raised voice.

 The host says, firmly, starting to object: "But he was fighting them too."

 He leans in a fraction on the first word.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** audio only, under P1_070 at *"other Romans"* — the failed attempt of a `CUT-IN:hold`. **Cut the audio after "But he"**; she carries on over it. Picture discarded.
**Subtitle:** But he—
**provenance:** `[V]` Voice — an attempt, not a claim; the words after the cut are never heard.
**SFX:** studio room tone only.

**added 2026-09-21 (director's toolkit — `CUT-IN:hold`):** the one interruption in Part 1, and it fails: she does not yield to the Roman framing. The run-on words are generated so the model is never asked to stop mid-sentence.


**P1_071** · BROLL_GEN · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool tunics, plain bronze helmets with a small flared neck guard and hinged cheek pieces, deep red wool cloaks, wide leather belts with hanging studded straps, heavy open-laced leather sandals. No metal shin guards. No plate or banded armour. One of them standing at rest before a rough plastered wall in hard light, cloak hanging still, helmet held under one arm. Tight, drawn from slightly below.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 He shifts his weight once and settles again; the cloak stirs slightly. The wall behind him is still.

 Audio: quiet outdoor air, faint wind, one small shift of equipment. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_070, then holds a beat
**SFX:** generated ambience ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**armour corrected** — mail, not banded plate. See P1_013. The reference tag is dropped: identity comes from the wardrobe block, and passing a reference for anonymous extras produced rows of clone faces in testing.

**P1_072** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host_d` · 32 syllables · needs 9.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, neutral and unhurried, stating it rather than pressing it. His tone stays level throughout.

 The host says, neutral and unhurried: "He was married to Octavian's sister at the time. He divorced her by letter and had her removed from his house in Rome."

 He rests his knuckles against his jaw as he lays it out, then lowers the hand on the last clause.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** He was married to Octavian's sister at the time. He divorced her by letter and had her removed from his house in Rome.
**provenance:** `[D]` Documented — Antony's marriage to Octavia, the divorce by letter and her removal from his house: Plutarch, *Ant.* 57.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_073** · INTERVIEW · GUEST · **11s** · Kling 3.0 Turbo, audio on · 10 cr/s · **110 cr**
`start_frame` `frame_cleopatra_e` · 36 syllables · needs 10.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is even and unsentimental, with no defensiveness at all. Her tone stays low and level throughout, never sharpening.

 The woman says, even, never defensive: "That marriage was a treaty between two men. When the treaty failed, so did it. Rome understood that perfectly, and later claimed it had not."

 She settles a little further back into the chair on the last clause, chin a fraction higher.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** That marriage was a treaty between two men. When the treaty failed, so did it. Rome understood that perfectly, and later claimed it had not.
**provenance:** `[I]` Inferred — The marriage as an instrument of the Treaty of Brundisium is the standard reading; the judgement that Rome understood it so is hers.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 11s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "That marriage was a treaty between two men. When the treaty failed, so did it. Rome understood that perfectly, and pretended otherwise afterwards." → rephrased to remove pretended otherwise — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_073a** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host says nothing and lets the silence sit. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. He holds her gaze, forearms resting along the armrests, entirely still.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** plays between P1_073 and P1_074 — **the second answer**: he leaves the silence, and she fills it with the real answer. Hard cut in on her last word, cut out on her first word of P1_074.
**Subtitle:** —

**added 2026-09-21 (director's toolkit — the second answer):** she had already given her account of the marriage; the host's silence is what draws out the harder line that follows. `P1_074` still chains from `P1_073` — she cannot have moved while he held the silence.


**P1_074** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `chain from P1_073` · 26 syllables · needs 7.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is direct and level, naming it without triumph. Her tone stays low and even, with the faintest lift at the corner of the mouth.

 The woman says, direct, without triumph: "And you still repeat his account. Two thousand years later, in this room, you opened with his word for me."

 She holds his gaze, settled back with her hands clasped in her lap, entirely still.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** And you still repeat his account. Two thousand years later, in this room, you opened with his word for me.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (continuity):** was a fresh seed frame (`frame_cleopatra_d`) straight after P1_073, the same speaker with nothing cut in between — a pose snap on the same camera. Mode 4 §7: *"Across an interjection or a two-second reaction they cannot have changed posture, so chain instead."* Now chained from P1_073. The gesture line now describes the pose she is actually in at the end of P1_073 (settled back, hands clasped) instead of a different one.

**P1_075** · INTERJECTION · HOST · **3s** · Kling 3.0 Turbo, audio on · 10 cr/s · **30 cr**
`start_frame` `frame_host_e` · 4 syllables · needs 2.6s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host concedes it plainly, without discomfort. His tone stays level and low, no defensiveness, no apology.

 The host says, plainly, without discomfort: "That's fair. I did."

 A brief pause, a small acknowledging nod, and he does not look away.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** That's fair. I did.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_076** · REACTION · GUEST · **5s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr**
`start_frame` `frame_cleopatra_e`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman holds the moment, neither pressing nor softening. She does not speak and her lips stay closed throughout — no talking, no mouthing of words. She takes one slow breath and keeps her gaze on him.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** plays between P1_075 and P1_077, soundscape only — MUSIC_Drone_Low under
**Subtitle:** —

### Act D — The Shadow of Actium

**P1_077** · INTERVIEW · HOST · **12s** · Kling 3.0 Turbo, audio on · 10 cr/s · **120 cr**
`start_frame` `frame_host_c` · 43 syllables · needs 11.7s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, level and factual, laying out the sequence. His tone stays warm and does not drop into weight.

 The host says, level and factual: "Before any fighting, Octavian seized the will Antony had left with the Vestals, and read it to the senate. In it he asked to be buried in Alexandria."

 He settles back with one ankle crossed, one hand resting open on his knee.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Before any fighting, Octavian seized the will Antony had left with the Vestals, and read it to the senate. In it he asked to be buried in Alexandria.
**provenance:** `[D]` Documented — Octavian's seizure of Antony's will from the Vestals and its public reading, including the Alexandria burial request: Dio 50.3; Plutarch, *Ant.* 58.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 13s → 12s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "Before any fighting, Octavian took Antony's will from the Vestals and read it out in the senate. It asked to be buried in Alexandria." → rephrased to remove took Antony's · it out · It asked — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged. Floor rose to 12.7s, so the clip goes 12s → 13s.

**P1_078** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_b` · 22 syllables · needs 7.3s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is quiet and level, naming it without triumph. Her tone stays low and even throughout.

 The woman says, quietly, without triumph: "Beside me. That was the line they could not forgive. A Roman choosing Egypt for his grave."

 She turns very slightly toward him on the last sentence, hands staying folded.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** `PUNCH` at *"A Roman choosing"* — push in ≤15% on the cut, hold to the end of the clip.
**Subtitle:** Beside me. That was the line they could not forgive. A Roman choosing Egypt for his grave.
**provenance:** `[I]` Inferred — The burial request is documented; that it was the unforgivable detail is her reading of the Roman reaction.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_079** · REACTION · HOST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_host_e`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host lets the answer sit. He does not speak and his lips stay closed throughout — no talking, no mouthing of words. He takes one slow breath and keeps his gaze on her.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_078, then holds a beat
**Subtitle:** —

**P1_080** · INTERVIEW · HOST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_host_b` · 27 syllables · needs 8.5s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host, precise and level, with a slightly harder edge that never becomes accusation. His tone does not rise.

 The host says, precise, never accusing: "And the declaration of war that followed named you. Not him. Rome declared war on a foreign queen."

 He leans forward slightly with his hands clasped between his knees.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** And the declaration of war that followed named you. Not him. Rome declared war on a foreign queen.
**provenance:** `[D]` Documented — War was declared on Cleopatra, not on Antony: Dio 50.4-6.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 9s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "And the declaration of war that followed named you. Not Antony. Rome declared war on a foreign queen." → rephrased to remove Not Antony — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_081** · INTERVIEW · GUEST · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr**
`start_frame` `frame_cleopatra_d` · 20 syllables · needs 6.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is flat and unhurried, stating it rather than arguing it. Her tone stays low and even throughout.

 The woman says, flat and unhurried: "It was still a war between Romans. Naming me only made it simpler to hide."

 She holds entirely still, forearms along the armrests.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** It was still a war between Romans. Naming me only made it simpler to hide.
**provenance:** `[I]` Inferred — That it remained a Roman civil war fought under a foreign name is the standard modern reading, stated here as hers.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**changed 2026-09-20 (junction rule):** "It was still a war between Romans. Naming me only made that easier to hide." → rephrased to remove that easier — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_082** · INTERVIEW · HOST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_host` · 25 syllables · needs 8.0s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host resets to something heavier, but stays level — no gravity added by the voice. His tone does not drop or slow into drama.

 The host says, level, adding no weight: "Which brings us to the water. Thirty-one BC, off Actium. The fleets meet, and the battle is going badly."

 He shifts his posture, settling square, both forearms along the armrests.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Which brings us to the water. Thirty-one BC, off Actium. The fleets meet, and the battle is going badly.
**provenance:** `[D]` Documented — Actium, 31 BC: Plutarch, *Ant.* 65-66; Dio 50.31-35.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "Which brings us to the water. Thirty-one BC. The fleets meet at Actium, and the battle is going badly." → rephrased to remove at Actium — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_083** · BROLL_GEN · **7s** · Kling 3.0 Turbo, audio on · 10 cr/s · **70 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Open sea under a low overcast sky, a heavy swell running, no land and no vessels anywhere in the frame, spray torn off the wave crests. Wide.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pulls back very slowly.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The swell rises and falls across the whole frame continuously, crests forming and collapsing, spray driving off them in the wind.

 Audio: heavy water, sustained wind, no gulls. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_082 from the second sentence to its end, cut back on his last word
**SFX:** generated water ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**P1_084** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**
`start_frame` `frame_cleopatra_c` · 21 syllables · needs 7.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman offers absolutely no emotion and no defence. Her tone stays low, even and unforced throughout.

 The woman says, without emotion or defence: "Sixty ships. Mine, not his. I took them out through a gap in the line and I sailed south."

 She holds his gaze, hands folded in her lap, entirely still.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** `PUNCH` at *"I took them out"* — push in ≤15% on the cut, hold to the end of the clip.
**Subtitle:** Sixty ships. Mine, not his. I took them out through a gap in the line and I sailed south.
**provenance:** `[D]` Documented — Roughly sixty ships, her own squadron, breaking through and sailing south during the battle: Plutarch, *Ant.* 66; Dio 50.33.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (blink rule):** the gesture line named a blink. Named blinks come back as constant, obvious blinking (`P1_056` test; `P1_007` measured ~4 blinks in 7 s against "blinks once"). Removed — the model blinks naturally on its own.

**P1_085** · INTERJECTION · HOST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_host_d` · 8 syllables · needs 3.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host states it flatly, not yet accusing. His tone stays level and low, and he leaves the line open rather than closing it.

 The host says, flatly, not yet accusing: "In the middle of the battle."

 His knuckles rest against his jaw and he holds the look, waiting.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** In the middle of the battle.
**provenance:** `[D]` Documented — Restates the documented withdrawal during the engagement: Plutarch, *Ant.* 66; Dio 50.33. Retagged from [V].
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 3s → 4s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_086** · INTERVIEW · GUEST · **4s** · Kling 3.0 Turbo, audio on · 10 cr/s · **40 cr**
`start_frame` `frame_cleopatra_e` · 8 syllables · needs 3.1s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman repeats it back exactly, offering no defence and no apology. Her tone stays low and even, matching his rather than answering it.

 The woman says, evenly, matching his tone: "In the middle of the battle."

 She holds the look, entirely still, hands clasped in her lap.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** In the middle of the battle.
**provenance:** `[D]` Documented — Her repetition of the same documented fact, used for emphasis: Plutarch, *Ant.* 66; Dio 50.33. Retagged from [V].
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 3s → 4s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**P1_087** · BROLL_GEN · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 The wake of a vessel seen from astern — a widening trail of disturbed water receding toward an empty horizon at dusk. No boat visible in the frame.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera drifts slowly backward, away from the wake.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 The wake spreads and flattens as it recedes, the disturbed water settling behind it toward the horizon.

 Audio: water displaced and settling, low wind. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of P1_086, then holds a beat
**SFX:** MUSIC_Drone_Low rises underneath

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**P1_088** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**
`start_frame` `frame_host_b` · 33 syllables · needs 9.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host is measured and deliberate, setting a hook without pressing. His tone stays level and warm.

 The host says, measured, never pressing: "We will spend most of the next part on those sixty ships. Because everything that happens afterwards depends on what you meant by them."

 He leans forward with his elbows on his thighs, hands clasped, and holds there.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** We will spend most of the next part on those sixty ships. Because everything that happens afterwards depends on what you meant by them.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 11s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "We will spend most of our next hour on those sixty ships. Because everything that happens afterwards depends on what you meant by them." → rephrased to remove next hour — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**P1_089** · INTERVIEW · GUEST · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr**
`start_frame` `frame_cleopatra_c` · 28 syllables · needs 8.2s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman is level with a faint challenge and no heat at all. Her tone stays low and even.

 The woman says, level, a challenge without heat: "Ask it properly when you do. Everyone who has asked me so far already knew the answer they wanted."

 One forearm rests along the armrest; the other hand opens slightly in her lap on the last clause.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** Ask it properly when you do. Everyone who has asked me so far already knew the answer they wanted.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**P1_090** · INTERVIEW · HOST · **10s** · Kling 3.0 Turbo, audio on · 10 cr/s · **100 cr**

`start_frame` `frame_host_d` · 31 syllables · needs 9.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host asks it lightly, almost as an afterthought, and lets the last question sit. His tone stays level and does not press.

 The host says, lightly, almost an afterthought: "One more thing before we break. Most people, if they know one thing about you, know you as Antony's lover. Was that what it was?"

 He settles back, one hand resting on the armrest, and holds her gaze.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** One more thing before we break. Most people, if they know one thing about you, know you as Antony's lover. Was that what it was?
**provenance:** `[D]` Documented — Antony and Cleopatra's association is the single best-known fact about her and the subject Part 2 opens on. The host's framing of what 'most people know' is a statement about reception, not about the record.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 12s → 10s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "One more thing before we break. Most people, if they know one thing about you, know that you loved Mark Antony. Was that what it was?" → rephrased to remove Mark Antony — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**changed:** the original ran *"Octavian's forces have landed in the delta. They are already ashore"* — live news arriving mid-interview, which contradicts the retrospective frame, and factually wrong besides: Octavian advanced overland from Syria and took Pelusium; the seaborne pressure that summer came from the west with Gallus at Paraetonium. Replacing the line removes the error rather than correcting it. The new question is the Part 2 hook.

**P1_091** · BROLL_GEN · **9s** · Kling 3.0 Turbo, audio on · 10 cr/s · **90 cr** + 3 cr still

**STEP 1 — still** (Seedream, ~3 cr / ~$0.07 on fal):

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 A worn silver coin lying on dark stone, close and filling much of the frame, struck with two facing profile portraits — a man and a woman — and worn lettering around the rim. Lit hard from one side so the relief throws shadow. No hands, no figures.

 Wide still image, nothing in motion. Composition balanced and simple.
```

**STEP 2 — video**, image-to-video from that still:

```
The camera pushes in very slowly on the coin.

 A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents. It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage.

 Only the light moves — the highlights travel across the two raised profiles and the worn lettering as the angle shifts. The coin itself is still.

 Audio: near silence, faint room air. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers P1_090 from the second sentence to its end, cut back on his last word
**SFX:** generated surf ducked under the line

**changed:** converted to charcoal — the photoreal wording (*35mm film grain, cinematic*) is gone, and the prompt now describes motion rather than re-describing what the start frame already carries.

**replaced.** The original showed legionaries wading ashore, which covered the old *"landed in the delta"* line — a line that has been deleted for being both outside the retrospective frame and factually wrong (Octavian advanced overland and took Pelusium; there was no amphibious landing). The new host line asks about Antony, so the cutaway is now the joint coinage the two of them actually issued: documented, an object rather than a person, and it makes no likeness claim about either.

**P1_092** · REACTION · GUEST · **4s** · audio OFF · Kling 3.0 Standard, audio OFF · 8 cr/s · **32 cr**
`start_frame` `frame_cleopatra`

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman receives the question without reacting to it. She does not speak and her lips stay closed throughout — no talking, no mouthing of words. She takes one steadying breath and remains composed. By the end of the clip she is still and upright, facing him, on the point of answering.

 Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** covers the tail of the host's line after P1_091 cuts back, then holds a beat
**Subtitle:** —

**P1_093** · INTERVIEW · GUEST · **8s** · Kling 3.0 Turbo, audio on · 10 cr/s · **80 cr**

`start_frame` `chain from P1_092` · 29 syllables · needs 7.9s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The woman takes the question without defending against it — composed, unhurried, faintly amused at the last clause. Her tone stays low and even.

 The woman says, composed, faintly amused at the end: "It was a treaty first. Whether it became more than that is a question no one has ever asked me honestly."

 She settles upright, hands folded in her lap, and holds his gaze.

 Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**Subtitle:** It was a treaty first. Whether it became more than that is a question no one has ever asked me honestly.
**provenance:** `[I]` Inferred — Rewritten line. The political basis of the Antony alliance is documented (Plutarch, *Ant.*; Dio 49); 'it was a treaty first' is her characterisation of it, not a source's words.
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** 9s → 8s (duration model v2, measured on six clips); delivery note moved inside the attribution (vendor syntax).

**changed:** the original ran *"I have very little time left"* — the clock again. The replacement answers the new question, opens more than it closes, and hands Part 2 its subject.

**P1_094** · INTERVIEW · HOST · **6s** · Kling 3.0 Turbo, audio on · 10 cr/s · **60 cr**

`start_frame` `frame_host_b` · 16 syllables · needs 5.4s (duration model v2)

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

 The host closes it warmly and without ceremony, as someone ending a session rather than a broadcast. His tone lifts very slightly on the last phrase.

 The host says, warmly, without ceremony: "Then that’s where we’ll pick this up. Part two, and the sixty ships."

 He gives a small nod and holds, hands still clasped between his knees.

 Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.

 Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo.
```

**edit_placement:** the hand-off. Last spoken line of the part; the wide follows it under music.
**Subtitle:** Then that’s where we’ll pick this up. Part two, and the sixty ships.
**provenance:** `[V]` Voice
**SFX:** studio room tone only.

**changed 2026-09-21 (recalculation pass):** delivery note moved inside the attribution (vendor syntax).

**changed 2026-09-20 (junction rule):** "Then that’s where we’ll pick it up. Part two, and the sixty ships." → rephrased to remove it up — a word ending in a stop running into a stressed vowel, the shape that failed five times as "without Egypt". Meaning and provenance unchanged.

**new shot.** The wide that follows carries no dialogue, so the hand-off needs its own clip — the structure is question → short guest response → host hands off → wide. Names the Part 2 subject explicitly, calling back to the sixty ships from P1_084.

**P1_095** · BUMPER_OUT · **5s transform, then held** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr** + 3 cr still

`BRAND_bumper_out` — **the live wide turns into a charcoal drawing of itself on camera**, and the credit roll runs over the drawing. Generated as a start→end frame transformation, not a cross-dissolve: the change is an event rather than a transition. Full rationale in `Fixed_Assets/SERIES_FURNITURE.md`.

**STEP 1 — start frame:** `frame_wide_cleopatra_marked.png` — the marked seed frame, which already exists. **0 cr.**

⚠️ **Not a frame lifted from a clip.** This step used to read *"lift a still from `P1_005`, the establishing wide"*. The establishing wide was removed from the kit on 2026-09-18, so there is no clip to lift from — and the seed frame was always the better source anyway, being a clean render rather than a compressed video frame.

**STEP 2 — end frame** (image-to-image, ~3 cr): run that still through the canonical style block.

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

 Keep the composition, the framing and both figures exactly as they are in the source image — same positions, same postures, same scale.
```

**STEP 3 — transformation**, start frame = the live still, end frame = the drawing, 5s:

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens and composition hold exactly as the start frame for the whole clip.

 The photographed room becomes a charcoal drawing of itself. The change begins at the edges of the frame and moves inward, so the two figures are the last thing to turn. Colour drains away to the warm grey of toned paper; shadows deepen into smudged charcoal and the paper grain rises through the whole image.

 Both people stay exactly where they are, at the same scale and in the same posture, through the whole change. Nobody moves, enters or leaves.

 Audio: quiet room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

**STEP 4 — hold** the last frame as a still for the rest of the credit roll. No reason to generate fifteen seconds of a picture that has stopped changing.

**edit_placement:** the close, after the host's hand-off in P1_094. MUSIC_Outro_Bed and the credit roll over the drawing, with `BRAND_mark` composited onto the studio panel.
**Subtitle:** —
**SFX:** room tone under the music.

**changed — this removes the only two-character generation in the kit and drops 150 cr a part to 43.** The row was a 15s wide of host and guest still talking, the one shot whose reliability had never been tested.

✅ **Tested and confirmed.** The figures hold position, scale and posture through the transformation, and it lands on the drawing rather than overshooting. No fallback needed.

## 6 · Assembly

I do this, not you. Send me the generated clips and I will return the assembled part.

1. **Run the ElevenLabs voice pass on all 66 talking clips first**, before trimming. Work from the processed versions after that, and keep the raws.
2. **Strip 1152 samples from the head of every converted clip, and loudness-normalise it** — one batch command, before anything reaches the timeline. Both are measured properties of the pass, not per-clip judgements:
   - ElevenLabs' MP3 export runs **exactly 1152 samples long — one MP3 granule, 26.1 ms** — written as head padding without gapless flagging, so decoders play it as leading silence. Strip it and the speech is **sample-aligned with the source at exactly 0 ms**, correlation unchanged. It looks like a lip-sync fault and is not one. **Do not slip clips on the timeline.** There is no WAV option on the Starter tier — MP3 44.1 kHz 128 kbps only — so this trim runs on every clip, every part.
   - The pass returns audio about **10 LUFS below source** (−34.0 against −23.6, with Speaker Boost already on). Headroom, not a fault — but normalise rather than applying a fixed gain, because the offset is not guaranteed constant across clips.

   ```bash
   ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,\\
   loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
   ```
3. Probe every clip for real duration, and for where speech actually starts and ends.
4. Trim heads and tails **in silence**, never mid-phoneme.
5. Butt-join the spine in shot order, closing every gap.
6. Lay the silent reactions and b-roll over the spine at the points their `edit_placement` describes, cutting on the beats named there rather than on a clock.
7. Normalise luma and saturation across chained runs, and **normalise each b-roll clip against its own first frame** — generated b-roll warms and darkens across a clip (measured over 8s: saturation 0.238 → 0.277, shadow 31.4% → 38.1%).
8. **Lay the room-tone bed under the entire part**, not only across the joins. Speech-to-speech resynthesises the voice rather than passing the source through, so the studio room tone **does not survive the pass** — measured, the source floor sits at −79 dBFS with 58% of its energy in 120–500 Hz (a structured room) and the converted floor at −86 dBFS, flat across every band (broadband dither). Both are inaudible, so there is no pumping at the cuts; the consequence is that **no clip has an acoustic floor at all**, and without a continuous bed the part sounds vacuum-sealed.
9. Burn in subtitles from the **Subtitle** fields.
10. Place on-screen source attributions on **`[D]` lines only**, using the source named in that row's **provenance** field. `[I]` lines are not attributed on screen — an inference with a citation under it reads as a claim the source does not make.

**Finish twice.** A **clean master** — picture, dialogue, room tone, music, no text of any kind — and the **titled master** that gets published, carrying subtitles, lower thirds, pull-quotes and source attributions. Mode 5 cuts reels from the clean one: all that text is positioned for 16:9, and a vertical crop slices straight through it.

What I cannot do here: judge a performance. If a clip is technically clean but the read is wrong, tell me and I will rewrite the line rather than try to cut around it.

## 7 · Primary sources

- Plutarch, *Life of Antony* — the principal narrative source, written over a century later and drawing on hostile Augustan-era material; used for sequence of events, not for motive.
- Cassius Dio, *Roman History*, Books 42–51 — the Actium narrative and the Octavian propaganda campaign, including the seizure and public reading of Antony's will.
- Caesar, *Civil War*, and the *Alexandrian War* — contemporary Roman account of the Egyptian intervention and the siege of the palace quarter.
- Josephus, *Jewish Antiquities* and *Against Apion* — an independent eastern perspective on Cleopatra's regional dealings.
- Ptolemaic coinage and the papyrological record, including the "ginesthō" royal subscription — evidence of her direct administrative activity in her own hand. This is what stands behind P1_030.
- Plutarch on her languages, and Roller on the Egyptian priesthood and the grain administration — behind P1_025 to P1_028.
- Modern scholarship: Duane Roller, *Cleopatra: A Biography*; Michel Chauveau, *Egypt in the Age of Cleopatra*; Prudence Jones, *Cleopatra: A Sourcebook*.

Dialogue is reconstructed from documented actions, administrative record, and accepted scholarly consensus about her circumstances and conduct. No surviving verbatim quotation of Cleopatra exists; nothing here contradicts the historical record.

Two lines deliberately correct a popular story rather than repeat it: the library (P1_047 — the dockside warehouse fire, not the Library) and the carpet (P1_042 — a bedding sack, per Plutarch).

## 8 · Trust disclaimer

**On screen** — the `P1_001` card, at 0:00, before any picture or sound. Fixed wording, byte-identical in every episode:

> AI-GENERATED DRAMATIZATION
>
> Historical reconstruction, not a recording.

Black, brand mark small at the foot, held 3 seconds, one soft brand sting under it. Built once in Mode 6 as `BRAND_disclosure` and reused — a fixed asset, not a per-episode build.

**In the description and on the end card** — the full statement:

> This programme is an AI-voiced dramatization. The guest is a historical reconstruction, not a recording. Dialogue is built from documented actions, primary sources, and academic consensus.

The host does not state the disclaimer aloud. The card, the description, the end card and Studio's "altered or synthetic content" toggle cover it; repeating it in dialogue cost twelve seconds of the opening minute for nothing.

Short version for Mode 5 reels: *"AI dramatization. Historical reconstruction, not a recording."* Reels circulate out of context, so their bumper stays.

The on-screen guest is a direct AI portrayal of Cleopatra VII, built from coin portraiture and archaeological evidence rather than the modern cinematic image — Reconstructable tier, per Mode 1.

## 9 · YouTube metadata

**Titles**

1. Cleopatra: "There Was No Egypt That Survived Without Me" — Part 1 of 2
2. The Interview Rome Didn't Want: Cleopatra VII Answers for Egypt [Part 1 of 2]
3. Cleopatra on Caesar, Antony, and the Charge She Sold Her Country [Part 1 of 2]

**Description hook.** Egypt was the richest kingdom in the Mediterranean and the least able to defend itself — and its last ruler has spent two thousand years being described by the man who destroyed her. In Part 1, Cleopatra VII answers for the alliance that saved Egypt and may have started selling it.

**Series index:** `[Part 1 of 2]`

⚠️ **Why `P1_002`, `P1_003` and `P1_005` are gaps rather than renumbered.** Ids are labels, not
indices. Renumbering ~90 rows to close three gaps would have had to update §12's six shot
references, every `plays between X and Y`, every `chain from X`, and the already-generated
`CARD_PLACEMENTS.md` — a large silent-failure surface for a cosmetic gain. **A kit built fresh by
Mode 4 comes out contiguous naturally; a kit edited in place keeps its ids stable so that work
already done against them stays valid.** Both are right in their own situation.

⚠️ **An arc is two parts. Always.** These titles said `Part 1/3` until 2026-09-18 — written before
the two-part decision and never corrected. A stale `/3` on a published title is a promise of a
third episode that is never coming, and it is visible to every viewer.

**No stock-footage attribution.** There is no stock footage in this part — all **twelve** b-roll shots are generated. The old Pexels credit block and the downloaded clips in `Episodes/Cleopatra/b-roll/` are both retired.

**Source list for the description — generated from the provenance tags**, not written beside them. Build it from every `[D]` and `[I]` row's named source or basis, deduplicated. Two checks make the claim honest: nothing cited that is not used, nothing claimed that is not cited.

**Name the corrections.** Two lines deliberately correct a popular story rather than repeat it — the carpet (`P1_042`, a bedding sack per Plutarch) and the library (`P1_047`, dockside warehouses rather than the Library). Those are the strongest available evidence of the show's method and belong in the description explicitly.

## 10 · Soundscape

**The part runs dry by default.** Music sits at structural points only; a drone appears where the content genuinely earns it and nowhere else. That restraint is the point — bedding every line in drones is what the channels this show is defined against do, and not doing it is legible to exactly the audience worth having.

All score tags are **BUILT** — the files are in `Fixed_Assets/Audio/`. Measurements, chosen takes and reject criteria in `Fixed_Assets/Audio/AUDIO_PROMPTS.md`; placement map in `Fixed_Assets/SERIES_FURNITURE.md`. The part can be generated and assembled now, with music laid in once the set exists.

### Always running

- **`ROOMTONE_studio`** — one continuous bed under the entire part, constant level, never ducking, running under held silences too. **Structural, not aesthetic:** the voice pass strips the studio ambience out of every clip, so without it the part sounds vacuum-sealed and every cut ticks.

### Fixed placements

| Cue | Where |
|---|---|
| `MUSIC_Theme_Main` | **inside `BRAND_opening` — nothing to place.** **Cut so the strongest beat lands at 2.35s**, where the sand reverses. The music stops dead with the sand at 2.0s — gap it, do not duck it. |
| `MUSIC_Outro_Bed` | already running **before** the `P1_095` transformation begins, so the change happens inside the music rather than being announced by it. Carries through the held drawing and the end card. Does not resolve — it decays. |
| `SFX_sand`, `SFX_plate` | **inside `BRAND_opening`** — nothing to place. `SFX_plate` is still laid by hand on every lower-third and pull-quote **entrance**; exits are silent. |
| `SFX_plate` | one soft paper settle on every lower-third and pull-quote **entrance**. Exits are silent. |

### Where the drone is earned — two places, and no more

- **`MUSIC_Drone_Low`** — enters under `P1_033` (Pompey killed at the shoreline, the head kept) and out after `P1_036`. This is the darkest passage in the part and the only place in Acts A–C that carries it.
- **`MUSIC_Drone_High`** — enters under `P1_077` (the will read out in the senate) and rises through the Actium sequence to `P1_090`. Act D is where the part turns, and the drone is what marks that.

**Everywhere else is dry.** Acts A and C run on voice and room tone alone. If a stretch of dialogue feels flat without music, that is a writing note, not a scoring one — do not paper over it with a bed.

### Diegetic sound

Generated inside each clip and named per shot. Where b-roll covers dialogue, duck or mute the generated ambience so the spoken line stays clean. **Do not generate movement foley** — it varies clip to clip and is harder to cut around than silence.

## 11 · Packaging

The title carries the subject; the thumbnail carries the provocation. They must not say the same thing — the viewer reads both at once, and duplicating wastes half the space.

**Chapter titles** — added 2026-09-21. Mode 6 fills the timecodes from the cut; YouTube needs the first at `0:00`, at least three, each ≥10 s.

| chapter | starts at |
|---|---|
| The charge | `0:00` — the opening and cold open |
| A kingdom that could not defend itself | `P1_008` |
| Caesar, and a head on the shore | `P1_033` |
| Kingdoms drawn on paper | `P1_059` |
| The will, the war, and sixty ships | `P1_077` |

**Thumbnail overlay lines** — 3 to 5 words, all caps, readable at phone size. Sits alongside the channel mark. Pick one:

1. **"NOTHING WITHOUT IT"** — her own words, and the thesis of the part. Pairs with any title.
2. **ROME NAMED HER FIRST** — leads with the propaganda angle; pairs with the seductress title.
3. **SHE SOLD EGYPT TO SAVE IT** — states the charge outright; strongest with a neutral title.

Avoid: her name (it is in the title), the part badge (that is a corner mark, not text), and question marks — questions read weaker than statements at thumbnail size.

**Thumbnail — BUILT.** `THUMB_cleopatra_p1.png` in this folder. System, recipe and exact values: `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`.

Toned paper ground, photoreal portrait lit for paper and placed whole on the right, ink type, walnut kicker reading `CLEOPATRA VII · PART 1`, statement `SHE WAS NEVER THE SEDUCTRESS`, mark bottom-left in ink.

**For Part 2, two lines of text change and nothing else** — the kicker and the statement. The portrait is reused; it is a per-guest asset, not a per-part one. Pull the statement from the Key Lines in §12, and check it does not repeat the title.

What the testing has to beat, measured on `frame_cleopatra.png` (see `thumbnail_test.png` in this folder):

| | |
|---|---|
| Source resolution | 2720 × 1536 |
| Tight 16:9 crop | 1342 × 755 — above YouTube's 1280×720 minimum |
| Face height, uncropped | ~45px at desktop feed size, ~26px mobile — **unusable** |
| Face height, cropped | ~91px — **usable** |

So cropping a pose frame is a real fallback, not a compromise to avoid. A generated still only earns its place if it fixes the three things the crop cannot: the microphone boom occupying the negative space the overlay line needs, the deliberately neutral expression, and the crop already sitting at the resolution floor with no room to go tighter.

## 12 · On-screen text

Placements are decided here, not at the edit. Geometry and treatment are fixed in `STUDIO_ASSETS.md`.

### Lower thirds — two, that is all

| | Opens over | Reads |
|---|---|---|
| Host | `P1_006`, his studio welcome | SALAH ALMAADAWY / *History Answers Back* |
| Guest | `P1_006a`, her first appearance — the reaction as he names her | CLEOPATRA VII / *Last ruler of Ptolemaic Egypt · 51–30 BC* |

Not over the hook clip in `BRAND_opening`'s 4.00–8.00 slot — that beat stays clean. Not over the direct-address shots either: those frames are frontal, so the enters-from-the-speaker's-side rule has no side to work with. Both land on the first studio appearance, which is also where the viewer is deciding who these two people are.

### Key lines — four, used in three places

Each is short enough to survive being read cold by someone who has watched nothing. These same four feed the pull-quotes below, the thumbnail candidates in §11, and the reel hooks in Mode 5.

| Line | From | Pull-quote lands over |
|---|---|---|
| "They were waiting for a reason." | `P1_019` | `P1_020` — host reaction, 4s |
| "The miscalculation was total, and I saw it before they did." | `P1_036` | `P1_037` — host reaction, 4s |
| "He needed a foreign woman to blame." | `P1_070` | `P1_071` — legionary b-roll, 8s |
| "A Roman choosing Egypt for his grave." | `P1_078` | `P1_079` — host reaction, 4s |

One per act — A, B, C, D. Every one lands **after** its line has finished, over picture that carries no dialogue, so it never runs against the burned subtitle saying the same words.

The teaser line — *"Egypt did not survive without me."* (changed 2026-09-21 from *"You assume those were two things. For me they were one."*) — is deliberately **not** pull-quoted. It already opens the episode at 0:04 and supplies the thumbnail overlay; a third appearance would be the same sentence three times.


### Context cards — who, where, what, on first mention

Added 2026-09-20. Opposite the speaker, upper band of the frame, 5.5 s, entering **as the word is
said**. Design fixed in `STUDIO_ASSETS.md` / `Branding/PLATE_SPEC.md`; rendered by
`build_episode_cards.py` from this table — **never written at the edit**. Side: `L` when the guest
speaks (she sits right), `R` when the host speaks. Each card is a factual claim and carries its
source; where a `[D]` line would also get an on-screen source credit at the same moment, the card's
source line **is** that credit — one piece of text at a time.

| # | Lands on | Word | Side | Label | Name | Gloss | Source |
|---|---|---|---|---|---|---|---|
| 01 | `P1_021` | brother | R | WHO | PTOLEMY XIII | Her younger brother and co-ruler, still a boy when they took the throne in 51 BC. | Caesar, *Civil War* 3.103 |
| 02 | `P1_024` | Ptolemaic | L | WHO | THE PTOLEMIES | Dynasty founded by Ptolemy, a general of Alexander the Great. Kings of Egypt from 305 BC. | Diodorus Siculus 20.53 |
| 03 | `P1_033` | Pompey | R | WHO | POMPEY | Rome's most celebrated general and Caesar's rival in the civil war. Beaten at Pharsalus, 48 BC. | Caesar, *Civil War* 3.88–99 |
| 04 | `P1_034` | Caesar | L | WHO | JULIUS CAESAR | Roman general who conquered Gaul, won the civil war and ruled Rome as dictator until 44 BC. | Suetonius, *Life of Julius Caesar* |
| 05 | `P1_059` | Antony | R | WHO | MARK ANTONY | Caesar's general. From 43 BC one of three men ruling Rome, and master of its eastern provinces. | Plutarch, *Life of Antony* |
| 06 | `P1_060` | Parthia | L | WHERE | PARTHIA | Empire east of the Euphrates, in today's Iran and Iraq. Rome's great rival in the East. | Plutarch, *Life of Crassus* |
| 07 | `P1_063` | Donations | L | WHAT | DONATIONS OF ALEXANDRIA | 34 BC: Antony proclaims Cleopatra's children rulers of kingdoms across the East. | Plutarch, *Antony* 54; Dio 49.41 |
| 08 | `P1_065` | Octavian | R | WHO | OCTAVIAN | Caesar's great-nephew and adopted heir; Antony's rival. From 27 BC, Augustus, the first emperor. | Suetonius, *Life of Augustus* |
| 09 | `P1_066` | Armenia | L | WHERE | ARMENIA | Mountain kingdom between Rome and Parthia. Antony seized its king in 34 BC. | Cassius Dio 49.39–40 |
| 10 | `P1_077` | Vestals | R | WHO | THE VESTALS | Priestesses of Vesta, keepers of Rome's sacred hearth. Wills and state papers were lodged in their care. | Plutarch, *Antony* 58; Suetonius, *Augustus* 101 |
| 11 | `P1_082` | Actium | R | WHERE | ACTIUM | Headland off western Greece. On 2 September 31 BC Octavian's fleet met Antony's and Cleopatra's there. | Cassius Dio 50.31–35 |

**Cutaways.** Three cards ride over a b-roll cutaway, which is allowed — b-roll has no face to
cover, and the card keeps its side: `06` continues into `P1_061`, `04` into the tail cover `P1_035`,
and `11` **enters** on `P1_083`, which covers `P1_082` from the sentence that says *Actium*. No card
overlaps a reaction of the other person, the lower thirds (`P1_006`/`P1_007`) or a pull-quote
(`P1_020`, `P1_037`, `P1_071`, `P1_079`).

**Left without a card, on purpose:** Rome, Egypt, Alexandria (said as a place, and inside card 07),
Octavia (explained in the line itself), Media (no longer in the line).

**Researched 2026-09-20, not written from memory.** The research found a `[D]` error in a spoken line —
`P1_066` said Armenia was not yet taken; Antony had seized it in 34 BC. Fixed in the row.


## 13 · Still outstanding for Part 1

**Nothing blocks generation.** The test programme is complete: camera lock (on both models), gesture without the enhancer, the ElevenLabs pass, b-roll start frames, the charcoal style, b-roll under motion, and the silent reaction all passed.

**Two things are unverified, and will be measured during production rather than tested separately:**

- **The chain path.** `P1_042`, `P1_057` and `P1_093` are chained and have never been generated on kling.ai. Measure luma at the first one — see §4.
- ~~`P1_095`, the closing wide.~~ **Resolved.** It is no longer a talking two-shot at all — it is the charcoal transformation, tested and confirmed.

**Both VERIFY flags are cleared — 2026-09-18.** `P1_019`: the kinship was wrong by a generation and the will is contested; the line now hedges and the clip goes to 13s. `P1_045`: 'four months' withdrawn for 'a winter', no clip change.

⚠️ **The old note said these were 'to be checked before publication rather than before generation'. That was wrong and the rule is now the opposite.** Such a flag sits on a *spoken* line, so changing a word means regenerating the clip and re-running the voice pass — 130 credits on `P1_019`. **Clear every such flag before generation, never after.**

**Needed before the part can be finished, not before it starts:**

**All of it is now built.** Updated 2026-09-18 — this list had gone stale and read as pending work.

- ~~Six `MUSIC_*` cues and `ROOMTONE_studio`~~ — **DONE.** Seven assets built, two cues cancelled
  (`MUSIC_Bed_Disclaimer`, `MUSIC_Sting_Transition`), both replaced by something the theme already
  contained. Measurements and reject criteria: `Fixed_Assets/Audio/AUDIO_PROMPTS.md`.
- ~~`BRAND_disclosure`, `BRAND_lowerthird`, `BRAND_pullquote`, `BRAND_bumper_in`, `BRAND_subscribe`,
  `BRAND_endcard`~~ — **DONE.** The disclosure card and the intro are inside `BRAND_opening.mp4`;
  the lower thirds, pull-quotes and end card are **generated per episode from §12 and the
  provenance tags** by `Branding/intro_source/build_episode_cards.py`, which is the last step of
  Mode 4. `BRAND_bumper_out` is still built per part, ~43 cr, from the marked wide seed frame.
- ~~The thumbnail still prompt is `PENDING` by design~~ — **resolved.** The prompt is Step 2 of
  `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`, and generating the portrait is now a **Mode 2**
  deliverable, once per guest, reused for Part 2.

  🔴 **This entry is why the list was audited.** It said `PENDING`, the portrait was then made by
  hand during testing, and nothing was ever updated to say *which mode makes it next time*. A later
  episode would have reached this point with no portrait and no instruction to generate one. **An
  artifact a kit names must be produced by a named mode** — "it already exists" is a fact about one
  episode, not about the pipeline. The marked wide seed frame had the same fault and is fixed the
  same way.
- The brand sign is composited onto the wide in Mode 6, never generated into it — **except in the
  outro**, where it goes onto the seed frame *before* the charcoal pass, so it is drawn rather than
  stamped.
