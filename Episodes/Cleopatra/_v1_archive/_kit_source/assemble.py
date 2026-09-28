# -*- coding: utf-8 -*-
import json,re,os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(HERE,"parsed.json")))
st=json.load(open(os.path.join(HERE,"build_stats.json")))
NEW=st["map"]
shotlist=open(os.path.join(HERE,"shotlist.md"),encoding="utf-8").read()
tail=d["tail"]
def renum(t): return re.sub(r'P1_(\d{3})', lambda m: NEW.get(m.group(0), m.group(0)), t)
tail=renum(tail)

HEAD = """# Cleopatra — Part 1 · Production Kit
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
| End frame slot | empty, except where a chain is stated |

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
| Talking spine (`INTERVIEW` / `INTERJECTION` / `NARRATION`) | 66 | 625 (10m 25s) | 10 | **6,250** |
| Reactions, silent | 10 | 42 | 8 | 336 |
| B-roll, generated | 15 | 101 | 10 | 1,010 |
| Establishing wide, silent | 1 | 4 | 8 | 32 |
| Closing wide (audio discarded) | 1 | 15 | 10 | 150 |
| Start frames for b-roll | 9 stills | — | — | ~27 |
| **Total** | **93 clips + 9 stills** | **787s** | | **~7,805** |
| Disclosure card, fixed asset | 1 | 3 | — | free |
| Teaser, edit-only lift | 1 | 5 | — | free |

Spine is 10m 25s. Reactions, b-roll and the wides overlay the spine rather than extending it, so the finished part runs a little over eleven minutes once the cold open and credit roll are counted.

Budget the reruns, not just the clips. Assume roughly one retry in six on talking clips — about 1,040 extra credits — so plan on **~8,850 credits** for Part 1.

**This is five times the old figure, and nothing got more expensive.** The previous total of ~1,710 was written for Higgsfield's 2.0 cr/s; kling.ai charges 10 cr/s for the same Turbo model and sells credits at a completely different price. Compare the money, not the credits: at Ultra-tier pricing Part 1 runs about **$46**. Do not carry the old credit numbers forward anywhere.

**Where the +280 credits went.** The five Pexels rows became generated charcoal b-roll (28s at 10 cr/s, plus 15 cr of stills). That buys one coherent visual language, no third-party licence surface, and no search step during writing — for about $1.72 a part.

**Every b-roll row is now two steps.** A still first, then image-to-video from it. The abstract rows used to go straight to text-to-video, but the charcoal style is the thing that must not drift across fifteen clips, and a start frame is what holds it. Three credits a row is cheap insurance.

## 3 · Start frames used

Host: `frame_host`, `_b`, `_c`, `_d`, `_e`, plus `frame_host_direct_b` and `_c` for the cold open.
Cleopatra: `frame_cleopatra`, `_b`, `_c`, `_d`, `_e`.
Wide: `frame_wide_cleopatra` (establishing, near the top) and `frame_wide_cleopatra_c` (the close — `CAST.md` designates `_c` for openings and closings).
Extras: **retired.** `@antony` and `@roman_legionary` are no longer character sheets. B-roll is charcoal, which a photoreal sheet cannot drive, and passing a reference for anonymous extras produced roughly twenty clone faces in testing. Identity for crowds now comes from the registered **wardrobe text block** in `STUDIO_ASSETS.md`, pasted byte-identical, with no reference image.

No speaker starts two consecutive turns from the same pose. The apparent repeats are deliberate: the two cold-open direct addresses are continuous, and the chained clips inherit their start frame from the previous clip's end frame.

## 4 · Generation order

1. **Cold open** — P1_002 to P1_007. Confirm the direct-address framing and the voice before committing to anything else.
2. **The validated pair** — P1_055 and P1_057. These two are known to work; generating them early confirms nothing has drifted on the platform side.
3. **Act A**, then B, C, D in order, talking clips first.
4. **Reactions** last within each act, once you know the exact tail you need to cover.
5. **B-roll stills** in one batch, then the b-roll videos in a second batch.
6. **The wides** last. The establishing wide and the closing wide use different start frames and different models.

**At the first chained clip, measure before trusting the chain procedure.** Kling extracts the end frame natively and applies it as the next start frame in-app. Both chain procedures in §5 were workarounds for faults introduced by *our own* ffmpeg extraction and by luma measurements taken on a different platform, so they may no longer apply. Compare the mean luma of the source clip's last frame against the new clip's first frame. If they match, drop both procedures and reconsider the three-link cap. If they do not, keep them exactly as written — and note that pre-lifting a frame to correct a loss that is not happening would make each link progressively *brighter*.

## 5 · Reading a row

Each row header carries the shot id, type, duration, **model, rate and credit cost**.

`start_frame` is the still to upload. Everything inside a code block is pasted into the prompt field, whole and unedited. **Subtitle** is the burn-in text. **provenance** is the line's source tag — see below. **edit_placement** on silent rows says what the clip is for, not a timecode; the exact cut is decided at assembly against the real durations. Rows carrying a **changed:** note were altered in this rebuild, and the note says why.

### Provenance tags — what backs every spoken line

| Tag | Meaning | Count |
|---|---|---|
| `[D]` **Documented** | attested in the record; the source is named on the line | 39 |
| `[I]` **Inferred** | consistent with the record, a reasonable reconstruction; the basis is named | 14 |
| `[V]` **Voice** | connective tissue, rapport, phrasing; **carries no factual claim** | 13 |

**A `[V]` line may not contain a factual assertion.** That rule is what makes the published source list honest, and the audit that applied it here moved seven lines out of `[V]` — host echoes like *\"They had handed him his enemy's head\"* restate a documented fact and are still asserting it.

**§7's source list is generated from these tags**, not assembled beside them: nothing cited that is not used, nothing claimed that is not cited.

Two tags carry an explicit **VERIFY** instruction — P1_019 (the kinship term for the Ptolemy who willed Egypt to Rome) and P1_045 (the four-month siege figure). Two more flag a deliberate correction of a popular story, P1_042 and P1_047, which the description should name.

### Chained rows

Chained rows say `chain from P1_0xx`: take that clip's **end frame** and use it as this clip's start frame. Kling does this natively in-app. The fallback — extract with `ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png`, no scale filter, no range conversion, and lift the frame about 1.5% before uploading — applies only if the native path proves lossy when measured at the first chain. Never exceed three links.

---

## Shot list

"""
out = HEAD + shotlist.rstrip() + "\n\n" + tail
open("P1_kit.md","w",encoding="utf-8").write(out)
print("kit written:", len(out.split("\n")), "lines")
