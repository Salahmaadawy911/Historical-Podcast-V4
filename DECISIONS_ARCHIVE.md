# Decisions archive — the evidence behind the rules

> ⚠️ **Read order (2026-09-28):** the numbered sections §1–§11 below are the 2026-09-18 record, and several were later
> superseded (the camera preset, the wides, the chain pre-lift, the duration figures). The section **"Relocated in the
> skill cleanup — 2026-09-28"** at the end says what replaced each one. The skills state the current rules.

**This is not a queue and nothing here is pending.** Everything in it has been written into the
skills, `STUDIO_ASSETS.md`, `Fixed_Assets/VOICES.md`, `NEXT_STEPS.md` and
`Episodes/Cleopatra/P1_kit.md`. It was held deliberately until the test programme closed, so the
changes landed as one consistent pass rather than the files churning between tests.

**Its job now is to be the reasoning and the measurements behind rules the skills state flatly.**
Where a rule looks arbitrary in a skill, the evidence for it is here. That is what lets the skill
files be short: a rule can be stated in one line *because* the working is recorded somewhere.

⚠️ **This file is the reason the cleanup pass has somewhere to put things.** When compressing a
skill, move the reasoning here rather than deleting it — the failure mode the project keeps hitting
is a rule with no surviving justification, which the next session overrides because it looks
arbitrary. The establishing wide, the accent rule and the VERIFY flags each came back more than
once for exactly that reason.

*(Renamed from `_PENDING_CHANGES.md` on 2026-09-18. The old name said "pending" while the file's own
first line said the opposite.)*

Two sections were **superseded before they were applied** and are marked as such in place:
§9's per-guest "when" decision (withdrawn by §10) and §9b's Pelusium correction (the line was
deleted rather than corrected, so only the worked example survives, as documentation of the gate).

Four things in here were **not file edits** and were resolved elsewhere since: the ElevenLabs paid
tier (done), the host's similarity value (tested, null — see `VOICES.md`), the music, SFX and brand
asset sets (all built), and the thumbnail still prompt. **The one genuinely outstanding item is
emailing Kling support to revoke the One-Click Recreate authorisation.**

---

## Test results so far

| Test | Result |
|---|---|
| **A — camera lock**, `P1_054` 10s Turbo | **PASS** — frame held |
| ~~Preset workflow~~ | dropped, not tested — see §3 |
| B-roll start frame, Kling image gen | **PASS** — sheet not needed for anonymous extras |
| Style: sketch vs photoreal | **SKETCH WINS** — see below |
| B-roll video, `P1_012` 8s | **PASS** — style survived motion |
| C — silent reaction, `P1_055` on **Turbo** | **FAIL** — mouthed gibberish |
| C2 — same, **Standard 3.0, audio off** | **PASS** — breath-shaped, not speech-shaped. Mouth mean 1.14 / peak 3.84; the blink peaks 9.81, 2.5x larger. Shoulders steady (mean 0.74, no frame over 3x mean). |
| Camera lock on **Standard 3.0** (free re-check of C2 clip) | **PASS** — first vs last frame, static regions: wall 1.44, top edge 1.69, table 1.28 mean abs diff; <0.2% of pixels over 25. Same lock line works on both models. |
| Chained clips / native frame extraction | **DEFERRED by decision** — not a separate test. Kling extracts the end frame natively and applies it as the next start frame, so the fix is already in hand. Measure luma drift on the first real chain (`P1_041`) during production; if native extraction is clean, drop the colour-match step from the pipeline. |
| ElevenLabs on the **paid** tier | pending — licensing check, not quality. Free-tier proving clip carries no commercial licence. |
| Wide two-shot `P1_093` 15s | pending — highest-risk generation in the kit |
| Room tone under the voice pass | **MEASURED — room tone does not survive the STS pass.** Source floor -79 dBFS, centroid 950 Hz, 58% of energy in 120-500 Hz (a structured room). ElevenLabs floor -86 dBFS, flat across all bands (17-22% each), centroid 3417 Hz (broadband dither, no room). True even with Remove Background Noise OFF - STS resynthesises, it does not pass the source through. Both floors are inaudible, so there is no cut-to-cut pumping; the consequence is that **no clip in the episode has an acoustic floor**, which promotes the room-tone bed from optional to mandatory and under everything, not just the joins. |
| Level after the STS pass | **-10.4 LUFS quieter than source** (src -23.6 LUFS / -5.1 dBTP; ElevenLabs -34.0 LUFS / -15.6 dBTP, with Speaker Boost already ON). Not a defect, but every converted clip must be loudness-normalised to a fixed target before assembly or clip-to-clip level will wander. |
| Lip-sync timing after the STS pass | **PASS - the speech is sample-aligned; the offset is a container artefact.** ElevenLabs' MP3 export is longer than the source by **exactly 1152 samples = one MP3 granule = 26.1 ms**, written as head padding without gapless flagging, so decoders play it as leading silence. Stripping those 1152 samples puts the lag at **exactly 0 ms** with correlation unchanged (0.887 -> 0.888, nothing clipped off the speech). Control test: round-tripping the source through identical MP3 settings in ffmpeg shifts by 0 ms, so the container is not inherently at fault - this is specific to how ElevenLabs writes the file. **Deterministic: 1152 samples on every clip regardless of length or content.** Fix = export WAV/PCM and it never occurs; if the tier is MP3-only, trim 1152 samples in the same batch pass as loudness. |

⚠️ **Confounder on Test A, worth one line of clarification.** Two things changed at once: the
`STATIC` / "the camera is stationary" **preset** was applied *and* the `LOCK` paragraph was
rewritten. We do not know which fixed the drift. It does not matter operationally while
staying on kling.ai — the combination works and both will always be used. It only matters for
portability: if the pipeline ever moves back to a platform where camera presets are unavailable
or bind to a different model, the prompt wording alone would be unproven. Record it honestly as
"preset + wording, applied together".

