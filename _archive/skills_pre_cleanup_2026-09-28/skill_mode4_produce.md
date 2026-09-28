# SKILL: MODE 4 (PRODUCE EPISODE PART)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.


> 📂 **Inputs and output — added 2026-09-19 so each mode can run in its own chat.**
> **Reads:** `Episodes/<Guest>/OUTLINE.md` (its words **approved** in `SCRIPT_READ.md`) and `Episodes/<Guest>/CAST.md`; for Part 2, also `P1_kit.md` and `P1_EDIT_NOTES.md`.
> **Mode 4 does not change words.** A line that needs rewording goes back to `OUTLINE.md`, through the outline gates, and into the read again — the kit is built from approved text only.
> **Writes:** `Episodes/<Guest>/P<n>_kit.md`, then the per-episode brand renders and `CARD_PLACEMENTS.md` from `build_episode_cards.py`.
> **Save the output to that file before the mode ends.** Anything that lives only in chat history
> is lost to the next mode.


> 🔴 **Gates before any clip is generated — full text at §Provenance, §0b, and "Check the consonant junctions".**
>
> ```bash
> # set once per run — every gate works for any guest and any part:
> G=Episodes/<Guest>; N=<part number>; K=$G/P${N}_kit.md
> grep -n "VERIFY" $K | grep -vi "cleared" && echo "STOP — unresolved claim in a spoken line"
> python3 Fixed_Assets/tools/junction_scan.py $K                       # must print nothing — HARD RULE
> grep -h "^ \?Voice:" $K | sed 's/^ //' | sort | uniq -c              # exactly ONE line per speaker, each identical to CAST.md and STUDIO_ASSETS.md
> python3 Fixed_Assets/tools/chain_frames.py $G $N                     # continuity gate: same speaker back to back must chain
> awk '/^```/{f=!f} f && tolower($0) ~ /blink|nod|shakes? (his|her) head|then back|then lowers|briefly/' $K   # must print nothing — never name a blink or a repeatable gesture (§5)
> python3 Fixed_Assets/tools/lines_check.py $K                         # banned phrases + every rare name has a pronunciation
python3 Fixed_Assets/tools/screen_share.py $K                        # the guest carries the picture (§8b, Screen share) — added 2026-09-24
> python3 Fixed_Assets/tools/clip_status.py $K                        # kept / to do / credits left (reads Shots/)
> python3 Fixed_Assets/tools/prompt_check.py $K                        # the prompt-writing lessons (Fixed_Assets/LESSONS.md L1–L4)
> python3 Fixed_Assets/tools/pose_check.py $K                          # every prompt written from its seed frame's pose-table entry (§5) — added 2026-09-24
> ls $G/STORY_REVIEW.md $G/SCRIPT_READ.md                            # the arc's script review (Mode 3) exists — and Salah has approved it
> python3 Fixed_Assets/Branding/intro_source/context_build.py check $K # every context card fits
> ```
>
> **Part-aware since 2026-09-22.** Every tool takes the part (`chain_frames.py $G $N`,
> `round_sheet.py $G <pass> --part $N`, `build_episode_cards.py $G --part $N`). Part 1 keeps its original
> output names; Part 2+ renders carry a `p<N>` tag so nothing from Part 1 is overwritten.
>
> The fourth line enforces §7's *"across an interjection … chain instead"*. Part 1 broke it three times
> (`P1_014→015`, `P1_064→065`, `P1_073→074`) — a fresh seed frame after the same speaker is a pose
> snap on the same camera. The alternative the rule allows is `edit_placement: audio only, under …`
> on the first clip, discarding its picture.
>
> The third line guards the accent. **Accent reaches the cut from the Kling `Voice:` block**, not from
> ElevenLabs (which supplies timbre), so a stray variant block means a different accent in those clips.
> On 2026-09-20 the check found `STUDIO_ASSETS.md` and `CAST.md` still carrying the retired
> *Mediterranean colouring* two days after the kit was fixed — a Part 2 kit copied from them would
> have brought it back.
>
> ⚠️ Never write the word itself in kit prose (*"no … flags remain"*) — the grep cannot tell a mention from a flag, and fired on exactly that on 2026-09-23.
>
> A single hit stops the run: the flag sits on a *spoken* line, so after generation a one-word fix
> costs a regeneration and a voice pass. Then scan the spoken lines for **falsifiable specifics**
> — numbers, dates, kinship, who-did-what, absolutes — and make sure each one in a `[D]` line names
> respectable support, or retag it `[I]`. Keep it proportionate: on Part 1 that was 14 lines of 66.
>
> **Before generating, check every asset the kit names actually exists.** A kit that references a
file nobody produced fails at the worst moment. Part 1 shipped with two such orphans — the
thumbnail portrait and the marked wide seed frame — both of which existed only because testing
made them by hand. Both are now Mode 2 deliverables. **"It already exists" is a statement about one
episode, not about the pipeline.**

**And Mode 4 does not end with the kit** — it ends with `build_episode_cards.py`, which renders
> every per-episode brand asset into the guest folder. See §0b.


Everything in this file was arrived at through live testing. Follow it rather than improvising a new approach — the failure modes it prevents are expensive to rediscover.

Before generating anything, view the actual current file for every asset this part will use — seed frames, character sheets, camera plates, B-roll extras — per `STUDIO_ASSETS.md`'s Visual Grounding Requirement. For Part 2, first re-read Part 1's kit and carry its voices, seating, wardrobe, disclaimer wording and established facts forward unchanged.

**An arc is two parts.** Part 1 is the inciting conflict and the compromise; Part 2 is the reckoning. Part 1 must work as a complete argument on its own — it is the only entry point the arc has — and Part 2 opens by re-establishing the stakes in one exchange rather than assuming Part 1 is fresh in the viewer's mind.

**Runtime is the cost.** The talking spine is roughly 85% of a part's generation spend; reactions, b-roll and the outro together are under 15%. On kling.ai at 1080p every minute of dialogue is **about 600 credits** (Turbo, 10 cr/s), so the length of a part is a budget decision before it is a creative one. Target 10–12 minutes of spine. Trimming b-roll to save money is a false economy — cut a question instead, or don't.

## 0. The Opening — fixed shape, every part

The first minute decides whether the rest of the work is seen. This shape is not negotiable per episode:

1. **Disclosure card, 0:00, 4 seconds — and it is no longer a separate asset.** It is the first four seconds of `BRAND_opening.mp4`, built and byte-identical. Three lines — *AI-GENERATED DRAMATIZATION / Historical reconstruction, not a recording.* and, small and quiet down by the mark, *A conversation I wanted to hear.* That third line is the one piece of the show that is about the person making it; it earns its place by costing no extra time and by explaining why anyone bothered, which the disclosure alone does not. **The longer personal statement belongs on the end card, not here** — at 0:00 the viewer has not yet decided you are worth their time. **The text is set, not faded:** each line wipes in left to right behind a soft edge, the way type appears when it is being printed. A fade reads as a slide transition; a wipe reads as something being made. **On paper, not black**, with the brand mark small at the foot: the whole opening is one continuous page, and a black card in front of it breaks that page for no gain. It runs **4 seconds rather than 3** because the clock strikes every four, and the extra second buys legibility on the second line. The bed is the theme's own clock — no separate sting, and never true silence. Fixed wording, byte-identical across the whole series, built once in Mode 6 as `BRAND_disclosure`. It goes first, before any picture or sound, the way a rating card does. Keep it to two lines: the steepest part of every retention graph is the first five seconds, so the card earns its place by being unmissable and brief. The full statement — dialogue built from documented actions, primary sources and academic consensus — lives in the video description and on the end card, where there is room to read it.
1b. **Composite card — eyewitness episodes only, ~4 seconds.** Not at 0:00. It goes at the end of the cold open, immediately before the guest first appears in the studio, which is where it is actually relevant: the viewer is about to meet this person and needs to know what they are. Fixed slot, per-episode wording:

   > This guest is a composite. No such individual existed.
   > The character is assembled from [N] first-hand accounts, listed in the description.

   Skip it entirely on named-figure episodes — Cleopatra is a reconstruction of a real person, which the 0:00 card already covers. Built in Mode 6 as `BRAND_composite`, with the numbers filled per episode.

   For eyewitness episodes this card matters more than the AI disclosure does. The 0:00 card answers "is this a recording"; this one answers "is this a real person you are putting words into", which is the question that actually carries the risk here.

2. **Guest teaser — now the 4-second hook slot inside `BRAND_opening`, rendered as the guest's face emerging from the paper** (2026-09-22; `hook_build.py`, spec in `SERIES_FURNITURE.md`, *The hook treatment*). An edit-only lift of the guest's single strongest sentence from later in the part — no generation, no credits. Cold, no music, no host. The guest is the reason anyone clicked; the guest's voice belongs in the first ten seconds, not the second minute. Repeating the line later in the episode is intended.
3. **Title beat — `BRAND_bumper_in`, 5 seconds. BUILT, fixed series asset, zero credits.** Toned paper, the mark in ink, and the sand in the hourglass falling — then running back up. Identical in every episode; the title is inside the bumper rather than laid over a plate. Spec and rationale in `Fixed_Assets/SERIES_FURNITURE.md`. **Never generate a title beat per episode** — it is the one piece of furniture a model would render differently every time, which is the same failure the blank studio panel exists to prevent.
4. **One host direct-address hook**, not two. Whichever beat carries the *charge* against the guest, ending on a handoff line. Any scene-setting the second beat would have done is almost always already inside the host's first question — check before writing it, and cut it if so.
4b. ~~Establishing wide, 4 seconds, silent.~~ **Removed 2026-09-18. There is no wide clip in the cold open, and none anywhere in the part.** The generated two-shot puts the figures at the wrong scale against the chairs — they read a size too large, while the same characters in the singles read normal, so the fault is visible the moment the two are cut together. It comes from the seed frame, so rerolling does not fix it; several attempts proved that. Four seconds of a held wide is long enough for anyone to see it. The two-shot survives only as the still that opens `BRAND_bumper_out`, where it sits for about a second and then turns into charcoal — short, and then stripped of the photographic reference the eye was judging scale against. **An empty studio wide is not the substitute**: a room with nobody in it proves nothing about the two people who are about to talk. The cold open now cuts from the hook straight into the singles.
5. **A short welcome exchange in the studio** — host greets the guest by name and title, guest answers in one line. 🔴 **The guest is seen before being heard** (settled 2026-09-20): while the host names and thanks the guest, cut to a silent REACTION of the guest receiving it — a slight acknowledging movement from the profile's *gesture range*, gaze settling on him — covering his line from the thanks to its end and holding a beat. The guest's lower third opens on that reaction, and the reply **chains** from it. A welcome that cuts from him saying the guest's name straight to the answer skips the moment the audience actually meets the guest. Both brief, both in character, and **each in their own single** — the two-shot never carries dialogue (§7), and there is no wide here at all any more. This is also the guest's first appearance in the studio, which the removed establishing shot used to make. This is what gets the guest on screen inside the first forty seconds.
6. **First question.**

**The host does not state the disclaimer aloud.** The card, the description and Studio's "altered or synthetic content" toggle cover it. Saying it again in dialogue costs twelve seconds of the most valuable real estate in the video and tells the viewer nothing the card did not.

Measure the result: time-to-first-guest-word should be under ten seconds, and time-to-guest-on-screen-in-the-studio under forty. If either runs long, the cold open is too heavy.

## 0b. The last step of Mode 4 — build the episode's brand assets

**Mode 4 does not end with the kit. It ends with the kit *and* every per-episode brand render
sitting in the guest folder.** Added 2026-09-18.

```bash
python3 Fixed_Assets/Branding/intro_source/build_episode_cards.py Episodes/<Guest> [--part N] [--composite N]
```

**Why here and not at the edit.** By the time the kit exists, every one of these is already decided
inside it — §12 carries the lower-third names and the pull-quote lines with the shot each lands
over, the provenance tags carry the sources, the arc carries the next part's title. Leaving the
renders to Mode 6 means re-reading all of that at the edit and deciding it again, which is where
on-screen text drifts from what the kit says. **Decide once, render once, drop in.**

It writes into `Episodes/<Guest>/`:

| | from |
|---|---|
| `BRAND_endcard_p1.mp4` + `.png` | `card_data_p1.json` |
| `BRAND_lowerthird_host` / `_guest` | §12, with `_L` for the host and `_R` for the guest |
| `BRAND_pullquote_01..NN` | §12, one per key line, on the speaker's side |
| `BRAND_context_01..NN` | §12 *Context cards*, opposite the speaker, as the word is said |
| `BRAND_composite_p1.mp4` | `--composite N`, **eyewitness episodes only** |
| `CARD_PLACEMENTS.md` | which file goes over which shot |

Plates come out as **alpha `.mov` (QuickTime Animation) and alpha `.webm`**. The webm is there
because a 5-second full-frame RLE plate runs past 20 MB; both carry the same picture.

⚠️ **The design is series-fixed; only the render is per episode.** Builders live in
`Branding/intro_source/`. **Never write a render into `Branding/`** — a card carrying one episode's
sources, or a literal `[N]`, sitting in the fixed folder is how the wrong one gets used.

⚠️ **The sources block is audited, not generated.** `sources_audit.py` runs first and reports what
the provenance tags actually cite against what the card lists, in both directions. The tags name
sources in prose inside a sentence explaining the claim, so extracting them mechanically produces a
list with every passing mention in it. **The card is a curated claim; the tags are the evidence.**
Curate `card_data_p1.json` from the audit; the script writes a stub if it is missing.

---

## 0c. The test batch — first part of every new guest, before Pass 1

Added 2026-09-23. Some techniques in this file are **written but not yet proven on Kling**. Before the
full spend, the few clips that test them are generated first, judged, and the result folded back into the
skills. Runs **after the gates pass and before `round_sheet.py` Pass 1**, on Part 1 of a new guest only;
Part 2 inherits whatever passed.

**Pick the shots from the kit in hand by the criteria**, never from a list of old shot ids. Tests may
share a shot where they do not interfere (a rare name and a temperature change in one line tests T1 and
T2 together). The test clips are normal kit rows — generated once, they are kept if they pass.

| # | question | a shot qualifies if | status |
|---|---|---|---|
| T1 | Does a **`Pronunciation:`** paragraph make Kling say a rare name right? (else respell inside the quote) | its line contains a rare name, ideally a silent letter or shifted stress | **settled 2026-09-24 — respell inside the quote; the note is read aloud** (§3, 3b) |
| T2 | Does a **beat map** (§4 item 8) give each sentence its own temperature, without extra pauses or notes read aloud? | a guest line of 3+ sentences whose temperature shifts | **settled 2026-09-24 — yes; now the default. Pauses run long → duration model v3** |
| T3 | Does a **`SPLIT`** line read as one continuous line — and does lip-sync drift after ~5 s in the whole take? | a line ≥ 10 s whose mood turns at a sentence, ideally with something that can cover the seam | **settled 2026-09-24 (`P1_087`→`P1_088`) — yes: same pitch, flat join, reads as one line in Resolve (Salah); only a loudness step, levelled per the split level rule. No lip-sync drift seen in the long beat-map takes, so the control is dropped. A `SPLIT` is now a fallback for lines over 15 s or a turn the body must show — a beat map in one clip stays the default** |
| T4 | Does a **trailing `…`** play as a thought let go, not a stop? | the first line in the kit that uses `…` | open |
| T5 | Does a **`CUT-IN`** stop read as a real interruption, and does its start frame stay closed-mouthed? | the first `cut` / `seen` / `yield` interruption | **settled 2026-09-25 (`P1_044`→`P1_045`→`P1_046`) — yes (Salah).** The stop starts from the frame at the end of the cut word (extracted by Claude — Kling's feature gives only the last frame); his mouth, open in that frame, closes within ~0.4 s and stays closed. Her reply opened with **3.2 s of silence** before *"Allies"* — never on screen: the edit starts her audio ~0.3 s before the cut and her picture after the stop |
| T8 | Is Kling's **label form** (`Name (delivery): line`, from its audio guide) better than ours (`says, <note>: "…"`)? Added 2026-09-24 (Salah) | a seed-start beat-map line in no other test | **settled 2026-09-24 — the label form, with quotes kept, is the attribution** (§3) |
| T6 | Does a **two-up** hold up in motion — crop, eyelines, the listener clip's length? Since 2026-09-24 it carries every host reaction during the guest's speech, so test **both kinds**: a reaction over her talking, and a shared silence | the first two-up of each kind | **T6a settled 2026-09-24 (`P1_008` + `P1_009`, reaction beside her line) — passes:** native 955 px crops from the `_e` pair, heads level, eyelines meet across the divider, reads as one conversation (Salah). Crop used: host x=150, guest x=800 (1916-wide sources). **T6b (shared silence) failed 2026-09-24** — two faces only reacting read as empty (Salah). A two-up always has someone talking; a silence goes on her face (§8b, Two-up) |

A test that **passes** becomes the rule: mark it `settled <date>` here and remove any hedge from the
section it tested. A test that **fails** removes the technique from Modes 3 and 4 and is recorded in
`DECISIONS_ARCHIVE.md` so it is not re-proposed. A test with no qualifying shot in this kit stays open.

## 1. Pipeline

- Generation runs on **kling.ai**, image-to-video, 1080p. Clips are capped at 15 seconds. **The model is chosen per shot type** — there is no single default any more:

  | Shot type | Model | Rate |
  |---|---|---|
  | Talking clips (`INTERVIEW`, `NARRATION`, `INTERJECTION`) | Kling 3.0 **Turbo** | 10 cr/s |
  | **Audio-only talking clips** — the picture is never used (his line under her listening, an `OFFMIC`, a line wholly under b-roll). Added 2026-09-24 (Salah) | Kling 3.0 **Turbo at 720p** | **8 cr/s** |
  | `REACTION` | Kling 3.0 **Standard, audio off** | **8 cr/s** |
  | `BROLL_GEN` | Kling 3.0 **Turbo**, audio on | 10 cr/s |
  | `WIDE_CREDITS` (audio discarded) | Kling 3.0 **Turbo**, audio on | 10 cr/s |

  **For any clip with no dialogue, Standard with audio off is cheaper than Turbo** — 8 against 10.
  **A talking clip whose picture is discarded is generated at 720p** (Turbo, 8 cr/s, confirmed on kling.ai 2026-09-24): the voice is the same model's, and the voice pass treats it identically. The builder marks it from the row's `screen:` line (its own speaker never on screen, no two-up) and `round_sheet.py` groups those clips under their own setting. Cleopatra P1: 15 clips, 53 s, ~106 cr saved. Never use 720p for a clip that is on screen even partly. That inverts the assumption the earlier versions of this file were built on. Full reasoning and rates in `STUDIO_ASSETS.md`.
- **The stationary camera preset is permitted and used.** This reverses the previous instruction, which was correct only on Higgsfield, where camera presets bound the clip to Higgsfield DoP and took it off Kling. On kling.ai the preset is native and was validated in Test A. The `LOCK` paragraph is still pasted in full alongside it.
- **Every other Kling preset is forbidden on a dialogue shot** — everything under Shot type, Light and shadow, Frame and Atmosphere. They are not settings; they are literal text appended to the prompt, and each one describes something the seed frame already fixes. See `STUDIO_ASSETS.md` for the two that look safe and are not.
- Every dialogue shot uses a **seed frame as the start image** — `frame_host`, `frame_host_direct`, `frame_guest`, `frame_wide_both`. The seed frame carries identity, wardrobe, room, lighting and framing. The prompt never describes any of them.
- Camera plates and character reference sheets are upstream tooling: they exist to make seed frames, and are referenced directly only for B-roll extras, who have no seed frame.
- Dialogue audio is generated natively inside the clip. The same pass produces ambience and diegetic effects, so B-roll arrives with its own sound. Suppress the model's default music bed in every prompt.
- 📖 **Platform detail lives in `skill_elevenlabs.md`** — rates, limits, and what the voice pass
  does and does not preserve. One trap worth carrying here: **the speech-to-speech model must be
  set explicitly to `eleven_multilingual_sts_v2`.** The API default is English-only and switches
  silently.
- **Vocal identity comes from ElevenLabs, not the video model.** Every talking clip goes through a speech-to-speech pass against the character's registered voice ID in `Fixed_Assets/VOICES.md`. Tested: picture and lip-sync survive untouched. This is a standard pipeline stage now, not a repair — it runs on all 65 talking clips, never on reactions (silent), b-roll (no dialogue) or the wide (audio discarded).
- **The prompt's voice block still matters, but its job shrank.** Speech-to-speech maps timbre onto the *source* delivery, so the generated voice must still be a clean, correctly-timed performance in roughly the right register — a badly mismatched source gives a poor result. Keep the registered descriptions byte-identical as before. Timbre and register no longer have to be right, only close — **the accent does, because it is not replaced (next point)**. So the full block — sex, age, timbre, register, accent placement, manner — is written into every talking clip even though the voice pass follows.
- ⚠️ **Accents belong in the KLING prompt's `Voice:` block — this was backwards until 2026-09-18.** It used to say accents belong in the ElevenLabs voice. They do not, and the host clone proved it: accent is carried by phonetics — vowel targets, consonant realisations, rhythm — and speech-to-speech takes all of those from the **source read**, which is the Kling clip. The ElevenLabs voice contributes timbre. A clone recorded in Egyptian Arabic returns native English precisely because the source read was native English. **So whatever accent Kling generates is the accent that survives to the cut**, and the `Voice:` block is where it is decided. Write it there, identically in every clip for that character, and keep the registered ElevenLabs description consistent with it. **A chosen accent is named plainly in that block, Kling-style** (*"with a light Greek accent"*) — the *never say "accent"* rule applies only to the ElevenLabs design description. Full wording rules: `skill_mode2_cast.md`, *"How to write a chosen accent"*.
- Keep the raw Kling clip alongside the processed one. If a voice is ever redesigned, raw clips can be re-processed; a discarded original means regenerating video.
- Generate an entire part in one resolution and one model tier, under identical platform settings. Record the settings; a change to them mid-part changes the performance for no visible reason.
- **Download every accepted clip into the episode folder the day it is generated.** Both platforms reserve the right to delete stored content without notice and owe nothing for it, and a lapsed subscription can take account access with it. The generated clips are the raw material of the part — the platform is a renderer, never a library.

## 2. Duration and Word Budget

> 🔴 **CURRENT MODEL — v4, 2026-09-25 (L21, L24):**
> **duration = lead (0.8 s seed / 0.3 s chained, +0.7 s for a pose entry) + syllables ÷ 4.3 + 1.3 s per sentence
> break or dash + 0.4 s tail, + 0.5 s on any line that needs 9 s or more, then rounded UP (never down) to a whole second.**
> Why: `P1_016` (need 4.06 s, rounded down to 4 s) ended 0.15 s after its last word; `P1_015` (34 syllables, 12 s)
> was cut off mid last word with her mouth still open — her pauses ran 1.45 / 1.6 s and she spoke at 4.1 syl/s.
> Across the kept takes sentence pauses average ~1.3 s. Spare time only costs a trim in the edit; a clip that is
> too short costs the whole clip. **Mode 6 runs `batch_check.py` over the part; a TIGHT flag means
> listen to the last word.** `syl.py` carries v4 — every builder, `lines_check` and `script_read` use it.
>
> **v3, 2026-09-24: the break allowance is 1.0 s, not 0.5 s.** Measured on the test
> batch: `P1_013` took 1.1 s at its sentence break, `P1_020` 1.6 s and 1.0 s, and two clips in a row ran their
> speech to the **last frame** — no tail to cut on, so a regeneration. Rate and lead-ins held (4.3–4.5 syl/s).
> Surplus silence costs a little credit and is trimmed in the edit; a missing tail costs a whole clip.
> `syl.py` carries v3; the v2 text below is kept for its measurements.
>
> **v2, 2026-09-21 (superseded by v3's break value only).**
> Measured on six Kling Turbo clips (`P1_004/006/007/055/057`, `P1_008`): the model speaks at **~4.3
> syllables/s** (4.1–5.4), opens with **~0.8 s** of silence from a seed frame (0.3 s when chained), and
> spends any slack as one long pause. So a clip is built, never padded:
>
> **duration = lead (0.8 s seed / 0.3 s chained) + syllables ÷ 4.3 + 0.5 s per sentence break or dash + 0.4 s tail**, rounded **up** to the next whole second; +0.5–1 s only where a written gesture needs room.
>
> Implemented as `syl.dur2()` in **`Fixed_Assets/tools/syl.py`** (series-wide copy, 2026-09-22; the
> original stays in `Episodes/Cleopatra/_v1_archive/_kit_source/` for that kit's build scripts). The old **3.85 syl/s + 1 s per break** figures
> below are superseded; they came from the previous platform and over-padded every clip by 1–2 s.
>
> **Re-measured per guest — added 2026-09-22.** The rate is a property of the *voice*, and two voices
> (this host, one guest) is all it was measured on. An older, slower or more rapid-fire guest will not
> match. So for every new guest, the **first three to five talking clips of Pass 1** are generated,
> measured (speech rate, lead-in, pause per break) and written into the guest's *duration calibration*
> in the `CAST.md` performance profile **before the rest of Pass 1 is generated**; if the guest rate
> differs from 4.3 by more than ~10%, recalculate that guest's rows. The host's rate carries over.

Testing established roughly **two spoken words per second**, assuming one internal sentence break. So:

- duration in seconds ≈ words ÷ 2
- add one second for each sentence break beyond the first

Validated points: 21 words at 10s, 15 words at 8s, 14 words at 7s.

**Never round the duration up.** Slack is not safety margin — the model paces to fill whatever it is given, spends the surplus dwelling at a sentence break, then compresses the tail, and compressed speech is exactly where lip-sync breaks down. Set the duration the line actually needs.

**Budget by syllable, not by word — the word count is only the first pass.** The model's constraint is syllables, so a line can pass the word budget and still fail.

**The model does not speak slower when given more time. It speaks at a fixed rate and pads with pauses.** Measured off the finished clips: 25 syllables in 6.40s of speech, and 27 syllables in 7.11s — **3.8 to 3.9 syllables per second**, effectively identical across both characters. Every second beyond that becomes silence, and the model chooses where to put it, usually by stretching one sentence break.

So duration is built, not guessed:

- **speech** = syllables ÷ 3.85
- **+ ~1s per sentence break** — the model takes these whether or not you want them
- **+ ~0.5s tail**

That total is the **floor**, and going under it is what causes the compressed tail. **Aim for the floor plus half a second, rounded to the nearest whole second.** Going far over is not free either: a 27-syllable line given 13s ran a 3.3-second dead pause mid-line, because the surplus had to go somewhere.

The pad was +1s until a 27-syllable line with a 9.5s floor was generated at 10s — a +0.5s pad — and came back clean, tail included. Tightening it takes about 30 seconds off an eleven-minute part, which is real money at every part from here. If a clip does come back rushed at the tighter pad, give that clip a second rather than loosening the rule for all of them.

The model predicts every result so far. 25 syllables floors at 9.0s — clean at 10s, and at 12s the surplus showed up as a 1.8s pause. 27 syllables floors at 9.5s — at 13s it produced a 3.3s pause. The line that failed everywhere was 34 syllables, floor 11.3s: impossible at 10s and barely inside 12s, which is why it compressed at the tail even when the clip looked long enough.

Two checks before any line is committed:
- **Density.** Above roughly 1.6 syllables per word, the line is too heavy for its word count and needs rewriting, not more seconds. Adding time spreads across the whole line; the compression is local.
- **Tail weight.** The last sentence must not carry a disproportionate share of the clip's syllables, and **a clip never ends on its densest word.** Compression lands at the tail, so the final few words are the ones that must be short and open. Where a line can be reordered to end lighter without losing its meaning, reorder it: "no me without Egypt, and no Egypt without me" ends on an open monosyllable where the reverse ends on two syllables, and reads stronger for her besides.
- **Surplus belongs at the end, never the middle.** Slack shows up as dwelling at sentence breaks, so a pause mid-line is the failure while a beat of silence after the last word is just a natural moment before the cut. A slightly generous duration on a line with few sentence breaks is therefore safe — the surplus has nowhere to go but the end.

Even a well-budgeted clip degrades slightly on its final word. That is why the tail cutaway earns its keep twice: `edit_placement`'s "covers the tail" form was written to hide the beat between one line ending and the next beginning, and that span is exactly where the mouth is weakest. Where the edit wants a reaction anyway, put it there.

This makes the Latinate abstractions this show runs on — independence, position, legitimacy, negotiation — mid-line words. Never the last beat. "Or was that the moment Egypt stopped being free?" works where "Or was it the moment independence started being traded for position?" failed on two platforms, three durations and four prompt revisions: same meaning, 12 syllables instead of 21, and the last three words are monosyllables.

Dramatic pauses are cheaper at cuts than inside clips. A silence between two shots costs nothing; a silence inside one costs words.

**A list of names runs long — measured 2026-09-24 (`P1_013`, T1).** *"Hebrews, Arabs, Meeds, Parthians"*
at the end of a line: the model took **1.1 s** at the sentence break before it (the model allows 0.5) and
slowed through the commas, so the speech ran to the **last frame** of an 8 s clip — the picture ends on
the final word and there is no tail to cut on. That is a **duration** failure, not a broken generation.
**Add 1 s to any clip whose line ends on a comma list of three or more names.** And a clip whose speech
reaches its last frame is always regenerated one second longer, never used as is.

**One beat, one clip — changed 2026-09-22 from "one utterance, one clip".** A clip carries one delivery
and about one gesture well; when a line *turns* inside a single clip, the model averages the two moods.
So: **a line with one mood stays whole.** A line whose mood **turns at a sentence**, or with a gesture
that must land on **one word**, **may be split** there into two clips — where the moment deserves it
(the crack, a key line, a long line with a turn; Mode 3 marks it `SPLIT`). The old objection — *"the
pose resets to the seed frame at the join"* — died with chaining: the second half **chains** from the
first, so the pose carries over exactly.

**Building a `SPLIT`:**
1. **Split only at a sentence break, never mid-sentence.** A small shift in pitch or energy between two
   takes sounds natural at a full stop and wrong in the middle of a clause. The ElevenLabs pass makes
   the timbre identical; the prosody comes from each take.
2. **A** ends on its sentence, duration from the v2 model. **B** is `chain from A` (0.3 s lead), its own
   duration. Each half gets **its own delivery note and its own single gesture** — that is the point.
3. **Every split row names how the seam is hidden** in `edit_placement`, best first: **(a)** a cutaway
   across the seam — a reaction of the listener, a b-roll, or an off-camera line — with A's audio running
   into B's underneath; **(b)** a `PUNCH` exactly on the seam; **(c)** a plain cut on the pause, relying on
   the chained pose and the join grade.
3b. **Level the two halves as one — measured 2026-09-24 (T3, `P1_087`/`P1_088`).** Pitch matched exactly
   (193 Hz both sides) and the picture join was clean (luma −0.4%, face difference 2.5), but B came back
   **~6–7 dB louder** than A — partly the written arc (*quieter → the decision*), partly take-to-take level.
   Per-clip loudness normalisation would flatten the arc and still leave a step; so the edit **normalises
   the pair together** (one gain for both), then trims any remaining step at the seam to **≤ 3 dB**.
4. **Budget:** ~1 s (~10 cr) extra per split for B's lead-in and tail; the edit trims both. A split
   counts as a chain link — never more than three links.
5. ⚠️ **Untested as of 2026-09-22.** Test T3 (§0c). Adopt widely only once a split reads as one
   continuous line.
6. **A line past the 15 s cap is split by Mode 4 even when Mode 3 did not mark it** — added 2026-09-23.
   The v2 duration can exceed 15 s on a line the outline wrote whole (Cleopatra P1: the cold-open narration
   at 15.8 s; her thesis at 15.0 s, which is the cap and leaves no room). The words do not change: split at
   the sentence where the delivery turns, chain B from A, and name the seam cover. On direct address the
   only cover is a plain cut on the pause (never a `PUNCH` there). A line of 13–15 s stays whole unless its
   mood turns. `lines_check.py` now prints a `LONG` warning for any outline line over 15 s, so Mode 3 can
   mark the `SPLIT` itself.

## 3. Prompt Architecture

Every speaking shot is built in this order, and only the middle two parts change between shots:

1. **Camera lock**, verbatim: "The camera does not move. Framing, lens, lighting and background stay exactly as the start frame throughout."
2. **Register and delivery**, in prose, outside the quotation marks, as its own short paragraph.
2b. 🔴 **Attribution form — settled 2026-09-24 by T8 (`P1_006`): Kling's label form, quotes kept.**
    `The woman (cool courtesy): "Thank you." The woman (plain): "It is rare that I am asked."` — one label
    and one bracketed delivery per sentence in a beat map, the label repeated for each segment, a physical
    beat (no quotes in it) between segments where the body moves. A/B on the same line and seed frame
    against `The woman says, cool courtesy: "…" Then, plain: "…"`: the label form gave a clearly different
    delivery per sentence, visible in her face (Salah). Quotes stay — they mark where speech starts and stops,
    and every gate reads them (`outline_lines.kit_spoken` accepts both forms). What follows about the older
    `says` form is kept for its reasoning.
2d. 🔴 **The bracket holds a simple Kling tone — never the outline's note. Added 2026-09-24 (Salah).**
    Kling's own examples read `(softly, in a surprised tone)`, `(in a low voice, agreeing, in a calm tone)`:
    one to three plain manner words. Our outline notes (*"personal, then the decision stated"*, *"quieter,
    then personal, the ceiling holding"*, *"the premise"*) are directions for a person, not for the model —
    job labels, metaphors and "then" give it nothing to play, and a "then" inside one bracket asks one
    sentence for two deliveries. So the builder maps every outline note through
    `Fixed_Assets/tools/tone_map.py` (shared by every guest — add new notes there) to a Kling-style phrase: *in a dry tone*, *plainly*,
    *quietly, in a serious tone*, *in a low, firm tone*, *in a coolly polite tone*. Rules for a mapping:
    manner words only (volume, pace, warmth, firmness); no "then", no job labels, no images; at most
    three words or one "in a … tone". **The build stops on an unmapped note** (`STOP — no Kling-style
    tone…`) — add the mapping, never pass the raw note. The outline keeps its own wording for Salah's read.
2c. **Attribution, immediately before the quote.** Kling's own dialogue guidance is to keep each speaker's line close to the character name, and fal's is that character labels must be consistent and pronouns avoided. So the register paragraph ends, and a short attribution — `The host says, <note>:` or `<guest label> says, <note>:` — sits directly against the opening quotation mark. **The guest label is the *prompt label* in the `CAST.md` performance profile** (Cleopatra: `The woman`; a male guest: `The man`, or `The old man`, `The soldier`…), fixed for the whole arc; every gesture and reaction line uses the profile's pronouns. Never copy a label or pronoun from another guest's kit. A long register clause wedged between the speaker and their line is the arrangement the vendor guidance warns against.
3. **The line itself**, in quotation marks, kept clean. No bracketed cues inside it — they get read aloud.
3b. **Pronunciation — respell the word inside the quote. Settled 2026-09-24 by test T1 (`P1_013`).**
    A name the model is likely to get wrong is written **as it sounds** inside the quoted line (*Medes* →
    *"Meeds"*, *Ptolemies* → *"Tolemies"*); the **Subtitle** field keeps the true spelling. Plain letters
    only — no capitals, hyphens or stress marks inside the quote (they are read or paused on). The kit's
    Pronunciation table carries a **Respell** column; the builder swaps the word in the prompt only.
    ❌ **Never a separate `Pronunciation:` paragraph.** Tested: Kling read it aloud as dialogue — the host
    said *"Medes"* twice (`shots/_tests/T1_A.mp4`). The respelled take (`T1_B.mp4`) said it right. Kling's
    own guides say nothing about pronunciation (checked 2026-09-24), so respelling is the method.
    A name with no safe respelling is left as written and **checked by ear on the take**; retake with a
    respelling if it comes back wrong — the ElevenLabs pass cannot fix it.

📖 **Vendor syntax, read against ours — 2026-09-20.** Kling's own audio guide says: *"Put each
speaker's name, line, and delivery note close together"*, with the delivery note **inside the
attribution** — *"the male lead says in a relaxed tone, '…'"*, or the label form
*`Mom (softly, in a surprised tone): …`*. It also names ambience in the same prompt (*"a faint hum of
the living room air conditioner"*), allows up to four speakers, supports dialects and accents stated
in the prompt, asks for simple grammar and short lines, and says the **speaking face must stay
readable** for lip-sync. Our structure already satisfies most of that — register beside the
attribution, ambience in the audio paragraph, accent in the `Voice:` block, one speaker per clip, a
locked mid-shot. **Two differences are worth testing rather than assuming:**

| ours | vendor form | why it might matter |
|---|---|---|
| register as its own paragraph, then `The host says: "…"` | delivery note *inside* the attribution: `The host says, level and without endorsing it: "…"` | brings the delivery note as close to the line as the guide asks, without losing the paragraph's negative instructions (*"never hardening"*) |
| no timing cue; every clip so far opens with 0.7–1.0 s of silence | vendor uses temporal markers (*"Immediately"*) to control speech sequencing | if *"He begins speaking immediately."* removes the lead-in, it buys ~0.8 s of runtime per clip — about 8 credits each, and a tighter cold open |

⚠️ **Do not rewrite the kit for either.** The current form is validated across six clips. **Test both
on one Act A clip** against the same seed frame and line: measure speech-onset time and listen for
register drift. Adopt only what measures better, and record the result here either way.

📏 **RESULT 2026-09-21, `P1_008`, same seed and line, 11 s each.**
| | A (inline note only) | B (+ *"He begins speaking immediately."*) |
|---|---|---|
| speech onset | 0.60 s | 0.35 s |
| voiced time / rate | 7.15 s · ~5.0 syl/s | 6.65 s · ~5.4 syl/s |
| pauses | 1.1 · 0.6 · 1.2 s | 1.3 · 2.2 s |
**Timing cue NOT adopted.** It bought 0.25 s of onset and gave it straight back as a longer pause,
while the line itself ran faster — the one outcome the test was written to reject. The inline
delivery note (take A, kept as `P1_008`) stays the format; its 0.6 s onset is also shorter than the
0.7–1.0 s seen before, which is inside the v2 lead-in allowance.

4. **One gesture**, described in its own sentence and anchored to a specific moment in the line.
5. **Voice block** — the character's registered voice description from `STUDIO_ASSETS.md` (`@voice_host` for the Host, `@voice_[name]` for the guest), pasted byte-identical. Never reworded, never shortened, never written from memory. The Host's voice is permanent for the life of the series; a guest's is fixed from their Mode 2 casting through both parts. Registered voices carry no pace language by construction — if one does, fix it at source in `STUDIO_ASSETS.md` rather than trimming it per shot.
6. **Audio block**, verbatim: "Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo."

**Never state pace anywhere in a prompt. Duration is the pace control.** Twenty-one words in twelve seconds *is* an unhurried delivery — the model has no other option. Telling it to be unhurried on top of that does not make it more measured, it makes it spend the budget early and compress the tail. Register direction covers tone and attitude only: never speed.

## 4. Register — the single most important rule

The model infers emotional register from the *content* of the line when the prompt does not state it, and the content-inferred default is always more dramatic than this show wants. An accusatory question gets played as an accusation. **Every speaking shot states its register explicitly.**

The host's default register is curious, level, pressing without prosecuting — an interviewer, never an interrogator. **The guest's default register is not written here — it is the *default register* and *emotional ceiling* in the performance profile of `Episodes/<Guest>/CAST.md`** (Mode 2, added 2026-09-22). Cleopatra's is composed and unapologetic, never pleading; another guest's will not be. These defaults live in the locked blocks; per-shot direction only ever states a deviation.

**The guest default inverts on composite eyewitness episodes.** "Composed and unapologetic" is honest for a monarch defending decisions they actually made; on a conscript or a junior official it manufactures apologia. Those guests run the **testimony register** instead — uncertain where the record shows uncertainty, silent where they did not know, caught out where the documentation catches them out, and never composed in a way the source material does not support. See `skill_mode1_pitch.md`, Eyewitness episodes, for the full rule set; the difference is settled at pitch and casting, and Mode 4 only executes it.

**Scope the constraint to tone, never to movement.** "His tone stays level throughout, never hardening or rising into accusation" works. "Holds the same pace and intensity from first word to last" freezes the body along with the voice.

Charged content is where escalation appears, and escalation means speed, and speed is where mouths fall apart — so the most dramatic lines are the most technically fragile. Direct them hardest.


### How to write an emotion — 2026-09-20

Kling's guide invites plain emotion words (*"in a surprised tone"*, *"excitedly"*). They work, and
that is the problem: a bare emotion noun is played at full strength, which is the content-inferred
default this section exists to control. So emotions are written, but **always as a manner plus its
ceiling**.

1. **Prefer manner words to emotion nouns.** *Level, dry, flat, unhurried, courteous, precise,
   careful, plain* describe how a person speaks. *Angry, sad, excited, devastated* describe a
   performance, and the model performs them.
2. **Name it, then say where it stops.** *"Dry, and never amused."* *"Level, and never hardening into
   accusation."* *"Steady, and it does not break."* The second half is what keeps HBO realism out of
   melodrama, and it is the half a vendor example never has.
3. **One step at a time.** Where a beat genuinely escalates, raise it one notch and state the
   ceiling: *"the voice lifts on the last clause and stops short of anger."* Two descriptors is the
   maximum; three is a mood board, and the model averages them.
4. **The strongest feeling is usually written as restraint** — a person holding something down reads
   as feeling more than a person letting it out, and it is far safer technically: escalation means
   speed, and speed is where lip-sync breaks. *"She says it as though it costs nothing, and her voice
   stays low"* beats *"bitterly"*.
5. **Emotion lives in the delivery note, never in the quote** — no bracketed cues, no capitals, no
   exclamation marks inside the line; they get read aloud or over-performed.
6. **The body carries the rest, as observable movement only** (§5 and the project's visual rule):
   *"her hand stops where it is"*, *"his knuckles press against his jaw"* — never *"she looks
   shocked"*. On a silent REACTION the body is the *only* channel: name the held state (*composed,
   unreadable, still*) plus one observable movement.
7. **Keep a character's register vocabulary stable** across the part. A guest who is *low and level*
   throughout, deviating twice, reads as a person; one described with a fresh adjective every shot
   reads as an actor being re-cast each clip.
8. **The beat map — one delivery per sentence, in one clip. This is the default, and the cheapest.**
   Added 2026-09-22. Mode 3 gives every multi-sentence line a beat map (job and temperature per
   sentence). The prompt carries it the way Kling's own guide writes multi-speaker scenes — speaker,
   delivery note and words kept together — except that **every segment is the same speaker**, and **a
   physical beat may sit between two segments** where the body should change:
   `The woman says, coolly correcting him: "You assume those were two things." Then, plainly: "For me they were one." She lifts one hand slightly from her lap. Then, with weight held under: "Egypt did not survive without me." She lets the hand settle. Then, quieter: "And I was nothing without it."`
   - **One clip, one generation, no seam, no extra credits** — the same cost as a single-note prompt.
   - **Physical beats between segments: one or two per clip at most**, taken from the guest's gesture
     range. Most segments carry voice only. Five actions in one clip is fidgeting (§5).
   - Each delivery note is manner-plus-ceiling and small; the register paragraph above still sets the
     frame. When a beat map is used, the separate gesture paragraph is dropped — the beats *are* the
     gestures.
   - **`SPLIT` (§2) is only for a turn too big for one clip** — where the body or the whole performance
     must change, or the line is past ~12 s. It costs a second clip and a seam; the beat map costs nothing.
   - ✅ **Settled 2026-09-24 by T2 (`P1_020`):** each sentence took its own delivery and nothing was read
     aloud. **The beat map is the default** wherever the outline gives one delivery per sentence
     (`note1 → note2 → …`, same count as the sentences) — the builder derives it from `OUTLINE.md`. Where the
     counts differ, the single delivery note stays. Budget the breaks with the current duration model (v4: 1.3 s a break; it paused
     1.6 s and 1.0 s between segments in T2). Each segment's note should be a **manner** (*dry, level, quieter*),
     not a stage label (*"the premise"*) — Mode 3 writes them that way.
   - ✅ **The parsers read every segment — fixed 2026-09-23.** `outline_lines.kit_spoken()` joins all the
     quoted segments of an attribution paragraph and drops the stage text between them; `junction_scan.py`,
     `lines_check.py`, `publish_sheet.py` and `script_read.py` use it. Physical beats between segments
     must carry **no quotation marks** (write *On the last word*, not *On "king"*), or they read as speech.

## 5. Gesture — settle versus advance

Gestures that **settle** read as ease: a weight shift, a hand opening and returning to rest, a slow breath, a small head tilt, settling back into the chair. Gestures that **advance** read as pressure: a lean-in, a hand pushing forward, a chin lifting, a gaze narrowing.

🔴 **Never name a blink — anywhere, in any prompt. Settled 2026-09-20.** Naming a blink does not
produce *one* blink; it makes blinking the subject of the clip. `P1_056` (*"blinks slowly once"*)
came back blinking constantly and obviously; `P1_007` (*"blinks once at the end"*) measured about
four blinks in seven seconds, several half-closed. The model blinks at a natural rate on its own —
the instruction only amplifies it. The same probably holds for any autonomic action written as a
count (*"once"*, *"slowly"*), so for an involuntary beat use a **breath or a settle**, and for
stillness describe the **held pose**, not the eyes. The pre-generation gate checks it.

## Respellings come from the outline table, never a hand list (2026-09-27, Salah, L48)

The kit builder reads every `write: X` from the outline's Pronunciation table and writes X inside the quote (subtitles
keep the real spelling). Cleopatra Part 1 had a hand-kept list of two (Medes, Ptolemies), so *Arsinoe* would have gone to
Kling raw, and the stress homograph *"Allies."* in `P1_046` came out wrong. `prompt_check.py` L48 fails a raw `write:` word
in a spoken quote, a table row with no `write:`/`plain` decision, and a lone stress homograph with no row.

## Every talking prompt says where the eyes stay (2026-09-28, Salah, L57)

`P1_028` looked into the lens on its last sentence (*"an edge comes into the last sentence"*). Only 16 of 93 talking prompts
named the eyeline. The builder now ends every talking prompt's action paragraph with *"Her eyes stay on the person
sitting opposite her, off frame to the left, from the first word to the last."* (host: *his / him / right*) — positive
wording only; naming the lens would invite it. Direct-address clips and the turn clip are exempt. `prompt_check.py` L57.

## Never "toward him / toward her" — name the side of the frame (2026-09-28, Salah, L58)

`P1_028` turned to the lens on its last sentence **twice**, even with the eyeline line (L57). On `frame_cleopatra_i` its
gesture was *"she turns a fraction further toward him"* — the old `_d` gesture was a chin lift, and never turned her. With
no one else in the frame, Kling reads *him* as the viewer. Every movement toward the other person names the side: guest
*"toward the left of the frame, where the person opposite her sits"*; host *"toward the right of the frame"*. The pose
tables are rewritten this way; `prompt_check.py` L58 fails *toward him/her* anywhere before the Voice line.

## Choosing a pose for each row — from the library (2026-09-27, Salah, L47)

The guest's `poses.py` is the pose library: each pose has `rank` (withdrawn→engaged), `use` (the beats it serves) and
possibly `only='react'`. For each guest row: match the row's delivery note to a pose's `use`; don't give the same person the
same pose on two consecutive shots unless the second is chained; move at most ~2 `rank` steps across a cut unless the line
turns hard; `only='react'` poses never start a talking clip. Spread the library across the part — every pose should appear.

## Silent reactions — never leave the model an empty clip (2026-09-27, Salah, L42)

Every silent reaction ends on **one small one-way move and a closing stillness** — *"Her chin lifts a fraction; otherwise
she is still."* / *"…nothing else moves."* The kept reactions all had one; `P1_003a` had none (it ended on a held pose)
and added *"as she is named to the room"* — both takes came back with movement from someone off frame, as if the camera
operator moved. A reaction with nothing to do lets Kling invent motion elsewhere; a phrase that implies other people
(*the room, an audience, everyone*) gives it someone to invent. `prompt_check.py` fails both.

**Every silent reaction has an END FRAME = its own start image (2026-09-27, Salah, L44).** All twelve kept reactions
were made with the same frame in both slots; `P1_003a` was the first without (the builder only set the end frame when
the next clip chained from it) and failed 4/4 with the host pushing into the corner. The end frame pins the whole
picture, so nothing can wander in. Seeded reactions: the seed in both slots. Chained reactions: the source clip's extracted last frame in **both** slots — even when it ends with the lips a little
parted; held for a few seconds it reads as listening, on the point of answering. (L45, ending on the seed instead, was tried
on `P1_047` and withdrawn the same day: a different end image makes the model morph between the two — Salah.) The builder writes it on every reaction; the round sheet shows it.

**A reaction that keeps failing is cut from one already kept (L43).** `P1_003a` still failed four times after that fix — every
take had a blurred shape (the host) pushing into the bottom-left corner on `frame_cleopatra`, while every kept reaction on
`_b`/`_e` was clean (`batch_check.py` flags it `CORNER`). After two failed takes of a short silent reaction, stop paying:
cut the length needed from a kept silent reaction of the same guest, **same pose as the shot on the other side of the
cut** if there is one, from a part of the episode far from it. A 1–2 s silent face does not read as a repeat.

## Generating — on kling.ai, chip OFF (Salah, 2026-09-26; chip dropped 2026-09-27, L51)

🔴 **Every clip is made on the Kling website with the camera chip OFF** — the v3 prompt holds the camera by itself
(b-roll never had it).

🔴 **Batches through the Kling CLI — in waves (2026-09-27, Salah, L52).** Claude runs
`python3 Fixed_Assets/tools/cli_wave.py Episodes/<Guest> --max N`: it lists the clips that are READY (seed start, or
chained from a clip already kept in `Shots/`), extracts each chained clip's start frame from its source's last frame into
`Shots/start_frames/<ID>_start.png` (`-sseof -0.08`, no scale, no lift — Kling's own last-frame image), and prints the one
`node Fixed_Assets/tools/kling_run.mjs …` command. Salah runs it on the Mac (running it = approving the spend); takes land
in `Shots/_tests/`. Salah looks at them; Claude moves the kept ones to `Shots/`, which makes the next wave (their chained
clips) ready. Settings come from each sheet header: Standard audio off (reactions, same image as `--tailImage`), Standard
audio on, Turbo 720p (audio only), Turbo 1080p. B-roll goes through the CLI too (2026-09-27, L54): `kling_broll.mjs <Guest> stills <ids>` (Kling image 3.0, 16:9, 2k → `Shots/stills/`), Salah looks at the stills, then `kling_broll.mjs <Guest> video <ids>` (Turbo 1080p from each still → `Shots/_tests/`). First wave: five mixed clips, to confirm
the v3 prompt holds the camera through the CLI as it did on the website. The round sheet lists every clip with its settings; paste each
block whole. **Save each take you are happy with straight to `Shots/<ID>.mp4`**; a retake replaces the file.
Chained clips start from the source clip's last frame with **Kling's own last-frame feature**.

🔴 **No per-take checking by Claude during generation** — Salah judges each take by eye; routine checks cost Claude
usage for little gain with the chip on. Claude measures a take **only when asked**, or when something must be
measured before the next clip can be made: the frame at a **`CUT-IN` cut word** (below). Loudness, pauses, lead-ins,
tight endings and small drifts are all handled at the **start of the edit** — Mode 6 runs `batch_check.py` once over
the whole part, and ElevenLabs speech-to-speech re-renders every voice anyway.

**The Kling CLI — tried and set aside (2026-09-25, LESSONS L20–L32).** It worked mechanically (clean downloads via
`urlWithoutWatermark`, same prices as the website, one command per batch), but it cannot set the stationary chip and
Turbo has no end frame through it: long clips drifted about half the time and short still clips about 1 in 7, with no
motion words in their prompts. The checking and retake rounds cost more than the clicks they saved. The tools stay in
`Fixed_Assets/tools/` (`kling_run.mjs`, `batch_check.py`, `cam_check.py`) — the script is unused unless Kling adds a
camera-lock option to its CLI; the two checkers are used by Mode 6.

🔴 **A `CUT-IN` stop starts from a frame inside the source clip, not its last frame** — Kling's
last-frame feature cannot give it. Claude times the cut word on the take and extracts that frame to
`Shots/start_frames/<ID>_start.png`, and the row reads `chain from <src> at <s>s` (2026-09-24, `P1_045`).
**A hand-written gesture (`gest_text`) names no body contact** — the start frame is picked after it is
written, and `P1_046`'s *"fingers lift from the armrest"* landed on a hands-in-lap pose; the pose
table's `avoid` list now fails that in `pose_check.py`.

🔴 **The clip ledger.** A kept clip lives at `Episodes/<Guest>/Shots/<ID>.mp4` — that file IS the record;
`clip_status.py` reads the folder and lists kept / to do and the credits left. `CLIPS.md` holds notes only where
there is something to say (a take kept with a known flaw, a retake reason, `REGEN <ID>`). A retired row keeps its
number empty so later clips keep their names.

🔴 **Every prompt is written from the pose table — never from memory of the frame. Added 2026-09-24 (Salah).**
`Fixed_Assets/tools/poses.py` (the Host, permanent) and `Episodes/<Guest>/poses.py` (written in Mode 2)
hold, for every seed frame: what it shows, its **hold** (the pose, held — the builder inserts it into
every silent reaction from that frame), an optional **entry** (what happens as a talking clip from it
begins), and its one-way **settle / advance / still** gestures. The builder reads the table; a frame
with no entry stops the build; `pose_check.py` fails a kit whose prompt drops a hold or an entry or
names a repeatable gesture. Change a pose's wording in the table, never in one prompt.

🔴 **A hand at the face comes down before the words. Added 2026-09-24 (`P1_084`, `frame_host_d`).** A talking
clip that starts from a pose with the hand against the jaw or chin says, in the register paragraph, that he
lowers the hand as he begins and it stays down — a jaw moving against resting knuckles is a lip-sync risk.
A silent reaction from that pose says the hand **stays** there. And every beat-map prompt keeps the row's
pose hold (*"His fingers stay resting against his jaw…"*) as its own paragraph — the builder had been
dropping holds that carry no anchor word (fixed 2026-09-24; 19 prompts in P1 got theirs back).

🔴 **The same holds for any gesture that can repeat — nod, head shake, tilt-and-return, look away and back,
hand up then down. Settled 2026-09-24 (`P1_009`, T6a).** *"A slow nod starts and stops almost at once;
then he is still"* came back nodding for the whole clip (Salah). Kling does not play a gesture once and
stop; it makes the named gesture the clip's activity and loops it. So a reaction names only **a move into
a position that then holds** — *her chin lifts a fraction* (passed in `P1_019`), *he sits back a fraction
and stays there*, *his jaw sets and stays set*, *his eyes crease with a laugh and stay creased* — or plain
stillness. A nod the edit needs is not generated: a still listener beside her line in a two-up already
reads as agreement. The gate above greps for the common offenders.

Same energy, opposite reading. Calm register takes settling gestures. Advancing gestures are reserved for moments that genuinely escalate — which makes intensity something directed rather than something that ambushes the shot.

**One gesture per clip, anchored to a moment in the line** ("on the second question", "on the last three words"). Unanchored gestures float; two gestures in a short clip read as twitching.

### The enhancer is gone — and so far that has cost nothing

Kling 3.0 Turbo has no prompt enhancer. Under Kling 3.0 it was ON and was filling in physical detail nobody wrote — it once had a guest point at herself on the word "me".

**Do not pre-emptively rewrite gesture paragraphs for this.** `P1_054` was generated on Turbo with the existing wording and came back with natural hand movement. That is the only evidence there is, and it says the paragraphs as written are already sufficient. Rewriting a validated prompt on a theory is how a working result gets broken.

Losing the enhancer is arguably a gain: the prompt reaching the model is now the prompt we wrote, so byte-identical blocks are genuinely deterministic and a whole class of unexplained mid-series drift disappears.

**Repair kit, for a clip that actually comes back wrong** — stiff, or inventing idle fidget. Applies to that clip only, and only to block 4:

1. **State the resting state** — what hands, forearms and shoulders do when they are *not* doing the gesture. "Hands staying folded in her lap" (Cleopatra) suppresses invented motion — describe the guest's own resting state from the seed frame.
2. **State the connective movement** — how the body arrives at the named beat and leaves it, not just the beat.
3. **State one involuntary beat** — a breath or a settle. **Never a blink** (see below).

Still one *deliberate* gesture per clip. These are texture, not extra beats: five actions in a four-second clip produces fidgeting, which is worse than stiffness.

**Sound is not written here.** Movement foley is thinner on Turbo — a hand returning to a chair arm came back near-silent. Accepted, not a defect to prompt around: the audio spec is dialogue-clean with minimal ambience, generated foley varies clip to clip and is harder to cut around than silence, and a room-tone bed runs under the whole part. A movement that must be heard is placed in the edit.

## 6. Writing the Dialogue

- **Short sentences.** Long compound clauses joined by dashes read well on the page and generate badly. Kling's guidance says the same in its own words: "Simpler grammar often leads to better results. Break complex sentences into shorter dialogue lines."
- 🔴 **Check the consonant junctions — HARD RULE since 2026-09-20, enforced by a script, no exceptions.**
  `python3 Fixed_Assets/tools/junction_scan.py Episodes/<Guest>/P<n>_kit.md` must print nothing before
  any clip is generated. It flags a word ending in a stop (/p b t d k g/, alone or closing a cluster)
  running straight into a word whose opening vowel carries primary stress, using the CMU Pronouncing
  Dictionary vendored beside it; proper names it lacks go in `Fixed_Assets/tools/names.dict`.
  Punctuation counts as a release; weak function words (*a, an, and, it, of, in, I* …) do not count
  as stressed. **It used to be advice, and advice was not applied:** Part 1's kit reached the
  generation step with 21 such junctions in 17 clips, including the validated pair's `P1_055`
  (*"moment Egypt"*). All were rewritten on 2026-09-20. A line that "worked once" with a junction is
  not an exception — the rule is cheaper than finding out which ones fail.
  ⚠️ **Found 2026-09-22: this gate went blind for a day.** When attributions moved to the inline form
  (`says, level and dry: "…"`), the scanner still looked for `says: "…"`, found **no lines at all**, and
  reported a clean kit. Re-run with the fix, Part 1 is genuinely clean. The scanner now **fails** if it
  finds fewer spoken lines than talking rows. **Any gate that parses the kit must count what it checked
  — a gate that silently checks nothing looks exactly like a pass.**
  **Fixes that keep the meaning:** a pronoun for a just-named noun (*"Not him."*); a word ending in a
  vowel, fricative or nasal before the name (*"with Antony"*, *"as Antony's lover"*, *"countries
  Antony"*); move the name to the start of a sentence; or a sentence break (*"Thirty-one BC, off
  Actium."*).
  **The last word of a clip is the other weak spot — added 2026-09-24 (T8).** A line ending on a word-final
  **stop cluster** (*described* /bd/, *marked* /kt/, *worked* /kt/) strained the mouth on that word in both
  takes. **Rule since 2026-09-24 (Salah): Mode 3 rephrases, with no exceptions** — `lines_check.py` fails the
  outline on every one (`TAIL-OK` withdrawn), and a `TAIL` warning in the kit means the outline was not fixed. Mode 4 never rewords one itself — it goes back to the outline.
  One phrase, "without Egypt", failed five times: at the end of a 12s clip, a 13s clip and a 7s clip, throughout the sentence when reversed, and again in the *middle* of an 8s clip — which is what ruled out both duration and position as the cause. Changing four letters fixed it: "without it" generated clean, same duration, same start frame, same everything else.

  The junction is a word-final stop landing directly against a stressed vowel — the mouth must release a plosive straight into a wide open vowel — compounded by a final `/pt/` cluster closing the word. When writing a line, read it for that shape: a word ending in **t, d, p, k, b, g** butted against a stressed vowel, and word-final clusters like **/pt/, /kt/, /st/, /ks/**. Rephrase at the writing stage, where it costs nothing, rather than discovering it at the generation stage, where it costs 30 credits a time. A pronoun standing in for a just-named noun usually dissolves the junction without touching the meaning.

  This is the first thing to suspect when a specific patch of a line keeps failing across changes of duration, position and phrasing. Everything else we tried was a global fix for a local problem.
- **No mirrored or repeated constructions.** A chiasmus ("no Egypt without me, and no me without Egypt") makes the model articulate two near-identical phoneme sequences back to back, and alignment can slip across the whole figure rather than at one point. Observed failing in both orderings. Say the same thing with two different constructions instead.
- **Vendor troubleshooting worth knowing:** dialogue that cuts off or rushes is documented as script-too-long-for-duration, fixed by shortening the script rather than lengthening the clip. Three or more speakers in one generation produces unreliable voice attribution — never write one.

**Unverified, do not design around yet:** third-party reporting claims lip-sync decouples progressively in clips beyond about 5 seconds, independent of word count, because the model's facial representation fluctuates across generation chunks. If true it would argue for short chained clips over one long one, which contradicts "one utterance, one clip". Not vendor-documented and not tested here. Worth a dedicated experiment — the same line at 12s versus split across two chained 6s clips — before anything is changed. **2026-09-22: folded into the `SPLIT` test on `P1_070`** (whole take against the two halves), in the test plan.
- **Questions end as questions.** A trailing clause after a comma parses as a statement however it is punctuated. Two clean interrogatives beat one long one, and a note that the voice lifts at the end helps.
- **Put the charge, don't make it.** "Or the moment you traded your country's independence" is a verdict wearing a question mark, and even a level delivery carries it. Attribute the proposition and invite an answer instead — the content stays hard, the posture stays interviewer.
- Sentence breaks create audible pauses. Budget them; don't fight them.
- **Pronunciation goes in the prompt, not beside it** — see §3, block 3b. A note beside the shot never reaches the model, and the ElevenLabs pass cannot correct a name Kling mispronounced. (Until 2026-09-22 this line said *"note pronunciation beside the shot"*, which meant nothing controlled pronunciation.)

## 6b. Provenance and the Knowledge Gate — audited before anything is generated

Mode 3 assigns a provenance tag to every line. Mode 4 **carries those tags into the kit and audits them before a single clip is generated**, because a factual error found after generation costs credits to fix and a factual error found after publication costs the show's positioning.

| Tag | Meaning | Requirement |
|---|---|---|
| **[D] Documented** | attested in the record | the source is named on the line |
| **[I] Inferred** | consistent with the record, a reasonable reconstruction | the basis is named |
| **[V] Voice** | connective tissue, rapport, phrasing, transitions | carries no factual claim |

**Hard rule: a [V] line may not contain a factual assertion.** Read down the tag column before generation and check every [V] line for smuggled facts — a date, a place, a number, a claim about what someone did. That is where invention leaks into the parts an audience will believe.

### 🔴 Generation gate: no VERIFY survives into a clip — settled 2026-09-18

**Before any clip is generated, grep the kit for `VERIFY`. A single hit stops the run.**

```bash
grep -n "VERIFY" Episodes/<Guest>/P<n>_kit.md | grep -vi "cleared" && echo "STOP — unresolved claim in a spoken line"
```

⚠️ **The `| grep -vi "cleared"` is load-bearing.** A resolved flag stays in the provenance tag as
**`VERIFY CLEARED <date>`** — the finding is worth keeping, and deleting it would invite the same
claim being re-flagged later. So the convention is: **`VERIFY` alone is live and stops the run;
`VERIFY CLEARED` is a record and does not.** Without the filter the gate fires on its own history
and gets ignored, which is worse than not having it.

**Second check on the same pass — and keep it proportionate.** This is not a citation audit of
every line. Scan the *spoken* lines for **falsifiable specifics**: numbers, dates, kinship or
titles, "who did what to whom", and absolutes like *first*, *only*, *never*. Those are what a critic
can look up and disprove; texture and phrasing carry no exposure.

Each falsifiable specific in a `[D]` line needs respectable support named in its tag — a primary
text, a modern academic book, or a scholarly reference work. If it does not have one, **the cheapest
fix is almost never a rewrite**: retag `[D]` → `[I]` and let the guest own the claim. A character's
characterisation cannot be a lie; an assertion by the programme can. No line change, no
regeneration. See Mode 3, *"the cheapest safety valve: give it to the guest"*.

```bash
# how many spoken lines even contain a checkable specific
grep -oE 'says[^"]*: "[^"]+"' Episodes/<Guest>/P<n>_kit.md | \
  grep -inE '\b([0-9]+|one|two|three|four|five|ten|twenty|hundred|thousand|father|mother|brother|sister|cousin|never|always|only|first)\b' | wc -l
