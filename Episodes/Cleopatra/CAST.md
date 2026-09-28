# CAST — Cleopatra VII

Written at Mode 2 casting. Mode 4 reads this before assigning any shot.

**Likeness Tier:** Real Identified Figure (Iconic — Reconstructable). Cast directly from
historically-grounded reconstruction, not the cinematic image.
**Character sheet:** `guest_cleopatra.png` → entity `@guest_cleopatra`
**Cross-shot plate:** `@cam2_guest` · **Wide plate:** `@cam3_wide`

## Voice — `@voice_cleopatra`
Pasted byte-identical into every clip of hers, across both parts. Never reworded.

> Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.

Carries no pace language by design — duration is the pace control.

**Accent: placeless, and it is delivered by this Kling block**, not by the ElevenLabs voice (`xMytukqVLj8LlL1L1sOo`), which supplies timbre only. Corrected 2026-09-20 — this line still carried the retired *Mediterranean colouring* after the kit had been fixed on 2026-09-18.

**Accent decision, defended (added at the 2026-09-23 audit):** placeless formal English. She was a Macedonian Greek Ptolemy, so a modern Egyptian voice is the modern-nationality default and is wrong; clipped Received Pronunciation is the documentary cliché for anyone ancient. Neither is historical, so the voice claims no nationality at all.

## Wardrobe
Dark hair drawn back in a low bun beneath a thin flat gold diadem, pearl drop earrings,
fine gold chain, cream undyed linen chiton with the himation draped across the left
shoulder. Itemised identically in every seed frame prompt.

**Period evidence (added at the 2026-09-23 audit):** her own coinage shows a royal diadem and the Greek melon coiffure gathered into a bun, draped Greek dress, the Ptolemaic nose. So the look is Greek court dress with a flat diadem, deliberately not the 1963 film look: no vulture crown, no nemes, no heavy kohl, no Egyptian wig.

## Register
Composed and unapologetic. She corrects premises rather than defending herself, and never
pleads. Her posture range is deliberately narrower than the Host's — a composed figure who
swings between postures stops reading as composed.

## Performance profile
*Added 2026-09-22 (Mode 2 spec). The single source for everything guest-specific that Modes 3, 4 and 6 read.*

| field | value |
|---|---|
| **Prompt label** | `The woman` |
| **Pronouns** | she / her |
| **Default register** | composed, unapologetic, never pleading — corrects premises rather than defending herself |
| **Emotional ceiling** | anger held well under the surface; never raised, never breaks |
| **Interruption style** | holds her ground (`hold`); cuts *in* on a leading question (`cut`); never `yield` to a Roman framing |
| **Gesture range** | small and contained: a hand opening and settling, chin a fraction higher, a slight turn toward him. Never a lean, never a raised hand |
| **Contractions** | formal: none |
| **Composite?** | no — named figure |
| **Hook framing** | 1365, 180, 240 (head centre x, y, crown-to-chin, in the 1920×1080 cross-shot) |
| **Duration calibration** | 4.3 syl/s (measured on six clips, 2026-09-21) |

## Pose Register — cross-shots
Five variants on `@cam2_guest`, eyeline off-frame left. Ordered from most withdrawn to most
engaged.

- **`frame_cleopatra_e`** — settled back into the chair, hands loosely clasped in her lap, chin a fraction higher. Reserved, withholding. Use where she declines a premise, gives a short answer, or lets a question sit.
- **`frame_cleopatra`** — upright and composed, back against the chair, hands resting in her lap. The neutral default. Listening, and straightforward answers carrying no particular weight.
- **`frame_cleopatra_b`** — upright, hands folded to one side of her lap, torso turned a little further toward him. Attentive. Use where she is following a line of questioning closely.
- **`frame_cleopatra_d`** — both forearms along the armrests, hands relaxed over the ends, shoulders square. Open and at ease, the most formally composed of the set. Use for statements of authority — the answers she treats as self-evident.
- **`frame_cleopatra_c`** — one forearm along the armrest nearer the camera, the other hand open and slightly raised in her lap. Explaining, offering a distinction. Her most engaged pose. Use where she is laying out reasoning rather than asserting.

**Five, not six — a forward-leaning pose was attempted twice and abandoned.** The model reads
"leaning forward" as "move the camera closer": both attempts returned tighter shots with the
table and microphone enlarged, measuring 26.5 and 23.4 against a set otherwise under 13.4, and
either would jump on a cut. `KEEP IDENTICAL`'s "do not reframe or zoom" does not survive a lean
instruction. The rejected files have been deleted.