---

## Changes queued

### 1. Platform moved to kling.ai — this is the big one

Locked settings, rates and every credit figure in the kit are written for Higgsfield. All of
it needs restating:

| | Old (Higgsfield) | New (kling.ai) |
|---|---|---|
| Video | Kling 3.0 Turbo @ 2.0 cr/s | Kling 3.0 Turbo @ **10 cr/s** |
| Camera control | preset forbidden (binds to DoP) | **preset used and working** |
| Stills | Seedream 5.0, same platform | Seedream 5.0 **stays on Higgsfield starter** |

**Part 1 at Kling rates:** 746s of video = **7,460 credits**, about **8,490** with retries.
Plus 12 Higgsfield credits for the four b-roll stills, plus 10,472 ElevenLabs credits for the
voice pass.

Per-part cost depends entirely on tier: **$45.91 on Ultra** (3.49 parts/month), **$85.79 on
Premier** (1.07 parts/month). Premier does not cover even one part comfortably. Worth naming
the current small tier explicitly in `STUDIO_ASSETS.md` when this is applied.

### 2. Camera preset is now part of locked settings

Reverses the current instruction. `STUDIO_ASSETS.md` and Mode 4 §7 both say never to apply a
camera preset — true on Higgsfield, where presets bind to Higgsfield DoP and take the clip off
Kling. On kling.ai the preset is native and passed Test A. Keep the `LOCK` paragraph as well;
belt and braces, and it is what makes the kit portable.

### 3. Kling's built-in presets — one is allowed, the rest are forbidden

They are not model settings. They are **literal text snippets** appended to the prompt — the
title is the content, and the typo in "capture the subject's front videw" confirms they are
raw strings.

**Allowed: none.** "the camera is stationary" is already the first sentence of `LOCK`, so the
preset adds nothing. Applying it as well is harmless — Test A passed that way — but the
paragraph is self-sufficient, which is what keeps the kit portable.

**Forbidden: every preset under Shot type, Light and shadow, Frame, and Atmosphere.** Each one
describes something the **seed frame already fixes** — framing, lens, lighting, background,
mood. Adding "medium shot", "soft light", "simple background" or "mysterious" to a prompt is
exactly the failure the seed-frame architecture exists to prevent, and it would undo the
consistency work across the whole pose set.

Two that look safe and are not:

- **"The speed of the camera motion is slow"** — presupposes motion and invites the drift we
  just fixed. Never.
- **"Shallow Depth of Field"** — already true of the plates. Restating it gives the model
  licence to reinterpret it.

**Custom presets: dropped.** The idea was to enforce byte-identical blocks through the tool
rather than through careful pasting. Not pursued — the blocks are written in the kit and
pasting them is no harder than inserting them, and it avoids a class of invisible-input
problem if a preset ever reformats or appends text. Prompts are pasted by hand, as before.

### 3b. PERIOD ACCURACY GATE — a real gap, found the expensive way

`roman_legionary.png` shows **lorica segmentata**, the banded iron plate armour. That is
Imperial kit, generally dated to the early first century **AD**. Cleopatra died in 30 BC; at
Actium the legions wore **lorica hamata** — chain mail — with Montefortino-type bronze helmets.
The sheet is roughly fifty years early.

**The sheet was generated from a prompt written here, and the prompt was never period-checked.**
That is the actual failure: research rigour was applied to the dialogue — primary sources named,
the library myth corrected, the carpet story corrected — and not at all to the visual assets.
Mode 1 checks Likeness Tier and Recognition Tier. Mode 3 checks IP filter safety. **Nothing
asks whether the costume is right for the date.**

This matters more for this show than most. The positioning is research-led, and the audience
that rewards that is precisely the audience that notices armour.

**Skill change to apply: a period check on every cast extra.** Belongs in `skill_mode3_outline.md`
where B-roll characters are cast, and in `skill_mode2_cast.md` alongside the tier checks. Shape:

> Before writing any extra's casting prompt, establish the **date** of the scenes they appear in
> and verify the costume, armour and equipment against that date, not against the general image
> of the culture. State the evidence in one line beside the prompt. Where a period detail is
> contested, say so and pick the conservative option. "Roman soldier", "medieval knight",
> "samurai" and similar span centuries of very different kit — the generic image is almost always
> the wrong one for a specific year.

**Also write the excluded items in.** Models default to the famous look, so the prompt must name
what is *not* there — "no plate or banded armour", "no metal shin guards" — or the default wins.

### 3c. Asset audit — consequences of the above

- **`Era_Stock_Extras/roman_legionary.png` — WRONG, regenerate.** Reused by three b-roll rows in
  Part 1 and by every future Roman episode, so fixing it once pays repeatedly.
- **`Episodes/Cleopatra/antony.png` — check.** Described as a brown leather cuirass with bronze
  fittings. A muscled or leather cuirass on a commander c. 40–30 BC is defensible; verify rather
  than assume.
- **`Episodes/Cleopatra/guest_cleopatra.png` — believed correct.** Cream linen chiton, draped
  himation, thin flat gold diadem: Hellenistic Greek dress, right for a Ptolemaic ruler.
- **`court_attendant.png` — check** against Ptolemaic court dress.

**Plus a fixed wardrobe text block per recurring extra**, byte-identical in every prompt, the way
`LOCK` is. It fixes continuity and accuracy at once, and unlike a reference image it cannot
produce a row of identical faces:

> Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool
> tunics, plain bronze helmets with a small flared neck guard and hinged cheek pieces, deep red
> wool cloaks, wide leather belts with hanging studded straps, heavy open-laced leather sandals.
> No metal shin guards. No plate or banded armour.

### 3d. STYLISED B-ROLL — confirmed by test, adopt it