```

On Part 1 that came to **14 lines out of 66, and only 4 of them `[D]`** — two of which were the
VERIFY flags. The job is small when it is aimed at the right thing.

Mode 3 is not allowed to emit one (see its three exits: verify it, cut the unverifiable precision,
or retag `[D]` → `[I]` and let the guest own the claim). This grep exists because one slipped
through anyway in Part 1 — twice — and sat for weeks as work parked on the person least able to do
it mid-edit.

**The cost asymmetry is the whole argument.** The flag is on a *spoken* line. Resolved at outline
it is a text edit and free. Resolved after generation it is a regeneration plus a voice pass —
130 credits on Part 1's `P1_019` — and resolved after publication it is a correction on a channel
whose entire positioning is that it does not need them.

⚠️ **Re-read the whole line, not the flagged word.** Part 1's flag said *"'cousin' is loose"*. The
kinship was indeed wrong by a generation — but the same sentence asserted a **contested will** as
documented fact, which the flag never mentioned and which was the larger exposure. A flag records
where someone felt uneasy, not the extent of what is wrong there.

⚠️ **Re-run the duration model on any line you change.** *"A winter"* is one syllable longer than
*"Four months"*, which pushed a 9s clip past its floor to 10s. Cheap to catch here, a reroll later.

The kit's published source list is **generated from the [D] and [I] tags**: nothing cited that is not used, nothing claimed that is not cited. A sources block assembled separately from the script is a claim the script cannot back.

**The Knowledge Gate** (full text in `skill_mode3_outline.md`) is re-run here on the written dialogue, because lines change between outline and kit:

1. **Is this in the right mouth?** The guest speaks from outside their own life and knows what was said about them since — but posterity's framing, modern vocabulary and scholarly interpretation belong to the **host**. The guest answers from experience and never cites a source.
2. **Did the event happen the way the line describes it** — the right method, not just the right place and date?
3. **Is a named specific available instead of a vague one?** Vagueness is where errors hide. *"Octavian's forces have landed in the delta"* passed every other check in this file and was wrong — he advanced overland from Syria and took Pelusium. *"Octavian has taken Pelusium"* is both accurate and better writing.

## 6c. Write prompts unwrapped — one line per paragraph

**Kling strips newlines without inserting a space.** A prompt hard-wrapped for readability arrives at the model with words fused at every line break — `frame.Soft`, `zoom.The` — and the person pasting it has to repair it by hand, every clip, every part.

**Every paragraph inside a prompt block is one unbroken line.** Paragraphs are separated by a blank line; nothing else wraps. This applies to the kit, to prompts written in chat, and to anything pasted into a generation field. Never reflow a prompt to make it look tidier in a narrow column — the readability is worth nothing and the cost is paid on every single paste.

The canonical blocks (`LOCK`, the voice descriptions, the audio paragraph, the charcoal style block) are already written this way. Keep them that way when copying them.

🔴 **Paragraph breaks are stripped too — so every paragraph after the first starts with one space.**
Found 2026-09-21: pasted into Kling, *"…the camera contributes none.The host, calm…"* — the blank line
between paragraphs vanishes and the sentences fuse. A fused boundary reads as one run-on block, and
the movement paragraph visibly lost force: adding a single space before it (`P1_008_B`) made the
movement land as written. A **leading** space survives copy-paste from a code block and from a file
where a trailing one is often trimmed, so the separator lives at the *start* of each paragraph line.
**Paste from the kit or the round sheet, not from chat** — chat rendering can drop spaces inside a
paragraph as well (*"stationary.Locked"*). `round_sheet.py` enforces the leading space.

## 7. Camera and Continuity

🔴 **Prompt structure v3 — camera + lighting — THE structure since 2026-09-27 (Salah, L51). Chip OFF.** Tested by hand
on ~15 Cleopatra clips with the stationary chip **off** (talking up to 13 s, reactions, and the `P1_046` retakes): the camera held
on every one (0 px), and brightening across a clip averaged ~1.4 % against ~1.8 % before. Every studio prompt is, in order:
1. `Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.`
2. ONE paragraph: `Only one person is in the frame.` + the direction + the lines and gestures;
3. the `Voice:` line (talking clips); 4. the `Audio:` line;
5. `Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.`
No leading spaces, no other camera words. The builder writes it (`LOCK`, `ONE`, `CONT`, `para()`); `prompt_check.py` L51 checks
the opening and the closing. Because it needs no chip, **the CLI can make studio clips again** (see *Generating*).

~~Camera lock v1 (2026-09-26, L33) — superseded by v3 above.~~ It opened with, verbatim:
> The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

followed by *"Only one person is in the frame."* (L19 — it stopped her knee wandering into his shot; kept by Salah), and
nothing about the camera anywhere else (no closing "Static camera shot").
With the website's *"the camera is stationary"* chip on, the newer v2 wording below still drifted; v1 + chip held on
every clip made before the experiments. The theory that naming *pan / tilt / zoom* invites them (L18) did not hold up
with the chip on — do not re-open it without a measured A/B on the website. `prompt_check.py` L3 checks the opening.
The v2 / v3 history below is kept for the record only.

**Camera lock v2 — 2026-09-25 (`P1_058`).** Every studio prompt opened with
> Static camera shot. The camera is stationary on a tripod; the framing, lens, lighting and background stay exactly as in the start frame for the whole clip.

— followed by *"Only one person is in the frame."* (L19) — and ends with **"Static camera shot."** (the builder appends
it to the audio line). **No camera-move word anywhere in the
prompt, even negated** — the v1 lock (*"zero pan, zero tilt, zero travel, zero zoom … All movement in the shot belongs to
the person"*) named four moves, the same trap as naming a blink or a nod (LESSONS L5, L18); third-party Kling guides say the
same (lead with "Static camera shot", repeat it, never use motion vocabulary). `P1_058` with v2 and **without the web chip**: background drift ≤ 2 px over
the clip, measured — **the prompt alone locks the camera**, so the CLI/MCP (which have no chip) can make studio clips.
Every take is measured with `cam_check.py` (≤ 3 px = held). `prompt_check.py` L3/L18 enforce both. The v1 text below is kept for its history only.

**Write the camera lock positively, and lead with the vendor's own phrase.** Video models handle negation badly — "the camera does not move" contains the word *move*, and it was ignored in testing, producing a slow drift. Kling ships **"The camera is stationary."** as a preset in its prompt directory, which makes it phrasing the model was tuned against rather than something invented here; Higgsfield's camera guide independently phrases every lock affirmatively (*"locked tripod bolted in place, zero rotation, zero travel"*). The canonical `LOCK` paragraph opens with theirs and keeps the rest, because the short phrase alone does not hold framing, lens and lighting:

> The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot belongs to the person; the camera contributes none.

That last clause is not decoration. A lock stated as pure absence of motion freezes the performer too — the same failure as scoping a register constraint to movement instead of tone (§4). Always name where movement **is** allowed. Never stack two different camera formulations in one prompt; they fight.

### Custom saved presets — considered and dropped

Kling's prompt directory accepts custom entries, and the idea was to save the blocks that must never vary — `LOCK`, `@voice_host`, `@voice_[guest]`, the audio paragraph — so the tool enforced byte-identity instead of care.

**Not pursued.** The blocks live in the kit, inserting a preset is no harder than pasting the block, and hand-pasting avoids a class of invisible-input problem: a preset that silently reformats or appends text puts us back where the prompt enhancer did, with the prompt reaching the model not being the prompt we wrote. Prompts are pasted by hand.

The one preset that *is* used is Kling's stationary camera preset, alongside the full `LOCK` paragraph rather than instead of it. **Measured 2026-09-24 (`P1_020`, first take): without the preset the camera moved despite the full `LOCK` paragraph** — so the preset is doing real work, not belt and braces. This settles what Test A could not separate. Never generate a dialogue or reaction clip without it.

**The camera lock in this file is the whole mechanism**, so it is worth getting exactly right — and keeping it in the prompt rather than in a platform setting is what lets the kit move to another platform unchanged.


- `frame_host` and `frame_host_direct` are Host-only; `frame_guest` is Guest-only. The Host occupies the left armchair and faces screen-right, the Guest the right armchair facing screen-left. This never changes.
- `frame_host_direct` is for direct address to the audience only — cold open, narration to camera. Never for dialogue with the guest.
- 🔴 **Never cut straight between a direct-address frame and a cross-shot of the same character — in either direction.** Into the studio (the hook handing off to the guest) or out of it (a sign-off turning from the guest to camera): the same fault, mirrored.
  `frame_host_direct` and `frame_host` are the **same camera, same framing, same chair** — only the
  eyeline differs. Cutting between them moves the eyes and nothing else, which reads as a glitch
  rather than a change of address.

  🔴 **Scope: this applies ONLY to a direct-address shot joined to a cross-shot of the same
  character.** Every other join — reaction → speech, a split utterance, anything within one
  address — keeps the **proven chain method** below, unchanged. Start+end frames are not a
  replacement for chaining; they solve the one join a chain handles worst, where the whole point of
  the cut is that the eyeline *changes*. Decided 2026-09-19.

  **Pose pairs — same body, only the eyeline differs.** Use these as the start/end pair so the
  model only has to turn a head:

  | direct address | cross-shot | shared pose |
  |---|---|---|
  | `frame_host_direct` | `frame_host` | settled back, forearms on the armrests |
  | `frame_host_direct_b` | `frame_host_b` | leaning forward, forearms on thighs, hands clasped |
  | `frame_host_direct_c` | `frame_host_e` | settled back, hands clasped in the lap |

  Going **out** to camera, reverse the pair: start on the cross-shot, end on its direct partner.

  **The fixes for that join, best first:**

  1. **Set the next shot's start frame as this shot's END frame.** Generate the direct clip with
     start `frame_host_direct_*` and end `frame_host_*`, and open the next shot on that same
     `frame_host_*`. The last frame of one clip is then the first frame of the next — **a
     pixel-identical join**, both ends anchored to vetted seed frames, no extraction, no chain
     luminance loss, and both clips can generate in parallel. **Pair the variants by body pose**
     so only the head has to turn: `direct_b` → `host_b` are the same lean with a different
     eyeline. Motivate the turn with the line — he turns to the guest as he hands off.
  2. **Chain** — start frame only on the direct clip, then start the next from its end frame. Proven.
  3. **Cut mid-turn** onto a fresh seed frame — the eyeline matches, but the pose can jump.
  4. **Put something between them** — the guest's reaction, or b-roll.

  🔴 **RESULT 2026-09-20: fix 1 is unavailable on Turbo — Turbo has no end-frame slot. Fix 2, the
  chain, is the default for this join on every talking clip.** `P1_004` ran it: the prompt alone
  produced the head turn (9.5–11.0s, motivated by the line, not rushed), the body stayed in the
  direct pose, and the chained join measured seamless in luma. So write the turn into the prompt and
  chain; do not reach for a second seed frame.
  🔴 **CURRENT RULE — 2026-09-27 (Salah, L40): the turn clip is on Turbo, and it always cuts away to the guest.**
  The direct-to-guest turn goes on **Kling 3.0 Turbo, audio on, no end frame**; the prompt says where the eyes go in frame
  terms and spreads the turn over the sentence (L38), but its end point is left to chance — on Turbo it heads the right way
  and overshoots. **Nothing chains from a turn clip.** The builder inserts a **short silent guest reaction (3 s, Standard,
  audio off, from a seed)** right after it; the edit cuts to her as the turn lands (~1.5 s on screen — it doubles as her
  first look), and the host's next clip starts from the **built guest-facing seed** (`host_b`), whose eyeline is right.
  A row added after clips exist takes the previous number plus a letter (`P1_003a`, the builder's `ADDED`) so nothing
  downstream is renumbered. Neither an end frame nor retries are spent on landing the eyeline.
  ~~L39 (superseded the same day): the direct-to-guest turn is on Kling 3.0 Turbo, audio on, no
  end frame, and the next clip chains from its last frame.~~ Two Standard + end-frame takes of Cleopatra `P1_003` both
  failed (the head snapped across in dead air), and each retry cost more than a Turbo retry. So: write the eyeline in
  **frame terms** read off the guest-facing seed (for this host: *a small, slow turn toward the right side of the frame,
  just past his microphone, eyes level at seated head height*), spread it over the whole sentence with no pause before it
  (L38), and keep hands and shoulders still. When a take lands, the next host clip starts from **its last frame**
  (Kling's last-frame option), not from the seed frame — the join is exact whatever pose he ends in. If the gaze ends
  visibly off the seed pose, check the last frame against it before the chained clip is made. If Turbo misses twice,
  the fallback costs nothing: he says line 1 to the lens, the introduction plays over the guest's face, and we cut back
  to him already facing her.
  ~~Changed 2026-09-26 (Salah): the direct-to-guest turn uses fix 1 after all — on Kling 3.0 Standard with audio**
  (12 cr/s), which has the end-frame slot Turbo lacks: start = the direct clip's last frame, **end = the guest-facing
  pose of the same lean** (`direct_b` → `host_b`), and the next clip starts from that seed frame (exact join). On Turbo
  the eyeline after the turn landed where luck put it (Cleopatra `P1_003`: right once, off to the left on the retake).
  One clip per part, +2 cr/s. The builder does it with `turn_end` on the row; the round sheet shows the end frame.
  ~~Fix 1 is unproven on a talking clip — after the gate, update this line either way.~~ Start+end frames are proven on silent clips — the draw-ons and `BRAND_bumper_out`. On
  dialogue the end-frame constraint may make the model rush the line to reach the pose in time,
  and it is not yet confirmed that **Turbo** accepts an end frame. Give the clip a second of
  headroom over its floor, and fall to fix 2 if it fails.
  🔴 **Write the turn slow and spread over the words (2026-09-26, Salah, L38 — still applies on Turbo).** Cleopatra `P1_003` on Standard + end
  frame: the model finished the line, went silent, snapped the head across in ~0.5 s (torso and hands shifting with it),
  then held 1.5 s before the second sentence — too fast and in dead air. The turn line must say: *no pause between the
  sentences; the head turns slowly, the turn takes the whole second sentence, eyes arriving on the last word; hands and
  shoulders stay where they are.* If a take still snaps in silence, don't regenerate first — Mode 6 retimes it.

  ⚠️ **This was hidden until 2026-09-18.** The 4s establishing wide used to sit between the hook and
  the welcome and absorb the eyeline change. **Removing the wide exposed a join that had always
  been there**, which is the kind of second-order consequence a structural deletion produces: the
  thing you removed was doing a job nobody had written down.

- **One beat, one clip, one angle** (see §2 — a `SPLIT` may divide one line into two chained clips on the *same* angle). Each angle is a separate generation with its own performance and its own audio — there is no matching take to cut to, the way there would be with real multi-camera coverage. Cutting between angles mid-utterance puts two different performances of the same line against each other and cannot be fixed by prompting. An angle change is therefore only ever a turn or a time break. Chained clips must stay in the same angle for the same reason: chaining exists to hold one utterance together.
- **THE WIDE NEVER CARRIES DIALOGUE.** This is structural, not a preference about reliability. ElevenLabs speech-to-speech converts a clip to **one** voice, so a two-speaker clip comes back with both characters sounding identical. A two-shot can carry a conversation as *picture*; it can never carry it as *dialogue*. Any line that must be heard is a single.

  *(The old note calling the wide "the least reliable generation in the kit — two characters in one clip is where voice attribution fails" was answering the wrong question. Attribution is irrelevant when the track is discarded, and the closing wide additionally sits under music and a credit roll, which makes it the most forgiving picture in the kit rather than the least.)*

- **`WIDE_SILENT` — retired as live video, 2026-09-18.** The kit generates no two-shot clip at all. The two-shot survives as the **still** that opens `BRAND_bumper_out`: `frame_wide_[name]_marked.png`, which already exists as a seed frame.

  **Why.** The scale fault described in §0 item 4b — figures a size too large against the chairs, inherited from the seed frame and so immune to rerolling. A four-second hold shows it; a one-second beat before a charcoal transformation does not, and the charcoal then removes the photographic reference the eye was judging scale against. So the shot is kept exactly where it survives and dropped everywhere it does not. **An empty studio wide was considered and rejected** as a replacement: it proves nothing about the two people, and the shot only ever worked because it landed after the host was already seated and speaking.

  ⚠️ **The act break is `BRAND_actbreak` — fixed furniture, zero credits a part.** A 4-second study drawing itself on the page, under the theme's own first 4.0 seconds, cut out exactly on 4.000 so the next act's first frame lands on the next strike. Two clips made once and alternated; **not** a wide, and **not** a charcoal scene, because all b-roll in this show is charcoal and a charcoal scene at a break is invisible as a break. The page is the one register the b-roll never uses. Full spec in `Fixed_Assets/SERIES_FURNITURE.md`.

  **Nothing is generated per part for a break, and nothing is edited.** The clip length is the break length. `MUSIC_Sting_Transition` is dead — the theme's own strike is the sting, same instrument, free.

- **The two-shot appears exactly once, at the close.** It is still the only thing that shows host and guest in the same room — without it the show is two singles intercut that never prove they share a space — but it does that job as the first frame of `BRAND_bumper_out` rather than as a clip at the top, and it costs nothing extra there because that frame already exists. **32 credits a part** come out of the kit with the establishing clip. It also reads better: the one picture of the two of them together arrives at the end, as it is becoming a drawing, in a show about reconstruction.

- 🔴 **The outro wide is built per part, from references (2026-09-28, Salah, L59).** The old per-guest wide was generated with
  both people in it and came out a size too large for the chairs, and its host pose never matched his last line — he speaks
  last, so the jump showed. Now, per part: (1) **Seedream, three references in order** — `cam3_wide.png` (room, chairs,
  camera), the host's **last clip's** pose frame, the guest's **last clip's** pose frame — the builder writes the prompt with
  both poses filled in; *no character sheet* (the pose frames gave the better likeness); (2) `outro_mark.py` composites the
  mark at the fixed panel coordinates; (3) charcoal end frame on **Kling Image 3.0, 2K**, image-to-image, the series style
  block + the composition lock; (4) the 5 s transformation, Standard audio off, v3 camera paragraph, no lighting paragraph.
  The round sheet lists the outro in full until `Shots/<id>.mp4` exists — it was once missed because the sheet skipped it.
- **The close is `BRAND_bumper_out`: the two-shot turns into a charcoal drawing of itself on camera**, and the credit roll runs over the drawing. ~~Built per part from `frame_wide_[name]_marked.png`~~ (see the rule above) — the seed frame, not a frame lifted from a clip — one charcoal pass (~3 cr) plus a 5s start→end transformation (40 cr), then the last frame is held under the credits. **~43 cr a part**, against 150 for the per-part talking wide it replaces, and no two-character generation anywhere in the kit. Prompts and rationale in `Fixed_Assets/SERIES_FURNITURE.md`.

- **`WIDE_CREDITS` — the per-part closing roll. Superseded by `BRAND_bumper_out`; kept here as the fallback** if a future format wants the characters visible under the credits. Turbo, audio on, **audio discarded entirely** in the edit, with `MUSIC_Outro_Bed` and the credits over it. Give the two of them a natural continuing conversation so the model animates a real performance; since nothing is heard, invented mouth movement is *on brief* here rather than a fault. **Write no dialogue lines and no `Voice:` blocks into this prompt** — they exist only to drive attribution that is being thrown away, and two voice blocks in one prompt is an unnecessary failure mode. Describe turn-taking instead: one speaks while the other listens and acknowledges, then the turn passes back, two or three turns across the clip.
  A clip caps at 15s, so a longer roll is two chained wides — same angle, so chaining is legal.
  **This is a candidate for replacement by a fixed series outro** built once and reused for every guest, which would remove it from the per-part budget entirely. Until that exists, the wide fills the slot.
- **A row inserted into an existing kit takes the previous id plus a letter** (`P1_006a`) — ids already worked against (chains, §12, `CARD_PLACEMENTS.md`, generated clips) never shift. All tools accept the suffix. A kit built fresh is numbered contiguously.
- **Seed frame or chain, decided by what the cut is.** A fresh seed frame is correct at a genuine turn — the other person speaks, or time passes — because the pose reset reads as a new moment. It is wrong inside a single continuous utterance, where the character visibly snaps back to the neutral pose mid-sentence. An utterance that genuinely must be split is therefore **chained**: each clip's `end_image_url` becomes the next clip's start frame, and any reaction inserted inside that utterance is chained through as well.

  🔴 **End-frame rule — settled 2026-09-24 (`P1_086`, Salah's idea).** A silent reaction that starts from a
  **seed frame** and is followed by the same person speaking is generated with **Standard's end-frame slot set
  to that same seed frame**; the speaking clip then **starts from the seed frame itself**, not from the
  reaction's last frame. Measured side by side: the end-frame take held her eyeline on the host throughout,
  its last frame matched the seed (face difference 4.1 against 9.4 without), and there was no rushed return —
  the last half-second was the calmest. Left free, her gaze sank in both `P1_019` and `P1_086`. The cost: about
  half the small movement (a stiller listener — right for a listening shot, especially a two-up half). What it
  buys: an exact join with no extraction and no grade, and 11 fewer chains in Cleopatra P1 (40 → 29), so those
  clips can be generated in any order. The kit writes `` `end_frame` `<seed>` `` on the row and
  `round_sheet.py` prints **END FRAME** in the sheet. Reactions that start from a *chained* frame keep the chain.

  **Batch process — settled 2026-09-20.** Only rows marked `chain from` need an extracted frame; every
  other row starts from a seed frame and can be generated at any time. So a part is generated in
  **two passes**, never shot by shot:
  1. **Pass 1 — everything with a seed frame**, including every chain *source* (in Part 1 those are the
     reactions `P1_041`, `P1_056`, `P1_092`). Drop the clips into `Episodes/<Guest>/shots/` named by id.
  2. **Extract all chain frames at once:**
     `python3 Fixed_Assets/tools/chain_frames.py Episodes/<Guest> <part>` → `shots/start_frames/<TARGET>_start.png`,
     named after the shot that **uses** the frame, extracted with the approved ffmpeg command only.
     It lists any source still missing and never overwrites an existing frame.
  3. **Pass 2 — the chained shots**, each uploading its `<TARGET>_start.png`.
  4. **Run the script again** — with the chained clips present it measures every join (luma and chroma,
     last frame vs first) and flags any that needs checking at the cut.
  **Never use the platform's extract-frame button or a screenshot for a chain frame** — that is where the
  +7.1% chroma jump at `P1_004` → `P1_006` came from.

  📏 **MEASURED — and corrected 2026-09-21.** Every clip generated so far starts **3.3–4.0% darker in
  luma than the image it was given** (host seed −4.0%, guest seed −3.3%, and the first properly
  extracted chain, `P1_056` → `P1_057`, −3.3% with chroma flat at −0.3%). The earlier reading of
  −0.4% at `P1_004` → `P1_006` was **confounded**: that start frame was not our extraction — it came in
  with +7.1% chroma and, it now appears, brighter too, which cancelled Kling's loss. **So the loss is
  real, per link.** 🔴 **Settled 2026-09-21: level it in the EDIT, not before generation.** Predicting
  the shift (pre-lifting) failed once already and would fail again the day the platform changes;
  measuring what actually happened cannot. `chain_frames.py` extracts the start frame with the approved
  ffmpeg command, unmodified (`LIFT = 0`), and once the chained clip is back it writes
  **`shots/_measure/JOIN_GRADES.md`** — one per-channel gain per chained clip
  (`colorchannelmixer=rr=…:gg=…:bb=…`), applied to the **whole** clip in the edit. It handles brightness
  and colour-range shifts in one filter (it reproduced the hand-tuned `P1_006` fix exactly). Only
  same-camera joins need it. **What an edit grade cannot fix** — and why the extraction rule and the
  three-link cap stay: clipped highlights or crushed shadows (the lamp, the dark panels — detail that is
  gone), a *local* change (the face warmer but the wall not), a change in sharpness or grain, and any
  change in *content* — pose, framing, light direction. Those need a regeneration, so the chain is
  still kept short.
  **Which frame to upload — settled 2026-09-21: Kling's own last-frame feature is the default.** Its
  only measured fault (+7.1% chroma at `P1_004` → `P1_006`) is a uniform colour shift, which the join
  grade removes, and it saves a download–extract–upload round trip per chain. The script's extracted
  frame (`shots/start_frames/`) is the **fallback** — use it if a Kling-extracted frame ever shows a
  *content* fault (softness, compression blocks, a crop or resize). Either way every clip is saved to
  `shots/` and `chain_frames.py` measures the join against the source's true last frame.

  ⚠️ **Kling extracts the end frame natively and applies it as the next start frame, in-app — no download, no re-upload.** That path may retire both procedures below, because both were workarounds for faults introduced by *our own* extraction and by measurements taken on a different platform. **Do not delete them until measured.** At the first real chain of a part, compare the mean luma of the source clip's last frame against the new clip's first frame. If they match, both procedures go and the three-link cap can be reconsidered — the cap exists because the loss accumulated. If they do not, the procedures stand as written. Note especially that pre-lifting a frame to compensate for a loss that is no longer happening would make each link progressively *brighter*.

  **Extract chain frames without a colour-range conversion.** A generated clip is limited-range video; a PNG is full-range. An extractor that converts between them stretches values away from centre, which lifts saturation by roughly 7% — invisible when the frame is viewed on its own, obvious the moment the two clips are cut together. The generator then reproduces the shifted frame faithfully, so the fault is impossible to see in the prompt or the output and looks like generation drift. Measured: a correctly extracted frame reads 14.66 saturation against the source clip's 14.72, while a range-converted one reads 15.82 — and the clip generated from it started at 15.84.

  **Chains accumulate a luminance loss — limit chain depth to three links.** Measured down a real chain: the source plate reads 79.62 average luma, the first generated clip 78.81, the second 77.50, the third 75.76. That is roughly 1.5% darker per link, about 4.9% over three, and it compounds indefinitely. Adjacent links differ by too little to see, which is exactly why it goes unnoticed until a late clip is cut against an early one. Re-anchor to the seed frame at every genuine turn and never chain more than three deep.

  **The loss cannot be prompted away** — the generator reproduces its start image faithfully (proved three times over), so a darker clip means it was handed a darker frame. No wording changes that. Fix it where it happens instead: **pre-compensate the extracted frame.** Measure the extracted PNG against the chain's first clip and lift it by the difference before it becomes the next start image, so each link enters at the original level and nothing accumulates. The loss is consistently around 1.1% per generation plus a little more in extraction, but measure rather than assume the constant. Correcting in the edit afterwards also works and is the fallback where a chain already exists.

  The platform's own extract-frame button did the conversion. Extract with `ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png` and no scale filter, then confirm the frame's saturation matches the source clip before generating from it. Every clip started from a Seedream plate lands 1-2% *below* its start image, so anything reading above its source is a conversion artefact, not the model. Better still, avoid the situation — keep utterances to one clip and place reactions at turns rather than inside a thought.
- **Read both pose registers before assigning anything.** The Host's is in `STUDIO_ASSETS.md`; the guest's is in `Episodes/[Guest Name]/CAST.md`, written at casting. Each says what a variant is and what it is for. Selection is a judgement about the beat, and it is not possible from filenames.
- **Select a pose variant for every fresh start frame.** Each seed frame is a set (`frame_host`, `frame_host_b` …). Never the same variant twice in a row for a character, and never the same one within three of their appearances. Choose it from what the beat is doing rather than at random — leaning forward for a question being pressed, settled back for a light one, hand near the jaw while turning something over. Random selection repeats by chance, which is the artefact being removed; a fixed cycle becomes its own pattern.
- A fresh variant is only correct where the character has had time to move — the other person spoke a full utterance. Across an interjection or a two-second reaction they cannot have changed posture, so chain instead. This is the same turn-versus-chain test as above; the variants only stop "fresh frame" meaning "identical frame".
- Never generate a new pose variant during production. The library is fixed before the part begins.
- Vary the cutting rhythm. A fixed cadence reads as mechanical.

## 8. Shot Types

- `INTERVIEW` — a character speaking on their seed frame.
- `NARRATION` — Host speaking on `frame_host_direct`, video later covered by B-roll. Bound by the same word budget as any other beat; long narration is consecutive clips sharing the voice block.
- `REACTION` — a character listening, silent, `generate_audio` off. **How a silent reaction is written — changed 2026-09-24 after `P1_019`:** describe the held mouth
  **positively** — *"Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly
  and quietly through her nose."* Never name what must not happen (*"no talking, no mouthing"*), never
  set a conversation in motion (*"listens to him"*, *"as the question reaches her"*), and never write a
  visible breath (*"one slow breath"*). `P1_019` (Standard, audio off, the old wording) came back with an
  open-mouthed exhale — mouth-area motion ~2× the passing reaction test. Same lesson as the blink rule:
  naming a thing makes it the subject. **Always state the eyeline too** — *"Her eyes stay on the person sitting opposite her, off frame to the left"* (host: *to the right*): the `P1_019` retake kept its mouth shut but let her gaze drift off him, and a chained clip inherits wherever the eyes ended. ⚠️ Verify on the `P1_019` retake; the model stays Standard with
  audio off (Turbo's audio track made the mouth invent speech — A5b). The cheapest shot available and the only one with no lip-sync risk at all. **Generate a distinct reaction for every use.** Reusing one reaction clip twice within a short span reads as an obvious repeat — the same blink, the same movement, at the same tempo — and it draws more attention than the cut it was meant to smooth.
- `BROLL_GEN` / `TITLE_CARD` — as below. (`BROLL_PEXELS` is retired; the stock tier no longer exists.)
- `WIDE_SILENT` — **retired 2026-09-18.** No two-shot clip is generated. The two-shot exists only as the still that opens `BRAND_bumper_out`; the cold open cuts from the hook straight into the singles, and act breaks are `BRAND_actbreak`, fixed furniture that costs nothing per part.
- `WIDE_CREDITS` — the closing roll, Turbo with audio on and the audio discarded in the edit. No dialogue lines, no `Voice:` blocks. One per part at most.
- **Repair path for a good take with a bad mouth:** Kling's separate lip-sync tool can remap mouth movement onto existing audio. Where a clip's performance and voice are right and only the articulation fails, that is cheaper than regenerating and rolling the dice on the performance again.
- `INTERJECTION` — two or three words, two or three seconds ("Mm." "Right." "That's fair."). Cheap, trivially easy to articulate, and the single biggest contributor to the illusion of a real conversation.

## 8b. Conversational Texture — write it in, do not hope for it

The shot types above are available; nothing so far made a run actually use them. A kit of
nothing but `INTERVIEW` rows would satisfy every other rule in this file and produce two
people taking turns reading at each other. The texture is what makes it read as a
conversation, and it is decided here, while the beats are being written — not later, and
not by whoever generates the clips, who will be working shot by shot with no view of how
they fit together.

**Place them deliberately, at the moments the drama asks for:**
- A **reaction** where the listener's face is more interesting than the speaker's — a hard question landing, a claim the other person visibly does not accept, the beat before an answer.
- An **interjection** where a real interviewer could not have stayed silent — a concession ("Mm. That's fair."), a small push ("But you knew."), a marker that he heard something significant.
- A **held beat** where a line needs air after it.
- A **cutaway** over the tail of a long line, which also hides the point where articulation is weakest.

**The check:** after writing the shot list, read down the `type` column. **More than three
consecutive `INTERVIEW` rows is a flag** — not automatically wrong, but it needs a reason.
Vary the spacing too; texture arriving on a fixed cadence reads as mechanical in a
different way.

**Density is a judgement, not a quota.** A tense exchange wants more; a long uninterrupted
answer that is genuinely holding attention wants none. But a whole act without a single
non-speaking beat is almost certainly wrong.

### The director's toolkit — building the outline's tags into rows

Added 2026-09-20. Mode 3 chooses the moments (*"The director's toolkit"* there); this is how each
becomes rows. If the outline did not mark any and the drama plainly asks for one, add it here —
same test: *would two real people do this here?* **Everything is built from single-speaker clips
and joined in the edit.** A two-speaker generation cannot pass the voice pass (§1).

| tag | rows | `edit_placement` |
|---|---|---|
| `OVERLAP` | a REACTION of the listener | `covers [speaker] over [moment], cut back on [cue]` |
| `NOD` | an INTERJECTION on camera; the speaker's next clip **chains** from it (continuity gate) | normal |
| `OFFMIC` | an INTERJECTION generated normally, picture discarded | `audio only, under [other shot] at [moment]` — the speaker's next clip may then use a fresh seed frame. Make sure the covering shot has room (tail or `BEAT`); give it a second more if not. |
| `BEAT` | a REACTION or held listener shot | `plays between [a] and [b], soundscape only` |
| `BROLL` | a BROLL_GEN row | `covers [speaker] from [moment] …` |
| `TWOUP` | the speaker's talking clip + the listener's clip **covering the same span** — a silent REACTION, or the listener's own chained clip where one exists | `two-up with [listener shot] from [moment] to [cue]` on the talking row. See *Two-up* below. |
| `CUT-IN` | see below | see below |

#### `CUT-IN` — the talking clip, a chained stop, and the interrupter

The model is **never** asked to stop mid-sentence (it fades or completes the line; both read
staged). Instead the stop is its own silent clip, chained from the talking clip **at the cut
point**:

1. **A — the talking clip.** Generates the whole line, run-on words included, budgeted for all of
   it. `spoken_text` stops at the cut word and ends with *—*. Pick a cut word that ends on a vowel
   or a nasal, never a stop, and **where a gesture is in motion** — the join then sits inside
   movement, where the eye does not look for it. Gesture paragraph: the hand moving with the point
   through the cut word.
2. **B — the stop.** REACTION, Standard **audio off**, 3 s (~24 cr). `start_frame`
   `chain from [A] at cut "[word]"` — **A's frame at the cut word, not its last frame**, since A
   runs on past it. Prompt by kind, positive and observable, and open with the mouth, because the
   start frame usually catches it mid-word: *"[Pronoun] lips close in the first moment and stay closed."* (pronouns and label from the profile; the lines below use Cleopatra's as the example)
   - `cut` — *"…her hand stops where it is and her eyes go to him."*
   - `seen` — *"…her hand stops mid-air, her brows lift slightly, and she turns her head toward him."*
   - `yield` — *"…she lowers her hand, opens it toward him, and settles back to listen."*
3. **C — the interrupter.** A normal talking clip; its line answers what was heard. Register:
   *"he comes in over her, firm but not loud"* (or the guest's own, if the guest interrupts). Gesture moving from
   the first word — **no lead-in stillness**, or the interruption lands late.
4. **`seen` only — W, the wind-up.** A REACTION of the interrupter leaning in and drawing breath,
   covering A a beat or two before the cut.
5. **`hold` — no chain.** A carries on; the gesture paragraph lifts the speaker's chin a fraction at the
   named word. The attempt is a 1–2 s `OFFMIC` (*"But—"*) placed `audio only, under [A] at "[word]"`.

Placements: A `interrupted by [C] after "[cut word]" — [kind]`; B `follows [A] at the cut, [C]'s
audio over it`; C `enters over [B] — interruption, audio overlaps ~0.3s before the cut`.

**The cut-point frame is found after A is generated:** time the cut word (audio envelope, confirmed
by ear), write the time into B's row as `chain from [A] at 6.42s`, and `chain_frames.py` extracts
that exact frame. Until then the script reports the row as *needs a cut time*.

#### Two-up (`TWOUP`) — both singles side by side. Added 2026-09-22; replaces what the wide was for.

The wide two-shot was cut because its figures read too large for the chairs (§0, 4b). A two-up shows
both people together using only the **singles**, which are right, so the fault never appears — and it
costs no generation beyond the listener clip the moment needed anyway. Fixed design (approved
2026-09-22, `Fixed_Assets/Branding/reference/splitscreen_reference.png`):
- 🔴 **Someone is always talking in a two-up. Settled 2026-09-24 (T6b, Salah): never both faces only
  reacting.** One half speaks, the other listens — that is the only two-up. A shared silence as a two-up
  (`P1_085` + `P1_086`, the silence after *"In a sanctuary"*) read as empty, two stills side by side.
  **A silence goes on one face** — normally hers, the one who has to answer: cut to her on his last
  words (they play off screen), hold the `BEAT`, then her answer. `screen_share.py` fails a two-up with
  no talking row in it.
- **Crop per pose, not one fixed offset.** Keep the whole figure in the half, hands included, with room
  in front of the face toward the divider: `frame_host_e` x=150, `frame_host_d` (hand lowered to the
  armrest) x=260, guest `_b`/`_e` x=800, on 1916-wide sources (T6, 2026-09-24).
- **Equal halves.** Host screen-left, guest screen-right — their eyelines meet across the divider and
  the table runs through both, so it reads as one room. Each half is a straight crop of its single,
  **never scaled up** (1080p source: a half is 960 × 1080 at native resolution).
- **Divider:** a 10 px paper-tone gutter with the walnut margin rule down its middle, 16–84% of frame
  height — the same rule as the on-screen plates.
- **The listener's half needs a clip as long as the span** — a silent REACTION (8 cr/s) written for it,
  or a chained clip already in the kit. Budget it in the row.
- **No text over a face or the divider.** Subtitles stay at the bottom; no lower third, context card or
  pull-quote while a two-up is on screen.
- **Changed 2026-09-24 (Salah): the two-up is the default way to show a host reaction while the guest
  is speaking** — his nod, his jaw setting, his failed attempt to come in, shown *beside* her rather than
  *instead of* her. Her half is her talking clip (already in the kit); his half is the reaction clip he
  would have had anyway. See *Screen share* below.
- **Cap: at most 7 per part, 3–6 s each, never two in a row, hard cut in and out** — never animated,
  never for ordinary back-and-forth. Past that it reads as a video call.
- **No text over a two-up** (below), so a pull-quote never lands on one — it lands on the guest's own
  held face after her line (§13b).

**Budget:** B ~24 cr, run-on words ~1–2 s, W ~24 cr. An `OFFMIC` costs a ~3 s clip whose picture is
discarded. Cheap for what they buy.

⚠️ **Untested as of 2026-09-20.** The risk to watch in B is an open-mouth start frame inviting the
model to keep mouthing; the silent reactions so far started closed. Check the first `CUT-IN` of a
part at the edit before a second is written into the next kit.


### Cutting rhythm — planned in the kit, not left to the edit

Added 2026-09-20. The kit decides these because only the kit sees the whole part.

- **Emotion first** (Murch's *Rule of Six* ranks it above story and rhythm): at any moment the
  picture belongs to **whoever is worth watching** — usually the speaker, but when the guest says something
  that lands, the host's face is often the stronger shot. Place host reactions on the guest's
  revelations, not only the guest's reactions on his questions.
- **Tighter early, freer later.** A visual change every ~10–20 s in the first three minutes (turns,
  reactions, a context card, a b-roll); every ~20–40 s after, with a long answer allowed to hold when
  it earns it. **No single picture holds past ~40 s** — the 15 s clip cap mostly guarantees this, so
  watch chained runs and b-roll-free stretches.
- **`PUNCH` — a zero-credit second framing.** In the edit, a push-in of **at most 15%** on the same
  clip (the source is 1080p; more turns soft). Two uses only: **emphasis** on a key line (hold it to
  the end of the clip), and **hiding a trim** inside a clip — when a dead pause is cut out, the punch
  lands exactly on the trim so the jump reads as a camera change. Write it as
  `edit_placement: punch-in at "[word]"`. Never on two consecutive shots, never on direct address, and
  keep the speaker's face clear of the subtitles. It changes nothing about the two camera frames —
  it is the same shot, closer.
- **Dead air.** A pause over ~1.2 s inside a talking clip that is not a written `BEAT` is trimmed in
  the edit, covered by a `PUNCH`, a reaction, a card or b-roll. Mark the expected ones in the kit where
  the duration model predicts slack; the edit trims the rest by ear.

### Screen share — the guest carries the picture. Settled 2026-09-24 (Salah), series-wide.

The guest is the reason anyone clicks; the host is the lens. Measured on the first Cleopatra rebuild,
the host had about a third of the words but close to half the picture, because his questions played on
his own face, eleven of the sixteen reactions were his, and six of seven b-roll rows covered her lines.
So the kit places the picture by rule, not by speaker:

- **Target: the guest on screen ≥ 65% of studio time** (aim 65–70%): her full frame plus two-up time,
  over her full frame + his full frame + two-up. B-roll and furniture are left out of the sum. Two-up time
  counts as hers (she is speaking) but is reported separately, so a kit cannot reach the target by living
  in split screen. **`Fixed_Assets/tools/screen_share.py` is a gate** — it reads each row's `screen:` line.
- **His questions, charges and pushes play on her face.** The line starts on him and the picture cuts to
  her **listening** as it turns to her (by its last clause), or the whole line runs under her when it is
  a short push or an echo. The listening clip is a guest `REACTION` (Standard, audio off, 8 cr/s) and her
  answer **chains from it**, so the cut from listening to speaking is seamless. His clip is still generated
  in full — its audio is the line.
- **He stays on his own face** for: his fixed slots (the cold-open address, the sign-off, Part 2's re-open),
  a line that turns the conversation to a new subject, his first question (his lower third), short
  interjections that re-anchor the picture, and lines where his face *is* the moment.
- **His reactions during her speech are two-ups** (above). **At most two full-frame host reactions per
  part** — the crack, or a reaction that must hold the screen alone (a card that needs his side of the
  room). The silent stop of a `CUT-IN` is part of his own line and does not count.
- **Re-anchor the chain.** A run of her on screen — answer → listening → answer — is a chain, and chains
  stop at three links. Put him on picture (a subject turn, a short interjection, the first words of a
  question) or a b-roll every second exchange so her next shot can start from a fresh seed frame.
- **Composite eyewitness guests — the exception.** Full-frame host reactions are allowed on the hardest
  testimony lines, so a witness defending the indefensible is never left unanswered on screen; the 65%
  target still stands. The gate relaxes the reaction count when the kit header says `composite: yes`.

**Every talking, reaction and b-roll row carries a `screen:` line** (`G 3.2 · H 1.1 · 2UP 0 · BROLL 0`,
seconds of speech-model time on screen for each), and the row that opens a two-up carries `twoup: #n`.
The builder computes them from the placements; the gate sums them.

