# FIXED STUDIO ASSETS (Kling 3.0 / 3.0 Turbo, on kling.ai)
All scene scripts must strictly reference these tags:
- `@host_base`: Permanent Host asset (modern investigator, plain black t-shirt, dark jeans).
- `@cam1_host`: Host cross-shot plate, empty. Camera on the right side of the round table looking diagonally across it at the LEFT armchair, seated eye level, medium framing. Floor lamp and dark charcoal panel wall behind that chair, walnut slat wall to the right of frame, near table edge and a microphone in the foreground. A seated Host faces screen-right.
- `@cam2_guest`: Guest cross-shot plate, empty, mirrored. Camera on the left side of the table looking diagonally across it at the RIGHT armchair. Shelf with books and plants behind that chair, walnut slat wall to the left of frame, near table edge and a microphone in the foreground. A seated Guest faces screen-left. Used for AI-cast guests — Archival fallback guests are inserted as stills, not composited here.
- `@cam3_wide`: Symmetrical wide master plate, empty. Both armchairs facing each other across the small round walnut table with two microphones standing on it, walnut slat wall centred behind, floor lamp and charcoal panel wall to the left, shelf with books and plants to the right, woven rug on light oak floor. Used for the cold open, act transitions and closing — not for dialogue coverage.
- `@guest_[name]`: Active AI-cast historical guest character asset — a Fully Anonymous Composite, an Eyewitness Substitution standing in for an Iconic-tier figure, a Reconstructable-tier real figure, or a non-iconic Real Identified Figure.
- `@archival_[name]`: Fallback-only tag for a Real Identified Figure (Standard) whose AI casting was blocked. Presented as a still with camera movement only — never facially animated or lip-synced. Not used for Iconic-tier figures, which are represented on screen by an Eyewitness Substitution instead.
- `@voice_host`: the Host's permanent series voice. Until a platform voice-ID mechanism is in place this is a prose description, and it must be pasted byte-identical into every Host prompt — never reworded, never summarised. Canonical text: *"Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting."*
- `@voice_[name]`: a guest's fixed voice, written once during Mode 2 casting and reused byte-identical for every clip of that guest across both parts. Build it from what the figure's circumstances support — age, bearing, and the register a person in that position would actually speak in — not from the pop-culture performance. Canonical text for `@voice_cleopatra`: *"Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading."* *(corrected 2026-09-20 to match the kit and `VOICES.md` — the 2026-09-18 accent fix reached all 32 kit blocks but not this registry line, which is exactly the file a Part 2 kit would have copied from.)*
- `@voice_newton`: canonical text — *"Voice: male, early 60s. Dry, lightly rasped baritone sitting higher and thinner than the Host's, worn at the top of its range. Clear educated English of an older, more formal kind, consonants over-finished by decades of being heard across a room. Sentences settle downward into a low quiet weight at the end. Never sonorous or pulpit-theatrical, never avuncular."*
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
- Voice QC during production: **superseded.** Every talking clip now passes through ElevenLabs speech-to-speech as a matter of course, so vocal identity comes from one registered voice and drift between clips is structurally impossible. Keep the first/middle/last comparison only as a *picture* check for platform shifts, not as a voice check.

Seating binding — never changes, within a part or across episodes: the Host occupies the LEFT armchair and is only ever shot on `@cam1_host`; the Guest occupies the RIGHT armchair and is only ever shot on `@cam2_guest`. All three plates are the same room seen from three fixed positions — floor lamp and dark charcoal panel wall on the left, walnut slat wall centred, shelf with books and plants on the right, small round walnut table with two stand microphones, woven rug, light oak floor, warm 2700K practicals.