All generated b-roll moves to **charcoal and graphite drawing on toned paper**. Pexels is
dropped entirely (+280 credits a part, about $1.72, for one coherent visual language and no
third-party licence surface at all).

**Why it won, measured rather than judged.** Against a frame of the studio:

| | value | saturation |
|---|---|---|
| Studio | 0.354 | 0.463 |
| Sketch b-roll | 0.471 | **0.236** |
| Photoreal b-roll | 0.314 | 0.496 |

The photoreal version sits almost on top of the studio's own numbers — it reads as the same
footage slightly darker, which is exactly the ambiguity to avoid. The sketch is brighter and
half as saturated, so the cut registers as a deliberate shift, while the hue stays in the same
warm family so it does not clash.

**The style survives animation.** `P1_012` at 8s held the drawing to the last frame — no
resolution into photographic footage. Stroke stability between consecutive frames was flat
across the clip (mean diff 8.96 / 9.03 / 9.01; high-frequency noise 13.75 / 13.73 / 13.68),
which means the change is camera and subject motion, not texture boiling. Shadows tracked the
figures correctly, which requires the model to hold the light geometry rather than copy texture
forward.

**Camera moves are allowed on b-roll and forbidden on dialogue.** The lock exists to protect
seed-frame continuity and the multi-camera studio grammar; neither applies to a cutaway. And
the rigidly locked interview is what gives a moving cutaway its value. Discipline: slow, one
move per shot, always with a reason. Vocabulary — slow push in (drawn toward something), slow
pull back (reveals, endings), slow tilt (scale, detail to context), slow lateral drift
(reliefs, objects, texture). Never handheld.

**This reverses one earlier rule:** "The speed of the camera motion is slow" is forbidden on
dialogue and correct on b-roll.

**B-roll prompts describe motion, not content.** The start frame already carries composition,
style, light and figures. Re-describing them invites reinterpretation instead of animation —
the same principle as the seed frames. Four paragraphs: the move, the medium stated as
persistent, what moves, the audio.

**The medium must be framed as persisting**, with the failure mode named: *"it stays a drawing
for every frame … it never resolves into photographic footage."* Stating the style once is not
enough; models drift toward photoreal.

**Assembly note:** generated b-roll warms and darkens slightly across a clip (over 8s:
saturation 0.238 → 0.277, shadow 31.4% → 38.1%). Normalise each b-roll clip against its own
first frame, the same way chain luma is compensated.

**"Nothing happens" is correct for b-roll under dialogue.** The viewer is listening; an event on
screen pulls attention off the line. Spend visual interest on the act transitions instead,
which carry no dialogue and must hold attention alone.

### 3e. CHAINS — native frame extraction may delete a whole procedure

Kling can extract a clip's last frame and apply it directly as the next generation's start
frame, in-app. No download, no re-upload.

**This may retire most of the chain instructions in the kit**, which currently read:

> extract with `ffmpeg -sseof -0.08 -i clip.mp4 -frames:v 1 out.png`, no scale filter, no range
> conversion — and upload it as this clip's start frame. Chains lose about 1.5% luma per link;
> lift the extracted frame before uploading.

Both halves of that were workarounds for problems that may not exist on this path:

- **The colour-range fault** — extracting a frame with a range conversion lifted saturation about
  7% (14.72 → 15.82). That was caused by *our* ffmpeg extraction, not by the platform. If Kling
  hands the frame straight across internally, the fault cannot occur and the `-sseof` recipe is
  simply unnecessary.
- **Chain luma loss of ~1.5% per link** (79.62 → 78.81 → 77.50 → 75.76) was measured on
  Higgsfield with **Kling 3.0**. Unmeasured on Turbo via native extraction. The instruction to
  pre-lift the frame may now be actively wrong — compensating for a loss that is not happening
  would make each link progressively brighter.

**Do not delete the instructions until measured.** Three chained clips exist in Part 1:
`P1_041`, `P1_056`, `P1_092`, all single-link. Cheap check when the first one is generated:
compare the mean luma of the source clip's last frame against the new clip's first frame. If
they match, both instructions go and the "never exceed three links" cap can be reconsidered
too — that cap existed because the loss accumulated.

**Keep the cap at three links until proven otherwise.** It costs nothing and the failure it
prevents is invisible until several links in.

### 3f. MODEL PER SHOT TYPE — measured rates, three-way split

| | rate | audio |
|---|---|---|
| Kling 3.0 Turbo | 10 cr/s | always on, no toggle |
| Kling 3.0 Standard, audio on | 12 cr/s | |
| Kling 3.0 Standard, **audio off** | **8 cr/s** | |

**For any clip with no dialogue, Standard with audio off is cheaper than Turbo** — 8 against 10.
That inverts the assumption the kit was built on.

| Shot type | Model | Why |
|---|---|---|
| Talking clips | **Turbo** | 10 cr/s, audio required anyway, cheaper than Standard's 12 |
| Silent reactions | **Standard 3.0, audio off** | 8 cr/s, and no audio channel for the mouth to follow |
| Generated b-roll | **Turbo, audio on** | style survival was measured there; the generated wind and footfalls are usable and the SFX set does not exist yet |
| Wide | **Turbo, audio on** | the track is discarded, but the characters must *speak* on camera for the credit roll — audio off would likely leave them silent |

**Why reactions failed on Turbo.** `P1_055` came back mouthing gibberish. Most likely cause is
not weak instruction-following but the **native audio track**: a face plus an audio channel with
no dialogue assigned invites the model to invent speech, and the mouth follows what it is
generating. Turbo offers no way to turn that off. Standard does — which removes the cause
rather than arguing with it in the prompt, and costs less.