## 9. Output: Editor-Ready Shot List and Creative Kit

### Kit header
`part`; `anchor_images` (every asset with its file path); the locked blocks written out once per character — register, voice and audio; and `voices`, naming the registered voice for each speaker.

### Shot list
Sequential, in final timeline order. Every row is one clip:

- `shot_id` — `P[part]_[###]_[type]_[subject]`, e.g. `P1_014_BROLL_legionary`. The number is assembly order.
- `type` — one of the types above.
- `start_frame` — **the exact seed frame variant this shot begins on**, or `chain from [shot_id]` where the shot continues an utterance. This is where the pose decision is recorded; a row without it is not finished.
- `duration_est` — seconds, computed from the word budget, never rounded up.
- `prompt` — paste-ready, built in the six-part shape from section 3.
- `spoken_text` — clean subtitle text, no direction.
- `sfx` — ambience and effects named inside the prompt so they generate in sync, plus anything to be added in post.
- `edit_placement` — **required on every silent row.** States the *intent*, not timings: which clip's audio runs underneath and how the shot is cut in. Exact in and out points are resolved at assembly from the clips' measured audio (section 9b). One of:
  - `covers [shot_id] over [described moment], cut back on [described cue]` — a cutaway over a speaking clip. The speaking clip is still generated at full length; only its picture is replaced. Describe the moment ("over his second question", "cut back on the guest's first word"), never a timecode.
  - `covers the tail of [shot_id], then holds a beat` — the free move: one silent generation covering both the end of a line and the pause after it, which also hides the point where a mouth is most likely to be degrading.
  - `plays between [shot_id] and [shot_id], soundscape only` — a held beat with no dialogue underneath.
  - `audio only, under [shot_id] at [described moment]` — an interjection used as an off-camera verbal nod: the clip's picture is discarded and only its voice is laid under the other character's continuing shot. Cheap, and the closest thing to a real interruption the format allows.
  - `diegetic only` — B-roll running on its own generated sound.
  - `interrupted by [shot_id] after "[cut word]" — [cut|seen|yield|hold]` — the talking clip A of a `CUT-IN`. See §8b, *The director's toolkit*.
  - `follows [shot_id] at the cut, [shot_id]'s audio over it` — the chained stop B.
  - `enters over [shot_id] — interruption, audio overlaps ~0.3s before the cut` — the interrupter C.