## Asset File Locations
Every asset tag above corresponds to an actual image file on disk, inside this project folder:
- Fixed Studio & Host assets → `Fixed_Assets/` (e.g., `Fixed_Assets/@host_base.png`, `Fixed_Assets/@cam1_host.png`, `Fixed_Assets/@cam2_guest.png`, `Fixed_Assets/@cam3_wide.png`). These are permanent and shared by every episode.
- Reusable Era Stock Extras (see below) → `Era_Stock_Extras/`. **These are now period-checked wardrobe *text blocks*, not images** — see the Era Stock Extras section for why.
- A guest's character sheet, plus any B-roll extra cast specifically for that guest's arc and not registered as reusable → `Episodes/[Guest Name]/` (e.g., `Episodes/Cleopatra/@guest_cleopatra.png`, `Episodes/Cleopatra/@antony.png`). Create this folder the first time Mode 2 casts that guest, and keep everything from that episode in it for easy cleanup later.

## Visual Grounding Requirement
Before writing any prompt, scene, or script that references one or more of these asset tags, retrieve and actually view the current image file(s) for every referenced tag, from the locations above — never rely on the tag name or its text description alone. This matters most for Mode 3's B-roll reuse check and Mode 4's scene generation, where several assets (Host, Guest, a camera plate, B-roll extras) are combined into one shot and need to visually agree with each other on scale, lighting, framing, and wardrobe. If an asset may have been regenerated or replaced since it was last viewed, view it again rather than trusting an earlier look.

## Seed Frames
The camera plates above are inputs. These are what production actually uses: a still of a character already seated in a plate, generated once from that character's reference sheet plus the plate, then used as the start frame for every video generation of that character. Files live in `Fixed_Assets/`.
- `frame_host`: Host seated in the left armchair, facing screen-right toward the guest. Default for all Host dialogue.
- `frame_host_direct`: Host in the same chair, same framing, looking into the lens. Used only for direct address to the audience — the cold open monologue and any narration to camera. Never for dialogue with the guest.
- `frame_guest`: Guest seated in the right armchair, facing screen-left toward the Host. Default for all Guest dialogue, and for silent reaction shots.
- `frame_wide_[name]`: Both characters seated, symmetrical wide, generated from `@cam3_wide`. Establishing, act transitions and the close. **Per-guest, not a fixed asset** — it contains the guest, so it lives in `Episodes/[Guest Name]/`, never in `Fixed_Assets/`.
  **The wide never carries dialogue.** Any line that must be heard is a single. This is structural, not stylistic: ElevenLabs speech-to-speech converts a clip to *one* voice, so a two-speaker clip comes back with both characters in the same voice. Two modes only — a **silent wide** (Standard 3.0, audio off, 8 cr/s: establishing, a beat between acts, a held moment after a hard answer; keep to 3–5s or lay music under it, because two people visibly mid-conversation but mute reads wrong if held long in silence), or a **conversing wide with the audio discarded** (Turbo, audio on), which in practice means only the close, under music and a credit roll.
  **Three variants per guest.** At wide scale only silhouette reads, so the host variants used here are `frame_host` (settled square), `_b` (leaning forward), `_c` (ankle crossed) and `_f` (arm over the chair back). The subtle cross-shot poses — `_d` knuckles at the jaw, `_e` hands clasped in the lap — are invisible at this distance and produce wides that look identical. The guest varies less, which is correct for a composed figure: hands in the lap versus a forearm along the armrest, plus a small change in torso angle.
  **The sign panel must be stated as blank in every wide prompt** or the model invents lettering.

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
- **`frame_host_b`** — leaning forward, elbows on the thighs, hands clasped between the knees. The most engaged, and he sits noticeably closer to camera because of the lean, so it cuts slightly larger than the rest. Reserve it: the pressing question, the moment the interview narrows. Overused it becomes the interrogator problem in body language rather than voice.

**Direct address (`frame_host_direct` set), eyeline into the lens — cold open and narration only, never dialogue with the guest:**
- **`frame_host_direct`** — settled back, hands resting on his thighs (as generated). Neutral narration.
- **`frame_host_direct_c`** — settled back, hands clasped in the lap. Slightly more formal; good for the trust disclaimer, where the delivery should be plain rather than dramatic.
- **`frame_host_direct_b`** — leaning forward, forearms on thighs, hands clasped. Confiding, closing distance with the audience. The cold-open hook and the sign-off.

Guest sets follow the same principle but vary less: a composed figure should not swing between postures, and the narrower range is correct rather than a limitation.