If the mouth still moves with audio off, the fallback is a prompt fix following the camera-lock
lesson: state what the mouth **is** rather than what it is not — *"Her mouth is closed, the lips
resting lightly together, the jaw relaxed and still. The only movement in her face is a slow
blink and the small rise and fall of breathing."* Same construction as "all movement in the shot
belongs to the person": name where motion is permitted.

**Revised part total:** 774s of video — spine 616 @10, reactions 42 @8, b-roll 101 @10, wide 15
@10 → **~7,656 credits**, plus ElevenLabs and fal stills.

### 4. Element syntax, only if elements are ever used

Kling references elements as `[@ElementName]`, bracketed. `STUDIO_ASSETS.md`'s tag convention
is written for Higgsfield's bare `@tag`. Not urgent — voice binding was dropped in favour of
ElevenLabs, and the only remaining element use would be b-roll extras, which now come from
Seedream start frames instead.

### 5. Already applied before the hold, listed for completeness

The ElevenLabs voice pass went into Mode 2, Mode 4, `STUDIO_ASSETS.md` and
`Fixed_Assets/VOICES.md` before this hold began. Those stand.

---

### 6. Mode 2 — Voice Design block (NEW, replaces the placeholder voice line)

Every guest gets **one designed voice, created once at cast time** and reused for
every clip across both parts. Designing per-clip is how a character stops sounding
like one person.

**Template** (ElevenLabs Voice Design format):

```
Native <Language>. <Gender>, <Age range>. Perfect audio quality.
Persona: <2-5 words>. Emotion: <2-3 adjectives>.
<1-2 sentences: timbre, pacing, delivery.>
<One sentence placing the English.>
```

**Writing rules**

- Never use the word **accent** - it causes dialect drift. Place the English
  descriptively instead: "Placeless formal English, neither British nor American."
- Never use **reverb, echo, phone, room, mic** or any production term - the docs
  state these degrade output.
- **Preview text must be a real line from the Mode 3 outline**, two sentences or
  more. The default preview sentence locks the voice to a generic register; a
  script line locks it to the show. Longer preview text also measurably stabilises
  the result.
- **Do not ask for archaic or "period" delivery.** The guest speaks modern English
  in a modern interview; the period lives in the picture and the content, not the
  vowels.

**The accent decision is editorial and must be defended in one line on the cast
sheet.** Two failure modes to name and reject explicitly:

- the modern-nationality default (Cleopatra was Ptolemaic Greek - a modern Egyptian
  voice is simply wrong)
- the documentary cliche (clipped Received Pronunciation for anyone ancient)

Placeless formal English is the safe answer and needs no apology; anything else
needs a reason written down.

**Hard rule:** the designed voice is a **voice-changer TARGET, never a
text-to-speech source.** Generating a guest line as TTS discards the Kling
performance and the lip sync with it. Design -> save -> run the Kling clip through
voice changer against the saved voice.

**Project-locked settings** (record the voice ID and these values in
`Fixed_Assets/VOICES.md` at cast time):

| Setting | Value | Why |
|---|---|---|
| Model | Eleven English v2 | |
| Stability | high | 65+ clips must match each other |
| Style Exaggeration | **0-10** | STS already carries an approved performance; style invents delivery on top of it and is the documented source of instability |
| Similarity | **high for designed guest voices** | a designed voice is already native-English, so there is no accent to bleed. This differs from the host's own clone - see below |
| Remove Background Noise | OFF | nothing to preserve either way; keeps the chain honest |
| Speaker Boost | ON | |
| Output format | highest non-lossy the tier offers | MP3 128k into a YouTube encode is two lossy generations |

**Host voice is the exception.** The host's voice is a clone of a non-native
speaker, so similarity pulls the clone's own accent through. Similarity must be
tuned by ear on a test clip - high enough to keep identity, low enough that the
source read's English survives. That tuned value goes in `VOICES.md` and is not the
same number as the guests'.

### 7. Edit-stage rules from the voice-pass measurement

1. **Loudness-normalise every converted clip to one fixed target** before assembly.
   The STS pass lands ~10 LUFS below source and the offset is not guaranteed
   constant across clips.
2. **Do NOT slip clips on the timeline.** The earlier "-1 frame" rule was wrong -
   diagnosed as one MP3 granule (1152 samples / 26.1 ms) of head padding in
   ElevenLabs' MP3 export, not a timing error in the model. Prefer WAV/PCM export,
   which removes it at source. On an MP3-only tier, trim it deterministically in
   the same pass as (1):

   ```bash
   ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,\
   loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
   ```

   Re-verify the 1152 figure once against a WAV export if the tier ever offers one;
   it is a property of their encoder, not of the audio.
3. **Room-tone bed runs under the whole episode**, not just under the joins. No
   clip has an acoustic floor after the voice pass.

### 8. STRUCTURAL — two-speaker clips cannot pass the voice pass

ElevenLabs speech-to-speech converts a clip to **one** voice. A clip containing two
speakers comes back with **both characters in the same voice**. This is not a
quality risk, it is a structural incompatibility.

Consequences, to be written into Mode 3 and Mode 4:

- **A two-shot can carry a conversation as picture, never as dialogue.** Any line
  that must be heard belongs in a single-character clip.
- `P1_093` was already correct in discarding its audio. The kit's note calling it
  "the least reliable generation in the kit: two characters in one clip is where
  voice attribution fails" **overstates the risk for this show** — attribution is
  irrelevant when the track is discarded, and this shot additionally sits under
  music and a credit roll. Reword the note.
- Because the audio is discarded, the scripted lines and both `Voice:` blocks come
  out of the `P1_093` prompt. They exist only to drive attribution that is thrown
  away, and two voice blocks in one prompt is an unnecessary failure mode.
- The only escape hatch, if a future episode genuinely needs a two-hander with
  audible dialogue: split the clip's audio at the turn, convert each segment
  against its own voice, reassemble. Costly and fiddly — treat as a last resort and
  write the outline to avoid needing it.