Runtime accounting: total runtime is the sum of INTERVIEW, NARRATION and standalone silent rows. A cutaway adds no runtime but does add a generation, so **generated seconds exceed finished seconds** — budget on generated seconds.

### Chain table — REQUIRED in every kit, placed right after the generation order
Added 2026-09-20. Every kit carries one table listing **every** row whose `start_frame` is
`chain from`, so the person generating sees at a glance which clips need an extracted frame and
which clip each depends on — and can generate in two passes instead of shot by shot:

| chained shot | starts from the last frame of | source type | start frame file |
|---|---|---|---|
| `P1_057` | `P1_056` | REACTION | `shots/start_frames/P1_057_start.png` |

Under the table, state the two passes in one line each: **Pass 1** = every seed-frame row, chain
sources included; **A seed frame waiting to be regenerated holds its rows:** `round_sheet.py … --hold frame_x` lists them as HELD at the top and leaves them off the sheet (2026-09-25).
**Chained rows are on the same sheet (since 2026-09-26)** — the sheet is ONE list in kit order with every chained clip placed **directly under its source** (marked *↳ chained*) and each entry carrying its own model / audio / chip settings (Salah): each is made right after its source clip is saved, starting from the source's last frame with **Kling's own last-frame feature** (colour matched in the edit). No separate Pass 2 round. Only a `CUT-IN` stop needs Claude (the frame at the cut word). If a kit has no
chained rows, the table is still present and says *none*. A `CUT-IN` stop chains from a **cut point**, not an end frame — its row says `at cut` until the time is measured, then `at 6.42s`; give it its own column value (*"P1_0xx at the cut word"*) so it is never mistaken for an end-frame chain. The table must agree with the rows —
`chain_frames.py` reads the rows, so a mismatch shows up as a missing or extra frame.