### Pose Variants
Every dialogue shot opens on its start image, so a character generated from one seed frame every time visibly returns to an identical resting position at each cut. Prompts cannot fix this — the start image *is* frame one, and the prompt only controls what happens after it. The variation has to exist in the frames themselves.

Each seed frame is therefore a **set**, not a single image. The original keeps its name and the variants suffix from `b`: `frame_host`, `frame_host_b` … `frame_host_f`. Everything is identical across a set — camera position, lens, framing, crop, wardrobe, lighting, eyeline — and only the seated posture differs.

Set sizes:
- `frame_host` — six. Permanent, generated once, never regenerated for a later episode.
- `frame_host_direct` — three. Permanent.
- `frame_[name]` — **five per guest**, generated at Mode 2 casting. It was six; the sixth was dropped for a measured reason worth keeping: a guest **leaning forward** failed repeatedly, because every generation from that frame shifted the camera zoom slightly. A pose that sits noticeably closer to the lens gives the model licence to reinterpret the framing, and the whole seed-frame architecture depends on it not doing that. The host's leaning-forward variant (`frame_host_b`) survives because it is used sparingly and the drift was smaller at his distance — but **treat any new forward-leaning guest pose as suspect and test it before adding it to a set.** Five poses is enough: a composed figure should not swing between postures anyway.
- `frame_wide_[name]` — ~~three per guest~~ **retired for new guests (2026-09-28, L59)**: the only wide is the per-part outro wide, `frame_wide_[name]_outro(_marked|_charcoal).png`, built in Mode 4 from `cam3_wide.png` + the two last-clip pose frames.

The prompts that generate the Host's permanent sets are kept in `Fixed_Assets/POSE_LIBRARY.md` so they are reused rather than rewritten. Variants are never generated mid-production to fit a particular line: the library is fixed before a part is produced, and Mode 4 selects from it.

## Tag Convention
Two kinds of tag exist in this project, used at completely different stages:
- `@`-prefixed tags (`@host_base`, `@cam1_host`, `@guest_[name]`, `@roman_legionary`, `@voice_host`) are **generation references** — images, seed frames, and voices held on the generation platform and consumed while a shot is generated.
- Un-prefixed `MUSIC_*` and `BRAND_*` tags are **edit-phase assets** — they never reach the generation platform and play no part in generation. They are placed on the timeline in the editor after every clip exists (Mode 6).

**Kling element syntax.** Where a tag is passed to kling.ai as an actual platform element, the reference is **bracketed** — `[@ElementName]`, not the bare `@tag` this project writes. The bare form is this project's internal notation and stays as it is. In practice the distinction rarely bites: voice binding moved to ElevenLabs, and b-roll extras now come from generated start frames rather than elements, so almost nothing is passed as an element any more.