Also: use `frame_wide_cleopatra_c` as the `P1_093` start frame rather than the base
variant. `CAST.md` designates `_c` for openings and closings; this is a closing.

### 8b. The wide-shot rule (Mode 3 + Mode 4)

Follows directly from §8. **Any line that must be heard is a single. The wide never
carries dialogue.**

Where a beat genuinely needs both characters and their words — the closing exchange
is the model case — write it as **host single + guest single + a non-talking wide**,
rather than one two-shot. The lines survive the voice pass because each clip has one
speaker; the wide supplies the geography.

Two legitimate modes for the wide:

| Mode | Model | Rate | Use |
|---|---|---|---|
| **Silent wide** | Standard 3.0, **audio off** | **8 cr/s** | establishing, a beat between acts, a held moment after a hard answer. Proven on the reaction test: audio off gives breath-shaped stillness, not mouthed gibberish. Keep to 3-5s, or lay music under it - two people visibly mid-conversation but mute reads wrong if held long in silence. |
| **Conversing wide, audio discarded** | Turbo, audio on | 10 cr/s | only where music covers it. In practice: the closing and credit roll, i.e. `P1_093` and little else. |

**The silent wide is the cheapest clip type in the kit** - below every talking clip.
Mode 3 may now use a two-shot beat freely for pacing, which it previously had to
avoid, provided the words live in the singles.

Budget note: splitting a two-hander costs three generations where the kit had one.
Worth it mid-episode for drama; **not** worth it for the closing, where the lines sit
under a credit roll and nobody needs to hear them. `P1_093` stays as a single
conversing wide.

### 9. The live-event frame — an undeclared series decision