### The completeness test
The kit is generated blind and assembled later. Whoever generates the clips sees one prompt
at a time and has no view of how any of it fits. **Every decision needed to cut the part must
therefore be in the kit** — which shot covers which, whose audio runs under a silent row,
where a beat is held, what the reaction is reacting to. If assembly would need a creative
question answered that the kit does not answer, the kit is not finished.

Read the shot list as though you had never seen the script and had to cut it. Anything you
would have to ask about is missing.

### On `sfx` — there is no fixed effects library
Diegetic sound generates inside each clip: name it in the prompt so it lands in sync, and it
arrives with the picture. Interview scenes need nothing beyond the generated room tone and
the `ROOMTONE_studio` bed. B-roll arrives with its own footsteps, fire and wind.

The `sfx` field's "added in post" half is for the rare case generation cannot cover, and
**no `SFX_*` asset set currently exists.** Do not write a kit row that depends on one. If a
part genuinely needs a recurring effect, it gets registered in `STUDIO_ASSETS.md` as a fixed
asset like the score, and created once — but the default assumption is that generation
supplies it.

### JSON payloads
Each row also carries a paste-ready fal payload: `prompt`, `start_image_url` (the seed frame), `duration`, `generate_audio`. Dialogue shots reference no entity at all — the seed frame carries everything and an `@` tag in a video prompt throws an element-reference error. B-roll extras, which have no seed frame, are referenced by their `@` tag. `shot_type` stays `customize`.