**Where start frames live (2026-09-26, Salah):** `Start_Frames/Host/` (every Host seed frame, permanent) and
`Start_Frames/<Guest>/` (that guest's poses, wide frames and marked versions). File names never change; a regenerated
frame replaces its file in place. `Start_Frames/_generic/` holds the pre-casting `frame_guest`. Per-clip chain frames
(`Shots/start_frames/`) are a different thing and stay with the episode.

## Locked Generation Settings
Fixed for the series. A settings change mid-part changes the performance for no visible
reason and cannot be diagnosed from the output, so these move only by deliberate decision.

- **Platform: kling.ai** (the official platform, not a reseller). Moved from Higgsfield — every credit figure in this project is written for Kling rates.
- **Video model:** depends on the shot. See the model table below; there is no single answer any more.
- **Resolution:** 1080p — every clip, every part.
- **Prompt enhancer: NOT AVAILABLE on Turbo.** It was ON under Kling 3.0 and measurably improved gesture work — it produced semantic gesture alignment nobody wrote into the prompt, a guest pointing at herself on the word "me". Turbo does not offer it — but `P1_054` generated on Turbo came back with natural hand movement anyway, so the existing gesture paragraphs stand. **Do not rewrite prompts for this.** `skill_mode4_produce.md` §5 carries a repair kit for any individual clip that does come back stiff.
- **Camera preset: the stationary preset is permitted and used.** This reverses the previous instruction, which was correct only on Higgsfield, where presets bound the clip to Higgsfield DoP and took it off Kling. On kling.ai the preset is native. The `LOCK` paragraph is still pasted in full alongside it — belt and braces, and it is what keeps the kit portable to any other platform. See the preset rules below.
- **Image model:** Seedream 5.0, for camera plates, character sheets and studio seed frames (and their pose edits). **B-roll stills are made with Kling image generation on kling.ai**, as tested (2026-09-26, L37). Reachable two ways: Higgsfield's starter plan, or **fal** pay-as-you-go at ~$0.0675 per image up to 1536x1536 (~$0.135 above that). fal avoids holding a second subscription for four stills a part.
- **Every clip is made on kling.ai with the camera chip OFF** — prompt structure v3 holds the camera and lighting (2026-09-27, L51; Mode 4 §7). The Kling CLI was tried and set aside — no chip, no Turbo end frame (Mode 4, *Generating*).
- **Voice: ElevenLabs**, speech-to-speech over every talking clip. Not the video model.
- Everything else at platform default; record any exposed parameter here the first time it is observed.

### Model per shot type — measured rates

| Model | Rate | Audio |
|---|---|---|
| Kling 3.0 Turbo | **10 cr/s** | always on, no toggle |
| Kling 3.0 Turbo, **720p** | **8 cr/s** | always on — used only for audio-only talking clips (picture discarded), 2026-09-24 |
| Kling 3.0 Standard, audio on | 12 cr/s | |
| Kling 3.0 Standard, **audio off** | **8 cr/s** | |

**For any clip with no dialogue, Standard with audio off is cheaper than Turbo** — 8 against 10. That inverts the assumption this project was built on.

| Shot type | Model | Why |
|---|---|---|
| Talking clips | **Turbo** | audio is required anyway, and 10 beats Standard's 12 |
| Silent reactions | **Standard 3.0, audio off** | 8 cr/s, and removing the audio channel removes the cause of invented mouth movement rather than arguing with it in the prompt |
| Silent wides | **Standard 3.0, audio off** | 8 cr/s — the cheapest clip type in the kit |
| Generated b-roll | **Turbo, audio on** | style survival was measured there, and the generated wind and footfalls are usable while the SFX set does not exist |
| Closing wide, audio discarded | **Turbo, audio on** | the track is thrown away, but the characters must visibly speak under the credit roll |

**Why reactions failed on Turbo.** `P1_055` came back mouthing gibberish. The cause is most likely the native audio track rather than weak instruction-following: a face plus an audio channel with no dialogue assigned invites the model to invent speech, and the mouth follows what it is generating. Turbo offers no way to turn that off. Standard does. Re-tested on Standard with audio off and it passed — mouth movement measured at mean 1.14 / peak 3.84 against a blink peaking at 9.81, i.e. breath-shaped, not speech-shaped.

### Kling's built-in presets — one is allowed, the rest are forbidden

They are not model settings. They are **literal text snippets appended to the prompt** — the title is the content, which the typo in "capture the subject's front videw" confirms.

**Allowed: the stationary camera preset, and nothing else.** "The camera is stationary" is already the first sentence of `LOCK`, so the preset adds nothing; applying it as well is harmless and is how Test A passed. The paragraph is self-sufficient, which is what keeps the kit portable.

**Forbidden: every preset under Shot type, Light and shadow, Frame, and Atmosphere.** Each describes something **the seed frame already fixes** — framing, lens, lighting, background, mood. Adding "medium shot", "soft light", "simple background" or "mysterious" is exactly the failure the seed-frame architecture exists to prevent, and it would undo the consistency work across the whole pose set.

Two that look safe and are not:

- **"The speed of the camera motion is slow"** — presupposes motion and invites the drift the lock exists to prevent. Never on dialogue. *(On b-roll it is not merely allowed but correct — see Mode 4.)*
- **"Shallow Depth of Field"** — already true of the plates. Restating it gives the model licence to reinterpret it.

**Custom presets: considered and dropped.** The idea was to enforce byte-identical blocks through the tool rather than through careful pasting. Not pursued: the blocks live in the kit, pasting them is no harder than inserting them, and it avoids a class of invisible-input problem if a preset ever reformats or appends text.

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

Room tone — `Fixed_Assets/Audio/ROOMTONE_studio.wav`. Not score: a technical bed, **generated on ElevenLabs** and built from four crossfaded takes. It is not extracted from clips and does not need to match them, because **nothing in a finished part carries the video model's native studio tone** — dialogue is resynthesised by the voice pass, reactions and silent wides run with audio off and have no track at all, and b-roll carries its own ambience. The bed does not represent the room; it is the room. Full prompt, build procedure and level target in `Fixed_Assets/SERIES_FURNITURE.md`. Laid under an entire part at low level, never ducking, it glues separately-generated clips into one continuous recording and stops every cut carrying a small audio discontinuity. It also runs under held silences, which is what makes a pause feel like a room instead of a dropout. Permanent — extract once, reuse forever.

Score — files in `Fixed_Assets/Audio/`:
- `MUSIC_Theme_Main`: series theme, under the cold open and title.
- `MUSIC_Sting_Transition`: short hit for act breaks, cliffhangers, and reveals.
- `MUSIC_Drone_Low`: sustained low-tension bed that can sit under dialogue without competing with it.
- `MUSIC_Drone_High`: heightened tension bed for climaxes and threat B-roll.
- `MUSIC_Bed_Disclaimer`: neutral, restrained bed under the trust disclaimer card, so the disclosure never plays dramatic.
- `MUSIC_Outro_Bed`: closing bed for the sign-off and end card.
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

Approved against a real frame (`Episodes/Cleopatra/lowerthird_mockup.png`). All values are fractions of the frame, so they hold at any delivery resolution.

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

Approved against real frames. **The plates are built — four transparent PNGs in `Branding/`, with the paper, the torn edge and the margin rule baked in; only the text changes per guest.** Files, placement rules and text offsets: `Branding/PLATE_SPEC.md`. Reference renders: `lowerthird_paper_sides.png`, `_options.png`, `_sizes.png`, `plate_placement_guide.png`.

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
- `BRAND_pullquote` — the on-screen quote. Playfair Display italic, two lines maximum, 4–5s. **Placed after the line has finished, never over it** — the burned subtitle is already carrying those words while she speaks, and running both is the same sentence twice in two typefaces. It lands over the silent reaction shot that follows the line, which is what those reactions are already there for. Three or four per part, ceiling not target.
- `BRAND_subscribe`, `BRAND_bumper_in`, `BRAND_bumper_out`, `BRAND_endcard`, `BRAND_disclosure`, `BRAND_composite` — **specified in `Fixed_Assets/SERIES_FURNITURE.md`**, built in Mode 6. All are guest-agnostic: made once, reused every episode. `BRAND_bumper_in` and the cards are motion graphics and need no generation at all; `BRAND_bumper_out` is a single 120-credit generation from the empty `cam3_wide.png` plate, which replaces a 150-credit-per-part closing wide **and removes the only two-character generation in the pipeline**.

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

Lower thirds, pull-quotes, context cards, source attributions and subtitles are burned into the **titled master**, positioned for 16:9. A 9:16 reel pan-and-scans across the frame, so any of that text is cropped, off-centre or half-gone in vertical.

Finish every part twice: a **clean master** (picture, dialogue, room tone, music — no text of any kind) and the **titled master** that gets published. Mode 5 cuts reels from the clean master and applies its own vertical text treatment. Cutting a reel from the titled master is a mistake that is invisible until the reel is already vertical.
- Superseded drafts have been deleted. Everything in `Branding/` is current.

### Studio Panel — the brand goes on in the edit, never in the plate
`cam3_wide.png` carries a **blank** illuminated panel on the slat wall. It stays blank, and
`@cam3_wide` on the platform points at the blank version. The branded reference image in
`Branding/cam3_wide_branded_reference.png` shows the intended result and is **never** used as
a generation input.

Why: the wide plate is the generation source for every wide seed frame and, through those,
every wide clip. Lettering in the source is re-rendered at each step — once by the image
model making the seed frame, then again by the video model across every frame of the clip.
Even if it survives, it is re-rolled independently per clip, so the sign could differ between
act transitions in the same episode. Compositing in the edit makes it pixel-identical in
every clip of every episode.

⚠️ **`brand_mark_1600.png` is not ink-centred.** Its canvas is 1600x560 but the ink runs y 0-518 — **0px padding at the top, 41px at the bottom.** Centring that canvas in any box pushes the visible mark *upward*, and scaling it by height makes it render about 7% smaller than intended. Both faults were live on the studio panel and on the thumbnail before being caught.

**Use `brand_mark_trimmed.png`** — the same artwork cropped to its ink, 1593x519, **true ratio 3.07:1** (which is the ~3.1:1 the brand spec always stated; the canvas ratio of 2.86:1 was the artefact). Centre that, and margins come out even.

The same check applies to any brand PNG before it is placed: measure the alpha bounding box, do not trust the canvas. `brand_symbol_720.png` happens to be near-symmetric and is safe.

**Fixed overlay, measured once — the camera never moves, so these never change:**
- Plate size `2720 x 1536`
- Panel face `x 1121–1591, y 394–556` (470 x 162)
- Resulting mark **399 x 129 at (1156, 410)** — margins left 35 / right 36, top 16 / bottom 17
- `BRAND_mark` at **85% of panel face width**, centred in the face — **use `brand_mark_trimmed.png`**, and centre on the INK, never on a PNG canvas. See the warning below.
- Treatment: **dark ink on the lit panel** (`#12161C`). Verified from the wide: the panel reads at ~140 against a frame average of ~60, and dark lettering is legible from the camera position where light lettering is not.

Applies to every wide clip — cold open, act transitions, closing. One static filter, same
coordinates, applied at assembly. The camera never moves, so this is not per-shot work: it is set once and reused.

### Revised: the mark is baked into the WIDE SEED FRAMES, not composited per clip

The blank-panel rule was written when the wide was expected to carry the cold open, every act transition **and** the close. It no longer does. Act transitions run on b-roll, and the close is a still-based charcoal transformation — which leaves **exactly one wide video generation in a part**, the 4s silent establishing shot.

The original risk was cross-clip inconsistency: a sign re-rolled independently per clip, differing between act transitions in the same episode. **With one wide clip per part, that risk no longer exists.**

And a blank panel actively hurts the outro: in a photograph an empty illuminated panel reads as a lit sign that happens to be out of focus; in a charcoal drawing it reads as a **hole** — a blank white rectangle in the middle of a drawn room. A lit sign in a photograph is a graphic; a sign in a drawing should be drawn.

**So the mark goes into the per-guest wide seed frames**, saved as `frame_wide_[name]_marked.png`, and those are used for both the establishing generation and the charcoal pass. One seed frame, not two.

`@cam3_wide` — the **plate** — still stays blank. It is the generation source for the seed frames themselves, and the mark is composited onto the seed frame after it exists, at the fixed coordinates below.

⚠️ **Check the 4s clip once.** The video model now renders the mark across ~96 frames. The camera is locked and the panel is small, so it should hold, but text is what video models warp. If it wobbles, overlay the crisp mark at the same fixed coordinates — that is the original static filter, unchanged, and it costs nothing.

**Studio panel geometry:** the wide plate carries a blank illuminated panel, roughly 3:1 landscape, at head height on the back wall. The mark is composited onto it in post — never generated into the plate, because the wide is rebuilt for every guest and a generated sign would re-roll each episode. Use `BRAND_mark` — verified against the real plate: warm light type on the slat wall between the chairs reads as a sign installed in that room.

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

`roman_legionary.png`, `court_attendant.png` and `antony.png` are **retired as generation inputs** — superseded by wardrobe blocks and charcoal start frames. Antony's character-sheet prompt is kept on file against the day he is cast as a guest in his own right, where he would appear in the studio photoreal and a sheet would be needed again.