The Cleopatra kit frames the interview as happening **at a moment in history**, with
news arriving during the conversation and a clock running on the guest's life
(`P1_089` "while we have been sitting here"; `P1_092` "I have very little time
left"). This was never surfaced as a decision — it arrived embedded in the dialogue.
It must become an explicit **Mode 1** choice before it propagates to every guest.

**Keep the device, but not as a template.**

- The *when* is a per-guest editorial decision: some interviewed at their peak, some
  at their fall, some in retrospect in old age. Every guest at the edge of their
  downfall is a formula by episode four, and it locks out the back half of a life.
- Record the chosen moment, and the reason, on the pitch sheet.

**The posterity rule (Mode 3, Mode 4).** A guest sealed in their own moment cannot
answer posterity — Cleopatra does not know what Plutarch wrote or what two thousand
years made of her. So: **the host carries posterity, the guest answers from her own
experience.** The host brings the later myth; she describes what actually happened.
This is already how the carpet (`P1_041`) and library (`P1_046`) lines work — it just
was never written down, so future scripts will drift into the guest knowing things
she cannot know.

### 9b. KNOWLEDGE GATE (sibling to the PERIOD ACCURACY GATE in §3b)

The period gate checks what things **look** like. Nothing checks what a guest can
**know**, or whether described events happened the way the line says. Same class of
error as the armour, different axis. Add to Mode 3 (outline) and Mode 4 (produce):

For every line, check:

1. **Can this speaker know this, at this moment?** Later sources, later
   interpretations and posterity's verdict belong to the host, never the guest.
2. **Did the event happen the way the line describes it** — not just the right place
   and date, but the right *method*?
3. **Is a named specific available instead of a vague one?** Named places and people
   are both better drama and easier to verify.

**Worked example — caught live, and it had passed every existing check:**

> `P1_089` as written: "Octavian's forces have landed in the delta. They are already
> ashore."

"Landed / ashore" reads as an amphibious assault. Octavian advanced on Egypt
**overland from Syria, taking Pelusium** on the eastern edge of the delta; the
seaborne pressure that summer came from the **west**, with Cornelius Gallus at
Paraetonium. Right geography, wrong method.

> Replacement: "Octavian has taken Pelusium. He is at the eastern edge of the delta,
> and he is coming."

Accurate, and stronger writing — a named place that fell beats a vague landing.
**Verify against Cassius Dio Book 51 before applying.**

### 9c. Part 1 ending — confirmed, no change

Close Part 1 on `P1_092`. Her line carries the Part 2 hook and a double meaning
(time in the interview, time in her life). The `P1_093` wide exchange does the same
job a second time and more weakly; splitting it into audible singles would cost
~100 credits to follow a strong button with a limp one. The wide stays picture.

### 10. FORMAT DECISION — retrospective, not live (supersedes §9)

**Measured before deciding:** of 65 spoken lines in `P1_kit.md`, only **3** carry a
live-event frame. The script is already retrospective. The live frame was introduced
in two shots at the end (`P1_089`, `P1_092`) and contradicts the other 62.

The cold-open hook proves the intent was always retrospective:

> "Its last ruler has been called a seductress for two thousand years. Mostly by the
> men who conquered her. Tonight she answers for herself."

That line requires her to know posterity. ("Tonight" is broadcast register, not a
historical moment — it stays.)

**The frame, for all guests, all episodes:**

The guest speaks **from outside their own life**. They know everything that happened
to them, including how it ended, and they know what was said and written about them
since. They answer **as themselves** — no modern vocabulary, no scholarly framing, no
citing of sources.

**The host carries posterity; the guest answers from experience.** The host puts the
later claim ("the story goes you were rolled out of a carpet"); the guest says what
actually happened. This is already how `P1_041` and `P1_046` work.

Why this replaces §9 rather than refining it:

- **No per-guest "when" to choose**, so the deathbed-formula risk disappears instead
  of needing management.
- **Safer on authenticity.** A simulated live historical moment edges toward
  pretending; a figure reflecting is transparently a device, consistent with the
  disclosure card.
- **It is where the show's best material lives** — a guest can only answer a charge
  they know was made.

§9's per-guest "when" decision is **withdrawn**. §9b (the KNOWLEDGE GATE) **stands**,
with its check 1 reworded: the guest may know their whole life and the record about
them, but speaks in their own register — the host supplies modern framing and
vocabulary. The Pelusium correction in §9b still applies to whatever replaces
`P1_089`.

### 10b. Part 1 ending — host-driven hand-off (replaces §9c)

Structure, repeatable for every guest:

**question -> short guest response that opens more than it closes -> host hands off
-> wide, music, credits.**

**Mode 3 picks the break point by finding the strongest unanswered question, not by
the clock.** Break where the audience most wants the answer.

Requires a **new clip**: the host's hand-off. Currently `P1_092` (guest) cuts
straight to the wide, and the wide carries no dialogue (§8b).

Draft — wording to be confirmed, syllable counts and duration floors computed on
application:

- **`P1_089` HOST** — "One more thing before we break. Most people, if they know one
  thing about you, know that you loved Mark Antony. Was that what it was?"
- **`P1_092` GUEST** — "It was a treaty first. Whether it became more than that is a
  question I have never been asked by anyone who wanted the true answer."
- **`P1_092b` HOST (new)** — "Then that's where we'll pick it up."

Points Part 2 at Antony and Actium. Removes the clock line and the Pelusium line
together.

### 11. SOURCE PROVENANCE — the list is derived from the script

Publishing a sources list in the description is making a claim, so the list must be
**generated from the script**, not assembled beside it.

Every dialogue line carries a tag in the kit:

| Tag | Meaning | Requirement |
|---|---|---|
| **[D] Documented** | attested in the record | the source is named on the line |
| **[I] Inferred** | consistent with the record, a reasonable reconstruction | the basis is named |
| **[V] Voice** | connective tissue, rapport, phrasing | carries no factual claim |

**Hard rule: a [V] line may not contain a factual assertion.** This is what stops
invention leaking into the parts an audience will believe.

The published source list is then built from the [D] and [I] tags: nothing cited that
is not used, nothing claimed that is not cited. Applies to Mode 3 (tags assigned at
outline) and Mode 4 (tags carried into the kit and audited before generation).


---

## 2026-09-22 — Moved out of the mode headers: why every mode saves its output to a file
Each mode's header used to carry: *"Cleopatra's pitch and outline were never saved as files — Part 1's
dialogue survives only inside `P1_kit.md`."* That is the incident behind the file-handoff contract
(every mode writes its output to `Episodes/<Guest>/…` before it ends). The rule stays in every header;
the Cleopatra-specific history lives here. **Open consequence:** before Mode 3 runs for Cleopatra
Part 2, `PITCH.md` and `OUTLINE.md` must be written from the Part 1 kit (see `NEXT_STEPS.md` B4).

## 2026-09-22 — Generalisation pass (discussion point 1)
The modes were audited for Cleopatra-specific assumptions. Found and fixed: (1) the guest was written
as a woman in the recipes and the attribution rule said *"The woman says:"* — guest label, pronouns,
register, emotional ceiling, interruption style and gesture range now live in a **performance
profile** in each guest's `CAST.md` (Mode 2), and Modes 3/4/6 read it; (2) every gate and tool was
hard-wired to `P1_kit.md` — all now take a part number, and Part 2+ renders carry a `p<N>` tag;
`sources_audit.py` audited every guest against a hard-coded Cleopatra source list — it now reads the
episode's `card_data_p<N>.json`; (3) the duration model is now re-measured per guest. Found on the
way: `junction_scan.py` had been **silently checking zero lines** since the inline-attribution change
of 2026-09-21 — fixed, and it now fails if it scans fewer lines than there are talking rows.

---

# Relocated in the skill cleanup — 2026-09-28

The skill files were rewritten to state each current rule once. What came out of them is recorded below — the
superseded versions, the measurements that decided them, and the procedures of tests that have passed. **The verbatim
pre-cleanup files are in `_archive/skills_pre_cleanup_2026-09-28/`**; this section is the readable index of what they
held. Every skill now carries a *Tested and ruled out* list pointing here and to `Fixed_Assets/LESSONS.md`.

## R1. The camera lock — every version, in order

| when | wording / setting | result |
|---|---|---|
| Higgsfield era | *"The camera does not move. Framing, lens, lighting and background stay exactly as the start frame throughout."* | ignored — slow drift. Video models handle negation badly ("does not **move**"). |
| 2026-09-18 (Test A, `P1_054`) | lock v1 + Kling's stationary preset, applied together | **PASS**, but confounded — two changes at once. |
| 2026-09-24 (`P1_020`, first take) | full lock v1, **no preset** | camera moved → the preset was doing real work (L3). |
| 2026-09-25 (`P1_058`, L18) | lock v2, no chip | held, ≤ 2 px. |
| 2026-09-25 (CLI, L23, L27, L28) | v2 / end-only wording through the CLI | drift on 3 of 16; long Turbo clips about half the time (P1_018 39 px orbit). |
| 2026-09-26 (L32, L33) | back to the website, chip on; v2 still drifted | v1 restored verbatim, with *"Only one person is in the frame."* (L19). |
| **2026-09-27 (L51)** | **structure v3**, chip OFF | **0 px on ~15 clips incl. 13 s talking and reactions; lighting drift ~1.4 % vs ~1.8 %.** Current. |

Lock v1, verbatim: *"The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom.
Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot
belongs to the person; the camera contributes none."* Its last clause existed because a lock stated as pure absence of
motion froze the performer too — the same failure as scoping a register constraint to movement.

Lock v2, verbatim: opening *"Static camera shot. The camera is stationary on a tripod; the framing, lens, lighting and
background stay exactly as in the start frame for the whole clip."*, closing *"Static camera shot."*, no camera-move word
anywhere (third-party Kling guides said the same). L18's theory — naming pan/tilt/zoom invites them — **did not hold up
with the chip on**; not to be re-opened without a measured A/B.

**Paragraph leading space (2026-09-21, `P1_008_B`):** Kling stripped the blank line between paragraphs and fused
sentences (*"…contributes none.The host, calm…"*); a single leading space made the movement paragraph land. Dropped for
studio prompts with v3, which was tested without it.

**Kling presets (2026-09-18):** they are literal text snippets (the typo *"front videw"* shows it). The stationary preset
was allowed; everything under Shot type / Light and shadow / Frame / Atmosphere forbidden; custom presets dropped. With
v3 no preset is used.

## R2. The duration model — every version

- **Previous platform:** ~2 words/s (*21 words at 10 s, 15 at 8 s, 14 at 7 s*); then **3.85 syl/s** measured (25 syl in
  6.40 s, 27 in 7.11 s) → *speech = syllables ÷ 3.85 + ~1 s per break + ~0.5 s tail*, aim the floor + 0.5 s, and
  **"never round up"** (slack became a mid-line pause: 27 syllables at 13 s → a 3.3 s pause; 25 syllables at 12 s →
  1.8 s). The 34-syllable line (floor 11.3 s) failed at 10 s and compressed at 12 s.
- **v2 (2026-09-21):** six Turbo clips (`P1_004/006/007/055/057`, `P1_008`): ~4.3 syl/s (4.1–5.4), lead 0.8 s seed /
  0.3 s chained, **0.5 s per break**, 0.4 s tail, rounded up. The old figures over-padded every clip by 1–2 s.
- **v3 (2026-09-24):** break 1.0 s — `P1_013` took 1.1 s at its break, `P1_020` 1.6 s and 1.0 s, and two clips ran speech
  to the last frame.
- **v4 (2026-09-25, L21, L24):** 1.3 s per break (the measured average of kept takes), +0.5 s on lines ≥ 9 s, never
  rounded down — `P1_016` rounded 4.06 → 4 s ended 0.15 s after its word; `P1_015` (34 syl, 12 s) was cut off with pauses
  of 1.45 / 1.6 s at 4.1 syl/s. Part 1 went 7,830 → 8,206 cr.

## R3. The timing-cue and vendor-syntax A/Bs (2026-09-20/21)

Kling's audio guide puts the delivery note *inside* the attribution and uses temporal markers (*"Immediately"*). Tested
on `P1_008`, same seed and line, 11 s: A (inline note) onset 0.60 s, 7.15 s voiced at ~5.0 syl/s, pauses 1.1/0.6/1.2 s;
B (+ *"He begins speaking immediately."*) onset 0.35 s, 6.65 s at ~5.4 syl/s, pauses 1.3/2.2 s. **Cue not adopted** — it
gave the onset back as a longer pause and rushed the line. The inline note was kept, then replaced by the label form
(T8, 2026-09-24).

## R4. The host's direct-to-guest turn — the whole path

1. 2026-09-19 plan: **start + end frames** on pose pairs (same body, only the eyeline differs) — `frame_host_direct` ↔
   `frame_host` (settled back), `_direct_b` ↔ `_b` (leaning forward), `_direct_c` ↔ `_e` (hands in lap). Fix ladder:
   end frame → chain → cut mid-turn → something between them.
2. 2026-09-20 (`P1_004`): **Turbo has no end-frame slot**; the prompt alone produced the head turn (9.5–11.0 s, not
   rushed), the chained join seamless in luma → chain became the default. Found because removing the establishing wide
   exposed a join the wide had been hiding.
3. 2026-09-26 (L34): Turbo's end eyeline was luck (right once, off to the left on the retake) → Standard + audio + end
   frame on the guest-facing pose (12 cr/s).
4. 2026-09-26 (L38): that snapped — line 1 ended, 2.6 s of silence, a ~0.5 s head snap with torso and hands, a hold, then
   line 2. Turn wording rewritten (no pause, turn across the whole sentence, eyes arrive on the last word, hands still).
5. 2026-09-27 (L39): a second Standard take failed too → back to Turbo, eyeline in frame terms, next clip chained.
6. 2026-09-27: a mirrored start frame (`Shots/_tests/mirror/`) so Turbo's leftward habit would land right — dropped.
7. **2026-09-27 (L40), current:** Turbo heads the right way but overshoots; nothing chains from the turn; a 3 s guest
   reaction is cut in as the turn lands; the host returns on the built seed. `P1_003a` itself was finally cut from
   `P1_126` after four failed takes (L43, L44).

## R5. Chains and joins — measurements

- **Luma loss per link** (Higgsfield, Kling 3.0): 79.62 → 78.81 → 77.50 → 75.76 (~1.5 % per link) — the origin of the
  three-link cap and of the (never used) pre-lift plan.
- **Colour range:** a correctly extracted frame read 14.66 saturation against the source's 14.72; a range-converted one
  15.82, and the clip generated from it started at 15.84 — the generator reproduces its start image faithfully.
- **2026-09-20:** `P1_004` → `P1_006` measured −0.4 % luma but **+7.1 % chroma**; the rule then said never use the
  platform's extract button.
- **2026-09-21, corrected:** every clip starts 3.3–4.0 % darker than its input (host −4.0 %, guest −3.3 %, `P1_056` →
  `P1_057` −3.3 % with chroma −0.3 %). The −0.4 % was a confound (that frame came in brighter). **Decided: level joins in
  the edit (`JOIN_GRADES.md`), not predict them;** Kling's own last-frame feature became the default (its only fault, a
  uniform colour shift, is removed by the grade).