## 9b. Assembly — performed here, not handed off

The kit is an assembly spec, not a document for a human editor. Whoever wrote the shots
knows why the reaction sits where it does and whose voice carries under it; that intent
does not survive being written down and handed over. So Mode 4 also cuts the part.

**The kit carries intent. Assembly resolves it by measurement.** A row says "the guest's reaction
covers the tail of his question, cut back on the first word of the answer" — it never says 6.5 seconds,
because nobody knows where his speech ends until the clip exists. Every number comes from
the actual audio at assembly time.

### What the user does
Generate each clip, then drop it in `Episodes/[Guest Name]/` named **exactly by its
`shot_id`** — `P1_031.mp4`, `P1_032.mp4`. The filename is the only link between a clip and
its row; a renamed file is an unplaceable clip. Clips can arrive in batches, and the part
is assembled incrementally act by act so problems surface early rather than at the end.

### Assembly procedure
1. **Probe every clip.** Duration, then `silencedetect` at −38 dB to get speech in and out points, then `volumedetect` on a silent stretch for the noise floor. Never estimate any of these.
2. **Cut during silence, never on a word.** A cut point inside a pause is invisible; one that clips a syllable is not. Take the cut a beat *before* a covered line begins so the reaction is established before the words arrive — an insert that lands simultaneously with the line reads as a mistake.
3. **Close the gaps.** A clip's trailing silence plus the next clip's leading silence add up, and a continuous exchange turns into a stilted one. Trim to roughly 0.3s between sentences of one utterance, more at a genuine turn. Judge it against what the beat is doing, not a fixed number.
4. **Normalise the chain.** Measure luma per link, lift each back to the first clip's level. Chains darken about 1.5% per link and adjacent links are too close to see.
5. **Lay the room tone bed.** From a generated silent clip, mirrored forward-and-reversed into a seamless loop, at roughly −50 dB against clip floors of −60 or below. It runs under everything, never ducking, and it is what makes a held pause read as a room instead of a dropout.
6. **Deliver the assembled part.** Not a folder of clips.

