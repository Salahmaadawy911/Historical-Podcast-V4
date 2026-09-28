# SKILL: MODE 2 (CAST GUEST)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.


> 📂 **Inputs and output — added 2026-09-19 so each mode can run in its own chat.**
> **Reads:** `Episodes/<Guest>/PITCH.md` (Likeness Tier and arc).
> **Writes:** `Episodes/<Guest>/CAST.md`, the character sheet, the five seed frames and the wide seed frames including `frame_wide_<guest>_marked.png` — **all start frames in `Start_Frames/<Guest>/`** (the Host's are in `Start_Frames/Host/`, 2026-09-26), the thumbnail portrait, and the voice ID in `Fixed_Assets/VOICES.md`.
> **Save the output to that file before the mode ends.** Anything that lives only in chat history
> is lost to the next mode.


## Guest Visual Protocol (branches on the Likeness Tier field from Mode 1)

If Likeness Tier = Fully Anonymous Composite:
Proceed with AI Cast Generation below.

If Likeness Tier = Real Identified Figure (Standard):
Attempt AI Cast Generation below first. If the platform blocks the generation, switch to the Archival Asset Brief for this guest rather than retrying with reworded prompts.

If Likeness Tier = Real Identified Figure (Iconic — Reconstructable):
Attempt AI Cast Generation below, built entirely from historically-grounded evidence (coin portraiture, contemporary written description, archaeological findings) rather than the recognizable modern/cinematic image associated with the figure's name. If this reconstruction is still blocked, fall back to an Eyewitness Substitution guest — do not use a real photo/portrait insert (Archival Asset Brief) for this tier.

If Likeness Tier = Real Identified Figure (Iconic):
This tier should never reach Mode 2 directly as the on-screen guest — Mode 1 substitutes an Eyewitness Substitution character instead, tagged as Fully Anonymous Composite or Real Identified Figure (Standard). If an Iconic-tier figure is passed to Mode 2 as the guest, treat it as a routing error: return to Mode 1 and generate an Eyewitness Substitution before casting.

## Archival Asset Brief (fallback for a blocked Real Identified Figure — Standard only)
Output these fields instead of an image-generation prompt:
- Sourcing Categories: 2-3 types of public-domain or clearly licensable sources to check for real reference images (e.g., national archives, government/military photo collections, library or museum public-domain holdings). Name institution types, not unverified specific URLs.
- Required Reference Shots: a clear frontal reference, a profile or three-quarter reference if available, and a full-body/wardrobe reference if available.
- Face Policy: the sourced real image is this guest's entire visual identity on camera, shown as a still with camera movement (pan/zoom/parallax) — never facially animated, lip-synced, or face-swapped to simulate speech. No exceptions.
- Permitted AI Assets: AI generation may still produce anything that excludes this guest's face and body — environment B-roll, document/artifact inserts, maps, or generic period atmosphere — under the IP Filter Safety and Color & Lighting Lock rules below.
- Audio: guest dialogue is AI-generated voice only, paired with the sourced archival image.
- Studio Asset Tag: register this guest as `@Archival_[Name]` (not `@Guest_[Name]`) for use in later modes.

## The output of this mode: `Episodes/<Guest>/CAST.md` — restored 2026-09-18

**Reconstructed from the Cleopatra `CAST.md` that this mode actually produced**, plus
`Fixed_Assets/POSE_LIBRARY.md` and `STUDIO_ASSETS.md`, after the original text was lost. Those
files point back here — `STUDIO_ASSETS.md` states that guest pose registers "live in
`Episodes/[Guest Name]/CAST.md`, written by Mode 2 at casting", and `POSE_LIBRARY.md` cites this
file for the seed-frame prompt structure — so both halves are recoverable from their outputs.

**Mode 2 is not finished until `CAST.md` exists.** Mode 4 reads it before assigning any shot.

| section | what it carries |
|---|---|
| **Likeness Tier** | the tier from Mode 1, and one line on how it was cast |
| **Character sheet** | the file and its entity tag, plus the cross-shot and wide plates |
| **Voice** | the `Voice:` block, **pasted byte-identical into every clip, across both parts** |
| **Wardrobe** | itemised — hair, headwear, jewellery, garments, drape — **repeated identically in every seed-frame prompt** |
| **Register** | how the character behaves: what they do instead of defending themselves, and how wide their posture range is |
| **Performance profile** | 🔴 **the single source for everything guest-specific that Modes 3, 4 and 6 need** — see below |
| **Pose Register — cross-shots** | every variant, with what each is *for* |
| **Wide variants** | the same, on the wide plate |
| **Acceptance record** | the measurements, not an opinion |

### The performance profile — added 2026-09-22

The modes are written for **any** guest. Everything that differs between a queen defending her
decisions, a conscript giving testimony and an old scientist settling scores lives here, and Modes 3,
4 and 6 read it instead of assuming. Write it at casting, from the Mode 1 pitch and the record; it is a
casting decision, not a script decision.

| field | what it decides | Cleopatra |
|---|---|---|
| **Prompt label** | the attribution in every Kling prompt — *"<label> says, …: "…""* — and the subject of every gesture line. Fixed for the whole arc; Kling's guide wants a consistent label | `The woman` |
| **Pronouns** | used in every gesture, reaction and interruption line | she / her |
| **Default register** | the delivery every speaking prompt starts from; per-shot direction states only deviations (Mode 4 §4) | composed, unapologetic, never pleading — corrects premises rather than defending |
| **Emotional ceiling** | the furthest the character goes, written as manner + limit (Mode 4 §4) | anger held well under the surface; never raised, never breaks |
| **Interruption style** | which `CUT-IN` kinds fit (Mode 3 toolkit) — who yields, who holds, who cuts in | holds her ground (`hold`); cuts *in* on a leading question (`cut`); never `yield` to a Roman framing |
| **Gesture range** | the few movements that belong to this person, and the ones that never do | small and contained: a hand opening and settling, chin a fraction higher, a slight turn toward him. Never a lean, never a raised hand |
| **Contractions** | whether the character speaks with contractions — a register choice, not a style whim | formal: none |
| **Composite?** | `yes` switches Mode 4 to the **testimony register** and turns on `BRAND_composite` | no — named figure |
| **Hook framing** | where the head sits in the guest's cross-shots — centre x, centre y and crown-to-chin height in pixels of the 1920×1080 frame — for `hook_build.py --face` (measure once on a seed frame) | 1365, 180, 240 |
| **Duration calibration** | the measured speech rate for this voice once the first clips are back (Mode 4 §2); blank until measured | 4.3 syl/s (measured on six clips, 2026-09-21) |

⚠️ **The `Voice:` block in `CAST.md` carries no pace language** — duration is the pace control, and
two mechanisms fighting over the same thing is how timing drifts. Pace belongs to the ElevenLabs
voice description; see `Fixed_Assets/VOICES.md`.

### Two assets the kit assumes exist — produce them here, 2026-09-18

**Found by auditing the Part 1 kit for assets no mode produces.** Both exist for Cleopatra only
because they were made by hand during testing. **A later episode has no testing phase**, so without
this section the kit would name files that nobody ever generates.

**1. The thumbnail portrait — once per guest.**
`Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md` already says the portrait is generated at "Mode 2
casting, from the character sheet", and **Step 2 of that file holds the exact prompt** — lit for
paper, head in the right third, the left half of frame empty, no studio furniture. Generate it
here, with the character sheet attached as the **only reference image** (never a seed frame or plate), as `Episodes/<Guest>/thumb_portrait_<guest>.png`, and register the filename in `CAST.md` **together with the exact prompt used**. The wardrobe words at the end of the Step 2 prompt belong to one guest: swap in this guest's garment and headwear from the *Wardrobe* section (added 2026-09-23).

⚠️ It is **reused for the guest's second part** — only the kicker and the statement change — so it
is a per-guest asset, not a per-part one. Generating it again for Part 2 is waste and invites drift.

**2. ~~The marked wide seed frame~~ — no longer made in Mode 2 (2026-09-28, L59).** The outro wide is now built **per part in
Mode 4** from three references (`cam3_wide.png` + the host's and the guest's last-clip pose frames), so the figures are true to
scale and each person matches their final clip. Mode 2 makes **no** `frame_wide_*` frames for a new guest. What Mode 2 must
still provide for it: the pose frames themselves (they are the references). The old text is kept below for the record.

~~**The marked wide seed frame — `frame_wide_[name]_marked.png`.**~~
The wide seed frame with `BRAND_mark` composited onto the studio panel at the fixed coordinates in
`STUDIO_ASSETS.md`. **`BRAND_bumper_out` starts from it at production time**, so it has to exist
before Mode 4 runs, and the mark must be in the frame *before* the charcoal pass so it is drawn
rather than stamped on. Register it in `CAST.md` with the pose variants.

🔴 **The general rule this came from: an artifact the kit names must be produced by a named mode.**
"It already exists" is only true for the episode that happened to make it during testing. When
adding anything to a kit, name the mode that produces it — or produce it here.

### The pose register

**Order the variants from most withdrawn to most engaged**, and give each one a use note naming the
beat it is for — *"where she declines a premise"*, *"for statements of authority"*. A filename tells
the production nothing; the use note is the whole value of the register.

🔴 **Write the pose table with the register. Added 2026-09-24.** Registering the poses in `CAST.md` is
not enough — Mode 4 writes prompts from `Episodes/<Guest>/poses.py` (`GUEST = {…}`, same fields as the
Host's `Fixed_Assets/tools/poses.py`; Cleopatra's is the worked example). For each frame: `desc`;
`hold` — the posture held, no gaze, used in every silent reaction from it; `entry` — **required when a
hand is at the face or chin**: the hand comes down as the line begins and stays down; `settle`,
`advance`, `still` — **one-way moves into a position that then holds**, never a move that goes and
comes back (*nod, open-and-close, lift-and-settle-back* — Kling loops them). Mode 4's build stops on a
frame with no entry. 🔴 **Make every variant by EDITING the reference frame, not from scratch (2026-09-26, measured).** Seedream
image-to-image with the set's reference as the only input — *"Keep this photograph exactly as it is — same room,
framing, lens, lighting, grade, grain and the same person … Change only <the arms / the head and eyes>. Nothing
else changes."* Twins built this way matched the room far better than prompt-built ones (`frame_host_direct_c` from
`frame_host_e`: room 2.8, shift 0, against 6.1 and a 5 px shift before; `frame_cleopatra_c` from `frame_cleopatra`:
room 2.7, shift 0, against 5.2 and 5 px + 0.4 % zoom). A replaced frame goes to `Start_Frames/_replaced_<date>/`.
🔴 **Frame-set check before approval (2026-09-26, Salah):** `python3 Fixed_Assets/tools/frame_set_check.py Start_Frames/<Guest>`
compares every new frame with the set's reference, the person excluded — the room must match: shift ≤ 2 px, zoom ≤ 3 px,
brightness ≤ 2 %, colour ≤ 3. A frame that fails is regenerated before it enters a kit (the saved report is
`Start_Frames/FRAME_CHECK.md`). Any frame used as an END frame is checked against its START twin the same way.
**Write each entry by looking at the finished image**, never from the placement
prompt — the model does not always obey it (two host frames differ from their prompts; found 2026-09-24).
List in `avoid` the body contacts the pose does not have (*armrest* for hands-in-lap), so a hand-written
gesture that fights the start frame fails `pose_check.py`. A regenerated frame keeps its entry unless the pose itself changed.
- 🔴 **No interlaced fingers in any guest pose (2026-09-27, Salah, L46).** Crossed or interlocked fingers from both hands read as glitched in motion. Write hands as *resting one over the other*, *side by side on the lap*, *one hand on the armrest*, *one hand open in the lap* — never *clasped*, *interlaced*, *fingers laced/crossed*, *steepled*, and put "fingers not interlaced" in the edit prompt. Applies to new guests and new pose frames only; Cleopatra's and the host's existing frames stay as they are (regenerating them would orphan kept clips).
- 🔴 **Pose moves name the side of the frame, never *toward him/her* (2026-09-28, L58)** — *him* with one person in frame reads as the viewer, and she turned to the lens.
- 🔴 **Rebuild the whole set, not just the flagged frames (2026-09-28, L56).** When a set moves to the edit method, every older prompt-built frame is rebuilt from the reference too, then all frames are looked at side by side — `frame_cleopatra_d` passed the checks and was still visibly off in chair and scale.
- 🔴 **Furniture landmarks (2026-09-27, L41).** Before the check, write `Start_Frames/<Guest>/landmarks.json` (and one for `Host/`): three or more windows at 1920×1080, each holding one horizontal edge of the chair (back top beside the shoulder, each armrest top), picked on the reference frame. The room grid alone cannot see the chair — it sits next to the person and is discarded with her. A FURNITURE flag means the variant is rebuilt by editing the reference, not accepted.