- **2026-09-20 → 2026-09-26:** chains were made in two passes (seed rows, then extract every chain frame, then the chained
  rows); since 2026-09-26 one sheet lists each chained clip under its source.
- **2026-09-24 end-frame rule (`P1_086`):** start = end = seed on a listening reaction held the eyeline (face diff 4.1 vs
  9.4 free), halved the small movement, and cut chained rows 40 → 29.

## R6. Wides and two-shots — why none are generated

- The generated two-shot put both figures a size too large against the chairs (from the seed frame; rerolling never
  fixed it). The 4 s establishing wide was cut 2026-09-18 (32 cr a part). `WIDE_SILENT` (Standard, audio off) and
  `WIDE_CREDITS` (Turbo, audio discarded, under a credit roll) were retired with it; the credit roll itself was dropped.
- Three `frame_wide_<guest>` variants per guest, the mark baked into `frame_wide_<guest>_marked.png`, and an
  empty-studio fixed outro (one 120-cr generation) were all proposed or built; the empty studio was rejected because it
  says nothing about the two people.
- **2026-09-28 (L59):** the per-guest marked wide also had the host in a different pose from his last line. The outro
  wide is now built per part from three references.
- **Structural:** speech-to-speech converts a clip to one voice, so a two-speaker clip can never carry heard dialogue.