### The honest limit
Assembly here is exact on everything measurable — timing, levels, colour, continuity — and
blind to everything else. Whether a performance lands, whether a pause is moving or merely
long, whether a reaction reads as listening or as vacancy: those need eyes on the cut. The
loop is therefore assemble, watch, report, adjust. That is how the combined test was built
and it is why it worked.

### Division with Mode 6
Mode 4 delivers a finished part: dialogue, cutaways, reactions, B-roll, room tone, colour
matched, cut to rhythm. Mode 6 takes the assembled parts and adds what belongs to the whole
episode — score, branding, titles, subtitles, export.

## 10. B-Roll

**All generated b-roll is charcoal and graphite drawing on toned paper.** Not a stylistic whim — it was tested against a photoreal alternative and won on measurement.

| | value | saturation |
|---|---|---|
| Studio frame | 0.354 | 0.463 |
| Sketch b-roll | 0.471 | **0.236** |
| Photoreal b-roll | 0.314 | 0.496 |

The photoreal version sits almost on top of the studio's own numbers — it reads as the same footage slightly darker, which is exactly the ambiguity a reconstruction show must avoid. The sketch is brighter and half as saturated, so the cut registers as a deliberate shift, while the hue stays in the same warm family so it does not clash.

**The style survives animation.** An 8s test held the drawing to the last frame with no resolution into photographic footage. Stroke stability between consecutive frames was flat across the clip (mean diff 8.96 / 9.03 / 9.01; high-frequency noise 13.75 / 13.73 / 13.68), meaning the change is camera and subject motion rather than texture boiling. Shadows tracked the figures correctly, which requires the model to hold the light geometry rather than copy texture forward.

**Pexels is dropped entirely.** The stock tier is gone: no search step, no availability check, no attribution block, no third-party licence surface. It costs about +280 credits a part (~$1.72) and buys one coherent visual language. Any surviving Pexels row, attribution field or `youtube_metadata` credit line is legacy and should be removed.

