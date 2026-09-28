# FIXED STUDIO ASSETS (Kling 3.0 / 3.0 Turbo, on kling.ai)

> 📚 **How this file is kept (cleanup 2026-09-28).** Current registry and rules only. Superseded versions (the wide seed
> frames, the camera preset, the six-cue score, the baked-in wide panel) are in `DECISIONS_ARCHIVE.md` and
> `_archive/skills_pre_cleanup_2026-09-28/STUDIO_ASSETS.md`.

All scene scripts must strictly reference these tags:
- `@host_base`: Permanent Host asset (modern investigator, plain black t-shirt, dark jeans).
- `@cam1_host`: Host cross-shot plate, empty. Camera on the right side of the round table looking diagonally across it at the LEFT armchair, seated eye level, medium framing. Floor lamp and dark charcoal panel wall behind that chair, walnut slat wall to the right of frame, near table edge and a microphone in the foreground. A seated Host faces screen-right.
- `@cam2_guest`: Guest cross-shot plate, empty, mirrored. Camera on the left side of the table looking diagonally across it at the RIGHT armchair. Shelf with books and plants behind that chair, walnut slat wall to the left of frame, near table edge and a microphone in the foreground. A seated Guest faces screen-left. Used for AI-cast guests — Archival fallback guests are inserted as stills, not composited here.
- `@cam3_wide`: Symmetrical wide master plate, empty. Both armchairs facing each other across the small round walnut table with two microphones standing on it, walnut slat wall centred behind, floor lamp and charcoal panel wall to the left, shelf with books and plants to the right, woven rug on light oak floor. **Used only as reference 1 of the per-part outro wide** (Mode 4 §7) — no wide clip is generated from it.
- `@guest_[name]`: Active AI-cast historical guest character asset — a Fully Anonymous Composite, an Eyewitness Substitution standing in for an Iconic-tier figure, a Reconstructable-tier real figure, or a non-iconic Real Identified Figure.
- `@archival_[name]`: Fallback-only tag for a Real Identified Figure (Standard) whose AI casting was blocked. Presented as a still with camera movement only — never facially animated or lip-synced. Not used for Iconic-tier figures, which are represented on screen by an Eyewitness Substitution instead.
- `@voice_host`: the Host's permanent series voice. Until a platform voice-ID mechanism is in place this is a prose description, and it must be pasted byte-identical into every Host prompt — never reworded, never summarised. Canonical text: *"Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting."*
- `@voice_[name]`: a guest's fixed voice, written once during Mode 2 casting and reused byte-identical for every clip of that guest across both parts. Build it from what the figure's circumstances support — age, bearing, and the register a person in that position would actually speak in — not from the pop-culture performance. Canonical text for `@voice_cleopatra`: *"Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading."* *(Must match `CAST.md`, `VOICES.md` and every kit's `Voice:` line — the Voice gate counts them; a stale copy here once carried a retired accent into the registry a Part 2 kit copies from.)*
- `@voice_newton` *(drafted ahead of casting; Newton has no guest folder yet — confirm in Mode 2 before use)*: canonical text — *"Voice: male, early 60s. Dry, lightly rasped baritone sitting higher and thinner than the Host's, worn at the top of its range. Clear educated English of an older, more formal kind, consonants over-finished by decades of being heard across a room. Sentences settle downward into a low quiet weight at the end. Never sonorous or pulpit-theatrical, never avuncular."*
### The host — brief (from the original master instructions, restated 2026-09-22)
- **The modern lens.** An objective, composed investigative journalist. He probes moral compromises,
  controversies and historical consequences with a modern analytical framework — and **carries
  posterity** (later judgements, scholarship, what was said afterwards), which the guest answers from
  experience (Mode 3, Knowledge Gate).
- **Interviewer, never interrogator.** Curious, level, pressing without prosecuting; puts the charge
  rather than making it; concedes plainly when the guest lands a point.
- **Speech:** conversational, **with natural contractions** (*"Let's start"*, *"That's fair"*). The
  guest's contraction habit is set per guest in the `CAST.md` performance profile.
- **Immersion:** he talks to the guest as someone sharing the table. He addresses the audience **only**
  in the fixed slots — the cold-open hook and the sign-off. The guest never addresses the camera, the
  audience or the production; speaking from beyond their own life is the show's premise, not a break.

- **No pace language in a registered voice.** Timbre, pitch placement, accent colouring and what the voice deliberately is not — never speed or rhythm. A voice description saying "measured, unhurried pace" fights the clip duration for control of the same thing, and the duration should win because it is exact. This is why the two texts above no longer carry the pace lines they were first written with.
- **Accent colouring for non-native guests.** A guest who would not have spoken English may carry a light accent colouring, as a dramatic convention. Keep it light and dignified: it should read as a trace of origin, never as a comic or exoticised performance, and never so heavy that it costs intelligibility or lip-sync. Optional in every case — drop it if the result is worse. **Wherever it is used, it is written into the KLING `Voice:` block** — accent is carried by phonetics, which speech-to-speech takes from the Kling source read; the ElevenLabs voice supplies timbre only. The registered text here, the `CAST.md` line, the kit's `Voice:` blocks and the ElevenLabs design description must all say the same thing.
- **No voice QC gate:** every talking clip passes through one ElevenLabs voice, so drift between clips cannot happen. A first/middle/last comparison of a part is kept only as a *picture* check for platform shifts.

Seating binding — never changes, within a part or across episodes: the Host occupies the LEFT armchair and is only ever shot on `@cam1_host`; the Guest occupies the RIGHT armchair and is only ever shot on `@cam2_guest`. All three plates are the same room seen from three fixed positions — floor lamp and dark charcoal panel wall on the left, walnut slat wall centred, shelf with books and plants on the right, small round walnut table with two stand microphones, woven rug, light oak floor, warm 2700K practicals.

## Asset File Locations
Every asset tag above corresponds to an actual image file on disk, inside this project folder:
- Fixed Studio & Host assets → `Fixed_Assets/` (`host_base.png`, `cam1_host.png`, `cam2_guest.png`, `cam3_wide.png`). Permanent and shared by every episode.
- Seed frames → `Start_Frames/Host/` (permanent) and `Start_Frames/<Guest>/` (see *Where start frames live* below).
- Reusable Era Stock Extras (see below) → `Era_Stock_Extras/`. **These are now period-checked wardrobe *text blocks*, not images** — see the Era Stock Extras section for why.
- A guest's character sheet, plus any B-roll extra cast specifically for that guest's arc and not registered as reusable → `Episodes/[Guest Name]/` (e.g. `Episodes/Cleopatra/guest_cleopatra.png`). Create this folder the first time Mode 2 casts that guest, and keep everything from that episode in it for easy cleanup later.

## Visual Grounding Requirement
Before writing any prompt, scene, or script that references one or more of these asset tags, retrieve and actually view the current image file(s) for every referenced tag, from the locations above — never rely on the tag name or its text description alone. This matters most for Mode 3's B-roll reuse check and Mode 4's scene generation, where several assets (Host, Guest, a camera plate, B-roll extras) are combined into one shot and need to visually agree with each other on scale, lighting, framing, and wardrobe. If an asset may have been regenerated or replaced since it was last viewed, view it again rather than trusting an earlier look.

## Seed Frames
The camera plates above are inputs. These are what production actually uses: a still of a character already seated in a plate, used as the start frame for every video generation of that character. The set's reference frame is generated from the character sheet plus the plate; **every other pose is an edit of the reference** (Mode 2, L36). Files live in `Start_Frames/`.
- `frame_host`: Host seated in the left armchair, facing screen-right toward the guest. Default for all Host dialogue.
- `frame_host_direct`: Host in the same chair, same framing, looking into the lens. Used only for direct address to the audience — the cold open monologue and any narration to camera. Never for dialogue with the guest.
- `frame_guest`: Guest seated in the right armchair, facing screen-left toward the Host. Default for all Guest dialogue, and for silent reaction shots.
- **No wide seed frames.** The only picture of both people is the per-part outro wide, built in Mode 4 from `cam3_wide.png` + the host's and the guest's last-clip pose frames (`frame_wide_[name]_outro(_marked|_charcoal).png`, L59). No clip with both people in it is generated — the voice pass converts a clip to one voice, and the generated wide had a figure-to-chair scale fault.

Casting a new guest is not finished until their `frame_[name]` exists: generate it from their character sheet plus `@cam2_guest` before Mode 4 produces any part. Scale check on every new seed frame — the armchair must read visibly wider than the person, with upholstery showing either side of the torso, matching `frame_host` and `frame_guest`.

Guest pose registers are not here — they are per-guest and live in `Episodes/[Guest Name]/CAST.md`,
written by Mode 2 at casting alongside the voice and wardrobe. Mode 4 reads both.

### Host Pose Register — what each frame is for
All verified against `@cam1_host`. Choose by what the beat is doing, never at random.
Ordered here roughly from most open and relaxed to most engaged.

**Facing the guest (`frame_host` set), eyeline off-frame right:**
- **`frame_host`** — settled back, both forearms along the armrests, hands relaxed. The neutral default. Listening, or asking something that carries no particular weight.
- **`frame_host_f`** — one arm draped over the front of the frame-left armrest (as generated), other hand flat on his thigh, torso open. The most off-duty pose in the set. Light moments, a warm aside, an easy question. Wrong for anything hard — it reads as not taking it seriously.
- **`frame_host_c`** — one ankle crossed over the opposite knee, hand resting on the shin, the raised foot prominent lower-left. Relaxed and informal, but more composed than `f`. Good for a long stretch of listening, or a question asked lightly on purpose while the content is not light.
- **`frame_host_e`** — settled back, forearms off the armrests, hands clasped in the lap, shoulders square. Attentive and slightly formal; the most contained pose. Good for receiving a serious answer, and for the turn into a difficult subject.
- **`frame_host_d`** — elbow on the frame-right armrest, knuckles resting against the jaw, other hand on the thigh. Reads as weighing something. Use where he is turning an answer over, following up on a detail, or visibly not satisfied.
- **`frame_host_h`** — settled back, one hand over the front of the armrest, the other open, palm up, by his thigh. Mid-explanation, his longer questions, laying out a premise.
- **`frame_host_b`** — leaning forward, elbows on the thighs, hands clasped between the knees. The most engaged, and he sits noticeably closer to camera because of the lean, so it cuts slightly larger than the rest. Reserve it: the pressing question, the moment the interview narrows. Overused it becomes the interrogator problem in body language rather than voice.
- **`frame_host_i`** — leaning well forward, forearms on his thighs, both hands apart and open between his knees. Pressing a hard question; leaning in on a challenge. (Built by editing `frame_host_b`; frame-set PASS.)

**The pose table is the authority for prompt wording** — `Fixed_Assets/tools/poses.py` (`rank`, `use`, `hold`, `entry`, gestures, `avoid`). This register is the human summary; where they differ, the table (written from the images) wins.

**Direct address (`frame_host_direct` set), eyeline into the lens — cold open and narration only, never dialogue with the guest:**
- **`frame_host_direct`** — settled back, hands resting on his thighs (as generated). Neutral narration.
- **`frame_host_direct_c`** — settled back, hands clasped in the lap. Slightly more formal; plain, undramatic narration. (The host never states the disclaimer aloud — Mode 4 §0.)
- **`frame_host_direct_b`** — leaning forward, forearms on thighs, hands clasped. Confiding, closing distance with the audience. The cold-open hook and the sign-off.

Guest sets follow the same principle but vary less: a composed figure should not swing between postures, and the narrower range is correct rather than a limitation.

### Pose Variants
Every dialogue shot opens on its start image, so a character generated from one seed frame every time visibly returns to an identical resting position at each cut. Prompts cannot fix this — the start image *is* frame one, and the prompt only controls what happens after it. The variation has to exist in the frames themselves.

Each seed frame is therefore a **set**, not a single image. The original keeps its name and the variants suffix from `b`: `frame_host`, `frame_host_b` … `frame_host_f`. Everything is identical across a set — camera position, lens, framing, crop, wardrobe, lighting, eyeline — and only the seated posture differs.

Set sizes:
- `frame_host` set — eight (`frame_host`, `_b`, `_c`, `_d`, `_e`, `_f`, `_h`, `_i`). Permanent for the series; a frame is replaced only when a check fails, in place, by editing the reference (Mode 2), with the old file moved to `Start_Frames/_replaced_<date>/`.
- `frame_host_direct` set — three. Permanent, same rule.
- `frame_[name]` — **about nine per guest** (L47), made at Mode 2 casting by editing the reference; Part 2 may add to Part 1's set. A **forward lean built from a prompt** was read as a zoom and failed; one built by the edit method has passed (`frame_host_i`) — so a lean is only ever made that way, and must pass the frame-set check's zoom limit and an eye check side by side.

The prompts behind the Host's sets are kept in `Fixed_Assets/POSE_LIBRARY.md`. Variants are never generated mid-production to fit a particular line: the library is fixed before a part is produced, and Mode 4 selects from it.

## Tag Convention
Two kinds of tag exist in this project, used at completely different stages:
- `@`-prefixed tags (`@host_base`, `@cam1_host`, `@guest_[name]`, `@voice_host`) are **generation references** — images, seed frames, and voices held on the generation platform and consumed while a shot is generated.
- Un-prefixed `MUSIC_*` and `BRAND_*` tags are **edit-phase assets** — they never reach the generation platform and play no part in generation. They are placed on the timeline in the editor after every clip exists (Mode 6).

**Kling element syntax.** Where a tag is passed to kling.ai as an actual platform element, the reference is **bracketed** — `[@ElementName]`, not the bare `@tag` this project writes. The bare form is this project's internal notation and stays as it is. In practice the distinction rarely bites: voice binding moved to ElevenLabs, and b-roll extras now come from generated start frames rather than elements, so almost nothing is passed as an element any more.

**Where start frames live (2026-09-26, Salah):** `Start_Frames/Host/` (every Host seed frame, permanent) and
`Start_Frames/<Guest>/` (that guest's poses, `landmarks.json`, and the per-part outro wides). File names never change; a regenerated
frame replaces its file in place. `Start_Frames/_generic/` holds the pre-casting `frame_guest`. Per-clip chain frames
(`Shots/start_frames/`) are a different thing and stay with the episode.

## Locked Generation Settings
Fixed for the series. A settings change mid-part changes the performance for no visible
reason and cannot be diagnosed from the output, so these move only by deliberate decision.

- **Platform: kling.ai** (the official platform, not a reseller). Moved from Higgsfield — every credit figure in this project is written for Kling rates.
- **Video model:** depends on the shot. See the model table below; there is no single answer any more.
- **Resolution:** 1080p — every clip, every part.
- **Prompt enhancer: NOT AVAILABLE on Turbo.** It was ON under Kling 3.0 and measurably improved gesture work — it produced semantic gesture alignment nobody wrote into the prompt, a guest pointing at herself on the word "me". Turbo does not offer it — but `P1_054` generated on Turbo came back with natural hand movement anyway, so the existing gesture paragraphs stand. **Do not rewrite prompts for this.** `skill_mode4_produce.md` §5 carries a repair kit for any individual clip that does come back stiff.
- **Camera chip / preset: OFF.** Prompt structure v3 (camera paragraph first, lighting paragraph last — Mode 4 §3) holds the camera and the lighting by itself; tested with the chip off on ~15 clips, 0 px drift (L51). Keeping the lock in the prompt rather than a platform setting is also what keeps the kit portable.
- **Image model:** Seedream 5.0, for camera plates, character sheets and studio seed frames (and their pose edits). **B-roll stills are made with Kling image generation on kling.ai**, as tested (2026-09-26, L37). Reachable two ways: Higgsfield's starter plan, or **fal** pay-as-you-go at ~$0.0675 per image up to 1536x1536 (~$0.135 above that). fal avoids holding a second subscription for four stills a part.
- **Generation route:** the Kling CLI in waves (`cli_wave.py` + `kling_run.mjs`, b-roll via `kling_broll.mjs`; L52, L54), the kling.ai website as the fallback — same prompts, same settings (Mode 4, *Generating*).
- **Voice: ElevenLabs**, speech-to-speech over every talking clip. Not the video model.
- Everything else at platform default; record any exposed parameter here the first time it is observed.

### Model per shot type — measured rates

| Model | Rate | Audio |
|---|---|---|
| Kling 3.0 Turbo | **10 cr/s** | always on, no toggle |
| Kling 3.0 Turbo, **720p** | **8 cr/s** | always on — used only for audio-only talking clips (picture discarded), 2026-09-24 |
| Kling 3.0 Standard, audio on | 12 cr/s | |
| Kling 3.0 Standard, **audio off** | **8 cr/s** | |

**For any clip with no dialogue, Standard with audio off is cheaper than Turbo** — 8 against 10.

| Shot type | Model | Why |
|---|---|---|
| Talking clips | **Turbo** | audio is required anyway, and 10 beats Standard's 12 |
| Silent reactions | **Standard 3.0, audio off** | 8 cr/s, and removing the audio channel removes the cause of invented mouth movement rather than arguing with it in the prompt |
| Audio-only talking clips (picture never used) | **Turbo, 720p** | 8 cr/s; the same voice for a picture that is thrown away |
| Generated b-roll | **Kling image 3.0 still, then Turbo, audio on** | style survival was measured there, and the generated ambience is usable |
| The outro transformation | **Standard 3.0, audio off, start + end frame** | 8 cr/s, 5 s |

**Why reactions failed on Turbo.** `P1_055` came back mouthing gibberish. The cause is most likely the native audio track rather than weak instruction-following: a face plus an audio channel with no dialogue assigned invites the model to invent speech, and the mouth follows what it is generating. Turbo offers no way to turn that off. Standard does. Re-tested on Standard with audio off and it passed — mouth movement measured at mean 1.14 / peak 3.84 against a blink peaking at 9.81, i.e. breath-shaped, not speech-shaped.

### Kling's built-in presets — none are used

They are not model settings. They are **literal text snippets appended to the prompt** — the title is the content, which the typo in "capture the subject's front videw" confirms. Every preset under Shot type, Light and shadow, Frame and Atmosphere describes something **the seed frame already fixes** — framing, lens, lighting, background, mood — and would undo the consistency of the pose set. Two that look safe and are not: *"The speed of the camera motion is slow"* (presupposes motion; on b-roll the move is written in the prompt instead) and *"Shallow Depth of Field"* (already true of the plates; restating it invites a reinterpretation). The stationary preset is no longer needed (v3, L51). **Custom saved presets:** dropped — a preset that reformats or appends text is an invisible input.

### The tool stack — one job each

| Stage | Tool |
|---|---|
| Picture and performance | **Kling 3.0 Turbo / Standard on kling.ai**, image-to-video, 1080p — model chosen per shot type, see the table above |
| Voice | **ElevenLabs**, speech-to-speech, ~17 cr/s, about $2 a part |
| Stills | **Seedream 5.0** for studio frames (Higgsfield starter or fal); **Kling image generation** for b-roll stills |
| Score and SFX | **ElevenLabs** — same $6 Starter plan as the voice pass; Music commercial use is included. Confirm the licence survives cancellation before generating. |

**Voice is no longer the video model's job.** Tested and passed: an accepted clip run through
ElevenLabs speech-to-speech came back with picture and lip-sync untouched and the timbre
replaced. That removes the largest coupling in the pipeline — vocal identity no longer depends
on which video model produced the clip, so the video model became swappable and Kling 3.0
Turbo can be used unconditionally as the cheapest option.

**The generated voice is now a carrier, not the product.** It still has to be a clean,
correctly-timed performance in roughly the right register, because speech-to-speech maps
timbre onto the *source* delivery — a badly mismatched source still gives a poor result. The
registered voice descriptions therefore stay exactly as written. What changes is that they no
longer have to be right, only close.

**Voice drift is now structurally impossible.** Every clip of a character passes through one
ElevenLabs voice. Retire the voice QC gate as a voice check; keep it only as a platform-shift
check.

⚠️ **The ElevenLabs free tier carries no commercial licence and its output cannot be
relicensed afterwards.** The proving clip was made there: it is a test artefact, not an asset,
and must never reach a published part. Every clip in a real part is processed on the paid
plan. Same trap as free-tier music, equally unfixable after the fact.

**What running without the enhancer changes.** The prompt reaching the model is now the prompt we wrote, which makes byte-identical blocks genuinely deterministic — a real gain, and it removes a whole class of unexplained mid-series drift, since the enhancer was a service that could be updated without notice. The cost is that nothing fills in the physical detail we left implicit. The voice QC gate (compare the first, middle and last clip of a part) still catches platform shifts either way.

**Diegetic movement sound is thinner on Turbo.** Observed in testing: on Kling 3.0 a hand returning to the chair arm and legs resettling produced audible movement in the generated track; on Turbo the same beat came back near-silent. Judged **not worth paying 20% more for** (Turbo 10 cr/s against Standard's 12), for three reasons: the audio spec is already "dialogue clean and prominent, ambience minimal"; generated foley is inconsistent clip to clip, which is harder to cut around than none at all; and a continuous room-tone bed runs under the whole part anyway (Mode 6), which is what actually sells the space. If a specific movement ever needs to be heard, place it deliberately from the SFX set rather than hoping the model supplies it.

## Pending Assets
A tag may be registered here before its file exists. Reference a pending tag normally — by name, in the place it will be used — and mark it `PENDING` in that mode's output, rather than inventing its characteristics or leaving it out. The Visual Grounding Requirement applies only to assets that actually exist: never describe how a pending asset looks or sounds. When the file lands in its folder the reference resolves with no rewriting needed, which is the reason these are tags rather than inline descriptions.

## Edit-Phase Assets (Score & Branding)
Diegetic sound — dialogue, ambience, footsteps, fire, wind — is generated natively inside each Kling clip and is never sourced externally (see `skill_mode4_produce.md`). The only audio that must come from outside generation is the deliberate score. Score and branding are both fixed asset sets: created once, reused across every episode, which is what gives the series a consistent identity.

Room tone — `Fixed_Assets/Audio/ROOMTONE_studio.wav`. Not score: a technical bed, **generated on ElevenLabs** — take 04, a 1:48 seamless loop. It is not extracted from clips and does not need to match them, because **nothing in a finished part carries the video model's native studio tone** — dialogue is resynthesised by the voice pass, reactions run with audio off and have no track at all, and b-roll carries its own ambience. The bed does not represent the room; it is the room. Full prompt, build procedure and level target in `Fixed_Assets/SERIES_FURNITURE.md`. Laid under an entire part at low level, never ducking, it glues separately-generated clips into one continuous recording and stops every cut carrying a small audio discontinuity. It also runs under held silences, which is what makes a pause feel like a room instead of a dropout. Permanent — generated once, reused forever.

Score — files in `Fixed_Assets/Audio/`:
**Five cues, all built (`NEXT_STEPS.md` A9):**
- `MUSIC_Theme_Main`: series theme — the whole of `BRAND_opening`. Its 4.0 s unit `MUSIC_Theme_teaser_loop.wav` is also the bed of the act breaks (and `teaser_bed.sh` builds a longer one); `MUSIC_Theme_teaser_runin.wav` hands off to the intro.
- `MUSIC_Drone_Low`: sustained low-tension bed that can sit under dialogue without competing with it.
- `MUSIC_Drone_High`: a higher, thinner bed — distinguished from the low drone by **register**, not dissonance.
- `MUSIC_Outro_Bed`: under the outro transformation and the end card.
- Effects: `SFX_sand` (the intro), `SFX_plate` (every plate entrance).
- **Cancelled, not to be made:** `MUSIC_Sting_Transition` and `MUSIC_Bed_Disclaimer` — the theme's own clock strikes do both jobs.
**Source settled: ElevenLabs.** The Starter plan ($6) lists **Commercial License** and **Music commercial use** as included features, so one subscription covers the voice pass, the score and the sound effects — one platform, one licence, already paid for. ✅ **The licence survives cancellation — confirmed in ElevenLabs' own documentation:** *"Once your subscription ends, you will still have a commercial license to use whatever you generated during that subscription forever."* Generate the whole set on the $6 tier and the rights hold even if the plan is later paused. The **free tier is the opposite** — audio generated outside a subscription *"will always require attribution"* and cannot be relicensed afterwards.

**Full specs, generation prompts and the placement map are in `Fixed_Assets/SERIES_FURNITURE.md`**, together with the intro and outro bumpers and the room-tone build procedure.

Branding — files in `Fixed_Assets/Branding/`:
The channel is **History Answers Back** — التاريخ يرد. Identity is permanent; it is created once and never redrawn per episode.

- `BRAND_mark` — `brand_mark.svg` / `_light.svg`. **The primary mark, used wherever there is horizontal room.** Line one is HISTORY at natural tracking followed by the symbol, the two sized to the same height and together filling the line exactly; line two is ANSWERS BACK in bold beneath. Block ratio ~3.1:1. Symbol and wordmark are one object, so there is no spacing decision at use time.
- `BRAND_mark_stack` — `brand_mark_stack.svg` / `_light.svg`. Symbol above, both lines justified below. Square and near-square formats: end card, social avatar card.
- `BRAND_symbol` — `brand_symbol.svg` / `_light.svg`. ⚠️ **`brand_symbol_720.png` is the INK version** (rgb ~`#12161C` with alpha), so it is invisible on a dark ground — export a light PNG from `_light.svg` before using the symbol over dark picture. A broadcast microphone whose grille holds an hourglass — the microphone is the silhouette so it survives to 20px, the hourglass is the counter-form inside it. Used alone for the corner watermark and anywhere the name already appears. Deliberately era-neutral: no columns or laurels, since the guest list runs from Cleopatra to Genghis Khan to Montezuma.
- `BRAND_wordmark` — `brand_wordmark.svg` / `_light.svg`. Both lines justified to the same width, no symbol. For contexts where the symbol cannot appear.
- `BRAND_avatar` — `brand_avatar.svg`, symbol knocked out of an ink circle. Channel avatar and favicon. Verified legible at 48px.
- **Never break the wordmark as "History Answers / Back"** — the eye reads line one first and lands on the noun phrase. No exclamation mark: the show sells credibility, and that punctuation sells volume.
- Typeface: Oswald, converted to outlines — no font dependency. Source files in `Fixed_Assets/Branding/fonts/`.
- Palette: ink `#12161C` (the acoustic panel), paper `#EDEFF2`, walnut `#9C6B3F` (the slat wall, the only accent), lamp `#E0B071` (the 2700K practical), slate `#5C6672`. One ink per mark, no gradients — it must hold as a 20px avatar and a 40% watermark.
- Watermark placement: **bottom-left** on both cross-shots. Bottom-right collides with the microphone stand.
### Banner geometry — shared by both on-screen text plates

Approved against a real frame. All values are fractions of the frame, so they hold at any delivery resolution.

| | Name banner | Pull-quote |
|---|---|---|
| Width | **42%** of frame width | **55%** of frame width |
| Height | **12.5%** of frame height | **15.5%** of frame height |
| Bottom edge | **90%** of frame height — 10% stays clear beneath | same, 90% |
| Side | bleeds off the **speaker's own side** edge | same side as the speaker |
| Text inset | 2.2% of frame width from the plate's leading edge | same |
| Leading edge | thin accent rule, ~0.3% of frame width | same |

**It bleeds off the edge on purpose.** Touching the frame edge is what makes it read as having slid in from there; a plate with a gap on both sides reads as a detached box sitting on the picture. It stops well short of the far side, and it never runs full width or sits flush to the bottom — that is a news chyron, not this show.

**The side follows the speaker.** The guest sits screen-right, so hers enters from the right; the host sits screen-left, so his mirrors it. This holds even when the speaker's side is the busier half of the frame — association with the person beats a cleaner background.

Both plates share the same bottom line and the same leading-edge rule so they read as one system rather than two graphics.

### Visual treatment — settled

Approved against real frames. **The plates are built — four transparent PNGs in `Branding/`, with the paper, the torn edge and the margin rule baked in; only the text changes per guest.** Files, placement rules and text offsets: `Branding/PLATE_SPEC.md`. (The decision screenshots were removed in the 2026-09-18 file cleanup; the geometry they settled is recorded here and in `PLATE_SPEC.md`.)

**The plate is a piece of toned paper, not a graphic panel.** This is the on-screen text joining the same visual family as the b-roll, so the show reads as one thing rather than a documentary with a podcast's captions bolted on.

| | value |
|---|---|
| Plate | **opaque** toned paper, base `#CDC1AC` |
| Texture | fine tooth + fibre + broad mottling + sparse darker flecks — visible at 1080p, not decorative |
| Leading edge | **torn (deckled)**, irregular, amplitude ~0.6% of frame width |
| Margin rule | walnut `#9C6B3F`, ~0.35% of frame width, **inset ~1.2% from the tear**, running the plate height less 16% top and bottom |
| Name | Anton caps, ink `#12161C`, cap height ~44% of plate height, baseline block starting 15.5% down |
| Second line | Libre Baskerville regular, `#463C38`, ~16% of plate height, starting 70% down |
| Pull-quote | Playfair Display italic, ink, ~28.5% of plate height, two lines at 17% and 54.5% |
| Shadow | offset 4px right / 6px down, 9px blur, 60% — enough to read as a card lying on the picture |

**The rule is a margin rule, not an edge rule.** The original spec put a thin accent rule *on* the leading edge. That fails once the edge is torn: the tear mask eats the rule, and conceptually a printed line on a ripped edge is incoherent. Inset, it reads as the ruled margin of a page — which is what it should have been all along.

**Everything mirrors for the host.** He sits screen-left, so his page enters from the left with the tear on its right, the margin rule inside that tear, and the type right-aligned against it. Not a flipped bitmap — the type never mirrors.

**The paper must be opaque and mid-value.** Two failures found while testing: a translucent paper plate reads as haze over the picture rather than as paper, and a near-white plate reads as a generic broadcast banner and carries no identity at all. Toned stock — the mid-value ground a charcoal drawing is made on — is what ties it to the b-roll and gives ink type its contrast.

Slide timing stays a Mode 6 decision. The geometry and the treatment above are not.

- `BRAND_lowerthird` — the name banner. Slides in from the speaker's side, holds 4.5s, slides out. Two lines: name in Anton caps, role and dates in Libre Baskerville beneath. Used **once per speaker per part**, on their first proper appearance — never on the teaser, which is a cold hook and stays clean. Contents:
  - Host: name, then the show name beneath.
  - Named guest: name, then title and dates — *CLEOPATRA VII / Last ruler of Ptolemaic Egypt · 51–30 BC*. The second line is doing real work for a viewer who does not know when she lived.
  - Composite guest: role, then the word *composite* and the setting — *A GERMAN INFANTRYMAN / composite · 6th Army, Stalingrad, 1942*. This reinforces `BRAND_composite` at the moment he is on screen.
- `BRAND_pullquote` — the on-screen quote. Playfair Display italic, two lines maximum, 4–5s. **Placed after the line has finished, never over it** — the burned subtitle is already carrying those words while she speaks, and running both is the same sentence twice in two typefaces. It lands over **the guest's own held face** after her line (the head of her listening clip), never over a two-up (Mode 4 §13b). Three or four per part, ceiling not target.
- `BRAND_opening` (disclosure card + hook slot + intro), `BRAND_actbreak`, `BRAND_subscribe` — **fixed furniture, built once**, specified in `Fixed_Assets/SERIES_FURNITURE.md`.
- `BRAND_endcard`, `BRAND_composite`, the lower thirds, pull-quotes and context cards — **design fixed, rendered per part** into `Episodes/<Guest>/` by `build_episode_cards.py` (Mode 4 §0b).
- `BRAND_bumper_out` — **built per part in Mode 4** from the outro wide (three references → mark → charcoal still → 5 s transformation, ~43 cr); the only picture of the two of them together.

### Context card — who / where / what, **APPROVED 2026-09-20** against `Episodes/Cleopatra/_v1_archive/context_card_mockup_guest.png` / `_host.png`

A viewer who does not know who Octavian was, or what the Donations of Alexandria were, drops out
of the argument even when every line is right. The context card is a short explainer on the
**first mention** of a person, place or event the argument depends on.

| | value |
|---|---|
| Plate | same toned paper, torn edge and walnut margin rule as the other plates — a **third crop** of `paper_source.png`, so it is not the same paper twice. `BRAND_context_plate_L.png` / `_R.png`, 1382 × 540 at the 3840 reference |
| Size | **36%** of frame width × **25%** of frame height — a little bigger than the pull-quote, because it carries four rows |
| Position | **upper band**, top edge at **7.5%** of frame height, bleeding off the frame edge **opposite the speaker**: `L` (screen-left) when the guest speaks, `R` when the host speaks |
| Why opposite and high | the speaker's own side and the bottom band belong to the speaker (name banner, pull-quote, subtitles, watermark bottom-left); the far side's upper band is empty slat wall in every seed frame |
| Rows | label `WHO` / `WHERE` / `WHAT` — Oswald SemiBold, walnut, tracked, 7.5% of plate height · name — Anton caps, ink, 18.5% (shrinks to fit, never wraps) · gloss — Libre Baskerville Regular, `#463C38`, 10.5%, **three lines maximum** · source — Libre Baskerville Italic, quiet `#625850`, 7.8% |
| Alignment | always **left-aligned** — the plate flips, the type never mirrors |
| Motion | enters from its own frame edge with the same 0.45 s settle as the other plates, rows set in line by line, fades out; **5.5 s**; `SFX_plate` on the entrance only |
| Text | a factual claim — written in Mode 3, sourced like a `[D]` line, ~8–14 words of gloss |

**Differs from the pull-quote on purpose:** a pull-quote is *her words* (italic, speaker's side,
after the line); a context card is *information* (upright, opposite side, as the word is said).
Builder: `Branding/intro_source/context_build.py` (`plates`, `still`, `check`, `mov`); rendered per
episode by `build_episode_cards.py` from the kit's §12 table.

### Two-up — approved 2026-09-22
Both singles side by side, equal halves, host left and guest right, 10 px paper-tone gutter with the
walnut rule — the show's picture of the two of them together, replacing the wide (whose figures read
too large for the chairs). Reference: `Fixed_Assets/Branding/reference/splitscreen_reference.png`.
Placement rules in Mode 4 §8b; cutting in Mode 6. **Since 2026-09-24 it is also the default picture for a
host reaction while the guest speaks** (up to 7 per part), so the guest stays on screen — the series rule
is that the guest carries ≥ 65% of the studio picture (Mode 4 §8b, *Screen share*).

### Two masters — keep a clean one

Lower thirds, pull-quotes, context cards, source attributions and subtitles are burned into the **titled master**, positioned for 16:9, and would be cut off or misplaced in a vertical reel.

Finish every part twice: a **clean master** (picture, dialogue, room tone, music — no text of any kind) and the **titled master** that gets published. Mode 5 cuts reels from the clean master and applies its own vertical text treatment. Cutting a reel from the titled master is a mistake that is invisible until the reel is already vertical.
- Superseded drafts have been deleted. Everything in `Branding/` is current.

### Studio panel — blank in the plate, the mark composited onto the outro still

`cam3_wide.png` carries a **blank** illuminated panel on the slat wall, and it stays blank — lettering in a generation
source is re-rendered, differently, at every step. The mark is composited by `Fixed_Assets/tools/outro_mark.py` onto
each part's outro wide **after** the Seedream step and **before** the charcoal pass, so it is drawn with the room rather
than stamped on it (in a charcoal drawing an empty lit panel reads as a hole). No other shot shows the panel. If the
image model mangles the mark in the charcoal pass, composite it crisp onto the finished drawing instead.

⚠️ **`brand_mark_1600.png` is not ink-centred.** Its canvas is 1600x560 but the ink runs y 0-518 — **0px padding at the
top, 41px at the bottom.** Centring that canvas pushes the visible mark *upward*, and scaling it by height renders it
about 7% small. **Use `brand_mark_trimmed.png`** — the same artwork cropped to its ink, 1593x519, **true ratio 3.07:1**.
The same check applies to any brand PNG before it is placed: measure the alpha bounding box, never trust the canvas.
`brand_symbol_720.png` happens to be near-symmetric and is safe.

**Fixed overlay, measured once — the camera never moves, so these never change:**
- Plate size `2720 x 1536`
- Panel face `x 1121–1591, y 394–556` (470 x 162)
- Resulting mark **399 x 129 at (1156, 410)** — margins left 35 / right 36, top 16 / bottom 17
- `BRAND_mark` at **85% of panel face width**, centred on the INK (`brand_mark_trimmed.png`)
- Treatment: **dark ink on the lit panel** (`#12161C`) — the panel reads ~140 against a frame average of ~60, and dark
  lettering is legible from the camera position where light lettering is not.

## Era Stock Extras — wardrobe text blocks, not images

Reusable, non-guest-specific recurring B-roll characters (soldiers, attendants, officials, crowds) that are not tied to one guest's arc. Written once, reused across every future arc set in a matching era and context.

**These used to be character sheets. They are not any more, and the change matters.**

Two findings retired the sheets together:

1. **B-roll is charcoal and graphite drawing on toned paper** (Mode 4 §10). A photoreal character sheet cannot drive a charcoal frame, so the sheets had nothing left to generate.
2. **Passing a reference image for anonymous extras produces rows of identical faces.** Measured: "the nearest man matching the reference" returned roughly twenty clone faces. Anonymous crowds are generated without a reference, from description alone.

So an era extra is now a **fixed block of wardrobe text**, pasted byte-identical into every b-roll start-frame prompt that needs it, exactly the way `LOCK` is pasted into every dialogue prompt. It fixes continuity and period accuracy at once, and unlike a reference image it cannot clone a face.

### The period gate applies here, and it is where it failed before

`roman_legionary.png` was generated showing **lorica segmentata** — banded iron plate, Imperial kit, generally dated to the early first century **AD**. Cleopatra died in 30 BC. At Actium the legions wore **lorica hamata**, chain mail, with Montefortino-type bronze helmets. The sheet was roughly fifty years early, and it was generated from a prompt written in this project that was never period-checked.

Retiring the sheets does **not** relax the gate — it moves it. The same error would now land in a wardrobe block instead of a PNG, and charcoal hides fine detail but mail against banded plate is a silhouette and texture difference that still reads.

**Before registering any era extra: establish the date of the scenes it appears in, verify costume, armour and equipment against that date rather than against the general image of the culture, and state the evidence in one line beneath the block.** "Roman soldier", "medieval knight" and "samurai" each span centuries of very different kit; the generic mental image is almost always wrong for a specific year. Where a detail is contested, say so and take the conservative option.

**Always name what is absent.** Models default to the famous silhouette, so the block must exclude it explicitly or the default wins.

### Registered blocks

**`legionary_late_republic`** — for any arc touching the Roman military sphere c. 100–30 BC: invasions, sieges, escorts, advancing-forces threat b-roll.

> Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool tunics, plain bronze helmets with a small flared neck guard and hinged cheek pieces, deep red wool cloaks, wide leather belts with hanging studded straps, heavy open-laced leather sandals. No metal shin guards. No plate or banded armour.

*Evidence: lorica hamata with Montefortino-type helmets is the standard reconstruction for Republican legions through the Actium period; lorica segmentata is an Imperial development and does not belong before the first century AD.*

Register a new block here once it is approved for reuse beyond the current arc. A one-off extra tied to a single scene stays in that guest's `Episodes/` folder instead. Before writing a new b-roll casting prompt in Mode 3, check this list for a block that already fits.

### Retired image assets

`roman_legionary.png`, `court_attendant.png` and `antony.png` are **retired as generation inputs** — superseded by wardrobe blocks and charcoal start frames — and are no longer in the project. If Antony is ever cast as a guest in his own right, he gets a fresh Mode 2 casting. The full block list lives in `Era_Stock_Extras/WARDROBE_BLOCKS.md`.