## R7. The Kling CLI — facts worth keeping (2026-09-25 → 27)

`@klingai/cli-global` 0.2.0; login per session (OAuth). `kling-video-v3_0_turbo`: prompt, duration 3–15, 720p/1080p —
**no audio toggle, no tail image**. `kling-video-v3_0` ("Standard"): 720p/1080p/4k, `enable_audio`, `prefer_multi_shots`,
`tail_image`, elements — **dangerous defaults 4k, multi-shot on, audio off**. No camera parameter. Downloads carry a
KlingAI watermark unless `urlWithoutWatermark` is used (L20). File host `s15-kling.klingai.com` was blocked from the
cloud session (only `kling.ai` / `klingai.com` allowed). Credits match the website (70 cr for 3 s Turbo + 5 s Standard
reaction). Rate limit: 2 in parallel, upload once, retry (L26). Set aside 2026-09-26 (L32) for lack of a camera lock;
back 2026-09-27 once v3 needed none (L51, L52).

## R8. Smaller settled items

- **Prompt enhancer:** ON under Kling 3.0 (it once had a guest point at herself on *"me"*); absent on Turbo; `P1_054` came
  back natural without it, so gesture paragraphs were not rewritten.
- **Unverified claim** that lip-sync decouples after ~5 s: folded into T3 (2026-09-22 → 24); no drift seen in the long
  beat-map takes; the control was dropped.
- **The `says` attribution** (`The woman says, cool courtesy: "…"`) — lost to the label form in T8.
- **T-test details:** T1 (`P1_013`, *"Medes"* read twice from a `Pronunciation:` paragraph; *"Meeds"* right); T3 (`P1_087`
  → `P1_088`: 193 Hz both sides, luma −0.4 %, face diff 2.5, B 6–7 dB louder); T5 (`P1_044` → `P1_045` → `P1_046`: mouth
  closed in ~0.4 s; reply opened with 3.2 s of silence); T6a (`P1_008` + `P1_009`, crops host x=150 / guest x=800); T6b
  (`P1_085` + `P1_086` shared silence — empty).
- **Thumbnail baseline (Cleopatra P1):** seed frames 2720×1536; a tight 16:9 crop lands ~1342×755; uncropped her head is
  22 % of frame height (~45 px at desktop feed size, ~26 px mobile); cropped ~91 px. The crop is at the resolution floor,
  the mic occupies the negative space, the expression is neutral by design — which is why the thumbnail portrait is a
  separate generation (`THUMBNAIL_SYSTEM.md`).
- **Forward-leaning guest pose:** attempted twice by prompt; both came back tighter with table and mic enlarged (26.5 and
  23.4 against a set under 13.4).

## R9. Series furniture — superseded specs

- **The hook slot** was first 6.17 s (one loop of the theme plus its run-in) on black, with the card in front of the
  opening; the card moved inside the file and the slot became 4.00–8.00 s (2026-09-22). The 2026-09-21 example line was
  *"Egypt did not survive without me."* (`P1_057` 5.6–9.6 s, 1.5 s live hold).
- **`BRAND_bumper_in`** began as a 5 s piece (sand falls 0.35–2.0 s, stops, reverses 2.35–3.1 s, lockup to 5.0 s; music
  cut so the reversal landed at 2.35 s); it is now the intro inside `BRAND_opening`, reversal at 16.52 s.
- **`BRAND_disclosure`** was specced as a 3 s black card with a sting; it is the first 4 s of `BRAND_opening`, on paper.
- **Act breaks, as built:** generated at 4 s (Standard audio off, 32 cr each), last frame held to 5.000 s, paper
  restored; the worn step was dropped after repeated failures. An earlier build cut out at 4.000 and let the next chime
  land on the interview — wrong, the break must own both chimes.
- **The outro test** (passed) ran on `frame_wide_cleopatra_marked.png`: charcoal still on Kling Image 3.0, then a 5 s
  Standard transformation under lock v1. Judging order: do the figures hold (the pass/fail); does the change move inward
  from the edges; does it land and stop; is the last frame a usable still. Fallbacks: an editor cross-dissolve if the
  figures drift; one retry for a uniform flip; regenerate the still for an overshoot.
- **Room tone** was first to be extracted from clips, then built from six takes crossfaded
  (`acrossfade=d=3:c1=tri:c2=tri`); it is one seamless take (take 04, 1:48).
- **Music:** six cues were specced; `MUSIC_Sting_Transition` (4 s) and `MUSIC_Bed_Disclaimer` (8 s) were cancelled;
  `MUSIC_Outro_Bed` went 90 → 60 → 35 s. Spend ~4,300 credits against ~9,800 for the original spec. The prompts are in
  `Fixed_Assets/Audio/AUDIO_PROMPTS.md`.