### The style block — one canonical paragraph, pasted byte-identical

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than
outline — broad washes and smudged shading, edges appearing where two tones meet rather
than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth.
Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights,
no metallic or gold accents.
```

For a video prompt, add: *"It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, and it never resolves into photographic footage."*

**The failure this block was rewritten to prevent is drifting toward graphic novel.** The first sketch test came back crisp and linear — hard helmet highlights, gold accents on the metal, forms bounded by drawn edges. That reads as comic-book illustration, and on a research-led show it undercuts the thing the style exists to signal.

**The dial is line versus wash, and the show sits at the wash end.** Three specific corrections, all now inside the block, all learned the expensive way:

- **"Forms built from tone rather than outline."** The single most load-bearing phrase. Without it the model draws contours and fills them, which is comic construction; with it, the model finds edges where tones meet, which is how a charcoal drawing is actually made.
- **Drop "white chalk highlights."** It was in the first prompt and it is what produced the crisp metallic glints. Anything naming a highlight material invites exactly that hard specular treatment.
- **Name the excluded accents.** "No metallic or gold accents" — the model adds warm metal by default on armour and jewellery, and one gold note is enough to flip the whole frame to illustration.

**When in doubt, push further toward wash.** A drawing that is slightly too soft still reads as a drawing; one that is slightly too linear reads as a different medium altogether.

*(The block deliberately does not say "documentary" or "not a graphic novel." Naming the thing you are avoiding puts it in the prompt — describe the construction instead.)*

### The two-step, and what each step is for

**With characters in the shot — two steps.**

1. A **still** (**Kling image generation on kling.ai**, 16:9 — the way the b-roll start frame was tested and passed; changed 2026-09-26, Salah, L37. Seedream is for studio frames only), generated in the charcoal style, holding the pose the video will move out of. Write it as a *still*: the subject at rest, nobody mid-stride, since a frozen action pose makes an awkward first frame.
   - **No reference image for anonymous extras.** Passing one produced roughly twenty clone faces in testing. Identity for a crowd comes from the registered **wardrobe text block** (`STUDIO_ASSETS.md`), pasted byte-identical, plus the composition.
   - **Describe crowds by arrangement, not by count.** "A column" rendered as a line abreast; "seen from behind, one rank behind another, receding into the distance" rendered correctly.
   - **Run the Period Accuracy Gate** (`skill_mode2_cast.md`) on the wardrobe before writing the still prompt. Charcoal hides fine detail, but mail against banded plate is a silhouette difference and it still reads.
   - 🔴 **Date every object, and ban what comes later (2026-09-27, L55).** The image model fills a vague noun with the
     picture it has seen most: *"ships"* became 18th-century galleons with gun smoke (Actium), *"warehouses"* got gabled
     roofs, *"a barge"* got a steamboat cabin and onlookers in top hats, a signet ring came out gold on a charcoal drawing.
     Every still prompt names the place and year (*"the Great Harbour of Alexandria in 48 BC"*), gives each object its
     period form (*"ancient oared war galleys: long low hulls, a bronze ram, one mast, a single square sail"*), and ends
     with the later forms it must not show (*"no cannon or gun smoke, no ship with more than one mast, no pitched roofs,
     no hats, no colour"*). Claude looks at the stills for anachronisms before the video step.
     **Wide views of ports, towns and fleets are where the model drifts most** (`P1_050` came back 19th-century three
     times: gabled warehouses, schooners, factory chimneys). Prefer a **close shot of one period object** (a ring, a shrine
     niche, amphorae on a quay, a ram at the waterline) — close shots were right first time; a wide gets one retry, then
     becomes a close shot.
2. The **Kling video** prompt, image-to-video, using that still as the start frame.

**With no character in the shot — also two steps. Changed 2026-09-23** (it said one step, text-to-video;
the v1 Part 1 kit had already moved every b-roll row to two steps and `round_sheet.py` builds a still for
every `BROLL_GEN` row, so the file and the tool disagreed). The charcoal style is the thing that must not
drift across a part's b-roll, and a start frame is what holds it; 3 credits a row is cheap insurance.

**Cost the stills.** Four character b-roll shots is twelve credits: small, but the kit's total is wrong if it omits them.

### The video prompt describes MOTION, NOT CONTENT

The start frame already carries composition, style, light and figures. Re-describing them invites reinterpretation instead of animation — the same principle that governs the dialogue seed frames. A b-roll video prompt is **four paragraphs and no more**:

1. **The move** — one camera move, named, with its reason implicit in the choice.
2. **The medium, stated as persisting.**
3. **What moves** in the frame.
4. **The audio.**

**The medium must be framed as persisting, with the failure mode named**: *"it stays a drawing for every frame … it never resolves into photographic footage."* Stating the style once is not enough; models drift toward photoreal across a clip.

### Camera moves are ALLOWED on b-roll and forbidden on dialogue

The lock exists to protect seed-frame continuity and the multi-camera studio grammar. Neither applies to a cutaway, and locking b-roll kills the only place in the show where the camera can move. The rigidly locked interview is precisely what gives a moving cutaway its value.

Discipline: **slow, one move per shot, always with a reason.** Vocabulary —

- **slow push in** — drawn toward something
- **slow pull back** — reveals, endings
- **slow tilt** — scale; detail to context
- **slow lateral drift** — reliefs, objects, texture

Never handheld. **This reverses one rule elsewhere in the project:** *"the speed of the camera motion is slow"* is forbidden on dialogue and correct here.

### "Nothing happens" is correct for b-roll under dialogue

The viewer is listening; an event on screen pulls attention off the line. A slow move over a held image is doing its job. Spend visual interest on the **act transitions** instead, which carry no dialogue and must hold attention alone.

### Assembly note

Generated b-roll warms and darkens slightly across a clip — measured over 8s, saturation 0.238 → 0.277 and shadow 31.4% → 38.1%. **Normalise each b-roll clip against its own first frame**, the same way chain luma is compensated.

### IP filter safety applies hardest here

B-roll is where period place and event names creep in. Describe the aesthetic, never the label. The spoken line may name people and places freely; the visual description may not.

## 11. Supporting Sections

- `primary_sources` — the texts, records and scholarship behind every Guest line.
- `trust_disclaimer` — mandatory, as a title card and/or Host line in Part 1's cold open. Carry a short version into Mode 5.
- `youtube_metadata` — the kit's §9, written to the fixed labels in **§15** (titles, hook, summary, heard-vs-record, tags, hashtags, pinned comment, playlists, end screen, series index). The **source list is generated from the line provenance tags** into `card_data_p<n>.json`, never written in §9.

  ⚠️ **The series index is `Part N of 2`, and every title carries it.** An arc is two parts —
  Mode 3 fixes this and it is not a per-guest decision. Part 1's kit shipped with `Part 1/3` on all
  three titles, written before the two-part rule and never corrected. **A stale part count is the
  one metadata error a viewer sees**, and it promises an episode that does not exist. (§6b). No stock-footage attribution block: there is no stock footage.
- `soundscape_design` — only what generation cannot supply: room-tone continuity across cuts, the `MUSIC_*` score tags and where each enters and exits, and any non-diegetic layer. Diegetic sound is named per shot in `sfx`.

## 12. Structure

- Part 1: Host cold open on the `frame_host_direct` set, carrying the trust disclaimer, before cutting to the guest. Use `frame_host_direct_b` — leaning in, confiding — for the hook, and `frame_host_direct_c` — settled, hands clasped, formal — for the disclaimer itself. The disclosure plays plain, never dramatic.
- Parts 2 and 3: brief recap open.
- Part 1 closes on a teaser that works as an invitation rather than a withheld ending. Part 2 closes definitively.

## 13. Saving

Save the finished kit into `Episodes/[Guest Name]/` as `P[N]_kit`, so the episode folder stays self-contained.


## 13b. Key Lines — identified once, used three times

While writing the dialogue, mark **three or four lines per part** as key lines: short, self-contained, and strong enough to carry meaning with no surrounding context. Record them in the kit as their own list, with the shot ID each comes from.

One set of lines then feeds three consumers, which is what keeps the part, the thumbnail and the reels feeling like one object rather than three:

- the **`BRAND_pullquote`** graphics inside the episode,
- the **thumbnail overlay** candidates in §14,
- the **reel hooks** in Mode 5.

A line qualifies only if it survives being read cold, in silence, by someone who has watched nothing. "You assume those were two things. For me they were one." qualifies. "They killed him at the shoreline and kept the head." does not — it needs the scene around it.

**Where the pull-quote sits is a writing decision, not an edit decision.** Place it in the kit, and place it *after* the line has been spoken — the burned subtitle already carries those words while the guest is talking, so a quote card over the same line is the same sentence twice in two typefaces. **Changed 2026-09-24:** it lands over **the guest's own held face** after the line — a beat at the head of her listening clip (Screen share, §8b) — not over a host reaction, which is now a two-up and carries no text. Her words, on her side, over her.

Three or four per part is the ceiling. One every thirty seconds is not emphasis, it is wallpaper, and it trains the viewer to stop reading them.

**The hook line is not pull-quoted if it stays the hook** — it already opens the episode and is heard again in context; a card makes it three times. Since the hook is re-picked in Mode 6 (Mode 3's is a first option), place the pull-quote if the line earns one and flag it in §12: Mode 6 drops that pull-quote if it keeps the line as the hook.

**Lower thirds** are placed here too, and there are only ever two per part: the host on his first proper appearance, the guest on hers. Never on the teaser — that beat is a cold hook and stays clean. Contents and treatment are fixed in `STUDIO_ASSETS.md`; the kit states the shot each one opens over.

**Context cards** are placed here too — the fourth kind of on-screen text, added 2026-09-20. Mode 3
writes them; the kit's §12 carries a **Context cards** table: `# | Lands on | Word | Side | Label |
Name | Gloss | Source`. Rules the table must satisfy:
- **Side** is opposite the voice: `L` when the guest speaks, `R` when the host speaks.
- **Enters as the word is said**, holds 5.5 s. It may ride over (or enter on) a **b-roll** cutaway —
  b-roll has no face to cover — but it must **never** overlap a reaction of the other person (their
  face is on the card's side), a lower third, or a pull-quote. Check every card against the
  `edit_placement` of the rows around it.
- 🔴 **A card must never ride onto the other person's face — including their talking shot.** Added
  2026-09-23. A card placed opposite the speaker sits exactly where the *other* person's face is in their
  own cross-shot (host face upper-left, guest upper-right). So when the word comes near the end of a line
  and the next shot is the other person, the card runs onto their face at the cut. Check the time left in
  the speaker's picture after the word: it must be ≥ 5.5 s. If it is not, in this order: **(1)** move the
  anchor to the other person's mention a moment later, if they say the word too (the card flips side with
  it); **(2)** cover the start of the reply with a **listener reaction chained from the speaker's clip**
  (J-cut — the reply is heard over the speaker's face) until the card has gone; **(3)** ride the card over a
  b-roll row that covers the join, cutting back only after the card has left. Cleopatra P1 needed all
  three (cards 03 and 07; 05; 06 and 08).
- **One text at a time.** Where a `[D]` line would also get an on-screen source credit (Mode 6) at
  the same moment, the card's source line *is* that credit.
- Run `python3 Fixed_Assets/Branding/intro_source/context_build.py check Episodes/<Guest>/P<n>_kit.md`
  — it fails any card whose gloss runs past three lines.

## 14. Packaging — delivered with the kit

Titles and thumbnail text are derived from the part's content, so they belong in the kit, not in Mode 6 as an afterthought. Every kit ends with a Packaging section containing:

- **Three title options** — written in §9 to the §15 rules (they become the Test & compare set).

- **Chapter titles, one per act** (plus `0:00` for the opening) — short, specific, curiosity-led (*"The kingdom that could not defend itself"*). Mode 6 fills the timecodes from the cut. YouTube needs the first chapter at `0:00`, at least three chapters, each at least 10 s. Chapters make a long part skimmable and appear as named segments in search.

- **Three thumbnail overlay lines** — the statement, quote or answer lifted from the part that goes on the thumbnail. 3–5 words, all caps, readable at phone size. Pull them from what the guest actually says; the guest's own words in quotes are usually the strongest of the three.

  The title carries the subject; the thumbnail carries the provocation. **They must not say the same thing** — the viewer reads both at once, and duplicating wastes half the space. Avoid question marks, which read weaker than statements at that size. **The guest name and part number DO appear on the thumbnail**, but never inside the overlay line — they sit in a small separate kicker above it (`CLEOPATRA VII · PART 1`). The usual advice to keep the name off is right for a single video and wrong for a series: the name is not selling the click, it is indexing the channel page, and a grid of twenty tiles carrying only statements cannot be navigated. See `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`.

  **On composite eyewitness episodes the packaging is where apologia actually gets read**, and no disclosure card fixes it. The title and the overlay line foreground the *event*, never the character's defence, and never a line that reads as the show endorsing him. "A GERMAN SOLDIER TELLS THE TRUTH" is the failure mode; "STALINGRAD, FROM INSIDE THE POCKET" is not. The guest's own words make the strongest overlay line on a named-figure episode and the most dangerous one here — check every candidate against how it reads to someone who never opens the video.

  The overlay line sits alongside the channel mark. Composition is fixed by the brand, not per episode: mark in one corner, line occupying roughly a third of the frame, subject in the rest.

- **The thumbnail.** **Settled — see `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`.** Three layers: a **photoreal** guest against darkness on the right, a **toned paper ground** — the same stock as the lower-third plates — with ink type over it, and 3–5 words in the dark left third. Built by **compositing two separate generations**, never by asking one prompt for a photoreal figure in a drawn world — that blends the styles across the whole frame and produces neither.
  **The portrait must be generated lit for paper** — soft even light, no dark side, and a flat pale background matching the paper's tone so there is no cutout at all. A portrait lit against black has a black shadow side that is unrecoverable once it sits on a light ground. Both a dark ground and a per-episode drawn scene were built, tested at feed sizes and rejected; the reasoning is recorded in `THUMBNAIL_SYSTEM.md` so it is not re-proposed.
  A per-episode drawn *scene* was considered and rejected: at the 22% that works visually the background cannot be read, so a scene strong enough to identify is also strong enough to eat the face's separation. The ground is therefore fixed for the whole series, and the only per-part inputs are the kicker and the statement.

### What the testing needs to beat — measured, Cleopatra Part 1

Recorded so the eventual prompt has a baseline rather than an opinion:

- Seed frames are **2720×1536**, so a tight 16:9 crop of one lands around **1342×755** — above YouTube's 1280×720 minimum. Cropping a pose frame is viable; it is not ruled out.
- **Uncropped, the frame is unusable.** The guest's head is 22% of frame height, which is roughly **45px** at desktop feed size and about 26px on mobile. No expression survives.
- **Cropped, it works.** The face reaches roughly **91px** and reads clearly at both sizes.
- Three things a purpose-made still should fix, and which the crop cannot: the **microphone boom occupies the negative space** the overlay line needs (the guest faces screen-left, so the empty side is the side the mic is on); the **expression is neutral by design**, correct for the format and weak for a thumbnail; and the crop is already **at the resolution floor**, so there is no room to go tighter.

Test against those three. A structure that removes the mic, gives a chosen expression, and leaves a clean third of frame for text is worth locking; one that does not is no better than cropping the pose frame, which is free.

The thumbnail is the single highest-leverage asset in the part. A viewer decides on it in under a second, before a frame of the generated work is visible.

## 15. The publish words — kit §9, assembled into `P<n>_PUBLISH.md`

**Added 2026-09-23.** Uploading a part is copy-paste, not writing. Mode 4 writes the *words* into the kit's §9 under fixed bold labels; `Fixed_Assets/tools/publish_sheet.py` assembles them — with the chapters from §11, the sources from `card_data_p<n>.json`, the disclosure from §8, and Mode 6's timecodes — into one sheet laid out in YouTube Studio's field order. Nothing is typed twice, so nothing drifts.

**§9 is written in exactly this shape** (the parser reads the labels; anything else in §9 — notes, ⚠️ warnings — is ignored):

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

What each one has to do:

| Label | Rule | Why |
|---|---|---|
| **Titles** | Exactly three, each ≤ 70 characters (100 is YouTube's hard max, but phones cut at ~70). Every title carries the series index. The primary names the guest. **Any words in quotation marks must be the guest's line verbatim** — the tool checks every quote against the spoken lines. The three should differ in *angle* (the quote / the charge / the event), not in wording. | All three go into Studio's **Test & compare**, which picks the winner on watch time, not clicks — so a misleading title loses by itself. A misquote in quotation marks is a factual error on the most-read line of the page. |
| **Description hook** | Two sentences. **The guest's name and the subject's search word in the first 150 characters** — that is all that shows above "…more", in search results and under the video. | The first lines are the only part most viewers and the search index weigh. |
| **Summary** | 200–300 words of plain prose: who, when, what this part covers, in the words people actually search (*Cleopatra and Julius Caesar*, *Battle of Actium*). No keyword lists. | Gives YouTube's index real language to match; a stuffed list reads as spam to both viewers and the system. |
| **Heard vs the record** | 1–3 items, each a popular belief and what the sources say, with the shot id that carries the correction. | The corrections are the show's strongest evidence of method, and a searched-for myth is a real way in. The tool strips the shot ids before pasting. |
| **Tags** | 10–15, ≤ 500 characters total: guest name and its spellings, period, place, the part's big events, the format (*historical interview*, *history podcast*). | Tags matter little for ranking; they catch misspellings. Cheap to do right, so do it. |
| **Hashtags** | **Exactly three**: guest, period, `#History`. | YouTube shows the first three above the title; past that they add nothing, and very many get all of them ignored. |
| **Pinned comment** | One question a viewer can answer from their own opinion, not a quiz. | Early replies are an engagement signal, and a question beats "like and subscribe". |
| **Playlists** | The series playlist, plus the guest's own two-part playlist. | Playlists are what carry a viewer from Part 1 into Part 2. |
| **End screen** | Part 2 (or, on a Part 2, the next guest's Part 1) + subscribe. | |
| **Series index** | `[Part N of 2]`. | See §11. |

**Check before the kit is done** (does not need the cut, so it runs in Mode 4):

```bash
python3 Fixed_Assets/tools/publish_sheet.py Episodes/$G --part $N --words-only   # exit 0 = the words pass
```

**The sheet itself is built in Mode 6**, once the cut exists — see Mode 6, *Publishing*. The tool also carries the settings Studio asks for every time — **Altered or synthetic content → Yes** (required: realistic synthetic people and voices), category, language, captions, audience — so they are never decided from memory at upload.

Channel-level values (series playlist link, category, language) live once in `Fixed_Assets/publish_defaults.json`; a `TODO` there blocks the sheet.