🔴 **A bigger pose library — 9 or so per guest, not 5 (2026-09-27, Salah, L47).** Editing the reference made frames cheap
and consistent, so a guest now gets roughly **9 poses** (Part 2 adds to Part 1's set; a new guest starts with ~9). More
poses means fewer repeats of the same picture across a part, which reads as a real conversation. **Range still follows
character:** the extra poses are *more variations inside her range* (where the hands are, how far back she sits), not
wider swings. Every pose in `poses.py` carries three library fields besides the prompt fields:
- `rank` — 1 (most withdrawn) … N (most engaged), the register order;
- `use` — the beats it is for, in words Mode 4 can match to a row's delivery note (*declines a premise*, *explains a distinction*, *grief held in*, *statement of authority*, *listening*);
- `only` — `'react'` for a pose kept to silent reactions (a hand near the face; L-entry rule), else omitted.
Mode 4 picks each row's pose by `use`, never repeats one pose on two consecutive shots of the same person unless chained,
and moves at most ~2 `rank` steps across a cut unless the line turns hard. The library is the table in `poses.py`, summarised
in `CAST.md`'s pose register; every new pose passes the frame-set check (room + FURNITURE) before it enters a kit.

**Range follows character.** Cleopatra's is deliberately narrower than the Host's: a composed figure
who swings between postures stops reading as composed.

⚠️ **Do not write a forward-leaning variant.** Attempted twice and abandoned: **the model reads
"leaning forward" as "move the camera closer."** Both attempts returned tighter shots with the table
and microphone enlarged, measuring 26.5 and 23.4 against a set otherwise under 13.4 — either would
jump on a cut. `KEEP IDENTICAL`'s "do not reframe or zoom" does not survive a lean instruction. Carry
"more engaged" through an open hand instead, which is cheaper and usually truer to the character.

### The seed-frame prompt — two inputs, one paragraph changes

`POSE_LIBRARY.md` holds the working template in full; it is the Host's copy of this structure and
the guest's is identical in shape. The rule is:

- **the character sheet supplies identity and wardrobe; the camera plate supplies the room and the
  camera.** Two inputs, always.
- **`KEEP IDENTICAL` blocks for both** — every material, colour and fixture from the plate, and face,
  hair and garments from the sheet. Including *"do not reframe, zoom, or change focal length"* and
  *"no second chair appears"*.
- **Only the `PLACEMENT` paragraph differs between variants.** Everything else is byte-identical.
- **The output is a photograph of the person in the room, not a panel sheet**, and none of the
  sheet's grey backdrop appears anywhere.

### Acceptance — by measurement, never by eye

**Compare room-only regions against the reference plate and record the numbers in `CAST.md`.**
Cleopatra's set, as the worked example: cross-shots **5.3–13.4 mean absolute difference**, inside
the tolerance the accepted Host set occupies (**8.6–15.9**); wides a and b **6–11**; wide c ran
**19–20 at the frame edges** — top of tolerance but geometrically sound, confirmed because the sign
panel sat at **y 393–395, height 161** in all three wides and in the plate, proving no camera move.
Panel blank in all three (**mean 216–220, dark pixels ~0.1%**).

**A variant failing the check is regenerated, not kept**, and the rejected files are deleted rather
than left to be picked up later by mistake.

## ⚠️ Period Accuracy Gate — restored 2026-09-18

**Run this before writing any casting prompt, for the guest and for every extra.**

> Establish the **date** of the scenes the figure appears in, and verify costume, armour and
> equipment against **that date**, not against the general image of the culture. State the evidence
> in one line beside the prompt. Where a period detail is contested, say so and pick the
> conservative option.

**"Roman soldier", "medieval knight", "samurai" and the like span centuries of very different kit,
and the generic image is almost always wrong for a specific year.**

**Also name what is not there.** Models default to the famous look, so the prompt must exclude it
explicitly — *"no plate or banded armour", "no metal shin guards"* — or the default wins.

**Found the expensive way.** `roman_legionary.png` was generated showing **lorica segmentata**, the
banded iron plate — Imperial kit from the early first century **AD**. Cleopatra died in 30 BC; at
Actium the legions wore **lorica hamata**, chain mail, with Montefortino-type bronze helmets. The
sheet was roughly fifty years early, and four b-roll rows inherited the error.

**The real failure was structural, not factual:** research rigour was applied to the dialogue —
sources named, the library myth corrected, the carpet story corrected — and not at all to the
visual assets. Mode 1 checks Likeness Tier and Recognition Tier; Mode 3 checks IP safety; nothing
asked whether the costume was right for the date. On a research-led show that is the worst place to
be loose, because **the audience that rewards the positioning is exactly the audience that notices
armour.**

## Voice Design at cast time — restored 2026-09-18

**Every guest gets one designed voice, created once at cast time**, and reused for every clip
across both parts. Designing per clip is how a character stops sounding like one person.

🔴 **Hard rule: the designed voice is a speech-to-speech TARGET, never a text-to-speech source.**
Generating a guest line as TTS discards the Kling performance and the lip sync with it. Design →
save → run the Kling clip through the voice pass against the saved voice.

**Prompt template:**

```
Native <Language + regional variant>. <Gender>, <Age range>. Perfect audio quality.
Persona: <2-5 words>. Emotion: <2-3 adjectives>.
<1-2 sentences: timbre, pacing, delivery.>
```

**Writing rules:**

- **Language and variant lead the first sentence.** Naming them late makes the voice drift
  mid-generation.
- **Never use the word "accent"** — it drags the model toward a regional dialect. Place the English
  descriptively instead: *"placeless formal English, neither British nor American."*
- **No production terms** — reverb, echo, phone, room, mic. The model does not apply effects; it
  degrades the voice trying.
- **Preview text is a real line from the Mode 3 outline**, not the default sentence, and it is a
  *performance script* rather than a restatement of the description.
- **Do not ask for archaic or "period" delivery.** The guest speaks modern English in a modern
  interview; the period lives in the picture and the content, not the vowels.

**The accent decision is editorial and must be defended in one line on the cast sheet.** Two
failure modes to name and reject explicitly: the **modern-nationality default** (Cleopatra was
Ptolemaic Greek — a modern Egyptian voice is simply wrong) and the **documentary cliché** (clipped
Received Pronunciation for anyone ancient). Placeless formal English is the safe answer and needs
no apology; anything else needs a reason written down.

⚠️ **But the accent is delivered by the KLING prompt, not by this voice.** Corrected 2026-09-18:
accent is carried by phonetics, and speech-to-speech takes phonetics from the **source read**. The
designed voice contributes timbre. Write the accent decision into the character's `Voice:` block in
the kit, byte-identical in every row, and keep this description consistent with it.

**How to write a chosen accent or voice trait in the Kling block — clarified 2026-09-20.** The
*"never use the word accent"* rule above is for the **ElevenLabs design description**, and for a
placeless decision. When the editorial decision *is* an accent, the Kling `Voice:` block names it
plainly, the way Kling's own guide does (*"with an Indian accent"*, *"in Cantonese"* —
`KLING_MIGRATION.md` §3): e.g. *"…Clear English with a light Greek accent, present but never
heavy."* Put it in the `Voice:` block, never in the register paragraph, and keep it byte-identical
in every clip of that character. **The split, one line:** Kling decides everything about the
*performance* — accent, dialect, tone, emotion, rhythm, timing — and ElevenLabs keeps all of it
while replacing only the *timbre* (`skill_elevenlabs.md`: *"What it keeps from the source: tone,
emotion, cadence, timing, and the accent and language of the performance."*). So any trait the
voice change cannot add on its own must be written into the Kling prompt, and the Kling block's
timbre words (age, pitch, gravel) still matter only so the source read is close enough to convert
cleanly.

📖 **Settings, credit costs and the exact parameter values live in `skill_elevenlabs.md` and
`Fixed_Assets/VOICES.md`, and those are the authority.** Do not copy values into this file — the
last copy went stale and contradicted them. At cast time: record the **voice ID** in `VOICES.md`
immediately, and note that the web UI does not expose a **seed**, so the saved voice *is* the asset
and must never be deleted. **Generate the reference render at cast time as well**, as
`Episodes/<Guest>/VOICE_<guest>_reference.mp3`: the preview paragraph spoken once in the saved voice, and the
only way to A/B a redesign if the voice is ever lost. Register it in `CAST.md` (added 2026-09-23;
for Cleopatra it was made late, not at casting).

## Recurring b-roll figures — the reference-sheet procedure

**Written 2026-09-18, and Part 1 needs none of it.** Recorded because the first episode that does
need it must not improvise.

**The problem it solves is identity, not style.** The charcoal style handles a person — tested, and
it holds. What it does not do by itself is make that person *the same person* in two different
b-roll shots. Generated independently from text, a named figure is a different man every time, which
is exactly the drift the seed-frame system exists to prevent for the studio characters.

### The default is still: no named faces in b-roll

**Check this before building anything.** Every b-roll row in Part 1 shows grain, ranks of anonymous
legionaries, a carved wall, a river, a worn coin — **evidence, not cast**, the same principle the
intro sketches are built on. That is a strength, not a gap:

- A named face asserts what a real person looked like. The show's whole position is that it is a
  reconstruction, and the guest's face carries a disclosure card; a b-roll figure carries nothing.
- Anonymous figures cost no continuity work, ever, in any episode.
- The rows read as documentary illustration rather than as dramatisation.

**So a named figure in b-roll is an exception that needs a reason**, not a default. Ask first
whether the shot works with an anonymous figure, an object, or a place. It usually does.

🔴 **Never apply this procedure to an anonymous figure — it has already failed that way.**
`@antony` and `@roman_legionary` were retired as character sheets on two findings, and the second
is the one that bites here: **passing a reference image for anonymous crowds produced roughly
twenty clone faces.** Extras get a **registered wardrobe text block** from `STUDIO_ASSETS.md`,
pasted byte-identical, **with no reference image at all**. A reference makes a crowd worse, not
better. The split is Mode 3's: anonymous → wardrobe block; named and identifiable → this procedure,
*plus* the full Likeness Tier check, because a named real person is a Mode 2 casting decision.

💡 **The first of those two findings was "a photoreal sheet cannot drive charcoal" — and this
procedure is the answer to it, not a reversal.** The old approach handed a photoreal reference
straight to a charcoal generation. Converting the face to charcoal *first* is precisely the missing
step. Nothing here reopens a settled decision; it closes the gap the decision identified.

⚠️ **Antony in Part 1 is drawn from behind, face not visible**, so the shot carries no likeness
claim and needs no reference. The retired sheet files are no longer in the project — if a future
episode needs him face-on, step 1 is a fresh realistic generation, not a conversion of something on
disk.

### When a named figure genuinely is needed

The pipeline mirrors the studio one exactly — character sheet → seed frame → clip — because that is
the structure already proven to hold identity across many generations.

1. **Generate a realistic face first, then convert it to charcoal.** Not charcoal directly.
   Identity lives in precise facial geometry, and a photoreal render is where the model is most
   controllable; charcoal is *deliberately* imprecise about edges, so defining a face in it means
   defining it in the medium worst suited to holding it. The photo→charcoal conversion preserving
   identity is already proven — it is what `BRAND_bumper_out` does.
2. **One converted face is enough. Do not build a multi-view character sheet.** The studio
   characters need one because photoreal likeness is unforgiving and the eye checks a face against
   a photograph. **Nobody does that to a drawing.** ~3 credits, once.

   💡 **This is a second benefit of the charcoal decision that was never planned for.** The style
   was chosen so a reconstruction could not be mistaken for footage. It also makes character
   continuity cheap, because the medium discards exactly the fine detail that would reveal drift.
   A requirement imported from the photoreal pipeline is over-engineering here.
3. **Register two things in `CAST.md`, not one:**
   - the reference file, `Episodes/<Guest>/broll_<name>_charcoal.png`
   - **a short byte-identical description of the figure's *massing*** — hair shape, beard, brow
     weight, jaw, neck, build. Something like *"heavy brow, short curled hair, thick neck, broad
     through the shoulders."*

   ⚠️ **In a drawing, "the same man" is carried by massing, not by facial metrics.** That phrase is
   what a viewer actually reads as continuity, so it is pasted into every b-roll prompt for that
   figure, byte-identical, never re-improvised per shot — the same discipline the registered voice
   descriptions use. Reference and words then reinforce each other, and on a generation where the
   reference transfers weakly the text still holds the silhouette.
4. **Every b-roll row for that figure uses the reference to build its start frame**, then the start
   frame drives the clip — the same two-step every character b-roll already uses.

⚠️ **Step 4 is the unproven link and should be tested before an episode depends on it.** Everything
above it is proven: the style carries a person, photo→charcoal holds identity, and a start frame
drives a clip. What has *not* been measured is whether a charcoal reference carries the face into a
**new scene** at a different angle and distance. Test with two shots of the same figure in different
settings and judge them **side by side** — not by looking at either alone, which is where a drifting
likeness always passes.

**Who gets a reference:** any figure appearing in **more than one** b-roll row. A one-off figure does
not need one, and anonymous figures never do.

## AI Cast Generation
Generate a hyper-detailed casting prompt for a 3-view character sheet.

IMPORTANT: Output the final prompt as a SINGLE raw block of text enclosed in a code block. Do NOT use Markdown headings, bolding, or bullet points inside the code block. Do NOT add conversational padding.

Incorporate the following details into the raw text prompt:
- Background & Layout: Neutral mid-gray background with thin dark dividers between the panels, 16:9 aspect ratio.
- Panel 1 (Left - Full Body Front): Ankle to shoulders. The head must be completely missing/erased above the neck without zooming in or altering body scale.
- Panel 2 (Center - Full Body Three-Quarter Rear Angle): Framed at the same scale as Panel 1. The body and shoulders must be visibly turned so one shoulder angles toward the camera and the other rotates away, with the far side of the torso partially visible in profile — never a flat, symmetric direct rear view.
- Panel 3 (Right - Close-Up Portrait): Strict frontal headshot with the only visible face. Any headwear or accessory (diadem, headband, etc.) must be called out as its own distinct, prominent detail rather than buried at the end of a long list, so it doesn't get dropped.
- Cross-Panel Consistency: Any draped, wrapped, or otherwise non-fixed garment element (a shawl, cloak, wrap, etc.) must be described identically in every panel it appears in — same style, same drape, same position — so the look cannot drift between panels within one generation.
- Color & Lighting Lock: Mandatory text must be included: "Cinematic color photography, 35mm color film quality, soft near-shadowless lighting, 5600K, readable colored skin texture, visible catchlight in the eyes. DO NOT GENERATE IN BLACK AND WHITE."
- IP Filter Safety: Do NOT use specific historical location names or event names in the prompt (e.g., instead of "Los Alamos 1945", use "1940s arid desert facility"). Describe the aesthetic, not the historical label, to avoid triggering copyright filters.
- Reconstructable-Tier Grounding: If this guest is tagged Real Identified Figure (Iconic — Reconstructable), build every physical and wardrobe detail from documented historical or archaeological evidence (coin portraiture, contemporary written description, material culture) and explicitly diverge from the figure's recognizable modern pop-culture depiction.
- Studio Asset Tag: register the resulting character as `@Guest_[Name]`.