This costs nothing. Five clears the selection rule comfortably, and a pronounced lean was her
least characteristic posture anyway — `frame_cleopatra_c` already carries "more engaged" through
an open hand rather than a body shift, which suits her better.

## Wide variants
All on `@cam3_wide`, both characters, sign panel blank. At wide scale only silhouette reads.

- **`frame_wide_cleopatra`** — Host settled back, forearms on the armrests; her hands in her lap. Neutral establishing.
- **`frame_wide_cleopatra_b`** — Host leaning forward, elbows on thighs; her hands folded, torso angled toward him. Use where the act that follows turns adversarial.
- **`frame_wide_cleopatra_c`** — Host with one ankle crossed; one of her forearms on the armrest. The most relaxed of the three — openings and closings rather than mid-argument transitions.

**Marked wides (registered at the 2026-09-23 audit):** `frame_wide_cleopatra_marked.png`, `_b_marked.png` and `_c_marked.png` are the same three frames with `BRAND_mark` on the panel at the fixed coordinates (`STUDIO_ASSETS.md`). `frame_wide_cleopatra_marked.png` is the start frame for `BRAND_bumper_out`. Checked by eye on 2026-09-23: the mark sits on the lit panel and the figures are unchanged.

## Thumbnail portrait
**`thumb_portrait_cleopatra.png`** (2720×1536): the clean portrait, with no type or ground on it. Reused for both parts; per part only the kicker and statement change (`Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`). Registered 2026-09-23. `THUMB_cleopatra_p1.png` is the **finished v1 Part 1 thumbnail** and is kept for comparison only: its statement is v1 creative text and is not carried into the rerun.

**Inputs:** one reference image, the character sheet `guest_cleopatra.png`, plus the prompt below. *"The woman from the reference"* refers to the sheet. No seed frame and no plate were used. Prompt recorded verbatim (Salah, 2026-09-23). It was pasted as one line, so the sentences run together at `camera.Soft`, `shadow.Plain` and `it.Cream`. It predates the reordered template in `THUMBNAIL_SYSTEM.md` Step 2 and came back with her head near the centre, which does not matter because Step 4 cuts out the figure and places it on the right:

```
A tight three-quarter portrait of the woman from the reference. Head and shoulders filling the right side of the frame, her body angled inward, her gaze directed off the left edge of frame past the camera.Soft even daylight from the front and slightly above. Gentle modelling on the cheek and jaw and a soft shadow beneath the jaw to separate her from the background, but no deep shadow anywhere on the face and no dark side — the contrast comes from her dark hair, brows and eyes, not from shadow.Plain flat background in a warm pale grey, the tone of toned drawing paper, evenly lit corner to corner with no vignette and no shadow cast onto it.Cream linen drapery, thin gold diadem. No microphone, no chair, no table, no furniture of any kind. 16:9.
```

## Audit — 2026-09-23 (B5 rerun, Mode 2 audit only; nothing regenerated)
Checked against today's `skill_mode2_cast.md`, with every named file confirmed on disk.

| section | result |
|---|---|
| Likeness Tier | ✅ matches `PITCH.md` |
| Character sheet, plates | ✅ `guest_cleopatra.png`, `@cam2_guest`, `@cam3_wide` present; tag form `@guest_<name>` matches `STUDIO_ASSETS.md` |
| Voice block | ✅ no pace language; placeless. ➕ one-line accent defence added |
| ElevenLabs voice | ✅ `xMytukqVLj8LlL1L1sOo` recorded in `VOICES.md`. ✅ reference render `Episodes/Cleopatra/VOICE_cleopatra_reference.mp3` (12.1 s) added by Salah 2026-09-23 |
| Wardrobe | ✅ itemised, and matches the seed frames and the portrait. ➕ period-evidence line added |
| Register, performance profile | ✅ all ten fields present; duration calibration of 4.3 syl/s is measured, and still valid because the voice and prompt label are unchanged |
| Pose register | ✅ five files present, ordered and annotated; no lean pose |
| Wide variants | ✅ three present. ➕ the marked wides were missing from this file and are now registered |
| Thumbnail portrait | ✅ `thumb_portrait_cleopatra.png` added by Salah 2026-09-23, with the prompt it came from; checked by eye: clean, lit for paper, diadem and earrings match the wardrobe |
| Acceptance record | ✅ by measurement |
| Recurring b-roll figures | none registered, and none needed yet. **Note for Mode 3:** the pitch's images include Arsinoe in chains and Antony on the ropes. Keep named figures unrecognisable (from behind, or in the crowd), or, if one appears in more than one b-roll row, run the reference-sheet procedure, whose step 4 is still untested |

